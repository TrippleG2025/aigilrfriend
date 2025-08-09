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
    char = db.query(Character).filter_by(key=body.character_key).first()
    if not char:
        db.close()
        raise HTTPException(404, "Character not found")
    reply = chat_completion(body.character_key, body.text)
    db.add(Message(character_id=char.id, role="user", content=body.text))
    db.add(Message(character_id=char.id, role="assistant", content=reply))
    db.commit()
    db.close()
    return {"reply": reply}
