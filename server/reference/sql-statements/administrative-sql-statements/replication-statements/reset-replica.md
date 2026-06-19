# RESET SLAVE

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

## Syntax

```bnf
RESET { SLAVE | REPLICA } ["connection_name"] [ALL]  [FOR CHANNEL "connection_name"].
```

## Description

RESET SLAVE makes the slave forget its [replication](../../../../ha-and-performance/standard-replication/) position in the master's [binary log](../../../../server-management/server-monitoring-logs/binary-log/). This statement is meant to be used for a clean start. It deletes the master.info and relay-log.info files, all the [relay log](../../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files, and starts a new relay log file. To use RESET SLAVE, the slave threads must be stopped (use [STOP SLAVE](stop-replica.md) if necessary).

Note: All relay log files are deleted, even if they have not been completely executed by the slave SQL thread. (This is a condition likely to exist on a replication slave if you have issued a STOP SLAVE statement or if the slave is highly loaded.)

Note: `RESET SLAVE` does not reset the global`gtid_slave_pos` variable. This means that a slave server configured with `CHANGE MASTER TO MASTER_USE_GTID=slave_pos` will not receive events with GTIDs occurring before the state saved in`gtid_slave_pos`. If the intent is to reprocess these events,`gtid_slave_pos` must be manually reset, e.g., by executing `set global gtid_slave_pos=""`.

Connection information stored in the master.info file is immediately reset using any values specified in the corresponding startup options. This information includes values such as master host, master port, master user, and master password. If the slave SQL thread was in the middle of replicating temporary tables when it was stopped, and RESET SLAVE is issued, these replicated temporary tables are deleted on the slave.

The `ALL` also resets the `PORT`, `HOST`, `USER`, and `PASSWORD` parameters for the slave. If you are using a connection name, it will be permanently deleted it and it will not show up anymore in [SHOW ALL SLAVES STATUS](../show/show-replica-status.md).

#### connection\_name

The `connection_name` option is used for [multi-source replication](../../../../ha-and-performance/standard-replication/multi-source-replication.md).

If there is only one nameless master, or the default master (as specified by the [default\_master\_connection](../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) system variable) is intended, `connection_name` can be omitted. If provided, the `RESET SLAVE` statement will apply to the specified master. `connection_name` is case-insensitive.

**MariaDB starting with** [**10.7.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.7/10.7.0)

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From MariaDB 10.7:
{% endhint %}

The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical to using the channel\_name directly after `RESET SLAVE`.
{% endtab %}

{% tab title="< 10.7" %}
{% hint style="info" %}
Before MariaDB 10.7:
{% endhint %}

`FOR CHANNEL` is not available.
{% endtab %}
{% endtabs %}

The `FOR CHANNEL` keyword was added for MySQL compatibility. This is identical as using the channel\_name directly after `RESET SLAVE`.

**MariaDB starting with** [**11.6.0**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.6/11.6.0)

{% tabs %}
{% tab title="Current" %}
{% hint style="info" %}
From MariaDB 12.0:
{% endhint %}

`RESET SLAVE` resets the `Master`/`Slave_last_event_time` and `Connects_Tried` values (see [SHOW SLAVE STATUS](../show/show-replica-status.md)).
{% endtab %}

{% tab title="< 12.0" %}
{% hint style="info" %}
From MariaDB 11.6 to before MariaDB 12.0:
{% endhint %}

`RESET SLAVE` resets the `Master`/`Slave_last_event_time` values (see [SHOW SLAVE STATUS](../show/show-replica-status.md)).
{% endtab %}

{% tab title="< 11.6" %}
{% hint style="info" %}
Before MariaDB 11.6:
{% endhint %}

`RESET SLAVE` does not reset the `Master`/`Slave_last_event_time` values (see [SHOW SLAVE STATUS](../show/show-replica-status.md)).
{% endtab %}
{% endtabs %}

## See Also

* [STOP SLAVE](stop-replica.md) stops the slave, but it can be restarted with [START SLAVE](start-replica.md) or after next MariaDB server restart.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
