from datetime import datetime
from typing import Annotated

from app.api.patients.schema import PatientItem

from app.api.doctors.schema import DoctorItem

from .schema import (
    CancelAppointment,
    AppointmentCountsData,
    AppointmentItemData,
    AppointmentIdData,
    CreateAppointment,
    GetAppointmentData,
    GetSuccessDetails,
    ScheduleAppointment,
)

from .response import (
    GetAppointmentResponse,
    GetAppointmentSuccessDetailsResponse,
    GetRecentAppointmentsResponse,
    AppointmentIdResponse,
)


from fastapi import APIRouter, Path, status
from zentra_api.responses import get_response_models

router = APIRouter(prefix="/appointment", tags=["Appointments"])


@router.post(
    "/create",
    status_code=status.HTTP_201_CREATED,
    response_model=AppointmentIdResponse,
    responses=get_response_models(409),
)
def create_appointment(
    appointment: CreateAppointment = CreateAppointment(
        reason="I'm in need of a checkup.",
        notes="I've been doing a lot of running lately!",
        schedule=datetime(year=2024, month=8, day=16, hour=13, minute=30).isoformat(),
        status="pending",
        patient="66ae1a630027aa57af4d",
        userId="66adf1210015d40e66ee",
        primaryPhysician="66927f7d003c45d3ccf6",
        cancellationReason=None,
    ),
):
    return AppointmentIdResponse(
        code=status.HTTP_201_CREATED,
        data=AppointmentIdData(
            id="66ae1e99000b7ff3f33f",
        ),
    )


@router.get(
    "/list",
    status_code=status.HTTP_200_OK,
    response_model=GetRecentAppointmentsResponse,
    responses=get_response_models(404),
)
def get_recent_appointments():
    data = AppointmentCountsData(
        scheduledCount=0,
        pendingCount=1,
        cancelledCount=0,
        appointments=[
            AppointmentItemData(
                id="66ae1e99000b7ff3f33f",
                reason="I'm in need of a checkup.",
                notes="I've been doing a lot of running lately!",
                schedule=datetime(
                    year=2024, month=8, day=16, hour=13, minute=30
                ).isoformat(),
                status="pending",
                patient=PatientItem(
                    id="66ae1a630027aa57af4d",
                    name="John Doe",
                ),
                userId="66adf1210015d40e66ee",
                physician=DoctorItem(
                    id="66927f7d003c45d3ccf6",
                    name="David Livingston",
                    avatarIcon="https://<avatarurl>.com/",
                ),
            )
        ],
    )

    return GetRecentAppointmentsResponse(
        code=status.HTTP_200_OK,
        data=data,
    )


@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=GetAppointmentResponse,
    responses=get_response_models(404),
)
def get_appointment(
    id: Annotated[
        str,
        Path(
            ...,
            description="The ID of the appointment. Try using: '66ae1e99000b7ff3f33f'",
        ),
    ],
):
    return GetAppointmentResponse(
        code=status.HTTP_200_OK,
        data=GetAppointmentData(
            id="66ae1e99000b7ff3f33f",
            reason="I'm in need of a checkup.",
            notes="I've been doing a lot of running lately!",
            schedule=datetime(
                year=2024, month=8, day=16, hour=13, minute=30
            ).isoformat(),
            status="pending",
            patient="66ae1a630027aa57af4d",
            userId="66adf1210015d40e66ee",
            doctor=DoctorItem(
                id="66927f7d003c45d3ccf6",
                name="David Livingston",
                avatarIcon="https://<avatarurl>.com/",
            ),
            cancellationReason=None,
        ),
    )


@router.get(
    "/{id}/success",
    status_code=status.HTTP_200_OK,
    response_model=GetAppointmentSuccessDetailsResponse,
    responses=get_response_models(404),
)
def get_success_details(
    id: Annotated[
        str,
        Path(
            ...,
            description="The ID of the appointment. Try using: '66ae1e99000b7ff3f33f'",
        ),
    ],
):
    return GetAppointmentSuccessDetailsResponse(
        code=status.HTTP_200_OK,
        data=GetSuccessDetails(
            id="66ae1e99000b7ff3f33f",
            doctor=DoctorItem(
                id="66927f7d003c45d3ccf6",
                name="David Livingston",
                avatarIcon="https://<avatarurl>.com/",
            ),
            schedule=datetime(
                year=2024, month=8, day=16, hour=13, minute=30
            ).isoformat(),
        ),
    )


@router.patch(
    "/cancel",
    status_code=status.HTTP_200_OK,
    response_model=AppointmentIdResponse,
    responses=get_response_models(404),
)
def cancel_appointment(
    details: CancelAppointment = CancelAppointment(
        id="66ae1e99000b7ff3f33f",
        cancellationReason="Something else came up, I can't make it. Sorry!",
        status="cancelled",
    ),
):
    return AppointmentIdResponse(
        code=status.HTTP_200_OK,
        data=AppointmentIdData(id="66ae1e99000b7ff3f33f"),
    )


@router.patch(
    "/schedule",
    status_code=status.HTTP_200_OK,
    response_model=AppointmentIdResponse,
    responses=get_response_models(404),
)
def schedule_appointment(
    details: ScheduleAppointment = ScheduleAppointment(
        id="66ae1e99000b7ff3f33f",
        primaryPhysician="66927f7d003c45d3ccf6",
        reason="I'm in need of a checkup.",
        notes="I've been doing a lot of running lately! ",
        schedule=datetime(year=2024, month=8, day=16, hour=13, minute=30).isoformat(),
        status="scheduled",
    ),
):
    return AppointmentIdResponse(
        code=status.HTTP_200_OK,
        data=AppointmentIdData(id="66ae1e99000b7ff3f33f"),
    )
