# MariaDB 10.0.20 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.20)[Release Notes](../../old-releases/10.0/10.0.20.md)[Changelog](mariadb-10020-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 18 Jun 2015

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.20.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #a6087e7](https://github.com/MariaDB/server/commit/a6087e7)\
  2015-06-17 16:13:02 +0200
  * [MDEV-5309](https://jira.mariadb.org/browse/MDEV-5309) - RENAME TABLE does not check for existence of the table's engine
* [Revision #5a4c5fa](https://github.com/MariaDB/server/commit/5a4c5fa)\
  2015-06-17 14:18:16 +0200
  * [MDEV-5977](https://jira.mariadb.org/browse/MDEV-5977) [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) is not installable on Trusty when "trusty-updates universe" is in sources.list
* [Revision #b56ad49](https://github.com/MariaDB/server/commit/b56ad49)\
  2015-06-16 17:27:53 +0200
  * [MDEV-8287](https://jira.mariadb.org/browse/MDEV-8287) DROP TABLE suppresses all engine errors
* [Revision #66fd45a](https://github.com/MariaDB/server/commit/66fd45a)\
  2015-06-08 21:06:56 +0200
  * [MDEV-7398](https://jira.mariadb.org/browse/MDEV-7398) mysqld segfaults on FreeBSD 10.1 i386 when built with clang 3.4
* [Revision #7bfda27](https://github.com/MariaDB/server/commit/7bfda27)\
  2015-06-16 23:46:22 +0200
  * [MDEV-8128](https://jira.mariadb.org/browse/MDEV-8128) cmake fails to detect boost libraries
* [Revision #26b0cf4](https://github.com/MariaDB/server/commit/26b0cf4)\
  2015-06-16 21:18:59 +0200
  * [MDEV-8183](https://jira.mariadb.org/browse/MDEV-8183) Adding option mysqldump --no-data-med
* [Revision #569d2f8](https://github.com/MariaDB/server/commit/569d2f8)\
  2015-06-16 23:57:49 +0200
  * Merge branch 'connect-10.0' into 10.0
* [Revision #985e430](https://github.com/MariaDB/server/commit/985e430)\
  2015-06-16 23:55:56 +0200
  * after-merge fixes
* [Revision #27f0bd7](https://github.com/MariaDB/server/commit/27f0bd7)\
  2015-06-16 17:33:21 +0300
  * Fix test case innodb.xa\_recovery crash on xtradb.
* [Revision #9680602](https://github.com/MariaDB/server/commit/9680602)\
  2015-06-16 16:20:55 +0300
  * Fix test failure on main.partition\_innodb.
* [Revision #ababe04](https://github.com/MariaDB/server/commit/ababe04)\
  2015-06-16 15:16:53 +0300
  * Fix crash on test innodb.innodb-virtual-columns. We should create only columns really stored to database.
* [Revision #b83855a](https://github.com/MariaDB/server/commit/b83855a)\
  2015-06-16 14:55:21 +0300
  * Fix innochecksum build failure.
* [Revision #5355972](https://github.com/MariaDB/server/commit/5355972)\
  2015-06-16 12:49:00 +0200
  * after merge fixes: InnoDB and XtraDB
* [Revision #ede0880](https://github.com/MariaDB/server/commit/ede0880)\
  2015-06-16 12:47:58 +0200
  * Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #9859d36](https://github.com/MariaDB/server/commit/9859d36)\
  2015-06-16 12:46:14 +0200
  * Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #a65162a](https://github.com/MariaDB/server/commit/a65162a)\
  2015-06-16 11:08:23 +0200
  * Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #9084945](https://github.com/MariaDB/server/commit/9084945)\
  2015-06-16 11:04:40 +0200
  * 5.6.24-72.2
* [Revision #3c37249](https://github.com/MariaDB/server/commit/3c37249)\
  2015-06-16 11:00:33 +0200
  * 5.6.25
* [Revision #139ba26](https://github.com/MariaDB/server/commit/139ba26)\
  2015-06-16 10:57:05 +0200
  * 5.6.25
* [Revision #909f760](https://github.com/MariaDB/server/commit/909f760)\
  2015-06-15 15:37:14 +0400
  * [MDEV-5309](https://jira.mariadb.org/browse/MDEV-5309) - RENAME TABLE does not check for existence of the table's engine
* [Revision #b988553](https://github.com/MariaDB/server/commit/b988553)\
  2015-06-15 15:42:14 +0200
  * [MDEV-7771](https://jira.mariadb.org/browse/MDEV-7771) missing client plugins when mariadb-shared is not installed
* [Revision #02421aa](https://github.com/MariaDB/server/commit/02421aa)\
  2015-06-15 18:07:41 +0500
  * [MDEV-7871](https://jira.mariadb.org/browse/MDEV-7871) Tests fail massively on "Assertion \`status\_var.memory\_used == 0'" when run with --ps --embedded. As the MF\_THREAD\_SPECIFIC was introduced to the alloc\_root's and the prealloc added to the statement::mem\_root and statement::result.alloc, we have to adjust the embedded server to it. The preallocation was removed for the embedded server as it makes no sence for it. The msyqltest should free the statement inside the proper thead to make the memory statistics happy.
* [Revision #a117030](https://github.com/MariaDB/server/commit/a117030)\
  2015-06-14 18:46:02 +0200
  * [MDEV-8131](https://jira.mariadb.org/browse/MDEV-8131) MariaDB does not build on hurd-i386: plugin/auth\_dialog/dialog.c:172:20: error: 'RTLD\_DEFAULT' undeclared
* [Revision #3288f26](https://github.com/MariaDB/server/commit/3288f26)\
  2015-06-14 20:19:05 +0200
  * include the correct IPv6 check in perfschema tests
* [Revision #2a0f086](https://github.com/MariaDB/server/commit/2a0f086)\
  2015-06-14 17:38:30 +0200
  * don't scream when auto-selected IPv6 is not available
* [Revision #a453a28](https://github.com/MariaDB/server/commit/a453a28)\
  2015-06-14 17:34:08 +0200
  * [MDEV-8083](https://jira.mariadb.org/browse/MDEV-8083) MTR is broken on systems with IPv6 disabled
* [Revision #aad8667](https://github.com/MariaDB/server/commit/aad8667)\
  2015-06-15 11:11:42 +0400
  * Committing a change into r/type\_time\_hires.result forgotten in the previous commit for [MDEV-8205](https://jira.mariadb.org/browse/MDEV-8205).
* [Revision #43e4522](https://github.com/MariaDB/server/commit/43e4522)\
  2015-06-15 11:04:06 +0400
  * [MDEV-8205](https://jira.mariadb.org/browse/MDEV-8205) timediff returns null when comparing decimal time to time string value
* [Revision #f69f3db](https://github.com/MariaDB/server/commit/f69f3db)\
  2015-06-15 08:25:09 +0200
  * Merge branch 'mdev8294' into 10.0
* [Revision #4c251af](https://github.com/MariaDB/server/commit/4c251af)\
  2015-06-15 08:23:26 +0200
  * [MDEV-8316](https://jira.mariadb.org/browse/MDEV-8316): debugger aborting because missing DBUG\_RETURN or DBUG\_VOID\_RETURN macro in function "any\_slave\_sql\_running"
* [Revision #93c039d](https://github.com/MariaDB/server/commit/93c039d)\
  2015-06-15 08:13:40 +0200
  * [MDEV-8294](https://jira.mariadb.org/browse/MDEV-8294): Inconsistent behavior of slave parallel threads at runtime
* [Revision #196528e](https://github.com/MariaDB/server/commit/196528e)\
  2015-06-14 18:54:13 +0500
  * [MDEV-8212](https://jira.mariadb.org/browse/MDEV-8212) alter table - failing to ADD PRIMARY KEY IF NOT EXISTS when existing index of same as column name. The default name for the primary key is rather 'PRIMARY' instead of the indexed column name.
* [Revision #fc31e31](https://github.com/MariaDB/server/commit/fc31e31)\
  2015-06-14 17:29:58 +0300
  * [MDEV-8179](https://jira.mariadb.org/browse/MDEV-8179): Absent progress report for operations on InnoDB tables
* [Revision #36bf482](https://github.com/MariaDB/server/commit/36bf482)\
  2015-06-14 15:51:34 +0200
  * [MDEV-8285](https://jira.mariadb.org/browse/MDEV-8285) compile fails under Mac OS X 10.6.8 due to use of strnlen
* [Revision #e2879ac](https://github.com/MariaDB/server/commit/e2879ac)\
  2015-06-14 08:14:28 +0300
  * [MDEV-7881](https://jira.mariadb.org/browse/MDEV-7881): InnoDB Logfile size - misleading error message
* [Revision #e85b661](https://github.com/MariaDB/server/commit/e85b661)\
  2015-06-12 08:00:48 +0200
  * Merge branch 'bb-10.0-serg' into 10.0
* [Revision #d437c35](https://github.com/MariaDB/server/commit/d437c35)\
  2015-06-11 22:54:03 +0400
  * Adding a few warning related protected methods in Field and reducing some duplicate code.
* [Revision #b9eb7f1](https://github.com/MariaDB/server/commit/b9eb7f1)\
  2015-06-11 20:20:52 +0200
  * CRLF
* [Revision #6d49d3b](https://github.com/MariaDB/server/commit/6d49d3b)\
  2015-06-11 20:20:45 +0200
  * compiler warnings
* [Revision #810cf36](https://github.com/MariaDB/server/commit/810cf36)\
  2015-06-11 20:20:35 +0200
  * Merge branch '5.5' into 10.0
* [Revision #d199a0f](https://github.com/MariaDB/server/commit/d199a0f)\
  2015-06-11 17:47:52 +0200
  * more renames after tokudb merge
* [Revision #b96c196](https://github.com/MariaDB/server/commit/b96c196)\
  2015-06-11 16:48:10 +0200
  * Item\_cache::safe\_charset\_converter() fixes
* [Revision #7c98e8a](https://github.com/MariaDB/server/commit/7c98e8a)\
  2015-06-11 16:43:56 +0200
  * fix after the tokudb ft-index merge
* [Revision #36f37a4](https://github.com/MariaDB/server/commit/36f37a4)\
  2015-06-10 12:01:06 +0200
  * Merge [MDEV-8294](https://jira.mariadb.org/browse/MDEV-8294) into 10.0
* [Revision #682ed00](https://github.com/MariaDB/server/commit/682ed00)\
  2015-06-10 11:57:42 +0200
  * [MDEV-8294](https://jira.mariadb.org/browse/MDEV-8294): Inconsistent behavior of slave parallel threads at runtime
* [Revision #5a44e1a](https://github.com/MariaDB/server/commit/5a44e1a)\
  2015-06-09 22:11:22 +0200
  * tests for [MDEV-7937](https://jira.mariadb.org/browse/MDEV-7937): Enforce SSL when --ssl client option is used
* [Revision #80f6b22](https://github.com/MariaDB/server/commit/80f6b22)\
  2015-06-09 16:08:09 +0400
  * [MDEV-3870](https://jira.mariadb.org/browse/MDEV-3870) - Valgrind warnings on OPTIMIZE MyISAM or Aria TABLE with disabled keys
* [Revision #3a50a8c](https://github.com/MariaDB/server/commit/3a50a8c)\
  2015-06-09 13:50:43 +0400
  * [MDEV-363](https://jira.mariadb.org/browse/MDEV-363) - Server crashes in intern\_plugin\_lock on concurrent installing semisync plugin and setting rpl\_semi\_sync\_master\_enabled
* [Revision #49a3392](https://github.com/MariaDB/server/commit/49a3392)\
  2015-06-09 11:57:31 +0400
  * [MDEV-363](https://jira.mariadb.org/browse/MDEV-363) - Server crashes in intern\_plugin\_lock on concurrent installing semisync plugin and setting rpl\_semi\_sync\_master\_enabled
* [Revision #e5005ce](https://github.com/MariaDB/server/commit/e5005ce)\
  2015-06-09 18:06:41 +0200
  * disable ssl for ssl-disabled tests
* [Revision #992d782](https://github.com/MariaDB/server/commit/992d782)\
  2015-06-09 18:56:09 +0300
  * [MDEV-6735](https://jira.mariadb.org/browse/MDEV-6735): Range checked for each record used with key (also [MDEV-7786](https://jira.mariadb.org/browse/MDEV-7786), [MDEV-7923](https://jira.mariadb.org/browse/MDEV-7923))
* [Revision #5d57e2d](https://github.com/MariaDB/server/commit/5d57e2d)\
  2015-06-09 16:46:45 +0300
  * Fix tests for 7937
* [Revision #be5035b](https://github.com/MariaDB/server/commit/be5035b)\
  2015-06-09 15:59:29 +0300
  * Added tests for [MDEV-7937](https://jira.mariadb.org/browse/MDEV-7937)
* [Revision #4ef7497](https://github.com/MariaDB/server/commit/4ef7497)\
  2015-06-09 14:08:44 +0300
  * [MDEV-7937](https://jira.mariadb.org/browse/MDEV-7937): Enforce SSL when --ssl client option is used
* [Revision #56e2d83](https://github.com/MariaDB/server/commit/56e2d83)\
  2015-05-02 08:45:10 +0200
  * [MDEV-7695](https://jira.mariadb.org/browse/MDEV-7695) MariaDB - ssl - fips: can not connect with --ssl-cipher=DHE-RSA-AES256-SHA - handshake failure
* [Revision #92b3659](https://github.com/MariaDB/server/commit/92b3659)\
  2015-06-09 12:05:06 +0400
  * [MDEV-7268](https://jira.mariadb.org/browse/MDEV-7268) Column of table cannot be converted from type 'decimal(0,?)' to type ' 'decimal(10,7)' Changing the error message to: "...from type 'decimal(0,?)/_old_/' to type ' 'decimal(10,7)'..." So it's now clear that the master data type is OLD decimal.
* [Revision #b1e1039](https://github.com/MariaDB/server/commit/b1e1039)\
  2015-06-09 07:36:24 +0400
  * [MDEV-8286](https://jira.mariadb.org/browse/MDEV-8286) Likely a redundant declaration of Item\_cache::used\_table\_map
* [Revision #a4d93e0](https://github.com/MariaDB/server/commit/a4d93e0)\
  2015-06-05 20:05:08 +0200
  * [MDEV-8050](https://jira.mariadb.org/browse/MDEV-8050) sphinx test cases cannot run with sphinxsearch-2.2.6
* [Revision #b41ad55](https://github.com/MariaDB/server/commit/b41ad55)\
  2015-06-08 15:09:20 +0200
  * update tokudb version
* [Revision #1707cfc](https://github.com/MariaDB/server/commit/1707cfc)\
  2015-06-08 21:55:52 +0500
  * [MDEV-8211](https://jira.mariadb.org/browse/MDEV-8211) plugins.server\_audit fails sporadically in buildbot. More fixes to assure the order of queries in the log.
* [Revision #87088b9](https://github.com/MariaDB/server/commit/87088b9)\
  2015-06-08 21:44:13 +0500
  * [MDEV-8211](https://jira.mariadb.org/browse/MDEV-8211) plugins.server\_audit fails sporadically in buildbot. This test also should be fixed - delay added so the connection event doesn't happen before the query.
* [Revision #96b3703](https://github.com/MariaDB/server/commit/96b3703)\
  2015-06-08 21:40:17 +0500
  * [MDEV-8211](https://jira.mariadb.org/browse/MDEV-8211) plugins.server\_audit fails sporadically in buildbot. Connection event can happen before the query ends. Added a delay to confirm the order.
* [Revision #a765cca](https://github.com/MariaDB/server/commit/a765cca)\
  2015-06-08 20:50:40 +0400
  * [MDEV-8067](https://jira.mariadb.org/browse/MDEV-8067) correct fix for MySQL Bug

## 19699237: UNINITIALIZED VARIABLE IN ITEM\_FIELD::STR\_RESULT

* [Revision #b37b52a](https://github.com/MariaDB/server/commit/b37b52a)\
  2015-06-08 13:47:07 +0500
  * [MDEV-4922](https://jira.mariadb.org/browse/MDEV-4922) Stored Procedure - Geometry parameter not working. Fhe GEOMETRY field should be handled just as the BLOB field. So that was fiexed in field\_conv. One additional bug was found and fixed meanwhile - thet the geometry field subtypes should also be merged for UNION command.
* [Revision #69ed429](https://github.com/MariaDB/server/commit/69ed429)\
  2015-06-08 12:09:13 +0500
  * [MDEV-7500](https://jira.mariadb.org/browse/MDEV-7500) thread\_handling option in my.cnf is not passing "connect events" to audit plugin. The MYSQL\_AUDIT\_NOTIFY\_CONNECTION\_CONNECT() call moved to the login\_connection() function. So that it'll be invoked in any thread handling mode.
* [Revision #1ae05db](https://github.com/MariaDB/server/commit/1ae05db)\
  2015-06-07 15:40:42 +0500
  * [MDEV-8078](https://jira.mariadb.org/browse/MDEV-8078) Memory disclosure/buffer overread on audit plugin. If the SET PASSWORD query doesn't have the password string, the parsing of it can fail. It manifested first in MySQL 5.6 as it started to hide password lines sent to the plugins. Fixed by checking for that case.
* [Revision #db0ecf2](https://github.com/MariaDB/server/commit/db0ecf2)\
  2015-06-06 19:12:44 +0500
  * [MDEV-8032](https://jira.mariadb.org/browse/MDEV-8032) \[PATCH] audit plugin - csv output broken. Symbols like TAB or NEWLINE should be escaped, which was forgotten in one place.
* [Revision #6264451](https://github.com/MariaDB/server/commit/6264451)\
  2015-06-06 16:13:51 +0200
  * [MDEV-8114](https://jira.mariadb.org/browse/MDEV-8114): server crash on updates with joins still on 10.0.18
* [Revision #1443227](https://github.com/MariaDB/server/commit/1443227)\
  2015-06-05 16:20:40 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #4728b51](https://github.com/MariaDB/server/commit/4728b51)\
  2015-06-05 16:20:23 +0200
  * Commit win packaging & upgrade\_wizard files
* [Revision #88998cf](https://github.com/MariaDB/server/commit/88998cf)\
  2015-06-05 16:10:50 +0200
  * Commit merge resolved files
* [Revision #a8b7b6c](https://github.com/MariaDB/server/commit/a8b7b6c)\
  2015-06-05 10:59:15 +0200
  * Commit merge resolved files
* [Revision #9a3b975](https://github.com/MariaDB/server/commit/9a3b975)\
  2015-06-05 09:51:17 +0200
  * Merge branch '5.5' into bb-5.5-serg
* [Revision #a2bb9d2](https://github.com/MariaDB/server/commit/a2bb9d2)\
  2015-06-04 16:04:05 +0400
  * [MDEV-7505](https://jira.mariadb.org/browse/MDEV-7505) - Too large scale in DECIMAL dynamic column getter crashes mysqld
* [Revision #b611ac0](https://github.com/MariaDB/server/commit/b611ac0)\
  2015-06-03 14:30:09 +0400
  * [MDEV-6236](https://jira.mariadb.org/browse/MDEV-6236) - \[PATCH] mysql\_tzinfo\_to\_sql may produce invalid SQL
* [Revision #af2256f](https://github.com/MariaDB/server/commit/af2256f)\
  2015-06-03 13:59:58 +0400
  * [MDEV-7207](https://jira.mariadb.org/browse/MDEV-7207) - ALTER VIEW does not change ALGORITM
* [Revision #ae0c576](https://github.com/MariaDB/server/commit/ae0c576)\
  2015-06-05 02:14:49 +0200
  * Merge branch 'merge/merge-xtradb-5.5' into bb-5.5-serg
* [Revision #f84f577](https://github.com/MariaDB/server/commit/f84f577)\
  2015-06-05 02:06:51 +0200
  * Merge tag 'mysql-5.5.44' into bb-5.5-serg
* [Revision #f07b346](https://github.com/MariaDB/server/commit/f07b346)\
  2015-06-05 02:04:32 +0200
  * do not re-populate I\_S tables in subqueries
* [Revision #1ff423d](https://github.com/MariaDB/server/commit/1ff423d)\
  2015-06-04 21:12:29 +0400
  * [MDEV-8243](https://jira.mariadb.org/browse/MDEV-8243) configure defines to empty string, not 1
* [Revision #750aa8b](https://github.com/MariaDB/server/commit/750aa8b)\
  2015-06-04 18:58:12 +0200
  * 5.5.43-37.2
* [Revision #980bdc3](https://github.com/MariaDB/server/commit/980bdc3)\
  2015-06-04 17:39:05 +0200
  * followup: CREATE SERVER tests should not be run for embedded
* [Revision #a477cd1](https://github.com/MariaDB/server/commit/a477cd1)\
  2015-06-03 23:31:05 +0300
  * [MDEV-6500](https://jira.mariadb.org/browse/MDEV-6500): Stale data returned after TRUNCATE PARTITION operation
* [Revision #08fa02c](https://github.com/MariaDB/server/commit/08fa02c)\
  2015-06-04 18:51:30 +0400
  * Some MYD files (e.g. in mysql-test/std\_data) could erroneously be treated by git as text files.
* [Revision #9da8a8f](https://github.com/MariaDB/server/commit/9da8a8f)\
  2015-06-04 18:49:12 +0400
  * [MDEV-7269](https://jira.mariadb.org/browse/MDEV-7269) mysqlbinlog Don't know how to handle column type=0 meta=0 (0000)

## [MDEV-8267](https://jira.mariadb.org/browse/MDEV-8267) Add /_old_/ comment into I\_S.COLUMN\_TYPE for old DECIMAL

* [Revision #a8b8544](https://github.com/MariaDB/server/commit/a8b8544)\
  2015-06-04 13:00:53 +0300
  * [MDEV-7906](https://jira.mariadb.org/browse/MDEV-7906): InnoDB: Failing assertion: prebuilt->sql\_stat\_start || trx->state == 1 on concurrent multi-table update
* [Revision #7b05650](https://github.com/MariaDB/server/commit/7b05650)\
  2015-06-03 20:24:51 +0200
  * Merge tag 'tokudb-engine/tokudb-7.5.7' into 5.5
* [Revision #e500c47](https://github.com/MariaDB/server/commit/e500c47)\
  2015-06-03 19:47:46 +0200
  * Merge tag 'tokudb-ft-index/tokudb-7.5.7' into 5.5
* [Revision #934a18d](https://github.com/MariaDB/server/commit/934a18d)\
  2015-06-03 19:42:34 +0200
  * .gitattributes: \*.dat files should not be CRLF converted
* [Revision #c79e98e](https://github.com/MariaDB/server/commit/c79e98e)\
  2015-06-03 18:45:08 +0200
  * [MDEV-8085](https://jira.mariadb.org/browse/MDEV-8085) main.group\_by failed in buildbot
* [Revision #0599d80](https://github.com/MariaDB/server/commit/0599d80)\
  2015-06-03 17:37:51 +0200
  * Fix swapping key numeric values on Big Endian machines. Fix typo error in CntIndexRange (kp instead of p) Change version date
* [Revision #5d8cee4](https://github.com/MariaDB/server/commit/5d8cee4)\
  2015-06-03 17:11:07 +0200
  * [MDEV-8224](https://jira.mariadb.org/browse/MDEV-8224) Server crashes in get\_server\_from\_table\_to\_cache on empty name
* [Revision #33d480f](https://github.com/MariaDB/server/commit/33d480f)\
  2015-06-03 16:33:10 +0200
  * [MDEV-4608](https://jira.mariadb.org/browse/MDEV-4608) deb packages for jessie
* [Revision #f806b4d](https://github.com/MariaDB/server/commit/f806b4d)\
  2015-06-03 12:13:43 +0200
  * [MDEV-8124](https://jira.mariadb.org/browse/MDEV-8124) mysqlcheck: --auto-repair runs REPAIR TABLE instead of REPAIR VIEW on views
* [Revision #535b514](https://github.com/MariaDB/server/commit/535b514)\
  2015-06-03 10:35:34 +0200
  * [MDEV-8123](https://jira.mariadb.org/browse/MDEV-8123) mysqlcheck: new --process-views option conflicts with --quick, --extended and such
* [Revision #64569fa](https://github.com/MariaDB/server/commit/64569fa)\
  2015-06-03 11:11:53 +0200
  * parser: better error messages for CHECK/REPAIR VIEW
* [Revision #4821cd9](https://github.com/MariaDB/server/commit/4821cd9)\
  2015-06-03 11:38:34 +0200
  * Fix swapping key numeric values on Big Endian machines. Fix typo error in CntIndexRange for big endian swapping
* [Revision #37a803c](https://github.com/MariaDB/server/commit/37a803c)\
  2015-06-03 11:31:18 +0200
  * Fix swapping key numeric values on Big Endian machines. Swap the key length when WORDS\_BIGENDIAN is defined Make the IOFF structure depending on WORDS\_BIGENDIAN
* [Revision #65ed254](https://github.com/MariaDB/server/commit/65ed254)\
  2015-06-03 10:07:33 +0200
  * Fix swapping key numeric values on Big Endian machines. Change the preprocessor variable used from BIG\_ENDIAN\_ORDER (only used by taoscript) to WORDS\_BIGENDIAN.
* [Revision #0ffef5d](https://github.com/MariaDB/server/commit/0ffef5d)\
  2015-06-03 09:54:56 +0200
  * [MDEV-8052](https://jira.mariadb.org/browse/MDEV-8052) abi detection incorrect with clang
* [Revision #70d8030](https://github.com/MariaDB/server/commit/70d8030)\
  2015-06-03 02:02:21 +0200
  * Fix swapping key numeric values on Big Endian machines.
* [Revision #8e7d665](https://github.com/MariaDB/server/commit/8e7d665)\
  2015-06-02 22:07:47 +0200
  * CRLF->LF
* [Revision #af26c36](https://github.com/MariaDB/server/commit/af26c36)\
  2015-06-02 12:28:42 +0200
  * Fix handling of NULL values when reading from tables.
* [Revision #514a7d8](https://github.com/MariaDB/server/commit/514a7d8)\
  2015-05-30 10:59:34 +0200
  * Add unicode ODBC types to the types recognized by CONNECT. Was added in function TranslateSQLType.
* [Revision #b6a5637](https://github.com/MariaDB/server/commit/b6a5637)\
  2015-05-27 16:23:38 +0200
  * Change all preprocessor compiler directives to use WIN as the mean of specifying Windows or not Windows compile. This is what MariaDB does.
* [Revision #6bd76f8](https://github.com/MariaDB/server/commit/6bd76f8)\
  2015-05-27 10:27:18 +0400
  * Merge pull request #73 from akopytov/[MDEV-7658](https://jira.mariadb.org/browse/MDEV-7658)-5.5
* [Revision #a99efc0](https://github.com/MariaDB/server/commit/a99efc0)\
  2015-05-27 09:16:24 +0300
  * Merge pull request #74 from akopytov/[MDEV-7658](https://jira.mariadb.org/browse/MDEV-7658)-10.0
* [Revision #7f7cee8](https://github.com/MariaDB/server/commit/7f7cee8)\
  2015-05-26 23:58:51 +0300
  * Merge branch '[MDEV-7658](https://jira.mariadb.org/browse/MDEV-7658)-5.5' into [MDEV-7658](https://jira.mariadb.org/browse/MDEV-7658)-10.0
* [Revision #70bc0a3](https://github.com/MariaDB/server/commit/70bc0a3)\
  2015-05-26 23:56:00 +0300
  * Fixes [MDEV-7658](https://jira.mariadb.org/browse/MDEV-7658): [MDEV-7026](https://jira.mariadb.org/browse/MDEV-7026) fix reintroduces [MDEV-6615](https://jira.mariadb.org/browse/MDEV-6615) on AArch64
* [Revision #f738598](https://github.com/MariaDB/server/commit/f738598)\
  2015-05-26 13:15:57 +0200
  * Merge [MDEV-8147](https://jira.mariadb.org/browse/MDEV-8147) into 10.0
* [Revision #e5f1e84](https://github.com/MariaDB/server/commit/e5f1e84)\
  2015-05-26 12:47:35 +0200
  * [MDEV-8147](https://jira.mariadb.org/browse/MDEV-8147): Assertion \`m\_lock\_type == 2' failed in handler::ha\_close() during parallel replication
* [Revision #fb98632](https://github.com/MariaDB/server/commit/fb98632)\
  2015-05-26 01:02:33 +0200
  * JSONColumns and XMLColumns revisited. They can retrieve their parameters directly from the PTOS argument. For this to work, finding the table options is now split in HA\_CONNECT functions and exported functions available from out of ha\_connect.
* [Revision #37840d5](https://github.com/MariaDB/server/commit/37840d5)\
  2015-05-20 11:19:44 +0200
  * Security: EOM modules must now be loaded from the plugin directory.
* [Revision #db33294](https://github.com/MariaDB/server/commit/db33294)\
  2015-05-17 19:55:48 +0200
  * Json array index (position) was badly set for default array setting
* [Revision #a82171c](https://github.com/MariaDB/server/commit/a82171c)\
  2015-05-17 15:22:42 +0200
  * In BIN table date\_format now imply by default field\_format='C'.
* [Revision #5d02928](https://github.com/MariaDB/server/commit/5d02928)\
  2015-05-16 10:26:34 +0200
  * remove second @ from CONFIGURE\_FILE (... @ONLY@)
* [Revision #b9c9109](https://github.com/MariaDB/server/commit/b9c9109)\
  2015-05-15 11:56:29 +0200
  * Fix a bug in BIN buffer initialisation (in FIXFAM::AllocateBuffer)
* [Revision #46199c0](https://github.com/MariaDB/server/commit/46199c0)\
  2015-05-14 14:43:37 +0400
  * [MDEV-8102](https://jira.mariadb.org/browse/MDEV-8102) REGEXP function fails to match hex values when expression is stored as a variable We don't fix the bug itself, we just make regex functions display errors returned from pcre\_exec() as MariaDB warnings.
* [Revision #e6b60ee](https://github.com/MariaDB/server/commit/e6b60ee)\
  2015-05-13 19:58:21 +0200
  * Make BIN table files more flexible with new column format. In particular enable to set length and endian setting. This should solve all problems on IBM390s machines.
* [Revision #0b4231e](https://github.com/MariaDB/server/commit/0b4231e)\
  2015-05-13 15:17:19 +0300
  * [MDEV-8154](https://jira.mariadb.org/browse/MDEV-8154) rpl.show\_status\_stop\_slave\_race-7126 sporadically causes internal check failure
* [Revision #6f8558b](https://github.com/MariaDB/server/commit/6f8558b)\
  2015-05-12 14:19:30 -0400
  * Fix for debug build failure
* [Revision #b3d3dd2](https://github.com/MariaDB/server/commit/b3d3dd2)\
  2015-05-12 03:44:10 +0300
  * [MDEV-8144](https://jira.mariadb.org/browse/MDEV-8144) percona.innodb\_sys\_index test fails
* [Revision #f027baf](https://github.com/MariaDB/server/commit/f027baf)\
  2015-05-12 03:43:36 +0300
  * Increase the version number
* [Revision #3810fefc](https://github.com/MariaDB/server/commit/3810fefc)\
  2015-05-10 12:40:30 +0200
  * resolving conflict
* [Revision #445fc77](https://github.com/MariaDB/server/commit/445fc77)\
  2015-05-10 12:14:21 +0200
  * Get rid of more GCC warnings about unused parameters
* [Revision #7c02f74](https://github.com/MariaDB/server/commit/7c02f74)\
  2015-05-10 12:22:43 +0200
  * Get rid of more GCC warnings about unused parameters
* [Revision #3b3f6ca](https://github.com/MariaDB/server/commit/3b3f6ca)\
  2015-05-08 13:21:42 +0200
  * Typo to check buildbot
* [Revision #c63bd86](https://github.com/MariaDB/server/commit/c63bd86)\
  2015-05-10 12:14:21 +0200
  * Get rid of more GCC warnings about unused parameters
* [Revision #f5d0c77](https://github.com/MariaDB/server/commit/f5d0c77)\
  2015-05-09 17:30:20 +0200
  * Get rid of GCC warnings about unused parameters
* [Revision #373d092](https://github.com/MariaDB/server/commit/373d092)\
  2015-05-08 17:19:48 +0300
  * Fix win/ files to be stored with LF in repository
* [Revision #23b2b95](https://github.com/MariaDB/server/commit/23b2b95)\
  2015-05-08 17:19:06 +0300
  * Update .gitattributes
* [Revision #6ef3c7d](https://github.com/MariaDB/server/commit/6ef3c7d)\
  2015-05-08 17:09:45 +0300
  * Updated .gitattributes
* [Revision #6b56e89](https://github.com/MariaDB/server/commit/6b56e89)\
  2015-05-08 13:21:42 +0200
  * Typo to check buildbot
* [Revision #5fa2a6c](https://github.com/MariaDB/server/commit/5fa2a6c)\
  2015-05-07 18:02:31 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #7704fde](https://github.com/MariaDB/server/commit/7704fde)\
  2015-05-07 18:01:49 +0200
  * Heidi stuff
* [Revision #c387e7d](https://github.com/MariaDB/server/commit/c387e7d)\
  2015-05-07 17:36:25 +0200
  * Heidi stuff
* [Revision #3a889b1](https://github.com/MariaDB/server/commit/3a889b1)\
  2015-05-07 16:59:25 +0200
  * Fix a bug in init\_table\_share that caused syntax error with Boolean options: oom|= sql->append(vull ? "ON" : "OFF"); replaced by: oom|= sql->append(vull ? "YES" : "NO");
* [Revision #12bebce](https://github.com/MariaDB/server/commit/12bebce)\
  2015-05-05 11:37:21 +0200\
  \*
  * Fix a regression bug on (XML) HTML tables.
* [Revision #1b07ba5](https://github.com/MariaDB/server/commit/1b07ba5)\
  2015-05-02 15:36:33 +0200
  * Fix [MDEV-8090](https://jira.mariadb.org/browse/MDEV-8090) in tabmysql.cpp

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
