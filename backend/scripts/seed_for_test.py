# backend/scripts/seed_for_test.py
import sys
import pathlib

# Projektpfad sicherstellen
root = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root))

from app.db import SessionLocal
from app.models import Character

def main():
    db = SessionLocal()
    if db.query(Character).count() == 0:
        char = Character(
            key="emma",
            name="Emma",
            style="friendly",
            prompt_template="You are Emma, a warm and supportive virtual girlfriend."
        )
        db.add(char)
        db.commit()
        print("✅ Seeded: Character 'emma'")
    else:
        print("ℹ️ Characters already seeded")

if __name__ == "__main__":
    main()
