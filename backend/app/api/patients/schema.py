from app.api.base import SuccessResponse

from .enums import Gender, IdentificationTypes

from pydantic import BaseModel, ConfigDict


class File(BaseModel):
    """A model for file delivery."""

    filename: str
    type: str
    size: int
    data: bytes


class PatientBase(BaseModel):
    """A base patient model with common fields."""

    userId: str
    birthDate: str
    gender: Gender
    address: str
    occupation: str
    emergencyContactName: str
    emergencyContactNumber: str
    primaryPhysician: str
    insuranceProvider: str
    insurancePolicyNumber: str
    allergies: str | None = None
    currentMedication: str | None = None
    familyMedicalHistory: str | None = None
    identificationType: IdentificationTypes | None = None
    identificationNumber: str | None = None
    identificationDocument: File | None = None
    treatmentConsent: bool
    disclosureConsent: bool
    privacyConsent: bool

    model_config = ConfigDict(use_enum_values=True)


class CreatePatient(PatientBase):
    """A model for creating a patient."""

    pass


class CreatePatientResponse(SuccessResponse):
    """A response model for creating a patient."""

    pass
