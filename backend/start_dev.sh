#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

# Ports freimachen
lsof -ti :8000 | xargs -r kill || lsof -ti :8000 | xargs -r kill -9

# venv + Pfad
source .venv/bin/activate
export PYTHONPATH="$PWD"

# Seed (idempotent)
python3 scripts/seed_for_test.py

# Server starten
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
