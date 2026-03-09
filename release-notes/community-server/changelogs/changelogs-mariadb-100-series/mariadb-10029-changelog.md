# MariaDB 10.0.29 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.29)[Release Notes](../../old-releases/10.0/10.0.29.md)[Changelog](mariadb-10029-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 13 Jan 2017

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.29.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #4f53384](https://github.com/MariaDB/server/commit/4f53384) 2017-01-12 03:37:35 +0200 - Merge branch 'bb-10.0-vicentiu' into 10.0
* [Revision #1c5ca7c](https://github.com/MariaDB/server/commit/1c5ca7c) 2017-01-12 03:36:45 +0200 - Merge branch '5.5' into 10.0
* [Revision #ab93a4d](https://github.com/MariaDB/server/commit/ab93a4d)\
  2017-01-11 09:05:36 -0500
  * [MDEV-11685](https://jira.mariadb.org/browse/MDEV-11685): sql\_mode can't be set with non-ascii connection charset
* [Revision #c1a23cd](https://github.com/MariaDB/server/commit/c1a23cd)\
  2017-01-10 18:31:03 +0100
  * [MDEV-11676](https://jira.mariadb.org/browse/MDEV-11676) Starting service with mysqld\_safe\_helper fails in SELINUX "enforcing" mode
* [Revision #6ad3dd6](https://github.com/MariaDB/server/commit/6ad3dd6)\
  2017-01-10 14:19:11 +0100
  * mysqld\_safe: don't close stdout if set -x
* [Revision #9a4bc0d](https://github.com/MariaDB/server/commit/9a4bc0d)\
  2017-01-03 16:38:56 +0200
  * Update mysql\_secure\_installation man page
* [Revision #4799af0](https://github.com/MariaDB/server/commit/4799af0)\
  2017-01-10 14:20:43 +0200
  * Fix unit test after merge from mysql 5.5.35 perfschema
* [Revision #d00d46f](https://github.com/MariaDB/server/commit/d00d46f) 2017-01-10 12:34:51 +0200 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #3e63fde](https://github.com/MariaDB/server/commit/3e63fde)\
  2017-01-09 14:19:02 +0400
  * Adding LOAD DATA tests for [MDEV-11079](https://jira.mariadb.org/browse/MDEV-11079) and [MDEV-11631](https://jira.mariadb.org/browse/MDEV-11631)
* [Revision #ecdb39a](https://github.com/MariaDB/server/commit/ecdb39a)\
  2017-01-10 12:08:36 +0200
  * Fix problems from 5.5 merge
* [Revision #94e18e2](https://github.com/MariaDB/server/commit/94e18e2) 2017-01-10 12:32:54 +0200 - Merge remote-tracking branch 'merge/merge-perfschema-5.6' into 10.0
* [Revision #c33db2cdc0](https://github.com/MariaDB/server/commit/c33db2cdc0)\
  2017-01-07 15:53:37 +0200
  * 5.6.35
* [Revision #ae47336](https://github.com/MariaDB/server/commit/ae47336)\
  2016-10-25 16:59:57 +0200
  * 5.6.34
* [Revision #682d484](https://github.com/MariaDB/server/commit/682d484) 2017-01-07 14:38:21 +0200 - Merge remote-tracking branch 'merge/merge-innodb-5.6' into 10.0
* [Revision #6ac84d9](https://github.com/MariaDB/server/commit/6ac84d9)\
  2017-01-07 14:24:42 +0200
  * 5.6.35
* [Revision #31d8c92](https://github.com/MariaDB/server/commit/31d8c92)\
  2016-10-25 16:58:47 +0200
  * 5.6.34
* [Revision #1a55455](https://github.com/MariaDB/server/commit/1a55455) 2017-01-06 20:24:50 +0200 - Merge remote-tracking branch 'connect/10.0' into bb-10.0-vicentiu
* [Revision #4314768](https://github.com/MariaDB/server/commit/4314768)\
  2016-12-25 12:32:05 +0100
  * Modified version number
* [Revision #6d2d0a7](https://github.com/MariaDB/server/commit/6d2d0a7) 2016-12-24 18:19:21 +0100 - Merge branch '10.0' of [server](https://github.com/MariaDB/server) into ob-10.0
* [Revision #e6b563f](https://github.com/MariaDB/server/commit/e6b563f)\
  2016-12-23 16:58:32 +0100
  * Fix some XML table type bugs
* [Revision #9523065](https://github.com/MariaDB/server/commit/9523065)\
  2016-12-14 14:20:23 +0100
  * [MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295): developing handling files contained in ZIP file. Enable using multiple zip files
* [Revision #d44723e](https://github.com/MariaDB/server/commit/d44723e)\
  2016-12-12 10:57:19 +0100
  * [MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295): developing handling files contained in ZIP file. A first experimental and limited implementation
* [Revision #599d8cc](https://github.com/MariaDB/server/commit/599d8cc)\
  2016-12-02 23:03:43 +0100
  * [MDEV-11366](https://jira.mariadb.org/browse/MDEV-11366) SIGBUS errors in Connect Storage Engine for ArmHF and MIPS. Fix includes launchpad fix plus more to cover writing BIN tables
* [Revision #2d78b25](https://github.com/MariaDB/server/commit/2d78b25)\
  2016-11-27 14:42:37 +0100
  * Fix null pointer java error when connecting to jdbc:drill driver. By setting the context class loader
* [Revision #aae6753](https://github.com/MariaDB/server/commit/aae6753)\
  2016-11-14 19:20:40 +0100
  * [MDEV-11051](https://jira.mariadb.org/browse/MDEV-11051) place Java classes ApacheInterface and JdbcInterface into single jar file. Try to fix the INSTALL command
* [Revision #5884aa1](https://github.com/MariaDB/server/commit/5884aa1)\
  2016-11-06 14:57:27 +0100
  * Fix [MDEV-11234](https://jira.mariadb.org/browse/MDEV-11234). Escape quoting character. Should be doubled. Now it is also possible to escape it by a backslash
* [Revision #e9aed13](https://github.com/MariaDB/server/commit/e9aed13) 2017-01-06 17:09:59 +0200 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #ae1b3d1](https://github.com/MariaDB/server/commit/ae1b3d1)\
  2017-01-05 13:54:31 -0800
  * Fixed bug [MDEV-10705](https://jira.mariadb.org/browse/MDEV-10705).
* [Revision #9e528d4](https://github.com/MariaDB/server/commit/9e528d4)\
  2017-01-05 17:38:55 +0200
  * [MDEV-11727](https://jira.mariadb.org/browse/MDEV-11727) Sequences of tests fail with valgrind warnings in buildbot
* [Revision #5302ef2](https://github.com/MariaDB/server/commit/5302ef2)\
  2017-01-01 23:13:04 +0200
  * [MDEV-11700](https://jira.mariadb.org/browse/MDEV-11700) funcs\_2.innodb\_charset fails in buldbot on valgrind builder with timeout
* [Revision #f1ee011](https://github.com/MariaDB/server/commit/f1ee011)\
  2017-01-04 23:05:22 +0200
  * [MDEV-11722](https://jira.mariadb.org/browse/MDEV-11722) main.join\_cache fails in buildbot on very slow builders
* [Revision #f4d12c1](https://github.com/MariaDB/server/commit/f4d12c1)\
  2017-01-04 13:36:55 +0100
  * [MDEV-11676](https://jira.mariadb.org/browse/MDEV-11676) Starting service with mysqld\_safe\_helper fails in SELINUX "enforcing" mode
* [Revision #e5d7fc9](https://github.com/MariaDB/server/commit/e5d7fc9)\
  2017-01-04 13:03:30 +0200
  * [MDEV-10100](https://jira.mariadb.org/browse/MDEV-10100) main.pool\_of\_threads fails sporadically in buildbot
* [Revision #0912fbb](https://github.com/MariaDB/server/commit/0912fbb)\
  2017-01-04 03:33:39 +0200
  * [MDEV-11719](https://jira.mariadb.org/browse/MDEV-11719) main.subselect\_no\_exists\_to\_in failed in buildbot
* [Revision #2718225](https://github.com/MariaDB/server/commit/2718225)\
  2016-12-24 09:47:55 -0500
  * bump the VERSION
* [Revision #ec6d8da](https://github.com/MariaDB/server/commit/ec6d8da)\
  2016-12-22 13:02:32 +0100
  * reduce code duplication a little
* [Revision #e7d7910](https://github.com/MariaDB/server/commit/e7d7910)\
  2016-12-22 11:13:07 +0100
  * add an assert
* [Revision #48655ce](https://github.com/MariaDB/server/commit/48655ce)\
  2016-12-22 12:23:48 +0100
  * test case for Bug #23303485 : HANDLE\_FATAL\_SIGNAL (SIG=11) IN `SUBSELECT_UNION_ENGINE::NO_ROWS`
* [Revision #9fefe97](https://github.com/MariaDB/server/commit/9fefe97) 2016-12-22 12:49:06 +0100 - Merge branch 'mysql/5.5' into 5.5
* [Revision #8fcdd6b](https://github.com/MariaDB/server/commit/8fcdd6b)\
  2016-12-20 21:16:23 +0100
  * Numerous issues in mysqld\_safe
* [Revision #c8e49f2](https://github.com/MariaDB/server/commit/c8e49f2)\
  2016-12-20 15:17:59 +0100
  * move check\_user/set\_user from mysqld.cc to mysys
* [Revision #706fb79](https://github.com/MariaDB/server/commit/706fb79)\
  2016-12-22 15:51:37 +0530
  * [MDEV-10927](https://jira.mariadb.org/browse/MDEV-10927): Crash When Using sort\_union Optimization
* [Revision #5e051bfa](https://github.com/MariaDB/server/commit/5e051bfa)\
  2016-12-21 15:39:45 +0400
  * [MDEV-10386](https://jira.mariadb.org/browse/MDEV-10386) Assertion \`\`fixed == 1'`failed in virtual String*`Item\_func\_conv\_charset::val\_str(String\*)\`
* [Revision #ef82fd8](https://github.com/MariaDB/server/commit/ef82fd8)\
  2016-12-20 17:42:08 +0400
  * [MDEV-11353](https://jira.mariadb.org/browse/MDEV-11353) - Identical logical conditions
* [Revision #cbd7548](https://github.com/MariaDB/server/commit/cbd7548)\
  2016-12-08 23:27:04 +0530
  * [MDEV-11353](https://jira.mariadb.org/browse/MDEV-11353): fixes Identical logical conditions
* [Revision #e025ebc](https://github.com/MariaDB/server/commit/e025ebc)\
  2016-12-20 12:45:48 +0000
  * Fix pointer formatting in crash handler output.
* [Revision #aaff3d6](https://github.com/MariaDB/server/commit/aaff3d6)\
  2016-12-20 10:25:25 +0100
  * [MDEV-10172](https://jira.mariadb.org/browse/MDEV-10172): UNION query returns incorrect rows outside conditional evaluation
* [Revision #f23b41b](https://github.com/MariaDB/server/commit/f23b41b)\
  2016-12-16 17:16:02 +0300
  * [MDEV-10148](https://jira.mariadb.org/browse/MDEV-10148): Database crashes in the query to the View
* [Revision #268bb69](https://github.com/MariaDB/server/commit/268bb69)\
  2016-12-16 17:08:31 +0300
  * [MDEV-7691](https://jira.mariadb.org/browse/MDEV-7691): Assertion \`\`outer\_context || !\*from\_field || \*from\_field == not\_found\_field'\` ...
* [Revision #19896d4](https://github.com/MariaDB/server/commit/19896d4)\
  2016-12-19 16:09:20 +0400
  * [MDEV-10274](https://jira.mariadb.org/browse/MDEV-10274) Bundling insert with create statement for table with unsigned Decimal primary key issues warning 1194.
* [Revision #2f6fede](https://github.com/MariaDB/server/commit/2f6fede)\
  2016-12-19 14:28:08 +0400
  * [MDEV-10524](https://jira.mariadb.org/browse/MDEV-10524) Assertion \`\`arg1\_int >= 0'`failed in`Item\_func\_additive\_op::result\_precision()\`
* [Revision #c4d9dc70](https://github.com/MariaDB/server/commit/c4d9dc70)\
  2016-12-16 14:44:08 +0200
  * Typo, update limit in comment
* [Revision #b2b210b](https://github.com/MariaDB/server/commit/b2b210b)\
  2016-12-16 17:42:21 +0100
  * [MDEV-11543](https://jira.mariadb.org/browse/MDEV-11543) Buildbot tests fail with warnings on server shutdown after rpl.rpl\_row\_mysqlbinlog
* [Revision #b03b38d](https://github.com/MariaDB/server/commit/b03b38d)\
  2016-12-16 10:10:08 +0100
  * cleanup: rpl.rpl\_row\_mysqlbinlog
* [Revision #e86580c](https://github.com/MariaDB/server/commit/e86580c)\
  2016-12-15 18:20:58 +0100
  * [MDEV-11552](https://jira.mariadb.org/browse/MDEV-11552) Queries executed by event scheduler are written to slow log incorrectly or not written at all
* [Revision #211cf93](https://github.com/MariaDB/server/commit/211cf93)\
  2016-12-16 18:37:11 +0400
  * [MDEV-11510](https://jira.mariadb.org/browse/MDEV-11510) Audit plugin sometimes causes server to crash when using with MySQL.
* [Revision #14e1f32](https://github.com/MariaDB/server/commit/14e1f32)\
  2016-12-11 00:50:00 +0200
  * Follow-up for 02d153c7b9 (str2decimal: don't return a negative zero)
* [Revision #833fda8](https://github.com/MariaDB/server/commit/833fda8)\
  2017-01-11 14:13:30 +0200
  * InnoDB: Enable UNIV\_DEBUG\_VALGRIND for cmake -DWITH\_VALGRIND
* [Revision #f516db3](https://github.com/MariaDB/server/commit/f516db3)\
  2017-01-11 04:45:47 +0200
  * Updated list of unstable tests for 10.0.29 release
* [Revision #78e6faf](https://github.com/MariaDB/server/commit/78e6faf)\
  2017-01-10 14:11:32 +0200
  * Fix an innodb\_plugin leak noted in [MDEV-11686](https://jira.mariadb.org/browse/MDEV-11686)
* [Revision #171e59e](https://github.com/MariaDB/server/commit/171e59e)\
  2017-01-09 23:37:42 +0400
  * [MDEV-11548](https://jira.mariadb.org/browse/MDEV-11548) Reproducible server crash after the 2nd ALTER TABLE ADD FOREIGN KEY IF NOT EXISTS.
* [Revision #eed319b](https://github.com/MariaDB/server/commit/eed319b)\
  2017-01-08 17:51:36 +0200
  * [MDEV-11317](https://jira.mariadb.org/browse/MDEV-11317): \`\`! is\_set()' or `!is_set() || (m_status == DA_OK_BULK && is_bulk_op())'` fails in `Diagnostics_area::set_ok_status` on CREATE OR REPLACE with ARCHIVE table
* [Revision #eaf6b05](https://github.com/MariaDB/server/commit/eaf6b05)\
  2017-01-04 22:41:43 +0100
  * [MDEV-11087](https://jira.mariadb.org/browse/MDEV-11087) Search path for my.ini is wrong for default installation Add \<install\_root>/data/my.ini to the search path - this my.ini location is used since [MariaDB 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)
* [Revision #82b8741](https://github.com/MariaDB/server/commit/82b8741)\
  2017-01-04 22:50:48 +0100
  * Windows : use meaningful DEFAULT\_MYSQL\_HOME - base directory for the default installation.
* [Revision #ae6eb7a](https://github.com/MariaDB/server/commit/ae6eb7a)\
  2017-01-04 23:04:37 +0100
  * [MDEV-11088](https://jira.mariadb.org/browse/MDEV-11088) Client plugins cannot be loaded by command line tools in default installation.
* [Revision #e4978d2](https://github.com/MariaDB/server/commit/e4978d2)\
  2016-07-25 16:06:52 +0300
  * [MDEV-9084](https://jira.mariadb.org/browse/MDEV-9084) Calling a stored function from a nested select from temporary table causes unpredictable behavior
* [Revision #43378f3](https://github.com/MariaDB/server/commit/43378f3)\
  2016-07-25 13:07:50 +0200
  * [MDEV-10271](https://jira.mariadb.org/browse/MDEV-10271): Stopped SQL slave thread doesn't print a message to error log like IO thread does
* [Revision #670b858](https://github.com/MariaDB/server/commit/670b858)\
  2017-01-01 15:36:56 +0200
  * Replication tests fail on valgrind due to waiting-related timeouts
* [Revision #b2b6cf4](https://github.com/MariaDB/server/commit/b2b6cf4)\
  2017-01-04 19:11:13 +0200
  * [MDEV-10988](https://jira.mariadb.org/browse/MDEV-10988) Sphinx test suite refuses to run silently
* [Revision #f0c19b6](https://github.com/MariaDB/server/commit/f0c19b6)\
  2017-01-05 20:13:34 +0200
  * [MDEV-11730](https://jira.mariadb.org/browse/MDEV-11730) Memory leak in innodb.innodb\_corrupt\_bit
* [Revision #9bf9270](https://github.com/MariaDB/server/commit/9bf9270)\
  2017-01-01 19:35:44 +0200
  * [MDEV-8518](https://jira.mariadb.org/browse/MDEV-8518) rpl.sec\_behind\_master-5114 fails sporadically in buildbot
* [Revision #bc4cac3](https://github.com/MariaDB/server/commit/bc4cac3)\
  2017-01-04 13:26:09 +0100
  * [MDEV-10035](https://jira.mariadb.org/browse/MDEV-10035): DBUG\_ASSERT on CREATE VIEW v1 AS SELECT \* FROM t1 FOR UPDATE
* [Revision #80d5d14](https://github.com/MariaDB/server/commit/80d5d14)\
  2017-01-03 19:32:47 +0200
  * [MDEV-11694](https://jira.mariadb.org/browse/MDEV-11694) InnoDB tries to create unused table SYS\_ZIP\_DICT
* [Revision #3871477](https://github.com/MariaDB/server/commit/3871477)\
  2017-01-01 20:06:03 +0200
  * [MDEV-10100](https://jira.mariadb.org/browse/MDEV-10100) main.pool\_of\_threads fails sporadically in buildbot
* [Revision #d02a77b](https://github.com/MariaDB/server/commit/d02a77b)\
  2016-12-27 14:13:32 +0530
  * [MDEV-11636](https://jira.mariadb.org/browse/MDEV-11636) Extra persistent columns on slave always gets NULL in RBR
* [Revision #37f294f](https://github.com/MariaDB/server/commit/37f294f)\
  2016-12-27 03:21:13 +0200
  * Disable the test for valgrind builds
* [Revision #9f863a1](https://github.com/MariaDB/server/commit/9f863a1)\
  2016-12-19 15:57:41 +0200
  * [MDEV-11602](https://jira.mariadb.org/browse/MDEV-11602) InnoDB leaks foreign key metadata on DDL operations
* [Revision #eb4f2e0](https://github.com/MariaDB/server/commit/eb4f2e0)\
  2016-12-10 22:19:09 +0200
  * [MDEV-11533](https://jira.mariadb.org/browse/MDEV-11533): Roles with trailing white spaces are not cleared correctly
* [Revision #3e8155c](https://github.com/MariaDB/server/commit/3e8155c) 2016-12-09 16:33:48 +0100 - Merge branch '5.5' into 10.0
* [Revision #03dabfa](https://github.com/MariaDB/server/commit/03dabfa)\
  2016-12-08 22:54:58 +0100
  * [MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in `handler::increment_statistics` or in make\_select or assertion failure `pfs_thread == ((PFS_thread*) pthread_getspecific((THR_PFS)))`
* [Revision #ab65db6](https://github.com/MariaDB/server/commit/ab65db6)\
  2016-12-08 21:03:45 +0100
  * Revert "[MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in `handler::increment_statistics` or in make\_select or assertion failure `pfs_thread == ((PFS_thread*) pthread_getspecific((THR_PFS)))"`
* [Revision #f5e0522](https://github.com/MariaDB/server/commit/f5e0522)\
  2016-12-07 13:06:14 +0100
  * [MDEV-10388](https://jira.mariadb.org/browse/MDEV-10388) [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md).x keeps (deleted) ML\* files in tmpdir after LOAD DATA completes
* [Revision #1d702ff](https://github.com/MariaDB/server/commit/1d702ff)\
  2016-12-07 14:42:08 +0400
  * [MDEV-8329](https://jira.mariadb.org/browse/MDEV-8329) MariaDB crashes when replicate\_wild\_ignore\_table is set to NULL.
* [Revision #d67ef7a](https://github.com/MariaDB/server/commit/d67ef7a)\
  2016-12-05 17:37:54 +0100
  * [MDEV-10663](https://jira.mariadb.org/browse/MDEV-10663): Use of Inline table columns in HAVING clause throws 1463 Error
* [Revision #035a5ac](https://github.com/MariaDB/server/commit/035a5ac)\
  2016-09-26 18:15:11 +0200
  * [MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in `handler::increment_statistics` or in make\_select or assertion failure `pfs_thread == ((PFS_thread*) pthread_getspecific((THR_PFS)))`
* [Revision #f988bce](https://github.com/MariaDB/server/commit/f988bce)\
  2016-09-21 18:36:34 +0200
  * [MDEV-10776](https://jira.mariadb.org/browse/MDEV-10776): Server crash on query
* [Revision #46dee0d](https://github.com/MariaDB/server/commit/46dee0d)\
  2016-12-05 16:50:12 +0400
  * [MDEV-10717](https://jira.mariadb.org/browse/MDEV-10717) Assertion `!null_value' failed in virtual bool` Item::send(Protocol\*, String\*)\`
* [Revision #18cdff6](https://github.com/MariaDB/server/commit/18cdff6)\
  2016-12-04 12:37:01 +0100
  * [MDEV-10293](https://jira.mariadb.org/browse/MDEV-10293) 'setupterm' was not declared in this scope
* [Revision #02d153c](https://github.com/MariaDB/server/commit/02d153c)\
  2016-06-26 13:37:27 +0200
  * str2decimal: don't return a negative zero
* [Revision #4a3acbc](https://github.com/MariaDB/server/commit/4a3acbc)\
  2016-12-02 00:19:49 +0100
  * [MDEV-11241](https://jira.mariadb.org/browse/MDEV-11241) Certain combining marks cause MariaDB to crash when doing Full-Text searches
* [Revision #0a4b508](https://github.com/MariaDB/server/commit/0a4b508)\
  2016-12-01 20:04:36 +0100
  * [MDEV-11242](https://jira.mariadb.org/browse/MDEV-11242) MariaDB Server releases contains promotion of MariaDB Corporation
* [Revision #f640527](https://github.com/MariaDB/server/commit/f640527)\
  2016-12-02 15:22:11 +0100
  * typo fixed: s/MSYQL/MYSQL/
* [Revision #9976223](https://github.com/MariaDB/server/commit/9976223)\
  2016-11-28 17:28:37 +0400
  * [MDEV-11171](https://jira.mariadb.org/browse/MDEV-11171) Assertion `m_cpp_buf <= ptr && ptr <= m_cpp_buf + m_buf_length' failed in` Lex\_input\_stream::body\_utf8\_append(const char\*, const char\*)\`
* [Revision #adc38ed](https://github.com/MariaDB/server/commit/adc38ed)\
  2016-11-14 08:02:35 +0100
  * Restore MY\_WME flag for my\_pread in read\_ddl\_log\_entry, fix errors in buildbot
* [Revision #96b62b5](https://github.com/MariaDB/server/commit/96b62b5)\
  2016-11-11 20:55:03 -0800
  * Fixed bug [MDEV-11161](https://jira.mariadb.org/browse/MDEV-11161). The flag `TABLE_LIST::fill_me` must be reset to false at the prepare phase for any materialized derived table used in the executed query. Otherwise if the optimizer decides to generate a key for such a table it is generated only for the first execution of the query.
* [Revision #10aee66](https://github.com/MariaDB/server/commit/10aee66)\
  2016-11-10 23:47:42 +0000
  * [MDEV-11248](https://jira.mariadb.org/browse/MDEV-11248) Fix passing offset parameter to my\_file\_pread in read\_ddl\_log\_file\_entry
* [Revision #e0f48e5](https://github.com/MariaDB/server/commit/e0f48e5)\
  2016-11-03 16:21:48 +0000
  * [MDEV-11214](https://jira.mariadb.org/browse/MDEV-11214) Windows : MSI installation fails, if run by a service user (e.g LocalSystem)
* [Revision #2a2e79b](https://github.com/MariaDB/server/commit/2a2e79b)\
  2016-10-27 13:03:49 +0000
  * [MDEV-11157](https://jira.mariadb.org/browse/MDEV-11157) Windows - Upgrade installer to use HeidiSQL 9.4
* [Revision #d8cb682](https://github.com/MariaDB/server/commit/d8cb682)\
  2016-10-26 21:54:41 +0000
  * VS2015 build fixes
* [Revision #aec4321](https://github.com/MariaDB/server/commit/aec4321)\
  2016-10-26 21:38:58 +0000
  * [MDEV-9409](https://jira.mariadb.org/browse/MDEV-9409) Windows - workaround VS2015 CRT bug that makes mysqldump/mysql\_install\_db.exe fail
* [Revision #106664f](https://github.com/MariaDB/server/commit/106664f)\
  2016-12-08 02:03:34 +0530
  * [MDEV-11162](https://jira.mariadb.org/browse/MDEV-11162) Assertion \`\`num\_records == m\_idx\_array.size()'`failed in`Filesort\_buffer::alloc\_sort\_buffer(uint, uint)\`
* [Revision #822fb79](https://github.com/MariaDB/server/commit/822fb79)\
  2016-12-07 23:44:52 +0530
  * [MDEV-11162](https://jira.mariadb.org/browse/MDEV-11162) Assertion \`\`num\_records == m\_idx\_array.size()'`failed in`Filesort\_buffer::alloc\_sort\_buffer(uint, uint)\`
* [Revision #c32d3e1](https://github.com/MariaDB/server/commit/c32d3e1)\
  2016-12-07 18:05:13 +0400
  * [MDEV-10787](https://jira.mariadb.org/browse/MDEV-10787) Assertion \`\`ltime->neg == 0'`failed in`void date\_to\_datetime(MYSQL\_TIME\*)\`
* [Revision #52b590b](https://github.com/MariaDB/server/commit/52b590b) 2016-12-07 10:04:10 +0400 - Merge pull request #271 from iangilfillan/10.0
* [Revision #3ada316969](https://github.com/MariaDB/server/commit/3ada316969)\
  2016-12-06 13:18:48 +0200
  * Update mysqldump man page
* [Revision #7f2fd34](https://github.com/MariaDB/server/commit/7f2fd34)\
  2016-12-02 14:34:45 +0100
  * [MDEV-11231](https://jira.mariadb.org/browse/MDEV-11231) Server crashes in check\_duplicate\_key on CREATE TABLE ... SELECT
* [Revision #c5ef621](https://github.com/MariaDB/server/commit/c5ef621) 2016-12-04 01:59:08 +0100 - Merge branch 'merge/merge-tokudb-5.6' into 10.0
* [Revision #d4f0686](https://github.com/MariaDB/server/commit/d4f0686)\
  2016-12-02 10:24:00 +0100
  * 5.6.34-79.1
* [Revision #f35b0d8](https://github.com/MariaDB/server/commit/f35b0d8) 2016-12-04 01:37:55 +0100 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #7436c3d](https://github.com/MariaDB/server/commit/7436c3d)\
  2016-12-02 10:22:18 +0100
  * 5.6.34-79.1
* [Revision #e4a0d75](https://github.com/MariaDB/server/commit/e4a0d75)\
  2016-12-04 01:35:57 +0100
  * import a test case from percona-server-5.6.34-79.1
* [Revision #e99990c](https://github.com/MariaDB/server/commit/e99990c)\
  2016-10-28 17:10:05 +0200
  * [MDEV-10744](https://jira.mariadb.org/browse/MDEV-10744): Roles are not fully case sensitive
* [Revision #525e214](https://github.com/MariaDB/server/commit/525e214)\
  2016-10-25 16:47:36 +0200
  * Remove labs() warning from maria and myisam storage engines
* [Revision #748d993](https://github.com/MariaDB/server/commit/748d993)\
  2016-11-29 11:28:15 -0800
  * Fixed bug [MDEV-11364](https://jira.mariadb.org/browse/MDEV-11364). The function `Item_func_isnull::update_used_tables()` must handle the case when the predicate is over not nullable column in a special way. This is actually a bug of [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)/5.5, but it's probably hard to demonstrate that it can cause problems there.
* [Revision #b209bc3](https://github.com/MariaDB/server/commit/b209bc3)\
  2016-11-29 09:01:46 +0200
  * [MDEV-10427](https://jira.mariadb.org/browse/MDEV-10427): innodb.innodb-wl5522-debug-zip fails sporadically in buildbot
* [Revision #dd0ff30](https://github.com/MariaDB/server/commit/dd0ff30)\
  2016-11-29 06:51:12 +0400
  * [MDEV-11343](https://jira.mariadb.org/browse/MDEV-11343) LOAD DATA INFILE fails to load data with an escape character followed by a multi-byte character
* [Revision #099ce1d](https://github.com/MariaDB/server/commit/099ce1d)\
  2016-11-25 15:59:47 +0400
  * [MDEV-11348](https://jira.mariadb.org/browse/MDEV-11348) LOAD DATA LOCAL INFILE crashes the server on loading a backslash followed by a multi-byte character
* [Revision #03ddc19](https://github.com/MariaDB/server/commit/03ddc19)\
  2016-11-17 15:15:20 +0200
  * [MDEV-6424](https://jira.mariadb.org/browse/MDEV-6424): MariaDB server crashes with assertion failure in file ha\_innodb.c line 11652
* [Revision #42a398b](https://github.com/MariaDB/server/commit/42a398b)\
  2016-11-17 12:04:39 +0400
  * Fixing a typo in the patch for [MDEV-10780](https://jira.mariadb.org/browse/MDEV-10780), which caused default.test failure.
* [Revision #390f2a0](https://github.com/MariaDB/server/commit/390f2a0)\
  2016-11-16 11:00:38 +0100
  * Fix incorrect reading of events from relaylog in parallel replication.
* [Revision #f1fcc1f](https://github.com/MariaDB/server/commit/f1fcc1f)\
  2016-11-15 23:00:11 +0100
  * Back-port `Master_info::using_parallel()` to 10.0.
* [Revision #9a09072](https://github.com/MariaDB/server/commit/9a09072) 2016-11-15 11:08:01 +0100 - Merge branch 'mdev10863' into 10.0
* [Revision #717f212](https://github.com/MariaDB/server/commit/717f212)\
  2016-11-04 12:33:42 +0100
  * [MDEV-10863](https://jira.mariadb.org/browse/MDEV-10863): parallel replication tries to continue from wrong position
* [Revision #1d9b043](https://github.com/MariaDB/server/commit/1d9b043)\
  2016-11-10 18:15:36 +0400
  * A join patch for [MDEV-10780](https://jira.mariadb.org/browse/MDEV-10780) and [MDEV-11265](https://jira.mariadb.org/browse/MDEV-11265)
* [Revision #9741e0e](https://github.com/MariaDB/server/commit/9741e0e)\
  2016-11-01 07:52:28 +0200
  * Initialize zip\_dict\_ids table and avoid referencing array items as currently MariaDB does not support compressed columns.
* [Revision #923a7f8](https://github.com/MariaDB/server/commit/923a7f8)\
  2016-10-31 12:16:53 +0200
  * [MDEV-11188](https://jira.mariadb.org/browse/MDEV-11188): rpl.rpl\_parallel\_partition fails with valgrind warnings in buildbot and outside
* [Revision #425d341](https://github.com/MariaDB/server/commit/425d341)\
  2016-10-28 11:46:15 -0400
  * bump the VERSION
* [Revision #cb7b03b](https://github.com/MariaDB/server/commit/cb7b03b)\
  2016-10-28 13:34:13 +0400
  * [MDEV-11164](https://jira.mariadb.org/browse/MDEV-11164) - hardening-wrapper has been removed from Debian Sid

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
