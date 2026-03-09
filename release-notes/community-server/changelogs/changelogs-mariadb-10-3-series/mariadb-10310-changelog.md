# MariaDB 10.3.10 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.10)[Release Notes](../../old-releases/10.3/10.3.10.md)[Changelog](mariadb-10310-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 4 Oct 2018

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.10.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #bad2f1569d](https://github.com/MariaDB/server/commit/bad2f1569d)\
  2018-09-12 16:36:45 +0400
  * [MDEV-17167](https://jira.mariadb.org/browse/MDEV-17167) - InnoDB: Failing assertion: table->get\_ref\_count() == 0 upon truncating a temporary table
* [Revision #b9a5ff3644](https://github.com/MariaDB/server/commit/b9a5ff3644)\
  2018-10-02 00:33:42 +0300
  * Updated list of unstable tests for 10.3.10 release
* Merge [Revision #9556d56da2](https://github.com/MariaDB/server/commit/9556d56da2) 2018-10-01 10:28:22 +0200 - Merge branch '10.3'
* [Revision #85cdb63f77](https://github.com/MariaDB/server/commit/85cdb63f77)\
  2018-09-26 17:18:13 +0300
  * Correct a function comment
* [Revision #5aa18f4e08](https://github.com/MariaDB/server/commit/5aa18f4e08)\
  2018-10-01 09:30:33 +0300
  * row\_build\_index\_entry(): Make index const
* [Revision #c58e502455](https://github.com/MariaDB/server/commit/c58e502455)\
  2018-09-28 06:45:41 +0300
  * Remove an unused function
* [Revision #ac8c7a1c08](https://github.com/MariaDB/server/commit/ac8c7a1c08)\
  2018-09-28 06:43:10 +0300
  * Fix -Wunused-variable
* [Revision #b154d302fa](https://github.com/MariaDB/server/commit/b154d302fa)\
  2018-09-28 23:10:37 +0200
  * memory leak when updating @@rocksdb\_update\_cf\_options
* [Revision #556f058ab2](https://github.com/MariaDB/server/commit/556f058ab2)\
  2018-09-28 18:04:26 +0200
  * ASAN error when strlen(db) < 6
* [Revision #c47c0ca50c](https://github.com/MariaDB/server/commit/c47c0ca50c)\
  2018-09-27 21:43:21 +0200
  * mtr: uninitialized warning (if --manual-gdb or --boot-gdb)
* [Revision #6d2c70bc55](https://github.com/MariaDB/server/commit/6d2c70bc55)\
  2018-09-27 19:45:00 +0200
  * Update test result (after galera library upgrade?)
* Merge [Revision #57e0da50bb](https://github.com/MariaDB/server/commit/57e0da50bb) 2018-09-26 20:49:51 +0200 - Merge branch '10.2' into 10.3
* [Revision #7aba6f8f88](https://github.com/MariaDB/server/commit/7aba6f8f88)\
  2018-09-22 15:36:27 +0200
  * fix galera\_sst\_rsync\_data\_dir again
* [Revision #5f654c2e91](https://github.com/MariaDB/server/commit/5f654c2e91)\
  2018-09-18 14:35:36 +0200
  * comments and dbug keywords
* [Revision #c16a54c02e](https://github.com/MariaDB/server/commit/c16a54c02e)\
  2018-06-21 16:46:11 +1000
  * [MDEV-16429](https://jira.mariadb.org/browse/MDEV-16429): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' fails upon attempt to update virtual column on partitioned versioned table
* [Revision #8893d199ef](https://github.com/MariaDB/server/commit/8893d199ef)\
  2018-09-15 10:26:23 +0200
  * [MDEV-17009](https://jira.mariadb.org/browse/MDEV-17009) PIE issue on FreeBSD after 10.3.9 update
* [Revision #27235eed67](https://github.com/MariaDB/server/commit/27235eed67)\
  2018-09-21 15:03:37 +0200
  * Revert "[MDEV-16768](https://jira.mariadb.org/browse/MDEV-16768): fix blob key length"
* [Revision #bc7d40d032](https://github.com/MariaDB/server/commit/bc7d40d032)\
  2018-09-21 09:17:33 +0300
  * Clean up some SPATIAL INDEX code
* [Revision #90b292ce31](https://github.com/MariaDB/server/commit/90b292ce31)\
  2018-09-19 17:29:25 +0300
  * Follow-up to [MDEV-16328](https://jira.mariadb.org/browse/MDEV-16328): ALTER TABLE…page\_compression\_level should not rebuild table
* [Revision #28ae79650d](https://github.com/MariaDB/server/commit/28ae79650d)\
  2018-09-19 09:12:58 +0300
  * Terminology: 'metadata' not 'default rec'
* [Revision #755187c853](https://github.com/MariaDB/server/commit/755187c853)\
  2018-09-19 07:21:24 +0300
  * Terminology: 'metadata record' instead of 'default row'
* [Revision #043639f9b0](https://github.com/MariaDB/server/commit/043639f9b0)\
  2018-09-18 21:25:24 +0300
  * Simplify innobase\_add\_instant\_try()
* Merge [Revision #159b41b869](https://github.com/MariaDB/server/commit/159b41b869) 2018-09-18 10:49:03 -0700 - [MDEV-17144](https://jira.mariadb.org/browse/MDEV-17144): Sample of spider\_direct\_sql cause crash
* [Revision #e33961611a](https://github.com/MariaDB/server/commit/e33961611a)\
  2018-09-17 18:39:16 -0700
  * [MDEV-17144](https://jira.mariadb.org/browse/MDEV-17144): Sample of spider\_direct\_sql cause crash
* [Revision #5ec144cfab](https://github.com/MariaDB/server/commit/5ec144cfab)\
  2018-09-17 18:49:53 -0700
  * [MDEV-17211](https://jira.mariadb.org/browse/MDEV-17211) Server crash on query
* [Revision #21f310db30](https://github.com/MariaDB/server/commit/21f310db30)\
  2018-09-17 18:10:37 +0300
  * Fix the Windows build
* [Revision #774a4cb547](https://github.com/MariaDB/server/commit/774a4cb547)\
  2018-09-17 17:50:56 +0300
  * Mroonga follow-up fix for [MDEV-16328](https://jira.mariadb.org/browse/MDEV-16328)
* [Revision #ac24289e66](https://github.com/MariaDB/server/commit/ac24289e66)\
  2018-09-17 14:22:30 +0300
  * [MDEV-16328](https://jira.mariadb.org/browse/MDEV-16328) ALTER TABLE…page\_compression\_level should not rebuild table
* [Revision #c5a9a63293](https://github.com/MariaDB/server/commit/c5a9a63293)\
  2018-09-15 14:28:19 -0700
  * [MDEV-16917](https://jira.mariadb.org/browse/MDEV-16917) Index affects query results
* [Revision #aba5c72be2](https://github.com/MariaDB/server/commit/aba5c72be2)\
  2018-09-14 15:06:58 +0300
  * [MDEV-17196](https://jira.mariadb.org/browse/MDEV-17196) Crash during instant ADD COLUMN with long DEFAULT value
* [Revision #ed49f9aae2](https://github.com/MariaDB/server/commit/ed49f9aae2)\
  2018-09-13 14:55:46 -0700
  * [MDEV-16912](https://jira.mariadb.org/browse/MDEV-16912): Spider Order By column\[datatime] limit 5 returns 3 rows
* [Revision #87609324e0](https://github.com/MariaDB/server/commit/87609324e0)\
  2018-08-04 22:57:52 -0700
  * [MDEV-16768](https://jira.mariadb.org/browse/MDEV-16768): fix blob key length
* Merge [Revision #8dda6d797a](https://github.com/MariaDB/server/commit/8dda6d797a) 2018-09-11 12:05:47 +0300 - Merge pull request #850 from HeMan/10.3
* [Revision #ff5a482d9c](https://github.com/MariaDB/server/commit/ff5a482d9c)\
  2018-08-24 10:43:27 +0200
  * Return code from starting MariaDB.
* Merge [Revision #ffd583bb8b](https://github.com/MariaDB/server/commit/ffd583bb8b) 2018-09-11 12:00:39 +0300 - Merge pull request #858 from codership/10.3-[MDEV-16052](https://jira.mariadb.org/browse/MDEV-16052)
* [Revision #17a208b5bb](https://github.com/MariaDB/server/commit/17a208b5bb)\
  2018-08-31 14:15:09 +0200
  * [MDEV-16052](https://jira.mariadb.org/browse/MDEV-16052) galera mtr galera\_certification\_double\_failure fails with deadlock
* Merge [Revision #4d93fea4e0](https://github.com/MariaDB/server/commit/4d93fea4e0) 2018-09-11 11:49:49 +0300 - Merge pull request #857 from codership/10.3-[MDEV-15845](https://jira.mariadb.org/browse/MDEV-15845)
* [Revision #58a1d274e6](https://github.com/MariaDB/server/commit/58a1d274e6)\
  2018-08-29 16:45:28 +0200
  * [MDEV-15845](https://jira.mariadb.org/browse/MDEV-15845) Test failure on galera.galera\_concurrent\_ctas
* Merge [Revision #6b61f1bbad](https://github.com/MariaDB/server/commit/6b61f1bbad) 2018-09-10 16:12:50 +0300 - [MDEV-17161](https://jira.mariadb.org/browse/MDEV-17161) TRUNCATE TABLE fails after upgrade from 10.1
* [Revision #fc34e4c067](https://github.com/MariaDB/server/commit/fc34e4c067)\
  2018-09-10 16:10:26 +0300
  * [MDEV-17161](https://jira.mariadb.org/browse/MDEV-17161) TRUNCATE TABLE fails after upgrade from 10.1
* Merge [Revision #b02c722e7a](https://github.com/MariaDB/server/commit/b02c722e7a) 2018-09-10 15:40:11 +0300 - [MDEV-17158](https://jira.mariadb.org/browse/MDEV-17158) TRUNCATE is not atomic after [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564)
* [Revision #75f8e86f57](https://github.com/MariaDB/server/commit/75f8e86f57)\
  2018-09-10 14:59:58 +0300
  * [MDEV-17158](https://jira.mariadb.org/browse/MDEV-17158) TRUNCATE is not atomic after [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564)
* [Revision #8618c58cc0](https://github.com/MariaDB/server/commit/8618c58cc0)\
  2018-09-09 11:39:20 +0300
  * Disable an unstable test
* Merge [Revision #5822d31696](https://github.com/MariaDB/server/commit/5822d31696) 2018-09-09 11:38:14 +0300 - Follow-up to [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407): Remove fil\_wait\_crypt\_bg\_threads()
* [Revision #99e36a7157](https://github.com/MariaDB/server/commit/99e36a7157)\
  2018-09-09 11:34:56 +0300
  * Follow-up to [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407): Remove fil\_wait\_crypt\_bg\_threads()
* [Revision #4c0d391c92](https://github.com/MariaDB/server/commit/4c0d391c92)\
  2018-09-08 16:18:42 +0100
  * Windows : fix broken build with OpenSSL
* Merge [Revision #5a1868b58d](https://github.com/MariaDB/server/commit/5a1868b58d) 2018-09-07 22:15:06 +0300 - [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) mariadb-backup does not work with TRUNCATE
* [Revision #980d1bf1a9](https://github.com/MariaDB/server/commit/980d1bf1a9)\
  2018-09-07 17:24:31 +0300
  * [MDEV-14717](https://jira.mariadb.org/browse/MDEV-14717): Prevent crash-downgrade to earlier [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md)
* [Revision #73ed19e44f](https://github.com/MariaDB/server/commit/73ed19e44f)\
  2018-09-06 11:51:50 +0300
  * [MDEV-14585](https://jira.mariadb.org/browse/MDEV-14585) Automatically remove #sql- tables in InnoDB dictionary during recovery
* [Revision #8dcacd3b01](https://github.com/MariaDB/server/commit/8dcacd3b01)\
  2018-09-06 11:47:54 +0300
  * Follow-up to [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407) innodb.drop\_table\_background failed in buildbot with "Tablespace for table exists"
* [Revision #754727bb8a](https://github.com/MariaDB/server/commit/754727bb8a)\
  2018-09-06 11:40:27 +0300
  * [MDEV-14378](https://jira.mariadb.org/browse/MDEV-14378) In ALGORITHM=INPLACE, use a common name for the intermediate tables or partitions
* [Revision #cf2a4426a2](https://github.com/MariaDB/server/commit/cf2a4426a2)\
  2018-09-06 10:32:49 +0300
  * [MDEV-14717](https://jira.mariadb.org/browse/MDEV-14717) RENAME TABLE in InnoDB is not crash-safe
* [Revision #e67b1070bb](https://github.com/MariaDB/server/commit/e67b1070bb)\
  2018-08-28 22:41:17 +0300
  * [MDEV-17049](https://jira.mariadb.org/browse/MDEV-17049) Enable innodb\_undo tests on buildbot
* [Revision #055a3334ad](https://github.com/MariaDB/server/commit/055a3334ad)\
  2018-08-28 13:43:06 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) mariadb-backup does not work with TRUNCATE
* Merge [Revision #4901f31c13](https://github.com/MariaDB/server/commit/4901f31c13) 2018-09-07 22:09:28 +0300 - Merge 10.2 into 10.3
* [Revision #c3a80175b1](https://github.com/MariaDB/server/commit/c3a80175b1)\
  2018-09-07 07:26:11 +0300
  * After-merge fix: s/tokudb\_logdump/tokudb\_logprint/
* Merge [Revision #8bd942d77b](https://github.com/MariaDB/server/commit/8bd942d77b) 2018-09-07 01:13:23 +0200 - Merge tag 'mariadb-10.3.9' into 10.3
* [Revision #3e6e843423](https://github.com/MariaDB/server/commit/3e6e843423)\
  2018-09-06 22:40:37 +0300
  * Disable some failing tests
* Merge [Revision #2f4c391958](https://github.com/MariaDB/server/commit/2f4c391958) 2018-09-06 22:35:45 +0300 - Merge 10.2 into 10.3
* Merge [Revision #3bfafd133f](https://github.com/MariaDB/server/commit/3bfafd133f) 2018-09-06 22:33:23 +0300 - [MDEV-16330](https://jira.mariadb.org/browse/MDEV-16330) code cleanup (pull request #848)
* [Revision #28461fe5ef](https://github.com/MariaDB/server/commit/28461fe5ef)\
  2018-08-22 22:06:38 +0300
  * [MDEV-16330](https://jira.mariadb.org/browse/MDEV-16330) Allow instant change of WITH SYSTEM VERSIONING column attribute
* [Revision #90c4f5669d](https://github.com/MariaDB/server/commit/90c4f5669d)\
  2018-09-05 19:45:52 +0300
  * Fixed wrong #ifdef related to DBUG\_ASSERT\_AS\_PRINTF
* [Revision #49d506cd1d](https://github.com/MariaDB/server/commit/49d506cd1d)\
  2018-09-04 09:48:37 +0300
  * Adjust --embedded result for [MDEV-14474](https://jira.mariadb.org/browse/MDEV-14474)
* [Revision #39c6775a35](https://github.com/MariaDB/server/commit/39c6775a35)\
  2018-09-02 22:37:53 +0300
  * Fixed func\_time.test that was depending on current time
* [Revision #62c4a1702a](https://github.com/MariaDB/server/commit/62c4a1702a)\
  2018-08-31 14:19:01 +0300
  * Disable galera tests that fails regularly
* [Revision #c03c6adf58](https://github.com/MariaDB/server/commit/c03c6adf58)\
  2018-08-31 14:19:01 +0300
  * Disable galera tests that fails regularly
* [Revision #6156089bc7](https://github.com/MariaDB/server/commit/6156089bc7)\
  2018-08-31 10:47:18 +0300
  * Fixed several issues with aria\_chk
* [Revision #ef88c7d306](https://github.com/MariaDB/server/commit/ef88c7d306)\
  2018-08-31 10:29:09 +0300
  * Fixed wrong result file that happend because of a previous merge
* [Revision #d8b8079e42](https://github.com/MariaDB/server/commit/d8b8079e42)\
  2018-08-30 11:30:28 -0700
  * EV-16992 Assertion \`table\_ref->table || table\_ref->view' failed in Field\_iterator\_table\_ref::set\_field\_iterator
* [Revision #7aa80ba66b](https://github.com/MariaDB/server/commit/7aa80ba66b)\
  2018-08-30 17:32:26 +0300
  * Sequences with negative numbers and auto\_increment\_increment crashes
* Merge [Revision #ceb5597184](https://github.com/MariaDB/server/commit/ceb5597184) 2018-08-29 19:34:00 -0700 - [MDEV-16889](https://jira.mariadb.org/browse/MDEV-16889): Spider Crash mysqld got exception 0xc0000005
* [Revision #4885baf682](https://github.com/MariaDB/server/commit/4885baf682)\
  2018-08-29 17:36:16 -0700
  * [MDEV-16889](https://jira.mariadb.org/browse/MDEV-16889): Spider Crash mysqld got exception 0xc0000005
* Merge [Revision #7830fb7f45](https://github.com/MariaDB/server/commit/7830fb7f45) 2018-08-28 12:22:56 +0300 - Merge 10.2 into 10.3
* [Revision #b805ebd7ed](https://github.com/MariaDB/server/commit/b805ebd7ed)\
  2018-08-28 12:20:20 +0300
  * Adjust a result for [MDEV-14474](https://jira.mariadb.org/browse/MDEV-14474)
* [Revision #497d86276f](https://github.com/MariaDB/server/commit/497d86276f)\
  2018-08-27 08:12:59 -0700
  * [MDEV-17017](https://jira.mariadb.org/browse/MDEV-17017) Explain for query using derived table specified with a table value constructor shows wrong number of rows
* [Revision #a290b807e8](https://github.com/MariaDB/server/commit/a290b807e8)\
  2018-08-27 12:03:02 +0300
  * [MDEV-17062](https://jira.mariadb.org/browse/MDEV-17062): Test failure on galera.MW-336 [MDEV-17058](https://jira.mariadb.org/browse/MDEV-17058): Test failure on wsrep.variables [MDEV-17060](https://jira.mariadb.org/browse/MDEV-17060): Test failure on galera.galera\_var\_slave\_threads
* [Revision #b6f055025b](https://github.com/MariaDB/server/commit/b6f055025b)\
  2018-08-25 19:56:00 +0300
  * Make funcs\_1.is\_check\_constraints deterministic
* [Revision #d526679efd](https://github.com/MariaDB/server/commit/d526679efd)\
  2018-04-03 12:41:13 +0000
  * [MDEV-14474](https://jira.mariadb.org/browse/MDEV-14474) information\_schema.check\_constraints
* Merge [Revision #7f73f5e4e5](https://github.com/MariaDB/server/commit/7f73f5e4e5) 2018-08-24 15:54:32 +0300 - Merge pull request #839 from minggr/fix-auto-inc
* [Revision #f7154242b8](https://github.com/MariaDB/server/commit/f7154242b8)\
  2018-08-16 10:28:29 -0700
  * [MDEV-16703](https://jira.mariadb.org/browse/MDEV-16703): Update AUTO\_INCREMENT in the UPDATE statement
* [Revision #9c5a038001](https://github.com/MariaDB/server/commit/9c5a038001)\
  2018-08-23 12:45:14 +0200
  * [MDEV-17040](https://jira.mariadb.org/browse/MDEV-17040) sql/sql\_yacc\_orac.cc is included but sql/sql\_yacc\_ora.cc isn't included in source archive
* [Revision #db3be33ec8](https://github.com/MariaDB/server/commit/db3be33ec8)\
  2018-07-24 01:59:15 +1000
  * [MDEV-16783](https://jira.mariadb.org/browse/MDEV-16783) Assertion \`!conds' failed in mysql\_delete upon 2nd execution of SP with DELETE HISTORY
* [Revision #6c6ca907ee](https://github.com/MariaDB/server/commit/6c6ca907ee)\
  2018-08-24 00:51:47 -0700
  * Correction for [MDEV-16930](https://jira.mariadb.org/browse/MDEV-16930).
* [Revision #2c76653849](https://github.com/MariaDB/server/commit/2c76653849)\
  2018-08-23 17:43:54 -0700
  * Added test cases for [MDEV-17017](https://jira.mariadb.org/browse/MDEV-17017) and [MDEV-16930](https://jira.mariadb.org/browse/MDEV-16930) into compat/oracle
* [Revision #b4cf8557e3](https://github.com/MariaDB/server/commit/b4cf8557e3)\
  2018-08-23 14:39:38 -0700
  * Corrected test results after the last change in range.test
* [Revision #6b9dd66f07](https://github.com/MariaDB/server/commit/6b9dd66f07)\
  2018-08-23 19:30:26 +0300
  * Move the testcase for BUG#21282 to a file that includes have\_debug.inc
* [Revision #c43d11b96e](https://github.com/MariaDB/server/commit/c43d11b96e)\
  2018-08-21 12:01:25 -0700
  * [MDEV-16930](https://jira.mariadb.org/browse/MDEV-16930) Crash when VALUES in derived table contains expressions
* [Revision #a1fd25c22b](https://github.com/MariaDB/server/commit/a1fd25c22b)\
  2018-08-18 22:57:20 -0700
  * [MDEV-17017](https://jira.mariadb.org/browse/MDEV-17017) Explain for query using derived table specified with a table value constructor shows wrong number of rows
* [Revision #0dadb96e16](https://github.com/MariaDB/server/commit/0dadb96e16)\
  2018-07-06 15:34:29 +1000
  * travis: llvm repo gpg key missing - use travis defination
* [Revision #34c7222c08](https://github.com/MariaDB/server/commit/34c7222c08)\
  2018-08-16 17:38:20 +0300
  * Fixed that -DDBUG\_ASSERT\_AS\_PRINTF works again
* [Revision #8716bb3b72](https://github.com/MariaDB/server/commit/8716bb3b72)\
  2018-08-16 09:41:20 +0300
  * After-merge fix: Restore DECLARE\_THREAD to fix Windows build
* Merge [Revision #1eb2d8f6e8](https://github.com/MariaDB/server/commit/1eb2d8f6e8) 2018-08-16 08:54:58 +0300 - Merge 10.2 into 10.3
* [Revision #197aa0d879](https://github.com/MariaDB/server/commit/197aa0d879)\
  2018-08-15 10:32:52 -0400
  * bump the VERSION
* [Revision #021652ba50](https://github.com/MariaDB/server/commit/021652ba50)\
  2018-08-14 19:34:33 +0300
  * [MDEV-15872](https://jira.mariadb.org/browse/MDEV-15872) Crash in online ALTER TABLE...ADD PRIMARY KEY after instant ADD COLUMN...NULL
* Merge [Revision #e10ca66bab](https://github.com/MariaDB/server/commit/e10ca66bab) 2018-08-13 13:23:59 -0700 - [MDEV-16398](https://jira.mariadb.org/browse/MDEV-16398): Spider Creates Query With Non-Existent Function
* [Revision #4b6dccc84a](https://github.com/MariaDB/server/commit/4b6dccc84a)\
  2018-08-09 00:04:09 -0700
  * [MDEV-16398](https://jira.mariadb.org/browse/MDEV-16398): Spider Creates Query With Non-Existent Function

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
