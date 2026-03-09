# MariaDB 5.1.55 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.1.55) | [Release Notes](../../old-releases/5.1/5.1.55.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 1 Mar 2011

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.55.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3041](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3041)
  * Disable variables-big with debug binaries.
  * When compiled with SAFEMALLOC or with Windows\
    Debug CRT, it allocates and initializes 5GB of memory.\
    The effect is 20 minutes of paging and swapping on\
    a 4GB VM.
  * Still allow the test to run with optimized binaries.\
    Memory is not initialized in this case, malloc()\
    of 5GB size will not bring the whole buffer into\
    physical memory.
* [Revision #3040](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3040)
  * Build fixes:
    * Fix signed/unsigned warning (error -Werror) in readline
    * change regex\_replace pattern to account for forward or backward slashes\
      in partition\_recover\_myisam ( fixes Windows/embedded)
* [Revision #3039](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3039)
  * Fix mtr errors with Windows/embedded/plugins.
  * Plugins do not work on Windows/embedded,\
    thus do not set plugin environment variables.
* [Revision #3038](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3038) \[merge]
  * Automatic merge with 5.1-merge to get in Merge with MySQL 5.1.55
    * [Revision #3034.1.10](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.10)
      * Fixed compiler warnings
    * [Revision #3034.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.9)
      * Fixed compiler and build error:
        * Fixed main.mysqlcheck error on windows
        * Fixed 'can't drop database pbxt' failure when running pbxt.mysqlslap
    * [Revision #3034.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.8)
      * maria/ma\_test\_all.sh can now be run with `--tmpdir=/dev/shm` for faster testing
      * Fixed mysql-test-run failures on window
      * Fixed compiler warnings from my last push (sorry about that)
      * Fixed that maria\_chk `--repair --extended` works again
      * Fixed compiler warnings about using not unitialized data
    * [Revision #3034.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.7)
      * Reduced memory requirements for mysqltest to 1/4.th This also gave a speedup for 5x for some tests.
      * Reduced memory usage from safe\_mutex.
      * Fixed problem with failing tests that could not restart mysqld becasue the port was reserved
      * More DBUG information
      * Fixed bug where bitmap\_set\_prefix() wrote over buffer area.
      * Initialize n\_pages\_flushed in xtradb which was used uninitialized.
    * [Revision #3034.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.6)
      * Fixed build failures
        * Removed references to deleted files
        * If we link staticly, check for static zlib
          * This should fix the problem with 'no -lz found' link error
        * Fixed build failure on window (Patch from Wlad)
        * Fixed build problem with federatedx when using -Werror
    * [Revision #3034.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.5)
      * Fixed test failure that ended with "There is no group named 'mysqld.10' that can be used to resolve 'port' for test"
    * [Revision #3034.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.4) \[merge]
      * Merge with main
    * [Revision #3034.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.3)
      * Merged InnoDB plugin from MySQL 5.1.54 -> MySQL 5.1.55 into xtradb
    * [Revision #3034.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.2) \[merge]
      * Merge with xtradb code changes
        * (4 tests are still failing, so this push is not yet stable)
      * [Revision #3030.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3030.1.2) \[merge]
        * Merge
      * [Revision #3030.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3030.1.1) \[merge]
        * Merge XtraDB from Percona Server 5.1.54-12.5 into MariaDB.
        * [Revision #0.6.45](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/0.6.45)
          * Updated with changes from Percona Server 5.1.54-12.5, from lp:percona-server as of February 4, 2011/
          * Merged: revid:oleg.tsarev@percona.com-20110113143630-b9ojivymbiwe3y2i
    * [Revision #3034.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034.1.1) \[merge]
      * Merge with MySQL 5.1.55
        * Fixed some issues with partitions and connection\_string, which also fixed [Bug #716890](https://bugs.launchpad.net/bugs/716890) "Pre- and post-recovery crash in Aria"
        * Fixed wrong assert in Aria
        * Now need to merge with latest xtradb before pushing
* [Revision #3037](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3037)
  * [Bug #688404](https://bugs.launchpad.net/bugs/688404) : Fix pbxt crashes on Windows 64 in debug build
  * The reason for the crash is misalignment on SSE instruciton\
    in setjmp(). The root cause is PBXT debug malloc(), which\
    unlike OS malloc does not guarantee 16 bytes alignment.
  * So the fix for now is disable PBXT debug malloc on Windows.\
    It was obsolete anyway, as it does not provide additional\
    benefits to C runtime debug routines (always used in debug\
    compilation) or to pageheap, available at runtime.
* [Revision #3036](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3036)
  * Enhanced tap to write out a message at which stage it was killed if it got a signal.
  * Added 'SIGINT' to list of tracked signals.
* [Revision #3035](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3035)
  * Fixed bug in federatedx patch that caused partition tests to fail.
  * Fixed that connection string is returned for partitioned federated tables.
* [Revision #3034](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3034) \[merge]
  * Automatic merge with trunk
    * [Revision #3032.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3032.1.2)
      * Fixed compiler warnings
    * [Revision #3032.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3032.1.1)
      * Applied patch for [Bug #585688](https://bugs.launchpad.net/bugs/585688) "maridb crashes in federatedx code" from lp:atcurtis/maria/federatedx:
        * Fixed Partition engine to store CONNECTION string for partitions.
          * Removed HA\_NO\_PARTITION flag from FederatedX.
          * Added test 'federated\_partition' to suite.
        * [Bug #585688](https://bugs.launchpad.net/bugs/585688) - maridb crashes in federatedx code
          * FederatedX handler instances, created on one thread and used on\
            another thread (via table cache) when "show table status" is executed\
            crashed because txn member was not initialized for current thread.
          * Added test 'federated\_bug\_585688' to suite.
      * Author for the patch is Antony Curtis
* [Revision #3033](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3033)
  * Fix build : declaration in the middle of statement in C file.
* [Revision #3032](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3032)
  * Fixes for Aria storage engine:
    * Fixed bug [Bug #624099](https://bugs.launchpad.net/bugs/624099) ma\_close.c:75: maria\_close: Assertion \`share->in\_trans == 0' failed on UNLOCK TABLES
    * Fixed bug that caused table to be marked as not closed (crashed) during recovery testing.
    * Use maria\_delete\_table\_files() instead of maria\_delete\_table() to delete tempoary tables (faster and safer)
    * Added checks to ensure that bitmap and internal mutex are always taken in right order.
    * For transactional tables, only mark the table as changed before page for table is to be written to disk (and thus the log is flushed).
      * This speeds up things a bit and fixes a problem where open\_count was incremented on disk but there was no log entry to fix it during recovery -> table was crashed.
    * Fixed a bug in repair() where table was not automaticly repaired.
    * Ensure that state->global\_changed, share->changed and share->state.open\_count are set and reset properly.
    * Added option `--ignore-control-file` to maria\_chk to be able to run maria\_chk even if the control file is locked.
* [Revision #3031](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3031)
  * Added missing header file strings\_def.h to dist
* [Revision #3030](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3030)
  * Fixed typo for non-debug build
* [Revision #3029](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3029)
  * Fixed bug in Archive with insert delayed
* [Revision #3028](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3028)
  * Don't delete directory mysql-test/var if we use mysql-test-run `--vardir=`
  * Fixed error in Maria unittest
  * Fixes other issues found by test case for [Bug #700623](https://bugs.launchpad.net/bugs/700623) "Aria recovery: ma\_blockrec.c:3930: \_ma\_update\_at\_original\_place: Assertion \`block->org\_bitmap\_value == .."
  * Fixes [Bug #670356](https://bugs.launchpad.net/bugs/670356) "Aria table "is marked as crashed and should be repaired"
* [Revision #3027](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3027)
  * Ignore some linked files
* [Revision #3026](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3026) \[merge]
  * Merge with 5.1
  * Fixed a couple of compilation failures that was not detected before merge.
    * [Revision #3023.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3023.1.2)
      * Aria fixes:
        * Fixed a bug where we didn't signal a thread waiting for bitmap flush that it's now time to continue which caused a deadlock in Aria.
        * Fix for [Bug #700623](https://bugs.launchpad.net/bugs/700623) "Aria recovery: ma\_blockrec.c:3930: \_ma\_update\_at\_original\_place: Assertion \`block->org\_bitmap\_value == \_ma\_bitmap\_get\_page\_bits(info, \&info->s->bitmap, page)' failed"
        * Fixed a bug in pagecache where a block could change while it was in use.
        * In maria\_chk set `--update-state` to on by default so that open\_count is cleared if table was ok during check.
    * [Revision #3023.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3023.1.1)
      * Flush DBUG log in case of DBUG\_ASSERT()
      * Added strings\_def.h into strings library to be able to have a DBUG\_ASSERT() version without \_db\_flush() call (as strings.a should not depend on dbug.a)
      * Remove include of m\_string.h in all string files (as it's included by string\_def.h).
      * Fixed include order.
      * Changed "m\_ctype.h" -> \<m\_ctype.h>
* [Revision #3025](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3025)
  * fixes for solaris 10
* [Revision #3024](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3024)
  * fix "`./configure --with-debug`" builds
  * (without CFLAGS=-DSAFEMALLOC).
* [Revision #3023](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3023)
  * Better fix for mysql\_test.cc::do\_remove\_files\_wildcard
* [Revision #3022](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3022)
  * Use \_ma\_set\_fatal\_error() in Aria also for HA\_ERR\_WRONG\_IN\_RECORD, to be able to get an assert as soon as a failure is detected.
  * Fixed stack overrun failure when calling maria\_chk\_data\_link().
* [Revision #3021](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3021)
  * Fixed bugs found by buildbot:
    * Use -Wno-uninitialized if -DFORCE\_INIT\_OF\_VARS is not used, to avoid warnings about not initialized variables.
    * Fixed compiler warnings
    * Added a name for each thr\_lock to get better error messages (This is needed to find out why 'archive.test' sometimes fails)
* [Revision #3020](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3020)
  * Aria issues:
    * Fix for [Bug #700623](https://bugs.launchpad.net/bugs/700623) "Aria recovery: ma\_blockrec.c:3930: \_ma\_update\_at\_original\_place: Assertion \`block->org\_bitmap\_value == \_ma\_bitmap\_get\_page\_bits(info, \&info->s->bitmap, page)' failed"
      * Issue was that when deleting a tail page where all index entries where full, the page was marked wrongly in the bitmap.
    * If debug\_assert\_if\_crashed\_table is set, we now crash when we find Aria corrupted.
    * Write more information if we find something wrong with the bitmap.
    * Fixed that REPAIR also can fix wrong create\_rename\_lsn issues (a very unlikely event)
    * Define STATE\_CRASHED\_FLAGS as set of all CRASHED flags (to simplify code)
* [Revision #3019](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3019)
  * Fixed bug that another thread used handler->s->id before it was recorded in the log.
  * This fixed an assert in recovert in mi\_recovery.c "cmp\_translog\_addr(rec->lsn, checkpoint\_start) < 0"
* [Revision #3018](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3018)
  * Fixed some mysql-test-run failures and compile warnings/errors
  * Added logging of all possible fatal table errors if `--log-warnings` set to `> 1`
* [Revision #3017](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3017)
  * Updated mysql-test-run to create on failure a var/log/files.log to allow us to analyze what was in the var directory on failure
  * This should help us analyze failures like innodb\_mysql.test that failes strangely in a CREATE TABLE statement.
* [Revision #3016](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3016) \[merge]
  * Merge
    * [Revision #3014.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3014.1.1)
      * Fixed [Bug #702310](https://bugs.launchpad.net/bugs/702310) / [MySQL Bug #59493](https://bugs.mysql.com/bug.php?id=59493).
      * An assertion failure was triggered for a 6-way join query that uses two\
        join buffers.
      * The failure happened because every call of the function flush\_cached\_records()\
        saved and restored status of all tables before the table join\_tab. It\
        must do it only for those of them that follow the last table that uses\
        a join buffer.
* [Revision #3015](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3015)
  * Call always ha\_index\_init(), not index\_init(), to ensure that active\_index is set correctly.
  * Fixes failures in merge.test
* [Revision #3014](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3014) \[merge]
  * Merge with 5.1
    * [Revision #3012.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3012.1.1)
      * Fix for [Bug #697610](https://bugs.launchpad.net/bugs/697610) ha\_index\_prev(uchar\*): Assertion \`inited==INDEX' failed with HANDLER + InnoDB in maria-5.3
* [Revision #3013](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3013) \[merge]
  * Merge [Bug #675118](https://bugs.launchpad.net/bugs/675118) into maria-5.1
    * [Revision #2998.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2998.1.1)
      * [Bug #675118](https://bugs.launchpad.net/bugs/675118): Elimination of a table results in an invalid execution plan
        * Fix for [MySQL Bug #52357](https://bugs.mysql.com/bug.php?id=52357) added NESTED\_JOIN::is\_fully\_covered() which would\
          not take into account that MariaDB's table elimination could eliminate tables\
          from join plan (and so, from join nest).
        * Fixed the check in the function to compare post-table-elimination numbers.
* [Revision #3012](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3012)
  * Fixed bug in Maria page cache that caused assert if block->request != 0 in free\_block()
* [Revision #3011](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3011)
  * Allow one to decrease page-buffer-size down to 1M (from 128M) for maria\_read\_log
  * Don't allow too low value of pagecache\_buffer\_size for mysqld
* [Revision #3010](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3010)
  * Allow smaller size for page-buffer-size
* [Revision #3009](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3009)
  * Fixed wrong test in maria\_rsame() that caused ma\_test\_all to fail.
* [Revision #3008](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3008)
  * Safety fix for Aria:
    * Set lastinx= 0 when last\_key.keyinfo is set.
* [Revision #3007](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3007)
  * Fixed that Aria works with HANDLER commands
  * Added test case for Aria
  * Tested HANDLER with HEAP (changes to HEAP code will be pushed in 5.3)
  * Moved all HANDLER test to suite/handler.
* [Revision #3006](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3006)
  * Don't do DBUG\_ASSERT for checksum errors when using REPAIR
  * mysql\_convert\_table\_format ignored `--engine` option.
  * Fix that zerofill() doesn't write out wrong data to client if run with auto repair.
  * Ensure that pagecache is properly flushed, even in case of errors.
  * Handle checksum errors in BLOCK\_RECORD format.
* [Revision #3005](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3005)
  * Bug fixing in Aria:
    * Fixed some bugs in recovery of blobs
    * Don't ASSERT() on checksum errors when running check table
    * Added to maria\_read\_log option `--tables-to-redo=list-of-tables` to only recover some tables (good for debugging)
* [Revision #3004](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3004)
  * Fixed overwrite of directory information on the row page.
  * This could only happen with very small rows on very full pages with old deleted information in middle of page.
* [Revision #3003](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3003)
  * ALTER TABLE IGNORE didn't ignore duplicates for unique add index for InnoDB
* [Revision #3002](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3002)
  * Make copy from heap to MyISAM / Aria killable.
  * Fixes [Bug #695006](https://bugs.launchpad.net/bugs/695006) converting HEAP to Aria" status do not respond to KILL QUERY
* [Revision #3001](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3001)
  * Fixed recovery problem in Aria where bitmap had wrong information after recovery.
  * [Bug #619731](https://bugs.launchpad.net/bugs/619731): Aria recovery corruption "Page 1: Row: 1 has an extent with wrong information in bitmap
* [Revision #3000](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/3000)
  * Updated README for MTR test suite
* [Revision #2999](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2999)
  * Speed up `mtr --parallel=<lots>` by scheduling some slow tests earlier.
  * The patch also fixes a race in rpl\_stop\_slave.test.
  * On machines with lots of CPU and memory, something like `mtr --parallel=10`\
    can speed up the test suite enormously. However, we have a few test cases\
    that run for long (several minutes), and if we are unlucky and happen to\
    schedule those towards the end of the test suite, we end up with most\
    workers idle while waiting for the last slow test to end, significantly\
    delaying the finish of the entire suite.
  * Improve this by marking the offending tests as taking "long", and trying\
    to schedule those tests early. This reduces the time towards the end of\
    the test suite run where some workers are waiting with nothing to do for\
    the remaining workers each to finish their last test.
  * Also, the rpl\_stop\_slave test had a race which could cause it to take\
    a 300 seconds debug\_sync timeout; this is fixed.
  * Testing on a 4-core 8GB machine, this patch speeds up the test suite with\
    around 30% for `--parallel=10` (debug build), allowing to run the entire\
    suite in 5 minutes.
* [Revision #2998](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2998)
  * Fixed [Bug #639935](https://bugs.launchpad.net/bugs/639935) ([MySQL Bug #58727](https://bugs.mysql.com/bug.php?id=58727)).
    * When the optimizer creates items out of other items it does\
      not have to call the fix\_fields method. Usually in these\
      cases it calls quick\_fix\_field() that just marks the\
      created item as fixed. If the created item is an Item\_func\
      object then calling quick\_fix\_field() works fine if the\
      arguments of the created functional item are already fixed.\
      Otherwise some unfixed nodes remain in the item tree and\
      it triggers an assertion failure whenever the item is\
      evaluated.
    * Fixed the problem by making the method quick\_fix\_field\
      virtual and providing an implementation for the class\
      Item\_func objects that recursively calls the method\
      for unfixed arguments of any functional item.
* [Revision #2997](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2997)
  * Increased version number to 5.1.54
* [Revision #2996](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2996)
  * Fixed bug in Aria that caused REPAIR to find old deleted rows.
* [Revision #2995](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2995)
  * Fixed typo that caused compile failure in thr\_lock.c
* [Revision #2994](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2994)
  * Fix for [Bug #686010](https://bugs.launchpad.net/bugs/686010) maria.optimize corrupts stack around alloca() call
* [Revision #2993](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2993)
  * Better warning message if lock test fails
  * Made archive.test a bit more safe
* [Revision #2992](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2992)
  * [Bug #687320](https://bugs.launchpad.net/bugs/687320): Fix sporadic test failures in innodb\_mysql.test and partition\_innodb\_semi\_consistent.test
    * Problem is that these tests run with `--innodb-lock-wait-timeout=2` in .opt\
      (and this is necessary as built-in innodb does not allow to change this\
      dynamically). This cases another part of the test to occasionally time\
      out an UPDATE, which subsequently caused the test case to timeout due to\
      waiting for a condition (successful UPDATE) that never occurs.
    * Fixed by re-trying the update in case of timeout.
    * Tested by inserting a sleep() in the connection that the UPDATE is waiting\
      for, and checking that the retry loops a couple of times until the other\
      connection is done and COMMITs.
* [Revision #2991](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2991)
  * Made sure that SELECT from the test case for bug BUG#56862/64041 uses\
    the same execution plan that is in the output of the corresponding\
    EXPLAIN.
* [Revision #2990](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2990)
  * [Bug #677407](https://bugs.launchpad.net/bugs/677407) / [MySQL Bug #48883](https://bugs.mysql.com/bug.php?id=48883): Stale data from INNODB\_LOCKS table.
  * The logic for how to check when to update the table cache for\
    INNODB\_LOCKS with real data was flawed. This could result in both\
    not updating the cache often enough (when the table is queried\
    repeatedly with less than 100 milliseconds in-between) resulting\
    in stale data; as well as updating too often (when multiple\
    queries against the table start at around the same time).
  * This caused occasional test failures in innodb\_information\_schema.
  * Fix by updating the "last updated" timestamp in the right place,\
    when the cache is updated, not when it is read.
* [Revision #2989](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2989)
  * Fix myisam\_crash\_before\_flush\_keys on Windows
  * Problem : mtr reports test failure because it sees\
    \[ERROR] mysqld got exception 0x80000003 ;\
    in the .err file
  * The exception comes from DBUG\_EXECUTE\_IF (.. abort())
  * Fix: use DBUG\_ABORT instead of abort() - it does not throw\
    any exceptions.
* [Revision #2988](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2988)
  * Fix [Bug #686184](https://bugs.launchpad.net/bugs/686184) - merge\_debug test fails.
    * The reason for failure is that DBUG\_EXECUTE\_IF in mi\_open()\
      only worked for Unix-formatted file names, due to strstr(name, "/crashed")
    * The fix change strstr() above to strstr(name, "crashed"), to it can work with\
      Windows file names as well.
* [Revision #2987](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2987) \[merge]
  * merge
    * [Revision #2982.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2982.1.1)
      * [Bug #473914](https://bugs.launchpad.net/bugs/473914): mysql\_client\_test fail with in debug compilaton on windows x64
        * Reason: inconsistent compilation, federatedx is compiled without SAFEMALLOC\
          flag, while anything else is compiled with SAFEMALLOC.
        * As a consequence, my\_hash\_init used inside federatedx initialization does not\
          provide correct caller info parameters (file, line) , so they are initialized with\
          whatever is on stack. When info about allocated memory is output in\
          COM\_DEBUG command, the server crashes trying to output string starting at\
          0xcccccccccccccccc.
        * The fix is to remove SAFEMALLOC preprocessor flags\
          from every CMakeLists.txt, except the top-level one.
        * Also, SAFEMALLOC is not defined by default now, instead\
          there is WITH\_DEBUG\_FULL CMake option which adds\
          -DSAFEMALLOC to C and C++ flags in debug compilation.\
          This option is off by default, because
          * Debug C runtime already has heap debugging builtin with overwrite and leak detection
          * safemalloc considerably slows down the tests.\\
        * Note also that
          * SAFEMALLOC is gone in MySQL5.5
          * On Windows, heap related overflows can also be found using free pageheap utility
    * (that is also part of application verifier). This is even more efficient if there are no other layers on top of Windows heap allocator, e.g it is most efficient with release version.
* [Revision #2986](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2986)
  * Fixed test case to be repeatable (after discussion with Igor)
* [Revision #2985](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2985) \[merge]
  * Merge with 5.1-release
* [Revision #2984](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2984) \[merge]
  * automatic merge with 5.1-release
* [Revision #2983](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2983) \[merge]
  * Automatic merge with 5.1-release
* [Revision #2982](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2982) \[merge]
  * merge
    * [Revision #2981.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2981.1.3)
      * address review comments
    * [Revision #2981.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2981.1.2)
      * Adapt fix\_vs\_config\_dir () for VS2010
      * MTR\_VS\_CONFIG is now determined by looking at parent directory\
        of sql\*\mysqld.exe, instead of looking at \*\*\BuildLog.htm
      * Reason : VS2010 does not create BuildLog.htm, hence prior method did not work.
    * [Revision #2981.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2981.1.1)
      * Make maria 5.1 compilable on Visual Studio 2010 and remove Windows warnings
        * Remove all mentioning of /MAP /MAPINFO link options (does not work in VS2010). Remove map files from packaging.
        * Fix warning about ETIMEDOUT being redefined.
        * Fix warning about FSP\_EXTENT\_SIZE in xtradb (32/64 bit right shift mismatch)
        * Silence warnings coming from generated code (flex/bison) in xtradb/innodb\_plugin.
        * Be nice to people without cygwin (me) and add win/configure-mariadb.bat with options suitable for quick compilation, e.g no embedded

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
