# MariaDB 10.8.4 Release Notes

The most recent release of [MariaDB 10.8](what-is-mariadb-108.md) is:[**MariaDB 10.8.8**](mariadb-10-8-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.8.8/)

[Download 10.8.4](https://downloads.mariadb.org/mariadb/10.8.4/) | [Release Notes](mariadb-1084-release-notes.md) | [Changelog](../../changelogs/10.8/10.8.4.md) | [Overview of 10.8](what-is-mariadb-108.md)

**Release date:** 15 Aug 2022

[MariaDB 10.8](what-is-mariadb-108.md) is the current short-term maintenance stable series of MariaDB. It is an evolution\
of [MariaDB 10.7](../release-notes-mariadb-10-7-series/what-is-mariadb-107.md) with several entirely new features.

[MariaDB 10.8.4](mariadb-1084-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.8**](what-is-mariadb-108.md) **see the**[**What is MariaDB 10.8?**](what-is-mariadb-108.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### InnoDB

* InnoDB corruption due to lack of file locking ([MDEV-28495](https://jira.mariadb.org/browse/MDEV-28495))
* FULLTEXT search with apostrophe, and mandatory words ([MDEV-20797](https://jira.mariadb.org/browse/MDEV-20797))
* ALTER TABLE IMPORT TABLESPACE corrupts an encrypted table ([MDEV-28779](https://jira.mariadb.org/browse/MDEV-28779))
* ALTER TABLE wrong-result fix ([MDEV-26294](https://jira.mariadb.org/browse/MDEV-26294))
* Crash recovery fixes ([MDEV-28668](https://jira.mariadb.org/browse/MDEV-28668), [MDEV-28731](https://jira.mariadb.org/browse/MDEV-28731))
* DDL crash recovery fixes ([MDEV-28752](https://jira.mariadb.org/browse/MDEV-28752), [MDEV-28802](https://jira.mariadb.org/browse/MDEV-28802), [MDEV-28864](https://jira.mariadb.org/browse/MDEV-28864), [MDEV-28870](https://jira.mariadb.org/browse/MDEV-28870), [MDEV-28923](https://jira.mariadb.org/browse/MDEV-28923), [MDEV-28977](https://jira.mariadb.org/browse/MDEV-28977))
* Avoid crashes on corrupted data ([MDEV-13542](https://jira.mariadb.org/browse/MDEV-13542), [MDEV-18519](https://jira.mariadb.org/browse/MDEV-18519), [MDEV-21098](https://jira.mariadb.org/browse/MDEV-21098), [MDEV-22388](https://jira.mariadb.org/browse/MDEV-22388), [MDEV-28457](https://jira.mariadb.org/browse/MDEV-28457), [MDEV-28950](https://jira.mariadb.org/browse/MDEV-28950))
* Bulk load bug fixes ([MDEV-28242](https://jira.mariadb.org/browse/MDEV-28242), [MDEV-28679](https://jira.mariadb.org/browse/MDEV-28679))
* Performance fixes ([MDEV-28708](https://jira.mariadb.org/browse/MDEV-28708), [MDEV-28766](https://jira.mariadb.org/browse/MDEV-28766))

### Replication

* [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) is stored in binlog, so that CREATE TABLE on slave would always have the same effect as on master. ([MDEV-29078](https://jira.mariadb.org/browse/MDEV-29078))
* ER\_SLAVE\_INCIDENT error is specified now on slave to be seen with SHOW-SLAVE-STATUS ([MDEV-21087](https://jira.mariadb.org/browse/MDEV-21087))
* INCIDENT\_EVENT is no longer binlogged when a being logged transaction can be safely rolledback ([MDEV-21443](https://jira.mariadb.org/browse/MDEV-21443))
* sequences related row-format events are made to correspond to binlog\_row\_image ([MDEV-28487](https://jira.mariadb.org/browse/MDEV-28487))
* Possible reason of FLUSH BINARY LOGS hang is eliminated ([MDEV-28948](https://jira.mariadb.org/browse/MDEV-28948))
* Fix out-of-order gtid error in the circular semisync setup ([MDEV-28609](https://jira.mariadb.org/browse/MDEV-28609))

### Galera

* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) updated to 26.4.12
* Possible to write/update with read\_only=ON and not a SUPER privilege ([MDEV-28546](https://jira.mariadb.org/browse/MDEV-28546))
* Node crashes with Transport endpoint is not connected mysqld got signal 6 ([MDEV-25068](https://jira.mariadb.org/browse/MDEV-25068))
* Galera4 not able to report proper wsrep\_incoming\_addresses ([MDEV-20627](https://jira.mariadb.org/browse/MDEV-20627))
* Galera should replicate nextval()-related changes in sequences with INCREMENT <> 0, at least NOCACHE ones with engine=InnoDB ([MDEV-27862](https://jira.mariadb.org/browse/MDEV-27862))
* Add support for OpenSSL 3.0 in Galera ([MDEV-25949](https://jira.mariadb.org/browse/MDEV-25949))

### Optimizer

* Server crash in JOIN\_CACHE::free or in copy\_fields ([MDEV-23809](https://jira.mariadb.org/browse/MDEV-23809))
  * Queries that use DISTINCT and an always-constant function like COLLATION(aggegate\_func(...)) could cause a server crash. Note that COLLATION() is a special function - its value is constant even if its argument is not costant.
* Crash when using ANY predicand with redundant subquery in GROUP BY clause ([MDEV-29139](https://jira.mariadb.org/browse/MDEV-29139))
  * A query with a subuquery in this form could cause a crash:

```sql
... ANY (SELECT ... GROUP BY (SELECT redundant_subselect_here)) ...
```

* MariaDB Server SEGV on INSERT .. SELECT ([MDEV-26427](https://jira.mariadb.org/browse/MDEV-26427))
  * Certain queries in form "INSERT ... SELECT with\_aggregate\_or\_window\_func" could cause a crash.
* restore\_prev\_nj\_state() doesn't update cur\_sj\_inner\_tables correctly ([MDEV-28749](https://jira.mariadb.org/browse/MDEV-28749))
  * Subquery semi-join optimization could miss LooseScan or FirstMatch strategies for certain queries.
* Optimizer uses all partitions after upgrade to 10.3 ([MDEV-28246](https://jira.mariadb.org/browse/MDEV-28246))
  * For multi-table UPDATE or DELETE queries, the optimizer failed to apply Partition Pruning optimization for the table that is updated or deleted from.
* Range optimizer regression for key IN (const, ....) ([MDEV-25020](https://jira.mariadb.org/browse/MDEV-25020))
  * The issue can be observed on [MariaDB 10.5.9](../mariadb-10-5-series/mariadb-1059-release-notes.md) and later versions which have the fix for [MDEV-9750](https://jira.mariadb.org/browse/MDEV-9750). That fix introduceds optimizer\_max\_sel\_arg\_weight.
  * If one sets optimizer\_max\_sel\_arg\_weight to a very high value or zero (which means "unlimited") and runs queries that produce heavy-weight graphs, they can observe a performance slowdown, e.g.:

```
table.keyXpartY [NOT] IN ( ... )
```

* Wrong result with table elimination combined with not\_null\_range\_scan ([MDEV-28858](https://jira.mariadb.org/browse/MDEV-28858))
  * If one runs with optimizer\_switch='not\_null\_range\_scan=on' (which is not enabled by default), a query that does a join and has const tables could produce a wrong result.
* Assertion \`tmp >= 0' failed in best\_access\_path ([MDEV-28882](https://jira.mariadb.org/browse/MDEV-28882))
  * If one uses histogram\_type=JSON\_HB, has collected a histogram of that type and runs a query that selects a very narrow range near histogram end, they can hit an assertion in the optimizer due to rounding errors in the histogram causing negative selectivity.

### Spider

* [spider\_init\_sql\_alloc\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables) and [spider\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables) have been deprecated ([MDEV-27926](https://jira.mariadb.org/browse/MDEV-27926), [MDEV-28560](https://jira.mariadb.org/browse/MDEV-28560))
* Spider's high-availability feature has been deprecated ([MDEV-28479](https://jira.mariadb.org/browse/MDEV-28479))

### JSON

* [JSON\_TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table): extract document fragment into JSON column ([MDEV-25875](https://jira.mariadb.org/browse/MDEV-25875))

### CONNECT

* [CONNECT Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/connect) now supports [INSERT IGNORE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert-ignore) with [Mysql Table type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/connect/connect-table-types/connect-mysql-table-type-accessing-mysqlmariadb-tables) ([MDEV-27766](https://jira.mariadb.org/browse/MDEV-27766))

### General

* [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) now also has a session scope, not only global ([MDEV-29225](https://jira.mariadb.org/browse/MDEV-29225))
* New [mariadb client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mysql-command-line-client) option, `-enable-cleartext-plugin`. Option does not do anything, and is for MySQL-compatibility purposes only.
* Crash in [JSON\_EXTRACT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_extract) ([MDEV-29188](https://jira.mariadb.org/browse/MDEV-29188))
* ALTER TABLE ALGORITHM=NOCOPY does not work after upgrade ([MDEV-28727](https://jira.mariadb.org/browse/MDEV-28727))
* Server crash upon CREATE VIEW with unknown column in ON condition ([MDEV-29088](https://jira.mariadb.org/browse/MDEV-29088))
* password\_reuse\_check plugin mixes username and password ([MDEV-28838](https://jira.mariadb.org/browse/MDEV-28838))
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.8](what-is-mariadb-108.md) for Debian 10 "Buster" for ppc64el
* Repositories for Ubuntu 22.04 and RHEL/Rocky 9 have been added in this release

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157)
  * [CVE-2022-32082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32082)
  * [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089)
  * [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081)
  * [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032)
  * [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091)
  * [CVE-2022-38791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38791)
  * [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084)

## Changelog

For a complete list of changes made in [MariaDB 10.8.4](mariadb-1084-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/10.8/10.8.4.md).

## Contributors

For a full list of contributors to [MariaDB 10.8.4](mariadb-1084-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-8-4-10-7-5-10-6-9-10-5-17-10-4-26-and-10-3-36-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
