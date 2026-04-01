# Orchestration

## Overview

The orchestration module provides high-level endpoints that coordinate multiple steps of the RAG (Retrieval Augmented Generation) workflow. These endpoints simplify integration by handling complex workflows in a single request.

## Orchestration Endpoints

### Ingestion Orchestration

```
POST /orchestrate/ingestion
```

**Purpose**: Orchestrates the complete ingestion workflow: document upload, processing, chunking, and embedding. This endpoint handles the entire pipeline from files to searchable chunks.

**Request**: `multipart/form-data` with files and optional configuration

**Form Parameters**:

* `files`: One or more files to upload (optional if using `file_paths`)
* `file_paths`: JSON array of server-side file paths (optional if using `files`)
* `config`: JSON string with chunking configuration (optional)

**Configuration JSON Structure**:

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
    "processor_type": "layout_aware_standard",
    "enable_ocr": true,
    "ocr_provider": "rapidocr",
    "enable_table_extraction": true,
    "table_structure_mode": "accurate"
  }
}
```

**Parameters:**

* `chunking_method`
  * `recursive`: Recursive text splitting (default)
  * `sentence`: Sentence-based chunking
  * `token`: Token-based chunking
  * `semantic`: Semantic similarity-based chunking (requires `threshold`)
* `chunk_size`: Number of tokens/characters per chunk (default: 512).
* `cloud_storage_sources` (optional): A JSON array used to ingest from an external integration (S3, GCS, or MinIO). Requires an `integration_id` and a `prefix`.
* `document_processing` (optional): A stringified JSON object defining the extraction tier:
  * `processor_type`: `"base"`, `"layout_aware_standard"` (Docling), or `"layout_aware_advanced"` (LlamaParse).
  * `enable_ocr`: Boolean to turn on OCR for scanned documents.

**Response**:

```json
{
  "message": "Successfully ingested and chunked 2 documents",
  "document_ids": [42, 43],
  "chunk_count": 25,
  "processing_time_seconds": 15.2
}
```

**Usage Example**: Upload and process documents in a single request.

```bash
# Upload files with custom chunking config
curl -X POST "http://localhost:8000/orchestrate/ingestion" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "files=@/path/to/document1.pdf" \
  -F "files=@/path/to/document2.docx" \
  -F 'config={"chunking_method":"semantic","chunk_size":512,"threshold":0.8}'

# Use server-side file paths
curl -X POST "http://localhost:8000/orchestrate/ingestion" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F 'file_paths=["./docs/file1.pdf","./docs/file2.pdf"]' \
  -F 'config={"chunking_method":"recursive","chunk_size":512}'
```

### Generation Orchestration

```
POST /orchestrate/generation
```

**Purpose**: Orchestrates the complete RAG workflow: retrieval and text generation in a single request. Automatically retrieves relevant chunks and generates a response.

**Request body (with a `reranking` object)**:

```json
{
  "query": "What are the key findings?",
  "document_ids": [1, 2, 3],
  "retrieval_method": "hybrid",
  "top_k": 5,
  "reranking": {
    "enabled": true,
    "model_type": "flashrank",
    "model_name": "ms-marco-MiniLM-L-12-v2",
    "top_k": 5
  },
  "llm_provider": "openai",
  "llm_model": "gpt-4"
}
```

**Request Parameters**:

* `query` (required): The user's question or prompt
* `document_ids` (optional): Filter retrieval to specific documents (default: all documents)
* `retrieval_method` (optional): `semantic`, `fulltext`, or `hybrid` (default: `hybrid`)
* `model_type` (optional): The backend library to use. Valid values: `"flashrank"`, `"sentence-transformers"`, `"cohere"`, `"hybrid"` (default: `"flashrank"`).
* `model_name` (optional): The specific reranker model to load (default: `"ms-marco-MiniLM-L-12-v2"`)
* `top_k` (optional): Number of chunks to retrieve (default: 5)
* `reranking` (optional): A JSON object to enable a high-accuracy second pass.
  * `enabled` (optional): Set to `true` to activate reranking (default: `false`).
  * `model_type` (optional): The backend library (`flashrank`, `sentence-transformers`, `cohere`, `hybrid`) (default: `"flashrank"`).
  * `model_name` (optional): The specific reranker model to load (default: `"ms-marco-MiniLM-L-12-v2"`).
  * `top_k` (optional): Number of reranked results to return to the LLM.
* `llm_provider` (optional): LLM provider - `openai`, `anthropic`, `gemini`, `cohere`, `ollama`, `azure`, `bedrock`
* `temperature` (optional): Controls randomness (0.0-2.0, default: 0.7)
* `top_p` (optional): Nucleus sampling (0.0-1.0, default: 0.9)
* `max_tokens` (optional): Maximum tokens to generate (1-8192, default: 500)
* `stream` (optional): Enable streaming (default: false)

**Response**:

```json
{
  "query": "What are the key features?",
  "response": "The key features include document processing, semantic search, and AI-powered generation...",
  "chunks_used": 5,
  "retrieval_method": "hybrid",
  "processing_time_seconds": 2.5,
  "retrieval_time_ms": 150.3,
  "generation_time_ms": 2350.7
}
```

**Response Fields**:

* `query`: The original query
* `response`: The generated response
* `chunks_used`: Number of chunks used for generation
* `retrieval_method`: The retrieval method used
* `processing_time_seconds`: Total processing time
* `retrieval_time_ms`: Time spent on retrieval (optional)
* `generation_time_ms`: Time spent on generation (optional)

**Usage Example**: Query documents and get an AI-generated response in one call.

```bash
curl -X POST "http://localhost:8000/orchestrate/generation" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the key features?",
    "document_ids": [42, 43],
    "retrieval_method": "hybrid",
    "top_k": 5,
    "llm_provider": "openai",
    "llm_model": "gpt-4"
  }'
