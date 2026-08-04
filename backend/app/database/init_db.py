from app.database.connection import engine
from app.database.base import Base
from app.models.chat import Chat


# Import all models here
from app.models.user import User
from app.models.prediction import Prediction


def create_tables():
    Base.metadata.create_all(bind=engine)