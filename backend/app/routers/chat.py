from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..services.openai_service import chat_completion
from ..db import SessionLocal
from ..models import Character, Message

router = APIRouter()

class ChatIn(BaseModel):
    character_key: str
    text: str

@router.post("/send")
def send(body: ChatIn):
    db = SessionLocal()

    # 1) Character-Validierung
    character = db.query(Character).filter_by(key=body.character_key).first()
    if not character:
        raise HTTPException(status_code=400, detail="invalid_character_key")

    # 2) MVP: feste user_id (später aus JWT)
    user_id = 1

    # 3) User-Message loggen
    db.add(Message(user_id=user_id, character_id=character.id, role="user", content=body.text))
    db.commit()

    # 4) Antwort generieren
    reply = chat_completion(body.character_key, body.text)

    # 5) Assistant-Message loggen
    db.add(Message(user_id=user_id, character_id=character.id, role="assistant", content=reply))
    db.commit()

    return {"reply": reply}

