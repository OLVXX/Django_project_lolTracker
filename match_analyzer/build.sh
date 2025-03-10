#!/usr/bin/env bash
# exit on error
set -o errexit

# Upgrade pip first
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p staticfiles

# Run Django commands
python manage.py collectstatic --no-input --clear
python manage.py migrate
