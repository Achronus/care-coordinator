from datetime import datetime

from app.api.appointments.enums import Status
from app.api.base import SuccessResponse
from app.api.doctors.schema import DoctorItem

from pydantic import BaseModel, ConfigDict, Field, field_validator


class AppointmentBase(BaseModel):
    """A base model for common appointment fields."""

    reason: str = Field(..., description="The reason for the appointment.")
    notes: str = Field(..., description="Additional notes related to the appointment.")
    schedule: datetime = Field(
        ...,
        description="The date and time of the appointment. Format: dd/mm/yyyy, hh:mm:ss",
    )
    status: Status = Field(..., description="The status of the appointment.")
    cancellationReason: str | None = Field(
        None, description="The reason for cancelling the appointment (optional)."
    )
    patient: str = Field(
        ..., description="The ID of the patient assigned to the appointment."
    )
    userId: str = Field(
        ..., description="The ID of the user assigned to the appointment."
    )

    model_config = ConfigDict(use_enum_values=True)

    @field_validator("schedule")
    def validate_schedule(cls, schedule: datetime) -> str:
        return schedule.isoformat()


class CreateAppointment(AppointmentBase):
    """A model for creating an appointment."""

    primaryPhysician: str = Field(
        ..., description="The ID of the doctor assigned to the appointment."
    )


class AppointmentOutputData(BaseModel):
    """The output data for the created appointment."""

    id: str = Field(..., description="The id of the created appointment.")


class CreateAppointmentResponse(SuccessResponse):
    """The response for creating an appointment."""

    data: AppointmentOutputData


class GetAppointmentData(AppointmentBase, AppointmentOutputData):
    """The output data for getting a single appointment."""

    doctor: DoctorItem = Field(
        ..., description="The details of the doctor assigned to the appointment."
    )
    schedule: str | datetime = Field(
        ...,
        description="The date and time of the appointment. Format required: ISO.",
    )

    @field_validator("schedule")
    def validate_schedule(cls, schedule: str | datetime) -> datetime:
        if isinstance(schedule, str):
            return datetime.fromisoformat(schedule)

        return datetime.fromisoformat(schedule.isoformat())


class GetAppointmentResponse(SuccessResponse):
    """The response for getting a single appointment."""

    data: GetAppointmentData


class GetSuccessDetails(AppointmentOutputData):
    """The output data for successfully getting the success appointment details."""

    doctor: DoctorItem = Field(
        ..., description="The details of the doctor assigned to the appointment."
    )
    schedule: str | datetime = Field(
        ...,
        description="The date and time of the appointment. Format required: ISO.",
    )

    @field_validator("schedule")
    def validate_schedule(cls, schedule: str | datetime) -> datetime:
        if isinstance(schedule, str):
            return datetime.fromisoformat(schedule)

        return datetime.fromisoformat(schedule.isoformat())


class GetAppointmentSuccessDetailsResponse(SuccessResponse):
    """The response for getting the success appointment details."""

    data: GetSuccessDetails
