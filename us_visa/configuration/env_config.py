import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()


def get_mongo_db_url() -> str:
    username = os.getenv("MONGO_DB_USERNAME")
    password = os.getenv("MONGO_DB_PASSWORD")

    if not username or not password:
        raise ValueError("MongoDB credentials missing")

    return (
        f"mongodb+srv://{quote_plus(username)}:{quote_plus(password)}"
        "@cluster0.1ggmf5m.mongodb.net/?appName=Cluster0"
    )
