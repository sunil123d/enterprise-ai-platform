from uuid import uuid4
from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from langchain_core.messages import (
    HumanMessage,
    AIMessage,
    SystemMessage,
)

from app.database.connection import get_db
from app.models.chat import Chat

from app.schemas.chat_schema import (
    ChatRequest,
    ChatResponse,
    SourceResponse,
)

from app.rag.chain import get_chain
from app.rag.general_chain import get_general_chain

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
    db: Session = Depends(get_db)
):

    print("\n==============================")
    print("QUESTION :", request.question)
    print("DOCUMENTS:", request.documents)
    print("HISTORY  :", request.history)
    print("==============================\n")

    formatted_history = ""

    for item in request.history:
        formatted_history += (
            f"User: {item.question}\n"
            f"Assistant: {item.answer}\n\n"
        )

    sources = []

    # ----------------------------
    # RAG MODE
    # ----------------------------
    if request.documents:

        print(">>>>>>>> USING RAG MODE <<<<<<<<")

        chain = get_chain(request.documents)

        result = chain.invoke(
            {
                "input": request.question,
                "history": formatted_history
            }
        )

        answer = result["answer"]

        for doc in result["context"]:
            sources.append(
                SourceResponse(
                    page=doc.metadata.get("page"),
                    source=doc.metadata.get("source")
                )
            )

    # ----------------------------
    # GENERAL AI MODE
    # ----------------------------
    else:

        print(">>>>>>>> USING GENERAL AI MODE <<<<<<<<")

        llm = get_general_chain()

        messages = [
            SystemMessage(
                content="""
You are Enterprise AI Assistant.

You are helpful, accurate and conversational.

Remember previous conversation.

If the user asks follow-up questions,
use previous messages.

If the topic changes,
start a new conversation naturally.
"""
            )
        ]

        for item in request.history:
            messages.append(
                HumanMessage(content=item.question)
            )
            messages.append(
                AIMessage(content=item.answer)
            )

        messages.append(
            HumanMessage(content=request.question)
        )

        response = llm.invoke(messages)

        answer = response.content

    # ----------------------------
    # Save Chat
    # ----------------------------

    chat = Chat(
        conversation_id=str(uuid4()),
        question=request.question,
        answer=answer,
        created_at=datetime.now()
    )

    db.add(chat)
    db.commit()
    db.refresh(chat)

    return ChatResponse(
        answer=answer,
        sources=sources
    )