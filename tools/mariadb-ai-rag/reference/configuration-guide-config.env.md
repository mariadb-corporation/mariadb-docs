# Configuration Guide (config.env)

This guide explains all configuration variables in the config.env.template file. It is designed for both technical and non-technical users to understand what each setting does and how to configure it for different deployment scenarios.

## Database Configuration

The system requires a MariaDB database to store documents, metadata, and user information.

### Option A: Local MariaDB (On-Premise / Development)

Use this for local development or on-premise deployments where you run MariaDB on your machine.

* `DB_HOST`: The IP address or hostname of your MariaDB server (e.g., `127.0.0.1` for local).
* `DB_PORT`: The port MariaDB listens on (default: `3306`).
* `DB_USER`: Database username (e.g., `root`).
* `DB_PASSWORD`: Database password.
* `DB_NAME`: The database name to use (e.g., `rag_db`).

#### Example (Local)

```ini
DB_HOST=127.0.0.1
DB_PORT=3306
DB_USER=root
DB_PASSWORD=Password123!
DB_NAME=rag_db
```

### Option B: MariaDB Cloud (SkySQL / Managed Service)

Use this for cloud-hosted MariaDB instances (e.g., MariaDB SkySQL).

* `DB_HOST`: The cloud endpoint provided by your hosting provider.
* `DB_PORT`: The cloud port (often different from 3306, e.g., `4059` for SkySQL).
* `DB_USER`: Cloud database username.
* `DB_PASSWORD`: Cloud database password.
* `DB_NAME`: The database name.

#### Example (Cloud)

```ini
DB_HOST=serverless-europe-west3.sysp0000.db2.skysql.com
DB_PORT=4059
DB_USER=dbpg_user
DB_PASSWORD=MEu...
DB_NAME=rag_db
```

#### SSL Configuration

* `DB_SSL_ENABLED`: Set to `true` if your database connection requires SSL/TLS encryption (recommended for cloud databases).

## Admin Credentials

Initial admin account credentials for the system.

* `ADMIN_EMAIL`: Email address for the admin user (e.g., `admin@example.com`).
* `ADMIN_PASSWORD`: Initial password for the admin account. **Change this in production.**

## License Configuration

* `MARIADB_LICENSE_KEY`: Your MariaDB license key (JWT token). Required for production deployments. This is validated at application startup. If invalid or expired, the application will not start.

## Embedding Configuration

Embeddings are numerical representations of text used for semantic search. The system converts documents and queries into embeddings to find semantically similar content.

#### Supported Provider examples

**Option A: OpenAI (Recommended for Production)**

```ini
EMBEDDING_PROVIDER=openai
embedding_model=text-embedding-3-small
```

Requires: `OPENAI_API_KEY` (see API Keys section below)

**Option B: HuggingFace (Local / Open Source)**

```ini
EMBEDDING_PROVIDER=huggingface
embedding_model=BAAI/bge-m3
```

Runs locally without external API calls. No API key required.

## API Keys

External service credentials for LLM, embedding, and parsing services.

* `OPENAI_API_KEY`: Your OpenAI API key (format: `sk-proj-...`). Required if using OpenAI for embeddings or LLM.
* `GEMINI_API_KEY`: Your Google Gemini API key (format: `AIza...`). Required if using Gemini as LLM provider.

**Security Note:** Never commit API keys to version control. Use environment variables or secret management systems.

## Security Keys

Cryptographic keys used to sign and verify authentication tokens.

* `SECRET_KEY`: General-purpose secret key for session management and CSRF protection.
* `JWT_SECRET_KEY`: Secret key for signing JWT authentication tokens.
* `MCP_AUTH_SECRET_KEY`: Secret key for MCP (Model Context Protocol) server authentication.

**Note:** You can use the same key for all three (as shown in the template).

## Document Processing Services

### Docling Ray Service (Layout-Aware Standard Parser)

Used for distributed document parsing with structure preservation.

* `DOCLING_RAY_SERVICE_URL`: The URL where the Ray service is running.
  * **Local Development:** `http://localhost:8003`
  * **Docker Deployment:** `http://docling-ray:8003`
  * **macOS Docker:** `http://host.docker.internal:8003`
* `DOCLING_RAY_REQUEST_TIMEOUT`: Maximum time (in seconds) to wait for Ray to process a document (default: `600` = 10 minutes).

## Server Ports & Hosts

Configuration for where the API server and MCP server listen.

