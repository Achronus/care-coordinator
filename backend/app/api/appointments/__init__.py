from app.db import connect
from app.config.settings import settings

from .schema import AppointmentOutputData, CreateAppointment, CreateAppointmentResponse

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
        print(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An appointment already exists with these details.",
        )
