# MariaDB 10.1.14 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.14)[Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-14-release-notes)[Changelog](mariadb-10114-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 10 May 2016

For the highlights of this release, see the [release notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #ee0695b](https://github.com/MariaDB/server/commit/ee0695b)\
  2016-05-08 13:37:12 +0300
  * Fix 32-bit sysvars test
* [Revision #234efb1](https://github.com/MariaDB/server/commit/234efb1)\
  2016-05-08 08:21:57 +0200
  * update 32-bit rdiff results
* [Revision #af93c02](https://github.com/MariaDB/server/commit/af93c02)\
  2016-05-07 09:12:48 +0200
  * [MDEV-10034](https://jira.mariadb.org/browse/MDEV-10034) Embedded server crashes on CREATE TABLE in PS protocol
* [Revision #5534d81](https://github.com/MariaDB/server/commit/5534d81)\
  2016-05-06 13:56:25 +0300
  * Merged change from MySQL 5.6 to [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) XtraDB including the test case
* [Revision #1512078](https://github.com/MariaDB/server/commit/1512078)\
  2016-04-29 10:50:39 -0400
  * [MDEV-9851](https://jira.mariadb.org/browse/MDEV-9851): CREATE USER w/o IDENTIFIED BY clause causes crash when using cracklib plugin
* [Revision #edbd0ce](https://github.com/MariaDB/server/commit/edbd0ce)\
  2016-04-29 09:37:00 -0400
  * [MDEV-9171](https://jira.mariadb.org/browse/MDEV-9171): innodb.innodb\_uninstall Test Failure
* [Revision #9a5c75a](https://github.com/MariaDB/server/commit/9a5c75a)\
  2016-04-29 09:34:44 -0400
  * [MDEV-9853](https://jira.mariadb.org/browse/MDEV-9853): WSREP says it cannot get fake InnoDB transaction ID followed by segmentation fault
* [Revision #9b2151f](https://github.com/MariaDB/server/commit/9b2151f)\
  2016-03-30 00:35:11 -0400
  * metadata\_lock\_info: Add compile time assertions
* [Revision #7abb570](https://github.com/MariaDB/server/commit/7abb570)\
  2016-03-30 00:22:38 -0400
  * [MDEV-6211](https://jira.mariadb.org/browse/MDEV-6211): MariaDB-Galera-server uses 'socat', but 'socat' is not in the dependency list
* [Revision #0a1c2a2](https://github.com/MariaDB/server/commit/0a1c2a2) 2016-05-05 09:15:04 -0400 - Merge branch '10.0-galera' into 10.1
* [Revision #c0238be](https://github.com/MariaDB/server/commit/c0238be) 2016-04-29 16:59:25 -0400 - Merge branch '5.5-galera' into 10.0-galera
* [Revision #51a32eb](https://github.com/MariaDB/server/commit/51a32eb)\
  2016-04-27 12:29:25 -0400
  * [MDEV-9884](https://jira.mariadb.org/browse/MDEV-9884): Existing /var/lib/mysql/.sst directory (with contents) causes SST to fail with xtrabackup-v2
* [Revision #43e19b3](https://github.com/MariaDB/server/commit/43e19b3)\
  2016-04-23 12:15:18 +0400
  * Fixed compilation failure due to unused var.
* [Revision #4f1c197](https://github.com/MariaDB/server/commit/4f1c197) 2016-04-25 11:06:16 -0400 - Merge tag 'mariadb-5.5.49' into 5.5-galera
* [Revision #8a1efa1](https://github.com/MariaDB/server/commit/8a1efa1) 2016-04-29 16:50:58 -0400 - Merge branch '10.0' into 10.0-galera
* [Revision #a87507e](https://github.com/MariaDB/server/commit/a87507e)\
  2016-05-05 15:39:04 +0400
  * [MDEV-9712](https://jira.mariadb.org/browse/MDEV-9712) Performance degradation of nested NULLIF
* [Revision #19c4d22](https://github.com/MariaDB/server/commit/19c4d22)\
  2016-05-05 12:35:12 +0200
  * skip debug\_sync test in release builds
* [Revision #4025251](https://github.com/MariaDB/server/commit/4025251)\
  2016-05-05 11:42:18 +0200
  * fix rpm installation issues on Fedoras
* [Revision #3a88adc](https://github.com/MariaDB/server/commit/3a88adc)\
  2016-05-05 11:28:35 +0400
  * [MDEV-717](https://jira.mariadb.org/browse/MDEV-717) [Bug #1003679](https://bugs.launchpad.net/bugs/1003679) - Wrong binlog order on concurrent DROP schema and CREATE function.
* [Revision #46973bb](https://github.com/MariaDB/server/commit/46973bb) 2016-05-05 08:47:17 +0200 - Merge branch 'bb-10.1-merge' into 10.1
* [Revision #1532598](https://github.com/MariaDB/server/commit/1532598)\
  2016-05-03 20:31:02 +0200
  * [MDEV-9155](https://jira.mariadb.org/browse/MDEV-9155) Enabling Defragmenting in 10.1.8 still causes OPTIMIZE TABLE to take metadatalocks
* [Revision #5ef0ce4](https://github.com/MariaDB/server/commit/5ef0ce4)\
  2016-05-03 13:07:05 +0200
  * comments
* [Revision #92e47c3](https://github.com/MariaDB/server/commit/92e47c3)\
  2016-05-02 18:28:40 +0200
  * test for group by pushdown with a view
* [Revision #ea195d3](https://github.com/MariaDB/server/commit/ea195d3)\
  2016-05-01 19:33:25 +0200
  * [MDEV-9949](https://jira.mariadb.org/browse/MDEV-9949) Connect Engine: long SRCDEF leads to broken table
* [Revision #09464dd](https://github.com/MariaDB/server/commit/09464dd)\
  2016-04-30 22:50:06 +0200
  * small parser cleanup
* [Revision #bf9404d](https://github.com/MariaDB/server/commit/bf9404d)\
  2016-05-04 16:05:30 +0200
  * protect against corrupted frms
* [Revision #bba3d42](https://github.com/MariaDB/server/commit/bba3d42)\
  2016-04-30 10:27:42 +0200
  * [MDEV-9926](https://jira.mariadb.org/browse/MDEV-9926) probes\_mysql.h includes nonexisting files
* [Revision #4db2ebb](https://github.com/MariaDB/server/commit/4db2ebb)\
  2016-04-30 09:09:10 +0200
  * [MDEV-9940](https://jira.mariadb.org/browse/MDEV-9940) CREATE ROLE blocked by password validation plugin
* [Revision #357f4d8](https://github.com/MariaDB/server/commit/357f4d8) 2016-05-05 01:04:05 +0200 - Merge branch 'connect/10.1' into 10.1
* [Revision #4a62480](https://github.com/MariaDB/server/commit/4a62480)\
  2016-04-26 11:22:30 +0200\
  \*
  * Add the use of prepared statement in the JDBC table type. modified: storage/connect/jdbconn.cpp modified: storage/connect/jdbconn.h modified: storage/connect/tabjdbc.cpp modified: storage/connect/tabjdbc.h
* [Revision #c086a96](https://github.com/MariaDB/server/commit/c086a96)\
  2016-04-24 19:56:32 +0200\
  \*
  * Fix an error causing MYSQL table to fail saying "no result set" when joining a table to a MYSQL indexed table. modified: storage/connect/myconn.cpp modified: storage/connect/myconn.h modified: storage/connect/tabmysql.cpp
* [Revision #afecdd2](https://github.com/MariaDB/server/commit/afecdd2)\
  2016-04-23 23:20:10 +0200\
  \*
  * Fix and error causing remote indexing to fail when for not unique index. Was experienced with MYSQL, ODBC and JDBC tables. modified: storage/connect/connect.cc
* [Revision #a1b2a28](https://github.com/MariaDB/server/commit/a1b2a28)\
  2016-03-25 13:02:34 +0100\
  \*
  * Fix [MDEV-9779](https://jira.mariadb.org/browse/MDEV-9779). Avoid buffer overflow when setting partname. modified: storage/connect/ha\_connect.cc modified: storage/connect/ha\_connect.h
* [Revision #d681c50](https://github.com/MariaDB/server/commit/d681c50)\
  2016-03-24 23:18:54 +0100\
  \*
  * Fix [MDEV-9779](https://jira.mariadb.org/browse/MDEV-9779). Connection was not recognized in the option list. This was a regression bug. modified: storage/connect/ha\_connect.cc modified: storage/connect/mysql-test/connect/r/part\_table.result modified: storage/connect/mysql-test/connect/t/part\_table.test
* [Revision #4040565](https://github.com/MariaDB/server/commit/4040565)\
  2016-05-04 20:28:20 +0200
  * fixes for buildbot
* [Revision #87e3e67](https://github.com/MariaDB/server/commit/87e3e67) 2016-05-04 15:23:26 +0200 - Merge branch '10.0' into 10.1
* [Revision #cee9ab9](https://github.com/MariaDB/server/commit/cee9ab9)\
  2016-04-30 11:23:46 -0400
  * bump the VERSION
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
* [Revision #fba385e](https://github.com/MariaDB/server/commit/fba385e)\
  2016-02-21 22:00:58 +0100
  * [MDEV-9487](https://jira.mariadb.org/browse/MDEV-9487): Server crashes in Time\_and\_counter\_tracker::incr\_loops with UNION in ALL subquery
* [Revision #a02d402](https://github.com/MariaDB/server/commit/a02d402)\
  2016-05-04 11:42:39 +0400
  * [MDEV-9618](https://jira.mariadb.org/browse/MDEV-9618) solaris sparc build fails on 10.1.
* [Revision #5dd0c77](https://github.com/MariaDB/server/commit/5dd0c77)\
  2016-05-03 20:53:29 +0300
  * [MDEV-9362](https://jira.mariadb.org/browse/MDEV-9362): InnoDB tables using DATA\_DIRECTORY created using MySQL 5.6 do not work with [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)
* [Revision #80da57c](https://github.com/MariaDB/server/commit/80da57c)\
  2016-05-03 20:13:58 +0200
  * remove the forgotten PARENT\_SCOPE
* [Revision #67723e9](https://github.com/MariaDB/server/commit/67723e9)\
  2016-05-03 15:23:34 +0200
  * Move MYSQL\_ADD\_PLUGIN outside of IF(OQGRAPH\_OK) condition, otherwise the plugin does not get compiled if cmake is called multiple times.
* [Revision #673efd0](https://github.com/MariaDB/server/commit/673efd0)\
  2016-05-03 15:18:55 +0200
  * [MDEV-10015](https://jira.mariadb.org/browse/MDEV-10015) Fix oqgraph compilation on Windows
* [Revision #94cd0f6](https://github.com/MariaDB/server/commit/94cd0f6)\
  2016-05-02 12:58:57 +0400
  * [MDEV-9898](https://jira.mariadb.org/browse/MDEV-9898) SET ROLE NONE can crash mysqld.
* [Revision #ad4239c](https://github.com/MariaDB/server/commit/ad4239c)\
  2016-05-01 18:52:13 +0300
  * Fixed assert if user table was mailformed. Added mysql\_to\_mariadb.sql script, to change mysql.user tables from MySQL 5.7 to MariaDB. After this script is run, one can get the other tables fixed by running mysql\_upgrade
* [Revision #037b78e](https://github.com/MariaDB/server/commit/037b78e)\
  2016-04-29 12:32:35 +0300
  * [MDEV-9242](https://jira.mariadb.org/browse/MDEV-9242): Innodb reports Assertion failure in file buf0dblwr.cc line 579
* [Revision #d5822a3](https://github.com/MariaDB/server/commit/d5822a3)\
  2016-04-28 16:27:42 +0300
  * Fixed some galera tests
* [Revision #d62b758](https://github.com/MariaDB/server/commit/d62b758)\
  2016-04-28 14:14:09 +0300
  * Moved mysqld\_server\_initialized to before galera is initialized.
* [Revision #ea83c1d](https://github.com/MariaDB/server/commit/ea83c1d)\
  2016-04-28 15:21:10 +0300
  * [MDEV-9977](https://jira.mariadb.org/browse/MDEV-9977): Crash when accessing large (>4G) InnoDB table on [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md).x 32-bit binaries.
* [Revision #732adec](https://github.com/MariaDB/server/commit/732adec)\
  2016-04-28 13:39:05 +0300
  * Removed some not needed when doing delete thd, which caused warnings about wrong mutex usage from safe\_mutex. Ensure that LOCK\_status is always taken before LOCK\_thread\_count
* [Revision #b4ff645](https://github.com/MariaDB/server/commit/b4ff645)\
  2016-04-28 11:10:55 +0300
  * Fixed wrong counting of global Memory\_used
* [Revision #7c6cb41](https://github.com/MariaDB/server/commit/7c6cb41)\
  2016-04-27 16:38:24 +0300
  * Ignore files in tmp (like mysqld.S)
* [Revision #48f02af](https://github.com/MariaDB/server/commit/48f02af)\
  2016-04-27 16:37:01 +0300
  * [MDEV-9602](https://jira.mariadb.org/browse/MDEV-9602) crash in st\_key::actual\_rec\_per\_key when group by constant
* [Revision #646c4ce](https://github.com/MariaDB/server/commit/646c4ce)\
  2016-04-27 16:13:14 +0200
  * [MDEV-9973](https://jira.mariadb.org/browse/MDEV-9973) : Do not set permissions for serviceaccount user (Win7 and later) This appears to break some installation, and it did not do anything useful anyway.
* [Revision #071ae30](https://github.com/MariaDB/server/commit/071ae30)\
  2016-04-27 11:07:43 +0300
  * [MDEV-9121](https://jira.mariadb.org/browse/MDEV-9121): innodb\_force\_recovery = 6 cannot recover ANY DATA when change buffer not empty
* [Revision #47e0717](https://github.com/MariaDB/server/commit/47e0717)\
  2016-04-27 11:08:46 +0400
  * [MDEV-9792](https://jira.mariadb.org/browse/MDEV-9792) Backport [MDEV-8713](https://jira.mariadb.org/browse/MDEV-8713) to 10.1.
* [Revision #1cf852d](https://github.com/MariaDB/server/commit/1cf852d)\
  2016-04-07 14:44:29 +0200
  * [MDEV-9383](https://jira.mariadb.org/browse/MDEV-9383): Server fails to read master.info after upgrade 10.0 -> 10.1
* [Revision #3f61251](https://github.com/MariaDB/server/commit/3f61251)\
  2016-04-07 20:38:21 +0300
  * Fixed results
* [Revision #293cb04](https://github.com/MariaDB/server/commit/293cb04)\
  2016-04-07 19:26:25 +0300
  * [MDEV-9621](https://jira.mariadb.org/browse/MDEV-9621) INSERT DELAYED fails on insert for tables with many columns This fix also fixes a connection hang when trying to do INSERT DELAYED to a crashed table.
* [Revision #4b6a351](https://github.com/MariaDB/server/commit/4b6a351)\
  2016-04-06 14:15:44 +0200
  * Use \_ReadWriteBarrier() rather than MemoryBarrier() for preventing compile optimization
* [Revision #fd7a8d1](https://github.com/MariaDB/server/commit/fd7a8d1)\
  2016-04-06 13:38:22 +0200
  * Fix compile error in UT\_COMPILER\_BARRIER on Visual Studio compiler.
* [Revision #9794cf2](https://github.com/MariaDB/server/commit/9794cf2) 2016-04-06 08:50:59 +0300 - Merge pull request #168 from grooverdan/10.1-[MDEV-8684](https://jira.mariadb.org/browse/MDEV-8684)-UT\_RELAX\_CPU\_isnt\_relaxing
* [Revision #26c38de](https://github.com/MariaDB/server/commit/26c38de)\
  2016-04-01 09:03:57 +1100
  * [MDEV-8684](https://jira.mariadb.org/browse/MDEV-8684): Use POWER wrappers rather than direct asm
* [Revision #64824a7](https://github.com/MariaDB/server/commit/64824a7)\
  2016-03-30 15:09:52 +1100
  * [MDEV-8684](https://jira.mariadb.org/browse/MDEV-8684): UT\_RELAX\_CPU on Power to non-empty expansion
* [Revision #3d1a7cb](https://github.com/MariaDB/server/commit/3d1a7cb)\
  2016-03-30 14:42:12 +1100
  * [MDEV-8684](https://jira.mariadb.org/browse/MDEV-8684): Remove delaying maths in ut\_delay
* [Revision #d4ba504](https://github.com/MariaDB/server/commit/d4ba504)\
  2016-03-30 14:32:20 +1100
  * Some POWER specific optimizations
* [Revision #2275640](https://github.com/MariaDB/server/commit/2275640)\
  2016-03-30 14:23:37 +1100
  * Bug#20045167 UT\_DELAY MISSING COMPILER BARRIER
* [Revision #0473733](https://github.com/MariaDB/server/commit/0473733)\
  2016-04-03 20:19:59 +0300
  * [MDEV-9860](https://jira.mariadb.org/browse/MDEV-9860): TokuDB ORDER BY DESC query is slower in 10.1 with ICP ON
* [Revision #c395aad](https://github.com/MariaDB/server/commit/c395aad)\
  2016-03-31 13:12:48 +0300
  * [MDEV-9840](https://jira.mariadb.org/browse/MDEV-9840): Test encryption.innodb-log-encrypt-crash fails on buildbot
* [Revision #37a65e3](https://github.com/MariaDB/server/commit/37a65e3)\
  2016-03-30 16:08:05 +0300
  * [MDEV-9793](https://jira.mariadb.org/browse/MDEV-9793): getting mysqld crypto key from key version failed
* [Revision #4ddb9de](https://github.com/MariaDB/server/commit/4ddb9de)\
  2016-03-30 14:59:25 +0300
  * [MDEV-9678](https://jira.mariadb.org/browse/MDEV-9678): Data Directory bug [MDEV-9833](https://jira.mariadb.org/browse/MDEV-9833): Log files are opened using O\_DIRECT causing problems if block size != 512

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
