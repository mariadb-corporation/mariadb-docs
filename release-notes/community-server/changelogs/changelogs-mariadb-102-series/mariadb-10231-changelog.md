# MariaDB 10.2.31 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.31/)[Release Notes](../../old-releases/10.2/10.2.31.md)[Changelog](mariadb-10231-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 28 Jan 2020

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.31.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.44](../changelogs-mariadb-101-series/mariadb-10144-changelog.md)
* [Revision #0a891ad6a6](https://github.com/MariaDB/server/commit/0a891ad6a6)\
  2020-01-26 18:40:22 +0200
  * List of unstable tests for 10.2.31 release
* Merge [Revision #f2ccfcaca1](https://github.com/MariaDB/server/commit/f2ccfcaca1) 2020-01-24 13:46:49 +0100 - Merge branch '10.1' into 10.2
* [Revision #ac3e3e12ad](https://github.com/MariaDB/server/commit/ac3e3e12ad)\
  2020-01-24 14:43:19 +0200
  * [MDEV-21509](https://jira.mariadb.org/browse/MDEV-21509): Work around occasional lost DEBUG\_SYNC
* [Revision #26a46444b4](https://github.com/MariaDB/server/commit/26a46444b4)\
  2020-01-23 23:26:01 +0100
  * don't run main.ssl\_system\_ca in --embedded
* [Revision #683a49889c](https://github.com/MariaDB/server/commit/683a49889c)\
  2020-01-24 00:29:06 +0400
  * MENT-464 ASAN MTR quick test - some failures to be investigated.
* [Revision #7aa443ca7d](https://github.com/MariaDB/server/commit/7aa443ca7d)\
  2020-01-23 16:29:52 +0200
  * Remove an unused tokuvalgrind script
* [Revision #1d12bff42c](https://github.com/MariaDB/server/commit/1d12bff42c)\
  2020-01-23 16:14:28 +0200
  * [MDEV-20775](https://jira.mariadb.org/browse/MDEV-20775): page\_zip\_validate() failure due to AUTO\_INCREMENT
* [Revision #7c166e68aa](https://github.com/MariaDB/server/commit/7c166e68aa)\
  2020-01-22 21:13:14 +0300
  * [MDEV-14183](https://jira.mariadb.org/browse/MDEV-14183): aria\_pack segfaults in compress\_maria\_file
* [Revision #1f9a0437da](https://github.com/MariaDB/server/commit/1f9a0437da)\
  2020-01-22 18:18:22 +0100
  * new C/C and --ssl-verify-server-cert tests
* [Revision #8eec2d61fc](https://github.com/MariaDB/server/commit/8eec2d61fc)\
  2020-01-21 15:17:43 +0100
  * [MDEV-21249](https://jira.mariadb.org/browse/MDEV-21249) [MariaDB 10.3.10](../../old-releases/10.3/10.3.10.md) When referring to bigint to generate timestamp data in the virtual generated column, the value of the generated column does not change when the time zone changes
* [Revision #4e7f3fb833](https://github.com/MariaDB/server/commit/4e7f3fb833)\
  2020-01-20 22:56:01 +0300
  * [MDEV-14183](https://jira.mariadb.org/browse/MDEV-14183): aria\_pack segfaults in compress\_maria\_file
* [Revision #90e7e6783b](https://github.com/MariaDB/server/commit/90e7e6783b)\
  2020-01-20 13:56:43 +0100
  * [MDEV-21360](https://jira.mariadb.org/browse/MDEV-21360) save/restore debud\_dbug instead of total reset at the end of the test
* [Revision #10a5e1eccb](https://github.com/MariaDB/server/commit/10a5e1eccb)\
  2020-01-16 23:37:15 +0100
  * [MDEV-21360](https://jira.mariadb.org/browse/MDEV-21360) save/restore debud\_dbug instead of total reset at the end of the test
* [Revision #8870f18e1d](https://github.com/MariaDB/server/commit/8870f18e1d)\
  2020-01-20 15:10:39 +0100
  * [MDEV-17292](https://jira.mariadb.org/browse/MDEV-17292) Package the pam\_user\_map module
* [Revision #42049f9d39](https://github.com/MariaDB/server/commit/42049f9d39)\
  2020-01-20 14:30:13 +0100
  * cleanup: simplify install\_layout.cmake
* [Revision #a5b38151c0](https://github.com/MariaDB/server/commit/a5b38151c0)\
  2020-01-20 18:05:48 +0100
  * new version CC 3.1
* Merge [Revision #3a1716a7e7](https://github.com/MariaDB/server/commit/3a1716a7e7) 2020-01-20 16:15:05 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #d07664498b](https://github.com/MariaDB/server/commit/d07664498b) 2020-01-20 16:10:30 +0100 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #8ff3eb417c](https://github.com/MariaDB/server/commit/8ff3eb417c)\
  2020-01-12 19:59:07 +0100
  * Fix [MDEV-21450](https://jira.mariadb.org/browse/MDEV-21450) Failed compile when XML table type is not supported. Was because XMLDEF was unconditionally called from REST table.
* [Revision #b1c8bf464b](https://github.com/MariaDB/server/commit/b1c8bf464b)\
  2019-12-10 16:46:32 +0100
  * Make LIKE\_FUNC only for version >= 10.2 in ha\_connect.cc
* [Revision #4692094de7](https://github.com/MariaDB/server/commit/4692094de7)\
  2019-12-04 15:20:04 +0100
  * Fix reldef.cpp (wrong flag for catalog columns)
* [Revision #817675459a](https://github.com/MariaDB/server/commit/817675459a)\
  2019-12-03 19:20:26 +0100
  * Fix tabrest.cpp when used for OEM
* [Revision #579d572d25](https://github.com/MariaDB/server/commit/579d572d25)\
  2019-12-03 18:06:05 +0100
  * Make restGetFile extern C
* [Revision #64b1b959f1](https://github.com/MariaDB/server/commit/64b1b959f1)\
  2019-12-01 01:16:23 +0100
  * comment out \<dlfnc.h> in tabrest.cppc
* [Revision #65310f5855](https://github.com/MariaDB/server/commit/65310f5855)\
  2019-12-01 00:14:24 +0100
  * \<dlfnc.h> in tabrest.cpp and redef.cpp
* [Revision #1f7f533144](https://github.com/MariaDB/server/commit/1f7f533144)\
  2019-11-30 19:03:29 +0100
  * Add include \<dlfnc.h> in tabrest.cpp
* [Revision #90d39f2f91](https://github.com/MariaDB/server/commit/90d39f2f91)\
  2020-01-20 13:46:44 +0200
  * [MDEV-21532](https://jira.mariadb.org/browse/MDEV-21532) : galera.galera\_rsu\_drop\_pk MTR failed: Result content mismatch
* [Revision #ceffabc421](https://github.com/MariaDB/server/commit/ceffabc421)\
  2020-01-20 08:40:32 +0200
  * Enable tests for --embedded
* [Revision #e47b780286](https://github.com/MariaDB/server/commit/e47b780286)\
  2020-01-20 08:38:55 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Work around DEBUG\_SYNC timeouts
* [Revision #d595a91bc6](https://github.com/MariaDB/server/commit/d595a91bc6)\
  2020-01-17 18:39:00 +0300
  * Fix a merge typo
* Merge [Revision #7b70cbd838](https://github.com/MariaDB/server/commit/7b70cbd838) 2020-01-17 16:24:40 +0200 - [MDEV-21499](https://jira.mariadb.org/browse/MDEV-21499) Merge new release of InnoDB 5.7.29 to 10.2
* [Revision #c25a0662b3](https://github.com/MariaDB/server/commit/c25a0662b3)\
  2019-11-08 09:24:38 +0100
  * Bug #30499288 - GCC 9.2.1 REPORTS A NEW WARNING FOR OS\_FILE\_GET\_PARENT\_DIR
* [Revision #08b0b2b6fb](https://github.com/MariaDB/server/commit/08b0b2b6fb)\
  2020-01-17 16:22:13 +0200
  * [MDEV-21513](https://jira.mariadb.org/browse/MDEV-21513): Avoid some crashes in ALTER TABLE...IMPORT TABLESPACE
* [Revision #457ce97ef2](https://github.com/MariaDB/server/commit/457ce97ef2)\
  2020-01-17 13:13:03 +0200
  * [MDEV-21512](https://jira.mariadb.org/browse/MDEV-21512) InnoDB may hang due to SPATIAL INDEX
* [Revision #c3695b4058](https://github.com/MariaDB/server/commit/c3695b4058)\
  2020-01-17 11:11:19 +0200
  * [MDEV-21511](https://jira.mariadb.org/browse/MDEV-21511): Remove unnecessary code
* [Revision #5838b52743](https://github.com/MariaDB/server/commit/5838b52743)\
  2020-01-17 10:46:33 +0200
  * [MDEV-21511](https://jira.mariadb.org/browse/MDEV-21511) Wrong estimate of affected BLOB columns in update
* [Revision #3e38d15585](https://github.com/MariaDB/server/commit/3e38d15585)\
  2020-01-17 10:37:25 +0200
  * [MDEV-21509](https://jira.mariadb.org/browse/MDEV-21509) Possible hang during purge of history, or rollback
* [Revision #9cae7bdcc0](https://github.com/MariaDB/server/commit/9cae7bdcc0)\
  2020-01-16 12:05:26 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Add the [WL#6326](https://askmonty.org/worklog/?tid=6326) tests
* [Revision #c4195305b2](https://github.com/MariaDB/server/commit/c4195305b2)\
  2020-01-16 13:18:44 +0200
  * [MDEV-17062](https://jira.mariadb.org/browse/MDEV-17062) : Test failure on galera.MW-336
* Merge [Revision #b04429434a](https://github.com/MariaDB/server/commit/b04429434a) 2020-01-17 00:24:17 +0300 - Merge branch '10.1' into 10.2
* [Revision #bb8226deab](https://github.com/MariaDB/server/commit/bb8226deab)\
  2020-01-16 11:59:56 +0200
  * [MDEV-21492](https://jira.mariadb.org/browse/MDEV-21492) : Galera test sporadic failure on galera.galera\_events2
* [Revision #0f0c284ec0](https://github.com/MariaDB/server/commit/0f0c284ec0)\
  2020-01-16 10:23:30 +0100
  * fix for rpl\_slave\_load\_remove\_tmpfile.test
* [Revision #a382f69e24](https://github.com/MariaDB/server/commit/a382f69e24)\
  2020-01-16 08:45:29 +0200
  * [MDEV-21498](https://jira.mariadb.org/browse/MDEV-21498) : wsrep.binlog\_format test failed on Azure
* [Revision #60d7011c5f](https://github.com/MariaDB/server/commit/60d7011c5f)\
  2020-01-10 10:44:39 +0100
  * [MDEV-21360](https://jira.mariadb.org/browse/MDEV-21360) global debug\_dbug pre-test value restoration issues
* [Revision #b7fb30e930](https://github.com/MariaDB/server/commit/b7fb30e930)\
  2020-01-09 13:38:48 +0100
  * [MDEV-21360](https://jira.mariadb.org/browse/MDEV-21360) global debug\_dbug pre-test value restoration issues
* [Revision #451573fab1](https://github.com/MariaDB/server/commit/451573fab1)\
  2019-12-23 21:48:59 +0100
  * [MDEV-21360](https://jira.mariadb.org/browse/MDEV-21360) debug\_dbug pre-test value restoration issues
* [Revision #800d1f3010](https://github.com/MariaDB/server/commit/800d1f3010)\
  2020-01-15 14:55:42 +0200
  * Disable usually failing Galera tests until a real fix is found.
* [Revision #7d31321464](https://github.com/MariaDB/server/commit/7d31321464)\
  2020-01-10 11:55:30 +0100
  * [MDEV-19803](https://jira.mariadb.org/browse/MDEV-19803) Long semaphore wait error on galera.MW-388
* [Revision #56529a7d7f](https://github.com/MariaDB/server/commit/56529a7d7f)\
  2020-01-10 22:50:19 +0700
  * [MDEV-21454](https://jira.mariadb.org/browse/MDEV-21454) Show actual mismatching values in mismatch error messages from row\_import::match\_table\_columns()
* [Revision #41cde4fe22](https://github.com/MariaDB/server/commit/41cde4fe22)\
  2020-01-09 12:45:05 +0530
  * [MDEV-18514](https://jira.mariadb.org/browse/MDEV-18514): Assertion \`!writer.checksum\_len || writer.remains == 0' failed
* Merge [Revision #8317f77ccc](https://github.com/MariaDB/server/commit/8317f77ccc) 2020-01-07 21:17:21 +0530 - Merge branch '10.1' into 10.2
* [Revision #0b4ae6724f](https://github.com/MariaDB/server/commit/0b4ae6724f)\
  2020-01-07 14:38:21 +0200
  * Fixup [MDEV-21429](https://jira.mariadb.org/browse/MDEV-21429): Correct a definition
* [Revision #82187a1221](https://github.com/MariaDB/server/commit/82187a1221)\
  2020-01-07 10:43:22 +0200
  * [MDEV-21429](https://jira.mariadb.org/browse/MDEV-21429) TRUNCATE and OPTIMIZE are being refused due to "row size too large"
* [Revision #5824e9f8df](https://github.com/MariaDB/server/commit/5824e9f8df)\
  2020-01-02 08:06:23 +0200
  * [MDEV-13569](https://jira.mariadb.org/browse/MDEV-13569): wsrep\_info.plugin failed in buildbot with "no nodes coming from prim view
* Merge [Revision #e99ba4ba51](https://github.com/MariaDB/server/commit/e99ba4ba51) 2020-01-07 07:44:37 +0200 - Merge 10.1 into 10.2
* [Revision #fd899b3bbd](https://github.com/MariaDB/server/commit/fd899b3bbd)\
  2019-12-23 01:18:39 +0800
  * Lets add another intrusive double linked list!
* Merge [Revision #b35290e19b](https://github.com/MariaDB/server/commit/b35290e19b) 2020-01-03 12:40:38 +0100 - Merge branch '10.1' into 10.2
* [Revision #ef1e488be3](https://github.com/MariaDB/server/commit/ef1e488be3)\
  2020-01-02 08:06:23 +0200
  * [MDEV-13569](https://jira.mariadb.org/browse/MDEV-13569): wsrep\_info.plugin failed in buildbot with "no nodes coming from prim view
* [Revision #4a012ce2f4](https://github.com/MariaDB/server/commit/4a012ce2f4)\
  2019-12-30 18:12:55 +0200
  * Post-fix for [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253): Remove redundant log writes
* [Revision #16bce0f6fe](https://github.com/MariaDB/server/commit/16bce0f6fe)\
  2019-12-27 11:23:28 +0200
  * Cleanup: Remove dict\_delete\_tablespace\_and\_datafiles()
* [Revision #891609b571](https://github.com/MariaDB/server/commit/891609b571)\
  2019-12-26 12:50:21 +0530
  * [MDEV-21318](https://jira.mariadb.org/browse/MDEV-21318): Wrong results with window functions and implicit grouping
* [Revision #3dfe1ba3b8](https://github.com/MariaDB/server/commit/3dfe1ba3b8)\
  2019-12-24 15:05:52 +0400
  * [MDEV-21388](https://jira.mariadb.org/browse/MDEV-21388) Wrong result of DAYNAME()=xxx in combination with condition\_pushdown\_for\_derived=on
* [Revision #cbc170adf2](https://github.com/MariaDB/server/commit/cbc170adf2)\
  2019-12-20 13:33:31 +0800
  * [MDEV-21362](https://jira.mariadb.org/browse/MDEV-21362) do something with -fno-builtin-memcmp for rem0cmp.cc
* [Revision #17b1b8118a](https://github.com/MariaDB/server/commit/17b1b8118a)\
  2019-12-23 12:43:15 +0200
  * [MDEV-21189](https://jira.mariadb.org/browse/MDEV-21189) : Dropping partition with 'wsrep\_OSU\_method=RSU' and 'SESSION sql\_log\_bin = 0' cases the galera node to hang
* [Revision #90ba87cb9e](https://github.com/MariaDB/server/commit/90ba87cb9e)\
  2019-12-23 15:56:57 +0530
  * [MDEV-19176](https://jira.mariadb.org/browse/MDEV-19176) Reduce the memory usage during recovery
* [Revision #bba59abb03](https://github.com/MariaDB/server/commit/bba59abb03)\
  2019-12-23 12:27:41 +0530
  * [MDEV-19176](https://jira.mariadb.org/browse/MDEV-19176) Reduce the memory usage during recovery
* [Revision #a59a015a75](https://github.com/MariaDB/server/commit/a59a015a75)\
  2019-12-23 07:47:16 +0200
  * Plug memory leaks from numa\_get\_mems\_allowed()
* Merge [Revision #73985d8301](https://github.com/MariaDB/server/commit/73985d8301) 2019-12-23 07:14:51 +0200 - Merge 10.1 into 10.2
* [Revision #496532b5c5](https://github.com/MariaDB/server/commit/496532b5c5)\
  2019-12-21 23:29:36 +0800
  * [MDEV-20950](https://jira.mariadb.org/browse/MDEV-20950): Fix 32-bit Windows build
* [Revision #aaaf6ceb8b](https://github.com/MariaDB/server/commit/aaaf6ceb8b)\
  2019-12-21 13:46:33 +0400
  * MDE-21369 rpl.rpl\_timezone fails with valgrind: Use of uninitialised value.
* [Revision #8174e68895](https://github.com/MariaDB/server/commit/8174e68895)\
  2019-12-20 17:55:13 +0200
  * [MDEV-21371](https://jira.mariadb.org/browse/MDEV-21371) Assertion failure in page\_rec\_get\_next\_low() during innodb\_gis.rtree\_compress
* [Revision #f6b58d2916](https://github.com/MariaDB/server/commit/f6b58d2916)\
  2019-12-20 01:16:31 +0800
  * [MDEV-21239](https://jira.mariadb.org/browse/MDEV-21239) ASAN use-after-poison in a server shutdown in innodb.innodb\_buffer\_pool\_resize
* [Revision #c3824766c5](https://github.com/MariaDB/server/commit/c3824766c5)\
  2019-12-18 09:52:10 +0200
  * Fortify galera\_partition test.
* [Revision #e9259d50f0](https://github.com/MariaDB/server/commit/e9259d50f0)\
  2019-12-17 12:10:36 +0200
  * [MDEV-21335](https://jira.mariadb.org/browse/MDEV-21335) : Galera test failure on suite wsrep
* [Revision #189fa30085](https://github.com/MariaDB/server/commit/189fa30085)\
  2019-12-17 21:57:40 +0100
  * [MDEV-21343](https://jira.mariadb.org/browse/MDEV-21343) Threadpool/Unix- wait\_begin() function does not wake/create threads, when it should
* [Revision #0d70f40bdb](https://github.com/MariaDB/server/commit/0d70f40bdb)\
  2019-12-17 16:06:15 +0100
  * Disable -Werror for rocksdb submodule
* [Revision #164cf4f463](https://github.com/MariaDB/server/commit/164cf4f463)\
  2019-12-17 21:45:53 +0530
  * [MDEV-16579](https://jira.mariadb.org/browse/MDEV-16579): Wrong result of query using DISTINCT COUNT(_) OVER (_)
* [Revision #8129ff1440](https://github.com/MariaDB/server/commit/8129ff1440)\
  2019-01-24 03:06:56 -0800
  * PR #1127 and PR #1150
* [Revision #f0aa073f2b](https://github.com/MariaDB/server/commit/f0aa073f2b)\
  2019-11-04 22:30:12 +0300
  * [MDEV-20950](https://jira.mariadb.org/browse/MDEV-20950) Reduce size of record offsets
* [Revision #beec9c0e19](https://github.com/MariaDB/server/commit/beec9c0e19)\
  2019-10-02 21:11:59 +0300
  * [MDEV-21255](https://jira.mariadb.org/browse/MDEV-21255): Deadlock of parallel slave and mariadb-backup (with failed log copy thread)
* [Revision #808036a61d](https://github.com/MariaDB/server/commit/808036a61d)\
  2019-12-12 03:45:34 +0530
  * [MDEV-19380](https://jira.mariadb.org/browse/MDEV-19380): ASAN heap-use-after-free in Protocol::net\_store\_data
* [Revision #546644f1cc](https://github.com/MariaDB/server/commit/546644f1cc)\
  2019-12-11 13:00:49 -0500
  * bump the VERSION
* [Revision #202a62deb0](https://github.com/MariaDB/server/commit/202a62deb0)\
  2019-12-11 11:22:03 +0100
  * [MDEV-11345](https://jira.mariadb.org/browse/MDEV-11345) Compile english error messages into mysqld executable.
* [Revision #280f1c2605](https://github.com/MariaDB/server/commit/280f1c2605)\
  2019-12-11 11:13:32 +0100
  * [MDEV-11345](https://jira.mariadb.org/browse/MDEV-11345) Compile english error messages into mysqld executable.
* [Revision #f2d3b2eede](https://github.com/MariaDB/server/commit/f2d3b2eede)\
  2019-12-10 16:56:52 +0200
  * Cleanup test sys\_vars.innodb\_buffer\_pool\_size\_basic
* [Revision #41e6a154ec](https://github.com/MariaDB/server/commit/41e6a154ec)\
  2019-12-10 11:23:46 +0200
  * [MDEV-14482](https://jira.mariadb.org/browse/MDEV-14482) - Cache line contention on ut\_rnd\_interval()
* [Revision #b1f2d3a8c8](https://github.com/MariaDB/server/commit/b1f2d3a8c8)\
  2019-12-10 11:20:26 +0200
  * [MDEV-21256](https://jira.mariadb.org/browse/MDEV-21256): Replace the 64-bit LCG with a 32-bit Galois LFSR
* [Revision #d146e3dcfe](https://github.com/MariaDB/server/commit/d146e3dcfe)\
  2019-12-10 11:14:57 +0200
  * [MDEV-21256](https://jira.mariadb.org/browse/MDEV-21256): Simplify ut\_rnd\_interval()
* [Revision #51fc8ab73e](https://github.com/MariaDB/server/commit/51fc8ab73e)\
  2019-12-09 12:17:12 +0200
  * [MDEV-21256](https://jira.mariadb.org/browse/MDEV-21256): Reduce the use of ut\_rnd\_gen\_next\_ulint()
* [Revision #4c0854f221](https://github.com/MariaDB/server/commit/4c0854f221)\
  2019-12-05 14:51:55 +0700
  * [MDEV-21223](https://jira.mariadb.org/browse/MDEV-21223) innodb\_fts.sync\_ddl fails in buildbot, server crashed in que\_thr\_step
* [Revision #af650c76a6](https://github.com/MariaDB/server/commit/af650c76a6)\
  2019-12-07 22:15:38 +0100
  * [MDEV-18460](https://jira.mariadb.org/browse/MDEV-18460): Server crashed in strmake / tdc\_create\_key / THD::create\_tmp\_table\_def\_key
* [Revision #425748f1b5](https://github.com/MariaDB/server/commit/425748f1b5)\
  2019-12-09 14:54:27 +0200
  * Cleanup: Replace a redundant statement with an assertion
* [Revision #292015d486](https://github.com/MariaDB/server/commit/292015d486)\
  2019-12-09 10:47:25 +0200
  * [MDEV-21254](https://jira.mariadb.org/browse/MDEV-21254) Remove unused keywords from the InnoDB SQL parser
* [Revision #59e14b9684](https://github.com/MariaDB/server/commit/59e14b9684)\
  2019-12-09 08:09:56 +0200
  * [MDEV-21189](https://jira.mariadb.org/browse/MDEV-21189): Dropping partition with 'wsrep\_OSU\_method=RSU' and 'SESSION sql\_log\_bin = 0' cases the galera node to hang
* [Revision #fd1979bc9a](https://github.com/MariaDB/server/commit/fd1979bc9a)\
  2019-12-09 01:17:16 +0400
  * [MDEV-18463](https://jira.mariadb.org/browse/MDEV-18463) Don't allow multiple table CONSTRAINTs with the same name.
* [Revision #6aa0fa3897](https://github.com/MariaDB/server/commit/6aa0fa3897)\
  2019-12-06 21:02:46 +0100
  * [CONC-417](https://jira.mariadb.org/browse/CONC-417) Windows clients using Schannel often encounter error SEC\_E\_INVALID\_TOKEN
* [Revision #6484288cd2](https://github.com/MariaDB/server/commit/6484288cd2)\
  2019-12-08 18:14:42 +0100
  * [CONC-447](https://jira.mariadb.org/browse/CONC-447) ERROR 2026 (HY000): SSL connection error: Certificate signature check failed

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
