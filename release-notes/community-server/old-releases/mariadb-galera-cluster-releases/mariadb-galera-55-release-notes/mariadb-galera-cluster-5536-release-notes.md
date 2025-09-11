# MariaDB Galera Cluster 5.5.36 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.36) |**Release Notes** |[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5536-changelog.md) |[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 12 Mar 2014

MariaDB Galera Cluster 5.5.36 is a [_**Stable**_](../../../about/release-criteria.md) (GA) release.\
It is a merge of [MariaDB 5.5.36](../../release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 5.5.36, with links to detailed\
information on each push, see the [MariaDB Galera Cluster 5.5.36 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5536-changelog.md).

## Includes [MariaDB 5.5.36](../../release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md) and Galera

MariaDB Galera Cluster 5.5.36 includes [MariaDB 5.5.36](../../release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md) with Codership additions\
(`lp:codership-mysql/5.5` till revision `3944`) and [Galera 25.3.2](https://codership.com/content/using-galera-cluster).\
This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x Galera`wsrep` provider. A 25.3.x `wsrep` provider is included in the MariaDB\
repositories and both 25.3.x and 25.2.x wsrep providers are available on the downloads page.

See the [MariaDB 5.5.36 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5536-changelog.md) for more information on the changes in\
MariaDB.

Important : While upgrading the nodes of a MariaDB Galera cluster care must be\
taken when using different versions of Galera library (wsrep provider). A\
MariaDB Galera cluster node with Galera version 3 (25.3.xx) might fail to join\
an existing cluster running with Galera 2 (25.2.xx) nodes. This happens due to\
difference in the default values of 'socket.checksum' for Galera 2 and Galera 3\
libraries.\
So, in order to fix this, the node with Galera 3 should be started\
with an additional wsrep provider option: `socket.checksum=1` in\
order to make it backward compatible with nodes running with Galera 2.\
For example:

```
--wsrep_provider_options='socket.checksum=1; [other provider options; ...]'
```

## Bug Fixes

This release contains fixes for bugs, compiler errors/warnings and improvements\
in existing scripts.

A list of all the bugs fixed can be found in the [changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5536-changelog.md).

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
