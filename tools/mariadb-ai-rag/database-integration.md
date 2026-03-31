# Database Integration

## Database Integration Endpoints

### Ingest from Database Table

```
POST /documents/ingest-from-table
```

**Purpose**: Ingests data directly from a MariaDB table or view, treating it as a CSV data source. This allows for seamless integration with existing database content.

**Request body**:

```json
{
  "table_name": "customer_feedback",
  "schema_name": "databridge",
  "column_mapping": {
    "content": "feedback_text",
    "metadata": ["customer_id", "product_id", "rating", "date_submitted"],
    "id_column": "feedback_id"
  },
  "filter_condition": "rating >= 3 AND date_submitted > '2025-01-01'",
  "batch_size": 1000,
  "authorized_users": ["user1@example.com", "user2@example.com"]
}
```

**Response**:

```json
{
  "job_id": "db_ingest_xyz123",
  "status": "processing",
  "table_name": "customer_feedback",
  "estimated_rows": 5230,
  "authorized_users": ["user1@example.com", "user2@example.com"]
}
```

**Usage Example**: Use this endpoint to ingest structured data from your database tables or views. The system will process each row as a document, with specified columns as content and metadata.

```bash
curl -X POST "http://localhost:8000/documents/ingest-from-table" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"table_name": "customer_feedback", "schema_name": "databridge", "column_mapping": {"content": "feedback_text", "metadata": ["customer_id", "product_id", "rating", "date_submitted"], "id_column": "feedback_id"}, "authorized_users": ["user1@example.com"]}'
```

### Ingest from SQL Query

```
POST /documents/sql-ingest
```

**Purpose**: Executes a SELECT query and ingests the results as a CSV document. The query results are stored as a document that can be chunked and searched. This provides a way to make database query results searchable via RAG.

**Request body**:

```json
{
  "sql_query": "SELECT id, title, content, author, published_date FROM articles WHERE status = 'published' AND category = 'technical'",
  "role": "ai_nexus",
  "document_name": "published_articles"
}
```

**Request Parameters**:

* `sql_query` (required): A SELECT query to execute (only SELECT queries are allowed)
* `role` (optional): Database role to use for query execution (default: from `DEFAULT_SQL_ROLE` environment variable)
* `document_name` (optional): Name for the generated CSV document (default: "query\_results")

**Security Notes**:

* Only SELECT queries are allowed (enforced by regex validation)
* Multiple statements are not allowed (no semicolons outside of quoted strings)
* User must have permission to use the specified role
* Query is executed using MariaDB's role-based access control

**Response**:

```json
{
  "id": 42,
  "source": "sql://generated/1729425000/published_articles.csv",
  "filename": "published_articles.csv",
  "status": "completed",
  "content": "id,title,content,author,published_date\n1,Article Title,Article content...,John Doe,2025-01-15\n...",
  "error_message": null,
  "created_at": "2025-10-20T12:00:00.123456",
  "updated_at": "2025-10-20T12:00:01.234567"
}
```

**Usage Example**: Query database and ingest results for RAG search.

```bash
curl -X POST "http://localhost:8000/documents/sql-ingest" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "sql_query": "SELECT id, title, content, author FROM articles WHERE status = '\''published'\''",
    "role": "ai_nexus",
    "document_name": "published_articles"
  }'
```

**Note**: The query results are converted to CSV format and stored as a document. You can then chunk this document using the chunking endpoints to make the data searchable.

### Check Database Ingestion Status

```
GET /documents/ingest-status/{job_id}
```

**Purpose**: Checks the status of a database ingestion job.

**Response**:

```json
{
  "job_id": "db_ingest_xyz123",
  "status": "completed",
  "processed_rows": 5230,
  "created_documents": 5230,
  "failed_rows": 0,
  "completion_time": "2025-08-25T12:34:56.789Z",
  "authorized_users": ["user1@example.com", "user2@example.com"]
}
```

**Usage Example**: Use this endpoint to monitor the progress of database ingestion jobs.

```bash
curl "http://localhost:8000/documents/ingest-status/db_ingest_xyz123" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
