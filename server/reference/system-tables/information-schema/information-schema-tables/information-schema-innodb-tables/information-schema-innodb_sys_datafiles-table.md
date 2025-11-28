---
description: >-
  The INNODB_SYS_DATAFILES table, now deprecated and removed, was intended to
  provide metadata for InnoDB tablespace paths.
---

# Information Schema INNODB\_SYS\_DATAFILES Table

{% hint style="info" %}
This table is deprecated and was removed in MariaDB 10.6.0.
{% endhint %}

The [Information Schema](../../) `INNODB_SYS_DATAFILES` table contains information about InnoDB datafile paths. It was intended to provide metadata for tablespaces inside InnoDB tables, which was never implemented in MariaDB and was removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) was required to view the table.

It contains the following columns:

| Column | Description                                                                                                       |
| ------ | ----------------------------------------------------------------------------------------------------------------- |
| SPACE  | Numeric tablespace. Matches the [INNODB\_SYS\_TABLES.SPACE](information-schema-innodb_sys_tables-table.md) value. |
| PATH   | Tablespace datafile path.                                                                                         |

## Example

```sql
SELECT * FROM INNODB_SYS_DATAFILES;
+-------+--------------------------------+
| SPACE | PATH                           |
+-------+--------------------------------+
|    19 | ./test/t2.ibd                  |
|    20 | ./test/t3.ibd                  |
...
|    68 | ./test/animals.ibd             |
|    69 | ./test/animal_count.ibd        |
|    70 | ./test/t.ibd                   |
+-------+--------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
