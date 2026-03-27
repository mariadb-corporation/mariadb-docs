---
hidden: true
noIndex: true
---

# Ubuntu Deployment Guide

## MariaDB AI RAG - Ubuntu Native Deployment Guide

**Deploy MariaDB AI RAG .deb package directly on Ubuntu (without Docker)**

***

### Quick Start

```bash
# 1. Install MariaDB
sudo apt update && sudo apt install -y mariadb-server mariadb-client
sudo systemctl start mariadb && sudo systemctl enable mariadb

# 2. Secure MariaDB (set root password during setup)
sudo mysql_secure_installation

# 3. Create database
sudo mariadb -u root -p <<EOF
CREATE DATABASE kb_chunks CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;
EOF

# 4. Install MariaDB AI RAG
sudo apt install -y ./ai-nexus.deb

# 5. Configure (update GEMINI_API_KEY)
cp /opt/rag-in-a-box/config/config.env.template /path/to/config.env
nano /path/to/config.env

# 6. Start services in their own terminals
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server

# 7. Verify
curl http://localhost:8000/health
```

***

### Prerequisites

#### System Requirements

* **OS**: Ubuntu 22.04 LTS or 24.04 LTS (x86\_64)
* **CPU**: 4+ cores (8+ recommended)
* **RAM**: 8+ GB (16+ recommended)
* **Storage**: 20+ GB free
* **Access**: Root/sudo privileges

#### Required

* **Google Gemini API Key**: Get from https://makersuite.google.com/app/apikey

#### Verify System

```bash
# Check Ubuntu version
lsb_release -a

# Check disk space
df -h /

# Check ports are free
sudo netstat -tuln | grep -E ':(8000|8002|3306)'
# No output = ports available
```

***

### Step 1: Install MariaDB

```bash
# Update package lists
sudo apt update

# Install MariaDB
sudo apt install -y mariadb-server mariadb-client

# Start and enable MariaDB
sudo systemctl start mariadb
sudo systemctl enable mariadb

# Verify running
sudo systemctl status mariadb
```

***

### Step 2: Secure MariaDB

```bash
sudo mysql_secure_installation
```

**Follow prompts:**

* Enter current password for root: \[Press Enter]
* Switch to unix\_socket authentication? **n**
* Change the root password? **Y**
  * New password: **\[Choose a secure password]**
  * Re-enter: **\[Same password]**
* Remove anonymous users? **Y**
* Disallow root login remotely? **Y**
* Remove test database? **Y**
* Reload privilege tables? **Y**

***

### Step 3: Create Database

```bash
# Login to MariaDB
sudo mariadb -u root -p
# Enter password: [your_password]
```

**In MariaDB shell:**

```sql
-- Create database
CREATE DATABASE kb_chunks CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Verify
SHOW DATABASES;

-- Exit
EXIT;
```

***

### Step 4: Configure MariaDB

```bash
# Edit configuration
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

**Add under `[mysqld]` section:**

```ini
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
innodb_page_size = 16k
innodb_default_row_format = dynamic
max_connections = 100
innodb_buffer_pool_size = 2G
```

**Save and restart:**

```bash
# Save: Ctrl+X, Y, Enter
sudo systemctl restart mariadb
```

***

### Step 5: Install MariaDB AI RAG Package

```bash
# Navigate to directory with .deb file
cd ~/

# Install package
sudo apt install -y ./ai-nexus.deb

# If dependency issues:
sudo dpkg -i ai-nexus.deb
sudo apt-get install -f
```

**Verify installation:**

```bash
# Check installed files
dpkg -L ai-nexus | head -20

# Expected locations:
# /opt/rag-in-a-box/bin/rag-api
# /opt/rag-in-a-box/bin/mcp-server
# /opt/rag-in-a-box/config/config.env.template

# Check binaries exist
ls -lh /opt/rag-in-a-box/bin/
```

***

### Step 6: Configure MariaDB AI RAG

```bash
# Edit configuration file
cp /opt/rag-in-a-box/config/config.env.template /path/to/config.env
nano /path/to/config.env
```

**Update these essential settings:**

```bash
# ===== DATABASE CONFIGURATION =====
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_secure_database_password
DB_NAME=kb_chunks

# ===== API KEYS (REQUIRED - UPDATE THIS!) =====
GEMINI_API_KEY=your_actual_gemini_api_key_here

# ===== SECURITY KEYS (MUST BE IDENTICAL) =====
SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three
JWT_SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three
MCP_AUTH_SECRET_KEY=your_generated_secret_key_must_be_same_for_all_three

# ===== SERVER CONFIGURATION =====
APP_HOST=0.0.0.0
APP_PORT=8000
MCP_HOST=0.0.0.0
MCP_PORT=8002

# ===== EMBEDDING & LLM =====
EMBEDDING_PROVIDER=gemini
embedding_model=text-embedding-004
LLM_PROVIDER=gemini
LLM_MODEL=gemini-2.0-flash

# ===== TABLE NAMES =====
DOCUMENTS_TABLE=documents_DEMO_gemini
VDB_TABLE=vdb_tbl_DEMO_gemini

