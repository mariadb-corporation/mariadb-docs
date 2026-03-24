# Configuration Guide (config.env)

This guide provides a comprehensive reference for all environment variables available in the `config.env.secure` file. Proper configuration of these variables is essential for securing your deployment, connecting to AI providers, and optimizing search accuracy.

## Mandatory License Key

The system performs a mandatory validation check at startup.

* `MARIADB_LICENSE_KEY`: [Your unique alphanumeric token](../deployment/overview.md#obtain-and-configure-the-mariadb-license-key) retrieved from the MariaDB Customer Portal.

{% hint style="info" %}
License Validity: MariaDB Trial License Keys are valid for 30 days from the date of generation. You may generate multiple licenses based on your subscription tier.
{% endhint %}

## Security & Unified Authentication

These variables establish a "secret handshake" between the RAG API and the MCP Server.

### The "Three-Key Rule"

For the system to function as a unified stack, you must set the following three variables to the exact same value. If these do not match, AI agents (such as Windsurf or Cursor) will be unable to authenticate with the RAG pipeline.

* `SECRET_KEY`: Primary secret for application security.
* `JWT_SECRET_KEY`: Used for generating and validating user session tokens.
* `MCP_AUTH_SECRET_KEY`: Specific key for the Model Context Protocol gateway.

**Secure Key Generation**

```
Do not use simple passwords. Generate a unique 32-character hex string to assign to all three variables using your terminal:
```

```bash
openssl rand -hex 32
```

### 3. Database Configuration

AI RAG 1.1 requires a MariaDB 11.8+ database to store documents, metadata, and vector embeddings.

### Common Database Variables

These variables are required regardless of your hosting model:

* `DB_PORT`: The port MariaDB listens on (Default: `3306`).
* `DB_USER`: Database username (e.g., `root`).
* `DB_PASSWORD`: Password for the database user.
* `DB_NAME`: The specific schema name (e.g., `rag_db`).

### Hosting Options (`DB_HOST`)

Select the appropriate hostname based on your deployment:

| **Hosting Scenario** | **DB\_HOST Value**       | **Description**                                                              |
| -------------------- | ------------------------ | ---------------------------------------------------------------------------- |
| Docker-Hosted        | `mariadb`                | Used when running the MariaDB container included in the Docker Compose file. |
| On-Premise / Local   | `127.0.0.1` or Server IP | Used for local development or existing network servers.                      |
| Cloud-Hosted         | Cloud Endpoint URL       | Used for managed services like MariaDB SkySQL, AWS RDS, or Azure.            |

\{% hint style="danger" %\}

SSL Mandatory for Cloud Databases: If your database is hosted in the cloud, you must set `DB_SSL_ENABLED=true`to ensure secure, encrypted communication over the public internet.

\{% endhint %\}

***

### 4. Admin Credentials

These credentials create the initial administrative account for the system.

* `ADMIN_EMAIL`: The email address for the primary admin user.
* `ADMIN_PASSWORD`: The initial password. It is critical to change this immediately after the first login in production environments.

***

### 5. AI Provider Configuration

Configure your Large Language Model (LLM) and Embedding providers.

### LLM Settings

* `LLM_PROVIDER`: Choose your AI provider (e.g., `gemini`, `openai`, or `ollama`).
* `LLM_MODEL`: The specific model name (e.g., `gemini-2.0-flash` or `gpt-4o`).
* `GEMINI_API_KEY` or `OPENAI_API_KEY`: Your provider-specific API key.

### Embedding Settings

* `EMBEDDING_PROVIDER`: Provider for vectorizing text (e.g., `openai`, `gemini`, or `huggingface`).
* `embedding_model`: Specific embedding model (e.g., `text-embedding-3-small`).

***

### 6. Reranking & Search Accuracy

Reranking improves search results by scoring retrieved document chunks for maximum relevance.

* `RERANKING_ENABLED`: Set to `true` to enable the accuracy-boosting secondary search pass.
* `RERANKING_MODEL_TYPE`: Defaults to `flashrank` (high-speed local reranking). Cloud-based `cohere` is also supported.
* `RERANKING_MODEL_NAME`: The specific scoring model. Default: `ms-marco-MiniLM-L-12-v2`.

***

### 7. Advanced Service Mapping

These variables ensure different containers in the Docker stack can find each other.

* `APP_HOST`: Set to `rag-api`.
* `MCP_HOST`: Set to `rag-api`.
* `MCP_MARIADB_HOST`: Set to `rag-api`.
* `DOCLING_RAY_SERVICE_URL`: The internal URL for the layout processing service (Default: `http://rag-docling-ray:8003`).
* `CELERY_BROKER_URL`: The connection string for the Redis message broker (Default: `redis://rag-redis:6379/0`).

\{% include "[https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/\~/reusable/pNHZQXPP5OEz2TgvhFva/](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/)" %\}

\{% @marketo/form formId="4316" %\}

Would you like me to help you draft the Release Notes for AI RAG 1.1 based on the "What's new" document mentioned by Egor?
