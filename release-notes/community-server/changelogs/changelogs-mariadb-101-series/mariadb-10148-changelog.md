# MariaDB 10.1.48 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.1/10.1.48.md)[Changelog](mariadb-10148-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.1.48/)

**Release date:** 3 Nov 2020

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.48.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #e55bb16b04](https://github.com/MariaDB/server/commit/e55bb16b04)\
  2020-10-30 02:47:21 +0200
  * List of unstable tests for 10.1.48 release
* [Revision #d6302c9a47](https://github.com/MariaDB/server/commit/d6302c9a47)\
  2020-10-28 20:44:03 +0100
  * [MDEV-23702](https://jira.mariadb.org/browse/MDEV-23702) calculating(auto rounding) issue
* [Revision #313cf9de2c](https://github.com/MariaDB/server/commit/313cf9de2c)\
  2020-10-29 01:42:07 +0100
  * update result files after backport
* [Revision #eae10a87ff](https://github.com/MariaDB/server/commit/eae10a87ff)\
  2020-10-29 08:29:03 +0100
  * Move result files at the correct place.
* [Revision #cb04c1bc64](https://github.com/MariaDB/server/commit/cb04c1bc64)\
  2020-10-28 13:35:43 +0100
  * [MDEV-24040](https://jira.mariadb.org/browse/MDEV-24040) - fix appveyor build
* [Revision #3829b408d6](https://github.com/MariaDB/server/commit/3829b408d6)\
  2020-10-27 20:31:16 +0100
  * [MDEV-24040](https://jira.mariadb.org/browse/MDEV-24040) Named pipe permission issue
* [Revision #d03ea82759](https://github.com/MariaDB/server/commit/d03ea82759)\
  2020-10-26 17:21:26 +0100
  * test case for BUG#31650096
* [Revision #a7d5e85c49](https://github.com/MariaDB/server/commit/a7d5e85c49)\
  2020-10-26 17:20:59 +0100
  * cleanup: have\_static\_innodb.inc
* [Revision #1269fd420d](https://github.com/MariaDB/server/commit/1269fd420d)\
  2020-08-31 12:21:07 +0530
  * BUG#31650096: MYSQL SERVER HEAP-USE-AFTER-FREE IN TRANS\_SAVEPOINT
* [Revision #0c3723e1d5](https://github.com/MariaDB/server/commit/0c3723e1d5)\
  2020-10-25 18:17:34 +0100
  * Bug#31304432 "INSUFFICIENT PRIVILEGE CHECK BY LOCK TABLES"
* [Revision #320a73f6a2](https://github.com/MariaDB/server/commit/320a73f6a2)\
  2020-10-25 18:16:24 +0100
  * cleanup: PRIV\_LOCK\_TABLES (10.5 style)
* [Revision #8584349108](https://github.com/MariaDB/server/commit/8584349108)\
  2020-10-23 18:09:01 +0300
  * [MDEV-14945](https://jira.mariadb.org/browse/MDEV-14945) possible buffer overflow in stack resolver
* [Revision #44c958dd7b](https://github.com/MariaDB/server/commit/44c958dd7b)\
  2020-10-24 14:57:16 +0300
  * Fix test failure on wsrep/variables test case.
* [Revision #f679d72679](https://github.com/MariaDB/server/commit/f679d72679)\
  2017-11-30 00:41:43 +0300
  * [MDEV-24017](https://jira.mariadb.org/browse/MDEV-24017): Blackhole : Specified key was too long; max key length is 1000 bytes
* Merge [Revision #06af03677c](https://github.com/MariaDB/server/commit/06af03677c) 2020-10-24 10:08:07 +0200 - Merge remote-tracking branch 'connect/10.1' into 10.1
* [Revision #671d9b6c61](https://github.com/MariaDB/server/commit/671d9b6c61)\
  2020-07-16 16:30:54 +0200\
  \*
  * Fix [MDEV-22571](https://jira.mariadb.org/browse/MDEV-22571) and [MDEV-22572](https://jira.mariadb.org/browse/MDEV-22572). Allow multiple ZIP table and enable using special column in them. modified: storage/connect/tabzip.cpp modified: storage/connect/tabzip.h
* [Revision #94b493571a](https://github.com/MariaDB/server/commit/94b493571a)\
  2020-10-23 12:20:17 +0400
  * [MDEV-20744](https://jira.mariadb.org/browse/MDEV-20744) SET GLOBAL `replicate_do_db` = DEFAULT causes crash.
* [Revision #897ea21e57](https://github.com/MariaDB/server/commit/897ea21e57)\
  2020-08-26 13:08:33 +0200
  * [MDEV-23358](https://jira.mariadb.org/browse/MDEV-23358) main.upgrade\_[MDEV-19650](https://jira.mariadb.org/browse/MDEV-19650) fails with result difference
* [Revision #43ec9370b3](https://github.com/MariaDB/server/commit/43ec9370b3)\
  2020-10-22 07:16:29 +0530
  * [MDEV-10149](https://jira.mariadb.org/browse/MDEV-10149): sys\_vars.rpl\_init\_slave\_func fails sporadically in buildbot
* [Revision #b4c225ac35](https://github.com/MariaDB/server/commit/b4c225ac35)\
  2020-10-07 16:06:20 +1100
  * [MDEV-23887](https://jira.mariadb.org/browse/MDEV-23887): check\_linker\_flags correct for old cmake compatibility
* Merge [Revision #65b7f72b51](https://github.com/MariaDB/server/commit/65b7f72b51) 2020-10-21 10:16:06 +0300 - InnoDB 5.6.50
* [Revision #c7552969d0](https://github.com/MariaDB/server/commit/c7552969d0)\
  2020-10-21 10:04:44 +0300
  * [MDEV-23999](https://jira.mariadb.org/browse/MDEV-23999) Potential stack overflow in InnoDB fulltext search
* [Revision #0627c4ae21](https://github.com/MariaDB/server/commit/0627c4ae21)\
  2020-10-17 14:18:54 +0200
  * Updated mtr help
* [Revision #9fca6645f4](https://github.com/MariaDB/server/commit/9fca6645f4)\
  2020-09-17 18:55:59 +0530
  * [MDEV-5628](https://jira.mariadb.org/browse/MDEV-5628): Assertion `! is_set()' or` !is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' fails on UPDATE on a partitioned table with subquery (MySQL:71630)
* [Revision #d36cd5f01e](https://github.com/MariaDB/server/commit/d36cd5f01e)\
  2020-07-27 02:51:33 +0530
  * [MDEV-17729](https://jira.mariadb.org/browse/MDEV-17729): Assertion \`! is\_set() || m\_can\_overwrite\_status' failed in Diagnostics\_area::set\_error\_status
* [Revision #3e807d255e](https://github.com/MariaDB/server/commit/3e807d255e)\
  2020-10-09 17:48:22 +0300
  * [MDEV-23938](https://jira.mariadb.org/browse/MDEV-23938): innodb row\_search\_idx\_cond\_check handle ICP\_ABORTED\_BY\_USER
* [Revision #72cb20820b](https://github.com/MariaDB/server/commit/72cb20820b)\
  2020-09-25 08:41:26 +0200
  * mysqlimport manpage - s/mysqldump/mysqlimport/g
* [Revision #6504d3d229](https://github.com/MariaDB/server/commit/6504d3d229)\
  2020-09-29 16:18:43 +0530
  * [MDEV-23722](https://jira.mariadb.org/browse/MDEV-23722) InnoDB: Assertion: result != FTS\_INVALID in fts\_trx\_row\_get\_new\_state
* [Revision #874942a0f9](https://github.com/MariaDB/server/commit/874942a0f9)\
  2020-10-05 13:26:28 +1100
  * [MDEV-4851](https://jira.mariadb.org/browse/MDEV-4851): (tests) log tables modifiable on log\_output!=TABLE
* [Revision #00c44fb18e](https://github.com/MariaDB/server/commit/00c44fb18e)\
  2012-09-20 12:34:31 +0530
  * [MDEV-4851](https://jira.mariadb.org/browse/MDEV-4851): BUG#11763447: 'YOU CANNOT 'ALTER' A LOG TABLE IF LOGGING IS ENABLED' EVEN IF I LOG TO FILE.
* Merge [Revision #83bd8ebfcd](https://github.com/MariaDB/server/commit/83bd8ebfcd) 2020-10-07 18:17:56 +0200 - Merge tag 'mariadb-10.1.47' into 10.1
* [Revision #1a850225d3](https://github.com/MariaDB/server/commit/1a850225d3)\
  2020-10-07 11:22:10 -0400
  * bump the VERSION
* [Revision #65c632cb9c](https://github.com/MariaDB/server/commit/65c632cb9c)\
  2020-09-29 19:12:00 +0300
  * [MDEV-23832](https://jira.mariadb.org/browse/MDEV-23832) Crash at startup in Log\_event::read\_log\_event
* [Revision #82301aea4f](https://github.com/MariaDB/server/commit/82301aea4f)\
  2020-10-02 05:19:41 +0200
  * [MDEV-23697](https://jira.mariadb.org/browse/MDEV-23697): bin/env perl -i -> bin/perl -i
* [Revision #904b811636](https://github.com/MariaDB/server/commit/904b811636)\
  2020-10-01 16:10:11 +1000
  * mtr: innodb\_stats\_dropped\_locked cleanup
* [Revision #7a1923c369](https://github.com/MariaDB/server/commit/7a1923c369)\
  2020-09-30 17:22:43 +0200
  * [MDEV-23697](https://jira.mariadb.org/browse/MDEV-23697): bin/env perl -i -> bin perl -i
* [Revision #83a520dbbb](https://github.com/MariaDB/server/commit/83a520dbbb)\
  2020-09-29 09:38:19 +0300
  * Cleanup: Remove unused rw\_lock\_t::writer\_is\_wait\_ex
* [Revision #fdb3c64e42](https://github.com/MariaDB/server/commit/fdb3c64e42)\
  2020-09-28 17:04:02 +0530
  * [MDEV-22277](https://jira.mariadb.org/browse/MDEV-22277) LeakSanitizer: detected memory leaks in mem\_heap\_create\_block\_func after attempt to create foreign key
* [Revision #15cd919535](https://github.com/MariaDB/server/commit/15cd919535)\
  2020-09-24 15:07:42 +0530
  * [MDEV-22330](https://jira.mariadb.org/browse/MDEV-22330): mysqlbinlog stops with an error Don't know how to handle column type: 255 meta: 4 (0004)
* [Revision #e0f5e7bc9e](https://github.com/MariaDB/server/commit/e0f5e7bc9e)\
  2020-09-25 15:58:08 +0300
  * Reverted wrong patch for mysql\_upgrade
* [Revision #1be8ac390d](https://github.com/MariaDB/server/commit/1be8ac390d)\
  2020-09-24 13:48:21 +1000
  * Revert "\[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] add show create user"
* [Revision #3d28d1f3aa](https://github.com/MariaDB/server/commit/3d28d1f3aa)\
  2020-09-24 08:16:30 +1000
  * [MDEV-23697](https://jira.mariadb.org/browse/MDEV-23697): /usr/bin/perl for debian scripts
* [Revision #4ddaa571fa](https://github.com/MariaDB/server/commit/4ddaa571fa)\
  2020-09-24 08:05:56 +1000
  * [MDEV-23697](https://jira.mariadb.org/browse/MDEV-23697): perl -w -> perl
* Merge [Revision #88c5c319e5](https://github.com/MariaDB/server/commit/88c5c319e5) 2020-09-24 08:00:41 +1000 - Merge branch '10.1' of [server](https://github.com/MariaDB/server) into 10.1
* [Revision #4c19227929](https://github.com/MariaDB/server/commit/4c19227929)\
  2017-12-12 11:24:39 +1100
  * systemd: mariadb@bootstrap - clear ExecStartPre and ExecStartPost
* [Revision #053653a23c](https://github.com/MariaDB/server/commit/053653a23c)\
  2016-03-08 11:05:32 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Update test cases for sysvars\_server\_embedded.
* [Revision #0ff897807f](https://github.com/MariaDB/server/commit/0ff897807f)\
  2016-03-08 10:50:04 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Make show\_create\_user testcase not run on embedded build
* [Revision #85b085972b](https://github.com/MariaDB/server/commit/85b085972b)\
  2016-03-08 00:35:03 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Post review fixes and cleanups.
* [Revision #f3f45e46b6](https://github.com/MariaDB/server/commit/f3f45e46b6)\
  2016-01-21 13:20:40 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Added show create user implementation.
* [Revision #a470b3570a](https://github.com/MariaDB/server/commit/a470b3570a)\
  2016-01-19 14:33:00 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Update test cases
* [Revision #f8b8d202bc](https://github.com/MariaDB/server/commit/f8b8d202bc)\
  2016-01-19 14:30:19 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Updated syntax for SHOW CREATE USER
* [Revision #6b6f066fdd](https://github.com/MariaDB/server/commit/6b6f066fdd)\
  2016-01-19 13:01:28 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Update test cases
* [Revision #a701e9e6c3](https://github.com/MariaDB/server/commit/a701e9e6c3)\
  2016-01-18 02:16:59 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Implement alter user and tested create user
* [Revision #c169838611](https://github.com/MariaDB/server/commit/c169838611)\
  2016-01-17 17:00:19 +0200
  * \[[MDEV-7978](https://jira.mariadb.org/browse/MDEV-7978)] Update grammar for new syntax
* [Revision #873cc1e77a](https://github.com/MariaDB/server/commit/873cc1e77a)\
  2020-09-16 14:03:32 +0530
  * [MDEV-21839](https://jira.mariadb.org/browse/MDEV-21839): Handle crazy offset to SHOW BINLOG EVENTS
* [Revision #5768f57d24](https://github.com/MariaDB/server/commit/5768f57d24)\
  2020-09-14 21:19:56 +1000
  * mtr: main.mysql\_upgrade - record after correcting error message
* [Revision #269f9c948c](https://github.com/MariaDB/server/commit/269f9c948c)\
  2020-09-12 09:27:46 +1000
  * mysql\_upgrade: fix error text
* [Revision #c3a3b4596c](https://github.com/MariaDB/server/commit/c3a3b4596c)\
  2020-09-11 15:27:58 +0100
  * [MDEV-17438](https://jira.mariadb.org/browse/MDEV-17438) rpl.show\_status\_stop\_slave\_race-7126 fails with timeout on Windows
* [Revision #a8f6bbb7a8](https://github.com/MariaDB/server/commit/a8f6bbb7a8)\
  2020-06-30 16:42:44 +0530
  * [MDEV-9501](https://jira.mariadb.org/browse/MDEV-9501): rpl.rpl\_binlog\_index, rpl.rpl\_gtid\_crash, rpl.rpl\_stm\_multi\_query fail sporadically in buildbot with Master command COM\_REGISTER\_SLAVE failed
* [Revision #420c4dcc7e](https://github.com/MariaDB/server/commit/420c4dcc7e)\
  2020-09-04 22:10:57 +0900
  * [MDEV-7098](https://jira.mariadb.org/browse/MDEV-7098) spider/bg.spider\_fixes failed in buildbot with safe\_mutex: Trying to unlock mutex conn->mta\_conn\_mutex that wasn't locked at storage/spider/spd\_db\_conn.cc, line 671
* [Revision #3ee2422624](https://github.com/MariaDB/server/commit/3ee2422624)\
  2020-09-04 17:40:51 +0800
  * InnoDB, XtraDB: handle EOPNOTSUPP from posix\_fallocate()
* [Revision #f0a57acb49](https://github.com/MariaDB/server/commit/f0a57acb49)\
  2020-09-03 11:31:06 +0400
  * [MDEV-23535](https://jira.mariadb.org/browse/MDEV-23535) SIGSEGV, SIGABRT and SIGILL in typeinfo for Item\_func\_set\_collation (on optimized builds)
* [Revision #94a520ddbe](https://github.com/MariaDB/server/commit/94a520ddbe)\
  2020-09-03 09:05:56 +0300
  * [MDEV-22387](https://jira.mariadb.org/browse/MDEV-22387): Do not pass null pointer to some memcpy()
* [Revision #a256070e7d](https://github.com/MariaDB/server/commit/a256070e7d)\
  2020-09-03 08:41:47 +0300
  * [MDEV-7110](https://jira.mariadb.org/browse/MDEV-7110) follow-up fix: Do not pass NULL as nonnull parameter
* [Revision #cd36bc01a5](https://github.com/MariaDB/server/commit/cd36bc01a5)\
  2020-08-26 16:25:28 +0530
  * [MDEV-23534](https://jira.mariadb.org/browse/MDEV-23534): SIGSEGV in sf\_malloc\_usable\_size/my\_free on SET GLOBAL REPLICATE\_DO\_TABLE
* [Revision #94e9dc95d4](https://github.com/MariaDB/server/commit/94e9dc95d4)\
  2020-09-01 15:52:36 +0300
  * [MDEV-23600](https://jira.mariadb.org/browse/MDEV-23600) Division by 0 in row\_search\_with\_covering\_prefix
* [Revision #feac078f15](https://github.com/MariaDB/server/commit/feac078f15)\
  2020-08-11 21:45:09 +0300
  * [MDEV-16372](https://jira.mariadb.org/browse/MDEV-16372) ER\_BASE64\_DECODE\_ERROR upon replaying binary log via mysqlbinlog --verbose
* [Revision #f69cc26757](https://github.com/MariaDB/server/commit/f69cc26757)\
  2020-08-27 17:34:12 +0530
  * [MDEV-23596](https://jira.mariadb.org/browse/MDEV-23596): Assertion \`tab->ref.use\_count' failed in join\_read\_key\_unlock\_row
* [Revision #62d1e3bf67](https://github.com/MariaDB/server/commit/62d1e3bf67)\
  2020-08-24 18:52:44 +0200
  * [MDEV-23569](https://jira.mariadb.org/browse/MDEV-23569) temporary tables can overwrite existing files
* [Revision #29d9df16ff](https://github.com/MariaDB/server/commit/29d9df16ff)\
  2020-08-21 08:52:45 +0300
  * Revert "[MDEV-21039](https://jira.mariadb.org/browse/MDEV-21039): Server fails to start with unknown mysqld\_safe options"
* [Revision #ece0b0623c](https://github.com/MariaDB/server/commit/ece0b0623c)\
  2020-08-16 22:14:59 +0200
  * [MDEV-23491](https://jira.mariadb.org/browse/MDEV-23491): bss\_start breaks compilation of various platforms
* [Revision #5796021174](https://github.com/MariaDB/server/commit/5796021174)\
  2020-08-11 14:03:02 +0200
  * [MDEV-21039](https://jira.mariadb.org/browse/MDEV-21039): Server fails to start with unknown mysqld\_safe options
* [Revision #b970363acf](https://github.com/MariaDB/server/commit/b970363acf)\
  2020-08-10 18:23:25 +1000
  * [MDEV-23440](https://jira.mariadb.org/browse/MDEV-23440): mysql\_tzinfo\_to\_sql to use transactions
* [Revision #7c2aad6be2](https://github.com/MariaDB/server/commit/7c2aad6be2)\
  2020-08-13 17:43:37 +0300
  * [MDEV-23463](https://jira.mariadb.org/browse/MDEV-23463) fil\_page\_decompress() debug check wastes 128KiB of stack
* [Revision #101ce10d0d](https://github.com/MariaDB/server/commit/101ce10d0d)\
  2020-08-12 18:35:21 +0300
  * [MDEV-20672](https://jira.mariadb.org/browse/MDEV-20672) Inconsistent usage message for innodb\_compression\_algorithm
* [Revision #efd8af535a](https://github.com/MariaDB/server/commit/efd8af535a)\
  2020-08-12 18:21:53 +0300
  * [MDEV-19526](https://jira.mariadb.org/browse/MDEV-19526) heap number overflow on innodb\_page\_size=64k
* [Revision #7ad4709a3b](https://github.com/MariaDB/server/commit/7ad4709a3b)\
  2020-08-04 14:25:58 +0200
  * [MDEV-21526](https://jira.mariadb.org/browse/MDEV-21526): mysqld\_multi no longer works with different server binaries
* [Revision #caf105905a](https://github.com/MariaDB/server/commit/caf105905a)\
  2020-08-11 10:33:10 +0400
  * Fixing sporading builtbot test failures happening at '00:00:00' sharp
* [Revision #7f67ef1485](https://github.com/MariaDB/server/commit/7f67ef1485)\
  2020-08-10 15:18:53 +0300
  * [MDEV-16115](https://jira.mariadb.org/browse/MDEV-16115) Hang after reducing innodb\_encryption\_threads
* [Revision #3e3da1642d](https://github.com/MariaDB/server/commit/3e3da1642d)\
  2020-08-10 10:16:31 -0400
  * bump the VERSION
* Merge [Revision #b350ef4cf4](https://github.com/MariaDB/server/commit/b350ef4cf4) 2020-08-10 16:07:48 +0200 - Merge remote-tracking branch 'bb-10.1-release' into 10.1
* [Revision #deb365581b](https://github.com/MariaDB/server/commit/deb365581b)\
  2020-05-05 19:23:29 +1000
  * [MDEV-23386](https://jira.mariadb.org/browse/MDEV-23386): mtr: main.mysqld--help autosized table{-open,}-cach and max-connections
* [Revision #85bd5314c5](https://github.com/MariaDB/server/commit/85bd5314c5)\
  2020-08-06 13:39:10 +0300
  * Better comment about TABLE::maybe\_null
* [Revision #ab578bdf45](https://github.com/MariaDB/server/commit/ab578bdf45)\
  2020-08-04 14:36:01 +0530
  * [MDEV-9513](https://jira.mariadb.org/browse/MDEV-9513): Assertion \`join->group\_list || !join->is\_in\_subquery()' failed in create\_sort\_index
* [Revision #0e80f5a693](https://github.com/MariaDB/server/commit/0e80f5a693)\
  2020-08-05 08:14:49 +0400
  * [MDEV-23105](https://jira.mariadb.org/browse/MDEV-23105) Cast number string with many leading zeros to decimal gives unexpected result

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
