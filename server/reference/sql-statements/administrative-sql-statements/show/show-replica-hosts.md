---
description: >-
  List registered replicas. This statement displays information about replica
  servers connected to the current primary.
---

# SHOW REPLICA HOSTS

## Syntax

```sql
SHOW { REPLICA | SLAVE } HOSTS
```

## Description

This command is run on the primary and displays a list of replicas that are currently registered with it. The output looks like this:

```sql
SHOW REPLICA HOSTS;
+------------+-----------+------+-----------+
| Server_id  | Host      | Port | Master_id |
+------------+-----------+------+-----------+
|  192168010 | iconnect2 | 3306 | 192168011 |
| 1921680101 | athena    | 3306 | 192168011 |
+------------+-----------+------+-----------+
```

`Server_id`: The unique server ID of the replica server, as configured in the server's option file, or on the command line with [--server-id=value](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md).

{% tabs %}
{% tab title="Current" %}
`Host`: The host name of the replica server, as configured in the server's option file, or on the command line with `--report-host=host_name` (note that this can differ from the machine name as configured in the operating system). If a replica doesn't configure `--report-host` explicitly, the value for the `Host` column is automatically extracted using the network connection's host name or IP address.
{% endtab %}

{% tab title="< 10.5" %}
`Host`: The host name of the replica server, as configured in the server's option file, or on the command line with `--report-host=host_name` (note that this can differ from the machine name as configured in the operating system). If a replica doesn't configure `--report-host` explicitly, the value for the `Host` column is automatically extracted using the network connection's host name or IP address. The Host value is left blank if a replica's `--report-host` parameter is not configured.
{% endtab %}
{% endtabs %}

`Port`: The port the replica server is listening on.

`Master_id`: The unique server ID of the primary server that the replica server is replicating from.

{% tabs %}
{% tab title="Current" %}
Requires the [REPLICATION MASTER ADMIN](../../account-management-sql-statements/grant.md#replication-master-admin) privilege.
{% endtab %}

{% tab title="< 10.5.1" %}
Requires the [REPLICATION SLAVE](../../account-management-sql-statements/grant.md#replication-slave) privilege.
{% endtab %}
{% endtabs %}

### SHOW REPLICA HOSTS

{% tabs %}
{% tab title="Current" %}
`SHOW REPLICA HOSTS` is an alias for `SHOW SLAVE HOSTS` .
{% endtab %}

{% tab title="< 10.5.1" %}
`SHOW REPLICA HOSTS` is not available, use `SHOW SLAVE HOSTS` instead.
{% endtab %}
{% endtabs %}

## See Also

* [MariaDB replication](../../../../ha-and-performance/standard-replication/)
* [Replication threads](../../../../ha-and-performance/standard-replication/replication-threads.md)
* [SHOW PROCESSLIST](show-processlist.md). In [SHOW PROCESSLIST](show-processlist.md) output, replica threads are identified by `Binlog Dump`

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
