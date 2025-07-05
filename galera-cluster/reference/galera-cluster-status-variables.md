# Galera Cluster Status Variables

## Viewing Galera Cluster Status Variables

Galera status variables can be viewed with the [SHOW STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/administrative-sql-statements/show/show-status) statement.

```
SHOW STATUS LIKE 'wsrep%';
```

See also the [Full list of MariaDB options, system and status variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/full-list-of-mariadb-options-system-and-status-variables).

## List of Galera Cluster status variables

MariaDB Galera Cluster has the following status variables:

#### `wsrep_applier_thread_count`

* Description: Stores current number of applier threads to make clear how many slave threads of this type there are.



#### `wsrep_apply_oooe`

* Description: How often writesets have been applied out of order, an indicators of parallelization efficiency.

#### `wsrep_apply_oool`

* Description: How often writesets with a higher sequence number were applied before ones with a lower sequence number, implying slow writesets.

#### `wsrep_apply_window`

* Description: Average distance between highest and lowest concurrently applied seqno.

#### `wsrep_cert_deps_distance`

* Description: Average distance between the highest and the lowest sequence numbers that can possibly be applied in parallel, or the potential degree of parallelization.

#### `wsrep_cert_index_size`

* Description: The number of entries in the certification index.

#### `wsrep_cert_interval`

* Description: Average number of transactions received while a transaction replicates.

#### `wsrep_cluster_capabilities`

* Description:

#### `wsrep_cluster_conf_id`

* Description: Total number of cluster membership changes that have taken place.

#### `wsrep_cluster_size`

* Description: Number of nodes currently in the cluster.

#### `wsrep_cluster_state_uuid`

