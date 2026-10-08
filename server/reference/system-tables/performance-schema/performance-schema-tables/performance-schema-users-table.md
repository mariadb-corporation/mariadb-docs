---
description: >-
  The users table tracks connection statistics aggregated by user name,
  including current active connections and total historical connections.
---

# Performance Schema users Table

## Description

Each user that connects to the server is stored as a row in the `users` table, along with current and total connections.

The table size is determined at startup by the value of the [performance\_schema\_users\_size](../performance-schema-system-variables.md#performance_schema_users_size) system variable. If this is set to `0`, user statistics will be disabled.

| Column               | Description                                                                          |
| -------------------- | ------------------------------------------------------------------------------------ |
| USER                 | The connection's client user name for the connection, or NULL if an internal thread. |
| CURRENT\_CONNECTIONS | Current connections for the user.                                                    |
| TOTAL\_CONNECTIONS   | Total connections for the user.                                                      |

## Example

```sql
SELECT * FROM performance_schema.users;
+------------------+---------------------+-------------------+
| USER             | CURRENT_CONNECTIONS | TOTAL_CONNECTIONS |
+------------------+---------------------+-------------------+
| debian-sys-maint |                   0 |                35 |
| NULL             |                  20 |                23 |
| root             |                   1 |                 2 |
+------------------+---------------------+-------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
