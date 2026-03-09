# MariaDB 5.5.34 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.34) |[Release Notes](../../old-releases/5.5/5.5.34.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 21 Nov 2013

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.34.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3976](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3976)\
  Mon 2013-11-18 15:48:01 +0400
  * [MDEV-5182](https://jira.mariadb.org/browse/MDEV-5182) - build of 10.0.4/r3863 fails @ 'cmake' with -DINSTALL\_SYSCONFDIR/-DDEFAULT\_SYSCONFDIR specified
* [Revision #3975](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3975) \[merge]\
  Wed 2013-11-20 09:20:48 +0100
  * merge
  * [Revision #3973.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3973.1.5) \[merge]\
    Tue 2013-11-19 15:43:22 +0100
    * Percona-Server-5.5.34-rel32.0 merge
    * [Revision #0.12.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.65)\
      Thu 2013-11-07 21:44:46 +0100
      * Percona-Server-5.5.34-rel32.0.tar.gz
  * [Revision #3973.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3973.1.4)\
    Tue 2013-11-19 15:35:57 +0100
    * .bzrignore
  * [Revision #3973.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3973.1.3) \[merge]\
    Tue 2013-11-19 15:35:31 +0100
    * merge with ft-engine and ft-index up to tag:tokudb-7.1.0
    * [Revision #0.34.5722](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5722)\
      Mon 2013-10-07 10:40:40 -0400
      * refs #82, fix CMakeLists.txt
    * [Revision #0.34.5721](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5721)\
      Mon 2013-10-07 10:35:05 -0400
      * refs #82, remove checkpoint\_1.cc for TokuDB 7.1.0, may bring it back fixed later. That is still open
    * [Revision #0.34.5720](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5720)\
      Mon 2013-10-07 10:17:03 -0400
      * refs #78 for minicrons with a period of longer than one second (checkpoints), change minicron to count the period from the beginning of the callback's execution and not the end. For checkpoints, this makes them reliably start every 60 seconds.
    * [Revision #0.34.5719](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5719)\
      Mon 2013-10-07 10:16:03 -0400
      * refs #84, remove some shared variables from logger
    * [Revision #0.34.5718](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5718)\
      Mon 2013-10-07 08:35:52 -0400
      * tokutek/ft-index#80 tokutek/ft-engine#94 impose an upper bound on loader memory reservations
    * [Revision #0.34.5717](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5717)\
      Fri 2013-10-04 16:49:53 -0400
      * tokutek/ft-index#76 add US Patent 8,489,638
    * [Revision #0.34.5716](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5716)\
      Fri 2013-10-04 11:34:49 -0400
      * refs #61, fix locking bug, add write list lock before reintegrating PAIRs into the cachetable on a open
    * [Revision #0.34.5715](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5715)\
      Thu 2013-10-03 16:35:03 -0400
      * refs #61, fix some tests, remove checkpoint\_callback.cc, as it is not an interesting test, still need t ofix checkpoint\_1.cc
    * [Revision #0.34.5714](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5714)\
      Wed 2013-10-02 12:01:14 -0400
      * closes #77, remove tabs from memory.cc
    * [Revision #0.34.5713](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5713)\
      Wed 2013-10-02 10:45:25 -0400
      * \#56 run lock escalation on a background thread
    * [Revision #0.34.5712](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5712)\
      Wed 2013-10-02 09:53:00 -0400
      * refs #61, - have closed cachefiles not immedietely free pairs, but set them to the side - leave freeing of pairs to the evictor and/or shutdown - should a cachefile be reopened before all pairs are freed, the pairs belonging to that cachefile are reintegrated into the cachetable
    * [Revision #0.34.5711](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5711)\
      Tue 2013-10-01 10:22:03 -0400
      * \#59 get test\_lock\_timeout\_callback to work with valgrind. change the type of a sync\_fetch\_and\_add from bool to int
    * [Revision #0.34.5710](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5710)\
      Thu 2013-09-26 11:33:47 -0400
      * This checkin was meant for a branch. Undoing
    * [Revision #0.34.5709](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5709)\
      Thu 2013-09-26 11:27:25 -0400
      * stuff
    * [Revision #0.34.5708](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5708)\
      Thu 2013-09-26 11:10:12 -0400
      * refs #61, remove test helper function toku\_cachefile\_flush, fix tests that use it to not need it
    * [Revision #0.34.5707](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5707)\
      Wed 2013-09-25 18:10:57 -0400
      * refs #61, fix optimized compilation that has TOKU\_DEBUG\_PARANOID off
    * [Revision #0.34.5706](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5706)\
      Wed 2013-09-25 17:49:05 -0400
      * refs #61, several code simplifications: - break up cachetable\_flush\_cachefile into more digestable functions, - decouple hash\_id from filenum - break up close\_userdata into close\_userdata and free\_userdata
    * [Revision #0.34.5705](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5705)\
      Wed 2013-09-25 15:23:03 -0400
      * refs #61, clean up code relating to cachefiles, expand the cachefiles\_list class and move some functionality in there.
    * [Revision #0.34.5704](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5704)\
      Wed 2013-09-25 11:07:30 -0400
      * refs #46, LOTS of refactoring done. Isolate mempool and OMT into a new class, bndata. Remove key from the leafentry.
    * [Revision #0.34.5703](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5703)\
      Thu 2013-09-19 17:21:29 -0400
      * \#56 benchmark that demos lock escalation stalls
    * [Revision #0.34.5702](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5702) \[merge]\
      Thu 2013-09-19 09:20:43 -0400
      * Merge branch 'master' of github.com:Tokutek/ft-index
      * [Revision #0.46.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.46.2)\
        Wed 2013-09-18 14:52:43 -0400
        * \#69 add long tail counts to global status
      * [Revision #0.46.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.46.1)\
        Wed 2013-09-18 13:29:05 -0400
        * \#69 measure long tail lock tree and cache table stalls
    * [Revision #0.34.5701](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5701)\
      Wed 2013-09-18 13:41:00 -0400
      * fixes #71 fix a test bug by caching the txnid instead of trying to use a txn object after it commits or aborts
    * [Revision #0.34.5700](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5700) \[merge]\
      Wed 2013-09-18 09:51:10 -0400
      * Merge branch 'master' of github.com:Tokutek/ft-index
      * [Revision #0.45.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.45.2) \[merge]\
        Wed 2013-09-18 09:49:43 -0400
        * Merge branch 'master' of github.com:Tokutek/ft-index
      * [Revision #0.45.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.45.1) \[merge]\
        Wed 2013-09-18 09:48:03 -0400
        * Merge branch 'bugs/70'
        * [Revision #0.44.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.44.3)\
          Wed 2013-09-18 09:47:18 -0400
          * Fix this test - did not get built or tested properly on my end due to BUILD\_TESTING=Off in the cmake config.
    * [Revision #0.34.5699](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5699)\
      Wed 2013-09-18 09:51:02 -0400
      * \#50 add long tail counts to global status
    * [Revision #0.34.5698](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5698)\
      Wed 2013-09-18 08:48:39 -0400
      * \#50 add long tail counts to global status
    * [Revision #0.34.5697](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5697) \[merge]\
      Wed 2013-09-18 00:19:25 -0400
      * Merge branch 'bugs/70'
      * [Revision #0.44.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.44.2)\
        Wed 2013-09-18 00:18:57 -0400
        * refs #70 Add a test to the range buffer that verifies the buf grows properly after a small append into a large append
    * [Revision #0.34.5696](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5696) \[merge]\
      Tue 2013-09-17 23:55:54 -0400
      * Merge branch 'bugs/70'
      * [Revision #0.44.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.44.1)\
        Tue 2013-09-17 23:55:37 -0400
        * fixed memory allocation error in range\_buffer #70
    * [Revision #0.34.5695](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5695)\
      Tue 2013-09-17 11:40:17 -0400
      * refs #59 turn off bdb builds for tokudb lock tree tests
    * [Revision #0.34.5694](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5694)\
      Tue 2013-09-17 11:39:26 -0400
      * refs #64 fix cpp guard
    * [Revision #0.34.5693](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5693)\
      Tue 2013-09-17 11:30:40 -0400
      * refs #64 fix clang on linux problems
    * [Revision #0.34.5692](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5692)\
      Sat 2013-09-14 10:48:35 -0400
      * Increase the lock timeout and sleep time to make this test less timing-dependent (though it still is)
    * [Revision #0.34.5691](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5691)\
      Fri 2013-09-13 11:10:49 -0400
      * refs #59 Add the locktree visualization APIs, new accessors in the DB and DB\_TXN, and a new operation in test\_stress0 for stress testing coverage
    * [Revision #0.34.5690](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5690)\
      Thu 2013-09-12 14:41:44 -0400
      * remove -u option from cp, fixes #66
    * [Revision #0.34.5689](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5689)\
      Thu 2013-09-12 09:00:47 -0400
      * fixed required cmake version #65
    * [Revision #0.34.5688](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5688)\
      Sun 2013-09-08 11:32:48 -0400
      * refs #62 fix how tdb\_logprint formats XID pairs
    * [Revision #0.34.5687](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5687)\
      Wed 2013-08-21 16:10:43 -0400
      * \#50 count lock tree timeouts
    * [Revision #0.34.5686](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5686)\
      Wed 2013-08-21 15:29:30 -0400
      * refs #36, have the FIFO realloc its buffer on resize, as opposed to malloc and memcpy
    * [Revision #0.34.5685](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5685)\
      Wed 2013-08-21 15:10:05 -0400
      * refs #54, improve the performance of hot indexing. This change does two things:
        * gets indexer to run in reverse, that is, start at the end and run to beginning
        * refines locking a bit. An estimate of the position of the hot indexer is stored, that is cheap to look at. Threads that use this estimate with a mutex either do only a quick comparison or set it to a new value. Threads doing writes (with XXX\_multiple calls) will check their position with respect to the estimate, and if they see the hot indexer is already past where they will modify, they don't grab the more expensive indexer lock. For insertion workloads that go to the end of the main dictionary of a table/collection, this check should practically always pass.
    * [Revision #0.34.5684](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5684)\
      Tue 2013-08-20 13:36:45 -0400
      * \#50 count long tail events like long fsyncs, checkpoints, and lock tree waits
    * [Revision #0.34.5683](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5683)\
      Tue 2013-08-20 11:31:13 -0400
      * fixes #55, fix test
    * [Revision #0.34.5682](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5682) \[merge]\
      Mon 2013-08-19 14:56:51 -0400
      * Merge branch 'bdb-compile-fix' of github.com:Tokutek/ft-index into bdb-compile-fix
      * [Revision #0.43.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.43.2)\
        Mon 2013-08-19 14:54:42 -0400
        * \#31 remove more tokudb only tests
      * [Revision #0.43.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.43.1)\
        Mon 2013-08-19 10:16:49 -0400
        * guarded new DBT\_ARRAY api functions with #ifdef USE\_TDB #31
    * [Revision #0.34.5681](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5681)\
      Mon 2013-08-19 14:56:27 -0400
      * \#31 remove more tokudb only tests
    * [Revision #0.34.5680](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5680)\
      Mon 2013-08-19 14:56:27 -0400
      * guarded new DBT\_ARRAY api functions with #ifdef USE\_TDB #31
    * [Revision #0.34.5679](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5679)\
      Mon 2013-08-19 14:06:37 -0400
      * refs #48, remove unnecessary paranoid\_invariant
    * [Revision #0.34.5678](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5678)\
      Sun 2013-08-18 11:13:46 -0400
      * refs #48, have ft\_flush\_some\_child still do a flush if the child is a leaf node, so garbage collection happens
    * [Revision #0.34.5677](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5677) \[merge]\
      Tue 2013-08-13 15:02:04 -0400
      * Merge branch 'bugs/mongo-399'
      * [Revision #0.39.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.39.3)\
        Tue 2013-08-13 15:01:27 -0400
        * refs Tokutek/mongo#399, change hot\_optimize to take bounds
    * [Revision #0.34.5676](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5676)\
      Mon 2013-08-12 14:20:59 -0700
      * Refs Tokutek/ft-index#26 Fixes Tokutek/ft-index#31 Change api for \*\_multiple to support array indexing. Never call put/del\_callback functions for src\_db.
    * [Revision #0.34.5675](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5675)\
      Thu 2013-08-08 14:31:54 -0700
      * Fixes Tokutek/ft-index#44 Fix loop counter/array bounds in test\_stress0
    * [Revision #0.34.5674](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.34.5674)\
      Mon 2013-08-05 09:48:54 -0400
      * allow tokftdump to work on old tokudb files
    * [Revision #0.28.1489](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1489)\
      Mon 2013-10-07 18:50:26 -0400
      * tokutek/ft-engine#122 set loose tokudb variables for mtr
    * [Revision #0.28.1488](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1488)\
      Mon 2013-10-07 10:41:13 -0400
      * tokutek/ft-engine#122 force all mysql tests to set a new tokudb session variable to hide the default compression
    * [Revision #0.28.1487](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1487)\
      Mon 2013-10-07 10:35:09 -0400
      * \#122 fix tests that need to show default row format
    * [Revision #0.28.1486](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1486)\
      Mon 2013-10-07 09:11:51 -0400
      * \#122 change default compression to zlib and add a session variable to control create info row format
    * [Revision #0.28.1485](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1485) \[merge]\
      Mon 2013-10-07 08:38:50 -0400
      * tokutek/ft-engine#94 tokutek/ft-index#80 configure an upper bound on loader memory reservations Merge branch 'loadermem80'
      * [Revision #0.42.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.42.1)\
        Thu 2013-10-03 13:56:57 -0400
        * tokutek/ft-index#80 tokutek/ft-engine#94 add tokudb\_loader\_memory\_size system variable that controls the size of each loader memory size
    * [Revision #0.28.1484](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1484)\
      Fri 2013-10-04 16:44:43 -0400
      * tokutek/ft-index#76 add US Patent 8,489,638
    * [Revision #0.28.1483](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1483)\
      Fri 2013-10-04 16:05:34 -0400
      * \#121 change default basement node size to 64KB from 128KB
    * [Revision #0.28.1482](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1482)\
      Fri 2013-10-04 11:45:05 -0400
      * \#90 fix race conditions in tests that cause sporadic test failures
    * [Revision #0.28.1481](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1481)\
      Thu 2013-10-03 16:53:46 -0400
      * \#90 test lock timeout
    * [Revision #0.28.1480](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1480)\
      Thu 2013-10-03 16:53:03 -0400
      * \#90 add a test scenario where the 2nd txn succeeds
    * [Revision #0.28.1479](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1479)\
      Thu 2013-10-03 16:06:45 -0400
      * Checking in mtr test & result files for lock visualization tree
    * [Revision #0.28.1478](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1478)\
      Wed 2013-10-02 12:14:14 -0400
      * \#90 set tokudb\_last\_lock\_timeout to a string parsable by the python json module
    * [Revision #0.28.1477](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1477)\
      Wed 2013-10-02 11:11:27 -0400
      * \#90 prefix info schema tests with i\_s\_
    * [Revision #0.28.1476](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1476)\
      Mon 2013-09-30 16:33:15 -0400
      * \#90 fix the is\_tokudb\_locks test result file to match the schema
    * [Revision #0.28.1475](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1475)\
      Mon 2013-09-30 13:18:07 -0400
      * tokutek/ft-engine#111 tokutek/ft-index#74 merge the tokumx error message for transparent huge pages into tokudb
    * [Revision #0.28.1474](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1474)\
      Mon 2013-09-30 11:08:53 -0400
      * \#80 default compress tokudb bulk loader temp files
    * [Revision #0.28.1473](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1473)\
      Fri 2013-09-27 13:43:43 -0400
      * \#86 tokudb lock tree info schema
    * [Revision #0.28.1472](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1472)\
      Fri 2013-09-27 13:14:23 -0400
      * remove cruft
    * [Revision #0.28.1471](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1471)\
      Fri 2013-09-27 09:43:39 -0400
      * \#104 default capture lock timeout conflict info into tokudb\_last\_lock\_timeout variable
    * [Revision #0.28.1470](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1470)\
      Thu 2013-09-26 17:16:41 -0400
      * \#90 tokudb info schema tests
    * [Revision #0.28.1469](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1469)\
      Thu 2013-09-26 12:05:54 -0400
      * \#92 add compiler and cmake checks from mariadb
    * [Revision #0.28.1468](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1468)\
      Thu 2013-09-26 09:53:50 -0400
      * \#104 write frm for existing tables before the txn is committed
    * [Revision #0.28.1467](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1467)\
      Tue 2013-09-24 14:27:27 -0400
      * \#92 use parent txn in ::delete\_or\_rename\_table. this removes error messages when running dict\_leak\_3518 test
    * [Revision #0.28.1466](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1466)\
      Tue 2013-09-24 10:26:27 -0400
      * \#97 use ${ZLIB\_LIBRARY}
    * [Revision #0.28.1465](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1465)\
      Mon 2013-09-23 16:13:40 -0400
      * \#99 reduce analyze time to 5 seconds (from 60 seconds). this will probably allow > 1M rows to be in the cardinality computation
    * [Revision #0.28.1464](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1464)\
      Mon 2013-09-23 14:32:48 -0400
      * \#92 add key\_is\_clustering accessor
    * [Revision #0.28.1463](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1463)\
      Mon 2013-09-23 13:45:07 -0400
      * \#92 remove memcpy\_fixed (no longer necessary)
    * [Revision #0.28.1462](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1462)\
      Mon 2013-09-23 13:42:48 -0400
      * \#92 simplify my\_free calls
    * [Revision #0.28.1461](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1461)\
      Fri 2013-09-20 11:22:39 -0400
      * refs #94, for keys with strings, add a memcmp at the end of the comparison function if we are doing comparisons in the fractal tree, so that case-insensitivities get resolved. Comparisons done inside the handlerton are unaffected.
    * [Revision #0.28.1460](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1460)\
      Fri 2013-09-20 09:53:15 -0400
      * \#81 cleanup thread variables a bit
    * [Revision #0.28.1459](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1459)\
      Thu 2013-09-19 17:38:47 -0400
      * \#81 fix tokudb\_file\_map test result file
    * [Revision #0.28.1458](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1458)\
      Thu 2013-09-19 14:24:13 -0400
      * \#81 denormalize dname in tokudb\_file\_map
    * [Revision #0.28.1457](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1457)\
      Thu 2013-09-19 13:34:55 -0400
      * \#81 cleanup thread variables
    * [Revision #0.28.1456](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1456)\
      Wed 2013-09-18 14:53:15 -0400
      * Tokutek/ft-index#69 fix global status result file
    * [Revision #0.28.1455](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1455)\
      Tue 2013-09-17 14:43:35 -0400
      * change tokudb\_fsync\_time units
    * [Revision #0.28.1454](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1454) \[merge]\
      Tue 2013-09-17 13:03:08 -0400
      * Merge branch 'lto' of github.com:Tokutek/ft-engine into lto
      * [Revision #0.40.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.40.2) \[merge]\
        Fri 2013-08-30 08:58:17 -0400
        * Merge branch 'lto' of github.com:Tokutek/ft-engine into lto
        * [Revision #0.41.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.41.1)\
          Tue 2013-08-27 14:09:56 -0400
          * added -flto -fuse-linker-plugin to RelWithDebInfo #77
      * [Revision #0.40.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.40.1)\
        Fri 2013-08-30 08:58:06 -0400
        * added -flto -fuse-linker-plugin to RelWithDebInfo #77
    * [Revision #0.28.1453](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1453)\
      Tue 2013-09-17 13:02:58 -0400
      * added -flto -fuse-linker-plugin to RelWithDebInfo #77
    * [Revision #0.28.1452](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1452)\
      Tue 2013-09-17 08:04:02 -0400
      * refs #82 delete the user data information schemas
    * [Revision #0.28.1451](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1451)\
      Tue 2013-09-17 07:43:22 -0400
      * refs #83 cond compile gdb on error feature
    * [Revision #0.28.1450](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1450)\
      Sun 2013-09-15 09:58:19 -0400
      * refs #71 basic lock tree visualization
    * [Revision #0.28.1449](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1449)\
      Tue 2013-09-10 06:22:25 -0400
      * refs #71 rearrange IS code
    * [Revision #0.28.1448](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1448)\
      Mon 2013-09-09 07:04:45 -0400
      * refs Tokutek/ft-engine#30 trace all txn begin calls
    * [Revision #0.28.1447](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1447)\
      Sun 2013-09-01 19:04:36 -0400
      * update README to 7.0.4
    * [Revision #0.28.1446](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1446)\
      Thu 2013-08-29 17:21:29 -0400
      * Tokutek/mysql56#26 fix crash on alter table of partitioned tokudb table
    * [Revision #0.28.1445](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1445)\
      Thu 2013-08-29 17:08:52 -0400
      * refs #26 fix inplace\_alter\_table for tokudb partitions
    * [Revision #0.28.1444](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1444)\
      Thu 2013-08-29 12:03:41 -0400
      * Tokutek/mariadb#10 Tokutek/ft-engine#79 set the tokudb\_version variable
    * [Revision #0.28.1443](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1443)\
      Wed 2013-08-28 10:35:17 -0400
      * tokutek/mysql56#24 always set default storage engine to tokudb in the cardinality tests
    * [Revision #0.28.1442](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1442)\
      Tue 2013-08-27 17:19:08 -0400
      * rebase to mysql 5.6.13
    * [Revision #0.28.1441](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1441)\
      Mon 2013-08-26 15:54:34 -0400
      * start port to mysql 5.6.13
    * [Revision #0.28.1440](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1440)\
      Sun 2013-08-25 12:38:49 -0400
      * Tokutek/mysql56#2 get tokudb storage engine to build on mysql 5.6
    * [Revision #0.28.1439](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1439)\
      Wed 2013-08-21 10:15:47 -0400
      * \#69 run create unique index with MDL shared no write (not hot WRT writes)
    * [Revision #0.28.1438](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1438)\
      Mon 2013-08-19 07:56:21 -0400
      * \#68 simplify tokustat output
    * [Revision #0.28.1437](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1437)\
      Sat 2013-08-17 18:23:48 -0400
      * closes #66, have may\_table\_be\_empty call use the same transaction that opens and possibly creates the table, otherwise it may block behind that transaction's lock tree locks
    * [Revision #0.28.1436](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1436)\
      Thu 2013-08-15 14:28:34 -0400
      * \#64 get hot text and blob column expansion working
    * [Revision #0.28.1435](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1435)\
      Tue 2013-08-13 15:04:13 -0400
      * refs Tokutek/mongo#399, make handlerton fix for TokuDB
    * [Revision #0.28.1434](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1434)\
      Mon 2013-08-12 17:11:45 -0400
      * refs Tokutek/ft-index/#26 have ha\_tokudb use new XXX\_multiple API
    * [Revision #0.28.1433](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1433)\
      Mon 2013-08-05 10:07:47 -0400
      * \#58 #62 ignore key block size settings for tokudb. use session variables instead.
    * [Revision #0.28.1432](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.28.1432)\
      Fri 2013-08-02 09:31:24 -0700
      * Refs Tokutek/ft-index#40 Add test for transactional case insensitive tables
  * [Revision #3973.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3973.1.2) \[merge]\
    Tue 2013-11-19 13:16:25 +0100
    * mysql-5.5.34 merge (some patches reverted, test case added)
    * [Revision #3077.190.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.53)\
      Mon 2013-09-09 19:49:44 +0200
      * Reverted the changes to spec file, updated the logic to get the correct count of PID files
    * [Revision #3077.190.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.52)\
      Mon 2013-09-09 20:21:02 +0530
      * Bug #16776528 RACE CONDITION CAN CAUSE MYSQLD TO REMOVE SOCKET FILE ERRANTLY
    * [Revision #3077.190.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.51)\
      Fri 2013-08-30 15:02:16 +0200
      * Fix to ignore mysqld\_safe.pid
    * [Revision #3077.190.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.50)\
      Fri 2013-08-30 06:33:02 +0200
      * Corrected the PID\_FILE\_PATT manipulation
    * [Revision #3077.190.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.49)\
      Thu 2013-08-29 14:33:28 +0200
      * Fix for Bug#17377159, ignore mysqld\_safe.pid file created by mysqld\_safe script
    * [Revision #3077.190.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.48) \[merge]\
      Tue 2013-08-27 00:15:43 +0200
      * Empty version change upmerge
      * [Revision #2661.848.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.64)\
        Tue 2013-08-27 00:02:22 +0200
        * Raise version number after cloning 5.1.72
    * [Revision #3077.190.47](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.47)\
      Mon 2013-08-26 14:43:12 +0400
      * Fix for bug #17356954 "CANNOT USE SAVEPOINTS AFTER ER\_LOCK\_DEADLOCK OR ER\_LOCK\_WAIT\_TIMEOUT".
    * [Revision #3077.190.46](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.46)\
      Fri 2013-08-23 18:56:31 +0530
      * Bug#11765252 - READ OF FREED MEMORY WHEN "USE DB" AND "SHOW PROCESSLIST"
    * [Revision #3077.190.45](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.45)\
      Fri 2013-08-23 18:19:54 +0530
      * Correcting file ids of newly added files in bug#11765252
    * [Revision #3077.190.44](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.44)\
      Fri 2013-08-23 17:13:44 +0530
    * [Revision #3077.190.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.43) \[merge]\
      Fri 2013-08-23 16:56:17 +0530
      * Bug#17029399 - CRASH IN ITEM\_REF::FIX\_FIELDS WITH TRIGGER ERRORS
      * [Revision #2661.848.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.63)\
        Fri 2013-08-23 16:54:25 +0530
        * Bug#17029399 - CRASH IN ITEM\_REF::FIX\_FIELDS WITH TRIGGER ERRORS
    * [Revision #3077.190.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.42)\
      Fri 2013-08-23 14:13:30 +0530
    * [Revision #3077.190.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.41)\
      Fri 2013-08-23 10:56:05 +0530
    * [Revision #3077.190.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.40) \[merge]\
      Fri 2013-08-23 09:07:09 +0530
      * [WL#7076](https://askmonty.org/worklog/?tid=7076): Backporting wl6715 to support both formats in 5.5, 5.6, 5.7.
      * [Revision #3077.192.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.192.1)\
        Tue 2013-07-02 11:58:39 +0530
        * [WL#7076](https://askmonty.org/worklog/?tid=7076): Backporting wl6715 to support both formats in 5.5, 5.6, 5.7
    * [Revision #3077.190.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.39)\
      Thu 2013-08-22 16:51:30 +0200
      * Corrected Date in the changelog
    * [Revision #3077.190.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.38)\
      Thu 2013-08-22 14:58:13 +0200
      * Removed bugnumber from the changelog and updated description
    * [Revision #3077.190.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.37)\
      Wed 2013-08-21 15:24:38 +0530
      * Bug#16995954 : PLUGIN\_AUTH TESTS FAIL ON SYSTEMS WITH NO HOSTNAME OTHER THAN LOCALHOST
    * [Revision #3077.190.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.36) \[merge]\
      Wed 2013-08-21 11:55:22 +0300
      * (Null) merge from mysql-5.1 to mysql-5.5.
      * [Revision #2661.848.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.62) \[merge]\
        Wed 2013-08-21 11:54:09 +0300
        * Merge working copy to mysql-5.1.
    * [Revision #3077.190.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.35) \[merge]\
      Wed 2013-08-21 10:04:48 +0300
      * (Null) merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.853.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.853.2) \[merge]\
        Wed 2013-08-21 10:03:31 +0300
        * Merge mysql-5.1 to working copy.
    * [Revision #3077.190.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.34) \[merge]\
      Wed 2013-08-21 08:48:04 +0300
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.853.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.853.1)\
        Wed 2013-08-21 08:22:05 +0300
        * Bug#12560151 61132: infinite loop in buf\_page\_get\_gen() when handling compressed pages
    * [Revision #3077.190.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.33) \[merge]\
      Wed 2013-08-21 10:44:22 +0530
      * Bug#11765252 - READ OF FREED MEMORY WHEN "USE DB" AND "SHOW PROCESSLIST"
      * [Revision #2661.848.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.61)\
        Wed 2013-08-21 10:39:40 +0530
        * Bug#11765252 - READ OF FREED MEMORY WHEN "USE DB" AND "SHOW PROCESSLIST"
    * [Revision #3077.190.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.32)\
      Tue 2013-08-20 12:21:35 +0200
      * Reverted Release version
    * [Revision #3077.190.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.31) \[merge]\
      Tue 2013-08-20 12:06:04 +0200
      * Upmerge of the Bug17211588 build
      * [Revision #3077.188.80](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.80)\
        Fri 2013-08-16 17:48:54 +0200
        * dummy commit
      * [Revision #3077.188.79](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.188.79)\
        Fri 2013-08-16 16:41:20 +0200
        * Added fix Provides for Bug#17211588
    * [Revision #3077.190.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.30)\
      Tue 2013-08-20 13:12:34 +0400
      * Fix for bug#14188793
        * "DEADLOCK CAUSED BY ALTER TABLE DOEN'T CLEAR STATUS OF ROLLBACKED TRANSACTION" and bug #17054007
        * "TRANSACTION IS NOT FULLY ROLLED BACK IN CASE OF INNODB DEADLOCK".
    * [Revision #3077.190.29](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.29)\
      Mon 2013-08-19 21:51:59 +0530
    * [Revision #3077.190.28](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.28) \[merge]\
      Fri 2013-08-16 15:49:13 +0300
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.848.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.60)\
        Fri 2013-08-16 15:45:41 +0300
        * Bug#17312846 CHECK TABLE ASSERTION FAILURE DICT\_TABLE\_GET\_FORMAT(CLUST\_INDEX->TABLE) >= 1
    * [Revision #3077.190.27](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.27) \[merge]\
      Thu 2013-08-15 15:34:12 +0300
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.848.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.59)\
        Thu 2013-08-15 15:23:23 +0300
        * Bug#17302896 DOUBLE PURGE ON ROLLBACK OF UPDATING A DELETE-MARKED RECORD
    * [Revision #3077.190.26](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.26) \[merge]\
      Wed 2013-08-14 10:24:36 +0300
      * Merge mysql-5.1 to mysql-5.5.
      * [Revision #2661.848.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.58)\
        Wed 2013-08-14 09:43:21 +0300
        * Bug#16971045 ASSERTION FAILURES ON ROLLBACK OF AN INSERT AFTER A FAILED BLOB WRITE
    * [Revision #3077.190.25](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.25) \[merge]\
      Mon 2013-08-12 23:06:58 +0530
      * Bug #16776528 RACE CONDITION CAN CAUSE MYSQLD TO REMOVE SOCKET FILE ERRANTLY Problem Description: A mysqld\_safe instance is started. An InnoDB crash recovery begins which takes few seconds to complete. During this crash recovery process happening, another mysqld\_safe instance is started with the same server startup parameters. Since the mysqld's pid file is absent during the crash recovery process the second instance assumes there is no other process and tries to acquire a lock on the ibdata files in the datadir. But this step fails and the 2nd instance keeps retrying 100 times each with a delay of 1 second. Now after the 100 attempts, the server goes down, but while going down it hits the mysqld\_safe script's cleanup section and without any check it blindly deletes the socket and pid files. Since no lock is placed on the socket file, it gets deleted.
      * [Revision #2661.848.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.57)\
        Mon 2013-08-12 21:54:50 +0530
        * Bug #16776528 RACE CONDITION CAN CAUSE MYSQLD TO REMOVE SOCKET FILE ERRANTLY Problem Description: A mysqld\_safe instance is started. An InnoDB crash recovery begins which takes few seconds to complete. During this crash recovery process happening, another mysqld\_safe instance is started with the same server startup parameters. Since the mysqld's pid file is absent during the crash recovery process the second instance assumes there is no other process and tries to acquire a lock on the ibdata files in the datadir. But this step fails and the 2nd instance keeps retrying 100 times each with a delay of 1 second. Now after the 100 attempts, the server goes down, but while going down it hits the mysqld\_safe script's cleanup section and without any check it blindly deletes the socket and pid files. Since no lock is placed on the socket file, it gets deleted.
    * [Revision #3077.190.24](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.24)\
      Mon 2013-08-12 11:09:33 +0200
      * Bug#16860588:CRASH WITH CREATE TABLE ... LIKE .. AND PARTITION VALUES IN (NULL)
    * [Revision #3077.190.23](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.23)\
      Mon 2013-08-12 10:52:08 +0200
      * Bug#17228383: VALGRIND WARNING IN IBUF\_DELETE\_REC
    * [Revision #3077.190.22](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.22) \[merge]\
      Mon 2013-08-12 19:46:44 +0530
      * Bug#16614004 - CRASH AFTER READING FREED MEMORY AFTER DOING DDL IN STORED ROUTINE
      * [Revision #3077.191.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.191.1)\
        Wed 2013-07-24 14:33:52 +0200
        * Fix for Bug#16614004 CRASH AFTER READING FREED MEMORY AFTER DOING DDL IN STORED ROUTINE Inside a loop in a stored procedure, we create a partitioned table. The CREATE statement is thus treated as a prepared statement: it is prepared once, and then executed by each iteration. Thus its Lex is reused many times. This Lex contains a part\_info member, which describes how the partitions should be laid out, including the partitioning function. Each execution of the CREATE does this, in open\_table\_from\_share ():
    * [Revision #3077.190.21](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.21)\
      Thu 2013-08-08 14:28:20 +0530
    * [Revision #3077.190.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.20)\
      Wed 2013-08-07 15:08:55 +0530
    * [Revision #3077.190.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.19)\
      Wed 2013-08-07 07:56:07 +0530
      * Bug#16416302 - CRASH WITH LOSSY RBR REPLICATION OF OLD STYLE DECIMALS
    * [Revision #3077.190.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.18) \[merge]\
      Wed 2013-07-31 23:01:01 +0200
      * Merge from mysql-5.5.33-release
    * [Revision #3077.190.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.17) \[merge]\
      Wed 2013-07-31 17:59:06 +0100
      * Bug#16997513 MY\_STRTOLL10 ACCEPTING OVERFLOWED UNSIGNED LONG LONG VALUES AS NORMAL ONES
      * [Revision #2661.848.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.56)\
        Wed 2013-07-31 17:54:40 +0100
        * Bug#16997513 MY\_STRTOLL10 ACCEPTING OVERFLOWED UNSIGNED LONG LONG VALUES AS NORMAL ONES
    * [Revision #3077.190.16](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.16) \[merge]\
      Tue 2013-07-30 09:51:14 +0530
      * Bug#17083851 BACKPORT BUG#11765744 TO 5.1, 5.5 AND 5.6
      * [Revision #2661.848.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.55)\
        Tue 2013-07-30 09:44:11 +0530
        * Bug#17083851 BACKPORT BUG#11765744 TO 5.1, 5.5 AND 5.6
    * [Revision #3077.190.15](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.15) \[merge]\
      Mon 2013-07-29 14:46:16 +0530
      * Bug#13417564 SKIP SLEEP IN SRV\_MASTER\_THREAD WHEN SHUTDOWN IS IN PROGRESS
      * [Revision #2661.848.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.54)\
        Mon 2013-07-29 14:45:06 +0530
        * Bug#13417564 SKIP SLEEP IN SRV\_MASTER\_THREAD WHEN SHUTDOWN IS IN PROGRESS
    * [Revision #3077.190.14](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.14)\
      Mon 2013-07-29 11:41:13 +0530
      * Bug #11766851 QUERYING I\_S.PARTITIONS CHANGES THE CARDINALITY OF THE PARTITIONS.
    * [Revision #3077.190.13](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.13)\
      Sat 2013-07-27 17:35:02 +0530
      * BUG#16290902 DROP TEMP TABLE IF EXISTS CAN CAUSE POINT IN TIME RECOVERY FAILURE ON SLAVES
    * [Revision #3077.190.12](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.12) \[merge]\
      Thu 2013-07-25 15:31:06 +0530
      * Merge from mysql-5.1 to mysql-5.5
      * [Revision #2661.848.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.53)\
        Thu 2013-07-25 14:53:23 +0530
        * Bug #17076737 DUPLICATE CONSTRAINTS DISPLAYED WHEN NAME INCLUDES "_IBFK_"
    * [Revision #3077.190.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.11)\
      Wed 2013-07-24 15:44:41 +0530
      * Bug#16865959 - PLEASE BACKPORT BUG 14749800.
    * [Revision #3077.190.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.10) \[merge]\
      Tue 2013-07-23 18:18:19 +0530
      * BUG#12535301- SYS\_VARS.RPL\_INIT\_SLAVE\_FUNC MISMATCHES IN DAILY-5.5
      * [Revision #2661.848.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.52)\
        Tue 2013-07-23 18:13:43 +0530
        * BUG#16295518 - SYS\_VARS.RPL\_INIT\_SLAVE\_FUNC IS FAILING ON MYSQL-5.1
        * BUG#12535301 - SYS\_VARS.RPL\_INIT\_SLAVE\_FUNC MISMATCHES IN DAILY-5.5
    * [Revision #3077.190.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.9)\
      Tue 2013-07-23 12:15:57 +0530
    * [Revision #3077.190.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.8)\
      Tue 2013-07-23 12:03:00 +0530
    * [Revision #3077.190.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.7)\
      Tue 2013-07-23 11:59:38 +0530
    * [Revision #3077.190.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.6) \[merge]\
      Thu 2013-07-18 11:44:00 +0530
      * BUG#15844882: MYSQLDUMP FROM 5.5 FAILS WITH AN ERROR WHEN TRYING TO DUMP DATA FROM MYSQL-5.6
      * [Revision #2661.848.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.51)\
        Thu 2013-07-18 11:40:08 +0530
        * BUG#15844882: MYSQLDUMP FROM 5.5 FAILS WITH AN ERROR WHEN TRYING TO DUMP DATA FROM MYSQL-5.6
    * [Revision #3077.190.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.5) \[merge]\
      Wed 2013-07-17 14:25:09 +0530
      * upmerge bug 17035577 5.1 => 5.5
      * [Revision #2661.848.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.50)\
        Wed 2013-07-17 14:24:02 +0530
        * Bug #17035577 - MTR V1 FAILS TO START SERVER MTR\_VERSION=1 PERL MYSQL-TEST-RUN.PL 1ST
    * [Revision #3077.190.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.4)\
      Wed 2013-07-10 14:00:30 +0800
      * Fix Bug #16710923 - FALSE REPORTS OF DB\_FOREIGN\_EXCEED\_MAX\_CASCADE
    * [Revision #3077.190.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.3)\
      Wed 2013-07-10 10:49:17 +0530
      * Bug #14017206 WITH CONSISTENT SNAPSHOT DOES NOT WORK WITH ISOLATION LEVEL SERIALIZABLE
    * [Revision #3077.190.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.2) \[merge]\
      Tue 2013-07-09 13:46:14 +0200
      * Empty version change upmerge
      * [Revision #2661.848.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2661.848.49)\
        Tue 2013-07-09 13:19:53 +0200
        * Raise version number after cloning 5.1.71
    * [Revision #3077.190.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.190.1)\
      Mon 2013-07-08 19:41:40 +0200
      * Raise version number after cloning 5.5.33
  * [Revision #3973.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3973.1.1)\
    Tue 2013-11-19 13:11:42 +0100
    * [MDEV-5236](https://jira.mariadb.org/browse/MDEV-5236) Status variables are not all listed alphabetically
* [Revision #3974](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3974)\
  Tue 2013-11-19 13:47:35 +0400
  * [MDEV-5069](https://jira.mariadb.org/browse/MDEV-5069): Server crashes in SEL\_ARG::increment\_use\_count with index\_merge+index\_merge\_sort\_union, FORCE INDEX - Don't call incr\_refs() is the merged SEL\_ARG\* is NULL.
* [Revision #3973](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3973)\
  Fri 2013-11-15 15:24:42 +0200
  * Added test case for new system variable innodb\_use\_stacktrace and made sure that it can be used only on startup. Fixed compiler problems on solaris and other platforms that do not contain necessary headers and functions.
* [Revision #3972](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3972)\
  Fri 2013-11-15 11:32:02 +0200
  * [MDEV-5247](https://jira.mariadb.org/browse/MDEV-5247): DB locked up at btr0cur.c line 568. Additional fixes to inconsistent usage of have\_LRU\_mutex and added additional debug assertions to guard incorrect usage of this mutex. Fixes issues found on additional testing and mysql test suite.
* [Revision #3971](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3971) \[merge]\
  Fri 2013-11-15 10:06:23 +0100
  * 5.3 merge
  * [Revision #2502.567.167](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.167)\
    Thu 2013-11-14 13:25:05 -0800
    * Fixed bug [MDEV-5288](https://jira.mariadb.org/browse/MDEV-5288). This bug was a consequence of the incorrect fix for bug [MDEV-5091](https://jira.mariadb.org/browse/MDEV-5091).
* [Revision #3970](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3970)\
  Thu 2013-11-14 14:43:24 +0200
  * Add new configuration variable
* [Revision #3969](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3969)\
  Thu 2013-11-14 14:27:46 +0200
  * Fix compiler error introduced on revision 3937, make sure that stackdump is compiled only on linux.
* [Revision #3968](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3968) \[merge]\
  Thu 2013-11-14 16:26:37 +0400
  * Merge 5.3->5.5
  * [Revision #2502.567.166](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.166) \[merge]\
    Thu 2013-11-14 16:14:09 +0400
    * Merge 5.2->5.3
    * [Revision #2502.566.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.58) \[merge]\
      Thu 2013-11-14 16:11:43 +0400
      * Merge 5.1->5.2
      * [Revision #2502.565.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.58)\
        Thu 2013-11-14 16:09:32 +0400
        * [MDEV-5290](https://jira.mariadb.org/browse/MDEV-5290) MTR cannot find mysql\_tzinfo\_to\_sql on Windows
  * [Revision #2502.567.165](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.165) \[merge]\
    Wed 2013-11-13 15:31:12 -0800
    * Merge
    * [Revision #2502.580.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.580.1)\
      Wed 2013-11-13 14:43:09 -0800
      * Fixed bug [MDEV-5091](https://jira.mariadb.org/browse/MDEV-5091). The function SELECT\_LEX::update\_used\_tables should process all ORDER BY lists in any subselect of a union.
* [Revision #3967](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3967)\
  Thu 2013-11-14 12:57:28 +0200
  * [MDEV-5247](https://jira.mariadb.org/browse/MDEV-5247): DB locked up at btr0cur.c line 568. There is inconsistent and non logical usage of have\_LRU\_mutex and incorrect value on ha\_innodb.cc when buf\_LRU\_free\_block is called. Additionally, for future long semaphore wait cases added a new configuration variable innodb\_use\_stacktrace. If this variable is true a signal handler for SIGUSR2 is installed when InnoDB server starts and when a long semaphore wait is detected at sync/sync0array.c we send SIGUSR2 signal to waiting thread and thread that has acuired RW-latch. For both threads a full stacktrace is produced as well as its is possible.
* [Revision #3966](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3966) \[merge]\
  Wed 2013-11-13 23:03:27 +0400
  * Fixes for storage\_engine tests on Windows
  * [Revision #3944.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3944.1.5)\
    Wed 2013-11-13 22:28:26 +0400
    * Workaround for the delayed InnoDB error messages in the log file
  * [Revision #3944.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3944.1.4)\
    Tue 2013-11-12 02:19:27 +0400
    * Windows-specific suppression and perl problems
  * [Revision #3944.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3944.1.3)\
    Mon 2013-11-11 23:40:40 +0400
    * Fixes for Windows and different time zones
* [Revision #3965](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3965) \[merge]\
  Wed 2013-11-13 19:16:35 +0400
  * Merge 5.3 -> 5.5
  * [Revision #2502.567.164](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.164) \[merge]\
    Wed 2013-11-13 18:34:12 +0400
    * Merge 5.2 -> 5.3
    * [Revision #2502.566.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.57) \[merge]\
      Wed 2013-11-13 18:28:40 +0400
      * Merge 5.1 -> 5.2
      * [Revision #2502.565.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.57)\
        Wed 2013-11-13 18:26:03 +0400
        * [MDEV-5226](https://jira.mariadb.org/browse/MDEV-5226) mysql\_tzinfo\_to\_sql errors with tzdata 2013f and above Allow only one level of symlink recursion in mysql\_tzdata\_to\_sql, to avoid infinite loops.
  * [Revision #2502.567.163](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.163)\
    Wed 2013-11-13 15:22:57 +0200
    * incorrect assertion removed
* [Revision #3964](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3964) \[merge]\
  Wed 2013-11-13 13:38:37 +0100
  * 5.3 merge
  * [Revision #2502.567.162](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.162)\
    Wed 2013-11-13 12:43:39 +0100
    * [MDEV-5284](https://jira.mariadb.org/browse/MDEV-5284) Assertion \`!(\*expr)->fixed' fails in replace\_where\_subcondition with IN suquery
  * [Revision #2502.567.161](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.161)\
    Tue 2013-11-12 15:02:25 +0100
    * [MDEV-5113](https://jira.mariadb.org/browse/MDEV-5113) Wrong result (extra row) and valgrind warnings in Item\_maxmin\_subselect::any\_value on 2nd execution of PS with SELECT subquery
* [Revision #3963](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3963) \[merge]\
  Wed 2013-11-13 08:29:12 +0400
  * Merge
  * [Revision #3943.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3943.1.1)\
    Tue 2013-11-12 17:37:32 +0400
    * [MDEV-5257](https://jira.mariadb.org/browse/MDEV-5257): MIN/MAX Optimization (Select tables optimized away) does not work for DateTime - MIN/MAX optimizer does a check whether a "field CMP const" comparison uses a constant that's longer than the field it is compared to. Make this check only for string columns, also compare character lengths, not byte lengths.
* [Revision #3962](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3962)\
  Wed 2013-11-13 07:40:46 +0400
  * [MDEV-5056](https://jira.mariadb.org/browse/MDEV-5056): Wrong result (extra rows) with materialization+semijoin, IN subqueries Apply fix suggested by Igor: - When eliminate\_item\_equal() generates pair-wise equalities from a multi-equality, do generate a "bridge" equality between the first field inside SJM nest and the field that's first in the overall multi-equality.
* [Revision #3961](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3961)\
  Mon 2013-11-11 22:53:40 +0100
  * [MDEV-4723](https://jira.mariadb.org/browse/MDEV-4723) "State" column of SHOW PROCESSLIST returns wrong values (non-ascii chars) for some states
* [Revision #3960](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3960)\
  Mon 2013-11-11 17:20:18 +0100
  * [MDEV-5236](https://jira.mariadb.org/browse/MDEV-5236) Status variables are not all listed alphabetically
* [Revision #3959](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3959)\
  Mon 2013-11-11 17:20:10 +0100
  * mark ft-index cmake variables as advanced
* [Revision #3958](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3958)\
  Mon 2013-11-11 16:17:32 +0100
  * [MDEV-4824](https://jira.mariadb.org/browse/MDEV-4824) userstats - wrong user statistics (and valgrind warnings)
* [Revision #3957](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3957)\
  Mon 2013-11-11 09:31:20 +0100
  * [MDEV-5116](https://jira.mariadb.org/browse/MDEV-5116) MariaDB upgrade breaks replication
* [Revision #3956](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3956)\
  Mon 2013-11-11 09:31:17 +0100
  * [MDEV-5101](https://jira.mariadb.org/browse/MDEV-5101) INFORMATION\_SCHEMA.PROCESSLIST reports an incorrect value for Time for connecting threads
* [Revision #3955](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3955)\
  Mon 2013-11-11 09:31:13 +0100
  * [MDEV-5186](https://jira.mariadb.org/browse/MDEV-5186) /usr/bin/mysqld\_safe doesn't have NUMA options support
* [Revision #3954](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3954)\
  Mon 2013-11-11 09:31:09 +0100
  * [MDEV-5022](https://jira.mariadb.org/browse/MDEV-5022) Strange message or wrong errno on mismatching versions of plugin and server
* [Revision #3953](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3953)\
  Mon 2013-11-11 09:31:05 +0100
  * [MDEV-5030](https://jira.mariadb.org/browse/MDEV-5030) RPM installation not running mysql\_install\_db if datadir exists
* [Revision #3952](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3952)\
  Mon 2013-11-11 09:31:02 +0100
  * [MDEV-5054](https://jira.mariadb.org/browse/MDEV-5054) Failing test(s): main.mysqld--help sys\_vars.character\_sets\_dir\_basic
* [Revision #3951](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3951)\
  Mon 2013-11-11 09:30:58 +0100
  * [MDEV-4977](https://jira.mariadb.org/browse/MDEV-4977) ./mysql-test/mysql-test-run.pl not identifying mariadb version
* [Revision #3950](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3950)\
  Mon 2013-11-11 09:30:48 +0100
  * [MDEV-5124](https://jira.mariadb.org/browse/MDEV-5124) cmake failure when fullhostname is not resolved
* [Revision #3949](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3949)\
  Mon 2013-11-11 09:30:35 +0100
  * [MDEV-5038](https://jira.mariadb.org/browse/MDEV-5038) put tokudb into the server package
* [Revision #3948](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3948)\
  Thu 2013-11-07 13:22:27 +0100
  * [MDEV-5250](https://jira.mariadb.org/browse/MDEV-5250) doesn't install on fedora if mysql is installed
* [Revision #3947](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3947)\
  Thu 2013-11-07 13:22:19 +0100
  * increase the version
* [Revision #3946](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3946) \[merge]\
  Mon 2013-11-11 20:38:04 +0200
  * merge 5.3->5.5
  * [Revision #2502.567.160](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.160)\
    Mon 2013-11-11 17:28:14 +0200
    * [MDEV-5153](https://jira.mariadb.org/browse/MDEV-5153): Server crashes in Item\_ref::fix\_fields on 2nd execution of PS with LEFT JOIN and MERGE view or SELECT SQ
  * [Revision #2502.567.159](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.159)\
    Mon 2013-11-11 16:40:46 +0200
    * [MDEV-5103](https://jira.mariadb.org/browse/MDEV-5103): server crashed on singular Item\_equal
* [Revision #3945](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3945) \[merge]\
  Mon 2013-11-11 00:15:42 +0400
  * [MDEV-5272](https://jira.mariadb.org/browse/MDEV-5272) MTR/mysqltest overlays for included files do not work on Windows
  * [Revision #3944.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3944.1.2)\
    Sun 2013-11-10 23:19:21 +0400
    * [MDEV-5272](https://jira.mariadb.org/browse/MDEV-5272) MTR/mysqltest overlays for included files do not work on Windows
  * [Revision #3944.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3944.1.1)\
    Sun 2013-11-10 14:37:32 +0400
    * Fix for overlayed include files on Windows and a test case
* [Revision #3944](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3944) \[merge]\
  Fri 2013-11-08 23:14:26 +0400
  * Merge 5.3 -> 5.5
  * [Revision #2502.567.158](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.158) \[merge]\
    Fri 2013-11-08 22:50:01 +0400
    * Merge 5.2 -> 5.3
    * [Revision #2502.566.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.56) \[merge]\
      Fri 2013-11-08 22:22:25 +0400
      * Merge 5.1 -> 5.2
      * [Revision #2502.565.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.56)\
        Fri 2013-11-08 22:19:24 +0400
        * [MDEV-5181](https://jira.mariadb.org/browse/MDEV-5181) incorrect binary search in remove\_status\_vars()
* [Revision #3943](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3943) \[merge]\
  Fri 2013-11-08 14:30:35 +0400
  * merge 5.3 -> 5.5
  * [Revision #2502.567.157](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.157)\
    Fri 2013-11-08 14:18:16 +0400
    * [MDEV-4842](https://jira.mariadb.org/browse/MDEV-4842) STR\_TO\_DATE does not work with UCS2/UTF16/UTF32
* [Revision #3942](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3942)\
  Wed 2013-11-06 22:53:39 +0400
  * [MDEV-5205](https://jira.mariadb.org/browse/MDEV-5205) - MariaDB does not start if more than 128 cpu's are available
* [Revision #3941](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3941)\
  Tue 2013-11-05 20:30:36 +0200
  * Added usage of handler error names to mysqltest
* [Revision #3940](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3940)\
  Tue 2013-11-05 20:28:24 +0200
  * Fixed core dump when doing "SET GLOBAL innodb\_buffer\_pool\_evict='uncompressed'"
* [Revision #3939](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3939)\
  Tue 2013-11-05 09:18:59 +0400
  * [MDEV-5205](https://jira.mariadb.org/browse/MDEV-5205) - MariaDB does not start if more than 128 cpu's are available
* [Revision #3938](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3938) \[merge]\
  Tue 2013-10-29 18:50:36 +0200
  * Merge 5.3->5.5
  * [Revision #2502.567.156](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.156)\
    Tue 2013-10-29 17:50:13 +0200
    * MariaDB made be compiled by gcc 4.8.1
  * [Revision #2502.567.155](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.155)\
    Tue 2013-10-29 12:39:03 +0200
    * [MDEV-5104](https://jira.mariadb.org/browse/MDEV-5104) crash in Item\_field::used\_tables with broken order by
  * [Revision #2502.567.154](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.154)\
    Mon 2013-10-21 13:45:49 +0300
    * [MDEV-5143](https://jira.mariadb.org/browse/MDEV-5143): update of a joined table with a nested subquery with a syntax error crashes mysqld with signal 11
* [Revision #3937](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3937)\
  Thu 2013-10-24 11:24:37 +0400
  * [MDEV-5102](https://jira.mariadb.org/browse/MDEV-5102) : MySQL Bug 69851
    * Backport MySQL's fix: do set ha\_partition::m\_pkey\_is\_clustered for ha\_partition objects created with handler->clone() call.
    * Also, include a testcase.
* [Revision #3936](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3936)\
  Wed 2013-10-23 15:22:47 +0300
  * [MDEV-5133](https://jira.mariadb.org/browse/MDEV-5133): Test suite tests \*\_func\_view fail in time zones East of UTC+3
* [Revision #3935](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3935)\
  Mon 2013-10-21 16:29:24 +0400
  * [MDEV-5127](https://jira.mariadb.org/browse/MDEV-5127) - Test suite test file\_contents fails in Slackware Linux
* [Revision #3934](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3934) \[merge]\
  Mon 2013-10-21 13:37:17 +0400
  * Merge 5.3 -> 5.5
  * [Revision #2502.567.153](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.153) \[merge]\
    Mon 2013-10-21 13:36:29 +0400
    * Merge 5.2 -> 5.3
    * [Revision #2502.566.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.55) \[merge]\
      Mon 2013-10-21 13:35:43 +0400
      * Merge 5.1 -> 5.2
      * [Revision #2502.565.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.55)\
        Mon 2013-10-21 13:34:18 +0400
        * A clean-up for DEV-4890 Valgrind warnings on shutdown on a build with openSSL
* [Revision #3933](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3933) \[merge]\
  Wed 2013-10-16 18:17:51 +0400
  * Merge 5.3->5.5
  * [Revision #2502.567.152](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.152) \[merge]\
    Wed 2013-10-16 18:13:13 +0400
    * Merge 5.2->5.3
    * [Revision #2502.566.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.54) \[merge]\
      Wed 2013-10-16 17:58:15 +0400
      * Merge 5.1->5.2
  * [Revision #2502.567.151](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.151) \[merge]\
    Wed 2013-10-16 17:48:31 +0400
    * Merge 5.1 -> 5.3
    * [Revision #2502.565.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.54)\
      Wed 2013-10-16 17:37:11 +0400
      * [MDEV-4890](https://jira.mariadb.org/browse/MDEV-4890) Valgrind warnings on shutdown on a build with openSSL
* [Revision #3932](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3932) \[merge]\
  Wed 2013-10-16 17:58:54 +0400
  * Merge 5.3 -> 5.5.
  * [Revision #2502.567.150](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.150)\
    Fri 2013-10-11 15:57:19 +0300
    * [MDEV-5107](https://jira.mariadb.org/browse/MDEV-5107):Left Join Yields All Nulls Instead of Appropriate Matches [MDEV-5034](https://jira.mariadb.org/browse/MDEV-5034):Wrong result on LEFT JOIN with a SELECT SQ or a merge view, UNION in IN subquery
* [Revision #3931](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3931)\
  Wed 2013-10-16 16:07:25 +0300
  * [MDEV-4981](https://jira.mariadb.org/browse/MDEV-4981): Account for queries handled by query-cache in USER\_STATISTICS (and in HOST\_STATISTICS)
* [Revision #3930](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3930)\
  Fri 2013-10-04 08:33:09 +0300
  * [MDEV-4981](https://jira.mariadb.org/browse/MDEV-4981): Account for queries handled by query-cache in USER\_STATISTICS (and in HOST\_STATISTICS)
* [Revision #3929](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3929) \[merge]\
  Mon 2013-10-14 12:30:20 -0700
  * Merge
  * [Revision #3927.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3927.1.1) \[merge]\
    Mon 2013-10-14 12:08:55 -0700
    * Merge 5.3->5.5
    * [Revision #2502.567.149](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.149)\
      Mon 2013-10-14 10:29:24 -0700
      * Fixed bug [MDEV-5135](https://jira.mariadb.org/browse/MDEV-5135). The patch for bug [MDEV-5105](https://jira.mariadb.org/browse/MDEV-5105) incorrectly counted conditions in nested joins.
* [Revision #3928](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3928)\
  Mon 2013-10-14 21:23:09 +0500
  * [MDEV-5131](https://jira.mariadb.org/browse/MDEV-5131) create\_embedded\_thd is not thread safe, libmysqld. The emb\_free\_embedded\_thd() has the thread-unsafe code so should be 'mutexed' also.
* [Revision #3927](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3927) \[merge]\
  Sun 2013-10-13 13:43:29 -0700
  * Merge 5.3-5.5
  * [Revision #2502.567.148](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.148)\
    Fri 2013-10-11 23:24:57 -0700
    * Fixed bug [MDEV-5132](https://jira.mariadb.org/browse/MDEV-5132). Objects of the classes Item\_func\_isnull and Item\_func\_isnotnull must have the flag sargable set to TRUE. Set the value of the flag sargable only in constructors of the classes inherited from Item\_int\_func.
  * [Revision #2502.567.147](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.147)\
    Fri 2013-10-11 12:50:30 -0700
    * Fixed a problem of the patch for [MDEV-5105](https://jira.mariadb.org/browse/MDEV-5105) that caused valgrind complains.
  * [Revision #2502.567.146](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.146)\
    Thu 2013-10-10 10:08:26 -0700
    * Fixed bug [MDEV-5105](https://jira.mariadb.org/browse/MDEV-5105). The bug caused a memory overwrite in the function update\_ref\_and\_keys() It happened due to a wrong value of SELECT\_LEX::cond\_count. This value historically was calculated by the fix\_fields method. Now the logic of calling this method became too complicated and, as a result, this value is calculated not always correctly. The patch changes the way how and when the values of SELECT\_LEX::cond\_count and of SELECT\_LEX::between\_count are calculated. The new code does it just at the beginning of update\_ref\_and\_keys().
  * [Revision #2502.567.145](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.145)\
    Fri 2013-10-04 09:51:07 -0700
    * Fixed bug [MDEV-5078](https://jira.mariadb.org/browse/MDEV-5078). For aggregated fields from views/derived tables the possible adjustment of thd->lex->in\_sum\_func->max\_arg\_level in the function Item\_field::fix\_fields must be done before we leave the function.
  * [Revision #2502.567.144](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.144)\
    Wed 2013-10-02 17:59:56 -0700
    * Fixed bug [MDEV-5028](https://jira.mariadb.org/browse/MDEV-5028). Apparently in a general case a short-cut for the distinct optimization is invalid if join buffers are used to join tables after the tables whose values are to selected.
* [Revision #3926](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3926)\
  Sun 2013-10-13 23:25:57 +0500
  * [MDEV-5131](https://jira.mariadb.org/browse/MDEV-5131) create\_embedded\_thd is not thread safe, libmysqld. LOCK\_thread\_count locked when we do threads.append().
* [Revision #3925](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3925)\
  Thu 2013-10-10 14:20:35 +0500
  * [MDEV-4788](https://jira.mariadb.org/browse/MDEV-4788) check mysql-5.5 changes in spatial.cc. Additional patch for the 5.5.
* [Revision #3924](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3924)\
  Wed 2013-10-09 17:30:50 +0500
  * [MDEV-3856](https://jira.mariadb.org/browse/MDEV-3856) Import of a large polygon fails/hangs. The Gis\_point::init\_from\_wkt called the String::realloc(), and this call is quite slow in the DEBUG mode. Which makes loading the huge polygon hang forever. Fixed by using the String::realloc(size, inc\_size) version instead as it's done for other spatial features.
* [Revision #3923](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3923)\
  Thu 2013-09-26 23:48:38 +0200
  * [MDEV-5076](https://jira.mariadb.org/browse/MDEV-5076) : Build on FreeBSD - when looking for execinfo library, and execinfo.h header, allow user-defined EXECINFO\_ROOT prefix, in case library and header are not placed under /usr/local . This change was requested by FreeBSD maintainer.
* [Revision #3922](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3922) \[merge]\
  Wed 2013-09-25 17:16:13 +0300
  * merge 5.3 -> 5.5
  * [Revision #2502.567.143](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.143)\
    Wed 2013-09-25 15:30:13 +0300
    * [MDEV-5039](https://jira.mariadb.org/browse/MDEV-5039): incorrect Item\_func\_regex::update\_used\_tables()
* [Revision #3921](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3921)\
  Tue 2013-09-24 19:52:51 +0200
  * [MDEV-5062](https://jira.mariadb.org/browse/MDEV-5062) : disable jemalloc by default everywhere, except Linux and OSX.
* [Revision #3920](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3920)\
  Mon 2013-09-23 23:33:18 +0200
  * [MDEV-5053](https://jira.mariadb.org/browse/MDEV-5053) - fix cyclic dependency when building with Ninja CMake generator
* [Revision #3919](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3919)\
  Mon 2013-09-23 20:17:46 +0300
  * Allow unique prefix for command line options, like any GNU program.
* [Revision #3918](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3918)\
  Mon 2013-09-23 20:17:03 +0300
  * TokuDB fixes:
    * Better error message when using huge pages
    * Fixed link error
    * Test suite should run even on system with huge pages
* [Revision #3917](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3917)\
  Tue 2013-09-17 18:51:14 +0400
  * [MDEV-4684](https://jira.mariadb.org/browse/MDEV-4684) - Enhancement request: `--init-command` support for mysqlslap
* [Revision #3916](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3916) \[merge]\
  Mon 2013-09-23 10:33:14 +0400
  * Merge fix for [MDEV-5037](https://jira.mariadb.org/browse/MDEV-5037) into 5.5
  * [Revision #3891.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3891.1.1)\
    Fri 2013-09-20 14:47:38 +0400
    * [MDEV-5037](https://jira.mariadb.org/browse/MDEV-5037): Server crash on a JOIN on a derived table with join\_cache\_level > 2
    * The crash was caused because the optimizer called handler->multi\_range\_read\_info() on a derived temporary table. That table has been created, but not opened yet. Because of that, handler::table was NULL, which caused crash. Fixed by changing DS-MRR methods to use handler::table\_share instead. handler::table\_share is set in handler ctor, so this should be safe.
* [Revision #3915](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3915)\
  Mon 2013-09-23 12:17:18 +0300
  * Tokudb made compilig.
* [Revision #3914](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3914)\
  Fri 2013-09-20 14:37:30 +0200
  * Update feedback plugin to recognize Windows 8.1 / Windows Server 2012 R2.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
