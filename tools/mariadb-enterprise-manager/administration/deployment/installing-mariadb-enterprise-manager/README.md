---
description: >-
  Step-by-step instructions for deploying the Enterprise Manager Server, both in
  an environment with internet access and in an air-gapped environment.
---

# Installing MariaDB Enterprise Manager



{% hint style="info" %}
Prerequisites

* Prepare a machine for Enterprise Manager installation that complies with [Hardware and System Requirements](../hardware-and-system-requirements.md)
* Make sure that you have required network ports opened: [Network and Firewall Requirements](../hardware-and-system-requirements.md)
* Obtain MariaDB Customer Download Token
  * Navigate to the [Customer Download Token at the MariaDB Customer Portal](https://customers.mariadb.com/downloads/token/)
  * Log in using your [MariaDB ID](https://id.mariadb.com/)
  * Copy the Customer Download Token to use as the password when logging in to the MariaDB Enterprise Docker Registry
{% endhint %}

## Standard Installation (with internet access)

{% stepper %}
{% step %}
**Login to the MariaDB Enterprise Docker Registry**

Log in to the MariaDB Enterprise Docker Registry providing your [MariaDB ID](https://id.mariadb.com/) as a username and Customer Download Token as a password.

* Docker:

<pre class="language-bash"><code class="lang-bash"># Login
<strong>docker login docker.mariadb.com
</strong></code></pre>

* Podman:

```bash
# Login
podman login --compat-auth-file .docker/config.json docker.mariadb.com
```
{% endstep %}

{% step %}
**Download the installer**

Insert your Customer Download Token into the download URL and download the installer:

{% code title="# Download installer" %}
```bash
wget https://dlm.mariadb.com/<Customer_Download_Token>/enterprise-release-helpers/install-enterprise-manager.sh
```
{% endcode %}
{% endstep %}

{% step %}
**Make the installer executable**

{% code title="# Make executable" %}
```bash
chmod +x install-enterprise-manager.sh
```
{% endcode %}
{% endstep %}

{% step %}
**Run the installer**

{% hint style="info" %}
Run the installer from a directory that does not already contain an `enterprise-manager` folder, otherwise the installer treats it as an existing installation and initiates an update process.
{% endhint %}

Install Enterprise Manager by running the installer.&#x20;

{% code title="# Run installer" %}
```bash
./install-enterprise-manager.sh
```
{% endcode %}

The installer prompts you to enter IP address and port number on which Enterprise Manager should listen to for incoming connections. Verify the auto-detected value and correct it if it's wrong.

{% hint style="info" %}
This address and port must be reachable from all monitored MariaDB Server and MaxScale hosts.
{% endhint %}

After you provide the details, the installer launches Enterprise Manager.
{% endstep %}

{% step %}
**Verify containers**

Run `docker compose ps` in the `enterprise-manager` directory to check that all of the constituent Docker containers are running. The containers are:

* `enterprise-manager-grafana`
* `enterprise-manager-nginx`
* `enterprise-manager-otelcol`
* `enterprise-manager-prometheus`
* `enterprise-manager-supermax`

{% code title="# Check containers" %}
```bash
cd enterprise-manager
docker compose ps
```
{% endcode %}
{% endstep %}

{% step %}
**Access the UI**

Access Enterprise Manager UI at:

https://`<Enterprise_Manager_IP>`:8090

At the login screen, use the default username `admin` and the generated password displayed after the installation finishes.
{% endstep %}
{% endstepper %}

The installer generates a self-signed TLS certificate for Enterprise Manager. To change the certificate, follow instructions at [Security in Enterprise Manager](../../security-in-enterprise-manager.md).

To modify metrics retention time, see [Metrics retention configuration](metrics-retention-configuration.md).

## Air-Gapped Installation

{% hint style="info" %}
Prerequisites

* A private registry that supports OCI artifacts (for example, Harbor, Zot, or JFrog Artifactory).
* A staging host with internet access and access to private registry, with docker (or podman) and the ORAS CLI installed.
* Obtain container image versions from the [Enterprise Manager release notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-manager-release-notes) and substitute them wherever a version placeholder appears below.
* Preparation of air-gapped machine for Enterprise Manager installation:
  * The latest version of installer is downloaded and placed on the machine as an executable
  * A supported [container engine](../hardware-and-system-requirements.md#system-requirements) is installed
  * The ORAS CLI is installed
  * The host has access to the private registry
{% endhint %}

### **Staging Host**

{% stepper %}
{% step %}
### **Login to the** MariaDB Enterprise Docker Registry

Log in to the MariaDB Enterprise Docker Registry providing your [MariaDB ID](https://id.mariadb.com/) as a username and Customer Download Token as a password.

* ORAS:

<pre class="language-bash"><code class="lang-bash"># Login
<strong>oras login docker.mariadb.com
</strong></code></pre>

* Docker:

<pre class="language-bash"><code class="lang-bash"># Login
<strong>docker login docker.mariadb.com
</strong></code></pre>

* Podman:

```bash
# Login
podman login --compat-auth-file .docker/config.json docker.mariadb.com
```
{% endstep %}

{% step %}
**Copy installer tarball to a private registry**

Copy the installer tarball to your private registry with ORAS CLI.

```bash
# Copy installer tarball
oras cp docker.mariadb.com/enterprise-manager-distrib:<release-version> \
   <private-registry>/mariadb/enterprise-manager-distrib:<release-version>
```
{% endstep %}

{% step %}
**Copy container images to a private registry**

Pull each image, retag it for your private registry, and push it. Use the versions specified in the release notes.

<pre class="language-bash"><code class="lang-bash"><strong># Backend
</strong>docker pull docker.mariadb.com/enterprise-manager-backend:&#x3C;backend-version>
docker tag  docker.mariadb.com/enterprise-manager-backend:&#x3C;backend-version> \
   &#x3C;private-registry>/mariadb/enterprise-manager-backend:&#x3C;backend-version>
docker push &#x3C;private-registry>/mariadb/enterprise-manager-backend:&#x3C;backend-version>

# Frontend
docker pull docker.mariadb.com/enterprise-manager-frontend:&#x3C;frontend-version>
docker tag  docker.mariadb.com/enterprise-manager-frontend:&#x3C;frontend-version> \
   &#x3C;private-registry>/mariadb/enterprise-manager-frontend:&#x3C;frontend-version>
docker push &#x3C;private-registry>/mariadb/enterprise-manager-frontend:&#x3C;frontend-version>

# Grafana
docker pull docker.io/grafana/grafana:&#x3C;grafana-version>
docker tag  docker.io/grafana/grafana:&#x3C;grafana-version> \
   &#x3C;private-registry>/mariadb/grafana:&#x3C;grafana-version>
docker push &#x3C;private-registry>/mariadb/grafana:&#x3C;grafana-version>

# Prometheus
docker pull docker.io/prom/prometheus:&#x3C;prometheus-version>
docker tag  docker.io/prom/prometheus:&#x3C;prometheus-version> \
   &#x3C;private-registry>/mariadb/prometheus:&#x3C;prometheus-version>
docker push &#x3C;private-registry>/mariadb/prometheus:&#x3C;prometheus-version>

# OpenTelemetry Collector
docker pull docker.io/otel/opentelemetry-collector-contrib:&#x3C;otelcol-version>
docker tag  docker.io/otel/opentelemetry-collector-contrib:&#x3C;otelcol-version> \
   &#x3C;private-registry>/mariadb/opentelemetry-collector-contrib:&#x3C;otelcol-version>
docker push &#x3C;private-registry>/mariadb/opentelemetry-collector-contrib:&#x3C;otelcol-version>
</code></pre>
{% endstep %}
{% endstepper %}

### **Enterprise Manager Host**

{% stepper %}
{% step %}
**Login to a private registry**

Log in to your private registry.

* Docker:

<pre class="language-bash"><code class="lang-bash"># Login
<strong>docker login &#x3C;private-registry>
</strong></code></pre>

* Podman:

```bash
# Login
podman login --compat-auth-file .docker/config.json <private-registry>
```
{% endstep %}

{% step %}
**Set the container image locations for installer**

Export the image variables so the installer pulls the container images from your registry instead of the internet. Use the versions from the release notes and replace the registry prefix with yours.&#x20;

{% code title="# Set variables for image locations" %}
```bash
export IMAGE_SUPERMAX=<private-registry>/mariadb/enterprise-manager-backend:<backend-version>
export IMAGE_NGINX=<private-registry>/mariadb/enterprise-manager-frontend:<frontend-version>
export IMAGE_GRAFANA=<private-registry>/mariadb/grafana:<grafana-version>
export IMAGE_PROMETHEUS=<private-registry>/mariadb/prometheus:<prometheus-version>
export IMAGE_OTELCOL=<private-registry>/mariadb/opentelemetry-collector-contrib:<otelcol-version>
```
{% endcode %}
{% endstep %}

{% step %}
**Run the installer**

{% hint style="info" %}
Run the installer from a directory that does not already contain an `enterprise-manager` folder, otherwise the installer treats it as an existing installation and initiates an update process.
{% endhint %}

Install Enterprise Manager by running the installer:

{% code title="# Run installer" %}
```bash
./install-enterprise-manager.sh \
  --registry <private-registry> \
  --repository mariadb/enterprise-manager-distrib \
  --tag <release-version>
```
{% endcode %}

The flags tell the installer where to pull the installation tarball from:

* `--registry` — your private registry hostname or IP address.
* `--repository` — the path to the tarball within your registry.
* `--tag` — the Enterprise Manager release version.

The installer prompts you to enter IP address and port number on which Enterprise Manager should listen to for incoming connections. Verify the auto-detected value and correct it if it's wrong.

{% hint style="info" %}
This address and port must be reachable from all monitored MariaDB Server and MaxScale hosts.
{% endhint %}

After you provide the details, the installer launches Enterprise Manager.
{% endstep %}

{% step %}
**Persist the container image locations**

The installer's generated `.env` file does not include the image locations you exported in the previous step. Add them to `enterprise-manager/.env` so restarts and upgrades continue to use your registry:

{% code title="# Persist image locations in .env file" %}
```bash
IMAGE_SUPERMAX=<private-registry>/mariadb/enterprise-manager-backend:<backend-version>
IMAGE_NGINX=<private-registry>/mariadb/enterprise-manager-frontend:<frontend-version>
IMAGE_GRAFANA=<private-registry>/mariadb/grafana:<grafana-version>
IMAGE_PROMETHEUS=<private-registry>/mariadb/prometheus:<prometheus-version>
IMAGE_OTELCOL=<private-registry>/mariadb/opentelemetry-collector-contrib:<otelcol-version>
```
{% endcode %}
{% endstep %}

{% step %}
**Verify containers**

Run `docker compose ps` in the `enterprise-manager` directory to check that all of the constituent Docker containers are running. The containers are:

* `enterprise-manager-grafana`
* `enterprise-manager-nginx`
* `enterprise-manager-otelcol`
* `enterprise-manager-prometheus`
* `enterprise-manager-supermax`

{% code title="# Check containers" %}
```bash
cd enterprise-manager
docker compose ps
```
{% endcode %}
{% endstep %}

{% step %}
**Access the UI**

Access Enterprise Manager UI at:

https://`<Enterprise_Manager_IP>`:8090

At the login screen, use the default username `admin` and the generated password displayed after the installation finishes.
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
