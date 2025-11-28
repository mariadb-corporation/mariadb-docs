# MariaDB 10.3.3 Release Notes

The most recent release of [MariaDB 10.3](what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.3) | [Release Notes](mariadb-1033-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1033-changelog.md) | [Overview of 10.3](what-is-mariadb-103.md)

**Release date:** 23 Dec 2017

[MariaDB 10.3](what-is-mariadb-103.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.2](../release-notes-mariadb-10-2-series/what-is-mariadb-102.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.3.3](mariadb-1033-release-notes.md) is a [_**Beta**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.3**](what-is-mariadb-103.md) **see the**[**What is MariaDB 10.3?**](what-is-mariadb-103.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

This is the first beta release in the [MariaDB 10.3](what-is-mariadb-103.md) series.

Notable changes of this release include:

## General

* [Table Value Constructors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/table-value-constructors). As a result, the [VALUES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/values-value) function has been renamed to `VALUE()` ([MDEV-12172](https://jira.mariadb.org/browse/MDEV-12172)) — GSoC 2017 project by Galina Shalygina
* [Transform \[NOT\] IN predicate with long list of values INTO \[NOT\] IN subquery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/conversion-of-big-in-predicates-into-subqueries) ([MDEV-12176](https://jira.mariadb.org/browse/MDEV-12176)) — GSoC 2017 project by Galina Shalygina
* [ROW TYPE OF](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/declare-variable#type-of-row-type-of) now supports local SP variables ([MDEV-14139](https://jira.mariadb.org/browse/MDEV-14139))
* [Aggregate stored functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-functions/stored-aggregate-functions) ([MDEV-7773](https://jira.mariadb.org/browse/MDEV-7773)) — GSoC 2016 project by Varun Gupta
* [OQGraph](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/oqgraph-storage-engine) supports "leaves" algorithm ([MDEV-11271](https://jira.mariadb.org/browse/MDEV-11271)) — contribution by Heinz Wiesinger
* Support for [LIMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/limit) clause in [GROUP\_CONCAT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/aggregate-functions/group_concat) ([MDEV-11297](https://jira.mariadb.org/browse/MDEV-11297))
* [PERCENTILE\_CONT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percentile_cont), [PERCENTILE\_DISC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percentile_disc), and [MEDIAN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/median) [window functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions) ([MDEV-12985](https://jira.mariadb.org/browse/MDEV-12985))
* [FOR ... END FOR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/for) statement ([MDEV-14415](https://jira.mariadb.org/browse/MDEV-14415))
* [XA RECOVER FORMAT='SQL'](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/xa-transactions) ([MDEV-14593](https://jira.mariadb.org/browse/MDEV-14593))
* Oracle compatible [SUBSTR()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/substring) function ([MDEV-14012](https://jira.mariadb.org/browse/MDEV-14012)) — contribution by Jérôme Brauge
* [INVISIBLE columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/invisible-columns) ([MDEV-10177](https://jira.mariadb.org/browse/MDEV-10177)) — GSoC 2016 project by Sachin Setiya
* Various scalability improvements ([MDEV-14529](https://jira.mariadb.org/browse/MDEV-14529), [MDEV-14505](https://jira.mariadb.org/browse/MDEV-14505))
* [Sequences](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-overview#using-sequences-in-default) can now be used with DEFAULT.
* [Semi-sync plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication) merged into the server ([MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073)) — contribution by Alibaba
* Numerous improvements for the partition engine ([MDEV-7698](https://jira.mariadb.org/browse/MDEV-7698)) — contribution by Kentoku Shiba
  * HANDLER support, condition pushdown, MRR, fulltext search, aggregate pushdown, bulk update/delete
* [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) updated to version 3.3.13
* Join push-down for Spider 3.3 ([MDEV-7698](https://jira.mariadb.org/browse/MDEV-7698)) — contribution by Kentoku Shiba
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.3](what-is-mariadb-103.md) for RHEL 7.2 and CentOS 7.2. Starting with the next 10.3 release we will be building MariaDB for CentOS 7 and RHEL 7 on version 7.3.
* [Galera wsrep library](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md) updated to 25.3.22
* [Repositories](https://downloads.mariadb.org/mariadb/repositories/) for Ubuntu 17.10 Artful added

### InnoDB

* [MDEV-14717](https://jira.mariadb.org/browse/MDEV-14717) crash-safe RENAME TABLE
* [MDEV-14585](https://jira.mariadb.org/browse/MDEV-14585) Automatically remove #sql- tables in InnoDB dictionary during recovery
* [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323) Rollback progress log messages during crash recovery are intermixed with unrelated log messages
* [MDEV-14589](https://jira.mariadb.org/browse/MDEV-14589) InnoDB should not lock a delete-marked record
* [MDEV-14511](https://jira.mariadb.org/browse/MDEV-14511) Use fewer transactions for updating InnoDB persistent statistics
* [MDEV-14374](https://jira.mariadb.org/browse/MDEV-14374) - UT\_DELAY code : Removing hardware barrier for arm64 bit platform
* [MDEV-14477](https://jira.mariadb.org/browse/MDEV-14477) InnoDB update\_time is wrongly updated after partial rollback or internal COMMIT
* Support CRC32 SSE4.2 implementation under Windows

### Variables and Modes

* New [sql\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode), EMPTY\_STRING\_IS\_NULL ([MDEV-14013](https://jira.mariadb.org/browse/MDEV-14013)) — contribution by Jérôme Brauge
* Added [bind\_address](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#bind_address) as a system variable ([MDEV-12542](https://jira.mariadb.org/browse/MDEV-12542)).
* New status variables [Table\_open\_cache\_active\_instances](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#table_open_cache_active_instances), [Table\_open\_cache\_hits](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#table_open_cache_hits), [Table\_open\_cache\_misses](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#table_open_cache_misses), [Table\_open\_cache\_overflows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#table_open_cache_overflows) ([MDEV-11153](https://jira.mariadb.org/browse/MDEV-11153))
* [innodb\_page\_cleaners](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables) is now dynamic ([MDEV-11025](https://jira.mariadb.org/browse/MDEV-11025))
* [binlog\_file\_cache\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) ([MDEV-14114](https://jira.mariadb.org/browse/MDEV-14114)) — contribution by Jun Su.
* [plugin\_maturity](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#plugin_maturity) is now set by default to one level less than server maturity. This may cause plugins below that maturity level that were previously working to no longer load ([MDEV-12501](https://jira.mariadb.org/browse/MDEV-12501)).
* [version\_malloc\_library](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#version_malloc_library) now correctly detects and reports tcmalloc ([MDEV-14315](https://jira.mariadb.org/browse/MDEV-14315))
* New variables [tcp\_keepalive\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tcp_keepalive_time), [tcp\_keepalive\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tcp_keepalive_interval), [tcp\_keepalive\_probes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tcp_keepalive_probes) ([MDEV-14412](https://jira.mariadb.org/browse/MDEV-14412)) — contribution by Oleg Obleukhov
* `tcp_linger`, `tcp_linger_timeout` ([MDEV-14113](https://jira.mariadb.org/browse/MDEV-14113)) — contribution by Shuode Li
* [slave\_transaction\_retry\_errors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables), allowing one to specify certain operations resulting in an error during replication to be retried, and [slave\_transaction\_retry\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) allowing the retry interval for a failed transaction to be set ([MDEV-7698](https://jira.mariadb.org/browse/MDEV-7698)) — contribution by Kentoku Shiba
* In addition to K, M, and G, numeric command-line options now support [T, P, and E suffixes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#setting-server-system-variables) — contribution by Daniel Black

**Do not use&#x20;**_**beta**_**&#x20;releases on production systems!**

For a complete list of changes made in [MariaDB 10.3.3](mariadb-1033-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-1033-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
