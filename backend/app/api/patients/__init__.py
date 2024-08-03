from datetime import datetime

from .schema import CreatePatient, PatientOutputData, UploadOutputData
from .response import CreatePatientResponse, PostUploadResponse

from fastapi import APIRouter, File, UploadFile, status

router = APIRouter(prefix="/patient", tags=["Patients"])


@router.post(
    "/upload",
    status_code=status.HTTP_201_CREATED,
    response_model=PostUploadResponse,
    operation_id="PatientUpload",
)
async def upload_file(
    file: UploadFile = File(..., description="The file to upload."),
):
    return PostUploadResponse(
        code=status.HTTP_201_CREATED,
        data=UploadOutputData(
            id="66ae1a620010e1eed7c5",
        ),
    )


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=CreatePatientResponse,
)
async def create_patient(
    patient: CreatePatient = CreatePatient(
        userId="66adf1210015d40e66ee",
        name="John Doe",
        email="johndoe@email.com",
        phone="+447964528921",
        birthDate=datetime(year=1990, month=1, day=1).isoformat(),
        gender="Male",
        address="Non existent lane, England, UK",
        occupation="The man of mystery",
        emergencyContactName="Jane Doe",
        emergencyContactNumber="+447964528921",
        primaryPhysician="66927f7d003c45d3ccf6",
        insuranceProvider="Axa",
        insurancePolicyNumber="ABC123",
        allergies=None,
        currentMedication=None,
        familyMedicalHistory=None,
        identificationType="Driver's License",
        identificationNumber="ABC123",
        identificationDocumentId="<drivers_license_img>",
        treatmentConsent=True,
        disclosureConsent=True,
        privacyConsent=True,
    ),
):
    return CreatePatientResponse(
        code=status.HTTP_201_CREATED,
        data=PatientOutputData(id="66ae1a630027aa57af4d"),
    )
