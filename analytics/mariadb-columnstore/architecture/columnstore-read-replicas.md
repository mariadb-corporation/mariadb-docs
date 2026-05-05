---
description: >-
  MariaDB ColumnStore read replicas (Alpha) add read-only nodes that scale
  read throughput by forwarding writes to RW nodes; they share storage and
  need at least one RW node per cluster.
---

# ColumnStore Read Replicas

{% hint style="info" %}
**The ColumnStore Read Replica topology is an Alpha release.** Do not use it in production without testing in your development environment first.
{% endhint %}

## Overview

The Read Replicas feature in MariaDB ColumnStore enables horizontal scaling of read performance by incorporating read-only nodes into a multi-node cluster. These replicas differ from standard ColumnStore nodes, in that they don't run the **WriteEngineServer process**. This means Read Replica nodes cannot handle write operations directly — instead, any write queries attempted on a replica are automatically forwarded to a read-write (RW) node.

Replicas utilize shared storage with other nodes in the cluster, ensuring data consistency without duplication. A key requirement is maintaining at least one RW node — a cluster consisting solely of read replicas is not operational and cannot process reads or writes.

{% hint style="warning" %}
Read-only nodes are incompatible with S3 as the storage backend.

Additionally, there is no automatic promotion of a read replica to RW mode if the only RW node fails, which could lead to temporary downtime until manual intervention.
{% endhint %}

## Key Features

* **Horizontal Read Scaling:** Adds compute power for handling more read-intensive queries without impacting write performance.
* **Write Forwarding:** Ensures writes on replicas are redirected to RW nodes, maintaining data integrity.
* **Shared Storage:** Replicas access the same DBRoots as RW nodes, promoting efficiency and reducing storage overhead.

## Key Commands

{% hint style="info" %}
These commands require [CMAPI](../reference/cmapi/).
{% endhint %}

* **Add Read Replica.** To introduce a read-only node for scaling reads, run this command:

```bash
sudo mcs node add --read-replica --node <private-ip>
```

* **Remove Node.** To safely remove any node (RW or replica) from the cluster, run this command:

```bash
sudo mcs node remove --node <private-ip>
```

This reassigns resources as needed without cluster disruption.

* **Verify Status.** To monitor the cluster's health and node roles, issue:

```bash
sudo mcs cluster status
```

## Limitations

* Node addition is restricted to private IPs only.
* Incompatible with S3 storage, limiting use to shared file systems.
* No automatic failover or promotion mechanism if the sole RW node goes down, requiring manual recovery.
* At least one RW node must always be present for the cluster to function properly, supporting both read and write operations.

## How-To

### Prerequisites

{% hint style="info" %}
**Ensure shared storage is mounted on all nodes** (at /var/lib/columnstore/data1 for non-s3 configuration), to ensure data consistency across RW nodes and read replicas.
{% endhint %}

Refer to [shared storage setup](columnstore-architectural-overview.md#shared-local-storage) for exact mount points details.

### Installation and Setup

{% stepper %}
{% step %}
**Set Up MariaDB Repository**

Run the following to add the MariaDB repository (adjust "11.4" to the latest stable version):

```bash
wget https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup ;
chmod +x mariadb_es_repo_setup;
./mariadb_es_repo_setup --token="xxxxx" --apply --mariadb-server-version="11.4"
```

See [this page](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage) for additional details about the ES repo setup.
{% endstep %}

{% step %}
**Install Packages**

{% hint style="info" %}
Run the following commands on all nodes.
{% endhint %}

**For RPM-based systems**, run this command:

```bash
sudo dnf install -y \
MariaDB-server MariaDB-columnstore-engine MariaDB-columnstore-cmapi
```

Refer to [this blog post](../columnstore-quickstart-guides/mariadb-columnstore-usage-guide.md) for additional information.

**For DEB-based systems**, run these commands:

```bash
sudo apt update
sudo apt install -y mariadb-server mariadb-plugin-columnstore mariadb-columnstore-cmapi
```
{% endstep %}

{% step %}
**Start and Enable Services**

```bash
sudo systemctl start mariadb
sudo systemctl enable mariadb
sudo systemctl start mariadb-columnstore-cmapi
sudo systemctl enable mariadb-columnstore-cmapi
```
{% endstep %}

{% step %}
**Configure the Initial RW Node**

On the primary RW node, set up the cluster API key (use a secure API key):

```bash
sudo mcs cluster set api-key --key <your-api-key-here>
```
{% endstep %}

{% step %}
**Add the Initial RW Node to the Cluster**

Run this from the primary RW node:

```bash
sudo mcs node add --node <private-ip-of-rw-node>
```
{% endstep %}

{% step %}
**Add Read Replica Nodes**

From the primary RW node, add each read replica:

```bash
sudo mcs node add --read-replica --node <private-ip-of-replica>
```
{% endstep %}

{% step %}
**Verify the Cluster**

Check the status to ensure nodes are added and the cluster is healthy:

```bash
sudo mcs cluster status
```
{% endstep %}

{% step %}
**Configure Replication Between Nodes**

See [this page](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/setting-up-replication) for instructions on how to set up replication, and [this page](../management/deployment/install-guide/multinode-s3/step-4-test-enterprise-columnstore.md) for instructions how to create user accounts and configure replication for multi-node local storage.
{% endstep %}

{% step %}
**Configure MaxScale**

See [this page](../management/deployment/install-guide/multnode-localstorage/step-7-start-and-configure-mariadb-maxscale.md) for instructions.
{% endstep %}
{% endstepper %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
