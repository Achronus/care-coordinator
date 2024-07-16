from app.db import connect
from app.config.settings import settings

from .schema import (
    CreatePatient,
    CreatePatientResponse,
    PatientOutputData,
    PostUploadResponse,
    UploadOutputData,
)

from appwrite.exception import AppwriteException
from appwrite.permission import Permission
from appwrite.role import Role
from appwrite.id import ID
from appwrite.input_file import InputFile

from fastapi import APIRouter, File, HTTPException, UploadFile, status

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
    try:
        content = await file.read()

        response = connect.storage.create_file(
            bucket_id=settings.DB.BUCKET_ID,
            file_id=ID.unique(),
            file=InputFile.from_bytes(bytes=content, filename=file.filename),
            permissions=[
                Permission.read(Role.team(id="admin")),
                Permission.write(Role.team(id="admin")),
            ],
        )

        return PostUploadResponse(
            code=status.HTTP_201_CREATED,
            data=UploadOutputData(
                id=response["$id"],
            ),
        )

    except AppwriteException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=e.message,
        )


@router.post(
    "/register",
    status_code=status.HTTP_201_CREATED,
    response_model=CreatePatientResponse,
)
def create_patient(patient: CreatePatient):
    try:
        file_id = patient.identificationDocumentId
        url = f"{settings.DB.ENDPOINT_URL}/storage/buckets/{settings.DB.BUCKET_ID}/files/{file_id}/view?project={settings.DB.PROJECT_ID}"

        data = patient.model_dump()
        data["identificationDocumentUrl"] = url
        data.pop("userId")

        _ = connect.storage.update_file(
            bucket_id=settings.DB.BUCKET_ID,
            file_id=file_id,
            permissions=[
                Permission.read(Role.user(id=patient.userId)),
                Permission.write(Role.user(id=patient.userId)),
            ],
        )

        response = connect.db.create_document(
            database_id=settings.DB.ID,
            collection_id=settings.DB.PATIENT_COLLECTION_ID,
            document_id=ID.unique(),
            data=data,
            permissions=[
                Permission.read(Role.user(id=patient.userId)),
                Permission.write(Role.user(id=patient.userId)),
                Permission.read(Role.team(id="admin")),
                Permission.write(Role.team(id="admin")),
            ],
        )

        return CreatePatientResponse(
            code=status.HTTP_201_CREATED,
            data=PatientOutputData(id=response["$id"]),
        )

    except AppwriteException as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="A patient already exists with these details.",
        )
