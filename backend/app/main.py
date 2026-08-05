from fastapi import FastAPI

from app.core.config import settings
from app.utils.logger import app_logger
from app.database.init_db import create_tables
from app.api.user_api import router as user_router
from app.api.auth_api import router as auth_router
from app.api.prediction_api import router as prediction_router
from app.api.rag_api import router as rag_router
from app.api.chat_api import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.profile_api import router as profile_router


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION
)

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


# Include routers here
app.include_router(chat_router)
app.include_router(user_router)
app.include_router(auth_router)
app.include_router(prediction_router)
app.include_router(rag_router)
app.include_router(profile_router)
@app.on_event("startup")
async def startup():

    app_logger.info("Starting Enterprise AI Platform...")

    create_tables()

    app_logger.info("Database Initialized")


@app.get("/")
def root():

    app_logger.info("Root endpoint accessed")

    return {
        "project": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "message": "Enterprise AI Platform Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }