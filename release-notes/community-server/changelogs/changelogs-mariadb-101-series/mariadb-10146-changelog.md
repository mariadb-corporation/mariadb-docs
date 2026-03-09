# MariaDB 10.1.46 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.46/)[Release Notes](../../old-releases/10.1/10.1.46.md)[Changelog](mariadb-10146-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 10 Aug 2020

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.46.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #c0ac310e3e](https://github.com/MariaDB/server/commit/c0ac310e3e)\
  2020-08-06 14:02:01 +0200
  * link failure on fulltest (xenial)
* Merge [Revision #a09a06d597](https://github.com/MariaDB/server/commit/a09a06d597) 2020-08-05 01:46:02 +0200 - Merge branch 'merge/merge-tokudb-5.6' into 10.1
* [Revision #2adaaeba83](https://github.com/MariaDB/server/commit/2adaaeba83)\
  2020-08-04 12:44:43 +0200
  * 5.6.49-89.0
* [Revision #e3c18b8e84](https://github.com/MariaDB/server/commit/e3c18b8e84)\
  2020-07-16 14:24:30 +0530
  * [MDEV-23089](https://jira.mariadb.org/browse/MDEV-23089) rpl\_parallel2 fails in 10.5
* [Revision #8bca92c884](https://github.com/MariaDB/server/commit/8bca92c884)\
  2020-08-03 13:03:37 +0300
  * Fix the typo in fix for [MDEV-21472](https://jira.mariadb.org/browse/MDEV-21472)
* [Revision #acfc500d03](https://github.com/MariaDB/server/commit/acfc500d03)\
  2020-08-02 19:42:45 +0200
  * compilation error on bintar-centos6-amd64-debug
* [Revision #dbb4572fe9](https://github.com/MariaDB/server/commit/dbb4572fe9)\
  2020-08-03 02:42:07 +0300
  * [MDEV-23375](https://jira.mariadb.org/browse/MDEV-23375) parts.partition\_debug fails when it's run after another test
* [Revision #7a4287d421](https://github.com/MariaDB/server/commit/7a4287d421)\
  2020-08-02 20:19:53 +0300
  * List of unstable tests for 10.1.46 release
* [Revision #09ec8e2e22](https://github.com/MariaDB/server/commit/09ec8e2e22)\
  2020-07-30 10:07:41 +0200
  * improve the error message for a dropped current role
* [Revision #4635218cb0](https://github.com/MariaDB/server/commit/4635218cb0)\
  2020-07-30 10:01:49 +0200
  * [MDEV-22521](https://jira.mariadb.org/browse/MDEV-22521) Server crashes in traverse\_role\_graph\_up or Assertion \`user' fails in traverse\_role\_graph\_impl
* [Revision #4860fe244b](https://github.com/MariaDB/server/commit/4860fe244b)\
  2020-07-30 11:01:16 +0300
  * XtraDB 5.6.49-89.0
* [Revision #7e9ffc69ec](https://github.com/MariaDB/server/commit/7e9ffc69ec)\
  2020-07-29 23:26:09 +0300
  * [MDEV-21472](https://jira.mariadb.org/browse/MDEV-21472): ALTER TABLE ... ANALYZE PARTITION ... with EITS reads and locks all rows
* [Revision #e54a7ac1b3](https://github.com/MariaDB/server/commit/e54a7ac1b3)\
  2020-07-29 12:17:31 +0200
  * [MDEV-23010](https://jira.mariadb.org/browse/MDEV-23010) UPDATE privilege at Database and Table level fail to update with SELECT command denied to user
* [Revision #2ba70f69fd](https://github.com/MariaDB/server/commit/2ba70f69fd)\
  2020-07-29 12:05:12 +0200
  * cleanup: reduce code duplication
* [Revision #0b5b2f8641](https://github.com/MariaDB/server/commit/0b5b2f8641)\
  2020-07-24 17:43:10 +0200
  * Bug #25207522: INCORRECT ORDER-BY BEHAVIOR ON A PARTITIONED TABLE WITH A COMPOSITE PREFIX INDEX
* [Revision #d5970779fa](https://github.com/MariaDB/server/commit/d5970779fa)\
  2020-06-12 13:53:23 +0200
  * bugfix: mysql\_create\_view() infinite loop
* [Revision #77b7f793f9](https://github.com/MariaDB/server/commit/77b7f793f9)\
  2020-05-17 18:44:23 +0200
  * [MDEV-18496](https://jira.mariadb.org/browse/MDEV-18496) Crash when Aria encryption is enabled but plugin not available
* [Revision #88cbe2f081](https://github.com/MariaDB/server/commit/88cbe2f081)\
  2020-05-17 18:34:22 +0200
  * [MDEV-18496](https://jira.mariadb.org/browse/MDEV-18496) Crash when Aria encryption is enabled but plugin not available
* [Revision #e6cb263ef3](https://github.com/MariaDB/server/commit/e6cb263ef3)\
  2020-07-19 11:10:12 +1000
  * [MDEV-15961](https://jira.mariadb.org/browse/MDEV-15961): Fix stacktraces under FreeBSD (aarch64)
* [Revision #beec8404fa](https://github.com/MariaDB/server/commit/beec8404fa)\
  2020-07-27 11:51:50 +1000
  * [MDEV-17076](https://jira.mariadb.org/browse/MDEV-17076): mtr int options aren't negative
* [Revision #99af3cbc85](https://github.com/MariaDB/server/commit/99af3cbc85)\
  2020-07-22 15:22:14 +1000
  * [MDEV-17076](https://jira.mariadb.org/browse/MDEV-17076): mtr max-{core,datadir} 0 means 0
* [Revision #1ce97358bb](https://github.com/MariaDB/server/commit/1ce97358bb)\
  2018-08-27 16:43:29 +0300
  * [MDEV-17076](https://jira.mariadb.org/browse/MDEV-17076): increment only if saving occurs
* [Revision #c81a2d2322](https://github.com/MariaDB/server/commit/c81a2d2322)\
  2020-07-27 18:54:21 +1000
  * [MDEV-23088](https://jira.mariadb.org/browse/MDEV-23088): Change LimitNOFILE default from 16364 to 16384
* [Revision #29851b677e](https://github.com/MariaDB/server/commit/29851b677e)\
  2020-07-24 17:03:15 +0400
  * [MDEV-23282](https://jira.mariadb.org/browse/MDEV-23282) FLOAT(53,0) badly handles out-of-range values
* [Revision #8460db12b5](https://github.com/MariaDB/server/commit/8460db12b5)\
  2020-07-25 12:59:53 +0300
  * Add testcases for [MDEV-20557](https://jira.mariadb.org/browse/MDEV-20557), [MDEV-21649](https://jira.mariadb.org/browse/MDEV-21649)
* [Revision #b000d6952f](https://github.com/MariaDB/server/commit/b000d6952f)\
  2020-07-24 22:31:29 +0300
  * [MDEV-23221](https://jira.mariadb.org/browse/MDEV-23221): A subquery causes crash
* [Revision #4b97f14a3d](https://github.com/MariaDB/server/commit/4b97f14a3d)\
  2020-07-22 11:20:32 +1000
  * mysql\_install\_db: help lists --defaults-file twice
* [Revision #8ef41c6084](https://github.com/MariaDB/server/commit/8ef41c6084)\
  2020-07-23 14:48:07 +0300
  * [MDEV-23272](https://jira.mariadb.org/browse/MDEV-23272) Galera stack-use-after-scope error with ASAN build
* [Revision #7d22d666d2](https://github.com/MariaDB/server/commit/7d22d666d2)\
  2020-07-20 12:02:00 +0200
  * [MDEV-15207](https://jira.mariadb.org/browse/MDEV-15207): mysql\_upgrade cannot create file mysql\_upgrade\_info
* [Revision #adeb736f9a](https://github.com/MariaDB/server/commit/adeb736f9a)\
  2020-07-23 16:34:38 +0530
  * [MDEV-22903](https://jira.mariadb.org/browse/MDEV-22903) heap-use-after-free while accessing fts cache deleted doc ids
* [Revision #52ccedd6dd](https://github.com/MariaDB/server/commit/52ccedd6dd)\
  2020-07-23 09:59:16 +0300
  * [MDEV-23268](https://jira.mariadb.org/browse/MDEV-23268) SIGSEGV on srv\_monitor\_event if InnoDB is read-only
* [Revision #d2982331a6](https://github.com/MariaDB/server/commit/d2982331a6)\
  2020-07-14 00:42:47 +0200
  * Code comment spellfixes
* [Revision #62d73df6b2](https://github.com/MariaDB/server/commit/62d73df6b2)\
  2020-07-22 14:44:25 +0530
  * [MDEV-19232](https://jira.mariadb.org/browse/MDEV-19232): Floating point precision / value comparison problem
* [Revision #57ec42bc32](https://github.com/MariaDB/server/commit/57ec42bc32)\
  2020-07-17 15:55:45 +0300
  * [MDEV-23190](https://jira.mariadb.org/browse/MDEV-23190) InnoDB data file extension is not crash-safe
* [Revision #98e2c17e9e](https://github.com/MariaDB/server/commit/98e2c17e9e)\
  2020-07-16 16:31:23 +0300
  * Cleanup: Remove fil\_check\_adress\_in\_tablespace()
* [Revision #14543afd59](https://github.com/MariaDB/server/commit/14543afd59)\
  2020-07-16 12:33:20 +0300
  * Cleanup: Remove unused AbstractCallback::m\_free\_limit
* [Revision #c400ef2586](https://github.com/MariaDB/server/commit/c400ef2586)\
  2020-07-17 22:00:36 +0530
  * Making the stat\_tables\_innodb test deterministic
* [Revision #1ba8df4c60](https://github.com/MariaDB/server/commit/1ba8df4c60)\
  2020-07-16 16:31:27 +0200
  * [MDEV-20401](https://jira.mariadb.org/browse/MDEV-20401): revert unnecessary change
* [Revision #4412a461a1](https://github.com/MariaDB/server/commit/4412a461a1)\
  2020-05-12 13:29:17 +0200
  * [MDEV-20401](https://jira.mariadb.org/browse/MDEV-20401): Server incorrectly auto-sets lower\_case\_file\_system value
* [Revision #7473e1841c](https://github.com/MariaDB/server/commit/7473e1841c)\
  2020-05-05 11:57:20 +1000
  * check\_linker\_flag: use for linker flags
* [Revision #dfdfeecb03](https://github.com/MariaDB/server/commit/dfdfeecb03)\
  2020-07-14 12:09:10 +0530
  * [MDEV-22851](https://jira.mariadb.org/browse/MDEV-22851): Engine independent index statistics are incorrect for large tables on Windows
* [Revision #67a03b7c94](https://github.com/MariaDB/server/commit/67a03b7c94)\
  2020-07-14 13:32:32 +0300
  * XtraDB 5.6.48-88.0
* [Revision #142f85142a](https://github.com/MariaDB/server/commit/142f85142a)\
  2020-07-14 13:25:18 +0300
  * Update the InnoDB version number to 5.6.49
* [Revision #8d061996e6](https://github.com/MariaDB/server/commit/8d061996e6)\
  2020-07-14 13:21:01 +0300
  * [MDEV-23161](https://jira.mariadb.org/browse/MDEV-23161) avg\_count\_reset may wrongly be NULL in I\_S.INNODB\_METRICS
* [Revision #dc58987eb7](https://github.com/MariaDB/server/commit/dc58987eb7)\
  2020-07-14 14:26:49 +0530
  * [MDEV-22765](https://jira.mariadb.org/browse/MDEV-22765) i\_s\_fts\_index\_cache\_fill\_one\_index() is not protect by the lock
* [Revision #e80183dbd5](https://github.com/MariaDB/server/commit/e80183dbd5)\
  2020-07-14 13:22:59 +0530
  * [MDEV-15662](https://jira.mariadb.org/browse/MDEV-15662) mariadb-backup.huge\_lsn fails sporadically with "log sequence number is in the future"
* [Revision #194a720e28](https://github.com/MariaDB/server/commit/194a720e28)\
  2020-07-10 17:50:04 +0530
  * [MDEV-22890](https://jira.mariadb.org/browse/MDEV-22890) DEADLOCK of threads detected: row0sel.cc S-LOCK / btr0cur.cc S-LOCK / row0quiesce.cc X-LOCK
* [Revision #f73db93329](https://github.com/MariaDB/server/commit/f73db93329)\
  2020-07-13 19:56:20 +0300
  * [MDEV-23027](https://jira.mariadb.org/browse/MDEV-23027) symlink\_wsrep\_sst\_rsync target built when WITH\_WSREP is off
* [Revision #f18c5a7ed7](https://github.com/MariaDB/server/commit/f18c5a7ed7)\
  2020-07-07 17:58:24 +0300
  * [MDEV-23114](https://jira.mariadb.org/browse/MDEV-23114) AUTH\_PAM plugin can not be disabled when using mysql\_release config
* [Revision #a536625553](https://github.com/MariaDB/server/commit/a536625553)\
  2020-07-01 14:11:31 +0530
  * [MDEV-22654](https://jira.mariadb.org/browse/MDEV-22654): Assertion \`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed in Diagnostics\_area::set\_ok\_status on FUNCTION replace
* [Revision #cad9a9b1f8](https://github.com/MariaDB/server/commit/cad9a9b1f8)\
  2020-07-06 13:51:13 +0200
  * [MDEV-23098](https://jira.mariadb.org/browse/MDEV-23098) mariadb-upgrade-service.exe does not work on WAMPServer
* [Revision #6163af9397](https://github.com/MariaDB/server/commit/6163af9397)\
  2020-07-06 16:29:09 +0530
  * [MDEV-22390](https://jira.mariadb.org/browse/MDEV-22390): Assertion \`m\_next\_rec\_ptr >= m\_rawmem' failed in Filesort\_buffer::spaceleft | SIGSEGV in memmove\_avx\_unaligned\_erms from my\_b\_write
* [Revision #3efdac2064](https://github.com/MariaDB/server/commit/3efdac2064)\
  2020-04-29 13:22:25 +1000
  * [MDEV-22173](https://jira.mariadb.org/browse/MDEV-22173): socket accept - test for failure
* [Revision #c43a666662](https://github.com/MariaDB/server/commit/c43a666662)\
  2020-07-02 06:04:42 +0300
  * Revert "Fix result of merge."
* [Revision #90d1e58ed0](https://github.com/MariaDB/server/commit/90d1e58ed0)\
  2020-07-02 06:04:31 +0300
  * [MDEV-22941](https://jira.mariadb.org/browse/MDEV-22941): Fix the DBUG\_ENTER name
* [Revision #41b0d98e69](https://github.com/MariaDB/server/commit/41b0d98e69)\
  2020-07-01 18:43:21 +0200
  * [MDEV-23067](https://jira.mariadb.org/browse/MDEV-23067) Windows : manually registered services rejected mysql\_upgrade\_service
* [Revision #fe05c16c8d](https://github.com/MariaDB/server/commit/fe05c16c8d)\
  2020-06-30 12:45:37 +0200
  * [MDEV-23052](https://jira.mariadb.org/browse/MDEV-23052) mysql\_install\_db.exe can run on existing non-empty directory, and remove it on error
* [Revision #1ea266f3ef](https://github.com/MariaDB/server/commit/1ea266f3ef)\
  2020-06-29 15:39:01 +0300
  * [MDEV-23003](https://jira.mariadb.org/browse/MDEV-23003) INFORMATION\_SCHEMA.INNODB\_TABLESPACES\_ENCRYPTION requires SUPER instead PROCESS privilege
* [Revision #ca55e09e9a](https://github.com/MariaDB/server/commit/ca55e09e9a)\
  2020-06-23 15:37:41 +1000
  * signal handler: use mariadb kb URL rather than MySQL one
* [Revision #37cb7a0071](https://github.com/MariaDB/server/commit/37cb7a0071)\
  2020-06-27 12:55:55 +0530
  * [MDEV-17606](https://jira.mariadb.org/browse/MDEV-17606): Query returns wrong results (while using CHARACTER SET utf8)
* [Revision #3bc8939552](https://github.com/MariaDB/server/commit/3bc8939552)\
  2020-06-17 10:48:28 +0530
  * [MDEV-22806](https://jira.mariadb.org/browse/MDEV-22806): MSAN reports use-of-uninitialized-value for rpl\_parallel\_conflicts.test
* Merge [Revision #bebc576422](https://github.com/MariaDB/server/commit/bebc576422) 2020-06-25 10:12:06 +0200 - Merge branch '10.1-[MDEV-22763](https://jira.mariadb.org/browse/MDEV-22763)' of [mariadb-server](https://github.com/codership/mariadb-server) into 10.1-[MDEV-22763](https://jira.mariadb.org/browse/MDEV-22763)
* [Revision #12f6db967b](https://github.com/MariaDB/server/commit/12f6db967b)\
  2020-06-01 12:34:33 +0300
  * [MDEV-22763](https://jira.mariadb.org/browse/MDEV-22763) backporting [MDEV-20225](https://jira.mariadb.org/browse/MDEV-20225) fix into 10.1
* [Revision #7ee6a3ae5f](https://github.com/MariaDB/server/commit/7ee6a3ae5f)\
  2020-06-25 09:58:42 +0200
  * [MDEV-22950](https://jira.mariadb.org/browse/MDEV-22950) followup
* [Revision #f1838434b8](https://github.com/MariaDB/server/commit/f1838434b8)\
  2020-05-29 11:36:28 +0530
  * [MDEV-22706](https://jira.mariadb.org/browse/MDEV-22706): Assertion \`!current' failed in PROFILING::start\_new\_query
* [Revision #9fb8d87d2d](https://github.com/MariaDB/server/commit/9fb8d87d2d)\
  2020-06-24 09:38:54 +0300
  * Test fixes.
* [Revision #8e58eeba78](https://github.com/MariaDB/server/commit/8e58eeba78)\
  2020-04-29 13:41:46 +0300
  * MTR tests to test Galera fix for node joining over several configuration changes.
* [Revision #e0793d3865](https://github.com/MariaDB/server/commit/e0793d3865)\
  2020-06-23 13:42:11 +0200
  * Fix result of merge.
* [Revision #37c88445e3](https://github.com/MariaDB/server/commit/37c88445e3)\
  2020-03-31 07:57:53 +1100
  * mtr: use env for perl
* [Revision #b1b9803cb8](https://github.com/MariaDB/server/commit/b1b9803cb8)\
  2020-06-20 01:01:50 +0200
  * Disable dtrace probes on Windows.
* [Revision #727252ff1b](https://github.com/MariaDB/server/commit/727252ff1b)\
  2020-06-20 01:00:36 +0200
  * [MDEV-22950](https://jira.mariadb.org/browse/MDEV-22950) : fix race condition in dbug
* [Revision #26907e7ef1](https://github.com/MariaDB/server/commit/26907e7ef1)\
  2020-06-19 16:04:45 +0400
  * [MDEV-22941](https://jira.mariadb.org/browse/MDEV-22941) Assertion \`idx < array.elements' failed in Dynamic\_array\<st\_mysql\_const\_lex\_string\*>::at
* [Revision #bf74f7f9ff](https://github.com/MariaDB/server/commit/bf74f7f9ff)\
  2020-06-15 15:57:01 +0530
  * [MDEV-20428](https://jira.mariadb.org/browse/MDEV-20428): "Start binlog\_dump" message doesn't indicate GTID position
* [Revision #93cee30309](https://github.com/MariaDB/server/commit/93cee30309)\
  2020-06-15 16:01:41 +0300
  * Check for krb5\_xfree instead of krb5\_free\_unparsed\_name
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
* [Revision #f30ff10c8d](https://github.com/MariaDB/server/commit/f30ff10c8d)\
  2020-05-29 00:32:08 +0530
  * [MDEV-22715](https://jira.mariadb.org/browse/MDEV-22715): SIGSEGV in radixsort\_for\_str\_ptr and in native\_compare/my\_qsort2 (optimized builds)
* [Revision #3f019d1771](https://github.com/MariaDB/server/commit/3f019d1771)\
  2020-06-03 14:14:08 +0200
  * Added missing include files to check for debug\_sync
* [Revision #8ec0e9111a](https://github.com/MariaDB/server/commit/8ec0e9111a)\
  2020-06-01 12:34:33 +0300
  * [MDEV-22763](https://jira.mariadb.org/browse/MDEV-22763) backporting [MDEV-20225](https://jira.mariadb.org/browse/MDEV-20225) fix into 10.1
* [Revision #40dbf0ea0e](https://github.com/MariaDB/server/commit/40dbf0ea0e)\
  2020-05-23 22:38:20 +0200
  * Fix duplicate word
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
* [Revision #dbe447a789](https://github.com/MariaDB/server/commit/dbe447a789)\
  2020-05-05 20:32:32 +0300
  * [MDEV-15152](https://jira.mariadb.org/browse/MDEV-15152) Optimistic parallel slave doesnt cope well with START SLAVE UNTIL
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
* [Revision #cb9c49a9b2](https://github.com/MariaDB/server/commit/cb9c49a9b2)\
  2020-05-21 18:16:27 +0400
  * [MDEV-22111](https://jira.mariadb.org/browse/MDEV-22111) ERROR 1064 & 1033 and SIGSEGV on CREATE TABLE w/ various charsets on 10.4/5 optimized builds | Assertion \`(uint) (table\_check\_constraints - share->check\_constraints) == (uint) (share->table\_check\_constraints - share->field\_check\_constraints)' failed
* [Revision #836d708997](https://github.com/MariaDB/server/commit/836d708997)\
  2020-05-19 11:22:39 +0530
  * [MDEV-22451](https://jira.mariadb.org/browse/MDEV-22451): SIGSEGV in memmove\_avx\_unaligned\_erms/memcpy from \_my\_b\_write on CREATE after RESET MASTER
* [Revision #a6b4d4beff](https://github.com/MariaDB/server/commit/a6b4d4beff)\
  2020-05-20 09:37:05 +0000
  * [MDEV-22631](https://jira.mariadb.org/browse/MDEV-22631) fix
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
* [Revision #44c8d84908](https://github.com/MariaDB/server/commit/44c8d84908)\
  2020-05-15 21:49:57 +0300
  * [MDEV-22520](https://jira.mariadb.org/browse/MDEV-22520) Assertion `gathered_length == thd->lex->comment.length` failed in binlog\_defragment
* [Revision #7baa40dffa](https://github.com/MariaDB/server/commit/7baa40dffa)\
  2020-05-18 16:37:51 +1000
  * [MDEV-21976](https://jira.mariadb.org/browse/MDEV-21976): mtr main.udf - broaden localhost (#1543)
* [Revision #3df297271a](https://github.com/MariaDB/server/commit/3df297271a)\
  2020-05-15 20:16:58 +0400
  * [MDEV-22579](https://jira.mariadb.org/browse/MDEV-22579) No error when inserting DEFAULT(non\_virtual\_column) into a virtual column
* [Revision #efd68f5e31](https://github.com/MariaDB/server/commit/efd68f5e31)\
  2020-05-11 19:56:14 +0530
  * [MDEV-22498](https://jira.mariadb.org/browse/MDEV-22498): SIGSEGV in Bitmap<64u>::merge on SELECT
* [Revision #ee5152fc4b](https://github.com/MariaDB/server/commit/ee5152fc4b)\
  2020-05-14 17:41:37 +0300
  * [MDEV-22070](https://jira.mariadb.org/browse/MDEV-22070) MSAN use-of-uninitialized-value in encryption.innodb-redo-badkey
* [Revision #31f34b20f3](https://github.com/MariaDB/server/commit/31f34b20f3)\
  2020-05-14 11:41:27 +0400
  * [MDEV-22502](https://jira.mariadb.org/browse/MDEV-22502) MDB crashes in CREATE TABLE AS SELECT when the precision of returning type = 0.
* [Revision #910c31928e](https://github.com/MariaDB/server/commit/910c31928e)\
  2020-05-13 18:46:28 +0400
  * [MDEV-22503](https://jira.mariadb.org/browse/MDEV-22503) MDB limits DECIMAL column precision to 16 doing CTAS with floor/ceil over DECIMAL(X,Y) where X > 16
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

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
