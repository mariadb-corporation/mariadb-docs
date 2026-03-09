# MariaDB 10.3.33 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.33](https://mariadb.org/download/?tab=mariadb\&release=10.3.33\&product=mariadb)[Release Notes](../../old-releases/10.3/10.3.33.md)[Changelog](mariadb-10333-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 9 Feb 2022

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.33.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.42](../changelogs-mariadb-102-series/mariadb-10242-changelog.md)
* Merge [Revision #41a163ac5c](https://github.com/MariaDB/server/commit/41a163ac5c) 2022-01-29 15:41:05 +0100 - Merge branch '10.2' into 10.3
* [Revision #a85d942be9](https://github.com/MariaDB/server/commit/a85d942be9)\
  2022-01-27 19:15:02 +0200
  * Fixed result file for rocksdb.i\_s\_deadlock
* [Revision #2f5d6ef039](https://github.com/MariaDB/server/commit/2f5d6ef039)\
  2022-01-27 17:00:52 +0200
  * Fixed random failure main/truncate\_notembedded
* [Revision #20a91b8fc5](https://github.com/MariaDB/server/commit/20a91b8fc5)\
  2022-01-27 16:37:58 +0200
  * [MDEV-27477](https://jira.mariadb.org/browse/MDEV-27477) Remaining SUSE patches for 10.2+
* [Revision #008c02c987](https://github.com/MariaDB/server/commit/008c02c987)\
  2022-01-27 16:12:16 +0200
  * [MDEV-27477](https://jira.mariadb.org/browse/MDEV-27477) Remaining SUSE patches for 10.2+
* [Revision #37886a29e5](https://github.com/MariaDB/server/commit/37886a29e5)\
  2022-01-27 16:07:02 +0200
  * Updated comment in systemd.cmake
* [Revision #020dc54dab](https://github.com/MariaDB/server/commit/020dc54dab)\
  2021-11-02 16:21:11 +0400
  * [MDEV-20770](https://jira.mariadb.org/browse/MDEV-20770) Server crashes in JOIN::transform\_in\_predicates\_into\_in\_subq upon 2nd execution of PS/SP comparing GEOMETRY with other types.
* [Revision #0041265671](https://github.com/MariaDB/server/commit/0041265671)\
  2022-01-24 23:14:46 -0800
  * [MDEV-27510](https://jira.mariadb.org/browse/MDEV-27510) Query returns wrong result when using split optimization
* [Revision #da37bfd8d6](https://github.com/MariaDB/server/commit/da37bfd8d6)\
  2021-12-28 17:43:40 +0400
  * [MDEV-18918](https://jira.mariadb.org/browse/MDEV-18918) SQL mode EMPTY\_STRING\_IS\_NULL breaks RBR upon CREATE TABLE .. SELECT
* [Revision #466d81709b](https://github.com/MariaDB/server/commit/466d81709b)\
  2021-10-05 12:56:11 +0400
  * [MDEV-26768](https://jira.mariadb.org/browse/MDEV-26768) Spider table crashes the server after the mysql\_list\_fields() client's call and produces weird result for SHOW FIELDS.
* [Revision #7922fbf7b7](https://github.com/MariaDB/server/commit/7922fbf7b7)\
  2021-11-23 17:55:08 +0300
  * [MDEV-26249](https://jira.mariadb.org/browse/MDEV-26249): Crash in Explain\_node::print\_explain\_for\_children with slow query log
* [Revision #dfbfd39e85](https://github.com/MariaDB/server/commit/dfbfd39e85)\
  2022-01-19 17:00:46 +0200
  * Updated rocksdb.corrupted\_data\_reads\_debug result file
* [Revision #97425f740f](https://github.com/MariaDB/server/commit/97425f740f)\
  2022-01-13 22:46:59 -0800
  * [MDEV-27132](https://jira.mariadb.org/browse/MDEV-27132) Wrong result from query when using split optimization
* [Revision #7105c810bd](https://github.com/MariaDB/server/commit/7105c810bd)\
  2022-01-15 14:17:19 +0300
  * [MDEV-27217](https://jira.mariadb.org/browse/MDEV-27217) typo fix
* [Revision #c81677bebb](https://github.com/MariaDB/server/commit/c81677bebb)\
  2022-01-14 12:00:46 +0300
  * rocksdb.tbl\_opt\_data\_index\_dir test fix
* [Revision #585cb18ed1](https://github.com/MariaDB/server/commit/585cb18ed1)\
  2022-01-13 23:35:17 +0300
  * [MDEV-27452](https://jira.mariadb.org/browse/MDEV-27452) TIMESTAMP(0) system field is allowed for certain creation of system-versioned table
* [Revision #241ac79e49](https://github.com/MariaDB/server/commit/241ac79e49)\
  2022-01-13 23:35:17 +0300
  * [MDEV-26778](https://jira.mariadb.org/browse/MDEV-26778) row\_start is not updated in current row for InnoDB
* [Revision #7c61fb2fe2](https://github.com/MariaDB/server/commit/7c61fb2fe2)\
  2022-01-13 23:35:17 +0300
  * [MDEV-27217](https://jira.mariadb.org/browse/MDEV-27217) ha\_partition::start\_stmt() ignored error fix
* [Revision #4d5ae2b325](https://github.com/MariaDB/server/commit/4d5ae2b325)\
  2022-01-13 23:35:16 +0300
  * [MDEV-27217](https://jira.mariadb.org/browse/MDEV-27217) DELETE partition selection doesn't work for history partitions
* [Revision #f9f6b190cc](https://github.com/MariaDB/server/commit/f9f6b190cc)\
  2022-01-13 23:35:16 +0300
  * Versioning test suite cleanups
* [Revision #c04adce8ac](https://github.com/MariaDB/server/commit/c04adce8ac)\
  2022-01-04 00:01:52 +0300
  * [MDEV-26337](https://jira.mariadb.org/browse/MDEV-26337): subquery with groupby and ROLLUP returns incorrect results on LEFT JOIN on INDEXED values
* [Revision #25f598f54f](https://github.com/MariaDB/server/commit/25f598f54f)\
  2021-11-16 12:53:51 +0200
  * [MDEV-26317](https://jira.mariadb.org/browse/MDEV-26317): Add SYSTEMD\_READWRITEPATH variable to mariadb.service.in-file
* [Revision #80da35a326](https://github.com/MariaDB/server/commit/80da35a326)\
  2021-12-26 18:13:49 +0200
  * [MDEV-27365](https://jira.mariadb.org/browse/MDEV-27365) CREATE-or-REPLACE SEQUENCE is binlogged without DDL flag
* [Revision #5fd5e9fff3](https://github.com/MariaDB/server/commit/5fd5e9fff3)\
  2021-12-17 21:23:32 +1100
  * improve checks for libatomic linking
* Merge [Revision #97695675c5](https://github.com/MariaDB/server/commit/97695675c5) 2021-12-24 04:17:55 +0100 - Merge branch 10.2 into 10.3
* Merge [Revision #3376668ca8](https://github.com/MariaDB/server/commit/3376668ca8) 2021-12-23 14:14:04 +0100 - Merge branch 10.2 into 10.3
* [Revision #a5ef74e7eb](https://github.com/MariaDB/server/commit/a5ef74e7eb)\
  2021-12-22 13:12:40 +0400
  * [MDEV-27195](https://jira.mariadb.org/browse/MDEV-27195) SIGSEGV in Table\_scope\_and\_contents\_source\_st::vers\_check\_system\_fields
* [Revision #3b33593f80](https://github.com/MariaDB/server/commit/3b33593f80)\
  2021-12-21 11:07:25 +0200
  * [MDEV-27332](https://jira.mariadb.org/browse/MDEV-27332) SIGSEGV in fetch\_data\_into\_cache()
* [Revision #3fd80d0874](https://github.com/MariaDB/server/commit/3fd80d0874)\
  2021-12-16 23:13:45 +0300
  * [MDEV-27244](https://jira.mariadb.org/browse/MDEV-27244) Table corruption upon adding serial data type
* [Revision #a65d01a4cf](https://github.com/MariaDB/server/commit/a65d01a4cf)\
  2021-10-20 19:24:31 +0700
  * [MDEV-23182](https://jira.mariadb.org/browse/MDEV-23182): Server crashes in Item::fix\_fields\_if\_needed / table\_value\_constr::prepare upon 2nd execution of PS
* [Revision #7bc629a5ce](https://github.com/MariaDB/server/commit/7bc629a5ce)\
  2021-12-13 02:15:57 +0100
  * [MDEV-27181](https://jira.mariadb.org/browse/MDEV-27181): Galera SST scripts should use ssl\_capath for CA directory
* [Revision #375ae890c7](https://github.com/MariaDB/server/commit/375ae890c7)\
  2021-12-07 15:25:43 +0100
  * enable rpl\_semi\_sync\_after\_sync and rpl\_semi\_sync\_slave\_compressed\_protocol tests
* Merge [Revision #153b75b576](https://github.com/MariaDB/server/commit/153b75b576) 2021-12-06 21:38:43 +0100 - Merge branch '10.2' into 10.3
* [Revision #045f5f7b10](https://github.com/MariaDB/server/commit/045f5f7b10)\
  2019-11-22 15:03:20 +0100
  * [MDEV-21108](https://jira.mariadb.org/browse/MDEV-21108) Add option for setting install paths of groonga
* [Revision #fafe60e7e2](https://github.com/MariaDB/server/commit/fafe60e7e2)\
  2021-11-29 10:34:33 +0200
  * [MDEV-27134](https://jira.mariadb.org/browse/MDEV-27134): Sporadic failure of DROP DATABASE test
* Merge [Revision #289721de9a](https://github.com/MariaDB/server/commit/289721de9a) 2021-11-29 10:33:06 +0200 - Merge 10.2 into 10.3
* Merge [Revision #9962cda527](https://github.com/MariaDB/server/commit/9962cda527) 2021-11-17 13:55:54 +0200 - Merge 10.2 into 10.3
* Merge [Revision #7ea12742d3](https://github.com/MariaDB/server/commit/7ea12742d3) 2021-11-12 00:08:53 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #524b4a89da](https://github.com/MariaDB/server/commit/524b4a89da) 2021-11-09 08:26:59 +0200 - Merge 10.2 into 10.3
* Merge [Revision #f7054ff5df](https://github.com/MariaDB/server/commit/f7054ff5df) 2021-11-09 07:59:36 +0200 - Merge mariadb-10.3.32 into 10.3
* [Revision #e026eddc7d](https://github.com/MariaDB/server/commit/e026eddc7d)\
  2021-11-08 12:56:18 -0500
  * bump the VERSION
* [Revision #c8cece9144](https://github.com/MariaDB/server/commit/c8cece9144)\
  2021-11-02 04:52:04 +0300
  * [MDEV-26928](https://jira.mariadb.org/browse/MDEV-26928) Column-inclusive WITH SYSTEM VERSIONING doesn't work with explicit system fields
* [Revision #1be39f86cc](https://github.com/MariaDB/server/commit/1be39f86cc)\
  2021-11-02 04:52:03 +0300
  * [MDEV-25552](https://jira.mariadb.org/browse/MDEV-25552) system versioned partitioned by LIMIT tables break CHECK TABLE
* [Revision #c6207ecba4](https://github.com/MariaDB/server/commit/c6207ecba4)\
  2021-11-02 04:52:03 +0300
  * [MDEV-25803](https://jira.mariadb.org/browse/MDEV-25803) innodb.alter\_candidate\_key fix
* [Revision #63c922ae0c](https://github.com/MariaDB/server/commit/63c922ae0c)\
  2021-11-02 04:52:03 +0300
  * [MDEV-25803](https://jira.mariadb.org/browse/MDEV-25803) Inplace ALTER breaks MyISAM/Aria table when order of keys is changed

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
