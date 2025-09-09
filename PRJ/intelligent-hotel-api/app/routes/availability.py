from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import joblib
from datetime import timedelta

router = APIRouter()


model = joblib.load("app/models/model_total_available_rooms.pkl")


event_data = pd.read_csv("app/Data/final_merged_data.csv", parse_dates=["date"])

class AvailabilityRequest(BaseModel):
    date_str: str
    date_fin: str
    roomType: int

def get_event_data_for_date(date):

    row = event_data[event_data["date"] == pd.to_datetime(date)]
    if not row.empty:
        return {
            "vacance_MA": int(row.iloc[0]["vacance_MA"]),
            "iseventday": int(row.iloc[0]["iseventday"])
        }
    return {
        "vacance_MA": 0,
        "iseventday": 0
    }

@router.post("/availability")
def predict_total_available(request: AvailabilityRequest):
    date_str = pd.to_datetime(request.date_str)
    date_fin = pd.to_datetime(request.date_fin)

    if date_fin < date_str:
        return {"error": "La date de fin doit être postérieure ou égale à la date de début"}

    delta = date_fin - date_str

    input_data = []
    result = []

    for i in range(delta.days + 1):
        current_date = date_str + timedelta(days=i)
        events = get_event_data_for_date(current_date)
        input_data.append({
            "day": current_date.day,
            "month": current_date.month,
            "weekday": current_date.weekday(),
            "roomType": request.roomType,
            "iseventday": events["iseventday"],
            "vacance_MA": events["vacance_MA"]
        })

    input_df = pd.DataFrame(input_data)
    
    expected_columns = ["day", "month", "weekday", "roomType", "iseventday", "vacance_MA"]
    input_df = input_df[expected_columns]

    predictions = model.predict(input_df)

    for i in range(len(predictions)):
        current_date = date_str + timedelta(days=i)
        result.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "total_available_predicted": int(round(predictions[i])),
            "iseventday": bool(input_data[i]["iseventday"]),
            "vacance_MA": bool(input_data[i]["vacance_MA"]),
            "roomType": request.roomType
        })

    return result