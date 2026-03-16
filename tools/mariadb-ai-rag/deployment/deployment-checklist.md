---
hidden: true
noIndex: true
---

# Deployment Checklist

## Pre-Deployment Checklist

### System Requirements Verification

#### Hardware

* [ ] CPU: 4+ cores available
* [ ] RAM: 8+ GB available
* [ ] Storage: 20+ GB free disk space
* [ ] Network: Stable internet connection

#### Software

* [ ] Operating System: Linux (Ubuntu or RHEL), Windows 10/11 Pro/Enterprise
* [ ] Docker installed (version 20.10+)
* [ ] Docker Compose installed (version 2.x+)
* [ ] Docker service is running
* [ ] Shell access (bash/zsh on Linux, PowerShell on Windows)

#### Verification Commands

**Linux:**

```bash
# Check Docker
docker --version

# Check disk space
df -h /

# Check shell
echo $SHELL
```

**Windows (PowerShell):**

```bash
# Check Docker
docker --version

# Check disk space
Get-PSDrive C | Select-Object Used,Free
```

***

### Port Availability Check

* [ ] Port 8000 is free (RAG API)
* [ ] Port 8002 is free (MCP Server)
* [ ] Port 3306 is free (MariaDB)
* [ ] Port 8200 is free (Vault - if using Vault mode)

#### Verification Commands

**Linux:**

```bash
# Check if ports are in use
sudo lsof -i :8000
sudo lsof -i :8002
sudo lsof -i :3306
sudo lsof -i :8200

# No output = ports are free ✓
# Alternative using netstat:
netstat -an | grep :8000
```

**Windows (PowerShell):**

```bash
# Check if ports are in use
netstat -ano | findstr :8000
netstat -ano | findstr :8002
netstat -ano | findstr :3306
netstat -ano | findstr :8200

# No output = ports are free ✓
```

***

### API Keys Obtained

* [ ] Google Gemini API Key obtained
* [ ] API Key tested and valid
* [ ] API Key saved securely

#### Get API Key

1. Visit: https://makersuite.google.com/app/apikey
2. Sign in with Google account
3. Click "Create API Key"
4. Copy and save the key

#### Test API Key

**Linux:**

```bash
# Test API key
API_KEY="YOUR_API_KEY_HERE"
curl "https://generativelanguage.googleapis.com/v1beta/models?key=$API_KEY"
# Should return list of models
```

**Windows (PowerShell):**

```bash
$apiKey = "YOUR_API_KEY_HERE"
$uri = "https://generativelanguage.googleapis.com/v1beta/models?key=$apiKey"
Invoke-RestMethod -Uri $uri
# Should return list of models
```

***

### Project Files Verification

* [ ] Navigate to project directory
* [ ] Verify all required files exist
* [ ] Verify file permissions

#### Required Files for Ubuntu Docker Deployment

```
├── rag-in-a-box_1.0_amd64.deb
├── Dockerfile
├── docker-compose.yml
├── start-services.sh
├── config.env.secure.local
├── config.env.vault.local
├── config.env.template
└── Localvault/
    ├── docker-compose.vault.yml
    └── setup_vault_local.ps1
```

#### Verification Commands

**Linux:**

```bash
# Navigate to download location
cd /path/to/download/location

# List files
ls -lh
```

**Windows (PowerShell):**

```powershell
# Navigate to download location
cd "C:\path\to\download\location"

# List files
Get-ChildItem | Select-Object Name, Length
```

***

### Configuration File Setup

* [ ] Open `config.env.secure.local`
* [ ] Update `GEMINI_API_KEY` with actual key
* [ ] Verify database credentials
* [ ] Verify security keys are identical
* [ ] Save configuration file

#### Critical Settings to Verify

```bash
# API Key (MUST UPDATE)
GEMINI_API_KEY=YOUR_ACTUAL_API_KEY_HERE

# Database (default values OK)
DB_HOST=mysql-db
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_secure_database_password
DB_NAME=kb_chunks

# Security Keys (MUST BE IDENTICAL)
SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three
JWT_SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three
MCP_AUTH_SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three

# Server Configuration (default values OK)
APP_HOST=0.0.0.0
APP_PORT=8000
MCP_HOST=0.0.0.0
MCP_PORT=8002
```

***

## Deployment Checklist - Standalone Mode

### Step 1: Build Docker Image

* [ ] Navigate to project directory
* [ ] Run build command
* [ ] Wait for build completion (2-5 minutes)
* [ ] Verify image created

