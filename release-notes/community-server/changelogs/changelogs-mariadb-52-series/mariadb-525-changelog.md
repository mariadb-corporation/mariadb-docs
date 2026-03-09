# MariaDB 5.2.5 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.2.5) | [Release Notes](../../old-releases/5.2/5.2.5.md) | **Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 3 Mar 2011

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.5.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #2929](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2929)\
  Tue 2011-03-01 23:24:17 +0200
  * Fixed wrong alias usage
* [Revision #2928](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2928)\
  Tue 2011-03-01 18:31:33 +0100
  * use mtr\_verbose() for debug output in suite.pm files
* [Revision #2927](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2927) \[merge]\
  Tue 2011-03-01 17:04:17 +0200
  * merge
    * [Revision #2643.114.65](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.65)\
      Tue 2011-03-01 16:21:27 +0200
      * Fixed for mac sed.
* [Revision #2926](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2926) \[merge]\
  Tue 2011-03-01 15:51:35 +0200
  * Merge with 5.1
    * [Revision #2643.114.64](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.64)\
      Tue 2011-03-01 15:31:24 +0200
      * Revoked changes from MySQL 5.1.55 merge as Sergei's code is more general
    * [Revision #2643.114.63](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.63)\
      Tue 2011-03-01 15:19:25 +0200
      * Allow -Wuninitialized without -O only for gcc 4.4 and upper
* [Revision #2925](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2925)\
  Tue 2011-03-01 13:37:29 +0200
  * Fixed wrong filenames in maria unittest that caused unittest to fail
* [Revision #2924](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2924) \[merge]\
  Tue 2011-03-01 00:46:13 +0200
  * Merge with 5.1 to get fixes for tests and compiler warnings
    * [Revision #2643.114.62](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.62)\
      Mon 2011-02-28 23:24:19 +0200
      * Get rid of compiler warnings
    * [Revision #2643.114.61](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.61)\
      Mon 2011-02-28 19:47:19 +0200
      * Increase version number
      * Taged a couple of tests with `--big-test`
* [Revision #2923](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2923)\
  Tue 2011-03-01 00:35:05 +0200
  * Fixes to mysql-test-run and tests
    * Added ORDER BY to get consistent results to federated\_server
    * Sort slow tests first
* [Revision #2922](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2922) \[merge]\
  Mon 2011-02-28 19:39:30 +0200
  * Merge with 5.1 to get in changes from MySQL 5.1.55
* [Revision #2921](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2921) \[merge]\
  Mon 2011-02-28 13:16:17 +0200
  * Merge with alias as String
    * [Revision #2883.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2883.1.2)\
      Mon 2011-02-28 12:48:50 +0200
      * Change TABLE->alias to String for less memory reallocation
      * Changed some String.ptr() -> String.c\_ptr() for String that are not guaranteed to end with \0
      * Removed some c\_ptr() usage from parameters to functions that takes ptr & length
      * Use preallocate buffers to avoid calling malloc() for most operations.
    * [Revision #2883.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2883.1.1) \[merge]\
      Tue 2010-11-09 10:20:09 +0200
      * automatic merge
        * [Revision #2882.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2882.1.1)\
          Mon 2010-11-08 13:43:54 +0200
          * Make SQLString reallocation addaptive
          * Avoid doing reallocs
          * Prealloc some strings / provide extension allocation size to some strings\
            This gave a 25 % speedup in some mysql-test-run tests.
* [Revision #2920](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2920)\
  Thu 2011-02-03 16:45:29 +0200
  * Increased precision for status variables Rows\_sent and Rows\_read from long to longlong
  * Fixed that status variables 'empty\_queries', 'access\_denied\_errors' and 'lost\_connections' are propageted to global status.
  * This should also remove some warnings with VC++
* [Revision #2919](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919)\
  Sat 2011-01-29 12:04:37 +0200
  * Fix compilation errors (and some warnings) when compiling ndb
  * Fixes part of [Bug #705213](https://bugs.launchpad.net/bugs/705213) (Other part is to be pushed into 5.1)
* [Revision #2918](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2918)\
  Mon 2011-01-24 15:47:28 +0200
  * Fix of [Bug #706884](https://bugs.launchpad.net/bugs/706884): fill\_record should be used for only one table (no need list).
* [Revision #2917](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2917)\
  Thu 2011-01-20 13:00:46 +0100
  * [Bug #705210](https://bugs.launchpad.net/bugs/705210) - Compiling with BUILD/compile-pentium64-debug fails
  * support building with -all-static (no dlopen and dlclose make few\
    related declarations unused or "statement have no effect") and -Werror
* [Revision #2916](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2916)\
  Thu 2011-01-20 12:59:47 +0100
  * [Bug #700982](https://bugs.launchpad.net/bugs/700982) - Non-portable code in client plugin (fails on ARM).
  * don't pass NULL as an argument where va\_list is expected.
* [Revision #2915](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2915)\
  Wed 2011-01-12 12:11:21 +0100
  * fix function prototype to follow the API
* [Revision #2914](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2914)\
  Fri 2011-01-14 16:51:18 +0200
  * Added suppression for failure on opensuse 64 bit.
* [Revision #2913](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2913) \[merge]\
  Fri 2011-01-14 16:49:27 +0200
  * Merge with 5.1
* [Revision #2912](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2912)\
  Thu 2011-01-13 13:28:36 +0100
  * [Bug #702303](https://bugs.launchpad.net/bugs/702303): Spurious `use` statements in output from mysqlbinlog `--rewrite-db="a->b"`
* [Revision #2911](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2911)\
  Wed 2011-01-12 17:58:13 +0200
  * Fixed assert as Aria in 5.2 has more flags than 5.1
* [Revision #2910](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2910) \[merge]\
  Wed 2011-01-12 17:38:13 +0200
  * Merge with 5.1
* [Revision #2909](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2909) \[merge]\
  Tue 2011-01-11 14:29:19 +0200
  * automatic merge with 5.1
* [Revision #2908](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2908) \[merge]\
  Mon 2011-01-10 23:42:47 +0200
  * Automatic merge with 5.1
* [Revision #2907](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2907) \[merge]\
  Fri 2011-01-07 18:07:22 +0200
  * merge with 5.1
* [Revision #2906](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2906)\
  Fri 2011-01-07 13:45:59 +0200
  * Fixed typos
  * Patch provided by Dolf Schimmel
* [Revision #2905](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2905) \[merge]\
  Fri 2011-01-07 13:12:09 +0200
  * Merge with base 5.2
    * [Revision #2903.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2903.1.3)\
      Fri 2011-01-07 12:17:34 +0200
      * Aria fixes:
        * Don't delete pages without flushing that has had a tail or head information in pagecache\_delete()
        * This fixes a case where REPAIR could find old deleted rows.
    * [Revision #2903.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2903.1.2) \[merge]\
      Fri 2011-01-07 12:05:46 +0200
      * Merge with 5.1
    * [Revision #2903.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2903.1.1) \[merge]\
      Wed 2011-01-05 16:03:58 +0200
      * Merge with 5.1
* [Revision #2904](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2904)\
  Thu 2011-01-06 15:55:29 +0100
  * [Bug #698132](https://bugs.launchpad.net/bugs/698132): Fix wrong buffer calculation in send\_change\_user\_packet()
* [Revision #2903](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2903)\
  Fri 2010-12-31 10:39:14 +0100
  * virtual columns:
    * move a capability from a virtual handler method to table\_flags()
    * rephrase error messages to avoid hard-coded English parts
    * admit in test cases that they need xtradb, not innodb
* [Revision #2902](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2902)\
  Mon 2010-12-27 10:53:02 +0100
  * fixes bug: [Bug #683112](https://bugs.launchpad.net/bugs/683112)
  * [Bug #665028](https://bugs.launchpad.net/bugs/665028) SHOW STORAGE ENGINES shows incorrect Transaction support for Aria
  * don't fill in handlerton::commit member, as it's not used\
    and makes MySQL believe that Aria is transactional.
  * Fix the TRANSACTIONAL=1 warning.
* [Revision #2901](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2901)\
  Mon 2010-12-20 19:19:24 +0100
  * [Bug #683112](https://bugs.launchpad.net/bugs/683112) Maria 5.2 incorrectly reports "(using password: NO)" even when password is specified
  * set thd->password appropriately also for cases when a user was not found.
* [Revision #2900](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2900)\
  Fri 2010-12-17 08:33:36 +0100
  * [Bug #691437](https://bugs.launchpad.net/bugs/691437): storage/sphinx/plug.in missing from source tarball.
  * It was missing from EXTRA\_DIST in Makefile.am.
* [Revision #2899](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2899) \[merge]\
  Mon 2010-12-13 15:51:47 +0200
  * merge with 5.1
  * (Includes patch for overrun detected by valgrind thanks to previous my\_alloca() -> my\_malloc() patch)
* [Revision #2898](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2898)\
  Mon 2010-12-13 15:05:57 +0200
  * When compiling with valgrind, change my\_alloca() to use my\_malloc()
    * This allows us to detect missing my\_afree() calls and also find overruns (when running with valgrind) to alloca() areas.
    * Added missing my\_afree() calls
    * Fixed wrong call to my\_afree()
* [Revision #2897](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2897)\
  Fri 2010-12-10 09:51:34 +0100
  * Fix wrong merge of patch for [MySQL Bug #46639](https://bugs.mysql.com/bug.php?id=46639).
* [Revision #2896](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2896) \[merge]\
  Tue 2010-12-07 00:14:16 +0100
  * merge [Bug #686184](https://bugs.launchpad.net/bugs/686184)
* [Revision #2895](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2895) \[merge]\
  Mon 2010-12-06 13:16:49 +0100
  * merge with 5.1

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
