# MariaDB Galera Cluster 10.0.22 Changelog

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.22)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10-0-22-release-notes.md)[Changelog](mariadb-galera-cluster-10022-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 19 Nov 2015

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10-0-22-release-notes.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #f4421c8](https://github.com/MariaDB/server/commit/f4421c8)\
  2015-11-16 12:39:56 -0500
  * Fix for some failing tests.
* [Revision #c78fc8b](https://github.com/MariaDB/server/commit/c78fc8b)\
  2015-11-16 12:35:06 -0500
  * MTR: rsync process is left running if pid file is removed
* [Revision #dcb7996](https://github.com/MariaDB/server/commit/dcb7996)\
  2015-11-15 17:24:47 -0500
  * Fix/disable failing tests.
* [Revision #e947a52](https://github.com/MariaDB/server/commit/e947a52)\
  2015-11-04 21:58:07 -0500
  * Update global\_suppressions.
* [Revision #2399f1a](https://github.com/MariaDB/server/commit/2399f1a)\
  2015-11-04 21:56:46 -0500
  * Fix for build failure.
* [Revision #4d15112](https://github.com/MariaDB/server/commit/4d15112)\
  2015-10-31 18:07:02 -0400
  * Merge tag 'mariadb-10.0.22' into 10.0-galera
* [Revision #d775ecd](https://github.com/MariaDB/server/commit/d775ecd)\
  2015-10-28 08:11:54 +0100
  * [MDEV-8543](https://jira.mariadb.org/browse/MDEV-8543) mysql.server script not correctly handle --pid-file.
* [Revision #d88aaaa](https://github.com/MariaDB/server/commit/d88aaaa)\
  2015-10-28 08:34:08 +0100
  * [MDEV-8525](https://jira.mariadb.org/browse/MDEV-8525) [mariadb 10.0.20](../../10.0/10.0.20.md) crashing when data is read by Kodi media center ([kodi.tv](https://kodi.tv)).
* [Revision #b0e3f48](https://github.com/MariaDB/server/commit/b0e3f48)\
  2015-10-22 16:08:45 +0200
  * [MDEV-8756](https://jira.mariadb.org/browse/MDEV-8756) [MariaDB 10.0.21](../../10.0/10.0.21.md) crashes during PREPARE
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
* [Revision #17b0b45](https://github.com/MariaDB/server/commit/17b0b45)\
  2015-10-21 09:20:54 +0300
  * Code cleanup.
* [Revision #ac9141c](https://github.com/MariaDB/server/commit/ac9141c)\
  2015-10-20 18:45:45 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #d51e466](https://github.com/MariaDB/server/commit/d51e466)\
  2015-10-20 13:20:10 +0200
  * Fix [MDEV-8966](https://jira.mariadb.org/browse/MDEV-8966) modified: storage/connect/ha\_connect.cc
* [Revision #f3e3624](https://github.com/MariaDB/server/commit/f3e3624)\
  2015-10-20 13:41:14 +0300
  * [MDEV-8869](https://jira.mariadb.org/browse/MDEV-8869): Potential lock\_sys->mutex deadlock
* [Revision #76701c6](https://github.com/MariaDB/server/commit/76701c6)\
  2015-10-19 14:17:36 +0300
  * Merge pull request #105 from philip-galera/10.0-galera-mysql-wsrep-gh202
* [Revision #52a9103](https://github.com/MariaDB/server/commit/52a9103)\
  2015-10-19 04:14:51 -0700
  * refs codership/mysql-wsrep#202 Fix bad cherry-pick (and the compiler warnings it generated)
* [Revision #9a3ff07](https://github.com/MariaDB/server/commit/9a3ff07)\
  2015-10-19 12:15:49 +0200
  * [MDEV-8565](https://jira.mariadb.org/browse/MDEV-8565): COLUMN\_CHECK fails on valid data
* [Revision #3ec139a](https://github.com/MariaDB/server/commit/3ec139a)\
  2015-10-19 12:05:25 +0300
  * Merge pull request #104 from philip-galera/10.0-galera-mysql-wsrep-gh202
* [Revision #43b2a45](https://github.com/MariaDB/server/commit/43b2a45)\
  2015-10-19 01:56:04 -0700
  * refs codership/mysql-wsrep#202 Added schema info into wsrep messages
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
* [Revision #4d33f9d](https://github.com/MariaDB/server/commit/4d33f9d)\
  2015-09-25 14:57:56 -0400
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #13615c5](https://github.com/MariaDB/server/commit/13615c5)\
  2015-09-25 13:56:02 -0400
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): Sporadic SEGFAULT on startup
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
* [Revision #d54bc3c](https://github.com/MariaDB/server/commit/d54bc3c)\
  2015-09-21 20:49:31 -0400
  * Cleanup: remove dead code which could also lead to race.
* [Revision #9d5767c](https://github.com/MariaDB/server/commit/9d5767c)\
  2015-09-21 20:47:05 -0400
  * Post-merge fix.
* [Revision #8d0d445](https://github.com/MariaDB/server/commit/8d0d445)\
  2015-09-21 17:32:37 +0300
  * Backport to 10.0: [MDEV-8779](https://jira.mariadb.org/browse/MDEV-8779): mysqld got signal 11 in sql/opt\_range\_mrr.cc:100(step\_down\_to)
* [Revision #db2e21b](https://github.com/MariaDB/server/commit/db2e21b)\
  2015-09-16 23:20:57 -0400
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): Sporadic SEGFAULT on startup
* [Revision #80d1237](https://github.com/MariaDB/server/commit/80d1237)\
  2015-09-16 12:14:59 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #019c9e0](https://github.com/MariaDB/server/commit/019c9e0)\
  2015-09-16 12:11:28 +0200
  * Fix assert error for where clause with UDF's was fixed in HA\_CONNECT::CondFilter moving res= pval->val\_str(\&tmp) but this was wrong. Now res is only used for strings. modified: storage/connect/ha\_connect.cc
* [Revision #fd1b2e4](https://github.com/MariaDB/server/commit/fd1b2e4)\
  2015-09-15 17:07:41 -0400
  * [MDEV-8803](https://jira.mariadb.org/browse/MDEV-8803): Debian jessie 8.2 + [MariaDB 10.1.7](../../10.1/10.1.7.md) + GaleraCluster
* [Revision #653aadc](https://github.com/MariaDB/server/commit/653aadc)\
  2015-09-15 16:27:04 -0400
  * [MDEV-8804](https://jira.mariadb.org/browse/MDEV-8804): bootstrap command missing in debian init script
* [Revision #eac8e43](https://github.com/MariaDB/server/commit/eac8e43)\
  2015-09-14 15:43:16 -0400
  * Avoid caching wsrep threads (fixed the erroneous condition).
* [Revision #a401c11](https://github.com/MariaDB/server/commit/a401c11)\
  2015-09-14 15:26:50 -0400
  * Fix failing test cases
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
* [Revision #ceac344](https://github.com/MariaDB/server/commit/ceac344)\
  2015-09-10 09:57:08 -0400
  * [Bug #1372840](https://bugs.launchpad.net/bugs/1372840) - test case
* [Revision #f479b5a](https://github.com/MariaDB/server/commit/f479b5a)\
  2015-09-10 00:29:06 -0400
  * Update WSREP\_PATCH\_REVNO
* [Revision #f951071](https://github.com/MariaDB/server/commit/f951071)\
  2015-09-08 22:11:56 -0700
  * Galera MTR Tests: fix typo in the galera\_as\_slave\_nonprim test, in suite/galera/galera\_3nodes\_as\_slave.cnf
* [Revision #b3ec0a8](https://github.com/MariaDB/server/commit/b3ec0a8)\
  2015-09-08 05:04:47 -0700
  * Galera MTR Tests: a test for async slave + non-prim
* [Revision #db66d2f](https://github.com/MariaDB/server/commit/db66d2f)\
  2015-09-10 00:20:49 -0400
  * refs codership/mysql-wsrep#188
* [Revision #2012a81](https://github.com/MariaDB/server/commit/2012a81)\
  2015-09-10 00:14:24 -0400
  * refs codership/mysql-wsrep#181
* [Revision #c915d8c](https://github.com/MariaDB/server/commit/c915d8c)\
  2015-09-01 00:57:20 -0700
  * Galera MTR Tests: attempt to work around codership/mysql-wsrep#179
* [Revision #25bbfe8](https://github.com/MariaDB/server/commit/25bbfe8)\
  2015-08-31 02:16:43 -0700
  * Galera MTR Tests: Instruct xtrabackup SST's socat to use 1024-bit DH keys to avoid 'error:14082174:SSL routines:SSL3\_CHECK\_CERT\_AND\_ALGORITHM:dh key too small'
* [Revision #b6f8033](https://github.com/MariaDB/server/commit/b6f8033)\
  2015-08-31 02:15:37 -0700
  * Galera MTR Tests: Tests around do-\* and ignore-\* binlog options
* [Revision #f7885fb](https://github.com/MariaDB/server/commit/f7885fb)\
  2015-08-27 00:54:26 -0700
  * Correct WSREP\_PATCH\_VERSION for 5.6 is 11
* [Revision #52c9235](https://github.com/MariaDB/server/commit/52c9235)\
  2015-08-25 06:15:20 -0700
  * Galera MTR Tests: Add known Galera and mysql-wsrep Valgrind issues to valgrind.supp
* [Revision #371dc33](https://github.com/MariaDB/server/commit/371dc33)\
  2015-08-24 06:56:30 -0700
  * refs codership/mysql-wsrep#90 MTR test case for mysql-wsrep#90
* [Revision #e5b595e](https://github.com/MariaDB/server/commit/e5b595e)\
  2015-08-14 05:14:53 -0700
  * Galera MTR Tests: fix typo in suite/galera/galera\_2nodes\_as\_slave.cnf
* [Revision #ee22ac3](https://github.com/MariaDB/server/commit/ee22ac3)\
  2015-08-14 01:16:25 -0700
  * Galera MTR Tests: Various test stability fixes (take #5)
* [Revision #7d73931](https://github.com/MariaDB/server/commit/7d73931)\
  2015-08-12 06:40:59 -0700
  * Galera MTR Tests: Various test stability fixes (take #4)
* [Revision #ff76214](https://github.com/MariaDB/server/commit/ff76214)\
  2015-08-12 05:32:18 -0700
  * Galera MTR Tests: Various test stability fixes (take #3)
* [Revision #fd0aaad](https://github.com/MariaDB/server/commit/fd0aaad)\
  2015-08-12 01:03:21 -0700
  * Galera MTR Tests: Various test stability fixes (take #2)
* [Revision #997119d](https://github.com/MariaDB/server/commit/997119d)\
  2015-08-11 04:22:38 -0700
  * Galera MTR Tests: Various test stability fixes.
* [Revision #182b237](https://github.com/MariaDB/server/commit/182b237)\
  2015-08-07 21:15:02 -0700
  * Galera MTR Tests: remove variable output from galera\_gra\_log.test (take #2)
* [Revision #c9d4581](https://github.com/MariaDB/server/commit/c9d4581)\
  2015-08-06 20:55:30 -0700
  * Galera MTR Tests: remove variable output from galera\_gra\_log.test
* [Revision #2316a4e](https://github.com/MariaDB/server/commit/2316a4e)\
  2015-08-06 00:34:00 -0700
  * Galera MTR Tests: Tests for GRA\*.log files, replication bundle, preordered events, forced binlog format
* [Revision #a1a7414](https://github.com/MariaDB/server/commit/a1a7414)\
  2015-08-03 03:20:52 -0700
  * Galera MTR Tests: An end-to-end test with restoring a node from xtrabackup; a test for restoring the primary component via pc.bootstrap
* [Revision #1e29068](https://github.com/MariaDB/server/commit/1e29068)\
  2015-07-23 04:30:07 -0700
  * Galera MTR Tests: Valgrind suppression for codership/galera#306
* [Revision #3893b5c](https://github.com/MariaDB/server/commit/3893b5c)\
  2015-07-23 04:29:40 -0700
  * Galera MTR Tests: mark all tests operating on large data sets with --source include/big-test.inc to help with Valgrind
* [Revision #83579c2](https://github.com/MariaDB/server/commit/83579c2)\
  2015-07-10 07:17:20 -0700
  * Galera MTR Tests: fixes for mysqldump SST/IST tests
* [Revision #10f5c08](https://github.com/MariaDB/server/commit/10f5c08)\
  2015-07-08 01:52:45 -0700
  * Refs codership/QA#47. Additional tests for FTWRL.
* [Revision #6104a27](https://github.com/MariaDB/server/commit/6104a27)\
  2015-07-07 06:01:00 -0700
  * Galera MTR Tests: increase lock wait timeout in suite/galera/t/galera\_many\_rows.test
* [Revision #4a630ce](https://github.com/MariaDB/server/commit/4a630ce)\
  2015-07-07 06:00:22 -0700
  * Galera MTR Tests: A test for xtrabackup with key+cert encryption.
* [Revision #edd9bd3](https://github.com/MariaDB/server/commit/edd9bd3)\
  2015-07-07 03:42:03 -0700
  * Fixes codership/mysql-wsrep#153 use --defaults-extra-file with mysqldump SST
* [Revision #5d531f0](https://github.com/MariaDB/server/commit/5d531f0)\
  2015-07-01 03:13:04 -0700
  * Galera MTR Tests: Use SET GLOBAL when setting wsrep\_replicate\_myisam, as it is a GLOBAL variable in MySQL Galera Cluster and SESSION in Percona XTraDB Cluster
* [Revision #fbe739c](https://github.com/MariaDB/server/commit/fbe739c)\
  2015-06-29 16:42:58 +0530
  * Bug#1421360: Add 'FLUSH TABLES' to Total Order Isolation execution.
* [Revision #5a002ad](https://github.com/MariaDB/server/commit/5a002ad)\
  2015-06-26 01:30:01 -0700
  * Galera MTR Tests: various tests and test fixes
* [Revision #f1a00ed](https://github.com/MariaDB/server/commit/f1a00ed)\
  2015-06-17 05:14:36 -0700
  * Galera MTR Tests: Use wsrep\_sst\_auth for tests that use xtrabackup + IST
* [Revision #2ea16b9](https://github.com/MariaDB/server/commit/2ea16b9)\
  2015-06-08 21:06:22 +0300
  * This commit fixes - errno handling in wsp::env::append() method, where error could be returned by mistake - return code of sst\_prepare\_other() when pthread\_create() fails - it was returning positive error code which by convention is treated as success.
* [Revision #0ccbbff](https://github.com/MariaDB/server/commit/0ccbbff)\
  2015-06-08 12:23:53 +0300
  * Slight cleanup improvement on a previous commit.
* [Revision #bc796c2](https://github.com/MariaDB/server/commit/bc796c2)\
  2015-06-08 01:43:27 -0700
  * Refs codership/mysql-wsrep#143 . Account for the case where the SST password is empty
* [Revision #86ee30c](https://github.com/MariaDB/server/commit/86ee30c)\
  2015-06-06 01:08:41 +0300
  * Refs codership/mysql-wsrep#141: this commit 1. Passes wsrep\_sst\_auth\_value to SST scripts via WSREP\_SST\_OPT\_AUTH envronmental variable, so it never appears on the command line 2. In mysqldump and xtrabackup\* SST scripts which rely on MySQL authentication, instead of passing password on the command line, SST script sets MYSQL\_PWD environment variable, so that password also never appears on the mysqldump/innobackupex command line.
* [Revision #197e9d2](https://github.com/MariaDB/server/commit/197e9d2)\
  2015-05-26 15:44:34 +0300
  * Refs codership/mysql-wsrep#132 - fix for THD::m\_digest initialization, according to Raghu
* [Revision #483078b](https://github.com/MariaDB/server/commit/483078b)\
  2015-05-15 02:15:58 -0700
  * Fixes codership/QA#87 . An MTR test for SERIALIZABLE
* [Revision #4102d52](https://github.com/MariaDB/server/commit/4102d52)\
  2015-05-11 02:21:39 -0700
  * Refs codership/mysql-wsrep#113 - tests around FLUSH TABLE, FLUSH TABLES, LOCK TABLE
* [Revision #2106fed](https://github.com/MariaDB/server/commit/2106fed)\
  2015-05-10 21:49:36 +0300
  * Refs codership/mysql-wsrep#113 - changed BF thread's MDL wait to never timeout - all explicit locks are now honored by BF threads
* [Revision #f9805e4](https://github.com/MariaDB/server/commit/f9805e4)\
  2015-05-08 03:21:50 -0700
  * Galera MTR Tests: tests for WAN restart, xtrabackup options and others.
* [Revision #ef7b089](https://github.com/MariaDB/server/commit/ef7b089)\
  2015-05-06 10:35:02 +0300
  * Fixes codership/mysql-wsrep#122 - causal/casual typos fixed in wsrep code
* [Revision #bace2a9](https://github.com/MariaDB/server/commit/bace2a9)\
  2015-05-05 01:21:55 -0700
  * Galera MTR Tests: add a test for socket.ssl\_compression
* [Revision #b5ef2bb](https://github.com/MariaDB/server/commit/b5ef2bb)\
  2015-04-28 23:34:47 -0700
  * Re-enable tests previously disabled due to mysql-wsrep#114
* [Revision #63c5bee](https://github.com/MariaDB/server/commit/63c5bee)\
  2015-04-28 20:38:25 +0300
  * Refs codership/mysql-wsrep#113 - Extended the protection of local FLUSH sessions to cover all exclusive MDL locks
* [Revision #417f778](https://github.com/MariaDB/server/commit/417f778)\
  2015-04-28 00:55:50 -0700
  * Galera MTR tests: disable innodb.innodb\_stats\_\* due to mysql-wsrep#114
* [Revision #6bb890c](https://github.com/MariaDB/server/commit/6bb890c)\
  2015-04-24 10:39:42 +0300
  * refs codership/mysql-wsrep#114 - skipping TOI if not using wsrep provider
* [Revision #c666090](https://github.com/MariaDB/server/commit/c666090)\
  2015-04-21 16:22:53 +0300
  * Refs codership/mysql-wsrep#113 Protecting non replicated FLUSH session from brute force aborts
* [Revision #045b31c](https://github.com/MariaDB/server/commit/045b31c)\
  2015-04-20 05:58:24 -0700
  * Test cases for codership/mysql-wsrep/110
* [Revision #dc9e325](https://github.com/MariaDB/server/commit/dc9e325)\
  2015-04-20 13:18:21 +0300
  * refs codership/mysql-wsrep#110 - clear table map events on SAVEPOINT
* [Revision #d0e24c6](https://github.com/MariaDB/server/commit/d0e24c6)\
  2015-04-01 02:52:24 -0700
  * Galera MTR Tests: Attempt to remove rare sporadic failures in galera\_transaction\_replay.test by waiting for all transactions to get blocked before proceeding.
* [Revision #f8b724d](https://github.com/MariaDB/server/commit/f8b724d)\
  2015-03-31 06:43:38 -0700
  * Galera MTR Tests: Enable the use of --parallel for port-intensive Galera tests by additionally specifying --port-group-size=50
* [Revision #9f716ae](https://github.com/MariaDB/server/commit/9f716ae)\
  2015-03-29 23:56:21 -0700
  * Galera MTR: Disable rpl.rpl\_rotate\_logs binlog.binlog\_index due to codership/mysql-wsrep#71
* [Revision #fa5f18d](https://github.com/MariaDB/server/commit/fa5f18d)\
  2015-09-09 20:51:39 -0400
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #37ae601](https://github.com/MariaDB/server/commit/37ae601)\
  2015-09-09 18:54:14 -0400
  * Update WSREP\_PATCH\_REVNO
* [Revision #760b0c4](https://github.com/MariaDB/server/commit/760b0c4)\
  2015-08-27 00:41:56 -0700
  * Bump WSREP\_PATCH\_VERSION in cmake/wsrep.cmake to 12
* [Revision #bee94cc](https://github.com/MariaDB/server/commit/bee94cc)\
  2015-07-07 22:34:25 -0700
  * Fixes codership/mysql-wsrep#153 use --defaults-extra-file with mysqldump SST
* [Revision #55dfddf](https://github.com/MariaDB/server/commit/55dfddf)\
  2015-06-09 17:02:26 +0300
  * Fixing donate callback return code
* [Revision #0465e3a](https://github.com/MariaDB/server/commit/0465e3a)\
  2015-06-09 11:36:31 +0300
  * Logging message cleanup
* [Revision #d809fcc](https://github.com/MariaDB/server/commit/d809fcc)\
  2015-06-08 21:06:22 +0300
  * This commit fixes - errno handling in wsp::env::append() method, where error could be returned by mistake - return code of sst\_prepare\_other() when pthread\_create() fails - it was returning positive error code which by convention is treated as success.
* [Revision #1b1410c](https://github.com/MariaDB/server/commit/1b1410c)\
  2015-06-08 12:23:53 +0300
  * Slight cleanup improvement on a previous commit.
* [Revision #62c2539](https://github.com/MariaDB/server/commit/62c2539)\
  2015-06-08 01:46:20 -0700
  * Refs codership/mysql-wsrep#143 . Account for the case where the SST password is empty
* [Revision #a7ea3ec](https://github.com/MariaDB/server/commit/a7ea3ec)\
  2015-06-06 01:38:07 +0300
  * Synced xtrabackup SST fixes from Percona tree (as of PXC 5.6.24-25.11 release). This fixes/adresses the following LP bugs: - LP1380697: wsrep\_sst\_xtrabackup-v2 doesn't stop when mysql is SIGKILLed. (full fix for this (as engineeered by Percona) requires Linux-specific patch that we don't carry, but keep xtrabackup scripts as close as possible) - LP1399134: Log the innobackupex/SST logs in SST to syslog if possible. (fixed) - LP1405668: Race condition between donor and joiner in PXB SST. (fixed) - LP1405985: Fail early if xtrabackup\_checkkpoints is missing. (fixed) - LP1407599: wsrep\_sst\_xtrabackup-v2 script causes innobackupex to print a false positive stack trace into the log. (fixed) - LP1441762: IST Fails with SST script error. (fixed) - LP1451670: Fail when move-back fails in xtrabackup SST. (fixed)
* [Revision #d78110e](https://github.com/MariaDB/server/commit/d78110e)\
  2015-06-06 01:08:41 +0300
  * Refs codership/mysql-wsrep#141: this commit 1. Passes wsrep\_sst\_auth\_value to SST scripts via WSREP\_SST\_OPT\_AUTH envronmental variable, so it never appears on the command line 2. In mysqldump and xtrabackup\* SST scripts which rely on MySQL authentication, instead of passing password on the command line, SST script sets MYSQL\_PWD environment variable, so that password also never appears on the mysqldump/innobackupex command line.
* [Revision #4f4f3a5](https://github.com/MariaDB/server/commit/4f4f3a5)\
  2015-05-02 22:25:39 +0300
  * Fixes codership/mysql-wsrep#118
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
* [Revision #f533b2b](https://github.com/MariaDB/server/commit/f533b2b)\
  2015-08-25 11:15:45 -0400
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #b66455f6](https://github.com/MariaDB/server/commit/b66455f6)\
  2015-08-24 01:41:12 +0300
  * Increase the version number
* [Revision #aef8bfd](https://github.com/MariaDB/server/commit/aef8bfd)\
  2015-08-24 01:37:21 +0300
  * [MDEV-8670](https://jira.mariadb.org/browse/MDEV-8670) main.[MDEV-504](https://jira.mariadb.org/browse/MDEV-504) fails on Windows (in buildbot and outside)
* [Revision #472d663](https://github.com/MariaDB/server/commit/472d663)\
  2015-08-22 01:18:02 -0400
  * [MDEV-8149](https://jira.mariadb.org/browse/MDEV-8149): Random mtr test failures during warning check
* [Revision #4ee2886](https://github.com/MariaDB/server/commit/4ee2886)\
  2015-08-20 20:55:52 -0400
  * [MDEV-5146](https://jira.mariadb.org/browse/MDEV-5146) : Bulk loads into partitioned table not working
* [Revision #ccd39b2](https://github.com/MariaDB/server/commit/ccd39b2)\
  2015-08-20 09:55:54 -0400
  * Backport partition tests from 10.0-galera.
* [Revision #98bebad](https://github.com/MariaDB/server/commit/98bebad)\
  2015-08-18 17:03:28 -0400
  * Fix for a typo.
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

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
