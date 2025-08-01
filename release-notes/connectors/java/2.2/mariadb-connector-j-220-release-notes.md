# Connector/J 2.2.0 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/2.2.0/)[Release Notes](mariadb-connector-j-220-release-notes.md)[Changelog](../changelogs/2.2/mariadb-connector-j-220-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md)

**Release date:** 9 Nov 2017

MariaDB Connector/J 2.2.0 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-j/README.md) **page**

## Features

* \[[CONJ-522](https://jira.mariadb.org/browse/CONJ-522)] Pool datasource implementation : MariaDB has now 2 different Datasources implementation. More information on [pool datasource implementation](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j/pool-datasource-implementation).
* \[[CONJ-530](https://jira.mariadb.org/browse/CONJ-530)] Permit Connection.abort() forcing killing the connection even if connection is stuck in another thread (like reading big resultset)
* \[[CONJ-531](https://jira.mariadb.org/browse/CONJ-531)] permit cancelling streaming result-set using Statement.cancel.
* \[[CONJ-495](https://jira.mariadb.org/browse/CONJ-495)] Improve reading result-set data
* \[[CONJ-510](https://jira.mariadb.org/browse/CONJ-510)] Permit connection creation to allow execution of read-only statements on slaves when master is down

## Bug Fixes

* \[[CONJ-532](https://jira.mariadb.org/browse/CONJ-532)] correction Statement.getMoreResults() for multi-queries
* \[[CONJ-533](https://jira.mariadb.org/browse/CONJ-533)] PrepareStatement.setTime() may insert incorrect time according to current timezone, time and option "useLegacyDatetimeCode"
* \[[CONJ-535](https://jira.mariadb.org/browse/CONJ-535)] correction on numerical getter for big BIT data type fields
* \[[CONJ-541](https://jira.mariadb.org/browse/CONJ-541)] Fix behavior of ResultSet#relative when crossing result set boundaries

## Misc

* \[[CONJ-469](https://jira.mariadb.org/browse/CONJ-469)] Improve Blob/Clob implementation (avoiding array copy from result-set row)
* \[[CONJ-539](https://jira.mariadb.org/browse/CONJ-539)] better message when server close connection
* \[misc] resultset.findColumn method use column name if alias not found
* \[misc] default option "connectTimeout" value to 30 seconds (was 0 = no timeout)
* \[misc] ensure that enablePacketDebug option works when timer tick is big

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
