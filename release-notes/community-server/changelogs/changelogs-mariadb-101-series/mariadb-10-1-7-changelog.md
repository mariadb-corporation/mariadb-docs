# MariaDB 10.1.7 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.7)[Release Notes](../../old-releases/10.1/10.1.7.md)[Changelog](mariadb-10-1-7-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 9 Sep 2015

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.7.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #4cb6edb](https://github.com/MariaDB/server/commit/4cb6edb)\
  2015-09-08 17:46:03 -0400
  * Update failing galera tests
* [Revision #28ad6a7](https://github.com/MariaDB/server/commit/28ad6a7)\
  2015-09-08 17:43:48 -0400
  * [MDEV-8763](https://jira.mariadb.org/browse/MDEV-8763): Galera tests failures with --ps-protocol
* [Revision #067ed23](https://github.com/MariaDB/server/commit/067ed23)\
  2015-09-08 21:01:58 +0300
  * [MDEV-8774](https://jira.mariadb.org/browse/MDEV-8774): Test innodb.innodb\_bug53290 failures on buildbot
* [Revision #bbb238c](https://github.com/MariaDB/server/commit/bbb238c)\
  2015-09-08 15:43:48 +0200
  * disable main.max\_statement\_time test
* [Revision #edb37ae](https://github.com/MariaDB/server/commit/edb37ae)\
  2015-09-08 15:38:11 +0200
  * disable encrypt\_tmp\_files and encrypt\_binlog by default
* [Revision #2c1553e](https://github.com/MariaDB/server/commit/2c1553e)\
  2015-09-08 16:08:08 +0300
  * [MDEV-8774](https://jira.mariadb.org/browse/MDEV-8774): Test innodb.innodb\_bug53290 failures on buildbot
* [Revision #de269f2](https://github.com/MariaDB/server/commit/de269f2)\
  2015-09-08 16:02:29 +0400
  * [MDEV-8766](https://jira.mariadb.org/browse/MDEV-8766) Wrong result for SELECT..WHERE LENGTH(time\_column)=8 AND time\_column=TIMESTAMP'2001-01-01 10:20:31'
* [Revision #b119110a](https://github.com/MariaDB/server/commit/b119110a)\
  2015-09-05 16:24:11 +0200
  * [MDEV-8581](https://jira.mariadb.org/browse/MDEV-8581) Unique prefix for default-tmp-storage-engine does not work
* [Revision #509b836](https://github.com/MariaDB/server/commit/509b836)\
  2015-09-04 15:54:20 +0300
  * [MDEV-8708](https://jira.mariadb.org/browse/MDEV-8708): InnoDB temp file encryption
* [Revision #4257442](https://github.com/MariaDB/server/commit/4257442)\
  2015-09-07 17:43:53 +0400
  * [MDEV-8699](https://jira.mariadb.org/browse/MDEV-8699) Wrong result for SELECT..WHERE HEX(date\_column)!='323030312D30312D3031' AND date\_column='2001-01-01x'
* [Revision #2029163](https://github.com/MariaDB/server/commit/2029163)\
  2015-09-07 11:07:40 +0400
  * [MDEV-8742](https://jira.mariadb.org/browse/MDEV-8742) Wrong result for SELECT..WHERE view\_latin1\_swedish\_ci\_field='a' COLLATE latin1\_bin The fix for [MDEV-8749](https://jira.mariadb.org/browse/MDEV-8749) also fixed [MDEV-8742](https://jira.mariadb.org/browse/MDEV-8742). Just adding the test case from the bug report.
* [Revision #bf7a2bb](https://github.com/MariaDB/server/commit/bf7a2bb)\
  2015-09-07 10:50:27 +0400
  * [MDEV-8704](https://jira.mariadb.org/browse/MDEV-8704) Wrong result for SELECT..WHERE LENGTH(double\_column)!=6 AND double\_column=100e0
* [Revision #5448e0a](https://github.com/MariaDB/server/commit/5448e0a)\
  2015-09-07 08:34:04 +0300
  * [MDEV-8745](https://jira.mariadb.org/browse/MDEV-8745): Bad InnoDB logging: "\[Note] InnoDB: not started"
* [Revision #e7dcec5](https://github.com/MariaDB/server/commit/e7dcec5)\
  2015-09-07 08:55:55 +0400
  * [MDEV-8703](https://jira.mariadb.org/browse/MDEV-8703) Wrong result for SELECT..WHERE LENGTH(decimal\_10\_1\_column)!=3 AND decimal\_10\_1\_column=1.10
* [Revision #0736cdd](https://github.com/MariaDB/server/commit/0736cdd)\
  2015-09-07 06:45:51 +0400
  * Field\_num::get\_equal\_const\_item() appeared to be in a wrong file (item.cc). Moving to field.cc.
* [Revision #4be6eee](https://github.com/MariaDB/server/commit/4be6eee)\
  2015-09-07 02:22:35 +0300
  * [MDEV-8760](https://jira.mariadb.org/browse/MDEV-8760) main.mysqlbinlog\_row\_big fails due to new default for max\_allowed\_packet
* [Revision #e616288](https://github.com/MariaDB/server/commit/e616288)\
  2015-09-07 02:18:49 +0300
  * [MDEV-8761](https://jira.mariadb.org/browse/MDEV-8761) encryption.innodb-bad-key-change2 fails with static file\_key\_management plugin
* [Revision #675ca12](https://github.com/MariaDB/server/commit/675ca12)\
  2015-09-06 21:01:59 +0300
  * Follow-up for [MDEV-6066](https://jira.mariadb.org/browse/MDEV-6066) (new defaults from 5.6 and 5.7)
* [Revision #1a36caf](https://github.com/MariaDB/server/commit/1a36caf)\
  2015-09-06 18:49:17 +0400
  * [MDEV-8729](https://jira.mariadb.org/browse/MDEV-8729) Wrong result for SELECT..WHERE HEX(enum\_column)='61' AND enum\_column='a '
* [Revision #e0df116](https://github.com/MariaDB/server/commit/e0df116)\
  2015-09-06 13:25:47 +0400
  * A clean-up after the patch for [MDEV-8747](https://jira.mariadb.org/browse/MDEV-8747) and [MDEV-8749](https://jira.mariadb.org/browse/MDEV-8749): removing IMPOSSIBLE\_RESULT from Item\_result, as it's not needed any more. The fact that an Item is not in a comparison context is now always designated by IDENTITY\_SUBST in Subst\_constraint. Previously IMPOSSIBLE\_RESULT and IDENTITY\_SUBST co-existed but actually meant the same thing.
* [Revision #c108019](https://github.com/MariaDB/server/commit/c108019)\
  2015-09-06 01:30:46 +0400
  * [MDEV-8747](https://jira.mariadb.org/browse/MDEV-8747) Wrong result for SELECT..WHERE derived\_table\_column='a' AND derived\_table\_column<>\_latin1'A' COLLATE latin1\_bin [MDEV-8749](https://jira.mariadb.org/browse/MDEV-8749) Wrong result for SELECT..WHERE derived\_table\_enum\_column='number' AND derived\_table\_enum\_column OP number
* [Revision #3d9abaf](https://github.com/MariaDB/server/commit/3d9abaf)\
  2015-09-05 23:54:18 +0400
  * [MDEV-8752](https://jira.mariadb.org/browse/MDEV-8752) Wrong result for SELECT..WHERE CASE enum\_field WHEN 1 THEN 1 ELSE 0 END AND a='5'
* [Revision #67dbfab](https://github.com/MariaDB/server/commit/67dbfab)\
  2015-09-05 14:30:42 +0300
  * Fix test not to be run on embedded, because of restart.
* [Revision #a0df822](https://github.com/MariaDB/server/commit/a0df822)\
  2015-09-05 07:18:57 +0300
  * [MDEV-8753](https://jira.mariadb.org/browse/MDEV-8753): 10.1 build is broken: xtradb/handler/ha\_innodb.cc:21430: error: redefinition of 'void ib\_push\_warning(trx\_t\*, ulint, const char\*, ...)'
* [Revision #e04723d](https://github.com/MariaDB/server/commit/e04723d)\
  2015-09-04 20:09:20 +0300
  * [MDEV-8750](https://jira.mariadb.org/browse/MDEV-8750): Server crashes in page\_cur\_is\_after\_last on altering table using a wrong encryption key
* [Revision #7e916bb](https://github.com/MariaDB/server/commit/7e916bb)\
  2015-08-31 19:47:14 +0300
  * [MDEV-8588](https://jira.mariadb.org/browse/MDEV-8588): Assertion failure in file ha\_innodb.cc line 21140 if at least one encrypted table exists and encryption service is not available
* [Revision #e197823](https://github.com/MariaDB/server/commit/e197823)\
  2015-08-16 09:53:27 +0300
  * [MDEV-8588](https://jira.mariadb.org/browse/MDEV-8588): Assertion failure in file ha\_innodb.cc line 21140 if at least one encrypted table exists and encryption service is not available
* [Revision #e9b6f95](https://github.com/MariaDB/server/commit/e9b6f95)\
  2015-09-04 16:30:11 +0200
  * test failure
* [Revision #6246b4c](https://github.com/MariaDB/server/commit/6246b4c)\
  2015-09-04 12:33:14 +0200
  * update encryption plugin and service versions
* [Revision #096510d](https://github.com/MariaDB/server/commit/096510d)\
  2015-09-04 12:28:47 +0200
  * fix dbug tags
* [Revision #7cd3c42](https://github.com/MariaDB/server/commit/7cd3c42)\
  2015-09-04 11:39:24 +0200
  * document new encryption plugin api
* [Revision #bc12d5f](https://github.com/MariaDB/server/commit/bc12d5f)\
  2015-09-03 18:06:55 +0200
  * [MDEV-6066](https://jira.mariadb.org/browse/MDEV-6066): Merge new defaults from 5.6 and 5.7
* [Revision #e3982ce](https://github.com/MariaDB/server/commit/e3982ce)\
  2015-08-11 18:45:38 +0200
  * [MDEV-6066](https://jira.mariadb.org/browse/MDEV-6066): Merge new defaults from 5.6 and 5.7 (defaults changed, QC can be stopped with no-zero size)
* [Revision #21daa7b](https://github.com/MariaDB/server/commit/21daa7b)\
  2015-08-10 21:45:11 +0200
  * [MDEV-6066](https://jira.mariadb.org/browse/MDEV-6066): Merge new defaults from 5.6 and 5.7 (autoset)
* [Revision #b85a001](https://github.com/MariaDB/server/commit/b85a001)\
  2015-09-02 09:58:08 +0200
  * [MDEV-8264](https://jira.mariadb.org/browse/MDEV-8264) encryption for binlog
* [Revision #41d68ca](https://github.com/MariaDB/server/commit/41d68ca)\
  2015-08-31 16:35:37 +0200
  * cleanup: Log\_event::write() and MYSQL\_BIN\_LOG::write\_cache()
* [Revision #704ba5c](https://github.com/MariaDB/server/commit/704ba5c)\
  2015-08-27 13:48:32 +0200
  * cleanup: correct usage of semicolons in sql\_yacc.yy
* [Revision #c862c15](https://github.com/MariaDB/server/commit/c862c15)\
  2015-08-25 17:29:58 +0200
  * cleanup: \[partial] removal of llstr()
* [Revision #fff6f42](https://github.com/MariaDB/server/commit/fff6f42)\
  2015-08-28 02:34:03 +0200
  * Revert f1abd015, make a smaller fix
* [Revision #1720fcd](https://github.com/MariaDB/server/commit/1720fcd)\
  2015-08-24 13:09:03 +0200
  * cleanup DBUG, DBUG\_DUMP\_EVENT\_BUF
* [Revision #781e18e](https://github.com/MariaDB/server/commit/781e18e)\
  2015-08-30 11:18:48 +0200
  * test cleanup: use --replace\_result correctly
* [Revision #55d7871](https://github.com/MariaDB/server/commit/55d7871)\
  2015-08-21 23:20:35 +0200
  * test cleanup: remove Format\_description\_log\_event size dependency
* [Revision #8aa473c](https://github.com/MariaDB/server/commit/8aa473c)\
  2015-08-21 23:16:54 +0200
  * fix show\_relaylog\_events.inc to work for multisource
* [Revision #274a47a](https://github.com/MariaDB/server/commit/274a47a)\
  2015-08-31 17:38:31 +0200
  * cleanup: remove Slave\_log\_event (unused since 2002)
* [Revision #2d2286f](https://github.com/MariaDB/server/commit/2d2286f)\
  2015-08-30 15:03:55 +0200
  * cleanup: use enum\_binlog\_checksum\_alg, not uint8
* [Revision #86b06a0](https://github.com/MariaDB/server/commit/86b06a0)\
  2015-09-04 00:44:34 +0200
  * cleanup: simplify nested multiline ?(?:(?:)):
* [Revision #7b54dec](https://github.com/MariaDB/server/commit/7b54dec)\
  2015-08-31 16:23:01 +0200
  * cleanup: comments
* [Revision #89e08bf](https://github.com/MariaDB/server/commit/89e08bf)\
  2015-08-30 14:59:12 +0200
  * cleanup: reformat
* [Revision #5018a66](https://github.com/MariaDB/server/commit/5018a66)\
  2015-08-17 18:38:30 +0200
  * cleanup: Log\_event::read\_log\_event()
* [Revision #08687f7](https://github.com/MariaDB/server/commit/08687f7)\
  2015-09-02 17:03:19 +0200
  * cleanup: my\_checksum
* [Revision #66b9a94](https://github.com/MariaDB/server/commit/66b9a94)\
  2015-09-04 10:32:52 +0200
  * New encryption API. Piece-wise encryption.
* [Revision #d94a982](https://github.com/MariaDB/server/commit/d94a982)\
  2015-09-01 14:36:41 +0200
  * my\_crypt unittest
* [Revision #e238d6c](https://github.com/MariaDB/server/commit/e238d6c)\
  2015-08-16 22:22:52 +0200
  * String::release and String::reset methods
* [Revision #4569a89](https://github.com/MariaDB/server/commit/4569a89)\
  2015-08-11 13:03:25 +0200
  * simplify and unify my\_safe\_alloca usage
* [Revision #b6776b3](https://github.com/MariaDB/server/commit/b6776b3)\
  2015-09-01 18:54:23 +0200
  * package new SELinux/AppArmor policies instead of old ones
* [Revision #a0114b8](https://github.com/MariaDB/server/commit/a0114b8)\
  2015-09-01 22:00:26 +0200
  * cmake: don't repeat yourself
* [Revision #e74f91d](https://github.com/MariaDB/server/commit/e74f91d)\
  2015-09-01 21:58:10 +0200
  * cmake: always use the same function to test for compiler flags
* [Revision #efbd4bb](https://github.com/MariaDB/server/commit/efbd4bb)\
  2015-08-13 09:22:01 +0200
  * cmake: fix warnings when PLUGIN\_MROONGA=NO
* [Revision #d33c883](https://github.com/MariaDB/server/commit/d33c883)\
  2015-09-04 08:47:29 +0200
  * more 32-bit fixes
* [Revision #1a599c7](https://github.com/MariaDB/server/commit/1a599c7)\
  2015-09-03 21:51:45 +0200
  * test fixes for 32bit
* [Revision #8f6aac8](https://github.com/MariaDB/server/commit/8f6aac8)\
  2015-09-03 17:11:18 +0200
  * fix innodb.innodb\_uninstall test to cleanup after itself
* [Revision #ce8d4d3](https://github.com/MariaDB/server/commit/ce8d4d3)\
  2015-09-03 16:32:17 +0200
  * cleanup: comment
* [Revision #a5b0a32](https://github.com/MariaDB/server/commit/a5b0a32)\
  2015-09-03 16:32:00 +0200
  * Merge branch '10.0-galera' into 10.1
* [Revision #09307c4](https://github.com/MariaDB/server/commit/09307c4)\
  2015-09-03 12:58:53 +0200
  * clang warning
* [Revision #530a6e7](https://github.com/MariaDB/server/commit/530a6e7)\
  2015-09-03 12:58:41 +0200
  * Merge branch '10.0' into 10.1
* [Revision #5088cbf](https://github.com/MariaDB/server/commit/5088cbf)\
  2015-09-02 15:56:24 +0400
  * [MDEV-8671](https://jira.mariadb.org/browse/MDEV-8671) Wrong result for SELECT..WHERE varchar\_column=' 1' AND (varchar\_column XOR '1')
* [Revision #0671430](https://github.com/MariaDB/server/commit/0671430)\
  2015-09-02 11:11:24 +0200
  * After-merge fix.
* [Revision #ef82cb7](https://github.com/MariaDB/server/commit/ef82cb7)\
  2015-09-02 10:53:37 +0200
  * Merge [MDEV-8725](https://jira.mariadb.org/browse/MDEV-8725) into 10.1
* [Revision #09bfaf3](https://github.com/MariaDB/server/commit/09bfaf3)\
  2015-09-02 10:08:09 +0200
  * Fix a potential lost wakeup for binlog\_commit\_wait\_usec
* [Revision #999c43a](https://github.com/MariaDB/server/commit/999c43a)\
  2015-09-02 09:57:18 +0200
  * [MDEV-8725](https://jira.mariadb.org/browse/MDEV-8725): Assertion \`!(thd->rgi\_slave && thd-> rgi\_slave->did\_mark\_start\_commit)' failed in ha\_rollback\_trans
* [Revision #4f37a86](https://github.com/MariaDB/server/commit/4f37a86)\
  2015-09-02 11:51:07 +0400
  * The fix for [MDEV-8723](https://jira.mariadb.org/browse/MDEV-8723) unintentionally broke vcol\_supported\_sql\_funcs\_myisam and vcol\_supported\_sql\_funcs\_innodb. Moving the test for using CHARSET(), COLLATION(), COERCIBILITY() in virtual column from vcol\_supported\_sql\_funcs\_xxx to vcol\_blocked\_sql\_funcs\_xxx, as these functions are not supported in virtual columns any longer. Discussed with Sanja on IRC.
* [Revision #aa1002a](https://github.com/MariaDB/server/commit/aa1002a)\
  2015-09-02 08:20:49 +0400
  * [MDEV-8723](https://jira.mariadb.org/browse/MDEV-8723) Wrong result for SELECT..WHERE COLLATION(a)='binary' AND a='a'
* [Revision #6881012](https://github.com/MariaDB/server/commit/6881012)\
  2015-09-01 22:48:17 +0400
  * [MDEV-8695](https://jira.mariadb.org/browse/MDEV-8695) Wrong result for SELECT..WHERE varchar\_column='a' AND CRC32(varchar\_column)=3904355907
* [Revision #4f0255c](https://github.com/MariaDB/server/commit/4f0255c)\
  2015-09-01 18:40:54 +0300
  * Fixed errors and bugs found by valgrind:
* [Revision #56aa199](https://github.com/MariaDB/server/commit/56aa199)\
  2015-08-31 12:57:46 +0300
  * [MDEV-6152](https://jira.mariadb.org/browse/MDEV-6152): Remove calls to current\_thd while creating Item
* [Revision #8ea9b8c](https://github.com/MariaDB/server/commit/8ea9b8c)\
  2015-09-01 19:24:58 +0400
  * [MDEV-8722](https://jira.mariadb.org/browse/MDEV-8722) The patch for [MDEV-8688](https://jira.mariadb.org/browse/MDEV-8688) disabled equal field propagation for temporal column and BETWEEN and IN Item::cmp\_context was inconsistently used in combination with cmp\_type() and result\_type() in different places of the code. Fixed to use cmp\_type() in all places where cmp\_context is involved, to avoid unexpected results for temporal data types (which have result\_type()==STRING\_RESULT and cmp\_type==TIME\_RESULT).
* [Revision #4b41e3c](https://github.com/MariaDB/server/commit/4b41e3c)\
  2015-08-31 18:40:24 +0200
  * [MDEV-6219](https://jira.mariadb.org/browse/MDEV-6219): Server crashes in Bitmap<64u>::merge (this=0x180, map2=...) on 2nd execution of PS with INSERT .. SELECT, derived\_merge
* [Revision #a3c24ee](https://github.com/MariaDB/server/commit/a3c24ee)\
  2015-08-31 18:18:10 +0400
  * [MDEV-8707](https://jira.mariadb.org/browse/MDEV-8707) Wrong result for SELECT..WHERE varchar\_column=DATE'2001-01-01' AND varchar\_column='2001-01-01'
* [Revision #44a9977](https://github.com/MariaDB/server/commit/44a9977)\
  2015-08-29 23:08:15 +0400
  * [MDEV-8698](https://jira.mariadb.org/browse/MDEV-8698) Wrong result for SELECT..WHERE a BETWEEN 'a' AND 'c' COLLATE latin1\_bin;
* [Revision #787adc6](https://github.com/MariaDB/server/commit/787adc6)\
  2015-08-29 21:41:37 +0400
  * [MDEV-8680](https://jira.mariadb.org/browse/MDEV-8680) Wrong result for SELECT..WHERE a IN ('a' COLLATE latin1\_bin,'b') AND a='a' The fix for [MDEV-8688](https://jira.mariadb.org/browse/MDEV-8688) fixed [MDEV-8680](https://jira.mariadb.org/browse/MDEV-8680) as well. Just adding a test case.
* [Revision #f071a12](https://github.com/MariaDB/server/commit/f071a12)\
  2015-08-29 19:26:30 +0400
  * [MDEV-8688](https://jira.mariadb.org/browse/MDEV-8688) Wrong result for SELECT..WHERE varchar\_column IN (1,2,3) AND varchar\_column=' 1';
* [Revision #09fb512](https://github.com/MariaDB/server/commit/09fb512)\
  2015-08-29 18:45:04 +0400
  * Clean-up: removing duplicate code: removing Item\_func\_in::compare\_collation() and Item\_func\_between::compare\_collation(), and adding Item\_func\_opt\_neg::compare\_collation() instead.
* [Revision #b4e56a5](https://github.com/MariaDB/server/commit/b4e56a5)\
  2015-08-29 16:31:11 +0400
  * Moving common members of Item\_func\_in and Item\_func\_between to their parent Item\_func\_opt\_neg. A pre-requisite patch for a number of upcoming equal field propagation related bug fixes.
* [Revision #3ba2a95](https://github.com/MariaDB/server/commit/3ba2a95)\
  2015-08-28 17:03:09 +0400
  * [MDEV-8694](https://jira.mariadb.org/browse/MDEV-8694) Wrong result for SELECT..WHERE a NOT LIKE 'a ' AND a='a' Note, the patch for [MDEV-8661](https://jira.mariadb.org/browse/MDEV-8661) unintentionally fixed [MDEV-8694](https://jira.mariadb.org/browse/MDEV-8694) as well, as a side effect. Adding a real clear fix: implementing Item\_func\_like::propagate\_equal\_fields() with comments.
* [Revision #3bca8db](https://github.com/MariaDB/server/commit/3bca8db)\
  2015-08-27 10:07:32 +0300
  * [MDEV-6152](https://jira.mariadb.org/browse/MDEV-6152): Remove calls to current\_thd while creating Item
* [Revision #3cb578c](https://github.com/MariaDB/server/commit/3cb578c)\
  2015-08-24 14:42:07 +0300
  * [MDEV-6152](https://jira.mariadb.org/browse/MDEV-6152): Remove calls to current\_thd while creating Item
* [Revision #ba340d8](https://github.com/MariaDB/server/commit/ba340d8)\
  2015-08-26 23:17:34 +0400
  * Making Item\_field::can\_be\_substituted\_to\_equal\_item() private.
* [Revision #1b6b44b](https://github.com/MariaDB/server/commit/1b6b44b)\
  2015-08-26 22:32:01 +0400
  * [MDEV-8661](https://jira.mariadb.org/browse/MDEV-8661) Wrong result for SELECT..WHERE a='a' AND a='a' COLLATE latin1\_bin [MDEV-8679](https://jira.mariadb.org/browse/MDEV-8679) Equal field propagation is not used for VARCHAR when it safely could
* [Revision #c0b7bf2](https://github.com/MariaDB/server/commit/c0b7bf2)\
  2015-08-26 18:07:34 +0300
  * [MDEV-8683](https://jira.mariadb.org/browse/MDEV-8683): Bunch of tests fail in buildbot on new InnoDB variables
* [Revision #3ed384b](https://github.com/MariaDB/server/commit/3ed384b)\
  2015-08-26 14:59:33 +0300
  * Merge pull request #94 from ericherman/evict\_table\_metric
* [Revision #f66ef6a](https://github.com/MariaDB/server/commit/f66ef6a)\
  2015-08-26 11:50:47 +0200
  * Add lru evict count for the idle loop (xtradb)
* [Revision #b7abdcf](https://github.com/MariaDB/server/commit/b7abdcf)\
  2015-08-26 11:48:19 +0200
  * Add lru evict count for the idle loop (innobase)
* [Revision #df32920](https://github.com/MariaDB/server/commit/df32920)\
  2015-08-26 10:26:19 +0200
  * Add eviction count for table cache lru cleanup (xtradb)
* [Revision #4f4373f](https://github.com/MariaDB/server/commit/4f4373f)\
  2015-08-26 10:02:06 +0200
  * Add eviction count for table cache lru cleanup (innobase)
* [Revision #cf154cc](https://github.com/MariaDB/server/commit/cf154cc)\
  2015-08-26 02:09:57 +0300
  * [MDEV-8676](https://jira.mariadb.org/browse/MDEV-8676) Some storage\_engine tests fail on 10.1
* [Revision #f533b2b](https://github.com/MariaDB/server/commit/f533b2b)\
  2015-08-25 11:15:45 -0400
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #871259f](https://github.com/MariaDB/server/commit/871259f)\
  2015-08-25 16:15:22 +0300
  * [MDEV-8665](https://jira.mariadb.org/browse/MDEV-8665): innodb.innodb\_bug14147491 fails in buildbot on some debug builds
* [Revision #2744487](https://github.com/MariaDB/server/commit/2744487)\
  2015-08-25 11:46:31 +0400
  * UNINIT\_VAR() fixes
* [Revision #b66455f6](https://github.com/MariaDB/server/commit/b66455f6)\
  2015-08-24 01:41:12 +0300
  * Increase the version number
* [Revision #aef8bfd](https://github.com/MariaDB/server/commit/aef8bfd)\
  2015-08-24 01:37:21 +0300
  * [MDEV-8670](https://jira.mariadb.org/browse/MDEV-8670) main.[MDEV-504](https://jira.mariadb.org/browse/MDEV-504) fails on Windows (in buildbot and outside)
* [Revision #c18110b](https://github.com/MariaDB/server/commit/c18110b)\
  2015-08-23 00:57:57 +0300
  * Increase the version number
* [Revision #472d663](https://github.com/MariaDB/server/commit/472d663)\
  2015-08-22 01:18:02 -0400
  * [MDEV-8149](https://jira.mariadb.org/browse/MDEV-8149): Random mtr test failures during warning check
* [Revision #98ba2bf](https://github.com/MariaDB/server/commit/98ba2bf)\
  2015-08-21 17:08:55 +0400
  * Clean-up: moving compare\_collation() from Item to Item\_bool\_func.
* [Revision #1bae0d9](https://github.com/MariaDB/server/commit/1bae0d9)\
  2015-08-20 15:24:13 +0300
  * Stage 2 of [MDEV-6152](https://jira.mariadb.org/browse/MDEV-6152):
* [Revision #31e365e](https://github.com/MariaDB/server/commit/31e365e)\
  2015-08-11 11:18:38 +0400
  * [MDEV-8010](https://jira.mariadb.org/browse/MDEV-8010) - Avoid sql\_alloc() in Items (Patch #1)
* [Revision #4ee2886](https://github.com/MariaDB/server/commit/4ee2886)\
  2015-08-20 20:55:52 -0400
  * [MDEV-5146](https://jira.mariadb.org/browse/MDEV-5146) : Bulk loads into partitioned table not working
* [Revision #ccd39b2](https://github.com/MariaDB/server/commit/ccd39b2)\
  2015-08-20 09:55:54 -0400
  * Backport partition tests from 10.0-galera.
* [Revision #98bebad](https://github.com/MariaDB/server/commit/98bebad)\
  2015-08-18 17:03:28 -0400
  * Fix for a typo.
* [Revision #9b475ee](https://github.com/MariaDB/server/commit/9b475ee)\
  2015-08-05 20:43:25 +0300
  * [MDEV-8289](https://jira.mariadb.org/browse/MDEV-8289): Semijoin inflates number of rows in query result - Make semi-join optimizer not to choose LooseScan when 1) the index is not covered and 2) full index scan will be required.
* [Revision #4374da6](https://github.com/MariaDB/server/commit/4374da6)\
  2015-08-18 11:27:00 +0300
  * Merge /my/maria-10.1-default into 10.1
* [Revision #dfac82e](https://github.com/MariaDB/server/commit/dfac82e)\
  2015-08-18 11:17:54 +0300
  * Fixed failing tests and compiler warnings - UNINIT\_VAR() was required for 4.8.3 on openSUSE 13.2
* [Revision #6b20342](https://github.com/MariaDB/server/commit/6b20342)\
  2015-08-18 00:42:08 +0300
  * Ensure that fields declared with NOT NULL doesn't have DEFAULT values if not specified and if not timestamp or auto\_increment
* [Revision #92fd658](https://github.com/MariaDB/server/commit/92fd658)\
  2015-07-17 16:27:41 +0300
  * [MDEV-8475](https://jira.mariadb.org/browse/MDEV-8475) stale .TMM file causes MyiSAM and Aria engine to stop serving the table
* [Revision #5fe8b74](https://github.com/MariaDB/server/commit/5fe8b74)\
  2015-08-17 15:53:43 +0400
  * Adding EXPLAIN SELECT tests for: [MDEV-7649](https://jira.mariadb.org/browse/MDEV-7649) wrong result when comparing utf8 column with an invalid literal This is a preparatory patch for: [MDEV-8433](https://jira.mariadb.org/browse/MDEV-8433) Make field<'broken-string' use indexes
* [Revision #c6a0cbd](https://github.com/MariaDB/server/commit/c6a0cbd)\
  2015-08-14 14:59:43 -0400
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #fe757e0](https://github.com/MariaDB/server/commit/fe757e0)\
  2015-08-14 13:45:52 -0400
  * Fix for some failing tests.
* [Revision #78b80cb](https://github.com/MariaDB/server/commit/78b80cb)\
  2015-08-14 18:34:41 +0400
  * Adding MY\_CHARSET\_HANDLER::native\_to\_mb(). This is a pre-requisite patch for: - [MDEV-8433](https://jira.mariadb.org/browse/MDEV-8433) Make field<'broken-string' use indexes - [MDEV-8625](https://jira.mariadb.org/browse/MDEV-8625) Bad result set with ignorable characters when using a prefix key - [MDEV-8626](https://jira.mariadb.org/browse/MDEV-8626) Bad result set with contractions when using a prefix key
* [Revision #bfb6ea0](https://github.com/MariaDB/server/commit/bfb6ea0)\
  2015-08-14 11:09:06 +0300
  * [MDEV-8589](https://jira.mariadb.org/browse/MDEV-8589): Non-default ENCRYPTION\_KEY\_ID is ignored upon reading a table
* [Revision #a807535](https://github.com/MariaDB/server/commit/a807535)\
  2015-08-14 15:49:56 +0300
  * [MDEV-8591](https://jira.mariadb.org/browse/MDEV-8591): Database page corruption on disk or a failed space, Assertion failure in file buf0buf.cc line 2856 on querying a table using wrong default encryption key
* [Revision #7145ca4](https://github.com/MariaDB/server/commit/7145ca4)\
  2015-08-14 11:11:39 +0400
  * Recording range\_mrr\_icp.result (forgotten in the patch for [MDEV-8613](https://jira.mariadb.org/browse/MDEV-8613))
* [Revision #5cf737c](https://github.com/MariaDB/server/commit/5cf737c)\
  2015-08-14 02:46:32 -0400
  * [MDEV-8464](https://jira.mariadb.org/browse/MDEV-8464) : ALTER VIEW not replicated in some cases
* [Revision #52f1543](https://github.com/MariaDB/server/commit/52f1543)\
  2015-08-14 01:37:21 -0400
  * Fix for a memory leak.
* [Revision #e996304](https://github.com/MariaDB/server/commit/e996304)\
  2015-08-14 01:31:38 -0400
  * [MDEV-8617](https://jira.mariadb.org/browse/MDEV-8617): Multiple galera tests failures with --ps-protocol
* [Revision #e99bc0d](https://github.com/MariaDB/server/commit/e99bc0d)\
  2015-08-14 09:23:03 +0400
  * Removing unused String\_copier::copy\_fix. Fixing misleading comments in String\_copiers::well\_formed\_copy().
* [Revision #8a18bb9](https://github.com/MariaDB/server/commit/8a18bb9)\
  2015-08-14 01:17:57 -0400
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #c18e0da](https://github.com/MariaDB/server/commit/c18e0da)\
  2015-08-14 00:01:18 -0400
  * [MDEV-8617](https://jira.mariadb.org/browse/MDEV-8617): Multiple galera tests failures with --ps-protocol
* [Revision #0750b2d](https://github.com/MariaDB/server/commit/0750b2d)\
  2015-08-13 16:41:02 +0400
  * [MDEV-8613](https://jira.mariadb.org/browse/MDEV-8613) Full table scan for WHERE indexed\_varchar\_column <=> 'bad-character'
* [Revision #60985e5](https://github.com/MariaDB/server/commit/60985e5)\
  2015-08-13 14:25:51 +0400
  * [MDEV-8610](https://jira.mariadb.org/browse/MDEV-8610) "WHERE CONTAINS(indexed\_geometry\_column,1)" causes full table scan
* [Revision #1bfe4da](https://github.com/MariaDB/server/commit/1bfe4da)\
  2015-08-13 01:28:15 +0300
  * Fixed mysqltest run failure: Test did not clean up after itself properly
* [Revision #afa9cb7](https://github.com/MariaDB/server/commit/afa9cb7)\
  2015-08-13 01:27:23 +0300
  * Fixed overrun in key cache if one tried to allocate a key cache of more than 45G with a key\_cache\_block\_size of 1024 or less.
* [Revision #e998dff](https://github.com/MariaDB/server/commit/e998dff)\
  2015-08-12 17:47:25 -0400
  * [MDEV-8598](https://jira.mariadb.org/browse/MDEV-8598) : Failed MySQL DDL commands and Galera replication
* [Revision #9d884fd](https://github.com/MariaDB/server/commit/9d884fd)\
  2015-08-12 17:28:45 +0400
  * [MDEV-8599](https://jira.mariadb.org/browse/MDEV-8599) "WHERE varchar\_field LIKE temporal\_const" does not use range optimizer
* [Revision #6e091dc](https://github.com/MariaDB/server/commit/6e091dc)\
  2015-08-12 14:43:17 +0400
  * Splitting a static function get\_func\_mm\_tree() into virtual methods in Item\_bool\_func descendants, which gives some advantages: - Removing the "bool inv" parameter, as its now available through "this" for Item\_func\_between and Item\_func\_in, and is not needed for the other Item\_func\_xxx. - Removing casts - Making a step to data types plugings
* [Revision #9a64262](https://github.com/MariaDB/server/commit/9a64262)\
  2015-08-12 10:52:12 +0400
  * Removing RANGE\_OPT\_PARA::cond Its initialization in Item\_func\_xxx::get\_mm\_tree() is redundant: the pointer to the current function is passed to get\_mm\_tree() anyway.
* [Revision #86a3613](https://github.com/MariaDB/server/commit/86a3613)\
  2015-08-10 11:46:41 +0400
  * [MDEV-8441](https://jira.mariadb.org/browse/MDEV-8441) Bad SHOW CREATE TABLE output for a table with a virtual column
* [Revision #840aefc](https://github.com/MariaDB/server/commit/840aefc)\
  2015-08-09 14:16:50 -0400
  * [MDEV-8590](https://jira.mariadb.org/browse/MDEV-8590): Fix embedded build failure
* [Revision #cd1a11a](https://github.com/MariaDB/server/commit/cd1a11a)\
  2015-08-08 15:04:15 -0400
  * [MDEV-7205](https://jira.mariadb.org/browse/MDEV-7205) : Galera cluster & sql\_log\_bin = off don't work
* [Revision #91acc8b](https://github.com/MariaDB/server/commit/91acc8b)\
  2015-08-08 14:21:22 -0400
  * Merge tag 'mariadb-10.0.21' into 10.0-galera
* [Revision #46ad86f](https://github.com/MariaDB/server/commit/46ad86f)\
  2015-08-08 12:49:20 +0300
  * [MDEV-8582](https://jira.mariadb.org/browse/MDEV-8582): innodb\_force\_primary\_key option does not force PK or unique key
* [Revision #3307eaa](https://github.com/MariaDB/server/commit/3307eaa)\
  2015-08-08 10:39:01 +0300
  * [MDEV-8582](https://jira.mariadb.org/browse/MDEV-8582): innodb\_force\_primary\_key option does not force PK or unique key
* [Revision #05bcb08](https://github.com/MariaDB/server/commit/05bcb08)\
  2015-08-08 10:09:45 +0300
  * [MDEV-8583](https://jira.mariadb.org/browse/MDEV-8583): Empty lines in encryption logging
* [Revision #18b0176](https://github.com/MariaDB/server/commit/18b0176)\
  2015-08-07 15:21:20 +0300
  * [MDEV-8410](https://jira.mariadb.org/browse/MDEV-8410): Changing file-key-management to example-key-management causes crash and no real error [MDEV-8409](https://jira.mariadb.org/browse/MDEV-8409): Changing file-key-management-encryption-algorithm causes crash and no real info why
* [Revision #5b9dd45](https://github.com/MariaDB/server/commit/5b9dd45)\
  2015-08-07 17:02:51 -0400
  * Merge tag 'mariadb-5.5.45' into 5.5-galera
* [Revision #3025c42](https://github.com/MariaDB/server/commit/3025c42)\
  2015-08-07 17:41:35 +0300
  * Make ANALYZE FORMAT=JSON show execution time for filesort element.
* [Revision #4c69dc8](https://github.com/MariaDB/server/commit/4c69dc8)\
  2015-08-06 00:36:40 -0400
  * [MDEV-7501](https://jira.mariadb.org/browse/MDEV-7501) : alter table exchange partition is not replicated in galera cluster
* [Revision #0403790](https://github.com/MariaDB/server/commit/0403790)\
  2015-08-05 20:07:46 +0200
  * increase the VERSION
* [Revision #50ef006](https://github.com/MariaDB/server/commit/50ef006)\
  2015-08-05 09:45:36 +0200
  * Merge branch '10.0' into bb-10.0-serg
* [Revision #928edb5](https://github.com/MariaDB/server/commit/928edb5)\
  2015-08-05 09:45:17 +0200
  * Merge branch '5.5' into 10.0
* [Revision #1610c42](https://github.com/MariaDB/server/commit/1610c42)\
  2015-08-05 00:02:46 +0200
  * Merge branch 'bb-10.0-jan' into 10.0
* [Revision #fa51f70](https://github.com/MariaDB/server/commit/fa51f70)\
  2015-08-04 23:42:44 +0200
  * correct the NULL-pointer test
* [Revision #006ffca](https://github.com/MariaDB/server/commit/006ffca)\
  2015-08-04 23:40:25 +0200
  * after-merge fixes
* [Revision #afd59b5](https://github.com/MariaDB/server/commit/afd59b5)\
  2015-08-04 15:47:30 +0200
  * Merge branch 'mdev8302-3' into 10.1
* [Revision #d6d5458](https://github.com/MariaDB/server/commit/d6d5458)\
  2015-08-04 15:38:03 +0200
  * Merge fix of embedded server build.
* [Revision #5ca061e](https://github.com/MariaDB/server/commit/5ca061e)\
  2015-08-04 15:35:04 +0200
  * Fix embedded server build
* [Revision #dbd2057](https://github.com/MariaDB/server/commit/dbd2057)\
  2015-08-04 12:39:22 +0200
  * Merge [MDEV-8302](https://jira.mariadb.org/browse/MDEV-8302) into 10.1
* [Revision #e8e2ef4](https://github.com/MariaDB/server/commit/e8e2ef4)\
  2015-08-04 11:53:14 +0200
  * Merge [MDEV-8302](https://jira.mariadb.org/browse/MDEV-8302) into 10.0
* [Revision #9b9c5e8](https://github.com/MariaDB/server/commit/9b9c5e8)\
  2015-08-04 11:20:03 +0200
  * [MDEV-8302](https://jira.mariadb.org/browse/MDEV-8302): Duplicate key with parallel replication
* [Revision #d71b584](https://github.com/MariaDB/server/commit/d71b584)\
  2015-08-04 08:33:31 +0300
  * Fix merge error.
* [Revision #9a5787d](https://github.com/MariaDB/server/commit/9a5787d)\
  2015-08-03 23:09:43 +0300
  * Merge commit '96badb16afcf' into 10.0
* [Revision #b74795b](https://github.com/MariaDB/server/commit/b74795b)\
  2015-07-29 21:38:45 +0300
  * [MDEV-7040](https://jira.mariadb.org/browse/MDEV-7040): Crash in field\_conv, memcpy\_field\_possible, part#2
* [Revision #cb92549](https://github.com/MariaDB/server/commit/cb92549)\
  2015-08-03 20:47:43 +0300
  * Merge branch 'tmp' into 10.0
* [Revision #193faa5](https://github.com/MariaDB/server/commit/193faa5)\
  2015-07-30 22:08:39 +0300
  * [MDEV-8554](https://jira.mariadb.org/browse/MDEV-8554): Server crashes in base\_list\_iterator::next\_fast ...
* [Revision #877de3a](https://github.com/MariaDB/server/commit/877de3a)\
  2015-07-30 22:08:39 +0300
  * [MDEV-8554](https://jira.mariadb.org/browse/MDEV-8554): Server crashes in base\_list\_iterator::next\_fast ...
* [Revision #0785b2d](https://github.com/MariaDB/server/commit/0785b2d)\
  2015-08-03 17:10:20 +0200
  * Merge '[MariaDB](https://github.com/Buggynours/MariaDB) 10.0' into 10.0
* [Revision #58a73e7](https://github.com/MariaDB/server/commit/58a73e7)\
  2015-08-03 16:48:19 +0200
  * remove generated CONNECT files
* [Revision #0a99293](https://github.com/MariaDB/server/commit/0a99293)\
  2015-08-03 16:34:59 +0200
  * Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #ab7b672](https://github.com/MariaDB/server/commit/ab7b672)\
  2015-08-03 16:23:58 +0200
  * Merge branch 'merge-innodb-5.6' into 10.0
* [Revision #4f479fb](https://github.com/MariaDB/server/commit/4f479fb)\
  2015-08-03 14:03:46 +0200
  * Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #167c540](https://github.com/MariaDB/server/commit/167c540)\
  2015-08-03 13:05:40 +0200
  * 5.6.26
* [Revision #5654412](https://github.com/MariaDB/server/commit/5654412)\
  2015-08-03 13:03:47 +0200
  * 5.6.26
* [Revision #772c3f3](https://github.com/MariaDB/server/commit/772c3f3)\
  2015-07-28 17:56:11 +0200
  * .gitattributes: pcre/testdata/greppatN4 -text
* [Revision #a0107d9](https://github.com/MariaDB/server/commit/a0107d9)\
  2015-07-28 00:05:42 +0200
  * [MDEV-8296](https://jira.mariadb.org/browse/MDEV-8296) MSVS 2013 & WiX 3.9
* [Revision #9cb8cff](https://github.com/MariaDB/server/commit/9cb8cff)\
  2015-07-28 00:01:59 +0200
  * [MDEV-8296](https://jira.mariadb.org/browse/MDEV-8296) MSVS 2013 & WiX 3.9
* [Revision #17a4a39](https://github.com/MariaDB/server/commit/17a4a39)\
  2015-08-01 15:08:33 +0200
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #0b3eb45](https://github.com/MariaDB/server/commit/0b3eb45)\
  2015-08-01 15:04:20 +0200
  * 5.6.25-73.1
* [Revision #1b0c81c](https://github.com/MariaDB/server/commit/1b0c81c)\
  2015-08-01 15:02:14 +0200
  * 5.5.44-37.3
* [Revision #6300f2f](https://github.com/MariaDB/server/commit/6300f2f)\
  2015-08-01 14:56:18 +0200
  * Merge tag 'mysql-5.5.45' into 5.5
* [Revision #96badb1](https://github.com/MariaDB/server/commit/96badb1)\
  2015-07-31 22:09:46 +0200
  * [MDEV-7821](https://jira.mariadb.org/browse/MDEV-7821) Server crashes in Item\_func\_group\_concat::fix\_fields on 2nd execution of PS
* [Revision #409709e](https://github.com/MariaDB/server/commit/409709e)\
  2015-07-31 20:33:10 +0200
  * compilation error on windows
* [Revision #82cecb1](https://github.com/MariaDB/server/commit/82cecb1)\
  2015-07-31 11:21:57 -0400
  * [MDEV-8240](https://jira.mariadb.org/browse/MDEV-8240) : Unknown option 'table\_type' when using Connect Engine on MGC
* [Revision #79deefc](https://github.com/MariaDB/server/commit/79deefc)\
  2015-07-31 12:31:37 +0200
  * [MDEV-8340](https://jira.mariadb.org/browse/MDEV-8340) Add "mysqlbinlog --binlog-row-event-max-size" support for [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md)
* [Revision #4d5772c](https://github.com/MariaDB/server/commit/4d5772c)\
  2015-07-31 10:13:01 +0200
  * [MDEV-7810](https://jira.mariadb.org/browse/MDEV-7810) Wrong result on execution of a query as a PS (both 1st and further executions)
* [Revision #2721d69](https://github.com/MariaDB/server/commit/2721d69)\
  2015-07-28 19:11:53 +0200
  * [MDEV-8352](https://jira.mariadb.org/browse/MDEV-8352) Increase Diffie-Helman modulus to 2048-bits
* [Revision #bfe2689](https://github.com/MariaDB/server/commit/bfe2689)\
  2015-07-31 13:13:39 +0400
  * [MDEV-8379](https://jira.mariadb.org/browse/MDEV-8379) - SUSE mariadb patches
* [Revision #360e597](https://github.com/MariaDB/server/commit/360e597)\
  2015-07-31 12:06:29 +0300
  * Make sure name buffer has string end marker on correct place.
* [Revision #1ad294e](https://github.com/MariaDB/server/commit/1ad294e)\
  2015-07-30 18:51:44 +0400
  * [MDEV-7821](https://jira.mariadb.org/browse/MDEV-7821) - Server crashes in Item\_func\_group\_concat::fix\_fields on 2nd execution of PS
* [Revision #fa765a4](https://github.com/MariaDB/server/commit/fa765a4)\
  2015-07-31 08:52:24 +0300
  * [MDEV-6697](https://jira.mariadb.org/browse/MDEV-6697): Improve foreign keys warnings/errors
* [Revision #e05cd97](https://github.com/MariaDB/server/commit/e05cd97)\
  2015-07-29 05:58:45 +0300
  * [MDEV-8524](https://jira.mariadb.org/browse/MDEV-8524): Improve error messaging when there is duplicate key or foreign key names
* [Revision #8ab46a5](https://github.com/MariaDB/server/commit/8ab46a5)\
  2015-07-30 13:27:56 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #7962add](https://github.com/MariaDB/server/commit/7962add)\
  2015-07-30 13:15:54 +0200
  * Fix [MDEV-8561](https://jira.mariadb.org/browse/MDEV-8561) removing a wrong patch modified: storage/connect/tabodbc.cpp
* [Revision #c4456b9](https://github.com/MariaDB/server/commit/c4456b9)\
  2015-07-30 14:02:44 +0300
  * [MDEV-7971](https://jira.mariadb.org/browse/MDEV-7971): Assertion \`name != null' failed in ACL\_internal\_schema\_registry::lookup...
* [Revision #0abde01](https://github.com/MariaDB/server/commit/0abde01)\
  2015-07-29 18:04:40 -0400
  * [MDEV-8240](https://jira.mariadb.org/browse/MDEV-8240) : Unknown option 'table\_type' when using Connect Engine on MGC
* [Revision #392df76](https://github.com/MariaDB/server/commit/392df76)\
  2015-07-23 12:50:58 +0400
  * [MDEV-4017](https://jira.mariadb.org/browse/MDEV-4017) - GET\_LOCK() with negative timeouts has strange behavior
* [Revision #4188ba9](https://github.com/MariaDB/server/commit/4188ba9)\
  2015-07-28 10:18:55 +0400
  * [MDEV-7652](https://jira.mariadb.org/browse/MDEV-7652) - More explanatory ERROR and WARNING messages when loading plugins with plugin-load-add that are already registered at mysql.plugin
* [Revision #701af14](https://github.com/MariaDB/server/commit/701af14)\
  2015-07-28 19:39:02 +0200
  * Merge branch 'ob-10.0' into 10.0
* [Revision #cf30074](https://github.com/MariaDB/server/commit/cf30074)\
  2015-07-27 12:50:51 +0200
  * [MDEV-7968](https://jira.mariadb.org/browse/MDEV-7968) Virtual column set to NULL using load data infile
* [Revision #6f14531](https://github.com/MariaDB/server/commit/6f14531)\
  2015-07-26 00:05:58 +0200
  * CONNECT: compiler warnings
* [Revision #00967e1](https://github.com/MariaDB/server/commit/00967e1)\
  2015-07-26 00:04:36 +0200
  * CONNECT: clean up a stray variable
* [Revision #40a6160](https://github.com/MariaDB/server/commit/40a6160)\
  2015-07-26 00:03:34 +0200
  * [MDEV-7574](https://jira.mariadb.org/browse/MDEV-7574) Security definer views don't work with CONNECT ODBC tables
* [Revision #121f3e4](https://github.com/MariaDB/server/commit/121f3e4)\
  2015-07-25 13:13:22 +0200
  * [MDEV-7429](https://jira.mariadb.org/browse/MDEV-7429) main.mysqldump fails sporadically in buildbot
* [Revision #cd0813e](https://github.com/MariaDB/server/commit/cd0813e)\
  2015-07-25 12:21:51 +0200
  * [MDEV-8534](https://jira.mariadb.org/browse/MDEV-8534) \[PATCH] mysql\_secure\_installation doesn't pass "socket" to "mysql"
* [Revision #39f5234](https://github.com/MariaDB/server/commit/39f5234)\
  2015-07-25 12:17:10 +0200
  * [MDEV-8534](https://jira.mariadb.org/browse/MDEV-8534) \[PATCH] mysql\_secure\_installation doesn't pass "socket" to "mysql"
* [Revision #517ef2b](https://github.com/MariaDB/server/commit/517ef2b)\
  2015-07-26 14:31:22 +0300
  * Added easy way to assert if another thread has died. Added some extra safety asserts in MyISAM key cache.
* [Revision #f3e578a](https://github.com/MariaDB/server/commit/f3e578a)\
  2015-07-26 14:19:04 +0300
  * Fixed [MDEV-8428](https://jira.mariadb.org/browse/MDEV-8428): Mangled DML statements on 2nd level slave when enabling binlog checksums
* [Revision #e40bc65](https://github.com/MariaDB/server/commit/e40bc65)\
  2015-07-25 15:14:40 +0300
  * Fixed memory loss detected on P8. This can happen when we call after\_flush but never call after\_rollback() or after\_commit().
* [Revision #7115341](https://github.com/MariaDB/server/commit/7115341)\
  2015-07-23 14:57:12 +0300
  * Fixed warnings and errors found by buildbot
* [Revision #2ebedfa](https://github.com/MariaDB/server/commit/2ebedfa)\
  2015-07-25 00:58:36 +0300
  * [MDEV-8532](https://jira.mariadb.org/browse/MDEV-8532) MTR cannot run with --embedded on Windows on a source build
* [Revision #35a0198](https://github.com/MariaDB/server/commit/35a0198)\
  2015-02-09 13:41:24 +0400
  * [MDEV-5096](https://jira.mariadb.org/browse/MDEV-5096) - Wrong error message on attempt to kill somebody else's query ID
* [Revision #a6ab8ef](https://github.com/MariaDB/server/commit/a6ab8ef)\
  2011-04-22 16:59:10 +0400
  * [MDEV-5997](https://jira.mariadb.org/browse/MDEV-5997) - MySQL bug#11759114 - '51401: GRANT TREATS NONEXISTENT FUNCTIONS/PRIVILEGES DIFFERENTLY'
* [Revision #d897015](https://github.com/MariaDB/server/commit/d897015)\
  2015-07-16 16:17:17 +0400
  * [MDEV-8399](https://jira.mariadb.org/browse/MDEV-8399) - \[PATCH] Missing Sanity Checks for memory allocation in MariaDB
* [Revision #4efcc35](https://github.com/MariaDB/server/commit/4efcc35)\
  2015-07-22 13:21:55 +0200
  * Fix (?) retrieving integer arguments in JSON UDF's modified: storage/connect/jsonudf.cpp
* [Revision #cb3a71d](https://github.com/MariaDB/server/commit/cb3a71d)\
  2015-07-22 11:17:55 +0400
  * Updating the instructions on how to prepare the OS to run "mtr connect.odbc\_postgresql"
* [Revision #7a96702](https://github.com/MariaDB/server/commit/7a96702)\
  2015-07-21 12:12:58 +0300
  * [MDEV-8474](https://jira.mariadb.org/browse/MDEV-8474): InnoDB sets per-connection data unsafely
* [Revision #83ba48b](https://github.com/MariaDB/server/commit/83ba48b)\
  2015-07-20 20:16:32 +0300
  * [MDEV-8506](https://jira.mariadb.org/browse/MDEV-8506) mroonga/wrapper.performance\_schema fails in buildbot on bld-dan-release
* [Revision #0bb0ace](https://github.com/MariaDB/server/commit/0bb0ace)\
  2015-07-20 14:36:30 +0300
  * [MDEV-8443](https://jira.mariadb.org/browse/MDEV-8443): mysql-test - innodb.innodb\_simulate\_comp\_failures 'innodb\_plugin' is failing
* [Revision #af2f7ce](https://github.com/MariaDB/server/commit/af2f7ce)\
  2015-07-19 22:51:19 -0400
  * [MDEV-8464](https://jira.mariadb.org/browse/MDEV-8464) : ALTER VIEW not replicated in some cases
* [Revision #40215a9](https://github.com/MariaDB/server/commit/40215a9)\
  2015-07-19 09:31:02 +0200
  * Merge [MDEV-8496](https://jira.mariadb.org/browse/MDEV-8496) into 10.0
* [Revision #a63d873](https://github.com/MariaDB/server/commit/a63d873)\
  2015-07-17 00:07:01 +0300
  * Merge branch '5.5' of github.com:MariaDB/server into 5.5
* [Revision #00d3b20](https://github.com/MariaDB/server/commit/00d3b20)\
  2015-07-17 00:06:27 +0300
  * [MDEV-8432](https://jira.mariadb.org/browse/MDEV-8432) Slave cannot replicate signed integer-type values with high bit set to 1
* [Revision #44de090](https://github.com/MariaDB/server/commit/44de090)\
  2015-07-17 00:02:25 +0300
  * [MDEV-8432](https://jira.mariadb.org/browse/MDEV-8432) Slave cannot replicate signed integer-type values with high bit set to 1
* [Revision #12da27d](https://github.com/MariaDB/server/commit/12da27d)\
  2015-07-16 16:28:06 +0400
  * [MDEV-8472](https://jira.mariadb.org/browse/MDEV-8472) BINARY, VARBINARY and BLOB return different warnings on CAST to DECIMAL
* [Revision #94bc506](https://github.com/MariaDB/server/commit/94bc506)\
  2015-06-30 18:01:40 +0400
  * [MDEV-8374](https://jira.mariadb.org/browse/MDEV-8374) - Debian: mysqld\_safe Can't log to error log and syslog at the same time
* [Revision #6efdc39](https://github.com/MariaDB/server/commit/6efdc39)\
  2015-07-14 20:36:23 +0300
  * [MDEV-8463](https://jira.mariadb.org/browse/MDEV-8463): 10.0 tree does not build
* [Revision #a9960ef](https://github.com/MariaDB/server/commit/a9960ef)\
  2015-06-30 19:43:34 +0300
  * [MDEV-8386](https://jira.mariadb.org/browse/MDEV-8386): MARIADB creates very big tmp file > 351Gb. Started happening after Version 10.0.16-15
* [Revision #0a43236](https://github.com/MariaDB/server/commit/0a43236)\
  2015-06-30 19:07:55 +0300
  * Code cleanup.
* [Revision #3bbffc2](https://github.com/MariaDB/server/commit/3bbffc2)\
  2015-07-13 19:29:09 +0300
  * Merge pull request #85 from josh4trunks/10.0
* [Revision #a95be96](https://github.com/MariaDB/server/commit/a95be96)\
  2015-07-12 19:53:38 -0700
  * Apply fix for raw devices to XtraDB
* [Revision #ee5633a](https://github.com/MariaDB/server/commit/ee5633a)\
  2015-07-12 19:46:29 -0700
  * Apply fix for raw devices to XtraDB
* [Revision #d983565](https://github.com/MariaDB/server/commit/d983565)\
  2015-07-10 14:03:39 +0300
  * Updated fill\_help\_tables for MariaDB - References changed from mysql.com to mariadb.com/kb - NDB specfic things removed - Changed other MySQL related things to MariaDB
* [Revision #b520feb](https://github.com/MariaDB/server/commit/b520feb)\
  2015-07-09 12:33:17 +0200
  * Resolving conflict on ha\_connect.cc
* [Revision #fdd9af5](https://github.com/MariaDB/server/commit/fdd9af5)\
  2015-07-07 19:37:05 +0200
  * Correct typo in endian.test
* [Revision #0efaedf](https://github.com/MariaDB/server/commit/0efaedf)\
  2015-07-07 18:16:42 +0200
  * Add some new tests: storage/connect/mysql-test/connect/r/endian.result storage/connect/mysql-test/connect/r/mysql\_index.result storage/connect/mysql-test/connect/t/endian.test storage/connect/mysql-test/connect/t/mysql\_index.test
* [Revision #6114101](https://github.com/MariaDB/server/commit/6114101)\
  2015-07-07 15:55:32 +0200
  * Fix regression bug on "select max(length(nom)) from emp1" when: The emp1 table type is MYSQL nom is an indexed column
* [Revision #f073593](https://github.com/MariaDB/server/commit/f073593)\
  2015-07-06 12:33:11 +0200
  * Fix loosing result lines when all of this is true: The table type is MYSQL The query where clause includes an indexed column The where clause contains < or <= operator on this column Change version date modified: storage/connect/ha\_connect.cc modified: storage/connect/tabmysql.cpp
* [Revision #1a8cf15](https://github.com/MariaDB/server/commit/1a8cf15)\
  2015-06-30 22:24:37 +0300
  * [MDEV-8392](https://jira.mariadb.org/browse/MDEV-8392): Couldn't alter field with default value for make it not nullable.
* [Revision #bc30046](https://github.com/MariaDB/server/commit/bc30046)\
  2015-06-26 14:48:22 +0300
  * Fix for [MDEV-8301](https://jira.mariadb.org/browse/MDEV-8301); Statistics for a thread could be counted twice in SHOW STATUS while thread was ending
* [Revision #67c56ab](https://github.com/MariaDB/server/commit/67c56ab)\
  2015-06-25 23:34:54 +0300
  * Simple cleanups - Removing use of calls to current\_thd - More DBUG\_PRINT - Code style changes - Made some local functions static Ensure that calls to print\_keyuse are locked with mutex to get all lines in same debug packet
* [Revision #8c81575](https://github.com/MariaDB/server/commit/8c81575)\
  2015-06-25 23:26:29 +0300
  * Problem was that for cases like: SELECT ... WHERE XX IN (SELECT YY) this was transformed to something like: SELECT ... WHERE IF\_EXISTS(SELECT ... HAVING XX=YY)
* [Revision #2e941fe](https://github.com/MariaDB/server/commit/2e941fe)\
  2015-06-25 23:18:48 +0300
  * Fixed crashing bug when using ONLY\_FULL\_GROUP\_BY in a stored procedure/trigger that is repeatedly executed. This is [MDEV-7601](https://jira.mariadb.org/browse/MDEV-7601), including it's sub tasks [MDEV-7594](https://jira.mariadb.org/browse/MDEV-7594), [MDEV-7555](https://jira.mariadb.org/browse/MDEV-7555), [MDEV-7590](https://jira.mariadb.org/browse/MDEV-7590), [MDEV-7581](https://jira.mariadb.org/browse/MDEV-7581), [MDEV-7589](https://jira.mariadb.org/browse/MDEV-7589)
* [Revision #8e524d2](https://github.com/MariaDB/server/commit/8e524d2)\
  2015-06-25 00:06:55 +0200
  * Set maturity to GAMMA modified ha\_connect.cc
* [Revision #0e270f7](https://github.com/MariaDB/server/commit/0e270f7)\
  2015-06-25 00:01:38 +0200
  * Set maturity to GAMMA modified ha\_connect.cc
* [Revision #8af5ab4](https://github.com/MariaDB/server/commit/8af5ab4)\
  2015-06-24 16:53:41 +0200
  * Merge [MDEV-8354](https://jira.mariadb.org/browse/MDEV-8354) into 10.0

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
