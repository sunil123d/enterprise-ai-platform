from pydantic import BaseModel


class DocumentResponse(BaseModel):
    filename: str


class DocumentChatRequest(BaseModel):
    document: str
    question: str


from pydantic import BaseModel


class DocumentResponse(BaseModel):
    filename: str


class UploadResponse(BaseModel):
    message: str


class DocumentChatRequest(BaseModel):
    document: str
    question: str