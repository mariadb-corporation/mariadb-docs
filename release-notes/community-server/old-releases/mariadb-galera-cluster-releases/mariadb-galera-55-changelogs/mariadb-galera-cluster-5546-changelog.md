# MariaDB Galera Cluster 5.5.46 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.46)[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5546-release-notes.md)[Changelog](mariadb-galera-cluster-5546-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 20 Oct 2015

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5546-release-notes.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #278ff16](https://github.com/MariaDB/server/commit/278ff16)\
  2015-10-15 05:47:06 -0400
  * Add warnings to galera test suppression list.
* [Revision #8d2d947](https://github.com/MariaDB/server/commit/8d2d947)\
  2015-10-13 15:42:53 -0400
  * Fix galera\_var\_dirty\_reads test.
* [Revision #fd68a7d](https://github.com/MariaDB/server/commit/fd68a7d)\
  2015-10-13 14:42:36 -0400
  * Merge tag 'mariadb-5.5.46' into 5.5-galera
* [Revision #16c4b3c](https://github.com/MariaDB/server/commit/16c4b3c)\
  2015-10-09 16:43:59 +0200
  * fixes for buildbot:
* [Revision #f41a41f](https://github.com/MariaDB/server/commit/f41a41f)\
  2015-10-09 00:06:16 +0200
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #db79f4c](https://github.com/MariaDB/server/commit/db79f4c)\
  2015-10-08 23:02:43 +0200
  * 5.5.45-37.4
* [Revision #82e9f6d](https://github.com/MariaDB/server/commit/82e9f6d)\
  2015-10-08 22:54:24 +0200
  * Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #c8d5112](https://github.com/MariaDB/server/commit/c8d5112)\
  2015-10-08 00:32:07 +0200
  * [MDEV-8796](https://jira.mariadb.org/browse/MDEV-8796) Delete with sub query with information\_schema.TABLES deletes too many rows
* [Revision #504802f](https://github.com/MariaDB/server/commit/504802f)\
  2015-08-05 11:57:35 +0200
  * [MDEV-7846](https://jira.mariadb.org/browse/MDEV-7846): postreview fix
* [Revision #54b9981](https://github.com/MariaDB/server/commit/54b9981)\
  2015-04-23 20:08:57 +0200
  * [MDEV-7846](https://jira.mariadb.org/browse/MDEV-7846): Server crashes in Item\_subselect::fix\_fields or fails with Thread stack overrun
* [Revision #0ab93fd](https://github.com/MariaDB/server/commit/0ab93fd)\
  2015-04-23 19:16:57 +0200
  * [MDEV-7445](https://jira.mariadb.org/browse/MDEV-7445):Server crash with Signal 6 [MDEV-7565](https://jira.mariadb.org/browse/MDEV-7565): Server crash with Signal 6 (part 2)
* [Revision #2e3e818](https://github.com/MariaDB/server/commit/2e3e818)\
  2015-04-23 19:11:06 +0200
  * [MDEV-7445](https://jira.mariadb.org/browse/MDEV-7445): Server crash with Signal 6
* [Revision #7ccde2c](https://github.com/MariaDB/server/commit/7ccde2c)\
  2015-04-23 19:04:11 +0200
  * [MDEV-7565](https://jira.mariadb.org/browse/MDEV-7565): Server crash with Signal 6 (part 2)
* [Revision #006acf7](https://github.com/MariaDB/server/commit/006acf7)\
  2015-09-30 10:49:45 +0300
  * Bug #68148: drop index on a foreign key column leads to missing table [MDEV-8845](https://jira.mariadb.org/browse/MDEV-8845): Table disappear after modifying FK
* [Revision #a95711e](https://github.com/MariaDB/server/commit/a95711e)\
  2015-09-29 08:39:54 +0300
  * [MDEV-8855](https://jira.mariadb.org/browse/MDEV-8855): innodb.innodb-fk-warnings fails on Windows
* [Revision #02a38fd](https://github.com/MariaDB/server/commit/02a38fd)\
  2015-09-24 17:25:52 +0200
  * [MDEV-8624](https://jira.mariadb.org/browse/MDEV-8624): MariaDB hangs on query with many logical condition
* [Revision #f804b74](https://github.com/MariaDB/server/commit/f804b74)\
  2015-09-28 03:40:29 +0300
  * [MDEV-8154](https://jira.mariadb.org/browse/MDEV-8154) rpl.show\_status\_stop\_slave\_race-7126 sporadically causes internal check failure
* [Revision #ce7d8c5](https://github.com/MariaDB/server/commit/ce7d8c5)\
  2015-09-27 18:01:47 +0300
  * [MDEV-7330](https://jira.mariadb.org/browse/MDEV-7330) plugins.feedback\_plugin\_send fails sporadically in buildbot
* [Revision #bdcf370](https://github.com/MariaDB/server/commit/bdcf370)\
  2015-09-27 16:00:48 +0300
  * [MDEV-7933](https://jira.mariadb.org/browse/MDEV-7933) plugins.feedback\_plugin\_send depends on being executed after plugins.feedback\_plugin\_load
* [Revision #2563609](https://github.com/MariaDB/server/commit/2563609)\
  2015-09-26 02:51:29 +0300
  * Increased the version number
* [Revision #86ed494](https://github.com/MariaDB/server/commit/86ed494)\
  2015-09-26 02:48:55 +0300
  * [MDEV-8849](https://jira.mariadb.org/browse/MDEV-8849) rpl.rpl\_innodb\_bug30888 sporadically fails in buildbot with testcase timeout
* [Revision #13615c5](https://github.com/MariaDB/server/commit/13615c5)\
  2015-09-25 13:56:02 -0400
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): Sporadic SEGFAULT on startup
* [Revision #dca4ab9](https://github.com/MariaDB/server/commit/dca4ab9)\
  2015-09-24 21:24:28 +0300
  * [MDEV-8841](https://jira.mariadb.org/browse/MDEV-8841) innodb\_zip.innodb-create-options fails in buildbot
* [Revision #5cc149f](https://github.com/MariaDB/server/commit/5cc149f)\
  2015-09-24 10:28:47 +0200
  * The compiler warnings fixed.
* [Revision #d54bc3c](https://github.com/MariaDB/server/commit/d54bc3c)\
  2015-09-21 20:49:31 -0400
  * Cleanup: remove dead code which could also lead to race.
* [Revision #9d5767c](https://github.com/MariaDB/server/commit/9d5767c)\
  2015-09-21 20:47:05 -0400
  * Post-merge fix.
* [Revision #db2e21b](https://github.com/MariaDB/server/commit/db2e21b)\
  2015-09-16 23:20:57 -0400
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208): Sporadic SEGFAULT on startup
* [Revision #fd1b2e4](https://github.com/MariaDB/server/commit/fd1b2e4)\
  2015-09-15 17:07:41 -0400
  * [MDEV-8803](https://jira.mariadb.org/browse/MDEV-8803): Debian jessie 8.2 + [MariaDB 10.1.7](../../10.1/10.1.7.md) + GaleraCluster
* [Revision #653aadc](https://github.com/MariaDB/server/commit/653aadc)\
  2015-09-15 16:27:04 -0400
  * [MDEV-8804](https://jira.mariadb.org/browse/MDEV-8804): bootstrap command missing in debian init script
* [Revision #37ae601](https://github.com/MariaDB/server/commit/37ae601)\
  2015-09-09 18:54:14 -0400
  * Update WSREP\_PATCH\_REVNO
* [Revision #760b0c4](https://github.com/MariaDB/server/commit/760b0c4)\
  2015-08-27 00:41:56 -0700
  * Bump WSREP\_PATCH\_VERSION in cmake/wsrep.cmake to 12
* [Revision #bee94cc](https://github.com/MariaDB/server/commit/bee94cc)\
  2015-07-07 22:34:25 -0700
  * Fixes codership/mysql-wsrep#153 use --defaults-extra-file with mysqldump SST
* [Revision #55dfddf](https://github.com/MariaDB/server/commit/55dfddf)\
  2015-06-09 17:02:26 +0300
  * Fixing donate callback return code
* [Revision #0465e3a](https://github.com/MariaDB/server/commit/0465e3a)\
  2015-06-09 11:36:31 +0300
  * Logging message cleanup
* [Revision #d809fcc](https://github.com/MariaDB/server/commit/d809fcc)\
  2015-06-08 21:06:22 +0300
  * This commit fixes - errno handling in wsp::env::append() method, where error could be returned by mistake - return code of sst\_prepare\_other() when pthread\_create() fails - it was returning positive error code which by convention is treated as success.
* [Revision #1b1410c](https://github.com/MariaDB/server/commit/1b1410c)\
  2015-06-08 12:23:53 +0300
  * Slight cleanup improvement on a previous commit.
* [Revision #62c2539](https://github.com/MariaDB/server/commit/62c2539)\
  2015-06-08 01:46:20 -0700
  * Refs codership/mysql-wsrep#143 . Account for the case where the SST password is empty
* [Revision #a7ea3ec](https://github.com/MariaDB/server/commit/a7ea3ec)\
  2015-06-06 01:38:07 +0300
  * Synced xtrabackup SST fixes from Percona tree (as of PXC 5.6.24-25.11 release). This fixes/adresses the following LP bugs: - LP1380697: wsrep\_sst\_xtrabackup-v2 doesn't stop when mysql is SIGKILLed. (full fix for this (as engineeered by Percona) requires Linux-specific patch that we don't carry, but keep xtrabackup scripts as close as possible) - LP1399134: Log the innobackupex/SST logs in SST to syslog if possible. (fixed) - LP1405668: Race condition between donor and joiner in PXB SST. (fixed) - LP1405985: Fail early if xtrabackup\_checkkpoints is missing. (fixed) - LP1407599: wsrep\_sst\_xtrabackup-v2 script causes innobackupex to print a false positive stack trace into the log. (fixed) - LP1441762: IST Fails with SST script error. (fixed) - LP1451670: Fail when move-back fails in xtrabackup SST. (fixed)
* [Revision #d78110e](https://github.com/MariaDB/server/commit/d78110e)\
  2015-06-06 01:08:41 +0300
  * Refs codership/mysql-wsrep#141: this commit 1. Passes wsrep\_sst\_auth\_value to SST scripts via WSREP\_SST\_OPT\_AUTH envronmental variable, so it never appears on the command line 2. In mysqldump and xtrabackup\* SST scripts which rely on MySQL authentication, instead of passing password on the command line, SST script sets MYSQL\_PWD environment variable, so that password also never appears on the mysqldump/innobackupex command line.
* [Revision #4f4f3a5](https://github.com/MariaDB/server/commit/4f4f3a5)\
  2015-05-02 22:25:39 +0300
  * Fixes codership/mysql-wsrep#118
* [Revision #29ac245](https://github.com/MariaDB/server/commit/29ac245)\
  2015-09-07 13:13:52 +0200
  * [MDEV-8473](https://jira.mariadb.org/browse/MDEV-8473): mysqlbinlog -v does not properly decode DECIMAL values in an RBR log
* [Revision #102a85f](https://github.com/MariaDB/server/commit/102a85f)\
  2015-09-03 18:00:43 +0200
  * [MDEV-8663](https://jira.mariadb.org/browse/MDEV-8663): IF Statement returns multiple values erroneously (or Assertion \`!null\_value' failed in Item::send(Protocol\*, String\*))
* [Revision #472d663](https://github.com/MariaDB/server/commit/472d663)\
  2015-08-22 01:18:02 -0400
  * [MDEV-8149](https://jira.mariadb.org/browse/MDEV-8149): Random mtr test failures during warning check
* [Revision #4ee2886](https://github.com/MariaDB/server/commit/4ee2886)\
  2015-08-20 20:55:52 -0400
  * [MDEV-5146](https://jira.mariadb.org/browse/MDEV-5146) : Bulk loads into partitioned table not working
* [Revision #ccd39b2](https://github.com/MariaDB/server/commit/ccd39b2)\
  2015-08-20 09:55:54 -0400
  * Backport partition tests from 10.0-galera.
* [Revision #98bebad](https://github.com/MariaDB/server/commit/98bebad)\
  2015-08-18 17:03:28 -0400
  * Fix for a typo.

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
