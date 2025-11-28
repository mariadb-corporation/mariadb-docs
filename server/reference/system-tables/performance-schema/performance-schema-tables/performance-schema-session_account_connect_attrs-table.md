---
description: >-
  This table exposes connection attributes for the current session's account,
  providing metadata passed by the client application for identification.
---

# Performance Schema session\_account\_connect\_attrs Table

## Description

The `session_account_connect_attrs` table shows connection attributes for the current session.

Applications can pass key/value connection attributes to the server when a connection is made. The [session\_connect\_attrs](performance-schema-session_connect_attrs-table.md) and `session_account_connect_attrs` tables provide access to this information, for all sessions and the current session respectively.

The C API functions [mysql\_options()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_options) and [mysql\_optionsv()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_optionsv) are used for passing connection attributes to the server.

`session_account_connect_attrs` contains the following columns:

| Column            | Description                                                      |
| ----------------- | ---------------------------------------------------------------- |
| PROCESSLIST\_ID   | Session connection identifier.                                   |
| ATTR\_NAME        | Attribute name.                                                  |
| ATTR\_VALUE       | Attribute value.                                                 |
| ORDINAL\_POSITION | Order in which attribute was added to the connection attributes. |

## Example

```sql
SELECT * FROM performance_schema.session_account_connect_attrs;
+----------------+-----------------+------------------+------------------+
| PROCESSLIST_ID | ATTR_NAME       | ATTR_VALUE       | ORDINAL_POSITION |
+----------------+-----------------+------------------+------------------+
|             45 | _os             | debian-linux-gnu |                0 |
|             45 | _client_name    | libmysql         |                1 |
|             45 | _pid            | 7711             |                2 |
|             45 | _client_version | 10.0.5           |                3 |
|             45 | _platform       | x86_64           |                4 |
|             45 | program_name    | mysql            |                5 |
+----------------+-----------------+------------------+------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
