# MariaDB Galera Cluster 5.5.42 Release Notes

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.42)[Release Notes](mariadb-galera-cluster-5542-release-notes.md)[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5542-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 11 Mar 2015

MariaDB Galera Cluster 5.5.42 is a [_**Stable**_](../../../about/release-criteria.md) (GA) release.\
It is a merge of [MariaDB 5.5.42](../../release-notes-mariadb-5-5-series/mariadb-5542-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 5.5.42, with links to detailed\
information on each push, see the [MariaDB Galera Cluster 5.5.42 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5542-changelog.md).

## Updates and fixes in this version

* Codership changes: `lp:codership-mysql/5.5` (till revision `4026`)
* The [Galera library](https://codership.com/content/using-galera-cluster) used\
  by MariaDB Galera Cluster and included in the MariaDB repositories has been\
  updated to version 25.3.9.
* On Ubuntu and Debian, as part of the upgrade to Galera version 25.3.9, the\
  Galera Arbitrator daemon (garbd) and the galera library have been renamed and\
  split into separate packages. The packages are named galera-3\
  and galera-arbitrator-3. When installing MariaDB Galera Cluster on Ubuntu\
  and Debian (the mariadb-galera-server package), the galera-3 package will\
  be automatically installed. You can then install the arbitrator package on a\
  separate node (recommended) or on one of the nodes running\
  mariadb-galera-server (not recommended).

## Notes

* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
  MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x\
  Galera `wsrep` provider. A 25.3.x `wsrep` provider is included in the\
  MariaDB repositories and is also available from the [downloads](https://downloads.mariadb.org/mariadb-galera/5.5.42) page.
* See the [MariaDB 5.5.42 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5542-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5542-changelog.md) for more information on the changes in\
  MariaDB.

Note: If Galera 25.2.x and 25.3.x are both being used in the cluster, MariaDB\
with Galera 25.3.x must be started with [wsrep\_provider\_options='socket.checksum=1'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketchecksum) in order to make it backward\
compatible with Galera v2. Galera wsrep providers other than 25.3.x or 25.2.x\
are not supported.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
