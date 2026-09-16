---
title: AI
description: >-
  Build AI features on MariaDB Server. Store and search vector embeddings in SQL,
  connect your AI framework, and give an agent access with the MCP server and
  RAG tools.
icon: robot
---

# AI

MariaDB Server stores embedding vectors in a `VECTOR` column, indexes them, and returns the nearest matches to a query vector using ordinary SQL. Vector search is built into the server itself, available in both MariaDB Community Server and MariaDB Enterprise Server from version 11.7, with no plugin or extension to install. Around it sit the framework integrations, an MCP server that gives an agent controlled access to the database, and tooling for retrieval augmented generation.

Keeping the vectors next to the relational data they describe is the practical advantage. A similarity search and the joins and filters that qualify it run as one statement, against one system, inside one transaction.

**Store and search vectors.** Start here. The vector overview explains vectors, distance functions, and vector indexes, and it is the page to read before designing a schema. The create table guide gives the exact syntax for a `VECTOR` column and its index. The hybrid search guide combines vector similarity with keyword matching using reciprocal rank fusion, which is what you want when pure semantic search returns results that are related but wrong.

**Connect your AI framework.** Most applications generate embeddings in a framework rather than in raw SQL. The framework integrations page covers using MariaDB as a vector store for the common AI development frameworks, so embeddings your application creates land in the database and are queried with the same SQL. For an application already in production, this is usually the shortest path to a working retrieval feature.

**Give an agent the database.** The MariaDB Enterprise MCP Server exposes the database over the Model Context Protocol, so an agent can inspect schemas and run read only SQL under access you control. The AI RAG tool assembles a retrieval pipeline that pairs vector search in the database with a language model.

Create a `VECTOR` column, get one similarity query returning rows, then build outward from there.

## Store and Search Vectors

{% content-ref url="explore-by-task/%7Bserver%7D/reference/sql-structure/vectors/vector-overview/" %}
[vector-overview](explore-by-task/%7Bserver%7D/reference/sql-structure/vectors/vector-overview/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/reference/sql-structure/vectors/create-table-with-vectors/" %}
[create-table-with-vectors](explore-by-task/%7Bserver%7D/reference/sql-structure/vectors/create-table-with-vectors/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/reference/sql-structure/vectors/optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf/" %}
[optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf](explore-by-task/%7Bserver%7D/reference/sql-structure/vectors/optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf/)
{% endcontent-ref %}

## Connect Your AI Framework

{% content-ref url="explore-by-task/%7Bserver%7D/reference/sql-structure/vectors/vector-framework-integrations/" %}
[vector-framework-integrations](explore-by-task/%7Bserver%7D/reference/sql-structure/vectors/vector-framework-integrations/)
{% endcontent-ref %}

## Give an Agent Access to the Database

{% content-ref url="explore-by-task/%7Btools%7D/mariadb-enterprise-mcp-server/architecture/" %}
[architecture](explore-by-task/%7Btools%7D/mariadb-enterprise-mcp-server/architecture/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Btools%7D/mariadb-ai-rag/" %}
[mariadb-ai-rag](explore-by-task/%7Btools%7D/mariadb-ai-rag/)
{% endcontent-ref %}
