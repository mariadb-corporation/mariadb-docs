# MariaDB 10.5.4 Changelog

The most recent release of [MariaDB 10.5](../../mariadb-10-5-series/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../mariadb-10-5-series/mariadb-10-5-28-release-notes.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download](https://downloads.mariadb.org/mariadb/10.5.4/)[Release Notes](../../mariadb-10-5-series/mariadb-1054-release-notes.md)[Changelog](mariadb-1054-changelog.md)[Overview of 10.5](../../mariadb-10-5-series/what-is-mariadb-105.md)

**Release date:** 24 Jun 2020

For the highlights of this release, see the[release notes](../../mariadb-10-5-series/mariadb-1054-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.13](../changelogs-mariadb-10-4-series/mariadb-10413-changelog.md)
* [Revision #5018b998a7](https://github.com/MariaDB/server/commit/5018b998a7)\
  2020-06-23 17:07:03 +0200
  * return --help option
* [Revision #039cb6f6bf](https://github.com/MariaDB/server/commit/039cb6f6bf)\
  2020-06-23 15:49:25 +0200
  * [MDEV-22981](https://jira.mariadb.org/browse/MDEV-22981): Bad "default-character-set" option in \[client] option group 50-client.cnf on Debian/Ubuntu
* [Revision #8394979aae](https://github.com/MariaDB/server/commit/8394979aae)\
  2020-06-22 12:10:06 +0200
  * update C/C
* [Revision #8ad9ef642a](https://github.com/MariaDB/server/commit/8ad9ef642a)\
  2020-06-21 19:15:42 +0200
  * [MDEV-22972](https://jira.mariadb.org/browse/MDEV-22972) After upgrading server/client to 10.5 clients identified via non-builtin plugins cannot be authenticated
* [Revision #ec2de1d58a](https://github.com/MariaDB/server/commit/ec2de1d58a)\
  2020-06-21 17:20:56 +0200
  * update MCS
* [Revision #63b3f78922](https://github.com/MariaDB/server/commit/63b3f78922)\
  2020-06-21 11:41:59 +0300
  * [MDEV-22970](https://jira.mariadb.org/browse/MDEV-22970): Disable [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139) due to corruption concerns
* [Revision #cdbbc69353](https://github.com/MariaDB/server/commit/cdbbc69353)\
  2020-06-21 00:21:14 +0200
  * [MDEV-22969](https://jira.mariadb.org/browse/MDEV-22969) MariaDB-server package conflicts with previous versions of MariaDB-client
* [Revision #bf2df461a2](https://github.com/MariaDB/server/commit/bf2df461a2)\
  2020-06-21 00:17:00 +0200
  * [MDEV-22967](https://jira.mariadb.org/browse/MDEV-22967) Spider does not load in 10.5 with default settings
* [Revision #4366e8c018](https://github.com/MariaDB/server/commit/4366e8c018)\
  2020-06-21 00:07:06 +0200
  * columnstore: fix python dependencies on sles123
* [Revision #cac79216d8](https://github.com/MariaDB/server/commit/cac79216d8)\
  2020-06-20 00:11:13 +0300
  * List of unstable tests for 10.5.4 release
* [Revision #f6f5222575](https://github.com/MariaDB/server/commit/f6f5222575)\
  2020-06-19 11:19:46 +0200
  * update MCS maturity
* [Revision #aa9a42d639](https://github.com/MariaDB/server/commit/aa9a42d639)\
  2020-06-18 15:32:46 +0000
  * Change the method to run SQL statements installing MCS to fix major update scenario.
* [Revision #1e7a68f84a](https://github.com/MariaDB/server/commit/1e7a68f84a)\
  2020-06-18 06:10:25 +0000
  * Both RPM and DEB now restart MDB uninstalling the plugin.
* [Revision #070413fab3](https://github.com/MariaDB/server/commit/070413fab3)\
  2020-06-17 12:35:14 +0200
  * columnstore: delete .rpmsave, install tests
* [Revision #976d4570cd](https://github.com/MariaDB/server/commit/976d4570cd)\
  2020-06-15 11:27:54 +0000
  * Change installed files list to align with the recent changes in the server. Updated MCS
* [Revision #00bc504b77](https://github.com/MariaDB/server/commit/00bc504b77)\
  2020-06-13 19:39:22 +0000
  * Add an explicit server dependency for RPMs and limit builds to x86\_64 and i386 only.
* [Revision #2e6acebedd](https://github.com/MariaDB/server/commit/2e6acebedd)\
  2020-06-08 06:50:18 +0000
  * [MDEV-22197](https://jira.mariadb.org/browse/MDEV-22197) Change .deb cleanup on uninstall and add extra install files.
* [Revision #71bf5085e4](https://github.com/MariaDB/server/commit/71bf5085e4)\
  2020-06-04 20:09:29 +0200
  * MCS on i386 deb
* [Revision #53a3b2725f](https://github.com/MariaDB/server/commit/53a3b2725f)\
  2020-06-03 19:52:15 +0200
  * RPM: columnstore conflicts with thrift
* [Revision #c2b12c554e](https://github.com/MariaDB/server/commit/c2b12c554e)\
  2020-06-03 09:52:53 +0200
  * build deb packages for columnstore
* [Revision #09e8c77cad](https://github.com/MariaDB/server/commit/09e8c77cad)\
  2020-05-22 17:59:44 +0000
  * Clean up for debian packaging and updates for systemd service units.
* [Revision #a5c273616f](https://github.com/MariaDB/server/commit/a5c273616f)\
  2020-05-19 13:20:03 +0000
  * This patch removes columnstore-libs and columnstore-platform RPMs metadata.
* [Revision #0f88fd84e6](https://github.com/MariaDB/server/commit/0f88fd84e6)\
  2020-05-14 08:46:44 +0000
  * [MCOL-3991](https://jira.mariadb.org/browse/MCOL-3991) MCS is now shiped in a single package.
* [Revision #c141a051bc](https://github.com/MariaDB/server/commit/c141a051bc)\
  2020-05-06 15:21:46 +0000
  * Update columnstore submodule with [MCOL-3982](https://jira.mariadb.org/browse/MCOL-3982) to build libmarias3 w/o autools.
* [Revision #a9bd0bcb25](https://github.com/MariaDB/server/commit/a9bd0bcb25)\
  2020-04-30 13:49:35 +0200
  * let's try to enable MCS
* [Revision #793dcc7368](https://github.com/MariaDB/server/commit/793dcc7368)\
  2019-11-27 14:34:14 +0000
  * Add stub for building ColumnStore
* [Revision #4e16e4fc01](https://github.com/MariaDB/server/commit/4e16e4fc01)\
  2020-06-19 12:59:15 +0200
  * Fix "unresolved external symbol" link errors with MSVC
* [Revision #35034d819c](https://github.com/MariaDB/server/commit/35034d819c)\
  2020-06-18 11:17:43 +0200
  * S3 is pluggable now
* [Revision #4acafaae9b](https://github.com/MariaDB/server/commit/4acafaae9b)\
  2020-06-19 00:28:05 +0200
  * cleanup: Aria headers
* [Revision #e9f62228ab](https://github.com/MariaDB/server/commit/e9f62228ab)\
  2020-06-19 16:25:59 +0200
  * Server maturity increased
* [Revision #e341fb0dae](https://github.com/MariaDB/server/commit/e341fb0dae)\
  2020-06-19 12:30:25 +0300
  * [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871) follow-up fix: AHI corruption & leak
* [Revision #4243785f28](https://github.com/MariaDB/server/commit/4243785f28)\
  2020-06-18 13:21:29 +0200
  * [MDEV-20302](https://jira.mariadb.org/browse/MDEV-20302) Server hangs upon concurrent SELECT from partitioned S3
* [Revision #60f08dd555](https://github.com/MariaDB/server/commit/60f08dd555)\
  2020-06-18 11:57:19 +0300
  * [MDEV-22925](https://jira.mariadb.org/browse/MDEV-22925) ALTER TABLE s3\_table ENGINE=Aria can cause failure on slave
* [Revision #6a0c05b761](https://github.com/MariaDB/server/commit/6a0c05b761)\
  2020-06-18 11:44:28 +0300
  * Fixed bugs in s3 test cases
* [Revision #00bd52b147](https://github.com/MariaDB/server/commit/00bd52b147)\
  2020-06-18 11:49:07 +0300
  * Added THD::binlog\_table\_should\_be\_logged() to simplify some code
* [Revision #1a49c5eb4d](https://github.com/MariaDB/server/commit/1a49c5eb4d)\
  2020-06-18 11:10:53 +0300
  * Cleanup's and more DBUG\_PRINT's
* [Revision #605555fc31](https://github.com/MariaDB/server/commit/605555fc31)\
  2020-06-19 00:09:36 +0200
  * Windows, compiling - use /diagnostics:caret flag, for better diagnostics
* [Revision #98333883ee](https://github.com/MariaDB/server/commit/98333883ee)\
  2020-06-18 23:12:54 +0200
  * [MDEV-22933](https://jira.mariadb.org/browse/MDEV-22933) - remove ---source include/not\_threadpool.inc from tests
* [Revision #b2feb03001](https://github.com/MariaDB/server/commit/b2feb03001)\
  2020-04-26 21:06:04 +1000
  * INSTALL\_UNIX\_ADDRDIR for debian to /run/mysqld/mysqld.sock
* [Revision #5155a300fa](https://github.com/MariaDB/server/commit/5155a300fa)\
  2020-06-18 13:38:30 +0300
  * [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871): Reduce InnoDB buf\_pool.page\_hash contention
* [Revision #cfd3d70ccb](https://github.com/MariaDB/server/commit/cfd3d70ccb)\
  2020-06-18 12:26:28 +0300
  * [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871): Remove pointer indirection for InnoDB hash\_table\_t
* [Revision #bf3c862faa](https://github.com/MariaDB/server/commit/bf3c862faa)\
  2020-06-18 12:17:37 +0300
  * [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871): Clean up btr\_search\_sys
* [Revision #9159b8976f](https://github.com/MariaDB/server/commit/9159b8976f)\
  2020-06-18 11:37:24 +0300
  * [MDEV-22871](https://jira.mariadb.org/browse/MDEV-22871): Clean up hash\_table\_t
* [Revision #08f6513cb2](https://github.com/MariaDB/server/commit/08f6513cb2)\
  2020-06-17 21:29:16 +1000
  * libutils: merge\_archives\_unix
* [Revision #38774f8dcb](https://github.com/MariaDB/server/commit/38774f8dcb)\
  2020-06-17 22:01:57 +1000
  * libutils: merge static libraries only once
* Merge [Revision #c515b1d092](https://github.com/MariaDB/server/commit/c515b1d092) 2020-06-18 13:58:54 +0300 - Merge 10.4 into 10.5
* [Revision #205b0ce6ad](https://github.com/MariaDB/server/commit/205b0ce6ad)\
  2020-06-16 12:02:13 +0300
  * [MDEV-22894](https://jira.mariadb.org/browse/MDEV-22894): mariadb-backup should not read \[mariadb-client] option group from configuration files
* [Revision #0121a9e0bb](https://github.com/MariaDB/server/commit/0121a9e0bb)\
  2020-06-16 11:21:28 +0300
  * [MDEV-18215](https://jira.mariadb.org/browse/MDEV-18215): mariadb-backup does not report unknown command line options
* [Revision #01ed614027](https://github.com/MariaDB/server/commit/01ed614027)\
  2020-06-18 12:13:31 +0300
  * Fix the test mariadb-backup.[MDEV-14447](https://jira.mariadb.org/browse/MDEV-14447)
* [Revision #d33c9ca1b0](https://github.com/MariaDB/server/commit/d33c9ca1b0)\
  2020-06-17 22:03:27 +0530
  * [MDEV-22902](https://jira.mariadb.org/browse/MDEV-22902) Assertion \`!page\_has\_siblings(block->frame)' failed in btr\_pcur\_store\_position
* [Revision #b7324e133f](https://github.com/MariaDB/server/commit/b7324e133f)\
  2020-06-17 19:30:19 +0300
  * Remove redundant code in opt\_range.cc: print\_key\_value()
* [Revision #9c577c2b90](https://github.com/MariaDB/server/commit/9c577c2b90)\
  2020-06-16 21:01:16 +0200
  * [MDEV-22917](https://jira.mariadb.org/browse/MDEV-22917) wolfssl might crash at startup when both SSL and encryption plugin are enabled
* [Revision #a0d598a4d2](https://github.com/MariaDB/server/commit/a0d598a4d2)\
  2020-06-04 18:37:18 +0800
  * [MDEV-22794](https://jira.mariadb.org/browse/MDEV-22794): Avoid potential rollback segment contention with increased scalability through even distribution
* [Revision #592a10d079](https://github.com/MariaDB/server/commit/592a10d079)\
  2020-05-22 22:44:37 +0530
  * [MDEV-22370](https://jira.mariadb.org/browse/MDEV-22370) safe\_mutex: Trying to lock uninitialized mutex at /data/src/10.4-bug/sql/rpl\_parallel.cc, line 470 upon shutdown during FTWRL
* [Revision #0128e13e62](https://github.com/MariaDB/server/commit/0128e13e62)\
  2020-06-15 16:39:41 +0300
  * [MDEV-21759](https://jira.mariadb.org/browse/MDEV-21759) galera.galera\_parallel\_autoinc\_manytrx sporadic failures.
* [Revision #49ac606a75](https://github.com/MariaDB/server/commit/49ac606a75)\
  2020-06-14 22:13:45 +0300
  * Fix include statements in galera\_ipv6\_mariadb-backup\_section and galera\_ipv6\_mariadb-backup MTR tests
* [Revision #9bdf35e90f](https://github.com/MariaDB/server/commit/9bdf35e90f)\
  2020-06-08 11:45:56 +0300
  * [MDEV-18215](https://jira.mariadb.org/browse/MDEV-18215): mariadb-backup does not report unknown command line options [MDEV-21298](https://jira.mariadb.org/browse/MDEV-21298): mariadb-backup doesn't read from the \[mariadbd] and \[mariadbd-X.Y] server option groups from configuration files [MDEV-21301](https://jira.mariadb.org/browse/MDEV-21301): mariadb-backup doesn't read \[mariadb-backup] option group in configuration file
* Merge [Revision #ceaa8b647a](https://github.com/MariaDB/server/commit/ceaa8b647a) 2020-06-14 10:32:09 +0300 - Merge commit 10.3 into 10.4
* Merge [Revision #32b34cb95e](https://github.com/MariaDB/server/commit/32b34cb95e) 2020-06-14 10:30:20 +0300 - Merge 10.2 into 10.3
* [Revision #2cd6afb083](https://github.com/MariaDB/server/commit/2cd6afb083)\
  2020-06-14 10:18:07 +0300
  * [MDEV-22889](https://jira.mariadb.org/browse/MDEV-22889): Disable innodb.innodb\_force\_recovery\_rollback
* [Revision #baff3ba6e3](https://github.com/MariaDB/server/commit/baff3ba6e3)\
  2020-06-17 11:33:14 +0200
  * S3 compilation error on x86
* [Revision #7c0cf20444](https://github.com/MariaDB/server/commit/7c0cf20444)\
  2020-06-14 15:43:30 +0200
  * update libmarias3
* [Revision #7bb32cda05](https://github.com/MariaDB/server/commit/7bb32cda05)\
  2020-06-17 17:40:15 +0200
  * more "removed" mysqld command-line options
* [Revision #083a344760](https://github.com/MariaDB/server/commit/083a344760)\
  2020-06-18 00:57:23 +0200
  * Fix error in cmake, when trying gcc on Windows.
* [Revision #e54723fa34](https://github.com/MariaDB/server/commit/e54723fa34)\
  2020-06-18 00:55:11 +0200
  * When compiling with RelWithDebInfo, always use -fno-omit-frame-pointer
* [Revision #815fc98732](https://github.com/MariaDB/server/commit/815fc98732)\
  2020-06-17 21:03:00 +0530
  * [MDEV-22904](https://jira.mariadb.org/browse/MDEV-22904) Compressed row format table tries to access freed blob
* [Revision #471d7a9762](https://github.com/MariaDB/server/commit/471d7a9762)\
  2020-06-14 22:13:45 +0300
  * Fix include statements in galera\_ipv6\_mariadb-backup\_section and galera\_ipv6\_mariadb-backup MTR tests
* [Revision #beb1918354](https://github.com/MariaDB/server/commit/beb1918354)\
  2020-06-15 16:39:41 +0300
  * [MDEV-21759](https://jira.mariadb.org/browse/MDEV-21759) galera.galera\_parallel\_autoinc\_manytrx sporadic failures.
* [Revision #8655d4a202](https://github.com/MariaDB/server/commit/8655d4a202)\
  2020-06-16 12:12:36 +0300
  * Add global ignore for Sending JOIN failed warning.
* [Revision #bf039b9127](https://github.com/MariaDB/server/commit/bf039b9127)\
  2020-06-17 12:58:33 +0300
  * [MDEV-22125](https://jira.mariadb.org/browse/MDEV-22125) : galera.galera\_drop\_multi MTR failed: InnoDB: MySQL is trying to drop database `fts`.\`\` though there are still open handles
* [Revision #bd62a636a4](https://github.com/MariaDB/server/commit/bd62a636a4)\
  2020-06-14 18:39:39 +0900
  * fix a compiler warning on GCC 9.3.0
* [Revision #d0c69ccab5](https://github.com/MariaDB/server/commit/d0c69ccab5)\
  2020-06-16 19:57:33 +0530
  * [MDEV-22911](https://jira.mariadb.org/browse/MDEV-22911): Fix the valgrind & MSAN instrumentation of [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139)
* [Revision #72fc4f3fef](https://github.com/MariaDB/server/commit/72fc4f3fef)\
  2020-06-15 01:47:45 +0200
  * [MDEV-22841](https://jira.mariadb.org/browse/MDEV-22841) ut\_new\_get\_key\_by\_file is unnecessarily expensive, followup
* [Revision #7803601dcb](https://github.com/MariaDB/server/commit/7803601dcb)\
  2020-06-11 01:39:11 +0300
  * [MDEV-22569](https://jira.mariadb.org/browse/MDEV-22569): Run bin/mariadbd instead of bin/mysqld
* [Revision #e290e5a75d](https://github.com/MariaDB/server/commit/e290e5a75d)\
  2020-06-15 23:21:29 +0400
  * [MDEV-22837](https://jira.mariadb.org/browse/MDEV-22837) JSON\_ARRAYAGG and JSON\_OBJECTAGG treat JSON arguments as text.
* [Revision #6c573a9146](https://github.com/MariaDB/server/commit/6c573a9146)\
  2020-06-15 22:51:21 +0400
  * [MDEV-22844](https://jira.mariadb.org/browse/MDEV-22844) JSON\_ARRAYAGG is limited by group\_concat\_max\_len.
* [Revision #30d41c8102](https://github.com/MariaDB/server/commit/30d41c8102)\
  2020-06-15 19:10:39 +0300
  * [MDEV-22881](https://jira.mariadb.org/browse/MDEV-22881) Unexpected errors, corrupt output, Valgrind / ASAN errors in Item\_ident::print or append\_identifier
* [Revision #359d5f56c3](https://github.com/MariaDB/server/commit/359d5f56c3)\
  2020-06-15 17:07:43 +0300
  * Fix drop\_combinations for embedded
* [Revision #4be4d57d36](https://github.com/MariaDB/server/commit/4be4d57d36)\
  2020-06-15 15:26:16 +0300
  * [MDEV-22887](https://jira.mariadb.org/browse/MDEV-22887) unresolved symbol crc32c\_vpmsum on Ubuntu Xenial
* [Revision #4080e3acef](https://github.com/MariaDB/server/commit/4080e3acef)\
  2020-06-15 12:26:53 +0200
  * fixup of "Make error messages from DROP TABLE and DROP TABLE IF EXISTS consistent" results
* [Revision #517e9334f2](https://github.com/MariaDB/server/commit/517e9334f2)\
  2020-06-15 12:59:53 +0300
  * [MDEV-22891](https://jira.mariadb.org/browse/MDEV-22891): Optimizer trace: const tables are not clearly visible
* [Revision #c9f5cb97af](https://github.com/MariaDB/server/commit/c9f5cb97af)\
  2020-06-12 17:03:15 +0300
  * Added checks for uninitalized memory when writing to IO\_CACHE
* [Revision #e843033d02](https://github.com/MariaDB/server/commit/e843033d02)\
  2020-06-11 13:51:36 +0300
  * Created a workaround for a bug in MSAN for va\_arg(,double)
* [Revision #d7a9cdc627](https://github.com/MariaDB/server/commit/d7a9cdc627)\
  2020-06-10 21:14:13 +0300
  * Fixed hang in Aria page cache with concurrent SELECT
* [Revision #b3179b7e32](https://github.com/MariaDB/server/commit/b3179b7e32)\
  2020-06-10 12:04:01 +0300
  * Cleaned up compile failure if DEBUG\_SYNC is disabled in DEBUG builds
* [Revision #7f941c4ef6](https://github.com/MariaDB/server/commit/7f941c4ef6)\
  2020-06-10 11:56:20 +0300
  * Fixed bug in trans\_check() where on error we gave wrong return value
* [Revision #56045ef94a](https://github.com/MariaDB/server/commit/56045ef94a)\
  2020-06-10 11:55:00 +0300
  * Fix for crash in Aria LOCK TABLES + CREATE TRIGGER
* [Revision #ab7eedc185](https://github.com/MariaDB/server/commit/ab7eedc185)\
  2020-06-08 23:55:13 +0300
  * Fixed typos in aria\_read\_log
* [Revision #654b593149](https://github.com/MariaDB/server/commit/654b593149)\
  2020-06-08 23:51:57 +0300
  * BINLOG with LOCK TABLES and SAVEPOINT could cause a crash in debug bin
* [Revision #6a3b581b90](https://github.com/MariaDB/server/commit/6a3b581b90)\
  2020-06-08 15:13:04 +0300
  * [MDEV-19745](https://jira.mariadb.org/browse/MDEV-19745) BACKUP STAGE BLOCK\_DDL hangs on flush sequence table
* [Revision #08d475c73b](https://github.com/MariaDB/server/commit/08d475c73b)\
  2020-06-08 15:05:57 +0300
  * Fixed core dump in "echo shutdown | mysqld --bootstrap"
* [Revision #1cca83784f](https://github.com/MariaDB/server/commit/1cca83784f)\
  2020-06-05 12:48:33 +0300
  * Updated code comments
* [Revision #d35616aab3](https://github.com/MariaDB/server/commit/d35616aab3)\
  2020-06-05 10:38:34 +0300
  * Fixed crash in failing instant alter table with partitioned table
* [Revision #10b88deb74](https://github.com/MariaDB/server/commit/10b88deb74)\
  2020-06-03 19:40:41 +0300
  * Changes needed for ColumnStore and insert cache
* [Revision #74df3c8024](https://github.com/MariaDB/server/commit/74df3c8024)\
  2020-06-03 18:42:54 +0300
  * Changed some DBUG\_PRINT that used error:
* [Revision #96d7294586](https://github.com/MariaDB/server/commit/96d7294586)\
  2020-06-03 18:41:17 +0300
  * Fixed access of undefined memory for compressed MyISAM and Aria tables
* [Revision #dfb41fddf6](https://github.com/MariaDB/server/commit/dfb41fddf6)\
  2020-06-05 18:55:11 +0300
  * Make error messages from DROP TABLE and DROP TABLE IF EXISTS consistent
* [Revision #346d10a953](https://github.com/MariaDB/server/commit/346d10a953)\
  2020-06-05 12:51:01 +0300
  * Fixed error messages from DROP VIEW to align with DROP TABLE
* [Revision #5bcb1d6532](https://github.com/MariaDB/server/commit/5bcb1d6532)\
  2020-06-01 23:27:14 +0300
  * [MDEV-11412](https://jira.mariadb.org/browse/MDEV-11412) Ensure that table is truly dropped when using DROP TABLE
* [Revision #5579c38991](https://github.com/MariaDB/server/commit/5579c38991)\
  2020-06-14 18:58:55 +0300
  * [MDEV-22884](https://jira.mariadb.org/browse/MDEV-22884): Adjust the test for PLUGIN\_PERFSCHEMA=NO
* [Revision #ad5edf3c15](https://github.com/MariaDB/server/commit/ad5edf3c15)\
  2020-06-14 10:18:07 +0300
  * [MDEV-22889](https://jira.mariadb.org/browse/MDEV-22889): Disable innodb.innodb\_force\_recovery\_rollback
* Merge [Revision #3dbc49f075](https://github.com/MariaDB/server/commit/3dbc49f075) 2020-06-14 10:13:53 +0300 - Merge 10.4 into 10.5
* [Revision #b58586aae9](https://github.com/MariaDB/server/commit/b58586aae9)\
  2020-06-13 12:49:22 +0200
  * [MDEV-21560](https://jira.mariadb.org/browse/MDEV-21560) Assertion \`grant\_table || grant\_table\_role' failed in check\_grant\_all\_columns
* Merge [Revision #805340936a](https://github.com/MariaDB/server/commit/805340936a) 2020-06-13 19:01:28 +0300 - Merge 10.3 into 10.4
* Merge [Revision #d83a443250](https://github.com/MariaDB/server/commit/d83a443250) 2020-06-13 15:11:43 +0300 - Merge 10.2 into 10.3
* [Revision #b68f1d847f](https://github.com/MariaDB/server/commit/b68f1d847f)\
  2020-06-13 14:45:52 +0300
  * [MDEV-21217](https://jira.mariadb.org/browse/MDEV-21217) innodb\_force\_recovery=2 may wrongly abort rollback
* [Revision #2fd2fd77e7](https://github.com/MariaDB/server/commit/2fd2fd77e7)\
  2020-06-12 10:45:54 +0300
  * Fix wrong merge of commit d218d1aa49e848cef2bdbe83bbaf08e474d5209c
* Merge [Revision #8c67ffffe8](https://github.com/MariaDB/server/commit/8c67ffffe8) 2020-06-11 22:35:30 +0300 - Merge branch '10.1' into 10.2
* [Revision #de20091f5c](https://github.com/MariaDB/server/commit/de20091f5c)\
  2020-06-10 20:02:46 +0400
  * [MDEV-22755](https://jira.mariadb.org/browse/MDEV-22755) CREATE USER leads to indirect SIGABRT in stack\_chk\_fail () from fill\_schema\_user\_privileges + \* stack smashing detected \* (on optimized builds)
* [Revision #ae3a7d5e43](https://github.com/MariaDB/server/commit/ae3a7d5e43)\
  2020-06-10 19:29:25 +0300
  * [MDEV-22834](https://jira.mariadb.org/browse/MDEV-22834): Disks plugin - change datatype to bigint
* [Revision #59717bbce4](https://github.com/MariaDB/server/commit/59717bbce4)\
  2019-05-22 14:59:00 +0200
  * [MDEV-5924](https://jira.mariadb.org/browse/MDEV-5924): MariaDB could crash after changing the query\_cache size
* [Revision #61862d711d](https://github.com/MariaDB/server/commit/61862d711d)\
  2020-06-10 09:34:56 +0200
  * Revert "[MDEV-22830](https://jira.mariadb.org/browse/MDEV-22830): SQL\_CALC\_FOUND\_ROWS not working properly for single SELECT for DUAL"
* [Revision #443391236d](https://github.com/MariaDB/server/commit/443391236d)\
  2020-06-09 01:35:39 +0530
  * [MDEV-22830](https://jira.mariadb.org/browse/MDEV-22830): SQL\_CALC\_FOUND\_ROWS not working properly for single SELECT for DUAL
* [Revision #e1045a768b](https://github.com/MariaDB/server/commit/e1045a768b)\
  2020-05-27 13:53:39 +0530
  * [MDEV-22717](https://jira.mariadb.org/browse/MDEV-22717): Conditional jump or move depends on uninitialised value(s) in find\_uniq\_filename(char\*, unsigned long)
* [Revision #4f48856906](https://github.com/MariaDB/server/commit/4f48856906)\
  2020-06-05 00:02:55 +0200
  * Client spelling mistakes
* [Revision #d218d1aa49](https://github.com/MariaDB/server/commit/d218d1aa49)\
  2020-06-05 13:11:33 +0530
  * [MDEV-22728](https://jira.mariadb.org/browse/MDEV-22728): SIGFPE in Unique::get\_cost\_calc\_buff\_size from prepare\_search\_best\_index\_intersect on optimized builds
* [Revision #e835881c47](https://github.com/MariaDB/server/commit/e835881c47)\
  2020-06-11 15:33:16 +0400
  * [MDEV-21619](https://jira.mariadb.org/browse/MDEV-21619) Server crash or assertion failures in my\_datetime\_to\_str
* [Revision #1bcc5cd9b6](https://github.com/MariaDB/server/commit/1bcc5cd9b6)\
  2020-06-10 16:14:14 +0300
  * Remove a stale test
* [Revision #9b9a354da9](https://github.com/MariaDB/server/commit/9b9a354da9)\
  2020-06-10 08:42:31 +0400
  * [MDEV-22849](https://jira.mariadb.org/browse/MDEV-22849) Reuse skip\_trailing\_space() in my\_hash\_sort\_utf8mbX
* [Revision #902742789e](https://github.com/MariaDB/server/commit/902742789e)\
  2020-06-09 21:54:42 +1000
  * innodb: dict\_mem\_table\_add\_col - compile warning fix argument 1 null where non-null expected (#1584)
* [Revision #6c30bc2181](https://github.com/MariaDB/server/commit/6c30bc2181)\
  2020-06-13 09:30:04 +0400
  * [MDEV-22268](https://jira.mariadb.org/browse/MDEV-22268) virtual longlong Item\_func\_div::int\_op(): Assertion \`0' failed in Item\_func\_div::int\_op
* [Revision #81a08c5462](https://github.com/MariaDB/server/commit/81a08c5462)\
  2020-06-08 11:25:30 +0530
  * [MDEV-11563](https://jira.mariadb.org/browse/MDEV-11563): GROUP\_CONCAT(DISTINCT ...) may produce a non-distinct list
* [Revision #f9e53a659c](https://github.com/MariaDB/server/commit/f9e53a659c)\
  2020-06-12 09:55:38 +0400
  * [MDEV-22499](https://jira.mariadb.org/browse/MDEV-22499) Assertion \`(uint) (table\_check\_constraints - share->check\_constraints) == (uint) (share->table\_check\_constraints - share->field\_check\_constraints)' failed in TABLE\_SHARE::init\_from\_binary\_frm\_image
* [Revision #bf2a244406](https://github.com/MariaDB/server/commit/bf2a244406)\
  2020-06-10 13:55:55 +0400
  * [MDEV-22854](https://jira.mariadb.org/browse/MDEV-22854) Garbage returned with SELECT CASE..DEFAULT(timestamp\_field\_with\_now\_as\_default)
* [Revision #86c50a255a](https://github.com/MariaDB/server/commit/86c50a255a)\
  2020-06-08 14:00:19 +0400
  * [MDEV-22734](https://jira.mariadb.org/browse/MDEV-22734) Assertion \`mon > 0 && mon < 13' failed in sec\_since\_epoch
* [Revision #9ed08f3576](https://github.com/MariaDB/server/commit/9ed08f3576)\
  2020-06-13 11:15:55 +0200
  * [MDEV-22884](https://jira.mariadb.org/browse/MDEV-22884) Assertion \`grant\_table || grant\_table\_role' failed on perfschema
* [Revision #574ef38005](https://github.com/MariaDB/server/commit/574ef38005)\
  2020-06-13 11:59:34 +0300
  * [MDEV-22190](https://jira.mariadb.org/browse/MDEV-22190) InnoDB: Apparent corruption of an index page ... to be written
* [Revision #114a843669](https://github.com/MariaDB/server/commit/114a843669)\
  2020-06-12 10:23:46 -0700
  * when printing Item\_in\_optimizer, use precedence of wrapped Item
* [Revision #ab9bd6284c](https://github.com/MariaDB/server/commit/ab9bd6284c)\
  2020-06-09 16:24:18 +0530
  * [MDEV-22840](https://jira.mariadb.org/browse/MDEV-22840): JSON\_ARRAYAGG gives wrong results with NULL values and ORDER by clause
* [Revision #0f6f0daa4d](https://github.com/MariaDB/server/commit/0f6f0daa4d)\
  2020-06-09 13:15:14 +0530
  * [MDEV-22011](https://jira.mariadb.org/browse/MDEV-22011): DISTINCT with JSON\_ARRAYAGG gives wrong results
* [Revision #a006e88cac](https://github.com/MariaDB/server/commit/a006e88cac)\
  2020-03-21 12:23:44 +0530
  * [MDEV-11563](https://jira.mariadb.org/browse/MDEV-11563): GROUP\_CONCAT(DISTINCT ...) may produce a non-distinct list
* [Revision #fd1755e49d](https://github.com/MariaDB/server/commit/fd1755e49d)\
  2020-06-12 21:14:08 +0300
  * [MDEV-15101](https://jira.mariadb.org/browse/MDEV-15101): Stop ANALYZE TABLE from flushing table definition cache
* [Revision #431200090e](https://github.com/MariaDB/server/commit/431200090e)\
  2020-06-12 20:30:01 +0300
  * [MDEV-22867](https://jira.mariadb.org/browse/MDEV-22867) Assertion instant.n\_core\_fields == n\_core\_fields failed
* [Revision #d7d80689b3](https://github.com/MariaDB/server/commit/d7d80689b3)\
  2020-06-12 13:24:23 +0300
  * [MDEV-15101](https://jira.mariadb.org/browse/MDEV-15101): Stop ANALYZE TABLE from flushing table definition cache
* [Revision #d34cc6b3fd](https://github.com/MariaDB/server/commit/d34cc6b3fd)\
  2020-06-12 21:57:12 +0530
  * [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139): Fix the MSAN instrumentation
* [Revision #d2c593c2a6](https://github.com/MariaDB/server/commit/d2c593c2a6)\
  2020-06-12 12:50:31 +0300
  * [MDEV-22877](https://jira.mariadb.org/browse/MDEV-22877) Avoid unnecessary buf\_pool.page\_hash S-latch acquisition
* [Revision #0b5dc6268f](https://github.com/MariaDB/server/commit/0b5dc6268f)\
  2020-06-12 13:21:42 +0200
  * more mysql\_create\_view link/unlink woes
* [Revision #fb70eb773c](https://github.com/MariaDB/server/commit/fb70eb773c)\
  2020-06-12 13:18:41 +0200
  * [MDEV-22878](https://jira.mariadb.org/browse/MDEV-22878) galera.wsrep\_strict\_ddl hangs in 10.5 after merge
* [Revision #efa67ee0ea](https://github.com/MariaDB/server/commit/efa67ee0ea)\
  2020-06-12 14:56:55 +0300
  * [MDEV-21851](https://jira.mariadb.org/browse/MDEV-21851): post-push to fix main.flush\_read\_lock.
* [Revision #82f3ceed12](https://github.com/MariaDB/server/commit/82f3ceed12)\
  2020-06-11 23:12:48 +0200
  * [MDEV-16470](https://jira.mariadb.org/browse/MDEV-16470): switch off user variables (and fixes of its support)
* [Revision #8ec21afc8e](https://github.com/MariaDB/server/commit/8ec21afc8e)\
  2020-06-10 19:29:25 +0300
  * [MDEV-22834](https://jira.mariadb.org/browse/MDEV-22834): Disks plugin - change datatype to bigint
* [Revision #e156a8da08](https://github.com/MariaDB/server/commit/e156a8da08)\
  2020-03-01 21:59:29 +0200
  * [MDEV-21851](https://jira.mariadb.org/browse/MDEV-21851): Error in BINLOG\_BASE64\_EVENT i s always error-logged as if it is done by Slave
* [Revision #762bf7a03b](https://github.com/MariaDB/server/commit/762bf7a03b)\
  2020-06-12 11:10:55 +0300
  * [MDEV-22602](https://jira.mariadb.org/browse/MDEV-22602) Disable UPDATE CASCADE for SQL constraints
* [Revision #02c255d1e0](https://github.com/MariaDB/server/commit/02c255d1e0)\
  2020-06-12 00:33:05 +0530
  * [MDEV-22119](https://jira.mariadb.org/browse/MDEV-22119): main.innodb\_ext\_key fails sporadically
* [Revision #c92f7e287f](https://github.com/MariaDB/server/commit/c92f7e287f)\
  2020-06-11 22:52:47 +0530
  * [MDEV-8139](https://jira.mariadb.org/browse/MDEV-8139) Fix Scrubbing
* [Revision #07d1c8567c](https://github.com/MariaDB/server/commit/07d1c8567c)\
  2020-06-10 16:26:13 +0200
  * post-fix for #1504
* [Revision #d3f4748254](https://github.com/MariaDB/server/commit/d3f4748254)\
  2020-06-11 10:29:03 +0200
  * [MDEV-22812](https://jira.mariadb.org/browse/MDEV-22812) "failed to create symbolic link" during the build
* [Revision #35acf39b5c](https://github.com/MariaDB/server/commit/35acf39b5c)\
  2020-06-11 18:14:39 +0530
  * [MDEV-21831](https://jira.mariadb.org/browse/MDEV-21831): Assertion \`length == pack\_length()' failed in Field\_inet6::sort\_string upon INSERT into RocksDB table
* [Revision #757e756d6e](https://github.com/MariaDB/server/commit/757e756d6e)\
  2020-06-11 17:30:33 +0300
  * [MDEV-22850](https://jira.mariadb.org/browse/MDEV-22850) Reduce buf\_pool.page\_hash latch contention
* [Revision #0af1b0bd21](https://github.com/MariaDB/server/commit/0af1b0bd21)\
  2020-06-06 07:37:05 +0900
  * Add information\_schema.spider\_wrapper\_protocols for knowing available wrappers of Spider
* [Revision #c9f262ee0d](https://github.com/MariaDB/server/commit/c9f262ee0d)\
  2020-06-11 15:00:00 +0300
  * [MDEV-22863](https://jira.mariadb.org/browse/MDEV-22863): Fix GCC 4.8.5 -Wconversion
* [Revision #7de4458d33](https://github.com/MariaDB/server/commit/7de4458d33)\
  2020-06-11 14:48:33 +0300
  * [MDEV-22865](https://jira.mariadb.org/browse/MDEV-22865) compilation failure on win32-debug
* [Revision #d6af055c55](https://github.com/MariaDB/server/commit/d6af055c55)\
  2020-06-11 14:47:34 +1000
  * [MDEV-22864](https://jira.mariadb.org/browse/MDEV-22864): cmake/libutils account for cmake-2.8.12.1
* [Revision #ade0f40ff1](https://github.com/MariaDB/server/commit/ade0f40ff1)\
  2020-06-10 18:42:47 +0530
  * [MDEV-22819](https://jira.mariadb.org/browse/MDEV-22819): Wrong result or Assertion \`ix > 0' failed in read\_to\_buffer upon select with GROUP BY and GROUP\_CONCAT
* [Revision #ba2c2cfb20](https://github.com/MariaDB/server/commit/ba2c2cfb20)\
  2020-06-11 11:47:03 +0530
  * Fix typo
* [Revision #72776d4c49](https://github.com/MariaDB/server/commit/72776d4c49)\
  2020-05-29 22:12:44 +0530
  * [MDEV-22722](https://jira.mariadb.org/browse/MDEV-22722) Assertion "inited==NONE" failed in handler::ha\_index\_init on the slave during UPDATE
* [Revision #7e798534f0](https://github.com/MariaDB/server/commit/7e798534f0)\
  2020-06-10 16:11:04 +0300
  * [MDEV-22858](https://jira.mariadb.org/browse/MDEV-22858) Remove unused innodb\_mem\_validate\_usec, innodb\_master\_purge\_usec
* [Revision #6e2d967b1b](https://github.com/MariaDB/server/commit/6e2d967b1b)\
  2020-06-09 23:03:08 +0400
  * [MDEV-14347](https://jira.mariadb.org/browse/MDEV-14347) CREATE PROCEDURE returns no error when using an unknown variable
* [Revision #264a98eaa0](https://github.com/MariaDB/server/commit/264a98eaa0)\
  2020-05-29 01:24:50 +0300
  * [MDEV-8069](https://jira.mariadb.org/browse/MDEV-8069) DROP or rebuild of a large table may lock up InnoDB
* Merge [Revision #af194ab5bd](https://github.com/MariaDB/server/commit/af194ab5bd) 2020-06-10 13:47:29 +0200 - Merge branch 'bb-10.5-[MDEV-22841](https://jira.mariadb.org/browse/MDEV-22841)' into 10.5
* [Revision #cc0205cf86](https://github.com/MariaDB/server/commit/cc0205cf86)\
  2020-04-26 22:43:57 +0300
  * [MDEV-19917](https://jira.mariadb.org/browse/MDEV-19917): Install Spider with a simple spider.cnf
* [Revision #aaaf005ce6](https://github.com/MariaDB/server/commit/aaaf005ce6)\
  2020-04-13 10:00:43 +0300
  * Deb: Clean up default configs for 10.5 era
* [Revision #680a13957c](https://github.com/MariaDB/server/commit/680a13957c)\
  2020-05-17 12:38:51 +0300
  * [MDEV-19933](https://jira.mariadb.org/browse/MDEV-19933): Sync mariadb-common and update-alternatives based /etc/mysql/
* [Revision #800eee42ce](https://github.com/MariaDB/server/commit/800eee42ce)\
  2020-06-09 14:36:29 +0530
  * [MDEV-22059](https://jira.mariadb.org/browse/MDEV-22059): MSAN report at replicate\_ignore\_table\_grant
* [Revision #dc06873474](https://github.com/MariaDB/server/commit/dc06873474)\
  2020-06-10 18:41:59 +1000
  * cmake: merge\_static\_libs - correct duplicate assumptions (#1583)
* [Revision #dd77f072f9](https://github.com/MariaDB/server/commit/dd77f072f9)\
  2020-06-10 08:12:06 +0200
  * [MDEV-22841](https://jira.mariadb.org/browse/MDEV-22841) ut\_new\_get\_key\_by\_file is unnecessarily expensive
* [Revision #ba4148698f](https://github.com/MariaDB/server/commit/ba4148698f)\
  2020-04-26 22:43:57 +0300
  * [MDEV-19917](https://jira.mariadb.org/browse/MDEV-19917): Install Spider with a simple spider.cnf
* [Revision #bb8477778b](https://github.com/MariaDB/server/commit/bb8477778b)\
  2020-04-13 10:00:43 +0300
  * Deb: Clean up default configs for 10.5 era
* [Revision #7c2079f600](https://github.com/MariaDB/server/commit/7c2079f600)\
  2020-05-17 12:38:51 +0300
  * [MDEV-19933](https://jira.mariadb.org/browse/MDEV-19933): Sync mariadb-common and update-alternatives based /etc/mysql/
* [Revision #840fb495ce](https://github.com/MariaDB/server/commit/840fb495ce)\
  2020-06-09 14:36:29 +0530
  * [MDEV-22059](https://jira.mariadb.org/browse/MDEV-22059): MSAN report at replicate\_ignore\_table\_grant
* [Revision #6e4e097bc2](https://github.com/MariaDB/server/commit/6e4e097bc2)\
  2020-06-10 18:41:59 +1000
  * cmake: merge\_static\_libs - correct duplicate assumptions (#1583)
* [Revision #17a7bafec0](https://github.com/MariaDB/server/commit/17a7bafec0)\
  2020-06-10 07:43:58 +0300
  * [MDEV-22110](https://jira.mariadb.org/browse/MDEV-22110) preparation: Remove mtr\_memo\_contains macros
* [Revision #d6f8c48424](https://github.com/MariaDB/server/commit/d6f8c48424)\
  2020-06-10 07:43:39 +0300
  * [MDEV-22110](https://jira.mariadb.org/browse/MDEV-22110) preparation: Remove some unused function parameters
* [Revision #59762ac4fa](https://github.com/MariaDB/server/commit/59762ac4fa)\
  2020-06-10 07:43:28 +0300
  * [MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053): Adjust results for innodb\_page\_hash\_locks=64
* [Revision #e76ca24bb1](https://github.com/MariaDB/server/commit/e76ca24bb1)\
  2020-06-10 07:29:26 +0300
  * Fix GCC -Wunused-function
* [Revision #3ccd6766d0](https://github.com/MariaDB/server/commit/3ccd6766d0)\
  2020-06-10 03:51:49 +0200
  * Fixed compilation error in DCMAKE\_BUILD\_TYPE=mysql\_release mode when WSREP enabled
* [Revision #648b54746c](https://github.com/MariaDB/server/commit/648b54746c)\
  2020-06-09 18:07:06 +0530
  * [MDEV-22399](https://jira.mariadb.org/browse/MDEV-22399): Remove multiple calls to enable and disable Handler::keyread and perform it after the plan refinement phase is done
* [Revision #70d4e55db9](https://github.com/MariaDB/server/commit/70d4e55db9)\
  2020-06-09 18:01:29 +0300
  * [MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053) fixup: Reduce contention in buf\_page\_get\_low()
* [Revision #e8a21ed301](https://github.com/MariaDB/server/commit/e8a21ed301)\
  2020-06-09 16:47:24 +0300
  * WIP
* [Revision #04c5cdffeb](https://github.com/MariaDB/server/commit/04c5cdffeb)\
  2020-06-09 10:23:47 +0530
  * [MDEV-22836](https://jira.mariadb.org/browse/MDEV-22836): Server crashes in err\_conv / ErrBuff::set\_str
* [Revision #89a33303c4](https://github.com/MariaDB/server/commit/89a33303c4)\
  2020-06-07 20:39:31 +0200
  * remove dead code
* [Revision #76cb2f9dd6](https://github.com/MariaDB/server/commit/76cb2f9dd6)\
  2020-06-09 12:54:04 +0400
  * [MDEV-21765](https://jira.mariadb.org/browse/MDEV-21765) Possibly inconsistent behavior of BIT\_xx functions with INET6 field
* [Revision #01e8459d93](https://github.com/MariaDB/server/commit/01e8459d93)\
  2020-06-08 19:56:43 +0300
  * [MDEV-22325](https://jira.mariadb.org/browse/MDEV-22325) ib\_logfile0 is too small for innodb\_thread\_concurrency=0. The size of ib\_logfile0 should be bigger than 200 kB \* innodb\_thread\_concurrency.
* [Revision #1b01833a4b](https://github.com/MariaDB/server/commit/1b01833a4b)\
  2020-06-08 13:14:27 +0300
  * [MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053) follow-up to reduce buf\_pool.mutex contention
* Merge [Revision #d3681335b1](https://github.com/MariaDB/server/commit/d3681335b1) 2020-06-08 12:58:11 +0300 - Merge 10.4 into 10.5
* Merge [Revision #57022dfb25](https://github.com/MariaDB/server/commit/57022dfb25) 2020-06-08 11:45:28 +0300 - Merge 10.3 into 10.4
* Merge [Revision #befb0bed68](https://github.com/MariaDB/server/commit/befb0bed68) 2020-06-08 11:09:49 +0300 - Merge 10.2 into 10.3
* [Revision #f458b40f66](https://github.com/MariaDB/server/commit/f458b40f66)\
  2020-06-08 10:28:34 +0300
  * [MDEV-22827](https://jira.mariadb.org/browse/MDEV-22827) InnoDB: Failing assertion: purge\_sys->n\_stop == 0
* [Revision #e9dbbf1120](https://github.com/MariaDB/server/commit/e9dbbf1120)\
  2020-06-06 11:38:38 -0700
  * [MDEV-22748](https://jira.mariadb.org/browse/MDEV-22748) MariaDB crash on WITH RECURSIVE large query
* [Revision #a9bee9884a](https://github.com/MariaDB/server/commit/a9bee9884a)\
  2020-06-07 16:30:50 +0300
  * Don't allow ALTER TABLE ... ORDER BY on SEQUENCE objects
* [Revision #e6a6382f15](https://github.com/MariaDB/server/commit/e6a6382f15)\
  2020-06-07 16:23:44 +0300
  * Don't allow illegal create options for SEQUENCE
* [Revision #fad348a9a6](https://github.com/MariaDB/server/commit/fad348a9a6)\
  2020-06-07 16:23:47 +0400
  * [MDEV-22822](https://jira.mariadb.org/browse/MDEV-22822) sql\_mode="oracle" cannot declare without variable errors
* [Revision #996431fdac](https://github.com/MariaDB/server/commit/996431fdac)\
  2020-06-08 12:52:29 +0300
  * Partition the test innodb.temp\_table\_savepoint
* [Revision #3be169093b](https://github.com/MariaDB/server/commit/3be169093b)\
  2020-06-07 18:54:34 +0300
  * [MDEV-22824](https://jira.mariadb.org/browse/MDEV-22824) Buffer overflow in dict\_table\_t::parse\_name()
* Merge [Revision #0e69f601aa](https://github.com/MariaDB/server/commit/0e69f601aa) 2020-06-07 12:22:06 +0300 - Merge 10.4 into 10.5
* [Revision #eb14e073ea](https://github.com/MariaDB/server/commit/eb14e073ea)\
  2020-06-03 13:36:36 +0530
  * [MDEV-22719](https://jira.mariadb.org/browse/MDEV-22719) Long unique keys are not created when individual key\_part->length < max\_key\_length but SUM(key\_parts->length) > max\_key\_length
* [Revision #e208f91ba8](https://github.com/MariaDB/server/commit/e208f91ba8)\
  2020-05-25 15:29:44 +0530
  * [MDEV-21804](https://jira.mariadb.org/browse/MDEV-21804) Assertion \`marked\_for\_read()' failed upon INSERT into table with long unique blob under binlog\_row\_image=NOBLOB
* Merge [Revision #c7a2fb1e08](https://github.com/MariaDB/server/commit/c7a2fb1e08) 2020-06-06 22:05:32 +0300 - Merge 10.3 into 10.4
* Merge [Revision #4612cb88fa](https://github.com/MariaDB/server/commit/4612cb88fa) 2020-06-06 21:38:57 +0300 - Merge 10.2 into 10.3
* [Revision #be0c46eb97](https://github.com/MariaDB/server/commit/be0c46eb97)\
  2020-06-06 21:34:21 +0300
  * [MDEV-22817](https://jira.mariadb.org/browse/MDEV-22817): Skip the test in --embedded
* Merge [Revision #b3e395a13e](https://github.com/MariaDB/server/commit/b3e395a13e) 2020-06-06 18:50:25 +0300 - Merge 10.2 into 10.3
* [Revision #187b9c924e](https://github.com/MariaDB/server/commit/187b9c924e)\
  2020-06-06 18:07:13 +0300
  * [MDEV-22817](https://jira.mariadb.org/browse/MDEV-22817): Add a test case
* Merge [Revision #0df01ccb66](https://github.com/MariaDB/server/commit/0df01ccb66) 2020-06-06 18:07:04 +0300 - Merge 10.1 into 10.2
* [Revision #f30ff10c8d](https://github.com/MariaDB/server/commit/f30ff10c8d)\
  2020-05-29 00:32:08 +0530
  * [MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715): SIGSEGV in radixsort\_for\_str\_ptr and in native\_compare/my\_qsort2 (optimized builds)
* [Revision #1bd5b75c73](https://github.com/MariaDB/server/commit/1bd5b75c73)\
  2020-06-06 09:32:18 +0300
  * [MDEV-22818](https://jira.mariadb.org/browse/MDEV-22818) Server crash on corrupted ROW\_FORMAT=COMPRESSED page
* [Revision #7a695d8a82](https://github.com/MariaDB/server/commit/7a695d8a82)\
  2020-06-05 23:33:24 +0300
  * fix compilation with VS2019, preview of 16.7 version
* [Revision #a8c200c73c](https://github.com/MariaDB/server/commit/a8c200c73c)\
  2020-06-05 10:38:40 -0700
  * [MDEV-22042](https://jira.mariadb.org/browse/MDEV-22042) Server crash in Item\_field::print on ANALYZE FORMAT=JSON
* Merge [Revision #fff7897e3a](https://github.com/MariaDB/server/commit/fff7897e3a) 2020-06-05 19:58:52 +0200 - Merge branch '10.2' of [server](https://github.com/MariaDB/server) into 10.2
* Merge [Revision #5f55f69e4a](https://github.com/MariaDB/server/commit/5f55f69e4a) 2020-06-05 18:32:37 +0200 - Merge 10.1 into 10.2
* [Revision #3f019d1771](https://github.com/MariaDB/server/commit/3f019d1771)\
  2020-06-03 14:14:08 +0200
  * Added missing include files to check for debug\_sync
* [Revision #8ec0e9111a](https://github.com/MariaDB/server/commit/8ec0e9111a)\
  2020-06-01 12:34:33 +0300
  * [MDEV-22763](https://jira.mariadb.org/browse/MDEV-22763) backporting [MDEV-20225](https://jira.mariadb.org/browse/MDEV-20225) fix into 10.1
* [Revision #40dbf0ea0e](https://github.com/MariaDB/server/commit/40dbf0ea0e)\
  2020-05-23 22:38:20 +0200
  * Fix duplicate word
* [Revision #e14ffd85d0](https://github.com/MariaDB/server/commit/e14ffd85d0)\
  2020-06-06 17:36:25 +0300
  * [MDEV-22721](https://jira.mariadb.org/browse/MDEV-22721) fixup for 32-bit GCC
* [Revision #7ae12371dd](https://github.com/MariaDB/server/commit/7ae12371dd)\
  2020-06-07 12:21:32 +0300
  * [MDEV-22817](https://jira.mariadb.org/browse/MDEV-22817) Assertion idlen <= MAX\_TABLE\_NAME\_LEN in create\_table\_info\_t::create\_foreign\_keys()
* [Revision #a08a8bc191](https://github.com/MariaDB/server/commit/a08a8bc191)\
  2020-06-06 17:29:41 +0300
  * [MDEV-22721](https://jira.mariadb.org/browse/MDEV-22721): Fix GCC 5.3.1 -Wconversion
* [Revision #79cdd7e76b](https://github.com/MariaDB/server/commit/79cdd7e76b)\
  2020-06-05 12:57:42 +0400
  * [MDEV-20305](https://jira.mariadb.org/browse/MDEV-20305) Data loss on DOUBLE and DECIMAL conversion to INT
* Merge [Revision #a793ae5bc1](https://github.com/MariaDB/server/commit/a793ae5bc1) 2020-06-06 08:55:22 +0300 - Merge 10.4 into 10.5
* Merge [Revision #9d479e2577](https://github.com/MariaDB/server/commit/9d479e2577) 2020-06-05 18:00:14 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #b9b279ecc4](https://github.com/MariaDB/server/commit/b9b279ecc4) 2020-06-05 17:59:35 +0200 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #15cdcb2af8](https://github.com/MariaDB/server/commit/15cdcb2af8)\
  2020-06-05 17:56:34 +0200
  * Fix appveyor build.
* [Revision #62516c53c1](https://github.com/MariaDB/server/commit/62516c53c1)\
  2020-06-06 08:51:38 +0300
  * [MDEV-22816](https://jira.mariadb.org/browse/MDEV-22816) Assertion \`node->space == fil\_system.sys\_space' failed in fil\_aio\_callback
* [Revision #095d656dea](https://github.com/MariaDB/server/commit/095d656dea)\
  2020-06-06 08:28:14 +0300
  * [MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053) fixup: MSAN use-of-uninitialized-value
* Merge [Revision #6877ef9a7c](https://github.com/MariaDB/server/commit/6877ef9a7c) 2020-06-05 20:36:43 +0300 - Merge 10.4 into 10.5
* Merge [Revision #68d9d512e9](https://github.com/MariaDB/server/commit/68d9d512e9) 2020-06-05 18:05:22 +0300 - Merge 10.3 into 10.4
* [Revision #286e52e948](https://github.com/MariaDB/server/commit/286e52e948)\
  2020-06-05 17:45:27 +0300
  * After-merge fix: GCC -Wmaybe-uninitialized
* Merge [Revision #680463a8d9](https://github.com/MariaDB/server/commit/680463a8d9) 2020-06-05 16:51:26 +0300 - Merge 10.2 into 10.3
* [Revision #efc70da5fd](https://github.com/MariaDB/server/commit/efc70da5fd)\
  2020-06-05 14:59:33 +0300
  * [MDEV-22769](https://jira.mariadb.org/browse/MDEV-22769) Shutdown hang or crash due to XA breaking locks
* [Revision #138c11cce5](https://github.com/MariaDB/server/commit/138c11cce5)\
  2020-06-04 12:29:32 +0300
  * [MDEV-22790](https://jira.mariadb.org/browse/MDEV-22790) Race between btr\_page\_mtr\_lock() dropping AHI on the same block
* [Revision #3677dd5cb4](https://github.com/MariaDB/server/commit/3677dd5cb4)\
  2020-06-05 15:20:20 +0300
  * [MDEV-22646](https://jira.mariadb.org/browse/MDEV-22646): Fix a memory leak
* [Revision #1828196f73](https://github.com/MariaDB/server/commit/1828196f73)\
  2020-06-05 13:29:01 +0200
  * Windows, build tweak.
* [Revision #29ed04cb6d](https://github.com/MariaDB/server/commit/29ed04cb6d)\
  2020-06-03 14:43:13 +0200
  * add stress suite to the list of default suites to run
* [Revision #dce4c0f979](https://github.com/MariaDB/server/commit/dce4c0f979)\
  2020-04-23 21:58:52 +0400
  * [MDEV-22339](https://jira.mariadb.org/browse/MDEV-22339) - Assertion \`str\_length < len' failed
* [Revision #c5883debd6](https://github.com/MariaDB/server/commit/c5883debd6)\
  2020-06-04 16:31:29 +0300
  * dict\_check\_sys\_tables(): Do not rely on buf\_page\_optimistic\_get()
* [Revision #f69278bcd0](https://github.com/MariaDB/server/commit/f69278bcd0)\
  2020-06-02 16:31:53 +0530
  * [MDEV-16230](https://jira.mariadb.org/browse/MDEV-16230): Server crashes when Analyze format=json is run with a window function with empty PARTITION BY and ORDER BY clauses
* [Revision #eba2d10ac5](https://github.com/MariaDB/server/commit/eba2d10ac5)\
  2020-06-04 10:24:10 +0300
  * [MDEV-22721](https://jira.mariadb.org/browse/MDEV-22721) Remove bloat caused by InnoDB logger class
* [Revision #ad2bf1129c](https://github.com/MariaDB/server/commit/ad2bf1129c)\
  2020-05-27 13:03:06 +0530
  * [MDEV-22646](https://jira.mariadb.org/browse/MDEV-22646) Assertion \`table2->cached' failed in dict\_table\_t::add\_to\_cache
* [Revision #ca3aa67964](https://github.com/MariaDB/server/commit/ca3aa67964)\
  2020-06-03 12:14:11 +0300
  * [MDEV-22577](https://jira.mariadb.org/browse/MDEV-22577) innodb\_fast\_shutdown=0 fails to report purge progress
* [Revision #05693cf214](https://github.com/MariaDB/server/commit/05693cf214)\
  2020-06-04 12:12:49 +0300
  * [MDEV-22112](https://jira.mariadb.org/browse/MDEV-22112) Assertion \`tab\_part\_info->part\_type == RANGE\_PARTITION || tab\_part\_info->part\_type == LIST\_PARTITION' failed in prep\_alter\_part\_table
* [Revision #6404645980](https://github.com/MariaDB/server/commit/6404645980)\
  2020-06-04 19:38:31 +0530
  * [MDEV-21626](https://jira.mariadb.org/browse/MDEV-21626): Optimizer misses the details about the picked join order
* [Revision #374f94c5a7](https://github.com/MariaDB/server/commit/374f94c5a7)\
  2020-06-05 19:04:04 +0300
  * [MDEV-21751](https://jira.mariadb.org/browse/MDEV-21751) followup: Bypass the change buffer on slow shutdown
* [Revision #d642c5b83d](https://github.com/MariaDB/server/commit/d642c5b83d)\
  2020-06-05 16:21:23 +0200
  * Reduce CPU usage in srv\_purge\_shutdown.
* [Revision #de1dbb7180](https://github.com/MariaDB/server/commit/de1dbb7180)\
  2020-06-01 16:24:15 +0530
  * [MDEV-21282](https://jira.mariadb.org/browse/MDEV-21282) Assertion 'mariadb\_table' failed in gcol.innodb\_virtual\_debug\_purge
* [Revision #d88870e6cc](https://github.com/MariaDB/server/commit/d88870e6cc)\
  2020-05-28 19:50:35 +0900
  * MENT-805 ODBC login fails with Spider from bb-10.5-MENT-30 if password contains a semicolon
* [Revision #b3250ab3b2](https://github.com/MariaDB/server/commit/b3250ab3b2)\
  2020-05-15 23:53:12 +0900
  * MENT-787 Server from bb-10.5-MENT-30 crashes upon Spider installation
* [Revision #0b7fe26e9d](https://github.com/MariaDB/server/commit/0b7fe26e9d)\
  2020-05-08 20:04:53 +0900
  * Change Spider's plugin maturity to BETA
* [Revision #a756d54704](https://github.com/MariaDB/server/commit/a756d54704)\
  2020-04-29 03:26:19 +0900
  * Fix issue caused by using spider\_bgs\_mode = 2 when Spider use limit\_mode = 1 internally for data nodes.
* [Revision #9ba56c072c](https://github.com/MariaDB/server/commit/9ba56c072c)\
  2020-04-27 08:46:30 +0900
  * Add a parameter spider\_strict\_group\_by for supporting ONLY\_FULL\_GROUP\_BY
* [Revision #bbb1140d47](https://github.com/MariaDB/server/commit/bbb1140d47)\
  2020-04-11 01:03:19 +0900
  * add pointer of ha\_spider to Spider's use\_result function
* [Revision #f16633c175](https://github.com/MariaDB/server/commit/f16633c175)\
  2020-04-10 18:12:58 +0900
  * fix evaluating bitmap issue in spider
* [Revision #18f32f2cd2](https://github.com/MariaDB/server/commit/18f32f2cd2)\
  2020-03-22 09:38:12 +0900
  * fix issue for escape charcters in table parameters of Spider
* [Revision #793b84b817](https://github.com/MariaDB/server/commit/793b84b817)\
  2020-03-22 09:36:37 +0900
  * add a table parameter "dsn" to Spider
* [Revision #932baa9410](https://github.com/MariaDB/server/commit/932baa9410)\
  2020-03-04 21:42:07 +0900
  * fix build errors on windows environments
* [Revision #6c3180bed9](https://github.com/MariaDB/server/commit/6c3180bed9)\
  2020-03-03 08:15:08 +0900
  * add test result of spider.bugfix insert\_select
* [Revision #94861b83f4](https://github.com/MariaDB/server/commit/94861b83f4)\
  2020-03-03 08:11:46 +0900
  * prepare for adding new connectors for Spider
* [Revision #23c8adda74](https://github.com/MariaDB/server/commit/23c8adda74)\
  2020-03-03 03:06:33 +0900
  * [MDEV-6268](https://jira.mariadb.org/browse/MDEV-6268) SPIDER table with no COMMENT clause causes queries to wait forever
* [Revision #272625d92a](https://github.com/MariaDB/server/commit/272625d92a)\
  2020-03-03 02:54:06 +0900
  * fix Spider executing one by one commands before SQL
* [Revision #c34deb4cd2](https://github.com/MariaDB/server/commit/c34deb4cd2)\
  2020-03-03 02:53:25 +0900
  * fix memory calculate for spider\_mon\_table\_cache
* [Revision #d3a6ed0550](https://github.com/MariaDB/server/commit/d3a6ed0550)\
  2020-03-03 02:52:46 +0900
  * fix divided lock table issue of Spider
* [Revision #418f16116f](https://github.com/MariaDB/server/commit/418f16116f)\
  2020-03-03 02:51:59 +0900
  * use ifdef for unused attributes for Spider
* [Revision #e954d9de88](https://github.com/MariaDB/server/commit/e954d9de88)\
  2020-03-03 02:50:40 +0900
  * [MDEV-19002](https://jira.mariadb.org/browse/MDEV-19002) Spider performance optimization with partition
* [Revision #8e6e5acef1](https://github.com/MariaDB/server/commit/8e6e5acef1)\
  2020-06-05 02:40:36 +1000
  * [MDEV-22753](https://jira.mariadb.org/browse/MDEV-22753) Server crashes upon INSERT into versioned partitioned table with WITHOUT OVERLAPS
* [Revision #35d327fddb](https://github.com/MariaDB/server/commit/35d327fddb)\
  2020-06-04 20:04:34 +1000
  * [MDEV-22599](https://jira.mariadb.org/browse/MDEV-22599) WITHOUT OVERLAPS does not work with prefix indexes
* [Revision #0c595bdeaa](https://github.com/MariaDB/server/commit/0c595bdeaa)\
  2020-06-02 16:06:41 +1000
  * [MDEV-22434](https://jira.mariadb.org/browse/MDEV-22434) UPDATE on RocksDB table with WITHOUT OVERLAPS fails
* [Revision #c3e09a2d3f](https://github.com/MariaDB/server/commit/c3e09a2d3f)\
  2020-06-01 22:30:58 +1000
  * [MDEV-22439](https://jira.mariadb.org/browse/MDEV-22439) Add FOR PORTION OF statements to the test for WITHOUT OVERLAPS
* [Revision #b1ab211dee](https://github.com/MariaDB/server/commit/b1ab211dee)\
  2020-06-05 12:35:46 +0300
  * [MDEV-15053](https://jira.mariadb.org/browse/MDEV-15053) Reduce buf\_pool\_t::mutex contention
* [Revision #9c55f83eae](https://github.com/MariaDB/server/commit/9c55f83eae)\
  2020-06-04 23:54:19 +0200
  * Cleanup - remove HAVE\_AIOWAIT and associated code from mysys
* [Revision #4af3f84895](https://github.com/MariaDB/server/commit/4af3f84895)\
  2020-06-04 13:03:22 +0200
  * For better experience in Visual Studio IDE, add header files to Innodb sources
* [Revision #4adc1269cc](https://github.com/MariaDB/server/commit/4adc1269cc)\
  2020-06-03 21:52:17 +0200
  * FreeBSD compilation fixes
* [Revision #70ab43b5b0](https://github.com/MariaDB/server/commit/70ab43b5b0)\
  2020-06-02 16:30:22 +0200
  * disable Cassandra engine by default
* [Revision #2fcff310d0](https://github.com/MariaDB/server/commit/2fcff310d0)\
  2020-06-04 14:21:04 +0400
  * [MDEV-21902](https://jira.mariadb.org/browse/MDEV-21902) Nested JSON\_ARRAYAGG in JSON\_OBJECT should not get escaped.
* [Revision #74198384e1](https://github.com/MariaDB/server/commit/74198384e1)\
  2020-06-04 13:53:14 +0400
  * [MDEV-21914](https://jira.mariadb.org/browse/MDEV-21914) JSON\_ARRAYAGG doesn't reject ORDER BY clause, but doesn't work either.
* [Revision #07daf73542](https://github.com/MariaDB/server/commit/07daf73542)\
  2020-06-04 11:00:17 +0400
  * [MDEV-22084](https://jira.mariadb.org/browse/MDEV-22084) Squared brackets missing from JSON\_ARRAYAGG when used in a view.
* [Revision #bb47050e1f](https://github.com/MariaDB/server/commit/bb47050e1f)\
  2020-06-04 10:00:56 +0400
  * [MDEV-22640](https://jira.mariadb.org/browse/MDEV-22640), [MDEV-22449](https://jira.mariadb.org/browse/MDEV-22449), [MDEV-21528](https://jira.mariadb.org/browse/MDEV-21528) JSON\_ARRAYAGG crashes with NULL values.
* [Revision #e7bab059b7](https://github.com/MariaDB/server/commit/e7bab059b7)\
  2020-06-03 17:39:33 +0200
  * [MDEV-22787](https://jira.mariadb.org/browse/MDEV-22787) postfix
* [Revision #4c52223493](https://github.com/MariaDB/server/commit/4c52223493)\
  2020-06-03 16:50:54 +0200
  * [MDEV-21751](https://jira.mariadb.org/browse/MDEV-21751) postfix
* [Revision #bee4b044f6](https://github.com/MariaDB/server/commit/bee4b044f6)\
  2020-06-03 16:19:13 +0200
  * [MDEV-21751](https://jira.mariadb.org/browse/MDEV-21751) innodb\_fast\_shutdown=0 can be unnecessarily slow
* [Revision #839ad5e132](https://github.com/MariaDB/server/commit/839ad5e132)\
  2020-06-03 16:09:00 +0400
  * [MDEV-22758](https://jira.mariadb.org/browse/MDEV-22758) Assertion \`!item->null\_value' failed in Type\_handler\_inet6::make\_sort\_key\_part
* [Revision #5b18ade0df](https://github.com/MariaDB/server/commit/5b18ade0df)\
  2020-06-03 16:49:06 +0300
  * [MDEV-22787](https://jira.mariadb.org/browse/MDEV-22787) fts\_optimize\_shutdown() deletes timer prematurely
* [Revision #58d2d82022](https://github.com/MariaDB/server/commit/58d2d82022)\
  2020-06-03 14:07:30 +0300
  * [MDEV-22710](https://jira.mariadb.org/browse/MDEV-22710) Assertion ...status != buf\_page\_t::FREED in ibuf\_remove\_free\_page()
* [Revision #463a8fc5fd](https://github.com/MariaDB/server/commit/463a8fc5fd)\
  2020-06-03 18:59:20 +1000
  * [MDEV-22641](https://jira.mariadb.org/browse/MDEV-22641): postfix - crc32{,c} fixups for ppc64
* Merge [Revision #701efbb25b](https://github.com/MariaDB/server/commit/701efbb25b) 2020-06-03 09:45:39 +0300 - Merge 10.4 into 10.5
* Merge [Revision #8059148154](https://github.com/MariaDB/server/commit/8059148154) 2020-06-03 07:32:09 +0300 - Merge 10.3 into 10.4
* Merge [Revision #8300f639a1](https://github.com/MariaDB/server/commit/8300f639a1) 2020-06-02 10:25:11 +0300 - Merge 10.2 into 10.3
* [Revision #50641db2d1](https://github.com/MariaDB/server/commit/50641db2d1)\
  2020-06-01 15:38:04 +0200
  * fix warning
* [Revision #02f68552a4](https://github.com/MariaDB/server/commit/02f68552a4)\
  2020-06-01 14:34:16 +0530
  * [MDEV-22650](https://jira.mariadb.org/browse/MDEV-22650) Dirty compressed page checksum validation fails
* [Revision #83d0e72b34](https://github.com/MariaDB/server/commit/83d0e72b34)\
  2020-06-01 10:23:11 +0300
  * Cleanup: Remove thr\_is\_recv(), trx\_is\_recv()
* [Revision #c50b7bee33](https://github.com/MariaDB/server/commit/c50b7bee33)\
  2020-06-01 10:18:47 +0300
  * [MDEV-21615](https://jira.mariadb.org/browse/MDEV-21615) InnoDB: innodb\_page\_size=x requires... should be logged as error
* Merge [Revision #d72eebaa3d](https://github.com/MariaDB/server/commit/d72eebaa3d) 2020-06-01 09:33:03 +0300 - Merge 10.1 into 10.2
* [Revision #49854811fa](https://github.com/MariaDB/server/commit/49854811fa)\
  2020-05-29 22:51:45 +0400
  * Attempt fixing mroonga gcc 8 build failure
* [Revision #c279878493](https://github.com/MariaDB/server/commit/c279878493)\
  2019-10-16 19:00:43 +0400
  * Thread safe histograms loading
* [Revision #609a0d3db3](https://github.com/MariaDB/server/commit/609a0d3db3)\
  2019-10-16 18:19:59 +0400
  * Thread safe statistics loading
* [Revision #1055a7f4fc](https://github.com/MariaDB/server/commit/1055a7f4fc)\
  2019-10-11 17:20:28 +0400
  * Simplified away statistics\_for\_tables\_is\_needed()
* [Revision #a2932e86b5](https://github.com/MariaDB/server/commit/a2932e86b5)\
  2020-05-29 15:31:24 +0400
  * [MDEV-22744](https://jira.mariadb.org/browse/MDEV-22744) \*SAN: sql/item\_xmlfunc.cc:791:43: runtime error: downcast of address ... which does not point to an object of type 'Item\_func' note: object is of type 'Item\_bool' (on optimized builds)
* [Revision #a1b3bebe1f](https://github.com/MariaDB/server/commit/a1b3bebe1f)\
  2020-05-28 19:34:27 +0200
  * fix pre-definition for embedded server for find\_user\_or\_anon()
* [Revision #957cb7b7ba](https://github.com/MariaDB/server/commit/957cb7b7ba)\
  2020-05-12 16:16:05 +0200
  * [MDEV-22312](https://jira.mariadb.org/browse/MDEV-22312): Bad error message for SET DEFAULT ROLE when user account is not granted the role
* [Revision #4832b751ad](https://github.com/MariaDB/server/commit/4832b751ad)\
  2020-05-31 11:00:47 +0200
  * cmake: quieter
* [Revision #804761a844](https://github.com/MariaDB/server/commit/804761a844)\
  2020-06-02 08:18:17 +0300
  * [MDEV-22770](https://jira.mariadb.org/browse/MDEV-22770) trx\_undo\_report\_rename() fails to release page latches
* [Revision #95ac790296](https://github.com/MariaDB/server/commit/95ac790296)\
  2020-06-02 21:25:51 +0300
  * [MDEV-22773](https://jira.mariadb.org/browse/MDEV-22773) Assertion page\_get\_page\_no... in btr\_pcur\_store\_position()
* [Revision #457e3128e0](https://github.com/MariaDB/server/commit/457e3128e0)\
  2020-06-02 21:28:21 +0300
  * Added larger timeout to backup\_stages.test
* [Revision #d5e8b4d7f9](https://github.com/MariaDB/server/commit/d5e8b4d7f9)\
  2020-06-02 14:17:48 +0530
  * [MDEV-22509](https://jira.mariadb.org/browse/MDEV-22509): Server crashes in Field\_inet6::store\_inet6\_null\_with\_warn / Field::maybe\_null
* [Revision #6df2f2db11](https://github.com/MariaDB/server/commit/6df2f2db11)\
  2020-06-02 14:40:51 +0300
  * [MDEV-21546](https://jira.mariadb.org/browse/MDEV-21546) main.backup\_stages occasionally reports lock wait timeout
* [Revision #0d6d63e150](https://github.com/MariaDB/server/commit/0d6d63e150)\
  2020-06-02 08:17:10 +0300
  * [MDEV-22027](https://jira.mariadb.org/browse/MDEV-22027) Assertion oldest\_lsn >= log\_sys.last\_checkpoint\_lsn failed
* [Revision #661ebd4699](https://github.com/MariaDB/server/commit/661ebd4699)\
  2020-06-01 16:21:50 +0200
  * Fix my\_checksum declaration.
* Merge [Revision #6e6d79a5cf](https://github.com/MariaDB/server/commit/6e6d79a5cf) 2020-06-01 15:44:01 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #f1c35a996f](https://github.com/MariaDB/server/commit/f1c35a996f) 2020-06-01 15:43:14 +0200 - Merge branch '10.3' into 10.4
* [Revision #fd2b46d879](https://github.com/MariaDB/server/commit/fd2b46d879)\
  2020-06-01 15:38:04 +0200
  * fix warning
* [Revision #ade8253cb9](https://github.com/MariaDB/server/commit/ade8253cb9)\
  2020-05-30 02:27:33 +0530
  * [MDEV-22303](https://jira.mariadb.org/browse/MDEV-22303): Incorrect ordering with REGEXP\_REPLACE and OFFSET/LIMIT
* [Revision #132d5822e2](https://github.com/MariaDB/server/commit/132d5822e2)\
  2019-11-01 16:40:26 +0900
  * MENT-458 MTR Big test "spider/bugfix.sql\_mode\_mariadb & myself" are both failing on Azure MTR pipeline
* [Revision #1d393fed71](https://github.com/MariaDB/server/commit/1d393fed71)\
  2019-11-01 16:45:48 +0900
  * MENT-456 MTR Big test "spider.show\_system\_tables" is failing on Azure MTR pipeline
* [Revision #33b839b2e7](https://github.com/MariaDB/server/commit/33b839b2e7)\
  2020-06-01 14:30:21 +0400
  * [MDEV-20280](https://jira.mariadb.org/browse/MDEV-20280) PERCENTILE\_DISC() rejects temporal and string input
* [Revision #f22093ad39](https://github.com/MariaDB/server/commit/f22093ad39)\
  2020-06-01 14:00:35 +0400
  * [MDEV-22764](https://jira.mariadb.org/browse/MDEV-22764) Crash with a stored aggregate function returning INET6
* [Revision #dec3f8ca69](https://github.com/MariaDB/server/commit/dec3f8ca69)\
  2020-06-01 14:04:06 +0530
  * [MDEV-22641](https://jira.mariadb.org/browse/MDEV-22641): Provide SIMD optimized wrapper for zlib crc32() (#1558)
* [Revision #6a6aa1c089](https://github.com/MariaDB/server/commit/6a6aa1c089)\
  2020-06-01 11:46:30 +0400
  * [MDEV-21764](https://jira.mariadb.org/browse/MDEV-21764) CONNECT table with INET6 field produces warnings upon SELECT
* [Revision #35cbbd4d70](https://github.com/MariaDB/server/commit/35cbbd4d70)\
  2020-06-01 10:35:01 +0400
  * [MDEV-20809](https://jira.mariadb.org/browse/MDEV-20809) EXTRACT from INET6 value does not produce any warnings
* [Revision #f67522ede6](https://github.com/MariaDB/server/commit/f67522ede6)\
  2020-05-31 20:29:21 +0300
  * [MDEV-22249](https://jira.mariadb.org/browse/MDEV-22249) Upgrade testing between major versions in MTR
* Merge [Revision #4a0b56f604](https://github.com/MariaDB/server/commit/4a0b56f604) 2020-05-31 10:28:59 +0300 - Merge 10.4 into 10.5
* Merge [Revision #6da14d7b4a](https://github.com/MariaDB/server/commit/6da14d7b4a) 2020-05-30 11:04:27 +0300 - Merge 10.3 into 10.4
* [Revision #2e1d10ecac](https://github.com/MariaDB/server/commit/2e1d10ecac)\
  2020-05-30 10:48:11 +0300
  * Add end-of-test markers to ease merges
* Merge [Revision #e9aaa10c11](https://github.com/MariaDB/server/commit/e9aaa10c11) 2020-05-29 22:21:19 +0300 - Merge 10.2 into 10.3
* [Revision #38ea795bb6](https://github.com/MariaDB/server/commit/38ea795bb6)\
  2020-05-29 01:51:30 +0900
  * Add a counter to avoid multiple initialization of Groonga mecab tokenizer
* [Revision #6e6a4227c0](https://github.com/MariaDB/server/commit/6e6a4227c0)\
  2020-05-28 10:21:46 +0900
  * Add grn\_db\_fin\_mecab\_tokenizer to finalyze mecab tokenizer
* [Revision #069200267d](https://github.com/MariaDB/server/commit/069200267d)\
  2020-05-28 15:03:28 +0200
  * Fix cmake warning - custom command succeeds without creating own OUTPUT.
* [Revision #b00cd3e453](https://github.com/MariaDB/server/commit/b00cd3e453)\
  2020-05-28 15:02:10 +0200
  * [MDEV-22743](https://jira.mariadb.org/browse/MDEV-22743) Windows 10 MSI installer : port in use is not determined
* [Revision #ff72f36948](https://github.com/MariaDB/server/commit/ff72f36948)\
  2020-05-28 02:06:23 +0200
  * MSI installer : Use CAQuietExec64 on Win64 , not CAQuietExec
* [Revision #e2d7da4982](https://github.com/MariaDB/server/commit/e2d7da4982)\
  2020-05-28 01:43:21 +0200
  * Remove unused WiX source file
* [Revision #8afcc37c68](https://github.com/MariaDB/server/commit/8afcc37c68)\
  2020-05-26 14:11:41 +0200
  * update C/C
* [Revision #2c9c9acbfc](https://github.com/MariaDB/server/commit/2c9c9acbfc)\
  2020-05-26 12:11:24 +0200
  * bintars should use bundled PCRE
* [Revision #9fd8f1b264](https://github.com/MariaDB/server/commit/9fd8f1b264)\
  2020-05-24 17:30:57 +0200
  * mtr: update titlebar when the test ends, not when it starts
* [Revision #e64dc07125](https://github.com/MariaDB/server/commit/e64dc07125)\
  2020-05-24 21:10:41 +0200
  * assert(a && b); -> assert(a); assert(b);
* [Revision #04726f2920](https://github.com/MariaDB/server/commit/04726f2920)\
  2020-05-23 18:35:42 +0200
  * get rid of cmake warning
* [Revision #8cf589218f](https://github.com/MariaDB/server/commit/8cf589218f)\
  2020-05-22 19:50:22 +0200
  * optimize performance of the build in a fresh clone
* [Revision #cceb965a79](https://github.com/MariaDB/server/commit/cceb965a79)\
  2020-05-22 12:05:53 +0200
  * Revert "[MDEV-12445](https://jira.mariadb.org/browse/MDEV-12445) : Rocksdb does not shutdown worker threads and aborts in memleak check on server shutdown"
* [Revision #6af37ba881](https://github.com/MariaDB/server/commit/6af37ba881)\
  2020-05-21 01:31:17 +0200
  * fix rocksdb zstd detection
* [Revision #ad77247866](https://github.com/MariaDB/server/commit/ad77247866)\
  2020-05-20 17:04:22 +0200
  * [MDEV-21958](https://jira.mariadb.org/browse/MDEV-21958) Query having many NOT-IN clauses running forever and causing available free memory to use completely
* [Revision #1e951155bd](https://github.com/MariaDB/server/commit/1e951155bd)\
  2020-05-20 17:02:47 +0200
  * bugfix: use THD::main\_mem\_root for kill error message
* [Revision #b01c8a6cc8](https://github.com/MariaDB/server/commit/b01c8a6cc8)\
  2020-05-14 16:18:01 +0200
  * [MDEV-22558](https://jira.mariadb.org/browse/MDEV-22558) wrong error for invalid utf8 table comment
* [Revision #39c141b4ae](https://github.com/MariaDB/server/commit/39c141b4ae)\
  2020-05-13 19:48:23 +0200
  * don't include .git files in source packages
* [Revision #a50e6c9eb1](https://github.com/MariaDB/server/commit/a50e6c9eb1)\
  2020-05-13 13:10:35 +0200
  * [MDEV-17153](https://jira.mariadb.org/browse/MDEV-17153) server crash on repair table ... use\_frm
* [Revision #19da9a51ae](https://github.com/MariaDB/server/commit/19da9a51ae)\
  2020-05-28 22:22:20 +0300
  * [MDEV-16937](https://jira.mariadb.org/browse/MDEV-16937) Strict SQL with system versioned tables causes issues
* [Revision #dd9773b723](https://github.com/MariaDB/server/commit/dd9773b723)\
  2020-05-28 22:22:19 +0300
  * [MDEV-22413](https://jira.mariadb.org/browse/MDEV-22413) Server hangs upon UPDATE on a view reading from versioned partitioned table
* [Revision #3e9b96b6ff](https://github.com/MariaDB/server/commit/3e9b96b6ff)\
  2019-06-13 19:29:02 +0300
  * [MDEV-18794](https://jira.mariadb.org/browse/MDEV-18794) append\_drop\_column() small refactoring
* [Revision #dac1280a65](https://github.com/MariaDB/server/commit/dac1280a65)\
  2020-05-28 20:54:38 +0300
  * [MDEV-18794](https://jira.mariadb.org/browse/MDEV-18794) Assertion \`!m\_innodb' failed in ha\_partition::cmp\_ref upon SELECT from partitioned table
* Merge [Revision #dad7a8ee7d](https://github.com/MariaDB/server/commit/dad7a8ee7d) 2020-05-27 17:10:39 +0300 - Merge 10.2 into 10.3
* [Revision #5139cfabb3](https://github.com/MariaDB/server/commit/5139cfabb3)\
  2020-05-27 12:59:27 +0300
  * fix compilation
* [Revision #1b3adaab25](https://github.com/MariaDB/server/commit/1b3adaab25)\
  2020-05-27 10:58:28 +0300
  * Fix the build with GCC 4.1.2
* [Revision #bf1aa7569e](https://github.com/MariaDB/server/commit/bf1aa7569e)\
  2020-05-27 09:53:36 +0300
  * Add an end-of-test marker to ease merges
* [Revision #67496281ea](https://github.com/MariaDB/server/commit/67496281ea)\
  2020-05-27 09:51:46 +0300
  * Fix the RelWithDebInfo build
* [Revision #18d8f06f31](https://github.com/MariaDB/server/commit/18d8f06f31)\
  2020-05-17 16:24:40 +0300
  * intrusive::list fixes
* [Revision #403dacf6a9](https://github.com/MariaDB/server/commit/403dacf6a9)\
  2020-05-26 20:04:47 +0300
  * Fixed crash in aria recovery when using bulk insert
* [Revision #0c1f97b3ab](https://github.com/MariaDB/server/commit/0c1f97b3ab)\
  2020-05-05 20:32:32 +0300
  * [MDEV-15152](https://jira.mariadb.org/browse/MDEV-15152) Optimistic parallel slave doesnt cope well with START SLAVE UNTIL
* Merge [Revision #451bfcd6bb](https://github.com/MariaDB/server/commit/451bfcd6bb) 2020-05-26 18:48:35 +0300 - Merge remote-tracking branch 'origin/10.1' into 10.2 to skip 10.1 dbe447a7890 commit.
* [Revision #dbe447a789](https://github.com/MariaDB/server/commit/dbe447a789)\
  2020-05-05 20:32:32 +0300
  * [MDEV-15152](https://jira.mariadb.org/browse/MDEV-15152) Optimistic parallel slave doesnt cope well with START SLAVE UNTIL
* [Revision #f1f14c2092](https://github.com/MariaDB/server/commit/f1f14c2092)\
  2020-05-26 13:14:47 +0300
  * [MDEV-20015](https://jira.mariadb.org/browse/MDEV-20015) Assertion \`!in\_use->is\_error()' failed in TABLE::update\_virtual\_field
* Merge [Revision #6a26e0c719](https://github.com/MariaDB/server/commit/6a26e0c719) 2020-05-26 13:01:34 +0300 - Merge 10.1 into 10.2
* Merge [Revision #adbf85fc89](https://github.com/MariaDB/server/commit/adbf85fc89) 2020-05-26 12:44:05 +0300 - Merge 5.5 into 10.1
* [Revision #9bbd685e8d](https://github.com/MariaDB/server/commit/9bbd685e8d)\
  2020-05-26 12:23:20 +0300
  * [MDEV-22513](https://jira.mariadb.org/browse/MDEV-22513) main.processlist\_notembedded Timeout in wait\_until\_count\_sessions
* [Revision #de13fccfc6](https://github.com/MariaDB/server/commit/de13fccfc6)\
  2020-05-11 12:50:03 -0400
  * bump the VERSION
* [Revision #76f4ae8295](https://github.com/MariaDB/server/commit/76f4ae8295)\
  2020-05-26 01:50:46 +0530
  * [MDEV-21495](https://jira.mariadb.org/browse/MDEV-21495): Conditional jump or move depends on uninitialised value in sel\_arg\_range\_seq\_next
* [Revision #fbcfbb0e1c](https://github.com/MariaDB/server/commit/fbcfbb0e1c)\
  2020-05-26 11:43:43 +0300
  * [MDEV-19751](https://jira.mariadb.org/browse/MDEV-19751) Wrong partitioning by KEY() after primary key dropped
* [Revision #4783494a5e](https://github.com/MariaDB/server/commit/4783494a5e)\
  2020-05-29 16:18:50 +0300
  * [MDEV-22283](https://jira.mariadb.org/browse/MDEV-22283) Server crashes in key\_copy or unexpected error 156
* Merge [Revision #d74e3a56e7](https://github.com/MariaDB/server/commit/d74e3a56e7) 2020-05-29 13:23:37 +0200 - Merge branch 'codership-10.4-[MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666)-v2' into 10.4
* [Revision #e04999c460](https://github.com/MariaDB/server/commit/e04999c460)\
  2020-05-26 14:01:13 +0200
  * Forgotten include files were added to check the necessary conditions for running the test
* Merge [Revision #98a2c6b69e](https://github.com/MariaDB/server/commit/98a2c6b69e) 2020-05-26 13:54:02 +0200 - Merge branch '10.4-[MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666)-v2' of [mariadb-server](https://github.com/codership/mariadb-server) into codership-10.4-[MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666)-v2
* [Revision #1af6e92f0b](https://github.com/MariaDB/server/commit/1af6e92f0b)\
  2020-05-25 14:23:42 +0300
  * [MDEV-22666](https://jira.mariadb.org/browse/MDEV-22666) galera.MW-328A hang
* [Revision #2fbf751407](https://github.com/MariaDB/server/commit/2fbf751407)\
  2020-05-29 12:00:31 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456) after-merge fix: Avoid functional change to rw\_lock\_s\_unlock()
* [Revision #57f7b4866f](https://github.com/MariaDB/server/commit/57f7b4866f)\
  2020-05-29 11:45:19 +0300
  * [MDEV-16937](https://jira.mariadb.org/browse/MDEV-16937) Strict SQL with system versioned tables causes issues (10.4)
* [Revision #278facee7c](https://github.com/MariaDB/server/commit/278facee7c)\
  2020-05-28 16:56:37 +0300
  * Added test case for query that was crashing in 10.4.13
* [Revision #ed1434df88](https://github.com/MariaDB/server/commit/ed1434df88)\
  2020-05-27 12:16:58 +0530
  * [MDEV-21787](https://jira.mariadb.org/browse/MDEV-21787) Alter table failure tries to access uninitialized column
* [Revision #fdb37d084b](https://github.com/MariaDB/server/commit/fdb37d084b)\
  2020-05-26 20:25:41 +0530
  * [MDEV-21787](https://jira.mariadb.org/browse/MDEV-21787) Alter table failure tries to access uninitialized column
* [Revision #3ad1af9366](https://github.com/MariaDB/server/commit/3ad1af9366)\
  2020-05-26 16:40:41 +0300
  * [MDEV-22545](https://jira.mariadb.org/browse/MDEV-22545): One more fix: main.perror-win
* [Revision #170487473e](https://github.com/MariaDB/server/commit/170487473e)\
  2020-05-26 15:46:09 +0300
  * After-merge fix: main.perror-win
* Merge [Revision #ca38b6e427](https://github.com/MariaDB/server/commit/ca38b6e427) 2020-05-26 11:54:55 +0300 - Merge 10.3 into 10.4
* [Revision #7476e8c7cd](https://github.com/MariaDB/server/commit/7476e8c7cd)\
  2020-05-25 21:42:26 +0530
  * [MDEV-22637](https://jira.mariadb.org/browse/MDEV-22637) Rollback of insert fails when column reorder happens
* Merge [Revision #ecc7f305dd](https://github.com/MariaDB/server/commit/ecc7f305dd) 2020-05-25 19:41:58 +0300 - Merge 10.2 into 10.3
* [Revision #5530a93f47](https://github.com/MariaDB/server/commit/5530a93f47)\
  2020-05-25 18:57:14 +0300
  * [MDEV-17092](https://jira.mariadb.org/browse/MDEV-17092) use-after-poison around lock\_trx\_handle\_wait\_low
* [Revision #e2c749380b](https://github.com/MariaDB/server/commit/e2c749380b)\
  2020-05-25 17:46:52 +0300
  * [MDEV-22545](https://jira.mariadb.org/browse/MDEV-22545) post-fix: Fix a test result
* [Revision #4a6b28c7b9](https://github.com/MariaDB/server/commit/4a6b28c7b9)\
  2020-05-05 20:44:43 +0530
  * [MDEV-22461](https://jira.mariadb.org/browse/MDEV-22461): JOIN::make\_aggr\_tables\_info(): Assertion \`select\_options & (1ULL << 17)' failed.
* [Revision #cf52dd174e](https://github.com/MariaDB/server/commit/cf52dd174e)\
  2020-05-20 13:34:51 +0200
  * [MDEV-22545](https://jira.mariadb.org/browse/MDEV-22545): my\_vsnprintf behaves not as in C standard
* [Revision #d8e2fa0c49](https://github.com/MariaDB/server/commit/d8e2fa0c49)\
  2020-05-23 14:36:33 +0300
  * Fixed compiler failure on windows
* [Revision #be647ff14d](https://github.com/MariaDB/server/commit/be647ff14d)\
  2020-05-22 18:02:24 +0300
  * Fixed deadlock with LOCK TABLES and ALTER TABLE
* [Revision #6462af1c2e](https://github.com/MariaDB/server/commit/6462af1c2e)\
  2020-05-22 15:00:29 +0400
  * [MDEV-22111](https://jira.mariadb.org/browse/MDEV-22111) ERROR 1064 & 1033 and SIGSEGV on CREATE TABLE w/ various charsets on 10.4/5 optimized builds | Assertion \`(uint) (table\_check\_constraints - share->check\_constraints) == (uint) (share->table\_check\_constraints - share->field\_check\_constraints)' failed
* Merge [Revision #bdab5b667e](https://github.com/MariaDB/server/commit/bdab5b667e) 2020-05-22 14:22:45 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #cb9c49a9b2](https://github.com/MariaDB/server/commit/cb9c49a9b2)\
  2020-05-21 18:16:27 +0400
  * [MDEV-22111](https://jira.mariadb.org/browse/MDEV-22111) ERROR 1064 & 1033 and SIGSEGV on CREATE TABLE w/ various charsets on 10.4/5 optimized builds | Assertion \`(uint) (table\_check\_constraints - share->check\_constraints) == (uint) (share->table\_check\_constraints - share->field\_check\_constraints)' failed
* [Revision #736ca14323](https://github.com/MariaDB/server/commit/736ca14323)\
  2020-05-22 15:42:11 +0300
  * Don't crash if creating sequence under XA
* [Revision #ea7830eef4](https://github.com/MariaDB/server/commit/ea7830eef4)\
  2020-05-22 16:31:16 +0400
  * [MDEV-14221](https://jira.mariadb.org/browse/MDEV-14221) Assertion \`0' failed in Item::field\_type\_for\_temporal\_comparison
* [Revision #dc22acfdb6](https://github.com/MariaDB/server/commit/dc22acfdb6)\
  2020-05-21 08:34:03 +0200
  * [MDEV-22616](https://jira.mariadb.org/browse/MDEV-22616) CHECK TABLE fails with wsrep\_trx\_fragment\_size > 0 (#1551)
* [Revision #0bf843cd13](https://github.com/MariaDB/server/commit/0bf843cd13)\
  2020-05-30 13:50:37 +0400
  * [MDEV-20366](https://jira.mariadb.org/browse/MDEV-20366) Server crashes in get\_current\_user upon SET PASSWORD via SP
* [Revision #ccdfcedf10](https://github.com/MariaDB/server/commit/ccdfcedf10)\
  2020-05-29 18:51:41 +0400
  * [MDEV-22693](https://jira.mariadb.org/browse/MDEV-22693) - InnoDB: get rid of casts for rw\_trx\_hash iterator
* [Revision #043828bdb3](https://github.com/MariaDB/server/commit/043828bdb3)\
  2020-05-29 22:47:29 +0300
  * Fixed wrong length in my\_default.c
* [Revision #df4ab26a6b](https://github.com/MariaDB/server/commit/df4ab26a6b)\
  2020-05-28 22:40:27 +0300
  * SHOW TABLE STATUS now shows if an Aria table is transactional or not
* [Revision #39dc461662](https://github.com/MariaDB/server/commit/39dc461662)\
  2020-05-29 16:49:10 +0300
  * [MDEV-22751](https://jira.mariadb.org/browse/MDEV-22751) Uninitialized tbl\_len in dict\_acquire\_mdl\_shared()
* [Revision #58f3f692b9](https://github.com/MariaDB/server/commit/58f3f692b9)\
  2020-05-29 15:43:52 +0200
  * [MDEV-22746](https://jira.mariadb.org/browse/MDEV-22746): Assertion \`(&(\&pagecache->cache\_lock)->m\_mutex)->count > 0 && pthread\_equal(pthread\_self(), (&(\&pagecache->cache\_lock)->m\_mutex)->thread)' failed in dec\_counter\_for\_resize\_op
* [Revision #32dd58e04b](https://github.com/MariaDB/server/commit/32dd58e04b)\
  2020-05-29 12:22:40 +0200
  * Removed function declaration of a non-existing function
* [Revision #213265130e](https://github.com/MariaDB/server/commit/213265130e)\
  2020-05-29 12:21:27 +0200
  * Remove some trailing whitespaces.
* [Revision #5bf9e0f875](https://github.com/MariaDB/server/commit/5bf9e0f875)\
  2020-05-29 13:41:11 +0300
  * [MDEV-22206](https://jira.mariadb.org/browse/MDEV-22206) Assertion "heap\_no == ULINT\_UNDEFINED" in trx0i\_s.cc
* [Revision #f76a1df003](https://github.com/MariaDB/server/commit/f76a1df003)\
  2020-05-29 11:57:59 +0300
  * [MDEV-21127](https://jira.mariadb.org/browse/MDEV-21127) Assertion failed in key\_text::key\_text
* [Revision #cdc2508ed1](https://github.com/MariaDB/server/commit/cdc2508ed1)\
  2020-05-29 11:07:55 +0400
  * [MDEV-22625](https://jira.mariadb.org/browse/MDEV-22625) SIGSEGV in intern\_find\_sys\_var (optimized builds)
* [Revision #c2a929185c](https://github.com/MariaDB/server/commit/c2a929185c)\
  2020-05-27 18:56:49 +0300
  * [MDEV-17491](https://jira.mariadb.org/browse/MDEV-17491) post-fix: GCC 7 -Wclass-memaccess
* [Revision #d72594d45d](https://github.com/MariaDB/server/commit/d72594d45d)\
  2020-05-27 19:38:55 +0400
  * Fixed main.implicit\_commit ASAN failure
* [Revision #2347c18c79](https://github.com/MariaDB/server/commit/2347c18c79)\
  2020-05-27 14:10:53 +0300
  * Renamed maria\_\* source files for executables to aria\_\*
* [Revision #c52e62a76f](https://github.com/MariaDB/server/commit/c52e62a76f)\
  2020-05-26 00:22:52 +0300
  * Improve logging of Aria redo's and undo's
* [Revision #514533eb9a](https://github.com/MariaDB/server/commit/514533eb9a)\
  2020-05-26 19:10:23 +0300
  * aria\_chk sets --warning-if-wrong-transid=0 if --ignore-control-file is used
* [Revision #3a37644a29](https://github.com/MariaDB/server/commit/3a37644a29)\
  2020-05-27 09:00:52 +0300
  * [MDEV-17491](https://jira.mariadb.org/browse/MDEV-17491): Use the optimized page\_id\_t more
* [Revision #5ebd6452fd](https://github.com/MariaDB/server/commit/5ebd6452fd)\
  2020-05-27 08:50:24 +0300
  * [MDEV-22697](https://jira.mariadb.org/browse/MDEV-22697): Post-push fix clang -Wnon-pod-varargs
* [Revision #03dcdad251](https://github.com/MariaDB/server/commit/03dcdad251)\
  2020-05-25 22:25:03 +0400
  * [MDEV-22697](https://jira.mariadb.org/browse/MDEV-22697) - InnoDB: remove trx->no
* [Revision #50b0ce44a2](https://github.com/MariaDB/server/commit/50b0ce44a2)\
  2020-05-16 01:13:02 +0400
  * [MDEV-22593](https://jira.mariadb.org/browse/MDEV-22593) - InnoDB: don't take trx\_sys.mutex in ReadView::open()
* [Revision #8569dac1ec](https://github.com/MariaDB/server/commit/8569dac1ec)\
  2020-05-23 13:33:26 +0200
  * allow thread\_pool\_size\_basic on Windows, in generic threadpool mode
* [Revision #e6f0371556](https://github.com/MariaDB/server/commit/e6f0371556)\
  2020-05-23 13:17:50 +0200
  * [MDEV-22696](https://jira.mariadb.org/browse/MDEV-22696) TP\_pool\_generic::set\_pool\_size logic so that it marks each connection to change group before the next socket read.
* [Revision #9aa6042a0d](https://github.com/MariaDB/server/commit/9aa6042a0d)\
  2020-05-24 17:13:12 +0200
  * [MDEV-22696](https://jira.mariadb.org/browse/MDEV-22696) Threadpool : make sure thd->event\_scheduler.data does not change as long as THD is in server\_threads.
* [Revision #17437eb259](https://github.com/MariaDB/server/commit/17437eb259)\
  2020-05-19 22:55:52 +0200
  * Threadpool - support changing group on Windows with generic thread pool
* [Revision #d8ea11a33f](https://github.com/MariaDB/server/commit/d8ea11a33f)\
  2020-05-25 09:47:35 +0300
  * [MDEV-22669](https://jira.mariadb.org/browse/MDEV-22669) fixup: WITH\_MSAN build fix
* [Revision #59f011943f](https://github.com/MariaDB/server/commit/59f011943f)\
  2020-05-24 19:29:56 +0300
  * [MDEV-22686](https://jira.mariadb.org/browse/MDEV-22686)

## Assertion \`trn' failed in ha\_maria::start\_stmt

* [Revision #6532b10040](https://github.com/MariaDB/server/commit/6532b10040)\
  2020-05-23 12:27:05 +0300
  * Fixed failure in sysvars\_server\_embedded,32bit
* [Revision #fc8359f0ac](https://github.com/MariaDB/server/commit/fc8359f0ac)\
  2020-05-22 19:10:56 +0300
  * Fixed failure in flush\_read\_lock.test
* [Revision #c779ef26b6](https://github.com/MariaDB/server/commit/c779ef26b6)\
  2020-05-21 15:33:55 +0300
  * Fixed error in galera\_vote\_rejoin\_ddl
* [Revision #f4ddde0698](https://github.com/MariaDB/server/commit/f4ddde0698)\
  2020-05-19 20:15:00 +0300
  * Only apply wsrep\_trx\_fragment\_size to InnoDB tables
* [Revision #c4bf4b7aef](https://github.com/MariaDB/server/commit/c4bf4b7aef)\
  2020-05-15 16:15:49 +0300
  * Fixed access to undefined memory found by valgrind and MSAN
* [Revision #dcc0baf540](https://github.com/MariaDB/server/commit/dcc0baf540)\
  2020-05-13 23:11:50 +0300
  * Don't print "Trying to delete tablespace several 10x times per second"
* [Revision #4ea171ffab](https://github.com/MariaDB/server/commit/4ea171ffab)\
  2020-05-12 18:56:41 +0300
  * Fixed compiler warnings from gcc and clang 5.0.1
* [Revision #9bf479b0cf](https://github.com/MariaDB/server/commit/9bf479b0cf)\
  2020-05-19 17:48:22 +0300
  * Update galera to work with independent sub transactions
* [Revision #4102f1589c](https://github.com/MariaDB/server/commit/4102f1589c)\
  2020-05-02 13:19:53 +0300
  * Aria will now register it's transactions
* [Revision #d1d472646d](https://github.com/MariaDB/server/commit/d1d472646d)\
  2020-05-04 14:20:14 +0300
  * Change THD->transaction to a pointer to enable multiple transactions
* [Revision #7ae812cf2c](https://github.com/MariaDB/server/commit/7ae812cf2c)\
  2020-04-27 18:54:13 +0300
  * Fix that BACKUP STAGE BLOCK\_COMMIT blocks commit to the Aria engine
* [Revision #b15615631f](https://github.com/MariaDB/server/commit/b15615631f)\
  2020-04-26 15:30:29 +0300
  * [MDEV-18286](https://jira.mariadb.org/browse/MDEV-18286) Assertion \`pagecache->cnt\_for\_resize\_op ...
* [Revision #7cb160961c](https://github.com/MariaDB/server/commit/7cb160961c)\
  2020-04-26 15:28:03 +0300
  * Changed debug label XXX in ma\_pagecache.cc XXX to proper lables
* [Revision #82d2dc9027](https://github.com/MariaDB/server/commit/82d2dc9027)\
  2020-05-02 13:20:24 +0300
  * Remove unneeded this-> usage from sql\_lex.cc
* [Revision #36019df323](https://github.com/MariaDB/server/commit/36019df323)\
  2020-04-30 12:06:49 +0300
  * Proper fix of User\_variables\_tracker::store
* [Revision #b1fabf6cc9](https://github.com/MariaDB/server/commit/b1fabf6cc9)\
  2020-04-28 12:00:27 +0300
  * Performance improvements to test if WSREP if active
* [Revision #93281221d1](https://github.com/MariaDB/server/commit/93281221d1)\
  2020-05-02 13:21:39 +0300
  * Don't include mysql-test/var\* files in git
* [Revision #c287dc9b04](https://github.com/MariaDB/server/commit/c287dc9b04)\
  2020-04-26 15:02:32 +0300
  * Fixed typo in variable description
* [Revision #610bb1d2c0](https://github.com/MariaDB/server/commit/610bb1d2c0)\
  2020-04-26 15:01:12 +0300
  * Fixed bug thr\_lock\_info\_init
* [Revision #8cf166bfb2](https://github.com/MariaDB/server/commit/8cf166bfb2)\
  2020-04-23 16:25:10 +0300
  * Update libmarias3 to fix a memory leak
* [Revision #51f0fa4eb3](https://github.com/MariaDB/server/commit/51f0fa4eb3)\
  2020-05-22 23:10:52 +0300
  * Cleanup: Remove a startup message
* [Revision #afdd6b1da1](https://github.com/MariaDB/server/commit/afdd6b1da1)\
  2020-05-22 20:47:04 +0300
  * [MDEV-22669](https://jira.mariadb.org/browse/MDEV-22669) InnoDB lacks CRC-32C acceleration on IA-32
* [Revision #14f1453b35](https://github.com/MariaDB/server/commit/14f1453b35)\
  2020-05-22 19:56:55 +0300
  * [MDEV-7318](https://jira.mariadb.org/browse/MDEV-7318): Fix a test case
* [Revision #b934a34c46](https://github.com/MariaDB/server/commit/b934a34c46)\
  2020-05-21 01:24:39 +0200
  * compilation failure
* Merge [Revision #9d63b63ec9](https://github.com/MariaDB/server/commit/9d63b63ec9) 2020-05-20 21:27:14 +0530 - Merge branch '10.4' into 10.5
* Merge [Revision #ce1c6dab3a](https://github.com/MariaDB/server/commit/ce1c6dab3a) 2020-05-20 21:15:43 +0530 - [MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451): SIGSEGV in memmove\_avx\_unaligned\_erms/memcpy from \_my\_b\_write on CREATE after RESET MASTER
* Merge [Revision #c7cdd049b5](https://github.com/MariaDB/server/commit/c7cdd049b5) 2020-05-20 21:02:39 +0530 - [MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451): SIGSEGV in memmove\_avx\_unaligned\_erms/memcpy from \_my\_b\_write on CREATE after RESET MASTER
* Merge [Revision #450a5b33a2](https://github.com/MariaDB/server/commit/450a5b33a2) 2020-05-20 20:49:04 +0530 - [MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451): SIGSEGV in memmove\_avx\_unaligned\_erms/memcpy from \_my\_b\_write on CREATE after RESET MASTER
* [Revision #836d708997](https://github.com/MariaDB/server/commit/836d708997)\
  2020-05-19 11:22:39 +0530
  * [MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451): SIGSEGV in memmove\_avx\_unaligned\_erms/memcpy from \_my\_b\_write on CREATE after RESET MASTER
* [Revision #a6b4d4beff](https://github.com/MariaDB/server/commit/a6b4d4beff)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
* Merge [Revision #5ece2155cb](https://github.com/MariaDB/server/commit/5ece2155cb) 2020-05-20 17:46:05 +0300 - Merge 10.4 into 10.5
* Merge [Revision #b8e694a314](https://github.com/MariaDB/server/commit/b8e694a314) 2020-05-20 17:10:12 +0300 - Merge 10.3 into 10.4
* Merge [Revision #ed41947b78](https://github.com/MariaDB/server/commit/ed41947b78) 2020-05-20 17:07:09 +0300 - Merge 10.2 into 10.3
* [Revision #22a6fa572b](https://github.com/MariaDB/server/commit/22a6fa572b)\
  2020-05-20 15:57:15 +0300
  * [MDEV-19114](https://jira.mariadb.org/browse/MDEV-19114) post-push fix: SIGSEGV on INSERT
* [Revision #ed29782a03](https://github.com/MariaDB/server/commit/ed29782a03)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
* [Revision #21e71766f6](https://github.com/MariaDB/server/commit/21e71766f6)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
* [Revision #96bc626b8f](https://github.com/MariaDB/server/commit/96bc626b8f)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
* Merge [Revision #d8dc3c72b6](https://github.com/MariaDB/server/commit/d8dc3c72b6) 2020-05-20 12:25:23 +0300 - Merge 10.3 into 10.4
* Merge [Revision #f4f0ef3e37](https://github.com/MariaDB/server/commit/f4f0ef3e37) 2020-05-20 11:41:51 +0300 - Merge 10.2 into 10.3
* Merge [Revision #e380f44742](https://github.com/MariaDB/server/commit/e380f44742) 2020-05-20 11:13:40 +0300 - Merge 10.1 into 10.2
* [Revision #6b2c8cac1b](https://github.com/MariaDB/server/commit/6b2c8cac1b)\
  2020-05-20 10:33:53 +0300
  * [MDEV-22258](https://jira.mariadb.org/browse/MDEV-22258) Limit innodb\_encryption\_threads to 255
* [Revision #7a5ba59e5f](https://github.com/MariaDB/server/commit/7a5ba59e5f)\
  2020-05-19 21:57:01 +0300
  * [MDEV-22472](https://jira.mariadb.org/browse/MDEV-22472) rpl.rpl\_fail\_register failed in buildbot with wrong result
* [Revision #395ed66b3b](https://github.com/MariaDB/server/commit/395ed66b3b)\
  2020-05-19 15:15:52 +0000
  * [MDEV-22636](https://jira.mariadb.org/browse/MDEV-22636) XML output for mtr doesn't work with valgrind option
* [Revision #e9a33a5392](https://github.com/MariaDB/server/commit/e9a33a5392)\
  2020-05-19 09:10:24 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) some test causes MTR interruption without generating summary and XML
* [Revision #1893a1370d](https://github.com/MariaDB/server/commit/1893a1370d)\
  2020-05-20 13:34:45 +0530
  * [MDEV-22633](https://jira.mariadb.org/browse/MDEV-22633) Assertion failed in prepare\_inplace\_alter\_table\_dict
* [Revision #d2900d917f](https://github.com/MariaDB/server/commit/d2900d917f)\
  2020-05-20 17:10:07 +1000
  * [MDEV-22629](https://jira.mariadb.org/browse/MDEV-22629) Remove fts\_indexes field from struct fts\_update\_t (#1537)
* [Revision #dd95935e5b](https://github.com/MariaDB/server/commit/dd95935e5b)\
  2020-05-20 09:26:05 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456) post-fix: Remove unused variable
* [Revision #ad0f85bcd2](https://github.com/MariaDB/server/commit/ad0f85bcd2)\
  2020-05-19 10:10:30 +0300
  * [MDEV-18838](https://jira.mariadb.org/browse/MDEV-18838) : galera.galera\_toi\_truncate: Test failure: mysqltest: query 'reap' succeeded - should have failed with errno 1213
* [Revision #2c4a2f2007](https://github.com/MariaDB/server/commit/2c4a2f2007)\
  2020-05-19 15:15:52 +0000
  * [MDEV-22636](https://jira.mariadb.org/browse/MDEV-22636) XML output for mtr doesn't work with valgrind option
* [Revision #d4f97e2086](https://github.com/MariaDB/server/commit/d4f97e2086)\
  2020-05-20 11:53:09 +0400
  * [MDEV-22391](https://jira.mariadb.org/browse/MDEV-22391) Assertion \`0' failed in Item\_type\_holder::val\_str on utf16 charset table query
* Merge [Revision #2bf93a8fd6](https://github.com/MariaDB/server/commit/2bf93a8fd6) 2020-05-19 21:18:15 +0300 - Merge 10.3 into 10.4
* [Revision #294ac1fbab](https://github.com/MariaDB/server/commit/294ac1fbab)\
  2020-05-19 15:15:52 +0000
  * [MDEV-22636](https://jira.mariadb.org/browse/MDEV-22636) XML output for mtr doesn't work with valgrind option
* Merge [Revision #79ed33c184](https://github.com/MariaDB/server/commit/79ed33c184) 2020-05-19 17:05:05 +0300 - Merge 10.2 into 10.3
* [Revision #a8f044e1a4](https://github.com/MariaDB/server/commit/a8f044e1a4)\
  2020-05-19 16:02:00 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456): Fix cmake -DWITH\_INNODB\_AHI=OFF
* [Revision #cb437417d2](https://github.com/MariaDB/server/commit/cb437417d2)\
  2020-05-19 12:33:47 +0300
  * [MDEV-19114](https://jira.mariadb.org/browse/MDEV-19114) gcol.innodb\_virtual\_debug: Assertion n\_fields>0 failed
* [Revision #f9144a42e7](https://github.com/MariaDB/server/commit/f9144a42e7)\
  2020-05-19 12:54:42 +0300
  * Don't run main.sp2 in emebedded server
* [Revision #996b9a9d04](https://github.com/MariaDB/server/commit/996b9a9d04)\
  2020-05-19 13:30:42 +0400
  * [MDEV-22591](https://jira.mariadb.org/browse/MDEV-22591) Debug build crashes on EXECUTE IMMEDIATE '... WHERE ?' USING IGNORE
* [Revision #0f9bfcc323](https://github.com/MariaDB/server/commit/0f9bfcc323)\
  2020-05-13 14:32:12 +0300
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): "mariadb-backup --prepare" exits with code 0 even though innodb error is logged
* Merge [Revision #a84060567c](https://github.com/MariaDB/server/commit/a84060567c) 2020-05-19 10:42:59 +0300 - Merge 10.1 into 10.2
* [Revision #44c8d84908](https://github.com/MariaDB/server/commit/44c8d84908)\
  2020-05-15 21:49:57 +0300
  * [MDEV-22520](https://jira.mariadb.org/browse/MDEV-22520) Assertion `gathered_length == thd->lex->comment.length` failed in binlog\_defragment
* [Revision #c93f8aca65](https://github.com/MariaDB/server/commit/c93f8aca65)\
  2020-05-19 10:21:16 +0300
  * [MDEV-22618](https://jira.mariadb.org/browse/MDEV-22618) Assertion !dict\_index\_is\_online\_ddl ... in lock\_table\_locks\_lookup
* [Revision #141cf43e61](https://github.com/MariaDB/server/commit/141cf43e61)\
  2020-05-18 21:49:07 +0300
  * Fixed assert in Aria on SHOW PROCEDURE STATUS
* [Revision #2e9f4cdc44](https://github.com/MariaDB/server/commit/2e9f4cdc44)\
  2020-05-19 15:43:35 +0300
  * [MDEV-21936](https://jira.mariadb.org/browse/MDEV-21936) Assertion !btr\_search\_own... in btr\_search\_drop\_page\_hash\_index
* [Revision #6b5f7ddc78](https://github.com/MariaDB/server/commit/6b5f7ddc78)\
  2020-05-19 15:15:52 +0000
  * [MDEV-22636](https://jira.mariadb.org/browse/MDEV-22636) XML output for mtr doesn't work with valgrind option
* [Revision #db6e5bd9aa](https://github.com/MariaDB/server/commit/db6e5bd9aa)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
* [Revision #12277e302e](https://github.com/MariaDB/server/commit/12277e302e)\
  2020-05-19 15:15:52 +0000
  * [MDEV-22636](https://jira.mariadb.org/browse/MDEV-22636) XML output for mtr doesn't work with valgrind option
* Merge [Revision #d2e96e492a](https://github.com/MariaDB/server/commit/d2e96e492a) 2020-05-19 14:33:08 +0300 - Merge 10.4 into 10.5
* [Revision #fa0397849a](https://github.com/MariaDB/server/commit/fa0397849a)\
  2020-05-19 14:07:34 +0300
  * Move c++ code from my\_atomic.h to my\_atomic\_wrapper.h
* [Revision #f7079d295b](https://github.com/MariaDB/server/commit/f7079d295b)\
  2020-05-19 12:40:59 +0400
  * [MDEV-22610](https://jira.mariadb.org/browse/MDEV-22610) Crash in INSERT INTO t1 (VALUES (DEFAULT) UNION VALUES (DEFAULT))
* Merge [Revision #49b29e35b2](https://github.com/MariaDB/server/commit/49b29e35b2) 2020-05-19 12:36:58 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* Merge [Revision #810b7f8ecb](https://github.com/MariaDB/server/commit/810b7f8ecb) 2020-05-19 12:03:12 +0400 - Merge remote-tracking branch 'origin/10.3' into 10.4
* [Revision #06fb78c6ac](https://github.com/MariaDB/server/commit/06fb78c6ac)\
  2020-05-18 11:29:43 +0400
  * [MDEV-21995](https://jira.mariadb.org/browse/MDEV-21995) Server crashes in Item\_field::real\_type\_handler with table value constructor
* [Revision #4869e7f4a8](https://github.com/MariaDB/server/commit/4869e7f4a8)\
  2020-05-18 16:39:38 +0200
  * [MDEV-22615](https://jira.mariadb.org/browse/MDEV-22615) system\_time\_zone may be incorrectly reported as "unknown".
* [Revision #3ea05d0842](https://github.com/MariaDB/server/commit/3ea05d0842)\
  2020-04-29 09:41:28 +1000
  * largepages: osx compile warning fix
* Merge [Revision #23047d3ed4](https://github.com/MariaDB/server/commit/23047d3ed4) 2020-05-18 17:30:02 +0300 - Merge 10.4 into 10.5
* Merge [Revision #faf6d0ef3f](https://github.com/MariaDB/server/commit/faf6d0ef3f) 2020-05-18 15:05:52 +0300 - Merge 10.3 into 10.4
* Merge [Revision #5e12aca57f](https://github.com/MariaDB/server/commit/5e12aca57f) 2020-05-18 14:10:11 +0300 - Merge 10.2 into 10.3
* [Revision #5b6bcb59ac](https://github.com/MariaDB/server/commit/5b6bcb59ac)\
  2020-05-18 14:04:31 +0300
  * [MDEV-22611](https://jira.mariadb.org/browse/MDEV-22611) Assertion btr\_search\_enabled failed during buffer pool resizing
* Merge [Revision #f0be95b5b0](https://github.com/MariaDB/server/commit/f0be95b5b0) 2020-05-18 14:09:34 +0300 - Merge 10.2 into 10.3
* [Revision #f9d8571f38](https://github.com/MariaDB/server/commit/f9d8571f38)\
  2020-05-15 18:35:19 +0200
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): galera\_sst\_mariadb-backup fails with "Failed to start mysqld.2"
* [Revision #e0ddb077d9](https://github.com/MariaDB/server/commit/e0ddb077d9)\
  2020-05-15 18:35:19 +0200
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): galera\_sst\_mariadb-backup fails with "Failed to start mysqld.2"
* Merge [Revision #03aaa7f7a1](https://github.com/MariaDB/server/commit/03aaa7f7a1) 2020-05-18 10:47:11 +0300 - Merge 10.2 into 10.3
* Merge [Revision #d0e3b0eea6](https://github.com/MariaDB/server/commit/d0e3b0eea6) 2020-05-18 09:43:58 +0300 - Merge 10.1 into 10.2
* [Revision #7baa40dffa](https://github.com/MariaDB/server/commit/7baa40dffa)\
  2020-05-18 16:37:51 +1000
  * [MDEV-21976](https://jira.mariadb.org/browse/MDEV-21976): mtr main.udf - broaden localhost (#1543)
* [Revision #c995090a53](https://github.com/MariaDB/server/commit/c995090a53)\
  2020-05-17 15:52:35 +0300
  * Travis-CI: Remove builds that always fail to make CI useful again
* [Revision #8d056affd8](https://github.com/MariaDB/server/commit/8d056affd8)\
  2020-04-05 23:55:23 +0300
  * Travis-CI: Shorten deb build log to keep it under 4 MB
* [Revision #9ddeccc299](https://github.com/MariaDB/server/commit/9ddeccc299)\
  2020-04-05 18:55:15 +0300
  * Travis-CI: Add missing build dependency dh-exec
* [Revision #4f26aea51b](https://github.com/MariaDB/server/commit/4f26aea51b)\
  2020-05-17 11:42:50 +0530
  * [MDEV-21269](https://jira.mariadb.org/browse/MDEV-21269) Parallel merging of fts index rebuild fails
* Merge [Revision #54c169a986](https://github.com/MariaDB/server/commit/54c169a986) 2020-05-16 12:28:03 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* Merge [Revision #bf8ae81269](https://github.com/MariaDB/server/commit/bf8ae81269) 2020-05-16 10:52:08 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #3df297271a](https://github.com/MariaDB/server/commit/3df297271a)\
  2020-05-15 20:16:58 +0400
  * [MDEV-22579](https://jira.mariadb.org/browse/MDEV-22579) No error when inserting DEFAULT(non\_virtual\_column) into a virtual column
* [Revision #386f168ab3](https://github.com/MariaDB/server/commit/386f168ab3)\
  2020-05-18 14:49:44 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456) after-merge fix: introduce Atomic\_relaxed
* [Revision #fde94b4cd6](https://github.com/MariaDB/server/commit/fde94b4cd6)\
  2020-05-08 11:35:15 +0300
  * [MDEV-21483](https://jira.mariadb.org/browse/MDEV-21483) : Galera MTR tests failed: galera.MW-328A galera.MW-328B
* [Revision #ea912d1605](https://github.com/MariaDB/server/commit/ea912d1605)\
  2020-05-15 18:35:19 +0200
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): galera\_sst\_mariadb-backup fails with "Failed to start mysqld.2"
* [Revision #0a5668f512](https://github.com/MariaDB/server/commit/0a5668f512)\
  2020-05-15 02:37:16 +0530
  * [MDEV-22556](https://jira.mariadb.org/browse/MDEV-22556): Incorrect result for window function when using encrypt-tmp-files=ON
* Merge [Revision #66f1e288a1](https://github.com/MariaDB/server/commit/66f1e288a1) 2020-05-16 07:54:09 +0300 - Merge 10.3 into 10.4
* Merge [Revision #38d62189a8](https://github.com/MariaDB/server/commit/38d62189a8) 2020-05-16 06:37:24 +0300 - Merge 10.2 into 10.3
* [Revision #3f12a5968a](https://github.com/MariaDB/server/commit/3f12a5968a)\
  2020-05-15 22:54:05 +0300
  * [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626): Make test more robust
* Merge [Revision #fc0960aa96](https://github.com/MariaDB/server/commit/fc0960aa96) 2020-05-15 22:37:07 +0300 - Merge 10.1 into 10.2
* [Revision #efd68f5e31](https://github.com/MariaDB/server/commit/efd68f5e31)\
  2020-05-11 19:56:14 +0530
  * [MDEV-22498](https://jira.mariadb.org/browse/MDEV-22498): SIGSEGV in Bitmap<64u>::merge on SELECT
* Merge [Revision #c8dd411781](https://github.com/MariaDB/server/commit/c8dd411781) 2020-05-15 22:18:11 +0300 - [MDEV-22544](https://jira.mariadb.org/browse/MDEV-22544) Inconsistent and Incorrect rw-lock stats
* [Revision #dcb0bd59ce](https://github.com/MariaDB/server/commit/dcb0bd59ce)\
  2020-05-14 15:05:36 +0800
  * [MDEV-22544](https://jira.mariadb.org/browse/MDEV-22544): Inconsistent and Incorrect rw-lock stats
* [Revision #85651269b6](https://github.com/MariaDB/server/commit/85651269b6)\
  2020-05-16 06:24:09 +0300
  * [MDEV-18100](https://jira.mariadb.org/browse/MDEV-18100): Clean up test
* Merge [Revision #9e6e43551f](https://github.com/MariaDB/server/commit/9e6e43551f) 2020-05-16 07:39:15 +0300 - Merge 10.3 into 10.4
* Merge [Revision #3d0bb2b7f1](https://github.com/MariaDB/server/commit/3d0bb2b7f1) 2020-05-15 19:11:57 +0300 - Merge 10.2 into 10.3
* [Revision #ad6171b91c](https://github.com/MariaDB/server/commit/ad6171b91c)\
  2020-05-15 17:10:59 +0300
  * [MDEV-22456](https://jira.mariadb.org/browse/MDEV-22456) Dropping the adaptive hash index may cause DDL to lock up InnoDB
* Merge [Revision #6a6bcc53b8](https://github.com/MariaDB/server/commit/6a6bcc53b8) 2020-05-15 17:55:01 +0300 - Merge 10.2 into 10.3
* [Revision #ff66d65a09](https://github.com/MariaDB/server/commit/ff66d65a09)\
  2020-05-15 17:09:20 +0300
  * Amend af784385b4a2b286000fa2c658e34283fe7bba60: Avoid vtable overhead
* [Revision #1cac6d4828](https://github.com/MariaDB/server/commit/1cac6d4828)\
  2020-05-14 15:24:47 +0300
  * span cleanup
* [Revision #af784385b4](https://github.com/MariaDB/server/commit/af784385b4)\
  2020-05-15 14:20:43 +0300
  * Fix for using uninitialized memory
* [Revision #277aa85c9b](https://github.com/MariaDB/server/commit/277aa85c9b)\
  2020-05-15 10:44:05 +0300
  * Fixed bugs found by valgrind
* Merge [Revision #1b16572074](https://github.com/MariaDB/server/commit/1b16572074) 2020-05-14 17:48:06 +0300 - Merge 10.1 into 10.2
* [Revision #ee5152fc4b](https://github.com/MariaDB/server/commit/ee5152fc4b)\
  2020-05-14 17:41:37 +0300
  * [MDEV-22070](https://jira.mariadb.org/browse/MDEV-22070) MSAN use-of-uninitialized-value in encryption.innodb-redo-badkey
* [Revision #fc58c17216](https://github.com/MariaDB/server/commit/fc58c17216)\
  2020-05-14 12:06:25 +0300
  * [MDEV-21336](https://jira.mariadb.org/browse/MDEV-21336) Memory leaks related to innodb\_debug\_sync
* [Revision #a12aed0398](https://github.com/MariaDB/server/commit/a12aed0398)\
  2020-05-14 10:55:32 +0300
  * Fix GCC 9.3.0 -Wunused-but-set-variable
* [Revision #7d51c35988](https://github.com/MariaDB/server/commit/7d51c35988)\
  2020-05-14 09:06:38 +0300
  * Fix GCC -Wnonnull
* [Revision #11147bea20](https://github.com/MariaDB/server/commit/11147bea20)\
  2020-05-14 09:05:04 +0300
  * Fix GCC -Wstringop-truncation
* [Revision #3c773cd855](https://github.com/MariaDB/server/commit/3c773cd855)\
  2020-05-14 13:35:52 +0300
  * [MDEV-19622](https://jira.mariadb.org/browse/MDEV-19622): Fix a TokuDB result
* Merge [Revision #4f29d776c7](https://github.com/MariaDB/server/commit/4f29d776c7) 2020-05-16 06:27:55 +0300 - Merge 10.3 into 10.4
* [Revision #3eadb135fd](https://github.com/MariaDB/server/commit/3eadb135fd)\
  2020-05-15 11:51:31 +0300
  * Fixed access to uninitalized memory found by valgrind
* [Revision #a7c4e85dd6](https://github.com/MariaDB/server/commit/a7c4e85dd6)\
  2020-05-15 11:50:59 +0300
  * Use history.h include file if readline is used
* [Revision #d49233caf6](https://github.com/MariaDB/server/commit/d49233caf6)\
  2020-05-14 18:38:49 +0530
  * [MDEV-18100](https://jira.mariadb.org/browse/MDEV-18100): User defined aggregate functions not working correctly when the schema is changed
* [Revision #1408e26d0b](https://github.com/MariaDB/server/commit/1408e26d0b)\
  2020-05-15 06:15:10 +0400
  * [MDEV-22560](https://jira.mariadb.org/browse/MDEV-22560) Crash on a table value constructor with an SP variable
* Merge [Revision #f7cf60991d](https://github.com/MariaDB/server/commit/f7cf60991d) 2020-05-14 12:33:22 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* Merge [Revision #4dc690dc28](https://github.com/MariaDB/server/commit/4dc690dc28) 2020-05-14 11:57:47 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #31f34b20f3](https://github.com/MariaDB/server/commit/31f34b20f3)\
  2020-05-14 11:41:27 +0400
  * [MDEV-22502](https://jira.mariadb.org/browse/MDEV-22502) MDB crashes in CREATE TABLE AS SELECT when the precision of returning type = 0.
* Merge [Revision #ef65c39ab3](https://github.com/MariaDB/server/commit/ef65c39ab3) 2020-05-14 10:01:54 +0400 - Merge remote-tracking branch 'origin/10.2' into 10.3
* Merge [Revision #f827ba3b84](https://github.com/MariaDB/server/commit/f827ba3b84) 2020-05-14 08:44:34 +0400 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #910c31928e](https://github.com/MariaDB/server/commit/910c31928e)\
  2020-05-13 18:46:28 +0400
  * [MDEV-22503](https://jira.mariadb.org/browse/MDEV-22503) MDB limits DECIMAL column precision to 16 doing CTAS with floor/ceil over DECIMAL(X,Y) where X > 16
* [Revision #edbf124515](https://github.com/MariaDB/server/commit/edbf124515)\
  2020-05-13 23:30:34 +0300
  * Ensure that auto\_increment fields are marked properly on update
* [Revision #f86d97c3fe](https://github.com/MariaDB/server/commit/f86d97c3fe)\
  2020-05-18 13:00:03 +0000
  * Compiling - improve multithreaded build
* [Revision #8eed9a4648](https://github.com/MariaDB/server/commit/8eed9a4648)\
  2020-05-18 11:10:35 +0000
  * [MDEV-22613](https://jira.mariadb.org/browse/MDEV-22613) Windows - reduce package size
* [Revision #21321fcbbd](https://github.com/MariaDB/server/commit/21321fcbbd)\
  2020-05-18 11:05:23 +0000
  * Windows : small cmake cleanup
* [Revision #1f952df44a](https://github.com/MariaDB/server/commit/1f952df44a)\
  2020-05-18 11:00:28 +0000
  * [MDEV-22612](https://jira.mariadb.org/browse/MDEV-22612) Fix -DWITH\_ASAN=1 on Windows.
* [Revision #9f8e555895](https://github.com/MariaDB/server/commit/9f8e555895)\
  2020-05-18 10:55:40 +0000
  * Fix clang-cl warning
* [Revision #9f294644c4](https://github.com/MariaDB/server/commit/9f294644c4)\
  2020-05-15 18:35:19 +0200
  * [MDEV-22554](https://jira.mariadb.org/browse/MDEV-22554): galera\_sst\_mariadb-backup fails with "Failed to start mysqld.2"
* [Revision #5d85bc08c6](https://github.com/MariaDB/server/commit/5d85bc08c6)\
  2020-05-16 11:48:26 +0300
  * [MDEV-21976](https://jira.mariadb.org/browse/MDEV-21976): Re-disable main.udf, reverts mistake in merge b30a01314217
* [Revision #91446c822f](https://github.com/MariaDB/server/commit/91446c822f)\
  2020-05-04 20:45:18 +0300
  * Deb: Create empty migrated-from-my.cnf-settings.conf for Buildbot tests
* [Revision #dab5698b3c](https://github.com/MariaDB/server/commit/dab5698b3c)\
  2020-04-09 21:23:25 +0300
  * Deb: Stop using mariadb-service-convert
* [Revision #69964c4425](https://github.com/MariaDB/server/commit/69964c4425)\
  2020-04-22 00:48:14 +0300
  * Deb: Add manually dh\_systemd\_start snippets
* [Revision #764dd39ca7](https://github.com/MariaDB/server/commit/764dd39ca7)\
  2020-04-26 10:41:21 +0300
  * Deb: Add support for legacy init systems again
* [Revision #69077dea25](https://github.com/MariaDB/server/commit/69077dea25)\
  2020-05-15 16:09:13 +0200
  * [MDEV-22578](https://jira.mariadb.org/browse/MDEV-22578) thread\_pool\_info crashes with clang6, using SSE instructions on unaligned memory
* Merge [Revision #f2a944516e](https://github.com/MariaDB/server/commit/f2a944516e) 2020-05-15 17:13:35 +0300 - Merge 10.4 into 10.5
* [Revision #a4996f951d](https://github.com/MariaDB/server/commit/a4996f951d)\
  2020-05-15 16:17:15 +0300
  * [MDEV-22563](https://jira.mariadb.org/browse/MDEV-22563) Segfault on duplicate free of Item\_func\_in::array
* [Revision #72789e4b2b](https://github.com/MariaDB/server/commit/72789e4b2b)\
  2020-05-15 15:14:08 +0300
  * Fixed access to not initalized memory
* [Revision #523d67a272](https://github.com/MariaDB/server/commit/523d67a272)\
  2020-05-14 09:17:14 +0300
  * [MDEV-22494](https://jira.mariadb.org/browse/MDEV-22494) : Galera assertion lock\_sys.mutex.is\_owned() at lock\_trx\_handle\_wait\_low
* [Revision #3bfe305c5c](https://github.com/MariaDB/server/commit/3bfe305c5c)\
  2020-05-14 15:46:17 +0200
  * [MDEV-22555](https://jira.mariadb.org/browse/MDEV-22555) Windows, packaging: binaries depend on vcruntime140\_1.dll, which is not in MSI
* [Revision #3b251e24b6](https://github.com/MariaDB/server/commit/3b251e24b6)\
  2020-05-13 13:42:32 +0200
  * Revert "Added --titlebar option to enable/disable the titlebar"
* Merge [Revision #b30a013142](https://github.com/MariaDB/server/commit/b30a013142) 2020-05-13 14:25:06 +0300 - Merge 10.4 into 10.5
* Merge [Revision #38f6c47f8a](https://github.com/MariaDB/server/commit/38f6c47f8a) 2020-05-13 12:52:57 +0300 - Merge 10.3 into 10.4
* Merge [Revision #15fa70b840](https://github.com/MariaDB/server/commit/15fa70b840) 2020-05-13 11:45:05 +0300 - Merge 10.2 into 10.3
* Merge [Revision #6bc4444d7c](https://github.com/MariaDB/server/commit/6bc4444d7c) 2020-05-13 11:12:31 +0300 - Merge 10.1 into 10.2
* Merge [Revision #23d3d180ca](https://github.com/MariaDB/server/commit/23d3d180ca) 2020-05-11 19:09:46 +0200 - Merge branch '10.1-release' into 10.1
* [Revision #a0778860af](https://github.com/MariaDB/server/commit/a0778860af)\
  2020-05-11 12:52:53 -0400
  * bump the VERSION
* [Revision #1887b5ae87](https://github.com/MariaDB/server/commit/1887b5ae87)\
  2020-05-08 13:27:57 +0300
  * [MDEV-22501](https://jira.mariadb.org/browse/MDEV-22501) Various issues when using --innodb-data-file-size-debug=-1
* [Revision #26aab96ecf](https://github.com/MariaDB/server/commit/26aab96ecf)\
  2020-05-07 20:44:33 +0300
  * [MDEV-22497](https://jira.mariadb.org/browse/MDEV-22497) \[ERROR] InnoDB: Unable to purge a record
* [Revision #8c4b526121](https://github.com/MariaDB/server/commit/8c4b526121)\
  2020-05-07 00:40:48 +0200
  * Windows, mtr : Fix "Subroutine HAVE\_WIN32\_CONSOLE redefined at (eval 25) line 1."
* [Revision #f7ba675555](https://github.com/MariaDB/server/commit/f7ba675555)\
  2020-05-06 18:14:26 +0200
  * [MDEV-22344](https://jira.mariadb.org/browse/MDEV-22344): Fix typos in comments
* [Revision #1af74d523a](https://github.com/MariaDB/server/commit/1af74d523a)\
  2020-05-05 12:49:29 +0200
  * postfix after e3f5789ac0b2 - var/log/stdout.log contains escape sequences.
* [Revision #95fa7bc89d](https://github.com/MariaDB/server/commit/95fa7bc89d)\
  2020-05-04 10:10:07 +0000
  * [MDEV-22273](https://jira.mariadb.org/browse/MDEV-22273) jUnit patch: xml test result differs from MTR output in case if retry
* [Revision #dc2a858bed](https://github.com/MariaDB/server/commit/dc2a858bed)\
  2020-04-17 08:28:31 +0000
  * [MDEV-22270](https://jira.mariadb.org/browse/MDEV-22270) JUnit patch: test name contains classname
* [Revision #218d20ffe3](https://github.com/MariaDB/server/commit/218d20ffe3)\
  2020-05-12 13:57:09 +0300
  * [MDEV-22398](https://jira.mariadb.org/browse/MDEV-22398): mariadb-backup.innodb\_xa\_rollback fails on repeat
* [Revision #0e6a5786d4](https://github.com/MariaDB/server/commit/0e6a5786d4)\
  2020-05-12 10:13:16 +0300
  * Cleanup: Remove InnoDB wrappers of thd\_charset(), thd\_query\_safe()
* [Revision #a2560b0077](https://github.com/MariaDB/server/commit/a2560b0077)\
  2020-05-12 10:13:00 +0300
  * [MDEV-22529](https://jira.mariadb.org/browse/MDEV-22529) thd\_query\_safe() isn’t, causing InnoDB to hang
* Merge [Revision #b57c6cb394](https://github.com/MariaDB/server/commit/b57c6cb394) 2020-05-11 19:53:35 +0200 - Merge branch '10.2-release' into 10.2
* [Revision #37759b262f](https://github.com/MariaDB/server/commit/37759b262f)\
  2020-05-11 12:55:06 -0400
  * bump the VERSION
* [Revision #ba3d58ad4c](https://github.com/MariaDB/server/commit/ba3d58ad4c)\
  2020-05-11 14:23:37 +0300
  * [MDEV-22523](https://jira.mariadb.org/browse/MDEV-22523) index->rtr\_ssn.mutex is wasting memory
* [Revision #4ae778bbec](https://github.com/MariaDB/server/commit/4ae778bbec)\
  2020-05-04 17:39:50 +0200
  * innodb: add space between thread name and "to exit" text
* [Revision #faf6f8c6a4](https://github.com/MariaDB/server/commit/faf6f8c6a4)\
  2020-05-08 16:39:37 +0300
  * Add global suppression for connectivity problems.
* [Revision #0b218df072](https://github.com/MariaDB/server/commit/0b218df072)\
  2020-05-08 14:11:41 +0200
  * [MDEV-22483](https://jira.mariadb.org/browse/MDEV-22483) mysql\_upgrade does not use current user as default for connecting to server
* [Revision #748fb55093](https://github.com/MariaDB/server/commit/748fb55093)\
  2020-05-08 11:35:15 +0300
  * [MDEV-21483](https://jira.mariadb.org/browse/MDEV-21483) : Galera MTR tests failed: galera.MW-328A galera.MW-328B
* [Revision #40d0b64167](https://github.com/MariaDB/server/commit/40d0b64167)\
  2020-05-08 09:13:47 +0300
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #0dee57c6f5](https://github.com/MariaDB/server/commit/0dee57c6f5)\
  2020-05-07 21:01:22 +0300
  * [MDEV-19344](https://jira.mariadb.org/browse/MDEV-19344) innodb.innodb-change-buffer-recovery fails
* [Revision #e6301d8f67](https://github.com/MariaDB/server/commit/e6301d8f67)\
  2020-05-06 17:23:49 +0300
  * [MDEV-21515](https://jira.mariadb.org/browse/MDEV-21515) : Galera test sporadic failure on galera.galera\_wsrep\_new\_cluster: Result content mismatch
* [Revision #2907ff2c2d](https://github.com/MariaDB/server/commit/2907ff2c2d)\
  2020-04-29 17:19:54 +0300
  * [MDEV-19741](https://jira.mariadb.org/browse/MDEV-19741) : Galera test failure on galera.galera\_sst\_mariadb-backup\_table\_options
* [Revision #06b245f768](https://github.com/MariaDB/server/commit/06b245f768)\
  2020-05-05 15:35:58 +0530
  * [MDEV-13266](https://jira.mariadb.org/browse/MDEV-13266): Race condition in ANALYZE TABLE / statistics collection
* [Revision #b9f177f66a](https://github.com/MariaDB/server/commit/b9f177f66a)\
  2020-05-05 08:54:33 +0300
  * [MDEV-11254](https://jira.mariadb.org/browse/MDEV-11254) cleanup: Remove buf\_page\_t::write\_size
* Merge [Revision #19d4e023c6](https://github.com/MariaDB/server/commit/19d4e023c6) 2020-05-11 20:27:44 +0200 - Merge branch '10.3-release' into 10.3
* [Revision #9f5ab66b72](https://github.com/MariaDB/server/commit/9f5ab66b72)\
  2020-05-11 12:57:01 -0400
  * bump the VERSION
* [Revision #d01d94d77b](https://github.com/MariaDB/server/commit/d01d94d77b)\
  2020-05-06 23:44:34 +0300
  * [MDEV-17568](https://jira.mariadb.org/browse/MDEV-17568): LATERAL DERIVED is not clearly visible in EXPLAIN FORMAT=JSON
* [Revision #9f20968169](https://github.com/MariaDB/server/commit/9f20968169)\
  2020-05-12 19:45:21 +0400
  * [MDEV-20261](https://jira.mariadb.org/browse/MDEV-20261) NULL passed to String::eq, SEGV, server crash, regression in 10.4
* Merge [Revision #db537a8372](https://github.com/MariaDB/server/commit/db537a8372) 2020-05-11 21:32:33 +0200 - Merge branch '10.4-release' into 10.4
* [Revision #15502e5e33](https://github.com/MariaDB/server/commit/15502e5e33)\
  2020-05-11 01:00:15 +0200
  * [MDEV-21965](https://jira.mariadb.org/browse/MDEV-21965) main.tls\_version and main.tls\_version1 fail in buildbot on Ubuntu Focal
* [Revision #6e99974d6e](https://github.com/MariaDB/server/commit/6e99974d6e)\
  2020-05-11 12:59:25 -0400
  * bump the VERSION
* [Revision #6adb0d2f7c](https://github.com/MariaDB/server/commit/6adb0d2f7c)\
  2020-05-08 18:20:38 +0200
  * [MDEV-22459](https://jira.mariadb.org/browse/MDEV-22459) pam v2 should log an error if auth\_pam\_tool exec fails
* [Revision #a878344ee5](https://github.com/MariaDB/server/commit/a878344ee5)\
  2020-05-08 09:16:37 +0300
  * [MDEV-21421](https://jira.mariadb.org/browse/MDEV-21421) : Galera test sporadic failure on galera.galera\_as\_slave\_gtid\_myisam: Result length mismatch
* [Revision #057a700a2a](https://github.com/MariaDB/server/commit/057a700a2a)\
  2020-05-07 14:23:33 +0300
  * [MDEV-22466](https://jira.mariadb.org/browse/MDEV-22466) : Galera missing .test or .result files
* [Revision #8d3795f173](https://github.com/MariaDB/server/commit/8d3795f173)\
  2020-05-07 00:53:16 +0200
  * [MDEV-22487](https://jira.mariadb.org/browse/MDEV-22487) WolfSSL - server prints "Please supply a buffer for error string"
* Merge [Revision #0186b0a077](https://github.com/MariaDB/server/commit/0186b0a077) 2020-05-12 15:58:15 +0300 - Merge mariadb-10.5.3 into 10.5
* [Revision #9810e0a722](https://github.com/MariaDB/server/commit/9810e0a722)\
  2020-05-12 07:32:03 -0400
  * bump the VERSION
* [Revision #cfe5ee90c8](https://github.com/MariaDB/server/commit/cfe5ee90c8)\
  2020-05-07 19:20:17 +0400
  * [MDEV-22043](https://jira.mariadb.org/browse/MDEV-22043) Special character leads to assertion in my\_wc\_to\_printable\_generic on 10.5.2 (debug)
* [Revision #c675886dcd](https://github.com/MariaDB/server/commit/c675886dcd)\
  2020-05-09 12:50:50 +0300
  * Added --titlebar option to enable/disable the titlebar
* [Revision #b99c3b20c9](https://github.com/MariaDB/server/commit/b99c3b20c9)\
  2020-05-09 12:46:33 +0300
  * Fixed test failure in parts.partition\_debug\_innodb/myisam

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
