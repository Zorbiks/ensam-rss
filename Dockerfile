# Use lightweight Python image based on Alpine Linux
FROM python:3.12-alpine

# Set working directory
WORKDIR /app

# Copy requirements first (better for Docker caching)
COPY requirements.txt /app/requirements.txt

# Install dependencies
RUN apk add --no-cache bash curl ca-certificates && \
    apk add --no-cache --virtual .build-deps gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

# Copy your app files
COPY ./app /app/app

# Copy crontab
COPY ./crontab /etc/crontabs/root

# Expose port
EXPOSE 8000

# Run cron and FastAPI
CMD python /app/app/generate_feed.py && crond -l 2 -L /var/log/cron.log & uvicorn app.server:app --host 0.0.0.0 --port 8000
