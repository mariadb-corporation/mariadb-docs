# MariaDB Galera Cluster 10.0.12 Release Notes

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.12)[Release Notes](mariadb-galera-cluster-10012-release-notes.md)[Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10012-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 28 Jun 2014

This is the 4th release in the MariaDB Galera Cluster 10.0 series. It is a [_**Stable**_](../../../about/release-criteria.md) (GA) release. It is a merge of [MariaDB 10.0.12](../../release-notes-mariadb-10-0-series/mariadb-10012-release-notes.md)\
and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 10.0.12, with links to\
detailed information on each push, see the [MariaDB Galera Cluster 10.0.12 Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10012-changelog.md).

## Updates and fixes in this version

* Galera `garbd` and `libgalera` are now included in the binary tarballs\
  ([MDEV-4463](https://jira.mariadb.org/browse/MDEV-4463))
* Codership changes: `lp:codership-mysql/5.6` (till rev `4101`).
* [Galera library](https://codership.com/content/using-galera-cluster)\
  versions: 25.3.5, 25.2.9
* Supported wsrep interface API version: 25

## Notes

* Snapshot state transfer: rsync and mysqldump SST methods support GTID. However, xtrabackup-v2\
  and xtrabackup SST methods currently do not support GTID.\
  ([lp:1326967](https://bugs.launchpad.net/percona-xtrabackup/+bug/1326967))
* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* Compatibility: Wsrep providers (Galera libraries) other than version 25.x.xx\
  are not supported.
* Compatibility: If Galera v2 and v3 are both being used in the cluster, MariaDB with\
  Galera v3 must be started with [wsrep\_provider\_options='socket.checksum=1'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketchecksum)\
  in order to make it backward compatible with Galera v2.
* Installation: Galera rpm packages had a file conflicting with Filesystem package, which caused installation to fail. Fixed Galera packages are now available for the following flavors : Fedora 19, Fedora 20 and CentOS 6. ([MDEV-4218](https://jira.mariadb.org/browse/MDEV-4218))
* See the [MariaDB 10.0.12 Release Notes](../../release-notes-mariadb-10-0-series/mariadb-10012-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10012-changelog.md) for more information on the changes in\
  MariaDB.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
