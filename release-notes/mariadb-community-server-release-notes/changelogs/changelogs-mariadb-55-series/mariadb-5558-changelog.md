# MariaDB 5.5.58 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5568-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.58)[Release Notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5558-release-notes.md)[Changelog](mariadb-5558-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 18 Oct 2017

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5558-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* [Revision #b000e16956](https://github.com/MariaDB/server/commit/b000e16956)\
  2017-10-17 10:57:51 +0200
  * Bug#26361149 MYSQL SERVER CRASHES AT: COL IN(IFNULL(CONST, COL), NAME\_CONST('NAME', NULL))
* Merge [Revision #df5f25fa7a](https://github.com/MariaDB/server/commit/df5f25fa7a) 2017-10-17 10:18:17 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #b036b6b594](https://github.com/MariaDB/server/commit/b036b6b594)\
  2017-10-16 12:34:17 +0200
  * [MDEV-13937](https://jira.mariadb.org/browse/MDEV-13937) Aria engine: Internal Error 160 after partition handling
* [Revision #19a702a85c](https://github.com/MariaDB/server/commit/19a702a85c)\
  2017-10-14 15:59:54 +0200
  * [MDEV-14056](https://jira.mariadb.org/browse/MDEV-14056) DROP TEMPORARY TABLE IF EXISTS causes error 1290 with read\_only option
* [Revision #421716391b](https://github.com/MariaDB/server/commit/421716391b)\
  2017-10-14 15:03:43 +0200
  * [MDEV-13912](https://jira.mariadb.org/browse/MDEV-13912) Can't refer the same column twice in one ALTER TABLE
* [Revision #93144b9e92](https://github.com/MariaDB/server/commit/93144b9e92)\
  2017-10-13 21:26:30 +0200
  * [MDEV-13440](https://jira.mariadb.org/browse/MDEV-13440) mysql\_install\_db fails with hard-coded langdir
* [Revision #52516706c8](https://github.com/MariaDB/server/commit/52516706c8)\
  2017-10-13 20:53:55 +0200
  * cleanup mysql\_install\_db
* [Revision #d76f5774fe](https://github.com/MariaDB/server/commit/d76f5774fe)\
  2017-09-16 14:52:42 +0200
  * [MDEV-13459](https://jira.mariadb.org/browse/MDEV-13459) Warnings, when compiling with gcc-7.x
* [Revision #3b7aa3017b](https://github.com/MariaDB/server/commit/3b7aa3017b)\
  2017-10-13 18:41:38 +0200
  * Cleanup usage of DBUG\_ASSERTS.
* [Revision #235b68299b](https://github.com/MariaDB/server/commit/235b68299b)\
  2017-02-18 17:47:31 +0100
  * [MDEV-9619](https://jira.mariadb.org/browse/MDEV-9619): Assertion \`null\_ref\_table' failed in virtual table\_map Item\_direct\_view\_ref::used\_tables() const on 2nd execution of PS
* [Revision #2bab29ebba](https://github.com/MariaDB/server/commit/2bab29ebba)\
  2017-10-13 07:24:35 -0700
  * Fixed the bug [MDEV-13135](https://jira.mariadb.org/browse/MDEV-13135).
* [Revision #8be76a6a90](https://github.com/MariaDB/server/commit/8be76a6a90)\
  2017-10-12 13:30:02 +0400
  * [MDEV-10892](https://jira.mariadb.org/browse/MDEV-10892) - rpl.rpl\_semi\_sync\_uninstall\_plugin fails with Assertion \`0' failure in buildbot
* [Revision #a4868c3509](https://github.com/MariaDB/server/commit/a4868c3509)\
  2016-12-19 22:03:28 +0100
  * [MDEV-9208](https://jira.mariadb.org/browse/MDEV-9208): Function->Function->View = Mysqld segfault (Server crashes in Dependency\_marker::visit\_field on 2nd execution with merged subquery)
* [Revision #991b9ee735](https://github.com/MariaDB/server/commit/991b9ee735)\
  2017-10-13 07:06:09 +0400
  * [MDEV-13530](https://jira.mariadb.org/browse/MDEV-13530) VARBINARY doesn't convert to BLOB for sizes 65533, 65534 and 65535
* [Revision #93aadda513](https://github.com/MariaDB/server/commit/93aadda513)\
  2017-10-08 22:15:00 +0300
  * [MDEV-13149](https://jira.mariadb.org/browse/MDEV-13149) -- show function status now works with PAD\_CHAR\_TO\_FULL\_LENGTH
* [Revision #c2509a1588](https://github.com/MariaDB/server/commit/c2509a1588)\
  2017-10-10 10:35:12 +0400
  * [MDEV-13972](https://jira.mariadb.org/browse/MDEV-13972) crash in Item\_func\_sec\_to\_time::get\_date
* [Revision #e30b6a983f](https://github.com/MariaDB/server/commit/e30b6a983f)\
  2017-10-06 18:23:40 +0400
  * [MDEV-11819](https://jira.mariadb.org/browse/MDEV-11819) NO\_ZERO\_IN\_DATE: Incorrect generated column value
* [Revision #bea99275de](https://github.com/MariaDB/server/commit/bea99275de)\
  2017-10-05 15:07:21 +0200
  * [MDEV-13595](https://jira.mariadb.org/browse/MDEV-13595): mariadb-10.2.8/storage/maria/ma\_loghandler.c:2730]: (style) Array index 'chunk\_offset' is used before limits check.
* [Revision #028d253dd7](https://github.com/MariaDB/server/commit/028d253dd7)\
  2017-10-02 10:22:42 +0300
  * [MDEV-13980](https://jira.mariadb.org/browse/MDEV-13980) InnoDB fails to discard record lock when discarding an index page
* [Revision #a47d16907d](https://github.com/MariaDB/server/commit/a47d16907d)\
  2017-09-19 13:08:24 +0400
  * [MDEV-13137](https://jira.mariadb.org/browse/MDEV-13137) MySQL 5.6.23 Crashes when SET GLOBAL server\_audit\_logging=OFF;
* Merge [Revision #e7bb818116](https://github.com/MariaDB/server/commit/e7bb818116) 2017-09-19 00:31:15 +0300 - Merge remote-tracking branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #f534eef794](https://github.com/MariaDB/server/commit/f534eef794)\
  2017-09-19 00:25:34 +0300
  * 5.5.57-38.9
* [Revision #d947d1bf6e](https://github.com/MariaDB/server/commit/d947d1bf6e)\
  2017-08-18 13:35:40 +0300
  * Do not stop repeating a test even if some executions are skipped
* [Revision #bcc1ba9218](https://github.com/MariaDB/server/commit/bcc1ba9218)\
  2017-08-16 19:18:39 +0200
  * [MDEV-11240](https://jira.mariadb.org/browse/MDEV-11240): Server crashes in check\_view\_single\_update or Assertion \`derived->table' failed in mysql\_derived\_merge\_for\_insert
* [Revision #e866e4cdbe](https://github.com/MariaDB/server/commit/e866e4cdbe)\
  2017-08-15 20:10:04 +0300
  * MTR's internal check of main.log\_tables-big failed
* [Revision #0739179857](https://github.com/MariaDB/server/commit/0739179857)\
  2017-08-08 21:13:45 +0530
  * [MDEV-13458](https://jira.mariadb.org/browse/MDEV-13458): Wrong result for aggregate function with distinct clause when the value for tmp\_table\_size is small
* [Revision #c8a0244e95](https://github.com/MariaDB/server/commit/c8a0244e95)\
  2017-07-19 11:47:59 -0400
  * bump the VERSION
* [Revision #76f7aac8e0](https://github.com/MariaDB/server/commit/76f7aac8e0)\
  2017-07-19 15:28:13 +0530
  * [MDEV-13065](https://jira.mariadb.org/browse/MDEV-13065) rpl.rpl\_[MDEV-11092](https://jira.mariadb.org/browse/MDEV-11092) fails sporadically in buildbot

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