### RAG API Server

* `APP_HOST`: The host/IP the RAG API binds to.
  * **Local Development:** `127.0.0.1` (localhost only)
  * **Docker (internal):** `rag-api` (service name)
  * **Production:** `0.0.0.0` (all interfaces)
* `APP_PORT`: The port the RAG API listens on (default: `8000`).

### MCP Server (Model Context Protocol)

* `MCP_HOST`: The host the MCP server binds to.
  * **Local Development:** `127.0.0.1`
  * **Docker (internal):** `mcp-server` (service name)
* `MCP_PORT`: The port the MCP server listens on (default: `8002`).

### MariaDB Connection from MCP

* `MCP_MARIADB_HOST`: The hostname/IP of MariaDB as seen from the MCP server.
  * **Local Development:** `127.0.0.1`
  * **Docker (internal):** `mariadb` (service name)
* `MCP_MARIADB_PORT`: The port MariaDB listens on (default: `3306`).

## MCP Configuration

Settings for the Model Context Protocol server (used for AI agent integration).

* `MCP_READ_ONLY`: Set to `true` to disable write operations (read-only mode).
* `MCP_ENABLE_AUTH`: Set to `true` to require authentication for MCP requests.
* `MCP_ENABLE_VECTOR_TOOLS`: Enable vector search tools in MCP.
* `MCP_ENABLE_DATABASE_TOOLS`: Enable direct database query tools in MCP.
* `MCP_ENABLE_RAG_TOOLS`: Enable RAG-specific tools (document ingestion, retrieval).
* `MCP_RAG_HEALTHCHECK_ENABLED`: Enable health checks for RAG endpoints.
* `MCP_STANDALONE_MODE`: Set to `true` to run MCP without the main RAG API.
* `MCP_LOG_LEVEL`: Logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`).

#### Document Base Path

* `MCP_DOCUMENT_BASE_PATH`: Base directory for MCP file ingestion (e.g., `/app` for Docker).

## RAG Configuration

Settings specific to the RAG (Retrieval-Augmented Generation) system.

* `DOCUMENTS_TABLE`: Name of the database table storing document metadata (e.g., `documents_DEMO`).
* `VDB_TABLE`: Name of the vector database table storing document chunks and embeddings (e.g., `vdb_tbl_DEMO`).

## LLM Configuration

Settings for the Large Language Model used to generate responses.

#### Supported Provider examples

**Option A: Google Gemini (Recommended)**

```ini
LLM_PROVIDER=gemini
LLM_MODEL=gemini-2.5-flash
```

Requires: `GEMINI_API_KEY`

**Option B: Ollama (Local / Open Source)**

```ini
LLM_PROVIDER=ollama
LLM_MODEL=gemma3:1b
```

Requires: `OLLAMA_HOST` configured (see section 12)

#### Ollama Configuration

* `OLLAMA_HOST`: The URL where Ollama is running.
  * **Local Development:** `http://localhost:11434`
  * **Docker Deployment:** `http://ollama:11434`
  * **macOS Docker:** `http://host.docker.internal:11434`

## CORS Configuration

Cross-Origin Resource Sharing (CORS) settings for API access from web browsers.

* `CORS_ALLOWED_ORIGINS`: Comma-separated list of allowed origins (e.g., `http://localhost:3000,http://127.0.0.1:3000`).
* `CORS_ALLOW_CREDENTIALS`: Set to `true` to allow credentials (cookies, auth headers) in cross-origin requests.
* `CORS_ALLOW_METHODS`: Comma-separated HTTP methods allowed (e.g., `GET,POST,PUT,DELETE,OPTIONS`).
* `CORS_ALLOW_HEADERS`: Comma-separated headers allowed (e.g., `Authorization,Content-Type`).

## Development Settings

Debugging and logging options.

* `DEBUG_MODE`: Set to `true` to enable debug mode (verbose error messages, auto-reload).
* `LOG_SQL_QUERIES`: Set to `true` to log all SQL queries (useful for debugging database issues).

## Token Expiry

* `ACCESS_TOKEN_EXPIRE_MINUTES`: How long authentication tokens remain valid (default: `120` minutes = 2 hours).

## Security Settings

#### Rate Limiting

Protects the API from abuse by limiting requests per user/IP.

* `RATE_LIMIT_REQUESTS`: Maximum number of requests allowed per window (default: `100`).
* `RATE_LIMIT_WINDOW`: Time window in seconds (default: `60` = 1 minute).

