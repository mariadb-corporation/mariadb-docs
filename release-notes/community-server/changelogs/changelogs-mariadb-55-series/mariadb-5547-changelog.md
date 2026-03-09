# MariaDB 5.5.47 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.47)[Release Notes](../../old-releases/5.5/5.5.47.md)[Changelog](mariadb-5547-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 10 Dec 2015

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.47.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #d67aacb](https://github.com/MariaDB/server/commit/d67aacb)\
  2015-12-09 17:11:55 +0100
  * fix xtradb compilation on windows
* [Revision #fa4d4fc](https://github.com/MariaDB/server/commit/fa4d4fc)\
  2015-12-09 10:06:28 +0100
  * unit tests for my\_getopt
* [Revision #584c07b](https://github.com/MariaDB/server/commit/584c07b)\
  2015-10-21 11:51:15 +0200
  * [MDEV-8978](https://jira.mariadb.org/browse/MDEV-8978) Specify GPL version in RPM metadata
* [Revision #142b725](https://github.com/MariaDB/server/commit/142b725)\
  2015-12-09 12:57:04 +0100
  * Merge branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #9457139](https://github.com/MariaDB/server/commit/9457139)\
  2015-12-09 12:27:04 +0100
  * 5.5.46-37.6
* [Revision #1a72c6f](https://github.com/MariaDB/server/commit/1a72c6f)\
  2015-12-09 11:51:59 +0100
  * Merge branch 'bb-5.5-serg' into 5.5
* [Revision #abf9d35](https://github.com/MariaDB/server/commit/abf9d35)\
  2015-12-09 10:00:49 +0100
  * Merge branch 'mysql/5.5' into 5.5
* [Revision #dac3149](https://github.com/MariaDB/server/commit/dac3149)\
  2015-12-08 17:20:34 +0400
  * [MDEV-9001](https://jira.mariadb.org/browse/MDEV-9001) - \[PATCH] Fix DB name quoting in mysqldump --routine
* [Revision #50a796d](https://github.com/MariaDB/server/commit/50a796d)\
  2015-12-08 10:16:41 +0100
  * [MDEV-8825](https://jira.mariadb.org/browse/MDEV-8825) mysql\_upgrade leaks the admin password when it spawns a shell process to execute mysqlcheck
* [Revision #c21b927](https://github.com/MariaDB/server/commit/c21b927)\
  2015-12-08 10:13:13 +0100
  * mysql\_upgrade cleanup
* [Revision #f0d774d](https://github.com/MariaDB/server/commit/f0d774d)\
  2015-12-07 20:06:54 +0100
  * [MDEV-9212](https://jira.mariadb.org/browse/MDEV-9212) ssl-validate-cert incorrect hostname check
* [Revision #544eeda](https://github.com/MariaDB/server/commit/544eeda)\
  2015-12-07 20:27:58 +0100
  * [MDEV-8644](https://jira.mariadb.org/browse/MDEV-8644) Using a UDF in a virtual column causes a crash when stopping the server
* [Revision #79d08e6](https://github.com/MariaDB/server/commit/79d08e6)\
  2015-12-07 15:15:43 +0100
  * small cleanup: udf\_init()/udf\_free() calls
* [Revision #859a736](https://github.com/MariaDB/server/commit/859a736)\
  2015-12-07 14:07:36 +0100
  * [MDEV-9161](https://jira.mariadb.org/browse/MDEV-9161) feedback\_plugin\_send in debug builds
* [Revision #99774f1](https://github.com/MariaDB/server/commit/99774f1)\
  2015-12-06 11:51:57 +0100
  * feedback plugin compilation warnings
* [Revision #8fd24b4](https://github.com/MariaDB/server/commit/8fd24b4)\
  2015-12-07 20:25:27 +0100
  * [MDEV-9226](https://jira.mariadb.org/browse/MDEV-9226) SHOW COLUMNS returns wrong column order for tables with large ENUMs
* [Revision #f18599a](https://github.com/MariaDB/server/commit/f18599a)\
  2015-12-06 20:22:33 +0100
  * tokudb compilation warnings
* [Revision #d1fe928](https://github.com/MariaDB/server/commit/d1fe928)\
  2015-12-06 12:01:12 +0100
  * [MDEV-8607](https://jira.mariadb.org/browse/MDEV-8607) Init script doesn't check all applicable configuration groups
* [Revision #18954ff](https://github.com/MariaDB/server/commit/18954ff)\
  2015-12-06 01:48:07 +0100
  * [MDEV-8313](https://jira.mariadb.org/browse/MDEV-8313) Got an error writing communication packets
* [Revision #354e567](https://github.com/MariaDB/server/commit/354e567)\
  2015-12-06 01:40:51 +0100
  * federatedx small cleanup
* [Revision #e05883b](https://github.com/MariaDB/server/commit/e05883b)\
  2015-12-05 15:25:15 +0100
  * [MDEV-7341](https://jira.mariadb.org/browse/MDEV-7341) mysqld\_multi doesn't recognize include directive (not following includes)
* [Revision #ef47b625](https://github.com/MariaDB/server/commit/ef47b625)\
  2015-12-05 11:29:00 +0100
  * [MDEV-8827](https://jira.mariadb.org/browse/MDEV-8827) Duplicate key with auto increment
* [Revision #c8652ee](https://github.com/MariaDB/server/commit/c8652ee)\
  2015-12-05 11:22:25 +0100
  * one more test
* [Revision #ee2fce5](https://github.com/MariaDB/server/commit/ee2fce5)\
  2015-10-20 09:41:44 +0200
  * fix debian logrotate slow log filename
* [Revision #0df22a5](https://github.com/MariaDB/server/commit/0df22a5)\
  2015-12-07 09:34:41 +0200
  * [MDEV-7050](https://jira.mariadb.org/browse/MDEV-7050): MySQL#74603 - Assertion \`comma\_length > 0' failed in mysql\_prepare\_create\_table
* [Revision #d85168e](https://github.com/MariaDB/server/commit/d85168e)\
  2015-12-07 09:20:31 +0200
  * Correct length check in my\_wc\_mb\_filename()
* [Revision #e528fe7](https://github.com/MariaDB/server/commit/e528fe7)\
  2015-12-05 12:21:33 +0200
  * Fix gcc v5.compiler errors.
* [Revision #082b859](https://github.com/MariaDB/server/commit/082b859)\
  2015-12-04 14:24:03 +0200
  * [MDEV-9233](https://jira.mariadb.org/browse/MDEV-9233): Copying MySQL 5.5 data directory to 10.0 with partition tables crashes on insert
* [Revision #d87bc55](https://github.com/MariaDB/server/commit/d87bc55)\
  2015-12-03 20:43:54 +0400
  * [MDEV-8630](https://jira.mariadb.org/browse/MDEV-8630) Datetime value dropped in "INSERT ... SELECT ... ON DUPLICATE KEY" Item\_func\_coalesce::fix\_length\_and\_dec() calls Item\_func::count\_string\_result\_length()) which called agg\_arg\_charsets() with wrong flags, so the collation derivation of the COALESCE result was not properly set to DERIVATION\_COERCIBLE. It erroneously stayed DERIVATION\_NUMERIC. So GREATEST() misinterpreted the argument as a number rather that a string and did not calculate its own length properly.
* [Revision #9f07c6b](https://github.com/MariaDB/server/commit/9f07c6b)\
  2015-12-02 16:08:54 +0400
  * [MDEV-9001](https://jira.mariadb.org/browse/MDEV-9001) - \[PATCH] Fix DB name quoting in mysqldump --routine
* [Revision #33589b2](https://github.com/MariaDB/server/commit/33589b2)\
  2015-12-03 13:18:10 +0200
  * [MDEV-7762](https://jira.mariadb.org/browse/MDEV-7762) InnoDB: Failing assertion: block->page.buf\_fix\_count > 0 in buf0buf.ic line 730
* [Revision #13ad179](https://github.com/MariaDB/server/commit/13ad179)\
  2015-11-20 14:50:18 +0100
  * [MDEV-8756](https://jira.mariadb.org/browse/MDEV-8756) [MariaDB 10.0.21](../../old-releases/10.0/10.0.21.md) crashes during PREPARE
* [Revision #43a5090](https://github.com/MariaDB/server/commit/43a5090)\
  2015-11-18 11:20:59 +0100
  * [MDEV-9051](https://jira.mariadb.org/browse/MDEV-9051) mysqld got signal 11, after upgrade to 10.1.8
* [Revision #7261629](https://github.com/MariaDB/server/commit/7261629)\
  2015-11-18 10:58:51 +0100
  * feedback plugin debug
* [Revision #e669a5f](https://github.com/MariaDB/server/commit/e669a5f)\
  2015-11-17 18:33:08 +0100
  * [MDEV-7588](https://jira.mariadb.org/browse/MDEV-7588) Add thd\_wait\_begin/end to notify threadpool of binlog waits
* [Revision #7e4da9b](https://github.com/MariaDB/server/commit/7e4da9b)\
  2015-11-06 16:36:41 +0100
  * [MDEV-8632](https://jira.mariadb.org/browse/MDEV-8632) Segmentation fault on INSERT
* [Revision #5d754fc](https://github.com/MariaDB/server/commit/5d754fc)\
  2015-11-09 09:23:32 +0200
  * [MDEV-8854](https://jira.mariadb.org/browse/MDEV-8854): New warning messages are unreadable
* [Revision #c88ca2c](https://github.com/MariaDB/server/commit/c88ca2c)\
  2015-11-06 17:56:56 +0100
  * [MDEV-8701](https://jira.mariadb.org/browse/MDEV-8701) Crash on derived query [MDEV-8938](https://jira.mariadb.org/browse/MDEV-8938) Server Crash on Update with joins
* [Revision #df80420](https://github.com/MariaDB/server/commit/df80420)\
  2015-10-21 14:42:56 +0200
  * fix events\_1 test for October 2015
* [Revision #978c2a3](https://github.com/MariaDB/server/commit/978c2a3)\
  2015-10-11 17:06:03 -0400
  * [MDEV-7640](https://jira.mariadb.org/browse/MDEV-7640): CHANGE MASTER TO doesn't work with prepared statements

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
