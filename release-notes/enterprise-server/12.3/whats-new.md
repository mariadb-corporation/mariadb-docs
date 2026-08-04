---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Enterprise
  Server 12.3
hidden: true
---

# What's New in MariaDB Enterprise Server 12.3

{% include "../../.gitbook/includes/unreleased-es-12.3.md" %}

MariaDB Enterprise Server 12.3 is the next long-term release series, succeeding [MariaDB Enterprise Server 11.8](../11.8/whats-new.md). It adds the innovations from MariaDB Community Server 12.0 through 12.3 to Enterprise Server, together with three capabilities that are exclusive to Enterprise Server: MariaDB Advanced Cluster, Conflict Detection and Resolution triggers, and password-less authentication using TLS certificates.

Because Enterprise Server backports selected features between release series, a number of MariaDB 12.x features were already delivered in Enterprise Server 11.8 and are therefore not repeated here. See [What's New in MariaDB Enterprise Server 11.8](../11.8/whats-new.md) for those.

## Exclusive to MariaDB Enterprise Server

### MariaDB Advanced Cluster

MariaDB Advanced Cluster replaces the Galera replication provider with a provider built on the Raft consensus protocol, extended with certification. It is delivered as the `raft` plugin and is configured through its own set of system variables rather than through `wsrep_provider_options`:

```ini
plugin-load-add=raft
wsrep-provider=raft
```

The plugin adds `raft_*` system variables for node identity, quorum timeouts, flow control, event-store sizing, log durability, and TLS, along with `raft_*` status variables and a set of Information Schema tables for observability: `RAFT_CERT_FAILURES`, `RAFT_CLUSTER_CONNECTIONS`, `RAFT_TIMERS`, `RAFT_RPC_SENT`, `RAFT_LATENCY_STATS`, `RAFT_SERVER_INSTANCES`, `RAFT_FOLLOWER_INFO`, and `RAFT_STATUS`.

Advanced Cluster is built on Linux only. <!-- TODO: confirm which Linux distributions ship the plugin — the raft READMEs and the build configuration disagree (see DOCS-6353) -->

{% hint style="warning" %}
Advanced Cluster does not yet cover everything MariaDB Enterprise Cluster (Galera) does. Replication log encryption and the `galera_group_members` Performance Schema table are not implemented.
{% endhint %}

MariaDB Enterprise Server 12.3 ships Advanced Cluster 0.9.1. For configuration details, the full variable reference, and the current limitations, see the [Advanced Cluster documentation](../../advanced-cluster/README.md).

### Conflict Detection and Resolution triggers

Conflict Detection and Resolution (CDR) triggers provide a native way to resolve row-based replication conflicts on the replica, rather than stopping the SQL thread or skipping events manually ([MENT-2033](https://jira.mariadb.org/browse/MENT-2033)).

A CDR trigger is declared with `FOR CONFLICT` and one of five conflict types:

```sql
CREATE TRIGGER resolve_dup FOR CONFLICT INSERT_INSERT ON t1 FOR EACH ROW ...
```

| Conflict type | Fires when |
| ------------- | ---------- |
| `INSERT_INSERT` | The replicated insert collides with an existing row |
| `UPDATE_UPDATE` | The replicated update finds a row whose current state differs |
| `DELETE_UPDATE` | The replicated delete's target row differs on the replica |
| `UPDATE_DELETE` | The replicated update's target row is missing on the replica |
| `DELETE_DELETE` | The replicated delete's target row is missing on the replica |

When `slave_run_triggers_for_rbr` is enabled, the replica intercepts handler errors such as duplicate keys and missing rows and diverts execution to the matching CDR trigger. Inside the trigger, you can:

* Modify the `NEW` row image to instruct the applier to resolve the conflict
* Issue `SIGNAL SQLSTATE '02TRG'` to skip the event and continue
* Issue a custom error to deliberately stop the SQL thread

CDR triggers add a third row accessor, `ORG`, which exposes the primary's before-image as extracted from the replication event, so a trigger can compare what the primary expected to change against what the replica actually holds. `ORG` is read-only in all contexts. Accessor availability depends on the conflict type: `ORG` is unavailable for `INSERT_INSERT` conflicts, because an insert has no before-image, and `OLD` is unavailable for `UPDATE_DELETE` and `DELETE_DELETE` conflicts, because the row is absent from the replica.

{% hint style="info" %}
In this release, CDR triggers require `binlog_row_image=FULL`. They do not support system-versioned tables, and are not supported with a parallel replication mode above `OPTIMISTIC`. Behavior in combination with `slave_exec_mode=IDEMPOTENT` is unspecified.
{% endhint %}

### Password-less authentication with TLS certificates

A new `tls_certificate` authentication plugin authenticates a client solely from its TLS certificate, with no password involved ([MENT-2425](https://jira.mariadb.org/browse/MENT-2425)). The account must be created with a `REQUIRE SUBJECT` clause; the plugin rejects the connection if it was not, so the certificate subject remains the authoritative identity check:

```sql
CREATE USER 'appuser'@'%'
  IDENTIFIED VIA tls_certificate
  REQUIRE SUBJECT '/CN=appuser/O=Example Corp';
```

The plugin accepts any standard client authentication plugin, so no client-side change is required. It is built in by default.

## Security

* Support for passphrase-protected SSL keys, via the [ssl\_passphrase]({server}/security/encryption/data-in-transit-encryption/ssltls-system-variables#ssl_passphrase) system variable ([MDEV-14091](https://jira.mariadb.org/browse/MDEV-14091))
* New [SET SESSION AUTHORIZATION]({server}/reference/sql-statements/account-management-sql-statements/set-session-authorization) statement, for performing actions as another user ([MDEV-20299](https://jira.mariadb.org/browse/MDEV-20299))
* SHA-256 support for the [file\_key\_management]({server}/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin) encryption plugin ([MDEV-34712](https://jira.mariadb.org/browse/MDEV-34712))
* The [Hashicorp Key Management plugin]({server}/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin) can flush its cache to force key rotation ([MDEV-30847](https://jira.mariadb.org/browse/MDEV-30847))
* [DROP USER]({server}/reference/sql-statements/account-management-sql-statements/drop-user) now warns by default if the user has active sessions, and fails in Oracle mode ([MDEV-35617](https://jira.mariadb.org/browse/MDEV-35617))

## Compatibility Features

* Oracle [`TO_DATE()`]({server}/reference/sql-functions/date-time-functions/to_date) ([MDEV-19683](https://jira.mariadb.org/browse/MDEV-19683)), [`TO_NUMBER()`]({server}/reference/sql-functions/numeric-functions/to_number) ([MDEV-20022](https://jira.mariadb.org/browse/MDEV-20022)), and [`TRUNC()`]({server}/reference/sql-functions/date-time-functions/trunc) ([MDEV-20023](https://jira.mariadb.org/browse/MDEV-20023)) functions
* `( + )` outer join syntax in [Oracle mode]({server}/reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax#oracle-mode) ([MDEV-13817](https://jira.mariadb.org/browse/MDEV-13817))
* Support for [cursors]({server}/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors) on prepared statements ([MDEV-33830](https://jira.mariadb.org/browse/MDEV-33830))
* SQL standard [`SET PATH`]({server}/reference/sql-statements/administrative-sql-statements/set-commands/set-path) statement ([MDEV-34391](https://jira.mariadb.org/browse/MDEV-34391))
* SQL standard [`IS JSON`]({server}/reference/sql-structure/operators/comparison-operators/is-json) predicate ([MDEV-37072](https://jira.mariadb.org/browse/MDEV-37072))
* Basic [XML data type]({server}/reference/data-types/string-data-types/xmltype) ([MDEV-37261](https://jira.mariadb.org/browse/MDEV-37261))
* `UPDATE` and `DELETE` can read from a [common table expression]({server}/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions) ([MDEV-37220](https://jira.mariadb.org/browse/MDEV-37220))

## Optimizer Hints

MariaDB Enterprise Server 12.3 introduces [optimizer hints]({server}/ha-and-performance/optimization-and-tuning/optimizer-hints), which let a query override optimizer decisions inline:

* Query block naming and table-level hints: `QB_NAME`, `NO_RANGE_OPTIMIZATION`, `NO_ICP`, `MRR`/`NO_MRR`, `BKA`/`NO_BKA`, `BNL`/`NO_BNL` ([MDEV-35504](https://jira.mariadb.org/browse/MDEV-35504))
* Subquery hints: `SEMIJOIN`, `SUBQUERY` ([MDEV-34888](https://jira.mariadb.org/browse/MDEV-34888))
* Join order hints: `JOIN_FIXED_ORDER`, `JOIN_ORDER`, `JOIN_PREFIX`, `JOIN_SUFFIX` ([MDEV-34870](https://jira.mariadb.org/browse/MDEV-34870))
* Index-level hints: `[NO_]JOIN_INDEX`, `[NO_]GROUP_INDEX`, `[NO_]ORDER_INDEX`, `[NO_]INDEX` ([MDEV-35856](https://jira.mariadb.org/browse/MDEV-35856)), `[NO_]ROWID_FILTER` ([MDEV-36089](https://jira.mariadb.org/browse/MDEV-36089)), `[NO_]INDEX_MERGE` ([MDEV-36125](https://jira.mariadb.org/browse/MDEV-36125))
* `[NO_]SPLIT_MATERIALIZED` ([MDEV-36092](https://jira.mariadb.org/browse/MDEV-36092)), `[NO_]DERIVED_CONDITION_PUSHDOWN` and `[NO_]MERGE` ([MDEV-36106](https://jira.mariadb.org/browse/MDEV-36106))
* `MAX_EXECUTION_TIME` ([MDEV-34860](https://jira.mariadb.org/browse/MDEV-34860))
* Implicit query block names ([MDEV-37511](https://jira.mariadb.org/browse/MDEV-37511))

## Optimizer

* [Rowid Filtering]({server}/ha-and-performance/optimization-and-tuning/query-optimizations/rowid-filtering-optimization) can now be applied to reverse-ordered scans ([MDEV-36094](https://jira.mariadb.org/browse/MDEV-36094))
* [Index Condition Pushdown]({server}/ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown) can now be applied to reverse-ordered scans ([MDEV-34413](https://jira.mariadb.org/browse/MDEV-34413))
* Loose index scan ("use index for group-by") can now use indexes with `DESC` key parts ([MDEV-32732](https://jira.mariadb.org/browse/MDEV-32732))
* `GROUP BY` and `ORDER BY` optimizations can use indexes on virtual columns ([MDEV-36132](https://jira.mariadb.org/browse/MDEV-36132))
* The [optimizer trace]({server}/ha-and-performance/optimization-and-tuning/query-optimizer/optimizer-trace) can include table and view definitions, controlled by the [optimizer\_record\_context]({server}/server-management/variables-and-modes/server-system-variables#optimizer_record_context) system variable ([MDEV-36483](https://jira.mariadb.org/browse/MDEV-36483))
* The join optimizer can infer that a derived table with a `GROUP BY` clause has distinct `GROUP BY` columns ([MDEV-36321](https://jira.mariadb.org/browse/MDEV-36321))
* Reorderable [LEFT JOINs]({server}/reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax) are optimized ([MDEV-36055](https://jira.mariadb.org/browse/MDEV-36055))

## Binary Logging and Replication

* The binary log can be stored in InnoDB, removing the need to sync it and improving binary logging performance ([MDEV-34705](https://jira.mariadb.org/browse/MDEV-34705)). New system variables include [binlog\_storage\_engine]({server}/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_storage_engine), [binlog\_directory]({server}/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_directory), and [innodb\_binlog\_state\_interval]({server}/server-usage/storage-engines/innodb/innodb-system-variables#innodb_binlog_state_interval)
* Row replication events larger than `max_packet_size` are fragmented, controlled by [binlog\_row\_event\_fragment\_threshold]({server}/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_row_event_fragment_threshold) ([MDEV-32570](https://jira.mariadb.org/browse/MDEV-32570))
* Creation and use of temporary tables in replication is now predictable, via the [create\_tmp\_table\_binlog\_formats]({server}/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#create_tmp_table_binlog_formats) system variable ([MDEV-36099](https://jira.mariadb.org/browse/MDEV-36099))
* Configurable defaults for the `MASTER_SSL_*` settings used by `CHANGE MASTER` ([MDEV-28302](https://jira.mariadb.org/browse/MDEV-28302))
* [show\_slave\_auth\_info]({server}/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#show_slave_auth_info) and [replicate\_same\_server\_id]({server}/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#replicate_same_server_id) are now system variables, not just startup options
* The server reports whether it was started with the [skip-slave-start]({server}/server-management/starting-and-stopping-mariadb/mariadbd-options#skip-slave-start) option ([MDEV-27669](https://jira.mariadb.org/browse/MDEV-27669))

## MariaDB Enterprise Cluster (Galera)

* Asynchronous replication between two Galera clusters can use parallel replication, managed by `slave_parallel_threads` ([MDEV-20065](https://jira.mariadb.org/browse/MDEV-20065))
* Write sets can be retried on Galera nodes, controlled by the [wsrep\_applier\_retry\_count]({galera}/reference/galera-cluster-system-variables#wsrep_applier_retry_count) system variable ([MDEV-36077](https://jira.mariadb.org/browse/MDEV-36077))
* Needless foreign key checks during Incremental State Transfers are avoided ([MDEV-34822](https://jira.mariadb.org/browse/MDEV-34822))

## Stored Routines and Triggers

* Support for the predefined weak `SYS_REFCURSOR` cursor type ([MDEV-20034](https://jira.mariadb.org/browse/MDEV-20034))
* [Triggers]({server}/server-usage/triggers-events/triggers/create-trigger#trigger_event) can fire on multiple events ([MDEV-10164](https://jira.mariadb.org/browse/MDEV-10164))

## GIS

New GIS functions, improving compatibility with MySQL 8:

* [ST\_Validate]({server}/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_validate) ([MDEV-34137](https://jira.mariadb.org/browse/MDEV-34137)) and [ST\_IsValid]({server}/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_isvalid) ([MDEV-34276](https://jira.mariadb.org/browse/MDEV-34276))
* [ST\_Simplify]({server}/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_simplify) ([MDEV-34141](https://jira.mariadb.org/browse/MDEV-34141))
* [ST\_Collect]({server}/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_collect) ([MDEV-34278](https://jira.mariadb.org/browse/MDEV-34278))
* [MBRCoveredBy]({server}/reference/sql-statements/geometry-constructors/mbr-minimum-bounding-rectangle/mbrcoveredby) ([MDEV-34138](https://jira.mariadb.org/browse/MDEV-34138))
* Geohash functions: [ST\_GeoHash]({server}/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_geohash) ([MDEV-34158](https://jira.mariadb.org/browse/MDEV-34158)), [ST\_LatFromGeoHash]({server}/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_latfromgeohash) ([MDEV-34159](https://jira.mariadb.org/browse/MDEV-34159)), [ST\_LongFromGeoHash]({server}/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_longfromgeohash) ([MDEV-34160](https://jira.mariadb.org/browse/MDEV-34160)), [ST\_PointFromGeoHash]({server}/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_pointfromgeohash) ([MDEV-34277](https://jira.mariadb.org/browse/MDEV-34277))

## Observability and Information Schema

* New [INFORMATION\_SCHEMA.TRIGGERED\_UPDATE\_COLUMNS]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-triggered_update_columns) table ([MDEV-36996](https://jira.mariadb.org/browse/MDEV-36996))
* New [INFORMATION\_SCHEMA.PARAMETERS]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-parameters-table)`.PARAMETER_DEFAULT` column ([MDEV-37054](https://jira.mariadb.org/browse/MDEV-37054))
* Advanced Cluster adds `raft_*` status variables and the `RAFT_*` Information Schema tables described above

## Data Types and SQL

* New hash algorithms for [`PARTITION BY KEY`]({server}/server-usage/partitioning-tables/partitioning-types/key-partitioning-type) ([MDEV-9826](https://jira.mariadb.org/browse/MDEV-9826))
* [Foreign key]({server}/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys) constraint names now need to be unique per table rather than per database ([MDEV-28933](https://jira.mariadb.org/browse/MDEV-28933))
* The [depth limit of 32 on JSON functions]({server}/reference/error-codes/mariadb-error-codes-4000-to-4099/e4043) has been removed ([MDEV-32854](https://jira.mariadb.org/browse/MDEV-32854))

## Tool Improvements

* [mariadb-dump]({server}/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) supports wildcards with the `-L` or `--wildcards` option ([MDEV-21376](https://jira.mariadb.org/browse/MDEV-21376))
* [mariadb-check]({server}/clients-and-utilities/table-tools/mariadb-check) and [CHECK TABLE]({server}/reference/sql-statements/table-statements/check-table) support [SEQUENCE tables]({server}/server-usage/storage-engines/sequence-storage-engine) ([MDEV-22491](https://jira.mariadb.org/browse/MDEV-22491))
* The [mariadb client]({server}/clients-and-utilities/mariadb-client/mariadb-command-line-client#script-dir) can set an alternative directory for scripts invoked with the `source` command, using `--script-dir` ([MDEV-23818](https://jira.mariadb.org/browse/MDEV-23818))

## MariaDB Enterprise Audit

Two capabilities from the MariaDB Community audit plugin are now available in MariaDB Enterprise Audit:

* Connection records log the client port alongside the host, so a connection is identified as `HOST:PORT`. When no port is available, the field records `unavailable` ([MENT-2470](https://jira.mariadb.org/browse/MENT-2470), porting [MDEV-12182](https://jira.mariadb.org/browse/MDEV-12182))
* `CONNECT` events record the TLS version used for the connection ([MENT-2471](https://jira.mariadb.org/browse/MENT-2471), porting [MDEV-33834](https://jira.mariadb.org/browse/MDEV-33834))

## Enterprise Packaging and Upgrade

* `mariadb-upgrade` no longer runs when upgrading from Community Server to Enterprise Server of the same major version ([MENT-1712](https://jira.mariadb.org/browse/MENT-1712))
* Enterprise packages retain their Galera runtime dependencies, including `galera-enterprise-4` and the SST tools. MariaDB 12.3 removed the Galera package dependency from Community Server packages ([MDEV-38744](https://jira.mariadb.org/browse/MDEV-38744)); Enterprise Server maps them to the enterprise variants instead ([MENT-2706](https://jira.mariadb.org/browse/MENT-2706))

## Differences from MariaDB Community Server 12.3

MariaDB Enterprise Server 12.3 is not a rebuild of Community Server 12.3. The differences that matter most for this series:

| Capability | Enterprise Server 12.3 | Community Server 12.3 |
| ---------- | ---------------------- | --------------------- |
| MariaDB Advanced Cluster (`raft`) | Available | Not available |
| Conflict Detection and Resolution triggers | Available | Not available |
| `tls_certificate` authentication plugin | Available | Not available |
| MariaDB Enterprise Audit (`server_audit2`) | Available | Community audit plugin only |
| Videx storage engine | Not shipped ([MENT-2629](https://jira.mariadb.org/browse/MENT-2629)) | Available |
| Sphinx, OQGraph, Mroonga storage engines | Not shipped | Available |
| GitHub call-to-action message in the `mariadb` client | Suppressed ([MENT-2642](https://jira.mariadb.org/browse/MENT-2642)) | Shown ([MDEV-38328](https://jira.mariadb.org/browse/MDEV-38328)) |

For the full list of differences, see [MariaDB Enterprise Server Differences](../about/mariadb-enterprise-server-differences/README.md).

## New System and Status Variables

* [System Variables Added in Enterprise Server 12.3]({server}/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/enterprise-server/system-variables-added-in-enterprise-server-12.3)
* [Status Variables Added in Enterprise Server 12.3]({server}/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/enterprise-server/status-variables-added-in-enterprise-server-12.3)

## Incompatible Changes

Because MariaDB Enterprise Server 12.3 is the first long-term release series after Enterprise Server 11.8, the following backward-incompatible changes may affect an upgrade.

### New Reserved Words

The following keywords are now [reserved words]({server}/reference/sql-structure/sql-language-structure/reserved-words) and can no longer be used as [identifiers]({server}/reference/sql-structure/sql-language-structure/identifier-names) without being quoted:

* `CONVERSION`
* `ST_COLLECT`
* `TO_DATE`

### Removed System Variables

The following deprecated system variables have been removed:

* [big\_tables]({server}/server-management/variables-and-modes/server-system-variables#big_tables)
* [large\_page\_size]({server}/server-management/variables-and-modes/server-system-variables#large_page_size)
* [storage\_engine]({server}/server-management/variables-and-modes/server-system-variables#storage_engine)

### Replication

{% hint style="warning" %}
When a replica is upgraded to a MariaDB Enterprise Server 12.3 release built on MariaDB 12.3.2, the `CHANGE MASTER TO ... master_use_gtid` setting is not carried over and is reset to `DEFAULT`. After upgrading, re-apply `master_use_gtid` if you rely on it. Downgrading is not affected. The underlying fix landed in MariaDB 12.3.3 ([MDEV-39788](https://jira.mariadb.org/browse/MDEV-39788)).
{% endhint %}

## Available Versions

{% include "../../.gitbook/includes/all-releases-es-12.3.md" %}

See also: [All MariaDB Enterprise Releases](../all-releases.md)

## Installation Instructions

* [Deploy MariaDB Enterprise with Repositories]({server}/server-management/install-and-upgrade-mariadb/mariadb-package-repository-setup-and-usage)
* [Deploy MariaDB Enterprise with Package Tarballs]({server}/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/package-tarballs)
* [Deploy MariaDB Enterprise with Docker]({server}/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker)

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
