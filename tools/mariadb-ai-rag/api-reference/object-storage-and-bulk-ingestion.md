# Object Storage and Bulk Ingestion

Users can upload documents one by one [through the API](api-reference.md#upload-documents).

Enterprise deployments often need to ingest thousands of files from cloud storage. Bulk cloud ingestion lets you connect an external bucket directly to the RAG system.

The system also uses Smart Sync, which is incremental sync. It compares each cloud file fingerprint (`ETag`) with the stored database record. It only downloads and processes files that are new or changed.

## How it works

Bulk ingestion uses an asynchronous background pipeline.

### Phase 1: Initial discovery and queuing

When a sync starts, the `sync_manager` scans the target bucket.

* Unsupported file extensions and directories are skipped.
* Quota checks enforce document and `files_per_sync` limits.
* Valid files are pushed to the Celery queue through `process_webhook_file_task`.

### Phase 2: Smart Sync

For each file, the system checks for an existing database record with the same `object_key`.

* If the file exists, has status `INDEXED`, and the provider `ETag` matches `content_hash`, the file is skipped.
* If the `ETag` differs, the file is treated as changed and queued again.

### Phase 3: Distributed processing

Celery workers pick up queued tasks, stream each file into memory, and pass it to the configured document processor.

Supported processors include `base`, `layout_aware_standard` with Docling + Ray, and LlamaParse. The processor extracts content, chunks it, and writes embeddings to the vector database.

### Supported cloud providers

When calling `POST /integrations`, use the correct `provider_type` and `credentials` structure.

### AWS S3

Use `provider_type: "s3"`.

Required credentials:

* `bucket`: S3 bucket name.
* `region`: AWS region, such as `us-east-1`.
* `access_key_id`: AWS access key.
* `secret_access_key`: AWS secret key.

### Google Cloud Storage

Use `provider_type: "gcs"`.

Required credentials:

* `bucket`: GCS bucket name.
* `project_id`: GCP project ID.
* `service_account_json`: Parsed service account JSON with read access to the bucket.

### MinIO or S3-compatible storage

Use `provider_type: "minio"`.

MinIO uses the same credentials as S3, plus an `endpoint_url`.

Required credentials:

* `bucket`: MinIO bucket name.
* `region`: Region, usually `us-east-1` for local MinIO.
* `access_key_id`: MinIO access key or username.
* `secret_access_key`: MinIO secret key or password.
* `endpoint_url`: MinIO server URL, such as `http://host.docker.internal:9000`.

### API Workflow

All endpoints require a valid JWT token in `Authorization: Bearer <token>`.

{% stepper %}
{% step %}
#### Create the integration

**Endpoint:** `POST /integrations`

Registers cloud storage credentials in the database.

```json
{
  "provider_type": "minio",
  "name": "Local MinIO Documentation",
  "credentials": {
    "bucket": "my-company-docs",
    "region": "us-east-1",
    "access_key_id": "minioadmin",
    "secret_access_key": "minioadmin",
    "endpoint_url": "http://127.0.0.1:9000"
  },
  "settings": {
    "sync_prefix": "documents/2024/",
    "file_extensions": [".pdf", ".docx", ".txt"],
    "max_file_size_mb": 100
  }
}
```

Save the returned `id`, such as `int_abc123`. You need it in later requests.
{% endstep %}

{% step %}
#### Validate the integration

**Endpoint:** `POST /integrations/{integration_id}/validate`

Tests bucket connectivity and confirms read access.

```json
{
  "is_valid": true,
  "message": "Connection successful",
  "details": {
    "provider": "s3",
    "bucket": "my-company-docs"
  }
}
```
{% endstep %}

{% step %}
#### Trigger a manual sync

**Endpoint:** `POST /integrations/{integration_id}/sync`

This scans the bucket and queues valid new or modified files for ingestion.

This step parses and loads documents, similar to `POST /documents/ingest`. Chunking must still be run separately afterward.
{% endstep %}

{% step %}
#### List integrations

**Endpoint:** `GET /integrations`

Returns configured integrations, status, and last sync time.
{% endstep %}

{% step %}
#### Update an integration

**Endpoint:** `PATCH /integrations/{integration_id}`

Use this to update settings, rotate credentials, rename the integration, or change status.

Behavior:

* `credentials` fully replaces the existing credentials.
* `settings` merges into the existing settings.

Example: update sync settings

```json
{
  "settings": {
    "sync_prefix": "documents/finance/",
    "file_extensions": [".pdf", ".docx"],
    "sync_frequency_minutes": 30
  }
}
```

Example: rotate MinIO credentials

```json
{
  "credentials": {
    "bucket": "my-minio-bucket",
    "endpoint_url": "http://127.0.0.1:9000",
    "access_key_id": "new_admin",
    "secret_access_key": "new_password"
  }
}
```

Example: disable an integration

```json
{
  "status": "inactive"
}
```
{% endstep %}

{% step %}
#### Delete an integration

**Endpoint:** `DELETE /integrations/{integration_id}`

This removes the integration and deletes related file records and database entries.
{% endstep %}

{% step %}
#### Ingest through orchestration

**Endpoint:** `POST /orchestrate/ingestion`

This is the recommended approach for targeted ingestion from folders inside an existing integration.

```json
{
  "chunking_method": "semantic",
  "chunk_size": 512,
  "cloud_storage_sources": [
    {
      "integration_id": "int_abc123",
      "prefix": "financial_reports/Q3/",
      "recursive": true,
      "file_extensions": [".pdf"]
    }
  ],
  "document_processing": {
    "processor_type": "layout_aware_standard"
  }
}
```

This scans `financial_reports/Q3/` in `int_abc123`, selects PDFs, parses them with `layout_aware_standard`, and chunks them semantically.
{% endstep %}
{% endstepper %}

## Managed file storage configuration

External integrations are read-only sources. The system also needs a storage backend for files uploaded directly through endpoints such as `/orchestrate/full-pipeline`.

Configure this in `.env` or `config.env`.

Supported backends:

* Local filesystem
* S3, including MinIO

### Core setting

* `FILE_STORAGE_TYPE`: Storage backend for manual uploads.
  * Use `local` for on-premise filesystem storage.
  * Use `s3` for AWS S3 or MinIO.

### Local storage

Use this when `FILE_STORAGE_TYPE=local`.

* `LOCAL_STORAGE_PATH`: Directory used for uploaded files, such as `./uploaded_files`.

Files are stored under `{LOCAL_STORAGE_PATH}/{user_id}/{filename}`.

When using Docker, mount a host volume to this path to persist files across restarts. Example: `-v /var/rag-uploads:/app/uploaded_files`.

### Managed S3 and MinIO storage

Use this when `FILE_STORAGE_TYPE=s3`.

Files are stored at `s3://{bucket}/{prefix}{user_id}/{filename}`.

Core AWS variables:

* `MANAGED_S3_BUCKET`: Central bucket name, such as `rag-staging-bucket`.
* `MANAGED_S3_REGION`: Bucket region, such as `us-east-1`.
* `MANAGED_S3_PREFIX`: Prefix for managed uploads, such as `uploads/`.
* `AWS_ACCESS_KEY_ID`: AWS access key.
* `AWS_SECRET_ACCESS_KEY`: AWS secret key.
* `AWS_DEFAULT_REGION`: Default AWS region.
* `AWS_CA_BUNDLE`: Optional custom CA bundle path.

Extra settings for MinIO or other S3-compatible storage:

* `MANAGED_S3_ENDPOINT_URL`: MinIO server URL, such as `http://host.docker.internal:9000`.
* `MANAGED_S3_USE_PATH_STYLE`: Set this to `true` for MinIO. This forces `http://endpoint/bucket` instead of `http://bucket.endpoint`.

## Summary

* `config.env` controls where manual uploads are stored.
* `/integrations` controls where bulk ingestion reads from.
* For initial setup, call `POST /integrations` and then `POST /integrations/{id}/validate`.
* For targeted ingestion, call `POST /orchestrate/ingestion` with `integration_id` in `cloud_storage_sources`.
* Smart Sync is enabled by default and skips unchanged files based on `ETag`.
