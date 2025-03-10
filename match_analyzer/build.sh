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

# Create static directories
mkdir -p static/analysis/css
mkdir -p static/analysis/js
mkdir -p static/analysis/img
mkdir -p staticfiles

# Copy CSS file from match_analyzer/staticfiles to correct static directory
if [ -f "match_analyzer/staticfiles/analysis/css/style.css" ]; then
  echo "Copying CSS from match_analyzer/staticfiles"
  cp -f match_analyzer/staticfiles/analysis/css/style.css static/analysis/css/
else
  echo "WARNING: CSS file not found in match_analyzer/staticfiles"
fi

# Create a basic CSS file if it doesn't exist
if [ ! -f "static/analysis/css/style.css" ]; then
  echo "Creating basic CSS file"
  echo "body { font-family: sans-serif; margin: 0; padding: 20px; }" > static/analysis/css/style.css
fi

# Show static directory structure
echo "Static directory contents:"
find static -type f | sort

# Run Django commands
python manage.py collectstatic --noinput
python manage.py migrate
