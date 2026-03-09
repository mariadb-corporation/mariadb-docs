# MariaDB 10.1.45 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.45/)[Release Notes](../../old-releases/10.1/10.1.45.md)[Changelog](mariadb-10145-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 12 May 2020

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.45.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 5.5.68](../changelogs-mariadb-55-series/mariadb-5568-changelog.md)
* [Revision #530da97c65](https://github.com/MariaDB/server/commit/530da97c65)\
  2020-05-08 09:14:34 +0200
  * cleanup: foreign-keys.test vs foreign\_key.test
* [Revision #6b521ac003](https://github.com/MariaDB/server/commit/6b521ac003)\
  2020-05-08 01:52:31 +0200
  * [MDEV-22180](https://jira.mariadb.org/browse/MDEV-22180) Planner opens unnecessary tables when updated table is referenced by foreign keys
* [Revision #0fcc3abf4a](https://github.com/MariaDB/server/commit/0fcc3abf4a)\
  2020-05-05 14:55:05 +0200
  * [MDEV-22180](https://jira.mariadb.org/browse/MDEV-22180) Planner opens unnecessary tables when updated table is referenced by foreign keys
* Merge [Revision #10aaa77509](https://github.com/MariaDB/server/commit/10aaa77509) 2020-05-06 20:24:08 +0200 - Merge branch '5.5' into 10.1
* [Revision #9c5d06a6d3](https://github.com/MariaDB/server/commit/9c5d06a6d3)\
  2020-05-05 13:11:52 +0200
  * [MDEV-21437](https://jira.mariadb.org/browse/MDEV-21437) MariaDB's SUSE/SLES packages don't "provide" all of the same capabilities as the platform's default packages
* [Revision #ccb58b955e](https://github.com/MariaDB/server/commit/ccb58b955e)\
  2020-05-04 17:20:17 +0300
  * List of unstable tests for 10.1.45 release
* [Revision #2748c4993c](https://github.com/MariaDB/server/commit/2748c4993c)\
  2020-05-04 13:42:38 +0530
  * [MDEV-19092](https://jira.mariadb.org/browse/MDEV-19092) Server crash when renaming the column when FOREIGN\_KEY\_CHECKS is disabled
* Merge [Revision #d233fd14a3](https://github.com/MariaDB/server/commit/d233fd14a3) 2020-04-30 21:27:32 +0200 - Merge branch 'merge-pcre' into 10.1
* [Revision #c1291d7a6b](https://github.com/MariaDB/server/commit/c1291d7a6b)\
  2020-04-30 18:40:02 +0200
  * 8.44
* Merge [Revision #4fc8961d49](https://github.com/MariaDB/server/commit/4fc8961d49) 2020-04-30 18:57:45 +0200 - Merge remote-tracking branch 'connect/10.1' into 10.1
* [Revision #41acc81f4d](https://github.com/MariaDB/server/commit/41acc81f4d)\
  2020-03-11 23:14:19 +0100
  * Fix [60637429#60637429](https://stackoverflow.com/questions/60625778/import-complex-xml-from-multiple-files-in-mariadb/60637429#60637429) Import complex XML from multiple files in MariaDB Some row results are missing and replaced by the last file one. Thats because Nx and Sx column members are not reset when changing file.
* Merge [Revision #da1fbcb665](https://github.com/MariaDB/server/commit/da1fbcb665) 2020-04-30 18:56:55 +0200 - Merge branch 'merge-tokudb-5.6' into 10.1
* [Revision #15db581ecb](https://github.com/MariaDB/server/commit/15db581ecb)\
  2020-04-30 18:29:36 +0200
  * 5.6.47-87.0
* Merge [Revision #23c6fb3e62](https://github.com/MariaDB/server/commit/23c6fb3e62) 2020-04-30 17:36:41 +0200 - Merge branch '5.5' into 10.1
* [Revision #de8c9b538f](https://github.com/MariaDB/server/commit/de8c9b538f)\
  2020-04-30 12:03:24 +1000
  * mysql-test-run.pl - fix strict subs in HAVE\_WIN32\_CONSOLE (#1521)
* [Revision #9b744ea0d3](https://github.com/MariaDB/server/commit/9b744ea0d3)\
  2020-04-30 01:21:44 +0200
  * [MDEV-22419](https://jira.mariadb.org/browse/MDEV-22419) update windows timezone data from using newest ICU source
* [Revision #e3f5789ac0](https://github.com/MariaDB/server/commit/e3f5789ac0)\
  2020-04-29 22:39:44 +0200
  * mysql-test-run.pl - show remaining test count and estimated time on Windows
* [Revision #946c879521](https://github.com/MariaDB/server/commit/946c879521)\
  2020-04-29 13:40:54 +1000
  * vio: typo on sock{et}\_errno in comment
* Merge [Revision #713e427b2e](https://github.com/MariaDB/server/commit/713e427b2e) 2020-04-28 16:20:19 +0300 - InnoDB 5.6.48
* [Revision #7041807476](https://github.com/MariaDB/server/commit/7041807476)\
  2020-04-28 14:51:25 +0300
  * [MDEV-22393](https://jira.mariadb.org/browse/MDEV-22393) Corruption for SET GLOBAL innodb\_ string variables
* [Revision #cce1b6e245](https://github.com/MariaDB/server/commit/cce1b6e245)\
  2020-04-28 11:46:29 +0300
  * [MDEV-22392](https://jira.mariadb.org/browse/MDEV-22392) Race condition on SET GLOBAL innodb\_buffer\_pool\_evict='uncompressed'
* [Revision #cf64d27bad](https://github.com/MariaDB/server/commit/cf64d27bad)\
  2020-04-28 11:40:04 +0300
  * Remove a duplicated copyright message
* [Revision #d956175d0d](https://github.com/MariaDB/server/commit/d956175d0d)\
  2020-04-27 11:39:46 +0300
  * XtraDB 5.6.47-87.0
* [Revision #edbdfc2f99](https://github.com/MariaDB/server/commit/edbdfc2f99)\
  2020-04-27 11:18:11 +0300
  * [MDEV-7962](https://jira.mariadb.org/browse/MDEV-7962) wsrep\_on() takes 0.14% in OLTP RO
* [Revision #dd4124c224](https://github.com/MariaDB/server/commit/dd4124c224)\
  2020-04-22 13:21:43 +0200
  * [MDEV-22271](https://jira.mariadb.org/browse/MDEV-22271) Excessive stack memory usage due to WSREP\_LOG
* [Revision #f462fbac61](https://github.com/MariaDB/server/commit/f462fbac61)\
  2020-04-21 22:57:54 +0200
  * [MDEV-22078](https://jira.mariadb.org/browse/MDEV-22078) MariaDB-compat missing from [MariaDB 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series) CentOS 8 Yum Repo
* [Revision #6be05ceb05](https://github.com/MariaDB/server/commit/6be05ceb05)\
  2020-04-27 09:40:51 +0300
  * [MDEV-22203](https://jira.mariadb.org/browse/MDEV-22203): WSREP\_ON is unnecessarily expensive to evaluate
* [Revision #758fbec6e3](https://github.com/MariaDB/server/commit/758fbec6e3)\
  2020-03-13 08:37:22 +0200
  * Fix clang 10 warnings
* [Revision #6a3fc1101c](https://github.com/MariaDB/server/commit/6a3fc1101c)\
  2020-04-27 09:40:10 +0300
  * Aria: Avoid unused variables in embedded server
* [Revision #d28ee189b7](https://github.com/MariaDB/server/commit/d28ee189b7)\
  2020-04-27 09:36:31 +0300
  * [MDEV-22271](https://jira.mariadb.org/browse/MDEV-22271): Follow-up fix of --embedded
* [Revision #5d856760fb](https://github.com/MariaDB/server/commit/5d856760fb)\
  2020-04-23 04:49:24 +0300
  * [MDEV-22349](https://jira.mariadb.org/browse/MDEV-22349) MTR re-bootstrap modifies environment variable MYSQLD\_BOOTSTRAP\_CMD
* [Revision #ad4b70562b](https://github.com/MariaDB/server/commit/ad4b70562b)\
  2020-04-17 11:59:23 +0300
  * Fix GCC 10 -Woverflow
* [Revision #7198c6ab2d](https://github.com/MariaDB/server/commit/7198c6ab2d)\
  2020-04-17 10:49:07 +0300
  * [MDEV-22271](https://jira.mariadb.org/browse/MDEV-22271) Excessive stack memory usage due to WSREP\_LOG
* Merge [Revision #18656797de](https://github.com/MariaDB/server/commit/18656797de) 2020-04-16 14:46:16 +0530 - Merge branch '5.5' into 10.1
* [Revision #f8166a05af](https://github.com/MariaDB/server/commit/f8166a05af)\
  2020-04-15 14:51:49 +0300
  * [MDEV-21549](https://jira.mariadb.org/browse/MDEV-21549) IMPORT TABLESPACE fails to adjust all tablespace ID in root pages
* [Revision #a215e2132d](https://github.com/MariaDB/server/commit/a215e2132d)\
  2020-04-15 14:47:56 +0300
  * mbstream: Remove duplicate definition of datasink\_buffer
* [Revision #ae688808fa](https://github.com/MariaDB/server/commit/ae688808fa)\
  2020-03-31 11:39:36 +1100
  * mtr: Only old windows patch-2.5.9 needs --binary
* Merge [Revision #26f0cd8afc](https://github.com/MariaDB/server/commit/26f0cd8afc) 2020-04-14 15:43:12 +0300 - Merge 5.5 into 10.1
* [Revision #0b7a79c6b0](https://github.com/MariaDB/server/commit/0b7a79c6b0)\
  2020-04-13 16:25:32 +0300
  * Revert "mtr: remove --binary from patch args"
* [Revision #613bc18a36](https://github.com/MariaDB/server/commit/613bc18a36)\
  2020-04-13 14:22:58 +0300
  * sysvars\_server\_\* tests need to have performance schema enabled
* [Revision #7937fed917](https://github.com/MariaDB/server/commit/7937fed917)\
  2020-04-12 10:36:47 +1000
  * appveyor: config backport from 10.2
* [Revision #1749a68968](https://github.com/MariaDB/server/commit/1749a68968)\
  2020-04-12 10:31:56 +1000
  * mtr: remove --binary from patch args
* [Revision #c8e0c524af](https://github.com/MariaDB/server/commit/c8e0c524af)\
  2020-03-31 14:18:06 +0200
  * [MDEV-20676](https://jira.mariadb.org/browse/MDEV-20676): systemd script not working
* [Revision #5720db2b43](https://github.com/MariaDB/server/commit/5720db2b43)\
  2020-04-07 07:45:49 +0000
  * [MDEV-22176](https://jira.mariadb.org/browse/MDEV-22176) Add JUnit support to MTR to generate XML test result
* [Revision #241ac3f487](https://github.com/MariaDB/server/commit/241ac3f487)\
  2019-11-28 17:37:57 +0500
  * [MDEV-21140](https://jira.mariadb.org/browse/MDEV-21140) Make galera\_recovery.sh work with fs.protected\_regular = 1 (#1417)
* [Revision #31eaa2029f](https://github.com/MariaDB/server/commit/31eaa2029f)\
  2020-04-01 15:16:11 +0300
  * [MDEV-19740](https://jira.mariadb.org/browse/MDEV-19740): Have MYSQL\_MAINTAINER\_MODE only enable -Werror
* Merge [Revision #f813131c7b](https://github.com/MariaDB/server/commit/f813131c7b) 2020-04-01 10:24:36 +0300 - Merge 5.5 into 10.1
* [Revision #f9639c2d1a](https://github.com/MariaDB/server/commit/f9639c2d1a)\
  2020-03-19 15:02:09 +0100
  * [MDEV-22037](https://jira.mariadb.org/browse/MDEV-22037): Add ability to skip content of some tables (work around for [MDEV-20939](https://jira.mariadb.org/browse/MDEV-20939))
* [Revision #1f7be88141](https://github.com/MariaDB/server/commit/1f7be88141)\
  2020-03-25 17:10:01 +0530
  * [MDEV-19092](https://jira.mariadb.org/browse/MDEV-19092) Server crash when renaming the column when FOREIGN\_KEY\_CHECKS is disabled
* [Revision #64dd396948](https://github.com/MariaDB/server/commit/64dd396948)\
  2020-03-18 19:45:25 +0100
  * remove redundant info on rpl test failure
* [Revision #328edf8560](https://github.com/MariaDB/server/commit/328edf8560)\
  2020-03-20 15:24:06 +0400
  * [MDEV-21977](https://jira.mariadb.org/browse/MDEV-21977) main.func\_math fails due to undefined behaviour
* [Revision #5c1ed707a3](https://github.com/MariaDB/server/commit/5c1ed707a3)\
  2020-02-26 19:39:26 +0100
  * mtr: update heuristics for --parallel=auto
* [Revision #0fe3d6d563](https://github.com/MariaDB/server/commit/0fe3d6d563)\
  2020-02-26 12:33:16 +0100
  * all status variables above `questions` MUST be ulong
* Merge [Revision #7b082fb099](https://github.com/MariaDB/server/commit/7b082fb099) 2020-03-13 07:03:42 +0200 - Merge 5.5 into 10.1
* [Revision #7f36300df5](https://github.com/MariaDB/server/commit/7f36300df5)\
  2020-03-11 16:40:34 +0300
  * [MDEV-21918](https://jira.mariadb.org/browse/MDEV-21918) improve page\_zip\_verify\_checksum()
* [Revision #df88e7cefa](https://github.com/MariaDB/server/commit/df88e7cefa)\
  2020-03-11 16:27:37 +0300
  * fix typedef-related warning and cleanup using namespace std
* [Revision #b30446c85d](https://github.com/MariaDB/server/commit/b30446c85d)\
  2020-03-11 13:46:57 +0300
  * Fix compile warning:
* [Revision #1c40cb6877](https://github.com/MariaDB/server/commit/1c40cb6877)\
  2020-03-10 13:26:57 +0200
  * Do not bother to disable non-existing tests
* Merge [Revision #345aaca14c](https://github.com/MariaDB/server/commit/345aaca14c) 2020-03-06 11:06:48 +0100 - Merge branch '5.5' into 10.1
* [Revision #395f23a10d](https://github.com/MariaDB/server/commit/395f23a10d)\
  2020-02-28 19:54:08 +0200
  * Remove unneded extra context line from test file to make it version independent
* [Revision #f21592c675](https://github.com/MariaDB/server/commit/f21592c675)\
  2018-11-01 13:16:11 -0400
  * mariadb.pc: remove unnecessary include directory
* [Revision #cd5d864fef](https://github.com/MariaDB/server/commit/cd5d864fef)\
  2020-02-25 15:58:42 +1100
  * mariadb{,@}.service comment typo open-file-limit -> open-files-limit
* [Revision #b9689712e0](https://github.com/MariaDB/server/commit/b9689712e0)\
  2019-12-31 18:02:54 +0100
  * [MDEV-21374](https://jira.mariadb.org/browse/MDEV-21374): When "--help --verbose" prints out configuration file paths, the --defaults-file option is not considered
* Merge [Revision #716161ea03](https://github.com/MariaDB/server/commit/716161ea03) 2020-02-10 14:18:00 +0100 - Merge branch '5.5' into 10.1
* [Revision #e568dc9723](https://github.com/MariaDB/server/commit/e568dc9723)\
  2020-02-08 18:58:28 +0200
  * Remove unused SRV\_MASTER\_PURGE\_INTERVAL
* [Revision #80da232576](https://github.com/MariaDB/server/commit/80da232576)\
  2020-02-07 15:22:16 +0530
  * [MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563) FTS thread aborts during shutdown
* [Revision #280bf17829](https://github.com/MariaDB/server/commit/280bf17829)\
  2020-02-06 20:42:29 +0530
  * [MDEV-21563](https://jira.mariadb.org/browse/MDEV-21563) FTS thread aborts during shutdown
* [Revision #0b36c27e0c](https://github.com/MariaDB/server/commit/0b36c27e0c)\
  2020-01-31 10:06:55 +0200
  * [MDEV-20307](https://jira.mariadb.org/browse/MDEV-20307): Remove a useless debug check to save stack space
* [Revision #afe9caa82d](https://github.com/MariaDB/server/commit/afe9caa82d)\
  2020-01-30 17:54:49 +0530
  * [MDEV-21564](https://jira.mariadb.org/browse/MDEV-21564) Assert in trx\_purge\_add\_update\_undo\_to\_history during shutdown
* [Revision #d89bb88674](https://github.com/MariaDB/server/commit/d89bb88674)\
  2020-01-23 16:17:55 +0530
  * [MDEV-20923](https://jira.mariadb.org/browse/MDEV-20923):UBSAN: member access within address … which does not point to an object of type 'xid\_count\_per\_binlog'
* [Revision #5271d43648](https://github.com/MariaDB/server/commit/5271d43648)\
  2020-01-28 18:03:13 +0200
  * [MDEV-14330](https://jira.mariadb.org/browse/MDEV-14330) Move mysqltest.1 man page to appropriate test package from server package
* [Revision #9aaa3e1fda](https://github.com/MariaDB/server/commit/9aaa3e1fda)\
  2020-01-28 17:48:57 +0200
  * Ingore sysusers and tmpfiles artifacts
* Merge [Revision #c5df6e1448](https://github.com/MariaDB/server/commit/c5df6e1448) 2020-01-28 09:23:53 +0100 - Merge branch 'bb-10.1-release' into 10.1
* [Revision #a7d02e8d24](https://github.com/MariaDB/server/commit/a7d02e8d24)\
  2020-01-27 15:06:54 -0500
  * bump the VERSION
* [Revision #742c36d048](https://github.com/MariaDB/server/commit/742c36d048)\
  2017-12-28 22:19:28 +0800
  * [MDEV-15052](https://jira.mariadb.org/browse/MDEV-15052): Allow sysusers and tmpfiles install for non-systemd users
* [Revision #b472bc2eba](https://github.com/MariaDB/server/commit/b472bc2eba)\
  2018-01-02 14:32:21 +0100
  * [MDEV-17028](https://jira.mariadb.org/browse/MDEV-17028): Use descriptive file names for sysusers and tmpfiles configuration

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
