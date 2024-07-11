from contextlib import asynccontextmanager
from app.api import auth
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(docs_url="/api/docs", redoc_url=None, lifespan=lifespan)


app.include_router(auth.router)
# app.include_router(root.router, prefix="/api")

origins = [
    "",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)
