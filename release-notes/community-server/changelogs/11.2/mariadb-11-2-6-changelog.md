# MariaDB 11.2.6 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md)[Changelog](mariadb-11-2-6-changelog.md)[Overview of 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.2.6/)

**Release date:** 1 Nov 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.2) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.11.10](../10.11/10.11.10.md)
* Includes all fixes from [MariaDB 11.1.6](../11.1/mariadb-11-1-6-changelog.md)
* [Revision #67c0fd2a41](https://github.com/MariaDB/server/commit/67c0fd2a41)\
  2024-10-30 09:36:12 +0200
  * [MDEV-35289](https://jira.mariadb.org/browse/MDEV-35289) innodb\_fast\_shutdown=0 might corrupt the system tablespace on 32-bit systems
* [Revision #45e1ddc00f](https://github.com/MariaDB/server/commit/45e1ddc00f)\
  2024-10-29 16:42:52 +0100
  * Revert "don't disable lto in DEB builds"
* Merge [Revision #69d033d165](https://github.com/MariaDB/server/commit/69d033d165) 2024-10-29 16:39:47 +0100 - Merge branch '10.11' into 11.2
* [Revision #52723ec09a](https://github.com/MariaDB/server/commit/52723ec09a)\
  2024-10-28 18:48:55 +0700
  * [MDEV-34880](https://jira.mariadb.org/browse/MDEV-34880) Incorrect result for query with derived table having TEXT field
* [Revision #6bd1cb0ea0](https://github.com/MariaDB/server/commit/6bd1cb0ea0)\
  2024-09-29 20:50:58 +0700
  * [MDEV-34880](https://jira.mariadb.org/browse/MDEV-34880) Incorrect result for query with derived table having TEXT field
* Merge [Revision #ebefef658e](https://github.com/MariaDB/server/commit/ebefef658e) 2024-10-18 11:32:22 +0300 - Merge 10.11 into 11.2
* [Revision #4a1ded61a4](https://github.com/MariaDB/server/commit/4a1ded61a4)\
  2024-10-16 21:34:24 +0530
  * [MDEV-34529](https://jira.mariadb.org/browse/MDEV-34529) Shrink the system tablespace when system tablespace contains [MDEV-30671](https://jira.mariadb.org/browse/MDEV-30671) leaked undo pages
* [Revision #66b8d32b75](https://github.com/MariaDB/server/commit/66b8d32b75)\
  2024-10-10 12:33:59 +0300
  * [MDEV-35072](https://jira.mariadb.org/browse/MDEV-35072): Assertion with optimizer\_join\_limit\_pref\_ratio and 1-table select
* [Revision #690f8a91f9](https://github.com/MariaDB/server/commit/690f8a91f9)\
  2024-10-04 17:14:58 +1000
  * [MDEV-35073](https://jira.mariadb.org/browse/MDEV-35073) Fix -Wmaybe-uninitialized in spider\_conn\_first\_link\_idx
* Merge [Revision #12a91b57e2](https://github.com/MariaDB/server/commit/12a91b57e2) 2024-10-03 13:24:43 +0300 - Merge 10.11 into 11.2
* Merge [Revision #f1b4d36cc3](https://github.com/MariaDB/server/commit/f1b4d36cc3) 2024-09-24 05:23:37 +0200 - Merge branch '10.11' into '11.2'
* [Revision #68e968bc98](https://github.com/MariaDB/server/commit/68e968bc98)\
  2024-09-19 11:15:38 +0200
  * [MDEV-30822](https://jira.mariadb.org/browse/MDEV-30822): Adjust wsrep\_sst\_mariadb-backup.sh to understand both pre-[MDEV-18931](https://jira.mariadb.org/browse/MDEV-18931) and post-[MDEV-18931](https://jira.mariadb.org/browse/MDEV-18931) file naming
* Merge [Revision #e782e416ac](https://github.com/MariaDB/server/commit/e782e416ac) 2024-09-18 07:38:49 +0300 - Merge 10.11 into 11.2
* [Revision #64b75865d5](https://github.com/MariaDB/server/commit/64b75865d5)\
  2024-09-18 07:06:35 +0300
  * [MDEV-34823](https://jira.mariadb.org/browse/MDEV-34823) after-merge fix
* Merge [Revision #ff88633b9c](https://github.com/MariaDB/server/commit/ff88633b9c) 2024-09-18 10:45:26 +1000 - Merge branch '10.11' into 11.2
* Merge [Revision #cfa9784edb](https://github.com/MariaDB/server/commit/cfa9784edb) 2024-09-18 10:25:16 +1000 - Merge branch '10.11' into 11.2
* Merge [Revision #5cd3fa81ef](https://github.com/MariaDB/server/commit/5cd3fa81ef) 2024-09-17 12:34:33 +0300 - Merge 10.11 -> 11.2
* Merge [Revision #f0de610d0c](https://github.com/MariaDB/server/commit/f0de610d0c) 2024-09-10 18:35:16 +0300 - Merge 10.11 into 11.2
* Merge [Revision #abd98336d2](https://github.com/MariaDB/server/commit/abd98336d2) 2024-09-09 13:25:40 +0300 - Merge 10.11 -> 11.2
* [Revision #06ad31d4b6](https://github.com/MariaDB/server/commit/06ad31d4b6)\
  2024-09-09 14:34:14 +0530
  * [MDEV-34855](https://jira.mariadb.org/browse/MDEV-34855) Bootstrap hangs while shrinking the system tablespace
* Merge [Revision #e91a799458](https://github.com/MariaDB/server/commit/e91a799458) 2024-08-29 16:02:57 +0300 - Merge 10.11 into 11.2
* Merge [Revision #6197e6abc4](https://github.com/MariaDB/server/commit/6197e6abc4) 2024-08-21 07:58:46 +0200 - Merge branch '10.11' into 11.2
* Merge [Revision #2b11450d09](https://github.com/MariaDB/server/commit/2b11450d09) 2024-08-20 11:29:44 +0200 - Merge branch '11.1' into 11.2
* Merge [Revision #3e3a326108](https://github.com/MariaDB/server/commit/3e3a326108) 2024-08-09 08:57:07 +0200 - Merge branch '11.1' into mariadb-11.1.6
* [Revision #fdaa44a416](https://github.com/MariaDB/server/commit/fdaa44a416)\
  2024-08-08 18:01:18 -0400
  * bump the VERSION
* [Revision #73b58ac487](https://github.com/MariaDB/server/commit/73b58ac487)\
  2024-08-01 13:07:12 +0700
  * [MDEV-34649](https://jira.mariadb.org/browse/MDEV-34649): Memory leaks on running DELETE statement in PS mode with positional parameters
* [Revision #12b01d740b](https://github.com/MariaDB/server/commit/12b01d740b)\
  2024-08-13 08:20:18 +0300
  * [MDEV-34707](https://jira.mariadb.org/browse/MDEV-34707): BUF\_GET\_RECOVER assertion failure on upgrade
* Merge [Revision #a851760889](https://github.com/MariaDB/server/commit/a851760889) 2024-08-09 08:59:38 +0200 - Merge branch '11.2' into mariadb-11.2.5
* [Revision #9a56a31561](https://github.com/MariaDB/server/commit/9a56a31561)\
  2024-08-08 18:02:30 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
