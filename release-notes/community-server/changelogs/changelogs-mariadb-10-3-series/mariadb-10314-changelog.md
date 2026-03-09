# MariaDB 10.3.14 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.14)[Release Notes](../../old-releases/10.3/10.3.14.md)[Changelog](mariadb-10314-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 2 Apr 2019

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.14.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #ab7b9cf912](https://github.com/MariaDB/server/commit/ab7b9cf912)\
  2019-04-01 16:58:37 +0300
  * Updated list of unstable tests for 10.3.14 release
* [Revision #ed661a0e59](https://github.com/MariaDB/server/commit/ed661a0e59)\
  2019-03-29 19:42:01 +0100
  * post-merge: -Werror fixes in 10.3
* Merge [Revision #4e1d3f83b7](https://github.com/MariaDB/server/commit/4e1d3f83b7) 2019-03-29 19:40:56 +0100 - Merge branch '10.2' into 10.3
* [Revision #cc71e7501c](https://github.com/MariaDB/server/commit/cc71e7501c)\
  2019-03-28 12:07:20 +0100
  * post-merge: -Werror fixes in 10.2
* Merge [Revision #f2a0c758da](https://github.com/MariaDB/server/commit/f2a0c758da) 2019-03-29 10:58:20 +0100 - Merge branch '10.1' into 10.2
* [Revision #d0116e10a5](https://github.com/MariaDB/server/commit/d0116e10a5)\
  2019-03-28 12:27:06 +0200
  * Revert [MDEV-18464](https://jira.mariadb.org/browse/MDEV-18464) and [MDEV-12009](https://jira.mariadb.org/browse/MDEV-12009)
* [Revision #81d71ee6b2](https://github.com/MariaDB/server/commit/81d71ee6b2)\
  2019-02-05 15:41:53 +0200
  * [MDEV-12009](https://jira.mariadb.org/browse/MDEV-12009): Allow to force kill user threads/query which are flagged as high priority by Galera
* [Revision #21b2fada7a](https://github.com/MariaDB/server/commit/21b2fada7a)\
  2019-03-27 09:28:49 +0200
  * [MDEV-18464](https://jira.mariadb.org/browse/MDEV-18464): Port kill\_one\_trx fixes from 10.4 to 10.1
* [Revision #deff3f7572](https://github.com/MariaDB/server/commit/deff3f7572)\
  2019-03-22 19:28:59 +0100
  * [MDEV-18466](https://jira.mariadb.org/browse/MDEV-18466) Unsafe to log updates on tables referenced by foreign keys with triggers in statement format
* [Revision #d8084116b5](https://github.com/MariaDB/server/commit/d8084116b5)\
  2019-03-16 19:44:40 +0100
  * [MDEV-7066](https://jira.mariadb.org/browse/MDEV-7066) No Source RPMs ... (and so no "yum-builddep MariaDB-server" either)
* [Revision #b12f14965d](https://github.com/MariaDB/server/commit/b12f14965d)\
  2019-03-16 19:37:44 +0100
  * [MDEV-7066](https://jira.mariadb.org/browse/MDEV-7066) No Source RPMs ... (and so no "yum-builddep MariaDB-server" either)
* [Revision #ecc2711328](https://github.com/MariaDB/server/commit/ecc2711328)\
  2019-03-16 19:33:07 +0100
  * [MDEV-7066](https://jira.mariadb.org/browse/MDEV-7066) No Source RPMs ... (and so no "yum-builddep MariaDB-server" either)
* [Revision #86e80f944f](https://github.com/MariaDB/server/commit/86e80f944f)\
  2019-03-16 19:30:51 +0100
  * cmake: don't do fake rpm Provides
* [Revision #39cea72e7b](https://github.com/MariaDB/server/commit/39cea72e7b)\
  2019-03-17 15:05:56 +0100
  * cmake: fix cpack\_source\_ignore\_files
* [Revision #6417297180](https://github.com/MariaDB/server/commit/6417297180)\
  2019-03-16 19:27:51 +0100
  * cmake: remove workarounds for cmake bugs #13248 and #12864
* [Revision #f97d879bf8](https://github.com/MariaDB/server/commit/f97d879bf8)\
  2019-03-16 19:24:49 +0100
  * cmake: re-enable -Werror in the maintainer mode
* Merge [Revision #1a4746e128](https://github.com/MariaDB/server/commit/1a4746e128) 2019-03-27 19:35:03 +0100 - Merge branch '5.5' into 10.1
* [Revision #f2d549d8db](https://github.com/MariaDB/server/commit/f2d549d8db)\
  2019-03-27 12:34:03 +0530
  * [MDEV-14784](https://jira.mariadb.org/browse/MDEV-14784): Slave crashes in show\_status\_array upon running a trigger with select from I\_S
* [Revision #9a8b8ea66b](https://github.com/MariaDB/server/commit/9a8b8ea66b)\
  2019-03-27 14:37:14 +0100
  * [MDEV-19060](https://jira.mariadb.org/browse/MDEV-19060) : mariadb-backup continues, despite failing to open a tablespace
* [Revision #fc168c3a5e](https://github.com/MariaDB/server/commit/fc168c3a5e)\
  2019-03-29 11:38:45 +0200
  * [MDEV-15587](https://jira.mariadb.org/browse/MDEV-15587) AES test fails, segfaults in EVP\_CipherInit\_ex
* [Revision #8fcd9478cc](https://github.com/MariaDB/server/commit/8fcd9478cc)\
  2019-03-28 15:54:42 +0300
  * [MDEV-18080](https://jira.mariadb.org/browse/MDEV-18080), part#1: MyRocks is slow with log-bin=off
* [Revision #e42192d7b3](https://github.com/MariaDB/server/commit/e42192d7b3)\
  2019-03-28 20:35:39 +0530
  * [MDEV-13895](https://jira.mariadb.org/browse/MDEV-13895): GTID and Master\_Delay causes excessive initial delay
* [Revision #05ad7fc3ed](https://github.com/MariaDB/server/commit/05ad7fc3ed)\
  2019-03-28 11:42:21 +0100
  * [MDEV-19054](https://jira.mariadb.org/browse/MDEV-19054) : mysql\_upgrade\_service now allows MySQL 5.7 to [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) upgrade.
* [Revision #0623cc7c16](https://github.com/MariaDB/server/commit/0623cc7c16)\
  2019-03-27 18:58:43 +0530
  * [MDEV-19051](https://jira.mariadb.org/browse/MDEV-19051) Avoid unnecessary writing MLOG\_INDEX\_LOAD
* [Revision #38cad6875f](https://github.com/MariaDB/server/commit/38cad6875f)\
  2019-03-28 13:14:49 +0530
  * [MDEV-18899](https://jira.mariadb.org/browse/MDEV-18899): Server crashes in Field::set\_warning\_truncated\_wrong\_value
* [Revision #a82cfe109c](https://github.com/MariaDB/server/commit/a82cfe109c)\
  2019-03-27 16:35:19 +0100
  * cleanup: move rbr-only test to rpl\_row.test
* [Revision #39d7e5969b](https://github.com/MariaDB/server/commit/39d7e5969b)\
  2018-07-05 21:03:37 +1000
  * [MDEV-16252](https://jira.mariadb.org/browse/MDEV-16252): MINIMAL binlog\_row\_image does not work for versioned tables
* [Revision #8123d79911](https://github.com/MariaDB/server/commit/8123d79911)\
  2019-03-26 20:19:32 +0100
  * [MDEV-15951](https://jira.mariadb.org/browse/MDEV-15951) system versioning by trx id doesn't work with partitioning
* [Revision #e6230e844c](https://github.com/MariaDB/server/commit/e6230e844c)\
  2019-02-22 22:17:41 +1000
  * [MDEV-15951](https://jira.mariadb.org/browse/MDEV-15951) system versioning by trx id doesn't work with partitioning
* [Revision #f6ee132491](https://github.com/MariaDB/server/commit/f6ee132491)\
  2018-12-19 14:05:40 +0300
  * Versioning tests stability improvement
* [Revision #8df04fb894](https://github.com/MariaDB/server/commit/8df04fb894)\
  2018-07-30 19:50:42 +0300
  * [MDEV-15412](https://jira.mariadb.org/browse/MDEV-15412) For any non-existing transaction ID, AS OF provides the current table contents without a warning
* [Revision #5c0bb0766d](https://github.com/MariaDB/server/commit/5c0bb0766d)\
  2019-03-29 11:56:52 +0200
  * Update 10.3 man pages
* [Revision #f3ff45f955](https://github.com/MariaDB/server/commit/f3ff45f955)\
  2019-03-27 15:00:12 +0200
  * [MDEV-15658](https://jira.mariadb.org/browse/MDEV-15658): Assertion failed in lock\_rec\_other\_trx\_holds\_expl\_callback
* Merge [Revision #349560d5d5](https://github.com/MariaDB/server/commit/349560d5d5) 2019-03-27 13:09:09 +0200 - Merge 10.2 into 10.3
* Merge [Revision #1e9c2b2305](https://github.com/MariaDB/server/commit/1e9c2b2305) 2019-03-27 12:26:11 +0200 - Merge 10.1 into 10.2
* Merge [Revision #a6585d5ce9](https://github.com/MariaDB/server/commit/a6585d5ce9) 2019-03-27 11:56:08 +0200 - Merge 10.0 into 10.1
* [Revision #828cc2ba7c](https://github.com/MariaDB/server/commit/828cc2ba7c)\
  2019-03-27 11:34:53 +0200
  * [MDEV-18417](https://jira.mariadb.org/browse/MDEV-18417)/[MDEV-18656](https://jira.mariadb.org/browse/MDEV-18656)/[MDEV-18417](https://jira.mariadb.org/browse/MDEV-18417): Work around compiler ASAN bug
* Merge [Revision #1933cf98e8](https://github.com/MariaDB/server/commit/1933cf98e8) 2019-03-26 14:13:46 +0200 - Merge 5.5 into 10.0
* [Revision #e890711279](https://github.com/MariaDB/server/commit/e890711279)\
  2019-03-26 00:42:57 +0400
  * Fixed ps-protocol thread\_pool\_server\_audit failure
* [Revision #cfe0fe1ad1](https://github.com/MariaDB/server/commit/cfe0fe1ad1)\
  2019-01-26 19:12:17 +0100
  * Fix tests in 2020
* [Revision #c61e8a6597](https://github.com/MariaDB/server/commit/c61e8a6597)\
  2019-03-24 13:24:28 -0400
  * Fix for [MDEV-17449](https://jira.mariadb.org/browse/MDEV-17449), typo in error message (#1146)
* [Revision #d8b7e76c37](https://github.com/MariaDB/server/commit/d8b7e76c37)\
  2019-02-07 01:23:28 -0500
  * Fix for [MDEV-18276](https://jira.mariadb.org/browse/MDEV-18276), typo in error message + all other occurrences of refering
* [Revision #778c525ff8](https://github.com/MariaDB/server/commit/778c525ff8)\
  2019-03-20 15:04:24 +0530
  * [MDEV-17119](https://jira.mariadb.org/browse/MDEV-17119) replicate\_rewrite\_db does not work for single chardatabase name
* [Revision #f00e25b4c4](https://github.com/MariaDB/server/commit/f00e25b4c4)\
  2019-02-10 15:48:12 -0500
  * Fix for [MDEV-15538](https://jira.mariadb.org/browse/MDEV-15538), '-N' Produce html output wrong
* Merge [Revision #2d592f757c](https://github.com/MariaDB/server/commit/2d592f757c) 2019-03-26 17:41:12 +0200 - Merge 10.2 into 10.3
* Merge [Revision #c676f58c27](https://github.com/MariaDB/server/commit/c676f58c27) 2019-03-26 17:38:33 +0200 - Merge 10.1 into 10.2
* [Revision #762419a573](https://github.com/MariaDB/server/commit/762419a573)\
  2019-03-26 17:19:05 +0200
  * Fixup for [MDEV-18968](https://jira.mariadb.org/browse/MDEV-18968)
* [Revision #a138d061b5](https://github.com/MariaDB/server/commit/a138d061b5)\
  2019-03-20 21:10:09 +0300
  * [MDEV-18869](https://jira.mariadb.org/browse/MDEV-18869) Assertion \`!((field)->vcol\_info && (field)->stored\_in\_db())' failed in innodb\_col\_no upon altering table with system versioning
* Merge [Revision #ffc69dbd05](https://github.com/MariaDB/server/commit/ffc69dbd05) 2019-03-26 15:03:37 +0200 - Merge 10.2 into 10.3
* Merge [Revision #ac4934535d](https://github.com/MariaDB/server/commit/ac4934535d) 2019-03-26 14:59:32 +0200 - Merge 10.1 into 10.2
* [Revision #f2c1c9590c](https://github.com/MariaDB/server/commit/f2c1c9590c)\
  2019-03-26 14:57:33 +0200
  * Fix cmake -DENABLED\_PROFILING=OFF
* Merge [Revision #226ca250ed](https://github.com/MariaDB/server/commit/226ca250ed) 2019-03-26 14:17:19 +0200 - Merge 10.1 into 10.2
* Merge [Revision #42fd537244](https://github.com/MariaDB/server/commit/42fd537244) 2019-03-26 13:51:40 +0200 - Merge 10.0 into 10.1
* [Revision #137812c88a](https://github.com/MariaDB/server/commit/137812c88a)\
  2018-11-28 15:25:53 +0100
  * Fix USE\_AFTER\_FREE (CWE-416)
* [Revision #9d2d80aace](https://github.com/MariaDB/server/commit/9d2d80aace)\
  2019-02-07 03:29:12 -0500
  * Update sql\_parse.cc
* [Revision #065ba53ccb](https://github.com/MariaDB/server/commit/065ba53ccb)\
  2019-03-26 13:51:15 +0200
  * [MDEV-12711](https://jira.mariadb.org/browse/MDEV-12711) mariadb-backup --backup is refused for multi-file system tablespace
* [Revision #6fbbb0853e](https://github.com/MariaDB/server/commit/6fbbb0853e)\
  2019-03-26 11:37:18 +0400
  * [MDEV-18968](https://jira.mariadb.org/browse/MDEV-18968) Both (WHERE 0.1) and (WHERE NOT 0.1) return empty set
* [Revision #ed643f4bb3](https://github.com/MariaDB/server/commit/ed643f4bb3)\
  2018-11-29 15:59:26 +0100
  * Fix resource leak
* [Revision #f704361cd6](https://github.com/MariaDB/server/commit/f704361cd6)\
  2019-03-22 15:48:49 +0400
  * Backporting slow log simulation logic details from 10.2 to 10.1
* [Revision #9c9bf9642e](https://github.com/MariaDB/server/commit/9c9bf9642e)\
  2018-12-04 14:45:27 +0100
  * Fix resource leak
* [Revision #89e390b7ce](https://github.com/MariaDB/server/commit/89e390b7ce)\
  2018-11-29 16:08:55 +0100
  * Fix resource leak
* [Revision #9ff713d33a](https://github.com/MariaDB/server/commit/9ff713d33a)\
  2018-11-29 15:28:03 +0100
  * Fix resource leak
* [Revision #b30bbb7d9a](https://github.com/MariaDB/server/commit/b30bbb7d9a)\
  2019-03-25 12:53:20 -0400
  * bump the VERSION
* [Revision #07096ada9b](https://github.com/MariaDB/server/commit/07096ada9b)\
  2019-03-25 17:15:34 +0200
  * Fix the Windows build
* Merge [Revision #dbc0d576a3](https://github.com/MariaDB/server/commit/dbc0d576a3) 2019-03-25 16:14:39 +0200 - Merge 10.2 into 10.3
* [Revision #525e79b057](https://github.com/MariaDB/server/commit/525e79b057)\
  2019-03-25 16:03:24 +0200
  * [MDEV-19022](https://jira.mariadb.org/browse/MDEV-19022): InnoDB fails to cleanup useless B-tree pages
* [Revision #ade0a0e9d5](https://github.com/MariaDB/server/commit/ade0a0e9d5)\
  2019-03-25 15:55:00 +0200
  * Avoid sign mismatch in comparisons
* [Revision #1bd9815479](https://github.com/MariaDB/server/commit/1bd9815479)\
  2019-03-25 11:27:29 +0200
  * [MDEV-14126](https://jira.mariadb.org/browse/MDEV-14126): Fix type mismatch
* Merge [Revision #c3a6c683e2](https://github.com/MariaDB/server/commit/c3a6c683e2) 2019-03-25 11:02:03 +0200 - Merge 10.2 into 10.3
* [Revision #72b934e3f7](https://github.com/MariaDB/server/commit/72b934e3f7)\
  2019-03-22 19:21:07 +0200
  * [MDEV-14126](https://jira.mariadb.org/browse/MDEV-14126): Detect unexpected emptying of B-tree pages
* [Revision #a4d0d6828b](https://github.com/MariaDB/server/commit/a4d0d6828b)\
  2019-03-22 19:19:34 +0200
  * [MDEV-14126](https://jira.mariadb.org/browse/MDEV-14126): Improve assertions in btr\_pcur\_store\_position()
* [Revision #b59d484696](https://github.com/MariaDB/server/commit/b59d484696)\
  2019-03-22 19:16:45 +0200
  * [MDEV-14126](https://jira.mariadb.org/browse/MDEV-14126): Remove page\_is\_root()
* [Revision #71c781bfe7](https://github.com/MariaDB/server/commit/71c781bfe7)\
  2019-03-25 10:29:25 +0200
  * [MDEV-18090](https://jira.mariadb.org/browse/MDEV-18090) Assertion failures due to virtual columns after upgrading to 10.2
* [Revision #f03f4da663](https://github.com/MariaDB/server/commit/f03f4da663)\
  2019-03-25 07:43:07 +0400
  * SEQUENCE tests for [MDEV-18892](https://jira.mariadb.org/browse/MDEV-18892) Regression in slow log and admin statements
* [Revision #dcdeb39480](https://github.com/MariaDB/server/commit/dcdeb39480)\
  2018-08-01 21:00:03 +0300
  * remove dead code
* [Revision #1d77a566ea](https://github.com/MariaDB/server/commit/1d77a566ea)\
  2018-07-23 22:31:31 +0300
  * remove dead code
* [Revision #92d1c9611e](https://github.com/MariaDB/server/commit/92d1c9611e)\
  2018-07-06 13:10:38 +0300
  * remove dead code
* [Revision #2327d4e430](https://github.com/MariaDB/server/commit/2327d4e430)\
  2018-06-20 15:49:33 +0300
  * remove unused method
* [Revision #67b601c503](https://github.com/MariaDB/server/commit/67b601c503)\
  2018-06-01 21:39:38 +0300
  * remove unused argument
* [Revision #8e9c5d1057](https://github.com/MariaDB/server/commit/8e9c5d1057)\
  2018-05-31 16:08:34 +0300
  * remove dead code
* [Revision #a07e29a0e5](https://github.com/MariaDB/server/commit/a07e29a0e5)\
  2018-05-29 23:55:57 +0300
  * cleanup TABLE\_SHARE
* [Revision #53216091dd](https://github.com/MariaDB/server/commit/53216091dd)\
  2018-05-29 19:06:15 +0300
  * remove dead code
* [Revision #a97ca9fe5b](https://github.com/MariaDB/server/commit/a97ca9fe5b)\
  2018-05-29 17:47:46 +0300
  * remove dead code
* [Revision #a523444eda](https://github.com/MariaDB/server/commit/a523444eda)\
  2018-05-28 18:39:27 +0300
  * remove dead code
* Merge [Revision #1c60f40868](https://github.com/MariaDB/server/commit/1c60f40868) 2019-03-22 14:41:36 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #f4484dfdbf](https://github.com/MariaDB/server/commit/f4484dfdbf)\
  2019-03-21 13:43:17 +0400
  * [MDEV-19008](https://jira.mariadb.org/browse/MDEV-19008) Slow EXPLAIN SELECT ... WHERE col IN (const1,const2,(subquery))
* [Revision #482710b20c](https://github.com/MariaDB/server/commit/482710b20c)\
  2019-03-21 10:14:57 +0200
  * Remove an unused variable
* Merge [Revision #5a780f2ec8](https://github.com/MariaDB/server/commit/5a780f2ec8) 2019-03-21 10:14:23 +0200 - Merge 10.2 into 10.3
* Merge [Revision #f41166133b](https://github.com/MariaDB/server/commit/f41166133b) 2019-03-20 18:37:53 +0200 - Merge 10.2 into 10.3
* [Revision #b47cec6c55](https://github.com/MariaDB/server/commit/b47cec6c55)\
  2019-03-20 18:10:23 +0200
  * [MDEV-18879](https://jira.mariadb.org/browse/MDEV-18879)/[MDEV-18972](https://jira.mariadb.org/browse/MDEV-18972) Corrupted record inserted by FOREIGN KEY operation
* Merge [Revision #117291db8b](https://github.com/MariaDB/server/commit/117291db8b) 2019-03-19 16:04:59 +0200 - Merge 10.2 into 10.3
* [Revision #26e5bff003](https://github.com/MariaDB/server/commit/26e5bff003)\
  2019-03-19 15:49:53 +0200
  * trx\_purge\_rseg\_get\_next\_history\_log(): Remove a parameter
* [Revision #cdb2208cd6](https://github.com/MariaDB/server/commit/cdb2208cd6)\
  2019-03-19 11:09:53 +0200
  * [MDEV-18966](https://jira.mariadb.org/browse/MDEV-18966) Transaction recovery may be broken after upgrade to 10.3
* [Revision #6893e9940a](https://github.com/MariaDB/server/commit/6893e9940a)\
  2019-03-19 11:09:10 +0200
  * trx\_purge\_add\_undo\_to\_history(): Non-functional cleanup
* Merge [Revision #397b6b13d0](https://github.com/MariaDB/server/commit/397b6b13d0) 2019-03-18 09:35:35 +0200 - [MDEV-18946](https://jira.mariadb.org/browse/MDEV-18946) munmap of 1 byte during shutdown is EINVAL
* [Revision #a9056a2b89](https://github.com/MariaDB/server/commit/a9056a2b89)\
  2019-03-07 18:39:20 +1100
  * [MDEV-18946](https://jira.mariadb.org/browse/MDEV-18946): innodb: {de|}allocate\_large\_{dodump|dontdump} added
* [Revision #8678a1052d](https://github.com/MariaDB/server/commit/8678a1052d)\
  2019-03-07 11:33:42 +1100
  * [MDEV-18946](https://jira.mariadb.org/browse/MDEV-18946): innodb: buffer\_pool - unallocate large pages requires size
* [Revision #4f410473ed](https://github.com/MariaDB/server/commit/4f410473ed)\
  2019-03-17 00:14:14 +0100
  * post-merge: --ps-protocol fixes
* [Revision #f38c352172](https://github.com/MariaDB/server/commit/f38c352172)\
  2019-03-16 16:03:54 +0100
  * post-merge: gcc 8 warnings
* Merge [Revision #b64fde8f38](https://github.com/MariaDB/server/commit/b64fde8f38) 2019-03-17 13:06:41 +0100 - Merge branch '10.2' into 10.3
* [Revision #a89ee3cd15](https://github.com/MariaDB/server/commit/a89ee3cd15)\
  2019-03-17 13:33:31 +0200
  * [MDEV-18952](https://jira.mariadb.org/browse/MDEV-18952) CHECK TABLE should use READ UNCOMMITED if innodb\_force\_recovery>=5
* [Revision #51e48b9f89](https://github.com/MariaDB/server/commit/51e48b9f89)\
  2018-12-24 03:21:58 -0800
  * Ignore VScode workspace
* [Revision #69b33fca8c](https://github.com/MariaDB/server/commit/69b33fca8c)\
  2019-03-12 16:02:34 +0200
  * [MDEV-18878](https://jira.mariadb.org/browse/MDEV-18878): After-merge fixes
* Merge [Revision #b32bc70e34](https://github.com/MariaDB/server/commit/b32bc70e34) 2019-03-12 14:26:34 +0200 - Merge 10.2 into 10.3
* [Revision #f010c90807](https://github.com/MariaDB/server/commit/f010c90807)\
  2019-03-11 20:03:27 +0200
  * Fixed memory leak in mysqltest
* Merge [Revision #814205f306](https://github.com/MariaDB/server/commit/814205f306) 2019-03-11 17:49:36 +0200 - Merge 10.2 into 10.3
* Merge [Revision #89b463ee99](https://github.com/MariaDB/server/commit/89b463ee99) 2019-03-08 22:00:24 +0200 - Merge 10.2 into 10.3
* [Revision #6740b2926b](https://github.com/MariaDB/server/commit/6740b2926b)\
  2019-03-08 15:04:52 +0100
  * Fix of PS after merge from 10.2.
* [Revision #94eb56fb29](https://github.com/MariaDB/server/commit/94eb56fb29)\
  2019-03-08 10:21:58 +0200
  * Give ASAN some more stack
* [Revision #136d21c82f](https://github.com/MariaDB/server/commit/136d21c82f)\
  2019-03-08 09:13:48 +0200
  * [MDEV-13818](https://jira.mariadb.org/browse/MDEV-13818): Revert an incorrect change
* Merge [Revision #2d0dd62cf7](https://github.com/MariaDB/server/commit/2d0dd62cf7) 2019-03-08 00:26:55 +0200 - Merge 10.2 into 10.3
* [Revision #d30f17af49](https://github.com/MariaDB/server/commit/d30f17af49)\
  2019-03-05 20:07:51 +0100
  * [MDEV-13818](https://jira.mariadb.org/browse/MDEV-13818) CREATE INDEX leaks memory if running out of undo log space
* [Revision #2bd204b965](https://github.com/MariaDB/server/commit/2bd204b965)\
  2019-03-06 11:41:22 +0100
  * fix memory leaks in mysql\_client\_test
* [Revision #f0cd707503](https://github.com/MariaDB/server/commit/f0cd707503)\
  2019-03-06 23:44:58 +0400
  * After-merge fix for [MDEV-18333](https://jira.mariadb.org/browse/MDEV-18333) Slow\_queries count doesn't increase when slow\_query\_log is turned off
* Merge [Revision #77103e9832](https://github.com/MariaDB/server/commit/77103e9832) 2019-03-06 16:20:13 +0200 - Merge 10.2 into 10.3
* [Revision #723ffdb32e](https://github.com/MariaDB/server/commit/723ffdb32e)\
  2019-03-05 14:11:42 +0100
  * [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519): After-merge fix for 10.3
* Merge [Revision #446b3ebdfc](https://github.com/MariaDB/server/commit/446b3ebdfc) 2019-03-05 12:56:05 +0200 - Merge 10.2 into 10.3
* [Revision #8f4de38f65](https://github.com/MariaDB/server/commit/8f4de38f65)\
  2019-03-04 23:10:30 -0800
  * [MDEV-18467](https://jira.mariadb.org/browse/MDEV-18467) Server crashes in fix\_semijoin\_strategies\_for\_picked\_join\_order
* Merge [Revision #a2fc36989e](https://github.com/MariaDB/server/commit/a2fc36989e) 2019-03-04 17:01:00 +0200 - Merge 10.2 into 10.3
* [Revision #82da98556c](https://github.com/MariaDB/server/commit/82da98556c)\
  2019-02-25 15:57:08 +0100
  * [MDEV-18605](https://jira.mariadb.org/browse/MDEV-18605): Loss of column aliases by using view and group
* [Revision #50b3632fa4](https://github.com/MariaDB/server/commit/50b3632fa4)\
  2019-02-25 21:49:04 +0100
  * [MDEV-9519](https://jira.mariadb.org/browse/MDEV-9519): Data corruption will happen on the Galera cluster size change
* [Revision #09bd213852](https://github.com/MariaDB/server/commit/09bd213852)\
  2019-02-22 21:38:55 -0800
  * [MDEV-18700](https://jira.mariadb.org/browse/MDEV-18700) EXPLAIN EXTENDED shows a wrong operation for query with UNION ALL after INTERSECT
* [Revision #4946eb7b54](https://github.com/MariaDB/server/commit/4946eb7b54)\
  2019-02-21 10:50:54 -0500
  * bump the VERSION
* Merge [Revision #a40de1bdeb](https://github.com/MariaDB/server/commit/a40de1bdeb) 2019-02-20 17:21:26 +0100 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #5296aa8b12](https://github.com/MariaDB/server/commit/5296aa8b12)\
  2019-02-20 12:25:57 +0100
  * [MDEV-18663](https://jira.mariadb.org/browse/MDEV-18663) Tests : use --core-file if mariadb-backup output is redirected to a file

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
