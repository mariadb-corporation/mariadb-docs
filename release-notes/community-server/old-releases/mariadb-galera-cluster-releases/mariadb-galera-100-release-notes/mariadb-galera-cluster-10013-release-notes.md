# MariaDB Galera Cluster 10.0.13 Release Notes

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.13)[Release Notes](mariadb-galera-cluster-10013-release-notes.md)[Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10013-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 3 Sep 2014

This is the 5th release in the MariaDB Galera Cluster 10.0 series. It is a [_**Stable**_](../../../about/release-criteria.md) (GA) release. It is a merge of [MariaDB 10.0.13](../../release-notes-mariadb-10-0-series/mariadb-10013-release-notes.md)\
and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 10.0.13, with links to\
detailed information on each push, see the [MariaDB Galera Cluster 10.0.13 Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10013-changelog.md).

## Updates and fixes in this version

* Galera `garbd` and `libgalera` are now included in the binary tarballs\
  ([MDEV-4463](https://jira.mariadb.org/browse/MDEV-4463))
* Codership changes: `lp:codership-mysql/5.6` (till rev `4123`).
* [Galera library](https://codership.com/content/using-galera-cluster)\
  versions: 25.3.5, 25.2.9
* Supported wsrep interface API version: 25

## Notes

* [Snapshot state transfer](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method): rsync and mysqldump SST methods support [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid). However, xtrabackup-v2\
  and xtrabackup SST methods currently do not support GTID.\
  ([lp:1326967](https://bugs.launchpad.net/percona-xtrabackup/+bug/1326967))
* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* Compatibility: Wsrep providers (Galera libraries) other than version 25.x.xx\
  are not supported.
* Compatibility: If Galera v2 and v3 are both being used in the cluster, MariaDB with\
  Galera v3 must be started with [wsrep\_provider\_options='socket.checksum=1'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketchecksum)\
  in order to make it backward compatible with Galera v2.
* See the [MariaDB 10.0.13 Release Notes](../../release-notes-mariadb-10-0-series/mariadb-10013-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10013-changelog.md) for more information on the changes in\
  MariaDB.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
