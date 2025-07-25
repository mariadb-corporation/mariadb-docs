# Connector/C 2.3.6 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.3.6)[Release Notes](mariadb-connector-c-236-release-notes.md)[Changelog](../changelogs/mariadb-connector-c-23-changelogs/mariadb-connector-c-236-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 7 Jun 2018

This is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of the MariaDB\
Connector/C, formerly known as MariaDB Client Library for C.

**For a description of this library see the**[**MariaDB Connector/C**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) **page.**

## Notable Bug Fixes

* [CONC-334](https://jira.mariadb.org/browse/CONC-334): Copy all members of MYSQL\_FIELD from mysql->fields to stmt->fields
* Fixed conversion from string to MYSQL\_TIME type (prepared statements)
* Added missing status defines (SERVER\_STATUS\_ANSI\_QUOTES, SERVER\_STATUS\_IN\_TRANS\_READONLY)
* [MDEV-15450](https://jira.mariadb.org/browse/MDEV-15450): Added new default connection attribute \_server\_host
* [CONC-315](https://jira.mariadb.org/browse/CONC-315): Changed default character set to latin1

## Changelog

For a list of changes made in this release, with links to detailed\
information on each push, see the [changelog](../changelogs/mariadb-connector-c-23-changelogs/mariadb-connector-c-236-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
