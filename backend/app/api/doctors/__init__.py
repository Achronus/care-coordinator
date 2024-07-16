from app.db import connect
from app.config.settings import settings

from .schema import DoctorListResponse, ListDoctorItem

from appwrite.exception import AppwriteException

from fastapi import APIRouter, HTTPException, status

router = APIRouter(prefix="/doctor", tags=["Doctors"])


@router.get(
    "/list",
    status_code=status.HTTP_200_OK,
    response_model=DoctorListResponse,
)
def doctors_list():
    try:
        result = connect.db.list_documents(
            database_id=settings.DB.ID,
            collection_id=settings.DB.DOCTOR_COLLECTION_ID,
        )

        data = [
            ListDoctorItem(
                name=item["name"],
                avatarIcon=item["avatarIcon"],
                id=item["$id"],
            )
            for item in result["documents"]
        ]

        return DoctorListResponse(
            code=status.HTTP_200_OK,
            data=data,
        )

    except AppwriteException as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )
