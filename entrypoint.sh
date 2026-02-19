#!/bin/sh

# Exit immediately if a command exits with a non-zero status.
#!/bin/sh
set -e

# Wait for database if needed
# ./wait-for-it.sh $DB_HOST:$DB_PORT -t 30

# Run migrations
python manage.py migrate --noinput

# Start Gunicorn on the port Cloud Run provides
exec /opt/venv/bin/gunicorn ugas_pilates.wsgi:application \
    --bind 0.0.0.0:${PORT:-8080} \
    --workers 2 \
    --worker-tmp-dir /dev/shm
