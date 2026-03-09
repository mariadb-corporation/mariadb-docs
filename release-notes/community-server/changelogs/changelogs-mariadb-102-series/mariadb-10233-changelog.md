# MariaDB 10.2.33 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.33/)[Release Notes](../../old-releases/10.2/10.2.33.md)[Changelog](mariadb-10233-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 10 Aug 2020

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.33.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.46](../changelogs-mariadb-101-series/mariadb-10146-changelog.md)
* Merge [Revision #fbcae42c2a](https://github.com/MariaDB/server/commit/fbcae42c2a) 2020-08-06 16:47:39 +0200 - Merge branch '10.1' into 10.2
* [Revision #dc716da457](https://github.com/MariaDB/server/commit/dc716da457)\
  2020-08-03 03:34:57 +0300
  * List of unstable tests for 10.2.33 release
* Merge [Revision #9c84b80f84](https://github.com/MariaDB/server/commit/9c84b80f84) 2020-08-03 02:57:50 +0300 - Merge branch '10.1' into 10.2
* [Revision #db2a217334](https://github.com/MariaDB/server/commit/db2a217334)\
  2020-08-02 17:28:20 +0200
  * Fix for mac
* [Revision #6e09e7c14b](https://github.com/MariaDB/server/commit/6e09e7c14b)\
  2020-08-02 11:18:30 +0200
  * C/C v3.1.9
* Merge [Revision #6d8af36bc7](https://github.com/MariaDB/server/commit/6d8af36bc7) 2020-08-02 11:14:56 +0200 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #ad0d2424dd](https://github.com/MariaDB/server/commit/ad0d2424dd)\
  2020-07-13 20:02:51 +0200
  * Fix compile error for KVM. Modified filamdbf.cpp
* [Revision #1e07df99f3](https://github.com/MariaDB/server/commit/1e07df99f3)\
  2020-07-13 16:30:57 +0200\
  \*
  * Fix [MDEV-22561](https://jira.mariadb.org/browse/MDEV-22561) Unable to access DBF inside a ZIP archive
* [Revision #2654ddd2d5](https://github.com/MariaDB/server/commit/2654ddd2d5)\
  2020-05-19 00:05:56 +0200\
  \*
  * Fix [MDEV-22571](https://jira.mariadb.org/browse/MDEV-22571) and [MDEV-22572](https://jira.mariadb.org/browse/MDEV-22572). Allow multiple ZIP table and enable using special column in them
* Merge [Revision #ef7cb0a0b5](https://github.com/MariaDB/server/commit/ef7cb0a0b5) 2020-08-02 11:05:29 +0200 - Merge branch '10.1' into 10.2
* [Revision #5ec40fbb27](https://github.com/MariaDB/server/commit/5ec40fbb27)\
  2020-07-31 16:45:35 +0530
  * [MDEV-14711](https://jira.mariadb.org/browse/MDEV-14711) Fix-up
* [Revision #a6066e230e](https://github.com/MariaDB/server/commit/a6066e230e)\
  2020-07-31 15:07:43 +0530
  * [MDEV-22511](https://jira.mariadb.org/browse/MDEV-22511) innodb.truncate\_foreign failed in buildbot with wrong error code
* [Revision #879ba1979b](https://github.com/MariaDB/server/commit/879ba1979b)\
  2020-07-31 11:51:44 +0300
  * [MDEV-11799](https://jira.mariadb.org/browse/MDEV-11799) Doublewrite recovery can corrupt data pages
* [Revision #f35d172103](https://github.com/MariaDB/server/commit/f35d172103)\
  2020-07-31 11:38:23 +0300
  * [MDEV-23198](https://jira.mariadb.org/browse/MDEV-23198) Crash in REPLACE
* [Revision #fd0abc890f](https://github.com/MariaDB/server/commit/fd0abc890f)\
  2020-07-29 01:01:24 +1000
  * [MDEV-18042](https://jira.mariadb.org/browse/MDEV-18042) Server crashes upon adding a non-null date column under NO\_ZERO\_DATE with ALGORITHM=INPLACE
* [Revision #91ebf1844f](https://github.com/MariaDB/server/commit/91ebf1844f)\
  2020-07-28 23:45:51 +1000
  * [MDEV-19338](https://jira.mariadb.org/browse/MDEV-19338) InnoDB: Failing assertion: !cursor->index->is\_committed()
* [Revision #8a612314d0](https://github.com/MariaDB/server/commit/8a612314d0)\
  2020-07-30 13:38:43 +0530
  * [MDEV-23332](https://jira.mariadb.org/browse/MDEV-23332) Index online status assert failure in btr\_search\_drop\_page\_hash\_index
* [Revision #c5d4dd2533](https://github.com/MariaDB/server/commit/c5d4dd2533)\
  2020-07-30 09:24:36 +0300
  * [MDEV-23339](https://jira.mariadb.org/browse/MDEV-23339) innodb\_force\_recovery=2 may still abort the rollback of recovered transactions
* [Revision #2107e3bb9c](https://github.com/MariaDB/server/commit/2107e3bb9c)\
  2020-07-28 10:39:05 +0200
  * [MDEV-21258](https://jira.mariadb.org/browse/MDEV-21258): Can't uninstall plugin if the library file doesn't exist
* [Revision #8ec877f40a](https://github.com/MariaDB/server/commit/8ec877f40a)\
  2020-07-29 08:17:57 +0300
  * speed up my\_timer\_init()
* [Revision #3c3f172f17](https://github.com/MariaDB/server/commit/3c3f172f17)\
  2020-07-28 11:24:07 +0300
  * [MDEV-23308](https://jira.mariadb.org/browse/MDEV-23308) CHECK TABLE attempts to access parent\_right\_page\_no=FIL\_NULL
* [Revision #6307b17aa1](https://github.com/MariaDB/server/commit/6307b17aa1)\
  2020-07-28 11:17:20 +0300
  * [MDEV-20142](https://jira.mariadb.org/browse/MDEV-20142) encryption.innodb\_encrypt\_temporary\_tables failed in buildbot with wrong result
* [Revision #940668f5cb](https://github.com/MariaDB/server/commit/940668f5cb)\
  2020-07-28 19:53:19 +1000
  * [MDEV-23137](https://jira.mariadb.org/browse/MDEV-23137): aarch64, postfix - cmake include
* [Revision #459b87f6b4](https://github.com/MariaDB/server/commit/459b87f6b4)\
  2020-06-18 11:02:19 +0300
  * [MDEV-9911](https://jira.mariadb.org/browse/MDEV-9911): NTILE must return an error when parameter is not stable
* [Revision #cae4b3f811](https://github.com/MariaDB/server/commit/cae4b3f811)\
  2020-06-22 14:39:15 +1000
  * rocksdb: FreeBSD disable jemalloc search
* [Revision #715beee46a](https://github.com/MariaDB/server/commit/715beee46a)\
  2020-07-02 09:39:13 +1000
  * [MDEV-23051](https://jira.mariadb.org/browse/MDEV-23051): riscv64 fails build (atomics)
* [Revision #d88ea26088](https://github.com/MariaDB/server/commit/d88ea26088)\
  2020-07-27 18:38:10 +0800
  * [MDEV-23137](https://jira.mariadb.org/browse/MDEV-23137): RocksDB: undefined reference to crc32c\_arm64
* [Revision #186d9d0d72](https://github.com/MariaDB/server/commit/186d9d0d72)\
  2020-06-22 14:24:31 +1000
  * [MDEV-12474](https://jira.mariadb.org/browse/MDEV-12474): rocksdb: mtr - rocksdb.concurrent\_alter use sh
* [Revision #a1f899a8ab](https://github.com/MariaDB/server/commit/a1f899a8ab)\
  2020-07-24 16:52:42 +0530
  * [MDEV-23233](https://jira.mariadb.org/browse/MDEV-23233): Race condition for btr\_search\_drop\_page\_hash\_index() in buf\_page\_create()
* [Revision #b4c742108f](https://github.com/MariaDB/server/commit/b4c742108f)\
  2020-07-27 14:34:24 +0300
  * Enable fixed test case.
* [Revision #a6410deba9](https://github.com/MariaDB/server/commit/a6410deba9)\
  2020-07-27 13:53:33 +0530
  * [MDEV-18916](https://jira.mariadb.org/browse/MDEV-18916): crash in Window\_spec::print\_partition() with decimals
* [Revision #5f1ec5cbb7](https://github.com/MariaDB/server/commit/5f1ec5cbb7)\
  2020-07-23 16:59:30 +0530
  * [MDEV-14711](https://jira.mariadb.org/browse/MDEV-14711) Assertion \`mode == 16 || mode == 12 || !fix\_block->page.file\_page\_was\_freed' failed in buf\_page\_get\_gen (rollback requesting a freed undo page)
* [Revision #a3a249c72f](https://github.com/MariaDB/server/commit/a3a249c72f)\
  2020-07-20 14:16:19 +0200
  * [MDEV-15236](https://jira.mariadb.org/browse/MDEV-15236): galera\_ist\_progress fails when trying to read transfer status
* [Revision #c9928cc0fb](https://github.com/MariaDB/server/commit/c9928cc0fb)\
  2020-06-23 10:23:40 +0300
  * [MDEV-20928](https://jira.mariadb.org/browse/MDEV-20928) mtr test galera.galera\_var\_innodb\_disallow\_writes test failure
* [Revision #ba23e6d76f](https://github.com/MariaDB/server/commit/ba23e6d76f)\
  2020-07-23 08:59:18 +0300
  * [MDEV-18177](https://jira.mariadb.org/browse/MDEV-18177) : Galera test failure on galera\_autoinc\_sst\_mariadb-backup
* [Revision #b3b1c51e4d](https://github.com/MariaDB/server/commit/b3b1c51e4d)\
  2020-07-23 20:43:09 +0530
  * [MDEV-23134](https://jira.mariadb.org/browse/MDEV-23134) SEGV in dict\_load\_table\_one during restart after server crash
* [Revision #fe39d02f51](https://github.com/MariaDB/server/commit/fe39d02f51)\
  2020-07-23 16:23:20 +0530
  * [MDEV-20638](https://jira.mariadb.org/browse/MDEV-20638) Remove the deadcode from srv\_master\_thread() and srv\_active\_wake\_master\_thread\_low()
* [Revision #b3dd95e035](https://github.com/MariaDB/server/commit/b3dd95e035)\
  2020-07-23 12:54:13 +0530
  * [MDEV-14203](https://jira.mariadb.org/browse/MDEV-14203): rpl.rpl\_extra\_col\_master\_myisam, rpl.rpl\_slave\_load\_tmpdir\_not\_exist failed in buildbot with a warning
* [Revision #3a8943ae73](https://github.com/MariaDB/server/commit/3a8943ae73)\
  2020-07-21 13:17:53 +0530
  * [MDEV-17481](https://jira.mariadb.org/browse/MDEV-17481) mariadb service won't shutdown when it's running and the OS datetime updated backwards
* [Revision #2a3bc0b9cd](https://github.com/MariaDB/server/commit/2a3bc0b9cd)\
  2020-07-21 12:49:27 +0530
  * [MDEV-13830](https://jira.mariadb.org/browse/MDEV-13830) Assertion failed: recv\_sys->mlog\_checkpoint\_lsn <= recv\_sys->recovered\_lsn
* [Revision #6898eae7f8](https://github.com/MariaDB/server/commit/6898eae7f8)\
  2020-07-22 11:17:43 +1000
  * fix assertion
* [Revision #ebca70ead3](https://github.com/MariaDB/server/commit/ebca70ead3)\
  2020-07-21 23:12:32 +1000
  * fix c++98 build
* [Revision #5acd391e8b](https://github.com/MariaDB/server/commit/5acd391e8b)\
  2019-09-04 04:29:03 +1000
  * [MDEV-16039](https://jira.mariadb.org/browse/MDEV-16039) Crash when selecting virtual columns generated using functions with DAYNAME()
* Merge [Revision #ca9276e37e](https://github.com/MariaDB/server/commit/ca9276e37e) 2020-07-20 14:53:24 +0300 - Merge 10.1 into 10.2
* [Revision #a1e52e7f32](https://github.com/MariaDB/server/commit/a1e52e7f32)\
  2020-07-16 16:40:37 +0200
  * [MDEV-20401](https://jira.mariadb.org/browse/MDEV-20401): revert unnecessary change
* [Revision #b3cae9db11](https://github.com/MariaDB/server/commit/b3cae9db11)\
  2020-05-12 13:29:17 +0200
  * [MDEV-20401](https://jira.mariadb.org/browse/MDEV-20401): Server incorrectly auto-sets lower\_case\_file\_system value
* [Revision #147d4b1ec0](https://github.com/MariaDB/server/commit/147d4b1ec0)\
  2020-07-16 06:35:15 +0300
  * [MDEV-21347](https://jira.mariadb.org/browse/MDEV-21347) innodb\_log\_optimize\_ddl=OFF is not crash safe
* [Revision #fee11c7727](https://github.com/MariaDB/server/commit/fee11c7727)\
  2020-07-15 19:26:20 +0300
  * Make page validation stricter
* [Revision #38b4c07833](https://github.com/MariaDB/server/commit/38b4c07833)\
  2020-07-15 19:25:24 +0300
  * [MDEV-23183](https://jira.mariadb.org/browse/MDEV-23183) Infinite loop on page\_validate() on corrupted page
* [Revision #9c8420fe8c](https://github.com/MariaDB/server/commit/9c8420fe8c)\
  2020-07-15 09:49:48 +0200
  * Fix compile warning
* [Revision #07e89bf7d1](https://github.com/MariaDB/server/commit/07e89bf7d1)\
  2020-07-14 15:13:40 +0300
  * [MDEV-23163](https://jira.mariadb.org/browse/MDEV-23163) Merge new release of InnoDB 5.7.31 to 10.2
* Merge [Revision #646a6005e7](https://github.com/MariaDB/server/commit/646a6005e7) 2020-07-14 15:10:59 +0300 - Merge 10.1 into 10.2
* [Revision #6b6c012f33](https://github.com/MariaDB/server/commit/6b6c012f33)\
  2020-07-14 09:36:38 +0200
  * Merge branch '10.4-[MDEV-18838](https://jira.mariadb.org/browse/MDEV-18838)' of [mariadb-server](https://github.com/codership/mariadb-server) into 10.2-[MDEV-18838](https://jira.mariadb.org/browse/MDEV-18838)
* [Revision #b0df247db6](https://github.com/MariaDB/server/commit/b0df247db6)\
  2020-07-10 10:45:04 +0530
  * [MDEV-22463](https://jira.mariadb.org/browse/MDEV-22463): Element\_type \&Bounds\_checked\_array\<Item \*>::operator \[Element\_type = Item \*]: Assertion \`n < m\_size' failed.
* [Revision #0994af43e5](https://github.com/MariaDB/server/commit/0994af43e5)\
  2020-07-02 19:03:39 +0530
  * [MDEV-22058](https://jira.mariadb.org/browse/MDEV-22058): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed in Diagnostics\_area::set\_ok\_status
* [Revision #f81ff93287](https://github.com/MariaDB/server/commit/f81ff93287)\
  2020-07-10 21:27:20 +0530
  * [MDEV-19119](https://jira.mariadb.org/browse/MDEV-19119): main.ssl\_crl fails in buildbot with wrong error code
* [Revision #737c3025e9](https://github.com/MariaDB/server/commit/737c3025e9)\
  2020-07-09 14:01:06 +0530
  * [MDEV-10120](https://jira.mariadb.org/browse/MDEV-10120): Wrong result of UNION .. ORDER BY GROUP\_CONCAT()
* [Revision #a759f9af51](https://github.com/MariaDB/server/commit/a759f9af51)\
  2020-07-09 08:54:59 +0200
  * Fix typo in the comment (and old info)
* [Revision #253aa7bbc4](https://github.com/MariaDB/server/commit/253aa7bbc4)\
  2020-07-07 17:30:52 +0530
  * [MDEV-12059](https://jira.mariadb.org/browse/MDEV-12059): Assertion \`precision > 0' failed with a window function or window aggregate function
* Merge [Revision #dba7e1e8e1](https://github.com/MariaDB/server/commit/dba7e1e8e1) 2020-07-02 06:05:13 +0300 - Merge 10.1 into 10.2
* [Revision #838a1046b2](https://github.com/MariaDB/server/commit/838a1046b2)\
  2020-07-02 06:03:59 +0300
  * [MDEV-20377](https://jira.mariadb.org/browse/MDEV-20377): Fix cmake -DPLUGIN\_PERFSCHEMA=NO
* [Revision #69df4f834b](https://github.com/MariaDB/server/commit/69df4f834b)\
  2020-07-01 20:34:06 +0300
  * [MDEV-20377](https://jira.mariadb.org/browse/MDEV-20377): Fix -Wunused-but-set-variable
* [Revision #be51738465](https://github.com/MariaDB/server/commit/be51738465)\
  2020-07-01 17:43:44 +0300
  * [MDEV-20428](https://jira.mariadb.org/browse/MDEV-20428) after-merge fix: Stabilize the test
* [Revision #c36834c832](https://github.com/MariaDB/server/commit/c36834c832)\
  2020-07-01 17:23:00 +0300
  * [MDEV-20377](https://jira.mariadb.org/browse/MDEV-20377): Make WITH\_MSAN more usable
* [Revision #5a097c5556](https://github.com/MariaDB/server/commit/5a097c5556)\
  2020-03-13 14:59:02 +0100
  * [MDEV-21222](https://jira.mariadb.org/browse/MDEV-21222) mariadb-backup.incremental\_backup failed with memory allocation failure
* [Revision #9ed50ece33](https://github.com/MariaDB/server/commit/9ed50ece33)\
  2020-07-01 17:18:47 +0300
  * [MDEV-22779](https://jira.mariadb.org/browse/MDEV-22779): Fix a memory leak in the unit test
* Merge [Revision #ea2bc974dc](https://github.com/MariaDB/server/commit/ea2bc974dc) 2020-07-01 11:32:21 +0300 - Merge 10.1 into 10.2
* [Revision #fbfb5b5f68](https://github.com/MariaDB/server/commit/fbfb5b5f68)\
  2020-07-01 11:39:22 +0530
  * [MDEV-22852](https://jira.mariadb.org/browse/MDEV-22852): SIGSEGV in sortlength (optimized builds)
* [Revision #4a2e7b5368](https://github.com/MariaDB/server/commit/4a2e7b5368)\
  2020-06-30 18:16:01 +0530
  * [MDEV-22984](https://jira.mariadb.org/browse/MDEV-22984): Throw an error when arguments to window functions are window functions
* [Revision #17109001d6](https://github.com/MariaDB/server/commit/17109001d6)\
  2020-06-30 12:00:54 +0300
  * speed up fil\_validate() in debug builds
* [Revision #97f7d4a9b4](https://github.com/MariaDB/server/commit/97f7d4a9b4)\
  2020-06-15 13:40:50 +0300
  * [MDEV-22726](https://jira.mariadb.org/browse/MDEV-22726): Add check that one can't change general or slow log to a transactional engine
* [Revision #e3104c4a8c](https://github.com/MariaDB/server/commit/e3104c4a8c)\
  2020-06-17 08:07:01 +0300
  * [MDEV-22179](https://jira.mariadb.org/browse/MDEV-22179) rr support for mtr
* [Revision #fe0cf85d5a](https://github.com/MariaDB/server/commit/fe0cf85d5a)\
  2020-02-11 10:27:59 -0800
  * [MDEV-21709](https://jira.mariadb.org/browse/MDEV-21709) ZFS snapdir=visible breaks Galera rsync SST replcation
* [Revision #eba9189777](https://github.com/MariaDB/server/commit/eba9189777)\
  2020-06-22 13:25:25 +0300
  * Test case cleanups.
* [Revision #51c8289ed6](https://github.com/MariaDB/server/commit/51c8289ed6)\
  2020-06-15 16:39:41 +0300
  * [MDEV-21759](https://jira.mariadb.org/browse/MDEV-21759) galera.galera\_parallel\_autoinc\_manytrx sporadic failures.
* [Revision #3ddb080536](https://github.com/MariaDB/server/commit/3ddb080536)\
  2020-06-14 22:13:45 +0300
  * Fix include statements in galera\_ipv6\_mariadb-backup\_section and galera\_ipv6\_mariadb-backup MTR tests
* [Revision #5d7e067cce](https://github.com/MariaDB/server/commit/5d7e067cce)\
  2020-06-17 12:58:33 +0300
  * [MDEV-22125](https://jira.mariadb.org/browse/MDEV-22125) : galera.galera\_drop\_multi MTR failed: InnoDB: MySQL is trying to drop database `fts`.\`\` though there are still open handles
* [Revision #319886eca7](https://github.com/MariaDB/server/commit/319886eca7)\
  2020-06-22 12:18:12 +0300
  * [MDEV-20928](https://jira.mariadb.org/browse/MDEV-20928) : Galera test failure on galera.galera\_var\_innodb\_disallow\_writes: Result length mismatch
* [Revision #30903c3743](https://github.com/MariaDB/server/commit/30903c3743)\
  2020-06-22 15:43:53 +0400
  * [MDEV-22976](https://jira.mariadb.org/browse/MDEV-22976) CAST(JSON\_EXTRACT() AS DECIMAL) does not handle boolean values
* [Revision #009ef36d9a](https://github.com/MariaDB/server/commit/009ef36d9a)\
  2020-06-16 22:59:00 +0300
  * [MDEV-22179](https://jira.mariadb.org/browse/MDEV-22179) rr support for mtr review
* [Revision #804ed12e0e](https://github.com/MariaDB/server/commit/804ed12e0e)\
  2020-04-17 16:32:51 +0530
  * [MDEV-22179](https://jira.mariadb.org/browse/MDEV-22179) rr(record and replay) support for mtr
* [Revision #e30c4cfc7a](https://github.com/MariaDB/server/commit/e30c4cfc7a)\
  2020-06-12 09:38:35 +0530
  * [MDEV-22811](https://jira.mariadb.org/browse/MDEV-22811) DDL fails to drop and re-create FTS index
* [Revision #b46b7144d1](https://github.com/MariaDB/server/commit/b46b7144d1)\
  2020-06-17 11:19:50 +0400
  * [MDEV-21695](https://jira.mariadb.org/browse/MDEV-21695) Server crashes in TABLE::evaluate\_update\_default\_function upon UPDATE on temporary table
* [Revision #fb0d18e412](https://github.com/MariaDB/server/commit/fb0d18e412)\
  2020-06-16 12:12:36 +0300
  * Add global ignore for Sending JOIN failed warning.
* [Revision #7710f28eec](https://github.com/MariaDB/server/commit/7710f28eec)\
  2020-06-15 09:29:17 +0300
  * Add missing include as test requires galera debug library
* [Revision #e623d24787](https://github.com/MariaDB/server/commit/e623d24787)\
  2020-06-13 23:28:09 +0300
  * [MDEV-22779](https://jira.mariadb.org/browse/MDEV-22779): Crash: Prepared Statement ..., part #2.
* [Revision #21e79331c8](https://github.com/MariaDB/server/commit/21e79331c8)\
  2020-06-13 16:45:55 +0300
  * [MDEV-22779](https://jira.mariadb.org/browse/MDEV-22779): Crash: Prepared Statement with a '?' parameter inside a re-used CTE
* [Revision #2cd6afb083](https://github.com/MariaDB/server/commit/2cd6afb083)\
  2020-06-14 10:18:07 +0300
  * [MDEV-22889](https://jira.mariadb.org/browse/MDEV-22889): Disable innodb.innodb\_force\_recovery\_rollback
* [Revision #b68f1d847f](https://github.com/MariaDB/server/commit/b68f1d847f)\
  2020-06-13 14:45:52 +0300
  * [MDEV-21217](https://jira.mariadb.org/browse/MDEV-21217) innodb\_force\_recovery=2 may wrongly abort rollback
* [Revision #2fd2fd77e7](https://github.com/MariaDB/server/commit/2fd2fd77e7)\
  2020-06-12 10:45:54 +0300
  * Fix wrong merge of commit d218d1aa49e848cef2bdbe83bbaf08e474d5209c
* Merge [Revision #8c67ffffe8](https://github.com/MariaDB/server/commit/8c67ffffe8) 2020-06-11 22:35:30 +0300 - Merge branch '10.1' into 10.2
* [Revision #e835881c47](https://github.com/MariaDB/server/commit/e835881c47)\
  2020-06-11 15:33:16 +0400
  * [MDEV-21619](https://jira.mariadb.org/browse/MDEV-21619) Server crash or assertion failures in my\_datetime\_to\_str
* [Revision #1bcc5cd9b6](https://github.com/MariaDB/server/commit/1bcc5cd9b6)\
  2020-06-10 16:14:14 +0300
  * Remove a stale test
* [Revision #9b9a354da9](https://github.com/MariaDB/server/commit/9b9a354da9)\
  2020-06-10 08:42:31 +0400
  * [MDEV-22849](https://jira.mariadb.org/browse/MDEV-22849) Reuse skip\_trailing\_space() in my\_hash\_sort\_utf8mbX
* [Revision #902742789e](https://github.com/MariaDB/server/commit/902742789e)\
  2020-06-09 21:54:42 +1000
  * innodb: dict\_mem\_table\_add\_col - compile warning fix argument 1 null where non-null expected (#1584)
* [Revision #f458b40f66](https://github.com/MariaDB/server/commit/f458b40f66)\
  2020-06-08 10:28:34 +0300
  * [MDEV-22827](https://jira.mariadb.org/browse/MDEV-22827) InnoDB: Failing assertion: purge\_sys->n\_stop == 0
* [Revision #e9dbbf1120](https://github.com/MariaDB/server/commit/e9dbbf1120)\
  2020-06-06 11:38:38 -0700
  * [MDEV-22748](https://jira.mariadb.org/browse/MDEV-22748) MariaDB crash on WITH RECURSIVE large query
* [Revision #be0c46eb97](https://github.com/MariaDB/server/commit/be0c46eb97)\
  2020-06-06 21:34:21 +0300
  * [MDEV-22817](https://jira.mariadb.org/browse/MDEV-22817): Skip the test in --embedded
* [Revision #187b9c924e](https://github.com/MariaDB/server/commit/187b9c924e)\
  2020-06-06 18:07:13 +0300
  * [MDEV-22817](https://jira.mariadb.org/browse/MDEV-22817): Add a test case
* Merge [Revision #0df01ccb66](https://github.com/MariaDB/server/commit/0df01ccb66) 2020-06-06 18:07:04 +0300 - Merge 10.1 into 10.2
* [Revision #1bd5b75c73](https://github.com/MariaDB/server/commit/1bd5b75c73)\
  2020-06-06 09:32:18 +0300
  * [MDEV-22818](https://jira.mariadb.org/browse/MDEV-22818) Server crash on corrupted ROW\_FORMAT=COMPRESSED page
* [Revision #7a695d8a82](https://github.com/MariaDB/server/commit/7a695d8a82)\
  2020-06-05 23:33:24 +0300
  * fix compilation with VS2019, preview of 16.7 version
* [Revision #a8c200c73c](https://github.com/MariaDB/server/commit/a8c200c73c)\
  2020-06-05 10:38:40 -0700
  * [MDEV-22042](https://jira.mariadb.org/browse/MDEV-22042) Server crash in Item\_field::print on ANALYZE FORMAT=JSON
* Merge [Revision #fff7897e3a](https://github.com/MariaDB/server/commit/fff7897e3a) 2020-06-05 19:58:52 +0200 - Merge branch '10.2' of [server](https://github.com/MariaDB/server) into 10.2
* [Revision #15cdcb2af8](https://github.com/MariaDB/server/commit/15cdcb2af8)\
  2020-06-05 17:56:34 +0200
  * Fix appveyor build.
* Merge [Revision #5f55f69e4a](https://github.com/MariaDB/server/commit/5f55f69e4a) 2020-06-05 18:32:37 +0200 - Merge 10.1 into 10.2
* [Revision #efc70da5fd](https://github.com/MariaDB/server/commit/efc70da5fd)\
  2020-06-05 14:59:33 +0300
  * [MDEV-22769](https://jira.mariadb.org/browse/MDEV-22769) Shutdown hang or crash due to XA breaking locks
* [Revision #138c11cce5](https://github.com/MariaDB/server/commit/138c11cce5)\
  2020-06-04 12:29:32 +0300
  * [MDEV-22790](https://jira.mariadb.org/browse/MDEV-22790) Race between btr\_page\_mtr\_lock() dropping AHI on the same block
* [Revision #3677dd5cb4](https://github.com/MariaDB/server/commit/3677dd5cb4)\
  2020-06-05 15:20:20 +0300
  * [MDEV-22646](https://jira.mariadb.org/browse/MDEV-22646): Fix a memory leak
* [Revision #1828196f73](https://github.com/MariaDB/server/commit/1828196f73)\
  2020-06-05 13:29:01 +0200
  * Windows, build tweak.
* [Revision #29ed04cb6d](https://github.com/MariaDB/server/commit/29ed04cb6d)\
  2020-06-03 14:43:13 +0200
  * add stress suite to the list of default suites to run
* [Revision #dce4c0f979](https://github.com/MariaDB/server/commit/dce4c0f979)\
  2020-04-23 21:58:52 +0400
  * [MDEV-22339](https://jira.mariadb.org/browse/MDEV-22339) - Assertion \`str\_length < len' failed
* [Revision #c5883debd6](https://github.com/MariaDB/server/commit/c5883debd6)\
  2020-06-04 16:31:29 +0300
  * dict\_check\_sys\_tables(): Do not rely on buf\_page\_optimistic\_get()
* [Revision #f69278bcd0](https://github.com/MariaDB/server/commit/f69278bcd0)\
  2020-06-02 16:31:53 +0530
  * [MDEV-16230](https://jira.mariadb.org/browse/MDEV-16230): Server crashes when Analyze format=json is run with a window function with empty PARTITION BY and ORDER BY clauses
* [Revision #eba2d10ac5](https://github.com/MariaDB/server/commit/eba2d10ac5)\
  2020-06-04 10:24:10 +0300
  * [MDEV-22721](https://jira.mariadb.org/browse/MDEV-22721) Remove bloat caused by InnoDB logger class
* [Revision #ad2bf1129c](https://github.com/MariaDB/server/commit/ad2bf1129c)\
  2020-05-27 13:03:06 +0530
  * [MDEV-22646](https://jira.mariadb.org/browse/MDEV-22646) Assertion \`table2->cached' failed in dict\_table\_t::add\_to\_cache
* [Revision #ca3aa67964](https://github.com/MariaDB/server/commit/ca3aa67964)\
  2020-06-03 12:14:11 +0300
  * [MDEV-22577](https://jira.mariadb.org/browse/MDEV-22577) innodb\_fast\_shutdown=0 fails to report purge progress
* [Revision #50641db2d1](https://github.com/MariaDB/server/commit/50641db2d1)\
  2020-06-01 15:38:04 +0200
  * fix warning
* [Revision #02f68552a4](https://github.com/MariaDB/server/commit/02f68552a4)\
  2020-06-01 14:34:16 +0530
  * [MDEV-22650](https://jira.mariadb.org/browse/MDEV-22650) Dirty compressed page checksum validation fails
* [Revision #83d0e72b34](https://github.com/MariaDB/server/commit/83d0e72b34)\
  2020-06-01 10:23:11 +0300
  * Cleanup: Remove thr\_is\_recv(), trx\_is\_recv()
* [Revision #c50b7bee33](https://github.com/MariaDB/server/commit/c50b7bee33)\
  2020-06-01 10:18:47 +0300
  * [MDEV-21615](https://jira.mariadb.org/browse/MDEV-21615) InnoDB: innodb\_page\_size=x requires... should be logged as error
* Merge [Revision #d72eebaa3d](https://github.com/MariaDB/server/commit/d72eebaa3d) 2020-06-01 09:33:03 +0300 - Merge 10.1 into 10.2
* [Revision #4832b751ad](https://github.com/MariaDB/server/commit/4832b751ad)\
  2020-05-31 11:00:47 +0200
  * cmake: quieter
* [Revision #38ea795bb6](https://github.com/MariaDB/server/commit/38ea795bb6)\
  2020-05-29 01:51:30 +0900
  * Add a counter to avoid multiple initialization of Groonga mecab tokenizer
* [Revision #6e6a4227c0](https://github.com/MariaDB/server/commit/6e6a4227c0)\
  2020-05-28 10:21:46 +0900
  * Add grn\_db\_fin\_mecab\_tokenizer to finalyze mecab tokenizer
* [Revision #069200267d](https://github.com/MariaDB/server/commit/069200267d)\
  2020-05-28 15:03:28 +0200
  * Fix cmake warning - custom command succeeds without creating own OUTPUT.
* [Revision #b00cd3e453](https://github.com/MariaDB/server/commit/b00cd3e453)\
  2020-05-28 15:02:10 +0200
  * [MDEV-22743](https://jira.mariadb.org/browse/MDEV-22743) Windows 10 MSI installer : port in use is not determined
* [Revision #ff72f36948](https://github.com/MariaDB/server/commit/ff72f36948)\
  2020-05-28 02:06:23 +0200
  * MSI installer : Use CAQuietExec64 on Win64 , not CAQuietExec
* [Revision #e2d7da4982](https://github.com/MariaDB/server/commit/e2d7da4982)\
  2020-05-28 01:43:21 +0200
  * Remove unused WiX source file
* [Revision #8afcc37c68](https://github.com/MariaDB/server/commit/8afcc37c68)\
  2020-05-26 14:11:41 +0200
  * update C/C
* [Revision #2c9c9acbfc](https://github.com/MariaDB/server/commit/2c9c9acbfc)\
  2020-05-26 12:11:24 +0200
  * bintars should use bundled PCRE
* [Revision #9fd8f1b264](https://github.com/MariaDB/server/commit/9fd8f1b264)\
  2020-05-24 17:30:57 +0200
  * mtr: update titlebar when the test ends, not when it starts
* [Revision #e64dc07125](https://github.com/MariaDB/server/commit/e64dc07125)\
  2020-05-24 21:10:41 +0200
  * assert(a && b); -> assert(a); assert(b);
* [Revision #04726f2920](https://github.com/MariaDB/server/commit/04726f2920)\
  2020-05-23 18:35:42 +0200
  * get rid of cmake warning
* [Revision #8cf589218f](https://github.com/MariaDB/server/commit/8cf589218f)\
  2020-05-22 19:50:22 +0200
  * optimize performance of the build in a fresh clone
* [Revision #cceb965a79](https://github.com/MariaDB/server/commit/cceb965a79)\
  2020-05-22 12:05:53 +0200
  * Revert "[MDEV-12445](https://jira.mariadb.org/browse/MDEV-12445) : Rocksdb does not shutdown worker threads and aborts in memleak check on server shutdown"
* [Revision #6af37ba881](https://github.com/MariaDB/server/commit/6af37ba881)\
  2020-05-21 01:31:17 +0200
  * fix rocksdb zstd detection
* [Revision #ad77247866](https://github.com/MariaDB/server/commit/ad77247866)\
  2020-05-20 17:04:22 +0200
  * [MDEV-21958](https://jira.mariadb.org/browse/MDEV-21958) Query having many NOT-IN clauses running forever and causing available free memory to use completely
* [Revision #1e951155bd](https://github.com/MariaDB/server/commit/1e951155bd)\
  2020-05-20 17:02:47 +0200
  * bugfix: use THD::main\_mem\_root for kill error message
* [Revision #b01c8a6cc8](https://github.com/MariaDB/server/commit/b01c8a6cc8)\
  2020-05-14 16:18:01 +0200
  * [MDEV-22558](https://jira.mariadb.org/browse/MDEV-22558) wrong error for invalid utf8 table comment
* [Revision #39c141b4ae](https://github.com/MariaDB/server/commit/39c141b4ae)\
  2020-05-13 19:48:23 +0200
  * don't include .git files in source packages
* [Revision #a50e6c9eb1](https://github.com/MariaDB/server/commit/a50e6c9eb1)\
  2020-05-13 13:10:35 +0200
  * [MDEV-17153](https://jira.mariadb.org/browse/MDEV-17153) server crash on repair table ... use\_frm
* [Revision #5139cfabb3](https://github.com/MariaDB/server/commit/5139cfabb3)\
  2020-05-27 12:59:27 +0300
  * fix compilation
* [Revision #1b3adaab25](https://github.com/MariaDB/server/commit/1b3adaab25)\
  2020-05-27 10:58:28 +0300
  * Fix the build with GCC 4.1.2
* [Revision #bf1aa7569e](https://github.com/MariaDB/server/commit/bf1aa7569e)\
  2020-05-27 09:53:36 +0300
  * Add an end-of-test marker to ease merges
* [Revision #67496281ea](https://github.com/MariaDB/server/commit/67496281ea)\
  2020-05-27 09:51:46 +0300
  * Fix the RelWithDebInfo build
* [Revision #18d8f06f31](https://github.com/MariaDB/server/commit/18d8f06f31)\
  2020-05-17 16:24:40 +0300
  * intrusive::list fixes
* [Revision #403dacf6a9](https://github.com/MariaDB/server/commit/403dacf6a9)\
  2020-05-26 20:04:47 +0300
  * Fixed crash in aria recovery when using bulk insert
* [Revision #0c1f97b3ab](https://github.com/MariaDB/server/commit/0c1f97b3ab)\
  2020-05-05 20:32:32 +0300
  * [MDEV-15152](https://jira.mariadb.org/browse/MDEV-15152) Optimistic parallel slave doesnt cope well with START SLAVE UNTIL
* Merge [Revision #451bfcd6bb](https://github.com/MariaDB/server/commit/451bfcd6bb) 2020-05-26 18:48:35 +0300 - Merge remote-tracking branch 'origin/10.1' into 10.2 to skip 10.1 dbe447a7890 commit.
* [Revision #f1f14c2092](https://github.com/MariaDB/server/commit/f1f14c2092)\
  2020-05-26 13:14:47 +0300
  * [MDEV-20015](https://jira.mariadb.org/browse/MDEV-20015) Assertion \`!in\_use->is\_error()' failed in TABLE::update\_virtual\_field
* Merge [Revision #6a26e0c719](https://github.com/MariaDB/server/commit/6a26e0c719) 2020-05-26 13:01:34 +0300 - Merge 10.1 into 10.2
* [Revision #fbcfbb0e1c](https://github.com/MariaDB/server/commit/fbcfbb0e1c)\
  2020-05-26 11:43:43 +0300
  * [MDEV-19751](https://jira.mariadb.org/browse/MDEV-19751) Wrong partitioning by KEY() after primary key dropped
* [Revision #5530a93f47](https://github.com/MariaDB/server/commit/5530a93f47)\
  2020-05-25 18:57:14 +0300
  * [MDEV-17092](https://jira.mariadb.org/browse/MDEV-17092) use-after-poison around lock\_trx\_handle\_wait\_low
* [Revision #e2c749380b](https://github.com/MariaDB/server/commit/e2c749380b)\
  2020-05-25 17:46:52 +0300
  * [MDEV-22545](https://jira.mariadb.org/browse/MDEV-22545) post-fix: Fix a test result
* [Revision #4a6b28c7b9](https://github.com/MariaDB/server/commit/4a6b28c7b9)\
  2020-05-05 20:44:43 +0530
  * [MDEV-22461](https://jira.mariadb.org/browse/MDEV-22461): JOIN::make\_aggr\_tables\_info(): Assertion \`select\_options & (1ULL << 17)' failed.
* [Revision #cf52dd174e](https://github.com/MariaDB/server/commit/cf52dd174e)\
  2020-05-20 13:34:51 +0200
  * [MDEV-22545](https://jira.mariadb.org/browse/MDEV-22545): my\_vsnprintf behaves not as in C standard
* [Revision #d8e2fa0c49](https://github.com/MariaDB/server/commit/d8e2fa0c49)\
  2020-05-23 14:36:33 +0300
  * Fixed compiler failure on windows
* [Revision #be647ff14d](https://github.com/MariaDB/server/commit/be647ff14d)\
  2020-05-22 18:02:24 +0300
  * Fixed deadlock with LOCK TABLES and ALTER TABLE
* [Revision #6462af1c2e](https://github.com/MariaDB/server/commit/6462af1c2e)\
  2020-05-22 15:00:29 +0400
  * [MDEV-22111](https://jira.mariadb.org/browse/MDEV-22111) ERROR 1064 & 1033 and SIGSEGV on CREATE TABLE w/ various charsets on 10.4/5 optimized builds | Assertion \`(uint) (table\_check\_constraints - share->check\_constraints) == (uint) (share->table\_check\_constraints - share->field\_check\_constraints)' failed
* Merge [Revision #bdab5b667e](https://github.com/MariaDB/server/commit/bdab5b667e) 2020-05-22 14:22:45 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* Merge [Revision #450a5b33a2](https://github.com/MariaDB/server/commit/450a5b33a2) 2020-05-20 20:49:04 +0530 - [MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451): SIGSEGV in memmove\_avx\_unaligned\_erms/memcpy from \_my\_b\_write on CREATE after RESET MASTER
* [Revision #22a6fa572b](https://github.com/MariaDB/server/commit/22a6fa572b)\
  2020-05-20 15:57:15 +0300
  * [MDEV-19114](https://jira.mariadb.org/browse/MDEV-19114) post-push fix: SIGSEGV on INSERT
* [Revision #ed29782a03](https://github.com/MariaDB/server/commit/ed29782a03)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
* Merge [Revision #e380f44742](https://github.com/MariaDB/server/commit/e380f44742) 2020-05-20 11:13:40 +0300 - Merge 10.1 into 10.2
* [Revision #1893a1370d](https://github.com/MariaDB/server/commit/1893a1370d)\
  2020-05-20 13:34:45 +0530
  * [MDEV-22633](https://jira.mariadb.org/browse/MDEV-22633) Assertion failed in prepare\_inplace\_alter\_table\_dict
* [Revision #d2900d917f](https://github.com/MariaDB/server/commit/d2900d917f)\
  2020-05-20 17:10:07 +1000
  * [MDEV-22629](https://jira.mariadb.org/browse/MDEV-22629) Remove fts\_indexes field from struct fts\_update\_t (#1537)
* [Revision #dd95935e5b](https://github.com/MariaDB/server/commit/dd95935e5b)\
  2020-05-20 09:26:05 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456) post-fix: Remove unused variable
* [Revision #ad0f85bcd2](https://github.com/MariaDB/server/commit/ad0f85bcd2)\
  2020-05-19 10:10:30 +0300
  * [MDEV-18838](https://jira.mariadb.org/browse/MDEV-18838) : galera.galera\_toi\_truncate: Test failure: mysqltest: query 'reap' succeeded - should have failed with errno 1213
* [Revision #2c4a2f2007](https://github.com/MariaDB/server/commit/2c4a2f2007)\
  2020-05-19 15:15:52 +0000
  * [MDEV-22636](https://jira.mariadb.org/browse/MDEV-22636) XML output for mtr doesn't work with valgrind option
* [Revision #a8f044e1a4](https://github.com/MariaDB/server/commit/a8f044e1a4)\
  2020-05-19 16:02:00 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456): Fix cmake -DWITH\_INNODB\_AHI=OFF
* [Revision #cb437417d2](https://github.com/MariaDB/server/commit/cb437417d2)\
  2020-05-19 12:33:47 +0300
  * [MDEV-19114](https://jira.mariadb.org/browse/MDEV-19114) gcol.innodb\_virtual\_debug: Assertion n\_fields>0 failed
* [Revision #f9144a42e7](https://github.com/MariaDB/server/commit/f9144a42e7)\
  2020-05-19 12:54:42 +0300
  * Don't run main.sp2 in emebedded server
* [Revision #996b9a9d04](https://github.com/MariaDB/server/commit/996b9a9d04)\
  2020-05-19 13:30:42 +0400
  * [MDEV-22591](https://jira.mariadb.org/browse/MDEV-22591) Debug build crashes on EXECUTE IMMEDIATE '... WHERE ?' USING IGNORE
* [Revision #0f9bfcc323](https://github.com/MariaDB/server/commit/0f9bfcc323)\
  2020-05-13 14:32:12 +0300
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): "mariadb-backup --prepare" exits with code 0 even though innodb error is logged
* Merge [Revision #a84060567c](https://github.com/MariaDB/server/commit/a84060567c) 2020-05-19 10:42:59 +0300 - Merge 10.1 into 10.2
* [Revision #c93f8aca65](https://github.com/MariaDB/server/commit/c93f8aca65)\
  2020-05-19 10:21:16 +0300
  * [MDEV-22618](https://jira.mariadb.org/browse/MDEV-22618) Assertion !dict\_index\_is\_online\_ddl ... in lock\_table\_locks\_lookup
* [Revision #141cf43e61](https://github.com/MariaDB/server/commit/141cf43e61)\
  2020-05-18 21:49:07 +0300
  * Fixed assert in Aria on SHOW PROCEDURE STATUS
* [Revision #5b6bcb59ac](https://github.com/MariaDB/server/commit/5b6bcb59ac)\
  2020-05-18 14:04:31 +0300
  * [MDEV-22611](https://jira.mariadb.org/browse/MDEV-22611) Assertion btr\_search\_enabled failed during buffer pool resizing
* [Revision #f9d8571f38](https://github.com/MariaDB/server/commit/f9d8571f38)\
  2020-05-15 18:35:19 +0200
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): galera\_sst\_mariadb-backup fails with "Failed to start mysqld.2"
* Merge [Revision #d0e3b0eea6](https://github.com/MariaDB/server/commit/d0e3b0eea6) 2020-05-18 09:43:58 +0300 - Merge 10.1 into 10.2
* [Revision #c995090a53](https://github.com/MariaDB/server/commit/c995090a53)\
  2020-05-17 15:52:35 +0300
  * Travis-CI: Remove builds that always fail to make CI useful again
* [Revision #8d056affd8](https://github.com/MariaDB/server/commit/8d056affd8)\
  2020-04-05 23:55:23 +0300
  * Travis-CI: Shorten deb build log to keep it under 4 MB
* [Revision #9ddeccc299](https://github.com/MariaDB/server/commit/9ddeccc299)\
  2020-04-05 18:55:15 +0300
  * Travis-CI: Add missing build dependency dh-exec
* Merge [Revision #bf8ae81269](https://github.com/MariaDB/server/commit/bf8ae81269) 2020-05-16 10:52:08 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #3f12a5968a](https://github.com/MariaDB/server/commit/3f12a5968a)\
  2020-05-15 22:54:05 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Make test more robust
* Merge [Revision #fc0960aa96](https://github.com/MariaDB/server/commit/fc0960aa96) 2020-05-15 22:37:07 +0300 - Merge 10.1 into 10.2
* Merge [Revision #c8dd411781](https://github.com/MariaDB/server/commit/c8dd411781) 2020-05-15 22:18:11 +0300 - [MDEV-22544](https://jira.mariadb.org/browse/MDEV-22544) Inconsistent and Incorrect rw-lock stats
* [Revision #dcb0bd59ce](https://github.com/MariaDB/server/commit/dcb0bd59ce)\
  2020-05-14 15:05:36 +0800
  * [MDEV-22544](https://jira.mariadb.org/browse/MDEV-22544): Inconsistent and Incorrect rw-lock stats
* [Revision #ad6171b91c](https://github.com/MariaDB/server/commit/ad6171b91c)\
  2020-05-15 17:10:59 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456) Dropping the adaptive hash index may cause DDL to lock up InnoDB
* [Revision #ff66d65a09](https://github.com/MariaDB/server/commit/ff66d65a09)\
  2020-05-15 17:09:20 +0300
  * Amend af784385b4a2b286000fa2c658e34283fe7bba60: Avoid vtable overhead
* [Revision #1cac6d4828](https://github.com/MariaDB/server/commit/1cac6d4828)\
  2020-05-14 15:24:47 +0300
  * span cleanup
* [Revision #af784385b4](https://github.com/MariaDB/server/commit/af784385b4)\
  2020-05-15 14:20:43 +0300
  * Fix for using uninitialized memory
* [Revision #277aa85c9b](https://github.com/MariaDB/server/commit/277aa85c9b)\
  2020-05-15 10:44:05 +0300
  * Fixed bugs found by valgrind
* Merge [Revision #1b16572074](https://github.com/MariaDB/server/commit/1b16572074) 2020-05-14 17:48:06 +0300 - Merge 10.1 into 10.2
* [Revision #fc58c17216](https://github.com/MariaDB/server/commit/fc58c17216)\
  2020-05-14 12:06:25 +0300
  * [MDEV-21336](https://jira.mariadb.org/browse/MDEV-21336) Memory leaks related to innodb\_debug\_sync
* [Revision #a12aed0398](https://github.com/MariaDB/server/commit/a12aed0398)\
  2020-05-14 10:55:32 +0300
  * Fix GCC 9.3.0 -Wunused-but-set-variable
* [Revision #7d51c35988](https://github.com/MariaDB/server/commit/7d51c35988)\
  2020-05-14 09:06:38 +0300
  * Fix GCC -Wnonnull
* [Revision #11147bea20](https://github.com/MariaDB/server/commit/11147bea20)\
  2020-05-14 09:05:04 +0300
  * Fix GCC -Wstringop-truncation
* [Revision #3c773cd855](https://github.com/MariaDB/server/commit/3c773cd855)\
  2020-05-14 13:35:52 +0300
  * [MDEV-19622](https://jira.mariadb.org/browse/MDEV-19622): Fix a TokuDB result
* Merge [Revision #4dc690dc28](https://github.com/MariaDB/server/commit/4dc690dc28) 2020-05-14 11:57:47 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* Merge [Revision #f827ba3b84](https://github.com/MariaDB/server/commit/f827ba3b84) 2020-05-14 08:44:34 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #edbf124515](https://github.com/MariaDB/server/commit/edbf124515)\
  2020-05-13 23:30:34 +0300
  * Ensure that auto\_increment fields are marked properly on update
* Merge [Revision #6bc4444d7c](https://github.com/MariaDB/server/commit/6bc4444d7c) 2020-05-13 11:12:31 +0300 - Merge 10.1 into 10.2
* [Revision #218d20ffe3](https://github.com/MariaDB/server/commit/218d20ffe3)\
  2020-05-12 13:57:09 +0300
  * [MDEV-22398](https://jira.mariadb.org/browse/MDEV-22398): mariadb-backup.innodb\_xa\_rollback fails on repeat
* [Revision #0e6a5786d4](https://github.com/MariaDB/server/commit/0e6a5786d4)\
  2020-05-12 10:13:16 +0300
  * Cleanup: Remove InnoDB wrappers of thd\_charset(), thd\_query\_safe()
* [Revision #a2560b0077](https://github.com/MariaDB/server/commit/a2560b0077)\
  2020-05-12 10:13:00 +0300
  * [MDEV-22529](https://jira.mariadb.org/browse/MDEV-22529) thd\_query\_safe() isn’t, causing InnoDB to hang
* Merge [Revision #b57c6cb394](https://github.com/MariaDB/server/commit/b57c6cb394) 2020-05-11 19:53:35 +0200 - Merge branch '10.2-release' into 10.2
* [Revision #37759b262f](https://github.com/MariaDB/server/commit/37759b262f)\
  2020-05-11 12:55:06 -0400
  * bump the VERSION
* [Revision #ba3d58ad4c](https://github.com/MariaDB/server/commit/ba3d58ad4c)\
  2020-05-11 14:23:37 +0300
  * [MDEV-22523](https://jira.mariadb.org/browse/MDEV-22523) index->rtr\_ssn.mutex is wasting memory
* [Revision #4ae778bbec](https://github.com/MariaDB/server/commit/4ae778bbec)\
  2020-05-04 17:39:50 +0200
  * innodb: add space between thread name and "to exit" text
* [Revision #faf6f8c6a4](https://github.com/MariaDB/server/commit/faf6f8c6a4)\
  2020-05-08 16:39:37 +0300
  * Add global suppression for connectivity problems.
* [Revision #0b218df072](https://github.com/MariaDB/server/commit/0b218df072)\
  2020-05-08 14:11:41 +0200
  * [MDEV-22483](https://jira.mariadb.org/browse/MDEV-22483) mysql\_upgrade does not use current user as default for connecting to server
* [Revision #748fb55093](https://github.com/MariaDB/server/commit/748fb55093)\
  2020-05-08 11:35:15 +0300
  * [MDEV-21483](https://jira.mariadb.org/browse/MDEV-21483) : Galera MTR tests failed: galera.MW-328A galera.MW-328B
* [Revision #40d0b64167](https://github.com/MariaDB/server/commit/40d0b64167)\
  2020-05-08 09:13:47 +0300
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #0dee57c6f5](https://github.com/MariaDB/server/commit/0dee57c6f5)\
  2020-05-07 21:01:22 +0300
  * [MDEV-19344](https://jira.mariadb.org/browse/MDEV-19344) innodb.innodb-change-buffer-recovery fails
* [Revision #e6301d8f67](https://github.com/MariaDB/server/commit/e6301d8f67)\
  2020-05-06 17:23:49 +0300
  * [MDEV-21515](https://jira.mariadb.org/browse/MDEV-21515) : Galera test sporadic failure on galera.galera\_wsrep\_new\_cluster: Result content mismatch
* [Revision #2907ff2c2d](https://github.com/MariaDB/server/commit/2907ff2c2d)\
  2020-04-29 17:19:54 +0300
  * [MDEV-19741](https://jira.mariadb.org/browse/MDEV-19741) : Galera test failure on galera.galera\_sst\_mariadb-backup\_table\_options
* [Revision #06b245f768](https://github.com/MariaDB/server/commit/06b245f768)\
  2020-05-05 15:35:58 +0530
  * [MDEV-13266](https://jira.mariadb.org/browse/MDEV-13266): Race condition in ANALYZE TABLE / statistics collection
* [Revision #b9f177f66a](https://github.com/MariaDB/server/commit/b9f177f66a)\
  2020-05-05 08:54:33 +0300
  * [MDEV-11254](https://jira.mariadb.org/browse/MDEV-11254) cleanup: Remove buf\_page\_t::write\_size

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
