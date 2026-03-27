---
hidden: true
noIndex: true
icon: rabbit
---

# Getting Started

MariaDB AI RAG enables organizations to leverage their own document repositories for AI-powered search and response generation. By combining MariaDB’s native vector search with advanced layout extraction and reranking, the system provides accurate, context-aware answers based strictly on your private data.

### System Architecture: "The Team"

The solution is deployed as a multi-container Docker stack where each component has a specialized role:

* rag-api (The Main Brain): A FastAPI server that handles authentication, manages endpoints, and orchestrates the RAG pipeline.
* mcp-server (The AI Gateway): A dedicated "VIP entrance" for AI agents and IDEs (like Windsurf or Cursor) to interact with your data.
* rag-redis (The Waiting Room): A message broker that stores tasks, such as processing large documents, ensuring the API remains responsive.
* rag-celery-worker (The Librarian): A background process that picks up tasks from Redis to extract text, create chunks, and generate vectors.
* rag-docling-ray (The Document Specialist): A specialist service that reads complex PDF layouts, tables, and multi-columns to ensure high-quality text extraction.
* rag-mariadb (The Database): MariaDB 11.8+ serves as the foundation, natively supporting both relational data and vector storage.

### The Deployment Roadmap

To get your system running, follow these high-level steps:

### Step A: Prerequisites

Ensure your host machine (Linux, macOS, or Windows with WSL2) has Docker and Docker Compose installed. You will also need:

* A valid MariaDB License Key.
* API Keys for your chosen AI providers (e.g., Google Gemini or OpenAI).

### Step B: Obtain Assets

Download the following files from the public AI RAG GitHub repository:

1. `docker-compose.yml`: The blueprint for the container stack.
2. `config.env.template`: The configuration template for your environment variables.

### Step C: Configuration

Copy the template to a new file named `config.env.secure` and update the mandatory fields:

* `MARIADB_LICENSE_KEY`: Your validated license.
* `GEMINI_API_KEY`: Your AI provider key.
* `DB_PASSWORD`: A secure password for your MariaDB instance.

### Step D: Launch

Open your terminal in the deployment folder and run:

```bash
docker compose up -d
```

Once the containers are "Healthy," access the interactive API documentation at `http://localhost:8000/docs`.

### Key 1.1 Capabilities

Once deployed, you can leverage these advanced features:

* Layout-Aware Extraction: Use Docling (Built-in/Local) or LlamaParse (Public Endpoint) to preserve complex document structures like tables and headers.
* Intelligent Reranking: Enable a "second pass" search using FlashRank (Local) or Cohere (Public Endpoint) to significantly improve result relevance.
* Automated Citations: AI responses automatically include footnotes or superscripts pointing to the exact document and page used for the answer.
* Bulk Cloud Ingestion: Connect directly to AWS S3, Google Cloud Storage, or MinIO to sync thousands of documents automatically.

### Next Steps

1. Authenticate: Generate your first JWT token via the `/token` endpoint.
2. Integrate: Connect your cloud storage bucket via the `/integrations` API.
3. Ingest: Use the Orchestration pipeline to process and vectorize your first documents.
4. Query: Ask questions against your data and receive citation-backed answers
