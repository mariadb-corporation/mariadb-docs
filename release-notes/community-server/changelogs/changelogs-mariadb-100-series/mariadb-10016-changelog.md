# MariaDB 10.0.16 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.16)[Release Notes](../../old-releases/10.0/10.0.16.md)[Changelog](mariadb-10016-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 27 Jan 2015

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.16.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4588](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4588)\
  Sun 2015-01-25 16:16:25 +0100
  * [MDEV-5719](https://jira.mariadb.org/browse/MDEV-5719): Wrong result with GROUP BY and LEFT OUTER JOIN
* [Revision #4587](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4587)\
  Fri 2015-01-23 14:17:38 +0100
  * win32-debug build failure
* [Revision #4586](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4586)\
  Fri 2015-01-23 13:56:46 +0100
  * [MDEV-7352](https://jira.mariadb.org/browse/MDEV-7352): main.kill\_processlist-6619 fails sporadically in buildbot
* [Revision #4585](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4585) \[merge]\
  Fri 2015-01-23 09:36:03 +0100
  * 5.5 merge
  * [Revision #3413.67.91](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.91)\
    Fri 2015-01-23 09:13:21 +0100
    * update tokudb version after merge
* [Revision #4584](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4584)\
  Thu 2015-01-22 16:11:03 +0100
  * [MDEV-7491](https://jira.mariadb.org/browse/MDEV-7491): Occasional test failure in innodb.group\_commit\_crash\_no\_optimize\_thread
* [Revision #4583](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4583)\
  Thu 2015-01-22 08:58:13 +0100
  * after merge. innodb/xtradb to work on Windows
* [Revision #4582](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4582) \[merge]\
  Wed 2015-01-21 14:58:41 +0100
  * connect merge
  * [Revision #4439.1.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.32)\
    Tue 2015-01-20 11:26:03 +0100
    * Last revision was to add the JSON table type. This one adds a sort on the multiple table result to obtain the same result on Windows and Linux (because files can be retrieved in a different order)
  * [Revision #4439.1.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.31) \[merge]\
    Tue 2015-01-20 01:21:56 +0100
    * Fix compile errors and warnings of LINUX G++
    * [Revision #4439.3.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.3.2)\
      Mon 2015-01-19 18:55:25 +0100
      * Adding the JSON table type
    * [Revision #4439.3.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.3.1)\
      Sat 2015-01-17 12:19:06 +0100
      * Fix two bugs concerning Discovery of CSV tables: Sep\_char default is now ',' like when discovery is not used If data\_charset is UTF8, column names retrieved from the header are no longer converted to UTF8 considering they already are ([MDEV-7421](https://jira.mariadb.org/browse/MDEV-7421))
  * [Revision #4439.1.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.30)\
    Sat 2015-01-17 11:54:41 +0100
    * Fix two bugs concerning Discovery of CSV tables: Sep\_char default is now ',' like when discovery is not used If data\_charset is UTF8, column names retrieved from the header are no longer converted to UTF8 considering they already are.
  * [Revision #4439.1.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.29)\
    Tue 2015-01-13 17:24:31 +0100
    * Add ConnectTimout and QueryTimout options for ODBC tables. Should fix [MDEV-7415](https://jira.mariadb.org/browse/MDEV-7415). (To be specified in option\_list)
  * [Revision #4439.1.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.28)\
    Fri 2015-01-09 23:36:50 +0100
    * Fix [MDEV-7427](https://jira.mariadb.org/browse/MDEV-7427) by not reallocating the date format in ScanRecord on each inserted row.
  * [Revision #4439.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.27)\
    Tue 2015-01-06 11:32:40 +0100
    * Typo to eliminate some GCC warnings
  * [Revision #4439.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.26)\
    Tue 2015-01-06 10:18:04 +0100
    * Set connection charset before calling mysql\_real\_connect for MYSQL tables. This should fix bug [MDEV-7343](https://jira.mariadb.org/browse/MDEV-7343).
  * [Revision #4439.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.25)\
    Sun 2014-12-14 22:47:12 +0100
    * Temporary fix for [MDEV-7304](https://jira.mariadb.org/browse/MDEV-7304).
  * [Revision #4439.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.24) \[merge]\
    Mon 2014-11-24 20:15:03 +0100
    * Move mktime in TIME\_to\_localtime because on Linux the hour can be modified
    * [Revision #4439.2.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.2.4)\
      Mon 2014-11-24 18:32:44 +0100
      * Make the fix for getting day names of dates more general
    * [Revision #4439.2.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.2.3)\
      Mon 2014-11-24 18:26:44 +0100
      * Enhance the implementation of ODBC tables when using scrollable cursor
    * [Revision #4439.2.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.2.2)\
      Sun 2014-11-23 16:12:26 +0100
      * Fix a bug causing the day always printed as Sunday for date columns with a date format specifying DDD or DDDD.
    * [Revision #4439.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.2.1)\
      Thu 2014-11-20 23:18:51 +0100
      * Remove gcc warning (variable n is set and not used)
  * [Revision #4439.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.23)\
    Thu 2014-11-20 12:57:33 +0100
    * Remove gcc warning on variable n set but not used
  * [Revision #4439.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4439.1.22)\
    Thu 2014-11-20 11:00:02 +0100
    * Implement putting in memory the result set from an ODBC query.
* [Revision #4581](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4581) \[merge]\
  Wed 2015-01-21 14:53:40 +0100
  * P\_S 5.6.22
  * [Revision #0.63.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.63.6)\
    Mon 2015-01-19 00:12:51 +0100
    * 5.6.22
* [Revision #4580](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4580) \[merge]\
  Wed 2015-01-21 14:34:58 +0100
  * XtraDB 5.6.22-71.0
  * [Revision #0.12.74](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.74)\
    Mon 2015-01-19 00:15:29 +0100
    * 5.6.22-71.0
* [Revision #4579](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4579) \[merge]\
  Wed 2015-01-21 14:33:39 +0100
  * InnoDB 5.6.22
  * [Revision #0.49.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.49.8)\
    Mon 2015-01-19 00:11:05 +0100
    * 5.6.22
* [Revision #4578](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4578)\
  Wed 2015-01-21 14:02:26 +0100
  * after-merge fixes
* [Revision #4577](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4577) \[merge]\
  Wed 2015-01-21 12:03:02 +0100
  * 5.5 merge
  * [Revision #3413.67.90](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.90)\
    Mon 2015-01-19 17:31:59 +0100
    * [MDEV-6671](https://jira.mariadb.org/browse/MDEV-6671) mysql\_server\_end breaks OpenSSL
  * [Revision #3413.67.89](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.89)\
    Mon 2015-01-19 17:18:24 +0100
    * [MDEV-6220](https://jira.mariadb.org/browse/MDEV-6220) mysqldump will not backup database with --flush-logs parameter and log\_error my.cnf parameter defined
  * [Revision #3413.67.88](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.88)\
    Mon 2015-01-19 16:41:37 +0100
    * [MDEV-7226](https://jira.mariadb.org/browse/MDEV-7226) sql-bench test-table-elimination does not execute
  * [Revision #3413.67.87](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.87)\
    Mon 2015-01-19 16:29:18 +0100
    * [MDEV-7475](https://jira.mariadb.org/browse/MDEV-7475) Wrong implementation of checking PLUGIN\_VAR\_SET condition
  * [Revision #3413.67.86](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.86)\
    Mon 2015-01-19 16:28:58 +0100
    * [MDEV-7294](https://jira.mariadb.org/browse/MDEV-7294) MTR does not use /dev/shm with a out-of-source build
  * [Revision #3413.67.85](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.85)\
    Fri 2015-01-16 18:13:02 +0100
    * [MDEV-6347](https://jira.mariadb.org/browse/MDEV-6347) Build RHEL7 packages
  * [Revision #3413.67.84](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.84)\
    Fri 2015-01-16 17:54:00 +0100
    * restore an incorrectly merged line
  * [Revision #3413.67.83](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.83)\
    Wed 2015-01-14 17:50:38 +0400
    * [MDEV-7448](https://jira.mariadb.org/browse/MDEV-7448) - mtr may leave stale mysqld
  * [Revision #3413.67.82](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.82)\
    Wed 2015-01-14 18:24:23 -0500
    * [MDEV-7368](https://jira.mariadb.org/browse/MDEV-7368) : SLES: Failed to start mysql.service: Unit mysql.service failed to load
  * [Revision #3413.67.81](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.81)\
    Wed 2015-01-14 12:10:13 +0100
    * [MDEV-7404](https://jira.mariadb.org/browse/MDEV-7404) REPAIR multiple tables crash in MDL\_ticket::has\_stronger\_or\_equal\_type
  * [Revision #3413.67.80](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.80) \[merge]\
    Tue 2015-01-13 23:44:32 +0100
    * TokuDB 7.5.4
  * [Revision #3413.67.79](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.79)\
    Tue 2015-01-13 19:28:03 +0100
    * cleanup
  * [Revision #3413.67.78](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.78)\
    Tue 2015-01-13 19:27:28 +0100
    * [MDEV-7333](https://jira.mariadb.org/browse/MDEV-7333) "'show table status like 'table\_name'" on tokudb table lead to MariaDB crash
  * [Revision #3413.67.77](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.77)\
    Sat 2015-01-10 14:07:46 +0100
    * [MDEV-7410](https://jira.mariadb.org/browse/MDEV-7410) Temporary table name conflict between sessions
  * [Revision #3413.67.76](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.76)\
    Tue 2015-01-06 16:32:41 +0100
    * [MDEV-7189](https://jira.mariadb.org/browse/MDEV-7189): main.processlist fails sporadically in buildbot
  * [Revision #3413.67.75](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.75)\
    Sun 2014-12-28 13:24:53 +0200
    * [MDEV-7369](https://jira.mariadb.org/browse/MDEV-7369): MariaDB build fails when XTRADB\_STORAGE\_ENGINE enabled
  * [Revision #3413.67.74](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.74)\
    Tue 2014-12-23 21:21:23 +0400
    * Increased the version number
  * [Revision #3413.67.73](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.73)\
    Sun 2014-12-21 19:23:28 +0100
    * Adding mariadb-version on the view creation to view frm. ([MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916) followup)
  * [Revision #3413.67.72](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.72)\
    Fri 2014-12-19 23:42:22 +0400
    * Fixed yet another compiler warning.
  * [Revision #3413.67.71](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.71)\
    Fri 2014-12-19 23:17:59 +0400
    * Fixed a couple of compiler warnings.
  * [Revision #3413.67.70](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.70) \[merge]\
    Fri 2014-12-19 11:44:03 +0100
    * merge
    * [Revision #3413.68.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.68.1) \[merge]\
      Fri 2014-12-19 11:35:44 +0100
      * mysql-5.5.41 merge
  * [Revision #3413.67.69](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.69) \[merge]\
    Thu 2014-12-18 20:38:47 +0300
    * Merge 5.3 -> 5.5
    * [Revision #2502.594.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.594.5)\
      Thu 2014-12-18 20:06:49 +0300
      * [MDEV-6830](https://jira.mariadb.org/browse/MDEV-6830): Server crashes in best\_access\_path after a sequence of SELECTs ...
  * [Revision #3413.67.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.68)\
    Thu 2014-12-18 00:13:16 +0100
    * [MDEV-7150](https://jira.mariadb.org/browse/MDEV-7150) Wrong auto increment values on INSERT .. ON DUPLICATE KEY UPDATE when the inserted columns include NULL in an auto-increment column
  * [Revision #3413.67.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.67)\
    Wed 2014-12-17 14:38:14 +0100
    * cleanup
  * [Revision #3413.67.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.66)\
    Wed 2014-12-17 14:35:13 +0100
    * [MDEV-6985](https://jira.mariadb.org/browse/MDEV-6985): MariaDB crashes on stored procedure call
  * [Revision #3413.67.65](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.65)\
    Tue 2014-12-16 15:33:13 +0400
    * DEV-7221 from\_days fails after null value
  * [Revision #3413.67.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.64)\
    Mon 2014-12-15 17:13:47 +0200
    * [MDEV-6855](https://jira.mariadb.org/browse/MDEV-6855) Assertion \`cond\_type == Item::FUNC\_ITEM' failed in check\_group\_min\_max\_predicates with GROUP BY, aggregate in WHERE SQ, multi-part key
  * [Revision #3413.67.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.63)\
    Mon 2014-12-15 14:49:23 +0200
    * [MDEV-4010](https://jira.mariadb.org/browse/MDEV-4010) Deadlock on concurrent INSERT .. SELECT into an Aria table with statement binary logging There was a bug in lock handling when mixing INSERT ... SELECT on the same table.
  * [Revision #3413.67.62](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.62)\
    Mon 2014-12-15 13:01:11 +0200
    * [MDEV-6896](https://jira.mariadb.org/browse/MDEV-6896) kill user command cause MariaDB crash
  * [Revision #3413.67.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.61)\
    Mon 2014-12-15 11:16:33 +0200
    * [MDEV-6871](https://jira.mariadb.org/browse/MDEV-6871) Multi-value insert on MyISAM table that makes slaves crash (when using --skip-external-locking=0) Problem was that repair() did lock and unlock tables, which leaved already locked tables in wrong state
  * [Revision #3413.67.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.60)\
    Fri 2014-12-12 17:10:51 -0500
    * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Addendum, update company name in copyright notice
  * [Revision #3413.67.59](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.59)\
    Fri 2014-12-12 10:38:19 -0500
    * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Update company name
  * [Revision #3413.67.58](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.58)\
    Mon 2014-12-01 14:58:29 +0400
    * [MDEV-7148](https://jira.mariadb.org/browse/MDEV-7148) - Recurring: InnoDB: Failing assertion: !lock->recursive
  * [Revision #3413.67.57](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.57)\
    Wed 2014-12-03 13:38:39 +0200
    * [MDEV-7252](https://jira.mariadb.org/browse/MDEV-7252): Test failure on innodb.innodb\_bug12400341 at Windows
  * [Revision #3413.67.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.56)\
    Tue 2014-12-02 12:19:29 +0200
    * [MDEV-7243](https://jira.mariadb.org/browse/MDEV-7243): innodb-change-buffer-recovery fails on windows
  * [Revision #3413.67.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.55)\
    Tue 2014-12-02 01:31:49 +0400
    * [MDEV-7169](https://jira.mariadb.org/browse/MDEV-7169): innodb.innodb\_bug14147491 fails in buildbot on Windows
  * [Revision #3413.67.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.54)\
    Tue 2014-11-25 12:04:32 +0200
    * Better comments part 2 with proof and simplified implementation. Thanks to Daniel Black.
  * [Revision #3413.67.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.53)\
    Tue 2014-11-25 08:22:10 +0200
    * Fix typo.
* [Revision #4576](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4576)\
  Mon 2015-01-19 16:30:32 +0100
  * remove incorrect asserts in innodb/xtradb. 0 is a valid file handle value.
* [Revision #4575](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4575)\
  Mon 2015-01-19 16:11:48 +0100
  * [MDEV-5679](https://jira.mariadb.org/browse/MDEV-5679) MariaDB holds stdin open after startup as mysqld
* [Revision #4574](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4574)\
  Mon 2015-01-19 14:32:28 +0100
  * [MDEV-7402](https://jira.mariadb.org/browse/MDEV-7402) 'reset master' hangs, waits for signalled COND\_xid\_list
* [Revision #4573](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4573)\
  Mon 2015-01-19 14:19:14 +0100
  * [MDEV-7299](https://jira.mariadb.org/browse/MDEV-7299) Assertion \`m\_status == DA\_ERROR || m\_status == DA\_OK' fails on concurrent execution of DDL, queries from I\_S, and KILL QUERY
* [Revision #4572](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4572)\
  Mon 2015-01-19 14:19:05 +0100
  * rename st\_my\_thread\_var::opt\_info -> st\_my\_thread\_var::keycache\_link
* [Revision #4571](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4571)\
  Mon 2015-01-19 14:18:55 +0100
  * remove unused st\_my\_thread\_var::cmp\_length
* [Revision #4570](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4570)\
  Mon 2015-01-19 14:18:44 +0100
  * [MDEV-7219](https://jira.mariadb.org/browse/MDEV-7219) SQL\_CALC\_FOUND\_ROWS yields wrong result
* [Revision #4569](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4569)\
  Mon 2015-01-19 14:18:34 +0100
  * [MDEV-7186](https://jira.mariadb.org/browse/MDEV-7186) get\_lock() crashes on Windows, main.sp\_notembedded and main.trigger\_notembedded fail in buildbot
* [Revision #4568](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4568)\
  Mon 2015-01-19 14:07:51 +0100
  * [MDEV-7184](https://jira.mariadb.org/browse/MDEV-7184) main.key\_cache fails in buildbot on Windows 32bit
* [Revision #4567](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4567)\
  Mon 2015-01-19 14:07:41 +0100
  * [MDEV-6728](https://jira.mariadb.org/browse/MDEV-6728) KILL QUERY executed on an idle connection can interrupt the next query
* [Revision #4566](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4566)\
  Mon 2015-01-19 14:07:29 +0100
  * [MDEV-7224](https://jira.mariadb.org/browse/MDEV-7224) OQGraph compile error
* [Revision #4565](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4565)\
  Mon 2015-01-19 14:07:22 +0100
  * mtr+valgrind: fix jemalloc check to work correctly for bundler and system jemalloc
* [Revision #4564](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4564)\
  Mon 2015-01-19 12:39:17 +0200
  * [MDEV-7477](https://jira.mariadb.org/browse/MDEV-7477): Make innochecksum work on compressed tables
* [Revision #4563](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4563)\
  Sun 2015-01-18 20:38:07 +0200
  * Fixed [MDEV-7314](https://jira.mariadb.org/browse/MDEV-7314): Deadlock when doing insert-select with Aria
* [Revision #4562](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4562)\
  Sun 2015-01-18 13:39:59 +0200
  * Return to original stage after mysql\_lock\_tables Stage "Filling schema table" is now properly shown in 'show processlist'
* [Revision #4561](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4561)\
  Sun 2015-01-18 01:54:11 +0400
  * [MDEV-7152](https://jira.mariadb.org/browse/MDEV-7152) Wrong result set for WHERE a='oe' COLLATE utf8\_german2\_ci AND a='oe'
  * The code that tested if `WHERE expr=value AND expr=const` can be rewritten to: `WHERE const=value AND expr=const` was incomplete in case of STRING\_RESULT.
  * Moving the test into a new function, to reduce duplicate code.
* [Revision #4560](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4560)\
  Sat 2015-01-17 16:58:10 +0000
  * [MDEV-7362](https://jira.mariadb.org/browse/MDEV-7362): ANALYZE TABLES crash with table-independent-statistics gathering
* [Revision #4559](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4559)\
  Sat 2015-01-17 17:52:03 +0400
  * [MDEV-7366](https://jira.mariadb.org/browse/MDEV-7366) SELECT 'a' = BINARY 'A' returns 1 (utf8 charset, utf8\_unicode\_ci collation) Fixing a wrong assymetric code in Arg\_comparator::set\_cmp\_func(). It existed for a long time, but showed up in 10.0.14 after the fix for "[MDEV-6666](https://jira.mariadb.org/browse/MDEV-6666) Malformed result for CONCAT(utf8\_column, binary\_string)".
* [Revision #4558](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4558)\
  Sat 2015-01-17 16:10:45 +0400
  * A post-fix for: [MDEV-7254](https://jira.mariadb.org/browse/MDEV-7254) Assigned expression is evaluated twice when updating column TIMESTAMP NOT NULL The test type\_timestamp failed depending on the build machine time zone. Setting a fixed time zone for the test.
* [Revision #4557](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4557)\
  Fri 2015-01-16 12:00:07 +0200
  * [MDEV-7254](https://jira.mariadb.org/browse/MDEV-7254): Assigned expression is evaluated twice when updating column TIMESTAMP NOT NULL
* [Revision #4556](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4556)\
  Fri 2015-01-16 11:26:03 +0200
  * Fix try for Buildbot test failure for tests innodb\_bug12400341 innodb-mdev7046 innodb\_stats\_fetch\_nonexistent
* [Revision #4555](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4555)\
  Thu 2015-01-15 20:15:50 +0400
  * [MDEV-7431](https://jira.mariadb.org/browse/MDEV-7431) main.log\_tables fails sporadically in buildbot
* [Revision #4554](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4554)\
  Thu 2015-01-15 15:55:09 +0100
  * [MDEV-7430](https://jira.mariadb.org/browse/MDEV-7430): rpl.rpl\_gtid\_crash still fails in buildbot
* [Revision #4553](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4553)\
  Wed 2015-01-14 18:26:29 -0500
  * [MDEV-7368](https://jira.mariadb.org/browse/MDEV-7368) : SLES: Failed to start mysql.service: Unit mysql.service failed to load
* [Revision #4552](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4552)\
  Wed 2015-01-14 18:19:05 +0100
  * [MDEV-7467](https://jira.mariadb.org/browse/MDEV-7467): sporadic failure in rpl.rpl\_gtid\_crash
* [Revision #4551](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4551)\
  Tue 2015-01-13 16:48:11 +0200
  * [MDEV-7262](https://jira.mariadb.org/browse/MDEV-7262): innodb.innodb-mdev7046 fail on BuildBot
* [Revision #4550](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4550)\
  Wed 2015-01-07 14:45:39 +0100
  * [MDEV-7326](https://jira.mariadb.org/browse/MDEV-7326): Server deadlock in connection with parallel replication
* [Revision #4549](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4549)\
  Tue 2015-01-06 16:08:42 +0200
  * [MDEV-7403](https://jira.mariadb.org/browse/MDEV-7403): should not pass recv\_writer\_thread\_handle to CloseHandle()
* [Revision #4548](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4548)\
  Tue 2015-01-06 09:52:09 +0100
  * [MDEV-7353](https://jira.mariadb.org/browse/MDEV-7353): rpl\_mdev6386 fails sporadically in buildbot
* [Revision #4547](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4547)\
  Tue 2014-12-30 17:10:54 +0200
  * [MDEV-5539](https://jira.mariadb.org/browse/MDEV-5539) Empty results in UNION with Sphinx engine The bug was fixed by Serg earlier by including Sphinx 2.2.6, but he forgot to update the test case.
* [Revision #4546](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4546)\
  Sun 2014-12-28 13:44:30 +0200
  * [MDEV-7369](https://jira.mariadb.org/browse/MDEV-7369): MariaDB build fails when XTRADB\_STORAGE\_ENGINE enabled
* [Revision #4545](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4545)\
  Fri 2014-12-19 09:25:29 +0200
  * Fixed compiler warnings
* [Revision #4544](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4544)\
  Thu 2014-12-18 11:59:08 +0100
  * [MDEV-7342](https://jira.mariadb.org/browse/MDEV-7342): Test failure in perfschema.setup\_instruments\_defaults
* [Revision #4543](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4543)\
  Fri 2014-12-12 17:13:13 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Addendum, update company name in copyright notice
* [Revision #4542](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4542)\
  Fri 2014-12-12 10:40:27 -0500
  * [MDEV-6891](https://jira.mariadb.org/browse/MDEV-6891): Update company name
* [Revision #4541](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4541)\
  Fri 2014-12-12 14:03:20 +0100
  * Fix typo that breaks compilation on platforms without atomics.
* [Revision #4540](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4540)\
  Wed 2014-12-10 12:12:09 +0200
  * Fix test case to allow success on create table (Windows).
* [Revision #4539](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4539) \[merge]\
  Sun 2014-12-07 21:24:02 +0400
  * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests
  * [Revision #4535.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535.1.8)\
    Fri 2014-12-05 21:38:16 +0400
    * Storage engines tests: ALTER ONLINE works differently for MERGE in 10.0
  * [Revision #4535.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535.1.7)\
    Fri 2014-12-05 14:23:24 +0400
    * Run engines tests for MyISAM and in-built InnoDB
  * [Revision #4535.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535.1.6)\
    Thu 2014-12-04 02:54:42 +0400
    * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 6
  * [Revision #4535.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535.1.5)\
    Thu 2014-12-04 02:17:09 +0400
    * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 5
  * [Revision #4535.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535.1.4)\
    Thu 2014-12-04 02:16:41 +0400
    * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 4
  * [Revision #4535.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535.1.3)\
    Thu 2014-12-04 01:59:25 +0400
    * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 3
  * [Revision #4535.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535.1.2)\
    Thu 2014-12-04 01:52:03 +0400
    * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 2
  * [Revision #4535.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535.1.1)\
    Wed 2014-12-03 19:53:40 +0400
    * [MDEV-7255](https://jira.mariadb.org/browse/MDEV-7255) Failures in engines/\* tests, part 1
* [Revision #4538](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4538)\
  Thu 2014-12-04 14:10:41 +0200
  * Add possibility to success on Windows.
* [Revision #4537](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4537)\
  Tue 2014-12-02 13:26:45 +0200
  * [MDEV-7242](https://jira.mariadb.org/browse/MDEV-7242): innodb.innodb-mdev7046 fails in various ways on buildbot
* [Revision #4536](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4536)\
  Wed 2014-12-03 15:49:31 +0100
  * [MDEV-4393](https://jira.mariadb.org/browse/MDEV-4393): show\_explain.test times out randomly
* [Revision #4535](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4535)\
  Tue 2014-12-02 20:35:45 +0100
  * put at least some output-generating statement in the test
* [Revision #4534](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4534)\
  Tue 2014-12-02 19:15:16 +0100
  * fix include/not\_embedded.inc to be independent from the environment
* [Revision #4533](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4533)\
  Tue 2014-12-02 18:11:05 +0100
  * [MDEV-7251](https://jira.mariadb.org/browse/MDEV-7251): Test failure in rpl.rpl\_parallel
* [Revision #4532](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4532)\
  Tue 2014-12-02 12:11:07 +0100
  * Fix wording in error log message, to be consistent with other messages ("IO thread" -> "I/O thread").
* [Revision #4531](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4531)\
  Tue 2014-12-02 12:10:21 +0100
  * [MDEV-7236](https://jira.mariadb.org/browse/MDEV-7236): rpl.rpl\_gtid\_basic failed in buildbot with wait\_condition timeout
* [Revision #4530](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4530)\
  Tue 2014-12-02 09:27:22 +0100
  * [MDEV-7241](https://jira.mariadb.org/browse/MDEV-7241): rpl.rpl\_parallel2 fails sporadically in buildbot
* [Revision #4529](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4529)\
  Mon 2014-12-01 23:56:36 +0100
  * add a proper cleanup to innodb.innodb-mdev7046 test
* [Revision #4528](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4528)\
  Mon 2014-12-01 22:24:58 +0100
  * remove ssl debugging report\_errors() function that was sometimes destroying the state
* [Revision #4527](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4527)\
  Mon 2014-12-01 15:35:01 +0100
  * tests that require server restart cannot be run with --embedded
* [Revision #4526](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4526)\
  Mon 2014-12-01 14:38:41 +0100
  * bump the version
* [Revision #4525](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4525)\
  Mon 2014-12-01 13:52:49 +0100
  * test failure: make list\_files more selective to prevent db.opt from showing up
* [Revision #4524](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4524)\
  Sat 2014-11-22 18:43:53 +0100
  * silence stderr correctly
* [Revision #4523](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4523)\
  Sat 2014-11-22 11:56:29 +0100
  * [MDEV-7144](https://jira.mariadb.org/browse/MDEV-7144) Warnings "bytes lost" during server shutdown after running connect.part\_file test in buildbot
* [Revision #4522](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4522)\
  Mon 2014-12-01 13:53:57 +0100
  * [MDEV-7237](https://jira.mariadb.org/browse/MDEV-7237): Parallel replication: incorrect relaylog position after stop/start the slave
* [Revision #4521](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4521)\
  Fri 2014-11-28 18:11:58 +0400
  * [MDEV-7149](https://jira.mariadb.org/browse/MDEV-7149) Constant propagation erroneously applied for LIKE Simply disallowing equality propagation into LIKE. A more delicate fix is be possible, but it would need too many changes, which is not desirable in 10.0 at this point.
* [Revision #4520](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4520)\
  Thu 2014-11-27 09:34:41 +0100
  * [MDEV-7037](https://jira.mariadb.org/browse/MDEV-7037): [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) does not build on Debian / kfreebsd-i386/amd64 due to MTR failure: multi\_source.gtid [MDEV-7106](https://jira.mariadb.org/browse/MDEV-7106): Sporadic test failure in multi\_source.gtid [MDEV-7153](https://jira.mariadb.org/browse/MDEV-7153): Yet another sporadic failure of multi\_source.gtid in buildbot
* [Revision #4519](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4519)\
  Thu 2014-11-27 11:47:22 +0400
  * Backporting a cleanup in boolean function from 10.1: Moving Item\_bool\_func2 and Item\_func\_opt\_neg from Item\_int\_func to Item\_bool\_func. Now all functions that return is\_bool\_func()=true have a common root class Item\_bool\_func. This change is needed to fix [MDEV-7149](https://jira.mariadb.org/browse/MDEV-7149) properly.
* [Revision #4518](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4518)\
  Wed 2014-11-26 16:41:28 +0200
  * Better comments part 2 with proof and simplified implementation. Thanks to Daniel Black.
* [Revision #4517](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4517)\
  Wed 2014-11-26 14:33:55 +0200
  * [MDEV-7214](https://jira.mariadb.org/browse/MDEV-7214): Test failure in main.partition\_innodb
* [Revision #4516](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4516)\
  Wed 2014-11-26 11:07:32 +0100
  * [MDEV-6582](https://jira.mariadb.org/browse/MDEV-6582): DEBUG\_SYNC does not reset mysys\_var->current\_mutex, causes assertion "Trying to unlock mutex that wasn't locked"
* [Revision #4515](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4515)\
  Tue 2014-11-25 14:19:11 +0100
  * [MDEV-7179](https://jira.mariadb.org/browse/MDEV-7179): rpl.rpl\_gtid\_crash failed in buildbot with Warning: database page corruption or a failed
* [Revision #4514](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4514)\
  Tue 2014-11-25 12:19:48 +0100
  * [MDEV-6903](https://jira.mariadb.org/browse/MDEV-6903): gtid\_slave\_pos is incorrect after master crash
* [Revision #4513](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4513)\
  Tue 2014-11-25 11:38:01 +0200
  * [MDEV-7046](https://jira.mariadb.org/browse/MDEV-7046): MySQL#74480 - Failing assertion: os\_file\_status(newpath, \&exists, \&type) after Operating system error number 36 in a file operation.
* [Revision #4512](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4512) \[merge]\
  Tue 2014-11-25 08:31:03 +0200
  * Better comments and add a test case.
  * [Revision #3413.67.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.67.52)\
    Tue 2014-11-25 08:06:41 +0200
    * Better comments and add a test case.
* [Revision #4511](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4511)\
  Mon 2014-11-24 20:35:02 +0200
  * [MDEV-7183](https://jira.mariadb.org/browse/MDEV-7183): innodb-wl5522-debug-zip fails in buildbot on Windows
* [Revision #4510](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4510)\
  Mon 2014-11-24 20:25:17 +0200
  * [MDEV-7169](https://jira.mariadb.org/browse/MDEV-7169): innodb.innodb\_bug14147491 fails in buildbot on Windows
* [Revision #4509](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4509)\
  Mon 2014-11-24 19:37:38 +0200
  * [MDEV-7168](https://jira.mariadb.org/browse/MDEV-7168): Tests innodb.innodb\_stats\_create\_table innodb.innodb\_stats\_drop\_locked fail and innodb.innodb\_stats\_fetch\_nonexistent fails in buildbot on Windows
* [Revision #4508](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4508)\
  Mon 2014-11-24 15:26:47 +0200
  * [MDEV-7164](https://jira.mariadb.org/browse/MDEV-7164): innodb.innodb-alter-table-disk-full fails in buildbot on Windows
* [Revision #4507](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4507)\
  Mon 2014-11-24 02:53:45 +0400
  * [MDEV-7157](https://jira.mariadb.org/browse/MDEV-7157) plugins.server\_audit fails sporadically in buildbot. Records can get to the different place in the log when multiple thread are logged. So the delay added to let the record be saved on the same place.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
