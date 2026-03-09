# MariaDB 5.2.4 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.2.4) | [Release Notes](../../old-releases/5.2/5.2.4.md) | **Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 6 Dec 2010

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.4.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #2894](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2894)
  * Removed compiler warning
* [Revision #2893](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2893) \[merge]
  * merge with 5.1-release
    * [Revision #2643.96.43](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.43)
      * Fixes to not trigger end-consistency testing of pagecache.
        * Moved end\_pagecache() to after maria\_close()
        * Flush page cache before closing files (in maria\_pack)
      * Fixed test suite failure for PBXT
    * [Revision #2643.96.42](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.42)
      * The assert removed because it do not take into account case when previous\
        and this buffers used for first time but previous buffer was not sent to\
        disk yet (i.e. previous buffer was never sent to disk yet).
* [Revision #2892](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2892) \[merge]
  * Automatic merge
    * [Revision #2890.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2890.1.3) \[merge]
      * Automatic merge with 5.1-release
        * [Revision #2643.96.41](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.41)
          * Aria unit tests fixed to have correct pagecache shutdown.
          * The Aria multithread test unlocked.
        * [Revision #2643.96.40](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.40)
          * Removed assert as gcc on gentoo couldn't compile it without a warning :(
          * (Not critical, we will just catch the error later)
        * [Revision #2643.96.39](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.39)
          * Fixed (wrong) compiler warning
    * [Revision #2890.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2890.1.2) \[merge]
      * Merge with 5.1
        * [Revision #2643.114.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.2) \[merge]
          * Automatic merge with 5.1-release
            * [Revision #2643.96.38](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.38)
              * Fixed compiler warning
              * Added missing inc\_counter\_for\_resize\_op(pagecache).
              * (caused maria.maria-preload.test to fail)
            * [Revision #2643.96.37](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.37)
              * Fixed compiler warnings.
              * Fixed timing test failures.
              * Fixed a failure in the Aria engines page cache and log handler (found with maria.maria-big test)
                * This could cause a core dump when deleting big blobs.
                * Added test to end\_pagecache() to verify that page cache was correctly used.
                  * inc\_counter\_for\_resize\_op and dec\_counter\_for\_resize\_op are called same number of times.
                  * All page cache blocks was properly deallocated (empty)
            * [Revision #2643.96.36](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.36)
              * Fix problems seen in Buildbot:
                * Make sure creation of t1 is replicated before trying to create trigger on it on slave
                * Use safe #ifdef for declaration as for definition to avoid warning about unused static function.
        * [Revision #2643.114.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.1) \[
          * merge]
          * merge
    * [Revision #2890.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2890.1.1)
      * Fixed compiler warnings but calling field->store(longlong, unsigned\_flag) with proper arguments.
* [Revision #2891](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2891) \[merge]
  * merge
    * [Revision #2643.105.44](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.44)
      * address review comments
    * [Revision #2643.105.43](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.43)
      * Adapt fix\_vs\_config\_dir () for VS2010
      * MTR\_VS\_CONFIG is now determined by looking at parent directory\
        of sql\*\mysqld.exe, instead of looking at \*\*\BuildLog.htm
      * Reason : VS2010 does not create BuildLog.htm, hence prior method did not work.
    * [Revision #2643.105.42](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.42)
      * Make maria 5.1 compilable on Visual Studio 2010 and remove Windows warnings
        * Remove all mentioning of /MAP /MAPINFO link options (does not work in VS2010).
          * Remove map files from packaging.
        * Fix warning about ETIMEDOUT being redefined.
        * Fix warning about FSP\_EXTENT\_SIZE in xtradb (32/64 bit right shift mismatch)
        * Silence warnings coming from generated code (flex/bison) in xtradb/innodb\_plugin.
        * Be nice to people without cygwin (me) and add win/configure-mariadb.bat with options suitable for quick compilation, e.g no embedded
* [Revision #2890](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2890) \[merge]
  * automatic merge with 5.1
    * [Revision #2643.96.35](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.35) \[merge]
      * Automatic merge with 5.1
    * [Revision #2643.96.34](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.34)
      * Fixed failures in buildbot
    * [Revision #2643.96.33](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.33)
      * [MySQL Bug #54201](https://bugs.mysql.com/bug.php?id=54201): "SET INSERT\_ID" event must be ignored if corresponding event is ignored
      * An INSERT query log event is preceeded by an INSERT\_ID intvar event if the\
        INSERT allocates a new auto\_increment value. But if we ignore the INSERT\
        due to `--replicate-ignore-table` or similar, then the INSERT\_ID event is\
        still executed, and the set value of INSERT\_ID lingers around in the\
        slave sql thread THD object indefinitely until the next INSERT that\
        happens to need allocation of a new auto\_increment value.
      * Normally this does not cause problems as such following INSERT would\
        normally come with its own INSERT\_ID event. In this bug, the user had\
        a trigger on the slave which was missing on the master, and this\
        trigger had an INSERT which could be affected. In any case, it seems\
        better to not leave a stray INSERT\_ID hanging around in the sql thread\
        THD indefinitely.
      * Note that events can also be skipped from apply\_event\_and\_update\_pos();\
        however it is not possible in that code to skip the INSERT without also\
        skipping the INSERT\_ID event.
* [Revision #2889](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2889)
  * Fixed compiler warnings
* [Revision #2888](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2888) \[merge]
  * merge with 5.1
    * [Revision #2643.105.41](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.41) \[merge]
      * Automatic merge with 5.1-release
        * [Revision #2643.96.32](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.32)
          * Fixed some compiler warnings
    * [Revision #2643.105.40](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.40)
      * Use three digits after the decimal point for better resolution and comparability of results.
    * [Revision #2643.105.39](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.39) \[merge]
      * Automatic merge with 5.1-release
        * [Revision #2643.96.31](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.31)
          * Fixed compiler and gmake warnings
            * Removed SCCS rule from Makefile.am
            * Made dummy rule in sql\_yacc.yy to get rid of compiler warning about not used label.
          * Don't use maintainer mode with valgrind (as we don't want to initialize all variables)
        * [Revision #2643.96.30](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.30)
          * Fixed compiler warnings and a compilation failure on windows
        * [Revision #2643.96.29](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.29)
          * Patch from Sergey Petrunya:
          * Fix post-merge failure in 5.1-merge
            * Let QUICK\_RANGE\_INTERSECT\_SELECT not make assumption that HA\_EXTRA\_KEYREAD\
              scans do not touch parts of table->record\[0] that refer to fields that are\
              not covered by the used index.
            * This assumption is not true for XtraDB (e.g. grep row/row0sel.c for\
              "init null bytes with default values as they might be").
        * [Revision #2643.96.28](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.28) \[merge]
          * Automatic merge with 5.1
        * [Revision #2643.96.27](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.27)
          * Fixed failing test cases
        * [Revision #2643.96.26](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.26)
          * Merge of innodb\_plugin for MySQL 5.1.53 with xtradb
          * Fixed compiler warnings in xtradb
          * Added back resetting of null bitmap but now in row\_search\_for\_mysql()
        * [Revision #2643.96.25](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.25)
          * A proper fix for [MySQL Bug #57688](https://bugs.mysql.com/bug.php?id=57688).
          * Introduced a new flag in the class Item. The flag is set\
            to 1 only for items that are used in GROUP BY lists of\
            queries with ROLLUP.
        * [Revision #2643.96.24](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.24) \[merge]
          * Automatic merge with base
            * [Revision #2643.113.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.113.1) \[merge]
              * Merge with MySQL 5.1.53
              * Open issues:
                * A better fix for #57688; Igor is working on this
                * Test failure in index\_merge\_innodb.test ; Igor promised to look at this
                * Some Innodb tests fails (need to merge with latest xtradb) ; Kristian promised to look at this.
                  * Failing tests: innodb\_plugin.innodb\_bug56143 innodb\_plugin.innodb\_bug56632 innodb\_plugin.innodb\_bug56680 innodb\_plugin.innodb\_bug57255
                * Werror is disabled; Should be enabled after merge with xtradb.
        * [Revision #2643.96.23](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.23)
          * Fix test failure when the mysql-test/ directory is not writable.
        * [Revision #2643.96.22](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.22) \[merge]
          * Merge XtraDB from Percona-Server 5.1.52-11.6 into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)\
            revid:oleg.tsarev@percona.com-20101118145125-wjhjrb5jwhi0g7sj
            * [Revision #0.6.44](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/0.6.44)
              * Updated with changes from lp:percona-server/release-5.1.52-11 as of November 24, 2010
              * Merged: revid:oleg.tsarev@percona.com-20101118145125-wjhjrb5jwhi0g7sj
        * [Revision #2643.96.21](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.96.21) \[merge]
          * Automerge with 5.1
            * [Revision #2643.112.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.112.1) \[merge]
              * Merge with MySQL 5.1.52
    * [Revision #2643.105.38](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.38)
      * Fix of [Bug #675248](https://bugs.launchpad.net/bugs/675248).
      * Registration of pointer change if we assign it to other pointer which should be identical after statement execution (PS/SP).
* [Revision #2887](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2887)
  * Use three digits after the decimal point for better resolution and comparability of results.
* [Revision #2886](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2886) \[merge]
  * Automerge [mariadb 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md) into [mariadb 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)
    * [Revision #2643.105.37](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.37)
    * Fix test failure with OpenSSL due to different error message than in YaSSL.
* [Revision #2885](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2885) \[merge]
  * Merge [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)->5.2
    * [Revision #2643.105.36](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.36)
      * Fix of the debugging print.
    * [Revision #2643.105.35](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.35)
      * [MWL#74](https://askmonty.org/worklog/?tid=74): Shared libmysqld.so library.
      * Switch makefiles to use libtool to build libmysqld.so, as well as all its\
        dependencies.
      * The previous MYSQL\_PLUGIN\_DEPENDS\_ON\_MYSQL\_INTERNALS() declaration is removed,\
        as it does not work well with a libtool build. Instead, plugins that need it\
        can specify an alternate object in MYSQL\_PLUGIN\_STATIC() that will be used for\
        embedded library. The plugin must then take care itself of compiling the\
        special object for embedded, rebuilding the source files previously listed in\
        MYSQL\_PLUGIN\_DEPENDS\_ON\_MYSQL\_INTERNALS() with @plugin\_embedded\_defs@ in\
        CFLAGS/CXXFLAGS. The extra target @XXX\_embedded\_static\_target@ is available\
        for the special object, this will be empty when `--without-embedded-server`.
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
    * [Revision #2643.105.34](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.34)
      * [Bug #643463](https://bugs.launchpad.net/bugs/643463): Slow XtraDB shutdown: Fix more sleeps delaying shutdown.
      * This patch removes most remaining delays due to uninteruptible sleep()\
        during shutdown, as found using PMP. This makes standard test run very\
        close in speed to with `--loose-innodb-fast-shutdown=2`, and greatly\
        speeds up running the test suite.
    * [Revision #2643.105.33](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.33)\
      Fix flags for non-debug builds
    * [Revision #2643.105.32](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.32)\
      Fixed mess in the types.
    * [Revision #2643.105.31](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.31)
      * Fixed bug discovered by testcase for [Bug #618558](https://bugs.launchpad.net/bugs/618558) (original bug seams to be fixed):
        * Fixed bug in pagecache\_delete\_internal() when deleting block that was flushed by another thread (fixed bug when block->next\_used was unexpectedly null)
      * Fixed some using uninitialized memory warnings found by valgrind.
    * [Revision #2643.105.30](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.105.30)
      * Added option BACKUP\_ALL to mysqld `--myisam-recover` to also get a backup of the index file before it's repaired.
      * Removed wrong call to translog\_buffer\_unlock() that caused 'unlocking not locked mutex' failure in Aria log handler.
* [Revision #2884](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2884)
  * fix for [Bug #673634](https://bugs.launchpad.net/bugs/673634):
  * better MYSQL\_PLUGIN\_WITHOUT that works correctly in all of the following:
    * `--with-plugin-XXX`
    * `--without-plugin-XXX`
    * `--with-plugins=XXX`
    * `--with-plugins=META`
    * `--with-plugins=XXX --without-plugin-XXX`
    * `--with-plugins=META --without-plugin-XXX`

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
