# MariaDB 10.4.19 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.19](https://downloads.mariadb.org/mariadb/10.4.19/)[Release Notes](../../old-releases/10.4/10.4.19.md)[Changelog](mariadb-10419-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 7 May 2021

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.19.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.29](../changelogs-mariadb-10-3-series/mariadb-10329-changelog.md)
* [Revision #a4139f8d68](https://github.com/MariaDB/server/commit/a4139f8d68)\
  2021-05-05 22:50:20 +0300
  * remove the test for [MDEV-16962](https://jira.mariadb.org/browse/MDEV-16962)
* [Revision #0775ca315e](https://github.com/MariaDB/server/commit/0775ca315e)\
  2021-05-05 19:27:29 +0200
  * [MDEV-23542](https://jira.mariadb.org/browse/MDEV-23542) Server crashes in thd\_clear\_errors()
* [Revision #da63eb16c9](https://github.com/MariaDB/server/commit/da63eb16c9)\
  2021-05-05 15:12:07 +0300
  * fix galera\_password.result for 10.4
* Merge [Revision #509e4990af](https://github.com/MariaDB/server/commit/509e4990af) 2021-05-05 23:03:01 +0300 - Merge branch bb-10.3-release into bb-10.4-release
* [Revision #0cc811c633](https://github.com/MariaDB/server/commit/0cc811c633)\
  2021-04-29 12:17:40 +0300
  * Update wsrep-lib
* [Revision #cec8ea3ab5](https://github.com/MariaDB/server/commit/cec8ea3ab5)\
  2021-04-19 22:54:45 +0900
  * [MDEV-22265](https://jira.mariadb.org/browse/MDEV-22265) Connect string character limit too small for full 64 character InnoDB table-name limit when using ad-hoc Spider server definitions.
* [Revision #b1b2689f17](https://github.com/MariaDB/server/commit/b1b2689f17)\
  2021-04-23 11:31:02 +0200
  * [MDEV-25553](https://jira.mariadb.org/browse/MDEV-25553) : Avoid unnecessary rollbacks with SR
* [Revision #206d630ea0](https://github.com/MariaDB/server/commit/206d630ea0)\
  2021-04-26 11:17:30 +0200
  * [MDEV-22227](https://jira.mariadb.org/browse/MDEV-22227) Assertion \`state\_ == s\_exec' failed in wsrep::client\_state::start\_transaction
* [Revision #4cd92143ea](https://github.com/MariaDB/server/commit/4cd92143ea)\
  2021-04-28 03:56:24 +0530
  * [MDEV-25630](https://jira.mariadb.org/browse/MDEV-25630) Rollback of instant operation adds wrong column to secondary index
* [Revision #5bc12ca9c2](https://github.com/MariaDB/server/commit/5bc12ca9c2)\
  2021-04-23 13:04:36 +0400
  * [MDEV-22265](https://jira.mariadb.org/browse/MDEV-22265) Connect string character limit too small for full 64 character InnoDB table-name limit when using ad-hoc Spider server definitions.
* Merge [Revision #90a306a7ab](https://github.com/MariaDB/server/commit/90a306a7ab) 2021-04-27 08:53:50 +0300 - Merge 10.3 into 10.4
* [Revision #9e6310e323](https://github.com/MariaDB/server/commit/9e6310e323)\
  2021-04-14 17:06:31 +0200
  * Fix MTR test wsrep.variables\_debug
* Merge [Revision #e4394cc547](https://github.com/MariaDB/server/commit/e4394cc547) 2021-04-25 10:20:57 +0300 - Merge 10.3 into 10.4
* Merge [Revision #ee455e6f2e](https://github.com/MariaDB/server/commit/ee455e6f2e) 2021-04-22 07:51:33 +0300 - Merge 10.3 into 10.4
* [Revision #0d267f7caa](https://github.com/MariaDB/server/commit/0d267f7caa)\
  2021-04-22 07:36:04 +0300
  * [MDEV-25362](https://jira.mariadb.org/browse/MDEV-25362) after-merge fix: Remove unnecessary code
* [Revision #ceed768eea](https://github.com/MariaDB/server/commit/ceed768eea)\
  2021-04-21 10:06:31 +0300
  * [MDEV-25362](https://jira.mariadb.org/browse/MDEV-25362) after-merge fix: GCC -Og -Wmaybe-uninitialized
* Merge [Revision #a0588d54a2](https://github.com/MariaDB/server/commit/a0588d54a2) 2021-04-21 07:58:42 +0300 - Merge 10.3 into 10.4
* [Revision #031f11717d](https://github.com/MariaDB/server/commit/031f11717d)\
  2021-04-18 15:29:13 +0300
  * Fix all warnings given by UBSAN
* [Revision #eb4123eefc](https://github.com/MariaDB/server/commit/eb4123eefc)\
  2021-04-14 22:40:46 +0200
  * More fixes to variable wsrep\_on
* [Revision #57caff245c](https://github.com/MariaDB/server/commit/57caff245c)\
  2021-04-11 09:37:36 +0300
  * [MDEV-25423](https://jira.mariadb.org/browse/MDEV-25423) : Donor node fails to shutdown after mysqldump SST
* [Revision #c3b016efde](https://github.com/MariaDB/server/commit/c3b016efde)\
  2021-02-05 11:06:25 +0100
  * [MDEV-22668](https://jira.mariadb.org/browse/MDEV-22668): "Flush SSL" command doesn't reload wsrep cert
* [Revision #767d63374e](https://github.com/MariaDB/server/commit/767d63374e)\
  2021-04-14 12:43:36 +0300
  * After-merge fix: Make GCC 4.8.5 happy
* Merge [Revision #5008171b05](https://github.com/MariaDB/server/commit/5008171b05) 2021-04-14 10:33:59 +0300 - Merge 10.3 into 10.4
* [Revision #61f84bba60](https://github.com/MariaDB/server/commit/61f84bba60)\
  2021-04-13 09:38:32 +0700
  * [MDEV-25197](https://jira.mariadb.org/browse/MDEV-25197): The statement set password=password('') executed in PS mode fails in case it is run by a user with expired password
* [Revision #e14b682636](https://github.com/MariaDB/server/commit/e14b682636)\
  2021-04-12 17:49:36 +0300
  * Fixed assert in WSREP if one started with --wsrep\_provider=.. --wsrep\_on=OFF
* [Revision #c03841ec0e](https://github.com/MariaDB/server/commit/c03841ec0e)\
  2021-04-08 17:25:02 +0300
  * [MDEV-23634](https://jira.mariadb.org/browse/MDEV-23634): Select query hanged the server and leads to OOM ...
* [Revision #4e2ca42225](https://github.com/MariaDB/server/commit/4e2ca42225)\
  2021-04-06 16:37:11 +0300
  * [MDEV-25334](https://jira.mariadb.org/browse/MDEV-25334) FTWRL/Backup blocks DDL on temporary tables with binlog enabled, assertion fails in Diagnostics\_area::set\_error\_status
* [Revision #58780b5afb](https://github.com/MariaDB/server/commit/58780b5afb)\
  2021-03-25 06:55:18 +0400
  * [MDEV-22775](https://jira.mariadb.org/browse/MDEV-22775) \[HY000]\[1553] Changing name of primary key column with foreign key constraint fails.
* [Revision #f69c1c9dcb](https://github.com/MariaDB/server/commit/f69c1c9dcb)\
  2021-04-06 16:57:38 +1000
  * [MDEV-19508](https://jira.mariadb.org/browse/MDEV-19508): SI\_KERNEL is not on all implementations
* [Revision #5b71e0424c](https://github.com/MariaDB/server/commit/5b71e0424c)\
  2021-04-06 15:33:13 +0300
  * [MDEV-21402](https://jira.mariadb.org/browse/MDEV-21402) : sql\_safe\_updates breaks Galera 4
* [Revision #f8488370d6](https://github.com/MariaDB/server/commit/f8488370d6)\
  2021-03-31 14:59:50 +0200
  * [MDEV-24956](https://jira.mariadb.org/browse/MDEV-24956): ALTER TABLE not replicated with Galera in [MariaDB 10.5.9](../../old-releases/10.5/10.5.9.md)
* [Revision #915983e1cc](https://github.com/MariaDB/server/commit/915983e1cc)\
  2021-03-24 10:55:27 +0100
  * [MDEV-25226](https://jira.mariadb.org/browse/MDEV-25226) Assertion when wsrep\_on set OFF with SR transaction
* [Revision #880baedcf6](https://github.com/MariaDB/server/commit/880baedcf6)\
  2021-04-02 18:13:46 +0300
  * [MDEV-17913](https://jira.mariadb.org/browse/MDEV-17913) Encrypted transactional Aria tables remain corrupt after crash recovery, automatic repairment does not work
* [Revision #8341f582b2](https://github.com/MariaDB/server/commit/8341f582b2)\
  2021-03-31 10:55:21 +0300
  * [MDEV-15527](https://jira.mariadb.org/browse/MDEV-15527) fixup for innodb\_checksum\_algorithm=full\_crc32
* Merge [Revision #50de71b026](https://github.com/MariaDB/server/commit/50de71b026) 2021-03-31 09:47:14 +0300 - Merge 10.3 into 10.4
* Merge [Revision #7ae37ff74f](https://github.com/MariaDB/server/commit/7ae37ff74f) 2021-03-27 17:12:28 +0200 - Merge 10.3 into 10.4
* [Revision #d1ff2c583f](https://github.com/MariaDB/server/commit/d1ff2c583f)\
  2021-03-16 12:53:40 +0100
  * [MDEV-21697](https://jira.mariadb.org/browse/MDEV-21697): Galera assertion !wsrep\_has\_changes(thd) || (thd->lex->sql\_command == SQLCOM\_CREATE\_TABLE && !thd->is\_current\_stmt\_binlog\_format\_row())
* [Revision #161f4036c4](https://github.com/MariaDB/server/commit/161f4036c4)\
  2021-03-25 07:37:50 +0200
  * [MDEV-24954](https://jira.mariadb.org/browse/MDEV-24954) : 10.5.9 crashes on int wsrep::client\_state::ordered\_commit(): Assertion \`owning\_thread\_id\_ == wsrep::this\_thread::get\_id()' failed.
* [Revision #2eae1376fe](https://github.com/MariaDB/server/commit/2eae1376fe)\
  2021-03-23 12:37:55 +0700
  * fixed typo in postinst script
* [Revision #aba7884138](https://github.com/MariaDB/server/commit/aba7884138)\
  2021-03-21 12:08:54 -0700
  * [MDEV-25206](https://jira.mariadb.org/browse/MDEV-25206) Crash with CREATE VIEW .. SELECT with non-existing field in ON condition
* Merge [Revision #d8dc8537e4](https://github.com/MariaDB/server/commit/d8dc8537e4) 2021-03-20 13:04:36 +0200 - Merge 10.3 into 10.4
* [Revision #550cf13eb3](https://github.com/MariaDB/server/commit/550cf13eb3)\
  2021-03-19 11:53:49 +0200
  * Disable failing Galera tests
* Merge [Revision #44d70c01f0](https://github.com/MariaDB/server/commit/44d70c01f0) 2021-03-19 11:42:44 +0200 - Merge 10.3 into 10.4
* [Revision #126725421e](https://github.com/MariaDB/server/commit/126725421e)\
  2021-03-18 14:43:08 +0200
  * [MDEV-25121](https://jira.mariadb.org/browse/MDEV-25121): innodb\_flush\_method=O\_DIRECT fails on compressed tables
* Merge [Revision #39c015b77e](https://github.com/MariaDB/server/commit/39c015b77e) 2021-03-18 14:17:58 +0200 - Merge 10.3 into 10.4
* [Revision #5511c21b41](https://github.com/MariaDB/server/commit/5511c21b41)\
  2021-03-16 13:13:50 +0200
  * [MDEV-23851](https://jira.mariadb.org/browse/MDEV-23851) BF-BF Conflict issue because of UK GAP locks
* [Revision #f4e4bff992](https://github.com/MariaDB/server/commit/f4e4bff992)\
  2021-03-16 13:02:44 +0200
  * [MDEV-24916](https://jira.mariadb.org/browse/MDEV-24916) : Assertion \`current\_stmt\_binlog\_format == BINLOG\_FORMAT\_STMT || current\_stmt\_binlog\_format == BINLOG\_FORMAT\_ROW' failed in THD::is\_current\_stmt\_binlog\_format\_row
* Merge [Revision #1ea6ac3c95](https://github.com/MariaDB/server/commit/1ea6ac3c95) 2021-03-11 19:33:45 +0200 - Merge 10.3 into 10.4
* [Revision #2c3014e8a7](https://github.com/MariaDB/server/commit/2c3014e8a7)\
  2021-03-11 19:14:35 +0200
  * [MDEV-24668](https://jira.mariadb.org/browse/MDEV-24668) fixup: uninitialized return value with Galera
* [Revision #06df0b0dce](https://github.com/MariaDB/server/commit/06df0b0dce)\
  2021-03-11 20:52:30 +0530
  * [MDEV-25107](https://jira.mariadb.org/browse/MDEV-25107) Check TABLE miscalutates the length of column
* [Revision #fa5f60681f](https://github.com/MariaDB/server/commit/fa5f60681f)\
  2020-06-18 01:11:39 +0300
  * [MDEV-20946](https://jira.mariadb.org/browse/MDEV-20946): Hard FTWRL deadlock under user level locks
* [Revision #8f4a3bf07c](https://github.com/MariaDB/server/commit/8f4a3bf07c)\
  2021-03-05 13:35:29 +0530
  * [MDEV-25057](https://jira.mariadb.org/browse/MDEV-25057) Assertion \`n\_fields < dtuple\_get\_n\_fields(entry)' failed in dtuple\_convert\_big\_rec
* [Revision #1dff411e84](https://github.com/MariaDB/server/commit/1dff411e84)\
  2021-03-08 18:54:58 +0000
  * arguments overflow fix proposal. the list is assumed to be implictly null terminated at usage time.
* [Revision #e3a597378e](https://github.com/MariaDB/server/commit/e3a597378e)\
  2021-02-03 19:44:34 +0000
  * mariadb-backup utility, binary path implementation for Mac.
* [Revision #1d762ee8fe](https://github.com/MariaDB/server/commit/1d762ee8fe)\
  2021-03-08 17:51:33 +0200
  * [MDEV-24363](https://jira.mariadb.org/browse/MDEV-24363) (followup fix) mysql.user view should
* [Revision #01a0d739c8](https://github.com/MariaDB/server/commit/01a0d739c8)\
  2021-03-07 01:53:52 +0100
  * [MDEV-24975](https://jira.mariadb.org/browse/MDEV-24975) Server consumes extra 4G memory upon querying INFORMATION\_SCHEMA.OPTIIMIZER\_TRACE
* [Revision #f24038b851](https://github.com/MariaDB/server/commit/f24038b851)\
  2021-03-07 14:06:01 +0100
  * mark Aria allocations for temp tables as MY\_THREAD\_SPECIFIC
* [Revision #9742cf4203](https://github.com/MariaDB/server/commit/9742cf4203)\
  2021-03-06 12:31:02 +0100
  * [MDEV-24668](https://jira.mariadb.org/browse/MDEV-24668) debug assert on SET PASSWORD when binlog fails
* [Revision #cf1ca57e75](https://github.com/MariaDB/server/commit/cf1ca57e75)\
  2021-03-06 12:18:48 +0100
  * cleanup: renames, no need to create a new .inc file
* [Revision #44b85406b8](https://github.com/MariaDB/server/commit/44b85406b8)\
  2021-03-05 11:11:13 +0200
  * [MDEV-24363](https://jira.mariadb.org/browse/MDEV-24363) (followup refactor) avoid listing mysql.user
* [Revision #363ba10784](https://github.com/MariaDB/server/commit/363ba10784)\
  2021-02-02 14:57:16 +0200
  * [MDEV-24363](https://jira.mariadb.org/browse/MDEV-24363) mysql.user password\_expired column is incorrect
* Merge [Revision #a26e7a3726](https://github.com/MariaDB/server/commit/a26e7a3726) 2021-03-08 09:39:54 +0200 - Merge 10.3 into 10.4
* Merge [Revision #39e2c95771](https://github.com/MariaDB/server/commit/39e2c95771) 2021-03-08 09:09:31 +0200 - Merge 10.3 into 10.4
* [Revision #fcc9f8b10c](https://github.com/MariaDB/server/commit/fcc9f8b10c)\
  2021-03-05 10:40:16 +0200
  * Remove unused HA\_EXTRA\_FAKE\_START\_STMT
* Merge [Revision #8bab5bb332](https://github.com/MariaDB/server/commit/8bab5bb332) 2021-03-05 10:36:51 +0200 - Merge 10.3 into 10.4
* [Revision #82efe4a15a](https://github.com/MariaDB/server/commit/82efe4a15a)\
  2021-03-02 14:13:39 +0200
  * [MDEV-23843](https://jira.mariadb.org/browse/MDEV-23843) Assertions in Diagnostics\_area upon table operations under FTWRL
* Merge [Revision #a6c6c4f463](https://github.com/MariaDB/server/commit/a6c6c4f463) 2021-02-25 12:31:26 +0200 - Merge 10.3 into 10.4
* Merge [Revision #ef96ec3b51](https://github.com/MariaDB/server/commit/ef96ec3b51) 2021-02-25 15:46:32 +1100 - Merge branch '10.3' into 10.4
* Merge [Revision #36810342d5](https://github.com/MariaDB/server/commit/36810342d5) 2021-02-25 13:16:10 +1100 - Merge branch '10.3' into 10.4
* [Revision #d1eeb4b839](https://github.com/MariaDB/server/commit/d1eeb4b839)\
  2021-02-24 12:02:54 +0200
  * [MDEV-24964](https://jira.mariadb.org/browse/MDEV-24964) : Heap-buffer-overflow on wsrep\_schema.cc ::remove\_fragments
* [Revision #f2428b9c24](https://github.com/MariaDB/server/commit/f2428b9c24)\
  2021-02-24 13:30:35 +0200
  * [MDEV-24967](https://jira.mariadb.org/browse/MDEV-24967) : Signal 11 on ha\_innodb.cc::bg\_wsrep\_kill\_trx line 18611
* [Revision #2628fa2dba](https://github.com/MariaDB/server/commit/2628fa2dba)\
  2021-02-05 12:52:48 +1100
  * [MDEV-20857](https://jira.mariadb.org/browse/MDEV-20857): perf schema conflict name filename\_hash
* Merge [Revision #ad0f0d2b1a](https://github.com/MariaDB/server/commit/ad0f0d2b1a) 2021-02-23 21:44:22 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #3c9d03edda](https://github.com/MariaDB/server/commit/3c9d03edda) 2021-02-23 14:11:08 +0200 - Merge 10.3 into 10.4
* Merge [Revision #245d33db4e](https://github.com/MariaDB/server/commit/245d33db4e) 2021-02-23 10:35:16 +0100 - Merge branch 'github/10.4' into 10.4
* [Revision #8b77e6c676](https://github.com/MariaDB/server/commit/8b77e6c676)\
  2020-12-15 17:39:24 +0200
  * [MDEV-24114](https://jira.mariadb.org/browse/MDEV-24114) SHOW CREATE USER doesnt display correct password expiry status
* Merge [Revision #e841957416](https://github.com/MariaDB/server/commit/e841957416) 2021-02-23 00:56:14 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #34fcd726a6](https://github.com/MariaDB/server/commit/34fcd726a6) 2021-02-23 00:08:56 +0100 - Merge branch 'bb-10.4-release' into 10.4
* [Revision #7b8dacc488](https://github.com/MariaDB/server/commit/7b8dacc488)\
  2021-02-22 09:43:28 -0500
  * bump the VERSION
* [Revision #901bcde2dd](https://github.com/MariaDB/server/commit/901bcde2dd)\
  2021-02-16 01:11:41 +0100
  * galera.galera\_gra\_log crashes
* [Revision #a5bcec727b](https://github.com/MariaDB/server/commit/a5bcec727b)\
  2021-02-16 08:46:14 +0200
  * [MDEV-24865](https://jira.mariadb.org/browse/MDEV-24865) : Server crashes when truncate mysql user table
* [Revision #d0defd1ea2](https://github.com/MariaDB/server/commit/d0defd1ea2)\
  2021-02-14 17:43:31 +0200
  * In case of an abort, write "handling fatal signal" to DBUG log.
* [Revision #af31e2c55d](https://github.com/MariaDB/server/commit/af31e2c55d)\
  2021-02-14 17:42:19 +0200
  * [MDEV-23843](https://jira.mariadb.org/browse/MDEV-23843) Assertions in Diagnostics\_area upon table operations under FTWRL
* [Revision #3cd32a9baf](https://github.com/MariaDB/server/commit/3cd32a9baf)\
  2021-02-12 17:56:46 +0200
  * Remove extra (not needed) error from multi-table-update for killed query
* [Revision #23833dce05](https://github.com/MariaDB/server/commit/23833dce05)\
  2021-02-12 11:28:42 +0300
  * [MDEV-24792](https://jira.mariadb.org/browse/MDEV-24792) Assertion \`!newest\_lsn || fil\_page\_get\_type(page)' failed upon mariadb-backup prepare in buf\_flush\_init\_for\_writing with innodb\_log\_optimize\_ddl=off
* [Revision #cb4434c44a](https://github.com/MariaDB/server/commit/cb4434c44a)\
  2021-02-13 10:28:10 +0200
  * [MDEV-24856](https://jira.mariadb.org/browse/MDEV-24856) : Server crashes when wsrep\_provider\_options set to NULL
* [Revision #542d769ea1](https://github.com/MariaDB/server/commit/542d769ea1)\
  2020-11-11 09:22:05 +0100
  * [MDEV-18280](https://jira.mariadb.org/browse/MDEV-18280): Galera test failure on galera\_split\_brain and galera\_kill\_nochanges

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
