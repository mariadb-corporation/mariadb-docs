# MariaDB Galera Cluster 5.5.57 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.57)[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5557-release-notes.md)[Changelog](mariadb-galera-cluster-5557-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 26 Jul 2017

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5557-release-notes.md). For changes in\
MariaDB, see the [MariaDB 5.5.57 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5557-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #d9675a10d5](https://github.com/MariaDB/server/commit/d9675a10d5)\
  2017-07-24 20:24:03 +0300
  * Remove unneeded code.
* [Revision #eec6417e05](https://github.com/MariaDB/server/commit/eec6417e05)\
  2017-07-24 16:14:27 +0300
  * Apply galera patches to XtraDB storage engine and remove one debug output.
* [Revision #2aaed4489f](https://github.com/MariaDB/server/commit/2aaed4489f)\
  2017-07-24 15:43:45 +0300
  * Fix regression on galera.partition test case by commenting the problematic condition.
* [Revision #07f8360f17](https://github.com/MariaDB/server/commit/07f8360f17)\
  2017-07-24 11:06:42 +0300
  * [MDEV-10379](https://jira.mariadb.org/browse/MDEV-10379): Failing assertion: xid\_seqno > trx\_sys\_cur\_xid\_seqno
* [Revision #e5c488a49b](https://github.com/MariaDB/server/commit/e5c488a49b)\
  2017-07-21 08:29:52 +0300
  * Fix failing test case.
* [Revision #970859a599](https://github.com/MariaDB/server/commit/970859a599)\
  2017-05-24 14:46:25 +0300
  * MW-383 Bumped wsrep patch version
* [Revision #be416cfa3b](https://github.com/MariaDB/server/commit/be416cfa3b)\
  2017-03-13 22:45:42 +0100
  * MW-86 Removed unnecessary wsrep\_sync\_wait before processing SQLCOM\_REPLACE
* [Revision #34853fa793](https://github.com/MariaDB/server/commit/34853fa793)\
  2017-03-13 15:35:04 +0100
  * MW-86 Additional wsrep\_sync\_wait coverage
* [Revision #a82611771b](https://github.com/MariaDB/server/commit/a82611771b)\
  2017-03-08 13:08:21 +0100
  * MW-86 Add separate wsrep\_sync\_wait bitmask value for SHOW commands
* [Revision #519e4322e1](https://github.com/MariaDB/server/commit/519e4322e1)\
  2017-05-08 23:12:51 +0300
  * MW-369 FK fixes
* [Revision #6326f0eac6](https://github.com/MariaDB/server/commit/6326f0eac6)\
  2017-05-05 11:09:01 +0300
  * MW-322 CTAS fix
* [Revision #20ab1665af](https://github.com/MariaDB/server/commit/20ab1665af)\
  2017-05-05 10:55:45 +0300
  * MW-322 Fix compilation error with debug build
* [Revision #dbda504275](https://github.com/MariaDB/server/commit/dbda504275)\
  2017-07-20 13:52:22 +0300
  * Fix merge error and compiler warning.
* [Revision #48b7245bf2](https://github.com/MariaDB/server/commit/48b7245bf2)\
  2017-04-27 20:28:22 +0300
  * MW-369 - merged fix for FK issue from 5.6-v25 branch
* [Revision #a4bc8db216](https://github.com/MariaDB/server/commit/a4bc8db216)\
  2017-04-27 19:51:18 +0300
  * MW-322 - CTAS fix merged to 5.5-v25 branch
* Merge [Revision #a481de30bb](https://github.com/MariaDB/server/commit/a481de30bb) 2017-07-20 08:56:09 +0300 - Merge tag 'mariadb-5.5.57' into 5.5-galera
* [Revision #e8a2a75121](https://github.com/MariaDB/server/commit/e8a2a75121)\
  2017-06-20 14:29:25 +0530
  * [MDEV-11036](https://jira.mariadb.org/browse/MDEV-11036) Add link wsrep\_sst\_rsync\_wan -> wsrep\_sst\_rsync
* [Revision #9df17790f2](https://github.com/MariaDB/server/commit/9df17790f2)\
  2017-05-03 13:10:17 -0400
  * bump the VERSION

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
