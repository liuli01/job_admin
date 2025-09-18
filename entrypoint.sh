#!/bin/bash

if [ "$APP_MODE" = "qcluster" ]; then
    echo "Starting qcluster service..."
    exec python manage.py qcluster
else
    echo "Running database migrations..."
    python manage.py migrate --noinput
    
    echo "Starting web service..."
    exec gunicorn core.wsgi:application --bind 0.0.0.0:8000
fi
