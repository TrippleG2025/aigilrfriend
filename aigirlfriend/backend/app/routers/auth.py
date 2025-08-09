from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from ..db import SessionLocal
from ..models import User
import hashlib, jwt, datetime
from ..config import JWT_SECRET

router = APIRouter()

class AuthIn(BaseModel):
    email: str
    password: str

def _hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

@router.post("/register")
def register(body: AuthIn):
    db = SessionLocal()
    if db.query(User).filter_by(email=body.email).first():
        raise HTTPException(400, "Email exists")
    u = User(email=body.email, password_hash=_hash_pw(body.password))
    db.add(u); db.commit()
    return {"ok": True}

@router.post("/login")
def login(body: AuthIn):
    db = SessionLocal()
    u = db.query(User).filter_by(email=body.email).first()
    if not u or u.password_hash != _hash_pw(body.password):
        raise HTTPException(401, "Invalid")
    token = jwt.encode(
        {"sub": str(u.id), "plan": u.plan, "exp": datetime.datetime.utcnow()+datetime.timedelta(hours=12)},
        JWT_SECRET, algorithm="HS256"
    )
    return {"token": token}
