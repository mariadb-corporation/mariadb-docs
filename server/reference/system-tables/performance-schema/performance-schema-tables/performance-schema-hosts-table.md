---
description: >-
  The hosts table contains aggregated connection statistics for each client
  host, including counts for current and total historical connections.
---

# Performance Schema hosts Table

## Description

The `hosts` table contains a row for each host used by clients to connect to the server, containing current and total connections.

The size is determined by the [performance\_schema\_hosts\_size](../performance-schema-system-variables.md#performance_schema_hosts_size) system variable, which, if set to zero, will disable connection statistics in the hosts table.

It contains the following columns:

| Column               | Description                                                                                                      |
| -------------------- | ---------------------------------------------------------------------------------------------------------------- |
| HOST                 | Host name used by the client to connect, NULL for internal threads or user sessions that failed to authenticate. |
| CURRENT\_CONNECTIONS | Current number of the host's connections.                                                                        |
| TOTAL\_CONNECTIONS   | Total number of the host's connections                                                                           |

## Example

```sql
SELECT * FROM hosts;
+-----------+---------------------+-------------------+
| HOST      | CURRENT_CONNECTIONS | TOTAL_CONNECTIONS |
+-----------+---------------------+-------------------+
| localhost |                   1 |                45 |
| NULL      |                  20 |                23 |
+-----------+---------------------+-------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
