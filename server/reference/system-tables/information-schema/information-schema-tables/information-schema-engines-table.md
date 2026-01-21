---
description: >-
  The Information Schema ENGINES table displays status information about the
  server's storage engines, including support level and transaction
  capabilities.
---

# Information Schema ENGINES Table

The [Information Schema](../) `ENGINES` table displays status information about the server's [storage engines](../../../../server-usage/storage-engines/).

It contains the following columns:

| Column       | Description                                                                                                    |
| ------------ | -------------------------------------------------------------------------------------------------------------- |
| ENGINE       | Name of the storage engine.                                                                                    |
| SUPPORT      | Whether the engine is the default, or is supported or not.                                                     |
| COMMENT      | Storage engine comments.                                                                                       |
| TRANSACTIONS | Whether or not the engine supports [transactions](../../../sql-statements/transactions/).                      |
| XA           | Whether or not the engine supports [XA transactions](../../../sql-statements/transactions/xa-transactions.md). |
| SAVEPOINTS   | Whether or not [savepoints](../../../sql-statements/transactions/savepoint.md) are supported.                  |

It provides identical information to the [SHOW ENGINES](../../../sql-statements/administrative-sql-statements/show/show-engines.md) statement. Since storage engines are plugins, different information about them is also shown in the [information\_schema.PLUGINS](plugins-table-information-schema.md) table and by the [SHOW PLUGINS](../../../sql-statements/administrative-sql-statements/show/show-plugins.md) statement.

The table is not a standard Information Schema table, and is a MySQL and MariaDB extension.

Note that both MySQL's InnoDB and Percona's XtraDB replacement are labeled as `InnoDB`. However, if XtraDB is in use, it will be specified in the `COMMENT` field. See [XtraDB and InnoDB](../../../../server-usage/storage-engines/innodb/). The same applies to [FederatedX](../../../../server-usage/storage-engines/federatedx-storage-engine/).

## Example

```sql
SELECT * FROM information_schema.ENGINES\G;
*************************** 1. row ***************************
      ENGINE: InnoDB
     SUPPORT: DEFAULT
     COMMENT: Supports transactions, row-level locking, and foreign keys
TRANSACTIONS: YES
          XA: YES
  SAVEPOINTS: YES
*************************** 2. row ***************************
      ENGINE: CSV
     SUPPORT: YES
     COMMENT: CSV storage engine
TRANSACTIONS: NO
          XA: NO
  SAVEPOINTS: NO
*************************** 3. row ***************************
      ENGINE: MyISAM
     SUPPORT: YES
     COMMENT: MyISAM storage engine
TRANSACTIONS: NO
          XA: NO
  SAVEPOINTS: NO
*************************** 4. row ***************************
      ENGINE: BLACKHOLE
     SUPPORT: YES
     COMMENT: /dev/null storage engine (anything you write to it disappears)
TRANSACTIONS: NO
          XA: NO
  SAVEPOINTS: NO
*************************** 5. row ***************************
      ENGINE: FEDERATED
     SUPPORT: YES
     COMMENT: FederatedX pluggable storage engine
TRANSACTIONS: YES
          XA: NO
  SAVEPOINTS: YES
*************************** 6. row ***************************
      ENGINE: MRG_MyISAM
     SUPPORT: YES
     COMMENT: Collection of identical MyISAM tables
TRANSACTIONS: NO
          XA: NO
  SAVEPOINTS: NO
*************************** 7. row ***************************
      ENGINE: ARCHIVE
     SUPPORT: YES
     COMMENT: Archive storage engine
TRANSACTIONS: NO
          XA: NO
  SAVEPOINTS: NO
*************************** 8. row ***************************
      ENGINE: MEMORY
     SUPPORT: YES
     COMMENT: Hash based, stored in memory, useful for temporary tables
TRANSACTIONS: NO
          XA: NO
  SAVEPOINTS: NO
*************************** 9. row ***************************
      ENGINE: PERFORMANCE_SCHEMA
     SUPPORT: YES
     COMMENT: Performance Schema
TRANSACTIONS: NO
          XA: NO
  SAVEPOINTS: NO
*************************** 10. row ***************************
      ENGINE: Aria
     SUPPORT: YES
     COMMENT: Crash-safe tables with MyISAM heritage
TRANSACTIONS: NO
          XA: NO
  SAVEPOINTS: NO
10 rows in set (0.00 sec)
```

Check if a given storage engine is available:

```sql
SELECT SUPPORT FROM information_schema.ENGINES WHERE ENGINE LIKE 'tokudb';
Empty SET
```

Check which storage engine supports XA transactions:

```sql
SELECT ENGINE FROM information_schema.ENGINES WHERE XA = 'YES';
+--------+
| ENGINE |
+--------+
| InnoDB |
+--------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
