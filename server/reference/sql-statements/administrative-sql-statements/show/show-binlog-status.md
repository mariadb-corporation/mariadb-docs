---
description: >-
  View the current status of the primary server's binary log. This statement
  returns the current log file name and position for replication
  synchronization.
---

# SHOW MASTER STATUS

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
SHOW [MASTER | BINLOG] STATUS
```
{% endtab %}

{% tab title="< 10.5.2" %}
```sql
SHOW MASTER STATUS
```
{% endtab %}
{% endtabs %}

## Description

Provides status information about the [binary log](../../../../server-management/server-monitoring-logs/binary-log/) files of the primary.

{% tabs %}
{% tab title="Current" %}
This statement requires the [BINLOG MONITOR](../../account-management-sql-statements/grant.md#binlog-monitor) privilege.
{% endtab %}

{% tab title="< 10.5.2" %}
This statement requires the [SUPER](../../account-management-sql-statements/grant.md#super) privilege and the [REPLICATION\_CLIENT](../../account-management-sql-statements/grant.md#replication-client) privilege.
{% endtab %}
{% endtabs %}

To see information about the current [GTIDs](../../../../ha-and-performance/standard-replication/gtid.md) in the binary log, use the [gtid\_binlog\_pos](../../../../ha-and-performance/standard-replication/gtid.md) variable.

## Example

```sql
SHOW BINLOG STATUS;
+--------------------+----------+--------------+------------------+
| File               | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+--------------------+----------+--------------+------------------+
| mariadb-bin.000016 |      475 |              |                  |
+--------------------+----------+--------------+------------------+
SELECT @@global.gtid_binlog_pos;
+--------------------------+
| @@global.gtid_binlog_pos |
+--------------------------+
| 0-1-2                    |
+--------------------------+
```

## See Also

* [MariaDB replication](../../../../ha-and-performance/standard-replication/)
* [Using and Maintaining the Binary Log](../../../../server-management/server-monitoring-logs/binary-log/using-and-maintaining-the-binary-log.md)
* [The gtid\_binlog\_pos variable](../../../../ha-and-performance/standard-replication/gtid.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
