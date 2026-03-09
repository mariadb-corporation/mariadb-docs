# MariaDB 5.5.29 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.29) | [Release Notes](../../old-releases/5.5/5.5.29.md) | **Changelog** |\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 30 Jan 2013

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.29.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3654](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3654)\
  Tue 2013-01-29 12:27:31 +0100
  * more changes for fedora18
* [Revision #3653](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3653)\
  Tue 2013-01-29 10:46:05 +0100
  * fix 'compat' rpm for fedora18
* [Revision #3652](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3652)\
  Mon 2013-01-28 17:24:50 +0100
  * fix embedded build with for cmake 2.6.2 (older cmake could not handle IF(NOT MATCHES)
* [Revision #3651](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3651)\
  Mon 2013-01-28 15:13:39 +0200
  * Fix for [MDEV-3948](https://jira.mariadb.org/browse/MDEV-3948), and backport of the following collection of fixes and backports from [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md).
  * The bug in [MDEV-3948](https://jira.mariadb.org/browse/MDEV-3948) was an instance of the problem fixed by Sergey's patch in 10.0 - namely that the range optimizer could change table->\[read | write]\_set, and not restore it.
  * revno: 3471 committer: Sergey Petrunya [psergey@askmonty.org](mailto:psergey@askmonty.org) branch nick: 10.0-serg-fix-imerge timestamp: Sat 2012-11-03 12:24:36 +0400 message:

## [MDEV-3817](https://jira.mariadb.org/browse/MDEV-3817): Wrong result with index\_merge+index\_merge\_intersection, InnoDB table, join, AND and OR conditions Reconcile the fixes from:

## # guilhem.bichot@oracle.com-20110805143029-ywrzuz15uzgontr0

## Fix for BUG#12698916 - "JOIN QUERY GIVES WRONG RESULT AT 2ND EXEC. OR

## AFTER FLUSH TABLES \[-INT VS NULL]"

## # guilhem.bichot@oracle.com-20111209150650-tzx3ldzxe1yfwji6

## Fix for BUG#12912171 - ASSERTION FAILED: QUICK->HEAD->READ\_SET == SAVE\_READ\_SET

## and

## and related fixes from: BUG#1006164, [MDEV-376](https://jira.mariadb.org/browse/MDEV-376):

* Now, ROR-merged QUICK\_RANGE\_SELECT objects make no assumptions about the values of table->read\_set and table->write\_set. Each QUICK\_ROR\_SELECT has (and had before) its own column bitmap, but now, all QUICK\_ROR\_SELECT's functions that care: reset(), init\_ror\_merged\_scan(), and get\_next() will set table->read\_set when invoked and restore it back to what it was before the call before they return.
* This allows to avoid the mess when somebody else modifies table->read\_set for some reason.
* [Revision #3650](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3650) \[merge]\
  Mon 2013-01-28 13:36:05 +0100
  * 5.3 merge
  * [Revision #2502.567.65](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.65) \[merge]\
    Mon 2013-01-28 09:12:23 +0100
    * 5.2 merge
    * [Revision #2502.566.42](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.42)\
      Mon 2013-01-28 09:10:01 +0100
      * compilation error with -Wuninitialized -Werror
    * [Revision #2502.566.41](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.41) \[merge]\
      Fri 2013-01-25 17:22:21 +0100
      * 5.1 merge
      * [Revision #2502.565.29](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.29)\
        Fri 2013-01-25 14:29:46 +0100
        * [MDEV-729](https://jira.mariadb.org/browse/MDEV-729) [Bug #998028](https://bugs.launchpad.net/bugs/998028) - Server crashes on normal shutdown in closefrm after executing a query from MyISAM table
        * don't write a key value into the record buffer - a key length can be larger then the record length.
      * [Revision #2502.565.28](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.28)\
        Fri 2013-01-25 12:26:35 +0100
        * [MDEV-759](https://jira.mariadb.org/browse/MDEV-759) [Bug #998340](https://bugs.launchpad.net/bugs/998340) - Valgrind complains on simple selects containing expression DAY(FROM\_UNIXTIME(-1))
        * check item->null\_value before using the result of item->val\_int()
  * [Revision #2502.567.64](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.64)\
    Sat 2013-01-26 22:33:18 +0100
    * [MDEV-3875](https://jira.mariadb.org/browse/MDEV-3875) Wrong result (missing row) on a DISTINCT query with the same subquery in the SELECT list and GROUP BY
    * fix remove\_dup\_with\_hash\_index() and remove\_dup\_with\_compare() to take NULLs into account
  * [Revision #2502.567.63](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.63)\
    Fri 2013-01-25 16:56:57 +0200
    * The problem was that expression with field after transformation (on the first execution) reached by fix\_fields() (via reference) before row which it belongs to (on the second execution) and fix\_field for row did not follow usual protocol for Items with argument (first check that the item fixed then call fix\_fields).
    * Item\_row::fix\_field fixed.
* [Revision #3649](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3649)\
  Mon 2013-01-28 13:49:14 +0200
  * [MDEV-4091](https://jira.mariadb.org/browse/MDEV-4091): Dynamic columns C functions should be included in libmysqlclient
* [Revision #3648](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3648) \[merge]\
  Sat 2013-01-26 22:23:27 +0100
  * Merge [MDEV-3842](https://jira.mariadb.org/browse/MDEV-3842), [MDEV-3923](https://jira.mariadb.org/browse/MDEV-3923), [MDEV-3971](https://jira.mariadb.org/browse/MDEV-3971)
  * [Revision #3644.1.4](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3644.1.4)\
    Fri 2013-01-25 23:34:46 +0100
    * fix embedded
  * [Revision #3644.1.3](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3644.1.3)\
    Fri 2013-01-25 18:59:30 +0100
    * Fix embedded build
  * [Revision #3644.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3644.1.2)\
    Fri 2013-01-25 17:26:10 +0100
    * [MDEV-3842](https://jira.mariadb.org/browse/MDEV-3842), [MDEV-3923](https://jira.mariadb.org/browse/MDEV-3923) :
    * Miscellaneous workarounds for drop-in compatibility problems with Linux distributions, arounf versioning of the MySQL 5.5 client shared library. There seems to be 3 different ways major distributions handle versioning
    *
      1. Fedora (also Mageia, and likely other Redhat descendants) way old, 5.1 API functions are given version libmysqlclient\_16 new API functions (client plugins, mysql\_stmt\_next ) are given version libmysqlclient\_18 some extra functions beyond API are exported. some functions are renamed.
    * 2.Debian Wheezy way all functions are given libmysqlclient\_18 version
    *
      3. Ubuntu way (or MySQL/MariaDB download packages) no versioning
    * UIp to this fix, MariaDB distributions did not have any versioning in the libraries, this rendered client library incompatible to distributions thus exchanging distribution's libmysqlclient.so.18.0.0 with MariaDB's did not work nicely (anywhere but on Ubuntu)
    * THE FIX is to build libraries the same way as distributions do it - when building RPMs, use same version script as Fedora does, Make sure to export extra-symbols, the same as Fedora exports. - when building DEBs, use the same version script as Debian Wheezy - do not use version scripts otherwise
    * Also, makes sure that extensions of MySQL APIs (asynchronous client functionality) is exported by the shared libraries.
  * [Revision #3644.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3644.1.1)\
    Fri 2013-01-25 16:50:14 +0100
    * [MDEV-3971](https://jira.mariadb.org/browse/MDEV-3971) : problems installing MariaDB packages (conflicts with mysql-libs-5.5) FIx : make "shared" RPM obsolete/provide mysql-libs
* [Revision #3647](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3647) \[merge]\
  Sat 2013-01-26 01:59:27 +0200
  * Automatic merge
  * [Revision #3645.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3645.1.1)\
    Fri 2013-01-25 21:40:42 +0200
    * Fixed [MDEV-3890](https://jira.mariadb.org/browse/MDEV-3890): Server crash inserting record on a temporary table after truncating it The problem was that a temporary table was re-created as a non-temporary table.
* [Revision #3646](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3646) \[merge]\
  Fri 2013-01-25 11:24:42 +0100
  * 5.3 merge
  * [Revision #2502.567.62](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.62) \[merge]\
    Fri 2013-01-25 10:20:45 +0100
    * 5.2 merge
    * [Revision #2502.566.40](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.40)\
      Fri 2013-01-25 10:19:35 +0100
      * [MDEV-4040](https://jira.mariadb.org/browse/MDEV-4040) Replace deprecated SET OPTION syntax in mysqldump
      * mysqldump.c: s/SET OPTION/SET/ (OPTION was, hm, optional since 3.21, so there's no need to use SET OPTION even in the old compatibility modes)
    * [Revision #2502.566.39](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.39)\
      Fri 2013-01-25 09:41:26 +0100
      * [MDEV-3909](https://jira.mariadb.org/browse/MDEV-3909) remote user enumeration ([CVE-2012-5615](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5615))
      * instead of returning Access denied on the incorrect user name, emulate the complete failed logic procedure, possibly with the change plugin packet.
    * [Revision #2502.566.38](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.38)\
      Fri 2013-01-25 00:20:53 +0100
      * report "using password: YES/NO" correctly for the COM\_CHANGE\_USER failures
    * [Revision #2502.566.37](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.37)\
      Fri 2013-01-25 00:17:39 +0100
      * [MDEV-3915](https://jira.mariadb.org/browse/MDEV-3915) COM\_CHANGE\_USER allows fast password brute-forcing ([CVE-2012-5627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5627))
      * allow only three failed change\_user per connection. successful change\_user do NOT reset the counter
* [Revision #3645](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3645) \[merge]\
  Wed 2013-01-23 15:18:05 -0800
  * Merge 5.3->5.5
  * [Revision #2502.567.61](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.61) \[merge]\
    Mon 2013-01-21 21:29:19 -0800
    * Merge 5.2->5.3
    * [Revision #2502.566.36](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.36) \[merge]\
      Mon 2013-01-21 15:23:40 -0800
      * Merge 5.1->5.2
      * [Revision #2502.565.27](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.27) \[merge]\
        Mon 2013-01-21 13:48:34 -0800
        * Merge.
        * [Revision #2502.571.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.571.1)\
          Mon 2013-01-21 11:47:45 -0800
          * Fixed bug [MDEV-4063](https://jira.mariadb.org/browse/MDEV-4063) (bug #56927). This bug could result in returning 0 for the expressions of the form \<aggregate\_function>(distinct field) when the system variable max\_heap\_table\_size was set to a small enough number. It happened because the method Unique::walk() did not support the case when more than one pass was needed to merge the trees of distinct values saved in an external file.
          * Backported a fix in grant\_lowercase.test from [mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series).
      * [Revision #2502.565.26](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.26)\
        Mon 2013-01-21 10:52:39 +0100
        * [MDEV-4029](https://jira.mariadb.org/browse/MDEV-4029) SELECT on information\_schema using a subquery locks up the information\_schema table due to incorrect mutexes handling
        * Early evaluation of subqueries in the WHERE conditions on I\_S.\*\_STATUS tables, otherwise the subquery on this same table will try to acquire LOCK\_status twice.
    * [Revision #2502.566.35](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.35)\
      Sat 2013-01-19 23:40:53 -0800
      * Corrected the test case for bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938).
    * [Revision #2502.566.34](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.34)\
      Wed 2013-01-16 11:17:58 -0800
      * Corrected the fix for bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938).
    * [Revision #2502.566.33](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.33)\
      Tue 2013-01-15 16:46:27 -0800
      * Fixed bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938). The original patch with the implementation of virtual columns did not support INSERT DELAYED into tables with virtual columns. This patch fixes the problem.
  * [Revision #2502.567.60](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.60)\
    Wed 2013-01-16 21:07:26 +0200
    * [MDEV-4056](https://jira.mariadb.org/browse/MDEV-4056) fix.
    * The problem was that maybe\_null of Item\_row and its componetes was unsynced after update\_used\_tables() (and so pushed\_cond\_guards was not initialized but then requested).
    * Fix updates Item\_row::maybe\_null on update\_used\_tables().
  * [Revision #2502.567.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.59)\
    Thu 2013-01-17 16:08:05 +0200
    * [MDEV-3900](https://jira.mariadb.org/browse/MDEV-3900) Optimizer difference between MySQL and MariaDB with stored functions in WHERE clause of UPDATE or DELETE statements
    * Analysis The reason for the less efficient plan was result of a prior design decision - to limit the eveluation of constant expressions during optimization to only non-expensive ones. With this approach all stored procedures were considered expensive, and were not evaluated during optimization. As a result, SPs didn't participate in range optimization, which resulted in a plan with table scan rather than index range scan.
    * Solution Instead of considering all SPs expensive, consider expensive only those SPs that are non-deterministic. If an SP is deterministic, the optimizer will checj if it is constant, and may eventually evaluate it during optimization.
  * [Revision #2502.567.58](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.58)\
    Thu 2013-01-17 13:53:15 +0200
    * backport of: Don't reset maybe\_null in update\_used\_tables(); This breaks ROLLUP This fixed failing test in group\_by.test
  * [Revision #2502.567.57](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.57)\
    Wed 2013-01-16 15:11:13 +0200
    * [MDEV-3988](https://jira.mariadb.org/browse/MDEV-3988) fix.
    * Subquery turned into constant too late to be excluded from grouping list so test for constant added to the create\_temp\_table().
  * [Revision #2502.567.56](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.56)\
    Fri 2013-01-11 20:26:34 -0800
    * Fixed bug [MDEV-4025](https://jira.mariadb.org/browse/MDEV-4025). The bug could lead to a wrong estimate of the number of expected rows in the output of the EXPLAIN commands for queries with GROUP BY. This could be observed in the test case for LP bug 934348.
  * [Revision #2502.567.55](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.55)\
    Fri 2013-01-11 12:44:21 +0100
    * [MDEV-4020](https://jira.mariadb.org/browse/MDEV-4020) : Make sure strmov symbol is exported by client library on Linux (even if the server and libraries itself use stpcpy instead of it)
    * It is a workaround that allows myodbc built by certain distributions' (CentOS,Fedora) to peacefully coexist with mariadb client libraries. The problem is that MyODBC in these distros needs strmov() to be exported by mysql client shared library, or else myodbc fails to load.
* [Revision #3644](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3644)\
  Wed 2013-01-23 14:58:05 +0100
  * remove one particularly stupid test
* [Revision #3643](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3643)\
  Mon 2013-01-21 12:20:54 +0100
  * [MDEV-4069](https://jira.mariadb.org/browse/MDEV-4069) thd\_wait\_end does not called in some cases in buf\_page\_read\_low in XtraDB engine
* [Revision #3642](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3642)\
  Tue 2013-01-22 13:29:59 +0200
  * Fixed typo in the function name. test suite added.
* [Revision #3641](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3641)\
  Mon 2013-01-21 14:34:39 +0200
  * [MDEV-3873](https://jira.mariadb.org/browse/MDEV-3873): fixed functions absend in 5.3.
* [Revision #3640](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3640)\
  Sun 2013-01-20 21:43:11 +0100
  * fix a strict aliasing warning - remove a meaningless cast.
* [Revision #3639](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3639)\
  Sun 2013-01-20 21:42:01 +0100
  * [MDEV-3952](https://jira.mariadb.org/browse/MDEV-3952) Incompatible change in MariaDB-5.5.28a-client rpm adds mytop when not in MariaDB-5.5.23-client (CentOS 5)
  * Same as for deb: don't add mytop to the client rpm.
* [Revision #3638](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3638)\
  Sun 2013-01-20 14:06:33 +0100
  * [MDEV-3934](https://jira.mariadb.org/browse/MDEV-3934) Assertion \`((keypart\_map+1) & keypart\_map) == 0' failed in \_mi\_pack\_key with an index on a POINT column
  * sel\_arg\_range\_seq\_next(): set keypart map also for GEOM\_FLAG keys
* [Revision #3637](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3637)\
  Sun 2013-01-20 00:46:51 +0100
  * [MDEV-4029](https://jira.mariadb.org/browse/MDEV-4029) SELECT on information\_schema using a subquery locks up the information\_schema table due to incorrect mutexes handling
  * Early evaluation of subqueries in the WHERE conditions on I\_S.\*\_STATUS tables, otherwise the subquery on this same table will try to acquire LOCK\_status twice.
* [Revision #3636](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3636)\
  Sat 2013-01-19 14:03:33 +0100
  * [MDEV-3832](https://jira.mariadb.org/browse/MDEV-3832) MariaDB conflicts with packages filesystem-3.1-2.fc18.i686 and jre-1.7.0\_09-fcs.i586 on Fedora 18
  * fix the rpm packaging to work on Fedora18. Two problems: \* conflicts on common directories with other packages. \* more auto-generated requirements for mariadb-test.rpm
* [Revision #3635](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3635)\
  Fri 2013-01-18 19:10:20 +0100
  * [MDEV-633](https://jira.mariadb.org/browse/MDEV-633) [Bug #1024058](https://bugs.launchpad.net/bugs/1024058) - mysqld XA crash in replication slave
  * initialize cache\_mngr and write the Xid into binlog even if binlog is disabled with SQL\_LOG\_BIN=0 or no --log-slave-updates in the slave thread
* [Revision #3634](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3634)\
  Fri 2013-01-18 19:07:59 +0100
  * simplify THD::binlog\_setup\_trx\_data() usage
* [Revision #3633](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3633)\
  Fri 2013-01-18 19:04:51 +0100
  * [MDEV-3908](https://jira.mariadb.org/browse/MDEV-3908) crash in multi-table delete and mdl ([CVE-2012-5612](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5612))
  * Add a test case. The fix comes with MySQL bug#15948123: SERVER WORKS INCORRECT WITH LONG TABLE ALIASES
* [Revision #3632](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3632)\
  Fri 2013-01-18 19:04:23 +0100
  * [MDEV-4065](https://jira.mariadb.org/browse/MDEV-4065) thd\_kill\_statement service
* [Revision #3631](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3631)\
  Fri 2013-01-18 18:49:07 +0100
  * Fix Windows installers' bootstrapper scripts , after mysql\_performance\_tables.sql was split off mysql\_system\_tables.sql
* [Revision #3630](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3630)\
  Thu 2013-01-17 02:27:10 +0200
  * Don't reset maybe\_null in update\_used\_tables(); This breaks ROLLUP This fixed failing test in group\_by.test
* [Revision #3629](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3629)\
  Thu 2013-01-17 01:08:49 +0200
  * Fixed compiler warning
* [Revision #3628](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3628) \[merge]\
  Wed 2013-01-16 11:13:08 +0100
  * xtradb merge. Percona-Server-5.5.28-rel29.3
  * [Revision #0.12.59](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.59)\
    Tue 2013-01-15 22:22:49 +0100
    * Percona-Server-5.5.28-rel29.3
* [Revision #3627](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3627)\
  Tue 2013-01-15 19:16:29 +0100
  * Test case and a different fix for MySQL bug#14485479
* [Revision #3626](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3626)\
  Tue 2013-01-15 19:16:18 +0100
  * small cleanups
* [Revision #3625](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3625)\
  Tue 2013-01-15 19:15:51 +0100
  * backport a test case for a 5.5 bug fix from the 5.6 tree
* [Revision #3624](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3624) \[merge]\
  Tue 2013-01-15 19:13:32 +0100
  * mysql-5.5.29 merge
  * [Revision #3077.166.19](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.166.19) \[
    * merge]\
      Tue 2012-09-11 17:42:22 +0300
    * merge
  * [Revision #3077.166.18](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.166.18)\
    Mon 2012-08-27 15:30:58 +0300
    * Bug #13548161: MYSQLD\_SAFE IMPROVEMENTS FOR 5.5 ALLWAYS SETS PLUGIN\_DIR TO DEFAULT IGNOR
    * The test in mysqld\_safe for the presence of the --plugin-dir and assigning a default value to it were performed before the actual argument parsing. This is wrong, as PLUGIN\_DIR mysqld\_safe code also uses MY\_BASEDIR\_VERSION to look for version specific plugin directory if present. Fixed by moving the PLUGIN\_DIR logic after the parse\_arguments() call.
  * [Revision #3077.166.17](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3077.166.17)\
    Fri 2012-08-24 15:01:31 +0300
    * Bug #14181049: MYSQL\_INSTALL\_DB.PL CREATES EMPTY SYSTEM TABLES FOR MYSQL
    * The script is different from what's used on unixes. It was not playing the table insertion script (mysql\_system\_tables\_data.sql), although it was checking for the presence of this script. Fixed by re-enabling the lookup for this file and replaying it at bootstrap time. Note that on the Unixes "SELECT @@hostname" does return a fully qualified name, whereas on Windows it returns only a hostname. So by default we're filtering records in the mysql.user table until we ensure this is fixed.
* [Revision #3623](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3623)\
  Tue 2013-01-15 19:08:49 +0100
  * update debian patch to apply
* [Revision #3622](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3622) \[merge]\
  Tue 2013-01-15 19:07:46 +0100
  * 5.3 merge
  * [Revision #2502.567.54](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.54) \[merge]\
    Thu 2013-01-10 15:40:21 +0100
    * 5.2->5.3 merge
    * [Revision #2502.566.32](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.32) \[merge]\
      Thu 2013-01-10 13:54:04 +0100
      * 5.1 merge
      * [Revision #2502.565.25](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.25) \[merge]\
        Wed 2013-01-09 23:51:51 +0100
        * mysql-5.1.67 merge
      * [Revision #2502.565.24](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.24)\
        Tue 2012-12-04 17:08:02 +0100
        * proactive s/strmov/strnmov/ in sql\_acl.cc and related test cases
    * [Revision #2502.566.31](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.31) \[merge]\
      Fri 2012-12-21 15:19:08 +0100
      * merge
      * [Revision #2502.565.23](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.23)\
        Fri 2012-12-21 15:17:26 +0100
        * Support VS2012. Exclude compiler-defined symbols from being exported by mysqld.exe
    * [Revision #2502.566.30](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.30) \[merge]\
      Fri 2012-12-21 14:04:25 +0100
      * merge
      * [Revision #2502.565.22](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.22)\
        Thu 2012-12-06 00:37:06 +0100
        * [MDEV-3918](https://jira.mariadb.org/browse/MDEV-3918): myisamchk bogus error for files larger than 4GB.
        * The failure is caused by failing stat() call . C Runtime function stat() uses old struct with 32bit st\_size member, and since Visual Studio 2010 , it returns an error on st\_size overflow (i.e on files larger than 4GB)
        * Fix replaces stat() by my\_stat(), the later is backed by 64bit-able stat64().
    * [Revision #2502.566.29](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.29)\
      Tue 2012-12-11 09:50:48 +0100
      * one-byte overflow with old passwords
    * [Revision #2502.566.28](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.28)\
      Mon 2012-11-26 13:33:24 +0100
      * Fix broken feedback plugin after [MDEV-712](https://jira.mariadb.org/browse/MDEV-712).
      * Link feedback plugin with yassl libraries, if with-ssl=bundled is used, since mysqld does not export SSL symbols anymore.
    * [Revision #2502.566.27](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.27)\
      Fri 2012-11-23 13:50:46 +0100
      * [MDEV-712](https://jira.mariadb.org/browse/MDEV-712) - [Bug #1024239](https://bugs.launchpad.net/bugs/1024239) - Mysqlclient exports the same symbols as openssl
      * Compile yassl and taocrypt using -fvisibility=hidden, when possible. This prevent symbols from being exported.
    * [Revision #2502.566.26](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.566.26) \[merge]\
      Thu 2012-11-22 18:29:53 +0100
      * merge 5.1
      * [Revision #2502.565.21](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.565.21)\
        Thu 2012-11-22 18:27:02 +0100
        * Feedback plugin now recognizes Windows 8 / Windows Server 2012.
  * [Revision #2502.567.53](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.53)\
    Tue 2013-01-08 21:23:03 +0100
    * [MDEV-3942](https://jira.mariadb.org/browse/MDEV-3942) FROM\_DAYS() returns different result in MariaDB comparing to MySQL: NULL vs 0000-00-00
    * fixed a regression, introduced while fixing [MDEV-456](https://jira.mariadb.org/browse/MDEV-456)
  * [Revision #2502.567.52](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.52)\
    Fri 2012-12-28 14:41:46 +0200
    * [MDEV-3873](https://jira.mariadb.org/browse/MDEV-3873) & [MDEV-3876](https://jira.mariadb.org/browse/MDEV-3876) & [MDEV-3912](https://jira.mariadb.org/browse/MDEV-3912) : Wrong result (extra rows) with ALL subquery from a MERGE view.
    * The problem was in the lost ability to be null for the table of a left join if it is a view/derived table.
    * It hapenned because setup\_table\_map(), was called earlier then we merged the view or derived.
    * Fixed by propagating new maybe\_null flag during Item::update\_used\_tables().
    * Change in join\_outer.test and join\_outer\_jcl6.test appeared because IS NULL reported no used tables (i.e. constant) for argument which could not be NULL and new maybe\_null flag was propagated for IS NULL argument (Item\_field) because table the Item\_field belonged to changed its maybe\_null status.
  * [Revision #2502.567.51](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.51)\
    Wed 2012-12-19 15:56:57 +0200
    * [MDEV-3928](https://jira.mariadb.org/browse/MDEV-3928): Assertion \`example' failed in Item\_cache::is\_expensive\_processor with a 2-level IN subquery
    * Analysis: The following call stack shows that it is possible to set Item\_cache::value\_cached, and the relevant value without setting Item\_cache::example.
    * \#0 Item\_cache\_temporal::store\_packed at item.cc:8395 #1 get\_datetime\_value at item\_cmpfunc.cc:915 #2 resolve\_const\_item at item.cc:7987 #3 propagate\_cond\_constants at sql\_select.cc:12264 #4 propagate\_cond\_constants at sql\_select.cc:12227 #5 optimize\_cond at sql\_select.cc:13026 #6 JOIN::optimize at sql\_select.cc:1016 #7 st\_select\_lex::optimize\_unflattened\_subqueries at sql\_lex.cc:3161 #8 JOIN::optimize\_unflattened\_subqueries at opt\_subselect.cc:4880 #9 JOIN::optimize at sql\_select.cc:1554
    * The fix is to set Item\_cache\_temporal::example even when the value is set directly by Item\_cache\_temporal::store\_packed. This makes the Item\_cache\_temporal object consistent.
  * [Revision #2502.567.50](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.50)\
    Wed 2012-12-05 21:06:00 +0200
    * [MDEV-3914](https://jira.mariadb.org/browse/MDEV-3914) fix.
    * Fixed algorithm of detecting of first real table in view/subquery-in-the-FROM-clase.
  * [Revision #2502.567.49](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.49)\
    Fri 2012-11-23 13:11:31 +0100
    * bump the version to 5.3.11
  * [Revision #2502.567.48](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.48) \[merge]\
    Thu 2012-11-22 10:30:39 -0800
    * Merge
    * [Revision #2502.570.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.570.1)\
      Wed 2012-11-21 21:55:04 -0800
      * Fixed LP bug #1002146 (bug [MDEV-645](https://jira.mariadb.org/browse/MDEV-645)). If the setting of system variables does not allow to use join buffer for a join query with GROUP BY \<f1,...> / ORDER BY \<f1,...> then filesort is not needed if the first joined table is scanned in the order compatible with order specified by the list \<f1,...>.
* [Revision #3621](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3621)\
  Tue 2013-01-15 17:46:46 +0100
  * remove thd\_mark\_as\_hard\_kill() (because it's conceptually wrong. only the user can decide whether the kill is allowed to leave tables in the inconsistent state, storage engine has no say in that)
* [Revision #3620](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3620)\
  Tue 2013-01-15 14:33:08 +0200
  * Fix for bug [MDEV-3992](https://jira.mariadb.org/browse/MDEV-3992), second attempt
  * The previous fix for [MDEV-3992](https://jira.mariadb.org/browse/MDEV-3992) was incomplete, because it still computed incorrectly the number of keyparts of the extended secondary key in the case when columns of the PK participate in the secondary key.
  * This patch by Monty corrects the above problem.
* [Revision #3619](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3619)\
  Mon 2013-01-14 15:05:05 +0200
  * Fix for bug [MDEV-3992](https://jira.mariadb.org/browse/MDEV-3992)
  * Analysis: The crash is a result of incorrect analysis of whether a secondary key can be extended with a primary in order to compute ORDER BY. The analysis is done in test\_if\_order\_by\_key(). This function doesn't take into account that the primary key may in fact index the same columns as the secondary key. For the test query test\_if\_order\_by\_key says that there is an extended key with total 2 keyparts. At the same time, the condition if (pkinfo->key\_part\[i].field->key\_start.is\_set(nr)) in test\_if\_cheaper\_oredring() becomes true for (i == 0), which results in an invalid access to rec\_per\_key\[-1].
  * Solution: The best solution would be to reuse KEY::ext\_key\_parts that is already computed by open\_binary\_frm(), however after detailed analysis the conclusion is that the change would be too intrusive for a GA release. The solution for 5.5 is to add a guard for the case when the 0-th key part is considered, and to assume that all keys will be scanned in this case.
* [Revision #3618](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3618)\
  Fri 2013-01-11 02:03:43 +0200
  * Buildbot fixes and cleanups: - Added --verbose to BUILD scripts to get make to write out compile commands. - Detect if AM\_EXTRA\_MAKEFLAGS=VERBOSE=1 was used with build scripts. - Don't write warnings about replication variables when doing bootstrap. - Fixed that mysql\_cond\_wait() and mysql\_cond\_timedwait() will report original source file in case of errors. - Ignore some compiler warnings
* [Revision #3617](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3617)\
  Fri 2013-01-11 01:31:50 +0200
  * Fixed crashing bug in GROUP\_CONCAT with ROLLUP Fixed [MDEV-4002](https://jira.mariadb.org/browse/MDEV-4002): Server crash or valgrind errors in Item\_func\_group\_concat::setup and Item\_func\_group\_concat::add
* [Revision #3616](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3616)\
  Fri 2013-01-11 00:53:07 +0200
  * Fixed problem with failing mysql\_upgrade when proc table was not correct. Moved out creation of performance schema tables from mysql\_system\_tables.sql as the performance\_tables creation scripts needs a working mysql.proc to work.
* [Revision #3615](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3615)\
  Fri 2013-01-11 00:35:33 +0200
  * Fixed [MDEV-4013](https://jira.mariadb.org/browse/MDEV-4013): Password length in replication setup Give error for wrong parameters to CHANGE MASTER Extend MASTER\_PASSWORD and MASTER\_HOST lengths
* [Revision #3614](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3614)\
  Fri 2013-01-11 00:22:14 +0200
  * Fixed some race conditons and bugs related to killed queries KILL now breaks locks inside InnoDB Fixed possible deadlock when running INNODB STATUS Added ha\_kill\_query() and kill\_query() to send kill signal to all storage engines Added reset\_killed() to ensure we don't reset killed state while awake() is getting called
* [Revision #3613](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3613)\
  Thu 2013-01-10 23:40:18 +0200
  * Fix for [MDEV-4009](https://jira.mariadb.org/browse/MDEV-4009): main.delayed sporadically fails with "query 'REPLACE DELAYED t1 VALUES (5)' failed: 1317: Query execution was interrupted" - Fixed broadcast without a proper mutex - Don't break existing locks if we are just testing if we can get the lock
* [Revision #3612](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3612)\
  Wed 2013-01-09 17:30:20 +0100
  * [MDEV-3846](https://jira.mariadb.org/browse/MDEV-3846) REFRESH\_CHECKPOINT and REFRESH\_TABLE\_STATS tokens share the same value
* [Revision #3611](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3611)\
  Wed 2013-01-09 17:29:51 +0100
  * [MDEV-3985](https://jira.mariadb.org/browse/MDEV-3985) crash: uninstall soname 'a'
* [Revision #3610](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3610)\
  Tue 2013-01-08 21:23:40 +0100
  * [MDEV-3883](https://jira.mariadb.org/browse/MDEV-3883) Show global status not in order
* [Revision #3609](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3609)\
  Tue 2013-01-08 21:21:28 +0100
  * [MDEV-3987](https://jira.mariadb.org/browse/MDEV-3987) uninitialized read in Item\_cond::fix\_fields leads to crash: select .. where .. in ( select ... )
  * change Item\_func\_group\_concat to use max\_length according to the expected semantics
* [Revision #3608](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3608)\
  Mon 2013-01-07 20:21:05 +0100
  * non-functional cleanup, clarifying CONVERT\_IF\_BIGGER\_TO\_BLOB
* [Revision #3607](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3607)\
  Sat 2013-01-05 23:52:25 +0100
  * Remove timed mutexes in XtraDB - obsolete feature that does not link on Windows, if plugin is build dynamically It was already removed from innobase in the past.
* [Revision #3606](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3606)\
  Tue 2013-01-01 15:33:25 +0100
  * [MDEV-3993](https://jira.mariadb.org/browse/MDEV-3993) - add MSI installer option to set character-set-server=utf8
* [Revision #3605](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3605) \[merge]\
  Mon 2012-12-31 01:39:26 +0400
  * [MDEV-3990](https://jira.mariadb.org/browse/MDEV-3990): engine tests went out of sync with current MariaDB code Reasons: - as of 5.5.27, YEAR(2) is deprecated, hence the new warning; - [MDEV-553](https://jira.mariadb.org/browse/MDEV-553) - different error code/message on out-of-range autoincrement; - INSERT IGNORE now produces a warning if a duplicate was encountered
  * [Revision #3604.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3604.1.1)\
    Fri 2012-12-28 17:02:33 +0400
    * storage\_engine tests and upstream engines/\* suites went out of sync with current MariaDB code. Reasons: - as of 5.5.27, YEAR(2) is deprecated, hence the new warning; - [MDEV-553](https://jira.mariadb.org/browse/MDEV-553) - different error code/message on out-of-range autoincrement; - INSERT IGNORE now produces a warning if a duplicate was encountered (change pushed along with [MDEV-553](https://jira.mariadb.org/browse/MDEV-553))
* [Revision #3604](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3604)\
  Thu 2012-12-06 17:30:22 +0100
  * typo
* [Revision #3603](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3603)\
  Thu 2012-12-06 16:34:02 +0100
  * if the debian package name for 5.5.28 is 5.5.28-mariadb1wheezy then for 5.5.28a it should be 5.5.28a-mariadb1wheezy not 5.5.28-mariadb-a1wheezy
* [Revision #3602](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3602)\
  Fri 2012-12-21 11:18:29 +0200
  * [MDEV-3902](https://jira.mariadb.org/browse/MDEV-3902) Assertion \`record\_length == m\_record\_length' failed at Filesort\_buffer::alloc\_sort\_buffer
  * This bug is a duplicate of [MDEV-3899](https://jira.mariadb.org/browse/MDEV-3899) so adding a test case only.
* [Revision #3601](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3601)\
  Fri 2012-12-21 00:12:37 +0100
  * [MDEV-3945](https://jira.mariadb.org/browse/MDEV-3945) - do not hold LOCK\_thread\_count when freeing THD.
  * The patch decreases the duration of LOCK\_thread\_count, so it is not hold during THD destructor and freeing memory. This mutex now only protects the integrity of threads list, when removing THD from it, and thread\_count variable.
  * The add\_to\_status() function that updates global status during client disconnect, is now correctly protected by the LOCK\_status mutex.
  * Benchmark : in a "non-persistent" sysbench test (oltp\_ro with reconnect after each query), \~ 25% more connects/disconnects were measured
* [Revision #3600](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3600)\
  Thu 2012-12-20 22:38:40 +0200
  * [MDEV-3899](https://jira.mariadb.org/browse/MDEV-3899) Valgrind warnings (blocks are definitely lost) in filesort on IN subquery with SUM and DISTINCT
  * Analysys: In the beginning of JOIN::cleanup there is code that is supposed to free all filesort buffers. The code assumes that the table being sorted is the first non-constant table. To get this table it calls: first\_top\_level\_tab(this, WITHOUT\_CONST\_TABLES)
  * However, first\_top\_level\_tab() instead returned the wrong table - the first one in the plan, instead of the first non-constant table. There is no other place outside filesort() where sort buffers may be freed. As a result, the sort buffer was not freed, and there was a memory leak.
  * Solution: Change first\_top\_level\_tab(), to test for WITH\_CONST\_TABLES instead of WITHOUT\_CONST\_TABLES.
* [Revision #3599](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3599)\
  Wed 2012-12-19 21:58:05 +0200
  * Fixed some compiler warnings
* [Revision #3598](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3598)\
  Tue 2012-12-18 12:44:15 +0200
  * [MDEV-3818](https://jira.mariadb.org/browse/MDEV-3818): Query against view over IS tables worse than equivalent query without view
  * Fixed the test to be lower-case because it fails on windows with mixed case.
* [Revision #3597](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3597)\
  Mon 2012-12-17 22:34:56 +0200
  * Fixed the CREATE TABLE IF EXIST generates warnings instead of errors
* [Revision #3596](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3596)\
  Mon 2012-12-17 15:23:58 +0200
  * [MDEV-3818](https://jira.mariadb.org/browse/MDEV-3818): Query against view over IS tables worse than equivalent query without view
  * Analysis: The reason for the suboptimal plan when querying IS tables through a view was that the view columns that participate in an equality are wrapped by an Item\_direct\_view\_ref and were not recognized as being direct column references.
  * Solution: Use the original Item\_field objects via the real\_item() method.
* [Revision #3595](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3595)\
  Sun 2012-12-16 20:51:48 +0200
  * Remember original table row pack type for ALTER TABLE if table is not copied.
* [Revision #3594](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3594)\
  Sun 2012-12-16 20:49:57 +0200
  * Removed lock wait timeout warning when using CREATE TABLE IF EXISTS
* [Revision #3593](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3593)\
  Sun 2012-12-16 16:13:17 +0200
  * Implemented [MDEV-3941](https://jira.mariadb.org/browse/MDEV-3941): CREATE TABLE xxx IF NOT EXISTS should not block if table exists. - Added option to check\_if\_table\_exists() to quickly check if table exists (either SHARE or .FRM) - Extended lock\_table\_names() to not wait for meta data locks if CREATE IF NOT EXISTS is used.
* [Revision #3592](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3592) \[merge]\
  Sun 2012-12-16 12:04:26 +0200
  * Automatic merge
  * [Revision #3544.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3544.1.1)\
    Fri 2012-12-14 20:21:50 +0200
    * Removed extra '+' from some lines (remains of old merge)
* [Revision #3591](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3591)\
  Mon 2012-11-26 21:22:44 +0200
  * Fix of [MDEV-3874](https://jira.mariadb.org/browse/MDEV-3874): Server crashes in Item\_field::print on a SELECT from a MERGE view with materialization+semijoin, subquery, ORDER BY.
  * The problem was that in debugging binaries it try to print item to assign human readable name to the item. But subquery item was already freed (join\_free/cleanup with full cleanup) so Item\_field refers to temporary table which memory had been already freed.
* [Revision #3590](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3590)\
  Tue 2012-12-04 16:06:07 -0800
  * Fixed bug [MDEV-3888](https://jira.mariadb.org/browse/MDEV-3888). When inserting a record with update on duplicate keys the server calls the ha\_index\_read\_idx\_map handler function to look for the record that violates unique key constraints. The third parameter of this call should mark only the base components of the index where the server is searched for the record. Possible hidden components of the primary key are to be unmarked.
* [Revision #3589](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3589)\
  Sat 2012-12-01 18:01:59 +0100
  * fix openssl\_1 test
* [Revision #3588](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/3588)\
  Sat 2012-12-01 16:33:22 +0100
  * [MDEV-3901](https://jira.mariadb.org/browse/MDEV-3901): Wrong SSL error messages
  * Fixed typo (missing comma)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