#### File Upload Security

* `MAX_FILE_SIZE`: Maximum file size allowed for upload (e.g., `200MB`).
* `ALLOWED_FILE_EXTENSIONS`: Comma-separated list of allowed file types (e.g., `.pdf,.txt,.docx,.md,.html,.csv,.xml`).
* `SCAN_UPLOADS_FOR_MALWARE`: Set to `true` to scan uploaded files for malware (requires antivirus integration).
* `QUARANTINE_SUSPICIOUS_FILES`: Set to `true` to isolate suspicious files instead of rejecting them.

#### Security Headers

* `SECURITY_HEADERS_ENABLED`: Set to `true` to enable HTTP security headers (recommended for production).

## Quota Settings

Resource limits per user to prevent abuse and control costs.

* `QUOTA_MAX_DOCUMENTS`: Maximum number of documents a user can ingest (default: `100`).
* `QUOTA_MAX_STORAGE_MB`: Maximum storage in MB per user (default: `1000` MB = 1 GB).
* `QUOTA_MAX_CONCURRENT_TASKS`: Maximum concurrent ingestion/processing tasks per user (default: `10`).
* `QUOTA_MAX_FILES_PER_SYNC`: Maximum files to sync in a single operation (default: `10`).
* `QUOTA_RATE_LIMIT_RPM`: Requests per minute limit per user (default: `60`).

## Reranking Configuration

Reranking improves search results by re-scoring retrieved documents based on relevance.

* `RERANKING_ENABLED`: Set to `true` to enable reranking globally (default: `false`).

#### Reranking Model

* `RERANKING_MODEL_TYPE`: Type of reranker (`flashrank`, `sentence-transformers`, `cohere`).
* `RERANKING_MODEL_NAME`: Specific model name (e.g., `ms-marco-MiniLM-L-12-v2` for FlashRank).
* `RERANKING_API_KEY`: API key if using cloud-based rerankers (e.g., Cohere).

#### Retrieval Strategy

* `RERANKING_TOP_K_MULTIPLIER`: Retrieve this many times more documents before reranking (e.g., `2.0` = retrieve 2x the final top\_k).
* `RERANKING_DEFAULT_TOP_K`: Final number of documents to return after reranking (default: `5`).

#### Performance

* `RERANKING_CACHE_MODELS`: Set to `true` to cache loaded models in memory.
* `RERANKING_CACHE_MAX_SIZE`: Maximum number of models to keep in cache (default: `3`).
* `RERANKING_BATCH_SIZE`: Number of documents to rerank in parallel (default: `32`).
* `RERANKING_ENABLE_BATCHING`: Set to `true` to enable batch reranking for efficiency.

## File Storage Configuration

Where uploaded documents are stored. Supports two backends: Local filesystem or AWS S3.

#### Option A: Local Storage (On-Premise / Development)

Used for storing files on the local filesystem.

* `FILE_STORAGE_TYPE=local`
* `LOCAL_STORAGE_PATH`: Directory path where files are stored (e.g., `./uploaded_files`). Files are organized as: `{LOCAL_STORAGE_PATH}/{user_id}/{filename}`

**Docker Note:** Mount a host volume to persist files across container restarts:

```yaml
volumes:
  - /var/rag-uploads:/app/uploaded_files
```

#### Option B: AWS S3 / MinIO (Cloud / Managed Storage)

Used for storing files in S3-compatible object storage.

* `FILE_STORAGE_TYPE=s3`

**Core S3 Settings**

* `MANAGED_S3_BUCKET`: The S3 bucket name (e.g., `rag-staging-bucket`).
* `MANAGED_S3_REGION`: AWS region (e.g., `us-east-1`).
* `MANAGED_S3_PREFIX`: Folder prefix inside the bucket (e.g., `uploads/`). Files are stored as: `s3://{bucket}/{prefix}{user_id}/{filename}`

**AWS Credentials**

* `AWS_ACCESS_KEY_ID`: Your AWS access key.
* `AWS_SECRET_ACCESS_KEY`: Your AWS secret key.
* `AWS_DEFAULT_REGION`: Default region for AWS SDK (e.g., `us-east-1`).
* `AWS_CA_BUNDLE`: (Optional) Path to custom CA certificate bundle for corporate networks.

**MinIO / S3-Compatible Storage**

If using MinIO instead of AWS S3:

