# MariaDB 10.1.21 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.21)[Release Notes](../../old-releases/10.1/10.1.21.md)[Changelog](mariadb-10121-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 18 Jan 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.21.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #f7d0304](https://github.com/MariaDB/server/commit/f7d0304) 2017-01-17 20:17:35 +0100 - Merge branch '10.0' into 10.1
* [Revision #6728aae](https://github.com/MariaDB/server/commit/6728aae) 2017-01-17 16:22:25 +0100 - Merge branch '5.5' into 10.0
* [Revision #b948b5f](https://github.com/MariaDB/server/commit/b948b5f)\
  2017-01-14 21:23:00 +0100
  * bugfix: Item\_func\_min\_max stored thd internally
* [Revision #798fcb5](https://github.com/MariaDB/server/commit/798fcb5)\
  2017-01-14 20:55:33 +0100
  * bugfix: cmp\_item\_row::alloc\_comparators() allocated on the wrong arena
* [Revision #67e2028](https://github.com/MariaDB/server/commit/67e2028)\
  2017-01-14 14:56:01 +0100
  * [MDEV-9690](https://jira.mariadb.org/browse/MDEV-9690) concurrent queries with virtual columns crash in temporal code
* [Revision #e4e801d](https://github.com/MariaDB/server/commit/e4e801d)\
  2017-01-17 11:15:21 +0100
  * connect: compilation errors and few obvious bugs
* [Revision #f797ea7](https://github.com/MariaDB/server/commit/f797ea7)\
  2017-01-16 18:47:53 +0100
  * [MDEV-11601](https://jira.mariadb.org/browse/MDEV-11601) Out-of-bounds string access in create\_schema\_table()
* [Revision #ef8003e](https://github.com/MariaDB/server/commit/ef8003e)\
  2017-01-16 18:23:02 +0100
  * [MDEV-11698](https://jira.mariadb.org/browse/MDEV-11698) Old Bug possibly not fixed; BEFORE INSERT Trigger on NOT NULL
* [Revision #e79e840](https://github.com/MariaDB/server/commit/e79e840)\
  2017-01-17 14:09:38 +0100
  * selinux fixes for 10.0->10.1 merge
* [Revision #736afe8](https://github.com/MariaDB/server/commit/736afe8)\
  2017-01-13 11:25:38 +0100
  * mysql\_install\_db enhancements to facilitate Debian bug#848616 fix
* [Revision #719e811](https://github.com/MariaDB/server/commit/719e811) 2017-01-17 17:11:28 +0100 - Merge branch '10.0' into 10.1
* [Revision #3e589d4](https://github.com/MariaDB/server/commit/3e589d4)\
  2017-01-17 12:24:55 +0100
  * [MDEV-11811](https://jira.mariadb.org/browse/MDEV-11811): dual master with parallel replication memory leak in write master
* [Revision #30a9ac4](https://github.com/MariaDB/server/commit/30a9ac4)\
  2017-01-17 15:32:41 +0400
  * [MDEV-10956](https://jira.mariadb.org/browse/MDEV-10956) Strict Password Validation Breaks Replication.
* [Revision #3953c55](https://github.com/MariaDB/server/commit/3953c55) 2017-01-17 04:17:26 +0200 - Merge remote-tracking branch 'origin/10.1' into 10.1
* [Revision #0349712](https://github.com/MariaDB/server/commit/0349712)\
  2017-01-16 18:26:14 +0200
  * [MDEV-11623](https://jira.mariadb.org/browse/MDEV-11623) follow-up: Adjust one more test.
* [Revision #1e192e9](https://github.com/MariaDB/server/commit/1e192e9)\
  2017-01-17 02:35:16 +0200
  * Post merge review fixes
* [Revision #d807e415](https://github.com/MariaDB/server/commit/d807e415)\
  2017-01-17 00:37:20 +0200
  * Post merge fix sysvars\_innodb for xtradb
* [Revision #6560e9c](https://github.com/MariaDB/server/commit/6560e9c)\
  2017-01-16 12:50:12 +0200
  * [MDEV-11711](https://jira.mariadb.org/browse/MDEV-11711): ArmHF EXPLAIN JSON garbage longlong values printed
* [Revision #eddbae4](https://github.com/MariaDB/server/commit/eddbae4)\
  2017-01-16 12:49:22 +0200
  * [MDEV-11712](https://jira.mariadb.org/browse/MDEV-11712): ArmHF EXPLAIN JSON garbage longlong values printed
* [Revision #7b44c31](https://github.com/MariaDB/server/commit/7b44c31) 2017-01-16 12:18:21 +0200 - Merge remote-tracking branch 'origin/10.1' into 10.1
* [Revision #7e3f3de](https://github.com/MariaDB/server/commit/7e3f3de)\
  2017-01-16 09:15:56 +0200
  * [MDEV-11623](https://jira.mariadb.org/browse/MDEV-11623) follow-up: Adjust tests.
* [Revision #3a91dec](https://github.com/MariaDB/server/commit/3a91dec)\
  2017-01-16 02:36:31 +0200
  * 101\_compatibility test fails on CentOS 5
* [Revision #34c89d0](https://github.com/MariaDB/server/commit/34c89d0)\
  2017-01-16 01:27:26 +0200
  * Updated list of unstable tests for 10.1.21
* [Revision #ab1e6fef](https://github.com/MariaDB/server/commit/ab1e6fef)\
  2017-01-14 00:13:16 +0200
  * [MDEV-11623](https://jira.mariadb.org/browse/MDEV-11623) [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) fails to start datadir created with [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)/MySQL 5.6 using innodb-page-size!=16K
* [Revision #a9d00db](https://github.com/MariaDB/server/commit/a9d00db)\
  2017-01-15 14:20:16 +0200
  * [MDEV-11799](https://jira.mariadb.org/browse/MDEV-11799) InnoDB can abort if the doublewrite buffer contains a bad and a good copy
* [Revision #9b99d9b](https://github.com/MariaDB/server/commit/9b99d9b)\
  2017-01-14 17:52:33 +0200
  * [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139): Disable a randomly failing test until the code is fixed.
* [Revision #5dfab33](https://github.com/MariaDB/server/commit/5dfab33)\
  2017-01-12 00:33:21 +0100
  * [MDEV-11551](https://jira.mariadb.org/browse/MDEV-11551) Server crashes in Field::is\_real\_null
* [Revision #7e2f9d0](https://github.com/MariaDB/server/commit/7e2f9d0)\
  2016-12-12 01:01:56 +0100
  * max\_session\_mem\_used server variable
* [Revision #ab3388c](https://github.com/MariaDB/server/commit/ab3388c)\
  2016-12-12 01:00:45 +0100
  * bugfix: mutex order violation in embedded
* [Revision #1282eb6](https://github.com/MariaDB/server/commit/1282eb6)\
  2016-12-11 17:16:15 +0100
  * cleanup: make malloc\_size\_cb\_func always defined
* [Revision #5ac71d4](https://github.com/MariaDB/server/commit/5ac71d4) 2017-01-16 04:53:57 +0200 - Merge remote-tracking branch '10.0-galera' into 10.1
* [Revision #5fc1ba6](https://github.com/MariaDB/server/commit/5fc1ba6)\
  2017-01-13 13:57:17 -0500
  * Fix for post-merge build failure.
* [Revision #ee8b5c3](https://github.com/MariaDB/server/commit/ee8b5c3) 2017-01-13 13:53:59 -0500 - Merge tag 'mariadb-10.0.29' into 10.0-galera
* [Revision #1154433](https://github.com/MariaDB/server/commit/1154433)\
  2016-12-27 14:13:32 +0530
  * [MDEV-11636](https://jira.mariadb.org/browse/MDEV-11636) Extra persistent columns on slave always gets NULL in RBR
* [Revision #be430b8](https://github.com/MariaDB/server/commit/be430b8)\
  2016-12-21 09:34:37 +0530
  * [MDEV-11490](https://jira.mariadb.org/browse/MDEV-11490) Galera\_3nodes test suite does not suppress Warnings.
* [Revision #4c1e181](https://github.com/MariaDB/server/commit/4c1e181)\
  2016-12-14 15:22:04 +0530
  * [MDEV-11479](https://jira.mariadb.org/browse/MDEV-11479) Improved wsrep\_dirty\_reads
* [Revision #ffdd1e9](https://github.com/MariaDB/server/commit/ffdd1e9)\
  2016-12-14 13:57:05 +0530
  * Revert "[MDEV-11016](https://jira.mariadb.org/browse/MDEV-11016) wsrep\_node\_is\_ready() check is too strict"
* [Revision #e156ea1](https://github.com/MariaDB/server/commit/e156ea1)\
  2016-12-09 12:15:41 -0500
  * Fix failing tests.
* [Revision #55b4579](https://github.com/MariaDB/server/commit/55b4579)\
  2016-12-05 16:28:29 -0500
  * Fix build failure.
* [Revision #52ea5ad](https://github.com/MariaDB/server/commit/52ea5ad)\
  2016-12-01 11:24:04 +0530
  * [MDEV-11016](https://jira.mariadb.org/browse/MDEV-11016) wsrep\_node\_is\_ready() check is too strict
* [Revision #41e11a8](https://github.com/MariaDB/server/commit/41e11a8)\
  2016-11-07 10:25:03 -0500
  * bump the VERSION
* [Revision #c7e1c89](https://github.com/MariaDB/server/commit/c7e1c89)\
  2016-11-02 21:10:39 -0400
  * Disable unstable galera\_concurrent\_ctas test.
* [Revision #7971360](https://github.com/MariaDB/server/commit/7971360)\
  2016-11-02 21:08:44 -0400
  * Fix a build failure noticed on Yakkety.
* [Revision #8e15768](https://github.com/MariaDB/server/commit/8e15768) 2017-01-16 03:18:14 +0200 - Merge branch '10.0' into 10.1
* [Revision #66744f4](https://github.com/MariaDB/server/commit/66744f4) 2017-01-14 19:56:00 +0200 - Merge branch '5.5' into 10.0
* [Revision #20ca1bc](https://github.com/MariaDB/server/commit/20ca1bc)\
  2017-01-12 13:54:21 +0100
  * [MDEV-11527](https://jira.mariadb.org/browse/MDEV-11527) Virtual columns do not get along well with NO\_ZERO\_DATE
* [Revision #0d1d0d7](https://github.com/MariaDB/server/commit/0d1d0d7)\
  2017-01-11 19:12:21 +0100
  * [MDEV-11706](https://jira.mariadb.org/browse/MDEV-11706) Assertion \`is\_stat\_field || !table || (!table->write\_set || bitmap\_is\_set(table->write\_set, field\_index) || (table->vcol\_set && bitmap\_is\_set(table->vcol\_set, field\_index)))' failed in Field\_time::store\_TIME\_with\_warning
* [Revision #939d125](https://github.com/MariaDB/server/commit/939d125)\
  2017-01-13 10:15:28 -0500
  * bump the VERSION
* [Revision #4f53384](https://github.com/MariaDB/server/commit/4f53384) 2017-01-12 03:37:35 +0200 - Merge branch 'bb-10.0-vicentiu' into 10.0
* [Revision #1c5ca7c](https://github.com/MariaDB/server/commit/1c5ca7c) 2017-01-12 03:36:45 +0200 - Merge branch '5.5' into 10.0
* [Revision #ab93a4d](https://github.com/MariaDB/server/commit/ab93a4d)\
  2017-01-11 09:05:36 -0500
  * [MDEV-11685](https://jira.mariadb.org/browse/MDEV-11685): sql\_mode can't be set with non-ascii connection charset
* [Revision #c1a23cd](https://github.com/MariaDB/server/commit/c1a23cd)\
  2017-01-10 18:31:03 +0100
  * [MDEV-11676](https://jira.mariadb.org/browse/MDEV-11676) Starting service with mysqld\_safe\_helper fails in SELINUX "enforcing" mode
* [Revision #6ad3dd6](https://github.com/MariaDB/server/commit/6ad3dd6)\
  2017-01-10 14:19:11 +0100
  * mysqld\_safe: don't close stdout if set -x
* [Revision #9a4bc0d](https://github.com/MariaDB/server/commit/9a4bc0d)\
  2017-01-03 16:38:56 +0200
  * Update mysql\_secure\_installation man page
* [Revision #4799af0](https://github.com/MariaDB/server/commit/4799af0)\
  2017-01-10 14:20:43 +0200
  * Fix unit test after merge from mysql 5.5.35 perfschema
* [Revision #d00d46f](https://github.com/MariaDB/server/commit/d00d46f) 2017-01-10 12:34:51 +0200 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #3e63fde](https://github.com/MariaDB/server/commit/3e63fde)\
  2017-01-09 14:19:02 +0400
  * Adding LOAD DATA tests for [MDEV-11079](https://jira.mariadb.org/browse/MDEV-11079) and [MDEV-11631](https://jira.mariadb.org/browse/MDEV-11631)
* [Revision #ecdb39a](https://github.com/MariaDB/server/commit/ecdb39a)\
  2017-01-10 12:08:36 +0200
  * Fix problems from 5.5 merge
* [Revision #94e18e2](https://github.com/MariaDB/server/commit/94e18e2) 2017-01-10 12:32:54 +0200 - Merge remote-tracking branch 'merge/merge-perfschema-5.6' into 10.0
* [Revision #c33db2c](https://github.com/MariaDB/server/commit/c33db2c)\
  2017-01-07 15:53:37 +0200
  * 5.6.35
* [Revision #ae47336](https://github.com/MariaDB/server/commit/ae47336)\
  2016-10-25 16:59:57 +0200
  * 5.6.34
* [Revision #682d484](https://github.com/MariaDB/server/commit/682d484) 2017-01-07 14:38:21 +0200 - Merge remote-tracking branch 'merge/merge-innodb-5.6' into 10.0
* [Revision #6ac84d9](https://github.com/MariaDB/server/commit/6ac84d9)\
  2017-01-07 14:24:42 +0200
  * 5.6.35
* [Revision #31d8c92](https://github.com/MariaDB/server/commit/31d8c92)\
  2016-10-25 16:58:47 +0200
  * 5.6.34
* [Revision #1a55455](https://github.com/MariaDB/server/commit/1a55455) 2017-01-06 20:24:50 +0200 - Merge remote-tracking branch 'connect/10.0' into bb-10.0-vicentiu
* [Revision #4314768](https://github.com/MariaDB/server/commit/4314768)\
  2016-12-25 12:32:05 +0100
  * Modified version number
* [Revision #6d2d0a7](https://github.com/MariaDB/server/commit/6d2d0a7) 2016-12-24 18:19:21 +0100 - Merge branch '10.0' of [server](https://github.com/MariaDB/server) into ob-10.0
* [Revision #e6b563f](https://github.com/MariaDB/server/commit/e6b563f)\
  2016-12-23 16:58:32 +0100
  * Fix some XML table type bugs: - in DOMNODELIST::DropItem if (Listp == NULL || Listp->length <= n) return true; is wrong, should be: if (Listp == NULL || Listp->length < n) return true; - Crash in discovery with libxml2 in XMLColumns because: if (!tdp->Usedom) nl was destroyed vp->nl = vp->pn->GetChildElements(g); is executed with vp->pn uninitialized. Fixed by adding: vp->pn = node; line 264. -In discovery with libxml2 some columns are not found. Because list was not recovered properly, nodes being modified and not reallocated. Fixed lines 214 and 277.
* [Revision #9523065](https://github.com/MariaDB/server/commit/9523065)\
  2016-12-14 14:20:23 +0100\
  \*
  * [MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295): developing handling files contained in ZIP file. Enable using multiple zip files
* [Revision #d44723e](https://github.com/MariaDB/server/commit/d44723e)\
  2016-12-12 10:57:19 +0100\
  \*
  * [MDEV-11295](https://jira.mariadb.org/browse/MDEV-11295): developing handling files contained in ZIP file. A first experimental and limited implementation
* [Revision #599d8cc](https://github.com/MariaDB/server/commit/599d8cc)\
  2016-12-02 23:03:43 +0100\
  \*
  * [MDEV-11366](https://jira.mariadb.org/browse/MDEV-11366) SIGBUS errors in Connect Storage Engine for ArmHF and MIPS. Fix includes launchpad fix plus more to cover writing BIN tables
* [Revision #2d78b25](https://github.com/MariaDB/server/commit/2d78b25)\
  2016-11-27 14:42:37 +0100\
  \*
  * Fix null pointer java error when connecting to jdbc:drill driver. By setting the context class loader
* [Revision #aae6753](https://github.com/MariaDB/server/commit/aae6753)\
  2016-11-14 19:20:40 +0100\
  \*
  * [MDEV-11051](https://jira.mariadb.org/browse/MDEV-11051) place Java classes ApacheInterface and JdbcInterface into single jar file. Try to fix the INSTALL command
* [Revision #5884aa1](https://github.com/MariaDB/server/commit/5884aa1)\
  2016-11-06 14:57:27 +0100\
  \*
  * Fix [MDEV-11234](https://jira.mariadb.org/browse/MDEV-11234). Escape quoting character. Should be doubled. Now it is also possible to escape it by a backslash
* [Revision #e9aed13](https://github.com/MariaDB/server/commit/e9aed13) 2017-01-06 17:09:59 +0200 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #ae1b3d1](https://github.com/MariaDB/server/commit/ae1b3d1)\
  2017-01-05 13:54:31 -0800
  * Fixed bug [MDEV-10705](https://jira.mariadb.org/browse/MDEV-10705).
* [Revision #9e528d4](https://github.com/MariaDB/server/commit/9e528d4)\
  2017-01-05 17:38:55 +0200
  * [MDEV-11727](https://jira.mariadb.org/browse/MDEV-11727) Sequences of tests fail with valgrind warnings in buildbot
* [Revision #5302ef2](https://github.com/MariaDB/server/commit/5302ef2)\
  2017-01-01 23:13:04 +0200
  * [MDEV-11700](https://jira.mariadb.org/browse/MDEV-11700) funcs\_2.innodb\_charset fails in buldbot on valgrind builder with timeout
* [Revision #f1ee011](https://github.com/MariaDB/server/commit/f1ee011)\
  2017-01-04 23:05:22 +0200
  * [MDEV-11722](https://jira.mariadb.org/browse/MDEV-11722) main.join\_cache fails in buildbot on very slow builders
* [Revision #f4d12c1](https://github.com/MariaDB/server/commit/f4d12c1)\
  2017-01-04 13:36:55 +0100
  * [MDEV-11676](https://jira.mariadb.org/browse/MDEV-11676) Starting service with mysqld\_safe\_helper fails in SELINUX "enforcing" mode
* [Revision #e5d7fc9](https://github.com/MariaDB/server/commit/e5d7fc9)\
  2017-01-04 13:03:30 +0200
  * [MDEV-10100](https://jira.mariadb.org/browse/MDEV-10100) main.pool\_of\_threads fails sporadically in buildbot
* [Revision #0912fbb](https://github.com/MariaDB/server/commit/0912fbb)\
  2017-01-04 03:33:39 +0200
  * [MDEV-11719](https://jira.mariadb.org/browse/MDEV-11719) main.subselect\_no\_exists\_to\_in failed in buildbot
* [Revision #2718225](https://github.com/MariaDB/server/commit/2718225)\
  2016-12-24 09:47:55 -0500
  * bump the VERSION
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
* [Revision #ebb8c9f](https://github.com/MariaDB/server/commit/ebb8c9f)\
  2017-01-12 15:16:45 +0400
  * [MDEV-11030](https://jira.mariadb.org/browse/MDEV-11030) Assertion \`precision > 0' failed in decimal\_bin\_size
* [Revision #2dc5d8b](https://github.com/MariaDB/server/commit/2dc5d8b)\
  2017-01-12 12:33:46 +0200
  * Improve an [MDEV-9011](https://jira.mariadb.org/browse/MDEV-9011) test of innodb\_encrypt\_log.
* [Revision #4507f1e](https://github.com/MariaDB/server/commit/4507f1e)\
  2017-01-11 14:26:30 +0200
  * Remove an excessive copyright message.
* [Revision #5b5bce8](https://github.com/MariaDB/server/commit/5b5bce8) 2017-01-11 14:19:06 +0200 - Merge 10.0 into 10.1
* [Revision #833fda8f](https://github.com/MariaDB/server/commit/833fda8f)\
  2017-01-11 14:13:30 +0200
  * InnoDB: Enable UNIV\_DEBUG\_VALGRIND for cmake -DWITH\_VALGRIND
* [Revision #f516db3](https://github.com/MariaDB/server/commit/f516db3)\
  2017-01-11 04:45:47 +0200
  * Updated list of unstable tests for 10.0.29 release
* [Revision #5044dae](https://github.com/MariaDB/server/commit/5044dae) 2017-01-10 14:30:11 +0200 - Merge 10.0 into 10.1
* [Revision #78e6faf](https://github.com/MariaDB/server/commit/78e6faf)\
  2017-01-10 14:11:32 +0200
  * Fix an innodb\_plugin leak noted in [MDEV-11686](https://jira.mariadb.org/browse/MDEV-11686)
* [Revision #171e59e](https://github.com/MariaDB/server/commit/171e59e)\
  2017-01-09 23:37:42 +0400
  * [MDEV-11548](https://jira.mariadb.org/browse/MDEV-11548) Reproducible server crash after the 2nd ALTER TABLE ADD FOREIGN KEY IF NOT EXISTS.
* [Revision #eed319b](https://github.com/MariaDB/server/commit/eed319b)\
  2017-01-08 17:51:36 +0200
  * [MDEV-11317](https://jira.mariadb.org/browse/MDEV-11317): `! is_set()' or` !is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' fails in Diagnostics\_area::set\_ok\_status on CREATE OR REPLACE with ARCHIVE table
* [Revision #eaf6b05](https://github.com/MariaDB/server/commit/eaf6b05)\
  2017-01-04 22:41:43 +0100
  * [MDEV-11087](https://jira.mariadb.org/browse/MDEV-11087) Search path for my.ini is wrong for default installation Add \<install\_root>/data/my.ini to the search path - this my.ini location is used since [MariaDB 5.2](../../old-releases/5.2/changes-improvements-in-mariadb-5-2.md)
* [Revision #82b8741](https://github.com/MariaDB/server/commit/82b8741)\
  2017-01-04 22:50:48 +0100
  * Windows : use meaningful DEFAULT\_MYSQL\_HOME - base directory for the default installation.
* [Revision #ae6eb7a](https://github.com/MariaDB/server/commit/ae6eb7a)\
  2017-01-04 23:04:37 +0100
  * [MDEV-11088](https://jira.mariadb.org/browse/MDEV-11088) Client plugins cannot be loaded by command line tools in default installation.
* [Revision #e4978d2](https://github.com/MariaDB/server/commit/e4978d2)\
  2016-07-25 16:06:52 +0300
  * [MDEV-9084](https://jira.mariadb.org/browse/MDEV-9084) Calling a stored function from a nested select from temporary table causes unpredictable behavior
* [Revision #43378f3](https://github.com/MariaDB/server/commit/43378f3)\
  2016-07-25 13:07:50 +0200
  * [MDEV-10271](https://jira.mariadb.org/browse/MDEV-10271): Stopped SQL slave thread doesn't print a message to error log like IO thread does
* [Revision #670b858](https://github.com/MariaDB/server/commit/670b858)\
  2017-01-01 15:36:56 +0200
  * Replication tests fail on valgrind due to waiting-related timeouts
* [Revision #b2b6cf4](https://github.com/MariaDB/server/commit/b2b6cf4)\
  2017-01-04 19:11:13 +0200
  * [MDEV-10988](https://jira.mariadb.org/browse/MDEV-10988) Sphinx test suite refuses to run silently
* [Revision #4b05d60](https://github.com/MariaDB/server/commit/4b05d60)\
  2017-01-09 09:15:21 +0200
  * Make encryption.innodb\_lotoftables more robust.
* [Revision #59ea645](https://github.com/MariaDB/server/commit/59ea645)\
  2017-01-09 09:12:32 +0200
  * Minor cleanup of innodb.innodb-change-buffer-recovery
* [Revision #384f4d1](https://github.com/MariaDB/server/commit/384f4d1)\
  2017-01-07 15:27:59 +0200
  * Post-push fix for [MDEV-11556](https://jira.mariadb.org/browse/MDEV-11556): Make the debug variable UINT.
* [Revision #8049d2e](https://github.com/MariaDB/server/commit/8049d2e) 2017-01-05 20:32:15 +0200 - Merge 10.0 into 10.1
* [Revision #f0c19b6](https://github.com/MariaDB/server/commit/f0c19b6)\
  2017-01-05 20:13:34 +0200
  * [MDEV-11730](https://jira.mariadb.org/browse/MDEV-11730) Memory leak in innodb.innodb\_corrupt\_bit
* [Revision #9bf92706d1](https://github.com/MariaDB/server/commit/9bf92706d1)\
  2017-01-01 19:35:44 +0200
  * [MDEV-8518](https://jira.mariadb.org/browse/MDEV-8518) rpl.sec\_behind\_master-5114 fails sporadically in buildbot
* [Revision #bc4cac3](https://github.com/MariaDB/server/commit/bc4cac3)\
  2017-01-04 13:26:09 +0100
  * [MDEV-10035](https://jira.mariadb.org/browse/MDEV-10035): DBUG\_ASSERT on CREATE VIEW v1 AS SELECT \* FROM t1 FOR UPDATE
* [Revision #fb5ee7d](https://github.com/MariaDB/server/commit/fb5ee7d)\
  2017-01-05 19:01:14 +0200
  * Plug a memory leak in buf\_dblwr\_process().
* [Revision #758af98](https://github.com/MariaDB/server/commit/758af98)\
  2017-01-05 10:42:19 +0200
  * Post-push fix for Part 1 of [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139) Fix scrubbing tests
* [Revision #ffb38c9](https://github.com/MariaDB/server/commit/ffb38c9)\
  2017-01-04 20:49:13 +0200
  * [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139) Fix scrubbing tests
* [Revision #719321e](https://github.com/MariaDB/server/commit/719321e)\
  2017-01-04 18:43:32 +0200
  * [MDEV-11638](https://jira.mariadb.org/browse/MDEV-11638) Encryption causes race conditions in InnoDB shutdown
* [Revision #0f8e17a](https://github.com/MariaDB/server/commit/0f8e17a)\
  2017-01-04 18:16:37 +0200
  * Part 1 of [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139) Fix scrubbing tests
* [Revision #0c1de94](https://github.com/MariaDB/server/commit/0c1de94) 2017-01-04 13:56:11 +0200 - Merge 10.0 into 10.1
* [Revision #80d5d14](https://github.com/MariaDB/server/commit/80d5d14)\
  2017-01-03 19:32:47 +0200
  * [MDEV-11694](https://jira.mariadb.org/browse/MDEV-11694) InnoDB tries to create unused table SYS\_ZIP\_DICT
* [Revision #3871477](https://github.com/MariaDB/server/commit/3871477)\
  2017-01-01 20:06:03 +0200
  * [MDEV-10100](https://jira.mariadb.org/browse/MDEV-10100) main.pool\_of\_threads fails sporadically in buildbot
* [Revision #d02a77b](https://github.com/MariaDB/server/commit/d02a77b)\
  2016-12-27 14:13:32 +0530
  * [MDEV-11636](https://jira.mariadb.org/browse/MDEV-11636) Extra persistent columns on slave always gets NULL in RBR
* [Revision #37f294f](https://github.com/MariaDB/server/commit/37f294f)\
  2016-12-27 03:21:13 +0200
  * Disable the test for valgrind builds
* [Revision #ba8198a](https://github.com/MariaDB/server/commit/ba8198a)\
  2017-01-03 15:44:44 +0200
  * Post-fix for [MDEV-11688](https://jira.mariadb.org/browse/MDEV-11688) fil\_crypt\_threads\_end() tries to create threads
* [Revision #fc77925](https://github.com/MariaDB/server/commit/fc77925)\
  2017-01-03 13:18:47 +0200
  * [MDEV-11688](https://jira.mariadb.org/browse/MDEV-11688) fil\_crypt\_threads\_end() tries to create threads after aborted InnoDB startup
* [Revision #b4616c4](https://github.com/MariaDB/server/commit/b4616c4)\
  2017-01-03 10:45:55 +0530
  * [MDEV-7955](https://jira.mariadb.org/browse/MDEV-7955) WSREP() appears on radar in OLTP RO
* [Revision #d9a1a20](https://github.com/MariaDB/server/commit/d9a1a20)\
  2017-01-03 10:10:58 +0530
  * [MDEV-11016](https://jira.mariadb.org/browse/MDEV-11016) wsrep\_node\_is\_ready() check is too strict
* [Revision #2f5670d](https://github.com/MariaDB/server/commit/2f5670d)\
  2016-12-27 14:13:32 +0530
  * [MDEV-11636](https://jira.mariadb.org/browse/MDEV-11636) Extra persistent columns on slave always gets NULL in RBR
* [Revision #8451e09](https://github.com/MariaDB/server/commit/8451e09)\
  2016-12-28 12:05:43 +0200
  * [MDEV-11556](https://jira.mariadb.org/browse/MDEV-11556) InnoDB redo log apply fails to adjust data file sizes
* [Revision #f493e39](https://github.com/MariaDB/server/commit/f493e39)\
  2016-12-29 15:03:12 +0200
  * Make the test work with any innodb\_page\_size.
* [Revision #23cc1be270](https://github.com/MariaDB/server/commit/23cc1be270)\
  2016-12-21 20:11:14 +0100
  * [MDEV-11584](https://jira.mariadb.org/browse/MDEV-11584): GRANT inside an SP does not work well on 2nd execution
* [Revision #283e9cf4cb](https://github.com/MariaDB/server/commit/283e9cf4cb)\
  2016-12-28 16:14:28 +0200
  * [MDEV-11656](https://jira.mariadb.org/browse/MDEV-11656): 'Data structure corruption' IMPORT TABLESPACE doesn't work for encrypted InnoDB tables if space\_id changed
* [Revision #d50cf42](https://github.com/MariaDB/server/commit/d50cf42)\
  2016-12-28 15:54:24 +0200
  * [MDEV-9282](https://jira.mariadb.org/browse/MDEV-9282) Debian: the Lintian complains about "shlib-calls-exit" in ha\_innodb.so
* [Revision #dc9f5df](https://github.com/MariaDB/server/commit/dc9f5df)\
  2016-12-27 20:41:32 +0200
  * Replication tests fail on valgrind due to waiting-related timeouts
* [Revision #545c912](https://github.com/MariaDB/server/commit/545c912)\
  2016-12-22 12:03:36 +0200
  * Remove an unnecessary comparison.
* [Revision #7e02fd1](https://github.com/MariaDB/server/commit/7e02fd1)\
  2016-12-22 14:20:47 +0200
  * [MDEV-11630](https://jira.mariadb.org/browse/MDEV-11630) Call mutex\_free() before freeing the mutex list
* [Revision #55eb712](https://github.com/MariaDB/server/commit/55eb712)\
  2016-12-22 14:02:51 +0200
  * [MDEV-11218](https://jira.mariadb.org/browse/MDEV-11218): encryption.innodb\_encryption\_discard\_import failed in buildbot
* [Revision #c51c885](https://github.com/MariaDB/server/commit/c51c885)\
  2016-12-21 22:41:07 +0200
  * Fixed compiler warning
* [Revision #c33c638](https://github.com/MariaDB/server/commit/c33c638)\
  2016-12-21 22:40:52 +0200
  * [MDEV-7558](https://jira.mariadb.org/browse/MDEV-7558) analyze\_stmt\_slow\_query\_log fails sporadically in buildbot
* [Revision #9e032d6](https://github.com/MariaDB/server/commit/9e032d6)\
  2016-12-21 09:34:37 +0530
  * [MDEV-11490](https://jira.mariadb.org/browse/MDEV-11490) Galera\_3nodes test suite does not suppress Warnings.
* [Revision #75ab65a](https://github.com/MariaDB/server/commit/75ab65a)\
  2016-12-20 15:31:02 -0500
  * Fix failing galera tests.
* [Revision #195241e](https://github.com/MariaDB/server/commit/195241e)\
  2016-12-20 15:03:56 +0200
  * Port the test innodb.doublewrite from MySQL 5.7.
* [Revision #44da95e](https://github.com/MariaDB/server/commit/44da95e) 2016-12-19 17:15:25 +0200 - Merge branch '10.0' into 10.1
* [Revision #9f863a1](https://github.com/MariaDB/server/commit/9f863a1)\
  2016-12-19 15:57:41 +0200
  * [MDEV-11602](https://jira.mariadb.org/browse/MDEV-11602) InnoDB leaks foreign key metadata on DDL operations
* [Revision #8e19833](https://github.com/MariaDB/server/commit/8e19833)\
  2016-12-15 10:34:41 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
