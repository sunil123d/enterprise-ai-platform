from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.models.user import User

router = APIRouter(
    prefix="/profile",
    tags=["Profile"]
)


@router.get("")
def get_profile(db: Session = Depends(get_db)):

    # Temporary: first user
    user = db.query(User).first()

    if not user:
        return {
            "message": "User not found"
        }

    return {
        "id": user.id,
        "full_name": user.full_name,
        "email": user.email,
        "role": user.role,
        "is_active": user.is_active
    }