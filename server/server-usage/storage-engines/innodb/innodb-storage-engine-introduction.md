---
description: >-
  An overview of the InnoDB storage engine, detailing its support for ACID
  transactions, row-level locking, and crash recovery.
---

# InnoDB Introduction

## Overview

MariaDB Enterprise Server uses the InnoDB storage engine by default. InnoDB is a general purpose transactional storage engine that is performant, ACID-compliant, and well-suited for most workloads.

## Benefits

The InnoDB storage engine:

* Is available with all versions of [MariaDB Enterprise Server](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/mariadb-enterprise-server-differences) and MariaDB Community Server.
* Is a general purpose storage engine.
* Is transactional and well-suited for online transactional processing (OLTP) workloads.
* Is ACID-compliant.
* Performs well for mixed read-write workloads.
* Supports online DDL.

## Feature Summary

| Feature                 | Detail                 | Resources                                                                                                                                                                                |
| ----------------------- | ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Storage Engine          | InnoDB                 |                                                                                                                                                                                          |
| Availability            | All ES and CS versions | [MariaDB Enterprise Server](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/JqgUabdZsoY5EiaJmqgn/)                                                                                      |
| Workload Optimization   | Transactional          |                                                                                                                                                                                          |
| Table Orientation       | Row                    |                                                                                                                                                                                          |
| Default Row Format      | Dynamic                | [InnoDB Row Formats](innodb-row-formats/) [InnoDB Dynamic Row Format](innodb-row-formats/innodb-dynamic-row-format.md)                                                                   |
| ACID-compliant          | Yes                    |                                                                                                                                                                                          |
| XA Transactions         | Yes                    |                                                                                                                                                                                          |
| Primary Keys            | Yes                    | InnoDB Primary Keys                                                                                                                                                                      |
| Auto-Increment          | Yes                    | [InnoDB AUTO\_INCREMENT Columns](auto_increment-handling-in-innodb.md)                                                                                                                   |
| Sequences               | Yes                    | InnoDB Sequences                                                                                                                                                                         |
| Foreign Keys            | Yes                    | InnoDB [Foreign Keys](innodb-storage-engine-introduction.md#foreign-key-constraints)                                                                                                     |
| Indexes                 | Yes                    | InnoDB Indexes                                                                                                                                                                           |
| Secondary Indexes       | Yes                    | InnoDB Secondary Indexes                                                                                                                                                                 |
| Unique Indexes          | Yes                    | InnoDB Unique Indexes                                                                                                                                                                    |
| Full-text Search        | Yes                    | InnoDB Full-text Indexes                                                                                                                                                                 |
| Spatial Indexes         | Yes                    | InnoDB Spatial Indexes                                                                                                                                                                   |
| Compression             | Yes                    | [Configure InnoDB Page Compression](innodb-page-compression.md)                                                                                                                          |
| Data-at-Rest Encryption | Yes                    |                                                                                                                                                                                          |
| High Availability (HA)  | Yes                    | • [MariaDB Replication](../../../ha-and-performance/standard-replication/) • [Galera Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide)  |
| Main Memory Caching     | Yes                    | [InnoDB Buffer Pool](innodb-buffer-pool.md)                                                                                                                                              |
| Transaction Logging     | Yes                    | • [InnoDB Redo Log (Crash Safety)](mariadb-enterprise-server-innodb-operations/configure-the-innodb-redo-log.md) • [InnoDB Undo Log (MVCC)](innodb-system-variables.md#innodb_undo_logs) |
| Garbage Collection      | Yes                    | [InnoDB Purge Threads](innodb-system-variables.md#innodb_purge_threads)                                                                                                                  |
| Online Schema changes   | Yes                    | [InnoDB Schema Changes](mariadb-enterprise-server-innodb-operations/schema-changes/)                                                                                                     |
| Non-locking Reads       | Yes                    |                                                                                                                                                                                          |
| Row Locking             | Yes                    |                                                                                                                                                                                          |

## Examples

### Creating an InnoDB Table

```sql
CREATE DATABASE hq_sales;
```

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
) ENGINE = InnoDB;
```

```sql
SELECT TABLE_SCHEMA, TABLE_NAME, ENGINE
FROM information_schema.TABLES
WHERE TABLE_SCHEMA='hq_sales'
AND TABLE_NAME='invoices';
+--------------+------------+--------+
| TABLE_SCHEMA | TABLE_NAME | ENGINE |
+--------------+------------+--------+
| hq_sales     | invoices   | InnoDB |
+--------------+------------+--------+
```

## Resources

### Architecture

* Background Thread Pool
* [Buffer Pool](innodb-buffer-pool.md)
* [I/O Threads](mariadb-enterprise-server-innodb-operations/configure-the-innodb-io-threads.md)
* [Purge Threads](innodb-purge.md)
* [Redo Log](innodb-redo-log.md)
* [Row Formats](innodb-row-formats/)
* [Undo Log](innodb-undo-log.md)

### Operations

* [Configure Page Compression](innodb-page-compression.md)
* [Configure the Buffer Pool](mariadb-enterprise-server-innodb-operations/configure-the-innodb-buffer-pool.md)
* [Configure the I/O Threads](mariadb-enterprise-server-innodb-operations/configure-the-innodb-io-threads.md)
* [Configure the Purge Threads](mariadb-enterprise-server-innodb-operations/configure-the-innodb-purge-threads.md)
* [Configure the Redo Log](mariadb-enterprise-server-innodb-operations/configure-the-innodb-redo-log.md)
* [Configure the Undo Log](mariadb-enterprise-server-innodb-operations/configure-the-innodb-undo-log.md)
* [Schema Changes](mariadb-enterprise-server-innodb-operations/schema-changes/)

## MariaDB documentation

* [InnoDB](./)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
