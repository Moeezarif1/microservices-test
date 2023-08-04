#!/bin/bash

# Activate the virtual environment
source /venv/bin/activate

# Load the environment variables
set -a; source /app/.env; set +a

echo "Running database migration"
(python manage.py makemigrations --merge) && (python manage.py migrate)
echo "Database migration completed"


# Start Gunicorn to serve the Django application
echo "Starting Gunicorn"
(gunicorn accounting.wsgi:application  --bind 0.0.0.0:8000 --workers 3)
echo "Stopped Gunicorn"