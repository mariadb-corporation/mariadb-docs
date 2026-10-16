---
title: AI
description: Add semantic search to your data with native vector search in SQL, and build it alongside a coding agent that knows MariaDB.
icon: robot
---

# AI

Agentic applications need their data and their embeddings in one place, and MariaDB Server keeps both in the same tables. Vector search is built into MariaDB Community Server from 11.7 and MariaDB Enterprise Server from 11.4.5-3, so you don't install a plugin or an extension. The steps below add semantic search to the `shop.products` table from the landing page, then point you at the tools that let a coding agent build the rest with you.

## Add Semantic Search to the Shop

{% stepper %}
{% step %}
### Store an Embedding for Each Product

An embedding is a list of numbers that an AI model produces from content, such as a product description, so that similar meanings land close together. Create a table that holds one `VECTOR` value per product, with a `VECTOR INDEX` built for cosine distance:

```sql
CREATE TABLE shop.product_embeddings (
  product_id INT PRIMARY KEY,
  embedding  VECTOR(4) NOT NULL,
  VECTOR INDEX (embedding) DISTANCE=cosine
);
```

The indexed column must be `NOT NULL`, and a table can have only one vector index. [CREATE TABLE with Vectors]({server}/reference/sql-structure/vectors/create-table-with-vectors) covers the `M` and `DISTANCE` options.
{% endstep %}

{% step %}
### Insert the Vectors

The `VEC_FromText` function turns a JSON array of numbers into a vector value. Every row must have the same number of dimensions as the column, which is four here:

```sql
INSERT INTO shop.product_embeddings (product_id, embedding) VALUES
  (1, VEC_FromText('[0.91, 0.12, 0.30, 0.05]')),
  (2, VEC_FromText('[0.20, 0.88, 0.35, 0.10]')),
  (3, VEC_FromText('[0.15, 0.10, 0.20, 0.95]'));
```

The [VEC\_FromText reference]({server}/reference/sql-functions/vector-functions/vec_fromtext) shows the binary format it produces, which is four bytes per dimension.
{% endstep %}

{% step %}
### Find the Nearest Products

Embed the search phrase with the same model, then sort by the `VEC_DISTANCE_COSINE` function and take the top rows. Sorting with `ORDER BY` and stopping at a `LIMIT` is the shape that lets the optimizer use the vector index. The join to the `products` table brings back names in the same query.

```sql
SELECT p.name,
       VEC_DISTANCE_COSINE(e.embedding, VEC_FromText('[0.85, 0.20, 0.25, 0.10]')) AS distance
FROM shop.product_embeddings AS e
JOIN shop.products AS p ON p.id = e.product_id
ORDER BY distance
LIMIT 2;
```

```
+---------------+---------------------+
| name          | distance            |
+---------------+---------------------+
| Desk lamp     | 0.00688833819260537 |
| Standing desk |  0.5012322990863076 |
+---------------+---------------------+
```

A smaller distance means a closer match. For an index built with `DISTANCE=euclidean`, sort by the `VEC_DISTANCE_EUCLIDEAN` function instead. [Using the vector index efficiently]({server}/reference/sql-structure/vectors/vector-overview#using-the-vector-index-efficiently) lists the query patterns that fall back to a full table scan.
{% endstep %}
{% endstepper %}

{% hint style="info" %}
Four dimensions keep the example readable. Real embedding models produce hundreds or thousands of dimensions per value, for example `VECTOR(768)` or `VECTOR(1536)`, and you generate them in your application code or AI framework, not by hand.
{% endhint %}

## Work With a Coding Agent

Give your agent MariaDB skills, the current docs, and a controlled path to your databases.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MariaDB AI Plugins</strong></td><td>Skills, an MCP server, and a local sandbox server for Claude Code, Codex, Pi, Hermes Agent, and OpenCode.</td><td><a href="https://github.com/mariadb/ai-plugins">ai-plugins</a></td></tr><tr><td><strong>Docs MCP Server</strong></td><td>Add <code>https://mariadb.com/docs/~gitbook/mcp</code> to your agent so it reads current MariaDB syntax instead of guessing.</td><td><a href="README.md#keep-your-agent-in-the-docs">README.md#keep-your-agent-in-the-docs</a></td></tr><tr><td><strong>MariaDB Enterprise MCP Server</strong></td><td>Give agents access to production databases, with the authentication and permissions you set.</td><td><a href="{tools}/mariadb-enterprise-mcp-server/introduction">introduction</a></td></tr></tbody></table>

## Go Deeper on Vectors

Read the overview before you design a production schema, then pick the retrieval pattern and framework that fit your application.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Vector Overview</strong></td><td>The <code>VECTOR</code> data type, the HNSW-based vector index, distance functions, and the versions of MariaDB Server that include them.</td><td><a href="{server}/reference/sql-structure/vectors/vector-overview">vector-overview</a></td></tr><tr><td><strong>Hybrid Search</strong></td><td>Merge vector similarity and full-text keyword results into one ranking with reciprocal rank fusion.</td><td><a href="{server}/reference/sql-structure/vectors/optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf">optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf</a></td></tr><tr><td><strong>Framework Integrations</strong></td><td>Use MariaDB as the vector store for LangChain, LlamaIndex, Spring AI, and other AI, web, and ORM frameworks.</td><td><a href="{server}/reference/sql-structure/vectors/vector-framework-integrations">vector-framework-integrations</a></td></tr></tbody></table>

## Clone a Sample

MariaDB maintains these open source projects on GitHub, and each README has the setup steps.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Vector Search Workshop</strong></td><td>Learn semantic search step by step with LangChain and MariaDB, in Python.</td><td><a href="https://github.com/mariadb-developers/vector-search-workshop">vector-search-workshop</a></td></tr><tr><td><strong>RAG Demo in Java</strong></td><td>Retrieval augmented generation with MariaDB vector search and the OpenAI API.</td><td><a href="https://github.com/mariadb-developers/mariadb-rag-demo-java">mariadb-rag-demo-java</a></td></tr><tr><td><strong>Semantic Search Web App</strong></td><td>A semantic search demo built with MariaDB, LangChain, FastAPI, and NiceGUI.</td><td><a href="https://github.com/mariadb-developers/langchain-fastapi-mariadb-webinar-demo">langchain-fastapi-mariadb-webinar-demo</a></td></tr></tbody></table>
