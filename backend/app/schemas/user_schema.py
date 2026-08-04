from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


from pydantic import BaseModel, ConfigDict

class UserResponse(BaseModel):

    ...

    model_config = ConfigDict(
        from_attributes=True
    )