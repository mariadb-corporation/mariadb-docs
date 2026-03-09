# MariaDB 5.5.63 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.63/)[Release Notes](../../old-releases/5.5/5.5.63.md)[Changelog](mariadb-5563-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 30 Jan 2019

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.63.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* [Revision #2175bfce3e](https://github.com/MariaDB/server/commit/2175bfce3e)\
  2019-01-25 23:12:35 +0100
  * Crude "auto-load-data-local-infile" mode
* [Revision #21f9037186](https://github.com/MariaDB/server/commit/21f9037186)\
  2019-01-24 00:58:20 +0200
  * [MDEV-18360](https://jira.mariadb.org/browse/MDEV-18360) Prevent set\_max\_open\_files from allocating too many files
* [Revision #ad220b96fb](https://github.com/MariaDB/server/commit/ad220b96fb)\
  2018-07-02 12:26:22 +0300
  * [MDEV-16658](https://jira.mariadb.org/browse/MDEV-16658) Memory leak in mysqltest on connect failure
* [Revision #949559285e](https://github.com/MariaDB/server/commit/949559285e)\
  2019-01-23 10:09:49 +0100
  * [MDEV-18059](https://jira.mariadb.org/browse/MDEV-18059) `support-files/mysql.server.sh stop` must run as root
* [Revision #a8da66f8c5](https://github.com/MariaDB/server/commit/a8da66f8c5)\
  2019-01-22 00:15:57 +0100
  * Bug #28499924: INCORRECT BEHAVIOR WITH UNION IN SUBQUERY
* [Revision #b20d94da35](https://github.com/MariaDB/server/commit/b20d94da35)\
  2018-10-09 12:03:35 +0530
  * Bug #28499924: INCORRECT BEHAVIOR WITH UNION IN SUBQUERY
* [Revision #6de2928d5b](https://github.com/MariaDB/server/commit/6de2928d5b)\
  2018-09-10 16:00:29 +0530
  * Bug #28178776 COMPARISON OF UNINITAILIZED MEMORY IN LOG\_IN\_USE
* [Revision #942a6bd009](https://github.com/MariaDB/server/commit/942a6bd009)\
  2019-01-23 09:51:06 +0200
  * [MDEV-18349](https://jira.mariadb.org/browse/MDEV-18349) InnoDB file size changes are not safe when file system crashes
* [Revision #9c5be7d131](https://github.com/MariaDB/server/commit/9c5be7d131)\
  2019-01-14 15:55:21 +0100
  * [MDEV-14580](https://jira.mariadb.org/browse/MDEV-14580): mysql\_install\_db elements based on dirname of mysql\_install\_db
* [Revision #50e593386f](https://github.com/MariaDB/server/commit/50e593386f)\
  2019-01-11 19:35:46 +1100
  * [MDEV-14580](https://jira.mariadb.org/browse/MDEV-14580): mysql\_install\_db elements based on dirname of mysql\_install\_db
* [Revision #0d3c49ef5d](https://github.com/MariaDB/server/commit/0d3c49ef5d)\
  2019-01-14 12:33:52 +0100
  * [MDEV-17615](https://jira.mariadb.org/browse/MDEV-17615) cmake ssl error on musl/libressl
* [Revision #e292d1a800](https://github.com/MariaDB/server/commit/e292d1a800)\
  2019-01-19 14:01:09 +0100
  * Avoid noisy Clang 7 warning about unused variable.
* [Revision #78f62e9079](https://github.com/MariaDB/server/commit/78f62e9079)\
  2019-01-04 13:32:51 +0600
  * remove duplicated paragraph from mysql\_install\_db.sh
* [Revision #459d6da869](https://github.com/MariaDB/server/commit/459d6da869)\
  2019-01-16 14:28:37 +0000
  * [MDEV-18269](https://jira.mariadb.org/browse/MDEV-18269) - fix off-by-one bug in unittest
* [Revision #1ecccb509c](https://github.com/MariaDB/server/commit/1ecccb509c)\
  2019-01-16 13:16:41 +0100
  * [MDEV-17085](https://jira.mariadb.org/browse/MDEV-17085): CHECKSUM TABLE EXTENDED does not work correctly
* [Revision #235374aee3](https://github.com/MariaDB/server/commit/235374aee3)\
  2019-01-15 18:44:03 +0100
  * [MDEV-18254](https://jira.mariadb.org/browse/MDEV-18254) upgrade HeidiSQL to 9.5
* [Revision #dc42b3c4d9](https://github.com/MariaDB/server/commit/dc42b3c4d9)\
  2019-01-11 01:44:07 +0100
  * Backport [MDEV-17504](https://jira.mariadb.org/browse/MDEV-17504) to 5.5
* [Revision #2450fd67ed](https://github.com/MariaDB/server/commit/2450fd67ed)\
  2019-01-02 12:03:15 +0100
  * fix the test for 2019
* [Revision #b0fd06a6f2](https://github.com/MariaDB/server/commit/b0fd06a6f2)\
  2018-12-18 17:07:29 +0400
  * [MDEV-15670](https://jira.mariadb.org/browse/MDEV-15670) - unit.my\_atomic failed in buildbot with Signal 11 thrown
* [Revision #65525550ab](https://github.com/MariaDB/server/commit/65525550ab)\
  2018-12-17 16:09:28 +0100
  * Don't default to bundled zlib
* [Revision #15eaeace39](https://github.com/MariaDB/server/commit/15eaeace39)\
  2018-12-12 19:58:20 +0400
  * [MDEV-16987](https://jira.mariadb.org/browse/MDEV-16987) - ALTER DATABASE possible in read-only mode
* [Revision #32b7d456d5](https://github.com/MariaDB/server/commit/32b7d456d5)\
  2018-11-28 19:19:16 +0100
  * mysqltest: use a dynamically growing command buffer
* [Revision #c362ea3ffd](https://github.com/MariaDB/server/commit/c362ea3ffd)\
  2014-06-25 12:32:22 +0200
  * Added Master\_Host to the Replication information
* [Revision #1956695c69](https://github.com/MariaDB/server/commit/1956695c69)\
  2018-11-15 16:45:43 +0400
  * [MDEV-17724](https://jira.mariadb.org/browse/MDEV-17724) Wrong result for BETWEEN 0 AND 18446744073709551615
* [Revision #7f175595c8](https://github.com/MariaDB/server/commit/7f175595c8)\
  2018-11-15 06:35:37 +0400
  * Backport for "[MDEV-17698](https://jira.mariadb.org/browse/MDEV-17698) MEMORY engine performance regression"
* [Revision #b68d8a05d3](https://github.com/MariaDB/server/commit/b68d8a05d3)\
  2018-10-12 09:07:05 +0200
  * [MDEV-17401](https://jira.mariadb.org/browse/MDEV-17401): LOAD DATA from very big file into MyISAM table results in EOF error and corrupt index
* [Revision #b7eca63620](https://github.com/MariaDB/server/commit/b7eca63620)\
  2018-11-01 18:47:53 +0100
  * fix the test to clean after itself
* [Revision #c32f7ed235](https://github.com/MariaDB/server/commit/c32f7ed235)\
  2018-10-31 18:18:48 +0100
  * [MDEV-17377](https://jira.mariadb.org/browse/MDEV-17377) invalid gap in auto-increment values after LOAD DATA
* [Revision #9ff9d2303d](https://github.com/MariaDB/server/commit/9ff9d2303d)\
  2018-10-28 22:50:49 +0900
  * test framework manual is moved
* [Revision #31f1fe223e](https://github.com/MariaDB/server/commit/31f1fe223e)\
  2018-10-30 20:19:56 +0100
  * don't try to build with OpenSSL 1.1+
* [Revision #250c5aa02c](https://github.com/MariaDB/server/commit/250c5aa02c)\
  2018-10-30 20:13:15 +0100
  * ./mtr --gdb='b mysql\_parse;r'
* [Revision #57898316b6](https://github.com/MariaDB/server/commit/57898316b6)\
  2018-10-30 18:15:41 +0400
  * [MDEV-17256](https://jira.mariadb.org/browse/MDEV-17256) Decimal field multiplication bug.
* [Revision #65cfc5873e](https://github.com/MariaDB/server/commit/65cfc5873e)\
  2018-10-26 04:00:00 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
