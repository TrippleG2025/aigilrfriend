from fastapi import FastAPI
from .db import create_all
from .routers import auth, chat

app = FastAPI(title="aigilrfriend")
create_all()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])

@app.get("/healthz")
def health():
    return {"ok": True}