```

### Streaming Generation Orchestration

```
POST /orchestrate/generation-stream
```

**Purpose**: Same as the generation endpoint but returns the response as a Server-Sent Events (SSE) stream for real-time display.

**Request body**: Same as `/orchestrate/generation`

**Response**: Server-Sent Events (SSE) stream with the following event types:

```json
// Start event
{"type": "start", "query": "What are the key features?"}

// Retrieval complete event
{"type": "retrieval_complete", "chunks_retrieved": 5, "retrieval_time_ms": 150.3}

// Token events (streamed as generated)
{"type": "token", "content": "The", "chunk_index": 1}
{"type": "token", "content": " key", "chunk_index": 2}
{"type": "token", "content": " features", "chunk_index": 3}

// Completion event
{"type": "complete", "total_time_seconds": 2.5, "tokens_generated": 150}

// Error event (if error occurs)
{"type": "error", "message": "Error description"}
```

**Usage Example**: Use this endpoint for real-time user interfaces with progressive response display.

```bash
curl -X POST "http://localhost:8000/orchestrate/generation-stream" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the key features?",
    "document_ids": [42, 43],
    "retrieval_method": "hybrid",
    "top_k": 5
  }'
```

### Full Pipeline

```
POST /orchestrate/full-pipeline
```

**Purpose**: Executes the complete RAG pipeline in a single request: document ingestion, chunking, embedding, retrieval, and generation. This is the ultimate one-call solution for processing new documents and getting an AI-generated answer.

**Request**: `multipart/form-data` with files and configuration

**Form Parameters**:

* `files`: One or more files to upload (optional if using `file_paths`)
* `file_paths`: JSON array of server-side file paths (optional if using `files`)
* `query`: The query string (required)
* `config`: JSON string with pipeline configuration (optional)

**Configuration JSON Structure**:

```json
{
  "chunking_method": "recursive",
  "chunk_size": 512,
  "chunk_overlap": 128,
  "retrieval_method": "hybrid",
  "top_k": 5,
  "embedding_provider": "openai",
  "embedding_model": "text-embedding-3-small",
  "llm_provider": "openai",
  "llm_model": "gpt-4",
  "temperature": 0.7,
  "top_p": 0.9,
  "max_tokens": 1000
}
```

**Response**:

```json
{
  "message": "Full pipeline completed successfully",
  "document_ids": [42, 43],
  "chunk_count": 25,
  "query": "What are the key features?",
  "response": "The key features include document processing, semantic search, and AI-powered generation...",
  "chunks_used": 5,
  "total_processing_time_seconds": 20.5
}
```

**Response Fields**:

* `message`: Status message
* `document_ids`: IDs of ingested documents
* `chunk_count`: Total chunks created
* `query`: The original query
* `response`: The AI-generated response
* `chunks_used`: Number of chunks used for generation
* `total_processing_time_seconds`: Total pipeline execution time

**Usage Example**: Process new documents and get an answer in one request.

```bash
# Upload files and query
curl -X POST "http://localhost:8000/orchestrate/full-pipeline" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "files=@/path/to/document1.pdf" \
  -F "files=@/path/to/document2.docx" \
  -F "query=What are the key features?" \
  -F 'config={"chunking_method":"semantic","retrieval_method":"hybrid","top_k":5}'

# Use server-side file paths
curl -X POST "http://localhost:8000/orchestrate/full-pipeline" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F 'file_paths=["./docs/file1.pdf","./docs/file2.pdf"]' \
  -F "query=Summarize the main points" \
  -F 'config={"chunking_method":"recursive","llm_model":"gpt-4"}'
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
