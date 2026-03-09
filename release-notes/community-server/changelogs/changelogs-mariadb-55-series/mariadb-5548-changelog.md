# MariaDB 5.5.48 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.48)[Release Notes](../../old-releases/5.5/5.5.48.md)[Changelog](mariadb-5548-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 11 Feb 2016

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.48.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #a9a08b1](https://github.com/MariaDB/server/commit/a9a08b1)\
  2016-02-10 10:03:47 +0400
  * [MDEV-9371](https://jira.mariadb.org/browse/MDEV-9371) select insert('a',2,1,'b') doesn't return expected 'a'
* [Revision #3c5c04b](https://github.com/MariaDB/server/commit/3c5c04b)\
  2016-02-10 03:49:11 +0200
  * [MDEV-7122](https://jira.mariadb.org/browse/MDEV-7122): Assertion \`0' failed in subselect\_hash\_sj\_engine::init
* [Revision #6b614c6](https://github.com/MariaDB/server/commit/6b614c6)\
  2016-02-09 13:50:48 +0100
  * [MDEV-7765](https://jira.mariadb.org/browse/MDEV-7765): Crash (Assertion \`!table || (!table->write\_set || bitmap\_is\_set(table->write\_set, field\_index) || bitmap\_is\_set(table->vcol\_set, field\_index))' fails) on using function over not created table
* [Revision #775cccc](https://github.com/MariaDB/server/commit/775cccc)\
  2016-02-08 22:53:40 +0200
  * [MDEV-7122](https://jira.mariadb.org/browse/MDEV-7122): Assertion \`0' failed in subselect\_hash\_sj\_engine::init
* [Revision #01628ce](https://github.com/MariaDB/server/commit/01628ce)\
  2016-02-09 14:08:36 +0100
  * Merge branch 'bb-5.5-serg' into 5.5
* [Revision #afce541](https://github.com/MariaDB/server/commit/afce541)\
  2016-02-09 14:06:45 +0100
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #5d478f5](https://github.com/MariaDB/server/commit/5d478f5)\
  2016-02-08 20:07:38 +0100
  * Bug#19817021
* [Revision #6703e5b](https://github.com/MariaDB/server/commit/6703e5b)\
  2016-02-08 20:07:09 +0100
  * Bug#20691429 ASSERTION \`CHILD\_L' FAILED IN STORAGE/MYISAMMRG/HA\_MYISAMMRG.CC:631
* [Revision #dece4bc](https://github.com/MariaDB/server/commit/dece4bc)\
  2016-02-09 11:28:44 +0100
  * cleanup: make assert more readable
* [Revision #63d3ccd](https://github.com/MariaDB/server/commit/63d3ccd)\
  2016-02-08 20:04:39 +0100
  * Bug#21205695 DROP TABLE MAY CAUSE SLAVES TO BREAK
* [Revision #f3444df](https://github.com/MariaDB/server/commit/f3444df)\
  2016-02-09 11:27:40 +0100
  * Merge branch 'mysql/5.5' into 5.5
* [Revision #ea0c3fc](https://github.com/MariaDB/server/commit/ea0c3fc)\
  2016-02-09 05:17:41 +0400
  * [MDEV-9438](https://jira.mariadb.org/browse/MDEV-9438) backport feedback-http-proxy to 5.5 and 10.0. The http-proxy option to the FEEDBACK plugin backported.
* [Revision #b17a435](https://github.com/MariaDB/server/commit/b17a435)\
  2016-02-09 02:31:47 +0300
  * [MDEV-6859](https://jira.mariadb.org/browse/MDEV-6859): scalar subqueries in a comparison produced unexpected result
* [Revision #3cfd36b](https://github.com/MariaDB/server/commit/3cfd36b)\
  2016-02-09 00:13:25 +0100
  * 5.5.47-37.7
* [Revision #d443d70](https://github.com/MariaDB/server/commit/d443d70)\
  2016-02-09 01:46:53 +0300
  * [MDEV-7823](https://jira.mariadb.org/browse/MDEV-7823): Server crashes in next\_depth\_first\_tab on nested IN clauses with SQ inside
* [Revision #c4cb240](https://github.com/MariaDB/server/commit/c4cb240)\
  2016-02-06 22:41:58 +0100
  * [MDEV-9024](https://jira.mariadb.org/browse/MDEV-9024) Build fails with VS2015
* [Revision #1e361f2](https://github.com/MariaDB/server/commit/1e361f2)\
  2016-02-06 13:57:59 +0100
  * [MDEV-4664](https://jira.mariadb.org/browse/MDEV-4664) mysql\_upgrade crashes if root's password contains an apostrophe/single quotation mark
* [Revision #9e4e412](https://github.com/MariaDB/server/commit/9e4e412)\
  2016-02-06 13:56:37 +0100
  * unit test for dynstr\_append\_os\_quoted()
* [Revision #41021c0](https://github.com/MariaDB/server/commit/41021c0)\
  2016-02-03 17:15:22 +0100
  * [MDEV-9462](https://jira.mariadb.org/browse/MDEV-9462): Out of memory using explain on 2 empty tables
* [Revision #ad94790](https://github.com/MariaDB/server/commit/ad94790)\
  2016-02-04 14:47:46 +0100
  * [MDEV-9453](https://jira.mariadb.org/browse/MDEV-9453) mysql\_upgrade.exe error when mysql is migrated to mariadb
* [Revision #0a76ad5](https://github.com/MariaDB/server/commit/0a76ad5)\
  2016-02-04 12:51:57 +0100
  * [MDEV-9175](https://jira.mariadb.org/browse/MDEV-9175) Query parser tansforms MICROSECOND into SECOND\_FRAC, which does not work
* [Revision #a90da6e](https://github.com/MariaDB/server/commit/a90da6e)\
  2016-02-05 14:04:24 +0100
  * [MDEV-9314](https://jira.mariadb.org/browse/MDEV-9314) fatal build error: viosslfactories.c:58:5: error: dereferencing pointer to incomplete type ‘DH {aka struct dh\_st}
* [Revision #db5f743](https://github.com/MariaDB/server/commit/db5f743)\
  2016-02-06 12:37:46 +0200
  * Merge pull request #148 from grooverdan/5.5-rpl\_reporting-cppcheck-va\_end
* [Revision #6ecf6d8](https://github.com/MariaDB/server/commit/6ecf6d8)\
  2016-02-05 17:46:01 +0100
  * [MDEV-7827](https://jira.mariadb.org/browse/MDEV-7827): Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index))' failed in Field\_long::val\_str on EXPLAIN EXTENDED
* [Revision #9f3b53f](https://github.com/MariaDB/server/commit/9f3b53f)\
  2015-12-14 19:16:29 +0100
  * [MDEV-9093](https://jira.mariadb.org/browse/MDEV-9093) Persistent computed column is not updated when update query contains join
* [Revision #a3d843d](https://github.com/MariaDB/server/commit/a3d843d)\
  2016-02-03 15:52:26 +0200
  * Fix function visibility as it is used on row0mysql.c in Windows.
* [Revision #f66d016](https://github.com/MariaDB/server/commit/f66d016)\
  2016-02-03 11:32:51 +0200
  * [MDEV-9471](https://jira.mariadb.org/browse/MDEV-9471): Server crashes or returns an error while trying to alter partitioning on a table moved from Windows to Linux
* [Revision #603c096](https://github.com/MariaDB/server/commit/603c096)\
  2016-02-03 00:43:00 +0100
  * [MDEV-9466](https://jira.mariadb.org/browse/MDEV-9466) : Exception handler on Windows does not output any text, if mysqld runs as service
* [Revision #0e84d54](https://github.com/MariaDB/server/commit/0e84d54)\
  2016-02-01 16:27:12 +0100
  * Merge [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112) into 5.5
* [Revision #8cf1f50](https://github.com/MariaDB/server/commit/8cf1f50)\
  2016-02-01 16:10:49 +0100
  * [MDEV-9112](https://jira.mariadb.org/browse/MDEV-9112): Non-blocking client API missing on non-x86 platforms
* [Revision #d0c5efc](https://github.com/MariaDB/server/commit/d0c5efc)\
  2016-01-29 23:53:44 +0200
  * If one compiled with too long MYSQL\_SERVER\_SUFFIX this caused a memory overrun that caused some test to fail.
* [Revision #a1ddf01](https://github.com/MariaDB/server/commit/a1ddf01)\
  2016-01-29 23:52:15 +0200
  * my\_decimal didn't compile properly with debug
* [Revision #3e5724f](https://github.com/MariaDB/server/commit/3e5724f)\
  2016-01-19 14:47:41 +1100
  * Add va\_end to make cppcheck happy
* [Revision #9c9d10b](https://github.com/MariaDB/server/commit/9c9d10b)\
  2016-01-15 09:50:27 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin not working with MySQL 5.7. fixing Windows crash.
* [Revision #fe4823d](https://github.com/MariaDB/server/commit/fe4823d)\
  2016-01-13 18:02:44 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin doesnt run with MySQL 5.7. updata thread\_pool\_server\_audit test result.
* [Revision #cdc9aa5](https://github.com/MariaDB/server/commit/cdc9aa5)\
  2016-01-13 15:24:33 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit Plugin doesn't run with MySQL 5.7. [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) built in debug gets unhappy with mutexes. Although everything is correct, some DBUG\_ASSERT can happen. So this patch keeps safe\_mutex silent.
* [Revision #c955253](https://github.com/MariaDB/server/commit/c955253)\
  2016-01-12 16:29:02 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin compiled with MariaDB can't install on MySQL 5.7. The audit API was seriously changed in MySQL 5.7. so we had to adapt the plugin's code to that.
* [Revision #5f48b61](https://github.com/MariaDB/server/commit/5f48b61)\
  2016-01-07 14:45:40 +0100
  * [MDEV-9298](https://jira.mariadb.org/browse/MDEV-9298) : Build failure when linking libmysql.
* [Revision #ff24820](https://github.com/MariaDB/server/commit/ff24820)\
  2015-12-30 19:39:31 +0100
  * Fix process handle leak in buildbot. GenerateConsoleCtrlEvent sent to non-existing process will add a process handle to this non-existing process to console host process conhost.exe
* [Revision #61d3621](https://github.com/MariaDB/server/commit/61d3621)\
  2015-12-29 18:40:41 +0400
  * Moving Field\_blob::store\_length() back from protected to public, as it's needed for Cassandra in 10.0.
* [Revision #e1b9be5](https://github.com/MariaDB/server/commit/e1b9be5)\
  2015-12-29 14:17:31 +0400
  * [MDEV-9319](https://jira.mariadb.org/browse/MDEV-9319) ALTER from a bigger to a smaller blob type truncates too much data
* [Revision #e126baa](https://github.com/MariaDB/server/commit/e126baa)\
  2015-12-21 10:19:02 +0100
  * [MDEV-9249](https://jira.mariadb.org/browse/MDEV-9249) MariaDB un-buildable on linux64: fails @ "error: ‘ERR\_remove\_state’ was not declared in this scope" when linking against OpenSSL 1.0.2e
* [Revision #591e74c](https://github.com/MariaDB/server/commit/591e74c)\
  2015-06-20 16:59:22 +0800
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #e386523](https://github.com/MariaDB/server/commit/e386523)\
  2015-12-19 13:53:43 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #f39b9e0](https://github.com/MariaDB/server/commit/f39b9e0)\
  2015-12-19 13:52:27 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #6414959](https://github.com/MariaDB/server/commit/6414959)\
  2015-12-19 13:31:44 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #f89c9fc](https://github.com/MariaDB/server/commit/f89c9fc)\
  2015-12-19 13:25:55 +0200
  * [MDEV-7526](https://jira.mariadb.org/browse/MDEV-7526): TokuDB doesn't build on OS X
* [Revision #0ed4744](https://github.com/MariaDB/server/commit/0ed4744)\
  2015-12-11 17:03:55 +0100
  * fix main.mysqldump test on windows
* [Revision #ca28d90](https://github.com/MariaDB/server/commit/ca28d90)\
  2015-12-09 17:54:55 +0100
  * [MDEV-7655](https://jira.mariadb.org/browse/MDEV-7655) SHOW CREATE TABLE returns invalid DDL when using virtual columns along with a table collation
* [Revision #f560c1b](https://github.com/MariaDB/server/commit/f560c1b)\
  2015-12-10 10:32:11 +0100
  * revert 5e9a50efc37c233f1e2a3616f8bcb36315aba4c2
* [Revision #265e833](https://github.com/MariaDB/server/commit/265e833)\
  2015-12-09 21:22:37 +0100
  * revert 415faa122b9c683661dafac82fff414fa6864151
* [Revision #c19972f](https://github.com/MariaDB/server/commit/c19972f)\
  2015-12-11 14:33:41 +0200
  * [MDEV-9251](https://jira.mariadb.org/browse/MDEV-9251): Fix MySQL Bug#20755615: InnoDB compares column names case sensitively, while according to Storage Engine API column names should be compared case insensitively. This can cause FRM and InnoDB data dictionary to go out of sync.
* [Revision #fa25921](https://github.com/MariaDB/server/commit/fa25921)\
  2015-12-10 11:22:53 +0100
  * [MDEV-8407](https://jira.mariadb.org/browse/MDEV-8407) Numeric errors, server crash with COLUMN\_JSON() on DECIMAL with precision > 40

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
