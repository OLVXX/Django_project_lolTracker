#!/usr/bin/env bash
# exit on error
set -o errexit

# Debug: Print current directory and contents
echo "Current directory:"
pwd
echo "Directory contents:"
ls -la

# First upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create static directory
mkdir -p staticfiles

# Debug: Print directory structure
echo "Full directory structure:"
find . -type f -name "manage.py"

# Run Django commands with the correct path
cd match_analyzer
python manage.py collectstatic --no-input
python manage.py migrate
