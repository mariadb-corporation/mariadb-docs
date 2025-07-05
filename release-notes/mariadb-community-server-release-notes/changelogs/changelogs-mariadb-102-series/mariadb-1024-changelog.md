# MariaDB 10.2.4 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.4)[Release Notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md)[Changelog](mariadb-1024-changelog.md)[Overview of 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)

**Release date:** 17 Feb 2017

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #34bbc76f1c](https://github.com/MariaDB/server/commit/34bbc76f1c)\
  2017-02-16 09:18:46 +0200
  * Simplify a [WL#6494](https://askmonty.org/worklog/?tid=6494)/[WL#7142](https://askmonty.org/worklog/?tid=7142) test.
* [Revision #7a5288015c](https://github.com/MariaDB/server/commit/7a5288015c)\
  2017-02-16 09:16:11 +0200
  * [MDEV-12072](https://jira.mariadb.org/browse/MDEV-12072) Do not unnecessarily construct rec\_printer objects
* [Revision #37925c6ccc](https://github.com/MariaDB/server/commit/37925c6ccc)\
  2017-02-15 22:41:45 -0800
  * Fixed bug [MDEV-9924](https://jira.mariadb.org/browse/MDEV-9924).
* [Revision #e688d81444](https://github.com/MariaDB/server/commit/e688d81444)\
  2017-02-14 07:18:55 -0800
  * [MDEV-10694](https://jira.mariadb.org/browse/MDEV-10694) - SIGFPE and/or huge memory allocation in maria\_create ...
* [Revision #24911cee4e](https://github.com/MariaDB/server/commit/24911cee4e)\
  2017-02-15 14:08:03 +0200
  * [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) can now start from MySQL 5.7 data directory
* [Revision #eb54d86b58](https://github.com/MariaDB/server/commit/eb54d86b58)\
  2017-02-15 08:53:25 +0200
  * [MDEV-10700](https://jira.mariadb.org/browse/MDEV-10700): 10.2.2 windowing function returns incorrect result
* [Revision #d06a44e027](https://github.com/MariaDB/server/commit/d06a44e027)\
  2017-02-15 08:43:39 +0200
  * [MDEV-11868](https://jira.mariadb.org/browse/MDEV-11868): min ( distinct ) over ( ) returns wrong value
* [Revision #88ddb1ea4e](https://github.com/MariaDB/server/commit/88ddb1ea4e)\
  2017-02-14 22:40:00 +0200
  * [MDEV-11697](https://jira.mariadb.org/browse/MDEV-11697): Lead Window Function Returns Incorrect Results
* [Revision #d474642254](https://github.com/MariaDB/server/commit/d474642254)\
  2017-02-14 18:31:30 +0200
  * [MDEV-10092](https://jira.mariadb.org/browse/MDEV-10092): Server crashes in ha\_heap::rnd\_pos / Table\_read\_cursor::get\_next
* [Revision #9fe9fb68ac](https://github.com/MariaDB/server/commit/9fe9fb68ac)\
  2017-02-14 14:02:29 +0200
  * [MDEV-10859](https://jira.mariadb.org/browse/MDEV-10859): Wrong result of aggregate window function in query with HAVING and no ORDER BY
* [Revision #a90066b1c7](https://github.com/MariaDB/server/commit/a90066b1c7)\
  2017-02-15 13:45:14 +0200
  * [MDEV-11641](https://jira.mariadb.org/browse/MDEV-11641) innobase\_get\_stmt\_safe() does not copy the last byte of thd->query\_string
* [Revision #703d0985ee](https://github.com/MariaDB/server/commit/703d0985ee)\
  2017-02-15 08:57:43 +0200
  * Fix some InnoDB memory leaks.
* [Revision #2af28a363c](https://github.com/MariaDB/server/commit/2af28a363c)\
  2017-02-10 12:11:42 +0200
  * [MDEV-11782](https://jira.mariadb.org/browse/MDEV-11782): Redefine the innodb\_encrypt\_log format
* [Revision #743ac7c2d0](https://github.com/MariaDB/server/commit/743ac7c2d0)\
  2017-02-14 11:13:24 +0200
  * [MDEV-12061](https://jira.mariadb.org/browse/MDEV-12061) Allow innodb\_log\_files\_in\_group=1
* [Revision #3d85292afd](https://github.com/MariaDB/server/commit/3d85292afd)\
  2017-02-14 17:28:59 +0100
  * sporadic failures of rpl.rpl\_binlog\_errors
* [Revision #96d097a7fa](https://github.com/MariaDB/server/commit/96d097a7fa)\
  2017-02-14 16:45:51 +0100
  * sporadic failures of main.default\_debug
* [Revision #41f42dff06](https://github.com/MariaDB/server/commit/41f42dff06)\
  2017-02-14 15:30:45 +0100
  * cleanup: mtr startup warning
* [Revision #6f6d0531dc](https://github.com/MariaDB/server/commit/6f6d0531dc)\
  2017-02-14 11:11:47 +0100
  * [MDEV-11439](https://jira.mariadb.org/browse/MDEV-11439) No data type JSON, but CAST(something AS JSON) pretends to work
* [Revision #e0fa2ce40f](https://github.com/MariaDB/server/commit/e0fa2ce40f)\
  2017-02-14 18:04:35 +0100
  * bugfix: uninitialized variable
* [Revision #8877f1c325](https://github.com/MariaDB/server/commit/8877f1c325)\
  2017-02-14 18:07:42 +0100
  * [MDEV-12056](https://jira.mariadb.org/browse/MDEV-12056) mysql\_config outputs non-existing mysqlclient
* [Revision #f76d5fefb8](https://github.com/MariaDB/server/commit/f76d5fefb8)\
  2017-02-14 17:51:03 +0400
  * [MDEV-11439](https://jira.mariadb.org/browse/MDEV-11439) No data type JSON, but CAST(something AS JSON) pretends to work.
* [Revision #2bf07556e8](https://github.com/MariaDB/server/commit/2bf07556e8)\
  2017-02-14 10:53:17 +0200
  * Post-push fix for [MDEV-12057](https://jira.mariadb.org/browse/MDEV-12057).
* [Revision #1b4b4f6887](https://github.com/MariaDB/server/commit/1b4b4f6887)\
  2017-02-13 14:06:01 +0200
  * [MDEV-12057](https://jira.mariadb.org/browse/MDEV-12057) Embedded server shutdown hangs in InnoDB
* [Revision #d731ce21a7](https://github.com/MariaDB/server/commit/d731ce21a7)\
  2017-02-13 14:40:51 +0200
  * [MDEV-11170](https://jira.mariadb.org/browse/MDEV-11170): [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) cannot start on MySQL 5.7 datadir
* [Revision #5ab93737be](https://github.com/MariaDB/server/commit/5ab93737be)\
  2017-02-13 03:15:33 +0200
  * [MDEV-11170](https://jira.mariadb.org/browse/MDEV-11170): [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) cannot start on MySQL 5.7 datadir
* [Revision #dc90e24978](https://github.com/MariaDB/server/commit/dc90e24978)\
  2017-02-10 12:46:44 +0200
  * Define a helper class to allow for saving sql\_mode using RAII
* [Revision #bdca350f59](https://github.com/MariaDB/server/commit/bdca350f59)\
  2017-02-10 12:39:10 +0200
  * Allow READ\_RECORD to make use of RAII and free itself on destruction
* [Revision #5bf338435a](https://github.com/MariaDB/server/commit/5bf338435a)\
  2017-02-07 17:16:20 +0200
  * [MDEV-11746](https://jira.mariadb.org/browse/MDEV-11746): Wrong result upon using FIRST\_VALUE with a window frame
* [Revision #57341852b5](https://github.com/MariaDB/server/commit/57341852b5)\
  2017-02-07 16:49:41 +0200
  * [MDEV-11746](https://jira.mariadb.org/browse/MDEV-11746): Wrong result upon using FIRST\_VALUE with a window frame
* [Revision #f675eab7dc](https://github.com/MariaDB/server/commit/f675eab7dc)\
  2017-02-07 14:02:25 +0200
  * [MDEV-10122](https://jira.mariadb.org/browse/MDEV-10122): MariaDB does not support group functions in some contexts where MySQL does
* [Revision #fdfdea40f1](https://github.com/MariaDB/server/commit/fdfdea40f1)\
  2016-12-12 02:57:07 +0200
  * [MDEV-11170](https://jira.mariadb.org/browse/MDEV-11170): [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) cannot start on MySQL 5.7 datadir:
* [Revision #e1f0f0dd06](https://github.com/MariaDB/server/commit/e1f0f0dd06)\
  2017-02-13 18:37:06 +0100
  * Revert "[MDEV-11439](https://jira.mariadb.org/browse/MDEV-11439) No data type JSON, but CAST(something AS JSON) pretends to work"
* [Revision #1f372cf1de](https://github.com/MariaDB/server/commit/1f372cf1de)\
  2017-02-13 18:07:59 +0100
  * [MDEV-11439](https://jira.mariadb.org/browse/MDEV-11439) No data type JSON, but CAST(something AS JSON) pretends to work
* [Revision #87075e7f87](https://github.com/MariaDB/server/commit/87075e7f87)\
  2017-02-09 17:43:14 +0100
  * [MDEV-11704](https://jira.mariadb.org/browse/MDEV-11704) InnoDB: Failing assertion: dfield\_is\_null(dfield2) || dfield2->data
* [Revision #239790d92f](https://github.com/MariaDB/server/commit/239790d92f)\
  2017-02-09 14:15:10 +0100
  * [MDEV-11604](https://jira.mariadb.org/browse/MDEV-11604) Assertion \`!check\_datetime\_range(ltime)' failed in TIME\_to\_longlong\_datetime\_packed
* [Revision #1afb11074e](https://github.com/MariaDB/server/commit/1afb11074e)\
  2017-02-09 12:06:15 +0100
  * [MDEV-11582](https://jira.mariadb.org/browse/MDEV-11582) InnoDB: Failing assertion: !((field)->vcol\_info && !(field)->stored\_in\_db())
* [Revision #ca503e830b](https://github.com/MariaDB/server/commit/ca503e830b)\
  2017-02-09 12:04:09 +0100
  * mtr: make sphinx skipping a bit less verbose
* [Revision #0df39e6037](https://github.com/MariaDB/server/commit/0df39e6037)\
  2017-02-08 20:00:39 +0100
  * bugfix: uninit variable
* [Revision #8d99166c69](https://github.com/MariaDB/server/commit/8d99166c69)\
  2017-02-06 23:52:47 +0100
  * [MDEV-11640](https://jira.mariadb.org/browse/MDEV-11640) gcol.gcol\_select\_myisam fails in buildbot on Power
* [Revision #0e5230e12d](https://github.com/MariaDB/server/commit/0e5230e12d)\
  2017-02-06 23:36:39 +0100
  * support keyread in READ\_RECORD
* [Revision #1913daf42c](https://github.com/MariaDB/server/commit/1913daf42c)\
  2017-02-04 19:58:32 +0100
  * bugfix: disable ICP in InnoDB for indexes on virtual columns
* [Revision #01dd355635](https://github.com/MariaDB/server/commit/01dd355635)\
  2017-02-05 13:00:12 +0100
  * cleanup: make a couple of tests more robust
* [Revision #cff144a8ea](https://github.com/MariaDB/server/commit/cff144a8ea)\
  2017-02-04 19:17:42 +0100
  * cleanup: handler::key\_read
* [Revision #dafb507e3e](https://github.com/MariaDB/server/commit/dafb507e3e)\
  2017-02-03 19:09:19 +0100
  * find\_all\_keys: add an assert, remove current\_thd
* [Revision #e46c42217f](https://github.com/MariaDB/server/commit/e46c42217f)\
  2017-02-02 00:47:07 +0100
  * cleanup: TABLE::mark\_columns\_used\_by\_index()
* [Revision #460ff39871](https://github.com/MariaDB/server/commit/460ff39871)\
  2017-02-02 12:44:01 +0100
  * bugfix: don't calculate vcols if doing keyread
* [Revision #3cae225b0f](https://github.com/MariaDB/server/commit/3cae225b0f)\
  2017-02-01 18:00:16 +0100
  * cleanup: remove TABLE::add\_read\_columns\_used\_by\_index
* [Revision #9fa6589f64](https://github.com/MariaDB/server/commit/9fa6589f64)\
  2017-02-02 19:15:11 +0100
  * bugfix: TABLE::mark\_columns\_used\_by\_index\_no\_reset
* [Revision #4dd7e11332](https://github.com/MariaDB/server/commit/4dd7e11332)\
  2017-02-01 19:59:24 +0100
  * cleanup: mark\_columns\_used\_by\_index\_no\_reset in handler::get\_auto\_increment
* [Revision #bf8f70a47c](https://github.com/MariaDB/server/commit/bf8f70a47c)\
  2017-02-01 17:20:35 +0100
  * cleanup: mark\_columns\_used\_by\_index\_no\_reset in opt\_range.cc
* [Revision #0254f1a6e0](https://github.com/MariaDB/server/commit/0254f1a6e0)\
  2017-02-02 15:49:31 +0100
  * bugfix: TABLE::mark\_columns\_used\_by\_index
* [Revision #5d7607f340](https://github.com/MariaDB/server/commit/5d7607f340)\
  2017-02-01 16:41:17 +0100
  * cleanup: style fixes, sql\_join\_cache.cc
* [Revision #8246b0ac50](https://github.com/MariaDB/server/commit/8246b0ac50)\
  2017-01-30 09:28:05 +0100
  * cleanup: TABLE::non\_determinstic\_insert
* [Revision #6c4144a468](https://github.com/MariaDB/server/commit/6c4144a468)\
  2017-01-30 01:01:28 +0100
  * InnoDB: suppress posix\_fallocate() failure errors when EINVAL
* [Revision #ef0db6bfd1](https://github.com/MariaDB/server/commit/ef0db6bfd1)\
  2017-01-29 12:02:56 +0100
  * fix rpl\_binlog\_errors test not to leave dbug enabled
* [Revision #d2f84ab978](https://github.com/MariaDB/server/commit/d2f84ab978)\
  2017-01-24 22:57:08 +0100
  * [MDEV-10352](https://jira.mariadb.org/browse/MDEV-10352) Server crashes in Field::set\_default on CREATE TABLE
* [Revision #b6a3917b05](https://github.com/MariaDB/server/commit/b6a3917b05)\
  2017-01-24 00:01:25 +0100
  * [MDEV-11750](https://jira.mariadb.org/browse/MDEV-11750) Assertion \`vfield' failed in TABLE::update\_virtual\_fields after crash recovery on corrupted MyISAM table
* [Revision #29ed440d44](https://github.com/MariaDB/server/commit/29ed440d44)\
  2017-01-22 17:14:36 +0100
  * [MDEV-11836](https://jira.mariadb.org/browse/MDEV-11836) vcol.vcol\_keys\_myisam fails in buildbot and outside
* [Revision #4cf4b61b24](https://github.com/MariaDB/server/commit/4cf4b61b24)\
  2017-01-23 12:26:29 +0100
  * oqgraph: remove redundant update\_virtual\_fields() calls
* [Revision #eda2ebefba](https://github.com/MariaDB/server/commit/eda2ebefba)\
  2017-01-18 20:40:15 +0100
  * [MDEV-11784](https://jira.mariadb.org/browse/MDEV-11784) View is created with invalid definition which causes ERROR 1241 (21000): Operand should contain 1 column(s)
* [Revision #cf00393378](https://github.com/MariaDB/server/commit/cf00393378)\
  2017-01-03 14:55:29 +0100
  * Race condition in DEFAULT() with expressions
* [Revision #cd4dd2b62d](https://github.com/MariaDB/server/commit/cd4dd2b62d)\
  2016-12-30 13:03:47 +0100
  * [MDEV-10201](https://jira.mariadb.org/browse/MDEV-10201) Bad results for CREATE TABLE t1 (a INT DEFAULT b, b INT DEFAULT 4)
* [Revision #588eca31e3](https://github.com/MariaDB/server/commit/588eca31e3)\
  2017-02-13 11:40:19 +0200
  * Post-fix for [MDEV-12050](https://jira.mariadb.org/browse/MDEV-12050) Remove unused InnoDB Memcached hooks
* [Revision #a45866c6db](https://github.com/MariaDB/server/commit/a45866c6db)\
  2017-02-11 17:45:36 +0200
  * [MDEV-12050](https://jira.mariadb.org/browse/MDEV-12050) Remove unused InnoDB Memcached hooks
* [Revision #3272a19741](https://github.com/MariaDB/server/commit/3272a19741)\
  2017-02-10 20:26:02 +0200
  * [MDEV-11782](https://jira.mariadb.org/browse/MDEV-11782) preparation: Add separate code for validating the 10.1 redo log.
* [Revision #96c4b9d49f](https://github.com/MariaDB/server/commit/96c4b9d49f)\
  2017-02-10 19:32:03 +0200
  * [MDEV-11782](https://jira.mariadb.org/browse/MDEV-11782) preparation: Remove recv\_sys\_t::last\_block.
* [Revision #412ee0330c](https://github.com/MariaDB/server/commit/412ee0330c)\
  2017-02-10 20:06:24 +0200
  * Fix a memory leak on aborted InnoDB startup.
* [Revision #d35aea5407](https://github.com/MariaDB/server/commit/d35aea5407)\
  2017-02-12 15:50:14 -0800
  * Fixed bugs [MDEV-12051](https://jira.mariadb.org/browse/MDEV-12051), [MDEV-10885](https://jira.mariadb.org/browse/MDEV-10885).
* [Revision #f04efa839d](https://github.com/MariaDB/server/commit/f04efa839d)\
  2017-02-11 11:16:36 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Fix for ctype\_gbk\_export\_import.test
* Merge [Revision #f3914d10b6](https://github.com/MariaDB/server/commit/f3914d10b6) 2017-02-11 09:45:34 +0100 - Merge branch 'bb-10.2-serg-merge' into 10.2
* Merge [Revision #2195bb4e41](https://github.com/MariaDB/server/commit/2195bb4e41) 2017-02-10 17:01:45 +0100 - Merge branch '10.1' into 10.2
* [Revision #bc4686f0f4](https://github.com/MariaDB/server/commit/bc4686f0f4)\
  2017-01-30 14:50:58 -0500
  * Minor test improvement
* [Revision #cd8482c19e](https://github.com/MariaDB/server/commit/cd8482c19e)\
  2017-01-30 14:49:44 -0500
  * [MDEV-11945](https://jira.mariadb.org/browse/MDEV-11945): Fix description for "max\_statement\_time" in --help
* [Revision #aa9db4c162](https://github.com/MariaDB/server/commit/aa9db4c162)\
  2017-01-29 13:21:38 -0500
  * [MDEV-11817](https://jira.mariadb.org/browse/MDEV-11817): Altering a table with more rows than ..
* [Revision #17cc619847](https://github.com/MariaDB/server/commit/17cc619847)\
  2017-01-31 15:42:52 +0200
  * [MDEV-11671](https://jira.mariadb.org/browse/MDEV-11671): Duplicated \[NOTE] output for changed innodb\_page\_size
* [Revision #41997d148d](https://github.com/MariaDB/server/commit/41997d148d)\
  2017-01-27 11:15:45 +0530
  * [MDEV-10812](https://jira.mariadb.org/browse/MDEV-10812) WSREP causes responses being sent to protocol commands that must not send a response
* [Revision #bb1e8e4367](https://github.com/MariaDB/server/commit/bb1e8e4367)\
  2017-01-31 10:02:37 +0530
  * [MDEV-4774](https://jira.mariadb.org/browse/MDEV-4774)- Fix tests cases
* Merge [Revision #1ebfeceeb2](https://github.com/MariaDB/server/commit/1ebfeceeb2) 2017-01-27 16:14:20 +0200 - Merge 10.0 into 10.1 (test-only changes)
* [Revision #4e82aaab2f](https://github.com/MariaDB/server/commit/4e82aaab2f)\
  2017-01-27 16:03:56 +0200
  * Clean up a few tests that kill the server.
* [Revision #ea9caea87e](https://github.com/MariaDB/server/commit/ea9caea87e)\
  2017-01-27 12:17:03 +0200
  * [MDEV-11814](https://jira.mariadb.org/browse/MDEV-11814) test fix
* [Revision #732672c304](https://github.com/MariaDB/server/commit/732672c304)\
  2016-12-05 15:25:59 +0200
  * [MDEV-11233](https://jira.mariadb.org/browse/MDEV-11233) CREATE FULLTEXT INDEX with a token longer than 127 bytes crashes server
* Merge [Revision #f1f8ebc325](https://github.com/MariaDB/server/commit/f1f8ebc325) 2017-01-26 23:40:11 +0200 - Merge 10.0 into 10.1
* [Revision #afb461587c](https://github.com/MariaDB/server/commit/afb461587c)\
  2017-01-26 14:05:00 +0200
  * [MDEV-11915](https://jira.mariadb.org/browse/MDEV-11915) Detect InnoDB system tablespace size mismatch early
* [Revision #49fe9bad01](https://github.com/MariaDB/server/commit/49fe9bad01)\
  2017-01-25 15:11:46 +0200
  * [MDEV-11814](https://jira.mariadb.org/browse/MDEV-11814) Refuse innodb\_read\_only startup if crash recovery is needed
* [Revision #8725b35d89](https://github.com/MariaDB/server/commit/8725b35d89)\
  2017-01-24 01:25:50 +0530
  * [MDEV-11108](https://jira.mariadb.org/browse/MDEV-11108): Assertion \`uniq\_tuple\_length\_arg <= table->file->max\_key\_length()' failed in SJ\_TMP\_TABLE::create\_sj\_weedout\_tmp\_table
* [Revision #18ef02b04d](https://github.com/MariaDB/server/commit/18ef02b04d)\
  2017-01-10 10:08:04 +0530
  * [MDEV-4774](https://jira.mariadb.org/browse/MDEV-4774) Strangeness with max\_binlog\_stmt\_cache\_size Settings
* [Revision #fbcdc3437c](https://github.com/MariaDB/server/commit/fbcdc3437c)\
  2017-01-17 22:08:19 +0100
  * connect zip bug fix
* Merge [Revision #6fbfb4c83c](https://github.com/MariaDB/server/commit/6fbfb4c83c) 2017-01-26 16:19:29 +0200 - Merge pull request #298 from iangilfillan/10.1
* [Revision #ee3febae04](https://github.com/MariaDB/server/commit/ee3febae04)\
  2017-01-26 13:51:03 +0200
  * Minor typo
* Merge [Revision #4113f1a7b7](https://github.com/MariaDB/server/commit/4113f1a7b7) 2017-01-26 02:57:12 +0300 - Merge branch 'grooverdan-10.1-[MDEV-11866](https://jira.mariadb.org/browse/MDEV-11866)-ANALYZE-FORMAT=JSON-volatility-normalise' into 10.1
* Merge [Revision #9394bc06d8](https://github.com/MariaDB/server/commit/9394bc06d8) 2017-01-26 02:56:49 +0300 - Merge branch '10.1-[MDEV-11866](https://jira.mariadb.org/browse/MDEV-11866)-ANALYZE-FORMAT=JSON-volatility-normalise' of git:github.com/grooverdan/mariadb-server into grooverdan-10.1-[MDEV-11866](https://jira.mariadb.org/browse/MDEV-11866)-ANALYZE-FORMAT=JSON-volatility-normalise
* [Revision #10b1f4dd09](https://github.com/MariaDB/server/commit/10b1f4dd09)\
  2017-01-23 13:32:57 +1100
  * [MDEV-11866](https://jira.mariadb.org/browse/MDEV-11866): ANALYZE FORMAT=JSON not predicatable for r\_total\_time\_ms/r\_buffer\_size
* [Revision #86ca1357b0](https://github.com/MariaDB/server/commit/86ca1357b0)\
  2017-01-24 19:26:16 +0530
  * Revert "[MDEV-7409](https://jira.mariadb.org/browse/MDEV-7409) On RBR, extend the PROCESSLIST info to include at least the name of the recently used table"
* [Revision #15f46d5174](https://github.com/MariaDB/server/commit/15f46d5174)\
  2017-01-23 22:27:42 +0530
  * [MDEV-7409](https://jira.mariadb.org/browse/MDEV-7409) On RBR, extend the PROCESSLIST info to include at least the name of the recently used table
* [Revision #b7b4c332c0](https://github.com/MariaDB/server/commit/b7b4c332c0)\
  2017-01-22 08:44:04 +0200
  * [MDEV-11614](https://jira.mariadb.org/browse/MDEV-11614): Syslog messages: "InnoDB: Log sequence number
* [Revision #213fc700b6](https://github.com/MariaDB/server/commit/213fc700b6)\
  2017-01-21 00:56:33 +0530
  * [MDEV-10232](https://jira.mariadb.org/browse/MDEV-10232): Scalar result of subquery changes after adding an outer select stmt
* [Revision #8a4d605500](https://github.com/MariaDB/server/commit/8a4d605500)\
  2017-01-19 12:20:54 +0200
  * [MDEV-11838](https://jira.mariadb.org/browse/MDEV-11838): Innodb-encryption-algorithm default should be != none
* [Revision #dc557ca817](https://github.com/MariaDB/server/commit/dc557ca817)\
  2017-01-19 08:19:08 +0200
  * [MDEV-11835](https://jira.mariadb.org/browse/MDEV-11835): InnoDB: Failing assertion: free\_slot != NULL on
* [Revision #a14638581b](https://github.com/MariaDB/server/commit/a14638581b)\
  2017-01-18 08:39:18 -0500
  * bump the VERSION
* [Revision #5593458062](https://github.com/MariaDB/server/commit/5593458062)\
  2017-02-10 17:20:46 -0800
  * Fixed bug [MDEV-12015](https://jira.mariadb.org/browse/MDEV-12015).
* [Revision #1b4f694adf](https://github.com/MariaDB/server/commit/1b4f694adf)\
  2017-02-10 14:17:19 +0000
  * [MDEV-10291](https://jira.mariadb.org/browse/MDEV-10291) : Fix race condition in bootstrap
* [Revision #6f42c3c5a4](https://github.com/MariaDB/server/commit/6f42c3c5a4)\
  2017-02-09 20:42:05 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Fix for mroonga 32-bit test failures.
* [Revision #c513c4cbf5](https://github.com/MariaDB/server/commit/c513c4cbf5)\
  2017-02-06 03:13:36 +0200
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Additional test fixes
* [Revision #c0209f8736](https://github.com/MariaDB/server/commit/c0209f8736)\
  2017-02-08 15:35:33 -0500
  * [MDEV-11908](https://jira.mariadb.org/browse/MDEV-11908): New default configuration produces warnings about itself upon startup
* [Revision #616f4a773a](https://github.com/MariaDB/server/commit/616f4a773a)\
  2017-02-08 15:28:52 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Reset sync\_binlog back to 0
* [Revision #8b2e642aa2](https://github.com/MariaDB/server/commit/8b2e642aa2)\
  2017-02-08 15:28:00 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Update tests to adapt to the new default sql\_mode
* [Revision #f556aa9b5f](https://github.com/MariaDB/server/commit/f556aa9b5f)\
  2017-01-31 12:34:38 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): SET shouldn't fail for invalid values in strict trans mode
* [Revision #04b52a0745](https://github.com/MariaDB/server/commit/04b52a0745)\
  2017-01-31 12:33:13 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Part 2
* [Revision #f8aa54f1bc](https://github.com/MariaDB/server/commit/f8aa54f1bc)\
  2017-01-11 09:05:36 -0500
  * [MDEV-11685](https://jira.mariadb.org/browse/MDEV-11685): sql\_mode can't be set with non-ascii connection charset
* [Revision #eaf9c4b54f](https://github.com/MariaDB/server/commit/eaf9c4b54f)\
  2016-12-24 10:58:33 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Disable rpl\_row\_index\_choice ([MDEV-11666](https://jira.mariadb.org/browse/MDEV-11666))
* [Revision #91991c1e2d](https://github.com/MariaDB/server/commit/91991c1e2d)\
  2016-12-21 23:02:51 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Test fixes
* [Revision #3435e8a515](https://github.com/MariaDB/server/commit/3435e8a515)\
  2016-12-19 17:32:45 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Part 1
* [Revision #185d140f19](https://github.com/MariaDB/server/commit/185d140f19)\
  2016-12-19 16:28:19 -0500
  * [MDEV-7635](https://jira.mariadb.org/browse/MDEV-7635): Renamed standards\_compliant\_cte to standard\_compliant\_cte
* [Revision #25f6d1dad7](https://github.com/MariaDB/server/commit/25f6d1dad7)\
  2017-02-09 18:19:03 +0100
  * Unused code removed.
* [Revision #ae3072c0af](https://github.com/MariaDB/server/commit/ae3072c0af)\
  2017-02-09 12:08:57 +0100
  * [MDEV-10554](https://jira.mariadb.org/browse/MDEV-10554): Assertion \`!derived->first\_select()->exclude\_from\_table\_unique\_test || derived->outer\_select()-> exclude\_from\_table\_unique\_test' failed in TABLE\_LIST::set\_check\_merged()
* [Revision #ee51f58236](https://github.com/MariaDB/server/commit/ee51f58236)\
  2016-10-12 18:36:22 +0200
  * [MDEV-10340](https://jira.mariadb.org/browse/MDEV-10340): support COM\_RESET\_CONNECTION
* [Revision #78b5e8d6ca](https://github.com/MariaDB/server/commit/78b5e8d6ca)\
  2017-02-09 19:33:28 -0800
  * Fixed bug [MDEV-11745](https://jira.mariadb.org/browse/MDEV-11745).
* [Revision #766ab17329](https://github.com/MariaDB/server/commit/766ab17329)\
  2017-02-10 01:24:54 +0400
  * [MDEV-11544](https://jira.mariadb.org/browse/MDEV-11544) innodb\_gis.precise fails in buildbot on Power.
* [Revision #25aaecb240](https://github.com/MariaDB/server/commit/25aaecb240)\
  2017-02-10 01:05:27 +0400
  * [MDEV-11858](https://jira.mariadb.org/browse/MDEV-11858) json\_merge() concatenates instead of merging.
* [Revision #3ae038b732](https://github.com/MariaDB/server/commit/3ae038b732)\
  2017-02-09 17:55:58 +0400
  * [MDEV-11857](https://jira.mariadb.org/browse/MDEV-11857) json\_search() shows "Out of memory" with empty key.
* [Revision #777422070a](https://github.com/MariaDB/server/commit/777422070a)\
  2017-02-09 15:57:21 +0200
  * Adjust a test that is not supposed to crash.
* [Revision #ddb284afaa](https://github.com/MariaDB/server/commit/ddb284afaa)\
  2017-01-16 18:47:53 +0100
  * [MDEV-11601](https://jira.mariadb.org/browse/MDEV-11601) Out-of-bounds string access in create\_schema\_table()
* [Revision #5ffbd084f5](https://github.com/MariaDB/server/commit/5ffbd084f5)\
  2017-02-09 16:02:21 +0200
  * Revert an accidental commit to work around [MDEV-11601](https://jira.mariadb.org/browse/MDEV-11601).
* [Revision #0e6968c244](https://github.com/MariaDB/server/commit/0e6968c244)\
  2017-02-09 17:38:53 +0400
  * [MDEV-11857](https://jira.mariadb.org/browse/MDEV-11857) json\_search() shows "Out of memory" with empty key.
* [Revision #66c6188a4b](https://github.com/MariaDB/server/commit/66c6188a4b)\
  2017-02-09 10:04:00 +0200
  * Relax assertions on shutdown after aborted startup.
* [Revision #070a8754c4](https://github.com/MariaDB/server/commit/070a8754c4)\
  2017-02-08 15:42:15 +0200
  * [MDEV-12024](https://jira.mariadb.org/browse/MDEV-12024) InnoDB startup fails to wait for recv\_writer\_thread to finish
* [Revision #bae2fc1f38](https://github.com/MariaDB/server/commit/bae2fc1f38)\
  2017-02-08 12:19:28 +0000
  * More verbose output for the Wix linker (light.exe)
* [Revision #3c411e3ad6](https://github.com/MariaDB/server/commit/3c411e3ad6)\
  2017-02-08 12:48:25 +0200
  * Test fix for [MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076) Persistent AUTO\_INCREMENT for InnoDB
* [Revision #9fa20716b6](https://github.com/MariaDB/server/commit/9fa20716b6)\
  2017-02-08 10:06:18 +0200
  * Remove some more error log spam.
* [Revision #a75633b5bd](https://github.com/MariaDB/server/commit/a75633b5bd)\
  2017-02-02 13:52:33 +0100
  * [MDEV-11681](https://jira.mariadb.org/browse/MDEV-11681): PARTITION BY LIST COLUMNS with default partition: Assertion \`part\_info->num\_list\_values' failed in get\_part\_iter\_for\_interval\_cols\_via\_map
* [Revision #7b27465e10](https://github.com/MariaDB/server/commit/7b27465e10)\
  2017-02-07 15:55:01 +0200
  * [MDEV-11974](https://jira.mariadb.org/browse/MDEV-11974): [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) encryption does not support spatial indexes
* [Revision #163ac07b93](https://github.com/MariaDB/server/commit/163ac07b93)\
  2017-02-08 06:47:39 +0400
  * [MDEV-12020](https://jira.mariadb.org/browse/MDEV-12020) ctype tests are non-deterministic due to missing sorting
* [Revision #abe6aca8d4](https://github.com/MariaDB/server/commit/abe6aca8d4)\
  2017-02-07 17:32:50 +0400
  * [MDEV-11554](https://jira.mariadb.org/browse/MDEV-11554) innodb\_gis.precise fails in buildbot on Power.
* [Revision #92bbf4ad04](https://github.com/MariaDB/server/commit/92bbf4ad04)\
  2017-02-06 18:44:35 +0200
  * [MDEV-11782](https://jira.mariadb.org/browse/MDEV-11782) WIP: Support upgrade from [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md).
* [Revision #b40a1fbc93](https://github.com/MariaDB/server/commit/b40a1fbc93)\
  2017-01-24 10:29:29 +0200
  * [MDEV-11782](https://jira.mariadb.org/browse/MDEV-11782) WIP: Clean up the code, and add a test.
* [Revision #c5fc3a903c](https://github.com/MariaDB/server/commit/c5fc3a903c)\
  2017-02-07 10:57:02 +0200
  * [MDEV-12004](https://jira.mariadb.org/browse/MDEV-12004) InnoDB wrongly thinks that a column is indexed after failed ADD UNIQUE INDEX
* [Revision #2aa47d9849](https://github.com/MariaDB/server/commit/2aa47d9849)\
  2017-01-31 12:25:25 +0200
  * [MDEV-11035](https://jira.mariadb.org/browse/MDEV-11035): Restore removed disallow-writes for Galera
* [Revision #c16c9e8e76](https://github.com/MariaDB/server/commit/c16c9e8e76)\
  2017-02-06 22:12:53 -0800
  * Fixed bug [MDEV-11999](https://jira.mariadb.org/browse/MDEV-11999).
* [Revision #2f00b73a4b](https://github.com/MariaDB/server/commit/2f00b73a4b)\
  2017-02-03 12:25:42 +0200
  * [MDEV-11985](https://jira.mariadb.org/browse/MDEV-11985) Make innodb\_read\_only shutdown more robust
* [Revision #a440d6ed3a](https://github.com/MariaDB/server/commit/a440d6ed3a)\
  2017-02-03 09:50:12 +0200
  * [MDEV-11948](https://jira.mariadb.org/browse/MDEV-11948) innodb.log\_file fails in buildbot on CentOS 5
* [Revision #3534500b87](https://github.com/MariaDB/server/commit/3534500b87)\
  2017-02-03 08:55:36 +0200
  * Test recovery when a .ibd file is a directory.
* [Revision #5a21094a43](https://github.com/MariaDB/server/commit/5a21094a43)\
  2017-02-03 08:32:58 +0200
  * Simplify innodb.innochecksum test.
* [Revision #abf7582112](https://github.com/MariaDB/server/commit/abf7582112)\
  2017-02-06 06:47:48 +0400
  * [MDEV-11557](https://jira.mariadb.org/browse/MDEV-11557) port MySQL-5.7 JSON tests to MariaDB.
* [Revision #e51b015fc3](https://github.com/MariaDB/server/commit/e51b015fc3)\
  2017-02-04 21:51:40 -0800
  * Fixed bug [MDEV-11138](https://jira.mariadb.org/browse/MDEV-11138).
* [Revision #20aae56efa](https://github.com/MariaDB/server/commit/20aae56efa)\
  2017-02-03 15:50:25 -0800
  * Fixed bug [MDEV-10660](https://jira.mariadb.org/browse/MDEV-10660).
* [Revision #bc12d993d7](https://github.com/MariaDB/server/commit/bc12d993d7)\
  2017-02-02 18:17:46 +0200
  * [MDEV-11947](https://jira.mariadb.org/browse/MDEV-11947) InnoDB purge workers fail to shut down
* [Revision #3ebe08204a](https://github.com/MariaDB/server/commit/3ebe08204a)\
  2017-02-02 17:00:27 +0200
  * [MDEV-11782](https://jira.mariadb.org/browse/MDEV-11782) Work-in-progress (test only).
* [Revision #5285504857](https://github.com/MariaDB/server/commit/5285504857)\
  2017-02-02 15:27:59 +0200
  * innodb.log\_corruption: Use the main error log.
* [Revision #fd7accabbb](https://github.com/MariaDB/server/commit/fd7accabbb)\
  2017-02-03 00:10:36 -0800
  * Fixed bug [MDEV-9923](https://jira.mariadb.org/browse/MDEV-9923).
* [Revision #5606f878bf](https://github.com/MariaDB/server/commit/5606f878bf)\
  2017-02-02 17:57:55 -0800
  * Fixed bug [MDEV-11594](https://jira.mariadb.org/browse/MDEV-11594).
* [Revision #d123ed852a](https://github.com/MariaDB/server/commit/d123ed852a)\
  2017-02-02 18:56:15 +0400
  * [MDEV-11938](https://jira.mariadb.org/browse/MDEV-11938) json.json\_no\_table crashes or fails with valgrind warnings in json\_find\_path / Item\_func\_json\_length::val\_int.
* [Revision #650ffcd3a0](https://github.com/MariaDB/server/commit/650ffcd3a0)\
  2017-02-01 15:47:33 +0200
  * Extend the innodb.log\_corruption test.
* [Revision #8481c70ede](https://github.com/MariaDB/server/commit/8481c70ede)\
  2017-02-01 19:15:28 -0800
  * Fixed bug [MDEV-11867](https://jira.mariadb.org/browse/MDEV-11867).
* [Revision #69114862f2](https://github.com/MariaDB/server/commit/69114862f2)\
  2017-02-01 13:08:21 -0800
  * Adjusted more tests after the fix for [MDEV-9976](https://jira.mariadb.org/browse/MDEV-9976).
* [Revision #b0ea044d12](https://github.com/MariaDB/server/commit/b0ea044d12)\
  2017-01-30 15:11:22 -0500
  * Update galera tests to adapt to recent changes in 10.2.
* [Revision #23628d123b](https://github.com/MariaDB/server/commit/23628d123b)\
  2017-02-01 12:14:37 +0100
  * Fix for [MDEV-11174](https://jira.mariadb.org/browse/MDEV-11174): A GCM encrypted ciphertext must contain an authentication tag with AES\_BLOCK\_SIZE length, so we need to check that the length of ciphertext is at least AES\_BLOCK\_SIZE.
* [Revision #e1977712cc](https://github.com/MariaDB/server/commit/e1977712cc)\
  2017-02-01 09:28:13 +0200
  * Clean up a test.
* [Revision #81b7fe9d38](https://github.com/MariaDB/server/commit/81b7fe9d38)\
  2017-01-31 19:43:03 +0200
  * Shut down InnoDB after aborted startup.
* [Revision #774056c825](https://github.com/MariaDB/server/commit/774056c825)\
  2017-01-31 14:20:40 +0200
  * [MDEV-11671](https://jira.mariadb.org/browse/MDEV-11671) Duplicated message for innodb\_page\_size
* [Revision #16bc16f9ba](https://github.com/MariaDB/server/commit/16bc16f9ba)\
  2017-01-31 14:12:14 +0200
  * Actually invoke free() in ut\_allocator::deallocate().
* [Revision #a5d8dc1818](https://github.com/MariaDB/server/commit/a5d8dc1818)\
  2017-01-31 12:06:52 +0200
  * Make the innochecksum tests more robust.
* [Revision #ba8ab6a79c](https://github.com/MariaDB/server/commit/ba8ab6a79c)\
  2017-01-31 16:10:15 -0800
  * Adjusted tests after the fix for bug [MDEV-9976](https://jira.mariadb.org/browse/MDEV-9976).
* [Revision #9073f9fd7d](https://github.com/MariaDB/server/commit/9073f9fd7d)\
  2017-01-31 10:32:59 -0800
  * Fixed bug [MDEV-9976](https://jira.mariadb.org/browse/MDEV-9976).
* [Revision #81c1abe8cf](https://github.com/MariaDB/server/commit/81c1abe8cf)\
  2017-01-30 11:56:23 -0800
  * Fixed bug [MDEV-10875](https://jira.mariadb.org/browse/MDEV-10875).
* [Revision #1d96b09890](https://github.com/MariaDB/server/commit/1d96b09890)\
  2017-01-31 23:41:10 +0400
  * [MDEV-9979](https://jira.mariadb.org/browse/MDEV-9979) Keywords UNBOUNDED, PRECEDING, FOLLOWING, TIES, OTHERS should be non-reserved
* [Revision #642077ea5a](https://github.com/MariaDB/server/commit/642077ea5a)\
  2017-01-30 17:50:54 +0200
  * srv\_get\_active\_thread\_type(): Remove a potential race condition.
* [Revision #7128328d41](https://github.com/MariaDB/server/commit/7128328d41)\
  2017-01-30 18:15:44 +0200
  * Remove a work-around for [MDEV-11689](https://jira.mariadb.org/browse/MDEV-11689).
* [Revision #1293e5e59b](https://github.com/MariaDB/server/commit/1293e5e59b)\
  2017-01-30 17:00:51 +0200
  * Rewrite the innodb.log\_file\_size test with DBUG\_EXECUTE\_IF.
* [Revision #9f918b9cf4](https://github.com/MariaDB/server/commit/9f918b9cf4)\
  2017-01-30 10:39:35 +0100
  * take into account scientific notation of floats in regex\_replace
* [Revision #31a9b3f4c8](https://github.com/MariaDB/server/commit/31a9b3f4c8)\
  2017-01-30 14:10:17 +0200
  * Fix a suppression that did not work on Windows.
* [Revision #8ab806d2f1](https://github.com/MariaDB/server/commit/8ab806d2f1)\
  2017-01-30 11:13:10 +0200
  * Do not remove the master error log file.
* [Revision #2a4881800c](https://github.com/MariaDB/server/commit/2a4881800c)\
  2017-01-30 01:15:30 +0100
  * InnoDB: don't pthread\_join() a thread that wasn't created
* [Revision #9189284ba3](https://github.com/MariaDB/server/commit/9189284ba3)\
  2017-01-29 14:12:08 +0100
  * remove a race-condition prone assertion
* [Revision #3d12587ca4](https://github.com/MariaDB/server/commit/3d12587ca4)\
  2017-01-24 15:14:13 +0100
  * [MDEV-11611](https://jira.mariadb.org/browse/MDEV-11611) fix Ninja build
* [Revision #78712eb52f](https://github.com/MariaDB/server/commit/78712eb52f)\
  2017-01-03 12:23:46 +0100
  * [MDEV-11708](https://jira.mariadb.org/browse/MDEV-11708) cmake -DWITH\_ASAN no longer works
* [Revision #a7d6271cbf](https://github.com/MariaDB/server/commit/a7d6271cbf)\
  2017-01-29 13:49:23 +0100
  * skip innodb.log\_corruption test if no unzip executable is found
* [Revision #abfcdb8fbc](https://github.com/MariaDB/server/commit/abfcdb8fbc)\
  2017-01-28 14:52:19 -0800
  * Fixed bug [MDEV-10773](https://jira.mariadb.org/browse/MDEV-10773).
* [Revision #64b5e94236](https://github.com/MariaDB/server/commit/64b5e94236)\
  2017-01-27 14:26:09 +0100
  * mysqlbinlog memory leaks
* [Revision #30ba310057](https://github.com/MariaDB/server/commit/30ba310057)\
  2017-01-27 18:05:11 +0100
  * cleanup: thd\_destructor\_proxy
* [Revision #2de0e42af5](https://github.com/MariaDB/server/commit/2de0e42af5)\
  2017-01-25 15:11:46 +0200
  * Import and adjust the InnoDB redo log tests from MySQL 5.7.
* [Revision #0f34160d1d](https://github.com/MariaDB/server/commit/0f34160d1d)\
  2017-01-27 16:14:20 +0200
  * Clean up a few tests that kill the server.
* [Revision #3dd6fca774](https://github.com/MariaDB/server/commit/3dd6fca774)\
  2017-01-27 14:17:36 +0200
  * Fix test failure on innodb-trim.
* [Revision #406e113e9a](https://github.com/MariaDB/server/commit/406e113e9a)\
  2017-01-26 14:05:00 +0200
  * [MDEV-11915](https://jira.mariadb.org/browse/MDEV-11915) Detect InnoDB system tablespace size mismatch early
* [Revision #3271da11c4](https://github.com/MariaDB/server/commit/3271da11c4)\
  2017-01-25 15:11:46 +0200
  * [MDEV-11814](https://jira.mariadb.org/browse/MDEV-11814) Refuse innodb\_read\_only startup if crash recovery is needed
* [Revision #8daa87dc06](https://github.com/MariaDB/server/commit/8daa87dc06)\
  2017-01-27 12:21:31 +0200
  * Fix a test.
* [Revision #4ee7174479](https://github.com/MariaDB/server/commit/4ee7174479)\
  2017-01-27 11:26:28 +0200
  * Fix test failure on innodb-trim.
* [Revision #ebdf70db2a](https://github.com/MariaDB/server/commit/ebdf70db2a)\
  2017-01-27 09:13:48 +0200
  * Fix test failure on innodb-wl5522
* [Revision #fea4959a0d](https://github.com/MariaDB/server/commit/fea4959a0d)\
  2017-01-27 09:08:15 +0200
  * Fix test failure on gcol.innodb\_virtual\_basic.
* [Revision #a5f6b4f9fd](https://github.com/MariaDB/server/commit/a5f6b4f9fd)\
  2017-01-26 17:39:15 +0000
  * Fix the code to determine sector size on Windows volume.
* [Revision #def258061b](https://github.com/MariaDB/server/commit/def258061b)\
  2016-11-04 13:00:11 +0000
  * increase default for max threads in the pool to max allowed value (64K) currently
* [Revision #d96ee168a1](https://github.com/MariaDB/server/commit/d96ee168a1)\
  2017-01-26 16:35:05 +0400
  * [MDEV-11557](https://jira.mariadb.org/browse/MDEV-11557) port MySQL-5.7 JSON tests to MariaDB.
* [Revision #71495a1748](https://github.com/MariaDB/server/commit/71495a1748)\
  2017-01-25 10:11:37 +0200
  * [MDEV-11849](https://jira.mariadb.org/browse/MDEV-11849): Fix storage/innobase/\* compile warnings
* [Revision #45f451c769](https://github.com/MariaDB/server/commit/45f451c769)\
  2017-01-20 12:10:13 +0200
  * [MDEV-11850](https://jira.mariadb.org/browse/MDEV-11850): Can't create foreign key referencing a virtual column
* [Revision #c6039a11c6](https://github.com/MariaDB/server/commit/c6039a11c6)\
  2017-01-25 16:38:45 +0200
  * Fix a test.
* [Revision #e92ee13254](https://github.com/MariaDB/server/commit/e92ee13254)\
  2017-01-25 16:05:32 +0200
  * Import and adjust a test from MySQL 5.7.
* [Revision #0b1a40852c](https://github.com/MariaDB/server/commit/0b1a40852c)\
  2017-01-25 15:59:37 +0200
  * Replace fil\_node\_t::is\_open with fil\_node\_t::is\_open().
* [Revision #8afe4faab9](https://github.com/MariaDB/server/commit/8afe4faab9)\
  2017-01-25 15:53:46 +0200
  * Fix fil\_ibd\_open() on Windows.
* [Revision #8531e19771](https://github.com/MariaDB/server/commit/8531e19771)\
  2017-01-25 12:33:39 +0200
  * buf\_page\_t is class on 10.2 not struct.
* [Revision #4b28798f95](https://github.com/MariaDB/server/commit/4b28798f95)\
  2017-01-25 10:04:14 +0200
  * Fix compiler error on x86.
* [Revision #17430a802b](https://github.com/MariaDB/server/commit/17430a802b)\
  2017-01-25 08:43:19 +0200
  * [MDEV-11905](https://jira.mariadb.org/browse/MDEV-11905): encryption.innodb-discard-import test fails
* [Revision #ddc14d8eb7](https://github.com/MariaDB/server/commit/ddc14d8eb7)\
  2017-01-25 07:51:08 +0200
  * [MDEV-10942](https://jira.mariadb.org/browse/MDEV-10942): innodb\_zip.innochecksum\_3, innodb\_zip.innochecksum\_2
* [Revision #84895c3cd7](https://github.com/MariaDB/server/commit/84895c3cd7)\
  2017-01-25 07:39:56 +0200
  * Fix compiler error on x86.
* [Revision #423b7da36f](https://github.com/MariaDB/server/commit/423b7da36f)\
  2017-01-24 13:11:26 -0800
  * Fixed bug [MDEV-11820](https://jira.mariadb.org/browse/MDEV-11820).
* [Revision #35760c0000](https://github.com/MariaDB/server/commit/35760c0000)\
  2017-01-25 00:13:15 +0400
  * [MDEV-11557](https://jira.mariadb.org/browse/MDEV-11557) Port MySQL-5.7 JSON tests to MariaDB.
* [Revision #1782102d97](https://github.com/MariaDB/server/commit/1782102d97)\
  2017-01-24 22:39:55 +0400
  * [MDEV-11042](https://jira.mariadb.org/browse/MDEV-11042) Implement GeoJSON functions.
* [Revision #6cdbf2027e](https://github.com/MariaDB/server/commit/6cdbf2027e)\
  2017-01-24 19:52:15 +0530
  * [MDEV-11108](https://jira.mariadb.org/browse/MDEV-11108): adjusted test results
* [Revision #50831b0f19](https://github.com/MariaDB/server/commit/50831b0f19)\
  2017-01-24 17:34:44 +0400
  * [MDEV-11557](https://jira.mariadb.org/browse/MDEV-11557) port MySQL-5.7 JSON tests to MariaDB.
* [Revision #e5398aca76](https://github.com/MariaDB/server/commit/e5398aca76)\
  2017-01-24 15:21:02 +0200
  * Native AIO should also punch\_hole if available.
* [Revision #106fbadaba](https://github.com/MariaDB/server/commit/106fbadaba)\
  2017-01-24 17:29:51 +0400
  * [MDEV-11848](https://jira.mariadb.org/browse/MDEV-11848) Automatic statement repreparation changes query semantics
* [Revision #ae91690d89](https://github.com/MariaDB/server/commit/ae91690d89)\
  2017-01-24 17:22:06 +0400
  * [MDEV-11780](https://jira.mariadb.org/browse/MDEV-11780) Crash with PREPARE + SP out parameter + literal
* [Revision #8368044997](https://github.com/MariaDB/server/commit/8368044997)\
  2017-01-24 15:10:45 +0200
  * Fix compiler error on native AIO.
* [Revision #51b248cfdd](https://github.com/MariaDB/server/commit/51b248cfdd)\
  2017-01-24 15:04:50 +0200
  * [MDEV-11879](https://jira.mariadb.org/browse/MDEV-11879): Duplicate option innochecksum -l (--log, --leaf)
* [Revision #6495806e59](https://github.com/MariaDB/server/commit/6495806e59)\
  2017-01-24 14:40:58 +0200
  * [MDEV-11254](https://jira.mariadb.org/browse/MDEV-11254): innodb-use-trim has no effect in 10.2
* [Revision #0d107a85b3](https://github.com/MariaDB/server/commit/0d107a85b3)\
  2017-01-24 02:29:04 +0400
  * [MDEV-11042](https://jira.mariadb.org/browse/MDEV-11042) Implement GeoJSON functions.
* [Revision #1f3ad6a4ba](https://github.com/MariaDB/server/commit/1f3ad6a4ba)\
  2017-01-24 01:21:43 +0530
  * [MDEV-11108](https://jira.mariadb.org/browse/MDEV-11108): Assertion \`uniq\_tuple\_length\_arg <= table->file->max\_key\_length()' failed in SJ\_TMP\_TABLE::create\_sj\_weedout\_tmp\_table
* [Revision #45e40892c5](https://github.com/MariaDB/server/commit/45e40892c5)\
  2017-01-23 22:25:29 +0400
  * [MDEV-11134](https://jira.mariadb.org/browse/MDEV-11134) Assertion \`fixed' failed in Item::const\_charset\_converter(THD\*, CHARSET\_INFO\*, bool, const char\*)
* [Revision #31031a52da](https://github.com/MariaDB/server/commit/31031a52da)\
  2017-01-22 17:46:33 +0200
  * [MDEV-11870](https://jira.mariadb.org/browse/MDEV-11870) Message "MariaDB Galera and flashback does not support"
* [Revision #beeacd2287](https://github.com/MariaDB/server/commit/beeacd2287)\
  2017-01-22 03:32:20 +0200
  * Follow-up for [MDEV-11065](https://jira.mariadb.org/browse/MDEV-11065) - add tests for compressed+encrypted binlog
* [Revision #4a14356efd](https://github.com/MariaDB/server/commit/4a14356efd)\
  2017-01-22 03:15:46 +0200
  * Disable vcol.vcol\_keys\_myisam until [MDEV-11836](https://jira.mariadb.org/browse/MDEV-11836) is fixed
* [Revision #d75d8631ed](https://github.com/MariaDB/server/commit/d75d8631ed)\
  2017-01-20 15:33:28 +0200
  * \[[MDEV-10570](https://jira.mariadb.org/browse/MDEV-10570)] Add Flashback support
* [Revision #b9631b4633](https://github.com/MariaDB/server/commit/b9631b4633)\
  2017-01-19 17:55:37 +0200
  * Follow-up for the 10.1 -> 10.2 merge
* Merge [Revision #b05bf8ff0f](https://github.com/MariaDB/server/commit/b05bf8ff0f) 2017-01-19 12:06:13 +0200 - Merge 10.1 to 10.2.
* [Revision #833aa97cec](https://github.com/MariaDB/server/commit/833aa97cec)\
  2017-01-18 21:03:01 -0800
  * Fixed bug [MDEV-11818](https://jira.mariadb.org/browse/MDEV-11818).
* [Revision #a1315a650a](https://github.com/MariaDB/server/commit/a1315a650a)\
  2017-01-18 14:02:17 +0200
  * [MDEV-11202](https://jira.mariadb.org/browse/MDEV-11202) InnoDB 10.1 -> 10.2 migration does not work
* [Revision #8780b89529](https://github.com/MariaDB/server/commit/8780b89529)\
  2017-01-18 12:53:35 +0200
  * [MDEV-11831](https://jira.mariadb.org/browse/MDEV-11831) Make InnoDB mini-transaction memo checks stricter
* [Revision #95ebca7197](https://github.com/MariaDB/server/commit/95ebca7197)\
  2017-01-18 13:38:52 +0200
  * Fix test failure on sysvars\_innodb.
* [Revision #716b87845d](https://github.com/MariaDB/server/commit/716b87845d)\
  2017-01-18 13:32:55 +0200
  * Fix test failure on innodb-page\_compression\_snappy test.
* [Revision #25e5ce1982](https://github.com/MariaDB/server/commit/25e5ce1982)\
  2017-01-18 14:13:11 +0300
  * NOT FIXED: [MDEV-10773](https://jira.mariadb.org/browse/MDEV-10773): ANALYZE FORMAT=JSON query\_with\_CTE crashes
* [Revision #9ea0b44c56](https://github.com/MariaDB/server/commit/9ea0b44c56)\
  2017-01-18 09:27:19 +0100
  * Such big blocks in query processing should be represented in the debugging trace.
* [Revision #08413254b7](https://github.com/MariaDB/server/commit/08413254b7)\
  2017-01-17 18:49:34 +0200
  * Remove references to innodb\_file\_format.
* [Revision #085b292a47](https://github.com/MariaDB/server/commit/085b292a47)\
  2017-01-17 17:08:00 +0200
  * [MDEV-11824](https://jira.mariadb.org/browse/MDEV-11824) Allow ROW\_FORMAT=DYNAMIC in the InnoDB system tablespace
* [Revision #7cf97ed4ee](https://github.com/MariaDB/server/commit/7cf97ed4ee)\
  2017-01-17 11:37:49 +0200
  * [MDEV-11816](https://jira.mariadb.org/browse/MDEV-11816) Disallow CREATE TEMPORARY TABLE…ROW\_FORMAT=COMPRESSED
* [Revision #494e4b99a4](https://github.com/MariaDB/server/commit/494e4b99a4)\
  2017-01-16 16:02:42 +0200
  * Remove MYSQL\_TABLESPACES.
* [Revision #1eabad5dbe](https://github.com/MariaDB/server/commit/1eabad5dbe)\
  2017-01-16 14:03:36 +0200
  * Remove MYSQL\_COMPRESSION.
* [Revision #70c11485d2](https://github.com/MariaDB/server/commit/70c11485d2)\
  2017-01-16 11:11:14 +0200
  * Remove MYSQL\_ENCRYPTION.
* [Revision #45f11a729c](https://github.com/MariaDB/server/commit/45f11a729c)\
  2017-01-18 00:56:24 +0300
  * [MDEV-10773](https://jira.mariadb.org/browse/MDEV-10773): ANALYZE FORMAT=JSON query\_with\_CTE crashes
* [Revision #6a65de6cda](https://github.com/MariaDB/server/commit/6a65de6cda)\
  2017-01-17 15:28:50 +0200
  * Correct a test broken in the merge 7c81f15ec3bcc
* [Revision #c849b7df61](https://github.com/MariaDB/server/commit/c849b7df61)\
  2017-01-17 11:52:31 +0200
  * [MDEV-11785](https://jira.mariadb.org/browse/MDEV-11785) Remove INFORMATION\_SCHEMA.INNODB\_TEMP\_TABLE\_INFO
* [Revision #bb109aeea3](https://github.com/MariaDB/server/commit/bb109aeea3)\
  2017-01-16 13:57:39 +0200
  * [MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076): Fix a broken assertion.
* [Revision #1ba7234b21](https://github.com/MariaDB/server/commit/1ba7234b21)\
  2017-01-12 13:30:10 +0200
  * Follow-up to [MDEV-11713](https://jira.mariadb.org/browse/MDEV-11713): Make more use of DBUG\_LOG
* Merge [Revision #7c81f15ec3](https://github.com/MariaDB/server/commit/7c81f15ec3) 2017-01-12 12:42:15 +0200 - Merge 10.1 into bb-10.2-[MDEV-11782](https://jira.mariadb.org/browse/MDEV-11782)
* Merge [Revision #fd0479ce59](https://github.com/MariaDB/server/commit/fd0479ce59) 2017-01-11 14:27:24 +0200 - Merge 10.1 into 10.2
* [Revision #5f0c31f928](https://github.com/MariaDB/server/commit/5f0c31f928)\
  2017-01-10 18:28:24 +0200
  * [MDEV-11597](https://jira.mariadb.org/browse/MDEV-11597) Assertion when doing select from virtual column with impossible value
* [Revision #177c191ff4](https://github.com/MariaDB/server/commit/177c191ff4)\
  2017-01-09 19:31:21 +0200
  * [MDEV-11606](https://jira.mariadb.org/browse/MDEV-11606) Server crashes in mi\_make\_key / sort\_key\_read
* [Revision #c9b3e4535b](https://github.com/MariaDB/server/commit/c9b3e4535b)\
  2017-01-09 18:46:20 +0200
  * [MDEV-11737](https://jira.mariadb.org/browse/MDEV-11737) Failing assertion: block->magic\_n == MEM\_BLOCK\_MAGIC\_N
* [Revision #6c5c98316f](https://github.com/MariaDB/server/commit/6c5c98316f)\
  2017-01-05 14:36:44 +0200
  * Updated mysql-test/README with information about KB
* [Revision #135e144479](https://github.com/MariaDB/server/commit/135e144479)\
  2017-01-05 01:07:03 +0200
  * [MDEV-11598](https://jira.mariadb.org/browse/MDEV-11598) Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed
* [Revision #de22cd3fe5](https://github.com/MariaDB/server/commit/de22cd3fe5)\
  2017-01-04 18:45:23 +0200
  * Fixes for failures in test scripts and removal of some compiler warnings
* [Revision #bf95970ec0](https://github.com/MariaDB/server/commit/bf95970ec0)\
  2017-01-03 15:47:17 +0200
  * Cleanups
* [Revision #53ae72e2ee](https://github.com/MariaDB/server/commit/53ae72e2ee)\
  2017-01-02 21:28:15 +0100
  * mtr uses dgcov for --gcov option
* [Revision #00f462cf1b](https://github.com/MariaDB/server/commit/00f462cf1b)\
  2017-01-02 11:03:25 +0100
  * dgcov: import, rewrite to work with cmake and git
* [Revision #7567cf5aef](https://github.com/MariaDB/server/commit/7567cf5aef)\
  2016-12-30 11:23:45 +0200
  * Fixes for using ssl with BUILD scripts.
* [Revision #ea1b25046c](https://github.com/MariaDB/server/commit/ea1b25046c)\
  2016-12-30 11:07:44 +0200
  * New simpler bugfix for UPDATE and virtual BLOBs
* [Revision #7454087d07](https://github.com/MariaDB/server/commit/7454087d07)\
  2016-12-27 17:18:10 +0200
  * Revert "bugfix: UPDATE and virtual BLOBs"
* [Revision #1628a2ae27](https://github.com/MariaDB/server/commit/1628a2ae27)\
  2016-12-27 01:30:20 +0200
  * Fixed issues found by buildbot
* [Revision #1afb17047a](https://github.com/MariaDB/server/commit/1afb17047a)\
  2016-12-20 18:06:49 +0200
  * Fixed bugs found by mysql-test-run:
* [Revision #ed008a74cf](https://github.com/MariaDB/server/commit/ed008a74cf)\
  2016-12-31 15:11:52 +0100
  * Make atomic writes general
* [Revision #ed0bc17bee](https://github.com/MariaDB/server/commit/ed0bc17bee)\
  2016-12-20 13:03:45 +0200
  * Removed usage of my\_hash\_search() with uninitialized HASH.
* [Revision #e80ad58de8](https://github.com/MariaDB/server/commit/e80ad58de8)\
  2016-12-19 22:25:42 +0200
  * Improve mysys/hash by caching hash\_nr
* [Revision #67034b6d52](https://github.com/MariaDB/server/commit/67034b6d52)\
  2016-12-06 14:05:09 +0200
  * Fixes for running with gcov
* Merge [Revision #f27ca6f667](https://github.com/MariaDB/server/commit/f27ca6f667) 2017-01-10 14:39:28 +0200 - Merge 10.1 into 10.2
* Merge [Revision #3d46768da2](https://github.com/MariaDB/server/commit/3d46768da2) 2017-01-09 09:47:12 +0200 - Merge 10.1 into 10.2
* [Revision #8773a5e161](https://github.com/MariaDB/server/commit/8773a5e161)\
  2017-01-07 15:36:08 +0200
  * Post-fix [MDEV-11695](https://jira.mariadb.org/browse/MDEV-11695) Define a reasonable upper limit for innodb\_spin\_wait\_delay
* Merge [Revision #6790bf049c](https://github.com/MariaDB/server/commit/6790bf049c) 2017-01-07 15:35:34 +0200 - Merge 10.1 into 10.2
* [Revision #bbd4844a43](https://github.com/MariaDB/server/commit/bbd4844a43)\
  2017-01-06 14:52:35 +0200
  * Suppress warnings of NUMA not working.
* [Revision #ac0b0efa14](https://github.com/MariaDB/server/commit/ac0b0efa14)\
  2017-01-06 14:42:28 +0200
  * Post-fix [MDEV-11695](https://jira.mariadb.org/browse/MDEV-11695) Define a reasonable upper limit for innodb\_spin\_wait\_delay
* Merge [Revision #4ce579d27f](https://github.com/MariaDB/server/commit/4ce579d27f) 2017-01-05 20:44:26 +0200 - Merge 10.1 into 10.2
* Merge [Revision #11b7dff5eb](https://github.com/MariaDB/server/commit/11b7dff5eb) 2017-01-05 19:03:56 +0200 - Merge 10.1 to 10.2.
* [Revision #30f27b0de0](https://github.com/MariaDB/server/commit/30f27b0de0)\
  2017-01-05 11:54:10 +0200
  * Post-merge fix for [MDEV-11638](https://jira.mariadb.org/browse/MDEV-11638).
* [Revision #a8ac6dc506](https://github.com/MariaDB/server/commit/a8ac6dc506)\
  2017-01-05 11:49:00 +0200
  * Fix InnoDB compilation warnings.
* [Revision #bf35deda09](https://github.com/MariaDB/server/commit/bf35deda09)\
  2017-01-03 15:38:09 +0200
  * [MDEV-11713](https://jira.mariadb.org/browse/MDEV-11713) Optimize DBUG\_PRINT and introduce DBUG\_LOG
* Merge [Revision #4e7b382d31](https://github.com/MariaDB/server/commit/4e7b382d31) 2017-01-05 10:48:03 +0200 - Merge 10.1 to 10.2
* [Revision #348ccb6f03](https://github.com/MariaDB/server/commit/348ccb6f03)\
  2017-01-04 14:33:24 -0800
  * Fixed bug [MDEV-11674](https://jira.mariadb.org/browse/MDEV-11674).
* [Revision #a758479c10](https://github.com/MariaDB/server/commit/a758479c10)\
  2017-01-03 15:44:44 +0200
  * Post-fix for [MDEV-11688](https://jira.mariadb.org/browse/MDEV-11688) fil\_crypt\_threads\_end() tries to create threads
* [Revision #a0d396fd3f](https://github.com/MariaDB/server/commit/a0d396fd3f)\
  2017-01-03 14:35:08 +0200
  * [MDEV-11684](https://jira.mariadb.org/browse/MDEV-11684): post-10.1-merge fixes
* [Revision #8a04b8cade](https://github.com/MariaDB/server/commit/8a04b8cade)\
  2017-01-03 13:18:47 +0200
  * [MDEV-11688](https://jira.mariadb.org/browse/MDEV-11688) fil\_crypt\_threads\_end() tries to create threads after aborted InnoDB startup
* [Revision #509e7773ec](https://github.com/MariaDB/server/commit/509e7773ec)\
  2017-01-03 12:09:14 +0200
  * [MDEV-11695](https://jira.mariadb.org/browse/MDEV-11695) Define a reasonable upper limit for innodb\_spin\_wait\_delay
* [Revision #403f6e9607](https://github.com/MariaDB/server/commit/403f6e9607)\
  2017-01-03 11:22:09 +0200
  * [MDEV-11705](https://jira.mariadb.org/browse/MDEV-11705): InnoDB: Failing assertion: (\&log\_sys->mutex)->is\_owned() if server started with innodb-scrub-log
* [Revision #4c610d10d4](https://github.com/MariaDB/server/commit/4c610d10d4)\
  2017-01-03 09:44:44 +0200
  * Post-fix for [MDEV-11195](https://jira.mariadb.org/browse/MDEV-11195) NUMA does not get enabled even when checks are passed
* [Revision #efcd0935f7](https://github.com/MariaDB/server/commit/efcd0935f7)\
  2016-12-27 14:13:32 +0530
  * [MDEV-11636](https://jira.mariadb.org/browse/MDEV-11636) Extra persistent columns on slave always gets NULL in RBR
* [Revision #b727213de2](https://github.com/MariaDB/server/commit/b727213de2)\
  2016-12-30 16:14:33 +0200
  * [MDEV-11687](https://jira.mariadb.org/browse/MDEV-11687) innodb\_use\_fallocate has no effect
* [Revision #63574f1275](https://github.com/MariaDB/server/commit/63574f1275)\
  2016-12-30 15:04:10 +0200
  * [MDEV-11690](https://jira.mariadb.org/browse/MDEV-11690) Remove UNIV\_HOTBACKUP
* Merge [Revision #9ebd767331](https://github.com/MariaDB/server/commit/9ebd767331) 2016-12-30 13:48:22 +0200 - Merge 10.1 into 10.2
* [Revision #1ab3866de2](https://github.com/MariaDB/server/commit/1ab3866de2)\
  2016-12-30 12:26:05 +0200
  * [MDEV-11687](https://jira.mariadb.org/browse/MDEV-11687) innodb\_use\_fallocate has no effect
* [Revision #d4342702bf](https://github.com/MariaDB/server/commit/d4342702bf)\
  2016-12-30 12:15:06 +0200
  * Remove dead references to NO\_FALLOCATE.
* [Revision #cbf80b0de8](https://github.com/MariaDB/server/commit/cbf80b0de8)\
  2016-12-30 12:12:34 +0200
  * Fix tests that were forgotten to run after the merge.
* Merge [Revision #970f17cbfc](https://github.com/MariaDB/server/commit/970f17cbfc) 2016-12-30 08:56:13 +0200 - Merge 10.1 into 10.2
* Merge [Revision #341c375d4b](https://github.com/MariaDB/server/commit/341c375d4b) 2016-12-30 08:21:20 +0200 - Merge 10.1 into 10.2
* [Revision #f2fe65106f](https://github.com/MariaDB/server/commit/f2fe65106f)\
  2016-12-28 17:13:14 +0200
  * [MDEV-11679](https://jira.mariadb.org/browse/MDEV-11679) Remove redundant function fsp\_header\_get\_crypt\_offset()
* Merge [Revision #7bcae22bf1](https://github.com/MariaDB/server/commit/7bcae22bf1) 2016-12-29 15:05:04 +0200 - Merge branch 'bb-10.2-[MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076)' into 10.2
* [Revision #6f4f9f2843](https://github.com/MariaDB/server/commit/6f4f9f2843)\
  2016-12-16 17:15:40 +0200
  * [MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076) Adjust a test result.
* [Revision #c64edc6b83](https://github.com/MariaDB/server/commit/c64edc6b83)\
  2016-12-15 18:51:41 +0200
  * [MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076): Preserve PAGE\_ROOT\_AUTO\_INC when emptying pages.
* [Revision #cb0ce5c2e9](https://github.com/MariaDB/server/commit/cb0ce5c2e9)\
  2016-12-16 10:19:14 +0200
  * [MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076): Optimize the test.
* [Revision #8777458a6e](https://github.com/MariaDB/server/commit/8777458a6e)\
  2016-12-14 19:56:39 +0200
  * [MDEV-6076](https://jira.mariadb.org/browse/MDEV-6076) Persistent AUTO\_INCREMENT for InnoDB
* [Revision #ab89359dde](https://github.com/MariaDB/server/commit/ab89359dde)\
  2016-12-27 19:40:07 +0100
  * enable tests that were skipped because of have\_xtradb
* [Revision #b3d6cbc25a](https://github.com/MariaDB/server/commit/b3d6cbc25a)\
  2016-12-27 18:13:33 +0100
  * cleanup: binlog.binlog\_killed\_simulate
* [Revision #0d897c2ceb](https://github.com/MariaDB/server/commit/0d897c2ceb)\
  2016-12-27 17:56:40 +0100
  * cleanup: binlog.binlog\_row\_annotate
* Merge [Revision #4a5d25c338](https://github.com/MariaDB/server/commit/4a5d25c338) 2016-12-29 13:23:18 +0100 - Merge branch '10.1' into 10.2
* [Revision #48dc7cc66e](https://github.com/MariaDB/server/commit/48dc7cc66e)\
  2016-12-27 18:08:18 +0100
  * cleanup: redundant memcmp()
* [Revision #100f721c0a](https://github.com/MariaDB/server/commit/100f721c0a)\
  2016-12-21 17:41:48 +0100
  * [MDEV-11584](https://jira.mariadb.org/browse/MDEV-11584): GRANT inside an SP does not work well on 2nd execution
* [Revision #143d512a22](https://github.com/MariaDB/server/commit/143d512a22)\
  2016-12-24 11:31:04 -0500
  * [MDEV-11035](https://jira.mariadb.org/browse/MDEV-11035): Re-enable galera\_var\_innodb\_disallow\_writes test
* [Revision #f5c4f1eb38](https://github.com/MariaDB/server/commit/f5c4f1eb38)\
  2016-12-24 09:54:23 -0500
  * bump the VERSION
* [Revision #3a1772798d](https://github.com/MariaDB/server/commit/3a1772798d)\
  2016-12-24 11:40:31 +0400
  * [MDEV-11573](https://jira.mariadb.org/browse/MDEV-11573) JSON\_LENGTH returns incorrect results.
* [Revision #4d10273b4f](https://github.com/MariaDB/server/commit/4d10273b4f)\
  2016-12-24 10:51:43 +0400
  * [MDEV-11571](https://jira.mariadb.org/browse/MDEV-11571) JSON\_EXTRACT returns wrong results.
* [Revision #bbb3fb318e](https://github.com/MariaDB/server/commit/bbb3fb318e)\
  2016-12-23 09:19:39 +0200
  * Follow-up for [MDEV-11630](https://jira.mariadb.org/browse/MDEV-11630) Call mutex\_free() before freeing the mutex list
* [Revision #08f79bdeda](https://github.com/MariaDB/server/commit/08f79bdeda)\
  2016-12-22 16:48:49 +0200
  * [MDEV-11635](https://jira.mariadb.org/browse/MDEV-11635) innodb.innodb\_mysql test hangs
* [Revision #d6a1f9f10f](https://github.com/MariaDB/server/commit/d6a1f9f10f)\
  2016-12-22 10:23:42 +0200
  * [MDEV-11630](https://jira.mariadb.org/browse/MDEV-11630) Call mutex\_free() before freeing the mutex list

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
