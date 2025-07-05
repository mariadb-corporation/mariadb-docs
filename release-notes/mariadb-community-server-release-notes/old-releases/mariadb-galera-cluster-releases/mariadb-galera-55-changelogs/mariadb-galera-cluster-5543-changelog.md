# MariaDB Galera Cluster 5.5.43 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.43)[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5543-release-notes.md)[Changelog](mariadb-galera-cluster-5543-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 15 May 2015

For the highlights of this release, see the[release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5543-release-notes.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #014fe12](https://github.com/MariaDB/server/commit/014fe12)\
  2015-05-12 14:19:30 -0400
  * Fix for debug build failure
* [Revision #18fee8b](https://github.com/MariaDB/server/commit/18fee8b)\
  2015-05-12 17:05:41 -0400
  * Revert last commit.
* [Revision #048039e](https://github.com/MariaDB/server/commit/048039e)\
  2015-05-11 15:42:20 -0400
  * Fix for build failure.
* [Revision #e1868fd](https://github.com/MariaDB/server/commit/e1868fd)\
  2015-05-07 22:18:34 +0200
  * [MDEV-8115](https://jira.mariadb.org/browse/MDEV-8115) mysql\_upgrade crashes the server with REPAIR VIEW
* [Revision #d256200](https://github.com/MariaDB/server/commit/d256200)\
  2015-05-04 13:50:52 -0400
  * Merge tag 'mariadb-5.5.43' into 5.5-galera
* [Revision #42f99d0](https://github.com/MariaDB/server/commit/42f99d0)\
  2015-03-18 21:17:31 +0200
  * codership/mysql-wsrep#67 - total order isolation for FLUSH
* [Revision #f3efc63](https://github.com/MariaDB/server/commit/f3efc63)\
  2015-02-10 18:27:21 +0200
  * refs codership/mysql-wsrep#60 explicit braces around empty body
* [Revision #70d6236](https://github.com/MariaDB/server/commit/70d6236)\
  2015-02-10 00:47:02 +0200
  * refs codership/mysql-wsrep#55 - To avoid compiler warming:
* [Revision #f6b1e0f](https://github.com/MariaDB/server/commit/f6b1e0f)\
  2015-02-05 14:38:03 +0200
  * refs #55 fixed debug build compilation errors
* [Revision #b02d736](https://github.com/MariaDB/server/commit/b02d736)\
  2014-12-10 23:29:28 +0200
  * Refs #25 - made sure signals that may be set to ignored in mysqld were set to default in the child process.
* [Revision #c72ed05](https://github.com/MariaDB/server/commit/c72ed05)\
  2014-12-10 01:45:50 +0200
  * This commit
    * improves MySQL client version check making it no less than required as opposed to exactly as required
    * adds event table copying to ensure same results as with rsync SST.
* [Revision #822c005](https://github.com/MariaDB/server/commit/822c005)\
  2014-12-09 22:13:14 +0200
  * Going more MTR-friendly - for SST prefer to use mysql client, mysqldump and my\_print\_defaults from the local build tree.
* [Revision #2a6e123](https://github.com/MariaDB/server/commit/2a6e123)\
  2015-03-30 17:58:41 -0400
  * refs #7 - handling lock queue granting in BF-BF conflict situation
* [Revision #68fe3a3](https://github.com/MariaDB/server/commit/68fe3a3)\
  2014-11-16 16:26:36 +0200
  * refs #7 - handling lock queue granting in BF-BF conflict situation
* [Revision #51744b3](https://github.com/MariaDB/server/commit/51744b3)\
  2014-10-31 15:55:18 +0800
  * Refs #8: \[5.5] preserve gvwstate.dat for pc recovery feature
* [Revision #4c87f72](https://github.com/MariaDB/server/commit/4c87f72)\
  2015-04-29 16:24:52 +0200
  * Merge branch '5.5' into bb-5.5-serg
* [Revision #a4477d2](https://github.com/MariaDB/server/commit/a4477d2)\
  2015-04-29 14:14:45 +0300
  * Fix failing test cases for [MDEV-7912](https://jira.mariadb.org/browse/MDEV-7912) patch
* [Revision #f632b51](https://github.com/MariaDB/server/commit/f632b51)\
  2015-04-28 21:27:43 +0200
  * [MDEV-7987](https://jira.mariadb.org/browse/MDEV-7987) Fatal error: Please read "Security" section of the manual to find out how to run mysqld as root!
* [Revision #6f17e23](https://github.com/MariaDB/server/commit/6f17e23)\
  2015-04-28 21:24:32 +0200
  * post-merge fixes
* [Revision #f9c02d7](https://github.com/MariaDB/server/commit/f9c02d7)\
  2015-04-28 21:11:49 +0200
  * Merge branch 'openquery/[MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916)-maria-5.5-check\_view-r4408' into 5.5
* [Revision #fbab068](https://github.com/MariaDB/server/commit/fbab068)\
  2015-04-28 13:57:21 +0200
  * post-merge changes, fixes, and tests
* [Revision #67a3ddf](https://github.com/MariaDB/server/commit/67a3ddf)\
  2015-04-28 13:54:37 +0200
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #40e9560](https://github.com/MariaDB/server/commit/40e9560)\
  2015-04-28 13:42:58 +0200
  * percona-server-5.5.42-37.1.tar.gz
* [Revision #c581ae0](https://github.com/MariaDB/server/commit/c581ae0)\
  2015-04-28 13:37:54 +0200
  * Null-merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #a5fa434](https://github.com/MariaDB/server/commit/a5fa434)\
  2015-04-28 15:31:49 +0500
  * [MDEV-7779](https://jira.mariadb.org/browse/MDEV-7779) View definition changes upon creation.
    * Fixed by using POINT instead of ST\_POINT in the item.
    * Later need to fix that with proper ST\_POINT implementation
* [Revision #4c174fc](https://github.com/MariaDB/server/commit/4c174fc)\
  2015-04-28 15:28:29 +0300
  * [MDEV-8020](https://jira.mariadb.org/browse/MDEV-8020): innodb.innodb-[MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055) produces valgrind warnings in buildbot
* [Revision #ac2b92c](https://github.com/MariaDB/server/commit/ac2b92c)\
  2015-04-28 15:09:04 +0300
  * [MDEV-7912](https://jira.mariadb.org/browse/MDEV-7912) multitable delete with wrongly set sort\_buffer\_size crashes in merge\_buffers
* [Revision #fd39c56](https://github.com/MariaDB/server/commit/fd39c56)\
  2015-04-27 23:37:51 +0200
  * move to storage/xtradb/
* [Revision #0f12ada](https://github.com/MariaDB/server/commit/0f12ada)\
  2015-04-27 21:04:06 +0200
  * Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #e4df6e5](https://github.com/MariaDB/server/commit/e4df6e5)\
  2015-04-27 16:19:54 +0200
  * Merge commit 'tokudb-engine/tokudb-7.5.6' into 5.5
* [Revision #2f446f2](https://github.com/MariaDB/server/commit/2f446f2)\
  2015-04-27 16:04:39 +0200
  * Merge commit 'tokudb-ft-index/tokudb-7.5.6' into 5.5
* [Revision #939a233](https://github.com/MariaDB/server/commit/939a233)\
  2015-04-27 15:56:39 +0200
  * Merge remote-tracking branch 'openquery/[MDEV-8060](https://jira.mariadb.org/browse/MDEV-8060)-shm-path' into 5.5
* [Revision #245cc73](https://github.com/MariaDB/server/commit/245cc73)\
  2015-04-27 12:47:39 +0200
  * [MDEV-7434](https://jira.mariadb.org/browse/MDEV-7434) XtraDB does not build on Solaris
* [Revision #e26b207](https://github.com/MariaDB/server/commit/e26b207)\
  2015-04-26 16:27:41 +0200
  * [MDEV-7938](https://jira.mariadb.org/browse/MDEV-7938) MariaDB Crashes Suddenly while writing binlogs
* [Revision #053143e](https://github.com/MariaDB/server/commit/053143e)\
  2015-04-25 21:56:46 +0200
  * [MDEV-7883](https://jira.mariadb.org/browse/MDEV-7883) Segmentation failure when running mysqladmin -u root -p
* [Revision #18215dd](https://github.com/MariaDB/server/commit/18215dd)\
  2015-04-25 17:22:46 +0200
  * [MDEV-7859](https://jira.mariadb.org/browse/MDEV-7859) SSL hostname verification fails for long subject names
* [Revision #9fd65db](https://github.com/MariaDB/server/commit/9fd65db)\
  2015-04-25 00:19:20 +0200
  * [MDEV-7585](https://jira.mariadb.org/browse/MDEV-7585) Assertion \`thd->is\_error() || kill\_errno || thd->killed == ABORT\_QUERY' failed in ha\_rows filesort
* [Revision #8e78160](https://github.com/MariaDB/server/commit/8e78160)\
  2015-04-24 21:41:00 +0200
  * [MDEV-6870](https://jira.mariadb.org/browse/MDEV-6870) Not possible to use FIFO file as a general\_log file
* [Revision #c05d431](https://github.com/MariaDB/server/commit/c05d431)\
  2015-04-24 21:03:43 +0200
  * bug: crash when sync() or close() of a log file fails on shutdown
* [Revision #8f499c3](https://github.com/MariaDB/server/commit/8f499c3)\
  2015-04-24 21:02:37 +0200
  * bug: debug assert crash when seek on log file fails
* [Revision #5fd0088](https://github.com/MariaDB/server/commit/5fd0088)\
  2015-04-27 15:31:12 +0200
  * [MDEV-8058](https://jira.mariadb.org/browse/MDEV-8058): funcs\_1.innodb\_views and funcs\_1.memory\_views fail
* [Revision #574227c](https://github.com/MariaDB/server/commit/574227c)\
  2015-04-27 21:15:23 +1000
  * /run/shm is the general replacement for /dev/shm in newer distros
* [Revision #f832021](https://github.com/MariaDB/server/commit/f832021)\
  2015-04-23 08:26:57 +0200
  * [MDEV-7126](https://jira.mariadb.org/browse/MDEV-7126) replication slave - deadlock in terminate\_slave\_thread with stop slave and show variables of replication filters and show global status
* [Revision #2d6c0a5](https://github.com/MariaDB/server/commit/2d6c0a5)\
  2015-04-24 13:44:22 +0200
  * Merge pull request #39 from openquery/[MDEV-7977](https://jira.mariadb.org/browse/MDEV-7977)-mutex-unlock\_LOCK\_log-in-MYSQL\_BIN\_LOG\_write\_incident
* [Revision #44d1e85](https://github.com/MariaDB/server/commit/44d1e85)\
  2015-04-24 11:00:34 +0400
  * [MDEV-7649](https://jira.mariadb.org/browse/MDEV-7649) wrong result when comparing utf8 column with an invalid literal
* [Revision #f9b2704](https://github.com/MariaDB/server/commit/f9b2704)\
  2015-04-23 23:06:14 +0300
  * Testcase for: [MDEV-7893](https://jira.mariadb.org/browse/MDEV-7893) table\_elimination works wrong ...
* [Revision #2010971](https://github.com/MariaDB/server/commit/2010971)\
  2015-04-14 23:18:54 +0200
  * [MDEV-6892](https://jira.mariadb.org/browse/MDEV-6892): WHERE does not apply
* [Revision #581b49d](https://github.com/MariaDB/server/commit/581b49d)\
  2015-04-22 18:13:30 -0400
  * [MDEV-7995](https://jira.mariadb.org/browse/MDEV-7995) : DMLs not getting replicated with log-bin=OFF & binlog-format != ROW
* [Revision #8cbaafd](https://github.com/MariaDB/server/commit/8cbaafd)\
  2015-04-22 10:14:11 +0200
  * [MDEV-8018](https://jira.mariadb.org/browse/MDEV-8018): main.multi\_update fails with --ps-protocol
* [Revision #e428c80](https://github.com/MariaDB/server/commit/e428c80)\
  2015-04-21 15:41:01 +0300
  * [MDEV-7911](https://jira.mariadb.org/browse/MDEV-7911): crash in Item\_cond::eval\_not\_null\_tables
* [Revision #f1f8adf](https://github.com/MariaDB/server/commit/f1f8adf)\
  2015-04-20 05:02:10 +0200
  * tokuftdump: Install to ${INSTALL\_BINDIR} instead of bin
* [Revision #4cfb7f9](https://github.com/MariaDB/server/commit/4cfb7f9)\
  2015-04-19 15:49:35 +0300
  * Increase the version number
* [Revision #1115a59](https://github.com/MariaDB/server/commit/1115a59)\
  2015-04-15 19:14:20 +0300
  * Merge pull request #41 from MariaDB/5.5-[MDEV-7820](https://jira.mariadb.org/browse/MDEV-7820)
* [Revision #eb47b22](https://github.com/MariaDB/server/commit/eb47b22)\
  2015-04-15 16:23:43 +0300
  * [MDEV-7820](https://jira.mariadb.org/browse/MDEV-7820) Server crashes in my\_strcasecmp\_utf8 on subquery in ORDER BY clause of GROUP\_CONCAT
* [Revision #59d847b](https://github.com/MariaDB/server/commit/59d847b)\
  2015-04-15 12:08:37 +0400
  * [MDEV-7814](https://jira.mariadb.org/browse/MDEV-7814) Assertion \`args\[0]->fixed' fails in Item\_func\_conv\_charset::Item\_func\_conv\_charset Removing a wrong assertion.
* [Revision #b9a7586](https://github.com/MariaDB/server/commit/b9a7586)\
  2015-03-05 16:34:13 +0100
  * [MDEV-7613](https://jira.mariadb.org/browse/MDEV-7613): [MariaDB 5.5.40](../../release-notes-mariadb-5-5-series/mariadb-5540-release-notes.md) server crash on update table left join with a view
* [Revision #83ce352](https://github.com/MariaDB/server/commit/83ce352)\
  2015-04-14 13:26:55 +1000
  * quote table name in mysql\_check:is\_view. increment version too
* [Revision #4987080](https://github.com/MariaDB/server/commit/4987080)\
  2015-04-14 13:26:22 +1000
  * Don't run upgrade-views if not mysql or --upgrade-system-tables
* [Revision #97e0aea](https://github.com/MariaDB/server/commit/97e0aea)\
  2015-04-14 12:43:50 +1000
  * mysqlcheck fix-view-algorithm -> upgrade-views
* [Revision #808608c](https://github.com/MariaDB/server/commit/808608c)\
  2015-04-14 11:26:13 +1000
  * corrected mysql\_upgrade to always list output for every phase
* [Revision #c584058](https://github.com/MariaDB/server/commit/c584058)\
  2015-04-14 11:01:31 +1000
  * Update tests for mysql\_upgrade\_view
* [Revision #76c18f7](https://github.com/MariaDB/server/commit/76c18f7)\
  2015-04-13 23:25:23 +1000
  * sql\_print\_information corrected
* [Revision #622891c](https://github.com/MariaDB/server/commit/622891c)\
  2015-04-13 22:58:45 +1000
  * mariadb\_fix\_view to allow fixing of view->mariadb\_version
* [Revision #8a827d5](https://github.com/MariaDB/server/commit/8a827d5)\
  2015-04-13 22:39:37 +1000
  * avoid calling runctiosn in DBUG\_RETURN
* [Revision #29721d7](https://github.com/MariaDB/server/commit/29721d7)\
  2015-04-13 22:31:44 +1000
  * mariadb\_fix\_view need only check view->mariadb\_version
* [Revision #7229b19](https://github.com/MariaDB/server/commit/7229b19)\
  2015-04-13 22:28:12 +1000
  * remove include sql\_view.h from sql\_table.cc - unneeded
* [Revision #fc277cd](https://github.com/MariaDB/server/commit/fc277cd)\
  2015-04-13 22:17:57 +1000
  * Add --fix-tables option to mysql-check
* [Revision #28b1731](https://github.com/MariaDB/server/commit/28b1731)\
  2015-04-13 21:12:23 +1000
  * Allow REPAIR NO\_WRITE\_TO\_BINLOG as per serg's review
* [Revision #f91dafc](https://github.com/MariaDB/server/commit/f91dafc)\
  2015-04-13 20:52:19 +1000
  * correct phase numbering in test results
* [Revision #eaa3da8](https://github.com/MariaDB/server/commit/eaa3da8)\
  2015-04-13 20:41:49 +1000
  * Add mysql-test/std\_data/mysql\_upgrade/\* for [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916)
* [Revision #4409e04](https://github.com/MariaDB/server/commit/4409e04)\
  2015-04-12 21:40:07 +1000
  * correct server side error messages
* [Revision #9b067a3](https://github.com/MariaDB/server/commit/9b067a3)\
  2015-04-12 21:05:01 +1000
  * Corrections to mysqlcheck
* [Revision #96e277a](https://github.com/MariaDB/server/commit/96e277a)\
  2015-04-12 20:42:13 +1000
  * mysql\_upgrade to pass binlog option to mysqlcheck
* [Revision #c8dbef2](https://github.com/MariaDB/server/commit/c8dbef2)\
  2015-04-12 20:41:28 +1000
  * [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916) REPAIR VIEW / mysql migration
* [Revision #e5191dd](https://github.com/MariaDB/server/commit/e5191dd)\
  2015-04-12 17:26:50 +1000
  * mysql-upgrade -> fix-view-algorithm as mysqlcheck option
* [Revision #25872e2](https://github.com/MariaDB/server/commit/25872e2)\
  2015-04-12 17:21:02 +1000
  * Correct phase count on mysql\_upgrade
* [Revision #ebd3c6c](https://github.com/MariaDB/server/commit/ebd3c6c)\
  2015-04-12 17:05:02 +1000
  * Remove mysql-upgrade / skip-mysql-upgrade options from mysql-upgrade.c
* [Revision #87f5bae](https://github.com/MariaDB/server/commit/87f5bae)\
  2015-04-12 16:50:16 +1000
  * Get my\_getop to parse opt\_mysql\_upgrade in mysqlcheck
* [Revision #70960e7](https://github.com/MariaDB/server/commit/70960e7)\
  2015-04-12 15:56:21 +1000
  * [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916): Upgrade from MySQL to MariaDB breaks already created views
* [Revision #85660d7](https://github.com/MariaDB/server/commit/85660d7)\
  2015-04-11 18:13:08 +1000
  * [MDEV-7977](https://jira.mariadb.org/browse/MDEV-7977) MYSQL\_BIN\_LOG::write\_incident failing to release LOCK\_log
* [Revision #cc84ac3](https://github.com/MariaDB/server/commit/cc84ac3)\
  2015-03-31 13:10:43 +0500
  * [MDEV-7596](https://jira.mariadb.org/browse/MDEV-7596) audit plugin - record full query / document line length / make buffer configurable.
    * The serve\_audit\_query\_log\_limit variable implemented.
    * Also QUERY\_DCL filter added.
* [Revision #995f622](https://github.com/MariaDB/server/commit/995f622)\
  2015-03-30 00:49:16 +0300
  * [MDEV-7858](https://jira.mariadb.org/browse/MDEV-7858): main.subselect\_sj2\_jcl6 fails in buildbot
* [Revision #d7445ea](https://github.com/MariaDB/server/commit/d7445ea)\
  2015-03-27 20:35:37 -0400
  * [MDEV-7194](https://jira.mariadb.org/browse/MDEV-7194): galera fails to replicate DDL queries when using binlog\_checksum
* [Revision #6a20454](https://github.com/MariaDB/server/commit/6a20454)\
  2015-03-24 16:41:04 -0400
  * [MDEV-7798](https://jira.mariadb.org/browse/MDEV-7798): mysql.server init script can't stop mysqld when WSREP is turned off
* [Revision #86f46a3d](https://github.com/MariaDB/server/commit/86f46a3d)\
  2015-03-23 09:49:32 +0200
  * [MDEV-7301](https://jira.mariadb.org/browse/MDEV-7301): Unknown column quoted with backticks in HAVING clause when using function.
* [Revision #9253064](https://github.com/MariaDB/server/commit/9253064)\
  2015-03-10 12:34:17 +0200
  * [MDEV-7682](https://jira.mariadb.org/browse/MDEV-7682) Incorrect use of SPATIAL KEY for query plan
* [Revision #5e20df2](https://github.com/MariaDB/server/commit/5e20df2)\
  2015-03-19 19:46:08 +0400
  * [MDEV-7641](https://jira.mariadb.org/browse/MDEV-7641) Server crash on set global server\_audit\_incl\_users=null.
* [Revision #c020d36](https://github.com/MariaDB/server/commit/c020d36)\
  2015-03-17 13:26:33 +0300
  * [MDEV-7474](https://jira.mariadb.org/browse/MDEV-7474): Semi-Join's DuplicateWeedout strategy skipped ...
* [Revision #5a3bf84](https://github.com/MariaDB/server/commit/5a3bf84)\
  2015-03-12 18:53:31 +0200
  * [MDEV-7692](https://jira.mariadb.org/browse/MDEV-7692) MariaDB - mysql-test - SUITE:percona - percona.innodb\_sys\_index 'xtradb' fails - @@version\_comment
* [Revision #7a6cad5](https://github.com/MariaDB/server/commit/7a6cad5)\
  2015-03-11 12:36:00 -0400
  * Backport fix for [MDEV-7673](https://jira.mariadb.org/browse/MDEV-7673), [MDEV-7203](https://jira.mariadb.org/browse/MDEV-7203) and [MDEV-7192](https://jira.mariadb.org/browse/MDEV-7192) from 10.0-galera
* [Revision #07ff90e](https://github.com/MariaDB/server/commit/07ff90e)\
  2015-03-09 22:55:54 -0400
  * Reduce gcache size to cut down disk usage
* [Revision #34f37aa](https://github.com/MariaDB/server/commit/34f37aa)\
  2015-03-02 19:18:10 +0200
  * [MDEV-7643](https://jira.mariadb.org/browse/MDEV-7643) MTR creates nested links when tests are run with --mem
* [Revision #17a3779](https://github.com/MariaDB/server/commit/17a3779)\
  2015-03-06 18:13:06 +0100
  * after innodb/xtradb merge: use the correct visibility for internal functions
* [Revision #d7d1907](https://github.com/MariaDB/server/commit/d7d1907)\
  2015-03-06 17:03:46 +0100
  * [MDEV-6838](https://jira.mariadb.org/browse/MDEV-6838) Using too big key for internal temp tables
* [Revision #12d87c3](https://github.com/MariaDB/server/commit/12d87c3)\
  2015-03-06 11:15:55 +0100
  * [MDEV-7659](https://jira.mariadb.org/browse/MDEV-7659) buildbot may leave stale mysqld
* [Revision #206b111](https://github.com/MariaDB/server/commit/206b111)\
  2015-03-06 11:19:23 +0200
  * [MDEV-7672](https://jira.mariadb.org/browse/MDEV-7672): Crash creating an InnoDB table with foreign keys
* [Revision #f66fbe8](https://github.com/MariaDB/server/commit/f66fbe8)\
  2015-03-05 12:05:59 +0200
  * [MDEV-7578](https://jira.mariadb.org/browse/MDEV-7578) :Slave is 10x slower to execute set of statements compared to master when using RBR
* [Revision #45b6edb](https://github.com/MariaDB/server/commit/45b6edb)\
  2015-02-28 23:44:55 +0200
  * [MDEV-6838](https://jira.mariadb.org/browse/MDEV-6838): Using too big key for internal temp tables
* [Revision #fa87fc7](https://github.com/MariaDB/server/commit/fa87fc7)\
  2015-02-27 18:28:40 +0100
  * update tokudb version after merge
* [Revision #b5d6aa5](https://github.com/MariaDB/server/commit/b5d6aa5)\
  2015-02-23 13:27:51 +0100
  * [MDEV-7310](https://jira.mariadb.org/browse/MDEV-7310): last\_commit\_pos\_offset set to wrong value after binlog rotate in group commit

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
