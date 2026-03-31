---
description: >-
  MariaDB AI RAG exposes a comprehensive RESTful API for programmatic
  interaction with the system. All API endpoints require authentication except
  for the login endpoint.
icon: paperclip
---

# API Reference

The MariaDB AI RAG API provides a comprehensive RESTful interface for document ingestion, chunking, retrieval, and AI-powered generation. All endpoints require JWT authentication except for the login endpoint.

## Available API Documentation

### [API Reference](api-reference.md)

Complete reference for all API endpoints including:

* Document ingestion and management
* Chunking operations
* Retrieval and search
* AI generation
* Batch operations

### [Access Control](access-control.md)

Authentication and authorization documentation:

* JWT-based authentication
* User management endpoints
* Role-based access control
* Document sharing and permissions
* User directory management

### [Database Integration](database-integration.md)

Direct database ingestion capabilities:

* SQL query ingestion
* Table and view ingestion
* Role-based database access
* Structured data processing

### [Orchestration](orchestration.md)

High-level workflow endpoints:

* Full pipeline orchestration
* Ingestion orchestration
* Generation orchestration
* Multi-step RAG workflows

## Quick Start

All API requests require authentication. First, obtain a JWT token:

```bash
curl -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=user@example.com&password=your_password"
```

Then include the token in subsequent requests:

```bash
curl -X GET "http://localhost:8000/documents" \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## Base URL

The default base URL for the API is:

```
http://localhost:8000
```

For production deployments, replace with your configured host and port.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
