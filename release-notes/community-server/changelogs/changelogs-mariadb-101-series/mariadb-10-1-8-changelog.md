# MariaDB 10.1.8 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.8)[Release Notes](../../old-releases/10.1/10.1.8.md)[Changelog](mariadb-10-1-8-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 17 Oct 2015

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.8.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #7e29f2d6](https://github.com/MariaDB/server/commit/7e29f2d6)\
  2015-10-15 18:25:54 +0400
  * [MDEV-8948](https://jira.mariadb.org/browse/MDEV-8948) ALTER ... INPLACE does work for BINARY, BLOB
* [Revision #1993780](https://github.com/MariaDB/server/commit/1993780)\
  2015-10-13 00:04:51 +0200
  * fix build on sol10-64
* [Revision #7454f1c](https://github.com/MariaDB/server/commit/7454f1c)\
  2015-10-15 08:49:58 +0200
  * fix events\_1 test for October 2015
* [Revision #534e424](https://github.com/MariaDB/server/commit/534e424)\
  2015-10-14 23:21:36 +0200
  * fix lowercase\* tests labrador
* [Revision #2a471e8](https://github.com/MariaDB/server/commit/2a471e8)\
  2015-10-14 15:29:57 +0200
  * fix func\_hybrid\_type crash in --ps --embedded
* [Revision #b867ade](https://github.com/MariaDB/server/commit/b867ade)\
  2015-10-14 18:33:16 +0400
  * Removing Used\_tables\_and\_const\_cache from "class udf\_handler". It was used only temporary, during udf\_handler::fix\_fields() time, and then copied to the owner Item\_func\_or\_sum object. Changing the code to use the Used\_tables\_and\_const\_cache part of the owner Item\_sum\_or\_func object directly.
* [Revision #3723c70](https://github.com/MariaDB/server/commit/3723c70)\
  2015-10-14 07:46:31 +0200
  * [MDEV-426](https://jira.mariadb.org/browse/MDEV-426): systemd PermissionsStartOnly=true by default
* [Revision #079cc48](https://github.com/MariaDB/server/commit/079cc48)\
  2015-10-14 07:32:34 +0200
  * [MDEV-426](https://jira.mariadb.org/browse/MDEV-426): systemd mariadb-sevice-convert - abs paths
* [Revision #82fb035](https://github.com/MariaDB/server/commit/82fb035)\
  2015-10-14 07:05:42 +0200
  * [MDEV-426](https://jira.mariadb.org/browse/MDEV-426): mariadb-service-convert to use MYSQLD\_OPTS
* [Revision #ddb93b4](https://github.com/MariaDB/server/commit/ddb93b4)\
  2015-10-14 05:14:06 -0400
  * WSREP\_TO\_ISOLATION\_BEGIN should be called with the table list.
* [Revision #950e6f5](https://github.com/MariaDB/server/commit/950e6f5)\
  2015-10-11 10:32:44 +0200
  * Fixed Fedora 22 package build failure.
* [Revision #6346d1d](https://github.com/MariaDB/server/commit/6346d1d)\
  2015-09-28 15:08:09 +0400
  * [MDEV-427](https://jira.mariadb.org/browse/MDEV-427)/[MDEV-5713](https://jira.mariadb.org/browse/MDEV-5713) Add systemd script with notify functionality
* [Revision #20c2ae3](https://github.com/MariaDB/server/commit/20c2ae3)\
  2015-09-17 22:16:19 +1000
  * [MDEV-427](https://jira.mariadb.org/browse/MDEV-427)/[MDEV-5713](https://jira.mariadb.org/browse/MDEV-5713) Add systemd script with notify functionality
* [Revision #92271c7](https://github.com/MariaDB/server/commit/92271c7)\
  2015-09-22 21:59:18 +0200
  * [MDEV-8087](https://jira.mariadb.org/browse/MDEV-8087): Server crashed in Time\_and\_counter\_tracker::incr\_loops
* [Revision #e19a6f3](https://github.com/MariaDB/server/commit/e19a6f3)\
  2015-10-12 10:03:04 +0200
  * Merge branch 'bb-10.1-serg' into 10.1
* [Revision #0b4c3ad](https://github.com/MariaDB/server/commit/0b4c3ad)\
  2015-10-12 10:49:37 +0400
  * Moving Used\_tables\_and\_const\_chache from Item\_func to Item\_func\_or\_sum and thus reusing Used\_tables\_and\_const\_cache for Item\_sum instead of declaring the same members inside Item\_sum.
* [Revision #dfb74de](https://github.com/MariaDB/server/commit/dfb74de)\
  2015-10-12 00:37:58 +0200
  * Merge branch '10.0' into 10.1
* [Revision #b785857](https://github.com/MariaDB/server/commit/b785857)\
  2015-10-11 11:53:02 +0200
  * s/--silent/--silent-startup/
* [Revision #b4fad1f](https://github.com/MariaDB/server/commit/b4fad1f)\
  2015-10-11 07:57:40 +0200
  * fix feedback plugin tests
* [Revision #c4e336e](https://github.com/MariaDB/server/commit/c4e336e)\
  2015-10-10 14:19:02 +0200
  * fix the encryption.filekeys\_nofile test
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
* [Revision #affff1a](https://github.com/MariaDB/server/commit/affff1a)\
  2015-10-09 13:08:41 +0300
  * Less logging of not critial things during startup/shutdown:
* [Revision #602c803](https://github.com/MariaDB/server/commit/602c803)\
  2015-10-09 13:02:55 +0300
  * Don't enable file\_key\_management\_plugin by default (as this gives warnings in the log) Better warning from file\_key\_management plugin if filename is not given
* [Revision #c696fc7](https://github.com/MariaDB/server/commit/c696fc7)\
  2015-10-09 13:01:07 +0300
  * Fixed compiler warnings and errors
* [Revision #b0935fc](https://github.com/MariaDB/server/commit/b0935fc)\
  2015-10-07 15:52:26 +0500
  * [MDEV-8842](https://jira.mariadb.org/browse/MDEV-8842) add group support to pam\_user\_map module. Added to the pam\_user\_map module.
* [Revision #3757bc5](https://github.com/MariaDB/server/commit/3757bc5)\
  2015-10-05 14:46:12 +0500
  * [MDEV-8431](https://jira.mariadb.org/browse/MDEV-8431) Feedback plugin needs an option for http proxy. 'feedback\_http\_proxy' system variable added to specify the proxy server as host:port. Not a dynamic one.
* [Revision #f41a41f](https://github.com/MariaDB/server/commit/f41a41f)\
  2015-10-09 00:06:16 +0200
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #db79f4c](https://github.com/MariaDB/server/commit/db79f4c)\
  2015-10-08 23:02:43 +0200
  * 5.5.45-37.4
* [Revision #82e9f6d](https://github.com/MariaDB/server/commit/82e9f6d)\
  2015-10-08 22:54:24 +0200
  * Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #16ad1fc](https://github.com/MariaDB/server/commit/16ad1fc)\
  2015-10-08 20:48:46 +0400
  * [MDEV-8921](https://jira.mariadb.org/browse/MDEV-8921) Wrong result for CAST(AVG(double\_column) AS SIGNED)
* [Revision #7091b78](https://github.com/MariaDB/server/commit/7091b78)\
  2015-10-08 19:19:21 +0400
  * [MDEV-8918](https://jira.mariadb.org/browse/MDEV-8918) Wrong result for CAST(AVG(bigint\_column) AS SIGNED)
* [Revision #174a0b9](https://github.com/MariaDB/server/commit/174a0b9)\
  2015-10-08 12:09:05 +0400
  * Clean-up: Item\_sum\_variance and Item\_variance\_field had hybrid type infrastructure, though in fact they always return REAL result. Removing hybrid type artifacts.
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
* [Revision #de1a48e](https://github.com/MariaDB/server/commit/de1a48e)\
  2015-10-08 08:59:58 +0400
  * A clean-up for a few recent result set metadata related bug fixes: - [MDEV-8875](https://jira.mariadb.org/browse/MDEV-8875) Wrong metadata for MAX(CAST(time\_column AS DATETIME)) - [MDEV-8873](https://jira.mariadb.org/browse/MDEV-8873) Wrong field type or metadata for LEAST(int\_column,string\_column) - [MDEV-8912](https://jira.mariadb.org/browse/MDEV-8912) Wrong metadata or type for @c:=string\_or\_blob\_field
* [Revision #8777724](https://github.com/MariaDB/server/commit/8777724)\
  2015-10-07 20:19:29 +0400
  * [MDEV-8912](https://jira.mariadb.org/browse/MDEV-8912) Wrong metadata or type for @c:=string\_or\_blob\_field
* [Revision #8afe96f](https://github.com/MariaDB/server/commit/8afe96f)\
  2015-10-07 11:42:23 +0400
  * [MDEV-8910](https://jira.mariadb.org/browse/MDEV-8910) Wrong metadata or field type for MAX(COALESCE(string\_field))
* [Revision #bed4e84](https://github.com/MariaDB/server/commit/bed4e84)\
  2015-08-18 13:28:17 +0200
  * [MDEV-8380](https://jira.mariadb.org/browse/MDEV-8380): Subquery parse error
* [Revision #d6371d3](https://github.com/MariaDB/server/commit/d6371d3)\
  2015-10-06 18:03:10 +0300
  * Combined fix for [MDEV-7267](https://jira.mariadb.org/browse/MDEV-7267) and [MDEV-8864](https://jira.mariadb.org/browse/MDEV-8864)
* [Revision #4a60204](https://github.com/MariaDB/server/commit/4a60204)\
  2015-10-06 16:15:34 +0300
  * [MDEV-8903](https://jira.mariadb.org/browse/MDEV-8903): Buildbot valgrind failure: Invalid read of size 1 in sql\_memdup...
* [Revision #1289794](https://github.com/MariaDB/server/commit/1289794)\
  2015-10-06 15:54:37 +0300
  * Fix for [MDEV-8321](https://jira.mariadb.org/browse/MDEV-8321), [MDEV-6223](https://jira.mariadb.org/browse/MDEV-6223)
* [Revision #21adad0](https://github.com/MariaDB/server/commit/21adad0)\
  2015-10-06 15:40:26 +0300
  * [MDEV-8901](https://jira.mariadb.org/browse/MDEV-8901): InnoDB: Punch hole is incorrecty done also to log files causing assertion and database corruption
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
* [Revision #90f2c82](https://github.com/MariaDB/server/commit/90f2c82)\
  2015-10-05 16:09:21 +0500
  * [MDEV-7817](https://jira.mariadb.org/browse/MDEV-7817) ALTER TABLE {ADD|DROP} INDEX IF \[NOT] EXISTS does not get written into binlog if nothing to do. Just log the ALTER statement even if there's nothing to do.
* [Revision #3c47809](https://github.com/MariaDB/server/commit/3c47809)\
  2015-10-06 00:48:46 +0400
  * Clean-up: changing switch(result\_type()) followed by a test for temporal types in case of STRING\_RESULT to switch(cmp\_type()).
* [Revision #56cd7d0](https://github.com/MariaDB/server/commit/56cd7d0)\
  2015-09-19 12:58:41 +0200
  * compilation failure on windows
* [Revision #6b0b194](https://github.com/MariaDB/server/commit/6b0b194)\
  2015-09-16 12:48:24 +0200
  * fix installation location for policy files
* [Revision #3407438](https://github.com/MariaDB/server/commit/3407438)\
  2015-10-04 09:53:05 +0200
  * fixes for buildbot
* [Revision #e302602](https://github.com/MariaDB/server/commit/e302602)\
  2015-05-28 22:42:32 +1000
  * plugin: qc\_info test - hide output so result isn't a binary file
* [Revision #d455793](https://github.com/MariaDB/server/commit/d455793)\
  2015-05-18 22:03:01 +1000
  * plugin - qc\_info - add Query Cache flags
* [Revision #3abfe76](https://github.com/MariaDB/server/commit/3abfe76)\
  2015-10-03 08:22:17 +0200
  * remove unused group\_by\_handler::init() method
* [Revision #21175bb](https://github.com/MariaDB/server/commit/21175bb)\
  2015-10-02 18:40:38 +0200
  * Don't use flags in the group\_by\_handler class
* [Revision #8dff1aa](https://github.com/MariaDB/server/commit/8dff1aa)\
  2015-10-02 13:06:30 +0200
  * bug: move one\_storage\_engine checking loop
* [Revision #c93ac0a](https://github.com/MariaDB/server/commit/c93ac0a)\
  2015-10-02 14:38:06 +0200
  * cleanups and simplifications
* [Revision #7ca8b4b](https://github.com/MariaDB/server/commit/7ca8b4b)\
  2015-10-02 10:19:40 +0200
  * move internal API out from group\_by\_handler
* [Revision #9ca3d9e](https://github.com/MariaDB/server/commit/9ca3d9e)\
  2015-10-02 10:19:34 +0200
  * remove unused method
* [Revision #e8daa41](https://github.com/MariaDB/server/commit/e8daa41)\
  2015-10-05 09:47:45 +0200
  * typos in comments, minor stylistic edits
* [Revision #cf50e13](https://github.com/MariaDB/server/commit/cf50e13)\
  2015-10-02 10:18:27 +0200
  * [MDEV-6080](https://jira.mariadb.org/browse/MDEV-6080): Allowing storage engine to shortcut group by queries
* [Revision #d8df2b94](https://github.com/MariaDB/server/commit/d8df2b94)\
  2015-10-02 10:18:40 +0200
  * Bugs, found by valgrind
* [Revision #ae2cdc1](https://github.com/MariaDB/server/commit/ae2cdc1)\
  2015-09-27 21:28:48 +0200
  * fix comments
* [Revision #8ed5fde](https://github.com/MariaDB/server/commit/8ed5fde)\
  2015-09-27 21:28:07 +0200
  * bug in JOIN\_TAB::cleanup() that caused freed memory to be accessed
* [Revision #4193fa7](https://github.com/MariaDB/server/commit/4193fa7)\
  2015-09-27 21:30:18 +0200
  * Simple optimization
* [Revision #7e31279](https://github.com/MariaDB/server/commit/7e31279)\
  2015-05-16 18:00:32 +0300
  * Speed up some innodb tests Fixed compiler warnings
* [Revision #b2b07b3](https://github.com/MariaDB/server/commit/b2b07b3)\
  2015-05-11 23:11:05 +0300
  * Don't write DROP TEMPORARY TABLE to binary log
* [Revision #d2f6166](https://github.com/MariaDB/server/commit/d2f6166)\
  2015-10-05 16:47:34 +0300
  * [MDEV-8830](https://jira.mariadb.org/browse/MDEV-8830): Weird output in the error log
* [Revision #23d4c95](https://github.com/MariaDB/server/commit/23d4c95)\
  2015-10-05 16:16:13 +0400
  * [MDEV-8896](https://jira.mariadb.org/browse/MDEV-8896) Dead code in stored\_field\_cmp\_to\_item()
* [Revision #9337173](https://github.com/MariaDB/server/commit/9337173)\
  2015-10-05 09:27:33 +0300
  * [MDEV-8893](https://jira.mariadb.org/browse/MDEV-8893): Test encryption.innodb\_encryption\_filekeys fails on buildbot
* [Revision #ba0b668](https://github.com/MariaDB/server/commit/ba0b668)\
  2015-10-04 09:37:57 +0400
  * A clean-up for [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950): - Turning get\_mm\_tree\_for\_const() from a static function into a protected method in Item. - Adding a new class Item\_bool\_func2\_with\_rev, for the functions and operators that have a reverse function and can use the range optimizer for to optimize "value OP field" as "field REV\_OP value". Deriving Item\_bool\_rowready\_func2 and Item\_funt\_spatial\_rel from the new class. - Removing Item\_bool\_func2::have\_rev\_func().
* [Revision #100d77e](https://github.com/MariaDB/server/commit/100d77e)\
  2015-10-02 14:48:32 +0400
  * Clean-up: removing the unused "Item\_result cmp\_type" parameter from the methods: - Item\_bool\_func::get\_func\_mm\_tree() - Item\_bool\_func::get\_mm\_parts() - Item\_bool\_func::get\_ne\_mm\_tree()
* [Revision #322bc6e](https://github.com/MariaDB/server/commit/322bc6e)\
  2015-10-02 12:14:50 +0400
  * Adding "virtual bool Field::can\_optimize\_range(...)" and moving the code from Item\_bool\_func::get\_mm\_leaf() into Field\_xxx::can\_optimize\_range(). This reduces the total amount of virtual calls. Also, it's a prerequisite change for the pluggable data types.
* [Revision #5e7f100](https://github.com/MariaDB/server/commit/5e7f100)\
  2015-10-01 13:50:11 +0300
  * [MDEV-8523](https://jira.mariadb.org/browse/MDEV-8523): InnoDB: Assertion failure in file buf0buf.cc line 5963 (Failing assertion: key\_version == 0 || key\_version >= bpage->key\_version)
* [Revision #6b36fb9](https://github.com/MariaDB/server/commit/6b36fb9)\
  2015-10-02 08:54:25 +0400
  * Clean-up: sharing duplicate code in Item\_field::val\_bool\_result() and Item\_ref::val\_bool\_result().
* [Revision #38f3b99](https://github.com/MariaDB/server/commit/38f3b99)\
  2015-10-01 20:36:25 -0400
  * [MDEV-8831](https://jira.mariadb.org/browse/MDEV-8831) : enforce\_storage\_engine doesn't block table creation on other nodes
* [Revision #accf9b5](https://github.com/MariaDB/server/commit/accf9b5)\
  2015-10-01 20:01:35 +0400
  * [MDEV-5694](https://jira.mariadb.org/browse/MDEV-5694) GREATEST(date, time) returns a wrong data type
* [Revision #a84fae2](https://github.com/MariaDB/server/commit/a84fae2)\
  2015-10-01 11:35:18 +0400
  * [MDEV-8836](https://jira.mariadb.org/browse/MDEV-8836) - Server crashed in my\_copy\_8bit on querying I\_S.PROCESSLIST
* [Revision #e1cbca1](https://github.com/MariaDB/server/commit/e1cbca1)\
  2015-10-01 14:21:12 +0400
  * [MDEV-657](https://jira.mariadb.org/browse/MDEV-657) [Bug #873142](https://bugs.launchpad.net/bugs/873142) - GREATEST() does not always return same signness of argument types. The patch for [MDEV-8871](https://jira.mariadb.org/browse/MDEV-8871) also fixed the problem reported in [MDEV-657](https://jira.mariadb.org/browse/MDEV-657). Adding the test case from the bug report.
* [Revision #b50c607](https://github.com/MariaDB/server/commit/b50c607)\
  2015-10-01 14:07:42 +0400
  * [MDEV-4848](https://jira.mariadb.org/browse/MDEV-4848) Wrong metadata or column type for LEAST(1.0,'10') [MDEV-8873](https://jira.mariadb.org/browse/MDEV-8873) Wrong field type or metadata for LEAST(int\_column,string\_column)
* [Revision #bb22eb5](https://github.com/MariaDB/server/commit/bb22eb5)\
  2015-10-01 13:40:23 +0400
  * [MDEV-8379](https://jira.mariadb.org/browse/MDEV-8379) - SUSE mariadb patches
* [Revision #727da9c](https://github.com/MariaDB/server/commit/727da9c)\
  2015-10-01 13:04:59 +0400
  * [MDEV-8379](https://jira.mariadb.org/browse/MDEV-8379) - SUSE mariadb patches
* [Revision #3266216](https://github.com/MariaDB/server/commit/3266216)\
  2015-10-01 08:16:14 +0300
  * [MDEV-8727](https://jira.mariadb.org/browse/MDEV-8727): Server/InnoDB hangs on shutdown after trying to read an encrypted table with a wrong key
* [Revision #cb2c799](https://github.com/MariaDB/server/commit/cb2c799)\
  2015-09-30 16:04:24 +0400
  * [MDEV-8860](https://jira.mariadb.org/browse/MDEV-8860) Wrong result for WHERE 2016 < SOME (SELECT CAST(time\_column AS DATETIME) FROM t1) [MDEV-8875](https://jira.mariadb.org/browse/MDEV-8875) Wrong metadata for MAX(CAST(time\_column AS DATETIME))
* [Revision #cc9cfec](https://github.com/MariaDB/server/commit/cc9cfec)\
  2015-09-30 12:37:34 +0400
  * [MDEV-8865](https://jira.mariadb.org/browse/MDEV-8865) Wrong field type or metadata for COALESCE(signed\_int\_column, unsigned\_int\_column) Item\_func\_hybrid\_field\_type did not return correct field\_type(), cmp\_type() and result\_type() in some cases, because cached\_result\_type and cached\_field\_type were set in independent pieces of the code and did not properly match to each other. Fix: - Removing Item\_func\_hybrid\_result\_type - Deriving Item\_func\_hybrid\_field\_type directly from Item\_func - Introducing a new class Type\_handler which guarantees that field\_type(), cmp\_type() and result\_type() are always properly synchronized and using the new class in Item\_func\_hybrid\_field\_type.
* [Revision #006acf7](https://github.com/MariaDB/server/commit/006acf7)\
  2015-09-30 10:49:45 +0300
  * Bug #68148: drop index on a foreign key column leads to missing table [MDEV-8845](https://jira.mariadb.org/browse/MDEV-8845): Table disappear after modifying FK
* [Revision #09b87d6](https://github.com/MariaDB/server/commit/09b87d6)\
  2015-09-30 10:05:16 +0400
  * [MDEV-8871](https://jira.mariadb.org/browse/MDEV-8871) Wrong result for CREATE TABLE .. SELECT LEAST(unsigned\_column,unsigned\_column)
* [Revision #c13f409](https://github.com/MariaDB/server/commit/c13f409)\
  2015-09-29 15:15:28 +0300
  * [MDEV-8815](https://jira.mariadb.org/browse/MDEV-8815): InnoDB should refuse to start if crash recovery fails instead of asserting
* [Revision #a95711e](https://github.com/MariaDB/server/commit/a95711e)\
  2015-09-29 08:39:54 +0300
  * [MDEV-8855](https://jira.mariadb.org/browse/MDEV-8855): innodb.innodb-fk-warnings fails on Windows
* [Revision #a4e5902](https://github.com/MariaDB/server/commit/a4e5902)\
  2015-09-28 19:12:05 +0400
  * [MDEV-8862](https://jira.mariadb.org/browse/MDEV-8862) Wrong field type for MAX(COALESCE(datetime\_column))
* [Revision #c5922c5](https://github.com/MariaDB/server/commit/c5922c5)\
  2015-09-28 13:59:44 +0300
  * [MDEV-8821](https://jira.mariadb.org/browse/MDEV-8821): Failing assertion: !page || page\_type != 0 in file log0recv. cc line 1404
* [Revision #02a38fd](https://github.com/MariaDB/server/commit/02a38fd)\
  2015-09-24 17:25:52 +0200
  * [MDEV-8624](https://jira.mariadb.org/browse/MDEV-8624): MariaDB hangs on query with many logical condition
* [Revision #3cc6e5b](https://github.com/MariaDB/server/commit/3cc6e5b)\
  2015-09-28 12:51:02 +0400
  * [MDEV-8852](https://jira.mariadb.org/browse/MDEV-8852) Implicit or explicit CAST from MAX(string) to INT,DOUBLE,DECIMAL does not produce warnings
* [Revision #54db387](https://github.com/MariaDB/server/commit/54db387)\
  2015-09-22 16:39:05 +0400
  * [MDEV-8682](https://jira.mariadb.org/browse/MDEV-8682) - CSV engine does not properly process "", in quotes
* [Revision #f804b74](https://github.com/MariaDB/server/commit/f804b74)\
  2015-09-28 03:40:29 +0300
  * [MDEV-8154](https://jira.mariadb.org/browse/MDEV-8154) rpl.show\_status\_stop\_slave\_race-7126 sporadically causes internal check failure
* [Revision #bca5894](https://github.com/MariaDB/server/commit/bca5894)\
  2015-09-27 19:20:43 -0400
  * Adjust warning suppression over a recent change in galera library.
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
* [Revision #6927459](https://github.com/MariaDB/server/commit/6927459)\
  2015-09-25 13:56:02 -0400
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): Sporadic SEGFAULT on startup
* [Revision #59037d9](https://github.com/MariaDB/server/commit/59037d9)\
  2015-09-16 23:20:57 -0400
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): Sporadic SEGFAULT on startup
* [Revision #30711c6](https://github.com/MariaDB/server/commit/30711c6)\
  2015-09-25 21:33:50 +0400
  * [MDEV-8806](https://jira.mariadb.org/browse/MDEV-8806) Numeric CAST produce different warnings for strings literals vs functions
* [Revision #26e4403](https://github.com/MariaDB/server/commit/26e4403)\
  2015-09-24 14:02:18 +0300
  * [MDEV-8819](https://jira.mariadb.org/browse/MDEV-8819): Failing assertion: block->page.space == page\_get\_space\_id(page\_align(ptr)) in file buf0buf.cc line 2551
* [Revision #9554342](https://github.com/MariaDB/server/commit/9554342)\
  2015-09-25 10:24:14 +0200
  * Merge branch '10.1' into pull-request-97
* [Revision #4070ce0](https://github.com/MariaDB/server/commit/4070ce0)\
  2015-09-25 07:18:04 +0400
  * [MDEV-8635](https://jira.mariadb.org/browse/MDEV-8635) Redundant warnings on WHERE decimal\_column='ax' The fix for [MDEV-8466](https://jira.mariadb.org/browse/MDEV-8466) earlier fixed [MDEV-8635](https://jira.mariadb.org/browse/MDEV-8635) as well. Adding a test only.
* [Revision #dca4ab9](https://github.com/MariaDB/server/commit/dca4ab9)\
  2015-09-24 21:24:28 +0300
  * [MDEV-8841](https://jira.mariadb.org/browse/MDEV-8841) innodb\_zip.innodb-create-options fails in buildbot
* [Revision #1250018](https://github.com/MariaDB/server/commit/1250018)\
  2015-09-24 16:31:45 +0300
  * Fix typos in JSON MRR output
* [Revision #7016621](https://github.com/MariaDB/server/commit/7016621)\
  2015-09-24 15:43:01 +0300
  * [MDEV-8829](https://jira.mariadb.org/browse/MDEV-8829): Assertion \`0' failed in Explain\_table\_access::tag\_to\_json
* [Revision #428f03c](https://github.com/MariaDB/server/commit/428f03c)\
  2015-09-24 15:48:02 +0400
  * [MDEV-8839](https://jira.mariadb.org/browse/MDEV-8839) COLUMN\_GET() produces warnings with no data
* [Revision #5cc149f](https://github.com/MariaDB/server/commit/5cc149f)\
  2015-09-24 10:28:47 +0200
  * The compiler warnings fixed.
* [Revision #e541894](https://github.com/MariaDB/server/commit/e541894)\
  2015-09-23 20:59:54 +0400
  * Fixing a failure in "mtr --ps xml", introduced by the patch for [MDEV-8466](https://jira.mariadb.org/browse/MDEV-8466) and [MDEV-8468](https://jira.mariadb.org/browse/MDEV-8468). Using --enable\_prepare\_warnings and --disable\_prepare\_warnings around the affected query, to have the same warning in regular and --ps mtr runs.
* [Revision #3ad035f](https://github.com/MariaDB/server/commit/3ad035f)\
  2015-09-23 20:42:28 +0400
  * [MDEV-8658](https://jira.mariadb.org/browse/MDEV-8658) DATE(zerofill\_column) and DATE(COALESCE(zerofill\_column)) return different results [MDEV-8660](https://jira.mariadb.org/browse/MDEV-8660) TIME(int\_zerofill\_column) returns a wrong result
* [Revision #b9da3ba](https://github.com/MariaDB/server/commit/b9da3ba)\
  2015-09-23 19:28:20 +0300
  * Follow-up for [MDEV-6756](https://jira.mariadb.org/browse/MDEV-6756) - fix the ps-protocol version of the tests
* [Revision #70effb6](https://github.com/MariaDB/server/commit/70effb6)\
  2015-09-23 19:15:29 +0300
  * Follow-up for [MDEV-6756](https://jira.mariadb.org/browse/MDEV-6756) - fix the embedded version of the test
* [Revision #138e7bf](https://github.com/MariaDB/server/commit/138e7bf)\
  2015-09-23 19:06:21 +0300
  * Follow up for disabling encrypt\_tmp\_files and encrypt\_binlog by default
* [Revision #5c62dd2](https://github.com/MariaDB/server/commit/5c62dd2)\
  2015-09-23 12:32:47 +0300
  * [MDEV-8832](https://jira.mariadb.org/browse/MDEV-8832): Encryption meta data should not be stored when ENCRYPTED=DEFAULT and innodb-encrypt-tables=OFF
* [Revision #212698b](https://github.com/MariaDB/server/commit/212698b)\
  2015-09-23 13:04:28 +0400
  * [MDEV-8253](https://jira.mariadb.org/browse/MDEV-8253) EXPLAIN SELECT prints unexpected characters Item\_string::clone\_item() creates a new Item\_string that points exactly to the same buffer that the original one does. Later, Item\_string::print() uses c\_ptr() for the original Item\_string, which reallocs the original buffer, and the clone remain with the old freed buffer. Refactoring the code not to use c\_ptr() in Item\_string::print().
* [Revision #180c44e](https://github.com/MariaDB/server/commit/180c44e)\
  2015-09-23 10:15:38 +0300
  * [MDEV-8817](https://jira.mariadb.org/browse/MDEV-8817): Failing assertion: new\_state->key\_version != ENCRYPTION\_KEY\_VERSION\_INVALID
* [Revision #7cbecad](https://github.com/MariaDB/server/commit/7cbecad)\
  2015-09-17 17:01:00 +0400
  * [MDEV-8664](https://jira.mariadb.org/browse/MDEV-8664) - plugins.show\_all\_plugins --embedded fails in buildbot
* [Revision #0cf39f4](https://github.com/MariaDB/server/commit/0cf39f4)\
  2015-09-22 15:03:59 +0300
  * [MDEV-8817](https://jira.mariadb.org/browse/MDEV-8817): Failing assertion: new\_state->key\_version != ENCRYPTION\_KEY\_VERSION\_INVALID
* [Revision #fea1568](https://github.com/MariaDB/server/commit/fea1568)\
  2015-09-22 13:35:23 +0200
  * Fix sporadic test failure in rpl\_gtid\_mdev4820.test
* [Revision #5c9c8ef](https://github.com/MariaDB/server/commit/5c9c8ef)\
  2015-09-22 14:01:54 +0400
  * [MDEV-3929](https://jira.mariadb.org/browse/MDEV-3929) Add system variable explicit\_defaults\_for\_timestamp for compatibility with MySQL
* [Revision #81727cd](https://github.com/MariaDB/server/commit/81727cd)\
  2015-09-22 12:54:01 +0300
  * Backport to 10.0: [MDEV-8779](https://jira.mariadb.org/browse/MDEV-8779): mysqld got signal 11 in sql/opt\_range\_mrr.cc:100(step\_down\_to)
* [Revision #89af0f1](https://github.com/MariaDB/server/commit/89af0f1)\
  2015-09-21 11:24:08 +0300
  * [MDEV-8770](https://jira.mariadb.org/browse/MDEV-8770): Incorrect error message when importing page compressed tablespace
* [Revision #e96f3c7](https://github.com/MariaDB/server/commit/e96f3c7)\
  2015-09-22 00:57:29 +0300
  * [MDEV-8779](https://jira.mariadb.org/browse/MDEV-8779): mysqld got signal 11 in sql/opt\_range\_mrr.cc:100(step\_down\_to)
* [Revision #22cc8f9](https://github.com/MariaDB/server/commit/22cc8f9)\
  2015-09-21 19:04:32 +0400
  * Changing a number of functions to aggregate argument character sets and collations from the global name space into private and protected methods in Item\_func\_or\_sum.
* [Revision #8d0d445](https://github.com/MariaDB/server/commit/8d0d445)\
  2015-09-21 17:32:37 +0300
  * Backport to 10.0: [MDEV-8779](https://jira.mariadb.org/browse/MDEV-8779): mysqld got signal 11 in sql/opt\_range\_mrr.cc:100(step\_down\_to)
* [Revision #9b9e36e](https://github.com/MariaDB/server/commit/9b9e36e)\
  2015-09-20 21:31:02 +0300
  * [MDEV-8779](https://jira.mariadb.org/browse/MDEV-8779): mysqld got signal 11 in sql/opt\_range\_mrr.cc:100(step\_down\_to)
* [Revision #139ce6c](https://github.com/MariaDB/server/commit/139ce6c)\
  2015-09-21 15:15:23 +0200
  * fix for 32bit system. Not meaninful for this test but volatile parameters replaced.
* [Revision #c8db0df](https://github.com/MariaDB/server/commit/c8db0df)\
  2015-09-21 16:18:20 +0400
  * Removing "DTCollation Arg\_comparator::cmp\_collation". Using a CHARSET\_INFO pointer instead.
* [Revision #2dc32c0](https://github.com/MariaDB/server/commit/2dc32c0)\
  2015-09-21 15:52:50 +0400
  * Removing "DTCollation user\_var\_entry::collation", using a CHARSET\_INFO pointer instread, as the "derivation" and "repertoire" parts of DTCollation were not really used by user\_var\_entry.
* [Revision #afa1773](https://github.com/MariaDB/server/commit/afa1773)\
  2015-09-21 12:40:07 +0400
  * Moving Item\_args::arg\_count from "public" to "protected".
* [Revision #1956340](https://github.com/MariaDB/server/commit/1956340)\
  2015-09-21 12:21:46 +0400
  * Removing global function agg\_item\_charsets\_for\_string\_result(). Moving agg\_arg\_charsets\_for\_string\_result() and agg\_arg\_charsets\_for\_string\_result\_with\_comparison() inside "protected" section in Item\_func\_or\_sum.
* [Revision #f727fb4](https://github.com/MariaDB/server/commit/f727fb4)\
  2015-09-20 20:22:22 +0200
  * Fix to make os\_thread\_id it compiled on windows.
* [Revision #d39a2f7](https://github.com/MariaDB/server/commit/d39a2f7)\
  2015-09-19 09:08:58 -0400
  * Update mandatory wsrep configuration options
* [Revision #161db7c](https://github.com/MariaDB/server/commit/161db7c)\
  2015-09-19 11:30:18 +0300
  * [MDEV-8773](https://jira.mariadb.org/browse/MDEV-8773): InnoDB innochecksum does not work with encrypted or page compressed tables
* [Revision #b75c003](https://github.com/MariaDB/server/commit/b75c003)\
  2015-09-18 23:03:35 +0400
  * [MDEV-8816](https://jira.mariadb.org/browse/MDEV-8816) Equal field propagation is not applied for WHERE varbinary\_column>=\_utf8'a' COLLATE utf8\_general\_ci AND varbinary\_column='A';
    1. Removing the legacy code that disabled equal field propagation in cases when comparison is done as VARBINARY. This is now correctly handled by the new propagation code in Item\_xxx::propagate\_equal\_fields() and Field\_str::can\_be\_substituted\_to\_equal\_item (the bug fix).
    2. Also, removing legacy (pre-MySQL-4.1) Arg\_comparator methods compare\_binary\_string() and compare\_e\_binary\_string(), as VARBINARY comparison is correcty handled in compare\_string() and compare\_e\_string() by the corresponding VARBINARY collation handler implemented in my\_charset\_bin. (not really a part of the bug fix)
* [Revision #da3ec3d](https://github.com/MariaDB/server/commit/da3ec3d)\
  2015-09-09 16:29:50 +0200
  * [MDEV-7970](https://jira.mariadb.org/browse/MDEV-7970): EXPLAIN FORMAT=JSON does not print HAVING
* [Revision #79140b0](https://github.com/MariaDB/server/commit/79140b0)\
  2015-09-18 13:30:44 +0400
  * [MDEV-8793](https://jira.mariadb.org/browse/MDEV-8793) Wrong result set for SELECT ... WHERE COALESCE(time\_column)=TIME('00:00:00') AND COALESCE(time\_column)=DATE('2015-09-11') [MDEV-8814](https://jira.mariadb.org/browse/MDEV-8814) Wrong result for WHERE datetime\_column > TIME('00:00:00')
* [Revision #f789158](https://github.com/MariaDB/server/commit/f789158)\
  2015-09-17 19:49:49 +0400
  * The patch for [MDEV-8466](https://jira.mariadb.org/browse/MDEV-8466) revealed a bug in str2my\_decimal, which did not return a correct "end\_of\_num" pointer in case of character sets with mbminlen>1 (ucs2, utf16, utf16le, utf32). The bug caused sporadic test failures on BuildBot, as well "uninitialized memory read" errors in valgrind builds.
* [Revision #c83810f](https://github.com/MariaDB/server/commit/c83810f)\
  2015-09-17 12:38:06 +0300
  * Fix test failures seen on buildbot where file\_key\_management plugin is linked statically and dynamic plugin is not available.
* [Revision #7dd137c](https://github.com/MariaDB/server/commit/7dd137c)\
  2015-08-12 23:09:48 +0200
  * [MDEV-6756](https://jira.mariadb.org/browse/MDEV-6756): map a linux pid (child pid) to a connection id shown in the output of SHOW PROCESSLIST
* [Revision #d9b25ae](https://github.com/MariaDB/server/commit/d9b25ae)\
  2015-09-17 11:05:07 +0400
  * [MDEV-8466](https://jira.mariadb.org/browse/MDEV-8466) CAST works differently for DECIMAL/INT vs DOUBLE for empty strings [MDEV-8468](https://jira.mariadb.org/browse/MDEV-8468) CAST and INSERT work differently for DECIMAL/INT vs DOUBLE for a string with trailing spaces
* [Revision #c69cf93](https://github.com/MariaDB/server/commit/c69cf93)\
  2015-09-16 17:24:34 +0400
  * [MDEV-8673](https://jira.mariadb.org/browse/MDEV-8673) - \[PATCH] Missing Sanity Check for strndup() in [MariaDB 10.0.2](../../old-releases/10.0/10.0.2.md) x
* [Revision #173e486](https://github.com/MariaDB/server/commit/173e486)\
  2015-09-16 13:01:04 +0300
  * [MDEV-8576](https://jira.mariadb.org/browse/MDEV-8576): Bootstrap should ignore --enforce-storage-engine option
* [Revision #bb52905](https://github.com/MariaDB/server/commit/bb52905)\
  2015-09-15 18:58:08 -0400
  * [MDEV-8034](https://jira.mariadb.org/browse/MDEV-8034) : wsrep\_node\_address can't be IPV6
* [Revision #31cf362](https://github.com/MariaDB/server/commit/31cf362)\
  2015-09-15 08:49:55 -0400
  * [MDEV-7873](https://jira.mariadb.org/browse/MDEV-7873): rpl.rpl\_domain\_id\_filter fails sporadically in buildbot #2
* [Revision #6cc1bef](https://github.com/MariaDB/server/commit/6cc1bef)\
  2015-09-15 14:11:33 +0300
  * Fix test to do proper cleanup.
* [Revision #9e6f3df](https://github.com/MariaDB/server/commit/9e6f3df)\
  2015-09-15 09:35:38 +0300
  * [MDEV-8799](https://jira.mariadb.org/browse/MDEV-8799): Server crashes in btr\_defragment\_add\_index, encryption.innodb-bad-key-change5 and alike fail in buildbot
* [Revision #3a0df3c](https://github.com/MariaDB/server/commit/3a0df3c)\
  2015-09-15 10:11:52 +0400
  * [MDEV-8372](https://jira.mariadb.org/browse/MDEV-8372) Use helper methods introduced in [MDEV-7824](https://jira.mariadb.org/browse/MDEV-7824) all around the code
* [Revision #3079bd4](https://github.com/MariaDB/server/commit/3079bd4)\
  2015-09-14 16:28:16 +0300
  * Fix release build compile failure.
* [Revision #4d3f680](https://github.com/MariaDB/server/commit/4d3f680)\
  2015-09-14 14:11:23 +0300
  * [MDEV-8772](https://jira.mariadb.org/browse/MDEV-8772): Assertion failure in file ha\_innodb.cc line 20027 when importing page compressed and encrypted tablespace using incorrect keys
* [Revision #5448df0](https://github.com/MariaDB/server/commit/5448df0)\
  2015-09-14 12:02:20 +0200
  * restore CRLF file ending in the test data
* [Revision #ddaddf1](https://github.com/MariaDB/server/commit/ddaddf1)\
  2015-09-14 12:15:27 +0300
  * [MDEV-8769](https://jira.mariadb.org/browse/MDEV-8769): Server crash at file btr0btr.ic line 122 when defragmenting encrypted table using incorrect keys
* [Revision #e3e2bbe](https://github.com/MariaDB/server/commit/e3e2bbe)\
  2015-09-14 10:58:38 +0200
  * [MDEV-6284](https://jira.mariadb.org/browse/MDEV-6284) Merge downstream Debian/Ubuntu packaging into upstream MariaDB
* [Revision #71b1444](https://github.com/MariaDB/server/commit/71b1444)\
  2015-09-14 11:01:14 +0300
  * [MDEV-8768](https://jira.mariadb.org/browse/MDEV-8768): Server crash at file btr0btr.ic line 122 when checking encrypted table using incorrect keys
* [Revision #abd31ca](https://github.com/MariaDB/server/commit/abd31ca)\
  2015-05-06 13:19:22 +0200
  * [MDEV-7990](https://jira.mariadb.org/browse/MDEV-7990): ERROR 1526 when procedure executed for second time ALTER TABLE partition ... pMAX values less than MAXVALUE
* [Revision #d581ef5](https://github.com/MariaDB/server/commit/d581ef5)\
  2015-09-14 08:27:14 +0300
  * [MDEV-8764](https://jira.mariadb.org/browse/MDEV-8764): Wrong error when encrypted table can't be decrypted.
* [Revision #27ec0e1](https://github.com/MariaDB/server/commit/27ec0e1)\
  2015-09-14 03:15:04 +0300
  * Increase the version number
* [Revision #80089a6](https://github.com/MariaDB/server/commit/80089a6)\
  2015-09-14 03:12:54 +0300
  * Follow-up for [MDEV-8675](https://jira.mariadb.org/browse/MDEV-8675) and [MDEV-8676](https://jira.mariadb.org/browse/MDEV-8676)
* [Revision #6cc2e7e](https://github.com/MariaDB/server/commit/6cc2e7e)\
  2015-09-13 23:32:10 +0400
  * [MDEV-8795](https://jira.mariadb.org/browse/MDEV-8795) Equal expression propagation does not work for temporal literals
* [Revision #9b577ed](https://github.com/MariaDB/server/commit/9b577ed)\
  2015-09-12 13:16:05 +0300
  * [MDEV-8577](https://jira.mariadb.org/browse/MDEV-8577): With enforce-storage-engine mysql\_upgrade corrupts the schema: ALTER TABLE should either bypass enforce-storage-engine, or mysql\_upgrade should refuse to run
* [Revision #1e9ab68](https://github.com/MariaDB/server/commit/1e9ab68)\
  2015-09-12 00:44:20 +0200
  * Merge.
* [Revision #39e8dc9](https://github.com/MariaDB/server/commit/39e8dc9)\
  2015-09-12 00:43:31 +0200
  * Merge.
* [Revision #528729f](https://github.com/MariaDB/server/commit/528729f)\
  2015-09-12 00:42:21 +0200
  * [MDEV-8193](https://jira.mariadb.org/browse/MDEV-8193): UNTIL clause in START SLAVE is sporadically disobeyed by parallel replication
* [Revision #96f4a90](https://github.com/MariaDB/server/commit/96f4a90)\
  2015-09-11 23:26:02 +0400
  * [MDEV-8675](https://jira.mariadb.org/browse/MDEV-8675) Different results of GIS functions on NULL vs NOT NULL columns
* [Revision #aaf6334](https://github.com/MariaDB/server/commit/aaf6334)\
  2015-09-11 15:48:34 +0400
  * [MDEV-8709](https://jira.mariadb.org/browse/MDEV-8709) Row equality elements do not get propagated The problem was fixed earlier by one of the [MDEV-8728](https://jira.mariadb.org/browse/MDEV-8728) subtasks. Adding a test case only.
* [Revision #9158212](https://github.com/MariaDB/server/commit/9158212)\
  2015-09-11 15:41:53 +0400
  * [MDEV-8369](https://jira.mariadb.org/browse/MDEV-8369) Unexpected impossible WHERE for a condition on a ZEROFILL field Disable IDENTITY\_SUBST propagation for ZEROFILL columns, as discussed with Sergei.
* [Revision #244f043](https://github.com/MariaDB/server/commit/244f043)\
  2015-09-11 12:03:04 +0200
  * Merge [MDEV-8193](https://jira.mariadb.org/browse/MDEV-8193) into 10.0
* [Revision #df9b8ae](https://github.com/MariaDB/server/commit/df9b8ae)\
  2015-09-11 12:01:48 +0200
  * Merge [MDEV-8193](https://jira.mariadb.org/browse/MDEV-8193) into 10.1
* [Revision #51eaa7f](https://github.com/MariaDB/server/commit/51eaa7f)\
  2015-09-11 10:51:56 +0200
  * [MDEV-8193](https://jira.mariadb.org/browse/MDEV-8193): UNTIL clause in START SLAVE is sporadically disobeyed by parallel replication
* [Revision #6f302d9](https://github.com/MariaDB/server/commit/6f302d9)\
  2015-09-11 11:35:15 +0400
  * [MDEV-8755](https://jira.mariadb.org/browse/MDEV-8755) Equal field propagation is not performed any longer for the IN list when multiple comparison types
* [Revision #0302efc](https://github.com/MariaDB/server/commit/0302efc)\
  2015-09-11 09:20:40 +0400
  * [MDEV-8705](https://jira.mariadb.org/browse/MDEV-8705) Wrong result for SELECT..WHERE latin1\_bin\_column='a' AND latin1\_bin\_column='A' [MDEV-8712](https://jira.mariadb.org/browse/MDEV-8712) Wrong result for SELECT..WHERE latin1\_bin\_column=\_latin1'a' AND latin1\_bin\_column='A'
* [Revision #4aebba3](https://github.com/MariaDB/server/commit/4aebba3)\
  2015-09-10 17:13:35 +0400
  * [MDEV-8740](https://jira.mariadb.org/browse/MDEV-8740) Wrong result for SELECT..WHERE year\_field=10 AND NULLIF(year\_field,2011.1)='2011' [MDEV-8754](https://jira.mariadb.org/browse/MDEV-8754) Wrong result for SELECT..WHERE year\_field=2020 AND NULLIF(year\_field,2010)='2020' Problems: 1. Item\_func\_nullif stored a copy of args\[0] in a private member m\_args0\_copy, which was invisible for the inherited Item\_func menthods, like update\_used\_tables(). As a result, after equal field propagation things like Item\_func\_nullif::const\_item() could return wrong result and a non-constant NULLIF() was erroneously treated as a constant at optimize\_cond() time. Solution: removing m\_args0\_copy and storing the return value item in args\[2] instead. 2. Equal field propagation did not work well for Item\_fun\_nullif. Solution: using ANY\_SUBST for args\[0] and args\[1], as they are in comparison, and IDENTITY\_SUBST for args\[2], as it's not in comparison.
* [Revision #8e553c4](https://github.com/MariaDB/server/commit/8e553c4)\
  2015-09-10 15:01:44 +0400
  * [MDEV-8785](https://jira.mariadb.org/browse/MDEV-8785) Wrong results for EXPLAIN EXTENDED...WHERE NULLIF(latin1\_col, \_utf8'a' COLLATE utf8\_bin) IS NOT NULL
* [Revision #4278d6d](https://github.com/MariaDB/server/commit/4278d6d)\
  2015-09-10 14:04:52 +0400
  * [MDEV-8786](https://jira.mariadb.org/browse/MDEV-8786) Wrong result for SELECT FORMAT=JSON \* FROM t1 WHERE a=\_latin1 0xDF
* [Revision #416b811](https://github.com/MariaDB/server/commit/416b811)\
  2015-09-08 21:56:25 +0200
  * [MDEV-8775](https://jira.mariadb.org/browse/MDEV-8775) enabling encryption is too error-prone
* [Revision #7bd2f20](https://github.com/MariaDB/server/commit/7bd2f20)\
  2015-09-08 17:07:34 +0200
  * make encrypt-binlog and encrypt-tmp-files to fail if no encryption
* [Revision #39b46ae](https://github.com/MariaDB/server/commit/39b46ae)\
  2015-09-09 15:39:09 +0400
  * [MDEV-8706](https://jira.mariadb.org/browse/MDEV-8706) Wrong result for SELECT..WHERE time\_column=TIMESTAMP'2015-08-30 00:00:00' AND time\_column='00:00:00'
* [Revision #3fcd84c](https://github.com/MariaDB/server/commit/3fcd84c)\
  2015-09-09 08:11:43 +0400
  * [MDEV-8741](https://jira.mariadb.org/browse/MDEV-8741) Equal field propagation leaves some remainders after simplifying WH ERE zerofill\_column=2010 AND zerofill\_column>=2010
* [Revision #f8754d6](https://github.com/MariaDB/server/commit/f8754d6)\
  2015-09-07 22:21:35 +0300
  * Merge branch '10.1' of [server](https://github.com/MariaDB/server) into ok-debpkg-10.1
* [Revision #29ac245](https://github.com/MariaDB/server/commit/29ac245)\
  2015-09-07 13:13:52 +0200
  * [MDEV-8473](https://jira.mariadb.org/browse/MDEV-8473): mysqlbinlog -v does not properly decode DECIMAL values in an RBR log
* [Revision #0ce0b88](https://github.com/MariaDB/server/commit/0ce0b88)\
  2015-09-01 11:47:06 +0200
  * [MDEV-8450](https://jira.mariadb.org/browse/MDEV-8450): PATCH] Wrong macro expansion in Query\_cache::send\_result\_to\_client()
* [Revision #d6c5e7e](https://github.com/MariaDB/server/commit/d6c5e7e)\
  2015-09-05 21:28:14 +0300
  * Merge branch '10.1' of [server](https://github.com/MariaDB/server) into ok-debpkg-10.1
* [Revision #102a85f](https://github.com/MariaDB/server/commit/102a85f)\
  2015-09-03 18:00:43 +0200
  * [MDEV-8663](https://jira.mariadb.org/browse/MDEV-8663): IF Statement returns multiple values erroneously (or Assertion \`!null\_value' failed in Item::send(Protocol\*, String\*))
* [Revision #9abf426](https://github.com/MariaDB/server/commit/9abf426)\
  2015-09-04 13:35:31 +0300
  * [MDEV-8443](https://jira.mariadb.org/browse/MDEV-8443): mysql-test - innodb.innodb\_simulate\_comp\_failures 'innodb\_plugin' is failing
* [Revision #b9fee60](https://github.com/MariaDB/server/commit/b9fee60)\
  2015-09-03 19:09:08 +0300
  * Revert "Make galera-3 a Recommends instead of Depends in Debian packaging"
* [Revision #bd8ffe7](https://github.com/MariaDB/server/commit/bd8ffe7)\
  2015-09-03 09:39:57 +0200
  * Merge pull request #87 from pivanof/qplan\_macros
* [Revision #9624b08](https://github.com/MariaDB/server/commit/9624b08)\
  2015-09-02 14:47:44 +0300
  * Merge branch '10.1' of [server](https://github.com/MariaDB/server) into ok-debpkg-10.1
* [Revision #83c7b1e](https://github.com/MariaDB/server/commit/83c7b1e)\
  2015-09-02 10:40:34 +0200
  * Merge [MDEV-8725](https://jira.mariadb.org/browse/MDEV-8725) into 10.0
* [Revision #c104e90](https://github.com/MariaDB/server/commit/c104e90)\
  2015-09-02 04:26:50 +0300
  * Unify virtual-\* package definitions with official Debian packaging
* [Revision #7b344bf](https://github.com/MariaDB/server/commit/7b344bf)\
  2015-09-01 23:06:12 +0300
  * Add [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) stanzas next to [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) in debian/control file
* [Revision #cc08c13](https://github.com/MariaDB/server/commit/cc08c13)\
  2015-09-01 23:01:43 +0300
  * Add MySQL 5.6 stanzas next to MySQL 5.5 in debian/control file
* [Revision #bd3864e](https://github.com/MariaDB/server/commit/bd3864e)\
  2015-09-01 13:50:04 +0300
  * Merge branch '10.1' of [server](https://github.com/MariaDB/server) into ok-debpkg-10.1
* [Revision #b007dfb](https://github.com/MariaDB/server/commit/b007dfb)\
  2015-08-31 09:18:30 +0300
  * Typofix: preceeding -> preceding
* [Revision #e87e26a](https://github.com/MariaDB/server/commit/e87e26a)\
  2015-08-31 09:07:09 +0300
  * Merge branch '10.1' of [server](https://github.com/MariaDB/server) into ok-debpkg
* [Revision #6bd94cf](https://github.com/MariaDB/server/commit/6bd94cf)\
  2015-08-30 22:59:27 +0300
  * Make galera-3 a Recommends instead of Depends in Debian packaging
* [Revision #a273f01](https://github.com/MariaDB/server/commit/a273f01)\
  2015-08-12 23:03:45 +0200
  * Fix spelling errors
* [Revision #f425c71](https://github.com/MariaDB/server/commit/f425c71)\
  2015-07-22 13:53:28 +0300
  * Merge documentation parts in debian/control from downstream
* [Revision #5a3d752](https://github.com/MariaDB/server/commit/5a3d752)\
  2015-07-22 13:45:43 +0300
  * Make autobake-deb.sh to omit .git directory from source tar.gz
* [Revision #220b4f2](https://github.com/MariaDB/server/commit/220b4f2)\
  2015-07-22 13:15:36 +0300
  * Merge (most) build dependencies in debian/control with downstream
* [Revision #16be184](https://github.com/MariaDB/server/commit/16be184)\
  2015-07-22 10:43:55 +0300
  * Extend debian/control build dependencies to max
* [Revision #61e31aa](https://github.com/MariaDB/server/commit/61e31aa)\
  2015-07-22 00:24:29 +0300
  * Remove files from debian/\* that are unrelevant for this upstream repo
* [Revision #6809fdb](https://github.com/MariaDB/server/commit/6809fdb)\
  2015-07-21 23:37:05 +0300
  * Update autobake.sh to match control file location. Drop lucid and squeeze support.
* [Revision #af9509d](https://github.com/MariaDB/server/commit/af9509d)\
  2015-07-21 23:24:05 +0300
  * debian/\*: wrap and sort for cleaner diffs
* [Revision #82e64fd](https://github.com/MariaDB/server/commit/82e64fd)\
  2015-07-21 23:13:05 +0300
  * Remove debian/dist/\* and have just one version
* [Revision #203f4d4](https://github.com/MariaDB/server/commit/203f4d4)\
  2015-07-16 15:59:55 -0700
  * Add parenthesis in macro definitions to prevent order of operation problems.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
