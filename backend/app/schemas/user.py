from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserInDb(UserBase):
    password: str


class UserOut(UserBase):
    id: UUID
    created_at: datetime
    active: bool | None = False

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
