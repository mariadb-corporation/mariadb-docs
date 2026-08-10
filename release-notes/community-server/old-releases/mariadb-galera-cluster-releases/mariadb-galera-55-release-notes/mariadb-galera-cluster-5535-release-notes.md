# MariaDB Galera Cluster 5.5.35 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.35) |**Release Notes** |[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5535-changelog.md) |[Overview of MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-guide)

**Release date:** 14 Feb 2014

MariaDB Galera Cluster 5.5.35 is a [_**Stable**_](../../../about/release-criteria.md) (GA) release.\
It is a merge of [MariaDB 5.5.35](mariadb-galera-cluster-5535-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are
available in the [**Galera**](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 5.5.35, with links to detailed
information on each push, see the [MariaDB Galera Cluster 5.5.35 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5535-changelog.md).

## Includes [MariaDB 5.5.35](../../5.5/5.5.35.md) and Galera

MariaDB Galera Cluster 5.5.35 includes [MariaDB 5.5.35](../../5.5/5.5.35.md) with Codership additions
(`lp:codership-mysql/5.5` till revision `3944`) and [Galera 25.3.2](https://codership.com/content/using-galera-cluster).\
This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x Galera`wsrep` provider. A 25.3.x `wsrep` provider is included in the MariaDB
repositories and both 25.3.x and 25.2.x wsrep providers are available on the downloads page.

See the [MariaDB 5.5.35 Release Notes](../../5.5/5.5.35.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5535-changelog.md) for more information on the changes in\
MariaDB.

Note: If Galera v2 and v3 are both being used in the cluster, MariaDB with Galera v3 must be started with wsrep\_provider\_options='socket.checksum=1' in order to make it backward compatible with Galera v2.

## Bug Fixes

This release contains fixes for bugs, compiler errors/warnings and improvements
in existing scripts.

A list of all the bugs fixed can be found in the [changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5535-changelog.md).

## Fedora, Ubuntu, and Mint

As per the [MariaDB Deprecation Policy](../../../about/platform-deprecation-policy.md), this will
be the final release of MariaDB Galera Cluster for Fedora 18 "Spherical Cow", Ubuntu 13.04\
"Raring", and Mint 15 "Olivia". When the next version of MariaDB Galera Cluster 5.5 is
released, repositories for these distributions will go away.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
