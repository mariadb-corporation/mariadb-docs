---
description: >-
  Return the connection ID. This function retrieves the unique thread identifier
  for the current client connection.
---

# CONNECTION\_ID

## Syntax

```sql
CONNECTION_ID()
```

## Description

Returns the connection ID for the connection. Every connection (including events) has an ID that is unique among the set of currently connected clients.

Returns `MYSQL_TYPE_LONG`, or int(10).

## Examples

```sql
SELECT CONNECTION_ID();
+-----------------+
| CONNECTION_ID() |
+-----------------+
|               3 |
+-----------------+
```

## See Also

* [SHOW PROCESSLIST](../../../sql-statements/administrative-sql-statements/show/show-processlist.md)
* [INFORMATION\_SCHEMA.PROCESSLIST](../../../system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
