# MariaDB 12.1 Changes & Improvements

{% include "../../.gitbook/includes/latest-12-1.md" %}

MariaDB 12.1 is a [rolling release](../about/release-model.md). It is an evolution of [MariaDB 12.0](../release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120.md) with several entirely new features.

## New Features

### Performance improvements <a href="#performance-improvements" id="performance-improvements"></a>

* Segmented key cache for [Aria storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) ([MDEV-24](https://jira.mariadb.org/browse/MDEV-24))
  * [aria\_pagecache\_segments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_pagecache_segments) system variable
* MDL scalability improvements ([MDEV-19749](https://jira.mariadb.org/browse/MDEV-19749))
* Parallel replication for [Galera](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) replicas ([MDEV-20065](https://jira.mariadb.org/browse/MDEV-20065))
* Buffered logging for [audit plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) ([MDEV-34680](https://jira.mariadb.org/browse/MDEV-34680))
* Faster [vector](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/vectors) distance calculations via extrapolation ([MDEV-36205](https://jira.mariadb.org/browse/MDEV-36205))

### Compatibility features <a href="#compatibility-features" id="compatibility-features"></a>

* caching\_sha2\_password plugin ([MDEV-9804](https://jira.mariadb.org/browse/MDEV-9804))
* [( + ) for outer join syntax in Oracle mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/join-syntax#oracle-mode) ([MDEV-13817](https://jira.mariadb.org/browse/MDEV-13817))
* Add [semisynchronous replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication) variable, [rpl\_semi\_sync\_master\_wait\_for\_slave\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication#rpl_semi_sync_master_wait_for_slave_count) ([MDEV-18983](https://jira.mariadb.org/browse/MDEV-18983))
* Associative arrays: DECLARE TYPE .. TABLE OF .. INDEX BY ([MDEV-34319](https://jira.mariadb.org/browse/MDEV-34319)) ([blog post](https://mariadb.org/bringing-oracles-associative-arrays-to-mariadb/))
* [DROP USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/drop-user) will now by default issue a warning if the user has active sessions, or fail in [Oracle mode](../about/compatibility-and-differences/sql_modeoracle.md) ([MDEV-35617](https://jira.mariadb.org/browse/MDEV-35617))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): [\[NO\_\]JOIN\_INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints#join_index-and-no_join_index), [\[NO\_\]GROUP\_INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints#group_index-and-no_group_index), [\[NO\_\]ORDER\_INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints#order_index-and-no_order_index), [\[NO\_\]INDEX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints#index-and-no_index) ([MDEV-35856](https://jira.mariadb.org/browse/MDEV-35856))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): [\[NO\_\]SPLIT\_MATERIALIZED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints#split_materialized-x-and-no_split_materialized-x) ([MDEV-36092](https://jira.mariadb.org/browse/MDEV-36092))
* [Optimizer hints](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints): [\[NO\_\]DERIVED\_CONDITION\_PUSHDOWN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/optimizer-hints#derived_condition_pushdown-and-no_derived_condition_pushdown), \[NO\_]MERGE ([MDEV-36106](https://jira.mariadb.org/browse/MDEV-36106))

### Miscellaneous <a href="#miscellaneous" id="miscellaneous"></a>

* Retry applying of write sets on galera nodes ([MDEV-36077](https://jira.mariadb.org/browse/MDEV-36077))
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) now supports [wildcards](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump#l-wildcards) with the `-L` or `--wildcards` option ([MDEV-21376](https://jira.mariadb.org/browse/MDEV-21376))
* Per-table unique FOREIGN KEY constraint names ([MDEV-28933](https://jira.mariadb.org/browse/MDEV-28933)) ([blog post](https://mariadb.org/per-table-unique-foreign-key-constraint-names-new-feature-in-mariadb-12-1/))
* Support for functional indexes in GROUP/ORDER BY ([MDEV-36132](https://jira.mariadb.org/browse/MDEV-36132))
* Include definitions of tables and views in the [optimizer trace](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/mariadb-internals-documentation-optimizer-trace) ([MDEV-36483](https://jira.mariadb.org/browse/MDEV-36483))
  * [optimizer\_record\_context](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#optimizer_record_context) system variable.

## List of All MariaDB 12.1 Releases

| Date         | Release                                           | Status  | Release Notes                                    | Changelog                                                                             |
| ------------ | ------------------------------------------------- | ------- | ------------------------------------------------ | ------------------------------------------------------------------------------------- |
| 7 Aug 2025   | [MariaDB 12.1.1](mariadb-12.1.1-release-notes.md) | RC      | [Release Notes](mariadb-12.1.1-release-notes.md) | [Changelog](../changelogs/changelogs-mariadb-12.1-series/mariadb-12.1.1-changelog.md) |
| 26 June 2025 | MariaDB 12.1.0                                    | Preview |                                                  |                                                                                       |

***

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
