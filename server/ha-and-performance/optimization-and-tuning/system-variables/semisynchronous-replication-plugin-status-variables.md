# Semisynchronous Replication Plugin Status Variables

This page documents status variables related to the [Semisynchronous Replication Plugin](../../standard-replication/semisynchronous-replication.md) (which has been merged into the main server from [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.3)). See [Server Status Variables](server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md).

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `Rpl_semi_sync_master_clients`

* Description: Number of semisynchronous slaves.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_get_ack`

* Description: Number of acknowledgements received by the master from slaves.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_net_avg_wait_time`

* Description: Average time the master waited for a slave to reply, in microseconds.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_net_wait_time`

* Description: Total time the master waited for slave replies, in microseconds.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_net_waits`

* Description: Total number of times the master waited for slave replies.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_no_times`

* Description: Number of times the master turned off semisynchronous replication. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Data Type: `numeric`

#### `Rpl_semi_sync_master_no_tx`

* Description: Number of commits that have not been successfully acknowledged by a slave. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Data Type: `numeric`

#### `Rpl_semi_sync_master_request_ack`

* Description: Number of acknowledgement requests sent to slaves.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_status`

* Description: Whether or not semisynchronous replication is currently operating on the master. The value will be `ON` if both the plugin has been enabled and a commit acknowledgment has occurred. It will be `OFF` if either the plugin has not been enabled, or the master is replicating asynchronously due to a commit acknowledgment timeout.
* Data Type: `boolean`

#### `Rpl_semi_sync_master_timefunc_failures`

* Description: Number of times the master failed when calling a time function, such as gettimeofday(). The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Data Type: `numeric`

#### `Rpl_semi_sync_master_tx_avg_wait_time`

* Description: Average time the master waited for each transaction, in microseconds.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_tx_wait_time`

* Description: Total time the master waited for transactions, in microseconds.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_tx_waits`

* Description: Total number of times the master waited for transactions.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_wait_pos_backtraverse`

* Description: Total number of times the master waited for an event that had binary coordinates lower than previous events waited for. Occurs if the order in which transactions start waiting for a reply is different from the order in which their binary log events were written. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Data Type: `numeric`

#### `Rpl_semi_sync_master_wait_sessions`

* Description: Number of sessions that are currently waiting for slave replies.
* Data Type: `numeric`

#### `Rpl_semi_sync_master_yes_tx`

* Description: Number of commits that have been successfully acknowledged by a slave. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Data Type: `numeric`

#### `Rpl_semi_sync_slave_status`

* Description: Whether or not semisynchronous replication is currently operating on the slave. `ON` if both semi-sync has been enabled for the replica (i.e. by setting the variable [rpl\_semi\_sync\_slave\_enabled](../../standard-replication/semisynchronous-replication.md#rpl_semi_sync_slave_enabled) to `TRUE`) and the slave I/O thread is running.
* Data Type: `boolean`

#### `Rpl_semi_sync_slave_send_ack`

* Description: Number of acknowledgements the slave sent to the master.
* Data Type: `numeric`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
