---
description: MariaDB Enterprise Manager installation and configuration guide
---

# Quickstart Guide

MariaDB Enterprise Manager is a database management and observability solution that provides advanced topology-aware monitoring coupled with visual schema management, query editing, and ERD design across multiple database connections.

This guide describes steps to install MariaDB Enterprise Manager for evaluation purposes.

## Prerequisites

{% stepper %}
{% step %}
#### Prepare a machine for Enterprise Manager installation

[Machine requirements](administration/deployment/hardware-and-system-requirements.md) (minimal hardware resources for evaluation):

* CPU: 2 cores (or 2 vCPUs) with x86-64 architecture
* RAM: 4 GB
* Storage: 100 GB

Other requirements:

* 64-bit Linux OS with installed Docker engine and Docker Compose: https://docs.docker.com/engine/install/
* [Network ports](administration/deployment/network-and-firewall-requirements.md) 8090 and 4318 opened for inbound traffic
{% endstep %}

{% step %}
#### Obtain MariaDB Customer Download Token

1. Navigate to the [Customer Download Token at the MariaDB Customer Portal](https://customers.mariadb.com/downloads/token/)
2. Log in using your [MariaDB ID](https://id.mariadb.com/)
3. Copy the Customer Download Token — you will use it as the password when logging in to the MariaDB Enterprise Docker Registry
{% endstep %}

{% step %}
#### Setup MariaDB Enterprise Repository - "MariaDB Enterprise Tools"

[Set up the repository for each monitored MariaDB Server and MaxScale](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage#mariadb_es_repo_setup)
{% endstep %}
{% endstepper %}

## Step 1: Install Enterprise Manager

{% stepper %}
{% step %}
#### Login to the MariaDB Enterprise Docker Registry

Use your MariaDB ID as username and Customer Download Token as password:

```bash
docker login docker.mariadb.com
```
{% endstep %}

{% step %}
#### Download the installation script

Insert your Customer Download Token into the download URL and download the installation script:

```bash
wget https://dlm.mariadb.com/<Customer_Download_Token>/enterprise-release-helpers/install-enterprise-manager.sh
```
{% endstep %}

{% step %}
#### Make the installation script executable

```bash
chmod +x install-enterprise-manager.sh
```
{% endstep %}

{% step %}
#### Run the installer with default options

```bash
./install-enterprise-manager.sh
```
{% endstep %}

{% step %}
#### Access Enterprise Manager UI

Open in a browser:

https://\<Enterprise\_Manager\_IP>:8090

At the login screen, use the default username `admin` and the generated password displayed after the installation script finishes.
{% endstep %}
{% endstepper %}

## Step 2: Register database topology in Enterprise Manager and enable monitoring

Below are procedures for topologies without and with MaxScale.

### Topology without MaxScale

{% stepper %}
{% step %}
#### Create monitoring user for each MariaDB Server (Enterprise Manager access)

Run on each [MariaDB server](usage/monitoring/dashboards/mariadb-server.md) (replace \<Enterprise\_Manager\_IP> ):

```sql
CREATE USER 'monitor'@'<Enterprise_Manager_IP>' IDENTIFIED BY '<password>';
GRANT REPLICA MONITOR ON *.* TO 'monitor'@'<Enterprise_Manager_IP>';
```
{% endstep %}

{% step %}
#### Add database topology in Enterprise Manager UI

Add each MariaDB Server in the Enterprise Manager UI, providing access details for each server.

<figure><img src="../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
#### Install agent on each MariaDB Server to enable metrics collection

On each MariaDB server install the [mema-agent package](administration/deployment/adding-databases/agent-installation-t-copy.md).

* RedHat-based (RHEL, CentOS, Rocky Linux):

```bash
sudo yum install -y mema-agent
```

* Debian-based (Ubuntu, Debian):

```bash
sudo apt install -y mema-agent
```
{% endstep %}

{% step %}
#### Create monitoring user for agent access (on each MariaDB Server)

Run on each MariaDB server:

```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT PROCESS, BINLOG MONITOR, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```
{% endstep %}

{% step %}
#### Setup agent using the command generated in Enterprise Manager UI

1.  In the UI, click the three dots beside the server you want to install the Agent on.\\

    <figure><img src="../.gitbook/assets/image (2) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
2. The UI will generate a unique setup command for that specific server with the username and password you provide.
3. Copy and run the command on that specific server.
4.  Repeat for all servers in the database fleet.\\

    <figure><img src="../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
#### Wait for metrics to appear

Wait 1–2 minutes for [metrics](../mariadb-enterprise-operator/metrics.md) to start populating in Enterprise Manager from the agents (default collection interval is 1 minute).
{% endstep %}
{% endstepper %}

<figure><img src="../.gitbook/assets/image (5) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Topology with MaxScale

{% stepper %}
{% step %}
#### Add MaxScale instances to Enterprise Manager

Add each MaxScale instance in the Enterprise Manager UI, providing access details.

<figure><img src="../.gitbook/assets/image (12).png" alt=""><figcaption></figcaption></figure>
{% endstep %}

{% step %}
#### Install agent on each MaxScale and MariaDB Server

On each MaxScale and each MariaDB server install the mema-agent package.

* RedHat-based (RHEL, CentOS, Rocky Linux):

```bash
sudo yum install -y mema-agent
```

* Debian-based (Ubuntu, Debian):

```bash
sudo apt install -y mema-agent
```
{% endstep %}

{% step %}
#### Create monitoring user for agent access (on each MariaDB Server)

Run on each MariaDB server:

```sql
CREATE USER 'monitor'@'localhost' IDENTIFIED BY '<password>';
GRANT PROCESS, BINLOG MONITOR, REPLICA MONITOR, REPLICATION MASTER ADMIN ON *.* TO 'monitor'@'localhost';
```
{% endstep %}

{% step %}
#### Setup agent using the command generated in Enterprise Manager UI

1. Click the three dots beside the server or MaxScale instance you want to install the Agent on and click **Install Agent**.
2. The UI will generate a unique setup command for that specific server/MaxScale instance with the username and password you provide. Copy the command.
3. On that specific server/MaxScale instance, paste and run the command in your terminal.
4. Repeat for all MaxScale and MariaDB servers.
{% endstep %}

{% step %}
#### Wait for metrics to appear

Wait 1–2 minutes for metrics to start populating in Enterprise Manager from the agents (default collection interval is 1 minute).
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
