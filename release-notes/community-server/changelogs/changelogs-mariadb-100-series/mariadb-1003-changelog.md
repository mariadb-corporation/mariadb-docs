# MariaDB 10.0.3 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.3) |[Release Notes](../../old-releases/10.0/10.0.3.md) |**Changelog** |[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 11 Jun 2013

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.3.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3761](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3761)\
  Mon 2013-06-10 08:40:25 +0200
  * remove .THIS file
* [Revision #3760](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3760)\
  Sun 2013-06-09 15:17:28 +0200
  * [MDEV-4469](https://jira.mariadb.org/browse/MDEV-4469) Fedora18 MariaDB-connect-engine packages are incorrectly asserting ownership of /usr/lib and /usr/lib64
* [Revision #3759](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3759) \[merge]\
  Sat 2013-06-08 01:16:00 +0400
  * Merge from 10.0-connect
  * [Revision #3746.1.45](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.45)\
    Sat 2013-06-08 00:24:27 +0400
    * Fixing a few compiler warnings
  * [Revision #3746.1.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.44)\
    Wed 2013-06-05 00:46:06 +0200\
    \*
    * Change CRLF line endings to LF
  * [Revision #3746.1.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.43)\
    Tue 2013-06-04 17:18:33 +0200\
    \*
    * Adding parallelism to the TBL table type
  * [Revision #3746.1.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.42)\
    Mon 2013-06-03 14:43:47 +0200
    * compiler warnings
  * [Revision #3746.1.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.41)\
    Mon 2013-06-03 11:57:34 +0400
    * Fixing the problem with my\_bool\_t defined two times. (it worked fine with the modern gcc, but failed on some other compilers).
  * [Revision #3746.1.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.40)\
    Tue 2013-05-28 21:06:15 +0200\
    \*
    * Fix crash when a null qrp is returned for OCCUR tables in connect\_assisted\_discovery
  * [Revision #3746.1.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.39)\
    Tue 2013-05-28 17:22:38 +0200\
    \*
    * Extending connect\_assisted\_discovery column automatic definition to OCCUR and PIVOT table types.
  * [Revision #3746.1.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.38)\
    Tue 2013-05-28 13:11:45 +0400
    * Recording test results forgotten in the commit adding thd\_timezone\_service.
  * [Revision #3746.1.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.37) \[merge]\
    Mon 2013-05-27 17:51:42 +0400
    * Merging with the latest 10.0
  * [Revision #3746.1.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.36)\
    Mon 2013-05-27 17:42:59 +0400\
    \*
    * Fixing embedded verision of the Connect engine when handling table\_type=MySQL (and some other types) to connect only to remote MySQL server, do not try to establish embedded connections from the running embedded connection.
  * [Revision #3746.1.35](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.35)\
    Mon 2013-05-27 12:42:39 +0400
    * Fixing ABI template, to take into account the latest change in the thd\_time\_zone\_service.
  * [Revision #3746.1.34](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.34)\
    Mon 2013-05-27 12:38:15 +0400
    * Fixing ABI template, to take into account the latest change in the thd\_time\_zone\_service.
  * [Revision #3746.1.33](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.33)\
    Mon 2013-05-27 00:17:04 +0200\
    \*
    * Fix Windows compile error
  * [Revision #3746.1.32](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.32)\
    Fri 2013-05-24 19:09:59 +0400
    * Adding the timezone plugin service, to convert between MYSQL\_TIME and my\_time\_t and back.
  * [Revision #3746.1.31](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.31)\
    Fri 2013-05-24 15:27:20 +0400
    * Do not run mysql.test in case of embedded server. We need a running MySQL server for this test.
  * [Revision #3746.1.30](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.30)\
    Fri 2013-05-24 15:21:06 +0400
    * Splitting SQLite3 tests into two parts:
  * [Revision #3746.1.29](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.29)\
    Fri 2013-05-24 11:31:43 +0400
    * Removing more cases of direct use of thd.
  * [Revision #3746.1.28](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.28)\
    Fri 2013-05-24 09:56:04 +0400
    * Removing direct access to thd, using functions: - thd\_query\_string() insted of thd->query\_string - thd\_sql\_command() instead ot thd->lex->sql\_command - table\_share->s.db.str instead of thd->db
  * [Revision #3746.1.27](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.27)\
    Fri 2013-05-24 00:19:26 +0200\
    \*
    * Fix setting default type to MYSQL->PROXY->DOS in some places where it was not done correctly. - Fix a bug causing add\_field to generate a syntax error on DOUBLE columns with a 0 decimal value. - Column can be undefined when Srcdef is specified.
  * [Revision #3746.1.26](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.26)\
    Thu 2013-05-23 12:04:52 +0400
    * Connect: fixing non thread-safe code. Passing "struct tm" buffer to GetGmTime() instead of using a static bufer.
  * [Revision #3746.1.25](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.25)\
    Wed 2013-05-22 13:35:21 +0200\
    \*
    * Changing CONNECT version number and date modified: storage/connect/ha\_connect.cc storage/connect/mysql-test/connect/r/xml.result
  * [Revision #3746.1.24](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.24)\
    Tue 2013-05-21 18:29:10 +0400
    * `mtr --suite=connect --embedded` tests did not work for two reasons:
  * [Revision #3746.1.23](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.23)\
    Mon 2013-05-20 18:17:09 +0200\
    \*
    * Correct misplaced parenthesis in last change
  * [Revision #3746.1.22](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.22)\
    Mon 2013-05-20 13:12:34 +0200\
    \*
    * Save and restore srcdef when getting a sub-table (could stay in cache)
  * [Revision #3746.1.21](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.21)\
    Sun 2013-05-19 20:16:04 +0200\
    \*
    * Removing unused copy file
  * [Revision #3746.1.20](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.20) \[merge]\
    Sun 2013-05-19 19:53:38 +0200\
    \*
    * Commit merged and resolve
    * [Revision #3746.3.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.3.4)\
      Mon 2013-05-13 16:48:03 +0400
      * Fixing warnings (mostly "no previous declaration")
    * [Revision #3746.3.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.3.3)\
      Mon 2013-05-13 15:57:49 +0400
      * Fixing compiler warnings ("no previous declaration for ...")
    * [Revision #3746.3.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.3.2)\
      Mon 2013-05-13 15:23:24 +0400
      * Fixing a few "no previous declaration" warnings
    * [Revision #3746.3.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.3.1)\
      Mon 2013-05-13 14:59:59 +0400
      * Fixing a few compilation warnings ("no previous declaration for XXX")
  * [Revision #3746.1.19](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.19)\
    Sun 2013-05-19 19:25:06 +0200\
    \*
    * Allowing views and queries as parameters for PROXY base tables NOTE: Checking for looping references cannot be done when using views as parameters. This should not be allowed on production servers and should be dependant on a system variable and/or on speciel grant.
  * [Revision #3746.1.18](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.18) \[merge]\
    Mon 2013-05-13 12:25:12 +0200\
    \*
    * Commit merged changes
    * [Revision #3746.2.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.2.2) \[merge]\
      Mon 2013-05-13 13:36:34 +0400
      * Merge from maria-10.0
    * [Revision #3746.2.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.2.1)\
      Mon 2013-05-13 13:35:56 +0400
      * Enabling `--suite=connect` by default
  * [Revision #3746.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.17)\
    Mon 2013-05-13 12:20:08 +0200\
    \*
    * Code cleaning. Eliminating unused code, functions, and variables.
  * [Revision #3746.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.16)\
    Mon 2013-05-13 11:37:34 +0200\
    \*
    * fix use of uninitialized variable (colp)
  * [Revision #3746.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.15)\
    Mon 2013-05-13 10:37:35 +0200\
    \*
    * Set tdbp to NULL when ignored
  * [Revision #3746.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.14)\
    Sun 2013-05-12 18:37:53 +0200\
    \*
    * Changing mode from +x to -x
  * [Revision #3746.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.13)\
    Sun 2013-05-12 18:14:03 +0200\
    \*
    * Code cleaning. modified: storage/connect/connect.cc storage/connect/tabutil.h
  * [Revision #3746.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.12)\
    Sat 2013-05-11 17:00:36 +0200\
    \*
    * Fix tabpivot compile errors on Linux. - Fix Tabpivot not closing the source table. - Fix pivot.test error on Linux by specifying ENDING=2 for the expenses table.
  * [Revision #3746.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.11)\
    Sat 2013-05-11 13:21:15 +0200\
    \*
    * Added a test case for PIVOT tables
  * [Revision #3746.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.10)\
    Fri 2013-05-10 23:05:16 +0200\
    \*
    * Add pivot table files and support
  * [Revision #3746.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.9)\
    Fri 2013-05-10 20:22:21 +0200\
    \*
    * Added table type PIVOT
  * [Revision #3746.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.8)\
    Thu 2013-05-09 16:16:45 +0200\
    \*
    * Fix inverted test on am in MYSQLDEF::DefineAM
  * [Revision #3746.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.7)\
    Sun 2013-05-05 12:45:26 +0200\
    \*
    * General code cleaning, eliminating a few potential bugs
  * [Revision #3746.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.6)\
    Sat 2013-05-04 00:47:55 +0200\
    \*
    * Add test for XCOL and OCCUR tables - Fix a bug causing a crash when doing an ALTER TABLE (because create\_info->alias is NULL)
  * [Revision #3746.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.5)\
    Thu 2013-05-02 16:33:15 +0200\
    \*
    * Adding a loop test to prevent PROXY based table to loop when repointing on itself. - Fix bug causing PROXY on non CONNECT tables to sometimes use the wrong DB. - Making some more tests in create that were in pre\_create not called anymore when columns are defined. - Updating some test results to reflect new warnings.
  * [Revision #3746.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.4)\
    Tue 2013-04-30 17:48:18 +0200\
    \*
    * Change in connect\_assisted\_discovery the default value for port from MYSQL\_PORT to 0. So it can be later set to mysqld\_port if necessary. Doing so, it is no more required to specify port when using the current port and the current port is not equal to MYSQL\_PORT (3306)
  * [Revision #3746.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.3)\
    Tue 2013-04-30 16:16:32 +0200\
    \*
    * Allow PROXY based tables to specify MySQL access parameters when the object table is not a CONNECT table. This was the case in previous versions but was no more possible with recent changes.
  * [Revision #3746.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.2)\
    Mon 2013-04-29 17:47:23 +0200\
    \*
    * Fix a bug causing a crash when using OEM tables based on BIN tables.
  * [Revision #3746.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746.1.1)\
    Mon 2013-04-29 13:50:20 +0200\
    \*
    * Adding 3 new table types: PROXY table base on another table. Used by several other types. XCOL proxy on a table having a colummn containing a list of values OCCUR proxy on a table having several columns containing the same type of values that can be put in a unique column and several rows. TBL Not new but now internally using the PROXY table class. - Fix 2 bugs in add\_field: Change '=' to ' ' after the COMMENT keyword. Quote column names between '\`' in the SQL string. - Update xml test result to the CONNECT version
* [Revision #3758](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3758) \[merge]\
  Thu 2013-06-06 21:32:29 +0200
  * 10.0-base merge (without InnoDB - all InnoDB changes were ignored)
  * [Revision #3427.1.218](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.218) \[merge]\
    Thu 2013-06-06 17:51:28 +0200
    * 5.5 merge
    * [Revision #3413.21.242](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.242)\
      Sat 2013-06-01 21:33:26 +0200
      * Fix a compile warning on NetBSD
    * [Revision #3413.21.241](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.241)\
      Sat 2013-06-01 21:30:33 +0200
      * [MDEV-4607](https://jira.mariadb.org/browse/MDEV-4607) : libreadline-related compilation problems on NetBSD.
    * [Revision #3413.21.240](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.240)\
      Thu 2013-05-30 08:23:49 +0300
      * [MDEV-4520](https://jira.mariadb.org/browse/MDEV-4520): Assertion \`0' fails in Query\_cache::end\_of\_result on concurrent drop event and event executio
    * [Revision #3413.21.239](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.239)\
      Tue 2013-05-28 21:25:59 +0200
      * followup for revision 3751 "centos5 gcc 4.1 asm bug" remove the workaround from cmake/os/FreeBSD.cmake
    * [Revision #3413.21.238](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.238)\
      Thu 2013-05-23 17:05:31 +0300
      * [MDEV-4520](https://jira.mariadb.org/browse/MDEV-4520): Assertion \`0' fails in Query\_cache::end\_of\_result on concurrent drop event and event execution
    * [Revision #3413.21.237](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.237)\
      Wed 2013-05-22 16:44:44 +0200
      * [MDEV-4548](https://jira.mariadb.org/browse/MDEV-4548) - compile sphinx.so/dll and include into packages
    * [Revision #3413.21.236](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.236)\
      Mon 2013-05-27 16:35:42 +0200
      * [MDEV-4553](https://jira.mariadb.org/browse/MDEV-4553) - Fixes for compilation under NetBSD.
    * [Revision #3413.21.235](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.235)\
      Fri 2013-05-24 14:33:04 +0200
      * [MDEV-4516](https://jira.mariadb.org/browse/MDEV-4516) SELECT from I\_S.QUERY\_CACHE\_INFO produces ER\_UNKNOWN\_ERROR when query cache size is 0
    * [Revision #3413.21.234](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.234)\
      Tue 2013-05-21 18:56:35 +0200
      * fix for compiled-in FederatedX
    * [Revision #3413.21.233](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.233)\
      Tue 2013-05-21 13:03:37 +0200
      * [MDEV-388](https://jira.mariadb.org/browse/MDEV-388) Creating a federated table with a non-existing server returns a random error code (part 2)
    * [Revision #3413.21.232](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.232) \[merge]\
      Tue 2013-05-21 09:43:34 +0200
      * 5.3 merge
      * [Revision #2502.567.103](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.103)\
        Tue 2013-05-21 09:42:10 +0200
        * fixes for buildbot
    * [Revision #3413.21.231](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.231)\
      Mon 2013-05-20 23:58:44 +0200
      * [MDEV-388](https://jira.mariadb.org/browse/MDEV-388) Creating a federated table with a non-existing server returns a random error code
    * [Revision #3413.21.230](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.230)\
      Mon 2013-05-20 13:41:03 +0200
      * increase MAX\_HA (number of simultaneously installed storage engines) to 64
    * [Revision #3413.21.229](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.229) \[merge]\
      Mon 2013-05-20 12:36:30 +0200
      * 5.3 merge. change maria.distinct to use a function that doesn't require ssl-enabled builds
      * [Revision #2502.567.102](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.102) \[merge]\
        Mon 2013-05-20 11:13:07 +0200
        * 5.2 merge
        * [Revision #2502.566.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.49) \[merge]\
          Mon 2013-05-20 10:53:04 +0200
          * 5.1 merge
          * [Revision #2502.565.49](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.49)\
            Sat 2013-05-11 20:23:57 +0300
            * Fixed compiler failure on solaris
          * [Revision #2502.565.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.48)\
            Sat 2013-05-11 18:57:06 +0300
            * Fixed compiler warning
          * [Revision #2502.565.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.47)\
            Sat 2013-05-11 15:55:11 +0300
            * [MDEV-4280](https://jira.mariadb.org/browse/MDEV-4280): Assertion \`empty\_size == empty\_size\_on\_page' failure in ma\_blockrec.c or ER\_NOT\_KEYFILE on query with DISTINCT and GROUP BY This could happen when using Aria for internal temporary files (default case) and using DISTINCT. \_ma\_scan\_restore\_block\_record() didn't work correctly if there was rows inserted, updated or deleted on the handler between calls to \_ma\_scan\_remember\_block\_record() and \_ma\_scan\_restore\_block\_record(). The effect was that some DISTINCT queries that used remove\_dup\_with\_compare() could fail.
          * [Revision #2502.565.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.46)\
            Tue 2013-04-09 09:58:51 +0300
            * [MDEV-4326](https://jira.mariadb.org/browse/MDEV-4326) fix.
        * [Revision #2502.566.48](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.48)\
          Sun 2013-05-19 16:38:56 +0200
          * [MDEV-4544](https://jira.mariadb.org/browse/MDEV-4544) - update MSI to include HeidiSQL 8.0
        * [Revision #2502.566.47](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.47)\
          Sun 2013-05-19 16:22:33 +0200
          * Fix cpack error - safe\_process.pl does not exist anymore.
        * [Revision #2502.566.46](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.46)\
          Wed 2013-05-08 14:32:32 +0200
          * [MDEV-4462](https://jira.mariadb.org/browse/MDEV-4462) mysqld gets SIGFPE when mysql.user table is empty
      * [Revision #2502.567.101](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.101)\
        Fri 2013-05-03 16:07:13 +0300
        * [MDEV-4290](https://jira.mariadb.org/browse/MDEV-4290): Fix agregate function resolution in derived tables (no name resolution over a derived table border)
      * [Revision #2502.567.100](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.100) \[merge]\
        Sun 2013-05-05 05:32:55 +0400
        * Merge
    * [Revision #3413.21.228](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.228)\
      Sun 2013-05-19 17:42:30 +0200
      * remove start menu shortcut to upgrade wizard
    * [Revision #3413.21.227](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.227)\
      Sun 2013-05-19 17:41:22 +0200
      * [MDEV-4544](https://jira.mariadb.org/browse/MDEV-4544) : Update MSI installer to use latest HeidiSQL 8.0
    * [Revision #3413.21.226](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.226)\
      Fri 2013-05-17 10:16:56 +0400
      * Bug#[MDEV-4518](https://jira.mariadb.org/browse/MDEV-4518) Server crashes in is\_white\_space when it's run with query cache, charset ucs2 and collation ucs2\_unicode\_ci
    * [Revision #3413.21.225](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.225)\
      Wed 2013-05-15 16:28:12 +0300\
      \*
      * Solaris fixes: - Fixed that wait\_timeout\_func and wait\_timeout tests works on solaris - We have to compile without NO\_ALARM on Solaris as Solaris doesn't support timeouts on sockets with setsockopt(.. SO\_RCVTIMEO). - Fixed that compile-solaris-amd64-debug works (before that we got a wrong ELF class: ELFCLASS64 on linkage) - Fixed some compiler warnings - Fixed some failing tests
    * [Revision #3413.21.224](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.224)\
      Wed 2013-05-15 02:36:37 +0500
      * [MDEV-4266](https://jira.mariadb.org/browse/MDEV-4266) Server upgrade via apt-get install does not work. Now empty 'highlevel' packages strictly depend on the same versions of files. These are mariadb-server, mariadb-client, mariadb-test
    * [Revision #3413.21.223](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.223)\
      Wed 2013-05-15 02:33:29 +0500
      * [MDEV-4521](https://jira.mariadb.org/browse/MDEV-4521) MBRContains, MBRWithin no longer work with geometries of different type. get\_mm\_leaf function can store all sorts of spatial features in one type of field it receives from an Item\_field. So we just allow that by setting the type of this field to GEOMETRY.
    * [Revision #3413.21.222](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.222)\
      Tue 2013-05-14 18:32:16 +0300
      * When one does 'REPAIR TABLE', update uuid() to the current system
    * [Revision #3413.21.221](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.221)\
      Tue 2013-05-14 14:49:52 +0200
      * Fix test failure in plugins.unix\_socket when running tests as user root.
    * [Revision #3413.21.220](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.220)\
      Mon 2013-05-13 16:11:39 +0200
      * [MDEV-4514](https://jira.mariadb.org/browse/MDEV-4514) After increasing user name length mysql.db is reported broken and event scheduler does not start
    * [Revision #3413.21.219](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.219)\
      Mon 2013-05-13 15:49:48 +0200
      * [MDEV-4505](https://jira.mariadb.org/browse/MDEV-4505) Buffer overrun when processing `--log-bin` parameter without file name
    * [Revision #3413.21.218](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.218)\
      Mon 2013-05-13 15:49:27 +0200
      * [MDEV-4199](https://jira.mariadb.org/browse/MDEV-4199) Installing postfix on CentOS 5.9 requires MariaDB-server
    * [Revision #3413.21.217](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.217)\
      Mon 2013-05-13 15:46:58 +0200
      * fix test cases
    * [Revision #3413.21.216](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.216)\
      Mon 2013-05-13 00:43:46 +0300
      * Fixed [MDEV-4291](https://jira.mariadb.org/browse/MDEV-4291): Assertion \`trid >= info->s->state.create\_trid' failure or data corruption (key points to record outside datafile) on INSERT into an Aria table.
    * [Revision #3413.21.215](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.215)\
      Sun 2013-05-12 11:29:16 +0300
      * [MDEV-3999](https://jira.mariadb.org/browse/MDEV-3999): Valgrind errors 'invalid write' or assorted server crashes on concurrent flow with partitioned Aria tables [MDEV-3989](https://jira.mariadb.org/browse/MDEV-3989): Server crashes on import from MariaDB mysqldump export with partitioned Aria table.
    * [Revision #3413.21.214](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.214)\
      Sat 2013-05-11 20:31:50 +0300
      * Fixed that SHOW PROCESSLIST and information\_schema.processlist uses the right length for user names. Fixed some failing tests
    * [Revision #3413.21.213](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.213)\
      Sat 2013-05-11 12:20:21 +0300
      * [MDEV-4231](https://jira.mariadb.org/browse/MDEV-4231): Possible bug in function \_ma\_apply\_undo\_row\_insert() Added comment to clearify the code.
    * [Revision #3413.21.212](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.212)\
      Thu 2013-05-09 23:25:57 +0200
      * Fix compile error
    * [Revision #3413.21.211](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.211)\
      Thu 2013-05-09 22:21:07 +0200
      * Small mysql\_install\_db.exe fixes - Use lc-messages-dir instead of deprecated `--language` when running mysqld in bootstrap mode. - Add some verbosity to mysql\_install\_db.exe when it runs in course of MSI installation.
    * [Revision #3413.21.210](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.210)\
      Wed 2013-05-08 20:37:17 +0200
      * [MDEV-4206](https://jira.mariadb.org/browse/MDEV-4206) : log all slow statements (do not use filters), if log\_slow\_filter is empty.
    * [Revision #3413.21.209](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.209)\
      Wed 2013-05-08 13:36:17 +0400
      * The bug [MDEV-4489](https://jira.mariadb.org/browse/MDEV-4489) "Replication of big5, cp932, gbk, sjis strings makes wrong values on slave" has been fixed.
    * [Revision #3413.21.208](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.208) \[merge]\
      Wed 2013-05-08 10:12:21 +0200
      * Merge with XtraDB as of Percona-Server-5.5.30-rel30.2
      * [Revision #0.12.62](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.62)\
        Wed 2013-05-08 09:52:54 +0200
        * Percona-Server-5.5.30-rel30.2.tar.gz
    * [Revision #3413.21.207](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.207)\
      Tue 2013-05-07 18:28:36 +0200
      * centos5 gcc 4.1 asm bug
    * [Revision #3413.21.206](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.206)\
      Tue 2013-05-07 18:26:22 +0200
      * Compilation warnings. openssl compilation problem.
    * [Revision #3413.21.205](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.205) \[merge]\
      Tue 2013-05-07 13:05:09 +0200
      * mysql-5.5.31 merge
      * [Revision #3077.184.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3077.184.3) \[merge]\
        Thu 2013-01-10 10:11:53 +1100
        * Merge from mysql-5.1 to mysql-5.5.
        * [Revision #2661.844.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2661.844.2)\
          Thu 2013-01-10 10:01:50 +1100
          * Bug#13997024 SEGV IN SYNC\_ARRAY\_CELL\_PRINT PRINTING OUT LONG SEMAPHORE WAIT DATA
    * [Revision #3413.21.204](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.204)\
      Mon 2013-05-06 16:51:41 +0300
      * If one declared several continue handler for the same condition on different level of stored procedures, all of them where executed. Now we only execute the innermost of them (the most relevant).
    * [Revision #3413.21.203](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.203) \[merge]\
      Sun 2013-05-05 05:38:09 +0400
      * [MDEV-4482](https://jira.mariadb.org/browse/MDEV-4482) fix null-merged to 5.5
      * [Revision #3413.31.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.31.1) \[merge]\
        Sun 2013-05-05 05:29:33 +0400
        * Merge
        * [Revision #2502.582.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.582.1)\
          Sun 2013-05-05 05:27:02 +0400
          * [MDEV-4482](https://jira.mariadb.org/browse/MDEV-4482): main.windows test fails in buildbot with result mismatch - Rollback an earlier patch (was pushed into 5.3 instead of 5.5)
    * [Revision #3413.21.202](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.202) \[merge]\
      Sat 2013-05-04 21:56:45 -0700
      * Merge 5.3->5.5
      * [Revision #2502.567.99](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.99)\
        Fri 2013-05-03 22:46:45 -0700
        * Fixed bug [MDEV-4336](https://jira.mariadb.org/browse/MDEV-4336). When iterating over a list of conditions using List\_iterator the function remove\_eq\_conds should skip all predicates that replace a condition from the list. Otherwise it can come to an infinite recursion.
      * [Revision #2502.567.98](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.98)\
        Fri 2013-05-03 18:45:20 -0700
        * Made consistent handling of the predicates of the form IS NULL in outer joins with that in inner joins. Previously such condition was transformed into the condition = 0 unless the field belonged to an inner table of an outer join. In this case the predicate was interpreted as for any other field. Now if the field in the predicate IS NULL belongs to an inner table of an outer join the predicate is transformed into the disjunction = 0 OR IS NULL. This is fully compatible with the semantics of such predicates in 5.5.
      * [Revision #2502.567.97](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.97)\
        Mon 2013-04-29 20:31:40 -0700
        * Fixed bug [MDEV-4274](https://jira.mariadb.org/browse/MDEV-4274). This bug was the result of incompleteness of the patch for bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177). When an OR condition is simplified to a single conjunct it is merged into the embedding AND condition. Multiple equalities are also merged, and any field item involved in those equality should acquire a pointer to a the multiple equality formed by this merge.
    * [Revision #3413.21.201](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.201)\
      Sat 2013-05-04 20:42:43 +0400
      * [MDEV-4071](https://jira.mariadb.org/browse/MDEV-4071): Valgrind warnings 'Invalid read' in subselect\_engine::calc\_const\_tables with ... - Call tmp\_having->update\_used\_tables() _before_ we have call JOIN::cleanup(). Making the call after join::cleanup() is not allowed, because subquery predicate items walk parent join's JOIN\_TAB structures. Which can be invalidated by JOIN::cleanup().
    * [Revision #3413.21.200](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.200)\
      Sat 2013-05-04 21:02:07 +0400
      * [MDEV-389](https://jira.mariadb.org/browse/MDEV-389): Wrong result (missing row) with semijoin, join\_cache\_level>4 ... - Added testcase
    * [Revision #3413.21.199](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.199)\
      Sat 2013-05-04 13:05:24 +0400
      * Update testcase result
    * [Revision #3413.21.198](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.198)\
      Sat 2013-05-04 01:08:20 +0400
      * [MDEV-4270](https://jira.mariadb.org/browse/MDEV-4270): crash in fix\_semijoin\_strategies\_for\_picked\_join\_order - Added testcase
    * [Revision #3413.21.197](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.197)\
      Sat 2013-05-04 00:56:50 +0400
      * [MDEV-621](https://jira.mariadb.org/browse/MDEV-621): [Bug #693329](https://bugs.launchpad.net/bugs/693329) - Assertion \`!is\_interleave\_error' failed on low optimizer\_search\_depth - When restore\_prev\_nj\_state() is called for the table that is the last remaining child of a nested join, do not leave that nested join's bit in join->cur\_embedding\_map.
    * [Revision #3413.21.196](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.196)\
      Fri 2013-05-03 00:10:43 +0400
      * [MDEV-4465](https://jira.mariadb.org/browse/MDEV-4465): Reproducible crash (mysqld got signal 11) in multi\_delete::initialize\_tables... - make multi\_delete::initialize\_tables() take into account that the JOIN structure may have semi-join nests (which are not fully initialized when this function is called, they have tab->table=NULL which caused the crash) - Also checked multi\_update::initialize\_tables(): it has a different logic and needed no fixing.
    * [Revision #3413.21.195](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.195)\
      Tue 2013-04-30 00:29:47 +0200
      * [MDEV-4458](https://jira.mariadb.org/browse/MDEV-4458) - Windows installer does not launch upgrade wizard anymore, even if there are upgradable instances (i.e windows service of lower MariaDB/MySQL version)
    * [Revision #3413.21.194](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.194)\
      Sun 2013-04-28 14:28:46 +0200
      * fix test on Windows
    * [Revision #3413.21.193](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.193)\
      Sat 2013-04-27 23:28:48 -0700
      * Fixed bug [MDEV-4340](https://jira.mariadb.org/browse/MDEV-4340). The function make\_join\_statistics checks whether eq\_ref access uses only constant expressions, and, if this is the case the function performs constant row substitution. The code of this check must take into account hidden components of extended secondary keys.
    * [Revision #3413.21.192](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.192)\
      Thu 2013-04-25 15:11:59 +0200
      * Fix build on Windows
    * [Revision #3413.21.191](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.191)\
      Thu 2013-04-25 13:16:35 +0200
      * Fix unsigned/signed conversion bug in event type during mysql\_binlog\_send().
    * [Revision #3413.21.190](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.190)\
      Mon 2013-04-22 16:22:39 +0200
      * [MDEV-4396](https://jira.mariadb.org/browse/MDEV-4396): Fix sporadic failure of test innodb.innodb\_bug14676111
    * [Revision #3413.21.189](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.189)\
      Fri 2013-04-19 12:50:16 +0200
      * [MDEV-260](https://jira.mariadb.org/browse/MDEV-260) auditing table accesses
    * [Revision #3413.21.188](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.188)\
      Fri 2013-04-19 12:08:55 +0200
      * [MDEV-4398](https://jira.mariadb.org/browse/MDEV-4398) - Change default for innodb\_use\_fallocate to FALSE, due to bugs in older Linux kernels (posix\_fallocate() does not always guarantee that file size is like one specified)
    * [Revision #3413.21.187](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.187)\
      Thu 2013-04-18 22:17:29 +0200
      * [MDEV-4332](https://jira.mariadb.org/browse/MDEV-4332) Increase username length from 16 characters
    * [Revision #3413.21.186](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.186)\
      Wed 2013-04-17 19:42:34 +0200
      * strmake\_buf(X,Y) helper, equivalent to strmake(X,Y,sizeof(X)-1) with a bit of lame protection against abuse.
  * [Revision #3427.1.217](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.217)\
    Thu 2013-06-06 17:38:07 +0200
    * fix compile error
  * [Revision #3427.1.216](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.216)\
    Thu 2013-06-06 15:51:36 +0300
    * Fixed timing failure in myisam-metadata.test
  * [Revision #3427.1.215](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.215)\
    Wed 2013-06-05 15:32:44 +0200
    * Fix two small problems in previous push.
  * [Revision #3427.1.214](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.214)\
    Wed 2013-06-05 14:32:47 +0200
    * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
  * [Revision #3427.1.213](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.213)\
    Mon 2013-06-03 07:41:38 +0200
    * [MDEV-4605](https://jira.mariadb.org/browse/MDEV-4605): Failing to load GTID slave position from rpl.gtid\_slave\_pos
  * [Revision #3427.1.212](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.212)\
    Wed 2013-05-29 14:23:40 +0200
    * [MDEV-4485](https://jira.mariadb.org/browse/MDEV-4485): Incorrect error handling in record\_gtid().
  * [Revision #3427.1.211](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.211)\
    Wed 2013-05-29 11:41:25 +0200
    * [MDEV-4485](https://jira.mariadb.org/browse/MDEV-4485): Master did not allow slave to connect from the very start (empty GTID pos) if GTIDs from other multi\_source master was present
* [Revision #3757](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3757)\
  Wed 2013-06-05 13:51:28 +0300\
  \*
  * Fixed compiler warning - Don't abort InnoDB if one can't allocate resources for AIO (this patch was in 5.5 and 10.0-base but was missing in 10.0)
* [Revision #3756](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3756) \[merge]\
  Tue 2013-05-28 16:35:52 +0200
  * merge compile fix 10.0-base -> 10.0
  * [Revision #3427.1.210](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.210)\
    Tue 2013-05-28 16:35:05 +0200
    * Fix type-typo which caused windows build failure.
* [Revision #3755](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3755) \[merge]\
  Tue 2013-05-28 15:46:32 +0200
  * Merge 10.0-base -> 10.0
  * [Revision #3752.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3752.1.1) \[merge]\
    Tue 2013-05-28 15:39:56 +0200
    * Merge 10.0-base -> 10.0
    * [Revision #3427.1.209](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.209)\
      Tue 2013-05-28 13:28:31 +0200
      * [MDEV-4478](https://jira.mariadb.org/browse/MDEV-4478): Implement GTID "strict mode"
    * [Revision #3427.1.208](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.208)\
      Sat 2013-05-25 06:32:00 +0200
      * [MDEV-4475](https://jira.mariadb.org/browse/MDEV-4475) follow-up patch: Add forgotten initialisation of the padding for empty Gtid\_List event
    * [Revision #3427.1.207](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.207)\
      Fri 2013-05-24 22:21:08 +0200
      * [MDEV-4475](https://jira.mariadb.org/browse/MDEV-4475): Replication from [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) to 5.5 does not work
    * [Revision #3427.1.206](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.206)\
      Wed 2013-05-22 17:36:48 +0200
      * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
    * [Revision #3427.1.205](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.205)\
      Thu 2013-05-16 12:41:11 +0200
      * Fix race condition in binlog dump thread during server shutdown.
    * [Revision #3427.1.204](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.204)\
      Wed 2013-05-15 19:52:21 +0200
      * [MDEV-26](https://jira.mariadb.org/browse/MDEV-26): Global transaction ID.
    * [Revision #3427.1.203](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.203)\
      Fri 2013-05-10 16:01:38 +0300
      * Merge of patch lp:ahiguti100/maria/handlersocket-fix-78 by Akira Higuchi A bugfix of HandlerSocket is not applied to mariadb yet
    * [Revision #3427.1.202](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.202)\
      Fri 2013-05-10 12:32:34 +0300
      * Added some fixes that should make MyISAM & Aria REPAIR work with more than 4G records - If one specifies `--force` twice to myisamchk and aria\_chk, then we will try to finnish the repair even if sort\_buffer would be too small. This was done by dynamically allocate buffer handler objects as long as memory lasts. - New option for myisamchk and aria\_chk: create-missing-keys - Changed default size of myisam\_sort\_buffer\_size from 8M to 128M. - Changed default size of sort\_buffer\_size in aria\_chk from 128M to 256M. - Increased information in error message about 'sort\_buffer\_size' beeing to small. - Print also to 'show warnings' if repair was retried. - Increased size of internal sort-buffer-readers from 16K to 128K - Changed printing of 'number of records' to use %ll instead of casting to long - Changed buffer sizes for myisam and aria to use MY\_ALIGN\_DOWN() to get same number of bytes allocated on different machines.
    * [Revision #3427.1.201](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.201)\
      Mon 2013-05-06 14:35:34 +0200
      * Fix big problem in previous push. (Relay log cleanup would nuke binlog state)
    * [Revision #3427.1.200](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.200)\
      Sun 2013-05-05 21:39:31 +0300
      * Fixed errors and compiler warnings found by buildbot Solaris fixes: - Fixed that wait\_timeout\_func and wait\_timeout tests works on solaris - We have to compile without NO\_ALARM on Solaris as Solaris doesn't support timeouts on sockets with setsockopt(.. SO\_RCVTIMEO). - Fixed that compile-solaris-amd64-debug works (before that we got a wrong ELF class: ELFCLASS64 on linkage) - Added missing sync\_with\_master Other bug fixes: - Free memory for rpl\_global\_gtid\_binlog\_state before exit() to avoid 'accessing uninitalized mutex' error.
* [Revision #3754](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3754)\
  Tue 2013-05-28 13:32:39 +0400
  * [MDEV-4001](https://jira.mariadb.org/browse/MDEV-4001): Cassandra: server crashes in ha\_cassandra::end\_bulk\_insert on INSERT .. SELECT with a non-existing column - INSERT ... SELECT may call handler->end\_bulk\_insert() without having called handler->start\_bulk\_insert(). Let Cassandra SE handle this.
* [Revision #3753](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3753)\
  Tue 2013-05-28 12:38:22 +0400
  * [MDEV-4443](https://jira.mariadb.org/browse/MDEV-4443): Cassandra SE: ERROR 1928 (HY000): Internal error: 'Thrift exception: Called write on non-open socket' - Made call re-try system also handle network disconnects (it will reconnect before retrying) - Added Cassandra\_network\_exceptions counter. - @@cassandra\_failure\_retries is now always honored.
* [Revision #3752](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3752)\
  Thu 2013-05-23 14:52:48 +0200
  * [MDEV-4566](https://jira.mariadb.org/browse/MDEV-4566) : Failing DBUG\_ASSERT() in SELECT SLEEP(), with threadpool.
* [Revision #3751](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3751)\
  Mon 2013-05-20 08:37:03 +0400
  * [MDEV-4000](https://jira.mariadb.org/browse/MDEV-4000): Mapping between Cassandra blob (BytesType) and MySQL BLOB does not work - Allow SQL blobs in the data mapping.
* [Revision #3750](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3750)\
  Mon 2013-05-20 08:06:34 +0400
  * Update test results.
* [Revision #3749](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3749) \[merge]\
  Fri 2013-05-03 12:10:16 +0200
  * Merge 10.0-base -> 10.0
  * [Revision #3427.1.199](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.199)\
    Fri 2013-05-03 11:27:29 +0200
    * [MDEV-4473](https://jira.mariadb.org/browse/MDEV-4473): mysql\_binlog\_send() starts sending events from wrong GTID position in some master failover scenarios
  * [Revision #3427.1.198](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.198)\
    Fri 2013-05-03 01:54:47 +0300
    * Instead of writing "Errcode" to the log for Slave errors, use "Internal MariaDB error code" This makes it clear that the error code has nothing to do with errno.
  * [Revision #3427.1.197](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.197)\
    Fri 2013-05-03 01:50:42 +0300
    * Fixed: [MDEV-4352](https://jira.mariadb.org/browse/MDEV-4352); LOAD DATA was not multi-source safe - Calls to cleanup\_load\_tmpdir() could delete temporary files for another master connection - Concurrent LOAD DATA commands from two master connections could use the same file name
* [Revision #3748](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3748) \[merge]\
  Mon 2013-04-29 12:03:54 +0200
  * Merge 10.0-base -> 10.0
  * [Revision #3427.1.196](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.196)\
    Mon 2013-04-29 10:57:48 +0200
    * [MDEV-4446](https://jira.mariadb.org/browse/MDEV-4446): Incorrect handling of binlog checksum when searching for GTID start position in binlog
  * [Revision #3427.1.195](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.195)\
    Thu 2013-04-25 13:25:14 +0200
    * Fix more failures in buildbot.
  * [Revision #3427.1.194](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.194)\
    Wed 2013-04-24 13:05:40 +0200
    * Add missing check for thd->killed in mysql\_binlog\_send().
* [Revision #3747](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3747)\
  Sun 2013-04-28 10:18:31 +0400
  * Fixing that ODBC detection always failed on Linux because
* [Revision #3746](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3746)\
  Thu 2013-04-25 17:12:52 +0400
  * ha\_cassandra.so and ha\_oqgraph.so can be build only if boost is installed on the build machine. So put them into the deb packages optionally.
* [Revision #3745](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3745)\
  Wed 2013-04-24 18:20:22 +0400
  * Adding ha\_oqgraph.so and ha\_cassandra.so back into the Debian and Ubuntu packages (they were unintentionally removed while moving ha\_connect.so into a separate package).
* [Revision #3744](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3744) \[merge]\
  Mon 2013-04-22 20:55:22 -0700
  * Merge 10.0-base -> 10.0
  * [Revision #3427.1.193](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.193) \[merge]\
    Mon 2013-04-22 07:40:54 -0700
    * Merge from mwl253
    * [Revision #3427.18.44](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.44)\
      Mon 2013-04-22 12:18:46 +0300
      * Make test working on case insensitive file system
  * [Revision #3427.1.192](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.1.192) \[merge]\
    Sun 2013-04-21 22:44:19 -0700
    * Merge mwl253 -> 10.0-base
    * [Revision #3427.18.43](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.43)\
      Mon 2013-04-22 06:46:26 +0300
      * Removed comparison of table names.
    * [Revision #3427.18.42](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.42)\
      Sun 2013-04-21 22:12:57 +0300
      * decode\_histogram fixed to show delta of the last value with maximum.
    * [Revision #3427.18.41](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.41)\
      Sun 2013-04-21 21:39:01 +0300
      * Fix of the test suite.
    * [Revision #3427.18.40](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.40)\
      Sat 2013-04-20 18:18:01 -0700
      * Changed a test case.
    * [Revision #3427.18.39](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.39)\
      Sat 2013-04-20 23:30:21 +0300
      * [MDEV-4402](https://jira.mariadb.org/browse/MDEV-4402) A function to visualize histograms data.
    * [Revision #3427.18.38](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.38) \[merge]\
      Sat 2013-04-20 02:24:01 -0700
      * Merge. Fixed a wrong result from `mysqld--help.test`.
      * [Revision #3427.22.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.22.2)\
        Fri 2013-04-19 19:35:13 +0300
        * [MDEV-4345](https://jira.mariadb.org/browse/MDEV-4345): fixed optimizer\_selectivity\_sampling\_limit default value.
      * [Revision #3427.22.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.22.1)\
        Fri 2013-04-19 18:59:46 +0300
        * [MDEV-4345](https://jira.mariadb.org/browse/MDEV-4345): Fixed system variables tests.
    * [Revision #3427.18.37](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.37)\
      Sat 2013-04-20 02:16:55 -0700
      * Fixed bug [MDEV-4406](https://jira.mariadb.org/browse/MDEV-4406). This bug in the code of get\_column\_range\_cardinality() could lead to wrong estimates of number of records in ranges for non-nullable columns.
    * [Revision #3427.18.36](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.18.36)\
      Thu 2013-04-18 22:22:04 +0300
      * [MDEV-4345](https://jira.mariadb.org/browse/MDEV-4345)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
