# MariaDB Galera Cluster 5.5.38 Release Notes

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.38)[Release Notes](mariadb-galera-cluster-5538-release-notes.md)[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5538-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 25 Jun 2014

MariaDB Galera Cluster 5.5.38 is a [_**Stable**_](../../../about/release-criteria.md) (GA) release.\
It is a merge of [MariaDB 5.5.38](../../release-notes-mariadb-5-5-series/mariadb-5538-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 5.5.38, with links to detailed\
information on each push, see the [MariaDB Galera Cluster 5.5.38 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5538-changelog.md).

## Notes about this release

* MariaDB Galera Cluster 5.5.38 includes [MariaDB 5.5.38](../../release-notes-mariadb-5-5-series/mariadb-5538-release-notes.md) with Codership\
  additions (`lp:codership-mysql/5.5` till revision `3997`) and [Galera 25.3.5](https://codership.com/content/using-galera-cluster).
* This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
  MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x\
  Galera `wsrep` provider. A 25.3.x `wsrep` provider is included in the\
  MariaDB repositories and both 25.3.x and 25.2.x wsrep providers are available\
  on the [downloads](https://downloads.mariadb.org/mariadb-galera/5.5.38) page.
* wsrep\_sst\_rsync (sst script) in MariaDB Galera Cluster 5.5.38 uses `lsof` which might not be installed by default on some linux distributions. It has to be installed if the `wsrep_sst_method` is set to `rsync` (default). Package managers should be able to automatically resolve this dependency ([MDEV-6264](https://jira.mariadb.org/browse/MDEV-6264)).
* Galera rpm packages had a file conflicting with Filesystem package ([MDEV-4218](https://jira.mariadb.org/browse/MDEV-4218)), which caused installation to fail. Fixed Galera packages are now available for the following flavors : Fedora 19, Fedora 20 and CentOS 6.

See the [MariaDB 5.5.38 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5538-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5538-changelog.md) for more information on the changes in\
MariaDB.

Note: If Galera 25.2.x and 25.3.x are both being used in the cluster, MariaDB\
with Galera 25.3.x must be started with`wsrep_provider_options='socket.checksum=1'` in order to make it backward\
compatible with Galera v2. Galera wsrep providers other than 25.3.x or 25.2.x\
are not supported.

## Bug Fixes

This release contains fixes for bugs, compiler errors/warnings and improvements\
in existing scripts.

A list of all the bugs fixed can be found in the [changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5538-changelog.md).

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
