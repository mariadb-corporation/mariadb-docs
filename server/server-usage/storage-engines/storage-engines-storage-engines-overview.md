---
description: >-
  An introduction to MariaDB's pluggable storage engine architecture,
  highlighting key engines like InnoDB, MyISAM, and Aria for different
  workloads.
---

# Storage Engines Overview

## Overview

MariaDB features pluggable storage engines to allow per-table workload optimization.

A storage engine is a type of [plugin](../../reference/plugins/) for MariaDB:

* Different storage engines may be optimized for different workloads, such as transactional workloads, analytical workloads, or high throughput workloads.
* Different storage engines may be designed for different use cases, such as federated table access, table sharding, and table archiving in the cloud.
* Different tables on the same server may use different storage engines.

| Engine                                                                    | Target          | Optimization         | Availability |
| ------------------------------------------------------------------------- | --------------- | -------------------- | ------------ |
| [Aria](aria/)                                                             | Read-Heavy      | Reads                | ES 10.5+     |
| [ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore) | Analytics, HTAP | Big Data, Analytical | ES 10.5+     |
| [InnoDB](innodb/)                                                         | General Purpose | Mixed Read/Write     | ES 10.5+     |
| [Memory](memory-storage-engine.md)                                        | Cache, Temp     | Temporary Data       | ES 10.5+     |
| [MyISAM](myisam-storage-engine/)                                          | Reads           | Reads                | ES 10.5+     |
| [MyRocks](myrocks/)                                                       | Write-Heavy     | I/O Reduction, SSD   | ES 10.5+     |
| [S3](s3-storage-engine/)                                                  | Cloud           | Read-Only            | ES 10.5+     |
| [Spider](spider/)                                                         | Federation      | Sharding, Interlink  | ES 10.5+     |

## Examples

### Identify the Default Storage Engine

Identify the server's global default storage engine by using [SHOW GLOBAL VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) to query the [default\_storage\_engine](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) system variable:

```sql
SHOW GLOBAL VARIABLES LIKE 'default_storage_engine';
```

```sql
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

Identify the session's default storage engine by using [SHOW SESSION VARIABLES](../../reference/sql-statements/administrative-sql-statements/show/show-variables.md):

```
SHOW SESSION VARIABLES LIKE 'default_storage_engine';
```

```sql
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

### Set the Default Storage Engine

Global default storage engine:

```sql
SET GLOBAL default_storage_engine='MyRocks';
```

Session default storage engine supersedes global default during this session:

```sql
SET SESSION default_storage_engine='MyRocks';
```

### Configure the Default Storage Engine

```bash
[mariadb]
...
default_storage_engine=MyRocks
```

### Identify Available Storage Engines

```sql
SHOW ENGINES;
```

### Choose Storage Engine for a New Table

Storage engine is specified at time of table creation using a ENGINE = parameter.

```sql
CREATE TABLE accounts.messages (
  id INT PRIMARY KEY AUTO_INCREMENT,
  sender_id INT,
  receiver_id INT,
  message TEXT
) ENGINE = MyRocks;
```

## Resources

### Engines for System Tables

Standard MariaDB storage engines are used for System Table storage:

* [Aria Storage Engine](aria/)
* [MyISAM Storage Engine](myisam-storage-engine/)

## FAQ

### Can I use more than one storage engine on a server?

* Yes, different tables can use different storage engines on the same server.
* To create a table with a specific storage engine, specify the ENGINE table option to the [CREATE TABLE](../../reference/sql-statements/data-definition/create/create-table.md) statement.

### Can I use more than one storage engine in a single query?

* Yes, a single query can reference tables that use multiple storage engines.
* In some cases, special configuration may be required. For example, ColumnStore requires cross engine joins to be configured.

### What storage engine should I use for transactional or OLTP workloads?

* [InnoDB](innodb/) is the recommended storage engine for transactional or OLTP workloads.

### What storage engine should I use for analytical or OLAP workloads?

* [ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore) is the recommended storage engine for analytical or OLAP workloads.

### What storage engine should I use if my application performs both transactional and analytical queries?

An application that performs both transactional and analytical queries is known as [hybrid transactional-analytical processing (HTAP)](https://mariadb.com/kb/en/deploy-htap-topology/).

HTAP can be implemented with MariaDB by using [InnoDB](innodb/) for transactional queries and [ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore) for analytical queries.

## Reference

### MariaDB Server Reference

* [Plugins](../../reference/plugins/).
* [Information Schema ENGINES table](../../reference/system-tables/information-schema/information-schema-tables/information-schema-engines-table.md), which shows available storage engines.
* [Information Schema TABLES table](../../reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md), which shows storage engine by table.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
