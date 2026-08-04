from sqlalchemy import Column, Integer, String, Boolean

from app.database.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    full_name = Column(String(100), nullable=False)

    email = Column(String(100), unique=True, index=True)

    hashed_password = Column(String(255))

    role = Column(String(30), default="user")

    is_active = Column(Boolean, default=True)