# MariaDB 10.0.12 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.12)[Release Notes](../../old-releases/10.0/10.0.12.md)[Changelog](mariadb-10012-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 16 Jun 2014

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.12.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4252](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4252)\
  Thu 2014-06-12 10:57:03 +0200
  * valgrind warning. initialize found\_rows earlier, before any "goto err".
* [Revision #4251](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4251)\
  Wed 2014-06-11 19:08:06 +0200
  * avoid uppercase table aliases tests - they're not portable
* [Revision #4250](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4250)\
  Wed 2014-06-11 16:03:10 +0500
  * [MDEV-5995](https://jira.mariadb.org/browse/MDEV-5995) MySQL Bug#12750920: EMBEDDED SERVER START/STOP. Some variables weren't cleared properly so consequitive embedded server start/stop failed. Cleanups added. Also mysql\_client\_test.c extended to test that (taken from Mattias Johnson's patch)
* [Revision #4249](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4249)\
  Wed 2014-06-11 10:09:29 +0200
  * [MDEV-6253](https://jira.mariadb.org/browse/MDEV-6253) MySQL Users Break when Migrating from MySQL 5.1 to [MariaDB 10.0.10](../../old-releases/10.0/10.0.10.md)
* [Revision #4248](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4248)\
  Wed 2014-06-11 10:09:24 +0200
  * [MDEV-6065](https://jira.mariadb.org/browse/MDEV-6065) MySQL Bug#13623473 "MISSING ROWS ON SELECT AND JOIN WITH TIME/DATETIME COMPARE
* [Revision #4247](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4247)\
  Wed 2014-06-11 10:08:08 +0200
  * [MDEV-6065](https://jira.mariadb.org/browse/MDEV-6065) MySQL Bug#13623473 "MISSING ROWS ON SELECT AND JOIN WITH TIME/DATETIME COMPARE"
* [Revision #4246](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4246)\
  Mon 2014-06-09 20:18:53 +0200
  * cleanup: remove special case from store\_key::store\_key(), add Field\_blob::new\_key\_field
* [Revision #4245](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4245)\
  Mon 2014-06-09 20:00:23 +0200
  * [MDEV-6249](https://jira.mariadb.org/browse/MDEV-6249) mark P\_S STABLE and disable it by default
* [Revision #4244](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4244) \[merge]\
  Tue 2014-06-10 15:32:56 -0700
  * Merge
  * [Revision #4242.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4242.1.1) \[merge]\
    Tue 2014-06-10 12:45:20 -0700
    * Merge.
    * [Revision #4233.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4233.1.1)\
      Tue 2014-06-10 10:34:58 -0700
      * Fixed bug [MDEV-6071](https://jira.mariadb.org/browse/MDEV-6071). The method JOIN\_CACHE::init may fail (return 1) if some conditions on the used join buffer is not satisfied. For example it fails if join\_buffer\_size is greater than join\_buffer\_space\_limit. The conditions should be checked when running the EXPLAIN command for the query. That's why the method JOIN\_CACHE::init has to be called for EXPLAIN commands as well.
* [Revision #4243](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4243) \[merge]\
  Tue 2014-06-10 21:51:02 +0200
  * Merge
  * [Revision #4241.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4241.1.1) \[merge]\
    Tue 2014-06-10 21:46:27 +0200
    * Merge
    * [Revision #4235.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4235.1.1)\
      Tue 2014-06-10 12:25:16 +0200
      * [MDEV-5985](https://jira.mariadb.org/browse/MDEV-5985): EITS: selectivity estimates look illogical for join and non-key equalities Part#1.
* [Revision #4242](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4242)\
  Tue 2014-06-10 17:02:46 +0500
  * [MDEV-4440](https://jira.mariadb.org/browse/MDEV-4440) IF NOT EXISTS in multi-action ALTER does not work when the problem is created by a previous part of the ALTER. Loops added to the handle\_if\_exists\_option() to check the CREATE/DROP lists for duplicates.
* [Revision #4241](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4241) \[merge]\
  Mon 2014-06-09 22:11:24 +0400
  * Merge spider fixes.
  * [Revision #4236.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4236.1.2)\
    Tue 2014-06-10 02:50:33 +0900
    * fix wrong result for Spider test
  * [Revision #4236.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4236.1.1)\
    Tue 2014-06-10 02:25:58 +0900
    * fix for Spider build error by abort\_loop on windows
* [Revision #4240](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4240) \[merge]\
  Mon 2014-06-09 18:00:53 +0200
  * 10.0-connect
  * [Revision #4155.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.10)\
    Fri 2014-05-30 14:53:15 +0200\
    \*
    * Eliminate virtual columns from CSV and FMT table fields modified: storage/connect/colblk.h storage/connect/reldef.h storage/connect/tabfmt.cpp
  * [Revision #4155.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.9)\
    Tue 2014-05-27 12:50:52 +0200\
    \*
    * Fix a bug causing the tabname option to be ignored when the connection string was not an URL but a server name. Also make the dbname option to be recignized in create (was only seached in option\_list) modified: storage/connect/ha\_connect.cc storage/connect/tabmysql.cpp
  * [Revision #4155.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.8)\
    Mon 2014-05-12 23:42:17 +0200\
    \*
    * Fix writing header of void CONNECT DBF tables on first insert. An error occured when the table definition had a special column that was not skipped from the header. modified: storage/connect/filamdbf.cpp
  * [Revision #4155.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4155.1.7)\
    Fri 2014-05-09 12:35:19 +0200\
    \*
    * Fix wrong error "Invalid offset for CVS table" when a special column is defined in a CSV table ([MDEV-6187](https://jira.mariadb.org/browse/MDEV-6187)) modified: storage/connect/ha\_connect.cc storage/connect/reldef.h storage/connect/tabfmt.cpp
* [Revision #4239](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4239)\
  Mon 2014-06-09 16:36:27 +0200
  * [MDEV-6320](https://jira.mariadb.org/browse/MDEV-6320) - disable spider.spider\_fixes
* [Revision #4238](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4238)\
  Mon 2014-06-09 14:22:43 +0200
  * bzr ignore 'pcre/test\*grep'
* [Revision #4237](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4237) \[merge]\
  Mon 2014-06-09 13:47:20 +0300
  * merge of [MDEV-6047](https://jira.mariadb.org/browse/MDEV-6047)
  * [Revision #4218.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4218.1.1)\
    Mon 2014-06-09 13:42:21 +0300
    * [MDEV-6047](https://jira.mariadb.org/browse/MDEV-6047): Make exists\_to\_in optimization ON by default
* [Revision #4236](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4236)\
  Sun 2014-06-08 19:52:11 +0900
  * merge Spider 3.2.4
* [Revision #4235](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4235) \[merge]\
  Sat 2014-06-07 23:45:05 +0200
  * Merge
  * [Revision #4221.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4221.1.1)\
    Sat 2014-06-07 19:00:26 +0200
    * [MDEV-6308](https://jira.mariadb.org/browse/MDEV-6308): Server crashes in table\_multi\_eq\_cond\_selectivity with ... - In table\_cond\_selectivity(), reset keyuse variable between the loops.
* [Revision #4234](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4234)\
  Fri 2014-06-06 21:28:42 +0400
  * [MDEV-5976](https://jira.mariadb.org/browse/MDEV-5976): TokuDB: Wrong query result using mrr=on - Key\_value\_records\_iterator::get\_next() should pass pointer to the key to handler->ha\_index\_next\_same(). Because of a typo bug, pointer-to-pointer was passed instead in certain cases.
* [Revision #4233](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4233)\
  Fri 2014-06-06 10:29:52 +0400
  * [MDEV-6102](https://jira.mariadb.org/browse/MDEV-6102) Comparison between TIME and DATETIME does not use CURRENT\_DATE [MDEV-6101](https://jira.mariadb.org/browse/MDEV-6101) Hybrid functions do not add CURRENT\_DATE when converting TIME to DATETIME
* [Revision #4232](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4232)\
  Fri 2014-06-06 00:09:17 +0200
  * revert tokudb changes that caused crashes
* [Revision #4231](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4231) \[merge]\
  Fri 2014-06-06 00:07:27 +0200
  * [MariaDB 5.5.38](../../old-releases/5.5/5.5.38.md) merge
* [Revision #4230](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4230) \[merge]\
  Thu 2014-06-05 16:05:08 +0200
  * pcre-8.35
  * [Revision #0.66.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.66.2)\
    Thu 2014-06-05 13:44:44 +0200
    * pcre-8.35.tar.bz2
* [Revision #4229](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4229)\
  Thu 2014-06-05 16:01:27 +0200
  * remove and ignore generated pcre files
* [Revision #4228](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4228) \[merge]\
  Thu 2014-06-05 16:00:49 +0200
  * pcre-8.34 mergetree initial merge
  * [Revision #0.66.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.66.1)\
    Thu 2014-06-05 12:47:55 +0200
    * pcre-8.34
* [Revision #4227](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4227)\
  Thu 2014-06-05 15:59:46 +0200
  * [MDEV-6221](https://jira.mariadb.org/browse/MDEV-6221) SQL\_CALC\_FOUND\_ROWS yields wrong result again
* [Revision #4226](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4226)\
  Thu 2014-06-05 15:59:41 +0200
  * revert the fix for [MDEV-5898](https://jira.mariadb.org/browse/MDEV-5898), restore the fix for [MDEV-5549](https://jira.mariadb.org/browse/MDEV-5549). simplify test case for [MDEV-5898](https://jira.mariadb.org/browse/MDEV-5898)
* [Revision #4225](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4225)\
  Thu 2014-06-05 15:59:35 +0200
  * [MDEV-5998](https://jira.mariadb.org/browse/MDEV-5998) MySQL Bug#11756966 - 48958: STORED PROCEDURES CAN BE LEVERAGED TO BYPASS DATABASE SECURITY
* [Revision #4224](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4224)\
  Thu 2014-06-05 15:59:25 +0200
  * [MDEV-6149](https://jira.mariadb.org/browse/MDEV-6149) Include file pcre.h missing in binary dist, meaing I\_S plugins can't be built
* [Revision #4223](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4223)\
  Thu 2014-06-05 09:04:43 +0200
  * [MDEV-6243](https://jira.mariadb.org/browse/MDEV-6243) mysql\_install\_db or mysql\_upgrade fails when default\_engine=archive
* [Revision #4222](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4222)\
  Thu 2014-06-05 09:03:55 +0200
  * [MDEV-6258](https://jira.mariadb.org/browse/MDEV-6258) [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) performance schema timestamps relative to epoch
* [Revision #4221](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4221)\
  Wed 2014-06-04 13:23:00 +0300
  * Fixed compiler warnings
* [Revision #4220](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4220)\
  Wed 2014-06-04 13:03:55 +0300
  * [MDEV-6046](https://jira.mariadb.org/browse/MDEV-6046): MySQL Bug#11766684 59851: UNINITIALISED VALUE IN ITEM\_FUNC\_LIKE::SELECT\_OPTIMIZE WITH SUBQUERY AND
* [Revision #4219](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4219)\
  Wed 2014-06-04 09:14:38 +0200
  * fix the code to compile without P\_S
* [Revision #4218](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4218)\
  Tue 2014-06-03 16:57:29 +0400
  * [MDEV-6103](https://jira.mariadb.org/browse/MDEV-6103) - Adding/removing non-materialized virtual column triggers table recreation
* [Revision #4217](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4217)\
  Wed 2014-06-04 00:26:27 +0400
  * [MDEV-5884](https://jira.mariadb.org/browse/MDEV-5884): EXPLAIN UPDATE ... ORDER BY LIMIT shows wrong #rows - Make get\_index\_for\_order() return correct #rows. changed EXPLAIN outputs are checked - only #rows is different.
* [Revision #4216](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4216)\
  Mon 2014-06-02 13:33:41 +0200
  * [MDEV-6280](https://jira.mariadb.org/browse/MDEV-6280) can't skip test with slash in its name
* [Revision #4215](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4215)\
  Mon 2014-06-02 12:33:17 +0400
  * [MDEV-6287](https://jira.mariadb.org/browse/MDEV-6287) Bad warning level when inserting a DATETIME value into a TIME column
* [Revision #4214](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4214)\
  Fri 2014-05-30 16:19:00 +0400
  * [MDEV-4051](https://jira.mariadb.org/browse/MDEV-4051) INET6\_ATON() and INET6\_NTOA()
* [Revision #4213](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4213)\
  Fri 2014-05-30 15:24:25 +0400
  * Moving implementation of INET\_ATON() INET\_NTOA() into separate files item\_inetfunc.h and item\_inetfunc.cc.
* [Revision #4212](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4212)\
  Mon 2014-05-26 22:41:35 +0400
  * Increase version number
* [Revision #4211](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4211)\
  Mon 2014-05-26 13:31:11 +0200
  * typo fixed (compilation failure with libwrap)
* [Revision #4210](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4210)\
  Tue 2014-05-13 11:53:30 +0200
  * [MDEV-6153](https://jira.mariadb.org/browse/MDEV-6153) Trivial Lintian errors in MariaDB sources: spelling errors and wrong executable bits

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
