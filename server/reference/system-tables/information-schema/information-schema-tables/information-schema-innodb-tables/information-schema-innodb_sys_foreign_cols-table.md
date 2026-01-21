---
description: >-
  The INNODB_SYS_FOREIGN_COLS table maps columns to their respective foreign key
  constraints within the InnoDB storage engine.
---

# Information Schema INNODB\_SYS\_FOREIGN\_COLS Table

The [Information Schema](../../) `INNODB_SYS_FOREIGN_COLS` table contains information about InnoDB [foreign key](../../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md) columns.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID             | <p>Foreign key index associated with this column, matching the <a href="information-schema-innodb_sys_foreign-table.md">INNODB_SYS_FOREIGN.ID</a> field.</p><p>Prior to <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.1-rolling-releases/changes-and-improvements-in-mariadb-12.1">MariaDB 12.1</a>, this is preceded by the database name. From MariaDB 12.1, foreign key names are only required to be unique per table, not per database, so the redundant database name is not shown.</p> |
| FOR\_COL\_NAME | Child column name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| REF\_COL\_NAME | Parent column name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| POS            | Ordinal position of the column in the table, starting from 0.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

## Examples

Prior to MariaDB 12.1:

```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_FOREIGN_COLS\G
*************************** 1. row ***************************
          ID: test/fk_book_author
FOR_COL_NAME: author_id
REF_COL_NAME: id
         POS: 0
```

From MariaDB 12.1:

```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_SYS_FOREIGN_COLS\G
*************************** 1. row ***************************
          ID: fk_book_author
FOR_COL_NAME: author_id
REF_COL_NAME: id
         POS: 0
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
