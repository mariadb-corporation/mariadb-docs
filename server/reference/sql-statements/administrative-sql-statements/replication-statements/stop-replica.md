# STOP REPLICA

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

## Syntax

```sql
STOP { SLAVE | REPLICA } ["connection_name"] [thread_type [, thread_type] ... ] 
[FOR CHANNEL "connection_name"]

STOP ALL { SLAVES | REPLICAS } [thread_type [, thread_type]]

STOP { SLAVE | REPLICA } ["connection_name"] [thread_type [, thread_type] ... ]

STOP ALL { SLAVES | REPLICAS } [thread_type [, thread_type]] 

thread_type: IO_THREAD | SQL_THREAD
```

## Description

Stops the replica threads. `STOP REPLICA` requires the [SUPER](../../account-management-sql-statements/grant.md#super) privilege, or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2), the [REPLICATION SLAVE ADMIN](../../account-management-sql-statements/grant.md#replication-slave-admin) privilege.

Like [START REPLICA](start-replica.md), this statement may be used with the `IO_THREAD` and`SQL_THREAD` options to name the thread or threads to be stopped. In almost all cases, one never need to use the `thread_type` options.

`STOP REPLICA` waits until any current replication event group affecting one or more non-transactional tables has finished executing (if there is any such replication group), or until the user issues a [KILL QUERY](../kill.md) or [KILL CONNECTION](../kill.md) statement.

Note that `STOP REPLICA` doesn't delete the connection permanently. Next time you execute [START REPLICA](start-replica.md) or the MariaDB server restarts, the replica connection is restored with it's [original arguments](change-master-to.md). If you want to delete a connection, you should execute [RESET REPLICA](reset-replica.md).

#### STOP ALL REPLICAS

`STOP ALL REPLICAS` stops all your running replicas. It will give you a `note` for every stopped connection. You can check the notes with [SHOW WARNINGS](../show/show-warnings.md).

#### connection\_name

The `connection_name` option is used for [multi-source replication](../../../../ha-and-performance/standard-replication/multi-source-replication.md).

If there is only one nameless master, or the default master (as specified by the [default\_master\_connection](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable) is intended, `connection_name` can be omitted. If provided, the `STOP REPLICA` statement will apply to the specified master. `connection_name` is case-insensitive.

**MariaDB starting with** [**10.7.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.0)

{% tabs %}
{% tab title="Current" %}
The `FOR CHANNEL` keyword is available for MySQL compatibility. This is identical as using the channel\_name directly after `STOP REPLICA`.
{% endtab %}

{% tab title="< 10.7.0" %}
The `FOR CHANNEL` keyword is not available.
{% endtab %}
{% endtabs %}

## See Also

* [CHANGE MASTER TO](change-master-to.md) is used to create and change connections.
* [START REPLICA](start-replica.md) is used to start a predefined connection.
* [RESET REPLICA](reset-replica.md) is used to reset parameters for a connection and also to permanently delete a master connection.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
