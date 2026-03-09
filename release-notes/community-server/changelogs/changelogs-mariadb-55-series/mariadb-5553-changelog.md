# MariaDB 5.5.53 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.53)[Release Notes](../../old-releases/5.5/5.5.53.md)[Changelog](mariadb-5553-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 17 Oct 2016

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.53.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #eac8d95](https://github.com/MariaDB/server/commit/eac8d95)\
  2016-10-14 12:51:53 +0200
  * compilation warning after xtradb merge
* [Revision #5a43a31](https://github.com/MariaDB/server/commit/5a43a31)\
  2016-10-14 00:33:49 +0200
  * mysqldump: comments and identifiers with new lines
* [Revision #01b39b7](https://github.com/MariaDB/server/commit/01b39b7)\
  2016-10-13 20:58:08 +0200
  * mysqltest: don't eat new lines in --exec
* [Revision #383007c](https://github.com/MariaDB/server/commit/383007c)\
  2016-10-13 21:35:01 +0200
  * mysql cli: fix USE command quoting
* [Revision #e4957de](https://github.com/MariaDB/server/commit/e4957de) 2016-10-13 12:40:24 +0200 - Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #6010a27](https://github.com/MariaDB/server/commit/6010a27)\
  2016-10-13 12:23:16 +0200
  * 5.5.52-38.3
* [Revision #02be50a](https://github.com/MariaDB/server/commit/02be50a) 2016-10-13 11:18:30 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #7497ebf](https://github.com/MariaDB/server/commit/7497ebf)\
  2016-09-29 10:16:24 +0200
  * mysqld\_safe: close stdout and stderr
* [Revision #0e76054](https://github.com/MariaDB/server/commit/0e76054)\
  2016-09-28 12:52:01 +0000
  * Feedback plugin : add support for Windows 10 / Server 2016.
* [Revision #b38d3c3](https://github.com/MariaDB/server/commit/b38d3c3)\
  2016-09-27 12:34:15 +0000
  * [MDEV-10907](https://jira.mariadb.org/browse/MDEV-10907) MTR and server writes can interleave in the error log
* [Revision #d61e526](https://github.com/MariaDB/server/commit/d61e526)\
  2016-09-26 17:48:08 +0200
  * [MDEV-10441](https://jira.mariadb.org/browse/MDEV-10441) Document the server\_audit\_loc\_info variable
* [Revision #c91fdb6](https://github.com/MariaDB/server/commit/c91fdb6)\
  2016-09-26 13:03:02 +0200
  * Windows , mtr : allow cdb to print core dumps also if --parallel > 1
* [Revision #8483659](https://github.com/MariaDB/server/commit/8483659)\
  2016-09-24 10:06:58 +0200
  * report correct write error on log writes
* [Revision #f620da1](https://github.com/MariaDB/server/commit/f620da1)\
  2016-09-24 01:17:35 +0200
  * [MDEV-10725](https://jira.mariadb.org/browse/MDEV-10725) Server 10.1.17 fails to build using clang with c++11
* [Revision #9434431](https://github.com/MariaDB/server/commit/9434431)\
  2016-09-24 13:50:42 +0200
  * Fix free() after my\_malloc() (should be my\_free()).
* [Revision #b3f7a80](https://github.com/MariaDB/server/commit/b3f7a80)\
  2016-09-13 11:12:54 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
