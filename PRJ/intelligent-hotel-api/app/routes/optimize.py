from fastapi import APIRouter
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
from datetime import timedelta

router = APIRouter()
model = joblib.load("app/models/model_occupancy_pricing_optimizer.pkl")
model_total_available = joblib.load("app/models/model_total_available_rooms.pkl")


event_data = pd.read_csv("app/Data/final_merged_data.csv", parse_dates=["date"])

class OptimizeRequest(BaseModel):
    date_str: str
    date_fin: str
    roomType: int
    occupancy: float

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

@router.post("/optimal")
def recommend(request: OptimizeRequest):
    start_date = pd.to_datetime(request.date_str)
    end_date = pd.to_datetime(request.date_fin)
    delta = end_date - start_date

    results = []

    for i in range(delta.days + 1):
        current_date = start_date + timedelta(days=i)
        events = get_event_data_for_date(current_date)

        input_total_available = pd.DataFrame([{
            "day": current_date.day,
            "month": current_date.month,
            "weekday": current_date.weekday(),
            "roomType": request.roomType,
            "iseventday": events["iseventday"],
            "vacance_MA": events["vacance_MA"]
        }])
        total_available = max(int(model_total_available.predict(input_total_available)[0]), 1)

        taux = request.occupancy
        input_data = pd.DataFrame([{
            "day": current_date.day,
            "month": current_date.month,
            "weekday": current_date.weekday(),
            "roomType": request.roomType,
            "occupancy": taux,
            "iseventday": events["iseventday"],
            "vacance_MA": events["vacance_MA"],
            "total_available": total_available
        }])
        price = model.predict(input_data)[0]
        chambres_occupees = (taux * total_available) / 100
        mean_price = price / chambres_occupees if chambres_occupees > 0 else 0.0

        results.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "iseventday": bool(events["iseventday"]),
            "vacance_MA": bool(events["vacance_MA"]),
            "roomType": request.roomType,
            "total_available": total_available,
            "optimal_occupancy": round(taux, 2),
            "max_total_price": round(price, 2),
            "mean_price_per_room": round(mean_price, 2)
        })

    return results