# ===== MCP CONFIGURATION =====
MCP_ENABLE_AUTH=true
MCP_ENABLE_VECTOR_TOOLS=true
MCP_ENABLE_DATABASE_TOOLS=true
MCP_ENABLE_RAG_TOOLS=true
MCP_READ_ONLY=false
MCP_LOG_LEVEL=INFO

# ===== PROCESSING =====
CHUNK_SIZE=512
CHUNK_OVERLAP=128
DOCUMENT_PROCESSING_BATCH_SIZE=5
EMBEDDING_BATCH_SIZE=32
```

**Save:** Ctrl+X, Y, Enter

***

### Step 7: Start Services in their own terminals

```bash
# Start RAG API
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env

# Start MCP Server
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server
```

### Step 8: Verify Deployment

Check listening ports:

```
sudo netstat -tuln | grep -E ':(8000|8002)'
```

Should show LISTEN on both ports

#### Test Health Endpoints

```bash
# Test RAG API
curl http://localhost:8000/health
# Expected: {"status":"healthy","database":"connected"}

# Test MCP Server
curl http://localhost:8002/health
# Expected: {"status":"healthy"}

# Test API info
curl http://localhost:8000/
```

#### View Logs

**Expected log messages:**

```
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

***

### Step 9: Test Functionality

#### Generate Authentication Token

```bash
# Generate token
curl -X POST "http://localhost:8000/token" \
  -H "Content-Type: application/json" \
  -d '{"username":"admin","password":"your_password"}'

# Save token for next commands
export TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

#### Test Document Upload

```bash
# Create test document
echo "This is a test document for MariaDB AI RAG RAG system. It contains sample text for testing." > test_document.txt

# Upload document
curl -X POST "http://localhost:8000/documents/ingest" \
  -H "Authorization: Bearer $TOKEN" \
  -F "file=@test_document.txt"

# Expected output:
# {"document_id":1,"filename":"test_document.txt","chunks_created":1,"status":"success"}
```

#### Test RAG Query

```bash
# Query the document
curl -X POST "http://localhost:8000/orchestrate/generation" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"query":"What is this document about?"}'

# Expected: AI-generated response with sources
```

#### Verify Database

```bash
# Login to MariaDB
mariadb -u root -p kb_chunks
# Enter password: [your_password]
```

**In MariaDB:**

```sql
-- Show tables
SHOW TABLES;

-- Check documents
SELECT id, filename, created_at FROM documents_DEMO_gemini;

-- Check embeddings
SELECT COUNT(*) FROM vdb_tbl_DEMO_gemini;

-- Exit
EXIT;
```

***

## Access Points

After successful deployment:

* **RAG API Swagger UI**: http://\<server-ip>:8000/docs
* **RAG API Health**: http://\<server-ip>:8000/health
* **MCP Server**: http://\<server-ip>:8002/mcp
* **MCP Health**: http://\<server-ip>:8002/health

**Get server IP:**

```bash
hostname -I
```

***

## Troubleshooting

### Services Won't Start

**Check logs in the terminal windows**

**Common causes:**

1. **MariaDB not running**

```bash
sudo systemctl status mariadb
sudo systemctl start mariadb
```

2. **Configuration errors**

```bash
nano /path/to/config.env
# Check for typos, missing values
```

3. **Port already in use**

```bash
sudo lsof -i :8000
sudo lsof -i :8002
# Stop conflicting service or kill process
```

4. **Permission issues**

```bash
sudo chmod +x /opt/rag-in-a-box/bin/rag-api
sudo chmod +x /opt/rag-in-a-box/bin/mcp-server
sudo chmod 640 /opt/rag-in-a-box/config/config.env.template
```

### Database Connection Fails

```bash
# Test MariaDB connection
mariadb -u root -p -e "SELECT 1;"

# Check MariaDB status
sudo systemctl status mariadb

# Restart MariaDB
sudo systemctl restart mariadb

# Check credentials in config
sudo grep DB_ /path/to/config.env

# View MariaDB logs
sudo tail -f /var/log/mysql/error.log
```

### Authentication Fails

```bash
# Verify all three secret keys are identical
sudo grep SECRET_KEY /path/to/config.env

# Should show same value for:
# SECRET_KEY=...
# JWT_SECRET_KEY=...
# MCP_AUTH_SECRET_KEY=...

# If different, fix and restart
nano /path/to/config.env
```

### API Key Invalid

```bash
# Test Gemini API key
API_KEY="YOUR_KEY"
curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=$API_KEY"

# If invalid, update config
nano /path/to/config.env
# Update: GEMINI_API_KEY=...

# Restart services
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server
```

### Port Already in Use

```bash
# Find process using port
sudo lsof -i :8000
sudo lsof -i :8002

# Kill process (if safe)
sudo kill <PID>
```

### Out of Memory

```bash
# Check memory
free -h
top

# Add swap if needed (4GB example)
sudo fallocate -l 4G /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Make permanent
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab
```

***

## Maintenance

### Daily Operations

```bash
# Check service status
sudo systemctl status mariadb

