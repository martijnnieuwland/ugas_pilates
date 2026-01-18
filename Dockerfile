# --- Builder Stage ---
# This stage installs build dependencies and Python packages
FROM python:3.12.4-slim AS builder

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

# Install system deps required to build some Python packages (psycopg2, etc.)
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	   build-essential \
	   libpq-dev \
	&& rm -rf /var/lib/apt/lists/*

# Create a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# --- Final Stage ---
# This stage copies the installed packages and application code
FROM python:3.12.4-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

WORKDIR /app

# Install only runtime dependencies
RUN apt-get update && apt-get install -y --no-install-recommends libpq5 netcat && rm -rf /var/lib/apt/lists/*

COPY --from=builder /opt/venv /opt/venv
COPY . /app

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["gunicorn", "ugas_pilates.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
