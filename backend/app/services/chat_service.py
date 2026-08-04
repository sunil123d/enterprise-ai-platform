import requests
from sqlalchemy.orm import Session

from app.models.chat import Chat

RAG_URL = "http://localhost:8001/chat"


def ask_rag(
    db: Session,
    user_id: int,
    question: str,
    documents: list[str] = []
):

    # Fetch last 5 chats for conversation memory
    history = (
        db.query(Chat)
        .filter(Chat.user_id == user_id)
        .order_by(Chat.id.desc())
        .limit(5)
        .all()
    )

    # Convert to chronological order
    conversation_history = []

    for chat in reversed(history):
        conversation_history.append(
            {
                "question": chat.question,
                "answer": chat.answer
            }
        )

    # Send question + history + selected documents
    response = requests.post(
        RAG_URL,
        json={
            "question": question,
            "history": conversation_history,
            "documents": documents
        }
    )

    if response.status_code != 200:
        raise Exception("RAG Service Not Available")

    result = response.json()

    answer = result["answer"]
    sources = result["sources"]

    # Save current chat
    chat = Chat(
        user_id=user_id,
        question=question,
        answer=answer
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return {
        "answer": answer,
        "sources": sources
    }


def delete_chat(
    db: Session,
    user_id: int,
    chat_id: int
):
    chat = (
        db.query(Chat)
        .filter(
            Chat.id == chat_id,
            Chat.user_id == user_id
        )
        .first()
    )

    if chat is None:
        return False

    db.delete(chat)
    db.commit()

    return True


def get_chat_history(
    db: Session,
    user_id: int
):

    chats = (
        db.query(Chat)
        .filter(Chat.user_id == user_id)
        .order_by(Chat.id.desc())
        .all()
    )

    return chats