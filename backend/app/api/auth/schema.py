from app.api.base import SuccessResponse
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: str | None = None


class UserBase(BaseModel):
    name: str
    email: str
    phone: str


class CreateUser(UserBase):
    pass


class CreateUserOutput(CreateUser):
    userID: str


class CreateUserResponse(SuccessResponse):
    data: CreateUserOutput


class UserInDB(UserBase):
    password: str
