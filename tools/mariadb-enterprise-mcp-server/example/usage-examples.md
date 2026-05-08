---
description: >-
  JSON payload examples for the MariaDB Enterprise MCP Server span SQL
  queries, vector store creation and search, document insertion, and RAG
  generation, each shown as a tool call.
---

# Usage Examples

## Standard SQL Query

{% code overflow="wrap" %}
```json
{ "tool": "execute_sql", "parameters": { "database_name": "test_db", "sql_query": "SELECT * FROM users WHERE id = %s", "parameters": [123] } }
```
{% endcode %}

***

## Create Vector Store

{% code overflow="wrap" %}
```json
{ "tool": "create_vector_store", "parameters": { "database_name": "test_db", "vector_store_name": "my_vectors", "model_name": "text-embedding-3-small", "distance_function": "cosine" } }
```
{% endcode %}

***

## Insert Documents into Vector Store

{% code overflow="wrap" %}
```json
{ "tool": "insert_docs_vector_store", "parameters": { "database_name": "test_db", "vector_store_name": "my_vectors", "documents": ["Sample text 1", "Sample text 2"], "metadata": [{"source": "doc1"}, {"source": "doc2"}] } }
```
{% endcode %}

## Semantic Search

{% code overflow="wrap" %}
```json
{ "tool": "search_vector_store", "parameters": { "database_name": "test_db", "vector_store_name": "my_vectors", "user_query": "What is the capital of France?", "k": 5 } }
```
{% endcode %}

## RAG Generation

{% code overflow="wrap" %}
```json
{ "tool": "rag_generation", "parameters": { "database_name": "test_db", "vector_store_name": "my_vectors", "user_query": "What is the capital of France?", "k": 5, "temperature": 0.9 } }
```
{% endcode %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
