# MariaDB 10.0.7 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.7) |[Release Notes](../../old-releases/10.0/10.0.7.md) |**Changelog** |[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 27 Dec 2013

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.7.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3961](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3961)\
  Mon 2013-12-23 10:29:25 +0100
  * update information\_schema-big.result
* [Revision #3960](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3960) \[merge]\
  Sun 2013-12-22 17:20:23 +0100
  * merge
  * [Revision #3950.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.14)\
    Sun 2013-12-22 17:14:05 +0100
    * mtr: abort when a suite.pm fails to load, don't just ignore the errors. Fix all suite.pm files that had errors and test files that were skipped because of that
  * [Revision #3950.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.13)\
    Sun 2013-12-22 17:11:38 +0100\
    \*
    * change the test to use is\_embedded.inc instead of a direct check \* remove is\_embedded.require
  * [Revision #3950.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.12)\
    Sun 2013-12-22 17:11:31 +0100
    * mtr: move collect\_default\_suites() after collect\_mysqld\_features(), because some suites may be disabled unless a plugin is available, and compiled-in plugins are only known after collect\_mysqld\_features().
  * [Revision #3950.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.11)\
    Sun 2013-12-22 17:11:24 +0100
    * don't install connect test suite explicitly, plugin.cmake does it automatically for all plugins
  * [Revision #3950.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.10)\
    Sun 2013-12-22 17:11:20 +0100
    * remove a deprecated API function from the plugin.h
  * [Revision #3950.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.9)\
    Sun 2013-12-22 17:11:16 +0100
    * remove duplicate function (see thd\_tx\_isolation())
  * [Revision #3950.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.8)\
    Sun 2013-12-22 17:10:47 +0100
    * mysql-test: \* rename "xtradb" combination to be called "innodb" \* disable xtradb\_plugin embedded tests (because of RECOMPILE\_FOR\_EMBEDDED)
  * [Revision #3950.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.7)\
    Sun 2013-12-22 17:09:16 +0100
    * use -visibility=hidden also for plugins linked statically into libmysqld (it was used only for plugins in mysqld)
  * [Revision #3950.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.6)\
    Sun 2013-12-22 17:09:10 +0100
    * put ha\_xtradb.so in deb packages
  * [Revision #3950.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.5)\
    Sun 2013-12-22 17:08:50 +0100
    * use dynamic libaio for ha\_xtradb.so
  * [Revision #3950.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.4)\
    Sun 2013-12-22 17:08:22 +0100
    * fix xtradb I\_S tables to load
  * [Revision #3950.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.3) \[merge]\
    Sun 2013-12-22 17:06:50 +0100
    * Percona-Server-5.6.14-rel62.0 merge
    * [Revision #0.12.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.67)\
      Mon 2013-12-16 15:38:05 +0100
      * Percona-Server-5.6.14-rel62.0.tar.gz
    * [Revision #0.12.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.66)\
      Mon 2013-12-16 15:36:18 +0100
      * rename \*.c -> \*.cc
  * [Revision #3950.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.2)\
    Mon 2013-12-16 15:52:36 +0100
    * undelete a file
  * [Revision #3950.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950.1.1)\
    Mon 2013-12-16 13:32:03 +0100
    * move oqgraph and sphinx suites into storage/\*/mysql-test/
* [Revision #3959](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3959) \[merge]\
  Sun 2013-12-22 17:18:45 +0100
  * merge 10.0-connect
  * [Revision #3913.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.22)\
    Fri 2013-12-20 12:24:24 +0100\
    \*
    * Fix [MDEV-5340](https://jira.mariadb.org/browse/MDEV-5340)
  * [Revision #3913.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.21) \[merge]\
    Fri 2013-12-20 13:46:45 +0400
    * Merge 10.0->10.0-connect
  * [Revision #3913.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.20)\
    Thu 2013-12-19 12:56:06 +0100\
    \*
    * Add extra column info in discovery
  * [Revision #3913.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.19) \[merge]\
    Tue 2013-12-17 17:50:55 +0400
    * Merge 10.0->10.0-connect
  * [Revision #3913.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.18)\
    Tue 2013-12-17 17:42:19 +0400
    * Fixing a compilation warning
  * [Revision #3913.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.17)\
    Mon 2013-12-16 17:40:42 +0100\
    \*
    * Fix logical error in STRBLK::SetValue
  * [Revision #3913.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.16)\
    Mon 2013-12-16 01:32:47 +0100\
    \*
    * Fix [MDEV-5393](https://jira.mariadb.org/browse/MDEV-5393) and [MDEV-5434](https://jira.mariadb.org/browse/MDEV-5434). It is a major update of ODBC catalog tables processing that takes care of: - Drastically reduce the amount of storage needed to process them. - Handle longjmp's. - Makes the line limit an option (MAXRES) - Schema can also be specified with the DBNAME option. - Issue warnings on fetch errors or when result lines have been limited. - Change some column names to reflect ODBC version 3 standard. The documentation has been updated accordingly
* [Revision #3958](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3958)\
  Fri 2013-12-20 12:42:33 +0400
  * [MDEV-4929](https://jira.mariadb.org/browse/MDEV-4929) Myanmar collation
* [Revision #3957](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3957) \[merge]\
  Thu 2013-12-19 17:54:02 +0400
  * Merge 10.0-base->10.0
  * [Revision #3427.35.229](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.229)\
    Thu 2013-12-19 17:50:08 +0400
    * A post-fix for [MDEV-5009](https://jira.mariadb.org/browse/MDEV-5009) don't look inside /\*!50700 ... \*/ comments
* [Revision #3956](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3956)\
  Thu 2013-12-19 12:39:40 +0400
  * [MDEV-4838](https://jira.mariadb.org/browse/MDEV-4838) Wrong metadata for DATE\_ADD('string', INVERVAL) The problem seems to be fixed by some earlier change and is not reproducible any longer. Only adding a test case.
* [Revision #3955](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3955) \[merge]\
  Wed 2013-12-18 01:56:13 +0400
  * Merge 10.0-base->10.0
  * [Revision #3427.35.228](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.228)\
    Wed 2013-12-18 01:08:39 +0400
    * [MDEV-5009](https://jira.mariadb.org/browse/MDEV-5009) don't look inside /\*!50700 ... \*/ comments
* [Revision #3954](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3954) \[merge]\
  Tue 2013-12-17 17:28:48 +0400
  * Merge 10.0-base->10.0
  * [Revision #3427.35.227](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.227) \[merge]\
    Tue 2013-12-17 16:23:08 +0400
    * Merge 5.5->10.0-base
    * [Revision #3413.21.463](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.463)\
      Tue 2013-12-17 15:19:26 +0400
      * [MDEV-5453](https://jira.mariadb.org/browse/MDEV-5453) Assertion \`src' fails in my\_strnxfrm\_unicode on GROUP BY MID(..) WITH ROLLUP Fixed a wrong assertion.
* [Revision #3953](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3953)\
  Tue 2013-12-17 14:40:56 +0400
  * [MDEV-5452](https://jira.mariadb.org/browse/MDEV-5452) 10.0 does not build on openSUSE 13.1
* [Revision #3952](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3952) \[merge]\
  Tue 2013-12-17 13:26:35 +0400
  * Merge from 10.0-base
  * [Revision #3427.35.226](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.226)\
    Tue 2013-12-17 13:23:05 +0400
    * [MDEV-5445](https://jira.mariadb.org/browse/MDEV-5445) Server crashes in Item\_func\_like::fix\_fields on LIKE ExtractValue(..) backporting from the main 10.0
* [Revision #3951](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3951)\
  Tue 2013-12-17 01:38:44 +0400
  * [MDEV-5445](https://jira.mariadb.org/browse/MDEV-5445) Server crashes in Item\_func\_like::fix\_fields on LIKE ExtractValue(..) Fixed.
* [Revision #3950](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3950) \[merge]\
  Mon 2013-12-16 13:28:35 +0100
  * merge
  * [Revision #3945.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3945.1.2) \[merge]\
    Mon 2013-12-16 13:02:21 +0100
    * 10.0-base merge
    * [Revision #3427.35.225](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.225) \[merge]\
      Sun 2013-12-15 15:57:26 +0100
      * 5.5 merge
    * [Revision #3427.35.224](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.224)\
      Sat 2013-12-14 19:13:37 -0800
      * Fixed bug [MDEV-5415](https://jira.mariadb.org/browse/MDEV-5415). Do not calculate selectivity of conditions for the tables of the information schema.
    * [Revision #3427.35.223](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.223)\
      Fri 2013-11-29 15:46:09 +0100
      * [MDEV-4986](https://jira.mariadb.org/browse/MDEV-4986): GTID - do not do on-disk update of master.info after every event group
    * [Revision #3427.35.222](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.222)\
      Fri 2013-11-29 15:44:22 +0400
      * Fixing mysql\_tzinfo\_to\_sql\_symlink.result that was unintentionally broken during merge 5.5->10.0-base
    * [Revision #3427.35.221](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.221) \[merge]\
      Wed 2013-11-27 10:12:09 -0800
      * Merge
      * [Revision #3427.40.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.40.1)\
        Wed 2013-11-27 09:06:34 -0800
        * Fixed bug [MDEV-5204](https://jira.mariadb.org/browse/MDEV-5204). Always use the value of table::file->stats.records when checking whether a table with HA\_STATS\_RECORDS\_IS\_EXACT flag contains not more than 1 record.
    * [Revision #3427.35.220](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.220)\
      Wed 2013-11-27 11:02:08 +0100
      * [MDEV-4816](https://jira.mariadb.org/browse/MDEV-4816): Incorrect disabling of binlog for mysql.gtid\_slave\_pos update
    * [Revision #3427.35.219](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.219)\
      Tue 2013-11-26 15:04:21 -0800
      * Added the test case for bug [MDEV-5200](https://jira.mariadb.org/browse/MDEV-5200). The bug was fixed by the patch applied to the 5.3 tree in the revision 3727.
    * [Revision #3427.35.218](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.218)\
      Tue 2013-11-26 11:26:08 +0400
      * Fixing mtr failures in mysql\_tzinfo\_to\_sql\_symlink.test on Labrador: sort directory data to make sure the same data order in the output of mysql\_tzinfo\_to\_sql on all platforms.
    * [Revision #3427.35.217](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.217) \[merge]\
      Mon 2013-11-25 10:04:41 -0800
      * Merge
      * [Revision #3413.21.441](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.441) \[merge]\
        Sun 2013-11-24 22:10:36 -0800
        * Merge
        * [Revision #2502.567.171](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.171)\
          Sun 2013-11-24 20:45:16 -0800
          * Made sure that JOIN::cond\_equal is correctly set after the call of remove\_eq\_conds() in the function make\_join\_statistics().
    * [Revision #3427.35.216](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.216)\
      Mon 2013-11-25 15:21:25 +0100
      * [MDEV-4946](https://jira.mariadb.org/browse/MDEV-4946): IO thread should expose its current GTID position
    * [Revision #3427.35.215](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.215) \[merge]\
      Sat 2013-11-23 10:40:07 -0800
      * Merge
      * [Revision #3413.21.440](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.440) \[merge]\
        Fri 2013-11-22 18:38:13 -0800
        * Merge
        * [Revision #2502.567.170](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.170)\
          Fri 2013-11-22 13:13:03 -0800
          * Post-review changes of the patch for bug [MDEV-5103](https://jira.mariadb.org/browse/MDEV-5103).
    * [Revision #3427.35.214](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.214)\
      Sat 2013-11-23 13:05:35 +0100
      * tokudb post-merge compilation fixes
    * [Revision #3427.35.213](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.213) \[merge]\
      Sat 2013-11-23 00:50:54 +0100
      * 5.5 merge
    * [Revision #3427.35.212](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.212)\
      Fri 2013-11-22 13:33:20 +0100
      * [MDEV-4983](https://jira.mariadb.org/browse/MDEV-4983): Do not leave stale master-bin.state binlog state file
    * [Revision #3427.35.211](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.211) \[merge]\
      Thu 2013-11-21 16:32:03 +0400
      * Merge
      * [Revision #3427.39.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.39.1)\
        Thu 2013-11-21 16:29:46 +0400
        * [MDEV-5308](https://jira.mariadb.org/browse/MDEV-5308) Crash when running with slow\_query\_log=1 - Make log\_slow\_statement() always call delete\_explain\_query().
    * [Revision #3427.35.210](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.210)\
      Thu 2013-11-21 14:42:25 +0100
      * [MDEV-4982](https://jira.mariadb.org/browse/MDEV-4982): GTID loses all binlog state after crash if InnoDB is disabled [MDEV-4725](https://jira.mariadb.org/browse/MDEV-4725): Incorrect binlog state recovery if crash while writing event group
    * [Revision #3427.35.209](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.209) \[merge]\
      Thu 2013-11-21 13:16:26 +0400
      * Merge 5.5->10.0-base
    * [Revision #3427.35.208](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.208)\
      Mon 2013-11-18 15:22:50 +0100
      * [MDEV-5306](https://jira.mariadb.org/browse/MDEV-5306): Missing locking around rpl\_global\_gtid\_binlog\_state
    * [Revision #3427.35.207](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.207)\
      Thu 2013-11-14 15:08:29 +0100
      * [MDEV-5291](https://jira.mariadb.org/browse/MDEV-5291): Slave transaction retry on temporary error leaves dangling error in SHOW SLAVE STATUS
  * [Revision #3945.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3945.1.1)\
    Fri 2013-12-13 14:26:10 +0100
    * [MDEV-5438](https://jira.mariadb.org/browse/MDEV-5438) A view can mask a table that supports discovery
* [Revision #3949](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3949)\
  Mon 2013-12-16 16:03:34 +0400
  * [MDEV-5319](https://jira.mariadb.org/browse/MDEV-5319) - Request for merge of Oqgraph v3 functionality storage/oqgraph into 10.0
* [Revision #3948](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3948)\
  Mon 2013-12-16 13:55:43 +0400
  * [MDEV-5319](https://jira.mariadb.org/browse/MDEV-5319) - Request for merge of Oqgraph v3 functionality storage/oqgraph into 10.0
* [Revision #3947](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3947)\
  Mon 2013-12-16 12:26:20 +0400
  * [MDEV-4748](https://jira.mariadb.org/browse/MDEV-4748) - metadata\_lock\_info plugin
* [Revision #3946](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3946) \[merge]\
  Mon 2013-12-16 01:19:03 +0400
  * Merge 10.0-connect -> 10.0.
  * [Revision #3913.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.15) \[merge]\
    Sat 2013-12-14 15:37:55 +0400
    * Merge 10.0->10.0-connect
  * [Revision #3913.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.14)\
    Thu 2013-12-12 17:26:01 +0400
    * ConnectSE: making odbc\_postgresql.test independent from the system locale (on Linux) and code pages (on Windows).
  * [Revision #3913.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.13)\
    Thu 2013-12-12 01:33:53 +0100\
    \*
    * Fix (temporarily) bug on odbc\_postgresql.test
  * [Revision #3913.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.12)\
    Wed 2013-12-11 23:33:36 +0100\
    \*
    * Add longjmp initialization in PlgAllocResult
  * [Revision #3913.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.11) \[merge]\
    Wed 2013-12-11 16:57:25 +0100\
    \*
    * Commit merged files from Alexander
    * [Revision #3913.2.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.2.2)\
      Wed 2013-12-11 19:47:37 +0400
      * Fixing the message displayed when the test PostgreSQL data source name does not exist.
    * [Revision #3913.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.2.1)\
      Wed 2013-12-11 18:47:46 +0400
      * [MDEV-5341](https://jira.mariadb.org/browse/MDEV-5341) ConnectSE: discovery for ODBC tables does not work if tables with the same names present in multiple schemas
  * [Revision #3913.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.10)\
    Wed 2013-12-11 16:52:01 +0100\
    \*
    * Fix errors and warnings occuring in `--embedded` tests
  * [Revision #3913.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.9)\
    Tue 2013-12-10 12:53:46 +0400
    * Moving the code checking libxml2 into a \*.inc file.
  * [Revision #3913.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.8)\
    Fri 2013-12-06 01:37:56 +0100\
    \*
    * Raise the limit on returned lines for table ODBC catalog tables to 16384 ([MDEV-5393](https://jira.mariadb.org/browse/MDEV-5393))
  * [Revision #3913.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.7)\
    Thu 2013-12-05 18:31:14 +0400
    * [MDEV-5343](https://jira.mariadb.org/browse/MDEV-5343) ConnectSE: ODBC: CATFUNC=Tables and CATFUNC=Columns crash when running against a data source with many tables
  * [Revision #3913.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.6)\
    Thu 2013-12-05 17:26:28 +0400
    * Adding basic ODBC tests that do not need a DSN
  * [Revision #3913.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.5)\
    Thu 2013-12-05 12:32:06 +0100\
    \*
    * Suppress eventual prompting when connecting to an ODBC source
  * [Revision #3913.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.4)\
    Thu 2013-12-05 01:00:28 +0100\
    \*
    * Previous [MDEV-5261](https://jira.mariadb.org/browse/MDEV-5261) was generating wrong warnings
  * [Revision #3913.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.3)\
    Wed 2013-12-04 23:53:30 +0100\
    \*
    * Fix bug [MDEV-5261](https://jira.mariadb.org/browse/MDEV-5261)
  * [Revision #3913.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.2)\
    Tue 2013-12-03 23:34:50 +0100\
    \*
    * Fix a typo error in tabutil line 213
  * [Revision #3913.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913.1.1)\
    Tue 2013-12-03 22:59:40 +0100\
    \*
    * Add support for unsigned numeric types
* [Revision #3945](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3945)\
  Fri 2013-12-13 17:18:10 +0400
  * Fixing temporarily test failures in ctype\_xxx. The problem reported as [MDEV-5444](https://jira.mariadb.org/browse/MDEV-5444).
* [Revision #3944](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3944)\
  Fri 2013-12-13 12:42:45 +0400
  * [MDEV-4748](https://jira.mariadb.org/browse/MDEV-4748) - metadata\_lock\_info plugin
* [Revision #3943](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3943)\
  Wed 2013-12-11 00:31:04 +0900
  * add metadata\_lock\_info
* [Revision #3942](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3942)\
  Thu 2013-12-12 20:30:56 +0100
  * add a forgotten my\_afree() to make valgrind happy
* [Revision #3941](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3941)\
  Thu 2013-12-12 21:49:14 +0400
  * [MDEV-5388](https://jira.mariadb.org/browse/MDEV-5388) - Reduce usage of LOCK\_open: unused\_tables
* [Revision #3940](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3940)\
  Tue 2013-12-10 19:00:36 +0400
  * [MDEV-4956](https://jira.mariadb.org/browse/MDEV-4956) - Reduce usage of LOCK\_open: TABLE\_SHARE::tdc.used\_tables
* [Revision #3939](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3939)\
  Thu 2013-12-12 17:02:13 +0100
  * restore debian/dist/Ubuntu/control that was changed by mistake
* [Revision #3938](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3938)\
  Mon 2013-12-09 12:39:31 +0100
  * correct old assert in add\_role\_user\_mapping\_action to match changed function prototypes. fix the element deleting logic for roles\_mappings\_hash
* [Revision #3937](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3937)\
  Mon 2013-12-09 12:39:19 +0100
  * remove sys\_var specific restore\_pluginvar\_names() function, use generic restore\_ptr\_backup() approach
* [Revision #3936](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3936)\
  Mon 2013-12-09 12:39:13 +0100
  * [MDEV-4403](https://jira.mariadb.org/browse/MDEV-4403) Attempting to use Cassandra storage engine causes "service 'my\_snprintf\_service' interface version mismatch"
* [Revision #3935](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3935)\
  Mon 2013-12-09 12:38:37 +0100
  * remove #ifdef ENABLE\_BEFORE\_END\_OF\_MERGE\_QQ
* [Revision #3934](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3934)\
  Mon 2013-12-09 12:38:30 +0100
  * cleanups: \* comments from [WL#5602](https://askmonty.org/worklog/?tid=5602) in sql\_acl.cc \* rename global memroots in sql\_acl.cc \* remove the second empty lex string constant
* [Revision #3933](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3933)\
  Mon 2013-12-09 12:38:20 +0100
  * bugfix: incorrect buffer sizes for net\_store\_length()
* [Revision #3932](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3932)\
  Mon 2013-12-09 12:38:09 +0100
  * reuse new safe\_net\_field\_length\_ll function where appropriate
* [Revision #3931](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3931)\
  Mon 2013-12-09 12:38:02 +0100
  * Do the partial merge of [WL#5602](https://askmonty.org/worklog/?tid=5602) correctly: Remove unused code (that should not have been merged) Add protocol extension (that should have been merged) Fix bugs (see pack.c)
* [Revision #3930](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3930)\
  Mon 2013-12-09 12:37:45 +0100
  * [MDEV-5115](https://jira.mariadb.org/browse/MDEV-5115) RBR from MySQL 5.6 to [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) does not work
* [Revision #3929](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3929)\
  Sun 2013-12-01 12:16:24 +0100
  * [MDEV-5367](https://jira.mariadb.org/browse/MDEV-5367) Server crashes in acl\_authenticate on concurrent thread connection, FLUSH PRIVILEGES
* [Revision #3928](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3928)\
  Thu 2013-11-28 22:35:59 +0100
  * [MDEV-4243](https://jira.mariadb.org/browse/MDEV-4243) \[PATCH] Warnings/errors while compiling with clang
* [Revision #3927](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3927)\
  Thu 2013-11-28 16:39:17 +0100
  * [MDEV-4955](https://jira.mariadb.org/browse/MDEV-4955) discover of table non-existance on CREATE when frm file exists, but the table does not.
* [Revision #3926](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3926)\
  Thu 2013-11-28 12:10:44 +0100
  * [MDEV-5281](https://jira.mariadb.org/browse/MDEV-5281) Partitioning issue after upgrade from 10.0.3-1 to 10.0.5-1
* [Revision #3925](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3925)\
  Wed 2013-11-27 22:30:59 +0100
  * typo fix in ha\_partition::rnd\_pos(), status wasn't updated
* [Revision #3924](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3924)\
  Mon 2013-11-25 15:46:33 +0100
  * Fix a first timestamp column in the sql-based table discovery
* [Revision #3923](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3923)\
  Thu 2013-11-21 15:06:23 +0100
  * remove obsolete licenses from README, add PCRE license
* [Revision #3922](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3922)\
  Thu 2013-11-21 15:05:25 +0100
  * remove unused libevent (that was merged from 5.6 by mistake)
* [Revision #3921](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3921)\
  Thu 2013-11-21 14:25:28 +0100
  * unreserve GET keyword
* [Revision #3920](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3920)\
  Thu 2013-12-12 19:18:49 +0400
  * MroongaSE: addint thd\_autoinc and thd\_error\_context plugin services
* [Revision #3919](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3919)\
  Wed 2013-12-11 16:37:53 +0400
  * [MDEV-5431](https://jira.mariadb.org/browse/MDEV-5431) Test main.ctype\_latin2 fails in buildbot Fixing include/ctype\_datetime.inc not to depend on the current time zone.
* [Revision #3918](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3918) \[merge]\
  Wed 2013-12-11 13:06:21 +0400
  * [MDEV-5319](https://jira.mariadb.org/browse/MDEV-5319) - Request for merge of Oqgraph v3 functionality storage/oqgraph into 10.0
  * [Revision #3916.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3916.1.1) \[merge]\
    Wed 2013-12-11 13:02:12 +0400
    * [MDEV-5319](https://jira.mariadb.org/browse/MDEV-5319) - Request for merge of Oqgraph v3 functionality storage/oqgraph into 10.0
* [Revision #3917](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3917)\
  Wed 2013-12-11 12:30:12 +0400
  * An upstream bug fixed: "mtr ctype\_ldml" failed when compiled with "gcc -funsigned-char". Changing the code not to depend on the signed/unsigned compiler defaults for the "char" data type.
* [Revision #3916](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3916)\
  Tue 2013-12-10 13:34:59 +0400
  * [MDEV-5298](https://jira.mariadb.org/browse/MDEV-5298) Illegal mix of collations on timestamp Fixed.
* [Revision #3915](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3915)\
  Fri 2013-12-06 19:02:55 +0400
  * [MDEV-5297](https://jira.mariadb.org/browse/MDEV-5297) TIME(0), TIMESTAMP(0) and DATETIME(0) are self-incompatible during replication (upstream) Fixed.
* [Revision #3914](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3914)\
  Thu 2013-12-05 16:54:50 +0400
  * Fixing an MSVC warning about double "const" data type qualifier in the code merged from MySQL-5.6:
* [Revision #3913](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3913) \[merge]\
  Tue 2013-12-03 14:12:53 +0400
  * Merge 10.0-connect -> 10.0
  * [Revision #3869.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.14)\
    Thu 2013-11-28 23:37:27 +0100\
    \*
    * Fix gcc compiling error
  * [Revision #3869.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.13)\
    Thu 2013-11-28 01:25:39 +0100\
    \*
    * Fix some wrong changes preparing for unsigned data types
  * [Revision #3869.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.12)\
    Tue 2013-11-26 11:47:48 +0100\
    \*
    * Fix gcc compilation warnings
  * [Revision #3869.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.11)\
    Fri 2013-11-22 16:03:54 +0100\
    \*
    * Fix good recognition of MYSQL table column types.
  * [Revision #3869.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.10)\
    Wed 2013-11-20 18:27:13 +0400
    * ConnectSE: Adding CATFUNC=Tables and CATFUC=Columns for the XLS ODBC data source.
  * [Revision #3869.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.9)\
    Wed 2013-11-20 14:50:52 +0400
    * Adding tests for CATFUC=Tables and CATFUNC=Columns into odbc\_sqlite3.test.
  * [Revision #3869.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.8)\
    Wed 2013-11-13 00:15:38 +0100\
    \*
    * Modify the way UPDATE and DELETE statements are sent to ODBC and MYSQL CONNECT tables to take care of kewords such as IGNORE.
  * [Revision #3869.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.7)\
    Mon 2013-11-11 18:30:36 +0100\
    \*
    * Add (limited) UPDATE/DELETE support to MYSQL type CONNECT tables
  * [Revision #3869.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.6)\
    Mon 2013-11-11 13:00:39 +0100\
    \*
    * Add (limited) support for UPDATE and DELETE to ODBC tables (also provide the possibility to issue NOTE warnings)
  * [Revision #3869.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.5)\
    Sat 2013-11-09 17:32:57 +0100\
    \*
    * BUG fixed: When updating, to avoid skipped update, force the table handler to retrieve write-only fields to be able to compare records and detect data change.
  * [Revision #3869.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.4)\
    Wed 2013-11-06 18:22:09 +0100\
    \*
    * Move all enum AMT definitions in one place (plgdbsem.h)
  * [Revision #3869.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.3)\
    Thu 2013-10-31 11:53:00 +0400\
    \*
    * Adding cmake code to install ConnectSE mtr tests - Including "connect" suite into the list of the default suites
  * [Revision #3869.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.2)\
    Tue 2013-10-29 16:21:57 +0100\
    \*
    * Update version number and date - Replace test on args\[i]->type() by args\[i]->field\_type() in ha\_connect::CheckCond. This to take care of cached items generated by executing a query in a procedure.
  * [Revision #3869.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3869.1.1)\
    Tue 2013-10-29 13:44:05 +0400
    * ConnectSE: fixing memory leaks reported by valgrind
* [Revision #3912](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3912)\
  Mon 2013-12-02 14:39:08 +0400
  * [MDEV-5357](https://jira.mariadb.org/browse/MDEV-5357) REGEXP word boundaries don't work Applied a patch from Philip Hazel implementing the non-standard syntax for word boundaries in PCRE, for compatibility with the old Henry Spencer's regex library.
* [Revision #3911](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3911)\
  Tue 2013-11-26 10:53:21 +0400
  * Fixing malformed data in mysql-test/std\_data/Index.xml
* [Revision #3910](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3910)\
  Mon 2013-11-25 18:49:40 +0400
  * [MDEV-5277](https://jira.mariadb.org/browse/MDEV-5277) - Ensure that all MySQL 5.6 options are supported by the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) server
* [Revision #3909](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3909)\
  Wed 2013-11-20 14:28:07 +0200
  * [MDEV-5010](https://jira.mariadb.org/browse/MDEV-5010): InnoDB errors appearing in logs with upgrade from 10.0.0 to 10.0.4.
* [Revision #3908](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3908)\
  Tue 2013-11-19 16:26:40 +0400
  * Increment the version number
* [Revision #3907](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3907)\
  Thu 2013-11-14 18:00:00 +0400
  * [MDEV-5220](https://jira.mariadb.org/browse/MDEV-5220) - \[PATCH] [MariaDB 10.0.4](../../old-releases/10.0/10.0.4.md) doesn't compile without perfschema

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
