---
description: Instructions for updating an existing Enterprise Manager deployment.
---

# Update Enterprise Manager

{% hint style="info" %}
Prerequisites

* Make a backup of Enterprise Manager data following instructions in [Backup & Restore of Enterprise Manager](https://mariadb.com/docs/tools/~/changes/145/mariadb-enterprise-manager/administration/backup-and-restore-of-enterprise-manager)
{% endhint %}

## Enterprise Manager Update

{% stepper %}
{% step %}
**Log in to Docker registry**

Login to the MariaDB Enterprise Docker Registry providing your [MariaDB ID](https://id.mariadb.com/) as a username and Customer Download Token as a password.

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
**Download the latest installer**

{% hint style="warning" %}
This installer performs an in-place update of an existing Enterprise Manager deployment. Download and run it in the directory that contains the existing deployment’s `enterprise-manager/` installation directory.
{% endhint %}

Insert your Customer Download Token into the download URL and download the latest installer in the the same folder where you have folder `enterprise-manager`:

```bash
# Download installer
wget https://dlm.mariadb.com/<Customer_Download_Token>/enterprise-release-helpers/install-enterprise-manager.sh
```
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

Install Enterprise Manager by running the installer:

{% code title="# Run installer" %}
```bash
./install-enterprise-manager.sh
```
{% endcode %}

During this step, the installer renames the existing `enterprise-manager/` directory to `enterprise-manager.old/`, downloads and extracts the new installation tarball into a new `enterprise-manager/` directory, and copies the existing `.env` file and TLS certificates from `enterprise-manager.old/` to preserve the current configuration. It then pulls the required container images and recreates the Enterprise Manager containers while reusing the existing container volumes.

When the update completes successfully, the message `Enterprise Manager has been upgraded` is displayed.
{% endstep %}

{% step %}
**Verify containers**

Run `docker compose ps` in the `enterprise-manager` directory to check that all of the constituent containers are running. The containers are:

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
{% endstepper %}

### Agent update <a href="#agent-update" id="agent-update"></a>

Update the `mema-agent` on each monitored MariaDB Server and MaxScale nodes. After the update, verify that the host continues to report to MariaDB Enterprise Manager.
