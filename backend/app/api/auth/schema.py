from app.api.base import SuccessResponse
from fastapi import Query
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    """A base user model with common fields."""

    name: str = Field(Query(..., description="The name of the user."))
    email: str = Field(Query(..., description="The email of the user."))
    phone: str = Field(Query(..., description="The contact number of the user."))


class CreateUser(UserBase):
    """A user model for creating a user."""

    pass


class CoreUserOutput(BaseModel):
    """The user details output."""

    userID: str = Field(..., description="The ID of the user.")
    name: str = Field(..., description="The name of the user.")
    email: str = Field(..., description="The email of the user.")
    phone: str = Field(..., description="The contact number of the user.")


class UserResponse(SuccessResponse):
    """The response received by creating and retrieving the user."""

    data: CoreUserOutput


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    name: str | None = None


class UserInDB(UserBase):
    password: str
