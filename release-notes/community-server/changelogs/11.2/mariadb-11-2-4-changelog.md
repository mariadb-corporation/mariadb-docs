# MariaDB 11.2.4 Changelog

The most recent release of [MariaDB 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md) is:[**MariaDB 11.2.6**](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.2.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.2.6/)

[Download 11.2.4](https://downloads.mariadb.org/mariadb/11.2.4/)[Release Notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md)[Changelog](mariadb-11-2-4-changelog.md)[Overview of 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md)

**Release date:** 16 May 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.2) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 11.1.5](../11.1/mariadb-11-1-5-changelog.md)
* [Revision #db06c5dd07](https://github.com/MariaDB/server/commit/db06c5dd07)\
  2024-05-13 11:09:55 +0200
  * main.alter\_table\_online fails in --view
* Merge [Revision #bf5da43e50](https://github.com/MariaDB/server/commit/bf5da43e50) 2024-05-13 10:00:26 +0200 - Merge branch '11.1' into 11.2
* [Revision #f8621f2a16](https://github.com/MariaDB/server/commit/f8621f2a16)\
  2024-05-12 23:08:04 +0200
  * remove redundant slow tests
* [Revision #5669cb7323](https://github.com/MariaDB/server/commit/5669cb7323)\
  2024-03-05 02:48:14 +0100
  * fix race in the [MDEV-32614](https://jira.mariadb.org/browse/MDEV-32614) test
* [Revision #c436b6a2bc](https://github.com/MariaDB/server/commit/c436b6a2bc)\
  2024-03-05 02:38:04 +0100
  * [MDEV-33450](https://jira.mariadb.org/browse/MDEV-33450) Assertion fails in main.alter\_table\_online\_debug
* [Revision #398ae9ee3c](https://github.com/MariaDB/server/commit/398ae9ee3c)\
  2024-02-29 22:52:08 +0100
  * [MDEV-33330](https://jira.mariadb.org/browse/MDEV-33330) Server crash or assertion failure in binlog\_get\_pending\_rows\_event
* [Revision #7fe764b109](https://github.com/MariaDB/server/commit/7fe764b109)\
  2024-04-22 22:51:23 +0200
  * [MDEV-32973](https://jira.mariadb.org/browse/MDEV-32973) SHOW TABLES LIKE shows temporary tables with non-matching names
* [Revision #4a35a3b50d](https://github.com/MariaDB/server/commit/4a35a3b50d)\
  2024-03-25 13:37:22 -0300
  * [MDEV-33659](https://jira.mariadb.org/browse/MDEV-33659) Server crashed at Create\_func\_aes\_decrypt::create\_native
* [Revision #0b8c5d74fc](https://github.com/MariaDB/server/commit/0b8c5d74fc)\
  2024-03-02 00:28:02 +0000
  * Update URLs in test\_upgrade script
* Merge [Revision #cd28b2479c](https://github.com/MariaDB/server/commit/cd28b2479c) 2024-04-09 12:12:33 +0200 - Merge branch '11.1' into 11.2
* [Revision #b620b3949a](https://github.com/MariaDB/server/commit/b620b3949a)\
  2024-03-18 17:43:16 +0700
  * [MDEV-33525](https://jira.mariadb.org/browse/MDEV-33525): Recreate/reuse temporary table
* Merge [Revision #1553a9dd79](https://github.com/MariaDB/server/commit/1553a9dd79) 2024-02-07 08:50:01 +0100 - Merge branch '11.2' into mariadb-11.2.3
* [Revision #35c19700bb](https://github.com/MariaDB/server/commit/35c19700bb)\
  2024-02-06 08:29:54 -0500
  * bump the VERSION
* [Revision #5d37cac793](https://github.com/MariaDB/server/commit/5d37cac793)\
  2024-02-03 06:40:06 +0100
  * [MDEV-33348](https://jira.mariadb.org/browse/MDEV-33348) ALTER TABLE lock waiting stages are indistinguishable
* [Revision #ba6f9943b2](https://github.com/MariaDB/server/commit/ba6f9943b2)\
  2024-01-31 22:04:39 +0100
  * online alter: show examined rows in the progress report
* [Revision #3059f274fb](https://github.com/MariaDB/server/commit/3059f274fb)\
  2024-01-31 19:59:07 +0100
  * online alter: relax the lock to upgrade to on the last replication stage
* [Revision #dccce98388](https://github.com/MariaDB/server/commit/dccce98388)\
  2024-01-17 21:26:52 +0100
  * unpack\_row+binlog\_cache\_data: fix unused variable
* [Revision #9599cbc28d](https://github.com/MariaDB/server/commit/9599cbc28d)\
  2024-01-09 12:37:26 +0100
  * online\_alter: clean up usage of cleanup\_cache\_list
* [Revision #50095046f3](https://github.com/MariaDB/server/commit/50095046f3)\
  2024-01-02 18:45:43 +0100
  * [MDEV-32614](https://jira.mariadb.org/browse/MDEV-32614) LeakSanitizer errors in copy\_data\_between\_tables
* [Revision #c2e16b3ad5](https://github.com/MariaDB/server/commit/c2e16b3ad5)\
  2023-11-17 23:40:10 +0100
  * [MDEV-32803](https://jira.mariadb.org/browse/MDEV-32803) Assertion \`total == 0' failed in Event\_log::write\_cache\_raw

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
