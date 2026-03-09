# MariaDB 10.1.20 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.20)[Release Notes](../../old-releases/10.1/10.1.20.md)[Changelog](mariadb-10120-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 15 Dec 2016

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.20.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #c13b501](https://github.com/MariaDB/server/commit/c13b501)\
  2016-12-14 19:20:17 +0000
  * Fix broken cmake -DBUILD\_CONFIG=mysql\_release on Windows.
* [Revision #d93bbca](https://github.com/MariaDB/server/commit/d93bbca)\
  2016-12-14 20:13:36 +0530
  * [MDEV-11479](https://jira.mariadb.org/browse/MDEV-11479) Improved wsrep\_dirty\_reads - Updated sysvars\_wsrep.result file
* [Revision #f41bd7e](https://github.com/MariaDB/server/commit/f41bd7e)\
  2016-12-13 05:07:02 +0530
  * [MDEV-11060](https://jira.mariadb.org/browse/MDEV-11060) sql/protocol.cc:532: void Protocol::end\_statement(): Assertion \`0' failed
* [Revision #0c79de2](https://github.com/MariaDB/server/commit/0c79de2)\
  2016-12-14 09:30:43 +0530
  * [MDEV-11479](https://jira.mariadb.org/browse/MDEV-11479) Improved wsrep\_dirty\_reads
* [Revision #25a9a3d](https://github.com/MariaDB/server/commit/25a9a3d)\
  2016-12-14 08:39:36 +0530
  * Revert "[MDEV-11016](https://jira.mariadb.org/browse/MDEV-11016) wsrep\_node\_is\_ready() check is too strict"
* [Revision #72cc73c](https://github.com/MariaDB/server/commit/72cc73c)\
  2016-12-13 11:51:33 +0200
  * [MDEV-10368](https://jira.mariadb.org/browse/MDEV-10368): get\_latest\_version() called too often
* [Revision #67b570a](https://github.com/MariaDB/server/commit/67b570a)\
  2016-12-05 20:58:49 -0500
  * [MDEV-10545](https://jira.mariadb.org/browse/MDEV-10545): Server crashed in my\_copy\_fix\_mb on querying I\_S and P\_S tables
* [Revision #9c88a54](https://github.com/MariaDB/server/commit/9c88a54)\
  2016-12-05 20:07:30 -0500
  * [MDEV-11179](https://jira.mariadb.org/browse/MDEV-11179): WSREP transaction excceded size limit in Galera cluster
* [Revision #dbb06d2](https://github.com/MariaDB/server/commit/dbb06d2)\
  2016-11-21 19:44:48 -0500
  * [MDEV-10954](https://jira.mariadb.org/browse/MDEV-10954): MariaDB Galera: wsrep\_sst\_common: line 120: which: command not found
* [Revision #5d9ca52](https://github.com/MariaDB/server/commit/5d9ca52)\
  2016-12-12 00:59:40 +0200
  * Updated the list of unstable tests after the merge
* [Revision #2f20d29](https://github.com/MariaDB/server/commit/2f20d29) 2016-12-11 09:53:42 +0100 - Merge branch '10.0' into 10.1
* [Revision #eb4f2e0](https://github.com/MariaDB/server/commit/eb4f2e0)\
  2016-12-10 22:19:09 +0200
  * [MDEV-11533](https://jira.mariadb.org/browse/MDEV-11533): Roles with trailing white spaces are not cleared correctly
* [Revision #3e8155c](https://github.com/MariaDB/server/commit/3e8155c) 2016-12-09 16:33:48 +0100 - Merge branch '5.5' into 10.0
* [Revision #03dabfa](https://github.com/MariaDB/server/commit/03dabfa)\
  2016-12-08 22:54:58 +0100
  * [MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in handler::increment\_statistics or in make\_select or assertion failure pfs\_thread == ((PFS\_thread\*) pthread\_getspecific((THR\_PFS)))
* [Revision #ab65db6](https://github.com/MariaDB/server/commit/ab65db6)\
  2016-12-08 21:03:45 +0100
  * Revert "[MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in handler::increment\_statistics or in make\_select or assertion failure pfs\_thread == ((PFS\_thread\*) pthread\_getspecific((THR\_PFS)))"
* [Revision #f5e0522](https://github.com/MariaDB/server/commit/f5e0522)\
  2016-12-07 13:06:14 +0100
  * [MDEV-10388](https://jira.mariadb.org/browse/MDEV-10388) [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md).x keeps (deleted) ML\* files in tmpdir after LOAD DATA completes
* [Revision #1d702ff](https://github.com/MariaDB/server/commit/1d702ff)\
  2016-12-07 14:42:08 +0400
  * [MDEV-8329](https://jira.mariadb.org/browse/MDEV-8329) MariaDB crashes when replicate\_wild\_ignore\_table is set to NULL.
* [Revision #d67ef7a](https://github.com/MariaDB/server/commit/d67ef7a)\
  2016-12-05 17:37:54 +0100
  * [MDEV-10663](https://jira.mariadb.org/browse/MDEV-10663): Use of Inline table columns in HAVING clause throws 1463 Error
* [Revision #035a5ac](https://github.com/MariaDB/server/commit/035a5ac)\
  2016-09-26 18:15:11 +0200
  * [MDEV-10713](https://jira.mariadb.org/browse/MDEV-10713): signal 11 error on multi-table update - crash in handler::increment\_statistics or in make\_select or assertion failure pfs\_thread == ((PFS\_thread\*) pthread\_getspecific((THR\_PFS)))
* [Revision #f988bce](https://github.com/MariaDB/server/commit/f988bce)\
  2016-09-21 18:36:34 +0200
  * [MDEV-10776](https://jira.mariadb.org/browse/MDEV-10776): Server crash on query
* [Revision #46dee0d](https://github.com/MariaDB/server/commit/46dee0d)\
  2016-12-05 16:50:12 +0400
  * [MDEV-10717](https://jira.mariadb.org/browse/MDEV-10717) Assertion \`!null\_value' failed in virtual bool Item::send(Protocol\*, String\*)
* [Revision #18cdff6](https://github.com/MariaDB/server/commit/18cdff6)\
  2016-12-04 12:37:01 +0100
  * [MDEV-10293](https://jira.mariadb.org/browse/MDEV-10293) 'setupterm' was not declared in this scope
* [Revision #02d153c](https://github.com/MariaDB/server/commit/02d153c)\
  2016-06-26 13:37:27 +0200
  * str2decimal: don't return a negative zero
* [Revision #4a3acbc](https://github.com/MariaDB/server/commit/4a3acbc)\
  2016-12-02 00:19:49 +0100
  * [MDEV-11241](https://jira.mariadb.org/browse/MDEV-11241) Certain combining marks cause MariaDB to crash when doing Full-Text searches
* [Revision #0a4b508](https://github.com/MariaDB/server/commit/0a4b508)\
  2016-12-01 20:04:36 +0100
  * [MDEV-11242](https://jira.mariadb.org/browse/MDEV-11242) MariaDB Server releases contains promotion of MariaDB Corporation
* [Revision #f640527](https://github.com/MariaDB/server/commit/f640527)\
  2016-12-02 15:22:11 +0100
  * typo fixed: s/MSYQL/MYSQL/
* [Revision #9976223](https://github.com/MariaDB/server/commit/9976223)\
  2016-11-28 17:28:37 +0400
  * [MDEV-11171](https://jira.mariadb.org/browse/MDEV-11171) Assertion \`m\_cpp\_buf <= ptr && ptr <= m\_cpp\_buf + m\_buf\_length' failed in Lex\_input\_stream::body\_utf8\_append(const char\*, const char\*)
* [Revision #adc38ed](https://github.com/MariaDB/server/commit/adc38ed)\
  2016-11-14 08:02:35 +0100
  * Restore MY\_WME flag for my\_pread in read\_ddl\_log\_entry, fix errors in buildbot
* [Revision #96b62b5](https://github.com/MariaDB/server/commit/96b62b5)\
  2016-11-11 20:55:03 -0800
  * Fixed bug [MDEV-11161](https://jira.mariadb.org/browse/MDEV-11161). The flag TABLE\_LIST::fill\_me must be reset to false at the prepare phase for any materialized derived table used in the executed query. Otherwise if the optimizer decides to generate a key for such a table it is generated only for the first execution of the query.
* [Revision #10aee66](https://github.com/MariaDB/server/commit/10aee66)\
  2016-11-10 23:47:42 +0000
  * [MDEV-11248](https://jira.mariadb.org/browse/MDEV-11248) Fix passing offset parameter to my\_file\_pread in read\_ddl\_log\_file\_entry
* [Revision #e0f48e5](https://github.com/MariaDB/server/commit/e0f48e5)\
  2016-11-03 16:21:48 +0000
  * [MDEV-11214](https://jira.mariadb.org/browse/MDEV-11214) Windows : MSI installation fails, if run by a service user (e.g LocalSystem)
* [Revision #2a2e79b](https://github.com/MariaDB/server/commit/2a2e79b)\
  2016-10-27 13:03:49 +0000
  * [MDEV-11157](https://jira.mariadb.org/browse/MDEV-11157) Windows - Upgrade installer to use HeidiSQL 9.4
* [Revision #d8cb682](https://github.com/MariaDB/server/commit/d8cb682)\
  2016-10-26 21:54:41 +0000
  * VS2015 build fixes
* [Revision #aec4321](https://github.com/MariaDB/server/commit/aec4321)\
  2016-10-26 21:38:58 +0000
  * [MDEV-9409](https://jira.mariadb.org/browse/MDEV-9409) Windows - workaround VS2015 CRT bug that makes mysqldump/mysql\_install\_db.exe fail
* [Revision #106664f](https://github.com/MariaDB/server/commit/106664f)\
  2016-12-08 02:03:34 +0530
  * [MDEV-11162](https://jira.mariadb.org/browse/MDEV-11162) Assertion \`num\_records == m\_idx\_array.size()' failed in Filesort\_buffer::alloc\_sort\_buffer(uint, uint)
* [Revision #822fb79](https://github.com/MariaDB/server/commit/822fb79)\
  2016-12-07 23:44:52 +0530
  * [MDEV-11162](https://jira.mariadb.org/browse/MDEV-11162) Assertion \`num\_records == m\_idx\_array.size()' failed in Filesort\_buffer::alloc\_sort\_buffer(uint, uint)
* [Revision #c32d3e1](https://github.com/MariaDB/server/commit/c32d3e1)\
  2016-12-07 18:05:13 +0400
  * [MDEV-10787](https://jira.mariadb.org/browse/MDEV-10787) Assertion \`ltime->neg == 0' failed in void date\_to\_datetime(MYSQL\_TIME\*)
* [Revision #52b590b](https://github.com/MariaDB/server/commit/52b590b) 2016-12-07 10:04:10 +0400 - Merge pull request #271 from iangilfillan/10.0
* [Revision #3ada316969](https://github.com/MariaDB/server/commit/3ada316969)\
  2016-12-06 13:18:48 +0200
  * Update mysqldump man page
* [Revision #7f2fd34](https://github.com/MariaDB/server/commit/7f2fd34)\
  2016-12-02 14:34:45 +0100
  * [MDEV-11231](https://jira.mariadb.org/browse/MDEV-11231) Server crashes in check\_duplicate\_key on CREATE TABLE ... SELECT
* [Revision #c5ef621](https://github.com/MariaDB/server/commit/c5ef621) 2016-12-04 01:59:08 +0100 - Merge branch 'merge/merge-tokudb-5.6' into 10.0
* [Revision #d4f0686](https://github.com/MariaDB/server/commit/d4f0686)\
  2016-12-02 10:24:00 +0100
  * 5.6.34-79.1
* [Revision #f35b0d8](https://github.com/MariaDB/server/commit/f35b0d8) 2016-12-04 01:37:55 +0100 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #7436c3d](https://github.com/MariaDB/server/commit/7436c3d)\
  2016-12-02 10:22:18 +0100
  * 5.6.34-79.1
* [Revision #e4a0d75](https://github.com/MariaDB/server/commit/e4a0d75)\
  2016-12-04 01:35:57 +0100
  * import a test case from percona-server-5.6.34-79.1
* [Revision #e99990c](https://github.com/MariaDB/server/commit/e99990c)\
  2016-10-28 17:10:05 +0200
  * [MDEV-10744](https://jira.mariadb.org/browse/MDEV-10744): Roles are not fully case sensitive
* [Revision #525e214](https://github.com/MariaDB/server/commit/525e214)\
  2016-10-25 16:47:36 +0200
  * Remove labs() warning from maria and myisam storage engines
* [Revision #748d993](https://github.com/MariaDB/server/commit/748d993)\
  2016-11-29 11:28:15 -0800
  * Fixed bug [MDEV-11364](https://jira.mariadb.org/browse/MDEV-11364). The function Item\_func\_isnull::update\_used\_tables() must handle the case when the predicate is over not nullable column in a special way. This is actually a bug of [MariaDB 5.3](../../old-releases/5.3/changes-improvements-in-mariadb-5-3.md)/5.5, but it's probably hard to demonstrate that it can cause problems there.
* [Revision #b209bc3](https://github.com/MariaDB/server/commit/b209bc3)\
  2016-11-29 09:01:46 +0200
  * [MDEV-10427](https://jira.mariadb.org/browse/MDEV-10427): innodb.innodb-wl5522-debug-zip fails sporadically in buildbot
* [Revision #dd0ff30](https://github.com/MariaDB/server/commit/dd0ff30)\
  2016-11-29 06:51:12 +0400
  * [MDEV-11343](https://jira.mariadb.org/browse/MDEV-11343) LOAD DATA INFILE fails to load data with an escape character followed by a multi-byte character
* [Revision #099ce1d](https://github.com/MariaDB/server/commit/099ce1d)\
  2016-11-25 15:59:47 +0400
  * [MDEV-11348](https://jira.mariadb.org/browse/MDEV-11348) LOAD DATA LOCAL INFILE crashes the server on loading a backslash followed by a multi-byte character
* [Revision #03ddc19](https://github.com/MariaDB/server/commit/03ddc19)\
  2016-11-17 15:15:20 +0200
  * [MDEV-6424](https://jira.mariadb.org/browse/MDEV-6424): MariaDB server crashes with assertion failure in file ha\_innodb.c line 11652
* [Revision #42a398b](https://github.com/MariaDB/server/commit/42a398b)\
  2016-11-17 12:04:39 +0400
  * Fixing a typo in the patch for [MDEV-10780](https://jira.mariadb.org/browse/MDEV-10780), which caused default.test failure.
* [Revision #390f2a0](https://github.com/MariaDB/server/commit/390f2a0)\
  2016-11-16 11:00:38 +0100
  * Fix incorrect reading of events from relaylog in parallel replication.
* [Revision #f1fcc1f](https://github.com/MariaDB/server/commit/f1fcc1f)\
  2016-11-15 23:00:11 +0100
  * Back-port Master\_info::using\_parallel() to 10.0.
* [Revision #9a09072](https://github.com/MariaDB/server/commit/9a09072) 2016-11-15 11:08:01 +0100 - Merge branch 'mdev10863' into 10.0
* [Revision #1d9b043](https://github.com/MariaDB/server/commit/1d9b043)\
  2016-11-10 18:15:36 +0400
  * A join patch for [MDEV-10780](https://jira.mariadb.org/browse/MDEV-10780) and [MDEV-11265](https://jira.mariadb.org/browse/MDEV-11265)
* [Revision #9741e0e](https://github.com/MariaDB/server/commit/9741e0e)\
  2016-11-01 07:52:28 +0200
  * Initialize zip\_dict\_ids table and avoid referencing array items as currently MariaDB does not support compressed columns.
* [Revision #923a7f8](https://github.com/MariaDB/server/commit/923a7f8)\
  2016-10-31 12:16:53 +0200
  * [MDEV-11188](https://jira.mariadb.org/browse/MDEV-11188): rpl.rpl\_parallel\_partition fails with valgrind warnings in buildbot and outside
* [Revision #425d341](https://github.com/MariaDB/server/commit/425d341)\
  2016-10-28 11:46:15 -0400
  * bump the VERSION
* [Revision #cb7b03b](https://github.com/MariaDB/server/commit/cb7b03b)\
  2016-10-28 13:34:13 +0400
  * [MDEV-11164](https://jira.mariadb.org/browse/MDEV-11164) - hardening-wrapper has been removed from Debian Sid
* [Revision #a629b51](https://github.com/MariaDB/server/commit/a629b51)\
  2016-12-10 23:04:41 +0200
  * Updated the list of unstable tests
* [Revision #83f7151](https://github.com/MariaDB/server/commit/83f7151)\
  2016-12-09 17:13:43 +0400
  * [MDEV-10435](https://jira.mariadb.org/browse/MDEV-10435) crash with bad stat tables.
* [Revision #870d758](https://github.com/MariaDB/server/commit/870d758)\
  2016-12-08 20:49:54 +0200
  * [MDEV-11491](https://jira.mariadb.org/browse/MDEV-11491) binlog\_encryption.rpl\_checksum fails sporadically in buildbot
* [Revision #8e702bc](https://github.com/MariaDB/server/commit/8e702bc)\
  2016-12-08 17:05:01 +0200
  * [MDEV-11504](https://jira.mariadb.org/browse/MDEV-11504) binlog\_encryption.encrypted\_master\_switch\_to\_unencrypted fails sporadically in buildbot
* [Revision #e1e1fbc](https://github.com/MariaDB/server/commit/e1e1fbc) 2016-12-07 14:05:04 +0400 - Merge pull request #272 from iangilfillan/10.1
* [Revision #63edd27](https://github.com/MariaDB/server/commit/63edd27)\
  2016-12-07 11:58:40 +0200
  * Update mysqld\_multi man page
* [Revision #2114aa4](https://github.com/MariaDB/server/commit/2114aa4) 2016-12-07 13:37:16 +0400 - Merge pull request #270 from JRonak/[MDEV-11354](https://jira.mariadb.org/browse/MDEV-11354)
* [Revision #d036be7](https://github.com/MariaDB/server/commit/d036be7)\
  2016-12-06 02:29:52 +0530
  * fixes [MDEV-11354](https://jira.mariadb.org/browse/MDEV-11354) twin include
* [Revision #74d52de](https://github.com/MariaDB/server/commit/74d52de)\
  2016-12-05 22:29:25 +0100
  * fix binlog\_encryption.binlog\_incident test
* [Revision #76546a0](https://github.com/MariaDB/server/commit/76546a0)\
  2016-12-05 15:51:24 +0100
  * [MDEV-10382](https://jira.mariadb.org/browse/MDEV-10382) Using systemd, mariadb doesn't restart on crashes
* [Revision #5142cd5](https://github.com/MariaDB/server/commit/5142cd5)\
  2016-12-04 21:19:32 +0100
  * [MDEV-11052](https://jira.mariadb.org/browse/MDEV-11052) mariadb-service-convert does not work after upgrading to 10.1.18
* [Revision #b5aa0f4](https://github.com/MariaDB/server/commit/b5aa0f4)\
  2016-12-03 20:34:50 +0100
  * [MDEV-11319](https://jira.mariadb.org/browse/MDEV-11319) mysqlbinlog crashes or fails with out of memory while reading some encrypted binlogs
* [Revision #952856c](https://github.com/MariaDB/server/commit/952856c)\
  2016-12-03 20:26:42 +0100
  * [MDEV-11288](https://jira.mariadb.org/browse/MDEV-11288) Server crashes in Binlog\_crypt\_data::init trying to feed encrypted log without decryption capabilities
* [Revision #611f916](https://github.com/MariaDB/server/commit/611f916)\
  2016-12-05 20:19:01 +0200
  * [MDEV-9038](https://jira.mariadb.org/browse/MDEV-9038) Binlog encryption tests
* [Revision #9199d72](https://github.com/MariaDB/server/commit/9199d72)\
  2016-12-05 15:25:59 +0200
  * [MDEV-11233](https://jira.mariadb.org/browse/MDEV-11233) CREATE FULLTEXT INDEX with a token longer than 127 bytes crashes server
* [Revision #ead6d0d](https://github.com/MariaDB/server/commit/ead6d0d)\
  2016-12-05 03:13:28 +0200
  * Follow-up for [MDEV-9451](https://jira.mariadb.org/browse/MDEV-9451) - fix XtraDB rdiff files
* [Revision #b0754ad](https://github.com/MariaDB/server/commit/b0754ad)\
  2016-12-05 03:11:42 +0200
  * Follow-up for [MDEV-11429](https://jira.mariadb.org/browse/MDEV-11429) - fix result files for embedded and 32-bit tests
* [Revision #f1b80d8](https://github.com/MariaDB/server/commit/f1b80d8)\
  2016-12-02 16:25:47 +0200
  * [MDEV-11236](https://jira.mariadb.org/browse/MDEV-11236) Failing assertion: state == TRX\_STATE\_NOT\_STARTED
* [Revision #1e7f961](https://github.com/MariaDB/server/commit/1e7f961)\
  2016-12-01 14:56:09 +0200
  * [MDEV-9451](https://jira.mariadb.org/browse/MDEV-9451) innodb\_buffer\_pool\_populate does not seem to work on 10.1.10
* [Revision #97b21a1](https://github.com/MariaDB/server/commit/97b21a1)\
  2016-12-02 14:02:30 +0200
  * [MDEV-10759](https://jira.mariadb.org/browse/MDEV-10759) Fix Aria to support 2-byte collation IDs - Used same fix as for MyISAM: High level collation byte stored in unused bit\_end position. - Moved language from header to base\_info - Removed unused bit\_end part in HA\_KEY\_SEG
* [Revision #2996f9a](https://github.com/MariaDB/server/commit/2996f9a)\
  2016-11-30 18:36:29 +0200
  * [MDEV-11429](https://jira.mariadb.org/browse/MDEV-11429) Increase number of max table\_open\_cache instances
* [Revision #2fd3af4](https://github.com/MariaDB/server/commit/2fd3af4)\
  2016-12-01 13:45:23 -0500
  * [MDEV-11168](https://jira.mariadb.org/browse/MDEV-11168): InnoDB: Failing assertion: !other\_lock || wsrep\_thd\_is\_BF(lock->trx->mysql\_thd, FALSE) || wsrep\_thd\_is\_BF(other\_lock->trx->mysql\_thd, FALSE)
* [Revision #dbdef41](https://github.com/MariaDB/server/commit/dbdef41)\
  2016-11-29 08:41:45 +0200
  * [MDEV-10686](https://jira.mariadb.org/browse/MDEV-10686): innodb\_zip.innodb\_prefix\_index\_liftedlimit failed with timeout in buildbot
* [Revision #9f31949](https://github.com/MariaDB/server/commit/9f31949)\
  2016-11-29 08:35:51 +0200
  * [MDEV-10739](https://jira.mariadb.org/browse/MDEV-10739): encryption.innodb-page\_encryption\_compression fails with timeout on valgrind
* [Revision #e493c6b](https://github.com/MariaDB/server/commit/e493c6b) 2016-11-28 09:57:28 +0100 - Merge remote-tracking branch 'my/tokudb\_optimistic\_parallel\_replication' into 10.1
* [Revision #3bec0b3](https://github.com/MariaDB/server/commit/3bec0b3)\
  2016-11-23 16:45:31 +0100
  * Parallel replication test case for TokuDB.
* [Revision #021f78f](https://github.com/MariaDB/server/commit/021f78f)\
  2016-11-23 16:44:03 +0100
  * Use thd\_kill\_level() over old thd\_killed() in TokuDB.
* [Revision #660a292](https://github.com/MariaDB/server/commit/660a292)\
  2016-11-23 16:46:33 +0100
  * Fix optimistic parallel replication for TokuDB.
* [Revision #d145d1b](https://github.com/MariaDB/server/commit/d145d1b)\
  2016-11-23 12:29:38 +0100
  * fix bogus stalls in the lock tree for low concurrency applications
* [Revision #a68d135](https://github.com/MariaDB/server/commit/a68d135)\
  2016-11-25 06:28:02 +0200
  * [MDEV-11349](https://jira.mariadb.org/browse/MDEV-11349) (2/2) Fix some bogus-looking Valgrind warnings
* [Revision #8da33e3](https://github.com/MariaDB/server/commit/8da33e3)\
  2016-11-25 06:09:00 +0200
  * [MDEV-11349](https://jira.mariadb.org/browse/MDEV-11349) (1/2) Fix some clang 4.0 warnings
* [Revision #1d8eafb](https://github.com/MariaDB/server/commit/1d8eafb)\
  2016-11-24 15:55:55 +0400
  * Removing the unused function my\_bincmp() from strings/ctype-ucs2.c
* [Revision #57058cb](https://github.com/MariaDB/server/commit/57058cb)\
  2016-11-22 16:38:36 +0200
  * [MDEV-10377](https://jira.mariadb.org/browse/MDEV-10377): innodb.innodb\_blob\_truncate fails in buildbot: Failing assertion: page\_type == 34354 || page\_type == 37401 || page\_type == 17855 || page\_type == 2 || page\_type == 3 || ...
* [Revision #ee3c99d](https://github.com/MariaDB/server/commit/ee3c99d) 2016-11-22 16:17:05 +0530 - Merge branch 'bb-[MDEV-11016](https://jira.mariadb.org/browse/MDEV-11016)' into 10.1
* [Revision #7ed5563](https://github.com/MariaDB/server/commit/7ed5563)\
  2016-10-26 14:52:24 +0530
  * [MDEV-11016](https://jira.mariadb.org/browse/MDEV-11016) wsrep\_node\_is\_ready() check is too strict Problem:- The condition that checks for node readiness is too strict as it does not allow SELECTs even if these selects do not access any tables. For example,if we run SELECT 1; OR SELECT @@max\_allowed\_packet; Solution:- We need not to report this error when all\_tables(lex->query\_tables) is NULL:
* [Revision #af05bec](https://github.com/MariaDB/server/commit/af05bec)\
  2016-11-16 13:52:41 +0200
  * [MDEV-10771](https://jira.mariadb.org/browse/MDEV-10771): Test innodb\_defragment\_fill\_factor does not work correctly
* [Revision #bccd0b5](https://github.com/MariaDB/server/commit/bccd0b5) 2016-11-15 13:10:21 +0100 - Merge branch 'mdev10863' into 10.1
* [Revision #717f212](https://github.com/MariaDB/server/commit/717f212)\
  2016-11-04 12:33:42 +0100
  * [MDEV-10863](https://jira.mariadb.org/browse/MDEV-10863): parallel replication tries to continue from wrong position
* [Revision #cf29e8c](https://github.com/MariaDB/server/commit/cf29e8c)\
  2016-11-14 11:02:57 -0500
  * wsrep\_info plugin: Fix test case
* [Revision #1fee017](https://github.com/MariaDB/server/commit/1fee017)\
  2016-11-09 15:23:25 +0200
  * [MDEV-10692](https://jira.mariadb.org/browse/MDEV-10692): InnoDB: Failing assertion: lock->trx->lock.wait\_lock == lock When we enter here wait\_lock could be already gone i.e. NULL, that should be allowed.
* [Revision #6ae3dd6](https://github.com/MariaDB/server/commit/6ae3dd6)\
  2016-11-09 00:10:45 +0100
  * AWS Key management plugin does not build on Centos7.
* [Revision #909e239](https://github.com/MariaDB/server/commit/909e239)\
  2016-11-07 10:51:35 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
