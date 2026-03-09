# MariaDB 5.5.49 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.49)[Release Notes](../../old-releases/5.5/5.5.49.md)[Changelog](mariadb-5549-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 22 Apr 2016

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.49.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #0991e19e](https://github.com/MariaDB/server/commit/0991e19e) 2016-04-20 20:25:46 +0200 - Merge branch 'bb-5.5-serg' into 5.5
* [Revision #63c834e](https://github.com/MariaDB/server/commit/63c834e) 2016-04-20 18:56:41 +0200 - Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #c9e56d5](https://github.com/MariaDB/server/commit/c9e56d5)\
  2016-04-18 17:38:05 +0200
  * 5.5.48-37.8
* [Revision #24ac546](https://github.com/MariaDB/server/commit/24ac546)\
  2016-04-20 18:27:23 +0200
  * use consistent error messaging for IGNORE
* [Revision #9e826bf](https://github.com/MariaDB/server/commit/9e826bf)\
  2016-04-20 15:28:44 +0200
  * trivial optimization
* [Revision #8f1f869](https://github.com/MariaDB/server/commit/8f1f869)\
  2016-04-20 15:26:37 +0200
  * another test case for ER\_DATA\_OUT\_OF\_RANGE on insert
* [Revision #b069d19](https://github.com/MariaDB/server/commit/b069d19) 2016-04-20 15:25:55 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #1bc0b0b](https://github.com/MariaDB/server/commit/1bc0b0b)\
  2016-04-19 11:08:16 +0200
  * fix a couple of dbug tests not to write to /tmp
* [Revision #cc04a9f](https://github.com/MariaDB/server/commit/cc04a9f)\
  2016-04-18 18:30:42 +0200
  * [MDEV-9835](https://jira.mariadb.org/browse/MDEV-9835) Valid password is not working after server restart
* [Revision #608c0e1](https://github.com/MariaDB/server/commit/608c0e1)\
  2016-04-18 11:57:34 +0200
  * [MDEV-5982](https://jira.mariadb.org/browse/MDEV-5982) `make` fail @ ".../libmysql\_versions.ld:155:9: invalid use of VERSION in input file"
* [Revision #ce35530](https://github.com/MariaDB/server/commit/ce35530)\
  2016-04-17 19:52:15 +0200
  * [MDEV-9885](https://jira.mariadb.org/browse/MDEV-9885) Client doesn't start if 'TERM' unknown
* [Revision #95fe71a](https://github.com/MariaDB/server/commit/95fe71a)\
  2016-04-17 18:51:54 +0200
  * [MDEV-9707](https://jira.mariadb.org/browse/MDEV-9707) MAX(timestamp(6) column) in correlated sub-query returns non-existent row data in original table
* [Revision #3294cd1](https://github.com/MariaDB/server/commit/3294cd1)\
  2016-04-16 17:36:47 +0200
  * [MDEV-9929](https://jira.mariadb.org/browse/MDEV-9929) MariaDB segfaults on command "mysqld --version" with ignore-db-dir option on /etc/my.cnf
* [Revision #4f133fb](https://github.com/MariaDB/server/commit/4f133fb)\
  2016-04-16 12:39:20 +0200
  * [MDEV-9493](https://jira.mariadb.org/browse/MDEV-9493) --tc-heuristic-recover option values off by one
* [Revision #edf71fd](https://github.com/MariaDB/server/commit/edf71fd)\
  2016-04-16 10:28:03 +0200
  * [MDEV-9928](https://jira.mariadb.org/browse/MDEV-9928) LC\_TIME\_NAMES=de\_AT; unusual name for february
* [Revision #9c64735](https://github.com/MariaDB/server/commit/9c64735)\
  2016-03-29 12:50:56 +0200
  * [MDEV-9748](https://jira.mariadb.org/browse/MDEV-9748) Include Twin (mysys\_err.h is included twice in mysys/my\_copy.c)
* [Revision #2a45fa9](https://github.com/MariaDB/server/commit/2a45fa9)\
  2016-04-20 19:03:59 +0200
  * [MDEV-9836](https://jira.mariadb.org/browse/MDEV-9836) Connection lost when using SSL
* [Revision #0c0a865](https://github.com/MariaDB/server/commit/0c0a865)\
  2016-04-19 16:16:13 +0400
  * [MDEV-9943](https://jira.mariadb.org/browse/MDEV-9943) - TokuDB fails to compile with gcc 5.2.1
* [Revision #62122ba](https://github.com/MariaDB/server/commit/62122ba)\
  2016-04-20 00:36:58 +0300
  * [MDEV-9953](https://jira.mariadb.org/browse/MDEV-9953) Debian packages install broken 'maria' test suite which cannot be run
* [Revision #e90f8b7](https://github.com/MariaDB/server/commit/e90f8b7)\
  2016-04-20 11:11:13 +0400
  * [MDEV-9413](https://jira.mariadb.org/browse/MDEV-9413) "datetime >= coalesce(c1(NULL))" doesn't return expected NULL
* [Revision #2564650](https://github.com/MariaDB/server/commit/2564650)\
  2016-04-20 11:02:34 +0400
  * [MDEV-9662](https://jira.mariadb.org/browse/MDEV-9662) Assertion \`precision || !scale' failed in my\_decimal\_precision\_to\_length\_no\_truncation(uint, uint8, bool)
* [Revision #9a98714](https://github.com/MariaDB/server/commit/9a98714)\
  2016-04-20 08:53:30 +0400
  * [MDEV-9745](https://jira.mariadb.org/browse/MDEV-9745) Crash with CASE WHEN TRUE THEN COALESCE(CAST(NULL AS UNSIGNED)) ELSE 4 END
* [Revision #6c0e231](https://github.com/MariaDB/server/commit/6c0e231)\
  2016-04-19 14:05:52 +0400
  * [MDEV-9945](https://jira.mariadb.org/browse/MDEV-9945) - main.kill\_processlist-6619 fails sporadically
* [Revision #18ff6f6](https://github.com/MariaDB/server/commit/18ff6f6)\
  2016-04-19 12:38:00 +0400
  * [MDEV-9944](https://jira.mariadb.org/browse/MDEV-9944) - main.events\_2 fails sporadically
* [Revision #6fd54c0](https://github.com/MariaDB/server/commit/6fd54c0)\
  2016-04-18 23:15:15 +0400
  * [MDEV-9521](https://jira.mariadb.org/browse/MDEV-9521) Least function returns 0000-00-00 for null date columns instead of null
* [Revision #777c213](https://github.com/MariaDB/server/commit/777c213)\
  2016-04-02 00:04:47 +0400
  * [MDEV-9862](https://jira.mariadb.org/browse/MDEV-9862) Illegal mix of collation, when comparing column with CASE expression
* [Revision #11b77e9](https://github.com/MariaDB/server/commit/11b77e9)\
  2016-03-18 16:55:11 +0100
  * [MDEV-9527](https://jira.mariadb.org/browse/MDEV-9527) build FAILs with GCC 5.1 with release supported "-std=c+11"
* [Revision #fc2c1e4](https://github.com/MariaDB/server/commit/fc2c1e4)\
  2016-03-17 21:29:52 +0100
  * [MDEV-9733](https://jira.mariadb.org/browse/MDEV-9733) Server crashes in lf\_pinbox\_real\_free on replication slaves
* [Revision #0b9fb9a](https://github.com/MariaDB/server/commit/0b9fb9a)\
  2016-03-17 10:45:15 +0100
  * [MDEV-9568](https://jira.mariadb.org/browse/MDEV-9568) mysqlcheck crashes with nonexistent table name
* [Revision #c29e450](https://github.com/MariaDB/server/commit/c29e450)\
  2016-02-26 03:02:07 +0200
  * [MDEV-4070](https://jira.mariadb.org/browse/MDEV-4070) sys\_vars.secure\_file\_priv fails sporadically if it's executed with --mem
* [Revision #ceba41c](https://github.com/MariaDB/server/commit/ceba41c)\
  2016-01-24 17:41:11 +0100
  * [MDEV-9299](https://jira.mariadb.org/browse/MDEV-9299) Test main.events\_2 incompatible with Debian reproducibility testing framework
* [Revision #e1385f2](https://github.com/MariaDB/server/commit/e1385f2)\
  2016-02-15 12:59:47 +0100
  * fix buffer overrun
* [Revision #3889b19](https://github.com/MariaDB/server/commit/3889b19)\
  2016-02-14 22:19:27 +0100
  * more strict ipv6\_ok check in mtr
* [Revision #8f5030e](https://github.com/MariaDB/server/commit/8f5030e)\
  2016-02-14 22:17:38 +0100
  * fix my\_gethwaddr() for solaris
* [Revision #95740bc](https://github.com/MariaDB/server/commit/95740bc)\
  2016-02-14 22:16:50 +0100
  * dtrace in cmake
* [Revision #a5d9597](https://github.com/MariaDB/server/commit/a5d9597)\
  2016-02-14 22:15:16 +0100
  * better inline check
* [Revision #5f078cc](https://github.com/MariaDB/server/commit/5f078cc)\
  2016-02-14 20:57:48 +0100
  * compilation errors on sparc sun studio 10
* [Revision #2a47817](https://github.com/MariaDB/server/commit/2a47817)\
  2016-02-14 18:33:20 +0200
  * [MDEV-9225](https://jira.mariadb.org/browse/MDEV-9225) mysql\_upgrade segfault due to missing /etc/my.cnf.d
* [Revision #b7dc830](https://github.com/MariaDB/server/commit/b7dc830)\
  2016-02-14 18:31:06 +0200
  * Fix memory leak when failing to read config file
* [Revision #93e9d81](https://github.com/MariaDB/server/commit/93e9d81)\
  2016-02-12 12:04:11 +0400
  * Errorneous PSI declaration line fixed.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
