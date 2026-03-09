# MariaDB 5.1.50 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.50) | [Release Notes](../../old-releases/5.1/5.1.50.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 09 Sep 2010

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.50.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #2911](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2911)
  * Give a more precise warning why something fails.
  * Fixed typo that caused warnings from mysql-test-run
* [Revision #2910](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2910) \[merge]
  * Automatic merge
    * [Revision #2891.3.6](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.3.6)
      * Fixed recovery bug where bitmap pages would not be correctly updated after\
        processing UNDO rows.
      * Fixed test failures in buildbot
      * Don't write errors when failing to send ok packet
    * [Revision #2891.3.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.3.5)
      * Fixed compiler failures when compiling non debug build
    * [Revision #2891.3.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.3.4) \[merge]
      * Automatic merge
        * [Revision #2891.1.29](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.29)
          * Fixed bug that 'maria\_read\_log -a' didn't set max\_trid when reparing tables.
          * Fixed bug in Aria when replacing short keys with long keys and a key\
            tree both overflow and underflow at same time.
          * Fixed several bugs when generating recovery logs when using RGQ with\
            replacing long keys with short keys and vice versa.
          * Lots of new DBUG\_ASSERT()'s
          * Added more information to recovery log to make it easier to know from\
            where log entry orginated.
          * Introduced MARIA\_PAGE->org\_size that tells what the size of the page was\
            in last log entry. This allows us to find out if all key changes for\
            index page was logged.
          * Small code cleanups:
            * Introduced \_ma\_log\_key\_changes() to log crc of key page changes
            * Added share->max\_index\_block\_size as max size of data one can put in\
              key block (block\_size - KEYPAGE\_CHECKSUM\_SIZE)
          * This will later simplify adding a directory to index pages.
            * Write page number instead of page postition to DBUG log
    * [Revision #2891.3.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.3.3)
      * make the check for windows\
        to work in cygnin perl too
    * [Revision #2891.3.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.3.2)
      * typo fixed
* [Revision #2909](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2909)
  * Added `--skip-bdb` as a compatibility option for old config files
* [Revision #2908](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2908)
  * Fixed compiler warnings
* [Revision #2907](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2907)
  * Fix compile failures and warnings on Windows from XtraDB "shm buffer pool" patch.\
    (It is not legal C to do pointer arithmetics on void \*).
* [Revision #2906](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2906)
  * Added missing include file (to get rid of compiler warning)
* [Revision #2905](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2905)
  * Fixed build failures
  * Cleaned up "`mysql_upgrade --help`" and "`mysqlcheck --help`"
* [Revision #2904](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2904)
  * Fixed failing test cases after update of xtradb
* [Revision #2903](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2903)
  * Nicer output for mysql\_upgrade
  * Added `--silent` option to mysql\_upgrade so that one can only get errors printed
  * Don't write unnecessary warning about log tables during upgrade
* [Revision #2902](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2902)
  * Result file update following XtraDB merge.
* [Revision #2901](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2901) \[merge]
  * Merge XtraDB from Percona Server 5.1.49-12 into MariaDB.
    * [Revision #2896.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2896.1.2)
      * Enable tests that were previously disabled waiting for XtraDB merge.
    * [Revision #2896.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2896.1.1) \[merge]
      * Merge XtraDB from Percona server 5.1.49-12 into MariaDB.
        * [Revision #0.6.42](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/0.6.42)
          * Updated with changes from lp:percona-server/release-5.1.49-12 as of September 3, 2010
* [Revision #2900](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2900)
  * Update test to use the shorter table names
* [Revision #2899](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2899)
  * Enable archive tables to work with mysql\_upgrade / repair
  * Made long file names from previous patch shorter
* [Revision #2898](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2898)
  * Fix that one can run mysql\_upgrade with long table names
  * Fall back to use ALTER TABLE for engines that doesn't support REPAIR when doing repair for upgrade.
  * Nicer output from mysql\_upgrade and mysql\_check
  * Updated all arrays that used NAME\_LEN to use SAFE\_NAME\_LEN to ensure that we don't break things accidently as names can now have a #mysql50

## prefix.

* [Revision #2897](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2897)
  * Fixed bugs (mostly on sparc) that caused crashes in mysql-test-run
* [Revision #2896](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2896)
  * Fixed test failure
* [Revision #2895](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2895)
  * Fixed build & test failures in buildbot
* [Revision #2894](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2894) \[merge]
  * Automatic merge
    * [Revision #2891.3.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.3.1)
      * use the correct path separator on windows.
      * remove duplicates from the `--plugin-load` list.
      * $ENV{TERM} can be undefined (on Windows)
* [Revision #2893](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2893)
  * Fixed failing tests
* [Revision #2892](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2892) \[merge]
  * Automerge
    * [Revision #2891.1.28](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.28) \[merge]
      * Merge with MySQL 5.1.50
        * Changed to still use bcmp() in certain cases becasue
          * Faster for short unaligneed strings than memcmp()
          * Bettern when using valgrind
        * Changed to use my\_sprintf() instead of sprintf() to get higher\
          portability for old systems
        * Changed code to use MariaDB version of select->skip\_record()
        * Removed -%::SCCS/s.% from Makefile.am:s to remove automake warnings
    * [Revision #2891.1.27](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.27)
      * mtr changes:
        * expanding unknown env variable does not abort mtr
        * have\_archive, blackhole, innodb - preload the corresponding engine
        * all options from .opt files get equal treatment, all are searched for\
          special options, not only -{master,slave}.opt as before (which ignored\
          suite.opt and `--mysqld=...`)
        * `--plugin-load` gets special treatment too - all instances are merged into\
          one
        * federated test fixed to preload federated
    * [Revision #2891.1.26](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.26)
      * Fixed typo in last push (sorry about that)
        * Need to get autopush to work to avoid bad pushes like this....
    * [Revision #2891.1.25](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.25)
      * Fixed failing test
      * Increased default buffers to speed up maria\_chk
    * [Revision #2891.1.24](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.24) \[merge]
      * Automatic merge
      * Fixed compiler warning
        * [Revision #2891.2.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.2.5)
          * Increase some very old limits.
          * This will give a smoother experience when using the Aria engine by those\
            that are using default limits without still causing a notable problem\
            for desktop users.
    * [Revision #2891.1.23](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.23) \[merge]
      * Automatic merge
        * [Revision #2891.2.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.2.4) \[merge]
          * Automatic merge with main 5.1
        * [Revision #2891.2.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.2.3)
          * Fix of [Bug #616253](https://bugs.launchpad.net/bugs/616253) Crash in \_ma\_bitmap\_set\_full\_page\_bits on Aria\
            recovery
          * The bug was based on wrong undo data in recovery file and not enough\
            checking of bad data.
        * [Revision #2891.2.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.2.2)
          * Trivial fixes, more safe DBUG\_ASSERT()'s and some more DBUG\_
            * CTRL-C now aborts 'source' commands in mysql client
            * Fix that thread id's are removed in convert-debug-for-diff.sh
        * [Revision #2891.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.2.1)
          * Fix for [Bug #612894](https://bugs.launchpad.net/bugs/612894) Some aggregate functions (such as MIN MAX) work\
            incorrectly in subqueries after getting NULL value
    * [Revision #2891.1.22](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.22)
      * allow suite.pm to tell mtr to skip the suite
    * [Revision #2891.1.21](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.21)
      * generalization of mtr to support suite.pm extensions:
        * no automatic `--loose-skip-innodb` added by mtr based on the test name.\
          instead loose-skip-innodb is now in the default\_mysqld.cnf
        * have\_innodb\_plugin.inc is changed to give a verbose "skip" message\
          (instead of "require: true")
        * My::Suite class. It's support in mtr, and everywhere
        * support for suite.pm
        * when sorting tests, take combinations into account
        * support for SUITENAME\_COMBINATIONS
        * no special treatment for innodb\_plugin in mtr\_cases.pm
        * two special pre-created config groups: ENV and OPT
        * allow option names to start from #
        * allow magic option to have an argument
        * remove dead code
        * fix @-substitution to works as expected
        * new processes take the value of $opt\_verbose automatically, no need to\
          pass it to a constructor
        * innodb\_plugin suite uses suite.pm and combinations file to test as much\
          as possible (innodb plugin, xtradb plugin, xtradb static - whatever\
          available)
        * besides test-master.opt and test-slave.opt a test.opt file is also\
          loaded, both for master and slave
        * .opt files for all included files are loaded too
        * progress report in the xterm titlebar
    * [Revision #2891.1.20](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.20)
      * missing DBUG\_RETURNs
    * [Revision #2891.1.19](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.19)
      * created \*-all build scripts that build with ndb\
        (as -max scripts don't)
    * [Revision #2891.1.18](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.18)
      * Fixed compilation failure and added some new suppressions
    * [Revision #2891.1.17](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.17)
      * Fixed wrong macro that caused compile failures when compiling without DBUG
    * [Revision #2891.1.16](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.16)
      * Fixed valgrind errors and compiler warnings discovered by buildbot
      * More DBUG\_ASSERT() to discover errors earlier
      * More checking of BLOCK structures in Aria.
      * Fixed crashing bug in Aria when doing UPDATE of several records in same\
        block when doing table scan.
    * [Revision #2891.1.15](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.15)
      * Added verbose mode to recovery
      * More DBUG
      * Added convert-debug-for-diff
      * Added missing (from last push) federated test case
    * [Revision #2891.1.14](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.14)
      * Trivial optimizations and cleanups
    * [Revision #2891.1.13](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.13)
      * Fix for [Bug #571200](https://bugs.launchpad.net/bugs/571200) [MySQL Bug #32426](https://bugs.mysql.com/bug.php?id=32426): FederatedX corrupt ORDER BY with TEXT
      * Patch taken from lp:capttofu/maria/bug\_571200 (originally for MariaDB\
        5.3, but adapted for 5.1)
    * [Revision #2891.1.12](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.12)
      * Added option `--start-from-checkpoint` to maria\_read\_log
      * Print out checked file names in maria\_check -s (unless you use a second -s)
      * Some trivial optimizations
    * [Revision #2891.1.11](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.11)
      * Disable events\_time\_zone.test as test is not predictable
    * [Revision #2891.1.10](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.10)
      * Fixed compiler warnings from Windows compiler
    * [Revision #2891.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.9)
      * Fixed [Bug #605798](https://bugs.launchpad.net/bugs/605798) RQG: Table corruption after Maria engine recovery - "Wrong data in bitmap"
      * maria\_chk & maria\_read\_log now reads block size from control file.
    * [Revision #2891.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.8)
      * Fixed typo that caused compile failure on Mac
      * Added straight\_join to make results predicatable
    * [Revision #2891.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.7)
      * Fixed wrong argument to translog\_write\_record() that caused core dump in\
        maria.maria-gis-rtree-trans and some other tests
      * (Bug introduced by my last push)
    * [Revision #2891.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.6)
      * Ignore ENOLCK errno from FreeBSD (known problem in old FreeBSD releases)
    * [Revision #2891.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/2891.1.5)
      * Added `--sync-sys=0` option for mysqld to skip sync() calls for faster testing
      * Fixed [Bug #613418](https://bugs.launchpad.net/bugs/613418) (M) aria recovery failure: ma\_key\_recover.c:981:\
        \_ma\_apply\_redo\_index: Assertion \`check\_page\_length == page\_length' failed

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
