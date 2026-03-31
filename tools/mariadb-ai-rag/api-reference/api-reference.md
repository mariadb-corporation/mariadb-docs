# Document Management and Chunking

## Document Management Endpoints

### Upload Documents

```
POST /documents/ingest
```

**Purpose**: Uploads and processes one or more documents for ingestion into the system. Documents are processed asynchronously in the background.

**Request**: `multipart/form-data` with one or more file attachments

**Request Parameters**:

* `files`: One or more files to upload (required)
* `document_processing` (optional): Stringified JSON object for advanced processing.
  * `processor_type`: `"base"`, `"layout_aware_standard"`, or `"layout_aware_advanced"`.

**Example Request:**

```bash
curl -X POST "http://localhost:8000/documents/ingest" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "files=@/path/to/document.pdf" \
  -F 'document_processing={"processor_type": "layout_aware_standard", "enable_ocr": 
```

**Response**:

```json
{
  "message": "2 documents have been queued for ingestion.",
  "documents": [
    {
      "id": 42,
      "source": "/uploaded_files/example1.pdf",
      "filename": "example1.pdf",
      "status": "pending",
      "content": null,
      "error_message": null,
      "created_at": "2025-10-20T12:00:00.123456",
      "updated_at": null
    },
    {
      "id": 43,
      "source": "/uploaded_files/example2.docx",
      "filename": "example2.docx",
      "status": "pending",
      "content": null,
      "error_message": null,
      "created_at": "2025-10-20T12:00:00.234567",
      "updated_at": null
    }
  ]
}
```

**Status Values**:

* `pending`: Document is queued for processing
* `completed`: Document has been successfully processed
* `failed`: Document processing failed (check `error_message`)

**Usage Example**: Upload one or more documents for ingestion.

```bash
# Upload single document
curl -X POST "http://localhost:8000/documents/ingest" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "files=@/path/to/document.pdf"

# Upload multiple documents
curl -X POST "http://localhost:8000/documents/ingest" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "files=@/path/to/document1.pdf" \
  -F "files=@/path/to/document2.docx"
```

**Note**: The endpoint accepts both single and multiple files. Documents are processed asynchronously, so the initial status will be `pending`. Use the document ID to check processing status later.

### List Documents

```
GET /documents
```

**Purpose**: Retrieves a paginated list of all documents uploaded by the authenticated user.

**Parameters**:

* `skip` (optional): Number of records to skip for pagination (default: 0)
* `limit` (optional): Maximum number of records to return (default: 100)

**Response**:

```json
{
  "documents": [
    {
      "id": 42,
      "filename": "example.pdf",
      "content_type": "application/pdf",
      "size": 1048576,
      "status": "completed",
      "created_at": "2025-08-25T11:42:00.123456",
      "updated_at": "2025-08-25T11:43:30.123456",
      "chunk_count": 15
    },
    {...}
  ],
  "total_count": 42,
  "page": 1,
  "pages": 5
}
```

**Usage Example**: Use this endpoint to monitor all documents in the system, check their processing status, or select documents for further operations.

```bash
curl "http://localhost:8000/documents?skip=0&limit=10" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Retrieve Document

```
GET /documents/{document_id}
```

**Purpose**: Retrieves detailed information about a specific document.

**Response**:

```json
{
  "id": 42,
  "filename": "example.pdf",
  "content_type": "application/pdf",
  "size": 1048576,
  "status": "completed",
  "created_at": "2025-08-25T11:42:00.123456",
  "updated_at": "2025-08-25T11:43:30.123456",
  "chunk_count": 15,
  "metadata": {
    "page_count": 10,
    "author": "John Doe",
    "creation_date": "2025-08-20"
  }
}
```

**Usage Example**: Use this endpoint to check the status of a specific document or retrieve its metadata.

```bash
curl "http://localhost:8000/documents/42" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

### Delete Documents

```
DELETE /documents
```

**Purpose**: Deletes multiple documents and their associated chunks and vector embeddings.

**Request body**:

```json
{
  "document_ids": [42, 43, 44]
}
```

**Response**:

```json
{
  "deleted_count": 3,
  "status": "success"
}
```

**Usage Example**: Use this endpoint to remove documents that are no longer needed, freeing up storage space and improving search performance.

```bash
curl -X DELETE "http://localhost:8000/documents" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"document_ids": [42, 43, 44]}'
```

## Chunking Endpoints

### Chunk Documents (Batch)

```
POST /chunk
```

**Purpose**: Processes multiple documents into chunks and creates vector embeddings for semantic search. Documents are processed asynchronously in the background.

**Request body**:

```json
{
  "document_ids": [42, 43, 44],
  "chunking_method": "recursive",
  "chunk_size": 512,
  "chunk_overlap": 128,
  "threshold": 0.8
}
```

**Chunking Methods**:

* `recursive`: Recursive text splitting (default)
* `sentence`: Sentence-based chunking
* `token`: Token-based chunking
* `semantic`: Semantic similarity-based chunking (requires `threshold`)

**Response**:

```json
{
  "message": "Chunking task scheduled for 3 documents",
  "queued_documents": [42, 43, 44],
  "status": "success"
}
```

**Usage Example**: Use this endpoint after document ingestion to prepare documents for semantic search. The chunking process divides documents into semantically meaningful segments and creates vector embeddings.

```bash
curl -X POST "http://localhost:8000/chunk" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "document_ids": [42, 43],
    "chunking_method": "semantic",
    "chunk_size": 512,
    "chunk_overlap": 128,
    "threshold": 0.8
  }'
```

**Note**: For semantic chunking, the `threshold` parameter controls how similar adjacent chunks should be before they are merged.

### Chunk All Documents

```
POST /chunk/all
```

**Purpose**: Processes all documents in the system into chunks. Useful for batch processing or reprocessing all documents with new chunking parameters.

**Request body**:

```json
{
  "chunking_method": "recursive",
  "chunk_size": 512,
  "chunk_overlap": 128,
  "threshold": 0.8
}
```

**Response**:

```json
{
  "message": "Chunking task scheduled for all documents",
  "queued_documents": [42, 43, 44, 45, 46],
  "status": "success"
}
```

**Usage Example**: Use this endpoint to reprocess all documents with new chunking settings.

```bash
curl -X POST "http://localhost:8000/chunk/all" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "chunking_method": "recursive",
    "chunk_size": 512,
    "chunk_overlap": 128
  }'
```

### Filter/Retrieve Chunks

```
POST /chunks/filter
```

**Purpose**: Retrieves chunks for specific documents. Use this to check if chunking has completed or to retrieve chunk data.

**Request body**:

```json
{
  "document_ids": [42, 43]
}
```

**Response**: Array of chunk objects

```json
[
  {
    "id": "uuid-string",
    "document_id": 42,
    "chunk_text": "This is the content of the first chunk...",
    "chunk_index": 0,
    "embedding": [0.123, 0.456, ...],
    "metadata": {}
  },
  {
    "id": "uuid-string-2",
    "document_id": 42,
    "chunk_text": "This is the content of the second chunk...",
    "chunk_index": 1,
    "embedding": [0.789, 0.012, ...],
    "metadata": {}
  }
]
```

**Usage Example**: Check if documents have been chunked and retrieve their chunks.

```bash
curl -X POST "http://localhost:8000/chunks/filter" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"document_ids": [42, 43]}'
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
