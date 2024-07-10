from app.config.settings import settings

from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID

client = Client()
client.set_endpoint("https://cloud.appwrite.io/v1")
client.set_project(settings.DB.PROJECT_ID)
client.set_key(settings.DB.API_KEY)

databases = Databases(client)
