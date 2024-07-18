from typing import Generic, TypeVar
from fastapi import status as fastapiStatus
from pydantic import BaseModel, Field, ValidationInfo, field_validator


T = TypeVar("T", bound=BaseModel)


class BaseSuccessResponse(BaseModel):
    """A base request model for successful API responses. Intended for client responses."""

    status: str = Field(
        default="success",
        frozen=True,
        description="The status of the response. Cannot be changed.",
    )
    code: int = Field(..., description="The HTTP response code.")
    response: str | None = Field(
        default=None,
        frozen=True,
        validate_default=True,
        description="The description for the type of HTTP response. Created dynamically. Cannot be assigned manually.",
    )
    data: BaseModel = Field(..., description="The response data.")
    headers: dict[str, str] | None = Field(
        default=None, description="The headers to send with the response (optional)."
    )

    @field_validator("response")
    def validate_code(cls, _: str, info: ValidationInfo) -> str:
        status_code: int = info.data.get("code")

        for item in fastapiStatus.__all__:
            if str(status_code) in item:
                return item.lstrip("HTTP_")


class ErrorDetails(BaseModel):
    """A details model for error API responses. Intended for client responses using the `HTTPException`."""

    status: str = Field(
        default="error",
        frozen=True,
        description="The status of the response. Cannot be changed.",
    )
    code: int = Field(..., description="The HTTP response code.")
    response: str | None = Field(
        default=None,
        frozen=True,
        validate_default=True,
        description="The description for the type of HTTP response. Created dynamically. Cannot be assigned manually.",
    )
    message: str = Field(..., description="The reason the error occured.")

    @field_validator("response")
    def validate_code(cls, _: str, info: ValidationInfo) -> str:
        status_code: int = info.data.get("code")

        for item in fastapiStatus.__all__:
            if str(status_code) in item:
                return item.lstrip("HTTP_")


class SuccessResponse(BaseSuccessResponse, Generic[T]):
    """A request model for successful API responses. Intended for client responses. Uses generics to change the data model."""

    data: T
