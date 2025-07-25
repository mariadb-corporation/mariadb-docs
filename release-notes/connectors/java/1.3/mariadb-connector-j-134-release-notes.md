# Connector/J 1.3.4 Release Notes

{% include "../../../.gitbook/includes/latest-java.md" %}

[Download](https://downloads.mariadb.org/connector-java/1.3.4/)[Release Notes](mariadb-connector-j-134-release-notes.md)[Changelog](../changelogs/1.3/mariadb-connector-j-134-changelog.md)[Connector/J Overview](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md)

**Release date:** 12 Jan 2016

MariaDB Connector/J 1.3.4 is a [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_\
release.

**For a description of MariaDB Connector/J see the**[**About MariaDB Connector/J**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-j/README.md) **page**

For a list of all changes made in this release, with links to detailed\
information on each push, see the [changelog](../changelogs/1.3/mariadb-connector-j-134-changelog.md).

This version is a bugfix release

## Notable changes and additions

### Major

* Failover improvements (reconnection implementation evolution, thread handling ...)
* [CONJ-236](https://jira.mariadb.org/browse/CONJ-236) : Correction on using getInt on a signed smallInt negative value on prepareStatement
* [CONJ-238](https://jira.mariadb.org/browse/CONJ-238) : PrepareStatement prepare exception handling

### Minor

* [CONJ-237](https://jira.mariadb.org/browse/CONJ-237) : Closing a close statement does not throw an Exception anymore
* [CONJ-239](https://jira.mariadb.org/browse/CONJ-239) : Permit commit when in autocommit mode
* [CONJ-240](https://jira.mariadb.org/browse/CONJ-240) : Permit using Connection.setReadOnly(true) during a transaction

## Behavior change

On a master/slave cluster, the driver uses 2 underlying connections: one to a\
master instance, one to a slave instance. When one of the connections fails, if\
the driver needs it right away, it will create a new connection immediately\
before re-executing the query, if possible.

If the failed connection is not needed immediately, this driver will subscribe\
to the "failover reconnection" that will be handled in other threads. Failover\
threads will attempt to create a new connection to replace a failing one, so\
the interruption is minimal for the queries in progress. When the client asks\
to use a failed connection, the new connection created by the failover thread\
will replace the failed one.

Example: after a failure on a slave connection, readonly operations are\
temporary executed on the master connection to avoid interruption on the client\
side. The failover thread will then create a new slave connection that will\
replace the failed one. The next query will use the new slave connection.

A pool of threads is initialized when using a master/slave configuration. The\
pool size evolves according to the number of connections.

More information on GitHub here:[high\
availability documentation](https://github.com/MariaDB/mariadb-connector-j/blob/master/documentation/Failover-and-high-availability)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
