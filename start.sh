#!/bin/bash
# Start TikTok Downloader backend
set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
BACKEND_DIR="$SCRIPT_DIR/backend"

cd "$BACKEND_DIR"

# Install dependencies if needed
if [ ! -d ".venv" ]; then
  echo "Creating virtual environment..."
  python3 -m venv .venv
fi

source .venv/bin/activate

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo "Starting server on http://0.0.0.0:8000"
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
