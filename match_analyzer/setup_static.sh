#!/bin/bash

# Create proper static file directories
mkdir -p static/css
mkdir -p static/js
mkdir -p static/img

# Copy static files from apps if they exist
if [ -d "analysis/static" ]; then
  cp -r analysis/static/* static/
fi

echo "Static directories created successfully"
