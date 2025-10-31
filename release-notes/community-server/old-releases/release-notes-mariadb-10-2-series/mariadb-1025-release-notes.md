# MariaDB 10.2.5 Release Notes

The most recent release of [MariaDB 10.2](what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.5) | [Release Notes](mariadb-1025-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1025-changelog.md) | [Overview of 10.2](what-is-mariadb-102.md)

**Release date:** 5 Apr 2017

[MariaDB 10.2](what-is-mariadb-102.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.1](../release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL 5.6 and 5.7.

[MariaDB 10.2.5](mariadb-1025-release-notes.md) is a [_**Release Candidate**_](../../about/release-criteria.md) _**(RC)**_ release.

**For an overview of** [**MariaDB 10.2**](what-is-mariadb-102.md) **see the**[**What is MariaDB 10.2?**](what-is-mariadb-102.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

* [TokuDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/legacy-storage-engines/tokudb) updated to 5.6.35-80.0
* [PCRE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/pcre) updated to 8.40
* [MDEV-12160](https://jira.mariadb.org/browse/MDEV-12160): [ed25519 authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519)
* [MDEV-11842](https://jira.mariadb.org/browse/MDEV-11842): Fix a 10.1.21 regression with failed INSERT, BEFORE INSERT triggers, and columns with no default value
* [MDEV-12075](https://jira.mariadb.org/browse/MDEV-12075): Fix a 10.1.21 regression in the InnoDB data file extension code
* [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027): better InnoDB crash recovery progress reporting
* [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): improvements to how InnoDB data files are extended
* Improvements to InnoDB startup/shutdown to make it more robust
* [MDEV-9734](https://jira.mariadb.org/browse/MDEV-9734): [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd) compatible bintar files now available
* [MDEV-9658](https://jira.mariadb.org/browse/MDEV-9658): [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/myrocks/building-myrocks-in-mariadb) alpha storage engine added
  * This is an alpha version of this storage engine with limited functionality at this time
  * Currently, zlib and snappy compression is supported (only zlib on Windows)
  * MyRocks is not available for 32-bit platforms
* [AWS Key Management plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/aws-key-management-encryption-plugin) added for Windows, CentOS, RHEL, and Fedora packages
* [MDEV-12091](https://jira.mariadb.org/browse/MDEV-12091): Shutdown fails to wait for rollback of recovered transactions to finish
* [MDEV-12219](https://jira.mariadb.org/browse/MDEV-12219): Discard temporary undo logs at transaction commit
* [MDEV-12289](https://jira.mariadb.org/browse/MDEV-12289): compatibility fix for upgrading from 5.5 or 10.x
* [MDEV-9255](https://jira.mariadb.org/browse/MDEV-9255): Two new columns added to the [Information Schema COLUMNS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-columns-table) table, providing information about [generated (virtual, or computed)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns) columns.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3313)
  * [CVE-2017-3302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3302)

## Notes

For a complete list of changes made in [MariaDB 10.2.5](mariadb-1025-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-102-series/mariadb-1025-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
