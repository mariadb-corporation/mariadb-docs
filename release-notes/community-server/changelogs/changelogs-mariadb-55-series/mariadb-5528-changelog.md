# MariaDB 5.5.28 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.28) |[Release Notes](../../old-releases/5.5/5.5.28.md) |**Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 22 Oct 2012

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.28.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3562](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3562)\
  Fri 2012-10-19 09:21:35 UTC
  * Fix the incorrect merge
* [Revision #3561](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3561) \[merge]\
  Thu 2012-10-18 23:33:06 +0200
  * 5.3 merge
  * [Revision #2502.567.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.31)\
    Wed 2012-10-10 22:42:50 +0300
    * Fix of [MDEV-3799](https://jira.mariadb.org/browse/MDEV-3799).
    * Find left table in right join (which turned to left join by reordering tables in join list but phisical order of tables of SELECT left as it was).
  * [Revision #2502.567.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.30)\
    Wed 2012-10-10 09:21:22 +0400
    * Backport of: olav.sandstaa@oracle.com-20120516074923-vd0dhp183vqcp2ql\
      .. into [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)
    * Fix for [Bug #12667154](https://bugs.launchpad.net/bugs/12667154) SAME QUERY EXEC AS WHERE SUBQ GIVES DIFFERENT\
      RESULTS ON IN() & NOT IN() COMP #3
    * This bug causes a wrong result in mysql-trunk when ICP is used\
      and bad performance in mysql-5.5 and mysql-trunk.
    * Using the query from bug report to explain what happens and causes\
      the wrong result from the query when ICP is enabled:
      1. The t3 table contains four records. The outer query will read\
         these and for each of these it will execute the subquery.
      2. Before the first execution of the subquery it will be optimized. In\
         this case the important is what happens to the first table t1:
      3. make\_join\_select() will call the range optimizer which decides\
         that t1 should be accessed using a range scan on the k1 index\
         It creates a QUICK\_RANGE\_SELECT object for this.
      4. As the last part of optimization the ICP code pushes the\
         condition down to the storage engine for table t1 on the k1 index.
      5. This produces the following information in the explain for this table:
         * 2 DEPENDENT SUBQUERY t1 range k1 k1 5 NULL 3 Using index condition; Using filesort
      6. Note the use of filesort.
      7. The first execution of the subquery does (among other things) due\
         to the need for sorting:
      8. Call create\_sort\_index() which again will call find\_all\_keys():
      9. find\_all\_keys() will read the required keys for all qualifying\
         rows from the storage engine. To do this it checks if it has a\
         quick-select for the table. It will use the quick-select for\
         reading records. In this case it will read four records from the\
         storage engine (based on the range criteria). The storage engine\
         will evaluate the pushed index condition for each record.
      10. At the end of create\_sort\_index() there is code that cleans up a\
          lot of stuff on the join tab. One of the things that is cleaned\
          is the select object. The result of this is that the\
          quick-select object created in make\_join\_select is deleted.
      11. The second execution of the subquery does the same as the first but\
          the result is different:
      12. Call create\_sort\_index() which again will call find\_all\_keys()\
          (same as for the first execution)
      13. find\_all\_keys() will read the keys from the storage engine. To\
          do this it checks if it has a quick-select for the table. Now\
          there is NO quick-select object(!) (since it was deleted in\
          step 3c). So find\_all\_keys defaults to read the table using a\
          table scan instead. So instead of reading the four relevant records\
          in the range it reads the entire table (6 records). It then\
          evaluates the table's condition (and here it goes wrong). Since\
          the entire condition has been pushed down to the storage engine\
          using ICP all 6 records qualify. (Note that the storage engine\
          will not evaluate the pushed index condition in this case since\
          it was pushed for the k1 index and now we do a table scan\
          without any index being used).\
          The result is that here we return six qualifying key values\
          instead of four due to not evaluating the table's condition.
      14. As above.
      15. The two last execution of the subquery will also produce wrong results\
          for the same reason.
      16. Summary: The problem occurs due to all but the first executions of the\
          subquery is done as a table scan without evaluating the table's\
          condition (which is pushed to the storage engine on a different\
          index). This is caused by the create\_sort\_index() function deleting\
          the quick-select object that should have been used for executing the\
          subquery as a range scan.
      17. Note that this bug in addition to causing wrong results also can\
          result in bad performance due to executing the subquery using a table\
          scan instead of a range scan. This is an issue in MySQL 5.5.
      18. The fix for this problem is to avoid that the Quick-select-object that\
          the optimizer created is deleted when create\_sort\_index() is doing\
          clean-up of the join-tab. This will ensure that the quick-select\
          object and the corresponding pushed index condition will be available\
          and used by all following executions of the subquery.
  * [Revision #2502.567.29](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.29)\
    Fri 2012-10-05 12:26:55 +0300
    * Fix of [MDEV-589](https://jira.mariadb.org/browse/MDEV-589).
    * The problem was in incorrect detection of merged views in tem\_direct\_view\_ref::used\_tables() .
  * [Revision #2502.567.28](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.28)\
    Mon 2012-10-01 19:04:17 -0700
    * Added the reported test case for LP bug #823237 (a duplicate of bug #823189).
  * [Revision #2502.567.27](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.27)\
    Mon 2012-10-01 15:42:49 +0200
    * increase the version
  * [Revision #2502.567.26](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.26)\
    Sat 2012-09-29 22:44:13 -0700
    * Fixed LP bug #1058071 ([MDEV-564](https://jira.mariadb.org/browse/MDEV-564)).
    * In some rare cases when the value of the system variable join\_buffer\_size\
      was set to a number less than 256 the function JOIN\_CACHE::set\_constants\
      determined the size of an offset in the join buffer equal to 1 though\
      the minimal join buffer required more than 256 bytes. This could cause\
      a crash of the server when records from the join buffer were read.
  * [Revision #2502.567.25](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.25)\
    Fri 2012-09-28 09:54:43 +0200
    * Fix compiler warnings that breaks build (-Werror).
  * [Revision #2502.567.24](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.24) \[merge]\
    Thu 2012-09-27 15:02:17 +0200
    * merge
    * [Revision #2502.566.11](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.11) \[merge]\
      Thu 2012-09-27 12:59:23 +0200
      * Merge from 5.1
      * [Revision #2502.565.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.9)\
        Thu 2012-09-27 12:25:45 +0200
        * Fix incorrect assembler in Taocrypt which causes crashes on i386 with certain GCC versions/options
    * [Revision #2502.566.10](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.10) \[merge]\
      Wed 2012-09-26 18:49:38 +0200
      * merge
      * [Revision #2502.565.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.8)\
        Wed 2012-09-26 11:59:49 +0200
        * always force the language in mysql\_install\_db
    * [Revision #2502.566.9](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.9)\
      Tue 2012-09-25 20:23:01 +0200
      * a simple pam user mapper module
    * [Revision #2502.566.8](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.8) \[merge]\
      Wed 2012-09-26 18:29:49 +0200
      * Merge from 5.1.
      * [Revision #2502.565.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.7)\
        Wed 2012-09-26 15:30:08 +0200
        * Fix some failures in 5.1 Buildbot:
          * Fix some warnings in newer GCC (-Werror ...).
          * Fix wrong STACK\_DIRECTION detected by configure due to compiler inlining.
  * [Revision #2502.567.23](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.23)\
    Thu 2012-09-27 13:18:07 +0500
    * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport --ignore-db-dir.
    * The feature was backported from MySQL 5.6.
    * Some code was added to make commands as
      * `SELECT * FROM ignored_db.t1;`
      * `CALL ignored_db.proc();`
      * `USE ignored_db;`
    * to take that option into account.
    * per-file comments:
      * mysql-test/r/ignore\_db\_dirs\_basic.result
        * test result added.
      * mysql-test/t/ignore\_db\_dirs\_basic-master.opt
        * options for the test,
        * actually the set of --ignore-db-dir lines.
      * mysql-test/t/ignore\_db\_dirs\_basic.test
        * test for the feature.
        * Same test from 5.6 was taken as a basis,
        * then tests for SELECT, CALL etc were added.
    * per-file comments:
      * sql/mysql\_priv.h
        * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport --ignore-db-dir.
        * interface for db\_name\_is\_in\_ignore\_list() added.
      * sql/mysqld.cc
        * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport --ignore-db-dir.
        * \--ignore-db-dir handling.
      * sql/set\_var.cc
        * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport --ignore-db-dir.
        * the @@ignore\_db\_dirs variable added.
      * sql/sql\_show.cc
        * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport --ignore-db-dir.
        * check if the directory is ignored.
      * sql/sql\_show.h
        * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport --ignore-db-dir.
        * interface added for opt\_ignored\_db\_dirs.
      * sql/table.cc
        * [MDEV-495](https://jira.mariadb.org/browse/MDEV-495) backport --ignore-db-dir.
        * check if the directory is ignored.
  * [Revision #2502.567.22](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.22) \[merge]\
    Mon 2012-09-24 17:29:26 +0200
    * merge
    * [Revision #2502.566.7](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.7) \[merge]\
      Mon 2012-09-24 13:57:45 +0200
      * merge
      * [Revision #2502.565.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.6)\
        Mon 2012-09-24 11:33:41 +0200
        * [MDEV-543](https://jira.mariadb.org/browse/MDEV-543) mysql\_install\_db doesn't work with blanks in either basedir or datadir path
  * [Revision #2502.567.21](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.21)\
    Thu 2012-09-20 12:48:59 +0300
    * [MDEV-521](https://jira.mariadb.org/browse/MDEV-521) fix.
    * After pullout item during single row subselect transformation it should be fixed properly.
* [Revision #3560](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3560)\
  Thu 2012-10-18 11:30:29 +0200
  * do not print return address when callstack is output on Windows, it does not provide any useful info
* [Revision #3559](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3559)\
  Thu 2012-10-18 11:19:28 +0200
  * Do not DBUG\_PRINT uninitialized variable. This avoid false positive from runtime checks in debug builds (Windows).
* [Revision #3558](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3558)\
  Wed 2012-10-17 19:04:08 +0200
  * RPM fixes:
  * shared should provide libmysqlclient.so.18(libmysqlclient\_16) too
  * don't "use DBD::mysql" explicitly in mytop
* [Revision #3557](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3557) \[merge]\
  Tue 2012-10-16 13:04:42 +0200
  * mysql-5.5.28
* [Revision #3556](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3556) \[merge]\
  Tue 2012-10-16 10:36:28 +0200
  * XtraDB 1.1.8-29.0
  * [Revision #0.12.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.56)\
    Fri 2012-10-12 17:40:06 +0200
    * Percona-Server-5.5.27-rel29.0
* [Revision #3555](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3555)\
  Tue 2012-10-16 10:35:05 +0200
  * minor test cleanup. one server restart less in mtr
* [Revision #3554](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3554)\
  Tue 2012-10-16 10:34:38 +0200
  * a typo caused plugins to have no MYSQL\_SERVER symbol defined.
  * don't try to define it for plugins, then, as they don't need it.
* [Revision #3553](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3553)\
  Fri 2012-10-12 18:15:38 +0200
  * simplify future xtradb merges (hopefully)
* [Revision #3552](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3552)\
  Fri 2012-10-12 16:44:54 +0300
  * [MDEV-435](https://jira.mariadb.org/browse/MDEV-435): Expensive subqueries may be evaluated during optimization in merge\_key\_fields
  * Fix by Sergey Petrunia.
  * This patch only prevents the evaluation of expensive subqueries during optimization.
  * The crash reported in this bug has been fixed by some other patch.
  * The fix is to call value->is\_null() only when !value->is\_expensive(), because is\_null()\
    may trigger evaluation of the Item, which in turn triggers subquery evaluation if the\
    Item is a subquery.
* [Revision #3551](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3551)\
  Fri 2012-10-12 10:54:46 +0200
  * [MDEV-3802](https://jira.mariadb.org/browse/MDEV-3802). Millisecond timeout support in non-blocking client library.
  * In 10.0, VIO timeouts can be in milliseconds, so we add a new function\
    mysql\_get\_timeout\_value\_ms() which can return millisecond-precision\
    timeout values.
  * In 5.5, we do not have millisecond precision for timeouts. But we still\
    provide the mysql\_get\_timeout\_value\_ms() function; this makes it easier\
    for applications as they can use the millisecond function in 10.0 and\
    still work with the 5.5 version of the client library.
* [Revision #3550](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3550)\
  Thu 2012-10-11 12:09:21 +0300
  * [MDEV-3804](https://jira.mariadb.org/browse/MDEV-3804):
  * MySQL fix for bug#11765413 removed (we have better and more general fix for the problem).
  * Test suite added.
* [Revision #3549](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3549)\
  Mon 2012-10-08 13:06:20 +0200
  * sort status variables
* [Revision #3548](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3548)\
  Fri 2012-10-05 14:24:38 +0200
  * [MDEV-3796](https://jira.mariadb.org/browse/MDEV-3796) various RPM problems
* [Revision #3547](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3547)\
  Mon 2012-10-01 16:12:15 +0200
  * increase the version
* [Revision #3546](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3546)\
  Mon 2012-10-01 16:11:46 +0200
  * update the r/mysqld--help,win.rdiff to match the updated r/mysqld--help.result
* [Revision #3545](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3545)\
  Mon 2012-10-08 13:56:57 +0200
  * [MDEV-519](https://jira.mariadb.org/browse/MDEV-519): mariadb-client-5.5 conflicts with package mytop
  * Do not include mytop in mariadb-client-5.5 .deb package.
  * There is already a Debian mytop package, so we get a package conflict.\
    And there is no reason for the MariaDB project to guerrilla-take-over\
    mytop maintenance.
* [Revision #3544](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3544)\
  Thu 2012-10-04 23:52:11 +0300
  * Fixed issues found by buildbot & valgrind:
    * Wrong thd uses in Item\_subselect, could lead to crash
    * Inititalize uninitialized variable in new autoincrement handling code
* [Revision #3543](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3543)\
  Tue 2012-10-02 16:26:22 +0300
  * Fixed installation issues on debian:
    * Don't abort if plugin table exists
    * Use longer timeout for start/stop of mysqld
* [Revision #3542](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3542)\
  Tue 2012-09-25 13:45:11 +0300
  * makes mi\_test\_all.sh & ma\_test\_all.sh working ([MDEV-285](https://jira.mariadb.org/browse/MDEV-285))
* [Revision #3541](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3541)\
  Tue 2012-09-25 00:46:54 +0200
  * [MDEV-546](https://jira.mariadb.org/browse/MDEV-546) : error when compiling client library - incorrect client\_settings.h
  * Remove sql directory from the include path to workaround the problem. This removes the ambiguity , since then only one client\_settings.h will be in the include paths
* [Revision #3540](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3540)\
  Sat 2012-09-22 14:19:02 +0300
  * Updated mytop to version 1.91
  * Fixed that 'Handler:' output gives correct result with MariaDB (not including temporary tables)
* [Revision #3539](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3539)\
  Fri 2012-09-21 15:03:38 +0200
  * Fix test failure on --embedded-server
* [Revision #3538](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3538)\
  Tue 2012-09-18 23:34:16 +0300
  * This fix+comments was originally made by Alexey Kopytov
  * [Bug #1035225](https://bugs.launchpad.net/bugs/1035225) / MySQL bug #66301: INSERT ... ON DUPLICATE KEY UPDATE +\
    innodb\_autoinc\_lock\_mode=1 is broken
  * The problem was that when certain INSERT ... ON DUPLICATE KEY UPDATE\
    were executed concurrently on a table containing an AUTO\_INCREMENT\
    column as a primary key, InnoDB would correctly reserve non-overlapping\
    AUTO\_INCREMENT intervals for each statement, but when the server\
    encountered the first duplicate key error on the secondary key in one of\
    the statements and performed an UPDATE, it also updated the internal\
    AUTO\_INCREMENT value to the one from the existing row that caused a\
    duplicate key error, even though the AUTO\_INCREMENT value was not\
    specified explicitly in the UPDATE clause. It would then proceed with\
    using AUTO\_INCREMENT values the range reserved previously by another\
    statement, causing duplicate key errors on the AUTO\_INCREMENT column.
  * Fixed by changing write\_record() to ensure that in case of a duplicate\
    key error the internal AUTO\_INCREMENT counter is only updated when the\
    AUTO\_INCREMENT value was explicitly updated by the UPDATE\
    clause. Otherwise it is restored to what it was before the duplicate key\
    error, as that value is unused and can be reused for subsequent\
    successfully inserted rows.
* [Revision #3537](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3537) \[merge]\
  Tue 2012-09-18 15:32:08 +0300
  * Automatic merge
  * [Revision #3533.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3533.1.2)\
    Tue 2012-09-18 15:14:19 +0300
    * Fix for [MDEV-533](https://jira.mariadb.org/browse/MDEV-533): Confusing error code when doing auto-increment insert for out-of-range values
      * create table t1 (a smallint primary key auto\_increment);
        * insert into t1 values(32767);
        * insert into t1 values(NULL);
        * ERROR 1062 (23000): Duplicate entry '32767' for key 'PRIMARY
      * Now on always gets error HA\_ERR\_AUTOINC\_RANGE=167 "Out of range value for column", independent of\
        store engine, SQL Mode or number of inserted rows. This is an unique error that is easier to test for in replication.
      * Another bug fix is that we now get an error when trying to insert a too big auto-generated value, even in non-strict mode.
        * Before one get insted the max column value inserted.
        * This patch also fixes some issues with inserting negative numbers in an auto-increment column.
        * Fixed the ER\_DUP\_ENTRY and HA\_ERR\_AUTOINC\_ERANGE are compared the same between master and slave.
        * This ensures that replication works between an old server to a new slave for auto-increment overflow errors.
        * Added SQLSTATE errors for handler errors
      * Smaller bug fixes:
        * Added warnings for duplicate key errors when using INSERT IGNORE
        * Fixed bug when using --skip-log-bin followed by --log-bin, which did set log-bin to "0"
        * Allow one to see how cmake is called by using --just-print --just-configure
  * [Revision #3533.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3533.1.1)\
    Thu 2012-09-13 21:11:47 +0300
    * Added THD::utime\_after\_query to avoid calling current\_utime() twice for every end-of-query
    * Increment long\_query\_count also if thd->variables.log\_slow\_rate\_limit is used
    * Added new state "Writing to binlog"
* [Revision #3536](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3536)\
  Tue 2012-09-18 15:31:21 +0300
  * Fixed test for ps-protocol
* [Revision #3535](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3535) \[merge]\
  Tue 2012-09-18 13:42:06 +0300
  * Merged the fix for [Bug #1009187](https://bugs.launchpad.net/bugs/1009187), [MDEV-373](https://jira.mariadb.org/browse/MDEV-373)
  * [Revision #2502.567.20](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.20) \[merge]\
    Mon 2012-09-17 11:13:46 +0300
    * Merged the fix for [Bug #1009187](https://bugs.launchpad.net/bugs/1009187), [MDEV-373](https://jira.mariadb.org/browse/MDEV-373).
    * Performed some refactoring and simplification that was enabled and required by the merge.
    * [Revision #2502.566.6](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.6)\
      Fri 2012-09-14 11:26:01 +0300
      * Fix [Bug #1009187](https://bugs.launchpad.net/bugs/1009187), [MDEV-373](https://jira.mariadb.org/browse/MDEV-373), mysql bug#58628
      * Analysis:
        * The queries in question use the \[unique | index]\_subquery execution methods.\
          These methods reuse the ref keys constructed by create\_ref\_for\_key(). The\
          way create\_ref\_for\_key() works is that it doesn't store in ref.key\_copy\[]\
          store\_key elements that represent constants. In particular it doesn't store\
          the store\_key for NULL constants.
        * The execution of \[unique | index]\_subquery calls\
          subselect\_uniquesubquery\_engine::copy\_ref\_key, which in addition to copy\
          the left IN argument into a index lookup key, is supposed to detect if\
          the left IN argument contains NULLs. Since the store\_key for the NULL\
          constant is not copied into the key array, the null is not detected, and\
          execution erroneously proceeds as if it should look for a complete match.
      * Solution:
        * The solution (unlike MySQL) is to reuse already computed information about\
          NULL presence. Item\_in\_optimizer::val\_int already finds out if the left IN\
          operand contains NULLs. The fix propagates this to the execution methods\
          subselect\_\[unique | index]subquery\_engine::exec so it knows if there were\
          NULL values independent of the presence of keys.
        * In addition the patch siplifies copy\_ref\_key() and the logic that hanldes\
          the case of NULLs in the left IN operand.
  * [Revision #2502.567.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.19)\
    Fri 2012-09-07 09:39:51 +0300
    * Fix of [MDEV-511](https://jira.mariadb.org/browse/MDEV-511).
    * As far as we reopen tables so TABLE become invalid we should remove the pointer on cleanup().
* [Revision #3534](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3534)\
  Tue 2012-09-18 00:42:05 +0300
  * Fixed issues in test suite when running with --ps-protocol
* [Revision #3533](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3533)\
  Mon 2012-09-10 17:26:54 +0300
  * Fixed random test failure
* [Revision #3532](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3532)\
  Mon 2012-09-10 16:46:33 +0300
  * Fixed Bug#1002564: Wrong result for a lookup query from a heap table
* [Revision #3531](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3531)\
  Mon 2012-09-10 13:53:19 +0300
  * Fixed compiler warning on Mac
* [Revision #3530](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3530)\
  Sun 2012-09-09 01:22:06 +0300
  * Added new status variables:
    * feature\_dynamic\_columns,feature\_fulltext,feature\_gis,feature\_locale,feature\_subquery,feature\_timezone,feature\_trigger,feature\_xml\
      Opened\_views, Executed\_triggers, Executed\_events
    * Added new process status 'updating status' as part of 'freeing items'
* [Revision #3529](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3529) \[merge]\
  Sun 2012-09-09 00:38:15 +0300
  * Automatic merge
  * [Revision #3521.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3521.1.2)\
    Fri 2012-09-07 17:05:17 +0300
    * Better error message when using --language or --log-bin
    * Simplify code
  * [Revision #3521.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3521.1.1)\
    Wed 2012-09-05 18:23:51 +0300
    * Added function last\_value() which returns the last value but evalutes all arguments as a side effect.
    * Original patch by Eric Herman
* [Revision #3528](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3528)\
  Fri 2012-09-07 09:17:31 +0300
  * Fix of [MDEV-511](https://jira.mariadb.org/browse/MDEV-511).
  * As far as we reopen tables so TABLE become invalid we should remove the pointer on cleanup().

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
