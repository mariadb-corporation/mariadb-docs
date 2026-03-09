# MariaDB 5.1.60 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.1.60) |[Release Notes](../../old-releases/5.1/5.1.60.md) |**Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 5 Dec 2011

For the highlights of this release, see the [release notes](../../old-releases/5.1/5.1.60.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3120](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3120)\
  Sat 2011-12-03 20:29:15 +0200
  * Added suppressions
  * Fixed feedback\_plugin\_send to not generate a random number of lines.
* [Revision #3119](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3119) \[merge]\
  Thu 2011-12-01 19:20:57 +0100
  * merge
  * [Revision #3117.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3117.1.2) \[
    * merge]\
      Thu 2011-12-01 19:18:45 +0100
    * merge
  * [Revision #3117.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3117.1.1)\
    Thu 2011-12-01 19:15:09 +0100
    * Fix main.merge testcase on Windows
* [Revision #3118](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3118)\
  Thu 2011-12-01 20:11:41 +0200
  * Fixed that `--with-libedit --without-readline` works
  * Fixed buildbot failures (compiler warnings, failing tests)
* [Revision #3117](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3117)\
  Wed 2011-11-30 20:57:09 +0200
  * Fixed compiler warning and errors
* [Revision #3116](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3116)\
  Wed 2011-11-30 18:44:51 +0200
  * Fixed compiler warnings and other bugs found by buildbot.
* [Revision #3115](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3115)\
  Wed 2011-11-30 11:37:28 +0100
  * test both federated and federatedX in the federated suite.
* [Revision #3114](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3114)\
  Wed 2011-11-30 13:53:25 +0100
  * Cherrypick into XtraDB: Bug#13002783 PARTIALLY UNINITIALIZED CASCADE UPDATE VECTOR
  * We merged the test case for this into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md), but the fix\
    was not yet part of XtraDB.
* [Revision #3113](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3113)\
  Wed 2011-11-30 00:34:05 +0200
  * Fixed compiler warnings
* [Revision #3112](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3112)\
  Tue 2011-11-29 15:32:25 +0200
  * Fixed that maria-recover works as expected.
    * "" is now used if no option is set
* [Revision #3111](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3111)\
  Tue 2011-11-29 01:10:17 +0100
  * Fix Windows build, and a conversion truncation warning.
* [Revision #3110](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3110)\
  Thu 2011-11-24 19:23:20 +0200
  * Fixed that one can use `--maria-recover=backup,force`
  * (Before we only allowed one option)
* [Revision #3109](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3109)\
  Thu 2011-11-24 16:04:19 +0200
  * Fixes for build failuers found by buildbot
* [Revision #3108](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3108) \[merge]\
  Wed 2011-11-23 19:32:14 +0200
  * Merge with MySQL 5.1.60
* [Revision #3107](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3107)\
  Wed 2011-11-23 10:25:27 +0200
  * Fixes of testcases after merge with MySQL 5.1.59
* [Revision #3106](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3106) \[merge]\
  Mon 2011-11-21 19:19:37 +0200
  * Merge of XtraDB for 5.1.59
  * [Revision #3104.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3104.1.1) \[merge]\
    Mon 2011-11-21 14:21:13 +0100
    * Merge XtraDB from Percona-Server-5.1.59-13 into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md).
    * [Revision #0.6.47](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/0.6.47)\
      mp: Mon 2011-11-21 13:20:15 +0100
      * Updated with changes from Percona Server 5.1.56-13, from
      * lp`:`percona-server/5.1, tag Percona-Server-5.1.59-13.0.
      * Merged: revid:ignacio.nin@percona.com-20111016133841-fzpr5s89n13ft1s1
* [Revision #3105](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3105) \[merge]\
  Mon 2011-11-21 19:17:56 +0200
  * Automatic merge
  * [Revision #3101.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3101.1.1) \[merge]\
    Mon 2011-11-21 19:13:14 +0200
    * Initial merge with MySQL 5.1 (XtraDB still needs to be merged)
    * Fixed up copyright messages.
* [Revision #3104](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3104)\
  Sun 2011-11-13 13:28:35 +0100
  * don't make feedback\_plugin\_send.test as 'big'
  * don't assume that the http reply packet will arrive in all in one piece
* [Revision #3103](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3103)\
  Sat 2011-11-12 18:40:51 +0100
  * increase feedback plugin version
* [Revision #3102](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3102)\
  Sat 2011-11-12 16:41:00 +0100
  * feedback plugin:
  * fix for mem\_total on windows
  * report the time of the data snapshot
* [Revision #3101](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3101)\
  Tue 2011-11-08 23:07:19 +0100
  * typos fixed
  * (thanks viva64.com)
* [Revision #3100](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3100)\
  Thu 2011-10-27 15:22:52 +0300
  * Fix gcc 4.6 warnings about assigned but not used variables.
  * Fixed my\_gethwaddr.c to allow compilation on Mac OS X.
* [Revision #3099](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3099)\
  Wed 2011-10-19 20:51:01 +0200
  * Fix endless loop in my\_gethwaddr()
* [Revision #3098](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3098)\
  Thu 2011-10-13 11:20:33 +0200
  * silence the "uninitialized" warning
* [Revision #3097](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3097)\
  Tue 2011-10-11 20:13:57 +0200
  * remove unconditional SAFEMALLOC/SAFEMUTEX from debug flags
* [Revision #3096](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3096)\
  Mon 2011-10-10 17:59:26 +0200
  * add a missing definition
* [Revision #3095](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3095)\
  Thu 2011-10-06 23:40:19 +0200
  * sort results in tests to make them stable
* [Revision #3094](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3094)\
  Thu 2011-10-06 23:39:44 +0200
  * disable feedback plugin by default. Now on windows too.
* [Revision #3093](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3093) \[merge]\
  Thu 2011-10-06 21:42:43 +0200
  * merge the feedback tree
  * [Revision #3091.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091.1.8)\
    Thu 2011-10-06 20:55:38 +0200
    * Implement uname() on Windows.
    * Also, fix code to get physical memory size.
  * [Revision #3091.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091.1.7) \[merge]\
    Thu 2011-10-06 18:48:16 +0200
    * merge with feedback-plugin
    * and disable feedback plugin by default, if it's compiled in.
    * [Revision #0.13.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/0.13.4)\
      mp: Thu 2011-10-06 18:24:00 +0200
      * add #define WITH\_FEEDBACK\_PLUGIN
  * [Revision #3091.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091.1.6)\
    Wed 2011-10-05 20:16:42 +0200
    * fix fulltext\_plugin.test on windows
  * [Revision #3091.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091.1.5)\
    Tue 2011-10-04 16:51:39 +0200
    * tests for feedback plugin,
    * bugfix: garbage in PLUGIN\_VAR\_STR variables when INSTALL'ing a plugin
  * [Revision #3091.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091.1.4) \[merge]\
    Tue 2011-10-04 16:03:10 +0200
    * merge feedback plugin
    * [Revision #0.13.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/0.13.3)\
      mp: Tue 2011-10-04 15:48:39 +0200
      * fix for static plugins in mariadb.
      * send "startup" message 5 minutes after startup, not immediately
    * [Revision #0.13.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/0.13.2)\
      mp: Mon 2011-10-03 08:43:01 +0200
      * don't use https url by default, if ssl is not available
    * [Revision #0.13.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/0.13.1)\
      mp: Sat 2011-10-01 21:23:01 +0200
      * initial checkin
  * [Revision #3091.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091.1.3)\
    Tue 2011-10-04 15:41:52 +0200
    * support for plugins on windows
  * [Revision #3091.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091.1.2)\
    Tue 2011-10-04 15:07:55 +0200
    * my\_gethwaddr() on Solaris and Windows
  * [Revision #3091.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091.1.1)\
    Tue 2011-10-04 15:01:26 +0200
    * remove redundant declarations
* [Revision #3092](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3092)\
  Wed 2011-10-05 16:37:05 +0300
  * Fix for issue found in buildbot where mysqld.\*.err files was missing
  * Added suppression message for valgrind failure found on OpenSuSE 11.1
* [Revision #3091](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3091)\
  Mon 2011-08-15 20:38:21 +0300
  * Fixed [Bug #826377](https://bugs.launchpad.net/bugs/826377) "Aria DB Format: Reading specific table from dump causes Wrong bytesec"
  * The bug was that when using bulk insert combined with lock table, we intitalized the io cache with the wrong file position.
  * This fixed a bug where MariaDB could not read in a table dump done with mysqldump.
* [Revision #3090](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3090)\
  Fri 2011-08-12 15:40:56 +0300
  * Fixed [Bug #814231](https://bugs.launchpad.net/bugs/814231) Aria post-recovery error "Bitmap at page 0 has pages reserved outside of data file length"
  * The bug was a wrong check in aria\_chk; The table was fine.
* [Revision #3089](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3089)\
  Sun 2011-07-31 22:25:37 +0200
  * Speed up mysql-test-run.pl.
  * Problem was the parsing of test suite files for various tags and options.
  * This was done inefficiently, and include files were re-parsed for every\
    place they were included. This caused a delay of 20 seconds or so before\
    the first test started to run.
  * By parsing more efficiently and re-using first parse for subsequent\
    inclusion of the same file, time spent parsing is reduced to less than\
    1 second, and start appears instantaneous.
  * (With this patch, full ./mtr runs in 3 minutes on my laptop (release\
    build.)
* [Revision #3088](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3088)\
  Sun 2011-07-24 01:27:48 -0700
  * Ensure that the last `--datadir` option is used from the my.cnf files.
* [Revision #3087](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3087)\
  Sun 2011-07-24 01:25:28 -0700
  * Fixes [Bug #805930](https://bugs.launchpad.net/bugs/805930) Sysbench breaks on multiple table test with [MariaDB 5.2.7](../../old-releases/5.2/5.2.7.md) + Aria
  * The bug happens when one uses MAX\_ROWS=

## with Aria & row\_format=page and one insert more than

## rows.

* [Revision #3086](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3086)\
  Thu 2011-07-21 18:32:44 +0300
  * test fix.
* [Revision #3085](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3085)\
  Thu 2011-07-21 15:14:16 +0300
  * Fixed PBXT test.
* [Revision #3084](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3084)\
  Thu 2011-07-21 12:29:00 +0300
  * Removed incorrect fix and its test suite (the test suit is duplicate).
  * Fixed explains of previous patch.
* [Revision #3083](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3083)\
  Thu 2011-07-21 11:45:19 +0300
  * The function description added.
* [Revision #3082](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3082)\
  Thu 2011-07-21 11:20:55 +0300
  * Fix of [Bug #777809](https://bugs.launchpad.net/bugs/777809)
  * There are 2 volatile condition constructions AND/OR constructions and fields(references) when first\
    good supported to be top elements of conditions because it is normal practice\
    (see copy\_andor\_structure for example) fields without any expression in the condition is really rare\
    and mostly useless case however it could lead to problems when optimiser changes/moves them unaware\
    of other variables referring to them. An easy solution of this problem is just to replace single field\
    in a condition with equivalent expression well supported by the server ( -> != 0).
* [Revision #3081](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3081)\
  Tue 2011-07-12 08:58:33 +0200
  * bugfix: create internal temporary tables in mysql\_tmpdir, not in datadir
* [Revision #3080](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3080)\
  Sun 2011-07-10 13:38:15 +0200
  * Post-fix for [Bug #808233](https://bugs.launchpad.net/bugs/808233) : replace uint with "unsigned int" in mysql.h.pp, too
* [Revision #3079](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3079) \[merge]\
  Sun 2011-07-10 12:33:08 +0200
  * merge
  * [Revision #3067.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3067.1.4) \[
    * merge]\
      Sun 2011-07-10 12:31:09 +0200
    * merge
  * [Revision #3067.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3067.1.3)\
    Sun 2011-07-10 12:27:42 +0200
    * [Bug #808233](https://bugs.launchpad.net/bugs/808233): Undefined uint in typelib.h
    * Fix is to replace uint in public header with unsigned int. uint is not\
      guaranteed to be defined by system headers.
* [Revision #3078](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3078)\
  Thu 2011-07-07 22:37:38 +0200
  * protocol safety fix:
    * before strlen(db) we need to be sure that
    * db lies within packet boundaries
* [Revision #3077](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3077)\
  Fri 2011-06-24 10:56:29 +0300
  * Fixed typo. (Old code worked as both tested parts where 'bool', but not nice code..)
* [Revision #3076](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3076)\
  Fri 2011-06-24 10:10:50 +0300
  * Fixes to aria
    * Fixed error when writing a blob to the last page on the bitmap.
    * Marked bitmap changed in once case that could cause two rows to use the same blob page.
* [Revision #3075](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3075)\
  Fri 2011-06-24 10:08:09 +0300
  * Fix for [Bug #798597](https://bugs.launchpad.net/bugs/798597) Incorrect "Duplicate entry" error with views and GROUP BY
* [Revision #3074](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3074)\
  Tue 2011-06-21 17:40:51 +0200
  * [Bug #790513](https://bugs.launchpad.net/bugs/790513) MariaDB crashes on startup
  * initialize plugins earlier, to support, for example, non-MyISAM mysql.plugin table.
* [Revision #3073](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3073)\
  Wed 2011-06-15 20:30:10 +0200
  * `./mtr --suite funcs_1 --ps-protocol`
* [Revision #3072](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3072)\
  Wed 2011-06-15 19:44:00 +0200
  * fix "`./configure --with-debug`" builds
  * (without CFLAGS=-DSAFEMALLOC).
* [Revision #3071](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3071)\
  Thu 2011-05-26 14:38:17 +0300
  * Disable call to setpriority() in pbxt. This caused mysqld to run with nice\
    priority -19, which was far from optimal.
* [Revision #3070](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3070)\
  Wed 2011-05-18 15:15:36 +0200
  * Fix mysqltest printing of include stack.
  * The printing of include stack in the error case in mysqltest omitted the\
    bottom of the stack (the line number in original test case file), and instead\
    printed the top of the stack twice. Fix to print each element on the stack\
    once and only once.
* [Revision #3069](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3069) \[merge]\
  Thu 2011-05-12 15:39:54 +0200
  * merge
  * [Revision #3067.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3067.1.2)\
    Thu 2011-05-12 15:34:02 +0200
    * Windows build : Make win\config.js optional in 5.1
    * Simplifies handling 5.1 in buildbot.
  * [Revision #3067.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3067.1.1)\
    Thu 2011-05-12 15:31:11 +0200
    * Fix check\_table\_file\_presence:
    * On Windows, do not attempt access() for special device names like\
      CON, PRN etc. access() would return 0, this does not mean that fiile\
      with this name exists.
* [Revision #3068](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3068)\
  Thu 2011-05-12 14:56:08 +0300
  * db\_name can change case, so we need copy of it for case insensitive FS.
* [Revision #3067](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3067)\
  Wed 2011-05-11 14:09:48 +0300
  * Bugfix: New table creation/renaming block added if old encoded table present.
* [Revision #3066](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3066)\
  Mon 2011-05-09 15:06:16 +0200
  * Fix buildbot failure in rpl\_stop\_slave.test.
  * Problem was setting DEBUG\_SYNC twice in a row too fast in the test case; this\
    could cause the second setting to override the first before the code had time\
    to react to the first, causing the signal to get lost.
  * Fixed by waiting for the code to receive the first signal before overwriting\
    it in the test case.
* [Revision #3065](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3065)\
  Fri 2011-05-06 14:01:51 +0300
  * Reverted unittest/unit.pl back to Test::Harness as some of our build\
    machines didn't support the new recommended TAP::Harness module
* [Revision #3064](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3064)\
  Thu 2011-05-05 23:28:42 +0300
  * Speed up pbxt.range test a bit
* [Revision #3063](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3063)\
  Thu 2011-05-05 14:51:01 +0300
  * Improved 'make test-unit' time slightly
* [Revision #3062](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3062) \[merge]\
  Wed 2011-05-04 21:56:29 +0300
  * Automatic merge
  * [Revision #3060.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3060.1.1)\
    Wed 2011-05-04 21:51:44 +0300
    * Fixed build errors on centos5-amd64-minimal, where we compile with very few character sets
    * Fixed compiler warnings
* [Revision #3061](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3061)\
  Wed 2011-05-04 21:28:02 +0300
  * Fixed build errors on centos5-amd64-minimal, where we compile with very few character sets
  * Fixed compiler warnings
* [Revision #3060](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3060) \[merge]\
  Wed 2011-05-04 16:12:39 +0200
  * merge
  * [Revision #3058.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3058.1.2)\
    Wed 2011-05-04 16:03:52 +0200
    * Cherrypick fix for maria recovery bug [Bug #686006](https://bugs.launchpad.net/bugs/686006) from 5.2\
      into 5.1
  * [Revision #3058.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3058.1.1)\
    Wed 2011-05-04 15:45:39 +0200
    * Avoid mtr warning on Windows during startup
    * The reason for mtr warning is that collect\_mysqld\_features() starts\
      mysqld with `--datadir=/tmp` and this directory does not exist on Windows.
    * Fix : instead of passing `--datadir=$opt_vardir/tmp`\
      in `collect_mysqld_features()` just\
      use `--datadir=`. mysqld does not need a correct\
      directory, just an existing one, as it is started\
      with `--help ---verbose --skip-grant-tables`.
* [Revision #3059](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3059) \[merge]\
  Wed 2011-05-04 11:59:16 +0300
  * Automatic merge
  * [Revision #3057.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3057.1.1)\
    Wed 2011-05-04 11:28:02 +0300
    * Fixed compiler warning
* [Revision #3058](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3058) \[merge]\
  Tue 2011-05-03 19:36:06 +0200
  * merge
  * [Revision #3056.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3056.1.2) \[
    * merge]\
      Tue 2011-05-03 19:32:17 +0200
    * merge
  * [Revision #3056.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3056.1.1)\
    Tue 2011-05-03 19:30:21 +0200
    * Fix warning (unused local variable)
* [Revision #3057](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3057) \[merge]\
  Tue 2011-05-03 18:27:14 +0300
  * Automatic merge
  * [Revision #3054.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3054.1.1)\
    Tue 2011-05-03 18:17:13 +0300
    * Fixed after-merge failures found by buildbot
* [Revision #3056](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3056)\
  Tue 2011-05-03 12:50:09 +0200
  * Fix Xtradb compile error on Win64 - conversion between pointers of different size
* [Revision #3055](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3055)\
  Mon 2011-05-02 23:03:26 +0200
  * Fix compile errors:
    * from xtradb merge
    * portability error in bitmap-t.c ( variable size array in non-portable)
* [Revision #3054](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3054) \[merge]\
  Mon 2011-05-02 21:42:52 +0300
  * Automatic merge
  * [Revision #3052.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3052.1.3) \[merge]\
    Mon 2011-05-02 21:41:02 +0300
    * Merge with xtradb fixes
  * [Revision #3052.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3052.1.2) \[merge]\
    Mon 2011-05-02 20:58:45 +0300
    * Merge with MySQL 5.1.57/58
    * Moved some BSD string functions from Unireg
  * [Revision #3052.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3052.1.1)\
    Thu 2011-04-28 23:58:00 +0300
    * Added calls to cleanup\_mutexes() for embedded library.
* [Revision #3053](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3053) \[merge]\
  Fri 2011-04-29 16:16:42 +0200
  * Merge XtraDB from Percona Server 5.1.56-12.7 into MariaDB-5.1.
  * [Revision #0.6.46](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/0.6.46)\
    Fri 2011-04-29 14:49:04 +0200
    * Updated with changes from Percona Server 5.1.56-12.7, from
    * lp`:`percona-dev/percona-server/release-5.1.56-12.7 percona-server-5.1.56-12.7\
      as of April 29, 2011.
    * Merged: revid:ignacio.nin@percona.com-20110427224434-e5a4kpyfwvj641q3
* [Revision #3052](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3052)\
  Tue 2011-04-12 13:49:16 +0200
  * [Bug #732124](https://bugs.launchpad.net/bugs/732124): PBXT result file updates that were forgotten when patch was pushed.
* [Revision #3051](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3051) \[merge]\
  Tue 2011-04-12 11:48:43 +0200
  * Merge fix of missing lock initialisation from Vlad:
  * "fixed the problem for the failing preload.test in pbxt suite"
  * [Revision #3050.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3050.1.1)\
    Thu 2011-04-07 18:28:52 +0200
    * fixed the preload.test pbxt bug
* [Revision #3050](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3050)\
  Wed 2011-03-09 19:45:48 +0200
  * Bug fix for [Bug #732124](https://bugs.launchpad.net/bugs/732124) union + limit returns wrong result
* [Revision #3049](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3049)\
  Tue 2011-03-08 14:55:36 +0200
  * Don't check if LAST\_IO\_Error has changed as this is not a user variable and it may change depending on timing issues between master and slave
* [Revision #3048](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3048)\
  Fri 2011-03-04 12:37:48 +0200
  * Removed wrong #ifdef that caused compile failure on Freebsd.
* [Revision #3047](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3047)\
  Tue 2011-03-01 18:03:38 +0100
  * typo (in the yassl error message) fixed
* [Revision #3046](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3046)\
  Tue 2011-03-01 16:21:27 +0200
  * Fixed for mac sed.
* [Revision #3045](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3045)\
  Tue 2011-03-01 15:31:24 +0200
  * Revoked changes from MySQL 5.1.55 merge as Sergei's code is more general
* [Revision #3044](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3044)\
  Tue 2011-03-01 15:19:25 +0200
  * Allow -Wuninitialized without -O only for gcc 4.4 and upper
* [Revision #3043](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3043)\
  Mon 2011-02-28 23:24:19 +0200
  * Get rid of compiler warnings
* [Revision #3042](https://bazaar.launchpad.net/~maria-captains/maria/5.1-release/revision/3042)\
  Mon 2011-02-28 19:47:19 +0200
  * Increase version number
  * Taged a couple of tests with `--big-test`

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
