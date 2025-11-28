# ColumnStore Storage Engine

## Overview

MariaDB Enterprise ColumnStore integrates with MariaDB Enterprise Server using the ColumnStore storage engine plugin. The ColumnStore storage engine plugin enables MariaDB Enterprise Server to interact with ColumnStore tables.

For deployment instructions and available documentation, see "MariaDB Enterprise ColumnStore."

The ColumnStore storage engine has the following features:

| Feature                | Detail             | Resources                                                                                                                                     |
| ---------------------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Storage Engine         | ColumnStore        |                                                                                                                                               |
| Availability           | ES 10.5+, CS 10.5+ | MariaDB Enterprise Server                                                                                                                     |
| Workload Optimization  | OLAP and Hybrid    | [OLAP Workloads ](columnstore-storage-architecture.md#olap-workloads)[Hybrid Workloads](columnstore-storage-architecture.md#hybrid-workloads) |
| Table Orientation      | Columnar           | [Columnar Storage Engine](columnstore-architectural-overview.md#columnar-storage-engine)                                                      |
| ACID-compliant         | Yes                |                                                                                                                                               |
| Indexes                | Unnecessary        | [Extent Elimination](mariadb-enterprise-columnstore-query-evaluation.md#extent-elimination)                                                   |
| Compression            | Yes                | [Compression](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression)  |
| High Availability (HA) | Yes                | [High Availability and Failover](columnstore-architectural-overview.md#high-availability-and-failover)                                        |
| Main Memory Caching    | Yes                |                                                                                                                                               |
| Transaction Logging    | Yes                | [Version Buffer](columnstore-storage-architecture.md#version-buffer)                                                                          |
| Garbage Collection     | Yes                | [ersion Buffer](columnstore-storage-architecture.md#version-buffer)                                                                           |
| Online Schema changes  | Yes                | [Online Schema Changes](mariadb-enterprise-columnstore-locking.md#online-schema-changes)                                                      |
| Non-locking Reads      | Yes                | [Lockless Reads](mariadb-enterprise-columnstore-locking.md#lockless-reads)                                                                    |

## Examples

### Creating a ColumnStore Table

To create a ColumnStore table, use the [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statement with the `ENGINE=ColumnStore` option:

```sql
CREATE DATABASE columnstore_db;

CREATE TABLE columnstore_db.analytics_test (
   id INT,
   str VARCHAR(50)
) ENGINE = ColumnStore;
```

### Multi-Node Configuration

To deploy a multi-node Enterprise ColumnStore deployment, a configuration similar to below is required:

```ini
[mariadb]
log_error                              = mariadbd.err
character_set_server                   = utf8
collation_server                       = utf8_general_ci
log_bin                                = mariadb-bin
log_bin_index                          = mariadb-bin.index
relay_log                              = mariadb-relay
relay_log_index                        = mariadb-relay.index
log_slave_updates                      = ON
gtid_strict_mode                       = ON

# This must be unique on each cluster node
server_id                              = 1
```

### Configure the Mandatory Utility User Account

To configure the mandatory utility user account, use the `mcsSetConfig` command:

```bash
sudo mcsSetConfig CrossEngineSupport Host 127.0.0.1
sudo mcsSetConfig CrossEngineSupport Port 3306
sudo mcsSetConfig CrossEngineSupport User cross_engine
sudo mcsSetConfig CrossEngineSupport Password cross_engine_passwd
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
