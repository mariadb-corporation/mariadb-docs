# Deployment

MariaDB AI RAG is an all-in-one, enterprise-ready solution that handles the entire Retrieval-Augmented Generation (RAG) pipeline, including document parsing with layout extraction, chunking, embedding generation, and easy-to-use retrieval APIs backed by hybrid search (vector + full-text search), with optional reranking before sending the relevant context to a foundation model for answer generation.

MariaDB AI RAG deployed as a containerized stack using Docker. For a quick evaluation, you can also leverage a MariaDB vector store deployed in a container alongside the AI RAG stack to get an end-to-end setup faster.

{% hint style="info" %}
As of AI RAG 1.1 release, native binary-based deployments (such as `.deb` or `.rpm` packages) are no longer available.
{% endhint %}

## Prerequisites

Ensure your environment meets the following requirements before starting the deployment:

* Hardware: Minimum 4 CPU cores, 8 GB RAM, and 20 GB free disk space.
* Operating System: 64-bit Linux
* Software: Docker Engine and Docker Compose must be installed.
* Mandatory Credentials:
  * [MariaDB License Key](overview.md#obtain-and-configure-the-mariadb-license-key): A valid key is required for the application to pass the startup check.
  * Model Provider API Keys: Credentials for chosen model providers (e.g., Google Gemini or OpenAI).
* Database: A [MariaDB 11.8+](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) instance is required for native vector search support.

## Setup & Launch Instructions

{% stepper %}
{% step %}
### Prepare Your Directory

Create a dedicated deployment folder on your host machine and navigate into it:

```bash
mkdir mariadb-rag-deployment
cd mariadb-rag-deployment
```
{% endstep %}

{% step %}
### Obtain Configuration Files

Download the following essential files from the public AI RAG GitHub repository and place them in your new folder:

1. [`docker-compose.yml`](https://raw.githubusercontent.com/mariadb-corporation/mariadb-docs/refs/heads/main/tools/docker-compose.yml): The blueprint defining all services in the stack.
2. [`config.env.template`](https://raw.githubusercontent.com/mariadb-corporation/mariadb-docs/refs/heads/main/tools/mariadb-ai-rag/config.env.template): The template containing all necessary environment variables.
{% endstep %}

{% step %}
### Create Local Storage Directory

Manually create these folders to prevent Docker from assigning 'root' permissions, which can cause access errors later:

```bash
mkdir uploaded_files
mkdir logs
```
{% endstep %}

{% step %}
### Obtain the MariaDB License Key

The application performs a mandatory validation check at startup and will fail to start if this key is missing, invalid, or expired. Each license is valid for 30 days from the day of generation.

To get your license, follow these steps:

1. Navigate to the [MariaDB License Portal](https://customers.mariadb.com/license/).
2.  Login with your MariaDB ID.<br>

    <figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
3.  Click **Get License** under the RAG Trial card.<br>

    <figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>
4.  Click **Generate License**. You may then _View_, _Copy_, or _Download_ the license information.<br>

    <figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>
5. Paste this key into your `config.env.secure` file as `MARIADB_LICENSE_KEY`.

{% hint style="info" %}
MariaDB trial license keys are valid for 30 days from the date of issue.
{% endhint %}
{% endstep %}

{% step %}
### **Configure Database and Security Keys**

{% hint style="info" %}
For a full breakdown of every variable in `config.env.secure`, see the [AI-RAG Configuration Guide](../reference/configuration-guide-config.env.md).
{% endhint %}

Open `config.env.secure` in a text editor to set your environment variables.

#### Security & Unified Authentication

To enable unified authentication across the API and MCP server, set these three variables to the same secure string

* `SECRET_KEY`
* `JWT_SECRET_KEY`
* `MCP_AUTH_SECRET_KEY`

{% hint style="success" %}
**Secure String Generation**

You may generate a secure 32-character string to assign to the three variables using  `openssl rand -hex 32`
{% endhint %}

{% hint style="danger" %}
Using a unique, randomly generated key prevents "replay attacks" and ensures that only your authorized MCP Gateway can trigger heavy-lifting tasks in the RAG API.
{% endhint %}

#### Model Provider Configuration

Specify the models and API keys for your chosen providers.

**LLM Settings**

* `LLM_PROVIDER`: Choose your provider (e.g., `gemini`, `openai`, or `ollama`).
* `LLM_MODEL`: The specific model name (e.g., `gemini-2.5-flash`).
* `GEMINI_API_KEY` or `OPENAI_API_KEY`: Your provider-specific API key.

**Embedding Settings**

* `EMBEDDING_PROVIDER`: Provider for vectorizing text (e.g., `openai`, `gemini`).
* `embedding_model`: Specific embedding model (e.g., `text-embedding-004`).

**Model Provider Setup Examples**

Choose your preferred provider by configuring the following variables:

{% tabs %}
{% tab title="Google Gemini Setup" %}
```ini
LLM_PROVIDER=gemini
LLM_MODEL=gemini-2.5-flash
GEMINI_API_KEY=your_gemini_key_here
EMBEDDING_PROVIDER=gemini
embedding_model=text-embedding-004
```
{% endtab %}

{% tab title="OpenAI Setup" %}
```ini
LLM_PROVIDER=openai
LLM_MODEL=gpt-4o
OPENAI_API_KEY=your_openai_key_here
EMBEDDING_PROVIDER=openai
embedding_model=text-embedding-3-small
```
{% endtab %}
{% endtabs %}

#### **Reranking & Search Accuracy**

Reranking ensures that the most relevant document chunks are sent to the AI model, significantly reducing "hallucinations".

* `RERANKING_ENABLED`: Set to `true` to activate the secondary search pass.
* `RERANKING_MODEL_TYPE`: Defaults to `flashrank` (local/CPU efficient). Cloud options include `cohere`.
* `RERANKING_MODEL_NAME`: The specific model used for scoring. Default: `ms-marco-MiniLM-L-12-v2`.

#### **Database Configuration**

These variables define how the application connects to your MariaDB 11.8+ instance.Common Connection Variables:

* `DB_PORT`: The port your database is listening on (Default: `3306`).
* `DB_USER`: The username for database access.
* `DB_PASSWORD`: The password for the specified user.
* `DB_NAME`: The name of the database schema.

{% hint style="warning" %}
**SSL Mandatory for Cloud Databases**&#x20;

For cloud-hosted instances, you must set `DB_SSL_ENABLED=true` to ensure secure, encrypted communication over the public internet.&#x20;
{% endhint %}

Update the `DB_HOST` variables based on your database location:

{% tabs %}
{% tab title="Docker-Hosted (Default)" %}
Set `DB_HOST=mariadb`. The hostname must match the container name provisioned with Docker Compose. Also set your preferred `DB_USER`, `DB_PASSWORD`, and `DB_NAME` for database that will be provisioned along AI RAG stack.
{% endtab %}

{% tab title="Local / On-Premise" %}
Set `DB_HOST` to your server IP (e.g., `192.168.1.100`). Also set `DB_USER`, `DB_PASSWORD`, and `DB_NAME` for AI RAG to access your database.
{% endtab %}

{% tab title="Cloud-Hosted" %}
Set `DB_HOST` to your cloud database URL. Also set `DB_USER`, `DB_PASSWORD`, and `DB_NAME` for AI RAG to access your database.
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
### Admin User Configuration

Set the admin credentials that will be used to access the AI RAG APIs:

* `ADMIN_EMAIL`  - Admin username
* `ADMIN_PASSWORD` - Admin user password
{% endstep %}

{% step %}
### **Launch the Application**

Run the following command to start the service

{% code title="" overflow="wrap" %}
```bash
docker compose -f docker-compose.yml --env-file config.env.secure up -d
```
{% endcode %}
{% endstep %}

{% step %}
### **Verify and Access**

Check the status of your services:

{% code title="Check status" %}
```bash
docker compose -f docker-compose.yml ps
```
{% endcode %}

Once services are Up or Healthy, access the interactive Swagger UI to view all API documentation and test endpoints:

* URL: `http://localhost:8000/docs`
{% endstep %}
{% endstepper %}
