# MariaDB 10.5.9 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.9](https://downloads.mariadb.org/mariadb/10.5.9/)[Release Notes](../../old-releases/10.5/10.5.9.md)[Changelog](mariadb-1059-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.9/)

**Release date:** 22 Feb 2021

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.9.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.18](../changelogs-mariadb-10-4-series/mariadb-10418-changelog.md)
* Merge [Revision #3a8ca9096e](https://github.com/MariaDB/server/commit/3a8ca9096e) 2021-02-19 10:37:25 +0100 - Merge branch 'bb-10.4-release' into bb-10.5-release
* [Revision #93522bc9a9](https://github.com/MariaDB/server/commit/93522bc9a9)\
  2021-02-18 18:20:50 +0200
  * [MDEV-24917](https://jira.mariadb.org/browse/MDEV-24917) Page cleaner wrongly remains idle
* [Revision #9d7dc1f6d0](https://github.com/MariaDB/server/commit/9d7dc1f6d0)\
  2021-02-16 16:47:04 +0200
  * List of unstable tests for 10.5.9 release
* [Revision #ae7989ca20](https://github.com/MariaDB/server/commit/ae7989ca20)\
  2021-02-16 01:11:41 +0100
  * galera.galera\_gra\_log crashes
* [Revision #638ede5bef](https://github.com/MariaDB/server/commit/638ede5bef)\
  2021-02-15 09:37:01 +0200
  * [MDEV-24864](https://jira.mariadb.org/browse/MDEV-24864) Fatal error in buf\_page\_get\_low() / fseg\_page\_is\_free()
* [Revision #f13f966304](https://github.com/MariaDB/server/commit/f13f966304)\
  2021-02-15 16:46:32 +0100
  * update PCRE2 ref
* [Revision #a89b7c1d6a](https://github.com/MariaDB/server/commit/a89b7c1d6a)\
  2021-02-15 16:44:37 +0100
  * columnstore 5.5.1-2
* Merge [Revision #25d9d2e37f](https://github.com/MariaDB/server/commit/25d9d2e37f) 2021-02-15 16:43:15 +0100 - Merge branch 'bb-10.4-release' into bb-10.5-release
* [Revision #5e3d3220bb](https://github.com/MariaDB/server/commit/5e3d3220bb)\
  2021-02-08 16:42:18 +1100
  * [MDEV-24344](https://jira.mariadb.org/browse/MDEV-24344): BINLOG REPLAY privilege is missing from SHOW PRIVILEGES
* [Revision #ffc5d06489](https://github.com/MariaDB/server/commit/ffc5d06489)\
  2021-02-08 21:03:04 +0200
  * [MDEV-24087](https://jira.mariadb.org/browse/MDEV-24087) s3.replication\_partition fails in buildbot wiht replication failure
* [Revision #bd5ac03896](https://github.com/MariaDB/server/commit/bd5ac03896)\
  2021-02-05 15:48:45 +0200
  * Make maria\_data\_root const char\*
* [Revision #5d6ad2ad66](https://github.com/MariaDB/server/commit/5d6ad2ad66)\
  2021-02-05 14:57:46 +0200
  * Added 'const' to arguments in get\_one\_option and find\_typeset()
* [Revision #e30a3048da](https://github.com/MariaDB/server/commit/e30a3048da)\
  2021-02-07 21:11:53 +0200
  * Ensure that mysqlbinlog frees all memory at exit
* [Revision #4f4a4cf9eb](https://github.com/MariaDB/server/commit/4f4a4cf9eb)\
  2021-02-07 12:19:24 +0200
  * [MDEV-23399](https://jira.mariadb.org/browse/MDEV-23399) fixup: Use plain pthread\_cond
* [Revision #7ce643782b](https://github.com/MariaDB/server/commit/7ce643782b)\
  2021-02-07 12:11:16 +0200
  * [MDEV-23379](https://jira.mariadb.org/browse/MDEV-23379) fixup: Remove dead PERFORMANCE\_SCHEMA code
* [Revision #eacefbca35](https://github.com/MariaDB/server/commit/eacefbca35)\
  2021-02-01 18:46:34 +0200
  * [MDEV-24750](https://jira.mariadb.org/browse/MDEV-24750) Various corruptions caused by Aria subsystem...
* [Revision #b76e5c6610](https://github.com/MariaDB/server/commit/b76e5c6610)\
  2021-02-02 18:16:16 +0530
  * [MDEV-24765](https://jira.mariadb.org/browse/MDEV-24765) fseg\_free\_extent fails to call buf\_page\_free() for the whole segment
* [Revision #b5dab19efa](https://github.com/MariaDB/server/commit/b5dab19efa)\
  2021-02-02 00:05:41 +0100
  * [MDEV-24757](https://jira.mariadb.org/browse/MDEV-24757) : fix potential null pointer dereference in I\_S.thread\_pool\_queues
* [Revision #e2c571ad84](https://github.com/MariaDB/server/commit/e2c571ad84)\
  2021-01-28 12:59:40 +0100
  * [MDEV-24498](https://jira.mariadb.org/browse/MDEV-24498) mysql\_config reports wrong libs for libmysqld
* [Revision #324e5f02a9](https://github.com/MariaDB/server/commit/324e5f02a9)\
  2021-02-01 18:43:07 +0200
  * [MDEV-24754](https://jira.mariadb.org/browse/MDEV-24754) Crash in ha\_partition\_inplace\_ctx::ha\_partition\_inplace\_ctx()
* [Revision #b1241585b2](https://github.com/MariaDB/server/commit/b1241585b2)\
  2021-01-30 15:04:27 +0000
  * Mac M1 build support proposal (minus rocksdb option) (#1743)
* [Revision #52795c2f78](https://github.com/MariaDB/server/commit/52795c2f78)\
  2020-12-29 10:33:06 +0100
  * Apple Silicon is a 64-bit platform
* [Revision #73c43ee9ed](https://github.com/MariaDB/server/commit/73c43ee9ed)\
  2021-01-30 00:54:21 +0300
  * [MDEV-24739](https://jira.mariadb.org/browse/MDEV-24739): Assertion \`root->weight >= ...' failed in SEL\_ARG::tree\_delete
* [Revision #a70a47f2f3](https://github.com/MariaDB/server/commit/a70a47f2f3)\
  2021-01-29 18:03:20 +0200
  * [MDEV-24661](https://jira.mariadb.org/browse/MDEV-24661): Remove the test innodb.innodb\_wl6326\_big
* [Revision #d8373fea5f](https://github.com/MariaDB/server/commit/d8373fea5f)\
  2021-01-27 14:17:43 +0100
  * [MDEV-24685](https://jira.mariadb.org/browse/MDEV-24685) - remove IO thread states output from SHOW ENGINE INNODB STATUS
* [Revision #c36720388d](https://github.com/MariaDB/server/commit/c36720388d)\
  2021-01-28 21:43:55 +0300
  * [MDEV-9750](https://jira.mariadb.org/browse/MDEV-9750): Quick memory exhaustion with 'extended\_keys=on' ...
* [Revision #a2eb974b50](https://github.com/MariaDB/server/commit/a2eb974b50)\
  2021-01-28 16:12:35 +0200
  * [MDEV-24721](https://jira.mariadb.org/browse/MDEV-24721) galera.mysql-wsrep-bugs-607 test failure
* [Revision #85130c5a4f](https://github.com/MariaDB/server/commit/85130c5a4f)\
  2021-01-20 21:59:51 +0100
  * [MDEV-24093](https://jira.mariadb.org/browse/MDEV-24093): Detect during mysql\_upgrade if type\_mysql\_json.so is needed and load it
* [Revision #6d1f1b61b5](https://github.com/MariaDB/server/commit/6d1f1b61b5)\
  2021-01-28 14:15:01 +0200
  * [MDEV-24564](https://jira.mariadb.org/browse/MDEV-24564) Statistics are lost after ALTER TABLE
* [Revision #744e9752d8](https://github.com/MariaDB/server/commit/744e9752d8)\
  2021-01-27 13:59:51 +0300
  * [MDEV-24705](https://jira.mariadb.org/browse/MDEV-24705) add check that LSN of the last skipped log record equals to FIL\_PAGE\_LSN field
* [Revision #6e80a34d68](https://github.com/MariaDB/server/commit/6e80a34d68)\
  2021-01-27 16:24:37 +0530
  * [MDEV-24695](https://jira.mariadb.org/browse/MDEV-24695) Encryption modifies a freed page
* [Revision #c6308355e5](https://github.com/MariaDB/server/commit/c6308355e5)\
  2021-01-28 07:51:43 +0200
  * [MDEV-24612](https://jira.mariadb.org/browse/MDEV-24612) fixup: Skip the test for --embedded
* [Revision #700ae20d45](https://github.com/MariaDB/server/commit/700ae20d45)\
  2021-01-26 20:09:39 +0530
  * [MDEV-24693](https://jira.mariadb.org/browse/MDEV-24693) LeakSanitizer: detected memory leaks in mem\_heap\_create\_block\_func / fts\_optimize\_create\_msg
* [Revision #30379d906b](https://github.com/MariaDB/server/commit/30379d906b)\
  2021-01-27 14:16:47 +0200
  * Update disabled.def in suites \* galera \* galera\_sr \* galera\_3nodes
* [Revision #e2bcf68279](https://github.com/MariaDB/server/commit/e2bcf68279)\
  2021-01-13 10:58:02 +0200
  * [MDEV-24010](https://jira.mariadb.org/browse/MDEV-24010) : galera\_3nodes.GCF-354 MTR fails : WSREP has not yet prepared node for application use
* [Revision #0565d19973](https://github.com/MariaDB/server/commit/0565d19973)\
  2021-01-26 09:36:18 +0000
  * [MDEV-24298](https://jira.mariadb.org/browse/MDEV-24298) Select Handler now process INSERT..SELECT with a single derived at the top level
* Merge [Revision #927a882341](https://github.com/MariaDB/server/commit/927a882341) 2021-01-25 15:06:52 +0200 - Merge 10.4 into 10.5
* Merge [Revision #961c7938bb](https://github.com/MariaDB/server/commit/961c7938bb) 2021-01-25 12:44:24 +0200 - Merge 10.4 into 10.5
* [Revision #5adcb2e7b8](https://github.com/MariaDB/server/commit/5adcb2e7b8)\
  2021-01-23 17:56:50 +0200
  * [MDEV-24661](https://jira.mariadb.org/browse/MDEV-24661): Disable an unstable test
* [Revision #84b8f529c7](https://github.com/MariaDB/server/commit/84b8f529c7)\
  2021-01-23 17:45:03 +0200
  * [MDEV-24659](https://jira.mariadb.org/browse/MDEV-24659) Assertion !fsp\_is\_system\_temporary(bpage->id().space()) failed in buf\_flush\_relocate\_on\_flush\_list()
* [Revision #bf1f9b59c7](https://github.com/MariaDB/server/commit/bf1f9b59c7)\
  2021-01-21 18:32:48 +0530
  * [MDEV-24638](https://jira.mariadb.org/browse/MDEV-24638) Avoid repetitive FTS SYNC request for table
* [Revision #816808d6c9](https://github.com/MariaDB/server/commit/816808d6c9)\
  2021-01-22 14:58:49 +0530
  * [MDEV-24652](https://jira.mariadb.org/browse/MDEV-24652) mtr fails while reusing the cached undo log block
* [Revision #6eb1eed53f](https://github.com/MariaDB/server/commit/6eb1eed53f)\
  2021-01-21 16:25:59 +0200
  * [MDEV-24452](https://jira.mariadb.org/browse/MDEV-24452) ALTER TABLE event take infinite time which for example breaks mysql\_upgrade
* [Revision #9930cb22c7](https://github.com/MariaDB/server/commit/9930cb22c7)\
  2021-01-18 23:17:04 +0300
  * [MDEV-24612](https://jira.mariadb.org/browse/MDEV-24612): innodb hangs if it's initialization is broken before encryption threads are started
* [Revision #7c052cdf0b](https://github.com/MariaDB/server/commit/7c052cdf0b)\
  2021-01-17 13:20:35 +0100
  * cmake warning, if/endif mismatch
* [Revision #a5b54f78a7](https://github.com/MariaDB/server/commit/a5b54f78a7)\
  2021-01-15 17:53:11 +0200
  * Code cleanups - Fix long lines to be <= 80 character - Trivial changes (no logic changes)
* [Revision #9a60e89a90](https://github.com/MariaDB/server/commit/9a60e89a90)\
  2020-12-14 15:27:07 +0200
  * Fixed some possible usage of freed memory
* [Revision #76b58c2af7](https://github.com/MariaDB/server/commit/76b58c2af7)\
  2021-01-15 13:36:32 +0200
  * [MDEV-24600](https://jira.mariadb.org/browse/MDEV-24600) performance\_schema.events\_transactions\_history\_long.trx\_id reports garbage
* [Revision #d79141d641](https://github.com/MariaDB/server/commit/d79141d641)\
  2021-01-10 23:54:40 +0000
  * msys: detects crc/cryptosupport on FreeBSD/arm
* [Revision #dc3681e5ed](https://github.com/MariaDB/server/commit/dc3681e5ed)\
  2020-12-06 19:48:11 +0000
  * Implement CPU feature checks for FreeBSD/powerpc64
* [Revision #deadec4e68](https://github.com/MariaDB/server/commit/deadec4e68)\
  2021-01-14 14:26:24 +0200
  * [MDEV-24569](https://jira.mariadb.org/browse/MDEV-24569): Change buffer merge modifies freed page
* [Revision #e4205fba7c](https://github.com/MariaDB/server/commit/e4205fba7c)\
  2021-01-13 19:11:31 +0200
  * [MDEV-24536](https://jira.mariadb.org/browse/MDEV-24536) innodb\_idle\_flush\_pct has no effect
* [Revision #2c845e0bd6](https://github.com/MariaDB/server/commit/2c845e0bd6)\
  2020-12-29 21:49:27 +0100
  * deb: relax server version dependencies for non-storage-engine plugins
* [Revision #0d2623d030](https://github.com/MariaDB/server/commit/0d2623d030)\
  2020-12-28 15:00:01 +0100
  * deb: remove i386 from Build-Depends of ColumnStore
* [Revision #81cb3e7934](https://github.com/MariaDB/server/commit/81cb3e7934)\
  2020-11-30 15:27:08 +0100
  * [MDEV-24292](https://jira.mariadb.org/browse/MDEV-24292) support semi-independent versioning for sub-packages
* [Revision #fbc171333e](https://github.com/MariaDB/server/commit/fbc171333e)\
  2020-11-27 14:36:10 +0100
  * [MDEV-24292](https://jira.mariadb.org/browse/MDEV-24292) support semi-independent versioning for sub-packages
* [Revision #5c53576c7b](https://github.com/MariaDB/server/commit/5c53576c7b)\
  2020-11-27 15:05:17 +0100
  * deb: use ${server:Version} for the version of the server package
* [Revision #78806be6d3](https://github.com/MariaDB/server/commit/78806be6d3)\
  2020-11-26 18:58:10 +0100
  * [MDEV-24292](https://jira.mariadb.org/browse/MDEV-24292) support semi-independent versioning for sub-packages
* [Revision #64d2849b3e](https://github.com/MariaDB/server/commit/64d2849b3e)\
  2020-11-26 17:56:02 +0100
  * [MDEV-24292](https://jira.mariadb.org/browse/MDEV-24292) support semi-independent versioning for sub-packages
* Merge [Revision #8de233af81](https://github.com/MariaDB/server/commit/8de233af81) 2021-01-11 16:29:51 +0200 - Merge 10.4 into 10.5
* [Revision #1015cbde59](https://github.com/MariaDB/server/commit/1015cbde59)\
  2021-01-11 09:02:36 +1100
  * [MDEV-24556](https://jira.mariadb.org/browse/MDEV-24556): Build does not recognize powerpc64 (OpenBSD)
* [Revision #49b8774951](https://github.com/MariaDB/server/commit/49b8774951)\
  2021-01-09 09:03:39 +0200
  * [MDEV-24546](https://jira.mariadb.org/browse/MDEV-24546) : AddressSanitizer: initialization-order-fiasco on address ... in Sys\_var\_integer from static\_initialization\_and\_destruction\_0, possibly inside global var wsrep\_gtid\_server
* [Revision #fae87e0c74](https://github.com/MariaDB/server/commit/fae87e0c74)\
  2021-01-07 11:18:13 +0200
  * [MDEV-24544](https://jira.mariadb.org/browse/MDEV-24544) innodb\_buffer\_pool\_wait\_free is not protected by mutex
* [Revision #a993310593](https://github.com/MariaDB/server/commit/a993310593)\
  2021-01-06 13:53:14 +0200
  * [MDEV-24537](https://jira.mariadb.org/browse/MDEV-24537) innodb\_max\_dirty\_pages\_pct\_lwm=0 lost its special meaning
* Merge [Revision #02e7bff882](https://github.com/MariaDB/server/commit/02e7bff882) 2021-01-06 10:53:00 +0100 - Merge commit '10.4' into 10.5
* [Revision #5f10870c8a](https://github.com/MariaDB/server/commit/5f10870c8a)\
  2021-01-04 17:34:17 +0200
  * [MDEV-24480](https://jira.mariadb.org/browse/MDEV-24480) Added wait condition to make sure table t1 is replicated to node\_2.
* [Revision #2072738743](https://github.com/MariaDB/server/commit/2072738743)\
  2020-12-26 20:34:15 +0200
  * Deb: Ignore Lintian error on ColumnStore libjemalloc.so inclusion
* [Revision #ae185f393c](https://github.com/MariaDB/server/commit/ae185f393c)\
  2020-12-26 21:17:11 +0200
  * Salsa-CI: Use aptitude to resolve build dependencies
* [Revision #09b1695b41](https://github.com/MariaDB/server/commit/09b1695b41)\
  2020-12-21 09:02:58 +0200
  * Travis-CI: Sync dependencies with Debian
* [Revision #fa9bd07305](https://github.com/MariaDB/server/commit/fa9bd07305)\
  2020-10-04 12:57:48 +0300
  * Deb: Revert emptying /etc/mysql/debian.cnf on upgrades
* [Revision #af8fa245a1](https://github.com/MariaDB/server/commit/af8fa245a1)\
  2020-12-20 23:29:29 +0200
  * Deb: Sync misc changes from downstream Debian
* [Revision #a3448b2395](https://github.com/MariaDB/server/commit/a3448b2395)\
  2020-12-20 23:13:50 +0200
  * Deb: Fix upgrade from Percona.com by ensuring server uses mariadb.cnf
* [Revision #ea56841997](https://github.com/MariaDB/server/commit/ea56841997)\
  2020-12-25 17:41:03 +0200
  * Deb: Make dependencies and debian/rules cross-compile compatible
* [Revision #ff36394ccc](https://github.com/MariaDB/server/commit/ff36394ccc)\
  2020-09-21 19:31:38 +0300
  * Deb: Correct documentation about systemd using debian-start
* [Revision #16876e47d8](https://github.com/MariaDB/server/commit/16876e47d8)\
  2020-10-06 22:39:32 +0300
  * Deb: Unify config file syntax style
* [Revision #1bf9acceef](https://github.com/MariaDB/server/commit/1bf9acceef)\
  2021-01-01 19:17:03 +0200
  * [MDEV-20386](https://jira.mariadb.org/browse/MDEV-20386): Allow RDRAND, RDSEED WITH\_MSAN
* [Revision #c1f0afb102](https://github.com/MariaDB/server/commit/c1f0afb102)\
  2021-01-01 19:15:46 +0200
  * WolfSSL v4.6.0-stable
* [Revision #139c85aafd](https://github.com/MariaDB/server/commit/139c85aafd)\
  2020-10-15 01:47:26 +0300
  * Travis-CI: Optimize rate of false negatives vs true failures
* [Revision #7a60bc22fc](https://github.com/MariaDB/server/commit/7a60bc22fc)\
  2020-12-22 14:56:44 +0200
  * Deb: Remove PLUGIN\_COLUMNSTORE=YES, it will build by default anyway
* [Revision #deecc75a02](https://github.com/MariaDB/server/commit/deecc75a02)\
  2020-12-22 14:15:49 +0200
  * Fix commit 113f18686d0 and d1809097966: PLUGIN\_COLUMNSTORE=NO by default
* Merge [Revision #b6be78d4e5](https://github.com/MariaDB/server/commit/b6be78d4e5) 2020-12-23 15:07:36 +0200 - Merge 10.4 into 10.5
* [Revision #ed5d675c75](https://github.com/MariaDB/server/commit/ed5d675c75)\
  2020-12-22 16:42:33 +0300
  * [MDEV-24364](https://jira.mariadb.org/browse/MDEV-24364) Alter rename table does not remove PFS share
* [Revision #113f18686d](https://github.com/MariaDB/server/commit/113f18686d)\
  2020-12-21 23:20:56 +0200
  * Fix previous commit: PLUGIN\_COLUMNSTORE=YES can only be active on amd64
* [Revision #ecb1b8721b](https://github.com/MariaDB/server/commit/ecb1b8721b)\
  2020-08-23 23:49:43 +0300
  * Salsa-CI: Copy most of Salsa-CI from Debian 10.5
* [Revision #d180909796](https://github.com/MariaDB/server/commit/d180909796)\
  2020-12-21 10:43:16 +0200
  * Deb: Don't build ColumnStore in native builds, only in autobake-deb.sh
* [Revision #e7c7f5c1bb](https://github.com/MariaDB/server/commit/e7c7f5c1bb)\
  2020-12-20 22:33:11 +0200
  * Deb: Run 'wrap-and-sort -av' to debian/ contents is easier to compare
* [Revision #39378e1366](https://github.com/MariaDB/server/commit/39378e1366)\
  2020-12-21 14:40:33 +0200
  * [MDEV-24448](https://jira.mariadb.org/browse/MDEV-24448) srv\_start(): Assertion !buf\_pool.any\_io\_pending()
* [Revision #6529cba2e2](https://github.com/MariaDB/server/commit/6529cba2e2)\
  2020-11-26 17:30:00 +0100
  * cleanup: plugin.cmake
* [Revision #4fae7b7a3e](https://github.com/MariaDB/server/commit/4fae7b7a3e)\
  2020-12-15 10:22:20 +0100
  * [MDEV-24346](https://jira.mariadb.org/browse/MDEV-24346) valgrind error in main.precedence
* [Revision #5b90970e87](https://github.com/MariaDB/server/commit/5b90970e87)\
  2020-12-11 11:28:54 +0100
  * increase INET6 plugin maturity
* [Revision #b5174eca7b](https://github.com/MariaDB/server/commit/b5174eca7b)\
  2020-12-09 14:09:59 +0100
  * cleanup: DBUG\_ASSERT && log.cc
* [Revision #e87a8efd32](https://github.com/MariaDB/server/commit/e87a8efd32)\
  2020-12-21 10:48:51 +0200
  * [MDEV-24455](https://jira.mariadb.org/browse/MDEV-24455) Assertion \`!m\_freed\_space' failed in mtr\_t::start
* [Revision #0c23e32d27](https://github.com/MariaDB/server/commit/0c23e32d27)\
  2020-12-18 17:12:57 +0200
  * [MDEV-24445](https://jira.mariadb.org/browse/MDEV-24445) Using innodb\_undo\_tablespaces corrupts system tablespace
* [Revision #cd093d79f9](https://github.com/MariaDB/server/commit/cd093d79f9)\
  2020-12-18 16:53:45 +0200
  * [MDEV-24442](https://jira.mariadb.org/browse/MDEV-24442) Assertion space->referenced() failed in fil\_crypt\_space\_needs\_rotation
* [Revision #a1974d1991](https://github.com/MariaDB/server/commit/a1974d1991)\
  2020-12-18 10:00:57 +0200
  * [MDEV-24426](https://jira.mariadb.org/browse/MDEV-24426) fixup: Assertion failure on shutdown
* [Revision #1fe3dd003a](https://github.com/MariaDB/server/commit/1fe3dd003a)\
  2020-12-17 13:46:21 +0200
  * [MDEV-24426](https://jira.mariadb.org/browse/MDEV-24426) fil\_crypt\_thread keep spinning even if innodb\_encryption\_rotate\_key\_age=0
* [Revision #6bb3949eb3](https://github.com/MariaDB/server/commit/6bb3949eb3)\
  2020-10-26 11:10:46 +0100
  * Contain AIX perror
* [Revision #2ce48f0678](https://github.com/MariaDB/server/commit/2ce48f0678)\
  2020-10-26 10:08:14 +0100
  * Fix build on GCC 5
* [Revision #a6e90992c1](https://github.com/MariaDB/server/commit/a6e90992c1)\
  2020-09-14 10:56:36 +0200
  * Add LARGE\_FILES flag for GCC AIX build
* [Revision #4fade4da6c](https://github.com/MariaDB/server/commit/4fade4da6c)\
  2020-09-11 17:00:38 +0200
  * Add -berok for head test on AIX
* [Revision #2dee6a74b2](https://github.com/MariaDB/server/commit/2dee6a74b2)\
  2020-09-11 17:00:09 +0200
  * Parse GSSAPI flags on AIX
* [Revision #1d7fc7280e](https://github.com/MariaDB/server/commit/1d7fc7280e)\
  2020-09-11 16:18:34 +0200
  * Add flags for AIX build
* [Revision #b23e545773](https://github.com/MariaDB/server/commit/b23e545773)\
  2020-09-11 16:05:57 +0200
  * Remove -Werror for AIX
* [Revision #1a49619a4c](https://github.com/MariaDB/server/commit/1a49619a4c)\
  2020-09-11 16:04:59 +0200
  * AIX workaround for GCC include bug
* [Revision #2c7247622a](https://github.com/MariaDB/server/commit/2c7247622a)\
  2020-09-11 16:02:58 +0200
  * AIX workaround for GCC TOC bug
* [Revision #77d7de8d47](https://github.com/MariaDB/server/commit/77d7de8d47)\
  2020-09-11 15:58:49 +0200
  * Support of AIX for auth\_socket plugin
* [Revision #2f5d372444](https://github.com/MariaDB/server/commit/2f5d372444)\
  2020-01-31 14:37:44 +0100
  * Add build on AIX
* [Revision #ee69c153d9](https://github.com/MariaDB/server/commit/ee69c153d9)\
  2020-12-08 16:28:16 +0800
  * [MDEV-24366](https://jira.mariadb.org/browse/MDEV-24366) Use environment variables as S3 test case variables
* [Revision #e4c2589517](https://github.com/MariaDB/server/commit/e4c2589517)\
  2020-12-14 19:50:45 +0200
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) Update Galera disabled.def file
* [Revision #e8217d070f](https://github.com/MariaDB/server/commit/e8217d070f)\
  2020-12-14 18:01:30 +0200
  * [MDEV-24313](https://jira.mariadb.org/browse/MDEV-24313) fixup: GCC 8 -Wconversion
* [Revision #2c226e01a8](https://github.com/MariaDB/server/commit/2c226e01a8)\
  2020-12-14 17:20:53 +0200
  * [MDEV-24313](https://jira.mariadb.org/browse/MDEV-24313) fixup: GCC -Wparentheses
* [Revision #f24b738318](https://github.com/MariaDB/server/commit/f24b738318)\
  2020-12-14 15:27:03 +0200
  * [MDEV-24313](https://jira.mariadb.org/browse/MDEV-24313) (2 of 2): Silently ignored innodb\_use\_native\_aio=1
* [Revision #17d3f8560b](https://github.com/MariaDB/server/commit/17d3f8560b)\
  2020-12-14 13:11:44 +0200
  * [MDEV-24313](https://jira.mariadb.org/browse/MDEV-24313) (1 of 2): Hang with innodb\_write\_io\_threads=1
* [Revision #8677c14e65](https://github.com/MariaDB/server/commit/8677c14e65)\
  2020-12-11 09:05:26 +0200
  * [MDEV-24391](https://jira.mariadb.org/browse/MDEV-24391) heap-use-after-free in fil\_space\_t::flush\_low()
* [Revision #0c7c449267](https://github.com/MariaDB/server/commit/0c7c449267)\
  2020-12-09 16:49:52 +0200
  * Remove unused DBUG\_EXECUTE\_IF "ignore\_punch\_hole"
* [Revision #5eb539555b](https://github.com/MariaDB/server/commit/5eb539555b)\
  2020-12-09 09:22:13 +0200
  * [MDEV-12227](https://jira.mariadb.org/browse/MDEV-12227) Defer writes to the InnoDB temporary tablespace
* [Revision #ea21d630be](https://github.com/MariaDB/server/commit/ea21d630be)\
  2020-12-08 19:05:08 +0200
  * Fix -Wunused-but-set-variable
* [Revision #f0c295e2de](https://github.com/MariaDB/server/commit/f0c295e2de)\
  2020-12-08 14:57:51 +0200
  * [MDEV-24369](https://jira.mariadb.org/browse/MDEV-24369) Page cleaner sleeps despite innodb\_max\_dirty\_pages\_pct\_lwm being exceeded
* [Revision #6859e80df7](https://github.com/MariaDB/server/commit/6859e80df7)\
  2020-12-08 16:51:14 +0300
  * [MDEV-24351](https://jira.mariadb.org/browse/MDEV-24351): S3, same-backend replication: Dropping a table on master...
* [Revision #3ee24b2306](https://github.com/MariaDB/server/commit/3ee24b2306)\
  2020-12-07 10:35:57 +0100
  * Simplify clang workarounds.
* [Revision #83591a23d6](https://github.com/MariaDB/server/commit/83591a23d6)\
  2020-12-04 17:52:23 +0200
  * [MDEV-24350](https://jira.mariadb.org/browse/MDEV-24350) buf\_dblwr unnecessarily uses memory-intensive srv\_stats counters
* [Revision #aa0e380568](https://github.com/MariaDB/server/commit/aa0e380568)\
  2020-12-04 14:11:48 +0200
  * [MDEV-24348](https://jira.mariadb.org/browse/MDEV-24348) InnoDB shutdown hang with innodb\_flush\_sync=0
* [Revision #6033cc8587](https://github.com/MariaDB/server/commit/6033cc8587)\
  2020-12-03 15:46:59 +0200
  * Fixed usage of not initialized memory in LIKE ... ESCAPE
* [Revision #f146969fb3](https://github.com/MariaDB/server/commit/f146969fb3)\
  2020-12-03 07:45:48 +0200
  * [MDEV-22929](https://jira.mariadb.org/browse/MDEV-22929) fixup: root\_name() clash with clang++
* [Revision #f3a58ed801](https://github.com/MariaDB/server/commit/f3a58ed801)\
  2020-12-02 22:04:57 +0200
  * [MDEV-24295](https://jira.mariadb.org/browse/MDEV-24295): Fix the non-clang build
* [Revision #4174fc1a1b](https://github.com/MariaDB/server/commit/4174fc1a1b)\
  2020-12-02 21:46:01 +0200
  * [MDEV-24295](https://jira.mariadb.org/browse/MDEV-24295): Fix the WITH\_MSAN build
* [Revision #9b725f9aef](https://github.com/MariaDB/server/commit/9b725f9aef)\
  2020-12-02 21:28:18 +0200
  * [MDEV-20051](https://jira.mariadb.org/browse/MDEV-20051) fixup: Correct galera.galera\_defaults result
* Merge [Revision #6a1e655cb0](https://github.com/MariaDB/server/commit/6a1e655cb0) 2020-12-02 18:29:49 +0200 - Merge 10.4 into 10.5
* [Revision #e76e12886f](https://github.com/MariaDB/server/commit/e76e12886f)\
  2020-12-01 12:04:32 +0200
  * [MDEV-21962](https://jira.mariadb.org/browse/MDEV-21962) fixup: Remove buf\_pool\_contains\_zip()
* [Revision #1435f35bda](https://github.com/MariaDB/server/commit/1435f35bda)\
  2020-11-27 01:09:11 +0100
  * Clarify some comments.
* [Revision #5bb5d4ad3a](https://github.com/MariaDB/server/commit/5bb5d4ad3a)\
  2020-11-26 23:31:42 +0100
  * [MDEV-24295](https://jira.mariadb.org/browse/MDEV-24295) Reduce wakeups by tpool maintenance timer, when server is idle
* [Revision #111963477b](https://github.com/MariaDB/server/commit/111963477b)\
  2020-11-30 15:19:25 +0300
  * Make LEX::print support single-table DELETE.
* [Revision #e34e53b554](https://github.com/MariaDB/server/commit/e34e53b554)\
  2020-11-30 13:59:20 +0200
  * [MDEV-24308](https://jira.mariadb.org/browse/MDEV-24308): Revert for Windows
* [Revision #8fa6e36375](https://github.com/MariaDB/server/commit/8fa6e36375)\
  2020-11-30 11:15:31 +0200
  * [MDEV-24308](https://jira.mariadb.org/browse/MDEV-24308): Remove some os\_thread\_ functions
* [Revision #b92391d5b1](https://github.com/MariaDB/server/commit/b92391d5b1)\
  2020-11-24 20:05:54 -0800
  * [MDEV-24242](https://jira.mariadb.org/browse/MDEV-24242) Query returns wrong result while using big\_tables=1
* [Revision #1555c6d125](https://github.com/MariaDB/server/commit/1555c6d125)\
  2020-11-26 12:40:41 +0200
  * Fixed compiler warnings from crc32c.cc
* [Revision #279b5f87de](https://github.com/MariaDB/server/commit/279b5f87de)\
  2020-11-24 16:45:26 +0200
  * Avoid some DBUG prints from idle server in thread pool
* [Revision #55f734ed87](https://github.com/MariaDB/server/commit/55f734ed87)\
  2020-11-24 16:44:51 +0200
  * Change to LONGLONG\_BUFFER\_SIZE usage to avoid extra mallocs
* [Revision #c8992fc35b](https://github.com/MariaDB/server/commit/c8992fc35b)\
  2020-11-17 14:28:31 +0200
  * Trivial cleanups, no logic changes
* [Revision #3d56bea3ef](https://github.com/MariaDB/server/commit/3d56bea3ef)\
  2020-11-17 13:44:43 +0200
  * Allow field\_name NOT NULL ENABLED
* [Revision #55b2788800](https://github.com/MariaDB/server/commit/55b2788800)\
  2020-11-09 20:57:27 +0200
  * Fixed length estimate for REPLACE()
* [Revision #657fcdf430](https://github.com/MariaDB/server/commit/657fcdf430)\
  2020-11-25 16:54:00 +0200
  * [MDEV-24280](https://jira.mariadb.org/browse/MDEV-24280) InnoDB triggers too many independent periodic tasks
* [Revision #7b1252c03d](https://github.com/MariaDB/server/commit/7b1252c03d)\
  2020-11-25 16:09:47 +0200
  * [MDEV-24278](https://jira.mariadb.org/browse/MDEV-24278) InnoDB page cleaner keeps waking up on idle server
* [Revision #f693b72547](https://github.com/MariaDB/server/commit/f693b72547)\
  2020-11-25 16:08:26 +0200
  * [MDEV-24270](https://jira.mariadb.org/browse/MDEV-24270): Clarify some comments
* [Revision #2de95f7a1e](https://github.com/MariaDB/server/commit/2de95f7a1e)\
  2020-11-25 13:06:51 +0100
  * Fix misspelling.
* [Revision #af98fddc2b](https://github.com/MariaDB/server/commit/af98fddc2b)\
  2020-11-25 11:12:53 +0100
  * Cleanup. Remove obsolete comment
* [Revision #c130c60b2b](https://github.com/MariaDB/server/commit/c130c60b2b)\
  2020-11-25 11:12:09 +0100
  * Cleanup. Provide accurate comment on my\_getevents().
* [Revision #78df9e37a6](https://github.com/MariaDB/server/commit/78df9e37a6)\
  2020-11-25 10:59:10 +0100
  * Partially Revert "[MDEV-24270](https://jira.mariadb.org/browse/MDEV-24270): Collect multiple completed events at a time"
* [Revision #3dfeae0e22](https://github.com/MariaDB/server/commit/3dfeae0e22)\
  2020-11-25 11:32:49 +0200
  * Cleanup: Fix Intel compiler warnings about sign conversions
* [Revision #4a22056c97](https://github.com/MariaDB/server/commit/4a22056c97)\
  2020-11-25 11:28:26 +0200
  * Cleanup: Remove redundant nonnull attributes
* [Revision #6479006e14](https://github.com/MariaDB/server/commit/6479006e14)\
  2020-11-25 09:42:38 +0200
  * [MDEV-24270](https://jira.mariadb.org/browse/MDEV-24270): Collect multiple completed events at a time
* [Revision #7a9405e3dc](https://github.com/MariaDB/server/commit/7a9405e3dc)\
  2020-11-25 09:40:12 +0200
  * [MDEV-24270](https://jira.mariadb.org/browse/MDEV-24270) Misuse of io\_getevents() causes wake-ups at least twice per second
* [Revision #1b12e251cd](https://github.com/MariaDB/server/commit/1b12e251cd)\
  2020-11-24 11:33:39 +0200
  * [MDEV-24271](https://jira.mariadb.org/browse/MDEV-24271) rw\_lock::read\_lock\_yield() may cause writer starvation
* [Revision #dcdc8c3506](https://github.com/MariaDB/server/commit/dcdc8c3506)\
  2020-11-20 13:40:35 +0200
  * [MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534) fixup: Remove HAVE\_IB\_LINUX\_FUTEX
* [Revision #1e5d989d2a](https://github.com/MariaDB/server/commit/1e5d989d2a)\
  2020-11-20 08:55:41 +0200
  * [MDEV-24167](https://jira.mariadb.org/browse/MDEV-24167): Remove PFS instrumentation of buf\_block\_t
* [Revision #156cb94b4b](https://github.com/MariaDB/server/commit/156cb94b4b)\
  2020-11-20 08:49:46 +0200
  * [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871) fixup: Relax a debug assertion
* [Revision #3c8ecb5bbd](https://github.com/MariaDB/server/commit/3c8ecb5bbd)\
  2020-11-20 08:06:24 +0200
  * Run innodb\_wl6326\_big only in debug builds
* [Revision #8ac19be8a2](https://github.com/MariaDB/server/commit/8ac19be8a2)\
  2020-11-19 20:25:57 +0200
  * Cleanup: Fix build problems with the Intel compiler
* [Revision #9c455945f5](https://github.com/MariaDB/server/commit/9c455945f5)\
  2020-11-19 20:22:36 +0200
  * [MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534) fixup: Use a compile-time constant
* [Revision #a16e3c326d](https://github.com/MariaDB/server/commit/a16e3c326d)\
  2020-11-10 07:54:22 +0000
  * Update MCS to resolve libmarias3 compulation for centos74-amd64-debug pipeline in community BB
* [Revision #3b486c28f7](https://github.com/MariaDB/server/commit/3b486c28f7)\
  2020-11-19 07:46:27 +1100
  * [MDEV-24125](https://jira.mariadb.org/browse/MDEV-24125): linux large pages, linux/mman.h needed
* [Revision #33d41167c5](https://github.com/MariaDB/server/commit/33d41167c5)\
  2020-11-18 10:27:18 +0200
  * [MDEV-24224](https://jira.mariadb.org/browse/MDEV-24224) Gap lock on delete in 10.5 using READ COMMITTED
* Merge [Revision #fabdad6857](https://github.com/MariaDB/server/commit/fabdad6857) 2020-11-17 18:15:13 +0200 - Merge 10.4 into 10.5
* [Revision #83a55670a6](https://github.com/MariaDB/server/commit/83a55670a6)\
  2020-11-17 09:39:36 +0200
  * [MDEV-24188](https://jira.mariadb.org/browse/MDEV-24188) fixup: Simplify the wait loop
* [Revision #694926a4f7](https://github.com/MariaDB/server/commit/694926a4f7)\
  2020-11-17 11:16:50 +0100
  * Fix suppression in MTR test galera\_3nodes.inconsistency\_shutdown
* [Revision #c815ffb975](https://github.com/MariaDB/server/commit/c815ffb975)\
  2020-11-16 23:10:53 +0530
  * [MDEV-23610](https://jira.mariadb.org/browse/MDEV-23610): Slave user can't run "SHOW SLAVE STATUS" anymore after upgrade to 10.5, mysql\_upgrade should take of that
* [Revision #7f30a5c423](https://github.com/MariaDB/server/commit/7f30a5c423)\
  2020-11-16 09:23:51 +1100
  * [MDEV-24125](https://jira.mariadb.org/browse/MDEV-24125): allow compile on Linux headers < 3.8
* [Revision #8cc5d2845c](https://github.com/MariaDB/server/commit/8cc5d2845c)\
  2020-11-16 09:05:10 +1100
  * [MDEV-24125](https://jira.mariadb.org/browse/MDEV-24125): linux large pages - Revert "Fixed centos 6 build failure"
* [Revision #0fc0eb1e5b](https://github.com/MariaDB/server/commit/0fc0eb1e5b)\
  2020-11-16 08:48:32 +1100
  * [MDEV-24124](https://jira.mariadb.org/browse/MDEV-24124): main.drop test - mulitarch/os error messages
* [Revision #2b347e9fc5](https://github.com/MariaDB/server/commit/2b347e9fc5)\
  2020-11-16 14:49:46 +0530
  * [MDEV-23610](https://jira.mariadb.org/browse/MDEV-23610): Slave user can't run "SHOW SLAVE STATUS" anymore after upgrade to 10.5, mysql\_upgrade should take of that
* [Revision #6da68049b5](https://github.com/MariaDB/server/commit/6da68049b5)\
  2020-11-16 14:31:44 +0530
  * [MDEV-23610](https://jira.mariadb.org/browse/MDEV-23610): Slave user can't run "SHOW SLAVE STATUS" anymore after upgrade to 10.5, mysql\_upgrade should take of that
* [Revision #1edd224372](https://github.com/MariaDB/server/commit/1edd224372)\
  2020-11-14 14:13:33 +0000
  * This patch puts MCS debian packaging files and part of debian/control into the engine directory
* [Revision #81b9c78500](https://github.com/MariaDB/server/commit/81b9c78500)\
  2020-11-14 12:28:28 +0100
  * [MDEV-24098](https://jira.mariadb.org/browse/MDEV-24098): 10.5 followup
* Merge [Revision #6daf6bbcfe](https://github.com/MariaDB/server/commit/6daf6bbcfe) 2020-11-14 10:15:54 +0100 - Merge branch '10.4' into 10.5
* Merge [Revision #e8f8992801](https://github.com/MariaDB/server/commit/e8f8992801) 2020-11-13 22:06:50 +0200 - [MDEV-24188](https://jira.mariadb.org/browse/MDEV-24188): Merge 10.4 into 10.5
* Merge [Revision #ca331bdcda](https://github.com/MariaDB/server/commit/ca331bdcda) 2020-11-13 21:54:32 +0200 - [MDEV-23619](https://jira.mariadb.org/browse/MDEV-23619): Merge 10.4 into 10.5
* Merge [Revision #d7a5824899](https://github.com/MariaDB/server/commit/d7a5824899) 2020-11-13 21:54:21 +0200 - Merge 10.4 into 10.5
* [Revision #97569d3c37](https://github.com/MariaDB/server/commit/97569d3c37)\
  2020-11-11 16:49:29 +0200
  * [MDEV-24196](https://jira.mariadb.org/browse/MDEV-24196) WITH\_UBSAN: member call on null pointer of log\_phys\_t
* Merge [Revision #b4a5ad8db5](https://github.com/MariaDB/server/commit/b4a5ad8db5) 2020-11-11 17:42:23 +0200 - Merge mariadb-10.5.8 into 10.5
* [Revision #fff469db7f](https://github.com/MariaDB/server/commit/fff469db7f)\
  2020-11-11 10:20:34 -0500
  * bump the VERSION
* [Revision #e9b3d44c6e](https://github.com/MariaDB/server/commit/e9b3d44c6e)\
  2020-11-11 09:11:34 +0200
  * [MDEV-24190](https://jira.mariadb.org/browse/MDEV-24190) Accessing INFORMATION\_SCHEMA.INNODB\_TABLESPACES\_ENCRYPTION may break innodb\_open\_files logic
* [Revision #10b2d5726f](https://github.com/MariaDB/server/commit/10b2d5726f)\
  2020-11-09 19:36:10 +0200
  * Fixed failing maria.create test
* [Revision #f424eb974d](https://github.com/MariaDB/server/commit/f424eb974d)\
  2020-11-05 11:41:43 +0200
  * Clean up the merge of [MDEV-22494](https://jira.mariadb.org/browse/MDEV-22494)
* [Revision #4cbfdeca84](https://github.com/MariaDB/server/commit/4cbfdeca84)\
  2020-11-04 16:55:36 +0200
  * [MDEV-24109](https://jira.mariadb.org/browse/MDEV-24109) InnoDB hangs with innodb\_flush\_sync=OFF
* [Revision #7b20aa576b](https://github.com/MariaDB/server/commit/7b20aa576b)\
  2020-11-04 13:33:30 +0700
  * [MDEV-24116](https://jira.mariadb.org/browse/MDEV-24116): Fix clang 12 -Wrange-loop-analysis
* [Revision #1418439d38](https://github.com/MariaDB/server/commit/1418439d38)\
  2020-11-03 11:00:36 -0500
  * bump the VERSION
* Merge [Revision #3bc6e0ea66](https://github.com/MariaDB/server/commit/3bc6e0ea66) 2020-11-03 16:24:57 +0200 - Merge bb-10.5-release into 10.5
* Merge [Revision #133b4b46fe](https://github.com/MariaDB/server/commit/133b4b46fe) 2020-11-03 16:24:47 +0200 - Merge 10.4 into 10.5
* [Revision #44836bcd12](https://github.com/MariaDB/server/commit/44836bcd12)\
  2020-11-03 10:47:25 +0100
  * Fix appvyeor's perl.exe path
* [Revision #440d4b282d](https://github.com/MariaDB/server/commit/440d4b282d)\
  2020-11-02 10:53:37 +0200
  * Fix clang -Winconsistent-missing-override
* [Revision #504d4c1ff6](https://github.com/MariaDB/server/commit/504d4c1ff6)\
  2020-11-02 10:07:05 +0100
  * Windows : require at least VS2019 for MSVC.
* [Revision #f244b499e7](https://github.com/MariaDB/server/commit/f244b499e7)\
  2020-10-14 15:40:46 +1000
  * handler: move row change start signal down after the checks
* [Revision #e618f7e9f6](https://github.com/MariaDB/server/commit/e618f7e9f6)\
  2020-10-20 15:21:28 +1000
  * [MDEV-22506](https://jira.mariadb.org/browse/MDEV-22506) Malformed error message for ER\_KEY\_CONTAINS\_PERIOD\_FIELDS
* [Revision #a79c6e369e](https://github.com/MariaDB/server/commit/a79c6e369e)\
  2020-10-22 01:32:44 +1000
  * [MDEV-22677](https://jira.mariadb.org/browse/MDEV-22677) UPDATE crashes on partitioned HEAP table WITHOUT OVERLAPS
* [Revision #d9e00770a3](https://github.com/MariaDB/server/commit/d9e00770a3)\
  2020-10-21 02:04:37 +1000
  * [MDEV-22608](https://jira.mariadb.org/browse/MDEV-22608) ASAN use-after-poison in TABLE::check\_period\_overlaps
* [Revision #afca976885](https://github.com/MariaDB/server/commit/afca976885)\
  2020-10-20 19:19:36 +1000
  * [MDEV-22639](https://jira.mariadb.org/browse/MDEV-22639) Assertion failed in ha\_check\_overlaps upon multi-table update
* [Revision #d543363f25](https://github.com/MariaDB/server/commit/d543363f25)\
  2020-09-24 21:59:28 +1000
  * [MDEV-22714](https://jira.mariadb.org/browse/MDEV-22714) Assertion failed upon multi-update on table WITHOUT OVERLAPS
* [Revision #30894fe9a9](https://github.com/MariaDB/server/commit/30894fe9a9)\
  2020-09-22 20:17:02 +1000
  * Add DBUG\_ASSERT in Field::ptr\_in\_record

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
