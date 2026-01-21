---
description: >-
  The mysql.func table registers user-defined functions (UDFs), storing their
  names and the shared library files containing their code.
---

# mysql.func Table

The `mysql.func` table stores information about [user-defined functions](../../../server-usage/user-defined-functions/) (UDFs) created with the [CREATE FUNCTION UDF](../../../server-usage/user-defined-functions/create-function-udf.md) statement.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.func` table contains the following fields:

| Field | Type                         | Null | Key | Default | Description                                                                                                                                                                                                |
| ----- | ---------------------------- | ---- | --- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name  | char(64)                     | NO   | PRI |         | UDF name                                                                                                                                                                                                   |
| ret   | tinyint(1)                   | NO   |     | 0       |                                                                                                                                                                                                            |
| dl    | char(128)                    | NO   |     |         | Shared library name                                                                                                                                                                                        |
| type  | enum('function','aggregate') | NO   |     | NULL    | Type, either function or aggregate. Aggregate functions are summary functions such as [SUM()](../../sql-functions/aggregate-functions/sum.md) and [AVG()](../../sql-functions/aggregate-functions/avg.md). |

## Example

```sql
SELECT * FROM mysql.func;
+------------------------------+-----+--------------+-----------+
| name                         | ret | dl           | type      |
+------------------------------+-----+--------------+-----------+
| spider_direct_sql            |   2 | ha_spider.so | function  |
| spider_bg_direct_sql         |   2 | ha_spider.so | aggregate |
| spider_ping_table            |   2 | ha_spider.so | function  |
| spider_copy_tables           |   2 | ha_spider.so | function  |
| spider_flush_table_mon_cache |   2 | ha_spider.so | function  |
+------------------------------+-----+--------------+-----------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
