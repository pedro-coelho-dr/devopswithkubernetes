#!/usr/bin/env bash
set -e

if [ -z "$POSTGRES_USER" ] || [ -z "$POSTGRES_PASSWORD" ] || [ -z "$POSTGRES_DB" ] || [ -z "$BUCKET_NAME" ]; then
  echo "Error: Required environment variables are not set."
  exit 1
fi

export URL="postgres://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgres-svc:5432/${POSTGRES_DB}"
TIMESTAMP=$(date +"%Y%m%d%H%M%S")
BACKUP_FILE="/tmp/backup_${TIMESTAMP}.sql"

echo "Starting database backup..."
pg_dump -v "$URL" > "$BACKUP_FILE"
echo "Backup completed: $BACKUP_FILE"

echo "Uploading backup to Google Cloud Storage..."
gsutil cp "$BACKUP_FILE" gs://corisco-db-backup/backup_${TIMESTAMP}.sql
echo "Backup successfully uploaded."
