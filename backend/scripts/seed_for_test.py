# scripts/seed_for_tests.py
from app.db import SessionLocal, engine
from app.models import Base, Character

# Tabellen sicherstellen (idempotent)
try:
    Base.metadata.create_all(bind=engine)
except Exception:
    pass

db = SessionLocal()
try:
    char = db.query(Character).first()
    if not char:
        db.add(Character(
            key="emma",
            name="Emma",
            style="friendly",
            prompt_template="You are Emma."
        ))
        db.commit()
        print("Seeded: Character 'emma'")
    else:
        if not getattr(char, "key", None):
            char.key = "emma"
            db.add(char)
            db.commit()
        print("Seed present:", getattr(char, "key", None))
finally:
    db.close()
