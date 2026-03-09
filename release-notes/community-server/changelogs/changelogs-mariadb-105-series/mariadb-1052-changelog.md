# MariaDB 10.5.2 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download](https://downloads.mariadb.org/mariadb/10.5.2/)[Release Notes](../../old-releases/10.5/10.5.2.md)[Changelog](mariadb-1052-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 26 Mar 2020

**Do not use&#x20;**_**beta**_**&#x20;releases in production!**

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.2.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.12](../changelogs-mariadb-10-4-series/mariadb-10412-changelog.md)
* [Revision #f01e7a4741](https://github.com/MariaDB/server/commit/f01e7a4741)\
  2020-03-25 12:09:47 +0200
  * [MDEV-22035](https://jira.mariadb.org/browse/MDEV-22035) Memory leak in main.mysqltest
* [Revision #9a7d284e20](https://github.com/MariaDB/server/commit/9a7d284e20)\
  2020-03-25 08:25:38 +0200
  * [MDEV-22031](https://jira.mariadb.org/browse/MDEV-22031) Assertion bpage->in\_page\_hash failed in buf\_pool\_watch\_set
* [Revision #19e998d20c](https://github.com/MariaDB/server/commit/19e998d20c)\
  2020-03-25 00:41:32 +0400
  * [MDEV-22030](https://jira.mariadb.org/browse/MDEV-22030) Don't grant REPLICATION MASTER ADMIN automatically on upgrade from an older JSON user table
* [Revision #30cacf3fce](https://github.com/MariaDB/server/commit/30cacf3fce)\
  2020-03-24 23:12:30 +0400
  * An additional test for [MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743) Split up SUPER privilege to smaller privileges
* [Revision #d23c3e03ac](https://github.com/MariaDB/server/commit/d23c3e03ac)\
  2020-03-23 20:13:24 +0200
  * Use truncate instead of delete to make stat\_tables.inc more repeatable
* [Revision #3faa15cfbd](https://github.com/MariaDB/server/commit/3faa15cfbd)\
  2020-03-17 17:49:45 +0200
  * Don't give warnings from safemalloc for aria\_pack --help
* [Revision #6736f152f4](https://github.com/MariaDB/server/commit/6736f152f4)\
  2020-03-03 13:21:08 +0200
  * Added FLUSH THREADS
* [Revision #37393bea23](https://github.com/MariaDB/server/commit/37393bea23)\
  2020-02-26 14:52:23 +0200
  * Replace handler::primary\_key\_is\_clustered() with handler::pk\_is\_clustering\_key()
* [Revision #8eba777c2b](https://github.com/MariaDB/server/commit/8eba777c2b)\
  2020-02-24 17:38:14 +0200
  * mysqld --help will now load mysqld.options table
* [Revision #324e42fbdc](https://github.com/MariaDB/server/commit/324e42fbdc)\
  2020-02-12 18:31:09 +0200
  * Give a better error message if we can't load mysql.plugin table
* [Revision #44790f58ac](https://github.com/MariaDB/server/commit/44790f58ac)\
  2020-01-30 17:36:45 +0200
  * Fixed typo in aria\_s3\_copy
* [Revision #3775e7cc00](https://github.com/MariaDB/server/commit/3775e7cc00)\
  2020-01-30 15:56:40 +0200
  * Fixed that file\_key\_management works with BUILD scripts
* [Revision #120b73a069](https://github.com/MariaDB/server/commit/120b73a069)\
  2020-01-30 15:50:45 +0200
  * Speed up writing to encrypted binlogs
* [Revision #91ab42a823](https://github.com/MariaDB/server/commit/91ab42a823)\
  2020-01-28 23:23:51 +0200
  * Clean up and speed up interfaces for binary row logging
* [Revision #f51df1dc78](https://github.com/MariaDB/server/commit/f51df1dc78)\
  2020-01-15 15:36:50 +0200
  * Fixed valgrind warning
* [Revision #4ef437558a](https://github.com/MariaDB/server/commit/4ef437558a)\
  2020-01-13 18:30:13 +0200
  * Improve update handler (long unique keys on blobs)
* [Revision #736998cb75](https://github.com/MariaDB/server/commit/736998cb75)\
  2019-12-30 14:11:31 +0200
  * Cleanups & indentation changes
* [Revision #6a9e24d046](https://github.com/MariaDB/server/commit/6a9e24d046)\
  2019-12-30 13:56:19 +0200
  * Added support for replication for S3
* [Revision #e5de1e26e7](https://github.com/MariaDB/server/commit/e5de1e26e7)\
  2020-03-24 09:52:36 +0200
  * Ignore mariadb-config.1
* [Revision #da82e75901](https://github.com/MariaDB/server/commit/da82e75901)\
  2020-01-24 00:44:48 +0400
  * handler::rebind()
* [Revision #bff79492c5](https://github.com/MariaDB/server/commit/bff79492c5)\
  2019-12-30 13:34:28 +0200
  * Added IF EXISTS to RENAME TABLE and ALTER TABLE
* Merge [Revision #5f5c63e0fe](https://github.com/MariaDB/server/commit/5f5c63e0fe) 2020-03-24 09:54:08 +0200 - Merge 10.4 into 10.5
* [Revision #efc97eff31](https://github.com/MariaDB/server/commit/efc97eff31)\
  2020-03-24 09:35:19 +0200
  * Fix clang -Wsometimes-uninitialized
* [Revision #8b647d6960](https://github.com/MariaDB/server/commit/8b647d6960)\
  2020-03-24 09:27:09 +0200
  * [MDEV-22020](https://jira.mariadb.org/browse/MDEV-22020): Fix spider/bugfix.return\_found\_rows\_update
* [Revision #a940151eec](https://github.com/MariaDB/server/commit/a940151eec)\
  2020-03-24 08:47:41 +0100
  * [MDEV-21988](https://jira.mariadb.org/browse/MDEV-21988): Assertion failure mysqld: bool trans\_commit\_stmt(THD\*): Assertion \`thd->in\_active\_multi\_stmt\_transaction() || thd->m\_transaction\_psi == null' failed. (#1476)
* [Revision #fbfd4fafd4](https://github.com/MariaDB/server/commit/fbfd4fafd4)\
  2020-03-24 00:58:54 +0100
  * autobake-deb.sh: include symlinks in the final listing
* [Revision #79b8901711](https://github.com/MariaDB/server/commit/79b8901711)\
  2020-03-23 13:11:51 +0000
  * [MDEV-22009](https://jira.mariadb.org/browse/MDEV-22009) mysqlhotcopy tool and wsrep scripts not found
* [Revision #e4afd3c337](https://github.com/MariaDB/server/commit/e4afd3c337)\
  2020-03-23 21:37:32 +0100
  * [MDEV-22003](https://jira.mariadb.org/browse/MDEV-22003) mysql\_config disappeared from 10.5 (e.g. binary tarball or source build)
* [Revision #73edb6ffd4](https://github.com/MariaDB/server/commit/73edb6ffd4)\
  2020-03-23 19:53:54 +0100
  * Revert "[MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303) Make executables MariaDB named"
* [Revision #4b1f608569](https://github.com/MariaDB/server/commit/4b1f608569)\
  2020-03-19 16:35:40 +0200
  * Travis-CI: Optimize the selection of tests to be smaller and more diverse
* [Revision #b0140c084e](https://github.com/MariaDB/server/commit/b0140c084e)\
  2020-03-19 16:18:39 +0200
  * Travis-CI: Mac OS X build improvements
* [Revision #a5d73d4d72](https://github.com/MariaDB/server/commit/a5d73d4d72)\
  2020-03-18 10:36:52 +0200
  * Travis-CI: Refactor .travis.yml and document
* [Revision #20ddc1e086](https://github.com/MariaDB/server/commit/20ddc1e086)\
  2020-03-18 09:54:14 +0200
  * Travis-CI: No-change cleanup of bad syntax in .travis-ci.yml
* [Revision #ed6168f7ce](https://github.com/MariaDB/server/commit/ed6168f7ce)\
  2020-03-23 22:46:02 +0300
  * cleanup: group deprecated:: code together
* [Revision #194c5b6ad2](https://github.com/MariaDB/server/commit/194c5b6ad2)\
  2020-03-23 00:58:51 +0300
  * [MDEV-21990](https://jira.mariadb.org/browse/MDEV-21990) Issue a message on changing deprecated innodb\_log\_files\_in\_group
* [Revision #8fdb695690](https://github.com/MariaDB/server/commit/8fdb695690)\
  2020-03-20 22:57:52 +0300
  * fix formatting and remove outdated comment
* [Revision #faab0d31a3](https://github.com/MariaDB/server/commit/faab0d31a3)\
  2020-03-23 17:47:06 +0400
  * [MDEV-22012](https://jira.mariadb.org/browse/MDEV-22012) Allow SET TIMESTAMP for users with GRANT BINLOG REPLAY when --secure-timestamp=replication
* [Revision #02fe997505](https://github.com/MariaDB/server/commit/02fe997505)\
  2020-03-23 10:45:08 +0100
  * fix a nondeterminism in perfschema.statement\_program\_non\_nested test
* [Revision #121a5e8d07](https://github.com/MariaDB/server/commit/121a5e8d07)\
  2020-03-23 10:27:37 +0200
  * Minor buffer pool cleanup
* [Revision #82c465f68e](https://github.com/MariaDB/server/commit/82c465f68e)\
  2020-03-23 09:50:35 +0200
  * [MDEV-21962](https://jira.mariadb.org/browse/MDEV-21962): Minor cleanup
* Merge [Revision #3b25083785](https://github.com/MariaDB/server/commit/3b25083785) 2020-03-23 10:50:14 +0200 - Merge 10.4 into 10.5
* [Revision #f7599f4799](https://github.com/MariaDB/server/commit/f7599f4799)\
  2020-03-23 13:13:20 +0530
  * [MDEV-21792](https://jira.mariadb.org/browse/MDEV-21792) Server aborts upon attempt to create foreign key on spatial field
* [Revision #81f700015e](https://github.com/MariaDB/server/commit/81f700015e)\
  2020-03-21 19:49:46 +0400
  * Cleanup my\_atomic.h includes
* [Revision #6acddd5367](https://github.com/MariaDB/server/commit/6acddd5367)\
  2020-03-21 19:46:49 +0400
  * global\_query\_id: my\_atomic to Atomic\_counter
* [Revision #62687801ff](https://github.com/MariaDB/server/commit/62687801ff)\
  2020-03-21 18:36:31 +0400
  * tc\_active\_instances: my\_atomic to std::atomic
* [Revision #3b3f931570](https://github.com/MariaDB/server/commit/3b3f931570)\
  2020-03-21 17:59:43 +0400
  * Discovery counters: my\_atomic to Atomic\_counter
* [Revision #a39d92ca57](https://github.com/MariaDB/server/commit/a39d92ca57)\
  2020-03-21 17:36:38 +0400
  * gtid\_pos\_table: my\_atomic to std::atomic
* [Revision #4d9977e5ff](https://github.com/MariaDB/server/commit/4d9977e5ff)\
  2020-03-21 15:52:24 +0400
  * default\_gtid\_pos\_table: my\_atomic to std::atomic
* [Revision #1a4998e982](https://github.com/MariaDB/server/commit/1a4998e982)\
  2020-03-23 09:22:29 +0100
  * [MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303) postfixes
* [Revision #5d1b8f4152](https://github.com/MariaDB/server/commit/5d1b8f4152)\
  2020-03-21 13:26:50 +0100
  * [MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303) Make executables MariaDB named
* [Revision #9e1b3af4a4](https://github.com/MariaDB/server/commit/9e1b3af4a4)\
  2020-03-20 16:41:54 +0200
  * [MDEV-21303](https://jira.mariadb.org/browse/MDEV-21303) Make executables MariaDB named
* [Revision #6fb59d525b](https://github.com/MariaDB/server/commit/6fb59d525b)\
  2020-03-21 12:39:58 +0200
  * [MDEV-742](https://jira.mariadb.org/browse/MDEV-742): Fix clang -Winconsistent-missing-override
* [Revision #2559075bda](https://github.com/MariaDB/server/commit/2559075bda)\
  2020-03-21 12:36:55 +0200
  * Correct a result
* Merge [Revision #5203bc10f1](https://github.com/MariaDB/server/commit/5203bc10f1) 2020-03-21 11:37:10 +0200 - Merge 10.4 into 10.5
* [Revision #9394cc8914](https://github.com/MariaDB/server/commit/9394cc8914)\
  2020-03-21 08:17:28 +0100
  * [MDEV-21675](https://jira.mariadb.org/browse/MDEV-21675): Data inconsistency after multirow insert rollback (#1474)
* Merge [Revision #bd3c8f47cd](https://github.com/MariaDB/server/commit/bd3c8f47cd) 2020-03-20 22:06:55 +0200 - Merge 10.3 into 10.4
* [Revision #fd5c36bed5](https://github.com/MariaDB/server/commit/fd5c36bed5)\
  2020-03-20 21:41:39 +0200
  * [MDEV-21959](https://jira.mariadb.org/browse/MDEV-21959): Fix a type mismatch on 64-bit systems
* Merge [Revision #44298e4dea](https://github.com/MariaDB/server/commit/44298e4dea) 2020-03-20 18:08:16 +0200 - Merge 10.2 into 10.3
* [Revision #9f7b8625e6](https://github.com/MariaDB/server/commit/9f7b8625e6)\
  2020-03-20 17:40:39 +0200
  * [MDEV-14431](https://jira.mariadb.org/browse/MDEV-14431): Fix ulong/ulonglong type mismatch
* [Revision #b034d708c8](https://github.com/MariaDB/server/commit/b034d708c8)\
  2020-03-20 16:34:15 +0200
  * [MDEV-21549](https://jira.mariadb.org/browse/MDEV-21549): Clean up the import/export tests
* [Revision #b8b3edff13](https://github.com/MariaDB/server/commit/b8b3edff13)\
  2020-03-20 13:14:05 +0200
  * [MDEV-21549](https://jira.mariadb.org/browse/MDEV-21549) IMPORT TABLESPACE fails to adjust all tablespace ID in root pages
* Merge [Revision #c9ec1cc751](https://github.com/MariaDB/server/commit/c9ec1cc751) 2020-03-20 15:37:08 +0200 - Merge 10.1 into 10.2
* [Revision #328edf8560](https://github.com/MariaDB/server/commit/328edf8560)\
  2020-03-20 15:24:06 +0400
  * [MDEV-21977](https://jira.mariadb.org/browse/MDEV-21977) main.func\_math fails due to undefined behaviour
* [Revision #5c1ed707a3](https://github.com/MariaDB/server/commit/5c1ed707a3)\
  2020-02-26 19:39:26 +0100
  * mtr: update heuristics for --parallel=auto
* [Revision #0fe3d6d563](https://github.com/MariaDB/server/commit/0fe3d6d563)\
  2020-02-26 12:33:16 +0100
  * all status variables above `questions` MUST be ulong
* [Revision #a66eebf57c](https://github.com/MariaDB/server/commit/a66eebf57c)\
  2020-03-19 07:52:35 +0200
  * [MDEV-21981](https://jira.mariadb.org/browse/MDEV-21981) Replace arithmetic + with bitwise OR when possible
* [Revision #6960e9ed24](https://github.com/MariaDB/server/commit/6960e9ed24)\
  2020-03-19 14:23:47 +0200
  * [MDEV-21983](https://jira.mariadb.org/browse/MDEV-21983): Crash on DROP/RENAME TABLE after DISCARD TABLESPACE
* [Revision #9fd692aeca](https://github.com/MariaDB/server/commit/9fd692aeca)\
  2020-03-19 12:57:22 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Clean up the buffer pool resizing tests from MySQL 5.7
* [Revision #bfb5e1c3f0](https://github.com/MariaDB/server/commit/bfb5e1c3f0)\
  2020-03-19 07:46:30 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Import and adjust buffer pool resizing tests from MySQL 5.7
* [Revision #e28b4b68d3](https://github.com/MariaDB/server/commit/e28b4b68d3)\
  2020-03-19 06:58:49 +0200
  * [MDEV-14057](https://jira.mariadb.org/browse/MDEV-14057): Fix some tests
* [Revision #a0ce62f804](https://github.com/MariaDB/server/commit/a0ce62f804)\
  2020-03-18 13:55:21 +0400
  * [MDEV-14057](https://jira.mariadb.org/browse/MDEV-14057) InnoDB GIS tests fail.
* [Revision #09e8707d90](https://github.com/MariaDB/server/commit/09e8707d90)\
  2020-03-18 14:55:22 +0530
  * [MDEV-21826](https://jira.mariadb.org/browse/MDEV-21826) Recovery failure : loop of Read redo log up to LSN
* [Revision #6ecbb211c0](https://github.com/MariaDB/server/commit/6ecbb211c0)\
  2020-03-18 09:33:26 +0100
  * new (fixed) version of CC.
* [Revision #ab0034a789](https://github.com/MariaDB/server/commit/ab0034a789)\
  2020-03-17 16:28:16 +0200
  * [MDEV-20370](https://jira.mariadb.org/browse/MDEV-20370) Crash after OPTIMIZE TABLE on TEMPORARY TABLE
* [Revision #e61b99073f](https://github.com/MariaDB/server/commit/e61b99073f)\
  2020-03-17 19:22:20 +0530
  * [MDEV-14808](https://jira.mariadb.org/browse/MDEV-14808) innodb\_fts.sync fails in buildbot with wrong result
* [Revision #e64a3df4dc](https://github.com/MariaDB/server/commit/e64a3df4dc)\
  2020-03-17 13:11:46 +0400
  * [MDEV-21959](https://jira.mariadb.org/browse/MDEV-21959) GIS error message doesn't show the wrong value, just the type.
* [Revision #89698cef72](https://github.com/MariaDB/server/commit/89698cef72)\
  2020-03-17 10:32:42 +0200
  * [MDEV-10570](https://jira.mariadb.org/browse/MDEV-10570): Fix -Wmaybe-uninitialized
* [Revision #b1d7ba472e](https://github.com/MariaDB/server/commit/b1d7ba472e)\
  2020-03-11 22:00:14 +0100
  * innodb: fix typo in function description
* [Revision #d529389358](https://github.com/MariaDB/server/commit/d529389358)\
  2020-03-20 15:38:37 +0200
  * [MDEV-21979](https://jira.mariadb.org/browse/MDEV-21979) Galera test sporadic failure on galera\_3nodes.galera\_pc\_weight (#1473)
* [Revision #ec5e48be4b](https://github.com/MariaDB/server/commit/ec5e48be4b)\
  2020-03-20 13:23:24 +0200
  * Test fixes for galera\_3nodes suite.
* [Revision #b6e3cfde26](https://github.com/MariaDB/server/commit/b6e3cfde26)\
  2020-03-19 12:39:26 +0200
  * Fix test case name and add debug sync include.
* Merge [Revision #1de104a4d6](https://github.com/MariaDB/server/commit/1de104a4d6) 2020-03-19 12:25:49 +0200 - Merge branch 'codership-10.4-[MDEV-19966](https://jira.mariadb.org/browse/MDEV-19966)' into 10.4
* Merge [Revision #91baaf450f](https://github.com/MariaDB/server/commit/91baaf450f) 2020-03-19 12:25:15 +0200 - Merge branch '10.4-[MDEV-19966](https://jira.mariadb.org/browse/MDEV-19966)' of [mariadb-server](https://github.com/codership/mariadb-server) into codership-10.4-[MDEV-19966](https://jira.mariadb.org/browse/MDEV-19966)
* [Revision #d87c16be79](https://github.com/MariaDB/server/commit/d87c16be79)\
  2020-02-24 17:04:43 +0100
  * [MDEV-20616](https://jira.mariadb.org/browse/MDEV-20616): MariaDB-Galera 10.4.8 | Transaction aborted | Sig 6 Shutdown
* [Revision #76cdc1d73e](https://github.com/MariaDB/server/commit/76cdc1d73e)\
  2020-03-21 10:25:54 +0200
  * Remove a misleading copyright message
* [Revision #bb24fa31fa](https://github.com/MariaDB/server/commit/bb24fa31fa)\
  2020-03-20 18:47:35 +0300
  * move my\_assume\_aligned() to a separate header
* [Revision #95da2113a0](https://github.com/MariaDB/server/commit/95da2113a0)\
  2020-03-20 13:14:05 +0200
  * [MDEV-21549](https://jira.mariadb.org/browse/MDEV-21549) IMPORT TABLESPACE fails to adjust all tablespace ID
* [Revision #fcc0b89d52](https://github.com/MariaDB/server/commit/fcc0b89d52)\
  2020-03-20 06:26:46 +0100
  * Fix MTR test galera\_3nodes\_sr.galera\_vote\_sr (#1439)
* [Revision #6297a1026d](https://github.com/MariaDB/server/commit/6297a1026d)\
  2020-03-19 11:17:20 +0200
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Import and adjust buffer pool resizing tests from MySQL 5.7
* [Revision #007bb37aff](https://github.com/MariaDB/server/commit/007bb37aff)\
  2020-03-19 05:52:34 +0200
  * [MDEV-21962](https://jira.mariadb.org/browse/MDEV-21962): Fix a bug in buf\_pool\_t::clear\_hash\_index()
* [Revision #f3a8ca9d3f](https://github.com/MariaDB/server/commit/f3a8ca9d3f)\
  2020-03-19 05:43:57 +0200
  * [MDEV-21975](https://jira.mariadb.org/browse/MDEV-21975): Fix the result
* [Revision #14ef6a2c10](https://github.com/MariaDB/server/commit/14ef6a2c10)\
  2020-03-18 22:54:31 +0200
  * [MDEV-21975](https://jira.mariadb.org/browse/MDEV-21975) Add BINLOG REPLAY privilege and bind new privileges to ...
* [Revision #12b7d5dc46](https://github.com/MariaDB/server/commit/12b7d5dc46)\
  2020-03-17 23:52:01 +0200
  * Travis-CI: Ignore clang/GCC 6 that permanently fails on 10.5 branch
* [Revision #41952c85f1](https://github.com/MariaDB/server/commit/41952c85f1)\
  2020-03-16 13:07:52 +0200
  * Travis-CI: Shorten deb build log to keep it under 4 MB
* [Revision #30b44aaec7](https://github.com/MariaDB/server/commit/30b44aaec7)\
  2020-03-17 21:31:37 +0200
  * Deb: Fix executable bit so dh-exec works (regression in fd2dc9c3fdfb7)
* [Revision #0f8d6e3bd8](https://github.com/MariaDB/server/commit/0f8d6e3bd8)\
  2020-03-16 16:13:16 +0200
  * [MDEV-21942](https://jira.mariadb.org/browse/MDEV-21942): Correctly use newer libpcre2 version (regression in b6b6980)
* Merge [Revision #c235691d67](https://github.com/MariaDB/server/commit/c235691d67) 2020-03-18 22:44:41 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #6a63457639](https://github.com/MariaDB/server/commit/6a63457639) 2020-03-18 22:15:21 +0200 - Merge branch '10.3' into 10.4
* [Revision #dd68db0c17](https://github.com/MariaDB/server/commit/dd68db0c17)\
  2020-03-18 22:14:38 +0200
  * Change exec bit to allow dh-exec to work
* [Revision #2e0277373d](https://github.com/MariaDB/server/commit/2e0277373d)\
  2020-03-16 17:49:44 +0200
  * Fixed multi\_update\_debug.test
* [Revision #dbde95d912](https://github.com/MariaDB/server/commit/dbde95d912)\
  2020-03-17 19:13:17 +0200
  * Updated aria\_pack to support transactional tables
* [Revision #a786f50de5](https://github.com/MariaDB/server/commit/a786f50de5)\
  2020-03-18 21:48:00 +0200
  * [MDEV-21962](https://jira.mariadb.org/browse/MDEV-21962) Allocate buf\_pool statically
* [Revision #e0eacbee77](https://github.com/MariaDB/server/commit/e0eacbee77)\
  2020-03-18 20:15:53 +0400
  * [MDEV-21975](https://jira.mariadb.org/browse/MDEV-21975) Add BINLOG REPLAY privilege and bind new privileges to gtid\_seq\_no, preudo\_thread\_id, server\_id, gtid\_domain\_id
* [Revision #d126c40107](https://github.com/MariaDB/server/commit/d126c40107)\
  2020-03-18 15:22:16 +0200
  * [MDEV-21966](https://jira.mariadb.org/browse/MDEV-21966): Fix clang -Winconsistent-missing-override
* [Revision #68f390e598](https://github.com/MariaDB/server/commit/68f390e598)\
  2020-03-18 17:14:07 +0400
  * [MDEV-21973](https://jira.mariadb.org/browse/MDEV-21973) Bind REPLICATION {MASTER|SLAVE} ADMIN to gtid\_\* GLOBAL-only system variables
* Merge [Revision #305cffebab](https://github.com/MariaDB/server/commit/305cffebab) 2020-03-18 12:00:38 +0200 - merge 10.4 to 10.5
* [Revision #517f659e6d](https://github.com/MariaDB/server/commit/517f659e6d)\
  2020-03-17 12:37:56 +0200
  * Fixed that caused failure in --ps binlog\_encryption.rpl\_gtid\_basic
* [Revision #a2d24def8c](https://github.com/MariaDB/server/commit/a2d24def8c)\
  2020-03-13 15:55:32 +0200
  * [MDEV-21932](https://jira.mariadb.org/browse/MDEV-21932) A fast plan with ROR index-merge is ignored when 'index\_merge\_sort\_union=off'
* [Revision #1242eb3d32](https://github.com/MariaDB/server/commit/1242eb3d32)\
  2020-03-13 15:28:42 +0200
  * Removed double records\_in\_range calls from multi\_range\_read\_info\_const
* [Revision #96b472c0ae](https://github.com/MariaDB/server/commit/96b472c0ae)\
  2020-03-17 00:56:49 +0100
  * [MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439)\
    Windows builds should have core\_file=1 by default
* [Revision #36b0b302f2](https://github.com/MariaDB/server/commit/36b0b302f2)\
  2020-03-18 13:27:38 +0400
  * [MDEV-21972](https://jira.mariadb.org/browse/MDEV-21972) Bind REPLICATION MASTER ADMIN to master\_verify\_checksum
* [Revision #1ddc1fc305](https://github.com/MariaDB/server/commit/1ddc1fc305)\
  2020-03-18 12:50:17 +0400
  * [MDEV-21971](https://jira.mariadb.org/browse/MDEV-21971) Bind BINLOG ADMIN to binlog\_annotate\_row\_events and binlog\_row\_image global and session variables
* [Revision #965fa62617](https://github.com/MariaDB/server/commit/965fa62617)\
  2020-03-18 11:52:11 +0400
  * [MDEV-21969](https://jira.mariadb.org/browse/MDEV-21969) Bind REPLICATION SLAVE ADMIN to relay\_log\_\*, sync\_master\_info, sync\_relay\_log, sync\_relay\_log\_info
* [Revision #91c6e6df04](https://github.com/MariaDB/server/commit/91c6e6df04)\
  2020-03-18 10:36:06 +0400
  * [MDEV-21967](https://jira.mariadb.org/browse/MDEV-21967) Bind REPLICATION {MASTER|SLAVE} ADMIN to rpl\_semi\_sync\_\* variables
* [Revision #535c284aed](https://github.com/MariaDB/server/commit/535c284aed)\
  2020-03-18 07:02:15 +0400
  * [MDEV-21966](https://jira.mariadb.org/browse/MDEV-21966) Bind REPLICATION SLAVE ADMIN to a number of global system variables
* [Revision #90b7ac28a9](https://github.com/MariaDB/server/commit/90b7ac28a9)\
  2020-03-17 19:08:28 +0400
  * [MDEV-21963](https://jira.mariadb.org/browse/MDEV-21963) Bind BINLOG ADMIN to a number of global system variables
* [Revision #dec14dcffe](https://github.com/MariaDB/server/commit/dec14dcffe)\
  2020-03-17 14:27:52 +0400
  * [MDEV-21961](https://jira.mariadb.org/browse/MDEV-21961) Bind CONNECTION ADMIN to a number of global system variables
* [Revision #513cfd046d](https://github.com/MariaDB/server/commit/513cfd046d)\
  2020-03-17 11:49:38 +0400
  * [MDEV-21960](https://jira.mariadb.org/browse/MDEV-21960) Bind READ\_ONLY ADMIN to @@read\_only
* [Revision #b602584183](https://github.com/MariaDB/server/commit/b602584183)\
  2020-03-17 11:08:00 +0400
  * [MDEV-21957](https://jira.mariadb.org/browse/MDEV-21957) Bind BINLOG ADMIN to @@binlog\_format, @@binlog\_direct\_.., @@sql\_log\_bin
* Merge [Revision #c7ba92372b](https://github.com/MariaDB/server/commit/c7ba92372b) 2020-03-17 07:58:41 +0200 - Merge 10.4 into 10.5
* [Revision #097e2f9d0a](https://github.com/MariaDB/server/commit/097e2f9d0a)\
  2020-03-16 16:51:35 +0200
  * [MDEV-16188](https://jira.mariadb.org/browse/MDEV-16188): Fix clang 10 -Wimplicit-int-float-conversion
* [Revision #b7f0644710](https://github.com/MariaDB/server/commit/b7f0644710)\
  2020-03-16 16:32:11 +0200
  * [MDEV-5313](https://jira.mariadb.org/browse/MDEV-5313): Fix GCC 10 -Wenum-conversion
* Merge [Revision #e5e95a287e](https://github.com/MariaDB/server/commit/e5e95a287e) 2020-03-16 16:24:36 +0200 - Merge 10.3 into 10.4
* [Revision #c7daabdb05](https://github.com/MariaDB/server/commit/c7daabdb05)\
  2020-03-16 10:10:11 +0200
  * [MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134)/[MDEV-21855](https://jira.mariadb.org/browse/MDEV-21855): Add a test case
* Merge [Revision #5fe87ac413](https://github.com/MariaDB/server/commit/5fe87ac413) 2020-03-13 12:30:29 +0200 - Merge 10.2 into 10.3
* [Revision #ed21202a14](https://github.com/MariaDB/server/commit/ed21202a14)\
  2020-03-13 12:09:19 +0200
  * Fix GCC 10.0 -Wstringop-overflow
* [Revision #d9d3c222ca](https://github.com/MariaDB/server/commit/d9d3c222ca)\
  2020-03-12 17:47:54 +0530
  * [MDEV-10047](https://jira.mariadb.org/browse/MDEV-10047): table-based master info repository
* [Revision #9f858f38c0](https://github.com/MariaDB/server/commit/9f858f38c0)\
  2020-03-13 08:37:22 +0200
  * Fix clang 10 warnings
* [Revision #2e8b0c56a0](https://github.com/MariaDB/server/commit/2e8b0c56a0)\
  2020-03-13 08:07:02 +0200
  * [MDEV-21933](https://jira.mariadb.org/browse/MDEV-21933) INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESPACES accesses SYS\_DATAFILES
* [Revision #47382a2f8c](https://github.com/MariaDB/server/commit/47382a2f8c)\
  2020-03-13 07:53:41 +0200
  * Fix GCC 10 -Wclass-memaccess
* [Revision #a8566f727f](https://github.com/MariaDB/server/commit/a8566f727f)\
  2020-03-13 07:39:14 +0200
  * Fix GCC 10 -Wstringop-truncation
* [Revision #2c8fa28f40](https://github.com/MariaDB/server/commit/2c8fa28f40)\
  2020-03-13 07:21:40 +0200
  * Update libmariadb
* Merge [Revision #32904dc5fa](https://github.com/MariaDB/server/commit/32904dc5fa) 2020-03-13 07:20:36 +0200 - Merge 10.1 into 10.2
* Merge [Revision #7b082fb099](https://github.com/MariaDB/server/commit/7b082fb099) 2020-03-13 07:03:42 +0200 - Merge 5.5 into 10.1
* [Revision #3ab33c6c92](https://github.com/MariaDB/server/commit/3ab33c6c92)\
  2020-03-11 14:27:16 +0200
  * Cleanup: clang-10 -Wmisleading-indentation
* [Revision #7f36300df5](https://github.com/MariaDB/server/commit/7f36300df5)\
  2020-03-11 16:40:34 +0300
  * [MDEV-21918](https://jira.mariadb.org/browse/MDEV-21918) improve page\_zip\_verify\_checksum()
* [Revision #df88e7cefa](https://github.com/MariaDB/server/commit/df88e7cefa)\
  2020-03-11 16:27:37 +0300
  * fix typedef-related warning and cleanup using namespace std
* [Revision #b30446c85d](https://github.com/MariaDB/server/commit/b30446c85d)\
  2020-03-11 13:46:57 +0300
  * Fix compile warning:
* [Revision #5257bcfc7a](https://github.com/MariaDB/server/commit/5257bcfc7a)\
  2020-03-12 14:47:38 +0300
  * InnoDB: improve error message for checksum mismatch
* [Revision #069bad5e6b](https://github.com/MariaDB/server/commit/069bad5e6b)\
  2020-03-11 12:10:49 +0200
  * Add galera debug sync to galera\_slave\_replay test.
* [Revision #51e9381dcc](https://github.com/MariaDB/server/commit/51e9381dcc)\
  2020-03-11 12:10:49 +0200
  * Add galera debug sync to galera\_slave\_replay test.
* [Revision #cebf43e166](https://github.com/MariaDB/server/commit/cebf43e166)\
  2020-03-11 22:04:06 +0200
  * Fixed wrong assert (found by clang)
* [Revision #2b3f6ab417](https://github.com/MariaDB/server/commit/2b3f6ab417)\
  2020-03-13 18:15:57 +0100
  * [MDEV-21599](https://jira.mariadb.org/browse/MDEV-21599) plugins.server\_audit fails sporadically in buildbot
* [Revision #023d986732](https://github.com/MariaDB/server/commit/023d986732)\
  2020-03-16 22:14:50 +0200
  * perfschema: remove unused variables
* Merge [Revision #7b5aaaa554](https://github.com/MariaDB/server/commit/7b5aaaa554) 2020-03-17 07:51:53 +0200 - Fix the build on big-endian systems
* [Revision #c6db115ce6](https://github.com/MariaDB/server/commit/c6db115ce6)\
  2020-03-16 20:52:21 +1100
  * Fix compile on all big endian related to innodb:ut\_crc32\_swap\_byteorder
* [Revision #bd6afd8b5e](https://github.com/MariaDB/server/commit/bd6afd8b5e)\
  2020-03-13 15:22:02 +0400
  * [MDEV-21956](https://jira.mariadb.org/browse/MDEV-21956) Add class Sys\_var\_charptr\_fscs
* [Revision #9cc7edb1cf](https://github.com/MariaDB/server/commit/9cc7edb1cf)\
  2020-03-16 21:53:47 +0200
  * Cleanup: Remove an unused variable
* [Revision #7dafab7569](https://github.com/MariaDB/server/commit/7dafab7569)\
  2020-03-16 11:10:01 +0300
  * [MDEV-21949](https://jira.mariadb.org/browse/MDEV-21949) key rotation for innodb\_encrypt\_log is not working in 10.5
* [Revision #0c2365c4e3](https://github.com/MariaDB/server/commit/0c2365c4e3)\
  2020-03-15 21:53:25 +0300
  * cleanup redo log
* [Revision #ce496d4f9e](https://github.com/MariaDB/server/commit/ce496d4f9e)\
  2020-03-14 22:10:46 +0300
  * cleanup redo log
* [Revision #56402e84b5](https://github.com/MariaDB/server/commit/56402e84b5)\
  2020-03-16 11:43:30 +0100
  * [MDEV-21824](https://jira.mariadb.org/browse/MDEV-21824)\
    Crash in convert\_error\_message
* [Revision #92d61c2229](https://github.com/MariaDB/server/commit/92d61c2229)\
  2020-03-16 11:18:59 +0100
  * fix typo on non-Linux/Windows
* [Revision #b66745e9b9](https://github.com/MariaDB/server/commit/b66745e9b9)\
  2020-03-16 10:47:19 +0100
  * fix a copy-paste error in 8fd654ce0e5
* [Revision #b55d960e43](https://github.com/MariaDB/server/commit/b55d960e43)\
  2020-03-16 10:33:16 +0100
  * fix a nondeterminism in perfschema.statement\_program\_nesting\_event\_check test
* [Revision #17080cbcf0](https://github.com/MariaDB/server/commit/17080cbcf0)\
  2020-03-16 08:58:54 +0200
  * [MDEV-21945](https://jira.mariadb.org/browse/MDEV-21945) Assertion w==OPT failed in trx\_purge\_add\_undo\_to\_history()
* [Revision #9bd583ce1f](https://github.com/MariaDB/server/commit/9bd583ce1f)\
  2020-03-14 21:13:23 +0100
  * [MDEV-21942](https://jira.mariadb.org/browse/MDEV-21942) Building 10.5 requires Internet access
* [Revision #b6b6980686](https://github.com/MariaDB/server/commit/b6b6980686)\
  2020-03-14 20:25:30 +0100
  * [MDEV-21942](https://jira.mariadb.org/browse/MDEV-21942) Building 10.5 requires Internet access
* [Revision #79499b597a](https://github.com/MariaDB/server/commit/79499b597a)\
  2020-03-15 20:53:46 +0100
  * update the test result for new perfschema
* [Revision #8fd654ce0e](https://github.com/MariaDB/server/commit/8fd654ce0e)\
  2020-03-14 17:22:45 +0100
  * [MDEV-21943](https://jira.mariadb.org/browse/MDEV-21943) reduce the binary tarball size
* [Revision #47e220a3a7](https://github.com/MariaDB/server/commit/47e220a3a7)\
  2020-03-14 15:17:43 +0100
  * [MDEV-21943](https://jira.mariadb.org/browse/MDEV-21943) reduce the binary tarball size
* [Revision #0afccbf7b8](https://github.com/MariaDB/server/commit/0afccbf7b8)\
  2020-03-11 12:17:27 +0100
  * restore stack traces that were broken by ebfe8c4e0e
* Merge [Revision #2fde97119e](https://github.com/MariaDB/server/commit/2fde97119e) 2020-03-16 08:42:50 +0900 - Merge branch '10.5' of github.com:MariaDB/server into 10.5
* [Revision #c8388de2fd](https://github.com/MariaDB/server/commit/c8388de2fd)\
  2020-03-04 18:30:08 +0200
  * Fix various spelling errors
* [Revision #3c57693ff1](https://github.com/MariaDB/server/commit/3c57693ff1)\
  2020-03-15 21:40:11 +0100
  * [MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534) - Improve innodb redo log group commit performance
* [Revision #637c17588a](https://github.com/MariaDB/server/commit/637c17588a)\
  2020-03-15 23:48:50 +0530
  * [MDEV-21922](https://jira.mariadb.org/browse/MDEV-21922): Allow packing addon fields even if they don't honour max\_length\_for\_sort\_data
* [Revision #345e21d2eb](https://github.com/MariaDB/server/commit/345e21d2eb)\
  2020-03-15 14:14:35 +0200
  * [MDEV-742](https://jira.mariadb.org/browse/MDEV-742) test correction.
* [Revision #5929e222e4](https://github.com/MariaDB/server/commit/5929e222e4)\
  2020-03-16 08:39:49 +0900
  * fix evaluating bitmap issue in spider
* [Revision #8e5ae4e4df](https://github.com/MariaDB/server/commit/8e5ae4e4df)\
  2020-03-15 12:52:53 +0400
  * Test case fix: sort XA RECOVER result
* [Revision #c8ae357341](https://github.com/MariaDB/server/commit/c8ae357341)\
  2019-03-31 01:47:28 +0400
  * [MDEV-742](https://jira.mariadb.org/browse/MDEV-742) XA PREPAREd transaction survive disconnect/server restart
* [Revision #5754ea2eca](https://github.com/MariaDB/server/commit/5754ea2eca)\
  2020-03-14 15:24:13 +0200
  * Fixed compiler failures with gcc 7.4.1 and new my\_malloc code
* [Revision #41cba6c90b](https://github.com/MariaDB/server/commit/41cba6c90b)\
  2020-03-14 09:56:00 +0100
  * [MDEV-21920](https://jira.mariadb.org/browse/MDEV-21920) binlog\_encryption.rpl\_gtid\_basic test failure with --ps
* Merge [Revision #91d1588d30](https://github.com/MariaDB/server/commit/91d1588d30) 2020-03-14 09:52:35 +0100 - Merge branch 'github/10.5' into 10.5
* [Revision #774fe8969a](https://github.com/MariaDB/server/commit/774fe8969a)\
  2020-03-13 12:45:34 +0300
  * cleanup redo log
* [Revision #78cc9c9ebf](https://github.com/MariaDB/server/commit/78cc9c9ebf)\
  2020-03-12 16:34:44 +0400
  * Pre-[MDEV-742](https://jira.mariadb.org/browse/MDEV-742) InnoDB fixes
* [Revision #662d8a8638](https://github.com/MariaDB/server/commit/662d8a8638)\
  2020-03-10 17:43:42 +0400
  * Extended debug\_sync\_control life time
* [Revision #c58686447f](https://github.com/MariaDB/server/commit/c58686447f)\
  2020-03-12 23:24:47 +0530
  * [MDEV-21903](https://jira.mariadb.org/browse/MDEV-21903) FTS optimize thread aborts during shutdown
* [Revision #e74c1c9ece](https://github.com/MariaDB/server/commit/e74c1c9ece)\
  2020-03-13 10:12:32 +0200
  * Update libmariadb to fix GCC -Wstringop-truncation
* [Revision #fbe662a503](https://github.com/MariaDB/server/commit/fbe662a503)\
  2020-03-13 10:09:15 +0200
  * [MDEV-15058](https://jira.mariadb.org/browse/MDEV-15058): Remove buf\_pool\_get\_dirty\_pages\_count()
* [Revision #2bbcf9a19c](https://github.com/MariaDB/server/commit/2bbcf9a19c)\
  2020-03-13 09:07:51 +0400
  * [MDEV-21920](https://jira.mariadb.org/browse/MDEV-21920) binlog\_encryption.rpl\_gtid\_basic test failure with --ps
* [Revision #f48718be4e](https://github.com/MariaDB/server/commit/f48718be4e)\
  2020-03-13 06:59:34 +0200
  * [MDEV-20632](https://jira.mariadb.org/browse/MDEV-20632): Fix -Wmaybe-uninitialized
* [Revision #c57b207958](https://github.com/MariaDB/server/commit/c57b207958)\
  2020-03-13 06:55:00 +0200
  * [MDEV-21907](https://jira.mariadb.org/browse/MDEV-21907): Fix or disable -Wconversion on GCC 5.3.0 i386
* [Revision #f224525204](https://github.com/MariaDB/server/commit/f224525204)\
  2020-03-12 19:46:41 +0200
  * [MDEV-21907](https://jira.mariadb.org/browse/MDEV-21907): InnoDB: Enable -Wconversion on clang and GCC
* [Revision #d82ac8d374](https://github.com/MariaDB/server/commit/d82ac8d374)\
  2020-03-12 19:44:52 +0200
  * [MDEV-21907](https://jira.mariadb.org/browse/MDEV-21907): Fix some -Wconversion outside InnoDB
* [Revision #c7920fa8ff](https://github.com/MariaDB/server/commit/c7920fa8ff)\
  2020-03-12 18:04:30 +0200
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264): Eliminate unsafe os\_aio\_userdata\_t type cast
* [Revision #8be3794b42](https://github.com/MariaDB/server/commit/8be3794b42)\
  2020-03-12 13:58:45 +0200
  * [MDEV-21924](https://jira.mariadb.org/browse/MDEV-21924) Clean up InnoDB GIS record comparison
* [Revision #0d76777872](https://github.com/MariaDB/server/commit/0d76777872)\
  2020-03-12 18:02:16 +0200
  * [MDEV-13362](https://jira.mariadb.org/browse/MDEV-13362): Fix -Wset-but-unused
* [Revision #28fabc86db](https://github.com/MariaDB/server/commit/28fabc86db)\
  2020-03-02 23:46:07 +0100
  * [MDEV-13362](https://jira.mariadb.org/browse/MDEV-13362): implement --require\_secure\_transport option
* [Revision #c4f3e37b0c](https://github.com/MariaDB/server/commit/c4f3e37b0c)\
  2020-03-13 20:33:20 +0100
  * fix a race condition in the perfschema.transaction\_nested\_events
* [Revision #92c05a391a](https://github.com/MariaDB/server/commit/92c05a391a)\
  2020-03-13 18:24:43 +0100
  * fix a race condition in the main.grant\_kill test
* [Revision #df25d67d5f](https://github.com/MariaDB/server/commit/df25d67d5f)\
  2020-03-13 17:52:10 +0100
  * perfschema test formatting. Use --echo #
* [Revision #57de4def85](https://github.com/MariaDB/server/commit/57de4def85)\
  2020-03-13 14:59:02 +0100
  * [MDEV-21222](https://jira.mariadb.org/browse/MDEV-21222) mariadb-backup.incremental\_backup failed with memory allocation failure
* [Revision #422ba20591](https://github.com/MariaDB/server/commit/422ba20591)\
  2020-03-12 19:30:58 +0100
  * mtr sets MYSQLTEST\_REAL\_VARDIR when MYSQLTEST\_VARDIR is a symlink
* Merge [Revision #fad47df995](https://github.com/MariaDB/server/commit/fad47df995) 2020-03-11 17:52:49 +0100 - Merge branch '10.4' into 10.5
* Merge [Revision #b7362d5fbc](https://github.com/MariaDB/server/commit/b7362d5fbc) 2020-03-11 14:28:24 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #3c9bc0ce19](https://github.com/MariaDB/server/commit/3c9bc0ce19) 2020-03-11 14:05:41 +0100 - Merge branch '10.2' into 10.3
* [Revision #02343c4a54](https://github.com/MariaDB/server/commit/02343c4a54)\
  2020-03-10 15:46:29 +0200
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Correct a type mismatch WITH\_INNODB\_EXTRA\_DEBUG
* [Revision #2b8b85bd0a](https://github.com/MariaDB/server/commit/2b8b85bd0a)\
  2020-03-10 15:14:53 +0300
  * fix use-after-free
* [Revision #69e4c74e07](https://github.com/MariaDB/server/commit/69e4c74e07)\
  2020-03-10 13:31:20 +0200
  * Make main.mysql\_client\_test non-great again
* Merge [Revision #8cd6cee876](https://github.com/MariaDB/server/commit/8cd6cee876) 2020-03-10 13:29:10 +0200 - Merge 10.1 into 10.2
* [Revision #1c40cb6877](https://github.com/MariaDB/server/commit/1c40cb6877)\
  2020-03-10 13:26:57 +0200
  * Do not bother to disable non-existing tests
* [Revision #7a52b6fd25](https://github.com/MariaDB/server/commit/7a52b6fd25)\
  2020-03-09 12:04:02 +0200
  * Minor cleanup of main.partition\_innodb
* [Revision #2bf4e574ad](https://github.com/MariaDB/server/commit/2bf4e574ad)\
  2020-03-09 09:00:14 +0200
  * [MDEV-21758](https://jira.mariadb.org/browse/MDEV-21758) : Events switched randomly to SLAVESIDE\_DISABLED
* [Revision #8fa1b6bb88](https://github.com/MariaDB/server/commit/8fa1b6bb88)\
  2018-02-20 15:35:09 +0300
  * [MDEV-15724](https://jira.mariadb.org/browse/MDEV-15724) - Possible crash in parser
* [Revision #fd2dc9c3fd](https://github.com/MariaDB/server/commit/fd2dc9c3fd)\
  2020-03-08 16:19:43 +0200
  * Correctly link mysqlclient.pc to mariadb.pc under multi-arch support
* Merge [Revision #1d99e4d674](https://github.com/MariaDB/server/commit/1d99e4d674) 2020-03-08 11:02:55 +0200 - Merge branch '10.2' into 10.3
* [Revision #d7f74150e5](https://github.com/MariaDB/server/commit/d7f74150e5)\
  2020-03-07 19:21:40 +0200
  * Check for CPU\_COUNT macro within my\_getncpus
* [Revision #6610532170](https://github.com/MariaDB/server/commit/6610532170)\
  2020-03-07 14:46:40 +0200
  * Update install layout to account for multi-arch setup
* Merge [Revision #b8c0e49670](https://github.com/MariaDB/server/commit/b8c0e49670) 2020-03-11 13:27:10 +0100 - Merge commit '10.3' into 10.4
* Merge [Revision #440452628d](https://github.com/MariaDB/server/commit/440452628d) 2020-03-06 23:28:26 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #75d286c2cc](https://github.com/MariaDB/server/commit/75d286c2cc) 2020-03-06 15:42:45 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #345aaca14c](https://github.com/MariaDB/server/commit/345aaca14c) 2020-03-06 11:06:48 +0100 - Merge branch '5.5' into 10.1
* [Revision #be77fa914c](https://github.com/MariaDB/server/commit/be77fa914c)\
  2020-02-12 14:30:31 +0100
  * [MDEV-21646](https://jira.mariadb.org/browse/MDEV-21646): Failure to compile my\_addr\_resolve.c with binutils-2.34
* [Revision #91aae18cc4](https://github.com/MariaDB/server/commit/91aae18cc4)\
  2020-03-06 13:46:19 +0200
  * Enable galera.galera\_ist\_mariadb-backup and galera.mysql-wsrep#33.
* [Revision #c5c1027c6e](https://github.com/MariaDB/server/commit/c5c1027c6e)\
  2020-02-26 13:46:27 +0200
  * [MDEV-19208](https://jira.mariadb.org/browse/MDEV-19208) mariadb.pc: install into libdir
* Merge [Revision #da10c6f448](https://github.com/MariaDB/server/commit/da10c6f448) 2020-03-05 10:52:43 +0200 - Merge branch '10.1' into 10.2
* [Revision #395f23a10d](https://github.com/MariaDB/server/commit/395f23a10d)\
  2020-02-28 19:54:08 +0200
  * Remove unneded extra context line from test file to make it version independent
* [Revision #f21592c675](https://github.com/MariaDB/server/commit/f21592c675)\
  2018-11-01 13:16:11 -0400
  * mariadb.pc: remove unnecessary include directory
* [Revision #cd5d864fef](https://github.com/MariaDB/server/commit/cd5d864fef)\
  2020-02-25 15:58:42 +1100
  * mariadb{,@}.service comment typo open-file-limit -> open-files-limit
* [Revision #b9689712e0](https://github.com/MariaDB/server/commit/b9689712e0)\
  2019-12-31 18:02:54 +0100
  * [MDEV-21374](https://jira.mariadb.org/browse/MDEV-21374): When "--help --verbose" prints out configuration file paths, the --defaults-file option is not considered
* [Revision #f0d2542a37](https://github.com/MariaDB/server/commit/f0d2542a37)\
  2020-03-02 16:35:57 +0100
  * [MDEV-21857](https://jira.mariadb.org/browse/MDEV-21857) - Fix sporadic failure of mdev375
* [Revision #8382f10691](https://github.com/MariaDB/server/commit/8382f10691)\
  2020-02-26 13:01:18 +0700
  * MENT-606 Error while setting value 'aes\_ctr' to 'file-key-management-encryption-algorithm'
* [Revision #42b29d4133](https://github.com/MariaDB/server/commit/42b29d4133)\
  2020-02-25 17:59:49 +0700
  * MENT-645 Undefined symbols for architecture x86\_64: \_pam\_syslog
* [Revision #4618c974e4](https://github.com/MariaDB/server/commit/4618c974e4)\
  2020-02-23 10:29:42 +0200
  * [MDEV-21723](https://jira.mariadb.org/browse/MDEV-21723) Async slave thread BF abort and replaying fixes (#1448)
* [Revision #3ce49a0a52](https://github.com/MariaDB/server/commit/3ce49a0a52)\
  2020-02-20 14:04:09 +0530
  * [MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563) FTS thread aborts during shutdown
* [Revision #0d1dd2e79d](https://github.com/MariaDB/server/commit/0d1dd2e79d)\
  2020-02-20 09:25:05 +0100
  * Clean wrong cherry-pick from previous commit
* [Revision #fb01cc3766](https://github.com/MariaDB/server/commit/fb01cc3766)\
  2018-11-09 14:38:22 +1100
  * my\_getncpus based on threads available
* [Revision #959fc0c0cc](https://github.com/MariaDB/server/commit/959fc0c0cc)\
  2020-02-17 14:01:16 +0200
  * [MDEV-21591](https://jira.mariadb.org/browse/MDEV-21591) : galera.galera\_rsu\_add\_pk MTR failed: Result content mismatch
* [Revision #93dc3e2652](https://github.com/MariaDB/server/commit/93dc3e2652)\
  2020-02-13 13:33:41 +0200
  * [MDEV-21488](https://jira.mariadb.org/browse/MDEV-21488) : Galera test sporadic failure on galera.galera\_var\_notify\_cmd
* [Revision #ed10a8cd97](https://github.com/MariaDB/server/commit/ed10a8cd97)\
  2020-02-13 12:51:50 +0200
  * [MDEV-21515](https://jira.mariadb.org/browse/MDEV-21515) : Galera test sporadic failure on galera.galera\_wsrep\_new\_cluster: Result content mismatch
* [Revision #6c1e0c0493](https://github.com/MariaDB/server/commit/6c1e0c0493)\
  2020-02-13 10:30:40 +0200
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #a6b92690e6](https://github.com/MariaDB/server/commit/a6b92690e6)\
  2020-02-12 10:32:30 +0200
  * [MDEV-21556](https://jira.mariadb.org/browse/MDEV-21556) : galera.lp1376747-4 MTR failed: Result length mismatch
* [Revision #f6663bfbd3](https://github.com/MariaDB/server/commit/f6663bfbd3)\
  2020-02-11 00:19:37 +0400
  * [MDEV-17941](https://jira.mariadb.org/browse/MDEV-17941) ALTER USER IF EXISTS does not work, although documentation says it should.
* [Revision #f8ab5ca374](https://github.com/MariaDB/server/commit/f8ab5ca374)\
  2020-02-28 14:40:00 +0100
  * [MDEV-20382](https://jira.mariadb.org/browse/MDEV-20382): SHOW PRIVILEGES displays "Delete versioning rows" rather than "Delete History"
* [Revision #a662cb9b43](https://github.com/MariaDB/server/commit/a662cb9b43)\
  2020-02-25 14:55:15 +0300
  * Better comments
* [Revision #cfa0506f8a](https://github.com/MariaDB/server/commit/cfa0506f8a)\
  2020-02-25 00:47:03 -0800
  * [MDEV-21554](https://jira.mariadb.org/browse/MDEV-21554) Crash in JOIN\_CACHE\_BKAH::skip\_index\_tuple when mrr=on and join\_cache\_level=6+
* [Revision #f6b9a29820](https://github.com/MariaDB/server/commit/f6b9a29820)\
  2019-10-15 15:03:53 +1100
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662): cmake remove empty INSTALL\_DEBUG\_TARGET
* [Revision #c749eb2b41](https://github.com/MariaDB/server/commit/c749eb2b41)\
  2019-10-15 14:35:46 +1100
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662): cmake: CMP0026 compatible for dtrace
* [Revision #affe7fabc7](https://github.com/MariaDB/server/commit/affe7fabc7)\
  2020-02-19 21:27:38 +0300
  * [MDEV-21628](https://jira.mariadb.org/browse/MDEV-21628): Index condition pushdown condition ... not used with BKA
* [Revision #85d4a45d15](https://github.com/MariaDB/server/commit/85d4a45d15)\
  2020-02-09 22:27:51 +0200
  * Deb: Run 'wrap-and-sort -a' so comparison across releases is easier
* [Revision #1f0e72f874](https://github.com/MariaDB/server/commit/1f0e72f874)\
  2020-02-12 10:44:46 +0200
  * Deb: Remove unnecessary manual libzstd1 dependency from RocksDB plugin
* [Revision #5c6c4b1395](https://github.com/MariaDB/server/commit/5c6c4b1395)\
  2020-03-09 14:53:35 +0200
  * Fixes for previous not-complete-push
* [Revision #c037cdadf4](https://github.com/MariaDB/server/commit/c037cdadf4)\
  2020-03-05 14:10:03 +0200
  * Added keyread\_time() to HEAP
* [Revision #a24d0926b9](https://github.com/MariaDB/server/commit/a24d0926b9)\
  2020-03-06 14:21:20 +0200
  * Second stage of optimizer\_trace optimizations
* [Revision #940fcbe73b](https://github.com/MariaDB/server/commit/940fcbe73b)\
  2020-03-06 10:33:11 +0200
  * Improved speed of optimizer trace
* [Revision #1ad8693a6f](https://github.com/MariaDB/server/commit/1ad8693a6f)\
  2020-02-28 15:44:56 +0000
  * [MDEV-21841](https://jira.mariadb.org/browse/MDEV-21841) CONV() function doesn't truncate its output to 21 when uses default charset.
* [Revision #e837a358b6](https://github.com/MariaDB/server/commit/e837a358b6)\
  2020-02-28 14:01:27 +0200
  * [MDEV-21693](https://jira.mariadb.org/browse/MDEV-21693): Fix clang -Winconsistent-missing-override
* [Revision #f56dd0a12d](https://github.com/MariaDB/server/commit/f56dd0a12d)\
  2020-02-28 14:29:05 +0530
  * [MDEV-21693](https://jira.mariadb.org/browse/MDEV-21693) ALGORITHM=INSTANT does not work for partitioned tables
* [Revision #a17a327f11](https://github.com/MariaDB/server/commit/a17a327f11)\
  2020-02-26 13:58:08 +0100
  * [MDEV-21684](https://jira.mariadb.org/browse/MDEV-21684): mysqld crash with signal 11 when renaming table+max\_statement\_time
* [Revision #e637355156](https://github.com/MariaDB/server/commit/e637355156)\
  2020-02-20 13:35:19 +0300
  * [MDEV-21610](https://jira.mariadb.org/browse/MDEV-21610) Different query results from 10.4.11 to 10.4.12
* [Revision #adcfea710f](https://github.com/MariaDB/server/commit/adcfea710f)\
  2020-02-19 14:57:47 +0300
  * Fix compile failure, compare\_key\_parts in handler shadowed by MyRocks
* [Revision #2fb881df1d](https://github.com/MariaDB/server/commit/2fb881df1d)\
  2020-02-18 22:49:42 -0800
  * [MDEV-21610](https://jira.mariadb.org/browse/MDEV-21610) Different query results from 10.4.11 to 10.4.12
* [Revision #df07e00a81](https://github.com/MariaDB/server/commit/df07e00a81)\
  2019-10-14 18:13:02 +0300
  * [MDEV-20726](https://jira.mariadb.org/browse/MDEV-20726) InnoDB: Assertion failure in file data0type.cc line 67
* [Revision #7ccc1710a0](https://github.com/MariaDB/server/commit/7ccc1710a0)\
  2019-10-14 16:20:16 +0300
  * cleanup: key parts comparison
* [Revision #5a42a114fd](https://github.com/MariaDB/server/commit/5a42a114fd)\
  2020-02-17 13:56:41 +0200
  * Add missing files.
* [Revision #1a73b995fc](https://github.com/MariaDB/server/commit/1a73b995fc)\
  2020-01-31 08:05:41 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #4eb4d07856](https://github.com/MariaDB/server/commit/4eb4d07856)\
  2020-02-14 08:20:52 +0200
  * Fix Galera test galera\_as\_slave\_ctas.
* [Revision #9ab171edd6](https://github.com/MariaDB/server/commit/9ab171edd6)\
  2020-02-13 17:06:02 +0200
  * [MDEV-21420](https://jira.mariadb.org/browse/MDEV-21420) : Galera test failure on galera.mysql-wsrep#33
* [Revision #38414b2bd0](https://github.com/MariaDB/server/commit/38414b2bd0)\
  2020-02-13 14:13:12 +0200
  * [MDEV-21514](https://jira.mariadb.org/browse/MDEV-21514) : Galera test failure on galera.galera\_wan\_restart\_sst on Azure
* [Revision #2cff542892](https://github.com/MariaDB/server/commit/2cff542892)\
  2019-11-28 17:37:57 +0500
  * [MDEV-21140](https://jira.mariadb.org/browse/MDEV-21140) Make galera\_recovery.sh work with fs.protected\_regular = 1 (#1417)
* [Revision #ba3e9d0adb](https://github.com/MariaDB/server/commit/ba3e9d0adb)\
  2020-02-13 12:38:15 +0200
  * [MDEV-18180](https://jira.mariadb.org/browse/MDEV-18180) : Galera test failure on galera.galera\_concurrent\_ctas
* [Revision #7002948bc5](https://github.com/MariaDB/server/commit/7002948bc5)\
  2020-02-12 11:29:37 +0200
  * [MDEV-21517](https://jira.mariadb.org/browse/MDEV-21517) : Galera test galera\_sr.GCF-561 failure: Result length mismatch
* [Revision #a3f3d40b33](https://github.com/MariaDB/server/commit/a3f3d40b33)\
  2020-02-13 08:32:59 +0200
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #5007633c10](https://github.com/MariaDB/server/commit/5007633c10)\
  2020-01-31 08:05:41 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #9f71804110](https://github.com/MariaDB/server/commit/9f71804110)\
  2020-02-13 23:50:17 +0300
  * [MDEV-21628](https://jira.mariadb.org/browse/MDEV-21628): Index condition pushdown condition ... not used with BKA
* [Revision #8eb0384556](https://github.com/MariaDB/server/commit/8eb0384556)\
  2020-02-14 20:32:46 +1100
  * mysys: remove windac my\_security\_attr\_create (#1391)
* [Revision #c400a73d7a](https://github.com/MariaDB/server/commit/c400a73d7a)\
  2020-02-13 16:26:47 +0300
  * micro optimization: avoid std::string copy
* [Revision #1394216e3d](https://github.com/MariaDB/server/commit/1394216e3d)\
  2020-02-07 23:43:52 +0400
  * [MDEV-21669](https://jira.mariadb.org/browse/MDEV-21669) InnoDB: Table ... contains indexes inside InnoDB, which is different from the number of indexes defined in the MariaDB
* [Revision #c5e00fea10](https://github.com/MariaDB/server/commit/c5e00fea10)\
  2019-11-01 19:18:47 +0400
  * [MDEV-20867](https://jira.mariadb.org/browse/MDEV-20867) - Perform careful review of "Server crashes with BACKUP STAGE and FLUSH TABLE table\_name"
* [Revision #9d7ed94f6a](https://github.com/MariaDB/server/commit/9d7ed94f6a)\
  2020-03-11 10:58:53 +0100
  * CMake cleanup - simplify create\_initial\_db.cmake
* [Revision #574d8b2940](https://github.com/MariaDB/server/commit/574d8b2940)\
  2020-03-10 20:05:17 +0200
  * [MDEV-21907](https://jira.mariadb.org/browse/MDEV-21907): Fix most clang -Wconversion in InnoDB
* [Revision #6ec3682371](https://github.com/MariaDB/server/commit/6ec3682371)\
  2020-03-11 08:28:45 +0200
  * [MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743): Re-record --big-test results
* [Revision #4f4fccecb2](https://github.com/MariaDB/server/commit/4f4fccecb2)\
  2020-03-11 08:27:36 +0200
  * Fix perfschema.statement\_program\_concurrency
* [Revision #0e04beb28f](https://github.com/MariaDB/server/commit/0e04beb28f)\
  2020-03-11 00:35:30 +0400
  * Recoding new suite/perfschema/r/start\_server\_low\_digest\_sql\_length.result
* [Revision #a1e330de5a](https://github.com/MariaDB/server/commit/a1e330de5a)\
  2020-02-28 21:59:01 +0400
  * [MDEV-21743](https://jira.mariadb.org/browse/MDEV-21743) Split up SUPER privilege to smaller privileges
* [Revision #91ba789aaf](https://github.com/MariaDB/server/commit/91ba789aaf)\
  2020-03-10 20:36:18 +0100
  * fix for VALGRIND build
* [Revision #7676208ce6](https://github.com/MariaDB/server/commit/7676208ce6)\
  2020-03-10 20:12:30 +0100
  * Fixed problem of exiting over 32 bit on windows.
* [Revision #43460839dd](https://github.com/MariaDB/server/commit/43460839dd)\
  2020-03-09 16:59:12 +0100
  * [MDEV-21795](https://jira.mariadb.org/browse/MDEV-21795) 10.5 with bundled pcre2 and embedded server could not be built
* [Revision #7180afa094](https://github.com/MariaDB/server/commit/7180afa094)\
  2020-03-07 15:12:02 +0100
  * fix perfschema for pool-of-threads
* [Revision #a9b8131d99](https://github.com/MariaDB/server/commit/a9b8131d99)\
  2020-03-02 20:25:19 +0100
  * cleanup: remove source files that aren't used
* [Revision #cbede21d0d](https://github.com/MariaDB/server/commit/cbede21d0d)\
  2020-02-27 16:00:43 +0100
  * cleanup: pass trxid by value
* [Revision #211421d5cc](https://github.com/MariaDB/server/commit/211421d5cc)\
  2020-02-27 15:26:27 +0100
  * cleanup: remove unused argument
* [Revision #c1c5222cae](https://github.com/MariaDB/server/commit/c1c5222cae)\
  2020-02-27 11:52:20 +0100
  * cleanup: PSI key is _always_ the first argument
* [Revision #7af733a5a2](https://github.com/MariaDB/server/commit/7af733a5a2)\
  2020-02-15 18:25:57 +0100
  * perfschema compilation, test and misc fixes
* [Revision #81cffda2e6](https://github.com/MariaDB/server/commit/81cffda2e6)\
  2020-02-14 16:38:49 +0100
  * perfschema transaction instrumentation related changes
* [Revision #6ded554fc2](https://github.com/MariaDB/server/commit/6ded554fc2)\
  2020-02-14 16:47:59 +0100
  * perfschema thread instrumentation related changes
* [Revision #0d837e8153](https://github.com/MariaDB/server/commit/0d837e8153)\
  2020-02-14 16:40:49 +0100
  * perfschema table io instrumentation related changes
* [Revision #cea187e349](https://github.com/MariaDB/server/commit/cea187e349)\
  2020-02-14 16:53:53 +0100
  * perfschema sysvar instrumentation related changes
* [Revision #7ce517c951](https://github.com/MariaDB/server/commit/7ce517c951)\
  2020-02-14 17:02:08 +0100
  * perfschema status vars instrumentation related changes
* [Revision #d4605bc90f](https://github.com/MariaDB/server/commit/d4605bc90f)\
  2020-02-14 17:05:31 +0100
  * perfschema statement instrumentation related changes
* [Revision #70e7b5095d](https://github.com/MariaDB/server/commit/70e7b5095d)\
  2020-02-14 16:29:16 +0100
  * perfschema sp instrumentation related changes
* [Revision #d5a0069702](https://github.com/MariaDB/server/commit/d5a0069702)\
  2020-02-14 16:25:45 +0100
  * perfschema socket instrumentation related changes
* [Revision #00819d8116](https://github.com/MariaDB/server/commit/00819d8116)\
  2020-02-14 16:59:52 +0100
  * perfschema ps instrumentation related changes
* [Revision #05779bc6f1](https://github.com/MariaDB/server/commit/05779bc6f1)\
  2020-02-14 16:28:05 +0100
  * perfschema mdl related instrumentation changes
* [Revision #22b6d8487a](https://github.com/MariaDB/server/commit/22b6d8487a)\
  2020-02-14 16:25:02 +0100
  * perfschema file instrumentation related changes
* [Revision #7c58e97bf6](https://github.com/MariaDB/server/commit/7c58e97bf6)\
  2020-01-29 13:50:26 +0100
  * perfschema memory related instrumentation changes
* [Revision #2ac3121af2](https://github.com/MariaDB/server/commit/2ac3121af2)\
  2020-02-14 16:42:23 +0100
  * perfschema - various collateral cleanups and small changes
* [Revision #0ea717f51a](https://github.com/MariaDB/server/commit/0ea717f51a)\
  2019-12-10 15:35:00 +0100
  * P\_S 5.7.28
* [Revision #dfe6e914e5](https://github.com/MariaDB/server/commit/dfe6e914e5)\
  2020-02-15 12:29:08 +0100
  * cleanup: remove TYPE\_ENUM\_PROXY from enum stored\_procedure\_type
* [Revision #f3f31eaa8e](https://github.com/MariaDB/server/commit/f3f31eaa8e)\
  2020-01-24 21:10:07 +0100
  * bugfix: in long uniques don't check for duplicates more than once
* [Revision #52d7980753](https://github.com/MariaDB/server/commit/52d7980753)\
  2014-06-12 12:35:55 +0200
  * Bug#18913935: REMOVE SUPPORT FOR LINUXTHREADS
* [Revision #17ea240f6b](https://github.com/MariaDB/server/commit/17ea240f6b)\
  2020-02-27 08:23:13 +0100
  * make pcre2 builds to work on an old cmake
* [Revision #f3e4674a27](https://github.com/MariaDB/server/commit/f3e4674a27)\
  2020-03-10 23:19:12 +0530
  * Fix a compilation bug for 64 bit windows
* [Revision #589a21c631](https://github.com/MariaDB/server/commit/589a21c631)\
  2020-03-10 19:02:53 +0200
  * [MDEV-21580](https://jira.mariadb.org/browse/MDEV-21580): Fix clang -Winconsistent-missing-override
* [Revision #e40858a7bd](https://github.com/MariaDB/server/commit/e40858a7bd)\
  2020-03-10 16:05:42 +0400
  * [MDEV-17832](https://jira.mariadb.org/browse/MDEV-17832) Protocol: extensions for Pluggable types and JSON, GEOMETRY
* [Revision #00749980ac](https://github.com/MariaDB/server/commit/00749980ac)\
  2020-03-10 18:12:11 +0530
  * Fixing a compilation failure on windows
* [Revision #9ae015878f](https://github.com/MariaDB/server/commit/9ae015878f)\
  2020-03-10 15:54:55 +0530
  * [MDEV-10047](https://jira.mariadb.org/browse/MDEV-10047): table-based master info repository
* [Revision #b753ac066b](https://github.com/MariaDB/server/commit/b753ac066b)\
  2020-03-10 04:56:38 +0530
  * [MDEV-21580](https://jira.mariadb.org/browse/MDEV-21580): Allow packed sort keys in sort buffer
* [Revision #561b5ce364](https://github.com/MariaDB/server/commit/561b5ce364)\
  2020-03-10 10:23:04 +0200
  * [MDEV-21748](https://jira.mariadb.org/browse/MDEV-21748) ASAN use-after-poison in PageBulk::insertPage()
* [Revision #e2e2f89303](https://github.com/MariaDB/server/commit/e2e2f89303)\
  2020-03-10 09:34:09 +0200
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528): Minor cleanup
* [Revision #e0e5d8c594](https://github.com/MariaDB/server/commit/e0e5d8c594)\
  2020-03-04 19:10:30 +0200
  * Deb: Update Debian packaging to include mytop and all new man pages
* [Revision #8607076545](https://github.com/MariaDB/server/commit/8607076545)\
  2020-03-04 19:30:34 +0200
  * Add a man page for mytop that is in sources
* [Revision #c7c0959c19](https://github.com/MariaDB/server/commit/c7c0959c19)\
  2020-03-04 19:23:05 +0200
  * Use correct reference in man page links
* [Revision #32fdf81f5c](https://github.com/MariaDB/server/commit/32fdf81f5c)\
  2020-03-04 19:09:16 +0200
  * Fix syntax error mysql-test-run in man page
* [Revision #0335af745c](https://github.com/MariaDB/server/commit/0335af745c)\
  2020-03-04 21:34:56 +0200
  * Add missing man pages for myrocks\_hotbackup
* [Revision #50c0939166](https://github.com/MariaDB/server/commit/50c0939166)\
  2020-01-27 21:50:16 +0100
  * [MDEV-20632](https://jira.mariadb.org/browse/MDEV-20632): Recursive CTE cycle detection using CYCLE clause (nonstandard)
* [Revision #a5584b13d1](https://github.com/MariaDB/server/commit/a5584b13d1)\
  2020-03-10 10:47:24 +0530
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528) Punch holes when pages are freed
* [Revision #a35b4ae898](https://github.com/MariaDB/server/commit/a35b4ae898)\
  2020-03-09 13:25:33 +0530
  * [MDEV-15528](https://jira.mariadb.org/browse/MDEV-15528) Punch holes when pages are freed
* [Revision #980108ceeb](https://github.com/MariaDB/server/commit/980108ceeb)\
  2020-02-03 16:02:05 +0100
  * [MDEV-21833](https://jira.mariadb.org/browse/MDEV-21833) Make slave\_run\_triggers\_for\_rbr enforce triggers to run on slave, even when there are triggers on the master
* [Revision #1f5a8e1f77](https://github.com/MariaDB/server/commit/1f5a8e1f77)\
  2020-03-09 22:49:15 +0400
  * Fixed signed/unsigned error on Windows
* [Revision #dd3ffdbd92](https://github.com/MariaDB/server/commit/dd3ffdbd92)\
  2020-03-02 17:12:35 +0200
  * [MDEV-21659](https://jira.mariadb.org/browse/MDEV-21659) XA rollback foreign\_xid is allowed inside active XA [MDEV-21854](https://jira.mariadb.org/browse/MDEV-21854) xa commit `xid` one phase for already prepared transaction must always error out
* [Revision #f4f6558666](https://github.com/MariaDB/server/commit/f4f6558666)\
  2020-03-09 21:53:52 +0400
  * Attempt fixing build failure on Windows
* [Revision #82e997ad3f](https://github.com/MariaDB/server/commit/82e997ad3f)\
  2020-03-09 18:31:18 +0400
  * [MDEV-21856](https://jira.mariadb.org/browse/MDEV-21856) - xid\_t::formatID has to be constrained to 4 byte size
* [Revision #276e042de3](https://github.com/MariaDB/server/commit/276e042de3)\
  2020-03-09 11:36:06 +0200
  * [MDEV-21893](https://jira.mariadb.org/browse/MDEV-21893): Assertion failure on upgrade with innodb\_encrypt\_log
* [Revision #adb4117631](https://github.com/MariaDB/server/commit/adb4117631)\
  2020-03-09 11:32:31 +0200
  * [MDEV-21892](https://jira.mariadb.org/browse/MDEV-21892): Assertion ...row\_get\_rec\_trx\_id... failed on SELECT
* [Revision #57c592f74d](https://github.com/MariaDB/server/commit/57c592f74d)\
  2020-03-07 14:47:15 +0200
  * Cleanup: Remove recv\_sys.remove\_extra\_log\_files
* [Revision #70f0dbe4d3](https://github.com/MariaDB/server/commit/70f0dbe4d3)\
  2020-03-07 12:01:20 +0200
  * Cleanup: log upgrade and encryption
* [Revision #522fbfcb5c](https://github.com/MariaDB/server/commit/522fbfcb5c)\
  2020-03-07 11:30:45 +0200
  * Cleanup: Remove recv\_sys.buf\_size
* [Revision #0a9633ee62](https://github.com/MariaDB/server/commit/0a9633ee62)\
  2020-03-07 01:26:28 +0300
  * Basic LEX::print function that supports UPDATEs
* [Revision #92eed38c24](https://github.com/MariaDB/server/commit/92eed38c24)\
  2020-03-07 01:20:45 +0300
  * Provide a show\_create\_table\_ex() function
* [Revision #cbbe4971b6](https://github.com/MariaDB/server/commit/cbbe4971b6)\
  2020-03-07 01:14:41 +0300
  * [MDEV-21887](https://jira.mariadb.org/browse/MDEV-21887): federatedx crashes on SELECT ... INTO query in select\_handler code
* [Revision #23685378ba](https://github.com/MariaDB/server/commit/23685378ba)\
  2020-03-06 11:06:59 +0200
  * [MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) preparation: Simplify redo log upgrade
* [Revision #a4ab54d70f](https://github.com/MariaDB/server/commit/a4ab54d70f)\
  2020-03-05 11:45:28 +0200
  * [MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) Cleanup: Use std::atomic for some log\_sys members
* [Revision #555f955a16](https://github.com/MariaDB/server/commit/555f955a16)\
  2020-03-05 11:35:09 +0300
  * use O\_DSYNC for InnoDB
* [Revision #f2832a010a](https://github.com/MariaDB/server/commit/f2832a010a)\
  2020-02-24 23:32:13 +0200
  * [MDEV-14918](https://jira.mariadb.org/browse/MDEV-14918): Use sst\_dump from package rocksdb-tools, don't build it
* [Revision #b464b999c9](https://github.com/MariaDB/server/commit/b464b999c9)\
  2020-02-24 23:22:28 +0200
  * [MDEV-17367](https://jira.mariadb.org/browse/MDEV-17367): Move my\_print\_defaults and \*.sql to mariadb-server-core
* [Revision #4b42fa3ce3](https://github.com/MariaDB/server/commit/4b42fa3ce3)\
  2020-03-05 08:50:13 +0200
  * [MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425): Remove the unused function mtr\_write\_log()
* [Revision #1312b4ebb6](https://github.com/MariaDB/server/commit/1312b4ebb6)\
  2020-03-05 07:31:55 +0200
  * [MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) preparation: Provide ut\_crc32\_low()
* [Revision #6b317c1cc3](https://github.com/MariaDB/server/commit/6b317c1cc3)\
  2020-03-05 07:26:04 +0200
  * Remove some redundant code flagged by clang or GCC
* [Revision #64be4ab4a8](https://github.com/MariaDB/server/commit/64be4ab4a8)\
  2020-03-04 17:06:49 +0200
  * [MDEV-21870](https://jira.mariadb.org/browse/MDEV-21870) Deprecate and ignore innodb\_scrub\_log and innodb\_scrub\_log\_speed
* [Revision #d62766a890](https://github.com/MariaDB/server/commit/d62766a890)\
  2020-02-28 16:55:51 +0200
  * [MDEV-21228](https://jira.mariadb.org/browse/MDEV-21228): mariadb-conv man page
* [Revision #8a25eb666d](https://github.com/MariaDB/server/commit/8a25eb666d)\
  2020-03-04 13:05:22 +0200
  * [MDEV-18214](https://jira.mariadb.org/browse/MDEV-18214) cleanup: Remove redundant MONITOR\_INC calls
* [Revision #9e488653ae](https://github.com/MariaDB/server/commit/9e488653ae)\
  2020-03-04 12:59:20 +0200
  * Cleanup: Make MONITOR\_LSN\_CHECKPOINT\_AGE a value.
* [Revision #4383897a01](https://github.com/MariaDB/server/commit/4383897a01)\
  2020-03-04 10:08:33 +0200
  * [MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) preparation: Remove log\_header\_read()
* [Revision #37e7bde12a](https://github.com/MariaDB/server/commit/37e7bde12a)\
  2020-03-03 22:15:44 +0200
  * [MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) preparation: Remove log\_t::append\_on\_checkpoint
* [Revision #1ef10744ab](https://github.com/MariaDB/server/commit/1ef10744ab)\
  2020-03-03 14:53:04 +0200
  * [MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534): Fix -Wmaybe-uninitialized
* [Revision #a736a2cbc4](https://github.com/MariaDB/server/commit/a736a2cbc4)\
  2020-03-03 14:41:32 +0200
  * [MDEV-21724](https://jira.mariadb.org/browse/MDEV-21724): Correctly invoke page\_dir\_split\_slot()
* [Revision #fae259f036](https://github.com/MariaDB/server/commit/fae259f036)\
  2020-03-03 13:23:04 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Introduce an EXTENDED record subtype TRIM\_PAGES
* [Revision #73dfb402bf](https://github.com/MariaDB/server/commit/73dfb402bf)\
  2020-03-02 20:05:28 +0530
  * [MDEV-20500](https://jira.mariadb.org/browse/MDEV-20500): Bad error msg on disabling local infile
* [Revision #8f8cc5f4c2](https://github.com/MariaDB/server/commit/8f8cc5f4c2)\
  2020-03-03 10:51:47 +0000
  * Merge pull request #1434 from citrus-it/illumos-auth-socket
* [Revision #a3d2d2c4cb](https://github.com/MariaDB/server/commit/a3d2d2c4cb)\
  2020-03-03 13:50:33 +0300
  * [MDEV-21747](https://jira.mariadb.org/browse/MDEV-21747) needless alter\_ctx arg in prep\_alter\_part\_table()
* [Revision #193725b81e](https://github.com/MariaDB/server/commit/193725b81e)\
  2020-03-03 13:50:33 +0300
  * [MDEV-7318](https://jira.mariadb.org/browse/MDEV-7318) RENAME INDEX
* [Revision #fa8ad75439](https://github.com/MariaDB/server/commit/fa8ad75439)\
  2020-03-03 13:50:32 +0300
  * [MDEV-16290](https://jira.mariadb.org/browse/MDEV-16290) ALTER TABLE ... RENAME COLUMN syntax
* [Revision #a99c93a7fa](https://github.com/MariaDB/server/commit/a99c93a7fa)\
  2020-03-02 14:28:01 +0100
  * Fix build on aarch64, after [MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534)
* [Revision #8511f04fdb](https://github.com/MariaDB/server/commit/8511f04fdb)\
  2020-03-02 14:34:52 +0200
  * Cleanup: Remove srv\_start\_lsn
* [Revision #55a5b5baf6](https://github.com/MariaDB/server/commit/55a5b5baf6)\
  2020-03-02 10:07:01 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) cleanup: Simplify mtr\_t::undo\_append()
* [Revision #721ec44e2a](https://github.com/MariaDB/server/commit/721ec44e2a)\
  2020-02-24 22:17:16 +0300
  * [MDEV-14479](https://jira.mariadb.org/browse/MDEV-14479): Do not acquire InnoDB record locks when covering table locks exist
* [Revision #47d8fcf4cd](https://github.com/MariaDB/server/commit/47d8fcf4cd)\
  2020-03-01 23:33:16 +0100
  * [MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534) - fix debug build
* [Revision #30ea63b7d2](https://github.com/MariaDB/server/commit/30ea63b7d2)\
  2020-02-07 22:12:35 +0100
  * [MDEV-21534](https://jira.mariadb.org/browse/MDEV-21534) - Improve innodb redo log group commit performance
* [Revision #607960c772](https://github.com/MariaDB/server/commit/607960c772)\
  2020-02-28 19:08:35 +0400
  * [MDEV-21766](https://jira.mariadb.org/browse/MDEV-21766) - Forbid XID with empty 'gtrid'
* [Revision #e26056e181](https://github.com/MariaDB/server/commit/e26056e181)\
  2020-02-12 18:26:18 +0400
  * [MDEV-21704](https://jira.mariadb.org/browse/MDEV-21704) Add a new JSON field "version\_id" into mysql.global\_priv.priv
* [Revision #0c35e80dc9](https://github.com/MariaDB/server/commit/0c35e80dc9)\
  2020-02-28 11:46:13 +0530
  * [MDEV-21838](https://jira.mariadb.org/browse/MDEV-21838): Add information about packed addon fields in ANALYZE FORMAT=JSON
* [Revision #8db623038f](https://github.com/MariaDB/server/commit/8db623038f)\
  2020-02-27 18:19:31 +0200
  * Fix GCC -Wsign-compare
* [Revision #a263ca26db](https://github.com/MariaDB/server/commit/a263ca26db)\
  2020-02-27 17:51:59 +0200
  * Fix GCC -Wparentheses
* [Revision #138cbec5f2](https://github.com/MariaDB/server/commit/138cbec5f2)\
  2020-02-27 17:19:44 +0200
  * [MDEV-21724](https://jira.mariadb.org/browse/MDEV-21724): Optimize page\_cur\_insert\_low() redo logging
* [Revision #dee6fb356b](https://github.com/MariaDB/server/commit/dee6fb356b)\
  2020-02-27 15:14:47 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) Cleanup: Remove page\_rec\_get\_base\_extra\_size()
* [Revision #e15ae1cfe1](https://github.com/MariaDB/server/commit/e15ae1cfe1)\
  2020-02-26 09:57:00 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Improve page\_cur\_delete\_rec() recovery
* [Revision #4431144ae5](https://github.com/MariaDB/server/commit/4431144ae5)\
  2020-02-26 09:58:31 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Make UNDO\_APPEND more robust
* [Revision #a346ff353e](https://github.com/MariaDB/server/commit/a346ff353e)\
  2020-02-27 18:04:06 +0400
  * cleanup trailing ws
* [Revision #127fee998f](https://github.com/MariaDB/server/commit/127fee998f)\
  2020-01-15 15:08:42 +0300
  * [MDEV-10569](https://jira.mariadb.org/browse/MDEV-10569): Add RELEASE\_ALL\_LOCKS function. Implementing the SQL function to release all named locks
* [Revision #98adcffe46](https://github.com/MariaDB/server/commit/98adcffe46)\
  2020-02-27 10:28:49 +0100
  * Revert "[MDEV-17554](https://jira.mariadb.org/browse/MDEV-17554) Auto-create new partition for system versioned tables with history partitioned by INTERVAL/LIMIT"
* [Revision #9894751a2a](https://github.com/MariaDB/server/commit/9894751a2a)\
  2020-02-25 20:58:03 +0300
  * Compilation fix
* [Revision #f707c83fff](https://github.com/MariaDB/server/commit/f707c83fff)\
  2020-02-25 14:14:17 +0300
  * [MDEV-17554](https://jira.mariadb.org/browse/MDEV-17554) Auto-create new partition for system versioned tables with history partitioned by INTERVAL/LIMIT
* [Revision #c12609dd9e](https://github.com/MariaDB/server/commit/c12609dd9e)\
  2020-02-11 11:29:19 +0530
  * Review comments: Refactoring the duplicates
* [Revision #193bc89a49](https://github.com/MariaDB/server/commit/193bc89a49)\
  2020-01-28 19:21:20 +0530
  * Adding s390x to Travis builds
* [Revision #852dcb9a56](https://github.com/MariaDB/server/commit/852dcb9a56)\
  2020-02-24 17:15:07 +0300
  * try to fix sysvars\_innodb,32bit test
* [Revision #0eca30a70d](https://github.com/MariaDB/server/commit/0eca30a70d)\
  2020-02-24 16:12:48 +0200
  * [MDEV-21749](https://jira.mariadb.org/browse/MDEV-21749): page\_cur\_insert\_rec\_low(): Assertion rdm - rd + bd <= insert\_buf + rec\_size failed.
* [Revision #956e12d639](https://github.com/MariaDB/server/commit/956e12d639)\
  2020-02-24 15:13:00 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Fix cmake -DWITH\_INNODB\_EXTRA\_DEBUG
* [Revision #572d20757b](https://github.com/MariaDB/server/commit/572d20757b)\
  2020-02-22 17:32:45 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Reduce log volume of page\_cur\_delete\_rec()
* [Revision #bc76cfe8f8](https://github.com/MariaDB/server/commit/bc76cfe8f8)\
  2020-02-21 11:57:29 +0200
  * Disable galera\_as\_slave\_gtid\_replicate\_do\_db\_cc because it crashes.
* [Revision #e253e3560d](https://github.com/MariaDB/server/commit/e253e3560d)\
  2020-02-21 08:28:20 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #17e1848b66](https://github.com/MariaDB/server/commit/17e1848b66)\
  2020-02-14 08:20:52 +0200
  * Fix Galera test galera\_as\_slave\_ctas.
* [Revision #d872cd6e4a](https://github.com/MariaDB/server/commit/d872cd6e4a)\
  2020-02-13 17:06:02 +0200
  * [MDEV-21420](https://jira.mariadb.org/browse/MDEV-21420) : Galera test failure on galera.mysql-wsrep#33
* [Revision #929e44b245](https://github.com/MariaDB/server/commit/929e44b245)\
  2020-02-13 14:13:12 +0200
  * [MDEV-21514](https://jira.mariadb.org/browse/MDEV-21514) : Galera test failure on galera.galera\_wan\_restart\_sst on Azure
* [Revision #316e41e39e](https://github.com/MariaDB/server/commit/316e41e39e)\
  2019-11-28 17:37:57 +0500
  * [MDEV-21140](https://jira.mariadb.org/browse/MDEV-21140) Make galera\_recovery.sh work with fs.protected\_regular = 1 (#1417)
* [Revision #713c5ea5bc](https://github.com/MariaDB/server/commit/713c5ea5bc)\
  2020-02-13 12:38:15 +0200
  * [MDEV-18180](https://jira.mariadb.org/browse/MDEV-18180) : Galera test failure on galera.galera\_concurrent\_ctas
* [Revision #77eb22fd58](https://github.com/MariaDB/server/commit/77eb22fd58)\
  2020-02-12 11:29:37 +0200
  * [MDEV-21517](https://jira.mariadb.org/browse/MDEV-21517) : Galera test galera\_sr.GCF-561 failure: Result length mismatch
* [Revision #6cc819b413](https://github.com/MariaDB/server/commit/6cc819b413)\
  2020-02-13 08:32:59 +0200
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #4b99358953](https://github.com/MariaDB/server/commit/4b99358953)\
  2020-02-21 08:25:20 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #96901d9545](https://github.com/MariaDB/server/commit/96901d9545)\
  2020-02-20 22:00:43 +0200
  * Cleanup: Remove dict\_ind\_redundant
* [Revision #6618fc2974](https://github.com/MariaDB/server/commit/6618fc2974)\
  2020-02-19 15:44:33 +0300
  * [MDEV-21774](https://jira.mariadb.org/browse/MDEV-21774) Innodb, Windows : restore file sharing logic in Innodb
* [Revision #84e3f9ce84](https://github.com/MariaDB/server/commit/84e3f9ce84)\
  2020-02-19 16:42:38 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Reduce log volume by an UNDO\_APPEND record
* [Revision #86f262f1c7](https://github.com/MariaDB/server/commit/86f262f1c7)\
  2020-02-19 10:58:04 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Reduce log volume by an UNDO\_INIT record
* [Revision #3ee100b0d1](https://github.com/MariaDB/server/commit/3ee100b0d1)\
  2020-02-19 16:39:02 +0300
  * revert accidental libmariadb change
* [Revision #29bb3744b4](https://github.com/MariaDB/server/commit/29bb3744b4)\
  2020-02-19 16:37:06 +0300
  * fix libpmem InnoDB linking
* [Revision #e62e285fc4](https://github.com/MariaDB/server/commit/e62e285fc4)\
  2020-02-19 12:51:08 +0300
  * remove unused function
* [Revision #9ef2d29ff4](https://github.com/MariaDB/server/commit/9ef2d29ff4)\
  2020-01-12 02:05:28 +0700
  * [MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) deprecate and ignore innodb\_log\_files\_in\_group
* [Revision #8d7a8e45bf](https://github.com/MariaDB/server/commit/8d7a8e45bf)\
  2020-02-19 09:35:48 +0200
  * Update wsrep-lib submodule.
* [Revision #9fd309498c](https://github.com/MariaDB/server/commit/9fd309498c)\
  2020-02-18 11:30:30 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) Cleanup: Rename INIT\_INDEX\_PAGE to EXTENDED
* [Revision #802a6b0a33](https://github.com/MariaDB/server/commit/802a6b0a33)\
  2020-02-18 10:54:56 +0200
  * Reduce innodb\_log\_buffer\_size
* [Revision #23de5b8f07](https://github.com/MariaDB/server/commit/23de5b8f07)\
  2020-02-18 10:54:28 +0200
  * [MDEV-21725](https://jira.mariadb.org/browse/MDEV-21725) Optimize btr\_page\_reorganize\_low() redo logging
* [Revision #41fe972db7](https://github.com/MariaDB/server/commit/41fe972db7)\
  2020-02-17 15:26:08 +0200
  * [MDEV-21744](https://jira.mariadb.org/browse/MDEV-21744) Assertion \`!rec\_offs\_nth\_sql\_null(offsets, n)' failed
* [Revision #055ce75d8b](https://github.com/MariaDB/server/commit/055ce75d8b)\
  2020-02-17 14:52:20 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Correct a debug assertion failure
* [Revision #22f649a67a](https://github.com/MariaDB/server/commit/22f649a67a)\
  2020-02-17 13:30:01 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Reformat page\_delete\_rec\_list\_end()
* [Revision #09feb176e9](https://github.com/MariaDB/server/commit/09feb176e9)\
  2020-02-17 10:49:42 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Optimize page\_cur\_delete\_rec() logging further
* [Revision #0683c8f7a2](https://github.com/MariaDB/server/commit/0683c8f7a2)\
  2020-02-17 13:32:36 +0200
  * Clarify, spelling for wsrep\_strict\_ddl description (#1447)
* [Revision #fc87698048](https://github.com/MariaDB/server/commit/fc87698048)\
  2020-02-17 10:13:32 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Write less log for BLOB pages
* [Revision #5874aac71f](https://github.com/MariaDB/server/commit/5874aac71f)\
  2020-02-16 17:22:28 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Fix a Galera assertion failure
* [Revision #d657cd7465](https://github.com/MariaDB/server/commit/d657cd7465)\
  2020-02-16 15:45:12 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Optimize page\_delete\_rec\_list\_end() logging
* [Revision #5876de19d0](https://github.com/MariaDB/server/commit/5876de19d0)\
  2020-02-16 15:09:01 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Remove bogus conditions
* [Revision #3887daf826](https://github.com/MariaDB/server/commit/3887daf826)\
  2020-02-16 14:10:26 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Optimize page\_cur\_delete\_rec() logging
* [Revision #2c34315df6](https://github.com/MariaDB/server/commit/2c34315df6)\
  2020-02-14 10:46:08 -0500
  * bump the VERSION
* [Revision #444c83b2ac](https://github.com/MariaDB/server/commit/444c83b2ac)\
  2020-02-14 14:40:16 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Test InnoDB upgrade from multi-file redo log
* [Revision #735c6ea3e6](https://github.com/MariaDB/server/commit/735c6ea3e6)\
  2020-02-14 15:45:18 +0300
  * fix Win build
* [Revision #3daef523af](https://github.com/MariaDB/server/commit/3daef523af)\
  2020-02-09 22:10:28 +0400
  * [MDEV-17084](https://jira.mariadb.org/browse/MDEV-17084) Optimize append only files for NVDIMM
* [Revision #d901919db2](https://github.com/MariaDB/server/commit/d901919db2)\
  2020-02-14 11:03:11 +0200
  * [MDEV-19747](https://jira.mariadb.org/browse/MDEV-19747): Fix a warning
* [Revision #37dc087f58](https://github.com/MariaDB/server/commit/37dc087f58)\
  2020-02-14 10:56:43 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Remove bogus comments and clean up code
* Merge [Revision #dd87a8b316](https://github.com/MariaDB/server/commit/dd87a8b316) 2020-02-14 09:16:30 +0100 - Merge commit 'bb-10.5-release' into 10.5
* [Revision #f8a9f90667](https://github.com/MariaDB/server/commit/f8a9f90667)\
  2020-02-13 19:13:45 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Remove support for crash-upgrade
* [Revision #7ae21b18a6](https://github.com/MariaDB/server/commit/7ae21b18a6)\
  2020-02-13 19:12:17 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Change the redo log encoding
* [Revision #9869005201](https://github.com/MariaDB/server/commit/9869005201)\
  2020-01-13 17:37:37 +0200
  * Cleanup ibuf\_page\_exists(): Take simpler parameters
* [Revision #67c76704a8](https://github.com/MariaDB/server/commit/67c76704a8)\
  2020-01-29 15:13:08 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Remove MLOG\_INDEX\_LOAD (innodb\_log\_optimize\_ddl)
* [Revision #f37a29dd66](https://github.com/MariaDB/server/commit/f37a29dd66)\
  2020-01-21 15:46:20 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Write log by mtr\_t member functions only
* [Revision #8a039ee107](https://github.com/MariaDB/server/commit/8a039ee107)\
  2020-01-22 20:12:08 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Introduce mtr\_t::zmemcpy()
* [Revision #2e7a084283](https://github.com/MariaDB/server/commit/2e7a084283)\
  2020-01-22 20:02:39 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174): Remove mlog\_write\_initial\_log\_record\_fast()
* [Revision #498f84a87b](https://github.com/MariaDB/server/commit/498f84a87b)\
  2019-12-12 18:34:47 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Remove mlog\_open\_and\_write\_index()
* [Revision #08ba388713](https://github.com/MariaDB/server/commit/08ba388713)\
  2020-02-13 12:33:27 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\_REC\_INSERT,MLOG\_COMP\_REC\_INSERT
* [Revision #2c4d5aa0fe](https://github.com/MariaDB/server/commit/2c4d5aa0fe)\
  2020-01-21 15:20:08 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\_ZIP\_PAGE\_COMPRESS
* [Revision #2a77b2a510](https://github.com/MariaDB/server/commit/2a77b2a510)\
  2020-02-13 11:41:54 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\__LIST\_DELETE and MLOG_\*REC\_DELETE
* [Revision #d00185c40d](https://github.com/MariaDB/server/commit/d00185c40d)\
  2019-12-11 18:04:34 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\_PAGE\_CREATE\_RTREE, MLOG\_PAGE\_COMP\_CREATE\_RTREE
* [Revision #b3d02a1fcf](https://github.com/MariaDB/server/commit/b3d02a1fcf)\
  2020-02-07 13:03:02 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace DELETE\_MARK redo log records with MLOG\_WRITE\_STRING
* [Revision #f3230111fc](https://github.com/MariaDB/server/commit/f3230111fc)\
  2019-12-11 16:54:17 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Introduce MLOG\_ZIP\_WRITE\_STRING
* [Revision #db5cdc3195](https://github.com/MariaDB/server/commit/db5cdc3195)\
  2020-01-22 18:52:36 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\_PAGE\_REORGANIZE, MLOG\_COMP\_PAGE\_REORGANIZE
* [Revision #276f996af9](https://github.com/MariaDB/server/commit/276f996af9)\
  2020-01-22 18:51:29 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\_\*\_END\_COPY\_CREATED
* [Revision #acd265b69b](https://github.com/MariaDB/server/commit/acd265b69b)\
  2019-06-17 15:38:14 +0300
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Exclusively use page\_zip\_reorganize() for ROW\_FORMAT=COMPRESSED
* [Revision #f802c989ec](https://github.com/MariaDB/server/commit/f802c989ec)\
  2019-12-09 17:13:48 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\_UNDO\_INSERT
* [Revision #e0bc29df18](https://github.com/MariaDB/server/commit/e0bc29df18)\
  2019-12-09 16:53:04 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\_UNDO\_HDR\_CREATE
* [Revision #737b701786](https://github.com/MariaDB/server/commit/737b701786)\
  2019-12-09 16:39:45 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Remove trx\_undo\_erase\_page\_end()
* [Revision #07d39cde92](https://github.com/MariaDB/server/commit/07d39cde92)\
  2019-12-09 16:26:14 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Replace MLOG\_UNDO\_INIT
* [Revision #5bea43f5e0](https://github.com/MariaDB/server/commit/5bea43f5e0)\
  2019-12-09 15:55:48 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Deprecate and ignore innodb\_log\_compressed\_pages
* [Revision #600eae9179](https://github.com/MariaDB/server/commit/600eae9179)\
  2020-02-07 13:33:51 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353): Remove MTR\_LOG\_SHORT\_INSERTS

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
