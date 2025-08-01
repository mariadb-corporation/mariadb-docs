# Connector/J 1.7.3 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.7.3/)[Release Notes](mariadb-connector-j-173-release-notes.md)[Changelog](../changelogs/1.7/mariadb-connector-j-173-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 14 Mar 2018

MariaDB Connector/J 1.7.3 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For an overview of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

## Bug Fixes

* \[[CONJ-583](https://jira.mariadb.org/browse/CONJ-583)] possible hang indefinitely using master/slave configuration and failover occur
* \[[CONJ-586](https://jira.mariadb.org/browse/CONJ-586)] erroneous transaction state when first command result as error
* \[[CONJ-587](https://jira.mariadb.org/browse/CONJ-587)] using allowMasterDownConnection option can lead to NPE when using setReadOnly()
* \[[CONJ-588](https://jira.mariadb.org/browse/CONJ-588)] using option 'allowMasterDownConnection' won't permit to connect if master is down
* \[[CONJ-534](https://jira.mariadb.org/browse/CONJ-534)] Connection.isValid() must be routed to Master and Slave connections to avoid any server timeout

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
