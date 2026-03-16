# Deployment & Administration

MariaDB AI RAG 1.1 (Beta) is a containerized Retrieval-Augmented Generation (RAG) solution designed for high-precision, citation-backed outputs. The system is deployed as a multi-container Docker stack, allowing components like the API brain, background workers, and document specialists to scale independently.

Note: As of the 1.1 release, native binary-based deployments (such as `.deb` or `.rpm` packages) are no longer available.

## Prerequisites

Ensure your environment meets the following requirements before starting the deployment:

* Hardware: Minimum 4 CPU cores, 8 GB RAM, and 20 GB free disk space.
* Operating System: 64-bit Linux (recommended), Windows (with WSL2), or macOS.
* Software: Docker Engine and Docker Compose (v2.x+) must be installed.
* Mandatory Credentials:
  * MariaDB License Key: A valid key is required for the application to pass the startup check.
  * AI Provider API Keys: Credentials for chosen AI providers (e.g., Google Gemini or OpenAI).
* Database: A MariaDB 11.8+ instance is required for native vector search support.

### Step-by-Step Instructions

### Step 1: Prepare Your Directory

Create a dedicated deployment folder on your host machine and navigate into it:

```bash
mkdir mariadb-rag-deployment
cd mariadb-rag-deployment
```

### Step 2: Obtain Configuration Files

Download the following essential files from the public AI RAG GitHub repository and place them in your new folder:

1. `docker-compose.dockerhub-dev.yml`: The blueprint defining all services in the stack.
2. `config.env.template`: The template containing all necessary environment variables.

### Step 3: Create Local Storage Directories

To avoid permission conflicts, manually create the storage and logging folders:

```bash
mkdir uploaded_files
mkdir logs
```

### Step 4: Update the Configuration File

Rename `config.env.template` to `config.env.secure` and update the following critical variables:

* `MARIADB_LICENSE_KEY`: Insert your valid license token here.
* AI API Keys: Provide keys for your providers (e.g., `GEMINI_API_KEY=your_key`).
* Database Configuration: Configure `DB_HOST`, `DB_USER`, and `DB_PASSWORD`. For the internal Docker container, set `DB_HOST=mariadb`.
* Security Keys: Ensure `SECRET_KEY`, `JWT_SECRET_KEY`, and `MCP_AUTH_SECRET_KEY` are all set to the same secure, random string to enable unified authentication.

### Step 5: Launch the Application

Start the container stack using Docker Compose:

```bash
docker compose -f docker-compose.dockerhub-dev.yml --env-file config.env.secure up -d
```

### Step 6: Verify the Deployment

Verification may take a few minutes as services initialize. Check the status of the containers:

```bash
docker compose -f docker-compose.dockerhub-dev.yml ps
```

All core services (e.g., `rag-api`, `mcp-server`, `rag-redis`) should show a status of Up or Healthy. Review the RAG API logs to confirm the license check passed:

```bash
docker compose -f docker-compose.dockerhub-dev.yml logs -f rag-api
```
