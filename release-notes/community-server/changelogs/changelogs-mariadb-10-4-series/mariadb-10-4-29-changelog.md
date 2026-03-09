# MariaDB 10.4.29 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.29](https://downloads.mariadb.org/mariadb/10.4.29/)[Release Notes](../../old-releases/10.4/10.4.29.md)[Changelog](mariadb-10-4-29-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.4.29/)

**Release date:** 10 May 2023

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.29.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.39](../changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md)
* [Revision #2594da7a33](https://github.com/MariaDB/server/commit/2594da7a33)\
  2023-05-05 11:16:23 +0300
  * [MDEV-31194](https://jira.mariadb.org/browse/MDEV-31194): Server crash or assertion failure with join\_cache\_level=4
* [Revision #7973ffde0f](https://github.com/MariaDB/server/commit/7973ffde0f)\
  2023-05-04 17:51:27 +0200
  * [MDEV-31189](https://jira.mariadb.org/browse/MDEV-31189) Server crash or assertion failure in upon 2nd execution of PS with views and HAVING
* [Revision #cf4a16b555](https://github.com/MariaDB/server/commit/cf4a16b555)\
  2023-05-04 16:05:08 +0200
  * [MDEV-31057](https://jira.mariadb.org/browse/MDEV-31057) rocksdb does not compile with gcc-13
* [Revision #4d6e458f9f](https://github.com/MariaDB/server/commit/4d6e458f9f)\
  2023-05-03 15:37:05 +0200
  * [MDEV-31164](https://jira.mariadb.org/browse/MDEV-31164) default current\_timestamp() not working when used INSERT ON DUPLICATE KEY in some cases
* [Revision #f5e7c56e32](https://github.com/MariaDB/server/commit/f5e7c56e32)\
  2023-05-04 08:11:00 +0200
  * [MDEV-31181](https://jira.mariadb.org/browse/MDEV-31181) Server crash in subselect\_uniquesubquery\_engine::print upon EXPLAIN EXTENDED DELETE
* [Revision #62ec258f10](https://github.com/MariaDB/server/commit/62ec258f10)\
  2023-05-04 08:05:40 +0200
  * Fix of selectivity test to behave correctly with embedded and view protocols.
* [Revision #ed3e6f66a2](https://github.com/MariaDB/server/commit/ed3e6f66a2)\
  2023-05-03 13:49:32 +0300
  * [MDEV-26301](https://jira.mariadb.org/browse/MDEV-26301): Split optimization refills: Optimizer Trace coverage
* [Revision #ce7ffe61d8](https://github.com/MariaDB/server/commit/ce7ffe61d8)\
  2023-05-02 23:17:07 -0700
  * [MDEV-26301](https://jira.mariadb.org/browse/MDEV-26301) Split optimization refills temporary table too many times
* [Revision #ec79f37718](https://github.com/MariaDB/server/commit/ec79f37718)\
  2023-05-03 10:32:29 +0300
  * [MDEV-29621](https://jira.mariadb.org/browse/MDEV-29621) part 2 of post-merge fixes in galera
* [Revision #430b972702](https://github.com/MariaDB/server/commit/430b972702)\
  2023-05-03 07:45:15 +0200
  * Protect a new condition (by Andrei)
* Merge [Revision #5597562aa6](https://github.com/MariaDB/server/commit/5597562aa6) 2023-05-02 20:14:47 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #1d15300b30](https://github.com/MariaDB/server/commit/1d15300b30) 2023-05-02 15:45:35 +0200 - Merge branch '10.4' into bb-10.4-release
* [Revision #c6ef9b1c1a](https://github.com/MariaDB/server/commit/c6ef9b1c1a)\
  2023-05-02 11:20:35 +0200
  * wsrep-lib external submodule update
* [Revision #ef227762b1](https://github.com/MariaDB/server/commit/ef227762b1)\
  2023-03-14 10:30:09 +0100
  * [MDEV-30838](https://jira.mariadb.org/browse/MDEV-30838) Assertion \`m\_thd == \_current\_thd()'
* [Revision #4e942bcd93](https://github.com/MariaDB/server/commit/4e942bcd93)\
  2023-01-23 12:09:54 +0200
  * [MDEV-30414](https://jira.mariadb.org/browse/MDEV-30414) sporadic failures with galera var retry autocommit
* Merge [Revision #edd0b03e60](https://github.com/MariaDB/server/commit/edd0b03e60) 2023-05-02 10:09:27 +0200 - Merge branch '10.3' into 10.4
* [Revision #ddcc9d2281](https://github.com/MariaDB/server/commit/ddcc9d2281)\
  2023-04-29 07:39:38 +0400
  * [MDEV-31153](https://jira.mariadb.org/browse/MDEV-31153) New methods Schema::make\_item\_func\_\* for REPLACE, SUBSTRING, TRIM
* [Revision #2e74f9d281](https://github.com/MariaDB/server/commit/2e74f9d281)\
  2023-04-29 06:33:09 +0400
  * Adding "const" qualifiers to a few trivial Lex\_input\_string methods
* [Revision #1963a87b2e](https://github.com/MariaDB/server/commit/1963a87b2e)\
  2023-04-25 16:07:05 +0000
  * [MDEV-30221](https://jira.mariadb.org/browse/MDEV-30221): Move environmental macros to before master-slave The fix was introduced, along with re-ordering to do other macros that check test environment capabilities before master/slave is set up.
* [Revision #85cc831880](https://github.com/MariaDB/server/commit/85cc831880)\
  2023-04-19 15:15:27 +0300
  * [MDEV-31067](https://jira.mariadb.org/browse/MDEV-31067): selectivity\_from\_histogram >1.0 for a DOUBLE\_PREC\_HB histogram
* [Revision #bc970573b3](https://github.com/MariaDB/server/commit/bc970573b3)\
  2023-04-28 11:25:31 +0200
  * [MDEV-22756](https://jira.mariadb.org/browse/MDEV-22756) SQL Error (1364): Field 'DB\_ROW\_HASH\_1' doesn't have a default value
* [Revision #adbad5e36f](https://github.com/MariaDB/server/commit/adbad5e36f)\
  2023-04-25 14:34:31 +0700
  * [MDEV-31113](https://jira.mariadb.org/browse/MDEV-31113) Server crashes in store\_length / Type\_handler\_string\_result::make\_sort\_key with DISTINCT and group function
* [Revision #f21664414d](https://github.com/MariaDB/server/commit/f21664414d)\
  2023-04-27 10:31:50 +0200
  * [MDEV-31129](https://jira.mariadb.org/browse/MDEV-31129) build failure with RocksDB, incompatible pointer to integer conversion
* [Revision #a959c22e7f](https://github.com/MariaDB/server/commit/a959c22e7f)\
  2023-04-27 10:46:41 +0200
  * return accidentally removed in 45d4f6b97b4811b1b7783dcd19526be1dbb196dc comment
* [Revision #6171119bc1](https://github.com/MariaDB/server/commit/6171119bc1)\
  2023-04-17 15:06:52 +0200
  * [MDEV-30889](https://jira.mariadb.org/browse/MDEV-30889): 3 - Item\_in\_optimizer leak
* [Revision #45d4f6b97b](https://github.com/MariaDB/server/commit/45d4f6b97b)\
  2023-04-12 15:08:23 +0200
  * [MDEV-30889](https://jira.mariadb.org/browse/MDEV-30889): 2 - Allocation in TABLE\_SHARE::init\_from\_sql\_statement\_string
* [Revision #348f4c9f3b](https://github.com/MariaDB/server/commit/348f4c9f3b)\
  2023-04-11 14:00:42 +0200
  * [MDEV-30889](https://jira.mariadb.org/browse/MDEV-30889): 1 - Allocation in Item\_subselect::mark\_as\_dependent
* [Revision #b942f41438](https://github.com/MariaDB/server/commit/b942f41438)\
  2023-04-25 12:37:13 +0200
  * [MDEV-30218](https://jira.mariadb.org/browse/MDEV-30218) update test result
* [Revision #b3817425d9](https://github.com/MariaDB/server/commit/b3817425d9)\
  2023-04-21 14:02:56 +0200
  * [MDEV-11356](https://jira.mariadb.org/browse/MDEV-11356) Option skip-core-file does not work
* [Revision #e22a57da82](https://github.com/MariaDB/server/commit/e22a57da82)\
  2023-03-23 18:45:34 +0200
  * [MDEV-30620](https://jira.mariadb.org/browse/MDEV-30620) Trying to lock uninitialized LOCK\_parallel\_entry
* [Revision #a72b2c3ffb](https://github.com/MariaDB/server/commit/a72b2c3ffb)\
  2023-04-24 17:57:45 +0300
  * [MDEV-31121](https://jira.mariadb.org/browse/MDEV-31121): ANALYZE statement produces 0 for all timings in embedded server
* [Revision #29fb041007](https://github.com/MariaDB/server/commit/29fb041007)\
  2023-04-05 10:43:28 -0600
  * [MDEV-30430](https://jira.mariadb.org/browse/MDEV-30430): Enabling system versioning on tables without primary key breaks replication
* [Revision #4ec3dca34b](https://github.com/MariaDB/server/commit/4ec3dca34b)\
  2022-09-29 13:40:51 -0600
  * [MDEV-28798](https://jira.mariadb.org/browse/MDEV-28798): Cosmetic Changes Only
* [Revision #d3e7dba329](https://github.com/MariaDB/server/commit/d3e7dba329)\
  2022-09-28 12:34:44 -0600
  * [MDEV-28798](https://jira.mariadb.org/browse/MDEV-28798): Previously Binlog Encrypted Master Segfaults on Binlog Dump with Using\_Gtid=Slave\_Pos
* [Revision #5dc9a6b455](https://github.com/MariaDB/server/commit/5dc9a6b455)\
  2023-04-21 13:46:14 -0700
  * [MDEV-31102](https://jira.mariadb.org/browse/MDEV-31102) Crash when pushing condition into view defined as union
* [Revision #d3e394b3b1](https://github.com/MariaDB/server/commit/d3e394b3b1)\
  2023-04-24 10:27:55 +0400
  * A cleanup for [MDEV-30968](https://jira.mariadb.org/browse/MDEV-30968) mariadb-backup does not copy Aria logs if aria\_log\_dir\_path is used
* [Revision #6dc6c22c14](https://github.com/MariaDB/server/commit/6dc6c22c14)\
  2023-04-21 18:49:52 -0700
  * [MDEV-31085](https://jira.mariadb.org/browse/MDEV-31085) Crash when processing multi-update using view with optimizer\_trace on
* [Revision #9f98a2acd7](https://github.com/MariaDB/server/commit/9f98a2acd7)\
  2023-04-13 15:42:53 +0400
  * [MDEV-30968](https://jira.mariadb.org/browse/MDEV-30968) mariadb-backup does not copy Aria logs if aria\_log\_dir\_path is used
* [Revision #da1c91fb92](https://github.com/MariaDB/server/commit/da1c91fb92)\
  2023-02-28 10:43:39 +1100
  * [MDEV-30713](https://jira.mariadb.org/browse/MDEV-30713) field length handling for CONNECT engine
* Merge [Revision #3d27f6d7f4](https://github.com/MariaDB/server/commit/3d27f6d7f4) 2023-04-21 09:10:58 +0200 - Merge branch '10.3' into 10.4
* [Revision #fc6e8a3d32](https://github.com/MariaDB/server/commit/fc6e8a3d32)\
  2023-01-31 14:14:55 -0800
  * Minimize unsafe C functions usage - replace strcat() and strcpy()
* [Revision #854e8b189e](https://github.com/MariaDB/server/commit/854e8b189e)\
  2023-04-19 15:53:26 +0300
  * [MDEV-28976](https://jira.mariadb.org/browse/MDEV-28976) fixup: A better fix
* [Revision #660afb1e9c](https://github.com/MariaDB/server/commit/660afb1e9c)\
  2023-04-13 16:26:03 +0530
  * [MDEV-30076](https://jira.mariadb.org/browse/MDEV-30076) ibuf\_insert tries to insert the entry for uncommitted index
* [Revision #2bfd04e314](https://github.com/MariaDB/server/commit/2bfd04e314)\
  2023-04-11 18:36:55 +0530
  * [MDEV-31025](https://jira.mariadb.org/browse/MDEV-31025) Redundant table alter fails when fixed column stored externally
* [Revision #b2bbc66a41](https://github.com/MariaDB/server/commit/b2bbc66a41)\
  2023-04-10 11:57:39 +0530
  * [MDEV-24011](https://jira.mariadb.org/browse/MDEV-24011) InnoDB: Failing assertion: index\_cache->words == NULL in fts0fts.cc line 551
* [Revision #d665186477](https://github.com/MariaDB/server/commit/d665186477)\
  2023-04-19 14:08:53 +0300
  * [MDEV-28976](https://jira.mariadb.org/browse/MDEV-28976): mtr must wait for server to actually die
* [Revision #feeeacc4d7](https://github.com/MariaDB/server/commit/feeeacc4d7)\
  2023-03-29 13:55:30 +0200
  * [MDEV-30955](https://jira.mariadb.org/browse/MDEV-30955) Explicit locks released too early in rollback path
* [Revision #bc3bfcf943](https://github.com/MariaDB/server/commit/bc3bfcf943)\
  2023-03-20 15:20:32 +0100
  * [MDEV-30862](https://jira.mariadb.org/browse/MDEV-30862) Assertion \`mode\_ == m\_high\_priority' failed
* [Revision #f575de39af](https://github.com/MariaDB/server/commit/f575de39af)\
  2023-04-11 09:39:40 +0200
  * rocksdb: Define \_GNU\_SOURCE during fallocate CMake probe
* [Revision #2e1c532bd2](https://github.com/MariaDB/server/commit/2e1c532bd2)\
  2023-03-24 13:04:05 +1100
  * alloca() fix
* [Revision #d1a4315f4c](https://github.com/MariaDB/server/commit/d1a4315f4c)\
  2023-04-13 07:49:35 +0200
  * [MDEV-30402](https://jira.mariadb.org/browse/MDEV-30402): Encrypted mariadb-backup SST breaks on distributions with newer socat
* [Revision #ef4d09948d](https://github.com/MariaDB/server/commit/ef4d09948d)\
  2023-04-11 21:21:45 -0700
  * [MDEV-20773](https://jira.mariadb.org/browse/MDEV-20773) Error from UPDATE when estimating selectivity of a range
* [Revision #7bcfa00a6a](https://github.com/MariaDB/server/commit/7bcfa00a6a)\
  2023-04-12 11:40:46 +0400
  * [MDEV-31039](https://jira.mariadb.org/browse/MDEV-31039) mariadb-backup: remove global variables ds\_data and ds\_meta
* [Revision #f83b7ae13d](https://github.com/MariaDB/server/commit/f83b7ae13d)\
  2023-04-06 07:50:23 +0300
  * [MDEV-26175](https://jira.mariadb.org/browse/MDEV-26175) : Assertion \`! thd->in\_sub\_stmt' failed in bool trans\_rollback\_stmt(THD\*)
* [Revision #4daea2f8b6](https://github.com/MariaDB/server/commit/4daea2f8b6)\
  2023-03-31 14:11:04 +0800
  * fix typo
* [Revision #ed2adc8c6f](https://github.com/MariaDB/server/commit/ed2adc8c6f)\
  2023-04-06 14:50:26 +0400
  * [MDEV-28190](https://jira.mariadb.org/browse/MDEV-28190) sql\_mode makes [MDEV-371](https://jira.mariadb.org/browse/MDEV-371) virtual column expressions nondeterministic
* [Revision #54715a1074](https://github.com/MariaDB/server/commit/54715a1074)\
  2023-04-06 09:57:58 +0400
  * [MDEV-30072](https://jira.mariadb.org/browse/MDEV-30072) Wrong ORDER BY for a partitioned prefix key + NOPAD
* [Revision #79e27a6bf9](https://github.com/MariaDB/server/commit/79e27a6bf9)\
  2023-04-05 23:34:03 +0200
  * [MDEV-25887](https://jira.mariadb.org/browse/MDEV-25887) "Got notification message from PID xxxx, but reception only permitted for main PID yyyy" in systemd during SST
* [Revision #06393cd8f8](https://github.com/MariaDB/server/commit/06393cd8f8)\
  2023-04-04 20:12:36 +0200
  * [MDEV-29602](https://jira.mariadb.org/browse/MDEV-29602) : Galera debug build crashes when the spider plugin is enabled
* [Revision #8f9bb82640](https://github.com/MariaDB/server/commit/8f9bb82640)\
  2023-03-31 05:41:00 +0400
  * [MDEV-30971](https://jira.mariadb.org/browse/MDEV-30971) Add a new system variable aria\_data\_home\_dir
* [Revision #8020b1bd73](https://github.com/MariaDB/server/commit/8020b1bd73)\
  2023-03-31 17:20:03 +0400
  * [MDEV-30034](https://jira.mariadb.org/browse/MDEV-30034) UNIQUE USING HASH accepts duplicate entries for tricky collations
* [Revision #0cc1694e9c](https://github.com/MariaDB/server/commit/0cc1694e9c)\
  2023-03-31 19:17:56 +0000
  * Make 'move\_file' command more reliable in 3 innodb tests
* [Revision #da73db2382](https://github.com/MariaDB/server/commit/da73db2382)\
  2023-03-13 17:27:28 -0400
  * Make 'move\_file' command more reliable in mysqltest
* [Revision #0a6343909f](https://github.com/MariaDB/server/commit/0a6343909f)\
  2023-04-01 15:58:14 +0200
  * ensure that STRING\_WITH\_LEN is only used with string literals
* [Revision #6a10468ed3](https://github.com/MariaDB/server/commit/6a10468ed3)\
  2023-03-15 22:03:51 +0100
  * [MDEV-13255](https://jira.mariadb.org/browse/MDEV-13255) main.status failed in buildbot
* [Revision #1767390be4](https://github.com/MariaDB/server/commit/1767390be4)\
  2023-04-01 14:42:05 +0200
  * Fix passing correct length of string in command print.
* [Revision #3b64244070](https://github.com/MariaDB/server/commit/3b64244070)\
  2023-03-24 16:06:11 +0000
  * Handle meaningless addr2line results and increase timeout
* [Revision #eaebe8b560](https://github.com/MariaDB/server/commit/eaebe8b560)\
  2023-03-31 12:48:13 +0200
  * [MDEV-25045](https://jira.mariadb.org/browse/MDEV-25045) : Assertion \`client\_state\_.mode() != wsrep::client\_state::m\_toi' failed in int wsrep::transaction::before\_commit()
* [Revision #cadc3efcdd](https://github.com/MariaDB/server/commit/cadc3efcdd)\
  2023-02-13 18:14:50 +0200
  * [MDEV-27317](https://jira.mariadb.org/browse/MDEV-27317) wsrep\_checkpoint order violation due to certification failure
* [Revision #f70de1451b](https://github.com/MariaDB/server/commit/f70de1451b)\
  2023-03-11 11:06:03 +0100
  * [MDEV-30351](https://jira.mariadb.org/browse/MDEV-30351) crash in Item\_func\_left::val\_str
* [Revision #a6780df49b](https://github.com/MariaDB/server/commit/a6780df49b)\
  2023-03-29 16:49:10 +0300
  * [MDEV-30453](https://jira.mariadb.org/browse/MDEV-30453) Setting innodb\_buffer\_pool\_filename to an empty string attempts to delete the data directory on shutdown
* [Revision #03b4a2d6e5](https://github.com/MariaDB/server/commit/03b4a2d6e5)\
  2023-03-29 11:56:44 +0400
  * [MDEV-26765](https://jira.mariadb.org/browse/MDEV-26765) UNIX\_TIMESTAMP(CURRENT\_TIME()) return null ?!?
* [Revision #113bef50e3](https://github.com/MariaDB/server/commit/113bef50e3)\
  2023-03-23 09:41:45 +1100
  * [MDEV-30581](https://jira.mariadb.org/browse/MDEV-30581) Add a testcase for [MDEV-29904](https://jira.mariadb.org/browse/MDEV-29904)
* [Revision #4c226c1850](https://github.com/MariaDB/server/commit/4c226c1850)\
  2023-03-23 16:26:17 +0300
  * [MDEV-29050](https://jira.mariadb.org/browse/MDEV-29050) mariadb-backup issues error messages during InnoDB tablespaces export on partial backup preparing
* [Revision #d575b07c86](https://github.com/MariaDB/server/commit/d575b07c86)\
  2023-03-06 23:02:03 +0530
  * [MDEV-24453](https://jira.mariadb.org/browse/MDEV-24453) Added support for a 5th --verbose parameter in mariadb-upgrade to show mysql results for mysql\_fix\_privilege\_tables
* [Revision #f33fc2fae5](https://github.com/MariaDB/server/commit/f33fc2fae5)\
  2023-03-22 21:59:18 -0700
  * [MDEV-30539](https://jira.mariadb.org/browse/MDEV-30539) EXPLAIN EXTENDED: no message with queries for DML statements
* [Revision #011261f4e9](https://github.com/MariaDB/server/commit/011261f4e9)\
  2023-03-24 08:52:28 +1100
  * sql\_class: sprintf -> snprintf
* [Revision #91e5e47a50](https://github.com/MariaDB/server/commit/91e5e47a50)\
  2023-03-23 21:07:32 +0300
  * [MDEV-30421](https://jira.mariadb.org/browse/MDEV-30421) more tests cleaned up
* [Revision #bdf5580611](https://github.com/MariaDB/server/commit/bdf5580611)\
  2023-03-23 21:07:32 +0300
  * [MDEV-30421](https://jira.mariadb.org/browse/MDEV-30421) rpl\_parallel.test cleanup
* [Revision #c596ad734d](https://github.com/MariaDB/server/commit/c596ad734d)\
  2023-03-08 12:59:50 +0100
  * [MDEV-30269](https://jira.mariadb.org/browse/MDEV-30269): Remove rpl\_semi\_sync\_\[slave,master] usage in code
* [Revision #ff3d4395d8](https://github.com/MariaDB/server/commit/ff3d4395d8)\
  2023-03-22 14:31:00 +0200
  * [MDEV-30882](https://jira.mariadb.org/browse/MDEV-30882) Crash on ROLLBACK in a ROW\_FORMAT=COMPRESSED table
* [Revision #7c91082e39](https://github.com/MariaDB/server/commit/7c91082e39)\
  2023-01-18 11:51:28 +1100
  * [MDEV-27912](https://jira.mariadb.org/browse/MDEV-27912) Fixing inconsistency w.r.t. expect files in tests.
* [Revision #e0560fc4cf](https://github.com/MariaDB/server/commit/e0560fc4cf)\
  2023-03-21 14:36:38 +0200
  * Remove a bogus UNIV\_ZIP\_DEBUG check
* [Revision #c73a65f55b](https://github.com/MariaDB/server/commit/c73a65f55b)\
  2023-03-21 14:33:54 +0200
  * [MDEV-29692](https://jira.mariadb.org/browse/MDEV-29692) Assertion \`(writeptr + (i \* size)) != local\_frame' failed upon IMPORT TABLESPACE
* [Revision #f8c3d4c2d5](https://github.com/MariaDB/server/commit/f8c3d4c2d5)\
  2023-03-17 18:51:33 +0300
  * [MDEV-28187](https://jira.mariadb.org/browse/MDEV-28187) mariadb-backup doesn't utilise innodb-undo-log-directory (if specified as a relative path) during copy-back operation
* [Revision #a2cb6d8760](https://github.com/MariaDB/server/commit/a2cb6d8760)\
  2023-03-20 16:47:53 +0200
  * Update feedback plugin URL to use feedback.mariadb.org subdomain
* [Revision #26e4ba5eb5](https://github.com/MariaDB/server/commit/26e4ba5eb5)\
  2023-03-20 14:12:52 +0200
  * Fix cmake -DWITH\_INNODB\_EXTRA\_DEBUG (UNIV\_ZIP\_DEBUG)
* [Revision #d4339620be](https://github.com/MariaDB/server/commit/d4339620be)\
  2023-03-05 15:12:13 +0200
  * [MDEV-30780](https://jira.mariadb.org/browse/MDEV-30780) optimistic parallel slave hangs after hit an error
* [Revision #dfdcd7ffab](https://github.com/MariaDB/server/commit/dfdcd7ffab)\
  2023-03-13 15:41:06 +0530
  * [MDEV-26198](https://jira.mariadb.org/browse/MDEV-26198) Assertion \`0' failed in row\_log\_table\_apply\_op during redundant table rebuild
* [Revision #8b37e79a39](https://github.com/MariaDB/server/commit/8b37e79a39)\
  2023-03-13 17:41:06 +0100
  * Post-[MDEV-30700](https://jira.mariadb.org/browse/MDEV-30700): moving alloca() definitions from all \*.h files to new header file
* [Revision #8145b308b0](https://github.com/MariaDB/server/commit/8145b308b0)\
  2023-03-10 18:14:45 +0100
  * [MDEV-30826](https://jira.mariadb.org/browse/MDEV-30826) Invalid data on mysql.host segfaults the server after an upgrade to 10.4
* [Revision #2ac832838f](https://github.com/MariaDB/server/commit/2ac832838f)\
  2023-03-07 20:05:12 +0100
  * post fix for "move alloca() definition from all \*.h files to one new header file"
* [Revision #94ed30e505](https://github.com/MariaDB/server/commit/94ed30e505)\
  2023-02-10 12:58:57 +1100
  * [MDEV-30613](https://jira.mariadb.org/browse/MDEV-30613) output\_core\_info crashes in my\_read()
* [Revision #2f6bb9cda5](https://github.com/MariaDB/server/commit/2f6bb9cda5)\
  2023-02-20 14:11:13 +0100
  * [MDEV-30698](https://jira.mariadb.org/browse/MDEV-30698) Cover missing test cases for mariadb-binlog options --raw \[and] --flashback
* [Revision #7300ab32cc](https://github.com/MariaDB/server/commit/7300ab32cc)\
  2023-03-02 12:05:36 +0100
  * Update handling of mysqlbinlog's `die()` function
* [Revision #f0ab1a28c9](https://github.com/MariaDB/server/commit/f0ab1a28c9)\
  2023-02-20 14:10:53 +0100
  * [MDEV-30697](https://jira.mariadb.org/browse/MDEV-30697): Memory leak detected when mariadb-binlog is used with option flashback
* [Revision #fb8c1762ad](https://github.com/MariaDB/server/commit/fb8c1762ad)\
  2021-02-07 21:11:53 +0200
  * Ensure that mysqlbinlog frees all memory at exit
* [Revision #8b0f766c6c](https://github.com/MariaDB/server/commit/8b0f766c6c)\
  2023-02-23 22:43:14 +0000
  * Minimize unsafe C functions usage
* [Revision #e240e2749e](https://github.com/MariaDB/server/commit/e240e2749e)\
  2023-03-03 17:33:07 -0800
  * [MDEV-30758](https://jira.mariadb.org/browse/MDEV-30758) mariadb-backup --help only lists server groups read in configuration
* [Revision #46a7e96339](https://github.com/MariaDB/server/commit/46a7e96339)\
  2023-03-02 14:21:59 +0100
  * move alloca() definition from all \*.h files to one new header file
* [Revision #66b21ed540](https://github.com/MariaDB/server/commit/66b21ed540)\
  2023-03-06 15:32:25 +0200
  * [MDEV-30567](https://jira.mariadb.org/browse/MDEV-30567) rec\_get\_offsets() is not optimal
* [Revision #99ee200b8b](https://github.com/MariaDB/server/commit/99ee200b8b)\
  2023-03-02 23:37:17 +0530
  * [MDEV-24005](https://jira.mariadb.org/browse/MDEV-24005) Updated the --use-memory option usage message in mariadb-backup help command
* [Revision #ccec9b1de9](https://github.com/MariaDB/server/commit/ccec9b1de9)\
  2023-03-01 22:49:27 -0800
  * [MDEV-30706](https://jira.mariadb.org/browse/MDEV-30706) Different results of selects from view and CTE with same definition [MDEV-30668](https://jira.mariadb.org/browse/MDEV-30668) Set function aggregated in outer select used in view definition
* [Revision #a6a906d766](https://github.com/MariaDB/server/commit/a6a906d766)\
  2022-11-25 12:54:24 +0100
  * [MDEV-26831](https://jira.mariadb.org/browse/MDEV-26831) fallout: fix problems of name resolution cache
* [Revision #7bdd878ae4](https://github.com/MariaDB/server/commit/7bdd878ae4)\
  2023-02-23 23:56:44 +0000
  * Fix few vulnerabilities found by Cppcheck
* [Revision #acfb5dfd97](https://github.com/MariaDB/server/commit/acfb5dfd97)\
  2023-03-01 20:46:18 +0000
  * [MDEV-22683](https://jira.mariadb.org/browse/MDEV-22683): Ensure system tables are correctly upgraded in [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/)
* [Revision #965bdf3e66](https://github.com/MariaDB/server/commit/965bdf3e66)\
  2023-02-28 10:49:25 +0400
  * [MDEV-30746](https://jira.mariadb.org/browse/MDEV-30746) Regression in ucs2\_general\_mysql500\_ci
* [Revision #841e8877cc](https://github.com/MariaDB/server/commit/841e8877cc)\
  2023-02-27 10:51:22 -0800
  * [MDEV-28603](https://jira.mariadb.org/browse/MDEV-28603) Invalid view when its definition uses TVC as single-value subquery
* [Revision #839c7fcf38](https://github.com/MariaDB/server/commit/839c7fcf38)\
  2023-02-23 19:56:07 +0530
  * [MDEV-30597](https://jira.mariadb.org/browse/MDEV-30597) Assertion \`flag == 1' failed in row\_build\_index\_entry\_low
* [Revision #a777a8a6a3](https://github.com/MariaDB/server/commit/a777a8a6a3)\
  2023-02-02 19:29:03 +0100
  * KILL USER and missing privileges
* [Revision #90c39c5a50](https://github.com/MariaDB/server/commit/90c39c5a50)\
  2023-02-01 20:20:57 +0100
  * hopefully the last case of walk-and-delete HASH antipattern
* [Revision #2e6a9886a9](https://github.com/MariaDB/server/commit/2e6a9886a9)\
  2023-02-01 18:56:10 +0100
  * [MDEV-30526](https://jira.mariadb.org/browse/MDEV-30526) Assertion \`rights == merged->cols' failed in update\_role\_columns
* [Revision #3c6f108540](https://github.com/MariaDB/server/commit/3c6f108540)\
  2023-01-31 16:07:27 +0100
  * Revert "ignore changes in submodules when committing everything"
* [Revision #358635bbad](https://github.com/MariaDB/server/commit/358635bbad)\
  2022-10-31 15:51:00 +0000
  * [MDEV-29782](https://jira.mariadb.org/browse/MDEV-29782) CONNECT YEAR type conversion fix
* [Revision #476b24d084](https://github.com/MariaDB/server/commit/476b24d084)\
  2023-02-16 14:19:33 +0200
  * [MDEV-20057](https://jira.mariadb.org/browse/MDEV-20057) Distinct SUM on CROSS JOIN and grouped returns wrong result
* [Revision #bd0d7ea540](https://github.com/MariaDB/server/commit/bd0d7ea540)\
  2023-02-08 12:57:03 +0100
  * MDBF-534: Coverity scan: fix client folder
* [Revision #24911a34b3](https://github.com/MariaDB/server/commit/24911a34b3)\
  2023-02-08 12:24:25 +0100
  * MDBF-534: Coverity scan: fix client folder
* [Revision #023bb2fc20](https://github.com/MariaDB/server/commit/023bb2fc20)\
  2023-02-13 13:39:25 +0100
  * MDBF-534: Coverity scan: fix client folder
* [Revision #ff7e0977f3](https://github.com/MariaDB/server/commit/ff7e0977f3)\
  2023-02-08 05:26:34 +0100
  * MDBF-534: Coverity scan: fix client folder
* [Revision #f0ea22a1e2](https://github.com/MariaDB/server/commit/f0ea22a1e2)\
  2023-02-08 05:16:29 +0100
  * MDBF-534: Coverity scan: fix client folder
* [Revision #4878891193](https://github.com/MariaDB/server/commit/4878891193)\
  2023-02-08 03:18:14 +0100
  * MDBF-534: Coverity scan: fix client folder
* [Revision #560c15c44b](https://github.com/MariaDB/server/commit/560c15c44b)\
  2023-02-04 22:10:49 +0100
  * MDBF-534: Coverity scan: fix client folder
* [Revision #9ab16e7f3e](https://github.com/MariaDB/server/commit/9ab16e7f3e)\
  2023-01-15 19:12:05 +0100
  * include/ssl\_compat.h: fix build with libressl >= 3.5.0
* [Revision #702d1af32c](https://github.com/MariaDB/server/commit/702d1af32c)\
  2023-02-15 01:18:26 +0530
  * [MDEV-30615](https://jira.mariadb.org/browse/MDEV-30615) Can't read from I\_S.INNODB\_SYS\_INDEXES when having a discarded tablesace
* [Revision #2e6872791a](https://github.com/MariaDB/server/commit/2e6872791a)\
  2023-02-02 17:12:39 +0200
  * [MDEV-30218](https://jira.mariadb.org/browse/MDEV-30218): Incorrect optimization for rowid\_filtering, correction
* [Revision #d1a46c68cd](https://github.com/MariaDB/server/commit/d1a46c68cd)\
  2023-01-31 13:14:53 -0800
  * [MDEV-30218](https://jira.mariadb.org/browse/MDEV-30218) Incorrect optimization for rowid\_filtering
* [Revision #03c9a4ef4a](https://github.com/MariaDB/server/commit/03c9a4ef4a)\
  2022-12-07 16:54:27 +0000
  * [MDEV-29091](https://jira.mariadb.org/browse/MDEV-29091): Correct event\_name in PFS for wait caused by FOR UPDATE
* [Revision #fab166532f](https://github.com/MariaDB/server/commit/fab166532f)\
  2023-02-09 18:41:45 +1100
  * [MDEV-30630](https://jira.mariadb.org/browse/MDEV-30630) locale: Chinese error messages for ZH\_CN
* [Revision #60f96b58e4](https://github.com/MariaDB/server/commit/60f96b58e4)\
  2022-12-08 20:46:26 +0000
  * Backport GitLab CI to earlier branches
* [Revision #81faf41786](https://github.com/MariaDB/server/commit/81faf41786)\
  2023-02-14 14:20:48 +0530
  * [MDEV-30597](https://jira.mariadb.org/browse/MDEV-30597) Assertion \`flag == 1' failed in row\_build\_index\_entry\_low
* [Revision #7170db3c3a](https://github.com/MariaDB/server/commit/7170db3c3a)\
  2023-02-13 16:54:13 +0300
  * [MDEV-30596](https://jira.mariadb.org/browse/MDEV-30596): Assertion 'pushed\_rowid\_filter != null ...' failed
* [Revision #a80eb9832e](https://github.com/MariaDB/server/commit/a80eb9832e)\
  2023-02-12 16:40:40 +0100
  * [MDEV-24538](https://jira.mariadb.org/browse/MDEV-24538): JSON\_LENGTH does not return error upon wrong number of parameters
* [Revision #cacea31687](https://github.com/MariaDB/server/commit/cacea31687)\
  2023-02-09 12:49:17 +1100
  * [MDEV-30621](https://jira.mariadb.org/browse/MDEV-30621): Türkiye is the correct current country naming
* [Revision #eecd4f1459](https://github.com/MariaDB/server/commit/eecd4f1459)\
  2023-02-08 10:32:35 -0700
  * [MDEV-30608](https://jira.mariadb.org/browse/MDEV-30608): rpl.rpl\_delayed\_parallel\_slave\_sbm sometimes fails with Seconds\_Behind\_Master should not have used second transaction timestamp
* [Revision #c63768425b](https://github.com/MariaDB/server/commit/c63768425b)\
  2023-02-08 19:24:15 -0800
  * [MDEV-30586](https://jira.mariadb.org/browse/MDEV-30586) DELETE with aggregation in subquery of WHERE returns bogus error
* [Revision #08c852026d](https://github.com/MariaDB/server/commit/08c852026d)\
  2023-02-07 13:57:20 +0200
  * Apply clang-tidy to remove empty constructors / destructors
* [Revision #8dab661416](https://github.com/MariaDB/server/commit/8dab661416)\
  2023-02-09 10:32:25 +0100
  * [MDEV-30624](https://jira.mariadb.org/browse/MDEV-30624) HeidiSQL 12.3
* [Revision #aa028e02c3](https://github.com/MariaDB/server/commit/aa028e02c3)\
  2023-02-09 09:15:08 +0100
  * Update Windows time zone mappings using latest CLDR data
* [Revision #493f2bca76](https://github.com/MariaDB/server/commit/493f2bca76)\
  2023-02-07 14:04:37 +0100
  * Add more workaround atop existing WolfSSL 5.5.4 workaround to compile ASAN on buildbot
* [Revision #785386c807](https://github.com/MariaDB/server/commit/785386c807)\
  2023-02-02 10:03:11 +1100
  * innodb: cmake - sched\_getcpu removed - not used
* [Revision #17423c6c51](https://github.com/MariaDB/server/commit/17423c6c51)\
  2023-02-03 11:51:20 +1100
  * [MDEV-30554](https://jira.mariadb.org/browse/MDEV-30554) RockDB libatomic linking on riscv64
* [Revision #ecc93c9824](https://github.com/MariaDB/server/commit/ecc93c9824)\
  2023-02-03 16:00:11 +1100
  * [MDEV-30492](https://jira.mariadb.org/browse/MDEV-30492) Crash when use mariadb-backup.exe with config 'innodb\_flush\_method=async\_unbuffered'
* [Revision #762fe015c1](https://github.com/MariaDB/server/commit/762fe015c1)\
  2023-02-04 16:35:30 +1100
  * [MDEV-30558](https://jira.mariadb.org/browse/MDEV-30558): ER\_KILL\_{,QUERY\_}DENIED\_ERROR - normalize id type
* Merge [Revision #40adf52d1c](https://github.com/MariaDB/server/commit/40adf52d1c) 2023-02-06 20:12:55 +0100 - Merge branch '10.4.28' into 10.4
* [Revision #d8c7dc2813](https://github.com/MariaDB/server/commit/d8c7dc2813)\
  2023-02-06 09:34:19 -0500
  * bump the VERSION
* [Revision #f4b900e6fa](https://github.com/MariaDB/server/commit/f4b900e6fa)\
  2023-01-05 12:21:20 +1100
  * [MDEV-24301](https://jira.mariadb.org/browse/MDEV-24301) \[Warning] Aborted connection (This connection closed normally)
* [Revision #bef20b5f36](https://github.com/MariaDB/server/commit/bef20b5f36)\
  2023-02-02 22:38:32 -0800
  * [MDEV-30538](https://jira.mariadb.org/browse/MDEV-30538) Plans for SELECT and multi-table UPDATE/DELETE unexpectedly differ
* [Revision #0845bce0d9](https://github.com/MariaDB/server/commit/0845bce0d9)\
  2023-02-03 16:57:53 +0400
  * [MDEV-30556](https://jira.mariadb.org/browse/MDEV-30556) UPPER() returns an empty string for U+0251 in Unicode-5.2.0+ collations for utf8
* [Revision #b05218e08f](https://github.com/MariaDB/server/commit/b05218e08f)\
  2023-01-30 08:55:35 +0200
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster
* [Revision #844ddb1109](https://github.com/MariaDB/server/commit/844ddb1109)\
  2023-01-26 14:34:12 +0200
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
