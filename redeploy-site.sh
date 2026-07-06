#!/bin/bash

set -e

PROJECT_DIR="/home/portfolio-site"

# Kill all tmux sessions
tmux kill-server 2>/dev/null || true

# Go to project directory
cd "$PROJECT_DIR"

# Update the repository
git fetch
git reset origin/main --hard

# Activate virtual environment
source ./python3-virtualenv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start Flask in a detached tmux session
tmux new-session -d -s flask \
"cd $PROJECT_DIR && source ./python3-virtualenv/bin/activate && flask run --host=0.0.0.0"

echo "Redeployment complete!"