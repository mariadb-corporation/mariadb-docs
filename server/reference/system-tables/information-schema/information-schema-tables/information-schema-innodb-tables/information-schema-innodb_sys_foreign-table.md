---
description: >-
  The INNODB_SYS_FOREIGN table provides metadata about foreign key constraints
  defined on InnoDB tables, including reference details.
---

# Information Schema INNODB\_SYS\_FOREIGN Table

The [Information Schema](../../) `INNODB_SYS_FOREIGN` table contains information about InnoDB [foreign keys](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md).

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column    | Description                                                                                                                                                                                                                                                                                                                                                                           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID        | Foreign key name. Prior to [MariaDB 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1), this is preceded by the database name. From MariaDB 12.1, foreign key names are only required to be unique per table, not per database, so the redundant database name is not shown. |
| FOR\_NAME | Database and table name of the foreign key child.                                                                                                                                                                                                                                                                                                                                     |
| REF\_NAME | Database and table name of the foreign key parent.                                                                                                                                                                                                                                                                                                                                    |
| N\_COLS   | Number of foreign key index columns.                                                                                                                                                                                                                                                                                                                                                  |
| TYPE      | Bit flag providing information about the foreign key.                                                                                                                                                                                                                                                                                                                                 |

The `TYPE` column provides a bit flag with information about the foreign key. This information is `OR`'ed together to read:

| Bit Flag | Description         |
| -------- | ------------------- |
| 1        | ON DELETE CASCADE   |
| 2        | ON UPDATE SET NULL  |
| 4        | ON UPDATE CASCADE   |
| 8        | ON UPDATE SET NULL  |
| 16       | ON DELETE NO ACTION |
| 32       | ON UPDATE NO ACTION |

## Example

Prior to [MariaDB 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1):

```sql
ELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_FOREIGN\G
*************************** 1. row ***************************
      ID: test/fk_book_author
FOR_NAME: test/book
REF_NAME: test/author
  N_COLS: 1
    TYPE: 1
...
```

From MariaDB 12.1:

```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_FOREIGN\G
*************************** 1. row ***************************
      ID: fk_book_author
FOR_NAME: test/book
REF_NAME: test/author
  N_COLS: 1
    TYPE: 1
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
