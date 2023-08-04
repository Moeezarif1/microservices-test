#!/bin/bash

# Activate the virtual environment
source /venv/bin/activate

# Load the environment variables
set -a; source /app/.env; set +a

echo "Running database migration"
(python manage.py makemigrations) && (python manage.py migrate main)
echo "Database migration completed"

# After copying the Django project files
echo "Running Collectstatic"
(python manage.py collectstatic --noinput)


# Start Gunicorn to serve the Django application
echo "Starting Gunicorn"
(gunicorn sales.wsgi:application  --bind 0.0.0.0:8000 --workers 3)
echo "Stopped Gunicorn"