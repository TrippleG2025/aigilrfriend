import os
from pathlib import Path
from dotenv import load_dotenv

# .env im backend/ und im Projektroot laden (ohne Fehler, wenn nicht vorhanden)
backend_env = Path(__file__).resolve().parents[1] / ".env"
root_env = Path(__file__).resolve().parents[2] / ".env"
for p in (backend_env, root_env):
    if p.exists():
        load_dotenv(p, override=False)

APP_ENV = os.getenv("APP_ENV", "dev")
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.sqlite3")
JWT_SECRET = os.getenv("JWT_SECRET", "dev-secret")
MOCK_EXTERNAL_CALLS = os.getenv("MOCK_EXTERNAL_CALLS", "true").lower() == "true"

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")
STRIPE_WEBHOOK_SECRET = os.getenv("STRIPE_WEBHOOK_SECRET", "")
