from .schema import CreateUser, CoreUserOutput, UserResponse


from fastapi import APIRouter, status
from zentra_api.responses import get_response_models

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/user/register",
    status_code=status.HTTP_201_CREATED,
    response_model=UserResponse,
    responses=get_response_models(409),
)
def create_user(
    user: CreateUser = CreateUser(
        name="John Doe",
        email="johndoe@email.com",
        phone="+447964528921",
    ),
):
    return UserResponse(
        code=status.HTTP_201_CREATED,
        data=CoreUserOutput(
            name="John Doe",
            email="johndoe@email.com",
            phone="+447964528921",
            userID="66adf1210015d40e66ee",
        ),
    )
