# MariaDB 5.2.7 Changelog

[Download](https://downloads.askmonty.org/mariadb/5.2.7) |[Release Notes](../../old-releases/5.2/5.2.7.md) |**Changelog** |[Overview of 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)

**Release date:** 14 Jun 2011

For the highlights of this release, see the [release notes](../../old-releases/5.2/5.2.7.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #2993](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2993)\
  Mon 2011-06-13 12:46:11 +0300
  * Fixed portability problem with partiton\_error.test
  * Added option to aria\_read\_log to crash recovery at certain points in the\ recovery process.
  * Fixed bug that caused future recovery attempts to fail if we got a crash/got\
    killed during closing of tables at end of recovery process.
* [Revision #2992](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2992)\
  Sun 2011-06-12 12:52:51 +0300
  * Fixed warning that sf\_malloc\_trough\_check was not used when compiling\
    without SAFEMALLOC
* [Revision #2991](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2991)\
  Sat 2011-06-11 14:53:08 +0300
  * Updated to new error messages for partitions when .par file is missing
* [Revision #2990](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2990)\
  Sat 2011-06-11 14:28:37 +0300
  * Increased server version to 5.2.7
* [Revision #2989](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2989)\
  Sat 2011-06-11 14:28:15 +0300
  * Fixes [MySQL Bug #60976](https://bugs.mysql.com/bug.php?id=60976) "Crash, valgrind warning and memory leak with partitioned\
    archive tables"
    * Noted that there was no memory leak, just a lot of used partitioned tables.
  * Fixed old bug: 'show status' now shows memory usage when compiled with\
    safemalloc.
  * Added option `--flush` to mysqlcheck.c to run a 'flush tables' between each\
    check to keep down memory usage.
  * Changed '`--safemalloc`' options to mysqld so that one can use `--safemalloc`\
    and `--skip-safemalloc`.
  * Now skip-safemalloc is default (ie, we only do checking of memory overrun\
    during free()) to speed up tests.
* [Revision #2988](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2988)\
  Fri 2011-06-10 02:02:58 +0300
  * A bit better fix for tmp-table problem
  * Fixed reference to not initialized memory detected by valgrind
* [Revision #2987](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2987) \[merge]\
  Thu 2011-06-09 20:38:59 +0300
  * Merge with bug fixes
    * [Revision #2983.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2983.1.2)\
      Thu 2011-06-09 20:22:03 +0300
      * Use dynamic row format when creating temporary tables without sumary\
        fields.
      * The reason for this is that BLOCK\_RECORD format is not good when there is\
        a lot of duplicated keys as it first writes the data (to get the row\
        position) and then writes the key (and thus checks for duplicates).
    * [Revision #2983.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2983.1.1)\
      Thu 2011-06-09 16:17:45 +0300
      * Fixed problem that global status variables 'bytes\_recieved' and 'binlog\_bytes\_written' where not correctly updated
* [Revision #2986](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2986)\
  Thu 2011-06-09 00:24:27 +0200
  * After talking to HeidiSQL people - libmysql.dll that comes with their distribution in place, dont replace with our own.
  * It also will result in less HeidiSQL restarts during MariaDB upgrades (since libmysql.dll won't be replaced)
* [Revision #2985](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2985)\
  Wed 2011-06-08 16:56:35 +0200
  * Fix a problem building MSI using localized (Spanish) Visual Studio 2010.
  * VS did not like to execute 2 commands in custom build step, workaround is\
    to use single COMMAND instead of 2.
* [Revision #2984](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2984) \[merge]\
  Tue 2011-06-07 22:50:08 +0200
  * merge [MWL#200](https://askmonty.org/worklog/?tid=200)
    * [Revision #2982.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2982.1.3)\
      Thu 2011-06-02 10:06:51 +0200
      * use our libmysql.dll with HeidiSQL, if we compile 32 bit
    * [Revision #2982.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2982.1.2)\
      Wed 2011-06-01 21:14:10 +0200
      * Use our libmysql.dll with Heidi, if we compile 32 bit
    * [Revision #2982.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2982.1.1)\
      Wed 2011-06-01 15:52:52 +0200
      * [MWL#200](https://askmonty.org/worklog/?tid=200) - provide options to install 3rd party components.
      * Added HeidiSQL as example, i.e cmake -DWITH\_THIRD\_PARTY=HeidiSQL\
        and building MSI will bundle HeidiSQL.
* [Revision #2983](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2983)\
  Mon 2011-06-06 16:39:06 +0300
  * Fixed lock sorting and lock check issues with thr\_lock that caused warnings\
    when running test suite.
  * Safety check that could cause core dump when doing create table with virtual\
    column.
* [Revision #2982](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2982) \[merge]\
  Fri 2011-05-27 19:09:40 +0200
  * merge
    * [Revision #2981.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2981.1.1)\
      Fri 2011-05-27 18:57:40 +0200
      * Workaround a cmake bug that was only visible on a newly installed Philip's machine.
      *   CMake 2.8.4 crashed on this line

          ```
          IF(something AND IS_DIRECTORY(something_else))
          ```

          when both "something" and "something\_else" were empty.\\
    * Changing the line slightly (using cascading "IF" instead) solved the crash.
* [Revision #2981](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2981)\
  Thu 2011-05-26 18:35:26 +0300
  * Fixed memory overrun in mysql\_tzinfo\_to\_sql
* [Revision #2980](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2980) \[merge]\
  Thu 2011-05-26 18:34:22 +0300
  * Automatic merge
    * [Revision #2978.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2978.1.1) \[merge]\
      Thu 2011-05-26 18:07:06 +0300
      * Merge with 5.1 to get in fix wrong setpriority() call
        * [Revision #2643.127.14](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.14)\
          Thu 2011-05-26 14:38:17 +0300
          * Disable call to setpriority() in pbxt. This caused mysqld to run with\
            nice priority -19, which was far from optimal.
* [Revision #2979](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2979)\
  Thu 2011-05-26 13:42:22 +0200
  * Fix line endings.
* [Revision #2978](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2978)\
  Thu 2011-05-26 02:01:47 +0200
  * Fixed sql\_perror() to return appropriate error messages on Windows,
  * The error message is now based on GetLastError() rather than errno.
  * Background: errno is C runtime specific and in many circumstances\
    it is not set, e.g when using Win32 API or socket functions.
* [Revision #2977](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2977)\
  Thu 2011-05-26 00:37:08 +0200
  * On Windows, collect mysql error log with Windows Error Reporting.
  * This simplifies postmortem analysis for crashes reported via Winqual.
* [Revision #2976](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2976)\
  Mon 2011-05-23 15:56:43 +0200
  * Enable PBXT to be a transactional engine for sql-bench.
  * HEAP is deprecated in favor of MEMORY.
* [Revision #2975](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2975)\
  Fri 2011-05-20 14:36:13 +0300
  * Ensure we don't read a [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md) errmsg.sys file or new errmsg.sys file\
    with holes for not used error messages
* [Revision #2974](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2974) \[merge]\
  Fri 2011-05-20 01:44:30 +0200
  * merge
    * [Revision #2973.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2973.1.1)\
      Fri 2011-05-20 01:38:42 +0200
      * Properly terminate options array with all-zero entry.
      * Fix CRLF end of lines, use LF instead
* [Revision #2973](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2973) \[merge]\
  Wed 2011-05-18 15:17:26 +0200
  * automerge
    * [Revision #2643.127.13](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.13)\
      Wed 2011-05-18 15:15:36 +0200
      * Fix mysqltest printing of include stack.
      * The printing of include stack in the error case in mysqltest omitted the\
        bottom of the stack (the line number in original test case file), and\
        instead printed the top of the stack twice. Fix to print each element on\
        the stack once and only once.
* [Revision #2972](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2972)\
  Sun 2011-05-15 13:38:18 +0200
  * Small CMake fixes :
    * add version info for the client library, dynamic plugins and some utilities
    * do not recompile client library sources 3 times (for mysqlclient ,\
      mysqlclient\_notls and libmysql) One time is sufficient, so get rid of\
      mysqlclient\_notls, and link static client library to the shared.
    * remove incremental linking flag
* [Revision #2971](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2971) \[merge]\
  Sat 2011-05-14 18:59:49 +0200
  * merge2
    * [Revision #2968.1.5](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2968.1.5)\
      Sat 2011-05-14 18:59:06 +0200
      *   Fix compile error on Unixes

          ```
          my_rwlock_destroy=>rwlock_destroy
          ```
* [Revision #2970](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2970) \[merge]\
  Sat 2011-05-14 18:45:33 +0200
  * merge
    * [Revision #2968.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2968.1.4)\
      Sat 2011-05-14 18:42:07 +0200
      * Fix bugs found by application verifier :
        * Fix active lock in freed memory in ha\_archive (share mutex was not\
          released prior to free())
        * Do not attempt vio\_fastsend or vio\_keepalive on named pipes and shared\
          memory.
    * [Revision #2968.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2968.1.3)\
      Sat 2011-05-14 18:37:20 +0200
      * [Bug #782223](https://bugs.launchpad.net/bugs/782223) : Memory released by Query\_cache::resize() or\
        Query\_cache::free() contains active rwlocks.
      * The bug was found by application verifier.
      * Fixed by destroying locks prior to free(),
    * [Revision #2968.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2968.1.2)\
      Sat 2011-05-14 01:05:12 +0200
      * Fix PBXT bugs found while testing with Application Verifier :
      * [Bug #782269](https://bugs.launchpad.net/bugs/782269) : critical sections are initialized twice in xt\_xn\_init\_db()
      * [Bug #782431](https://bugs.launchpad.net/bugs/782431): active lock in memory released by xt\_ind\_exit()
      * [Bug #782433](https://bugs.launchpad.net/bugs/782433) : xt\_heap\_release() does not release spinlock hp->h\_lock initialized in xt\_heap\_new().
      * [Bug #782435](https://bugs.launchpad.net/bugs/782435): xt\_exit\_row\_locks() tries to release unallocated locks
    * [Revision #2968.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2968.1.1)\
      Fri 2011-05-13 17:55:36 +0200
      * [Bug #782269](https://bugs.launchpad.net/bugs/782269) : Fixed double initialization of condition variables in PBXT.
* [Revision #2969](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2969)\
  Fri 2011-05-13 16:22:05 +0300
  * Made test-unit run in parlallel. This was achived by having all aria tests\
    that uses temporary files to create the temporary file in an unique\
    tempdirectory.
  * aria\_chk now returns 1 if one got any warnings during check and 2 if one got\
    errors.
  * [Bug #728919](https://bugs.launchpad.net/bugs/728919) maria\_chk should fail on all detected corruptions
* [Revision #2968](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2968) \[merge]\
  Thu 2011-05-12 16:31:54 +0200
  * merge
    * [Revision #2643.127.12](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.12) \[merge]\
      Thu 2011-05-12 15:39:54 +0200
      * merge
        * [Revision #2643.130.2](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.130.2)\
          Thu 2011-05-12 15:34:02 +0200
          * Windows build : Make win\config.js optional in 5.1\
            Simplifies handling 5.1 in buildbot.
        * [Revision #2643.130.1](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.130.1)\
          Thu 2011-05-12 15:31:11 +0200
          * Fix check\_table\_file\_presence:
          * On Windows, do not attempt access() for special device names like CON,\
            PRN etc. access() would return 0, this does not mean that fiile with\
            this name exists.
    * [Revision #2643.127.11](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.11)\
      Thu 2011-05-12 14:56:08 +0300
      * db\_name can change case, so we need copy of it for case insensitive FS.
    * [Revision #2643.127.10](https://bazaar.launchpad.net/~maria-captains/maria/5.2/revision/2643.127.10)\
      Wed 2011-05-11 14:09:48 +0300
      * Bugfix: New table creation/renaming block added if old encoded table present.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
