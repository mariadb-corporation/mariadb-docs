# MariaDB Galera Cluster 5.5.46 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.46)[Release Notes](mariadb-galera-cluster-5546-release-notes.md)[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5546-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 20 Oct 2015

MariaDB Galera Cluster 5.5.46 is a [_**Stable**_](../../../about/release-criteria.md) (GA)\
release. It is a merge of [MariaDB 5.5.46](../../release-notes-mariadb-5-5-series/mariadb-5546-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 5.5.46, with links to detailed\
information on each push, see the [MariaDB Galera Cluster 5.5.46 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5546-changelog.md).

## Updates and fixes in this version

* This release is mainly a bug-fix release.
* Codership changes:[github.com/codership/mysql-wsrep/tree/5.5](https://github.com/codership/mysql-wsrep/tree/5.5)\
  (till commit `4f81026`)
* The [Galera library](https://codership.com/content/using-galera-cluster) used\
  by MariaDB Galera Cluster and included in the MariaDB repositories is\
  currently at version 25.3.9.
* [MDEV-5146](https://jira.mariadb.org/browse/MDEV-5146): Updates from LOAD DATA on a partitioned table were not getting\
  replicated to other nodes in the cluster
* [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): A node could crash during startup
* [MDEV-8834](https://jira.mariadb.org/browse/MDEV-8834): In a concurrent scenario, a session was able to write to a\
  read\_only node

### Deprecated Distributions

As per the [MariaDB Deprecation Policy](../../../about/platform-deprecation-policy.md), this will be the last release of MariaDB Galera Cluster 5.5 for Ubuntu 14.10 "Utopic" and Fedora 20.

## Notes

* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
  MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x\
  Galera `wsrep` provider. A 25.3.x `wsrep` provider is included in the\
  MariaDB repositories and is also available from the [downloads](https://downloads.mariadb.org/mariadb-galera/5.5.46) page.
* See the [MariaDB 5.5.46 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5546-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5546-changelog.md) for more information on the changes in\
  MariaDB.

Note: If Galera 25.2.x and 25.3.x are both being used in the cluster, MariaDB\
with Galera 25.3.x must be started with [wsrep\_provider\_options='socket.checksum=1'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketchecksum) in order to make it backward\
compatible with Galera v2. Galera wsrep providers other than 25.3.x or 25.2.x\
are not supported.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
