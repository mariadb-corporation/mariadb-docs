# MariaDB 10.1.37 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.37)[Release Notes](../../old-releases/10.1/10.1.37.md)[Changelog](mariadb-10137-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 2 Nov 2018

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.37.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #8d834cd0f3](https://github.com/MariaDB/server/commit/8d834cd0f3)\
  2018-10-31 23:48:29 +0200
  * Updated list of unstable tests for 10.1.37 release
* [Revision #bf28ba67b6](https://github.com/MariaDB/server/commit/bf28ba67b6)\
  2018-10-31 22:06:15 +0100
  * update rdiffs for 32bit
* [Revision #a5cbdd63bc](https://github.com/MariaDB/server/commit/a5cbdd63bc)\
  2018-10-31 12:08:28 +0200
  * Fix innodb.table\_flags,debug
* [Revision #b92ff45089](https://github.com/MariaDB/server/commit/b92ff45089)\
  2018-10-31 10:35:15 +0100
  * disabling a crashing test
* Merge [Revision #a6e0000494](https://github.com/MariaDB/server/commit/a6e0000494) 2018-10-31 10:32:48 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #09e97299ba](https://github.com/MariaDB/server/commit/09e97299ba) 2018-10-31 00:25:26 +0100 - Merge branch '5.5' into 10.0
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
* Merge [Revision #f4eec7fab0](https://github.com/MariaDB/server/commit/f4eec7fab0) 2018-10-31 09:32:58 +0100 - Merge branch '10.1' into bb-10.1-serg
* [Revision #6af46f610f](https://github.com/MariaDB/server/commit/6af46f610f)\
  2018-10-30 12:28:03 +0000
  * README: Add reporting security vulns. direction
* Merge [Revision #44f6f44593](https://github.com/MariaDB/server/commit/44f6f44593) 2018-10-30 13:02:59 +0100 - Merge branch '10.0' into 10.1
* [Revision #8772824ce7](https://github.com/MariaDB/server/commit/8772824ce7)\
  2018-10-29 23:21:55 +0100
  * Restore auto-switch to bundled ssl if WITH\_SSL=yes
* [Revision #d5f564a996](https://github.com/MariaDB/server/commit/d5f564a996)\
  2018-10-28 12:42:06 +0100
  * rpm fixes: more %ignore'd files
* [Revision #329058be29](https://github.com/MariaDB/server/commit/329058be29)\
  2018-09-27 17:28:01 +0200
  * wsrep: create a macro for the error: label
* [Revision #0140bfac5e](https://github.com/MariaDB/server/commit/0140bfac5e)\
  2018-10-02 22:50:28 +0200
  * [MDEV-16127](https://jira.mariadb.org/browse/MDEV-16127) mroonga/storage.\* tests fail with GCC 8
* [Revision #5b735e8f09](https://github.com/MariaDB/server/commit/5b735e8f09)\
  2018-09-17 21:40:23 +0300
  * [MDEV-17133](https://jira.mariadb.org/browse/MDEV-17133) dump thread reads from a past position
* [Revision #2a576f71c5](https://github.com/MariaDB/server/commit/2a576f71c5)\
  2018-10-07 14:25:59 +0200
  * cmake: fix ucontext detection
* [Revision #d8974ebd67](https://github.com/MariaDB/server/commit/d8974ebd67)\
  2018-10-08 21:47:53 +0300
  * [MDEV-14431](https://jira.mariadb.org/browse/MDEV-14431) binlog.binlog\_flush\_binlogs\_delete\_domain failed in buildbot
* [Revision #5a5bc21a65](https://github.com/MariaDB/server/commit/5a5bc21a65)\
  2018-10-16 09:19:03 +0100
  * auth\_gssapi : Fix string formatting in my\_printf\_error()
* [Revision #952f394f8e](https://github.com/MariaDB/server/commit/952f394f8e)\
  2018-10-16 09:17:03 +0100
  * remove MYF flags from plugin
* [Revision #ea9c407e0b](https://github.com/MariaDB/server/commit/ea9c407e0b)\
  2018-10-15 23:07:30 +0100
  * Fix regular expression in replace\_regex in auth\_gssapi test.
* [Revision #64b48aebe4](https://github.com/MariaDB/server/commit/64b48aebe4)\
  2018-10-15 22:57:15 +0100
  * make auth\_gssapi\_basic work, also in domain environment.
* [Revision #311126758e](https://github.com/MariaDB/server/commit/311126758e)\
  2018-10-15 22:11:14 +0100
  * [MDEV-17462](https://jira.mariadb.org/browse/MDEV-17462) Heap corruption with auth\_gssapi on Windows.
* Merge [Revision #1f8b0752ad](https://github.com/MariaDB/server/commit/1f8b0752ad) 2018-10-13 22:53:31 +0200 - Merge branch 'gtid\_table\_garbage\_rows' into 10.1
* [Revision #61bba2a540](https://github.com/MariaDB/server/commit/61bba2a540)\
  2018-10-13 22:53:12 +0200
  * Fix build of embedded server
* Merge [Revision #bc2903e744](https://github.com/MariaDB/server/commit/bc2903e744) 2018-10-13 19:31:42 +0200 - Merge branch 'gtid\_table\_garbage\_rows' into 10.1
* [Revision #2f4a0c5be2](https://github.com/MariaDB/server/commit/2f4a0c5be2)\
  2018-10-07 18:59:52 +0200
  * Fix accumulation of old rows in mysql.gtid\_slave\_pos
* [Revision #3c3c4ae225](https://github.com/MariaDB/server/commit/3c3c4ae225)\
  2018-10-10 09:14:16 +0300
  * [MDEV-17403](https://jira.mariadb.org/browse/MDEV-17403): Test failure on galera.galera\_enum
* [Revision #5b0b6660f6](https://github.com/MariaDB/server/commit/5b0b6660f6)\
  2018-10-09 18:34:37 +0100
  * [MDEV-17413](https://jira.mariadb.org/browse/MDEV-17413) - Don't crash in my\_malloc\_size\_cb\_func() if thread specific memory is requested and current\_thd is NULL.
* [Revision #f517d8c742](https://github.com/MariaDB/server/commit/f517d8c742)\
  2018-10-02 14:30:44 +0300
  * [MDEV-17346](https://jira.mariadb.org/browse/MDEV-17346) parallel slave start and stop races to workers disappeared
* [Revision #1eca49577e](https://github.com/MariaDB/server/commit/1eca49577e)\
  2018-10-07 10:19:19 -0700
  * [MDEV-17382](https://jira.mariadb.org/browse/MDEV-17382) Hash join algorithm should not be used to join materialized derived table / view by equality
* Merge [Revision #079d0a8724](https://github.com/MariaDB/server/commit/079d0a8724) 2018-10-05 17:40:06 +0300 - Merge pull request #876 from tempesta-tech/tt-10.1-[MDEV-17313](https://jira.mariadb.org/browse/MDEV-17313)-counter-race
* [Revision #15803fce92](https://github.com/MariaDB/server/commit/15803fce92)\
  2018-09-28 19:57:06 +0300
  * [MDEV-17313](https://jira.mariadb.org/browse/MDEV-17313) Data race in ib\_counter\_t
* [Revision #1655053ac1](https://github.com/MariaDB/server/commit/1655053ac1)\
  2018-09-21 16:04:16 +0400
  * [MDEV-17200](https://jira.mariadb.org/browse/MDEV-17200) - pthread\_detach called for already detached threads
* [Revision #e855912733](https://github.com/MariaDB/server/commit/e855912733)\
  2018-10-04 13:29:29 +0300
  * Test by reverting [MDEV-16656](https://jira.mariadb.org/browse/MDEV-16656): DROP DATABASE crashes the Galera Cluster
* [Revision #6c29544c20](https://github.com/MariaDB/server/commit/6c29544c20)\
  2018-10-04 08:05:50 +0300
  * Enable for staging tree.
* [Revision #391b7f5bd1](https://github.com/MariaDB/server/commit/391b7f5bd1)\
  2018-10-04 08:04:55 +0300
  * Fix typo.
* [Revision #e2a1c58582](https://github.com/MariaDB/server/commit/e2a1c58582)\
  2018-10-03 08:58:23 +0300
  * Fix test failure on wsrep.variables
* [Revision #84a24d36d8](https://github.com/MariaDB/server/commit/84a24d36d8)\
  2018-10-03 08:49:57 +0300
  * [MDEV-17357](https://jira.mariadb.org/browse/MDEV-17357): Test failure on galera.galera\_pc\_ignore\_sb
* Merge [Revision #649451ae0d](https://github.com/MariaDB/server/commit/649451ae0d) 2018-10-01 12:47:35 +0300 - Merge pull request #875 from tempesta-tech/sysprg/[MDEV-16656](https://jira.mariadb.org/browse/MDEV-16656)
* [Revision #c62e49d0cf](https://github.com/MariaDB/server/commit/c62e49d0cf)\
  2018-10-01 09:53:37 +0200
  * [MDEV-16656](https://jira.mariadb.org/browse/MDEV-16656): DROP DATABASE crashes the Galera Cluster
* [Revision #865237e5af](https://github.com/MariaDB/server/commit/865237e5af)\
  2018-10-01 15:15:34 +0530
  * Fix rpl\_parallel\_optimistic\_nobinlog failure on binlog
* Merge [Revision #1fc5a6f30c](https://github.com/MariaDB/server/commit/1fc5a6f30c) 2018-09-23 12:58:11 +0200 - Merge branch '10.0' into 10.1
* [Revision #87dc4e98dd](https://github.com/MariaDB/server/commit/87dc4e98dd)\
  2018-09-23 13:53:57 +0300
  * [MDEV-17276](https://jira.mariadb.org/browse/MDEV-17276): Adjust Galera tests after Galera library 25.3.24
* [Revision #eefaf4fdc9](https://github.com/MariaDB/server/commit/eefaf4fdc9)\
  2018-09-20 15:44:04 +0300
  * Adjust disabled Galera tests.
* [Revision #428669fa83](https://github.com/MariaDB/server/commit/428669fa83)\
  2018-09-20 06:51:40 +0300
  * [MDEV-15805](https://jira.mariadb.org/browse/MDEV-15805): Test failure on galera.query\_cache
* [Revision #3177d26627](https://github.com/MariaDB/server/commit/3177d26627)\
  2018-09-19 13:10:54 +0300
  * [MDEV-13873](https://jira.mariadb.org/browse/MDEV-13873): galera.galera\_suspend\_slave failed in buildbot with wrong error code
* [Revision #45712a9a1f](https://github.com/MariaDB/server/commit/45712a9a1f)\
  2018-09-19 12:19:30 +0300
  * [MDEV-13871](https://jira.mariadb.org/browse/MDEV-13871): galera.galera\_unicode\_identifiers failed in buildbot with 'Unknown database'
* [Revision #82524239c4](https://github.com/MariaDB/server/commit/82524239c4)\
  2018-09-19 11:42:43 +0300
  * [MDEV-17208](https://jira.mariadb.org/browse/MDEV-17208): Test failure on galera.MW-286
* [Revision #cd363fecbf](https://github.com/MariaDB/server/commit/cd363fecbf)\
  2018-09-19 01:24:46 -0700
  * Removed duplicate tests.
* [Revision #cc616bea53](https://github.com/MariaDB/server/commit/cc616bea53)\
  2018-09-17 18:18:19 +0300
  * Test galera.query\_cache is still failing on bb.
* [Revision #145c947b88](https://github.com/MariaDB/server/commit/145c947b88)\
  2018-09-17 12:03:41 +0300
  * [MDEV-17206](https://jira.mariadb.org/browse/MDEV-17206): Test failure on galera.galera\_ist\_\* in debug builds
* [Revision #dbf4e68704](https://github.com/MariaDB/server/commit/dbf4e68704)\
  2018-09-17 09:05:52 +0300
  * [MDEV-13879](https://jira.mariadb.org/browse/MDEV-13879): galera.galera\_wan fails in buildbot with Stray state UUID msg or with "Transport endpoint is not connected" or with a failure to start a node
* [Revision #6a31e86bbd](https://github.com/MariaDB/server/commit/6a31e86bbd)\
  2018-09-17 08:11:38 +0300
  * Adjust Galera disabled tests based on test results.
* [Revision #d3a8b5aa9c](https://github.com/MariaDB/server/commit/d3a8b5aa9c)\
  2018-09-14 13:10:48 +0300
  * [MDEV-14143](https://jira.mariadb.org/browse/MDEV-14143): galera.galera\_kill\_smallchanges, galera.galera\_kill\_ddl fail in buildbot with "Last Applied Action message in non-primary configuration from member 0"
* [Revision #c886368a3a](https://github.com/MariaDB/server/commit/c886368a3a)\
  2018-09-14 11:16:54 +0300
  * Test galera\_sst\_rsync\_data\_dir has different result on release and debug builds. Modified version for 10.1 from following commit:
* [Revision #ed7a0e5efc](https://github.com/MariaDB/server/commit/ed7a0e5efc)\
  2018-09-14 10:35:37 +0300
  * [MDEV-13876](https://jira.mariadb.org/browse/MDEV-13876): galera.MW-328A failed in buildbot with wrong result or timeout
* [Revision #6c47c1c456](https://github.com/MariaDB/server/commit/6c47c1c456)\
  2018-09-13 13:27:03 -0700
  * [MDEV-16912](https://jira.mariadb.org/browse/MDEV-16912): Spider Order By column\[datatime] limit 5 returns 3 rows
* [Revision #c9d6728c36](https://github.com/MariaDB/server/commit/c9d6728c36)\
  2018-09-13 11:15:22 +0200
  * try to fix version detection
* Merge [Revision #ec457c08d7](https://github.com/MariaDB/server/commit/ec457c08d7) 2018-09-13 08:29:41 +0300 - Merge pull request #865 from grooverdan/[MDEV-17173](https://jira.mariadb.org/browse/MDEV-17173)-wsrep\_sst
* [Revision #b96d36344e](https://github.com/MariaDB/server/commit/b96d36344e)\
  2018-09-13 09:58:50 +1000
  * [MDEV-17173](https://jira.mariadb.org/browse/MDEV-17173): correct parsing of 12.13.14.15:4444/xtrabackup\_sst leaving LSN/SST\_VER blank
* [Revision #6c7910ee22](https://github.com/MariaDB/server/commit/6c7910ee22)\
  2018-09-12 11:25:47 +0300
  * Fix test galera#505 galera library version check.
* [Revision #e63b84b916](https://github.com/MariaDB/server/commit/e63b84b916)\
  2018-09-09 21:07:46 +0300
  * [MDEV-17155](https://jira.mariadb.org/browse/MDEV-17155): Incorrect ORDER BY optimization: full index scan is used instead of range
* [Revision #038804d594](https://github.com/MariaDB/server/commit/038804d594)\
  2018-09-12 14:56:48 +0300
  * Update disabled Galera tests.
* [Revision #794e89ed3f](https://github.com/MariaDB/server/commit/794e89ed3f)\
  2018-09-12 14:54:59 +0300
  * [MDEV-17108](https://jira.mariadb.org/browse/MDEV-17108): Test failure on galera.galera\_kill\_ddl
* [Revision #c76ee73dc7](https://github.com/MariaDB/server/commit/c76ee73dc7)\
  2018-09-12 13:32:14 +0300
  * [MDEV-13743](https://jira.mariadb.org/browse/MDEV-13743): galera\_toi\_truncate may fail with: query 'reap' succeeded - should have failed with errno 1213
* [Revision #16384fae63](https://github.com/MariaDB/server/commit/16384fae63)\
  2018-08-29 16:45:28 +0200
  * [MDEV-15845](https://jira.mariadb.org/browse/MDEV-15845) Test failure on galera.galera\_concurrent\_ctas
* [Revision #e46b2a3e94](https://github.com/MariaDB/server/commit/e46b2a3e94)\
  2018-09-11 20:59:35 +0100
  * [MDEV-12956](https://jira.mariadb.org/browse/MDEV-12956) provide default datadir for mariadb-backup --copy-back
* [Revision #21829bd743](https://github.com/MariaDB/server/commit/21829bd743)\
  2018-09-11 08:19:16 +0300
  * [MDEV-17106](https://jira.mariadb.org/browse/MDEV-17106): Test failure on galera.galera\_binlog\_stmt\_autoinc
* [Revision #bdaace9b30](https://github.com/MariaDB/server/commit/bdaace9b30)\
  2018-09-10 13:43:37 +0300
  * [MDEV-17151](https://jira.mariadb.org/browse/MDEV-17151): Galera test failure on galera.galera\_var\_node\_address
* [Revision #c1f308054d](https://github.com/MariaDB/server/commit/c1f308054d)\
  2018-09-08 16:57:31 +0300
  * [MDEV-17143](https://jira.mariadb.org/browse/MDEV-17143): Galera test failure on galera.MW-44
* [Revision #f1bcfbb437](https://github.com/MariaDB/server/commit/f1bcfbb437)\
  2018-09-08 11:34:22 -0400
  * bump the VERSION
* [Revision #f01c4a10d7](https://github.com/MariaDB/server/commit/f01c4a10d7)\
  2018-09-08 08:12:55 +0300
  * Add one more wait for truncate in MW-44.
* Merge [Revision #908ac40bdb](https://github.com/MariaDB/server/commit/908ac40bdb) 2018-09-07 20:24:49 +0200 - Merge branch 'bb-10.1-release' into 10.1
* [Revision #0254be96f7](https://github.com/MariaDB/server/commit/0254be96f7)\
  2018-09-07 15:43:03 +0200
  * remove doubly-installed file
* [Revision #edb3a32c6c](https://github.com/MariaDB/server/commit/edb3a32c6c)\
  2018-09-06 14:16:09 +0300
  * [MDEV-17143](https://jira.mariadb.org/browse/MDEV-17143): Galera test failure on galera.MW-44

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
