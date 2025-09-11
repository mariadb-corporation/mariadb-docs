---
hidden: true
---

# Connector/ODBC 3.2.7 Release Notes

{% include "../../../.gitbook/includes/unreleased-odbc.md" %}

<a href="https://mariadb.com/downloads/connectors/connectors-data-access/odbc-connector" class="button primary">Download</a> <a href="connector-odbc-3.2.7-release-notes.md" class="button secondary">Release Notes</a> <a href="../changelogs/mariadb-connector-odbc-3-2-changelogs/connector-odbc-3.2.7-changelog.md" class="button secondary">Changelog</a> <a href="https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc" class="button secondary">About MariaDB Connector/ODBC</a>

**Release date:** ?

This is a [Stable (GA)](../../../community-server/about/release-criteria.md) release of MariaDB Connector/ODBC 3.2.

MariaDB Connector/ODBC 3.2.7 is built on top of [MariaDB Connector/C v.3.4.5](../../c/3.4/3.4.5.md).

## Bug Fixes

* ODBC-469 - SSLVERIFY=0, still getting The certificate's CN name does not match the passed value on Windows
* ODBC-470 - Dropping statement handle could break protocol if other statement hasn't finished fetching results
* ODBC-471 - Fetching of stored procedure out parameters could fail in case of result-set streaming
* ODBC-472 - Some internal classes destructors called functions that can throw in some conditions
* ODBC-473 - SQLGetData could write data of the wrong length in case of resultset streaming and cached resultset
* ODBC-474 - Bulk operations with parameter callbacks could not respect NULL value indicators

## Changelog

For a complete list of every change made in this release, with links to detailed information on each push, see the [changelog](../changelogs/mariadb-connector-odbc-3-2-changelogs/connector-odbc-3.2.7-changelog.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% @marketo/form formid="4316" formId="4316" %}