#### Commands

```bash
cd "c:\Users\YourUsername\OneDrive\WIP\MariaDB AI RAG Binaries\Ubuntu"
cd "c:\Users\YourUsername\OneDrive\WIP\AI Nexus Binaries\Ubuntu"
cd "c:\DOWNLOAD-LOCATION"
docker build -t ai-nexus-image .
```

#### Verification

```bash
docker images | Select-String "ai-nexus-image"
# Should show: ai-nexus-image    latest    <image-id>    <time>    ~1.2GB
```

***

### Step 2: Start Services

* [ ] Run docker-compose command
* [ ] Verify containers starting
* [ ] Wait for startup completion

#### Commands

```bash
docker compose up -d
```

#### Expected Output

```
[+] Running 3/3
 ✔ Network ai-nexus-network    Created
 ✔ Container mysql-db          Started
 ✔ Container ai-nexus          Started
```

***

### Step 3: Monitor Startup

* [ ] Watch container logs
* [ ] Wait for "RAG API is ready" message
* [ ] Wait for "MCP Server ready" message
* [ ] Verify no error messages

#### Commands

```bash
docker logs ai-nexus -f
# Press Ctrl+C to exit (containers keep running)
```

#### Expected Log Messages

```
Starting RAG server...
RAG server started with PID: 15
Waiting for RAG API to be ready...
✓ RAG API is ready! (took ~30 seconds)
Starting MCP server...
Adaptive MCP Server ready on 0.0.0.0:8002
INFO:     Uvicorn running on http://0.0.0.0:8000
```

***

### Step 4: Verify Container Status

* [ ] Check container status
* [ ] Verify both containers running
* [ ] Verify mysql-db is healthy
* [ ] Verify port mappings

#### Commands

```bash
docker-compose ps
```

#### Expected Output

```
NAME       STATUS                    PORTS
ai-nexus   Up X minutes              0.0.0.0:8000->8000/tcp, 0.0.0.0:8002->8002/tcp
mysql-db   Up X minutes (healthy)    0.0.0.0:3306->3306/tcp
```

***

### Step 5: Test API Accessibility

* [ ] Test RAG API health endpoint
* [ ] Open Swagger UI in browser
* [ ] Test MCP Server health endpoint
* [ ] Verify no connection errors

#### Commands

**Linux:**

```bash
# Test RAG API
curl http://localhost:8000/health

# Open Swagger UI in browser

xdg-open http://localhost:8000/docs  # Linux

# Test MCP Server
curl http://localhost:8002/health
```

**Windows (PowerShell):**

```powershell
# Test RAG API
Invoke-RestMethod -Uri "http://localhost:8000/health"

# Open Swagger UI
Start-Process "http://localhost:8000/docs"

# Test MCP Server
Invoke-RestMethod -Uri "http://localhost:8002/health"
```

***

## Deployment Checklist - Vault Mode

### Step 1: Build Docker Image

* [ ] Navigate to project directory
* [ ] Run build command
* [ ] Verify image created

#### Commands

```bash
cd "c:\Users\YourUsername\OneDrive\WIP\MariaDB AI RAG Binaries\Ubuntu"
cd "c:\Users\YourUsername\OneDrive\WIP\AI Nexus Binaries\Ubuntu"
cd "c:\DOWNLOAD-LOCATION"
docker build -t ai-nexus-image .
```

***

### Step 2: Run Vault Setup Script

* [ ] Run automated Vault setup
* [ ] Verify Vault container started
* [ ] Verify secrets stored
* [ ] Note Vault credentials

#### Commands

```bash
.\Localvault\setup_vault_local.ps1
```

#### Expected Output

```
[SUCCESS] Vault Setup Complete!

Vault Details:
  URL:    http://127.0.0.1:8200
  Token:  rag-root-token
  Path:   secret/rag-in-a-box
```

***

### Step 3: Verify Vault Status

* [ ] Check Vault container running
* [ ] View stored secrets
* [ ] Verify all secrets present

#### Commands

```bash
# Check Vault container
docker ps --filter "name=rag-vault"

# View secrets
docker exec -e VAULT_TOKEN=rag-root-token rag-vault vault kv get secret/rag-in-a-box
```

***

### Step 4: Update Gemini API Key in Vault

* [ ] Run patch command with actual API key
* [ ] Verify update successful
* [ ] Verify new version created

