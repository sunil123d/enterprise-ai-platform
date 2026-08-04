from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "Enterprise AI Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    GROQ_API_KEY: str = ""

    OLLAMA_MODEL: str = "llama3.2"

    DATABASE_URL: str = "sqlite:///./enterprise.db"

    SECRET_KEY: str = ""

    CHROMA_DB: str = "app/chroma_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )
settings = Settings()
