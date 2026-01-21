---
description: >-
  Deployment instructions for a single-node MariaDB Enterprise Server instance
  with the ColumnStore engine using S3-compatible object storage.
---

# Enterprise Server with ColumnStore (Object Storage)

## Overview

This procedure describes the deployment of the Single-Node Enterprise ColumnStore topology with Object storage.

MariaDB Enterprise ColumnStore 23.10 is a columnar storage engine for MariaDB Enterprise Server and Enterprise ColumnStore is best suited for Online Analytical Processing (OLAP) workloads.

This procedure has 5 steps, which are executed in sequence.

This page provides an overview of the topology, requirements, and deployment procedures.

Please read and understand this procedure before executing.

## Procedure Steps

<table><thead><tr><th width="189.11102294921875">Step</th><th>Description</th></tr></thead><tbody><tr><td>Step 1</td><td><a href="step-1-prepare-systems-for-enterprise-columnstore-nodes.md">Prepare System for Enterprise ColumnStore</a></td></tr><tr><td>Step 2</td><td><a href="step-2-install-enterprise-columnstore.md">Install Enterprise ColumnStore</a></td></tr><tr><td>Step 3</td><td><a href="step-3-start-and-configure-enterprise-columnstore.md">Start and Configure Enterprise ColumnStore</a></td></tr><tr><td>Step 4</td><td><a href="step-4-test-enterprise-columnstore.md">Test Enterprise ColumnStore</a></td></tr><tr><td>Step 5</td><td><a href="step-5-bulk-import-of-data.md">Bulk Import Data to Enterprise ColumnStore</a></td></tr></tbody></table>

## Support

Customers can obtain support by [submitting a support case](https://mariadb.com/support/).

## Components

The following components are deployed during this procedure:

<table><thead><tr><th width="248.370361328125">Component</th><th>Function</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/">MariaDB Enterprise Server</a></td><td>Modern SQL RDBMS with high availability, pluggable storage engines, hot online backups, and audit logging.</td></tr></tbody></table>

### MariaDB Enterprise Server Components

<table><thead><tr><th width="285.1112060546875">Component</th><th>Description</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/">MariaDB Enterprise ColumnStore</a></td><td><ul><li>Columnar Storage Engine</li><li>Optimized for Online Analytical Processing (OLAP) workloads</li><li>S3-compatible object storage</li></ul></td></tr></tbody></table>

## Topology

<figure><img src="../../../../.gitbook/assets/ent-col-single-node-topology-object-no-title.png" alt=""><figcaption></figcaption></figure>

The Single-Node Enterprise ColumnStore topology provides support for Online Analytical Processing (OLAP) workloads to MariaDB Enterprise Server.

The Enterprise ColumnStore node:

* Receives queries from the application
* Executes queries
* Use [S3-compatible object storage](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/storagemanager/certified-s3-object-storage-providers) for data

### High Availability

Single-Node Enterprise ColumnStore does not provide high availability (HA) for Online Analytical Processing (OLAP). If you would like to deploy Enterprise ColumnStore with high availability, see [Enterprise ColumnStore with Object storage](../../columnstore-object-storage/).

## Requirements

These requirements are for the Single-Node Enterprise ColumnStore, when deployed with MariaDB Enterprise Server and MariaDB Enterprise ColumnStore.

## Operating System

* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, PPC64LE, ARM64)
* Red Hat UBI 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* Ubuntu 20.04 LTS (x86\_64, ARM64)
* Ubuntu 22.04 LTS (x86\_64, ARM64)
* Ubuntu 24.04 LTS (x86\_64, ARM64)

### Minimum Hardware Requirements

MariaDB Enterprise ColumnStore's minimum hardware requirements are not intended for production environments, but the minimum hardware requirements can be appropriate for development and test environments. For production environments, see the [recommended hardware requirements](./#recommended-hardware-requirements) instead.

The minimum hardware requirements are:

| Component                   | CPU      | Memory |
| --------------------------- | -------- | ------ |
| Enterprise ColumnStore node | 4+ cores | 16+ GB |

MariaDB Enterprise ColumnStore will refuse to start if the system has less than 3 GB of memory.

If Enterprise ColumnStore is started on a system with less memory, the following error message will be written to the ColumnStore system log called `crit.log`:

```
Apr 30 21:54:35 a1ebc96a2519 PrimProc[1004]: 35.668435 |0|0|0| C 28 CAL0000: Error total memory available is less than 3GB.
```

And the following error message will be raised to the client:

```
ERROR 1815 (HY000): Internal error: System is not ready yet. Please try again.
```

### Recommended Hardware Requirements

MariaDB Enterprise ColumnStore's recommended hardware requirements are intended for production analytics.

