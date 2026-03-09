# MariaDB 10.0.25 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.25)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10025-release-notes)[Changelog](mariadb-10025-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 30 Apr 2016

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #9eba34f](https://github.com/MariaDB/server/commit/9eba34f)\
  2016-04-28 22:18:15 +0200
  * Fix crash due to heap corruption in main.shm
* [Revision #94bad73](https://github.com/MariaDB/server/commit/94bad73)\
  2016-04-28 21:59:23 +0400
  * [MDEV-9988](https://jira.mariadb.org/browse/MDEV-9988) - Insert cast to suppress -Wdynamic-class-memaccess
* [Revision #e581072](https://github.com/MariaDB/server/commit/e581072)\
  2016-04-27 18:16:03 +0200
  * Fix msxml6 search in Connect engine on Windows, as it fails on new builders.
* [Revision #cf22514](https://github.com/MariaDB/server/commit/cf22514)\
  2016-04-27 08:34:35 +0200
  * after-merge fixes for failures in buildbot
* [Revision #8b1563e](https://github.com/MariaDB/server/commit/8b1563e) 2016-04-26 23:48:18 +0200 - Merge branch 'connect/10.0' into 10.0
* [Revision #10de438](https://github.com/MariaDB/server/commit/10de438) 2016-04-25 11:41:48 +0200 - Merge branch 'ob-10.0' into 10.0
* [Revision #26adbb2](https://github.com/MariaDB/server/commit/26adbb2)\
  2016-04-25 00:13:06 +0200\
  \*
  * Fix an error causing MYSQL table to fail saying "no result set" when joining a table to a MYSQL indexed table. modified: storage/connect/myconn.cpp modified: storage/connect/myconn.h modified: storage/connect/tabmysql.cpp
* [Revision #6e48347](https://github.com/MariaDB/server/commit/6e48347) 2016-03-25 18:11:21 +0100 - Merge branch 'ob-10.0' into 10.0
* [Revision #8c9fd07](https://github.com/MariaDB/server/commit/8c9fd07)\
  2016-03-25 12:46:42 +0100\
  \*
  * Fix [MDEV-9779](https://jira.mariadb.org/browse/MDEV-9779). Avoid buffer overflow when setting partname. modified: storage/connect/ha\_connect.cc modified: storage/connect/ha\_connect.h
* [Revision #2c4715b](https://github.com/MariaDB/server/commit/2c4715b)\
  2016-03-25 11:11:25 +0100
  * Bigger partname to avoid [MDEV-9779](https://jira.mariadb.org/browse/MDEV-9779)
* [Revision #e80c4b3](https://github.com/MariaDB/server/commit/e80c4b3)\
  2016-03-24 23:36:39 +0100\
  \*
  * Fix [MDEV-9779](https://jira.mariadb.org/browse/MDEV-9779). Connection was not recognized in the option list. This was a regression bug. modified: storage/connect/ha\_connect.cc modified: storage/connect/mysql-test/connect/r/part\_table.result modified: storage/connect/mysql-test/connect/t/part\_table.test
* [Revision #cbe3511](https://github.com/MariaDB/server/commit/cbe3511) 2016-03-19 13:32:28 +0100 - Merge branch 'ob-10.0' into 10.0
* [Revision #c1efc4a](https://github.com/MariaDB/server/commit/c1efc4a)\
  2016-03-19 12:13:36 +0100\
  \*
  * Fix compile error when copying a string on itself. modified: storage/connect/value.cpp
* [Revision #433c8a8](https://github.com/MariaDB/server/commit/433c8a8) 2016-03-17 10:17:42 +0100 - Merge branch 'ob-10.0' into 10.0
* [Revision #6689097](https://github.com/MariaDB/server/commit/6689097)\
  2016-03-16 23:56:43 +0100\
  \*
  * Fix crash when sorting a TBL table with thread=yes. This was because Tablist can be NULL when no lacal tables are in the list. modified: storage/connect/tabtbl.cpp modified: storage/connect/mysql-test/connect/r/tbl.result modified: storage/connect/mysql-test/connect/t/tbl.test
* [Revision #fb9e2fa](https://github.com/MariaDB/server/commit/fb9e2fa)\
  2016-03-16 19:17:55 +0100\
  \*
  * Fix [MDEV-9603](https://jira.mariadb.org/browse/MDEV-9603) compiler error. modified: storage/connect/tabmysql.cpp
* [Revision #539b736](https://github.com/MariaDB/server/commit/539b736) 2016-02-20 10:40:32 +0100 - Merge branch 'ob-10.0' into 10.0
* [Revision #02fa3b8](https://github.com/MariaDB/server/commit/02fa3b8)\
  2016-02-20 01:02:48 +0100\
  \*
  * Fix to [MDEV-9579](https://jira.mariadb.org/browse/MDEV-9579) be testing for void result. modified: storage/connect/tabodbc.cpp
* [Revision #cfad394](https://github.com/MariaDB/server/commit/cfad394) 2016-04-26 23:43:48 +0200 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #5b8ac23](https://github.com/MariaDB/server/commit/5b8ac23)\
  2016-04-26 19:07:11 +0200
  * 5.6.29-76.2
* [Revision #c4dcfb6](https://github.com/MariaDB/server/commit/c4dcfb6) 2016-04-26 23:20:32 +0200 - Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #f1aae86](https://github.com/MariaDB/server/commit/f1aae86)\
  2016-04-26 19:05:10 +0200
  * 5.6.30
* [Revision #872649c](https://github.com/MariaDB/server/commit/872649c) 2016-04-26 23:05:26 +0200 - Merge branch '5.5' into 10.0
* [Revision #4f1ad43](https://github.com/MariaDB/server/commit/4f1ad43)\
  2016-04-26 16:15:15 +0400
  * [MDEV-9987](https://jira.mariadb.org/browse/MDEV-9987) - gen\_lex\_hash leaks memory, making LeakSanitizer builds fail
* [Revision #29868de](https://github.com/MariaDB/server/commit/29868de)\
  2016-04-26 12:58:14 +0200
  * [MDEV-9986](https://jira.mariadb.org/browse/MDEV-9986) Full-text search of the utf8mb4 column causes crash
* [Revision #7f5ceb7](https://github.com/MariaDB/server/commit/7f5ceb7)\
  2016-04-26 11:49:35 +0200
  * disable main.wait\_timeout\_not\_windows for embedded
* [Revision #2220480](https://github.com/MariaDB/server/commit/2220480)\
  2016-04-25 18:59:41 +0200
  * [MDEV-7775](https://jira.mariadb.org/browse/MDEV-7775) Wrong error message (Unknown error) when idle sessions are killed after wait\_timeout
* [Revision #a98ecc2](https://github.com/MariaDB/server/commit/a98ecc2)\
  2016-04-23 12:19:40 +0200
  * support SEARCH\_RANGE in search\_pattern\_in\_file.inc
* [Revision #2b7573e](https://github.com/MariaDB/server/commit/2b7573e)\
  2016-04-24 13:36:51 +0400
  * [MDEV-9975](https://jira.mariadb.org/browse/MDEV-9975) - main.partition\_innodb\_plugin fails sporadically
* [Revision #19e3597](https://github.com/MariaDB/server/commit/19e3597)\
  2016-04-07 10:47:46 +0300
  * [MDEV-9142](https://jira.mariadb.org/browse/MDEV-9142) :Adding Constraint with no database reference results in ERROR 1046 (3D000) at line 13: No database selected.
* [Revision #0ea4c73](https://github.com/MariaDB/server/commit/0ea4c73)\
  2016-04-23 12:15:18 +0400
  * Fixed compilation failure due to unused var.
* [Revision #618e300](https://github.com/MariaDB/server/commit/618e300)\
  2016-04-22 12:57:39 +0400
  * [MDEV-9970](https://jira.mariadb.org/browse/MDEV-9970) - main.sp-threads fails sporadically
* [Revision #bd75ee7](https://github.com/MariaDB/server/commit/bd75ee7)\
  2016-04-22 09:10:00 -0400
  * bump the VERSION
* [Revision #3f0d07e](https://github.com/MariaDB/server/commit/3f0d07e)\
  2016-04-22 16:04:20 +0400
  * [MDEV-9372](https://jira.mariadb.org/browse/MDEV-9372) select 100 between 1 and 9223372036854775808 returns false
* [Revision #0991e19e](https://github.com/MariaDB/server/commit/0991e19e) 2016-04-20 20:25:46 +0200 - Merge branch 'bb-5.5-serg' into 5.5
* [Revision #63c834e](https://github.com/MariaDB/server/commit/63c834e) 2016-04-20 18:56:41 +0200 - Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #c9e56d5](https://github.com/MariaDB/server/commit/c9e56d5)\
  2016-04-18 17:38:05 +0200
  * 5.5.48-37.8
* [Revision #24ac546](https://github.com/MariaDB/server/commit/24ac546)\
  2016-04-20 18:27:23 +0200
  * use consistent error messaging for IGNORE
* [Revision #9e826bf](https://github.com/MariaDB/server/commit/9e826bf)\
  2016-04-20 15:28:44 +0200
  * trivial optimization
* [Revision #8f1f869](https://github.com/MariaDB/server/commit/8f1f869)\
  2016-04-20 15:26:37 +0200
  * another test case for ER\_DATA\_OUT\_OF\_RANGE on insert
* [Revision #b069d19](https://github.com/MariaDB/server/commit/b069d19) 2016-04-20 15:25:55 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #1bc0b0b](https://github.com/MariaDB/server/commit/1bc0b0b)\
  2016-04-19 11:08:16 +0200
  * fix a couple of dbug tests not to write to /tmp
* [Revision #cc04a9f](https://github.com/MariaDB/server/commit/cc04a9f)\
  2016-04-18 18:30:42 +0200
  * [MDEV-9835](https://jira.mariadb.org/browse/MDEV-9835) Valid password is not working after server restart
* [Revision #608c0e1](https://github.com/MariaDB/server/commit/608c0e1)\
  2016-04-18 11:57:34 +0200
  * [MDEV-5982](https://jira.mariadb.org/browse/MDEV-5982) `make` fail @ ".../libmysql\_versions.ld:155:9: invalid use of VERSION in input file"
* [Revision #ce35530](https://github.com/MariaDB/server/commit/ce35530)\
  2016-04-17 19:52:15 +0200
  * [MDEV-9885](https://jira.mariadb.org/browse/MDEV-9885) Client doesn't start if 'TERM' unknown
* [Revision #95fe71a](https://github.com/MariaDB/server/commit/95fe71a)\
  2016-04-17 18:51:54 +0200
  * [MDEV-9707](https://jira.mariadb.org/browse/MDEV-9707) MAX(timestamp(6) column) in correlated sub-query returns non-existent row data in original table
* [Revision #3294cd1](https://github.com/MariaDB/server/commit/3294cd1)\
  2016-04-16 17:36:47 +0200
  * [MDEV-9929](https://jira.mariadb.org/browse/MDEV-9929) MariaDB segfaults on command "mysqld --version" with ignore-db-dir option on /etc/my.cnf
* [Revision #4f133fb](https://github.com/MariaDB/server/commit/4f133fb)\
  2016-04-16 12:39:20 +0200
  * [MDEV-9493](https://jira.mariadb.org/browse/MDEV-9493) --tc-heuristic-recover option values off by one
* [Revision #edf71fd](https://github.com/MariaDB/server/commit/edf71fd)\
  2016-04-16 10:28:03 +0200
  * [MDEV-9928](https://jira.mariadb.org/browse/MDEV-9928) LC\_TIME\_NAMES=de\_AT; unusual name for february
* [Revision #9c64735](https://github.com/MariaDB/server/commit/9c64735)\
  2016-03-29 12:50:56 +0200
  * [MDEV-9748](https://jira.mariadb.org/browse/MDEV-9748) Include Twin (mysys\_err.h is included twice in mysys/my\_copy.c)
* [Revision #2a45fa9](https://github.com/MariaDB/server/commit/2a45fa9)\
  2016-04-20 19:03:59 +0200
  * [MDEV-9836](https://jira.mariadb.org/browse/MDEV-9836) Connection lost when using SSL
* [Revision #0c0a865](https://github.com/MariaDB/server/commit/0c0a865)\
  2016-04-19 16:16:13 +0400
  * [MDEV-9943](https://jira.mariadb.org/browse/MDEV-9943) - TokuDB fails to compile with gcc 5.2.1
* [Revision #62122ba](https://github.com/MariaDB/server/commit/62122ba)\
  2016-04-20 00:36:58 +0300
  * [MDEV-9953](https://jira.mariadb.org/browse/MDEV-9953) Debian packages install broken 'maria' test suite which cannot be run
* [Revision #e90f8b7](https://github.com/MariaDB/server/commit/e90f8b7)\
  2016-04-20 11:11:13 +0400
  * [MDEV-9413](https://jira.mariadb.org/browse/MDEV-9413) "datetime >= coalesce(c1(NULL))" doesn't return expected NULL
* [Revision #2564650](https://github.com/MariaDB/server/commit/2564650)\
  2016-04-20 11:02:34 +0400
  * [MDEV-9662](https://jira.mariadb.org/browse/MDEV-9662) Assertion \`precision || !scale' failed in my\_decimal\_precision\_to\_length\_no\_truncation(uint, uint8, bool)
* [Revision #9a98714](https://github.com/MariaDB/server/commit/9a98714)\
  2016-04-20 08:53:30 +0400
  * [MDEV-9745](https://jira.mariadb.org/browse/MDEV-9745) Crash with CASE WHEN TRUE THEN COALESCE(CAST(NULL AS UNSIGNED)) ELSE 4 END
* [Revision #6c0e231](https://github.com/MariaDB/server/commit/6c0e231)\
  2016-04-19 14:05:52 +0400
  * [MDEV-9945](https://jira.mariadb.org/browse/MDEV-9945) - main.kill\_processlist-6619 fails sporadically
* [Revision #18ff6f6](https://github.com/MariaDB/server/commit/18ff6f6)\
  2016-04-19 12:38:00 +0400
  * [MDEV-9944](https://jira.mariadb.org/browse/MDEV-9944) - main.events\_2 fails sporadically
* [Revision #6fd54c0](https://github.com/MariaDB/server/commit/6fd54c0)\
  2016-04-18 23:15:15 +0400
  * [MDEV-9521](https://jira.mariadb.org/browse/MDEV-9521) Least function returns 0000-00-00 for null date columns instead of null
* [Revision #777c213](https://github.com/MariaDB/server/commit/777c213)\
  2016-04-02 00:04:47 +0400
  * [MDEV-9862](https://jira.mariadb.org/browse/MDEV-9862) Illegal mix of collation, when comparing column with CASE expression
* [Revision #4995bcf](https://github.com/MariaDB/server/commit/4995bcf)\
  2016-04-26 17:00:47 +0200
  * [MDEV-9610](https://jira.mariadb.org/browse/MDEV-9610) Trigger on normal table can't insert into CONNECT engine table - Access Denied
* [Revision #b7ad1ba](https://github.com/MariaDB/server/commit/b7ad1ba)\
  2016-04-26 20:11:40 +0300
  * Fixed mutex that wasn't properly unlocked (typo in last patch)
* [Revision #44554d6](https://github.com/MariaDB/server/commit/44554d6)\
  2016-04-26 14:37:19 +0400
  * [MDEV-9605](https://jira.mariadb.org/browse/MDEV-9605) mysqlbinlog does not accept ssl-ca option as expected. Added SSL support to the mysqlbinlog.
* [Revision #0dbc664](https://github.com/MariaDB/server/commit/0dbc664)\
  2016-04-26 12:22:02 +0300
  * Fix for [MDEV-9679](https://jira.mariadb.org/browse/MDEV-9679) main.delayed fails sporadically
* [Revision #f6cc7f1](https://github.com/MariaDB/server/commit/f6cc7f1)\
  2016-04-25 15:37:24 +0300
  * Fixed failing test cases and compiler warnings - Fixed wait condition in kill\_processlist-6619 - Updated Ssl\_chiper for openssl tests - Added supression for valgrinds when using libcrypto - Fixed wrong argument to pthread\_mutex in server\_audit.c when compiling with debug - Adding missing debug\_sync\_update() to debug\_sync.h - Added initializers to some variables and fixed error handling in jsonudf.cpp - Fixed cluster\_filter\_unpack\_varchar which doesn't have a stable index type. - Updated compiler\_warnings.supp
* [Revision #ce38add](https://github.com/MariaDB/server/commit/ce38add)\
  2016-04-24 11:18:59 +0200
  * [MDEV-9617](https://jira.mariadb.org/browse/MDEV-9617) solaris sparc build fails on 10.0
* [Revision #7b58fd5](https://github.com/MariaDB/server/commit/7b58fd5)\
  2016-04-23 18:49:19 +0200
  * tests -DDEFAULT\_CHARSET=utf8 -DDEFAULT\_COLLATION=utf8\_general\_ci
* [Revision #0ee919b](https://github.com/MariaDB/server/commit/0ee919b)\
  2016-04-22 13:15:04 +0200
  * [MDEV-8480](https://jira.mariadb.org/browse/MDEV-8480) mysql-test - main.func\_encrypt\_ucs2 fails if FIPS=1
* [Revision #797cadc](https://github.com/MariaDB/server/commit/797cadc)\
  2016-04-22 13:13:48 +0200
  * [MDEV-8482](https://jira.mariadb.org/browse/MDEV-8482) mysql-test - main.func\_encrypt fails if FIPS=1
* [Revision #906f97d](https://github.com/MariaDB/server/commit/906f97d)\
  2016-04-22 13:10:14 +0200
  * [MDEV-8481](https://jira.mariadb.org/browse/MDEV-8481) mysql-test - main.func\_crypt fails if FIPS=1
* [Revision #78989b6](https://github.com/MariaDB/server/commit/78989b6)\
  2016-04-22 08:46:38 +0200
  * [MDEV-9168](https://jira.mariadb.org/browse/MDEV-9168) altering a column comment does a full copy
* [Revision #b233b15](https://github.com/MariaDB/server/commit/b233b15)\
  2016-04-22 08:25:36 +0200
  * [MDEV-9868](https://jira.mariadb.org/browse/MDEV-9868) Altering a partitioned table comment does a full copy
* [Revision #97728e1](https://github.com/MariaDB/server/commit/97728e1)\
  2016-04-22 08:16:06 +0200
  * comment
* [Revision #d821dd1](https://github.com/MariaDB/server/commit/d821dd1)\
  2016-04-21 14:51:37 +0200
  * [MDEV-9580](https://jira.mariadb.org/browse/MDEV-9580) SHOW GRANTS FOR \<current\_user> fails
* [Revision #23b1b69](https://github.com/MariaDB/server/commit/23b1b69)\
  2016-04-09 22:39:22 +0930
  * Comment from [153](https://github.com/MariaDB/server/pull/153)
* [Revision #6651005](https://github.com/MariaDB/server/commit/6651005)\
  2016-01-22 21:13:33 +1030
  * Fix for [MDEV-8206](https://jira.mariadb.org/browse/MDEV-8206), as per Jira comments of 2015-11-16 and 2015-11-30
* [Revision #011497b](https://github.com/MariaDB/server/commit/011497b)\
  2016-04-21 10:04:26 +0200
  * [MDEV-9869](https://jira.mariadb.org/browse/MDEV-9869) INSTALL SONAME 'ha\_connect'
* [Revision #250a89c](https://github.com/MariaDB/server/commit/250a89c)\
  2016-04-22 15:30:10 +0400
  * [MDEV-9283](https://jira.mariadb.org/browse/MDEV-9283) - Debian: the Lintian complains about "shlib-calls-exit" in ha\_oqgraph.so
* [Revision #994030c](https://github.com/MariaDB/server/commit/994030c)\
  2016-04-21 16:51:00 +0400
  * [MDEV-8889](https://jira.mariadb.org/browse/MDEV-8889) - Assertion \`next\_insert\_id == 0' failed in handler::ha\_external\_lock
* [Revision #298e1d3f](https://github.com/MariaDB/server/commit/298e1d3f)\
  2016-04-22 11:36:10 +0300
  * Improve error diagnostics on I/O errors. If node->name is NULL try to use space->name instead.
* [Revision #628bc57](https://github.com/MariaDB/server/commit/628bc57)\
  2016-04-21 10:52:52 +0300
  * [MDEV-9918](https://jira.mariadb.org/browse/MDEV-9918): \[ERROR] mysqld got signal 11 during ALTER TABLE `name` COLUMN ADD
* [Revision #e5410da](https://github.com/MariaDB/server/commit/e5410da)\
  2016-04-21 08:18:54 -0700
  * SEGFAULT in get\_column\_grant()
* [Revision #072ca71](https://github.com/MariaDB/server/commit/072ca71)\
  2016-04-20 18:20:31 +0400
  * [MDEV-9281](https://jira.mariadb.org/browse/MDEV-9281) - Debian: the Lintian complains about "shlib-calls-exit" in handlersocket.so [MDEV-9278](https://jira.mariadb.org/browse/MDEV-9278) - Debian: the Lintian complains about "shlib-calls-exit" in ha\_spider.so
* [Revision #f8adecc](https://github.com/MariaDB/server/commit/f8adecc)\
  2016-04-04 17:04:14 +0300
  * [MDEV-9713](https://jira.mariadb.org/browse/MDEV-9713) Sporadic test failure: sys\_vars.innodb\_buffer\_pool\_load\_now\_basic
* [Revision #f6d99a0](https://github.com/MariaDB/server/commit/f6d99a0)\
  2016-03-24 08:57:41 +0100
  * [MDEV-9773](https://jira.mariadb.org/browse/MDEV-9773): Memory corruption in mariadb\_dyncol\_unpack
* [Revision #22ebf3c](https://github.com/MariaDB/server/commit/22ebf3c)\
  2016-03-18 16:54:38 +0100
  * [MDEV-9527](https://jira.mariadb.org/browse/MDEV-9527) build FAILs with GCC 5.1 with release supported "-std=c+11"
* [Revision #98ea806](https://github.com/MariaDB/server/commit/98ea806) 2016-03-21 11:54:45 +0100 - Merge branch '5.5' into 10.0
* [Revision #11b77e9](https://github.com/MariaDB/server/commit/11b77e9)\
  2016-03-18 16:55:11 +0100
  * [MDEV-9527](https://jira.mariadb.org/browse/MDEV-9527) build FAILs with GCC 5.1 with release supported "-std=c+11"
* [Revision #fc2c1e4](https://github.com/MariaDB/server/commit/fc2c1e4)\
  2016-03-17 21:29:52 +0100
  * [MDEV-9733](https://jira.mariadb.org/browse/MDEV-9733) Server crashes in lf\_pinbox\_real\_free on replication slaves
* [Revision #0b9fb9a](https://github.com/MariaDB/server/commit/0b9fb9a)\
  2016-03-17 10:45:15 +0100
  * [MDEV-9568](https://jira.mariadb.org/browse/MDEV-9568) mysqlcheck crashes with nonexistent table name
* [Revision #c29e450](https://github.com/MariaDB/server/commit/c29e450)\
  2016-02-26 03:02:07 +0200
  * [MDEV-4070](https://jira.mariadb.org/browse/MDEV-4070) sys\_vars.secure\_file\_priv fails sporadically if it's executed with --mem
* [Revision #ceba41c](https://github.com/MariaDB/server/commit/ceba41c)\
  2016-01-24 17:41:11 +0100
  * [MDEV-9299](https://jira.mariadb.org/browse/MDEV-9299) Test main.events\_2 incompatible with Debian reproducibility testing framework
* [Revision #b9e5718](https://github.com/MariaDB/server/commit/b9e5718)\
  2016-03-18 13:57:46 +0100
  * [MDEV-9679](https://jira.mariadb.org/browse/MDEV-9679) main.delayed fails sporadically
* [Revision #d158ba62](https://github.com/MariaDB/server/commit/d158ba62)\
  2016-03-17 17:41:45 +0100
  * ASAN error in OQGraph engine
* [Revision #a2de604](https://github.com/MariaDB/server/commit/a2de604)\
  2016-03-17 17:40:53 +0100
  * ASAN error in CONNECT engine
* [Revision #2ed882f](https://github.com/MariaDB/server/commit/2ed882f)\
  2016-03-17 17:38:12 +0100
  * update tests and results
* [Revision #620d975](https://github.com/MariaDB/server/commit/620d975)\
  2016-03-17 13:08:17 +0100
  * typo in a comment
* [Revision #7baff9f](https://github.com/MariaDB/server/commit/7baff9f)\
  2016-03-17 13:08:06 +0100
  * fix extension\_based\_table\_discovery for partitioned tables
* [Revision #8b9432f](https://github.com/MariaDB/server/commit/8b9432f)\
  2016-03-17 12:02:28 +0100
  * [MDEV-9698](https://jira.mariadb.org/browse/MDEV-9698) Buffer overflow in extension\_based\_table\_discovery()
* [Revision #ee68777](https://github.com/MariaDB/server/commit/ee68777)\
  2016-02-27 20:08:59 +0100
  * Use /bin/sh
* [Revision #e69c6e8](https://github.com/MariaDB/server/commit/e69c6e8)\
  2016-02-18 21:43:19 +0100
  * [MDEV-9560](https://jira.mariadb.org/browse/MDEV-9560) [Mariadb 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) Crashes when replicating from 10.0
* [Revision #96a7e74](https://github.com/MariaDB/server/commit/96a7e74)\
  2016-03-18 00:28:18 +0200
  * Extra space in the result file
* [Revision #3badfe0](https://github.com/MariaDB/server/commit/3badfe0) 2016-03-16 12:21:38 +0400 - Merge pull request #164 from iangilfillan/10.0
* [Revision #497800e](https://github.com/MariaDB/server/commit/497800e)\
  2016-03-15 14:41:29 +0200
  * Update sponsors
* [Revision #0125e58](https://github.com/MariaDB/server/commit/0125e58)\
  2016-03-12 17:50:57 +0200
  * [MDEV-9713](https://jira.mariadb.org/browse/MDEV-9713) Sporadic test failure: sys\_vars.innodb\_buffer\_pool\_load\_now\_basic
* [Revision #8103526](https://github.com/MariaDB/server/commit/8103526)\
  2016-03-11 13:36:29 +0200
  * [MDEV-9667](https://jira.mariadb.org/browse/MDEV-9667): Server hangs after select count(distinct name) from t2 where a=8366 and b>=5 and b<=5;
* [Revision #8942824](https://github.com/MariaDB/server/commit/8942824)\
  2016-03-10 13:08:34 +0400
  * Fixed false errors returned by logrotate script
* [Revision #d7721fc](https://github.com/MariaDB/server/commit/d7721fc) 2016-03-09 09:55:13 +0400 - Merge pull request #162 from iangilfillan/10.0
* [Revision #6befd84](https://github.com/MariaDB/server/commit/6befd84)\
  2016-03-08 15:24:01 +0200
  * Update AskMonty and Atlassian references to MariaDB
* [Revision #3c37f35](https://github.com/MariaDB/server/commit/3c37f35) 2016-03-07 14:25:02 +0400 - Merge pull request #159 from ottok/ok-debpkg-10.0
* [Revision #1777fd5](https://github.com/MariaDB/server/commit/1777fd5)\
  2016-03-04 02:09:37 +0200
  * Fix spelling: occurred, execute, which etc
* [Revision #f825191](https://github.com/MariaDB/server/commit/f825191)\
  2016-03-03 08:40:49 +0100
  * [MDEV-9595](https://jira.mariadb.org/browse/MDEV-9595): Shutdown takes forever with many replication channels
* [Revision #c3071af](https://github.com/MariaDB/server/commit/c3071af) 2016-03-01 10:45:33 +0400 - Merge pull request #158 from ottok/ok-debpkg-10.0
* [Revision #802843e](https://github.com/MariaDB/server/commit/802843e)\
  2016-02-29 23:02:53 +0200
  * [MDEV-9643](https://jira.mariadb.org/browse/MDEV-9643): Don't emit any "deb-systemd-helper not found" warnings
* [Revision #e7d50ef](https://github.com/MariaDB/server/commit/e7d50ef)\
  2016-02-26 00:25:55 +0200
  * [MDEV-7907](https://jira.mariadb.org/browse/MDEV-7907) tokudb.cluster\_filter\_unpack\_varchar\_hidden fails sporadically in buildbot
* [Revision #5f2f3c4](https://github.com/MariaDB/server/commit/5f2f3c4)\
  2016-02-18 09:22:41 +0100
  * connect engine compiler warnings

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
