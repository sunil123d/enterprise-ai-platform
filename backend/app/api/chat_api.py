from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.connection import get_db
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.chat_service import ask_rag
from app.services.current_user_service import get_user_by_email
from app.core.dependencies import get_current_user
from fastapi import APIRouter, Depends, HTTPException

from app.services.chat_service import (
    ask_rag,
    get_chat_history,
    delete_chat
)

from typing import List

from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse,
    ChatHistoryResponse
)

from app.services.chat_service import (
    ask_rag,
    get_chat_history
)

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)


@router.post(
    "",
    response_model=ChatResponse
)
def chat(
    request: ChatRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_user_by_email(
        db,
        current_user["sub"]
    )

    return ask_rag(
        db=db,
        user_id=user.id,
        question=request.question,
        documents=request.documents
    )
@router.get(
    "/history",
    response_model=List[ChatHistoryResponse]
)
def history(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):
    user = get_user_by_email(
        db,
        current_user["sub"]
    )

    return get_chat_history(
        db,
        user.id
    )

@router.delete("/{chat_id}")
def remove_chat(
    chat_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    user = get_user_by_email(
        db,
        current_user["sub"]
    )

    deleted = delete_chat(
        db=db,
        user_id=user.id,
        chat_id=chat_id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Chat not found"
        )

    return {
        "message": "Chat deleted successfully"
    }