# MariaDB 10.0.22 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.22)[Release Notes](../../old-releases/10.0/10.0.22.md)[Changelog](mariadb-10022-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 29 Oct 2015

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.22.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #d775ecd](https://github.com/MariaDB/server/commit/d775ecd)\
  2015-10-28 08:11:54 +0100
  * [MDEV-8543](https://jira.mariadb.org/browse/MDEV-8543) mysql.server script not correctly handle --pid-file.
* [Revision #d88aaaa](https://github.com/MariaDB/server/commit/d88aaaa)\
  2015-10-28 08:34:08 +0100
  * [MDEV-8525](https://jira.mariadb.org/browse/MDEV-8525) [mariadb 10.0.20](../../old-releases/10.0/10.0.20.md) crashing when data is read by Kodi media center ([kodi.tv](https://kodi.tv)).
* [Revision #b0e3f48](https://github.com/MariaDB/server/commit/b0e3f48)\
  2015-10-22 16:08:45 +0200
  * [MDEV-8756](https://jira.mariadb.org/browse/MDEV-8756) [MariaDB 10.0.21](../../old-releases/10.0/10.0.21.md) crashes during PREPARE
* [Revision #ac67f9a](https://github.com/MariaDB/server/commit/ac67f9a)\
  2015-10-28 12:53:23 +0400
  * Removed mistakenly committed test file.
* [Revision #ce1b450](https://github.com/MariaDB/server/commit/ce1b450)\
  2015-10-22 13:57:44 +0200
  * [MDEV-7930](https://jira.mariadb.org/browse/MDEV-7930) Assertion \`table\_share->tmp\_table != NO\_TMP\_TABLE || m\_lock\_type != 2' failed in handler::ha\_index\_read\_map
* [Revision #e1ed331](https://github.com/MariaDB/server/commit/e1ed331)\
  2014-07-01 16:52:35 +0530
  * [MDEV-8805](https://jira.mariadb.org/browse/MDEV-8805) - Assertion \`!m\_ordered\_rec\_buffer' failed in ha\_partition::init\_record\_priority\_queue()
* [Revision #4834d82](https://github.com/MariaDB/server/commit/4834d82)\
  2015-10-28 08:42:51 +0200
  * [MDEV-8932](https://jira.mariadb.org/browse/MDEV-8932): innodb buffer pool hit rate is less than zero
* [Revision #a9b5a8d](https://github.com/MariaDB/server/commit/a9b5a8d)\
  2015-10-28 00:08:18 +0100
  * Merge branch 'bb-10.0-serg' into 10.0
* [Revision #3c5733c](https://github.com/MariaDB/server/commit/3c5733c)\
  2015-10-27 18:57:28 +0100
  * Merge branch 'connect/10.0' into 10.0
* [Revision #13884cf](https://github.com/MariaDB/server/commit/13884cf)\
  2015-10-27 13:00:15 +0200
  * [MDEV-8696](https://jira.mariadb.org/browse/MDEV-8696): Adding indexes on empty table is slow with large innodb\_sort\_buffer\_size.
* [Revision #d6480f4](https://github.com/MariaDB/server/commit/d6480f4)\
  2015-10-11 10:32:44 +0200
  * Fixed Fedora 22 package build failure.
* [Revision #e4f9d20](https://github.com/MariaDB/server/commit/e4f9d20)\
  2015-10-23 15:06:43 +0400
  * [MDEV-8498](https://jira.mariadb.org/browse/MDEV-8498) - mysql\_secure\_installation can't find "mysql" in basedir
* [Revision #c918522](https://github.com/MariaDB/server/commit/c918522)\
  2015-10-25 22:45:48 +0400
  * [MDEV-8358](https://jira.mariadb.org/browse/MDEV-8358) ALTER TABLE .. ADD PRIMARY KEY IF NOT EXISTS -> ERROR 1068 (42000): Multiple primary key defined Checks for multiple primary keys added.
* [Revision #6a28882](https://github.com/MariaDB/server/commit/6a28882)\
  2015-10-24 20:06:59 +0200
  * merge commit 02b00b154
* [Revision #84da154](https://github.com/MariaDB/server/commit/84da154)\
  2015-10-23 22:21:50 +0200
  * [MDEV-8883](https://jira.mariadb.org/browse/MDEV-8883) more cross-compiling fixes
* [Revision #fb87133](https://github.com/MariaDB/server/commit/fb87133)\
  2015-10-23 11:31:18 +0200
  * remove unneded #include's that had a dubious explanation
* [Revision #2c0bcff](https://github.com/MariaDB/server/commit/2c0bcff)\
  2015-10-24 20:16:06 +0400
  * [MDEV-8693](https://jira.mariadb.org/browse/MDEV-8693) Tests connect.bin connect.endian fail on armhf (on Debian build system)
* [Revision #d546d1c](https://github.com/MariaDB/server/commit/d546d1c)\
  2015-10-23 18:49:02 +0300
  * Fixed [MDEV-8408](https://jira.mariadb.org/browse/MDEV-8408) Assertion \`inited==INDEX' failed in int handler::ha\_index\_first(uchar\*)
* [Revision #df8832c](https://github.com/MariaDB/server/commit/df8832c)\
  2015-10-22 15:23:18 +0200
  * [MDEV-8883](https://jira.mariadb.org/browse/MDEV-8883) more cross-compiling fixes
* [Revision #581d852](https://github.com/MariaDB/server/commit/581d852)\
  2015-10-22 13:55:55 +0200
  * [MDEV-8868](https://jira.mariadb.org/browse/MDEV-8868) Consider adding a check for libjemalloc version in cmake and/or at runtime
* [Revision #6f07547](https://github.com/MariaDB/server/commit/6f07547)\
  2015-10-22 13:09:38 +0200
  * [MDEV-8614](https://jira.mariadb.org/browse/MDEV-8614) Assertion \`status == 0' failed in add\_role\_user\_mapping\_action on RENAME USER
* [Revision #956e92d](https://github.com/MariaDB/server/commit/956e92d)\
  2015-10-22 11:58:54 +0200
  * [MDEV-8609](https://jira.mariadb.org/browse/MDEV-8609) Server crashes in is\_invalid\_role\_name on reloading ACL with a blank role name
* [Revision #27328ca](https://github.com/MariaDB/server/commit/27328ca)\
  2015-10-22 10:27:36 +0200
  * add comment to a test
* [Revision #3e1c743](https://github.com/MariaDB/server/commit/3e1c743)\
  2015-10-22 07:23:59 +0200
  * [MDEV-7656](https://jira.mariadb.org/browse/MDEV-7656) init\_file option does not allow changing passwords
* [Revision #e257b8b](https://github.com/MariaDB/server/commit/e257b8b)\
  2015-10-21 16:22:20 +0200
  * fix the dbug tag name
* [Revision #e5cce2b](https://github.com/MariaDB/server/commit/e5cce2b)\
  2015-10-22 07:15:23 +0200
  * fix build on sol10-64
* [Revision #41a3c58](https://github.com/MariaDB/server/commit/41a3c58)\
  2015-10-21 19:40:38 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #b35f997](https://github.com/MariaDB/server/commit/b35f997)\
  2015-10-21 19:24:01 +0200
  * Fix [MDEV-8882](https://jira.mariadb.org/browse/MDEV-8882) modified: storage/connect/tabodbc.cpp
* [Revision #18f7dfe](https://github.com/MariaDB/server/commit/18f7dfe)\
  2015-10-15 12:11:17 +0300
  * Allow mysql\_upgrade to enable event after table is corrected
* [Revision #95faf34](https://github.com/MariaDB/server/commit/95faf34)\
  2015-10-12 13:05:31 +0300
  * Set opt\_noacl (running with--skip-grant-tables) to 0 if we reload grant tables.
* [Revision #0d90b8b](https://github.com/MariaDB/server/commit/0d90b8b)\
  2015-10-21 14:59:36 +0200
  * Merge branch '5.5' into 10.0
* [Revision #df80420](https://github.com/MariaDB/server/commit/df80420)\
  2015-10-21 14:42:56 +0200
  * fix events\_1 test for October 2015
* [Revision #ac9141c](https://github.com/MariaDB/server/commit/ac9141c)\
  2015-10-20 18:45:45 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #d51e466](https://github.com/MariaDB/server/commit/d51e466)\
  2015-10-20 13:20:10 +0200
  * Fix [MDEV-8966](https://jira.mariadb.org/browse/MDEV-8966) modified: storage/connect/ha\_connect.cc
* [Revision #9a3ff07](https://github.com/MariaDB/server/commit/9a3ff07)\
  2015-10-19 12:15:49 +0200
  * [MDEV-8565](https://jira.mariadb.org/browse/MDEV-8565): COLUMN\_CHECK fails on valid data
* [Revision #f515422](https://github.com/MariaDB/server/commit/f515422)\
  2015-10-18 15:06:14 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #9020946](https://github.com/MariaDB/server/commit/9020946)\
  2015-10-18 15:03:45 +0200
  * Fix [MDEV-8926](https://jira.mariadb.org/browse/MDEV-8926) modified: storage/connect/ha\_connect.cc
* [Revision #978c2a3](https://github.com/MariaDB/server/commit/978c2a3)\
  2015-10-11 17:06:03 -0400
  * [MDEV-7640](https://jira.mariadb.org/browse/MDEV-7640): CHANGE MASTER TO doesn't work with prepared statements
* [Revision #151f967](https://github.com/MariaDB/server/commit/151f967)\
  2015-10-11 17:06:03 -0400
  * [MDEV-7640](https://jira.mariadb.org/browse/MDEV-7640): CHANGE MASTER TO doesn't work with prepared statements
* [Revision #e7cb032](https://github.com/MariaDB/server/commit/e7cb032)\
  2015-10-09 19:29:03 +0200
  * fixes for buildbot:
* [Revision #2ca4141](https://github.com/MariaDB/server/commit/2ca4141)\
  2015-10-09 18:24:17 +0200
  * Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #01be663](https://github.com/MariaDB/server/commit/01be663)\
  2015-10-09 18:16:27 +0200
  * Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #77c44a3](https://github.com/MariaDB/server/commit/77c44a3)\
  2015-10-09 17:48:31 +0200
  * update innodb version
* [Revision #04af573](https://github.com/MariaDB/server/commit/04af573)\
  2015-10-09 17:47:30 +0200
  * Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #1b41eed](https://github.com/MariaDB/server/commit/1b41eed)\
  2015-10-09 17:22:53 +0200
  * 5.6.27
* [Revision #86ff4da](https://github.com/MariaDB/server/commit/86ff4da)\
  2015-10-09 17:21:46 +0200
  * 5.6.27
* [Revision #6a821d7](https://github.com/MariaDB/server/commit/6a821d7)\
  2015-10-09 17:20:49 +0200
  * 5.6.26-74.0
* [Revision #cfeedbf](https://github.com/MariaDB/server/commit/cfeedbf)\
  2015-10-09 17:12:26 +0200
  * Merge branch '5.5' into 10.0
* [Revision #16c4b3c](https://github.com/MariaDB/server/commit/16c4b3c)\
  2015-10-09 16:43:59 +0200
  * fixes for buildbot:
* [Revision #bff1af9](https://github.com/MariaDB/server/commit/bff1af9)\
  2015-07-16 15:50:26 -0700
  * Clarify the log message about master\_info and relay\_info files.
* [Revision #0ea4233](https://github.com/MariaDB/server/commit/0ea4233)\
  2015-09-18 18:27:54 +0200
  * remove --default-myisam from mtr
* [Revision #2a9bcc6](https://github.com/MariaDB/server/commit/2a9bcc6)\
  2015-09-17 14:45:28 +0200
  * [MDEV-7680](https://jira.mariadb.org/browse/MDEV-7680): mysqld man page
* [Revision #99142ab](https://github.com/MariaDB/server/commit/99142ab)\
  2015-09-17 14:34:03 +0200
  * mysql and mysqldhow man pages
* [Revision #ed195b2](https://github.com/MariaDB/server/commit/ed195b2)\
  2015-09-10 20:12:50 +0200
  * [MDEV-7680](https://jira.mariadb.org/browse/MDEV-7680): mysqld\_safe and mysql\_multi man pages
* [Revision #5077509](https://github.com/MariaDB/server/commit/5077509)\
  2015-09-09 14:32:52 +0200
  * [MDEV-7680](https://jira.mariadb.org/browse/MDEV-7680): Update man pages
* [Revision #f41a41f](https://github.com/MariaDB/server/commit/f41a41f)\
  2015-10-09 00:06:16 +0200
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #db79f4c](https://github.com/MariaDB/server/commit/db79f4c)\
  2015-10-08 23:02:43 +0200
  * 5.5.45-37.4
* [Revision #82e9f6d](https://github.com/MariaDB/server/commit/82e9f6d)\
  2015-10-08 22:54:24 +0200
  * Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #c8d5112](https://github.com/MariaDB/server/commit/c8d5112)\
  2015-10-08 00:32:07 +0200
  * [MDEV-8796](https://jira.mariadb.org/browse/MDEV-8796) Delete with sub query with information\_schema.TABLES deletes too many rows
* [Revision #6dd4114](https://github.com/MariaDB/server/commit/6dd4114)\
  2015-10-08 10:45:32 +0300
  * Better error messages if slave is not properly configured
* [Revision #a69a6dd](https://github.com/MariaDB/server/commit/a69a6dd)\
  2015-10-08 10:45:09 +0300
  * [MDEV-4487](https://jira.mariadb.org/browse/MDEV-4487) Allow replication from MySQL 5.6+ when GTID is enabled on the master [MDEV-8685](https://jira.mariadb.org/browse/MDEV-8685) MariaDB fails to decode Anonymous\_GTID entries [MDEV-5705](https://jira.mariadb.org/browse/MDEV-5705) Replication testing: 5.6->10.0
* [Revision #7c1e2fe](https://github.com/MariaDB/server/commit/7c1e2fe)\
  2015-10-08 10:17:07 +0300
  * Better error message if failed
* [Revision #ca051fa](https://github.com/MariaDB/server/commit/ca051fa)\
  2015-10-08 10:16:35 +0300
  * Allow row events in replication stream for slave in all cases (even when configured with --binlog-format=statement). Before we got an error on the slave and the slave stopped if the master was configured with --binlog-format=mixed or --binlog-format=row.
* [Revision #d278fb4](https://github.com/MariaDB/server/commit/d278fb4)\
  2015-10-08 09:58:44 +0300
  * Fixed tokudb test result to make it stable (was altering between index and range)
* [Revision #4a60204](https://github.com/MariaDB/server/commit/4a60204)\
  2015-10-06 16:15:34 +0300
  * [MDEV-8903](https://jira.mariadb.org/browse/MDEV-8903): Buildbot valgrind failure: Invalid read of size 1 in sql\_memdup...
* [Revision #1289794](https://github.com/MariaDB/server/commit/1289794)\
  2015-10-06 15:54:37 +0300
  * Fix for [MDEV-8321](https://jira.mariadb.org/browse/MDEV-8321), [MDEV-6223](https://jira.mariadb.org/browse/MDEV-6223)
* [Revision #504802f](https://github.com/MariaDB/server/commit/504802f)\
  2015-08-05 11:57:35 +0200
  * [MDEV-7846](https://jira.mariadb.org/browse/MDEV-7846): postreview fix
* [Revision #54b9981](https://github.com/MariaDB/server/commit/54b9981)\
  2015-04-23 20:08:57 +0200
  * [MDEV-7846](https://jira.mariadb.org/browse/MDEV-7846): Server crashes in Item\_subselect::fix\_fields or fails with Thread stack overrun
* [Revision #0ab93fd](https://github.com/MariaDB/server/commit/0ab93fd)\
  2015-04-23 19:16:57 +0200
  * [MDEV-7445](https://jira.mariadb.org/browse/MDEV-7445):Server crash with Signal 6 [MDEV-7565](https://jira.mariadb.org/browse/MDEV-7565): Server crash with Signal 6 (part 2)
* [Revision #2e3e818](https://github.com/MariaDB/server/commit/2e3e818)\
  2015-04-23 19:11:06 +0200
  * [MDEV-7445](https://jira.mariadb.org/browse/MDEV-7445): Server crash with Signal 6
* [Revision #7ccde2c](https://github.com/MariaDB/server/commit/7ccde2c)\
  2015-04-23 19:04:11 +0200
  * [MDEV-7565](https://jira.mariadb.org/browse/MDEV-7565): Server crash with Signal 6 (part 2)
* [Revision #a7dd24c](https://github.com/MariaDB/server/commit/a7dd24c)\
  2015-10-06 13:52:27 +0300
  * [MDEV-8299](https://jira.mariadb.org/browse/MDEV-8299): MyISAM or Aria table gets corrupted after EXPLAIN INSERT and INSERT
* [Revision #bb22eb5](https://github.com/MariaDB/server/commit/bb22eb5)\
  2015-10-01 13:40:23 +0400
  * [MDEV-8379](https://jira.mariadb.org/browse/MDEV-8379) - SUSE mariadb patches
* [Revision #727da9c](https://github.com/MariaDB/server/commit/727da9c)\
  2015-10-01 13:04:59 +0400
  * [MDEV-8379](https://jira.mariadb.org/browse/MDEV-8379) - SUSE mariadb patches
* [Revision #006acf7](https://github.com/MariaDB/server/commit/006acf7)\
  2015-09-30 10:49:45 +0300
  * Bug #68148: drop index on a foreign key column leads to missing table [MDEV-8845](https://jira.mariadb.org/browse/MDEV-8845): Table disappear after modifying FK
* [Revision #a95711e](https://github.com/MariaDB/server/commit/a95711e)\
  2015-09-29 08:39:54 +0300
  * [MDEV-8855](https://jira.mariadb.org/browse/MDEV-8855): innodb.innodb-fk-warnings fails on Windows
* [Revision #02a38fd](https://github.com/MariaDB/server/commit/02a38fd)\
  2015-09-24 17:25:52 +0200
  * [MDEV-8624](https://jira.mariadb.org/browse/MDEV-8624): MariaDB hangs on query with many logical condition
* [Revision #f804b74](https://github.com/MariaDB/server/commit/f804b74)\
  2015-09-28 03:40:29 +0300
  * [MDEV-8154](https://jira.mariadb.org/browse/MDEV-8154) rpl.show\_status\_stop\_slave\_race-7126 sporadically causes internal check failure
* [Revision #ce7d8c5](https://github.com/MariaDB/server/commit/ce7d8c5)\
  2015-09-27 18:01:47 +0300
  * [MDEV-7330](https://jira.mariadb.org/browse/MDEV-7330) plugins.feedback\_plugin\_send fails sporadically in buildbot
* [Revision #bdcf370](https://github.com/MariaDB/server/commit/bdcf370)\
  2015-09-27 16:00:48 +0300
  * [MDEV-7933](https://jira.mariadb.org/browse/MDEV-7933) plugins.feedback\_plugin\_send depends on being executed after plugins.feedback\_plugin\_load
* [Revision #2563609](https://github.com/MariaDB/server/commit/2563609)\
  2015-09-26 02:51:29 +0300
  * Increased the version number
* [Revision #86ed494](https://github.com/MariaDB/server/commit/86ed494)\
  2015-09-26 02:48:55 +0300
  * [MDEV-8849](https://jira.mariadb.org/browse/MDEV-8849) rpl.rpl\_innodb\_bug30888 sporadically fails in buildbot with testcase timeout
* [Revision #dca4ab9](https://github.com/MariaDB/server/commit/dca4ab9)\
  2015-09-24 21:24:28 +0300
  * [MDEV-8841](https://jira.mariadb.org/browse/MDEV-8841) innodb\_zip.innodb-create-options fails in buildbot
* [Revision #5cc149f](https://github.com/MariaDB/server/commit/5cc149f)\
  2015-09-24 10:28:47 +0200
  * The compiler warnings fixed.
* [Revision #fea1568](https://github.com/MariaDB/server/commit/fea1568)\
  2015-09-22 13:35:23 +0200
  * Fix sporadic test failure in rpl\_gtid\_mdev4820.test
* [Revision #81727cd](https://github.com/MariaDB/server/commit/81727cd)\
  2015-09-22 12:54:01 +0300
  * Backport to 10.0: [MDEV-8779](https://jira.mariadb.org/browse/MDEV-8779): mysqld got signal 11 in sql/opt\_range\_mrr.cc:100(step\_down\_to)
* [Revision #8d0d445](https://github.com/MariaDB/server/commit/8d0d445)\
  2015-09-21 17:32:37 +0300
  * Backport to 10.0: [MDEV-8779](https://jira.mariadb.org/browse/MDEV-8779): mysqld got signal 11 in sql/opt\_range\_mrr.cc:100(step\_down\_to)
* [Revision #80d1237](https://github.com/MariaDB/server/commit/80d1237)\
  2015-09-16 12:14:59 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #019c9e0](https://github.com/MariaDB/server/commit/019c9e0)\
  2015-09-16 12:11:28 +0200
  * Fix assert error for where clause with UDF's was fixed in HA\_CONNECT::CondFilter moving res= pval->val\_str(\&tmp) but this was wrong. Now res is only used for strings. modified: storage/connect/ha\_connect.cc
* [Revision #abd31ca](https://github.com/MariaDB/server/commit/abd31ca)\
  2015-05-06 13:19:22 +0200
  * [MDEV-7990](https://jira.mariadb.org/browse/MDEV-7990): ERROR 1526 when procedure executed for second time ALTER TABLE partition ... pMAX values less than MAXVALUE
* [Revision #39e8dc9](https://github.com/MariaDB/server/commit/39e8dc9)\
  2015-09-12 00:43:31 +0200
  * Merge.
* [Revision #528729f](https://github.com/MariaDB/server/commit/528729f)\
  2015-09-12 00:42:21 +0200
  * [MDEV-8193](https://jira.mariadb.org/browse/MDEV-8193): UNTIL clause in START SLAVE is sporadically disobeyed by parallel replication
* [Revision #244f043](https://github.com/MariaDB/server/commit/244f043)\
  2015-09-11 12:03:04 +0200
  * Merge [MDEV-8193](https://jira.mariadb.org/browse/MDEV-8193) into 10.0
* [Revision #51eaa7f](https://github.com/MariaDB/server/commit/51eaa7f)\
  2015-09-11 10:51:56 +0200
  * [MDEV-8193](https://jira.mariadb.org/browse/MDEV-8193): UNTIL clause in START SLAVE is sporadically disobeyed by parallel replication
* [Revision #d69931e](https://github.com/MariaDB/server/commit/d69931e)\
  2015-09-09 01:28:04 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #e939ea5](https://github.com/MariaDB/server/commit/e939ea5)\
  2015-09-09 01:26:00 +0200
  * Fix assert error for where clause with UDF's was fixed in HA\_CONNECT::CondFilter moving pval->val\_str(\&tmp) modified: storage/connect/ha\_connect.cc
* [Revision #29ac245](https://github.com/MariaDB/server/commit/29ac245)\
  2015-09-07 13:13:52 +0200
  * [MDEV-8473](https://jira.mariadb.org/browse/MDEV-8473): mysqlbinlog -v does not properly decode DECIMAL values in an RBR log
* [Revision #0ce0b88](https://github.com/MariaDB/server/commit/0ce0b88)\
  2015-09-01 11:47:06 +0200
  * [MDEV-8450](https://jira.mariadb.org/browse/MDEV-8450): PATCH] Wrong macro expansion in Query\_cache::send\_result\_to\_client()
* [Revision #102a85f](https://github.com/MariaDB/server/commit/102a85f)\
  2015-09-03 18:00:43 +0200
  * [MDEV-8663](https://jira.mariadb.org/browse/MDEV-8663): IF Statement returns multiple values erroneously (or Assertion \`!null\_value' failed in Item::send(Protocol\*, String\*))
* [Revision #9abf426](https://github.com/MariaDB/server/commit/9abf426)\
  2015-09-04 13:35:31 +0300
  * [MDEV-8443](https://jira.mariadb.org/browse/MDEV-8443): mysql-test - innodb.innodb\_simulate\_comp\_failures 'innodb\_plugin' is failing
* [Revision #bd8ffe7](https://github.com/MariaDB/server/commit/bd8ffe7)\
  2015-09-03 09:39:57 +0200
  * Merge pull request #87 from pivanof/qplan\_macros
* [Revision #83c7b1e](https://github.com/MariaDB/server/commit/83c7b1e)\
  2015-09-02 10:40:34 +0200
  * Merge [MDEV-8725](https://jira.mariadb.org/browse/MDEV-8725) into 10.0
* [Revision #09bfaf3](https://github.com/MariaDB/server/commit/09bfaf3)\
  2015-09-02 10:08:09 +0200
  * Fix a potential lost wakeup for binlog\_commit\_wait\_usec
* [Revision #999c43a](https://github.com/MariaDB/server/commit/999c43a)\
  2015-09-02 09:57:18 +0200
  * [MDEV-8725](https://jira.mariadb.org/browse/MDEV-8725): Assertion \`!(thd->rgi\_slave && thd-> rgi\_slave->did\_mark\_start\_commit)' failed in ha\_rollback\_trans
* [Revision #4b41e3c](https://github.com/MariaDB/server/commit/4b41e3c)\
  2015-08-31 18:40:24 +0200
  * [MDEV-6219](https://jira.mariadb.org/browse/MDEV-6219): Server crashes in Bitmap<64u>::merge (this=0x180, map2=...) on 2nd execution of PS with INSERT .. SELECT, derived\_merge
* [Revision #b66455f6](https://github.com/MariaDB/server/commit/b66455f6)\
  2015-08-24 01:41:12 +0300
  * Increase the version number
* [Revision #aef8bfd](https://github.com/MariaDB/server/commit/aef8bfd)\
  2015-08-24 01:37:21 +0300
  * [MDEV-8670](https://jira.mariadb.org/browse/MDEV-8670) main.[MDEV-504](https://jira.mariadb.org/browse/MDEV-504) fails on Windows (in buildbot and outside)
* [Revision #9b475ee](https://github.com/MariaDB/server/commit/9b475ee)\
  2015-08-05 20:43:25 +0300
  * [MDEV-8289](https://jira.mariadb.org/browse/MDEV-8289): Semijoin inflates number of rows in query result - Make semi-join optimizer not to choose LooseScan when 1) the index is not covered and 2) full index scan will be required.
* [Revision #cd9b919](https://github.com/MariaDB/server/commit/cd9b919)\
  2015-08-14 15:49:46 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #6d46c97](https://github.com/MariaDB/server/commit/6d46c97)\
  2015-08-14 14:23:14 +0200
  * Fix crash when SetValue\_char is called with a negative length value. This can happen in odbconn.cpp when SQLFetch returns SQL\_NO\_TOTAL (-4) as length. modified: storage/connect/odbconn.cpp modified: storage/connect/value.cpp
* [Revision #1bfe4da](https://github.com/MariaDB/server/commit/1bfe4da)\
  2015-08-13 01:28:15 +0300
  * Fixed mysqltest run failure: Test did not clean up after itself properly
* [Revision #afa9cb7](https://github.com/MariaDB/server/commit/afa9cb7)\
  2015-08-13 01:27:23 +0300
  * Fixed overrun in key cache if one tried to allocate a key cache of more than 45G with a key\_cache\_block\_size of 1024 or less.
* [Revision #335ec7a](https://github.com/MariaDB/server/commit/335ec7a)\
  2015-08-11 21:15:33 +0200
  * Prevent wrong update of expanded columns when pretty is not 2. modified: storage/connect/tabjson.cpp
* [Revision #0eacebf](https://github.com/MariaDB/server/commit/0eacebf)\
  2015-08-08 10:54:47 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #5f53303](https://github.com/MariaDB/server/commit/5f53303)\
  2015-08-06 17:46:47 +0200
  * Fix the TDBDOS::EstimatedLength function that was wrongly counting its calculation virtual and special columns. modified: storage/connect/reldef.h modified: storage/connect/tabdos.cpp
* [Revision #203f4d4](https://github.com/MariaDB/server/commit/203f4d4)\
  2015-07-16 15:59:55 -0700
  * Add parenthesis in macro definitions to prevent order of operation problems.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
