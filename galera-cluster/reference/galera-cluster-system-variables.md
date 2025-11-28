# Galera Cluster System Variables

/This page documents system variables related to Galera Cluster. For options that are not system variables, see [Galera Options](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#galera-cluster-options).

See [Server System Variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables) for a complete list of system variables and instructions on setting them.

Also see the [Full list of MariaDB options, system and status variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables).

#### `wsrep_allowlist`

* Description:
  * Allowed IP addresses, comma delimited.
  * Note that setting `gmcast.listen_addr=tcp://[::]:4567` on a dual-stack system (eg. Linux with `net.ipv6.bindv6only = 0`), IPv4 addresses need to allowlisted using the IPv4-mapped IPv6 address (eg. `::ffff:1.2.3.4`).
* Commandline: `--wsrep-allowlist=value1[,value2...]`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: None
* Introduced: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010)

#### `wsrep_applier_retry_count`

* Description: Maximum number of applier retry attempts. Prior to MariaDB 12.1, replication\
  applying always stops for the first non-ignored failure occurring in event applying, and the node will emergency abort (or start inconsistency voting). Some failures, however, can be concurrency related, and applying may succeed if the operation is tried at later time. This variable controls the retry-applying feature. It is set to zero by default, which means no retrying.
* Commandline: `--wsrep-applier-retry-count=value`
* Scope: Global
* Dynamic: Yes
* Data Type: INT UNSIGNED
* Default Value: `0`
* Range: `0` to `4294967295`
* Introduced: [MariaDB 12.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.1/changes-and-improvements-in-mariadb-12.1)

#### `wsrep_auto_increment_control`

* Description: If set to `1` (the default), will automatically adjust the [auto\_increment\_increment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) and [auto\_increment\_offset](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) variables according to the size of the cluster, and when the cluster size changes. This avoids replication conflicts due to [auto\_increment](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/auto_increment). In a primary-replica environment, can be set to `OFF`.
* Commandline: `--wsrep-auto-increment-control[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `ON`

#### `wsrep_causal_reads`

* Description: If set to `ON` (`OFF` is default), enforces [read-committed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/transactions-read-committed) characteristics across the cluster. In the case that a primary applies an event more quickly than a replica, the two could briefly be out-of-sync. With this variable set to `ON`, the replica will wait for the event to be applied before processing further queries. Setting to `ON` also results in larger read latencies. Deprecated by [wsrep\_sync\_wait=1](galera-cluster-system-variables.md#wsrep_sync_wait).
* Commandline: `--wsrep-causal-reads[={0|1}]`
* Scope: Session
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`
* Removed: [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes)

#### `wsrep_certificate_expiration_hours_warning`

{% content-ref url="wsrep-variable-details/wsrep_certificate_expiration_hours_warning.md" %}
[wsrep\_certificate\_expiration\_hours\_warning.md](wsrep-variable-details/wsrep_certificate_expiration_hours_warning.md)
{% endcontent-ref %}

#### `wsrep_certification_rules`

* Description: Certification rules to use in the cluster. Possible values are:
  * `strict`: Stricter rules that could result in more certification failures. For example with foreign keys, certification failure could result if different nodes receive non-conflicting insertions at about the same time that point to the same row in a parent table
  * `optimized`: relaxed rules that allow more concurrency and cause less certification failures.
* Commandline: `--wsrep-certifcation-rules`
* Scope: Global
* Dynamic: Yes
* Data Type: Enumeration
* Default Value: `strict`
* Valid Values: `strict`, `optimized`

#### `wsrep_certify_nonPK`

