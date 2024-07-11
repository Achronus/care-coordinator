from typing import Any

from appwrite.services.databases import Databases
from appwrite.id import ID
from fastapi import HTTPException
from pydantic import BaseModel, ConfigDict


class CRUD(BaseModel):
    """Handles create, read, update, and delete operations for a database collection."""

    db: Databases
    db_id: str
    collection_id: str

    model_config = ConfigDict(arbitrary_types_allowed=True)

    async def create_item(self, data: dict) -> dict[str, Any]:
        """Adds an item to the collection."""
        try:
            response = self.db.create_document(
                database_id=self.db_id,
                collection_id=self.collection_id,
                document_id=ID.unique(),
                data=data,
            )
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def get_single_item(self, id: str) -> dict[str, Any]:
        """Retrieves a single item from the collection."""
        response = self.db.get_document(
            database_id=self.db_id,
            collection_id=self.collection_id,
            document_id=id,
        )

        if id not in response:
            raise HTTPException(status_code=404, detail="Item not found")

    async def get_multiple_items(self) -> dict[str, Any]:
        """Retrieves multiple items from a collection."""
        try:
            response = self.db.list_documents(
                database_id=self.db_id,
                collection_id=self.collection_id,
            )
            return response["documents"]
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def update_item(self, id: str, data: dict) -> dict[str, Any]:
        """Updates an item in the collection."""
        try:
            response = self.db.update_document(
                database_id=self.db_id,
                collection_id=self.collection_id,
                document_id=id,
                data=data,
            )
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def delete_item(self, id: str) -> dict[str, Any]:
        """Deletes an item from the collection."""
        try:
            response = self.db.delete_document(
                database_id=self.db_id,
                collection_id=self.collection_id,
                document_id=id,
            )
            return response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
