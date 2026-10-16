---
title: AI
description: >-
  Build AI features on MariaDB: work with a coding agent, store and search vectors in SQL, and connect retrieval to your AI framework.
icon: robot
---

# AI

There are two sides to AI on MariaDB. One is the application you're building, where MariaDB stores embeddings in a native `VECTOR` column and finds the nearest matches with ordinary SQL. The other is how you build it, with a coding agent that knows MariaDB and can reach a database while it works with you.

Vector search is part of the server in MariaDB Community Server and MariaDB Enterprise Server from version 11.7, with no plugin or extension to install. Because the vectors sit in the same tables as the rest of your data, a similarity search and the filters and joins around it run as one query.

## Work With a Coding Agent

Give your agent MariaDB knowledge and a database to work against.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>MariaDB AI Plugins</strong></td><td>Skills, an MCP server, and a local sandbox server for Claude Code, Codex, Pi, Hermes Agent, and OpenCode.</td><td><a href="https://github.com/mariadb/ai-plugins">ai-plugins</a></td></tr><tr><td><strong>Docs MCP Server</strong></td><td>Point your agent at these docs so it reads current MariaDB syntax instead of guessing.</td><td><a href="README.md#keep-your-agent-in-the-docs">README.md#keep-your-agent-in-the-docs</a></td></tr><tr><td><strong>MariaDB Enterprise MCP Server</strong></td><td>Give agents controlled access to production databases, with authentication and permissions you set.</td><td><a href="{tools}/mariadb-enterprise-mcp-server/introduction">introduction</a></td></tr></tbody></table>

## Store and Search Vectors

Read the overview before you design a schema. It explains distance functions and vector indexes.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Vector Overview</strong></td><td>What a vector column is, how similarity search works, and when to add a vector index.</td><td><a href="{server}/reference/sql-structure/vectors/vector-overview">vector-overview</a></td></tr><tr><td><strong>Create a Table With Vectors</strong></td><td>The exact syntax for a <code>VECTOR</code> column and its index.</td><td><a href="{server}/reference/sql-structure/vectors/create-table-with-vectors">create-table-with-vectors</a></td></tr><tr><td><strong>Hybrid Search</strong></td><td>Combine vector similarity with keyword matching using reciprocal rank fusion.</td><td><a href="{server}/reference/sql-structure/vectors/optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf">optimizing-hybrid-search-query-with-reciprocal-rank-fusion-rrf</a></td></tr></tbody></table>

## Build Retrieval

Most applications create embeddings in a framework and keep them in the database.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Framework Integrations</strong></td><td>Use MariaDB as the vector store for LangChain, LlamaIndex, Spring AI, and other frameworks.</td><td><a href="{server}/reference/sql-structure/vectors/vector-framework-integrations">vector-framework-integrations</a></td></tr><tr><td><strong>Vector Search Workshop</strong></td><td>A hands-on workshop that builds semantic search on MariaDB from the ground up.</td><td><a href="https://github.com/mariadb-developers/vector-search-workshop">vector-search-workshop</a></td></tr><tr><td><strong>RAG Demo in Java</strong></td><td>A retrieval augmented generation app that uses MariaDB for both its data and its vectors.</td><td><a href="https://github.com/mariadb-developers/mariadb-rag-demo-java">mariadb-rag-demo-java</a></td></tr></tbody></table>
