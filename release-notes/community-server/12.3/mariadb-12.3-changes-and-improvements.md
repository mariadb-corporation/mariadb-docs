---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Community
  Server 12.3
---

# MariaDB 12.3 Changes & Improvements

{% include "../../.gitbook/includes/latest-12-3.md" %}

MariaDB 12.3 is a [long term release](../about/release-model.md), maintained until June 2029. This page lists all changes and improvements added since [MariaDB 11.8](../11.8/what-is-mariadb-118.md), the previous LTS release.

## New Features

### Security <a href="#security" id="security"></a>

* Support for passphrase protected keys ([MDEV-14091](https://jira.mariadb.org/browse/MDEV-14091))
  * [ssl\_passphrase system](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/ssltls-system-variables#ssl_passphrase) variable
* New statement [SET SESSION AUTHORIZATION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-session-authorization) for performing actions as another user ([MDEV-20299](https://jira.mariadb.org/browse/MDEV-20299))
* Implement SHA2 (sha256) support for the [file\_key\_management.so](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin#current-greater-than-12.0.1) plugin (TDE) — `.so` is Linux only ([MDEV-34712](https://jira.mariadb.org/browse/MDEV-34712))

### Compatibility Features

* Oracle [`TO_DATE()`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/to_date) function ([MDEV-19683](https://jira.mariadb.com/browse/MDEV-19683))
* Support for [cursors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors) on prepared statements ([MDEV-33830](https://jira.mariadb.com/browse/MDEV-33830))
* SQL Standard [`SET PATH`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set-path) statement ([MDEV-34391](https://jira.mariadb.com/browse/MDEV-34391))
* SQL Standard [`IS JSON`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/operators/comparison-operators/is-json) predicate ([MDEV-37072](https://jira.mariadb.com/browse/MDEV-37072))
* Allow [`UPDATE`/`DELETE` to read from a CTE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions) ([MDEV-37220](https://jira.mariadb.com/browse/MDEV-37220))
* Basic [XML data type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/xmltype) ([MDEV-37261](https://jira.mariadb.com/browse/MDEV-37261))
* New authentication plugin [caching\_sha2\_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/clientserver-protocol/1-connecting/caching_sha2_password-authentication-plugin) for MySQL compatibility ([MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804))
* [( + ) for outer join syntax in Oracle mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax#oracle-mode) ([MDEV-13817](https://jira.mariadb.org/browse/MDEV-13817))
* Associative arrays: [DECLARE TYPE .. TABLE OF .. INDEX BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/declare-type) ([MDEV-34319](https://jira.mariadb.org/browse/MDEV-34319)) ([blog post](https://mariadb.org/bringing-oracles-associative-arrays-to-mariadb/))
* [DROP USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/drop-user) will now by default issue a warning if the user has active sessions, or fail in [Oracle mode](https://github.com/mariadb-corporation/mariadb-docs/blob/main/release-notes/about/compatibility-and-differences/sql_modeoracle.md) ([MDEV-35617](https://jira.mariadb.org/browse/MDEV-35617))
* Implement Oracle [TO\_NUMBER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/to_number) function ([MDEV-20022](https://jira.mariadb.org/browse/MDEV-20022))
* Implement Oracle [TRUNC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/trunc) function ([MDEV-20023](https://jira.mariadb.org/browse/MDEV-20023))

### Performance improvements <a href="#performance-improvements" id="performance-improvements"></a>

* Segmented key cache for [Aria storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) ([MDEV-24](https://jira.mariadb.org/browse/MDEV-24))
  * The new [aria\_pagecache\_segments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_pagecache_segments) system variable defines how many segments are used, default is `1`, maximum `128`
* MDL scalability improvements ([MDEV-19749](https://jira.mariadb.org/browse/MDEV-19749))
* Asynchronous replication between two [Galera Clusters](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) can now use parallel replication
  * This is managed by the [slave\_parallel\_threads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/high-availability/using-mariadb-replication-with-mariadb-galera-cluster/using-mariadb-replication-with-mariadb-galera-cluster-using-mariadb-replica#parallel-replication-support) system variable ([MDEV-20065](https://jira.mariadb.org/browse/MDEV-20065))
* The [audit plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) now supports buffered logging
  * The size of the buffer is defined using the new system variable [server\_audit\_file\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables#server_audit_file_buffer_size) ([MDEV-34680](https://jira.mariadb.org/browse/MDEV-34680))
* Faster [vector](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors) distance calculations via extrapolation ([MDEV-36205](https://jira.mariadb.org/browse/MDEV-36205))

### Audit Plugin <a href="#audit-plugin" id="audit-plugin"></a>

* The [Audit Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-overview) now logs HOST:PORT of incoming connections instead of just the host ([MDEV-1282](https://jira.mariadb.org/browse/MDEV-1282))
* Added [tls\_version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/ssltls-system-variables#tls_version) field for connection audit plugins ([MDEV-33834](https://jira.mariadb.org/browse/MDEV-33834))

### Configuration <a href="#configuration" id="configuration"></a>

* Get option group suffix from `$MARIADB_GROUP_SUFFIX` in addition to `$MYSQL_GROUP_SUFFIX` ([MDEV-21375](https://jira.mariadb.org/browse/MDEV-21375))

### Data types <a href="#data-types" id="data-types"></a>

* Comparison [ROW](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/row)(stored\_func(),1)=ROW(1,1) erroneously called stored\_func() twice per row. It led to a performance degradation, as well as to a double execution of the possible stored function side effects. ([MDEV-36322](https://jira.mariadb.org/browse/MDEV-36322))

### MariaDB Cluster (Galera) <a href="#galera" id="galera"></a>

* In [MariaDB Cluster (Galera)](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/), needless foreign key checks during Incremental State Transfers are now avoided ([MDEV-34822](https://jira.mariadb.org/browse/MDEV-34822))

### GIS <a href="#gis" id="gis"></a>

New [GIS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry/gis-features-in-533) functions. These functions improve compatibility with MySQL 8.

* [ST\_Validate](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_validate) ([MDEV-34137](https://jira.mariadb.org/browse/MDEV-34137))
* [MBRCoveredBy](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/mbr-minimum-bounding-rectangle/mbrcoveredby) ([MDEV-34138](https://jira.mariadb.org/browse/MDEV-34138))
* [ST\_Simplify](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_simplify) ([MDEV-34141](https://jira.mariadb.org/browse/MDEV-34141))
* [ST\_GeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_geohash) ([MDEV-34158](https://jira.mariadb.org/browse/MDEV-34158))
* [ST\_LatFromGeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_latfromgeohash) ([MDEV-34159](https://jira.mariadb.org/browse/MDEV-34159))
* [ST\_LongFromGeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_longfromgeohash) ([MDEV-34160](https://jira.mariadb.org/browse/MDEV-34160))
* [ST\_PointFromGeoHash](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_pointfromgeohash) ([MDEV-34277](https://jira.mariadb.org/browse/MDEV-34277))
* [ST\_IsValid](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_isvalid) ([MDEV-34276](https://jira.mariadb.org/browse/MDEV-34276))
* [ST\_Collect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/geometry-constructors/miscellaneous-gis-functions/st_collect) ([MDEV-34278](https://jira.mariadb.org/browse/MDEV-34278))

### mariadb Client

* Can set an alternative directory path for searching scripts invoked via the source command, with the [--script-dir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#script-dir) mariadb client option ([MDEV-23818](https://jira.mariadb.org/browse/MDEV-23818))

### Optimizer <a href="#optimizer" id="optimizer"></a>

* [Rowid Filtering](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/rowid-filtering-optimization) optimization can now be applied for reverse-ordered scans ([MDEV-36094](https://jira.mariadb.org/browse/MDEV-36094))
* [Index Condition Pushdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index-condition-pushdown) optimization can now applied for reverse-ordered scans ([MDEV-34413](https://jira.mariadb.org/browse/MDEV-34413))
* Loose Index Scan ("Use index for group-by") optimization can now use indexes with DESC key parts ([MDEV-32732](https://jira.mariadb.org/browse/MDEV-32732))
* find\_order\_in\_list mismatch when order item needs fixing() ([MDEV-36607](https://jira.mariadb.org/browse/MDEV-36607))
* If the join\_condition is specified via USING (column\_list), the query plan depends on the sequence of tables in the query ([MDEV-36592](https://jira.mariadb.org/browse/MDEV-36592))
* Optimizations for GROUP/ORDER BY can make use of indexes on virtual columns ([MDEV-36132](https://jira.mariadb.org/browse/MDEV-36132))
* Include definitions of tables and views in the [optimizer trace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizer/optimizer-trace) ([MDEV-36483](https://jira.mariadb.org/browse/MDEV-36483))
  * [optimizer\_record\_context](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_record_context) system variable.
* Join optimizer is now able to infer that derived table with GROUP BY clause has distinct GROUP BY columns ([MDEV-36321](https://jira.mariadb.org/browse/MDEV-36321))

### Optimizer hints <a href="#optimizer-hints" id="optimizer-hints"></a>

* Add support for [optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints) ([MDEV-35504](https://jira.mariadb.org/browse/MDEV-35504))
  * [QB\_NAME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#query-block-naming)
  * [NO\_RANGE\_OPTIMIZATION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#no_range_optimization)
  * [NO\_ICP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#no_icp)
  * [MRR, NO\_MRR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#mrr-and-no_mrr)
  * [BKA, NO\_BKA](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#bka-and-no_bka)
  * [BNL, NO\_BNL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#bnl-and-no_bnl)
* Add support for subquery optimizer hints ([MDEV-34888](https://jira.mariadb.org/browse/MDEV-34888))
  * [SEMIJOIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#semijoin-and-no_semijoin)
  * [SUBQUERY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#subquery-hint)
* Add support for join order hints ([MDEV-34870](https://jira.mariadb.org/browse/MDEV-34870))
  * [JOIN\_FIXED\_ORDER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints/expanded-optimizer-hints#join_fixed_order) similar to existing STRAIGHT\_JOIN hint
  * [JOIN\_ORDER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints/expanded-optimizer-hints#join_order) to apply the specified table order
  * [JOIN\_PREFIX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints/expanded-optimizer-hints#join_prefix) to hint what tables should be first in the join
  * [JOIN\_SUFFIX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints/expanded-optimizer-hints#join_suffix) to hint what tables should be last in the join
* Add support for the [MAX\_EXECUTION\_TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#max_execution_time) hint ([MDEV-34860](https://jira.mariadb.org/browse/MDEV-34860))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints): [\[NO\_\]JOIN\_INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#join_index-and-no_join_index), [\[NO\_\]GROUP\_INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#group_index-and-no_group_index), [\[NO\_\]ORDER\_INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#order_index-and-no_order_index), [\[NO\_\]INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#index-and-no_index) ([MDEV-35856](https://jira.mariadb.org/browse/MDEV-35856))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints): [\[NO\_\]SPLIT\_MATERIALIZED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#split_materialized-x-and-no_split_materialized-x) ([MDEV-36092](https://jira.mariadb.org/browse/MDEV-36092))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints): [\[NO\_\]DERIVED\_CONDITION\_PUSHDOWN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#derived_condition_pushdown-and-no_derived_condition_pushdown), [\[NO\_\]MERGE ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints#merge-and-no_merge)([MDEV-36106](https://jira.mariadb.org/browse/MDEV-36106))
* [Optimizer hint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints): [\[NO\_\]ROWID\_FILTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints/index-level-hints#rowid_filter-no_rowid_filter) ([MDEV-36089](https://jira.mariadb.org/browse/MDEV-36089)),
* [Optimizer hint](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints): [\[NO\_\]INDEX\_MERGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints/index-level-hints#index_merge-no_index_merge) ([MDEV-36125](https://jira.mariadb.org/browse/MDEV-36125))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimizer-hints): Implicit query block names ([MDEV-37511](https://jira.mariadb.org/browse/MDEV-37511))

### Replication

* Server displays if it was started with the [skip-slave-start](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#skip-slave-start) option ([MDEV-27669](https://jira.mariadb.org/browse/MDEV-27669))
* [show\_slave\_auth\_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#show_slave_auth_info) has been added as a system variable (previously it was just an option). It determines whether to show the user and password in [SHOW REPLICA HOSTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-hosts) (SHOW SLAVE HOSTS) on the primary.
* [replicate\_same\_server\_id](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#replicate_same_server_id) system variable added (previously it was just an option), which permits not skipping events having our server id.
* Ensure that creation and usage of temporary tables in replication is predictable ([MDEV-36099](https://jira.mariadb.org/browse/MDEV-36099))
  * [create\_tmp\_table\_binlog\_formats](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#create_tmp_table_binlog_formats) system variable.
* Configurable defaults for `MASTER_SSL_*` settings for `CHANGE MASTER` ([MDEV-28302](https://jira.mariadb.com/browse/MDEV-28302))
* Fragment ROW replication events larger than `max_packet_size` ([MDEV-32570](https://jira.mariadb.com/browse/MDEV-32570))
* Improving performance of binary logging by removing the need of syncing it ([MDEV-34705](https://jira.mariadb.com/browse/MDEV-34705))

### Stored Routines <a href="#stored-routines" id="stored-routines"></a>

* Add support for the pre-defined weak SYS\_REFCURSOR ([MDEV-20034](https://jira.mariadb.org/browse/MDEV-20034))
  * [max\_open\_cursors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#max_open_cursors) system variable limits the number of [cursors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors) opened at the same time

### Server <a href="#server" id="server"></a>

* Add the FM format to [TO\_CHAR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/to_char), which suppresses following padding ([MDEV-36216](https://jira.mariadb.org/browse/MDEV-36216))
* [mariadb-check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/table-tools/mariadb-check) and [CHECK TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) now support [SEQUENCE tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/sequence-storage-engine) ([MDEV-22491](https://jira.mariadb.org/browse/MDEV-22491))

### Trigger <a href="#trigger" id="trigger"></a>

* Add support for [TRIGGERS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers) that fire on multiple events ([MDEV-10164](https://jira.mariadb.org/browse/MDEV-10164))

### Miscellaneous

* [Hashicorp Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin): Implement cache flush for forced key rotation ([MDEV-30847](https://jira.mariadb.com/browse/MDEV-30847))
* New hash algorithms for [`PARTITION BY KEY`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/partitioning-tables/partitioning-types/key-partitioning-type) ([MDEV-9826](https://jira.mariadb.com/browse/MDEV-9826))
* Optimise reorderable [LEFT JOINs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins/join-syntax) ([MDEV-36055](https://jira.mariadb.com/browse/MDEV-36055))
* Retry applying of write sets on [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) nodes ([MDEV-36077](https://jira.mariadb.org/browse/MDEV-36077))
  * Controlled through the [wsrep\_applier\_retry\_count](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_applier_retry_count) system variable
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) now supports [wildcards](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#l-wildcards) with the `-L` or `--wildcards` option ([MDEV-21376](https://jira.mariadb.org/browse/MDEV-21376))
* [Foreign key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys) constraint names no longer need to be unique per database, only per table ([MDEV-28933](https://jira.mariadb.org/browse/MDEV-28933)) ([blog post](https://mariadb.org/per-table-unique-foreign-key-constraint-names-new-feature-in-mariadb-12-1/))
* Remove [depth limit of 32 from JSON functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/error-codes/mariadb-error-codes-4000-to-4099/e4043) ([MDEV-32854](https://jira.mariadb.org/browse/MDEV-32854))
* Add [INFORMATION\_SCHEMA.TRIGGERED\_UPDATE\_COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-triggered_update_columns) ([MDEV-36996](https://jira.mariadb.org/browse/MDEV-36996))
* Implement [INFORMATION\_SCHEMA.PARAMETERS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-parameters-table).PARAMETER\_DEFAULT column ([MDEV-37054](https://jira.mariadb.org/browse/MDEV-37054))

## Notable Items

### MariaDB Cluster (Galera)

* The Galera package dependency has been removed from server packages ([MDEV-38744](https://jira.mariadb.org/browse/MDEV-38744))

### Variables

For a list of all new variables added since MariaDB 11.8, see:

* [System Variables Added in MariaDB 12.0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-12.0)
* [System Variables Added in MariaDB 12.1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-12.1)
* [System Variables Added in MariaDB 12.2](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-12.2)
* [System Variables Added in MariaDB 12.3](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-12.3)

## Incompatible Changes

Since MariaDB 12.3 is the first long-term release after [MariaDB 11.8](../11.8/what-is-mariadb-118.md), the following backward-incompatible changes may affect an upgrade. For the full upgrade procedure, see [Upgrading from MariaDB 11.8 to MariaDB 12.3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-11-8-to-mariadb-12-3).

### New Reserved Words

The following keywords are now [reserved words](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/reserved-words). They can no longer be used as [identifiers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/identifier-names) without being quoted:

* `CONVERSION`
* `ST_COLLECT`
* `TO_DATE`

### Removed System Variables

The following deprecated system variables have been removed:

* [big\_tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#big_tables), deprecated in [MariaDB 10.5.0](../old-releases/10.5/10.5.0.md), removed in [MariaDB 12.0](../old-releases/12.0/what-is-mariadb-120.md)
* [large\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#large_page_size), deprecated in [MariaDB 10.5.3](../old-releases/10.5/10.5.3.md), removed in [MariaDB 12.0](../old-releases/12.0/what-is-mariadb-120.md)
* [storage\_engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#storage_engine), deprecated in [MariaDB 5.5](../old-releases/5.5/changes-improvements-in-mariadb-5-5.md), removed in [MariaDB 12.0](../old-releases/12.0/what-is-mariadb-120.md)

### Replication

* When upgrading a replica from a pre-12.3 release to MariaDB 12.3, the `CHANGE MASTER TO ... master_use_gtid` setting is not currently carried over and is reset to `DEFAULT` ([MDEV-39788](https://jira.mariadb.org/browse/MDEV-39788)). After upgrading, re-apply `master_use_gtid` if you rely on it. Downgrading is not affected. See [Upgrading from MariaDB 11.8 to MariaDB 12.3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-11-8-to-mariadb-12-3) for details.

## Security Vulnerabilities Fixed in MariaDB 12.3

For a complete list of security vulnerabilities (CVEs) fixed across all versions of MariaDB Community Server, see the [Security Vulnerabilities Fixed in MariaDB Community Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/cve/community-server) page.

| CVE ID (with cve.org link)                                        | CVSS base score (v3.1) | Community Server 12.3 Release |
| ----------------------------------------------------------------- | ---------------------- | ----------------------------- |
| [CVE-2026-44173](https://www.cve.org/CVERecord?id=CVE-2026-44173) | 5.0                    | [MariaDB 12.3.2](12.3.2.md)   |
| [CVE-2026-44172](https://www.cve.org/CVERecord?id=CVE-2026-44172) | 5.0                    | [MariaDB 12.3.2](12.3.2.md)   |
| [CVE-2026-44171](https://www.cve.org/CVERecord?id=CVE-2026-44171) | 6.3                    | [MariaDB 12.3.2](12.3.2.md)   |
| [CVE-2026-44170](https://www.cve.org/CVERecord?id=CVE-2026-44170) | 5.0                    | [MariaDB 12.3.2](12.3.2.md)   |
| [CVE-2026-44169](https://www.cve.org/CVERecord?id=CVE-2026-44169) | 4.3                    | [MariaDB 12.3.2](12.3.2.md)   |
| [CVE-2026-44168](https://www.cve.org/CVERecord?id=CVE-2026-44168) | 8.0                    | [MariaDB 12.3.2](12.3.2.md)   |

## List of All MariaDB 12.3 Releases

| Date        | Release              | Status      | Release Notes              | Changelog                                 |
| ----------- | -------------------- | ----------- | -------------------------- | ----------------------------------------- |
| 28 May 2026 | 12.3.2               | Stable (GA) | [Release Notes](12.3.2.md) | [Changelog](../changelogs/12.3/12.3.2.md) |
| 12 Feb 2026 | 12.3.1               | RC          | [Release Notes](12.3.1.md) | [Changelog](../changelogs/12.3/12.3.1.md) |
| 22 Dec 2025 | MariaDB 12.3 Preview | Preview     |                            |                                           |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
