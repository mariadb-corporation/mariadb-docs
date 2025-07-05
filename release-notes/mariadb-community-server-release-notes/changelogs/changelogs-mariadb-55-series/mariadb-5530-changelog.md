# MariaDB 5.5.30 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.30) | [Release Notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5530-release-notes.md) | **Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 12 Mar 2013

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5530-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3690](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3690)\
  Mon 2013-03-11 13:50:17 +0400
  * The i386 specific code improving character set conversion on the ASCII range was not enabled on x86\_64 machines. Enabling it. Gives up to 18 times conversion performance improvement.
  * modified: sql/sql\_string.cc
* [Revision #3689](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3689) \[merge]\
  Sun 2013-03-10 12:46:56 +0100
  * 5.3->5.5 merge
  * [Revision #2502.567.79](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.79)\
    Fri 2013-03-08 00:25:26 -0800
    * Fixed bug [MDEV-4250](https://jira.mariadb.org/browse/MDEV-4250). This is a bug in the legacy code. It did not manifest itself because it was masked by other bugs that were fixed by the patches for [MDEV-4172](https://jira.mariadb.org/browse/MDEV-4172) and [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177).
  * [Revision #2502.567.78](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.78)\
    Wed 2013-03-06 22:22:24 +0100
    * Fix typo (clang issued warning that =+ was used where += was intended)
  * [Revision #2502.567.77](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.77)\
    Wed 2013-03-06 21:10:58 +0200
    * [MDEV-4241](https://jira.mariadb.org/browse/MDEV-4241) fix.
    * Field\_enum incorrectly inherited decimals() from Field\_string. Field\_enum should be always integer in numeric context.
* [Revision #3688](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3688)\
  Fri 2013-03-08 19:09:45 +0100
  * [MDEV-4186](https://jira.mariadb.org/browse/MDEV-4186) Test case main.myisampack fails on ppc32 (only)
  * fix the declaration to use the correct type for st\_handler\_check\_param::sort\_buffer\_length. remove redundant casts.
* [Revision #3687](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3687)\
  Fri 2013-03-08 19:09:15 +0100
  * [MDEV-4175](https://jira.mariadb.org/browse/MDEV-4175) auth\_socket to build on OpenBSD / Bitrig
* [Revision #3686](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3686) \[merge]\
  Fri 2013-03-08 19:08:45 +0100
  * merge with XtraDB as of Percona-Server-5.5.30-rel30.1
  * [Revision #0.12.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.61)\
    Fri 2013-03-08 13:13:46 +0100
    * Percona-Server-5.5.30-rel30.1.tar.gz
* [Revision #3685](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3685)\
  Wed 2013-03-06 09:38:08 +0100
  * hack in dependencies to imitate mysql-\*.rpm even better
* [Revision #3684](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3684)\
  Wed 2013-03-06 09:32:13 +0100
  * [MDEV-4068](https://jira.mariadb.org/browse/MDEV-4068) rpm scriptlet chown command dangerous
  * add `--mysqld` option to my\_print\_defaults change server-postin script to use that
* [Revision #3683](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3683)\
  Tue 2013-03-05 17:49:37 +0100
  * [MDEV-4066](https://jira.mariadb.org/browse/MDEV-4066) semisync\_master + temporary tables causes memory leaks
  * close (and auto-drop) temporary tables before rolling back the last transaction in the connection.
* [Revision #3682](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3682)\
  Wed 2013-03-06 01:45:25 +0400
  * TODO-424 geometry query crashes server. The bug was found by Alyssa Milburn. If the number of points of a geometry feature read from binary representation is greater than 0x10000000, then the (uint32) (num\_points \* 16) will cut the higher byte, which leads to various errors. Fixed by additional check if (num\_points > max\_n\_points).
* [Revision #3681](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3681)\
  Tue 2013-03-05 20:15:36 +0200
  * Fix for assert found by mysql-test-run
* [Revision #3680](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3680)\
  Tue 2013-03-05 00:53:18 +0200
  * Fixed issue with LOCK TABLE + ALTER TABLE ENABLE KEYS + SHOW commands.
* [Revision #3679](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3679)\
  Mon 2013-03-04 12:49:35 +0100
  * Fix wrong install location for DEB supportfiles.
* [Revision #3678](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3678) \[merge]\
  Sat 2013-03-02 14:04:11 -0800
  * Merge
  * [Revision #3672.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3672.1.1)\
    Sat 2013-03-02 12:36:32 -0800
    * Fixed bug [MDEV-4220](https://jira.mariadb.org/browse/MDEV-4220). This bug is a regression bug. The regression was introduced by the patch for [MDEV-3851](https://jira.mariadb.org/browse/MDEV-3851), that tried to weaken the condition when a ref access with an extended key can be converted to an eq\_ref access. The patch incorrectly formed this condition. As a result, while improving performance for some queries, the patch caused worse performance for another queries.
* [Revision #3677](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3677)\
  Fri 2013-03-01 20:58:19 +0100
  * [MDEV-4216](https://jira.mariadb.org/browse/MDEV-4216) : export additional functions mysql\_get\_timeout\_value(),mysql\_get\_timeout\_value\_ms(), mysql\_get\_socket() from shared client library. They are documented as part of async API.
  * Also, remove functions mysql\_close\_slow\_part\_start() and mysql\_close\_slow\_part\_cont() from exports - they are not documented anywhere.
* [Revision #3676](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3676)\
  Fri 2013-03-01 11:36:15 -0500
  * Removed the obsolete instructions from the MySQL 5.1 manual. Instead provide a link to
* [Revision #3675](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3675) \[merge]\
  Fri 2013-03-01 18:09:06 +0200
  * Automatic merge
  * [Revision #3667.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3667.1.3)\
    Fri 2013-03-01 18:01:44 +0200
    * Fixed bug MPDEV-628 / [Bug #989055](https://bugs.launchpad.net/bugs/989055) - Querying myisam table metadata may corrupt the table.
    * The issue was that there was that SHOW commands could open the table in the store engine, even in cases where it should not be allowed to do that (ie, the storage engines meta data for that table was under big changes).
    * The cases where this should not be allowed are: - ALTER TABLE DISABLE KEYS - ALTER TABLE ENABLE KEYS - REPAIR TABLE - OPTIMIZE TABLE - DROP TABLE
    * This patch adds a new mode, protected\_against\_usage(). If this is used then the SHOW command will wait until the table is accessable. This is implemented by re-using the already exising 'version' flag for TABLE\_SHARE. It also added functions to be used to change TABLE\_SHARE->version instead of changing it directly.
  * [Revision #3667.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3667.1.2)\
    Thu 2013-02-28 16:47:03 +0200
    * Added test case for bug in replace with replication that existed in MySQL 5.1: Replace with an auto\_increment primary key and another unique key didn't replicate correctly with REPLACE
  * [Revision #3667.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3667.1.1)\
    Thu 2013-02-28 08:42:05 +0200
    * Added support for `--crash-script` in mysqld\_safe. Trivial cleanup
* [Revision #3674](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3674)\
  Fri 2013-03-01 14:58:19 +0100
  * Fix compile error when building with DBUG, but without DEBUG\_SYNC.
* [Revision #3673](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3673) \[merge]\
  Fri 2013-03-01 11:44:10 +0400
  * Merge 5.3->5.5
  * [Revision #2502.567.76](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.76)\
    Fri 2013-03-01 08:23:35 +0400
    * Fix compile error on windows in fix for [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177).
  * [Revision #2502.567.75](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.75) \[merge]\
    Thu 2013-02-28 17:09:56 -0800
    * Merge
    * [Revision #2502.574.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.574.1)\
      Thu 2013-02-28 14:35:46 -0800
      * Fixed bug [MDEV-4209](https://jira.mariadb.org/browse/MDEV-4209) Do not include BLOB fields into the key to access the temporary table created for a materialized view/derived table. BLOB components are not allowed in keys.
* [Revision #3672](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3672) \[merge]\
  Thu 2013-02-28 23:56:17 +0100
  * merge with XtraDB as of Percona-Server-5.5.29-rel30.0
  * [Revision #0.12.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.60)\
    Thu 2013-02-28 22:23:45 +0100
    * Percona-Server-5.5.29-rel30.0.tar.gz
* [Revision #3671](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3671) \[merge]\
  Thu 2013-02-28 22:47:29 +0100
  * 5.3->5.5 merge
  * [Revision #2502.567.74](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.74) \[merge]\
    Thu 2013-02-28 21:48:47 +0100
    * 5.2 -> 5.3
    * [Revision #2502.566.43](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.43) \[merge]\
      Thu 2013-02-28 19:00:58 +0100
      * 5.1 -> 5.2 merge
      * [Revision #2502.565.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.36)\
        Thu 2013-02-28 11:46:35 +0100
        * a simpler fix for MySQL Bug #12408412: GROUP\_CONCAT + ORDER BY + INPUT/OUTPUT SAME USER VARIABLE = CRASH and MySQL Bug#14664077 SEVERE PERFORMANCE DEGRADATION IN SOME CASES WHEN USER VARIABLES ARE USED
      * [Revision #2502.565.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.35)\
        Thu 2013-02-28 10:00:07 +0100
        * Fixed BUG#51763 Can't delete rows from MEMORY table with HASH key
      * [Revision #2502.565.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.34) \[merge]\
        Thu 2013-02-28 09:58:39 +0100
        * mysql-5.1 merge
      * [Revision #2502.565.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.33)\
        Tue 2013-02-26 21:20:15 +0100
        * [MDEV-4203](https://jira.mariadb.org/browse/MDEV-4203) : fix maria SE repair functions (wrong operator precedence)
      * [Revision #2502.565.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.32)\
        Thu 2013-02-21 23:20:26 +0100
        * [MDEV-4194](https://jira.mariadb.org/browse/MDEV-4194): Fix typo (missing comma) in mysys error messages
      * [Revision #2502.565.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.31)\
        Thu 2013-02-14 16:27:55 +0400
        * [MDEV-4169](https://jira.mariadb.org/browse/MDEV-4169): mysql-test-run doesn't strip expected warnings (setrlimit)
      * [Revision #2502.565.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.30)\
        Fri 2013-02-01 00:09:36 +0200
        * Fix bug [MDEV-641](https://jira.mariadb.org/browse/MDEV-641)
        * Analysis: Range analysis discoveres that the query can be executed via loose index scan for GROUP BY. Later, GROUP BY analysis fails to confirm that the GROUP operation can be computed via an index because there is no logic to handle duplicate field references in the GROUP clause. As a result the optimizer produces an inconsistent plan. It constructs a temporary table, but on the other hand the group fields are not set to point there.
        * Solution: Make loose scan analysis work in sync with order by analysis. In the case of duplicate columns loose scan will not be applicable. This limitation will be lifted in 10.0 by removing duplicate columns.
  * [Revision #2502.567.73](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.73)\
    Thu 2013-02-28 09:55:35 -0800
    * Fixed a compile error for some platform.
  * [Revision #2502.567.72](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.72)\
    Sun 2013-02-24 19:16:11 -0800
    * Fixed bug [MDEV-4177](https://jira.mariadb.org/browse/MDEV-4177) The function remove\_eq\_cond removes the parts of a disjunction for which it has been proved that they are always true. In the result of this removal the disjunction may be converted into a formula without OR that must be merged into the AND formula that contains the disjunction. The merging of two AND conditions must take into account the multiple equalities that may be part of each of them. These multiple equality must be merged and become part of the and object built as the result of the merge of the AND conditions. Erroneously the function remove\_eq\_cond lacked the code that would merge multiple equalities of the merged AND conditions. This could lead to confusing situations when at the same AND level there were two multiple equalities with common members and the list of equal items contained only some of these multiple equalities. This, in its turn, could lead to an incorrect work of the function substitute\_for\_best\_equal\_field when it tried to optimize ref accesses. This resulted in forming invalid TABLE\_REF objects that were used to build look-up keys when materialized subqueries were exploited.
  * [Revision #2502.567.71](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.71)\
    Thu 2013-02-21 17:13:12 -0800
    * Fixed bug [MDEV-4172](https://jira.mariadb.org/browse/MDEV-4172). This bug in the legacy code could manifest itself in queries with semi-join materialized subqueries. When a subquery is materialized all conditions that are imposed only on the columns belonging to the tables from the subquery are taken into account.The code responsible for subquery optimizations that employes subquery materialization makes sure to remove these conditions from the WHERE conditions of the query obtained after it has transformed the original query into a query with a semi-join. If the condition to be removed is an equality condition it could be added to ON expressions and/or conditions from disjunctive branches (parts of OR conditions) in an attempt to generate better access keys to the tables of the query. Such equalities are supposed to be removed later from all the formulas where they have been added to. However, erroneously, this was not done in some cases when an ON expression and/or a disjunctive part of the OR condition could be converted into one multiple equality. As a result some equality predicates over columns belonging to the tables of the materialized subquery remained in the ON condition and/or the a disjunctive part of the OR condition, and the excuter later, when trying to evaluate them, returned wrong answers as the values of the fields from these equalities were not valid. This happened because any standalone multiple equality (a multiple equality that are not ANDed with any other predicates) lacked the information about equality predicates inherited from upper levels (in particular, inherited from the WHERE condition). The fix adds a reference to such information to any standalone multiple equality.
  * [Revision #2502.567.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.70) \[merge]\
    Wed 2013-02-20 19:22:02 -0800
    * Merge.
    * [Revision #2502.573.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.573.1)\
      Wed 2013-02-20 18:01:36 -0800
      * Fixed bug [MDEV-3913](https://jira.mariadb.org/browse/MDEV-3913). The wrong result set returned by the left join query from the bug test case happened due to several inconsistencies and bugs of the legacy mysql code.
      * The bug test case uses an execution plan that employs a scan of a materialized IN subquery from the WHERE condition. When materializing such an IN- subquery the optimizer injects additional equalities into the WHERE clause. These equalities express the constraints imposed by the subquery predicate. The injected equality of the query in the test case happens to belong to the same equality class, and a new equality imposing a condition on the rows of the materialized subquery is inferred from this class. Simultaneously the multiple equality is added to the ON expression of the LEFT JOIN used in the main query.
      * The inferred equality of the form f1=f2 is taken into account when optimizing the scan of the rows the temporary table that is the result of the subquery materialization: only the values of the field f1 are read from the table into the record buffer. Meanwhile the inferred equality is removed from the WHERE conditions altogether as a constraint on the fields of the temporary table that has been used when filling this table. This equality is supposed to be removed from the ON expression when the multiple equalities of the ON expression are converted into an optimal set of equality predicates. It supposed to be removed from the ON expression as an equality inferred from only equalities of the WHERE condition. Yet, it did not happened due to the following bug in the code.
      * Erroneously the code tried to build multiple equality for ON expression twice: the first time, when it called optimize\_cond() for the WHERE condition, the second time, when it called this function for the HAVING condition. When executing optimize\_con() for the WHERE condition a reference to the multiple equality of the WHERE condition is set in the multiple equality of the ON expression. This reference would allow later to convert multiple equalities of the ON expression into equality predicates. However the second call of build\_equal\_items() for the ON expression that happened when optimize\_cond() was called for the HAVING condition reset this reference to NULL.
      * This bug fix blocks calling build\_equal\_items() for ON expressions for the second time. In general, it will be beneficial for many queries as it removes from ON expressions any equalities that are to be checked for the WHERE condition. The patch also fixes two bugs in the list manipulation operations and a bug in the function substitute\_for\_best\_equal\_field() that resulted in passing wrong reference to the multiple equalities of where conditions when processing multiple equalities of ON expressions.
      * The code of substitute\_for\_best\_equal\_field() and the code the helper function eliminate\_item\_equal() were also streamlined and cleaned up. Now the conversion of the multiple equalities into an optimal set of equality predicates first produces the sequence of the all equalities processing multiple equalities one by one, and, only after this, it inserts the equalities at the beginning of the other conditions.
      * The multiple changes in the output of EXPLAIN EXTENDED are mainly the result of this streamlining, but in some cases is the result of the removal of unneeded equalities from ON expressions. In some test cases this removal were reflected in the output of EXPLAIN resulted in disappearance of “Using where” in some rows of the execution plans.
  * [Revision #2502.567.69](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.69)\
    Wed 2013-02-13 11:58:16 +0200
    * Fix for [MDEV-4140](https://jira.mariadb.org/browse/MDEV-4140)
    * Analysis: Range analysis detects that the subquery is expensive and doesn't build a range access method. Later, the applicability test for loose scan doesn't take that into account, and builds a loose scan method without a range scan on the min/max column. As a result loose scan fetches the first key in each group, rather than the first key that satisfies the condition on the min/max column.
    * Solution: Since there is no SEL\_ARG tree to be used for the min/max column, it is not possible to use loose scan if the min/max column is compared with an expensive scalar subquery. Make the test for loose scan applicability to be in sync with the range analysis code by testing if the min/max argument is compared with an expensive predicate.
  * [Revision #2502.567.68](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.68) \[merge]\
    Tue 2013-02-12 11:49:46 -0800
    * Merge.
    * [Revision #2502.572.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.572.1)\
      Thu 2013-02-07 21:46:02 -0800
      * Fixed bug [MDEV-3995](https://jira.mariadb.org/browse/MDEV-3995). This bug happened because the executor tried to use a wrong TABLE REF object when building access keys. It constructed keys from fields of a materialized table from a ref object created to construct keys from the fields of the underlying base table. This could happen only when materialized table was created for a non-correlated IN subquery and only when the materialized table used for lookups. In this case we are guaranteed to be able to construct the keys from the fields of tables that would be outer tables for the tables of the IN subquery. The patch makes sure that no ref objects constructed from fields of materialized lookup tables are to be used.
  * [Revision #2502.567.67](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.67)\
    Mon 2013-02-11 10:55:58 +0200
    * [MDEV-4123](https://jira.mariadb.org/browse/MDEV-4123) fix.
    * Missed update\_used\_tables() call for multi-update values.
  * [Revision #2502.567.66](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.66)\
    Mon 2013-02-04 17:35:48 +0200
    * Fix for bug [MDEV-765](https://jira.mariadb.org/browse/MDEV-765) ([Bug #825075](https://bugs.launchpad.net/bugs/825075))
    * Analys: The cause for the wrong result was that the optimizer incorrectly chose min/max loose scan when it is not applicable. The applicability test missed the case when a condition on the MIN/MAX argument was OR-ed with a condition on some other field. In this case, the MIN/MAX condition cannot be used for loose scan.
    * Solution: Extend the test check\_group\_min\_max\_predicates() to check that the WHERE clause is of the form: "cond1 AND cond2" where cond1 - does not use min\_max\_column at all. cond2 - is an AND/OR tree with leaves in form "min\_max\_column $CMP$ const" or $CMP$ is one of the functions between, is \[not] null
* [Revision #3670](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3670)\
  Thu 2013-02-28 20:19:53 +0100
  * revert
  * revid:georgi.kodinov@oracle.com-20120309130449-82e3bs5v3et1x0ef committer: Georgi Kodinov [Georgi.Kodinov@Oracle.com](mailto:Georgi.Kodinov@Oracle.com) timestamp: Fri 2012-03-09 15:04:49 +0200 message: Bug #12408412: GROUP\_CONCAT + ORDER BY + INPUT/OUTPUT SAME USER VARIABLE = CRASH Moved the preparation of the variables that receive the output from SELECT INTO from execution time (JOIN:execute) to compile time (JOIN::prepare). This ensures that if the same variable is used in the SELECT part of SELECT INTO it will be properly marked as non-const for this query. Test case added. Used proper fast iterator.
  * a better fix (much smaller and without regressions) is coming from 5.1
* [Revision #3669](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3669) \[merge]\
  Thu 2013-02-28 18:42:49 +0100
  * merge with mysql-5.5.30 minus few incorrect or not applicable changesets
  * [Revision #3077.175.83](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.175.83)\
    Mon 2012-12-17 23:13:46 +0800
    * Approved by Jimmy and Inaam. rb#1576
* [Revision #3668](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3668)\
  Wed 2013-02-27 10:43:07 +0400
  * [MDEV-4208](https://jira.mariadb.org/browse/MDEV-4208): Test rpl.rpl\_rotate\_purge\_deadlock has incorrect preamble
* [Revision #3667](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3667)\
  Sun 2013-02-24 20:05:26 +0100
  * Compilation : fix oqgraph's system check, in case where boost header aren't in standard include directory.
* [Revision #3666](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3666)\
  Thu 2013-02-21 22:59:54 +0100
  * [MDEV-4190](https://jira.mariadb.org/browse/MDEV-4190) : Fix system checks for OpenBSD
* [Revision #3665](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3665)\
  Thu 2013-02-21 21:46:24 +0100
  * [MDEV-4021](https://jira.mariadb.org/browse/MDEV-4021) : Enable Ctrl-C handler when reading password, on Windows.
  * Prior to this patch, \_getch() was used to read password input from console. getch() has a property that it reads Ctrl-C as character with ASCII code 0x03, and disregards Ctrl-C handler for current process. The fix is to use ReadConsole() API instead of getch() , after setting console mode to ENABLE\_PROCESSED\_INPUT - this mode allows current process to handle Ctrl-C events.
* [Revision #3664](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3664)\
  Wed 2013-02-20 14:52:43 +0100
  * [MDEV-4181](https://jira.mariadb.org/browse/MDEV-4181) : ensure mysql client's beep works on all Windows systems. Use MessageBeep, which employs sound card, rather than system speaker. The secondary benefit is that one can use volume control for this sound (see MySQL's Bug #17088)
* [Revision #3663](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3663)\
  Thu 2013-02-21 01:03:45 +0400
  * [MDEV-3819](https://jira.mariadb.org/browse/MDEV-3819) missing constraints for spatial column types. Checks added to return and error when inappropriate geometry type is stored in a field.
* [Revision #3662](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3662)\
  Tue 2013-02-19 23:46:52 +0100
  * [MDEV-4174](https://jira.mariadb.org/browse/MDEV-4174) - Use kqueue for threadpool implementation on more BSD variants than just FreeBSD or OSX - i.e NetBSD, OpenBSD, DragonFly, etc.
* [Revision #3661](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3661)\
  Mon 2013-02-18 20:51:36 +0100
  * fix typo
* [Revision #3660](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3660)\
  Mon 2013-02-18 20:35:11 +0100
  * [MDEV-4183](https://jira.mariadb.org/browse/MDEV-4183): Export additional symbols from RPMs , compatibly to distribution RPMs. -Ensure that symbols listed in CLIENT\_API\_EXTRA are not thrown away by the linker. -Add THR\_KEY\_mysys to this list, because Fedora18 exports it.
* [Revision #3659](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3659)\
  Fri 2013-02-08 22:24:06 +0100
  * [MDEV-4156](https://jira.mariadb.org/browse/MDEV-4156) Test cases query\_cache and query\_cache\_size\_basic fail on 32 bit ppc and s390
* [Revision #3658](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3658)\
  Fri 2013-02-08 12:59:54 +0100
  * make rpm packages to respect CMAKE\_INSTALL\_PREFIX
* [Revision #3657](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3657)\
  Mon 2013-02-04 15:43:26 +0100
  * [MDEV-4127](https://jira.mariadb.org/browse/MDEV-4127) : Export additional symbols when building RPM, to enable both recompiling mysqli or odbc from sources in addition to drop-in replacement functionality.
  * The case in question is compiling mysqli from sources, that needs client\_errors via ER() macro.
  * Previously, we exported it as mysql\_client\_errors (compatibly to Fedora's style symbol renaming, see [MDEV-3842](https://jira.mariadb.org/browse/MDEV-3842)). However, if MariaDB header files are used when compiling mysqli, client\_errors needs to be exported with its original name.
* [Revision #3656](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3656)\
  Sun 2013-02-03 02:53:57 +0400
  * [MDEV-4028](https://jira.mariadb.org/browse/MDEV-4028) - Converted rdiff files to uniform [MDEV-11](https://jira.mariadb.org/browse/MDEV-11) - Modifed tests and result files to use explicit column lists in INSERT and SELECT statements
* [Revision #3655](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3655)\
  Wed 2013-01-30 17:25:02 +0100
  * [MDEV-4113](https://jira.mariadb.org/browse/MDEV-4113): Assertion (group->connection\_count > 0) fails with Percona server in replication test.
  * Assertion happens in replication thread during THD destruction, when thread calls my\_sync(), which in turn calls thd\_wait\_begin() callback. Connection count can be 0, because the counter was decremented before THD destructor. This assertion currently reproducible only in Percona server and not in MariaDB, due to differences in replication code.
  * Fixed by moving code to decrement connection counter after the THD destructor.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
