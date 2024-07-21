from . import MessageResponse

from pydantic import BaseModel, Field, field_validator, validate_call
from fastapi import status


@validate_call
def build_response(code: int, no_strip: bool = False) -> str:
    """A utility function for building a string representation of a response code."""
    for item in status.__all__:
        if str(code) in item:
            if no_strip:
                return item

            return item.lstrip("HTTP_")

    raise ValueError(
        f"'{code}' isn't a valid HTTP response code! Try 'fastapi.status' for a list of valid response codes"
    )


@validate_call
def get_code_status(code: int) -> str:
    """A utility function for retrieving the code status based on the code."""
    # Validate code exists
    _ = build_response(code)

    code_type_map = {
        "info": range(100, 200),
        "success": range(200, 300),
        "redirect": range(300, 400),
        "error": range(400, 600),
    }

    for key, code_range in code_type_map.items():
        if code in code_range:
            return key


class HTTPMessage(BaseModel):
    """A model for HTTP messages."""

    code: int = Field(..., description="The HTTP response code.")
    message: str = Field(..., description="The reason the response occured.")
    headers: dict[str, str] | None = Field(
        default=None, description="The headers to send with the response (optional)."
    )

    @field_validator("headers")
    def validate_headers(cls, headers: dict[str, str] | None) -> dict:
        if headers is None:
            return {}

        return headers


@validate_call
def msg_response_model(model: HTTPMessage) -> dict:
    """A utility function for building message response schemas."""
    response = build_response(model.code)
    status = get_code_status(model.code)

    return {
        model.code: {
            "model": MessageResponse,
            "content": {
                "application/json": {
                    "example": {
                        "status": status,
                        "code": model.code,
                        "response": response,
                        "message": model.message,
                        "headers": model.headers,
                    }
                }
            },
        }
    }


HTTP_404_MSG = HTTPMessage(
    code=status.HTTP_404_NOT_FOUND,
    message="The requested resource could not be found. Please check the endpoint URL and try again.",
)

HTTP_409_MSG = HTTPMessage(
    code=status.HTTP_409_CONFLICT,
    message="There is a conflict with the current state of the resource. Please review your request for any conflicts and try again.",
)

HTTP_ERROR_404 = msg_response_model(HTTP_404_MSG)
HTTP_ERROR_409 = msg_response_model(HTTP_409_MSG)
