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
    password: str


class UserInDB(UserBase):
    hashed_password: str
