# MariaDB 5.1.51 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.51) | [Release Notes](../../old-releases/5.1/5.1.51.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 19 Nov 2010

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.51.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #2976](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2976)
  * Fix of the debugging print.
* [Revision #2975](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2975)
  * [MWL#74](https://askmonty.org/worklog/?tid=74): Shared libmysqld.so library.
    * Switch makefiles to use libtool to build libmysqld.so, as well as all its\
      dependencies.
    * The previous MYSQL\_PLUGIN\_DEPENDS\_ON\_MYSQL\_INTERNALS() declaration is\
      removed, as it does not work well with a libtool build. Instead, plugins\
      that need it can specify an alternate object in MYSQL\_PLUGIN\_STATIC() that\
      will be used for embedded library. The plugin must then take care itself of\
      compiling the special object for embedded, rebuilding the source files\
      previously listed in MYSQL\_PLUGIN\_DEPENDS\_ON\_MYSQL\_INTERNALS() with\
      @plugin\_embedded\_defs@ in CFLAGS/CXXFLAGS. The extra target\
      @XXX\_embedded\_static\_target@ is available for the special object, this will\
      be empty when `--without-embedded-server`.
    * All in-tree plugins are changed to build their static targets with libtool.\
      Additional plugins that want to work with libmysqld.so will need to be\
      similarly modified to build with libtool (or otherwise provide an -fPIC\
      object). Dynamically loaded plugins are not affected.
    * The old libraries like libmysys.a, libmyisam.a and similar libraries, which\
      were installed by `make install` though this is of little use, are still built\
      and installed to not break package scripts etc. that expect them. These\
      libraries are kept static to avoid introducing new .so dependencies.
    * The patch also fixes a handfull of duplicate symbol linker errors, where we\
      included some object twice during linking; these for one reason or another did\
      not produce errors before but caused problems on some platforms with this\
      patch (eg. Mac OS X linker is more strict for shared objects).
    * This patch only does what is necessary to build libmysqld.so. There are some\
      more cleanups that are possible now that we are using libtool more fully,\
      which could done in subsequent patches (though we may not bother as we are\
      switching from autotools to CMake anyway):
      * In libmysql\_r/, we should be able to just link libmysys.la etc, instead of\
        symlinking and re-compiling sources into the directory.
      * In libmysql/, we can similarly avoid symlinking and recompiling sources if\
        we instead build a libmysys\_nothread.la library with appropriate CFLAGS and\
        link that.
      * In sql/, we can build a separate target libmysql\_int.la with appropriate\
        CFLAGS for embedded and use that in libmysqld/ instead of symlinking\
        sources.
      * libmysys.a, libmyisam.a and similar libraries could be installed as .so\
        also to save on code size; or alternatively could be not installed at all.
* [Revision #2974](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2974)
  * [Bug #643463](https://bugs.launchpad.net/bugs/643463): Slow XtraDB shutdown: Fix more sleeps delaying shutdown.
    * This patch removes most remaining delays due to uninteruptible sleep()\
      during shutdown, as found using PMP. This makes standard test run very\
      close in speed to with `--loose-innodb-fast-shutdown=2`, and greatly speeds\
      up running the test suite.
* [Revision #2973](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2973)
  * Fix flags for non-debug builds
* [Revision #2972](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2972)
  * Fixed mess in the types.
* [Revision #2971](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2971)
  * Fixed bug discovered by testcase for [Bug #618558](https://bugs.launchpad.net/bugs/618558) (original bug seams to be fixed):
    * Fixed bug in pagecache\_delete\_internal() when deleting block that was\
      flushed by another thread (fixed bug when block->next\_used was unexpectedly\
      null) Fixed some using uninitialized memory warnings found by valgrind.
* [Revision #2970](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2970)
  * Added option BACKUP\_ALL to mysqld `--myisam-recover` to also get a backup of\
    the index file before it's repaired.
  * Removed wrong call to translog\_buffer\_unlock() that caused 'unlocking not\
    locked mutex' failure in Aria log handler.
* [Revision #2969](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2969) \[merge]\
  Automatic merge
  * [Revision #2967.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2967.1.1)
    * When scanning pages, stop when you are at 'data\_file\_length'.
    * This fixes a bug that gave ER\_FILE\_TOO\_SHORT error when scanning Aria tables.
* [Revision #2968](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2968)
  * [Bug #643463](https://bugs.launchpad.net/bugs/643463): slow XtraDB shutdown due to 10 second sleep in purge thread
    * Implement os\_event\_wait\_time() for POSIX systems.
    * In the purge thread, use os\_event\_wait\_time() when sleeping rather than sleep,\
      and signal the event when server shuts down, so we do not need to wait for\
      upto 10 seconds until the purge thread wakes up.
    * Also fix bug that warnings that were pushed after we call set\_ok\_status() were\
      not included in the waning count sent to the client in the result packet.
    * Also in mysqltest, in recursive die() invocation at least print the message\
      before aborting.
* [Revision #2967](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2967)
  * Fixed compile error when not using gcc (crashes at least on windows)
* [Revision #2966](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2966) \[merge]
  * Automatic merge
  * [Revision #2964.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2964.1.1)
    * Fixed compiler & valgrind warnings from my previous push.
    * Fixed a bug in Aria when two threads was inserting into the same table and\
      row page and one thread did an abort becasue of duplicate key.
* [Revision #2965](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2965)
  * \#endif fixed.
* [Revision #2964](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2964)
  * Fix for: [Bug #634955](https://bugs.launchpad.net/bugs/634955): Assert in \_ma\_update\_at\_original\_place()
  * Added locking of lock mutex when updating status in external\_unlock() for\
    Aria and MyISAM tables.
  * Fixed that 'source' command doesn't cause mysql command line tool to exit on error.
  * DEBUG\_EXECUTE() and DEBUG\_EVALUATE\_IF() should not execute things based on\
    wildcards. (Allows one to run `--debug` with mysql-test-run scripts that uses\
    @debug)
  * Fixed several core dump, deadlock and crashed table bugs in handling of LOCK\
    TABLE with MERGE tables:
    * Added priority of locks to avoid crashes with MERGE tables.
    * Added thr\_lock\_merge() to allow one to merge two results of thr\_lock().
  * Fixed 'not found row' bug in REPLACE with Aria tables.
  * Mark MyISAM tables that are part of MERGE with HA\_OPEN\_MERGE\_TABLE and set\
    the locks to have priority THR\_LOCK\_MERGE\_PRIV.
    * By sorting MERGE tables last in thr\_multi\_unlock() it's safer to release\
      and relock them many times (can happen when TRIGGERS are created)
  * Avoid printing (null) in debug file (to easier find out wrong NULL pointer\
    usage with %s).
* [Revision #2963](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2963)
  * mysqltest: Fix reversed error check, causing truncated output when testcase fails.
  * Also fix missing zero termination in DBUG\_PRINT, causing garbage output\
    in `--debug` output.
* [Revision #2962](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2962)
  * Fix test failure (timeout) in `--valgrind` tests in Buildbot.
  * The main.ps\_ddl test does `SELECT * FROM mysql.general_log;` that can be really\
    expensive with `--valgrind` if previous test cases put lots of data in the\
    general log since last server restart. Fix by truncating the log at test start.
* [Revision #2961](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2961)
  * workaround for [MySQL Bug #57491](https://bugs.mysql.com/bug.php?id=57491)
* [Revision #2960](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2960)
  * Show the number of warm keycache blocks in SHOW STATUS
* [Revision #2959](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2959)
  * Make the skip-on-windows check as the first one, as the master-slave include\
    fails on windows.
* [Revision #2958](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2958)
  * better fix for MySQL bugs
    * [MySQL Bug #26447](https://bugs.mysql.com/bug.php?id=26447) prefer a clustered key for an index scan, as secondary index is\
      always slower
      * ... which was fixed to cause
    * [MySQL Bug #35850](https://bugs.mysql.com/bug.php?id=35850) queries take 50% longer
      * ... and was reverted
  * and
    * [MySQL Bug #39653](https://bugs.mysql.com/bug.php?id=39653) prefer a secondary index for an index scan, as clustered key is\
      always slower
      * ... which was fixed to cause
    * [MySQL Bug #55656](https://bugs.mysql.com/bug.php?id=55656) mysqldump takes six days instead of half an hour
      * ... and was amended with a special case workaround
* [Revision #2957](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2957)
  * fixes [Bug #618608](https://bugs.launchpad.net/bugs/618608) build mysqld.exe with federatedx not federated
* [Revision #2956](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2956)
  * updated test results
* [Revision #2955](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2955)
  * fixed a bad merge
* [Revision #2954](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2954) \[merge]
  * Merge XtraDB from Percona-server-5.1.51-12 into MariaDB.
  * [Revision #2952.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2952.1.1) \[merge]
    * Merge XtraDB from Percona-server-5.1.51-12 into MariaDB.
    * [Revision #0.6.43](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/0.6.43)
      * Updated with changes from lp:percona-server/release-5.1.51-12 as of October 19, 2010
* [Revision #2953](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2953) \[merge]
  * MySQL 5.1.51 merge
* [Revision #2952](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2952)
  * Reverted the MySQL fix for [MySQL Bug #51242](https://bugs.mysql.com/bug.php?id=51242) that was rejected once for\
    mariadb-5.1.48 and mistakingly pulled in back for maria-5.1.50.
* [Revision #2951](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2951)
  * Fixes for bugs found by running test case for [Bug #608369](https://bugs.launchpad.net/bugs/608369) "Page: 1 Found wrong\
    page type 0' on CHECK TABLE EXTENDED"
  * Fixed overflow when using long `--debug=xxxxxx` line.
  * Fixed that "`mysqld --disable-debug --debug`" works.
  * Ensure that MariaDB doesn't start if the Aria engine didn't start and we are\
    using Aria for temporary tables.
  * More DBUG\_ASSERT() and more info in debug log.
* [Revision #2950](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2950)
  * Use less memory on stack in sql\_parse.cc and in repair/check for MyISAM & Aria
* [Revision #2949](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2949)
  * Fixes some bug in Aria recovery:
    * \_ma\_apply\_redo\_index: Assertion \`page\_offset != 0 && page\_offset + length <= page\_length' failed
  * Fixes one bug and one log assert when inserting rows:
    * \_ma\_log\_split: Assertion \`org\_length <= info->s->max\_index\_block\_size' failed
    * write\_block\_record: Assertion '(data\_length < MAX\_TAIL\_SIZE(block\_size)' failed
  * Mark in recovery log where \_ma\_log\_add() calls was done (for better debugging).
* [Revision #2948](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2948) \[merge]
  * Automatic merge
    * [Revision #2945.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2945.1.1)
      * Fix for [MySQL Bug #43152](https://bugs.mysql.com/bug.php?id=43152) "Assertion \`bitmap\_is\_set\_all(\&table->s->all\_set)'\
        failed in handler::ha\_reset"
      * The reason for this was that some bitmap test functions changed the\
        bitmap, which caused problems when the same bitmap was used by multiple\
        threads.
* [Revision #2947](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2947)
  * Don't use deprecated `--skip-locking` option in example config files.
* [Revision #2946](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2946) \[merge]
  * merge
    * [Revision #2940.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2940.1.2)
      * clarified mtr treatment of the `--plugin-load` option in the mysql-test/README.suites file.
  * [Revision #2940.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2940.1.1)
    * fix for [MySQL Bug #44797](https://bugs.mysql.com/bug.php?id=44797) - plugins w/o command-line options have no disabling option in `--help`
* [Revision #2945](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2945)
  * Merge with 1.0.11-7 Pre-GA - 2010-09-09
  * Updated results for failing test cases (In all cases the estimated number of rows was different)
* [Revision #2944](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2944) \[merge]
  * Merge
    * [Revision #2943.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2943.1.1)
      * Fixed [MySQL Bug #57024](https://bugs.mysql.com/bug.php?id=57024).
      * The condition over the outer tables now are extracted from the on\
        condition of any outer join. This condition is saved in a special field of\
        the JOIN\_TAB structure for the first inner table of the outer join. The\
        condition is checked before the first inner table is accessed. If it turns\
        out to be false the table is not accessed at all and a null complemented\
        row is generated immediately.
* [Revision #2943](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2943) \[merge]
  * Merge
    * [Revision #2938.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2938.1.2)
      * Changed the test case for [MySQL Bug #53161](https://bugs.mysql.com/bug.php?id=53161) to make it independent on\
        the setting of optimizer switch for table elimination.
* [Revision #2942](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2942) \[merge]
  * Merge
    * [Revision #2938.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2938.1.1)
      * Fixed [MySQL Bug #53161](https://bugs.mysql.com/bug.php?id=53161):\
        The implementation of the virtual method not\_null\_tables for the class\
        Item\_outer\_ref must always return 0.
* [Revision #2941](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2941) \[merge]
  * Merge
    * [Revision #2933.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2933.1.1)
      * Fixed [MySQL Bug #56862](https://bugs.mysql.com/bug.php?id=56862) ([Bug #640419](https://bugs.launchpad.net/bugs/640419)):\
        Made sure that rr\_quick is used to read the next record whenever\
        a quick select is used to retrieve the table records.
* [Revision #2940](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2940)
  * fixes for windows
* [Revision #2939](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2939)
  * bug in plugin.m4 that prevented group list in the MYSQL\_PLUGIN declaration\
    from working.
* [Revision #2938](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2938) \[merge]
  * Automatic merge
    * [Revision #2932.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2932.1.1)
      * mysqltest now gives error messages with error code for my\_delete,\
        my\_rename, my\_copy etc.
      * Fixed crashing bug when doing ALTER TABLE RENAME with transactional\
        tables.
* [Revision #2937](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2937)
  * Fix preserving mysqld error log across server restarts, broken by recent mtr\
    changes.
* [Revision #2936](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2936) \[merge]
  * Merge: fix valgrind failure in Unique class
    * [Revision #2928.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2928.2.1)
      * Fix valgrind failure with Unique class
* [Revision #2935](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2935)
  * don't build dynamic plugins when configured with `--disable-shared`.
  * libtool does not like it and fails the build.
* [Revision #2934](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2934) \[merge]
  * merged
    * [Revision #2928.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2928.1.2)
      * to simpliy and unify the code
    * [Revision #2928.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2928.1.1)
      * build dynamic plugins with the -shared libtool option to avoid\
        double compilation
* [Revision #2933](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2933)
  * Adjusted the results of pbxt.join\_nested after the fix for [MySQL Bug #49600](https://bugs.mysql.com/bug.php?id=49600)
* [Revision #2932](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2932) \[merge]
  * Merge
    * [Revision #2929.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2929.1.1)
      * Fixed Aria recovery bug:\
        When reopening table during recovery, don't set file length from file\
        sizes as file is not flushed.
      * New feature in Aria recovery:\
        Create database directory if missing.
* [Revision #2931](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2931) \[merge]
  * Merge
    * [Revision #2927.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2927.2.1)
      * Fixed [MySQL Bug #49600](https://bugs.mysql.com/bug.php?id=49600):
      * The problem could be demonstrated with an outer join of two single-row\
        tables where the values of the join attributes were null. Any query\
        with such a join could return a wrong result set if the where\
        condition of the query was not empty. For queries with empty\
        where conditions the result sets were correct.
      * This was the consequence of two bugs in the code:
        * Item\_equal objects for on conditions of outer joins were\
          not built if the processed query had no where condition
        * the check for null values in the code that evaluated constant\
          Item\_equal objects was incorrect.
      * Fixed both above problems.
      * Added a test case for the bug and adjusted results for some other\
        test cases.
* [Revision #2930](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2930) \[merge]
  * Merge
    * [Revision #2927.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2927.1.2) \[merge]
      * Pulled in the latest changes in 5.1.
    * [Revision #2927.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2927.1.1)
      * Fixed [MySQL Bug #49322](https://bugs.mysql.com/bug.php?id=49322):\
        When not-exists optimization was applied to a table that\
        happened to be an inner table of two outer joins, one\
        embedded into another, then setting the match flag for\
        the embedding outer join on could be skipped. This caused\
        generation of extra null complemented rows.\
        Made sure that the match flags are set correctly in all cases\
        when not-exists optimization is used.
* [Revision #2929](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2929)
  * Fix for [Bug #634943](https://bugs.launchpad.net/bugs/634943) "marked as crashed", "zerofilling" and "wrong data in\
    bitmap" when recovering Aria tables
    * This was an interaction of several bugs:
      * Tables marked as opened was not properly unmarked on recovery if there was\
        not changes since checkpoint
      * zerofill of tables put wrong data in bitmap if directory for page was full
      * Tables was thought as 'moved' during recovery if they had a create\_lsn\
        bigger than the lsn in the control file.
* [Revision #2928](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2928)
  * Fixed [Bug #605798](https://bugs.launchpad.net/bugs/605798) "wrong data in bitmap" after recovery.
  * Extend remove\_function\_from\_trace.pl to work with many threads (patch from\
    Sergei)
* [Revision #2927](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2927)
  * Updated failure text for maria\_install\_db
  * Don't give warning about block\_insert if table is crashed.
* [Revision #2926](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2926) \[merge]
  * Automatic merge with 5.1-release (5.1.50)
* [Revision #2925](https://bazaar.launchpad.net/~maria-captains/maria/5.1/revision/2925)
  * Write message to stderr if recovery is not likely to succeed because we don't log records for batch inserts.
  * Don't do UNDO or REDO on a crashed table.
  * More DBUG\_PRINT

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
