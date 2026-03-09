# MariaDB 5.2.11 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.2.11) |[Release Notes](../../old-releases/5.2/5.2.11.md) |**Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 2 Apr 2012

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.11.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3130](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3130) \[merge]\
  Fri 2012-03-30 16:12:21 +0200
  * merge
  * [Revision #2643.127.86](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.86)\
    Fri 2012-03-30 16:09:57 +0200
    * [MDEV-205](https://jira.mariadb.org/browse/MDEV-205) don't install libevent headers
* [Revision #3129](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3129) \[merge]\
  Fri 2012-03-30 13:51:16 +0300
  * Automatic merge
  * [Revision #2643.127.85](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.85)\
    Fri 2012-03-30 13:42:52 +0300
    * Fixed [Bug #967914](https://bugs.launchpad.net/bugs/967914) "CHECK TABLE persistently reports table corruption after removing Aria logs"
    * Fixed that repair removes the 'table is moved' mark.
* [Revision #3128](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3128) \[merge]\
  Thu 2012-03-29 21:15:30 +0200
  * merge
  * [Revision #2643.127.84](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.84)\
    Thu 2012-03-29 18:06:08 +0200
    * fix the test case for windows: replace\_result /
  * [Revision #2643.127.83](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.83)\
    Thu 2012-03-29 16:36:06 +0200
    * make the code compile again
* [Revision #3127](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3127) \[merge]\
  Wed 2012-03-28 13:49:07 +0300
  * Merge with 5.1
  * [Revision #2643.127.82](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.82)\
    Wed 2012-03-28 13:22:21 +0300
  * Fixed [Bug #944422](https://bugs.launchpad.net/bugs/944422) "mysql\_upgrade destroys Maria tables?"
  * The issue was that check/optimize/anaylze did not zerofill the table before they started to work on it.
  * Added one more element to not often used function handler::auto\_repair() to allow handler to decide when to auto repair.
* [Revision #3126](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3126) \[merge]\
  Wed 2012-03-21 18:30:34 +0100
  * merge
  * [Revision #2643.127.81](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.81)\
    Wed 2012-03-21 18:22:02 +0100
    * [Bug #933959](https://bugs.launchpad.net/bugs/933959) Assertion \`0' failed in net\_end\_statement(THD\*) on concurrent SELECT FROM I\_S.INNODB\_SYS\_INDEXES and ALTER TABLE
    * Workaround: report a generic error if an I\_S plugin failed silently.
  * [Revision #2643.127.80](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.80)\
    Thu 2012-03-15 15:06:06 +0100
    * Fix access to uninitialized variable in innodb error message in case WriteFile() fails.
  * [Revision #2643.127.79](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.79)\
    Wed 2012-03-14 21:16:24 +0100
    * restore my\_safe\_printf\_stderr for "crash-safe sigsegv handler"
      * use vsnprintf()
      * use write() on windows, not WriteFile or fwrite()
      * localtime\_r is still a problem
* [Revision #3125](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3125)\
  Wed 2012-03-14 12:09:03 +0200
  * test suite for [Bug #694450](https://bugs.launchpad.net/bugs/694450)
* [Revision #3124](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3124) \[merge]\
  Mon 2012-03-12 12:15:55 +0100
  * merge
  * [Revision #2643.127.78](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.78)\
    Mon 2012-03-12 11:31:40 +0100
    * [Bug #952714](https://bugs.launchpad.net/bugs/952714): Fix formatting of the crash messages in signal/exception handler
* [Revision #3123](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3123)\
  Mon 2012-03-12 12:14:04 +0100
  * [Bug #952607](https://bugs.launchpad.net/bugs/952607): Do not show MySQL services preinstalled by Dell in the upgrade wizard
* [Revision #3122](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3122)\
  Fri 2012-03-09 15:37:16 -0800
  * Fixed [Bug #930814](https://bugs.launchpad.net/bugs/930814).
    * This bug was introduced into [mariadb 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md) in the December 2010 with\
      the patch that added a new engine property: the ability to support\
      virtual columns.
    * As a result of this bug the information from frm files for tables\
      that contained virtual columns did not appear in the information schema\
      tables.
* [Revision #3121](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3121)\
  Fri 2012-03-09 14:28:02 +0200
  * Added test case for [Bug #905782](https://bugs.launchpad.net/bugs/905782) "Assertion `pageno < ((1ULL)` <<\` 40)' failed at ma\_pagecache.c:3438: pagecache\_read or table corruption on INSERT into a ucs2 table"
  * The orignal bug has been fixed earlier
* [Revision #3120](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3120)\
  Fri 2012-03-09 14:06:17 +0200
  * Added ucs2 test moved from maria3.test. ([MDEV-167](https://jira.mariadb.org/browse/MDEV-167))
* [Revision #3119](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3119)\
  Thu 2012-03-08 22:33:01 -0800
  * Fixed [Bug #884175](https://bugs.launchpad.net/bugs/884175).
  * If in the where clause of the a query some comparison conditions on the\
    field under a MIN/MAX aggregate function contained constants whose sizes\
    exceeded the size of the field then the query could return a wrong result\
    when the optimizer had chosen to apply the MIN/MAX optimization.
  * With such conditions the MIN/MAX optimization still could be applied, yet\
    it would require a more thorough analysis of the keys built to find\
    the value of MIN/MAX aggregate functions with index look-ups.
  * The current patch just prohibits using the MIN/MAX optimization in this\
    situation.
* [Revision #3118](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3118) \[merge]\
  Tue 2012-03-06 01:48:38 +0100
  * merge
  * [Revision #3116.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3116.1.1)\
    Tue 2012-03-06 01:46:32 +0100
    * [Bug #947631](https://bugs.launchpad.net/bugs/947631): Uninstall wipes HeidiSQL settings, even if HeidiSQL is installed prior to MariaDB
    * Fixed detection of installed HeidiSQL in the machine, prevent installing own copy if HeidiSQL is already installed.
    * On deinstallation, do not remove settings if official HeidiSQL is detected.
* [Revision #3117](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3117)\
  Thu 2012-03-01 09:27:42 +0200
  * Return original checksum value inside the test.
  * Move ucs2 test in separate file ([MDEV-167](https://jira.mariadb.org/browse/MDEV-167)).
* [Revision #3116](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3116) \[merge]\
  Tue 2012-02-28 13:50:30 +0200
  * Automatic merge
  * [Revision #3113.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3113.1.1)\
    Tue 2012-02-28 13:39:02 +0200
    * Fixed [Bug #905716](https://bugs.launchpad.net/bugs/905716) "Assertion \`page->size <= share->max\_index\_block\_size'"
    * The issue was that Aria allowed too long keys to be created (so that the internal buffer was not big enough to hold the whole key).
    * Key lengths is now limited to HA\_MAX\_KEY\_LENGTH (1000), as for MyISAM.
    * Fixed failure in "\_ma\_apply\_redo\_index: Assertion \`new\_page\_length == 0", as found by buildbot.
* [Revision #3115](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3115)\
  Sat 2012-02-25 17:10:07 -0800
  * Fixed [Bug #939866](https://bugs.launchpad.net/bugs/939866).
  * The field key\_cache\_mem\_size of the KEY\_CACHE structure must be\
    initialized in the function init\_key\_cache() and updated in the\
    function resize\_key\_cache().
* [Revision #3114](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3114)\
  Sat 2012-02-25 09:03:06 +0200
  * Fix of [Bug #938518](https://bugs.launchpad.net/bugs/938518) (also [Bug #791761](https://bugs.launchpad.net/bugs/791761) and [Bug #806955](https://bugs.launchpad.net/bugs/806955))
  * Cause of the bug is uninitialized items before evaluation HAVING clasue in case of empty result.
* [Revision #3113](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3113) \[merge]\
  Fri 2012-02-24 17:21:44 +0200
  * Automatic merge
  * [Revision #2643.127.77](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.77)\
    Fri 2012-02-24 17:01:47 +0200
    * Fix for [Bug #909635](https://bugs.launchpad.net/bugs/909635): MariaDB crashes on a select with long varchar and blob fields
    * Problem was a crash in internal temporary (Maria) files when row length exceeded 65535
* [Revision #3112](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3112)\
  Wed 2012-02-22 00:10:39 -0800
  * Back-ported the fix and test cases for bugs #59487 and #43368 from\
    the mysql-5.6 code line.
* [Revision #3111](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3111) \[merge]\
  Tue 2012-02-21 17:48:15 +0200
  * Automatic merge with 5.1
  * [Revision #2643.127.76](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.76)\
    Tue 2012-02-21 14:17:33 +0200
    * Fixed suppression expression.
* [Revision #3110](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3110)\
  Tue 2012-02-21 09:35:46 +0200
  * Fixed wrong test case
* [Revision #3109](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3109) \[merge]\
  Tue 2012-02-21 01:55:12 +0200
  * Merge with 5.1
  * [Revision #2643.127.75](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.75) \[merge]\
    Tue 2012-02-21 01:51:55 +0200
    * Automatic merge
    * [Revision #2643.135.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.135.1)\
      Tue 2012-02-21 01:44:50 +0200
      * More general handling of memory loss in dlclose (backported from 5.2)
      * Fixed supression in mysql-test-run so it also works on windows.
* [Revision #3108](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3108) \[merge]\
  Tue 2012-02-21 01:49:14 +0200
  * Automatic merge
  * [Revision #3106.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3106.1.2)\
    Tue 2012-02-21 01:46:51 +0200
    * Added missing signal values to signal\_handler.cc
    * [Revision #3106.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3106.1.1) \[merge]\
      Mon 2012-02-20 17:58:00 +0200
      * Merge with 5.1
* [Revision #3107](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3107) \[merge]\
  Mon 2012-02-20 18:46:22 +0100
  * merge
  * [Revision #2643.127.74](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.74)\
    Mon 2012-02-20 18:07:38 +0100
    * Fix compilation on Windows, and various Windows related mistakes introduced by\
      "safe exception patch".
    * Remove misleading comments suggesting about signal() Windows, the routine here\
      is part of a exception handler, and sig parameter is an exception code.
  * [Revision #2643.127.73](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.73)\
    Mon 2012-02-20 17:56:47 +0200
    * Fixed compiler warnings
* [Revision #3106](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3106) \[merge]\
  Mon 2012-02-20 17:49:21 +0200
  * Merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md) and MySQL 5.1.61
  * [Revision #2643.127.72](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.72) \[merge]\
    Mon 2012-02-20 16:23:18 +0200
    * Merge with MYSQL 5.1.61
    * Fixed README with link to source
    * Merged InnoDB change to XtraDB
  * [Revision #2643.127.71](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.71) \[
    * merge]\
      Sat 2012-02-11 16:42:46 +0100
    * merge
  * [Revision #2643.127.70](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.70)\
    Wed 2012-01-25 11:34:43 +0100
    * mtr runs only "big" tests, if `--big-test` is repeated twice
  * [Revision #2643.127.69](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.69)\
    Wed 2012-01-04 20:10:15 +0100
    * report innodb\_file\_per\_table, innodb\_flush\_log\_at\_trx\_commit, innodb\_flush\_method
* [Revision #3105](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3105)\
  Mon 2012-02-20 14:03:44 +0200
  * Fixed [Bug #902654](https://bugs.launchpad.net/bugs/902654) "MariaDB consistently crashes in collect\_tables on Aria checkpoint execution"
  * This happend when you have more than 1024 open Aria tables during checkpoint.
* [Revision #3104](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3104)\
  Thu 2012-02-16 16:06:49 -0800
  * Fixed [Bug #933117](https://bugs.launchpad.net/bugs/933117).
  * The bug was fixed with the code back-ported from the patch for [Bug #800184](https://bugs.launchpad.net/bugs/800184)\
    pushed into mariadb-5.3.
* [Revision #3103](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3103)\
  Sun 2012-02-12 23:02:56 +0100
  * Use newly released HeidiSQL 7.0 in the MSI installer
* [Revision #3102](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3102) \[merge]\
  Sat 2012-02-11 15:05:07 +0100
  * merge
  * [Revision #3098.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3098.1.1) \[merge]\
    Sat 2012-02-11 14:57:44 +0100
    * Fix for [MDEV-140](https://jira.mariadb.org/browse/MDEV-140), [Bug #930145](https://bugs.launchpad.net/bugs/930145) - broken SSL connectivity for some connectors
    * [Revision #2643.134.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.134.3)\
      Sat 2012-02-11 03:25:49 +0100
      * fixes [Bug #930145](https://bugs.launchpad.net/bugs/930145)
      * A recent change in the server protocol code broke SSL connection for some client libraries.
      * Protocol documentation\
        ([MySQL\_Internals\_ClientServer\_Protocol](https://forge.mysql.com/wiki/MySQL_Internals_ClientServer_Protocol)) says\
        that initial packet sent by client if client wants SSL, consists of client\
        capability flags only (4 bytes or 2 bytes edependent on protocol\
        versionl). Some clients happen to send more in the initial SSL packet (C\
        client, Python connector), while others (Java, .NET) follow the docs and\
        send only client capability flags.
      * A change that broke Java client was a newly introduced check that frst\
        client packet has 32 or more bytes. This is generally wrong, if client\
        capability flags contains CLIENT\_SSL.
      * Also, fixed the code such that read max client packet size and charset in\
        the first packet prior to SSL handshake. With SSL, clients do not have to\
        send this info, they can only send client flags.
      * This is now fixed such that max packet size and charset are not read prior\
        to SSL handshake, in case of SSL they are read from the "complete" client\
        authentication packet after SSL initialization.
* [Revision #3101](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3101)\
  Fri 2012-02-03 12:24:55 +0200
  * Fixed DELETE issues of view over view over table.
* [Revision #3100](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3100)\
  Fri 2012-02-03 10:31:30 +0200
  * Added 5.2 test result delimiter
* [Revision #3099](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3099)\
  Fri 2012-02-03 10:28:23 +0200
  * Fix check of view updatability in case of underlying view changes its updatability.
    * For single table update/insert added deep check of single tables (single\_table\_updatable()).
    * For multi-table view insert added additional check of target table (check\_view\_single\_update).
    * Multi-update was correct.
  * Test suite for all cases added.
* [Revision #3098](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3098)\
  Mon 2012-01-23 11:43:28 +0100
  * [MDEV-106](https://jira.mariadb.org/browse/MDEV-106) my\_gethwaddr() does not compile on Solaris 11
* [Revision #3097](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3097)\
  Fri 2012-01-20 23:54:43 -0800
  * Fixed [Bug #919427](https://bugs.launchpad.net/bugs/919427).
  * The function subselect\_uniquesubquery\_engine::copy\_ref\_key has to take into\
    account that when EXPLAIN is processed the array of store\_key object created\
    for any TABLE\_REF may contain elements for constant items. These items should\
    be ignored by thefunction.
* [Revision #3096](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3096)\
  Thu 2012-01-12 20:13:41 +0100
  * [Bug #901693](https://bugs.launchpad.net/bugs/901693) dialog.c:perform\_dialog treats every password prompt as first
* [Revision #3095](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3095)\
  Thu 2012-01-12 20:13:22 +0100
  * [Bug #893522](https://bugs.launchpad.net/bugs/893522) more problems found by PVS Studio
* [Revision #3094](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3094)\
  Thu 2012-01-12 20:12:46 +0100
  * openpam compatibility
* [Revision #3093](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3093)\
  Thu 2012-01-12 20:12:14 +0100
  * fixes for get\_password():
    1. on windows: don't hang when there's no console, that is, \_getch() returns -1.
    2. on windows: \_getch() returns an int, not char.\
       to distinguish between (char)255 and (int)-1
    3. everywhere. isspace(pos\[-1]) == ' ' never worked,\
       isspace() returns a boolean, not a char. the never-worked loop was\
       removed to preserve the existing behavior.
* [Revision #3092](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3092)\
  Fri 2011-12-30 13:57:03 +0100
  * plugin renamed socket\_peercred -> unix\_socket.
  * test added.
* [Revision #3091](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3091)\
  Thu 2011-12-29 22:52:13 +0100
  * on windows: don't link all plugins with mysqld, only do it for storage engines.
* [Revision #3090](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3090)\
  Sat 2012-01-14 00:02:02 -0800
  * Back-ported the test case for bug #12616253 from mariadb-5.3 that\
    was actually a duplicate of [Bug #888456](https://bugs.launchpad.net/bugs/888456) fixed in mariadb-5.2.
* [Revision #3089](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3089)\
  Fri 2012-01-13 19:00:50 -0800
  * Back-ported the fix and the test case for [MySQL Bug #50257](https://bugs.mysql.com/bug.php?id=50257) from mariadb-5.3 code line.
  * Adjusted results for a few test cases.
* [Revision #3088](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3088)\
  Fri 2012-01-13 12:23:19 -0800
  * Back-ported the test cases for bug #12763207 from mysql-5.6 code line into 5.2
  * Completed the fix for this bug.
  * Note: in 5.3 the affected 'if' statement in Item\_in\_subselect::single\_value\_transformer()\
    starting with the condition (thd->variables.sql\_mode & MODE\_ONLY\_FULL\_GROUP\_BY)\
    should be removed altogether. The change from table.cc is not needed either.
  * This is because in 5.3
    * min/max transformation for subqueries are done at the optimization phase
    * evaluation of the expensive subqueries is done at the execution phase.
  * Added an EXPLAIN EXTENDED to the test case for bug #12329653.
* [Revision #3087](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3087)\
  Tue 2012-01-10 19:26:47 +0100
  * [MDEV-50](https://jira.mariadb.org/browse/MDEV-50) : Fix default compilation comment
* [Revision #3086](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3086)\
  Tue 2012-01-10 19:23:00 +0100
  * Fix [MDEV-49](https://jira.mariadb.org/browse/MDEV-49) : version\_compile\_machine server variable is 'unknown' for x64 builds
* [Revision #3085](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3085)\
  Sun 2012-01-08 20:29:05 +0200
  * Fixed compiler and test failures found by buildbot
* [Revision #3084](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3084) \[merge]\
  Sat 2012-01-07 14:59:03 +0200
  * Merge
  * [Revision #3082.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3082.1.1)\
    Sat 2012-01-07 10:23:46 +0200
    * Fixed wrong merge
* [Revision #3083](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3083)\
  Thu 2012-01-05 11:06:52 +0200
  * Fix of [Bug #793589](https://bugs.launchpad.net/bugs/793589) Wrong result with double ORDER BY
  * Problem was in caching 'eq\_ref' dependency between calls of remove\_const() for ORDER BY and GROUP BY lists.
* [Revision #3082](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3082) \[merge]\
  Wed 2012-01-04 17:22:06 +0200
  * Merge with 5.1
  * [Revision #2643.127.68](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.68)\
    Thu 2011-12-29 21:55:17 -0800
  * Fixed [Bug #848652](https://bugs.launchpad.net/bugs/848652).
  * The cause of this bug was the same as for [Bug #902356](https://bugs.launchpad.net/bugs/902356) fixed for 5.3.
  * [Revision #2643.127.67](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.67)\
    Wed 2011-12-21 13:23:15 +0200
    * Fixes [Bug #907049](https://bugs.launchpad.net/bugs/907049) "Server started with skip-aria crashes on an attempt to connect to it"
* [Revision #3081](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3081)\
  Mon 2012-01-02 23:52:31 +0100
  * Fix embedded/windows tests- move COND\_manager and LOCK\_manager to sql\_manager.cc, to prevent race condition that results into accessing already destroyed critical section
* [Revision #3080](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3080)\
  Thu 2011-12-29 15:09:20 -0800
  * Fixed [Bug #806057](https://bugs.launchpad.net/bugs/806057).
    * A table expression with a natural join or a USING clause is transformed\
      into an equivalent expression with equi-join ON conditions. If a reference\
      to a virtual column happened to occur only in these generated equi-join\
      conditions then it was not erroneously marked in the TABLE::vcol\_set bitmap.
    * This could lead to wrong results for queries containing natural join\
      expressions or USING clauses.
* [Revision #3079](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3079)\
  Wed 2011-12-28 18:47:01 -0800
  * Fixed [Bug #777654](https://bugs.launchpad.net/bugs/777654).
  * The method Item\_sum\_num::fix\_fields() calculated the value of\
    the flag Item\_sum\_num::maybe\_null in some cases incorrectly.
* [Revision #3078](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3078)\
  Tue 2011-12-27 19:13:53 -0800
  * Fixed [Bug #879860](https://bugs.launchpad.net/bugs/879860).
  * The MIN/MAX optimization cannot be applied to a subquery if its WHERE clause\
    contains a conjunctive condition depending on an outer reference.
* [Revision #3077](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3077)\
  Tue 2011-12-27 13:19:13 -0800
  * Fixed [Bug #904345](https://bugs.launchpad.net/bugs/904345).
  * The MIN/MAX optimizer code from the function opt\_sum\_query erroneously\
    did not take into account conjunctive conditions that did not depend on\
    any table, yet were not identified as constant items. These could be\
    items containing rand() or PS/SP parameters. These items are supposed\
    to be evaluated at the execution phase. That's why if such conditions\
    can be extracted from the WHERE condition the MIN/MAX optimization is\
    not applied as currently it is always done at the optimization phase.
  * (In 5.3 expensive subqueries are also evaluated only at the execution\
    phase. So, if a constant condition with such subquery can be extracted\
    from the WHERE clause the MIN/MAX optimization should not be applied\
    in 5.3.)
  * IF an IN/ALL/SOME predicate with a constant left part is transformed\
    into an EXISTS subquery the resulting subquery should not be considered\
    uncacheable if the right part of the predicate is not uncacheable.
  * Backported the function dbug\_print\_item() from 5.3. The function is used\
    only for debugging.
* [Revision #3076](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3076) \[merge]\
  Fri 2011-12-23 15:02:57 +0100
  * merge
  * [Revision #3075.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3075.1.1)\
    Thu 2011-12-22 15:50:33 +0100
    * [Bug #906638](https://bugs.launchpad.net/bugs/906638) : Fixes to build oqgraph with boost 1.48
      * dijkstra\_shortest\_paths() needs a Graph as first parameter, in case of reverse\_graph we now need to use\
        its m\_g member
      * use boost::tuples::tie() on all places where tie() was used . Reason -\
        fix the build with Visual Studio 10 SP1 (which includes std:tr1:tie, thus creating ambiguity)
* [Revision #3075](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3075)\
  Thu 2011-12-22 11:07:04 +0100
  * compilation warning - unused variable
* [Revision #3074](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3074)\
  Wed 2011-12-21 12:45:53 +0200
  * Supression condition made wider to cover some other system cases.
* [Revision #3073](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3073)\
  Tue 2011-12-20 01:56:41 -0800
  * Fixed [Bug #794005](https://bugs.launchpad.net/bugs/794005).
  * The function st\_table::mark\_virtual\_columns\_for\_write() did not take into\
    account the fact that for any table the value of st\_table::vfield is 0\
    when there are no virtual columns in the table definition.
* [Revision #3072](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3072)\
  Mon 2011-12-19 14:55:30 -0800
  * Fixed [Bug #906322](https://bugs.launchpad.net/bugs/906322).
  * If the sorted table belongs to a dependent subquery then the function\
    create\_sort\_index() should not clear TABLE:: select and TABLE::select\
    for this table after the sort of the table has been performed, because\
    these members are needed for the second execution of the subquery.
* [Revision #3071](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3071) \[merge]\
  Tue 2011-12-13 20:08:41 +0200
  * Merge with 5.1
  * Updated version number in configure
  * [Revision #2643.127.66](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.66)\
    Mon 2011-12-12 16:28:16 +0100
    * new "`./configure --disable-distribution`" option
  * [Revision #2643.127.65](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.65)\
    Mon 2011-12-12 13:37:18 +0100
    * Fix GCC build failure in PBXT in some cases/platforms.
  * [Revision #2643.127.64](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.64)\
    Sun 2011-12-11 22:58:01 +0200
    * Fixed valgrind problem: reference on deleted memory of temporary table name.
    * Removed previous patch of this problem.
* [Revision #3070](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3070)\
  Tue 2011-12-13 19:57:19 +0200
  * Fixed [Bug #887051](https://bugs.launchpad.net/bugs/887051) ; Error in recovery with LOAD DATA + DELETE
* [Revision #3069](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3069)\
  Mon 2011-12-12 12:36:46 +0200
  * Fixed [Bug #900375](https://bugs.launchpad.net/bugs/900375)
  * The range optimizer incorrectly chose a loose scan for group by\
    when there is a correlated WHERE condition. This range access\
    method cannot be executed for correlated conditions also with the\
    "range checked for each record" because generally the range access\
    method can change for each outer record. Loose scan destructively\
    changes the query plan and removes the GROUP operation, which will\
    result in wrong query plans if another range access is chosen\
    dynamically.
* [Revision #3068](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/3068)\
  Thu 2011-12-08 12:05:52 +0200
  * Fixed [Bug #888456](https://bugs.launchpad.net/bugs/888456)
  * Analysis:
    * The class member QUICK\_GROUP\_MIN\_MAX\_SELECT::seen\_first\_key\
      was not reset between subquery re-executions. Thus each\
      subsequent execution continued from the group that was\
      reached by the previous subquery execution. As a result\
      loose scan reached end of file much earlier, and returned\
      empty result where it shouldn't.
  * Solution:
    * Reset seen\_first\_key before each re-execution of the\
      loose scan.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
