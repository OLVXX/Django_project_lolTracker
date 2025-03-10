#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Navigate to the directory containing manage.py
cd match_analyzer

# Run Django commands
python manage.py collectstatic --no-input
python manage.py migrate
