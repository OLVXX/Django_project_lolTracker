#!/usr/bin/env bash
# exit on error
set -o errexit

# First upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Print current directory for debugging
pwd
ls -la

# Create static directory
mkdir -p staticfiles

# Run Django commands with explicit path to manage.py
python match_analyzer/manage.py collectstatic --no-input
python match_analyzer/manage.py migrate
