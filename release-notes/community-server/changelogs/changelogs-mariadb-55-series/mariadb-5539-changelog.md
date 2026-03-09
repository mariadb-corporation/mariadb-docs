# MariaDB 5.5.39 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.39)[Release Notes](../../old-releases/5.5/5.5.39.md)[Changelog](mariadb-5539-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 5 Aug 2014

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.39.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4264](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4264)\
  Sun 2014-08-03 13:38:54 +0200
  * [MDEV-6507](https://jira.mariadb.org/browse/MDEV-6507) tokudb release builds compiled with debug code on
* [Revision #4263](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4263)\
  Sun 2014-08-03 12:45:14 +0200
  * Bug#17638477 UNINSTALL AND INSTALL SEMI-SYNC PLUGIN CAUSES SLAVES TO BREAK
* [Revision #4262](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4262)\
  Sun 2014-08-03 07:38:41 +0200
  * fix xtradb on windows (again)
* [Revision #4261](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4261) \[merge]\
  Sat 2014-08-02 21:26:16 +0200
  * mysql-5.5.39 merge
* [Revision #4260](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4260) \[merge]\
  Fri 2014-08-01 17:04:15 +0200
  * tokudb-7.1.7
  * [Revision #0.28.1650](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1650)\
    Fri 2014-06-13 14:43:36 -0400
    * \#252 fix the [MDEV-6324](https://jira.mariadb.org/browse/MDEV-6324) fix
  * [Revision #0.28.1649](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1649)\
    Fri 2014-06-13 12:06:05 -0400
    * \#250 reset thd proc info in end\_bulk\_insert to fix invalid proc info pointer inside of a deleted ha\_tokudb object
  * [Revision #0.28.1648](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1648)\
    Tue 2014-06-10 18:55:57 -0400
    * \#252 fix [MDEV-6324](https://jira.mariadb.org/browse/MDEV-6324) uninit var in discover3
  * [Revision #0.28.1647](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1647)\
    Wed 2014-06-04 10:44:15 -0400
    * \#250 restore proc info to valid pointers in commit, abort, analyze, and optimize
  * [Revision #0.28.1646](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1646)\
    Mon 2014-06-02 16:24:47 -0400
    * \#248 install PS+TokuDB tarballs
  * [Revision #0.28.1645](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1645)\
    Sun 2014-06-01 12:48:53 -0400
    * \#225 fix tokudb store lock to fix lock tables crash
  * [Revision #0.28.1644](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1644)\
    Sun 2014-06-01 07:49:28 -0400
    * \#225 hot optimize for 5.6 and 10.0 using alter recreate
  * [Revision #0.28.1643](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1643)\
    Sat 2014-05-31 12:16:56 -0400
    * \#245 use row estimate parameter to start\_bulk\_insert to decide if a loader is used
  * [Revision #0.28.1642](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1642)\
    Thu 2014-05-29 07:41:16 -0400
    * \#241 unique key check should avoid relocking keys if the table is already prelocked by the loader
  * [Revision #0.28.1641](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1641)\
    Sun 2014-05-25 08:44:04 -0400
    * TokuDB 7.1.6 is released
  * [Revision #0.28.1640](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1640)\
    Tue 2014-05-20 08:18:13 -0400
    * \#236 mysqld\_safe should use libjemalloc.so if it exists in the tarball
  * [Revision #0.28.1639](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1639)\
    Wed 2014-05-14 14:43:44 -0400
    * \#206 merge [mariadb 10.0.11](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-0-series/mariadb-10011-release-notes) changes
  * [Revision #0.28.1638](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1638)\
    Tue 2014-05-13 08:56:06 -0400
    * \#221 fix tokudb::estimate\_num\_rows
  * [Revision #0.28.1637](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1637)\
    Sat 2014-05-10 15:53:31 -0400
    * \#232 compile in jemalloc detector
  * [Revision #0.28.1636](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1636)\
    Thu 2014-05-08 17:39:29 -0400
    * \#231 change lock\_uniq\_key\_empty test to work without the bulk insert avoidance patch
  * [Revision #0.28.1635](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1635)\
    Thu 2014-05-08 15:03:10 -0400
    * \#230 disable the tokudb bulk loader in the tokudb locks schema tests
  * [Revision #0.28.1634](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1634)\
    Wed 2014-05-07 08:20:41 -0400
    * \#228 use thd\_get/set\_ha\_data for tokudb\_trx data
  * [Revision #0.28.1633](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1633)\
    Tue 2014-05-06 13:17:49 -0400
    * \#226 delete CMakeLists.in, no longer used
  * [Revision #0.34.5889](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5889) \[merge]\
    Wed 2014-06-04 15:42:20 -0400
    * Merge branch 'bugs/255'
    * [Revision #0.64.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.64.4)\
      Wed 2014-06-04 15:42:11 -0400
      * refs #255, have the fsync\_log minicron shutdown before we close the logger in env\_close
  * [Revision #0.34.5888](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5888)\
    Wed 2014-06-04 15:40:35 -0400
    * Revert "refs #255, have the fsync\_log minicron shutdown before we close the logger in env\_close"
  * [Revision #0.34.5887](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5887)\
    Wed 2014-06-04 15:34:08 -0400
    * refs #255, have the fsync\_log minicron shutdown before we close the logger in env\_close
  * [Revision #0.34.5886](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5886)\
    Fri 2014-05-30 12:58:28 -0400
    * \#229 make ftdump easier to use
  * [Revision #0.34.5885](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5885) \[merge]\
    Thu 2014-05-29 11:07:09 -0400
    * Merge branch 'stress-test-script-updates'
    * [Revision #0.64.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.64.3)\
      Thu 2014-05-29 11:06:45 -0400
      * added 7.1.6 data set to stress test runner
    * [Revision #0.64.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.64.2)\
      Thu 2014-05-29 11:06:33 -0400
      * added test\_stress\_with\_verify to stress test runner
  * [Revision #0.34.5884](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5884) \[merge]\
    Wed 2014-05-28 13:37:55 -0400
    * Merge pull request #251 from Tokutek/verify-promotion
    * [Revision #0.64.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.64.1)\
      Wed 2014-05-28 12:09:49 -0400
      * changed ft-verify to work with promotion #250
  * [Revision #0.34.5883](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5883)\
    Tue 2014-05-27 16:44:08 -0400
    * refs #226 Fix a benign (but nevertheless important) bug where nonleaf partial eviction would fail to move stale messages out of the fresh message tree before serializing them to memory.
  * [Revision #0.34.5882](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5882) \[merge]\
    Sun 2014-05-25 12:43:46 -0400
    * Merge pull request #180 from Tokutek/rightmost\_leaf
    * [Revision #0.63.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.63.1)\
      Sun 2014-05-25 12:42:52 -0400
      * fixes #158 Use promotion to record the blocknum of the rightmost non-root leaf node in each FT. When the FT detects a rightmost insertion pattern, it attempts to do inserts and unique checks directly into the rightmost leaf node, greatly optimizing sequential insert speed.
  * [Revision #0.34.5881](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5881)\
    Fri 2014-05-23 18:29:27 -0400
    * Revert "FT-242 Begin breaking up fttypes.h by moving many things to their"
  * [Revision #0.34.5880](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5880)\
    Fri 2014-05-23 18:29:24 -0400
    * Revert "TMX-1 Rename TokuKV to TokuFT"
  * [Revision #0.34.5879](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5879)\
    Fri 2014-05-23 18:29:09 -0400
    * Revert "TMX-242 Add cursor.h, which missed the last commit"
  * [Revision #0.34.5878](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5878)\
    Fri 2014-05-23 18:13:59 -0400
    * TMX-242 Add cursor.h, which missed the last commit
  * [Revision #0.34.5877](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5877)\
    Fri 2014-05-23 18:13:32 -0400
    * TMX-1 Rename TokuKV to TokuFT
  * [Revision #0.34.5876](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5876)\
    Fri 2014-05-23 18:10:29 -0400
    * FT-242 Begin breaking up fttypes.h by moving many things to their appropriate headers
  * [Revision #0.34.5875](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5875)\
    Fri 2014-05-23 14:25:54 -0400
    * fixed typo #226
  * [Revision #0.34.5874](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5874)\
    Fri 2014-05-23 14:02:53 -0400
    * vectorized loops in new deserialization code #226
  * [Revision #0.34.5873](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5873)\
    Fri 2014-05-23 10:56:18 -0400
    * \#247 fix loader->close fd leak when NOFILE limit exceeded
  * [Revision #0.34.5872](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5872)\
    Fri 2014-05-23 08:42:19 -0400
    * changed CHECKPOINT\_DURATION\[\_LAST] to UINT64 #249
  * [Revision #0.34.5871](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5871)\
    Thu 2014-05-22 18:57:56 -0400
    * fixes #226 When serializing a nonleaf node, include the offsets stored in each message tree. This removes a sort during deserialization, which can be expensive when there are many messages and I/O is fast. This change supports auto-upgrade from older versions.
  * [Revision #0.34.5870](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5870)\
    Thu 2014-05-22 18:57:56 -0400
    * fixes #248 Convert to a tree on omt clone if it must support marks
  * [Revision #0.34.5869](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5869)\
    Wed 2014-05-21 11:51:26 -0400
    * \#244 skip jemalloc build if it is not in the third party directory
  * [Revision #0.34.5868](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5868) \[merge]\
    Tue 2014-05-20 14:40:46 -0400
    * Merge pull request #245 from Tokutek/gcc-4.9-support
    * [Revision #0.62.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.62.2)\
      Tue 2014-05-20 14:39:56 -0400
      * moved/cleaned up gcc-ar/gcc-ranlib checking #245
    * [Revision #0.62.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.62.1)\
      Tue 2014-05-20 13:51:32 -0400
      * Support gcc 4.9 in cmake, fix uninitialized value warnings
  * [Revision #0.34.5867](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5867)\
    Mon 2014-05-19 10:48:17 -0400
    * \#242 fix loader creation bug that unlinks the wrong fractal tree files
  * [Revision #0.34.5866](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5866)\
    Thu 2014-05-15 10:00:41 -0400
    * \#239 fix dbremove crash when NOFILE limit is exceeded
  * [Revision #0.34.5865](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5865)\
    Thu 2014-05-15 08:33:30 -0400
    * \#240 make the toku thread pool handle transient thread creation errors
  * [Revision #0.34.5864](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5864)\
    Tue 2014-05-13 16:05:00 -0400
    * \#237 fix various bulk loader bugs related to nproc ulimit exceeded
* [Revision #4259](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4259) \[merge]\
  Fri 2014-08-01 16:51:12 +0200
  * 5.3 merge
  * [Revision #2502.567.236](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.236)\
    Fri 2014-08-01 12:04:55 +0200
    * fix func\_time.test to be independent from the system time zone
  * [Revision #2502.567.235](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.235)\
    Mon 2014-07-28 13:47:55 +0400
    * [MDEV-4511](https://jira.mariadb.org/browse/MDEV-4511) Assertion \`scale <= precision' fails on GROUP BY TIMEDIFF with incorrect types [MDEV-6302](https://jira.mariadb.org/browse/MDEV-6302) Wrong result set when using GROUP BY FROM\_UNIXTIME(...)+0 Fixed.
  * [Revision #2502.567.234](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.234)\
    Wed 2014-07-23 19:36:15 +0200
    * [MDEV-6290](https://jira.mariadb.org/browse/MDEV-6290) Crash in KILL HARD QUERY USER x@y when slave threads are running
* [Revision #4258](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4258)\
  Fri 2014-08-01 14:33:49 +0300
  * Add missing results file.
* [Revision #4257](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4257) \[merge]\
  Fri 2014-08-01 12:54:56 +0300
  * Merged percona-server-5.5.38-35.2.
  * [Revision #0.12.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.69)\
    Thu 2014-07-31 21:25:13 +0200
    * percona-server-5.5.38-35.2
* [Revision #4256](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4256)\
  Thu 2014-07-31 13:13:33 +0300
  * Fixed memory overflow
* [Revision #4255](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4255)\
  Thu 2014-07-31 10:11:10 +0300
  * [MDEV-6441](https://jira.mariadb.org/browse/MDEV-6441): memory leak
* [Revision #4254](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4254)\
  Wed 2014-07-30 13:27:52 +0300
  * Fix for [MDEV-6493](https://jira.mariadb.org/browse/MDEV-6493): Assertion \`table->file->stats.records > 0 || error' failure, or 'Invalid write' valgrind warnings, or crash on scenario with Aria table, view, LOCK TABLES
* [Revision #4253](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4253)\
  Wed 2014-07-30 10:05:01 +0300
  * Fixed some compiler warnings
* [Revision #4252](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4252)\
  Tue 2014-07-29 12:56:43 +0200
  * fix the test to pass on windows (lower\_case\_file\_system)
* [Revision #4251](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4251)\
  Tue 2014-07-29 12:05:58 +0200
  * [MDEV-5924](https://jira.mariadb.org/browse/MDEV-5924) MariaDB could crash after changing the query\_cache size with SET GLOBAL
* [Revision #4250](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4250)\
  Tue 2014-07-29 09:09:52 +0200
  * [MDEV-6497](https://jira.mariadb.org/browse/MDEV-6497) InnoDB deadlocks on UNINSTALL PLUGIN
* [Revision #4249](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4249)\
  Mon 2014-07-28 13:31:46 +0400
  * [MDEV-6378](https://jira.mariadb.org/browse/MDEV-6378) mtr engines iuds time tests fail
* [Revision #4248](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4248)\
  Mon 2014-07-28 12:47:14 +0400
  * [MDEV-5745](https://jira.mariadb.org/browse/MDEV-5745) analyze MySQL fix for bug#12368495
* [Revision #4247](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4247)\
  Mon 2014-07-28 09:42:52 +0200
  * disable the test for [MDEV-6351](https://jira.mariadb.org/browse/MDEV-6351) on embedded
* [Revision #4246](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4246)\
  Sun 2014-07-27 21:02:00 +0200
  * [MDEV-6082](https://jira.mariadb.org/browse/MDEV-6082) Assertion \`0' fails in TC\_LOG\_DUMMY::log\_and\_order on DML after installing TokuDB at runtime on server with disabled InnoDB
* [Revision #4245](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4245)\
  Sat 2014-07-26 23:08:38 +0200
  * [MDEV-6428](https://jira.mariadb.org/browse/MDEV-6428) \[PATCH] MariaDB start script doesn't realize failure of MariaDB startup
* [Revision #4244](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4244)\
  Sun 2014-07-27 08:44:45 +0300
  * Fix compiler error on sparc.
* [Revision #4243](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4243)\
  Sat 2014-07-26 21:14:21 +0300
  * Fix InnoDB: Assertion failure in thread 2868898624 in file buf0lru.c line 1000 InnoDB: Failing assertion: mutex\_own(\&buf\_pool->LRU\_list\_mutex)
* [Revision #4242](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4242)\
  Fri 2014-07-25 14:15:33 +0200
  * [MDEV-5706](https://jira.mariadb.org/browse/MDEV-5706) MariaDB does not build on hurd-i386
* [Revision #4241](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4241)\
  Thu 2014-07-24 09:51:51 +0200
  * fix remaining warnings in manpages (for debian lint ?)
* [Revision #4240](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4240)\
  Wed 2014-07-23 21:44:35 +0200
  * [MDEV-5958](https://jira.mariadb.org/browse/MDEV-5958) Inconsitent handling of invalid arguments for mysqld\_safe
* [Revision #4239](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4239)\
  Wed 2014-07-23 12:01:05 +0200
  * [MDEV-6409](https://jira.mariadb.org/browse/MDEV-6409) CREATE VIEW replication problem if error occurs in mysql\_register\_view
* [Revision #4238](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4238)\
  Fri 2014-07-25 09:34:05 +0300
  * Fix test failure caused by simulated compression failure on IBUF\_DUMMY table.
* [Revision #4237](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4237)\
  Thu 2014-07-24 14:35:09 +0300
  * Fix too agressive long semaphore wait output and add guard against introducing compression failures on insert buffer.
* [Revision #4236](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4236)\
  Wed 2014-07-23 22:48:31 +0400
  * [MDEV-6322](https://jira.mariadb.org/browse/MDEV-6322): The PARTITION engine can return wrong query results MySQL Bug#71095: Wrong results with PARTITION BY LIST COLUMNS() MySQL Bug#72803: Wrong "Impossible where" with LIST partitioning [MDEV-6240](https://jira.mariadb.org/browse/MDEV-6240): Wrong "Impossible where" with LIST partitioning - Backprot the fix from MySQL Bug#71095.
* [Revision #4235](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4235)\
  Wed 2014-07-23 19:53:29 +0400
  * [MDEV-6289](https://jira.mariadb.org/browse/MDEV-6289) : Unexpected results when querying information\_schema - When traversing JOIN\_TABs with first\_linear\_tab/next\_linear\_tab(), don't forget to enter the semi-join nest when it is the first table in the join order. Failure to do so could cause e.g. I\_S tables not to be filled.
* [Revision #4234](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4234) \[merge]\
  Wed 2014-07-23 14:59:23 +0400
  * Merge 5.3->5.5
  * [Revision #2502.567.233](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.233)\
    Wed 2014-07-23 13:38:48 +0400
    * [MDEV-5750](https://jira.mariadb.org/browse/MDEV-5750) Assertion \`ltime->year == 0' fails on a query with EXTRACT DAY\_MINUTE and TIME column Item\_func\_min\_max::get\_date() did not clear ltime->year when returning a TIME value.
* [Revision #4233](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4233)\
  Wed 2014-07-23 13:52:17 +0300
  * Fix compiler errors on product build.
* [Revision #4232](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4232)\
  Tue 2014-06-24 11:41:35 +0400
  * [MDEV-6313](https://jira.mariadb.org/browse/MDEV-6313) - mysqld --log-bin=no-such-dir/master crashes during server initialization
* [Revision #4231](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4231)\
  Tue 2014-06-17 13:03:26 +0400
  * [MDEV-6351](https://jira.mariadb.org/browse/MDEV-6351) - --plugin=force has no effect for built-in plugins
* [Revision #4230](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4230)\
  Wed 2014-07-23 09:04:59 +0300
  * [MDEV-5673](https://jira.mariadb.org/browse/MDEV-5673): Crash while parallel dropping multiple tables under heavy load
* [Revision #4229](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4229)\
  Tue 2014-07-22 22:08:06 +0300
  * [MDEV-5670](https://jira.mariadb.org/browse/MDEV-5670): Assertion failure in file buf0lru.c line 2355
* [Revision #4228](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4228)\
  Tue 2014-07-22 19:32:58 +0400
  * [MDEV-6434](https://jira.mariadb.org/browse/MDEV-6434): Wrong result (extra rows) with ORDER BY, multiple-column index, InnoDB - Part #2. Fix obvious problems in the previous patch.
* [Revision #4227](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4227)\
  Tue 2014-07-22 15:52:49 +0400
  * [MDEV-6434](https://jira.mariadb.org/browse/MDEV-6434): Wrong result (extra rows) with ORDER BY, multiple-column index, InnoDB - Filesort has an optmization where it reads only columns that are needed before the sorting is done. - When ref(\_or\_null) is picked by the join optimizer, it may remove parts of WHERE clause that are guaranteed to be true. - However, if we use quick select, we must put all of the range columns into the read set. Not doing so will may cause us to fail to detect the end of the range.
* [Revision #4226](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4226)\
  Tue 2014-07-15 12:37:34 +0300
  * Makes innodb/xtradb compilable in 5.5
* [Revision #4225](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4225)\
  Tue 2014-07-08 17:21:13 +0300
  * [MDEV-6348](https://jira.mariadb.org/browse/MDEV-6348): mariadb crash signal 11
* [Revision #4224](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4224)\
  Fri 2014-07-04 12:25:32 +0300
  * [MDEV-5621](https://jira.mariadb.org/browse/MDEV-5621): Server random crash on ALTER TABLE
* [Revision #4223](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4223)\
  Fri 2014-07-04 08:42:59 +0300
  * [MDEV-6191](https://jira.mariadb.org/browse/MDEV-6191): row\_search\_for\_mysql comment and code consistency about isolation level and gap locks
* [Revision #4222](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4222)\
  Fri 2014-07-04 08:16:45 +0300
  * [MDEV-6318](https://jira.mariadb.org/browse/MDEV-6318): MariaDB with XtraDB uses times more of IO events than with InnoDB plugin
* [Revision #4221](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4221)\
  Mon 2014-06-30 14:06:28 +0300
  * [MDEV-6225](https://jira.mariadb.org/browse/MDEV-6225): Idle replication slave keeps crashing.
* [Revision #4220](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4220)\
  Wed 2014-06-18 14:47:23 +0200
  * install new aria\* manpages
* [Revision #4219](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4219)\
  Tue 2014-06-17 14:10:13 +0200
  * [MDEV-6188](https://jira.mariadb.org/browse/MDEV-6188): master\_retry\_count (ignored if disconnect happens on SET master\_heartbeat\_period)
* [Revision #4218](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4218)\
  Tue 2014-06-17 09:44:19 +0200
  * [MDEV-6343](https://jira.mariadb.org/browse/MDEV-6343): Incorrect error handling in mysqldump
* [Revision #4217](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4217)\
  Mon 2014-06-16 22:11:54 +0200
  * [bugreport.cgi?bug=751805](https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=751805) typo fixed
* [Revision #4216](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4216)\
  Wed 2014-06-11 16:23:20 +0400
  * [MDEV-6329](https://jira.mariadb.org/browse/MDEV-6329) - Buffer overrun in find\_uniq\_filename
* [Revision #4215](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4215)\
  Tue 2014-06-10 19:53:27 +0400
  * Increased version number

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
