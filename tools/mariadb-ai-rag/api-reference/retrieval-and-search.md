# Retrieval and Search

## Retrieval and Search Endpoints

### Semantic Retrieval

```
POST /retrieve
```

**Purpose**: Performs semantic search to retrieve relevant document chunks based on a query using vector similarity.

**Request body**:

```json
{
  "query": "What is MariaDB AI RAG?",
  "top_k": 20,
  "document_ids": [42, 43]
}
```

**Request Parameters**:

* `query` (required): The search query
* `top_k` (optional): Number of results to return (default: 20)
* `document_ids` (optional): Filter results to specific document IDs (default: all documents)

**Response**: Array of retrieval results

```json
[
  {
    "id": "uuid-chunk-id",
    "document_id": 42,
    "content": "MariaDB AI RAG is an enterprise-grade RAG solution...",
    "metadata": {},
    "distance": 0.15
  },
  {
    "id": "uuid-chunk-id-2",
    "document_id": 43,
    "content": "Key features include document processing and semantic search...",
    "metadata": {},
    "distance": 0.23
  }
]
```

**Response Fields**:

* `id`: Unique chunk identifier
* `document_id`: ID of the source document
* `content`: The chunk text content
* `metadata`: Additional metadata about the chunk
* `distance`: Vector distance (lower = more similar)

**Usage Example**: Use this endpoint to find semantically relevant information. The system converts your query into a vector embedding and finds the most similar chunks.

```bash
curl -X POST "http://localhost:8000/retrieve" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What is MariaDB AI RAG?",
    "top_k": 5,
    "document_ids": [42, 43]
  }'
```

### Full-Text Search

```
POST /search
```

**Purpose**: Performs full-text search using MariaDB's FULLTEXT index to find relevant document chunks.

**Request body**:

```json
{
  "query": "MariaDB features",
  "top_k": 10,
  "document_ids": [42, 43]
}
```

**Request Parameters**:

* `query` (required): The search query
* `top_k` (optional): Number of results to return (default: 10)
* `document_ids` (optional): Filter results to specific document IDs

**Response**: Array of search results

```json
[
  {
    "id": "uuid-chunk-id",
    "document_id": 42,
    "source": "/uploaded_files/product_overview.pdf",
    "content": "MariaDB features include vector search, full-text indexing...",
    "score": 15.5
  },
  {
    "id": "uuid-chunk-id-2",
    "document_id": 43,
    "source": "/uploaded_files/technical_docs.pdf",
    "content": "Additional MariaDB capabilities for enterprise applications...",
    "score": 12.3
  }
]
```

**Response Fields**:

* `id`: Unique chunk identifier
* `document_id`: ID of the source document
* `source`: File path of the source document
* `content`: The chunk text content
* `score`: Relevance score (higher = more relevant)

**Usage Example**: Use this endpoint for keyword-based search when you need exact term matching.

```bash
curl -X POST "http://localhost:8000/search" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "MariaDB features",
    "top_k": 10
  }'
```

### Hybrid Search

```
POST /hybrid_search
```

**Purpose**: Combines semantic search (vector similarity) and full-text search using Reciprocal Rank Fusion (RRF) for optimal results.

**Request body**:

```json
{
  "query": "MariaDB vector capabilities",
  "top_k": 20,
  "k": 60,
  "provider": "openai",
  "model": "text-embedding-3-small",
  "document_ids": [42, 43]
}
```

**Request Parameters**:

* `query` (required): The search query
* `top_k` (optional): Number of results to return (default: 20)
* `k` (optional): RRF parameter for rank fusion (default: 60)
* `provider` (optional): Embedding provider for semantic search
* `model` (optional): Embedding model for semantic search
* `document_ids` (optional): Filter results to specific document IDs

**Response**: Array of hybrid search results

```json
[
  {
    "id": "uuid-chunk-id",
    "document_id": 42,
    "source": "/uploaded_files/product_overview.pdf",
    "content": "MariaDB vector capabilities enable semantic search...",
    "metadata": {},
    "distance": 0.18,
    "score": 14.2
  },
  {
    "id": "uuid-chunk-id-2",
    "document_id": 43,
    "source": "/uploaded_files/technical_docs.pdf",
    "content": "Vector indexing in MariaDB provides fast similarity search...",
    "metadata": {},
    "distance": 0.25,
    "score": 11.8
  }
]
```

