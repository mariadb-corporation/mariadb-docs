# MariaDB 5.5.42 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.42)[Release Notes](../../old-releases/5.5/5.5.42.md)[Changelog](mariadb-5542-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 19 Feb 2015

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.42.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #fdd6c11](https://github.com/MariaDB/server/commit/fdd6c11)\
  2015-02-13 12:57:11 +0100
  * [MDEV-7419](https://jira.mariadb.org/browse/MDEV-7419) Function cli\_safe\_read not exported
* [Revision #13927f8](https://github.com/MariaDB/server/commit/13927f8)\
  2015-02-11 18:32:40 +0100
  * percona-server-5.5.41-37.0
* [Revision #d996dc2](https://github.com/MariaDB/server/commit/d996dc2)\
  2015-02-11 15:02:15 +0100
  * [MDEV-7290](https://jira.mariadb.org/browse/MDEV-7290) please update MSI installer to include HeidiSQL 9.1
* [Revision #63108dc](https://github.com/MariaDB/server/commit/63108dc)\
  2015-02-10 12:26:21 +0100
  * Fix the tree to work in git. Backport corresponing 10.1 changes.
* [Revision #7588424](https://github.com/MariaDB/server/commit/7588424)\
  2015-02-10 10:19:42 +0100
  * restore a cross-compiling bit that was lost in a merge
* [Revision #a34fd50](https://github.com/MariaDB/server/commit/a34fd50)\
  2015-02-09 20:53:36 +0100
  * [MDEV-7478](https://jira.mariadb.org/browse/MDEV-7478) log-basename unpredictable behavior in standalone mode
* [Revision #f007f82](https://github.com/MariaDB/server/commit/f007f82)\
  2015-02-09 20:53:28 +0100
  * [MDEV-7351](https://jira.mariadb.org/browse/MDEV-7351) 5.5 build fails on Ubuntu Utopic in buildbot
* [Revision #c233d6e](https://github.com/MariaDB/server/commit/c233d6e)\
  2015-02-11 01:26:50 +0100
  * [MDEV-7260](https://jira.mariadb.org/browse/MDEV-7260): Crash in get\_best\_combination when executing multi-table UPDATE with nested views
* [Revision #cfb7d5d](https://github.com/MariaDB/server/commit/cfb7d5d)\
  2015-02-10 16:16:31 +0400
  * [MDEV-7516](https://jira.mariadb.org/browse/MDEV-7516) Assertion \`!cur\_p->event' failed in Gcalc\_scan\_iterator::arrange\_event(int, int). When the distance in ST\_BUFFER is too far negative the coordinates can run out of the operational area. We should just return an empty geometry in this case.
* [Revision #552f1b3](https://github.com/MariaDB/server/commit/552f1b3)\
  2015-02-10 14:17:23 +0200
  * Fix test failures on innodb-[MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055) and innodb-[MDEV-7513](https://jira.mariadb.org/browse/MDEV-7513).
* [Revision #ada0743](https://github.com/MariaDB/server/commit/ada0743)\
  2015-02-10 08:08:59 +0200
  * Fix test failure on innodb-[MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055).
* [Revision #44a9e3f](https://github.com/MariaDB/server/commit/44a9e3f)\
  2015-02-09 16:14:27 +0200
  * [MDEV-7139](https://jira.mariadb.org/browse/MDEV-7139): Sporadic failure in innodb.innodb\_corrupt\_bit on P8
* [Revision #919f40e](https://github.com/MariaDB/server/commit/919f40e)\
  2015-02-08 22:38:19 +0400
  * Audit plugin v1.2.0.
* [Revision #0d73bc1](https://github.com/MariaDB/server/commit/0d73bc1)\
  2015-02-08 15:47:00 +0300
  * [MDEV-7519](https://jira.mariadb.org/browse/MDEV-7519) debian / ubuntu packaging creation of plugin table (if not exists)
* [Revision #b9d616c](https://github.com/MariaDB/server/commit/b9d616c)\
  2015-02-06 15:49:45 +0400
  * [MDEV-7435](https://jira.mariadb.org/browse/MDEV-7435) Windows debug: Run-Time Check Failure #3 - The variable 'unused' is being used without being initialized. Fixed as it's done in 10.0.
* [Revision #5c6eb52](https://github.com/MariaDB/server/commit/5c6eb52)\
  2015-02-04 16:50:29 +0200
  * Fix test failure.
* [Revision #8cc9751](https://github.com/MariaDB/server/commit/8cc9751)\
  2015-02-04 14:40:46 +0200
  * [MDEV-7538](https://jira.mariadb.org/browse/MDEV-7538): Wrong constraint (TINYINT or MEDIUMINT and INT) causes server crash
* [Revision #422ffe9](https://github.com/MariaDB/server/commit/422ffe9)\
  2015-02-04 11:12:46 +0200
  * InnoDB and XtraDB produce different output on [MDEV-7513](https://jira.mariadb.org/browse/MDEV-7513).
* [Revision #f320915](https://github.com/MariaDB/server/commit/f320915)\
  2015-02-04 10:50:16 +0200
  * [MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055): MySQL#74664 - InnoDB: Failing assertion: len <= col->len || col->mtype == 5 || (col->len == 0 && col->mtype == 1) in file rem0rec.cc line 845
* [Revision #7afbf33](https://github.com/MariaDB/server/commit/7afbf33)\
  2015-02-04 09:29:54 +0200
  * [MDEV-7513](https://jira.mariadb.org/browse/MDEV-7513): ib\_warn\_row\_too\_big dereferences null thd
* [Revision #5f63c9c](https://github.com/MariaDB/server/commit/5f63c9c)\
  2015-01-29 14:34:31 +0100
  * recreate expired certificates for SSL tests
* [Revision #9033aa0](https://github.com/MariaDB/server/commit/9033aa0)\
  2015-01-28 11:49:55 +0100
  * [MDEV-6128](https://jira.mariadb.org/browse/MDEV-6128):\[PATCH] mysqlcheck wrongly escapes '.' in table names
* [Revision #cb9c116](https://github.com/MariaDB/server/commit/cb9c116)\
  2015-01-23 09:13:21 +0100
  * update tokudb version after merge
* [Revision #8bc712e](https://github.com/MariaDB/server/commit/8bc712e)\
  2015-01-19 17:31:59 +0100
  * [MDEV-6671](https://jira.mariadb.org/browse/MDEV-6671) mysql\_server\_end breaks OpenSSL
* [Revision #3212aaa](https://github.com/MariaDB/server/commit/3212aaa)\
  2015-01-19 17:18:24 +0100
  * [MDEV-6220](https://jira.mariadb.org/browse/MDEV-6220) mysqldump will not backup database with --flush-logs parameter and log\_error my.cnf parameter defined
* [Revision #a18eb83](https://github.com/MariaDB/server/commit/a18eb83)\
  2015-01-19 16:41:37 +0100
  * [MDEV-7226](https://jira.mariadb.org/browse/MDEV-7226) sql-bench test-table-elimination does not execute
* [Revision #595cf63](https://github.com/MariaDB/server/commit/595cf63)\
  2015-01-19 16:29:18 +0100
  * [MDEV-7475](https://jira.mariadb.org/browse/MDEV-7475) Wrong implementation of checking PLUGIN\_VAR\_SET condition
* [Revision #5d0d6cb](https://github.com/MariaDB/server/commit/5d0d6cb)\
  2015-01-19 16:28:58 +0100
  * [MDEV-7294](https://jira.mariadb.org/browse/MDEV-7294) MTR does not use /dev/shm with a out-of-source build
* [Revision #3f118a7](https://github.com/MariaDB/server/commit/3f118a7)\
  2015-01-16 18:13:02 +0100
  * [MDEV-6347](https://jira.mariadb.org/browse/MDEV-6347) Build RHEL7 packages
* [Revision #2fc0b22](https://github.com/MariaDB/server/commit/2fc0b22)\
  2015-01-16 17:54:00 +0100
  * restore an incorrectly merged line
* [Revision #ca6b86f](https://github.com/MariaDB/server/commit/ca6b86f)\
  2015-01-14 17:50:38 +0400
  * [MDEV-7448](https://jira.mariadb.org/browse/MDEV-7448) - mtr may leave stale mysqld
* [Revision #d9d9940](https://github.com/MariaDB/server/commit/d9d9940)\
  2015-01-14 18:24:23 -0500
  * [MDEV-7368](https://jira.mariadb.org/browse/MDEV-7368) : SLES: Failed to start mysql.service: Unit mysql.service failed to load
* [Revision #5900333](https://github.com/MariaDB/server/commit/5900333)\
  2015-01-14 12:10:13 +0100
  * [MDEV-7404](https://jira.mariadb.org/browse/MDEV-7404) REPAIR multiple tables crash in MDL\_ticket::has\_stronger\_or\_equal\_type
* [Revision #e53b41a](https://github.com/MariaDB/server/commit/e53b41a)\
  2015-01-13 19:28:03 +0100
  * cleanup
* [Revision #7f9f313](https://github.com/MariaDB/server/commit/7f9f313)\
  2015-01-13 19:27:28 +0100
  * [MDEV-7333](https://jira.mariadb.org/browse/MDEV-7333) "'show table status like 'table\_name'" on tokudb table lead to MariaDB crash
* [Revision #2ab4968](https://github.com/MariaDB/server/commit/2ab4968)\
  2015-01-10 14:07:46 +0100
  * [MDEV-7410](https://jira.mariadb.org/browse/MDEV-7410) Temporary table name conflict between sessions
* [Revision #0064952](https://github.com/MariaDB/server/commit/0064952)\
  2015-01-06 16:32:41 +0100
  * [MDEV-7189](https://jira.mariadb.org/browse/MDEV-7189): main.processlist fails sporadically in buildbot
* [Revision #068416d](https://github.com/MariaDB/server/commit/068416d)\
  2015-01-02 09:50:51 -0500
  * DB-785 add a txn api to check if a txn is prepared
* [Revision #5fafc3c](https://github.com/MariaDB/server/commit/5fafc3c)\
  2014-12-28 13:24:53 +0200
  * [MDEV-7369](https://jira.mariadb.org/browse/MDEV-7369): MariaDB build fails when XTRADB\_STORAGE\_ENGINE enabled
* [Revision #8051205](https://github.com/MariaDB/server/commit/8051205)\
  2014-12-23 21:21:23 +0400
  * Increased the version number
* [Revision #3818bbb](https://github.com/MariaDB/server/commit/3818bbb)\
  2014-12-21 19:23:28 +0100
  * Adding mariadb-version on the view creation to view frm. ([MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916) followup)
* [Revision #260727a](https://github.com/MariaDB/server/commit/260727a)\
  2014-12-19 23:42:22 +0400
  * Fixed yet another compiler warning.
* [Revision #094640c](https://github.com/MariaDB/server/commit/094640c)\
  2014-12-19 23:17:59 +0400
  * Fixed a couple of compiler warnings.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
