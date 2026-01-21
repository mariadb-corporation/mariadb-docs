---
description: >-
  Enable or disable binary logging for the current session. This statement
  allows administrators to perform operations without replicating them to
  replicas.
---

# SET SQL\_LOG\_BIN

## Syntax

```sql
SET [SESSION] sql_log_bin = {0|1}
```

## Description

Sets the [sql\_log\_bin](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#sql_log_bin) system variable, which disables or enables [binary logging](../../../../server-management/server-monitoring-logs/binary-log/) for the current connection, if the client has the `SUPER` [privilege](../../account-management-sql-statements/grant.md). The statement is refused with an error if the client does not have that privilege.

Note that setting `sql_log_bin=1` has no effect if [log\_bin](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin) variable, which enables global binary logging, is not set.

{% tabs %}
{% tab title="Current" %}
You cannot set `sql_log_bin` as a global variable.
{% endtab %}

{% tab title="< 5.6 / 5.5" %}
You can set `sql_log_bin` as a global variable. This is considered dangerous, though, as it can damage replication.
{% endtab %}
{% endtabs %}

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
