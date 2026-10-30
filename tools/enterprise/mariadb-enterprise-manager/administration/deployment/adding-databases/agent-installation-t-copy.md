---
description: >-
  Instructions for installing the mema-agent application using native OS package
  managers, including prerequisite steps for creating a local monitor user in
  MariaDB.
---

# Agent Installation

{% hint style="warning" %}
To install `mema-agent`, you need to set up [MariaDB Enterprise Repository - "MariaDB Enterprise Tools"](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage#repositories).
{% endhint %}

The `mema-agent` is a small application that must be installed on every server you wish to monitor with MariaDB Enterprise Manager, including MariaDB Server nodes and MaxScale nodes.

This guide covers the recommended installation method using a package manager.

### Prerequisite: Create the Local Monitor User

Before installing the agent on a MariaDB Server host, you must create a local user that the agent will use to connect to the database and collect metrics.

Log in to your MariaDB Server and run the following:

{% code title="Create monitor user" %}
```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT SELECT, PROCESS, REPLICATION CLIENT, RELOAD, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```
{% endcode %}

_Replace `<password>` with a secure password. You will need these credentials later when linking the agent in the Enterprise Manager UI._

### Installation via Package Manager (Recommended)

This method uses your OS's native package manager (`dnf`, `apt`, `zypper`) to install the agent from the MariaDB Enterprise repository.

#### Step 1: Configure the MariaDB Enterprise Repository

If you haven't already configured the MariaDB Enterprise repository on the server, follow these steps.

{% stepper %}
{% step %}
**Get your Customer Download Token**

* Navigate to the [MariaDB Customer Portal](https://customers.mariadb.com/downloads/token/) and log in.
* Copy your **Customer Download Token**. You will need this for the script.
{% endstep %}

{% step %}
**Download the repository setup script**

In your server's terminal, download the official setup script:

```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
```
{% endstep %}

{% step %}
**Run the script**

Make the script executable, then run it with your download token:

{% code title="# Make script executable and run" %}
```bash
chmod +x mariadb_es_repo_setup
sudo ./mariadb_es_repo_setup --token="YOUR_TOKEN_HERE" --apply
```
{% endcode %}

_Replace `YOUR_TOKEN_HERE` with the token you copied from the Customer Portal._
{% endstep %}
{% endstepper %}

#### Step 2: Install the Agent Package

Once the repository is configured, use your system's package manager to install the agent.

{% tabs %}
{% tab title="Red Hat / Rocky / CentOS" %}
```bash
sudo dnf install mema-agent
```
{% endtab %}

{% tab title="Debian / Ubuntu" %}
```bash
sudo apt-get install mema-agent
```
{% endtab %}

{% tab title="SLES" %}
```bash
sudo zypper install mema-agent
```
{% endtab %}
{% endtabs %}

The agent is now installed, but it isn't running yet: the package enables and starts no services. The agent starts when you link it to Enterprise Manager, because the `mema-agent setup` command that links it writes the agent's configuration and then enables and starts `mema-agent.target`.

### Upgrading the Agent

Upgrade the agent with your system's package manager:

{% tabs %}
{% tab title="Red Hat / Rocky / CentOS" %}
```bash
sudo dnf upgrade mema-agent
```
{% endtab %}

{% tab title="Debian / Ubuntu" %}
```bash
sudo apt-get update
sudo apt-get install --only-upgrade mema-agent
```
{% endtab %}

{% tab title="SLES" %}
```bash
sudo zypper update mema-agent
```
{% endtab %}
{% endtabs %}

From `mema-agent` 1.1.3, an upgrade restarts a running agent, so it switches to the new version immediately. An agent that isn't running is not started. Releases up to and including 1.1.0 don't restart the agent. If you install one of them, restart it yourself:

```bash
sudo systemctl daemon-reload
sudo systemctl restart mema-agent.target
```

{% hint style="warning" %}
**Nodes linked with OpenTelemetry credentials**

On a node linked with `--otlp-user` and `--otlp-password`, the collector never started on any 1.0.x agent, so the node sent no metrics, even though `mema-agent setup` reported success. Upgrading the package doesn't fix the configuration that 1.0.x wrote. After upgrading such a node, run the setup command again with the same options. Nodes linked without OpenTelemetry credentials aren't affected.
{% endhint %}

{% hint style="info" %}
Some `mema-agent` 1.0.1 deb packages enabled `mema-agent.target` when they were installed. An upgrade keeps that setting, so on a node that was never linked, the target can stay enabled without being configured. Linking the agent configures it. To leave the node unlinked instead, disable the target with `sudo systemctl disable mema-agent.target`.
{% endhint %}

### Next Steps: Linking the Agent 🔗

After the agent is installed, it is not yet configured or linked to your MariaDB Enterprise Manager server, and it doesn't run until it is linked.

The final step is to link the agent, which is done from the Enterprise Manager UI. Please refer to the [Adding Databases guide](./) for the specific steps to generate the linking command.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