* Description: When set to `ON` (the default), Galera will still certify transactions for tables with no [primary key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/mariadb-quickstart-guides/mariadb-indexes-guide#primary-key). However, this can still cause undefined behavior in some circumstances. It is recommended to define primary keys for every InnoDB table when using Galera.
* Commandline: `--wsrep-certify-nonPK[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `ON`

#### `wsrep_cluster_address`

* Description: The addresses of cluster nodes to connect to when starting up.
  * Good practice is to specify all possible cluster nodes, in the form `gcomm://<node1 or ip:port>,<node2 or ip2:port>,<node3 or ip3:port>`.
  * Specifying an empty ip (`gcomm://`) will cause the node to start a new cluster (which should not be done in the my.cnf file, as after each restart the server will not rejoin the current cluster).
  * The variable can be changed at runtime in some configurations, and will result in the node closing the connection to any current cluster, and connecting to the new address.
  * If specifying a port, note that this is the Galera port, not the MariaDB port.
  * For example:
    * `gcomm://192.168.0.1,192.168.0.2,192.168.0.3`
    * `gcomm://192.168.0.1:1234,192.168.0.2:1234,192.168.0.3:1234?gmcast.listen_addr=tcp://0.0.0.0:1234`
  * See also [gmcast.listen\_addr](wsrep-variable-details/wsrep_provider_options.md#gmcastlisten_addr)
* Commandline: `--wsrep-cluster-address=value`
* Scope: Global
* Dynamic: No
* Data Type: String

#### `wsrep_cluster_name`

* Description: The name of the cluster. Nodes cannot connect to clusters with a different name, so needs to be identical on all nodes in the same cluster. The variable can be set dynamically, but note that doing so may be unsafe and cause an outage, and that the wsrep provider is unloaded and loaded.
* Commandline: `--wsrep-cluster-name=value`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: `my_wsrep_cluster`

{% content-ref url="wsrep-variable-details/wsrep_cluster_name.md" %}
[wsrep\_cluster\_name.md](wsrep-variable-details/wsrep_cluster_name.md)
{% endcontent-ref %}

#### `wsrep_convert_LOCK_to_trx`

* Description: Converts [LOCK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/lock-tables)/[UNLOCK TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/transactions-unlock-tables) statements to [BEGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/begin-end) and [COMMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/commit). Used mainly for getting older applications to work with a multi-primary setup, use carefully, as can result in extremely large writesets.
* Commandline: `--wsrep-convert-LOCK-to-trx[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`

#### `wsrep_data_home_dir`

* Description: Directory where wsrep provider will store its internal files.
* Commandline: `--wsrep-data-home-dir=value`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: The [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir) variable value.

#### `wsrep_dbug_option`

* Description: Unused. The mechanism to pass the DBUG options to the wsrep provider hasn't been implemented.
* Commandline: `--wsrep-dbug-option=value`
* Scope: Global
* Dynamic: Yes
* Data Type: String

#### `wsrep_debug`

* Description: WSREP debug level logging.
  * Before [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.1), DDL logging was only logged on the originating node. From [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.1), it is logged on other nodes as well.

It is an enum. Valid values are:`0: NONE`: Off (default)`1: SERVER`: MariaDB server code contains WSREP\_DEBUG log writes, and these will be added to server error log`2: TRANSACTION`: Logging from wsrep-lib transaction is added to the error log`3: STREAMING`: Logging from streaming transactions in wsrep-lib is added to the error log`4: CLIENT`: Logging from wsrep-lib client state is added to the error log.

* Commandline:
  * `--wsrep-debug[={NONE|SERVER|TRANSACTION|STREAMING|CLIENT}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Enumeration
* Default Value: `NONE`
* Valid Values: `NONE`, `SERVER`, `TRANSACTION`, `STREAMING`, `CLIENT`

#### `wsrep_desync`

* Description: When a node receives more write-sets than it can apply, the transactions are placed in a received queue. If the node's received queue has too many write-sets waiting to be applied (as defined by the [gcs.fc\_limit](wsrep-variable-details/wsrep_provider_options.md#gcsfc_limit) WSREP provider option), then the node would usually engage Flow Control. However, when this option is set to `ON`, Flow Control will be disabled for the desynced node. The desynced node works through the received queue until it reaches a more manageable size. The desynced node continues to receive write-sets from the other nodes in the cluster. The other nodes in the cluster do not wait for the desynced node to catch up, so the desynced node can fall even further behind the other nodes in the cluster. You can check if a node is desynced by checking if the [wsrep\_local\_state\_comment](galera-cluster-status-variables.md#wsrep_local_state_comment) status variable is equal to `Donor/Desynced`.
* Commandline: `--wsrep-desync[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`

#### `wsrep_dirty_reads`

* Description: By default, when not synchronized with the group ([wsrep\_ready](galera-cluster-status-variables.md#wsrep_ready)=OFF) a node will reject all queries other than SET and SHOW. If `wsrep_dirty_reads` is set to `1`, queries which do not change data, like SELECT queries (dirty reads), creating of prepare statement, etc. will be accepted by the node.
* Commandline: `--wsrep-dirty-reads[={0|1}]`
* Scope: Global,Session
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`
* Valid Values: `ON`, `OFF`

#### `wsrep_drupal_282555_workaround`

* Description: If set to `ON`, a workaround for [Drupal/MySQL/InnoDB bug #282555](https://www.drupal.org/node/282555) is enabled. This is a bug where, in some cases, when inserting a `DEFAULT` value into an [AUTO\_INCREMENT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/auto_increment) column, a duplicate key error may be returned.
* Commandline: `--wsrep-drupal-282555-workaround[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`

#### `wsrep_forced_binlog_format`

* Description: A [binary log format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats) that will override any session binlog format settings.
* Commandline: `--wsrep-forced-binlog-format=value`
* Scope: Global
* Dynamic: Yes
* Default Value: `NONE`
* Data Type: Enum
* Valid Values: `STATEMENT`, `ROW`, `MIXED` or `NONE` (which resets the forced binlog format state).

#### `wsrep_gtid_domain_id`

* Description: This system variable defines the [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) domain ID that is used for [wsrep GTID mode](../high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md#wsrep-gtid-mode).
  * When [wsrep\_gtid\_mode](galera-cluster-system-variables.md#wsrep_gtid_mode) is set to `ON`, `wsrep_gtid_domain_id` is used in place of [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_domain_id) for all Galera Cluster write sets.
  * When [wsrep\_gtid\_mode](galera-cluster-system-variables.md#wsrep_gtid_mode) is set to `OFF`, `wsrep_gtid_domain_id` is simply ignored to allow for backward compatibility.
  * There are some additional requirements that need to be met in order for this mode to generate consistent [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid). For more information, see [Using MariaDB GTIDs with MariaDB Galera Cluster](../high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md).
* Commandline: `--wsrep-gtid-domain-id=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `0` to `4294967295`

#### `wsrep_gtid_mode`

* Description: [Wsrep GTID mode](../high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md#wsrep-gtid-mode) attempts to keep [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) consistent for Galera Cluster write sets on all cluster nodes. [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) state is initially copied to a joiner node during an [SST](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md). If you are planning to use Galera Cluster with [MariaDB replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication), then wsrep GTID mode can be helpful.
  * When `wsrep_gtid_mode` is set to `ON`, [wsrep\_gtid\_domain\_id](galera-cluster-system-variables.md#wsrep_gtid_domain_id) is used in place of [gtid\_domain\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_domain_id) for all Galera Cluster write sets.
  * When `wsrep_gtid_mode` is set to `OFF`, [wsrep\_gtid\_domain\_id](galera-cluster-system-variables.md#wsrep_gtid_domain_id) is simply ignored to allow for backward compatibility.
  * There are some additional requirements that need to be met in order for this mode to generate consistent [GTIDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid). For more information, see [Using MariaDB GTIDs with MariaDB Galera Cluster](../high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-gtids-with-mariadb-galera-cluster.md).
* Commandline: `--wsrep-gtid-mode[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`

#### `wsrep_gtid_seq_no`

* Description: Internal server usage, manually set WSREP GTID seqno.
* Commandline: None
* Scope: Session only
* Dynamic: Yes
* Data Type: `numeric`
* Range: `0` to `18446744073709551615`
* Introduced: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)

#### `wsrep_ignore_apply_errors`

* Description: Bitmask determining whether errors are ignored, or reported back to the provider.
  * 0: No errors are skipped.
  * 1: Ignore some DDL errors (DROP DATABASE, DROP TABLE, DROP INDEX, ALTER TABLE).
  * 2: Skip DML errors (Only ignores DELETE errors).
  * 4: Ignore all DDL errors.
* Commandline: `--wsrep-ignore-apply-errors`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `7`
* Range: `0` to `7`

#### `wsrep_load_data_splitting`

* Description: If set to `ON`, [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) supports big data files by introducing transaction splitting. The setting has been deprecated in Galera 4, and defaults to `OFF`
* Commandline: `--wsrep-load-data-splitting[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`
* Deprecated: [MariaDB 10.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1042-release-notes)
* Removed: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115)

#### `wsrep_log_conflicts`

* Description: If set to `ON` (`OFF` is default), details of conflicting MDL as well as InnoDB locks in the cluster will be logged.
* Commandline: `--wsrep-log-conflicts[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`

#### `wsrep_max_ws_rows`

* Description: Maximum permitted number of rows per writeset. The support for this variable has been added and in order to be backward compatible the default value has been changed to `0`, which essentially allows writesets to be any size.
* Commandline: `--wsrep-max-ws-rows=#`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value:
  * `0`
* Range: `0` to `1048576`

#### `wsrep_max_ws_size`

* Description: Maximum permitted size in bytes per write set. Writesets exceeding 2GB will be rejected.
* Commandline: `--wsrep-max-ws-size=#`
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value:
  * `2147483647` (2GB)
* Range: `1024` to `2147483647`

#### `wsrep_mode`

* Description: Turns on `WSREP` features which are not part of default behavior.
  * `BINLOG_ROW_FORMAT_ONLY`: Only `ROW` [binlog format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats) is supported.
  * `DISALLOW_LOCAL_GTID`: Nodes can have GTIDs for local transactions in a number of scenarios. If `DISALLOW_LOCAL_GTID` is set, these operations produce an error `ERROR HY000: Galera replication not supported`. Scenarios include:
    * A DDL statement is executed with `wsrep_OSU_method=RSU` set.
    * A DML statement writes to a non-InnoDB table.
    * A DML statement writes to an InnoDB table with wsrep\_on=OFF set.
  * `REPLICATE_ARIA`: Whether or not DML updates for [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) tables will be replicated. This functionality is experimental and should not be relied upon in production systems.
  * `REPLICATE_MYISAM`: Whether or not DML updates for a [MyISAM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine) tables will be replicated. This functionality is experimental and should not be relied upon in production systems.
  * `REQUIRED_PRIMARY_KEY`: Table should have PRIMARY KEY defined.
  * `STRICT_REPLICATION`: Same as the old [wsrep\_strict\_ddl](galera-cluster-system-variables.md#wsrep_strict_ddl) setting.
  * `SKIP_APPLIER_FK_CHECKS_IN_IST`: When this operation mode is set, and the node is processing IST or catch-up, appliers skip FK[^1] checking. See [this page for details](../high-availability/rapid-node-recovery-with-ist-and-the-gcache.md#skipping-foreign-key-checks).\
    This flag is available from MariaDB 12.0.
* Command line: `--wsrep-mode=value`
* Scope: Global
* Dynamic: Yes
* Data Type: Enumeration
* Default Value: (Empty)
* Valid Values: `SKIP_APPLIER_FK_CHECKS_IN_IST`,  `BINLOG_ROW_FORMAT_ONLY`, `DISALLOW_LOCAL_GTID`, `REQUIRED_PRIMARY_KEY`, `REPLICATE_ARIA`, `REPLICATE_MYISAM` and `STRICT_REPLICATION`&#x20;
* Introduced: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0)

#### `wsrep_mysql_replication_bundle`

* Description: Determines the number of replication events that are grouped together. Experimental implementation aimed to assist with bottlenecks when a single replica faces a large commit time delay. If set to `0` (the default), there is no grouping.
* Commandline: `--wsrep-mysql-replication-bundle=#`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `0`
* Range: `0` to `1000`

#### `wsrep_node_address`

* Description: Specifies the node's network address, in the format `ip address[:port]`. It supports IPv6. The default behavior is for the node to pull the address of the first network interface on the system and the default Galera port. This autoguessing can be unreliable, particularly in the following cases:
  * cloud deployments
  * container deployments
  * servers with multiple network interfaces.
  * servers running multiple nodes.
  * network address translation (NAT).
  * clusters with nodes in more than one region.
* See also [wsrep\_provider\_options -> gmcast.listen\_addr](wsrep-variable-details/wsrep_provider_options.md#gmcastlisten_addr)
* Commandline: `--wsrep-node-address=value`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: Primary network address, usually `eth0` with a default port of 4567, or `0.0.0.0` if no IP address.

#### `wsrep_node_incoming_address`

* Description: This is the address from which the node listens for client connections. If an address is not specified or it's set to `AUTO` (default), mysqld uses either [--bind-address](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#bind_address) or [--wsrep-node-address](galera-cluster-system-variables.md#wsrep_node_address), or tries to get one from the list of available network interfaces, in the same order. See also [wsrep\_provider\_options -> gmcast.listen\_addr](wsrep-variable-details/wsrep_provider_options.md#gmcastlisten_addr).
* Commandline: `--wsrep-node-incoming-address=value`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: `AUTO`

#### `wsrep_node_name`

* Description: Name of this node. This name can be used in [wsrep\_sst\_donor](galera-cluster-system-variables.md#wsrep_sst_donor) as a preferred donor. Note that multiple nodes in a cluster can have the same name.
* Commandline: `--wsrep-node-name=value`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: The server's hostname.

#### `wsrep_notify_cmd`

* Description: Command to be executed each time the node state or the cluster membership changes. Can be used for raising an alarm, configuring load balancers and so on. See the [Codership Notification Script page](https://galeracluster.com/library/documentation/notification-cmd.html) for more details.
* Commandline: `--wsrep-notify-command=value`
* Scope: Global
* Dynamic:
  * No (>= [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1059-release-notes))
  * Yes (<= [MariaDB 10.5.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1058-release-notes))
* Data Type: String
* Default Value: Empty

#### `wsrep_on`

* Description: Whether or not wsrep replication is enabled. If the global value is set to `OFF` , it is not possible to load the provider and join the node in the cluster. If only the session value is set to `OFF`, the operations from that particular session are not replicated in the cluster, but other sessions and applier threads will continue as normal. The session value of the variable does not affect the node's membership and thus, regardless of its value, the node keeps receiving updates from other nodes in the cluster. It is set to `OFF` by default and must be turned on to enable Galera replication.
* Commandline: `--wsrep-on[={0|1}]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`
* Valid Values: `ON`, `OFF`

#### `wsrep_OSU_method`

* Description: Online schema upgrade method. The default is `TOI`, specifying the setting without the optional parameter will set to `RSU`.
  * `TOI`: Total Order Isolation. In each cluster node, DDL is processed in the same order regarding other transactions, guaranteeing data consistency. However, affected parts of the database will be locked for the whole cluster.
  * `RSU`: Rolling Schema Upgrade. DDL processing is only done locally on the node, and the user needs perform the changes manually on each node. The node is desynced from the rest of the cluster while the processing takes place to avoid the blocking other nodes. Schema changes [must be backwards compatible in the same way as for ROW based replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-when-the-primary-and-replica-have-different-table-definitions) to avoid breaking replication when the DDL processing is complete on the single node, and replication recommences.
* Commandline: `--wsrep-OSU-method[=value]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: Enum
* Default Value: `TOI`
* Valid Values: `TOI`, `RSU`

#### `wsrep_patch_version`

* Description: Wsrep patch version, for example `wsrep_25.10`.
* Commandline: None
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: None

#### `wsrep_provider`

* Description: Location of the wsrep library, usually `/usr/lib/libgalera_smm.so` on Debian and Ubuntu, and `/usr/lib64/libgalera_smm.so` on Red Hat/CentOS.
* Commandline: `--wsrep-provider=value`
* Scope: Global
  * No (>= [MariaDB 10.5.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1059-release-notes))
  * Yes (<= [MariaDB 10.5.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1058-release-notes))
* Data Type: String
* Default Value: None

#### `wsrep_provider_options`

* Description: Semicolon (;) separated list of wsrep options (see [wsrep\_provider\_options](wsrep-variable-details/wsrep_provider_options.md)).
* Commandline: `--wsrep-provider-options=value`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: Empty

{% content-ref url="wsrep-variable-details/wsrep_provider_options.md" %}
[wsrep\_provider\_options.md](wsrep-variable-details/wsrep_provider_options.md)
{% endcontent-ref %}

#### `wsrep_recover`

* Description: If set to `ON` when the server starts, the server will recover the sequence number of the most recent write set applied by Galera, and it will be output to `stderr`, which is usually redirected to the [error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log). At that point, the server will exit. This sequence number can be provided to the [wsrep\_start\_position](galera-cluster-system-variables.md#wsrep_start_position) system variable.
* Commandline: `--wsrep-recover[={0|1}]`
* Scope: Global
* Dynamic: No
* Data Type: Boolean
* Default Value: `OFF`

#### `wsrep_reject_queries`

* Description: Variable to set to reject queries from client connections, useful for maintenance. The node continues to apply write-sets, but an `Error 1047: Unknown command` error is generated by a client query.
  * `NONE` - Not set. Queries will be processed as normal.
  * `ALL` - All queries from client connections will be rejected, but existing client connections will be maintained.
  * `ALL_KILL` All queries from client connections will be rejected, and existing client connections, including the current one, will be immediately killed.
* Commandline: `--wsrep-reject-queries[=value]`
* Scope: Global
* Dynamic: Yes
* Data Type: Enum
* Default Value: `NONE`
* Valid Values: `NONE`, `ALL`, `ALL_KILL`

#### `wsrep_replicate_myisam`

* Description: Whether or not DML updates for [MyISAM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine) tables will be replicated. This functionality is still experimental and should not be relied upon in production systems. Deprecated in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6), and removed in [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107), use [wsrep\_mode](galera-cluster-system-variables.md#wsrep_mode) instead.
* Commandline: `--wsrep-replicate-myisam[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Default Value: `OFF`
* Data Type: Boolean
* Valid Values: `ON`, `OFF`
* Deprecated: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0)
* Removed: [MariaDB 10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

#### `wsrep_restart_slave`

* Description: If set to ON, the replica is restarted automatically, when node joins back to cluster.
* Commandline: `--wsrep-restart-slave[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Default Value: `OFF`
* Data Type: Boolean

#### `wsrep_retry_autocommit`

* Description: Number of times autocommited queries will be retried due to cluster-wide conflicts before returning an error to the client. If set to `0`, no retries will be attempted, while a value of `1` (the default) or more specifies the number of retries attempted. Can be useful to assist applications using autocommit to avoid deadlocks.
* Commandline: `--wsrep-retry-autocommit=value`
* Scope: Global
* Dynamic: No
* Data Type: Numeric
* Default Value: `1`
* Range: `0` to `10000`

#### `wsrep_slave_FK_checks`

* Description: If set to ON (the default), the applier replica thread performs foreign key constraint checks.
* Commandline: `--wsrep-slave-FK-checks[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: ON

#### `wsrep_slave_threads`

* Description: Number of replica threads used to apply Galera write sets in parallel. The Galera replica threads are able to determine which write sets are safe to apply in parallel. However, if your cluster nodes seem to have frequent consistency problems, then setting the value to `1` will probably fix the problem. See [About Galera Replication: Galera Replica Threads](../readme/about-galera-replication.md#galera-slave-threads) for more information.
* Commandline: `--wsrep-slave-threads=`#
* Scope: Global
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `1`
* Range: `1` to `512`

#### `wsrep_slave_UK_checks`

* Description: If set to ON, the applier replica thread performs secondary index uniqueness checks.
* Commandline: `--wsrep-slave-UK-checks[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: OFF

#### `wsrep_sr_store`

* Description: Storage for streaming replication fragments.
* Commandline: `--wsrep-sr-store=val`
* Scope: Global
* Dynamic: No
* Data Type: Enum
* Default Value: `table`
* Valid Values: `table`, `none`

#### `wsrep_ssl_mode`

{% content-ref url="wsrep-variable-details/wsrep_ssl_mode.md" %}
[wsrep\_ssl\_mode.md](wsrep-variable-details/wsrep_ssl_mode.md)
{% endcontent-ref %}

#### `wsrep_sst_auth`

* Description: Username and password of the user to use for replication. Unused if [wsrep\_sst\_method](galera-cluster-system-variables.md#wsrep_sst_method) is set to `rsync`, while for other methods it should be in the format `<user>:<password>`. The contents are masked in logs and when querying the value with [SHOW VARIABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-variables). See [Introduction to State Snapshot Transfers (SSTs)](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) for more information.
* Commandline: `--wsrep-sst-auth=value`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: (Empty)

#### `wsrep_sst_donor`

* Description: Comma-separated list (from 5.5.33) or name (as per [wsrep\_node\_name](galera-cluster-system-variables.md#wsrep_node_name)) of the servers as donors, or the source of the state transfer, in order of preference. The donor-selection algorithm, in general, prefers a donor capable of transferring only the missing transactions (IST) to the joiner node, instead of the complete state (SST). Thus, it starts by looking for an IST-capable node in the given donor list followed by rest of the nodes in the cluster. In case multiple candidate nodes are found outside the specified donor list, the node in the same segment ([gmcast.segment](wsrep-variable-details/wsrep_provider_options.md#gmcastsegment)) as the joiner is preferred. If none of the existing nodes in the cluster can serve the missing transactions through IST, the algorithm moves on to look for a suitable node to transfer the entire state (SST). It first looks at the nodes specified in the donor list (irrespective of their segment). If no suitable donor is still found, the rest of the donor nodes are checked for suitability only if the donor list has a "terminating-comma". Note that a stateless node (the Galera arbitrator) can never be a donor. See [Introduction to State Snapshot Transfers (SSTs)](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) for more information.\
  \[NOTE] Although the variable is dynamic, the node will not use the new value unless the node requiring SST or IST disconnects from the cluster. To force this, set [wsrep\_cluster\_address](galera-cluster-system-variables.md#wsrep_cluster_address) to an empty string and back to the nodes list. After setting this variable dynamically, on startup the value from the configuration file will be used again.
* Commandline: `--wsrep-sst-donor=value`
* Scope: Global
* Dynamic: Yes (read note above)
* Data Type: String
* Default Value:

#### `wsrep_sst_donor_rejects_queries`

* Description: If set to `ON` (`OFF` is default), the donor node will reject incoming queries, returning an `UNKNOWN COMMAND` error code. Can be used for informing load balancers that a node is unavailable.
* Commandline: `--wsrep-sst-donor-rejects-queries[={0|1}]`
* Scope: Global
* Dynamic: Yes
* Data Type: Boolean
* Default Value: `OFF`

#### `wsrep_sst_method`

* Description: Method used for taking the [state snapshot transfer (SST)](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md). See [Introduction to State Snapshot Transfers (SSTs): SST Methods](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md#sst-methods) for more information.
* Commandline: `--wsrep-sst-method=value`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: `rsync`
* Valid Values: `rsync`, `mysqldump`, `xtrabackup`, `xtrabackup-v2`, `mariadb-backup`

{% content-ref url="wsrep-variable-details/wsrep_sst_method.md" %}
[wsrep\_sst\_method.md](wsrep-variable-details/wsrep_sst_method.md)
{% endcontent-ref %}

#### `wsrep_sst_receive_address`

* Description: This is the address where other nodes (donor) in the cluster connect to in order to send the state-transfer updates. If an address is not specified or its set to `AUTO` (default), mysqld uses [--wsrep\_node\_address](galera-cluster-system-variables.md#wsrep_node_address)'s value as the receiving address. However, if [--wsrep\_node\_address](galera-cluster-system-variables.md#wsrep_node_address) is not set, it uses address from either [--bind-address](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#bind_address) or tries to get one from the list of available network interfaces, in the same order. Note: setting it to `localhost` will make it impossible for nodes running on other hosts to reach this node. See [Introduction to State Snapshot Transfers (SSTs)](../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md) for more information.
* Commandline: `--wsrep-sst-receive-address=value`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: `AUTO`

#### `wsrep_start_position`

* Description: The start position that the node should use in the format: `UUID:seq_no`. The proper value to use for this position can be recovered with [wsrep\_recover](galera-cluster-system-variables.md#wsrep_recover).
* Commandline: `--wsrep-start-position=value`
* Scope: Global
* Dynamic: Yes
* Data Type: String
* Default Value: `00000000-0000-0000-0000-000000000000:-1`

#### `wsrep_status_file`

* Description: wsrep status output filename.
* Commandline: `--wsrep-status-file=value`
* Scope: Global
* Dynamic: No
* Data Type: String
* Default Value: None
* Introduced: [MariaDB 10.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109)

#### `wsrep_strict_ddl`

* Description: If set, reject DDL statements on affected tables not supporting Galera replication. This is done by checking if the table is InnoDB, which is the only table currently fully supporting Galera replication. MyISAM tables will not trigger the error if the experimental [wsrep\_replicate\_myisam](galera-cluster-system-variables.md#wsrep_replicate_myisam) setting is `ON`. If set, should be set on all tables in the cluster. Affected DDL statements include: [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) (e.g. CREATE TABLE t1(a int) engine=Aria) [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) [TRUNCATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/table-statements/truncate-table)[CREATE VIEW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/views/create-view) [CREATE TRIGGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers/create-trigger) [CREATE INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-index) [DROP INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-definition/drop/drop-index) [RENAME TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/rename-table) [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table)\
  Statements in [procedures](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures), [events](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/event-scheduler), and [functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions) are permitted as the affected\
  tables are only known at execution. Furthermore, the various USER, ROLE, SERVER and\
  DATABASE statements are also allowed as they do not have an affected table. Deprecated in [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0) and removed in [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107). Use [wsrep\_mode=STRICT\_REPLICATION](galera-cluster-system-variables.md#wsrep_mode) instead.
* Commandline: `--wsrep-strict-ddl[={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)
* Deprecated: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.0)
* Removed: [MariaDB 10.7.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-release-notes)

#### `wsrep_sync_wait`

* Description: Setting this variable ensures causality checks will take place before executing an operation of the type specified by the value, ensuring that the statement is executed on a fully synced node. While the check is taking place, new queries are blocked on the node to allow the server to catch up with all updates made in the cluster up to the point where the check was begun. Once reached, the original query is executed on the node. This can result in higher latency. Note that when [wsrep\_dirty\_reads](galera-cluster-system-variables.md#wsrep_dirty_reads) is ON, values of wsrep\_sync\_wait become irrelevant. Sample usage (for a critical read that must have the most up-to-date data) `SET SESSION wsrep_sync_wait=1; SELECT ...; SET SESSION wsrep_sync_wait=0;`
  * `0` - Disabled (default)
  * `1` - READ (SELECT and BEGIN/START TRANSACTION). This is the same as [wsrep\_causal\_reads=1](galera-cluster-system-variables.md#wsrep_causal_reads).
  * `2` - UPDATE and DELETE;
  * `3` - READ, UPDATE and DELETE;
  * `4` - INSERT and REPLACE;
  * `5` - READ, INSERT and REPLACE;
  * `6` - UPDATE, DELETE, INSERT and REPLACE;
  * `7` - READ, UPDATE, DELETE, INSERT and REPLACE;
  * `8` - SHOW
  * `9` - READ and SHOW
  * `10` - UPDATE, DELETE and SHOW
  * `11` - READ, UPDATE, DELETE and SHOW
  * `12` - INSERT, REPLACE and SHOW
  * `13` - READ, INSERT, REPLACE and SHOW
  * `14` - UPDATE, DELETE, INSERT, REPLACE and SHOW
  * `15` - READ, UPDATE, DELETE, INSERT, REPLACE and SHOW
* Commandline: `--wsrep-sync-wait=`#
* Scope: Session
* Dynamic: Yes
* Data Type: Numeric
* Default Value: `0`
* Range:
  * `0` to `15`

#### `wsrep_trx_fragment_size`

* Description: Size of transaction fragments for streaming replication (measured in units as specified by [wsrep\_trx\_fragment\_unit](galera-cluster-system-variables.md#wsrep_trx_fragment_unit))
* Commandline: `--wsrep-trx-fragment-size=`#
* Scope: Session
* Dynamic: Yes
* Data Type: numeric
* Default Value: `0`
* Range: `0` to `2147483647`

#### `wsrep_trx_fragment_unit`

* Description: Unit for streaming replication transaction fragments' size:
  * `bytes`: transaction’s binlog events buffer size in bytes
  * `rows`: number of rows affected by the transaction
  * `statements`: number of SQL statements executed in the multi-statement transaction
* Commandline: `--wsrep-trx-fragment-unit=value`
* Scope: Session
* Dynamic: Yes
* Data Type: enum
* Default Value: `bytes`
* Valid Values: `bytes`, `rows` or `statements`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: Foreign Key
