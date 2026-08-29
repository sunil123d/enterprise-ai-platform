import requests
from sqlalchemy.orm import Session
from app.models.chat import Chat
import os


RAG_URL = os.getenv(
    "RAG_SERVICE_URL",
    "http://localhost:8001/chat"
)


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

    print("\n========== RAG REQUEST ==========")
    print("RAG URL:", RAG_URL)
    print("QUESTION:", question)
    print("DOCUMENTS:", documents)
    print("HISTORY:", conversation_history)
    print("=================================\n")

    try:

        # Send question + history + selected documents
        response = requests.post(
            RAG_URL,
            json={
                "question": question,
                "history": conversation_history,
                "documents": documents
            },
            timeout=120
        )

        print("RAG STATUS:", response.status_code)
        print("RAG RESPONSE:", response.text)

        if response.status_code != 200:

            print("========== RAG ERROR ==========")
            print("RAG URL:", RAG_URL)
            print("STATUS:", response.status_code)
            print("RESPONSE:", response.text)
            print("================================")

            raise Exception(
                f"RAG Service Error: {response.status_code} - {response.text}"
            )

        result = response.json()

        answer = result["answer"]
        sources = result.get("sources", [])

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

    except requests.exceptions.RequestException as e:

        print("========== RAG CONNECTION ERROR ==========")
        print("RAG URL:", RAG_URL)
        print("ERROR:", str(e))
        print("==========================================")

        raise Exception(f"Cannot connect to RAG Service: {str(e)}")


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