# MariaDB 5.3.12 Changelog

[Download](https://downloads.mariadb.org/mariadb/5.3.12) | [Release Notes](../../old-releases/5.3/5.3.12.md) | **Changelog** |[Overview of 5.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)

**Release date:** 30 Jan 2013

For the highlights of this release, see the [release notes](../../old-releases/5.3/5.3.12.md).

The revision number links will take you to the revision's page on Launchpad. On Launchpad you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3621](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3621) \[merge]\
  Mon 2013-01-28 09:12:23 +0100
  * 5.2 merge
  * [Revision #2732.57.52](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.52)\
    Mon 2013-01-28 09:10:01 +0100
    * compilation error with -Wuninitialized -Werror
  * [Revision #2732.57.51](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.51) \[merge]\
    Fri 2013-01-25 17:22:21 +0100
    * 5.1 merge
    * [Revision #2643.153.38](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.38)\
      Fri 2013-01-25 14:29:46 +0100
      * [MDEV-729](https://jira.mariadb.org/browse/MDEV-729) [Bug #998028](https://bugs.launchpad.net/bugs/998028) - Server crashes on normal shutdown in closefrm after executing a query from MyISAM table
      * don't write a key value into the record buffer - a key length can be larger then the record length.
    * [Revision #2643.153.37](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.37)\
      Fri 2013-01-25 12:26:35 +0100
      * [MDEV-759](https://jira.mariadb.org/browse/MDEV-759) [Bug #998340](https://bugs.launchpad.net/bugs/998340) - Valgrind complains on simple selects containing expression DAY(FROM\_UNIXTIME(-1))
      * check item->null\_value before using the result of item->val\_int()
* [Revision #3620](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3620)\
  Sat 2013-01-26 22:33:18 +0100
  * [MDEV-3875](https://jira.mariadb.org/browse/MDEV-3875) Wrong result (missing row) on a DISTINCT query with the same subquery in the SELECT list and GROUP BY
  * fix remove\_dup\_with\_hash\_index() and remove\_dup\_with\_compare() to take NULLs into account
* [Revision #3619](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3619)\
  Fri 2013-01-25 16:56:57 +0200
  * The problem was that expression with field after transformation (on the first execution) reached by fix\_fields() (via reference) before row which it belongs to (on the second execution) and fix\_field for row did not follow usual protocol for Items with argument (first check that the item fixed then call fix\_fields).
  * Item\_row::fix\_field fixed.
* [Revision #3618](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3618) \[merge]\
  Fri 2013-01-25 10:20:45 +0100
  * 5.2 merge
  * [Revision #2732.57.50](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.50)\
    Fri 2013-01-25 10:19:35 +0100
    * [MDEV-4040](https://jira.mariadb.org/browse/MDEV-4040) Replace deprecated SET OPTION syntax in mysqldump
    * mysqldump.c: s/SET OPTION/SET/ (OPTION was, hm, optional since 3.21, so there's no need to use SET OPTION even in the old compatibility modes)
  * [Revision #2732.57.49](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.49)\
    Fri 2013-01-25 09:41:26 +0100
    * [MDEV-3909](https://jira.mariadb.org/browse/MDEV-3909) remote user enumeration ([CVE-2012-5615](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5615))
    * instead of returning Access denied on the incorrect user name, emulate the complete failed logic procedure, possibly with the change plugin packet.
  * [Revision #2732.57.48](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.48)\
    Fri 2013-01-25 00:20:53 +0100
    * report "using password: YES/NO" correctly for the COM\_CHANGE\_USER failures
  * [Revision #2732.57.47](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.47)\
    Fri 2013-01-25 00:17:39 +0100
    * [MDEV-3915](https://jira.mariadb.org/browse/MDEV-3915) COM\_CHANGE\_USER allows fast password brute-forcing ([CVE-2012-5627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5627))
    * allow only three failed change\_user per connection. successful change\_user do NOT reset the counter
* [Revision #3617](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3617) \[merge]\
  Mon 2013-01-21 21:29:19 -0800
  * Merge 5.2->5.3
  * [Revision #2732.57.46](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.46) \[merge]\
    Mon 2013-01-21 15:23:40 -0800
    * Merge 5.1->5.2
    * [Revision #2643.153.36](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.36) \[merge]\
      Mon 2013-01-21 13:48:34 -0800
      * Merge.
      * [Revision #2643.155.1](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.155.1)\
        Mon 2013-01-21 11:47:45 -0800
        * Fixed bug [MDEV-4063](https://jira.mariadb.org/browse/MDEV-4063) (bug #56927). This bug could result in returning 0 for the expressions of the form \<aggregate\_function>(distinct field) when the system variable max\_heap\_table\_size was set to a small enough number. It happened because the method Unique::walk() did not support the case when more than one pass was needed to merge the trees of distinct values saved in an external file.
        * Backported a fix in grant\_lowercase.test from [mariadb 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-55-series).
    * [Revision #2643.153.35](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.35)\
      Mon 2013-01-21 10:52:39 +0100
      * [MDEV-4029](https://jira.mariadb.org/browse/MDEV-4029) SELECT on information\_schema using a subquery locks up the information\_schema table due to incorrect mutexes handling
      * Early evaluation of subqueries in the WHERE conditions on I\_S.\*\_STATUS tables, otherwise the subquery on this same table will try to acquire LOCK\_status twice.
  * [Revision #2732.57.45](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.45)\
    Sat 2013-01-19 23:40:53 -0800
    * Corrected the test case for bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938).
  * [Revision #2732.57.44](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.44)\
    Wed 2013-01-16 11:17:58 -0800
    * Corrected the fix for bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938).
  * [Revision #2732.57.43](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.43)\
    Tue 2013-01-15 16:46:27 -0800
    * Fixed bug [MDEV-3938](https://jira.mariadb.org/browse/MDEV-3938). The original patch with the implementation of virtual columns did not support INSERT DELAYED into tables with virtual columns. This patch fixes the problem.
* [Revision #3616](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3616)\
  Wed 2013-01-16 21:07:26 +0200
  * [MDEV-4056](https://jira.mariadb.org/browse/MDEV-4056) fix.
  * The problem was that maybe\_null of Item\_row and its componetes was unsynced after update\_used\_tables() (and so pushed\_cond\_guards was not initialized but then requested).
  * Fix updates Item\_row::maybe\_null on update\_used\_tables().
* [Revision #3615](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3615)\
  Thu 2013-01-17 16:08:05 +0200
  * [MDEV-3900](https://jira.mariadb.org/browse/MDEV-3900) Optimizer difference between MySQL and MariaDB with stored functions in WHERE clause of UPDATE or DELETE statements
  * Analysis The reason for the less efficient plan was result of a prior design decision - to limit the eveluation of constant expressions during optimization to only non-expensive ones. With this approach all stored procedures were considered expensive, and were not evaluated during optimization. As a result, SPs didn't participate in range optimization, which resulted in a plan with table scan rather than index range scan.
  * Solution Instead of considering all SPs expensive, consider expensive only those SPs that are non-deterministic. If an SP is deterministic, the optimizer will checj if it is constant, and may eventually evaluate it during optimization.
* [Revision #3614](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3614)\
  Thu 2013-01-17 13:53:15 +0200
  * backport of: Don't reset maybe\_null in update\_used\_tables(); This breaks ROLLUP This fixed failing test in group\_by.test
* [Revision #3613](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3613)\
  Wed 2013-01-16 15:11:13 +0200
  * [MDEV-3988](https://jira.mariadb.org/browse/MDEV-3988) fix.
  * Subquery turned into constant too late to be excluded from grouping list so test for constant added to the create\_temp\_table().
* [Revision #3612](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3612)\
  Fri 2013-01-11 20:26:34 -0800
  * Fixed bug [MDEV-4025](https://jira.mariadb.org/browse/MDEV-4025). The bug could lead to a wrong estimate of the number of expected rows in the output of the EXPLAIN commands for queries with GROUP BY. This could be observed in the test case for LP bug 934348.
* [Revision #3611](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3611)\
  Fri 2013-01-11 12:44:21 +0100
  * [MDEV-4020](https://jira.mariadb.org/browse/MDEV-4020) : Make sure strmov symbol is exported by client library on Linux (even if the server and libraries itself use stpcpy instead of it)
  * It is a workaround that allows myodbc built by certain distributions' (CentOS,Fedora) to peacefully coexist with mariadb client libraries. The problem is that MyODBC in these distros needs strmov() to be exported by mysql client shared library, or else myodbc fails to load.
* [Revision #3610](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3610) \[merge]\
  Thu 2013-01-10 15:40:21 +0100
  * 5.2->5.3 merge
  * [Revision #2732.57.42](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.42) \[merge]\
    Thu 2013-01-10 13:54:04 +0100
    * 5.1 merge
    * [Revision #2643.153.34](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.34) \[merge]\
      Wed 2013-01-09 23:51:51 +0100
      * mysql-5.1.67 merge
    * [Revision #2643.153.33](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.33)\
      Tue 2012-12-04 17:08:02 +0100
      * proactive s/strmov/strnmov/ in sql\_acl.cc and related test cases
  * [Revision #2732.57.41](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.41) \[merge]\
    Fri 2012-12-21 15:19:08 +0100
    * merge
    * [Revision #2643.153.32](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.32)\
      Fri 2012-12-21 15:17:26 +0100
      * Support VS2012. Exclude compiler-defined symbols from being exported by mysqld.exe
  * [Revision #2732.57.40](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.40) \[merge]\
    Fri 2012-12-21 14:04:25 +0100
    * merge
    * [Revision #2643.153.31](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.31)\
      Thu 2012-12-06 00:37:06 +0100
      * [MDEV-3918](https://jira.mariadb.org/browse/MDEV-3918): myisamchk bogus error for files larger than 4GB.
      * The failure is caused by failing stat() call . C Runtime function stat() uses old struct with 32bit st\_size member, and since Visual Studio 2010 , it returns an error on st\_size overflow (i.e on files larger than 4GB)
      * Fix replaces stat() by my\_stat(), the later is backed by 64bit-able stat64().
  * [Revision #2732.57.39](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.39)\
    Tue 2012-12-11 09:50:48 +0100
    * one-byte overflow with old passwords
  * [Revision #2732.57.38](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.38)\
    Mon 2012-11-26 13:33:24 +0100
    * Fix broken feedback plugin after [MDEV-712](https://jira.mariadb.org/browse/MDEV-712).
    * Link feedback plugin with yassl libraries, if with-ssl=bundled is used, since mysqld does not export SSL symbols anymore.
  * [Revision #2732.57.37](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.37)\
    Fri 2012-11-23 13:50:46 +0100
    * [MDEV-712](https://jira.mariadb.org/browse/MDEV-712) - [Bug #1024239](https://bugs.launchpad.net/bugs/1024239) - Mysqlclient exports the same symbols as openssl
    * Compile yassl and taocrypt using -fvisibility=hidden, when possible. This prevent symbols from being exported.
  * [Revision #2732.57.36](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2732.57.36) \[merge]\
    Thu 2012-11-22 18:29:53 +0100
    * merge 5.1
    * [Revision #2643.153.30](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/2643.153.30)\
      Thu 2012-11-22 18:27:02 +0100
      * Feedback plugin now recognizes Windows 8 / Windows Server 2012.
* [Revision #3609](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3609)\
  Tue 2013-01-08 21:23:03 +0100
  * [MDEV-3942](https://jira.mariadb.org/browse/MDEV-3942) FROM\_DAYS() returns different result in MariaDB comparing to MySQL: NULL vs 0000-00-00
  * fixed a regression, introduced while fixing [MDEV-456](https://jira.mariadb.org/browse/MDEV-456)
* [Revision #3608](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3608)\
  Fri 2012-12-28 14:41:46 +0200
  * [MDEV-3873](https://jira.mariadb.org/browse/MDEV-3873) & [MDEV-3876](https://jira.mariadb.org/browse/MDEV-3876) & [MDEV-3912](https://jira.mariadb.org/browse/MDEV-3912) : Wrong result (extra rows) with ALL subquery from a MERGE view.
  * The problem was in the lost ability to be null for the table of a left join if it is a view/derived table.
  * It hapenned because setup\_table\_map(), was called earlier then we merged the view or derived.
  * Fixed by propagating new maybe\_null flag during Item::update\_used\_tables().
  * Change in join\_outer.test and join\_outer\_jcl6.test appeared because IS NULL reported no used tables (i.e. constant) for argument which could not be NULL and new maybe\_null flag was propagated for IS NULL argument (Item\_field) because table the Item\_field belonged to changed its maybe\_null status.
* [Revision #3607](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3607)\
  Wed 2012-12-19 15:56:57 +0200
  * [MDEV-3928](https://jira.mariadb.org/browse/MDEV-3928): Assertion \`example' failed in Item\_cache::is\_expensive\_processor with a 2-level IN subquery
  * Analysis: The following call stack shows that it is possible to set Item\_cache::value\_cached, and the relevant value without setting Item\_cache::example.
  * \#0 Item\_cache\_temporal::store\_packed at item.cc:8395 #1 get\_datetime\_value at item\_cmpfunc.cc:915 #2 resolve\_const\_item at item.cc:7987 #3 propagate\_cond\_constants at sql\_select.cc:12264 #4 propagate\_cond\_constants at sql\_select.cc:12227 #5 optimize\_cond at sql\_select.cc:13026 #6 JOIN::optimize at sql\_select.cc:1016 #7 st\_select\_lex::optimize\_unflattened\_subqueries at sql\_lex.cc:3161 #8 JOIN::optimize\_unflattened\_subqueries at opt\_subselect.cc:4880 #9 JOIN::optimize at sql\_select.cc:1554
  * The fix is to set Item\_cache\_temporal::example even when the value is set directly by Item\_cache\_temporal::store\_packed. This makes the Item\_cache\_temporal object consistent.
* [Revision #3606](https://bazaar.launchpad.net/~maria-captains/maria/5.3/revision/3606)\
  Wed 2012-12-05 21:06:00 +0200
  * [MDEV-3914](https://jira.mariadb.org/browse/MDEV-3914) fix.
  * Fixed algorithm of detecting of first real table in view/subquery-in-the-FROM-clase.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
