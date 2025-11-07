# MariaDB 11.5.1 Changelog

The most recent release of [MariaDB 11.5](../../old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115.md) is:[**MariaDB 11.5.2**](../../old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-2-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.5.2/)

[Download 11.5.1](https://downloads.mariadb.org/mariadb/11.5.1/)[Release Notes](../../old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-1-release-notes.md)[Changelog](mariadb-11-5-1-changelog.md)[Overview of 11.5](../../old-releases/release-notes-mariadb-11-5-rolling-releases/what-is-mariadb-115.md)

**Release date:** 30 May 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-1-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Changes from [11.5.0](../../old-releases/release-notes-mariadb-11-5-rolling-releases/mariadb-11-5-0-release-notes.md) are also included in this changelog
* Includes all fixes from [MariaDB 11.4.2](../11.4/11.4.2.md)
* [Revision #65079ece42](https://github.com/MariaDB/server/commit/65079ece42)\
  2024-05-28 07:27:30 +0400
  * Re-recording `MTR_FEEDBACK_PLUGIN=1 mtr plugins.feedback_plugin_send` results
* [Revision #173edf607d](https://github.com/MariaDB/server/commit/173edf607d)\
  2024-03-15 22:12:30 +0100
  * [MDEV-32218](https://jira.mariadb.org/browse/MDEV-32218) PASSWORD\_EXPIRATION\_TIME column
* [Revision #d229b4af0e](https://github.com/MariaDB/server/commit/d229b4af0e)\
  2024-02-29 16:49:18 +0100
  * [MDEV-23729](https://jira.mariadb.org/browse/MDEV-23729) [MDEV-32218](https://jira.mariadb.org/browse/MDEV-32218) INFORMATION\_SCHEMA table for user data
* [Revision #bec1f32103](https://github.com/MariaDB/server/commit/bec1f32103)\
  2024-05-26 17:40:25 +0200
  * disable failing galera test
* [Revision #d88765e6e8](https://github.com/MariaDB/server/commit/d88765e6e8)\
  2024-05-22 22:39:46 +0200
  * columnstore 23.10.1-2
* [Revision #86055e4243](https://github.com/MariaDB/server/commit/86055e4243)\
  2024-04-15 21:12:26 +0300
  * [MDEV-33913](https://jira.mariadb.org/browse/MDEV-33913) TABLE\_STATISTICS increments ROWS\_CHANGED twice upon UPDATE and does not count DELETE
* [Revision #94033fcf83](https://github.com/MariaDB/server/commit/94033fcf83)\
  2023-12-31 16:32:16 +0200
  * [MDEV-33151](https://jira.mariadb.org/browse/MDEV-33151) Add more columns to TABLE\_STATISTICS and USER STATS
* [Revision #c94451865c](https://github.com/MariaDB/server/commit/c94451865c)\
  2024-05-24 10:09:52 +0200
  * INFORMATION\_SCHEMA.ALL\_PLUGINS: filter away more errors
* [Revision #bfbdc273d2](https://github.com/MariaDB/server/commit/bfbdc273d2)\
  2024-05-21 22:41:37 +0200
  * my\_errno can not be set to EE\_ error numbers
* [Revision #aebd16201f](https://github.com/MariaDB/server/commit/aebd16201f)\
  2024-05-21 21:04:41 +0200
  * don't use session locale for the error log
* [Revision #9cb0bb1de0](https://github.com/MariaDB/server/commit/9cb0bb1de0)\
  2024-05-21 20:35:00 +0200
  * restore the error message that was changed by mistake
* [Revision #443aa52c35](https://github.com/MariaDB/server/commit/443aa52c35)\
  2024-05-21 16:49:35 +0200
  * fix chi error message
* [Revision #fdd27497df](https://github.com/MariaDB/server/commit/fdd27497df)\
  2024-05-21 00:24:35 +0200
  * cleanup: remove redundant code
* [Revision #ce5b8e5944](https://github.com/MariaDB/server/commit/ce5b8e5944)\
  2024-05-21 00:23:51 +0200
  * cleanup: clarify the function name and purpose
* [Revision #d500c22f6d](https://github.com/MariaDB/server/commit/d500c22f6d)\
  2024-05-20 23:11:29 +0200
  * remove double-printing of safemalloc report
* [Revision #381e9adb6c](https://github.com/MariaDB/server/commit/381e9adb6c)\
  2024-05-17 13:42:55 +0300
  * [MDEV-34150](https://jira.mariadb.org/browse/MDEV-34150) Assertion failure in Diagnostics\_area::set\_error\_status upon binary logging hitting tmp space limit
* [Revision #fcb3183479](https://github.com/MariaDB/server/commit/fcb3183479)\
  2024-05-15 14:32:54 +0300
  * [MDEV-34142](https://jira.mariadb.org/browse/MDEV-34142) Server crashes in create\_internal\_tmp\_table with low tmp space limit
* [Revision #46751d4b81](https://github.com/MariaDB/server/commit/46751d4b81)\
  2024-05-03 10:27:35 +0300
  * [MDEV-34060](https://jira.mariadb.org/browse/MDEV-34060) Unexpected behavior upon reading I\_S.ALL\_PLUGINS under limited tmp space.
* [Revision #7d1467e9e9](https://github.com/MariaDB/server/commit/7d1467e9e9)\
  2024-05-02 19:07:41 +0300
  * [MDEV-34054](https://jira.mariadb.org/browse/MDEV-34054) Memory leak in Window\_func\_runner::exec after encountering "temporary space limit reached" error
* [Revision #178ab560ae](https://github.com/MariaDB/server/commit/178ab560ae)\
  2024-04-30 14:38:48 +0300
  * [MDEV-34016](https://jira.mariadb.org/browse/MDEV-34016) Assertion \`info->key\_del\_used == 0' failed in maria\_close with limited tmp space
* [Revision #d2304554ac](https://github.com/MariaDB/server/commit/d2304554ac)\
  2024-04-20 14:02:05 +0300
  * [MDEV-33751](https://jira.mariadb.org/browse/MDEV-33751) Assertion \`thd' failed in int temp\_file\_size\_cb\_func(tmp\_file\_tracking\*, int)
* [Revision #865ef0f567](https://github.com/MariaDB/server/commit/865ef0f567)\
  2024-04-06 12:07:49 +0300
  * [MDEV-33680](https://jira.mariadb.org/browse/MDEV-33680) Server hangs or assertion fails upon SELECT with limited max\_tmp\_space\_usage
* [Revision #b9f5793176](https://github.com/MariaDB/server/commit/b9f5793176)\
  2024-03-14 17:59:00 +0100
  * [MDEV-9101](https://jira.mariadb.org/browse/MDEV-9101) Limit size of created disk temporary files and tables
* [Revision #b60419e0e4](https://github.com/MariaDB/server/commit/b60419e0e4)\
  2024-05-21 00:27:25 +0200
  * fixed that Filesort\_on\_disk in slow query log works again
* [Revision #9c7e57a41b](https://github.com/MariaDB/server/commit/9c7e57a41b)\
  2024-05-03 10:44:41 +0300
  * Improve error message for ER\_CANT\_FIND\_DL\_ENTRY
* [Revision #9293d40fa7](https://github.com/MariaDB/server/commit/9293d40fa7)\
  2024-05-19 16:52:23 +0200
  * [MDEV-33145](https://jira.mariadb.org/browse/MDEV-33145) support for old-mode=OLD\_FLUSH\_STATUS
* [Revision #9ecec1f730](https://github.com/MariaDB/server/commit/9ecec1f730)\
  2024-05-19 16:51:50 +0200
  * cleanup: old\_mode\_deprecated
* [Revision #fd3b7f5eba](https://github.com/MariaDB/server/commit/fd3b7f5eba)\
  2024-05-19 20:06:09 +0200
  * cleanup: make the test more debuggable
* [Revision #775cba4d0f](https://github.com/MariaDB/server/commit/775cba4d0f)\
  2023-12-31 16:23:04 +0200
  * [MDEV-33145](https://jira.mariadb.org/browse/MDEV-33145) Add FLUSH GLOBAL STATUS
* [Revision #d2b39a2c82](https://github.com/MariaDB/server/commit/d2b39a2c82)\
  2023-12-30 12:10:15 +0200
  * Reset some longlong global variables as part of FLUSH STATUS
* [Revision #d7bc28e2a6](https://github.com/MariaDB/server/commit/d7bc28e2a6)\
  2023-12-31 14:10:32 +0200
  * Removed not used variable from log\_grep.inc
* [Revision #f3cb73a4c1](https://github.com/MariaDB/server/commit/f3cb73a4c1)\
  2024-05-26 23:19:11 +0200
  * revert the test change that fais on 32-bit
* [Revision #eb0c719947](https://github.com/MariaDB/server/commit/eb0c719947)\
  2024-04-25 17:46:33 +0000
  * Add GitLab MTR runs to ensure support past 2038
* [Revision #dcbc526a20](https://github.com/MariaDB/server/commit/dcbc526a20)\
  2024-04-25 17:44:43 +0000
  * Alter thr\_timer to allow server startup past 2038
* [Revision #84331c5bd7](https://github.com/MariaDB/server/commit/84331c5bd7)\
  2024-05-14 16:52:29 +0200
  * remove double-declaration of --alter-algorithm
* [Revision #cc758332ba](https://github.com/MariaDB/server/commit/cc758332ba)\
  2024-03-14 20:46:41 +0100
  * ER\_VARIABLE\_DELETED fix typos, adjust wording, fix plugins.
* [Revision #ae9a4799d7](https://github.com/MariaDB/server/commit/ae9a4799d7)\
  2024-04-18 16:29:19 +0300
  * [MDEV-33938](https://jira.mariadb.org/browse/MDEV-33938) Analyze table on sequences should be prohibited
* [Revision #9e7e1f6244](https://github.com/MariaDB/server/commit/9e7e1f6244)\
  2024-05-07 10:47:11 +0300
  * Added 'crash\_error' to Aria for recording of reason for crash)
* [Revision #24c57165d5](https://github.com/MariaDB/server/commit/24c57165d5)\
  2023-12-19 17:51:23 +0200
  * ALTER TABLE and replication should convert old row\_end timestamps to new timestamp range
* [Revision #c4cad8d50c](https://github.com/MariaDB/server/commit/c4cad8d50c)\
  2024-01-29 11:52:44 +0200
  * [MDEV-33449](https://jira.mariadb.org/browse/MDEV-33449) improving repair of tables
* [Revision #2464ee758a](https://github.com/MariaDB/server/commit/2464ee758a)\
  2024-03-12 13:54:30 +0200
  * [MDEV-33655](https://jira.mariadb.org/browse/MDEV-33655) Remove alter\_algorithm
* [Revision #6254fcf84a](https://github.com/MariaDB/server/commit/6254fcf84a)\
  2024-04-21 14:29:31 +0300
  * Fix that one cannot change value for deleted variables
* [Revision #8af7a99443](https://github.com/MariaDB/server/commit/8af7a99443)\
  2024-03-12 18:00:34 +0200
  * Fixed warnings when using deprecated variables
* [Revision #c862416338](https://github.com/MariaDB/server/commit/c862416338)\
  2024-01-21 13:39:27 +0200
  * Updated CONNECT engine to support date and timestamp for the full range.
* [Revision #b879b8a5c8](https://github.com/MariaDB/server/commit/b879b8a5c8)\
  2023-09-18 17:30:22 +0300
  * More windows changes for 32 bit unsigned timestamp:
* [Revision #b8ffd99cee](https://github.com/MariaDB/server/commit/b8ffd99cee)\
  2023-09-18 12:05:41 +0300
  * Extends 64 bit windows to support timestamps up to year 2106.
* [Revision #dfdedd46e4](https://github.com/MariaDB/server/commit/dfdedd46e4)\
  2023-09-11 17:58:22 +0300
  * [MDEV-32188](https://jira.mariadb.org/browse/MDEV-32188) make TIMESTAMP use whole 32-bit unsigned range
* [Revision #ce6cce85d4](https://github.com/MariaDB/server/commit/ce6cce85d4)\
  2024-03-08 15:36:41 +0200
  * [MDEV-33620](https://jira.mariadb.org/browse/MDEV-33620) Improve times and states in show processlist for replication
* [Revision #d2e6fe02d7](https://github.com/MariaDB/server/commit/d2e6fe02d7)\
  2024-02-26 12:10:08 +0200
  * Generate a warning(note) and write to error log if master\_pos\_wait() fails.
* [Revision #153c9173ea](https://github.com/MariaDB/server/commit/153c9173ea)\
  2024-02-26 12:01:42 +0200
  * Print more information when thread loops in read/write in net\_serv.cc
* [Revision #201e28fac1](https://github.com/MariaDB/server/commit/201e28fac1)\
  2024-05-13 17:32:41 +0200
  * cleanup: redundant condition
* [Revision #9f4b745408](https://github.com/MariaDB/server/commit/9f4b745408)\
  2024-05-13 13:53:04 +0200
  * cleanup: optimize is\_system\_table\_name/is\_statistics\_table\_name
* [Revision #0f414f639c](https://github.com/MariaDB/server/commit/0f414f639c)\
  2024-04-18 11:45:21 +0300
  * [MDEV-33881](https://jira.mariadb.org/browse/MDEV-33881) Userstat skips system tables inconsistently
* [Revision #ab513b007b](https://github.com/MariaDB/server/commit/ab513b007b)\
  2024-01-04 20:44:38 +0200
  * Optimize checking if a table is a statistics table
* [Revision #a00e99acca](https://github.com/MariaDB/server/commit/a00e99acca)\
  2024-01-02 17:11:14 +0200
  * [MDEV-33152](https://jira.mariadb.org/browse/MDEV-33152) Add QUERIES to INDEX\_STATISTICS
* [Revision #869e67c92f](https://github.com/MariaDB/server/commit/869e67c92f)\
  2024-05-07 20:38:34 +0200
  * cleanup: remove thd->stmt\_changes\_data
* [Revision #3781848bca](https://github.com/MariaDB/server/commit/3781848bca)\
  2024-05-07 20:08:17 +0200
  * mark the deprecated sysvar deprecated
* [Revision #062eca7424](https://github.com/MariaDB/server/commit/062eca7424)\
  2024-04-29 18:29:35 +0300
  * Allow tests to be run without debug when possible, and on Windows
* [Revision #243b9f3cd2](https://github.com/MariaDB/server/commit/243b9f3cd2)\
  2024-02-20 17:25:40 +0200
  * [MDEV-33501](https://jira.mariadb.org/browse/MDEV-33501) Extend query\_response\_time plugin to be compatible with Percona server
* [Revision #5296f908ed](https://github.com/MariaDB/server/commit/5296f908ed)\
  2024-05-03 19:19:03 +0200
  * [MDEV-28671](https://jira.mariadb.org/browse/MDEV-28671) post-testing fixes
* [Revision #53582238a3](https://github.com/MariaDB/server/commit/53582238a3)\
  2024-03-12 14:08:23 +0100
  * cleanup: remove convert\_dash\_to\_underscore
* [Revision #df10a945fc](https://github.com/MariaDB/server/commit/df10a945fc)\
  2024-03-12 15:26:29 +0100
  * [MDEV-28671](https://jira.mariadb.org/browse/MDEV-28671) post-merge fixes
* [Revision #4186fa72fb](https://github.com/MariaDB/server/commit/4186fa72fb)\
  2023-05-17 19:21:29 +0000
  * [MDEV-28671](https://jira.mariadb.org/browse/MDEV-28671) Enable var deprecation for mysqld help output
* [Revision #25094f339b](https://github.com/MariaDB/server/commit/25094f339b)\
  2024-05-26 16:11:20 +0200
  * after merge fix
* [Revision #78325a25d6](https://github.com/MariaDB/server/commit/78325a25d6)\
  2024-05-27 10:46:46 +0400
  * [MDEV-33696](https://jira.mariadb.org/browse/MDEV-33696) main.dyncol and ctype\_unicode\_casefold\_bmp.inc in --view
* Merge [Revision #b2fc885469](https://github.com/MariaDB/server/commit/b2fc885469) 2024-05-26 20:13:16 +0200 - Merge branch '11.4' into 11.5
* [Revision #18edb0959f](https://github.com/MariaDB/server/commit/18edb0959f)\
  2024-05-25 10:08:09 +0400
  * Fixing mariadb-install-db.exe failure on Windows (Illegal mix of collations)
* [Revision #283b9285c3](https://github.com/MariaDB/server/commit/283b9285c3)\
  2024-03-29 13:28:40 +0400
  * [MDEV-33701](https://jira.mariadb.org/browse/MDEV-33701) upgrades from 11.4 to 11.5 don't work
* [Revision #a0cde3648e](https://github.com/MariaDB/server/commit/a0cde3648e)\
  2024-04-01 10:17:19 +0400
  * [MDEV-33698](https://jira.mariadb.org/browse/MDEV-33698) tests in the jp suite fail
* [Revision #903b5d6a83](https://github.com/MariaDB/server/commit/903b5d6a83)\
  2023-11-02 14:16:09 +0400
  * [MDEV-25829](https://jira.mariadb.org/browse/MDEV-25829) Change default Unicode collation to uca1400\_ai\_ci
* [Revision #a3117c7983](https://github.com/MariaDB/server/commit/a3117c7983)\
  2023-11-15 10:14:28 +0400
  * [MDEV-25829](https://jira.mariadb.org/browse/MDEV-25829) Change default Unicode collation to uca1400\_ai\_ci
* [Revision #1b65cc9da7](https://github.com/MariaDB/server/commit/1b65cc9da7)\
  2023-11-15 06:09:41 +0400
  * [MDEV-25829](https://jira.mariadb.org/browse/MDEV-25829) Change default Unicode collation to uca1400\_ai\_ci
* [Revision #44974a0788](https://github.com/MariaDB/server/commit/44974a0788)\
  2024-05-24 12:26:45 +0200
  * Fix duplicated on merge tests
* [Revision #6c323c7a03](https://github.com/MariaDB/server/commit/6c323c7a03)\
  2024-05-23 21:54:29 +0200
  * Fix version
* [Revision #aee03ea56b](https://github.com/MariaDB/server/commit/aee03ea56b)\
  2024-05-22 09:55:53 -0600
  * 11.5 Fix Merge Conflict Between [MDEV-7850](https://jira.mariadb.org/browse/MDEV-7850) and [MDEV-33672](https://jira.mariadb.org/browse/MDEV-33672)
* Merge [Revision #dd7d9d7fb1](https://github.com/MariaDB/server/commit/dd7d9d7fb1) 2024-05-23 17:01:43 +0200 - Merge branch '11.4' into 11.5
* [Revision #e4afa61053](https://github.com/MariaDB/server/commit/e4afa61053)\
  2023-07-10 18:53:19 +0300
  * [MDEV-7850](https://jira.mariadb.org/browse/MDEV-7850): Extend GTID Binlog Events with Thread Id
* [Revision #f151c5f389](https://github.com/MariaDB/server/commit/f151c5f389)\
  2024-04-29 11:36:11 +0400
  * [MDEV-34025](https://jira.mariadb.org/browse/MDEV-34025) Virtual columns do not check assignment cast validity
* [Revision #f582ea4d5b](https://github.com/MariaDB/server/commit/f582ea4d5b)\
  2024-04-29 14:02:28 +0400
  * A cleanup for [MDEV-12668](https://jira.mariadb.org/browse/MDEV-12668) SRID is not preserved in UNION, VIEW, MIN, MAX
* [Revision #001f93df2b](https://github.com/MariaDB/server/commit/001f93df2b)\
  2024-04-23 12:57:36 +0400
  * [MDEV-12668](https://jira.mariadb.org/browse/MDEV-12668) SRID is not preserved in UNION, VIEW, MIN, MAX
* [Revision #486d42d812](https://github.com/MariaDB/server/commit/486d42d812)\
  2024-04-22 20:39:31 +0300
  * [MDEV-18478](https://jira.mariadb.org/browse/MDEV-18478) ANALYZE for statement should show selectivity of ICP, part#3
* [Revision #86e727b1ee](https://github.com/MariaDB/server/commit/86e727b1ee)\
  2024-04-01 14:32:25 -0400
  * We rely on handler\_stats pointing to a valid active\_handler\_stats instance, for ICP accounting, which is created during ha\_handler\_stats\_reset(). Always invoke that method during table init to ensure that the handler, regardless of implementation, has the pointer set correctly
* [Revision #a11a10191a](https://github.com/MariaDB/server/commit/a11a10191a)\
  2024-03-29 10:25:21 -0400
  * accrue statistics to correct handler
* [Revision #0940a96940](https://github.com/MariaDB/server/commit/0940a96940)\
  2024-02-26 11:32:38 +0300
  * [MDEV-18478](https://jira.mariadb.org/browse/MDEV-18478) ANALYZE for statement should show selectivity of ICP, part#2
* [Revision #e87d1e391b](https://github.com/MariaDB/server/commit/e87d1e391b)\
  2023-12-11 16:06:59 +0300
  * [MDEV-18478](https://jira.mariadb.org/browse/MDEV-18478) ANALYZE for statement should show selectivity of ICP, part#1
* [Revision #3f9182126c](https://github.com/MariaDB/server/commit/3f9182126c)\
  2024-03-15 18:42:06 +0100
  * mysqltest: support MARIADB\_OPT\_RESTRICTED\_AUTH
* [Revision #5d74e43914](https://github.com/MariaDB/server/commit/5d74e43914)\
  2024-03-15 14:48:06 +0100
  * small cleanup: mysqltest
* [Revision #594bd86e3e](https://github.com/MariaDB/server/commit/594bd86e3e)\
  2024-03-15 18:42:56 +0100
  * fix SSL tests for the new C/C 3.4
* [Revision #ea6975b1f1](https://github.com/MariaDB/server/commit/ea6975b1f1)\
  2023-12-04 18:49:39 +0100
  * [MDEV-30366](https://jira.mariadb.org/browse/MDEV-30366) Permit bulk implementation to return ALL individual results
* [Revision #73ed0a23eb](https://github.com/MariaDB/server/commit/73ed0a23eb)\
  2024-03-04 23:12:34 +0100
  * [MDEV-33625](https://jira.mariadb.org/browse/MDEV-33625) Add option --dir to mariadb-dump
* [Revision #901cb2aa2f](https://github.com/MariaDB/server/commit/901cb2aa2f)\
  2024-03-17 15:00:09 +0100
  * reset cached client plugin when it's no longer needed
* [Revision #fd247cc21f](https://github.com/MariaDB/server/commit/fd247cc21f)\
  2023-04-26 15:27:01 +0400
  * [MDEV-31340](https://jira.mariadb.org/browse/MDEV-31340) Remove MY\_COLLATION\_HANDLER::strcasecmp()
* [Revision #159b7ca3f2](https://github.com/MariaDB/server/commit/159b7ca3f2)\
  2024-03-13 11:53:31 +0300
  * [MDEV-12404](https://jira.mariadb.org/browse/MDEV-12404): Add assertions about Index Condition Pushdown use
* [Revision #ee3d4ec414](https://github.com/MariaDB/server/commit/ee3d4ec414)\
  2024-01-31 11:59:21 -0500
  * [MDEV-12404](https://jira.mariadb.org/browse/MDEV-12404) Index condition pushdown on partitioned tables
* [Revision #e0b6db2de7](https://github.com/MariaDB/server/commit/e0b6db2de7)\
  2024-03-01 12:59:21 +1100
  * [MDEV-31609](https://jira.mariadb.org/browse/MDEV-31609) Send initial values of system variables in first OK packet
* [Revision #e32736ec59](https://github.com/MariaDB/server/commit/e32736ec59)\
  2024-03-01 10:10:44 +1100
  * [MDEV-31609](https://jira.mariadb.org/browse/MDEV-31609) mtr: only print session tracking from the last statement
* [Revision #7bec41d25d](https://github.com/MariaDB/server/commit/7bec41d25d)\
  2024-03-26 14:37:17 +1100
  * [MDEV-33734](https://jira.mariadb.org/browse/MDEV-33734) Improve the sequence increment inequality testing
* [Revision #9b02b7c77a](https://github.com/MariaDB/server/commit/9b02b7c77a)\
  2024-04-04 17:13:09 +0400
  * [MDEV-33827](https://jira.mariadb.org/browse/MDEV-33827) UUID() returns a NULL-able result
* [Revision #0c0db46ba2](https://github.com/MariaDB/server/commit/0c0db46ba2)\
  2024-02-29 06:00:46 -0500
  * Update doxygen annotations in `plugin.h`
* [Revision #aba03eef07](https://github.com/MariaDB/server/commit/aba03eef07)\
  2024-03-22 15:29:41 +1100
  * [MDEV-33739](https://jira.mariadb.org/browse/MDEV-33739) Check field type of the first field in check\_sequence\_fields()
* [Revision #593392ba8b](https://github.com/MariaDB/server/commit/593392ba8b)\
  2024-02-21 12:19:26 +1100
  * [MDEV-31789](https://jira.mariadb.org/browse/MDEV-31789) Deprecate spider\_casual\_read
* [Revision #fcd7ae73da](https://github.com/MariaDB/server/commit/fcd7ae73da)\
  2024-03-21 14:45:59 +0100
  * re-enable WITH\_SSL as a backward-compatibility shortcut
* [Revision #71d92723bf](https://github.com/MariaDB/server/commit/71d92723bf)\
  2024-03-21 11:37:12 +0100
  * [MDEV-33696](https://jira.mariadb.org/browse/MDEV-33696) main.dyncol and ctype\_unicode\_casefold\_bmp.inc in --view
* [Revision #f10805fc29](https://github.com/MariaDB/server/commit/f10805fc29)\
  2024-03-21 11:31:24 +0100
  * [MDEV-31531](https://jira.mariadb.org/browse/MDEV-31531) fix wsrep tests after 929c2e06aae4
* [Revision #d0c47cd161](https://github.com/MariaDB/server/commit/d0c47cd161)\
  2024-03-17 10:41:59 +0100
  * wsrep.wsrep\_provider\_plugin\_defaults update to 26.4.17
* [Revision #473ee856d1](https://github.com/MariaDB/server/commit/473ee856d1)\
  2024-03-16 17:18:10 +0100
  * [MDEV-28152](https://jira.mariadb.org/browse/MDEV-28152) fix UBSAN error
* [Revision #2be3b8e8a3](https://github.com/MariaDB/server/commit/2be3b8e8a3)\
  2024-03-16 13:50:44 +0100
  * main.information\_schema-big is neither big nor not\_embedded
* [Revision #14ec1536ac](https://github.com/MariaDB/server/commit/14ec1536ac)\
  2024-03-18 13:30:03 +0100
  * [MDEV-33519](https://jira.mariadb.org/browse/MDEV-33519) Remove WITH\_SSL=\<custom\_location\_of\_openssl> option
* [Revision #1e889a6e6c](https://github.com/MariaDB/server/commit/1e889a6e6c)\
  2024-03-07 12:00:36 +0400
  * [MDEV-33621](https://jira.mariadb.org/browse/MDEV-33621) Unify duplicate code in my\_wildcmp\_uca\_impl() and my\_wildcmp\_unicode\_impl()
* [Revision #9e7afa7782](https://github.com/MariaDB/server/commit/9e7afa7782)\
  2024-03-07 17:08:41 +0400
  * Extra tests for [MDEV-30716](https://jira.mariadb.org/browse/MDEV-30716) Wrong casefolding in xxx\_unicode\_520\_ci for U+0700..U+07FF
* [Revision #929c2e06aa](https://github.com/MariaDB/server/commit/929c2e06aa)\
  2023-06-23 13:24:02 +0400
  * [MDEV-31531](https://jira.mariadb.org/browse/MDEV-31531) Remove my\_casedn\_str() and my\_caseup\_str()
* [Revision #de9c357284](https://github.com/MariaDB/server/commit/de9c357284)\
  2024-01-24 19:28:51 +0100
  * [MDEV-32841](https://jira.mariadb.org/browse/MDEV-32841) Add tests for new counters.
* [Revision #59df9f26bb](https://github.com/MariaDB/server/commit/59df9f26bb)\
  2024-01-23 16:06:37 +0100
  * [MDEV-32841](https://jira.mariadb.org/browse/MDEV-32841) - review fixes
* [Revision #f8bb99bf4a](https://github.com/MariaDB/server/commit/f8bb99bf4a)\
  2024-01-23 15:31:02 +0100
  * [MDEV-32841](https://jira.mariadb.org/browse/MDEV-32841) Use chrono::duration instead of chrono::duration
* [Revision #01466adc13](https://github.com/MariaDB/server/commit/01466adc13)\
  2024-01-09 10:47:33 +0100
  * [MDEV-32841](https://jira.mariadb.org/browse/MDEV-32841) Provide Innodb async IO statistics
* [Revision #374783c3d9](https://github.com/MariaDB/server/commit/374783c3d9)\
  2024-01-04 12:12:50 +1100
  * [MDEV-28152](https://jira.mariadb.org/browse/MDEV-28152) Features for sequences
* [Revision #eeba940311](https://github.com/MariaDB/server/commit/eeba940311)\
  2024-02-16 00:07:33 +0100
  * remove deprecated since 10.4
* [Revision #04f0504831](https://github.com/MariaDB/server/commit/04f0504831)\
  2024-02-15 15:07:19 +0100
  * 11.5 branch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
