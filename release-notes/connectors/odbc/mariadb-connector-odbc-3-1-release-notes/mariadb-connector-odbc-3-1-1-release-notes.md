# Connector/ODBC 3.1.1 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-3-1-1-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-311-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 9 May 2019

This is a [Stable (GA)](../../../community-server/about/release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.1 is built on top of [MariaDB Connector/C v.3.0.9](../../c/mariadb-connector-c-30-release-notes/mariadb-connector-c-309-release-notes.md).

## Notable Changes

Version 3.1 is mainly about adding support for MacOS X. There is now an installation package for MacOS X that has been compiled on MacOS X version 10.13.6 (High Sierra). It works with the iODBC Driver Manager and supports only Unicode (not ANSI). Make sure to install iODBC and OpenSSL, if not installed already. If you use Homebrew they can easily be installed with:

```bash
brew install libiodbc
brew install openssl
```

## Bug Fixes

MariaDB Connector/ODBC 3.1.1 contains all bug fixes in [MariaDB Connector/ODBC v.3.0.9](../mariadb-connector-odbc-30-release-notes/mariadb-connector-odbc-309-release-notes.md). Other changes:

* [ODBC-223](https://jira.mariadb.org/browse/ODBC-223) - Add Connector/ODBC to default odbcinst.ini on Mac

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the [changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-311-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
