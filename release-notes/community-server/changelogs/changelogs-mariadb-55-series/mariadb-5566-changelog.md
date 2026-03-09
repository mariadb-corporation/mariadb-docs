# MariaDB 5.5.66 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.66/)[Release Notes](../../old-releases/5.5/5.5.66.md)[Changelog](mariadb-5566-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 5 Nov 2019

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.66.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* [Revision #9277b6ec1c](https://github.com/MariaDB/server/commit/9277b6ec1c)\
  2019-10-30 14:38:18 +0100
  * Revert "[MDEV-14448](https://jira.mariadb.org/browse/MDEV-14448): Ctrl-C should not exit the client"
* [Revision #afb4878703](https://github.com/MariaDB/server/commit/afb4878703)\
  2019-06-25 15:52:05 +0400
  * [MDEV-18783](https://jira.mariadb.org/browse/MDEV-18783) - Server crash in hp\_rb\_make\_key
* [Revision #20b72a3fad](https://github.com/MariaDB/server/commit/20b72a3fad)\
  2019-10-30 00:47:50 +0100
  * compilation fix for Windows
* [Revision #84088d9458](https://github.com/MariaDB/server/commit/84088d9458)\
  2019-10-29 21:56:24 +0300
  * add .clang-format file for InnoDB
* [Revision #396313d301](https://github.com/MariaDB/server/commit/396313d301)\
  2019-05-22 01:54:47 -0700
  * [MDEV-14448](https://jira.mariadb.org/browse/MDEV-14448): Ctrl-C should not exit the client
* [Revision #719ac0ad4a](https://github.com/MariaDB/server/commit/719ac0ad4a)\
  2019-10-19 09:32:11 +0200
  * crash in string-to-int conversion
* [Revision #412e3e6917](https://github.com/MariaDB/server/commit/412e3e6917)\
  2019-09-13 09:52:30 +0200
  * [MDEV-9546](https://jira.mariadb.org/browse/MDEV-9546) mysqlaccess script shows an old version (which was vulnerable to [CVE-2005-0004](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-0004))
* [Revision #c9b5280371](https://github.com/MariaDB/server/commit/c9b5280371)\
  2019-10-19 10:01:26 +0200
  * [MDEV-20466](https://jira.mariadb.org/browse/MDEV-20466): fix of embedded test suite
* [Revision #b7bc8c3fcb](https://github.com/MariaDB/server/commit/b7bc8c3fcb)\
  2019-10-15 19:28:24 +0200
  * [MDEV-20466](https://jira.mariadb.org/browse/MDEV-20466): fix of test suite
* [Revision #4ba763db77](https://github.com/MariaDB/server/commit/4ba763db77)\
  2019-10-15 12:24:23 +0200
  * [MDEV-13172](https://jira.mariadb.org/browse/MDEV-13172): Wrong result / SELECT ... WHERE EXISTS ... (with UNIQUE Key)
* [Revision #c2854c7863](https://github.com/MariaDB/server/commit/c2854c7863)\
  2019-10-14 16:45:51 +0200
  * [MDEV-20466](https://jira.mariadb.org/browse/MDEV-20466): SHOW PROCESSLIST truncates query text on \0 bytes
* [Revision #ea61b79694](https://github.com/MariaDB/server/commit/ea61b79694)\
  2019-10-11 14:12:36 +0300
  * [MDEV-20805](https://jira.mariadb.org/browse/MDEV-20805) ibuf\_add\_free\_page() is not initializing FIL\_PAGE\_TYPE first
* [Revision #4ebaf81360](https://github.com/MariaDB/server/commit/4ebaf81360)\
  2019-10-11 14:02:35 +0300
  * [MDEV-19455](https://jira.mariadb.org/browse/MDEV-19455): Avoid SET DEBUG\_DBUG='-d,...' construct
* [Revision #db9a4d928d](https://github.com/MariaDB/server/commit/db9a4d928d)\
  2019-10-07 17:18:10 +0300
  * Remove orphan declaration buf\_flush\_wait\_batch\_end\_wait\_only()
* [Revision #d481f69a7d](https://github.com/MariaDB/server/commit/d481f69a7d)\
  2019-10-01 05:55:14 +0400
  * [MDEV-20704](https://jira.mariadb.org/browse/MDEV-20704) An index on a double column erroneously uses prefix compression
* [Revision #67b0faa29e](https://github.com/MariaDB/server/commit/67b0faa29e)\
  2019-09-24 10:46:18 +0400
  * [MDEV-20495](https://jira.mariadb.org/browse/MDEV-20495) Assertion \`precision > 0' failed in decimal\_bin\_size upon CREATE .. SELECT with zerofilled decimal
* [Revision #fd3ad41eed](https://github.com/MariaDB/server/commit/fd3ad41eed)\
  2019-09-16 22:36:19 +0300
  * Update mysqld\_safe.sh - introduce defaults-group-suffix handling
* [Revision #13274032af](https://github.com/MariaDB/server/commit/13274032af)\
  2019-03-24 23:25:20 -0400
  * [MDEV-4968](https://jira.mariadb.org/browse/MDEV-4968) Old advices in mysql-log-rotate script
* [Revision #38fa0141ee](https://github.com/MariaDB/server/commit/38fa0141ee)\
  2019-09-12 12:09:02 +0200
  * Fix spelling mistakes in MyISAM code comments
* [Revision #f541d3f18e](https://github.com/MariaDB/server/commit/f541d3f18e)\
  2019-09-16 10:40:06 -0700
  * [MDEV-20596](https://jira.mariadb.org/browse/MDEV-20596) Configure fails with newer CMake
* [Revision #df61c58499](https://github.com/MariaDB/server/commit/df61c58499)\
  2019-09-01 12:29:55 +0200
  * [MDEV-14383](https://jira.mariadb.org/browse/MDEV-14383) tokudb\_bugs. tests failed in buildbot, lost connection to server
* [Revision #4e89fdb9d8](https://github.com/MariaDB/server/commit/4e89fdb9d8)\
  2019-08-17 12:59:16 -0400
  * [MDEV-19837](https://jira.mariadb.org/browse/MDEV-19837) and [MDEV-19816](https://jira.mariadb.org/browse/MDEV-19816): Change some comments
* [Revision #e746f451d5](https://github.com/MariaDB/server/commit/e746f451d5)\
  2019-08-15 17:27:49 -0700
  * [MDEV-20265](https://jira.mariadb.org/browse/MDEV-20265) Unknown column in field list
* [Revision #ec1f195ecf](https://github.com/MariaDB/server/commit/ec1f195ecf)\
  2019-08-16 14:32:44 +0400
  * [MDEV-15955](https://jira.mariadb.org/browse/MDEV-15955) Assertion \`field\_types == 0 || field\_types\[field\_pos] == MYSQL\_TYPE\_LONGLONG' failed in Protocol\_text::store\_longlong
* [Revision #1217e4a0c0](https://github.com/MariaDB/server/commit/1217e4a0c0)\
  2019-08-12 14:12:32 +0300
  * Fix -Wimplicit-fallthrough
* [Revision #b2a387a3f1](https://github.com/MariaDB/server/commit/b2a387a3f1)\
  2019-08-12 14:05:26 +0300
  * Document TRASH\_FILL, TRASH\_ALLOC, TRASH\_FREE
* [Revision #cabf10b640](https://github.com/MariaDB/server/commit/cabf10b640)\
  2019-07-31 09:53:58 -0400
  * bump the VERSION
* [Revision #f8a1a262e2](https://github.com/MariaDB/server/commit/f8a1a262e2)\
  2019-07-26 13:15:44 +0200
  * Move the test not suitable for embedded.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
