# MariaDB 10.5.19 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.5/10.5.19.md)[Changelog](mariadb-10-5-19-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.19/)

**Release date:** 6 Feb 2023

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.19.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.28](../changelogs-mariadb-10-4-series/mariadb-10-4-28-changelog.md)
* [Revision #f8a85af8ca](https://github.com/MariaDB/server/commit/f8a85af8ca)\
  2023-01-30 19:26:16 +0200
  * [MDEV-30940](https://jira.mariadb.org/browse/MDEV-30940): Revert "binlog.innodb\_rc\_insert\_before\_delete is disabled with [MDEV-30490](https://jira.mariadb.org/browse/MDEV-30490)"
* [Revision #b2ea57e899](https://github.com/MariaDB/server/commit/b2ea57e899)\
  2023-01-28 17:10:42 +0200
  * binlog.innodb\_rc\_insert\_before\_delete is disabled with [MDEV-30490](https://jira.mariadb.org/browse/MDEV-30490)
* Merge [Revision #db8019ef00](https://github.com/MariaDB/server/commit/db8019ef00) 2023-01-30 13:25:02 +0100 - Merge branch '10.4' into 10.5
* [Revision #6173a4a15b](https://github.com/MariaDB/server/commit/6173a4a15b)\
  2023-01-28 17:10:42 +0200
  * binlog.innodb\_rc\_insert\_before\_delete is disabled with [MDEV-30490](https://jira.mariadb.org/browse/MDEV-30490)
* Merge [Revision #7fa02f5c0b](https://github.com/MariaDB/server/commit/7fa02f5c0b) 2023-01-27 13:54:14 +0100 - Merge branch '10.4' into 10.5
* [Revision #c8f9bb2718](https://github.com/MariaDB/server/commit/c8f9bb2718)\
  2023-01-26 12:04:28 +0300
  * [MDEV-30218](https://jira.mariadb.org/browse/MDEV-30218): Incorrect optimization for rowid\_filtering, correction
* Merge [Revision #dd24fa3063](https://github.com/MariaDB/server/commit/dd24fa3063) 2023-01-26 10:34:26 +0100 - Merge branch '10.3' into 10.4
* [Revision #672cdcbb93](https://github.com/MariaDB/server/commit/672cdcbb93)\
  2023-01-26 14:47:52 +0200
  * [MDEV-30404](https://jira.mariadb.org/browse/MDEV-30404): Inconsistent updates of PAGE\_MAX\_TRX\_ID on ROW\_FORMAT=COMPRESSED pages
* [Revision #e02ed04d17](https://github.com/MariaDB/server/commit/e02ed04d17)\
  2023-01-25 13:53:10 +0200
  * [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855) fixup: Remove SRV\_MASTER\_CHECKPOINT\_INTERVAL
* [Revision #8bccba1d4a](https://github.com/MariaDB/server/commit/8bccba1d4a)\
  2023-01-25 10:01:00 +0200
  * [MDEV-30465](https://jira.mariadb.org/browse/MDEV-30465) : Galera test galera\_sr.[MDEV-27615](https://jira.mariadb.org/browse/MDEV-27615) takes 5mins
* [Revision #2ba6f3d46a](https://github.com/MariaDB/server/commit/2ba6f3d46a)\
  2023-01-23 10:49:57 +0200
  * Update 10.5 HELP tables
* [Revision #dc646c2389](https://github.com/MariaDB/server/commit/dc646c2389)\
  2023-01-19 19:42:24 +0200
  * [MDEV-30423](https://jira.mariadb.org/browse/MDEV-30423) Deadlock on Replica during BACKUP STAGE BLOCK\_COMMIT on XA transactions
* [Revision #647a7232ff](https://github.com/MariaDB/server/commit/647a7232ff)\
  2023-01-20 16:07:43 +0530
  * [MDEV-30438](https://jira.mariadb.org/browse/MDEV-30438) innodb.undo\_truncate,4k fails when innodb-immediate-scrub-data-uncompressed is enabled
* Merge [Revision #d9fbc6289d](https://github.com/MariaDB/server/commit/d9fbc6289d) 2023-01-20 13:02:19 +0100 - Merge branch 'merge-perfschema-5.7' into 10.5
* [Revision #986276f019](https://github.com/MariaDB/server/commit/986276f019)\
  2023-01-20 12:55:21 +0100
  * mysql-5.7.41
* [Revision #eeb8ebb152](https://github.com/MariaDB/server/commit/eeb8ebb152)\
  2023-01-16 17:02:16 +0100
  * [MDEV-29774](https://jira.mariadb.org/browse/MDEV-29774) BF abort no longer wakes up debug\_sync waiters
* [Revision #8d91e3f614](https://github.com/MariaDB/server/commit/8d91e3f614)\
  2023-01-10 12:48:09 +1100
  * [MDEV-30191](https://jira.mariadb.org/browse/MDEV-30191) Remove the to-be-freed spider condition in an sp call
* [Revision #da798c9511](https://github.com/MariaDB/server/commit/da798c9511)\
  2023-01-16 14:18:07 +0100
  * new PCRE2 10.42
* Merge [Revision #86059fd10a](https://github.com/MariaDB/server/commit/86059fd10a) 2023-01-18 14:52:13 +0100 - Merge branch '10.4' into 10.5
* [Revision #ff72a9431a](https://github.com/MariaDB/server/commit/ff72a9431a)\
  2022-12-29 22:46:53 +0530
  * [MDEV-26392](https://jira.mariadb.org/browse/MDEV-26392): Crash with json\_get\_path\_next and 10.5.12
* Merge [Revision #0459d2ccfc](https://github.com/MariaDB/server/commit/0459d2ccfc) 2023-01-17 19:01:28 +0200 - Merge 10.4 into 10.5
* [Revision #22cd3358b3](https://github.com/MariaDB/server/commit/22cd3358b3)\
  2023-01-16 12:08:05 +0100
  * fix failures of main.func\_json --ps
* [Revision #3b932255cc](https://github.com/MariaDB/server/commit/3b932255cc)\
  2023-01-16 12:05:15 +0100
  * cleanup: const\_Item->real\_item()
* [Revision #cce76fef38](https://github.com/MariaDB/server/commit/cce76fef38)\
  2022-11-03 19:17:25 +0100
  * ADD CONSTRAINT IF NOT EXISTS didn't work in SP
* [Revision #a5eff044cb](https://github.com/MariaDB/server/commit/a5eff044cb)\
  2022-11-03 18:31:42 +0100
  * [MDEV-22602](https://jira.mariadb.org/browse/MDEV-22602) Disable UPDATE CASCADE for SQL constraints
* [Revision #107d54600e](https://github.com/MariaDB/server/commit/107d54600e)\
  2023-01-17 14:06:04 +0200
  * Stabilize tests
* [Revision #9ec475c376](https://github.com/MariaDB/server/commit/9ec475c376)\
  2023-01-11 17:28:22 +0100
  * [MDEV-29171](https://jira.mariadb.org/browse/MDEV-29171) changing the value of wsrep\_gtid\_domain\_id with full cluster restart fails on some nodes
* Merge [Revision #179c283372](https://github.com/MariaDB/server/commit/179c283372) 2023-01-14 08:25:57 +0200 - Merge branch 10.4 into 10.5
* [Revision #981a6b7044](https://github.com/MariaDB/server/commit/981a6b7044)\
  2023-01-12 22:31:18 +0200
  * [MDEV-30395](https://jira.mariadb.org/browse/MDEV-30395) Wrong result with semijoin and Federated as outer table
* [Revision #0595dd0f56](https://github.com/MariaDB/server/commit/0595dd0f56)\
  2023-01-12 18:45:40 +0200
  * [MDEV-30080](https://jira.mariadb.org/browse/MDEV-30080) Wrong result with LEFT JOINs involving constant tables
* Merge [Revision #73ecab3d26](https://github.com/MariaDB/server/commit/73ecab3d26) 2023-01-13 10:18:30 +0200 - Merge 10.4 into 10.5
* [Revision #7d1df207c4](https://github.com/MariaDB/server/commit/7d1df207c4)\
  2023-01-11 18:12:40 +0200
  * [MDEV-30373](https://jira.mariadb.org/browse/MDEV-30373) Wrong result with range access
* [Revision #17858e03a7](https://github.com/MariaDB/server/commit/17858e03a7)\
  2023-01-02 13:13:59 +0530
  * [MDEV-30179](https://jira.mariadb.org/browse/MDEV-30179) mariadb-backup --backup fails with FATAL ERROR: ... failed to copy datafile
* [Revision #cad33ded19](https://github.com/MariaDB/server/commit/cad33ded19)\
  2023-01-06 09:08:43 +1100
  * [MDEV-30344](https://jira.mariadb.org/browse/MDEV-30344): Without wsrep needs wsrep{,\_on}.h headers
* [Revision #d0a534d293](https://github.com/MariaDB/server/commit/d0a534d293)\
  2023-01-05 14:06:01 +0600
  * Fix synopses in mysys APIs
* [Revision #494acc1938](https://github.com/MariaDB/server/commit/494acc1938)\
  2023-01-04 19:16:45 +0200
  * [MDEV-30325](https://jira.mariadb.org/browse/MDEV-30325) Wrong result upon range query using index condition wrong result upon range query using index condition
* [Revision #f8f747547a](https://github.com/MariaDB/server/commit/f8f747547a)\
  2023-01-05 00:20:44 +0000
  * [MDEV-30344](https://jira.mariadb.org/browse/MDEV-30344) MTR tests fail when built without WSREP
* [Revision #d0603fc5ba](https://github.com/MariaDB/server/commit/d0603fc5ba)\
  2023-01-02 18:34:19 +0200
  * [MDEV-30240](https://jira.mariadb.org/browse/MDEV-30240) Wrong result upon aggregate function with SQL\_BUFFER\_RESULT
* Merge [Revision #8b9b4ab3f5](https://github.com/MariaDB/server/commit/8b9b4ab3f5) 2023-01-03 17:08:42 +0200 - Merge 10.4 into 10.5
* [Revision #c4938eafc5](https://github.com/MariaDB/server/commit/c4938eafc5)\
  2022-12-16 15:51:38 +0000
  * [MDEV-30275](https://jira.mariadb.org/browse/MDEV-30275): mariadb names rather than mysql names should be used
* [Revision #fd6f19d732](https://github.com/MariaDB/server/commit/fd6f19d732)\
  2023-01-02 18:58:19 +0600
  * Fix a typo in CmakeLists.txt
* [Revision #84539f6460](https://github.com/MariaDB/server/commit/84539f6460)\
  2022-12-19 16:23:30 -0600
  * header typo
* [Revision #8b18932ebc](https://github.com/MariaDB/server/commit/8b18932ebc)\
  2022-12-16 17:01:52 -0600
  * debian typos
* [Revision #b8f4b984f9](https://github.com/MariaDB/server/commit/b8f4b984f9)\
  2022-12-16 17:08:56 +0200
  * [MDEV-24685](https://jira.mariadb.org/browse/MDEV-24685) fixup: Remove srv\_n\_file\_io\_threads
* [Revision #d0cd49497f](https://github.com/MariaDB/server/commit/d0cd49497f)\
  2022-12-13 12:43:19 +0200
  * [MDEV-30118](https://jira.mariadb.org/browse/MDEV-30118) exception in ha\_maria::extra
* [Revision #92ff7bb63f](https://github.com/MariaDB/server/commit/92ff7bb63f)\
  2022-12-15 12:45:26 +0200
  * [MDEV-30227](https://jira.mariadb.org/browse/MDEV-30227) \[ERROR] \[FATAL] InnoDB: fdatasync() returned 9
* [Revision #03fee585c1](https://github.com/MariaDB/server/commit/03fee585c1)\
  2022-12-15 18:16:35 +1100
  * mtr: more galera disables - linked in [MDEV-30172](https://jira.mariadb.org/browse/MDEV-30172)
* [Revision #97c6cd9798](https://github.com/MariaDB/server/commit/97c6cd9798)\
  2022-12-15 08:48:34 +1100
  * Deb: debian-start.inc - do not quote exe variables
* [Revision #0f351b620a](https://github.com/MariaDB/server/commit/0f351b620a)\
  2022-12-14 19:35:19 +1100
  * rpm: server-post - use mariadb-install-db
* [Revision #9ee055a27f](https://github.com/MariaDB/server/commit/9ee055a27f)\
  2022-12-14 19:13:17 +1100
  * Deb: mariadb-server.postinst to use mariadb-install-db
* [Revision #40b62a93c6](https://github.com/MariaDB/server/commit/40b62a93c6)\
  2022-12-13 16:08:06 +1100
  * mariadb-install-db: use mariadb names
* [Revision #952af4a179](https://github.com/MariaDB/server/commit/952af4a179)\
  2022-12-12 16:23:30 +1100
  * Deb: MariaDB names as default for deb scripts
* [Revision #687657c270](https://github.com/MariaDB/server/commit/687657c270)\
  2022-12-14 11:08:35 +1100
  * [MDEV-30172](https://jira.mariadb.org/browse/MDEV-30172) re-disable galera tests
* Merge [Revision #1dc2f35598](https://github.com/MariaDB/server/commit/1dc2f35598) 2022-12-13 14:39:18 +0200 - Merge 10.4 into 10.5
* [Revision #da5d349935](https://github.com/MariaDB/server/commit/da5d349935)\
  2022-11-27 16:07:40 +0100
  * fix error on reading 5.5 tables with generated columns
* [Revision #cc78cd7d15](https://github.com/MariaDB/server/commit/cc78cd7d15)\
  2022-12-13 12:48:55 +1100
  * [MDEV-30172](https://jira.mariadb.org/browse/MDEV-30172) galera 10.5 test cleanup
* [Revision #58fecbebce](https://github.com/MariaDB/server/commit/58fecbebce)\
  2022-12-13 10:38:19 +1100
  * mtr: galera/galera\_3node disable failed tests
* Merge [Revision #72f1384c3a](https://github.com/MariaDB/server/commit/72f1384c3a) 2022-12-13 09:29:49 +1100 - Merge branch 10.4 into 10.5
* [Revision #851816532b](https://github.com/MariaDB/server/commit/851816532b)\
  2022-09-20 09:52:44 +0300
  * [MDEV-28834](https://jira.mariadb.org/browse/MDEV-28834): Add minimal support for Lintian version 2.115 and above
* [Revision #e748f5cc83](https://github.com/MariaDB/server/commit/e748f5cc83)\
  2022-11-30 21:18:47 +0200
  * Fixed a crash during automatic zerofill of moved Aria table
* [Revision #dd20a43c6c](https://github.com/MariaDB/server/commit/dd20a43c6c)\
  2022-12-02 11:54:35 +0530
  * [MDEV-30114](https://jira.mariadb.org/browse/MDEV-30114) Incremental prepare fails when innodb\_undo\_tablespaces > 0
* Merge [Revision #7487c313bc](https://github.com/MariaDB/server/commit/7487c313bc) 2022-12-01 11:04:58 +0200 - Merge 10.4 into 10.5
* [Revision #4eb8e51c26](https://github.com/MariaDB/server/commit/4eb8e51c26)\
  2022-11-30 13:10:52 +0200
  * Merge 10.4 into 10.5
* [Revision #1181564131](https://github.com/MariaDB/server/commit/1181564131)\
  2022-11-30 08:32:05 +0200
  * [MDEV-24412](https://jira.mariadb.org/browse/MDEV-24412): Disable the test on ./mtr --embedded
* [Revision #846112ce36](https://github.com/MariaDB/server/commit/846112ce36)\
  2022-11-30 06:57:32 +0200
  * [MDEV-24412](https://jira.mariadb.org/browse/MDEV-24412): Create a separate test
* [Revision #7b44d0ba57](https://github.com/MariaDB/server/commit/7b44d0ba57)\
  2022-11-29 05:21:03 +1100
  * [MDEV-23230](https://jira.mariadb.org/browse/MDEV-23230) wsrep files installed when built without WSREP (#2334)
* [Revision #bd694bb7b2](https://github.com/MariaDB/server/commit/bd694bb7b2)\
  2022-11-28 11:56:09 +0200
  * [MDEV-24412](https://jira.mariadb.org/browse/MDEV-24412) InnoDB: Upgrade after a crash is not supported
* [Revision #db14eb16f9](https://github.com/MariaDB/server/commit/db14eb16f9)\
  2022-11-28 11:34:22 +0200
  * [MDEV-30106](https://jira.mariadb.org/browse/MDEV-30106) InnoDB fails to validate the change buffer on startup
* [Revision #e0d672f30b](https://github.com/MariaDB/server/commit/e0d672f30b)\
  2022-11-28 11:34:00 +0200
  * [MDEV-30089](https://jira.mariadb.org/browse/MDEV-30089) Metrics not incremented for 1st iteration in buf\_LRU\_free\_from\_common\_LRU\_list()
* [Revision #183ca823bb](https://github.com/MariaDB/server/commit/183ca823bb)\
  2022-11-22 08:37:27 +1100
  * [MDEV-25417](https://jira.mariadb.org/browse/MDEV-25417): Remove innodb buffer pool load throttling
* [Revision #812443c251](https://github.com/MariaDB/server/commit/812443c251)\
  2022-09-27 10:31:24 -0600
  * [MDEV-29607](https://jira.mariadb.org/browse/MDEV-29607): binlog.binlog\_checkpoint fails in buildbot with result content mismatch
* [Revision #7919b14387](https://github.com/MariaDB/server/commit/7919b14387)\
  2022-11-25 17:28:09 +1100
  * Query cache: removed unused THD from few functions
* [Revision #7141c26094](https://github.com/MariaDB/server/commit/7141c26094)\
  2022-11-25 16:27:24 +1100
  * [MDEV-29760](https://jira.mariadb.org/browse/MDEV-29760): DROP DATABASE hangs when particular query cache is present
* [Revision #165564d3c3](https://github.com/MariaDB/server/commit/165564d3c3)\
  2022-11-23 17:34:05 +0200
  * [MDEV-30009](https://jira.mariadb.org/browse/MDEV-30009) InnoDB shutdown hangs when the change buffer is corrupted
* [Revision #9d388192c7](https://github.com/MariaDB/server/commit/9d388192c7)\
  2022-11-22 15:32:47 +0200
  * Cleanup: Say "mariadbd" instead of "mysqld" in InnoDB messages
* [Revision #cff9939d09](https://github.com/MariaDB/server/commit/cff9939d09)\
  2022-11-22 15:31:12 +0200
  * [MDEV-30068](https://jira.mariadb.org/browse/MDEV-30068) Confusing error message when encryption is not available on recovery
* [Revision #4e5e8166b4](https://github.com/MariaDB/server/commit/4e5e8166b4)\
  2022-11-21 17:55:35 +0200
  * [MDEV-19514](https://jira.mariadb.org/browse/MDEV-19514) fixup: Fix recovery with innodb\_change\_buffering\_debug=1
* Merge [Revision #faee972f18](https://github.com/MariaDB/server/commit/faee972f18) 2022-11-21 12:09:21 +0100 - Merge branch '10.4' into 10.5
* [Revision #c9ccd978eb](https://github.com/MariaDB/server/commit/c9ccd978eb)\
  2022-11-20 11:33:47 +0200
  * Fix clang -Winconsistent-missing-override
* Merge [Revision #5995ca3166](https://github.com/MariaDB/server/commit/5995ca3166) 2022-11-20 11:32:59 +0200 - Merge 10.4 into 10.5
* [Revision #41028d70f6](https://github.com/MariaDB/server/commit/41028d70f6)\
  2022-11-17 08:33:05 +0200
  * [MDEV-29982](https://jira.mariadb.org/browse/MDEV-29982) fixup: Relax the test
* [Revision #4b3b1eb810](https://github.com/MariaDB/server/commit/4b3b1eb810)\
  2022-11-16 13:46:24 +0100
  * [MDEV-25625](https://jira.mariadb.org/browse/MDEV-25625) Test sys\_vars.wsrep\_on\_without\_provider fails: mysqltest: At line 8: query 'SET GLOBAL wsrep\_on=ON' failed with wrong errno 1193: 'Unknown system variable 'wsrep\_on'', instead of 1210...
* [Revision #0b25551a61](https://github.com/MariaDB/server/commit/0b25551a61)\
  2022-11-15 16:56:13 +0200
  * [MDEV-29999](https://jira.mariadb.org/browse/MDEV-29999) innodb\_undo\_log\_truncate=ON is not crash safe
* [Revision #72c728feba](https://github.com/MariaDB/server/commit/72c728feba)\
  2022-11-15 11:34:00 +0400
  * [MDEV-29370](https://jira.mariadb.org/browse/MDEV-29370) Functions in packages are slow and seems to ignore deterministic
* [Revision #dc2741be52](https://github.com/MariaDB/server/commit/dc2741be52)\
  2022-11-14 15:40:28 +0200
  * [MDEV-29984](https://jira.mariadb.org/browse/MDEV-29984) innodb\_fast\_shutdown=0 fails to report change buffer merge progress
* [Revision #744b33c287](https://github.com/MariaDB/server/commit/744b33c287)\
  2022-11-14 14:12:20 +0200
  * Cleanup: Remove a useless header file
* [Revision #ee7fba1749](https://github.com/MariaDB/server/commit/ee7fba1749)\
  2022-11-14 14:01:37 +0200
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) fixup: Remove unused variables
* [Revision #e0e096faaa](https://github.com/MariaDB/server/commit/e0e096faaa)\
  2022-11-14 12:18:03 +0200
  * [MDEV-29982](https://jira.mariadb.org/browse/MDEV-29982) Improve the InnoDB log overwrite error message
* [Revision #2283f82de5](https://github.com/MariaDB/server/commit/2283f82de5)\
  2022-11-14 10:22:29 +0200
  * [MDEV-29905](https://jira.mariadb.org/browse/MDEV-29905) fixup: Remove some unnecessary code
* [Revision #5bf5e6eeca](https://github.com/MariaDB/server/commit/5bf5e6eeca)\
  2022-11-12 13:14:23 +0000
  * OS detection logic in my\_gethwaddr.c is backwards
* [Revision #7ee612c912](https://github.com/MariaDB/server/commit/7ee612c912)\
  2022-11-10 12:50:44 +0200
  * [MDEV-21174](https://jira.mariadb.org/browse/MDEV-21174) fixup: Remove mtr\_t::release\_page()
* [Revision #7aa8b209df](https://github.com/MariaDB/server/commit/7aa8b209df)\
  2022-11-08 14:26:38 +0000
  * [MDEV-29866](https://jira.mariadb.org/browse/MDEV-29866): Add RESET MASTER to clear possible remaining binlog from previous test
* [Revision #e616c9a0ef](https://github.com/MariaDB/server/commit/e616c9a0ef)\
  2022-11-08 10:19:16 +0000
  * [MDEV-28970](https://jira.mariadb.org/browse/MDEV-28970): Add RESET MASTER to clear possible remaining binlog from previous test
* Merge [Revision #3278c57917](https://github.com/MariaDB/server/commit/3278c57917) 2022-11-09 09:30:37 +0200 - Merge 10.4 into 10.5
* [Revision #b955f4eff7](https://github.com/MariaDB/server/commit/b955f4eff7)\
  2022-11-08 18:21:39 +0200
  * [MDEV-22512](https://jira.mariadb.org/browse/MDEV-22512): Re-enable the tests on 10.5
* Merge [Revision #a732d5e2ba](https://github.com/MariaDB/server/commit/a732d5e2ba) 2022-11-08 17:01:28 +0200 - Merge 10.4 into 10.5
* Merge [Revision #fe330b63fe](https://github.com/MariaDB/server/commit/fe330b63fe) 2022-11-07 16:14:35 +0100 - Merge branch '10.5' into bb-10.5-release
* [Revision #9201cda37c](https://github.com/MariaDB/server/commit/9201cda37c)\
  2022-11-07 09:18:20 -0500
  * bump the VERSION
* [Revision #ab81aefef6](https://github.com/MariaDB/server/commit/ab81aefef6)\
  2022-10-26 20:30:47 -0400
  * Fix building my\_gethwaddr() on OpenBSD - part for 10.5 and newer

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
