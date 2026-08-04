from fastapi import APIRouter

from app.schemas.rag_schema import RagRequest
from app.services.rag_service import ask_rag

router = APIRouter(
    prefix="/assistant",
    tags=["AI Assistant"]
)


@router.post("/chat")
async def chat(request: RagRequest):

    return await ask_rag(
        request.question
    )