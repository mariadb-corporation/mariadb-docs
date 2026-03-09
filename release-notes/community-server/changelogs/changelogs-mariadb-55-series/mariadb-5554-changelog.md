# MariaDB 5.5.54 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.54)[Release Notes](../../old-releases/5.5/5.5.54.md)[Changelog](mariadb-5554-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 24 Dec 2016

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.54.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #ec6d8da](https://github.com/MariaDB/server/commit/ec6d8da)\
  2016-12-22 13:02:32 +0100
  * reduce code duplication a little
* [Revision #e7d7910](https://github.com/MariaDB/server/commit/e7d7910)\
  2016-12-22 11:13:07 +0100
  * add an assert
* [Revision #48655ce](https://github.com/MariaDB/server/commit/48655ce)\
  2016-12-22 12:23:48 +0100
  * test case for Bug #23303485 : HANDLE\_FATAL\_SIGNAL (SIG=11) IN SUBSELECT\_UNION\_ENGINE::NO\_ROWS
* [Revision #9fefe97](https://github.com/MariaDB/server/commit/9fefe97) 2016-12-22 12:49:06 +0100 - Merge branch 'mysql/5.5' into 5.5
* [Revision #8fcdd6b](https://github.com/MariaDB/server/commit/8fcdd6b)\
  2016-12-20 21:16:23 +0100
  * Numerous issues in mysqld\_safe
* [Revision #c8e49f2](https://github.com/MariaDB/server/commit/c8e49f2)\
  2016-12-20 15:17:59 +0100
  * move check\_user/set\_user from mysqld.cc to mysys
* [Revision #706fb79](https://github.com/MariaDB/server/commit/706fb79)\
  2016-12-22 15:51:37 +0530
  * [MDEV-10927](https://jira.mariadb.org/browse/MDEV-10927): Crash When Using sort\_union Optimization
* [Revision #5e051bfa](https://github.com/MariaDB/server/commit/5e051bfa)\
  2016-12-21 15:39:45 +0400
  * [MDEV-10386](https://jira.mariadb.org/browse/MDEV-10386) Assertion \`fixed == 1' failed in virtual String\* Item\_func\_conv\_charset::val\_str(String\*)
* [Revision #ef82fd8](https://github.com/MariaDB/server/commit/ef82fd8)\
  2016-12-20 17:42:08 +0400
  * [MDEV-11353](https://jira.mariadb.org/browse/MDEV-11353) - Identical logical conditions
* [Revision #cbd7548](https://github.com/MariaDB/server/commit/cbd7548)\
  2016-12-08 23:27:04 +0530
  * [MDEV-11353](https://jira.mariadb.org/browse/MDEV-11353): fixes Identical logical conditions
* [Revision #e025ebc](https://github.com/MariaDB/server/commit/e025ebc)\
  2016-12-20 12:45:48 +0000
  * Fix pointer formatting in crash handler output.
* [Revision #aaff3d6](https://github.com/MariaDB/server/commit/aaff3d6)\
  2016-12-20 10:25:25 +0100
  * [MDEV-10172](https://jira.mariadb.org/browse/MDEV-10172): UNION query returns incorrect rows outside conditional evaluation
* [Revision #f23b41b](https://github.com/MariaDB/server/commit/f23b41b)\
  2016-12-16 17:16:02 +0300
  * [MDEV-10148](https://jira.mariadb.org/browse/MDEV-10148): Database crashes in the query to the View
* [Revision #268bb69](https://github.com/MariaDB/server/commit/268bb69)\
  2016-12-16 17:08:31 +0300
  * [MDEV-7691](https://jira.mariadb.org/browse/MDEV-7691): Assertion \`outer\_context || !\*from\_field || \*from\_field == not\_found\_field' ...
* [Revision #19896d4](https://github.com/MariaDB/server/commit/19896d4)\
  2016-12-19 16:09:20 +0400
  * [MDEV-10274](https://jira.mariadb.org/browse/MDEV-10274) Bundling insert with create statement for table with unsigned Decimal primary key issues warning 1194.
* [Revision #2f6fede](https://github.com/MariaDB/server/commit/2f6fede)\
  2016-12-19 14:28:08 +0400
  * [MDEV-10524](https://jira.mariadb.org/browse/MDEV-10524) Assertion \`arg1\_int >= 0' failed in Item\_func\_additive\_op::result\_precision()
* [Revision #c4d9dc70](https://github.com/MariaDB/server/commit/c4d9dc70)\
  2016-12-16 14:44:08 +0200
  * Typo, update limit in comment
* [Revision #b2b210b](https://github.com/MariaDB/server/commit/b2b210b)\
  2016-12-16 17:42:21 +0100
  * [MDEV-11543](https://jira.mariadb.org/browse/MDEV-11543) Buildbot tests fail with warnings on server shutdown after rpl.rpl\_row\_mysqlbinlog
* [Revision #b03b38d](https://github.com/MariaDB/server/commit/b03b38d)\
  2016-12-16 10:10:08 +0100
  * cleanup: rpl.rpl\_row\_mysqlbinlog
* [Revision #e86580c](https://github.com/MariaDB/server/commit/e86580c)\
  2016-12-15 18:20:58 +0100
  * [MDEV-11552](https://jira.mariadb.org/browse/MDEV-11552) Queries executed by event scheduler are written to slow log incorrectly or not written at all
* [Revision #211cf93](https://github.com/MariaDB/server/commit/211cf93)\
  2016-12-16 18:37:11 +0400
  * [MDEV-11510](https://jira.mariadb.org/browse/MDEV-11510) Audit plugin sometimes causes server to crash when using with MySQL.
* [Revision #14e1f32](https://github.com/MariaDB/server/commit/14e1f32)\
  2016-12-11 00:50:00 +0200
  * Follow-up for 02d153c7b9 (str2decimal: don't return a negative zero)
* [Revision #03dabfa](https://github.com/MariaDB/server/commit/03dabfa)\
  2016-12-08 22:54:58 +0100
  * [MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in handler::increment\_statistics or in make\_select or assertion failure pfs\_thread == ((PFS\_thread\*) pthread\_getspecific((THR\_PFS)))
* [Revision #ab65db6](https://github.com/MariaDB/server/commit/ab65db6)\
  2016-12-08 21:03:45 +0100
  * Revert "[MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in handler::increment\_statistics or in make\_select or assertion failure pfs\_thread == ((PFS\_thread\*) pthread\_getspecific((THR\_PFS)))"
* [Revision #f5e0522](https://github.com/MariaDB/server/commit/f5e0522)\
  2016-12-07 13:06:14 +0100
  * [MDEV-10388](https://jira.mariadb.org/browse/MDEV-10388) [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md).x keeps (deleted) ML\* files in tmpdir after LOAD DATA completes
* [Revision #1d702ff](https://github.com/MariaDB/server/commit/1d702ff)\
  2016-12-07 14:42:08 +0400
  * [MDEV-8329](https://jira.mariadb.org/browse/MDEV-8329) MariaDB crashes when replicate\_wild\_ignore\_table is set to NULL.
* [Revision #d67ef7a](https://github.com/MariaDB/server/commit/d67ef7a)\
  2016-12-05 17:37:54 +0100
  * [MDEV-10663](https://jira.mariadb.org/browse/MDEV-10663): Use of Inline table columns in HAVING clause throws 1463 Error
* [Revision #035a5ac](https://github.com/MariaDB/server/commit/035a5ac)\
  2016-09-26 18:15:11 +0200
  * [MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in handler::increment\_statistics or in make\_select or assertion failure pfs\_thread == ((PFS\_thread\*) pthread\_getspecific((THR\_PFS)))
* [Revision #f988bce](https://github.com/MariaDB/server/commit/f988bce)\
  2016-09-21 18:36:34 +0200
  * [MDEV-10776](https://jira.mariadb.org/browse/MDEV-10776): Server crash on query
* [Revision #46dee0d](https://github.com/MariaDB/server/commit/46dee0d)\
  2016-12-05 16:50:12 +0400
  * [MDEV-10717](https://jira.mariadb.org/browse/MDEV-10717) Assertion \`!null\_value' failed in virtual bool Item::send(Protocol\*, String\*)
* [Revision #18cdff6](https://github.com/MariaDB/server/commit/18cdff6)\
  2016-12-04 12:37:01 +0100
  * [MDEV-10293](https://jira.mariadb.org/browse/MDEV-10293) 'setupterm' was not declared in this scope
* [Revision #02d153c](https://github.com/MariaDB/server/commit/02d153c)\
  2016-06-26 13:37:27 +0200
  * str2decimal: don't return a negative zero
* [Revision #4a3acbc](https://github.com/MariaDB/server/commit/4a3acbc)\
  2016-12-02 00:19:49 +0100
  * [MDEV-11241](https://jira.mariadb.org/browse/MDEV-11241) Certain combining marks cause MariaDB to crash when doing Full-Text searches
* [Revision #0a4b508](https://github.com/MariaDB/server/commit/0a4b508)\
  2016-12-01 20:04:36 +0100
  * [MDEV-11242](https://jira.mariadb.org/browse/MDEV-11242) MariaDB Server releases contains promotion of MariaDB Corporation
* [Revision #f640527](https://github.com/MariaDB/server/commit/f640527)\
  2016-12-02 15:22:11 +0100
  * typo fixed: s/MSYQL/MYSQL/
* [Revision #9976223](https://github.com/MariaDB/server/commit/9976223)\
  2016-11-28 17:28:37 +0400
  * [MDEV-11171](https://jira.mariadb.org/browse/MDEV-11171) Assertion \`m\_cpp\_buf <= ptr && ptr <= m\_cpp\_buf + m\_buf\_length' failed in Lex\_input\_stream::body\_utf8\_append(const char\*, const char\*)
* [Revision #adc38ed](https://github.com/MariaDB/server/commit/adc38ed)\
  2016-11-14 08:02:35 +0100
  * Restore MY\_WME flag for my\_pread in read\_ddl\_log\_entry, fix errors in buildbot
* [Revision #96b62b5](https://github.com/MariaDB/server/commit/96b62b5)\
  2016-11-11 20:55:03 -0800
  * Fixed bug [MDEV-11161](https://jira.mariadb.org/browse/MDEV-11161). The flag TABLE\_LIST::fill\_me must be reset to false at the prepare phase for any materialized derived table used in the executed query. Otherwise if the optimizer decides to generate a key for such a table it is generated only for the first execution of the query.
* [Revision #10aee66](https://github.com/MariaDB/server/commit/10aee66)\
  2016-11-10 23:47:42 +0000
  * [MDEV-11248](https://jira.mariadb.org/browse/MDEV-11248) Fix passing offset parameter to my\_file\_pread in read\_ddl\_log\_file\_entry
* [Revision #e0f48e5](https://github.com/MariaDB/server/commit/e0f48e5)\
  2016-11-03 16:21:48 +0000
  * [MDEV-11214](https://jira.mariadb.org/browse/MDEV-11214) Windows : MSI installation fails, if run by a service user (e.g LocalSystem)
* [Revision #2a2e79b](https://github.com/MariaDB/server/commit/2a2e79b)\
  2016-10-27 13:03:49 +0000
  * [MDEV-11157](https://jira.mariadb.org/browse/MDEV-11157) Windows - Upgrade installer to use HeidiSQL 9.4
* [Revision #d8cb682](https://github.com/MariaDB/server/commit/d8cb682)\
  2016-10-26 21:54:41 +0000
  * VS2015 build fixes
* [Revision #aec4321](https://github.com/MariaDB/server/commit/aec4321)\
  2016-10-26 21:38:58 +0000
  * [MDEV-9409](https://jira.mariadb.org/browse/MDEV-9409) Windows - workaround VS2015 CRT bug that makes mysqldump/mysql\_install\_db.exe fail
* [Revision #6e25727](https://github.com/MariaDB/server/commit/6e25727)\
  2016-10-17 11:43:47 -0400
  * bump the VERSION
* [Revision #df87be5](https://github.com/MariaDB/server/commit/df87be5)\
  2016-10-17 14:04:45 +0300
  * [MDEV-11069](https://jira.mariadb.org/browse/MDEV-11069) main.information\_schema test fails if hostname includes 'user'

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
