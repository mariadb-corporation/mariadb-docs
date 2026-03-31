# Troubleshooting Guide

This guide provides diagnostic steps and solutions for common issues encountered when deploying MariaDB AI RAG 1.1 (Beta).

### Application Startup Issues

### The RAG Application (rag-api) exits immediately

The most common cause for immediate failure is an invalid, expired, or missing MARIADB\_LICENSE\_KEY. AI RAG performs a mandatory license check at startup and will not run without a validated token.

{% hint style="info" %}
Action Required: Verify your license key in the [`config.env.secure` file.](../reference/configuration-guide-config.env.md)
{% endhint %}

Recommended Steps:

1. Check the application logs to confirm the license failure.
2. Ensure the host has outbound access to port 443 to reach the licensing server (`https://*.mariadb.com`).

```bash
docker compose -f docker-compose.dockerhub-dev.yml logs rag-api
```

### Port is already allocated error

Docker will throw this error if a required port (e.g., 8000 or 3306) is already in use by another program on your machine.

Recommended Steps:

1. Identify the conflicting process using the command below.
2. Stop the conflicting program or modify the port mappings in your `docker-compose.yml` file.

```bash
# Example for port 8000
netstat -ano | findstr :8000
```

### Database and Ingestion Issues

### Database Connection Errors

While the stack is configured to wait for services, timeouts can occur on slower hardware during the initial startup sequence.

Recommended Steps:

1. Check the status of all containers to ensure `mariadb` shows as Healthy.
2. Restart the environment to clear the timeout.

Bash

```bash
docker compose -f docker-compose.dockerhub-dev.yml stop
docker compose -f docker-compose.dockerhub-dev.yml start
```

### Documents stuck in "pending" status

Asynchronous tasks like document processing are handled by background workers. If documents do not progress past "pending," the task pipeline may be interrupted.

Recommended Steps:

1. Ensure the `rag-redis` container is running and reachable on port 6379.
2. Verify that the `rag-celery-worker` is active and picking up tasks from the message broker.

{% code overflow="wrap" %}
```bash
docker compose -f docker-compose.dockerhub-dev.yml logs rag-celery-worker
```
{% endcode %}

### Document Extraction Issues

### Layout-Aware extraction (Docling Ray) failing

Advanced extraction tiers require the dedicated Docling Ray service to be functional and reachable.

Recommended Steps:

1. Confirm the `rag-docling-ray` container is running and accessible internally on port 8003.
2. Large or complex PDFs may exhaust system memory; ensure the host has at least 8 GB of RAM available.

### Diagnostic Procedures

### 1. Check Overall Service Health

Use Docker Compose to verify that all constituent containers are running correctly: \{% code title="Verify status" %\}

Bash

```
docker compose -f docker-compose.dockerhub-dev.yml ps
```

\{% endcode %\}

### 2. Verify Network Connectivity

Ensure the internal services can communicate on their assigned ports:

* Inbound: 8000 (API), 8002 (MCP), 3306 (DB), 8003 (Ray), 6379 (Redis).
* Outbound: 443 (External AI Providers & MariaDB Licensing).

### 3. Check Clock Synchronization

Ensure the host machine's time is synchronized (e.g., via NTP). Significant time drift can cause authentication failures with external AI providers and licensing servers.
