
import os
from datetime import datetime, timezone
from pymongo import MongoClient


class MongoLogger:

    def __init__(self):
        mongo_uri = os.getenv("MONGODB_URI")
        print("MongoDB URI loaded:", bool(mongo_uri))

        if not mongo_uri:
            raise ValueError("MONGODB_URI is missing from .env file")

        self.client = MongoClient(
            mongo_uri,
            serverSelectionTimeoutMS=10000
        )

        self.db = self.client["llm_monitoring"]
        self.collection = self.db["call_logs"]

        # Check whether MongoDB Atlas is reachable
        self.client.admin.command("ping")

        print("Connected to MongoDB Atlas successfully!")

    def log_call(self, log_data):
        log_data["timestamp"] = datetime.now(timezone.utc)
        self.collection.insert_one(log_data)

    def close(self):
        self.client.close()
