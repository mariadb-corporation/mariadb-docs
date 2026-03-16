---
hidden: true
noIndex: true
---

# Configuration

## Overview

This guide covers the basic configuration of the MariaDB AI RAG system. For production deployments and advanced configuration scenarios, please refer to the [Deployment Documentation](../deployment/).

**See Also:**

* [Ubuntu Deployment Guide](../deployment/ubuntu-deployment.md) - Production configuration for Ubuntu/Debian
* [Docker Deployment Guide](../../mariadb-enterprise-operator/docker-images.md) - Container-based deployment configuration
* [Deployment Checklist](../deployment/deployment-checklist.md) - Configuration validation checklist
* [Technical Architecture](../deployment/technical-architecture.md) - System architecture and configuration details

## Configuration File

MariaDB AI RAG uses a `.env` configuration file located in the installation directory. A template is provided at `config.env.template`. Copy this file to `.env` and modify the parameters according to your environment.

```ini
# Database Configuration (Required)
DB_HOST=localhost
DB_PORT=3306
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_NAME=rag_db

# Authentication (Required)
SECRET_KEY=your_secret_key_here_generate_a_secure_random_string

# Embedding Configuration (Required)
EMBEDDING_PROVIDER=openai
EMBEDDING_MODEL=text-embedding-3-small

# API Keys (Set based on your embedding/LLM provider)
OPENAI_API_KEY=your_openai_api_key
GEMINI_API_KEY=your_gemini_api_key
VOYAGE_API_KEY=your_voyage_api_key
COHERE_API_KEY=your_cohere_api_key
```

## Database Initialization

MariaDB AI RAG requires a properly configured database. The system can automatically initialize the database schema during first startup, or you can manually initialize it using the provided SQL script:

```bash
mysql -u username -p database_name < init-db.sql
```

## Security Configuration

### Authentication

MariaDB AI RAG implements JWT-based authentication. Configure the following parameters in your `.env` file:

```ini
SECRET_KEY=your_secure_random_string
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

For production environments, it is strongly recommended to use a properly generated secure random string for the `SECRET_KEY`.

### API Key Management

External service API keys should be securely stored in the `.env` file. In production environments, consider using a secure vault solution or environment variable management system.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
