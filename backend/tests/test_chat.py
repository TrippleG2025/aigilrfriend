from fastapi.testclient import TestClient
from app.main import app
from app.db import SessionLocal
from app.models import Character, Message

client = TestClient(app)

def test_chat_logs_and_validates_character():
    db = SessionLocal()

    # Seeds sollten min. 1 Character angelegt haben
    char = db.query(Character).first()
    assert char is not None, "No character seeded"

    before = db.query(Message).count()

    # 1) Gültiger Character
    r = client.post("/chat/send", json={"character_key": char.key, "text": "Hi"})
    assert r.status_code == 200
    assert "reply" in r.json()

    after_valid = db.query(Message).count()
    assert after_valid == before + 2  # user + assistant

    # 2) Ungültiger Character
    r2 = client.post("/chat/send", json={"character_key": "does_not_exist", "text": "Yo"})
    assert r2.status_code == 400
    assert r2.json()["detail"] == "invalid_character_key"
