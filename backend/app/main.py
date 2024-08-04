from contextlib import asynccontextmanager

from app import auth
from app.api import doctors, patients, appointments, retrieval

from app.api.responses import ErrorResponse
from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(docs_url="/api/docs", redoc_url=None, lifespan=lifespan)


app.include_router(auth.router)
app.include_router(appointments.router, prefix="/api")
app.include_router(doctors.router, prefix="/api")
app.include_router(patients.router, prefix="/api")
app.include_router(retrieval.router, prefix="/api", include_in_schema=False)

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "https://cc.achronus.dev/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    details = ErrorResponse(code=exc.status_code, message=exc.detail).model_dump()
    return JSONResponse(details, status_code=exc.status_code)
