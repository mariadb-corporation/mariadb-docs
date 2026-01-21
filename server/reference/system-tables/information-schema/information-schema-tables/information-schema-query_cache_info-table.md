---
description: >-
  The Information Schema QUERY_CACHE_INFO table shows all queries currently
  stored in the query cache, aiding in cache performance analysis.
---

# Information Schema QUERY\_CACHE\_INFO Table

## Description

{% hint style="info" %}
This table is not a standard Information Schema table, but a MariaDB extension.
{% endhint %}

The `QUERY_CACHE_INFO` table is created by the [QUERY\_CACHE\_INFO](../../../plugins/other-plugins/query-cache-information-plugin.md) plugin, and allows you to see the contents of the [query cache](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache.md). It creates a table in the [information\_schema](../) database that shows all queries that are in the cache. You must have the `PROCESS` privilege (see [GRANT](../../../sql-statements/account-management-sql-statements/grant.md)) to use this table.

It contains the following columns:

| Column                     | Description                                   |
| -------------------------- | --------------------------------------------- |
| STATEMENT\_SCHEMA          | Database used when query was included         |
| STATEMENT\_TEXT            | Query text                                    |
| RESULT\_BLOCKS\_COUNT      | Number of result blocks                       |
| RESULT\_BLOCKS\_SIZE       | Size in bytes of result blocks                |
| RESULT\_BLOCKS\_SIZE\_USED | Size in bytes of used blocks                  |
| LIMIT                      |                                               |
| MAX\_SORT\_LENGTH          |                                               |
| GROUP\_CONCAT\_MAX\_LENGTH |                                               |
| CHARACTER\_SET\_CLIENT     |                                               |
| CHARACTER\_SET\_RESULT     |                                               |
| COLLATION                  |                                               |
| TIMEZONE                   |                                               |
| DEFAULT\_WEEK\_FORMAT      |                                               |
| DIV\_PRECISION\_INCREMENT  |                                               |
| SQL\_MODE                  |                                               |
| LC\_TIME\_NAMES            |                                               |
| CLIENT\_LONG\_FLAG         |                                               |
| CLIENT\_PROTOCOL\_41       |                                               |
| PROTOCOL\_TYPE             |                                               |
| MORE\_RESULTS\_EXISTS      |                                               |
| IN\_TRANS                  |                                               |
| AUTOCOMMIT                 |                                               |
| PACKET\_NUMBER             |                                               |
| HITS                       | Incremented each time the query cache is hit. |

For example:

```sql
SELECT * FROM information_schema.QUERY_CACHE_INFO;
+------------------+-----------------+---------------------+--------------------+-------------------------+
| STATEMENT_SCHEMA | STATEMENT_TEXT  | RESULT_BLOCKS_COUNT | RESULT_BLOCKS_SIZE | RESULT_BLOCKS_SIZE_USED |
+------------------+-----------------+---------------------+--------------------+-------------------------+
...
| test             | SELECT * FROM a |                   1 |                512 |                     143 |
| test             | select * FROM a |                   1 |                512 |                     143 |
...
+------------------+-----------------+---------------------+--------------------+-------------------------
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
