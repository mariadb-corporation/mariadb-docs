# MariaDB 10.4.31 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.4/10.4.31.md)[Changelog](mariadb-10-4-31-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.4.31/)

**Release date:** 14 Aug 2023

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.31.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.39](../changelogs-mariadb-10-3-series/mariadb-10-3-39-changelog.md)
* [Revision #0ede90dd31](https://github.com/MariaDB/server/commit/0ede90dd31)\
  2023-08-08 12:06:21 +0530
  * [MDEV-31869](https://jira.mariadb.org/browse/MDEV-31869) Server aborts when table does drop column
* [Revision #ab10a675ac](https://github.com/MariaDB/server/commit/ab10a675ac)\
  2023-07-31 17:36:59 +0200
  * [MDEV-31092](https://jira.mariadb.org/browse/MDEV-31092) mysqldump --force doesn't ignore error as it should
* [Revision #4dd38f9f39](https://github.com/MariaDB/server/commit/4dd38f9f39)\
  2023-07-31 20:36:19 +0200
  * [MDEV-31800](https://jira.mariadb.org/browse/MDEV-31800) Problem with open ranges on prefix blobs keys
* [Revision #4da80a41f6](https://github.com/MariaDB/server/commit/4da80a41f6)\
  2023-07-31 14:39:05 +0200
  * Fix double definition of CRYPTO\_cleanup\_all\_ex\_data
* [Revision #69b118a346](https://github.com/MariaDB/server/commit/69b118a346)\
  2023-07-31 14:42:02 +0300
  * Revert "[MDEV-30528](https://jira.mariadb.org/browse/MDEV-30528) Assertion in dtype\_get\_at\_most\_n\_mbchars"
* [Revision #f182de2ec8](https://github.com/MariaDB/server/commit/f182de2ec8)\
  2023-07-31 09:28:28 +0300
  * [MDEV-30159](https://jira.mariadb.org/browse/MDEV-30159) fixup: Plug a memory leak in the test
* [Revision #a4b9e9b95f](https://github.com/MariaDB/server/commit/a4b9e9b95f)\
  2023-07-24 13:46:18 +0200
  * Fix rpl.rpl\_rotate\_logs to work with --repeat
* [Revision #d632c85bb7](https://github.com/MariaDB/server/commit/d632c85bb7)\
  2023-07-17 15:06:50 +0200
  * [MDEV-31723](https://jira.mariadb.org/browse/MDEV-31723): Crash on SET SESSION gtid\_seq\_no= DEFAULT
* [Revision #9854fb6fa7](https://github.com/MariaDB/server/commit/9854fb6fa7)\
  2023-05-31 11:57:45 +0700
  * [MDEV-31003](https://jira.mariadb.org/browse/MDEV-31003): Second execution for ps-protocol
* [Revision #23dae6173c](https://github.com/MariaDB/server/commit/23dae6173c)\
  2019-01-24 23:30:11 -0500
  * [MDEV-18374](https://jira.mariadb.org/browse/MDEV-18374): Add SELinux policy to cracklib\_password\_check packages
* [Revision #515ba857ba](https://github.com/MariaDB/server/commit/515ba857ba)\
  2023-06-06 11:53:14 +0700
  * [MDEV-31407](https://jira.mariadb.org/browse/MDEV-31407): Add aliases in opt\_trace.test for long column name for removing "--disable-view-protocol"
* [Revision #2a46b358a7](https://github.com/MariaDB/server/commit/2a46b358a7)\
  2023-07-25 13:23:18 +0200
  * new WolfSSL v5.6.3-stable
* [Revision #063f4ac25e](https://github.com/MariaDB/server/commit/063f4ac25e)\
  2023-06-28 10:28:31 -0600
  * [MDEV-30619](https://jira.mariadb.org/browse/MDEV-30619): Parallel Slave SQL Thread Can Update Seconds\_Behind\_Master with Active Workers
* [Revision #734583b0d7](https://github.com/MariaDB/server/commit/734583b0d7)\
  2023-07-25 13:10:52 +1000
  * [MDEV-31400](https://jira.mariadb.org/browse/MDEV-31400) Simple plugin dependency resolution
* [Revision #668eb2ce45](https://github.com/MariaDB/server/commit/668eb2ce45)\
  2023-07-24 10:38:41 +0200
  * New CC 3.1
* Merge [Revision #7d968f8c8a](https://github.com/MariaDB/server/commit/7d968f8c8a) 2023-07-24 06:11:16 +0200 - Merge branch '10.4' of [server](https://github.com/MariaDB/server) into 10.4
* [Revision #1c9002cfc8](https://github.com/MariaDB/server/commit/1c9002cfc8)\
  2023-07-23 18:58:26 +0200
  * Remove CLIENT\_SSL\_VERIFY\_SERVER\_CERT
* [Revision #8b01c2962b](https://github.com/MariaDB/server/commit/8b01c2962b)\
  2023-07-23 18:58:26 +0200
  * Remove CLIENT\_SSL\_VERIFY\_SERVER\_CERT
* [Revision #73c9415e6a](https://github.com/MariaDB/server/commit/73c9415e6a)\
  2023-07-18 12:58:58 +1000
  * [MDEV-31727](https://jira.mariadb.org/browse/MDEV-31727): pcre stack size not functioning on clang-16
* [Revision #3e7561cf35](https://github.com/MariaDB/server/commit/3e7561cf35)\
  2023-07-20 14:14:00 +0300
  * [MDEV-29357](https://jira.mariadb.org/browse/MDEV-29357) Assertion (fixed) in Item\_func\_dayname on INSERT
* [Revision #14cc7e7d6e](https://github.com/MariaDB/server/commit/14cc7e7d6e)\
  2023-07-20 14:14:00 +0300
  * [MDEV-25644](https://jira.mariadb.org/browse/MDEV-25644) UPDATE not working properly on transaction precise system versioned table
* [Revision #21a8d2c313](https://github.com/MariaDB/server/commit/21a8d2c313)\
  2023-07-20 14:13:59 +0300
  * [MDEV-31319](https://jira.mariadb.org/browse/MDEV-31319) Assertion const\_item\_cache == true failed in Item\_func::fix\_fields
* [Revision #c5a8341115](https://github.com/MariaDB/server/commit/c5a8341115)\
  2023-07-20 14:13:59 +0300
  * [MDEV-23100](https://jira.mariadb.org/browse/MDEV-23100) ODKU of non-versioning column inserts history row
* [Revision #fe618de691](https://github.com/MariaDB/server/commit/fe618de691)\
  2023-07-20 14:13:59 +0300
  * [MDEV-31313](https://jira.mariadb.org/browse/MDEV-31313) SYSTEM VERSIONING and FOREIGN KEY CASCADE create orphan rows on replica
* [Revision #add0c01bae](https://github.com/MariaDB/server/commit/add0c01bae)\
  2023-07-20 14:13:59 +0300
  * [MDEV-30528](https://jira.mariadb.org/browse/MDEV-30528) Assertion in dtype\_get\_at\_most\_n\_mbchars
* [Revision #2ba5c387c1](https://github.com/MariaDB/server/commit/2ba5c387c1)\
  2023-07-10 13:57:07 -0700
  * Avoid triggering stringop-truncation warning in safe\_strcpy
* [Revision #daeccfcf2b](https://github.com/MariaDB/server/commit/daeccfcf2b)\
  2023-05-23 10:02:33 +0300
  * Optimized version of safe\_strcpy()
* [Revision #620aeb44db](https://github.com/MariaDB/server/commit/620aeb44db)\
  2023-07-14 14:51:09 +0200
  * [MDEV-30159](https://jira.mariadb.org/browse/MDEV-30159): Client can crash the server with a mysql\_list\_fields("view") call
* [Revision #5a44700aaa](https://github.com/MariaDB/server/commit/5a44700aaa)\
  2023-07-05 13:01:43 +1000
  * [MDEV-31625](https://jira.mariadb.org/browse/MDEV-31625) connect engine file\_type=DBF insert fails
* [Revision #cf50379b91](https://github.com/MariaDB/server/commit/cf50379b91)\
  2023-06-27 12:10:48 +0200
  * [MDEV-25237](https://jira.mariadb.org/browse/MDEV-25237) crash after setting global session\_track\_system\_variables to an invalid value
* [Revision #03c2157dd6](https://github.com/MariaDB/server/commit/03c2157dd6)\
  2023-07-20 11:56:19 +0400
  * [MDEV-28384](https://jira.mariadb.org/browse/MDEV-28384) UBSAN: null pointer passed as argument 1, which is declared to never be null in my\_strnncoll\_binary on SELECT ... COUNT or GROUP\_CONCAT
* [Revision #a79f4f6ec9](https://github.com/MariaDB/server/commit/a79f4f6ec9)\
  2023-07-20 11:06:30 +0400
  * [MDEV-22856](https://jira.mariadb.org/browse/MDEV-22856) Assertion `!str || str != Ptr' and Assertion` !str || str != Ptr || !is\_alloced()' failed in String::copy
* [Revision #d067de20d6](https://github.com/MariaDB/server/commit/d067de20d6)\
  2023-07-20 13:33:14 +1000
  * [MDEV-23133](https://jira.mariadb.org/browse/MDEV-23133) session tracker - warning message typo
* [Revision #30f3db3cf1](https://github.com/MariaDB/server/commit/30f3db3cf1)\
  2023-07-19 10:33:20 +0400
  * [MDEV-29019](https://jira.mariadb.org/browse/MDEV-29019) Assertion \`(length % 4) == 0' failed in my\_lengthsp\_utf32 on SELECT
* [Revision #9e5c1fb5d3](https://github.com/MariaDB/server/commit/9e5c1fb5d3)\
  2023-07-19 06:13:44 +0400
  * [MDEV-23838](https://jira.mariadb.org/browse/MDEV-23838) Possibly wrong result or Assertion \`0' failed in Item\_func\_round::native\_op
* [Revision #fbc157ab33](https://github.com/MariaDB/server/commit/fbc157ab33)\
  2023-07-18 11:59:42 +1000
  * [MDEV-31545](https://jira.mariadb.org/browse/MDEV-31545) GCC 13 -Wdangling-pointer in execute\_show\_status()
* [Revision #4b3f930639](https://github.com/MariaDB/server/commit/4b3f930639)\
  2023-07-10 11:40:00 +1000
  * [MDEV-31336](https://jira.mariadb.org/browse/MDEV-31336): pam\_user\_map : not supporting username or groupname containing @ character
* [Revision #b884216be7](https://github.com/MariaDB/server/commit/b884216be7)\
  2023-07-14 10:13:17 +0200
  * [MDEV-28017](https://jira.mariadb.org/browse/MDEV-28017) Illegal mix of collations (cp1251\_general\_ci,IMPLICIT), (latin1\_swedish\_ci,COERCIBLE), (latin1\_swedish\_ci,COERCIBLE) for operation 'between'
* [Revision #e1d31a10af](https://github.com/MariaDB/server/commit/e1d31a10af)\
  2023-07-13 13:22:24 +1000
  * [MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524) Fixing spider table param / variable overriding
* [Revision #7dde504aef](https://github.com/MariaDB/server/commit/7dde504aef)\
  2023-07-05 19:01:13 +0300
  * q

## This is a combination of 2 commits.

* [Revision #3f5cee8f54](https://github.com/MariaDB/server/commit/3f5cee8f54)\
  2023-06-21 21:45:29 +0200
  * Fix one case that should not be marked transactional in the GTID event
* [Revision #08585b0949](https://github.com/MariaDB/server/commit/08585b0949)\
  2023-06-20 23:23:26 +0200
  * [MDEV-31509](https://jira.mariadb.org/browse/MDEV-31509): Lost data with FTWRL and STOP SLAVE
* [Revision #d4309d4830](https://github.com/MariaDB/server/commit/d4309d4830)\
  2023-06-15 21:46:01 +0200
  * [MDEV-31448](https://jira.mariadb.org/browse/MDEV-31448): Killing a replica thread awaiting its GCO can hang/crash a parallel replica
* [Revision #5d61442c85](https://github.com/MariaDB/server/commit/5d61442c85)\
  2023-06-15 21:35:53 +0200
  * [MDEV-31448](https://jira.mariadb.org/browse/MDEV-31448): Killing a replica thread awaiting its GCO can hang/crash a parallel replica
* [Revision #a8ea6627a4](https://github.com/MariaDB/server/commit/a8ea6627a4)\
  2023-06-11 17:44:58 +0200
  * [MDEV-31448](https://jira.mariadb.org/browse/MDEV-31448): Killing a replica thread awaiting its GCO can hang/crash a parallel replica
* [Revision #60bec1d54d](https://github.com/MariaDB/server/commit/60bec1d54d)\
  2023-06-10 22:36:16 +0200
  * [MDEV-13915](https://jira.mariadb.org/browse/MDEV-13915): STOP SLAVE takes very long time on a busy system
* [Revision #b4646c675c](https://github.com/MariaDB/server/commit/b4646c675c)\
  2023-06-16 15:33:51 +0200
  * Misc. small cleanups unrelated to any particular MDEV
* [Revision #23d53913fb](https://github.com/MariaDB/server/commit/23d53913fb)\
  2023-06-15 15:18:40 +1000
  * [MDEV-27038](https://jira.mariadb.org/browse/MDEV-27038) Custom configuration file procedure does not work with Docker Desktop for Windows 10+
* [Revision #7a5c984fa3](https://github.com/MariaDB/server/commit/7a5c984fa3)\
  2023-07-10 18:43:56 +0300
  * [MDEV-20010](https://jira.mariadb.org/browse/MDEV-20010) Equal on two RANK window functions create wrong result
* [Revision #12a5fb4b36](https://github.com/MariaDB/server/commit/12a5fb4b36)\
  2023-07-10 13:46:34 +0300
  * [MDEV-31641](https://jira.mariadb.org/browse/MDEV-31641) innochecksum dies with Floating point exception
* [Revision #02cd3675c4](https://github.com/MariaDB/server/commit/02cd3675c4)\
  2023-05-22 15:07:05 +0200
  * [MDEV-31064](https://jira.mariadb.org/browse/MDEV-31064) Changes in a SP are not immediately seen in I\_S.parameters
* [Revision #8fb863e6a4](https://github.com/MariaDB/server/commit/8fb863e6a4)\
  2023-07-07 10:33:47 +0200
  * [MDEV-24712](https://jira.mariadb.org/browse/MDEV-24712) get\_partition\_set is never executed in ha\_partition::multi\_range\_key\_create\_key due to bitwise & with 0 constant
* [Revision #94a8921e9d](https://github.com/MariaDB/server/commit/94a8921e9d)\
  2023-07-05 19:28:27 +0700
  * [MDEV-29284](https://jira.mariadb.org/browse/MDEV-29284) ANALYZE doesn't work with pushed derived tables
* [Revision #1bfd3cc457](https://github.com/MariaDB/server/commit/1bfd3cc457)\
  2023-07-03 16:04:15 +0300
  * [MDEV-10962](https://jira.mariadb.org/browse/MDEV-10962) Deadlock with 3 concurrent DELETEs by unique key
* [Revision #19cdddf17d](https://github.com/MariaDB/server/commit/19cdddf17d)\
  2023-07-06 13:49:06 +0400
  * A cleanup for [MDEV-30932](https://jira.mariadb.org/browse/MDEV-30932) UBSAN: negation of -X cannot be represented in type ..
* [Revision #23e252aef2](https://github.com/MariaDB/server/commit/23e252aef2)\
  2023-07-05 16:35:01 +0530
  * [MDEV-23187](https://jira.mariadb.org/browse/MDEV-23187) misses resetting collation connection
* [Revision #9856bb4245](https://github.com/MariaDB/server/commit/9856bb4245)\
  2023-07-02 21:16:03 +0200
  * [MDEV-31602](https://jira.mariadb.org/browse/MDEV-31602): Race on rpl\_global\_gtid\_slave\_state when starting IO thread
* [Revision #922db0642b](https://github.com/MariaDB/server/commit/922db0642b)\
  2023-06-28 14:25:53 +1000
  * [MDEV-31421](https://jira.mariadb.org/browse/MDEV-31421) Fix spider test cleanup
* [Revision #ea386c9d06](https://github.com/MariaDB/server/commit/ea386c9d06)\
  2023-06-05 11:00:44 +0300
  * Fix use of uninitialized variable
* [Revision #5c81c50f10](https://github.com/MariaDB/server/commit/5c81c50f10)\
  2023-06-30 21:03:29 +0200
  * [MDEV-31214](https://jira.mariadb.org/browse/MDEV-31214) Recursive CTE execution is interrupted without errors or warnings
* [Revision #22e5a5ff6e](https://github.com/MariaDB/server/commit/22e5a5ff6e)\
  2023-06-30 20:51:17 +0200
  * generalize ER\_QUERY\_EXCEEDED\_ROWS\_EXAMINED\_LIMIT
* [Revision #d458136e7d](https://github.com/MariaDB/server/commit/d458136e7d)\
  2023-06-30 19:22:21 +0200
  * cleanup: ER\_QUERY\_TIMEOUT -> ER\_UNUSED\_1
* [Revision #b8088487e4](https://github.com/MariaDB/server/commit/b8088487e4)\
  2023-07-03 16:09:18 +0300
  * [MDEV-19216](https://jira.mariadb.org/browse/MDEV-19216) Assertion ...SYS\_FOREIGN failed in btr\_node\_ptr\_max\_size
* [Revision #0105220e3b](https://github.com/MariaDB/server/commit/0105220e3b)\
  2023-07-03 16:06:10 +0300
  * Remove tests that duplicate innodb.max\_record\_size
* [Revision #77a229cd2d](https://github.com/MariaDB/server/commit/77a229cd2d)\
  2023-05-30 16:08:41 +0200
  * [MDEV-31358](https://jira.mariadb.org/browse/MDEV-31358): Update description for MariaDB debian/rpm packages
* [Revision #e146940ab3](https://github.com/MariaDB/server/commit/e146940ab3)\
  2023-06-30 01:28:29 +0200
  * [MDEV-31480](https://jira.mariadb.org/browse/MDEV-31480) RPM packages fail to install because they require /bin/sh for %pretrans
* [Revision #67657a01bf](https://github.com/MariaDB/server/commit/67657a01bf)\
  2023-06-28 16:47:27 +0400
  * [MDEV-30932](https://jira.mariadb.org/browse/MDEV-30932) UBSAN: negation of -X cannot be represented in type .. 'long long int'; cast to an unsigned type to negate this value .. to itself in Item\_func\_mul::int\_op and Item\_func\_round::int\_op
* [Revision #428c7964a2](https://github.com/MariaDB/server/commit/428c7964a2)\
  2023-06-29 11:22:13 +1000
  * [MDEV-30370](https://jira.mariadb.org/browse/MDEV-30370) \[fixup] Spider: mdev\_30370.test needs wsrep to run.
* [Revision #ea4b8d4ce9](https://github.com/MariaDB/server/commit/ea4b8d4ce9)\
  2023-06-28 14:41:24 +1000
  * [MDEV-31101](https://jira.mariadb.org/browse/MDEV-31101) Spider: temporarily disable mdev\_29904.test
* [Revision #d214628af4](https://github.com/MariaDB/server/commit/d214628af4)\
  2023-05-07 11:33:07 +0200
  * mtr: fix the help text for debuggers
* [Revision #5f09b53bdb](https://github.com/MariaDB/server/commit/5f09b53bdb)\
  2023-06-05 19:09:38 +0530
  * [MDEV-31086](https://jira.mariadb.org/browse/MDEV-31086) MODIFY COLUMN can break FK constraints, and lead to unrestorable dumps
* [Revision #423c28f0aa](https://github.com/MariaDB/server/commit/423c28f0aa)\
  2023-01-03 16:24:04 +1100
  * [MDEV-29447](https://jira.mariadb.org/browse/MDEV-29447) [MDEV-26285](https://jira.mariadb.org/browse/MDEV-26285) [MDEV-31338](https://jira.mariadb.org/browse/MDEV-31338) Refactor spider\_db\_mbase\_util::open\_item\_func
* [Revision #b37357eb46](https://github.com/MariaDB/server/commit/b37357eb46)\
  2023-06-26 11:03:15 +0300
  * Fix GCC 13 -Wmaybe-uninitialized
* [Revision #9c0e91a27c](https://github.com/MariaDB/server/commit/9c0e91a27c)\
  2023-06-22 15:26:23 +0200
  * Adjust OpenSSL context sizes for CiscoSSL
* [Revision #1f72450260](https://github.com/MariaDB/server/commit/1f72450260)\
  2023-06-22 15:24:09 +0200
  * Revert "[MDEV-23925](https://jira.mariadb.org/browse/MDEV-23925): Fixed warnings generated during compilation of mysys\_ssl/openssl.c on MacOS"
* [Revision #d32fc5b8e0](https://github.com/MariaDB/server/commit/d32fc5b8e0)\
  2023-06-12 22:16:49 +0200
  * [MDEV-31461](https://jira.mariadb.org/browse/MDEV-31461) mariadb SIGSEGV when built with -DCLIENT\_PLUGIN\_DIALOG=STATIC
* [Revision #f5dceafd0b](https://github.com/MariaDB/server/commit/f5dceafd0b)\
  2023-03-29 19:42:21 +0300
  * [MDEV-30964](https://jira.mariadb.org/browse/MDEV-30964): MAX\_SEL\_ARG memory exhaustion is not visible in the optimizer trace
* [Revision #2165c30486](https://github.com/MariaDB/server/commit/2165c30486)\
  2023-06-08 11:35:21 +0300
  * Fix testcase for [MDEV-31240](https://jira.mariadb.org/browse/MDEV-31240) to work with --view-protocol.
* Merge [Revision #78b1831c9f](https://github.com/MariaDB/server/commit/78b1831c9f) 2023-06-07 15:08:29 +0200 - Merge branch '10.4' into 10.4.30
* [Revision #78a1f3ce81](https://github.com/MariaDB/server/commit/78a1f3ce81)\
  2023-06-07 08:09:02 -0400
  * bump the VERSION
* [Revision #7e17a88e75](https://github.com/MariaDB/server/commit/7e17a88e75)\
  2023-05-25 12:52:38 +1000
  * [MDEV-30435](https://jira.mariadb.org/browse/MDEV-30435) [MDEV-30981](https://jira.mariadb.org/browse/MDEV-30981) Fix ubsan errors w.r.t. memcpy in spd\_trx.cc
* [Revision #8ed88e3455](https://github.com/MariaDB/server/commit/8ed88e3455)\
  2023-06-06 08:11:38 -0600
  * Revert "[MDEV-13915](https://jira.mariadb.org/browse/MDEV-13915): STOP SLAVE takes very long time on a busy system"
* [Revision #677d6f0f23](https://github.com/MariaDB/server/commit/677d6f0f23)\
  2023-06-01 16:44:35 +0200
  * [MDEV-31183](https://jira.mariadb.org/browse/MDEV-31183) binlog\_encryption.encrypted\_master\_switch\_to\_unencrypted\_gtid fails in BB with UBSAN runtime error: downcast of address
* [Revision #0a99d457b3](https://github.com/MariaDB/server/commit/0a99d457b3)\
  2023-03-08 13:49:32 -0700
  * [MDEV-13915](https://jira.mariadb.org/browse/MDEV-13915): STOP SLAVE takes very long time on a busy system
* [Revision #8de6740a2f](https://github.com/MariaDB/server/commit/8de6740a2f)\
  2023-06-04 19:04:49 +0800
  * [MDEV-31205](https://jira.mariadb.org/browse/MDEV-31205) Typo: complatible > compatible
* [Revision #c05ecda61f](https://github.com/MariaDB/server/commit/c05ecda61f)\
  2023-06-01 22:15:41 +0200
  * fix string literal escaping in views
* [Revision #69684f689c](https://github.com/MariaDB/server/commit/69684f689c)\
  2023-06-01 18:31:08 +0200
  * use correct collation\_connection in --view
* [Revision #c0463704c2](https://github.com/MariaDB/server/commit/c0463704c2)\
  2023-06-01 17:28:41 +0200
  * fix the test for --view
* [Revision #aca641da28](https://github.com/MariaDB/server/commit/aca641da28)\
  2023-05-31 14:40:17 +0200
  * mtr: handle the case of existing but unreadable /proc/cpuinfo
* [Revision #d14c485e1c](https://github.com/MariaDB/server/commit/d14c485e1c)\
  2023-06-02 12:49:17 +0200
  * test fixes for 32bit
* [Revision #d785fa8d0b](https://github.com/MariaDB/server/commit/d785fa8d0b)\
  2023-06-02 12:12:00 +0200
  * cmake warnings
* [Revision #270c233847](https://github.com/MariaDB/server/commit/270c233847)\
  2023-06-02 10:46:02 +0200
  * clarify why cmake is looking for Java and JNI
* [Revision #dc9498beb6](https://github.com/MariaDB/server/commit/dc9498beb6)\
  2023-06-02 09:02:09 +0200
  * Revert "[MDEV-31230](https://jira.mariadb.org/browse/MDEV-31230): Fix CONNECT\_JDBC in CMake"
* [Revision #bd1eb89d7f](https://github.com/MariaDB/server/commit/bd1eb89d7f)\
  2023-06-02 10:52:28 +1000
  * Adding .ccls-cache/ to .gitignore
* [Revision #2771890bab](https://github.com/MariaDB/server/commit/2771890bab)\
  2023-05-18 12:08:40 +1000
  * [MDEV-31301](https://jira.mariadb.org/browse/MDEV-31301) sql/opt\_split.cc:1043:5: warning: ‘best\_param\_tables’ may be used uninitialized
* [Revision #94e5b43ff5](https://github.com/MariaDB/server/commit/94e5b43ff5)\
  2023-05-25 15:26:46 +0300
  * [MDEV-31335](https://jira.mariadb.org/browse/MDEV-31335) : Create sequence can cause inconsistency
* [Revision #1d0e3d80d8](https://github.com/MariaDB/server/commit/1d0e3d80d8)\
  2023-05-09 15:39:15 +0200
  * [MDEV-31230](https://jira.mariadb.org/browse/MDEV-31230): Fix CONNECT\_JDBC in CMake
* [Revision #d657f18ea7](https://github.com/MariaDB/server/commit/d657f18ea7)\
  2023-05-27 16:31:22 +0300
  * [MDEV-31226](https://jira.mariadb.org/browse/MDEV-31226) Server crash or assertion failure with row size close to join\_buffer\_size
* [Revision #832b157bbe](https://github.com/MariaDB/server/commit/832b157bbe)\
  2023-05-25 23:10:53 +0000
  * [MDEV-30214](https://jira.mariadb.org/browse/MDEV-30214): Generalize log filename in IO Error message
* [Revision #d1b1f8c9f2](https://github.com/MariaDB/server/commit/d1b1f8c9f2)\
  2023-05-24 15:32:53 +0300
  * Updated some test result for 32 bit systems
* [Revision #9f909e546e](https://github.com/MariaDB/server/commit/9f909e546e)\
  2023-05-02 12:42:13 +0300
  * [MDEV-30197](https://jira.mariadb.org/browse/MDEV-30197) : Missing DBUG\_RETURN or DBUG\_VOID\_RETURN macro in function "Wsrep\_schema::restore\_view()"
* [Revision #1ac00c5e9f](https://github.com/MariaDB/server/commit/1ac00c5e9f)\
  2023-03-15 15:27:23 +0100
  * [MDEV-30855](https://jira.mariadb.org/browse/MDEV-30855) Remove test galera.galera\_bf\_abort\_group\_commit
* [Revision #6966d7fe4b](https://github.com/MariaDB/server/commit/6966d7fe4b)\
  2023-04-17 16:04:01 +0300
  * [MDEV-29293](https://jira.mariadb.org/browse/MDEV-29293) MariaDB stuck on starting commit state
* [Revision #60f0765b58](https://github.com/MariaDB/server/commit/60f0765b58)\
  2023-01-29 19:39:14 +0700
  * [MDEV-30143](https://jira.mariadb.org/browse/MDEV-30143) Segfault on select query using index for group-by and filesort
* [Revision #131ef14a6e](https://github.com/MariaDB/server/commit/131ef14a6e)\
  2023-05-10 20:08:33 +0300
  * Fix ./mtr --view-protocol opt\_trace
* [Revision #b54e7b0cea](https://github.com/MariaDB/server/commit/b54e7b0cea)\
  2023-05-12 12:11:53 +0300
  * [MDEV-31185](https://jira.mariadb.org/browse/MDEV-31185) rw\_trx\_hash\_t::find() unpins pins too early
* [Revision #f4ce1e487e](https://github.com/MariaDB/server/commit/f4ce1e487e)\
  2023-03-18 00:19:08 +0000
  * All-green GitLab CI in 10.4 branch
* [Revision #1db4fc543b](https://github.com/MariaDB/server/commit/1db4fc543b)\
  2022-08-30 04:21:40 -0400
  * Ensure that source files contain only valid UTF8 encodings (#2188)
* [Revision #c205f6c127](https://github.com/MariaDB/server/commit/c205f6c127)\
  2022-09-02 05:40:33 -0400
  * Remove unused French translations in Connect engine (#2252)
* [Revision #956d6c4af9](https://github.com/MariaDB/server/commit/956d6c4af9)\
  2023-04-20 13:26:09 +0300
  * [MDEV-21479](https://jira.mariadb.org/browse/MDEV-21479) : Galera 4 unable to query cluster state if not primary component
* [Revision #ffd5d74c4f](https://github.com/MariaDB/server/commit/ffd5d74c4f)\
  2023-05-11 07:46:57 +0300
  * [MDEV-30013](https://jira.mariadb.org/browse/MDEV-30013) : Assertion \`state() == s\_aborting || state() == s\_must\_replay' failed in int wsrep::transaction::after\_rollback()
* [Revision #b7b8a9ee43](https://github.com/MariaDB/server/commit/b7b8a9ee43)\
  2023-04-13 16:43:30 +0530
  * [MDEV-23187](https://jira.mariadb.org/browse/MDEV-23187): Assorted assertion failures in json\_find\_path with certain collations
* [Revision #996b040f93](https://github.com/MariaDB/server/commit/996b040f93)\
  2023-05-12 22:30:47 +0000
  * [MDEV-30232](https://jira.mariadb.org/browse/MDEV-30232): Increase timeouts to fix sporadic fails
* [Revision #8810b1ecf1](https://github.com/MariaDB/server/commit/8810b1ecf1)\
  2023-05-13 17:09:57 +0100
  * Fix Connect compile issue
* [Revision #2ff01e763e](https://github.com/MariaDB/server/commit/2ff01e763e)\
  2023-03-10 14:41:11 -0800
  * Fix insecure use of strcpy, strcat and sprintf in Connect
* [Revision #b3cdb61249](https://github.com/MariaDB/server/commit/b3cdb61249)\
  2023-05-12 11:51:58 +0400
  * [MDEV-31250](https://jira.mariadb.org/browse/MDEV-31250) ROW variables do not get assigned from subselects
* [Revision #0474466bc2](https://github.com/MariaDB/server/commit/0474466bc2)\
  2023-05-11 23:34:41 -0700
  * [MDEV-31240](https://jira.mariadb.org/browse/MDEV-31240) Crash with condition pushable into derived and containing outer reference
* [Revision #f102b595e8](https://github.com/MariaDB/server/commit/f102b595e8)\
  2023-05-03 08:29:38 +0300
  * [MDEV-28433](https://jira.mariadb.org/browse/MDEV-28433) : Server crashes when wsrep\_sst\_donor and wsrep\_cluster\_address set to NULL
* [Revision #7d55eb00f3](https://github.com/MariaDB/server/commit/7d55eb00f3)\
  2023-03-16 09:29:10 +0100
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) Remove test galera.[MDEV-27713](https://jira.mariadb.org/browse/MDEV-27713)
* [Revision #3a7b311350](https://github.com/MariaDB/server/commit/3a7b311350)\
  2023-05-12 02:46:42 +0200
  * [MDEV-30388](https://jira.mariadb.org/browse/MDEV-30388) correction: fix compilation error
* [Revision #28eaf66e18](https://github.com/MariaDB/server/commit/28eaf66e18)\
  2023-05-10 08:42:37 +0300
  * [MDEV-30388](https://jira.mariadb.org/browse/MDEV-30388) : Assertion \`!wsrep\_has\_changes(thd) || (thd->lex->sql\_command == SQLCOM\_CREATE\_TABLE && !thd->is\_current\_stmt\_binlog\_format\_row()) || thd->wsrep\_cs().transaction().state() == wsrep::transaction::s\_aborted' failed
* Merge [Revision #de703a2b21](https://github.com/MariaDB/server/commit/de703a2b21) 2023-05-11 09:07:45 +0200 - Merge branch '10.4' into 10.4.29 release
* [Revision #7e7e12e747](https://github.com/MariaDB/server/commit/7e7e12e747)\
  2023-04-24 18:38:42 +0700
  * [MDEV-30765](https://jira.mariadb.org/browse/MDEV-30765) SHOW TABLES not working properly with lower\_case\_table\_names=2
* [Revision #8c6e314ba9](https://github.com/MariaDB/server/commit/8c6e314ba9)\
  2023-05-10 08:11:15 -0400
  * bump the VERSION
* [Revision #6544d88ff5](https://github.com/MariaDB/server/commit/6544d88ff5)\
  2023-05-09 21:20:10 -0700
  * [MDEV-31224](https://jira.mariadb.org/browse/MDEV-31224) Crash with EXPLAIN EXTENDED for multi-table update of system table
* [Revision #a09f661f43](https://github.com/MariaDB/server/commit/a09f661f43)\
  2023-05-08 11:42:24 -0700
  * [MDEV-31181](https://jira.mariadb.org/browse/MDEV-31181) Crash with EXPLAIN EXTENDED for single-table DELETE using IN predicand
* [Revision #84b9fc25a2](https://github.com/MariaDB/server/commit/84b9fc25a2)\
  2023-05-05 11:31:35 +0300
  * Fixed wrong test cases (embedded and ASAN)
* [Revision #c874d5c68d](https://github.com/MariaDB/server/commit/c874d5c68d)\
  2023-05-04 19:13:30 +0300
  * Added missing test file
* [Revision #e74390d94f](https://github.com/MariaDB/server/commit/e74390d94f)\
  2023-05-04 13:06:39 +0300
  * Cleanup of sql\_join\_cache code (no logic changes)
* [Revision #5fd46be5a7](https://github.com/MariaDB/server/commit/5fd46be5a7)\
  2023-05-04 12:43:18 +0300
  * Fixed calculation of JOIN\_CACHE::max\_records
* [Revision #08a4732860](https://github.com/MariaDB/server/commit/08a4732860)\
  2023-05-03 21:27:30 +0300
  * [MDEV-28217](https://jira.mariadb.org/browse/MDEV-28217) Incorrect Join Execution When Controlling Join Buffer Size
* [Revision #01ea779149](https://github.com/MariaDB/server/commit/01ea779149)\
  2023-04-28 14:41:27 +0400
  * [MDEV-31174](https://jira.mariadb.org/browse/MDEV-31174) New class Native\_functions\_hash
* [Revision #9b6f87b62a](https://github.com/MariaDB/server/commit/9b6f87b62a)\
  2023-05-03 01:34:32 +0200
  * [MDEV-30892](https://jira.mariadb.org/browse/MDEV-30892) test galera.galera\_log\_bin is not deterministic
* [Revision #7f96dd50e2](https://github.com/MariaDB/server/commit/7f96dd50e2)\
  2023-05-02 22:30:57 +0300
  * [MDEV-6768](https://jira.mariadb.org/browse/MDEV-6768) Wrong result with aggregate with join with no result set
* [Revision #4f7317579e](https://github.com/MariaDB/server/commit/4f7317579e)\
  2023-04-29 20:39:50 +0300
  * Fixed "Trying to lock uninitialized mutex' in parallel replication
* [Revision #4cb0d43ac6](https://github.com/MariaDB/server/commit/4cb0d43ac6)\
  2023-03-17 12:02:04 +0200
  * [MDEV-28054](https://jira.mariadb.org/browse/MDEV-28054) Various crashes upon INSERT/UPDATE after changing Aria settings
* [Revision #1ef22e28ad](https://github.com/MariaDB/server/commit/1ef22e28ad)\
  2023-03-16 17:24:12 +0200
  * [MDEV-26258](https://jira.mariadb.org/browse/MDEV-26258) Various crashes/asserts/corruptions when Aria encryption is enabled/used, but the encryption plugin is not loaded

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
