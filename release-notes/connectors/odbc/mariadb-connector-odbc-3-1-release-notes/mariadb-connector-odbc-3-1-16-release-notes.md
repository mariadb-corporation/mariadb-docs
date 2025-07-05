# MariaDB Connector/ODBC 3.1.16 Release Notes

The most recent [_**Stable**_](../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/ODBC is:[**MariaDB Connector/ODBC 3.2.5**](../mariadb-connector-odbc-3-2-release-notes/mariadb-connector-odbc-3-2-5-release-notes.md)

[Download](https://mariadb.com/downloads/#connectors)[Release Notes](mariadb-connector-odbc-3-1-16-release-notes.md)[Changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3116-changelog.md)[About MariaDB Connector/ODBC](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-odbc/README.md)

**Release date:** 22 Jun 2022

This is a [Stable (GA)](../../../mariadb-release-criteria.md) release of MariaDB Connector/ODBC 3.1.

MariaDB Connector/ODBC 3.1.16 is built on top of[MariaDB Connector/C v.3.3.1](../../c/mariadb-connector-c-33-release-notes/mariadb-connector-c-331-release-notes.md).

## Notable Changes

* The failover feature has been added ([ODBC-366](https://jira.mariadb.org/browse/ODBC-366)) - it’s possible to provide a comma separated list of hosts as a server name, for simple failover in case one or more hosts are not available. The following syntax is required:
  * hostname and port must be separated by a colon (:)
  * IPv6 addresses must be enclosed within square brackets
  * hostname:port pairs must be separated by a comma (,)
  * if only one host:port was specified, the host string needs to end with a comma.
  * if no port was specified, the default port will be used.
  * Examples for failover host string:\
    \*
    * 127.0.0.1:3307,
* MariaDB Connector/ODBC 3.1.16 is statically linked for Windows and MacOS with MariaDB Connector/C 3.3.1\
  MariaDB Connector/ODBC 3.1.16 is dynamically linked for Linux with MariaDB Connector/C, version 3.2 and 3.3 can be used, but 3.3 is required for the failover feature
* NULLISCURRENT connection string option has been added. It allows to force NULL catalog name value to be treated as currently selected schema in SQLTables. Otherwise, that is the default behavior, it’s treated as “any” schema([ODBC-298](https://jira.mariadb.org/browse/ODBC-298))
* NOLOCALINFILE connection string option has been added. Non-zero value disables LOAD DATA LOCAL INFILE execution, zero value enables it. By default it's enabled([ODBC-347](https://jira.mariadb.org/browse/ODBC-347))\
  Tarball layout has been fixed. Now only the lib subdirectory is present, but not lib64 or even both. That subdirectory contains both C/ODBC and C/C library files, as well as plugin library files in the plugin subdirectory of it. Also files belonging to Connector/C installation package have been removed([ODBC-352](https://jira.mariadb.org/browse/ODBC-352))

## Bug Fixes

* [ODBC-328](https://jira.mariadb.org/browse/ODBC-328) - Error connecting to some server versions not supporting session tracking with “Unknown system \*variable 'session\_track\_schema'” error. In particular, this bug occurred if connecting to xpand.
* [ODBC-346](https://jira.mariadb.org/browse/ODBC-346) - MariaDB Connector/ODBC package for MacOS is missing the Connector/C runtime library.
* [ODBC-356](https://jira.mariadb.org/browse/ODBC-356) - Fixed use of indexes in search for the best row identifier for positioned operations.
* [ODBC-359](https://jira.mariadb.org/browse/ODBC-359) - Segmentation fault in SQLFetch. The crash occurred if the NULL SQL\_C\_WCHAR buffer had been bound in SQLBindCol in order to obtain the required buffer length.
* [ODBC-361](https://jira.mariadb.org/browse/ODBC-361) - MS Access will get wrong data if unique index on nullable column is used
* [ODBC-365](https://jira.mariadb.org/browse/ODBC-365) - Length is not returned for SQL\_C\_WCHAR on SQLFetch if data buffer is NULL

## Changelog

For a complete list of every change made in this release, with links to\
detailed information on each push, see the[changelog](../changelogs/mariadb-connector-odbc-31-changelogs/mariadb-connector-odbc-3116-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
