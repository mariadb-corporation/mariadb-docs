---
description: >-
  The Information Schema INDEX_STATISTICS table provides statistics on index
  usage, helping to identify unused indexes and optimize performance.
---

# Information Schema INDEX\_STATISTICS Table

The [Information Schema](../) `INDEX_STATISTICS` table shows statistics on index usage and makes it possible to do such things as locating unused indexes and generating the commands to remove them.

This is part of the [User Statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics.md) feature, which is not enabled by default.

It contains the following columns:

| Field         | Type         | Notes                                                                                                                                                                                                                                                                  |
| ------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TABLE\_SCHEMA | VARCHAR(192) | The schema (database) name.                                                                                                                                                                                                                                            |
| TABLE\_NAME   | VARCHAR(192) | The table name.                                                                                                                                                                                                                                                        |
| INDEX\_NAME   | VARCHAR(192) | The index name (as visible in [SHOW CREATE TABLE](../../../sql-statements/administrative-sql-statements/show/show-create-table.md)).                                                                                                                                   |
| ROWS\_READ    | BIGINT(21)   | The number of rows read from this index.                                                                                                                                                                                                                               |
| QUERIES       | BIGINT(21)   | Incremented for each index the query is part of. This assists one to see how effective the index is. From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115) |

## Example

```sql
SELECT * FROM information_schema.INDEX_STATISTICS 
WHERE TABLE_NAME = "author";
+--------------+------------+------------+-----------+
| TABLE_SCHEMA | TABLE_NAME | INDEX_NAME | ROWS_READ |
+--------------+------------+------------+-----------+
| books        | author     | by_name    |        15 |
+--------------+------------+------------+-----------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
