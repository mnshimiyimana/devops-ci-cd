#!/bin/sh

gunicorn todo_project.wsgi:application --bind 0.0.0.0:8000 --workers 3 --timeout 120 