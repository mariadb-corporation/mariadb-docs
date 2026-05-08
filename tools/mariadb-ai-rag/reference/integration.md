---
description: >-
  Integration guide for connecting MariaDB AI RAG to external applications,
  with Python REST API examples for authentication, document upload,
  chunking, and middleware setup.
---

# Integration

## External Systems

MariaDB AI RAG can be integrated with external systems through its REST API. Common integration patterns include:

* **Document Management Systems**: Automatically ingest documents from DMS platforms using the document ingestion endpoints
* **Knowledge Bases**: Enhance existing knowledge bases with AI-powered search via the retrieval endpoints
* **Customer Support Systems**: Integrate with ticketing systems for AI-assisted responses using the orchestration pipeline
* **Business Intelligence Tools**: Connect BI tools for natural language querying of data through the API

Example integration with a document management system:

```python
import requests
import json

# Authenticate
auth_response = requests.post(
    "http://localhost:8000/token",
    data={"username": "user@example.com", "password": "secure_password"}
)
token = auth_response.json()["access_token"]

# Upload document
with open("document.pdf", "rb") as f:
    files = {"file": ("document.pdf", f, "application/pdf")}
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(
        "http://localhost:8000/documents/ingest",
        files=files,
        headers=headers
    )

document_id = response.json()["id"]

# Process document
chunking_response = requests.post(
    "http://localhost:8000/chunks/document",
    json={"document_id": document_id},
    headers={"Authorization": f"Bearer {token}"}
)
```

## Authentication Integration

MariaDB AI RAG uses JWT-based authentication. The system can be integrated with existing authentication systems by implementing custom authentication middleware.

```
# JWT Authentication settings
SECRET_KEY=your_secure_random_string
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
