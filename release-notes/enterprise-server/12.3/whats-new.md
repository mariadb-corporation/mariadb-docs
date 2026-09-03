---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Enterprise
  Server 12.3
hidden: true
---

# What's New in MariaDB Enterprise Server 12.3

{% include "../../.gitbook/includes/unreleased-es-12.3.md" %}

MariaDB Enterprise Server 12.3 is the next long-term release series, succeeding [MariaDB Enterprise Server 11.8](../11.8/whats-new.md). It brings the innovations of MariaDB Community Server 12.0 through 12.3 to Enterprise Server, and adds three capabilities that exist only in Enterprise Server: MariaDB Advanced Cluster, Conflict Detection and Resolution triggers, and password-less authentication using TLS certificates.

Because Enterprise Server backports selected features between release series, a number of MariaDB 12.x features were already delivered in Enterprise Server 11.8 and are not repeated here. See [What's New in MariaDB Enterprise Server 11.8](../11.8/whats-new.md) for those.

## Exclusive to MariaDB Enterprise Server

### MariaDB Advanced Cluster

MariaDB Advanced Cluster is a new clustering option that replaces the Galera replication provider with one built on the Raft consensus protocol, extended with certification. Where MariaDB Enterprise Cluster (Galera) relies on a certification-based provider tuned through `wsrep_provider_options`, Advanced Cluster is delivered as the `raft` plugin and is configured entirely through its own system variables.

Enable it by loading the plugin and selecting it as the replication provider:

```ini
plugin-load-add=raft
wsrep-provider=raft
```

The listen address is taken from `wsrep_node_address` by default. If that variable does not specify a port, or is autodetected, the `raft_listen_port` variable determines the port instead.

Advanced Cluster adds its own configuration and observability surface:

* **Node identity and quorum**: each node takes a unique identifier, and election and heartbeat behavior is controlled by a set of timeout variables
* **Flow control**: the leader throttles requests when nodes drift too far apart in commit position
* **Event store**: replication logs are held in a sized in-memory buffer backed by on-disk files, with configurable durability
* **TLS**: cluster communication can be secured independently of client connections, with its own certificate, key, CA, cipher, and verification settings
* **Status variables**: `raft_*` status variables report the current leader, term, log index, and flow-control activity
* **Information Schema tables**: `RAFT_CERT_FAILURES`, `RAFT_CLUSTER_CONNECTIONS`, `RAFT_TIMERS`, `RAFT_RPC_SENT`, `RAFT_LATENCY_STATS`, `RAFT_SERVER_INSTANCES`, `RAFT_FOLLOWER_INFO`, and `RAFT_STATUS`

Advanced Cluster is built on Linux only. <!-- TODO: confirm which Linux distributions ship the plugin — the raft READMEs and the build configuration disagree (see DOCS-6353) -->

{% hint style="warning" %}
Advanced Cluster does not yet cover everything MariaDB Enterprise Cluster (Galera) does. Replication log encryption and the `galera_group_members` Performance Schema table are not implemented.
{% endhint %}

MariaDB Enterprise Server 12.3 ships Advanced Cluster 0.9.1. For configuration details, the full variable reference, and current limitations, see the [Advanced Cluster documentation](../../advanced-cluster/README.md).

### Conflict Detection and Resolution triggers

When a replica applies row-based replication events, a row may not be in the state the primary expected — because it was changed locally, already deleted, or already inserted by another source. Traditionally the replica had two options: stop the SQL thread, or skip the event and accept divergence.

Conflict Detection and Resolution (CDR) triggers give you a third option: resolve the conflict on the replica, in SQL, as it happens. A CDR trigger is declared with `FOR CONFLICT` and one of five conflict types:

```sql
CREATE TRIGGER resolve_dup FOR CONFLICT INSERT_INSERT ON t1 FOR EACH ROW
BEGIN
  -- inspect ORG and OLD, then set NEW to the winning row
END;
```

The conflict type selects which divergence the trigger handles:

| Conflict type | Fires when |
| ------------- | ---------- |
| `INSERT_INSERT` | A replicated insert collides with a row that already exists on the replica |
| `UPDATE_UPDATE` | A replicated update finds its target row in a different state than the primary had |
| `DELETE_UPDATE` | A replicated delete finds its target row in a different state than the primary had |
| `UPDATE_DELETE` | A replicated update's target row is missing from the replica |
| `DELETE_DELETE` | A replicated delete's target row is missing from the replica |

When `slave_run_triggers_for_rbr` is enabled, the replica intercepts handler errors such as duplicate keys and missing rows and diverts execution to the matching CDR trigger. Inside the trigger you have three ways to conclude:

* **Resolve it** — modify the `NEW` row image, and the applier writes or updates that row
* **Skip it** — issue `SIGNAL SQLSTATE '02TRG'` to ignore the conflict and continue applying
* **Stop** — raise a custom error to halt the SQL thread deliberately, for conflicts that need a human

To make resolution decisions possible, CDR triggers introduce a third row accessor alongside `OLD` and `NEW`:

* **`ORG`** is the primary's before-image, taken from the replication event. It shows the state the primary expected to modify, so a trigger can compare the primary's assumption against what the replica actually holds
* `ORG` is read-only in every context
* `ORG` is unavailable in `INSERT_INSERT` conflicts, because an insert has no before-image
* `OLD` is unavailable in `UPDATE_DELETE` and `DELETE_DELETE` conflicts, because the row is not present on the replica

{% hint style="info" %}
In this release, CDR triggers require `binlog_row_image=FULL`. They do not support system-versioned tables and are not supported with a parallel replication mode above `OPTIMISTIC`. Behavior in combination with `slave_exec_mode=IDEMPOTENT` is unspecified.
{% endhint %}

### Password-less authentication with TLS certificates

Deployments that already issue client certificates can now authenticate users from the certificate alone, with no password stored on the server or sent over the wire. The new `tls_certificate` authentication plugin does exactly that.

The account must carry a `REQUIRE SUBJECT` clause. The plugin rejects any connection for an account created without one, so the certificate subject always remains the authoritative identity check:

```sql
CREATE USER 'appuser'@'%'
  IDENTIFIED VIA tls_certificate
  REQUIRE SUBJECT '/CN=appuser/O=Example Corp';
```

The plugin is built in by default and accepts any standard client authentication plugin, so existing clients and connectors need no change.

## Security

* **Passphrase-protected SSL keys**: a private key protected by a passphrase can now be used, with the passphrase supplied through the [ssl\_passphrase](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/ssltls-system-variables#ssl_passphrase) system variable
* **New** [**SET SESSION AUTHORIZATION**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-session-authorization) **statement**: perform work as another user within a session, which is useful for administrative tooling and for reproducing a user's privileges:

    ```sql
    SET SESSION AUTHORIZATION foo@bar;
    ```

  * Switching to another account requires the `SET USER` privilege; switching to your own account needs no privilege
  * The statement is not permitted inside stored procedures
* **SHA-256 for File Key Management**: the [file\_key\_management](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) encryption plugin supports SHA-256 digests
* **Forced key rotation for HashiCorp**: the [Hashicorp Key Management plugin](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin) can flush its key cache, so a rotation performed in Vault takes effect without a restart
* **Safer** [**DROP USER**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/drop-user): dropping an account that still has active sessions now raises a warning by default, and fails outright in Oracle mode

## Compatibility Features

* **Oracle date and number functions**: [`TO_DATE()`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/to_date), [`TO_NUMBER()`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/to_number), and [`TRUNC()`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/trunc) reduce the rewriting needed when migrating Oracle SQL
* **Oracle outer join syntax**: the `( + )` operator is accepted in [Oracle mode](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax#oracle-mode), so legacy queries port across unchanged
* **Cursors on prepared statements**: a [cursor](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors) can now be opened over a prepared statement, allowing the query text to be built at runtime
* **SQL standard** [**SET PATH**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set-path): sets the schema search path used to resolve unqualified stored routine names:

    ```sql
    SET PATH 'schema_a,schema_b';
    ```
* **SQL standard** [**IS JSON**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/is-json) **predicate**: tests whether a value is valid JSON, without a function call:

    ```sql
    SELECT '[1, 2]' IS JSON;
    SELECT '{"key1":1, "key2":[2,3]}' IS JSON;
    ```
* **Basic** [**XML data type**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/xmltype): a dedicated type for XML documents, improving Oracle compatibility
* [**Common table expressions in UPDATE and DELETE**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions): `UPDATE` and `DELETE` can read from a CTE, so a computed row set can drive a modification without a temporary table

## Optimizer Hints

MariaDB Enterprise Server 12.3 introduces [optimizer hints](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints), which let a single query override optimizer decisions without changing server-wide settings. Hints are written as comments immediately after the statement keyword:

```sql
SELECT /*+ MAX_EXECUTION_TIME(1000) NO_ICP(t1) */ * FROM t1 WHERE ...;
```

The available hints cover:

* **Query block naming**: `QB_NAME` labels a query block so other hints can target it, including implicit names for unlabeled blocks
* **Access and join methods**: `NO_RANGE_OPTIMIZATION`, `NO_ICP`, `MRR`/`NO_MRR`, `BKA`/`NO_BKA`, `BNL`/`NO_BNL`
* **Join order**: `JOIN_FIXED_ORDER` pins the order as written, while `JOIN_ORDER`, `JOIN_PREFIX`, and `JOIN_SUFFIX` constrain it partially
* **Index selection**: `[NO_]INDEX`, `[NO_]JOIN_INDEX`, `[NO_]GROUP_INDEX`, `[NO_]ORDER_INDEX`, `[NO_]INDEX_MERGE`, and `[NO_]ROWID_FILTER`
* **Subquery strategy**: `SEMIJOIN` and `SUBQUERY` choose how a subquery is executed
* **Derived tables**: `[NO_]SPLIT_MATERIALIZED`, `[NO_]DERIVED_CONDITION_PUSHDOWN`, and `[NO_]MERGE`
* **Execution time**: `MAX_EXECUTION_TIME` caps how long a statement may run

## Optimizer

* **Reverse-ordered scans use more optimizations**: [Rowid Filtering](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/rowid-filtering-optimization) and [Index Condition Pushdown](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown) now apply to descending scans, so `ORDER BY ... DESC` queries benefit from the same filtering as ascending ones
* **Loose index scan with descending keys**: the "use index for group-by" optimization can use indexes that declare `DESC` key parts
* **Indexes on virtual columns**: `GROUP BY` and `ORDER BY` can be satisfied from an index built on a virtual column
* **Richer optimizer trace**: the [optimizer trace](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizer/optimizer-trace) can include the definitions of the tables and views involved, controlled by the [optimizer\_record\_context](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_record_context) system variable — useful when a plan has to be diagnosed from a trace alone
* **Better derived table estimates**: the join optimizer recognizes that a derived table with a `GROUP BY` clause produces distinct grouping columns, which sharpens cardinality estimates
* **Reorderable LEFT JOINs**: [outer joins](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax) that can safely be reordered are now considered for reordering

## Binary Logging and Replication

* **Storage-engine-integrated binary log**: a more efficient binary log implementation that uses InnoDB internals to write the binary log rather than syncing a separate file, which removes the binary log's own fsync from the commit path. It is selected at startup with the read-only [binlog\_storage\_engine](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_storage_engine) option and is only available for engines that support it. Related settings are [binlog\_directory](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_directory) and [innodb\_binlog\_state\_interval](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_binlog_state_interval)
* **Fragmented row events**: row events larger than `max_packet_size` are split rather than failing, controlled by [binlog\_row\_event\_fragment\_threshold](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_event_fragment_threshold)
* **Predictable temporary tables in replication**: [create\_tmp\_table\_binlog\_formats](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#create_tmp_table_binlog_formats) makes the binary logging of temporary table creation and use explicit rather than format-dependent
* **Configurable replication TLS defaults**: the `MASTER_SSL_*` settings used by `CHANGE MASTER` can be given server defaults, so each replica does not have to repeat them
* **More settings promoted to system variables**: [show\_slave\_auth\_info](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#show_slave_auth_info) and [replicate\_same\_server\_id](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#replicate_same_server_id) were previously startup options only, and can now be inspected as system variables
* **Visible skip-slave-start**: the server reports whether it was started with the [skip-slave-start](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#skip-slave-start) option, removing a common source of confusion when a replica does not begin applying

## MariaDB Enterprise Cluster (Galera)

* **Parallel replication between clusters**: asynchronous replication from one Galera cluster to another can apply in parallel, managed by `slave_parallel_threads`
* **Write set retry**: a write set that fails to apply can be retried rather than immediately aborting the node, controlled by the [wsrep\_applier\_retry\_count](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_applier_retry_count) system variable
* **Faster Incremental State Transfers**: unnecessary foreign key checks during an IST are avoided

## Stored Routines and Triggers

* **Weak `SYS_REFCURSOR` cursor type**: a cursor can be held in a variable and passed between routines, which is the Oracle idiom for returning a result set from a procedure:

    ```sql
    DECLARE c0 SYS_REFCURSOR;
    ```

  * The number of simultaneously open cursors is bounded by the `max_open_cursors` system variable
* **Triggers on multiple events**: one [trigger](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers/create-trigger#trigger_event) body can serve several events, instead of duplicating it once per event:

    ```sql
    CREATE TRIGGER audit_t1 BEFORE INSERT OR UPDATE OR DELETE ON t1 FOR EACH ROW ...
    ```

## GIS

Nine new GIS functions improve compatibility with MySQL 8:

* [ST\_Validate](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_validate) returns the geometry if it is valid, and `NULL` otherwise
* [ST\_IsValid](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_isvalid) tests a geometry for validity
* [ST\_Simplify](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_simplify) reduces the number of points in a geometry within a given tolerance
* [ST\_Collect](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_collect) aggregates several geometries into one collection
* [MBRCoveredBy](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/mbr-minimum-bounding-rectangle/mbrcoveredby) tests whether one minimum bounding rectangle is covered by another
* [ST\_GeoHash](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_geohash) encodes a point as a geohash string
* [ST\_LatFromGeoHash](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_latfromgeohash) and [ST\_LongFromGeoHash](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_longfromgeohash) decode the latitude and longitude from a geohash
* [ST\_PointFromGeoHash](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_pointfromgeohash) decodes a geohash back into a point

## MariaDB Enterprise Audit

Two capabilities from the MariaDB Community audit plugin are now available in MariaDB Enterprise Audit:

* **Client port in connection records**: a connection is identified as `HOST:PORT` rather than by host alone, which distinguishes concurrent connections from the same host. When no port is available, the field records `unavailable`
* **TLS version in `CONNECT` events**: each connection event records the TLS version negotiated, so audit logs can evidence which sessions used which protocol version

## Observability and Information Schema

* **New** [**INFORMATION\_SCHEMA.TRIGGERED\_UPDATE\_COLUMNS**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-triggered_update_columns) **table**: reports which columns a trigger is defined to fire on
* **New** [**INFORMATION\_SCHEMA.PARAMETERS**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-parameters-table)`.PARAMETER_DEFAULT` **column**: exposes the default value of a stored routine parameter
* **Advanced Cluster observability**: `raft_*` status variables and the `RAFT_*` Information Schema tables described above

## Data Types and SQL

* **New hash algorithms for** [**PARTITION BY KEY**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/partitioning-tables/partitioning-types/key-partitioning-type): improves distribution across partitions
* **Per-table foreign key constraint names**: a [foreign key](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys) constraint name now needs to be unique only within its table rather than across the whole database, which removes a frequent obstacle when consolidating schemas
* **No depth limit on JSON functions**: the [previous limit of 32 levels](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/error-codes/mariadb-error-codes-4000-to-4099/e4043) has been removed, so deeply nested documents can be processed

## Tool Improvements

* [**mariadb-dump**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump): the `-L` or `--wildcards` option selects databases and tables by pattern rather than by exact name
* [**mariadb-check**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check) **and** [**CHECK TABLE**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table): both now support [SEQUENCE tables](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/sequence-storage-engine)
* [**mariadb client**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#script-dir): the `--script-dir` option sets an alternative directory for scripts invoked with the `source` command

## Enterprise Packaging and Upgrade

* **Simpler Community-to-Enterprise upgrades**: `mariadb-upgrade` no longer runs when moving from Community Server to Enterprise Server of the same major version, since the data directory format is unchanged
* **Galera runtime dependencies retained**: MariaDB 12.3 removed the Galera package dependency from Community Server packages. Enterprise Server packages instead map those dependencies to their enterprise variants, including `galera-enterprise-4` and the SST tools, so an Enterprise Cluster deployment still installs what it needs

## Differences from MariaDB Community Server 12.3

MariaDB Enterprise Server 12.3 is not a rebuild of Community Server 12.3. The differences that matter most for this series:

| Capability | Enterprise Server 12.3 | Community Server 12.3 |
| ---------- | ---------------------- | --------------------- |
| MariaDB Advanced Cluster (`raft`) | Available | Not available |
| Conflict Detection and Resolution triggers | Available | Not available |
| `tls_certificate` authentication plugin | Available | Not available |
| MariaDB Enterprise Audit (`server_audit2`) | Available | Community audit plugin only |
| Videx storage engine | Not shipped | Available |
| Sphinx, OQGraph, Mroonga storage engines | Not shipped | Available |
| GitHub call-to-action message in the `mariadb` client | Suppressed | Shown |

For the full list of differences, see [MariaDB Enterprise Server Differences](../about/mariadb-enterprise-server-differences/README.md).

## New System and Status Variables

* [System Variables Added in Enterprise Server 12.3](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/enterprise-server/system-variables-added-in-enterprise-server-12.3)
* [Status Variables Added in Enterprise Server 12.3](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/enterprise-server/status-variables-added-in-enterprise-server-12.3)

## Incompatible Changes

Because MariaDB Enterprise Server 12.3 is the first long-term release series after Enterprise Server 11.8, the following backward-incompatible changes may affect an upgrade.

### New Reserved Words

The following keywords are now [reserved words](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/reserved-words) and can no longer be used as [identifiers](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/identifier-names) without being quoted:

* `CONVERSION`
* `ST_COLLECT`
* `TO_DATE`

### Removed System Variables

The following deprecated system variables have been removed:

* [big\_tables](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#big_tables)
* [large\_page\_size](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#large_page_size)
* [storage\_engine](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#storage_engine)

## Available Versions

{% include "../../.gitbook/includes/all-releases-es-12.3.md" %}

See also: [All MariaDB Enterprise Releases](../all-releases.md)

## Installation Instructions

* [Deploy MariaDB Enterprise with Repositories](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage)
* [Deploy MariaDB Enterprise with Package Tarballs](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/package-tarballs)
* [Deploy MariaDB Enterprise with Docker](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker)

## What's new in older release series

* [What's New in MariaDB Enterprise Server 11.8](../11.8/whats-new.md)
* [What's New in MariaDB Enterprise Server 11.4](../11.4/whats-new.md)
* [What's New in MariaDB Enterprise Server 10.6](../10.6/whats-new.md)
* [What's New in MariaDB Enterprise Server 10.5](../old-releases/10.5/whats-new-in-mariadb-enterprise-server-10-5.md)
* [What's New in MariaDB Enterprise Server 10.4](../old-releases/10.4/whats-new-in-mariadb-enterprise-server-10-4.md)
* [What's New in MariaDB Enterprise Server 10.3](../old-releases/10.3/whats-new-in-mariadb-enterprise-server-10-3.md)
* [What's New in MariaDB Enterprise Server 10.2](../old-releases/10.2/whats-new-in-mariadb-enterprise-server-10-2.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
