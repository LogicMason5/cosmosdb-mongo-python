import os
import sys
from typing import Tuple
import pymongo
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.mongo_client import MongoClient


class MongoConfig:
    """Loads and validates MongoDB configuration from environment variables."""

    def __init__(self):
        self.mongo_url: str = os.getenv("MONGO_URL", "")
        self.mongo_database: str = os.getenv("MONGO_DATABASE", "")
        self.mongo_collection: str = os.getenv("MONGO_COLLECTION", "")

        self._validate()

    def _validate(self):
        missing = []
        if not self.mongo_url:
            missing.append("MONGO_URL")
        if not self.mongo_database:
            missing.append("MONGO_DATABASE")
        if not self.mongo_collection:
            missing.append("MONGO_COLLECTION")

        if missing:
            sys.exit(
                f"Missing required environment variables: {', '.join(missing)}.\n"
                "Please set them and try again."
            )


class MongoConnector:
    """Handles MongoDB connection and collection retrieval."""

    def __init__(self, config: MongoConfig):
        self.config = config
        self.client: MongoClient | None = None

    def connect(self) -> MongoClient:
        """Create MongoDB client."""
        try:
            self.client = pymongo.MongoClient(self.config.mongo_url)
            return self.client
        except Exception as e:
            sys.exit(f"Failed to connect to MongoDB: {e}")

    def list_databases(self) -> list[str]:
        """Return available databases."""
        if not self.client:
            raise RuntimeError("Mongo client not initialized.")
        dbs = self.client.list_database_names()
        print("Available databases:", dbs)
        return dbs

    def get_database(self) -> Database:
        """Return database handle."""
        if not self.client:
            raise RuntimeError("Mongo client not initialized.")

        dbs = self.list_databases()
        if self.config.mongo_database not in dbs:
            sys.exit(
                f"Database '{self.config.mongo_database}' does not exist. "
                "Create it first."
            )

        return self.client[self.config.mongo_database]

    def get_collection(self, db: Database) -> Collection:
        """Return collection handle."""
        collections = db.list_collection_names()

        if self.config.mongo_collection not in collections:
            sys.exit(
                f"Collection '{self.config.mongo_collection}' does not exist "
                f"in database '{self.config.mongo_database}'. Create it first."
            )

        print(f"Collection '{self.config.mongo_collection}' found.")
        return db[self.config.mongo_collection]

    def connect_and_get_collection(self) -> Collection:
        """Full pipeline: connect → validate → return collection."""
        self.connect()
        db = self.get_database()
        collection = self.get_collection(db)
        return collection


def connect_and_get_collection() -> Collection:
    """Convenience helper."""
    config = MongoConfig()
    connector = MongoConnector(config)
    return connector.connect_and_get_collection()


# Example usage
if __name__ == "__main__":
    collection = connect_and_get_collection()

    print("Connected successfully.")
    print("Collection:", collection.name)
