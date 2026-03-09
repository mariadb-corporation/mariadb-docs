# MariaDB 5.5.65 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.65/)[Release Notes](../../old-releases/5.5/5.5.65.md)[Changelog](mariadb-5565-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 31 Jul 2019

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.65.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* [Revision #cc37250a76](https://github.com/MariaDB/server/commit/cc37250a76)\
  2019-07-25 16:36:32 +0200
  * Backslash added to wrong cachacters of names of client plugin.
* [Revision #2536c0b1eb](https://github.com/MariaDB/server/commit/2536c0b1eb)\
  2019-04-17 15:36:29 +0530
  * BUG#28642318: POINT IN TIME RECOVERY USING MYSQLBINLOG BROKEN WITH TEMPORARY TABLE -> ERRORS
* [Revision #7473a71a28](https://github.com/MariaDB/server/commit/7473a71a28)\
  2019-05-20 10:53:00 +0400
  * Bug #29419820: MEMORY LEAK IN MY\_YYOVERFLOW()
* [Revision #8ddb7e3eb7](https://github.com/MariaDB/server/commit/8ddb7e3eb7)\
  2019-07-24 13:14:03 +0200
  * Bug#27167197 USING ? IN INSTALL PLUGIN QUERY ABORTS DEBUG, AND HANGS OPTIMIZED SERVER
* [Revision #5e8ab9b7af](https://github.com/MariaDB/server/commit/5e8ab9b7af)\
  2019-04-16 09:33:02 +0530
  * Bug#27302459: EMPTY VALUE IN MYSQL.PLUGIN TABLE CAUSES SERVER TO EXIT ON STARTUP
* [Revision #c5e9674300](https://github.com/MariaDB/server/commit/c5e9674300)\
  2019-03-07 14:08:19 +0100
  * Bug #27312862: ASAN: HEAP-USE-AFTER-FREE: UPDATEXML RB#21666 RB#21666
* [Revision #9c6777c03c](https://github.com/MariaDB/server/commit/9c6777c03c)\
  2019-02-28 09:29:45 +0530
  * Bug#27259654 - ISSUES FOUND BY PVS-STUDIO STATIC ANALYZER
* [Revision #9d93f9dac4](https://github.com/MariaDB/server/commit/9d93f9dac4)\
  2019-07-23 15:00:53 +0300
  * [MDEV-8827](https://jira.mariadb.org/browse/MDEV-8827): Fix the 32-bit build
* [Revision #739f5239f1](https://github.com/MariaDB/server/commit/739f5239f1)\
  2019-05-02 10:43:17 +0530
  * Bug#15851528 DUPLICATE KEY ERROR ON AUTO-INC PK WITH MIXED AUTO\_INCREMENT\_INCREMENT CLIENTS
* [Revision #7153e15542](https://github.com/MariaDB/server/commit/7153e15542)\
  2019-07-23 11:01:44 +0300
  * Revert "[MDEV-8827](https://jira.mariadb.org/browse/MDEV-8827) Duplicate key with auto increment"
* [Revision #07ba5560da](https://github.com/MariaDB/server/commit/07ba5560da)\
  2016-08-26 11:00:44 +0530
  * Bug #20989615 INNODB AUTO\_INCREMENT PRODUCES SAME VALUE TWICE
* [Revision #82563c5fc0](https://github.com/MariaDB/server/commit/82563c5fc0)\
  2019-07-21 12:09:17 +0200
  * [MDEV-20110](https://jira.mariadb.org/browse/MDEV-20110) don't try to load client plugins with invalid names
* [Revision #f90040fd9c](https://github.com/MariaDB/server/commit/f90040fd9c)\
  2019-07-17 12:31:45 +0200
  * [MDEV-19429](https://jira.mariadb.org/browse/MDEV-19429): Wrong query result with EXISTS and LIMIT 0
* [Revision #cc86a0bd11](https://github.com/MariaDB/server/commit/cc86a0bd11)\
  2019-07-11 14:50:50 +0200
  * [MDEV-15572](https://jira.mariadb.org/browse/MDEV-15572): view.test, server crash with --big-tables=1
* [Revision #1a79a29c87](https://github.com/MariaDB/server/commit/1a79a29c87)\
  2019-07-12 10:03:33 +0200
  * [MDEV-17042](https://jira.mariadb.org/browse/MDEV-17042): prepared statement does not return error with SQL\_MODE STRICT\_TRANS\_TABLES.
* [Revision #8540fa83bb](https://github.com/MariaDB/server/commit/8540fa83bb)\
  2019-06-30 13:16:12 -0700
  * [MDEV-19421](https://jira.mariadb.org/browse/MDEV-19421) Basic 3-way join queries are not parsed.
* [Revision #8997f20f12](https://github.com/MariaDB/server/commit/8997f20f12)\
  2018-09-29 11:30:27 +0200
  * use -f with pgrep
* [Revision #399d012c81](https://github.com/MariaDB/server/commit/399d012c81)\
  2019-07-05 15:14:52 +0200
  * [MDEV-19922](https://jira.mariadb.org/browse/MDEV-19922) Old version of heidisql in mariadb installer
* [Revision #ecd8f44844](https://github.com/MariaDB/server/commit/ecd8f44844)\
  2019-07-01 13:55:05 +0300
  * Extra comment to mysql\_install\_db
* [Revision #d890c45b62](https://github.com/MariaDB/server/commit/d890c45b62)\
  2019-04-15 09:13:47 +1000
  * mysql\_install\_db: assume builddir is dirname0
* [Revision #69be8f3c5b](https://github.com/MariaDB/server/commit/69be8f3c5b)\
  2019-06-14 00:33:01 -0700
  * Apply valid parameter type for test case in i\_s\_parameters.test
* [Revision #645191aa13](https://github.com/MariaDB/server/commit/645191aa13)\
  2019-06-20 18:50:20 -0700
  * [MDEV-19778](https://jira.mariadb.org/browse/MDEV-19778) Wrong Result on Left Outer Join with Subquery right on true and WHERE filter afterwards
* [Revision #15065a2398](https://github.com/MariaDB/server/commit/15065a2398)\
  2019-05-27 13:18:24 +0300
  * [MDEV-19531](https://jira.mariadb.org/browse/MDEV-19531) Add colors to mtr
* [Revision #167da05f55](https://github.com/MariaDB/server/commit/167da05f55)\
  2019-06-17 14:23:10 -0700
  * [MDEV-19790](https://jira.mariadb.org/browse/MDEV-19790) Wrong result for query with outer join and IS NOT TRUE predicate in where clause
* [Revision #039b8782d4](https://github.com/MariaDB/server/commit/039b8782d4)\
  2019-06-12 22:36:43 +0300
  * [MDEV-13631](https://jira.mariadb.org/browse/MDEV-13631) Make use of clang-format
* [Revision #7a7d9904e1](https://github.com/MariaDB/server/commit/7a7d9904e1)\
  2019-06-11 12:02:26 +0300
  * [MDEV-18479](https://jira.mariadb.org/browse/MDEV-18479): Avoid COST\_MULT(records, 1)
* [Revision #96ee9ea02e](https://github.com/MariaDB/server/commit/96ee9ea02e)\
  2019-06-10 22:38:55 -0700
  * [MDEV-18479](https://jira.mariadb.org/browse/MDEV-18479) Another complement
* [Revision #6db2ebbb2a](https://github.com/MariaDB/server/commit/6db2ebbb2a)\
  2019-06-09 10:39:52 -0700
  * [MDEV-19580](https://jira.mariadb.org/browse/MDEV-19580) Unrelated JOINs corrupt usage of 'WHERE function() IN (subquery)'
* [Revision #6660c072ad](https://github.com/MariaDB/server/commit/6660c072ad)\
  2019-05-22 21:56:36 +0200
  * [MDEV-19491](https://jira.mariadb.org/browse/MDEV-19491) update query stopped working after mariadb upgrade 10.2.23 -> 10.2.24
* [Revision #1d4ac3d4d3](https://github.com/MariaDB/server/commit/1d4ac3d4d3)\
  2019-05-22 22:05:56 +0200
  * cleanup
* [Revision #5de08a53ef](https://github.com/MariaDB/server/commit/5de08a53ef)\
  2019-04-11 15:46:39 +0300
  * [MDEV-13631](https://jira.mariadb.org/browse/MDEV-13631) Make use of clang-format
* [Revision #cbb90f77cd](https://github.com/MariaDB/server/commit/cbb90f77cd)\
  2019-05-28 23:26:36 -0700
  * [MDEV-18479](https://jira.mariadb.org/browse/MDEV-18479) Complement
* [Revision #eb09580b67](https://github.com/MariaDB/server/commit/eb09580b67)\
  2019-05-28 14:53:08 -0700
  * [MDEV-19588](https://jira.mariadb.org/browse/MDEV-19588) Wrong results from query, using left join.
* [Revision #0955462d0a](https://github.com/MariaDB/server/commit/0955462d0a)\
  2019-05-27 19:08:00 -0700
  * [MDEV-18479](https://jira.mariadb.org/browse/MDEV-18479) Assertion \`join->best\_read < double(1.79769313486231570815e+308L)' or server crashes in JOIN::fix\_all\_splittings\_in\_plan after EXPLAIN
* [Revision #4584c18631](https://github.com/MariaDB/server/commit/4584c18631)\
  2019-05-22 00:52:15 +0200
  * make CPACK\_RPM\_DEBUGINFO\_PACKAGE configurable from the command-line
* [Revision #5034b31b01](https://github.com/MariaDB/server/commit/5034b31b01)\
  2019-05-20 18:23:10 +0200
  * [MDEV-17799](https://jira.mariadb.org/browse/MDEV-17799) Add ASAN-poisoned redzones for MEM\_ROOT
* [Revision #7b59ec6f34](https://github.com/MariaDB/server/commit/7b59ec6f34)\
  2018-11-28 13:25:43 +0300
  * [MDEV-17799](https://jira.mariadb.org/browse/MDEV-17799) Add ASAN-poisoned redzones for MEM\_ROOT and mem\_heap\_t
* [Revision #2c9844a438](https://github.com/MariaDB/server/commit/2c9844a438)\
  2019-05-19 11:44:34 -0700
  * [MDEV-18896](https://jira.mariadb.org/browse/MDEV-18896) Crash in convert\_join\_subqueries\_to\_semijoins : Correction
* [Revision #5543b75550](https://github.com/MariaDB/server/commit/5543b75550)\
  2019-05-11 21:29:06 +0300
  * Update FSF Address
* [Revision #15f1e03d46](https://github.com/MariaDB/server/commit/15f1e03d46)\
  2019-05-11 18:08:32 +0300
  * Follow-up to changing FSF address
* [Revision #17b4f99928](https://github.com/MariaDB/server/commit/17b4f99928)\
  2019-05-10 20:49:46 +0300
  * Update FSF address
* [Revision #aba9115426](https://github.com/MariaDB/server/commit/aba9115426)\
  2019-04-30 12:29:40 +0200
  * [MDEV-19349](https://jira.mariadb.org/browse/MDEV-19349) mysql\_install\_db: segfault at tmp\_file\_prefix check
* [Revision #71a748d575](https://github.com/MariaDB/server/commit/71a748d575)\
  2019-04-29 12:18:18 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
