# MariaDB Galera Cluster 5.5.51 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.51)[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5551-release-notes.md)[Changelog](mariadb-galera-cluster-5551-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 15 Aug 2016

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5551-release-notes.md). For changes in\
MariaDB, see the [MariaDB 5.5.51 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5551-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #d40d3f4](https://github.com/MariaDB/server/commit/d40d3f4)\
  2016-07-19 20:44:02 +0000
  * [MDEV-10314](https://jira.mariadb.org/browse/MDEV-10314) : wsrep\_client\_thread was not set in threadpool.
* [Revision #abfbe80](https://github.com/MariaDB/server/commit/abfbe80)\
  2016-08-10 14:48:44 -0400
  * MW-292: Fix test case
* [Revision #dfadb36](https://github.com/MariaDB/server/commit/dfadb36)\
  2016-07-15 01:13:32 -0700
  * Galera MTR Tests: Test case for MW-292 : NOW() returns stale timestamp after transaction replay
* [Revision #9a809fe](https://github.com/MariaDB/server/commit/9a809fe)\
  2016-07-14 14:29:59 +0200
  * MW-292 Reset timestamp after transaction replay
* [Revision #38a0def](https://github.com/MariaDB/server/commit/38a0def)\
  2016-08-10 10:34:54 -0400
  * Merge tag '[mariadb-5.5.51](../../../changelogs/changelogs-mariadb-55-series/mariadb-5551-changelog.md)' into 5.5-galera
* [Revision #44e3046](https://github.com/MariaDB/server/commit/44e3046)\
  2016-08-03 22:15:57 -0400
  * [MDEV-10487](https://jira.mariadb.org/browse/MDEV-10487): Galera SST using rsync does not filter out lost+found

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
