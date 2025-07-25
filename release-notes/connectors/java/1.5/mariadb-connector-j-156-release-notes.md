# Connector/J 1.5.6 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.5.6/)[Release Notes](mariadb-connector-j-156-release-notes.md)[Changelog](../changelogs/1.5/mariadb-connector-j-156-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 22 Dec 2016

MariaDB Connector/J 1.5.6 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Notable Changes

This version is a bug-fix release.

### Bugfix

* [CONJ-399](https://jira.mariadb.org/browse/CONJ-399) : resultSet getLong() for BIGINT column fails if value is Long.MIN\_VALUE in Text protocol
* [CONJ-395](https://jira.mariadb.org/browse/CONJ-395) : Aurora does not randomise selection of read replicas
* [CONJ-392](https://jira.mariadb.org/browse/CONJ-392) : Aurora cluster endpoint detection timezone issue
* [CONJ-394](https://jira.mariadb.org/browse/CONJ-394) : mysql\_native\_password plugin authentication fail when default-auth set
* [CONJ-388](https://jira.mariadb.org/browse/CONJ-388) : handle timestamp '0000-00-00 00:00:00' getString()
* [CONJ-391](https://jira.mariadb.org/browse/CONJ-391) : Use SELECT in place of SHOW command on connection
* [CONJ-396](https://jira.mariadb.org/browse/CONJ-396) : revised implementation for handling multiple resultSet correctly for a unique command (was failing if more than 2)

### Misc

* [CONJ-380](https://jira.mariadb.org/browse/CONJ-380) : continous integration now test against maxscale

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
