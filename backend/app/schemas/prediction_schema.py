from pydantic import BaseModel


from datetime import datetime


class PredictionHistoryResponse(BaseModel):
    prediction: int
    probability: float
    model_name: str
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class ChurnPredictionRequest(BaseModel):

    gender: int
    SeniorCitizen: int
    Partner: int
    Dependents: int
    tenure: int
    PhoneService: int
    MultipleLines: int
    InternetService: int
    OnlineSecurity: int
    OnlineBackup: int
    DeviceProtection: int
    TechSupport: int
    StreamingTV: int
    StreamingMovies: int
    Contract: int
    PaperlessBilling: int
    PaymentMethod: int
    MonthlyCharges: float
    TotalCharges: float


class ChurnPredictionResponse(BaseModel):

    prediction: int
    probability: float