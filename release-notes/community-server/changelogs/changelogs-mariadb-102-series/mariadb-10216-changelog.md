# MariaDB 10.2.16 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.16)[Release Notes](../../old-releases/10.2/10.2.16.md)[Changelog](mariadb-10216-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 26 Jun 2018

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.16.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #bb825194b8](https://github.com/MariaDB/server/commit/bb825194b8)\
  2018-06-25 14:04:16 +0300
  * Updated list of unstable tests for 10.2.16
* [Revision #ee6ac4d313](https://github.com/MariaDB/server/commit/ee6ac4d313)\
  2018-06-25 09:08:07 +0400
  * [MDEV-12574](https://jira.mariadb.org/browse/MDEV-12574) MAX(old\_decimal) produces a column of the old DECIMAL type
* [Revision #01bbb912bf](https://github.com/MariaDB/server/commit/01bbb912bf)\
  2018-06-24 15:30:54 +0200
  * update C/C
* Merge [Revision #a40c06e03a](https://github.com/MariaDB/server/commit/a40c06e03a) 2018-06-24 15:27:38 +0200 - Merge branch 'connect/10.2' into 10.2
* [Revision #c69efab396](https://github.com/MariaDB/server/commit/c69efab396)\
  2018-06-18 17:54:30 +0200\
  \*
  * Fix [MDEV-16167](https://jira.mariadb.org/browse/MDEV-16167) Cannot insert unsigned values into a VEC table modified: storage/connect/filamvct.cpp modified: storage/connect/tabvct.cpp
* [Revision #f577311027](https://github.com/MariaDB/server/commit/f577311027)\
  2018-06-23 23:44:11 +0200
  * fix mroonga post-install script
* [Revision #f25a5c39c1](https://github.com/MariaDB/server/commit/f25a5c39c1)\
  2018-06-23 15:37:09 +0200
  * [MDEV-14560](https://jira.mariadb.org/browse/MDEV-14560) Extra engines enabled through additional config are not loaded on first installation
* [Revision #a19089ff4e](https://github.com/MariaDB/server/commit/a19089ff4e)\
  2018-06-22 17:41:33 +0200
  * [MDEV-16537](https://jira.mariadb.org/browse/MDEV-16537) aws key management plugin on Ubuntu bionic has impossible dependencies
* [Revision #ffb96be9e7](https://github.com/MariaDB/server/commit/ffb96be9e7)\
  2018-06-22 14:13:10 +0200
  * fix debian packaging for tokudb
* [Revision #b2190f859b](https://github.com/MariaDB/server/commit/b2190f859b)\
  2018-06-22 15:45:17 +0200
  * fix vcol.vcol\_misc --embedded
* [Revision #e561a346c3](https://github.com/MariaDB/server/commit/e561a346c3)\
  2018-06-23 15:30:52 +0200
  * fix mtr warnings after 5f0510225aa
* [Revision #95ef8de891](https://github.com/MariaDB/server/commit/95ef8de891)\
  2018-06-22 23:30:26 +0100
  * mariadb-backup - rename backup-rocksdb option to rocksdb-backup
* [Revision #ecc4682672](https://github.com/MariaDB/server/commit/ecc4682672)\
  2018-06-22 15:24:09 +0100
  * [MDEV-16519](https://jira.mariadb.org/browse/MDEV-16519) : mariadb-backup should fail if MDL could not be acquired with lock-ddl-per-table
* [Revision #0d745343fc](https://github.com/MariaDB/server/commit/0d745343fc)\
  2018-06-22 09:52:21 +0200
  * fix plugins.processlist
* [Revision #ef64856b97](https://github.com/MariaDB/server/commit/ef64856b97)\
  2018-06-21 23:49:37 +0200
  * don't crash on innodb\_undo\_tablespaces=1
* [Revision #082eec1418](https://github.com/MariaDB/server/commit/082eec1418)\
  2018-06-21 23:48:59 +0200
  * SET wsrep\_on=1 - only check innodb\_lock\_schedule\_algorithm if innodb is enabled
* Merge [Revision #b942aa34c1](https://github.com/MariaDB/server/commit/b942aa34c1) 2018-06-21 23:47:39 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #c09a8b5b36](https://github.com/MariaDB/server/commit/c09a8b5b36) 2018-06-21 08:34:35 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #d8192f5495](https://github.com/MariaDB/server/commit/d8192f5495) 2018-06-21 00:44:10 +0200 - Merge branch '5.5' into 10.0
* [Revision #2b8f2b3e88](https://github.com/MariaDB/server/commit/2b8f2b3e88)\
  2018-06-20 23:30:49 +0200
  * Fix unit suite on Windows and in out-of-source builds
* [Revision #0a9d78f51d](https://github.com/MariaDB/server/commit/0a9d78f51d)\
  2018-06-20 23:27:23 +0200
  * Revert "[MDEV-16075](https://jira.mariadb.org/browse/MDEV-16075): Workaround to run MTR test suite for make test"
* Merge [Revision #4b821e02f6](https://github.com/MariaDB/server/commit/4b821e02f6) 2018-06-20 16:57:21 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* Merge [Revision #6c08ff3eb7](https://github.com/MariaDB/server/commit/6c08ff3eb7) 2018-06-20 16:55:24 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #170b43c156](https://github.com/MariaDB/server/commit/170b43c156)\
  2018-06-20 16:36:46 +0400
  * [MDEV-16534](https://jira.mariadb.org/browse/MDEV-16534) PPC64: Unexpected error with a negative value into auto-increment columns in HEAP, MyISAM, ARIA
* [Revision #5f2a67a6c3](https://github.com/MariaDB/server/commit/5f2a67a6c3)\
  2018-06-20 02:36:00 +0530
  * [MDEV-15247](https://jira.mariadb.org/browse/MDEV-15247): Crash when SET NAMES 'utf8' is set
* [Revision #bb24663f5a](https://github.com/MariaDB/server/commit/bb24663f5a)\
  2018-06-20 10:45:57 +0200
  * [MDEV-13577](https://jira.mariadb.org/browse/MDEV-13577) slave\_parallel\_mode=optimistic should not report the mode's specific temporary errors
* [Revision #44682962e3](https://github.com/MariaDB/server/commit/44682962e3)\
  2018-06-20 11:10:15 +0200
  * Fix another double WSREP\_ISOLATION\_BEGIN merge error
* [Revision #04c4745478](https://github.com/MariaDB/server/commit/04c4745478)\
  2018-06-20 01:28:59 +0300
  * Fix double WSREP\_ISOLATION\_BEGIN merge error
* Merge [Revision #f5b128dfad](https://github.com/MariaDB/server/commit/f5b128dfad) 2018-06-19 14:04:53 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* Merge [Revision #c450f7d8d5](https://github.com/MariaDB/server/commit/c450f7d8d5) 2018-06-19 14:03:41 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #15b92915ed](https://github.com/MariaDB/server/commit/15b92915ed)\
  2018-06-19 13:02:02 +0400
  * [MDEV-15834](https://jira.mariadb.org/browse/MDEV-15834) The code in TABLE\_SHARE::init\_from\_binary\_frm\_image() is not safe
* [Revision #e425216045](https://github.com/MariaDB/server/commit/e425216045)\
  2018-01-31 09:35:38 +0100
  * [MDEV-15113](https://jira.mariadb.org/browse/MDEV-15113): Hang in Aria loghandler
* [Revision #147744d455](https://github.com/MariaDB/server/commit/147744d455)\
  2018-06-11 08:52:26 -0700
  * [MDEV-16235](https://jira.mariadb.org/browse/MDEV-16235) Server crashes in my\_utf8\_uni or in my\_strtod\_int upon SELECT .. LIMIT 0 (new variant)
* [Revision #f7b1b2bc5d](https://github.com/MariaDB/server/commit/f7b1b2bc5d)\
  2018-06-18 07:40:58 -0400
  * bump the VERSION
* [Revision #fe3f9fa918](https://github.com/MariaDB/server/commit/fe3f9fa918)\
  2018-06-21 15:17:15 +0400
  * [MDEV-12809](https://jira.mariadb.org/browse/MDEV-12809) Bad column type created for TEXT(1431655798) CHARACTER SET utf8
* [Revision #635c5e3281](https://github.com/MariaDB/server/commit/635c5e3281)\
  2018-06-19 19:07:32 +0200
  * mysql\_install\_db: clarify the after-install message
* [Revision #df704b5a1b](https://github.com/MariaDB/server/commit/df704b5a1b)\
  2018-06-19 18:28:39 +0200
  * don't use my\_error(0) or my\_printf\_error(0)
* [Revision #af2dd582e6](https://github.com/MariaDB/server/commit/af2dd582e6)\
  2018-06-18 21:28:27 +0200
  * empty password is a valid password, don't crash
* [Revision #5f0510225a](https://github.com/MariaDB/server/commit/5f0510225a)\
  2018-06-18 21:00:25 +0200
  * [MDEV-16238](https://jira.mariadb.org/browse/MDEV-16238) root/localhost authn prioritizes authentication\_string over Password
* [Revision #b4db59ba47](https://github.com/MariaDB/server/commit/b4db59ba47)\
  2018-06-18 19:06:55 +0200
  * [MDEV-15596](https://jira.mariadb.org/browse/MDEV-15596) 10.2 doesn't work with openssl 1.1.1
* [Revision #1db1340c0c](https://github.com/MariaDB/server/commit/1db1340c0c)\
  2018-06-18 11:51:27 +0200
  * [MDEV-14578](https://jira.mariadb.org/browse/MDEV-14578): mysql\_install\_db install unix\_socket plugin when --auth-root-authentication-method=socket
* [Revision #53db5edbcf](https://github.com/MariaDB/server/commit/53db5edbcf)\
  2018-05-18 15:10:52 +1000
  * [MDEV-14578](https://jira.mariadb.org/browse/MDEV-14578): mysql\_install\_db install unix\_socket plugin when --auth-root-authentication-method=socket
* [Revision #1033fa4bcc](https://github.com/MariaDB/server/commit/1033fa4bcc)\
  2018-06-12 19:06:55 +0200
  * [MDEV-13403](https://jira.mariadb.org/browse/MDEV-13403) Mariadb (with TokuDB) excessive memory usage/leak
* [Revision #be9d923af2](https://github.com/MariaDB/server/commit/be9d923af2)\
  2018-06-20 22:45:10 +0400
  * [MDEV-11917](https://jira.mariadb.org/browse/MDEV-11917) enum/set command-line options aren't respecting max-\* settings.
* [Revision #621caad3ca](https://github.com/MariaDB/server/commit/621caad3ca)\
  2018-06-20 17:14:04 +0400
  * [MDEV-11917](https://jira.mariadb.org/browse/MDEV-11917) enum/set command-line options aren't respecting max-\* settings.
* [Revision #d79bf0009a](https://github.com/MariaDB/server/commit/d79bf0009a)\
  2018-06-20 01:23:07 +0300
  * [MDEV-16525](https://jira.mariadb.org/browse/MDEV-16525): MyRocks linking fails with: Undefined reference to \`ZDICT\_trainFromBuffer'
* [Revision #778df04661](https://github.com/MariaDB/server/commit/778df04661)\
  2018-06-19 19:19:40 +0200
  * [MDEV-16517](https://jira.mariadb.org/browse/MDEV-16517): Server crash in Item\_func\_in::val\_int() when IN predicate defined with non-constant values is pushed down
* [Revision #10d09a57f8](https://github.com/MariaDB/server/commit/10d09a57f8)\
  2018-06-18 22:44:58 +0300
  * Fixed failing test acl\_load\_mutex-5170
* [Revision #ab19466656](https://github.com/MariaDB/server/commit/ab19466656)\
  2018-06-17 14:19:51 +0300
  * [MDEV-15114](https://jira.mariadb.org/browse/MDEV-15114) ASAN heap-use-after-free in mem\_heap\_dup or dfield\_data\_is\_binary\_equal
* [Revision #831df10981](https://github.com/MariaDB/server/commit/831df10981)\
  2018-06-16 12:03:15 +0300
  * Add PART\_INDIRECT\_KEY\_FLAG
* [Revision #5ba6cee012](https://github.com/MariaDB/server/commit/5ba6cee012)\
  2018-06-18 23:00:34 +0400
  * [MDEV-16209](https://jira.mariadb.org/browse/MDEV-16209) JSON\_EXTRACT in query crashes server.
* [Revision #eb77f8cf8d](https://github.com/MariaDB/server/commit/eb77f8cf8d)\
  2018-06-18 14:26:37 +0530
  * [MDEV-16087](https://jira.mariadb.org/browse/MDEV-16087) Inconsistent SELECT results when query cache is enabled
* [Revision #352c7e0dfa](https://github.com/MariaDB/server/commit/352c7e0dfa)\
  2018-06-17 17:15:21 +0400
  * [MDEV-15905](https://jira.mariadb.org/browse/MDEV-15905) select json\_value('{"b":true}','$.b')=1 --> false with "Truncated incorrect DOUBLE value: 'true'".
* [Revision #b8514c94f6](https://github.com/MariaDB/server/commit/b8514c94f6)\
  2018-06-15 14:09:15 +0300
  * [MDEV-16496](https://jira.mariadb.org/browse/MDEV-16496) mariadb-backup: Implement --verbose option to instrument InnoDB log apply
* [Revision #ff317fe08e](https://github.com/MariaDB/server/commit/ff317fe08e)\
  2018-06-15 13:31:43 +0300
  * Follow-up to [MDEV-16367](https://jira.mariadb.org/browse/MDEV-16367) mariadb-backup: error: failed to copy enough redo log
* [Revision #6b8802e8dd](https://github.com/MariaDB/server/commit/6b8802e8dd)\
  2018-05-08 15:26:26 +0200
  * [MDEV-11071](https://jira.mariadb.org/browse/MDEV-11071): Assertion \`thd->transaction.stmt.is\_empty()' failed in Locked\_tables\_list::unlock\_locked\_table
* [Revision #c55de8d40b](https://github.com/MariaDB/server/commit/c55de8d40b)\
  2018-06-15 10:11:51 +0400
  * [MDEV-9334](https://jira.mariadb.org/browse/MDEV-9334) ALTER from DECIMAL to BIGINT UNSIGNED returns a wrong result
* [Revision #ec4fdd5749](https://github.com/MariaDB/server/commit/ec4fdd5749)\
  2018-06-13 16:32:25 +0200
  * [MDEV-16386](https://jira.mariadb.org/browse/MDEV-16386): Wrong result when pushdown into the HAVING clause of the materialized derived table/view that uses aliases is done
* [Revision #a79b033b35](https://github.com/MariaDB/server/commit/a79b033b35)\
  2018-06-14 14:23:20 +0300
  * [MDEV-16457](https://jira.mariadb.org/browse/MDEV-16457) mariadb-backup 10.2+ should default to innodb\_checksum\_algorithm=crc32
* [Revision #2ca904f0ca](https://github.com/MariaDB/server/commit/2ca904f0ca)\
  2018-06-13 16:15:21 +0300
  * [MDEV-13103](https://jira.mariadb.org/browse/MDEV-13103) Deal with page\_compressed page corruption
* [Revision #2cdb483bc4](https://github.com/MariaDB/server/commit/2cdb483bc4)\
  2018-06-14 13:13:23 +0400
  * [MDEV-15352](https://jira.mariadb.org/browse/MDEV-15352) AUTO\_INCREMENT breaks after updating a column value to a negative number
* [Revision #23ced2f846](https://github.com/MariaDB/server/commit/23ced2f846)\
  2018-06-13 23:37:09 +0400
  * [MDEV-16311](https://jira.mariadb.org/browse/MDEV-16311) Server crash when using a NAME\_CONST() with a CURSOR
* [Revision #8662015c90](https://github.com/MariaDB/server/commit/8662015c90)\
  2018-06-13 15:26:50 +0300
  * [MDEV-15304](https://jira.mariadb.org/browse/MDEV-15304): Server crash in print\_keydup\_error / key\_unpack or unexpected ER\_DUP\_KEY
* [Revision #931daaf79b](https://github.com/MariaDB/server/commit/931daaf79b)\
  2018-06-13 14:50:25 +0300
  * [MDEV-15319](https://jira.mariadb.org/browse/MDEV-15319): \[SQL Layer] Server crashes in Field::set\_null / myrocks::ha\_rocksdb ...
* [Revision #2412c15191](https://github.com/MariaDB/server/commit/2412c15191)\
  2018-06-13 11:56:56 +0400
  * [MDEV-15870](https://jira.mariadb.org/browse/MDEV-15870) Using aggregate and window function in unexpected places can crash the server
* [Revision #ae0aefb1c5](https://github.com/MariaDB/server/commit/ae0aefb1c5)\
  2018-06-12 14:12:36 +0400
  * [MDEV-12060](https://jira.mariadb.org/browse/MDEV-12060) Crash in EXECUTE IMMEDIATE with an expression returning a GRANT command
* [Revision #8f5f0575ab](https://github.com/MariaDB/server/commit/8f5f0575ab)\
  2018-06-11 13:02:47 +0300
  * [MDEV-16456](https://jira.mariadb.org/browse/MDEV-16456) InnoDB error "returned OS error 71" complains about wrong path
* [Revision #d54d067601](https://github.com/MariaDB/server/commit/d54d067601)\
  2018-06-11 21:16:37 +0300
  * Undo wrong my\_free overflow
* [Revision #ecd4c2b4a9](https://github.com/MariaDB/server/commit/ecd4c2b4a9)\
  2018-06-11 20:24:41 +0300
  * Add missed change from 7ffa82b03c8da12062223d5e332e972d6f828d44
* [Revision #aba2d7301f](https://github.com/MariaDB/server/commit/aba2d7301f)\
  2018-06-07 15:13:54 +0100
  * [MDEV-13122](https://jira.mariadb.org/browse/MDEV-13122) Backup myrocksdb with mariadb-backup.
* [Revision #ea70586282](https://github.com/MariaDB/server/commit/ea70586282)\
  2018-06-07 15:12:26 +0100
  * [MDEV-16300](https://jira.mariadb.org/browse/MDEV-16300) : remove rocksdb checkpoint created by mariadb-backup.
* [Revision #dc9c555415](https://github.com/MariaDB/server/commit/dc9c555415)\
  2018-06-07 14:29:35 +0300
  * [MDEV-16367](https://jira.mariadb.org/browse/MDEV-16367) mariadb-backup: error: failed to copy enough redo log
* [Revision #619c277a6c](https://github.com/MariaDB/server/commit/619c277a6c)\
  2018-06-07 14:11:55 +0300
  * mariadb-backup: Make some globals static
* Merge [Revision #df42830b28](https://github.com/MariaDB/server/commit/df42830b28) 2018-06-06 11:25:33 +0300 - Merge 10.1 into 10.2
* [Revision #738c5c8424](https://github.com/MariaDB/server/commit/738c5c8424)\
  2018-01-12 13:06:14 +0000
  * [MDEV-12642](https://jira.mariadb.org/browse/MDEV-12642): Build deb source packages on buildbot, just not on Travis-CI
* [Revision #8dc70c862b](https://github.com/MariaDB/server/commit/8dc70c862b)\
  2018-06-04 15:55:37 +0300
  * [MDEV-16376](https://jira.mariadb.org/browse/MDEV-16376) ASAN: heap-use-after-free in gcol.innodb\_virtual\_debug
* [Revision #5932a4e77d](https://github.com/MariaDB/server/commit/5932a4e77d)\
  2018-06-04 11:31:39 +0300
  * [MDEV-13834](https://jira.mariadb.org/browse/MDEV-13834): Upgrade failure from 10.1 innodb\_encrypt\_log
* [Revision #40dc1a6846](https://github.com/MariaDB/server/commit/40dc1a6846)\
  2018-05-26 16:42:13 -0700
  * Better Link Spacing
* [Revision #b2f86ebdd2](https://github.com/MariaDB/server/commit/b2f86ebdd2)\
  2018-05-31 18:55:07 -0700
  * [MDEV-16353](https://jira.mariadb.org/browse/MDEV-16353) Server crash on query with CTE
* [Revision #a31e99a89c](https://github.com/MariaDB/server/commit/a31e99a89c)\
  2018-05-30 10:48:48 +0300
  * Remove an unnecessary #include
* [Revision #6f96ff7268](https://github.com/MariaDB/server/commit/6f96ff7268)\
  2018-05-29 17:14:34 +0300
  * Allow tests to work with cmake -DPLUGIN\_PARTITION=NO
* [Revision #7269c70821](https://github.com/MariaDB/server/commit/7269c70821)\
  2018-05-29 16:52:59 +0300
  * Add an end-marker to ease future merges
* Merge [Revision #18934fb583](https://github.com/MariaDB/server/commit/18934fb583) 2018-05-29 16:36:16 +0300 - Merge 10.1 into 10.2
* [Revision #8a42ad7a5d](https://github.com/MariaDB/server/commit/8a42ad7a5d)\
  2018-05-28 14:20:44 +0300
  * [MDEV-13834](https://jira.mariadb.org/browse/MDEV-13834) 10.2 wrongly recognizes 10.1.10 innodb\_encrypt\_log=ON data as after-crash and refuses to start
* [Revision #1a8afb4885](https://github.com/MariaDB/server/commit/1a8afb4885)\
  2018-05-28 13:01:27 +0300
  * [MDEV-16310](https://jira.mariadb.org/browse/MDEV-16310): rocksdb.check\_ignore\_unknown\_options fails on OS X
* [Revision #13c241c64f](https://github.com/MariaDB/server/commit/13c241c64f)\
  2018-05-26 17:03:00 +0300
  * Fixed memory overrun in binlog\_encryption.encrypted\_master
* [Revision #2d62a4cb2f](https://github.com/MariaDB/server/commit/2d62a4cb2f)\
  2018-05-26 17:01:42 +0300
  * Updated results for galera\_encrypt\_tmp\_files
* [Revision #b8fdd56a4d](https://github.com/MariaDB/server/commit/b8fdd56a4d)\
  2018-05-24 20:11:52 +0000
  * Fix conversion warnings/errors.
* [Revision #7a4f81b4c0](https://github.com/MariaDB/server/commit/7a4f81b4c0)\
  2018-05-24 16:20:31 +0300
  * Extend debug\_assert\_on\_not\_freed\_memory
* Merge [Revision #494c981d23](https://github.com/MariaDB/server/commit/494c981d23) 2018-05-24 18:56:33 +0300 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #72a8d29e00](https://github.com/MariaDB/server/commit/72a8d29e00)\
  2018-05-23 22:45:32 +0300
  * Fixed archive to work with record\[1]
* [Revision #4cd2a0eb56](https://github.com/MariaDB/server/commit/4cd2a0eb56)\
  2018-05-23 22:42:29 +0300
  * [MDEV-15243](https://jira.mariadb.org/browse/MDEV-15243) Crash with virtual fields and row based binary logging
* [Revision #1c8c6bcd6f](https://github.com/MariaDB/server/commit/1c8c6bcd6f)\
  2018-05-24 15:30:22 +0300
  * [MDEV-13779](https://jira.mariadb.org/browse/MDEV-13779) InnoDB fails to shut down purge, causing hang
* [Revision #52df804026](https://github.com/MariaDB/server/commit/52df804026)\
  2018-05-24 11:09:59 +0300
  * [MDEV-16267](https://jira.mariadb.org/browse/MDEV-16267) Wrong INFORMATION\_SCHEMA.INNODB\_BUFFER\_PAGE.TABLE\_NAME
* [Revision #fdb8d0181e](https://github.com/MariaDB/server/commit/fdb8d0181e)\
  2018-05-23 15:24:45 +0300
  * [MDEV-16262](https://jira.mariadb.org/browse/MDEV-16262): rocksdb.issue255 test sometimes fails in buildbot
* [Revision #6e63db265f](https://github.com/MariaDB/server/commit/6e63db265f)\
  2018-05-23 00:24:28 +0300
  * Suppress warnings from partition\_open\_files\_limit
* [Revision #2dff8fecb7](https://github.com/MariaDB/server/commit/2dff8fecb7)\
  2018-05-23 00:19:15 +0300
  * [MDEV-15338](https://jira.mariadb.org/browse/MDEV-15338) Crash in debug build when dropping column that is part of CHECK
* [Revision #a107c79fcd](https://github.com/MariaDB/server/commit/a107c79fcd)\
  2018-05-22 19:36:51 +0300
  * [MDEV-12439](https://jira.mariadb.org/browse/MDEV-12439): MariaRocks produces numerous (spurious?) valgrind failures
* [Revision #afe5a51c2d](https://github.com/MariaDB/server/commit/afe5a51c2d)\
  2018-05-21 18:16:03 -0700
  * [MDEV-12900](https://jira.mariadb.org/browse/MDEV-12900): spider tests failed in buildbot with valgrind
* [Revision #31584c8bb8](https://github.com/MariaDB/server/commit/31584c8bb8)\
  2018-05-21 13:43:50 +0300
  * Set MyRocks plugin version to Stable
* [Revision #36043c58f5](https://github.com/MariaDB/server/commit/36043c58f5)\
  2018-05-20 20:26:40 +0200
  * .gitignore
* Merge [Revision #ff1d10ef9c](https://github.com/MariaDB/server/commit/ff1d10ef9c) 2018-05-20 02:07:21 +0200 - Merge branch '10.1' into 10.2
* [Revision #6f530c63cd](https://github.com/MariaDB/server/commit/6f530c63cd)\
  2018-05-19 09:06:04 +0200
  * cleanup: specify memroot explicitly in `new Explain_xxx`
* [Revision #1cc67e090e](https://github.com/MariaDB/server/commit/1cc67e090e)\
  2018-05-18 19:12:35 +0200
  * [MDEV-16153](https://jira.mariadb.org/browse/MDEV-16153) Server crashes in Apc\_target::disable, ASAN heap-use-after-free in Explain\_query::Explain\_query upon/after EXECUTE IMMEDIATE
* [Revision #207e5ba316](https://github.com/MariaDB/server/commit/207e5ba316)\
  2018-05-19 17:04:47 +0000
  * mariadb-backup : Fix race condition when killing query waiting for MDL
* [Revision #dd51082eca](https://github.com/MariaDB/server/commit/dd51082eca)\
  2018-05-19 00:26:35 +0300
  * [MDEV-12465](https://jira.mariadb.org/browse/MDEV-12465): Server crashes in my\_scan\_weight\_utf8\_bin upon collecting stats for RocksDB table
* [Revision #06aaaef51a](https://github.com/MariaDB/server/commit/06aaaef51a)\
  2018-05-18 23:58:24 +0300
  * [MDEV-16200](https://jira.mariadb.org/browse/MDEV-16200): -DPLUGIN\_ROCKSDB=YES leads to errors during build
* [Revision #727d0d4f9b](https://github.com/MariaDB/server/commit/727d0d4f9b)\
  2018-05-18 17:26:12 +0300
  * [MDEV-15304](https://jira.mariadb.org/browse/MDEV-15304): Server crash in print\_keydup\_error / key\_unpack or unexpected ER\_DUP\_KEY
* [Revision #de86997160](https://github.com/MariaDB/server/commit/de86997160)\
  2018-05-17 22:56:27 -0700
  * [MDEV-15581](https://jira.mariadb.org/browse/MDEV-15581) Incorrect result (missing row) with UNION DISTINCT in anchor parts
* [Revision #52c98bf830](https://github.com/MariaDB/server/commit/52c98bf830)\
  2018-05-18 00:35:59 -0400
  * bump the VERSION
* [Revision #d309c2fc88](https://github.com/MariaDB/server/commit/d309c2fc88)\
  2018-05-17 15:47:17 -0700
  * [MDEV-16212](https://jira.mariadb.org/browse/MDEV-16212) Memory leak with recursive CTE that uses global ORDER BY with recursive subquery
* [Revision #ab9d420df3](https://github.com/MariaDB/server/commit/ab9d420df3)\
  2018-05-17 11:21:13 -0700
  * [MDEV-7914](https://jira.mariadb.org/browse/MDEV-7914): spider/bg.ha, spider/bg.ha\_part crash server sporadically in buildbot
* Merge [Revision #50275321c3](https://github.com/MariaDB/server/commit/50275321c3) 2018-05-17 11:25:35 +0200 - Merge branch '10.2' into bb-10.2-release
* [Revision #a4e7800701](https://github.com/MariaDB/server/commit/a4e7800701)\
  2018-05-16 16:35:33 +0300
  * [MDEV-13779](https://jira.mariadb.org/browse/MDEV-13779) InnoDB fails to shut down purge workers, causing hang

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