* Description: UUID state of the cluster. If it matches the value in [wsrep\_local\_state\_uuid](galera-cluster-status-variables.md#wsrep_local_state_uuid), the local and cluster nodes are in sync.

#### `wsrep_cluster_status`

* Description: Cluster component status. Possible values are `PRIMARY` (primary group configuration, quorum present), `NON_PRIMARY` (non-primary group configuration, quorum lost) or `DISCONNECTED` (not connected to group, retrying).

#### `wsrep_cluster_weight`

* Description: The total weight of the current members in the cluster. The value is counted as a sum of pc.weight of the nodes in the current Primary Component.

#### `wsrep_commit_oooe`

* Description: How often a transaction was committed out of order.

#### `wsrep_commit_oool`

* Description: No meaning.

#### `wsrep_commit_window`

* Description: Average distance between highest and lowest concurrently committed seqno.

#### `wsrep_connected`

* Description: Whether or not MariaDB is connected to the wsrep provider. Possible values are `ON` or `OFF`.

#### `wsrep_desync_count`

* Description: Returns the number of operations in progress that require the node to temporarily desync from the cluster.

#### `wsrep_evs_delayed`

* Description: Provides a comma separated list of all the nodes this node has registered on its delayed list.

#### `wsrep_evs_evict_list`

* Description: Lists the UUID’s of all nodes evicted from the cluster. Evicted nodes cannot rejoin the cluster until you restart their mysqld processes.

#### `wsrep_evs_repl_latency`

* Description: This status variable provides figures for the replication latency on group communication. It measures latency (in seconds) from the time point when a message is sent out to the time point when a message is received. As replication is a group operation, this essentially gives you the slowest ACK and longest RTT in the cluster. Format is min/avg/​max/stddev

#### `wsrep_evs_state`

* Description: Shows the internal state of the EVS Protocol.

#### `wsrep_flow_control_paused`

* Description: The fraction of time since the last FLUSH STATUS command that replication was paused due to flow control.

#### `wsrep_flow_control_paused_ns`

* Description: The total time spent in a paused state measured in nanoseconds.

#### `wsrep_flow_control_recv`

* Description: Number of FC\_PAUSE events received as well as sent since the most recent status query.

#### `wsrep_flow_control_sent`

* Description: Number of FC\_PAUSE events sent since the most recent status query

#### `wsrep_gcomm_uuid`

* Description: The UUID assigned to the node.

#### `wsrep_incoming_addresses`

* Description: Comma-separated list of incoming server addresses in the cluster component.

#### `wsrep_last_committed`

* Description: Sequence number of the most recently committed transaction.

#### `wsrep_local_bf_aborts`

* Description: Total number of local transactions aborted by slave transactions while being executed

#### `wsrep_local_cached_downto`

* Description: The lowest sequence number, or seqno, in the write-set cache (GCache).

#### `wsrep_local_cert_failures`

* Description: Total number of local transactions that failed the certification test.

#### `wsrep_local_commits`

* Description: Total number of local transactions committed on the node.

#### `wsrep_local_index`

* Description: The node's index in the cluster. The index is zero-based.

#### `wsrep_local_recv_queue`

* Description: Current length of the receive queue, which is the number of writesets waiting to be applied.

#### `wsrep_local_recv_queue_avg`

* Description: Average length of the receive queue since the most recent status query. If this value is noticeably larger than zero, the node is likely to be overloaded, and cannot apply the writesets as quickly as they arrive, resulting in replication throttling.

#### `wsrep_local_recv_queue_max`

* Description: The maximum length of the recv queue since the last FLUSH STATUS command.

#### `wsrep_local_recv_queue_min`

* Description: The minimum length of the recv queue since the last FLUSH STATUS command.

#### `wsrep_local_replays`

* Description: Total number of transaction replays due to asymmetric lock granularity.

#### `wsrep_local_send_queue`

* Description: Current length of the send queue, which is the number of writesets waiting to be sent.

#### `wsrep_local_send_queue_avg`

* Description: Average length of the send queue since the most recent status query. If this value is noticeably larger than zero, there is most likely network throughput or replication throttling issues.

#### `wsrep_local_send_queue_max`

* Description: The maximum length of the send queue since the last FLUSH STATUS command.

#### `wsrep_local_send_queue_min`

* Description: The minimum length of the send queue since the last FLUSH STATUS command.

#### `wsrep_local_state`

* Description: Internal Galera Cluster FSM state number.

#### `wsrep_local_state_comment`

* Description: Human-readable explanation of the state.

#### `wsrep_local_state_uuid`

* Description: The node's UUID state. If it matches the value in [wsrep\_cluster\_state\_uuid](galera-cluster-status-variables.md#wsrep_cluster_state_uuid), the local and cluster nodes are in sync.

#### `wsrep_open_connections`

* Description: The number of open connection objects inside the wsrep provider.

#### `wsrep_open_transactions`

* Description: The number of locally running transactions which have been registered inside the wsrep provider. This means transactions which have made operations which have caused write set population to happen. Transactions which are read only are not counted.

#### `wsrep_protocol_version`

* Description: The wsrep protocol version being used.

#### `wsrep_provider_name`

* Description: The name of the provider. The default is "Galera".

#### `wsrep_provider_vendor`

* Description: The vendor string.

#### `wsrep_provider_version`

* Description: The version number of the Galera wsrep provider

#### `wsrep_ready`

* Description: Whether or not the Galera wsrep provider is ready. Possible values are `ON` or `OFF`

#### `wsrep_received`

* Description: Total number of writesets received from other nodes.

#### `wsrep_received_bytes`

* Description: Total size in bytes of all writesets received from other nodes.

#### `wsrep_repl_data_bytes`

* Description: Total size of data replicated.

#### `wsrep_repl_keys`

* Description: Total number of keys replicated.

#### `wsrep_repl_keys_bytes`

* Description: Total size of keys replicated.

#### `wsrep_repl_other_bytes`

* Description: Total size of other bits replicated.

#### `wsrep_replicated`

* Description: Total number of writesets replicated to other nodes.

#### `wsrep_replicated_bytes`

* Description: Total size in bytes of all writesets replicated to other nodes.

#### `wsrep_rollbacker_thread_count`

* Description: Stores current number of rollbacker threads to make clear how many slave threads of this type there are.

#### `wsrep_thread_count`

* Description: Total number of wsrep (applier/rollbacker) threads.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
