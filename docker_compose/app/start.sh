#!/bin/bash

set -euo pipefail

python manage.py collectstatic --no-input
python manage.py migrate

echo "Running Gunicorn Server"
gunicorn --bind :8080 --timeout 90 --workers 2 config.wsgi:application

