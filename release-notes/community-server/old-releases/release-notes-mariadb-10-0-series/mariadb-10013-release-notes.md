# MariaDB 10.0.13 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is: [**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.13) | [Release Notes](mariadb-10013-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10013-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 11 Aug 2014

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current stable series of MariaDB. It is an evolution of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new features not found anywhere else and\
with backported and reimplemented features from MySQL 5.6.

[MariaDB 10.0.13](mariadb-10013-release-notes.md) is a [_**Stable**_](../../about/release-criteria.md) (_GA_) release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the** [**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

* Fixes for the following security vulnerabilities:
  * [CVE-2010-5298](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2010-5298)
  * [CVE-2014-0195](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0195)
  * [CVE-2014-0198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0198)
  * [CVE-2014-0221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0221)
  * [CVE-2014-0224](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0224)
  * [CVE-2014-3470](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-3470)
  * [CVE-2014-6474](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6474)
  * [CVE-2014-6489](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6489)
  * [CVE-2014-6564](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6564)
  * [CVE-2012-5615](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5615)
  * [CVE-2014-4274](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-4274)
  * [CVE-2014-4287](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-4287)
  * [CVE-2014-6463](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6463)
  * [CVE-2014-6478](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6478)
  * [CVE-2014-6484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6484)
  * [CVE-2014-6495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6495)
  * [CVE-2014-6505](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6505)
  * [CVE-2014-6520](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6520)
  * [CVE-2014-6530](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6530)
  * [CVE-2014-6551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-6551)
  * [CVE-2015-0391](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-0391)
* [filesort-with-small-limit-optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/filesort-with-small-limit-optimization) is now visible through the [slow query log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log) and a new status variable, [sort\_priority\_queue\_sorts](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-status-variables#sort_priority_queue_sorts).
* New variables [aria\_pagecache\_file\_hash\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_pagecache_file_hash_size) and [key\_cache\_file\_hash\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myisam-storage-engine/myisam-system-variables#key_cache_file_hash_size) for determining the number of hash buckets for open and changed files for Aria and MyISAM respectively.
* [Connect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/connect) engine supports partitioning.
* Many plugins have had their [maturity level](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/list-of-plugins) increased (from beta to gamma or from gamma to stable).
* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) upgraded to 7.1.7
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) upgraded to 5.6.19-67.0
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) upgraded to 5.6.19
* [Performance\_Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) upgraded to 5.6.20

For a complete list of changes made in [MariaDB 10.0.13](mariadb-10013-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-10013-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
