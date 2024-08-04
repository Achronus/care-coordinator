from typing import Annotated

from app.api.appointments.response import GetRecentAppointmentsResponse
from app.api.appointments.schema import AppointmentCountsData, AppointmentItemData
from app.api.patients.schema import PatientItem
from app.api.responses.messages import HTTP_ERROR_404
from app.db import get_appointment_db, get_doctor_db
from app.db.crud import CRUD

from app.api.doctors.schema import DoctorItem
from app.api.doctors.response import DoctorListResponse

from appwrite.exception import AppwriteException
from appwrite.query import Query
from fastapi import APIRouter, Depends, status, HTTPException


router = APIRouter(prefix="/retrieval", tags=None)


@router.get(
    "/doctor/list",
    status_code=status.HTTP_200_OK,
    response_model=DoctorListResponse,
)
def doctors_list(db: Annotated[CRUD, Depends(get_doctor_db)]):
    try:
        response = db.get_multiple()

        data = [
            DoctorItem(
                name=item["name"],
                avatarIcon=item["avatarIcon"],
                id=item["$id"],
            )
            for item in response["documents"]
        ]

        return DoctorListResponse(
            code=status.HTTP_200_OK,
            data=data,
        )

    except AppwriteException as e:
        print(e.message)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=e.message,
        )


@router.get(
    "/appointment/list",
    status_code=status.HTTP_200_OK,
    response_model=GetRecentAppointmentsResponse,
    responses=HTTP_ERROR_404,
)
def get_recent_appointments(db: Annotated[CRUD, Depends(get_appointment_db)]):
    try:
        appointments = db.get_multiple(queries=[Query.order_desc("$createdAt")])
        scheduled = db.get_multiple(
            queries=[
                Query.equal("status", "scheduled"),
                Query.select("$id"),
            ]
        )
        pending = db.get_multiple(
            queries=[
                Query.equal("status", "pending"),
                Query.select("$id"),
            ]
        )
        cancelled = db.get_multiple(
            queries=[
                Query.equal("status", "cancelled"),
                Query.select("$id"),
            ]
        )

        appointments = [
            AppointmentItemData(
                id=appointment["$id"],
                reason=appointment["reason"],
                notes=appointment["notes"],
                schedule=appointment["schedule"],
                status=appointment["status"],
                cancellationReason=appointment["cancellationReason"],
                userId=appointment["userId"],
                patient=PatientItem(
                    id=appointment["patient"]["$id"],
                    name=appointment["patient"]["name"],
                ),
                physician=DoctorItem(
                    id=appointment["primaryPhysician"]["$id"],
                    name=appointment["primaryPhysician"]["name"],
                    avatarIcon=appointment["primaryPhysician"]["avatarIcon"],
                ),
            )
            for appointment in appointments["documents"]
        ]

        data = AppointmentCountsData(
            scheduledCount=len(scheduled["documents"]),
            pendingCount=len(pending["documents"]),
            cancelledCount=len(cancelled["documents"]),
            appointments=appointments,
        )

        return GetRecentAppointmentsResponse(
            code=status.HTTP_200_OK,
            data=data,
        )

    except AppwriteException as e:
        print(e.message)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointments cannot be found.",
        )
