from typing import Generic, TypeVar

from .messages import build_response

from pydantic import BaseModel, Field, ValidationInfo, field_validator


T = TypeVar("T", bound=BaseModel)


class BaseResponse(BaseModel):
    """A base request model for API responses. Intended for client responses."""

    status: str = Field(
        ...,
        description="The status of the response.",
    )
    code: int = Field(..., description="The HTTP response code.")
    response: str | None = Field(
        default=None,
        frozen=True,
        validate_default=True,
        description="The description for the type of HTTP response. Created dynamically. Cannot be assigned manually.",
    )

    @field_validator("response")
    def validate_code(cls, _: str, info: ValidationInfo) -> str:
        code: int = info.data.get("code")
        return build_response(code)


class BaseSuccessResponse(BaseResponse):
    """A base request model for successful API responses. Intended for client responses."""

    status: str = Field(
        default="success",
        frozen=True,
        description="The status of the response. Cannot be changed.",
    )
    data: BaseModel = Field(..., description="The response data.")
    headers: dict[str, str] | None = Field(
        default=None, description="The headers to send with the response (optional)."
    )


class MessageResponse(BaseResponse):
    """A message response model for API responses. Intended for client responses."""

    message: str = Field(..., description="The reason the response occured.")
    headers: dict[str, str] | None = Field(
        default=None, description="The headers to send with the response (optional)."
    )


class ErrorResponse(MessageResponse):
    """An error response model. Intended for client responses."""

    status: str = Field(
        default="error",
        frozen=True,
        description="The status of the response. Cannot be changed.",
    )


class SuccessResponse(BaseSuccessResponse, Generic[T]):
    """A success response model. Intended for client responses. Uses generics to change the data model."""

    data: T
