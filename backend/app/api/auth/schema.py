from app.api.base import SuccessResponse
from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: str | None = None


class UserBase(BaseModel):
    """A base user model with common fields."""

    name: str
    email: str
    phone: str


class CreateUser(UserBase):
    """A user model for creating a user."""

    pass


class CoreUserOutput(UserBase):
    """A data model for storing the core user details."""

    userID: str


class CoreUserResponse(SuccessResponse):
    """A response model for creating and retrieving the user."""

    data: CoreUserOutput


class UserInDB(UserBase):
    password: str
