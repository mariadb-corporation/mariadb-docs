# MariaDB 10.2.35 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download 10.2.35](https://downloads.mariadb.org/mariadb/10.2.35/)[Release Notes](../../old-releases/10.2/10.2.35.md)[Changelog](mariadb-10235-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 3 Nov 2020

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.35.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Includes all fixes from [MariaDB 10.1.48](../changelogs-mariadb-101-series/mariadb-10148-changelog.md)
* [Revision #6d3792a9a2](https://github.com/MariaDB/server/commit/6d3792a9a2)\
  2020-10-31 19:49:24 +0200
  * List of unstable tests for 10.2.35 release
* [Revision #72eea39d4c](https://github.com/MariaDB/server/commit/72eea39d4c)\
  2020-10-30 12:58:16 +0200
  * [MDEV-23991](https://jira.mariadb.org/browse/MDEV-23991) fixup: Initialize the memory
* [Revision #fbcd7c0c06](https://github.com/MariaDB/server/commit/fbcd7c0c06)\
  2020-10-30 12:22:23 +0200
  * Update Connector/C
* [Revision #5a0c34e4c2](https://github.com/MariaDB/server/commit/5a0c34e4c2)\
  2020-10-30 14:56:57 +0530
  * [MDEV-24033](https://jira.mariadb.org/browse/MDEV-24033): SIGSEGV in `memcmp_avx2_movbe from queue_insert | SIGSEGV in memcmp_avx2_movbe` from native\_compare
* [Revision #5482d62760](https://github.com/MariaDB/server/commit/5482d62760)\
  2020-10-30 09:19:29 +0200
  * Fix sporadic test failure on galera\_parallel\_apply\_3nodes.
* [Revision #a90b15837c](https://github.com/MariaDB/server/commit/a90b15837c)\
  2020-10-29 22:20:21 +0100
  * [MDEV-19838](https://jira.mariadb.org/browse/MDEV-19838): fix of error messages
* [Revision #f9b0ee07ef](https://github.com/MariaDB/server/commit/f9b0ee07ef)\
  2020-10-29 22:19:32 +0100
  * [MDEV-19838](https://jira.mariadb.org/browse/MDEV-19838): followup, fix for PS & embedded
* Merge [Revision #2e5450af05](https://github.com/MariaDB/server/commit/2e5450af05) 2020-10-29 15:16:53 +0100 - Merge branch '10.1' into 10.2
* [Revision #17cf27f5b6](https://github.com/MariaDB/server/commit/17cf27f5b6)\
  2020-10-26 18:08:58 +0100
  * remove non-working debug assert
* [Revision #4b854d4795](https://github.com/MariaDB/server/commit/4b854d4795)\
  2020-10-27 22:26:41 +0100
  * [MDEV-19838](https://jira.mariadb.org/browse/MDEV-19838) Wrong direxec param data caused crash
* [Revision #6cb88685c4](https://github.com/MariaDB/server/commit/6cb88685c4)\
  2020-10-27 20:03:41 +0300
  * [MDEV-24026](https://jira.mariadb.org/browse/MDEV-24026): InnoDB: Failing assertion: os\_total\_large\_mem\_allocated >= size upon incremental backup
* [Revision #9e3e4c0e04](https://github.com/MariaDB/server/commit/9e3e4c0e04)\
  2020-10-28 20:54:29 +0100
  * new CC
* [Revision #d5c9f84dfc](https://github.com/MariaDB/server/commit/d5c9f84dfc)\
  2020-10-28 14:00:37 +0200
  * [MDEV-22707](https://jira.mariadb.org/browse/MDEV-22707) : galera got stuck after flush tables
* Merge [Revision #65e26bc1ba](https://github.com/MariaDB/server/commit/65e26bc1ba) 2020-10-28 10:56:38 +0100 - Merge branch '10.1' into 10.2
* [Revision #cc5f4428b8](https://github.com/MariaDB/server/commit/cc5f4428b8)\
  2020-10-28 08:13:06 +0200
  * [MDEV-23693](https://jira.mariadb.org/browse/MDEV-23693) fixup: Remove unused btr\_search\_t::withdraw\_clock
* [Revision #527ade2590](https://github.com/MariaDB/server/commit/527ade2590)\
  2020-10-28 07:27:18 +0200
  * [MDEV-23163](https://jira.mariadb.org/browse/MDEV-23163) Merge new release of InnoDB 5.7.32 to 10.2
* [Revision #afc9d00c66](https://github.com/MariaDB/server/commit/afc9d00c66)\
  2020-10-27 12:24:55 +0300
  * [MDEV-23991](https://jira.mariadb.org/browse/MDEV-23991) dict\_table\_stats\_lock() has unnecessarily long scope
* [Revision #42e1815ad8](https://github.com/MariaDB/server/commit/42e1815ad8)\
  2020-10-27 15:35:04 +0200
  * [MDEV-16952](https://jira.mariadb.org/browse/MDEV-16952) Introduce SET GLOBAL innodb\_max\_purge\_lag\_wait
* [Revision #8761571a71](https://github.com/MariaDB/server/commit/8761571a71)\
  2020-10-27 00:30:39 +0400
  * [MDEV-22524](https://jira.mariadb.org/browse/MDEV-22524) SIGABRT in safe\_mutex\_unlock with session\_track\_system\_variables and max\_relay\_log\_size.
* [Revision #bc540b8706](https://github.com/MariaDB/server/commit/bc540b8706)\
  2020-10-27 17:56:49 +0530
  * [MDEV-23693](https://jira.mariadb.org/browse/MDEV-23693) Failing assertion: my\_atomic\_load32\_explicit(\&lock->lock\_word, MY\_MEMORY\_ORDER\_RELAXED) == X\_LOCK\_DECR
* [Revision #6a614d6934](https://github.com/MariaDB/server/commit/6a614d6934)\
  2020-10-21 09:48:52 +0200
  * [MDEV-22707](https://jira.mariadb.org/browse/MDEV-22707): galera got stuck after flush tables
* [Revision #1ff8588c3f](https://github.com/MariaDB/server/commit/1ff8588c3f)\
  2020-08-28 18:18:25 +0530
  * Bug #31228694 FTS QUERY WITH LIMIT HIT AN ASSERT
* [Revision #e391417f0f](https://github.com/MariaDB/server/commit/e391417f0f)\
  2020-10-26 12:21:29 +0200
  * Bug #30933728 INNODB FTS PHRASE SEARCH HIT AN ASSERT
* Merge [Revision #784473b986](https://github.com/MariaDB/server/commit/784473b986) 2020-10-26 09:08:44 +0100 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #dc3a693b70](https://github.com/MariaDB/server/commit/dc3a693b70)\
  2020-10-18 17:20:44 +0200\
  \*
  * Inline MakePtr and MakeOff with OFFSET as size\_t Also add a new member Saved\_Size in the Global structure. modified: storage/connect/global.h modified: storage/connect/plugutil.cpp modified: storage/connect/user\_connect.cc modified: storage/connect/jsonudf.cpp
* [Revision #5d2ddef26e](https://github.com/MariaDB/server/commit/5d2ddef26e)\
  2020-10-06 12:50:12 +0200
  * Fix search for json subtable in tabjson.cpp
* [Revision #d4138e7eed](https://github.com/MariaDB/server/commit/d4138e7eed)\
  2020-10-05 15:21:58 +0200
  * Fix compile error in tabjson.cpp (ULONG -> ulong)
* [Revision #307258c8ee](https://github.com/MariaDB/server/commit/307258c8ee)\
  2020-10-05 12:29:51 +0200\
  \*
  * Use BIN type when charset='binary' modified: storage/connect/ha\_connect.cc
* [Revision #c6eb127ca8](https://github.com/MariaDB/server/commit/c6eb127ca8)\
  2020-10-03 19:06:05 +0200\
  \*
  * Fix allocating work space larger than 4GB The variable connect\_work\_size is now ulong or ulonglong for 64bit machines. modified: storage/connect/ha\_connect.cc modified: storage/connect/user\_connect.cc
* [Revision #99ab562a92](https://github.com/MariaDB/server/commit/99ab562a92)\
  2020-10-01 19:18:26 +0200\
  \*
  * Make possible to allocate work space larger than 4GB All variables handling sizes that were uint are now size\_t. The variable connect\_work\_size is now ulong (was uint); Also make Json functiosn to allocate a larger memory (M=9 was 7) modified: storage/connect/global.h modified: storage/connect/ha\_connect.cc modified: storage/connect/json.cpp modified: storage/connect/jsonudf.cpp modified: storage/connect/plgdbutl.cpp modified: storage/connect/plugutil.cpp modified: storage/connect/user\_connect.cc
* [Revision #2fdc50367c](https://github.com/MariaDB/server/commit/2fdc50367c)\
  2020-10-25 19:18:54 +0100
  * remove disable\_abort\_on\_error from precedence.test
* [Revision #3ba8f619e4](https://github.com/MariaDB/server/commit/3ba8f619e4)\
  2020-10-25 11:47:16 +0530
  * [MDEV-23370](https://jira.mariadb.org/browse/MDEV-23370) innodb\_fts.innodb\_fts\_misc failed in buildbot, server crashed in dict\_table\_autoinc\_destroy
* [Revision #987df9b37a](https://github.com/MariaDB/server/commit/987df9b37a)\
  2020-10-25 11:48:34 +0200
  * [MDEV-23720](https://jira.mariadb.org/browse/MDEV-23720) Change innodb\_log\_optimize\_ddl=OFF by default
* [Revision #4e987b1c6b](https://github.com/MariaDB/server/commit/4e987b1c6b)\
  2020-04-22 20:13:21 +0200
  * [MDEV-22313](https://jira.mariadb.org/browse/MDEV-22313): Neither SHOW CREATE USER nor SHOW GRANTS prints a user's default role
* [Revision #64fe9d6d9a](https://github.com/MariaDB/server/commit/64fe9d6d9a)\
  2020-10-24 11:10:37 +0300
  * Do not leak memory in the skipped [MDEV-23768](https://jira.mariadb.org/browse/MDEV-23768) unit test
* [Revision #b94e8e4b25](https://github.com/MariaDB/server/commit/b94e8e4b25)\
  2020-10-23 12:32:49 +0530
  * [MDEV-23867](https://jira.mariadb.org/browse/MDEV-23867): insert... select crash in compute\_window\_func
* [Revision #5a9df1550f](https://github.com/MariaDB/server/commit/5a9df1550f)\
  2020-10-12 13:38:59 +0300
  * [MDEV-23941](https://jira.mariadb.org/browse/MDEV-23941): strings/json\_lib.c:893:12: style: Suspicious condition
* [Revision #8894dae1df](https://github.com/MariaDB/server/commit/8894dae1df)\
  2020-10-19 12:57:44 +0200
  * [MDEV-17408](https://jira.mariadb.org/browse/MDEV-17408) VIEW is incorrectly defined for a combination of = and BETWEEN
* [Revision #05a878c139](https://github.com/MariaDB/server/commit/05a878c139)\
  2020-10-05 12:50:51 +0200
  * precedence bugfixing
* [Revision #7f974e5ad3](https://github.com/MariaDB/server/commit/7f974e5ad3)\
  2020-10-16 15:07:34 +0200
  * cleanup: remove redundant BANG\_PRECEDENCE
* [Revision #8c83e6eadf](https://github.com/MariaDB/server/commit/8c83e6eadf)\
  2020-10-16 14:32:14 +0200
  * cleanup: remove redundant ADDINTERVAL\_PRECEDENCE
* [Revision #9ad4e0d6d8](https://github.com/MariaDB/server/commit/9ad4e0d6d8)\
  2020-10-14 14:00:09 +0200
  * A fairly exhastive test for operator precedence
* [Revision #71a5857291](https://github.com/MariaDB/server/commit/71a5857291)\
  2020-10-05 13:11:12 +0200
  * cleanup: move precedence tests into precedence\_bugs.test
* [Revision #2cd5df8c83](https://github.com/MariaDB/server/commit/2cd5df8c83)\
  2020-10-01 16:35:55 +0200
  * [MDEV-23656](https://jira.mariadb.org/browse/MDEV-23656) view: removal of parentheses results in wrong result
* [Revision #15f03c2041](https://github.com/MariaDB/server/commit/15f03c2041)\
  2020-08-31 09:54:46 +0200
  * [MDEV-23492](https://jira.mariadb.org/browse/MDEV-23492) performance\_schema\_digests\_size changing from default to 5000 when enabling performance\_schema
* [Revision #1cabfe2c2b](https://github.com/MariaDB/server/commit/1cabfe2c2b)\
  2020-10-23 15:45:04 +0200
  * .gitignore
* [Revision #e864e6b181](https://github.com/MariaDB/server/commit/e864e6b181)\
  2020-10-23 15:44:07 +0200
  * compilation failure with new C/C
* [Revision #4654501e00](https://github.com/MariaDB/server/commit/4654501e00)\
  2020-10-23 20:01:50 +0700
  * [MDEV-23926](https://jira.mariadb.org/browse/MDEV-23926): Follow-up patch
* [Revision #58da04b261](https://github.com/MariaDB/server/commit/58da04b261)\
  2020-10-23 19:15:22 +0700
  * [MDEV-23926](https://jira.mariadb.org/browse/MDEV-23926): Follow-up patch
* [Revision #79f6f0c4fc](https://github.com/MariaDB/server/commit/79f6f0c4fc)\
  2020-10-23 18:42:26 +0700
  * [MDEV-23564](https://jira.mariadb.org/browse/MDEV-23564): CMAKE failing due to deprecated Apple GSS method
* [Revision #1a70c2c73a](https://github.com/MariaDB/server/commit/1a70c2c73a)\
  2020-10-23 18:10:16 +0700
  * [MDEV-23926](https://jira.mariadb.org/browse/MDEV-23926): Follow-up patch to add missed file plugin/auth\_pam/config.h.cmake
* [Revision #5e7cde41e0](https://github.com/MariaDB/server/commit/5e7cde41e0)\
  2020-10-23 17:21:10 +0700
  * [MDEV-23926](https://jira.mariadb.org/browse/MDEV-23926): Follow-up patch to cleanup plugin/auth\_pam/CMakeLists.txt code
* [Revision #6dc14453c5](https://github.com/MariaDB/server/commit/6dc14453c5)\
  2020-10-23 17:18:39 +0700
  * [MDEV-23926](https://jira.mariadb.org/browse/MDEV-23926): Fix warnings generated during compilation of plugin/auth\_pam/mapper/pam\_user\_map.c on MacOS
* [Revision #985ede9203](https://github.com/MariaDB/server/commit/985ede9203)\
  2020-10-20 13:05:58 +0300
  * [MDEV-20755](https://jira.mariadb.org/browse/MDEV-20755) InnoDB: Database page corruption on disk or a failed file read of tablespace upon prepare of mariadb-backup incremental backup
* [Revision #cc1646dae8](https://github.com/MariaDB/server/commit/cc1646dae8)\
  2020-10-22 14:00:17 +0400
  * [MDEV-19443](https://jira.mariadb.org/browse/MDEV-19443) server\_audit plugin doesn't log proxy users.
* [Revision #21ea14db8c](https://github.com/MariaDB/server/commit/21ea14db8c)\
  2020-10-22 15:51:14 +0400
  * [MDEV-20593](https://jira.mariadb.org/browse/MDEV-20593) SIGSEGV in report\_json\_error\_ex (on optimized builds).
* Merge [Revision #620ea816ad](https://github.com/MariaDB/server/commit/620ea816ad) 2020-10-21 14:02:04 +0300 - Merge 10.1 into 10.2
* [Revision #a1b6691f93](https://github.com/MariaDB/server/commit/a1b6691f93)\
  2020-10-21 17:43:23 +0700
  * [MDEV-23925](https://jira.mariadb.org/browse/MDEV-23925): Fixed warnings generated during compilation of mysys\_ssl/openssl.c on MacOS
* [Revision #0049d5b515](https://github.com/MariaDB/server/commit/0049d5b515)\
  2020-10-20 19:11:15 +0300
  * Revert [MDEV-23484](https://jira.mariadb.org/browse/MDEV-23484) Rollback unnecessarily acquires dict\_operation\_lock
* [Revision #832a6acb72](https://github.com/MariaDB/server/commit/832a6acb72)\
  2020-10-20 18:31:56 +0300
  * [MDEV-23996](https://jira.mariadb.org/browse/MDEV-23996) Race conditions in SHOW ENGINE INNODB MUTEX
* [Revision #d1af93a5e8](https://github.com/MariaDB/server/commit/d1af93a5e8)\
  2020-10-17 14:33:04 +0200
  * Update mtr help
* [Revision #888010d9dd](https://github.com/MariaDB/server/commit/888010d9dd)\
  2020-03-24 14:55:07 +0100
  * [MDEV-21951](https://jira.mariadb.org/browse/MDEV-21951): mariadb-backup SST fail if data-directory have lost+found directory
* [Revision #692a44b309](https://github.com/MariaDB/server/commit/692a44b309)\
  2020-10-20 12:01:37 +0200
  * [MDEV-23327](https://jira.mariadb.org/browse/MDEV-23327): followup
* [Revision #1066312a12](https://github.com/MariaDB/server/commit/1066312a12)\
  2020-10-19 20:36:05 +0300
  * [MDEV-23982](https://jira.mariadb.org/browse/MDEV-23982): mariadb-backup hangs on backup
* [Revision #f4f00e7c40](https://github.com/MariaDB/server/commit/f4f00e7c40)\
  2020-10-19 19:37:03 +0530
  * [MDEV-23966](https://jira.mariadb.org/browse/MDEV-23966) btr\_search\_sys->hash\_tables accessed without taking proper ahi latch
* [Revision #923ecbdfef](https://github.com/MariaDB/server/commit/923ecbdfef)\
  2020-10-19 19:36:00 +0530
  * [MDEV-23387](https://jira.mariadb.org/browse/MDEV-23387) dict\_load\_foreign() fails to load the table during alter
* [Revision #bba22543b1](https://github.com/MariaDB/server/commit/bba22543b1)\
  2020-07-29 21:54:24 +0200
  * [MDEV-23327](https://jira.mariadb.org/browse/MDEV-23327) Can't uninstall UDF if the implementation library file doesn't exist
* [Revision #95bb3cb886](https://github.com/MariaDB/server/commit/95bb3cb886)\
  2020-10-06 17:43:13 +0200
  * [MDEV-16676](https://jira.mariadb.org/browse/MDEV-16676) Using malloc-lib=jemalloc in [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) causes non-critical error about missing mysql\_config on startup
* [Revision #db02c458c9](https://github.com/MariaDB/server/commit/db02c458c9)\
  2020-10-17 13:13:01 +0300
  * Clean up some encryption tests
* [Revision #ebb39bc59c](https://github.com/MariaDB/server/commit/ebb39bc59c)\
  2020-10-13 13:37:33 +0200
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659): Update Galera disabled.def file
* [Revision #31201dcbaf](https://github.com/MariaDB/server/commit/31201dcbaf)\
  2020-10-13 13:33:47 +0200
  * [MDEV-21770](https://jira.mariadb.org/browse/MDEV-21770): `galera_3nodes.galera_ipv6_mariadb-backup` fails
* [Revision #24c5af6758](https://github.com/MariaDB/server/commit/24c5af6758)\
  2020-10-14 15:55:16 +0200
  * Fix the constants names
* [Revision #ff8ffef3e1](https://github.com/MariaDB/server/commit/ff8ffef3e1)\
  2020-10-02 11:09:01 +1000
  * [MDEV-23201](https://jira.mariadb.org/browse/MDEV-23201): mysql\_upgrade order mysql.user for 5.7 cross-upgrade
* [Revision #4383c705ab](https://github.com/MariaDB/server/commit/4383c705ab)\
  2020-10-14 21:30:15 +0300
  * [MDEV-23960](https://jira.mariadb.org/browse/MDEV-23960) UBSAN ../storage/innobase/buf/buf0buddy.cc:350:6: runtime error: index 4096 out of bounds for type 'byte \[38]'
* [Revision #e98a5e166c](https://github.com/MariaDB/server/commit/e98a5e166c)\
  2020-10-14 19:01:17 +0300
  * [MDEV-23955](https://jira.mariadb.org/browse/MDEV-23955) main.multi\_update\_big times out
* [Revision #4a97e25aec](https://github.com/MariaDB/server/commit/4a97e25aec)\
  2020-09-29 15:26:04 +0200
  * minor fixes of rpl\_start\_stop\_slave and rpl\_slave\_grp\_exec tests, expanding rpl\_gtid\_delete\_domain for easier later analysis
* [Revision #52dad6fd26](https://github.com/MariaDB/server/commit/52dad6fd26)\
  2020-10-13 03:23:46 +0300
  * [MDEV-21584](https://jira.mariadb.org/browse/MDEV-21584) Linux aio returned OS error 22
* [Revision #222e1b806f](https://github.com/MariaDB/server/commit/222e1b806f)\
  2020-10-10 11:06:59 +0300
  * Add missing file.
* [Revision #a3eddd9f11](https://github.com/MariaDB/server/commit/a3eddd9f11)\
  2020-10-08 13:35:06 +0300
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) : Update Galera disabled.def file
* [Revision #fc3b5c7db3](https://github.com/MariaDB/server/commit/fc3b5c7db3)\
  2020-10-06 14:46:47 +0300
  * [MDEV-17585](https://jira.mariadb.org/browse/MDEV-17585) : wsrep.variables failed in buildbot with deadlock on CREATE USER
* [Revision #266bf77bc7](https://github.com/MariaDB/server/commit/266bf77bc7)\
  2020-10-06 13:40:14 +0300
  * [MDEV-19968](https://jira.mariadb.org/browse/MDEV-19968) : Galera test failure on galera\_load\_data
* [Revision #8984d77910](https://github.com/MariaDB/server/commit/8984d77910)\
  2020-10-02 10:00:59 +0530
  * [MDEV-21329](https://jira.mariadb.org/browse/MDEV-21329) InnoDB: Failing assertion: lock->lock\_word.load(std::memory\_order\_relaxed) == X\_LOCK\_DECR upon server shutdown
* Merge [Revision #b18921cfd2](https://github.com/MariaDB/server/commit/b18921cfd2) 2020-10-07 18:40:50 +0200 - Merge tag 'mariadb-10.2.34' into 10.2
* [Revision #4aec143ad8](https://github.com/MariaDB/server/commit/4aec143ad8)\
  2020-10-07 11:23:43 -0400
  * bump the VERSION
* [Revision #291be49474](https://github.com/MariaDB/server/commit/291be49474)\
  2020-09-24 22:02:00 -0700
  * [MDEV-23811](https://jira.mariadb.org/browse/MDEV-23811): With large number of indexes optimizer chooses an inefficient plan
* [Revision #1595189250](https://github.com/MariaDB/server/commit/1595189250)\
  2020-10-06 22:35:43 +0300
  * [MDEV-23897](https://jira.mariadb.org/browse/MDEV-23897) SIGSEGV on commit with innodb\_lock\_schedule\_algorithm=VATS
* [Revision #2b832151ad](https://github.com/MariaDB/server/commit/2b832151ad)\
  2020-10-06 15:07:06 +0300
  * [MDEV-23787](https://jira.mariadb.org/browse/MDEV-23787) mtr --rr fixes
* [Revision #5933081d8b](https://github.com/MariaDB/server/commit/5933081d8b)\
  2020-10-02 17:30:02 +0200
  * [MDEV-18163](https://jira.mariadb.org/browse/MDEV-18163) Assertion `table_share->tmp_table != NO_TMP_TABLE || m_lock_type != 2' failed in handler::ha_rnd_next(); / Assertion` table\_list->table' failed in find\_field\_in\_table\_ref / ERROR 1901 (on optimized builds)
* [Revision #b3a9fbdbab](https://github.com/MariaDB/server/commit/b3a9fbdbab)\
  2020-10-06 17:07:52 +1100
  * travis: 10.2 only - make faster
* [Revision #350c9eb705](https://github.com/MariaDB/server/commit/350c9eb705)\
  2020-10-06 13:50:26 +0300
  * [MDEV-23894](https://jira.mariadb.org/browse/MDEV-23894) UBSAN: several call to function show\_binlog\_vars(THD\*, st\_mysql\_show\_var\*, char\*) through pointer to incorrect function type 'int (\*)(THD \*, st\_mysql\_show\_var \*, void \*, system\_status\_var \*, enum\_var\_type) errors
* [Revision #33f19876a2](https://github.com/MariaDB/server/commit/33f19876a2)\
  2020-10-06 12:03:13 +0300
  * [MDEV-18593](https://jira.mariadb.org/browse/MDEV-18593) : galera.galera\_gcache\_recover\_full\_gcache: Test failure: galera\_gcache\_recover\_full\_gcache.test: assert\_grep.inc failed
* [Revision #577c61e8be](https://github.com/MariaDB/server/commit/577c61e8be)\
  2020-10-06 07:47:11 +0300
  * [MDEV-23888](https://jira.mariadb.org/browse/MDEV-23888): Potential server hang on replication with InnoDB
* [Revision #01ffccd6a4](https://github.com/MariaDB/server/commit/01ffccd6a4)\
  2020-10-05 20:01:05 +0300
  * UBSAN: UndefinedBehaviorSanitizer: undefined-behavior ../sql/item\_cmpfunc.cc:3650:14
* [Revision #0aef658dfa](https://github.com/MariaDB/server/commit/0aef658dfa)\
  2020-10-05 10:34:01 +0300
  * Remove unnecessary and incorrect add\_suppression. Changes to be committed: modified: mysql-test/suite/sys\_vars/r/wsrep\_cluster\_address\_basic.result modified: mysql-test/suite/sys\_vars/t/wsrep\_cluster\_address\_basic.test
* [Revision #295e2d500b](https://github.com/MariaDB/server/commit/295e2d500b)\
  2020-10-05 09:34:27 +0300
  * [MDEV-16664](https://jira.mariadb.org/browse/MDEV-16664): Add deprecation warning for innodb\_lock\_schedule\_algorithm=VATS
* [Revision #199bc67144](https://github.com/MariaDB/server/commit/199bc67144)\
  2020-10-05 09:12:12 +0300
  * Cleanup: Remove unused SYNC\_REC\_LOCK
* [Revision #34cf947ef2](https://github.com/MariaDB/server/commit/34cf947ef2)\
  2020-10-03 12:38:19 +0300
  * UBSAN UndefinedBehaviorSanitizer: undefined-behavior ../mysys/hash.c:798:9
* [Revision #dab56d5e8e](https://github.com/MariaDB/server/commit/dab56d5e8e)\
  2020-10-03 00:24:53 +0200
  * [MDEV-23879](https://jira.mariadb.org/browse/MDEV-23879) server hangs with threadpool, compression, and client pipelining
* [Revision #b8b1aef6b1](https://github.com/MariaDB/server/commit/b8b1aef6b1)\
  2020-10-02 08:40:06 +0300
  * Cleanup: Orphan que\_thr\_mutex declaration
* [Revision #46890349bf](https://github.com/MariaDB/server/commit/46890349bf)\
  2020-10-02 08:36:50 +0300
  * Cleanup: Remove fts\_t::bg\_threads\_mutex, fts\_t::bg\_threads
* [Revision #d6b33ea237](https://github.com/MariaDB/server/commit/d6b33ea237)\
  2020-09-30 18:02:29 +0530
  * [MDEV-23856](https://jira.mariadb.org/browse/MDEV-23856) fts\_optimize\_wq accessed after shutdown of FTS Optimize thread
* [Revision #cd5f4d2a59](https://github.com/MariaDB/server/commit/cd5f4d2a59)\
  2020-09-30 13:26:46 +0300
  * Cleanup: Remove unused fts\_cache\_t::optimize\_lock
* [Revision #aa2f263e59](https://github.com/MariaDB/server/commit/aa2f263e59)\
  2020-09-29 11:07:34 +0300
  * Cleanup: Remove constant parameters async=false, index\_name=NULL
* [Revision #74bd3683ca](https://github.com/MariaDB/server/commit/74bd3683ca)\
  2020-09-29 11:04:12 +0300
  * [MDEV-23839](https://jira.mariadb.org/browse/MDEV-23839) innodb\_fast\_shutdown=0 hang on change buffer merge
* Merge [Revision #a441b06489](https://github.com/MariaDB/server/commit/a441b06489) 2020-09-29 10:04:37 +0300 - Merge 10.1 into 10.2
* [Revision #842616532a](https://github.com/MariaDB/server/commit/842616532a)\
  2020-09-28 14:39:24 +0300
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) : Update Galera disabled.def file
* Merge [Revision #3a5e719e00](https://github.com/MariaDB/server/commit/3a5e719e00) 2020-09-28 14:03:46 +0530 - Merge branch '10.1' into 10.2
* [Revision #c078f55f47](https://github.com/MariaDB/server/commit/c078f55f47)\
  2020-09-28 11:05:09 +0300
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) : Update Galera disabled.def file
* [Revision #7c5519c12d](https://github.com/MariaDB/server/commit/7c5519c12d)\
  2020-09-23 12:47:49 +0300
  * [MDEV-22387](https://jira.mariadb.org/browse/MDEV-22387): Do not violate attribute((nonnull))
* [Revision #70960bd33d](https://github.com/MariaDB/server/commit/70960bd33d)\
  2020-09-23 12:42:30 +0300
  * UBSAN: Fix a bit shift overflow
* [Revision #af40a2b43e](https://github.com/MariaDB/server/commit/af40a2b43e)\
  2020-09-23 12:27:56 +0300
  * Fix GCC 10.2.0 -Og -fsanitize=undefined -Wmaybe-uninitialized
* [Revision #0448558a0d](https://github.com/MariaDB/server/commit/0448558a0d)\
  2020-09-23 12:14:05 +0300
  * Fix GCC 10.2.0 -Og -fsanitize=undefined -Wformat-overflow
* [Revision #594c11fffc](https://github.com/MariaDB/server/commit/594c11fffc)\
  2020-09-01 12:49:09 +0200
  * Ukrainian error text translations added.
* Merge [Revision #9d0ee2dcb7](https://github.com/MariaDB/server/commit/9d0ee2dcb7) 2020-09-22 15:21:43 +0300 - Merge 10.1 into 10.2
* [Revision #78efa10930](https://github.com/MariaDB/server/commit/78efa10930)\
  2020-09-22 13:55:36 +0300
  * [MDEV-22939](https://jira.mariadb.org/browse/MDEV-22939): Restore an AUTO\_INCREMENT check
* [Revision #3eb81136e1](https://github.com/MariaDB/server/commit/3eb81136e1)\
  2020-09-22 13:40:05 +0300
  * [MDEV-22939](https://jira.mariadb.org/browse/MDEV-22939) Server crashes in row\_make\_new\_pathname()
* [Revision #e5e83daf32](https://github.com/MariaDB/server/commit/e5e83daf32)\
  2020-09-22 13:09:51 +0300
  * Make DISCARD TABLESPACE more robust
* [Revision #2af8f712de](https://github.com/MariaDB/server/commit/2af8f712de)\
  2020-09-22 13:08:09 +0300
  * [MDEV-23776](https://jira.mariadb.org/browse/MDEV-23776): Re-apply the fix and make the test more robust
* [Revision #732cd7fd53](https://github.com/MariaDB/server/commit/732cd7fd53)\
  2020-09-22 11:13:51 +0300
  * [MDEV-23705](https://jira.mariadb.org/browse/MDEV-23705) Assertion 'table->data\_dir\_path || !space'
* [Revision #eb38b1f703](https://github.com/MariaDB/server/commit/eb38b1f703)\
  2020-09-22 10:41:06 +0300
  * Revert "[MDEV-23776](https://jira.mariadb.org/browse/MDEV-23776) Test encryption.create\_or\_replace fails with a warning"
* [Revision #e05650e686](https://github.com/MariaDB/server/commit/e05650e686)\
  2020-09-21 16:35:28 +0300
  * [MDEV-23776](https://jira.mariadb.org/browse/MDEV-23776): Add the reduced encryption.create\_or\_replace test
* [Revision #407d170c92](https://github.com/MariaDB/server/commit/407d170c92)\
  2020-09-21 16:29:29 +0300
  * [MDEV-23711](https://jira.mariadb.org/browse/MDEV-23711) fixup: GCC -Og -Wmaybe-uninitialized
* [Revision #a9d8f5c1a5](https://github.com/MariaDB/server/commit/a9d8f5c1a5)\
  2020-09-21 16:14:35 +0300
  * [MDEV-23776](https://jira.mariadb.org/browse/MDEV-23776): Split encryption.create\_or\_replace
* [Revision #e33f7b6faa](https://github.com/MariaDB/server/commit/e33f7b6faa)\
  2020-09-21 15:55:27 +0300
  * [MDEV-23776](https://jira.mariadb.org/browse/MDEV-23776) Test encryption.create\_or\_replace fails with a warning
* [Revision #a3bdce8f1e](https://github.com/MariaDB/server/commit/a3bdce8f1e)\
  2020-09-21 14:01:56 +0300
  * [MDEV-23659](https://jira.mariadb.org/browse/MDEV-23659) : Update Galera disabled.def file
* [Revision #a0e2a293bc](https://github.com/MariaDB/server/commit/a0e2a293bc)\
  2020-09-21 13:59:13 +0300
  * Fix try.
* [Revision #6c4c88dbb8](https://github.com/MariaDB/server/commit/6c4c88dbb8)\
  2020-09-21 12:52:44 +0300
  * [MDEV-18867](https://jira.mariadb.org/browse/MDEV-18867): Remove an orphan function
* [Revision #0a224edc3e](https://github.com/MariaDB/server/commit/0a224edc3e)\
  2020-09-19 00:08:38 +0300
  * [MDEV-23711](https://jira.mariadb.org/browse/MDEV-23711) make mariadb-backup innodb redo log read error message more clear
* [Revision #69d536a22d](https://github.com/MariaDB/server/commit/69d536a22d)\
  2020-09-18 07:32:36 +0300
  * [MDEV-23751](https://jira.mariadb.org/browse/MDEV-23751) : galera\_3nodes test failures on ipv6 sst tests
* [Revision #f381e019b6](https://github.com/MariaDB/server/commit/f381e019b6)\
  2020-09-17 12:55:06 +0300
  * [MDEV-23574](https://jira.mariadb.org/browse/MDEV-23574) : galera\_3nodes.galera\_ipv6\_mariadb-backup\_section MTR failed: Could not open '../galera/include/have\_mariadb-backup.inc'
* [Revision #e3e657373a](https://github.com/MariaDB/server/commit/e3e657373a)\
  2020-09-17 08:25:07 +0300
  * [MDEV-21769](https://jira.mariadb.org/browse/MDEV-21769) : `galera_3nodes.galera_safe_to_bootstrap` fails
* [Revision #96426dac91](https://github.com/MariaDB/server/commit/96426dac91)\
  2020-09-16 15:23:41 +0300
  * [MDEV-21655](https://jira.mariadb.org/browse/MDEV-21655) : galera.galera\_wan\_restart\_ist MTR fails sporadically: WSREP did not transition to state READY
* [Revision #80075ba011](https://github.com/MariaDB/server/commit/80075ba011)\
  2020-09-07 19:43:23 +0300
  * [MDEV-19264](https://jira.mariadb.org/browse/MDEV-19264) Better support MariaDB GTID for mariadb-backup's --slave-info option
* [Revision #ae8ff3a067](https://github.com/MariaDB/server/commit/ae8ff3a067)\
  2020-09-09 11:41:06 +1000
  * [MDEV-20396](https://jira.mariadb.org/browse/MDEV-20396) Server crashes after DELETE with SEL NULL Foreign key and a virtual column in index
* [Revision #bc2dbdb601](https://github.com/MariaDB/server/commit/bc2dbdb601)\
  2020-09-11 12:21:00 +0300
  * [MDEV-23587](https://jira.mariadb.org/browse/MDEV-23587) : galera\_3nodes.galera\_var\_dirty\_reads2 MTR failed: 1047: WSREP has not yet prepared node for application use
* [Revision #bfd1ed5a13](https://github.com/MariaDB/server/commit/bfd1ed5a13)\
  2020-09-11 12:24:29 +0530
  * [MDEV-18867](https://jira.mariadb.org/browse/MDEV-18867) Long Time to Stop and Start
* [Revision #224c950462](https://github.com/MariaDB/server/commit/224c950462)\
  2020-08-26 14:11:17 +0300
  * [MDEV-23101](https://jira.mariadb.org/browse/MDEV-23101) : SIGSEGV in lock\_rec\_unlock() when Galera is enabled
* [Revision #75e82f71f1](https://github.com/MariaDB/server/commit/75e82f71f1)\
  2020-09-09 17:14:48 +0530
  * [MDEV-18867](https://jira.mariadb.org/browse/MDEV-18867) Long Time to Stop and Start
* [Revision #5c07ce406b](https://github.com/MariaDB/server/commit/5c07ce406b)\
  2020-09-09 16:03:15 +0300
  * [MDEV-23706](https://jira.mariadb.org/browse/MDEV-23706) : Galera test failure on galera\_autoinc\_sst\_mariadb-backup
* [Revision #0eb38243ce](https://github.com/MariaDB/server/commit/0eb38243ce)\
  2020-09-09 13:04:11 +0300
  * [MDEV-23456](https://jira.mariadb.org/browse/MDEV-23456) fixup: Simplify a comparison
* [Revision #040ae4c59b](https://github.com/MariaDB/server/commit/040ae4c59b)\
  2020-09-09 13:02:25 +0300
  * [MDEV-22924](https://jira.mariadb.org/browse/MDEV-22924) fixup: Replace C++11 auto
* [Revision #d44c0f46c5](https://github.com/MariaDB/server/commit/d44c0f46c5)\
  2020-09-09 12:26:51 +0300
  * [MDEV-22924](https://jira.mariadb.org/browse/MDEV-22924) fixup: Replace C++11 nullptr
* [Revision #64c8fa58a8](https://github.com/MariaDB/server/commit/64c8fa58a8)\
  2020-09-09 12:04:42 +0300
  * [MDEV-23685](https://jira.mariadb.org/browse/MDEV-23685) SIGSEGV on ADD FOREIGN KEY after failed ADD KEY
* [Revision #c26eae0cc0](https://github.com/MariaDB/server/commit/c26eae0cc0)\
  2020-09-09 12:01:03 +0300
  * [MDEV-23456](https://jira.mariadb.org/browse/MDEV-23456) fixup: Fix mtr\_t::get\_fix\_count()
* [Revision #b1009ae5c1](https://github.com/MariaDB/server/commit/b1009ae5c1)\
  2020-09-09 11:58:15 +0530
  * [MDEV-23456](https://jira.mariadb.org/browse/MDEV-23456) fil\_space\_crypt\_t::write\_page0() is accessing an uninitialized page
* [Revision #f99cace77f](https://github.com/MariaDB/server/commit/f99cace77f)\
  2020-09-07 15:31:54 +0300
  * [MDEV-22924](https://jira.mariadb.org/browse/MDEV-22924) Corruption in MVCC read via secondary index
* [Revision #9dedba16ab](https://github.com/MariaDB/server/commit/9dedba16ab)\
  2020-09-04 22:10:57 +0900
  * [MDEV-7098](https://jira.mariadb.org/browse/MDEV-7098) spider/bg.spider\_fixes failed in buildbot with safe\_mutex: Trying to unlock mutex conn->mta\_conn\_mutex that wasn't locked at storage/spider/spd\_db\_conn.cc, line 671
* [Revision #c029d45623](https://github.com/MariaDB/server/commit/c029d45623)\
  2020-09-04 12:07:46 +0300
  * [MDEV-23600](https://jira.mariadb.org/browse/MDEV-23600) follow-up: uninitialized rec\_field\_is\_prefix
* [Revision #8c2909a2a4](https://github.com/MariaDB/server/commit/8c2909a2a4)\
  2020-09-04 09:12:27 +0000
  * Fix a typo in the previous cset
* [Revision #d63fcbc2f0](https://github.com/MariaDB/server/commit/d63fcbc2f0)\
  2020-09-03 15:26:55 +0000
  * [MDEV-23661](https://jira.mariadb.org/browse/MDEV-23661): RocksDB produces "missing initializer for member" warnings
* Merge [Revision #2a93e632b1](https://github.com/MariaDB/server/commit/2a93e632b1) 2020-09-03 09:10:03 +0300 - Merge 10.1 into 10.2
* [Revision #9aea50616c](https://github.com/MariaDB/server/commit/9aea50616c)\
  2020-09-02 14:57:48 +0300
  * Increase mariadb-backup SST initial timeout to avoid timeouts.
* [Revision #837bbbafc5](https://github.com/MariaDB/server/commit/837bbbafc5)\
  2020-09-02 16:15:02 +0530
  * [MDEV-23470](https://jira.mariadb.org/browse/MDEV-23470) InnoDB: Failing assertion: cmp < 0 in row\_ins\_check\_foreign\_constraint
* [Revision #054f96ecff](https://github.com/MariaDB/server/commit/054f96ecff)\
  2020-09-02 12:54:14 +1000
  * innodb: osx build failure fix
* Merge [Revision #4d51ca6386](https://github.com/MariaDB/server/commit/4d51ca6386) 2020-09-01 16:20:23 +0300 - Merge 10.1 into 10.2
* [Revision #ebafe5a236](https://github.com/MariaDB/server/commit/ebafe5a236)\
  2020-08-31 17:20:03 +0300
  * Cleanup: Avoid repeated calls to dict\_col\_t::is\_virtual()
* [Revision #4a165f3711](https://github.com/MariaDB/server/commit/4a165f3711)\
  2020-08-31 16:48:28 +0300
  * Fix GCC 10.2.0 -Og -Wmaybe-uninitialized
* [Revision #97db6c15ea](https://github.com/MariaDB/server/commit/97db6c15ea)\
  2020-08-11 00:38:32 +1000
  * [MDEV-20618](https://jira.mariadb.org/browse/MDEV-20618) Assertion failed in row\_upd\_sec\_index\_entry
* [Revision #a3d66090c7](https://github.com/MariaDB/server/commit/a3d66090c7)\
  2020-08-21 20:05:02 +1000
  * [MDEV-18366](https://jira.mariadb.org/browse/MDEV-18366) Crash on SELECT on a table with indexed virtual columns
* [Revision #6112a0f93d](https://github.com/MariaDB/server/commit/6112a0f93d)\
  2020-08-11 21:45:09 +0300
  * [MDEV-16372](https://jira.mariadb.org/browse/MDEV-16372) ER\_BASE64\_DECODE\_ERROR upon replaying binary log via mysqlbinlog --verbose
* [Revision #9bb17ecf43](https://github.com/MariaDB/server/commit/9bb17ecf43)\
  2020-08-31 13:01:57 +0300
  * fix clang build
* [Revision #c710c450e3](https://github.com/MariaDB/server/commit/c710c450e3)\
  2020-08-28 16:40:12 +0300
  * [MDEV-21578](https://jira.mariadb.org/browse/MDEV-21578) : CREATE OR REPLACE TRIGGER in Galera cluster not replicating
* [Revision #df07ea0b27](https://github.com/MariaDB/server/commit/df07ea0b27)\
  2020-08-27 10:52:39 +0300
  * [MDEV-23557](https://jira.mariadb.org/browse/MDEV-23557) Galera heap-buffer-overflow in wsrep\_rec\_get\_foreign\_key
* [Revision #5843dc485b](https://github.com/MariaDB/server/commit/5843dc485b)\
  2020-08-27 15:00:49 +0300
  * Update galera and galera\_3nodes disabled.def file after fixes.
* [Revision #c08afc4363](https://github.com/MariaDB/server/commit/c08afc4363)\
  2020-08-27 15:00:25 +0300
  * Update galera\_3nodes suite global ignore list.
* [Revision #a34f93010c](https://github.com/MariaDB/server/commit/a34f93010c)\
  2020-08-27 14:58:55 +0300
  * [MDEV-23587](https://jira.mariadb.org/browse/MDEV-23587) : galera\_3nodes.galera\_var\_dirty\_reads2 MTR failed: 1047: WSREP has not yet prepared node for application use
* [Revision #fcea7918de](https://github.com/MariaDB/server/commit/fcea7918de)\
  2020-08-27 14:56:13 +0300
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580) : galera\_3nodes.galera\_ipv6\_rsync\_section MTR failed: WSREP\_SST: \[ERROR] rsync daemon port '16008' has been taken
* [Revision #2845ed682c](https://github.com/MariaDB/server/commit/2845ed682c)\
  2020-08-27 14:52:12 +0300
  * [MDEV-23581](https://jira.mariadb.org/browse/MDEV-23581) : galera\_3nodes.galera\_ipv6\_rsync MTR failed: WSREP\_SST: \[ERROR] rsync daemon port '16008' has been taken
* [Revision #3135de4266](https://github.com/MariaDB/server/commit/3135de4266)\
  2020-08-27 14:51:06 +0300
  * [MDEV-23576](https://jira.mariadb.org/browse/MDEV-23576) : galera\_3nodes.galera\_ipv6\_mysqldump MTR failed: WSREP\_SST: \[ERROR] rsync daemon port '16008' has been taken
* [Revision #97d830565f](https://github.com/MariaDB/server/commit/97d830565f)\
  2020-08-27 14:50:21 +0300
  * [MDEV-23574](https://jira.mariadb.org/browse/MDEV-23574) : galera\_3nodes.galera\_ipv6\_mariadb-backup\_section MTR failed: Could not open '../galera/include/have\_mariadb-backup.inc'
* [Revision #f54295f546](https://github.com/MariaDB/server/commit/f54295f546)\
  2020-08-27 14:49:17 +0300
  * [MDEV-23573](https://jira.mariadb.org/browse/MDEV-23573) : galera\_3nodes.galera\_ipv6\_mariadb-backup MTR failed: Could not open '../galera/include/have\_mariadb-backup.inc
* [Revision #b3e43eeec7](https://github.com/MariaDB/server/commit/b3e43eeec7)\
  2020-08-27 13:52:15 +0300
  * Remove xtrabackup and innobackupex test cases.
* [Revision #21a96581fd](https://github.com/MariaDB/server/commit/21a96581fd)\
  2020-08-26 04:16:55 +0300
  * [MDEV-23583](https://jira.mariadb.org/browse/MDEV-23583) Fix up community suite/galera\_3nodes/disabled.def
* [Revision #8cf8ad86d4](https://github.com/MariaDB/server/commit/8cf8ad86d4)\
  2020-08-25 15:32:15 +0300
  * [MDEV-23547](https://jira.mariadb.org/browse/MDEV-23547) InnoDB: Failing assertion: \*len in row\_upd\_ext\_fetch
* [Revision #c0e5cf79ad](https://github.com/MariaDB/server/commit/c0e5cf79ad)\
  2020-08-25 15:23:20 +0300
  * [MDEV-22543](https://jira.mariadb.org/browse/MDEV-22543): Remove orphan declaration of wsrep\_is\_sst\_progress
* [Revision #0be70a1b77](https://github.com/MariaDB/server/commit/0be70a1b77)\
  2020-08-17 08:57:13 +0300
  * [MDEV-23483](https://jira.mariadb.org/browse/MDEV-23483): Set Galera SST thd as system thread
* [Revision #6fa40b85be](https://github.com/MariaDB/server/commit/6fa40b85be)\
  2020-08-25 10:15:04 +0300
  * [MDEV-23554](https://jira.mariadb.org/browse/MDEV-23554) Wrong default value for foreign\_key\_checks variable
* [Revision #4a90bb85c0](https://github.com/MariaDB/server/commit/4a90bb85c0)\
  2020-08-24 20:53:51 +0300
  * InnoDB: fix debug assertion
* [Revision #f3160ee44f](https://github.com/MariaDB/server/commit/f3160ee44f)\
  2020-08-21 18:22:55 +0300
  * [MDEV-22782](https://jira.mariadb.org/browse/MDEV-22782) AddressSanitizer race condition in trx\_free()
* [Revision #a19cb3884f](https://github.com/MariaDB/server/commit/a19cb3884f)\
  2020-08-20 15:32:35 +0300
  * [MDEV-23511](https://jira.mariadb.org/browse/MDEV-23511) shutdown\_server 10 times out, causing server kill at shutdown
* Merge [Revision #a43faf6b16](https://github.com/MariaDB/server/commit/a43faf6b16) 2020-08-21 10:16:49 +0300 - Merge 10.1 into 10.2
* [Revision #a79c257894](https://github.com/MariaDB/server/commit/a79c257894)\
  2020-08-20 11:38:10 +0530
  * [MDEV-23452](https://jira.mariadb.org/browse/MDEV-23452) Assertion \`buf\_page\_get\_io\_fix(bpage) == BUF\_IO\_NONE' failed in buf\_page\_set\_sticky
* [Revision #e9d6f1c7ac](https://github.com/MariaDB/server/commit/e9d6f1c7ac)\
  2020-08-18 13:41:03 +0530
  * [MDEV-23452](https://jira.mariadb.org/browse/MDEV-23452) Assertion \`buf\_page\_get\_io\_fix(bpage) == BUF\_IO\_NONE' failed in buf\_page\_set\_sticky
* [Revision #22c4a7512f](https://github.com/MariaDB/server/commit/22c4a7512f)\
  2020-08-20 08:34:55 +0300
  * [MDEV-23514](https://jira.mariadb.org/browse/MDEV-23514) Race conditions between ROLLBACK and ALTER TABLE
* Merge [Revision #bfba2bce6a](https://github.com/MariaDB/server/commit/bfba2bce6a) 2020-08-20 06:00:36 +0300 - Merge 10.1 into 10.2
* [Revision #309302a3da](https://github.com/MariaDB/server/commit/309302a3da)\
  2020-08-19 11:18:56 +0300
  * [MDEV-23475](https://jira.mariadb.org/browse/MDEV-23475) InnoDB performance regression for write-heavy workloads
* [Revision #1509363970](https://github.com/MariaDB/server/commit/1509363970)\
  2020-08-18 17:30:34 +0300
  * [MDEV-23484](https://jira.mariadb.org/browse/MDEV-23484) Rollback unnecessarily acquires dict\_operation\_lock for every row
* [Revision #4c50120d14](https://github.com/MariaDB/server/commit/4c50120d14)\
  2020-08-14 14:52:14 +0300
  * [MDEV-23474](https://jira.mariadb.org/browse/MDEV-23474) InnoDB fails to restart after SET GLOBAL innodb\_log\_checksums=OFF
* [Revision #8268f26605](https://github.com/MariaDB/server/commit/8268f26605)\
  2020-08-07 19:02:48 +0530
  * [MDEV-22934](https://jira.mariadb.org/browse/MDEV-22934) Table disappear after two alter table command
* [Revision #362b18c536](https://github.com/MariaDB/server/commit/362b18c536)\
  2020-08-03 16:51:41 +0530
  * [MDEV-23380](https://jira.mariadb.org/browse/MDEV-23380) InnoDB reads a page from disk despite parsing MLOG\_INIT\_FILE\_PAGE2 record
* Merge [Revision #3e617b8bef](https://github.com/MariaDB/server/commit/3e617b8bef) 2020-08-13 17:50:40 +0300 - Merge 10.1 into 10.2
* Merge [Revision #182e2d4a6c](https://github.com/MariaDB/server/commit/182e2d4a6c) 2020-08-13 07:38:35 +0300 - Merge 10.1 into 10.2
* [Revision #18f374cb20](https://github.com/MariaDB/server/commit/18f374cb20)\
  2020-08-12 13:12:51 +0300
  * [MDEV-23439](https://jira.mariadb.org/browse/MDEV-23439) Assertion size == space->size failed in buf\_read\_ahead\_random
* [Revision #4387e3a13b](https://github.com/MariaDB/server/commit/4387e3a13b)\
  2020-08-12 13:08:17 +0300
  * Use DBUG\_ASSERT(ptr != NULL) to ease merging to 10.3
* [Revision #5a4ae142f4](https://github.com/MariaDB/server/commit/5a4ae142f4)\
  2020-08-12 10:24:09 +0300
  * replace assert() with DBUG\_ASSERT()
* [Revision #01738d08f3](https://github.com/MariaDB/server/commit/01738d08f3)\
  2020-08-11 20:12:30 +0300
  * add debug assertion to ilist
* [Revision #c96be848d3](https://github.com/MariaDB/server/commit/c96be848d3)\
  2020-08-11 18:52:38 +0300
  * [MDEV-14119](https://jira.mariadb.org/browse/MDEV-14119) Assertion cmp\_rec\_rec() in ALTER TABLE
* [Revision #de8d57e522](https://github.com/MariaDB/server/commit/de8d57e522)\
  2020-08-11 15:49:37 +0300
  * [MDEV-23447](https://jira.mariadb.org/browse/MDEV-23447) SIGSEGV in fil\_system\_t::keyrotate\_next()
* [Revision #31aef3ae99](https://github.com/MariaDB/server/commit/31aef3ae99)\
  2020-08-11 15:48:58 +0300
  * Fix GCC 10.2.0 -Og -Wmaybe-uninitialized
* [Revision #57d1a5fa8e](https://github.com/MariaDB/server/commit/57d1a5fa8e)\
  2020-08-10 11:44:42 +0300
  * [MDEV-22543](https://jira.mariadb.org/browse/MDEV-22543) : Galera SST donation fails, FLUSH TABLES WITH READ LOCK times out
* [Revision #78ea8ad425](https://github.com/MariaDB/server/commit/78ea8ad425)\
  2020-08-10 18:03:05 +0000
  * [MDEV-23378](https://jira.mariadb.org/browse/MDEV-23378) - fix an alleged memory "leak" in threadpool.
* Merge [Revision #3b6dadb5eb](https://github.com/MariaDB/server/commit/3b6dadb5eb) 2020-08-10 17:57:14 +0300 - Merge 10.1 into 10.2
* Merge [Revision #0460d42b94](https://github.com/MariaDB/server/commit/0460d42b94) 2020-08-10 17:31:49 +0300 - Merge mariadb-10.2.33
* [Revision #debd36c880](https://github.com/MariaDB/server/commit/debd36c880)\
  2020-08-10 10:23:10 -0400
  * bump the VERSION
* [Revision #845e3c9801](https://github.com/MariaDB/server/commit/845e3c9801)\
  2020-08-07 10:22:38 +0300
  * Replaced infinite loop in procedure with limited loop to avoid hang.
* [Revision #1dec60c795](https://github.com/MariaDB/server/commit/1dec60c795)\
  2020-08-07 09:06:13 +0300
  * [MDEV-22626](https://jira.mariadb.org/browse/MDEV-22626): mysql\_tzinfo\_to\_sql not replicates timezone to galeranodes if only 1 timezone will be loaded.
* [Revision #caa474f8e3](https://github.com/MariaDB/server/commit/caa474f8e3)\
  2020-08-06 17:50:20 +0530
  * [MDEV-15180](https://jira.mariadb.org/browse/MDEV-15180): server crashed with NTH\_VALUE()
* [Revision #1e31d74833](https://github.com/MariaDB/server/commit/1e31d74833)\
  2020-07-23 14:17:05 +0530
  * [MDEV-17066](https://jira.mariadb.org/browse/MDEV-17066): Bytes lost or Assertion \`status\_var.local\_memory\_used == 0 after DELETE with subquery with ROLLUP
* [Revision #91caf130b7](https://github.com/MariaDB/server/commit/91caf130b7)\
  2020-08-04 09:56:09 +0300
  * [MDEV-23101](https://jira.mariadb.org/browse/MDEV-23101) fixup: Remove redundant code
* [Revision #5fb07d22f1](https://github.com/MariaDB/server/commit/5fb07d22f1)\
  2020-07-27 19:07:08 +0530
  * [MDEV-23082](https://jira.mariadb.org/browse/MDEV-23082): ER\_TABLEACCESS\_DENIED\_ERROR error message is truncated, and inaccurately
* [Revision #745fa255ba](https://github.com/MariaDB/server/commit/745fa255ba)\
  2020-07-16 22:15:55 +0530
  * [MDEV-14836](https://jira.mariadb.org/browse/MDEV-14836): Assertion \`m\_status == DA\_ERROR' failed in Diagnostics\_area::sql\_errno upon query from I\_S with LIMIT ROWS EXAMINED
* [Revision #87b1625b5c](https://github.com/MariaDB/server/commit/87b1625b5c)\
  2020-08-04 07:53:13 +0300
  * Test case MW-328A still fails, thus disable it until it is really fixed.
* [Revision #a8ec45863b](https://github.com/MariaDB/server/commit/a8ec45863b)\
  2020-08-03 15:15:40 +0300
  * [MDEV-23101](https://jira.mariadb.org/browse/MDEV-23101): SIGSEGV in lock\_rec\_unlock() when Galera is enabled

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