#### Commands

```bash
docker exec -e VAULT_TOKEN=rag-root-token rag-vault vault kv patch secret/rag-in-a-box GEMINI_API_KEY="YOUR_ACTUAL_API_KEY"
```

***

### Step 5: Start MariaDB AI RAG with Vault Config

### Step 5: Start AI Nexus with Vault Config

### Step 5: Start MariaDB AI RAG with Vault Config

* [ ] Run docker-compose with vault config
* [ ] Verify containers starting
* [ ] Monitor logs for Vault connection

#### Commands

```bash
docker-compose --env-file config.env.vault.local up -d
```

***

### Step 6: Verify Deployment

* [ ] Check container status
* [ ] Verify logs show successful startup
* [ ] Test API endpoints
* [ ] Verify Vault integration working

#### Commands

**Linux:**

```bash
docker compose ps
docker logs ai-nexus -f
curl http://localhost:8000/health
```

**Windows (PowerShell):**

```powershell
docker compose ps
docker logs ai-nexus -f
Invoke-RestMethod -Uri "http://localhost:8000/health"
```

***

## Post-Deployment Checklist

### Authentication Setup

* [ ] Open Swagger UI
* [ ] Navigate to /token endpoint
* [ ] Generate authentication token
* [ ] Copy and save token
* [ ] Test token with authorized endpoint

#### Steps

1. Open: http://localhost:8000/docs
2. Click on `POST /token`
3. Click "Try it out"
4.  Enter credentials:

    ```json
    {
      "username": "admin",
      "password": "your_password"
    }
    ```
5. Click "Execute"
6. Copy `access_token` from response

***

### Authorize in Swagger UI

* [ ] Click "Authorize" button (🔒 icon)
* [ ] Enter: `Bearer YOUR_TOKEN_HERE`
* [ ] Click "Authorize"
* [ ] Verify authorization successful

***

### Test Document Ingestion

* [ ] Navigate to POST /ingest endpoint
* [ ] Click "Try it out"
* [ ] Upload test document
* [ ] Click "Execute"
* [ ] Verify successful response
* [ ] Note document ID

#### Test Files

Use files from `test_documents/` directory or upload your own:

* PDF files
* TXT files
* DOCX files
* MD files

***

### Test RAG Query

* [ ] Navigate to POST /generate endpoint
* [ ] Enter question about uploaded document
* [ ] Click "Execute"
* [ ] Verify AI-generated response
* [ ] Verify sources included

#### Example Query

```json
{
  "query": "What is the main topic of the document?"
}
```

***

### Test MCP Server (Optional)

* [ ] Configure MCP client (Windsurf/Claude)
* [ ] Add server configuration
* [ ] Test connection
* [ ] Verify tools available

#### MCP Configuration

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

***

## Verification Checklist

### System Health Checks

* [ ] RAG API health endpoint returns "healthy"
* [ ] MCP Server health endpoint returns "healthy"
* [ ] Database connection successful
* [ ] No error messages in logs
* [ ] All containers running

#### Commands

**Linux:**

```bash
# Check all services
docker compose ps

# Check RAG API health
curl http://localhost:8000/health

# Check MCP Server health
curl http://localhost:8002/health

# Check logs
docker logs ai-nexus --tail 50
docker logs mysql-db --tail 50
```

**Windows (PowerShell):**

```powershell
# Check all services
docker compose ps

# Check RAG API health
Invoke-RestMethod -Uri "http://localhost:8000/health"

# Check MCP Server health
Invoke-RestMethod -Uri "http://localhost:8002/health"

# Check logs
docker logs ai-nexus --tail 50
docker logs mysql-db --tail 50
```

***

### Functional Tests

* [ ] Document upload works
* [ ] Document processing completes
* [ ] Embeddings generated
* [ ] Semantic search works
* [ ] RAG queries return answers
* [ ] Authentication works
* [ ] MCP tools accessible (if using MCP)

***

### Performance Checks

* [ ] Document ingestion completes in reasonable time
* [ ] Query responses within 2-4 seconds
* [ ] No memory leaks (check `docker stats`)
* [ ] CPU usage acceptable
* [ ] Disk space sufficient

#### Commands

```bash
# Monitor resource usage
docker stats ai-nexus mysql-db

# Check disk space
docker system df
```

***

## Troubleshooting Checklist

### If Services Won't Start

