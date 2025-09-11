# MariaDB Galera Cluster 10.0.16 Release Notes

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.16)[Release Notes](mariadb-galera-cluster-10016-release-notes.md)[Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10016-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 29 Jan 2015

This is a release in the MariaDB Galera Cluster 10.0 series. It is a [_**Stable**_](../../../about/release-criteria.md) (GA) release. It is a merge of [MariaDB 10.0.16](../../release-notes-mariadb-10-0-series/mariadb-10016-release-notes.md)\
and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 10.0.16, with links to\
detailed information on each push, see the [MariaDB Galera Cluster 10.0.16 Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10016-changelog.md).

## Updates and fixes in this version

* Codership changes: `lp:codership-mysql/5.6` (till rev `4144`).
* [Galera library](https://codership.com/content/using-galera-cluster)\
  versions: 25.3.5, 25.2.9
* Supported wsrep interface API version: 25

## Notes

* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* New session-only system variable :[wsrep\_dirty\_reads](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_dirty_reads)\
  ([MDEV-7476](https://jira.mariadb.org/browse/MDEV-7476))
* MariaDB Galera Cluster supports ROW binlog\_format only, thus it discards any\
  request of setting it to any value other than ROW with an error. With this\
  release, this restriction has been eased a bit to allow setting of\
  binlog\_format to other formats at SESSION scope. ([MDEV-7322](https://jira.mariadb.org/browse/MDEV-7322))
* Compatibility: Wsrep providers (Galera libraries) other than version 25.x.xx\
  are not supported.
* Compatibility: If Galera v2 and v3 are both being used in the cluster,\
  MariaDB with Galera v3 must be started with [wsrep\_provider\_options='socket.checksum=1'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketchecksum)\
  in order to make it backward compatible with Galera v2.
* See the [MariaDB 10.0.16 Release Notes](../../release-notes-mariadb-10-0-series/mariadb-10016-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10016-changelog.md) for more information on the changes in\
  MariaDB.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
