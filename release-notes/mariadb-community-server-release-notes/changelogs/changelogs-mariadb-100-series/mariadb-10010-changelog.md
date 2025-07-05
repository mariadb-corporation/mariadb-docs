# MariaDB 10.0.10 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.10) |[Release Notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md) |**Changelog** |[Overview of 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md)

**Release date:** 31 Mar 2014

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4140](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4140) \[merge]\
  Sat 2014-03-29 17:32:46 +0100
  * 10.0-connect merge
  * [Revision #3984.1.17](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.17)\
    Sat 2014-03-29 17:31:08 +0100
    * never put anything with side-effects in an assert() - asserts can be conditionally compiled out.
  * [Revision #3984.1.16](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.16)\
    Thu 2014-03-27 19:07:17 +0100
    * Make local MySQL connection default to unix socket on Linux or enable to use named pipe on Windows by specifying the host as '.' This addresses [MDEV-5952](https://jira.mariadb.org/browse/MDEV-5952).
    * modified:
      * storage/connect/myconn.cpp
  * [Revision #3984.1.15](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.15)\
    Thu 2014-03-27 13:25:02 +0100
    * disable connect tests for `--embedded`
  * [Revision #3984.1.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.14)\
    Sun 2014-03-23 15:50:39 +0100
    * Should fix valgrind diag on uninitialized value
    * modified:
      * storage/connect/tabdos.cpp
  * [Revision #3984.1.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.13)\
    Fri 2014-03-21 23:58:11 +0100
    * Fix bug [MDEV-5928](https://jira.mariadb.org/browse/MDEV-5928)
    * modified:
      * storage/connect/tabxml.cpp
  * [Revision #3984.1.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.12)\
    Fri 2014-03-21 22:47:40 +0100
    * Remove 2 compile warnings
    * modified:
      * storage/connect/ha\_connect.cc
  * [Revision #3984.1.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.11)\
    Fri 2014-03-21 22:24:54 +0100
    * Fix bug [MDEV-5919](https://jira.mariadb.org/browse/MDEV-5919). Was because doing fseek of a stream closed by another thread.
    * modified:
      * storage/connect/filamtxt.cpp
  * [Revision #3984.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.10)\
    Fri 2014-03-21 02:40:27 +0100
    * FIX [MDEV-5918](https://jira.mariadb.org/browse/MDEV-5918)
    * modified:
      * storage/connect/ha\_connect.cc
  * [Revision #3984.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.9)\
    Wed 2014-03-19 15:45:21 +0100
    * FIX [MDEV-5890](https://jira.mariadb.org/browse/MDEV-5890) and [MDEV-5900](https://jira.mariadb.org/browse/MDEV-5900)
    * modified:
      * storage/connect/filamtxt.cpp
      * storage/connect/ha\_connect.cc
  * [Revision #3984.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.8)\
    Wed 2014-03-19 02:25:28 +0100
    * Suppress call to PROFILE\_End in connect\_done\_func that causes Signal 11 on Linux
    * modified:
      * storage/connect/ha\_connect.cc
  * [Revision #3984.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.7)\
    Tue 2014-03-18 19:25:50 +0100
    * FIX PIVOT bug [MDEV-5869](https://jira.mariadb.org/browse/MDEV-5869) caused by using fop (field option ptr) when NULL.
    * modified:
      * storage/connect/ha\_connect.cc
  * [Revision #3984.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.6)\
    Mon 2014-03-10 18:29:04 +0100
    * NOTE: an experimental implementation of MRR was done but not kept in this version. Sure enough, it never caused any improvement in the execution speed and rather caused a small increase of execution time. This is probably because values are sorted by rowid in each range of CONNECT indexes. This could be reconsidered if a customer have a need for processing very big files.
  * [Revision #3984.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.5)\
    Wed 2014-03-05 12:10:02 +0100
    * Fix [MDEV-5497](https://jira.mariadb.org/browse/MDEV-5497). The city column length was wrong in the create table statements.
    * modified:
      * storage/connect/mysql-test/connect/r/fix.result
      * storage/connect/mysql-test/connect/t/fix.test
  * [Revision #3984.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.4)\
    Thu 2014-02-27 18:00:01 +0100
    * Fix bug [MDEV-5734](https://jira.mariadb.org/browse/MDEV-5734)
    * modified:
      * storage/connect/mysql-test/connect/r/pivot.result
      * storage/connect/mysql-test/connect/t/pivot.test
      * storage/connect/tabmysql.cpp
      * storage/connect/tabpivot.cpp
  * [Revision #3984.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.3)\
    Sun 2014-02-16 22:52:57 +0100
    * Make alter.test to work on both Windows and Linux
    * modified:
      * storage/connect/mysql-test/connect/r/alter.result
      * storage/connect/mysql-test/connect/t/alter.test
  * [Revision #3984.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.2)\
    Sun 2014-02-16 18:05:43 +0100
    * This is a minor change commitment
  * [Revision #3984.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3984.1.1)\
    Fri 2014-02-07 22:44:43 +0100
    * Check field option changes on ALTER TABLE in check\_if\_supported\_inplace\_alter. If yes, the in-place algorithm cannot be used (inward tables)
    * modified:
      * storage/connect/ha\_connect.cc
      * storage/connect/ha\_connect.h
* [Revision #4139](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4139)\
  Sat 2014-03-29 14:16:58 +0100
  * temporarily disable part of the test in ps-protocol. name resolution issues. see [MDEV-5981](https://jira.mariadb.org/browse/MDEV-5981)
* [Revision #4138](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4138)\
  Sat 2014-03-29 11:33:25 +0100
  * another post-fix patch for [MDEV-5850](https://jira.mariadb.org/browse/MDEV-5850): MySQL Bug#21317: SHOW CREATE DATABASE does not obey to lower\_case\_table\_names (for case-insensitive filesystems)
* [Revision #4137](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4137)\
  Sat 2014-03-29 11:33:20 +0100
  * [MDEV-5969](https://jira.mariadb.org/browse/MDEV-5969) Crash in prepared statement with NO\_ZERO\_IN\_DATE and ROLLUP [MDEV-5971](https://jira.mariadb.org/browse/MDEV-5971) Asymmetry between CAST(DATE'2001-00-00') to INT and TO CHAR in prepared statements
* [Revision #4136](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4136)\
  Sat 2014-03-29 11:32:49 +0100
  * update the result file
* [Revision #4135](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4135)\
  Fri 2014-03-28 21:46:58 +0100
  * [MDEV-5979](https://jira.mariadb.org/browse/MDEV-5979) Server crashes on truncating a temporary InnoDB table on Windows
* [Revision #4134](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4134) \[merge]\
  Fri 2014-03-28 21:42:57 +0200
  * automatic merge
  * [Revision #4130.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4130.1.2)\
    Fri 2014-03-28 09:31:43 +0200
    * Updated sponsors and authors
  * [Revision #4130.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4130.1.1)\
    Fri 2014-03-28 09:31:24 +0200
    * Fixed that the we don't change CREATE to CREATE OR REPLACE, except if the slave removed an existing table as part of CREATE. This will help the following replicaition scenario: [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) master (statement replication) -> [MariaDB 10.0](../../old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0.md) slave (row based replication) -> MySQL or MariaDB 5.x slave
* [Revision #4133](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4133)\
  Fri 2014-03-28 11:30:10 +0400
  * [MDEV-5964](https://jira.mariadb.org/browse/MDEV-5964) - main.[MDEV-504](https://jira.mariadb.org/browse/MDEV-504) unveils assertion failure in TABLE\_SHARE::visit\_subgraph
* [Revision #4132](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4132)\
  Fri 2014-03-28 23:18:33 +0400
  * Change the order of parameters in DECODE\_HISTOGRAM to match the order of fields in mysql.column\_stats.
* [Revision #4131](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4131) \[merge]\
  Fri 2014-03-28 22:19:16 +0400
  * Merge
  * [Revision #4129.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4129.1.1)\
    Fri 2014-03-28 22:17:57 +0400
    * [MDEV-5978](https://jira.mariadb.org/browse/MDEV-5978): valgrind failure in rpl\_row\_corruption - Fix valgrind failure: don't touch table\_list->master\_had\_triggers when RBR\_TRIGGERS is not compiled in.
* [Revision #4130](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4130)\
  Thu 2014-03-27 23:23:28 +0100
  * post-fix patch for [MDEV-5850](https://jira.mariadb.org/browse/MDEV-5850): MySQL Bug#21317: SHOW CREATE DATABASE does not obey to lower\_case\_table\_names
* [Revision #4129](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4129) \[merge]\
  Fri 2014-03-28 00:38:56 +0400
  * Merge
  * [Revision #4126.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4126.1.1)\
    Fri 2014-03-28 00:32:53 +0400
    * [MDEV-4360](https://jira.mariadb.org/browse/MDEV-4360): ANALYZE shows "Table is already up to date" while updating stats - Show a line with "Engine-independent statistics collected" when ANALYZE command caused EITS statistics to be recollected.
* [Revision #4128](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4128)\
  Thu 2014-03-27 12:17:53 +0100
  * compilation failure on windows
* [Revision #4127](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4127)\
  Thu 2014-03-27 12:04:34 +0100
  * mtr: remove `--use-copy`, autodetect symlink support instead
* [Revision #4126](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4126) \[merge]\
  Thu 2014-03-27 14:57:53 +0400
  * Merge
  * [Revision #4116.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4116.1.1)\
    Thu 2014-03-27 14:55:29 +0400
    * [MDEV-5962](https://jira.mariadb.org/browse/MDEV-5962): EITS: value "position" calculated incorrectly for CHAR(n) columns - Dont substract unsigned numbers, use correct calculations. - (there is no testcase because effort is required to come up with it)
* [Revision #4125](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4125)\
  Thu 2014-03-27 11:25:27 +0100
  * update .result file
* [Revision #4124](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4124)\
  Mon 2014-03-24 08:18:01 +0200
  * [MDEV-5876](https://jira.mariadb.org/browse/MDEV-5876): MySQL bug #11766767 - "59957: VIEW USING MERGE PERMISSIONS IN MULTI-TABLE UPDATE"
* [Revision #4123](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4123)\
  Sun 2014-03-23 21:09:38 +0200
  * Make copy\_up\_file\_and\_fill() safe for disk full Fixed use-copy option to mysql-test-run
* [Revision #4122](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4122)\
  Sun 2014-03-23 18:39:10 +0200
  * [MDEV-5930](https://jira.mariadb.org/browse/MDEV-5930) Server crashes in thd\_get\_ha\_data on CREATE OR REPLACE TABLE
* [Revision #4121](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4121)\
  Sun 2014-03-23 17:00:29 +0200
  * [MDEV-5818](https://jira.mariadb.org/browse/MDEV-5818): [MySQL Worklog #6145](https://dev.mysql.com/worklog/task/?id=6145): Separate the dependence of DATA DIRECTORY from symbolic links
* [Revision #4120](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4120)\
  Sun 2014-03-23 15:55:05 +0200
  * [MDEV-5930](https://jira.mariadb.org/browse/MDEV-5930): Server crashes in thd\_get\_ha\_data on CREATE OR REPLACE TABLE
* [Revision #4119](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4119)\
  Sun 2014-03-23 15:43:57 +0200
  * [MDEV-5850](https://jira.mariadb.org/browse/MDEV-5850): MySQL Bug#21317: SHOW CREATE DATABASE does not obey to lower\_case\_table\_names Bug #3329 Incomplete lower\_case\_table\_names=2 implementation
* [Revision #4118](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4118)\
  Sat 2014-03-22 12:32:36 +0200
  * [MDEV-734](https://jira.mariadb.org/browse/MDEV-734): [Bug #917662](https://bugs.launchpad.net/bugs/917662) - mysql\_print\_status() missing final fflush()
* [Revision #4117](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4117)\
  Sat 2014-03-22 12:08:35 +0200
  * [MDEV-5906](https://jira.mariadb.org/browse/MDEV-5906): Thread status not changed when applying log events
* [Revision #4116](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4116)\
  Thu 2014-03-27 13:08:00 +0400
  * Code cleanup: - Move \[some] engine-agnostic tests from t/selectivity.test to t/selectivity\_no\_engine.test - Move Histogram::point\_selectivity to sql\_statistics.cc
* [Revision #4115](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4115) \[merge]\
  Thu 2014-03-27 12:37:05 +0400
  * Merge
  * [Revision #4074.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4074.1.3)\
    Thu 2014-03-27 12:30:49 +0400
    * [MDEV-5926](https://jira.mariadb.org/browse/MDEV-5926), [MDEV-4362](https://jira.mariadb.org/browse/MDEV-4362) post-fixes: - Histogram::find\_bucket() should not walk off the end of the value range. - Address review feedback in Histogram::point\_selectivity(): different handling for zero-width buckets, and explanations.
  * [Revision #4074.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4074.1.2)\
    Wed 2014-03-26 21:05:31 +0400
    * [MDEV-4362](https://jira.mariadb.org/browse/MDEV-4362): {division by zero when lookup constant is outside the value table} - Fix Histogram::point\_selectivity() to work in the case where the passed value\_pos=0 (or 1) and the first (or the last) bucket in the histogram has zero value-range (i.e one value).
  * [Revision #4074.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4074.1.1)\
    Wed 2014-03-26 17:55:00 +0400
    * [MDEV-5926](https://jira.mariadb.org/browse/MDEV-5926): EITS: Histogram estimates for column=least\_possible\_value are wrong \[Attempt #2] - Use a new selectivity calculation formula in Histogram::point\_selectivity. The formula is different from the old one because it was developed from scratch. it doesn't have any possible division-by-zero problems.
* [Revision #4114](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4114)\
  Thu 2014-03-27 08:11:05 +0100
  * heap.test: hide a warning on 32-bit
* [Revision #4113](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4113)\
  Wed 2014-03-26 22:32:20 +0100
  * [MDEV-5433](https://jira.mariadb.org/browse/MDEV-5433) select\_result::send\_error() is unused
* [Revision #4112](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4112)\
  Wed 2014-03-26 22:32:15 +0100
  * [MDEV-5943](https://jira.mariadb.org/browse/MDEV-5943) 'show table status' does not immediately show tokudb tables [MDEV-5839](https://jira.mariadb.org/browse/MDEV-5839) TokuDB tables not properly cleaned on DROP DATABASE
* [Revision #4111](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4111)\
  Wed 2014-03-26 22:32:10 +0100
  * Fix hostcache\_ipv4\_blocked and hostcache\_ipv6\_blocked to pass. Don't abort plugin reads whem mpvio->make\_it\_fail is set - this can leak information.
* [Revision #4110](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4110)\
  Wed 2014-03-26 22:31:17 +0100
  * update tokudb tests for 10.0
* [Revision #4109](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4109)\
  Wed 2014-03-26 22:26:13 +0100
  * Revert revision sergii@pisem.net-20130123151853-xc6i3l11aqv0iykk Rename back my\_init\_dynamic\_array2() -> init\_dynamic\_array2() It happens to be a part of the de facto API :(
* [Revision #4108](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4108) \[merge]\
  Wed 2014-03-26 22:25:38 +0100
  * 5.5 merge
  * [Revision #3413.21.585](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.585)\
    Wed 2014-03-26 19:56:23 +0100
    * [MDEV-5955](https://jira.mariadb.org/browse/MDEV-5955) Server crashes in handler::ha\_external\_lock or assertion \`m\_lock\_type == 2' fails in handler::ha\_close on disconnect with a locked temporary table
  * [Revision #3413.21.584](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.584)\
    Wed 2014-03-26 21:58:27 +0200
    * [MDEV-5905](https://jira.mariadb.org/browse/MDEV-5905): Creating tmp. memory table kills the server
  * [Revision #3413.21.583](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.583)\
    Wed 2014-03-26 08:24:19 +0100
    * compilation failure with BUILD/compile-amd64-valgrind-max
  * [Revision #3413.21.582](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.582)\
    Tue 2014-03-25 22:41:18 +0100
    * move file->position() down, to make sure it's executed only when previous file->index\_next (or other file->... index access method) succeeded
  * [Revision #3413.21.581](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.581)\
    Tue 2014-03-25 17:34:45 +0100
    * don't put libmysqlclient symbols extra-used on debian in the libmysqlclient\_16 version node.
  * [Revision #3413.21.580](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.580) \[merge]\
    Tue 2014-03-25 11:09:12 +0100
    * 5.3 merge
    * [Revision #2502.567.220](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.220)\
      Sun 2014-03-23 16:02:56 +0400
      * [MDEV-5783](https://jira.mariadb.org/browse/MDEV-5783) Assertion \`0' failed in make\_sortkey(SORTPARAM\*, uchar\*, uchar\*) on ORDER BY HEX( UNCOMPRESSED\_LENGTH( pk ) )
    * [Revision #2502.567.219](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.219)\
      Fri 2014-03-21 12:23:09 +0200
      * Fix to make it compiling with valgrind.
    * [Revision #2502.567.218](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.218) \[merge]\
      Tue 2014-03-18 12:06:32 +0400
      * Merge
      * [Revision #2502.592.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.592.1)\
        Thu 2014-03-13 12:20:57 +0100
        * [MDEV-5811](https://jira.mariadb.org/browse/MDEV-5811): Server crashes in best\_access\_path with materialization+semijoin and big\_tables=ON - With big\_tables=ON, materialized table will use Aria (or MyISAM) SE, which allows prefix key reads. However, the temp.table has rec\_per\_key=NULL which causes the optimizer to crash when attempting to read index statistics for a prefix index read. - Fixed by providing a rec\_per\_key array with zeros (i.e. "no statistics data")
  * [Revision #3413.21.579](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.579)\
    Mon 2014-03-24 20:02:08 +0100
    * [MDEV-5913](https://jira.mariadb.org/browse/MDEV-5913) Windows: 10.0 crashes on shutdown
  * [Revision #3413.21.578](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.578)\
    Mon 2014-03-24 20:02:00 +0100
    * mysqltest bug: reset `--replace` command after every error message (because error messages use replacements)
  * [Revision #3413.21.577](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.577)\
    Mon 2014-03-24 20:01:55 +0100
    * [MDEV-5822](https://jira.mariadb.org/browse/MDEV-5822) TokuDB fails to compile without partition storage engine
  * [Revision #3413.21.576](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.576)\
    Mon 2014-03-24 20:01:50 +0100
    * tokudb: make compression=TOKUDB\_ZLIB the default (instead of TOKUDB\_UNCOMPRESSED) for new tables
  * [Revision #3413.21.575](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.575)\
    Mon 2014-03-24 20:01:45 +0100
    * rpl tests: move "include/master-slave.inc" down to be after all possible checks that can skip the test
  * [Revision #3413.21.574](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.574)\
    Mon 2014-03-24 20:01:37 +0100
    * [MDEV-5831](https://jira.mariadb.org/browse/MDEV-5831) Upgrade from [MariaDB 5.5.36](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5536-release-notes.md) via yum fails
  * [Revision #3413.21.573](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.573)\
    Wed 2014-03-19 10:03:34 +0100
    * [MDEV-5773](https://jira.mariadb.org/browse/MDEV-5773) symbol list\_add, version libmysqlclient\_18 not defined in file libmysqlclient.so.18 with link time reference [MDEV-5763](https://jira.mariadb.org/browse/MDEV-5763) libmyodbc.so: undefined symbol: int2str [MDEV-5739](https://jira.mariadb.org/browse/MDEV-5739) Symbol missing in libmysqlclient.so.18 (make\_scrambled\_password)
  * [Revision #3413.21.572](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.572)\
    Wed 2014-03-19 10:02:41 +0100
    * [MDEV-5892](https://jira.mariadb.org/browse/MDEV-5892) Centos startup script is broken
  * [Revision #3413.21.571](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.571)\
    Sun 2014-03-23 18:44:48 +0400
    * [MDEV-5862](https://jira.mariadb.org/browse/MDEV-5862) server\_audit test fails in buildbot on Mac (labrador). The RTLD\_DEFAULT value on Labrador machine is not NULL, so the dlsym() commands in the server\_audit just fail to bind the necessary functions. Fixed by using RTLD\_DEFAULT explicitly.
  * [Revision #3413.21.570](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.570) \[merge]\
    Tue 2014-03-18 18:29:07 +0100
    * merge
    * [Revision #3413.64.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.64.5) \[merge]\
      Tue 2014-03-18 09:02:57 +0100
      * merge ft-index and ft-engine as of 7.1.5
    * [Revision #3413.64.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.64.4) \[merge]\
      Mon 2014-03-17 17:41:54 +0100
      * percona-server-5.5.36-34.0
      * [Revision #0.48.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.48.2)\
        Mon 2014-03-17 17:40:07 +0100
        * percona-server-5.5.36-34.0.tar.gz
    * [Revision #3413.64.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.64.3) \[merge]\
      Mon 2014-03-17 13:04:28 +0100
      * null-merge from 5.3 (from 5.2, from 5.1, from mysql-5.1.73)
      * [Revision #2502.567.217](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.217) \[merge]\
        Sun 2014-03-16 21:03:01 +0100
        * 5.2 merge
        * [Revision #2502.566.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.67) \[merge]\
          Sun 2014-03-16 13:59:44 +0100
          * 5.1 merge
          * [Revision #2502.565.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.68) \[merge]\
            Sat 2014-03-15 18:24:15 +0100
            * mysql-5.1.73 merge
    * [Revision #3413.64.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.64.2) \[merge]\
      Sun 2014-03-16 19:21:37 +0100
      * 5.3-merge
      * [Revision #2502.567.216](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.216) \[merge]\
        Sun 2014-03-16 12:44:47 +0100
        * 5.2 merge
        * [Revision #2502.566.66](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.66)\
          Thu 2014-03-13 20:12:50 +0100
          * don't run unix\_socket tests when $USER is already present in mysql.user (as it's done in 10.0)
      * [Revision #2502.567.215](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.215)\
        Fri 2014-03-14 11:38:17 +0200
        * [MDEV-5446](https://jira.mariadb.org/browse/MDEV-5446): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' fails on EXPLAIN EXTENDED with VALUES function
      * [Revision #2502.567.214](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.214) \[merge]\
        Thu 2014-03-13 18:36:52 +0100
        * 5.2 merge
        * [Revision #2502.566.65](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.65)\
          Thu 2014-03-13 16:35:14 +0100
          * unix\_socket bypasses make\_if\_fail by not doing any network reads
        * [Revision #2502.566.64](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.64)\
          Thu 2014-03-13 16:34:34 +0100
          * mtr: move if(unix\_socket) test to include/have\_unix\_socket.inc
      * [Revision #2502.567.213](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.213) \[merge]\
        Wed 2014-03-12 18:47:19 +0200
        * merge 5.2->5.3
        * [Revision #2502.566.63](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.566.63) \[merge]\
          Wed 2014-03-12 18:43:44 +0200
          * merge 5.1->5.2
          * [Revision #2502.565.67](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.565.67)\
            Wed 2014-03-12 15:50:00 +0200
            * [MDEV-5717](https://jira.mariadb.org/browse/MDEV-5717): Server crash with insert statement containing DEFAULT into view
      * [Revision #2502.567.212](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.212)\
        Wed 2014-03-12 12:34:16 +0200
        * [MDEV-5717](https://jira.mariadb.org/browse/MDEV-5717): Server crash with insert statement containing DEFAULT into view
      * [Revision #2502.567.211](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.211)\
        Fri 2014-03-07 13:57:07 +0200
        * [MDEV-5740](https://jira.mariadb.org/browse/MDEV-5740): Assertion \`!derived->first\_select()->exclude\_from\_table\_unique\_test || derived->outer\_select()-> exclude\_from\_table\_unique\_test' failed on 2nd execution of PS with derived\_merge
      * [Revision #2502.567.210](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/2502.567.210)\
        Thu 2014-03-06 13:56:34 -0800
        * Fixed bug [MDEV-5686](https://jira.mariadb.org/browse/MDEV-5686). The calls of the function remove\_eq\_conds() may change the and/or structure of the where conditions. So JOIN::equal\_cond should be updated for non-recursive calls of remove\_eq\_conds().
    * [Revision #3413.64.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.64.1)\
      Wed 2014-02-26 16:15:52 +0100
      * Fix code in make\_sortkey() that only worked by chance (assert added by MySQL verified that strnxfrm can only _increase_ the string length if from == to, and the latter is a random decision made by individual items and String::realloc).
  * [Revision #3413.21.569](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.569)\
    Tue 2014-03-18 16:26:02 +0200
    * Fixed buildbot issues
  * [Revision #3413.21.568](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.568)\
    Tue 2014-03-18 10:26:50 +0200
    * Fixed some buildbot failures
  * [Revision #3413.21.567](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.567)\
    Mon 2014-03-17 19:09:53 +0400
    * [MDEV-5681](https://jira.mariadb.org/browse/MDEV-5681) audit log will not rotate when the file size exceeds global variable setting. Notifications about changed variables: server\_audit\_file\_rotate\_now server\_audit\_file\_rotations server\_audit\_file\_rotations are now handled and one doesn't need to stop/start logging to make them effective.
  * [Revision #3413.21.566](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.566)\
    Fri 2014-03-14 16:29:23 +0200
    * [MDEV-5829](https://jira.mariadb.org/browse/MDEV-5829): STOP SLAVE resets global status variables
  * [Revision #3413.21.565](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.565)\
    Thu 2014-02-13 11:40:49 +0400
    * [MDEV-5089](https://jira.mariadb.org/browse/MDEV-5089) - possible deadlocks between rwlocks and mutexes
  * [Revision #3413.21.564](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.564)\
    Tue 2014-03-11 19:07:02 +0100
    * Debugging aid: Add T\* List::elem(int n) which returns N-th element in the list. - There was List::nth\_element() but it didn't work because linker removed it. - Now, removal by linker is prevented for important values of T, and function is renamed.
  * [Revision #3413.21.563](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.563) \[merge]\
    Tue 2014-03-11 17:14:48 +0100
    * Merge
    * [Revision #3413.63.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.63.1)\
      Tue 2014-03-11 16:45:08 +0100
      * [MDEV-5177](https://jira.mariadb.org/browse/MDEV-5177): ha\_partition and innodb index intersection produce fewer rows (MySQL Bug#70703) (This is attempt at fix #2) (re-commit with fixed typo) - Moved the testcase from partition\_test to partition\_innodb.test where it can really work. - Made ordered index scans over ha\_partition tables to satisfy ROR property for the case where underlying table uses extended keys.
  * [Revision #3413.21.562](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.562)\
    Tue 2014-03-11 17:37:46 +0200
    * Fixed test failure (5.5 had different test result than 10.0)
* [Revision #4107](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4107)\
  Wed 2014-03-26 09:43:02 +0100
  * [MDEV-5920](https://jira.mariadb.org/browse/MDEV-5920) MySQL Bug#16765410 FTS: STACK AROUND THE VARIABLE 'MYSTR' WAS CORRUPTED IN INNOBASE\_STRNXFRM
* [Revision #4106](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4106)\
  Wed 2014-03-26 09:42:52 +0100
  * [MDEV-5861](https://jira.mariadb.org/browse/MDEV-5861) MySQL Bug#12601974 - STORED PROCEDURE SQL\_MODE=NO\_BACKSLASH\_ESCAPES IGNORED AND BREAKS REPLICATION
* [Revision #4105](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4105)\
  Wed 2014-03-26 09:42:33 +0100
  * make append\_query\_string() more usable: simplify the prototype and move it to sql\_string.h
* [Revision #4104](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4104)\
  Wed 2014-03-26 09:41:52 +0100
  * remove append\_escaped(), use String::append\_for\_single\_quote() instead
* [Revision #4103](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4103)\
  Wed 2014-03-26 09:41:37 +0100
  * small cleanup in sql\_acl.cc: use LEX\_STRING, keep similar functions together, remove duplicated code
* [Revision #4102](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4102)\
  Wed 2014-03-26 09:41:28 +0100
  * [MDEV-5909](https://jira.mariadb.org/browse/MDEV-5909) MySQL BUG#11748924 PARTITIONS: TOO-LONG COMMENT CAUSES NO WARNING
* [Revision #4101](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4101)\
  Wed 2014-03-26 09:41:16 +0100
  * build\_frm\_image(): don't try to guess the "real table name" from the field list, it doesn't work if ALTER TABLE has replaced all fields. Instead, pass the correct original table name down from the caller.
* [Revision #4100](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4100)\
  Wed 2014-03-26 09:33:54 +0100
  * TokuDB: make the default value for the table compression= attribute to come from the variable @@session.tokudb\_row\_format
* [Revision #4099](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4099)\
  Wed 2014-03-26 09:33:03 +0100
  * bug in HA\_TOPTION\_SYSVAR of the enum type - enum string was generated incorrectly
* [Revision #4098](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4098)\
  Wed 2014-03-26 09:32:54 +0100
  * [MDEV-5815](https://jira.mariadb.org/browse/MDEV-5815) MySQL BUG#11751736: DROP DATABASE STATEMENT SHOULD REMOVE .OLD SUFFIX FROM DATABASE DIRECTORY
* [Revision #4097](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4097)\
  Fri 2014-03-21 14:36:49 +0100
  * [MDEV-5817](https://jira.mariadb.org/browse/MDEV-5817) MySQL BUG#11825482: Broken key length calculation for btree index
* [Revision #4096](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4096)\
  Fri 2014-03-21 14:05:44 +0100
  * [MDEV-5823](https://jira.mariadb.org/browse/MDEV-5823) MySQL bug#11760213-52599: ALTER TABLE REMOVE PARTITIONING ON NON-PARTITIONED TABLE CORRUPTS MYISAM
* [Revision #4095](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4095)\
  Thu 2014-03-20 23:27:08 +0100
  * [MDEV-5846](https://jira.mariadb.org/browse/MDEV-5846) MySQL Bug #18144 - Cost with FORCE/USE index seems incorrect in some cases.
* [Revision #4094](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4094)\
  Thu 2014-03-20 23:26:50 +0100
  * [MDEV-5820](https://jira.mariadb.org/browse/MDEV-5820) MySQL Bug #54805 definitions in regex/my\_regex.h conflict with /usr/include/regex.h
* [Revision #4093](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4093)\
  Thu 2014-03-20 23:26:41 +0100
  * [MDEV-5849](https://jira.mariadb.org/browse/MDEV-5849) MySQL bug#12602983 - User without privilege on routine can discover its existence by executing "select non\_existing\_func();" or by "call non\_existing\_proc()"
* [Revision #4092](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4092)\
  Thu 2014-03-20 09:50:45 +0100
  * [MDEV-5858](https://jira.mariadb.org/browse/MDEV-5858) MySQL Bug#12744991 - DECIMAL\_ROUND(X,D) GIVES WRONG RESULTS WHEN D == N\*(-9)
* [Revision #4091](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4091)\
  Thu 2014-03-20 00:44:35 +0100
  * [MDEV-5894](https://jira.mariadb.org/browse/MDEV-5894) MySQL BUG#34750: Print database name in Unknown Table error message
* [Revision #4090](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4090)\
  Wed 2014-03-19 20:33:12 +0100
  * [MDEV-5898](https://jira.mariadb.org/browse/MDEV-5898) FOUND\_ROWS() return incorrect value when using DISTINCT
* [Revision #4089](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4089)\
  Wed 2014-03-19 09:58:18 +0100
  * [MDEV-5404](https://jira.mariadb.org/browse/MDEV-5404) Can't free data returned by mariadb\_dyncol\_unpack on windows
* [Revision #4088](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4088)\
  Wed 2014-03-19 09:58:06 +0100
  * [MDEV-5173](https://jira.mariadb.org/browse/MDEV-5173) Cppcheck report
* [Revision #4087](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4087)\
  Wed 2014-03-19 09:57:57 +0100
  * [MDEV-5787](https://jira.mariadb.org/browse/MDEV-5787) Server crashes in row\_mysql\_convert\_row\_to\_innobase on CREATE .. SELECT
* [Revision #4086](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4086)\
  Wed 2014-03-19 09:57:45 +0100
  * [MDEV-5771](https://jira.mariadb.org/browse/MDEV-5771) Privileges acquired via roles depend on the order of granting
* [Revision #4085](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4085)\
  Wed 2014-03-19 09:57:17 +0100\
  \*
  1. move Debug\_role\_merges\_routine status variable increment to a correct function (similar to other Debug\_role\_merges\_\* variables). 2. make optional arguments of propagate\_role\_grants() really optional
* [Revision #4084](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4084)\
  Wed 2014-03-19 09:57:09 +0100
  * List<>-style template wrapper over hash\_filo
* [Revision #4083](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4083)\
  Wed 2014-03-19 09:56:46 +0100
  * update plugins' maturity levels: old plugins get STABLE newer plugins get GAMMA those that had bugs recently get BETA
* [Revision #4082](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4082)\
  Wed 2014-03-26 15:17:12 +0200
  * [MDEV-5949](https://jira.mariadb.org/browse/MDEV-5949): Performance of XtraDB slows down significantly on long benchmarks when compressed tables are used.
* [Revision #4081](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4081)\
  Mon 2014-03-24 11:22:16 +0100
  * [MDEV-5825](https://jira.mariadb.org/browse/MDEV-5825): Assertion \`! is\_set() || m\_can\_overwrite\_status' fails in Diagnostics\_area::set\_error\_status on executing rpl.rpl\_parallel test
* [Revision #4080](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4080)\
  Sun 2014-03-23 19:43:01 +0400
  * [MDEV-5781](https://jira.mariadb.org/browse/MDEV-5781) Item\_sum\_std::val\_real(): Assertion \`nr >= 0.0' fails on query with STDDEV\_POP, ROUND and variable
* [Revision #4079](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4079)\
  Sun 2014-03-23 15:15:07 +0400
  * A joint patch for: - [MDEV-5689](https://jira.mariadb.org/browse/MDEV-5689) ExtractValue(xml, 'substring(/x,/y)') crashes - [MDEV-5709](https://jira.mariadb.org/browse/MDEV-5709) ExtractValue() with XPath variable references returns wrong result.
* [Revision #4078](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4078)\
  Sun 2014-03-23 14:22:44 +0400
  * [MDEV-5870](https://jira.mariadb.org/browse/MDEV-5870) Assertion \`ltime->neg == 0' fails with COALESCE, ADDDATE, MAKEDATE A huge number in the "day" part of an interval made the code to return a negative date erroneously. Adding a test to return an error on a too large "day" value.
* [Revision #4077](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4077)\
  Sat 2014-03-22 12:44:39 -0700
  * Fixed bug [MDEV-5931](https://jira.mariadb.org/browse/MDEV-5931). After constant table row substitution the where condition may be converted to always true. The function calculate\_cond\_selectivity\_for\_table() should take into account this possibility.
* [Revision #4076](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4076)\
  Fri 2014-03-21 13:30:55 +0100
  * [MDEV-5914](https://jira.mariadb.org/browse/MDEV-5914): Parallel replication deadlock due to InnoDB lock conflicts
* [Revision #4075](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4075)\
  Fri 2014-03-21 10:11:28 +0100
  * [MDEV-5921](https://jira.mariadb.org/browse/MDEV-5921): In parallel replication, an error is not correctly signalled to the next transaction
* [Revision #4074](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4074)\
  Fri 2014-03-21 15:42:37 +0400
  * [MDEV-5917](https://jira.mariadb.org/browse/MDEV-5917): EITS: different order of predicates in IN (...) causes different estimates - Forgot to update one .result file.
* [Revision #4073](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4073)\
  Fri 2014-03-21 08:39:04 +0200
  * [MDEV-5830](https://jira.mariadb.org/browse/MDEV-5830): Assertion failure mutex\_get\_waiters(mutex) == 0 at shutdown.
* [Revision #4072](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4072)\
  Fri 2014-03-21 00:53:41 +0400
  * [MDEV-5917](https://jira.mariadb.org/browse/MDEV-5917): EITS: different order of predicates in IN (...) causes different estimates - Save range key before making field->pos\_in\_interval() call (like we do for non-equality ranges)
* [Revision #4071](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4071)\
  Thu 2014-03-20 11:11:13 +0400
  * [MDEV-5864](https://jira.mariadb.org/browse/MDEV-5864) - Reduce usage of LOCK\_open: TABLE\_SHARE::tdc.free\_tables
* [Revision #4070](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4070)\
  Thu 2014-03-20 09:32:37 +0200
  * Remove assertions now that the actual bug has been repeated.
* [Revision #4069](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4069) \[merge]\
  Thu 2014-03-20 01:07:01 +0200
  * Automatic merge
  * [Revision #4064.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4064.1.2)\
    Thu 2014-03-20 00:59:13 +0200
    * Fix for [MDEV-5589](https://jira.mariadb.org/browse/MDEV-5589): "Discrepancy in binlog on half-failed CREATE OR REPLACE"
  * [Revision #4064.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4064.1.1) \[merge]\
    Wed 2014-03-19 15:18:29 +0200
    * Automatic merge
    * [Revision #4063.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4063.1.1)\
      Wed 2014-03-19 15:15:57 +0200
      * [MDEV-5854](https://jira.mariadb.org/browse/MDEV-5854) Interrupted CREATE OR REPLACE is written into binlog, and in a wrong format
* [Revision #4068](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4068) \[merge]\
  Wed 2014-03-19 14:58:29 -0700
  * Merge.
  * [Revision #3427.47.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.47.1)\
    Tue 2014-03-18 11:30:50 -0700
    * Fixed bug [MDEV-5191](https://jira.mariadb.org/browse/MDEV-5191). Corrected cost estimates when a join buffer is used and the optimizer is requested to use condition selectivities.
* [Revision #4067](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4067)\
  Wed 2014-03-19 19:35:42 +0200
  * Better to use ut\_ad macro.
* [Revision #4066](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4066)\
  Wed 2014-03-19 20:05:54 +0400
  * [MDEV-5901](https://jira.mariadb.org/browse/MDEV-5901): EITS: killing the server leaves statistical tables in "marked as crashed" state - Part#2: call HA\_EXTRA\_FLUSH for the correct handler object, and call it after every change (ha\_write\_row, ha\_update\_row, ha\_delete\_row).
* [Revision #4065](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4065)\
  Wed 2014-03-19 17:23:38 +0200
  * [MDEV-5830](https://jira.mariadb.org/browse/MDEV-5830): Assertion failure mutex\_get\_waiters(mutex) == 0 at shutdown.
* [Revision #4064](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4064) \[merge]\
  Wed 2014-03-19 16:37:17 +0400
  * Merge
  * [Revision #4060.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4060.1.1)\
    Wed 2014-03-19 16:32:57 +0400
    * [MDEV-5901](https://jira.mariadb.org/browse/MDEV-5901): EITS: killing the server leaves statistical tables in "marked as crashed" state - Do like sp.cc does with mysql.proc table: call HA\_EXTRA\_FLUSH after we've modified a statistical table.
* [Revision #4063](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4063)\
  Wed 2014-03-19 11:35:32 +0200
  * RBR triggers compiled-out with ifdefs in 10.0
* [Revision #4062](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4062)\
  Wed 2014-03-19 11:00:56 +0200
  * [MDEV-9095](https://jira.mariadb.org/browse/MDEV-9095): Executing triggers on slave in row-based replication
* [Revision #4061](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4061)\
  Mon 2014-03-17 15:49:41 +0200
  * [MDEV-5878](https://jira.mariadb.org/browse/MDEV-5878): Failing assertion: mutex\_own(mutex) with innodb\_use\_fallocate=ON.
* [Revision #4060](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4060) \[merge]\
  Mon 2014-03-17 13:45:56 +0400
  * Merge
  * [Revision #4054.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4054.1.1)\
    Sun 2014-03-16 14:33:37 +0100
    * [MDEV-4410](https://jira.mariadb.org/browse/MDEV-4410): update does not want to use a covering index, but select uses it - If an UPDATE 1) modifies the key it is using, and 2) has ORDER BY ... LIMIT which matches the key it is using, Then we should use "Using buffer", not "Using filesort".
* [Revision #4059](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4059)\
  Mon 2014-03-17 09:44:17 +0100
  * Fix missing .result file update before push.
* [Revision #4058](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4058)\
  Wed 2014-03-12 09:08:17 +0100
  * Update the help text for `--slave-parallel-threads`, to clarify the meaning of the count, and to remove the alpha warning.
* [Revision #4057](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4057)\
  Wed 2014-03-12 00:14:49 +0100
  * [MDEV-5804](https://jira.mariadb.org/browse/MDEV-5804): If same GTID is received on multiple master connections in multi-source replication, the event is double-executed causing corruption or replication failure
* [Revision #4056](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4056)\
  Sun 2014-03-09 10:27:38 +0100
  * [MDEV-5804](https://jira.mariadb.org/browse/MDEV-5804): If same GTID is received on multiple master connections in multi-source replication, the event is double-executed causing corruption or replication failure
* [Revision #4055](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4055)\
  Sat 2014-03-15 16:56:35 +0400
  * create\_or\_replace test failed with embedded-server due to different thread IDs
* [Revision #4054](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4054)\
  Fri 2014-03-14 18:52:16 +0100
  * [MDEV-5814](https://jira.mariadb.org/browse/MDEV-5814): MySQL Bug#13948247 DIVISION BY 0 IN GET\_BEST\_DISJUNCT\_QUICK WITH FORCE INDEX GROUP BY - Adopt MySQL's fix: don't run index\_merge optimizer if the table statistics reports that the table has 0 rows.
* [Revision #4053](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4053) \[merge]\
  Fri 2014-03-14 17:23:13 +0100
  * Merge
  * [Revision #4032.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4032.1.4)\
    Fri 2014-03-07 13:21:16 +0100
    * Bug #13571700 TINYBLOB NOT NULL, CRASH IN PROTOCOL::NET\_STORE\_DATA - Backport testcase from mysql-5.6
  * [Revision #4032.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4032.1.3)\
    Fri 2014-03-07 13:14:58 +0100
    * Bug#45227: Lost HAVING clause led to a wrong result. - Backport testcase from mysql-5.6
  * [Revision #4032.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4032.1.2)\
    Fri 2014-03-07 13:00:20 +0100
    * BUG#13803810: TOO FEW ROWS RETURNED FOR RANGE ACCESS IN VARCHAR INDEX USING DATETIME VALUE - Backport the testcase from mysql-5.6
  * [Revision #4032.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4032.1.1)\
    Fri 2014-03-07 12:49:40 +0100
    * BUG#13731380: RANGE OPTIMIZER CALLS RECORDS\_IN\_RANGE() FOR OPEN RANGE - Backport testcase from mysql-5.6
* [Revision #4052](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4052)\
  Fri 2014-03-14 09:31:16 +0200
  * [MDEV-5819](https://jira.mariadb.org/browse/MDEV-5819): MySQL Bug #13500371 63704: CONVERSION OF '1.' TO A NUMBER GIVES ERROR 1265 (WARN\_DATA\_TRUNCATED)
* [Revision #4051](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4051) \[merge]\
  Thu 2014-03-13 16:43:11 +0200
  * Merge with 10.0-base Automatic merge, except for server\_audit.cc that had to be modified slightly Changes to xtradb and innobase where ignored was these made no sence for 10.0
  * [Revision #3427.43.14](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.14) \[merge]\
    Tue 2014-03-11 17:49:09 +0200
    * Merge with 5.5
    * [Revision #3413.21.561](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.561)\
      Tue 2014-03-11 16:53:24 +0200
      * Fixed a compiler failure and removed some warnings in windows
    * [Revision #3413.21.560](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.560)\
      Mon 2014-03-10 21:40:27 +0200
      * Fixed [MDEV-5724](https://jira.mariadb.org/browse/MDEV-5724) "Server crashes on SQL select containing more group by and left join statements using innodb tables"
    * [Revision #3413.21.559](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.559)\
      Tue 2014-03-04 20:50:19 +0100
      * [MDEV-5703](https://jira.mariadb.org/browse/MDEV-5703): \[PATCH] Slave disconnects and fails to reconnect on Error\_code: 1159
    * [Revision #3413.21.558](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.558)\
      Tue 2014-03-04 16:15:58 +0400
      * [MDEV-5723](https://jira.mariadb.org/browse/MDEV-5723): mysqldump -uroot unusable for multi-database operations, checks all databases - MariaDB-5.5 part of the fix: since we can't easily fix query optimization for I\_S tables, run the affected-tablespaces query with semijoin=off. It happens to have a good query plan with that setting.
    * [Revision #3413.21.557](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.557)\
      Fri 2014-02-28 00:41:08 +0400
      * [MDEV-5756](https://jira.mariadb.org/browse/MDEV-5756) Add Audit Plugin to Debian packaging.
    * [Revision #3413.21.556](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.556)\
      Fri 2014-02-28 00:23:20 +0400
      * [MDEV-5436](https://jira.mariadb.org/browse/MDEV-5436) mysqld crash signal 11 in mysql\_audit\_general. That error 'Can't open the pid file' leads to mysqld crash signal 11 in mysql\_audit\_general() called with the 'thd' parameter set to NULL. That wasn't checked when the thd->db and thd->db\_length were accessed. Fixed by checking for the NULL thd.
    * [Revision #3413.21.555](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.555)\
      Wed 2014-02-26 16:25:05 +0400
      * Increment the version number
    * [Revision #3413.21.554](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.554)\
      Wed 2014-02-26 13:49:50 +0200
      * [MDEV-5746](https://jira.mariadb.org/browse/MDEV-5746): Slow file extend when innodb\_use\_fallocate=1 and SSD file storage.
    * [Revision #3413.21.553](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.553)\
      Wed 2014-02-26 12:06:12 +0200
      * [MDEV-5742](https://jira.mariadb.org/browse/MDEV-5742): Assertion failure node->n\_pending on fil0fil.c line 5039 on debug build when innodb\_use\_fallocate=1
    * [Revision #3413.21.552](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3413.21.552)\
      Mon 2014-02-24 23:40:16 +0400
      * MariaDB Audit plugin added.
* [Revision #4050](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4050)\
  Thu 2014-03-13 10:38:41 +0200
  * [MDEV-5840](https://jira.mariadb.org/browse/MDEV-5840): group\_concat( column\_json(dynamic\_column )) return empty result
* [Revision #4049](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4049)\
  Wed 2014-03-12 12:34:47 +0100
  * update test results
* [Revision #4048](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4048)\
  Wed 2014-03-12 12:34:36 +0100
  * typo fixed
* [Revision #4047](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4047)\
  Wed 2014-03-12 11:26:40 +0200
  * [MDEV-5619](https://jira.mariadb.org/browse/MDEV-5619): CREATE OR REPLACE does not release MDL\_EXCLUSIVE upon failure
* [Revision #4046](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4046)\
  Wed 2014-03-12 11:24:03 +0200
  * Fixed some failing tests Remove memory warnings if mysql client aborts early Changed copyright for clients
* [Revision #4045](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4045)\
  Fri 2014-03-07 11:43:06 +0400
  * [MDEV-5766](https://jira.mariadb.org/browse/MDEV-5766) - my\_atomic\_load does memory writes
* [Revision #4044](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4044)\
  Tue 2014-03-11 00:03:53 +0400
  * Increase version number
* [Revision #4043](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4043)\
  Tue 2014-03-11 00:02:22 +0400
  * The test had synchronization point, but did not save master position before that, which caused indeterministic outcome
* [Revision #4042](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4042)\
  Mon 2014-03-10 21:14:38 +0200
  * Fixed [MDEV-5724](https://jira.mariadb.org/browse/MDEV-5724) "Server crashes on SQL select containing more group by and left join statements using innodb tables"
* [Revision #4041](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4041)\
  Mon 2014-03-10 14:08:12 +0200
  * Fixed [MDEV-5780](https://jira.mariadb.org/browse/MDEV-5780) "create-big fails in 10.0"

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
