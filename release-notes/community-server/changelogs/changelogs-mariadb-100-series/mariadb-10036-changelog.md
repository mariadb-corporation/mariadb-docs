# MariaDB 10.0.36 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.36)[Release Notes](../../old-releases/10.0/10.0.36.md)[Changelog](mariadb-10036-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 1 Aug 2018

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.36.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #e023f9a4d5](https://github.com/MariaDB/server/commit/e023f9a4d5)\
  2018-07-31 15:19:01 +0300
  * Unstable tests for 10.0.36 release, latest additions
* [Revision #e52315a4a2](https://github.com/MariaDB/server/commit/e52315a4a2)\
  2018-07-30 18:06:30 +0300
  * [MDEV-16855](https://jira.mariadb.org/browse/MDEV-16855) Fix fts\_sync\_synchronization in InnoDB
* [Revision #5ed2da9587](https://github.com/MariaDB/server/commit/5ed2da9587)\
  2018-07-30 16:28:20 +0300
  * Apply the 5.6.40 security fixes to XtraDB
* Merge [Revision #7c773abdf7](https://github.com/MariaDB/server/commit/7c773abdf7) 2018-07-30 15:44:31 +0300 - Merge 5.5 into 10.0
* Merge [Revision #4c21c367b3](https://github.com/MariaDB/server/commit/4c21c367b3) 2018-07-30 15:19:26 +0300 - Merge InnoDB MySQL 5.6.41 to 10.0
* [Revision #29ddc6e9e3](https://github.com/MariaDB/server/commit/29ddc6e9e3)\
  2018-05-17 16:53:30 +0530
  * Bug #27326796 - MYSQL CRASH WITH INNODB ASSERTION FAILURE IN FILE PARS0PARS.CC
* Merge [Revision #91181b225c](https://github.com/MariaDB/server/commit/91181b225c) 2018-07-30 15:09:25 +0300 - Merge 5.5 into 10.0
* [Revision #d17e9a02c4](https://github.com/MariaDB/server/commit/d17e9a02c4)\
  2018-07-30 14:05:24 +0300
  * Fix InnoDB/XtraDB warnings by GCC 8.2.0
* [Revision #8bdd125067](https://github.com/MariaDB/server/commit/8bdd125067)\
  2018-07-30 13:13:43 +0300
  * [MDEV-16851](https://jira.mariadb.org/browse/MDEV-16851) On schema mismatch in IMPORT TABLESPACE, display ROW\_FORMAT in clear text
* [Revision #340963351c](https://github.com/MariaDB/server/commit/340963351c)\
  2018-07-30 10:39:42 +0300
  * Use a more precise argument for memset()
* [Revision #c631060713](https://github.com/MariaDB/server/commit/c631060713)\
  2018-07-24 23:45:55 -0700
  * [MDEV-16820](https://jira.mariadb.org/browse/MDEV-16820) Lost 'Impossible where' from query with inexpensive subquery
* [Revision #1bda5e3a8f](https://github.com/MariaDB/server/commit/1bda5e3a8f)\
  2018-07-24 20:09:42 +0300
  * List of unstable tests for 10.0.36 release
* [Revision #9fbe360e9f](https://github.com/MariaDB/server/commit/9fbe360e9f)\
  2018-07-24 18:24:21 +0200
  * make plugins.processlist more robust
* [Revision #e0139c2b92](https://github.com/MariaDB/server/commit/e0139c2b92)\
  2018-07-24 18:16:41 +0200
  * fix plugins.processlist
* Merge [Revision #5e67567b15](https://github.com/MariaDB/server/commit/5e67567b15) 2018-07-24 10:42:35 +0200 - Merge pull request #726 from fauust/10.0-[MDEV-14672](https://jira.mariadb.org/browse/MDEV-14672)
* Merge [Revision #4645a66316](https://github.com/MariaDB/server/commit/4645a66316) 2018-06-13 21:11:18 +0200 - Merge branch '10.0-[MDEV-14672](https://jira.mariadb.org/browse/MDEV-14672)' of github.com:fauust/mariadb into 10.0-[MDEV-14672](https://jira.mariadb.org/browse/MDEV-14672)
* [Revision #eee5bd9a2e](https://github.com/MariaDB/server/commit/eee5bd9a2e)\
  2018-04-03 10:33:11 -0300
  * Package dependency case problem
* [Revision #d4e9473923](https://github.com/MariaDB/server/commit/d4e9473923)\
  2018-04-03 10:33:11 -0300
  * Package dependency case problem
* Merge [Revision #304440b014](https://github.com/MariaDB/server/commit/304440b014) 2018-07-23 11:55:18 +0200 - Merge branch '5.5' into bb-10.0-merge-sanja
* [Revision #d57ddaa190](https://github.com/MariaDB/server/commit/d57ddaa190)\
  2018-07-16 15:12:38 +0200
  * [MDEV-15551](https://jira.mariadb.org/browse/MDEV-15551) Server hangs or assertion \`strcmp(share->unique\_file\_name,filename) || share->last\_version' fails in test\_if\_reopen or unexpected ER\_LOCK\_DEADLOCK
* [Revision #5c744bb535](https://github.com/MariaDB/server/commit/5c744bb535)\
  2018-07-14 13:48:50 +0200
  * [MDEV-14882](https://jira.mariadb.org/browse/MDEV-14882) mysql\_upgrade performs unnecessary conversions back and forth
* [Revision #40f29ecbf1](https://github.com/MariaDB/server/commit/40f29ecbf1)\
  2018-07-14 00:51:23 +0200
  * [MDEV-13397](https://jira.mariadb.org/browse/MDEV-13397) MariaDB upgrade fail when using default\_time\_zone
* [Revision #33eccb5776](https://github.com/MariaDB/server/commit/33eccb5776)\
  2018-07-13 21:37:22 +0200
  * [MDEV-11790](https://jira.mariadb.org/browse/MDEV-11790) WITHOUT\_SERVER installs mysqld\_safe\_helper
* [Revision #bd5cf02bbe](https://github.com/MariaDB/server/commit/bd5cf02bbe)\
  2018-07-13 16:54:47 +0200
  * [MDEV-11741](https://jira.mariadb.org/browse/MDEV-11741) handler::ha\_reset(): Assertion \`bitmap\_is\_set\_all(\&table->s->all\_set)' failed or server crash in mi\_reset or buffer overrun or unexpected ER\_CANT\_REMOVE\_ALL\_FIELDS
* [Revision #0b3e28a4cd](https://github.com/MariaDB/server/commit/0b3e28a4cd)\
  2018-07-12 21:58:11 +0200
  * [MDEV-8941](https://jira.mariadb.org/browse/MDEV-8941) Compile on Solaris (SPARC) fails with errors in filamvct.cpp
* [Revision #e2ac4098ed](https://github.com/MariaDB/server/commit/e2ac4098ed)\
  2018-07-19 13:02:14 +0400
  * Simplify caseup() and casedn() in charsets
* [Revision #ab58493db2](https://github.com/MariaDB/server/commit/ab58493db2)\
  2018-07-19 09:55:19 +0400
  * [MDEV-13118](https://jira.mariadb.org/browse/MDEV-13118) Wrong results with LOWER and UPPER and subquery
* [Revision #ada54101a7](https://github.com/MariaDB/server/commit/ada54101a7)\
  2018-05-30 16:25:44 +0530
  * [MDEV-9266](https://jira.mariadb.org/browse/MDEV-9266) Creating index on temporaray table breaks replication
* Merge [Revision #e5c26fdfab](https://github.com/MariaDB/server/commit/e5c26fdfab) 2018-07-17 16:56:21 +0200 - Merge branch '5.5' into bb-10.0-merge
* [Revision #1fd84f9129](https://github.com/MariaDB/server/commit/1fd84f9129)\
  2018-07-13 23:03:57 -0700
  * [MDEV-16760](https://jira.mariadb.org/browse/MDEV-16760) CREATE OR REPLACE TABLE never updates statistical tables
* [Revision #c89bb15c31](https://github.com/MariaDB/server/commit/c89bb15c31)\
  2018-07-13 17:48:30 -0700
  * [MDEV-16757](https://jira.mariadb.org/browse/MDEV-16757) Memory leak after adding manually min/max statistical data for blob column
* [Revision #ad9d1e8c3f](https://github.com/MariaDB/server/commit/ad9d1e8c3f)\
  2018-07-11 02:28:42 +0530
  * [MDEV-16552](https://jira.mariadb.org/browse/MDEV-16552): \[10.0] ASAN global-buffer-overflow in is\_stat\_table / statistics\_for\_tables\_is\_needed
* [Revision #a2c0376e08](https://github.com/MariaDB/server/commit/a2c0376e08)\
  2018-07-02 17:45:19 +0100
  * Fix build on non-Windows, broken by 0897a25c0f0b9b865
* [Revision #8c5d64dafb](https://github.com/MariaDB/server/commit/8c5d64dafb)\
  2018-07-02 15:22:52 +0100
  * Post-fix after [MDEV-8540](https://jira.mariadb.org/browse/MDEV-8540) - do not close stdin on Windows.
* [Revision #0897a25c0f](https://github.com/MariaDB/server/commit/0897a25c0f)\
  2018-07-02 15:02:31 +0100
  * [MDEV-16596](https://jira.mariadb.org/browse/MDEV-16596) : Windows - redo log does not work on native 4K sector disks.
* [Revision #3d4beee1a9](https://github.com/MariaDB/server/commit/3d4beee1a9)\
  2018-06-28 11:59:25 +0200
  * remove double-counting
* [Revision #bf4244d1a0](https://github.com/MariaDB/server/commit/bf4244d1a0)\
  2018-06-27 17:01:09 +0400
  * [MDEV-8540](https://jira.mariadb.org/browse/MDEV-8540) - Crash on server shutdown since 10.0.16
* Merge [Revision #cc8772f33e](https://github.com/MariaDB/server/commit/cc8772f33e) 2018-06-26 17:02:46 +0300 - [MDEV-15953](https://jira.mariadb.org/browse/MDEV-15953) Alter InnoDB Partitioned Table ignores pre-existing DATA DIRECTORY attribute
* [Revision #ff8b3c8df8](https://github.com/MariaDB/server/commit/ff8b3c8df8)\
  2018-06-23 13:49:36 +0300
  * [MDEV-15953](https://jira.mariadb.org/browse/MDEV-15953) Alter InnoDB Partitioned Table Moves Files (which were originally not in the datadir) to the datadir
* [Revision #28e1f1453f](https://github.com/MariaDB/server/commit/28e1f1453f)\
  2018-06-19 18:14:47 +0300
  * [MDEV-15242](https://jira.mariadb.org/browse/MDEV-15242) Poor RBR update performance with partitioned tables
* [Revision #364a20fe0b](https://github.com/MariaDB/server/commit/364a20fe0b)\
  2018-06-23 19:36:26 -0700
  * [MDEV-16507](https://jira.mariadb.org/browse/MDEV-16507) SIGSEGV when use\_stat\_tables = preferably and optimizer\_use\_condition\_selectivity = 4
* Merge [Revision #d8192f5495](https://github.com/MariaDB/server/commit/d8192f5495) 2018-06-21 00:44:10 +0200 - Merge branch '5.5' into 10.0
* Merge [Revision #6c08ff3eb7](https://github.com/MariaDB/server/commit/6c08ff3eb7) 2018-06-20 16:55:24 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #5f2a67a6c3](https://github.com/MariaDB/server/commit/5f2a67a6c3)\
  2018-06-20 02:36:00 +0530
  * [MDEV-15247](https://jira.mariadb.org/browse/MDEV-15247): Crash when SET NAMES 'utf8' is set
* Merge [Revision #c450f7d8d5](https://github.com/MariaDB/server/commit/c450f7d8d5) 2018-06-19 14:03:41 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #3661d98822](https://github.com/MariaDB/server/commit/3661d98822)\
  2018-06-13 20:31:40 +0200
  * fix SHOW PROCESSLIST for --embedded
* [Revision #51254da52c](https://github.com/MariaDB/server/commit/51254da52c)\
  2018-06-12 12:37:28 +0200
  * [MDEV-15359](https://jira.mariadb.org/browse/MDEV-15359) Thread stay in "cleaning up" status after finishing
* [Revision #d2e1ed8b93](https://github.com/MariaDB/server/commit/d2e1ed8b93)\
  2018-06-13 08:33:25 +0300
  * Fix innodb.rename\_table for embedded
* Merge [Revision #170bec36c0](https://github.com/MariaDB/server/commit/170bec36c0) 2018-06-12 17:59:31 +0300 - Merge branch '5.5' into 10.0
* [Revision #6b8d34fe0d](https://github.com/MariaDB/server/commit/6b8d34fe0d)\
  2018-06-12 12:36:51 +0400
  * [MDEV-14668](https://jira.mariadb.org/browse/MDEV-14668) ADD PRIMARY KEY IF NOT EXISTS on composite key.
* [Revision #0ad9c3a016](https://github.com/MariaDB/server/commit/0ad9c3a016)\
  2018-06-11 13:02:47 +0300
  * [MDEV-16456](https://jira.mariadb.org/browse/MDEV-16456) InnoDB error "returned OS error 71" complains about wrong path
* [Revision #24d7cbe1e0](https://github.com/MariaDB/server/commit/24d7cbe1e0)\
  2018-06-10 16:26:57 +0300
  * Ensure TokuDB compiles both on Linux and OS X
* [Revision #e5a3d24b87](https://github.com/MariaDB/server/commit/e5a3d24b87)\
  2018-06-10 21:45:05 +0300
  * Followup for make TokuDB compile with GCC-8
* [Revision #719ed09e5e](https://github.com/MariaDB/server/commit/719ed09e5e)\
  2018-06-10 18:25:11 +0300
  * Update test results post-merge
* Merge [Revision #3ead951180](https://github.com/MariaDB/server/commit/3ead951180) 2018-06-10 17:16:27 +0300 - Merge branch '5.5' into 10.0
* [Revision #7053e26e18](https://github.com/MariaDB/server/commit/7053e26e18)\
  2018-05-10 10:00:51 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Fix TokuDB build issues on macOS 10.13.4
* [Revision #8f82c48443](https://github.com/MariaDB/server/commit/8f82c48443)\
  2018-05-09 16:29:18 +0300
  * [MDEV-15778](https://jira.mariadb.org/browse/MDEV-15778): Restore file permissions lost in merge
* [Revision #cd33280b68](https://github.com/MariaDB/server/commit/cd33280b68)\
  2018-06-09 11:26:52 +0530
  * [MDEV-16374](https://jira.mariadb.org/browse/MDEV-16374): Filtered shows 0 for materilization scan for a semi join, which makes optimizer always picks materialization scan over materialization lookup
* [Revision #15155ecd34](https://github.com/MariaDB/server/commit/15155ecd34)\
  2018-06-08 20:42:39 +0100
  * fix typo
* [Revision #5bfd562a00](https://github.com/MariaDB/server/commit/5bfd562a00)\
  2018-06-08 20:42:25 +0100
  * [MDEV-16445](https://jira.mariadb.org/browse/MDEV-16445) mysql\_upgrade\_service should add skip-slave-start to server start parameters
* [Revision #141bc58ac9](https://github.com/MariaDB/server/commit/141bc58ac9)\
  2018-06-08 19:52:30 +0100
  * [MDEV-16430](https://jira.mariadb.org/browse/MDEV-16430): mysql\_upgrade\_service does not write log file.
* [Revision #55abcfa7b7](https://github.com/MariaDB/server/commit/55abcfa7b7)\
  2018-06-05 18:16:12 +0300
  * [MDEV-16124](https://jira.mariadb.org/browse/MDEV-16124) fil\_rename\_tablespace() times out and crashes server during table-rebuilding ALTER TABLE
* [Revision #a61724a3ca](https://github.com/MariaDB/server/commit/a61724a3ca)\
  2018-05-24 11:38:34 +0300
  * [MDEV-16267](https://jira.mariadb.org/browse/MDEV-16267) Wrong INFORMATION\_SCHEMA.INNODB\_BUFFER\_PAGE.TABLE\_NAME
* [Revision #a816aa066e](https://github.com/MariaDB/server/commit/a816aa066e)\
  2018-05-23 11:26:49 +0300
  * Fixed ASAN heap-use-after-free handler::ha\_index\_or\_rnd\_end
* [Revision #908676dfd9](https://github.com/MariaDB/server/commit/908676dfd9)\
  2018-05-22 23:05:01 +0300
  * [MDEV-15308](https://jira.mariadb.org/browse/MDEV-15308) Assertion \`ha\_alter\_info->alter\_info->drop\_list.elements
* [Revision #da71c1bad7](https://github.com/MariaDB/server/commit/da71c1bad7)\
  2018-05-22 14:36:06 +0300
  * [MDEV-16229](https://jira.mariadb.org/browse/MDEV-16229) Replication aborts with ER\_VIEW\_SELECT\_TMPTABLE after half-failed RENAME
* [Revision #2f3779d31c](https://github.com/MariaDB/server/commit/2f3779d31c)\
  2018-05-20 14:19:14 +0300
  * Fixes for Aria transaction handling with lock tables
* Merge [Revision #c1b5d2801e](https://github.com/MariaDB/server/commit/c1b5d2801e) 2018-05-19 15:38:34 +0200 - Merge branch '5.5' into 10.0
* [Revision #cf5226174b](https://github.com/MariaDB/server/commit/cf5226174b)\
  2018-05-19 15:34:17 +0200
  * [MDEV-11129](https://jira.mariadb.org/browse/MDEV-11129) CREATE OR REPLACE TABLE t1 AS SELECT spfunc() crashes if spfunc() references t1
* [Revision #ef295c31e3](https://github.com/MariaDB/server/commit/ef295c31e3)\
  2018-05-16 21:51:46 +0300
  * [MDEV-11129](https://jira.mariadb.org/browse/MDEV-11129) CREATE OR REPLACE TABLE t1 AS SELECT spfunc() crashes if spfunc() references t1
* [Revision #d703e09cd6](https://github.com/MariaDB/server/commit/d703e09cd6)\
  2017-09-21 16:30:24 +0300
  * Fix that FLUSH TABLES FOR EXPORT also works for Aria tables.
* [Revision #b050df4fd3](https://github.com/MariaDB/server/commit/b050df4fd3)\
  2018-05-15 12:30:32 +0300
  * [MDEV-14943](https://jira.mariadb.org/browse/MDEV-14943) Alter table ORDER BY bug
* [Revision #197bf0fe35](https://github.com/MariaDB/server/commit/197bf0fe35)\
  2018-02-22 18:45:38 +0530
  * Bug #26334149 - MYSQL CRASHES WHEN FULL TEXT INDEXES IBD FILES ARE ORPHANED DUE TO RENAME TABLE
* [Revision #9c03ba8f0d](https://github.com/MariaDB/server/commit/9c03ba8f0d)\
  2017-12-27 11:56:11 +0530
  * Bug #27041445 SERVER ABORTS IF FTS\_DOC\_ID EXCEEDS FTS\_DOC\_ID\_MAX\_STEP
* Merge [Revision #c70fc6b16a](https://github.com/MariaDB/server/commit/c70fc6b16a) 2018-05-11 14:07:05 +0300 - Merge 5.5 into 10.0 (no changes)
* [Revision #580a8061a7](https://github.com/MariaDB/server/commit/580a8061a7)\
  2018-05-11 13:48:57 +0300
  * Remove a redundant condition added by the 5.6.40 merge
* [Revision #3cbfe8cc47](https://github.com/MariaDB/server/commit/3cbfe8cc47)\
  2018-05-10 19:00:54 +0400
  * [MDEV-15480](https://jira.mariadb.org/browse/MDEV-15480) Audit plugin does not respect QUERY\_DML for audit plugin.
* [Revision #4f42f0d1ea](https://github.com/MariaDB/server/commit/4f42f0d1ea)\
  2018-05-09 15:06:48 +0300
  * [MDEV-16119](https://jira.mariadb.org/browse/MDEV-16119) InnoDB lock->index refers to a freed object after failed ADD INDEX
* [Revision #34045af03f](https://github.com/MariaDB/server/commit/34045af03f)\
  2018-05-06 22:46:56 +0200
  * [MDEV-15216](https://jira.mariadb.org/browse/MDEV-15216) Assertion \`! is\_set() || m\_can\_overwrite\_status' failed in Diagnostics\_area::set\_error\_status upon operation inside XA
* [Revision #087ea8f820](https://github.com/MariaDB/server/commit/087ea8f820)\
  2018-05-08 10:31:35 +0200
  * de-obfuscate rpl\_\*\_implicit\_commit\_binlog test
* [Revision #0d429dcb37](https://github.com/MariaDB/server/commit/0d429dcb37)\
  2018-05-06 22:47:30 +0200
  * rename a test
* [Revision #7b9486d2eb](https://github.com/MariaDB/server/commit/7b9486d2eb)\
  2018-05-07 11:52:05 +0300
  * [MDEV-14693](https://jira.mariadb.org/browse/MDEV-14693) XA: Assertion \`!clust\_index->online\_log' failed in rollback\_inplace\_alter\_table
* Merge [Revision #3c07ed141c](https://github.com/MariaDB/server/commit/3c07ed141c) 2018-05-04 17:35:09 +0200 - Merge branch '5.5' into 10.0
* [Revision #04b1e61d69](https://github.com/MariaDB/server/commit/04b1e61d69)\
  2018-05-04 15:51:13 +0200
  * compiler warning
* [Revision #1cb7c4bfc0](https://github.com/MariaDB/server/commit/1cb7c4bfc0)\
  2018-05-03 16:14:54 +0100
  * [MDEV-16084](https://jira.mariadb.org/browse/MDEV-16084) Calling exit() from a signal handler is unsafe.
* [Revision #a411910dd6](https://github.com/MariaDB/server/commit/a411910dd6)\
  2018-05-03 10:26:00 -0400
  * bump the VERSION
* Merge [Revision #b432d4ad66](https://github.com/MariaDB/server/commit/b432d4ad66) 2018-05-03 11:42:19 +0300 - [MDEV-16080](https://jira.mariadb.org/browse/MDEV-16080) Crash in online table rebuild with concurrent DELETE of many BLOBs
* [Revision #f47eac2882](https://github.com/MariaDB/server/commit/f47eac2882)\
  2018-01-10 20:54:09 +0530
  * Bug #25928471: ONLINE ALTER AND CONCURRENT DELETE ON TABLE WITH MANY TEXT COLUMNS CAUSES CRASH

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
