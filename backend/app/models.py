from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    plan = Column(String, default="free")  # free|premium|vip
    created_at = Column(DateTime, default=datetime.utcnow)

class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    name = Column(String)
    style = Column(Text)  # simple JSON string or free text
    prompt_template = Column(Text)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    character_id = Column(Integer, ForeignKey("characters.id"))
    role = Column(String)      # "user" | "assistant"
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
