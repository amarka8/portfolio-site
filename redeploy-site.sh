#!/bin/bash

set -e

PROJECT_DIR="/home/portfolio-site"

# Go to project directory
cd "$PROJECT_DIR"

# Update the repository
git fetch
git reset origin/main --hard

# deactivate any existing docker container run of our myportfolio container
docker compose -f docker-compose.prod.yml down

# activate any existing docker container run of our myportfolio container
docker compose -f docker-compose.prod.yml up -d --build

