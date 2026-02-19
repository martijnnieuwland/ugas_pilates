# --- Builder Stage ---
FROM python:3.12.4-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Install Python packages
COPY requirements.txt .
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r requirements.txt

# --- Final Stage ---
FROM python:3.12.4-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Create non-root user
RUN addgroup --system django && adduser --system --ingroup django django

# Runtime dependencies
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y --no-install-recommends libpq5 netcat-openbsd && \
    rm -rf /var/lib/apt/lists/*

# Copy virtual environment
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copy project code
COPY . .

# Run collectstatic using dummy values.
# We prefix the command with the variables.
RUN SECRET_KEY=dummy \
    DB_NAME=dummy \
    DB_USER=dummy \
    DB_PASSWORD=dummy \
    CLOUD_SQL_CONNECTION_NAME=dummy:dummy:dummy \
    python manage.py collectstatic --noinput --settings=ugas_pilates.settings.prod || true

# Copy entrypoint script and set permissions
COPY --chown=django:django entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

# Create staticfiles directory and set ownership
RUN mkdir -p /app/staticfiles && chown django:django /app/staticfiles

# Switch to non-root user
USER django

# Use entrypoint.sh to handle migrations, staticfiles, and Gunicorn
ENTRYPOINT ["/app/entrypoint.sh"]
