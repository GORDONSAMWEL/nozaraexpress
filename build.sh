#!/bin/bash

# Exit immediately if a command fails
set -e

echo "Installing Python dependencies..."
pip install -r requirements.txt

echo "Applying database migrations..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build complete!"
