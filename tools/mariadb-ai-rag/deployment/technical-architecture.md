---
hidden: true
noIndex: true
---

# Technical Architecture

## Table of Contents

1. [System Architecture](technical-architecture.md#system-architecture)
2. [Component Details](technical-architecture.md#component-details)
3. [Data Flow](technical-architecture.md#data-flow)
4. [Security Architecture](technical-architecture.md#security-architecture)
5. [Configuration Management](technical-architecture.md#configuration-management)
6. [API Specifications](technical-architecture.md#api-specifications)
7. [Database Schema](technical-architecture.md#database-schema)
8. [Performance Characteristics](technical-architecture.md#performance-characteristics)

***

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Windows Host System                         │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐    │
│  │              Docker Desktop (WSL 2 Backend)                 │    │
│  │                                                             │    │
│  │  ┌────────────────────────────────────────────────────────┐ │    │
│  │  │              Docker Network: ai-nexus-network          │ │    │
│  │  │                  (Bridge Driver)                       │ │    │
│  │  │                                                        │ │    │
│  │  │  ┌──────────────────────────────────────────────────┐  │ │    │
│  │  │  │      ai-nexus Container (Ubuntu 24.04)           │  │ │    │
│  │  │  │                                                  │  │ │    │
│  │  │  │  ┌────────────────────────────────────────────┐  │  │ │    │
│  │  │  │  │  Process 1: RAG API (PID: dynamic)         │  │  │ │    │
│  │  │  │  │  - Framework: FastAPI                      │  │  │ │    │
│  │  │  │  │  - Server: Uvicorn (ASGI)                  │  │  │ │    │
│  │  │  │  │  - Bind: 0.0.0.0:8000                      │  │  │ │    │
│  │  │  │  │  - Workers: 1                              │  │  │ │    │
│  │  │  │  │  - Binary: /opt/rag-in-a-box/bin/rag-api   │  │  │ │    │
│  │  │  │  └────────────────────────────────────────────┘  │  │ │    │
│  │  │  │                                                  │  │ │    │
│  │  │  │  ┌────────────────────────────────────────────┐  │  │ │    │
│  │  │  │  │  Process 2: MCP Server (PID: dynamic)      │  │  │ │    │
│  │  │  │  │  - Framework: FastAPI                      │  │  │ │    │
│  │  │  │  │  - Server: Uvicorn (ASGI)                  │  │  │ │    │
│  │  │  │  │  - Bind: 0.0.0.0:8002                      │  │  │ │    │
│  │  │  │  │  - Workers: 1                              │  │  │ │    │
│  │  │  │  │  - Binary: /opt/rag-in-a-box/bin/mcp-server│  │  │ │    │
│  │  │  │  └────────────────────────────────────────────┘  │  │ │    │
│  │  │  │                                                  │  │ │    │
│  │  │  │  Startup: start-services.sh                      │  │ │    │
│  │  │  │  Health Check: 180s timeout, 10s interval        │  │ │    │
│  │  │  └──────────────────┬────────────────────────────┘     │ │    │
│  │  │                     │                                  │ │    │
│  │  │                     │ MySQL Protocol (Port 3306)       │ │    │
│  │  │                     │                                  │ │    │
│  │  │  ┌──────────────────▼────────────────────────────┐     │ │    │
│  │  │  │      mysql-db Container (MariaDB 11)          │     │ │    │
│  │  │  │                                               │     │ │    │
│  │  │  │  ┌──────────────────────────────────────────┐ │     │ │    │
│  │  │  │  │  MariaDB Server                          │ │     │ │    │
│  │  │  │  │  - Version: 11.x                         │ │     │ │    │
│  │  │  │  │  - Storage Engine: InnoDB                │ │     │ │    │
│  │  │  │  │  - Character Set: utf8mb4                │ │     │ │    │
│  │  │  │  │  - Collation: utf8mb4_unicode_ci         │ │     │ │    │
│  │  │  │  │  - Page Size: 16KB                       │ │     │ │    │
│  │  │  │  │  - Row Format: Dynamic                   │ │     │ │    │
│  │  │  │  └──────────────────────────────────────────┘ │     │ │    │
│  │  │  │                                               │     │ │    │
│  │  │  │  ┌──────────────────────────────────────────┐ │     │ │    │
│  │  │  │  │  Persistent Volume: mysql_data           │ │     │ │    │
│  │  │  │  │  - Database: kb_chunks                   │ │     │ │    │
│  │  │  │  │  - Tables: documents_*, vdb_tbl_*        │ │     │ │    │
│  │  │  │  │  - Indexes: Vector indexes               │ │     │ │    │
│  │  │  │  └──────────────────────────────────────────┘ │     │ │    │
│  │  │  └────────────────────────────────────────────┘ │ │           │
│  │  └─────────────────────────────────────────────────┘ │           │
│  └───────────────────────────────────────────────────────┘          │
│                                                                     │
│  Port Mappings (Host → Container):                                  │
│  - 8000:8000  (RAG API)                                             │
│  - 8002:8002  (MCP Server)                                          │
│  - 3306:3306  (MariaDB)                                             │
└─────────────────────────────────────────────────────────────────────┘

External Services (Internet):
┌─────────────────────────────────────────────────┐
│  Google Generative AI API                       │
│  - Endpoint: generativelanguage.googleapis.com  │
│  - Embedding: gemini-embedding-001                │
│  - LLM: gemini-2.5-flash-lite                        │
└─────────────────────────────────────────────────┘
```

### Container Dependency Graph

```
Start Order:
1. mysql-db (MariaDB)
   ├─ Health Check: 30s start period, 10s interval
   └─ Condition: service_healthy

2. ai-nexus (Application)
   ├─ Depends on: mysql-db (healthy)
   ├─ Startup Script: start-services.sh
   │   ├─ Start RAG API (background)
   │   ├─ Wait for RAG API health (max 180s)
   │   └─ Start MCP Server (foreground)
   └─ Restart Policy: unless-stopped
```

***

## Component Details

### 1. RAG API Component

**Binary Location**: `/opt/rag-in-a-box/bin/rag-api`

**Responsibilities**:

* Document ingestion and processing
* Text chunking and embedding generation
* Vector storage and retrieval
* Semantic search
* RAG query processing
* Authentication and authorization

**Technology Stack**:

* **Framework**: FastAPI (Python)
* **ASGI Server**: Uvicorn
* **Database Driver**: PyMySQL / aiomysql
* **Embedding Client**: Google Generative AI SDK
* **Document Processing**: LangChain / Custom parsers

**Endpoints**:

```
Authentication:
POST   /token                 - Generate JWT token

Document Management:
POST   /documents/ingest      - Upload and process documents
GET    /documents             - List all documents
GET    /documents/{id}        - Get document details
DELETE /documents/{id}        - Delete document

RAG Operations:
POST   /generate              - Generate RAG response
POST   /search                - Semantic search
GET    /embeddings/{doc_id}   - Get document embeddings

Health & Status:
GET    /health                - Health check
GET    /                      - API info
GET    /docs                  - Swagger UI
GET    /openapi.json          - OpenAPI spec
```

**Configuration Variables**:

```bash
APP_HOST=0.0.0.0
APP_PORT=8000
DB_HOST=mysql-db
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_secure_database_password
DB_NAME=kb_chunks
GEMINI_API_KEY=your_gemini_api_key
SECRET_KEY=your_generated_secret_key
JWT_SECRET_KEY=<secret>
EMBEDDING_PROVIDER=gemini
embedding_model=gemini-embedding-001
LLM_PROVIDER=gemini
LLM_MODEL=gemini-2.5-flash-lite
DOCUMENTS_TABLE=documents_DEMO_gemini
VDB_TABLE=vdb_tbl_DEMO_gemini
CHUNK_SIZE=512
CHUNK_OVERLAP=128
```

### 2. MCP Server Component

**Binary Location**: `/opt/rag-in-a-box/bin/mcp-server`

**Responsibilities**:

* Model Context Protocol implementation
* Database tool exposure
* Vector store tool exposure
* RAG tool exposure
* Authentication and rate limiting

**Technology Stack**:

* **Framework**: FastAPI (Python)
* **ASGI Server**: Uvicorn
* **Protocol**: MCP (Model Context Protocol)
* **Database Client**: PyMySQL

**Available Tools**:

**Core Tools**:

* `health_check` - Server health verification
* `get_server_status` - Detailed server status

**Database Tools**:

* `list_databases` - List all databases
* `list_tables` - List tables in database
* `get_table_schema` - Get table structure
* `execute_sql` - Execute SQL queries
* `create_database` - Create new database
* `drop_database` - Delete database

**Vector Store Tools**:

* `create_vector_store` - Create vector store
* `delete_vector_store` - Delete vector store
* `list_vector_stores` - List all vector stores
* `insert_docs_vector_store` - Add documents
* `search_vector_store` - Semantic search

**RAG Tools**:

* `ingest_documents` - Ingest documents via RAG API
* `generate_response` - Generate RAG responses

**Configuration Variables**:

```bash
MCP_HOST=0.0.0.0
MCP_PORT=8002
MCP_MARIADB_HOST=mysql-db
MCP_MARIADB_PORT=3306
MCP_AUTH_SECRET_KEY=<secret>
MCP_ENABLE_AUTH=true
MCP_ENABLE_VECTOR_TOOLS=true
MCP_ENABLE_DATABASE_TOOLS=true
MCP_ENABLE_RAG_TOOLS=true
MCP_READ_ONLY=false
MCP_STANDALONE_MODE=false
MCP_RAG_HEALTHCHECK_ENABLED=true
MCP_LOG_LEVEL=INFO
```

### 3. MariaDB Component

**Image**: `mariadb:11`

**Configuration**:

```yaml
Environment:
  MYSQL_ROOT_PASSWORD: your_secure_database_password
  MYSQL_DATABASE: kb_chunks

Command:
  --character-set-server=utf8mb4
  --collation-server=utf8mb4_unicode_ci
  --innodb-page-size=16k
  --innodb-default-row-format=dynamic

Health Check:
  Test: healthcheck.sh --connect --innodb_initialized
  Interval: 10s
  Timeout: 5s
  Retries: 10
  Start Period: 30s

Volume:
  mysql_data:/var/lib/mysql (persistent)
```

**Database Schema**:

```sql
-- Documents Table
CREATE TABLE documents_DEMO_gemini (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    content LONGTEXT,
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_filename (filename),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Vector Database Table
CREATE TABLE vdb_tbl_DEMO_gemini (
    id INT AUTO_INCREMENT PRIMARY KEY,
    document_id INT NOT NULL,
    chunk_index INT NOT NULL,
    chunk_text LONGTEXT NOT NULL,
    embedding BLOB,  -- 768-dimensional vector (3072 bytes)
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id) REFERENCES documents_DEMO_gemini(id) ON DELETE CASCADE,
    INDEX idx_document_id (document_id),
    INDEX idx_chunk_index (chunk_index)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

***

## Data Flow

### Document Ingestion Flow

```
User Upload
    │
    ▼
┌───────────────────────────────────────┐
│  1. RAG API - File Reception          │
│  - Validate file type                 │
│  - Check file size (max 200MB)        │
│  - Generate unique ID                 │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  2. Document Processing               │
│  - Extract text from file             │
│  - Clean and normalize text           │
│  - Store in documents table           │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  3. Text Chunking                     │
│  - Method: Recursive character split  │
│  - Chunk size: 512 tokens             │
│  - Overlap: 128 tokens                │
│  - Generate chunk metadata            │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  4. Embedding Generation              │
│  - Batch size: 32 chunks              │
│  - Call Gemini API                    │
│  - Model: gemini-embedding-001          │
│  - Dimensions: 768                    │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  5. Vector Storage                    │
│  - Store in vdb_tbl_DEMO_gemini       │
│  - Link to document_id                │
│  - Store chunk text + embedding       │
│  - Create indexes                     │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  6. Response to User                  │
│  - Document ID                        │
│  - Number of chunks                   │
│  - Processing status                  │
└───────────────────────────────────────┘
```

### RAG Query Flow

```
User Query
    │
    ▼
┌───────────────────────────────────────┐
│  1. Query Reception                   │
│  - Validate JWT token                 │
│  - Parse query text                   │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  2. Query Embedding                   │
│  - Call Gemini API                    │
│  - Generate 768-dim vector            │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  3. Similarity Search                 │
│  - Calculate cosine similarity        │
│  - Filter by threshold (0.8)          │
│  - Retrieve top-k chunks (default: 5) │
│  - Order by similarity score          │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  4. Context Preparation               │
│  - Combine retrieved chunks           │
│  - Add source metadata                │
│  - Format for LLM prompt              │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  5. LLM Generation                    │
│  - Construct prompt:                  │
│    "Context: {chunks}"                │
│    "Question: {query}"                │
│  - Call Gemini LLM                    │
│  - Model: gemini-2.5-flash-lite            │
└───────────────┬───────────────────────┘
                │
                ▼
┌───────────────────────────────────────┐
│  6. Response Formatting               │
│  - AI-generated answer                │
│  - Source documents                   │
│  - Confidence scores                  │
│  - Metadata                           │
└───────────────┬───────────────────────┘
                │
                ▼
    Return to User
```

***

## Security Architecture

### Authentication Flow

```
┌─────────────────────────────────────────────────────────────┐
│  1. Token Generation                                        │
│                                                             │
│  POST /token                                                │
│  Body: {"username": "admin", "password": "password"}        │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Server validates credentials                          │ │
│  │  Generates JWT with:                                   │ │
│  │  - Header: {"alg": "HS256", "typ": "JWT"}              │ │
│  │  - Payload: {"sub": "admin", "exp": <timestamp>}       │ │
│  │  - Signature: HMAC-SHA256(header.payload, SECRET_KEY)  │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  Response: {"access_token": "eyJ...", "token_type": "bearer"}│
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│  2. Authenticated Request                                   │
│                                                             │
│  GET /documents                                             │
│  Headers: {"Authorization": "Bearer eyJ..."}                │
│                                                             │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Server extracts token                                 │ │
│  │  Verifies signature with SECRET_KEY                    │ │
│  │  Checks expiration (30 minutes)                        │ │
│  │  Validates claims                                      │ │
│  └────────────────────────────────────────────────────────┘ │
│                                                             │
│  If valid: Process request                                  │
│  If invalid: Return 401 Unauthorized                        │
└─────────────────────────────────────────────────────────────┘
```

### Security Keys

**Critical Requirement**: All three keys must be identical for unified authentication:

```bash
SECRET_KEY=<same-value>
JWT_SECRET_KEY=<same-value>
MCP_AUTH_SECRET_KEY=<same-value>
```

**Key Generation** (for production):

```python
import secrets
key = secrets.token_urlsafe(64)
# Use this key for all three variables
```

### Security Features

1. **JWT Authentication**
   * Algorithm: HS256
   * Expiration: 30 minutes (configurable)
   * Unified token for RAG API and MCP Server
2. **Rate Limiting**
   * 100 requests per minute (default)
   * Configurable per endpoint
3. **CORS Configuration**
   * Allowed origins: Configurable
   * Credentials: Supported
   * Methods: GET, POST, PUT, DELETE, OPTIONS
4. **File Upload Security**
   * Max file size: 200MB
   * Allowed extensions: .pdf, .txt, .docx, .md, .html, .csv, .json, .xml
   * Malware scanning: Optional
   * Quarantine: Enabled for suspicious files
5. **Database Security**
   * Parameterized queries (SQL injection prevention)
   * Connection pooling
   * Encrypted connections (optional)

***

## Configuration Management

### Configuration Modes

#### 1. Standalone Mode

**File**: `config.env.secure.local` **Usage**: Direct environment variables **Security**: Secrets stored in file **Best for**: Development, single developer

#### 2. Vault Mode

**File**: `config.env.vault.local` **Usage**: HashiCorp Vault integration **Security**: Secrets stored in Vault **Best for**: Team development, production-like

**Vault Configuration**:

```bash
VAULT_ADDR=http://rag-vault:8200
VAULT_TOKEN=rag-root-token
VAULT_SECRET_PATH=rag-in-a-box
VAULT_MOUNT_POINT=secret
```

#### 3. 1Password Mode

**File**: `config.env.1password.employee` **Usage**: 1Password CLI references **Security**: Secrets in 1Password vault **Best for**: Enterprise with 1Password

**1Password References**:

```bash
GEMINI_API_KEY=op://Employee/RAG-API-Keys/gemini
DB_PASSWORD=op://Employee/RAG-Database/password
```

#### 4. HCP Vault Mode

**File**: `config.env.hcp.live` **Usage**: HashiCorp Cloud Platform **Security**: Cloud-managed secrets **Best for**: Production cloud deployments

***

## API Specifications

### RAG API Endpoints

#### POST /token

**Description**: Generate JWT authentication token

**Request**:

```json
{
  "username": "admin",
  "password": "your_password"
}
```

**Response**:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

#### POST /ingest

**Description**: Upload and process documents

**Headers**:

```
Authorization: Bearer <token>
Content-Type: multipart/form-data
```

**Request**:

```
file: <binary-file-data>
```

**Response**:

```json
{
  "document_id": 123,
  "filename": "document.pdf",
  "chunks_created": 45,
  "status": "success"
}
```

#### POST /generate

**Description**: Generate RAG response

**Headers**:

```
Authorization: Bearer <token>
Content-Type: application/json
```

**Request**:

```json
{
  "query": "What is the main topic?",
  "top_k": 5,
  "threshold": 0.8
}
```

**Response**:

```json
{
  "answer": "The main topic is...",
  "sources": [
    {
      "document_id": 123,
      "chunk_index": 5,
      "similarity": 0.92,
      "text": "..."
    }
  ],
  "metadata": {
    "processing_time": 1.23,
    "model": "gemini-2.5-flash-lite"
  }
}
```

***

## Database Schema

### Tables

#### documents\_DEMO\_gemini

```sql
CREATE TABLE documents_DEMO_gemini (
    id INT AUTO_INCREMENT PRIMARY KEY,
    filename VARCHAR(255) NOT NULL,
    content LONGTEXT,
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_filename (filename),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

#### vdb\_tbl\_DEMO\_gemini

```sql
CREATE TABLE vdb_tbl_DEMO_gemini (
    id INT AUTO_INCREMENT PRIMARY KEY,
    document_id INT NOT NULL,
    chunk_index INT NOT NULL,
    chunk_text LONGTEXT NOT NULL,
    embedding BLOB,
    metadata JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (document_id) REFERENCES documents_DEMO_gemini(id) ON DELETE CASCADE,
    INDEX idx_document_id (document_id),
    INDEX idx_chunk_index (chunk_index)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
```

### Vector Storage Format

**Embedding Dimensions**: 768 (float32) **Storage Size**: 768 × 4 bytes = 3,072 bytes per vector **Format**: Binary BLOB **Encoding**: IEEE 754 single-precision floating-point

***

## Performance Characteristics

### Resource Requirements

**Per Container**:

```
ai-nexus:
  CPU: 1-2 cores
  RAM: 2-4 GB
  Disk: 1 GB (application)

mysql-db:
  CPU: 1-2 cores
  RAM: 2-4 GB
  Disk: Variable (depends on data)
```

### Performance Metrics

**Document Ingestion**:

* Processing speed: \~5 documents/batch
* Chunking: \~100 chunks/second
* Embedding generation: \~32 chunks/batch
* Total time: \~30-60 seconds per document (depends on size)

**Query Performance**:

* Embedding generation: \~100-200ms
* Similarity search: \~50-100ms (depends on dataset size)
* LLM generation: \~1-3 seconds
* Total response time: \~2-4 seconds

### Scalability

**Current Limits**:

* Max file size: 200MB
* Max concurrent requests: 100/minute
* Database connections: 10 (pool size)

**Scaling Options**:

* Horizontal: Deploy multiple ai-nexus containers
* Vertical: Increase container resources
* Database: Use read replicas for queries

***

**End of Technical Architecture Document**

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
