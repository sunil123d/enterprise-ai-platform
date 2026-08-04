from app.database.connection import engine
from app.database.base import Base

# Import models
import app.models.chat


def create_tables():

    Base.metadata.create_all(bind=engine)