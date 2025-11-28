# MariaDB 10.0.9 Release Notes

The most recent release in the [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.9) | **Release Notes** | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1009-changelog.md) | [Overview of 10.0](changes-improvements-in-mariadb-10-0.md)

**Release date:** 10 Mar 2014

[MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) is the current development version of MariaDB. It is an evolution\
of the [MariaDB 5.5 series](../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) with several entirely new\
features not found anywhere else and with backported and\
reimplemented features from MySQL 5.6.

[MariaDB 10.0.9](mariadb-1009-release-notes.md) is an [_**RC**_](../../about/release-criteria.md) (_Release Candidate_)\
release. This is the tenth 10.0-based release, and the second RC release.\
All features planned for inclusion in the stable (GA) [MariaDB 10.0](changes-improvements-in-mariadb-10-0.md) series are\
included in this release.

**For an overview of** [**MariaDB 10.0**](changes-improvements-in-mariadb-10-0.md) **see the**[**What is MariaDB 10.0?**](changes-improvements-in-mariadb-10-0.md) **page.**

Thanks, and enjoy MariaDB!

## Notable changes

[MariaDB 10.0.9](mariadb-1009-release-notes.md) is primarily a bug-fix and polishing release.

Notable changes of this release include:

* Fixes for the following security vulnerabilities:
  * [CVE-2014-4243](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-4243)
  * [CVE-2014-2419](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2419)
  * [CVE-2014-0384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-0384)
  * [CVE-2014-2438](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2438)
  * [CVE-2014-2432](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2432)
* InnoDB upgraded to version 5.6.15
* [Extended-keys optimization ](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/mariadb-internals-documentation-query-optimizer/extended-keys)is now enabled by default.
* MariaDB can be compiled to use the system's [PCRE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) library.
* Added [MASTER\_GTID\_WAIT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/master_gtid_wait) and [@@last\_gtid](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid).
* When a [TIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/time) value is casted to a [DATETIME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/datetime), the date part will be the [CURRENT\_DATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/current_date), not `0000-00-00`. This is compatible with the SQL standard and MySQL-5.6. One can use [@@old\_mode=ZERO\_DATE\_TIME\_CAST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/old_mode) to revert to the old behavior.
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) is now the default InnoDB implementation, Oracle InnoDB is a plugin that can be dynamically loaded if desired.
* Builds for Debian Sid and Ubuntu Trusty are being made available for the first time in the MariaDB [repositories](https://downloads.mariadb.org/mariadb/repositories/). For this release the Trusty packages are considered as alpha releases. The Sid packages will likely always be considered as such. Both were made as part of normal MariaDB development, and we're making them available for those that want to test or try them out.

For a complete list of changes made in [MariaDB 10.0.9](mariadb-1009-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1009-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
