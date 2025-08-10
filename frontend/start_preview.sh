#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

# Port freimachen
lsof -ti :5173 | xargs -r kill || lsof -ti :5173 | xargs -r kill -9

# API-URL sicherstellen (falls noch nicht gesetzt, .env.local anlegen)
test -f .env.local || echo 'VITE_API_URL=http://localhost:8000' > .env.local

# Build & Serve
npm install
npm run build
npx serve dist -l 5173