# Test RAG API
curl http://localhost:8000/health
# Expected: {"status":"healthy","database":"connected"}

# Test MCP Server
curl http://localhost:8002/health
# Expected: {"status":"healthy"}

# Test API info
curl http://localhost:8000/

# Monitor disk space
df -h
```

### Backup Database

```bash
# Backup
sudo mysqldump -u root -p kb_chunks > kb_chunks_backup_$(date +%Y%m%d).sql

# Compress backup
gzip kb_chunks_backup_$(date +%Y%m%d).sql

# Restore (if needed)
mariadb -u root -p kb_chunks < kb_chunks_backup_20241013.sql
```

### Update Configuration

```bash
# Edit config
nano /path/to/config.env

# Restart services to apply changes
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server
```

### Update MariaDB AI RAG

```bash
# Install new version
sudo apt install -y ./ai-nexus-new-version.deb

# Start services in their own terminals
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server

# Verify
curl http://localhost:8000/health
```

### Optimize Database

```bash
mariadb -u root -p <<EOF
USE kb_chunks;
OPTIMIZE TABLE documents_DEMO_gemini;
OPTIMIZE TABLE vdb_tbl_DEMO_gemini;
EXIT;
EOF
```

***

## Uninstall

```bash
# Remove package
sudo apt remove --purge rag-in-a-box

# Remove configuration (optional)
sudo rm -rf /opt/rag-in-a-box/

# Remove database (optional - ⚠️ deletes all data)
mariadb -u root -p -e "DROP DATABASE kb_chunks;"
```

***

## Security Best Practices

### Change Default Passwords

```bash
# Change MariaDB root password
sudo mariadb -u root -p
```

```sql
ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_secure_password';
FLUSH PRIVILEGES;
EXIT;
```

**Update config:**

```bash
nano /path/to/config.env
# DB_PASSWORD=your_new_secure_password
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server
```

### Generate New Secret Keys

```bash
# Generate secure key
python3 -c "import secrets; print(secrets.token_urlsafe(64))"

# Use same value for all three keys in config
nano /path/to/config.env
```

### Configure Firewall

```bash
# Install UFW
sudo apt install -y ufw

# Allow SSH (IMPORTANT!)
sudo ufw allow 22/tcp

# Allow RAG API
sudo ufw allow 8000/tcp

# Allow MCP Server
sudo ufw allow 8002/tcp

# Enable firewall
sudo ufw enable

# Check status
sudo ufw status
```

### Restrict Database Access

```bash
# Create dedicated database user
sudo mariadb -u root -p
```

```sql
CREATE USER 'rag_user'@'localhost' IDENTIFIED BY 'your_secure_password';
GRANT ALL PRIVILEGES ON kb_chunks.* TO 'rag_user'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

**Update config:**

```bash
nano /path/to/config.env
# DB_USER=rag_user
# DB_PASSWORD=your_secure_password
```

***

## Quick Reference

### Essential Commands

```bash
# Start services
/opt/rag-in-a-box/bin/rag-api --config /path/to/config.env
CONFIG_FILE=/path/to/config.env /opt/rag-in-a-box/bin/mcp-server

# Test health
curl http://localhost:8000/health

# Edit config
nano /path/to/config.env

# Database access
mariadb -u root -p kb_chunks
```

### File Locations

```
/opt/rag-in-a-box/bin/rag-api                   # RAG API binary
/opt/rag-in-a-box/bin/mcp-server                # MCP Server binary
/opt/rag-in-a-box/config/config.env.template    # Configuration file
/var/log/mysql/error.log                        # MariaDB logs
```

### Service Dependencies

```
MariaDB (Port 3306)
    ↓
RAG API (Port 8000)
    ↓
MCP Server (Port 8002)
```

**Start order:** MariaDB → RAG API → MCP Server\
**Stop order:** MCP Server → RAG API → MariaDB

***

## Architecture Overview

```
Ubuntu System (Native)
├── MariaDB Service (systemd)
│   └── Database: kb_chunks (Port 3306)
├── RAG API Service (systemd)
│   └── FastAPI Server (Port 8000)
└── MCP Server Service (systemd)
    └── FastAPI Server (Port 8002)
```

***

## Performance Tuning

### MariaDB Optimization

```bash
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf
```

```ini
[mysqld]
# Adjust based on available RAM
innodb_buffer_pool_size = 4G  # 50-70% of RAM
max_connections = 200
innodb_log_file_size = 512M
query_cache_size = 0
query_cache_type = 0
```

### System Resources

```bash
# Monitor resources
htop
# Or
top

# Check disk I/O
iostat -x 1

# Check network
iftop
```

***

## Deployment Complete! 🎉

Your MariaDB AI RAG is now running natively on Ubuntu.

**Next Steps:**

1. Access Swagger UI: http://\<server-ip>:8000/docs
2. Generate authentication token
3. Upload test documents
4. Start querying with RAG

**For support:**

* Check logs
* Verify config: `nano /path/to/config.env`
* Test health: `curl http://localhost:8000/health`

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