**Response Fields**:

* `id`: Unique chunk identifier
* `document_id`: ID of the source document
* `source`: File path of the source document
* `content`: The chunk text content
* `metadata`: Additional metadata about the chunk
* `distance`: Vector distance from semantic search (lower = more similar)
* `score`: Full-text relevance score (higher = more relevant)

**Usage Example**: Use this endpoint for the best of both worlds - combining semantic understanding with keyword matching.

```bash
curl -X POST "http://localhost:8000/hybrid_search" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "MariaDB vector capabilities",
    "top_k": 10,
    "k": 60
  }'
```

### Generate Text

```
POST /generate
```

**Purpose**: Generates a response to a query using a language model and the provided context chunks.

**Request body**:

```json
{
  "query": "Explain MariaDB AI RAG features",
  "chunks": [
    "MariaDB AI RAG is an enterprise-grade RAG solution that integrates with MariaDB...",
    "Key features include document processing, semantic search, and AI-powered responses..."
  ],
  "llm_provider": "openai",
  "llm_model": "gpt-4",
  "temperature": 0.7,
  "top_p": 0.9,
  "max_tokens": 1000
}
```

**Request Parameters**:

* `query` (required): The user's question or prompt
* `chunks` (required): Array of context chunks to use for generation
* `llm_provider` (optional): LLM provider - `openai`, `anthropic`, `gemini`, `cohere`, `ollama`, `azure`, `bedrock`
* `llm_model` (optional): Specific model to use (e.g., `gpt-4`, `claude-3-opus`)
* `temperature` (optional): Controls randomness (0.0-2.0, default: 0.7)
* `top_p` (optional): Nucleus sampling parameter (0.0-1.0, default: 0.9)
* `max_tokens` (optional): Maximum tokens to generate (1-8192, default: 500)

**Response**:

```json
{
  "response": "MariaDB AI RAG is an enterprise-grade Retrieval-Augmented Generation (RAG) solution that seamlessly integrates with MariaDB. Its key features include..."
}
```

**Usage Example**: Use this endpoint after retrieving relevant chunks to generate a coherent response based on the information in those chunks.

```bash
curl -X POST "http://localhost:8000/generate" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain MariaDB AI RAG features",
    "chunks": ["chunk1", "chunk2"],
    "llm_provider": "openai",
    "llm_model": "gpt-4",
    "temperature": 0.7
  }'
```

### Asynchronous Generation

```
POST /generate-async
```

**Purpose**: Generates a response asynchronously, useful for long-running generation tasks.

**Request body**: Same as `/generate`

**Response**: Same as `/generate`

**Usage Example**: Use this endpoint for generation tasks that may take longer to complete.

```bash
curl -X POST "http://localhost:8000/generate-async" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Provide a detailed analysis",
    "chunks": ["chunk1", "chunk2"],
    "llm_provider": "openai",
    "llm_model": "gpt-4"
  }'
```

### Streaming Generation

```
POST /generate-stream
```

**Purpose**: Generates a response with streaming output (Server-Sent Events), allowing for real-time display of results as tokens are generated.

**Request body**: Same as `/generate`

**Response**: Server-Sent Events (SSE) stream with the following event types:

```json
// Start event
{"type": "start", "provider": "openai", "model": "gpt-4"}

// Token events (streamed as generated)
{"type": "token", "content": "MariaDB", "chunk_index": 1}
{"type": "token", "content": " Data", "chunk_index": 2}
{"type": "token", "content": " Bridge", "chunk_index": 3}

// Completion event
{"type": "complete", "duration": 2.5, "chunks_streamed": 150}

// Error event (if error occurs)
{"type": "error", "message": "Error description"}
```

**Usage Example**: Use this endpoint for a better user experience when generating longer responses, as it allows displaying partial results as they become available.

```bash
curl -X POST "http://localhost:8000/generate-stream" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain MariaDB AI RAG features",
    "chunks": ["chunk1", "chunk2"],
    "llm_provider": "openai",
    "llm_model": "gpt-4"
  }'
```
