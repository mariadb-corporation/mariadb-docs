# MariaDB Galera 5.5.32 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.32) |**Release Notes** |[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-5532-changelog.md) |[Overview of Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 30 Aug 2013

[MariaDB Galera 5.5.32](mariadb-galera-5532-release-notes.md) is a [_**Stable**_](../../../about/release-criteria.md) (GA) release.\
It is a merge of [MariaDB 5.5.32](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/mariadb-galera-cluster-releases/mariadb-galera-55-release-notes/mariadb-galera-5532-release-notes) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the Knowledgebase.

For a list of changes made in [MariaDB Galera 5.5.32](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-galera-cluster-5532-release-notes/README.md), with links to detailed\
information on each push, see the [MariaDB Galera 5.5.32 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-5532-changelog.md).

## Includes [MariaDB 5.5.32](../../release-notes-mariadb-5-5-series/mariadb-5532-release-notes.md) and Galera Cluster

[MariaDB Galera 5.5.32](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-galera-cluster-5532-release-notes/README.md) includes [MariaDB 5.5.32](../../release-notes-mariadb-5-5-series/mariadb-5532-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster). See the [MariaDB 5.5.32](../../release-notes-mariadb-5-5-series/mariadb-5532-release-notes.md) [Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5532-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5532-changelog.md) for more information on the changes in [MariaDB 5.5.32](../../release-notes-mariadb-5-5-series/mariadb-5532-release-notes.md).

## Includes Galera wsrep provider version 23.2.6

The Galera library on Ubuntu/Debian, and x86\_64 versions of Red Hat 6, CentOS\
6, and Fedora has been updated to version 23.2.6.

## Packaging Fixes

This version includes several packaging fixes including a fix for [MDEV-4229](https://jira.mariadb.org/browse/MDEV-4229)\
regarding binaries for Debian Wheezy.

One packaging fix that still exists is one that prevents the installation of\
the wsrep package on Fedora systems ([MDEV-4141](https://jira.mariadb.org/browse/MDEV-4141)). It is hoped this issue will be fixed soon. When it is this paragraph will be updated. For now, Fedora packages are in the repository, but the galera package must be installed manually, and may not work even then.

## Other fixes

* [MDEV-4953](https://jira.mariadb.org/browse/MDEV-4953) Delete on a partioned table is not replicated
* LOAD DATA INFILE now supports big data files by introducing transaction\
  splitting, which is controlled via the [wsrep\_load\_data\_splitting](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables) global\
  variable

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
