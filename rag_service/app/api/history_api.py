from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import desc

from app.database.connection import get_db
from app.models.chat import Chat

router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("")
def get_history(db: Session = Depends(get_db)):

    chats = db.query(Chat).order_by(
        desc(Chat.id)
    ).all()

    result = []

    for chat in chats:

        result.append(
            {
                "id": chat.id,
                "conversation_id": chat.conversation_id,
                "question": chat.question,
                "answer": chat.answer,
                "created_at": chat.created_at
            }
        )

    return result