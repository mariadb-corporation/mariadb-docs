---
description: >-
  The Information Schema TABLE_STATISTICS table provides usage statistics for
  tables, such as the number of rows read or changed.
---

# Information Schema TABLE\_STATISTICS Table

The [Information Schema](../) `TABLE_STATISTICS` table shows statistics on table usage.

This is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.

It contains the following columns:

| Field                     | Type         | Notes                                                                                                                      |
| ------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------- |
| TABLE\_SCHEMA             | varchar(192) | The schema (database) name.                                                                                                |
| TABLE\_NAME               | varchar(192) | The table name.                                                                                                            |
| ROWS\_READ                | bigint(21)   | The number of rows read from the table.                                                                                    |
| ROWS\_CHANGED             | bigint(21)   | The number of rows changed in the table.                                                                                   |
| ROWS\_CHANGED\_X\_INDEXES | bigint(21)   | The number of rows changed in the table, multiplied by the number of indexes changed.                                      |
| ROWS\_INSERTED            | bigint(21)   | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115) |
| ROWS\_UPDATED             | bigint(21)   | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115) |
| ROWS\_DELETED             | bigint(21)   | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115) |
| KEY\_READ\_HITS           | bigint(21)   | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115) |
| KEY\_READ\_MISSES         | bigint(21)   | From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115) |

#### Example

```sql
SELECT * FROM INFORMATION_SCHEMA.TABLE_STATISTICS WHERE TABLE_NAME='user';
+--------------+------------+-----------+--------------+------------------------+
| TABLE_SCHEMA | TABLE_NAME | ROWS_READ | ROWS_CHANGED | ROWS_CHANGED_X_INDEXES |
+--------------+------------+-----------+--------------+------------------------+
| mysql        | user       |         5 |            2 |                      2 |
+--------------+------------+-----------+--------------+------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
