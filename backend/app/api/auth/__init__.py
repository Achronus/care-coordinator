from .schema import CreateUser
from app.db import connect

from appwrite.id import ID
from appwrite.exception import AppwriteException

from fastapi import APIRouter, HTTPException, status


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/user/{user_id}")
def get_user(user_id: str):
    try:
        result = connect.users.get(user_id)
    except AppwriteException as e:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=e)

    return result


@router.post("/sign-in", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser):
    try:
        result = connect.users.create(user_id=ID.unique(), **user.model_dump())
    except AppwriteException as e:
        return HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=e)

    return result
