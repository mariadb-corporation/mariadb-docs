# Connector/C 2.3.1 Release notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.3.1)[Release Notes](mariadb-connector-c-231-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-23-changelogs/mariadb-connector-c-231-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 4 Aug 2016

This is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## New features

* Added support for OpenSSL 1.1 library

## Notable Bug fixes

* [CONC-194](https://jira.mariadb.org/browse/CONC-194): Fixed wrong behaviour of mysql\_stmt\_fetch\_column: If a blob is fetched in pieces, offset was ignored.
* [CONC-196](https://jira.mariadb.org/browse/CONC-196): When retrieving large result sets mysql\_stmt\_store\_result was 4 times slower than libmysql due to extra loops in alloc\_root() function. (see also [ODBC-31](https://jira.mariadb.org/browse/ODBC-31))

For a list of changes made in this release, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-c-23-changelogs/mariadb-connector-c-231-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
