---
description: >-
  MCP Server authentication uses JWT tokens with bcrypt hashing, role-based
  access control, and four deployment modes including standalone, 1Password,
  Local Vault, and HCP Vault.
---

# Authentication

A cornerstone of the Enterprise edition is its ability to integrate with centralized secret managers, eliminating the need for static credentials stored in local or `.env` files. The server dynamically fetches database credentials and API keys at startup, ensuring a secure and compliant operational posture.

## Key Features

* **Multi-layered Authentication**: JWT-based authentication (HS256/RS256) with bcrypt password hashing
* **Adaptive Architecture**: Intelligent tool registration based on service availability
* **Role-Based Access Control (RBAC)**: Fine-grained permission management
* **Multiple Deployment Modes**: Standalone, 1Password, Local Vault, and HCP Vault
* **Database-Enforced User Validation**: Shared database ensures only registered users can access services

## Authentication Flow

### 1. User Registration

```mermaid

graph TD
    A[User] --> B[POST /register]
    B --> C[Hash Password]
    C --> D[Store in DB]
    D --> E[Return User Object]

```

### 2. User Login

```mermaid

graph TD
    A[User] --> B[POST /token]
    B --> C[Verify Credentials]
    C --> D[Assign Roles]
    D --> E[Generate JWT]
    E --> F[Return Token]
```

### 3. Authenticated Request

```mermaid
graph TD
    A[Client]
    B[MCP Server]
    C["RAG API (Optional)"]
    D[Database]

    A -- "1. Request with JWT" --> B
    B -- "2. Validate User" --> D
    D -- "User Record" --> B
    B -- "3. Forward Request" --> C
    C -- "Result" --> B
    B -- "4. Response" --> A

```

## Deployment Modes

### 1. Standalone

**Purpose:** Simple deployment with direct environment variables

**Configuration**: Direct environment variables

**Key Settings:**

```bash
# Direct values in config file
DB_HOST=localhost
DB_PASSWORD=your_password
SECRET_KEY=your_secret_key
JWT_SECRET_KEY=your_jwt_secret
GEMINI_API_KEY=your_api_key
```

**When to Use**: Development, testing, small deployments, No external secret management available

**Startup:**

```bash
# RAG API
rag-api.exe --config=config.env.secure.local

# MCP Server
$env:MCP_CONFIG="config.env.secure.local"
mcp-server.exe
```

### 2. 1Password

**Purpose:** Secure secret management using 1Password CLI

**Configuration**: `op://` secret references

**Key Settings:**

```bash
# 1Password references
DB_USER=op://Employee/RAG-Database/username
DB_PASSWORD=op://Employee/RAG-Database/password
SECRET_KEY=op://Employee/RAG-Security/secret-key
JWT_SECRET_KEY=op://Employee/RAG-Security/jwt-secret
GEMINI_API_KEY=op://Employee/RAG-API-Keys/gemini
```

**Prerequisites:**

1. Install 1Password CLI
2. Authenticate: `op signin`
3. Create vault and items with required secrets

**Startup:**

```bash
# RAG API
op run --env-file=config.env.1password.employee -- rag-api.exe

# MCP Server
op run --env-file=config.env.1password.employee -- mcp-server.exe
```

**When to Use**: Team environments, shared secrets, Production

### 3. Local Vault

**Purpose:** Development with local HashiCorp Vault

**Configuration**: Local Vault server

**Key Settings:**

```bash
# Vault Configuration
VAULT_ADDR=http://127.0.0.1:8200
VAULT_TOKEN=rag-root-token
VAULT_SKIP_VERIFY=true
VAULT_SECRET_PATH=rag-in-a-box
VAULT_MOUNT_POINT=secret
```

**Setup:**

```bash
# Start Vault in dev mode
vault server -dev -dev-root-token-id="rag-root-token"

# Store secrets
vault kv put secret/rag-in-a-box/database \
    DB_USER=root \
    DB_PASSWORD=Password123! \
    DB_NAME=kb_chunks

vault kv put secret/rag-in-a-box/security \
    SECRET_KEY=your_secret_key \
    JWT_SECRET_KEY=your_jwt_secret

vault kv put secret/rag-in-a-box/api-keys \
    GEMINI_API_KEY=your_api_key
```

**Startup:**

```bash
# RAG API
rag-api.exe --config=config.env.vault.local

# MCP Server
$env:MCP_CONFIG="config.env.vault.local"
mcp-server.exe
```

**When to Use**: Development, Production with proper vault setup

### 4. HCP Vault

**Purpose:** Production deployment with HashiCorp Cloud Platform Vault

**Configuration**: HCP Vault cluster

**Key Settings:**

```bash
# HCP Vault Configuration
VAULT_ADDR=https://your-vault-cluster.hashicorp.cloud:8200
VAULT_NAMESPACE=admin
VAULT_SKIP_VERIFY=false
VAULT_SECRET_PATH=rag-in-a-box
VAULT_MOUNT_POINT=secret

# AppRole Authentication
VAULT_ROLE_ID=your-vault-role-id
VAULT_SECRET_ID=your-vault-secret-id
```

**Setup:**

1. Create HCP Vault cluster
2. Configure AppRole authentication
3. Create policies for application access
4. Store secrets in Vault
5. Generate role\_id and secret\_id

**Startup:**

```bash
# RAG API
rag-api.exe --config=config.env.hcp.live

# MCP Server
$env:MCP_CONFIG="config.env.hcp.live"
mcp-server.exe
```

**When to Use**: Production, enterprise deployments

***

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
