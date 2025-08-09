import os

APP_ENV = os.getenv("APP_ENV", "dev")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.sqlite3")
JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret")
MOCK_EXTERNAL_CALLS = os.getenv("MOCK_EXTERNAL_CALLS", "true").lower() == "true"
