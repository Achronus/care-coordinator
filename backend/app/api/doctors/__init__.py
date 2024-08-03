from typing import Annotated

from .schema import DoctorItem
from .response import DoctorListResponse, GetDoctorResponse


from fastapi import APIRouter, Path, status

router = APIRouter(prefix="/doctor", tags=["Doctors"])


@router.get(
    "/list",
    status_code=status.HTTP_200_OK,
    response_model=DoctorListResponse,
)
def doctors_list():
    return DoctorListResponse(
        code=status.HTTP_200_OK,
        data=[
            DoctorItem(
                name="David Livingston",
                avatarIcon="https://<avataricon>.com/",
                id="66927f7d003c45d3ccf6",
            ),
            DoctorItem(
                name="Jasmine Lee",
                avatarIcon="https://<avataricon>.com/",
                id="66927f96002253a3aebb",
            ),
        ],
    )


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=GetDoctorResponse,
)
def get_doctor(
    id: Annotated[
        str,
        Path(
            ...,
            description="The ID of the appointment. Try using: '66ae1e99000b7ff3f33f'",
        ),
    ],
):
    return GetDoctorResponse(
        code=status.HTTP_200_OK,
        data=DoctorItem(
            name="David Livingston",
            avatarIcon="https://<avataricon>.com/",
            id="66ae1e99000b7ff3f33f",
        ),
    )
