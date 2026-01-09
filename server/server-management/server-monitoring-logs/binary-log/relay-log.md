---
description: >-
  Overview of the relay log, a set of log files created by a replica server to
  store events received from the primary's binary log before executing them.
---

# Relay Log

The relay log is a set of log files created by a replica during [replication](../../../ha-and-performance/standard-replication/).

It's the same format as the [binary log](./), containing a record of events that affect the data or structure; thus, [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) can be used to display its contents. It consists of a set of relay log files and an index file containing a list of all relay log files.

Events are read from the primary's binary log and written to the replica's relay log. They are then performed on the replica. Old relay log files are automatically removed once they are no longer needed.

## Creating Relay Log Files

New relay log files are created by the replica at the following times:

* When the IO thread starts.
* When the logs are flushed, with [FLUSH LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) or [mariadb-admin flush-logs](../../../clients-and-utilities/administrative-tools/mariadb-admin.md).
* When the maximum size, determined by the [max\_relay\_log\_size](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#max_relay_log_size) system variable, has been reached.

## Relay Log Names

By default, the relay log will be given a name `host_name-relay-bin.nnnnnn`, with `host_name` referring to the server's host name, and #nnnnnn`the sequence number.`

This causes problems if the replica's host name changes, returning this error:

```
Failed to open the relay log and Could not find target log during relay log initialization
```

To prevent this, you can specify the relay log file name by setting the [relay\_log](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log) and [relay\_log\_index](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_index) system variables.

If you need to overcome this issue while replication is already underway,you can stop the replica, prepend the old relay log index file to the new relay log index file, and restart the replica.

For example:

```bash
shell> cat NEW_relay_log_name.index >> OLD_relay_log_name.index
shell> mv OLD_relay_log_name.index NEW_relay_log_name.index
```

## Viewing Relay Logs

The [SHOW RELAYLOG EVENTS](../../../reference/sql-statements/administrative-sql-statements/show/show-relaylog-events.md) shows events in the relay log, and, since relay log files are the same format as binary log files, they can be read with the [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) utility.

## Removing Old Relay Logs

Old relay logs are automatically removed once all events have been implemented on the replica, and the relay log file is no longer needed. This behavior can be changed by adjusting the [relay\_log\_purge](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_purge) system variable from its default of `1` to `0`, in which case the relay logs will be left on the server.

Relay logs are also removed by the [CHANGE MASTER](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) statement unless a [relay log option](../../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#relay_log_options) is used.

One can also flush the logs with the [FLUSH RELAY LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) commands.

If the relay logs are taking up too much space on the replica, the [relay\_log\_space\_limit](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#relay_log_space_limit) system variable can be set to limit the size. The IO thread will stop until the SQL thread has cleared the backlog. By default there is no limit.

## See also

* [FLUSH RELAY LOGS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
