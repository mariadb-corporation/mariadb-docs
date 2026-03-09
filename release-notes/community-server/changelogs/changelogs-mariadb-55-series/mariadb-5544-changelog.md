# MariaDB 5.5.44 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.44)[Release Notes](../../old-releases/5.5/5.5.44.md)[Changelog](mariadb-5544-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 11 Jun 2015

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.44.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

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
* [Revision #0ffef5d](https://github.com/MariaDB/server/commit/0ffef5d)\
  2015-06-03 09:54:56 +0200
  * [MDEV-8052](https://jira.mariadb.org/browse/MDEV-8052) abi detection incorrect with clang
* [Revision #8e7d665](https://github.com/MariaDB/server/commit/8e7d665)\
  2015-06-02 22:07:47 +0200
  * CRLF->LF
* [Revision #6bd76f8](https://github.com/MariaDB/server/commit/6bd76f8)\
  2015-05-27 10:27:18 +0400
  * Merge pull request #73 from akopytov/[MDEV-7658](https://jira.mariadb.org/browse/MDEV-7658)-5.5
* [Revision #70bc0a3](https://github.com/MariaDB/server/commit/70bc0a3)\
  2015-05-26 23:56:00 +0300
  * Fixes [MDEV-7658](https://jira.mariadb.org/browse/MDEV-7658): [MDEV-7026](https://jira.mariadb.org/browse/MDEV-7026) fix reintroduces [MDEV-6615](https://jira.mariadb.org/browse/MDEV-6615) on AArch64
* [Revision #5d02928](https://github.com/MariaDB/server/commit/5d02928)\
  2015-05-16 10:26:34 +0200
  * remove second @ from CONFIGURE\_FILE (... @ONLY@)
* [Revision #6f8558b](https://github.com/MariaDB/server/commit/6f8558b)\
  2015-05-12 14:19:30 -0400
  * Fix for debug build failure
* [Revision #373d092](https://github.com/MariaDB/server/commit/373d092)\
  2015-05-08 17:19:48 +0300
  * Fix win/ files to be stored with LF in repository
* [Revision #23b2b95](https://github.com/MariaDB/server/commit/23b2b95)\
  2015-05-08 17:19:06 +0300
  * Update .gitattributes
* [Revision #6ef3c7d](https://github.com/MariaDB/server/commit/6ef3c7d)\
  2015-05-08 17:09:45 +0300
  * Updated .gitattributes
* [Revision #0014bdc](https://github.com/MariaDB/server/commit/0014bdc)\
  2015-05-07 22:18:34 +0200
  * [MDEV-8115](https://jira.mariadb.org/browse/MDEV-8115) mysql\_upgrade crashes the server with REPAIR VIEW
* [Revision #8350ea0](https://github.com/MariaDB/server/commit/8350ea0)\
  2015-05-07 13:04:03 +0300
  * Fix compiler error if compiler does not support c99 style initializers.
* [Revision #f704b33](https://github.com/MariaDB/server/commit/f704b33)\
  2015-05-06 16:47:23 +0300
  * Merge pull request #52 from openquery/[MDEV-8053](https://jira.mariadb.org/browse/MDEV-8053)-c99-style-for-structure-members
* [Revision #4d606cb](https://github.com/MariaDB/server/commit/4d606cb)\
  2015-04-24 23:17:16 +1000
  * c99 style for assigning structure members

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
