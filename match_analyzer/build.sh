#!/usr/bin/env bash
# exit on error
set -o errexit

# Debug: Show current directory
echo "Current directory:"
pwd
ls -la

# First upgrade pip
python -m pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p static
mkdir -p staticfiles

# Copy static files to static dir if needed
if [ -d "analysis/static" ]; then
  echo "Copying static files from analysis/static"
  cp -r analysis/static/* static/
fi

if [ -d "match_analyzer/analysis/static" ]; then
  echo "Copying static files from match_analyzer/analysis/static"
  cp -r match_analyzer/analysis/static/* static/
fi

# Show directory structure for debugging
echo "Directory structure after setup:"
find . -type d -name static -o -name templates | sort

# Run Django commands
python manage.py collectstatic --no-input --clear
python manage.py migrate
