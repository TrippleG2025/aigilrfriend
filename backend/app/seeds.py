from .db import SessionLocal
from .models import User, Character
import hashlib, json
from pathlib import Path

def _hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

def run_seeds():
    db = SessionLocal()

    # Default-User sicher anlegen
    u = db.query(User).filter_by(email="test@example.com").first()
    if not u:
        u = User(email="test@example.com", password_hash=_hash_pw("test123"), plan="free")
        db.add(u)

    # Characters aus /characters
    chars_dir = Path(__file__).resolve().parents[2] / "characters"
    for key in ["emma", "lara"]:
        p = chars_dir / f"{key}.yaml"
        if p.exists() and not db.query(Character).filter_by(key=key).first():
            raw = p.read_text(encoding="utf-8")
            db.add(Character(key=key, name=key.title(), style=json.dumps({"style":"warm"}), prompt_template=raw))

    db.commit()
    db.close()

