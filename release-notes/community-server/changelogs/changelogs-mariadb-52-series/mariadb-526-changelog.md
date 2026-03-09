# MariaDB 5.2.6 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.2.6) |[Release Notes](../../old-releases/5.2/5.2.6.md) |**Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 12 May 2011

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.6.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #2967](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2967)\
  Tue 2011-05-10 18:19:11 +0200
  * small enhancement of the create table options feature:
  * no unnecessary casting from void\*, more type safety.
  * typos fixed.
* [Revision #2966](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2966)\
  Tue 2011-05-10 18:18:25 +0200
  * Fix Windows embedded warnings
* [Revision #2965](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2965)\
  Tue 2011-05-10 18:00:28 +0200
  * Cygwin-specific klugde to workaround missing TEMP/TMP variables.
* [Revision #2964](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2964) \[merge]\
  Mon 2011-05-09 15:09:40 +0200
  * Automatic merge [Mariadb 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)->5.2.
    * [Revision #2643.127.9](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.9)\
      Mon 2011-05-09 15:06:16 +0200
      * Fix buildbot failure in rpl\_stop\_slave.test.
      * Problem was setting DEBUG\_SYNC twice in a row too fast in the test case;\
        this could cause the second setting to override the first before the code\
        had time to react to the first, causing the signal to get lost.
      * Fixed by waiting for the code to receive the first signal before\
        overwriting it in the test case.
* [Revision #2963](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2963)\
  Mon 2011-05-09 15:14:04 +0300
  * Make event stop code even more robust.
  * (Test failed if we added my\_sleep(200000) in event\_queue::cond\_wait() just before pthread\_cond\_wait(); Not likely scenario but better to get that fixed too)
* [Revision #2962](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2962)\
  Mon 2011-05-09 14:38:49 +0300
  * mysqltest: Write command to be executed to the log BEFORE executing the command.
  * Fixed race condition in event that could cause hang when stopping event scheduler with SET GLOBAL event\_scheduler=OFF
* [Revision #2961](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2961) \[merge]\
  Sun 2011-05-08 12:51:26 +0300
  * Automatic merge
    * [Revision #2959.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2959.1.1) \[merge]\
      Sun 2011-05-08 12:37:38 +0300
      * Automatic merge with 5.1
        * [Revision #2643.127.8](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.8)\
          Fri 2011-05-06 14:01:51 +0300
          * Reverted unittest/unit.pl back to Test::Harness as some of our build machines didn't support the new recommended TAP::Harness module
        * [Revision #2643.127.7](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.7)\
          Thu 2011-05-05 23:28:42 +0300
          * Speed up pbxt.range test a bit
        * [Revision #2643.127.6](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.6)\
          Thu 2011-05-05 14:51:01 +0300
          * Improved 'make test-unit' time slightly
* [Revision #2960](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2960)\
  Sat 2011-05-07 19:27:07 +0200
  * Fix effect of recent mismerge (it made default pid file name ".pid" instead of "hostname.pid")
* [Revision #2959](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2959) \[merge]\
  Wed 2011-05-04 22:33:18 +0300
  * Automatic merge
    * [Revision #2956.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2956.1.1) \[merge]\
      Wed 2011-05-04 22:25:56 +0300
      * Automatic merge with 5.1
        * [Revision #2643.127.5](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.5) \[merge]\
          Wed 2011-05-04 21:56:29 +0300
          * Automatic merge
            * [Revision #2643.129.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.129.1)\
              Wed 2011-05-04 21:51:44 +0300
              * Fixed build errors on centos5-amd64-minimal, where we compile with very few character sets
              * Fixed compiler warnings
        * [Revision #2643.127.4](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.4)\
          Wed 2011-05-04 21:28:02 +0300
          * Fixed build errors on centos5-amd64-minimal, where we compile with very few character sets
          * Fixed compiler warnings
* [Revision #2958](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2958) \[merge]\
  Wed 2011-05-04 17:11:54 +0200
  * merge
    * [Revision #2643.127.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.3) \[merge]\
      Wed 2011-05-04 16:12:39 +0200
      * merge
        * [Revision #2643.128.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.128.2)\
          Wed 2011-05-04 16:03:52 +0200
          * Cherrypick fix for maria recovery bug [Bug #686006](https://bugs.launchpad.net/bugs/686006) from 5.2 into 5.1
        * [Revision #2643.128.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.128.1)\
          Wed 2011-05-04 15:45:39 +0200
          * Avoid mtr warning on Windows during startup
          * The reason for mtr warning is that collect\_mysqld\_features() starts mysqld with `--datadir=/tmp` and this\
            directory does not exist on Windows.
          * Fix : instead of passing `--datadir=$opt_vardir/tmp` in collect\_mysqld\_features() just use `--datadir=`.\
            mysqld does not need a correct directory, just an existing one, as it is started with `--help` `---verbose` `--skip-grant-tables`.
* [Revision #2957](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2957)\
  Wed 2011-05-04 14:47:27 +0200
  * fix noisy warnings in header files
* [Revision #2956](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2956) \[merge]\
  Wed 2011-05-04 12:04:13 +0300
  * Automatic merge
    * [Revision #2643.127.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.2) \[merge]\
      Wed 2011-05-04 11:59:16 +0300
      * Automatic merge
    * [Revision #2643.127.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.1) \[merge]\
      Tue 2011-05-03 19:36:06 +0200
      * merge
        * [Revision #2643.126.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.126.2) \[
          * merge]\
            Tue 2011-05-03 19:32:17 +0200
          * merge
        * [Revision #2643.126.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.126.1)\
          Tue 2011-05-03 19:30:21 +0200
          * Fix warning (unused local variable)
* [Revision #2955](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2955) \[merge]\
  Wed 2011-05-04 11:35:51 +0300
  * Automatic merge with 5.1
    * [Revision #2643.114.77](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.77)\
      Wed 2011-05-04 11:28:02 +0300
      * Fixed compiler warning
* [Revision #2954](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2954)\
  Wed 2011-05-04 11:31:06 +0300
  * Fixed typo that caused compiler warning
* [Revision #2953](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2953) \[merge]\
  Tue 2011-05-03 19:11:39 +0300
  * Automatic merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
    * [Revision #2643.114.76](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.76) \[merge]\
      Tue 2011-05-03 18:27:14 +0300
      * Automatic merge
        * [Revision #2643.125.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.125.1)\
          Tue 2011-05-03 18:17:13 +0300
          * Fixed after-merge failures found by buildbot
    * [Revision #2643.114.75](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.75)\
      Tue 2011-05-03 12:50:09 +0200
      * Fix Xtradb compile error on Win64 - conversion between pointers of different size
    * [Revision #2643.114.74](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.74)\
      Mon 2011-05-02 23:03:26 +0200
      * Fix compile errors:
* from xtradb merge
* portability error in bitmap-t.c ( variable size array in non-portable)
* [Revision #2952](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2952) \[merge]\
  Tue 2011-05-03 19:10:10 +0300
  * Merge with [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)
    * [Revision #2643.114.73](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.73) \[merge]\
      Mon 2011-05-02 21:42:52 +0300
      * Automatic merge
        * [Revision #2643.124.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.124.3) \[merge]\
          Mon 2011-05-02 21:41:02 +0300
          * Merge with xtradb fixes
        * [Revision #2643.124.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.124.2) \[merge]\
          Mon 2011-05-02 20:58:45 +0300
          * Merge with MySQL 5.1.57/58
          * Moved some BSD string functions from Unireg
        * [Revision #2643.124.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.124.1)\
          Thu 2011-04-28 23:58:00 +0300
          * Added calls to cleanup\_mutexes() for embedded library.
    * [Revision #2643.114.72](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.72) \[merge]\
      Fri 2011-04-29 16:16:42 +0200
      * Merge XtraDB from Percona Server 5.1.56-12.7 into MariaDB-5.1.
        * [Revision #0.6.46](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/0.6.46)\
          Fri 2011-04-29 14:49:04 +0200
          * Updated with changes from Percona Server 5.1.56-12.7, from\
            lp:percona-dev/percona-server/release-5.1.56-12.7 percona-server-5.1.56-12.7\
            as of April 29, 2011.
          * Merged: revid:ignacio.nin@percona.com-20110427224434-e5a4kpyfwvj641q3
* [Revision #2951](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2951) \[merge]\
  Tue 2011-04-12 14:26:06 +0200
  * Merge [Mariadb 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)->5.2
    * [Revision #2643.114.71](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.71)\
      Tue 2011-04-12 13:49:16 +0200
      * [Bug #732124](https://bugs.launchpad.net/bugs/732124): PBXT result file updates that were forgotten when patch was pushed.
    * [Revision #2643.114.70](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.70) \[merge]\
      Tue 2011-04-12 11:48:43 +0200
      * Merge fix of missing lock initialisation from Vlad:\
        "fixed the problem for the failing preload.test in pbxt suite"
        * [Revision #2643.123.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.123.1)\
          Thu 2011-04-07 18:28:52 +0200
          * fixed the preload.test pbxt bug
    * [Revision #2643.114.69](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.69)\
      Wed 2011-03-09 19:45:48 +0200
      * Bug fix for [Bug #732124](https://bugs.launchpad.net/bugs/732124) union + limit returns wrong result
* [Revision #2950](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2950)\
  Sun 2011-04-10 22:48:28 -0700
  * Detect Boost installation and build OQGRAPH when possible. For now, disable oqgraph on x64 until [Bug #756966](https://bugs.launchpad.net/bugs/756966) is solved.
* [Revision #2949](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2949) \[merge]\
  Fri 2011-04-08 02:58:14 +0200
  * merge
    * [Revision #2948.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2948.1.3)\
      Fri 2011-04-08 02:49:04 +0200
      * enable 'Optimized for transactions'configuration checkbox if innodb is compiled in
    * [Revision #2948.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2948.1.2)\
      Fri 2011-04-08 01:42:47 +0200
      * fix CRLF line endings to LF
    * [Revision #2948.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2948.1.1)\
      Fri 2011-04-08 01:41:07 +0200
      * Fix SQL syntax error when running mysql `--bootstrap`.
* [Revision #2948](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2948) \[merge]\
  Sun 2011-04-03 21:12:29 +0200
  * merge
    * [Revision #2947.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2947.1.1)\
      Sun 2011-04-03 20:56:47 +0200
      * Fix error in "make dist" (sql/CMakeLists.txt is not delivered in source distribution)
* [Revision #2947](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2947)\
  Wed 2011-03-30 21:26:31 +0200
  * [Bug #686006](https://bugs.launchpad.net/bugs/686006) : maria recovery tests fail.
  * All failing cases were attempts to use connection after\
    the server was brought down and restarted. Connections\
    used client reconnect option.
  * The reason for failures is the behavior of sockets on Windows:\
    for a short period after crash (short enough to make the error\
    not reproducible under debugger), write to socket on client\
    side would succeed but subsequent read would fail.
  * MYSQL\_OPT\_RECONNECT does not really help in this case ,\
    because in the case given here ,as mysql\_real\_query()\
    (which can handle reconnect option) succeeds and\
    mysql\_read\_results() (can't handle reconnect) fails.
  * The fix is adding `--include` wait\_until\_connected\_again.inc to\
    appropriate places in test. This ensures that read errors are\
    caught and connection is recreated.
* [Revision #2946](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2946)\
  Wed 2011-03-30 19:20:22 +0300
  * Fixed problem that fill\_record() allocated memory for every call. This could be a problem when doing big unions as memory could be filled up.
* [Revision #2945](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2945)\
  Tue 2011-03-29 19:15:44 +0200
  * fix VS warning about variable 'unused' being used
* [Revision #2944](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2944)\
  Tue 2011-03-29 19:01:42 +0200
  * Add optional CMake parameter TINY\_VERSION.
  * Parameter setting has the effect on 4th part of the version string in executable's version info on Windows.
  * It could be set e.g to bzr revno to uniquely identify different builds for the same major.minor.patch combo.
* [Revision #2943](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2943)\
  Mon 2011-03-28 16:53:46 +0200
  * [Bug #702084](https://bugs.launchpad.net/bugs/702084) - myisam\_block\_size is not reported in SHOW GLOBAL VARIABLES
  * add a read-only server variable @@myisam\_block\_size
* [Revision #2942](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2942) \[merge]\
  Mon 2011-03-28 17:17:41 +0200
  * merge
    * [Revision #2941.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2941.1.1)\
      Mon 2011-03-28 17:01:40 +0200
      * CMake/code signing:
      * Use MYSQL\_INSTALL\_TARGETS() macro for DLLs\
        (libmysql and libmysqld) to ensure that libraries\
        are signed, if signing is requested.
* [Revision #2941](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2941)\
  Mon 2011-03-28 12:56:34 +0200
  * Sign MSI if code signing is requested.
  * Remove SIGNCODE\_ENABLED variable from create\_msi.cmake.in,\
    it was already removed from other places.
* [Revision #2940](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2940)\
  Mon 2011-03-28 12:49:20 +0300
  * Fixed test failures with embedded server
* [Revision #2939](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2939)\
  Mon 2011-03-28 02:02:24 +0200
  * Fix build error (wrong printf-like format)
* [Revision #2938](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2938)\
  Mon 2011-03-28 01:05:34 +0200
  * CMake fixes for buildbot/MSI package building and signing:
    * FIND\_PROGRAM (signtool) will now get a hint about location of signtool.exe (Windows SDK)
    * Targets "package" or "msi" will now fail, l if signing is requested but does not work\
      (e.g invalid certificate)
    * During install, do not re-sign binaries, if they are already signed.
    * Preserve mysqld\_error.h timestamp whenever possible. This helps avoiding situations\
      where the whole server is rebuilt, whenever comp\_err.exe changes (for example after code\
      signing, or also after a minor fix in mysys)
    * Fix Wix error in UpgradeVersion, if patch part of the version is 0.
* [Revision #2937](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2937) \[merge]\
  Wed 2011-03-23 19:22:38 +0200
  * Merge with base 5.2
    * [Revision #2933.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2933.1.2)\
      Wed 2011-03-23 17:59:41 +0200
      * Added `--log-basename` to mysqld to allow one to set the prefix for all logs with one command
      * Changed test suite to use `--log-basename` (to get the code tested)
      * Added `--sync-sys=1` to test suite to speed it up.
      * Better error messages if something goes wrong with mysql\_install\_db
    * [Revision #2933.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2933.1.1)\
      Fri 2011-03-18 17:03:43 +0200
      * Ensure that all clients reads the appropriate 'client', client-mariadb and 'mariadb' sections from my.cnf
      * The mysqld server and all clients now reads the new client-server section
      * Fixed that mysqldumpslow supports new slow log formats and new mysqld `--slow-` options
* [Revision #2936](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2936) \[merge]\
  Fri 2011-03-11 16:07:09 +0100
  * merge
    * [Revision #2919.1.30](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.30)\
      Fri 2011-03-11 16:06:35 +0100
      * fix warning
* [Revision #2935](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2935) \[merge]\
  Fri 2011-03-11 15:44:04 +0100
  * merge
    * [Revision #2919.1.29](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.29)\
      Fri 2011-03-11 15:43:05 +0100
      * remove unused variable
* [Revision #2934](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2934) \[merge]\
  Fri 2011-03-11 15:12:57 +0100
  * merge
    * [Revision #2919.1.28](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.28) \[merge]\
      Thu 2011-03-10 09:39:14 +0100
      * merge 5.2
    * [Revision #2919.1.27](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.27)\
      Wed 2011-03-09 20:21:03 +0100
      * [MWL#59](https://askmonty.org/worklog/?tid=59) - windows installer.
      * Address Monty's review comments
    * [Revision #2919.1.26](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.26)\
      Tue 2011-02-15 13:04:55 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : Philip's review:
        * Take into account that mysql services start even with\
          invalid defaults files (using data file relative to mysqld.exe location).\
          Handle this case in upgrade scenarios, as if there was no`--defaults-file` in service definition.
    * [Revision #2919.1.25](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.25)\
      Mon 2011-02-14 19:36:06 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : address Philip's final review comments :
        * rename upgrade\_wizard.exe to mysql\_upgrade\_wizard.exe
        * have shortcut to upgrade wizard in the menu folder
    * [Revision #2919.1.24](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.24)\
      Tue 2011-02-08 13:07:31 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55): look for my.cnf in addition to my.ini trying to figure out defaults file for the service
    * [Revision #2919.1.23](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.23)\
      Tue 2011-02-08 12:05:16 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55): mysql\_upgrade\_service.exe will now ensure that datadir is always written to my.ini file
    * [Revision #2919.1.22](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.22)\
      Mon 2011-02-07 17:12:35 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : Adjust UI according to some user's expectations.
      * If upgradable instances are found, bring a new dialog to inform user about it. This gives user a\
        chance to deselect "database instance" feature early, because experience\
        shows nobody really looks at features and their in their description in\
        "customize setup" dialog. This also tells user that existing instances\
        can be upgraded.
    * [Revision #2919.1.21](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.21)\
      Fri 2011-02-04 19:51:23 +0100
      * Remove `--loose-skip-pbxt` kludge from mysql\_install\_db\
        and mysql\_upgrade\_service, after [Bug #688404](https://bugs.launchpad.net/bugs/688404) was\
        fixed.
    * [Revision #2919.1.20](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.20)\
      Fri 2011-02-04 19:47:56 +0100
      * [Bug #688404](https://bugs.launchpad.net/bugs/688404) : Fix pbxt crashes on Windows 64 in debug build
      * The reason for the crash is misalignment on SSE instruciton\
        in setjmp(). The root cause is PBXT debug malloc(), which\
        unlike OS malloc does not guarantee 16 bytes alignment.
      * So the fix for now is disable PBXT debug malloc on Windows.\
        It was obsolete anyway, as it does not provide additional\
        benefits to C runtime debug routines (always used in debug\
        compilation) or to pageheap, available at runtime.
    * [Revision #2919.1.19](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.19)\
      Fri 2011-02-04 12:20:41 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55): Handle cases where service was installed with\
        mysqld `--install` without any parameters.
      * In such case, service name is always MYSQL, as service\
        binary path is "path\to\mysqld.exe" "MySQL". Guess data\
        directory it is either from my.ini (which is assumed to\
        be in the installation root), or just data directory\
        under install root.
    * [Revision #2919.1.18](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.18)\
      Fri 2011-02-04 12:16:23 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) :
        * Allow MSI and NSIS side-by-side installation if installed NSIS package\
          differs in "major.minor" version numbers. Still disallow MSI and NSIS\
          if major.minor versions of both packages match.
    * [Revision #2919.1.17](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.17)\
      Thu 2011-02-03 21:02:20 +0100
      * On Philips request, introduce a variable\
        BUILD\_RELEASE to disable graceful fallbacks\
        if WiX or MFC is not available.
    * [Revision #2919.1.16](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.16)\
      Thu 2011-02-03 18:56:30 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : Add banner text to command line utilities\
        (Philip's review)
    * [Revision #2919.1.15](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.15)\
      Thu 2011-02-03 17:51:03 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55): correct mysqld.exe file path, to extract version from it.
      * Take into account that services registered by MySQL do not have\
        .exe extension in service binary path.
    * [Revision #2919.1.14](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.14)\
      Thu 2011-02-03 16:05:21 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : force per-machine installation.
      * Problem: user without privileges can have an half-complete\
        installation, if he manages to click on "Ignore" for all errors\
        in the installer.
      * As a result, he will miss ARP registry keys, and uninstall\
        will not be possible using "Add/Remove Programs" applet.
    * [Revision #2919.1.13](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.13)\
      Wed 2011-02-02 01:34:22 +0100
      * AssignProcessToJobObject cannot assign current process\
        on Win7 with the most strict user account control setting\
        (secure desktop)
      * Fix: use job object for child process only, not for current\
        process itself.
    * [Revision #2919.1.12](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.12)\
      Wed 2011-02-02 01:30:24 +0100
      * Fix service user name and directory ACL setting on localized Windows
        * Spell username correctly as "NT AUTHORITY\NetworkService"
        * Also, use well-known SIDs for predefined user when assigning directory\
          ACLs (the names differ in localized Windows)
    * [Revision #2919.1.11](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.11)\
      Tue 2011-02-01 01:58:37 +0100
      * workaround [CMake Bug #11240](https://www.vtk.org/Bug/view.php?id=11240) (problems making mysqlserver.lib on Win64)
    * [Revision #2919.1.10](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.10)\
      Tue 2011-02-01 01:57:23 +0100
      * remove an extra LocalFree() call for pOldDacls, it is not allocated on heap
    * [Revision #2919.1.9](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.9)\
      Sun 2011-01-30 23:40:56 +0100
      * add some forgotten jpgs
    * [Revision #2919.1.8](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.8)\
      Sun 2011-01-30 23:20:02 +0100
      * add forgotten files generated by VS MFC project
    * [Revision #2919.1.7](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.7)\
      Sun 2011-01-30 22:42:02 +0100
      * split long lines, use get\_mysql\_service\_properties()
    * [Revision #2919.1.6](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.6)\
      Sun 2011-01-30 22:27:59 +0100
      * Move common functionality (analyze service configuration) into winservice library
    * [Revision #2919.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.5)\
      Sat 2011-01-29 19:06:50 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : implement MSI installer
      * The general technique to generate MSI using CMake is taken from MySQL 5.5
      * Additional features not present in 5.5 installer :
        * optionally creating a new database\
          (as Windows service), using new mysql\_install\_db.exe to do the job
        * optional upgrade of existing services from old MySQL or Maria installation.\
          This work is actually done by the upgrade wizard that is launched at the\
          end of installation.
    * [Revision #2919.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.4)\
      Sat 2011-01-29 19:02:43 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : implement upgrade\_wizard - GUI program\
        to uzpgrade existing MySQL/Maria services to higher version.
      * To be used in installer (but also can be used outside of installer too)
    * [Revision #2919.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.3)\
      Sat 2011-01-29 19:00:05 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) - mysql\_upgrade\_service.exe
      * New utility to upgrade Windows service to higher MariaDB version.
      * Its functionality includes changing service definition as well as\
        running mysql\_upgrade.
    * [Revision #2919.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.2)\
      Sat 2011-01-29 18:55:48 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : mysql\_install\_db.exe - command line utilityto install new database\
        on Windows.
        * Some parameters not present in traditional mysql\_install\_db are present\
          e.g `--port`, `--default-user` (whether to create a new users) or`--service` (windows service name)
    * [Revision #2919.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2919.1.1)\
      Sat 2011-01-29 18:51:12 +0100
      * [MWL#55](https://askmonty.org/worklog/?tid=55) : cherrypick MySQL 5.5 CMake/build improvements in order\
        to be able to build MSI based installer
* [Revision #2933](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2933) \[merge]\
  Tue 2011-03-08 15:16:13 +0200
  * Automatic merge with 5.1
    * [Revision #2643.114.68](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.68)\
      Tue 2011-03-08 14:55:36 +0200
      * Don't check if LAST\_IO\_Error has changed as this is not a user variable\
        and it may change depending on timing issues between master and slave
* [Revision #2932](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2932)\
  Mon 2011-03-07 15:10:32 +0100
  * pass WITH\_ARIA\_STORAGE\_ENGINE to configure.js
* [Revision #2931](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2931) \[merge]\
  Fri 2011-03-04 12:39:27 +0200
  * Automatic merge with 5.2 to fix compiler failure on FreeBSD
    * [Revision #2643.114.67](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.67)\
      Fri 2011-03-04 12:37:48 +0200
      * Removed wrong #ifdef that caused compile failure on Freebsd.
    * [Revision #2643.114.66](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.114.66)\
      Tue 2011-03-01 18:03:38 +0100
      * typo (in the yassl error message) fixed
* [Revision #2930](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2930)\
  Fri 2011-03-04 12:38:46 +0200
  * Updated version number

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
