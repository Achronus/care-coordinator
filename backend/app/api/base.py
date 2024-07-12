from enum import StrEnum

from fastapi import status as fastapiStatus
from pydantic import BaseModel, Field, ValidationInfo, field_validator


class Status(StrEnum):
    SUCCESS = "success"
    ERROR = "error"


class SuccessResponse(BaseModel):
    """
    A base model for success API responses. Intended for client responses.

    Parameters:
    - `statusCode` (`integer`) - the HTTP response code for the request
    - `data` (`pydantic.BaseModel`) - a Pydantic model containing the data response
    - `headers` (`dict[str, str], optional`) - an optional set of headers to send with the response. `None` by default
    - `status` (`string, frozen`) - the status of the response. Always `success`. Cannot be changed
    - `response` (`string, frozen`) - a string representation of the HTTP response code. Dynamically populated based on the `statusCode` value. Cannot be assigned manually
    """

    status: Status = Field(default="success", frozen=True)
    statusCode: int
    response: str | None = Field(default=None, frozen=True, validate_default=True)
    data: BaseModel
    headers: dict[str, str] | None = None

    @field_validator("response")
    def validate_code(cls, _: str, info: ValidationInfo) -> str:
        status_code: int = info.data.get("statusCode")

        for item in fastapiStatus.__all__:
            if str(status_code) in item:
                return item.lstrip("HTTP_")


class ErrorDetails(BaseModel):
    """
    A base model for error API responses. Intended for client responses using the `HTTPException`.

    Parameters:
    - `statusCode` (`integer | fastapi.status`) - the HTTP response code for the request
    - `message` (`string`) - a string of text explaining the response error
    - `status` (`string, frozen`) - the status of the response. Always `success`. Cannot be changed
    - `response` (`string, frozen`) - a string representation of the HTTP response code. Dynamically populated based on the `statusCode` value. Cannot be assigned manually
    """

    status: Status = Field(default="error", frozen=True)
    statusCode: int
    response: str | None = Field(default=None, frozen=True, validate_default=True)
    message: str

    @field_validator("response")
    def validate_code(cls, _: str, info: ValidationInfo) -> str:
        status_code: int = info.data.get("statusCode")

        for item in fastapiStatus.__all__:
            if str(status_code) in item:
                return item.lstrip("HTTP_")
