import pathlib, sys
import pytest
# conftest.py – ganz oben hinzufügen:
import os, pathlib
# sicherstellen, dass Tests die gleiche DB benutzen wie das Setup-Skript
default_db = pathlib.Path(__file__).resolve().parents[2] / "backend" / ".codex.sqlite3"
os.environ.setdefault("DATABASE_URL", f"sqlite:///{default_db}")

# Projektwurzel in sys.path
root = pathlib.Path(__file__).resolve().parents[1]
if str(root) not in sys.path:
    sys.path.insert(0, str(root))

# Konkrete Importe passend zu deiner Struktur
from app.db import SessionLocal, engine
from app.models import Base, Character, Message  # noqa: F401  (Message evtl. von Tests genutzt)

@pytest.fixture(autouse=True, scope="session")
def db_bootstrap():
    """
    Stellt sicher, dass das Schema existiert und mind. ein Character
    mit gültigem key + minimalen Pflichtfeldern vorhanden ist.
    """
    # Tabellen anlegen (idempotent)
    try:
        Base.metadata.create_all(bind=engine)
    except Exception:
        pass

    db = SessionLocal()
    try:
        char = db.query(Character).first()
        if not char:
            char = Character(
                key="emma",                       # wichtig: key gesetzt
                name="Emma",
                style="friendly",                 # einfache Defaults
                prompt_template="You are Emma."   # einfacher Default
            )
            db.add(char)
            db.commit()
        else:
            # fehlenden key nachtragen
            if not getattr(char, "key", None):
                char.key = "emma"
                db.add(char)
                db.commit()
    finally:
        db.close()
