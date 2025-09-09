from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
from datetime import timedelta
import os

router = APIRouter()  


event_data = pd.read_csv("app/Data/final_merged_data.csv", parse_dates=["date"])

class AgencyRequest(BaseModel):
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




@router.post("/agency/{agency_id}")
def predict_agency(agency_id: str, request: AgencyRequest):

    model_path = f"app/models/agencies/agency_{agency_id}.pkl"

    if not os.path.exists(model_path):
        raise HTTPException(status_code=404, detail="Agency model not found")

    model = joblib.load(model_path)

    start_date = pd.to_datetime(request.date_str)
    end_date = pd.to_datetime(request.date_fin)
    delta = end_date - start_date

    results = []

    for i in range(delta.days + 1):
        current_date = start_date + timedelta(days=i)
        events = get_event_data_for_date(current_date)

        input_data = pd.DataFrame([{
            "day": current_date.day,
            "month": current_date.month,
            "weekday": current_date.weekday(),
            "roomType": request.roomType,
            "iseventday": events["iseventday"],
            "vacance_MA": events["vacance_MA"]
        }])

        prediction = model.predict(input_data)[0]
        results.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "roomType": request.roomType,
            "iseventday": bool(events["iseventday"]),
            "vacance_MA": bool(events["vacance_MA"]),
            "booked": int(round(prediction[0])),
            "available": int(round(prediction[1]))
        })

    return results