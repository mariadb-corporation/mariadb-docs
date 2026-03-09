# MariaDB 5.5.38 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.38)[Release Notes](../../old-releases/5.5/5.5.38.md)[Changelog](mariadb-5538-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 9 Jun 2014

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.38.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4214](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4214)\
  Thu 2014-06-05 19:25:51 +0200
  * fix range.test
* [Revision #4213](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4213)\
  Thu 2014-06-05 19:18:35 +0400
  * [MDEV-6105](https://jira.mariadb.org/browse/MDEV-6105): Emoji unicode character string search query makes mariadb performance down - When range optimizer cannot the lookup value into \[VAR]CHAR(n) column, it should produce: = "Impossible range" for equality = "no range" for non-equalities.
* [Revision #4212](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4212) \[merge]\
  Thu 2014-06-05 09:15:25 +0400
  * Merge 5.3->5.5
  * [Revision #2502.567.232](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.232)\
    Thu 2014-06-05 09:01:05 +0400
    * Fixing a valgrind warning introduced in the previous changeset: "have\_warnings" was set to an uninialized value when converting a negative number to datetime.
* [Revision #4211](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4211) \[merge]\
  Wed 2014-06-04 21:53:15 +0400
  * Merge 5.3->5.5
  * [Revision #2502.567.231](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.231)\
    Wed 2014-06-04 20:32:57 +0400
    * [MDEV-4858](https://jira.mariadb.org/browse/MDEV-4858) Wrong results for a huge unsigned value inserted into a TIME column [MDEV-6099](https://jira.mariadb.org/browse/MDEV-6099) Bad results for DATE\_ADD(.., INTERVAL 2000000000000000000.0 SECOND) [MDEV-6097](https://jira.mariadb.org/browse/MDEV-6097) Inconsistent results for CAST(int,decimal,double AS DATETIME) [MDEV-6100](https://jira.mariadb.org/browse/MDEV-6100) No warning on CAST(9000000 AS TIME)
* [Revision #4210](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4210)\
  Wed 2014-06-04 10:10:19 +0300
  * [MDEV-6163](https://jira.mariadb.org/browse/MDEV-6163): Error while executing an update query that has the same table in a sub-query
* [Revision #4209](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4209)\
  Tue 2014-06-03 10:58:03 +0200
  * mark tokudb in 5.5 as MariaDB\_PLUGIN\_MATURITY\_GAMMA, not MariaDB\_PLUGIN\_MATURITY\_ALPHA.
* [Revision #4208](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4208)\
  Tue 2014-06-03 10:57:57 +0200
  * cmake: mark AIO\_LIBRARY, EVENT\_LIBRARY, GROFF, NROFF as advanced; use -ggdb3 if supported
* [Revision #4207](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4207)\
  Tue 2014-06-03 10:52:36 +0200
  * Add a test case for MySQL's: Bug #18167356: EXPLAIN W/ EXISTS(SELECT\* UNION SELECT\*) WHERE ONE OF SELECT\* IS DISTINCT FAILS.
* [Revision #4206](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4206) \[merge]\
  Tue 2014-06-03 09:55:08 +0200
  * mysql-5.5.38 merge
* [Revision #4205](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4205) \[merge]\
  Tue 2014-06-03 09:53:10 +0200
  * merge with XtraDB 5.5.37-35.0
  * [Revision #0.12.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.68)\
    Mon 2014-06-02 23:25:54 +0200
    * percona-server-5.5.37-35.0.tar.gz
* [Revision #4204](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4204) \[merge]\
  Mon 2014-06-02 19:08:59 +0200
  * 5.3 merge
  * [Revision #2502.567.230](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.230) \[merge]\
    Mon 2014-06-02 17:38:58 +0200
    * 5.2 merge
    * [Revision #2502.566.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.70) \[merge]\
      Mon 2014-06-02 17:33:08 +0200
      * 5.1 merge
      * [Revision #2502.565.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.70)\
        Wed 2014-04-23 01:16:41 +0400
        * Change in the result file merged from 5.1 did not take into account MariaDB-specific result replacement
      * [Revision #2502.565.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.69)\
        Mon 2014-04-21 18:09:18 +0400
        * [MDEV-750](https://jira.mariadb.org/browse/MDEV-750) [Bug #800035](https://bugs.launchpad.net/bugs/800035) - intermittent rpl\_deadlock\_innodb failures
  * [Revision #2502.567.229](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.229)\
    Mon 2014-06-02 15:36:06 +0300
    * [MDEV-6251](https://jira.mariadb.org/browse/MDEV-6251): SIGSEGV in query optimizer (in set\_check\_materialized with MERGE view)
* [Revision #4203](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4203)\
  Sun 2014-06-01 11:23:20 +0200
  * don't install ndb related .ini files, remove mysql\_fix\_privilege\_tables.1 and mysqlman.1
* [Revision #4202](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4202)\
  Sat 2014-05-31 13:18:56 +0200
  * [MDEV-5645](https://jira.mariadb.org/browse/MDEV-5645) MariaDB-5.5.35 - references are made to an "EXCEPTIONS-CLIENT" file but it does not exist
* [Revision #4201](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4201)\
  Sat 2014-05-31 10:16:25 +0200
  * disable unstable tokudb tests
* [Revision #4200](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4200)\
  Fri 2014-05-30 23:19:26 +0200
  * [MDEV-5485](https://jira.mariadb.org/browse/MDEV-5485) Minor man pages formatting issues [MDEV-6281](https://jira.mariadb.org/browse/MDEV-6281) Typo in mysql\_install\_db scripts and collateral changes:
* [Revision #4199](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4199)\
  Thu 2014-05-29 02:25:37 +0400
  * [MDEV-6239](https://jira.mariadb.org/browse/MDEV-6239): Partition pruning is not working as expected in an inner query - Make partition pruning work for tables inside semi-join nests (the new condition is the same that range optimizer uses so it should be ok)
* [Revision #4198](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4198)\
  Tue 2014-05-27 21:05:44 +0200
  * [MDEV-6271](https://jira.mariadb.org/browse/MDEV-6271) update MSI installer to include latest Version of HeidiSQL (8.3.x.x)
* [Revision #4197](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4197)\
  Tue 2014-05-27 20:57:28 +0200
  * [MDEV-6273](https://jira.mariadb.org/browse/MDEV-6273) Export my\_progname symbol in libmysqlclient.so
* [Revision #4196](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4196)\
  Wed 2014-05-28 17:32:43 +0400
  * [MDEV-6263](https://jira.mariadb.org/browse/MDEV-6263): Wrong result when using IN subquery with order by - When the optimizer chose LooseScan, make\_join\_readinfo() should use the index that was chosen for LooseScan, and should not try to find a better (shortest) index.
* [Revision #4195](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4195)\
  Wed 2014-05-28 16:51:19 +0500
  * [MDEV-6216](https://jira.mariadb.org/browse/MDEV-6216) sys\_vars.completion\_type\_func fails in --embedded.
* [Revision #4194](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4194)\
  Tue 2014-05-06 12:13:03 +0400
  * [MDEV-6083](https://jira.mariadb.org/browse/MDEV-6083) - Assertion \`! (&(\&LOCK\_open)->m\_mutex)->count || ! pthread\_equal(pth read\_self(), (&(\&LOCK\_open)->m\_mutex)->thread)' fails in intern\_sys\_var\_ptr on server shutdown after uninstalling TokuDB plugin at runtime
* [Revision #4193](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4193)\
  Tue 2014-05-27 09:45:01 +0300
  * 2 typo fixed
* [Revision #4192](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4192)\
  Thu 2014-05-22 16:20:56 +0300
  * [MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257): [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) fails to start with 10.0 InnoDB log files
* [Revision #4191](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4191)\
  Wed 2014-05-21 13:14:43 +0300
  * [MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257): [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) fails to start with 10.0 InnoDB log files
* [Revision #4190](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4190)\
  Sat 2014-05-17 10:42:59 +0300
  * [MDEV-6245](https://jira.mariadb.org/browse/MDEV-6245) Certain compressed tables with myisampack are corrupted by "CHECK TABLE" - Fixed bug that we where using wrong checksum algorithm when using VARCHAR with fixed lenth rows - Ensure in myisampack that HA\_OPTION\_NULL\_FIELDS is set for tables with null fields.
* [Revision #4189](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4189)\
  Mon 2014-05-12 12:56:13 +0200
  * [MDEV-4925](https://jira.mariadb.org/browse/MDEV-4925) Wrong result - count(distinct), Using index for group-by (scanning)
* [Revision #4188](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4188)\
  Fri 2014-05-09 11:03:39 +0300
  * [MDEV-4791](https://jira.mariadb.org/browse/MDEV-4791): Assertion range\_end >= range\_start fails in log0online.c on select from I\_S.INNODB\_CHANGED\_PAGES
* [Revision #4187](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4187)\
  Thu 2014-05-08 22:56:36 +0300
  * [MDEV-6193](https://jira.mariadb.org/browse/MDEV-6193): Problems with multi-table updates that JOIN against read-only table
* [Revision #4186](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4186) \[merge]\
  Wed 2014-05-07 09:28:12 +0300
  * merge 5.5->5.3
  * [Revision #2502.567.228](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.228)\
    Thu 2014-05-01 17:19:17 +0300
    * [MDEV-5981](https://jira.mariadb.org/browse/MDEV-5981): name resolution issues with views and multi-update in ps-protocol
* [Revision #4185](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4185)\
  Tue 2014-05-06 23:44:02 +0300
  * Fixed bug where CHECK TABLE for a MYISAM table before 5.5.38 wrongly gave warning: "Table upgrade required..."
* [Revision #4184](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4184)\
  Tue 2014-05-06 14:52:40 +0200
  * update test file for windows
* [Revision #4183](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4183)\
  Tue 2014-05-06 14:40:32 +0200
  * after tokudb-7.1.6 merge
* [Revision #4182](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4182) \[merge]\
  Mon 2014-05-05 22:59:44 +0200
  * merge: `git://github.com/Tokutek/ft-index.git` `git://github.com/Tokutek/ft-engine.git` at the tag tokudb-7.1.6
* [Revision #4181](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4181)\
  Mon 2014-05-05 15:41:29 +0200
  * update test results
* [Revision #4180](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4180)\
  Mon 2014-05-05 14:24:25 +0200
  * [MDEV-6056](https://jira.mariadb.org/browse/MDEV-6056) \[PATCH] mysqldump writes usage to stdout even when not explicitly requested
* [Revision #4179](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4179)\
  Mon 2014-05-05 12:51:21 +0200
  * fix broken -DWITHOUT\_SERVER build: move sql-dependent unit test from mysys/ to sql/
* [Revision #4178](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4178)\
  Mon 2014-05-05 12:51:11 +0200
  * [MDEV-6131](https://jira.mariadb.org/browse/MDEV-6131) Unable to build Connector/ODBC 5.2.5 undefined reference to \`my\_charset\_latin1'
* [Revision #4177](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4177)\
  Thu 2014-05-01 15:43:51 +0200
  * [MDEV-6091](https://jira.mariadb.org/browse/MDEV-6091) mysqldump goes in a loop and segfaults if --dump-slave is specified and it cannot connect to the server
* [Revision #4176](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4176)\
  Mon 2014-04-28 12:11:35 +0200
  * fix XtraDB version to tell the truth
* [Revision #4175](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4175)\
  Mon 2014-04-28 11:11:16 +0200
  * rename handler::ha\_set\_lock\_type() -> handler::set\_lock\_type(), because it's not a handler convenience wrapper
* [Revision #4174](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4174)\
  Fri 2014-02-28 15:46:02 +0400
  * [MDEV-5081](https://jira.mariadb.org/browse/MDEV-5081) - Simple performance improvement for MariaDB
* [Revision #4173](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4173)\
  Sat 2014-05-03 19:12:17 +0300
  * Added new states to be able to better diagnose where server hangs. - Table locks now ends with state "After table lock" - Open table now ends with state "After opening tables" - All calls to close\_thread\_tables(), not only from mysql\_execute\_command(), has state "closing tables" - Added state "executing" for mysql admin commands, like CACHE INDEX, REPAIR TABLE etc. - Added state "Finding key cache" for CACHE INDEX - Added state "Filling schema table" when we generate temporary table for SHOW commands and information schema.
* [Revision #4172](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4172)\
  Tue 2014-04-29 14:38:01 +0400
  * An after-fix for [MDEV-6146](https://jira.mariadb.org/browse/MDEV-6146) Can't mix (latin1\_swedish\_ci,NUMERIC) and (utf8\_unicode\_ci,IMPLICIT) for MATCH The original patch broke "mtr --ps fulltext".
* [Revision #4171](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4171)\
  Mon 2014-04-28 17:01:58 +0400
  * [MDEV-5459](https://jira.mariadb.org/browse/MDEV-5459) Illegal mix of collations for datetime
* [Revision #4170](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4170)\
  Mon 2014-04-28 15:56:31 +0400
  * [MDEV-5702](https://jira.mariadb.org/browse/MDEV-5702) Incorrect results are returned with NULLIF()
* [Revision #4169](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4169)\
  Mon 2014-04-28 09:13:53 +0300
  * [MDEV-6139](https://jira.mariadb.org/browse/MDEV-6139): UPDATE w/ join against MRG\_MyISAM table with read-only sub-table failsUPDATE w/ join against MRG\_MyISAM table with read-only sub-table fails
* [Revision #4168](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4168)\
  Mon 2014-04-28 08:30:05 +0300
  * [MDEV-6160](https://jira.mariadb.org/browse/MDEV-6160): InnoDB: Failing assertion: page\_is\_comp(next\_page) == page\_is\_comp(page)
* [Revision #4167](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4167)\
  Mon 2014-04-28 03:37:53 +0400
  * Modified the condition for skipping innodb.innodb-autoinc to exclude the part which was defined by MariaDB version and thus caused a wrong check result
* [Revision #4166](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4166)\
  Mon 2014-04-28 02:56:53 +0400
  * [MDEV-6178](https://jira.mariadb.org/browse/MDEV-6178) mysql\_upgrade breaks databases with long user names
* [Revision #4165](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4165)\
  Sat 2014-04-26 23:16:51 +0400
  * [MDEV-6169](https://jira.mariadb.org/browse/MDEV-6169) main.myisam-metadata fails mtr internal check
* [Revision #4164](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4164)\
  Sat 2014-04-26 21:32:08 +0400
  * [MDEV-6168](https://jira.mariadb.org/browse/MDEV-6168) rpl.rpl\_heartbeat\_basic fails mtr internal check
* [Revision #4163](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4163)\
  Sat 2014-04-26 21:29:15 +0400
  * Increment the version number
* [Revision #4162](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4162)\
  Thu 2014-04-24 18:20:57 +0300
  * [MDEV-6129](https://jira.mariadb.org/browse/MDEV-6129): Server crashes during UNION with ORDER BY field IS NULL
* [Revision #4161](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4161) \[merge]\
  Wed 2014-04-23 17:43:20 +0400
  * Merge 5.3->5.5
  * [Revision #2502.567.227](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.227)\
    Wed 2014-04-23 15:53:47 +0400
    * [MDEV-5338](https://jira.mariadb.org/browse/MDEV-5338) XML parser accepts malformed data
* [Revision #4160](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4160)\
  Wed 2014-04-23 10:28:06 +0400
  * [MDEV-6146](https://jira.mariadb.org/browse/MDEV-6146) Can't mix (latin1\_swedish\_ci,NUMERIC) and (utf8\_unicode\_ci,IMPLICIT) for MATCH
* [Revision #4159](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4159) \[merge]\
  Mon 2014-04-21 14:22:18 +0400
  * Merge from 5.3
  * [Revision #2502.567.226](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.226)\
    Mon 2014-04-21 13:19:32 +0400
    * [MDEV-6045](https://jira.mariadb.org/browse/MDEV-6045) MySQL Bug#11829861 - SUBSTRING\_INDEX() RESULTS "OMIT" CHARACTER WHEN USED INSIDE LOWER()
* [Revision #4158](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4158) \[merge]\
  Mon 2014-04-21 12:19:47 +0400
  * Merge from 5.3.
  * [Revision #2502.567.225](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.225)\
    Mon 2014-04-21 11:29:50 +0400
    * An after-fix for [MDEV-6134](https://jira.mariadb.org/browse/MDEV-6134) SUBSTRING\_INDEX returns wrong result for 8bit character sets when delimiter is not found
  * [Revision #2502.567.224](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.224)\
    Mon 2014-04-21 10:13:38 +0400
    * [MDEV-6134](https://jira.mariadb.org/browse/MDEV-6134) SUBSTRING\_INDEX returns wrong result for 8bit character sets when delimiter is not found
* [Revision #4157](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4157) \[merge]\
  Fri 2014-04-18 13:41:15 +0400
  * Merge from 5.3
  * [Revision #2502.567.223](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.223)\
    Fri 2014-04-18 12:19:51 +0400
    * [MDEV-5041](https://jira.mariadb.org/browse/MDEV-5041) Inserting a TIME with hour>24 into a DATETIME column produces a wrong value
* [Revision #4156](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4156) \[merge]\
  Fri 2014-04-18 12:16:56 +0400
  * Merge from 5.3
  * [Revision #2502.567.222](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.222)\
    Wed 2014-04-16 22:34:52 -0700
    * Fixed bugs [MDEV-5927](https://jira.mariadb.org/browse/MDEV-5927) and [MDEV-6116](https://jira.mariadb.org/browse/MDEV-6116). Both bugs are caused by the same problem: the function optimize\_cond() should update the value of \*cond\_equal rather than the value of join->cond\_equal, because it is called not only for the WHERE condition, but for the HAVING condition as well.
* [Revision #4155](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4155)\
  Thu 2014-04-17 02:12:08 +0500
  * [MDEV-6124](https://jira.mariadb.org/browse/MDEV-6124) Audit plugin fails with the Percona-Server 5.6. Some lines of code in file\_logger.c were lost while moving to the general MariaDB tree. Adding them.
* [Revision #4154](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4154)\
  Tue 2014-04-15 20:41:08 +0500
  * [MDEV-4856](https://jira.mariadb.org/browse/MDEV-4856) SQL\_ERROR\_LOG shows 1146 errors which didnt appear in mysql client. The fill\_schema\_table() function used to call get\_table\_share() for a table name in WHERE then clear the error list. That way plugins receive the superfluous error notification if it happens in it. Also the problem was that error handler didn't prevent the suppressed error message from logging anyway as the logging happens in THD::raise\_condition before the handler call. Trigger\_error\_handler is remade into Warnings\_only\_error\_handler, so it stores the error message in all cases in the thd->stmt\_da. Then later the stored error is raised.
* [Revision #4153](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4153)\
  Tue 2014-04-15 18:17:47 +0500
  * [MDEV-5138](https://jira.mariadb.org/browse/MDEV-5138) Numerous test failures in "mtr --ps --embedded". If a prepared statement calls an stored procedure, the thd->server\_status out of the SP goes up to the PS and then to the client. So that the client gets the SERVER\_STATUS\_CURSOR\_EXISTS status if the SP uses a cursor. Which makes the embedded server fail. Fixed by saving/restoring the upper-level server\_status in sp\_head::execute().
* [Revision #4152](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4152)\
  Tue 2014-04-15 18:16:47 +0500
  * [MDEV-5138](https://jira.mariadb.org/browse/MDEV-5138) Numerous test failures in "mtr --ps --embedded". Thread can be disconnected internally for example after COMMIT statements. So we should check this for the statement execution.
* [Revision #4151](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4151)\
  Tue 2014-04-15 18:12:25 +0500
  * [MDEV-5138](https://jira.mariadb.org/browse/MDEV-5138) Numerous test failures in "mtr --ps --embedded". mysqltest in the 'embedded-server' mode runs queries in a separate thread, but it didn't do so for the prepared statements - they were run in the main thread. That leads to inconsistencies. When a test sets SESSION 'dbug' variable like SET SESSION debug\_dbug="+d,warn\_during\_ha\_commit\_trans"; it is run as a plain query in that separate thread, so the main thread remains unaffected. After that the prepared statement run in the main thread doesn't produce expected 'dbug' errors, so the test fails. To fix that I made prepared statement to be run in that special thread along with the plain queries. That makes the environment consistent.
* [Revision #4150](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4150)\
  Tue 2014-04-15 18:09:58 +0500
  * [MDEV-5138](https://jira.mariadb.org/browse/MDEV-5138) Numerous test failures in "mtr --ps --embedded". As Davi added code like sav\_protocol= thd->protocol thd->protocol= \&thd->protocol\_binary ... thd->protocol= sav\_protocol the fucntions like emb\_store\_querycache\_result() cannot determine the used protocol testing thd->protocol == \&thd->protocol\_binary. Fixed by additional check thd->command == COM\_STMT\_EXECUTE.
* [Revision #4149](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4149)\
  Tue 2014-04-15 18:08:33 +0500
  * [MDEV-5138](https://jira.mariadb.org/browse/MDEV-5138) Numerous test failures in "mtr --ps --embedded". The function Protocol::net\_store\_data(a, b, CHARSET\_A, CHARSET\_B) should be adapted to be working in the embedded server as it's done with the Protocol::net\_store\_data(a, b). That new function renamed as net\_store\_data\_cs, so we can make it virtual.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
