# MariaDB Galera Cluster 10.0.14 Release Notes

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.14)[Release Notes](mariadb-galera-cluster-10014-release-notes.md)[Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10014-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 16 Oct 2014

This is the 6th release in the MariaDB Galera Cluster 10.0 series. It is a [_**Stable**_](../../../about/release-criteria.md) (GA) release. It is a merge of [MariaDB 10.0.14](../../release-notes-mariadb-10-0-series/mariadb-10014-release-notes.md)\
and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 10.0.14, with links to\
detailed information on each push, see the [MariaDB Galera Cluster 10.0.14 Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10014-changelog.md).

## Updates and fixes in this version

* Codership changes: `lp:codership-mysql/5.6` (till rev `4144`).
* [Galera library](https://codership.com/content/using-galera-cluster)\
  versions: 25.3.5, 25.2.9
* Supported wsrep interface API version: 25
* Restrictions on the use of the [Query Cache](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/query-cache) in MariaDB Galera\
  Cluster have been lifted with this release.

## Notes

* As per the [MariaDB Deprecation Policy](../../../about/platform-deprecation-policy.md), this will be the last release of MariaDB Galera Cluster 10.0 for both Ubuntu 13.10 "Saucy" and Mint 16 "Petra".
* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* Compatibility: Wsrep providers (Galera libraries) other than version 25.x.xx\
  are not supported.
* Compatibility: If Galera v2 and v3 are both being used in the cluster,\
  MariaDB with Galera v3 must be started with [wsrep\_provider\_options='socket.checksum=1'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketchecksum)\
  in order to make it backward compatible with Galera v2.
* See the [MariaDB 10.0.14 Release Notes](../../release-notes-mariadb-10-0-series/mariadb-10014-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10014-changelog.md) for more information on the changes in\
  MariaDB.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
