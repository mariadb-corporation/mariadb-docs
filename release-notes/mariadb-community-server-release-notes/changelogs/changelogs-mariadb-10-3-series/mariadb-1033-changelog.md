# MariaDB 10.3.3 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/release-notes-mariadb-10-3-series/mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.3)[Release Notes](../../old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md)[Changelog](mariadb-1033-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 23 Dec 2017

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #52c40b406d](https://github.com/MariaDB/server/commit/52c40b406d)\
  2017-12-22 22:12:52 +0200
  * Initialize MYSQL\_LOCK->flags variable
* [Revision #1d9fd4faec](https://github.com/MariaDB/server/commit/1d9fd4faec)\
  2017-12-22 15:03:24 +0200
  * Fixed compiler warnings in guess\_malloc\_library
* [Revision #d9e90292eb](https://github.com/MariaDB/server/commit/d9e90292eb)\
  2017-12-22 14:56:39 +0200
  * Fixed failures in innodb tests caused by not flushed restart
* [Revision #9cc7789e90](https://github.com/MariaDB/server/commit/9cc7789e90)\
  2017-12-22 14:56:09 +0200
  * MDEV 13679 Enabled sequences to be used in DEFAULT
* [Revision #5b4c8469d5](https://github.com/MariaDB/server/commit/5b4c8469d5)\
  2017-12-22 14:34:41 +0200
  * Added CHECK\_FIELD\_EXPRESSION
* [Revision #139e8afc2c](https://github.com/MariaDB/server/commit/139e8afc2c)\
  2017-12-22 14:16:21 +0200
  * Re-enable 'S' for --debug (sf\_sanity checking for each call)
* [Revision #1464f4808c](https://github.com/MariaDB/server/commit/1464f4808c)\
  2017-12-21 18:04:59 +0400
  * [MDEV-14477](https://jira.mariadb.org/browse/MDEV-14477) InnoDB update\_time is wrongly updated after partial rollback or internal COMMIT
* [Revision #37f5569909](https://github.com/MariaDB/server/commit/37f5569909)\
  2017-11-04 19:14:34 +0100
  * @@in\_predicate\_conversion\_threshold
* Merge [Revision #9ec2479778](https://github.com/MariaDB/server/commit/9ec2479778) 2017-12-21 08:36:02 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #40f4525f43](https://github.com/MariaDB/server/commit/40f4525f43)\
  2017-12-21 08:20:31 +0200
  * [MDEV-14585](https://jira.mariadb.org/browse/MDEV-14585): Adjust the innodb.innodb-alter-tempfile test case
* Merge [Revision #1ec8d45c4d](https://github.com/MariaDB/server/commit/1ec8d45c4d) 2017-12-20 23:18:41 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #69e88de0fe](https://github.com/MariaDB/server/commit/69e88de0fe)\
  2017-12-20 23:15:44 +0200
  * [MDEV-14585](https://jira.mariadb.org/browse/MDEV-14585): Adjust the innodb.alter\_crash test case
* [Revision #b4165985c9](https://github.com/MariaDB/server/commit/b4165985c9)\
  2017-12-20 22:47:01 +0200
  * [MDEV-14585](https://jira.mariadb.org/browse/MDEV-14585) Automatically remove #sql- tables in InnoDB dictionary during recovery
* Merge [Revision #2534b5cb99](https://github.com/MariaDB/server/commit/2534b5cb99) 2017-12-20 22:36:51 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #0bc36758ba](https://github.com/MariaDB/server/commit/0bc36758ba)\
  2017-12-20 22:19:47 +0200
  * [MDEV-14717](https://jira.mariadb.org/browse/MDEV-14717) RENAME TABLE in InnoDB is not crash-safe
* [Revision #b4e5d5e2db](https://github.com/MariaDB/server/commit/b4e5d5e2db)\
  2017-12-20 01:30:12 +0200
  * Updated result for alter\_crash
* Merge [Revision #0436a0ff3c](https://github.com/MariaDB/server/commit/0436a0ff3c) 2017-12-19 17:28:22 +0200 - Merge bb-10.2-ext into 10.3
* [Revision #88aff5f471](https://github.com/MariaDB/server/commit/88aff5f471)\
  2017-12-18 13:38:36 +0200
  * Follow-up to [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407) innodb.drop\_table\_background failed in buildbot with "Tablespace for table exists"
* Merge [Revision #028e91f380](https://github.com/MariaDB/server/commit/028e91f380) 2017-12-19 17:12:14 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #8d70097c21](https://github.com/MariaDB/server/commit/8d70097c21) 2017-12-19 16:48:28 +0200 - Merge 10.1 to 10.2
* [Revision #252e690c85](https://github.com/MariaDB/server/commit/252e690c85)\
  2017-12-19 16:13:35 +0200
  * Fix galera.view test case crash.
* [Revision #ce4cdfa0f8](https://github.com/MariaDB/server/commit/ce4cdfa0f8)\
  2017-12-19 08:56:31 +1100
  * [MDEV-13809](https://jira.mariadb.org/browse/MDEV-13809): \[service] should \[Service] in systemd service files
* [Revision #64f1fab068](https://github.com/MariaDB/server/commit/64f1fab068)\
  2017-12-19 10:24:50 +1100
  * [MDEV-12128](https://jira.mariadb.org/browse/MDEV-12128): systemd - add Documentation= directives
* Merge [Revision #09c5bbf471](https://github.com/MariaDB/server/commit/09c5bbf471) 2017-12-18 20:05:50 +0200 - Merge 10.0 into 10.1
* [Revision #40088bfc7e](https://github.com/MariaDB/server/commit/40088bfc7e)\
  2017-12-18 19:46:23 +0200
  * [MDEV-13407](https://jira.mariadb.org/browse/MDEV-13407) innodb.drop\_table\_background failed in buildbot with "Tablespace for table exists"
* [Revision #03e91ce324](https://github.com/MariaDB/server/commit/03e91ce324)\
  2017-12-15 16:38:46 +0100
  * [MDEV-14641](https://jira.mariadb.org/browse/MDEV-14641) Incompatible key or row definition between the MariaDB .frm file and the information in the storage engine
* [Revision #c1e5fef05d](https://github.com/MariaDB/server/commit/c1e5fef05d)\
  2017-12-18 11:25:38 +0400
  * [MDEV-14008](https://jira.mariadb.org/browse/MDEV-14008) Assertion failing: \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())
* [Revision #682c3bfd25](https://github.com/MariaDB/server/commit/682c3bfd25)\
  2016-11-21 16:20:10 -0500
  * [MDEV-10442](https://jira.mariadb.org/browse/MDEV-10442): "Address already in use" on restart
* [Revision #91daf8819c](https://github.com/MariaDB/server/commit/91daf8819c)\
  2017-12-12 17:47:06 +0100
  * MW-416
* [Revision #beabe6b216](https://github.com/MariaDB/server/commit/beabe6b216)\
  2017-10-16 19:33:06 +0200
  * [MDEV-13969](https://jira.mariadb.org/browse/MDEV-13969) sst mysqldump and xtrabackup-v2 handle WSREP\_SST\_OPT\_CONF incorrectly
* [Revision #1c2f59f7fb](https://github.com/MariaDB/server/commit/1c2f59f7fb)\
  2017-10-01 15:45:51 +0200
  * [MDEV-13969](https://jira.mariadb.org/browse/MDEV-13969) sst mysqldump and xtrabackup-v2 handle WSREP\_SST\_OPT\_CONF incorrectly
* [Revision #f32063c513](https://github.com/MariaDB/server/commit/f32063c513)\
  2017-12-18 15:37:06 +0000
  * [MDEV-13620](https://jira.mariadb.org/browse/MDEV-13620) - improve help message for 'plugin-dir' and 'plugin-load' options.
* [Revision #6ee9cba745](https://github.com/MariaDB/server/commit/6ee9cba745)\
  2017-12-18 15:21:50 +0400
  * [MDEV-10486](https://jira.mariadb.org/browse/MDEV-10486) MariaDB 10.x does not update rows\_examined in performance\_schema tables.
* [Revision #ef9e78c9d4](https://github.com/MariaDB/server/commit/ef9e78c9d4)\
  2017-12-13 11:52:53 +0100
  * [MDEV-14524](https://jira.mariadb.org/browse/MDEV-14524) TokuDB is unable to be built on Linux
* [Revision #079c359971](https://github.com/MariaDB/server/commit/079c359971)\
  2017-12-19 11:49:40 +0200
  * [MDEV-14629](https://jira.mariadb.org/browse/MDEV-14629): failing assertion when a user-defined variable is defined by the recursive CTE
* [Revision #06f0b23a78](https://github.com/MariaDB/server/commit/06f0b23a78)\
  2017-12-17 17:53:53 +0200
  * Fixed memory leak in my\_rocks
* [Revision #4bd63bd551](https://github.com/MariaDB/server/commit/4bd63bd551)\
  2017-12-16 17:45:55 +0300
  * [MDEV-14679](https://jira.mariadb.org/browse/MDEV-14679): RocksdB plugin fails to load with "Loading of unknown plugin ROCKSDB\_CFSTATS
* [Revision #7380376370](https://github.com/MariaDB/server/commit/7380376370)\
  2017-12-16 16:44:33 +0300
  * [MDEV-14293](https://jira.mariadb.org/browse/MDEV-14293): MyRocks lacks basic functionality
* [Revision #64b11e61b5](https://github.com/MariaDB/server/commit/64b11e61b5)\
  2017-12-15 17:59:33 +0300
  * [MDEV-14293](https://jira.mariadb.org/browse/MDEV-14293): MyRocks lacks basic functionality
* [Revision #a9a4089175](https://github.com/MariaDB/server/commit/a9a4089175)\
  2017-12-14 13:47:38 +0200
  * Plug a small memory leak in mariadb-backup --backup
* [Revision #8ed78cf7f9](https://github.com/MariaDB/server/commit/8ed78cf7f9)\
  2017-12-18 12:24:02 +0400
  * xa.test fixed to be thread-stable.
* [Revision #7fd7805574](https://github.com/MariaDB/server/commit/7fd7805574)\
  2017-12-11 19:20:37 +0000
  * [MDEV-14315](https://jira.mariadb.org/browse/MDEV-14315) -- Reflect use of tcmalloc in a system variable and error log
* [Revision #0acac4fe5f](https://github.com/MariaDB/server/commit/0acac4fe5f)\
  2017-12-18 01:55:40 +0400
  * [MDEV-14593](https://jira.mariadb.org/browse/MDEV-14593) human-readable XA RECOVER.
* [Revision #0fd3def284](https://github.com/MariaDB/server/commit/0fd3def284)\
  2017-12-19 15:36:36 +0200
  * Remove MLOG\_UNDO\_ERASE\_END
* [Revision #9ee8917dfd](https://github.com/MariaDB/server/commit/9ee8917dfd)\
  2017-12-19 15:34:02 +0200
  * Replace MLOG\_UNDO\_INSERT with MLOG\_WRITE\_STRING, MLOG\_2BYTES
* [Revision #ccb3550221](https://github.com/MariaDB/server/commit/ccb3550221)\
  2017-12-19 14:37:48 +0200
  * Replace MLOG\_UNDO\_INIT with MLOG\_2BYTES, MLOG\_4BYTES
* [Revision #3464b67025](https://github.com/MariaDB/server/commit/3464b67025)\
  2017-12-05 12:39:37 +1100
  * mysys: handle T, P, E suffixs
* [Revision #22f2b39c14](https://github.com/MariaDB/server/commit/22f2b39c14)\
  2017-12-06 00:36:17 +0300
  * fix data races in rwlock
* [Revision #ca9ed393ef](https://github.com/MariaDB/server/commit/ca9ed393ef)\
  2017-12-18 22:59:05 +0200
  * [MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073). rpl.perf\_buildin\_semisync\_issue40 is corrected to expect the Rpl\_semi\_sync\_master\_clients value of 1 (ll.307..). Explicit sleeps are converted to wait\_xyz.
* [Revision #3791d0cfcf](https://github.com/MariaDB/server/commit/3791d0cfcf)\
  2017-12-17 21:25:48 +0200
  * Test result changed
* [Revision #86308aa995](https://github.com/MariaDB/server/commit/86308aa995)\
  2017-12-13 02:23:57 +0200
  * [MDEV-14579](https://jira.mariadb.org/browse/MDEV-14579): New tests for condition pushdown into materialized views/defined tables defined with INTERSECT/EXCEPT added
* [Revision #529120e1cb](https://github.com/MariaDB/server/commit/529120e1cb)\
  2017-11-27 21:06:17 +0200
  * [MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073). This patch is a followup of the previous one to convert the trailing underscore identifier to mariadb standard. For identifier representing class private members the underscore is replaced with a `m_` prefix. Otherwise `_` is just removed.
* [Revision #f279d3c43a](https://github.com/MariaDB/server/commit/f279d3c43a)\
  2017-11-25 18:54:42 +0200
  * [MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073). This part converts the Ali patch\`s identifiers to the MariaDB standard. Also some renaming is done as well as white spaces removal.
* [Revision #6a84e3407d](https://github.com/MariaDB/server/commit/6a84e3407d)\
  2017-11-27 13:00:08 +0200
  * [MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073). This patch replaces semisync's native function\_enter,exit and its custom trace faciltiy with standard DBUG\_ based equivalents.
* [Revision #c0ea3056b6](https://github.com/MariaDB/server/commit/c0ea3056b6)\
  2017-11-22 23:38:16 +0200
  * [MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073). This is a part with a new test (refined Ali's one) and affected result files.
* [Revision #74b35b6874](https://github.com/MariaDB/server/commit/74b35b6874)\
  2017-11-22 19:34:42 +0200
  * [MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073). This part patch weeds out RUN\_HOOK from the server as semisync is defined statically. Consequently the observer interfaces are removed as well.
* [Revision #e972125f11](https://github.com/MariaDB/server/commit/e972125f11)\
  2017-11-22 17:10:34 +0200
  * [MDEV-13073](https://jira.mariadb.org/browse/MDEV-13073) This part merges the Ali semisync related changes and specifically the ack receiving functionality. Semisync is turned to be static instead of plugin so its functions are invoked at the same points as RUN\_HOOKS. The RUN\_HOOKS and the observer interface remain to be removed by later patch.
* [Revision #abceaa7542](https://github.com/MariaDB/server/commit/abceaa7542)\
  2017-10-26 19:14:37 +0300
  * Optimize RUN\_HOOK() call
* [Revision #13770edbcb](https://github.com/MariaDB/server/commit/13770edbcb)\
  2017-10-26 17:20:20 +0300
  * Changed from using LOCK\_log to LOCK\_binlog\_end\_pos for binary log
* [Revision #ea37c129f9](https://github.com/MariaDB/server/commit/ea37c129f9)\
  2017-10-26 12:46:45 +0300
  * Removed not used lock argument from read\_log\_event
* [Revision #2e53b96a0a](https://github.com/MariaDB/server/commit/2e53b96a0a)\
  2017-10-25 11:07:44 +0300
  * Moved semisync from a plugin to normal server
* [Revision #77030649fb](https://github.com/MariaDB/server/commit/77030649fb)\
  2017-12-13 15:30:08 +0900
  * Fix typos in some comments
* [Revision #d91d1c8dbc](https://github.com/MariaDB/server/commit/d91d1c8dbc)\
  2017-12-14 09:19:53 +0000
  * Test cleanup related to [MDEV-12501](https://jira.mariadb.org/browse/MDEV-12501)
* [Revision #4ef86e36e8](https://github.com/MariaDB/server/commit/4ef86e36e8)\
  2017-12-14 12:39:12 +0000
  * A fix of mtr bug uncovered by [MDEV-12501](https://jira.mariadb.org/browse/MDEV-12501): passing of parameters in rebootstrap
* [Revision #34f2f4fa43](https://github.com/MariaDB/server/commit/34f2f4fa43)\
  2017-12-15 13:50:30 +0200
  * [MDEV-14660](https://jira.mariadb.org/browse/MDEV-14660) Assertion failure in lock\_move\_rec\_list\_start() after instant ADD COLUMN
* [Revision #e4efbfd904](https://github.com/MariaDB/server/commit/e4efbfd904)\
  2017-12-14 11:43:54 +0200
  * Remove dead code lock\_remove\_recovered\_trx\_record\_locks()
* [Revision #2b67b7cb08](https://github.com/MariaDB/server/commit/2b67b7cb08)\
  2017-12-13 11:14:13 +0300
  * Misc: updated .gitignore
* [Revision #0bc3c0fbc8](https://github.com/MariaDB/server/commit/0bc3c0fbc8)\
  2017-12-14 19:17:27 +0530
  * mysqldump fix for invisible column
* [Revision #c90db2c8be](https://github.com/MariaDB/server/commit/c90db2c8be)\
  2017-12-07 13:58:18 +0530
  * BuildBot bug fix for invisible columns
* [Revision #022b163ac8](https://github.com/MariaDB/server/commit/022b163ac8)\
  2017-12-03 15:37:32 +0100
  * Add tests for system and completely invisible columns
* [Revision #84726906c9](https://github.com/MariaDB/server/commit/84726906c9)\
  2017-12-02 07:00:04 +0530
  * [MDEV-10177](https://jira.mariadb.org/browse/MDEV-10177) Invisible Columns and Invisible Index
* Merge [Revision #866ccc8890](https://github.com/MariaDB/server/commit/866ccc8890) 2017-12-14 11:34:30 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #1b5f0cbd46](https://github.com/MariaDB/server/commit/1b5f0cbd46) 2017-12-14 09:53:19 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #8063804943](https://github.com/MariaDB/server/commit/8063804943)\
  2017-12-13 23:14:54 +0200
  * Re-remove the file kill\_and\_restart\_mysqld.inc
* Merge [Revision #ece9c54e10](https://github.com/MariaDB/server/commit/ece9c54e10) 2017-12-13 23:14:15 +0200 - Merge 10.1 into 10.2
* Merge [Revision #7be5b6f0e6](https://github.com/MariaDB/server/commit/7be5b6f0e6) 2017-12-13 23:04:30 +0200 - Merge 10.0 into 10.1
* [Revision #9d76b27498](https://github.com/MariaDB/server/commit/9d76b27498)\
  2017-12-13 22:30:13 +0200
  * Follow-up fix for [MDEV-12352](https://jira.mariadb.org/browse/MDEV-12352): Plug a memory leak
* [Revision #e9cc486c97](https://github.com/MariaDB/server/commit/e9cc486c97)\
  2017-12-13 20:42:53 +0200
  * Fix a typo: schedule, scheduling
* [Revision #2fe990df9f](https://github.com/MariaDB/server/commit/2fe990df9f)\
  2017-12-13 20:41:32 +0200
  * Fix the grammar of an error message
* Merge [Revision #46305b006b](https://github.com/MariaDB/server/commit/46305b006b) 2017-12-13 19:12:16 +0200 - Merge 10.0 into 10.1
* [Revision #b1977a39de](https://github.com/MariaDB/server/commit/b1977a39de)\
  2017-12-13 18:56:22 +0200
  * [MDEV-12323](https://jira.mariadb.org/browse/MDEV-12323) Rollback progress log messages during crash recovery are intermixed with unrelated log messages
* [Revision #08d0ea1fcf](https://github.com/MariaDB/server/commit/08d0ea1fcf)\
  2017-12-13 18:53:46 +0200
  * Follow-up to [MDEV-11027](https://jira.mariadb.org/browse/MDEV-11027): Use recv\_sys\_t::report()
* [Revision #b46fa627ca](https://github.com/MariaDB/server/commit/b46fa627ca)\
  2017-12-13 18:02:09 +0200
  * [MDEV-12352](https://jira.mariadb.org/browse/MDEV-12352) InnoDB shutdown should not be blocked by a large transaction rollback
* [Revision #6559ba71a5](https://github.com/MariaDB/server/commit/6559ba71a5)\
  2017-12-13 16:18:08 +0200
  * [MDEV-13797](https://jira.mariadb.org/browse/MDEV-13797) InnoDB may hang if shutdown is initiated soon after startup while rolling back recovered incomplete transactions
* [Revision #b93a87f186](https://github.com/MariaDB/server/commit/b93a87f186)\
  2017-12-13 12:52:28 +0200
  * Try to prevent sporadic test failures
* Merge [Revision #ce07d09fd3](https://github.com/MariaDB/server/commit/ce07d09fd3) 2017-12-12 19:28:26 +0200 - Merge 10.0 into 10.1
* [Revision #622466644d](https://github.com/MariaDB/server/commit/622466644d)\
  2017-11-20 11:00:44 +0200
  * mysql\_uprade --help and man page fixes
* [Revision #d8ccc61f76](https://github.com/MariaDB/server/commit/d8ccc61f76)\
  2017-11-16 14:03:02 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #93326ef051](https://github.com/MariaDB/server/commit/93326ef051)\
  2017-11-16 13:21:07 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #923ea5dbf6](https://github.com/MariaDB/server/commit/923ea5dbf6)\
  2017-11-16 13:18:22 +0200
  * [MDEV-9663](https://jira.mariadb.org/browse/MDEV-9663): InnoDB assertion failure: \*cursor->index->name == TEMP\_INDEX\_PREFIX
* [Revision #02e35ef5f2](https://github.com/MariaDB/server/commit/02e35ef5f2)\
  2017-11-15 15:52:03 +0400
  * [MDEV-12681](https://jira.mariadb.org/browse/MDEV-12681) Wrong VIEW results for CHAR(0xDF USING latin1)
* [Revision #ea1739f90d](https://github.com/MariaDB/server/commit/ea1739f90d)\
  2017-11-14 11:29:52 +0300
  * removed garbase struct member
* [Revision #2913f615f0](https://github.com/MariaDB/server/commit/2913f615f0)\
  2017-11-13 16:30:02 +0100
  * [MDEV-8949](https://jira.mariadb.org/browse/MDEV-8949): COLUMN\_CREATE unicode name breakage
* [Revision #c0e10f375a](https://github.com/MariaDB/server/commit/c0e10f375a)\
  2017-11-10 09:07:45 +0200
  * Fix a -Wimplicit-fallthrough warning
* [Revision #de76cbdcb0](https://github.com/MariaDB/server/commit/de76cbdcb0)\
  2017-12-09 11:21:56 +0200
  * Add Galera test cases that fail to disabled.
* [Revision #feb8296ee6](https://github.com/MariaDB/server/commit/feb8296ee6)\
  2017-12-09 11:21:23 +0200
  * [MDEV-14401](https://jira.mariadb.org/browse/MDEV-14401): Stored procedure that declares a handler that catches ER\_LOCK\_DEADLOCK error causes thd->is\_error() assertion
* [Revision #e66bb57267](https://github.com/MariaDB/server/commit/e66bb57267)\
  2017-12-09 11:20:46 +0200
  * [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837): WSREP: BF lock wait long
* [Revision #1374f958c1](https://github.com/MariaDB/server/commit/1374f958c1)\
  2017-12-07 17:22:24 +0200
  * Fixed failing tokudb tests
* [Revision #58eb4e5db9](https://github.com/MariaDB/server/commit/58eb4e5db9)\
  2017-12-13 14:16:15 +0200
  * [MDEV-14422](https://jira.mariadb.org/browse/MDEV-14422) Assertion failure in trx\_purge\_run() on shutdown
* [Revision #0e69d0b094](https://github.com/MariaDB/server/commit/0e69d0b094)\
  2017-12-13 00:29:44 +0200
  * [MDEV-14607](https://jira.mariadb.org/browse/MDEV-14607) storage\_engine-rocksdb.type\_bit\_indexes fails after latest pushes
* [Revision #a3476a5de2](https://github.com/MariaDB/server/commit/a3476a5de2)\
  2017-12-12 20:00:28 +0200
  * Skip btr\_search\_latches\[] in SHOW ENGINE INNODB STATUS
* [Revision #701e22d5cd](https://github.com/MariaDB/server/commit/701e22d5cd)\
  2017-12-13 15:08:16 +0400
  * Removing a dead code in sql\_load.cc
* [Revision #a53e087ea9](https://github.com/MariaDB/server/commit/a53e087ea9)\
  2017-12-13 13:22:45 +0400
  * [MDEV-14628](https://jira.mariadb.org/browse/MDEV-14628) Wrong autoinc value assigned by LOAD XML in the NO\_AUTO\_VALUE\_ON\_ZERO mode
* [Revision #d2f557fa3d](https://github.com/MariaDB/server/commit/d2f557fa3d)\
  2017-12-12 15:42:22 +0200
  * Fixed crash in show processlist with blocked connection
* [Revision #159a6c2e60](https://github.com/MariaDB/server/commit/159a6c2e60)\
  2017-12-12 22:53:38 +0400
  * [MDEV-14505](https://jira.mariadb.org/browse/MDEV-14505) - Threads\_running becomes scalability bottleneck
* Merge [Revision #751e0f6b1e](https://github.com/MariaDB/server/commit/751e0f6b1e) 2017-12-12 10:58:39 -0800 - Merge remote-tracking branch 'origin/bb-10.3-[MDEV-14568](https://jira.mariadb.org/browse/MDEV-14568)' into 10.3
* [Revision #04a4b21508](https://github.com/MariaDB/server/commit/04a4b21508)\
  2017-12-05 11:18:47 -0800
  * [MDEV-14568](https://jira.mariadb.org/browse/MDEV-14568): Server does not shut down with SIGTERM after installing Spider 3.3 plugin
* [Revision #364f42d091](https://github.com/MariaDB/server/commit/364f42d091)\
  2017-12-12 20:03:42 +0300
  * Scripts: --tail-lines option for mtr (#493)
* [Revision #d4a4185451](https://github.com/MariaDB/server/commit/d4a4185451)\
  2017-12-12 15:04:29 +0200
  * MDEV Assertion \`partition\_id == m\_extra\_cache\_part\_id' failed in ha\_partition::late\_extra\_no\_cache
* Merge [Revision #0edd395e8d](https://github.com/MariaDB/server/commit/0edd395e8d) 2017-12-12 13:32:49 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #0628123617](https://github.com/MariaDB/server/commit/0628123617) 2017-12-12 13:27:35 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #86c69263a4](https://github.com/MariaDB/server/commit/86c69263a4)\
  2017-12-12 13:31:41 +0300
  * [MDEV-14389](https://jira.mariadb.org/browse/MDEV-14389): MyRocks and NOPAD collations
* [Revision #ccf22b8025](https://github.com/MariaDB/server/commit/ccf22b8025)\
  2017-12-12 13:26:57 +0200
  * Post-merge fix: Adjust message codes in results
* [Revision #c2c4c1952d](https://github.com/MariaDB/server/commit/c2c4c1952d)\
  2017-12-12 09:57:40 +0200
  * Remove an unused error code
* Merge [Revision #34841d2305](https://github.com/MariaDB/server/commit/34841d2305) 2017-12-12 09:35:18 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #a285e68018](https://github.com/MariaDB/server/commit/a285e68018) 2017-12-12 09:15:17 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #e12f77a7e3](https://github.com/MariaDB/server/commit/e12f77a7e3)\
  2017-12-12 01:33:03 +0300
  * [MDEV-14389](https://jira.mariadb.org/browse/MDEV-14389): MyRocks and NOPAD collations
* [Revision #8695c816e7](https://github.com/MariaDB/server/commit/8695c816e7)\
  2017-12-11 15:57:21 +0200
  * Wrap atomic\_compare\_exchange\_n() as valid C
* Merge [Revision #e312a407b8](https://github.com/MariaDB/server/commit/e312a407b8) 2017-12-11 15:06:11 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #13b9ec651a](https://github.com/MariaDB/server/commit/13b9ec651a)\
  2017-12-11 14:39:53 +0200
  * [MDEV-14589](https://jira.mariadb.org/browse/MDEV-14589) InnoDB should not lock a delete-marked record
* [Revision #434c9e6f0e](https://github.com/MariaDB/server/commit/434c9e6f0e)\
  2017-12-11 13:55:05 +0200
  * [MDEV-14614](https://jira.mariadb.org/browse/MDEV-14614) InnoDB: Failing assertion in dict\_stats\_rename\_table()
* [Revision #1e6ac94451](https://github.com/MariaDB/server/commit/1e6ac94451)\
  2017-12-11 12:37:19 +0200
  * Correct the comment of row\_vers\_impl\_x\_locked()
* [Revision #bdeb27a000](https://github.com/MariaDB/server/commit/bdeb27a000)\
  2017-12-10 19:22:48 +0300
  * [MDEV-14123](https://jira.mariadb.org/browse/MDEV-14123): .rocksdb folder may break workflow which re-create data directory
* [Revision #ddc1d6904a](https://github.com/MariaDB/server/commit/ddc1d6904a)\
  2017-12-08 16:41:51 +0300
  * [MDEV-14123](https://jira.mariadb.org/browse/MDEV-14123): .rocksdb folder may break workflow which re-create data directory
* [Revision #b8a0373ed2](https://github.com/MariaDB/server/commit/b8a0373ed2)\
  2017-12-08 16:13:03 +0300
  * [MDEV-14123](https://jira.mariadb.org/browse/MDEV-14123): ".rocksdb folder may break workflow", and other MDEVs
* [Revision #40eee1da17](https://github.com/MariaDB/server/commit/40eee1da17)\
  2017-12-11 10:06:32 +0200
  * [MDEV-14614](https://jira.mariadb.org/browse/MDEV-14614) InnoDB: Failing assertion: trx->error\_state == DB\_SUCCESS or lock wait timeout upon saving statistics
* [Revision #86beb08774](https://github.com/MariaDB/server/commit/86beb08774)\
  2017-12-11 09:31:28 +0200
  * Remove an unnecessary dependency on persistent statistics
* [Revision #0af52734a7](https://github.com/MariaDB/server/commit/0af52734a7)\
  2017-12-08 16:36:19 +0200
  * Remove the unused function row\_is\_magic\_monitor\_table()
* [Revision #51bc407403](https://github.com/MariaDB/server/commit/51bc407403)\
  2017-12-08 16:31:54 +0200
  * Remove dead code for "InnoDB table(space) monitor"
* [Revision #927dd9f355](https://github.com/MariaDB/server/commit/927dd9f355)\
  2017-12-08 21:35:29 +0400
  * Fixed LF\_BACKOFF calls
* [Revision #3945049809](https://github.com/MariaDB/server/commit/3945049809)\
  2017-12-08 15:18:39 +0200
  * Remove space\_name\_list\_t
* Merge [Revision #094b0f869b](https://github.com/MariaDB/server/commit/094b0f869b) 2017-12-08 16:00:10 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #bf96310657](https://github.com/MariaDB/server/commit/bf96310657)\
  2017-12-08 13:10:41 +0000
  * Fix warnings
* [Revision #2662228d18](https://github.com/MariaDB/server/commit/2662228d18)\
  2017-12-08 13:33:11 +0200
  * Fix test failures.
* [Revision #0e5eef886a](https://github.com/MariaDB/server/commit/0e5eef886a)\
  2017-12-08 13:19:19 +0400
  * [MDEV-14350](https://jira.mariadb.org/browse/MDEV-14350) Index use with collation utf8mb4\_unicode\_nopad\_ci on LIKE pattern with wrong results
* [Revision #38908aaf81](https://github.com/MariaDB/server/commit/38908aaf81)\
  2017-12-08 10:07:11 +0200
  * Fix failing mtr tests
* [Revision #c2118a08b1](https://github.com/MariaDB/server/commit/c2118a08b1)\
  2017-12-07 21:28:00 +0200
  * Move all kill mutex protection to LOCK\_thd\_kill
* [Revision #3574f9c7bc](https://github.com/MariaDB/server/commit/3574f9c7bc)\
  2017-12-07 21:10:51 +0200
  * Updated MW-388.result file
* [Revision #7891a713da](https://github.com/MariaDB/server/commit/7891a713da)\
  2017-12-07 15:15:22 +0200
  * Don't wait too long in SHOW PROCESSLIST
* [Revision #b3346c2f41](https://github.com/MariaDB/server/commit/b3346c2f41)\
  2017-12-07 15:03:59 +0200
  * Restore LF\_BACKOFF
* [Revision #07e9ff1fe1](https://github.com/MariaDB/server/commit/07e9ff1fe1)\
  2017-11-11 22:27:03 +0200
  * [MDEV-14378](https://jira.mariadb.org/browse/MDEV-14378) In ALGORITHM=INPLACE, use a common name for the intermediate tables or partitions
* Merge [Revision #0a02c1a667](https://github.com/MariaDB/server/commit/0a02c1a667) 2017-12-08 10:02:28 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #dfafe15abb](https://github.com/MariaDB/server/commit/dfafe15abb)\
  2017-12-08 09:53:11 +0200
  * [MDEV-14606](https://jira.mariadb.org/browse/MDEV-14606) Assertion failure on IMPORT TABLESPACE
* [Revision #578b26598a](https://github.com/MariaDB/server/commit/578b26598a)\
  2017-12-08 01:15:10 +0300
  * [MDEV-14607](https://jira.mariadb.org/browse/MDEV-14607): storage\_engine-rocksdb.type\_bit\_indexes fails after latest pushes
* [Revision #4d016e6ed2](https://github.com/MariaDB/server/commit/4d016e6ed2)\
  2017-12-07 12:59:32 +0200
  * Add Galera test cases that fail to disabled.
* [Revision #ba576c5b78](https://github.com/MariaDB/server/commit/ba576c5b78)\
  2017-12-07 12:43:26 +0200
  * [MDEV-14401](https://jira.mariadb.org/browse/MDEV-14401): Stored procedure that declares a handler that catches ER\_LOCK\_DEADLOCK error causes thd->is\_error() assertion
* [Revision #da3a3a68df](https://github.com/MariaDB/server/commit/da3a3a68df)\
  2017-12-07 12:26:29 +0200
  * [MDEV-12837](https://jira.mariadb.org/browse/MDEV-12837): WSREP: BF lock wait long
* [Revision #3eaca005ff](https://github.com/MariaDB/server/commit/3eaca005ff)\
  2017-12-05 17:05:05 +0200
  * Ensure that mysqladmin also works with [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) + more
* [Revision #a61fbf87ed](https://github.com/MariaDB/server/commit/a61fbf87ed)\
  2017-12-08 09:44:53 +0400
  * Adding the -Wnon-virtual-dtor GCC/CLang flag in maintainer mode
* [Revision #08dae44711](https://github.com/MariaDB/server/commit/08dae44711)\
  2017-12-07 15:54:27 +0400
  * [MDEV-14228](https://jira.mariadb.org/browse/MDEV-14228) MariaDB crashes with function
* [Revision #6d4b0958dc](https://github.com/MariaDB/server/commit/6d4b0958dc)\
  2017-12-07 11:41:52 +0200
  * Fix failing test mysql\_client\_test
* [Revision #62eaf7b657](https://github.com/MariaDB/server/commit/62eaf7b657)\
  2017-12-12 12:09:52 +0530
  * [MDEV-14573](https://jira.mariadb.org/browse/MDEV-14573): Upgrade from previous versions is broken for procedures
* [Revision #70d6c944cb](https://github.com/MariaDB/server/commit/70d6c944cb)\
  2017-12-04 18:53:19 +0000
  * [MDEV-14113](https://jira.mariadb.org/browse/MDEV-14113) Use abortive TCP close, in case server closes the connection first, and we do not care whether client has received all data.
* [Revision #8f581e8bf1](https://github.com/MariaDB/server/commit/8f581e8bf1)\
  2017-12-10 23:10:43 +0530
  * Removing files sql/item\_sum.cc.orig and sql/item\_sum.h.orig added by commit 6d63a03490298a8b7246e7f4516eb383534f8e8c [MDEV-11297](https://jira.mariadb.org/browse/MDEV-11297): Add support for LIMIT clause in GROUP\_CONCAT()
* [Revision #99bcec295d](https://github.com/MariaDB/server/commit/99bcec295d)\
  2017-11-24 21:56:13 +0000
  * [MDEV-12501](https://jira.mariadb.org/browse/MDEV-12501) -- set --maturity-level by default
* [Revision #c60095a818](https://github.com/MariaDB/server/commit/c60095a818)\
  2017-12-07 18:36:01 +0400
  * Faster atomic loads and stores on windows
* [Revision #b04f2a0f01](https://github.com/MariaDB/server/commit/b04f2a0f01)\
  2017-12-01 15:48:03 +0400
  * [MDEV-14529](https://jira.mariadb.org/browse/MDEV-14529) - InnoDB rw-locks: optimize memory barriers
* [Revision #51bb18f989](https://github.com/MariaDB/server/commit/51bb18f989)\
  2017-12-01 13:52:24 +0400
  * [MDEV-14529](https://jira.mariadb.org/browse/MDEV-14529) - InnoDB rw-locks: optimize memory barriers
* [Revision #5b624f00fc](https://github.com/MariaDB/server/commit/5b624f00fc)\
  2017-12-01 13:37:07 +0400
  * [MDEV-14529](https://jira.mariadb.org/browse/MDEV-14529) - InnoDB rw-locks: optimize memory barriers
* [Revision #57d20f1132](https://github.com/MariaDB/server/commit/57d20f1132)\
  2017-12-01 13:14:42 +0400
  * [MDEV-14529](https://jira.mariadb.org/browse/MDEV-14529) - InnoDB rw-locks: optimize memory barriers
* [Revision #c73e77da0f](https://github.com/MariaDB/server/commit/c73e77da0f)\
  2017-12-01 12:02:51 +0400
  * [MDEV-14529](https://jira.mariadb.org/browse/MDEV-14529) - InnoDB rw-locks: optimize memory barriers
* [Revision #db715ff392](https://github.com/MariaDB/server/commit/db715ff392)\
  2017-12-08 11:38:00 +0200
  * Add extra mutex check to wsrep\_aborting\_thd\_enqueue
* [Revision #68cd543539](https://github.com/MariaDB/server/commit/68cd543539)\
  2017-12-08 11:37:33 +0200
  * Search for galera libraries also in /usr/lib64/galera-3
* [Revision #c4581735d0](https://github.com/MariaDB/server/commit/c4581735d0)\
  2017-12-08 11:36:18 +0200
  * Cleanups
* [Revision #6d63a03490](https://github.com/MariaDB/server/commit/6d63a03490)\
  2017-12-08 12:21:26 +0530
  * [MDEV-11297](https://jira.mariadb.org/browse/MDEV-11297): Add support for LIMIT clause in GROUP\_CONCAT()
* [Revision #3aa618a969](https://github.com/MariaDB/server/commit/3aa618a969)\
  2017-12-07 14:35:32 +0200
  * [MDEV-13820](https://jira.mariadb.org/browse/MDEV-13820) trx\_id\_check() fails during row\_log\_table\_apply()
* Merge [Revision #4ea5b126c5](https://github.com/MariaDB/server/commit/4ea5b126c5) 2017-12-07 08:21:00 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #bce4065129](https://github.com/MariaDB/server/commit/bce4065129) 2017-12-07 08:18:43 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #51c73a431f](https://github.com/MariaDB/server/commit/51c73a431f) 2017-12-07 08:17:50 +0200 - Merge 10.1 into 10.2
* [Revision #447931c6ab](https://github.com/MariaDB/server/commit/447931c6ab)\
  2017-12-07 08:14:49 +0200
  * Post-fix for [MDEV-14587](https://jira.mariadb.org/browse/MDEV-14587)
* Merge [Revision #976f6fb1b6](https://github.com/MariaDB/server/commit/976f6fb1b6) 2017-12-06 19:36:33 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #ce07676502](https://github.com/MariaDB/server/commit/ce07676502) 2017-12-06 19:11:12 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #77fb7ccba4](https://github.com/MariaDB/server/commit/77fb7ccba4)\
  2017-12-04 16:26:14 +0200
  * Follow-up fix to [MDEV-13201](https://jira.mariadb.org/browse/MDEV-13201) Assertion `srv_undo_sources || ...` failed on shutdown during DDL operation
* [Revision #7dc6066dea](https://github.com/MariaDB/server/commit/7dc6066dea)\
  2017-12-01 16:51:24 +0200
  * [MDEV-14511](https://jira.mariadb.org/browse/MDEV-14511) Use fewer transactions for updating InnoDB persistent statistics
* [Revision #2c1e4d4d7a](https://github.com/MariaDB/server/commit/2c1e4d4d7a)\
  2017-12-05 16:33:38 +0300
  * [MDEV-14563](https://jira.mariadb.org/browse/MDEV-14563): Wrong query plan for query with no PK
* [Revision #a6254e5e7d](https://github.com/MariaDB/server/commit/a6254e5e7d)\
  2017-12-04 15:01:57 +0300
  * [MDEV-14563](https://jira.mariadb.org/browse/MDEV-14563): Wrong query plan for query with no PK
* [Revision #c3803914c5](https://github.com/MariaDB/server/commit/c3803914c5)\
  2017-12-02 17:26:37 +0000
  * [MDEV-14433](https://jira.mariadb.org/browse/MDEV-14433): RocksDB may show empty or incorrect output with rocksdb\_strict\_collation\_check=off
* Merge [Revision #f1f2b7742f](https://github.com/MariaDB/server/commit/f1f2b7742f) 2017-12-06 10:40:58 +0200 - [MDEV-13626](https://jira.mariadb.org/browse/MDEV-13626) Merge InnoDB test cases from MySQL 5.7 (part 4)
* [Revision #afe6aef5ff](https://github.com/MariaDB/server/commit/afe6aef5ff)\
  2017-12-06 10:37:08 +0200
  * Adjust the test innodb.virtual\_stats and rename to gcol.innodb\_virtual\_stats
* [Revision #b1cd5ca2af](https://github.com/MariaDB/server/commit/b1cd5ca2af)\
  2017-12-06 10:35:09 +0200
  * Import innodb.virtual\_stats from MySQL 5.7
* [Revision #e9bc0f75ef](https://github.com/MariaDB/server/commit/e9bc0f75ef)\
  2017-12-06 10:32:24 +0200
  * [MDEV-5834](https://jira.mariadb.org/browse/MDEV-5834) cleanup: Inline two tiny functions
* Merge [Revision #1d526f31fb](https://github.com/MariaDB/server/commit/1d526f31fb) 2017-12-05 14:23:57 +0200 - Merge 10.1 into 10.2
* [Revision #63cbb98275](https://github.com/MariaDB/server/commit/63cbb98275)\
  2017-12-05 13:25:09 +0200
  * [MDEV-14587](https://jira.mariadb.org/browse/MDEV-14587) dict\_stats\_process\_entry\_from\_defrag\_pool() fails to call dict\_table\_close() when index==NULL
* [Revision #d7b0b8ddac](https://github.com/MariaDB/server/commit/d7b0b8ddac)\
  2017-12-03 15:21:53 +0200
  * [MDEV-10688](https://jira.mariadb.org/browse/MDEV-10688) rpl.rpl\_row\_log\_innodb failed in buildbot
* [Revision #d1ab89037a](https://github.com/MariaDB/server/commit/d1ab89037a)\
  2017-12-05 12:50:35 +0200
  * [MDEV-13670](https://jira.mariadb.org/browse/MDEV-13670)/[MDEV-14550](https://jira.mariadb.org/browse/MDEV-14550) Error log flood : "InnoDB: page\_cleaner: 1000ms intended loop took N ms. The settings might not be optimal."
* [Revision #8be7548085](https://github.com/MariaDB/server/commit/8be7548085)\
  2017-12-04 13:43:02 +0200
  * Follow-up to [MDEV-12698](https://jira.mariadb.org/browse/MDEV-12698): Adjust some comments
* [Revision #bd8fd3b7c3](https://github.com/MariaDB/server/commit/bd8fd3b7c3)\
  2017-12-04 11:48:12 +0200
  * Remove references to UNIV\_SYNC\_DEBUG which was merged with UNIV\_DEBUG
* [Revision #d9188adae5](https://github.com/MariaDB/server/commit/d9188adae5)\
  2017-12-03 12:45:54 +0200
  * resolve\_stack\_dump updated to match latest stack trace format
* [Revision #a34b976d8e](https://github.com/MariaDB/server/commit/a34b976d8e)\
  2016-10-07 16:58:12 +0200
  * Add "leaves" algorithm to oqgraph.
* [Revision #5868a184fa](https://github.com/MariaDB/server/commit/5868a184fa)\
  2017-12-05 08:49:28 +0000
  * Revert "[MDEV-12501](https://jira.mariadb.org/browse/MDEV-12501) -- set --maturity-level by default"
* [Revision #1af2d7ba23](https://github.com/MariaDB/server/commit/1af2d7ba23)\
  2017-11-24 21:56:13 +0000
  * [MDEV-12501](https://jira.mariadb.org/browse/MDEV-12501) -- set --maturity-level by default
* [Revision #60c446584c](https://github.com/MariaDB/server/commit/60c446584c)\
  2017-11-22 21:09:24 +0200
  * [MDEV-7773](https://jira.mariadb.org/browse/MDEV-7773): Aggregate stored functions
* [Revision #7448b01bb5](https://github.com/MariaDB/server/commit/7448b01bb5)\
  2017-12-02 22:30:48 +0200
  * Remove the side effect of setting m\_sp from Item\_sp::init\_result\_field
* [Revision #c12d1ed48e](https://github.com/MariaDB/server/commit/c12d1ed48e)\
  2017-11-23 10:38:04 +0200
  * Refactor parts of Item\_func\_sp into Item\_sp
* [Revision #b213f57dc3](https://github.com/MariaDB/server/commit/b213f57dc3)\
  2017-12-04 11:29:00 +0200
  * Follow-up to [MDEV-12288](https://jira.mariadb.org/browse/MDEV-12288): Avoid mutex acquistion in trx\_rw\_is\_active(0)
* [Revision #751ad74491](https://github.com/MariaDB/server/commit/751ad74491)\
  2017-12-04 11:28:10 +0200
  * Silence -Wimplicit-fallthrough
* [Revision #60df17e95a](https://github.com/MariaDB/server/commit/60df17e95a)\
  2017-12-02 21:50:08 +0200
  * Remove compiler warnings
* [Revision #52ca07c2a0](https://github.com/MariaDB/server/commit/52ca07c2a0)\
  2017-11-28 23:42:51 +0200
  * Add direct join support for Spider
* [Revision #bfaf2d6e35](https://github.com/MariaDB/server/commit/bfaf2d6e35)\
  2017-11-28 22:42:59 +0200
  * Changes to fix 64-bit Windows build errors and warnings.
* [Revision #207594afac](https://github.com/MariaDB/server/commit/207594afac)\
  2017-11-27 21:53:02 +0200
  * merge Spider 3.3.13
* [Revision #e53ef202bd](https://github.com/MariaDB/server/commit/e53ef202bd)\
  2017-11-16 11:11:52 +0200
  * Adding direct update/delete to the server and to the partition engine.
* [Revision #d1e4ecec07](https://github.com/MariaDB/server/commit/d1e4ecec07)\
  2017-11-15 04:31:10 +0200
  * Spider fix: Stop searching next when m\_top\_entry=NO\_CURRENT\_PART\_ID
* [Revision #352feb49c4](https://github.com/MariaDB/server/commit/352feb49c4)\
  2017-11-15 04:28:53 +0200
  * Cleanups for ha\_partition.cc
* [Revision #b016e1ba7f](https://github.com/MariaDB/server/commit/b016e1ba7f)\
  2017-11-07 11:04:45 +0200
  * [MDEV-7702](https://jira.mariadb.org/browse/MDEV-7702) Spiral patch 004\_mariadb-10.0.15.slave-trx-retry.diff
* [Revision #3907ff2d24](https://github.com/MariaDB/server/commit/3907ff2d24)\
  2017-09-29 17:48:32 +0300
  * Fix index scan cleanup in the partition engine.
* [Revision #f26e14e2d8](https://github.com/MariaDB/server/commit/f26e14e2d8)\
  2017-09-28 16:38:10 +0300
  * Adding option to tell that cmp\_ref handler call is expensive
* [Revision #dc17ac1638](https://github.com/MariaDB/server/commit/dc17ac1638)\
  2017-09-27 22:48:05 +0300
  * Adding support for auto\_increment in the partition engine.
* [Revision #2f09b28e0f](https://github.com/MariaDB/server/commit/2f09b28e0f)\
  2017-09-26 00:56:10 +0300
  * Adding Full Text Search support to partitions
* [Revision #5b409843b8](https://github.com/MariaDB/server/commit/5b409843b8)\
  2017-09-26 00:23:55 +0300
  * Fixed indentation in ha\_partition.cc when assigning variables
* [Revision #da26d16dd1](https://github.com/MariaDB/server/commit/da26d16dd1)\
  2017-09-09 16:20:55 +0300
  * Add direct aggregates
* [Revision #6f5a7e9227](https://github.com/MariaDB/server/commit/6f5a7e9227)\
  2017-07-22 11:27:38 +0300
  * Added more DBUG information
* [Revision #8eeb689e9f](https://github.com/MariaDB/server/commit/8eeb689e9f)\
  2017-07-05 18:20:06 +0300
  * Adding multi\_range\_read support to partitions
* [Revision #d5268a610a](https://github.com/MariaDB/server/commit/d5268a610a)\
  2016-12-05 13:04:47 +0200
  * [MDEV-7700](https://jira.mariadb.org/browse/MDEV-7700) Spiral patch 002\_mariadb-10.0.15.spider.diff, part 2
* [Revision #7abe11499a](https://github.com/MariaDB/server/commit/7abe11499a)\
  2016-12-05 12:17:52 +0200
  * MDEV 7701 extra() calls for VP engine
* [Revision #3d1d4b874d](https://github.com/MariaDB/server/commit/3d1d4b874d)\
  2016-11-21 20:36:23 +0200
  * [MDEV-7700](https://jira.mariadb.org/browse/MDEV-7700) Spiral patch 002\_mariadb-10.0.15.spider.diff - Enable HA\_EXTRA\_WRITE\_CAN\_REPLACE and HA\_EXTRA\_WRITE\_CANNOT\_REPLACE for partition engine.
* [Revision #25a1fdd18c](https://github.com/MariaDB/server/commit/25a1fdd18c)\
  2016-11-21 10:00:52 +0200
  * Applied patch 001\_mariadb-10.0.15.partition\_cond\_push.diff - Added cond\_push() and cond\_pop() to ha\_partition.cc
* [Revision #c57e1bf5e6](https://github.com/MariaDB/server/commit/c57e1bf5e6)\
  2016-11-20 22:30:30 +0200
  * Added spider patches for adding HANDLER support for the partition engine
* [Revision #6660708523](https://github.com/MariaDB/server/commit/6660708523)\
  2017-12-01 12:34:37 +0200
  * Changed "const row not found" to "Const row not found"
* [Revision #c24d1d665c](https://github.com/MariaDB/server/commit/c24d1d665c)\
  2017-11-30 17:03:55 +0200
  * Improve error messages
* [Revision #cfaaace635](https://github.com/MariaDB/server/commit/cfaaace635)\
  2017-11-30 17:02:15 +0200
  * Write leaked memory before assert, if compiled with safemalloc
* [Revision #c65911ac46](https://github.com/MariaDB/server/commit/c65911ac46)\
  2017-11-30 17:01:23 +0200
  * Mark constant 'null\_tables' with table->const\_table=1
* Merge [Revision #ddac2d7a1e](https://github.com/MariaDB/server/commit/ddac2d7a1e) 2017-12-01 15:37:30 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #24c9785a67](https://github.com/MariaDB/server/commit/24c9785a67) 2017-12-01 15:35:16 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #40bf5c951b](https://github.com/MariaDB/server/commit/40bf5c951b)\
  2017-12-01 15:28:33 +0200
  * Fix a Bison warning about semantic type clash in default action
* [Revision #8d24bef640](https://github.com/MariaDB/server/commit/8d24bef640)\
  2017-12-01 15:02:04 +0200
  * [MDEV-14080](https://jira.mariadb.org/browse/MDEV-14080) InnoDB shutdown sometimes hangs
* [Revision #f59a1826f8](https://github.com/MariaDB/server/commit/f59a1826f8)\
  2017-11-29 22:56:23 +0000
  * [MDEV-14536](https://jira.mariadb.org/browse/MDEV-14536) : during backup, retry read of log blocks, if there is (possibly intermittent) checksum mismatch.
* Merge [Revision #3fe261bd2b](https://github.com/MariaDB/server/commit/3fe261bd2b) 2017-11-29 15:08:04 +0000 - Merge remote-tracking branch 'origin/10.1' into 10.2
* [Revision #bf6d11c4d6](https://github.com/MariaDB/server/commit/bf6d11c4d6)\
  2017-11-29 14:53:12 +0000
  * [MDEV-14536](https://jira.mariadb.org/browse/MDEV-14536) : In mariadb-backup, reread redo log blocks , if checksum mismatch is detected.
* [Revision #8cee2f136d](https://github.com/MariaDB/server/commit/8cee2f136d)\
  2017-11-23 18:42:28 +0200
  * [MDEV-13384](https://jira.mariadb.org/browse/MDEV-13384): "window" seems like a reserved column name but it's not listed as one
* [Revision #e01d788428](https://github.com/MariaDB/server/commit/e01d788428)\
  2017-11-30 18:07:28 +0400
  * Optimized away excessive condition
* Merge [Revision #7cb3520c06](https://github.com/MariaDB/server/commit/7cb3520c06) 2017-11-30 08:16:37 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #5b697c5a23](https://github.com/MariaDB/server/commit/5b697c5a23) 2017-11-29 12:06:48 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #b65fd73bb1](https://github.com/MariaDB/server/commit/b65fd73bb1)\
  2017-11-28 15:59:36 -0500
  * bump the VERSION
* [Revision #23d2dae5f0](https://github.com/MariaDB/server/commit/23d2dae5f0)\
  2017-11-28 18:23:35 +0200
  * Fix some integer type mismatch warnings
* [Revision #e02b860861](https://github.com/MariaDB/server/commit/e02b860861)\
  2017-11-20 20:39:59 +0000
  * Windows, generic threadpool cleanups
* [Revision #e01d33d773](https://github.com/MariaDB/server/commit/e01d33d773)\
  2017-11-29 10:03:51 +0400
  * [MDEV-14467](https://jira.mariadb.org/browse/MDEV-14467) Item\_param: replace {INT|DECIMAL|REAL|STRING|TIME}\_VALUE with Type\_handler
* [Revision #590400f743](https://github.com/MariaDB/server/commit/590400f743)\
  2017-11-28 06:25:14 +0400
  * [MDEV-14517](https://jira.mariadb.org/browse/MDEV-14517) Cleanup for Item::with\_subselect and Item::has\_subquery()
* [Revision #6aedbf40e0](https://github.com/MariaDB/server/commit/6aedbf40e0)\
  2017-11-24 12:40:00 +0400
  * [MDEV-14494](https://jira.mariadb.org/browse/MDEV-14494) Move set\_param\_xxx() in sql\_prepare.cc to methods in Item\_param and Type\_handler
* [Revision #a18f6009e3](https://github.com/MariaDB/server/commit/a18f6009e3)\
  2017-11-22 11:38:29 +0400
  * A cleanup for [MDEV-12846](https://jira.mariadb.org/browse/MDEV-12846) sql\_mode=ORACLE: using Oracle-style placeholders in direct query execution makes the server crash
* Merge [Revision #366bb162fe](https://github.com/MariaDB/server/commit/366bb162fe) 2017-11-21 18:59:30 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #563f1d894b](https://github.com/MariaDB/server/commit/563f1d894b)\
  2017-11-21 16:02:26 +0400
  * [MDEV-14454](https://jira.mariadb.org/browse/MDEV-14454) Binary protocol returns wrong collation ID for SP OUT parameters
* Merge [Revision #4a8039b04e](https://github.com/MariaDB/server/commit/4a8039b04e) 2017-11-20 11:12:08 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #a0c7d3ff94](https://github.com/MariaDB/server/commit/a0c7d3ff94)\
  2017-11-16 14:33:28 +0400
  * [MDEV-14415](https://jira.mariadb.org/browse/MDEV-14415) Add Oracle-style FOR loop to sql\_mode=DEFAULT
* [Revision #1c34608436](https://github.com/MariaDB/server/commit/1c34608436)\
  2017-11-15 19:18:28 +0400
  * [MDEV-14404](https://jira.mariadb.org/browse/MDEV-14404) Don't use LEX::check\_exists in ALTER SEQUENCE
* [Revision #7663773e56](https://github.com/MariaDB/server/commit/7663773e56)\
  2017-11-15 14:42:04 +0400
  * [MDEV-11160](https://jira.mariadb.org/browse/MDEV-11160) "Incorrect column name" when "CREATE TABLE t1 AS SELECT spvar"
* [Revision #ac8e0507fe](https://github.com/MariaDB/server/commit/ac8e0507fe)\
  2017-11-15 14:34:04 +0400
  * [MDEV-11155](https://jira.mariadb.org/browse/MDEV-11155) Bad error message when creating a SET column with comma and non-ASCII characters
* [Revision #b8f906dd4b](https://github.com/MariaDB/server/commit/b8f906dd4b)\
  2017-11-15 14:18:46 +0400
  * [MDEV-12846](https://jira.mariadb.org/browse/MDEV-12846) sql\_mode=ORACLE: using Oracle-style placeholders in direct query execution makes the server crash
* [Revision #765452dbef](https://github.com/MariaDB/server/commit/765452dbef)\
  2017-11-14 16:31:10 +0400
  * [MDEV-14388](https://jira.mariadb.org/browse/MDEV-14388) Server crashes in handle\_select / val\_uint in ORACLE mode
* [Revision #071aece907](https://github.com/MariaDB/server/commit/071aece907)\
  2017-11-13 21:58:00 +0400
  * [MDEV-14376](https://jira.mariadb.org/browse/MDEV-14376) Explicit CAST(CHAR(N)) erroneously escalates warnings to errors in STRICT\_ALL\_TABLES
* [Revision #0611797729](https://github.com/MariaDB/server/commit/0611797729)\
  2017-11-13 13:04:21 +0100
  * Fix of result code check by Monty's request.
* [Revision #d1b666b5c6](https://github.com/MariaDB/server/commit/d1b666b5c6)\
  2017-11-13 10:02:59 +0100
  * [MDEV-14346](https://jira.mariadb.org/browse/MDEV-14346): incorrect result of intersect with ANY/ALL/IN subquery
* [Revision #d2bf101cbf](https://github.com/MariaDB/server/commit/d2bf101cbf)\
  2017-11-13 09:41:29 +0100
  * [MDEV-13723](https://jira.mariadb.org/browse/MDEV-13723): Server crashes in ha\_heap::find\_unique\_row or Assertion \`0' failed in st\_select\_lex\_unit::optimize with INTERSECT
* [Revision #51b30586ea](https://github.com/MariaDB/server/commit/51b30586ea)\
  2016-09-20 15:41:38 +0000
  * FRM: fail to load extra2 option with size 1 fix
* [Revision #0c6ff122fa](https://github.com/MariaDB/server/commit/0c6ff122fa)\
  2017-11-28 17:22:46 +0200
  * Follow-up fix to [MDEV-14477](https://jira.mariadb.org/browse/MDEV-14477): Use proper std::map allocator
* [Revision #12c977ca7b](https://github.com/MariaDB/server/commit/12c977ca7b)\
  2017-11-28 16:59:52 +0400
  * [MDEV-14374](https://jira.mariadb.org/browse/MDEV-14374) - UT\_DELAY code : Removing hardware barrier for arm64 bit platform
* [Revision #a489d91993](https://github.com/MariaDB/server/commit/a489d91993)\
  2017-11-28 16:34:31 +0400
  * Cleanup UT\_LOW\_PRIORITY\_CPU/UT\_RESUME\_PRIORITY\_CPU
* [Revision #1c4968f2f3](https://github.com/MariaDB/server/commit/1c4968f2f3)\
  2017-11-27 14:43:24 +0000
  * Fix warnings
* [Revision #1029b22feb](https://github.com/MariaDB/server/commit/1029b22feb)\
  2017-09-04 15:40:21 +0400
  * [MDEV-13728](https://jira.mariadb.org/browse/MDEV-13728) - Import MySQL 5.7 atomic operations for MSVC and Solaris
* [Revision #62fb022110](https://github.com/MariaDB/server/commit/62fb022110)\
  2017-11-27 11:19:26 +0200
  * Adjust the result diffs for innodb.instant\_alter
* [Revision #447cd7b1af](https://github.com/MariaDB/server/commit/447cd7b1af)\
  2017-11-27 10:06:37 +0200
  * Test MDL with a more generic ALTER TABLE statement
* [Revision #ab63290c35](https://github.com/MariaDB/server/commit/ab63290c35)\
  2017-11-24 16:26:44 +0200
  * Removed "deprecated" warning from explicit\_defaults\_for\_timestamp
* [Revision #abf61fd91f](https://github.com/MariaDB/server/commit/abf61fd91f)\
  2017-11-24 14:57:44 +0400
  * Fixed build failure with PFS disabled
* [Revision #17529785f1](https://github.com/MariaDB/server/commit/17529785f1)\
  2017-11-24 13:26:15 +0400
  * Fix hang in buf\_flush\_set\_page\_cleaner\_thread\_cnt
* [Revision #1773116fe0](https://github.com/MariaDB/server/commit/1773116fe0)\
  2017-11-23 15:02:26 +0200
  * Use ST\_AsText() to get textual result
* [Revision #84ee7a1000](https://github.com/MariaDB/server/commit/84ee7a1000)\
  2017-11-23 15:22:10 +0400
  * Less code to depend on ut\_crc32\_init()
* [Revision #aaf5ee85f3](https://github.com/MariaDB/server/commit/aaf5ee85f3)\
  2017-11-23 14:53:16 +0400
  * Removed HW acceleration for big endian checksum
* [Revision #62ce8ce75f](https://github.com/MariaDB/server/commit/62ce8ce75f)\
  2017-11-23 14:35:50 +0400
  * Removed ut\_crc32\_byte\_by\_byte: never used
* [Revision #e69466d023](https://github.com/MariaDB/server/commit/e69466d023)\
  2017-11-10 19:02:27 +0200
  * Improve performance of heap tables
* [Revision #d8ada08152](https://github.com/MariaDB/server/commit/d8ada08152)\
  2017-11-22 16:27:59 +0200
  * [MDEV-14477](https://jira.mariadb.org/browse/MDEV-14477) InnoDB update\_time is wrongly updated after partial rollback or internal COMMIT
* [Revision #fda4fabe9c](https://github.com/MariaDB/server/commit/fda4fabe9c)\
  2017-11-22 17:42:34 +0200
  * Correct a comment
* [Revision #8a24be6e74](https://github.com/MariaDB/server/commit/8a24be6e74)\
  2017-11-22 08:01:43 +0200
  * Less dependencies in include files
* [Revision #166056f744](https://github.com/MariaDB/server/commit/166056f744)\
  2017-11-22 08:01:07 +0200
  * Remove not used mem\_root argument from build\_clone(), get\_copy() and get\_item\_copy()
* [Revision #e44107c4d9](https://github.com/MariaDB/server/commit/e44107c4d9)\
  2017-11-22 14:38:51 +0400
  * Tencent contributions added
* [Revision #feec04f29d](https://github.com/MariaDB/server/commit/feec04f29d)\
  2017-11-17 12:18:16 +0800
  * Travis-CI: clean up cruft and add more in-line commments
* [Revision #325c9ce9b3](https://github.com/MariaDB/server/commit/325c9ce9b3)\
  2017-11-17 12:17:26 +0800
  * Travis-CI: slim down the deb build so it passes in the 50 minute time limit
* [Revision #b9e029d706](https://github.com/MariaDB/server/commit/b9e029d706)\
  2017-11-17 12:12:44 +0800
  * Travis-CI: make deb job visible on the parallel jobs list
* [Revision #c029eae02d](https://github.com/MariaDB/server/commit/c029eae02d)\
  2017-11-17 19:39:52 +0900
  * Spelling fix
* [Revision #e0a00c5a2f](https://github.com/MariaDB/server/commit/e0a00c5a2f)\
  2017-11-17 19:36:47 +0000
  * [MDEV-14412](https://jira.mariadb.org/browse/MDEV-14412) Support TCP keepalive options
* [Revision #faee08c10c](https://github.com/MariaDB/server/commit/faee08c10c)\
  2017-10-30 21:39:55 +0100
  * [MDEV-14114](https://jira.mariadb.org/browse/MDEV-14114) Intoduce variable for binlog io cache size.
* [Revision #5b3da95bf3](https://github.com/MariaDB/server/commit/5b3da95bf3)\
  2017-11-17 05:21:12 +0200
  * Simplify fn\_rext
* [Revision #326bfb071c](https://github.com/MariaDB/server/commit/326bfb071c)\
  2017-11-17 05:18:32 +0200
  * [MDEV-14378](https://jira.mariadb.org/browse/MDEV-14378) - Allow on to drop orphaned #sql- tables
* [Revision #cf5e193d06](https://github.com/MariaDB/server/commit/cf5e193d06)\
  2017-11-17 01:55:37 +0200
  * Remove mark\_check\_constraint\_columns from delete
* [Revision #87933d5261](https://github.com/MariaDB/server/commit/87933d5261)\
  2017-11-14 07:47:58 +0200
  * Handle failures from malloc
* [Revision #31bd86c8df](https://github.com/MariaDB/server/commit/31bd86c8df)\
  2017-11-14 13:16:31 +0300
  * Tests: dependency on wsrep removed from sql\_sequence tests
* [Revision #5fdd51e7c0](https://github.com/MariaDB/server/commit/5fdd51e7c0)\
  2017-11-16 10:12:21 +0200
  * Removed accidentally added sysvars files
* [Revision #3948f4b4dc](https://github.com/MariaDB/server/commit/3948f4b4dc)\
  2017-11-07 11:22:08 +1100
  * mysys: Remove freebsd freopen implementation
* [Revision #761e6574c8](https://github.com/MariaDB/server/commit/761e6574c8)\
  2017-11-15 02:41:45 +0200
  * [MDEV-14396](https://jira.mariadb.org/browse/MDEV-14396) Assertion failed in create\_option\_need\_rebuild
* [Revision #e94c9d24f6](https://github.com/MariaDB/server/commit/e94c9d24f6)\
  2017-11-11 22:27:03 +0200
  * [MDEV-14378](https://jira.mariadb.org/browse/MDEV-14378) In ALGORITHM=INPLACE, use a common name for the intermediate tables or partitions
* Merge [Revision #a48aa0cd56](https://github.com/MariaDB/server/commit/a48aa0cd56) 2017-11-10 16:12:45 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #386e5d476e](https://github.com/MariaDB/server/commit/386e5d476e) 2017-11-10 16:07:01 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #1ca72a0c0d](https://github.com/MariaDB/server/commit/1ca72a0c0d) 2017-11-10 08:27:09 +0200 - Merge 10.2 into bb-10.2-ext
* Merge [Revision #0bb0d52221](https://github.com/MariaDB/server/commit/0bb0d52221) 2017-11-09 23:21:41 +0200 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #7dbff2c513](https://github.com/MariaDB/server/commit/7dbff2c513)\
  2017-11-09 08:26:52 +0200
  * Fixed failing test case as part of adding MAX\_MEMORY\_USED
* [Revision #8d576bcbdd](https://github.com/MariaDB/server/commit/8d576bcbdd)\
  2017-11-09 08:26:50 +0400
  * Test cleanup for Monty's bce807f70fbd386fd70dee3161972cb3449531b1
* [Revision #99a2870905](https://github.com/MariaDB/server/commit/99a2870905)\
  2017-11-05 20:05:41 +0200
  * Simple cleanups
* [Revision #bce807f70f](https://github.com/MariaDB/server/commit/bce807f70f)\
  2017-11-05 20:05:02 +0200
  * Rename some errors that uses MySQL -> MariaDB
* [Revision #c9f612dbde](https://github.com/MariaDB/server/commit/c9f612dbde)\
  2017-11-05 17:04:20 +0200
  * Add more execution stages (commit, rollback, etc)
* [Revision #61706e61fe](https://github.com/MariaDB/server/commit/61706e61fe)\
  2017-11-05 16:38:21 +0200
  * Disable some test that fails constantly
* [Revision #98b3f28862](https://github.com/MariaDB/server/commit/98b3f28862)\
  2017-11-05 22:22:01 +0400
  * [MDEV-14217](https://jira.mariadb.org/browse/MDEV-14217) \[db crash] Recursive CTE when SELECT includes new field
* [Revision #4e34eaf187](https://github.com/MariaDB/server/commit/4e34eaf187)\
  2017-11-04 12:44:56 +0200
  * Remove an unused variable
* Merge [Revision #5fc79476b5](https://github.com/MariaDB/server/commit/5fc79476b5) 2017-11-03 09:29:21 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #7a63a7dc6d](https://github.com/MariaDB/server/commit/7a63a7dc6d)\
  2017-11-03 09:27:53 +0400
  * [MDEV-14269](https://jira.mariadb.org/browse/MDEV-14269) errors.test fails with valgrind (Conditional jump or move depends on uninitialised value)
* [Revision #3ab112eb39](https://github.com/MariaDB/server/commit/3ab112eb39)\
  2017-11-01 20:30:45 +0200
  * Fixed compiler warning and unitialized memory warning
* [Revision #a17e7d0747](https://github.com/MariaDB/server/commit/a17e7d0747)\
  2017-11-01 20:30:32 +0200
  * Updated valgrind.supp
* [Revision #c127a1ba14](https://github.com/MariaDB/server/commit/c127a1ba14)\
  2017-11-01 20:30:12 +0200
  * Reduce memory used by maria\_open
* [Revision #9ec19b9b41](https://github.com/MariaDB/server/commit/9ec19b9b41)\
  2017-11-01 20:28:36 +0200
  * Reducing memory when using information schema
* [Revision #8409f721ff](https://github.com/MariaDB/server/commit/8409f721ff)\
  2017-11-10 09:18:53 +0200
  * setval(): Do not fall through from GET\_FLAGSET to GET\_BIT
* [Revision #623ed1c204](https://github.com/MariaDB/server/commit/623ed1c204)\
  2017-11-10 11:22:51 +0100
  * [MDEV-13723](https://jira.mariadb.org/browse/MDEV-13723): Server crashes in ha\_heap::find\_unique\_row or Assertion \`0' failed in st\_select\_lex\_unit::optimize with INTERSECT
* [Revision #06a9a366a3](https://github.com/MariaDB/server/commit/06a9a366a3)\
  2017-11-07 12:06:15 +0400
  * [MDEV-14235](https://jira.mariadb.org/browse/MDEV-14235) main.mysql\_upgrade\_noengine failed, results mismatch
* [Revision #2ba1616e5d](https://github.com/MariaDB/server/commit/2ba1616e5d)\
  2017-11-05 11:59:19 -0800
  * Fixed [MDEV-14281](https://jira.mariadb.org/browse/MDEV-14281) Wrong result from query with NOT IN predicate in WHERE
* [Revision #d957a6c1f6](https://github.com/MariaDB/server/commit/d957a6c1f6)\
  2017-11-04 13:55:46 +0200
  * Adjust 32-bit sys\_vars results
* [Revision #c2a868b18c](https://github.com/MariaDB/server/commit/c2a868b18c)\
  2017-11-03 23:40:35 -0700
  * Another adjustment after the merge of [MDEV-12172](https://jira.mariadb.org/browse/MDEV-12172).
* [Revision #9333431e14](https://github.com/MariaDB/server/commit/9333431e14)\
  2017-11-03 23:12:07 -0700
  * Adjusted tests after changing the default value for the system variable @@in\_subquery\_conversion\_threshold
* [Revision #5b5aa235ea](https://github.com/MariaDB/server/commit/5b5aa235ea)\
  2017-11-03 20:05:03 -0700
  * Changed the default value for the system variable @@in\_subquery\_conversion\_threshold.
* [Revision #388ba068ba](https://github.com/MariaDB/server/commit/388ba068ba)\
  2017-11-03 15:12:01 -0700
  * Post-merge fixes for [MDEV-12172](https://jira.mariadb.org/browse/MDEV-12172), [MDEV-12176](https://jira.mariadb.org/browse/MDEV-12176).
* [Revision #9ada5a3c1a](https://github.com/MariaDB/server/commit/9ada5a3c1a)\
  2017-11-02 22:28:04 +0400
  * Cleanup tests for [MDEV-13049](https://jira.mariadb.org/browse/MDEV-13049) Querying INFORMATION\_SCHEMA becomes slow in [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)
* [Revision #3a9b7f4ecd](https://github.com/MariaDB/server/commit/3a9b7f4ecd)\
  2017-11-02 17:49:36 +0400
  * A cleanup for [MDEV-12172](https://jira.mariadb.org/browse/MDEV-12172): Fixing "mtr --suite=compat/oracle" test failures
* [Revision #6402ca7870](https://github.com/MariaDB/server/commit/6402ca7870)\
  2017-11-01 22:26:25 +0200
  * [MDEV-14016](https://jira.mariadb.org/browse/MDEV-14016) Allow instant ADD COLUMN, ADD INDEX, LOCK=NONE
* Merge [Revision #5603a5842b](https://github.com/MariaDB/server/commit/5603a5842b) 2017-11-02 12:08:37 +0200 - Merge bb-10.2-ext into 10.3
* Merge [Revision #2ec7b87053](https://github.com/MariaDB/server/commit/2ec7b87053) 2017-11-01 14:37:31 +0200 - Merge 10.2 into bb-10.2-ext
* [Revision #06ec864a09](https://github.com/MariaDB/server/commit/06ec864a09)\
  2017-11-02 12:06:46 +0200
  * Try to fix sys\_vars.sysvars\_debug,32bit
* [Revision #72817cafe2](https://github.com/MariaDB/server/commit/72817cafe2)\
  2017-11-02 11:31:28 +0200
  * Remove a type cast
* [Revision #a9faad5f78](https://github.com/MariaDB/server/commit/a9faad5f78)\
  2017-11-01 19:27:27 +0200
  * Remove an unused variable
* [Revision #1103abdae1](https://github.com/MariaDB/server/commit/1103abdae1)\
  2017-07-13 16:37:33 +1000
  * keycache: restructure functions that are controlled by arguements
* [Revision #0750b5f825](https://github.com/MariaDB/server/commit/0750b5f825)\
  2017-11-02 11:06:02 +0200
  * Fixed compilation failures
* Merge [Revision #914e2c9ba8](https://github.com/MariaDB/server/commit/914e2c9ba8) 2017-11-01 21:48:03 -0700 - Merge branch '10.3' of github.com:MariaDB/server into 10.3
* [Revision #a607e4e7aa](https://github.com/MariaDB/server/commit/a607e4e7aa)\
  2017-10-28 22:28:31 +0300
  * Added the syntax for percentile functions and median function to the sql\_yacc\_ora.yy file
* [Revision #ab5503c8c5](https://github.com/MariaDB/server/commit/ab5503c8c5)\
  2017-10-27 20:04:05 +0530
  * Updates the tests for the percentile functions
* [Revision #40887913ff](https://github.com/MariaDB/server/commit/40887913ff)\
  2017-10-27 00:16:13 +0530
  * Update the error messages involving percentile functions
* [Revision #0ef6127c29](https://github.com/MariaDB/server/commit/0ef6127c29)\
  2017-10-27 00:10:22 +0530
  * Date-time fields are disabled currently for the result type of percentile function
* [Revision #58a6e43513](https://github.com/MariaDB/server/commit/58a6e43513)\
  2017-09-07 23:51:42 +0530
  * Tests added for percentile and median functions
* [Revision #b77105cab6](https://github.com/MariaDB/server/commit/b77105cab6)\
  2017-10-26 23:55:52 +0530
  * Only single element order-by list is allowed for percentile functions
* [Revision #4f4f8f3fb1](https://github.com/MariaDB/server/commit/4f4f8f3fb1)\
  2017-10-26 23:55:09 +0530
  * Added the median function to the parser , it should behave as a percentile\_cont function with its argument fixed to 0.5
* [Revision #02a4a4b512](https://github.com/MariaDB/server/commit/02a4a4b512)\
  2017-09-07 17:40:09 +0530
  * Added fix\_fields for percentile function to check the type of argument and to ensure that only numeric arguments are allowed
* [Revision #b5c104d00a](https://github.com/MariaDB/server/commit/b5c104d00a)\
  2017-09-07 17:37:55 +0530
  * Changes made according to the review given, mostly fixing coding style errors
* [Revision #24e219b179](https://github.com/MariaDB/server/commit/24e219b179)\
  2017-08-29 18:27:16 +0300
  * Remove has\_error as a member from Item\_sum and use THD::is\_error() instead
* [Revision #f4ba298abd](https://github.com/MariaDB/server/commit/f4ba298abd)\
  2017-07-18 02:58:08 +0530
  * Fixed indentation in the syntax rules for the sql\_yacc.yy , also added the rules of the percentile functions to the sql\_yacc\_ora.yy
* [Revision #f8e135c7df](https://github.com/MariaDB/server/commit/f8e135c7df)\
  2017-07-18 01:55:31 +0530
  * made changes according to the review, mostly removing unused code and fixing code to follow the coding conventions
* [Revision #f04426f727](https://github.com/MariaDB/server/commit/f04426f727)\
  2017-07-17 15:23:21 +0530
  * Added more tests for the percentile functions
* [Revision #03ed22326a](https://github.com/MariaDB/server/commit/03ed22326a)\
  2017-07-17 15:10:19 +0530
  * Added the error 1)ER\_ARGUMENT\_OUT\_OF\_RANGE: This error is thrown if the argument of the percentile function is not in the range \[0,1] 2)ER\_ARGUMENT\_NOT\_CONSTANT: This error is thrown if the argument of the percnetile function is not constant in the entire partition of the window function
* [Revision #6511069e7f](https://github.com/MariaDB/server/commit/6511069e7f)\
  2017-07-17 15:08:08 +0530
  * Added the error ER\_WRONG\_TYPE\_FOR\_PERCENTILE\_CONT, which ensures that the result type for percentile\_cont is always numerical
* [Revision #947ce922c9](https://github.com/MariaDB/server/commit/947ce922c9)\
  2017-07-17 15:06:42 +0530
  * Added the error ER\_NOT\_SINGLE\_ELEMENT\_ORDER\_LIST for th percentile functions, these ensure that for the percentile function we have the order list with exactly one element
* [Revision #96565ac311](https://github.com/MariaDB/server/commit/96565ac311)\
  2017-07-17 15:02:22 +0530
  * Added the function setting\_handler\_for\_percentile\_function() for the percentile\_disc function that would set the type of the result field for percentile\_disc. Percentile\_cont would habe double precision result type
* [Revision #330577988f](https://github.com/MariaDB/server/commit/330577988f)\
  2017-07-17 13:25:08 +0530
  * has\_error field added to the item\_sum class. This field ensures that query is terminated if we get any error during the add function call. This is currently used only for the percentile functions
* [Revision #64a2a30295](https://github.com/MariaDB/server/commit/64a2a30295)\
  2017-07-17 13:21:23 +0530
  * Error codes added for the percentile functions, the errors are -ER\_NOT\_SINGLE\_ELEMENT\_ORDER\_LIST -ER\_WRONG\_TYPE\_FOR\_PERCENTILE\_CONT -ER\_ARGUMENT\_NOT\_CONSTANT -ER\_ARGUMENT\_OUT\_OF\_RANGE
* [Revision #eb2187a24f](https://github.com/MariaDB/server/commit/eb2187a24f)\
  2017-07-17 13:19:20 +0530
  * Val\_str function added for the percentile\_disc function, as it can have result type as STRING\_RESULT
* [Revision #3393005e95](https://github.com/MariaDB/server/commit/3393005e95)\
  2017-07-10 01:12:56 +0530
  * Ensured that the element in the order by clause should have a numerical time, if not throw an error
* [Revision #275ce39f05](https://github.com/MariaDB/server/commit/275ce39f05)\
  2017-07-07 17:37:06 +0530
  * Percentile class implemented, most of the functions have the same functionalite as the percentile cont class
* [Revision #01d2b6e9d9](https://github.com/MariaDB/server/commit/01d2b6e9d9)\
  2017-07-06 01:29:49 +0530
  * Implemented the implementation of percentile functions using Item\_cache instead of Cache\_Item
* [Revision #d2214da4d0](https://github.com/MariaDB/server/commit/d2214da4d0)\
  2017-06-27 12:44:00 +0530
  * Test case added for the percentile disc function
* [Revision #ba9fbc6a83](https://github.com/MariaDB/server/commit/ba9fbc6a83)\
  2017-06-27 02:50:18 +0530
  * implementation of add() function added to the Item\_sum\_percentile\_disc class
* [Revision #c85552f42b](https://github.com/MariaDB/server/commit/c85552f42b)\
  2017-06-27 02:24:32 +0530
  * Added a class Frame\_unbounded\_following\_set\_count\_special, which is required to ignore all the null values while calculating the number of rows in the partition
* [Revision #31f1541f1e](https://github.com/MariaDB/server/commit/31f1541f1e)\
  2017-06-26 03:53:27 +0530
  * Setting handler to have the return type as that of the element by which we are ordering the partition
* [Revision #cc046fa92c](https://github.com/MariaDB/server/commit/cc046fa92c)\
  2017-06-26 03:39:25 +0530
  * A basic implementation of the add function is added
* [Revision #18747a4baa](https://github.com/MariaDB/server/commit/18747a4baa)\
  2017-06-26 02:15:19 +0530
  * Added value field to Item\_sum\_percentile\_disc Check for single element in the order\_list is added
* [Revision #129626f171](https://github.com/MariaDB/server/commit/129626f171)\
  2017-06-26 01:55:05 +0530
  * Added get\_item() to Cached\_item\_item and get\_value to the Cached\_item
* [Revision #280945bf29](https://github.com/MariaDB/server/commit/280945bf29)\
  2017-06-22 21:43:45 +0530
  * [MDEV-12985](https://jira.mariadb.org/browse/MDEV-12985): support percentile and median window functions
* [Revision #fadfe447e8](https://github.com/MariaDB/server/commit/fadfe447e8)\
  2017-06-13 11:54:39 +0530
  * [MDEV-12985](https://jira.mariadb.org/browse/MDEV-12985): syntax added for the percentile\_cont and percentile\_disc functions
* [Revision #29c4bd9d27](https://github.com/MariaDB/server/commit/29c4bd9d27)\
  2017-11-01 13:20:32 +0000
  * SOURCE\_REVISION should always be defined in source\_revision.h
* Merge [Revision #6f1b6061d8](https://github.com/MariaDB/server/commit/6f1b6061d8) 2017-11-01 21:42:26 -0700 - Merge remote-tracking branch 'shagalla/10.3-mdev12172' into 10.3
* [Revision #34737e0cee](https://github.com/MariaDB/server/commit/34737e0cee)\
  2017-10-30 13:16:15 +0200
  * trigger.result corrected
* [Revision #43625a31cb](https://github.com/MariaDB/server/commit/43625a31cb)\
  2017-10-29 21:09:07 +0200
  * Mistakes corrected. Test results corrected.
* [Revision #99d3f217eb](https://github.com/MariaDB/server/commit/99d3f217eb)\
  2017-10-28 21:54:22 +0200
  * Mistakes corrected, variable defined.
* [Revision #a4ded0a9b5](https://github.com/MariaDB/server/commit/a4ded0a9b5)\
  2017-10-28 20:54:18 +0200
  * Mistakes corrected. TVC can be used in IN subquery and in PARTITION BY struct now. Special variable to control working of optimization added.
* [Revision #75370a58f4](https://github.com/MariaDB/server/commit/75370a58f4)\
  2017-09-04 22:29:58 +0200
  * New tests on errors added. Comments corrected. Some procedures corrected.
* [Revision #6bce8e1422](https://github.com/MariaDB/server/commit/6bce8e1422)\
  2017-09-02 23:19:20 +0200
  * Post review changes for the optimization of IN predicates into IN subqueries.
* [Revision #d76f74d46c](https://github.com/MariaDB/server/commit/d76f74d46c)\
  2017-09-01 19:18:50 +0200
  * Remarked opt\_tvc.test added.
* [Revision #e701770749](https://github.com/MariaDB/server/commit/e701770749)\
  2017-09-01 19:01:06 +0200
  * Memory allocation corrected. New tests added.
* [Revision #1efa9ed8ca](https://github.com/MariaDB/server/commit/1efa9ed8ca)\
  2017-08-29 21:24:05 +0200
  * Some mistakes in opt\_range.cc and libmysqld/CMakeLists.txt files corrected
* [Revision #a5a01dbb08](https://github.com/MariaDB/server/commit/a5a01dbb08)\
  2017-08-29 21:03:15 +0200
  * Mistakes corrected. Now all tests in opt\_tvc.test file work correctly
* [Revision #91149bbd82](https://github.com/MariaDB/server/commit/91149bbd82)\
  2017-08-29 16:58:32 +0200
  * Mistakes corrected, new error messages added
* [Revision #570d2e7d0f](https://github.com/MariaDB/server/commit/570d2e7d0f)\
  2017-08-29 02:32:39 +0200
  * Summarized results of two previous commits (26 July, 25 August)
* [Revision #3310076dbe](https://github.com/MariaDB/server/commit/3310076dbe)\
  2017-08-25 19:06:13 +0200
  * Optimization that transforms IN-predicate in IN-subselect made.
* [Revision #9103ee3c6b](https://github.com/MariaDB/server/commit/9103ee3c6b)\
  2017-07-26 22:46:16 +0300
  * Queries where TVCs are used are processed successufully. TVCs can be used separately, with UNION/UNION ALL, in derived tables, in views and in common table expressions.
* [Revision #7ba19ba384](https://github.com/MariaDB/server/commit/7ba19ba384)\
  2017-06-30 13:54:33 +0300
  * Mistakes corrected, test file corrected.
* [Revision #615da8f70b](https://github.com/MariaDB/server/commit/615da8f70b)\
  2017-06-29 15:32:17 +0300
  * New structure Table Value Constructor added in grammar. TVC can be used in UNION-statement, in view and in subquery.
* [Revision #613dd62a76](https://github.com/MariaDB/server/commit/613dd62a76)\
  2017-08-10 15:45:03 +0400
  * [MDEV-11153](https://jira.mariadb.org/browse/MDEV-11153) - Introduce status variables for table cache monitoring and tuning
* [Revision #5d3ed9acdd](https://github.com/MariaDB/server/commit/5d3ed9acdd)\
  2017-10-31 13:00:20 +0400
  * (Part#2) [MDEV-13049](https://jira.mariadb.org/browse/MDEV-13049) Querying INFORMATION\_SCHEMA becomes slow in [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)
* Merge [Revision #835cbbcc7b](https://github.com/MariaDB/server/commit/835cbbcc7b) 2017-10-30 20:47:39 +0400 - Merge remote-tracking branch 'origin/bb-10.2-ext' into 10.3
* Merge [Revision #003cb2f424](https://github.com/MariaDB/server/commit/003cb2f424) 2017-10-30 16:42:46 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #84ed288f68](https://github.com/MariaDB/server/commit/84ed288f68)\
  2017-10-04 15:12:36 +0400
  * [MDEV-13997](https://jira.mariadb.org/browse/MDEV-13997) Change Item\_bool\_rowready\_func2 to cache const items at fix time rather than evaluation time
* [Revision #667e4b97aa](https://github.com/MariaDB/server/commit/667e4b97aa)\
  2017-10-30 09:24:39 +0400
  * [MDEV-14212](https://jira.mariadb.org/browse/MDEV-14212) Add Field\_row for SP ROW variables
* [Revision #5dd5253f7e](https://github.com/MariaDB/server/commit/5dd5253f7e)\
  2017-10-27 20:48:16 +0400
  * [MDEV-14139](https://jira.mariadb.org/browse/MDEV-14139) Anchored data types for variables
* [Revision #e7637ec061](https://github.com/MariaDB/server/commit/e7637ec061)\
  2017-10-23 15:24:02 +0400
  * A cleanup for [MDEV-12007](https://jira.mariadb.org/browse/MDEV-12007) Allow ROW variables as a cursor FETCH target
* [Revision #1355fadb59](https://github.com/MariaDB/server/commit/1355fadb59)\
  2017-10-14 17:31:57 +0300
  * [MDEV-13720](https://jira.mariadb.org/browse/MDEV-13720) Server crashes in SEQUENCE::write\_lock for temporary tables
* [Revision #eea07f5f58](https://github.com/MariaDB/server/commit/eea07f5f58)\
  2017-10-22 20:14:52 +0300
  * [MDEV-13721](https://jira.mariadb.org/browse/MDEV-13721) Assertion is\_lock\_owner() failed in mysql\_rm\_table\_no\_locks
* [Revision #a3b4f575b9](https://github.com/MariaDB/server/commit/a3b4f575b9)\
  2017-10-22 20:06:01 +0300
  * Reset table->record\[1] early for sequences to fix comparision of innodb row
* [Revision #7204f66c6a](https://github.com/MariaDB/server/commit/7204f66c6a)\
  2017-10-22 13:01:33 +0300
  * [MDEV-13711](https://jira.mariadb.org/browse/MDEV-13711) Assertion failure on CREATE TABLE .. LIKE
* [Revision #7447b4ce37](https://github.com/MariaDB/server/commit/7447b4ce37)\
  2017-10-22 12:26:32 +0300
  * [MDEV-13714](https://jira.mariadb.org/browse/MDEV-13714) Value of SEQUENCE table option is ignored upon creation
* [Revision #f64cff9206](https://github.com/MariaDB/server/commit/f64cff9206)\
  2017-10-22 12:05:43 +0300
  * [MDEV-13715](https://jira.mariadb.org/browse/MDEV-13715) Server crashes in ha\_partition::engine\_name
* [Revision #edfdf0d0a3](https://github.com/MariaDB/server/commit/edfdf0d0a3)\
  2017-10-20 18:44:28 +0400
  * A cleanup for [MDEV-13415](https://jira.mariadb.org/browse/MDEV-13415) Wrap the code in sp.cc into a class Sp\_handler
* [Revision #211f9eea60](https://github.com/MariaDB/server/commit/211f9eea60)\
  2017-10-19 13:22:38 +0300
  * [MDEV-14092](https://jira.mariadb.org/browse/MDEV-14092) NEXTVAL fails on slave
* [Revision #e156db85a7](https://github.com/MariaDB/server/commit/e156db85a7)\
  2017-10-19 12:57:00 +0400
  * sp\_rcontext::sp cleanup
* [Revision #f5e09b5f8f](https://github.com/MariaDB/server/commit/f5e09b5f8f)\
  2017-10-19 11:48:34 +0400
  * Moving a piece of open\_and\_process\_routine() into a new function sp\_acquire\_routine()
* Merge [Revision #30e7d6709f](https://github.com/MariaDB/server/commit/30e7d6709f) 2017-10-18 14:11:55 +0400 - Merge remote-tracking branch 'origin/10.2' into bb-10.2-ext
* [Revision #75aabd03d5](https://github.com/MariaDB/server/commit/75aabd03d5)\
  2017-10-13 15:55:42 +0200
  * [MDEV-14013](https://jira.mariadb.org/browse/MDEV-14013) : sql\_mode=EMPTY\_STRING\_IS\_NULL
* Merge [Revision #081f5aa826](https://github.com/MariaDB/server/commit/081f5aa826) 2017-10-07 11:59:01 +0400 - Merge pull request #462 from halfspawn/bb-10.2-ext
* [Revision #34f36a335b](https://github.com/MariaDB/server/commit/34f36a335b)\
  2017-10-06 09:23:06 +0200
  * [MDEV-14012](https://jira.mariadb.org/browse/MDEV-14012) - sql\_mode=Oracle: substr(): treat position 0 as position 1
* [Revision #fe8cf8fdf1](https://github.com/MariaDB/server/commit/fe8cf8fdf1)\
  2017-10-30 16:06:42 +0400
  * Embedded tests fixed.
* [Revision #f88fcf2514](https://github.com/MariaDB/server/commit/f88fcf2514)\
  2017-10-30 07:37:25 +0400
  * [MDEV-12542](https://jira.mariadb.org/browse/MDEV-12542) Add bind\_address system variable.
* [Revision #ecee3c71e1](https://github.com/MariaDB/server/commit/ecee3c71e1)\
  2017-10-28 12:45:49 +0300
  * Fix sign mismatch warnings
* [Revision #769f060398](https://github.com/MariaDB/server/commit/769f060398)\
  2017-10-27 19:21:58 +0000
  * Fix some warnings
* [Revision #a81ea75390](https://github.com/MariaDB/server/commit/a81ea75390)\
  2017-10-27 08:14:02 +1100
  * travis: no percona tests in 10.3
* [Revision #770c5c1c9e](https://github.com/MariaDB/server/commit/770c5c1c9e)\
  2017-10-26 13:05:11 +0300
  * [MDEV-14111](https://jira.mariadb.org/browse/MDEV-14111) Inplace update assert after instant adding column
* [Revision #b23a109695](https://github.com/MariaDB/server/commit/b23a109695)\
  2017-09-09 11:34:12 +0300
  * [MDEV-11025](https://jira.mariadb.org/browse/MDEV-11025): Make number of page cleaner threads variable dynamic New test cases innodb-page-cleaners
* [Revision #3722372ae5](https://github.com/MariaDB/server/commit/3722372ae5)\
  2017-10-20 12:40:45 +0400
  * [MDEV-11549](https://jira.mariadb.org/browse/MDEV-11549) - Twin include
* [Revision #c65fdcf7c8](https://github.com/MariaDB/server/commit/c65fdcf7c8)\
  2017-10-13 21:59:15 +0300
  * [MDEV-14062](https://jira.mariadb.org/browse/MDEV-14062) Upgrade from 10.0 fails on assertion during ALTER TABLE
* [Revision #f3ad3bbe77](https://github.com/MariaDB/server/commit/f3ad3bbe77)\
  2017-10-12 17:13:01 +0300
  * fix data races
* [Revision #7d2a7782fe](https://github.com/MariaDB/server/commit/7d2a7782fe)\
  2017-10-11 17:14:17 +0400
  * Fixed build failure
* [Revision #62b21fc101](https://github.com/MariaDB/server/commit/62b21fc101)\
  2017-10-11 12:56:23 +0300
  * fix some data races (#464)
* [Revision #a4c23ac720](https://github.com/MariaDB/server/commit/a4c23ac720)\
  2017-10-10 13:15:45 +0300
  * remove unndeded class member variable
* [Revision #bbfd18c691](https://github.com/MariaDB/server/commit/bbfd18c691)\
  2017-10-09 22:55:05 +0300
  * fix unsynchronized read (#463)
* [Revision #b3027d4065](https://github.com/MariaDB/server/commit/b3027d4065)\
  2017-10-09 21:09:54 +0300
  * [MDEV-11369](https://jira.mariadb.org/browse/MDEV-11369): Test ROW\_FORMAT=COMPRESSED
* [Revision #9a10e7fc6f](https://github.com/MariaDB/server/commit/9a10e7fc6f)\
  2017-10-09 11:34:59 -0400
  * bump the VERSION
* [Revision #6edba392d8](https://github.com/MariaDB/server/commit/6edba392d8)\
  2017-10-09 12:55:01 +0300
  * Work around [MDEV-14029](https://jira.mariadb.org/browse/MDEV-14029) Server does not remove #sql\*.frm files after crash during ALTER TABLE
* [Revision #1a4c63238c](https://github.com/MariaDB/server/commit/1a4c63238c)\
  2017-10-09 08:47:54 +0300
  * [MDEV-14022](https://jira.mariadb.org/browse/MDEV-14022) Upgrade from 10.0/10.1 fails on assertion

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