The recommended hardware requirements are:

| Component                   | CPU       | Memory  |
| --------------------------- | --------- | ------- |
| Enterprise ColumnStore node | 64+ cores | 128+ GB |

### Storage Requirements

Single-node Enterprise ColumnStore with Object Storage requires the following storage type:

<table><thead><tr><th width="288.6666259765625">Storage Type</th><th>Description</th></tr></thead><tbody><tr><td><a href="./#s3-compatible-object-storage-requirements">S3-Compatible Object Storage</a></td><td>Single-node Enterprise ColumnStore with Object Storage uses S3-compatible object storage to store data.</td></tr></tbody></table>

### S3-Compatible Object Storage Requirements

Single-node Enterprise ColumnStore with Object Storage uses S3-compatible object storage to store data.

Many S3-compatible object storage services exist. MariaDB Corporation cannot make guarantees about all S3-compatible object storage services, because different services provide different functionality.

For the preferred S3-compatible object storage providers that provide cloud and hardware solutions, see the following sections:

* [Cloud](./#preferred-object-storage-providers-cloud)
* [Hardware](./#preferred-object-storage-providers-hardware)

The use of non-cloud and non-hardware providers is at your own risk.

If you have any questions about using specific S3-compatible object storage with MariaDB Enterprise ColumnStore, [contact us](https://mariadb.com/contact).

### Preferred Object Storage Providers: Cloud

* Amazon Web Services (AWS) S3
* Google Cloud Storage
* Azure Storage
* Alibaba Cloud Object Storage Service

### Preferred Object Storage Providers: Hardware

* Cloudian HyperStore
* Dell EMC
* Seagate Lyve Rack
* Quantum ActiveScale
* IBM Cloud Object Storage

## Quick Reference

MariaDB Enterprise Server Configuration Management

<table><thead><tr><th width="221.111083984375">Method</th><th>Description</th></tr></thead><tbody><tr><td>Configuration File</td><td>Configuration files (such as <code>/etc/my.cnf</code>) can be used to set <a href="../../../../ha-and-performance/optimization-and-tuning/system-variables/">system variables</a> and <a href="../../../../reference/full-list-of-mariadb-options-system-and-status-variables.md">options</a>. The server must be restarted to apply changes made to configuration files.</td></tr><tr><td>Command-line</td><td>The server can be started with command-line options that set <a href="../../../../ha-and-performance/optimization-and-tuning/system-variables/">system variables</a> and <a href="../../../../reference/full-list-of-mariadb-options-system-and-status-variables.md">options</a>.</td></tr><tr><td>SQL</td><td>Users can set <a href="../../../../ha-and-performance/optimization-and-tuning/system-variables/">system variables</a> that support dynamic changes on-the-fly using the <a href="../../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md">SET</a> statement.</td></tr></tbody></table>

MariaDB Enterprise Server packages are configured to read configuration files from different paths, depending on the operating system. Making custom changes to Enterprise Server default configuration files is not recommended because custom changes may be overwritten by other default configuration files that are loaded later.

To ensure that your custom changes will be read last, create a custom configuration file with the `z-` prefix in one of the include directories.

<table><thead><tr><th width="317.1112060546875" valign="top">Distribution</th><th valign="top">Example Configuration File Path</th></tr></thead><tbody><tr><td valign="top"><ul><li>CentOS</li><li>Red Hat Enterprise Linux (RHEL)</li></ul></td><td valign="top"><code>/etc/my.cnf.d/z-custom-mariadb.cnf</code></td></tr><tr><td valign="top"><ul><li>Debian</li><li>Ubuntu</li></ul></td><td valign="top"><code>/etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf</code></td></tr></tbody></table>

## MariaDB Enterprise Server Service Management

The `systemctl` command is used to start and stop the MariaDB Enterprise Server service.

<table><thead><tr><th width="227.037109375">Operation</th><th>Command</th></tr></thead><tbody><tr><td>Start</td><td><code>sudo systemctl start mariadb</code></td></tr><tr><td>Stop</td><td><code>sudo systemctl stop mariadb</code></td></tr><tr><td>Restart</td><td><code>sudo systemctl restart mariadb</code></td></tr><tr><td>Enable during startup</td><td><code>sudo systemctl enable mariadb</code></td></tr><tr><td>Disable during startup</td><td><code>sudo systemctl disable mariadb</code></td></tr><tr><td>Status</td><td><code>sudo systemctl status mariadb</code></td></tr></tbody></table>

## Next Step

Navigation in the Single-Node Enterprise ColumnStore topology with Object storage deployment procedure:

Next: Step 1: Install MariaDB Enterprise ColumnStore.

{% include "../../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
