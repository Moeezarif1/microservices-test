#!/bin/bash

# Activate the virtual environment
source /venv/bin/activate

# Load the environment variables
set -a; source /app/.env; set +a

echo "Running database migration"
(python manage.py makemigrations --merge --noinput) && (python manage.py migrate)
echo "Database migration completed"

# After copying the Django project files
echo "Running Collectstatic"
(python manage.py collectstatic --noinput)

# Start the Django development server
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
     echo "creating django superuser"
     EXIT_CODE=0
     (python manage.py createsuperuser --noinput) || EXIT_CODE=$?
     if [ $EXIT_CODE -gt 0 ]; then
        echo "Unable to create superuser"
     else
        echo "superuser created"
     fi
fi

# Start Gunicorn to serve the Django application
echo "Starting Gunicorn"
(gunicorn warehouse.wsgi:application  --bind 0.0.0.0:8000 --workers 3)
echo "Stopped Gunicorn"