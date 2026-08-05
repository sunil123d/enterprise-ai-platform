from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.document_api import router as document_router
from app.api.chat_api import router as chat_router
from app.api.history_api import router as history_router

from app.database.init_db import create_tables


app = FastAPI()


@app.on_event("startup")
async def startup():
    create_tables()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://enterprise-ai-platform-lime.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(document_router)
app.include_router(chat_router)
app.include_router(history_router)