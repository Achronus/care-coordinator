from app.config.settings import settings

from app.db.crud import CRUD
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage
from appwrite.services.messaging import Messaging
from appwrite.services.users import Users

from pydantic import BaseModel, ConfigDict


class DBConnections(BaseModel):
    """A model to access all database connections on server run."""

    client: Client
    db: Databases
    storage: Storage
    messaging: Messaging
    users: Users

    model_config = ConfigDict(arbitrary_types_allowed=True)


def init_db() -> DBConnections:
    """Initialise the database."""
    client = Client()
    client.set_endpoint("https://cloud.appwrite.io/v1")
    client.set_project(settings.DB.PROJECT_ID)
    client.set_key(settings.DB.API_KEY)

    db = Databases(client)
    storage = Storage(client)
    messaging = Messaging(client)
    users = Users(client)

    return DBConnections(
        client=client,
        db=db,
        storage=storage,
        messaging=messaging,
        users=users,
    )


connect = init_db()

patient = CRUD(
    db=connect.db,
    db_id=settings.DB.ID,
    collection_id=settings.DB.PATIENT_COLLECTION_ID,
)

doctor = CRUD(
    db=connect.db,
    db_id=settings.DB.ID,
    collection_id=settings.DB.DOCTOR_COLLECTION_ID,
)

appointment = CRUD(
    db=connect.db,
    db_id=settings.DB.ID,
    collection_id=settings.DB.APPOINTMENT_COLLECTION_ID,
)
