---
description: >-
  View server status variables. This statement displays counters and metrics for
  server activity, performance, and health.
---

# SHOW STATUS

## Syntax

```sql
SHOW [GLOBAL | SESSION] STATUS
    [LIKE 'pattern' | WHERE expr]
```

## Description

`SHOW STATUS` provides server status information. This information also can be obtained using the [mariadb-admin extended-status](../../../../clients-and-utilities/administrative-tools/mariadb-admin.md) command, or by querying the [Information Schema GLOBAL\_STATUS and SESSION\_STATUS](../../../system-tables/information-schema/information-schema-tables/information-schema-global_status-and-session_status-tables.md) tables. The `LIKE` clause, if present, indicates which variable names to match. The `WHERE` clause can be given to select rows using more general conditions.

With the `GLOBAL` modifier, `SHOW STATUS` displays the status values for all connections to MariaDB. With`SESSION`, it displays the status values for the current connection. If no modifier is present, the default is`SESSION`. `LOCAL` is a synonym for`SESSION`. If you see a lot of 0 values, the reason is probably that you have used `SHOW STATUS` with a new connection instead of `SHOW GLOBAL STATUS`.

Some status variables have only a global value. For these, you get the same value for both `GLOBAL` and `SESSION`.

See [Server Status Variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md) for a full list, scope and description of the variables that can be viewed with `SHOW STATUS`.

The `LIKE` clause, if present on its own, indicates which variable name to match.

The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

## Examples

```sql
SHOW GLOBAL STATUS;
+--------------------------------------------------------------+----------------------------------------+
| Variable_name                                                | Value                                  |
+--------------------------------------------------------------+----------------------------------------+
| Aborted_clients                                              | 0                                      |
| Aborted_connects                                             | 0                                      |
| Access_denied_errors                                         | 0                                      |
| Acl_column_grants                                            | 0                                      |
| Acl_database_grants                                          | 2                                      |
| Acl_function_grants                                          | 0                                      |
| Acl_procedure_grants                                         | 0                                      |
| Acl_proxy_users                                              | 2                                      |
| Acl_role_grants                                              | 0                                      |
| Acl_roles                                                    | 0                                      |
| Acl_table_grants                                             | 0                                      |
| Acl_users                                                    | 6                                      |
| Aria_pagecache_blocks_not_flushed                            | 0                                      |
| Aria_pagecache_blocks_unused                                 | 15706                                  |
...
| wsrep_local_index                                            | 18446744073709551615                   |
| wsrep_provider_name                                          |                                        |
| wsrep_provider_vendor                                        |                                        |
| wsrep_provider_version                                       |                                        |
| wsrep_ready                                                  | OFF                                    |
| wsrep_thread_count                                           | 0                                      |
+--------------------------------------------------------------+----------------------------------------+
516 rows in set (0.00 sec)
```

Example of filtered output:

```sql
SHOW STATUS LIKE 'Key%';
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| Key_blocks_not_flushed | 0      |
| Key_blocks_unused      | 107163 |
| Key_blocks_used        | 0      |
| Key_blocks_warm        | 0      |
| Key_read_requests      | 0      |
| Key_reads              | 0      |
| Key_write_requests     | 0      |
| Key_writes             | 0      |
+------------------------+--------+
8 rows in set (0.00 sec)
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
