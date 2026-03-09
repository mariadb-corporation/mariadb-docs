# MariaDB 10.5.1 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download](https://downloads.mariadb.org/mariadb/10.5.1/)[Release Notes](../../old-releases/10.5/10.5.1.md)[Changelog](mariadb-1051-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 14 Feb 2020

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.1.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.12](../changelogs-mariadb-10-4-series/mariadb-10412-changelog.md)
* [Revision #6dc46b5a4d](https://github.com/MariaDB/server/commit/6dc46b5a4d)\
  2020-02-13 17:09:02 +0100
  * alpha -> beta
* [Revision #ac51bcfd8d](https://github.com/MariaDB/server/commit/ac51bcfd8d)\
  2020-02-13 13:18:34 +0200
  * Update rdiff for sysvars 32bit to account for removed options
* [Revision #efa9079fbd](https://github.com/MariaDB/server/commit/efa9079fbd)\
  2020-02-12 16:50:58 +0200
  * Fix compilation error due to type mismatch in tpool\_generic.cc
* [Revision #ad17aa110c](https://github.com/MariaDB/server/commit/ad17aa110c)\
  2020-01-08 14:29:46 +0200
  * [MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650): Options deprecated in previous versions - multi\_range\_count
* [Revision #5aebd78e27](https://github.com/MariaDB/server/commit/5aebd78e27)\
  2020-02-12 18:54:41 +0200
  * [MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650): Options deprecated in previous versions - mroonga\_default\_parser
* [Revision #a05b38c120](https://github.com/MariaDB/server/commit/a05b38c120)\
  2020-02-12 18:53:37 +0200
  * [MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650): Options deprecated in previous versions - skip-bdb
* [Revision #8bbcaab160](https://github.com/MariaDB/server/commit/8bbcaab160)\
  2020-01-21 15:39:02 +0200
  * [MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650): Options deprecated in previous versions - thread\_concurrency
* [Revision #fc5a4cfdf5](https://github.com/MariaDB/server/commit/fc5a4cfdf5)\
  2020-01-21 14:21:53 +0200
  * [MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650): Options deprecated in previous versions - old\_alter\_table
* [Revision #899056cfab](https://github.com/MariaDB/server/commit/899056cfab)\
  2020-01-14 22:29:59 +0100
  * for every deprecated sysvar note a version when it happened
* [Revision #1bc9cce702](https://github.com/MariaDB/server/commit/1bc9cce702)\
  2020-01-19 19:13:01 +0200
  * Policy improvement for removed options and system variables
* [Revision #45bc7574fb](https://github.com/MariaDB/server/commit/45bc7574fb)\
  2020-01-13 21:07:04 +0200
  * [MDEV-18650](https://jira.mariadb.org/browse/MDEV-18650): Options deprecated in previous versions - storage\_engine
* [Revision #415797f1a6](https://github.com/MariaDB/server/commit/415797f1a6)\
  2019-07-24 20:49:12 -0300
  * Deb: Run 'wrap-and-sort -a' so comparison across releases is easier
* [Revision #20a7f75fbf](https://github.com/MariaDB/server/commit/20a7f75fbf)\
  2020-02-12 20:54:59 +0200
  * [MDEV-15058](https://jira.mariadb.org/browse/MDEV-15058): Revert the changes to INFORMATION\_SCHEMA
* [Revision #f0606a7530](https://github.com/MariaDB/server/commit/f0606a7530)\
  2020-02-11 17:16:37 +0530
  * [MDEV-21665](https://jira.mariadb.org/browse/MDEV-21665): Server crashes in my\_qsort2 / Filesort\_buffer::sort\_buffer
* [Revision #1a6f708ec5](https://github.com/MariaDB/server/commit/1a6f708ec5)\
  2020-02-12 14:45:21 +0200
  * [MDEV-15058](https://jira.mariadb.org/browse/MDEV-15058): Deprecate and ignore innodb\_buffer\_pool\_instances
* [Revision #0448c614c8](https://github.com/MariaDB/server/commit/0448c614c8)\
  2020-02-12 09:33:08 +0200
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264): Remove unused page\_cleaner\_t::is\_started
* [Revision #2a6fa1c42b](https://github.com/MariaDB/server/commit/2a6fa1c42b)\
  2020-02-12 09:12:18 +0200
  * [MDEV-21132](https://jira.mariadb.org/browse/MDEV-21132): Use memcpy\_aligned, memset\_aligned
* Merge [Revision #4b087e1754](https://github.com/MariaDB/server/commit/4b087e1754) 2020-02-12 08:55:17 +0100 - Merge branch '10.4' into 10.5
* Merge [Revision #646d1ec83a](https://github.com/MariaDB/server/commit/646d1ec83a) 2020-02-11 14:40:35 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #58b70dc136](https://github.com/MariaDB/server/commit/58b70dc136) 2020-02-10 20:34:16 +0100 - Merge branch '10.2' into 10.3
* [Revision #235d7c6f54](https://github.com/MariaDB/server/commit/235d7c6f54)\
  2020-02-06 12:14:40 +0100
  * Ignore /lib64 for rpm
* Merge [Revision #594282a534](https://github.com/MariaDB/server/commit/594282a534) 2020-02-10 14:31:39 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #716161ea03](https://github.com/MariaDB/server/commit/716161ea03) 2020-02-10 14:18:00 +0100 - Merge branch '5.5' into 10.1
* [Revision #4932ec871f](https://github.com/MariaDB/server/commit/4932ec871f)\
  2020-01-29 12:49:06 +0100
  * Clean the comment for `table_f_c unt` parameter
* [Revision #e568dc9723](https://github.com/MariaDB/server/commit/e568dc9723)\
  2020-02-08 18:58:28 +0200
  * Remove unused SRV\_MASTER\_PURGE\_INTERVAL
* [Revision #80da232576](https://github.com/MariaDB/server/commit/80da232576)\
  2020-02-07 15:22:16 +0530
  * [MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563) FTS thread aborts during shutdown
* [Revision #280bf17829](https://github.com/MariaDB/server/commit/280bf17829)\
  2020-02-06 20:42:29 +0530
  * [MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563) FTS thread aborts during shutdown
* [Revision #b08579aa28](https://github.com/MariaDB/server/commit/b08579aa28)\
  2020-01-30 21:11:24 +0100
  * [MDEV-16308](https://jira.mariadb.org/browse/MDEV-16308) : protocol messed up sporadically
* [Revision #6fc72ce169](https://github.com/MariaDB/server/commit/6fc72ce169)\
  2020-02-07 14:18:17 +0200
  * [MDEV-21667](https://jira.mariadb.org/browse/MDEV-21667) : Galera test failure on MW-336
* [Revision #0ea8894e52](https://github.com/MariaDB/server/commit/0ea8894e52)\
  2020-01-31 08:05:41 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #785a9ac93a](https://github.com/MariaDB/server/commit/785a9ac93a)\
  2020-02-07 10:42:57 +0100
  * added warning to ignore
* [Revision #82c3b42a6e](https://github.com/MariaDB/server/commit/82c3b42a6e)\
  2020-02-06 20:03:04 +0100
  * Windows test fix
* [Revision #3be751d5b9](https://github.com/MariaDB/server/commit/3be751d5b9)\
  2020-02-07 16:01:31 +0530
  * [MDEV-21608](https://jira.mariadb.org/browse/MDEV-21608) Assertion \`n\_ext == dtuple\_get\_n\_ext(dtuple)' failed during updation of PK
* [Revision #ebbc572b82](https://github.com/MariaDB/server/commit/ebbc572b82)\
  2020-02-06 10:50:04 +0200
  * [MDEV-12121](https://jira.mariadb.org/browse/MDEV-12121): Clean up WITH\_INNODB\_AHI=OFF
* [Revision #236aed3f5f](https://github.com/MariaDB/server/commit/236aed3f5f)\
  2020-02-03 19:23:38 +0100
  * [MDEV-21656](https://jira.mariadb.org/browse/MDEV-21656): Wrong directory for pam\_user\_map.so JIRA:[MDEV-17292](https://jira.mariadb.org/browse/MDEV-17292)
* [Revision #a241d41195](https://github.com/MariaDB/server/commit/a241d41195)\
  2019-07-10 13:40:54 +0200
  * [MDEV-18027](https://jira.mariadb.org/browse/MDEV-18027): Running out of file descriptors and eventual crash
* [Revision #a9d1324867](https://github.com/MariaDB/server/commit/a9d1324867)\
  2020-02-03 12:10:59 +0200
  * Cleanup: Remove mem\_block\_t::magic\_n and mem\_block\_validate()
* [Revision #37b9734c06](https://github.com/MariaDB/server/commit/37b9734c06)\
  2020-02-03 10:02:58 +0200
  * [MDEV-21636](https://jira.mariadb.org/browse/MDEV-21636) information\_schema.innodb\_mutexes.name column is not populated
* [Revision #bd36a4ca12](https://github.com/MariaDB/server/commit/bd36a4ca12)\
  2020-01-30 13:11:06 +0800
  * introduce HASH\_REPLACE() for hash\_table\_t
* [Revision #d72038a738](https://github.com/MariaDB/server/commit/d72038a738)\
  2020-02-07 14:18:17 +0200
  * [MDEV-21667](https://jira.mariadb.org/browse/MDEV-21667) : Galera test failure on MW-336
* [Revision #a30ab52635](https://github.com/MariaDB/server/commit/a30ab52635)\
  2020-01-31 08:05:41 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #8d7462ec49](https://github.com/MariaDB/server/commit/8d7462ec49)\
  2020-02-07 19:42:11 -0800
  * [MDEV-21614](https://jira.mariadb.org/browse/MDEV-21614) Wrong query results with optimizer\_switch="split\_materialized=on"
* [Revision #fafb35ee51](https://github.com/MariaDB/server/commit/fafb35ee51)\
  2019-11-06 12:35:19 +0100
  * [MDEV-20076](https://jira.mariadb.org/browse/MDEV-20076): SHOW GRANTS does not quote role names properly
* [Revision #b3ded21922](https://github.com/MariaDB/server/commit/b3ded21922)\
  2020-02-05 00:54:16 +0300
  * ha\_partition: add comments, comment out unused member variables
* [Revision #b0fa308086](https://github.com/MariaDB/server/commit/b0fa308086)\
  2020-02-02 15:13:29 +0300
  * [MDEV-21195](https://jira.mariadb.org/browse/MDEV-21195) INSERT chooses wrong partition for RANGE partitioning by DECIMAL column
* [Revision #74deeaee34](https://github.com/MariaDB/server/commit/74deeaee34)\
  2020-02-02 15:13:29 +0300
  * [MDEV-21317](https://jira.mariadb.org/browse/MDEV-21317) mysqlhotcopy and transaction\_registry table
* [Revision #e13e49e5ab](https://github.com/MariaDB/server/commit/e13e49e5ab)\
  2020-02-02 15:13:29 +0300
  * [MDEV-20528](https://jira.mariadb.org/browse/MDEV-20528) innodb.purge\_secondary\_[MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222) failed in buildbot, debug sync point wait timed out
* [Revision #006f6f97b1](https://github.com/MariaDB/server/commit/006f6f97b1)\
  2020-02-02 15:13:29 +0300
  * [MDEV-17798](https://jira.mariadb.org/browse/MDEV-17798) System variable system\_versioning\_asof accepts wrong values
* [Revision #14e6f0251c](https://github.com/MariaDB/server/commit/14e6f0251c)\
  2020-02-02 15:13:29 +0300
  * [MDEV-20955](https://jira.mariadb.org/browse/MDEV-20955) versioning.update failed in buildbot with wrong result code
* [Revision #c8bd8d5c64](https://github.com/MariaDB/server/commit/c8bd8d5c64)\
  2020-01-31 13:16:11 +0200
  * [MDEV-14330](https://jira.mariadb.org/browse/MDEV-14330): After-merge fix
* Merge [Revision #5ff66fb0b9](https://github.com/MariaDB/server/commit/5ff66fb0b9) 2020-01-31 11:37:12 +0200 - Merge 10.2 into 10.3
* [Revision #256994ef74](https://github.com/MariaDB/server/commit/256994ef74)\
  2020-01-31 11:33:07 +0200
  * [MDEV-21586](https://jira.mariadb.org/browse/MDEV-21586): Fix a warning for converting my\_bool to bool
* Merge [Revision #2daf3b14fe](https://github.com/MariaDB/server/commit/2daf3b14fe) 2020-01-31 10:53:56 +0200 - Merge 10.1 into 10.2
* [Revision #0b36c27e0c](https://github.com/MariaDB/server/commit/0b36c27e0c)\
  2020-01-31 10:06:55 +0200
  * [MDEV-20307](https://jira.mariadb.org/browse/MDEV-20307): Remove a useless debug check to save stack space
* [Revision #afe9caa82d](https://github.com/MariaDB/server/commit/afe9caa82d)\
  2020-01-30 17:54:49 +0530
  * [MDEV-21564](https://jira.mariadb.org/browse/MDEV-21564) Assert in trx\_purge\_add\_update\_undo\_to\_history during shutdown
* [Revision #d89bb88674](https://github.com/MariaDB/server/commit/d89bb88674)\
  2020-01-23 16:17:55 +0530
  * [MDEV-20923](https://jira.mariadb.org/browse/MDEV-20923):UBSAN: member access within address … which does not point to an object of type 'xid\_count\_per\_binlog'
* [Revision #5271d43648](https://github.com/MariaDB/server/commit/5271d43648)\
  2020-01-28 18:03:13 +0200
  * [MDEV-14330](https://jira.mariadb.org/browse/MDEV-14330) Move mysqltest.1 man page to appropriate test package from server package
* [Revision #9aaa3e1fda](https://github.com/MariaDB/server/commit/9aaa3e1fda)\
  2020-01-28 17:48:57 +0200
  * Ingore sysusers and tmpfiles artifacts
* Merge [Revision #c5df6e1448](https://github.com/MariaDB/server/commit/c5df6e1448) 2020-01-28 09:23:53 +0100 - Merge branch 'bb-10.1-release' into 10.1
* [Revision #84d4005bad](https://github.com/MariaDB/server/commit/84d4005bad)\
  2020-01-25 23:50:41 +0200
  * List of unstable tests for 10.1.44 release
* [Revision #742c36d048](https://github.com/MariaDB/server/commit/742c36d048)\
  2017-12-28 22:19:28 +0800
  * [MDEV-15052](https://jira.mariadb.org/browse/MDEV-15052): Allow sysusers and tmpfiles install for non-systemd users
* [Revision #b472bc2eba](https://github.com/MariaDB/server/commit/b472bc2eba)\
  2018-01-02 14:32:21 +0100
  * [MDEV-17028](https://jira.mariadb.org/browse/MDEV-17028): Use descriptive file names for sysusers and tmpfiles configuration
* [Revision #f37a56de3c](https://github.com/MariaDB/server/commit/f37a56de3c)\
  2020-01-30 18:42:51 +0100
  * [MDEV-21586](https://jira.mariadb.org/browse/MDEV-21586) Server does not start if lc\_messages setting was not english.
* [Revision #07e34cddb6](https://github.com/MariaDB/server/commit/07e34cddb6)\
  2020-01-28 13:52:47 +0200
  * [MDEV-14330](https://jira.mariadb.org/browse/MDEV-14330): move tokudb manpages to right packages
* [Revision #a134ec3736](https://github.com/MariaDB/server/commit/a134ec3736)\
  2020-01-28 18:00:19 +0530
  * [MDEV-21550](https://jira.mariadb.org/browse/MDEV-21550) Assertion \`!table->fts->in\_queue' failed in fts\_optimize\_remove\_table
* [Revision #0a891ad6a6](https://github.com/MariaDB/server/commit/0a891ad6a6)\
  2020-01-26 18:40:22 +0200
  * List of unstable tests for 10.2.31 release
* Merge [Revision #dbbe9961a5](https://github.com/MariaDB/server/commit/dbbe9961a5) 2020-01-28 09:28:18 +0100 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #0152704ae3](https://github.com/MariaDB/server/commit/0152704ae3)\
  2020-01-26 20:34:09 +0200
  * List of unstable tests for 10.3.22 release
* Merge [Revision #e10e922afd](https://github.com/MariaDB/server/commit/e10e922afd) 2020-01-25 16:09:34 +0100 - Merge branch '[MDEV-21383](https://jira.mariadb.org/browse/MDEV-21383)' into 10.3
* [Revision #fc2f2fa853](https://github.com/MariaDB/server/commit/fc2f2fa853)\
  2020-02-11 18:44:26 +0200
  * [MDEV-19747](https://jira.mariadb.org/browse/MDEV-19747): Deprecate and ignore innodb\_log\_optimize\_ddl
* [Revision #8ccb3caafb](https://github.com/MariaDB/server/commit/8ccb3caafb)\
  2020-02-11 18:03:19 +0200
  * [MDEV-17491](https://jira.mariadb.org/browse/MDEV-17491) micro optimize page\_id\_t further
* [Revision #f3dac59174](https://github.com/MariaDB/server/commit/f3dac59174)\
  2020-02-11 16:31:04 +0200
  * [MDEV-21351](https://jira.mariadb.org/browse/MDEV-21351): Fix a performance regression
* [Revision #e6a50e41da](https://github.com/MariaDB/server/commit/e6a50e41da)\
  2019-10-02 13:24:34 +0300
  * [MDEV-20051](https://jira.mariadb.org/browse/MDEV-20051): Add new mode to wsrep\_OSU\_method in which Galera checks storage engine of the effected table
* [Revision #41541a7c48](https://github.com/MariaDB/server/commit/41541a7c48)\
  2020-02-10 21:19:28 -0800
  * [MDEV-21683](https://jira.mariadb.org/browse/MDEV-21683) Server crashes in get\_quick\_keys with not\_null\_range\_scan
* [Revision #83e75b39b3](https://github.com/MariaDB/server/commit/83e75b39b3)\
  2020-02-09 21:53:11 +0400
  * [MDEV-21702](https://jira.mariadb.org/browse/MDEV-21702) Add a data type for privileges
* [Revision #f79f537f9f](https://github.com/MariaDB/server/commit/f79f537f9f)\
  2020-02-10 21:57:27 +0300
  * [MDEV-21690](https://jira.mariadb.org/browse/MDEV-21690) LeakSanitizer: detected memory leaks in mem\_heap\_create\_block\_func
* [Revision #77c6382312](https://github.com/MariaDB/server/commit/77c6382312)\
  2020-02-05 12:43:17 +0400
  * [MDEV-21689](https://jira.mariadb.org/browse/MDEV-21689) Add Sql\_cmd for GRANT/REVOKE statements
* [Revision #06b0623adb](https://github.com/MariaDB/server/commit/06b0623adb)\
  2020-02-08 14:12:59 +0200
  * Cleanup: Aligned InnoDB index page header access
* [Revision #c5856b0a68](https://github.com/MariaDB/server/commit/c5856b0a68)\
  2020-02-08 11:47:42 +0200
  * [MDEV-21351](https://jira.mariadb.org/browse/MDEV-21351): Allocate aligned memory
* [Revision #6eed99f1f3](https://github.com/MariaDB/server/commit/6eed99f1f3)\
  2020-02-08 11:40:55 +0200
  * [MDEV-21248](https://jira.mariadb.org/browse/MDEV-21248): Do not break the build on clang
* [Revision #35c2778519](https://github.com/MariaDB/server/commit/35c2778519)\
  2019-12-08 10:52:27 +0100
  * [MDEV-21248](https://jira.mariadb.org/browse/MDEV-21248): Prevent optimizing out buf argument in check\_stack\_overrun.
* [Revision #0d1ca19383](https://github.com/MariaDB/server/commit/0d1ca19383)\
  2020-02-07 13:44:13 +0200
  * One more fixup for sizeof(mtr\_t) reduction
* [Revision #91e7b44399](https://github.com/MariaDB/server/commit/91e7b44399)\
  2020-02-07 13:29:08 +0200
  * mtr\_t::get\_log\_mode(): Remove a redundant assertion
* [Revision #2b260f2ddd](https://github.com/MariaDB/server/commit/2b260f2ddd)\
  2020-02-07 13:15:33 +0200
  * Fixup the parent commit
* [Revision #9a999469f7](https://github.com/MariaDB/server/commit/9a999469f7)\
  2020-02-07 11:55:33 +0200
  * Cleanup: Recude sizeof(mtr\_t)
* Merge [Revision #8b6cfda631](https://github.com/MariaDB/server/commit/8b6cfda631) 2020-02-07 08:51:20 +0200 - Merge 10.4 into 10.5
* [Revision #c1eaa385ff](https://github.com/MariaDB/server/commit/c1eaa385ff)\
  2020-02-03 18:20:24 +0100
  * [MDEV-21616](https://jira.mariadb.org/browse/MDEV-21616): Server crash when using "SET STATEMENT max\_statement\_time=0 FOR desc xxx" lead to collapse
* [Revision #2acc6f2d95](https://github.com/MariaDB/server/commit/2acc6f2d95)\
  2020-02-05 11:12:10 +0200
  * [MDEV-21658](https://jira.mariadb.org/browse/MDEV-21658) Error on online ADD PRIMARY KEY after instant DROP/reorder
* [Revision #a56f78243e](https://github.com/MariaDB/server/commit/a56f78243e)\
  2020-02-04 16:31:52 +0200
  * [MDEV-21645](https://jira.mariadb.org/browse/MDEV-21645) SIGSEGV in innobase\_get\_computed\_value
* [Revision #46386661a2](https://github.com/MariaDB/server/commit/46386661a2)\
  2020-02-04 09:00:36 +0200
  * [MDEV-20625](https://jira.mariadb.org/browse/MDEV-20625) : MariaDB asserting when enabling wsrep\_on
* [Revision #93278ee8ad](https://github.com/MariaDB/server/commit/93278ee8ad)\
  2019-10-08 10:47:30 +0200
  * [MDEV-20625](https://jira.mariadb.org/browse/MDEV-20625): MariaDB asserting when enabling wsrep=on
* [Revision #574354a6b2](https://github.com/MariaDB/server/commit/574354a6b2)\
  2020-02-03 19:45:30 +0200
  * [MDEV-20625](https://jira.mariadb.org/browse/MDEV-20625) : MariaDB asserting when enabling wsrep\_on
* [Revision #eed6d215f1](https://github.com/MariaDB/server/commit/eed6d215f1)\
  2019-10-09 21:16:31 +0530
  * [MDEV-20001](https://jira.mariadb.org/browse/MDEV-20001) Potential dangerous regression: INSERT INTO >=100 rows fail for myisam table with HASH indexes
* [Revision #b615d275b8](https://github.com/MariaDB/server/commit/b615d275b8)\
  2020-02-02 15:13:29 +0300
  * [MDEV-17798](https://jira.mariadb.org/browse/MDEV-17798) System variable system\_versioning\_asof accepts wrong values (10.4)
* [Revision #5a6023cf6f](https://github.com/MariaDB/server/commit/5a6023cf6f)\
  2019-10-08 17:35:09 +0530
  * [MDEV-18791](https://jira.mariadb.org/browse/MDEV-18791) Wrong error upon creating Aria table with long index on BLOB
* [Revision #1b414c0313](https://github.com/MariaDB/server/commit/1b414c0313)\
  2020-02-01 15:06:12 +0200
  * [MDEV-21256](https://jira.mariadb.org/browse/MDEV-21256) after-merge fix: Use std::atomic
* [Revision #4b291588bb](https://github.com/MariaDB/server/commit/4b291588bb)\
  2020-02-01 14:53:41 +0200
  * [MDEV-19845](https://jira.mariadb.org/browse/MDEV-19845): Make my\_cpu.h self-contained
* [Revision #d87b725eeb](https://github.com/MariaDB/server/commit/d87b725eeb)\
  2020-01-31 09:54:43 +0200
  * [MDEV-17844](https://jira.mariadb.org/browse/MDEV-17844) recs\_off\_validate() fails in page\_zip\_write\_trx\_id\_and\_roll\_ptr()
* [Revision #88bcc7f21c](https://github.com/MariaDB/server/commit/88bcc7f21c)\
  2020-01-31 09:17:12 +0200
  * Fixup cd2c0e013ccb5f9b009743dfd7188585a539d9b5
* [Revision #a10a94b262](https://github.com/MariaDB/server/commit/a10a94b262)\
  2020-01-31 11:47:17 +0530
  * Empty commit
* [Revision #4d61f1247a](https://github.com/MariaDB/server/commit/4d61f1247a)\
  2020-01-29 16:41:04 +0200
  * Fixed compiler warnings from gcc 7.4.1
* [Revision #cd2c0e013c](https://github.com/MariaDB/server/commit/cd2c0e013c)\
  2020-01-29 17:31:08 +0200
  * Added error output wsrep\_print\_version
* [Revision #8b97eba31b](https://github.com/MariaDB/server/commit/8b97eba31b)\
  2020-02-07 08:12:58 +0200
  * [MDEV-21674](https://jira.mariadb.org/browse/MDEV-21674) purge\_sys.stop() fails to wait for purge workers to complete
* [Revision #cd3bdc09db](https://github.com/MariaDB/server/commit/cd3bdc09db)\
  2020-02-06 14:52:11 +0200
  * [MDEV-18582](https://jira.mariadb.org/browse/MDEV-18582): Fix a race condition
* [Revision #6d214415c9](https://github.com/MariaDB/server/commit/6d214415c9)\
  2020-02-06 09:00:19 +0200
  * [MDEV-21351](https://jira.mariadb.org/browse/MDEV-21351): Free processed recv\_sys\_t::blocks
* [Revision #d0c8316bf5](https://github.com/MariaDB/server/commit/d0c8316bf5)\
  2020-02-05 09:02:33 +0100
  * Incorrect behaviour of WSREP\_SYNC\_WAIT\_UPTO\_GTID (#1442)
* [Revision #daaa881cfe](https://github.com/MariaDB/server/commit/daaa881cfe)\
  2020-02-04 22:30:08 +0400
  * libpmem cmake macros
* [Revision #42e825dd0a](https://github.com/MariaDB/server/commit/42e825dd0a)\
  2020-02-04 18:16:21 +0530
  * [MDEV-20601](https://jira.mariadb.org/browse/MDEV-20601): Make REPLICA a synonym for SLAVE in SQL statements
* [Revision #287c1db786](https://github.com/MariaDB/server/commit/287c1db786)\
  2020-02-03 17:59:14 +0800
  * try to fix Win x86 build
* [Revision #691c691adc](https://github.com/MariaDB/server/commit/691c691adc)\
  2020-02-01 23:54:57 +0800
  * clean up redo log
* [Revision #74f7620636](https://github.com/MariaDB/server/commit/74f7620636)\
  2020-01-30 09:28:16 +0100
  * [MDEV-21598](https://jira.mariadb.org/browse/MDEV-21598) Galera test galera.galera\_sst\_mysqldump does not take wsrep-new-cluster into account
* [Revision #41bc736871](https://github.com/MariaDB/server/commit/41bc736871)\
  2019-04-01 13:23:05 +0200
  * Galera GTID support
* [Revision #5defdc382b](https://github.com/MariaDB/server/commit/5defdc382b)\
  2020-01-29 14:28:45 +0200
  * Cleanup: Remove mtr\_state\_t and mtr\_t::m\_state
* [Revision #c69a8629f7](https://github.com/MariaDB/server/commit/c69a8629f7)\
  2020-01-29 13:39:06 +0200
  * [MDEV-21362](https://jira.mariadb.org/browse/MDEV-21362): Do not call memcmp on null pointers
* [Revision #50324ce624](https://github.com/MariaDB/server/commit/50324ce624)\
  2020-01-29 12:53:39 +0200
  * [MDEV-21351](https://jira.mariadb.org/browse/MDEV-21351) Replace recv\_sys.heap with list of buf\_block\_t
* Merge [Revision #a983b24407](https://github.com/MariaDB/server/commit/a983b24407) 2020-01-28 14:17:09 +0200 - Merge 10.4 into 10.5
* Merge [Revision #bc89105496](https://github.com/MariaDB/server/commit/bc89105496) 2020-01-28 09:42:21 +0100 - Merge branch 'bb-10.4-release' into 10.4
* [Revision #a915142f48](https://github.com/MariaDB/server/commit/a915142f48)\
  2020-01-28 15:29:05 +0400
  * Fixing a compilation failure of Windows (introduced in [MDEV-21581](https://jira.mariadb.org/browse/MDEV-21581))
* [Revision #f1e13fdc8d](https://github.com/MariaDB/server/commit/f1e13fdc8d)\
  2020-01-26 20:27:13 +0400
  * [MDEV-21581](https://jira.mariadb.org/browse/MDEV-21581) Helper functions and methods for CHARSET\_INFO
* [Revision #dd68ba74f3](https://github.com/MariaDB/server/commit/dd68ba74f3)\
  2020-01-27 10:37:32 +0200
  * Changed Travis to 10.5
* [Revision #b534a6675c](https://github.com/MariaDB/server/commit/b534a6675c)\
  2020-01-24 14:36:43 +0800
  * cleanup redo log
* [Revision #6af00b2cc6](https://github.com/MariaDB/server/commit/6af00b2cc6)\
  2020-01-24 12:59:56 +0200
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678): Ignore #sql-ib tables in --suite=parts
* [Revision #34dafb7e3a](https://github.com/MariaDB/server/commit/34dafb7e3a)\
  2020-01-23 22:46:43 +0800
  * redo log mics fixes
* [Revision #b19760b843](https://github.com/MariaDB/server/commit/b19760b843)\
  2020-01-23 14:27:49 +0100
  * [MDEV-21551](https://jira.mariadb.org/browse/MDEV-21551) : Assertion \`m\_active\_threads.size() >= m\_long\_tasks\_count + m\_waiting\_task\_count' failed"
* [Revision #0e25a8b4a6](https://github.com/MariaDB/server/commit/0e25a8b4a6)\
  2020-01-23 18:15:28 +0530
  * [MDEV-21344](https://jira.mariadb.org/browse/MDEV-21344): Uninitialized tbl\_buf in dict\_acquire\_mdl\_shared()
* [Revision #fde1589f9b](https://github.com/MariaDB/server/commit/fde1589f9b)\
  2020-01-22 19:35:38 +0100
  * [MDEV-21551](https://jira.mariadb.org/browse/MDEV-21551) Fix race condition in thread\_pool\_generic::wait\_begin()
* [Revision #700e010309](https://github.com/MariaDB/server/commit/700e010309)\
  2020-01-21 22:22:48 +0800
  * fix aligned memcpy()-like functions usage
* [Revision #cdd54c852a](https://github.com/MariaDB/server/commit/cdd54c852a)\
  2020-01-22 11:35:50 +0200
  * Cleanup: Make Bounds\_checked\_array default-constructible
* [Revision #eab0dc6854](https://github.com/MariaDB/server/commit/eab0dc6854)\
  2020-01-22 16:19:56 +0530
  * [MDEV-21542](https://jira.mariadb.org/browse/MDEV-21542): main.order\_by\_pack\_big fails sporadically with wrong result
* [Revision #588eac58fd](https://github.com/MariaDB/server/commit/588eac58fd)\
  2020-01-22 10:06:07 +0200
  * [MDEV-21551](https://jira.mariadb.org/browse/MDEV-21551): Fix -Wsign-compare
* [Revision #6f2ca4eac1](https://github.com/MariaDB/server/commit/6f2ca4eac1)\
  2020-01-22 10:06:02 +0200
  * [MDEV-21263](https://jira.mariadb.org/browse/MDEV-21263): Fix -Wclass-memaccess
* [Revision #39e4fe8fa1](https://github.com/MariaDB/server/commit/39e4fe8fa1)\
  2020-01-22 12:28:20 +0530
  * [MDEV-21541](https://jira.mariadb.org/browse/MDEV-21541): main.sum\_distinct-big fails with Assertion \`m\_buffer\_end == null || end <= m\_buffer\_end'
* [Revision #daf28db027](https://github.com/MariaDB/server/commit/daf28db027)\
  2020-01-21 14:27:17 +0400
  * [MDEV-21537](https://jira.mariadb.org/browse/MDEV-21537) InnoDB INFORMATION\_SCHEMA tables fail to define DEFAULT for ENUM NOT NULL
* [Revision #c20bf8fd49](https://github.com/MariaDB/server/commit/c20bf8fd49)\
  2020-01-22 00:01:25 +0100
  * [MDEV-21551](https://jira.mariadb.org/browse/MDEV-21551) Fix calculation of current concurrency level in maybe\_wake\_or\_create\_thread()
* [Revision #92d6c13206](https://github.com/MariaDB/server/commit/92d6c13206)\
  2020-01-21 21:41:16 +0100
  * [MDEV-21548](https://jira.mariadb.org/browse/MDEV-21548) Explicitly declare sql\_bultins library STATIC.
* [Revision #e1b62f3026](https://github.com/MariaDB/server/commit/e1b62f3026)\
  2020-01-21 12:56:54 +0200
  * [MDEV-21263](https://jira.mariadb.org/browse/MDEV-21263): Use C++11 default constructor
* [Revision #6f54a5abea](https://github.com/MariaDB/server/commit/6f54a5abea)\
  2020-01-21 10:48:12 +0100
  * [MDEV-21544](https://jira.mariadb.org/browse/MDEV-21544) instrument sync\_array waits with tpool::wait\_begin/end
* [Revision #28129cd4e1](https://github.com/MariaDB/server/commit/28129cd4e1)\
  2020-01-21 13:35:18 +0530
  * Fix a compilation issue
* [Revision #acc4da9c18](https://github.com/MariaDB/server/commit/acc4da9c18)\
  2020-01-21 08:34:19 +0200
  * After-merge fix
* [Revision #f52bf92014](https://github.com/MariaDB/server/commit/f52bf92014)\
  2020-01-21 01:37:47 +0530
  * [MDEV-21263](https://jira.mariadb.org/browse/MDEV-21263): Allow packed values of non-sorted fields in the sort buffer
* Merge [Revision #ded128aa9b](https://github.com/MariaDB/server/commit/ded128aa9b) 2020-01-20 16:48:56 +0200 - Merge 10.4 into 10.5
* [Revision #64952203af](https://github.com/MariaDB/server/commit/64952203af)\
  2020-01-20 16:41:41 +0200
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115): Fix up sys\_vars.sysvars\_innodb
* [Revision #e9de6386ad](https://github.com/MariaDB/server/commit/e9de6386ad)\
  2020-01-10 21:46:34 +0700
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115) remove now unneeded constraint
* [Revision #744d545fd7](https://github.com/MariaDB/server/commit/744d545fd7)\
  2020-01-17 10:37:11 +0100
  * restore support for --defaults-file=<(...)
* [Revision #8bcbdaf730](https://github.com/MariaDB/server/commit/8bcbdaf730)\
  2020-01-17 10:40:01 +0100
  * cleanup: remove unused arguments
* [Revision #6f65931f88](https://github.com/MariaDB/server/commit/6f65931f88)\
  2020-01-16 13:29:29 +0400
  * [MDEV-19906](https://jira.mariadb.org/browse/MDEV-19906) Port show\_old\_temporals from MySQL 5.6
* [Revision #e7558d4760](https://github.com/MariaDB/server/commit/e7558d4760)\
  2020-01-16 18:04:43 +0100
  * fix compilation w/o perfschema
* [Revision #fc5a6a28f7](https://github.com/MariaDB/server/commit/fc5a6a28f7)\
  2020-01-14 20:55:20 +0100
  * compatibility with pcre2 < 10.30
* [Revision #ff5a528f26](https://github.com/MariaDB/server/commit/ff5a528f26)\
  2020-01-13 13:08:55 +0100
  * mysqltest crashes on Debian
* [Revision #1b1bf430b8](https://github.com/MariaDB/server/commit/1b1bf430b8)\
  2020-01-12 20:50:14 +0100
  * tolerate old pcre versions without PCRE2\_EXTENDED\_MORE flag
* [Revision #0b8b84d8d8](https://github.com/MariaDB/server/commit/0b8b84d8d8)\
  2020-01-16 13:25:37 +0100
  * [MDEV-21501](https://jira.mariadb.org/browse/MDEV-21501) Innodb AIO: release IO slots early in io\_callback
* [Revision #c32fd50952](https://github.com/MariaDB/server/commit/c32fd50952)\
  2020-01-16 10:13:24 +0400
  * A cleanup for [MDEV-16542](https://jira.mariadb.org/browse/MDEV-16542) Fix ALTER TABLE FORCE to upgrade temporal types
* [Revision #497ee33848](https://github.com/MariaDB/server/commit/497ee33848)\
  2020-01-15 07:58:50 +0400
  * [MDEV-21497](https://jira.mariadb.org/browse/MDEV-21497) Make Field\_time, Field\_datetime, Field\_timestamp abstract
* [Revision #cc3135cf83](https://github.com/MariaDB/server/commit/cc3135cf83)\
  2020-01-14 12:31:17 +0200
  * Fix a typo in a comment
* [Revision #8576a7bacf](https://github.com/MariaDB/server/commit/8576a7bacf)\
  2020-01-13 14:28:08 +0200
  * [MDEV-21281](https://jira.mariadb.org/browse/MDEV-21281) main.backup\_interaction fails intermittently
* [Revision #98a67eccc5](https://github.com/MariaDB/server/commit/98a67eccc5)\
  2019-12-16 18:27:06 +0100
  * [MDEV-21327](https://jira.mariadb.org/browse/MDEV-21327) : MDL wait notification for innodb background threadpool
* [Revision #508bc20a85](https://github.com/MariaDB/server/commit/508bc20a85)\
  2020-01-12 21:34:24 +0100
  * tpool - misc fixes
* [Revision #c27577a1ad](https://github.com/MariaDB/server/commit/c27577a1ad)\
  2019-12-16 18:22:59 +0100
  * [MDEV-21326](https://jira.mariadb.org/browse/MDEV-21326) : Address TSAN warnings in tpool.
* [Revision #1bbb67b3f2](https://github.com/MariaDB/server/commit/1bbb67b3f2)\
  2020-01-12 19:10:59 +0100
  * Fix assertion with --innodb-sync-debug=ON
* [Revision #bada05a883](https://github.com/MariaDB/server/commit/bada05a883)\
  2020-01-12 13:45:36 +0100
  * tpool - implement post-task callback (for Innodb debugging)
* [Revision #90002480e9](https://github.com/MariaDB/server/commit/90002480e9)\
  2020-01-10 19:08:46 +0200
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115): Remove OS\_AIO\_LOG and IORequest::LOG
* [Revision #f7da495a78](https://github.com/MariaDB/server/commit/f7da495a78)\
  2020-01-10 15:12:07 +0200
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115): Remove some redundant comparisons
* [Revision #314a14f20d](https://github.com/MariaDB/server/commit/314a14f20d)\
  2020-01-09 22:45:46 +0700
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115) redo log is not affected by srv\_file\_flush\_method anymore
* [Revision #3a3605f4b1](https://github.com/MariaDB/server/commit/3a3605f4b1)\
  2020-01-08 22:53:03 +0700
  * [MDEV-21382](https://jira.mariadb.org/browse/MDEV-21382) fix compilation without perfschema plugin
* [Revision #9cd6b230ac](https://github.com/MariaDB/server/commit/9cd6b230ac)\
  2020-01-09 09:03:30 +0200
  * [MDEV-20839](https://jira.mariadb.org/browse/MDEV-20839): Re-enable the test
* [Revision #c62efb083c](https://github.com/MariaDB/server/commit/c62efb083c)\
  2020-01-08 18:23:55 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Remove a bogus comment
* [Revision #c4de197a0a](https://github.com/MariaDB/server/commit/c4de197a0a)\
  2020-01-08 14:08:00 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Optimize page\_set\_autoinc()
* [Revision #a0eefdf32e](https://github.com/MariaDB/server/commit/a0eefdf32e)\
  2020-01-08 17:09:31 +0530
  * After-merge fix: Actually apply the changes The merge a8ed0f77a3734be15f95a67b5880ed96919e3236 was accidentally a null-merge.
* Merge [Revision #a8ed0f77a3](https://github.com/MariaDB/server/commit/a8ed0f77a3) 2020-01-08 16:37:59 +0530 - Merge branch '10.4' into 10.5
* [Revision #3d9759a9b5](https://github.com/MariaDB/server/commit/3d9759a9b5)\
  2020-01-07 23:43:30 +0700
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115) fix counter
* Merge [Revision #68fe5f534c](https://github.com/MariaDB/server/commit/68fe5f534c) 2020-01-07 14:10:15 +0200 - Merge 10.4 into 10.5
* [Revision #1488de674c](https://github.com/MariaDB/server/commit/1488de674c)\
  2020-01-07 16:38:14 +0530
  * [MDEV-21344](https://jira.mariadb.org/browse/MDEV-21344) Valgrind uninitialised value warnings in dict\_acquire\_mdl\_shared
* [Revision #6f2e228529](https://github.com/MariaDB/server/commit/6f2e228529)\
  2020-01-05 00:44:47 +0700
  * [MDEV-21382](https://jira.mariadb.org/browse/MDEV-21382) use fdatasync() for redo log where appropriate
* [Revision #d9789718b9](https://github.com/MariaDB/server/commit/d9789718b9)\
  2020-01-04 00:23:26 +0700
  * bling windows build fix
* [Revision #ccd87d34a4](https://github.com/MariaDB/server/commit/ccd87d34a4)\
  2020-01-03 17:54:12 +0200
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678): Ignore #sql-ib tables in main.partition\_alter
* Merge [Revision #ca8c3be47d](https://github.com/MariaDB/server/commit/ca8c3be47d) 2020-01-03 16:15:40 +0200 - Merge 10.4 into 10.5
* [Revision #9949ab9393](https://github.com/MariaDB/server/commit/9949ab9393)\
  2020-01-02 11:05:47 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Cleanup MLOG\_FILE\_NAME logging
* [Revision #562c037b48](https://github.com/MariaDB/server/commit/562c037b48)\
  2019-11-25 22:32:24 +0700
  * [MDEV-18115](https://jira.mariadb.org/browse/MDEV-18115) Remove dummy tablespace for the redo log
* Merge [Revision #3fa4a9e6be](https://github.com/MariaDB/server/commit/3fa4a9e6be) 2019-12-30 10:29:43 +0200 - Merge 10.4 into 10.5
* [Revision #b36154a109](https://github.com/MariaDB/server/commit/b36154a109)\
  2019-12-27 21:20:03 +0200
  * Cleanup log\_rec\_t
* Merge [Revision #8cc15c036d](https://github.com/MariaDB/server/commit/8cc15c036d) 2019-12-27 21:17:16 +0200 - Merge 10.4 into 10.5
* [Revision #cc28947315](https://github.com/MariaDB/server/commit/cc28947315)\
  2019-12-16 17:59:42 +0100
  * [MDEV-20632](https://jira.mariadb.org/browse/MDEV-20632): prerequisite:
* [Revision #961413d26f](https://github.com/MariaDB/server/commit/961413d26f)\
  2019-12-25 15:09:51 +0000
  * Fix PCRE2 build for Windows, with Ninja and Makefiles generator.
* [Revision #373443903b](https://github.com/MariaDB/server/commit/373443903b)\
  2019-12-20 01:32:37 +0800
  * [MDEV-21362](https://jira.mariadb.org/browse/MDEV-21362) do something with -fno-builtin-memcmp for rem0cmp.cc
* [Revision #714762ddb7](https://github.com/MariaDB/server/commit/714762ddb7)\
  2019-12-23 17:48:01 +0530
  * [MDEV-18648](https://jira.mariadb.org/browse/MDEV-18648): slave\_parallel\_mode= optimistic default in 10.5
* [Revision #7e10e80b8f](https://github.com/MariaDB/server/commit/7e10e80b8f)\
  2019-12-20 15:51:37 +0100
  * correct dbug function names
* [Revision #83b0468c47](https://github.com/MariaDB/server/commit/83b0468c47)\
  2019-12-20 15:51:25 +0100
  * dependencies for VS
* [Revision #67f928d8c2](https://github.com/MariaDB/server/commit/67f928d8c2)\
  2019-12-18 17:51:01 +0100
  * remove pcre, add support for bundled pcre2
* [Revision #3b654d54c1](https://github.com/MariaDB/server/commit/3b654d54c1)\
  2019-12-18 17:50:09 +0100
  * longer regex error messages
* [Revision #9dadfdcde5](https://github.com/MariaDB/server/commit/9dadfdcde5)\
  2019-12-17 01:37:59 +0400
  * [MDEV-14024](https://jira.mariadb.org/browse/MDEV-14024) PCRE2.
* [Revision #ce70573f62](https://github.com/MariaDB/server/commit/ce70573f62)\
  2019-12-20 17:57:32 +0200
  * [MDEV-21353](https://jira.mariadb.org/browse/MDEV-21353) Assertion failures due to btr\_pcur\_restore\_pos() misbehaving
* [Revision #305081a735](https://github.com/MariaDB/server/commit/305081a735)\
  2019-12-16 14:27:06 +0700
  * check I/O buffer size and alignment in InnoDB
* [Revision #44be8652c5](https://github.com/MariaDB/server/commit/44be8652c5)\
  2019-12-18 16:27:26 +0200
  * Cleanup: Remove fil\_space\_get\_flags()
* [Revision #fb4a897fd9](https://github.com/MariaDB/server/commit/fb4a897fd9)\
  2019-12-17 15:39:21 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Remove UNIV\_LOG\_LSN\_DEBUG
* Merge [Revision #3c7718150d](https://github.com/MariaDB/server/commit/3c7718150d) 2019-12-17 14:46:57 +0200 - Merge 10.4 into 10.5
* [Revision #c24253d0fa](https://github.com/MariaDB/server/commit/c24253d0fa)\
  2019-12-16 13:14:05 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Fix the WITH\_INNODB\_EXTRA\_DEBUG build
* [Revision #89633995e4](https://github.com/MariaDB/server/commit/89633995e4)\
  2019-12-16 08:53:00 +0200
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678): Actually ignore #sql-ib tables
* Merge [Revision #28c89b7151](https://github.com/MariaDB/server/commit/28c89b7151) 2019-12-16 07:47:17 +0200 - Merge 10.4 into 10.5
* [Revision #745fd4b39f](https://github.com/MariaDB/server/commit/745fd4b39f)\
  2019-12-13 17:53:55 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Remove some mlog\_write\_initial\_log\_record\_fast()
* [Revision #2b5a269cb4](https://github.com/MariaDB/server/commit/2b5a269cb4)\
  2019-12-13 15:58:30 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Clean up record insertion
* [Revision #befde6e97e](https://github.com/MariaDB/server/commit/befde6e97e)\
  2019-12-13 15:28:39 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Clean up page\_cur\_delete\_rec()
* [Revision #1c282d4bc4](https://github.com/MariaDB/server/commit/1c282d4bc4)\
  2019-12-13 18:02:59 +0200
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678): Ignore stray #sql-ib tables
* [Revision #a9ea0056c7](https://github.com/MariaDB/server/commit/a9ea0056c7)\
  2019-12-13 16:40:16 +0700
  * [MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133): use aligned memcpy in redo log and buffer pool
* [Revision #bbd2fa5c65](https://github.com/MariaDB/server/commit/bbd2fa5c65)\
  2019-12-12 17:06:42 +0400
  * [MDEV-21278](https://jira.mariadb.org/browse/MDEV-21278) Assertion `is_unsigned() == attr.unsigned_flag' or Assertion` field.is\_sane()' failed
* [Revision #ce41a9075a](https://github.com/MariaDB/server/commit/ce41a9075a)\
  2019-12-12 21:12:52 +0700
  * fix a memory leak introduced by f4b4284650cc787b8e4c9d4515dca1917cb138b5
* [Revision #f4b4284650](https://github.com/MariaDB/server/commit/f4b4284650)\
  2019-12-11 23:32:50 +0700
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678) Prefer MDL to dict\_sys.latch for innodb background tasks
* [Revision #adb117cf69](https://github.com/MariaDB/server/commit/adb117cf69)\
  2019-12-10 16:18:30 +0200
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678): Fix a problem with duplicate #sql2 table names
* [Revision #ea37b14409](https://github.com/MariaDB/server/commit/ea37b14409)\
  2019-12-10 15:42:50 +0200
  * [MDEV-16678](https://jira.mariadb.org/browse/MDEV-16678) Prefer MDL to dict\_sys.latch for innodb background tasks
* [Revision #e47bd0073c](https://github.com/MariaDB/server/commit/e47bd0073c)\
  2019-12-09 20:23:51 +0100
  * [MDEV-21262](https://jira.mariadb.org/browse/MDEV-21262) MTR does not work with Windows ASAN builds
* [Revision #66de4fef76](https://github.com/MariaDB/server/commit/66de4fef76)\
  2019-11-29 22:26:04 +0000
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) - some improvements
* [Revision #d3b2625ba0](https://github.com/MariaDB/server/commit/d3b2625ba0)\
  2019-12-09 21:11:08 +0200
  * [MDEV-21259](https://jira.mariadb.org/browse/MDEV-21259) Assertion failed in mtr\_t::write()
* [Revision #d30dbaa20d](https://github.com/MariaDB/server/commit/d30dbaa20d)\
  2019-12-07 18:17:08 +0400
  * A cleanup for [MDEV-8844](https://jira.mariadb.org/browse/MDEV-8844): Fixing compilation failure on Windows
* [Revision #3c6065a270](https://github.com/MariaDB/server/commit/3c6065a270)\
  2019-12-06 18:51:05 +0400
  * [MDEV-8844](https://jira.mariadb.org/browse/MDEV-8844) Unreadable control characters printed as is in warnings
* [Revision #00445652db](https://github.com/MariaDB/server/commit/00445652db)\
  2019-12-06 10:27:59 +0400
  * A cleanup for [MDEV-17088](https://jira.mariadb.org/browse/MDEV-17088) Provide tools to encode/decode mysql-encoded file system names
* [Revision #1b040ce570](https://github.com/MariaDB/server/commit/1b040ce570)\
  2019-12-06 04:32:56 +0900
  * fix compiler warnings
* [Revision #6189774c37](https://github.com/MariaDB/server/commit/6189774c37)\
  2019-12-05 12:44:19 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Fix undefined behaviour
* [Revision #46fc3bdbca](https://github.com/MariaDB/server/commit/46fc3bdbca)\
  2019-12-05 08:19:49 +0200
  * [MDEV-21225](https://jira.mariadb.org/browse/MDEV-21225): Fix warnings
* [Revision #2c7b6214e7](https://github.com/MariaDB/server/commit/2c7b6214e7)\
  2019-12-03 17:21:25 +0400
  * A cleanup for [MDEV-17088](https://jira.mariadb.org/browse/MDEV-17088) Provide tools to encode/decode mysql-encoded file system names
* [Revision #42a4ae54c2](https://github.com/MariaDB/server/commit/42a4ae54c2)\
  2019-12-05 06:42:31 +0200
  * [MDEV-21225](https://jira.mariadb.org/browse/MDEV-21225) Remove ut\_align() and use aligned\_malloc()
* [Revision #504202bd7f](https://github.com/MariaDB/server/commit/504202bd7f)\
  2019-12-04 20:01:04 +0200
  * [MDEV-21216](https://jira.mariadb.org/browse/MDEV-21216): Remove fsp\_header\_get\_space\_id()
* [Revision #2352f51625](https://github.com/MariaDB/server/commit/2352f51625)\
  2019-12-04 18:25:01 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Fix Galera
* [Revision #6b5cdd4ff7](https://github.com/MariaDB/server/commit/6b5cdd4ff7)\
  2019-12-04 15:19:39 +0200
  * [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514): Update stale comments
* [Revision #95e903261e](https://github.com/MariaDB/server/commit/95e903261e)\
  2019-12-04 15:00:57 +0200
  * [MDEV-21216](https://jira.mariadb.org/browse/MDEV-21216) InnoDB does dirty read of TRX\_SYS page before recovery
* [Revision #e5dfdc5606](https://github.com/MariaDB/server/commit/e5dfdc5606)\
  2019-12-04 14:45:11 +0200
  * Cleanup: use constexpr for SRV\_UNDO\_TABLESPACE\_SIZE\_IN\_PAGES
* [Revision #bf3034195f](https://github.com/MariaDB/server/commit/bf3034195f)\
  2019-11-26 09:35:09 +0100
  * Part2: [MDEV-12518](https://jira.mariadb.org/browse/MDEV-12518) Unify sql\_yacc.yy and sql\_yacc\_ora.yy
* [Revision #3f9d7072e9](https://github.com/MariaDB/server/commit/3f9d7072e9)\
  2019-11-25 12:19:39 +0400
  * Part1: [MDEV-12518](https://jira.mariadb.org/browse/MDEV-12518) Unify sql\_yacc.yy and sql\_yacc\_ora.yy
* [Revision #bb45941685](https://github.com/MariaDB/server/commit/bb45941685)\
  2019-12-04 10:51:38 +0200
  * [MDEV-21205](https://jira.mariadb.org/browse/MDEV-21205) Assertion failure in btr\_sec\_min\_rec\_mark
* [Revision #3b9a978a3b](https://github.com/MariaDB/server/commit/3b9a978a3b)\
  2019-12-03 15:32:40 -0500
  * bump the VERSION
* [Revision #2ac0e64cad](https://github.com/MariaDB/server/commit/2ac0e64cad)\
  2019-12-03 12:22:58 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Fix the 32-bit build
* [Revision #af5947f433](https://github.com/MariaDB/server/commit/af5947f433)\
  2019-12-03 10:29:50 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Replace mlog\_write\_string() with mtr\_t::memcpy()
* [Revision #87839258f8](https://github.com/MariaDB/server/commit/87839258f8)\
  2019-12-03 10:26:53 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Replace mlog\_memset() with mtr\_t::memset()
* [Revision #caea64df18](https://github.com/MariaDB/server/commit/caea64df18)\
  2019-12-03 10:20:44 +0200
  * Cleanup: Remove some page\_get\_page\_no() calls
* [Revision #56f6dab1d0](https://github.com/MariaDB/server/commit/56f6dab1d0)\
  2019-12-03 10:19:45 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Replace mlog\_write\_ulint() with mtr\_t::write()
* [Revision #504823bcce](https://github.com/MariaDB/server/commit/504823bcce)\
  2019-12-02 18:50:05 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Cleanup MLOG\_PAGE\_CREATE
* [Revision #57444a3b30](https://github.com/MariaDB/server/commit/57444a3b30)\
  2019-12-03 08:44:49 +0200
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264): Minor cleanup
* [Revision #cd92c6c83d](https://github.com/MariaDB/server/commit/cd92c6c83d)\
  2019-12-02 16:16:38 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Do not write MLOG\_REC\_MIN\_MARK
* [Revision #8ebd91c1a9](https://github.com/MariaDB/server/commit/8ebd91c1a9)\
  2019-12-02 08:57:33 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Do not write MLOG\_FILE\_WRITE\_CRYPT\_DATA
* [Revision #bf2cc46798](https://github.com/MariaDB/server/commit/bf2cc46798)\
  2019-12-02 10:04:55 +0200
  * [MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133): Remove buf\_frame\_copy()
* [Revision #6f89946892](https://github.com/MariaDB/server/commit/6f89946892)\
  2019-12-03 11:53:26 +0300
  * [MDEV-17554](https://jira.mariadb.org/browse/MDEV-17554) versioning partition tests reorganize
* [Revision #9ed8d364cd](https://github.com/MariaDB/server/commit/9ed8d364cd)\
  2019-12-03 11:53:25 +0300
  * [MDEV-17554](https://jira.mariadb.org/browse/MDEV-17554) history partitioning cleanups
* Merge [Revision #8ed646f071](https://github.com/MariaDB/server/commit/8ed646f071) 2019-12-02 13:35:54 +0300 - Merge 10.4 into 10.5
* [Revision #523879dd51](https://github.com/MariaDB/server/commit/523879dd51)\
  2019-11-30 13:18:28 +0400
  * A cleanup for [MDEV-17088](https://jira.mariadb.org/browse/MDEV-17088): disabling mariadb-conv-\*.test for embedded
* [Revision #326515878d](https://github.com/MariaDB/server/commit/326515878d)\
  2019-11-29 14:48:47 +0200
  * [MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133): Alignment hints for ROW\_FORMAT=COMPRESSED
* Merge [Revision #5a00792c69](https://github.com/MariaDB/server/commit/5a00792c69) 2019-11-29 11:25:40 +0200 - Merge 10.4 into 10.5
* [Revision #51a4260f00](https://github.com/MariaDB/server/commit/51a4260f00)\
  2019-11-29 11:23:35 +0200
  * [MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133): Introduce memmove\_aligned()
* Merge [Revision #0f71e9e66b](https://github.com/MariaDB/server/commit/0f71e9e66b) 2019-11-28 19:55:16 +0200 - Merge 10.4 into 10.5
* [Revision #683bc53dc8](https://github.com/MariaDB/server/commit/683bc53dc8)\
  2019-11-28 16:39:15 +0200
  * [MDEV-21132](https://jira.mariadb.org/browse/MDEV-21132): Add debug assertions
* Merge [Revision #beae2cf006](https://github.com/MariaDB/server/commit/beae2cf006) 2019-11-28 16:35:20 +0200 - Merge 10.4 into 10.5
* [Revision #bacdc4df61](https://github.com/MariaDB/server/commit/bacdc4df61)\
  2019-11-28 14:29:36 +0100
  * [MDEV-17088](https://jira.mariadb.org/browse/MDEV-17088) - fix overlinking
* [Revision #4ad083cd64](https://github.com/MariaDB/server/commit/4ad083cd64)\
  2019-11-27 13:29:03 +0400
  * [MDEV-17088](https://jira.mariadb.org/browse/MDEV-17088) Provide tools to encode/decode mysql-encoded file system names
* [Revision #f6003fbc8c](https://github.com/MariaDB/server/commit/f6003fbc8c)\
  2019-11-28 17:37:57 +0500
  * [MDEV-21140](https://jira.mariadb.org/browse/MDEV-21140) Make galera\_recovery.sh work with fs.protected\_regular = 1 (#1417)
* [Revision #a6e8a7df82](https://github.com/MariaDB/server/commit/a6e8a7df82)\
  2019-11-28 11:44:40 +0200
  * Cleanup: flst\_read\_addr(), fil\_addr\_t
* Merge [Revision #29710b2839](https://github.com/MariaDB/server/commit/29710b2839) 2019-11-27 16:02:34 +0100 - Merge branch '10.4' into 10.5
* Merge [Revision #ddbbf97670](https://github.com/MariaDB/server/commit/ddbbf97670) 2019-11-27 06:29:14 +0200 - Merge 10.4 into 10.5
* [Revision #d1851b3009](https://github.com/MariaDB/server/commit/d1851b3009)\
  2019-11-26 19:52:07 +0200
  * Code cleanups
* [Revision #dc75f3e06d](https://github.com/MariaDB/server/commit/dc75f3e06d)\
  2019-11-26 16:32:51 +0200
  * [MDEV-21152](https://jira.mariadb.org/browse/MDEV-21152) Bogus debug assertion btr\_pcur\_is\_after\_last\_in\_tree() in ibuf code
* [Revision #a35427f3fb](https://github.com/MariaDB/server/commit/a35427f3fb)\
  2019-11-26 15:45:31 +0300
  * [MDEV-21127](https://jira.mariadb.org/browse/MDEV-21127) Assertion in key\_text::key\_text()
* [Revision #25e2a556de](https://github.com/MariaDB/server/commit/25e2a556de)\
  2019-11-26 10:14:07 +0200
  * [MDEV-21133](https://jira.mariadb.org/browse/MDEV-21133) Optimize access to InnoDB page header fields
* [Revision #86407a59b3](https://github.com/MariaDB/server/commit/86407a59b3)\
  2019-11-25 17:09:26 +0100
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) - Fix assertion \`m\_queue.empty() && !m\_tasks\_running' in tpool::task\_group destructor
* [Revision #38c2c16cc4](https://github.com/MariaDB/server/commit/38c2c16cc4)\
  2019-06-19 18:20:49 +0400
  * Removed tc\_purge() and purge\_tables() argument
* [Revision #092834cd2c](https://github.com/MariaDB/server/commit/092834cd2c)\
  2019-06-19 17:42:37 +0400
  * Removed kill\_delayed\_threads\_for\_table()
* [Revision #0aa807d100](https://github.com/MariaDB/server/commit/0aa807d100)\
  2019-06-19 14:59:36 +0400
  * Removed tdc\_increment\_refresh\_version()
* Merge [Revision #0c05a2ed71](https://github.com/MariaDB/server/commit/0c05a2ed71) 2019-11-25 17:24:09 +0300 - Merge 10.4 into 10.5

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
