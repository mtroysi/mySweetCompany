#!/bin/bash
python manage.py migrate                  # Apply database migrations
python manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
# touch /srv/logs/gunicorn.log
# touch /srv/logs/access.log
# tail -n 0 -f /srv/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn mySweetCompany.wsgi:application \
    --name mySweetCompany \
    --bind 0.0.0.0:8001 \
    --workers 3 \
    "$@"
