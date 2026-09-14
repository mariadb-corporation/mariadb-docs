# MariaDB Galera Cluster 10.0.7 Release Notes

The most recent [MariaDB Galera Cluster 10.0](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7) release is:[**MariaDB Galera Cluster 10.0.38**](mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.7) |**Release Notes** |[Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-1007-changelog.md) |[Overview of MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-guide)

**Release date:** 24 Feb 2014

MariaDB Galera Cluster 10.0.7 is an [_**Alpha**_](../../../about/release-criteria.md) release.\
It is a merge of [MariaDB 10.0.7](../../10.0/changes-improvements-in-mariadb-10-0.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are
available in the [**Galera**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 10.0.7, with links to
detailed information on each push, see the [MariaDB Galera Cluster 10.0.7 Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-1007-changelog.md).

## Includes [MariaDB 10.0.7](../../10.0/10.0.7.md) and Galera Cluster

MariaDB Galera Cluster 10.0.7 includes [MariaDB 10.0.7](../../10.0/10.0.7.md) with Codership additions
(`lp:codership-mysql/5.5` till revision `3944`) and [Galera 25.3.2](https://codership.com/content/using-galera-cluster).\
This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x Galera`wsrep` provider. A 25.3.x `wsrep` provider is included in the MariaDB
repositories. And both 25.3.x and 25.2.x `wsrep` providers are available on the downloads page.

See the [MariaDB 10.0.7 Release Notes](../../10.0/10.0.7.md) and [Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-1007-changelog.md) for more information on the changes in\
MariaDB.

Note: If Galera v2 and v3 are both being used in the cluster, MariaDB with Galera v3 must be started with wsrep\_provider\_options='socket.checksum=1' in order to make it backward compatible with Galera v2.

## First Alpha Release

This is the first alpha release for this series of MariaDB Galera Cluster. It
is being released now to get it into the hands of any who might want to test
it. **Do not run Alpha releases on production systems!**

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
