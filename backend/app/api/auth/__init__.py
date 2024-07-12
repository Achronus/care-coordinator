from app.db import connect

from .schema import CreateUser, CreateUserOutput, CreateUserResponse

from appwrite.id import ID
from appwrite.exception import AppwriteException

from fastapi import APIRouter, HTTPException, status


router = APIRouter(prefix="/auth", tags=["Authentication"])


# @router.get(
#     "/user/{user_id}",
#     status_code=status.HTTP_200_OK,
#     response_model=SuccessResponse,
# )
# def get_user(user_id: str):
#     try:
#         result = connect.users.get(user_id)
#         return SuccessResponse(status_code=status.HTTP_200_OK, data=result)

#     except AppwriteException as e:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail=e.message,
#         )


@router.post(
    "/user/register",
    status_code=status.HTTP_201_CREATED,
    # response_model=CreateUserResponse,
)
def create_user(user: CreateUser):
    try:
        result = connect.users.create(
            user_id=ID.unique(),
            **user.model_dump(),
            password=None,
        )
        return CreateUserResponse(
            code=status.HTTP_201_CREATED,
            data=CreateUserOutput(
                userID=result["$id"],
                **result,
            ),
        )

    except AppwriteException as e:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=e.message,
        )
