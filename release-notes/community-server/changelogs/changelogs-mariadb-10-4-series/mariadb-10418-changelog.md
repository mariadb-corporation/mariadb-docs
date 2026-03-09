# MariaDB 10.4.18 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.18](https://downloads.mariadb.org/mariadb/10.4.18/)[Release Notes](../../old-releases/10.4/10.4.18.md)[Changelog](mariadb-10418-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 22 Feb 2021

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.18.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.28](../changelogs-mariadb-10-3-series/mariadb-10328-changelog.md)
* Merge [Revision #53123dfa3e](https://github.com/MariaDB/server/commit/53123dfa3e) 2021-02-18 23:17:50 +0100 - Merge branch 'bb-10.3-release' into bb-10.4-release
* [Revision #2696538723](https://github.com/MariaDB/server/commit/2696538723)\
  2021-02-12 17:31:25 +0100
  * updating @@wsrep\_cluster\_address deadlocks
* [Revision #b91e77cff3](https://github.com/MariaDB/server/commit/b91e77cff3)\
  2021-02-12 11:29:40 +0100
  * fix a 3-way deadlock in galera\_sr.galera-features#56
* [Revision #259b945204](https://github.com/MariaDB/server/commit/259b945204)\
  2021-02-12 15:05:24 +0100
  * remove find\_thread\_with\_thd\_data\_lock\_callback
* [Revision #eac8341df4](https://github.com/MariaDB/server/commit/eac8341df4)\
  2021-02-07 17:48:58 +0100
  * [MDEV-23328](https://jira.mariadb.org/browse/MDEV-23328) Server hang due to Galera lock conflict resolution
* [Revision #9703cffa8c](https://github.com/MariaDB/server/commit/9703cffa8c)\
  2021-02-05 14:59:27 +0100
  * don't take mutexes conditionally
* [Revision #259a1902a0](https://github.com/MariaDB/server/commit/259a1902a0)\
  2021-02-05 15:00:38 +0100
  * cleanup: THD::abort\_current\_cond\_wait()
* [Revision #cbbcc8fa2b](https://github.com/MariaDB/server/commit/cbbcc8fa2b)\
  2021-02-08 23:36:06 +0200
  * List of unstable tests for 10.4.18 release
* Merge [Revision #00a313ecf3](https://github.com/MariaDB/server/commit/00a313ecf3) 2021-02-12 17:44:22 +0100 - Merge branch 'bb-10.3-release' into bb-10.4-release
* [Revision #ef5adf5207](https://github.com/MariaDB/server/commit/ef5adf5207)\
  2021-02-04 16:06:54 +0100
  * [MDEV-24274](https://jira.mariadb.org/browse/MDEV-24274) ALTER TABLE with CHECK CONSTRAINTS gives "Out of Memory" error
* [Revision #c2c23e598d](https://github.com/MariaDB/server/commit/c2c23e598d)\
  2021-01-27 09:11:46 +0200
  * Update galera.disabled.def file
* [Revision #1398160a71](https://github.com/MariaDB/server/commit/1398160a71)\
  2021-01-26 14:41:23 +0300
  * [MDEV-24522](https://jira.mariadb.org/browse/MDEV-24522) Assertion \`inited==NONE' fails upon UPDATE on versioned table with unique blob
* [Revision #e626f511f9](https://github.com/MariaDB/server/commit/e626f511f9)\
  2021-01-25 14:56:38 +0200
  * [MDEV-24653](https://jira.mariadb.org/browse/MDEV-24653) fixup: Make the test deterministic
* Merge [Revision #5db3827689](https://github.com/MariaDB/server/commit/5db3827689) 2021-01-25 14:43:07 +0200 - Merge 10.3 into 10.4
* [Revision #0c3d264207](https://github.com/MariaDB/server/commit/0c3d264207)\
  2021-01-25 13:56:10 +0200
  * instant\_alter\_debug: Cover everything with innodb\_instant\_alter\_column
* Merge [Revision #3467f63764](https://github.com/MariaDB/server/commit/3467f63764) 2021-01-25 11:02:07 +0200 - Merge 10.3 into 10.4
* [Revision #ce141d0714](https://github.com/MariaDB/server/commit/ce141d0714)\
  2021-01-22 12:12:42 +0200
  * [MDEV-24463](https://jira.mariadb.org/browse/MDEV-24463) : galera.galera\_sst\_mysqldump\_with\_key MTR failed: 'INSERT failed: 1213: Deadlock found when trying to get lock
* [Revision #be5fce16a0](https://github.com/MariaDB/server/commit/be5fce16a0)\
  2021-01-19 10:00:05 +0200
  * [MDEV-24596](https://jira.mariadb.org/browse/MDEV-24596) : Assertion \`state\_ == s\_exec || state\_ == s\_quitting' failed in wsrep::client\_state::disable\_streaming
* [Revision #9377e9ba0c](https://github.com/MariaDB/server/commit/9377e9ba0c)\
  2021-01-14 18:18:06 +0200
  * [MDEV-21153](https://jira.mariadb.org/browse/MDEV-21153) Replica nodes crash due to indexed virtual columns and FK cascading delete
* [Revision #8bcddb02b7](https://github.com/MariaDB/server/commit/8bcddb02b7)\
  2021-01-19 16:08:46 +0700
  * [MDEV-24577](https://jira.mariadb.org/browse/MDEV-24577): Fix warnings generated during compilation of plugin/auth\_pam/testing/pam\_mariadb\_mtr.c on FreeBSD
* [Revision #b87828b6c8](https://github.com/MariaDB/server/commit/b87828b6c8)\
  2021-01-14 11:26:28 +0200
  * [MDEV-22285](https://jira.mariadb.org/browse/MDEV-22285) : Assertion \`xid\_seqno > wsrep\_seqno' failed in trx\_rseg\_update\_wsrep\_checkpoint on SET @@global.wsrep\_start\_position
* [Revision #4afab3c725](https://github.com/MariaDB/server/commit/4afab3c725)\
  2021-01-13 13:08:07 +0200
  * [MDEV-18542](https://jira.mariadb.org/browse/MDEV-18542) : galera\_sr.galera-features#56: Test failure: signal 6; mysqltest: Can't connect to local MySQL server
* [Revision #403818f466](https://github.com/MariaDB/server/commit/403818f466)\
  2021-01-13 08:45:03 +0200
  * [MDEV-21523](https://jira.mariadb.org/browse/MDEV-21523) : galera.[MDEV-16509](https://jira.mariadb.org/browse/MDEV-16509) MTR failed: timeout after 900 seconds: Can't connect to local MySQL server
* [Revision #7789726843](https://github.com/MariaDB/server/commit/7789726843)\
  2021-01-12 13:01:07 +0200
  * [MDEV-24447](https://jira.mariadb.org/browse/MDEV-24447) : galera.galera\_toi\_lock\_shared MTR failed: WSREP: ALTER TABLE isolation failure
* [Revision #ffc384e044](https://github.com/MariaDB/server/commit/ffc384e044)\
  2021-01-12 11:50:31 +0530
  * [MDEV-23804](https://jira.mariadb.org/browse/MDEV-23804): Server crashes in st\_select\_lex::collect\_grouping\_fields\_for\_derived
* Merge [Revision #fd5e103aa4](https://github.com/MariaDB/server/commit/fd5e103aa4) 2021-01-11 10:35:06 +0200 - Merge 10.3 into 10.4
* [Revision #a131b976b2](https://github.com/MariaDB/server/commit/a131b976b2)\
  2021-01-08 15:05:07 +0100
  * Fix MTR test galera\_as\_slave\_replay
* [Revision #26d913a743](https://github.com/MariaDB/server/commit/26d913a743)\
  2021-01-08 08:44:18 +0200
  * Update wsrep-lib
* [Revision #033f8d13ce](https://github.com/MariaDB/server/commit/033f8d13ce)\
  2020-12-30 23:51:29 +0200
  * Update wsrep-lib (new logger interface) Ensure consistent use of logging macros in wsrep-related code
* [Revision #7edbd27258](https://github.com/MariaDB/server/commit/7edbd27258)\
  2021-01-04 18:24:06 +0200
  * [MDEV-24500](https://jira.mariadb.org/browse/MDEV-24500): Added wait condition to make sure table t1 is replicated to node\_2.
* [Revision #d67e17bb81](https://github.com/MariaDB/server/commit/d67e17bb81)\
  2021-01-02 16:11:55 +0200
  * [MDEV-24512](https://jira.mariadb.org/browse/MDEV-24512) Assertion failed in rec\_is\_metadata() in btr\_discard\_only\_page\_on\_level()
* [Revision #734c587f68](https://github.com/MariaDB/server/commit/734c587f68)\
  2021-01-01 19:17:03 +0200
  * [MDEV-20386](https://jira.mariadb.org/browse/MDEV-20386): Allow RDRAND, RDSEED WITH\_MSAN
* [Revision #c1a7a82bca](https://github.com/MariaDB/server/commit/c1a7a82bca)\
  2021-01-01 19:15:46 +0200
  * WolfSSL v4.6.0-stable
* Merge [Revision #3454b5cf35](https://github.com/MariaDB/server/commit/3454b5cf35) 2020-12-29 14:32:58 +0100 - Merge branch '10.3' into 10.4
* [Revision #4601e6e565](https://github.com/MariaDB/server/commit/4601e6e565)\
  2020-10-29 16:30:52 +0200
  * [MDEV-24255](https://jira.mariadb.org/browse/MDEV-24255) MTR test galera\_bf\_abort fails with --ps-protocol
* Merge [Revision #a64cb6d265](https://github.com/MariaDB/server/commit/a64cb6d265) 2020-12-28 13:46:22 +0200 - Merge 10.3 into 10.4
* Merge [Revision #478b83032b](https://github.com/MariaDB/server/commit/478b83032b) 2020-12-25 09:13:28 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #0aa02567dd](https://github.com/MariaDB/server/commit/0aa02567dd) 2020-12-23 14:52:59 +0200 - Merge 10.3 into 10.4
* [Revision #04741dc736](https://github.com/MariaDB/server/commit/04741dc736)\
  2020-12-21 14:44:56 +0100
  * MENT-1047 Assertion \`active() == false' failed with "XA START.."
* [Revision #b79b3ff655](https://github.com/MariaDB/server/commit/b79b3ff655)\
  2020-10-02 11:39:27 +0200
  * [MDEV-23468](https://jira.mariadb.org/browse/MDEV-23468): inline\_mysql\_socket\_send: Assertion \`mysql\_socket.fd != -1' failed on shutdown
* [Revision #41a961d85c](https://github.com/MariaDB/server/commit/41a961d85c)\
  2020-12-02 20:52:35 +0200
  * [MDEV-24327](https://jira.mariadb.org/browse/MDEV-24327) wsrep XID checkpointing order violation with cert failures
* [Revision #87fa6d2c5c](https://github.com/MariaDB/server/commit/87fa6d2c5c)\
  2020-12-02 17:28:49 +0200
  * [MDEV-24327](https://jira.mariadb.org/browse/MDEV-24327) wsrep XID checkpointing order with log\_slave\_updates=OFF
* [Revision #d4c35fb21b](https://github.com/MariaDB/server/commit/d4c35fb21b)\
  2020-10-24 21:01:07 +1100
  * [MDEV-24207](https://jira.mariadb.org/browse/MDEV-24207): recognise mysql forms of invalid password for mysql\_native\_password
* [Revision #0ea650022d](https://github.com/MariaDB/server/commit/0ea650022d)\
  2020-12-14 19:50:48 +0200
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) Update Galera disabled.def file
* [Revision #e9d86d80be](https://github.com/MariaDB/server/commit/e9d86d80be)\
  2020-12-11 14:32:08 +0100
  * issue ER\_USER\_IS\_BLOCKED also for non-existent users
* [Revision #dcc7f93965](https://github.com/MariaDB/server/commit/dcc7f93965)\
  2020-12-11 22:45:54 +0300
  * [MDEV-21958](https://jira.mariadb.org/browse/MDEV-21958): Query having many NOT-IN clauses running forever, part 3
* [Revision #502bc77f23](https://github.com/MariaDB/server/commit/502bc77f23)\
  2020-12-11 22:44:13 +0300
  * [MDEV-21958](https://jira.mariadb.org/browse/MDEV-21958): Query having many NOT-IN clauses running forever, part 2
* [Revision #4addd31531](https://github.com/MariaDB/server/commit/4addd31531)\
  2020-12-11 18:54:21 +0300
  * [MDEV-21958](https://jira.mariadb.org/browse/MDEV-21958): Query having many NOT-IN clauses running forever
* [Revision #0adbf27f00](https://github.com/MariaDB/server/commit/0adbf27f00)\
  2020-12-11 17:33:44 +0300
  * Run innodb.innodb\_stats test with EITS disabled.
* [Revision #e007fcf59d](https://github.com/MariaDB/server/commit/e007fcf59d)\
  2020-12-08 11:59:58 +0530
  * [MDEV-19716](https://jira.mariadb.org/browse/MDEV-19716): ASAN use-after-poison in Query\_log\_event::Query\_log\_event / THD::log\_events\_and\_free\_tmp\_shares
* [Revision #a50cb4867a](https://github.com/MariaDB/server/commit/a50cb4867a)\
  2020-12-02 11:34:37 +0300
  * [MDEV-24334](https://jira.mariadb.org/browse/MDEV-24334) make monitor\_set\_tbl global variable thread-safe
* [Revision #fccd810404](https://github.com/MariaDB/server/commit/fccd810404)\
  2020-12-02 09:58:50 +0300
  * [MDEV-24333](https://jira.mariadb.org/browse/MDEV-24333) Data race in os\_file\_pread at os/os0file.cc:3308 on os\_n\_file\_reads
* [Revision #24ec8eaf66](https://github.com/MariaDB/server/commit/24ec8eaf66)\
  2020-12-02 16:16:29 +0200
  * [MDEV-15532](https://jira.mariadb.org/browse/MDEV-15532) after-merge fixes from Monty
* Merge [Revision #589cf8dbf3](https://github.com/MariaDB/server/commit/589cf8dbf3) 2020-12-01 19:51:14 +0200 - Merge 10.3 into 10.4
* [Revision #a3531775b1](https://github.com/MariaDB/server/commit/a3531775b1)\
  2020-11-30 19:53:58 +0200
  * [MDEV-15532](https://jira.mariadb.org/browse/MDEV-15532) Assertion \`!log->same\_pk' failed in row\_log\_table\_apply\_delete
* [Revision #6261b1f45e](https://github.com/MariaDB/server/commit/6261b1f45e)\
  2020-11-30 19:49:06 +0200
  * Fixed maria.create test
* [Revision #7effcb8ed6](https://github.com/MariaDB/server/commit/7effcb8ed6)\
  2020-11-21 21:12:22 +0530
  * [MDEV-23846](https://jira.mariadb.org/browse/MDEV-23846): O\_TMPFILE error in mysqlbinlog stream output breaks restore
* [Revision #031e1427ed](https://github.com/MariaDB/server/commit/031e1427ed)\
  2020-11-17 11:10:53 +0200
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659): Update Galera disabled.def file
* [Revision #6f50f51e60](https://github.com/MariaDB/server/commit/6f50f51e60)\
  2020-11-18 14:21:12 +0200
  * [MDEV-21494](https://jira.mariadb.org/browse/MDEV-21494) : Galera test sporadic failure on galera.galera\_defaults
* [Revision #60035bd2f1](https://github.com/MariaDB/server/commit/60035bd2f1)\
  2020-10-29 09:42:58 +0100
  * Make test galera\_parallel\_apply\_3nodes deterministic
* [Revision #3897ce2396](https://github.com/MariaDB/server/commit/3897ce2396)\
  2020-11-17 12:21:40 +0200
  * [MDEV-21523](https://jira.mariadb.org/browse/MDEV-21523) : galera.[MDEV-16509](https://jira.mariadb.org/browse/MDEV-16509) MTR failed: timeout after 900 seconds: Can't connect to local MySQL server
* [Revision #b04be43ead](https://github.com/MariaDB/server/commit/b04be43ead)\
  2020-11-17 09:21:11 +0200
  * [MDEV-24165](https://jira.mariadb.org/browse/MDEV-24165) : Galera test failure on galera\_var\_ignore\_apply\_errors
* [Revision #bbf0b55c17](https://github.com/MariaDB/server/commit/bbf0b55c17)\
  2020-11-17 18:13:47 +0200
  * Work around [MDEV-24232](https://jira.mariadb.org/browse/MDEV-24232): Skip perfschema.nesting if WITH\_WSREP=OFF
* [Revision #796f708f85](https://github.com/MariaDB/server/commit/796f708f85)\
  2020-11-17 19:23:33 +0700
  * [MDEV-24115](https://jira.mariadb.org/browse/MDEV-24115) Fix -Wconversion in Timeval::Timeval() on Mac OS X
* Merge [Revision #f0c9903795](https://github.com/MariaDB/server/commit/f0c9903795) 2020-11-17 13:56:20 +0200 - Merge 10.3 into 10.4
* [Revision #1ae7809a7c](https://github.com/MariaDB/server/commit/1ae7809a7c)\
  2020-11-13 11:38:17 +0100
  * Restore autoincrement offset in MTR test [MDEV-24063](https://jira.mariadb.org/browse/MDEV-24063)
* Merge [Revision #1bebc8de5d](https://github.com/MariaDB/server/commit/1bebc8de5d) 2020-11-14 10:05:23 +0100 - Merge branch '10.3' into 10.4
* Merge [Revision #749ecedfec](https://github.com/MariaDB/server/commit/749ecedfec) 2020-11-13 20:45:28 +0200 - [MDEV-24188](https://jira.mariadb.org/browse/MDEV-24188): Merge 10.3 into 10.4
* Merge [Revision #b63dc3f370](https://github.com/MariaDB/server/commit/b63dc3f370) 2020-11-13 20:43:54 +0200 - [MDEV-23619](https://jira.mariadb.org/browse/MDEV-23619): Merge 10.3 into 10.4
* Merge [Revision #b2029c0300](https://github.com/MariaDB/server/commit/b2029c0300) 2020-11-12 15:39:02 +0530 - Merge branch '10.3' into 10.4
* Merge [Revision #972dc6ee98](https://github.com/MariaDB/server/commit/972dc6ee98) 2020-11-12 11:18:04 +0200 - Merge 10.3 into 10.4
* [Revision #2fbcddbeaf](https://github.com/MariaDB/server/commit/2fbcddbeaf)\
  2020-11-09 12:41:52 +0200
  * [MDEV-24119](https://jira.mariadb.org/browse/MDEV-24119) MDL BF-BF Conflict caused by TRUNCATE TABLE
* [Revision #ad432ef4c0](https://github.com/MariaDB/server/commit/ad432ef4c0)\
  2020-11-04 13:42:18 +0200
  * [MDEV-24119](https://jira.mariadb.org/browse/MDEV-24119) MDL BF-BF Conflict caused by TRUNCATE TABLE
* Merge [Revision #99a9774754](https://github.com/MariaDB/server/commit/99a9774754) 2020-11-11 17:26:51 +0200 - Merge mariadb-10.4.17 into 10.4
* [Revision #940db6abc8](https://github.com/MariaDB/server/commit/940db6abc8)\
  2020-11-11 10:19:27 -0500
  * bump the VERSION
* [Revision #83f3d12fcd](https://github.com/MariaDB/server/commit/83f3d12fcd)\
  2020-10-01 11:18:54 +0200
  * Update wsrep-lib
* [Revision #3a5cf14def](https://github.com/MariaDB/server/commit/3a5cf14def)\
  2020-11-09 19:47:44 +0100
  * [MDEV-24175](https://jira.mariadb.org/browse/MDEV-24175) Windows - fix detection of SSD
* [Revision #4e24b3187c](https://github.com/MariaDB/server/commit/4e24b3187c)\
  2020-11-10 14:19:01 +0200
  * [MDEV-19951](https://jira.mariadb.org/browse/MDEV-19951) followup: Remove unused st\_handler\_tablename, tablename\_compare
* [Revision #f5d2d455a6](https://github.com/MariaDB/server/commit/f5d2d455a6)\
  2020-11-07 10:13:17 +1100
  * [MDEV-24098](https://jira.mariadb.org/browse/MDEV-24098) (Oracle mode) CREATE USER/ALTER USER PASSWORD EXPIRE/LOCK in either order
* [Revision #add6782636](https://github.com/MariaDB/server/commit/add6782636)\
  2020-11-04 15:25:00 +1100
  * [MDEV-24098](https://jira.mariadb.org/browse/MDEV-24098) CREATE USER/ALTER USER PASSWORD EXPIRE/LOCK in either order
* [Revision #fd7569ea6b](https://github.com/MariaDB/server/commit/fd7569ea6b)\
  2020-11-04 13:39:38 +1100
  * [MDEV-24098](https://jira.mariadb.org/browse/MDEV-24098): SHOW CREATE USER invalid for both PASSWORD and LOCKED
* [Revision #b13fe8e51b](https://github.com/MariaDB/server/commit/b13fe8e51b)\
  2020-10-16 14:33:22 +0000
  * [MDEV-18842](https://jira.mariadb.org/browse/MDEV-18842): Unfortunate error message when the same column is used for application period start and end
* [Revision #0f04f61395](https://github.com/MariaDB/server/commit/0f04f61395)\
  2020-11-04 09:28:02 +0200
  * Need more information about mysql-wsrep#198 sporadic test failure.
* [Revision #1f1fa07cd5](https://github.com/MariaDB/server/commit/1f1fa07cd5)\
  2020-10-30 13:45:27 +0100
  * [MDEV-24063](https://jira.mariadb.org/browse/MDEV-24063) Assertion during graceful shutdown with wsrep\_on=OFF
* [Revision #4d6c661144](https://github.com/MariaDB/server/commit/4d6c661144)\
  2020-10-27 12:45:42 +0200
  * [MDEV-21577](https://jira.mariadb.org/browse/MDEV-21577) MDL BF-BF conflict
* [Revision #5739c7702d](https://github.com/MariaDB/server/commit/5739c7702d)\
  2020-11-03 10:59:26 -0500
  * bump the VERSION
* Merge [Revision #533a13af06](https://github.com/MariaDB/server/commit/533a13af06) 2020-11-03 14:49:17 +0200 - Merge 10.3 into 10.4
* [Revision #4b3690b504](https://github.com/MariaDB/server/commit/4b3690b504)\
  2020-11-03 14:46:54 +0200
  * fixup 67cb7ea22ac1a510dcbaf9bc48f0f8cf9e0ce8f5
* [Revision #67cb7ea22a](https://github.com/MariaDB/server/commit/67cb7ea22a)\
  2020-11-03 09:12:06 +0200
  * Clean up wsrep.variables
* [Revision #4489b66afb](https://github.com/MariaDB/server/commit/4489b66afb)\
  2020-10-30 13:48:21 +0200
  * [MDEV-23872](https://jira.mariadb.org/browse/MDEV-23872) Crash in galera::TrxHandle::state()
* [Revision #9e14a2df8c](https://github.com/MariaDB/server/commit/9e14a2df8c)\
  2020-11-02 16:04:46 +0200
  * [MDEV-24072](https://jira.mariadb.org/browse/MDEV-24072) Assertion 'ib\_table.n\_v\_cols' failed in instant\_alter\_column\_possible()
* [Revision #5b779c220d](https://github.com/MariaDB/server/commit/5b779c220d)\
  2020-07-16 16:31:59 +1000
  * [MDEV-22974](https://jira.mariadb.org/browse/MDEV-22974): mysql\_native\_password make "invalid" valid

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
