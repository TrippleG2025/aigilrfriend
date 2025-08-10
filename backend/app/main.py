from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .db import create_all
from .routers import auth, chat

app = FastAPI(title="aigilrfriend")
create_all()

# CORS: erlaube alle localhost/127.0.0.1 Ports (5173, 54xxx etc.)
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,   # falls nicht nötig, kannst du es auf False setzen
    allow_methods=["*"],      # wichtig: lässt OPTIONS (Preflight) zu
    allow_headers=["*"],      # z. B. Content-Type
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(chat.router, prefix="/chat", tags=["chat"])

@app.get("/healthz")
def health():
    return {"ok": True}
