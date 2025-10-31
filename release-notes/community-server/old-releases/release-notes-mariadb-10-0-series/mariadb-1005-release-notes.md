# MariaDB 10.0.5 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

There was a packaging issue with 10.0.5 on Debian & Ubuntu that prevented TokuDB from installing. This was fixed in 10.0.6.

[Download](https://downloads.mariadb.org/mariadb/10.0.5) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1005-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 7 Nov 2013

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current development version of MariaDB. It is an evolution\
of [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) the MariaDB 5.5 series with several entirely new\
features not found anywhere else and with backported and\
reimplemented features from MySQL 5.6.

[MariaDB 10.0.5](mariadb-1005-release-notes.md) is a [_**Beta**_](../../about/release-criteria.md) release. This is the\
sixth 10.0-based release, and the first beta release. We are releasing it now\
to get it into the hands of any who might want to test it. All features planned\
for inclusion in the stable (GA) [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series are included in this\
release. This is still a beta however, not a final, production-ready, release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

For a list of changes made in [MariaDB 10.0.5](mariadb-1005-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1005-changelog.md).

## Based on [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)

The [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series builds off of the [MariaDB 5.5 series.](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) It includes\
completely new features and features imported and backported from MySQL 5.6.

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Security fixes

This release includes fixes for the following security vulnerabilities:

* [CVE-2013-5807](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-5807)
* [CVE-2013-3839](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-3839)

## From [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md)

* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) from [MariaDB 5.5](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) has been merged into this version of MariaDB
* Starting with this version, [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is now built with [jemalloc](https://www.canonware.com/jemalloc/) by default on Linux (not on\
  Solaris or Windows).

## Newly Implemented Features

* [MDEV-4506](https://jira.mariadb.org/browse/MDEV-4506): [Parallel replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/parallel-replication)
* [MDEV-4397](https://jira.mariadb.org/browse/MDEV-4397): [Roles](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/user-account-management/roles)
* [MDEV-407](https://jira.mariadb.org/browse/MDEV-407): [EXPLAIN in the slow query log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log/explain-in-the-slow-query-log).
* [MDEV-4425](https://jira.mariadb.org/browse/MDEV-4425): [PCRE library, REGEXP\_REPLACE, REGEXP\_INSTR, REGEXP\_SUBSTR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) functions
* [MDEV-4911](https://jira.mariadb.org/browse/MDEV-4911): [KILL QUERY ID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/kill) : the ability to kill a query by the query ID\
  instead of the thread ID.
* [MDEV-3814](https://jira.mariadb.org/browse/MDEV-3814): [DELETE .. RETURNING](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete)\`\`
* [MDEV-4133](https://jira.mariadb.org/browse/MDEV-4133): use fallocate() in XtraDB/InnoDB

## Features and Fixes Merged or Backported from MySQL 5.6.10

* [MDEV-5163](https://jira.mariadb.org/browse/MDEV-5163): [WEIGHT\_STRING()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/weight_string) function
* [MDEV-3798](https://jira.mariadb.org/browse/MDEV-3798): [EXPLAIN for UPDATE/DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain)
* [MDEV-4411](https://jira.mariadb.org/browse/MDEV-4411): Connection attributes (see the [performance schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) tables [session\_connect\_attrs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-session_connect_attrs-table) and [session\_account\_connect\_attrs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema/performance-schema-tables/performance-schema-session_account_connect_attrs-table))
* [MDEV-4928](https://jira.mariadb.org/browse/MDEV-4928): Collation customization improvements (see [Supported Characters Sets and Collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations)).
* [MDEV-5025](https://jira.mariadb.org/browse/MDEV-5025): [TO\_BASE64()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/to_base64) and [FROM\_BASE64()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/from_base64) functions

## Incompatible Changes

* New [reserved word](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/reserved-words): RETURNING. This can no longer be used as an [identifier](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sql-language-structure/identifier-names) without being quoted.

For full details, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1005-changelog.md).

## Fedora 17

As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last version of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Fedora 17. The Fedora 17 repository for [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) will go away at the next release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md).

Thanks, and enjoy MariaDB!

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
