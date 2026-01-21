---
description: >-
  The mysql.transaction_registry table is used by system-versioned tables to
  track transaction IDs and their commit timestamps.
---

# mysql.transaction\_registry Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.transaction_registry` table is part of [system-versioned tables](../../sql-structure/temporal-tables/system-versioned-tables.md). It is used for [transaction-precise versioning](../../sql-structure/temporal-tables/system-versioned-tables.md#transaction-precise-history-in-innodb), and contains the following fields:

| Field            | Type                                                                       | Null | Key      | Default                    | Description                                                                                                                   |
| ---------------- | -------------------------------------------------------------------------- | ---- | -------- | -------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| transaction\_id  | bigint(20) unsigned                                                        | NO   | Primary  | NULL                       |                                                                                                                               |
| commit\_id       | bigint(20) unsigned                                                        | NO   | Unique   | NULL                       |                                                                                                                               |
| begin\_timestamp | timestamp(6)                                                               | NO   | Multiple | 0000-00-00 00:00:00.000000 | Timestamp when the transaction began (BEGIN statement), however see [MDEV-16024](https://jira.mariadb.org/browse/MDEV-16024). |
| commit           | timestamp(6)                                                               | NO   | Multiple | 0000-00-00 00:00:00.000000 | Timestamp when the transaction was committed.                                                                                 |
| isolation\_level | enum('READ-UNCOMMITTED','READ-COMMITTED','REPEATABLE-READ','SERIALIZABLE') | NO   |          | NULL                       | Transaction [isolation level](../../sql-statements/transactions/set-transaction.md#isolation-levels).                         |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
