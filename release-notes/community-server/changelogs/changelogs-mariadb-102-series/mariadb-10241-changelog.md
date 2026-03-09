# MariaDB 10.2.41 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download 10.2.41](https://mariadb.org/download/?tab=mariadb\&release=10.2.41\&product=mariadb)[Release Notes](../../old-releases/10.2/10.2.41.md)[Changelog](mariadb-10241-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 8 Nov 2021

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.41.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #561b6c7e51](https://github.com/MariaDB/server/commit/561b6c7e51)\
  2021-10-25 18:25:03 +0300
  * [MDEV-26833](https://jira.mariadb.org/browse/MDEV-26833) Missed statement rollback in case transaction drops or create temporary table
* [Revision #e571eaae9f](https://github.com/MariaDB/server/commit/e571eaae9f)\
  2021-11-02 07:20:30 +0200
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* [Revision #ea239034de](https://github.com/MariaDB/server/commit/ea239034de)\
  2021-11-01 13:07:55 +0200
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* [Revision #db50ea3ad3](https://github.com/MariaDB/server/commit/db50ea3ad3)\
  2021-10-21 14:49:51 +0300
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* [Revision #c8b39f7ee2](https://github.com/MariaDB/server/commit/c8b39f7ee2)\
  2021-10-21 13:48:59 +0300
  * [MDEV-25114](https://jira.mariadb.org/browse/MDEV-25114): Crash: WSREP: invalid state ROLLED\_BACK (FATAL)
* [Revision #b3cdf4168c](https://github.com/MariaDB/server/commit/b3cdf4168c)\
  2021-10-28 12:24:31 +0200
  * fix depricated pthread\_yield() for tokudb
* Merge [Revision #99c893586c](https://github.com/MariaDB/server/commit/99c893586c) 2021-10-28 10:30:36 +0200 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #94fb9d9377](https://github.com/MariaDB/server/commit/94fb9d9377)\
  2021-10-15 12:20:33 +0200
  * Fix [MDEV-24493](https://jira.mariadb.org/browse/MDEV-24493)
* [Revision #46fed496b6](https://github.com/MariaDB/server/commit/46fed496b6)\
  2021-07-31 11:20:09 +0200
  * Fix bson crash and mongo test
* [Revision #1d468ee040](https://github.com/MariaDB/server/commit/1d468ee040)\
  2021-07-30 10:45:26 +0200
  * Fix slow processing of pretty json files by BSON tables
* [Revision #ff3274dd7c](https://github.com/MariaDB/server/commit/ff3274dd7c)\
  2021-10-27 21:52:35 +0200
  * Fix message severity for "thread pool blocked" messages.
* [Revision #563daec123](https://github.com/MariaDB/server/commit/563daec123)\
  2021-10-28 07:35:49 +0300
  * [MDEV-26867](https://jira.mariadb.org/browse/MDEV-26867): Update the InnoDB version number to 5.7.36
* [Revision #1f5ca66e53](https://github.com/MariaDB/server/commit/1f5ca66e53)\
  2021-10-27 18:37:33 +0300
  * [MDEV-26866](https://jira.mariadb.org/browse/MDEV-26866) FOREIGN KEY…SET NULL corrupts an index on a virtual column
* [Revision #3a9967d757](https://github.com/MariaDB/server/commit/3a9967d757)\
  2021-10-27 10:13:56 +0300
  * Fix compile warning:
* [Revision #2ed148c8d7](https://github.com/MariaDB/server/commit/2ed148c8d7)\
  2021-10-27 10:50:15 +0400
  * [MDEV-25402](https://jira.mariadb.org/browse/MDEV-25402) Assertion \`!str || str != Ptr' failed in String::copy
* [Revision #4b8340d899](https://github.com/MariaDB/server/commit/4b8340d899)\
  2021-10-27 08:54:06 +0300
  * Fix tests for PLUGIN\_PARTITION=NO
* [Revision #d062b69037](https://github.com/MariaDB/server/commit/d062b69037)\
  2021-10-26 11:01:11 +0200
  * [MDEV-26868](https://jira.mariadb.org/browse/MDEV-26868): Session tracking flag in OK\_PACKET
* [Revision #1f70e4b00c](https://github.com/MariaDB/server/commit/1f70e4b00c)\
  2021-10-25 22:21:27 +0200
  * pthread\_yield() is depricated now, so use sched\_yield() if possible.
* [Revision #1fb4537e6f](https://github.com/MariaDB/server/commit/1fb4537e6f)\
  2021-10-25 22:20:29 +0200
  * Safemalloc typo fix found by clang.
* [Revision #2084800768](https://github.com/MariaDB/server/commit/2084800768)\
  2021-10-19 11:09:06 +0200
  * Try to fix appveyor to prevent occasional failing of mysql\_client\_test
* [Revision #6211c35549](https://github.com/MariaDB/server/commit/6211c35549)\
  2021-10-19 11:06:32 +0200
  * [MDEV-23391](https://jira.mariadb.org/browse/MDEV-23391) Crash/assertion CREATE OR REPLACE TABLE AS SELECT under LOCK TABLE
* [Revision #81b8547697](https://github.com/MariaDB/server/commit/81b8547697)\
  2021-10-26 15:57:54 +0530
  * [MDEV-26902](https://jira.mariadb.org/browse/MDEV-26902) Auxilary fts table evicts during DDL
* [Revision #efedf3da68](https://github.com/MariaDB/server/commit/efedf3da68)\
  2021-10-20 14:53:01 +0400
  * [MDEV-22711](https://jira.mariadb.org/browse/MDEV-22711) Assertion \`nr != 0' failed in handler::update\_auto\_increment.
* [Revision #d627d00b13](https://github.com/MariaDB/server/commit/d627d00b13)\
  2021-10-21 15:11:20 +0400
  * [MDEV-26556](https://jira.mariadb.org/browse/MDEV-26556) An improper locking bug(s) due to unreleased lock.
* [Revision #d22c8cae00](https://github.com/MariaDB/server/commit/d22c8cae00)\
  2021-10-25 10:48:24 +0200
  * compilation fixes for sys-devel/gcc-11.2.0:11
* [Revision #481aa0af46](https://github.com/MariaDB/server/commit/481aa0af46)\
  2021-10-25 15:14:43 +0300
  * [MDEV-23267](https://jira.mariadb.org/browse/MDEV-23267) Assertion on --bootstrap --innodb-force-recovery
* [Revision #a441a56915](https://github.com/MariaDB/server/commit/a441a56915)\
  2021-10-20 19:53:49 +0300
  * Fix comment
* [Revision #7d6617e966](https://github.com/MariaDB/server/commit/7d6617e966)\
  2021-10-21 15:21:44 +0300
  * [MDEV-19129](https://jira.mariadb.org/browse/MDEV-19129): Xcode compatibility update: mysql-test-run.pl: rename $opt\_vs\_config to $multiconfig to use with other cmake multiconfig generators
* [Revision #39f63f6643](https://github.com/MariaDB/server/commit/39f63f6643)\
  2021-10-21 15:53:35 +0300
  * [MDEV-19522](https://jira.mariadb.org/browse/MDEV-19522) fixup: Use correct printf format
* [Revision #fbb1e92e25](https://github.com/MariaDB/server/commit/fbb1e92e25)\
  2021-10-21 14:35:23 +0300
  * [MDEV-19522](https://jira.mariadb.org/browse/MDEV-19522) fixup: Integer type mismatch in unit test
* [Revision #1a2308d3f4](https://github.com/MariaDB/server/commit/1a2308d3f4)\
  2021-10-21 12:57:09 +0300
  * [MDEV-26865](https://jira.mariadb.org/browse/MDEV-26865): Add test case and instrumentation
* [Revision #2d98b967e3](https://github.com/MariaDB/server/commit/2d98b967e3)\
  2021-10-21 12:44:27 +0300
  * [MDEV-26865](https://jira.mariadb.org/browse/MDEV-26865) fts\_optimize\_thread cannot keep up with workload
* [Revision #c484a358c8](https://github.com/MariaDB/server/commit/c484a358c8)\
  2021-10-21 12:29:33 +0300
  * [MDEV-26864](https://jira.mariadb.org/browse/MDEV-26864) Race condition between transaction commit and undo log truncation
* [Revision #8ce8c269f4](https://github.com/MariaDB/server/commit/8ce8c269f4)\
  2021-10-06 18:50:56 +0530
  * [MDEV-19522](https://jira.mariadb.org/browse/MDEV-19522) InnoDB commit fails when FTS\_DOC\_ID value is greater than 4294967295
* [Revision #6b4fad9402](https://github.com/MariaDB/server/commit/6b4fad9402)\
  2021-10-21 12:27:38 +0300
  * [MDEV-22627](https://jira.mariadb.org/browse/MDEV-22627) fixup: Add a type cast for 32-bit platforms
* [Revision #d3426c4c0c](https://github.com/MariaDB/server/commit/d3426c4c0c)\
  2021-10-21 12:26:54 +0300
  * [MDEV-26262](https://jira.mariadb.org/browse/MDEV-26262) fixup: Remove a bogus assertion
* [Revision #2e844a08f7](https://github.com/MariaDB/server/commit/2e844a08f7)\
  2021-10-21 11:54:01 +0300
  * [MDEV-19129](https://jira.mariadb.org/browse/MDEV-19129): Xcode compatibility update: mysql-test-run.pl
* [Revision #05c3dced86](https://github.com/MariaDB/server/commit/05c3dced86)\
  2021-10-20 22:16:23 +0300
  * [MDEV-22627](https://jira.mariadb.org/browse/MDEV-22627) fixup: Cover also ALTER TABLE...ALGORITHM=INPLACE
* [Revision #69b3de830d](https://github.com/MariaDB/server/commit/69b3de830d)\
  2021-10-20 15:55:27 +0300
  * Update libmariadb
* [Revision #b06e8167a7](https://github.com/MariaDB/server/commit/b06e8167a7)\
  2021-10-20 15:54:25 +0300
  * [MDEV-22627](https://jira.mariadb.org/browse/MDEV-22627) Failing assertion: dict\_tf2\_is\_valid(flags, flags2)
* [Revision #caebe151c1](https://github.com/MariaDB/server/commit/caebe151c1)\
  2021-10-07 17:02:26 +0300
  * [MDEV-22445](https://jira.mariadb.org/browse/MDEV-22445) Crash on HANDLER READ NEXT after XA PREPARE
* [Revision #1811fd51fb](https://github.com/MariaDB/server/commit/1811fd51fb)\
  2021-08-02 14:24:54 +0300
  * [MDEV-26262](https://jira.mariadb.org/browse/MDEV-26262) frm is corrupted after ER\_EXPRESSION\_REFERS\_TO\_UNINIT\_FIELD
* [Revision #a8401ad5af](https://github.com/MariaDB/server/commit/a8401ad5af)\
  2021-07-21 15:42:21 +0300
  * restore default.test, default.result after [MDEV-23597](https://jira.mariadb.org/browse/MDEV-23597) c47e4aab62c65 commit
* [Revision #1a54cf62f8](https://github.com/MariaDB/server/commit/1a54cf62f8)\
  2021-10-11 15:05:44 +0400
  * [MDEV-24585](https://jira.mariadb.org/browse/MDEV-24585) Assertion \`je->s.cs == nice\_js->charset()' failed in json\_nice.
* [Revision #5316703141](https://github.com/MariaDB/server/commit/5316703141)\
  2021-10-19 08:46:16 +0300
  * [MDEV-14804](https://jira.mariadb.org/browse/MDEV-14804) innodb.update\_time failed in buildbot with wrong result
* [Revision #27bf57fd6d](https://github.com/MariaDB/server/commit/27bf57fd6d)\
  2021-10-01 14:46:22 +0200
  * [MDEV-26299](https://jira.mariadb.org/browse/MDEV-26299): Some views force server (and mysqldump) to generate invalid SQL for their definitions
* [Revision #2291f8ef73](https://github.com/MariaDB/server/commit/2291f8ef73)\
  2021-10-13 07:31:32 -0600
  * [MDEV-25284](https://jira.mariadb.org/browse/MDEV-25284): Assertion \`info->type == READ\_CACHE || info->type == WRITE\_CACHE' failed
* [Revision #5f63f5dc60](https://github.com/MariaDB/server/commit/5f63f5dc60)\
  2021-10-15 21:56:17 +0400
  * A clean-up patch for [MDEV-23408](https://jira.mariadb.org/browse/MDEV-23408): fixing test failure on Windows
* [Revision #9e6c383867](https://github.com/MariaDB/server/commit/9e6c383867)\
  2021-10-13 13:13:27 +0300
  * [MDEV-17964](https://jira.mariadb.org/browse/MDEV-17964): Assertion \`status == 0' failed in add\_role\_user\_mapping\_action
* [Revision #a2a42f4eba](https://github.com/MariaDB/server/commit/a2a42f4eba)\
  2021-10-13 12:57:57 +0400
  * [MDEV-23408](https://jira.mariadb.org/browse/MDEV-23408) Wrong result upon query from I\_S and further Assertion \`!alias\_arg || strlen(alias\_arg->str) == alias\_arg->length' failed with certain connection charset
* [Revision #bbae2d398f](https://github.com/MariaDB/server/commit/bbae2d398f)\
  2021-09-29 19:19:38 +0300
  * [MDEV-26712](https://jira.mariadb.org/browse/MDEV-26712) row events never reset thd->mem\_root
* [Revision #ef0dc50c05](https://github.com/MariaDB/server/commit/ef0dc50c05)\
  2021-10-13 11:56:33 +0300
  * [MDEV-26815](https://jira.mariadb.org/browse/MDEV-26815) : galera.galera\_ftwrl\_drain fails with wrong errno 1146
* [Revision #2bb8d7c2f3](https://github.com/MariaDB/server/commit/2bb8d7c2f3)\
  2021-10-13 10:38:41 +0300
  * [MDEV-26811](https://jira.mariadb.org/browse/MDEV-26811): Assertion "log\_sys->n\_pending\_flushes == 1" fails
* [Revision #6f32b28be5](https://github.com/MariaDB/server/commit/6f32b28be5)\
  2021-10-06 11:31:08 +0300
  * Xcode compatibility update
* [Revision #8f04ec2885](https://github.com/MariaDB/server/commit/8f04ec2885)\
  2021-10-09 22:27:31 +0400
  * [MDEV-25925](https://jira.mariadb.org/browse/MDEV-25925) Warning: Memory not freed: 32 on INSERT DELAYED
* [Revision #eadd878808](https://github.com/MariaDB/server/commit/eadd878808)\
  2021-10-08 20:44:38 +0400
  * [MDEV-23269](https://jira.mariadb.org/browse/MDEV-23269) SIGSEGV in ft\_boolean\_check\_syntax\_string on setting ft\_boolean\_syntax
* [Revision #9300b66577](https://github.com/MariaDB/server/commit/9300b66577)\
  2021-10-10 18:42:32 +0400
  * [MDEV-24742](https://jira.mariadb.org/browse/MDEV-24742) Server crashes in Charset::numchars / String::numchars
* [Revision #5e3e5ccbea](https://github.com/MariaDB/server/commit/5e3e5ccbea)\
  2021-10-11 08:26:33 -0400
  * Apple Silicon is a 64-bit platform (#1922)
* [Revision #89936f11e9](https://github.com/MariaDB/server/commit/89936f11e9)\
  2021-09-28 16:00:41 +0300
  * [MDEV-18278](https://jira.mariadb.org/browse/MDEV-18278) Misleading error message in error log upon failed table creation
* [Revision #275e7d23f7](https://github.com/MariaDB/server/commit/275e7d23f7)\
  2021-09-22 19:09:37 +0300
  * [MDEV-14846](https://jira.mariadb.org/browse/MDEV-14846) InnoDB: assertion on trx->state because of deadlock error ignored
* [Revision #1d71dacd51](https://github.com/MariaDB/server/commit/1d71dacd51)\
  2021-10-11 10:15:52 +0300
  * [MDEV-24454](https://jira.mariadb.org/browse/MDEV-24454) fixup: Fix plugins.feedback\_plugin\_send
* [Revision #26eb666463](https://github.com/MariaDB/server/commit/26eb666463)\
  2021-10-08 19:17:06 +0300
  * Make Explain\_node::children protected
* [Revision #478020171d](https://github.com/MariaDB/server/commit/478020171d)\
  2021-10-07 11:28:49 -0600
  * [MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444): mysql --binary-mode is not able to replay some mysqlbinlog outputs
* [Revision #1ce35c327e](https://github.com/MariaDB/server/commit/1ce35c327e)\
  2021-10-06 07:42:03 -0600
  * [MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444): mysql --binary-mode is not able to replay some mysqlbinlog outputs
* [Revision #d28b118d7b](https://github.com/MariaDB/server/commit/d28b118d7b)\
  2021-10-03 16:49:54 +0200
  * Fix MSVC warning with bison 3.8.2
* [Revision #d5a15f04f4](https://github.com/MariaDB/server/commit/d5a15f04f4)\
  2021-09-29 11:24:18 +0300
  * [MDEV-24978](https://jira.mariadb.org/browse/MDEV-24978) crash with transaction on table with no PK and long fulltext column
* [Revision #b2a5e0f282](https://github.com/MariaDB/server/commit/b2a5e0f282)\
  2021-09-29 12:13:11 +0300
  * Make innodb.innodb\_defrag\_stats more deterministic
* [Revision #3690c549c6](https://github.com/MariaDB/server/commit/3690c549c6)\
  2021-07-23 11:14:13 +0200
  * [MDEV-24454](https://jira.mariadb.org/browse/MDEV-24454) Crash at change\_item\_tree
* [Revision #1a62c87897](https://github.com/MariaDB/server/commit/1a62c87897)\
  2021-09-27 08:25:22 +0300
  * Remove test from galera\_fulltext until [MDEV-24978](https://jira.mariadb.org/browse/MDEV-24978) is fixed.
* [Revision #f59f5c4a10](https://github.com/MariaDB/server/commit/f59f5c4a10)\
  2021-09-24 16:21:20 +0300
  * Revert [MDEV-25114](https://jira.mariadb.org/browse/MDEV-25114)
* [Revision #cfe1a258e8](https://github.com/MariaDB/server/commit/cfe1a258e8)\
  2021-09-24 15:33:53 +0300
  * Update libmariadb
* [Revision #77b1196522](https://github.com/MariaDB/server/commit/77b1196522)\
  2021-09-23 16:14:54 +0200
  * [MDEV-26360](https://jira.mariadb.org/browse/MDEV-26360): Using hostnames breaks certificate validation
* [Revision #467011bcac](https://github.com/MariaDB/server/commit/467011bcac)\
  2021-09-22 18:08:50 +0700
  * [MDEV-26612](https://jira.mariadb.org/browse/MDEV-26612) Two different ways to start MariaDB service can cause data corruption
* [Revision #47ba552304](https://github.com/MariaDB/server/commit/47ba552304)\
  2021-09-24 07:33:27 +0300
  * Revert "[MDEV-24978](https://jira.mariadb.org/browse/MDEV-24978) : SIGABRT in libc\_message"
* [Revision #88a4be75a5](https://github.com/MariaDB/server/commit/88a4be75a5)\
  2021-09-15 09:16:44 +0300
  * [MDEV-25114](https://jira.mariadb.org/browse/MDEV-25114) Crash: WSREP: invalid state ROLLED\_BACK (FATAL)
* [Revision #9d97f92feb](https://github.com/MariaDB/server/commit/9d97f92feb)\
  2021-09-13 08:19:29 +0300
  * Revert "[MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution" and Revert "[MDEV-24873](https://jira.mariadb.org/browse/MDEV-24873) galera.galera\_as\_slave\_ctas MTR failed:..."
* [Revision #1cb218c37c](https://github.com/MariaDB/server/commit/1cb218c37c)\
  2021-09-22 14:15:00 +0300
  * [MDEV-26450](https://jira.mariadb.org/browse/MDEV-26450): Corruption due to innodb\_undo\_log\_truncate
* [Revision #21d19ed45b](https://github.com/MariaDB/server/commit/21d19ed45b)\
  2021-09-21 18:02:04 +0300
  * Silence a warning about unused Bison label
* [Revision #ac1c6738f9](https://github.com/MariaDB/server/commit/ac1c6738f9)\
  2021-09-22 17:54:22 +0800
  * [MDEV-26545](https://jira.mariadb.org/browse/MDEV-26545) Spider does not correctly handle UDF and stored function in where conds
* [Revision #f4d6d01782](https://github.com/MariaDB/server/commit/f4d6d01782)\
  2021-09-20 12:10:53 +0200
  * [MDEV-26441](https://jira.mariadb.org/browse/MDEV-26441): Linux-dependent construct in SST scripts
* [Revision #3209bc667f](https://github.com/MariaDB/server/commit/3209bc667f)\
  2021-09-18 15:47:52 +0300
  * [MDEV-26636](https://jira.mariadb.org/browse/MDEV-26636): InnoDB defragmentation statistics cause races on TEMPORARY TABLE
* [Revision #496d3dded4](https://github.com/MariaDB/server/commit/496d3dded4)\
  2021-09-17 19:37:29 +0530
  * [MDEV-15675](https://jira.mariadb.org/browse/MDEV-15675) encryption.innodb\_encryption failed in buildbot with timeout
* [Revision #dce490e9d4](https://github.com/MariaDB/server/commit/dce490e9d4)\
  2021-09-15 16:37:54 +0200
  * Give less memory to get reliable error.
* [Revision #dabc3329c3](https://github.com/MariaDB/server/commit/dabc3329c3)\
  2021-09-16 20:42:26 +1000
  * [MDEV-26622](https://jira.mariadb.org/browse/MDEV-26622): man mysqldump - insert-ignore not insert-into
* [Revision #b1351c1594](https://github.com/MariaDB/server/commit/b1351c1594)\
  2021-09-15 14:55:45 +0200
  * [MDEV-26574](https://jira.mariadb.org/browse/MDEV-26574) An improper locking bug due to unreleased lock in the ds\_xbstream.cc
* [Revision #8937762ead](https://github.com/MariaDB/server/commit/8937762ead)\
  2021-09-15 14:19:24 +0200
  * [MDEV-26573](https://jira.mariadb.org/browse/MDEV-26573) : A static analyzer warning about ds\_archive.cc
* [Revision #696de6d06c](https://github.com/MariaDB/server/commit/696de6d06c)\
  2021-09-13 12:37:07 +0530
  * [MDEV-25702](https://jira.mariadb.org/browse/MDEV-25702) Auxiliary FTS table evicts during optimize table
* [Revision #f345172379](https://github.com/MariaDB/server/commit/f345172379)\
  2021-09-10 21:40:19 +0200
  * [MDEV-26527](https://jira.mariadb.org/browse/MDEV-26527) speedup appveyor build - 10.2
* [Revision #3504f70f7f](https://github.com/MariaDB/server/commit/3504f70f7f)\
  2021-09-11 13:08:13 +0200
  * Bison 3.7 - fix "conversion from 'ptrdiff\_t' to 'ulong', possible loss of data"
* [Revision #879e21b68c](https://github.com/MariaDB/server/commit/879e21b68c)\
  2021-09-10 19:32:56 +0200
  * Define minbuild target for 10.2
* [Revision #7e6b033507](https://github.com/MariaDB/server/commit/7e6b033507)\
  2021-09-10 18:10:54 +0200
  * Fix MYSQL\_MAINTAINER\_MODE=ERR, on Windows, with Ninja , in 10.2
* [Revision #ac064c2b47](https://github.com/MariaDB/server/commit/ac064c2b47)\
  2021-09-11 11:12:11 +0300
  * Fix an occasional timeout in innodb.alter\_partitioned
* [Revision #d09426f9e6](https://github.com/MariaDB/server/commit/d09426f9e6)\
  2021-09-10 19:15:41 +0300
  * [MDEV-26537](https://jira.mariadb.org/browse/MDEV-26537) InnoDB corrupts files due to incorrect st\_blksize calculation
* [Revision #1c378f1b95](https://github.com/MariaDB/server/commit/1c378f1b95)\
  2021-09-10 12:02:44 +0200
  * Speedup build of the MSI package
* [Revision #c7184c470e](https://github.com/MariaDB/server/commit/c7184c470e)\
  2021-09-09 09:57:39 +0200
  * fix main.truncate failures in --embedded
* [Revision #0d3de06eda](https://github.com/MariaDB/server/commit/0d3de06eda)\
  2021-09-07 13:21:48 +0200
  * disable bzip2/lz4/lzo in rpm builds, distro dependent
* [Revision #ca2f89deac](https://github.com/MariaDB/server/commit/ca2f89deac)\
  2021-09-07 09:28:57 +0200
  * disable bzip2/lz4/lzo in bintar builds, as they always have been
* [Revision #630d722902](https://github.com/MariaDB/server/commit/630d722902)\
  2019-04-10 03:35:01 -0700
  * [MDEV-19227](https://jira.mariadb.org/browse/MDEV-19227): mysql\_plugin doesn't run bootstrap from source
* [Revision #528abc749e](https://github.com/MariaDB/server/commit/528abc749e)\
  2021-05-02 15:43:04 -0500
  * [MDEV-25325](https://jira.mariadb.org/browse/MDEV-25325) built-in documentation for performance\_schema tables
* [Revision #edde990e35](https://github.com/MariaDB/server/commit/edde990e35)\
  2021-07-26 16:31:22 +0530
  * [MDEV-23365](https://jira.mariadb.org/browse/MDEV-23365): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed upon killed TRUNCATE
* [Revision #f17537579a](https://github.com/MariaDB/server/commit/f17537579a)\
  2021-09-06 09:49:53 +0200
  * disable cmake feature summary after the first run
* [Revision #38648bbbf5](https://github.com/MariaDB/server/commit/38648bbbf5)\
  2021-09-06 09:10:52 +1000
  * [MDEV-12055](https://jira.mariadb.org/browse/MDEV-12055) binlog.binlog\_stm\_ctype\_ucs postfix
* [Revision #21d31b9970](https://github.com/MariaDB/server/commit/21d31b9970)\
  2021-09-06 08:47:54 +1000
  * [MDEV-26529](https://jira.mariadb.org/browse/MDEV-26529): binlog.binlog\_flush\_binlogs\_delete\_domain fails on RISC-V
* [Revision #f55477060c](https://github.com/MariaDB/server/commit/f55477060c)\
  2021-09-01 14:30:18 +0300
  * [MDEV-26518](https://jira.mariadb.org/browse/MDEV-26518) ; Galera incorrectly handles primary or unique keys with any multi-byte character set
* [Revision #99f6a266c8](https://github.com/MariaDB/server/commit/99f6a266c8)\
  2021-09-01 09:25:52 +0300
  * [MDEV-26517](https://jira.mariadb.org/browse/MDEV-26517) : Galera test failure on galera\_fk\_cascade\_delete\_debug
* [Revision #5613ead49e](https://github.com/MariaDB/server/commit/5613ead49e)\
  2021-09-01 19:17:48 +0200
  * [MDEV-26521](https://jira.mariadb.org/browse/MDEV-26521) Remove [MDEV-504](https://jira.mariadb.org/browse/MDEV-504).test
* [Revision #d6b7738dcc](https://github.com/MariaDB/server/commit/d6b7738dcc)\
  2021-09-01 18:21:34 +0200
  * Fix potential null pointer access after the allocation error
* [Revision #234ae43d5a](https://github.com/MariaDB/server/commit/234ae43d5a)\
  2021-09-01 18:18:34 +0200
  * Cleanup - remove confusing comment.
* [Revision #a4a4d6a7c8](https://github.com/MariaDB/server/commit/a4a4d6a7c8)\
  2021-09-01 03:53:27 +0300
  * [MDEV-26514](https://jira.mariadb.org/browse/MDEV-26514) Option to build a separate test zip package on Windows
* [Revision #8382c3260b](https://github.com/MariaDB/server/commit/8382c3260b)\
  2021-08-31 21:13:13 +0300
  * [MDEV-26514](https://jira.mariadb.org/browse/MDEV-26514) Option to build a separate test zip package on Windows
* [Revision #1597b3d76b](https://github.com/MariaDB/server/commit/1597b3d76b)\
  2021-08-29 23:19:42 +0200
  * disable bzip2, lzma, and lzo explicitly in debian release builds
* [Revision #ceb40ef45b](https://github.com/MariaDB/server/commit/ceb40ef45b)\
  2021-08-30 14:26:27 +0300
  * [MDEV-26504](https://jira.mariadb.org/browse/MDEV-26504) THD::copy\_db\_to() fails to return true if THD::db is null
* [Revision #fda704c82c](https://github.com/MariaDB/server/commit/fda704c82c)\
  2021-08-30 11:52:59 +0300
  * Fix GCC 11 -Wmaybe-uninitialized for PLUGIN\_PERFSCHEMA
* [Revision #969edf02c5](https://github.com/MariaDB/server/commit/969edf02c5)\
  2021-08-30 11:10:43 +0300
  * Update libmariadb
* [Revision #600e494906](https://github.com/MariaDB/server/commit/600e494906)\
  2021-08-29 09:33:00 +0200
  * mtr: fix the check where a combination is pre-selected
* [Revision #fe2a7048e7](https://github.com/MariaDB/server/commit/fe2a7048e7)\
  2021-08-26 15:13:48 +0200
  * typo fixed
* [Revision #228630f61a](https://github.com/MariaDB/server/commit/228630f61a)\
  2021-08-25 16:53:39 +1000
  * rocksdb: disable on arm64 except for Linux
* [Revision #c45aeeab38](https://github.com/MariaDB/server/commit/c45aeeab38)\
  2021-08-25 09:18:29 +0200
  * Remove FLUSH PRIVILEGES from mysql\_setpermission
* [Revision #683f91a287](https://github.com/MariaDB/server/commit/683f91a287)\
  2021-08-25 09:15:24 +0200
  * Fix mysql\_setpermission hostname logic
* [Revision #ece30d47ca](https://github.com/MariaDB/server/commit/ece30d47ca)\
  2021-07-08 21:47:38 +1000
  * [MDEV-26109](https://jira.mariadb.org/browse/MDEV-26109): s390x detected as 32bit in mtr tests
* [Revision #1f1d5606e0](https://github.com/MariaDB/server/commit/1f1d5606e0)\
  2021-08-23 15:14:54 +0300
  * Disable 2 commonly failing innodb\_gis tests
* [Revision #4ee9e06642](https://github.com/MariaDB/server/commit/4ee9e06642)\
  2021-08-23 16:47:25 +0600
  * fix clang build
* [Revision #ca89489716](https://github.com/MariaDB/server/commit/ca89489716)\
  2021-08-23 10:06:21 +0300
  * [MDEV-26383](https://jira.mariadb.org/browse/MDEV-26383) fixup: Consistently protect freed\_indexes with autoinc\_mutex
* [Revision #08e5a3d2e3](https://github.com/MariaDB/server/commit/08e5a3d2e3)\
  2021-08-19 16:46:01 +0530
  * [MDEV-26383](https://jira.mariadb.org/browse/MDEV-26383) ASAN heap-use-after-free failure in btr\_search\_lazy\_free
* [Revision #557bb344e4](https://github.com/MariaDB/server/commit/557bb344e4)\
  2021-08-20 12:43:28 +0300
  * Unused flag creates cleaning issue (piuparts)
* [Revision #0b2241aebc](https://github.com/MariaDB/server/commit/0b2241aebc)\
  2021-08-20 11:14:36 +0300
  * [MDEV-26443](https://jira.mariadb.org/browse/MDEV-26443) HAVE\_C99\_INITIALIZERS is not applicable to C++
* [Revision #15ac6c5867](https://github.com/MariaDB/server/commit/15ac6c5867)\
  2021-08-16 17:15:37 -0700
  * CMakeLists.txt: remove MYSQL\_SOURCE\_DIR from MYSQL\_INCLUDE\_DIRS
* [Revision #da6f4d5164](https://github.com/MariaDB/server/commit/da6f4d5164)\
  2021-08-18 16:45:09 +0300
  * [MDEV-26131](https://jira.mariadb.org/browse/MDEV-26131) fixup
* [Revision #0edf44c53a](https://github.com/MariaDB/server/commit/0edf44c53a)\
  2021-08-18 16:28:34 +0300
  * [MDEV-20931](https://jira.mariadb.org/browse/MDEV-20931) fixup: innodb.import\_corrupted test case cleanup
* [Revision #0dec71ca53](https://github.com/MariaDB/server/commit/0dec71ca53)\
  2021-08-18 16:07:15 +1000
  * [MDEV-26350](https://jira.mariadb.org/browse/MDEV-26350): select\_lex->ref\_pointer\_array.size() % 5 == 0
* [Revision #f73eea4984](https://github.com/MariaDB/server/commit/f73eea4984)\
  2021-08-18 12:10:31 +0300
  * [MDEV-26131](https://jira.mariadb.org/browse/MDEV-26131) fixup: ./mtr --embedded encryption.innodb\_import
* [Revision #890f2ad769](https://github.com/MariaDB/server/commit/890f2ad769)\
  2021-07-16 00:39:39 +0300
  * [MDEV-20931](https://jira.mariadb.org/browse/MDEV-20931) ALTER...IMPORT can crash the server
* [Revision #89445b64fe](https://github.com/MariaDB/server/commit/89445b64fe)\
  2021-07-28 19:25:25 +0530
  * [MDEV-26131](https://jira.mariadb.org/browse/MDEV-26131) SEGV in ha\_innobase::discard\_or\_import\_tablespace
* [Revision #4cd063b9e4](https://github.com/MariaDB/server/commit/4cd063b9e4)\
  2021-08-16 12:10:20 +0300
  * [MDEV-26376](https://jira.mariadb.org/browse/MDEV-26376) pars\_info\_bind\_id() unnecessarily copies strings
* [Revision #50428b3995](https://github.com/MariaDB/server/commit/50428b3995)\
  2021-08-16 02:00:10 +0200
  * [MDEV-26101](https://jira.mariadb.org/browse/MDEV-26101): Galera WSREP SST broken on 10.6 under FreeBSD
* [Revision #094e039166](https://github.com/MariaDB/server/commit/094e039166)\
  2021-08-15 21:12:58 +0200
  * [MDEV-26340](https://jira.mariadb.org/browse/MDEV-26340): rsync uses `--whole-file` only in wan mode
* [Revision #d1a948cfaa](https://github.com/MariaDB/server/commit/d1a948cfaa)\
  2021-08-15 21:03:07 +0200
  * [MDEV-26211](https://jira.mariadb.org/browse/MDEV-26211): Cluster joiner node is failed to start when using TLS
* [Revision #3b29315fde](https://github.com/MariaDB/server/commit/3b29315fde)\
  2021-08-15 09:00:06 +1000
  * mysql\_client\_test: test\_bug40365 gcc-11.2.1 indentation complaint
* [Revision #f725020ff7](https://github.com/MariaDB/server/commit/f725020ff7)\
  2021-08-09 11:52:03 +0200
  * Fix cmake warning caused by 751ebe44fda4deb715fc2235548517c287f2a559
* [Revision #160d97a4aa](https://github.com/MariaDB/server/commit/160d97a4aa)\
  2021-08-05 23:48:02 +0300
  * [MDEV-18734](https://jira.mariadb.org/browse/MDEV-18734) ASAN heap-use-after-free upon sorting by blob column from partitioned table
* [Revision #b8deb02859](https://github.com/MariaDB/server/commit/b8deb02859)\
  2021-08-05 09:11:46 -0400
  * bump the VERSION
* [Revision #175c9fe1d5](https://github.com/MariaDB/server/commit/175c9fe1d5)\
  2021-08-03 09:50:22 +0200
  * cleanup: specifying plugin dependencies in CMakeLists.txt

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
