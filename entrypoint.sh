#!/bin/bash

if [ "$APP_MODE" = "qcluster" ]; then
    echo "Starting qcluster service..."
    exec python manage.py qcluster
else
    echo "Starting web service..."
    exec gunicorn taobao_sms.wsgi:application --bind 0.0.0.0:8000
fi
