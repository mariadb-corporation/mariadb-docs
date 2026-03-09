# MariaDB 10.0.30 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.30)[Release Notes](../../old-releases/10.0/10.0.30.md)[Changelog](mariadb-10030-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 8 Mar 2017

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.30.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #c4f3e64c23](https://github.com/MariaDB/server/commit/c4f3e64c23) 2017-03-06 21:50:42 +0200 - Merge branch 'bb-10.0-vicentiu' into 10.0
* [Revision #dc1c9e69d0](https://github.com/MariaDB/server/commit/dc1c9e69d0)\
  2017-03-06 19:25:22 +0200
  * Make tokudb report ENOENT when renaming table to nonexistant DB
* [Revision #3da916246f](https://github.com/MariaDB/server/commit/3da916246f)\
  2017-03-06 19:17:15 +0200
  * Revert "Add extra HA\_ERR message that Percona introduced within TokuDB 5.6.35-80"
* [Revision #9741017b1f](https://github.com/MariaDB/server/commit/9741017b1f)\
  2017-03-05 15:17:23 +0200
  * Disable 2 tokudb tests
* [Revision #7bf914e157](https://github.com/MariaDB/server/commit/7bf914e157)\
  2017-03-05 14:50:03 +0200
  * rpl\_extra\_col\_slave\_tokudb changes result set
* [Revision #97041acf7f](https://github.com/MariaDB/server/commit/97041acf7f)\
  2017-03-05 14:32:30 +0200
  * Fix tokudb.gap\_lock\_error test
* [Revision #4c3b732d9f](https://github.com/MariaDB/server/commit/4c3b732d9f)\
  2017-03-05 12:26:32 +0200
  * Updated list of unstable tests for 10.0.30 release
* [Revision #1cac281ebe](https://github.com/MariaDB/server/commit/1cac281ebe) 2017-03-05 02:44:39 +0200 - Merge branch 'merge-pcre' into 10.0
* [Revision #dfd7749120](https://github.com/MariaDB/server/commit/dfd7749120)\
  2017-03-05 02:27:59 +0200
  * 8.40
* [Revision #895b253963](https://github.com/MariaDB/server/commit/895b253963) 2017-03-05 02:22:40 +0200 - Merge remote-tracking branch 'connect/10.0' into 10.0
* [Revision #b2956b2ab4](https://github.com/MariaDB/server/commit/b2956b2ab4)\
  2017-03-02 12:12:53 +0100
  * Update version number and date modified: storage/connect/ha\_connect.cc
* [Revision #d75e5e6e26](https://github.com/MariaDB/server/commit/d75e5e6e26)\
  2017-02-24 23:21:20 +0100
  * Fix crashing when joining two JDBC tables.. Was in close (the virtual machine could have been detached. modified: storage/connect/jdbconn.cpp
* [Revision #6f34d8807c](https://github.com/MariaDB/server/commit/6f34d8807c)\
  2017-02-16 18:01:48 +0100
  * All changes made on 10.1
* [Revision #82913b0e90](https://github.com/MariaDB/server/commit/82913b0e90)\
  2017-01-17 19:39:49 +0100
  * Commit changes made for version 10.1
* [Revision #fa59ac5055](https://github.com/MariaDB/server/commit/fa59ac5055)\
  2017-03-05 02:01:49 +0200
  * Add extra HA\_ERR message that Percona introduced within TokuDB 5.6.35-80
* [Revision #b7a3bce06e](https://github.com/MariaDB/server/commit/b7a3bce06e) 2017-03-05 02:01:21 +0200 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #d71df7e1db](https://github.com/MariaDB/server/commit/d71df7e1db)\
  2017-03-05 01:31:32 +0200
  * 5.6.35-80.0
* [Revision #5139c4b688](https://github.com/MariaDB/server/commit/5139c4b688)\
  2017-03-05 01:06:01 +0200
  * Update xtradb version to match the merged one
* [Revision #5d0c123007](https://github.com/MariaDB/server/commit/5d0c123007)\
  2017-03-05 01:00:21 +0200
  * Add missing sys\_var test for innodb\_stats\_include\_delete\_marked
* [Revision #83da1a1e57](https://github.com/MariaDB/server/commit/83da1a1e57) 2017-03-05 00:59:57 +0200 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #8d69ce7b82](https://github.com/MariaDB/server/commit/8d69ce7b82)\
  2017-03-04 20:49:14 +0200
  * 5.6.35-80.0
* [Revision #f4806772d3](https://github.com/MariaDB/server/commit/f4806772d3)\
  2017-03-03 20:16:16 +0200
  * Add missing DBUG\_RETURN
* [Revision #606a4a4847](https://github.com/MariaDB/server/commit/606a4a4847)\
  2017-03-03 20:12:48 +0200
  * Post [MDEV-11902](https://jira.mariadb.org/browse/MDEV-11902) Fix test failures in maria and myisam storage engines
* [Revision #1acfa942ed](https://github.com/MariaDB/server/commit/1acfa942ed) 2017-03-03 01:37:54 +0200 - Merge branch '5.5' into 10.0
* [Revision #5a0fff50f8](https://github.com/MariaDB/server/commit/5a0fff50f8)\
  2017-02-26 15:40:18 -0800
  * Fixed bug [MDEV-12099](https://jira.mariadb.org/browse/MDEV-12099).
* [Revision #199f88cb9c](https://github.com/MariaDB/server/commit/199f88cb9c)\
  2017-02-23 12:48:15 +0100
  * [MDEV-5999](https://jira.mariadb.org/browse/MDEV-5999) MySQL Bug#12766319 - 61865: RENAME USER DOES NOT WORK CORRECTLY - REQUIRES FLUSH PRIVILEGES
* [Revision #494a94158a](https://github.com/MariaDB/server/commit/494a94158a)\
  2017-02-23 12:41:13 +0100
  * Fix for bug#11759114 - '51401: GRANT TREATS NONEXISTENT FUNCTIONS/PRIVILEGES DIFFERENTLY'.
* [Revision #0a480f03c6](https://github.com/MariaDB/server/commit/0a480f03c6)\
  2017-02-23 10:37:02 +0100
  * delete the installation warning for CentOS4/RHEL4
* [Revision #2c354e7468](https://github.com/MariaDB/server/commit/2c354e7468)\
  2017-02-23 10:34:51 +0100
  * [MDEV-11789](https://jira.mariadb.org/browse/MDEV-11789) MariaDB fails to restart after 10.0.29-1.el7 update
* [Revision #713d513624](https://github.com/MariaDB/server/commit/713d513624)\
  2017-02-23 10:32:34 +0100
  * [MDEV-12074](https://jira.mariadb.org/browse/MDEV-12074) selinux build failure on Fedora 24
* [Revision #831b531895](https://github.com/MariaDB/server/commit/831b531895)\
  2017-02-22 15:22:22 +0100
  * [MDEV-10788](https://jira.mariadb.org/browse/MDEV-10788) Not able to compile source with -DBUILD\_CONFIG=mysql\_release -DCMAKE\_BUILD\_TYPE=Debug
* [Revision #44534487d4](https://github.com/MariaDB/server/commit/44534487d4)\
  2017-02-21 11:07:42 +0100
  * [MDEV-11505](https://jira.mariadb.org/browse/MDEV-11505) wrong databasename in mysqldump comment
* [Revision #d72dbb4122](https://github.com/MariaDB/server/commit/d72dbb4122)\
  2017-02-20 22:40:47 +0100
  * bugfix: remove my\_delete\_with\_symlink()
* [Revision #955f2f036d](https://github.com/MariaDB/server/commit/955f2f036d)\
  2017-02-20 19:53:12 +0100
  * race-condition safe implementation of test\_if\_data\_home\_dir()
* [Revision #93cb0246b8](https://github.com/MariaDB/server/commit/93cb0246b8)\
  2017-02-20 11:07:38 +0100
  * race-condition safe implementation of mi\_delete\_table/maria\_delete\_table
* [Revision #6d50324558](https://github.com/MariaDB/server/commit/6d50324558)\
  2017-02-20 22:41:17 +0100
  * support MY\_NOSYMLINKS in my\_delete()
* [Revision #f2d24ea68b](https://github.com/MariaDB/server/commit/f2d24ea68b)\
  2017-02-20 13:39:54 +0100
  * compilation failure
* [Revision #b6862c914f](https://github.com/MariaDB/server/commit/b6862c914f)\
  2017-02-18 15:18:35 +0100
  * cleanup: remove now-unused argument
* [Revision #b27fd90ad3](https://github.com/MariaDB/server/commit/b27fd90ad3)\
  2017-02-15 18:45:19 +0100
  * [MDEV-11902](https://jira.mariadb.org/browse/MDEV-11902) mi\_open race condition
* [Revision #d78d0d459d](https://github.com/MariaDB/server/commit/d78d0d459d)\
  2017-02-18 10:38:14 +0100
  * cleanup: NO\_OPEN\_3 was never defined
* [Revision #8722d4b8d2](https://github.com/MariaDB/server/commit/8722d4b8d2)\
  2017-02-18 10:20:15 +0100
  * cleanup: remove 16-year-old "TODO"
* [Revision #c826ac9d53](https://github.com/MariaDB/server/commit/c826ac9d53)\
  2017-02-18 10:10:34 +0100
  * cleanup: mysys\_test\_invalid\_symlink
* [Revision #24d8bc707a](https://github.com/MariaDB/server/commit/24d8bc707a)\
  2017-02-18 10:08:49 +0100
  * cleanup: my\_register\_filename()
* [Revision #3cba74e032](https://github.com/MariaDB/server/commit/3cba74e032)\
  2017-02-18 10:01:31 +0100
  * cleanup: fn\_format, remove dead code
* [Revision #924a81a548](https://github.com/MariaDB/server/commit/924a81a548)\
  2017-02-18 15:06:25 +0100
  * bugfix: DEBUG\_SYNC() invoked with no THD
* [Revision #8897b50dca](https://github.com/MariaDB/server/commit/8897b50dca)\
  2017-02-16 13:24:00 +0100
  * [MDEV-11525](https://jira.mariadb.org/browse/MDEV-11525) Assertion \`cp + len <= buff + buff\_size' failed in JOIN\_CACHE::write\_record\_data
* [Revision #eef2101489](https://github.com/MariaDB/server/commit/eef2101489)\
  2017-02-16 11:32:47 +0100
  * [MDEV-11933](https://jira.mariadb.org/browse/MDEV-11933) Wrong usage of linked list in mysql\_prune\_stmt\_list
* [Revision #ac78927aef](https://github.com/MariaDB/server/commit/ac78927aef)\
  2017-02-24 00:10:08 -0800
  * Fixed bug [MDEV-7992](https://jira.mariadb.org/browse/MDEV-7992).
* [Revision #bdb672fe96](https://github.com/MariaDB/server/commit/bdb672fe96)\
  2017-02-23 19:46:10 +0200
  * [MDEV-12120](https://jira.mariadb.org/browse/MDEV-12120) tokudb\_bugs.xa-N tests fail with timeout on valgrind
* [Revision #365c4e971a](https://github.com/MariaDB/server/commit/365c4e971a)\
  2017-02-22 10:03:33 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520)/[MDEV-5746](https://jira.mariadb.org/browse/MDEV-5746) post-fix: Do not posix\_fallocate() too much.
* [Revision #6de50b2c7f](https://github.com/MariaDB/server/commit/6de50b2c7f)\
  2017-02-22 09:17:30 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) post-fixes
* [Revision #32591b750f](https://github.com/MariaDB/server/commit/32591b750f)\
  2017-02-22 11:40:01 +0530
  * [MDEV-11718](https://jira.mariadb.org/browse/MDEV-11718) 5.5 rpl and federated tests massively fail in buildbot with valgrind
* [Revision #cf673adee2](https://github.com/MariaDB/server/commit/cf673adee2)\
  2017-02-22 01:36:16 +0400
  * [MDEV-10418](https://jira.mariadb.org/browse/MDEV-10418) Assertion \`m\_extra\_cache' failed in ha\_partition::late\_extra\_cache(uint).
* [Revision #978179a9d4](https://github.com/MariaDB/server/commit/978179a9d4)\
  2017-02-20 17:58:42 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) Extending an InnoDB data file unnecessarily allocates a large memory buffer on Windows
* [Revision #2bfe83adec](https://github.com/MariaDB/server/commit/2bfe83adec)\
  2017-02-20 17:16:59 +0200
  * Remove a bogus Valgrind "suppression".
* [Revision #5ddfcb05ca](https://github.com/MariaDB/server/commit/5ddfcb05ca)\
  2017-02-17 13:37:18 +0100
  * [MDEV-9455](https://jira.mariadb.org/browse/MDEV-9455): \[ERROR] mysqld got signal 11
* [Revision #1b7aae90fb](https://github.com/MariaDB/server/commit/1b7aae90fb)\
  2017-02-20 18:22:01 +0400
  * [MDEV-11904](https://jira.mariadb.org/browse/MDEV-11904) Make Audit Plugin working with MySQL 8.0.
* [Revision #6364adb199](https://github.com/MariaDB/server/commit/6364adb199)\
  2017-02-18 20:39:49 +0200
  * [MDEV-10621](https://jira.mariadb.org/browse/MDEV-10621) parts.partition\_float\_myisam failed with timeout in buildbot
* [Revision #f49375fddf](https://github.com/MariaDB/server/commit/f49375fddf)\
  2017-02-16 23:44:54 -0800
  * Fixed bug [MDEV-9028](https://jira.mariadb.org/browse/MDEV-9028).
* [Revision #b70cd26d73](https://github.com/MariaDB/server/commit/b70cd26d73)\
  2017-02-17 00:57:24 +0200
  * [MDEV-11668](https://jira.mariadb.org/browse/MDEV-11668) rpl.rpl\_heartbeat\_basic fails sporadically in buildbot
* [Revision #29d78dbb44](https://github.com/MariaDB/server/commit/29d78dbb44)\
  2017-02-12 23:19:48 +0600
  * minor typo in a description of mysql\_parse()
* [Revision #108b211ee2](https://github.com/MariaDB/server/commit/108b211ee2)\
  2017-02-16 12:02:31 +0200
  * Fix gcc 6.3.x compiler warnings.
* [Revision #2e8fa1c2b2](https://github.com/MariaDB/server/commit/2e8fa1c2b2)\
  2017-02-13 17:29:32 -0500
  * [MDEV-12058](https://jira.mariadb.org/browse/MDEV-12058): MariaDB Test Suite issue with test sys\_vars.secure\_file\_priv.test
* [Revision #60c932a3d0](https://github.com/MariaDB/server/commit/60c932a3d0)\
  2017-01-27 16:47:00 +0200
  * backported build-tags from 10.2 to ensure that 'make tags' works again with xemacs
* [Revision #5c9baf54e7](https://github.com/MariaDB/server/commit/5c9baf54e7)\
  2017-01-27 16:46:26 +0200
  * Fix for memory leak in applications, like QT,that calls my\_thread\_global\_init() + my\_thrad\_global\_end() repeatadily. This caused THR\_KEY\_mysys to be allocated multiple times.
* [Revision #46eef1ede2](https://github.com/MariaDB/server/commit/46eef1ede2)\
  2017-01-23 19:40:22 -0800
  * Fixed bug [MDEV-11859](https://jira.mariadb.org/browse/MDEV-11859).
* [Revision #f003cc8a35](https://github.com/MariaDB/server/commit/f003cc8a35)\
  2017-01-18 11:42:41 -0800
  * Fixed bug [MDEV-8603](https://jira.mariadb.org/browse/MDEV-8603).
* [Revision #29c776cfd1](https://github.com/MariaDB/server/commit/29c776cfd1)\
  2017-03-03 12:03:33 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520): Retry posix\_fallocate() after EINTR.
* [Revision #d04d835f64](https://github.com/MariaDB/server/commit/d04d835f64)\
  2017-02-28 22:26:53 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): support-files/mysql-log-rotate.sh not binlog either
* [Revision #156cf86def](https://github.com/MariaDB/server/commit/156cf86def)\
  2017-02-28 21:47:44 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): Alter Debian log rotate to not rotate binary/relay logs
* [Revision #0af8b565f2](https://github.com/MariaDB/server/commit/0af8b565f2)\
  2017-02-28 21:39:34 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): mysqladmin flush-X-log options
* [Revision #33c1f20d8e](https://github.com/MariaDB/server/commit/33c1f20d8e)\
  2017-02-28 20:21:19 +1100
  * [MDEV-11610](https://jira.mariadb.org/browse/MDEV-11610): Add --local to mysqladmin
* [Revision #659047b820](https://github.com/MariaDB/server/commit/659047b820)\
  2017-01-23 08:34:59 +1100
  * [MDEV-11386](https://jira.mariadb.org/browse/MDEV-11386): Advance Toochain library cache workaround (temporary)
* [Revision #71f53bf72d](https://github.com/MariaDB/server/commit/71f53bf72d)\
  2017-03-02 12:35:31 +0400
  * [MDEV-11221](https://jira.mariadb.org/browse/MDEV-11221) - main.events\_restart failed in bb
* [Revision #c1c5b7a8d2](https://github.com/MariaDB/server/commit/c1c5b7a8d2)\
  2017-03-01 11:41:48 +0400
  * Fixed missing DBUG\_RETURN
* [Revision #e9ad4bdb42](https://github.com/MariaDB/server/commit/e9ad4bdb42)\
  2017-02-28 15:23:44 +0400
  * [MDEV-11221](https://jira.mariadb.org/browse/MDEV-11221) - main.events\_restart failed in bb
* [Revision #cc413ce9a3](https://github.com/MariaDB/server/commit/cc413ce9a3)\
  2017-02-23 20:45:07 +0100
  * [MDEV-11753](https://jira.mariadb.org/browse/MDEV-11753) Link failure on missing -L${LIBLZ4\_LIBRARY\_DIR}
* [Revision #370cf70136](https://github.com/MariaDB/server/commit/370cf70136)\
  2017-02-22 19:50:27 +0100
  * [MDEV-11757](https://jira.mariadb.org/browse/MDEV-11757) KEY\_BLOCK\_SIZE strangeness when UNCOMPRESSing COMPRESSed InnoDB tables
* [Revision #6a12c05347](https://github.com/MariaDB/server/commit/6a12c05347)\
  2017-02-10 22:39:22 +0200
  * Fixed wrong arguments to sql\_print\_error()
* [Revision #84ed5e1d5f](https://github.com/MariaDB/server/commit/84ed5e1d5f)\
  2017-02-10 22:35:04 +0200
  * Fixed hang doing FLUSH TABLES WITH READ LOCK and parallel replication
* [Revision #f3c65ce951](https://github.com/MariaDB/server/commit/f3c65ce951)\
  2017-02-10 20:30:37 +0200
  * Add protection to not access is\_open() without LOCK\_log mutex
* [Revision #b624b41abb](https://github.com/MariaDB/server/commit/b624b41abb)\
  2017-02-10 20:25:01 +0200
  * Don't allow one to kill START SLAVE while the slaves IO\_THREAD or SQL\_THREAD is starting.
* [Revision #d7a9aed43f](https://github.com/MariaDB/server/commit/d7a9aed43f)\
  2017-02-08 02:14:54 +0200
  * Fixed test failing as myisam table was deleted before oqgraph table.
* [Revision #4bad74e139](https://github.com/MariaDB/server/commit/4bad74e139)\
  2017-02-05 02:23:49 +0200
  * Added error checking for all calls to flush\_relay\_log\_info() and stmt\_done()
* [Revision #a2de378c00](https://github.com/MariaDB/server/commit/a2de378c00)\
  2017-01-30 16:13:49 +0200
  * Add protection for reinitialization of mutex in parallel replaction
* [Revision #c5e25c8b40](https://github.com/MariaDB/server/commit/c5e25c8b40)\
  2017-01-29 23:44:24 +0200
  * Added a separate lock for start/stop/reset slave. This solves some possible dead locks when one calls stop slave while slave is starting.
* [Revision #e65f667bb6](https://github.com/MariaDB/server/commit/e65f667bb6)\
  2017-01-29 22:10:56 +0200
  * [MDEV-9573](https://jira.mariadb.org/browse/MDEV-9573) 'Stop slave' hangs on replication slave
* [Revision #d5c54f3990](https://github.com/MariaDB/server/commit/d5c54f3990)\
  2017-01-29 18:18:19 +0200
  * Fixed compiler warnings
* [Revision #ce903428a8](https://github.com/MariaDB/server/commit/ce903428a8)\
  2017-02-23 11:27:52 +0200
  * Update MariaDB Foundation sponsors
* [Revision #d4baeca441](https://github.com/MariaDB/server/commit/d4baeca441)\
  2017-02-28 12:57:33 +0000
  * Windows : Fix server compile errors when compile with /Zc:strictStrings option
* [Revision #fc673a2c12](https://github.com/MariaDB/server/commit/fc673a2c12)\
  2017-02-28 09:54:12 +0200
  * [MDEV-12127](https://jira.mariadb.org/browse/MDEV-12127) InnoDB: Assertion failure loop\_count < 5 in file log0log.cc
* [Revision #b54566d73b](https://github.com/MariaDB/server/commit/b54566d73b)\
  2017-02-28 10:08:12 +1100
  * [MDEV-11619](https://jira.mariadb.org/browse/MDEV-11619): mtr --mem {no argument of a directory} (#320)
* [Revision #e5b877ce27](https://github.com/MariaDB/server/commit/e5b877ce27)\
  2017-02-23 21:50:55 +0100
  * [MDEV-11935](https://jira.mariadb.org/browse/MDEV-11935): Queries in stored procedures with and EXISTS(SELECT \* FROM VIEW) crashes and closes hte conneciton.
* [Revision #fdeeab01c0](https://github.com/MariaDB/server/commit/fdeeab01c0)\
  2017-02-26 23:01:23 +0400
  * [MDEV-6390](https://jira.mariadb.org/browse/MDEV-6390) CONVERT TO CHARACTER SET utf8 doesn't change DEFAULT CHARSET.
* [Revision #ae142c21a5](https://github.com/MariaDB/server/commit/ae142c21a5)\
  2017-02-23 14:24:34 +0200
  * [MDEV-12106](https://jira.mariadb.org/browse/MDEV-12106) Valgrind tests fail all over in buildbot on 10.0
* [Revision #a0ce92ddc7](https://github.com/MariaDB/server/commit/a0ce92ddc7)\
  2017-02-22 12:32:17 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) post-fix
* [Revision #81695ab8b5](https://github.com/MariaDB/server/commit/81695ab8b5)\
  2017-02-21 16:52:41 +0200
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) Extending an InnoDB data file unnecessarily allocates a large memory buffer on Windows
* [Revision #6dc00f97b7](https://github.com/MariaDB/server/commit/6dc00f97b7)\
  2017-02-21 15:03:34 +0200
  * [MDEV-11774](https://jira.mariadb.org/browse/MDEV-11774) tokudb.locks-select-update-3 failed in buildbot with lock wait timeout
* [Revision #13493078e9](https://github.com/MariaDB/server/commit/13493078e9)\
  2017-02-16 19:40:03 +0200
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) innodb.innodb\_bug14676111 fails
* [Revision #72994d6442](https://github.com/MariaDB/server/commit/72994d6442)\
  2017-02-17 10:36:50 +0200
  * Revert the [MDEV-4396](https://jira.mariadb.org/browse/MDEV-4396) tweak to innodb.innodb\_bug14676111.
* [Revision #343ba58562](https://github.com/MariaDB/server/commit/343ba58562)\
  2017-02-18 16:33:18 +0200
  * [MDEV-10631](https://jira.mariadb.org/browse/MDEV-10631) rpl.rpl\_mdev6386 failed in buildbot
* [Revision #72a822f2ec](https://github.com/MariaDB/server/commit/72a822f2ec)\
  2017-02-17 20:09:14 +0200
  * [MDEV-11766](https://jira.mariadb.org/browse/MDEV-11766) Tests failed in buildbot with semaphore waiting warnings
* [Revision #5e42c958a5](https://github.com/MariaDB/server/commit/5e42c958a5)\
  2017-02-20 10:43:42 +1100
  * [MDEV-11619](https://jira.mariadb.org/browse/MDEV-11619): mtr --mem and $MTR\_MEM support in sane and consistent manner (10.0) (#289)
* [Revision #01d5d6db4c](https://github.com/MariaDB/server/commit/01d5d6db4c)\
  2017-02-16 11:16:27 +0200
  * Fix GCC 6.3.0 warnings.
* [Revision #6011fb6daa](https://github.com/MariaDB/server/commit/6011fb6daa)\
  2017-02-09 08:47:38 +0200
  * Post-push fix for [MDEV-11947](https://jira.mariadb.org/browse/MDEV-11947) InnoDB purge workers fail to shut down
* [Revision #d831e4c22a](https://github.com/MariaDB/server/commit/d831e4c22a)\
  2017-02-08 15:42:15 +0200
  * [MDEV-12024](https://jira.mariadb.org/browse/MDEV-12024) InnoDB startup fails to wait for recv\_writer\_thread to finish
* [Revision #f162704570](https://github.com/MariaDB/server/commit/f162704570)\
  2017-01-30 17:00:51 +0200
  * Rewrite the innodb.log\_file\_size test with DBUG\_EXECUTE\_IF.
* [Revision #20e8347447](https://github.com/MariaDB/server/commit/20e8347447)\
  2017-02-03 12:25:42 +0200
  * [MDEV-11985](https://jira.mariadb.org/browse/MDEV-11985) Make innodb\_read\_only shutdown more robust
* [Revision #9f0dbb3120](https://github.com/MariaDB/server/commit/9f0dbb3120)\
  2017-02-03 18:17:36 +0200
  * [MDEV-11947](https://jira.mariadb.org/browse/MDEV-11947) InnoDB purge workers fail to shut down
* [Revision #e174d923d9](https://github.com/MariaDB/server/commit/e174d923d9)\
  2017-02-03 19:33:09 +0200
  * innodb.innodb-get-fk: Actually test --innodb-read-only.
* [Revision #1d725c8176](https://github.com/MariaDB/server/commit/1d725c8176)\
  2017-02-01 02:16:01 +0200
  * Flush suppressions table to prevent corruption when server is killed
* [Revision #b3dac63f9b](https://github.com/MariaDB/server/commit/b3dac63f9b)\
  2017-02-01 02:14:37 +0200
  * Produce better diagnostics when backtrace attempt fails
* [Revision #923d7d0ad2](https://github.com/MariaDB/server/commit/923d7d0ad2)\
  2017-01-29 00:50:28 +0200
  * Set sys\_errno upon exec command
* [Revision #c46d140961](https://github.com/MariaDB/server/commit/c46d140961)\
  2017-01-29 21:00:02 +0200
  * [MDEV-11764](https://jira.mariadb.org/browse/MDEV-11764) perfschema.table\_name fails in buildbot
* [Revision #f7e03d4419](https://github.com/MariaDB/server/commit/f7e03d4419)\
  2017-01-30 18:35:26 -0500
  * [MDEV-4774](https://jira.mariadb.org/browse/MDEV-4774): Fix test case
* [Revision #4e82aaab2f](https://github.com/MariaDB/server/commit/4e82aaab2f)\
  2017-01-27 16:03:56 +0200
  * Clean up a few tests that kill the server.
* [Revision #ea9caea87e](https://github.com/MariaDB/server/commit/ea9caea87e)\
  2017-01-27 12:17:03 +0200
  * [MDEV-11814](https://jira.mariadb.org/browse/MDEV-11814) test fix
* [Revision #732672c304](https://github.com/MariaDB/server/commit/732672c304)\
  2016-12-05 15:25:59 +0200
  * [MDEV-11233](https://jira.mariadb.org/browse/MDEV-11233) CREATE FULLTEXT INDEX with a token longer than 127 bytes crashes server
* [Revision #afb461587c](https://github.com/MariaDB/server/commit/afb461587c)\
  2017-01-26 14:05:00 +0200
  * [MDEV-11915](https://jira.mariadb.org/browse/MDEV-11915) Detect InnoDB system tablespace size mismatch early
* [Revision #49fe9bad01](https://github.com/MariaDB/server/commit/49fe9bad01)\
  2017-01-25 15:11:46 +0200
  * [MDEV-11814](https://jira.mariadb.org/browse/MDEV-11814) Refuse innodb\_read\_only startup if crash recovery is needed
* [Revision #8725b35d89](https://github.com/MariaDB/server/commit/8725b35d89)\
  2017-01-24 01:25:50 +0530
  * [MDEV-11108](https://jira.mariadb.org/browse/MDEV-11108): Assertion \`uniq\_tuple\_length\_arg <= table->file->max\_key\_length()' failed in SJ\_TMP\_TABLE::create\_sj\_weedout\_tmp\_table
* [Revision #18ef02b04d](https://github.com/MariaDB/server/commit/18ef02b04d)\
  2017-01-10 10:08:04 +0530
  * [MDEV-4774](https://jira.mariadb.org/browse/MDEV-4774) Strangeness with max\_binlog\_stmt\_cache\_size Settings
* [Revision #fbcdc3437c](https://github.com/MariaDB/server/commit/fbcdc3437c)\
  2017-01-17 22:08:19 +0100
  * connect zip bug fix
* [Revision #6728aae3b3](https://github.com/MariaDB/server/commit/6728aae3b3) 2017-01-17 16:22:25 +0100 - Merge branch '5.5' into 10.0
* [Revision #b948b5f7c6](https://github.com/MariaDB/server/commit/b948b5f7c6)\
  2017-01-14 21:23:00 +0100
  * bugfix: Item\_func\_min\_max stored thd internally
* [Revision #798fcb5416](https://github.com/MariaDB/server/commit/798fcb5416)\
  2017-01-14 20:55:33 +0100
  * bugfix: cmp\_item\_row::alloc\_comparators() allocated on the wrong arena
* [Revision #67e2028161](https://github.com/MariaDB/server/commit/67e2028161)\
  2017-01-14 14:56:01 +0100
  * [MDEV-9690](https://jira.mariadb.org/browse/MDEV-9690) concurrent queries with virtual columns crash in temporal code
* [Revision #e4e801d478](https://github.com/MariaDB/server/commit/e4e801d478)\
  2017-01-17 11:15:21 +0100
  * connect: compilation errors and few obvious bugs
* [Revision #3e589d4b8e](https://github.com/MariaDB/server/commit/3e589d4b8e)\
  2017-01-17 12:24:55 +0100
  * [MDEV-11811](https://jira.mariadb.org/browse/MDEV-11811): dual master with parallel replication memory leak in write master
* [Revision #66744f4540](https://github.com/MariaDB/server/commit/66744f4540) 2017-01-14 19:56:00 +0200 - Merge branch '5.5' into 10.0
* [Revision #20ca1bcf4b](https://github.com/MariaDB/server/commit/20ca1bcf4b)\
  2017-01-12 13:54:21 +0100
  * [MDEV-11527](https://jira.mariadb.org/browse/MDEV-11527) Virtual columns do not get along well with NO\_ZERO\_DATE
* [Revision #0d1d0d77f2](https://github.com/MariaDB/server/commit/0d1d0d77f2)\
  2017-01-11 19:12:21 +0100
  * [MDEV-11706](https://jira.mariadb.org/browse/MDEV-11706) Assertion \`is\_stat\_field || !table || (!table->write\_set || bitmap\_is\_set(table->write\_set, field\_index) || (table->vcol\_set && bitmap\_is\_set(table->vcol\_set, field\_index)))' failed in Field\_time::store\_TIME\_with\_warning
* [Revision #939d1255a7](https://github.com/MariaDB/server/commit/939d1255a7)\
  2017-01-13 10:15:28 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
