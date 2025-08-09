import sys
from pathlib import Path
from fastapi import HTTPException

# Allow importing from backend/app
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.routers.chat import ChatIn, send  # noqa: E402
from app.db import SessionLocal, create_all  # noqa: E402
from app.seeds import run_seeds  # noqa: E402
from app.models import Message  # noqa: E402

# Create tables and seed database with test data
create_all()
run_seeds()

def test_send_chat_persists_messages():
    db = SessionLocal()
    count_before = db.query(Message).count()
    result = send(ChatIn(character_key="emma", text="hello"))
    assert result["reply"] == "[emma] Mock: hello"
    count_after = db.query(Message).count()
    db.close()
    assert count_after == count_before + 2

def test_send_unknown_character():
    try:
        send(ChatIn(character_key="unknown", text="hi"))
    except HTTPException as exc:
        assert exc.status_code == 404
    else:
        assert False, "expected HTTPException"
