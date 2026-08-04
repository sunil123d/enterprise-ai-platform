from fastapi import APIRouter
from fastapi import Depends
from app.core.dependencies import get_current_user
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from app.schemas.prediction_schema import PredictionHistoryResponse
from app.services.prediction_service import get_prediction_history

from app.database.connection import get_db

from app.schemas.prediction_schema import (
    ChurnPredictionRequest,
    ChurnPredictionResponse,
)

from app.services.prediction_service import predict_churn

router = APIRouter(
    prefix="/predict",
    tags=["Prediction"]
)


@router.post(
    "/churn",
    response_model=ChurnPredictionResponse
)
def predict(
    request: ChurnPredictionRequest,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    return predict_churn(
    db=db,
    user_email=current_user["sub"],
    data=request.model_dump()
)

@router.get(
    "/history",
    response_model=List[PredictionHistoryResponse]
)
def history(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return get_prediction_history(
        db,
        current_user
    )