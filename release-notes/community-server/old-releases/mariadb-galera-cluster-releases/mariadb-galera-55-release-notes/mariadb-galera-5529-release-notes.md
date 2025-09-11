# MariaDB Galera 5.5.29 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.29) |**Release Notes** |[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-5529-changelog.md) |[Overview of Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 5 Mar 2013

[MariaDB Galera 5.5.29](mariadb-galera-5529-release-notes.md) is a [_**Stable**_](../../../about/release-criteria.md) (GA) release. In general this means that there are no known serious bugs, except for those marked as feature requests, that no bugs were fixed since last release that caused a notable code changes, and that we believe the code is ready for general usage (based on bug inflow). It is a merge of [MariaDB 5.5.29](../../release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with some additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) section of the Knowledgebase.

For a list of changes made in [MariaDB Galera 5.5.29](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-galera-cluster-5529-release-notes/README.md), with links to detailed\
information on each push, see the [MariaDB Galera 5.5.29 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-5529-changelog.md).

In most respects [MariaDB](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb/README.md) will work exactly as MySQL: all commands,\
interfaces, libraries and APIs that exist in MySQL also exist in MariaDB.

## Includes [MariaDB 5.5.29](../../release-notes-mariadb-5-5-series/mariadb-5529-release-notes.md) and Galera Cluster

[MariaDB Galera 5.5.29](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-galera-cluster-5529-release-notes/README.md) includes [MariaDB 5.5.29](../../release-notes-mariadb-5-5-series/mariadb-5529-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster). See the [MariaDB 5.5.29](../../release-notes-mariadb-5-5-series/mariadb-5529-release-notes.md) [Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5529-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5529-changelog.md) for more information on the changes in [MariaDB 5.5.29](../../release-notes-mariadb-5-5-series/mariadb-5529-release-notes.md).

## Combined Repositories

The repositories for MariaDB and MariaDB Galera Cluster are combined. Please\
visit the [MariaDB Repository Configuration Tool](https://downloads.mariadb.org/mariadb/repositories/)\
to generate commands suitable for many different Linux Distributions.

When using the repositories to install MariaDB Galera Cluster, the only\
difference between it and installing MariaDB is to specify the MariaDB Galera\
Server package instead of the MariaDB Server package and to install the Galera\
package. For example, on Ubuntu, after updating the mariadb.list file the\
following command will install MariaDB Galera Server:

```bash
sudo apt-get update
sudo apt-get install mariadb-galera-server galera
```

If MariaDB is already installed on the server the package manager will\
uninstall the appropriate packages prior to installing the MariaDB Galera\
Cluster packages.

See the [MariaDB 5.5.29 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5529-changelog.md) for full details\
of the many packaging and other fixes.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
