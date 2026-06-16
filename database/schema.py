from pydantic import BaseModel
from datetime import datetime

class UserBaseSchema(BaseModel):
    username: str

class UserCreateSchema(UserBaseSchema):
    password: str

class UserResponseSchema(UserBaseSchema):
    id: int
    created_at: datetime