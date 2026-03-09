# MariaDB 5.5.67 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.67)[Release Notes](../../old-releases/5.5/5.5.67.md)[Changelog](mariadb-5567-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 28 Jan 2020

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.67.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* [Revision #4d1c1b23e1](https://github.com/MariaDB/server/commit/4d1c1b23e1)\
  2020-01-17 15:08:11 +0100
  * Bug#29630767 - USE OF UNINITIALIZED VALUE IN LIBMYSQL (CLIENT.CC FUNCTION RUN\_PLUGIN\_AUTH)
* [Revision #49b9ce15ef](https://github.com/MariaDB/server/commit/49b9ce15ef)\
  2019-11-20 08:10:36 +0530
  * Bug#30194841 INSERT ON DUPLICATE KEY UPDATE UPDATES THE WRONG ROW
* [Revision #1bee9efcc4](https://github.com/MariaDB/server/commit/1bee9efcc4)\
  2020-01-16 13:37:21 +0200
  * [MDEV-21210](https://jira.mariadb.org/browse/MDEV-21210): main.uniques\_crash-7912 tries to allocate 1TB of memory
* [Revision #409aba3d99](https://github.com/MariaDB/server/commit/409aba3d99)\
  2020-01-16 12:40:45 +0200
  * Improve documentation of Unique class
* [Revision #5683c113b8](https://github.com/MariaDB/server/commit/5683c113b8)\
  2019-12-05 07:58:02 +0200
  * Use get\_ident\_len in heartbeat event error messages
* [Revision #3c94c5b8fa](https://github.com/MariaDB/server/commit/3c94c5b8fa)\
  2020-01-03 10:25:46 +0100
  * [MDEV-21416](https://jira.mariadb.org/browse/MDEV-21416): main.events\_bugs fails due to 2020-01-01 date
* [Revision #80c97f8c0c](https://github.com/MariaDB/server/commit/80c97f8c0c)\
  2019-12-17 22:36:26 +0100
  * [MDEV-21343](https://jira.mariadb.org/browse/MDEV-21343) Threadpool/Unix- wait\_begin() function does not wake/create threads, when it should
* [Revision #fc860d3fa3](https://github.com/MariaDB/server/commit/fc860d3fa3)\
  2019-12-16 12:57:08 +0400
  * [MDEV-21065](https://jira.mariadb.org/browse/MDEV-21065) UNIQUE constraint causes a query with string comparison to omit a row in the result set
* [Revision #794911a27a](https://github.com/MariaDB/server/commit/794911a27a)\
  2019-12-13 11:23:29 +0100
  * tokudb: disable check\_huge\_pages\_in\_practice()
* [Revision #91c3d99804](https://github.com/MariaDB/server/commit/91c3d99804)\
  2019-12-13 11:23:04 +0100
  * tokudb: fix to compile with gcc 9.2.0
* [Revision #e3d3bbf598](https://github.com/MariaDB/server/commit/e3d3bbf598)\
  2019-11-28 15:08:29 +0100
  * Using `variables` instead of `values` in mysqld --help documentation would be more accurate
* [Revision #3cb60ec2c3](https://github.com/MariaDB/server/commit/3cb60ec2c3)\
  2019-11-29 15:50:40 +0100
  * Update `stracer` description in `mtr`. `strace-client` is not used
* [Revision #866e5c250e](https://github.com/MariaDB/server/commit/866e5c250e)\
  2018-02-11 14:42:11 +1100
  * [MDEV-15503](https://jira.mariadb.org/browse/MDEV-15503): mtr fix --strace
* [Revision #d8ace23d26](https://github.com/MariaDB/server/commit/d8ace23d26)\
  2019-10-23 17:40:24 +0500
  * Fixed some typos in mysql.cc
* [Revision #e23cb3835e](https://github.com/MariaDB/server/commit/e23cb3835e)\
  2019-11-05 09:53:45 -0500
  * bump the VERSION
* [Revision #cd156e2c3e](https://github.com/MariaDB/server/commit/cd156e2c3e)\
  2019-11-04 18:30:48 +0100
  * [MDEV-20971](https://jira.mariadb.org/browse/MDEV-20971) ASAN heap-use-after-free in list\_delete / heap\_close

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
