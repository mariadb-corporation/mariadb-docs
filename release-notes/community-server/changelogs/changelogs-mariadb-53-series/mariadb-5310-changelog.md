# MariaDB 5.3.10 Changelog

[Download](https://downloads.mariadb.org/mariadb/5.3.10) |[Release Notes](../../old-releases/5.3/5.3.10.md) |**Changelog** |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 13 Nov 2012

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.10.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #3599](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3599)\
  Sat 2012-11-10 00:10:06 +0200
  * Increase the version number to 5.3.10.
* [Revision #3598](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3598)\
  Sat 2012-11-10 00:04:44 +0200
  * adjusted test result
* [Revision #3597](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3597)\
  Fri 2012-11-09 15:27:13 +0200
  * adjust openssl\_1 test as in 5.2 (no idea why this didn't merge)
* [Revision #3596](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3596)\
  Fri 2012-11-09 13:07:32 +0200
  * [MDEV-3810](https://jira.mariadb.org/browse/MDEV-3810) fix.
  * The problem is that memory alocated by copy\_andor\_structure() well be freed,\
    but if level of SELECT\_LEX it will be excluded (in case of merge derived tables and view)\
    then sl->where/having will not be updated here but still can be accessed (so it will be access to freed memory).
  * (patch by Sanja)
* [Revision #3595](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3595) \[merge]\
  Fri 2012-11-09 13:05:05 +0200
  * merge from 5.2
  * [Revision #2732.57.33](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.33)\
    Fri 2012-11-09 12:49:12 +0200
    * Disable PBXT on Windows to match all other platforms.
* [Revision #3594](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3594) \[merge]\
  Fri 2012-11-09 12:54:48 +0200
  * merge test case adjustments from 5.2
  * [Revision #2732.57.32](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.32)\
    Fri 2012-11-09 11:56:27 +0200
    * Removed the dependency on PBXT from tests information\_schema\_all\_engines, and is\_columns\_is.
    * Made information\_schema\_all\_engines stable by adding "sorted\_result".
* [Revision #3593](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3593) \[merge]\
  Fri 2012-11-09 10:47:33 +0200
  * Merge from 5.2
  * [Revision #2732.57.31](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.31)\
    Thu 2012-11-08 23:18:56 +0100
    * Fix mis-merge.
* [Revision #3592](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3592) \[merge]\
  Fri 2012-11-09 10:11:20 +0200
  * Merge [MariaDB 5.1.66](../../old-releases/5.1/5.1.66.md) -> 5.2 -> 5.3
  * [Revision #2732.57.30](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.30) \[merge]\
    Thu 2012-11-08 22:26:05 +0200
    * Merged and adjusted test cases from 5.1 after the merge with 5.1.
    * [Revision #2643.153.23](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.23)\
      Wed 2012-11-07 17:48:02 +0200
      * Updated test results after the mysql 5.1 merge.
  * [Revision #2732.57.29](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.29) \[merge]\
    Thu 2012-11-08 15:24:35 +0200
    * Merge [MariaDB 5.1.66](../../old-releases/5.1/5.1.66.md) -> 5.2.12
    * [Revision #2643.153.22](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.22) \[merge]\
      Tue 2012-11-06 11:52:55 +0200
      * Merge MySQL 5.1.66 -> MariaDB 5.1.65
    * [Revision #2643.153.21](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.21) \[merge]\
      Thu 2012-11-01 16:20:09 +0100
      * Merge XtraDB from Percona-Server 5.1.66-rel14.1 into [MariaDB 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md).
      * [Revision #0.6.48](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/0.6.48)\
        Thu 2012-11-01 15:16:42 +0100
        * Updated with changes from Percona Server 5.1.66-rel14.1 tarball.
  * [Revision #2732.57.28](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.28)\
    Fri 2012-11-02 08:21:03 +0100
    * Update result file now we no longer build PBXT.
* [Revision #3591](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3591) \[merge]\
  Fri 2012-11-02 15:59:16 -0700
  * Merge.
  * [Revision #3588.2.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3588.2.1)\
    Thu 2012-11-01 14:54:33 -0700
    * Fixed bug [MDEV-585](https://jira.mariadb.org/browse/MDEV-585) (LP bug #637962)
    * If, when executing a query with ORDER BY col LIMIT n, the optimizer chose\
      an index-merge scan to access the table containing col while there existed\
      an index defined over col then optimizer did not consider the possibility\
      of using an alternative range scan by this index to avoid filesort. This\
      could cause a performance degradation if the optimizer flag index\_merge was\
      set up to 'on'.
* [Revision #3590](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3590) \[merge]\
  Fri 2012-11-02 15:35:09 +0400
  * Merge: bzr ignore sql-bench/test-table-elimination
  * [Revision #3588.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3588.1.1)\
    Fri 2012-11-02 15:31:54 +0400
    * bzr ignore sql-bench/test-table-elimination
* [Revision #3589](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3589) \[merge]\
  Thu 2012-11-01 21:36:31 +0200
  * Merge 5.2 -> 5.3
  * [Revision #2732.57.27](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.27) \[merge]\
    Thu 2012-11-01 15:44:34 +0200
    * Merge 5.1 -> 5.2
    * [Revision #2643.153.20](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.20)\
      Wed 2012-10-31 23:49:51 +0200
      * Fixed [MDEV-612](https://jira.mariadb.org/browse/MDEV-612), [Bug #1010759](https://bugs.launchpad.net/bugs/1010759) - Valgrind error ha\_maria::check\_if\_incompatible\_data on
    * [Revision #2643.153.19](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.19)\
      Wed 2012-10-31 23:22:32 +0200
      * Fixed [MDEV-647](https://jira.mariadb.org/browse/MDEV-647),[Bug #986261](https://bugs.launchpad.net/bugs/986261) - Aria unit tests fail at ma\_test2
  * [Revision #2732.57.26](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.26)\
    Thu 2012-11-01 00:06:09 +0200
    * Fix of non-deterministic results.
  * [Revision #2732.57.25](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.25)\
    Wed 2012-10-31 23:04:53 +0200
    * Do not build pbxt.
  * [Revision #2732.57.24](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.24)\
    Tue 2012-10-09 17:36:02 +0300
    * [MDEV-616](https://jira.mariadb.org/browse/MDEV-616) fix (MySQL fix accepted)
  * [Revision #2732.57.23](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.23)\
    Sun 2012-10-14 19:29:31 +0300
    * [MDEV-746](https://jira.mariadb.org/browse/MDEV-746): Merged mysql fix of the [Bug #1002546](https://bugs.launchpad.net/bugs/1002546) & MySQL Bug#13651009.
    * Empty result after reading const tables now works for subqueries.
  * [Revision #2732.57.22](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.22)\
    Tue 2012-10-02 12:53:20 +0300
    * fixed [MDEV-568](https://jira.mariadb.org/browse/MDEV-568): Wrong result for a hash index look-up if the index is unique and the key is NULL
    * Check ability of index to be NULL as it made in MyISAM. UNIQUE with NULL could have several NULL entries so we have to continue even if ve have found a row.
* [Revision #3588](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3588)\
  Wed 2012-10-31 09:34:25 +0400
  * [MDEV-772](https://jira.mariadb.org/browse/MDEV-772), [MDEV-744](https://jira.mariadb.org/browse/MDEV-744): Fix test-table-elimination script to work.
* [Revision #3587](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3587)\
  Wed 2012-10-10 22:42:50 +0300
  * Fix of [MDEV-3799](https://jira.mariadb.org/browse/MDEV-3799).
  * Find left table in right join (which turned to left join by reordering tables in join list but phisical order of tables of SELECT left as it was).
* [Revision #3586](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3586)\
  Wed 2012-10-10 09:21:22 +0400
  * Backport of: olav.sandstaa@oracle.com-20120516074923-vd0dhp183vqcp2ql
  * .. into [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)

```
Fix for Bug#12667154 SAME QUERY EXEC AS WHERE SUBQ GIVES DIFFERENT
 RESULTS ON IN() & NOT IN() COMP #3
. 
 This bug causes a wrong result in mysql-trunk when ICP is used
 and bad performance in mysql-5.5 and mysql-trunk.
. 
 Using the query from bug report to explain what happens and causes
 the wrong result from the query when ICP is enabled:
. 
 1. The t3 table contains four records. The outer query will read
 these and for each of these it will execute the subquery.
. 
 2. Before the first execution of the subquery it will be optimized. In
 this case the important is what happens to the first table t1:
 -make_join_select() will call the range optimizer which decides
 that t1 should be accessed using a range scan on the k1 index
 It creates a QUICK_RANGE_SELECT object for this.
 -As the last part of optimization the ICP code pushes the
 condition down to the storage engine for table t1 on the k1 index.
. 
 This produces the following information in the explain for this table:
. 
 2 DEPENDENT SUBQUERY t1 range k1 k1 5 NULL 3 Using index condition; Using filesort
. 
 Note the use of filesort.
. 
 3. The first execution of the subquery does (among other things) due
 to the need for sorting:
 a. Call create_sort_index() which again will call find_all_keys():
 b. find_all_keys() will read the required keys for all qualifying
 rows from the storage engine. To do this it checks if it has a
 quick-select for the table. It will use the quick-select for
 reading records. In this case it will read four records from the
 storage engine (based on the range criteria). The storage engine
 will evaluate the pushed index condition for each record.
 c. At the end of create_sort_index() there is code that cleans up a
 lot of stuff on the join tab. One of the things that is cleaned
 is the select object. The result of this is that the
 quick-select object created in make_join_select is deleted.
. 
 4. The second execution of the subquery does the same as the first but
 the result is different:
 a. Call create_sort_index() which again will call find_all_keys()
 (same as for the first execution)
 b. find_all_keys() will read the keys from the storage engine. To
 do this it checks if it has a quick-select for the table. Now
 there is NO quick-select object(!) (since it was deleted in
 step 3c). So find_all_keys defaults to read the table using a
 table scan instead. So instead of reading the four relevant records
 in the range it reads the entire table (6 records). It then
 evaluates the table's condition (and here it goes wrong). Since
 the entire condition has been pushed down to the storage engine
 using ICP all 6 records qualify. (Note that the storage engine
 will not evaluate the pushed index condition in this case since
 it was pushed for the k1 index and now we do a table scan
 without any index being used).
 The result is that here we return six qualifying key values
 instead of four due to not evaluating the table's condition.
 c. As above.
. 
 5. The two last execution of the subquery will also produce wrong results
 for the same reason.
. 
 Summary: The problem occurs due to all but the first executions of the
 subquery is done as a table scan without evaluating the table's
 condition (which is pushed to the storage engine on a different
 index). This is caused by the create_sort_index() function deleting
 the quick-select object that should have been used for executing the
 subquery as a range scan.
. 
 Note that this bug in addition to causing wrong results also can
 result in bad performance due to executing the subquery using a table
 scan instead of a range scan. This is an issue in MySQL 5.5.
. 
 The fix for this problem is to avoid that the Quick-select-object that
 the optimizer created is deleted when create_sort_index() is doing
 clean-up of the join-tab. This will ensure that the quick-select
 object and the corresponding pushed index condition will be available
 and used by all following executions of the subquery.
```

* [Revision #3585](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3585)\
  Fri 2012-10-05 12:26:55 +0300
  * Fix of [MDEV-589](https://jira.mariadb.org/browse/MDEV-589).
  * The problem was in incorrect detection of merged views in tem\_direct\_view\_ref::used\_tables() .
* [Revision #3584](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3584)\
  Mon 2012-10-01 19:04:17 -0700
  * Added the reported test case for LP bug #823237 (a duplicate of bug #823189).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
