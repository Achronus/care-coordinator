from app.db import connect
from app.config.settings import settings

from .schema import DoctorListResponse, DoctorItem, GetDoctorResponse

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
            DoctorItem(
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


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=GetDoctorResponse,
)
def get_doctor(id: str):
    try:
        result = connect.db.get_document(
            database_id=settings.DB.ID,
            collection_id=settings.DB.DOCTOR_COLLECTION_ID,
            document_id=id,
        )

        data = DoctorItem(
            name=result["name"],
            avatarIcon=result["avatarIcon"],
            id=result["$id"],
        )

        return GetDoctorResponse(
            code=status.HTTP_200_OK,
            data=data,
        )

    except AppwriteException as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Doctor doesn't exist.",
        )
