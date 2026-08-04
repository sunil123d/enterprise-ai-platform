from pathlib import Path

import joblib
import pandas as pd
from sqlalchemy.orm import Session

from app.models.prediction import Prediction


def get_prediction_history(
    db: Session,
    user_email: str
):
    return (
        db.query(Prediction)
        .filter(Prediction.user_email == user_email)
        .order_by(Prediction.created_at.desc())
        .all()
    )



MODEL_PATH = Path("app/ml/models/best_model.pkl")

# Load model once
model = joblib.load(MODEL_PATH)


def predict_churn(
    db: Session,
    user_email: str,
    data: dict
):

    df = pd.DataFrame([data])

    prediction = int(model.predict(df)[0])

    probability = float(model.predict_proba(df)[0][1])

    # Save prediction
    prediction_log = Prediction(
        user_email=user_email,
        prediction=prediction,
        probability=probability,
        model_name="XGBoost"
    )

    db.add(prediction_log)
    db.commit()

    return {
        "prediction": prediction,
        "probability": round(probability, 4)
    }