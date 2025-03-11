#!/bin/bash

# Create proper static file directories
mkdir -p static/css
mkdir -p static/js
mkdir -p static/img

# Create directories for the analysis app static files
mkdir -p match_analyzer/analysis/static/analysis/css
mkdir -p match_analyzer/analysis/static/analysis/js
mkdir -p match_analyzer/analysis/static/analysis/img

# Add default CSS file if it doesn't exist
if [ ! -f "match_analyzer/analysis/static/analysis/css/style.css" ]; then
  echo "/* Default styles for match analyzer */" > match_analyzer/analysis/static/analysis/css/style.css
fi

# Copy static files from apps if they exist
if [ -d "analysis/static" ]; then
  cp -r analysis/static/* static/
fi

echo "Static directories created successfully"
