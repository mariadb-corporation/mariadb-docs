---
description: >-
  The TEMP_TABLES_INFO table lists active InnoDB temporary tables, including
  their column counts and tablespace identifiers.
---

# Information Schema TEMP\_TABLES\_INFO Table

{% hint style="info" %}
This table was removed and is no longer a part of MariaDB. See [MDEV-12459](https://jira.mariadb.org/browse/MDEV-12459) for an alternative.
{% endhint %}

The [Information Schema](../../) `TEMP_TABLES_INFO` table contains information about active InnoDB temporary tables. All user and system-created temporary tables are reported when querying this table, with the exception of optimized internal temporary tables. The data is stored in memory.

Previously, InnoDB temp table metadata was rather stored in InnoDB system tables.

It has the following columns:

| Column                 | Description                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TABLE\_ID              | Table ID.                                                                                                                                                                                                                                                                                                                                                            |
| NAME                   | Table name.                                                                                                                                                                                                                                                                                                                                                          |
| N\_COLS                | Number of columns in the temporary table, including three hidden columns that InnoDB creates (DB\_ROW\_ID, DB\_TRX\_ID, and DB\_ROLL\_PTR).                                                                                                                                                                                                                          |
| SPACE                  | Numerical identifier for the tablespace identifier holding the temporary table. Compressed temporary tables are stored by default in separate per-table tablespaces in the temporary file directory. For non-compressed tables, the shared temporary table is named ibtmp1, found in the data directory. Always a non-zero value, and regenerated on server restart. |
| PER\_TABLE\_TABLESPACE | If TRUE, the temporary table resides in a separate per-table tablespace. If FALSE, it resides in the shared temporary tablespace.                                                                                                                                                                                                                                    |
| IS\_COMPRESSED         | TRUE if the table is compressed.                                                                                                                                                                                                                                                                                                                                     |

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

## Examples

```sql
CREATE TEMPORARY TABLE t (i INT) ENGINE=INNODB;

SELECT * FROM INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO;
+----------+--------------+--------+-------+----------------------+---------------+
| TABLE_ID | NAME         | N_COLS | SPACE | PER_TABLE_TABLESPACE | IS_COMPRESSED |
+----------+--------------+--------+-------+----------------------+---------------+
|       39 | #sql1c93_3_1 |      4 |    64 | FALSE                | FALSE         |
+----------+--------------+--------+-------+----------------------+---------------+
```

Adding a compressed table:

```sql
SET GLOBAL innodb_file_format="Barracuda";

CREATE TEMPORARY TABLE t2 (i INT) ROW_FORMAT=COMPRESSED ENGINE=INNODB;

SELECT * FROM INFORMATION_SCHEMA.INNODB_TEMP_TABLE_INFO;
+----------+--------------+--------+-------+----------------------+---------------+
| TABLE_ID | NAME         | N_COLS | SPACE | PER_TABLE_TABLESPACE | IS_COMPRESSED |
+----------+--------------+--------+-------+----------------------+---------------+
|       40 | #sql1c93_3_3 |      4 |    65 | TRUE                 | TRUE          |
|       39 | #sql1c93_3_1 |      4 |    64 | FALSE                | FALSE         |
+----------+--------------+--------+-------+----------------------+---------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
