from fastapi import APIRouter
from pydantic import BaseModel
from ..services.openai_service import chat_completion

router = APIRouter()

class ChatIn(BaseModel):
    character_key: str
    text: str

@router.post("/send")
def send(body: ChatIn):
    reply = chat_completion(body.character_key, body.text)
    return {"reply": reply}
