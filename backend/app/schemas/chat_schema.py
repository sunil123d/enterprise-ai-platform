from pydantic import BaseModel


class HistoryItem(BaseModel):
    question: str
    answer: str


class ChatRequest(BaseModel):
    question: str
    history: list[HistoryItem] = []
    documents: list[str] = []


class SourceResponse(BaseModel):
    page: int | None = None
    source: str | None = None


class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceResponse] = []


class ChatHistoryResponse(BaseModel):
    id: int
    question: str
    answer: str

    class Config:
        from_attributes = True