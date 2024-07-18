from app.api.appointments.schema import (
    AppointmentCountsData,
    AppointmentOutputData,
    GetAppointmentData,
    GetSuccessDetails,
)

from app.api.base import SuccessResponse


class CreateAppointmentResponse(SuccessResponse[AppointmentOutputData]):
    """The response for creating an appointment."""

    pass


class GetAppointmentResponse(SuccessResponse[GetAppointmentData]):
    """The response for getting a single appointment."""

    pass


class GetAppointmentSuccessDetailsResponse(SuccessResponse[GetSuccessDetails]):
    """The response for getting the success appointment details."""

    pass


class GetRecentAppointmentsResponse(SuccessResponse[AppointmentCountsData]):
    """The response for getting recent appointments."""

    pass
