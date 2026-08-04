from pathlib import Path

from fastapi import APIRouter
import shutil
from app.rag.vectorstore import load_db

from app.schemas.document_schema import (
    DocumentResponse,
    DocumentChatRequest,
)

from app.schemas.chat_schema import (
    ChatResponse,
    SourceResponse,
)

from fastapi import UploadFile, File, HTTPException

from app.schemas.document_schema import (
    DocumentResponse,
    DocumentChatRequest,
    UploadResponse,
)

from app.rag.ingest import ingest

from app.rag.document_chain import get_document_chain

router = APIRouter(tags=["Documents"])

UPLOAD_DIR = Path("app/uploads")

@router.post(
    "/documents/upload",
    response_model=UploadResponse
)
async def upload_document(
    file: UploadFile = File(...)
):

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    UPLOAD_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    file_path = UPLOAD_DIR / file.filename

    with open(file_path, "wb") as f:
        f.write(await file.read())

    ingest(str(file_path))

    return UploadResponse(
        message="Document uploaded successfully."
    )


@router.get(
    "/documents",
    response_model=list[DocumentResponse]
)
def list_documents():

    files = []

    for file in UPLOAD_DIR.glob("*.pdf"):
        files.append(
            DocumentResponse(
                filename=file.name
            )
        )

    return files

@router.delete("/documents/{filename}")
def delete_document(filename: str):

    file_path = UPLOAD_DIR / filename

    if not file_path.exists():
        raise HTTPException(
            status_code=404,
            detail="Document not found."
        )

    # Delete PDF file
    file_path.unlink()

    # Remove vectors from Chroma
    db = load_db()

    docs = db.get()

    ids_to_delete = []

    for i in range(len(docs["ids"])):

        source = docs["metadatas"][i].get("source", "")

        if source.endswith(filename):
            ids_to_delete.append(docs["ids"][i])

    if ids_to_delete:
        db.delete(ids=ids_to_delete)

    return {
        "message": "Document deleted successfully."
    }

@router.post(
    "/chat/document",
    response_model=ChatResponse
)
def chat_with_document(request: DocumentChatRequest):

    chain = get_document_chain(request.document)

    result = chain.invoke(
        {
            "input": request.question
        }
    )

    sources = []

    for doc in result["context"]:
        sources.append(
            SourceResponse(
                page=doc.metadata.get("page"),
                source=doc.metadata.get("source")
            )
        )

    return ChatResponse(
        answer=result["answer"],
        sources=sources
    )