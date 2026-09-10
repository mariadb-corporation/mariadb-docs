---
title: AI
description: >-
  Build AI features on MariaDB. Store and search vector embeddings in SQL,
  connect your AI framework, and give an agent access with the MCP server and
  RAG tools.
icon: robot
---

# AI

Build AI features on the data you already have, in SQL. MariaDB stores embedding vectors in a `VECTOR` column, indexes them, and finds the nearest matches to a query vector with the SQL you already write. Vector search ships in the server itself, so it is there for Community Server and Enterprise Server alike, with no plugin to install and no separate product to buy. Around it are the framework integrations, the MCP server that lets an agent query your database, and the RAG tooling that ties it all into retrieval augmented generation. The guides below get you from a first vector to a working AI feature.

**Store and search vectors.** Vectors are the foundation, so start there. The vector overview explains how vectors, distance functions, and vector indexes work, and it is the page to read before you design a schema. The create table guide gives you the exact syntax for a `VECTOR` column and its index, the schema every vector feature rests on. Want search that blends meaning with keywords? The hybrid search guide uses reciprocal rank fusion to merge the two rankings, so a query gets the best of both.

**Connect your AI framework.** Most AI applications generate embeddings in a framework rather than raw SQL. The framework integrations page connects MariaDB as a vector store to the common AI development frameworks, so the embeddings your application creates land in the database and are searched with the same SQL. For an app you already run, this is usually the shortest path to a working retrieval feature.

**Give an agent the database.** To put MariaDB behind an agent, the Enterprise MCP Server exposes it through the Model Context Protocol, so an agent can inspect schemas and run read only SQL under controlled access. The AI RAG tool assembles a retrieval pipeline over your data, pairing the vector search in the database with a language model.

Start with a `VECTOR` column, get a similarity query running, then build outward.

## Store and search vectors

{% content-ref url="{server}/reference/sql-structure/vectors/vector-overview" %}
[Vector Overview]({server}/reference/sql-structure/vectors/vector-overview)
{% endcontent-ref %}

{% content-ref url="{server}/reference/sql-structure/vectors/create-table-with-vectors" %}
[Create a Table with Vectors]({server}/reference/sql-structure/vectors/create-table-with-vectors)
{% endcontent-ref %}

{% content-ref url="{server}/reference/sql-structure/vectors/optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf" %}
[Hybrid Search with Reciprocal Rank Fusion]({server}/reference/sql-structure/vectors/optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf)
{% endcontent-ref %}

## Connect your AI framework

{% content-ref url="{server}/reference/sql-structure/vectors/vector-framework-integrations" %}
[Vector Framework Integrations]({server}/reference/sql-structure/vectors/vector-framework-integrations)
{% endcontent-ref %}

## Give an agent access to the database

{% content-ref url="{tools}/mariadb-enterprise-mcp-server/architecture" %}
[Enterprise MCP Server Architecture]({tools}/mariadb-enterprise-mcp-server/architecture)
{% endcontent-ref %}

{% content-ref url="{tools}/mariadb-ai-rag" %}
[MariaDB AI RAG]({tools}/mariadb-ai-rag)
{% endcontent-ref %}
