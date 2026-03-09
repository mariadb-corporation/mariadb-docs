# MariaDB 10.1.44 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.44)[Release Notes](../../old-releases/10.1/10.1.44.md)[Changelog](mariadb-10144-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 28 Jan 2020

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.44.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 5.5.67](../changelogs-mariadb-55-series/mariadb-5567-changelog.md)
* [Revision #84d4005bad](https://github.com/MariaDB/server/commit/84d4005bad)\
  2020-01-25 23:50:41 +0200
  * List of unstable tests for 10.1.44 release
* [Revision #599a06098b](https://github.com/MariaDB/server/commit/599a06098b)\
  2020-01-24 13:35:03 +0530
  * [MDEV-21490](https://jira.mariadb.org/browse/MDEV-21490): binlog tests fail with valgrind: Conditional jump or move depends on uninitialised value in sql\_ex\_info::init
* [Revision #982294ac16](https://github.com/MariaDB/server/commit/982294ac16)\
  2020-01-14 13:57:14 +0100
  * [MDEV-17601](https://jira.mariadb.org/browse/MDEV-17601): MariaDB Galera does not expect 'mbstream' as streamfmt
* [Revision #578b6ba02a](https://github.com/MariaDB/server/commit/578b6ba02a)\
  2020-01-14 14:23:15 +0100
  * [MDEV-19457](https://jira.mariadb.org/browse/MDEV-19457): sys\_vars.wsrep\_provider\_basic failed in buildbot
* Merge [Revision #7993f893b8](https://github.com/MariaDB/server/commit/7993f893b8) 2020-01-19 14:37:25 +0100 - Merge branch 'merge-tokudb-5.6' into 10.1
* [Revision #6cb208107e](https://github.com/MariaDB/server/commit/6cb208107e)\
  2020-01-19 14:08:35 +0100
  * 5.6.46-86.2
* Merge [Revision #10eacd5ff7](https://github.com/MariaDB/server/commit/10eacd5ff7) 2020-01-19 13:11:45 +0100 - Merge branch 'merge-perfschema-5.6' into 10.1
* [Revision #3aff3f3679](https://github.com/MariaDB/server/commit/3aff3f3679)\
  2020-01-19 12:52:07 +0100
  * 5.6.47
* Merge [Revision #5ce6ec3fb5](https://github.com/MariaDB/server/commit/5ce6ec3fb5) 2020-01-19 12:27:44 +0100 - Merge remote-tracking branch 'connect/10.1' into 10.1
* [Revision #85f2217cc8](https://github.com/MariaDB/server/commit/85f2217cc8)\
  2020-01-12 00:52:46 +0100
  * Update grant tests for new MariaDB version 10.1.44
* Merge [Revision #54449161f8](https://github.com/MariaDB/server/commit/54449161f8) 2020-01-11 18:34:57 +0100 - Merge with last MariaDB version
* [Revision #98f70fa26b](https://github.com/MariaDB/server/commit/98f70fa26b)\
  2020-01-11 16:05:39 +0100
  * Fix [MDEV-21450](https://jira.mariadb.org/browse/MDEV-21450) Failed compile when XML table type is not supported. Was because XMLDEF was unconditionally called from REST table.
* [Revision #0b624debdf](https://github.com/MariaDB/server/commit/0b624debdf)\
  2020-01-09 16:10:25 +0100
  * Update to version 1.07 (as for [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md))
* Merge [Revision #f31bf6f094](https://github.com/MariaDB/server/commit/f31bf6f094) 2020-01-19 12:22:12 +0100 - Merge branch '5.5' into 10.1
* [Revision #02af6278fb](https://github.com/MariaDB/server/commit/02af6278fb)\
  2020-01-17 17:39:20 +0200
  * InnoDB 5.6.47 and XtraDB 5.6.46-86.2
* [Revision #bde7e0ba6e](https://github.com/MariaDB/server/commit/bde7e0ba6e)\
  2020-01-16 11:40:21 +0200
  * [MDEV-21500](https://jira.mariadb.org/browse/MDEV-21500) Server hang when using simulated AIO
* [Revision #23041af720](https://github.com/MariaDB/server/commit/23041af720)\
  2020-01-15 16:35:59 +0300
  * [MDEV-21341](https://jira.mariadb.org/browse/MDEV-21341): Fix UBSAN failures, part 8: fix error in compare\_fields\_by\_table\_order
* [Revision #4635047ca1](https://github.com/MariaDB/server/commit/4635047ca1)\
  2020-01-15 16:34:51 +0300
  * [MDEV-21341](https://jira.mariadb.org/browse/MDEV-21341): Fix UBSAN failures, part #5
* [Revision #5e5ae51b73](https://github.com/MariaDB/server/commit/5e5ae51b73)\
  2020-01-12 20:50:12 +0200
  * [MDEV-21341](https://jira.mariadb.org/browse/MDEV-21341): Fix UBSAN failures: Issue Six
* [Revision #cb204e11ea](https://github.com/MariaDB/server/commit/cb204e11ea)\
  2020-01-07 18:26:53 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #d05c511d34](https://github.com/MariaDB/server/commit/d05c511d34)\
  2019-12-18 15:04:06 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #bac3353361](https://github.com/MariaDB/server/commit/bac3353361)\
  2019-12-18 15:03:32 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #2187f1c2ca](https://github.com/MariaDB/server/commit/2187f1c2ca)\
  2019-12-18 15:02:56 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #d6fa69e4be](https://github.com/MariaDB/server/commit/d6fa69e4be)\
  2019-12-18 15:02:23 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #15781283eb](https://github.com/MariaDB/server/commit/15781283eb)\
  2019-12-18 15:01:48 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #a42ef10815](https://github.com/MariaDB/server/commit/a42ef10815)\
  2019-12-18 15:01:19 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #5a54e84e5d](https://github.com/MariaDB/server/commit/5a54e84e5d)\
  2019-12-18 15:00:47 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #913f405d95](https://github.com/MariaDB/server/commit/913f405d95)\
  2019-12-18 15:00:20 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #a6dd827a4d](https://github.com/MariaDB/server/commit/a6dd827a4d)\
  2019-12-18 14:59:44 +0530
  * [MDEV-18046](https://jira.mariadb.org/browse/MDEV-18046): Assortment of crashes, assertion failures and ASAN errors in mysql\_show\_binlog\_events
* [Revision #1adc559370](https://github.com/MariaDB/server/commit/1adc559370)\
  2020-01-03 22:54:28 +0530
  * Making group\_by test stable
* Merge [Revision #4d7f073506](https://github.com/MariaDB/server/commit/4d7f073506) 2020-01-03 10:36:23 +0100 - Merge branch '5.5' into 10.1
* [Revision #faf2a6e5f0](https://github.com/MariaDB/server/commit/faf2a6e5f0)\
  2019-12-31 11:00:15 +0530
  * [MDEV-20922](https://jira.mariadb.org/browse/MDEV-20922): Adding an order by changes the query results
* [Revision #359d91aaee](https://github.com/MariaDB/server/commit/359d91aaee)\
  2019-12-26 17:14:51 +0530
  * [MDEV-19680](https://jira.mariadb.org/browse/MDEV-19680):: Assertion \`!table || (!table->read\_set || bitmap\_is\_set(table->read\_set, field\_index) || (!(ptr >= table->record\[0] && ptr < table->record\[0] + table->s->reclength)))' or alike failed upon SELECT with mix of functions from simple view
* [Revision #9f7fcb9f25](https://github.com/MariaDB/server/commit/9f7fcb9f25)\
  2019-12-23 21:39:10 +0100
  * mtr: include restart\_opts in --verbose-restart
* [Revision #aade6e53d3](https://github.com/MariaDB/server/commit/aade6e53d3)\
  2019-12-20 19:47:31 +0100
  * fix a bad merge
* [Revision #1f1e3ce8a1](https://github.com/MariaDB/server/commit/1f1e3ce8a1)\
  2019-12-19 14:03:54 +0400
  * [MDEV-21319](https://jira.mariadb.org/browse/MDEV-21319) COUNT(\*) returns 1, actual SELECT returns no result in 10.3.21, but 1 result in 10.1.41
* [Revision #a5a433e256](https://github.com/MariaDB/server/commit/a5a433e256)\
  2019-12-18 23:35:33 +0800
  * fix windows compilation
* [Revision #3d3d8f1012](https://github.com/MariaDB/server/commit/3d3d8f1012)\
  2019-12-17 21:50:58 +0800
  * [MDEV-21337](https://jira.mariadb.org/browse/MDEV-21337) fix aligned\_malloc()
* [Revision #984b3c1544](https://github.com/MariaDB/server/commit/984b3c1544)\
  2019-12-18 13:11:07 +0300
  * [MDEV-21341](https://jira.mariadb.org/browse/MDEV-21341): Fix UBSAN failures, part #3
* [Revision #8b9db11718](https://github.com/MariaDB/server/commit/8b9db11718)\
  2019-12-18 12:56:54 +0300
  * [MDEV-21341](https://jira.mariadb.org/browse/MDEV-21341): Fix optimizer-related UBSAN failures, part #2
* [Revision #0ac0bc8cb6](https://github.com/MariaDB/server/commit/0ac0bc8cb6)\
  2019-12-18 12:34:14 +0300
  * [MDEV-21341](https://jira.mariadb.org/browse/MDEV-21341): Fix optimizer-related UBSAN failures, part #1:
* Merge [Revision #3d98892232](https://github.com/MariaDB/server/commit/3d98892232) 2019-12-16 13:08:17 +0400 - Merge remote-tracking branch 'origin/5.5' into 10.1
* [Revision #a3a8360d57](https://github.com/MariaDB/server/commit/a3a8360d57)\
  2019-12-12 00:05:55 +0100
  * CMake,Windows - cleanup data directory prior to bootstrap for nitial\_database target
* [Revision #8d2f6d3ca5](https://github.com/MariaDB/server/commit/8d2f6d3ca5)\
  2019-12-11 16:57:59 +0100
  * Fix overly chatty connect cmake, once again
* [Revision #e949b2d4ab](https://github.com/MariaDB/server/commit/e949b2d4ab)\
  2019-12-06 19:56:23 +0530
  * [MDEV-20959](https://jira.mariadb.org/browse/MDEV-20959): binlog.binlog\_parallel\_replication\_marks\_row fails in buildbot with wrong result
* [Revision #42bad56aab](https://github.com/MariaDB/server/commit/42bad56aab)\
  2019-12-04 22:29:33 +0700
  * [MDEV-21014](https://jira.mariadb.org/browse/MDEV-21014) MTR does not detect {A,M,T,L,UB}SAN errors which happen upon server shutdown
* [Revision #2b7e461cc0](https://github.com/MariaDB/server/commit/2b7e461cc0)\
  2019-12-05 12:39:04 +0200
  * [MDEV-21209](https://jira.mariadb.org/browse/MDEV-21209) : mysql\_tzinfo\_to\_sql's Galera checks do not work
* Merge [Revision #f00198e09f](https://github.com/MariaDB/server/commit/f00198e09f) 2019-12-05 10:37:02 +0100 - Merge branch 'bb-10.1-[MDEV-17571](https://jira.mariadb.org/browse/MDEV-17571)' of github.com:MariaDB/server into bb-10.1-[MDEV-17571](https://jira.mariadb.org/browse/MDEV-17571)
* [Revision #c5dafca87e](https://github.com/MariaDB/server/commit/c5dafca87e)\
  2019-12-04 14:28:13 +0100
  * [MDEV-17571](https://jira.mariadb.org/browse/MDEV-17571) Make systemd timeout behavior more compatible with long Galera SSTs
* [Revision #d78f02d73d](https://github.com/MariaDB/server/commit/d78f02d73d)\
  2019-12-04 14:28:13 +0100
  * [MDEV-17571](https://jira.mariadb.org/browse/MDEV-17571) Make systemd timeout behavior more compatible with long Galera SSTs
* [Revision #3efbb5a169](https://github.com/MariaDB/server/commit/3efbb5a169)\
  2019-12-04 23:40:33 +0200
  * List of unstable tests - intermediate update
* [Revision #05e72a3333](https://github.com/MariaDB/server/commit/05e72a3333)\
  2019-12-03 22:22:23 +0100
  * .clang-format - do not sort include files.
* [Revision #155a8a5215](https://github.com/MariaDB/server/commit/155a8a5215)\
  2019-12-03 22:21:05 +0100
  * .clang-format - do _not_ sort include files
* Merge [Revision #117c8146de](https://github.com/MariaDB/server/commit/117c8146de) 2019-12-03 09:39:53 +0100 - Merge branch '5.5' into 10.1
* [Revision #d930422e9e](https://github.com/MariaDB/server/commit/d930422e9e)\
  2019-11-29 13:21:23 +0100
  * Fix the line break warning (groff/lintian).
* [Revision #33cf4da183](https://github.com/MariaDB/server/commit/33cf4da183)\
  2019-11-30 18:19:20 +0700
  * cleanup: replace exit(1) with abort()
* [Revision #6fe2aae3ce](https://github.com/MariaDB/server/commit/6fe2aae3ce)\
  2019-11-30 12:14:00 +0700
  * InnoDB: log unsuccessful calls to pthread\_attr\_init() and pthread\_create() before crash
* [Revision #2855edf9ee](https://github.com/MariaDB/server/commit/2855edf9ee)\
  2019-11-23 23:26:35 +0700
  * try to fix data races in DBUG
* [Revision #6218bf1b41](https://github.com/MariaDB/server/commit/6218bf1b41)\
  2019-11-26 21:48:22 +0200
  * cracklib-runtime needs a comma after to parse properly
* [Revision #427eedd012](https://github.com/MariaDB/server/commit/427eedd012)\
  2019-11-26 19:52:37 +0200
  * [MDEV-13288](https://jira.mariadb.org/browse/MDEV-13288): Proper fix for cracklib-runtime
* [Revision #ed2379f983](https://github.com/MariaDB/server/commit/ed2379f983)\
  2019-11-25 11:08:13 +0200
  * [MDEV-13288](https://jira.mariadb.org/browse/MDEV-13288): Upstream debian patch
* [Revision #23664bc7a5](https://github.com/MariaDB/server/commit/23664bc7a5)\
  2019-11-21 10:34:36 -0500
  * Fix incorrect DBUG\_ENTER message for join\_read\_last
* [Revision #38839854b7](https://github.com/MariaDB/server/commit/38839854b7)\
  2019-11-26 08:49:50 +0200
  * [MDEV-19572](https://jira.mariadb.org/browse/MDEV-19572) async slave node fails to apply MyISAM only writes (#1418)
* [Revision #a51f3b09bb](https://github.com/MariaDB/server/commit/a51f3b09bb)\
  2019-11-21 00:32:27 +0700
  * cleanup DBUG
* [Revision #8fbfcce911](https://github.com/MariaDB/server/commit/8fbfcce911)\
  2019-11-19 17:09:43 +0700
  * cleanup: remove always true condition to fix clang warning
* [Revision #c6b097ab37](https://github.com/MariaDB/server/commit/c6b097ab37)\
  2019-11-18 15:22:01 +0200
  * Remove excessive sleep from test.
* [Revision #5c68343db7](https://github.com/MariaDB/server/commit/5c68343db7)\
  2019-11-18 15:18:00 +0200
  * [MDEV-18497](https://jira.mariadb.org/browse/MDEV-18497) CTAS async replication from mariadb master crashes galera nodes (#1410)
* [Revision #2909725636](https://github.com/MariaDB/server/commit/2909725636)\
  2019-11-18 11:50:58 +0530
  * [MDEV-21044](https://jira.mariadb.org/browse/MDEV-21044): Wrong result when using a smaller size for sort buffer
* [Revision #214023aa0e](https://github.com/MariaDB/server/commit/214023aa0e)\
  2019-01-18 13:45:06 +1100
  * systemd: mariadb@bootstrap doesn't bootstrap, galera\_new\_cluster does
* [Revision #7df07c7666](https://github.com/MariaDB/server/commit/7df07c7666)\
  2019-11-05 15:01:29 +0530
  * [MDEV-20953](https://jira.mariadb.org/browse/MDEV-20953): binlog\_encryption.rpl\_corruption failed in buildbot due to wrong error code
* [Revision #13db50fc03](https://github.com/MariaDB/server/commit/13db50fc03)\
  2019-11-06 17:05:58 +0200
  * [MDEV-19376](https://jira.mariadb.org/browse/MDEV-19376) Repl\_semi\_sync\_master::commit\_trx assertion failure: ... || !m\_active\_tranxs->is\_tranx\_end\_pos(trx\_wait\_binlog\_name, trx\_wait\_binlog\_pos)
* [Revision #dfd2d3d861](https://github.com/MariaDB/server/commit/dfd2d3d861)\
  2019-11-08 09:50:14 -0500
  * bump the VERSION
* [Revision #c4a844ca51](https://github.com/MariaDB/server/commit/c4a844ca51)\
  2019-11-08 08:03:49 +0100
  * [MDEV-20981](https://jira.mariadb.org/browse/MDEV-20981) wsrep\_sst\_mariadb-backup fails silently when mariadb-backup is not installed (#1406)
* [Revision #b1ab2ba583](https://github.com/MariaDB/server/commit/b1ab2ba583)\
  2019-11-07 15:24:21 +0530
  * [MDEV-20519](https://jira.mariadb.org/browse/MDEV-20519): Query plan regression with optimizer\_use\_condition\_selectivity > 1

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