* `MANAGED_S3_ENDPOINT_URL`: The MinIO server URL (e.g., `http://host.docker.internal:9000`).
  * **Local Development:** `http://localhost:9000`
  * **Docker Deployment:** `http://minio:9000`
  * **macOS Docker:** `http://host.docker.internal:9000`
* `MANAGED_S3_USE_PATH_STYLE`: Set to `true` for MinIO. This forces path-style URLs (`http://endpoint/bucket`) instead of virtual-hosted-style (`http://bucket.endpoint`).

## Celery Configuration (Background Tasks)

Celery is used for asynchronous background tasks like document ingestion and processing.

#### Core Settings

* `CELERY_ENABLED`: Set to `true` to enable background task processing. By default it's need to be **true**.
* `CELERY_POOL`: Type of worker pool, please use `threads`.
* `CELERY_AUTOSCALE`: Worker scaling (format: `max,min`). Example: `8,2` = scale between 2-8 workers.

#### Message Broker (Redis)

Celery uses Redis to queue and manage tasks.

* `CELERY_BROKER_URL`: Redis connection URL for task queue.
  * **Local Development:** `redis://localhost:6379/0`
  * **Docker Deployment:** `redis://redis:6379/0`
  * **macOS Docker:** `redis://redis:6379/0` (use service name, not host.docker.internal)
* `CELERY_RESULT_BACKEND`: Redis connection URL for storing task results.
  * **Local Development:** `redis://localhost:6379/0`
  * **Docker Deployment:** `redis://redis:6379/0`
  * **macOS Docker:** `redis://redis:6379/0`
* `REDIS_URL`: General Redis connection URL (used by other components).
  * **Local Development:** `redis://localhost:6379/0`
  * **Docker Deployment:** `redis://redis:6379/0`
  * **macOS Docker:** `redis://redis:6379/0`

#### Worker Settings

* `CELERY_WORKER_CONCURRENCY`: Number of worker processes (default: `4`).
* `CELERY_WORKER_PREFETCH_MULTIPLIER`: Tasks to prefetch per worker (default: `4`).
* `CELERY_TASK_TIME_LIMIT`: Hard time limit per task in seconds (default: `3600` = 1 hour).
* `CELERY_TASK_SOFT_TIME_LIMIT`: Soft time limit in seconds (default: `3300` = 55 minutes).

## Document Processing Configuration

Settings for different document parsing engines.

#### Available Processors

* **base**: Fast text extraction using pdfplumber and python-docx (always available).
* **layout\_aware\_standard**: Docling-based Markdown conversion preserving document structure (local processing).
* **layout\_aware\_advanced**: LlamaParse cloud API for highest quality parsing (requires API key).

#### Docling (Layout-Aware Standard)

* `DOCLING_OCR_PROVIDER`: OCR engine for scanned documents. Default: `rapidocr`.
* `DOCLING_RAY_HEAD_ADDRESS`: Ray cluster address for distributed processing.
  * `auto`: Automatically detect or create a local Ray cluster.

#### LlamaParse (Layout-Aware Advanced)

* `LLAMA_CLOUD_API_KEY`: API key for LlamaParse cloud service. Get your key from: https://cloud.llamaindex.ai

## Troubleshooting

#### "All connection attempts failed" Error

**Cause:** Incorrect hostname/IP in connection URLs.

**Solution:**

* For services on the host machine (macOS): Use `host.docker.internal`.
* For services in Docker containers: Use the service name from docker-compose.yml.
* For local development: Use `localhost` or `127.0.0.1`.

#### Redis Connection Errors

**Cause:** Redis URL misconfiguration.

**Solution:** Ensure all three Redis URLs are consistent:

```ini
CELERY_BROKER_URL=redis://redis:6379/0
CELERY_RESULT_BACKEND=redis://redis:6379/0
REDIS_URL=redis://redis:6379/0
```

#### Document Processing Timeout

**Cause:** `DOCLING_RAY_REQUEST_TIMEOUT` is too short for large documents.

**Solution:** Increase the timeout value (in seconds). Example: `DOCLING_RAY_REQUEST_TIMEOUT=1200` (20 minutes).

#### S3 / MinIO Connection Issues

**Cause:** Incorrect endpoint URL or credentials.

**Solution:**

* Verify `MANAGED_S3_ENDPOINT_URL` is correct (e.g., `http://host.docker.internal:9000` for macOS).
* Verify `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` are correct.
* Ensure `MANAGED_S3_USE_PATH_STYLE=true` for MinIO.
