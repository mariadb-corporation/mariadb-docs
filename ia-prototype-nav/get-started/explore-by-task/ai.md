---
title: AI
description: >-
  Build AI features on MariaDB. Store and search vector embeddings in SQL,
  connect AI frameworks, and use the MCP server and RAG tools.
icon: robot
---

# AI

MariaDB supports AI application patterns directly in the database. The central piece is vector search: MariaDB stores embedding vectors in a `VECTOR` column, indexes them, and finds the nearest matches to a query vector with SQL. This capability ships in the server itself, so it is available to Community Server and Enterprise Server users alike, not held behind a separate product or a plugin you install. Around it sit the framework integrations, the MCP server that lets an AI agent query MariaDB, and the RAG tooling that assembles retrieval augmented generation on top of your data. This page brings those pieces together, because a working AI feature usually uses more than one of them.

Start with vectors, because they are the foundation the rest builds on. The vector overview explains how vectors, distance functions, and vector indexes work in MariaDB, and it is the page to read before you design a schema. The create table guide then shows the exact syntax for a `VECTOR` column and its index, which is the schema every vector feature sits on. For search that combines vector similarity with keyword matching, the hybrid search guide covers reciprocal rank fusion, a method that merges the two rankings into one result set, so a query benefits from both semantic and exact matches rather than choosing between them.

Most AI applications are built with a framework rather than raw SQL, and you generate embeddings in that framework before storing them. The framework integrations page covers connecting MariaDB as a vector store to the common AI development frameworks, so the embeddings your application creates land in the database and are searched with the same SQL described above. This is usually the shortest path from an existing application to a working retrieval feature, because it reuses the stack you already have.

Two tools connect MariaDB to an AI agent rather than to your application code. The Enterprise MCP Server exposes the database through the Model Context Protocol, so an agent can inspect schemas and run read only SQL against MariaDB under controlled access. The AI RAG tool assembles a retrieval augmented generation pipeline over your data, combining the vector search in the database with a language model. Reach for these when you are building an agent or a question answering system rather than adding search to an application you already run.

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
