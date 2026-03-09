# MariaDB 10.3.30 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.30](https://downloads.mariadb.org/mariadb/10.3.30/)[Release Notes](../../old-releases/10.3/10.3.30.md)[Changelog](mariadb-10330-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 23 Jun 2021

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.30.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.39](../changelogs-mariadb-102-series/mariadb-10239-changelog.md)
* [Revision #75a65d3201](https://github.com/MariaDB/server/commit/75a65d3201)\
  2021-06-09 14:23:20 +0300
  * [MDEV-25886](https://jira.mariadb.org/browse/MDEV-25886) CHECK TABLE crash with DB\_MISSING\_HISTORY if innodb\_read\_only
* Merge [Revision #6e9642beb2](https://github.com/MariaDB/server/commit/6e9642beb2) 2021-06-08 14:33:07 +0300 - Merge 10.2 into 10.3
* [Revision #8149e4d0a1](https://github.com/MariaDB/server/commit/8149e4d0a1)\
  2021-06-07 15:08:18 -0700
  * [MDEV-25682](https://jira.mariadb.org/browse/MDEV-25682) Explain shows an execution plan different from actually executed
* [Revision #b1b4d67bcd](https://github.com/MariaDB/server/commit/b1b4d67bcd)\
  2021-06-04 15:00:34 +0200
  * [MDEV-21373](https://jira.mariadb.org/browse/MDEV-21373) DBUG compilation - bad synchronization in ha\_heap::external\_lock()
* [Revision #2d38c5e64e](https://github.com/MariaDB/server/commit/2d38c5e64e)\
  2021-06-04 09:35:18 +0300
  * [MDEV-17749](https://jira.mariadb.org/browse/MDEV-17749) fixup: ./mtr --embedded main.lock\_kill (again)
* [Revision #663bc849b5](https://github.com/MariaDB/server/commit/663bc849b5)\
  2021-05-26 23:41:59 -0700
  * [MDEV-25714](https://jira.mariadb.org/browse/MDEV-25714) Join using derived with aggregation returns incorrect results
* Merge [Revision #aa70690e9a](https://github.com/MariaDB/server/commit/aa70690e9a) 2021-06-02 08:29:01 +0300 - Merge 10.2 into 10.3
* [Revision #4847a2e730](https://github.com/MariaDB/server/commit/4847a2e730)\
  2021-06-02 08:28:48 +0300
  * [MDEV-17749](https://jira.mariadb.org/browse/MDEV-17749) fixup: ./mtr --embedded main.lock\_kill
* Merge [Revision #950a220060](https://github.com/MariaDB/server/commit/950a220060) 2021-06-01 08:40:59 +0300 - Merge 10.2 into 10.3
* [Revision #1e5ebf3762](https://github.com/MariaDB/server/commit/1e5ebf3762)\
  2021-05-26 14:53:26 +0300
  * Fixed results for main.delete\_use\_source to make it repeatable
* [Revision #aa284e0237](https://github.com/MariaDB/server/commit/aa284e0237)\
  2021-05-26 14:35:23 +0300
  * [MDEV-17749](https://jira.mariadb.org/browse/MDEV-17749) Kill during LOCK TABLE ; ALTER TABLE causes assert
* Merge [Revision #1864a8ea93](https://github.com/MariaDB/server/commit/1864a8ea93) 2021-05-24 09:38:49 +0300 - Merge 10.2 into 10.3
* [Revision #b01a9fd817](https://github.com/MariaDB/server/commit/b01a9fd817)\
  2021-05-21 03:13:37 +0200
  * [MDEV-25719](https://jira.mariadb.org/browse/MDEV-25719): stunnel uses "verifyChain" without subject checks
* Merge [Revision #ca3f497564](https://github.com/MariaDB/server/commit/ca3f497564) 2021-05-18 08:40:19 +0300 - Merge 10.2 into 10.3, except [MDEV-25682](https://jira.mariadb.org/browse/MDEV-25682)
* [Revision #9f03a394ff](https://github.com/MariaDB/server/commit/9f03a394ff)\
  2021-05-17 18:59:26 +0200
  * wsrep\_sst\_common.sh: file mode changed back to 664
* [Revision #f92cd0c56b](https://github.com/MariaDB/server/commit/f92cd0c56b)\
  2021-05-14 12:51:36 +0200
  * [MDEV-25669](https://jira.mariadb.org/browse/MDEV-25669): SST scripts should check all server groups in config files
* [Revision #16437e5e25](https://github.com/MariaDB/server/commit/16437e5e25)\
  2021-05-13 12:23:11 +0200
  * Added missing connection lines to some tests
* [Revision #1447b39475](https://github.com/MariaDB/server/commit/1447b39475)\
  2021-05-07 14:04:24 +0300
  * Updated galera\_3nodes disabled.def file
* [Revision #2d47bad3ac](https://github.com/MariaDB/server/commit/2d47bad3ac)\
  2021-05-11 10:04:52 +0200
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580) addendum: normal operation in configurations where stunnel is not available
* [Revision #7e8a89387b](https://github.com/MariaDB/server/commit/7e8a89387b)\
  2021-05-10 04:27:16 +0200
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580): WSREP\_SST: \[ERROR] rsync daemon port has been taken
* [Revision #bc4d995cfa](https://github.com/MariaDB/server/commit/bc4d995cfa)\
  2021-05-10 10:49:19 -0400
  * bump the VERSION
* Merge [Revision #98e6159892](https://github.com/MariaDB/server/commit/98e6159892) 2021-05-10 09:09:50 +0300 - Merge 10.2 into 10.3
* Merge [Revision #72753d2b65](https://github.com/MariaDB/server/commit/72753d2b65) 2021-05-07 11:51:22 +0200 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #625e44a80d](https://github.com/MariaDB/server/commit/625e44a80d)\
  2021-05-05 15:46:22 +0530
  * [MDEV-25597](https://jira.mariadb.org/browse/MDEV-25597): Disable rpl\_semi\_sync\_slave\_compressed\_protocol.test

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
