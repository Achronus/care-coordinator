from app.api.base import SuccessResponse
from pydantic import BaseModel


class DoctorBase(BaseModel):
    """A base doctor model with common fields."""

    name: str


class ListDoctorItem(DoctorBase):
    """A data model for storing a single doctor list item."""

    avatarIcon: str
    id: str


class DoctorListResponse(SuccessResponse):
    """A response model for returning a list of doctors."""

    data: list[ListDoctorItem]
