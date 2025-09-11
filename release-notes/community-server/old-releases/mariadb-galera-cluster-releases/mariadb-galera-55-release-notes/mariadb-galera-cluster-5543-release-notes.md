# MariaDB Galera Cluster 5.5.43 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.43)[Release Notes](mariadb-galera-cluster-5543-release-notes.md)[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5543-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 15 May 2015

MariaDB Galera Cluster 5.5.43 is a [_**Stable**_](../../../about/release-criteria.md) (GA) release.\
It is a merge of [MariaDB 5.5.43](../../release-notes-mariadb-5-5-series/mariadb-5543-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 5.5.43, with links to detailed\
information on each push, see the [MariaDB Galera Cluster 5.5.43 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5543-changelog.md).

## Updates and fixes in this version

* Codership changes: `github.com/codership/mysql-wsrep/tree/5.5` (till commit `11dc27f`)
* Fix for [MDEV-8115](https://jira.mariadb.org/browse/MDEV-8115): mysql\_upgrade crashes the server with REPAIR VIEW
* The following [FLUSH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) commands are now executed under total order isolation:
  * FLUSH DES\_KEY\_FILE
  * FLUSH HOSTS
  * FLUSH PRIVILEGES
  * FLUSH QUERY CACHE
  * FLUSH STATUS
  * FLUSH USER\_RESOURCES

### Deprecated Distributions

As per the [MariaDB Deprecation Policy](../../../about/platform-deprecation-policy.md), this will\
be the final release of MariaDB Galera Cluster 5.5 for Fedora 19 "Schrödinger's Cat", Ubuntu\
10.04 LTS "Lucid", and Mint 9 LTS "Isadora". When the next\
version of MariaDB Galera Cluster 5.5 is released, repositories for these distributions will\
go away.

## Notes

* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
  MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x\
  Galera `wsrep` provider. A 25.3.x `wsrep` provider is included in the\
  MariaDB repositories and is also available from the [downloads](https://downloads.mariadb.org/mariadb-galera/5.5.43) page.
* See the [MariaDB 5.5.43 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5543-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5543-changelog.md) for more information on the changes in\
  MariaDB.

Note: If Galera 25.2.x and 25.3.x are both being used in the cluster, MariaDB\
with Galera 25.3.x must be started with [wsrep\_provider\_options='socket.checksum=1'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketchecksum) in order to make it backward\
compatible with Galera v2. Galera wsrep providers other than 25.3.x or 25.2.x\
are not supported.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
