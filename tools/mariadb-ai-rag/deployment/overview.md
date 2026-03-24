# Deployment

MariaDB AI RAG 1.1 (Beta) is a containerized Retrieval-Augmented Generation (RAG) solution designed for high-precision, citation-backed outputs. The system is deployed as a multi-container Docker stack, allowing components like the API brain, background workers, and document specialists to scale independently.

{% hint style="info" %}
As of AI RAG 1.1 release, native binary-based deployments (such as `.deb` or `.rpm` packages) are no longer available.
{% endhint %}

## Prerequisites

Ensure your environment meets the following requirements before starting the deployment:

* Hardware: Minimum 4 CPU cores, 8 GB RAM, and 20 GB free disk space.
* Operating System: 64-bit Linux
* Software: Docker Engine and Docker Compose (v2.x+) must be installed.
* Mandatory Credentials:
  * [MariaDB License Key](overview.md#obtain-and-configure-the-mariadb-license-key): A valid key is required for the application to pass the startup check.
  * AI Provider API Keys: Credentials for chosen AI providers (e.g., Google Gemini or OpenAI).
* Database: A [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118)+ instance is required for native vector search support.

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

1. [`docker-compose.dockerhub-dev.yml`](https://raw.githubusercontent.com/mariadb-corporation/mariadb-docs/refs/heads/main/tools/docker-compose.dockerhub-dev.yml): The blueprint defining all services in the stack.
2. [`config.env.secure`](overview.md#configure-database-and-security-keys): The template containing all necessary environment variables.
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
### Obtain and Configure the MariaDB License Key

The application performs a mandatory validation check at startup and will fail to start if this key is missing, invalid, or expired. Each license is valid for 30 days from the day of generation, and you can generate a maximum of four at a time.

To grab your license step-by-step:

1. Navigate to the [MariaDB License Portal](https://customers.mariadb.com/license/).
2.  Login with your MariaDB ID.<br>

    <figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>
3.  Click **Get License** under the RAG Trial card.<br>

    <figure><img src="../../.gitbook/assets/image (8).png" alt=""><figcaption></figcaption></figure>
4.  Click **Generate License**. You may then _View_, _Copy_, or _Download_ the license information.<br>

    <figure><img src="../../.gitbook/assets/image (25).png" alt=""><figcaption></figcaption></figure>
5. Paste this key into your `config.env.secure` file as `MARIADB_LICENSE_KEY`.

{% hint style="info" %}
MariaDB Trial License Keys are valid for 30 days from the date of generation. You may generate multiple licenses based on your subcription tier
{% endhint %}
{% endstep %}

{% step %}
### **Configure Database and Security Keys**

Open `config.env.secure` in a text editor to set your environment variables.

#### **Security Keys**

To enable unified authentication across the API and MCP server, set these three variables to the same secure string

* `SECRET_KEY`
* `JWT_SECRET_KEY`
* `MCP_AUTH_SECRET_KEY`

#### AI Provider Setup Examples

Choose your preferred provider by configuring the following variables:

{% tabs %}
{% tab title="Google Gemini Setup" %}
```ini
LLM_PROVIDER=gemini
LLM_MODEL=gemini-2.0-flash
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

#### **Database Configuration**

Update the `DB_HOST` variables based on your database location:

{% tabs %}
{% tab title="Docker-Hosted (Default)" %}
Set `DB_HOST=mariadb`. Hostnames must match internal container names.a
{% endtab %}

{% tab title="Local / On-Premise" %}
Set `DB_HOST` to your server IP (e.g., `192.168.1.100`).
{% endtab %}

{% tab title="Cloud-Hosted" %}
Set `DB_HOST` to your cloud URL.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
**SSL Required for Cloud**

For Cloud-Hosted, you must set `DB_SSL_ENABLED=true` to ensure secure communication.
{% endhint %}
{% endstep %}

{% step %}
### **Launch the Application**

Run the following command to start the service

{% code title="" overflow="wrap" %}
```bash
docker compose -f docker-compose.dockerhub-dev.yml --env-file config.env.secure 
```
{% endcode %}
{% endstep %}

{% step %}
### **Verify and Access**

Check the status of your services:

{% code title="Check status" %}
```bash
docker compose -f docker-compose.dockerhub-dev.yml ps
```
{% endcode %}

Once services are Up or Healthy, access the interactive Swagger UI to view all API documentation and test endpoints:

* URL: `http://localhost:8000/docs`
{% endstep %}
{% endstepper %}