* [ ] Check Docker Desktop is running
* [ ] Check logs: `docker logs ai-nexus --tail 100`
* [ ] Check logs: `docker logs mysql-db --tail 50`
* [ ] Verify ports are free
* [ ] Rebuild image: `docker build -t ai-nexus-image .`
* [ ] Clean restart: `docker-compose down -v && docker-compose up -d`

***

### If Database Connection Fails

* [ ] Check mysql-db container status
* [ ] Wait for "(healthy)" status
* [ ] Verify DB\_HOST=mysql-db in config
* [ ] Check database logs
* [ ] Verify network connectivity

#### Commands

```bash
docker logs mysql-db --tail 20
docker-compose ps
docker exec ai-nexus ping mysql-db
```

***

### If Authentication Fails

* [ ] Verify all three secret keys are identical
* [ ] Generate new token from /token endpoint
* [ ] Check token format: `Bearer <token>`
* [ ] Verify token not expired (30 min default)
* [ ] Restart containers if keys changed

#### Commands

```bash
# Check secret keys
docker exec ai-nexus env | Select-String "SECRET"

# Restart if needed
docker-compose restart
```

***

### If API Key Invalid

* [ ] Test API key with Google API
* [ ] Get new key from https://makersuite.google.com/app/apikey
* [ ] Update in config.env.secure.local OR Vault
* [ ] Restart: `docker restart ai-nexus`

#### Test API Key

```bash
$apiKey = "YOUR_API_KEY"
$uri = "https://generativelanguage.googleapis.com/v1beta/models?key=$apiKey"
Invoke-RestMethod -Uri $uri
```

***

### If Ports Already in Use

* [ ] Find process using port
* [ ] Stop conflicting process
* [ ] OR change ports in docker-compose.yml
* [ ] Restart services

#### Commands

```bash
# Find process on port 8000
netstat -ano | findstr :8000

# Stop process (replace <PID>)
Stop-Process -Id <PID> -Force
```

***

## Maintenance Checklist

### Daily Operations

* [ ] Check container status: `docker-compose ps`
* [ ] Check logs for errors: `docker logs ai-nexus --tail 50`
* [ ] Monitor disk space: `docker system df`
* [ ] Backup database if needed

***

### Weekly Operations

* [ ] Review logs for issues
* [ ] Check resource usage: `docker stats`
* [ ] Update API keys if rotated
* [ ] Clean unused Docker resources: `docker system prune`

***

### Stopping Services

* [ ] Stop MariaDB AI RAG: `docker-compose down`
* [ ] Stop AI Nexus: `docker-compose down`
* [ ] Stop MariaDB AI RAG: `docker-compose down`
* [ ] Stop Vault (if used): `docker-compose -f "Localvault/docker-compose.vault.yml" down`
* [ ] Verify all containers stopped: `docker ps`

***

### Starting Services

* [ ] Standalone: `docker-compose up -d`
* [ ] Vault: `docker-compose --env-file config.env.vault.local up -d`
* [ ] Verify startup: `docker logs ai-nexus -f`

***

## Quick Reference Commands

### Essential Commands

```bash
# Navigate to project
cd "c:\Users\YourUsername\OneDrive\WIP\MariaDB AI RAG Binaries\Ubuntu"
cd "c:\Users\YourUsername\OneDrive\WIP\AI Nexus Binaries\Ubuntu"
cd "c:\DOWNLOAD-LOCATION"

# Build image
docker build -t ai-nexus-image .

# Start (Standalone)
docker-compose up -d

# Start (Vault)
docker-compose --env-file config.env.vault.local up -d

# Stop
docker-compose down

# View logs
docker logs ai-nexus -f

# Check status
docker-compose ps

# Restart
docker-compose restart

# Clean restart
docker-compose down -v && docker-compose up -d
```

***

## Deployment Sign-Off

### Final Verification

* [ ] All containers running
* [ ] All health checks passing
* [ ] Authentication working
* [ ] Document ingestion tested
* [ ] RAG queries tested
* [ ] No errors in logs
* [ ] Documentation reviewed
* [ ] Team notified (if applicable)

### Deployment Details

**Deployment Date**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Deployment Mode**:

* [ ] Standalone
* [ ] Vault
* [ ] 1Password
* [ ] HCP Vault

**Deployed By**: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

**Access URLs**:

* RAG API: http://localhost:8000/docs
* MCP Server: http://localhost:8002/mcp

**Notes**:

***

***

***

***

**✅ Deployment Complete!**

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
