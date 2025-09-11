# MariaDB Galera Cluster 5.5.34 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.34) |**Release Notes** |[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5534-changelog.md) |[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 18 Dec 2013

MariaDB Galera Cluster 5.5.34 is a [_**Stable**_](../../../about/release-criteria.md) (GA) release.\
It is a merge of [MariaDB 5.5.34](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/mariadb-galera-cluster-releases/mariadb-galera-55-release-notes/mariadb-galera-cluster-5534-release-notes) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the Knowledgebase.

For a list of changes made in MariaDB Galera Cluster 5.5.34, with links to detailed\
information on each push, see the [MariaDB Galera Cluster 5.5.34 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5534-changelog.md).

## Includes [MariaDB 5.5.34](../../release-notes-mariadb-5-5-series/mariadb-5534-release-notes.md) and Galera Cluster

MariaDB Galera Cluster 5.5.34 includes [MariaDB 5.5.34](../../release-notes-mariadb-5-5-series/mariadb-5534-release-notes.md) with Codership additions (`lp:codership-mysql/5.5-23` till revision `3942`) and [Galera Cluster 23.2.7](https://codership.com/content/using-galera-cluster). See the [MariaDB 5.5.34 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5534-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5534-changelog.md) for more information on the changes in\
MariaDB.

## Bug Fixes

This release contains fixes for some crashing bugs, memory leaks, compiler\
errors/warnings and improvements in existing scripts.

* [MDEV-5408](https://jira.mariadb.org/browse/MDEV-5408): Crash in mariadb-wsrep during plugin load at startup
* [MDEV-5386](https://jira.mariadb.org/browse/MDEV-5386): Server crashes in thd\_get\_ha\_data on maria-5.5-galera tree while\
  running 'check testcase before test
* [MDEV-443](https://jira.mariadb.org/browse/MDEV-443): Galera: Server crashes on flushing tables for SST if started with\
  character\_set\_server utf16 or utf32 or ucs2, and with wsrep\_sst\_method=rsync
* [MDEV-4227](https://jira.mariadb.org/browse/MDEV-4227): Galera server should stop crashing on setting binlog\_format\
  STATEMENT
* [MDEV-4222](https://jira.mariadb.org/browse/MDEV-4222): Assertion \`( ((global\_system\_variables.wsrep\_on) && (thd &&\
  thd->variables.wsrep\_on)) && wsrep\_emulate\_bin\_log) || mysql\_bin\_log\
  .is\_open()' fails on SAVEPOINT with disabled wsrep\_provider
* [MDEV-4235](https://jira.mariadb.org/browse/MDEV-4235): Galera: Assertion \`0' fails in tdc\_remove\_table on creating a\
  trigger
* [MDEV-4223](https://jira.mariadb.org/browse/MDEV-4223): Galera: InnoDB assertion failure !mutex\_own(mutex) in file\
  sync0sync.ic line 207
* [MDEV-4233](https://jira.mariadb.org/browse/MDEV-4233): Galera: assertion: (lock->trx)->wait\_lock == lock fails in file\
  lock0lock.c line 796

A list of all the bugs fixed can be found in the [changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5534-changelog.md).

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
