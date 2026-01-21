---
description: >-
  The INNODB_SYS_TABLESTATS table offers low-level performance statistics for
  InnoDB tables, such as row counts and modification counters.
---

# Information Schema INNODB\_SYS\_TABLESTATS Table

The [Information Schema](../../) `INNODB_SYS_TABLESTATS` table contains InnoDB status information. It can be used for developing new performance-related extensions, or high-level performance monitoring.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

Note that the MySQL InnoDB and Percona XtraDB versions of the tables differ (see [XtraDB and InnoDB](../../../../../server-usage/storage-engines/innodb/)).

It contains the following columns:

| Column                 | Description                                                                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TABLE\_ID              | Table ID, matching the [INNODB\_SYS\_TABLES.TABLE\_ID](information-schema-innodb_sys_tables-table.md) value.                                               |
| SCHEMA                 | Database name (XtraDB only).                                                                                                                               |
| NAME                   | Table name, matching the [INNODB\_SYS\_TABLES.NAME](information-schema-innodb_sys_tables-table.md) value.                                                  |
| STATS\_INITIALIZED     | Initialized if statistics have already been collected, otherwise Uninitialized.                                                                            |
| NUM\_ROWS              | Estimated number of rows currently in the table. Updated after each statement modifying the data, but uncommited transactions mean it may not be accurate. |
| CLUST\_INDEX\_SIZE     | Number of pages on disk storing the clustered index, holding InnoDB table data in primary key order, or NULL if not statistics yet collected.              |
| OTHER\_INDEX\_SIZE     | Number of pages on disk storing secondary indexes for the table, or NULL if not statistics yet collected.                                                  |
| MODIFIED\_COUNTER      | Number of rows modified by statements modifying data.                                                                                                      |
| AUTOINC                | [Auto\_increment](../../../../data-types/auto_increment.md) value.                                                                                         |
| REF\_COUNT             | Countdown to zero, when table metadata can be removed from the table cache. (InnoDB only)                                                                  |
| MYSQL\_HANDLES\_OPENED | (XtraDB only).                                                                                                                                             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
