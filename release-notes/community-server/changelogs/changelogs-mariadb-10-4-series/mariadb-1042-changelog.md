# MariaDB 10.4.2 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.2/)[Release Notes](../../old-releases/10.4/10.4.2.md)[Changelog](mariadb-1042-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 29 Jan 2019

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.2.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #9c60535f86](https://github.com/MariaDB/server/commit/9c60535f86)\
  2019-01-26 22:29:24 +0100
  * SSL test fixes
* [Revision #eff7f9bea2](https://github.com/MariaDB/server/commit/eff7f9bea2)\
  2019-01-28 13:49:47 +0100
  * update the result file after the merge
* [Revision #41a9a677eb](https://github.com/MariaDB/server/commit/41a9a677eb)\
  2019-01-27 12:18:39 +0100
  * downgrade wsrep\_plugin\_init()/wsrep\_plugin\_deinit log messages
* [Revision #4007eaba91](https://github.com/MariaDB/server/commit/4007eaba91)\
  2019-01-26 19:12:26 +0200
  * Removed declaration of strconvert() from innodb\_priv.h
* [Revision #c0c62196ca](https://github.com/MariaDB/server/commit/c0c62196ca)\
  2019-01-26 19:12:00 +0200
  * Removed \n from sql\_print\_error()
* [Revision #d0bfa4afc4](https://github.com/MariaDB/server/commit/d0bfa4afc4)\
  2019-01-26 19:11:06 +0200
  * Fixed failing testcase when blackhole engine is not enabled
* [Revision #574cde9be4](https://github.com/MariaDB/server/commit/574cde9be4)\
  2019-01-26 10:26:20 +0100
  * fix failing openssl\_1 test
* Merge [Revision #9b76e2843b](https://github.com/MariaDB/server/commit/9b76e2843b) 2019-01-26 01:13:41 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #3b1b665fcb](https://github.com/MariaDB/server/commit/3b1b665fcb) 2019-01-25 20:33:47 +0100 - Merge branch '10.2' into 10.3
* [Revision #3fb6d2587d](https://github.com/MariaDB/server/commit/3fb6d2587d)\
  2019-01-25 19:26:39 +0100
  * Don't run tests that check privileges in --embedded
* [Revision #d4515d1305](https://github.com/MariaDB/server/commit/d4515d1305)\
  2019-01-25 14:05:54 +0100
  * Deb: don't edit control file from inside rules file
* [Revision #74f184aff2](https://github.com/MariaDB/server/commit/74f184aff2)\
  2019-01-24 20:18:55 +0100
  * Fix tests not to fail with OpenSSL 1.1.1 with TLSv1.3
* [Revision #a4ab66c8f8](https://github.com/MariaDB/server/commit/a4ab66c8f8)\
  2019-01-09 23:10:16 +0100
  * Make the PYTHON\_SHEBANG value configurable
* [Revision #7334f9717d](https://github.com/MariaDB/server/commit/7334f9717d)\
  2019-01-09 15:05:02 +0100
  * Do not import commands library as it is not used
* [Revision #e99e6f29e9](https://github.com/MariaDB/server/commit/e99e6f29e9)\
  2019-01-05 11:49:35 +0100
  * cleanup: trg2bit() helper
* [Revision #0e1f7f5c4a](https://github.com/MariaDB/server/commit/0e1f7f5c4a)\
  2019-01-25 12:04:28 +0300
  * [MDEV-18057](https://jira.mariadb.org/browse/MDEV-18057) Assertion \`(node->state == 5) || (node->state == 6)' failed in row\_upd\_sec\_step upon DELETE after UPDATE failed due to FK violation
* Merge [Revision #9bd80ada6f](https://github.com/MariaDB/server/commit/9bd80ada6f) 2019-01-25 16:35:13 +0200 - Merge 10.2 into 10.3
* [Revision #31d0727a10](https://github.com/MariaDB/server/commit/31d0727a10)\
  2019-01-25 15:23:57 +0200
  * [MDEV-18235](https://jira.mariadb.org/browse/MDEV-18235): Changes related to fsync()
* [Revision #d97db40a9f](https://github.com/MariaDB/server/commit/d97db40a9f)\
  2019-01-25 12:46:23 +0200
  * [MDEV-18352](https://jira.mariadb.org/browse/MDEV-18352) Add a regression test for VARCHAR enlarging
* Merge [Revision #f2518f3da9](https://github.com/MariaDB/server/commit/f2518f3da9) 2019-01-25 14:38:44 +0200 - Merge pull request #1136 from tempesta-tech/sysprg/[MDEV-18379](https://jira.mariadb.org/browse/MDEV-18379)
* [Revision #a22dc6268b](https://github.com/MariaDB/server/commit/a22dc6268b)\
  2019-01-25 12:29:50 +0100
  * [MDEV-18379](https://jira.mariadb.org/browse/MDEV-18379): Unification of check for IPv6
* [Revision #45c47a04bd](https://github.com/MariaDB/server/commit/45c47a04bd)\
  2019-01-24 10:43:27 +0100
  * [MDEV-17401](https://jira.mariadb.org/browse/MDEV-17401): LOAD DATA from very big file into MyISAM table results in EOF error and corrupt index
* [Revision #06a37d37a1](https://github.com/MariaDB/server/commit/06a37d37a1)\
  2019-01-25 13:22:49 +0300
  * [MDEV-18122](https://jira.mariadb.org/browse/MDEV-18122) Assertion 'table->versioned() == m\_prebuilt->table->versioned()' failed in ha\_innobase::open
* Merge [Revision #e77156d51d](https://github.com/MariaDB/server/commit/e77156d51d) 2019-01-25 15:58:01 +0200 - Merge pull request #1135 from codership/10.4-fix-galera\_3nodes-ipv6
* [Revision #24807c0aaf](https://github.com/MariaDB/server/commit/24807c0aaf)\
  2019-01-25 11:12:41 +0200
  * Updated wsrep-lib to have more permissive compiler options by default
* [Revision #fc77fc80d2](https://github.com/MariaDB/server/commit/fc77fc80d2)\
  2019-01-25 11:05:28 +0200
  * Fixed Galera test regressions from 10.3 merge
* Merge [Revision #a3a89470fd](https://github.com/MariaDB/server/commit/a3a89470fd) 2019-01-25 08:08:32 +0200 - Merge 10.3 into 10.4
* Merge [Revision #e9ba165bcb](https://github.com/MariaDB/server/commit/e9ba165bcb) 2019-01-25 08:03:48 +0200 - Merge pull request #1129 from GeoffMontee/10.3-geoff-[MDEV-18372](https://jira.mariadb.org/browse/MDEV-18372)
* [Revision #f4ca2445c3](https://github.com/MariaDB/server/commit/f4ca2445c3)\
  2019-01-24 17:18:26 -0500
  * [MDEV-18372](https://jira.mariadb.org/browse/MDEV-18372): Minor [MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973)-related merge issue to 10.3
* [Revision #9c72615929](https://github.com/MariaDB/server/commit/9c72615929)\
  2019-01-25 08:07:06 +0200
  * Correct a result
* [Revision #2d60e3232d](https://github.com/MariaDB/server/commit/2d60e3232d)\
  2019-01-25 07:56:57 +0200
  * [MDEV-18369](https://jira.mariadb.org/browse/MDEV-18369): Crash at wsrep\_handle\_SR\_rollback(THD\*, THD\*): Assertion \`victim\_thd' failed.
* Merge [Revision #78829a5780](https://github.com/MariaDB/server/commit/78829a5780) 2019-01-24 22:42:35 +0200 - Merge 10.3 into 10.4
* Merge [Revision #947b6b849d](https://github.com/MariaDB/server/commit/947b6b849d) 2019-01-24 16:14:12 +0200 - Merge 10.2 into 10.3
* [Revision #fab531a150](https://github.com/MariaDB/server/commit/fab531a150)\
  2019-01-24 15:57:26 +0200
  * Fix the build after [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803)
* Merge [Revision #25161e6219](https://github.com/MariaDB/server/commit/25161e6219) 2019-01-24 14:43:29 +0200 - Merge 10.1 into 10.2
* Merge [Revision #65350042a4](https://github.com/MariaDB/server/commit/65350042a4) 2019-01-24 13:24:13 +0200 - Merge 10.0 into 10.1
* [Revision #edeba0c873](https://github.com/MariaDB/server/commit/edeba0c873)\
  2019-01-23 18:50:47 +0100
  * [MDEV-17868](https://jira.mariadb.org/browse/MDEV-17868) mysqltest fails to link with system PCRE libraries
* [Revision #a0f3b9f94f](https://github.com/MariaDB/server/commit/a0f3b9f94f)\
  2019-01-24 13:52:51 +0530
  * [MDEV-17376](https://jira.mariadb.org/browse/MDEV-17376) Server fails to set ADD\_PK\_INDEX, DROP\_PK\_INDEX if unique index nominated as PK
* [Revision #cce2b45c8f](https://github.com/MariaDB/server/commit/cce2b45c8f)\
  2019-01-10 16:32:56 +0200
  * [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803) Row-based event is not applied when table map id is greater 32 bit int
* [Revision #ba1ce3aeae](https://github.com/MariaDB/server/commit/ba1ce3aeae)\
  2019-01-24 12:01:43 +0200
  * [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803) side effect resulted in table id advance. A test result file is updated.
* [Revision #b22354680e](https://github.com/MariaDB/server/commit/b22354680e)\
  2019-01-23 20:16:21 +0200
  * merge 10.0 -> 10.1 to resolve [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803) conflicts.
* [Revision #c2a4bfad22](https://github.com/MariaDB/server/commit/c2a4bfad22)\
  2019-01-09 19:17:06 +0100
  * [MDEV-18119](https://jira.mariadb.org/browse/MDEV-18119) upgrading from 10.3 to 10.4 can result in the password for a user to be wiped out
* [Revision #d24060b179](https://github.com/MariaDB/server/commit/d24060b179)\
  2019-01-23 17:20:41 +0100
  * [MDEV-17421](https://jira.mariadb.org/browse/MDEV-17421): mtr does not restart the server whose parameters were changed
* [Revision #7886a70ef9](https://github.com/MariaDB/server/commit/7886a70ef9)\
  2019-01-23 17:18:57 +0100
  * [MDEV-17421](https://jira.mariadb.org/browse/MDEV-17421): mtr does not restart the server whose parameters were changed
* Merge [Revision #2d098933ee](https://github.com/MariaDB/server/commit/2d098933ee) 2019-01-23 18:03:51 +0200 - Merge pull request #880 from tempesta-tech/sysprg/[MDEV-17421](https://jira.mariadb.org/browse/MDEV-17421)
* [Revision #1eb364f8b3](https://github.com/MariaDB/server/commit/1eb364f8b3)\
  2018-10-10 17:16:34 +0200
  * [MDEV-17421](https://jira.mariadb.org/browse/MDEV-17421): mtr does not restart the server whose parameters were changed
* [Revision #7930ab7e33](https://github.com/MariaDB/server/commit/7930ab7e33)\
  2019-01-24 12:36:10 +0200
  * Comment out the statement that triggers [MDEV-18366](https://jira.mariadb.org/browse/MDEV-18366)
* [Revision #46f712c73c](https://github.com/MariaDB/server/commit/46f712c73c)\
  2019-01-24 12:31:54 +0200
  * [MDEV-15114](https://jira.mariadb.org/browse/MDEV-15114): Fix memory leaks
* [Revision #b572814baa](https://github.com/MariaDB/server/commit/b572814baa)\
  2019-01-23 20:56:52 +0200
  * After-merge fix of a result
* Merge [Revision #3dac4e9f0e](https://github.com/MariaDB/server/commit/3dac4e9f0e) 2019-01-23 19:48:19 +0200 - [MDEV-18338](https://jira.mariadb.org/browse/MDEV-18338) Merge new release of InnoDB 5.7.25 to 10.2
* [Revision #d283f80eae](https://github.com/MariaDB/server/commit/d283f80eae)\
  2019-01-22 16:43:59 +0200
  * Update the InnoDB version number
* [Revision #64678ca506](https://github.com/MariaDB/server/commit/64678ca506)\
  2019-01-23 18:09:32 +0200
  * Bug #22990029: Add a test case
* [Revision #aa8a31dadd](https://github.com/MariaDB/server/commit/aa8a31dadd)\
  2018-10-10 18:05:02 +0530
  * Bug #22990029 GCOLS: INCORRECT BEHAVIOR AFTER DATA INSERTED WITH IGNORE KEYWORD
* [Revision #e32305e505](https://github.com/MariaDB/server/commit/e32305e505)\
  2019-01-23 19:45:12 +0200
  * Add a test for Bug #28470805 DELETE CASCADE CRASHES ... ON RESTART
* Merge [Revision #9a7281a703](https://github.com/MariaDB/server/commit/9a7281a703) 2019-01-23 15:09:06 +0200 - Merge 10.1 into 10.2
* Merge [Revision #3b6d2efcb1](https://github.com/MariaDB/server/commit/3b6d2efcb1) 2019-01-23 14:34:23 +0200 - Merge 10.0 into 10.1
* [Revision #2a0f1d6132](https://github.com/MariaDB/server/commit/2a0f1d6132)\
  2019-01-22 11:06:15 +0100
  * Bug#28867993: POSSIBLE ISSUE WITH MYSQL SERVER RESTART
* [Revision #31d592ba7d](https://github.com/MariaDB/server/commit/31d592ba7d)\
  2019-01-23 12:05:24 +0200
  * [MDEV-18349](https://jira.mariadb.org/browse/MDEV-18349) InnoDB file size changes are not safe when file system crashes
* [Revision #6786fb004c](https://github.com/MariaDB/server/commit/6786fb004c)\
  2019-01-16 14:46:36 +0100
  * [MDEV-15925](https://jira.mariadb.org/browse/MDEV-15925) FRM\_MAX\_SIZE too low for some use cases
* [Revision #2061e00c20](https://github.com/MariaDB/server/commit/2061e00c20)\
  2019-01-17 22:56:12 +0200
  * [MDEV-14440](https://jira.mariadb.org/browse/MDEV-14440): Assertion \`inited==RND' failed in handler::ha\_rnd\_end
* [Revision #52d13036d8](https://github.com/MariaDB/server/commit/52d13036d8)\
  2019-01-23 13:44:20 +0200
  * [MDEV-17933](https://jira.mariadb.org/browse/MDEV-17933) slow server status - dict\_sys\_get\_size()
* Merge [Revision #f9cc956065](https://github.com/MariaDB/server/commit/f9cc956065) 2019-01-21 15:06:48 +0200 - Merge pull request #1114 from GeoffMontee/10.1-geoff-[MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973)
* [Revision #2084cd5422](https://github.com/MariaDB/server/commit/2084cd5422)\
  2019-01-21 05:42:00 -0500
  * [MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973): Don't overwrite xtrabackup-v2/mariadb-backup SST logs by default
* [Revision #d06ebd932d](https://github.com/MariaDB/server/commit/d06ebd932d)\
  2019-01-22 06:51:03 +0200
  * Remove references to removed dict\_sys->size
* [Revision #2565c02ca5](https://github.com/MariaDB/server/commit/2565c02ca5)\
  2019-01-22 06:19:21 +0200
  * Remove unnecessary type casts
* [Revision #5c159c9037](https://github.com/MariaDB/server/commit/5c159c9037)\
  2019-01-23 12:00:12 +0000
  * [MDEV-18356](https://jira.mariadb.org/browse/MDEV-18356)\
    Renamed backup-encrypted option introduced in 7158edcba3af3766e9329f9927ce4adfd2a40bf8
* [Revision #9f4d4f404f](https://github.com/MariaDB/server/commit/9f4d4f404f)\
  2019-01-22 18:23:47 +0400
  * [MDEV-12747](https://jira.mariadb.org/browse/MDEV-12747) - main.mysqld\_option\_err fails in buildbot with timeout
* Merge [Revision #55be043c13](https://github.com/MariaDB/server/commit/55be043c13) 2019-01-23 12:07:36 +0200 - Merge pull request #1120 from tempesta-tech/sysprg/[MDEV-17835](https://jira.mariadb.org/browse/MDEV-17835) v2
* [Revision #0e89e90f42](https://github.com/MariaDB/server/commit/0e89e90f42)\
  2019-01-22 13:28:03 +0100
  * [MDEV-17835](https://jira.mariadb.org/browse/MDEV-17835): Remove wsrep-sst-method=xtrabackup
* [Revision #d6ba849617](https://github.com/MariaDB/server/commit/d6ba849617)\
  2019-01-24 17:16:23 +0200
  * Remove unused code
* [Revision #48fb4504c5](https://github.com/MariaDB/server/commit/48fb4504c5)\
  2019-01-24 16:02:49 +0100
  * [MDEV-18337](https://jira.mariadb.org/browse/MDEV-18337) Upgrade to 10.4 fails on some Ubuntu's due to dialog.so conflict
* [Revision #f3ce9edaf9](https://github.com/MariaDB/server/commit/f3ce9edaf9)\
  2019-01-24 17:15:46 +0300
  * Fix compilation on Windows
* [Revision #c3a1cd3555](https://github.com/MariaDB/server/commit/c3a1cd3555)\
  2019-01-24 10:47:19 +0200
  * Silence "WSREP: Server initial position ..." message when wsrep-debug=OFF
* Merge [Revision #f7a511fb7a](https://github.com/MariaDB/server/commit/f7a511fb7a) 2019-01-24 09:16:17 +0200 - Merge pull request #1124 from codership/10.4-test-pr
* [Revision #4c5de558a2](https://github.com/MariaDB/server/commit/4c5de558a2)\
  2019-01-23 16:26:42 +0200
  * Update wsrep-lib to have OSX compilation fixes
* [Revision #501f5c98b2](https://github.com/MariaDB/server/commit/501f5c98b2)\
  2019-01-24 09:14:30 +0200
  * Move Galera disabled.def files from test directory to correct suite directory.
* [Revision #3238f2a6e9](https://github.com/MariaDB/server/commit/3238f2a6e9)\
  2019-01-23 16:26:09 +0300
  * [MDEV-18073](https://jira.mariadb.org/browse/MDEV-18073): get\_range\_limit\_read\_cost() doesnt adjust LIMIT for the range access
* [Revision #b7a784ae25](https://github.com/MariaDB/server/commit/b7a784ae25)\
  2019-01-23 15:49:49 +0300
  * [MDEV-17761](https://jira.mariadb.org/browse/MDEV-17761): Odd optimizer choice with ORDER BY LIMIT and condition selectivity
* [Revision #36a2a185fe](https://github.com/MariaDB/server/commit/36a2a185fe)\
  2019-01-23 15:30:00 +0400
  * Galera4
* [Revision #382115b992](https://github.com/MariaDB/server/commit/382115b992)\
  2019-01-21 19:10:38 +0400
  * [MDEV-12747](https://jira.mariadb.org/browse/MDEV-12747) - main.mysqld\_option\_err fails in buildbot with timeout
* [Revision #71261e3188](https://github.com/MariaDB/server/commit/71261e3188)\
  2019-01-21 15:25:37 +0200
  * [MDEV-18315](https://jira.mariadb.org/browse/MDEV-18315)/[MDEV-18316](https://jira.mariadb.org/browse/MDEV-18316): Assertion failures on instant DROP COLUMN
* Merge [Revision #8aae31cf49](https://github.com/MariaDB/server/commit/8aae31cf49) 2019-01-21 11:21:27 +0200 - Merge 10.3 into 10.4
* [Revision #d4144c8e01](https://github.com/MariaDB/server/commit/d4144c8e01)\
  2019-01-21 09:32:06 +0200
  * [MDEV-17821](https://jira.mariadb.org/browse/MDEV-17821) Assertion !page\_rec\_is\_supremum(rec) failed in btr\_pcur\_store\_position
* Merge [Revision #4edb29380c](https://github.com/MariaDB/server/commit/4edb29380c) 2019-01-18 14:24:10 +0200 - Merge 10.3 into 10.4
* [Revision #778192454e](https://github.com/MariaDB/server/commit/778192454e)\
  2019-01-18 14:22:33 +0200
  * [MDEV-17823](https://jira.mariadb.org/browse/MDEV-17823): Fix the non-debug build
* Merge [Revision #0474be0aab](https://github.com/MariaDB/server/commit/0474be0aab) 2019-01-18 13:58:33 +0200 - Merge 10.3 into 10.4
* [Revision #4e75bfcb21](https://github.com/MariaDB/server/commit/4e75bfcb21)\
  2019-01-18 12:39:19 +0200
  * [MDEV-18152](https://jira.mariadb.org/browse/MDEV-18152) Assertion 'num\_fts\_index <= 1' failed
* Merge [Revision #a0d3ead83a](https://github.com/MariaDB/server/commit/a0d3ead83a) 2019-01-18 10:43:31 +0200 - Merge 10.2 into 10.3
* Merge [Revision #37ffdb44ef](https://github.com/MariaDB/server/commit/37ffdb44ef) 2019-01-18 06:51:52 +0200 - Merge 10.1 into 10.2
* [Revision #1d72db45a8](https://github.com/MariaDB/server/commit/1d72db45a8)\
  2019-01-18 06:46:39 +0200
  * [MDEV-18237](https://jira.mariadb.org/browse/MDEV-18237) InnoDB: Unable to drop FTS index aux table and further errors (possibly bogus)
* [Revision #69221746db](https://github.com/MariaDB/server/commit/69221746db)\
  2019-01-17 23:17:37 +0100
  * [MDEV-18289](https://jira.mariadb.org/browse/MDEV-18289) - Fix a race between thd\_destructor\_proxy() startup and server shutdown.
* [Revision #5f60c7c3c2](https://github.com/MariaDB/server/commit/5f60c7c3c2)\
  2019-01-18 10:39:52 +0200
  * [MDEV-17823](https://jira.mariadb.org/browse/MDEV-17823) Assertion failed when accessing indexed instantly added column
* [Revision #937c90ce2d](https://github.com/MariaDB/server/commit/937c90ce2d)\
  2019-01-18 03:31:11 +0400
  * [MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313) Improve Audit API.
* [Revision #cc18a5db9b](https://github.com/MariaDB/server/commit/cc18a5db9b)\
  2019-01-18 03:18:02 +0400
  * [MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313) Improving audit API.
* [Revision #dd03cb3776](https://github.com/MariaDB/server/commit/dd03cb3776)\
  2019-01-17 19:49:56 +0400
  * [MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313) Improving audit plugin API.
* [Revision #5fb4e4ab39](https://github.com/MariaDB/server/commit/5fb4e4ab39)\
  2019-01-17 14:16:59 +0200
  * [MDEV-18149](https://jira.mariadb.org/browse/MDEV-18149) Crash after DROP COLUMN of AUTO\_INCREMENT column on nonempty table
* Merge [Revision #9dc81d2a7a](https://github.com/MariaDB/server/commit/9dc81d2a7a) 2019-01-17 13:21:27 +0200 - Merge 10.3 into 10.4
* Merge [Revision #77cbaa96ad](https://github.com/MariaDB/server/commit/77cbaa96ad) 2019-01-17 12:33:31 +0200 - Merge 10.2 into 10.3
* Merge [Revision #8e80fd6bfd](https://github.com/MariaDB/server/commit/8e80fd6bfd) 2019-01-17 11:24:38 +0200 - Merge 10.1 into 10.2
* [Revision #c1aae37087](https://github.com/MariaDB/server/commit/c1aae37087)\
  2019-01-17 10:11:02 +0200
  * Re-record results for the changed max\_value of table\_definition\_cache
* [Revision #ad376a05fa](https://github.com/MariaDB/server/commit/ad376a05fa)\
  2019-01-17 13:09:14 +0530
  * [MDEV-18279](https://jira.mariadb.org/browse/MDEV-18279) MLOG\_FILE\_WRITE\_CRYPT\_DATA fails to set the crypt\_data->type for tablespace.
* [Revision #a84be48e00](https://github.com/MariaDB/server/commit/a84be48e00)\
  2019-01-17 09:39:20 +0200
  * Update ,32bit.rdiff
* Merge [Revision #71eb762611](https://github.com/MariaDB/server/commit/71eb762611) 2019-01-17 06:40:24 +0200 - Merge 10.0 into 10.1
* [Revision #19a7656fb1](https://github.com/MariaDB/server/commit/19a7656fb1)\
  2018-05-21 10:42:44 +1000
  * safemalloc: warn, flush after fprintf
* [Revision #db469b6907](https://github.com/MariaDB/server/commit/db469b6907)\
  2019-01-11 11:55:07 +0100
  * [MDEV-17475](https://jira.mariadb.org/browse/MDEV-17475): Increase maximum possible value for table\_definition\_cache to match table\_open\_cache
* Merge [Revision #12f362c333](https://github.com/MariaDB/server/commit/12f362c333) 2019-01-15 14:53:27 +0200 - [MDEV-18233](https://jira.mariadb.org/browse/MDEV-18233) Moving the hash\_node\_t to improve locality of reference
* [Revision #a06a3e4670](https://github.com/MariaDB/server/commit/a06a3e4670)\
  2019-01-14 22:14:56 +0300
  * [MDEV-18233](https://jira.mariadb.org/browse/MDEV-18233) Moving the hash\_node\_t to improve locality of reference
* [Revision #e0633f25e8](https://github.com/MariaDB/server/commit/e0633f25e8)\
  2019-01-15 14:55:12 +0300
  * [MDEV-18243](https://jira.mariadb.org/browse/MDEV-18243) incorrect ASAN instrumentation
* [Revision #71e9f0d123](https://github.com/MariaDB/server/commit/71e9f0d123)\
  2019-01-15 11:50:15 +0200
  * [MDEV-17797](https://jira.mariadb.org/browse/MDEV-17797) Add ASAN poisoning for mem\_heap\_t
* Merge [Revision #b4c471099d](https://github.com/MariaDB/server/commit/b4c471099d) 2019-01-14 14:06:26 +0200 - Merge pull request #973 from tempesta-tech/tt-10.0-[MDEV-16499](https://jira.mariadb.org/browse/MDEV-16499)-virtual-innodb
* [Revision #e8bb94ccc8](https://github.com/MariaDB/server/commit/e8bb94ccc8)\
  2018-11-30 01:15:30 +0300
  * [MDEV-16499](https://jira.mariadb.org/browse/MDEV-16499) \[10.1] ER\_NO\_SUCH\_TABLE\_IN\_ENGINE followed by "Please drop the table and recreate" upon adding FULLTEXT key to table with virtual column
* [Revision #d0d0f88f2c](https://github.com/MariaDB/server/commit/d0d0f88f2c)\
  2019-01-06 23:15:25 +0530
  * [MDEV-13784](https://jira.mariadb.org/browse/MDEV-13784): query causes seg fault
* [Revision #038785e1f8](https://github.com/MariaDB/server/commit/038785e1f8)\
  2019-01-16 23:02:39 +0530
  * [MDEV-18183](https://jira.mariadb.org/browse/MDEV-18183) Server startup fails while dropping garbage encrypted tablespace
* [Revision #69328c31ed](https://github.com/MariaDB/server/commit/69328c31ed)\
  2019-01-15 09:58:35 +0100
  * [MDEV-18176](https://jira.mariadb.org/browse/MDEV-18176) Galera test failure on galera.galera\_gtid\_slave\_sst\_rsync
* [Revision #7d3161def8](https://github.com/MariaDB/server/commit/7d3161def8)\
  2019-01-14 13:09:27 +0100
  * [MDEV-18225](https://jira.mariadb.org/browse/MDEV-18225) Avoid use of LOCK\_prepared\_stmt\_count mutex in Statement\_map destructo
* [Revision #f3e9d9a6e6](https://github.com/MariaDB/server/commit/f3e9d9a6e6)\
  2018-10-12 01:43:12 -0700
  * Change information\_schema-big to include innodb
* [Revision #802e8d6b89](https://github.com/MariaDB/server/commit/802e8d6b89)\
  2018-10-07 04:51:46 -0700
  * Backport INFORMATION\_SCHEMA.CHECK\_CONSTRAINTS
* [Revision #2153aaf66e](https://github.com/MariaDB/server/commit/2153aaf66e)\
  2019-01-15 22:47:54 +0100
  * mariadb-backup : use die() macro for fatal exit with error message.
* [Revision #a8a27e65a8](https://github.com/MariaDB/server/commit/a8a27e65a8)\
  2019-01-14 22:28:23 +0100
  * [MDEV-18212](https://jira.mariadb.org/browse/MDEV-18212) mariadb-backup: Make output format uniform whenever possible
* [Revision #61b600079b](https://github.com/MariaDB/server/commit/61b600079b)\
  2019-01-15 09:47:34 +0200
  * [MDEV-16690](https://jira.mariadb.org/browse/MDEV-16690) node hang due to conflicting inserts in FK child table
* [Revision #62a0224666](https://github.com/MariaDB/server/commit/62a0224666)\
  2019-01-09 09:26:17 +1100
  * safemalloc: put bad\_ptr error arguments in right order
* [Revision #890e027870](https://github.com/MariaDB/server/commit/890e027870)\
  2019-01-17 10:30:09 +0400
  * [MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313) Improving audit api.
* [Revision #294d9bf248](https://github.com/MariaDB/server/commit/294d9bf248)\
  2019-01-17 03:52:52 +0400
  * [MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313) Improving audit api.
* [Revision #edba047080](https://github.com/MariaDB/server/commit/edba047080)\
  2019-01-16 18:46:32 +0200
  * [MDEV-18218](https://jira.mariadb.org/browse/MDEV-18218) Assertion \`0' failed in btr\_page\_reorganize\_low upon DROP COLUMN
* [Revision #b13d356af8](https://github.com/MariaDB/server/commit/b13d356af8)\
  2019-01-16 05:39:03 +0200
  * Disable a failing test
* Merge [Revision #78d8bb71eb](https://github.com/MariaDB/server/commit/78d8bb71eb) 2019-01-16 05:38:30 +0200 - Merge 10.3 into 10.4
* [Revision #848fd3f765](https://github.com/MariaDB/server/commit/848fd3f765)\
  2019-01-16 05:25:53 +0200
  * Add release result diff for galera\_ist\_innodb\_flush\_logs
* [Revision #4bcd7da076](https://github.com/MariaDB/server/commit/4bcd7da076)\
  2019-01-15 16:44:13 +0100
  * fixup! Fixed compiler warnings from optimized builds
* [Revision #9990027f87](https://github.com/MariaDB/server/commit/9990027f87)\
  2019-01-15 17:05:42 +0200
  * Fixed compiler warnings from optimized builds
* Merge [Revision #ce06990056](https://github.com/MariaDB/server/commit/ce06990056) 2019-01-15 15:22:03 +0200 - Merge pull request #1088 from tempesta-tech/tt-10.4-[MDEV-18173](https://jira.mariadb.org/browse/MDEV-18173)
* [Revision #35318d730a](https://github.com/MariaDB/server/commit/35318d730a)\
  2019-01-14 14:05:21 +0300
  * [MDEV-18173](https://jira.mariadb.org/browse/MDEV-18173) Assertion `o->ind == vers_end' or` o->ind == vers\_start' failed in dict\_table\_t::instant\_column
* Merge [Revision #55a0c3eb6d](https://github.com/MariaDB/server/commit/55a0c3eb6d) 2019-01-15 12:30:29 +0200 - Merge 10.3 into 10.4
* [Revision #8655592ae5](https://github.com/MariaDB/server/commit/8655592ae5)\
  2019-01-15 08:52:26 +0200
  * recv\_log\_recover\_10\_4(): Fix a trivial bug
* Merge [Revision #efb510462e](https://github.com/MariaDB/server/commit/efb510462e) 2019-01-14 14:55:50 +0200 - Merge 10.2 into 10.3
* [Revision #662217a592](https://github.com/MariaDB/server/commit/662217a592)\
  2019-01-09 16:36:41 +0300
  * [MDEV-18186](https://jira.mariadb.org/browse/MDEV-18186) assertion failure on missing InnoDB index
* [Revision #cbdc2d9489](https://github.com/MariaDB/server/commit/cbdc2d9489)\
  2018-12-27 21:14:07 +0300
  * Replace log\_group\_t::file\_header\_bufs with local array
* [Revision #46046f2e59](https://github.com/MariaDB/server/commit/46046f2e59)\
  2019-01-14 13:20:59 +0200
  * After-merge fix: Disable a failing test
* Merge [Revision #248dc12e60](https://github.com/MariaDB/server/commit/248dc12e60) 2019-01-14 11:37:51 +0200 - Merge 10.1 into 10.2
* [Revision #7372fe4da1](https://github.com/MariaDB/server/commit/7372fe4da1)\
  2018-12-03 12:59:45 +0100
  * xb\_process\_datadir(): Fix resource leaks
* [Revision #1d56d875fe](https://github.com/MariaDB/server/commit/1d56d875fe)\
  2019-01-07 12:12:30 +0200
  * [MDEV-15740](https://jira.mariadb.org/browse/MDEV-15740): InnoDB does not flush redo log when it shoul
* [Revision #f5ee7fb31f](https://github.com/MariaDB/server/commit/f5ee7fb31f)\
  2018-11-29 13:38:16 +0100
  * Fix a memory leak in ALTER TABLE
* [Revision #79078167c3](https://github.com/MariaDB/server/commit/79078167c3)\
  2018-12-19 22:30:28 +0530
  * [MDEV-17753](https://jira.mariadb.org/browse/MDEV-17753) ALTER USER fail to replicate
* [Revision #7331c661db](https://github.com/MariaDB/server/commit/7331c661db)\
  2019-01-10 19:35:45 +0100
  * [MDEV-18201](https://jira.mariadb.org/browse/MDEV-18201) : mariadb-backup- fix processing of rename/create sequence in prepare
* [Revision #4a872ae1e7](https://github.com/MariaDB/server/commit/4a872ae1e7)\
  2019-01-09 22:28:31 +0100
  * [MDEV-18185](https://jira.mariadb.org/browse/MDEV-18185) - mariadb-backup - fix specific case of table rename handing in prepare.
* [Revision #a75dbfd718](https://github.com/MariaDB/server/commit/a75dbfd718)\
  2019-01-14 14:37:34 +0200
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Remove fil\_space\_t::name\_hash
* [Revision #14471d92c5](https://github.com/MariaDB/server/commit/14471d92c5)\
  2019-01-15 11:41:30 +0200
  * Minor InnoDB refactoring
* [Revision #e82756503f](https://github.com/MariaDB/server/commit/e82756503f)\
  2019-01-15 09:56:33 +0200
  * Fixes for failures related to push for BACKUP LOCK
* [Revision #29f77d41f5](https://github.com/MariaDB/server/commit/29f77d41f5)\
  2019-01-14 20:51:05 +0400
  * [MDEV-18205](https://jira.mariadb.org/browse/MDEV-18205) Assertion \`str\_length < len' failed in Binary\_string::realloc\_raw
* [Revision #aad0165cea](https://github.com/MariaDB/server/commit/aad0165cea)\
  2019-01-14 15:46:49 +0200
  * Added support for BACKUP LOCK / BACKUP UNLOCK
* [Revision #3975e22d55](https://github.com/MariaDB/server/commit/3975e22d55)\
  2019-01-14 15:29:24 +0200
  * Ignore some new executables
* [Revision #32bb579192](https://github.com/MariaDB/server/commit/32bb579192)\
  2019-01-14 14:43:24 +0100
  * replace hardcoded string "#sql" with tmp\_file\_prefix
* [Revision #24bc8edcc5](https://github.com/MariaDB/server/commit/24bc8edcc5)\
  2019-01-14 14:25:08 +0100
  * [MDEV-18184](https://jira.mariadb.org/browse/MDEV-18184) Do not copy temporary files (prefixed with #sql-) to backup
* [Revision #c6b2b74645](https://github.com/MariaDB/server/commit/c6b2b74645)\
  2019-01-14 13:40:08 +0200
  * Fix Valgrind build after e7924a8598cbb785363ddd6489cb3c1210347f5f
* [Revision #d97a26a67d](https://github.com/MariaDB/server/commit/d97a26a67d)\
  2019-01-14 15:23:10 +0400
  * [MDEV-18145](https://jira.mariadb.org/browse/MDEV-18145) Assertion \`0' failed in Item::val\_native upon SELECT subquery with timestamp
* Merge [Revision #ac9b818c24](https://github.com/MariaDB/server/commit/ac9b818c24) 2019-01-14 09:40:12 +0200 - Merge 10.3 into 10.4
* [Revision #69290ce3eb](https://github.com/MariaDB/server/commit/69290ce3eb)\
  2019-01-14 09:24:39 +0200
  * [MDEV-18224](https://jira.mariadb.org/browse/MDEV-18224) MTR's internal check of the test case 'innodb.recovery\_shutdown' failed due to extra #sql-ib\*.ibd files
* [Revision #82490a97db](https://github.com/MariaDB/server/commit/82490a97db)\
  2019-01-10 16:08:26 +0400
  * [MDEV-18150](https://jira.mariadb.org/browse/MDEV-18150) Assertion \`decimals\_to\_set <= 38' failed in Item\_func\_round::fix\_length\_and\_dec\_decimal
* [Revision #2ffa11e33e](https://github.com/MariaDB/server/commit/2ffa11e33e)\
  2019-01-09 15:00:56 +0200
  * Appveyor configuration and addition of badge
* Merge [Revision #4bf47cb989](https://github.com/MariaDB/server/commit/4bf47cb989) 2019-01-09 10:17:51 +0000 - Merge pull request #559 from grooverdan/10.3-travis-systemversioning
* [Revision #5cf45fb272](https://github.com/MariaDB/server/commit/5cf45fb272)\
  2018-01-18 20:33:02 +1100
  * travis: add versioning to test suite
* Merge [Revision #13df03a04e](https://github.com/MariaDB/server/commit/13df03a04e) 2019-01-09 07:53:22 +0000 - Merge pull request #768 from grooverdan/10.3-travis-osx-zstd
* [Revision #2b39f43613](https://github.com/MariaDB/server/commit/2b39f43613)\
  2018-05-23 14:58:13 +1000
  * travis: add zstd for osx
* [Revision #e7924a8598](https://github.com/MariaDB/server/commit/e7924a8598)\
  2019-01-11 15:47:35 +0200
  * Remove code duplication around buf\_pool->flush\_rbt
* [Revision #301bd62b25](https://github.com/MariaDB/server/commit/301bd62b25)\
  2019-01-10 00:45:34 +0200
  * [MDEV-17820](https://jira.mariadb.org/browse/MDEV-17820) Assertion failed on instant DROP COLUMN
* [Revision #6bd5c555d9](https://github.com/MariaDB/server/commit/6bd5c555d9)\
  2019-01-09 19:50:48 +0200
  * [MDEV-18190](https://jira.mariadb.org/browse/MDEV-18190) A table with variable-length PRIMARY KEY is unaccessible after instant DROP COLUMN
* [Revision #65083ba64c](https://github.com/MariaDB/server/commit/65083ba64c)\
  2019-01-08 01:30:13 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* Merge [Revision #e2b585c1c5](https://github.com/MariaDB/server/commit/e2b585c1c5) 2019-01-08 18:22:43 +0200 - Merge 10.3 into 10.4
* Merge [Revision #38f1c9df32](https://github.com/MariaDB/server/commit/38f1c9df32) 2019-01-08 17:37:44 +0200 - Merge 10.2 into 10.3
* [Revision #9edadc29b1](https://github.com/MariaDB/server/commit/9edadc29b1)\
  2019-01-08 20:41:39 +0530
  * [MDEV-17748](https://jira.mariadb.org/browse/MDEV-17748) innodb.alter\_inplace\_perfschema fails in buildbot with wrong result
* [Revision #0c20b247de](https://github.com/MariaDB/server/commit/0c20b247de)\
  2019-01-04 21:22:41 +0200
  * Disable galera.query\_cache test.
* [Revision #b6b15de85d](https://github.com/MariaDB/server/commit/b6b15de85d)\
  2019-01-04 20:23:13 +0200
  * Disable failing Galera test galera\_query\_cache.
* Merge [Revision #3d8011b375](https://github.com/MariaDB/server/commit/3d8011b375) 2019-01-04 14:47:56 +0200 - Merge pull request #929 from angeloudy/fix-broken-thing
* [Revision #cb85803c45](https://github.com/MariaDB/server/commit/cb85803c45)\
  2019-01-02 15:40:55 +1100
  * Use absolute path for mariadb-backup binary
* [Revision #216d5f7899](https://github.com/MariaDB/server/commit/216d5f7899)\
  2018-11-29 12:36:57 +1100
  * use `ps -p` instead of `ps --pid`
* [Revision #0e794c6a69](https://github.com/MariaDB/server/commit/0e794c6a69)\
  2018-11-15 13:51:09 +1100
  * Make mariadb-backup.sh compatible on FreeBSD
* [Revision #d27bea9e9a](https://github.com/MariaDB/server/commit/d27bea9e9a)\
  2019-01-07 07:31:25 -0500
  * bump the VERSION
* [Revision #83c81d8991](https://github.com/MariaDB/server/commit/83c81d8991)\
  2018-12-05 13:13:07 +0100
  * [MDEV-7598](https://jira.mariadb.org/browse/MDEV-7598) Lock user after too many password errors
* [Revision #30da40bb8c](https://github.com/MariaDB/server/commit/30da40bb8c)\
  2019-01-08 00:57:19 +0200
  * [MDEV-18160](https://jira.mariadb.org/browse/MDEV-18160)/[MDEV-18162](https://jira.mariadb.org/browse/MDEV-18162) Assertion failure or crash after DROP COLUMN
* [Revision #39a8caa51c](https://github.com/MariaDB/server/commit/39a8caa51c)\
  2019-01-07 01:18:19 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #c66db377d7](https://github.com/MariaDB/server/commit/c66db377d7)\
  2019-01-07 00:06:24 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #aa2db75419](https://github.com/MariaDB/server/commit/aa2db75419)\
  2019-01-07 07:38:56 +0200
  * Fix test result differences
* Merge [Revision #734510a44d](https://github.com/MariaDB/server/commit/734510a44d) 2019-01-06 17:43:02 +0200 - Merge 10.3 into 10.4
* [Revision #2465d3e00b](https://github.com/MariaDB/server/commit/2465d3e00b)\
  2019-01-01 19:23:52 +0200
  * Remove unnecessary attribute((unused))
* [Revision #88cc78c9c4](https://github.com/MariaDB/server/commit/88cc78c9c4)\
  2019-01-01 15:12:39 +0200
  * Removed compiler warnings
* [Revision #17b73fb954](https://github.com/MariaDB/server/commit/17b73fb954)\
  2018-12-31 21:08:27 +0200
  * Use the accessor HA\_CREATE\_INFO::tmp\_table()
* [Revision #3bdd93c10a](https://github.com/MariaDB/server/commit/3bdd93c10a)\
  2018-12-29 01:46:56 +0400
  * tc\_contention\_warning\_reported transition to std::atomic
* [Revision #0f034e2e96](https://github.com/MariaDB/server/commit/0f034e2e96)\
  2018-12-29 01:37:46 +0400
  * time\_collector transition to std::atomic
* [Revision #1e7df0e530](https://github.com/MariaDB/server/commit/1e7df0e530)\
  2018-12-29 00:44:34 +0400
  * XID\_cache\_element::m\_state transition to std::atomic
* [Revision #9e37537c4e](https://github.com/MariaDB/server/commit/9e37537c4e)\
  2018-12-29 00:04:55 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #e2d96e8a16](https://github.com/MariaDB/server/commit/e2d96e8a16)\
  2018-12-28 23:51:15 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #66bca0dfa9](https://github.com/MariaDB/server/commit/66bca0dfa9)\
  2018-12-28 22:28:58 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #c6a00544ff](https://github.com/MariaDB/server/commit/c6a00544ff)\
  2018-12-28 21:00:23 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #d2bdd78915](https://github.com/MariaDB/server/commit/d2bdd78915)\
  2018-12-28 18:51:13 +0400
  * Master\_info counters transition to Atomic\_counter
* [Revision #656a702ca9](https://github.com/MariaDB/server/commit/656a702ca9)\
  2018-12-28 17:53:50 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #54b3fd2581](https://github.com/MariaDB/server/commit/54b3fd2581)\
  2018-12-28 17:17:11 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #fbe2a5b7d6](https://github.com/MariaDB/server/commit/fbe2a5b7d6)\
  2018-12-28 15:23:54 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #28d627392b](https://github.com/MariaDB/server/commit/28d627392b)\
  2018-12-28 14:43:06 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #adc30ecab5](https://github.com/MariaDB/server/commit/adc30ecab5)\
  2018-12-28 14:24:22 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #d46b3c99b4](https://github.com/MariaDB/server/commit/d46b3c99b4)\
  2018-12-03 19:56:55 +0300
  * [MDEV-17697](https://jira.mariadb.org/browse/MDEV-17697) Broken versioning info after instant drop column
* [Revision #cb2f36d3ea](https://github.com/MariaDB/server/commit/cb2f36d3ea)\
  2018-12-28 15:33:34 +0200
  * [MDEV-14975](https://jira.mariadb.org/browse/MDEV-14975): Cleanup check\_all\_privileges()
* [Revision #6639fc3fda](https://github.com/MariaDB/server/commit/6639fc3fda)\
  2018-12-28 15:23:42 +0200
  * [MDEV-18098](https://jira.mariadb.org/browse/MDEV-18098) Crash after rollback of instant DROP COLUMN
* [Revision #dc90234bda](https://github.com/MariaDB/server/commit/dc90234bda)\
  2018-12-28 01:47:17 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #830a7c67a4](https://github.com/MariaDB/server/commit/830a7c67a4)\
  2018-12-27 22:56:10 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #db9b96ef02](https://github.com/MariaDB/server/commit/db9b96ef02)\
  2018-12-28 13:22:44 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441): Pointer indirection for buf\_block\_t::debug\_latch
* [Revision #0e11d96a84](https://github.com/MariaDB/server/commit/0e11d96a84)\
  2018-12-28 09:56:46 +0200
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441): Pointer indirection for buf\_block\_t::debug\_latch
* [Revision #aa4e8dfdf9](https://github.com/MariaDB/server/commit/aa4e8dfdf9)\
  2018-12-28 09:45:35 +0200
  * fts\_fetch\_doc\_from\_rec(): Remove redundant variables
* [Revision #c4ec6bb69e](https://github.com/MariaDB/server/commit/c4ec6bb69e)\
  2018-12-28 00:15:29 +0100
  * "flush ssl" ASAN warnings with yassl
* [Revision #0ce7f6b0bf](https://github.com/MariaDB/server/commit/0ce7f6b0bf)\
  2018-12-27 18:32:09 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #f401ba477c](https://github.com/MariaDB/server/commit/f401ba477c)\
  2018-12-27 00:54:39 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #5cc6b48f39](https://github.com/MariaDB/server/commit/5cc6b48f39)\
  2018-12-27 00:34:18 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #4ef481f5bc](https://github.com/MariaDB/server/commit/4ef481f5bc)\
  2018-12-26 23:59:17 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #dbd40edfe6](https://github.com/MariaDB/server/commit/dbd40edfe6)\
  2018-10-25 19:13:05 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #66ec8adb77](https://github.com/MariaDB/server/commit/66ec8adb77)\
  2018-10-25 18:59:08 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #edde1f6e0d](https://github.com/MariaDB/server/commit/edde1f6e0d)\
  2018-10-25 17:37:16 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #de32e66336](https://github.com/MariaDB/server/commit/de32e66336)\
  2018-10-25 13:28:14 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #b1c3e6c2f2](https://github.com/MariaDB/server/commit/b1c3e6c2f2)\
  2018-10-14 22:44:14 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #d93653bf96](https://github.com/MariaDB/server/commit/d93653bf96)\
  2018-10-14 16:23:45 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #8c82ca171e](https://github.com/MariaDB/server/commit/8c82ca171e)\
  2018-10-14 16:01:49 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #e60dc209d4](https://github.com/MariaDB/server/commit/e60dc209d4)\
  2018-10-14 15:10:31 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #9581c4a8f5](https://github.com/MariaDB/server/commit/9581c4a8f5)\
  2018-10-14 13:44:49 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #4404ee2901](https://github.com/MariaDB/server/commit/4404ee2901)\
  2018-10-14 12:53:52 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #dab38ce023](https://github.com/MariaDB/server/commit/dab38ce023)\
  2018-10-14 00:24:48 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #e976c7dbf2](https://github.com/MariaDB/server/commit/e976c7dbf2)\
  2018-10-13 23:22:05 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #6a150e26d9](https://github.com/MariaDB/server/commit/6a150e26d9)\
  2018-10-13 22:52:44 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #601f45fdcd](https://github.com/MariaDB/server/commit/601f45fdcd)\
  2018-10-13 22:16:50 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #2e5d35961d](https://github.com/MariaDB/server/commit/2e5d35961d)\
  2018-10-13 21:48:59 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #5c657e9fa5](https://github.com/MariaDB/server/commit/5c657e9fa5)\
  2018-10-13 21:31:12 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #67dbfe6e9c](https://github.com/MariaDB/server/commit/67dbfe6e9c)\
  2018-09-19 21:37:04 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #4abdd798f7](https://github.com/MariaDB/server/commit/4abdd798f7)\
  2018-09-19 21:01:57 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #8023fc6d45](https://github.com/MariaDB/server/commit/8023fc6d45)\
  2018-09-19 20:55:50 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #90377b8028](https://github.com/MariaDB/server/commit/90377b8028)\
  2018-09-19 20:51:35 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #03e461634d](https://github.com/MariaDB/server/commit/03e461634d)\
  2018-09-19 20:34:03 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #ca83115b3e](https://github.com/MariaDB/server/commit/ca83115b3e)\
  2018-12-26 16:49:11 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #88b7b8199a](https://github.com/MariaDB/server/commit/88b7b8199a)\
  2018-12-27 16:28:22 +0200
  * [MDEV-18076](https://jira.mariadb.org/browse/MDEV-18076)/[MDEV-18077](https://jira.mariadb.org/browse/MDEV-18077) Crash on AUTO\_INCREMENT column after instant DROP
* [Revision #003720755f](https://github.com/MariaDB/server/commit/003720755f)\
  2018-12-27 15:32:26 +0200
  * [MDEV-18033](https://jira.mariadb.org/browse/MDEV-18033)/[MDEV-18034](https://jira.mariadb.org/browse/MDEV-18034): Assertion failed on NOT NULL removal
* [Revision #3b5e8d799a](https://github.com/MariaDB/server/commit/3b5e8d799a)\
  2018-12-26 16:55:54 +0000
  * travis: Fix ccache not used on macOS targets
* [Revision #f409eb4d36](https://github.com/MariaDB/server/commit/f409eb4d36)\
  2018-12-27 10:32:33 +0400
  * [MDEV-17959](https://jira.mariadb.org/browse/MDEV-17959) Assertion \`opt\_bootstrap || mysql\_parse\_status || thd->lex->select\_stack\_top == 0' failed in parse\_sql upon DELETE HISTORY under ORACLE mode
* [Revision #829fce9ea6](https://github.com/MariaDB/server/commit/829fce9ea6)\
  2018-12-25 12:01:13 +0000
  * travis: upgrade Ubuntu target dist to 16.04 Xenial
* Merge [Revision #838c196f26](https://github.com/MariaDB/server/commit/838c196f26) 2018-12-25 11:39:13 +0000 - Merge pull request #937 from grooverdan/10.4-travis
* [Revision #85c9c07cd6](https://github.com/MariaDB/server/commit/85c9c07cd6)\
  2018-11-23 11:46:52 +1100
  * travis: clang - C{,XX}FLAGS=-Wno-unused-command-line-argument
* [Revision #00c5c225a1](https://github.com/MariaDB/server/commit/00c5c225a1)\
  2018-11-23 11:11:45 +1100
  * travis: add CC\_VERSION=8
* [Revision #83b7372b29](https://github.com/MariaDB/server/commit/83b7372b29)\
  2018-11-23 10:41:38 +1100
  * travis: update CC\_VERSIONS to 6 and 7
* [Revision #ca619ed123](https://github.com/MariaDB/server/commit/ca619ed123)\
  2018-12-25 10:23:20 +0400
  * [MDEV-18072](https://jira.mariadb.org/browse/MDEV-18072) Assertion \`is\_null() == item->null\_value || conv' failed in Timestamp\_or\_zero\_datetime\_native\_null::Timestamp\_or\_zero\_datetime\_native\_null upon query with GROUP BY
* [Revision #7d7df70c11](https://github.com/MariaDB/server/commit/7d7df70c11)\
  2018-12-25 08:31:09 +0400
  * [MDEV-18070](https://jira.mariadb.org/browse/MDEV-18070) Assertion \`nanoseconds <= 1000000000' failed in Temporal::add\_nanoseconds\_ssff with TIME\_ROUND\_FRACTIONAL
* [Revision #b316989223](https://github.com/MariaDB/server/commit/b316989223)\
  2018-12-25 08:27:07 +0400
  * [MDEV-18072](https://jira.mariadb.org/browse/MDEV-18072) Assertion \`is\_null() == item->null\_value || conv' failed in Timestamp\_or\_zero\_datetime\_native\_null::Timestamp\_or\_zero\_datetime\_native\_null upon query with GROUP BY
* [Revision #a8eb0c76bf](https://github.com/MariaDB/server/commit/a8eb0c76bf)\
  2018-12-21 16:40:42 +0200
  * [MDEV-18048](https://jira.mariadb.org/browse/MDEV-18048): Relax a too strict debug assertion
* [Revision #ccb1acbd3c](https://github.com/MariaDB/server/commit/ccb1acbd3c)\
  2018-12-21 16:38:12 +0200
  * [MDEV-18035](https://jira.mariadb.org/browse/MDEV-18035) Failing assertion on DELETE
* [Revision #2fe40a7af0](https://github.com/MariaDB/server/commit/2fe40a7af0)\
  2018-12-20 14:21:14 +0200
  * [MDEV-18009](https://jira.mariadb.org/browse/MDEV-18009) Missing redo log flush in innodb.instant\_alter\_crash
* [Revision #505f283189](https://github.com/MariaDB/server/commit/505f283189)\
  2018-12-20 11:07:40 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
