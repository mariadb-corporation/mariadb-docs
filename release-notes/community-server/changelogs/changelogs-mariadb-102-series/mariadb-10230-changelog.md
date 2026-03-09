# MariaDB 10.2.30 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.30/)[Release Notes](../../old-releases/10.2/10.2.30.md)[Changelog](mariadb-10230-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 11 Dec 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.30.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.43](../changelogs-mariadb-101-series/mariadb-10143-changelog.md)
* [Revision #3cc0e0befb](https://github.com/MariaDB/server/commit/3cc0e0befb)\
  2019-12-05 01:28:11 +0200
  * List of unstable tests for 10.2.30 release
* [Revision #c9b9eb3315](https://github.com/MariaDB/server/commit/c9b9eb3315)\
  2019-12-04 11:46:37 +0200
  * [MDEV-18497](https://jira.mariadb.org/browse/MDEV-18497) : CTAS async replication from mariadb master crashes galera nodes (#1410)
* [Revision #f7d35ffc76](https://github.com/MariaDB/server/commit/f7d35ffc76)\
  2019-12-03 20:39:16 +0100
  * Galera test fix after merge.
* [Revision #ccc5e57730](https://github.com/MariaDB/server/commit/ccc5e57730)\
  2019-12-03 15:44:41 +0100
  * vew CC v 3.1
* Merge [Revision #425437b290](https://github.com/MariaDB/server/commit/425437b290) 2019-12-03 15:42:54 +0100 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #f0da39be7f](https://github.com/MariaDB/server/commit/f0da39be7f)\
  2019-11-26 19:22:46 +0100\
  \*
  * Fix [MDEV-13782](https://jira.mariadb.org/browse/MDEV-13782) Problem with NOT LIKE queries
* [Revision #fb91774e4e](https://github.com/MariaDB/server/commit/fb91774e4e)\
  2019-11-24 22:58:55 +0100
  * These changed were made after pulling 10.2.30 from origin
  * Temporarily fix [MDEV-13782](https://jira.mariadb.org/browse/MDEV-13782) by commenting out LIKE\_FUNC in CondFilter
* [Revision #b4bfa12b00](https://github.com/MariaDB/server/commit/b4bfa12b00)\
  2019-11-21 20:12:06 +0100
  * Fix compile error (missing declaration) in tabrest.cpp
* [Revision #420789512f](https://github.com/MariaDB/server/commit/420789512f)\
  2019-11-21 19:38:17 +0100
  * Fix compile error (missing declaration) in tabrest.cpp
* [Revision #7a9eca1191](https://github.com/MariaDB/server/commit/7a9eca1191)\
  2019-11-21 18:33:52 +0100
  * Fix compile error (imcomplete switch) in ha\_connect.cc
* Merge [Revision #3ad054170c](https://github.com/MariaDB/server/commit/3ad054170c) 2019-11-21 16:27:50 +0100 - These changed were made after pulling 10.2.30 from origin, Temporarily fix [MDEV-13782](https://jira.mariadb.org/browse/MDEV-13782) by commenting out LIKE\_FUNC i, CondFilter
* [Revision #9c0e462ff2](https://github.com/MariaDB/server/commit/9c0e462ff2)\
  2019-11-16 15:59:16 +0100
  * Fix missing declaration in tabrest.cpp causing compiling failure on Linux
* [Revision #2cb4b152c8](https://github.com/MariaDB/server/commit/2cb4b152c8)\
  2019-11-16 14:59:54 +0100
  * This new CONNECT version 1.07 fully implements NOSQL support. It allows working on JSON or XML data retrieved as REST query results from all binary distributions of MariaDB when cpprestsdk is installed and the GetRest library is available.
  * Make Rest available for MariaDB binary distributed versions.
  * Change RestGet function so it can be called from a library.
* Merge [Revision #f8b5e147da](https://github.com/MariaDB/server/commit/f8b5e147da) 2019-12-03 14:45:06 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #117c8146de](https://github.com/MariaDB/server/commit/117c8146de) 2019-12-03 09:39:53 +0100 - Merge branch '5.5' into 10.1
* [Revision #e3d3bbf598](https://github.com/MariaDB/server/commit/e3d3bbf598)\
  2019-11-28 15:08:29 +0100
  * Using `variables` instead of `values` in mysqld --help documentation would be more accurate
* [Revision #3cb60ec2c3](https://github.com/MariaDB/server/commit/3cb60ec2c3)\
  2019-11-29 15:50:40 +0100
  * Update `stracer` description in `mtr`. `strace-client` is not used
* [Revision #866e5c250e](https://github.com/MariaDB/server/commit/866e5c250e)\
  2018-02-11 14:42:11 +1100
  * [MDEV-15503](https://jira.mariadb.org/browse/MDEV-15503): mtr fix --strace
* [Revision #d8ace23d26](https://github.com/MariaDB/server/commit/d8ace23d26)\
  2019-10-23 17:40:24 +0500
  * Fixed some typos in mysql.cc
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
* [Revision #543f22a2d0](https://github.com/MariaDB/server/commit/543f22a2d0)\
  2019-11-27 11:58:20 +0700
  * check parameters of io\_submit() and LinuxAIOHandler::reserve\_slot()
* [Revision #88073dae79](https://github.com/MariaDB/server/commit/88073dae79)\
  2019-12-03 08:04:46 +0200
  * [MDEV-21198](https://jira.mariadb.org/browse/MDEV-21198) : Galera test failure on galera\_var\_notify\_cmd
* [Revision #3ff8fb5141](https://github.com/MariaDB/server/commit/3ff8fb5141)\
  2019-12-03 07:34:46 +0200
  * InnoDB: Remove unused get\_wkb\_of\_default\_point()
* [Revision #c6ed37b88a](https://github.com/MariaDB/server/commit/c6ed37b88a)\
  2019-11-30 09:48:15 +0200
  * [MDEV-21182](https://jira.mariadb.org/browse/MDEV-21182): Galera test failure on MW-284
* [Revision #3fb0fe400c](https://github.com/MariaDB/server/commit/3fb0fe400c)\
  2019-11-29 21:25:52 +0000
  * MENT-510 Failing test(s): perfschema.threads\_insert\_delayed.
* [Revision #bd11bd63cc](https://github.com/MariaDB/server/commit/bd11bd63cc)\
  2019-11-20 21:27:30 +0300
  * [MDEV-18310](https://jira.mariadb.org/browse/MDEV-18310): Aria engine: Undo phase failed with "Got error 121 when executing undo undo\_key\_delete" upon startup on datadir restored from incremental backup
* [Revision #32ce5301a9](https://github.com/MariaDB/server/commit/32ce5301a9)\
  2019-11-28 22:50:46 +0100
  * Update libmariadb
* [Revision #bfa6db38cd](https://github.com/MariaDB/server/commit/bfa6db38cd)\
  2019-11-27 09:31:47 +0400
  * MENT-510 Failing test(s): perfschema.threads\_insert\_delayed.
* [Revision #0e403db2c8](https://github.com/MariaDB/server/commit/0e403db2c8)\
  2019-11-27 09:23:00 +0400
  * MENT-237 Audit to show INSERT DELAYED for the executing user.
* [Revision #49ed1ae320](https://github.com/MariaDB/server/commit/49ed1ae320)\
  2019-11-26 22:57:55 +0700
  * fix double io\_destroy() + cleanup
* [Revision #a8395853cc](https://github.com/MariaDB/server/commit/a8395853cc)\
  2019-11-26 16:32:51 +0200
  * [MDEV-21152](https://jira.mariadb.org/browse/MDEV-21152) Bogus debug assertion btr\_pcur\_is\_after\_last\_in\_tree() in ibuf code
* [Revision #3551cd32a8](https://github.com/MariaDB/server/commit/3551cd32a8)\
  2019-04-16 22:10:05 +0800
  * [MDEV-17508](https://jira.mariadb.org/browse/MDEV-17508) Fix bug for spider when using "not like"
* [Revision #d30e51fafb](https://github.com/MariaDB/server/commit/d30e51fafb)\
  2019-11-11 15:47:42 +0300
  * cleanup Linux AIO
* [Revision #899c5bd5aa](https://github.com/MariaDB/server/commit/899c5bd5aa)\
  2019-11-18 23:26:21 +0700
  * [MDEV-20832](https://jira.mariadb.org/browse/MDEV-20832) Don't print "row size too large" warnings in error log if innodb\_strict\_mode=OFF and log\_warnings<=2
* [Revision #6718d3bc32](https://github.com/MariaDB/server/commit/6718d3bc32)\
  2018-05-25 22:16:04 +0400
  * [MDEV-21082](https://jira.mariadb.org/browse/MDEV-21082): isnan/isinf compilation errors, isfinite warnings on MacOS
* [Revision #b80df9eba2](https://github.com/MariaDB/server/commit/b80df9eba2)\
  2019-11-17 21:57:16 +0200
  * [MDEV-21069](https://jira.mariadb.org/browse/MDEV-21069) Crash on DROP TABLE if the data file is corrupted
* [Revision #bd2b05df6c](https://github.com/MariaDB/server/commit/bd2b05df6c)\
  2019-11-15 11:14:25 +0100
  * update create\_w\_max\_indexes\_128.result
* [Revision #98694ab0cb](https://github.com/MariaDB/server/commit/98694ab0cb)\
  2019-11-03 00:15:29 +0300
  * [MDEV-20949](https://jira.mariadb.org/browse/MDEV-20949) Stop issuing 'row size' error on DML
* [Revision #3b573c0783](https://github.com/MariaDB/server/commit/3b573c0783)\
  2019-11-13 09:51:28 +0200
  * Clean up mtr\_t::commit() further
* [Revision #abd45cdc38](https://github.com/MariaDB/server/commit/abd45cdc38)\
  2019-11-13 09:26:10 +0200
  * [MDEV-20934](https://jira.mariadb.org/browse/MDEV-20934): Correct a debug assertion
* [Revision #f127fb9807](https://github.com/MariaDB/server/commit/f127fb9807)\
  2019-11-12 20:05:17 +0900
  * Fix a typo in mariadb-plugin-mroonga.prerm
* [Revision #2570cb8b91](https://github.com/MariaDB/server/commit/2570cb8b91)\
  2019-11-12 15:46:57 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Clean up mtr\_t
* [Revision #dc8380b65d](https://github.com/MariaDB/server/commit/dc8380b65d)\
  2019-11-12 14:41:24 +0200
  * [MDEV-14602](https://jira.mariadb.org/browse/MDEV-14602): Cleanup recv\_dblwr\_t::find\_page()
* Merge [Revision #2350066e63](https://github.com/MariaDB/server/commit/2350066e63) 2019-11-12 14:36:37 +0200 - Merge 10.1 into 10.2
* [Revision #7df07c7666](https://github.com/MariaDB/server/commit/7df07c7666)\
  2019-11-05 15:01:29 +0530
  * [MDEV-20953](https://jira.mariadb.org/browse/MDEV-20953): binlog\_encryption.rpl\_corruption failed in buildbot due to wrong error code
* [Revision #40e65e878e](https://github.com/MariaDB/server/commit/40e65e878e)\
  2019-11-11 21:12:14 +0200
  * rpl\_semi\_sync\_gtid\_reconnect results merge
* Merge [Revision #26fd880d5e](https://github.com/MariaDB/server/commit/26fd880d5e) 2019-11-11 16:03:43 +0200 - manual merge 10.1->10.2
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
* [Revision #142442d571](https://github.com/MariaDB/server/commit/142442d571)\
  2019-11-11 14:18:50 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Cleanup XDES\_CLEAN\_BIT
* [Revision #878bc854d9](https://github.com/MariaDB/server/commit/878bc854d9)\
  2019-11-11 14:07:01 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up dict\_hdr\_create()
* [Revision #33f74e8fcf](https://github.com/MariaDB/server/commit/33f74e8fcf)\
  2019-11-11 14:02:38 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up IMPORT TABLESPACE
* [Revision #dfdd96214b](https://github.com/MariaDB/server/commit/dfdd96214b)\
  2019-11-11 13:56:55 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up btr\_root\_raise\_and\_insert()
* [Revision #fc2ca2be4e](https://github.com/MariaDB/server/commit/fc2ca2be4e)\
  2019-11-11 13:43:24 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up page allocation
* [Revision #98e1d603bf](https://github.com/MariaDB/server/commit/98e1d603bf)\
  2019-11-08 11:04:26 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Optimize writing BTR\_EXTERN\_LEN
* [Revision #3621df70ca](https://github.com/MariaDB/server/commit/3621df70ca)\
  2019-11-11 13:26:19 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up rtr\_adjust\_upper\_level()
* [Revision #29d67d051a](https://github.com/MariaDB/server/commit/29d67d051a)\
  2019-11-11 13:36:21 +0200
  * Cleanup btr\_page\_get\_prev(), btr\_page\_get\_next()
* [Revision #1d2458f813](https://github.com/MariaDB/server/commit/1d2458f813)\
  2019-11-11 13:26:19 +0200
  * [MDEV-21024](https://jira.mariadb.org/browse/MDEV-21024): Clean up rtr\_adjust\_upper\_level()
* [Revision #cbf5f6d6b5](https://github.com/MariaDB/server/commit/cbf5f6d6b5)\
  2019-11-08 09:51:11 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
