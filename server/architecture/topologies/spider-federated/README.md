---
description: Deploy Spider Federated Topology
---

# Spider Federated

## Overview

<table><thead><tr><th valign="top">Software Version</th><th>Diagram</th><th valign="top">Features</th></tr></thead><tbody><tr><td valign="top"><ul><li>Enterprise Server 10.4</li><li>Enterprise Server 10.5</li><li>Enterprise Server 10.6</li><li>Enterprise Server 11.4</li></ul></td><td><img src="../../../.gitbook/assets/spider-federated.svg" alt=""></td><td valign="top"><p><strong>Read from and write to tables on remote ES nodes</strong></p><ul><li>Spider Node uses Spider storage engine for Federated Spider Tables</li><li>Federated Spider Table is a "virtual" table</li><li>Spider uses MariaDB foreign data wrapper to query Data Table on Data Node</li><li>Data Node uses non-Spider storage engine for Data Tables</li><li>Supports transactions</li><li>Enterprise Server 10.3+, Enterprise Spider</li></ul></td></tr></tbody></table>

This procedure describes the deployment of the **Spider Federated topology** with MariaDB Enterprise Server

This procedure incrementally deploys MariaDB Enterprise Spider on an existing MariaDB Enterprise Server deployment.

In the Spider Federated topology, a Spider Node contains one or more "virtual" Spider Tables. A Spider Table does not store data. When a Spider Table is queried, the Enterprise Spider storage engine uses a MariaDB foreign data wrapper to read from and write to a Data Table on a Data Node.

This procedure has 3 steps, which are executed in sequence.

This page provides an overview of the topology, requirements, and deployment procedure.

The topology described is representative of basic product capabilities. MariaDB products can be deployed to form other topologies, leverage advanced product capabilities, or combine the capabilities of multiple topologies.

## Prerequisites

If you have not yet deployed MariaDB Enterprise Server on the Spider Node and Data Node, first deploy a topology containing MariaDB Enterprise Server. Several [topologies](../) are documented.

## Procedure Steps

<table><thead><tr><th width="166.592529296875">Step</th><th>Description</th></tr></thead><tbody><tr><td>Step 1</td><td><a href="step-1-install-enterprise-spider.md">Install Enterprise Spider</a></td></tr><tr><td>Step 2</td><td><a href="step-2-configure-spider-node-and-data-node.md">Configure Spider Node and Data Node</a></td></tr><tr><td>Step 3</td><td><a href="step-3-test-spider-federated-topology.md">Test Spider Federated Topology</a></td></tr></tbody></table>

## Support

Customers can obtain support by [submitting a support case](https://mariadb.com/support/).

## Components

The following components are deployed during this procedure:

<table><thead><tr><th width="302.8887939453125">Component</th><th>Function</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/">MariaDB Enterprise Server</a></td><td>Modern SQL RDBMS with high availability, pluggable storage engines, hot online backups, and audit logging.</td></tr><tr><td><a href="../../../server-usage/storage-engines/spider/">MariaDB Enterprise Spider</a></td><td>Storage engine used by Spider Tables to read from and write to Data Tables using the MariaDB foreign data wrapper.</td></tr></tbody></table>

## Term Definitions

<table><thead><tr><th width="240.073974609375">Term</th><th>Definition</th></tr></thead><tbody><tr><td>Data Node</td><td>A Data Node is a MariaDB Enterprise Server node that contains one or more Data Tables.</td></tr><tr><td>Data Table</td><td>A Data Table stores data for a Spider Table. When a Spider Table is queried, the Enterprise Spider storage engine uses the MariaDB foreign data wrapper to read from and write to the Data Table on a Data Node. The Data Table must be created on the Data Node with the same structure as the Spider Table. The Data Table must use a non-Spider storage engine, such as <a href="../../../server-usage/storage-engines/innodb/">InnoDB</a> or <a href="https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/architecture/columnstore-storage-engine-overview">ColumnStore</a>.</td></tr><tr><td>ODBC Data Source</td><td>An ODBC Data Source relies on an ODBC Driver and an ODBC Driver Manager to query an external data source.</td></tr><tr><td>ODBC Driver</td><td>An ODBC Driver is a library that integrates with a ODBC Driver Manager to query an external data source.</td></tr><tr><td>ODBC Driver Manager</td><td>An ODBC Driver Manager allows applications to use ODBC Drivers.</td></tr><tr><td>Spider Node</td><td>A Spider Node is a MariaDB Enterprise Server node that contains one or more Spider Tables.</td></tr><tr><td>Spider Node</td><td>A Spider Table is a virtual table that does not store data. When a Spider Table is queried, the <a href="../../../server-usage/storage-engines/spider/">Enterprise Spider storage engine</a> uses foreign data wrappers to read from and write to Data Tables on Data Nodes or ODBC Data Sources.</td></tr></tbody></table>

## Topology

<figure><img src="../../../.gitbook/assets/spider-federated.svg" alt=""><figcaption></figcaption></figure>

In the Spider Federated topology, a Spider Node contains one or more "virtual" Spider Tables. A Spider Table does not store data. When a Spider Table is queried, the Enterprise Spider storage engine uses a MariaDB foreign data wrapper to read from and write to a Data Table on a Data Node.

The Spider Federated topology consists of:

* One MariaDB Enterprise Server node is a Spider Node
* One MariaDB Enterprise Server node is a Data Node

The Spider Node:

* Contains one or more Spider Tables
* Uses the [Enterprise Spider storage engine](../../../server-usage/storage-engines/spider/) plugin for Spider Tables
* Uses a MariaDB foreign data wrapper to query the Data Table on the Data Node

The Data Node:

* Contains a Data Table for each Spider Table
* Uses a non-Spider storage engine for each Data Table, such as [InnoDB](../../../server-usage/storage-engines/innodb/) or [ColumnStore](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/mariadb-columnstore/architecture/columnstore-storage-engine-overview)

For additional information, see "[Spider Federated Topology Operations](../../../server-usage/storage-engines/spider/spider-storage-engine-introduction/mariadb-enterprise-spider-operations/federated-mariadb-enterprise-spider-topology-operations/)".

## Requirements

These requirements are for the Spider Federated topology when deployed with MariaDB Enterprise Server

* [Node Count](./#node-count)
* [Operating Systems](./#operating-systems)

### Node Count

* One or more MariaDB Enterprise Server nodes must be deployed as Spider Nodes. The Spider Nodes contain Spider Tables.
* One or more MariaDB Enterprise Server nodes must be deployed as Data Nodes. The Data Nodes contain Data Tables.

### Operating Systems

In alignment to the [enterprise lifecycle](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/enterprise-server-lifecycle), the Spider Federated topology with MariaDB Enterprise Server is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, PPC64LE, ARM64)
* Red Hat UBI 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 LTS (x86\_64, ARM64)
* Ubuntu 22.04 LTS (x86\_64, ARM64)
* Ubuntu 24.04 LTS (x86\_64, ARM64)

## Next Step

Navigation in the procedure "Deploy Spider Federated Topology":

Next: Step 1: Install Enterprise Spider

{% include "../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
