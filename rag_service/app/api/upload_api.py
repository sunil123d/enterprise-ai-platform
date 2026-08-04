from pathlib import Path
import shutil

from fastapi import APIRouter, UploadFile, File, HTTPException

from app.schemas.upload_schema import UploadResponse
from app.rag.ingest import ingest

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@router.post(
    "",
    response_model=UploadResponse
)
def upload_pdf(
    file: UploadFile = File(...)
):

    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    save_path = UPLOAD_DIR / file.filename

    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest(str(save_path))

    return UploadResponse(
        message="Document uploaded successfully.",
        filename=file.filename
    )