from app.api.doctors.schema import DoctorItem
from app.db import connect
from app.config.settings import settings

from .schema import (
    AppointmentOutputData,
    CreateAppointment,
    CreateAppointmentResponse,
    GetAppointmentData,
    GetAppointmentResponse,
    GetAppointmentSuccessDetailsResponse,
    GetSuccessDetails,
)

from appwrite.id import ID
from appwrite.exception import AppwriteException
from appwrite.permission import Permission
from appwrite.role import Role

from fastapi import APIRouter, HTTPException, status


router = APIRouter(prefix="/appointment", tags=["Appointments"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=CreateAppointmentResponse,
)
def create_appointment(appointment: CreateAppointment):
    try:
        response = connect.db.create_document(
            database_id=settings.DB.ID,
            collection_id=settings.DB.APPOINTMENT_COLLECTION_ID,
            document_id=ID.unique(),
            data=appointment.model_dump(),
            permissions=[
                Permission.read(Role.user(id=appointment.userId)),
                Permission.write(Role.user(id=appointment.userId)),
                Permission.read(Role.team(id="admin")),
                Permission.write(Role.team(id="admin")),
            ],
        )

        return CreateAppointmentResponse(
            code=status.HTTP_201_CREATED,
            data=AppointmentOutputData(
                id=response["$id"],
            ),
        )

    except AppwriteException as e:
        print(e.message)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An appointment already exists with these details.",
        )


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=GetAppointmentResponse,
)
def get_appointment(id: str):
    try:
        response = connect.db.get_document(
            database_id=settings.DB.ID,
            collection_id=settings.DB.APPOINTMENT_COLLECTION_ID,
            document_id=id,
        )

        patient = response["patient"]
        doctor = DoctorItem(
            **response["primaryPhysician"],
            id=response["primaryPhysician"]["$id"],
        )
        core_data: dict = response
        core_data.pop("patient")

        data = GetAppointmentData(
            **core_data,
            id=response["$id"],
            doctor=doctor,
            patient=patient["$id"],
        )

        return GetAppointmentResponse(
            code=status.HTTP_200_OK,
            data=data,
        )

    except AppwriteException as e:
        print(e.message)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment doesn't exist.",
        )


@router.get(
    "/{id}/success",
    status_code=status.HTTP_200_OK,
    response_model=GetAppointmentSuccessDetailsResponse,
)
def get_success_details(id: str):
    try:
        response = connect.db.get_document(
            database_id=settings.DB.ID,
            collection_id=settings.DB.APPOINTMENT_COLLECTION_ID,
            document_id=id,
        )

        doctor = DoctorItem(
            **response["primaryPhysician"],
            id=response["primaryPhysician"]["$id"],
        )

        data = GetSuccessDetails(
            id=response["$id"],
            doctor=doctor,
            schedule=response["schedule"],
        )

        return GetAppointmentSuccessDetailsResponse(
            code=status.HTTP_200_OK,
            data=data,
        )

    except AppwriteException as e:
        print(e.message)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment doesn't exist.",
        )
