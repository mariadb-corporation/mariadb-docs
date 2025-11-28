# MariaDB 10.0.8 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.8) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1008-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 10 Feb 2014

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current development version of MariaDB. It is an evolution\
of the [MariaDB 5.5 series](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new\
features not found anywhere else and with backported and\
reimplemented features from MySQL 5.6.

[MariaDB 10.0.8](mariadb-1008-release-notes.md) is an [_**RC**_](../../about/release-criteria.md) (_Release Candidate_)\
release. This is the ninth 10.0-based release, and the first RC release.\
All features planned for inclusion in the stable (GA) [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series are\
included in this release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

[MariaDB 10.0.8](mariadb-1008-release-notes.md) is primarily a bug-fix and polishing release.

Notable changes of this release include:

* Fixes for the following security vulnerabilities:
  * [CVE-2014-0412](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0412)
  * [CVE-2014-0401](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0401)
  * [CVE-2014-0437](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0437)
  * [CVE-2014-0420](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0420)
  * [CVE-2013-5908](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-5908)
* InnoDB upgraded to version 5.6.14
* [FLUSH ... FOR EXPORT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export) works
* Added a new server variable, [old\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old_mode), to allow selectively restoring old behavior, in contrast to the old "all-or-nothing" approach of the `--old` command-line option. See [OLD MODE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/old_mode) for more.
* Added a new read-only server variable [malloc\_library](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#malloc_version)
* Bundled [PCRE library](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) upgraded to version 8.34
* The [CREATE OR REPLACE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#create-or-replace) statement was added. It is used internally for replication ([MDEV-5491](https://jira.mariadb.org/browse/MDEV-5491)), but it is also can be used by clients as any other SQL statement.
  * This enables replication to be able to continue even if the slave crashes (due to, for example, a bug or power outage) in the middle of a `CREATE TABLE`, `CREATE ... SELECT`, or `DROP TABLE`. When the slave comes back up it can replay the statement without any data loss if needed.
  * As part of this change, the [slave-ddl-exec-mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) variable was added. It specifies how `CREATE TABLE` and `DROP TABLE` statements are replicated.

For a complete list of changes made in [MariaDB 10.0.8](mariadb-1008-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1008-changelog.md).

## Fedora, Ubuntu, and Mint

As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will\
be the final release of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) for Fedora 18 "Spherical Cow", Ubuntu 13.04\
"Raring", and Mint 15 "Olivia". When the next version of [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is\
released, repositories for these distributions will go away.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
