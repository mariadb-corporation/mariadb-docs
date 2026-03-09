# MariaDB 10.3.19 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

After an upgrade MariaDB Server can crash if InnoDB tables exist with a `FULLTEXT INDEX` and a `FOREIGN KEY` constraint attached to them. We got reports that the crash already will be encountered on startup, but a crash is also possible at a later stage. See [MDEV-20987](https://jira.mariadb.org/browse/MDEV-20987) for more details.**Do not download or use this release.**

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.3/10.3.19.md)[Changelog](mariadb-10319-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.3.19/)

**Release date:** 5 Nov 2019

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.19.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.28](../changelogs-mariadb-102-series/mariadb-10228-changelog.md)
* [Revision #e1a2b12577](https://github.com/MariaDB/server/commit/e1a2b12577)\
  2019-11-03 17:59:48 +0200
  * List of unstable tests for 10.3.19 release
* [Revision #9c6fec88b1](https://github.com/MariaDB/server/commit/9c6fec88b1)\
  2019-11-01 21:40:10 +0300
  * [MDEV-17171](https://jira.mariadb.org/browse/MDEV-17171): RocksDB Tables do not have "Creation Date"
* [Revision #9c72963d2a](https://github.com/MariaDB/server/commit/9c72963d2a)\
  2019-10-31 19:44:29 +0300
  * [MDEV-17171](https://jira.mariadb.org/browse/MDEV-17171): RocksDB Tables do not have "Creation Date"
* [Revision #162f475c4b](https://github.com/MariaDB/server/commit/162f475c4b)\
  2019-11-01 06:57:20 +0530
  * [MDEV-20938](https://jira.mariadb.org/browse/MDEV-20938) Double free of dict\_foreign\_t during instant ALTER TABLE
* [Revision #6dce6aeceb](https://github.com/MariaDB/server/commit/6dce6aeceb)\
  2019-11-01 09:39:43 +0400
  * [MDEV-18244](https://jira.mariadb.org/browse/MDEV-18244) Server crashes in ha\_innobase::update\_thd / ... / ha\_partition::update\_next\_auto\_inc\_val.
* Merge [Revision #55b2281a5d](https://github.com/MariaDB/server/commit/55b2281a5d) 2019-10-31 10:58:06 +0100 - Merge branch '10.2' into 10.3
* [Revision #d6d621cec1](https://github.com/MariaDB/server/commit/d6d621cec1)\
  2019-10-30 13:53:07 +0100
  * [MDEV-18819](https://jira.mariadb.org/browse/MDEV-18819) ALTER\_COLUMN\_VCOL is not set for generated stored columns
* [Revision #73c864b5d1](https://github.com/MariaDB/server/commit/73c864b5d1)\
  2019-10-30 12:25:07 +0100
  * Fix clang-cl build on Windows
* [Revision #bef843b97f](https://github.com/MariaDB/server/commit/bef843b97f)\
  2019-10-29 18:20:32 +0200
  * [MDEV-20917](https://jira.mariadb.org/browse/MDEV-20917) InnoDB is passing NULL to nonnull function parameters
* [Revision #cb14d2e1a5](https://github.com/MariaDB/server/commit/cb14d2e1a5)\
  2019-10-28 13:29:46 +0530
  * Follow up fix for [MDEV-16871](https://jira.mariadb.org/browse/MDEV-16871)
* [Revision #803d0521a2](https://github.com/MariaDB/server/commit/803d0521a2)\
  2019-06-16 01:25:03 +0200
  * compilation failure on ppc with -DCMAKE\_BUILD\_TYPE=Debug
* [Revision #716d396bb3](https://github.com/MariaDB/server/commit/716d396bb3)\
  2019-10-21 18:41:58 +0300
  * Remove \n from DBUG\_PRINT statements
* [Revision #06d2e1d828](https://github.com/MariaDB/server/commit/06d2e1d828)\
  2019-10-21 17:17:09 +0300
  * read-only slave using statement replication should replicate tmp tables
* [Revision #7def2877e3](https://github.com/MariaDB/server/commit/7def2877e3)\
  2019-10-20 11:52:20 +0300
  * Write error message if aria\_log.??????? files are missing
* [Revision #67687d06bf](https://github.com/MariaDB/server/commit/67687d06bf)\
  2019-10-14 18:22:27 +0300
  * Simplify TABLE::decide\_logging\_format()
* [Revision #b62101f84b](https://github.com/MariaDB/server/commit/b62101f84b)\
  2019-10-14 18:14:36 +0300
  * Fixes for binary logging --read-only mode
* [Revision #e0b6294338](https://github.com/MariaDB/server/commit/e0b6294338)\
  2019-10-18 10:24:53 +0400
  * [MDEV-20855](https://jira.mariadb.org/browse/MDEV-20855) Crash with PARTITION BY LIST and extended characters
* Merge [Revision #0b9cee2cbf](https://github.com/MariaDB/server/commit/0b9cee2cbf) 2019-10-18 09:05:27 +0300 - Merge 10.2 into 10.3
* [Revision #de2186dd2f](https://github.com/MariaDB/server/commit/de2186dd2f)\
  2019-10-17 14:08:33 +0200
  * [MDEV-20074](https://jira.mariadb.org/browse/MDEV-20074): Lost connection on update trigger
* [Revision #6cdde9ebbf](https://github.com/MariaDB/server/commit/6cdde9ebbf)\
  2019-10-16 13:01:40 +0300
  * [MDEV-20836](https://jira.mariadb.org/browse/MDEV-20836) : Galera test failure on wsrep.variables
* [Revision #7ae0be25a6](https://github.com/MariaDB/server/commit/7ae0be25a6)\
  2019-10-14 15:07:21 +0300
  * [MDEV-20812](https://jira.mariadb.org/browse/MDEV-20812) Unexpected ER\_ROW\_IS\_REFERENCED\_2 upon DELETE from versioned table with FK
* [Revision #fa6c606257](https://github.com/MariaDB/server/commit/fa6c606257)\
  2019-10-12 21:58:34 +0300
  * [MDEV-20814](https://jira.mariadb.org/browse/MDEV-20814) Assertion index->is\_instant() failed on trivial upgrade from 10.1
* Merge [Revision #bb450b1fed](https://github.com/MariaDB/server/commit/bb450b1fed) 2019-10-12 15:38:58 +0300 - Merge 10.2 into 10.3
* Merge [Revision #8e3d85e112](https://github.com/MariaDB/server/commit/8e3d85e112) 2019-10-12 06:34:09 +0300 - Merge 10.2 into 10.3
* [Revision #0ecc85c5d9](https://github.com/MariaDB/server/commit/0ecc85c5d9)\
  2019-10-07 12:34:08 +0200
  * [MDEV-20728](https://jira.mariadb.org/browse/MDEV-20728): /usr/sbin/mysqld: unknown variable 'defaults-group-suffix=mysqld1
* [Revision #4cdb72f237](https://github.com/MariaDB/server/commit/4cdb72f237)\
  2019-10-10 21:21:24 +0300
  * [MDEV-19783](https://jira.mariadb.org/browse/MDEV-19783): Relax an assertion
* [Revision #01f45becd1](https://github.com/MariaDB/server/commit/01f45becd1)\
  2019-10-10 20:40:26 +0300
  * [MDEV-19783](https://jira.mariadb.org/browse/MDEV-19783): Add more assertions
* Merge [Revision #7f84e3ad75](https://github.com/MariaDB/server/commit/7f84e3ad75) 2019-10-10 20:38:44 +0300 - Merge 10.2 into 10.3
* [Revision #545c545206](https://github.com/MariaDB/server/commit/545c545206)\
  2019-10-10 13:35:32 +0300
  * Fix compilation 2 (GCC 9)
* [Revision #3c78d1b640](https://github.com/MariaDB/server/commit/3c78d1b640)\
  2019-10-10 11:08:31 +0300
  * Fix Mroonga compilation
* [Revision #cb3f856ecd](https://github.com/MariaDB/server/commit/cb3f856ecd)\
  2019-10-10 10:36:11 +0300
  * Fix compiler error when using -Wconversion.
* [Revision #c9cba59749](https://github.com/MariaDB/server/commit/c9cba59749)\
  2018-10-08 20:38:58 +0300
  * [MDEV-17333](https://jira.mariadb.org/browse/MDEV-17333) Assertion in update\_auto\_increment() upon exotic LOAD
* [Revision #a92f3146d2](https://github.com/MariaDB/server/commit/a92f3146d2)\
  2019-05-11 17:27:23 +0300
  * [MDEV-19406](https://jira.mariadb.org/browse/MDEV-19406) Assertion on updating view of join with versioned table
* [Revision #647a38818a](https://github.com/MariaDB/server/commit/647a38818a)\
  2018-05-23 22:15:04 +0300
  * [MDEV-16130](https://jira.mariadb.org/browse/MDEV-16130) wrong error message adding AS ROW START to versioned table
* [Revision #75ba5c815d](https://github.com/MariaDB/server/commit/75ba5c815d)\
  2018-05-30 13:19:03 +0300
  * [MDEV-16210](https://jira.mariadb.org/browse/MDEV-16210) FK constraints on versioned tables use historical rows, which may cause constraint violation
* [Revision #6684989801](https://github.com/MariaDB/server/commit/6684989801)\
  2018-05-30 12:43:54 +0300
  * versioning test suite fixes
* [Revision #cf71cc838e](https://github.com/MariaDB/server/commit/cf71cc838e)\
  2019-10-09 22:05:33 +0400
  * After merge fix, this line was removed in adefaef
* Merge [Revision #892378fb9d](https://github.com/MariaDB/server/commit/892378fb9d) 2019-10-09 13:25:11 +0300 - Merge 10.2 into 10.3
* [Revision #f11d425a15](https://github.com/MariaDB/server/commit/f11d425a15)\
  2019-10-09 09:16:40 +0300
  * [MDEV-20591](https://jira.mariadb.org/browse/MDEV-20591): Follow-up fix
* [Revision #896b869685](https://github.com/MariaDB/server/commit/896b869685)\
  2019-10-05 09:12:56 +0200
  * [MDEV-19238](https://jira.mariadb.org/browse/MDEV-19238) Mariadb spider - crashes on where null
* [Revision #b7408be0c3](https://github.com/MariaDB/server/commit/b7408be0c3)\
  2019-10-04 16:46:41 +0200
  * [MDEV-20753](https://jira.mariadb.org/browse/MDEV-20753): Sequence with limit 0 crashes server
* [Revision #b1ac174279](https://github.com/MariaDB/server/commit/b1ac174279)\
  2019-10-07 12:49:57 -0400
  * Cast string literal to char\* [MDEV-20767](https://jira.mariadb.org/browse/MDEV-20767)
* [Revision #1e0f09cacb](https://github.com/MariaDB/server/commit/1e0f09cacb)\
  2018-05-17 14:40:55 +0530
  * [MDEV-16239](https://jira.mariadb.org/browse/MDEV-16239) Many test in rpl suite fails
* [Revision #01bf9f8c3d](https://github.com/MariaDB/server/commit/01bf9f8c3d)\
  2019-09-14 12:53:36 +0530
  * [MDEV-20591](https://jira.mariadb.org/browse/MDEV-20591) Wrong Number of rows in mysqlbinlog output
* [Revision #5b2fa078e8](https://github.com/MariaDB/server/commit/5b2fa078e8)\
  2019-10-02 20:17:00 +0400
  * Cleanup mman.h includes
* [Revision #716c748f97](https://github.com/MariaDB/server/commit/716c748f97)\
  2019-09-23 18:28:55 +1000
  * [MDEV-20684](https://jira.mariadb.org/browse/MDEV-20684): innodb/query cache use madvise CORE/NOCORE on FreeBSD
* Merge [Revision #7e44c455f4](https://github.com/MariaDB/server/commit/7e44c455f4) 2019-10-01 09:37:40 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #6c2724fc05](https://github.com/MariaDB/server/commit/6c2724fc05)\
  2019-09-30 15:27:48 +0400
  * [MDEV-19628](https://jira.mariadb.org/browse/MDEV-19628) JSON with starting double quotes key is not valid.
* [Revision #6ac2a35553](https://github.com/MariaDB/server/commit/6ac2a35553)\
  2019-09-30 14:43:32 +0400
  * [MDEV-19628](https://jira.mariadb.org/browse/MDEV-19628) JSON with starting double quotes key is not valid.
* Merge [Revision #2911a9a693](https://github.com/MariaDB/server/commit/2911a9a693) 2019-09-27 15:56:15 +0300 - Merge 10.2 into 10.3
* [Revision #46facaedbf](https://github.com/MariaDB/server/commit/46facaedbf)\
  2019-09-26 15:18:43 +0300
  * Fix GCC 9 -Wmaybe-uninitialized
* Merge [Revision #1cf0694d10](https://github.com/MariaDB/server/commit/1cf0694d10) 2019-09-26 13:18:57 +0300 - Merge 10.2 into 10.3
* [Revision #3e4931cdf3](https://github.com/MariaDB/server/commit/3e4931cdf3)\
  2019-09-26 13:18:22 +0300
  * [MDEV-20675](https://jira.mariadb.org/browse/MDEV-20675) Crash in SHOW ENGINE INNODB STATUS with innodb\_force\_recovery=5
* Merge [Revision #b6bb64e54a](https://github.com/MariaDB/server/commit/b6bb64e54a) 2019-09-24 23:05:09 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #0e50ee6f28](https://github.com/MariaDB/server/commit/0e50ee6f28)\
  2019-09-24 20:43:32 +0300
  * Remove --basedir arg from systemd startup scripts
* Merge [Revision #7ae290c757](https://github.com/MariaDB/server/commit/7ae290c757) 2019-09-24 13:39:31 +0300 - Merge 10.2 into 10.3
* [Revision #e157f81771](https://github.com/MariaDB/server/commit/e157f81771)\
  2019-09-23 10:41:13 +0300
  * Remove Field::is\_stat\_field completely
* Merge [Revision #c016ea660e](https://github.com/MariaDB/server/commit/c016ea660e) 2019-09-23 10:25:34 +0300 - Merge 10.2 into 10.3
* [Revision #1bbe8c5e0f](https://github.com/MariaDB/server/commit/1bbe8c5e0f)\
  2019-09-22 04:08:48 +0300
  * Proper fix for disabling warnings in read\_statistics\_for\_table().
* [Revision #ba7725dace](https://github.com/MariaDB/server/commit/ba7725dace)\
  2019-09-20 15:59:54 -0700
  * [MDEV-20229](https://jira.mariadb.org/browse/MDEV-20229) CTE defined with table value constructor cannot be used in views
* [Revision #90a9c4cae7](https://github.com/MariaDB/server/commit/90a9c4cae7)\
  2019-09-16 15:45:24 +0530
  * [MDEV-20217](https://jira.mariadb.org/browse/MDEV-20217): Semi\_sync: Last\_IO\_Error: Fatal error: Failed to run 'after\_queue\_event' hook
* [Revision #bfbf0f2251](https://github.com/MariaDB/server/commit/bfbf0f2251)\
  2019-09-13 18:11:32 +0300
  * [MDEV-20525](https://jira.mariadb.org/browse/MDEV-20525): Fix the -std=c90 builds
* [Revision #b214264aee](https://github.com/MariaDB/server/commit/b214264aee)\
  2019-09-13 15:28:53 +0300
  * [MDEV-20525](https://jira.mariadb.org/browse/MDEV-20525) rocksdb debug compilation fails on Windows due to unresolved my\_assert variable
* [Revision #41290e91b7](https://github.com/MariaDB/server/commit/41290e91b7)\
  2019-09-12 17:06:06 +0200
  * Fix CMake warning in spider, in Windows ninja build
* [Revision #9554ef0678](https://github.com/MariaDB/server/commit/9554ef0678)\
  2019-09-12 11:12:55 +0400
  * [MDEV-19670](https://jira.mariadb.org/browse/MDEV-19670) json escaped unicode parse error.
* Merge [Revision #0fa5ad3acf](https://github.com/MariaDB/server/commit/0fa5ad3acf) 2019-09-11 16:42:01 +0300 - Merge 10.2 into 10.3
* [Revision #40ab433ecc](https://github.com/MariaDB/server/commit/40ab433ecc)\
  2019-09-11 09:13:47 -0400
  * bump the VERSION
* Merge [Revision #c6a6830916](https://github.com/MariaDB/server/commit/c6a6830916) 2019-09-11 10:32:24 +0300 - Merge 10.2 into 10.3
* [Revision #f1616bacb7](https://github.com/MariaDB/server/commit/f1616bacb7)\
  2019-09-11 10:13:19 +0400
  * Adding missing semicolons to sql\_yacc\_ora.yy (10.3), indentation cleanups.
* [Revision #f1309fac33](https://github.com/MariaDB/server/commit/f1309fac33)\
  2019-09-11 05:12:37 +0400
  * Adding missing semicolons to sql\_yacc.yy (10.3), indentation cleanups.
* Merge [Revision #48f8e3f3f4](https://github.com/MariaDB/server/commit/48f8e3f3f4) 2019-09-11 04:47:01 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #ff5ecfd335](https://github.com/MariaDB/server/commit/ff5ecfd335)\
  2019-09-10 10:04:04 +0300
  * Correct the merge 0f83c8878dc1389212c134f65d37a43d9d248250
* Merge [Revision #da9201dd5b](https://github.com/MariaDB/server/commit/da9201dd5b) 2019-09-10 09:25:20 +0300 - Merge 10.2 into 10.3
* [Revision #aabd1c8fcb](https://github.com/MariaDB/server/commit/aabd1c8fcb)\
  2019-09-09 22:30:53 +0300
  * [MDEV-16490](https://jira.mariadb.org/browse/MDEV-16490) fix versioning.partition failure
* [Revision #f6a7730c45](https://github.com/MariaDB/server/commit/f6a7730c45)\
  2018-06-22 23:26:43 +1000
  * [MDEV-16490](https://jira.mariadb.org/browse/MDEV-16490): It's possible to make a system versioned table without any versioning field

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
