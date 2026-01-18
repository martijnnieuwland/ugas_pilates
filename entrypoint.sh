#!/bin/sh
set -e

# Optionally wait for Postgres (if SQL_HOST/SQL_PORT are provided)
if [ -n "$SQL_HOST" ] && [ -n "$SQL_PORT" ]; then
  echo "Waiting for $SQL_HOST:$SQL_PORT..."
  while ! nc -z "$SQL_HOST" "$SQL_PORT"; do
    sleep 1
  done
fi

# Run migrations and collect static files
python manage.py migrate --noinput
python manage.py collectstatic --noinput

# Execute the container command (e.g. gunicorn)
exec "$@"
