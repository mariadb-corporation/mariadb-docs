# MariaDB 5.2.10 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.2.10) |[Release Notes](../../old-releases/5.2/5.2.10.md) |**Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 5 Dec 2011

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.10.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3067](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3067)\
  Sat 2011-12-03 22:44:33 +0100
  * updated the version in configure
* [Revision #3066](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3066)\
  Fri 2011-12-02 16:27:13 +0100
  * PAM plugin with test
* [Revision #3065](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3065)\
  Fri 2011-12-02 16:26:43 +0100
  1. add `--plugin-dir` and `--default-auth` to mysqltest.
  2. dialog plugin now always returns mysql->password if non-empty and the first question is of password type
  3. split get\_tty\_password into get\_tty\_password\_buff and strdup.
  4. dialog plugin now uses get\_tty\_password by default
  5. dialog.test
  6. moved small tests of individual plugins into a dedicated suite
* [Revision #3064](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3064)\
  Sat 2011-12-03 10:53:00 +0100
  * update tests
* [Revision #3063](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3063) \[merge]\
  Sat 2011-12-03 20:47:25 +0200
  * Merge with 5.1
  * [Revision #2643.127.63](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.63)\
    Sat 2011-12-03 20:29:15 +0200
    * Added suppressions
    * Fixed feedback\_plugin\_send to not generate a random number of lines.
  * [Revision #2643.127.62](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.62) \[merge]\
    Thu 2011-12-01 19:20:57 +0100
    * merge
    * [Revision #2643.134.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.134.2) \[merge]\
      Thu 2011-12-01 19:18:45 +0100
      * merge
      * [Revision #2643.134.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.134.1)\
        Thu 2011-12-01 19:15:09 +0100
        * Fix main.merge testcase on Windows
* [Revision #3062](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3062)\
  Sat 2011-12-03 20:44:54 +0200
  * Fixed buildbot warnings
* [Revision #3061](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3061)\
  Fri 2011-12-02 18:10:54 +0200
  * Fixed some Aria limits to be more sane
* [Revision #3060](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3060) \[merge]\
  Fri 2011-12-02 17:32:56 +0200
  * Merge
  * [Revision #3058.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3058.1.1)\
    Fri 2011-12-02 17:22:17 +0200
    * Fixed bug where automaticly zerofilled table was not part of recovery if crash happended before next checkpoint.
* [Revision #3059](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3059)\
  Thu 2011-12-01 22:37:45 +0100
  * Fix intermittently failing variables-notembedded test case.\
    After sending packet that is too large, clienrt can get either an error packet with\
    ER\_NET\_PACKET\_TOO\_LARGE, or a socket error. Both cases are valid, since the\
    server does not ensure reply was fully read by client, before shutting down and closing\
    the socket.
* [Revision #3058](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3058)\
  Thu 2011-12-01 20:21:11 +0200
  * Fixed compiler warning
* [Revision #3057](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3057) \[merge]\
  Thu 2011-12-01 20:14:53 +0200
  * Merge with 5.1
  * [Revision #2643.127.61](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.61)\
    Thu 2011-12-01 20:11:41 +0200
    * Fixed that `--with-libedit --without-readline` works
    * Fixed buildbot failures (compiler warnings, failing tests)
* [Revision #3056](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3056) \[merge]\
  Wed 2011-11-30 22:57:18 +0200
  * Merge with 5.1
  * [Revision #2643.127.60](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.60)\
    Wed 2011-11-30 20:57:09 +0200
    * Fixed compiler warning and errors
  * [Revision #2643.127.59](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.59)\
    Wed 2011-11-30 18:44:51 +0200
    * Fixed compiler warnings and other bugs found by buildbot.
  * [Revision #2643.127.58](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.58)\
    Wed 2011-11-30 11:37:28 +0100
    * test both federated and federatedX in the federated suite.
  * [Revision #2643.127.57](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.57)\
    Wed 2011-11-30 13:53:25 +0100
    * Cherrypick into XtraDB: bug#13002783 PARTIALLY UNINITIALIZED CASCADE UPDATE VECTOR
    * We merged the test case for this into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md), but the fix was not yet part of XtraDB.
* [Revision #2643.127.56](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.56)\
  Wed 2011-11-30 00:34:05 +0200
  * Fixed compiler warnings
* [Revision #3055](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3055) \[merge]\
  Tue 2011-11-29 22:48:24 +0200
  * Merge with 5.1 + fixes for build failures in 5.2
  * [Revision #2643.127.55](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.55)\
    Tue 2011-11-29 15:32:25 +0200
    * Fixed that maria-recover works as expected.
    * "" is now used if no option is set
  * [Revision #2643.127.54](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.54)\
    Tue 2011-11-29 01:10:17 +0100
    * Fix Windows build, and a conversion truncation warning.
  * [Revision #2643.127.53](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.53)\
    Thu 2011-11-24 19:23:20 +0200
    * Fixed that one can use --maria-recover=backup,force\
      (Before we only allowed one option)
* [Revision #3054](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3054)\
  Tue 2011-11-29 08:50:54 +0100
  * Fix testcases:
    1. main.merge fails with errno 13 in copy\_file().
    2. The reason for the error is that copy\_file tries to create a file with the same name as recently deleted one,\
       and there is still an open handle for the deleted file.\
       To fix, use my\_delete\_allow\_opened() for MTR's delete\_file. On Windows, this renames file to unique name\
       prior to deletion, and prevents EACCES errors for files opened with FILE\_SHARE\_DELETE.
    3. innodb\_bug59641
    4. generates warnings, after server was killed and restarted in the test case.
    5. The warnings are about test\_suppression table (needs to be repaired, as it that was written just prior to the crash)
    6. Fixed by using FLUSH TABLES after populating warning suppression table.
* [Revision #3053](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3053)\
  Tue 2011-11-29 02:00:24 +0100
  * merge, fix Windows warnings
* [Revision #3052](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3052)\
  Mon 2011-11-28 15:08:12 +0100
  * after merge fixes
* [Revision #3051](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3051) \[merge]\
  Thu 2011-11-24 22:48:35 +0200
  * Automatic merge
  * [Revision #3042.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3042.1.2)\
    Thu 2011-11-24 19:07:36 +0200
    * Added test case for [Bug #875797](https://bugs.launchpad.net/bugs/875797) Using 'innodb\_sys\_indexes' causes core dump
  * [Revision #3042.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3042.1.1) \[merge]\
    Thu 2011-11-24 18:48:58 +0200
    * Merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
    * [Revision #2643.127.52](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.52)\
      Thu 2011-11-24 16:04:19 +0200
      * Fixes for build failuers found by buildbot
    * [Revision #2643.127.51](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.51) \[merge]\
      Wed 2011-11-23 19:32:14 +0200
      * Merge with MySQL 5.1.60
    * [Revision #2643.127.50](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.50)\
      Wed 2011-11-23 10:25:27 +0200
      * Fixes of testcases after merge with MySQL 5.1.59
    * [Revision #2643.127.49](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.49) \[merge]\
      Mon 2011-11-21 19:19:37 +0200
      * Merge of XtraDB for 5.1.59
      * [Revision #2643.133.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.133.1) \[merge]\
        Mon 2011-11-21 14:21:13 +0100
        * Merge XtraDB from Percona-Server-5.1.59-13 into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md).
        * [Revision #0.6.47](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/0.6.47)\
          Mon 2011-11-21 13:20:15 +0100
          * Updated with changes from Percona Server 5.1.56-13, from
          * lp`:`percona-server/5.1, tag Percona-Server-5.1.59-13.0.
          * Merged: revid:ignacio.nin@percona.com-20111016133841-fzpr5s89n13ft1s1
    * [Revision #2643.127.48](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.48) \[merge]\
      Mon 2011-11-21 19:17:56 +0200
      * Automatic merge
      * [Revision #2643.132.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.132.1) \[merge]\
        Mon 2011-11-21 19:13:14 +0200
        * Initail merge with MySQL 5.1 (XtraDB still needs to be merged)
        * Fixed up copyright messages.
* [Revision #3050](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3050)\
  Tue 2011-11-22 21:55:11 +0100
  * fix dialog plugin to work on windows
* [Revision #3049](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3049)\
  Tue 2011-11-15 13:14:54 +0200
  * Fix for [Bug #780425](https://bugs.launchpad.net/bugs/780425) sql\_buffer\_result=1 gives wrong result for GROUP BY with a +

## constant expression"

* [Revision #3048](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3048) \[merge]\
  Sun 2011-11-13 18:41:45 +0100
  * 5.1->5.2 merge
  * [Revision #2643.127.47](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.47)\
    Sun 2011-11-13 13:28:35 +0100
    * don't make feedback\_plugin\_send.test as 'big'
    * don't assume that the http reply packet will arrive in all in one piece
* [Revision #3047](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3047) \[merge]\
  Sun 2011-11-13 08:30:03 +0100
  * 5.1-5.2 merge
  * [Revision #2643.127.46](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.46)\
    Sat 2011-11-12 18:40:51 +0100
    * increase feedback plugin version
* [Revision #3046](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3046) \[merge]\
  Sat 2011-11-12 16:47:14 +0100
  * 5.1 merge
  * [Revision #2643.127.45](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.45)\
    Sat 2011-11-12 16:41:00 +0100
    * feedback plugin:
      * fix for mem\_total on windows
      * report the time of the data snapshot
  * [Revision #2643.127.44](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.44)\
    Tue 2011-11-08 23:07:19 +0100
    * typos fixed
    * (thanks viva64.com)
* [Revision #3045](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3045) \[merge]\
  Fri 2011-11-04 12:41:27 +0200
  * Merge of gcc 4.6 fixes
  * [Revision #3043.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3043.1.2)\
    Thu 2011-10-27 19:18:25 +0300
    * Fix gcc 4.6 warning after merge with 5.1
  * [Revision #3043.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3043.1.1) \[merge]\
    Thu 2011-10-27 17:51:30 +0300
    * 5.1->5.2 merge (gcc 4.6 warnings and apple hwaddress fixes).
    * [Revision #2643.127.43](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.43)\
      Thu 2011-10-27 15:22:52 +0300
      * Fix gcc 4.6 warnings about assigned but not used variables.
      * Fixed my\_gethwaddr.c to allow compilation on Mac OS X.
* [Revision #3044](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3044)\
  Tue 2011-11-01 12:36:43 +0400
  * [Bug #884184](https://bugs.launchpad.net/bugs/884184): Wrong result with RIGHT JOIN + derived\_merge
    *   Make eliminate\_tables\_for\_list() take into account that it is not possible\
        to eliminate a table if it is used in the upper-side ON expressions.\
        Example:

        ```
        xxx JOIN (t1 LEFT JOIN t2 ON cond ) ON func(t2.columns)
        ```
    * Here it would eliminate t2 which is not possible because of use of t2.columns.
* [Revision #3043](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3043) \[merge]\
  Wed 2011-10-19 20:53:16 +0200
  * merge from 5.1
  * [Revision #2643.127.42](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.42)\
    Wed 2011-10-19 20:51:01 +0200
    * Fix endless loop in my\_gethwaddr()
  * [Revision #2643.127.41](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.41)\
    Thu 2011-10-13 11:20:33 +0200
    * silence the "uninitialized" warning
* [Revision #3042](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3042)\
  Sun 2011-10-16 21:55:53 +0300
  * Fixed wrong info message for mysqld `--general-log`
  * Fixed wrong parameter type for `--general-log`. Now one can enable it with `--general-log= 1 | true | on`
  * Fixed that bool parameters can also take 'on' and 'off' as parameters. This is in line with the values assigned to them in mysqld.
* [Revision #3041](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3041)\
  Wed 2011-10-12 12:07:14 +0200
  * Add option to enable feedback plugin to the MSI installer.
* [Revision #3040](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3040) \[merge]\
  Tue 2011-10-11 20:16:11 +0200
  * merge
  * [Revision #2643.127.40](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.40)\
    Tue 2011-10-11 20:13:57 +0200
    * remove unconditional SAFEMALLOC/SAFEMUTEX from debug flags
* [Revision #3039](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3039) \[merge]\
  Mon 2011-10-10 19:34:37 +0200
  * merge
  * [Revision #2643.127.39](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.39)\
    Mon 2011-10-10 17:59:26 +0200
    * add a missing definition
* [Revision #3038](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3038)\
  Sat 2011-10-08 19:00:00 +0200
  * fix feedback plugin for 5.2
* [Revision #3037](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3037) \[merge]\
  Fri 2011-10-07 00:18:30 +0200
  * merge with 5.1
  * [Revision #2643.127.38](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.38)\
    Thu 2011-10-06 23:40:19 +0200
    * sort results in tests to make them stable
  * [Revision #2643.127.37](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.37)\
    Thu 2011-10-06 23:39:44 +0200
    * disable feedback plugin by default. Now on windows too.
  * [Revision #2643.127.36](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.36) \[merge]\
    Thu 2011-10-06 21:42:43 +0200
    * merge the feedback tree
    * [Revision #2643.131.8](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.131.8)\
      Thu 2011-10-06 20:55:38 +0200
      * Implement uname() on Windows.
      * Also, fix code to get physical memory size.
    * [Revision #2643.131.7](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.131.7) \[merge]\
      Thu 2011-10-06 18:48:16 +0200
      * merge with feedback-plugin
      * and disable feedback plugin by default, if it's compiled in.
      * [Revision #0.13.4](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/0.13.4)\
        Thu 2011-10-06 18:24:00 +0200
        * add `#define WITH_FEEDBACK_PLUGIN`
    * [Revision #2643.131.6](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.131.6)\
      Wed 2011-10-05 20:16:42 +0200
      * fix fulltext\_plugin.test on windows
    * [Revision #2643.131.5](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.131.5)\
      Tue 2011-10-04 16:51:39 +0200
      * tests for feedback plugin,
      * bugfix: garbage in PLUGIN\_VAR\_STR variables when INSTALL'ing a plugin
    * [Revision #2643.131.4](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.131.4) \[merge]\
      Tue 2011-10-04 16:03:10 +0200
      * merge feedback plugin
      * [Revision #0.13.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/0.13.3)\
        Tue 2011-10-04 15:48:39 +0200
        * fix for static plugins in mariadb.
        * send "startup" message 5 minutes after startup, not immediately
      * [Revision #0.13.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/0.13.2)\
        Mon 2011-10-03 08:43:01 +0200
        * don't use https url by default, if ssl is not available
      * [Revision #0.13.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/0.13.1)\
        Sat 2011-10-01 21:23:01 +0200
        * initial checkin
    * [Revision #2643.131.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.131.3)\
      Tue 2011-10-04 15:41:52 +0200
      * support for plugins on windows
    * [Revision #2643.131.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.131.2)\
      Tue 2011-10-04 15:07:55 +0200
      * my\_gethwaddr() on Solaris and Windows
    * [Revision #2643.131.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.131.1)\
      Tue 2011-10-04 15:01:26 +0200
      * remove redundant declarations
* [Revision #3036](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3036)\
  Thu 2011-10-06 16:56:59 +0300
  * Fixed that when using a trigger mysql.proc is now accessed\
    Cleanup: Changed procedure type from a int/char to an enum for easier to manage and debug code.
* [Revision #3035](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3035) \[merge]\
  Wed 2011-10-05 16:53:35 +0300
  * Automatic merge with 5.1
  * [Revision #2643.127.35](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/2643.127.35)\
    Wed 2011-10-05 16:37:05 +0300
    * Fix for issue found in buildbot where mysqld.\*.err files was missing
    * Added suppression message for valgrind failure found on OpenSuSE 11.1
* [Revision #3034](https://bazaar.launchpad.net/~maria-captains/maria/5.2-release/revision/3034)\
  Wed 2011-10-05 15:59:49 +0300
  * Fixed [Bug #859051](https://bugs.launchpad.net/bugs/859051) "Periodic aria checkpoints prevent power management"
  * Now the aria\_log\_control\_file and log file is not touched if aria files are not written to.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
