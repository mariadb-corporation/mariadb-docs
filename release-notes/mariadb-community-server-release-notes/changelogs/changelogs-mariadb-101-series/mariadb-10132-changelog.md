# MariaDB 10.1.32 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.32)[Release Notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10132-release-notes.md)[Changelog](mariadb-10132-changelog.md)[Overview of 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)

**Release date:** 27 Mar 2018

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10132-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #4d83b01537](https://github.com/MariaDB/server/commit/4d83b01537)\
  2018-03-26 17:14:08 +0300
  * Updated list of unstable tests for 10.1.32 release
* [Revision #15795b9f9a](https://github.com/MariaDB/server/commit/15795b9f9a)\
  2018-03-24 14:24:20 +0100
  * save/restore auto\_inc settings in galera\_sst\_rsync test
* [Revision #7454d5f952](https://github.com/MariaDB/server/commit/7454d5f952)\
  2018-03-24 12:34:14 +0100
  * save/restore auto\_inc settings in galera\_sst\_mysqldump test
* [Revision #5fdbc3f66b](https://github.com/MariaDB/server/commit/5fdbc3f66b)\
  2018-03-24 13:50:52 +0100
  * compiler warning
* [Revision #0b74a1fa64](https://github.com/MariaDB/server/commit/0b74a1fa64)\
  2018-03-24 00:37:38 +0400
  * [MDEV-14533](https://jira.mariadb.org/browse/MDEV-14533) Provide information\_schema tables using which hardware information can be obtained.
* [Revision #3b644ac1f7](https://github.com/MariaDB/server/commit/3b644ac1f7)\
  2018-03-24 00:30:28 +0400
  * [MDEV-14533](https://jira.mariadb.org/browse/MDEV-14533) Provide information\_schema tables using which hardware information can be obtained.
* Merge [Revision #febe1e8503](https://github.com/MariaDB/server/commit/febe1e8503) 2018-03-23 17:40:53 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #a2e47f8c41](https://github.com/MariaDB/server/commit/a2e47f8c41) 2018-03-23 11:44:29 +0100 - Merge branch '5.5' into 10.0
* [Revision #ddc5c65333](https://github.com/MariaDB/server/commit/ddc5c65333)\
  2018-03-22 03:01:53 +0530
  * [MDEV-14779](https://jira.mariadb.org/browse/MDEV-14779): using left join causes incorrect results with materialization and derived tables
* [Revision #f3994b7432](https://github.com/MariaDB/server/commit/f3994b7432)\
  2018-03-21 12:13:37 +0100
  * [MDEV-15492](https://jira.mariadb.org/browse/MDEV-15492): Subquery crash similar to [MDEV-10050](https://jira.mariadb.org/browse/MDEV-10050)
* [Revision #2dd4e50d5f](https://github.com/MariaDB/server/commit/2dd4e50d5f)\
  2018-03-21 01:34:45 +0530
  * [MDEV-15555](https://jira.mariadb.org/browse/MDEV-15555): select from DUAL where false yielding wrong result when in a IN
* [Revision #d3681c18f9](https://github.com/MariaDB/server/commit/d3681c18f9)\
  2017-11-14 07:22:25 +0800
  * followup for 89b0d5cb6e3, backport 8c422bf48d7
* [Revision #af86422f08](https://github.com/MariaDB/server/commit/af86422f08)\
  2018-03-21 22:29:00 +0000
  * [MDEV-13023](https://jira.mariadb.org/browse/MDEV-13023) mariadb-backup does not preserve holes for page compressed tables.
* [Revision #ca291015bc](https://github.com/MariaDB/server/commit/ca291015bc)\
  2018-03-20 17:25:49 +0400
  * [MDEV-10269](https://jira.mariadb.org/browse/MDEV-10269) - Killed queries from I\_S stay in 'Killed' state for long time and don't let server shut down
* [Revision #4092f90655](https://github.com/MariaDB/server/commit/4092f90655)\
  2018-03-22 13:48:31 +0100
  * [MDEV-15409](https://jira.mariadb.org/browse/MDEV-15409) make sure every sst script is tested in buildbot
* [Revision #5ff7ed96d5](https://github.com/MariaDB/server/commit/5ff7ed96d5)\
  2018-03-20 22:42:42 +0100
  * [MDEV-15409](https://jira.mariadb.org/browse/MDEV-15409) make sure every sst script is tested in buildbot
* [Revision #60d4abc1e5](https://github.com/MariaDB/server/commit/60d4abc1e5)\
  2018-03-20 13:51:55 +0100
  * [MDEV-15409](https://jira.mariadb.org/browse/MDEV-15409) make sure every sst script is tested in buildbot
* [Revision #4b1cbff7a8](https://github.com/MariaDB/server/commit/4b1cbff7a8)\
  2018-03-20 01:49:32 +0100
  * [MDEV-15409](https://jira.mariadb.org/browse/MDEV-15409) make sure every sst script is tested in buildbot
* [Revision #8f1014e9a0](https://github.com/MariaDB/server/commit/8f1014e9a0)\
  2018-03-19 23:27:10 +0100
  * [MDEV-15409](https://jira.mariadb.org/browse/MDEV-15409) make sure every sst script is tested in buildbot
* [Revision #7e300424a3](https://github.com/MariaDB/server/commit/7e300424a3)\
  2018-03-19 23:23:51 +0100
  * wsrep\_sst\_auth: fix a memory leak
* [Revision #ccd5c9c64e](https://github.com/MariaDB/server/commit/ccd5c9c64e)\
  2018-03-19 23:06:59 +0100
  * mysql: don't prepare strings if they won't be used
* [Revision #a15ab358fc](https://github.com/MariaDB/server/commit/a15ab358fc)\
  2018-03-20 22:35:19 +0100
  * wsrep\_sst scripts: support traditional netcat
* [Revision #89b0d5cb6e](https://github.com/MariaDB/server/commit/89b0d5cb6e)\
  2017-10-16 17:49:52 +0200
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968) sst fails with "WSREP\_SST\_OPT\_PORT: readonly variable"
* [Revision #de55a7d1f9](https://github.com/MariaDB/server/commit/de55a7d1f9)\
  2018-03-20 20:54:58 +0100
  * Allow table-less selects even when wsrep is not ready
* [Revision #b6e2973ee6](https://github.com/MariaDB/server/commit/b6e2973ee6)\
  2018-03-21 12:59:40 +0100
  * [MDEV-14533](https://jira.mariadb.org/browse/MDEV-14533) Provide information\_schema tables using which hardware information can be obtained.
* [Revision #f5b2761c70](https://github.com/MariaDB/server/commit/f5b2761c70)\
  2018-03-23 00:18:21 +0400
  * [MDEV-10871](https://jira.mariadb.org/browse/MDEV-10871) Add logging capability to pam\_user\_map.c.
* [Revision #0cba2c1ccb](https://github.com/MariaDB/server/commit/0cba2c1ccb)\
  2018-03-22 16:23:37 +0400
  * [MDEV-15633](https://jira.mariadb.org/browse/MDEV-15633) Memory leak after [MDEV-15005](https://jira.mariadb.org/browse/MDEV-15005)
* [Revision #b6d68c6aa3](https://github.com/MariaDB/server/commit/b6d68c6aa3)\
  2018-03-22 14:19:16 +0530
  * [MDEV-13561](https://jira.mariadb.org/browse/MDEV-13561) mariadb-backup is incompatible with retroactively created innodb\_undo\_tablespaces
* [Revision #4629db0dd6](https://github.com/MariaDB/server/commit/4629db0dd6)\
  2018-03-21 09:38:23 +0200
  * Fix test failure on galera\_var\_reject\_queries.
* [Revision #ca9d9029e6](https://github.com/MariaDB/server/commit/ca9d9029e6)\
  2018-03-21 12:32:38 +0200
  * Partially revert commit 2a729b5f4b14f9f04cf81e1d8dd4eec4ad6cb7cd
* [Revision #c704523195](https://github.com/MariaDB/server/commit/c704523195)\
  2018-03-21 11:58:17 +0200
  * Remove orphan wsrep\_node\_is\_ready()
* [Revision #9652038453](https://github.com/MariaDB/server/commit/9652038453)\
  2018-03-21 12:33:38 +0400
  * [MDEV-14533](https://jira.mariadb.org/browse/MDEV-14533) Provide information\_schema tables using which hardware information can be obtained.
* [Revision #15051ab14a](https://github.com/MariaDB/server/commit/15051ab14a)\
  2018-03-21 08:13:43 +0200
  * Disable a failing test
* Merge [Revision #613be24b7a](https://github.com/MariaDB/server/commit/613be24b7a) 2018-03-20 19:25:08 +0200 - Merge 10.0 into 10.1
* Merge [Revision #0492100059](https://github.com/MariaDB/server/commit/0492100059) 2018-03-20 18:36:03 +0200 - Merge 5.5 into 10.0
* Merge [Revision #69bc3c1976](https://github.com/MariaDB/server/commit/69bc3c1976) 2018-03-20 18:18:57 +0200 - PR #666: [MDEV-15030](https://jira.mariadb.org/browse/MDEV-15030) Add ASAN instrumentation
* [Revision #5a8f8f89d6](https://github.com/MariaDB/server/commit/5a8f8f89d6)\
  2018-03-20 10:46:57 +0300
  * honor alignment rules and xtradb too
* [Revision #75c76dbb06](https://github.com/MariaDB/server/commit/75c76dbb06)\
  2018-03-19 16:18:53 +0300
  * [MDEV-15030](https://jira.mariadb.org/browse/MDEV-15030) Add ASAN instrumentation
* [Revision #0943b33de3](https://github.com/MariaDB/server/commit/0943b33de3)\
  2018-03-14 14:35:27 +0000
  * [MDEV-12190](https://jira.mariadb.org/browse/MDEV-12190) YASSL isn't able to negotiate TLS version correctly
* [Revision #e3dd9a95e5](https://github.com/MariaDB/server/commit/e3dd9a95e5)\
  2018-03-16 18:57:21 +0530
  * [MDEV-6736](https://jira.mariadb.org/browse/MDEV-6736): Valgrind warnings 'Invalid read' in subselect\_engine::calc\_const\_tables with SQ in WHERE and HAVING, ORDER BY, materialization+semijoin
* [Revision #e0a0fe7d81](https://github.com/MariaDB/server/commit/e0a0fe7d81)\
  2018-03-19 18:12:37 +0200
  * [MDEV-12396](https://jira.mariadb.org/browse/MDEV-12396) IMPORT TABLESPACE: Do not retry partial reads
* [Revision #a80af35a85](https://github.com/MariaDB/server/commit/a80af35a85)\
  2018-03-20 13:03:01 +0200
  * [MDEV-12396](https://jira.mariadb.org/browse/MDEV-12396) IMPORT cleanup: ROW\_FORMAT=COMPRESSED
* [Revision #eaa7bfb59f](https://github.com/MariaDB/server/commit/eaa7bfb59f)\
  2018-03-20 12:55:00 +0200
  * [MDEV-12396](https://jira.mariadb.org/browse/MDEV-12396) IMPORT TABLESPACE: Simplify validation
* [Revision #6247c64c2a](https://github.com/MariaDB/server/commit/6247c64c2a)\
  2018-03-19 13:11:54 +0200
  * [MDEV-12396](https://jira.mariadb.org/browse/MDEV-12396) IMPORT TABLESPACE cleanup
* [Revision #eee73ddfbb](https://github.com/MariaDB/server/commit/eee73ddfbb)\
  2018-03-20 17:51:57 +0530
  * [MDEV-12255](https://jira.mariadb.org/browse/MDEV-12255) innodb\_prefix\_index\_cluster\_optimization hits debug build assert on UTF-8 columns
* [Revision #bc2e7d7889](https://github.com/MariaDB/server/commit/bc2e7d7889)\
  2018-03-20 12:10:17 +0200
  * Fix test case MW-329.
* [Revision #33028f7c4b](https://github.com/MariaDB/server/commit/33028f7c4b)\
  2016-03-03 02:57:21 -0800
  * Refs: MW-245 - Adjust tests to account for the new behavior.
* [Revision #9a89614857](https://github.com/MariaDB/server/commit/9a89614857)\
  2016-03-03 09:35:52 +0200
  * Refs: MW-245 - changed logic so that in non primary node it is possible to do SET + SHOW + SELECT from information and pfs schema, when dirty reads are not enabled - however, non table selects are not allowed (e.g. SELECT 1)
* [Revision #c5dd2abf4c](https://github.com/MariaDB/server/commit/c5dd2abf4c)\
  2016-03-02 21:32:06 +0200
  * Refs MW-245 - logic was wrong in detecting if queries are allowed in non primary node. it allowed select with no table list to execute even if dirty reads was not specified
* [Revision #84d4ab5be1](https://github.com/MariaDB/server/commit/84d4ab5be1)\
  2016-02-19 00:16:36 -0800
  * refs MW-245: Galera MTR Tests: additional tests for wsrep\_reject\_queries, wsrep\_dirty\_reads
* [Revision #8f717ed360](https://github.com/MariaDB/server/commit/8f717ed360)\
  2016-02-19 00:14:26 +0200
  * refs MW-245 - allowing USE with dirty reads configuration - fix for logic of setting wsrep ready status
* [Revision #2a729b5f4b](https://github.com/MariaDB/server/commit/2a729b5f4b)\
  2016-02-17 11:20:48 +0200
  * refs MW-245 - merged wsrep\_dirty\_reads and wsrep\_reject\_queries from PXC
* [Revision #e390f7b675](https://github.com/MariaDB/server/commit/e390f7b675)\
  2018-03-20 11:05:28 +0530
  * [MDEV-12737](https://jira.mariadb.org/browse/MDEV-12737): tokudb\_mariadb.mdev6657 fails in buildbot with different plan, and outside with valgrind warnings
* [Revision #7cf2428db3](https://github.com/MariaDB/server/commit/7cf2428db3)\
  2018-03-19 12:49:22 -0700
  * [MDEV-10991](https://jira.mariadb.org/browse/MDEV-10991): Server crashes in spider\_udf\_direct\_sql\_create\_conn - tests in spider/oracle\* suites crash the server
* Merge [Revision #24b353162f](https://github.com/MariaDB/server/commit/24b353162f) 2018-03-19 15:21:01 +0200 - Merge branch '10.0-galera' into 10.1
* [Revision #8b54c31486](https://github.com/MariaDB/server/commit/8b54c31486)\
  2018-03-14 13:31:28 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): where O\_CLOEXEC is available, use for innodb buf\_dump
* Merge [Revision #930682c487](https://github.com/MariaDB/server/commit/930682c487) 2018-03-14 09:38:04 +0200 - Merge pull request #636 from grooverdan/10.0-galera-[MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743)-linux-aio-ib\_logfile0
* [Revision #26e4a48bda](https://github.com/MariaDB/server/commit/26e4a48bda)\
  2018-03-02 10:50:38 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): ib\_logfile0 Use O\_CLOEXEC so galera SST scripts don't get fd
* [Revision #7bd95307f2](https://github.com/MariaDB/server/commit/7bd95307f2)\
  2018-01-30 05:37:22 -0800
  * Bump wsrep patch version to 25.23
* [Revision #57ae4992ed](https://github.com/MariaDB/server/commit/57ae4992ed)\
  2018-02-06 11:29:36 -0500
  * bump the VERSION
* [Revision #f538a64817](https://github.com/MariaDB/server/commit/f538a64817)\
  2018-03-19 13:07:41 +0400
  * [MDEV-15005](https://jira.mariadb.org/browse/MDEV-15005) ASAN: stack-buffer-overflow in my\_strnncollsp\_simple
* [Revision #31e2ab513d](https://github.com/MariaDB/server/commit/31e2ab513d)\
  2018-02-14 09:48:29 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #f46155a31b](https://github.com/MariaDB/server/commit/f46155a31b)\
  2018-02-14 13:52:37 +0200
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549): Galera test failures
* [Revision #e5e83249c1](https://github.com/MariaDB/server/commit/e5e83249c1)\
  2018-02-15 10:34:01 +0200
  * [MDEV-14875](https://jira.mariadb.org/browse/MDEV-14875): galera\_new\_cluster crashes mysqld when existing server contains databases
* [Revision #a0c722d853](https://github.com/MariaDB/server/commit/a0c722d853)\
  2018-03-16 18:35:41 +0530
  * [MDEV-15321](https://jira.mariadb.org/browse/MDEV-15321):different results when using value of optimizer\_use\_condition\_selectivity=4 and =1
* [Revision #0a534348c7](https://github.com/MariaDB/server/commit/0a534348c7)\
  2018-03-15 15:34:45 +0400
  * [MDEV-14265](https://jira.mariadb.org/browse/MDEV-14265) - RPMLint warning: shared-lib-calls-exit
* [Revision #7033af9e81](https://github.com/MariaDB/server/commit/7033af9e81)\
  2018-03-16 08:34:12 +0200
  * Conditionally define TRX\_WSREP\_ABORT
* [Revision #ca40330d1d](https://github.com/MariaDB/server/commit/ca40330d1d)\
  2018-03-16 08:23:56 +0200
  * Fix a deadlock in thd\_report\_wait\_for()
* [Revision #dbb3960ad8](https://github.com/MariaDB/server/commit/dbb3960ad8)\
  2018-03-15 19:48:29 +0200
  * Follow-up to [MDEV-11236](https://jira.mariadb.org/browse/MDEV-11236)/[MDEV-14846](https://jira.mariadb.org/browse/MDEV-14846) debug assertion
* [Revision #723f87e9d3](https://github.com/MariaDB/server/commit/723f87e9d3)\
  2018-03-14 09:39:47 +0200
  * lock\_table\_create(), lock\_rec\_create(): Clean up the WSREP code
* [Revision #a54abf0175](https://github.com/MariaDB/server/commit/a54abf0175)\
  2018-03-13 14:00:45 +0200
  * innobase\_kill\_query(): Use lock\_trx\_handle\_wait()
* Merge [Revision #4d248974e0](https://github.com/MariaDB/server/commit/4d248974e0) 2018-03-15 17:28:08 +0200 - Merge pull request #663 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_var\_slave\_threads
* [Revision #ba6cf25396](https://github.com/MariaDB/server/commit/ba6cf25396)\
  2018-03-15 16:03:25 +0100
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable test galera.galera\_var\_slave\_threads
* Merge [Revision #1bec0c4595](https://github.com/MariaDB/server/commit/1bec0c4595) 2018-03-15 13:58:46 +0200 - Merge pull request #650 from codership/[MDEV-14144](https://jira.mariadb.org/browse/MDEV-14144)
* Merge [Revision #c7c52ef1e8](https://github.com/MariaDB/server/commit/c7c52ef1e8) 2018-03-15 13:58:14 +0200 - Merge branch '10.1' into [MDEV-14144](https://jira.mariadb.org/browse/MDEV-14144)
* Merge [Revision #de3725a7db](https://github.com/MariaDB/server/commit/de3725a7db) 2018-03-15 13:57:31 +0200 - Merge pull request #654 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_var\_max\_ws\_rows
* Merge [Revision #59c313c698](https://github.com/MariaDB/server/commit/59c313c698) 2018-03-15 13:57:01 +0200 - Merge branch '10.1' into [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_var\_max\_ws\_rows
* Merge [Revision #866ddbec25](https://github.com/MariaDB/server/commit/866ddbec25) 2018-03-15 13:54:50 +0200 - Merge pull request #656 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-MW-366
* [Revision #9953588ac4](https://github.com/MariaDB/server/commit/9953588ac4)\
  2018-03-13 14:27:44 +0100
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable MTR test galera.MW-366
* Merge [Revision #ff172467ec](https://github.com/MariaDB/server/commit/ff172467ec) 2018-03-15 12:55:03 +0200 - Merge pull request #659 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-galera\_bf\_abort\_for\_update
* [Revision #9a21fd34af](https://github.com/MariaDB/server/commit/9a21fd34af)\
  2018-03-14 10:27:31 +0100
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Re-enable test galera.galera\_bf\_abort\_for\_update
* [Revision #fe66f766bb](https://github.com/MariaDB/server/commit/fe66f766bb)\
  2017-09-20 18:38:08 +0300
  * Fix and enable galera.galera\_bf\_abort\_for\_update
* Merge [Revision #047abdac3e](https://github.com/MariaDB/server/commit/047abdac3e) 2018-03-15 12:52:41 +0200 - Merge pull request #653 from codership/[MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549)-fixes-for-MW-286
* [Revision #0368e75a55](https://github.com/MariaDB/server/commit/0368e75a55)\
  2018-03-15 11:36:36 +0100
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Re-enable tests MW-328A, MW-328B, MW-328C and MW-329
* [Revision #a3ba3aab5a](https://github.com/MariaDB/server/commit/a3ba3aab5a)\
  2018-03-08 11:11:03 +0100
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Wrong usage of mutex 'LOCK\_wsrep\_thd' and 'LOCK\_thd\_kill' test galera.MW-286
* [Revision #0f0776b2ad](https://github.com/MariaDB/server/commit/0f0776b2ad)\
  2018-03-08 10:55:52 +0100
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix and re-enable test galera.MW-286
* [Revision #efb9dec2b9](https://github.com/MariaDB/server/commit/efb9dec2b9)\
  2018-03-15 10:23:42 +0400
  * A 32bit cleanup for [MDEV-14452](https://jira.mariadb.org/browse/MDEV-14452) Precision in INTERVAL xxx DAY\_MICROSECOND parsed wrong?
* Merge [Revision #8152c52e1a](https://github.com/MariaDB/server/commit/8152c52e1a) 2018-03-15 03:45:28 +0200 - Merge remote-tracking branch '10.0' into 10.1
* Merge [Revision #3d5dff6cae](https://github.com/MariaDB/server/commit/3d5dff6cae) 2018-03-14 12:10:31 +0200 - Merge branch '5.5' into 10.0
* [Revision #926edd48e1](https://github.com/MariaDB/server/commit/926edd48e1)\
  2018-03-06 19:59:57 +0530
  * [MDEV-15235](https://jira.mariadb.org/browse/MDEV-15235): Assertion \`length > 0' failed in create\_ref\_for\_key
* [Revision #ac3fd5acac](https://github.com/MariaDB/server/commit/ac3fd5acac)\
  2018-02-03 22:01:30 +1100
  * debian: VCS is on github
* [Revision #48c11d407b](https://github.com/MariaDB/server/commit/48c11d407b)\
  2018-03-13 12:42:41 +0400
  * [MDEV-13202](https://jira.mariadb.org/browse/MDEV-13202) Assertion \`ltime->neg == 0' failed in date\_to\_datetime
* [Revision #782fb1e016](https://github.com/MariaDB/server/commit/782fb1e016)\
  2018-03-14 18:47:02 +1100
  * fix ucontext configure check
* [Revision #38579cefa9](https://github.com/MariaDB/server/commit/38579cefa9)\
  2018-03-14 14:46:23 +0400
  * [MDEV-14452](https://jira.mariadb.org/browse/MDEV-14452) Precision in INTERVAL xxx DAY\_MICROSECOND parsed wrong?
* [Revision #9005108234](https://github.com/MariaDB/server/commit/9005108234)\
  2018-01-26 23:26:39 +0200
  * [MDEV-14721](https://jira.mariadb.org/browse/MDEV-14721) Big transaction events get lost on semisync master when replicate\_events\_marked\_for\_skip=FILTER\_ON\_MASTER
* [Revision #12f9cf075f](https://github.com/MariaDB/server/commit/12f9cf075f)\
  2018-03-12 16:48:42 +0400
  * Removed unused variables.
* Merge [Revision #0be18c4038](https://github.com/MariaDB/server/commit/0be18c4038) 2018-03-12 13:22:13 +0200 - Merge 10.0 into 10.1
* [Revision #4a35e76f64](https://github.com/MariaDB/server/commit/4a35e76f64)\
  2018-03-12 13:06:21 +0200
  * [MDEV-14773](https://jira.mariadb.org/browse/MDEV-14773) DROP TABLE hangs for InnoDB table with FULLTEXT index
* Merge [Revision #10f06b07bc](https://github.com/MariaDB/server/commit/10f06b07bc) 2018-03-09 22:43:54 +0200 - Merge 10.0 into 10.1
* [Revision #4a5c237c76](https://github.com/MariaDB/server/commit/4a5c237c76)\
  2018-03-09 22:26:27 +0200
  * [MDEV-14648](https://jira.mariadb.org/browse/MDEV-14648) Restore fix for MySQL BUG#39053 - UNINSTALL PLUGIN does not allow the storage engine to cleanup open connections
* [Revision #9ee39d2b9b](https://github.com/MariaDB/server/commit/9ee39d2b9b)\
  2018-03-09 10:20:19 +0100
  * [MDEV-13549](https://jira.mariadb.org/browse/MDEV-13549) Fix for test galera.galera\_var\_max\_ws\_rows
* [Revision #f1de725fda](https://github.com/MariaDB/server/commit/f1de725fda)\
  2018-03-12 13:41:47 +0100
  * [MDEV-14144](https://jira.mariadb.org/browse/MDEV-14144) Re-enable MTR test galera.galera\_as\_slave
* [Revision #05261f97c8](https://github.com/MariaDB/server/commit/05261f97c8)\
  2016-06-14 08:14:37 -0700
  * Galera MTR Tests: Modify mysqltest so that if a --let = `SELECT ...` query is interrupted, the test does not fail but the error is communicated to caller
* [Revision #8ef727b3d0](https://github.com/MariaDB/server/commit/8ef727b3d0)\
  2018-03-07 12:07:49 +0200
  * [MDEV-14904](https://jira.mariadb.org/browse/MDEV-14904) Backport innodb\_default\_row\_format
* [Revision #176d603cc7](https://github.com/MariaDB/server/commit/176d603cc7)\
  2018-03-04 18:59:29 +0100
  * [MDEV-15462](https://jira.mariadb.org/browse/MDEV-15462) TokuDB does not build on openSUSE
* [Revision #e49c1d1cef](https://github.com/MariaDB/server/commit/e49c1d1cef)\
  2018-02-24 09:32:50 +0100
  * mtr: force-flush stderr and stdout
* Merge [Revision #a04e4f531a](https://github.com/MariaDB/server/commit/a04e4f531a) 2018-02-22 14:12:02 +0100 - Merge branch '10.0' into 10.1
* Merge [Revision #b728641e86](https://github.com/MariaDB/server/commit/b728641e86) 2018-02-22 09:22:03 +0100 - Merge branch '5.5' into 10.0
* [Revision #7bd258c44c](https://github.com/MariaDB/server/commit/7bd258c44c)\
  2018-02-15 10:06:14 +0100
  * fix plugins.server\_audit test for --ps
* [Revision #03de234baf](https://github.com/MariaDB/server/commit/03de234baf)\
  2018-02-14 19:12:23 +0100
  * [MDEV-13982](https://jira.mariadb.org/browse/MDEV-13982) Server crashes in ha\_partition::engine\_name
* [Revision #2709380587](https://github.com/MariaDB/server/commit/2709380587)\
  2018-02-14 18:14:24 +0100
  * [MDEV-13748](https://jira.mariadb.org/browse/MDEV-13748) Assertion \`status\_var.local\_memory\_used == 0 || !debug\_assert\_on\_not\_freed\_memory' failed in virtual THD::THD after query with INTERSECT
* [Revision #c8afe7daac](https://github.com/MariaDB/server/commit/c8afe7daac)\
  2018-02-05 14:13:26 +0100
  * cleanup: remove a duplicated test case
* [Revision #7c6cf7fefe](https://github.com/MariaDB/server/commit/7c6cf7fefe)\
  2018-01-25 14:25:48 +0100
  * bug: ha\_heap was unilaterally increasing reclength
* [Revision #88d1c1c551](https://github.com/MariaDB/server/commit/88d1c1c551)\
  2018-02-12 15:12:49 +0100
  * [MDEV-15288](https://jira.mariadb.org/browse/MDEV-15288) Configure errors when building without INNOBASE
* [Revision #504beb1325](https://github.com/MariaDB/server/commit/504beb1325)\
  2018-02-22 12:20:46 +0200
  * Add supressions for possible warning.
* [Revision #5d8ac1ece1](https://github.com/MariaDB/server/commit/5d8ac1ece1)\
  2018-02-14 13:30:52 +0100
  * log all mtr output in vardir/log/stdout.log
* [Revision #50359719f0](https://github.com/MariaDB/server/commit/50359719f0)\
  2018-02-14 12:35:47 +0100
  * fix compilation -DWITH\_PERFSCHEMA=NO
* [Revision #18455ec3f1](https://github.com/MariaDB/server/commit/18455ec3f1)\
  2018-02-14 12:35:12 +0100
  * fix compilation wih -DPLUGIN\_PARTITION=NO
* [Revision #4e6dab94d0](https://github.com/MariaDB/server/commit/4e6dab94d0)\
  2018-02-21 19:38:57 +0530
  * [MDEV-10](https://jira.mariadb.org/browse/MDEV-10).1.31 does not join an existing cluster with SST xtrabackup-v2
* [Revision #56d6776524](https://github.com/MariaDB/server/commit/56d6776524)\
  2018-02-20 20:03:23 +0000
  * Windows : remove freopen(), "to keep fd = 0 busy".
* [Revision #c3a3b77f9a](https://github.com/MariaDB/server/commit/c3a3b77f9a)\
  2018-02-20 09:27:31 +0200
  * Disable failing Galera tests:
* [Revision #3a7126cbb7](https://github.com/MariaDB/server/commit/3a7126cbb7)\
  2018-02-20 09:17:29 +0200
  * Disable galera\_gtid until 1047: WSREP has not yet prepared node for application use is fixed.
* [Revision #b697f213a7](https://github.com/MariaDB/server/commit/b697f213a7)\
  2018-02-19 13:53:35 +0400
  * [MDEV-14541](https://jira.mariadb.org/browse/MDEV-14541) - Workaround GCC ICE on ARM64
* [Revision #7a84688e2c](https://github.com/MariaDB/server/commit/7a84688e2c)\
  2018-02-18 07:47:47 +0200
  * [MDEV-14814](https://jira.mariadb.org/browse/MDEV-14814): encryption.innodb\_encryption-page-compression failed in buildbot with timeout on wait condition
* [Revision #9ea3ad6d75](https://github.com/MariaDB/server/commit/9ea3ad6d75)\
  2018-02-18 07:32:19 +0200
  * Disable failing test.
* [Revision #0e8cb572f1](https://github.com/MariaDB/server/commit/0e8cb572f1)\
  2018-02-17 15:18:14 +0200
  * Fix innodb\_encryption-page-compression test by force flushing dirty pages.
* [Revision #55bc3f1dd9](https://github.com/MariaDB/server/commit/55bc3f1dd9)\
  2018-02-17 18:04:06 +0200
  * Fixed performance problem with Aria in find\_head()
* [Revision #965e16376c](https://github.com/MariaDB/server/commit/965e16376c)\
  2018-02-17 17:48:23 +0200
  * TokuDB didn't compile with valgrind
* [Revision #f853b8ed26](https://github.com/MariaDB/server/commit/f853b8ed26)\
  2018-02-17 17:47:18 +0200
  * partition\_alter\_myisam produces warning if no symlink support
* [Revision #9a46d97149](https://github.com/MariaDB/server/commit/9a46d97149)\
  2018-02-17 14:20:33 +0200
  * [MDEV-15333](https://jira.mariadb.org/browse/MDEV-15333) MariaDB (still) slow start
* [Revision #a351f40cba](https://github.com/MariaDB/server/commit/a351f40cba)\
  2018-02-16 14:14:43 +0400
  * [MDEV-14541](https://jira.mariadb.org/browse/MDEV-14541) - Workaround GCC ICE on ARM64
* [Revision #21e5335154](https://github.com/MariaDB/server/commit/21e5335154)\
  2018-02-16 10:19:57 +0200
  * [MDEV-9962](https://jira.mariadb.org/browse/MDEV-9962): encryption.innodb\_encryption\_filekeys stalled waiting for key encryption threads to decrypt all required spaces
* [Revision #d3fbff38b9](https://github.com/MariaDB/server/commit/d3fbff38b9)\
  2018-02-16 08:21:19 +0200
  * [MDEV-14814](https://jira.mariadb.org/browse/MDEV-14814): encryption.innodb\_encryption-page-compression failed in buildbot with timeout on wait condition
* [Revision #a33c9a07e5](https://github.com/MariaDB/server/commit/a33c9a07e5)\
  2017-11-13 11:36:21 +0000
  * [GAL-506](https://github.com/codership/galera/issues/506) breaks galera\_defaults MTR test by upping repl.proto\_max again. Fix this once and for all by overwriting it with constant string since it makes little sense to check for it in this test.
* Merge [Revision #2202afd541](https://github.com/MariaDB/server/commit/2202afd541) 2018-02-13 14:32:17 +0200 - Merge 10.0 into 10.1
* [Revision #c051eaba46](https://github.com/MariaDB/server/commit/c051eaba46)\
  2018-02-13 13:01:14 +0200
  * [MDEV-14988](https://jira.mariadb.org/browse/MDEV-14988) innodb\_read\_only tries to modify files if transactions were recovered in COMMITTED state
* [Revision #b88542681b](https://github.com/MariaDB/server/commit/b88542681b)\
  2018-02-10 22:17:49 +0400
  * [MDEV-14611](https://jira.mariadb.org/browse/MDEV-14611) ALTER TABLE EXCHANGE PARTITION does not work properly when used with DATA DIRECTORY.
* [Revision #a2feeb3d6f](https://github.com/MariaDB/server/commit/a2feeb3d6f)\
  2018-02-10 21:51:24 +0400
  * After-merge fixes for "sys\_vars.sysvars\_innodb '32bit,xtradb'" test results.
* Merge [Revision #e07451f71f](https://github.com/MariaDB/server/commit/e07451f71f) 2018-02-09 19:49:19 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #b0a92333c0](https://github.com/MariaDB/server/commit/b0a92333c0)\
  2018-02-09 19:47:00 +0400
  * [MDEV-15262](https://jira.mariadb.org/browse/MDEV-15262) Wrong results for SELECT..WHERE non\_indexed\_datetime\_column=indexed\_time\_column
* [Revision #6f0b316fbe](https://github.com/MariaDB/server/commit/6f0b316fbe)\
  2018-02-08 21:12:11 +0200
  * Update wrong xtradb version
* [Revision #564891c532](https://github.com/MariaDB/server/commit/564891c532)\
  2018-02-09 17:17:32 +0200
  * [MDEV-14508](https://jira.mariadb.org/browse/MDEV-14508): encryption.innodb-compressed-blob failed in buildbot, assertion in btr0cur.cc line 1398
* [Revision #b75d8453d4](https://github.com/MariaDB/server/commit/b75d8453d4)\
  2018-02-07 19:08:53 +0100
  * [MDEV-14868](https://jira.mariadb.org/browse/MDEV-14868) MariaDB server crashes after using ROLLBACK TO when encrypt\_tmp\_files=ON
* [Revision #60dfe12be3](https://github.com/MariaDB/server/commit/60dfe12be3)\
  2018-02-07 18:54:11 +0100
  * [MDEV-14868](https://jira.mariadb.org/browse/MDEV-14868) MariaDB server crashes after using ROLLBACK TO when encrypt\_tmp\_files=ON
* [Revision #47d1679ac6](https://github.com/MariaDB/server/commit/47d1679ac6)\
  2018-02-06 20:26:59 +0100
  * fix encryption.tempfiles to check that encrypt\_tmp\_files is ON
* [Revision #06d77eb43a](https://github.com/MariaDB/server/commit/06d77eb43a)\
  2018-02-08 14:55:01 +0200
  * [MDEV-14427](https://jira.mariadb.org/browse/MDEV-14427): encryption.innodb-bad-key-change failed in buildbot
* Merge [Revision #871f2a6ee2](https://github.com/MariaDB/server/commit/871f2a6ee2) 2018-02-08 13:29:08 +0200 - Merge 10.0 into 10.1
* [Revision #9216a4f69f](https://github.com/MariaDB/server/commit/9216a4f69f)\
  2018-02-08 13:26:44 +0200
  * Make the test innodb.recovery\_shutdown more robust
* [Revision #5421e3aee7](https://github.com/MariaDB/server/commit/5421e3aee7)\
  2018-02-08 12:51:19 +0200
  * [MDEV-15249](https://jira.mariadb.org/browse/MDEV-15249) Crash in MVCC read after IMPORT TABLESPACE
* [Revision #b6455479e5](https://github.com/MariaDB/server/commit/b6455479e5)\
  2018-02-07 18:14:45 +0100
  * [MDEV-15230](https://jira.mariadb.org/browse/MDEV-15230): column\_json breaks cyrillic in 10.1.31
* [Revision #b253a0c3a9](https://github.com/MariaDB/server/commit/b253a0c3a9)\
  2018-02-06 12:44:43 -0500
  * bump the VERSION
* [Revision #0c25e58db6](https://github.com/MariaDB/server/commit/0c25e58db6)\
  2018-02-06 02:38:01 +0100
  * correctly detect unsupported compiler flags
* [Revision #4418abb267](https://github.com/MariaDB/server/commit/4418abb267)\
  2018-02-06 02:33:56 +0100
  * cleanup: simplify maintainer.cmake
* [Revision #7407313f11](https://github.com/MariaDB/server/commit/7407313f11)\
  2018-02-05 16:03:28 +0100
  * silence the annoying compiler warning
* Merge [Revision #3f42529a6f](https://github.com/MariaDB/server/commit/3f42529a6f) 2018-02-05 09:25:33 +0200 - Merge 10.0 into 10.1
* [Revision #cb5374801e](https://github.com/MariaDB/server/commit/cb5374801e)\
  2018-02-05 09:23:36 +0200
  * [MDEV-15202](https://jira.mariadb.org/browse/MDEV-15202) innodb.log\_file\_size failed in buildbot

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
