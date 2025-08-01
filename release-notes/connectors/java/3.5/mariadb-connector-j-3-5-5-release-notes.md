# Connector/J 3.5.5 Release Notes

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector" class="button primary">Download</a> <a href="mariadb-connector-j-3-5-4-release-notes.md" class="button secondary">Release Notes</a> <a href="../changelogs/3.5/mariadb-connector-j-3-5-4-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/about-mariadb-connector-j" class="button secondary">Connector/J Overview</a>

**Release date:** 1 Aug 2025

MariaDB Connector/J 3.5.5 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release.

{% hint style="info" %}
**For an overview of MariaDB Connector/J see the** [**About MariaDB Connector/J**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/about-mariadb-connector-j) **page**
{% endhint %}

## Bugs Fixed

* ensure rollback and release savepoint operation to be sent to server, even when there is no transaction in progress ([CONJ-1265](https://jira.mariadb.org/browse/CONJ-1265))
* forceConnectionTimeZoneToSession doesn't always set the timezone to server ([CONJ-1270](https://jira.mariadb.org/browse/CONJ-1270))

## Changelog

For a complete list of changes made in MariaDB Connector/J 3.5.5, with links to detailed\
information on each push, see the [changelog](../changelogs/3.5/mariadb-connector-j-3-5-5-changelog.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
