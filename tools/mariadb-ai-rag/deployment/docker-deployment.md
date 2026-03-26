---
hidden: true
noIndex: true
---

# Docker Deployment Guide

## 📋 Quick Navigation

* [System Overview](docker-deployment.md#system-overview)
* [Prerequisites](docker-deployment.md#prerequisites)
* [Deployment - Standalone Mode](docker-deployment.md#deployment---standalone-mode)
* [Deployment - Vault Mode](docker-deployment.md#deployment---vault-mode)
* [Post-Deployment](docker-deployment.md#post-deployment)
* [Usage Guide](docker-deployment.md#usage-guide)
* [Troubleshooting](docker-deployment.md#troubleshooting)

***

## System Overview

### What is MariaDB AI RAG?

**MariaDB AI RAG (RAG-in-a-Box)** is a containerized RAG system providing:

* Document ingestion & processing (PDF, TXT, DOCX, MD, etc.)
* Vector embeddings using Google Gemini
* Semantic search & AI-powered queries
* RESTful RAG API (Port 8000)
* MCP Server for AI agents (Port 8002)
* MariaDB 11 with vector support (Port 3306)

### Architecture

```
Windows Host
  └─ Docker Desktop
      ├─ ai-nexus Container (Ubuntu 24.04)
      │   ├─ RAG API (Port 8000) - FastAPI
      │   └─ MCP Server (Port 8002) - FastAPI
      └─ mysql-db Container (MariaDB 11)
          └─ Vector Database (Port 3306)
```

### Technology Stack

* **Container**: Docker Desktop + Docker Compose
* **OS**: Ubuntu 24.04 LTS
* **Database**: MariaDB 11 with vector support
* **Embedding**: Google Gemini text-embedding-004 (768-dim)
* **LLM**: Google Gemini gemini-2.5-flash
* **Framework**: FastAPI + Uvicorn

***

## Prerequisites

### Hardware Requirements

| Component | Minimum    | Recommended |
| --------- | ---------- | ----------- |
| CPU       | 4 cores    | 8+ cores    |
| RAM       | 8 GB       | 16+ GB      |
| Storage   | 20 GB free | 50+ GB free |

### Software Requirements

1. **Windows 10/11 Pro/Enterprise** (64-bit)
2. **Docker Desktop** 4.x+ with WSL 2 backend
3. **PowerShell** 5.1+ (built-in)

### API Keys

1. **Google Gemini API Key** (Required)
   * Get from: https://makersuite.google.com/app/apikey
   * Free tier available

### Port Requirements

* 8000 (RAG API)
* 8002 (MCP Server)
* 3306 (MariaDB)
* 8200 (Vault - if using Vault mode)

***

## Pre-Deployment Checklist

### 1. Verify Docker Installation

```powershell
docker --version
docker-compose --version

# Test Docker
docker run hello-world
```

### 2. Check Available Ports

```powershell
# Verify ports are free
netstat -ano | findstr :8000
netstat -ano | findstr :8002
netstat -ano | findstr :3306

# No output = ports are free ✓
```

### 3. Navigate to Project Directory

```powershell
# Navigate to your MariaDB AI RAG deployment directory
cd "<path-to-your-mariadb-ai-rag-directory>"

# Verify required files exist
Get-ChildItem | Select-Object Name

# Required files:
# ✓ ai-nexus.deb
# ✓ Dockerfile
# ✓ docker-compose.yml
# ✓ start-services.sh
# ✓ config.env.secure.local
```

### 4. Configure API Key

```powershell
# Edit configuration file
notepad config.env.secure.local

# Update this line with your actual API key:
# GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE

# Save and close
```

***

## Deployment - Standalone Mode

**Standalone Mode** = Simplest setup with secrets in config file

### Step 1: Build Docker Image

```powershell
# Ensure you're in the MariaDB AI RAG directory
docker build -t ai-nexus-image .
```

**Time**: 2-5 minutes (first time)

### Step 2: Start Services

```powershell
docker-compose up -d
```

**Expected Output**:

```
[+] Running 3/3
 ✔ Network ai-nexus-network    Created
 ✔ Container mysql-db          Started
 ✔ Container ai-nexus          Started
```

### Step 3: Monitor Startup

```powershell
docker logs ai-nexus -f
```

**Wait for**:

```
✓ RAG API is ready! (took ~30 seconds)
Starting MCP server...
Adaptive MCP Server ready on 0.0.0.0:8002
```

Press `Ctrl+C` to exit logs (containers keep running)

### Step 4: Verify Services

```powershell
docker-compose ps
```

**Expected**:

```
NAME       STATUS                    PORTS
ai-nexus   Up X minutes              0.0.0.0:8000->8000/tcp, 0.0.0.0:8002->8002/tcp
mysql-db   Up X minutes (healthy)    0.0.0.0:3306->3306/tcp
```

### Step 5: Test Accessibility

```powershell
# Test RAG API
Invoke-RestMethod -Uri "http://localhost:8000/health"

# Open Swagger UI
Start-Process "http://localhost:8000/docs"
```

### ✅ Deployment Complete!

**Access Points**:

* RAG API: http://localhost:8000/docs
* MCP Server: http://localhost:8002/mcp

***

## Deployment - Vault Mode

**Vault Mode** = Production-like secret management with HashiCorp Vault

### Step 1: Build Docker Image

```powershell
# Ensure you're in the MariaDB AI RAG directory
docker build -t ai-nexus-image .
```

### Step 2: Run Automated Vault Setup

```powershell
.\Localvault\setup_vault_local.ps1
```

**Expected**:

```
[SUCCESS] Vault Setup Complete!

Vault Details:
  URL:    http://127.0.0.1:8200
  Token:  rag-root-token
  Path:   secret/rag-in-a-box
```

### Step 3: Update Gemini API Key in Vault

```powershell
docker exec -e VAULT_TOKEN=rag-root-token rag-vault vault kv patch secret/rag-in-a-box GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"
```

### Step 4: Start MariaDB AI RAG with Vault Config

```powershell
docker-compose --env-file config.env.vault.local up -d
```

### Step 5: Monitor & Verify

```powershell
# Watch logs
docker logs ai-nexus -f

# Check status
docker-compose ps
```

### ✅ Deployment Complete!

**Vault Management**:

```powershell
# View secrets
docker exec -e VAULT_TOKEN=rag-root-token rag-vault vault kv get secret/rag-in-a-box

# Update secret
docker exec -e VAULT_TOKEN=rag-root-token rag-vault vault kv patch secret/rag-in-a-box KEY="value"

# Restart to apply changes
docker restart ai-nexus
```

***

## Post-Deployment

### 1. Generate Authentication Token

```powershell
# Open Swagger UI
Start-Process "http://localhost:8000/docs"

# In browser:
# 1. Navigate to POST /token endpoint
# 2. Click "Try it out"
# 3. Enter credentials:
#    {
#      "username": "admin",
#      "password": "your_password"
#    }
# 4. Click "Execute"
# 5. Copy the "access_token" from response
```

### 2. Authorize in Swagger UI

```
1. Click "Authorize" button (🔒 icon)
2. Enter: Bearer YOUR_TOKEN_HERE
3. Click "Authorize"
```

### 3. Test Document Ingestion

```
1. Navigate to POST /ingest endpoint
2. Click "Try it out"
3. Upload a test document (PDF/TXT)
4. Click "Execute"
5. Verify: Response shows document processed
```

### 4. Test RAG Query

```
1. Navigate to POST /generate endpoint
2. Enter a question about your document
3. Click "Execute"
4. Verify: AI-generated response with sources
```

***

## Usage Guide

### Document Ingestion

#### Via Swagger UI

1. Open http://localhost:8000/docs
2. Authorize with Bearer token
3. Use `POST /documents/ingest` endpoint
4. Upload file(s)
5. Wait for processing

#### Via PowerShell

```powershell
$token = "YOUR_TOKEN_HERE"
$headers = @{
    "Authorization" = "Bearer $token"
}

$file = "C:\path\to\document.pdf"
$form = @{
    file = Get-Item -Path $file
}

Invoke-RestMethod -Uri "http://localhost:8000/documents/ingest" `
    -Method POST `
    -Headers $headers `
    -Form $form
```

### RAG Query

#### Via Swagger UI

1. Open http://localhost:8000/docs
2. Use `POST /orchestrate/generation` endpoint
3. Enter your question
4. Get AI-generated answer

#### Via PowerShell

```powershell
$token = "YOUR_TOKEN_HERE"
$headers = @{
    "Authorization" = "Bearer $token"
    "Content-Type" = "application/json"
}

$body = @{
    query = "What is the main topic of the document?"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:8000/orchestrate/generation" `
    -Method POST `
    -Headers $headers `
    -Body $body
```

### MCP Server Integration

#### For Windsurf/Claude Desktop

Add to MCP configuration:

```json
{
  "mcpServers": {
    "ai-nexus": {
      "url": "http://localhost:8002/mcp",
      "headers": {
        "Authorization": "Bearer YOUR_TOKEN_HERE"
      }
    }
  }
}
```

#### Available MCP Tools

* **Database Tools**: `execute_sql`, `list_tables`, `get_table_schema`
* **Vector Tools**: `create_vector_store`, `search_vector_store`
* **RAG Tools**: `ingest_documents`, `generate_response`
* **Health Tools**: `health_check`, `get_server_status`

***

## Troubleshooting

### Services Won't Start

```powershell
# Check logs
docker logs ai-nexus --tail 100
docker logs mysql-db --tail 50

# Rebuild and restart
docker build -t ai-nexus-image .
docker-compose down
docker-compose up -d
```

### Database Connection Errors

```powershell
# Check MariaDB status
docker logs mysql-db --tail 20

# Wait for healthy status
docker-compose ps
# Look for "(healthy)" next to mysql-db

# Verify DB_HOST in config
# Should be: DB_HOST=mysql-db
```

### Port Already in Use

```powershell
# Find process using port
netstat -ano | findstr :8000

# Stop process (replace <PID>)
Stop-Process -Id <PID> -Force

# Or change port in docker-compose.yml
```

### Authentication Fails

```powershell
# Verify secret keys are identical
docker exec ai-nexus env | Select-String "SECRET"

# All three must match:
# SECRET_KEY
# JWT_SECRET_KEY
# MCP_AUTH_SECRET_KEY

# If different, edit config and restart
docker-compose down
docker-compose up -d
```

### API Key Invalid

```powershell
# Test Gemini API key
$apiKey = "YOUR_API_KEY"
$uri = "https://generativelanguage.googleapis.com/v1beta/models?key=$apiKey"
Invoke-RestMethod -Uri $uri

# If error: Get new key from https://makersuite.google.com/app/apikey
# Update in config.env.secure.local or Vault
# Restart: docker restart ai-nexus
```

### Health Check Timeout

```powershell
# Increase timeout in start-services.sh
# Edit: MAX_WAIT=300  # 5 minutes

# Rebuild
docker build -t ai-nexus-image .
docker-compose down
docker-compose up -d
```

***

## Management Commands

### View Status

```powershell
docker-compose ps
```

### View Logs

```powershell
# All services
docker-compose logs -f

# Specific service
docker logs ai-nexus -f
docker logs mysql-db -f

# Last N lines
docker logs ai-nexus --tail 100
```

### Stop Services

```powershell
# Stop MariaDB AI RAG
docker-compose down

# Stop Vault (if using Vault mode)
docker-compose -f "Localvault/docker-compose.vault.yml" down
```

### Start Services

```powershell
# Standalone mode
docker-compose up -d

# Vault mode
docker-compose --env-file config.env.vault.local up -d
```

### Restart Services

```powershell
# Restart all
docker-compose restart

# Restart specific service
docker restart ai-nexus
```

### Clean Everything (⚠️ Deletes Data)

```powershell
docker-compose down -v
```

### Access Container Shell

```powershell
docker exec -it ai-nexus /bin/bash
```

### View Resource Usage

```powershell
docker stats ai-nexus mysql-db
```

***

## Quick Reference

### Standalone Mode

```powershell
# Build
docker build -t ai-nexus-image .

# Start
docker-compose up -d

# Stop
docker-compose down
```

### Vault Mode

```powershell
# Setup Vault (one-time)
.\Localvault\setup_vault_local.ps1

# Start
docker-compose --env-file config.env.vault.local up -d

# Stop
docker-compose down
docker-compose -f "Localvault/docker-compose.vault.yml" down
```

### Switching Modes

```powershell
# Stop current mode
docker-compose down

# Start different mode
docker-compose up -d  # Standalone
docker-compose --env-file config.env.vault.local up -d  # Vault
```

### Access Points

* **RAG API**: http://localhost:8000/docs
* **MCP Server**: http://localhost:8002/mcp
* **Database**: localhost:3306

***

## Support

### Check Logs

```powershell
docker logs ai-nexus --tail 100
```

### Verify Configuration

```powershell
docker exec ai-nexus env | Select-String "GEMINI"
docker exec ai-nexus env | Select-String "DB_"
```

### Test Connectivity

```powershell
# RAG API
Invoke-RestMethod -Uri "http://localhost:8000/health"

# MCP Server
Invoke-RestMethod -Uri "http://localhost:8002/health"

# Database (from container)
docker exec ai-nexus curl -s http://mysql-db:3306
```

***

**🎉 Deployment Complete! Your MariaDB AI RAG is ready to use.**

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
