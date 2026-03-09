# MariaDB 10.0.4 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.4) |[Release Notes](../../old-releases/10.0/10.0.4.md) |**Changelog** |[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 16 Aug 2013

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.4.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3801](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3801)\
  Thu 2013-08-15 18:15:32 +0400
  * [MDEV-4897](https://jira.mariadb.org/browse/MDEV-4897) - Assertion '`share->tdc.prev == 0 && share->tdc.next == 0`' failed in `TABLE_SHARE*` `tdc_acquire_share(THD*`, `const char*`, `const char*`, `const char*`, `uint`, `uint`, `TABLE)`
* [Revision #3800](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3800)\
  Thu 2013-08-15 16:45:29 +0400
  * [MDEV-4864](https://jira.mariadb.org/browse/MDEV-4864) - Merge tests for EXCHANGE PARTITION feature
* [Revision #3799](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3799)\
  Thu 2013-08-15 15:32:18 +0400
  * An additional test for [MDEV-4871](https://jira.mariadb.org/browse/MDEV-4871) Temporal literals do not accept nanoseconds
* [Revision #3798](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3798)\
  Thu 2013-08-15 15:24:34 +0400
  * [MDEV-4871](https://jira.mariadb.org/browse/MDEV-4871) Temporal literals do not accept nanoseconds
* [Revision #3797](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3797)\
  Thu 2013-08-15 10:47:18 +0200
  * fix tests that were relying on @@have\_partitioning
* [Revision #3796](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3796) \[merge]\
  Thu 2013-08-15 13:31:49 +0400
  * Merge with 10.0-connect
  * [Revision #3763.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.23)\
    Wed 2013-08-14 16:07:32 +0200
    * Change the Blanks parameter from true to false in catalog getting information function. This solve the problem of uninitialised zone that was detected by valgrind.
  * [Revision #3763.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.22)\
    Tue 2013-08-13 18:53:14 +0200
    * FIX [MDEV-4853](https://jira.mariadb.org/browse/MDEV-4853) + another bug causing the whole section to be deleted when deleting one key of a INI table with layout=Row. The same happens for layout=column but this is normal as one line is one section.
  * [Revision #3763.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.21)\
    Mon 2013-08-12 21:51:56 +0200
    * Fix [MDEV-4878](https://jira.mariadb.org/browse/MDEV-4878). Table locking is now supported.
  * [Revision #3763.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.20)\
    Sun 2013-08-11 17:46:59 +0200
    * Fix [MDEV-4494](https://jira.mariadb.org/browse/MDEV-4494). Suppress the flag HA\_NULL\_IN\_KEY.
  * [Revision #3763.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.19)\
    Sun 2013-08-11 14:21:38 +0200
    * Fix [MDEV-4881](https://jira.mariadb.org/browse/MDEV-4881). SQL\_TYPE\_DECIMAL was not recognized in ha\_connect::GetColumnOption.
    * Crash on second SELECT was because tshp was not reset to NULL in case of error.
  * [Revision #3763.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.18)\
    Fri 2013-08-09 18:53:40 +0200
    * Better message for CONNECT unspported commands
  * [Revision #3763.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.17)\
    Fri 2013-08-09 18:02:47 +0200
    * Implement the SERVID special columns. This imply modifying the way special columns are processed. This will be documented. Also some code cleanup and some changes to prepare the indexing of nullable columns (not achieve yet)
  * [Revision #3763.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.16)\
    Tue 2013-08-06 12:17:11 +0200
    * Issue a warning instead of an error when inserting in release built a value concerning a nullable column wrongly created as indexed ([MDEV-4494](https://jira.mariadb.org/browse/MDEV-4494))
  * [Revision #3763.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.15)\
    Mon 2013-07-29 12:26:08 +0200
    * Just update the version number and date
  * [Revision #3763.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.14)\
    Fri 2013-07-26 15:33:03 +0200
    * Restore comment handling commented out in R3772. Should be fixed by R3776
  * [Revision #3763.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.13)\
    Fri 2013-07-26 09:52:16 +0200
    * Restrict memcpy length in CHRBLK::SetValue
  * [Revision #3763.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.12)\
    Fri 2013-07-26 00:11:48 +0200
    * Fix length when TYPVAL::SetValue\_char is called from MYSQLCOL::ReadColumn.
  * [Revision #3763.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.11)\
    Thu 2013-07-25 21:14:49 +0200
    * Restore test results to the discovery old way. (when using NEW\_WAY, show create table displays table types unquoted)
  * [Revision #3763.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.10)\
    Thu 2013-07-25 19:15:07 +0200
    * Restore tests to handle the cases that were giving Valgrind warnings.
  * [Revision #3763.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.9)\
    Thu 2013-07-25 19:09:46 +0200
    * Fix a few test in TYPVAL that cause Valgrind warnings
  * [Revision #3763.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.8)\
    Thu 2013-07-25 19:05:57 +0200
    * Modify discovery to test a new way of adding columns. Currently the old way is still used if NEW\_WAY is not defined.
  * [Revision #3763.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.7)\
    Sat 2013-07-20 19:22:12 +0200
    * Fix bug causing connect\_assisted\_discovery to fail on some table types (WMI). In add\_field a decimal value could be specified for columns not being DOUBLE.
  * [Revision #3763.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.6)\
    Fri 2013-07-12 11:25:01 +0200
    * CONNECT not should use query cache because working on external data prone to be modified out of MariaDB
  * [Revision #3763.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.5)\
    Fri 2013-07-12 11:18:54 +0200
    * Fix "Result content mismatch"
  * [Revision #3763.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.4)\
    Thu 2013-07-11 17:45:31 +0200
    * Applying temporary restrictions to test files. This is to suppress some valgrind warnings and consist principally in:
      1. Not supporting connect\_assisted\_discovery to all PROXY based table types
      2. Not supporting the PIVOT table type
    * This temporarily until the valgrind errors/warnings are fixed
  * [Revision #3763.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.3)\
    Thu 2013-07-11 17:44:15 +0200
    * cleaning code and show some functions return code
* [Revision #3795](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3795)\
  Wed 2013-08-14 18:56:41 +0200
  * raise a version
* [Revision #3794](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3794)\
  Wed 2013-08-14 12:50:17 +0400
  * Adjusted test results after recent changes.
* [Revision #3793](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3793)\
  Wed 2013-08-14 12:48:50 +0400
  * [MDEV-4702](https://jira.mariadb.org/browse/MDEV-4702) - Reduce usage of LOCK\_open
* [Revision #3792](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3792)\
  Tue 2013-08-13 16:02:10 +0200
  * [MDEV-4492](https://jira.mariadb.org/browse/MDEV-4492) InnoDB generates non-existing link to manual based on the server version
* [Revision #3791](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3791)\
  Tue 2013-08-13 13:35:36 +0200
  * [MDEV-4865](https://jira.mariadb.org/browse/MDEV-4865) Change related to `--log` option/variable was merged partially
* [Revision #3790](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3790)\
  Mon 2013-08-12 22:08:25 +0200
  * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) merge 10.0-monty -> 10.0
* [Revision #3789](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3789)\
  Mon 2013-08-12 22:05:23 +0200
  * cleanup \* use sql\_mode\_for\_dates() where appropriate. \* always specify an argument for sql\_mode\_for\_dates() (future-proof. easier to notice and fix if the caller will start using thd from a local variable or an argument)
* [Revision #3788](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3788)\
  Mon 2013-08-12 21:27:43 +0200
  * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) merge 10.0-monty -> 10.0
* [Revision #3787](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3787)\
  Mon 2013-08-12 21:07:10 +0200
  * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) merge 10.0-monty -> 10.0
* [Revision #3786](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3786)\
  Mon 2013-08-12 20:56:35 +0200
  * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) merge 10.0-monty -> 10.0
* [Revision #3785](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3785)\
  Mon 2013-08-12 18:32:53 +0200
  * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) merge 10.0-monty -> 10.0
* [Revision #3784](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3784)\
  Mon 2013-08-12 16:02:20 +0200
  * don't error out in Sys\_var::global\_value\_ptr(), it's not nice when unconfigured gtid prevents SHOW VARIABLES from working
* [Revision #3783](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3783)\
  Mon 2013-08-12 15:46:35 +0200
  * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) merge 10.0-monty -> 10.0
* [Revision #3782](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3782)\
  Mon 2013-08-12 14:17:51 +0200
  * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) merge 10.0-monty -> 10.0
* [Revision #3781](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3781)\
  Mon 2013-08-12 17:21:52 +0300
  * Fix bug [MDEV-4885](https://jira.mariadb.org/browse/MDEV-4885): When performance schema is disabled, autosized parameters show 18446744073709551615 instead of -1 (patch by Serg)
* [Revision #3780](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3780) \[merge]\
  Thu 2013-08-08 12:05:02 +0400
  * Merge fixes for: [MDEV-4797](https://jira.mariadb.org/browse/MDEV-4797) - Spider crash on show create table spider table and replication multi source to one of the partitions [MDEV-4747](https://jira.mariadb.org/browse/MDEV-4747) - Spider: add missing install\_spider.sql
  * [Revision #3762.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3762.1.4)\
    Wed 2013-07-31 03:14:57 +0900
    * fix for [MDEV-4797](https://jira.mariadb.org/browse/MDEV-4797)
  * [Revision #3762.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3762.1.3)\
    Thu 2013-07-04 02:55:48 +0900
    * change CMakeLists.txt for install install\_spider.sql. [MDEV-4747](https://jira.mariadb.org/browse/MDEV-4747) - Spider: add missing install\_spider.sql
  * [Revision #3762.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3762.1.2)\
    Sat 2013-06-29 11:35:04 +0900
    * move installing sql file into scripts directory
  * [Revision #3762.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3762.1.1)\
    Sat 2013-06-29 02:08:02 +0900
    * add installing sql file
* [Revision #3779](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3779)\
  Thu 2013-08-08 12:03:30 +0400
  * Do not require libssl1.0.0 (not available on all buildbot platforms).
* [Revision #3778](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3778)\
  Wed 2013-08-07 17:08:51 -0700
  * Added missing tests for innodb persistent statistics (from mysql-5.6.10)
* [Revision #3777](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3777)\
  Wed 2013-08-07 13:18:26 -0700
  * Added missing tests for GET DIAGNOSTICS.
* [Revision #3776](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3776) \[merge]\
  Wed 2013-08-07 17:21:37 +0400
  * Merge 10.0-serg -> 10.0
  * [Revision #3773.1.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.47) \[merge]\
    Wed 2013-08-07 19:40:25 +0400
    * Null merge.
  * [Revision #3773.1.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.46)\
    Wed 2013-08-07 15:55:17 +0400
    * Attempt to fix sproadic failures of rpl.rpl\_err\_ignoredtable.
  * [Revision #3773.1.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.45)\
    Wed 2013-08-07 10:57:45 +0400
    * [MDEV-4819](https://jira.mariadb.org/browse/MDEV-4819) Upgrade from MySQL 5.6 does not work
  * [Revision #3773.1.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.44)\
    Tue 2013-08-06 14:02:07 +0400
    * [MDEV-4801](https://jira.mariadb.org/browse/MDEV-4801) - Server crashes in my\_strdup on setting innodb\_ft\_user\_stopword\_table to DEFAULT
  * [Revision #3773.1.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.43)\
    Mon 2013-08-05 13:52:53 -0700
    * Fixed a valgrind warning: reverted the change done for WL 4443.
  * [Revision #3773.1.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.42) \[merge]\
    Mon 2013-08-05 07:16:07 -0700
    * Merge.
    * [Revision #3773.4.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.4.1)\
      Wed 2013-07-31 06:45:44 -0700
      * Fixed a wrong merge in prune\_partitions()
  * [Revision #3773.1.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.41)\
    Sun 2013-08-04 23:21:11 +0500
    * valgrind errors in gis.test and funcs\_1.storedproc fixed. Field\_geom::store() should check if the source is it's value.
  * [Revision #3773.1.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.40) \[merge]\
    Fri 2013-08-02 18:14:35 +0400
    * Automatic merge
    * [Revision #3773.3.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.3.1)\
      Fri 2013-08-02 18:12:09 +0400
      * [MDEV-4816](https://jira.mariadb.org/browse/MDEV-4816): rpl.rpl\_trunc\_temp fails in 10.0-serg Temorary fix for a number of replication tests (rpl.rpl\_temp\_table\_mix\_row rpl.rpl\_trunc\_temp rpl.rpl\_current\_user rpl.rpl\_gtid\_master\_promote):
  * [Revision #3773.1.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.39)\
    Fri 2013-08-02 19:52:26 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.38)\
    Fri 2013-08-02 13:36:25 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) merge 10.0-monty > 10.0
  * [Revision #3773.1.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.37)\
    Thu 2013-08-01 22:13:06 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.36)\
    Thu 2013-08-01 17:12:58 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.35)\
    Thu 2013-08-01 16:09:26 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.34)\
    Thu 2013-08-01 16:04:13 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.33)\
    Thu 2013-08-01 16:00:50 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.32)\
    Wed 2013-07-31 16:41:29 +0300
    * Virtual column support for new innodb.
  * [Revision #3773.1.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.31)\
    Wed 2013-07-31 15:04:14 +0200
    * [MDEV-4712](https://jira.mariadb.org/browse/MDEV-4712) : Fix "shutdown" test.
  * [Revision #3773.1.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.30) \[merge]\
    Wed 2013-07-31 15:02:11 +0400
    * Merged fix for uninitialized variables.
    * [Revision #3413.21.295](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.295)\
      Thu 2013-07-18 11:16:18 +0300
      * Fix of using uninitialized variadle.
  * [Revision #3773.1.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.29)\
    Wed 2013-07-31 14:55:54 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.28)\
    Wed 2013-07-31 14:51:25 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.27)\
    Tue 2013-07-30 23:42:16 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.26)\
    Tue 2013-07-30 17:54:40 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.25)\
    Tue 2013-07-30 17:50:48 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.24)\
    Tue 2013-07-30 17:47:53 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.23)\
    Mon 2013-07-29 18:08:49 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.22)\
    Sat 2013-07-27 17:04:57 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.21)\
    Fri 2013-07-26 18:48:06 -0700
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.20)\
    Fri 2013-07-26 23:02:48 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.19)\
    Fri 2013-07-26 16:03:56 +0500
    * main.gis test fixed.
  * [Revision #3773.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.18)\
    Fri 2013-07-26 13:11:43 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.17)\
    Fri 2013-07-26 13:04:59 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.16)\
    Thu 2013-07-25 13:42:06 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.15)\
    Thu 2013-07-25 13:40:18 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.14)\
    Thu 2013-07-25 13:37:30 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.13) \[merge]\
    Wed 2013-07-24 14:45:47 +0400
    * Automatic merge
    * [Revision #3773.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.2.1)\
      Wed 2013-07-24 14:43:57 +0400
      * Alternative fix for failure in filesort\_debug.test. - Make THD::raise\_condition() call push\_warning() after set\_error\_status() call. (they seem to have accidentally exchanged in this merge cset: sergii@pisem.net-20130721143919-7cltcw2l9g29f983) - Rollback the patch from two csets before (the one with comment: Update filesort\_debug.test (see comment #1 in [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) for analysis))
  * [Revision #3773.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.12)\
    Wed 2013-07-24 16:51:48 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.11)\
    Wed 2013-07-24 16:48:23 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.10)\
    Wed 2013-07-24 16:45:24 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty - 10.0
  * [Revision #3773.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.9)\
    Wed 2013-07-24 12:35:18 +0400
    * Fix testsuite: update tests for `mysql-test/t/system_mysql_db_fix*`
    * As of 10.0.2, MariaDB has mysql.gtid\_slave\_pos table as system table.
  * [Revision #3773.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.8)\
    Wed 2013-07-24 10:05:12 +0400
    * Update filesort\_debug.test (see comment #1 in [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) for analysis)
  * [Revision #3773.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.7)\
    Tue 2013-07-23 18:29:16 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty → 10.0
  * [Revision #3773.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.6)\
    Tue 2013-07-23 18:03:23 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty → 10.0
  * [Revision #3773.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.5)\
    Tue 2013-07-23 17:38:44 +0400
    * [MDEV-4786](https://jira.mariadb.org/browse/MDEV-4786) - merge 10.0-monty → 10.0
  * [Revision #3773.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.4)\
    Tue 2013-07-23 17:22:02 +0400
    * MDEV4786 - merge 10.0-monty → 10.0
  * [Revision #3773.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.3)\
    Sun 2013-07-21 19:24:20 +0200
    * more post-merge fixes: \* update results \* don't force HA\_CREATE\_DELAY\_KEY\_WRITE on all temp tables, (bad for CREATE ... LIKE) instead imply it in myisam/aria \* restore HA\_ERR\_TABLE\_DEF\_CHANGED in archive \* increase the default number of rwlock classes in P\_S to fit all our rwlocks
  * [Revision #3773.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.2)\
    Sun 2013-07-21 16:43:42 +0200
    * cosmetic fixes
  * [Revision #3773.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773.1.1) \[merge]\
    Sun 2013-07-21 16:39:19 +0200
    * 10.0-monty merge
    * [Revision #3492.3.135](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.135)\
      Wed 2013-07-17 18:51:12 +0200
      * merge few bug fixes from 5.6
    * [Revision #3492.3.134](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.134)\
      Thu 2013-07-18 12:35:00 +0300
      * [MDEV-617](https://jira.mariadb.org/browse/MDEV-617) [Bug #671189](https://bugs.launchpad.net/bugs/671189) - Query cache is not used for tables or databases with dots in their names test suite added to be sure that bug is fixed
    * [Revision #3492.3.133](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.133)\
      Mon 2013-07-15 22:50:06 +0200
      * [MDEV-4757](https://jira.mariadb.org/browse/MDEV-4757) Change mysql.slow\_log.event\_time from TIMESTAMP to TIMESTAMP(6)
    * [Revision #3492.3.132](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.132)\
      Mon 2013-07-15 21:17:08 +0200
      * in field\_conv() don't simply check to->type() == MYSQL\_TYPE\_BLOB, this misses GEOMETRY columns.
    * [Revision #3492.3.131](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.131)\
      Mon 2013-07-15 18:01:22 +0200
      * Fixes for innodb suite, merging tests from 5.6.
    * [Revision #3492.3.130](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.130)\
      Mon 2013-07-15 13:43:15 +0200
      * Fix main test suite on Windows
    * [Revision #3492.3.129](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.129)\
      Mon 2013-07-15 13:42:50 +0200
      * Windows, compilation : restore support for erxceptions (fixes warnings in Innodb code)
    * [Revision #3492.3.128](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.128)\
      Sun 2013-07-14 23:20:25 +0200
      * many simple fixes for innodb suite, merging tests from 5.6
    * [Revision #3492.3.127](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.127)\
      Sun 2013-07-14 19:44:37 +0200
      * fix pfs\_digest\* tests.
    * [Revision #3492.3.126](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.126)\
      Sun 2013-07-14 13:48:06 +0200
      * parts suite merged
    * [Revision #3492.3.125](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.125)\
      Sat 2013-07-13 22:29:30 +0200
      * update results
    * [Revision #3492.3.124](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.124)\
      Sat 2013-07-13 22:29:17 +0200
      * fix for maria.maria test
    * [Revision #3492.3.123](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.123)\
      Sat 2013-07-13 22:28:53 +0200
      * update plugin API versions in tests
    * [Revision #3492.3.122](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.122)\
      Sat 2013-07-13 17:48:06 +0200
      * SHA1 service (because mysql\_ssl library is built with -fvisibility=hidden)
    * [Revision #3492.3.121](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.121)\
      Sat 2013-07-13 15:13:24 +0200
      * Fix compiler warning - using "const" twice for CHARSET\_INFO.
    * [Revision #3492.3.120](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.120)\
      Sat 2013-07-13 15:09:47 +0200
      * Fix compile error on Windows.
    * [Revision #3492.3.119](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.119)\
      Sat 2013-07-13 09:22:00 +0200
      * sys\_var suite passes
    * [Revision #3492.3.118](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.118)\
      Fri 2013-07-12 23:07:32 +0200
      * fix the maria suite
    * [Revision #3492.3.117](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.117)\
      Fri 2013-07-12 21:41:20 +0200
      * update handler.\* tests
    * [Revision #3492.3.116](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.116)\
      Fri 2013-07-12 20:48:28 +0200
      * update test results
    * [Revision #3492.3.115](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.115)\
      Fri 2013-07-12 19:58:06 +0200
      * federated.partition test - fix the bad merge
    * [Revision #3492.3.114](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.114)\
      Fri 2013-07-12 17:40:20 +0200
      * binlog\_old\_versions.test
    * [Revision #3492.3.113](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.113)\
      Fri 2013-07-12 16:24:20 +0200
      * archive.test and others
    * [Revision #3492.3.112](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.112)\
      Fri 2013-07-12 16:31:01 +0300
      * now results is correct
    * [Revision #3492.3.111](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.111)\
      Fri 2013-07-12 13:32:37 +0200
      * fix lost vcol checks in sql\_table.cc, remove unused FIELD\_IS\_xxx flags change vcol tests to use innodb, not xtradb.
    * [Revision #3492.3.110](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.110)\
      Fri 2013-07-12 11:36:54 +0200
      * restore ha\_example::check\_if\_incompatible\_data(), create\_info->fields\_option\_struct, create\_info->indexes\_option\_struct lost in the merge. add test cases.
    * [Revision #3492.3.109](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.109)\
      Thu 2013-07-11 21:23:55 +0300
      * Merge the following patch from MySQL 5.6.10, in order to make perfschema.binlog\_\* tests work.
    * [Revision #3492.3.108](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.108)\
      Fri 2013-07-12 10:21:14 +0200
      * fix upgrade.test - update from 5.6
    * [Revision #3492.3.107](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.107)\
      Fri 2013-07-12 10:17:52 +0200
      * merge bugfuxes for sp-error.test
    * [Revision #3492.3.106](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.106)\
      Fri 2013-07-12 09:37:07 +0300
      * changes corresponts to changes in 5.6
    * [Revision #3492.3.105](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.105)\
      Thu 2013-07-11 23:16:33 +0200
      * temporal-related changes. don't apply sql\_mode flags on the lower level (str\_to\_datetime), do it on the upper level, in items that return temporal values.
    * [Revision #3492.3.104](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.104)\
      Thu 2013-07-11 21:56:58 +0200
      * fix truncate\_coverage.test: update from 5.6
    * [Revision #3492.3.103](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.103)\
      Thu 2013-07-11 21:40:30 +0200
      * fix signal\_demo3.test: fix a typo in the merge, and update results to match 5.6
    * [Revision #3492.3.102](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.102)\
      Thu 2013-07-11 18:57:11 +0200
      * fix merge.test: online alter table support for MERGE tables, really
    * [Revision #3492.3.101](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.101)\
      Thu 2013-07-11 16:54:03 +0200
      * fix create.test: update the results, don't restore the incorrectly merged feature. it'll go away in the next 10.0 merge
    * [Revision #3492.3.100](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.100)\
      Thu 2013-07-11 14:10:44 +0200
      * remove unused function
    * [Revision #3492.3.99](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.99)\
      Thu 2013-07-11 14:08:51 +0200
      * fix alter\_table.test: remove old assert as it was removed from 5.6, add extra\_func code from 5.5, that was lost in a merge
    * [Revision #3492.3.98](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.98)\
      Thu 2013-07-11 16:27:57 +0300
      * added lost part about preopened temporary tables
    * [Revision #3492.3.97](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.97)\
      Thu 2013-07-11 12:25:08 +0300
      * [MDEV-4710](https://jira.mariadb.org/browse/MDEV-4710) Merge Performance Schema test cases from MySQL 5.6.10
    * [Revision #3492.3.96](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.96)\
      Wed 2013-07-10 21:19:11 +0200
      * fix cast.test, select.test, select\_jcl6.test: update results after strict\_date\_checking=1
    * [Revision #3492.3.95](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.95)\
      Wed 2013-07-10 20:11:01 +0200
      * fix plugin.test - bad merge in TABLE\_SHARE::destroy, ha\_share must be deleted before the plugin
    * [Revision #3492.3.94](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.94)\
      Wed 2013-07-10 19:22:19 +0200
      * fix func\_time.test - WEEK(), WEEKDAY(), WEEKOFYEAR() must require TIME\_NO\_ZERO\_IN\_DATE
    * [Revision #3492.3.93](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.93)\
      Wed 2013-07-10 19:09:26 +0200
      * fix select\_pkeycache: update results after strict\_date\_checking=1
    * [Revision #3492.3.92](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.92)\
      Wed 2013-07-10 18:58:34 +0200
      * fix status.test - don't use lock\_tables\_precheck() for SHOW PROC STATUS, it shouldn't require LOCK\_TABLE\_ACL
    * [Revision #3492.3.91](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.91)\
      Wed 2013-07-10 17:10:22 +0200
      * fix innodb\_mysql\_sync test - update from 5.6
    * [Revision #3492.3.90](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.90)\
      Wed 2013-07-10 15:23:46 +0200
      * fix flush\_read\_lock - update the test and results form 5.6
    * [Revision #3492.3.89](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.89)\
      Wed 2013-07-10 13:34:07 +0200
      * clearly mark unused error messages as such
    * [Revision #3492.3.88](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.88)\
      Wed 2013-07-10 12:48:56 +0200
      * fix for alter\_table\_online test.
    * [Revision #3492.3.87](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.87)\
      Wed 2013-07-10 15:30:17 +0300
      * [MDEV-4710](https://jira.mariadb.org/browse/MDEV-4710) Merge Performance Schema test cases from MySQL 5.6.10
    * [Revision #3492.3.86](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.86)\
      Tue 2013-07-09 22:36:53 +0200
      * [MDEV-4758](https://jira.mariadb.org/browse/MDEV-4758) 10.0-monty tree: ALTER TABLE CHANGE COLUMN doesn't drop EITS stats
    * [Revision #3492.3.85](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.85)\
      Tue 2013-07-09 22:30:04 +0200
      * cmake: don't check for the compiler on every invocation of RESTRICT\_SYMBOL\_EXPORTS(), do it only once
    * [Revision #3492.3.84](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.84)\
      Tue 2013-07-09 18:43:12 +0200
      * commit\_1innodb.test: update results from 5.6
    * [Revision #3492.3.83](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.83)\
      Tue 2013-07-09 18:09:22 +0200
      * fix mysql\_client\_test failure, sometimes we do warnings differently
    * [Revision #3492.3.82](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.82)\
      Tue 2013-07-09 21:15:01 +0300
      * Cought errors are not shown
    * [Revision #3492.3.81](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.81)\
      Tue 2013-07-09 15:39:57 +0400
      * 10.0-monty: trivial test result updates
    * [Revision #3492.3.80](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.80)\
      Tue 2013-07-09 13:40:26 +0400
      * Trivial test result updates.
    * [Revision #3492.3.79](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.79)\
      Tue 2013-07-09 15:42:36 +0400
      * Fix merge.test failure - Problem: mysql\_admin\_table() calls open\_temporary\_tables(). This causes assertion failure, because mysql\_execute\_command() has already called open\_temporary\_tables() - Solution: call close\_thread\_tables() at the start of mysql\_admin\_table(), like mysql-5.6 does
    * [Revision #3492.3.78](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.78) \[merge]\
      Mon 2013-07-08 22:06:04 -0700
      * Merge
      * [Revision #3492.13.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.13.1) \[merge]\
        Mon 2013-07-08 20:45:02 +0400
        * Automatic merge
        * [Revision #3492.12.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.12.2)\
          Mon 2013-07-08 20:21:27 +0400
          * Fix assert failures in main.merge test (line 234) and main.merge\_mmap (line 44) - After the merge from mysql-5.6, open\_tables() did not call open\_and\_process\_table() for temporary table. The logic was that temporary tables were already opened when mysql\_execute\_command() has called open\_temporary\_tables(). This worked for the most part, except for temporary tables of type MERGE. for which open\_and\_process\_table() must call table->file->extra(HA\_EXTRA\_ADD\_CHILDREN\_LIST). Failure to make this call resulted in crash further in execution.
    * [Revision #3492.3.77](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.77)\
      Mon 2013-07-08 18:35:44 -0700
      * Fixed all remaining failures in partition tests. Commented out the test case for bug 50036 as it was done in mysql-5.6.10.
    * [Revision #3492.3.76](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.76) \[merge]\
      Mon 2013-07-08 12:59:18 -0700
      * Merge
      * [Revision #3492.12.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.12.1)\
        Mon 2013-07-08 18:29:52 +0400
        * More trivial test result updates
    * [Revision #3492.3.75](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.75)\
      Mon 2013-07-08 12:55:11 -0700
      * Fixed a failure in partition\_truncate.test.
    * [Revision #3492.3.74](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.74) \[merge]\
      Mon 2013-07-08 18:15:50 +0400
      * Automatic merge
      * [Revision #3492.11.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.11.1)\
        Mon 2013-07-08 18:14:24 +0400
        * Fix test failure in myisam.test: Put back the code tht produces the warning about "Table storage engine %s does not support the create option 'TRANSACTIONAL=1'"
    * [Revision #3492.3.73](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.73)\
      Mon 2013-07-08 19:11:57 +0300
      * fixed result.
    * [Revision #3492.3.72](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.72) \[merge]\
      Mon 2013-07-08 12:59:50 +0400
      * Automatic merge
      * [Revision #3492.10.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.10.1)\
        Mon 2013-07-08 12:57:58 +0400
        * Fix test errors like: -Note 1031 Table storage engine for 't1' doesn't have this option +Note 1031 Table storage engine for 'InnoDB' doesn't have this option
    * [Revision #3492.3.71](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.71)\
      Mon 2013-07-08 15:19:50 +0300
      * Merge performance schema test cases from MySQL 5.6.10
    * [Revision #3492.3.70](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.70)\
      Mon 2013-07-08 11:16:11 +0400
      * More test result updates: - Update test results for tests using SPs: SPs no longer emit warnings/errors that were caught and handled inside SP
    * [Revision #3492.3.69](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.69)\
      Mon 2013-07-08 13:42:38 +0400
      * More trivial test results updates
    * [Revision #3492.3.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.68)\
      Mon 2013-07-08 09:50:18 +0300
      * The compiler warning about ';' fix.
    * [Revision #3492.3.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.67)\
      Sun 2013-07-07 14:09:52 +0400
      * Update test results to fix trivial test failures in parts testsuite - New error message text - PARTITION is now a reserved word in SQL, so it should be quoted
    * [Revision #3492.3.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.66)\
      Fri 2013-07-05 21:42:06 +0400
      * More buildbot test result updates
    * [Revision #3492.3.65](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.65)\
      Fri 2013-07-05 19:57:48 +0400
      * Post-merge buildbot fixes: Update trivial .reject/.result differences (all checked)
    * [Revision #3492.3.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.64)\
      Fri 2013-07-05 19:40:34 +0400
      * Merge from mysql-5.6 fix for bug#11761752 (was already partially merged)
    * [Revision #3492.3.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.63)\
      Fri 2013-07-05 16:56:05 +0400
      * Test result updates
    * [Revision #3492.3.62](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.62)\
      Fri 2013-07-05 16:45:22 +0400
      * Fix compilation: tests/async\_queries links againist client library, and must use C++ linking due to client library using SSL library, which needs C++ linking
    * [Revision #3492.3.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.61)\
      Fri 2013-07-05 15:25:01 +0400
      * Fix limit\_rows\_examined.test: - Take into account that Dynamic\_array::back() now returns pointer to the last element (it used to return pointer to right after the last element) - Fix error messages merge: ER\_INTERNAL\_ERROR was defined independently by both mysql-5.6 and mariadb-5.5. Switch to their error number, and still support ours for compatibility.
    * [Revision #3492.3.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.60)\
      Fri 2013-07-05 15:20:39 +0400
      * Fix compile error on Windows
    * [Revision #3492.3.59](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.59)\
      Fri 2013-07-05 17:21:14 +0300
      * known results differences
    * [Revision #3492.3.58](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.58)\
      Fri 2013-07-05 17:06:02 +0300
      * fixed result (error message and error message intercepting).
    * [Revision #3492.3.57](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.57)\
      Fri 2013-07-05 16:58:37 +0300
      * fixed opening temporary tables.
    * [Revision #3492.3.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.56)\
      Fri 2013-07-05 14:00:17 +0400
      * Update test result: same as in 10.0 and maria (and mysql) 5.5
    * [Revision #3492.3.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.55)\
      Fri 2013-07-05 13:56:05 +0400
      * Fix trivial compile failures observed in buildbot
    * [Revision #3492.3.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.54)\
      Fri 2013-07-05 14:40:01 +0200
      * Set valid default ("yes") for WITH\_SSL cmake variable on Unixes.
    * [Revision #3492.3.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.53)\
      Fri 2013-07-05 11:23:18 +0400
      * Fix mysqldump.test: update test result
    * [Revision #3492.3.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.52)\
      Fri 2013-07-05 10:52:31 +0400
      * Update test result: PASSWORD(NULL) returns '' now.
    * [Revision #3492.3.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.51)\
      Fri 2013-07-05 10:44:06 +0400
      * More test result updates, follow the previous cset
    * [Revision #3492.3.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.50)\
      Fri 2013-07-05 10:40:45 +0400
      * More test result updates: - strict.test updated (changed back) after the cset with "Fix type\_newdecimal.test ..." two csets ago - row-checksum.test changed the code from HA\_WRONG\_CREATE\_OPTION to ER\_ILLEGAL\_HA\_CREATE\_OPTION, like mysql-5.6 did
    * [Revision #3492.3.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.49)\
      Fri 2013-07-05 10:21:15 +0400
      * Fix a number of tests:
        * MariaDB does not have mysql.slave\_master\_info, mysql.slave\_relay\_log\_info ,mysql.slave\_worker\_info or mysql.ndb\_binlog\_index tables.
        * Some tests expected to have these tables (this was an incorrect merge from 5.6, which merged necessary tables like mysql.innodb\*stats, but also got these tables)
    * [Revision #3492.3.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.48)\
      Fri 2013-07-05 09:53:18 +0400
      * Fix type\_newdecimal.test: Warning was produced instead of NOTE. The cause was typo in the merge.
    * [Revision #3492.3.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.47)\
      Fri 2013-07-05 07:24:04 +0400
      * Fix innodb\_ignore\_builtin.test
    * [Revision #3492.3.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.46) \[merge]\
      Thu 2013-07-04 17:58:39 +0400
      * Automatic merge
      * [Revision #3492.9.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.9.1)\
        Thu 2013-07-04 17:57:42 +0400
        * Update log\_tables.test: some definitions of columns have changed, and slow\_log got 'thread\_id' column.
    * [Revision #3492.3.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.45)\
      Thu 2013-07-04 17:08:15 +0400
      * Update test result for mysql-test/t/ctype\_errors.test (checked)
    * [Revision #3492.3.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.44)\
      Thu 2013-07-04 17:01:36 +0400
      * Fix fix\_priv\_tables.test: make mysql\_system\_tables\_fix.sql to not modify user.password\_expired column.
    * [Revision #3492.3.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.43)\
      Thu 2013-07-04 16:36:43 +0400
      * Fix typo in scripts/mysql\_system\_tables\_fix.sql
    * [Revision #3492.3.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.42) \[merge]\
      Thu 2013-07-04 15:46:53 +0400
      * Automatic merge
      * [Revision #3492.8.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.8.1)\
        Thu 2013-07-04 15:45:58 +0400
        * [MDEV-4756](https://jira.mariadb.org/browse/MDEV-4756): 10.0-monty tree: log\_state.test fails - make the test output stable - make Log\_to\_csv\_event\_handler::log\_slow() to write the value of thd->thread\_id (it didn't, and so 0 was always logged).
    * [Revision #3492.3.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.41)\
      Thu 2013-07-04 15:05:43 +0400
      * Update test results: handlersocket.test (approved by Serg)
    * [Revision #3492.3.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.40)\
      Thu 2013-07-04 09:38:33 +0400
      * Update more test results (all checked).
    * [Revision #3492.3.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.39) \[merge]\
      Thu 2013-07-04 09:11:21 +0400
      * Automatic merge
      * [Revision #3492.7.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.7.1)\
        Thu 2013-07-04 07:21:54 +0400
        * [MDEV-4753](https://jira.mariadb.org/browse/MDEV-4753): partition\_innodb\_stmt reports memory leaks from dict/dict0stats\_bg.cc:69 - Work around the problem by forcing recalc\_pool to free its buffer in dict\_stats\_recalc\_pool\_deinit().
    * [Revision #3492.3.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.38)\
      Thu 2013-07-04 10:39:19 +0300
      * fixed typo.
    * [Revision #3492.3.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.37)\
      Wed 2013-07-03 20:48:41 +0400
      * Fix a number of trivial test failures by updating error message: "Unknown table tbl" is now "Unknown table database.tbl" (part#3)
    * [Revision #3492.3.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.36)\
      Wed 2013-07-03 20:10:51 +0400
      * Cont'd: Fix a number of trivial test failures by updating error message: "Unknown table tbl" is now "Unknown table database.tbl"
    * [Revision #3492.3.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.35) \[merge]\
      Wed 2013-07-03 20:05:05 +0400
      * Automatic merge
      * [Revision #3492.6.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.6.1)\
        Wed 2013-07-03 20:02:48 +0400
        * Fix a number of trivial test failures by updating error message: "Unknown table tbl" is now "Unknown table database.tbl"
    * [Revision #3492.3.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.34) \[merge]\
      Wed 2013-07-03 22:57:13 +0300
      * Automatic merge
      * [Revision #3492.5.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.5.1)\
        Wed 2013-07-03 22:50:34 +0300
        * Fixed issues with partitions and create temporary table SELECT ... Merged all ddl\_logging code. Merged sql\_partition.cc innodb\_mysql\_lock2.test and partition\_cache.test now works. Changed interface to strconvert() to make it easier to use with not \0 terminated strings.
    * [Revision #3492.3.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.33)\
      Wed 2013-07-03 19:42:05 +0400
      * [MDEV-4750](https://jira.mariadb.org/browse/MDEV-4750): (patch#2): undo previous attempts to stabilize persistent table statistics with ANALYZE TABLE commands
    * [Revision #3492.3.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.32) \[merge]\
      Wed 2013-07-03 19:40:40 +0400
      * Merge
      * [Revision #3492.4.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.4.1)\
        Wed 2013-07-03 19:32:58 +0400
        * [MDEV-4750](https://jira.mariadb.org/browse/MDEV-4750): Fix a number of test failures in EXPLAIN outputs caused by weird behavior in innodb's persistent stats - Run the testsuite without innodb persistent stats
    * [Revision #3492.3.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.31)\
      Wed 2013-07-03 22:34:12 +0300
      * [MDEV-4058](https://jira.mariadb.org/browse/MDEV-4058)
    * [Revision #3492.3.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.30)\
      Wed 2013-07-03 14:42:48 +0400
      * Fix test failure in mysql-test/t/type\_bit\_innodb.test - Run ANALYZE TABLE after insert, like mysql-5.6 does.
    * [Revision #3492.3.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.29)\
      Wed 2013-07-03 14:24:56 +0400
      * Fix test failure for join\_outer\_innodb.test: reuse the approach from vasil.dimov@oracle.com-20120521133620-glj6l0ntcsrz0wbl run ANALYZE TABLE.
    * [Revision #3492.3.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.28)\
      Wed 2013-07-03 12:19:03 +0300
      * [MDEV-4058](https://jira.mariadb.org/browse/MDEV-4058)
    * [Revision #3492.3.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.27)\
      Thu 2013-06-27 12:51:34 +0300
      * [MDEV-4058](https://jira.mariadb.org/browse/MDEV-4058)
    * [Revision #3492.3.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.26)\
      Wed 2013-07-03 10:22:19 +0300
      * ps\_ddl1.test fix
    * [Revision #3492.3.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.25)\
      Wed 2013-07-03 10:19:47 +0300
      * ps.test fixed
    * [Revision #3492.3.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.24)\
      Wed 2013-07-03 10:18:22 +0300
      * ps\_1general fixed.
    * [Revision #3492.3.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.23)\
      Tue 2013-07-02 22:11:12 +0300
      * strict.test now works.
    * [Revision #3492.3.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.22)\
      Tue 2013-07-02 20:43:35 +0300
      * mdl\_sync now works.
    * [Revision #3492.3.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.21)\
      Tue 2013-07-02 16:44:53 +0300
      * Pull of revision 3313 (Pre-requisite patch for Bug#11763162 (55843 - Handled condition appears as not handled) fixed.
    * [Revision #3492.3.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.20)\
      Mon 2013-07-01 11:31:18 +0300
      * correct result of the ps.tset
    * [Revision #3492.3.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.19)\
      Fri 2013-06-28 01:53:41 +0300
      * Fixed some wrong format strings. Fixed OPTIMIZE with innodb
    * [Revision #3492.3.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.18)\
      Thu 2013-06-27 17:42:18 +0300
      * merge of 2876.430.11 & 2876.430.1 CF\_PREOPEN\_TMP\_TABLES & CF\_HA\_CLOSE & Patch for Bug#11746602 (27480: Extend CREATE TEMPORARY TABLES privilege to allow temp table operations).
    * [Revision #3492.3.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.17)\
      Thu 2013-06-27 14:01:03 +0300
      * ha\_partition.cc and ha\_partition.h are now completely merged Added sql\_mode\_t to simplify merges
    * [Revision #3492.3.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.16)\
      Wed 2013-06-26 13:17:27 +0300
      * A fix of unions with duplicate rows and returning bug fix for [Bug #732124](https://bugs.launchpad.net/bugs/732124) union + limit returns wrong result
    * [Revision #3492.3.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.15)\
      Tue 2013-06-25 18:55:12 -0700
      * Some corrections of the merge for the partition code.
    * [Revision #3492.3.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.14)\
      Sun 2013-06-23 12:15:43 +0300
      * Added option to avoid warnings from innodb
    * [Revision #3492.3.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.13)\
      Sat 2013-06-22 18:47:12 +0300
      * Don't update table and index statics for temporary tables Fixed type and testing of last\_update type for innodb\_table\_stats
    * [Revision #3492.3.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.12)\
      Fri 2013-06-21 15:17:48 +0300
      * Case when we close temporary table which was not opened in its engine (ALTER TABLE) fixed.
    * [Revision #3492.3.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.11)\
      Thu 2013-06-20 14:49:25 +0300
      * Fixed memory leaks. alias.test now runs clean with valgrind
    * [Revision #3492.3.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.10)\
      Wed 2013-06-19 22:57:46 +0300
      * Fixed some memory leaks Disabled some asserts that we can't yet have enabled
    * [Revision #3492.3.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.9)\
      Wed 2013-06-19 14:32:14 +0300
      * Finished merging wl5986 started by Igor.
    * [Revision #3492.3.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.8)\
      Tue 2013-06-18 02:01:34 +0300
      * Fixed some merge issues: - temporary tables now works - mysql-system\_tables updated to not use temporary tables - PASSWORD() function fixed - Support for STATS\_AUTO\_RECALC, STATS\_PERSISTENT and STATS\_SAMPLE\_PAGES table options
    * [Revision #3492.3.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.7)\
      Mon 2013-06-17 13:34:54 +0300
      * Debugging output fixed to make finding executing commands easy.
    * [Revision #3492.3.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.6)\
      Mon 2013-06-17 09:14:58 +0300
      * Cassandra SE build fix for merge.
    * [Revision #3492.3.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.5)\
      Sun 2013-06-16 21:26:40 +0300
      * More merge fixes:
        * mdl.cc and mdl.h merged completely
        * mysql\_system\_tables\*.sql merged completely
        * Fixed wrong merge of lock\_tables
      * Added some missing functions:
        * bool THD::notify\_shared\_lock()
        * Dynamic\_array::pop, Dynamic\_array::del
        * Added MDL\_context\_owner to THD
        * Added metadata\_locks\_hash\_instances
    * [Revision #3492.3.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.4)\
      Sat 2013-06-15 23:01:01 +0300
      * Fixed patch that was part of last push that didn't apply correctly.
    * [Revision #3492.3.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.3)\
      Sat 2013-06-15 18:32:08 +0300
      * Applied all changes from Igor and Sanja
    * [Revision #3492.3.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.2)\
      Tue 2013-05-21 22:00:08 +0300
      * Push a lot of small fixes to get larger parts to compile
    * [Revision #3492.3.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3492.3.1)\
      Tue 2013-03-26 00:03:13 +0200
      * Temporary commit of 10.0-merge
* [Revision #3775](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3775)\
  Wed 2013-08-07 17:20:22 +0400
  * Better comments
* [Revision #3774](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3774)\
  Thu 2013-08-01 17:03:15 +0400
  * Merging my\_convert() from 10.0-serg
* [Revision #3773](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3773) \[merge]\
  Thu 2013-07-18 16:46:57 +0200
  * 10.0-base merge
  * [Revision #3427.1.245](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.245) \[merge]\
    Wed 2013-07-17 21:24:29 +0200
    * 5.5 merge
    * [Revision #3413.21.294](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.294)\
      Wed 2013-07-17 17:03:59 +0300
      * Revert of marko.makela@oracle.com-20130430103950-j353faze84zzk9xf for xtradb (fix of [MySQL Bug #69623](https://bugs.mysql.com/bug.php?id=69623))
    * [Revision #3413.21.293](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.293)\
      Wed 2013-07-17 16:42:13 +0300
      * Fix for [MDEV-4219](https://jira.mariadb.org/browse/MDEV-4219) A simple select query returns random data (upstream bug#68473)
    * [Revision #3413.21.292](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.292) \[merge]\
      Tue 2013-07-16 19:30:39 +0200
      * merge Percona-Server-5.5.32-rel31.0.tar.gz
      * [Revision #0.12.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.63)\
        Tue 2013-07-16 14:55:47 +0200
        * Percona-Server-5.5.32-rel31.0.tar.gz
    * [Revision #3413.21.291](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.291) \[merge]\
      Tue 2013-07-16 19:09:54 +0200
      * mysql-5.5.32 merge
      * [Revision #3077.187.102](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.102)\
        Thu 2013-05-16 17:33:32 +0200
        * Fix for BUG

## 16812255: Removing the `--random-password` option which is supported only for MYSQL server versions 5.6 and above.

```
  * [Revision #3077.187.101](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.101)
```

Thu 2013-05-16 10:24:26 +0200

```
    * Changes to verify the solaris upgrade issue.
  * [Revision #3077.187.100](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.100)
```

Wed 2013-05-15 16:29:31 +0200

```
    * Fixing the RPM-ULN build issue by ignoring the postinstall_check.sh.
  * [Revision #3077.187.99](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.99)
```

Wed 2013-05-15 15:37:20 +0200

```
    * Bug 16812255 - 5.5.32 pkg installation failed during mysql_install_db execution
  * [Revision #3077.187.98](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.98)
```

Mon 2013-05-13 10:21:09 +0200

```
    * Updated copyright year information
  * [Revision #3077.187.97](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.97)
```

Mon 2013-05-13 09:46:44 +0200

```
    * Adding fix for Bug#16798868
  * [Revision #3077.187.96](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.96)
```

Wed 2013-05-08 12:08:20 +0200

```
    * Bug#16779374: new error message added to 5.5 after 5.6 ga - reusing number already used by 5.6
  * [Revision #3077.187.95](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.95)
```

Tue 2013-05-07 14:36:46 +0200

```
    * ULN-RPMs bug fix for BR16298542
  * [Revision #3077.187.94](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.94)
```

Mon 2013-05-06 20:31:26 +0530

```
    * Bug #16722314 foreign key id modified during export Bug #16754901 PARS_INFO_FREE not called in dict_create_add_foreign_to_dictionary
  * [Revision #3077.187.93](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.93)
```

Mon 2013-05-06 16:06:32 +0200

```
    * Bug#16757869: InnoDB: possible regression in 5.5.31, BUG #16004999
  * [Revision #3077.187.92](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.92)
```

Mon 2013-05-06 15:19:37 +0200

```
    * Updated spec file for Bug #16488773
  * [Revision #3077.187.91](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.91)
```

Fri 2013-05-03 16:39:17 +0300\
\* [Revision #3077.187.90](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.90) \[merge]\
Tue 2013-04-30 20:40:38 +0200

```
    * merge from mysql-5.1
    * [Revision #2661.848.26](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.26)
```

Tue 2013-04-30 20:39:12 +0200

```
      * Bug#16405422 - recovery failure, ASSERT !RECV_NO_LOG_WRITE
  * [Revision #3077.187.89](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.89) [merge]
```

Tue 2013-04-30 22:46:37 +0530

```
    * BUG#16222245 - crash with explain for a query with loose scan for GROUP BY, MyISAM
    * [Revision #2661.848.25](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.25)
```

Tue 2013-04-30 22:38:34 +0530

```
      * BUG#16222245 - crash with explain for a query with loose scan for GROUP BY, MyISAM
  * [Revision #3077.187.88](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.88)
```

Tue 2013-04-30 13:39:50 +0300

```
    * Bug#16720368 InnoDB ignores *.IBD file breakage at startup
  * [Revision #3077.187.87](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.87)
```

Sat 2013-04-27 16:04:54 +0800

```
    * Bug #13004581 	blackhole binary log with row ignores update and delete statements
  * [Revision #3077.187.86](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.86)
```

Thu 2013-04-25 11:56:26 +0530

```
    * BUG#16698172-cannot do point-in-time recovery for single database; mysqlbinlog
  * [Revision #3077.187.85](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.85)
```

Wed 2013-04-24 17:21:42 +0300

```
    * Bug #16680313: client doesn't read plugin-dir from my.cnf set by mysql_read_default_file
    * Parsing of the plugin-dir config file option was not working due to a typo. Fixed the typo.
    * No test case can be added due to lack of support for defaults-exitra-file testing in mysql-test-run.pl.
    * Thanks to Sinisa for contributing the fix.
  * [Revision #3077.187.84](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.84) [merge]
```

Wed 2013-04-24 13:34:11 +0530

```
    * [Revision #2661.848.24](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.24)
```

Wed 2013-04-24 13:31:10 +0530\
\* [Revision #3077.187.83](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.83) \[merge]\
Wed 2013-04-24 08:48:34 +0200

```
    * Null merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.23](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.23)
```

Wed 2013-04-24 08:47:30 +0200

```
      * Bug #15973904 InnoDB partition code holds lock_open and sleeps while opening missing partition
  * [Revision #3077.187.82](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.82)
```

Wed 2013-04-24 08:42:59 +0200

```
    * Merge from mysql-5.1 to mysql-5.5
  * [Revision #3077.187.81](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.81) [merge]
```

Mon 2013-04-22 14:30:47 +0200

```
    * Upmerge of the 5.1.69 build
    * [Revision #2661.848.22](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.22)
```

Mon 2013-04-22 14:01:07 +0200

```
      * Merge from mysql-5.1.69-release
  * [Revision #3077.187.80](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.80) [merge]
```

Sat 2013-04-20 12:36:11 +0530

```
    * Bug#16073689 : crash in ITEM_FUNC_MATCH::INIT_SEARCH
    * [Revision #2661.848.21](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.21)
```

Sat 2013-04-20 12:28:22 +0530

```
      * Bug#16073689 : crash in ITEM_FUNC_MATCH::INIT_SEARCH
  * [Revision #3077.187.79](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.79) [merge]
```

Thu 2013-04-18 12:52:59 +0200

```
    * Merge from mysql-5.5.31-release
  * [Revision #3077.187.78](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.78)
```

Wed 2013-04-17 09:26:51 +0200

```
    * Bug#16626742 in my_md5final in mysys/md5.c, ctx is not properly zeroed as intended
  * [Revision #3077.187.77](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.77)
```

Tue 2013-04-16 16:26:45 +0530

```
    * Bug #16632543 - INCORRECT VALUE OF BOGOMIPS IN MYSQLTEST
  * [Revision #3077.187.76](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.76) [merge]
```

Tue 2013-04-16 12:17:18 +0200

```
    * Merging the changes for Bug 16633169 - mysql.info contains outdated information.
    * [Revision #2661.848.20](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.20)
```

Tue 2013-04-16 12:12:18 +0200

```
      * Bug 16633169 - mysql.info contains outdated information.
  * [Revision #3077.187.75](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.75) [merge]
```

Sun 2013-04-14 08:09:56 +0530

```
    * Merge from 5.1 to 5.5
    * [Revision #2661.848.19](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.19)
```

Sun 2013-04-14 07:30:49 +0530

```
      * Bug#16347426:assertion failed: `(SELECT_INSERT && !TABLES->NEXT_NAME_RESOLUTION_TABLE) || !TAB`
  * [Revision #3077.187.74](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.74)
```

Fri 2013-04-12 14:18:21 +0530

```
    * BUG#16615117 mysqldump produces a change master statement with a port number enclosed in quotes
  * [Revision #3077.187.73](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.73)
```

Fri 2013-04-12 09:39:56 +0200

```
    * Bug#16540042: wrong query result when using range over partial index
  * [Revision #3077.187.72](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.72)
```

Thu 2013-04-11 10:50:50 +0800

```
    * Bug	:#16005310 fiX BUG - innodb_row_lock_time_max seems to have an overflow
  * [Revision #3077.187.71](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.71)
```

Wed 2013-04-10 16:43:09 +0200

```
    * Bug#16395606 scripts missing execute bit
  * [Revision #3077.187.70](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.70)
```

Wed 2013-04-10 11:50:41 +0530

```
    * BUG#16402143 - stack corruption in DBUG_EXPLAIN description and fix: DBUG_EXPLAIN result in buffer overflow when the DEBUG variable values length exceed 255. In _db_explain_ function which call macro str_to_buf incorrectly passes the length of buf avaliable to strnmov as len+1. The fix calculates the avaliable space in buf and passes it to strnxmov.
  * [Revision #3077.187.69](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.69) [merge]
```

Tue 2013-04-09 14:03:35 +0530

```
    * local merge.
    * [Revision #2661.848.18](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.18)
```

Tue 2013-04-09 14:00:05 +0530

```
      * Backporting patch for bug #15852074.
  * [Revision #3077.187.68](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.68) [merge]
```

Mon 2013-04-08 18:53:24 +0530

```
    * null merge
    * [Revision #2661.848.17](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.17)
```

Mon 2013-04-08 18:48:57 +0530\
\* [Revision #3077.187.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.67) \[merge]\
Mon 2013-04-08 18:14:06 +0530

```
    * [Revision #2661.848.16](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.16)
```

Mon 2013-04-08 18:12:39 +0530\
\* [Revision #3077.187.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.66)\
Mon 2013-04-08 15:25:45 +0530

```
    * BUG#15978766 - test valgrind_report fails innodb tests
  * [Revision #3077.187.65](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.65)
```

Thu 2013-04-04 14:54:16 +0530

```
    * Bug #16401597 - mtr v1 returns incorrect path to variable @@basedir
  * [Revision #3077.187.64](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.64)
```

Wed 2013-04-03 18:09:37 +0200

```
    * Bug 16534721 - mysql_install_db runs again during upgrade even data directory exists
  * [Revision #3077.187.63](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.63) [merge]
```

Tue 2013-04-02 16:20:49 +0200

```
    * merge 5.1 => 5.5
    * [Revision #2661.848.15](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.15)
```

Tue 2013-04-02 16:05:10 +0200

```
      * Bug#14700180 crash in copy_funcs This is a backport of the fix for Bug #13966809 crash in copy_funcs when grouping by outer query blob field in subquery
  * [Revision #3077.187.62](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.62)
```

Tue 2013-04-02 11:14:39 +0200

```
    * Bug#11765629 cmake: can suppress installation of sql-bench, but not mysql-test
  * [Revision #3077.187.61](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.61) [merge]
```

Tue 2013-04-02 11:17:06 +0530

```
    * [Revision #2661.848.14](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.14)
```

Tue 2013-04-02 11:16:26 +0530\
\* [Revision #3077.187.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.60) \[merge]\
Mon 2013-04-01 13:45:27 +0530

```
    * [Revision #2661.848.13](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.13)
```

Mon 2013-04-01 12:26:55 +0530\
\* [Revision #3077.187.59](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.59) \[merge]\
Sun 2013-03-31 06:52:16 +0530

```
    * Merge from 5.1 to 5.5
    * [Revision #2661.848.12](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.12)
```

Sun 2013-03-31 06:48:30 +0530

```
      * Bug #16347343 : CRASH, GROUP_CONCAT, DERIVED TABLES
  * [Revision #3077.187.58](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.58)
```

Sat 2013-03-30 19:24:54 +0530

```
    * Bug#14261010: on duplicate key update crashes the server
  * [Revision #3077.187.57](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.57) [merge]
```

Fri 2013-03-29 22:11:33 +0530

```
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.11](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.11)
```

Fri 2013-03-29 22:01:10 +0530

```
      * Bug #16244691 server gone away error occurs depending on the number of table/key relations
  * [Revision #3077.187.56](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.56)
```

Fri 2013-03-29 16:33:33 +0530

```
    * Bug #16402124 - mtr processes certain assigned vardir values wrong
  * [Revision #3077.187.55](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.55) [merge]
```

Fri 2013-03-29 15:14:38 +0530

```
    * [Revision #2661.848.10](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.10)
```

Fri 2013-03-29 15:09:14 +0530\
\* [Revision #3077.187.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.54)\
Fri 2013-03-29 11:44:42 +0530\
\* [Revision #3077.187.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.53)\
Fri 2013-03-29 09:28:31 +0530

```
    * Bug #15948818-semi-sync enabled master crashes when event scheduler drops events
  * [Revision #3077.187.52](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.52) [merge]
```

Thu 2013-03-28 17:41:22 +0200

```
    * merge
    * [Revision #2661.848.9](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.9)
```

Thu 2013-03-28 17:37:29 +0200

```
      * Addendum #1 to the fix for bug #16451878 : geometry query crashes server
  * [Revision #3077.187.51](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.51) [merge]
```

Thu 2013-03-28 19:17:28 +0530

```
    * Merge from 5.1 to 5.5
    * [Revision #2661.848.8](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.8)
```

Thu 2013-03-28 19:11:26 +0530

```
      * BUG#11753852: if() values are evaluated differently in a regular sql vs prepared statement
  * [Revision #3077.187.50](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.50) [merge]
```

Thu 2013-03-28 14:18:51 +0530

```
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.7](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.7)
```

Thu 2013-03-28 14:14:39 +0530

```
      * Bug#14324766:partially written insert statement in binlog no errors reported
  * [Revision #3077.187.49](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.49)
```

Thu 2013-03-28 11:47:43 +0530

```
    * Bug #16403186 - mtr on windows should not try to start cdb if running with parallel
  * [Revision #3077.187.48](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.48) [merge]
```

Thu 2013-03-28 10:43:50 +0530

```
    * Null merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.6](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.6)
```

Thu 2013-03-28 10:42:42 +0530

```
      * Bug #16244691 server gone away error occurs depending on the number of table/key relations
  * [Revision #3077.187.47](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.47) [merge]
```

Thu 2013-03-28 10:25:23 +0530

```
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.849.1](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.849.1)
```

Wed 2013-03-27 11:11:38 +0530

```
      * Bug #16244691 server gone away error occurs depending on the number of table/key relations
  * [Revision #3077.187.46](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.46) [merge]
```

Wed 2013-03-27 16:06:33 +0200

```
    * merge 5.1->5.5
    * [Revision #2661.848.5](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.5)
```

Wed 2013-03-27 16:03:00 +0200

```
      * Bug #16451878: geometry query crashes server
  * [Revision #3077.187.45](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.45) [merge]
```

Wed 2013-03-27 11:22:25 +0000

```
    * BUG#16541422: log-slave-updates + replicate-wild-ignore-table fails for user variables
    * [Revision #2661.848.4](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.4)
```

Wed 2013-03-27 11:19:29 +0000

```
      * BUG#16541422: log-slave-updates + replicate-wild-ignore-table fails for user variables
  * [Revision #3077.187.44](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.44) [merge]
```

Wed 2013-03-27 11:59:40 +0530

```
    * Merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.848.3](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.3)
```

Wed 2013-03-27 11:53:01 +0530

```
      * Bug#11829838: ALTER TABLE not binlogged with `--BINLOG-IGNORE-DB` and fully qualified table
  * [Revision #3077.187.43](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.43) [merge]
```

Tue 2013-03-26 23:11:55 +0200

```
    * merge from 5.1->5.5 repo.
    * [Revision #2661.848.2](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.2) [merge]
```

Tue 2013-03-26 23:10:42 +0200

```
      * merge from 5.1 repo.
  * [Revision #3077.187.42](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.42)
```

Tue 2013-03-26 21:45:39 +0200\
\* [Revision #3077.187.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.41) \[merge]\
Tue 2013-03-26 20:52:01 +0200

```
    * merge from 5.1
    * [Revision #2661.848.1](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.848.1)
```

Tue 2013-03-26 19:24:01 +0200

```
      * Bug#16541422 log-slave-updates + replicate-wild-ignore-table fails for user variables
  * [Revision #3077.187.40](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.40) [merge]
```

Tue 2013-03-26 08:24:11 +0100

```
    * NULL merge 5.1 => 5.5
    * [Revision #2661.844.69](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.69)
```

Tue 2013-03-26 08:22:45 +0100

```
      * Bug#62856 Check for "stack overrun" doesn't work with gcc-4.6, server crashes Bug#13243248 check for "stack overrun" doesn't work with gcc-4.6, server crashes
  * [Revision #3077.187.39](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.39)
```

Mon 2013-03-25 11:27:12 +0530

```
    * BUG#16438800 - slave_max_allowed_packet not honored on slave io connect
  * [Revision #3077.187.38](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.38) [merge]
```

Fri 2013-03-22 20:16:53 +0530

```
    * local merge.
    * [Revision #2661.844.68](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.68)
```

Fri 2013-03-22 20:00:40 +0530

```
      * Bug#12671635 : Updating embedded tests.
  * [Revision #3077.187.37](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.37) [merge]
```

Fri 2013-03-22 15:33:59 +0530

```
    * local merge.
    * [Revision #2661.844.67](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.67)
```

Fri 2013-03-22 15:29:57 +0530

```
      * Bug#12671635 : Fixing test cases.
  * [Revision #3077.187.36](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.36)
```

Fri 2013-03-22 14:55:30 +0530

```
    * Bug#16500013 : post-fix
  * [Revision #3077.187.35](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.35) [merge]
```

Thu 2013-03-21 23:40:25 +0530

```
    * Merge of patch for Bug#12671635 from mysql-5.1.
    * [Revision #2661.844.66](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.66)
```

Thu 2013-03-21 23:36:02 +0530

```
      * Bug#12671635 help-tableformat doesn't match help-files
  * [Revision #3077.187.34](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.34)
```

Thu 2013-03-21 22:51:40 +0530

```
    * Bug#16500013 : add version check to mysql_upgrade
  * [Revision #3077.187.33](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.33)
```

Thu 2013-03-21 11:40:43 +0530

```
    * Bug #16051728 server crashes in add_identifier on concurrent alter table and show engine innod
  * [Revision #3077.187.32](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.32) [merge]
```

Wed 2013-03-20 17:52:15 +0100

```
    * Null merge from 5.1 for permission changes.
    * [Revision #2661.844.65](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.65)
```

Wed 2013-03-20 17:49:30 +0100

```
      * Correcting the permissions of executable files.
  * [Revision #3077.187.31](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.31)
```

Wed 2013-03-20 17:50:15 +0100

```
    * Correcting the permissions of the executable files.
  * [Revision #3077.187.30](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.30)
```

Tue 2013-03-19 17:09:17 +0100

```
    * Bug#13009341 crash in str_to_datetime after misbehaving "blob" value comparison
  * [Revision #3077.187.29](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.29)
```

Wed 2013-03-20 11:20:12 +0100

```
    * Bug#16394084: loose index scan with quoted int predicate returns random data
  * [Revision #3077.187.28](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.28)
```

Tue 2013-03-19 15:08:19 +0100

```
    * Bug#16359402 crash with aggregates: assertion failed: n < m_size
  * [Revision #3077.187.27](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.27)
```

Tue 2013-03-19 15:53:48 +0100

```
    * Fix for Bug 16395495 - old fsf address in gpl header
  * [Revision #3077.187.26](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.26) [merge]
```

Tue 2013-03-19 13:36:34 +0100

```
    * Upmerging the changes for Bug 16395495 from 5.1
    * [Revision #2661.844.64](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.64)
```

Tue 2013-03-19 13:29:12 +0100

```
      * Bug 16395495 - old fsf address in gpl header
  * [Revision #3077.187.25](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.25)
```

Mon 2013-03-18 17:20:30 +0200

```
    * Fix Bug#16400412 unnecessary dict_update_statistics during concurrent updates
  * [Revision #3077.187.24](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.24) [merge]
```

Tue 2013-03-19 05:35:30 +0100

```
    * Upmerging the changes for Bug 16401147 from 5.1
    * [Revision #2661.844.63](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.63)
```

Tue 2013-03-19 05:19:31 +0100

```
      * Bug 16401147 - crlf instead of lf in readme
  * [Revision #3077.187.23](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.23)
```

Tue 2013-03-19 05:24:03 +0100

```
    * Bug 16401147 - crlf instead of lf in readme
  * [Revision #3077.187.22](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.22) [merge]
```

Mon 2013-03-18 15:03:54 +0530

```
    * merge from mysql-5.1 to mysql-5.5
    * [Revision #2661.844.62](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.62)
```

Mon 2013-03-18 15:01:16 +0530

```
      * Bug#14771299 out-of-bound reads write in mysqlbinlog
  * [Revision #3077.187.21](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.21)
```

Mon 2013-03-18 13:48:53 +0530

```
    * Bug #16076289 : backport fix for bug #14786792 to 5.5
  * [Revision #3077.187.20](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.20) [merge]
```

Mon 2013-03-18 12:46:06 +0530

```
    * Merge of patch for bug #14685362 from mysql-5.1.
    * [Revision #2661.844.61](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.61)
```

Mon 2013-03-18 12:44:38 +0530

```
      * Bug#14685362 : memory leaks in mysql client in interactive mode
  * [Revision #3077.187.19](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.19) [merge]
```

Fri 2013-03-15 08:57:59 +0530

```
    * Bug#16056813-memory leak on filtered slave Null merge from mysql-5.1
    * [Revision #2661.844.60](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.60)
```

Fri 2013-03-15 08:56:20 +0530

```
      * Bug#16056813-memory leak on filtered slave
  * [Revision #3077.187.18](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.18)
```

Thu 2013-03-14 15:33:25 +0100

```
    * Bug#16359402 crash with aggregates: assertion failed: `n < m_size`
  * [Revision #3077.187.17](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.17) [merge]
```

Thu 2013-03-14 11:22:08 +0300

```
    * 5.1 -> 5.5 merge
    * [Revision #2661.844.59](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.59)
```

Thu 2013-03-14 11:11:17 +0300

```
      * Bug #16075310 SERVER CRASH OR VALGRIND ERRORS IN ITEM_FUNC_GROUP_CONCAT::SETUP AND ::ADD Item_func_group_concat::copy_or_same() creates a copy of original object. It also creates a copy of ORDER structure because ORDER struct elements may be modified in find_order_in_list() called from Item_func_group_concat::setup(). As ORDER copy is created using memcpy, ORDER::next elements point to original ORDER structs. Thus find_order_in_list() called from EXECUTE stmt modifies ordinal ORDER item pointers so they point to runtime items, these items are freed after execution, so original ORDER structure becomes invalid. The fix is to properly update ORDER::next fields so that they point to new ORDER elements.
  * [Revision #3077.187.16](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.16) [merge]
```

Wed 2013-03-13 16:29:11 +0530

```
    * BUG #14593883-replication breaks when set data type columns are used inside a stored procedure
    * Merging post-push fix from mysql-5.1
    * [Revision #2661.844.58](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.58)
```

Wed 2013-03-13 16:24:35 +0530

```
      * Bug #14593883-replication breaks when set data type columns are used inside a stored procedure
  * [Revision #3077.187.15](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.15)
```

Wed 2013-03-13 11:43:21 +0530

```
    * Bug #16268289 lock_rec_validate_page() may dereference a pointer to a freed lock
  * [Revision #3077.187.14](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.14) [merge]
```

Wed 2013-03-13 09:43:50 +0530

```
    * Bug #16084346: ssl_connect_debug.test failure in 5.1
    * [Revision #2661.844.57](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.57)
```

Wed 2013-03-13 09:42:07 +0530\
\* [Revision #3077.187.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.13) \[merge]\
Tue 2013-03-12 22:44:32 +0530

```
    * Bug #14593883-replication breaks when set data type columns are used inside a stored procedure
    * [Revision #2661.844.56](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.56)
```

Tue 2013-03-12 22:36:13 +0530

```
      * Bug #14593883-replication breaks when set data type columns are used inside a stored procedure
  * [Revision #3077.187.12](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.12)
```

Tue 2013-03-12 13:58:10 +0200

```
    * Bug #16409715 assert sync_thread_levels_g(array, level - 1, true), ibuf, free space management
  * [Revision #3077.187.11](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.11) [merge]
```

Tue 2013-03-12 13:57:02 +0200

```
    * Merge mysql-5.1 to mysql-5.5.
    * [Revision #2661.844.55](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.55)
```

Tue 2013-03-12 13:42:12 +0200

```
      * Bug #16463505 pessimistic page_zip_available() may cause infinite page split
    * [Revision #2661.844.54](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.54)
```

Tue 2013-03-12 13:37:00 +0200\
\* [Revision #3077.187.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.10)\
Mon 2013-03-11 16:46:11 +0100

```
    * Bug #11766815 invalid system check time_t_unsigned
  * [Revision #3077.187.9](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.9)
```

Mon 2013-03-11 12:03:26 +0530\
\* [Revision #3077.187.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.8)\
Fri 2013-03-08 14:55:41 +0530\
\* [Revision #3077.187.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.187.7)\
Thu 2013-03-07 14:44:35 +0530

```
    * BUG #16069598 - server crash by null pointer dereferencing in mem_heap_create_block()
  * [Revision #3077.187.6](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.6)
```

Fri 2013-03-01 13:25:59 +0100

```
    * Bug #11765489 cmake build on mac os x does not determine cpu type
  * [Revision #3077.187.5](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.5)
```

Thu 2013-03-07 12:12:58 +0530

```
    * Bug#16169063: security concern because of insufficient logging
  * [Revision #3077.187.4](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.4)
```

Wed 2013-03-06 11:49:57 +0530

```
    * Bug #16133801 unexplainable innodb unique index locks on delete + insert with same values
  * [Revision #3077.187.3](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.3) [merge]
```

Wed 2013-03-06 06:52:18 +0100

```
    * NULL Merge for release 5.1.69
    * [Revision #2661.844.53](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2661.844.53)
```

Tue 2013-03-05 16:09:54 +0100

```
      * Raise version number after cloning 5.1.69
  * [Revision #3077.187.2](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.2)
```

Tue 2013-03-05 10:47:49 -0500

```
    * Bug#16068056 InnoDB calls buf_validate() too often with univ_debug
  * [Revision #3077.187.1](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3077.187.1)
```

Tue 2013-03-05 12:19:07 +0100

```
    * Raise version number after cloning 5.5.31
* [Revision #3413.21.290](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.290) [merge]
```

Tue 2013-07-16 19:03:06 +0200

```
  * 5.3 merge
  * [Revision #2502.567.114](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.114) [merge]
```

Mon 2013-07-15 18:32:25 +0200

```
    * 5.2 merge
    * [Revision #2502.566.51](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.566.51)
```

Tue 2013-07-09 22:24:57 +0200

```
      * [MDEV-4409](https://jira.mariadb.org/browse/MDEV-4409) - Fix deadlock in MySQL key cache code, that can happen if there is a key cache resize running in parallel with an update.
* [Revision #3413.21.289](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.289) [merge]
```

Tue 2013-07-16 15:59:30 +0400

```
  * Automatic merge
  * [Revision #3413.32.1](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.32.1)
```

Tue 2013-07-16 15:57:27 +0400

```
    * [MDEV-4782](https://jira.mariadb.org/browse/MDEV-4782): Valgrind warnings (Conditional jump or move depends on uninitialised value) with InnoDB, semijoin - in sub_select(): don't call table->file->position() when reading the first record produced an error.
* [Revision #3413.21.288](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.288)
```

Tue 2013-07-16 17:26:25 +0400

```
  * Update test results after the last cset.
* [Revision #3413.21.287](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.287)
```

Tue 2013-07-16 10:56:42 +0400

```
  * [MDEV-4778](https://jira.mariadb.org/browse/MDEV-4778): Incorrect results from Aria/MyISAM SELECT using index with prefix length on TEXT column Backport the fix olav.sandstaa@sun.com-20101102184747-qfuntqwj021imy9r: "Fix for Bug#52660 Perf. regr. using ICP for MyISAM on range queries on an index containing TEXT" (together with further fixes in that code) into MyISAM and Aria.
* [Revision #3413.21.286](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.286)
```

Tue 2013-07-16 09:22:17 +0400

```
  * [MDEV-4173](https://jira.mariadb.org/browse/MDEV-4173): Wrong result (extra row) with semijoin=on, joins in outer query, LEFT JOIN in the subquery Apply the patch from Patryk Pomykalski:

    * create_internal_tmp_table_from_heap() will now return information whether the last row that we tried to write was a duplicate row. (mysql-5.6 also has this change)
* [Revision #3413.21.285](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.285)
```

Mon 2013-07-15 18:51:52 +0400

```
  * [MDEV-4536](https://jira.mariadb.org/browse/MDEV-4536), [MDEV-4042](https://jira.mariadb.org/browse/MDEV-4042) - Make JOIN::cleanup(true) also work correctly when the query is KILLed after join optimization was started but before a query plan was produced
* [Revision #3413.21.284](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.284)
```

Thu 2013-07-11 19:27:39 +0400

```
  * [MDEV-4042](https://jira.mariadb.org/browse/MDEV-4042): Assertion `table->key_read == 0' fails in close_thread_table on EXPLAIN [MDEV-4536](https://jira.mariadb.org/browse/MDEV-4536): ...sql/sql_base.cc:1598: `bool close_thread_table(THD*, TABLE**)`: Assertion - Make JOIN::cleanup(full=true) always free join optimization tabs.
* [Revision #3413.21.283](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.283)
```

Thu 2013-07-11 15:12:50 +0400

```
  * [MDEV-4556](https://jira.mariadb.org/browse/MDEV-4556) Server crashes in SEL_ARG::rb_insert with index_merge+index_merge_sort_union, FORCE INDEX - merge_same_index_scans() may put the same SEL_ARG tree in multiple result plans. make it call incr_refs() on the SEL_ARG trees that it does key_or() on, because key_or(sel_arg_tree_1, sel_arg_tree_2) call may invalidate SEL_ARG trees pointed by sel_arg_tree_1 and sel_arg_tree_2.
* [Revision #3413.21.282](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.282) [merge]
```

Wed 2013-07-10 02:05:06 +0400

```
  * Merge from 5.3
  * [Revision #2502.567.113](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.113) [merge]
```

Tue 2013-07-09 11:02:56 +0400

```
    * Merge from 5.2
    * [Revision #2502.566.50](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.566.50) [merge]
```

Tue 2013-07-09 10:54:47 +0400

```
      * Merge from 5.1
      * [Revision #2502.565.51](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.565.51)
```

Sat 2013-07-06 15:28:11 +0200

```
        * Bug #69682 - mysqld crashes after uninstall of plugin with "first" status var
      * [Revision #2502.565.50](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.565.50)
```

Fri 2013-05-24 17:35:30 +0200

```
        * [MDEV-4575](https://jira.mariadb.org/browse/MDEV-4575) MySQL client doesn't strip off 5.5.5- prefix while connecting to 10.x server
  * [Revision #2502.567.112](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.112)
```

Fri 2013-07-05 20:45:42 +0200

```
    * [MDEV-4610](https://jira.mariadb.org/browse/MDEV-4610) SQL query crashes MariaDB with derived_with_keys [MDEV-4643](https://jira.mariadb.org/browse/MDEV-4643) MariaDB crashes consistently when trying a SELECT on VIEW with a UNION and an additional JOIN in SELECT
  * [Revision #2502.567.111](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.111)
```

Fri 2013-07-05 17:54:25 +0200

```
    * [MDEV-4665](https://jira.mariadb.org/browse/MDEV-4665) crash when referencing missing function in a subquery
  * [Revision #2502.567.110](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.110)
```

Fri 2013-07-05 16:02:02 +0200

```
    * [MDEV-4257](https://jira.mariadb.org/browse/MDEV-4257) Assertion `!table || (!table->read_set || bitmap_is_set(table->read_set, field_index))' fails on FROM subquery with fulltext search, derived_merge=on
* [Revision #3413.21.281](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.281) [merge]
```

Mon 2013-07-08 16:49:42 +0400

```
  * Merging from 5.3
  * [Revision #2502.567.109](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.109)
```

Wed 2013-07-03 09:46:20 +0200

```
    * [MDEV-4667](https://jira.mariadb.org/browse/MDEV-4667) DATE('string') incompability between mysql and mariadb
* [Revision #3413.21.280](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.280)
```

Thu 2013-07-04 18:37:55 +0300

```
  * [MDEV-4752](https://jira.mariadb.org/browse/MDEV-4752): Segfault during parsing of illegal query
* [Revision #3413.21.279](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.279)
```

Mon 2013-07-01 17:54:24 +0200

```
  * [MDEV-4718](https://jira.mariadb.org/browse/MDEV-4718) Test "outfile_loaddata" fails on bigendian arches (ppc64)
* [Revision #3413.21.278](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.278)
```

Mon 2013-07-01 12:03:10 +0200

```
  * [MDEV-4670](https://jira.mariadb.org/browse/MDEV-4670) THD::awake bug with my_sleep call
* [Revision #3413.21.277](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.277)
```

Mon 2013-07-01 12:02:44 +0200

```
  * [MDEV-4683](https://jira.mariadb.org/browse/MDEV-4683) query start_time not reset when going to sleep
* [Revision #3413.21.276](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.276) [merge]
```

Fri 2013-06-28 16:27:22 +0400

```
  * Merge
  * [Revision #2502.567.108](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.108)
```

Fri 2013-06-28 16:25:06 +0400

```
    * A clean-up for [MDEV-4634](https://jira.mariadb.org/browse/MDEV-4634)
* [Revision #3413.21.275](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.275) [merge]
```

Fri 2013-06-28 15:20:40 +0400

```
  * Merge from 5.3
  * [Revision #2502.567.107](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.107)
```

Fri 2013-06-28 12:00:25 +0400

```
    * [MDEV-4634](https://jira.mariadb.org/browse/MDEV-4634) Crash in CONVERT_TZ Item_func_min_max::get_date() did not check the returned value against the fuzzy_date flags, so it could return a bad value to the caller that expects a good date (e.h. CONVERT_TZ).
* [Revision #3413.21.274](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.274)
```

Thu 2013-06-27 14:19:04 +0200

```
  * [MDEV-4720](https://jira.mariadb.org/browse/MDEV-4720) : fix my_context.h for use with x32 ABI. Do not use x64 assembler implementation in x32.
* [Revision #3413.21.273](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.273)
```

Sat 2013-06-22 14:02:03 +0200

```
  * [MDEV-4685](https://jira.mariadb.org/browse/MDEV-4685) Compile error on LFS
* [Revision #3413.21.272](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.272) [merge]
```

Tue 2013-06-18 13:14:46 +0400

```
  * Merging [MDEV-4635](https://jira.mariadb.org/browse/MDEV-4635) from 5.3.
  * [Revision #2502.567.106](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.106)
```

Mon 2013-06-17 19:25:55 +0400

```
    * [MDEV-4635](https://jira.mariadb.org/browse/MDEV-4635) Crash in UNIX_TIMESTAMP(STR_TO_DATE('2020','%Y'))
* [Revision #3413.21.271](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.271)
```

Mon 2013-06-17 19:18:14 +0200

```
  * [MDEV-4503](https://jira.mariadb.org/browse/MDEV-4503) : Installation fails if TEMP directory contains "" subdirectory.
* [Revision #3413.21.270](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.270)
```

Mon 2013-06-17 17:58:53 +0200

```
  * unit test case for [MDEV-4576](https://jira.mariadb.org/browse/MDEV-4576)
* [Revision #3413.21.269](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.269)
```

Sun 2013-06-16 22:13:26 +0200

```
  * [MDEV-4576](https://jira.mariadb.org/browse/MDEV-4576) : Aria storage engine's temporary files might not be deleted (Errcode : 13) See also MySQL Bug #39750 and similar ones.
* [Revision #3413.21.268](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.268)
```

Sat 2013-06-15 14:22:03 +0200

```
  * [MDEV-4601](https://jira.mariadb.org/browse/MDEV-4601) : Allow MariaDB to be build without non-blocking client.
* [Revision #3413.21.267](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.267) [merge]
```

Mon 2013-06-17 20:33:36 +0300

```
  * 5.3 -> 5.5 Merge
  * [Revision #2502.567.105](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.105)
```

Mon 2013-06-17 17:04:51 +0400

```
    * [MDEV-4651](https://jira.mariadb.org/browse/MDEV-4651) Crash in my_decimal2decimal in a ORDER BY query
  * [Revision #2502.567.104](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/2502.567.104)
```

Thu 2013-06-06 23:33:40 +0300

```
    * [MDEV-4593](https://jira.mariadb.org/browse/MDEV-4593): p_s: crash in simplify_joins with delete using subselect from view
* [Revision #3413.21.266](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.266)
```

Sat 2013-06-15 16:02:43 +0200

```
  * [MDEV-4466](https://jira.mariadb.org/browse/MDEV-4466) Partitioned Aria table created by a previous version is recognized as TEST_SQL_DISCOVERY
* [Revision #3413.21.265](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.265)
```

Fri 2013-06-14 14:04:58 +0200

```
  * [MDEV-4006](https://jira.mariadb.org/browse/MDEV-4006) mysql_plugin.1 is removed from source which is not necessary
* [Revision #3413.21.264](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.264)
```

Thu 2013-06-13 20:19:32 +0200

```
  * [MDEV-4578](https://jira.mariadb.org/browse/MDEV-4578) information_schema.processlist reports incorrect value for Time (2147483647)
* [Revision #3413.21.263](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.263)
```

Thu 2013-06-13 20:19:11 +0200

```
  * [MDEV-4529](https://jira.mariadb.org/browse/MDEV-4529) Assertion `tmp->state == 4' fails on mix of INSTALL SONAME / UNINSTALL PLUGIN
* [Revision #3413.21.262](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.262)
```

Thu 2013-06-13 20:18:40 +0200

```
  * [MDEV-4519](https://jira.mariadb.org/browse/MDEV-4519) SHOW EVENTS and SHOW PROCEDURE STATUS truncate long user names
* [Revision #3413.21.261](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.261)
```

Thu 2013-06-13 15:33:02 +0200

```
  * [MDEV-4515](https://jira.mariadb.org/browse/MDEV-4515) Long user names are truncated to 48 symbols in error messages
* [Revision #3413.21.260](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.260)
```

Thu 2013-06-13 15:13:13 +0200

```
  * [MDEV-4444](https://jira.mariadb.org/browse/MDEV-4444) Server crashes with "safe_mutex: Trying to destroy a mutex share->mutex that was locked" on attempt to recover an archive table
* [Revision #3413.21.259](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.259)
```

Thu 2013-06-13 14:32:57 +0200

```
  * [MDEV-703](https://jira.mariadb.org/browse/MDEV-703) [Bug #870310](https://bugs.launchpad.net/bugs/870310) - killall -9 in init-script
* [Revision #3413.21.258](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.258)
```

Thu 2013-06-13 14:14:47 +0200

```
  * [MDEV-4573](https://jira.mariadb.org/browse/MDEV-4573) UNINSTALL PLUGIN misleading error message for non-dynamic plugins
* [Revision #3413.21.257](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.257)
```

Thu 2013-06-13 00:13:23 +0200

```
  * [MDEV-4614](https://jira.mariadb.org/browse/MDEV-4614) Man pages fixes
* [Revision #3413.21.256](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.256)
```

Wed 2013-06-12 22:12:09 +0200

```
  * [MDEV-4604](https://jira.mariadb.org/browse/MDEV-4604) Wrong server status when sending out parameters
* [Revision #3413.21.255](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.255)
```

Wed 2013-06-12 20:38:22 +0200

```
  * [MDEV-4509](https://jira.mariadb.org/browse/MDEV-4509) mysql init script should accept arguments
* [Revision #3413.21.254](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.254)
```

Wed 2013-06-12 20:29:19 +0200

```
  * [MDEV-4422](https://jira.mariadb.org/browse/MDEV-4422) SHOW PROCESSLIST reference to THD::db not protected against simultaneous updates
* [Revision #3413.21.253](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.253)
```

Tue 2013-06-11 12:53:35 +0200

```
  * [MDEV-4636](https://jira.mariadb.org/browse/MDEV-4636) use mysql_cleartext_plugin from auth_pam
* [Revision #3413.21.252](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.252)
```

Tue 2013-06-11 11:11:05 +0200

```
  * [MDEV-4574](https://jira.mariadb.org/browse/MDEV-4574) Missing connection option MYSQL_ENABLE_CLEARTEXT_PLUGIN
* [Revision #3413.21.251](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.251)
```

Mon 2013-06-10 21:45:30 +0200

```
  * [MDEV-4297](https://jira.mariadb.org/browse/MDEV-4297) mysql `--binary-mode`
* [Revision #3413.21.250](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.250)
```

Wed 2013-06-12 05:09:28 +0400

```
  * [MDEV-4629](https://jira.mariadb.org/browse/MDEV-4629) MTR tests main.variables and some of sys_vars.* fail on 32-bit builds
* [Revision #3413.21.249](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.249)
```

Tue 2013-06-11 13:49:43 +0300

```
  * Fixed tests that failed on 32 bit because of my earlier fixes of 32 bit limits.
* [Revision #3413.21.248](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.248)
```

Fri 2013-06-07 15:35:13 +0200

```
  * [MDEV-4468](https://jira.mariadb.org/browse/MDEV-4468) Assertion '`error != 0`' fails or timeout occurs on select from a FEDERATED table which points at a non-existent table
* [Revision #3413.21.247](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.247)
```

Fri 2013-06-07 15:34:59 +0200

```
  * [MDEV-4480](https://jira.mariadb.org/browse/MDEV-4480) Assertion `inited == NONE' fails on closing a connection with open handler on temporary table
* [Revision #3413.21.246](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.246)
```

Fri 2013-06-07 10:02:50 +0200

```
  * [MDEV-4564](https://jira.mariadb.org/browse/MDEV-4564) ALTER on a temporary table generates an audit event
* [Revision #3413.21.245](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.245)
```

Sun 2013-06-09 13:26:10 +0300

```
  * Added -Wno-uninitialized to avoid warnings in release builds (uninitalized variables are detected by DBUG builds) - Fixed wrong declaration which cased compile failure on 32 bit
* [Revision #3413.21.244](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.244)
```

Thu 2013-06-06 15:14:23 +0300

```
  * Fixed some cache variables that could be set to higher value than what the code supported (size_t) Fixed some cases that didn't work with > 4G buffers. Fixed compiler warnings
* [Revision #3413.21.243](https://bazaar.launchpad.net/%7Emaria-captains/maria/10.0/revision/3413.21.243)
```

Wed 2013-06-05 23:53:35 +0300

```
  * Run test suite with smaller aria keybuffer size (to make it possible to run more tests in parallel) -Added test and extra code to ensure we don't leave keyread on for a handler table. -Create on disk temporary files always with long data pointers if SQL_SMALL_RESULT is not used. This ensures that we can handle temporary files bigger than 4G.
```

* [Revision #3427.1.244](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.244)\
  Wed 2013-07-10 12:01:52 +0200
  * [MDEV-4708](https://jira.mariadb.org/browse/MDEV-4708): GTID strict mode doesn't work on a database with purged binlogs
* [Revision #3427.1.243](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.243)\
  Wed 2013-07-10 11:45:15 +0200
  * [MDEV-4708](https://jira.mariadb.org/browse/MDEV-4708): GTID strict mode doesn't work on a database with purged binlogs
* [Revision #3427.1.242](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.242)\
  Mon 2013-06-24 20:56:55 +0200
  * cleanup: remove LF\_REQUIRE\_PINS, use compile\_time\_assert() instead of reimplementing it
* [Revision #3427.1.241](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.241)\
  Mon 2013-06-24 20:56:49 +0200
  * [MDEV-4660](https://jira.mariadb.org/browse/MDEV-4660) SHUTDOWN command
* [Revision #3427.1.240](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.240)\
  Mon 2013-06-24 20:56:30 +0200
  * [MDEV-4617](https://jira.mariadb.org/browse/MDEV-4617) PLUGINS - Show internal Locales in I\_S
* [Revision #3427.1.239](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.239)\
  Tue 2013-06-25 12:05:52 +0400
  * Added calls for BINLOG\_GTID\_POS() function to the basic GTID test case
* [Revision #3427.1.238](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.238)\
  Mon 2013-06-24 16:33:31 +0200
  * Fix sporadic failure of test rpl.rpl\_gtid\_startpos
* [Revision #3427.1.237](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.237)\
  Fri 2013-06-21 21:23:24 +0200
  * [MDEV-4692](https://jira.mariadb.org/browse/MDEV-4692): mysql.gtid\_slave\_pos accumulates values for a domain
* [Revision #3427.1.236](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.236)\
  Fri 2013-06-21 11:53:46 +0200
  * [MDEV-4688](https://jira.mariadb.org/browse/MDEV-4688): empty @@gtid\_slave\_pos during slave commit.
* [Revision #3427.1.235](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.235)\
  Thu 2013-06-20 09:04:44 +0200
  * [MDEV-4686](https://jira.mariadb.org/browse/MDEV-4686): Temporary variable for sub\_id is 32-bit, should be 64-bit
* [Revision #3427.1.234](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.234) \[merge]\
  Tue 2013-06-18 11:18:38 +0400
  * Merge.
  * [Revision #3427.25.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.25.2)\
    Fri 2013-06-14 12:10:59 +0400
    * [MDEV-4568](https://jira.mariadb.org/browse/MDEV-4568) - Port Percona response time distribution as audit plugin
  * [Revision #3427.25.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.25.1) \[merge]\
    Mon 2013-06-10 15:07:55 +0400
    * Merge.
    * [Revision #3427.24.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.24.1) \[merge]\
      Fri 2013-06-07 12:10:45 +0400
      * Merge.
      * [Revision #3427.23.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.23.4)\
        Thu 2013-06-06 19:27:17 +0400
        * [MDEV-4594](https://jira.mariadb.org/browse/MDEV-4594) - CREATE SERVER crashes embedded
      * [Revision #3427.23.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.23.3)\
        Thu 2013-06-06 12:01:09 +0400
        * [MDEV-4568](https://jira.mariadb.org/browse/MDEV-4568) - Port Percona response time distribution as audit plugin
      * [Revision #3427.23.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.23.2)\
        Wed 2013-06-05 13:38:41 +0400
        * [MDEV-4568](https://jira.mariadb.org/browse/MDEV-4568) - Port Percona response time distribution as audit plugin Test fixes.
      * [Revision #3427.23.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.23.1)\
        Tue 2013-06-04 10:01:31 +0400
        * [MDEV-4568](https://jira.mariadb.org/browse/MDEV-4568) - Port Percona response time distribution as audit plugin
* [Revision #3427.1.233](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.233)\
  Sun 2013-06-16 22:01:07 +0200
  * [MDEV-4456](https://jira.mariadb.org/browse/MDEV-4456) Reverse discovery of ARCHIVE table on SELECT after disappearance of ARZ file
* [Revision #3427.1.232](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.232)\
  Sun 2013-06-16 17:26:27 +0200
  * remove extraneous statement from the test
* [Revision #3427.1.231](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.231)\
  Sun 2013-06-16 17:19:53 +0200
  * [MDEV-4451](https://jira.mariadb.org/browse/MDEV-4451) Attempt to write-lock a SEQUENCE table with log-bin enabled causes ER\_BINLOG\_ROW\_ENGINE
* [Revision #3427.1.230](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.230)\
  Sun 2013-06-16 17:07:15 +0200
  * [MDEV-4449](https://jira.mariadb.org/browse/MDEV-4449) SEQUENCE depends on TEST\_SQL\_DISCOVERY for discovering tables upon DDL
* [Revision #3427.1.229](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.229)\
  Sat 2013-06-15 23:53:41 +0200
  * [MDEV-4450](https://jira.mariadb.org/browse/MDEV-4450) misleading error messages from init\_from\_sql\_statement\_string()
* [Revision #3427.1.228](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.228)\
  Sat 2013-06-15 19:10:00 +0200
  * partitioning frm bugs:
* [Revision #3427.1.227](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.227)\
  Sat 2013-06-15 19:09:55 +0200
  * remove unsusd DB\_TYPE value
* [Revision #3427.1.226](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.226)\
  Sat 2013-06-15 19:09:47 +0200
  * plugin\_hton helper
* [Revision #3427.1.225](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.225)\
  Sat 2013-06-15 19:09:40 +0200
  * Fix to compile without partitioning. Remove few ifdef's
* [Revision #3427.1.224](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.224)\
  Sat 2013-06-15 19:09:31 +0200
  * [MDEV-4441](https://jira.mariadb.org/browse/MDEV-4441) DROP DATABASE with a newly created ARCHIVE table does not work
* [Revision #3427.1.223](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.223)\
  Sat 2013-06-08 12:36:21 +0200
  * Forgotten .result file update.
* [Revision #3427.1.222](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.222)\
  Fri 2013-06-07 14:39:00 +0200
  * [MDEV-4490](https://jira.mariadb.org/browse/MDEV-4490): Old-style master position points at the last GTID event after slave restart
* [Revision #3427.1.221](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.221)\
  Fri 2013-06-07 10:58:34 +0200
  * [MDEV-4486](https://jira.mariadb.org/browse/MDEV-4486): Allow to start old-style replication even if mysql.rpl\_slave\_state is unavailable
* [Revision #3427.1.220](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.220)\
  Fri 2013-06-07 09:31:11 +0200
  * [MDEV-4591](https://jira.mariadb.org/browse/MDEV-4591):Setting gtid\* values from inside a transaction might cause unexpected results
* [Revision #3427.1.219](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.219)\
  Fri 2013-06-07 08:43:21 +0200
  * [MDEV-4483](https://jira.mariadb.org/browse/MDEV-4483): CHANGE MASTER TO master\_use\_gtid=xxx looses old-style coordinates.
* [Revision #3772](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3772)\
  Wed 2013-07-17 17:46:16 +0300
  * [MDEV-4647](https://jira.mariadb.org/browse/MDEV-4647): Valgrind warnings (Conditional jump or move depends on uninitialised value) in Item\_equal::fix\_fields Fix to calm down valgrind.
* [Revision #3771](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3771)\
  Tue 2013-07-16 15:44:38 +0300
  * [MDEV-4570](https://jira.mariadb.org/browse/MDEV-4570) \[PATCH] Sys\_query\_cache\_limit initialization depends on initialization in other source files
* [Revision #3770](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3770)\
  Tue 2013-07-16 15:43:43 +0300
  * [MDEV-4548](https://jira.mariadb.org/browse/MDEV-4548) \[PATCH] Limit the amount of side-checking done in innodb-zip test
* [Revision #3769](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3769)\
  Tue 2013-07-16 15:16:38 +0300
  * [MDEV-4547](https://jira.mariadb.org/browse/MDEV-4547) \[PATCH] Make REFRESH\_\* constants to be 64-bit in 32-bit compilation
* [Revision #3768](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3768)\
  Tue 2013-07-16 12:26:04 +0300
  * [MDEV-4546](https://jira.mariadb.org/browse/MDEV-4546) Perfschema unit tests to return non-zero on failure.
* [Revision #3767](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3767)\
  Tue 2013-07-16 11:31:06 +0300
  * Building libmysqld fixed.
* [Revision #3766](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3766) \[merge]\
  Wed 2013-07-10 18:46:33 +0400
  * Merging temporal literals
  * [Revision #3763.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.2.1)\
    Wed 2013-07-10 12:12:27 +0400
    * Adding support for the SQL-standard temporal literals.
* [Revision #3765](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3765)\
  Wed 2013-07-10 11:49:17 +0400
  * Adding support for MySQL-5.6 temporal column types:
* [Revision #3764](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3764) \[merge]\
  Wed 2013-07-10 11:39:15 +0400
  * Merge from 10.0-connect
  * [Revision #3763.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.2)\
    Mon 2013-07-08 19:03:15 +0200
    * Suppress some ubuntu compiler warnings
  * [Revision #3763.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763.1.1)\
    Mon 2013-07-08 17:26:27 +0400
    * Re-enabling connect tests in 10.0-connect
* [Revision #3763](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3763) \[merge]\
  Mon 2013-07-08 17:21:47 +0400
  * Merging from 10.0-connect
  * [Revision #3746.1.84](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.84)\
    Mon 2013-07-08 12:20:12 +0200
    * Suppressing wrong code (INI tables are not indexables)
  * [Revision #3746.1.83](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.83)\
    Mon 2013-07-08 13:39:45 +0400
    * Adding instructions on how to install sqlite3 ODBC driver for test purposes.
  * [Revision #3746.1.82](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.82)\
    Mon 2013-07-08 13:11:40 +0400
    * Fixing some of the memory leaks in ODBCColumns().
  * [Revision #3746.1.81](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.81)\
    Mon 2013-07-08 11:43:45 +0400
    * Fixing a warning: - cast to pointer from integer of different size
  * [Revision #3746.1.80](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.80)\
    Mon 2013-07-08 11:28:07 +0400
    * Fixing warnings: - no previous declaration for ‘const char\* PLGtoMYSQLtype - no previous declaration for ‘int MYSQLtoPLG(int)’ - no previous declaration for ‘char\* MyDateFmt(int)’ - no previous declaration for ‘char\* MyDateFmt(char\*)’ - no previous declaration for ‘int MYSQLtoPLG(char\*)’ - no previous declaration for ‘enum\_field\_types PLGtoMYSQL
  * [Revision #3746.1.79](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.79)\
    Mon 2013-07-08 11:26:24 +0400
    * Fixing a warning: - no previous declaration for ‘void\* ThreadOpen(void\*)’
  * [Revision #3746.1.78](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.78)\
    Mon 2013-07-08 11:22:32 +0400
    * Fixing warnings: - no previous declaration for ‘bool OcrSrcCol' - no previous declaration for ‘bool OcrColumns' - no previous declaration for ‘\_qryres\* PivotColumns'
  * [Revision #3746.1.77](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.77)\
    Mon 2013-07-08 11:16:16 +0400
    * Fixing a warning: - no previous declaration for ‘int PrepareColist
  * [Revision #3746.1.76](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.76)\
    Mon 2013-07-08 11:11:53 +0400
    * Fixing warnings: - no previous declaration for ‘char\* GetIni(int)’ - no previous declaration for ‘void SetTrc()’
  * [Revision #3746.1.75](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.75)\
    Mon 2013-07-08 11:05:59 +0400
    * Fixing warnings:
  * [Revision #3746.1.74](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.74)\
    Mon 2013-07-08 10:52:20 +0400
    * fixing warnings: - no previous declaration for ‘ddwrap’ - implicit declaration of function ‘ddwrap’
  * [Revision #3746.1.73](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.73)\
    Mon 2013-07-08 10:49:50 +0400
    * Fixing a typo in the previous push
  * [Revision #3746.1.72](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.72)\
    Mon 2013-07-08 10:46:15 +0400
    * fixing warnings: - no previous declaration for ‘\_isatty’ - implicit declaration of function ‘\_isatty’
  * [Revision #3746.1.71](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.71)\
    Mon 2013-07-08 10:37:09 +0400
    * Fixing the "no previous declaration for ‘\_strerror'" warning.
  * [Revision #3746.1.70](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.70)\
    Mon 2013-07-08 10:20:53 +0400
    * Fixing numerous "variable is set but never used" warnings.
  * [Revision #3746.1.69](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.69)\
    Sat 2013-07-06 10:58:22 +0200
    * Remove unuseful option causing valgrind error or warning
  * [Revision #3746.1.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.68)\
    Fri 2013-07-05 13:13:45 +0200
    * Try to fix a uninitialised valgrind warning
  * [Revision #3746.1.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.67)\
    Thu 2013-07-04 23:13:07 +0200
    * Make sure Remark is initialised
  * [Revision #3746.1.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.66)\
    Thu 2013-07-04 20:09:50 +0200
    * Make sure Remark is initialised in ha\_connect::GetColumnOption
  * [Revision #3746.1.65](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.65)\
    Wed 2013-07-03 23:58:22 +0200
    * Makes memory check conditionally
  * [Revision #3746.1.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.64)\
    Wed 2013-07-03 12:06:49 +0200
    * Make sure result are ordered the same on all platforms
  * [Revision #3746.1.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.63)\
    Tue 2013-07-02 00:07:48 +0200
    * Fix memory leak in libdoc.cpp in LIBXMLDOC::GetNodeList replacing xmlXPathFreeNodeSetList(Xop);
    * Caused memory leak, by xmlXPathFreeObject(Xop);
  * [Revision #3746.1.62](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.62)\
    Sun 2013-06-30 19:08:09 +0200
    * Working on eliminating valgrind warning/errors
  * [Revision #3746.1.61](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.61)\
    Sun 2013-06-30 12:43:30 +0200
    * Trying to get rid of some valgrind warnings
  * [Revision #3746.1.60](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.60)\
    Sat 2013-06-29 22:53:21 +0200
    * Release storage allocated by flex
  * [Revision #3746.1.59](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.59)\
    Sat 2013-06-29 01:10:31 +0200
    * Add the PROFILE\_End function in inihandl. Called by connect\_done\_func to release the cache memory allocated by the PROFILE perocessing. (also add some break at the end of switch's to avoid warnings)
  * [Revision #3746.1.58](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.58)\
    Fri 2013-06-28 14:22:32 +0200
    * Release memory allocated by inihandl in connect\_done\_func.
  * [Revision #3746.1.57](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.57)\
    Wed 2013-06-26 20:00:15 +0200
    * Trying to remove those warnings about non virtual destructor
  * [Revision #3746.1.56](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.56)\
    Wed 2013-06-26 19:52:38 +0200
    * In connect\_assisted\_discovery the test on topt->quoted must be done on its signed value
  * [Revision #3746.1.55](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.55)\
    Wed 2013-06-26 19:42:28 +0200
    * Fix potential bug in MYSQLCOL::WriteColumn: ShowValue was call with \*Bind->length instead of Bind->buffer\_length
  * [Revision #3746.1.54](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.54)\
    Sun 2013-06-16 19:07:27 +0200
    * Implemented: The use of Federated servers.
  * [Revision #3746.1.53](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.53)\
    Fri 2013-06-14 21:00:12 +0200
    * Add a test case for multiple tables
  * [Revision #3746.1.52](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.52)\
    Fri 2013-06-14 20:52:46 +0200
    * Fix regression error for multiple 2 tables.
  * [Revision #3746.1.51](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.51)\
    Wed 2013-06-12 20:48:55 +0200
    * To avoid crashing in debug mode, the error message concerning the making of the index is changed to a warning.
  * [Revision #3746.1.50](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.50)\
    Wed 2013-06-12 16:51:12 +0200
    * Suballocate filename in TDBMUL::InitFileNames. This fix the bug [MDEV-4524](https://jira.mariadb.org/browse/MDEV-4524) but I still don't know why it happened with a stack variable. (and only on Linux)
  * [Revision #3746.1.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.49)\
    Wed 2013-06-12 11:39:57 +0200
    * Add trace in TDBMUL::GetMaxSize.
  * [Revision #3746.1.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.48)\
    Wed 2013-06-12 01:02:04 +0200
    * Fix [MDEV-4638](https://jira.mariadb.org/browse/MDEV-4638)
  * [Revision #3746.1.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.47) \[merge]\
    Sat 2013-06-08 13:04:21 +0200
    * Commit merged changes
    * [Revision #3759.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3759.1.1)\
      Sat 2013-06-08 01:20:49 +0400
      * Enabling Connect tests
  * [Revision #3746.1.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.46)\
    Sat 2013-06-08 01:02:22 +0200
    * Set timeout values in MYSQLC::Open
* [Revision #3762](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3762)\
  Thu 2013-06-27 15:18:48 +0400
  * [MDEV-4438](https://jira.mariadb.org/browse/MDEV-4438) - Spider storage engine

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
