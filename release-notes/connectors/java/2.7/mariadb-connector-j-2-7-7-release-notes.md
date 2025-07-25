# Connector/J 2.7.7 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://mariadb.com/downloads/connectors)[Release Notes](mariadb-connector-j-2-7-7-release-notes.md)[Changelog](../changelogs/2.7/mariadb-connector-j-2-7-7-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 08 Nov 2022

MariaDB Connector/J 2.7.7 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Bugs Fixed

* [CONJ-1021](https://jira.mariadb.org/browse/CONJ-1021) GSSAPI authentication might result in connection reset
* [CONJ-1019](https://jira.mariadb.org/browse/CONJ-1019) DatabaseMetaData.getImportedKeys should return real value for PK\_NAME column
* [CONJ-1016](https://jira.mariadb.org/browse/CONJ-1016) avoid splitting BULK command into multiple commands in case of prepareStatement.setNull() use
* [CONJ-1011](https://jira.mariadb.org/browse/CONJ-1011) correcting possible NPE when using statement.cancel() that coincide with statement.close() in another thread
* [CONJ-1007](https://jira.mariadb.org/browse/CONJ-1007) Socket file descriptors are leaked after connecting with unix socket if DB is not up running

## Changelog

For a complete list of changes made in MariaDB Connector/J 2.7.7, with links to detailed\
information on each push, see the [changelog](../changelogs/2.7/mariadb-connector-j-2-7-7-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
