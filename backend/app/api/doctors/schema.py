from app.api.base import SuccessResponse
from pydantic import BaseModel


class DoctorBase(BaseModel):
    """A base doctor model with common fields."""

    name: str


class DoctorItem(DoctorBase):
    """A data model for a single doctor item."""

    avatarIcon: str
    id: str


class DoctorListResponse(SuccessResponse):
    """A response for getting a list of doctors."""

    data: list[DoctorItem]


class GetDoctorResponse(SuccessResponse):
    """A response for getting a single doctor."""

    data: DoctorItem
