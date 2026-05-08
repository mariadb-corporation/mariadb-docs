---
description: >-
  MariaDB Enterprise MCP Server provides database introspection and SQL
  tools, vector store and semantic search tools, and RAG orchestration for
  document ingestion and response generation.
---

# Features

The MariaDB Enterprise MCP Server offers a comprehensive suite of tools, categorized into standard database operations, advanced vector functionalities, and workflow orchestration.

## Standard Database Operations

These tools provide fundamental control and insight into your MariaDB environment. By default, operations are read-only (`MCP_READ_ONLY = true`) but can be configured for write access (`MCP_READ_ONLY = false`).

* `list_databases`: Discovers all accessible databases.
* `list_tables`: Enumerates all tables within a specified database.
* `get_table_schema`: Retrieves the detailed schema for a specific table, including column names, data types, keys, and default values.
* `execute_sql`: Executes read-only SQL queries like `SELECT`, `SHOW`, and `DESCRIBE`. Supports parameterized queries for enhanced security.
* `create_database`: Creates a new database if it does not already exist.

## Harnessing the Power of Vectors: Advanced AI Functionality

The server’s integrated vector functionality enables semantic search and other embedding-based operations directly within your database.

### Vector Store Management

* `create_vector_store`: Creates a new table optimized as a vector store. The schema includes columns for `id`, `document`, `embedding` (VECTOR type), and `metadata` (JSON). Users can specify the embedding model and distance function (e.g., cosine, euclidean) at creation.
* `list_vector_stores`: Lists all tables in a database that are identified as vector stores.
* `delete_vector_store`: Securely removes a vector store table.

### Embedding and Search Operations

* `insert_docs_vector_store`: Inserts documents and associated metadata into a vector store. The server manages the generation of embeddings using a configured service.
* `search_vector_store`: Performs semantic similarity searches by generating an embedding for a user query and finding the 'k' most similar documents in the specified vector store.

## Workflow Orchestration

The server exposes powerful orchestration endpoints that allow an AI agent to execute an entire RAG pipeline through a single, secure interface.

* **Ingestion (`/orchestrate/ingestion`)**: Triggers the ingestion of documents into a specified vector store, including the chunking and embedding processes.
* **Generation (`/orchestrate/generation`)**: Executes a query against a set of documents, performing retrieval and generating a final, context-aware response from an LLM.

***

### Tool Summary

| Tool Name                  | Description                                                                                          | Category                     |
| -------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------- |
| `list_databases`           | Discovers all accessible databases.                                                                  | Standard Database Operations |
| `list_tables`              | Enumerates all tables within a specified database.                                                   | Standard Database Operations |
| `get_table_schema`         | Retrieves the detailed schema for a specific table.                                                  | Standard Database Operations |
| `execute_sql`              | Executes read-only SQL queries.                                                                      | Standard Database Operations |
| `create_database`          | Creates a new database if it does not already exist.                                                 | Standard Database Operations |
| `create_vector_store`      | Creates a new table optimized as a vector store.                                                     | Vector & AI Functionality    |
| `list_vector_stores`       | Lists all tables identified as vector stores.                                                        | Vector & AI Functionality    |
| `delete_vector_store`      | Securely removes a vector store table.                                                               | Vector & AI Functionality    |
| `insert_docs_vector_store` | Inserts documents and metadata into a vector store.                                                  | Vector & AI Functionality    |
| `search_vector_store`      | Performs a semantic similarity search on a vector store.                                             | Vector & AI Functionality    |
| `rag_ingestion`            | Triggers the full document ingestion pipeline.                                                       | Workflow Orchestration       |
| `rag_generation`           | Synthesizes retrieved information with the user's query to generate a final, context-aware response. | Workflow Orchestration       |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
