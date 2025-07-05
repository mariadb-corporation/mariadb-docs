# MariaDB 10.2.8 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/release-notes-mariadb-10-2-series/mariadb-10244-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.8)[Release Notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md)[Changelog](mariadb-1028-changelog.md)[Overview of 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)

**Release date:** 18 Aug 2017

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-2-series/mariadb-1028-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #c548fb0667](https://github.com/MariaDB/server/commit/c548fb0667)\
  2017-08-16 19:18:39 +0200
  * [MDEV-11240](https://jira.mariadb.org/browse/MDEV-11240): Server crashes in check\_view\_single\_update or Assertion \`derived->table' failed in mysql\_derived\_merge\_for\_insert
* Merge [Revision #cb1e76e4de](https://github.com/MariaDB/server/commit/cb1e76e4de) 2017-08-17 11:32:16 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #48fe832650](https://github.com/MariaDB/server/commit/48fe832650) 2017-08-15 09:50:31 +0200 - Merge branch '10.0' into 10.1
* [Revision #7581fb23e2](https://github.com/MariaDB/server/commit/7581fb23e2)\
  2017-08-14 18:37:53 +0200
  * compilation fix for SLES 11 SP4
* [Revision #fc556a8d94](https://github.com/MariaDB/server/commit/fc556a8d94)\
  2017-08-10 12:03:48 +0200
  * compilation fix for SLES 11 SP4
* [Revision #3e20a42bfb](https://github.com/MariaDB/server/commit/3e20a42bfb)\
  2017-08-11 13:59:53 +0400
  * [MDEV-8579](https://jira.mariadb.org/browse/MDEV-8579) - Some sysvars in I\_S are missing any meaningful help (comment) text
* [Revision #f066c89a97](https://github.com/MariaDB/server/commit/f066c89a97)\
  2017-08-10 16:02:54 +0200
  * [MDEV-8579](https://jira.mariadb.org/browse/MDEV-8579) Expand system variable documentation
* [Revision #a4c882f0e5](https://github.com/MariaDB/server/commit/a4c882f0e5)\
  2017-08-13 23:47:26 +0200
  * allow OpenSSL 0.9.8 again
* [Revision #1ff65c271f](https://github.com/MariaDB/server/commit/1ff65c271f)\
  2017-08-10 10:16:05 -0400
  * bump the VERSION
* Merge [Revision #31e794bcac](https://github.com/MariaDB/server/commit/31e794bcac) 2017-08-09 17:14:40 +0300 - Merge 10.0 into 10.1
* [Revision #cb9648a6b5](https://github.com/MariaDB/server/commit/cb9648a6b5)\
  2017-08-09 14:29:22 +0300
  * Revert an InnoDB Memcached plugin fix that was merged from MySQL 5.6.37
* [Revision #a4885dde4c](https://github.com/MariaDB/server/commit/a4885dde4c)\
  2017-08-16 18:44:17 +0200
  * [MDEV-13535](https://jira.mariadb.org/browse/MDEV-13535) Query on MyISAM table corrupts the table
* [Revision #1b7e55900a](https://github.com/MariaDB/server/commit/1b7e55900a)\
  2017-08-16 13:26:53 +0200
  * CONNECT: compilation fix
* [Revision #158f96f6e3](https://github.com/MariaDB/server/commit/158f96f6e3)\
  2017-08-16 13:25:57 +0200
  * CONNECT: fix the test to use tcp not unix socket
* Merge [Revision #678fb208e4](https://github.com/MariaDB/server/commit/678fb208e4) 2017-08-16 18:16:50 +0200 - Merge branch 'connect/10.2' into 10.2
* [Revision #60fa113f51](https://github.com/MariaDB/server/commit/60fa113f51)\
  2017-08-12 18:32:32 +0200
  * Fix [MDEV-13503](https://jira.mariadb.org/browse/MDEV-13503)
* [Revision #efc8a5b689](https://github.com/MariaDB/server/commit/efc8a5b689)\
  2017-08-09 12:50:06 +0200
  * Fix gcc compile error: crosses initialization of const char\* drv
* [Revision #3523c12eb0](https://github.com/MariaDB/server/commit/3523c12eb0)\
  2017-08-09 01:37:06 +0200
  * Re-Re-trying to fix Linux compile on DWORD
* [Revision #272b397748](https://github.com/MariaDB/server/commit/272b397748)\
  2017-08-09 01:23:48 +0200
  * Re-trying to fix Linux compile on DWORD
* [Revision #7947121e9a](https://github.com/MariaDB/server/commit/7947121e9a)\
  2017-08-08 22:36:22 +0200
  * Trying to fix Linux compile on DWORDW
* [Revision #4d4ba60c6e](https://github.com/MariaDB/server/commit/4d4ba60c6e)\
  2017-08-08 17:36:54 +0200
  * Fix [MDEV-13463](https://jira.mariadb.org/browse/MDEV-13463) unescape table name during detection of table structure
* [Revision #017d9ccf5d](https://github.com/MariaDB/server/commit/017d9ccf5d)\
  2017-08-08 11:32:35 +0200
  * Fix Linux compile error by #define NODW
* [Revision #cdf00b8d92](https://github.com/MariaDB/server/commit/cdf00b8d92)\
  2017-08-07 16:24:53 +0200
  * Fix bug returning pointer to a stack string in JVALUE::GetString
* [Revision #f5b0993bbd](https://github.com/MariaDB/server/commit/f5b0993bbd)\
  2017-08-06 22:01:18 +0200
  * Fix Linux compile error by #define NODW
* [Revision #0387c13ee7](https://github.com/MariaDB/server/commit/0387c13ee7)\
  2017-08-06 19:56:57 +0200
  * Add a define making ha\_connect.cc source unique for all MariaDB version. #if defined(NEW\_MAR) #define stored\_in\_db stored\_in\_db() #endif NEW\_MAR)
* [Revision #d8f99f165b](https://github.com/MariaDB/server/commit/d8f99f165b)\
  2017-08-05 18:08:51 +0200
  * Add FBLOCK when opening ODBC, JSON and MONGO tables. This to have automatic closing in case of thrown error
* [Revision #df3fd420e5](https://github.com/MariaDB/server/commit/df3fd420e5)\
  2017-07-28 21:13:19 +0200
  * wrapname hidden when no JDBC support
* [Revision #13b26f84bd](https://github.com/MariaDB/server/commit/13b26f84bd)\
  2017-07-28 15:39:31 +0200
  * \-- Fix wrong setting of Pipe
* [Revision #c51b1a1f60](https://github.com/MariaDB/server/commit/c51b1a1f60)\
  2017-07-25 00:40:42 +0200
  * Update storage/connect/JavaWrappers.jar
* [Revision #f5cd810629](https://github.com/MariaDB/server/commit/f5cd810629)\
  2017-07-25 00:21:45 +0200
  * Update storage/connect/JavaWrappers.jar
* [Revision #376d1c433c](https://github.com/MariaDB/server/commit/376d1c433c)\
  2017-07-24 00:05:07 +0200
  * Update storage/connect/JavaWrappers.jar
* [Revision #510e67c6fd](https://github.com/MariaDB/server/commit/510e67c6fd)\
  2017-07-23 12:41:44 +0200
  * Fix discovery crash for Java Mongo tables
* [Revision #7388f95319](https://github.com/MariaDB/server/commit/7388f95319)\
  2017-07-23 11:58:20 +0200
  * \-- Last wrappers version with support of Java Mongo discovery
* [Revision #cfe3252afe](https://github.com/MariaDB/server/commit/cfe3252afe)\
  2017-07-22 17:23:26 +0200
  * \-- No suppressing of the GetPlug function. It is GetUser that can cause memory leak when xp is modified. The old xp must be poped or is never freed
* [Revision #3329fbae19](https://github.com/MariaDB/server/commit/3329fbae19)\
  2017-07-22 00:21:59 +0200
  * \-- Suppress the GetPlug function causing memory leak
* [Revision #6fdd5cda6a](https://github.com/MariaDB/server/commit/6fdd5cda6a)\
  2017-07-21 16:26:08 +0200
  * Fix compile error
* [Revision #8476d3052a](https://github.com/MariaDB/server/commit/8476d3052a)\
  2017-07-21 15:24:13 +0200
  * \-- Add mutex for user\_connect handling
* [Revision #df091237a8](https://github.com/MariaDB/server/commit/df091237a8)\
  2017-07-20 11:19:44 +0200
  * Modified /storage/connect/value.cpp line 668
* [Revision #e99af2a3fa](https://github.com/MariaDB/server/commit/e99af2a3fa)\
  2017-07-19 23:30:40 +0200
  * \-- Fix warnings from the new GCC 7
* [Revision #ad2a4c42b6](https://github.com/MariaDB/server/commit/ad2a4c42b6)\
  2017-07-19 18:31:40 +0200
  * Parenthesize set null in SetValue\_pval
* [Revision #e05920f783](https://github.com/MariaDB/server/commit/e05920f783)\
  2017-07-19 00:16:58 +0200
  * \-- Check whether USERBLK still exists in PlugExit
* [Revision #38c9c0d22b](https://github.com/MariaDB/server/commit/38c9c0d22b)\
  2017-07-18 16:12:32 +0200
  * Fix compile warnings and errors for nullptr
* [Revision #f590296c28](https://github.com/MariaDB/server/commit/f590296c28)\
  2017-07-18 13:16:55 +0200
  * \-- Finalize work on MongoDB access Implement discovery for the MongoDB Java Driver Create classes to minimize code and avoid dupicates Rearrange and rename implied files
* [Revision #58b56f14a0](https://github.com/MariaDB/server/commit/58b56f14a0)\
  2017-08-16 12:44:46 +0200
  * cleanup: remove ha\_innopart.cc
* [Revision #b3a4bc481b](https://github.com/MariaDB/server/commit/b3a4bc481b)\
  2017-08-16 14:36:03 +0300
  * [MDEV-13513](https://jira.mariadb.org/browse/MDEV-13513): rocksdb.drop\_table fails in buidbot with assertion failure
* [Revision #a28152aafc](https://github.com/MariaDB/server/commit/a28152aafc)\
  2017-08-15 15:37:10 -0700
  * Fixed the bug [MDEV-13346](https://jira.mariadb.org/browse/MDEV-13346).
* [Revision #c354cb66b0](https://github.com/MariaDB/server/commit/c354cb66b0)\
  2017-08-15 16:42:11 +0300
  * [MDEV-13515](https://jira.mariadb.org/browse/MDEV-13515): rocksdb.use\_direct\_reads\_writes fails in buildbot with not found pattern
* [Revision #5d1c0d0086](https://github.com/MariaDB/server/commit/5d1c0d0086)\
  2017-08-15 10:11:26 +0300
  * [MDEV-13331](https://jira.mariadb.org/browse/MDEV-13331) FK DELETE CASCADE does not honor innodb\_lock\_wait\_timeout
* [Revision #2f342c4507](https://github.com/MariaDB/server/commit/2f342c4507)\
  2017-08-14 16:01:08 +0300
  * [MDEV-13498](https://jira.mariadb.org/browse/MDEV-13498) DELETE with CASCADE constraints takes long time / [MDEV-13246](https://jira.mariadb.org/browse/MDEV-13246)
* [Revision #b4f6b678a6](https://github.com/MariaDB/server/commit/b4f6b678a6)\
  2017-08-14 15:55:04 +0300
  * [MDEV-13520](https://jira.mariadb.org/browse/MDEV-13520) InnoDB attempts UPDATE with DB\_TRX\_ID=0 if innodb\_force\_recovery=3
* [Revision #a5e4365eb9](https://github.com/MariaDB/server/commit/a5e4365eb9)\
  2017-08-14 12:46:26 +0300
  * Fix a test result
* [Revision #c724fcd7a0](https://github.com/MariaDB/server/commit/c724fcd7a0)\
  2017-08-15 01:11:37 +0200
  * [MDEV-13525](https://jira.mariadb.org/browse/MDEV-13525) mtr and mysql-test-run symlinks are not installed anymore
* [Revision #88879b37fc](https://github.com/MariaDB/server/commit/88879b37fc)\
  2017-08-14 23:39:35 +0300
  * Changes to RocksDB tests after the engine merge
* [Revision #d24f76e1a8](https://github.com/MariaDB/server/commit/d24f76e1a8)\
  2017-08-14 23:12:35 +0300
  * [MDEV-13522](https://jira.mariadb.org/browse/MDEV-13522): rocksdb.rocksdb\_parts failed in buildbot
* [Revision #fa7016cec1](https://github.com/MariaDB/server/commit/fa7016cec1)\
  2017-08-13 19:37:41 +0200
  * un-disable a bunch of funcs\_1 tests
* [Revision #b2af0ddcf9](https://github.com/MariaDB/server/commit/b2af0ddcf9)\
  2017-08-13 19:12:36 +0200
  * enable innodb tests for virtual indexed columns (sic!)
* [Revision #399e14f066](https://github.com/MariaDB/server/commit/399e14f066)\
  2017-08-13 01:08:30 +0200
  * [MDEV-13435](https://jira.mariadb.org/browse/MDEV-13435) Crash when selecting virtual columns generated using JSON functions
* [Revision #d924e0b993](https://github.com/MariaDB/server/commit/d924e0b993)\
  2017-08-12 19:09:03 +0200
  * [MDEV-13375](https://jira.mariadb.org/browse/MDEV-13375) back\_log ignored
* [Revision #d07daa3125](https://github.com/MariaDB/server/commit/d07daa3125)\
  2017-08-12 18:54:05 +0200
  * [MDEV-13313](https://jira.mariadb.org/browse/MDEV-13313) JSON type alias is insufficiently compatible
* [Revision #04b288ae47](https://github.com/MariaDB/server/commit/04b288ae47)\
  2017-08-12 18:52:38 +0200
  * [MDEV-11114](https://jira.mariadb.org/browse/MDEV-11114) Cannot drop column referenced by CHECK constraint
* [Revision #28ddc9b3bb](https://github.com/MariaDB/server/commit/28ddc9b3bb)\
  2017-08-12 17:36:47 +0200
  * small cleanup
* [Revision #87f39bf824](https://github.com/MariaDB/server/commit/87f39bf824)\
  2017-08-12 13:07:33 +0200
  * [MDEV-8659](https://jira.mariadb.org/browse/MDEV-8659) Conflicting declaration is accepted: INT SIGNED ZEROFILL
* [Revision #40eff5e097](https://github.com/MariaDB/server/commit/40eff5e097)\
  2017-08-11 18:21:53 +0200
  * cleanup: include/restart\_mysqld.inc
* [Revision #1b993721ff](https://github.com/MariaDB/server/commit/1b993721ff)\
  2017-08-11 16:24:01 +0200
  * [MDEV-13472](https://jira.mariadb.org/browse/MDEV-13472) rpl.rpl\_semi\_sync\_wait\_point crashes because of thd\_destructor\_proxy
* [Revision #023131e395](https://github.com/MariaDB/server/commit/023131e395)\
  2017-08-11 16:22:40 +0200
  * InnoDB: restore thd->proc\_info in innobase\_reset\_background\_thd()
* [Revision #dd67456af3](https://github.com/MariaDB/server/commit/dd67456af3)\
  2017-08-11 16:18:16 +0200
  * InnoDB: disallow fast\_shutdown=0 when purge threads have exited
* [Revision #fc279d7ea2](https://github.com/MariaDB/server/commit/fc279d7ea2)\
  2017-08-11 18:36:51 +0200
  * InnoDB: test case to exploit a purge thread shutdown race condition
* [Revision #34319403a5](https://github.com/MariaDB/server/commit/34319403a5)\
  2017-08-11 16:17:08 +0200
  * fix a comment
* [Revision #3ec96c1824](https://github.com/MariaDB/server/commit/3ec96c1824)\
  2017-08-09 20:35:33 +0200
  * [MDEV-13370](https://jira.mariadb.org/browse/MDEV-13370) Ambiguous behaviour regarding installation of header files
* [Revision #c872b10022](https://github.com/MariaDB/server/commit/c872b10022)\
  2017-08-09 18:23:04 +0200
  * don't install same files twice
* [Revision #c9db190fed](https://github.com/MariaDB/server/commit/c9db190fed)\
  2017-07-10 15:06:41 +0200
  * cmake: update submodules automatically during the build
* [Revision #bfa9990e33](https://github.com/MariaDB/server/commit/bfa9990e33)\
  2017-08-02 15:11:35 +0200
  * cleanup: simplify the assignment
* [Revision #0188819229](https://github.com/MariaDB/server/commit/0188819229)\
  2017-08-14 17:22:18 +0000
  * [MDEV-13514](https://jira.mariadb.org/browse/MDEV-13514) fix compilation for aws\_key\_management plugin
* [Revision #cfa18cb5cf](https://github.com/MariaDB/server/commit/cfa18cb5cf)\
  2017-08-14 14:30:22 +0300
  * MyRocks: Fix merge typo in server stderr message
* [Revision #84008f26b3](https://github.com/MariaDB/server/commit/84008f26b3)\
  2017-08-11 15:25:37 +0000
  * [MDEV-12469](https://jira.mariadb.org/browse/MDEV-12469) : Update AWS SDK version to avoid gcc7 compile errors.
* [Revision #5a43c8bae7](https://github.com/MariaDB/server/commit/5a43c8bae7)\
  2017-08-11 16:42:27 +0300
  * [MDEV-13416](https://jira.mariadb.org/browse/MDEV-13416) mariadb-backup --backup fails to copy log if LSN is above 4294967295
* [Revision #79d2853354](https://github.com/MariaDB/server/commit/79d2853354)\
  2017-08-11 00:50:29 +0400
  * [MDEV-12604](https://jira.mariadb.org/browse/MDEV-12604) Comparison of JSON\_EXTRACT result differs with Mysql.
* [Revision #bfffe571ac](https://github.com/MariaDB/server/commit/bfffe571ac)\
  2017-08-10 14:00:51 +0300
  * Fix some GCC 7 warnings for InnoDB
* [Revision #cb2a57c203](https://github.com/MariaDB/server/commit/cb2a57c203)\
  2017-08-07 13:42:35 +0200
  * [MDEV-13439](https://jira.mariadb.org/browse/MDEV-13439): Database permissions are not enough to run a subquery with GROUP BY within a view
* Merge [Revision #bdab49d389](https://github.com/MariaDB/server/commit/bdab49d389) 2017-08-09 22:29:02 +0300 - [MDEV-13481](https://jira.mariadb.org/browse/MDEV-13481) Merge new release of InnoDB MySQL 5.7.19 to 10.2
* [Revision #38be0beb5d](https://github.com/MariaDB/server/commit/38be0beb5d)\
  2017-05-18 13:53:27 +0530
  * Bug #24961167 CONCURRENT INSERT FAILS IF TABLE DOES REBUILD
* [Revision #5721d5ba12](https://github.com/MariaDB/server/commit/5721d5ba12)\
  2017-05-08 10:28:58 +0530
  * Bug #24960450 CONCURRENT DELETE DOESN'T APPLY DURING TABLE REBUILD
* [Revision #ab2c31850d](https://github.com/MariaDB/server/commit/ab2c31850d)\
  2017-08-09 16:47:09 +0300
  * Import a test case from MySQL 5.7.19
* [Revision #f2eaac5d92](https://github.com/MariaDB/server/commit/f2eaac5d92)\
  2017-08-09 16:34:57 +0300
  * Remove dead references to clust\_templ\_for\_sec
* [Revision #9d57468dde](https://github.com/MariaDB/server/commit/9d57468dde)\
  2017-05-18 14:09:23 +0530
  * Bug #25357789 INNODB: LATCH ORDER VIOLATION DURING TRUNCATE TABLE IF INNODB\_SYNC\_DEBUG ENABLED
* [Revision #bf8054b0e8](https://github.com/MariaDB/server/commit/bf8054b0e8)\
  2017-03-24 12:18:52 +0530
  * BUG#25365223 ERRORLOG UPDATED WITH NOTES INFORMATION WHEN A REF FKEY ISN'T FOUND IN GRSETUP
* [Revision #88c391ad6d](https://github.com/MariaDB/server/commit/88c391ad6d)\
  2017-03-22 16:39:35 +0530
  * Bug #25573565 TABLE REBUILD USES EXCESSIVE MEMORY
* [Revision #a72f34c0a2](https://github.com/MariaDB/server/commit/a72f34c0a2)\
  2017-08-09 15:21:42 +0300
  * [MDEV-12868](https://jira.mariadb.org/browse/MDEV-12868) MySQL bug #84038 also affects [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)
* [Revision #067ee84d67](https://github.com/MariaDB/server/commit/067ee84d67)\
  2017-08-04 11:02:13 +0200
  * [MDEV-13300](https://jira.mariadb.org/browse/MDEV-13300) Query cache doesn't take in account CLIENT\_DEPRECATE\_EOF capability
* [Revision #86f9b77147](https://github.com/MariaDB/server/commit/86f9b77147)\
  2017-08-09 12:47:12 +0300
  * [MDEV-13037](https://jira.mariadb.org/browse/MDEV-13037): wsrep\_sst\_mysqldump checking wrong version of mysql client
* [Revision #6b14fd6d6d](https://github.com/MariaDB/server/commit/6b14fd6d6d)\
  2017-08-09 10:42:38 +0300
  * A followup to [MDEV-13470](https://jira.mariadb.org/browse/MDEV-13470): remove the code that is now useless
* [Revision #d0c66c87a7](https://github.com/MariaDB/server/commit/d0c66c87a7)\
  2017-08-09 09:53:24 +0300
  * Fix a random result mismatch of encryption.innodb\_encrypt\_log
* [Revision #c720e68f53](https://github.com/MariaDB/server/commit/c720e68f53)\
  2017-08-08 19:54:12 +0300
  * [MDEV-13472](https://jira.mariadb.org/browse/MDEV-13472) rpl.rpl\_semi\_sync\_wait\_point crashes because of thd\_destructor\_proxy
* [Revision #ffa3789495](https://github.com/MariaDB/server/commit/ffa3789495)\
  2017-08-08 15:34:41 +0300
  * Follow-up to [MDEV-11487](https://jira.mariadb.org/browse/MDEV-11487): Remove InnoDB internal temporary tables
* [Revision #c3f9fdeaf5](https://github.com/MariaDB/server/commit/c3f9fdeaf5)\
  2017-08-08 15:32:23 +0300
  * Add DBUG "trx" instrumentation that was used for catching [MDEV-13470](https://jira.mariadb.org/browse/MDEV-13470)
* [Revision #2152fbdc89](https://github.com/MariaDB/server/commit/2152fbdc89)\
  2017-08-08 15:25:48 +0300
  * [MDEV-13470](https://jira.mariadb.org/browse/MDEV-13470) DELETE IGNORE should not ignore deadlocks (again)
* [Revision #4bca34d8a4](https://github.com/MariaDB/server/commit/4bca34d8a4)\
  2017-08-08 15:40:11 +0400
  * [MDEV-12789](https://jira.mariadb.org/browse/MDEV-12789) JSON\_KEYS returns duplicate keys twice.
* [Revision #01a4eb8f76](https://github.com/MariaDB/server/commit/01a4eb8f76)\
  2017-08-08 13:49:29 +0400
  * [MDEV-12732](https://jira.mariadb.org/browse/MDEV-12732) json.json\_no\_table fails with valgrind in buildbot and outside.
* [Revision #bb71d9abf2](https://github.com/MariaDB/server/commit/bb71d9abf2)\
  2017-08-08 10:35:26 +0400
  * [MDEV-12604](https://jira.mariadb.org/browse/MDEV-12604) Comparison of JSON\_EXTRACT result differs with Mysql.
* [Revision #86e0a73eaa](https://github.com/MariaDB/server/commit/86e0a73eaa)\
  2017-08-07 23:38:27 +0300
  * Remove wait\_innodb\_all\_purged.inc
* [Revision #03f3bdce5f](https://github.com/MariaDB/server/commit/03f3bdce5f)\
  2017-08-07 23:14:56 +0300
  * Deterministically wait for purge using wait\_all\_purged.inc
* [Revision #6f623907cd](https://github.com/MariaDB/server/commit/6f623907cd)\
  2017-08-07 17:21:30 +0300
  * Backport [MDEV-13430](https://jira.mariadb.org/browse/MDEV-13430) recovery improvement to [MariaDB 10.2](../../old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102.md)
* [Revision #34eef269eb](https://github.com/MariaDB/server/commit/34eef269eb)\
  2017-08-04 13:57:26 +0300
  * [MDEV-11939](https://jira.mariadb.org/browse/MDEV-11939): innochecksum mistakes a file for an encrypted one (page 0 invalid)
* [Revision #36e81a23c5](https://github.com/MariaDB/server/commit/36e81a23c5)\
  2017-08-07 12:38:47 +0200
  * [MDEV-11937](https://jira.mariadb.org/browse/MDEV-11937): InnoDB flushes redo log too often
* [Revision #5ae598390a](https://github.com/MariaDB/server/commit/5ae598390a)\
  2017-08-07 18:12:24 +0300
  * Attempt to make rocksdb.rocksdb\_parts stable
* [Revision #30c36b2c15](https://github.com/MariaDB/server/commit/30c36b2c15)\
  2017-08-07 17:25:11 +0300
  * Make rocksdb.rocksdb\_icp test stable
* Merge [Revision #1fad491cff](https://github.com/MariaDB/server/commit/1fad491cff) 2017-08-07 16:13:17 +0300 - Merge branch '10.2' of github.com:MariaDB/server into 10.2
* [Revision #dcdc1c6d09](https://github.com/MariaDB/server/commit/dcdc1c6d09)\
  2017-08-07 13:54:37 +0300
  * [MDEV-13452](https://jira.mariadb.org/browse/MDEV-13452) Assertion \`!recv\_no\_log\_write' failed in log\_reserve\_and\_open()
* [Revision #a33220fbef](https://github.com/MariaDB/server/commit/a33220fbef)\
  2017-08-07 13:50:31 +0300
  * [MDEV-13451](https://jira.mariadb.org/browse/MDEV-13451) Assertion \`!recv\_no\_ibuf\_operations' failed in ibuf\_page\_low()
* [Revision #f701ac65e9](https://github.com/MariaDB/server/commit/f701ac65e9)\
  2017-08-07 13:46:45 +0400
  * [MDEV-12324](https://jira.mariadb.org/browse/MDEV-12324) Wrong result (phantom array value) on JSON\_EXTRACT.
* [Revision #4ff6ebf76a](https://github.com/MariaDB/server/commit/4ff6ebf76a)\
  2017-08-07 12:49:04 +0400
  * [MDEV-12181](https://jira.mariadb.org/browse/MDEV-12181) ST\_AsGeoJSON argument does not limit decimals.
* [Revision #0b30ce4f31](https://github.com/MariaDB/server/commit/0b30ce4f31)\
  2017-08-07 16:04:38 +0300
  * [MDEV-13374](https://jira.mariadb.org/browse/MDEV-13374): Server crashes in first\_linear\_tab / st\_select\_lex::set\_explain\_type
* [Revision #c508691a93](https://github.com/MariaDB/server/commit/c508691a93)\
  2017-08-07 11:04:09 +1000
  * travis: add clang-5.0
* Merge [Revision #29ad628491](https://github.com/MariaDB/server/commit/29ad628491) 2017-08-06 23:58:05 +0300 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks
* [Revision #11948d7586](https://github.com/MariaDB/server/commit/11948d7586)\
  2017-08-06 16:27:37 +0400
  * [MDEV-12180](https://jira.mariadb.org/browse/MDEV-12180) ST\_GeomFromGeoJSON option argument appears to have no effect.
* Merge [Revision #24a25a2c11](https://github.com/MariaDB/server/commit/24a25a2c11) 2017-08-06 15:37:27 +0300 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks
* [Revision #6d51817d2c](https://github.com/MariaDB/server/commit/6d51817d2c)\
  2017-08-04 13:33:48 +0400
  * Support for server error messages in Hindi
* [Revision #bcc10a5a44](https://github.com/MariaDB/server/commit/bcc10a5a44)\
  2017-08-03 17:31:05 +0400
  * Support for server error messages in Hindi
* [Revision #7507000ce2](https://github.com/MariaDB/server/commit/7507000ce2)\
  2017-08-03 17:28:46 +0400
  * Support for server error messages in Hindi
* [Revision #bf256392e6](https://github.com/MariaDB/server/commit/bf256392e6)\
  2017-02-25 16:13:32 -0500
  * Support for server error messages in Hindi.
* [Revision #93a6eed607](https://github.com/MariaDB/server/commit/93a6eed607)\
  2017-08-06 15:36:50 +0300
  * Backport to 10.2: Make rocksdb.type\_varchar test stable
* [Revision #7925a4bce8](https://github.com/MariaDB/server/commit/7925a4bce8)\
  2017-08-05 13:57:17 +0000
  * More comments
* [Revision #eda033255a](https://github.com/MariaDB/server/commit/eda033255a)\
  2017-08-03 15:16:40 +0000
  * Make "SET @@rocksdb\_bulk\_load=0" return an error instead of crashing the server
* [Revision #fcb8d8e598](https://github.com/MariaDB/server/commit/fcb8d8e598)\
  2017-08-01 19:19:54 +0000
  * Make rocksdb.prefix\_extractor\_override work on Windows
* [Revision #0899724257](https://github.com/MariaDB/server/commit/0899724257)\
  2017-08-01 08:50:48 +0000
  * Use proper #include's
* [Revision #2963a49f72](https://github.com/MariaDB/server/commit/2963a49f72)\
  2017-08-01 08:50:25 +0000
  * Post-merge fix: Rdb\_io\_watchdog doesn't support windows
* [Revision #61ca3cf524](https://github.com/MariaDB/server/commit/61ca3cf524)\
  2017-07-31 17:34:47 +0000
  * Post-merge fix: Rdb\_io\_watchdog doesn't support windows
* [Revision #1388afcd84](https://github.com/MariaDB/server/commit/1388afcd84)\
  2017-07-31 13:44:15 +0000
  * [MDEV-13413](https://jira.mariadb.org/browse/MDEV-13413): After the merge rocksdb.drop\_table fails with warnings
* [Revision #6bf757a2a9](https://github.com/MariaDB/server/commit/6bf757a2a9)\
  2017-07-30 13:37:04 +0000
  * Disable rocksdb.issue243\_transactionStatus
* [Revision #4eec6d4cca](https://github.com/MariaDB/server/commit/4eec6d4cca)\
  2017-07-30 13:36:11 +0000
  * Update test result for rocksdb.tbl\_opt\_data\_index\_dir
* [Revision #da9c669210](https://github.com/MariaDB/server/commit/da9c669210)\
  2017-07-30 12:09:51 +0000
  * Fixes for a few more post-merge test failures
* [Revision #d74e43e7bc](https://github.com/MariaDB/server/commit/d74e43e7bc)\
  2017-07-30 11:12:54 +0000
  * Fix rocksdb.duplicate\_table test
* [Revision #894c797eaf](https://github.com/MariaDB/server/commit/894c797eaf)\
  2017-07-30 10:51:27 +0000
  * Mark all tests that are derived from rocksdb.bulk\_load as "big".
* [Revision #1e6b02e688](https://github.com/MariaDB/server/commit/1e6b02e688)\
  2017-07-30 10:42:39 +0000
  * [MDEV-13404](https://jira.mariadb.org/browse/MDEV-13404): MyRocks upstream uses I\_S.table\_statistics.row\_lock\_deadlocks
* [Revision #c90753e671](https://github.com/MariaDB/server/commit/c90753e671)\
  2017-07-30 09:03:42 +0000
  * Follow the upstream MyRocks: provide details in the ER\_LOCK\_DEADLOCK message
* [Revision #123187dfed](https://github.com/MariaDB/server/commit/123187dfed)\
  2017-07-29 18:06:46 +0000
  * Fix the merge of rocksdb\_sys\_vars test suite
* Merge [Revision #ff0ae68eae](https://github.com/MariaDB/server/commit/ff0ae68eae) 2017-07-29 17:05:38 +0000 - Merge branch 'bb-10.2-mariarocks' of github.com:MariaDB/server into bb-10.2-mariarocks
* [Revision #b2617cae3f](https://github.com/MariaDB/server/commit/b2617cae3f)\
  2017-07-29 17:24:10 +0300
  * Post-merge fix: fix compilation
* [Revision #d083c2490a](https://github.com/MariaDB/server/commit/d083c2490a)\
  2017-07-29 17:05:14 +0000
  * Make rocksdb.bloomfilter\_skip pass.
* [Revision #a95ace491b](https://github.com/MariaDB/server/commit/a95ace491b)\
  2017-07-29 15:26:55 +0000
  * Test result updates: don't hardcode error numbers in the tests.
* [Revision #be6c4f5d15](https://github.com/MariaDB/server/commit/be6c4f5d15)\
  2017-07-29 13:24:55 +0000
  * More post-merge updates to get the tests pass
* [Revision #a89d01fb60](https://github.com/MariaDB/server/commit/a89d01fb60)\
  2017-07-29 11:06:22 +0000
  * Trivial updates to get a few rocksdb.\* testcases to pass
* Merge [Revision #f2952485a1](https://github.com/MariaDB/server/commit/f2952485a1) 2017-07-29 10:06:09 +0000 - Merge MyRocks merge tree into bb-10.2-mariarocks, unfinished.
* [Revision #43d5edf97c](https://github.com/MariaDB/server/commit/43d5edf97c)\
  2017-07-28 17:52:07 +0000
  * Copy of commit 394d0712d3d46a87a8063e14e998e9c22336e3a6 Author: Anca Agape [anca@fb.com](mailto:anca@fb.com) Date: Thu Jul 27 15:43:07 2017 -0700
* [Revision #488f46f3de](https://github.com/MariaDB/server/commit/488f46f3de)\
  2017-07-24 15:41:17 +0300
  * [MDEV-13153](https://jira.mariadb.org/browse/MDEV-13153): Assertion ... failed on partitioned RocksDB table
* [Revision #8c0129dc32](https://github.com/MariaDB/server/commit/8c0129dc32)\
  2017-07-28 12:30:30 +0400
  * [MDEV-13396](https://jira.mariadb.org/browse/MDEV-13396) Unexpected "alter routine comand defined" during CREATE OR REPLACE PROCEDURE
* [Revision #2a1035b004](https://github.com/MariaDB/server/commit/2a1035b004)\
  2017-07-21 20:09:19 +0300
  * [MDEV-13351](https://jira.mariadb.org/browse/MDEV-13351): Server crashes in st\_select\_lex::set\_explain\_type upon UNION with window function
* [Revision #e2afdb1ee4](https://github.com/MariaDB/server/commit/e2afdb1ee4)\
  2017-07-21 19:06:01 +0300
  * [MDEV-13344](https://jira.mariadb.org/browse/MDEV-13344): Server crashes in AGGR\_OP::put\_record on subquery
* [Revision #17fc288b30](https://github.com/MariaDB/server/commit/17fc288b30)\
  2017-07-21 13:53:58 +0300
  * [MDEV-13352](https://jira.mariadb.org/browse/MDEV-13352): Server crashes in st\_join\_table::remove\_duplicates
* [Revision #bc75c57cfc](https://github.com/MariaDB/server/commit/bc75c57cfc)\
  2017-07-18 00:01:48 +0600
  * update .gitignore
* [Revision #013595f56f](https://github.com/MariaDB/server/commit/013595f56f)\
  2017-07-17 17:04:18 +0000
  * [MDEV-13332](https://jira.mariadb.org/browse/MDEV-13332) mariadb-backup from 10.2.x crashes with --ftwrl-\* options
* [Revision #1b3cf18e4e](https://github.com/MariaDB/server/commit/1b3cf18e4e)\
  2017-07-15 19:35:06 +0200
  * CONNECT: accessed p\[i] outside of the loop
* [Revision #95dcfeded4](https://github.com/MariaDB/server/commit/95dcfeded4)\
  2017-07-13 19:19:43 +0200
  * deb packages didn't build
* Merge [Revision #b9aab7d9e3](https://github.com/MariaDB/server/commit/b9aab7d9e3) 2017-07-13 10:33:24 +0200 - Merge branch 'connect/10.2' into 10.2
* [Revision #a9d32010d0](https://github.com/MariaDB/server/commit/a9d32010d0)\
  2017-07-04 19:18:14 +0200
  * Fix [MDEV-13239](https://jira.mariadb.org/browse/MDEV-13239) Suppress the restriction about no blanks around , and = in the OPTION\_LIST
* Merge [Revision #7542aff665](https://github.com/MariaDB/server/commit/7542aff665) 2017-07-03 22:35:15 +0200 - Merge branch 'ob-10.2' of [MariaDB](https://github.com/Buggynours/MariaDB) into ob-10.2
* [Revision #0631cdab4b](https://github.com/MariaDB/server/commit/0631cdab4b)\
  2017-07-02 23:33:22 +0200
  * Define nullptr in jdbconn.cpp
* [Revision #b63f847743](https://github.com/MariaDB/server/commit/b63f847743)\
  2017-07-02 23:33:22 +0200
  * Suppress warning when creating mongo JSON tables
* [Revision #94e5d7de85](https://github.com/MariaDB/server/commit/94e5d7de85)\
  2017-07-02 22:29:31 +0200
  * Add Support of the MongoDB Java Driver
* [Revision #c51548d6b4](https://github.com/MariaDB/server/commit/c51548d6b4)\
  2017-06-11 17:22:56 +0200
  * Fix unhandled exception: Force type int for ENUMs. Replace remaining longjmp
* [Revision #f3452fcd84](https://github.com/MariaDB/server/commit/f3452fcd84)\
  2017-06-10 00:52:56 +0200
  * Add MONGO catalog table
* [Revision #da3c3b903f](https://github.com/MariaDB/server/commit/da3c3b903f)\
  2017-06-08 18:01:47 +0200
  * Fix [MDEV-12973](https://jira.mariadb.org/browse/MDEV-12973): Blank columns querying SQL Server Added support of NCHAR, NVARCHAR an ROWID JDBC types
* [Revision #5b534a6889](https://github.com/MariaDB/server/commit/5b534a6889)\
  2017-06-06 17:28:26 +0200
  * Fix [MDEV-12969](https://jira.mariadb.org/browse/MDEV-12969). Crash during inserting binary value in Connect table. Seems due to making an index on unsigned integer that triggers an un-handled THROW
* [Revision #c746b768ad](https://github.com/MariaDB/server/commit/c746b768ad)\
  2017-06-03 23:33:51 +0200
  * Tabname defaults to the table name for MONGO tables
* [Revision #aef1493224](https://github.com/MariaDB/server/commit/aef1493224)\
  2017-06-01 10:14:03 +0200
  * Protect Info function against NULL g pointer
* [Revision #de1a9b172a](https://github.com/MariaDB/server/commit/de1a9b172a)\
  2017-05-29 19:46:59 +0200
  * Add table option FILTER used by Mongo and Json tables
* [Revision #cbdfdfc829](https://github.com/MariaDB/server/commit/cbdfdfc829)\
  2017-05-28 12:43:54 +0200
  * Add CHECK TABLE to the list of accepted commands. This is to avoid an error to be reported when executing this command on a CONNECT table
* [Revision #f5dfd9f6cd](https://github.com/MariaDB/server/commit/f5dfd9f6cd)\
  2017-05-26 14:36:15 +0200
  * Use english error msg in xml.result
* [Revision #b72c4e50d6](https://github.com/MariaDB/server/commit/b72c4e50d6)\
  2017-05-26 14:29:04 +0200
  * Missing quote in infoschema2-9739.result
* [Revision #bffa06c7fa](https://github.com/MariaDB/server/commit/bffa06c7fa)\
  2017-05-26 11:31:36 +0200
  * Try to fix failing tests on LINUX
* [Revision #e58620cd63](https://github.com/MariaDB/server/commit/e58620cd63)\
  2017-05-25 23:51:57 +0200
  * Try to fix failing tests
* [Revision #7f02ab70b3](https://github.com/MariaDB/server/commit/7f02ab70b3)\
  2017-05-25 21:43:11 +0200
  * Recognize xmlsup option case insensitive
* [Revision #46cf1a0db3](https://github.com/MariaDB/server/commit/46cf1a0db3)\
  2017-05-23 23:02:48 +0200
  * Fix bug: Discovery of JSON table fails in DEBUG mode when NO MONGO support. (tdb->Uri is uninitialized)
* [Revision #3e36eb230b](https://github.com/MariaDB/server/commit/3e36eb230b)\
  2017-05-23 19:35:50 +0200
  * Fix gcc compiler warnings reported by Sergei
* [Revision #e8333389c8](https://github.com/MariaDB/server/commit/e8333389c8)\
  2017-05-18 12:57:24 +0200
  * .gitignore
* [Revision #a76c05bba0](https://github.com/MariaDB/server/commit/a76c05bba0)\
  2017-07-12 22:40:43 +0200
  * Require either OpenSSL 1.0 or 1.1 on Debian
* [Revision #7fc75c420a](https://github.com/MariaDB/server/commit/7fc75c420a)\
  2017-07-12 22:39:58 +0200
  * fix compilation with OpenSSL 1.1
* [Revision #1d730ac42d](https://github.com/MariaDB/server/commit/1d730ac42d)\
  2017-07-12 21:31:14 +0300
  * Rename mariadb-backup-10.2.files to mariadb-backup-10.2.install
* [Revision #9b4d281ecd](https://github.com/MariaDB/server/commit/9b4d281ecd)\
  2017-07-12 19:46:44 +0530
  * [MDEV-13826](https://jira.mariadb.org/browse/MDEV-13826): Floating point exception in Filesort\_tracker::print\_json\_members(Json\_writer\*)
* [Revision #52a5bfa078](https://github.com/MariaDB/server/commit/52a5bfa078)\
  2017-07-12 09:42:21 -0400
  * bump the VERSION
* [Revision #3904014ed3](https://github.com/MariaDB/server/commit/3904014ed3)\
  2017-07-11 18:09:38 +1000
  * [MDEV-13288](https://jira.mariadb.org/browse/MDEV-13288): Travis dependency cracklib-runtime

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
