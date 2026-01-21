---
description: >-
  List the binary log files on the server. View the file names and sizes to
  monitor replication logs and manage disk usage.
---

# SHOW BINARY LOGS

## Syntax

```sql
SHOW BINARY LOGS
SHOW MASTER LOGS
```

## Description

Lists the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) files on the server. This statement is used as part of the procedure described in [PURGE BINARY LOGS](../purge-binary-logs.md), that shows how to determine which logs can be purged.

{% tabs %}
{% tab title="Current" %}
This statement requires the [BINLOG MONITOR](../../account-management-sql-statements/grant.md#binlog-monitor) privilege.
{% endtab %}

{% tab title="< 10.5.2" %}
This statement requires the [SUPER](../../account-management-sql-statements/grant.md#super) privilege and the [REPLICATION\_CLIENT](../../account-management-sql-statements/grant.md#replication-client) privilege.
{% endtab %}
{% endtabs %}

## Examples

```sql
SHOW BINARY LOGS;
+--------------------+-----------+
| Log_name           | File_size |
+--------------------+-----------+
| mariadb-bin.000001 |     19039 |
| mariadb-bin.000002 |    717389 |
| mariadb-bin.000003 |       300 |
| mariadb-bin.000004 |       333 |
| mariadb-bin.000005 |       899 |
| mariadb-bin.000006 |       125 |
| mariadb-bin.000007 |     18907 |
| mariadb-bin.000008 |     19530 |
| mariadb-bin.000009 |       151 |
| mariadb-bin.000010 |       151 |
| mariadb-bin.000011 |       125 |
| mariadb-bin.000012 |       151 |
| mariadb-bin.000013 |       151 |
| mariadb-bin.000014 |       125 |
| mariadb-bin.000015 |       151 |
| mariadb-bin.000016 |       314 |
+--------------------+-----------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
