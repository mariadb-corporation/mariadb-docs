# MariaDB 10.3.4 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.4)[Release Notes](../../old-releases/10.3/10.3.4.md)[Changelog](mariadb-1034-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 18 Jan 2018

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.4.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Merge [Revision #8f102b584d](https://github.com/MariaDB/server/commit/8f102b584d) 2018-01-17 00:45:02 +0100 - Merge branch 'github/10.3' into bb-10.3-temporal
* [Revision #d87531a6a0](https://github.com/MariaDB/server/commit/d87531a6a0)\
  2018-01-16 14:05:06 +0200
  * Follow-up to [MDEV-14952](https://jira.mariadb.org/browse/MDEV-14952): Remove some more btr\_get\_search\_latch()
* [Revision #2281fcf38a](https://github.com/MariaDB/server/commit/2281fcf38a)\
  2018-01-16 13:42:33 +0200
  * Follow-up fix to [MDEV-14952](https://jira.mariadb.org/browse/MDEV-14952) for mariadb-backup
* [Revision #1d522353c8](https://github.com/MariaDB/server/commit/1d522353c8)\
  2018-01-12 20:32:12 +0000
  * Deb: wrap-and-sort -a the lib\* packages in debian/control
* [Revision #3862d8bc89](https://github.com/MariaDB/server/commit/3862d8bc89)\
  2018-01-12 22:56:53 +0000
  * Deb: wrap-and-sort -a
* [Revision #72768cf188](https://github.com/MariaDB/server/commit/72768cf188)\
  2018-01-12 20:27:22 +0000
  * Deb: Warn if sources contain a file that is not installed anywhere
* [Revision #b5edb4ca3a](https://github.com/MariaDB/server/commit/b5edb4ca3a)\
  2018-01-12 16:56:55 +0000
  * Deb: Add missing files into correct packages and rest in not-installed
* [Revision #dbc9cfa52b](https://github.com/MariaDB/server/commit/dbc9cfa52b)\
  2018-01-12 19:35:01 +0000
  * Deb: .manpages files should only contain man pages unique to deb packages
* [Revision #711e8c5634](https://github.com/MariaDB/server/commit/711e8c5634)\
  2018-01-12 13:06:14 +0000
  * [MDEV-12642](https://jira.mariadb.org/browse/MDEV-12642): Build deb source packages on buildbot, just not on Travis-CI
* [Revision #a41192def8](https://github.com/MariaDB/server/commit/a41192def8)\
  2018-01-11 20:27:40 +0000
  * Deb: Fix spelling etc Lintian complaints
* [Revision #ed00fd2bce](https://github.com/MariaDB/server/commit/ed00fd2bce)\
  2018-01-11 20:04:09 +0000
  * Deb: switch from usr/include/mysql to usr/include/mariadb
* [Revision #5b3bf57be2](https://github.com/MariaDB/server/commit/5b3bf57be2)\
  2018-01-11 17:58:41 +0000
  * Deb: Install missing man pages
* [Revision #be59851ad9](https://github.com/MariaDB/server/commit/be59851ad9)\
  2018-01-11 15:11:16 +0000
  * Deb: Match official Debian package libmariadb-dev-compat
* [Revision #9ef2268eda](https://github.com/MariaDB/server/commit/9ef2268eda)\
  2018-01-11 15:48:17 +0000
  * Deb: Simplify libmariadb.so.3 links
* [Revision #65db816c32](https://github.com/MariaDB/server/commit/65db816c32)\
  2018-01-11 14:59:46 +0000
  * Deb: Split libmysqlclient19/20 compat links into a separate package
* [Revision #90f1f72622](https://github.com/MariaDB/server/commit/90f1f72622)\
  2018-01-11 12:49:21 +0000
  * Deb: Add missing files to packages
* [Revision #503fcfb80f](https://github.com/MariaDB/server/commit/503fcfb80f)\
  2018-01-11 10:51:03 +0000
  * Deb: Re-remove unnecessary version suffixes from package names
* [Revision #9719fb4bef](https://github.com/MariaDB/server/commit/9719fb4bef)\
  2018-01-11 10:46:04 +0000
  * Deb: Re-rename \*.files into \*.install
* [Revision #846517d9b7](https://github.com/MariaDB/server/commit/846517d9b7)\
  2018-01-11 09:46:09 +0000
  * Deb: Recover include/mariadb wrongly removed in commit 9b10b4181f70634c
* [Revision #094938255d](https://github.com/MariaDB/server/commit/094938255d)\
  2018-01-12 12:05:30 +0000
  * Deb: sync architecture restrictions from packaging in Debian official
* [Revision #e260c6a087](https://github.com/MariaDB/server/commit/e260c6a087)\
  2018-01-12 12:04:01 +0000
  * Fix commit 9631d933fbc2ec99874 so Travis CI doesn't fail
* [Revision #da27dc995e](https://github.com/MariaDB/server/commit/da27dc995e)\
  2018-01-16 09:18:22 +0000
  * Fix Windows build
* [Revision #0664d633e4](https://github.com/MariaDB/server/commit/0664d633e4)\
  2018-01-15 19:51:09 +0200
  * [MDEV-14952](https://jira.mariadb.org/browse/MDEV-14952) Avoid repeated calls to btr\_get\_search\_latch()
* [Revision #4beb699a36](https://github.com/MariaDB/server/commit/4beb699a36)\
  2018-01-15 17:35:34 +0200
  * [MDEV-14952](https://jira.mariadb.org/browse/MDEV-14952) Avoid repeated calls to btr\_get\_search\_latch()
* [Revision #542ad0fa3f](https://github.com/MariaDB/server/commit/542ad0fa3f)\
  2018-01-15 17:58:16 +0200
  * btr\_search\_check\_guess(): Remove the parameter 'mode'
* [Revision #12f804acfa](https://github.com/MariaDB/server/commit/12f804acfa)\
  2018-01-15 18:08:59 +0200
  * [MDEV-14441](https://jira.mariadb.org/browse/MDEV-14441) Deadlock due to InnoDB adaptive hash index
* [Revision #458e33cfbc](https://github.com/MariaDB/server/commit/458e33cfbc)\
  2018-01-15 17:06:26 +0200
  * [MDEV-14441](https://jira.mariadb.org/browse/MDEV-14441) Deadlock due to InnoDB adaptive hash index
* Merge [Revision #4ef25dbfd8](https://github.com/MariaDB/server/commit/4ef25dbfd8) 2018-01-15 19:11:28 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #e2e740030d](https://github.com/MariaDB/server/commit/e2e740030d) 2018-01-15 19:07:02 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #3fdd390791](https://github.com/MariaDB/server/commit/3fdd390791)\
  2018-01-15 19:02:38 +0200
  * [MDEV-14441](https://jira.mariadb.org/browse/MDEV-14441) InnoDB hangs when setting innodb\_adaptive\_hash\_index=OFF during UPDATE
* [Revision #abbce9ed56](https://github.com/MariaDB/server/commit/abbce9ed56)\
  2017-12-22 15:03:24 +0200
  * Fixed compiler warnings in guess\_malloc\_library
* Merge [Revision #39f236a2f5](https://github.com/MariaDB/server/commit/39f236a2f5) 2018-01-15 16:41:10 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #9c6fc7b644](https://github.com/MariaDB/server/commit/9c6fc7b644)\
  2018-01-15 16:38:16 +0200
  * Fix -Wsign-compare introduced by Compilation speed (#546)
* Merge [Revision #27b6b2625e](https://github.com/MariaDB/server/commit/27b6b2625e) 2018-01-15 16:22:02 +0200 - Merge 10.1 into 10.2
* [Revision #4794e5b091](https://github.com/MariaDB/server/commit/4794e5b091)\
  2018-01-15 16:19:46 +0200
  * Fix a test that always failed on --embedded
* [Revision #85aea5a12b](https://github.com/MariaDB/server/commit/85aea5a12b)\
  2018-01-15 16:50:18 +0300
  * Update .result for rocksdb.rpl\_row\_triggers (not the whole test works yet)
* [Revision #850702da6b](https://github.com/MariaDB/server/commit/850702da6b)\
  2018-01-15 15:37:22 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Merge InnoDB test cases from MySQL 5.7 (part 6)
* [Revision #ec062c6181](https://github.com/MariaDB/server/commit/ec062c6181)\
  2018-01-15 15:26:02 +0200
  * [MDEV-12121](https://jira.mariadb.org/browse/MDEV-12121) follow-up: Unbreak the WITH\_INNODB\_AHI=OFF build
* [Revision #72136ae75c](https://github.com/MariaDB/server/commit/72136ae75c)\
  2018-01-14 19:50:45 +0300
  * Compilation speed (#546)
* [Revision #3d798be1d4](https://github.com/MariaDB/server/commit/3d798be1d4)\
  2018-01-15 10:49:03 +0200
  * [MDEV-14655](https://jira.mariadb.org/browse/MDEV-14655) Assertion \`!fts\_index' failed in prepare\_inplace\_alter\_table\_dict
* Merge [Revision #2750a02065](https://github.com/MariaDB/server/commit/2750a02065) 2018-01-13 20:37:00 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #68e5d6a941](https://github.com/MariaDB/server/commit/68e5d6a941)\
  2018-01-13 20:27:46 +0200
  * Do not truncate integers on 32-bit systems in Rows\_event\_tracker
* Merge [Revision #70fff3688d](https://github.com/MariaDB/server/commit/70fff3688d) 2018-01-13 18:25:24 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #bec2712775](https://github.com/MariaDB/server/commit/bec2712775) 2018-01-13 18:18:28 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #fc65577873](https://github.com/MariaDB/server/commit/fc65577873)\
  2018-01-13 18:04:03 +0200
  * [MDEV-14887](https://jira.mariadb.org/browse/MDEV-14887) On a 32-bit system, [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) mishandles data file sizes exceeding 4GiB
* [Revision #09ef28abd7](https://github.com/MariaDB/server/commit/09ef28abd7)\
  2018-01-13 16:38:43 +0200
  * Fixed BUILD scripts
* Merge [Revision #1eea7966f3](https://github.com/MariaDB/server/commit/1eea7966f3) 2018-01-13 01:27:35 +0300 - Merge branch 'bb-10.2-mariarocks' into 10.2
* [Revision #4cafd8e66f](https://github.com/MariaDB/server/commit/4cafd8e66f)\
  2018-01-13 01:26:06 +0300
  * rocksdb.information\_schema testcase is not stable
* [Revision #2da1917912](https://github.com/MariaDB/server/commit/2da1917912)\
  2018-01-12 16:04:29 +0000
  * Attempt to eliminate race conditions in rocksdb.information\_schema
* [Revision #028e2ddc54](https://github.com/MariaDB/server/commit/028e2ddc54)\
  2018-01-12 19:16:36 +0530
  * Added a missing result file to the rocksdb\_sys\_vars result suite
* [Revision #c481fc9ca7](https://github.com/MariaDB/server/commit/c481fc9ca7)\
  2018-01-12 15:57:08 +0300
  * Change MyRocks maturity from Alpha to Beta
* [Revision #d32f5be307](https://github.com/MariaDB/server/commit/d32f5be307)\
  2018-01-12 15:11:56 +0300
  * [MDEV-14372](https://jira.mariadb.org/browse/MDEV-14372): Fix and enable rocksdb.information\_schema test
* [Revision #0a63b50c7a](https://github.com/MariaDB/server/commit/0a63b50c7a)\
  2017-11-28 16:34:31 +0400
  * Cleanup UT\_LOW\_PRIORITY\_CPU/UT\_RESUME\_PRIORITY\_CPU
* [Revision #3dc3ab1a30](https://github.com/MariaDB/server/commit/3dc3ab1a30)\
  2018-01-11 23:56:54 +0200
  * Added checking that row events ends with a proper end block
* [Revision #5fce14dad0](https://github.com/MariaDB/server/commit/5fce14dad0)\
  2018-01-11 23:55:13 +0200
  * Removed wrong DBUG\_DUMP that accessed not initialized memory.
* [Revision #3e6fcb6ac8](https://github.com/MariaDB/server/commit/3e6fcb6ac8)\
  2018-01-12 16:44:27 +0200
  * [MDEV-14935](https://jira.mariadb.org/browse/MDEV-14935) Remove bogus conditions related to not redo-logging PAGE\_MAX\_TRX\_ID changes
* [Revision #c9c28bef3c](https://github.com/MariaDB/server/commit/c9c28bef3c)\
  2017-11-15 12:37:32 +0800
  * Minor spelling fixes in code comments, docs and output
* [Revision #21239bb0fd](https://github.com/MariaDB/server/commit/21239bb0fd)\
  2018-01-11 22:54:22 +0200
  * After-merge fix to innodb.log\_corruption
* Merge [Revision #6dd302d164](https://github.com/MariaDB/server/commit/6dd302d164) 2018-01-11 19:44:41 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #cca611d1c0](https://github.com/MariaDB/server/commit/cca611d1c0) 2018-01-11 18:00:31 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #bf7719111f](https://github.com/MariaDB/server/commit/bf7719111f)\
  2018-01-11 17:09:51 +0200
  * Removed duplicated copyright message
* [Revision #30ecd2884a](https://github.com/MariaDB/server/commit/30ecd2884a)\
  2018-01-11 12:12:31 +0200
  * Fix compilation warnings for libmariadb
* Merge [Revision #e9842de20c](https://github.com/MariaDB/server/commit/e9842de20c) 2018-01-11 12:03:23 +0200 - Merge 10.1 into 10.2
* [Revision #578ffcc5ef](https://github.com/MariaDB/server/commit/578ffcc5ef)\
  2018-01-11 10:56:13 +0200
  * Skip mariadb-backup.huge\_lsn if encryption is not available
* Merge [Revision #c15b3d2d41](https://github.com/MariaDB/server/commit/c15b3d2d41) 2018-01-11 10:44:05 +0200 - Merge 10.0 into 10.1
* Merge [Revision #4c1479545d](https://github.com/MariaDB/server/commit/4c1479545d) 2018-01-11 10:16:38 +0200 - Merge 5.5 into 10.0
* [Revision #bdcd7f79e4](https://github.com/MariaDB/server/commit/bdcd7f79e4)\
  2018-01-11 09:33:26 +0200
  * [MDEV-14916](https://jira.mariadb.org/browse/MDEV-14916) InnoDB reports warning for "Purge reached the head of the history list"
* [Revision #9c9cf556a1](https://github.com/MariaDB/server/commit/9c9cf556a1)\
  2017-10-06 17:52:35 +0200
  * [MDEV-13933](https://jira.mariadb.org/browse/MDEV-13933): Wrong results in COUNT() query with EXISTS and exists\_to\_in
* [Revision #a9c55c0059](https://github.com/MariaDB/server/commit/a9c55c0059)\
  2018-01-10 10:21:52 +0200
  * [MDEV-13814](https://jira.mariadb.org/browse/MDEV-13814) Extra logging when innodb\_log\_archive=ON
* [Revision #a408e881cf](https://github.com/MariaDB/server/commit/a408e881cf)\
  2018-01-10 09:17:43 +0200
  * [MDEV-14174](https://jira.mariadb.org/browse/MDEV-14174) crash on start with innodb-track-changed-pages
* [Revision #07aa985979](https://github.com/MariaDB/server/commit/07aa985979)\
  2018-01-09 12:37:58 +0200
  * [MDEV-14776](https://jira.mariadb.org/browse/MDEV-14776): InnoDB Monitor output generated by specific error is flooding error logs
* [Revision #cdb7a8fa69](https://github.com/MariaDB/server/commit/cdb7a8fa69)\
  2018-01-10 20:16:52 +0000
  * Silence warning coming from Windows' own header dbghelp.h
* [Revision #79fc074710](https://github.com/MariaDB/server/commit/79fc074710)\
  2018-01-10 16:43:25 +0000
  * Update CONC
* [Revision #ec97aba284](https://github.com/MariaDB/server/commit/ec97aba284)\
  2018-01-10 19:36:38 +0200
  * Fixed BUILD scripts
* [Revision #dfde5ae912](https://github.com/MariaDB/server/commit/dfde5ae912)\
  2018-01-10 13:53:44 +0200
  * [MDEV-14130](https://jira.mariadb.org/browse/MDEV-14130) InnoDB messages should not refer to the MySQL 5.7 manual
* [Revision #d1cf9b167c](https://github.com/MariaDB/server/commit/d1cf9b167c)\
  2018-01-10 13:18:02 +0200
  * [MDEV-14909](https://jira.mariadb.org/browse/MDEV-14909) [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) refuses to start up after clean shutdown of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md)
* [Revision #b132d4d749](https://github.com/MariaDB/server/commit/b132d4d749)\
  2018-01-09 22:52:01 +0000
  * Windows, compilation : Treat warning as error, if MYSQL\_MAINTAINER\_MODE is set to ERR
* [Revision #7d201d7b30](https://github.com/MariaDB/server/commit/7d201d7b30)\
  2018-01-06 09:32:47 -0800
  * Fixed [MDEV-14879](https://jira.mariadb.org/browse/MDEV-14879) Lost rows for query using recursive CTE with recursive reference in subquery
* [Revision #075f61a1d4](https://github.com/MariaDB/server/commit/075f61a1d4)\
  2018-01-09 11:30:36 +0200
  * Revert part of commit fec844aca88e1c6b9c36bb0b811e92d9d023ffb9
* Merge [Revision #5208e89807](https://github.com/MariaDB/server/commit/5208e89807) 2018-01-08 17:21:23 +0200 - Merge 10.1 into 10.2
* [Revision #18ccbf014a](https://github.com/MariaDB/server/commit/18ccbf014a)\
  2018-01-08 17:09:21 +0200
  * Make the [MDEV-14874](https://jira.mariadb.org/browse/MDEV-14874) test case more robust
* Merge [Revision #d8eef0f611](https://github.com/MariaDB/server/commit/d8eef0f611) 2018-01-08 16:45:58 +0200 - Merge 10.1 into 10.2
* Merge [Revision #29b6e809a9](https://github.com/MariaDB/server/commit/29b6e809a9) 2018-01-08 14:51:20 +0200 - Merge 10.0 into 10.1
* [Revision #c903ba2f1e](https://github.com/MariaDB/server/commit/c903ba2f1e)\
  2018-01-08 14:24:04 +0200
  * [MDEV-13205](https://jira.mariadb.org/browse/MDEV-13205) InnoDB: Failing assertion: !dict\_index\_is\_online\_ddl(index) upon ALTER TABLE
* [Revision #899c5899be](https://github.com/MariaDB/server/commit/899c5899be)\
  2018-01-08 12:58:25 +0200
  * MLOG-13101 Debug assertion failed in recv\_parse\_or\_apply\_log\_rec\_body()
* [Revision #8099941b46](https://github.com/MariaDB/server/commit/8099941b46)\
  2018-01-08 10:58:36 +0200
  * [MDEV-13487](https://jira.mariadb.org/browse/MDEV-13487) Assertion failure in rec\_get\_trx\_id()
* [Revision #ae7e1b9b13](https://github.com/MariaDB/server/commit/ae7e1b9b13)\
  2018-01-08 12:25:31 +0200
  * [MDEV-13262](https://jira.mariadb.org/browse/MDEV-13262): innodb.deadlock\_detect failed in buildbot
* Merge [Revision #9ede569260](https://github.com/MariaDB/server/commit/9ede569260) 2018-01-08 09:54:40 +0200 - Merge 10.1 into 10.2
* [Revision #16d308e21d](https://github.com/MariaDB/server/commit/16d308e21d)\
  2018-01-08 09:24:13 +0200
  * [MDEV-14874](https://jira.mariadb.org/browse/MDEV-14874) innodb\_encrypt\_log corrupts the log when the LSN crosses 32-bit boundary
* [Revision #73cf630ffc](https://github.com/MariaDB/server/commit/73cf630ffc)\
  2018-01-06 23:51:37 +0530
  * Fix Compile Error while using Flag '-DUSE\_ARIA\_FOR\_TMP\_TABLES:BOOL=OFF'
* Merge [Revision #59990747bc](https://github.com/MariaDB/server/commit/59990747bc) 2018-01-06 17:39:50 +0000 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #3a22d6c136](https://github.com/MariaDB/server/commit/3a22d6c136)\
  2018-01-05 18:22:57 +0000
  * Fix conf\_to\_src build.
* Merge [Revision #da39ca1f67](https://github.com/MariaDB/server/commit/da39ca1f67) 2018-01-06 17:39:19 +0000 - Merge branch '10.2' of [server](https://github.com/mariadb/server) into 10.2
* [Revision #15b1840f43](https://github.com/MariaDB/server/commit/15b1840f43)\
  2018-01-05 12:13:23 -0800
  * Added the test case from for [MDEV-14777](https://jira.mariadb.org/browse/MDEV-14777): Crash in [MariaDB 10.2.12](../../old-releases/10.2/10.2.12.md) on query using VIEW and WITH RECURSIVE.
* [Revision #578345305e](https://github.com/MariaDB/server/commit/578345305e)\
  2018-01-05 10:17:29 -0800
  * Added a test case for [MDEV-13454](https://jira.mariadb.org/browse/MDEV-13454): Improper error in ONLY\_FULL\_GROUP\_BY sql\_mode with condition\_pushdown\_for\_derived=on
* Merge [Revision #e6e24fe836](https://github.com/MariaDB/server/commit/e6e24fe836) 2018-01-05 16:52:25 +0000 - Merge branch '10.2' of [server](https://github.com/mariadb/server) into 10.2
* [Revision #0de565a564](https://github.com/MariaDB/server/commit/0de565a564)\
  2018-01-04 23:40:37 -0800
  * Fixed [MDEV-14852](https://jira.mariadb.org/browse/MDEV-14852) Fails to reopen temp table within standard CTE
* [Revision #b9e0945397](https://github.com/MariaDB/server/commit/b9e0945397)\
  2018-01-04 16:52:15 +0000
  * update libmariadb
* [Revision #773c3ceb57](https://github.com/MariaDB/server/commit/773c3ceb57)\
  2018-01-11 15:39:36 +0200
  * [MDEV-14824](https://jira.mariadb.org/browse/MDEV-14824) Assertion \`!trx\_is\_started(trx)' failed in innobase\_start\_trx\_and\_assign\_read\_view
* [Revision #919169e1f9](https://github.com/MariaDB/server/commit/919169e1f9)\
  2018-01-08 17:01:55 +0000
  * Fix warning
* [Revision #0ca2ea1a65](https://github.com/MariaDB/server/commit/0ca2ea1a65)\
  2017-12-20 14:59:36 +0400
  * [MDEV-14638](https://jira.mariadb.org/browse/MDEV-14638) - Replace trx\_sys\_t::rw\_trx\_set with LF\_HASH
* [Revision #380069c235](https://github.com/MariaDB/server/commit/380069c235)\
  2017-12-13 15:40:41 +0400
  * [MDEV-14638](https://jira.mariadb.org/browse/MDEV-14638) - Replace trx\_sys\_t::rw\_trx\_set with LF\_HASH
* [Revision #1a62c8a396](https://github.com/MariaDB/server/commit/1a62c8a396)\
  2018-01-10 14:41:10 +0200
  * [MDEV-14822](https://jira.mariadb.org/browse/MDEV-14822) binlog.binlog\_killed fails with wrong result
* [Revision #715a507e33](https://github.com/MariaDB/server/commit/715a507e33)\
  2018-01-14 16:03:35 +0100
  * [MDEV-14786](https://jira.mariadb.org/browse/MDEV-14786) Server crashes in Item\_cond::transform on 2nd execution of SP querying from a view
* [Revision #1ea2b2956b](https://github.com/MariaDB/server/commit/1ea2b2956b)\
  2018-01-14 12:37:55 +0100
  * Revert "[MDEV-14786](https://jira.mariadb.org/browse/MDEV-14786) Server crashes in Item\_cond::transform on 2nd execution of SP querying from a view \[fixes #436]"
* [Revision #edb6375910](https://github.com/MariaDB/server/commit/edb6375910)\
  2018-01-13 12:15:46 +0100
  * compilation warning on windows
* [Revision #2484a2e4c8](https://github.com/MariaDB/server/commit/2484a2e4c8)\
  2018-01-12 22:21:38 +0100
  * cleanup: remove include/rpl\_events.inc
* [Revision #bd87c872c0](https://github.com/MariaDB/server/commit/bd87c872c0)\
  2018-01-12 21:32:07 +0100
  * cleanup: don't generate tests with SP or PS
* [Revision #558ee2ee84](https://github.com/MariaDB/server/commit/558ee2ee84)\
  2018-01-12 14:47:33 +0100
  * fix --embedded tests
* [Revision #8ee071a22d](https://github.com/MariaDB/server/commit/8ee071a22d)\
  2018-01-11 23:04:49 +0100
  * cleanup: remove redundant check
* [Revision #826f615fc9](https://github.com/MariaDB/server/commit/826f615fc9)\
  2018-01-11 19:41:32 +0100
  * [MDEV-14788](https://jira.mariadb.org/browse/MDEV-14788) System versioning cannot be based on local timestamps, as it is now
* [Revision #6a8cf407d2](https://github.com/MariaDB/server/commit/6a8cf407d2)\
  2018-01-11 16:34:32 +0100
  * fix tests on windows
* [Revision #28bed45469](https://github.com/MariaDB/server/commit/28bed45469)\
  2018-01-11 14:52:26 +0100
  * debug: don't hide row\_start/row\_end columns for testing
* [Revision #5d3bae242c](https://github.com/MariaDB/server/commit/5d3bae242c)\
  2018-01-10 20:09:06 +0100
  * remove dead VERS\_EXPERIMENTAL code
* [Revision #376b0ea1da](https://github.com/MariaDB/server/commit/376b0ea1da)\
  2018-01-10 19:26:31 +0100
  * Revert "SQL: Backup\_query\_start\_time RAII"
* [Revision #a544f920e3](https://github.com/MariaDB/server/commit/a544f920e3)\
  2018-01-10 16:12:24 +0100
  * remove "Transaction-based system versioning is EXPERIMENTAL" warning
* [Revision #7e1738c3c4](https://github.com/MariaDB/server/commit/7e1738c3c4)\
  2018-01-10 14:05:56 +0100
  * fix debian builds
* [Revision #57fd548d10](https://github.com/MariaDB/server/commit/57fd548d10)\
  2018-01-12 22:45:35 +0300
  * SQL: uninitialized read \[#387]
* [Revision #93e8ee4ae1](https://github.com/MariaDB/server/commit/93e8ee4ae1)\
  2018-01-12 12:54:07 +0300
  * [MDEV-14923](https://jira.mariadb.org/browse/MDEV-14923) Assertion upon INSERT into locked versioned partitioned table
* [Revision #fbed4ca4f1](https://github.com/MariaDB/server/commit/fbed4ca4f1)\
  2018-01-10 22:09:09 +0300
  * [MDEV-14816](https://jira.mariadb.org/browse/MDEV-14816) Assertion `join->best_read < double(1.797...e+308L)` failed in bool greedy\_search
* [Revision #f96b1a4e39](https://github.com/MariaDB/server/commit/f96b1a4e39)\
  2018-01-10 16:44:29 +0300
  * [MDEV-14798](https://jira.mariadb.org/browse/MDEV-14798) Add, drop system versioning semantic and syntax
* [Revision #eedab70c1c](https://github.com/MariaDB/server/commit/eedab70c1c)\
  2018-01-10 12:30:27 +0300
  * [MDEV-14871](https://jira.mariadb.org/browse/MDEV-14871) Server crashes in fill\_record / fill\_record\_n\_invoke\_before\_triggers upon inserting into versioned table with trigger
* Merge [Revision #c59c1a0736](https://github.com/MariaDB/server/commit/c59c1a0736) 2018-01-10 12:36:55 +0300 - System Versioning 1.0 pre8
* [Revision #0b597d3ab2](https://github.com/MariaDB/server/commit/0b597d3ab2)\
  2018-01-09 14:50:02 +0200
  * Follow-up to [MDEV-14837](https://jira.mariadb.org/browse/MDEV-14837): Relax a too strict assertion
* [Revision #fe79ac5b0e](https://github.com/MariaDB/server/commit/fe79ac5b0e)\
  2018-01-09 13:45:39 +0200
  * [MDEV-14837](https://jira.mariadb.org/browse/MDEV-14837) Duplicate primary keys are allowed after ADD COLUMN / UPDATE
* [Revision #5a1283a4fa](https://github.com/MariaDB/server/commit/5a1283a4fa)\
  2018-01-09 13:44:43 +0200
  * Follow-up to [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288): Add --debug=d,purge diagnostics
* [Revision #c5ac1f953b](https://github.com/MariaDB/server/commit/c5ac1f953b)\
  2018-01-08 15:21:52 -0800
  * Fixed [MDEV-14880](https://jira.mariadb.org/browse/MDEV-14880): Assertion \`inj\_cond\_list.elements' failed in JOIN::inject\_best\_splitting\_cond
* [Revision #7349b9ab5e](https://github.com/MariaDB/server/commit/7349b9ab5e)\
  2018-01-07 11:45:13 +0000
  * [MDEV-14881](https://jira.mariadb.org/browse/MDEV-14881) cmake should succeed after installing libaio.
* [Revision #a603b46593](https://github.com/MariaDB/server/commit/a603b46593)\
  2018-01-07 11:37:38 +0000
  * Fix warnings
* [Revision #7a01e64c3a](https://github.com/MariaDB/server/commit/7a01e64c3a)\
  2018-01-06 22:11:42 +0000
  * Fix warnings
* Merge [Revision #fa7d85bb87](https://github.com/MariaDB/server/commit/fa7d85bb87) 2018-01-05 22:52:06 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #6d49ef49e5](https://github.com/MariaDB/server/commit/6d49ef49e5)\
  2018-01-05 22:48:09 +0200
  * Fix a -Wimplicit-fallthrough warning
* [Revision #f77fe24d2d](https://github.com/MariaDB/server/commit/f77fe24d2d)\
  2018-01-05 22:45:23 +0200
  * Fix a warning about extra parenthesis
* [Revision #23bd61a141](https://github.com/MariaDB/server/commit/23bd61a141)\
  2018-01-05 18:58:45 +0000
  * Fix warning
* [Revision #894fbe6862](https://github.com/MariaDB/server/commit/894fbe6862)\
  2018-01-05 17:11:37 +0000
  * Fix warnings
* Merge [Revision #e9a2082634](https://github.com/MariaDB/server/commit/e9a2082634) 2018-01-05 16:52:40 +0200 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* Merge [Revision #287d105398](https://github.com/MariaDB/server/commit/287d105398) 2018-01-05 12:11:58 +0200 - Merge 10.1 into 10.2
* [Revision #d9e0c06b5d](https://github.com/MariaDB/server/commit/d9e0c06b5d)\
  2017-12-21 12:04:07 +0300
  * Tests: detect table count for some encryption tests
* [Revision #9c9db1cbe2](https://github.com/MariaDB/server/commit/9c9db1cbe2)\
  2018-01-05 11:58:45 +0200
  * [MDEV-14059](https://jira.mariadb.org/browse/MDEV-14059) Work around a problem exposed by InnoDB GIS debug check
* Merge [Revision #c8e6364407](https://github.com/MariaDB/server/commit/c8e6364407) 2018-01-04 20:47:34 +0200 - Merge branch 10.1 into 10.2
* Merge [Revision #21470de148](https://github.com/MariaDB/server/commit/21470de148) 2018-01-04 20:42:29 +0200 - Merge 10.0 into 10.1
* [Revision #4496fd71f4](https://github.com/MariaDB/server/commit/4496fd71f4)\
  2018-01-04 20:38:42 +0200
  * Fix a truncation warning introduced in [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323)
* [Revision #8dc77a72ea](https://github.com/MariaDB/server/commit/8dc77a72ea)\
  2018-01-04 19:16:59 +0200
  * [MDEV-14057](https://jira.mariadb.org/browse/MDEV-14057) InnoDB GIS tests fail
* [Revision #218dbf68b8](https://github.com/MariaDB/server/commit/218dbf68b8)\
  2018-01-04 19:32:29 +0200
  * [MDEV-14058](https://jira.mariadb.org/browse/MDEV-14058) InnoDB Assertion failure !leaf on rem0rec.cc line 566 on test innodb\_gis.rtree\_recovery
* [Revision #0f253d3e64](https://github.com/MariaDB/server/commit/0f253d3e64)\
  2018-01-04 10:41:08 -0500
  * bump the VERSION
* [Revision #5e0b13d173](https://github.com/MariaDB/server/commit/5e0b13d173)\
  2018-01-04 16:21:18 +0200
  * Fixed wrong arguments to printf and related functions
* [Revision #c584a496d7](https://github.com/MariaDB/server/commit/c584a496d7)\
  2018-01-04 14:04:52 +0300
  * Fix out-of-date comments.
* [Revision #6feb74c4b2](https://github.com/MariaDB/server/commit/6feb74c4b2)\
  2018-01-05 22:50:28 +0200
  * row\_upd\_rec\_in\_place(): Relax a debug assertion
* Merge [Revision #64ab0fb721](https://github.com/MariaDB/server/commit/64ab0fb721) 2018-01-05 09:49:10 +0200 - Merge pull request #534 from tempesta-tech/upstream/test\_innodb\_encryption
* [Revision #64afa5be1c](https://github.com/MariaDB/server/commit/64afa5be1c)\
  2017-12-21 12:04:07 +0300
  * Tests: detect table count for some encryption tests
* [Revision #c9ad134e56](https://github.com/MariaDB/server/commit/c9ad134e56)\
  2018-01-04 17:59:58 +0200
  * Relax a bogus debug assertion
* Merge [Revision #145ae15a33](https://github.com/MariaDB/server/commit/145ae15a33) 2018-01-04 09:22:59 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #1a1bda2222](https://github.com/MariaDB/server/commit/1a1bda2222)\
  2018-01-03 22:43:41 +0200
  * Do not misspell "fall through"
* Merge [Revision #3fcbeb4a63](https://github.com/MariaDB/server/commit/3fcbeb4a63) 2018-01-03 22:42:27 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #af0ba43838](https://github.com/MariaDB/server/commit/af0ba43838)\
  2018-01-03 22:21:32 +0200
  * Do not misspell "fall through"
* Merge [Revision #fcde91114d](https://github.com/MariaDB/server/commit/fcde91114d) 2018-01-03 20:42:09 +0200 - Merge 10.1 into 10.2
* Merge [Revision #1e89c86dd7](https://github.com/MariaDB/server/commit/1e89c86dd7) 2018-01-03 20:41:34 +0200 - Merge 10.0 into 10.1
* Merge [Revision #8ac1982fcc](https://github.com/MariaDB/server/commit/8ac1982fcc) 2018-01-03 20:40:41 +0200 - Merge 5.5 into 10.0
* [Revision #84c9c8b2e9](https://github.com/MariaDB/server/commit/84c9c8b2e9)\
  2018-01-03 15:01:17 +0200
  * Silence some -Wimplicit-fallthrough by proper spelling
* Merge [Revision #f7fd6ace18](https://github.com/MariaDB/server/commit/f7fd6ace18) 2018-01-03 15:48:47 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #9eb3fcc9fb](https://github.com/MariaDB/server/commit/9eb3fcc9fb)\
  2018-01-03 14:30:58 +0200
  * Follow-up fix of [MDEV-14717](https://jira.mariadb.org/browse/MDEV-14717) RENAME TABLE in InnoDB is not crash-safe
* Merge [Revision #c2c2173727](https://github.com/MariaDB/server/commit/c2c2173727) 2018-01-03 02:59:32 +0200 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #16cd55a33a](https://github.com/MariaDB/server/commit/16cd55a33a)\
  2018-01-03 01:05:25 +0200
  * Fixed crashing bug in mysqlbinlog
* [Revision #14e01bd868](https://github.com/MariaDB/server/commit/14e01bd868)\
  2018-01-02 02:03:12 +0200
  * Fixed simple failures:
* Merge [Revision #fbab79c9b8](https://github.com/MariaDB/server/commit/fbab79c9b8) 2018-01-01 19:39:59 +0200 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #afbb72b3b6](https://github.com/MariaDB/server/commit/afbb72b3b6)\
  2017-12-29 13:22:34 +0200
  * Made IO\_CACHE safe for reading big blocks (> 2G)
* [Revision #e64184134a](https://github.com/MariaDB/server/commit/e64184134a)\
  2017-12-23 16:59:41 +0200
  * mysqlbinlog now prints "

## Number of rows" and stops on errors

* [Revision #acd2862e65](https://github.com/MariaDB/server/commit/acd2862e65)\
  2018-01-03 15:22:52 +0200
  * [MDEV-14848](https://jira.mariadb.org/browse/MDEV-14848) [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) refuses InnoDB crash-upgrade from [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md)
* [Revision #36ba58cb75](https://github.com/MariaDB/server/commit/36ba58cb75)\
  2018-01-03 00:12:36 +0200
  * Fixed that sequences and default works with ps-protocol
* [Revision #86cf60a615](https://github.com/MariaDB/server/commit/86cf60a615)\
  2018-01-02 14:09:16 -0800
  * Fixed [MDEV-14845](https://jira.mariadb.org/browse/MDEV-14845) Server crashes in st\_join\_table::is\_inner\_table\_of\_outer\_join
* Merge [Revision #c664c48726](https://github.com/MariaDB/server/commit/c664c48726) 2017-12-30 16:19:17 -0800 - Merge branch '10.3' into bb-10.3-igor
* [Revision #b2a102fb58](https://github.com/MariaDB/server/commit/b2a102fb58)\
  2017-11-23 13:03:23 +0200
  * Fix double floating point error in dtoa.c
* [Revision #f9f976b217](https://github.com/MariaDB/server/commit/f9f976b217)\
  2017-11-16 10:33:28 +0200
  * Fix ssl cmake configuration not checking for symbols properly
* [Revision #b443c0e056](https://github.com/MariaDB/server/commit/b443c0e056)\
  2017-11-23 19:13:12 +0200
  * Lean down compilation when running travis with rpl
* [Revision #4f0299f8b3](https://github.com/MariaDB/server/commit/4f0299f8b3)\
  2017-12-30 12:29:09 -0800
  * This is a full cost-based implementation of the optimization that employs splitting technique for equi-joins of materialized derived tables/views/CTEs. (see [MDEV-13369](https://jira.mariadb.org/browse/MDEV-13369) and [MDEV-13389](https://jira.mariadb.org/browse/MDEV-13389)).
* [Revision #7a66e0ab8f](https://github.com/MariaDB/server/commit/7a66e0ab8f)\
  2017-12-25 23:11:56 +0530
  * Typo Errors Fixed like essensially->essentially
* [Revision #8307fc9d6c](https://github.com/MariaDB/server/commit/8307fc9d6c)\
  2017-12-25 18:40:06 +0300
  * fix a data race in debug build (#523)
* [Revision #1761e38208](https://github.com/MariaDB/server/commit/1761e38208)\
  2017-12-23 09:40:52 -0500
  * bump the VERSION
* [Revision #26971c9aea](https://github.com/MariaDB/server/commit/26971c9aea)\
  2018-01-09 19:06:21 +0100
  * SQL: versioning info in INFORMATION\_SCHEMA
* [Revision #6470a9343d](https://github.com/MariaDB/server/commit/6470a9343d)\
  2018-01-09 19:34:38 +0100
  * Tests: use bigint in versioning.create,trx\_id
* [Revision #34abee2c21](https://github.com/MariaDB/server/commit/34abee2c21)\
  2018-01-10 10:33:23 +0300
  * Daemon: debug\_system\_versioning\_show, debug\_system\_versioning\_force
* [Revision #c777add74f](https://github.com/MariaDB/server/commit/c777add74f)\
  2018-01-08 20:15:42 +0100
  * Tests: inserting an explicit value into a vers column
* [Revision #b85efdc3af](https://github.com/MariaDB/server/commit/b85efdc3af)\
  2018-01-08 18:03:55 +0100
  * rename system\_time columns
* [Revision #cf1e5bef59](https://github.com/MariaDB/server/commit/cf1e5bef59)\
  2018-01-09 15:48:37 +0300
  * Cleanup: needless set\_current\_time()
* [Revision #be81b00c84](https://github.com/MariaDB/server/commit/be81b00c84)\
  2018-01-04 22:15:05 +0100
  * [MDEV-14788](https://jira.mariadb.org/browse/MDEV-14788) System versioning cannot be based on local timestamps, as it is now
* [Revision #c92bf28b5f](https://github.com/MariaDB/server/commit/c92bf28b5f)\
  2018-01-04 15:29:42 +0100
  * cleanup: don't use thd->set\_current\_time() directly
* [Revision #d20d7a92c0](https://github.com/MariaDB/server/commit/d20d7a92c0)\
  2018-01-03 21:10:41 +0100
  * make versioning plugin more clearly a test-only thing
* [Revision #07b1a77430](https://github.com/MariaDB/server/commit/07b1a77430)\
  2018-01-09 15:28:08 +0300
  * SQL: Backup\_query\_start\_time RAII
* [Revision #3395ab7324](https://github.com/MariaDB/server/commit/3395ab7324)\
  2018-01-03 19:12:48 +0100
  * small cleanup: backup\_query\_start\_time()
* [Revision #e52a237fe9](https://github.com/MariaDB/server/commit/e52a237fe9)\
  2018-01-03 18:51:24 +0100
  * remove ifdefs around PSI\_THREAD\_CALL
* [Revision #e577b5667a](https://github.com/MariaDB/server/commit/e577b5667a)\
  2018-01-03 17:19:39 +0100
  * fix compilation w/o P\_S
* [Revision #ca4dbcff69](https://github.com/MariaDB/server/commit/ca4dbcff69)\
  2018-01-02 22:04:10 +0100
  * Tests: system columns _not_ being auto-renamed (create, alter)
* [Revision #35b679b924](https://github.com/MariaDB/server/commit/35b679b924)\
  2017-12-30 22:34:58 +0100
  * SQL: error messages
* [Revision #e6a7457653](https://github.com/MariaDB/server/commit/e6a7457653)\
  2017-12-30 13:40:36 +0100
  * SQL: derived, hiding, error messages
* [Revision #b06b5c3eab](https://github.com/MariaDB/server/commit/b06b5c3eab)\
  2017-12-29 15:28:59 +0100
  * Tests: disabled cte.test
* [Revision #1a0b986e78](https://github.com/MariaDB/server/commit/1a0b986e78)\
  2017-12-27 15:16:17 +0100
  * [MDEV-14764](https://jira.mariadb.org/browse/MDEV-14764) Confusing error message: Table `t1` must have at least one temporal column
* [Revision #5dddbafa4e](https://github.com/MariaDB/server/commit/5dddbafa4e)\
  2018-01-08 13:32:02 +0300
  * [MDEV-14821](https://jira.mariadb.org/browse/MDEV-14821) Assertion `!is_set() || (m_status == DA_OK_BULK && is_bulk_op())` failed in Diagnostics\_area::set\_ok\_status
* [Revision #912769b7dc](https://github.com/MariaDB/server/commit/912769b7dc)\
  2018-01-06 11:56:38 +0300
  * SQL: lower priority of warning in vers\_part\_rotate() for ALTER \[fixes #446]
* [Revision #daf883f95c](https://github.com/MariaDB/server/commit/daf883f95c)\
  2018-01-03 19:47:01 +0300
  * [MDEV-14817](https://jira.mariadb.org/browse/MDEV-14817) Server crashes in prep\_alter\_part\_table() after table lock and multiple add partition \[fixes #440]
* [Revision #dbf21ff396](https://github.com/MariaDB/server/commit/dbf21ff396)\
  2018-01-03 15:51:23 +0300
  * [MDEV-14787](https://jira.mariadb.org/browse/MDEV-14787) CREATE does not allow tables with versioning columns only, but ALTER does
* [Revision #b8b5d8d87d](https://github.com/MariaDB/server/commit/b8b5d8d87d)\
  2018-01-02 15:28:50 +0300
  * [MDEV-14828](https://jira.mariadb.org/browse/MDEV-14828) Server crashes in JOIN::prepare / setup\_fields on 2nd execution of PS \[fixes #437]
* [Revision #8efca72f4a](https://github.com/MariaDB/server/commit/8efca72f4a)\
  2018-01-01 13:41:50 +0300
  * [MDEV-14792](https://jira.mariadb.org/browse/MDEV-14792) INSERT without column list into table with explicit versioning columns produces bad data
* [Revision #157150cfcf](https://github.com/MariaDB/server/commit/157150cfcf)\
  2017-12-29 16:28:13 +0300
  * [MDEV-14769](https://jira.mariadb.org/browse/MDEV-14769) Temporary table can be altered into system versioning + system\_versioning\_alter\_history has no effect
* [Revision #7069071d7d](https://github.com/MariaDB/server/commit/7069071d7d)\
  2017-12-29 12:28:37 +0300
  * [MDEV-14786](https://jira.mariadb.org/browse/MDEV-14786) Server crashes in Item\_cond::transform on 2nd execution of SP querying from a view \[fixes #436]
* [Revision #19f0b512a9](https://github.com/MariaDB/server/commit/19f0b512a9)\
  2017-12-28 10:42:42 +0300
  * Tests: record mariadb-backup.system\_versioning \[#387]
* [Revision #2a3c66a636](https://github.com/MariaDB/server/commit/2a3c66a636)\
  2017-12-28 10:40:00 +0300
  * IB: move methods to proper place
* [Revision #d72462a29b](https://github.com/MariaDB/server/commit/d72462a29b)\
  2017-12-27 16:41:43 +0300
  * SQL: TRX\_ID to TIMESTAMP versioning switch \[fixes #428]
* [Revision #d1e4c5d13e](https://github.com/MariaDB/server/commit/d1e4c5d13e)\
  2017-12-27 15:25:40 +0300
  * [MDEV-14748](https://jira.mariadb.org/browse/MDEV-14748) Assertion in ha\_myisammrg::attach\_children() \[fixes #434]
* [Revision #9daf583ab6](https://github.com/MariaDB/server/commit/9daf583ab6)\
  2017-12-24 01:48:21 +0100
  * fix CREATE ... SELECT
* [Revision #1a06a48230](https://github.com/MariaDB/server/commit/1a06a48230)\
  2017-12-23 12:23:04 +0100
  * Tests: ER\_VERS\_DUPLICATE\_ROW\_START\_END check
* [Revision #759843ae60](https://github.com/MariaDB/server/commit/759843ae60)\
  2017-12-23 12:07:54 +0100
  * dead code prev\_insert\_id()
* [Revision #0fe67f2ef9](https://github.com/MariaDB/server/commit/0fe67f2ef9)\
  2017-12-26 17:16:50 +0300
  * [MDEV-14744](https://jira.mariadb.org/browse/MDEV-14744) Assertion \`table->versioned() == m\_prebuilt->table->versioned()' failed in ha\_innobase::open
* [Revision #04451f0f8a](https://github.com/MariaDB/server/commit/04451f0f8a)\
  2017-12-26 14:58:02 +0300
  * [MDEV-14765](https://jira.mariadb.org/browse/MDEV-14765) Server crashes in Sys\_var\_vers\_asof::update
* [Revision #11c6882741](https://github.com/MariaDB/server/commit/11c6882741)\
  2017-12-25 18:17:55 +0300
  * [MDEV-14747](https://jira.mariadb.org/browse/MDEV-14747) ALTER PARTITION BY SYSTEM\_TIME after LOCK TABLES
* [Revision #4236f589b6](https://github.com/MariaDB/server/commit/4236f589b6)\
  2017-12-25 16:40:11 +0300
  * [MDEV-14751](https://jira.mariadb.org/browse/MDEV-14751) Server crashes in TABLE::versioned on 2nd execution of SP \[fixes #431]
* [Revision #b9bc8bbdc0](https://github.com/MariaDB/server/commit/b9bc8bbdc0)\
  2017-12-25 13:40:38 +0300
  * SQL: SP forced invalidate via 0
* [Revision #d8aabb44b5](https://github.com/MariaDB/server/commit/d8aabb44b5)\
  2017-12-25 13:38:03 +0300
  * SQL: prohibit ALTER ... AS ROW START|END \[fixes #429]
* [Revision #ea49441c41](https://github.com/MariaDB/server/commit/ea49441c41)\
  2017-12-22 16:39:28 +0300
  * Partition: uninitialized vers\_info fix
* [Revision #9cbf9e3b92](https://github.com/MariaDB/server/commit/9cbf9e3b92)\
  2017-12-22 16:33:24 +0300
  * Tests: rocksdb.misc \[#387]
* [Revision #57f827cdd6](https://github.com/MariaDB/server/commit/57f827cdd6)\
  2017-12-22 14:50:07 +0300
  * [MDEV-14741](https://jira.mariadb.org/browse/MDEV-14741) Assertion '(trx)->start\_file == 0' failed in row\_truncate\_table\_for\_mysql()
* [Revision #7f1777af88](https://github.com/MariaDB/server/commit/7f1777af88)\
  2017-12-22 14:31:04 +0300
  * SQL: DELETE HISTORY error message in prepared statements \[#387]
* [Revision #098a1d7ddb](https://github.com/MariaDB/server/commit/098a1d7ddb)\
  2017-12-22 13:32:00 +0300
  * [MDEV-14632](https://jira.mariadb.org/browse/MDEV-14632) Assertion \`!((new\_col->prtype ^ col->prtype) & 256U)' failed in row\_log\_table\_apply\_convert\_mrec
* [Revision #1e8eae40ce](https://github.com/MariaDB/server/commit/1e8eae40ce)\
  2017-12-22 12:50:44 +0300
  * [MDEV-14740](https://jira.mariadb.org/browse/MDEV-14740) Locking assertion for system\_time partitioning
* [Revision #d6b68b0e8d](https://github.com/MariaDB/server/commit/d6b68b0e8d)\
  2017-12-21 21:15:20 +0300
  * Tests: mariadb-backup.system\_versioning \[#387]
* [Revision #e6c5eb5c58](https://github.com/MariaDB/server/commit/e6c5eb5c58)\
  2017-12-21 18:24:58 +0300
  * [MDEV-14730](https://jira.mariadb.org/browse/MDEV-14730) Assertion \`m\_lock\_type == 2' failed in handler::ha\_close
* [Revision #7e39f70044](https://github.com/MariaDB/server/commit/7e39f70044)\
  2017-12-21 16:15:56 +0300
  * [MDEV-14722](https://jira.mariadb.org/browse/MDEV-14722) Partition: assertion in ha\_commit\_trans() for sub-statement
* [Revision #368ad5ec36](https://github.com/MariaDB/server/commit/368ad5ec36)\
  2017-12-21 11:43:09 +0100
  * compiler warning
* [Revision #c968a7ebfd](https://github.com/MariaDB/server/commit/c968a7ebfd)\
  2017-12-11 20:26:21 +0100
  * Fix tests
* [Revision #64749432ef](https://github.com/MariaDB/server/commit/64749432ef)\
  2017-12-21 11:39:24 +0100
  * Revert "[MDEV-14681](https://jira.mariadb.org/browse/MDEV-14681) Bogus ER\_UNSUPPORTED\_EXTENSION", fix differently
* [Revision #e65a695f28](https://github.com/MariaDB/server/commit/e65a695f28)\
  2017-12-21 15:02:51 +0300
  * Tests: disabled embedded for versioning.trx\_id \[#387]
* [Revision #aa4d1bedfc](https://github.com/MariaDB/server/commit/aa4d1bedfc)\
  2017-12-21 14:59:46 +0300
  * [MDEV-14689](https://jira.mariadb.org/browse/MDEV-14689) Server crashes in find\_field\_in\_tables on 2nd execution of PS with versioned table and view
* [Revision #6dc75b5f89](https://github.com/MariaDB/server/commit/6dc75b5f89)\
  2017-12-21 14:59:18 +0300
  * [MDEV-14632](https://jira.mariadb.org/browse/MDEV-14632) Assertion \`!((new\_col->prtype ^ col->prtype) & 256U)' failed in row\_log\_table\_apply\_convert\_mrec
* [Revision #7880dc65f5](https://github.com/MariaDB/server/commit/7880dc65f5)\
  2017-12-21 12:04:07 +0300
  * Tests: detect table count for some encryption tests
* [Revision #ba3e689c4d](https://github.com/MariaDB/server/commit/ba3e689c4d)\
  2017-12-21 11:52:39 +0300
  * Tests: full test results \[#387]
* [Revision #fbbdd44f72](https://github.com/MariaDB/server/commit/fbbdd44f72)\
  2017-12-21 11:49:48 +0300
  * Tests: removed --transaction-registry option \[#387]
* Merge [Revision #5c0a19c873](https://github.com/MariaDB/server/commit/5c0a19c873) 2017-12-21 11:16:42 +0300 - System Versioning 1.0 pre7
* [Revision #5c760d952b](https://github.com/MariaDB/server/commit/5c760d952b)\
  2017-12-21 10:48:48 +0300
  * Parser: default SYSTEM\_TIME ALL for DELETE HISTORY
* [Revision #36888cc531](https://github.com/MariaDB/server/commit/36888cc531)\
  2017-12-21 10:23:56 +0300
  * [MDEV-14686](https://jira.mariadb.org/browse/MDEV-14686) Server crashes in Item\_field::used\_tables on 2nd call of SP \[fixes #422]
* [Revision #a04a283469](https://github.com/MariaDB/server/commit/a04a283469)\
  2017-12-21 10:14:25 +0300
  * [MDEV-14692](https://jira.mariadb.org/browse/MDEV-14692) Server crash in MDL\_ticket::has\_stronger\_or\_equal\_type
* [Revision #acdfacee75](https://github.com/MariaDB/server/commit/acdfacee75)\
  2017-12-20 22:46:28 +0300
  * IB: TRT is not updated on ADD SYSTEM VERSIONING \[fixes #413]
* [Revision #6e530d4df5](https://github.com/MariaDB/server/commit/6e530d4df5)\
  2017-12-20 21:04:22 +0300
  * [MDEV-14685](https://jira.mariadb.org/browse/MDEV-14685) Assertion \`!fully || (bool) hist\_part' failed in Vers\_part\_info::initialized
* [Revision #4bc268d406](https://github.com/MariaDB/server/commit/4bc268d406)\
  2017-12-20 19:42:15 +0300
  * [MDEV-14632](https://jira.mariadb.org/browse/MDEV-14632) Assertion \`!((new\_col->prtype ^ col->prtype) & 256U)' failed in row\_log\_table\_apply\_convert\_mrec
* [Revision #b13f1cc59a](https://github.com/MariaDB/server/commit/b13f1cc59a)\
  2017-12-20 16:41:42 +0300
  * [MDEV-14681](https://jira.mariadb.org/browse/MDEV-14681) Bogus ER\_UNSUPPORTED\_EXTENSION
* [Revision #7eff2080fd](https://github.com/MariaDB/server/commit/7eff2080fd)\
  2017-12-20 16:12:32 +0300
  * [MDEV-14687](https://jira.mariadb.org/browse/MDEV-14687) DELETE HISTORY in prepared stmt crash \[fixes #421]
* [Revision #c5d0c38efc](https://github.com/MariaDB/server/commit/c5d0c38efc)\
  2017-12-19 22:05:25 +0300
  * [MDEV-14676](https://jira.mariadb.org/browse/MDEV-14676) Redundancy in error codes
* [Revision #fc21529f14](https://github.com/MariaDB/server/commit/fc21529f14)\
  2017-12-19 21:54:07 +0300
  * [MDEV-14683](https://jira.mariadb.org/browse/MDEV-14683) Possible redundancy in error codes
* [Revision #617e108fb6](https://github.com/MariaDB/server/commit/617e108fb6)\
  2017-12-16 21:33:43 +0100
  * s/TRUNCATE ... TO/DELETE HISTORY FROM ... BEFORE/
* [Revision #ee68d019d1](https://github.com/MariaDB/server/commit/ee68d019d1)\
  2017-12-19 16:12:56 +0300
  * SQL: removed VERS\_HIDDEN\_FLAG \[closes #409]
* [Revision #8ba06032ae](https://github.com/MariaDB/server/commit/8ba06032ae)\
  2017-12-19 15:12:11 +0300
  * [MDEV-14684](https://jira.mariadb.org/browse/MDEV-14684) Assertion \`table' failed in mysql\_delete
* [Revision #04bed58acf](https://github.com/MariaDB/server/commit/04bed58acf)\
  2017-12-18 21:36:38 +0300
  * SQL: partitioning CREATE, ALTER fixes
* [Revision #b0d9dc43ca](https://github.com/MariaDB/server/commit/b0d9dc43ca)\
  2017-12-18 21:18:19 +0300
  * SQL: system\_versioning\_transaction\_registry default OFF
* [Revision #db13dbc71d](https://github.com/MariaDB/server/commit/db13dbc71d)\
  2017-12-18 21:01:44 +0300
  * IB: compiler error fix for max signatures
* [Revision #82379ce14d](https://github.com/MariaDB/server/commit/82379ce14d)\
  2017-12-18 19:11:14 +0300
  * SQL: error messages revised
* [Revision #b55a149194](https://github.com/MariaDB/server/commit/b55a149194)\
  2017-12-18 19:03:51 +0300
  * Timestamp-based versioning for InnoDB \[closes #209]
* [Revision #d5e37621cf](https://github.com/MariaDB/server/commit/d5e37621cf)\
  2017-12-17 12:29:01 +0300
  * Scripts: VTMD\_TEMPLATE removed \[#286]
* [Revision #62b44b0efa](https://github.com/MariaDB/server/commit/62b44b0efa)\
  2017-12-17 12:10:19 +0300
  * Tests: innodb\_encryption detect table count
* [Revision #656d6f399e](https://github.com/MariaDB/server/commit/656d6f399e)\
  2017-12-15 23:33:03 +0300
  * SQL: missing stmt\_arena \[#387]
* [Revision #9b55cc73f1](https://github.com/MariaDB/server/commit/9b55cc73f1)\
  2017-12-15 20:37:36 +0300
  * SQL, IB: unversioned fields with ALTER TABLE \[fixes #401]
* Merge [Revision #4624e565f3](https://github.com/MariaDB/server/commit/4624e565f3) 2017-12-15 18:12:18 +0300 - System Versioning 1.0 pre6
* [Revision #84e14bff4a](https://github.com/MariaDB/server/commit/84e14bff4a)\
  2017-12-14 20:18:53 +0100
  * privilege: s/delete versioning rows/delete history/
* [Revision #18405e5fd9](https://github.com/MariaDB/server/commit/18405e5fd9)\
  2017-12-14 18:35:12 +0100
  * Partitioning syntax for versioning
* [Revision #f149013393](https://github.com/MariaDB/server/commit/f149013393)\
  2017-12-11 20:26:21 +0100
  * rename versioning\_\* variables
* [Revision #ca6454bcfe](https://github.com/MariaDB/server/commit/ca6454bcfe)\
  2017-12-11 14:09:58 +0100
  * for now, remove FOR SYSTEM\_TIME at the end of the query
* [Revision #a1141e226d](https://github.com/MariaDB/server/commit/a1141e226d)\
  2017-12-08 16:29:16 +0100
  * fix nullable autoinc test w/o versioning
* [Revision #e77080c7d5](https://github.com/MariaDB/server/commit/e77080c7d5)\
  2017-12-07 14:47:58 +0100
  * if a table is partitioned by system\_time, its partitions are not versioned
* [Revision #21d0a9fe3b](https://github.com/MariaDB/server/commit/21d0a9fe3b)\
  2017-12-06 20:02:26 +0100
  * yet another error message fix
* [Revision #70d7672377](https://github.com/MariaDB/server/commit/70d7672377)\
  2017-12-15 16:41:49 +0300
  * SQL: [MDEV-14633](https://jira.mariadb.org/browse/MDEV-14633) Assertion on TRT read \[fixes #406]
* [Revision #0e0f1126e6](https://github.com/MariaDB/server/commit/0e0f1126e6)\
  2017-12-15 16:35:53 +0300
  * [MDEV-14649](https://jira.mariadb.org/browse/MDEV-14649) Assertion \`t->mysql\_col\_len == 8' failed in row\_insert\_for\_mysql
* Merge [Revision #73606a3977](https://github.com/MariaDB/server/commit/73606a3977) 2017-12-15 15:01:13 +0300 - System Versioning 1.0 pre5 \[closes #407]
* [Revision #2ae2876a6c](https://github.com/MariaDB/server/commit/2ae2876a6c)\
  2017-12-14 21:16:31 +0300
  * [MDEV-14652](https://jira.mariadb.org/browse/MDEV-14652) NATURAL JOIN crash in mark\_common\_columns() \[fixes #405]
* [Revision #4be2173e0f](https://github.com/MariaDB/server/commit/4be2173e0f)\
  2017-12-14 20:06:03 +0300
  * SQL: uninitialized read \[#387]
* [Revision #27187443ef](https://github.com/MariaDB/server/commit/27187443ef)\
  2017-12-14 19:41:28 +0300
  * [MDEV-14650](https://jira.mariadb.org/browse/MDEV-14650) Assertion 0 failed in TABLE::vers\_update\_fields \[fixes #402]
* [Revision #ab5ec0f346](https://github.com/MariaDB/server/commit/ab5ec0f346)\
  2017-12-14 19:11:02 +0300
  * SQL: disable truncate history on partitioned \[fixes #399]
* [Revision #f96815fe97](https://github.com/MariaDB/server/commit/f96815fe97)\
  2017-12-14 18:40:57 +0300
  * SQL: unit resolution Item\_field not yet accessible \[fixes #398]
* [Revision #1668efb722](https://github.com/MariaDB/server/commit/1668efb722)\
  2017-12-14 18:14:21 +0300
  * [MDEV-14645](https://jira.mariadb.org/browse/MDEV-14645): AS OF TIMESTAMP is misused as TRX\_ID \[fixes #396]
* Merge [Revision #765569602d](https://github.com/MariaDB/server/commit/765569602d) 2017-12-14 16:01:05 +0300 - System Versioning 1.0 pre4
* [Revision #5d5ae2f4fe](https://github.com/MariaDB/server/commit/5d5ae2f4fe)\
  2017-12-14 15:50:02 +0300
  * Tests: fix encryption.debug\_key\_management \[#387]
* [Revision #f14f04838b](https://github.com/MariaDB/server/commit/f14f04838b)\
  2017-12-14 15:38:52 +0300
  * Tests: fix encryption.encrypt\_and\_grep \[#387]
* [Revision #2e3b580ba4](https://github.com/MariaDB/server/commit/2e3b580ba4)\
  2017-12-14 13:43:37 +0300
  * SQL: inner/outer system\_time consistency \[fixes #384]
* [Revision #eab471260b](https://github.com/MariaDB/server/commit/eab471260b)\
  2017-12-13 23:51:30 +0300
  * Paritioning: better error for disabled IB engine
* [Revision #8e8363bb75](https://github.com/MariaDB/server/commit/8e8363bb75)\
  2017-12-13 18:03:38 +0300
  * SQL: VIEW system fields propagation removed \[fixes #393]
* [Revision #a83fcbaa3b](https://github.com/MariaDB/server/commit/a83fcbaa3b)\
  2017-12-13 17:58:36 +0300
  * [MDEV-14632](https://jira.mariadb.org/browse/MDEV-14632) Assertion \`!((new\_col->prtype ^ col->prtype) & 256U)' failed in row\_log\_table\_apply\_convert\_mrec
* [Revision #bc4a86699d](https://github.com/MariaDB/server/commit/bc4a86699d)\
  2017-12-13 15:31:46 +0300
  * SQL: recursive CTE inner derived vers\_conditions \[fix #385]
* [Revision #22f45062de](https://github.com/MariaDB/server/commit/22f45062de)\
  2017-12-13 12:14:34 +0300
  * Cleanup: unwrapped large block in vers\_setup\_conds()
* [Revision #717f274b87](https://github.com/MariaDB/server/commit/717f274b87)\
  2017-12-12 22:33:49 +0300
  * [MDEV-14631](https://jira.mariadb.org/browse/MDEV-14631) Assertion \`!sys\_trx\_start && !sys\_trx\_end' failed in crete\_tmp\_table
* [Revision #c66a20b494](https://github.com/MariaDB/server/commit/c66a20b494)\
  2017-12-12 22:01:39 +0300
  * SQL: better check for partition engine \[#366]
* [Revision #74cc9ec142](https://github.com/MariaDB/server/commit/74cc9ec142)\
  2017-12-12 21:40:13 +0300
  * Tests: regenerate funcs\_1.is\_columns\_mysql\_embedded \[#387]
* [Revision #459f40a232](https://github.com/MariaDB/server/commit/459f40a232)\
  2017-12-12 21:30:49 +0300
  * SQL: create..select revisited \[closes #370]
* [Revision #a0e137c4a9](https://github.com/MariaDB/server/commit/a0e137c4a9)\
  2017-12-12 20:27:47 +0300
  * SQL: RIGHT JOIN in derived \[fix #383]
* [Revision #cb4657e3b4](https://github.com/MariaDB/server/commit/cb4657e3b4)\
  2017-12-12 14:56:28 +0300
  * [MDEV-14627](https://jira.mariadb.org/browse/MDEV-14627) SQL: disallow ADD SYSTEM VERSIONING for system-versioned tables
* [Revision #9c718de2ed](https://github.com/MariaDB/server/commit/9c718de2ed)\
  2017-12-12 01:04:07 +0300
  * Tests: versioning.derived fix for buildbot
* Merge [Revision #79dd77e6ae](https://github.com/MariaDB/server/commit/79dd77e6ae) 2017-12-11 15:43:41 +0300 - System Versioning 1.0 pre3
* [Revision #b7cd182896](https://github.com/MariaDB/server/commit/b7cd182896)\
  2017-12-10 23:52:51 +0300
  * SQL: DEFAULT value for system fields \[closes #376]
* [Revision #2968543f8d](https://github.com/MariaDB/server/commit/2968543f8d)\
  2017-12-08 16:03:50 +0300
  * IB: NULL instead of autodecrement \[closes #373]
* [Revision #947aa0bab9](https://github.com/MariaDB/server/commit/947aa0bab9)\
  2017-12-08 12:57:07 +0300
  * SQL: vers\_setup\_select() misc refactoring
* [Revision #37adb4c066](https://github.com/MariaDB/server/commit/37adb4c066)\
  2017-12-07 16:52:05 +0300
  * SQL: vers\_update\_user\_fields() mem\_root fix \[#365 bug 12]
* [Revision #ad51d77f79](https://github.com/MariaDB/server/commit/ad51d77f79)\
  2017-12-06 22:34:56 +0300
  * SQL: WHERE top level item \[#365 bug 11]
* [Revision #8c9c302016](https://github.com/MariaDB/server/commit/8c9c302016)\
  2017-12-06 15:54:00 +0300
  * SQL: fix implicit sys fields for implicit engine of partitioned table \[#366]
* [Revision #03b54a6b8a](https://github.com/MariaDB/server/commit/03b54a6b8a)\
  2017-12-06 14:45:54 +0300
  * SQL: table with duplicate ROW START/END columns \[fixes #369]
* [Revision #84b718ae70](https://github.com/MariaDB/server/commit/84b718ae70)\
  2017-12-06 06:14:22 +0300
  * SQL: derived SYSTEM\_TIME clash detection \[closes #371]
* [Revision #d04063c5b9](https://github.com/MariaDB/server/commit/d04063c5b9)\
  2017-11-28 14:52:49 +0100
  * SQL: revert unnecessary change
* [Revision #b3fe45bcd4](https://github.com/MariaDB/server/commit/b3fe45bcd4)\
  2017-12-04 18:41:07 +0100
  * rephrase error messages, fix quoting
* [Revision #903be4e6be](https://github.com/MariaDB/server/commit/903be4e6be)\
  2017-12-04 16:49:51 +0100
  * remove my\_error\_as and one unnecessary error message
* [Revision #f4270fc544](https://github.com/MariaDB/server/commit/f4270fc544)\
  2017-12-04 17:07:10 +0100
  * s/Delete\_versioning\_rows\_priv/Truncate\_versioning\_priv/
* [Revision #ea1ccfa500](https://github.com/MariaDB/server/commit/ea1ccfa500)\
  2017-12-02 16:23:16 +0100
  * SQL: regression fix: make NOW a valid identifier again \[#363]
* [Revision #d3845132fc](https://github.com/MariaDB/server/commit/d3845132fc)\
  2017-12-01 09:09:37 +0100
  * remove 'vers\_auto\_decrement'
* [Revision #6a7911d4c8](https://github.com/MariaDB/server/commit/6a7911d4c8)\
  2017-11-30 17:21:12 +0100
  * has\_vers\_fields should be calculated per table, not globally
* [Revision #9d2f1ddee7](https://github.com/MariaDB/server/commit/9d2f1ddee7)\
  2017-11-30 16:20:44 +0100
  * remove BOOL
* [Revision #a46f585aa7](https://github.com/MariaDB/server/commit/a46f585aa7)\
  2017-11-30 16:10:35 +0100
  * restore Field::get\_timestamp() prototype
* [Revision #30841c0382](https://github.com/MariaDB/server/commit/30841c0382)\
  2017-11-30 15:20:55 +0100
  * Revert "Parser: no implicit NOT NULL for system fields \[fixes #163]"
* [Revision #e60da371d1](https://github.com/MariaDB/server/commit/e60da371d1)\
  2017-11-30 13:42:11 +0100
  * fix versioning tests not to fail w/o innodb
* [Revision #8dd84ec7f3](https://github.com/MariaDB/server/commit/8dd84ec7f3)\
  2017-06-05 20:30:33 +0200
  * versioning/common.inc must "have\_innodb"
* [Revision #69e4062cc7](https://github.com/MariaDB/server/commit/69e4062cc7)\
  2017-11-30 10:37:49 +0100
  * Remove capture\_warnings.sh and print\_warnings.cmake
* [Revision #3198bc839d](https://github.com/MariaDB/server/commit/3198bc839d)\
  2017-11-28 16:38:58 +0100
  * Parser: unreserve keywords
* [Revision #6ac773421f](https://github.com/MariaDB/server/commit/6ac773421f)\
  2017-12-05 12:21:25 +0300
  * SQL: WHERE cond freed prematurely for PS \[#365 bug 10]
* [Revision #3d88a72f76](https://github.com/MariaDB/server/commit/3d88a72f76)\
  2017-12-05 03:25:34 +0300
  * SQL: fix subquery not a derived table \[#365 bug 9]
* [Revision #56adced376](https://github.com/MariaDB/server/commit/56adced376)\
  2017-12-04 12:36:07 +0300
  * SQL,IB: REPLACE semantics \[#365 bug 8]
* [Revision #f489865558](https://github.com/MariaDB/server/commit/f489865558)\
  2017-11-30 17:10:43 +0200
  * SQL: Clarify a FIXME comment on TR\_table in ha\_commit\_trans()
* [Revision #92d6bd7208](https://github.com/MariaDB/server/commit/92d6bd7208)\
  2017-11-29 15:43:48 +0200
  * Minor InnoDB cleanup (follow-up to #337)
* [Revision #5bf14f93a4](https://github.com/MariaDB/server/commit/5bf14f93a4)\
  2017-12-04 00:07:33 +0300
  * Tests: fix combinations
* [Revision #68e160fb25](https://github.com/MariaDB/server/commit/68e160fb25)\
  2017-12-03 23:06:24 +0300
  * Tests: removed common.inc from results
* [Revision #ce78bafe7a](https://github.com/MariaDB/server/commit/ce78bafe7a)\
  2017-12-03 21:25:07 +0300
  * MTR: MTR\_COMBINATIONS envvar for tests
* [Revision #36c0bec2c7](https://github.com/MariaDB/server/commit/36c0bec2c7)\
  2017-12-03 17:57:32 +0300
  * IB: remove alloc on update
* [Revision #70b82f641c](https://github.com/MariaDB/server/commit/70b82f641c)\
  2017-12-02 19:52:26 +0300
  * SQL: duplicate of historical row fix \[#365 bug 7]
* [Revision #a3802ecb58](https://github.com/MariaDB/server/commit/a3802ecb58)\
  2017-12-02 12:54:32 +0300
  * IB: assertion failure on delete with foreign \[#366]
* [Revision #5c820a7125](https://github.com/MariaDB/server/commit/5c820a7125)\
  2017-12-01 10:08:57 +0300
  * SQL: create\_like\_table strip versioning for tmp tables \[#365 bug 6]
* [Revision #b9225bb52c](https://github.com/MariaDB/server/commit/b9225bb52c)\
  2017-11-30 23:23:15 +0300
  * SQL: outdated select\_lex->where fix \[#365 bug 5]
* [Revision #e4b86780ae](https://github.com/MariaDB/server/commit/e4b86780ae)\
  2017-11-30 07:56:52 +0300
  * SQL: optimized transformer fix \[#365 bug 4]
* [Revision #2305666a05](https://github.com/MariaDB/server/commit/2305666a05)\
  2017-11-29 11:57:52 +0300
  * SQL: insert delayed fix \[#365 bug 3]
* [Revision #8d548f8e86](https://github.com/MariaDB/server/commit/8d548f8e86)\
  2017-11-28 22:56:01 +0300
  * SQL: fill\_record() field-value inconsistency fix \[#365 bug 2]
* [Revision #47ea526efa](https://github.com/MariaDB/server/commit/47ea526efa)\
  2017-11-28 21:40:27 +0300
  * IB: get template with virtual columns \[#365 bug 1]
* [Revision #f924a94d2f](https://github.com/MariaDB/server/commit/f924a94d2f)\
  2017-11-28 18:12:18 +0300
  * SQL: disable versioned DML for transaction\_registry=off \[closes #364]
* [Revision #dcc00d2be3](https://github.com/MariaDB/server/commit/dcc00d2be3)\
  2017-11-28 15:03:25 +0300
  * IB: combine is\_delete, vers\_delete into enum \[closes #337]
* [Revision #f826f1249b](https://github.com/MariaDB/server/commit/f826f1249b)\
  2017-11-28 14:21:00 +0300
  * Tests: suppress tinyint error for ppc64le \[#347]
* [Revision #8eac050440](https://github.com/MariaDB/server/commit/8eac050440)\
  2017-11-28 11:40:13 +0300
  * Tests: revert unneded changes
* [Revision #219280392e](https://github.com/MariaDB/server/commit/219280392e)\
  2017-11-27 16:38:52 +0200
  * Cleanup: Do not add a parameter to row\_update\_for\_mysql()
* [Revision #3fdd9c1ccc](https://github.com/MariaDB/server/commit/3fdd9c1ccc)\
  2017-11-27 16:38:21 +0200
  * Correct a comment
* [Revision #86b590c064](https://github.com/MariaDB/server/commit/86b590c064)\
  2017-11-27 21:40:42 +0300
  * SQL: hide system fields from PK \[#361]
* [Revision #f9d875d212](https://github.com/MariaDB/server/commit/f9d875d212)\
  2017-11-27 19:48:36 +0300
  * SQL: disable engine change \[fixes #358]
* [Revision #ababd6a935](https://github.com/MariaDB/server/commit/ababd6a935)\
  2017-11-27 18:28:56 +0300
  * SQL: destroy Vers\_min\_max\_stats \[#346]
* [Revision #941e8b7b0b](https://github.com/MariaDB/server/commit/941e8b7b0b)\
  2017-11-27 16:38:43 +0300
  * Tests: suppression for innodb.log\_corruption
* [Revision #9b6a790660](https://github.com/MariaDB/server/commit/9b6a790660)\
  2017-11-27 10:06:37 +0200
  * Use the FORCE to avoid trouble with vtmd\_template \[#356]
* [Revision #1e3620cc39](https://github.com/MariaDB/server/commit/1e3620cc39)\
  2017-11-23 21:51:54 +0300
  * Tests: commit\_id, truncate for Windows fix \[#307]
* [Revision #aeee150656](https://github.com/MariaDB/server/commit/aeee150656)\
  2017-11-27 13:29:54 +0300
  * SQL: switch\_defaults\_to\_nullable\_trigger\_fields() fix \[#355]
* [Revision #7fab5ecabb](https://github.com/MariaDB/server/commit/7fab5ecabb)\
  2017-11-25 12:56:42 +0300
  * Tests: enable disabled tests \[closes #341]
* [Revision #01a8bad897](https://github.com/MariaDB/server/commit/01a8bad897)\
  2017-11-25 18:04:14 +0300
  * SQL: allow PERIOD as identifier \[fixes #331]
* [Revision #62470fc787](https://github.com/MariaDB/server/commit/62470fc787)\
  2017-11-24 21:26:43 +0300
  * SQL: recreate PRIMARY KEY on DROP SYSTEM VERSIONING \[#348]
* [Revision #0c571f8c4e](https://github.com/MariaDB/server/commit/0c571f8c4e)\
  2017-11-24 19:15:10 +0300
  * SQL: versioning\_alter\_history ERROR mode \[closes #350]
* [Revision #7320c683b9](https://github.com/MariaDB/server/commit/7320c683b9)\
  2017-11-24 17:44:43 +0300
  * Parser: disable SV for tmp tables \[closes #344]
* [Revision #86e57eaaa3](https://github.com/MariaDB/server/commit/86e57eaaa3)\
  2017-11-24 13:55:36 +0200
  * Remove upd\_node\_t::versioned
* [Revision #0b89a42ffc](https://github.com/MariaDB/server/commit/0b89a42ffc)\
  2017-11-24 12:03:24 +0200
  * Remove the flag vers\_update\_trt
* [Revision #03fbfeef66](https://github.com/MariaDB/server/commit/03fbfeef66)\
  2017-11-22 22:21:37 +0200
  * Identify system-versioned columns in the InnoDB dictionary
* [Revision #0cdc1164dc](https://github.com/MariaDB/server/commit/0cdc1164dc)\
  2017-11-24 15:34:57 +0300
  * SQL, IB: various refactoring \[#337]
* [Revision #4dd8736c15](https://github.com/MariaDB/server/commit/4dd8736c15)\
  2017-11-24 09:05:32 +0200
  * Cleanup: removed unused variable in sql\_yacc
* Merge [Revision #6e0b2c7fe0](https://github.com/MariaDB/server/commit/6e0b2c7fe0) 2017-11-23 18:57:26 +0300 - System Versioning 1.0pre2
* [Revision #cbe93291e4](https://github.com/MariaDB/server/commit/cbe93291e4)\
  2017-11-23 17:41:27 +0300
  * SQL,IB: add auto\_inc copy mode fix \[#347]
* [Revision #b612f3baa2](https://github.com/MariaDB/server/commit/b612f3baa2)\
  2017-11-22 17:16:57 +0200
  * Tests: more fine-grained TRT check
* [Revision #5aae304fa0](https://github.com/MariaDB/server/commit/5aae304fa0)\
  2017-11-22 15:24:30 +0300
  * SQL: low timer resolution hack for THD::start\_time \[#307]
* [Revision #3d51315912](https://github.com/MariaDB/server/commit/3d51315912)\
  2017-11-18 23:10:53 +0300
  * Tests: disabled DDL survival tests \[#196]
* [Revision #5994b6873c](https://github.com/MariaDB/server/commit/5994b6873c)\
  2017-11-21 12:25:05 +0300
  * Daemon: TRT check doesn't abort \[fixes #335]
* [Revision #0b40a981de](https://github.com/MariaDB/server/commit/0b40a981de)\
  2017-11-21 15:25:37 +0300
  * Scripts: versioning plugin in deb package \[closes #332]
* [Revision #91ba4f04be](https://github.com/MariaDB/server/commit/91ba4f04be)\
  2017-11-20 18:34:25 +0300
  * SQL: prohibit column conversion to system fields for non-empty table \[fixes #310]
* [Revision #00b98264a8](https://github.com/MariaDB/server/commit/00b98264a8)\
  2017-11-20 15:22:07 +0300
  * IB: removed alloc from row\_ins\_set\_tuple\_col\_8()
* [Revision #4ecb38d7c9](https://github.com/MariaDB/server/commit/4ecb38d7c9)\
  2017-11-19 09:08:41 +0300
  * SQL: variadic argument type fix \[#307]
* [Revision #b0c44d2874](https://github.com/MariaDB/server/commit/b0c44d2874)\
  2017-11-18 23:20:52 +0300
  * Misc: Debian patch for db.Delete\_versioning\_rows\_priv
* [Revision #2b16681ee0](https://github.com/MariaDB/server/commit/2b16681ee0)\
  2017-11-17 23:39:48 +0300
  * SQL, IB: single check of vers\_update\_trt \[#305]
* [Revision #c31aa75dee](https://github.com/MariaDB/server/commit/c31aa75dee)\
  2017-11-17 19:59:31 +0300
  * SQL: open TRT only after versioned write \[#305]\[fixes #321]
* [Revision #9ee3ca8d84](https://github.com/MariaDB/server/commit/9ee3ca8d84)\
  2017-11-17 16:28:24 +0300
  * Tests: reverted original results \[#322]
* [Revision #e83b54cb34](https://github.com/MariaDB/server/commit/e83b54cb34)\
  2017-11-15 18:09:44 +0300
  * Tests: disabled tests failing in 10.3 \[#302]
* [Revision #64d9b82825](https://github.com/MariaDB/server/commit/64d9b82825)\
  2017-11-13 22:45:10 +0300
  * Tests: TRT-related results \[#305]
* [Revision #4f386579f8](https://github.com/MariaDB/server/commit/4f386579f8)\
  2017-11-17 10:07:09 +0300
  * Tests: renamed to mariadb-backup.system\_versioning \[#307]
* [Revision #75cf92fac9](https://github.com/MariaDB/server/commit/75cf92fac9)\
  2017-11-16 16:19:10 +0300
  * Tests: regenerate embedded \[#302]
* [Revision #a4439fef96](https://github.com/MariaDB/server/commit/a4439fef96)\
  2017-11-14 15:47:01 +0300
  * SQL: don't update TRT when altered \[#305, #302]
* [Revision #ecf259cacf](https://github.com/MariaDB/server/commit/ecf259cacf)\
  2017-11-16 15:38:59 +0300
  * SQL: main.flush\_read\_lock fix \[#302]
* [Revision #f9714ef6f4](https://github.com/MariaDB/server/commit/f9714ef6f4)\
  2017-11-15 23:24:45 +0300
  * SQL: open TRT only after versioned write \[#305]
* [Revision #a1e5b4a3c8](https://github.com/MariaDB/server/commit/a1e5b4a3c8)\
  2017-11-15 18:53:59 +0300
  * Tests: table\_flags result \[#302]
* [Revision #6d78496aee](https://github.com/MariaDB/server/commit/6d78496aee)\
  2017-11-15 18:20:42 +0300
  * Tests: disabled TRT for some IB tests \[#302]
* [Revision #f39df037f6](https://github.com/MariaDB/server/commit/f39df037f6)\
  2017-11-15 18:08:00 +0300
  * Daemon: TRT check respects --transaction-registry \[#302]
* [Revision #3fc943cd87](https://github.com/MariaDB/server/commit/3fc943cd87)\
  2017-11-15 17:53:14 +0300
  * Tests: suppressions for innodb\_force\_recovery, ibuf\_not\_empty \[#302]
* [Revision #d83fea9208](https://github.com/MariaDB/server/commit/d83fea9208)\
  2017-11-15 15:19:04 +0300
  * IB: stack corruption on windows \[#302]
* [Revision #af88c66252](https://github.com/MariaDB/server/commit/af88c66252)\
  2017-11-15 14:46:13 +0300
  * SQL,Client: mysqldump for TRT fix \[#302]
* [Revision #0a4aa47ac5](https://github.com/MariaDB/server/commit/0a4aa47ac5)\
  2017-11-15 12:04:51 +0300
  * Revert "Scripts: check PLUGIN\_ROCKSDB to skip cloning it"
* [Revision #870f016356](https://github.com/MariaDB/server/commit/870f016356)\
  2017-11-15 09:46:28 +0800
  * don't `git submodule update` from rocksdb/CMakeLists.txt (#492)
* [Revision #29d25e0522](https://github.com/MariaDB/server/commit/29d25e0522)\
  2017-11-15 00:38:36 +0300
  * IB: row\_ins 'trx' arg reverted \[#305]
* [Revision #97540a5e00](https://github.com/MariaDB/server/commit/97540a5e00)\
  2017-11-14 21:42:21 +0300
  * Tests: regenerated encryption.innodb\_lotoftables \[#302]
* [Revision #9980886cab](https://github.com/MariaDB/server/commit/9980886cab)\
  2017-11-15 00:04:04 +0300
  * Revert "SQL: 1-row partition rotation fix \[fixes #260]"
* [Revision #2b60afe8d2](https://github.com/MariaDB/server/commit/2b60afe8d2)\
  2017-11-14 20:40:33 +0300
  * SQL: TRT fix for crash\_commit\_after \[#305, #302]
* [Revision #ab04950136](https://github.com/MariaDB/server/commit/ab04950136)\
  2017-11-14 19:22:05 +0300
  * Tests: innodb encryption \[#305, #302]
* [Revision #42c0b1d814](https://github.com/MariaDB/server/commit/42c0b1d814)\
  2017-11-14 16:37:21 +0300
  * Sysvars: fix versioning\_asof\_timestamp \[#302]
* [Revision #90c809a61d](https://github.com/MariaDB/server/commit/90c809a61d)\
  2017-11-14 15:04:18 +0300
  * IB: VTQ cleanups \[#305]
* [Revision #ad69c4b722](https://github.com/MariaDB/server/commit/ad69c4b722)\
  2017-11-14 13:16:31 +0300
  * Tests: dependency on wsrep removed from sql\_sequence tests
* [Revision #f9b8c908a0](https://github.com/MariaDB/server/commit/f9b8c908a0)\
  2017-11-13 23:54:04 +0300
  * SQL: ADD/DROP SYSTEM VERSIONING syntax for ALTER TABLE
* [Revision #67907c699c](https://github.com/MariaDB/server/commit/67907c699c)\
  2017-11-13 23:11:27 +0300
  * Tests: better 'near' place fix
* [Revision #72274c10f0](https://github.com/MariaDB/server/commit/72274c10f0)\
  2017-11-13 14:27:58 +0300
  * SQL: TRT failure fixes \[closes #318]
* [Revision #cc6701a7b3](https://github.com/MariaDB/server/commit/cc6701a7b3)\
  2017-11-13 13:00:00 +0300
  * Tests: vtmd, optimized, partition
* [Revision #27b3642a7c](https://github.com/MariaDB/server/commit/27b3642a7c)\
  2017-11-02 12:12:51 +0200
  * Enable --suite=versioning on Windows
* [Revision #08099bc05a](https://github.com/MariaDB/server/commit/08099bc05a)\
  2017-11-11 22:59:28 +0300
  * Daemon: check TRT schema \[closes #309]
* [Revision #0b2c308888](https://github.com/MariaDB/server/commit/0b2c308888)\
  2017-11-10 20:41:30 +0300
  * Daemon: disable --versioning-force for --bootstrap
* [Revision #0812c5ffdf](https://github.com/MariaDB/server/commit/0812c5ffdf)\
  2017-11-10 18:15:46 +0300
  * SQL: versioned check for inplace alter \[#305]
* [Revision #33085349e9](https://github.com/MariaDB/server/commit/33085349e9)\
  2017-11-10 17:54:46 +0300
  * IB, SQL: removed VTQ, added TRT on SQL layer \[closes #305]
* [Revision #fa79f6ac86](https://github.com/MariaDB/server/commit/fa79f6ac86)\
  2017-11-05 19:47:06 +0300
  * IB: style changes \[closes #306]
* [Revision #8972291ac1](https://github.com/MariaDB/server/commit/8972291ac1)\
  2017-11-01 22:13:05 +0300
  * IB: misc fixes \[#305]
* [Revision #e674806282](https://github.com/MariaDB/server/commit/e674806282)\
  2017-11-01 20:17:48 +0300
  * IB: DICT\_TF2\_VERSIONED flag removed
* [Revision #4a662df945](https://github.com/MariaDB/server/commit/4a662df945)\
  2017-11-01 08:08:36 +0300
  * IB: do not use long and ullong types \[#306]
* [Revision #ba80eeb584](https://github.com/MariaDB/server/commit/ba80eeb584)\
  2017-10-31 20:10:37 +0200
  * Fix warnings
* [Revision #ef295cb720](https://github.com/MariaDB/server/commit/ef295cb720)\
  2017-10-26 22:13:30 +0300
  * Revert changes to .gitignore
* [Revision #a80c71dfbb](https://github.com/MariaDB/server/commit/a80c71dfbb)\
  2017-11-01 00:30:46 +0300
  * Scripts: bootstrap fix \[#307]
* [Revision #70a4659d0e](https://github.com/MariaDB/server/commit/70a4659d0e)\
  2017-10-31 18:41:23 +0300
  * Tests: result updates encryption.innodb\_lotoftables encryption.innodb\_encryption funcs\_1.is\_columns\_mysql
* [Revision #fcbb672faa](https://github.com/MariaDB/server/commit/fcbb672faa)\
  2017-10-31 17:54:09 +0300
  * SQL: NOT NULL for timestamps \[#63, #300]
* [Revision #55e9a5e2a4](https://github.com/MariaDB/server/commit/55e9a5e2a4)\
  2017-10-31 14:19:10 +0300
  * Misc: original README.md
* [Revision #e707502a13](https://github.com/MariaDB/server/commit/e707502a13)\
  2017-10-31 12:32:24 +0300
  * Tests: mariadb-backup simple case \[closes #282]
* [Revision #f5ba28404b](https://github.com/MariaDB/server/commit/f5ba28404b)\
  2017-10-31 11:36:38 +0300
  * Tests: innodb.row\_format\_redundant
* [Revision #3f790104c9](https://github.com/MariaDB/server/commit/3f790104c9)\
  2017-10-29 00:14:16 +0300
  * Tests: full test results innodb.innodb-index-online-fk innodb.instant\_alter\_debug innodb.innodb\_skip\_innodb\_is\_tables sys\_vars.sysvars\_server\_notembedded main.mysqld--help
* [Revision #d47dc0747b](https://github.com/MariaDB/server/commit/d47dc0747b)\
  2017-10-28 22:26:04 +0300
  * Tests: partition\_syntax, innodb\_zip.16k, innodb.table\_flags
* [Revision #d7ef775ab6](https://github.com/MariaDB/server/commit/d7ef775ab6)\
  2017-10-28 22:18:32 +0300
  * Scripts: WARN\_MODE off by default
* [Revision #b76787b2c1](https://github.com/MariaDB/server/commit/b76787b2c1)\
  2017-10-28 19:21:33 +0300
  * SQL: removed CLI option --versioning-asof-timestamp
* [Revision #0d3b8ed048](https://github.com/MariaDB/server/commit/0d3b8ed048)\
  2017-10-28 13:51:49 +0300
  * fix win32 warnings
* [Revision #a899e52d08](https://github.com/MariaDB/server/commit/a899e52d08)\
  2017-10-28 12:36:57 +0300
  * Misc: Debian patches update
* [Revision #ca463b533e](https://github.com/MariaDB/server/commit/ca463b533e)\
  2017-10-27 15:23:20 +0300
  * SQL: optimized build fix on view/derived
* [Revision #669fd1d962](https://github.com/MariaDB/server/commit/669fd1d962)\
  2017-10-27 11:54:27 +0300
  * IB: ulint compilation fixes
* [Revision #1d9d351346](https://github.com/MariaDB/server/commit/1d9d351346)\
  2017-10-26 18:14:54 +0300
  * SQL, Test: main suite \[fixes #300]
* [Revision #73f655d576](https://github.com/MariaDB/server/commit/73f655d576)\
  2017-10-25 21:21:40 +0300
  * SQL: VIEW without VERS\_COMMIT\_TS + CTE fix \[fixes #295]
* [Revision #9aae0be8f9](https://github.com/MariaDB/server/commit/9aae0be8f9)\
  2017-10-24 19:48:05 +0300
  * SQL: disabled SYSTEM\_TIME partitioning for InnoDB \[fixes #294]
* [Revision #0ab99d2f34](https://github.com/MariaDB/server/commit/0ab99d2f34)\
  2017-10-24 12:09:04 +0300
  * SQL: no\_replicate for VTMD \[fixes #289]
* [Revision #335bfb3421](https://github.com/MariaDB/server/commit/335bfb3421)\
  2017-10-23 20:15:38 +0300
  * Tests: view.test combinations
* [Revision #7ebd12e779](https://github.com/MariaDB/server/commit/7ebd12e779)\
  2017-10-23 15:12:37 +0300
  * SQL: VIEW of UNION \[fixes #293]
* [Revision #d70bb5e64e](https://github.com/MariaDB/server/commit/d70bb5e64e)\
  2017-10-22 22:20:43 +0300
  * SQL: delete from VIEW \[fixes #291]
* [Revision #c9520cb0c4](https://github.com/MariaDB/server/commit/c9520cb0c4)\
  2017-10-22 20:23:16 +0300
  * SQL: sysvar versioning\_asof\_timestamp \[fixes #292, #279]
* [Revision #a86d6bad54](https://github.com/MariaDB/server/commit/a86d6bad54)\
  2017-10-30 23:44:13 +0300
  * Scripts: check PLUGIN\_ROCKSDB to skip cloning it
* Merge [Revision #497c6add88](https://github.com/MariaDB/server/commit/497c6add88) 2017-11-13 11:06:18 +0300 - System Versioning pre1.0
* Merge [Revision #d8d7251019](https://github.com/MariaDB/server/commit/d8d7251019) 2017-11-07 00:37:49 +0300 - System Versioning pre0.12
* [Revision #ce66d5b2a5](https://github.com/MariaDB/server/commit/ce66d5b2a5)\
  2017-10-17 17:23:59 +0300
  * SQL: assertion in partition\_info::vers\_trx\_id\_to\_ts()
* [Revision #17bd486f36](https://github.com/MariaDB/server/commit/17bd486f36)\
  2017-10-17 17:20:46 +0300
  * SQL: thd\_start\_utime() fix \[fixes #284]
* [Revision #8e193661d2](https://github.com/MariaDB/server/commit/8e193661d2)\
  2017-10-09 18:42:59 +0300
  * IB: vtq\_notify\_on\_commit initialization fix
* [Revision #d7a484b04f](https://github.com/MariaDB/server/commit/d7a484b04f)\
  2017-10-04 13:36:31 +0300
  * SQL: segfault after make\_select() in VTMD
* [Revision #1d056f5abc](https://github.com/MariaDB/server/commit/1d056f5abc)\
  2017-10-03 00:31:44 +0300
  * SQL: not a VTMD table warning \[related to #199]
* [Revision #9062385c20](https://github.com/MariaDB/server/commit/9062385c20)\
  2017-09-29 17:51:10 +0300
  * SQL: invalidate current SP at archive substitution \[closes #127]
* [Revision #5e42511ce1](https://github.com/MariaDB/server/commit/5e42511ce1)\
  2017-09-28 13:16:04 +0300
  * SQL: SELECT from archive table \[closes #127]
* [Revision #c5801dd67b](https://github.com/MariaDB/server/commit/c5801dd67b)\
  2017-09-27 22:08:20 +0300
  * SQL: hide archive tables \[closes #193]
* [Revision #e9e3cb0f6e](https://github.com/MariaDB/server/commit/e9e3cb0f6e)\
  2017-09-27 14:29:25 +0300
  * SQL: VTMD for SHOW CREATE fixes \[related to #125]
* [Revision #79e17b26fb](https://github.com/MariaDB/server/commit/79e17b26fb)\
  2017-09-27 10:24:40 +0300
  * SQL: VTMD\_table::get\_archive\_tables() misc fixes
* [Revision #75bc483d7a](https://github.com/MariaDB/server/commit/75bc483d7a)\
  2017-09-25 13:24:44 +0300
  * Tests: moved concat\_execN() to common.inc
* [Revision #f79c4469ff](https://github.com/MariaDB/server/commit/f79c4469ff)\
  2017-09-25 11:29:16 +0300
  * SQL: helpers to get archive tables list \[closes #199]
* [Revision #7f2064780c](https://github.com/MariaDB/server/commit/7f2064780c)\
  2017-09-22 22:09:41 +0300
  * SQL: versioning\_alter\_history values description
* [Revision #3b7c10f0b7](https://github.com/MariaDB/server/commit/3b7c10f0b7)\
  2017-09-20 14:32:48 +0300
  * Style: garbage Copy\_field member
* [Revision #11a9d8f7e3](https://github.com/MariaDB/server/commit/11a9d8f7e3)\
  2017-09-20 13:14:16 +0300
  * Tests: typo fix in cte.test
* [Revision #6c9b71d734](https://github.com/MariaDB/server/commit/6c9b71d734)\
  2017-09-20 13:07:15 +0300
  * SQL: VTMD for OR REPLACE \[fixes #270]
* [Revision #9ba635fda3](https://github.com/MariaDB/server/commit/9ba635fda3)\
  2017-09-14 13:56:24 +0300
  * SQL: VIEW with UNION fix \[fixes #269]
* [Revision #7e764ae188](https://github.com/MariaDB/server/commit/7e764ae188)\
  2017-09-13 10:57:23 +0300
  * SQL: 1-row partition rotation fix \[fixes #260]
* [Revision #78d2430aa2](https://github.com/MariaDB/server/commit/78d2430aa2)\
  2017-09-12 16:27:44 +0300
  * Tests: VTMD + modify column
* [Revision #a49239b57a](https://github.com/MariaDB/server/commit/a49239b57a)\
  2017-09-08 10:22:24 +0300
  * SQL: truncate syntax and privilege \[closes #229]
* [Revision #904b69cd9e](https://github.com/MariaDB/server/commit/904b69cd9e)\
  2017-09-07 15:49:11 +0300
  * SQL: partitioning misc fixes \[closes #242]
* [Revision #a734c2f0fb](https://github.com/MariaDB/server/commit/a734c2f0fb)\
  2017-09-05 16:49:08 +0300
  * Style: partitioning, sysvars, handler fixes
* [Revision #40e3922ac2](https://github.com/MariaDB/server/commit/40e3922ac2)\
  2017-09-04 19:16:22 +0300
  * Tests: results update in sys\_vars, funcs\_1 suites
* [Revision #88ccf759c1](https://github.com/MariaDB/server/commit/88ccf759c1)\
  2017-09-01 19:05:20 +0300
  * SQL: pruning, derived, view fixes \[fixes #244]
* [Revision #c2a70c8050](https://github.com/MariaDB/server/commit/c2a70c8050)\
  2017-09-01 12:41:46 +0300
  * SQL, IB: option to drop historical rows on ALTER \[closes #249]
* [Revision #a6aaa4fefe](https://github.com/MariaDB/server/commit/a6aaa4fefe)\
  2017-08-30 15:28:43 +0300
  * SQL: move Vers\_extended\_item::vtq\_cached\_result() to Item \[closes #250]
* [Revision #b231a85200](https://github.com/MariaDB/server/commit/b231a85200)\
  2017-08-30 11:14:03 +0300
  * Plugins: lost terminator in versioning plugin \[fixes #248]
* [Revision #ccddb4f766](https://github.com/MariaDB/server/commit/ccddb4f766)\
  2017-08-18 21:06:02 +0300
  * Misc: simplify code
* [Revision #b4cd2d3c12](https://github.com/MariaDB/server/commit/b4cd2d3c12)\
  2017-08-18 15:30:55 +0300
  * Tests: duplicate system versioning field
* [Revision #99baeaa951](https://github.com/MariaDB/server/commit/99baeaa951)\
  2017-08-18 14:29:22 +0300
  * SQL: MAX microseconds for current system rows \[fixes #245]
* [Revision #9714c4463d](https://github.com/MariaDB/server/commit/9714c4463d)\
  2017-08-17 08:58:07 +0300
  * Misc: comment
* [Revision #d3d2ea9fd5](https://github.com/MariaDB/server/commit/d3d2ea9fd5)\
  2017-08-08 17:12:16 +0300
  * SQL, Parser: system\_time logic and syntax fixes \[closes #237]
* [Revision #53370de103](https://github.com/MariaDB/server/commit/53370de103)\
  2017-08-04 17:06:33 +0300
  * IB: partition-wise ha\_innopart::rnd\_init() \[fixes #208]
* [Revision #5ce6044b1c](https://github.com/MariaDB/server/commit/5ce6044b1c)\
  2017-08-03 15:04:15 +0300
  * SQL: remove versioning only when hidden system fields
* [Revision #c2c8808a16](https://github.com/MariaDB/server/commit/c2c8808a16)\
  2017-08-03 10:11:49 +0300
  * SQL: compare TRX\_ID fields against timestamps \[closes #231]
* [Revision #d998da0306](https://github.com/MariaDB/server/commit/d998da0306)\
  2017-07-31 11:42:48 +0300
  * SQL: replication fixes \[fixes #234]
* [Revision #88454b3320](https://github.com/MariaDB/server/commit/88454b3320)\
  2017-07-24 16:22:59 +0300
  * SQL: comment and check about ALTER in update\_auto\_increment()
* [Revision #aa292666cc](https://github.com/MariaDB/server/commit/aa292666cc)\
  2017-07-23 17:07:56 +0300
  * Parser: moved 'for system\_time' before alias
* [Revision #a5ec9fc1b4](https://github.com/MariaDB/server/commit/a5ec9fc1b4)\
  2017-07-21 17:52:47 +0300
  * Style: mysqld.h comments
* [Revision #c2f6214671](https://github.com/MariaDB/server/commit/c2f6214671)\
  2017-07-21 07:53:58 +0300
  * Tests: renamed optimized\_fields to optimized
* [Revision #c99bd3ac1a](https://github.com/MariaDB/server/commit/c99bd3ac1a)\
  2017-07-20 15:00:10 +0300
  * Tests: truncate.test: get rid of transaction number
* [Revision #f8b6256992](https://github.com/MariaDB/server/commit/f8b6256992)\
  2017-07-15 13:59:15 +0300
  * SQL: disallow ALTER CHANGE of system fields \[fixes #213]
* [Revision #909867d014](https://github.com/MariaDB/server/commit/909867d014)\
  2017-07-13 18:48:30 +0300
  * SQL: optimized fields fix for NOT NULL \[fixes #226]
* [Revision #91c8b43e77](https://github.com/MariaDB/server/commit/91c8b43e77)\
  2017-07-12 11:24:03 +0300
  * Parser: syntax for query system\_time \[closes #230]
* [Revision #60e456df33](https://github.com/MariaDB/server/commit/60e456df33)\
  2017-07-12 10:36:02 +0300
  * SQL: system\_time propagation from derived table \[fixes #228]
* [Revision #dcb54040bc](https://github.com/MariaDB/server/commit/dcb54040bc)\
  2017-07-07 17:52:23 +0300
  * SQL: VTQ testing iface moved to plugin \[closes #224]
* [Revision #42a0289de9](https://github.com/MariaDB/server/commit/42a0289de9)\
  2017-07-06 15:22:10 +0300
  * Tests: optimized fields
* [Revision #1903b407da](https://github.com/MariaDB/server/commit/1903b407da)\
  2017-07-04 17:45:14 +0300
  * SQL: ignore columns WITHOUT VERSIONING \[fixes #220]
* [Revision #bdcce58fad](https://github.com/MariaDB/server/commit/bdcce58fad)\
  2017-07-04 12:05:40 +0300
  * IB: long names in information\_schema
* [Revision #72de7721b9](https://github.com/MariaDB/server/commit/72de7721b9)\
  2017-07-03 17:38:59 +0300
  * SQL: No implicit versioning when created from SELECT \[closes #219]
* [Revision #5570ab3789](https://github.com/MariaDB/server/commit/5570ab3789)\
  2017-07-03 12:15:55 +0300
  * SQL: history records became alive on copy \[fixes #212]
* [Revision #4b0f1284ee](https://github.com/MariaDB/server/commit/4b0f1284ee)\
  2017-06-29 19:35:08 +0300
  * SQL: revisit error messages \[closes #217]
* [Revision #177e477553](https://github.com/MariaDB/server/commit/177e477553)\
  2017-06-29 15:11:06 +0300
  * Tests: VTQ iso\_level check fix
* [Revision #229c528110](https://github.com/MariaDB/server/commit/229c528110)\
  2017-06-27 20:59:27 +0300
  * SQL: hide system fields instead of drop \[closes #210]
* [Revision #46d572dde4](https://github.com/MariaDB/server/commit/46d572dde4)\
  2017-06-27 12:22:52 +0300
  * SQL: default engine fix in create from versioned \[fixes #206]
* [Revision #faab918ecd](https://github.com/MariaDB/server/commit/faab918ecd)\
  2017-06-23 09:33:25 +0300
  * Style: comment about VTQ
* [Revision #b44425c6be](https://github.com/MariaDB/server/commit/b44425c6be)\
  2017-06-22 23:36:50 +0300
  * Misc, SQL: checks cleanup in Item\_field::set\_field()
* [Revision #07ff0e1202](https://github.com/MariaDB/server/commit/07ff0e1202)\
  2017-06-22 23:09:34 +0300
  * SQL: start\_end\_t members as LEX\_CSTRING
* [Revision #670b7f5fd4](https://github.com/MariaDB/server/commit/670b7f5fd4)\
  2017-06-22 20:15:03 +0300
  * Style: API renames
* [Revision #2442a81eff](https://github.com/MariaDB/server/commit/2442a81eff)\
  2017-06-20 11:37:12 +0300
  * IB: read lock on partitioned table read \[closes #200]
* [Revision #ac5eb9771e](https://github.com/MariaDB/server/commit/ac5eb9771e)\
  2017-06-17 17:59:22 +0300
  * SQL: Versioned SHOW CREATE TABLE \[closes #125]
* [Revision #448374a228](https://github.com/MariaDB/server/commit/448374a228)\
  2017-06-15 16:02:32 +0300
  * SQL, IB: (0.10) VTMD tracking \[closes #124]
* [Revision #efaa0d66da](https://github.com/MariaDB/server/commit/efaa0d66da)\
  2017-06-13 10:07:16 +0300
  * Cleanup: stale sql/field.h.orig
* [Revision #f915fe8eae](https://github.com/MariaDB/server/commit/f915fe8eae)\
  2017-06-02 16:53:24 +0300
  * SQL: renamed vers\_thd\_get\_now() to THD::query\_start\_TIME()
* [Revision #397a891538](https://github.com/MariaDB/server/commit/397a891538)\
  2017-05-25 15:19:49 +0300
  * SQL: minor cleanup in mysql\_alter\_table()
* [Revision #1c8a2de73e](https://github.com/MariaDB/server/commit/1c8a2de73e)\
  2017-05-24 18:52:48 +0300
  * Scripts: VTMD schema fix
* [Revision #414651c80a](https://github.com/MariaDB/server/commit/414651c80a)\
  2017-05-23 11:15:44 +0300
  * SQL: ALTER ADD COLUMN order fix
* [Revision #3bdf5b60ec](https://github.com/MariaDB/server/commit/3bdf5b60ec)\
  2017-05-22 23:43:55 +0300
  * Misc: README.md Travis CI label
* [Revision #84b4baef93](https://github.com/MariaDB/server/commit/84b4baef93)\
  2017-05-22 23:40:48 +0300
  * SQL: SHOW CREATE for GENERATED ALWAYS AS ROW
* [Revision #45f6acd296](https://github.com/MariaDB/server/commit/45f6acd296)\
  2017-05-19 23:27:40 +0300
  * Scripts: VTMD table \[closes #122]
* [Revision #abba11e6c4](https://github.com/MariaDB/server/commit/abba11e6c4)\
  2017-05-19 01:40:11 +0300
  * SQL: fix fix\_create\_like()
* [Revision #ec0002e908](https://github.com/MariaDB/server/commit/ec0002e908)\
  2017-05-18 16:44:29 +0300
  * Parser: useful attributes for AS ROW fields
* [Revision #fe71bdf568](https://github.com/MariaDB/server/commit/fe71bdf568)\
  2017-05-14 21:33:01 +0300
  * Tests: order independence of versioning fields
* [Revision #7445be89af](https://github.com/MariaDB/server/commit/7445be89af)\
  2017-05-11 12:29:14 +0300
  * IB: correct way of using start\_time\_micro \[fixes #189]
* [Revision #f751b30884](https://github.com/MariaDB/server/commit/f751b30884)\
  2017-05-03 14:28:15 +0300
  * Style: comment fixes
* [Revision #0185872449](https://github.com/MariaDB/server/commit/0185872449)\
  2017-04-24 14:47:44 +0300
  * SQL: versioning DDL part I \[closes #172]
* [Revision #f94fd4b730](https://github.com/MariaDB/server/commit/f94fd4b730)\
  2017-05-03 12:09:17 +0300
  * Style: warning fix
* [Revision #44506f2669](https://github.com/MariaDB/server/commit/44506f2669)\
  2017-05-03 06:15:20 +0300
  * SQL: vers\_ sysvars renamed to versioning\_
* [Revision #dc12395b0b](https://github.com/MariaDB/server/commit/dc12395b0b)\
  2017-05-02 17:41:29 +0300
  * Misc: travis speed up
* [Revision #1bdf011314](https://github.com/MariaDB/server/commit/1bdf011314)\
  2017-05-02 11:02:03 +0300
  * Merge: stale innodb\_support\_xa\_basic
* [Revision #7e0ff13d7a](https://github.com/MariaDB/server/commit/7e0ff13d7a)\
  2017-04-30 23:51:42 +0300
  * SQL: derived fixes \[related to #185]
* [Revision #8a11f9b243](https://github.com/MariaDB/server/commit/8a11f9b243)\
  2017-04-30 23:12:29 +0300
  * SQL: VIEW fix \[related to #185]
* [Revision #f43726a15d](https://github.com/MariaDB/server/commit/f43726a15d)\
  2017-04-29 22:28:32 +0300
  * Scipts: --tail-lines option for mtr
* [Revision #7153ff85a1](https://github.com/MariaDB/server/commit/7153ff85a1)\
  2017-04-28 12:07:04 +0300
  * SQL: derived tables improvements \[closes #185]
* [Revision #79688b0546](https://github.com/MariaDB/server/commit/79688b0546)\
  2017-04-28 15:49:09 +0300
  * IB: missed start\_time\_micro in minor ways of trx start
* [Revision #642525b9ad](https://github.com/MariaDB/server/commit/642525b9ad)\
  2017-04-28 09:46:00 +0300
  * Tests: cte\_recursive, simple (new plans)
* [Revision #b19645caf5](https://github.com/MariaDB/server/commit/b19645caf5)\
  2017-04-27 10:50:23 +0300
  * Tests: verify\_vtq() fix
* [Revision #122ffa2211](https://github.com/MariaDB/server/commit/122ffa2211)\
  2017-04-27 10:24:16 +0300
  * SQL(misc): Query\_arena\_stmt RAII
* [Revision #1e8a81dea6](https://github.com/MariaDB/server/commit/1e8a81dea6)\
  2017-04-25 15:02:48 +0300
  * SQL: CREATE VIEW and misc improvements \[fixes #183]
* [Revision #27a6ef0a9e](https://github.com/MariaDB/server/commit/27a6ef0a9e)\
  2017-04-19 16:34:36 +0300
  * IB,SQL: Innopart UPDATE \[fixes #178]
* [Revision #7d2ed77e31](https://github.com/MariaDB/server/commit/7d2ed77e31)\
  2017-04-17 20:35:39 +0300
  * SQL: SIGSEGV in create\_tmp\_table() \[fixes #179] tests are in main,rpl suites
* [Revision #6ac4dfedf4](https://github.com/MariaDB/server/commit/6ac4dfedf4)\
  2017-04-17 12:42:49 +0300
  * Tests: sys\_vars.sysvars\_server\_notembedded result (3) Related to #175
* [Revision #915963ba30](https://github.com/MariaDB/server/commit/915963ba30)\
  2017-04-14 11:07:58 +0300
  * SQL: SIGABRT fix on versioned partitioning error \[fixes #177]
* [Revision #e72e3cd01f](https://github.com/MariaDB/server/commit/e72e3cd01f)\
  2017-04-12 23:19:13 +0300
  * IB: redundant btr\_pcur\_move\_to\_prev\_page() removed
* [Revision #ecc6cd95c4](https://github.com/MariaDB/server/commit/ecc6cd95c4)\
  2017-04-11 19:37:48 +0300
  * SQL: Default 'simple' algorithm for InnoDB 'AS OF' \[closes #175]
* [Revision #a1d42a6f20](https://github.com/MariaDB/server/commit/a1d42a6f20)\
  2017-04-11 18:28:24 +0300
  * Misc: code cleanup
* [Revision #06ad9c01a6](https://github.com/MariaDB/server/commit/06ad9c01a6)\
  2017-04-11 18:19:01 +0300
  * Misc: unneeded code after c17b5a3c973dff544613043b74db7d131e0cb55a
* [Revision #d64702d43a](https://github.com/MariaDB/server/commit/d64702d43a)\
  2017-04-11 17:58:56 +0300
  * SQL: different results when querying a VIEW from PREPARED STATEMENT and without it \[fixes #176]
* [Revision #ecd18bc099](https://github.com/MariaDB/server/commit/ecd18bc099)\
  2017-04-05 21:37:31 +0300
  * SQL: allow FOR SYSTEM\_TIME BEFORE for SELECT queries \[closes #170]
* [Revision #4af3cb82e6](https://github.com/MariaDB/server/commit/4af3cb82e6)\
  2017-04-05 18:51:31 +0300
  * IB: MIN/MAX trx\_id by querying VTQ with commit ts \[closes #168]
* [Revision #994cdf1b7a](https://github.com/MariaDB/server/commit/994cdf1b7a)\
  2017-04-17 11:22:52 +0300
  * Parser: Oracle mode fix
* [Revision #d85fa88676](https://github.com/MariaDB/server/commit/d85fa88676)\
  2017-03-31 13:21:30 +0300
  * Misc: disable clang warning 'offset for non-POD type'
* [Revision #9e9af76eaf](https://github.com/MariaDB/server/commit/9e9af76eaf)\
  2017-03-30 12:57:31 +0300
  * SQL: vers\_current\_time refactoring \[closes #117]
* [Revision #b240671c04](https://github.com/MariaDB/server/commit/b240671c04)\
  2017-03-30 23:13:09 +0300
  * Tests: sys\_vars.sysvars\_server\_notembedded result (2) Related to #157
* [Revision #f77a4135bf](https://github.com/MariaDB/server/commit/f77a4135bf)\
  2017-03-30 15:32:31 +0300
  * SQL: parsing of QUERY FOR \[fixes #159] Reverts 46e36bbffa7cd8d9eb861a22755025ffe8751449 - SQL: fix assertion failure in parser
* [Revision #f8b562f5e7](https://github.com/MariaDB/server/commit/f8b562f5e7)\
  2017-03-28 15:44:48 +0300
  * Scripts: capture\_warnings.sh missed errors and exit status fix
* [Revision #67cd92b6f4](https://github.com/MariaDB/server/commit/67cd92b6f4)\
  2017-03-24 16:00:42 +0300
  * SQL, IB: Copy history via CREATE .. SELECT \[closes #157, #152]
* [Revision #7a525e7e93](https://github.com/MariaDB/server/commit/7a525e7e93)\
  2017-03-24 14:53:20 +0300
  * Parser: no implicit NOT NULL for system fields \[fixes #163]
* [Revision #14f007f907](https://github.com/MariaDB/server/commit/14f007f907)\
  2017-03-23 23:19:22 +0300
  * SQL: versioning in embedded JOINs \[fixes #160]
* [Revision #e8ae9f1ae9](https://github.com/MariaDB/server/commit/e8ae9f1ae9)\
  2017-03-23 16:14:19 +0300
  * SQL: VIEW NATURAL JOIN TABLE \[fixes #161]
* [Revision #21e8b22f53](https://github.com/MariaDB/server/commit/21e8b22f53)\
  2017-03-21 13:33:26 +0300
  * Misc: vers\_select\_conds\_t::init\_from\_sysvar()
* [Revision #352d83569b](https://github.com/MariaDB/server/commit/352d83569b)\
  2017-03-16 18:35:36 +0300
  * SQL: versioning for tmp HEAP tables created from IB tables \[closes #158]
* [Revision #1894fab11a](https://github.com/MariaDB/server/commit/1894fab11a)\
  2017-03-15 18:36:54 +0300
  * Tests: split versioning.select into combinations
* [Revision #fb0b3e5902](https://github.com/MariaDB/server/commit/fb0b3e5902)\
  2017-03-15 16:32:44 +0300
  * SQL: NATURAL LEFT JOIN for versioned tables \[fixes #156]
* [Revision #5a08bd3515](https://github.com/MariaDB/server/commit/5a08bd3515)\
  2017-03-14 20:55:17 +0300
  * Tests: subqueries with JOINed tables with different FOR SYSTEM\_TIME clauses \[closes #154]
* [Revision #7fd549095f](https://github.com/MariaDB/server/commit/7fd549095f)\
  2017-03-14 13:38:59 +0300
  * IB: return correct sys\_trx\_end in TRIGGER after UPDATE \[fixes #100]
* [Revision #4ebf680c9b](https://github.com/MariaDB/server/commit/4ebf680c9b)\
  2017-03-14 13:05:39 +0300
  * SQL: VIEW over a JOIN of versioned tables \[fixes #153]
* [Revision #92c7a87119](https://github.com/MariaDB/server/commit/92c7a87119)\
  2017-03-14 10:09:44 +0300
  * Misc: vers\_setup\_select() Item\_field ctor fix
* [Revision #77f23b3e49](https://github.com/MariaDB/server/commit/77f23b3e49)\
  2017-03-14 06:44:48 +0300
  * Tests: sys\_vars.sysvars\_server\_notembedded result
* [Revision #9ea02899f8](https://github.com/MariaDB/server/commit/9ea02899f8)\
  2017-03-13 20:14:24 +0300
  * SQL: nested equi-join for versioned table \[fixes #150]
* [Revision #a37cf5258b](https://github.com/MariaDB/server/commit/a37cf5258b)\
  2017-03-13 14:29:21 +0300
  * SQL: CREATE VIEW with view\_list from versioned table \[fixes #151]
* [Revision #4782b74023](https://github.com/MariaDB/server/commit/4782b74023)\
  2017-03-11 13:09:07 +0700
  * Misc: warnings fix
* [Revision #d85e7a5e01](https://github.com/MariaDB/server/commit/d85e7a5e01)\
  2017-03-10 16:55:14 +0300
  * SQL: NATUAL JOIN on view + table \[fixes #148]
* [Revision #0e01038936](https://github.com/MariaDB/server/commit/0e01038936)\
  2017-03-10 20:25:30 +0700
  * SQL: forced, hidden versioning \[closes #32]
* [Revision #cbb674282a](https://github.com/MariaDB/server/commit/cbb674282a)\
  2017-03-09 12:16:53 +0700
  * SQL: moved VTQ items to separate file
* [Revision #afe64a450e](https://github.com/MariaDB/server/commit/afe64a450e)\
  2017-03-08 00:45:23 +0700
  * IB: moved VTQ funcs to separate file
* [Revision #7a22dd3716](https://github.com/MariaDB/server/commit/7a22dd3716)\
  2017-03-06 20:07:10 +0300
  * SQL: INNER JOIN USING with versioned tables \[fixes #147]
* [Revision #9355e3e966](https://github.com/MariaDB/server/commit/9355e3e966)\
  2017-03-06 15:53:53 +0300
  * SQL: CREATE TABLE LIKE for versioned tables \[fixes #146]
* [Revision #17745222a1](https://github.com/MariaDB/server/commit/17745222a1)\
  2017-03-05 23:51:02 +0300
  * SQL: incorrect check on specific JOIN query \[fixes #145]
* [Revision #204b54d2d9](https://github.com/MariaDB/server/commit/204b54d2d9)\
  2017-03-04 23:05:45 +0300
  * SQL: create versioned tmp table from query \[fixes #144]
* [Revision #b8bfc06b26](https://github.com/MariaDB/server/commit/b8bfc06b26)\
  2017-02-27 16:31:37 +0300
  * SQL, Tests: temporal\_current\_timestamp for setting default AS OF timestamp \[closes #117]
* [Revision #fc7da4dd4f](https://github.com/MariaDB/server/commit/fc7da4dd4f)\
  2017-02-20 10:06:58 +0300
  * IB, SQL: InnoDB partitioning \[closes #118]
* [Revision #fb801289f3](https://github.com/MariaDB/server/commit/fb801289f3)\
  2017-02-17 15:11:15 +0300
  * IB, Tests: ALTER with ALGORITHM=INPLACE for InnoDB \[closes #87]
* [Revision #bcc8ba78bc](https://github.com/MariaDB/server/commit/bcc8ba78bc)\
  2017-02-09 12:01:05 +0300
  * SQL, Tests: versioning for nested queries and CTE \[closes #74]
* [Revision #c9b2980c4f](https://github.com/MariaDB/server/commit/c9b2980c4f)\
  2017-02-17 15:18:24 +0300
  * Scripts: fix Travis label in README.md
* [Revision #7aa3ebdd18](https://github.com/MariaDB/server/commit/7aa3ebdd18)\
  2017-01-31 22:41:38 +0300
  * SQL, Tests: FOR SYSTEM\_TIME for VIEWs \[closes #98]
* [Revision #5853266fab](https://github.com/MariaDB/server/commit/5853266fab)\
  2017-02-08 21:54:13 +0300
  * Style: condition rewrite
* [Revision #e7ac369a72](https://github.com/MariaDB/server/commit/e7ac369a72)\
  2017-02-02 16:21:06 +0300
  * Scripts: print\_warnings deps fix
* [Revision #94f83b262d](https://github.com/MariaDB/server/commit/94f83b262d)\
  2017-01-21 16:38:57 +0300
  * SQL: fix assertion failure in parser \[closes #119]
* [Revision #64be66b6c0](https://github.com/MariaDB/server/commit/64be66b6c0)\
  2017-01-22 15:03:13 +0300
  * Scripts: suppress warnings via suppress.warnings file \[closes #78]
* [Revision #8be01458a3](https://github.com/MariaDB/server/commit/8be01458a3)\
  2017-01-21 19:34:06 +0300
  * Scripts: try to fix Travis
* [Revision #daa9bc8bdf](https://github.com/MariaDB/server/commit/daa9bc8bdf)\
  2017-01-21 18:19:46 +0300
  * Scripts: by default test versioning too
* [Revision #8378ddad2d](https://github.com/MariaDB/server/commit/8378ddad2d)\
  2017-01-19 23:09:47 +0300
  * Tests: disable tests failing in 10.3
* [Revision #26a3ff0a22](https://github.com/MariaDB/server/commit/26a3ff0a22)\
  2016-12-31 15:33:26 +0000
  * SQL: (0.6) Pruning for VERSIONING partitions \[closes #97]
* [Revision #e069de7d9d](https://github.com/MariaDB/server/commit/e069de7d9d)\
  2017-01-12 13:51:12 +0300
  * SQL: TRUNCATE FOR SYSTEM\_TIME BEFORE \[closes #111]
* [Revision #3a64d55aed](https://github.com/MariaDB/server/commit/3a64d55aed)\
  2017-01-13 13:56:01 +0000
  * Parser, SQL: table-specific FOR SYSTEM\_TIME \[closes #116]
* [Revision #57692d7117](https://github.com/MariaDB/server/commit/57692d7117)\
  2017-01-10 15:15:39 +0300
  * SQL, IB: ALTER ADD AUTO\_INCREMENT for versioned tables \[closes #112]
* [Revision #c9e4ac4b72](https://github.com/MariaDB/server/commit/c9e4ac4b72)\
  2016-12-23 17:05:57 +0300
  * 0.6: truncate history feature \[closes #96]
* [Revision #4c37011582](https://github.com/MariaDB/server/commit/4c37011582)\
  2017-01-17 13:47:08 +0300
  * Tests: disabled failing (in 10.2) tests
* [Revision #abb2f9488d](https://github.com/MariaDB/server/commit/abb2f9488d)\
  2016-12-26 18:46:02 +0300
  * IB: skip sys\_trx\_start when comparing master and slave rows \[closes #107]
* [Revision #4383e16cbe](https://github.com/MariaDB/server/commit/4383e16cbe)\
  2016-12-25 08:25:17 +0000
  * IB: skip check\_ref on historical record \[fixes #101]
* [Revision #ea60760e47](https://github.com/MariaDB/server/commit/ea60760e47)\
  2016-12-22 07:34:33 +0000
  * SQL: missed FOR SYSTEM\_TIME ALL for FOR\_SYSTEM\_TIME\_UNSPECIFIED
* [Revision #27d9e762a9](https://github.com/MariaDB/server/commit/27d9e762a9)\
  2016-12-21 08:17:44 +0000
  * SQL: prohibit write-locking of historic rows \[fixes #102]
* [Revision #46badf17c4](https://github.com/MariaDB/server/commit/46badf17c4)\
  2016-12-21 05:57:00 +0000
  * IB: FK cascade delete when parent versioned \[fixes #101]
* [Revision #412dd1e1f3](https://github.com/MariaDB/server/commit/412dd1e1f3)\
  2016-12-20 18:52:45 +0000
  * SQL: FOR SYSTEM\_TIME support in VIEW expression \[fixes #99]
* [Revision #2157c6bfbc](https://github.com/MariaDB/server/commit/2157c6bfbc)\
  2016-12-19 11:48:12 +0000
  * IB: misc cleanup
* [Revision #e45b85eb3e](https://github.com/MariaDB/server/commit/e45b85eb3e)\
  2016-12-18 17:06:43 +0000
  * SQL: replication from unversioned to versioned \[fixes #94]
* [Revision #ef10ef98ab](https://github.com/MariaDB/server/commit/ef10ef98ab)\
  2016-12-16 14:11:23 +0300
  * SQL: UPDATE on row-based replication \[closes: #94]
* [Revision #41d9840850](https://github.com/MariaDB/server/commit/41d9840850)\
  2016-12-15 13:04:45 +0300
  * SQL: remove unneded return value
* [Revision #e851c140f4](https://github.com/MariaDB/server/commit/e851c140f4)\
  2016-12-11 17:04:11 +0000
  * SQL: (0.5) Versioned partitions \[closes #77]
* [Revision #dc4ef66fee](https://github.com/MariaDB/server/commit/dc4ef66fee)\
  2016-12-10 21:56:32 +0300
  * SQL: optimize FOR SYSTEM\_TIME ALL queries \[closes #85]
* [Revision #1dc021360b](https://github.com/MariaDB/server/commit/1dc021360b)\
  2016-12-10 19:26:09 +0300
  * Scripts: valgrind with test suite
* [Revision #1742561b4e](https://github.com/MariaDB/server/commit/1742561b4e)\
  2016-12-10 18:33:40 +0300
  * fix use-after-free \[closes #89]
* [Revision #a17b8f707f](https://github.com/MariaDB/server/commit/a17b8f707f)\
  2016-12-07 15:15:47 +0300
  * 0.5: basic support for ALTER TABLE for InnoDB and other storage engines \[closes #57]
* [Revision #65e900ff04](https://github.com/MariaDB/server/commit/65e900ff04)\
  2016-12-09 23:08:31 +0300
  * IB: remove unused function
* [Revision #695c5aabad](https://github.com/MariaDB/server/commit/695c5aabad)\
  2016-12-09 06:36:31 +0000
  * SQL: error on FOR SYSTEM\_TIME without any versioned tables
* [Revision #1bedafb733](https://github.com/MariaDB/server/commit/1bedafb733)\
  2016-11-24 17:36:02 +0300
  * fix build and some warnings
* [Revision #48d924693f](https://github.com/MariaDB/server/commit/48d924693f)\
  2016-11-23 22:30:14 +0300
  * IB: do not insert into VTQ on optimized fields only update \[closes #80]
* [Revision #dd3099a00d](https://github.com/MariaDB/server/commit/dd3099a00d)\
  2016-11-24 04:00:28 +0000
  * SQL: unsupported engine fix for VTQ funcs
* [Revision #6c516e77d5](https://github.com/MariaDB/server/commit/6c516e77d5)\
  2016-11-23 12:20:48 +0000
  * IB: notify VTQ on innobase\_commit\_ordered() \[fixes #79]
* [Revision #eff649eba4](https://github.com/MariaDB/server/commit/eff649eba4)\
  2016-11-21 16:41:51 +0000
  * Parser: syntax extension FOR SYSTEM\_TIME ALL
* [Revision #9a7a9ae9b9](https://github.com/MariaDB/server/commit/9a7a9ae9b9)\
  2016-11-21 13:16:46 +0000
  * Scripts: capture\_warnings.sh fix
* [Revision #53d9e614ae](https://github.com/MariaDB/server/commit/53d9e614ae)\
  2016-11-21 15:44:20 +0300
  * Scripts: reprint warnings fix
* [Revision #a1c36f2e15](https://github.com/MariaDB/server/commit/a1c36f2e15)\
  2016-11-20 18:17:28 +0000
  * SQL: default NULL for sys fields + misc fixes
* [Revision #b98f09fcbf](https://github.com/MariaDB/server/commit/b98f09fcbf)\
  2016-11-20 22:17:35 +0300
  * Scripts: Three modes of warning printing.
* [Revision #303d72a0f4](https://github.com/MariaDB/server/commit/303d72a0f4)\
  2016-11-19 12:29:07 +0000
  * SQL: redundant error codes reduced
* [Revision #52a6812595](https://github.com/MariaDB/server/commit/52a6812595)\
  2016-11-19 13:59:12 +0300
  * Scripts: flag to disable warnings reprinting
* [Revision #be0f586972](https://github.com/MariaDB/server/commit/be0f586972)\
  2016-11-16 13:05:40 +0000
  * Scripts: print warnings fixes
* [Revision #a5feb98c47](https://github.com/MariaDB/server/commit/a5feb98c47)\
  2016-11-13 18:37:03 +0300
  * Scripts: collect and reprint warnings
* [Revision #d54d36c45e](https://github.com/MariaDB/server/commit/d54d36c45e)\
  2016-11-14 06:14:28 +0000
  * IB, SQL: (0.4) COMMIT\_ID-based ordering of transactions
* [Revision #07cc46acea](https://github.com/MariaDB/server/commit/07cc46acea)\
  2016-11-14 20:30:21 +0700
  * Scripts: travis.yml typo fix
* [Revision #618d87e5cb](https://github.com/MariaDB/server/commit/618d87e5cb)\
  2016-11-10 14:34:09 +0300
  * Scripts: debug and release configurations for travis build
* [Revision #1645e97cc9](https://github.com/MariaDB/server/commit/1645e97cc9)\
  2016-11-10 13:47:50 +0300
  * Tests: forgotten foreign.result
* [Revision #20b2719f45](https://github.com/MariaDB/server/commit/20b2719f45)\
  2016-11-08 15:36:20 +0300
  * Misc: foreign check code cleanups
* [Revision #0581c018b7](https://github.com/MariaDB/server/commit/0581c018b7)\
  2016-11-07 22:01:29 +0300
  * SQL: NULL instead of optimized fields in versioned queries
* [Revision #19641ce89f](https://github.com/MariaDB/server/commit/19641ce89f)\
  2016-11-04 22:30:56 +0000
  * IB: production compilation fix
* [Revision #d65bc82909](https://github.com/MariaDB/server/commit/d65bc82909)\
  2016-10-31 12:44:58 +0000
  * Tests: (0.4) TRANSACTION support in queries (#27)
* [Revision #6d89a4a49b](https://github.com/MariaDB/server/commit/6d89a4a49b)\
  2016-10-14 13:25:28 +0000
  * Parser, SQL: (0.4) TRANSACTION support in queries
* [Revision #a22cbc453f](https://github.com/MariaDB/server/commit/a22cbc453f)\
  2016-11-01 19:51:44 +0300
  * IB: (0.4) foreign keys for versioned tables (#58)
* [Revision #012e3e7e4e](https://github.com/MariaDB/server/commit/012e3e7e4e)\
  2016-11-01 14:24:18 +0000
  * Comment: reminder for merging HIDDEN feature (closes #38)
* [Revision #4cfc5dc814](https://github.com/MariaDB/server/commit/4cfc5dc814)\
  2016-10-30 05:59:42 +0000
  * Tests: disabled some tests
* [Revision #3c634602b9](https://github.com/MariaDB/server/commit/3c634602b9)\
  2016-10-29 08:28:17 +0000
  * Parser: SYSTEM\_TIME\_SYM (fixes #67)
* [Revision #7d815be198](https://github.com/MariaDB/server/commit/7d815be198)\
  2016-10-26 14:32:41 +0300
  * SQL: store versioning field flags in EXTRA2
* [Revision #e094228631](https://github.com/MariaDB/server/commit/e094228631)\
  2016-10-20 23:05:55 +0300
  * SQL: hide implicitly added columns from SELECT \*
* [Revision #70168978fc](https://github.com/MariaDB/server/commit/70168978fc)\
  2016-10-25 10:42:26 +0000
  * Scripts: Travis-CI for natsys/trunk
* [Revision #5dea51657d](https://github.com/MariaDB/server/commit/5dea51657d)\
  2016-10-20 09:12:41 +0000
  * IB: optimized update for non-versioned fields
* [Revision #01c9d1c97f](https://github.com/MariaDB/server/commit/01c9d1c97f)\
  2016-10-18 16:35:52 +0000
  * SQL: SP idempotency fix
* [Revision #44e581ebfc](https://github.com/MariaDB/server/commit/44e581ebfc)\
  2016-10-18 12:09:27 +0000
  * Tests: removed from main suite
* [Revision #d3b737d910](https://github.com/MariaDB/server/commit/d3b737d910)\
  2016-10-18 09:05:49 +0000
  * Tests: moved to dedicated versioning suite
* [Revision #5cf3dd79fa](https://github.com/MariaDB/server/commit/5cf3dd79fa)\
  2016-10-18 08:07:22 +0000
  * SQL: JOIN + WHERE in SP
* [Revision #4c5a2e504d](https://github.com/MariaDB/server/commit/4c5a2e504d)\
  2016-10-15 14:15:28 +0000
  * Tests: create, select\_pkeycache, select\_jcl6 results
* [Revision #0a8fd20ad6](https://github.com/MariaDB/server/commit/0a8fd20ad6)\
  2016-10-15 08:21:11 +0000
  * SQL: NOT NULL for implicit fields (fixes #46)
* [Revision #31e296c558](https://github.com/MariaDB/server/commit/31e296c558)\
  2016-10-15 07:46:11 +0000
  * IB: wrong 'interface consistency' (fixes #47)
* [Revision #a03da4fa78](https://github.com/MariaDB/server/commit/a03da4fa78)\
  2016-10-15 00:54:32 +0300
  * Style: removed unused header, other small fixes
* [Revision #2edb6fda2a](https://github.com/MariaDB/server/commit/2edb6fda2a)\
  2016-10-14 20:33:41 +0000
  * Tests: select.test fix
* [Revision #27944ef9b4](https://github.com/MariaDB/server/commit/27944ef9b4)\
  2016-10-14 23:08:37 +0300
  * enable update\_multi.test
* [Revision #2c4527fb94](https://github.com/MariaDB/server/commit/2c4527fb94)\
  2016-10-14 18:18:35 +0300
  * Tests: added tests for versioned tables with implicitly added fields
* [Revision #6ccae7369b](https://github.com/MariaDB/server/commit/6ccae7369b)\
  2016-10-14 07:24:59 +0000
  * SQL: fixed LEFT JOIN, RIGHT JOIN
* [Revision #82114170bc](https://github.com/MariaDB/server/commit/82114170bc)\
  2016-10-13 20:23:27 +0000
  * SQL: implicit fields for IB tables + misc cleanups
* [Revision #a9a56b2355](https://github.com/MariaDB/server/commit/a9a56b2355)\
  2016-10-02 12:35:50 +0300
  * SQL: 0.3 per column versioning syntax, .frm, optimized updates and tests
* [Revision #2db17e6624](https://github.com/MariaDB/server/commit/2db17e6624)\
  2016-10-13 13:30:22 +0000
  * Parser: versioned JOIN fix
* [Revision #5c4473dc74](https://github.com/MariaDB/server/commit/5c4473dc74)\
  2016-10-12 15:01:42 +0000
  * IB: misc fix
* [Revision #3579f5f9f7](https://github.com/MariaDB/server/commit/3579f5f9f7)\
  2016-10-04 09:36:47 +0000
  * Tests: insert, update, delete, insert\_select, insert\_update, multi\_update
* [Revision #53a892fcfd](https://github.com/MariaDB/server/commit/53a892fcfd)\
  2016-09-30 13:15:08 +0000
  * IB: 0.2 part IV
* [Revision #f13bf7178d](https://github.com/MariaDB/server/commit/f13bf7178d)\
  2016-10-11 06:14:45 +0000
  * Parser: expressions instead string literals in TIMESTAMP clauses
* [Revision #c6b029d7cd](https://github.com/MariaDB/server/commit/c6b029d7cd)\
  2016-10-09 15:34:42 +0000
  * Tests: dependency on xtradb for some tests
* [Revision #a7df730636](https://github.com/MariaDB/server/commit/a7df730636)\
  2016-10-04 15:56:06 +0300
  * SQL: fix timestamp type for generated fields
* [Revision #78c5d1d79c](https://github.com/MariaDB/server/commit/78c5d1d79c)\
  2016-10-03 07:03:04 +0000
  * SQL: respect signed in set\_max(), is\_max()
* [Revision #a72259353a](https://github.com/MariaDB/server/commit/a72259353a)\
  2016-10-03 02:48:08 +0000
  * Cleanup: garbage hunk
* [Revision #1ec7dbe176](https://github.com/MariaDB/server/commit/1ec7dbe176)\
  2016-09-29 11:12:46 +0000
  * IB: 0.2 part III
* [Revision #23f4e40839](https://github.com/MariaDB/server/commit/23f4e40839)\
  2016-09-26 08:24:39 +0000
  * Tests: insert, update, delete for VTQ
* [Revision #3b64fed504](https://github.com/MariaDB/server/commit/3b64fed504)\
  2016-09-28 08:56:02 +0000
  * Style: renamed prepare\_keys\_for\_sys\_ver()
* [Revision #bdb12d1499](https://github.com/MariaDB/server/commit/bdb12d1499)\
  2016-09-26 08:37:53 +0000
  * IB: 0.2 part II
* [Revision #002a1bd076](https://github.com/MariaDB/server/commit/002a1bd076)\
  2016-09-26 05:55:13 +0000
  * Scripts: use InnoDB in tests, XtraDB disabled
* [Revision #7deb6cb39e](https://github.com/MariaDB/server/commit/7deb6cb39e)\
  2016-09-24 09:36:57 +0000
  * Scripts: WITH\_INNOBASE\_STORAGE\_ENGINE fix 2 (590af2a4fda6e76b12b58b514099af408dcc40df)
* [Revision #87507451e7](https://github.com/MariaDB/server/commit/87507451e7)\
  2016-09-23 16:01:14 +0000
  * SQL: fractions in I\_S TIMESTAMP fields
* [Revision #9186cae449](https://github.com/MariaDB/server/commit/9186cae449)\
  2016-09-23 18:03:02 +0300
  * Style: related to DBUG\_ASSERT usage
* [Revision #84e1971128](https://github.com/MariaDB/server/commit/84e1971128)\
  2016-09-22 05:56:34 +0000
  * IB: 0.2 part I
* [Revision #bd0b21d22c](https://github.com/MariaDB/server/commit/bd0b21d22c)\
  2016-09-22 15:03:05 +0300
  * SQL: fix for lost code in debug macros
* [Revision #d8c8d7b946](https://github.com/MariaDB/server/commit/d8c8d7b946)\
  2016-09-21 23:30:52 +0300
  * added implicitly generated fields in versioned tables support and refactored code a bit
* [Revision #013345d119](https://github.com/MariaDB/server/commit/013345d119)\
  2016-09-18 04:43:05 +0000
  * vers\_update\_fields: assert instead of return
* [Revision #8936abcd87](https://github.com/MariaDB/server/commit/8936abcd87)\
  2016-09-17 14:35:48 +0000
  * Delete: code duplication fix
* [Revision #8f5f4c2160](https://github.com/MariaDB/server/commit/8f5f4c2160)\
  2016-09-16 16:55:58 +0000
  * Scripts: WITH\_INNOBASE\_STORAGE\_ENGINE fix
* [Revision #be6f2d302c](https://github.com/MariaDB/server/commit/be6f2d302c)\
  2016-06-19 07:38:28 +0100
  * 0.1: SQL-level System Versioning
* [Revision #14bdfa8541](https://github.com/MariaDB/server/commit/14bdfa8541)\
  2016-09-02 19:03:36 +0200
  * Scripts: .gitignore
* [Revision #cc3c63cbae](https://github.com/MariaDB/server/commit/cc3c63cbae)\
  2016-11-08 21:57:22 +0300
  * Scripts: Ninja build system fix

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
