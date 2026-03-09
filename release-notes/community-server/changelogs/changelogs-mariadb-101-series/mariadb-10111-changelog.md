# MariaDB 10.1.11 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.11)[Release Notes](../../old-releases/10.1/10.1.11.md)[Changelog](mariadb-10111-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 29 Jan 2016

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.11.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #7b14ba6](https://github.com/MariaDB/server/commit/7b14ba6)\
  2016-01-28 14:06:05 +0200
  * [MDEV-8724](https://jira.mariadb.org/browse/MDEV-8724) Assertion \`rc == 0' failed in ma\_decrypt on reading an Aria table
* [Revision #ce40cca](https://github.com/MariaDB/server/commit/ce40cca)\
  2016-01-28 13:58:39 +0400
  * [MDEV-9181](https://jira.mariadb.org/browse/MDEV-9181) (NULLIF(count(table.col)), 0) gives wrong result on 10.1.x Wrapping args\[0] and args\[2] into an Item\_cache for aggregate functions.
* [Revision #5092ab28](https://github.com/MariaDB/server/commit/5092ab28)\
  2016-01-28 08:57:30 +0100
  * bump the version
* [Revision #11c85e1](https://github.com/MariaDB/server/commit/11c85e1)\
  2016-01-27 23:58:01 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. The SQL command 'PREPARE' was broken - should be take into account.
* [Revision #418518c](https://github.com/MariaDB/server/commit/418518c)\
  2016-01-27 16:42:42 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. Keep the embedded-server version valid.
* [Revision #d16d40b](https://github.com/MariaDB/server/commit/d16d40b)\
  2016-01-27 14:58:52 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. SHOW CREATE PROCEDURE/FUNCTION fixed.
* [Revision #34df314](https://github.com/MariaDB/server/commit/34df314)\
  2016-01-27 13:57:25 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. SHOW BINARY LOGS fixed.
* [Revision #efb36ac](https://github.com/MariaDB/server/commit/efb36ac)\
  2016-01-27 13:42:53 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. SHOW MASTER STATUS fixed.
* [Revision #75a1d86](https://github.com/MariaDB/server/commit/75a1d86)\
  2016-01-27 13:31:53 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. SHOW SLAVE STATUS fixed.
* [Revision #552d330](https://github.com/MariaDB/server/commit/552d330)\
  2016-01-27 12:39:27 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. Fix for SHOW GRANTS statement.
* [Revision #f3926cd](https://github.com/MariaDB/server/commit/f3926cd)\
  2016-01-27 12:01:55 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. Fix for SHOW CREATE DATABASE.
* [Revision #07e9762](https://github.com/MariaDB/server/commit/07e9762)\
  2016-01-22 19:29:26 +0100
  * [MDEV-8615](https://jira.mariadb.org/browse/MDEV-8615): Assertion \`m\_cpp\_buf <= begin\_ptr && begin\_ptr <= m\_cpp\_buf + m\_buf\_length' failed in Lex\_input\_stream::body\_utf8\_start
* [Revision #eb15566](https://github.com/MariaDB/server/commit/eb15566)\
  2016-01-27 15:26:12 +0100
  * fix failures of ps and ps\_1general in --ps-protocol
* [Revision #02cc921](https://github.com/MariaDB/server/commit/02cc921)\
  2016-01-27 15:14:57 +0100
  * compiler warnings
* [Revision #4b31e6d](https://github.com/MariaDB/server/commit/4b31e6d)\
  2016-01-27 15:23:42 +0100
  * Address review comments, add unit test
* [Revision #c1bf5ba](https://github.com/MariaDB/server/commit/c1bf5ba)\
  2015-10-13 17:10:16 +0200
  * Revert "On Windows SSL works with sockets only, so we shouldn't tell the client"
* [Revision #33e5a8a](https://github.com/MariaDB/server/commit/33e5a8a)\
  2015-10-13 16:35:53 +0200
  * On Windows SSL works with sockets only, so we shouldn't tell the client that we support SSL when using named pipes or shared memory.
* [Revision #ef3ca5c](https://github.com/MariaDB/server/commit/ef3ca5c)\
  2015-10-13 10:13:53 +0200
  * New authentication plugin for authentication via named pipe on Windows operating systems.
* [Revision #13b79f4](https://github.com/MariaDB/server/commit/13b79f4)\
  2016-01-27 16:33:41 +0200
  * Fixed [MDEV-9347](https://jira.mariadb.org/browse/MDEV-9347) Not all rows returned by the C API
* [Revision #b404b23](https://github.com/MariaDB/server/commit/b404b23)\
  2016-01-27 11:42:31 +0400
  * [MDEV-9332](https://jira.mariadb.org/browse/MDEV-9332) Bug after upgrade to 10.1.10
* [Revision #7d39b28](https://github.com/MariaDB/server/commit/7d39b28)\
  2016-01-26 16:33:06 +0200
  * \[[MDEV-9468](https://jira.mariadb.org/browse/MDEV-9468)]: Client hangs in my\_addr\_resolve
* [Revision #d227399](https://github.com/MariaDB/server/commit/d227399)\
  2016-01-26 23:16:56 +0400
  * Comment fixed.
* [Revision #df26954](https://github.com/MariaDB/server/commit/df26954)\
  2016-01-26 16:00:59 +0400
  * [MDEV-5273](https://jira.mariadb.org/browse/MDEV-5273) Prepared statement doesn't return metadata after prepare. The metadata creation part of the mysqld\_shww\_create separated to be used on the mysqld\_stmt\_prepare stage.
* [Revision #a095c99](https://github.com/MariaDB/server/commit/a095c99)\
  2016-01-26 17:56:41 +0100
  * Fix packaging for client RPM plugins - provide 'ignored' list
* [Revision #7831b79](https://github.com/MariaDB/server/commit/7831b79)\
  2016-01-26 17:46:42 +0100
  * Merge branch '10.1' of [server](https://github.com/MariaDB/server) into 10.1
* [Revision #77c75a4](https://github.com/MariaDB/server/commit/77c75a4)\
  2016-01-26 17:52:24 +0400
  * A clean-up patch for Item\_func\_conv\_charset (needed for [MDEV-9181](https://jira.mariadb.org/browse/MDEV-9181)) Removing the "conv\_charset" member and using collation.collation instead, as they duplicated each other.
* [Revision #c76ab94](https://github.com/MariaDB/server/commit/c76ab94)\
  2016-01-26 14:36:13 +0100
  * Fix invalid format warnings
* [Revision #71b3906](https://github.com/MariaDB/server/commit/71b3906)\
  2016-01-25 20:17:55 +0100
  * after merge fixes
* [Revision #44dea7f](https://github.com/MariaDB/server/commit/44dea7f)\
  2016-01-25 22:59:41 +0100
  * Merge branch 'connect/10.1' into 10.1
* [Revision #f4faac4](https://github.com/MariaDB/server/commit/f4faac4)\
  2016-01-25 22:58:57 +0100
  * Merge branch '10.0' into 10.1
* [Revision #2ff65ba](https://github.com/MariaDB/server/commit/2ff65ba)\
  2016-01-24 17:41:11 +0100
  * [MDEV-9299](https://jira.mariadb.org/browse/MDEV-9299) Test main.events\_2 incompatible with Debian reproducibility testing framework
* [Revision #ed4fb9b](https://github.com/MariaDB/server/commit/ed4fb9b)\
  2016-01-24 19:53:32 +0100
  * [MDEV-9259](https://jira.mariadb.org/browse/MDEV-9259) Add missing mroonga files to Debian packaging in 10.1
* [Revision #5da7c34](https://github.com/MariaDB/server/commit/5da7c34)\
  2016-01-23 20:40:01 +0100
  * [MDEV-9428](https://jira.mariadb.org/browse/MDEV-9428) NO\_AUTO\_VALUE\_ON\_ZERO is ignored when a trigger before insert is defined
* [Revision #68910e7](https://github.com/MariaDB/server/commit/68910e7)\
  2016-01-24 20:43:19 +0100
  * [MDEV-9273](https://jira.mariadb.org/browse/MDEV-9273) ERROR 1819 on grant statment for existing user
* [Revision #d14c4c7](https://github.com/MariaDB/server/commit/d14c4c7)\
  2016-01-24 20:00:35 +0100
  * cleanup: move all password validation logic into one function
* [Revision #d5b1b1a](https://github.com/MariaDB/server/commit/d5b1b1a)\
  2016-01-25 22:57:47 +0100
  * stack too small on labrador (again!)
* [Revision #666b966](https://github.com/MariaDB/server/commit/666b966)\
  2016-01-25 19:03:33 +0100
  * update test results
* [Revision #c371073](https://github.com/MariaDB/server/commit/c371073)\
  2016-01-23 16:24:32 +0100
  * cleanup: LEX\_USER::pwtext and LEX\_USER::pwhash
* [Revision #1fea7e7](https://github.com/MariaDB/server/commit/1fea7e7)\
  2016-01-23 16:08:24 +0100
  * cleanup: create LEX\_USER::reset\_auth()
* [Revision #b01e2ff](https://github.com/MariaDB/server/commit/b01e2ff)\
  2016-01-21 22:10:44 +0100
  * [MDEV-9385](https://jira.mariadb.org/browse/MDEV-9385) Devel package wants ownership of /usr/share/pkgconfig on CentOS/RHEL
* [Revision #5a5f18f](https://github.com/MariaDB/server/commit/5a5f18f)\
  2016-01-21 21:58:30 +0100
  * [MDEV-9205](https://jira.mariadb.org/browse/MDEV-9205) PAM user map plugin does not work with LDAP groups
* [Revision #a2330c8](https://github.com/MariaDB/server/commit/a2330c8)\
  2016-01-25 17:04:09 +0100
  * [MDEV-8208](https://jira.mariadb.org/browse/MDEV-8208) Sporadic SEGFAULT on startup
* [Revision #744e605](https://github.com/MariaDB/server/commit/744e605)\
  2015-12-26 09:40:49 +0100
  * cleanup: wsrep helper to create a thread
* [Revision #0fab28c](https://github.com/MariaDB/server/commit/0fab28c)\
  2015-12-22 20:25:29 +0100
  * cmake: better auto \*.i targets in Makefiles
* [Revision #1793646](https://github.com/MariaDB/server/commit/1793646)\
  2016-01-25 16:37:08 +0400
  * Merge branch '5.5' into 10.0
* [Revision #da0991c](https://github.com/MariaDB/server/commit/da0991c)\
  2016-01-21 14:03:24 +0400
  * [MDEV-7875](https://jira.mariadb.org/browse/MDEV-7875) Duplicate maria\_add\_gis\_sp script in the sources. Now both are generated by the cmake from the scripts/maria\_add\_gis\_sp.sql.in
* [Revision #ff8d400](https://github.com/MariaDB/server/commit/ff8d400)\
  2016-01-24 12:31:11 +0300
  * [MDEV-9457](https://jira.mariadb.org/browse/MDEV-9457): Poor query plan chosen for ORDER BY query by a recent 10.1
* [Revision #825f51d](https://github.com/MariaDB/server/commit/825f51d)\
  2015-12-16 19:33:41 +0100
  * [MDEV-9118](https://jira.mariadb.org/browse/MDEV-9118) ANALYZE TABLE for Engine independent status fetchs blob/text columns without use
* [Revision #45920d3](https://github.com/MariaDB/server/commit/45920d3)\
  2016-01-20 21:29:37 +0100
  * Merge pull request #151 from frozencemetery/my\_name
* [Revision #42d9f3d](https://github.com/MariaDB/server/commit/42d9f3d)\
  2016-01-20 13:24:30 -0500
  * Fix spelling of my name
* [Revision #4bb62e9](https://github.com/MariaDB/server/commit/4bb62e9)\
  2016-01-20 14:35:11 +0100
  * Do not require server RPM for client plugins
* [Revision #67cf76a](https://github.com/MariaDB/server/commit/67cf76a)\
  2016-01-18 19:30:46 +0100
  * MDEV 4691- address review comments
* [Revision #059c0c8](https://github.com/MariaDB/server/commit/059c0c8)\
  2016-01-19 07:59:02 +0200
  * Merge pull request #149 from grooverdan/10.1-static-analysis-innodbchecksum
* [Revision #f602c39](https://github.com/MariaDB/server/commit/f602c39)\
  2016-01-19 14:19:31 +1100
  * innodbchecksum: add fclose and handle errors
* [Revision #e7a89b4](https://github.com/MariaDB/server/commit/e7a89b4)\
  2016-01-17 22:57:37 +0200
  * Revert "\[Code cleanup] Refactor duplicate code within myisam and maria sort.cc"
* [Revision #acc8379](https://github.com/MariaDB/server/commit/acc8379)\
  2016-01-17 22:57:27 +0200
  * Revert "Fixed compilation failure on MacOSX"
* [Revision #275f7d7](https://github.com/MariaDB/server/commit/275f7d7)\
  2016-01-17 22:33:36 +0200
  * Remove warning in my\_addr\_resolve
* [Revision #b2bd10d](https://github.com/MariaDB/server/commit/b2bd10d)\
  2016-01-17 22:23:21 +0200
  * \[[MDEV-9427](https://jira.mariadb.org/browse/MDEV-9427)] Server does not build on OpenSUSE 42.1
* [Revision #6d3ffd2](https://github.com/MariaDB/server/commit/6d3ffd2)\
  2015-12-11 09:16:42 +0200
  * Fixed a crash during stacktrace printing if addr2line failed to start.
* [Revision #df32495](https://github.com/MariaDB/server/commit/df32495)\
  2015-12-10 03:56:31 +0200
  * Fixed compilation failure on MacOSX
* [Revision #727f92f](https://github.com/MariaDB/server/commit/727f92f)\
  2015-12-09 23:36:16 +0200
  * \[Code cleanup] Refactor duplicate code within myisam and maria sort.cc
* [Revision #38bcb44](https://github.com/MariaDB/server/commit/38bcb44)\
  2016-01-15 14:24:11 +0100
  * After-merge fix.
* [Revision #2f88b14](https://github.com/MariaDB/server/commit/2f88b14)\
  2016-01-15 13:01:19 +0100
  * Merge branch 'tmp' into tmp-10.1
* [Revision #74b1af1](https://github.com/MariaDB/server/commit/74b1af1)\
  2016-01-15 12:50:23 +0100
  * Merge branch 'tmp' into tmp-10.0
* [Revision #06b2e32](https://github.com/MariaDB/server/commit/06b2e32)\
  2016-01-15 12:42:51 +0100
  * Fix error handling for GTID and domain-based parallel replication
* [Revision #9c9d10b](https://github.com/MariaDB/server/commit/9c9d10b)\
  2016-01-15 09:50:27 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin not working with MySQL 5.7. fixing Windows crash.
* [Revision #55d61ec](https://github.com/MariaDB/server/commit/55d61ec)\
  2016-01-14 13:31:08 +0100
  * [MDEV-4961](https://jira.mariadb.org/browse/MDEV-4961) SSPI/GSSAPI/Kerberos authentication plugin
* [Revision #fe4823d](https://github.com/MariaDB/server/commit/fe4823d)\
  2016-01-13 18:02:44 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin doesnt run with MySQL 5.7. updata thread\_pool\_server\_audit test result.
* [Revision #cdc9aa5](https://github.com/MariaDB/server/commit/cdc9aa5)\
  2016-01-13 15:24:33 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit Plugin doesn't run with MySQL 5.7. [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) built in debug gets unhappy with mutexes. Although everything is correct, some DBUG\_ASSERT can happen. So this patch keeps safe\_mutex silent.
* [Revision #c955253](https://github.com/MariaDB/server/commit/c955253)\
  2016-01-12 16:29:02 +0400
  * [MDEV-9106](https://jira.mariadb.org/browse/MDEV-9106) Audit plugin compiled with MariaDB can't install on MySQL 5.7. The audit API was seriously changed in MySQL 5.7. so we had to adapt the plugin's code to that.
* [Revision #3e20a0d](https://github.com/MariaDB/server/commit/3e20a0d)\
  2016-01-09 19:51:51 +0100\
  \*
  * Fix [MDEV-9239](https://jira.mariadb.org/browse/MDEV-9239). Meanwhile, make all references to the database in XTAB Schema (was sometimes in XTAB Catalog)
* [Revision #3730d8a](https://github.com/MariaDB/server/commit/3730d8a)\
  2016-01-05 22:48:50 +0100
  * [MDEV-9366](https://jira.mariadb.org/browse/MDEV-9366) : do\_shutdown\_server fails to detect server shutdown on Windows. Fix test whether process is alive in mysqltest.
* [Revision #1236333](https://github.com/MariaDB/server/commit/1236333)\
  2015-12-24 21:46:38 +0100
  * Fix annoying repetitive tokudb build warning, if MariaDB is build on non-Linux x64 system
* [Revision #5f48b61](https://github.com/MariaDB/server/commit/5f48b61)\
  2016-01-07 14:45:40 +0100
  * [MDEV-9298](https://jira.mariadb.org/browse/MDEV-9298) : Build failure when linking libmysql.
* [Revision #111acb7](https://github.com/MariaDB/server/commit/111acb7)\
  2016-01-05 18:50:54 +0200
  * [MDEV-9359](https://jira.mariadb.org/browse/MDEV-9359): encryption.create\_or\_replace fails sporadically in buildbot: failing assertion: mutex->magic\_n == MUTEX\_MAGIC\_N
* [Revision #8fcc0bf](https://github.com/MariaDB/server/commit/8fcc0bf)\
  2016-01-03 13:27:59 +0200
  * Fixed bug in semi\_sync replication tests.
* [Revision #661a6d8](https://github.com/MariaDB/server/commit/661a6d8)\
  2016-01-03 13:20:07 +0200
  * Cleanup of slave code:
* [Revision #4b4777a](https://github.com/MariaDB/server/commit/4b4777a)\
  2016-01-03 12:48:55 +0200
  * Backported fix for ccache Fixed compiler warnings Added --big-test to tokudb change\_column\_char & change\_column\_bin
* [Revision #56e0de0](https://github.com/MariaDB/server/commit/56e0de0)\
  2015-12-30 20:56:52 +0100
  * Merge branch '10.0' into 10.1
* [Revision #ae7b39a](https://github.com/MariaDB/server/commit/ae7b39a)\
  2015-12-30 20:55:12 +0100
  * Merge branch '5.5' into 10.0
* [Revision #ff24820](https://github.com/MariaDB/server/commit/ff24820)\
  2015-12-30 19:39:31 +0100
  * Fix process handle leak in buildbot. GenerateConsoleCtrlEvent sent to non-existing process will add a process handle to this non-existing process to console host process conhost.exe
* [Revision #1bb66ea](https://github.com/MariaDB/server/commit/1bb66ea)\
  2015-12-29 18:44:13 +0400
  * Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #4d3bc26](https://github.com/MariaDB/server/commit/4d3bc26)\
  2015-12-29 18:41:37 +0400
  * Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #61d3621](https://github.com/MariaDB/server/commit/61d3621)\
  2015-12-29 18:40:41 +0400
  * Moving Field\_blob::store\_length() back from protected to public, as it's needed for Cassandra in 10.0.
* [Revision #4282ac4](https://github.com/MariaDB/server/commit/4282ac4)\
  2015-12-29 15:22:33 +0400
  * Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #7529870](https://github.com/MariaDB/server/commit/7529870)\
  2015-12-29 15:19:29 +0400
  * Merge branch '10.0' of github.com:MariaDB/server into 10.0
* [Revision #6d7362e](https://github.com/MariaDB/server/commit/6d7362e)\
  2015-12-29 15:18:55 +0400
  * Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #f31a891](https://github.com/MariaDB/server/commit/f31a891)\
  2015-11-18 15:51:20 +0400
  * [MDEV-9128](https://jira.mariadb.org/browse/MDEV-9128) - Compiling on IBM System Z fails
* [Revision #93b078c](https://github.com/MariaDB/server/commit/93b078c)\
  2015-12-27 15:40:34 +0400
  * [MDEV-9128](https://jira.mariadb.org/browse/MDEV-9128) - Compiling on IBM System Z fails
* [Revision #e1b9be5](https://github.com/MariaDB/server/commit/e1b9be5)\
  2015-12-29 14:17:31 +0400
  * [MDEV-9319](https://jira.mariadb.org/browse/MDEV-9319) ALTER from a bigger to a smaller blob type truncates too much data
* [Revision #3e76d54](https://github.com/MariaDB/server/commit/3e76d54)\
  2015-12-27 19:37:28 +0100\
  \*
  * Fix [MDEV-9322](https://jira.mariadb.org/browse/MDEV-9322).
* [Revision #30b2447](https://github.com/MariaDB/server/commit/30b2447)\
  2015-12-27 15:40:34 +0400
  * [MDEV-9128](https://jira.mariadb.org/browse/MDEV-9128) - Compiling on IBM System Z fails
* [Revision #0f10a5c](https://github.com/MariaDB/server/commit/0f10a5c)\
  2015-12-24 21:46:38 +0100
  * Fix annoying repetitive tokudb build warning, if MariaDB is build on non-Linux x64 system
* [Revision #000eba9](https://github.com/MariaDB/server/commit/000eba9)\
  2015-12-23 10:42:55 -0500
  * Merge branch '10.0-galera' into 10.1
* [Revision #89a2648](https://github.com/MariaDB/server/commit/89a2648)\
  2015-12-23 09:51:32 -0500
  * [MDEV-9224](https://jira.mariadb.org/browse/MDEV-9224): postfix - thd can be null in reload\_acl\_and\_cache()
* [Revision #e6c0f25](https://github.com/MariaDB/server/commit/e6c0f25)\
  2015-12-22 15:09:29 -0500
  * Merge branch '5.5-galera' into 10.0-galera
* [Revision #fe4047d](https://github.com/MariaDB/server/commit/fe4047d)\
  2015-12-22 15:02:18 -0500
  * [MDEV-9224](https://jira.mariadb.org/browse/MDEV-9224) : Database lockup on flush in galera
* [Revision #70113ee](https://github.com/MariaDB/server/commit/70113ee)\
  2015-12-22 14:58:02 -0500
  * [MDEV-9290](https://jira.mariadb.org/browse/MDEV-9290) : InnoDB: Assertion failure in file trx0sys.cc line 353

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
