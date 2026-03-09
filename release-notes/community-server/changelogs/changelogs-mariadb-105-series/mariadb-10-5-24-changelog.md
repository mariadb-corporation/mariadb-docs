# MariaDB 10.5.24 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.24](https://downloads.mariadb.org/mariadb/10.5.24/)[Release Notes](../../old-releases/10.5/10.5.24.md)[Changelog](mariadb-10-5-24-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 7 Feb 2024

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.24.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.33](../changelogs-mariadb-10-4-series/mariadb-10-4-33-changelog.md)
* Merge [Revision #01f6abd1d4](https://github.com/MariaDB/server/commit/01f6abd1d4) 2024-01-31 17:32:53 +0100 - Merge branch '10.4' into 10.5
* [Revision #97fcafb9ec](https://github.com/MariaDB/server/commit/97fcafb9ec)\
  2024-01-10 15:35:25 +0400
  * [MDEV-32837](https://jira.mariadb.org/browse/MDEV-32837) long unique does not work like unique key when using replace
* [Revision #a7ee3bc58b](https://github.com/MariaDB/server/commit/a7ee3bc58b)\
  2024-01-22 18:02:11 +0100
  * [MDEV-29954](https://jira.mariadb.org/browse/MDEV-29954) Unique hash key on column prefix is computed incorrectly
* [Revision #14d00fdb15](https://github.com/MariaDB/server/commit/14d00fdb15)\
  2024-01-22 18:17:05 +0100
  * cleanup: MY\_STRNNCOLLSP\_NCHARS\_EMULATE\_TRIMMED\_TRAILING\_SPACES
* [Revision #8bb464899f](https://github.com/MariaDB/server/commit/8bb464899f)\
  2024-01-22 18:01:37 +0100
  * cleanup: unused and undefined methods
* [Revision #dcb814c44e](https://github.com/MariaDB/server/commit/dcb814c44e)\
  2024-01-21 23:28:54 +0100
  * [MDEV-11628](https://jira.mariadb.org/browse/MDEV-11628) mysql.slow\_log reports incorrect start time
* [Revision #db9fad1562](https://github.com/MariaDB/server/commit/db9fad1562)\
  2024-01-21 23:20:07 +0100
  * cleanup: main.log\_tables test
* [Revision #2bc940f7c9](https://github.com/MariaDB/server/commit/2bc940f7c9)\
  2024-01-20 11:01:46 +0100
  * disable perfschema in mtr bootstrap
* [Revision #81d01855fe](https://github.com/MariaDB/server/commit/81d01855fe)\
  2024-01-23 13:22:58 +0400
  * [MDEV-28651](https://jira.mariadb.org/browse/MDEV-28651) quote(NULL) returns incorrect result in view ('NU' instead of 'NULL')
* [Revision #5ce6a352b6](https://github.com/MariaDB/server/commit/5ce6a352b6)\
  2024-01-22 14:23:44 +1100
  * [MDEV-33290](https://jira.mariadb.org/browse/MDEV-33290): Disable ColumnStore based on boost version
* [Revision #13e49b783f](https://github.com/MariaDB/server/commit/13e49b783f)\
  2024-01-19 18:40:53 +0700
  * sql\_test.cc compile fix
* [Revision #117388225c](https://github.com/MariaDB/server/commit/117388225c)\
  2024-01-12 09:32:34 +1200
  * [MDEV-33165](https://jira.mariadb.org/browse/MDEV-33165) Incorrect result interceptor passed to mysql\_explain\_union()
* [Revision #207c85783b](https://github.com/MariaDB/server/commit/207c85783b)\
  2024-01-19 10:31:45 -0700
  * [MDEV-33283](https://jira.mariadb.org/browse/MDEV-33283): Binlog Checksum is Zeroed by Zlib if Part of Event Data is Empty
* [Revision #7573fe8b07](https://github.com/MariaDB/server/commit/7573fe8b07)\
  2024-01-19 15:00:13 +0530
  * [MDEV-32968](https://jira.mariadb.org/browse/MDEV-32968) InnoDB fails to restore tablespace first page from doublewrite buffer when page is empty
* [Revision #c95ba183d2](https://github.com/MariaDB/server/commit/c95ba183d2)\
  2023-12-21 20:08:32 +0000
  * Replace incorrect message `mariadb-safe` with correct `mariadbd-safe`
* [Revision #fa3171df08](https://github.com/MariaDB/server/commit/fa3171df08)\
  2023-12-27 18:57:49 +0400
  * [MDEV-27666](https://jira.mariadb.org/browse/MDEV-27666) User variable not parsed as geometry variable in geometry function
* [Revision #caad34df54](https://github.com/MariaDB/server/commit/caad34df54)\
  2024-01-15 14:08:27 +0530
  * [MDEV-32968](https://jira.mariadb.org/browse/MDEV-32968) InnoDB fails to restore tablespace first page from doublewrite buffer when page is empty
* [Revision #ee30491e50](https://github.com/MariaDB/server/commit/ee30491e50)\
  2023-11-15 11:09:26 +0200
  * [MDEV-32111](https://jira.mariadb.org/browse/MDEV-32111): Debian Sid/Trixie will not have libncurses 5 anymore
* [Revision #48e4962c44](https://github.com/MariaDB/server/commit/48e4962c44)\
  2023-07-06 11:55:40 +0700
  * [MDEV-29298](https://jira.mariadb.org/browse/MDEV-29298) INSERT ... SELECT Does not produce an optimizer trace
* [Revision #5b0a4159ef](https://github.com/MariaDB/server/commit/5b0a4159ef)\
  2024-01-05 13:44:49 +0100
  * Fix test failures on s390x in test following main.column\_compression\_rpl
* [Revision #8a763c014e](https://github.com/MariaDB/server/commit/8a763c014e)\
  2024-01-12 15:39:38 +0100
  * [MDEV-32235](https://jira.mariadb.org/browse/MDEV-32235): mysql\_json cannot be used on newly created table
* [Revision #8b5c1d5afa](https://github.com/MariaDB/server/commit/8b5c1d5afa)\
  2024-01-12 15:20:25 +0100
  * Revert "[MDEV-32235](https://jira.mariadb.org/browse/MDEV-32235): mysql\_json cannot be used on newly created table"
* [Revision #22f3ebe4bf](https://github.com/MariaDB/server/commit/22f3ebe4bf)\
  2024-01-11 15:15:46 +0100
  * [MDEV-32235](https://jira.mariadb.org/browse/MDEV-32235): mysql\_json cannot be used on newly created table
* [Revision #9a5f85dcbe](https://github.com/MariaDB/server/commit/9a5f85dcbe)\
  2023-11-13 15:40:13 +0100
  * [MDEV-32790](https://jira.mariadb.org/browse/MDEV-32790): Output result in show create table for mysql\_json type should be longtext
* [Revision #9e9e0b99ad](https://github.com/MariaDB/server/commit/9e9e0b99ad)\
  2023-12-19 12:18:13 +1100
  * [MDEV-30170](https://jira.mariadb.org/browse/MDEV-30170) ha\_spider::delete\_table() should report table not exist
* [Revision #7801c6d22d](https://github.com/MariaDB/server/commit/7801c6d22d)\
  2023-12-15 17:37:28 +1100
  * [MDEV-29002](https://jira.mariadb.org/browse/MDEV-29002) Spider: remove SPIDER\_CONN::loop\_check\_meraged\_last
* [Revision #761d5c8987](https://github.com/MariaDB/server/commit/761d5c8987)\
  2024-01-10 00:56:19 +0100
  * [MDEV-33092](https://jira.mariadb.org/browse/MDEV-33092) Undefined reference to concurrency on Solaris
* [Revision #c4ebf87f86](https://github.com/MariaDB/server/commit/c4ebf87f86)\
  2023-12-13 21:02:44 +0100
  * [MDEV-32984](https://jira.mariadb.org/browse/MDEV-32984) Update federated table and column privileges
* Merge [Revision #c9902a20b3](https://github.com/MariaDB/server/commit/c9902a20b3) 2024-01-10 18:01:46 +1100 - Merge branch '10.4' into 10.5
* [Revision #0b612619ef](https://github.com/MariaDB/server/commit/0b612619ef)\
  2024-01-08 14:36:54 +0200
  * [MDEV-33098](https://jira.mariadb.org/browse/MDEV-33098): Fix some instrumentation for innodb.doublewrite\_debug
* [Revision #cc5c0eda4c](https://github.com/MariaDB/server/commit/cc5c0eda4c)\
  2024-01-03 12:08:21 +0200
  * [MDEV-33156](https://jira.mariadb.org/browse/MDEV-33156) Crash on innodb\_buf\_flush\_list\_now=ON and innodb\_force\_recovery=6
* Merge [Revision #3a3a4f044f](https://github.com/MariaDB/server/commit/3a3a4f044f) 2024-01-03 12:07:51 +0200 - Merge 10.4 into 10.5
* [Revision #77b8bedf34](https://github.com/MariaDB/server/commit/77b8bedf34)\
  2024-01-03 15:08:22 +0530
  * [MDEV-33098](https://jira.mariadb.org/browse/MDEV-33098) The test innodb.doublewrite\_debug occasionally fails to start up InnoDB
* [Revision #362c0950e8](https://github.com/MariaDB/server/commit/362c0950e8)\
  2023-10-23 11:49:47 +0200
  * [MDEV-32549](https://jira.mariadb.org/browse/MDEV-32549) Cluster inconsistent after SAVEPOINT is rolled back
* [Revision #c89f769f24](https://github.com/MariaDB/server/commit/c89f769f24)\
  2023-11-21 15:43:11 +0200
  * [MDEV-31905](https://jira.mariadb.org/browse/MDEV-31905) GTID inconsistency
* [Revision #569381df83](https://github.com/MariaDB/server/commit/569381df83)\
  2023-12-21 19:20:18 +0100
  * [MDEV-33046](https://jira.mariadb.org/browse/MDEV-33046) fixup. Do not try to schedule timer without dict\_stats\_start()
* [Revision #7cc332b724](https://github.com/MariaDB/server/commit/7cc332b724)\
  2023-12-21 01:55:25 +0100
  * [MDEV-33046](https://jira.mariadb.org/browse/MDEV-33046) - delete unnecessary synchronization with dict\_stats\_mutex
* Merge [Revision #a3dd7ea09f](https://github.com/MariaDB/server/commit/a3dd7ea09f) 2023-12-21 11:30:32 +0200 - Merge 10.4 into 10.5
* [Revision #cfaab614ea](https://github.com/MariaDB/server/commit/cfaab614ea)\
  2023-12-19 10:03:54 +0200
  * [MDEV-24481](https://jira.mariadb.org/browse/MDEV-24481) : galera\_3nodes.galera\_vote\_rejoin\_mysqldump MTR failed: mysql\_shutdown failed
* [Revision #2b8c59fffa](https://github.com/MariaDB/server/commit/2b8c59fffa)\
  2023-12-20 14:51:00 +0300
  * Fix main.type\_timestamp: Change 10.10 in "End of 10.10 tests" to 10.5
* Merge [Revision #12995559f9](https://github.com/MariaDB/server/commit/12995559f9) 2023-12-19 18:30:58 +0200 - Merge 10.4 into 10.5
* [Revision #476ff0927a](https://github.com/MariaDB/server/commit/476ff0927a)\
  2023-12-19 14:45:39 +0200
  * [MDEV-33062](https://jira.mariadb.org/browse/MDEV-33062) innodb\_undo\_log\_truncate=ON prevents fast shutdown
* [Revision #4c2e971841](https://github.com/MariaDB/server/commit/4c2e971841)\
  2023-12-18 10:37:11 +0200
  * [MDEV-33052](https://jira.mariadb.org/browse/MDEV-33052) MSAN use-of-uninitialized-value in buf\_read\_ahead\_linear()
* Merge [Revision #4ae105a37d](https://github.com/MariaDB/server/commit/4ae105a37d) 2023-12-18 08:59:07 +0200 - Merge 10.4 into 10.5
* [Revision #f98d2ef5b4](https://github.com/MariaDB/server/commit/f98d2ef5b4)\
  2023-12-15 15:38:31 +0200
  * [MDEV-33009](https://jira.mariadb.org/browse/MDEV-33009) Server hangs for a long time with innodb\_undo\_log\_truncate=ON
* [Revision #2c60d43d7d](https://github.com/MariaDB/server/commit/2c60d43d7d)\
  2023-12-13 16:24:34 +1100
  * [MDEV-33006](https://jira.mariadb.org/browse/MDEV-33006) Missing required privilege CONNECTION ADMIN
* [Revision #e472b682e0](https://github.com/MariaDB/server/commit/e472b682e0)\
  2023-11-29 18:56:59 +0100
  * [MDEV-32839](https://jira.mariadb.org/browse/MDEV-32839) LONG UNIQUE gives error when used with REPLACE
* [Revision #81609d8625](https://github.com/MariaDB/server/commit/81609d8625)\
  2023-11-29 17:19:40 +0100
  * cleanup: remove innodb-specific code around update\_auto\_increment()
* [Revision #c5904702cd](https://github.com/MariaDB/server/commit/c5904702cd)\
  2023-11-29 17:19:14 +0100
  * cleanup: remove partition-specific code around update\_auto\_increment()
* [Revision #b94ae3870b](https://github.com/MariaDB/server/commit/b94ae3870b)\
  2023-12-12 11:27:20 +1100
  * \[fixup] galera: Fix an accidental logical inversion in a recent merge
* [Revision #da9ffca908](https://github.com/MariaDB/server/commit/da9ffca908)\
  2023-11-24 07:38:16 +0100
  * [MDEV-29816](https://jira.mariadb.org/browse/MDEV-29816) rpl.rpl\_parallel\_29322 occasionally fails in BB
* [Revision #1e80601b82](https://github.com/MariaDB/server/commit/1e80601b82)\
  2023-12-11 10:37:12 +0200
  * [MDEV-16264](https://jira.mariadb.org/browse/MDEV-16264) fixup: Remove a useless test
* [Revision #03ee23bcbb](https://github.com/MariaDB/server/commit/03ee23bcbb)\
  2023-12-11 10:42:37 +0400
  * [MDEV-17226](https://jira.mariadb.org/browse/MDEV-17226) Column Data in Truncated on UNION to the length of the first value if using REPLACE
* [Revision #2d775fd01a](https://github.com/MariaDB/server/commit/2d775fd01a)\
  2023-11-30 05:32:09 +0400
  * Cleanup: Removing the unused method Type\_handler::get\_handler\_by\_cmp\_type
* [Revision #a356a940d2](https://github.com/MariaDB/server/commit/a356a940d2)\
  2023-12-08 10:55:13 +0200
  * [MDEV-32971](https://jira.mariadb.org/browse/MDEV-32971) Assertion !recv\_sys.is\_corrupt\_fs() failed on recovery
* [Revision #c8346c0bac](https://github.com/MariaDB/server/commit/c8346c0bac)\
  2023-12-08 09:31:34 +0200
  * [MDEV-31939](https://jira.mariadb.org/browse/MDEV-31939) Adaptive flush recommendation ignores dirty ratio and checkpoint age
* Merge [Revision #d7c6d306fb](https://github.com/MariaDB/server/commit/d7c6d306fb) 2023-12-08 18:02:23 +1100 - Merge branch '10.4' into 10.5
* [Revision #d5a6ea36f3](https://github.com/MariaDB/server/commit/d5a6ea36f3)\
  2023-12-07 18:44:28 +0530
  * [MDEV-32242](https://jira.mariadb.org/browse/MDEV-32242) innodb.doublewrite test case always gets skipped
* Merge [Revision #c33ca17c17](https://github.com/MariaDB/server/commit/c33ca17c17) 2023-12-07 17:52:44 +1100 - Merge branch '10.4' into 10.5
* Merge [Revision #13dd787530](https://github.com/MariaDB/server/commit/13dd787530) 2023-12-07 16:38:00 +1100 - Merge branch '10.4' into 10.5
* [Revision #ddd5449c57](https://github.com/MariaDB/server/commit/ddd5449c57)\
  2023-12-05 14:33:16 +1100
  * \[fixup] post-merge spider fixup
* [Revision #b97f4c340e](https://github.com/MariaDB/server/commit/b97f4c340e)\
  2023-12-04 20:34:45 +0300
  * Followup for fix for [MDEV-20169](https://jira.mariadb.org/browse/MDEV-20169): enable main.partition\_innodb
* [Revision #2700d20b7c](https://github.com/MariaDB/server/commit/2700d20b7c)\
  2023-12-04 10:30:39 +0100
  * [MDEV-32725](https://jira.mariadb.org/browse/MDEV-32725) innodb.import\_update\_stats accesses uninitialized ib\_table->stat\_n\_rows
* [Revision #af2e91d9f2](https://github.com/MariaDB/server/commit/af2e91d9f2)\
  2023-11-30 09:59:23 +0100
  * fix for the test (real fixes will be in 10.4)
* Merge [Revision #98a39b0c91](https://github.com/MariaDB/server/commit/98a39b0c91) 2023-12-01 13:43:58 +0100 - Merge branch '10.4' into 10.5
* [Revision #c6a9fd7904](https://github.com/MariaDB/server/commit/c6a9fd7904)\
  2023-11-30 11:47:44 +1200
  * [MDEV-32212](https://jira.mariadb.org/browse/MDEV-32212) DELETE with ORDER BY and semijoin optimization causing crash
* [Revision #89a5a8d234](https://github.com/MariaDB/server/commit/89a5a8d234)\
  2023-11-30 09:43:36 +0200
  * [MDEV-32269](https://jira.mariadb.org/browse/MDEV-32269) InnoDB after ALTER TABLE…IMPORT TABLESPACE may not be crash safe
* [Revision #968061fd9c](https://github.com/MariaDB/server/commit/968061fd9c)\
  2023-11-27 21:03:21 +0300
  * [MDEV-28682](https://jira.mariadb.org/browse/MDEV-28682) gcol.gcol\_purge contaminates further execution of innodb.gap\_locks
* [Revision #387b92df97](https://github.com/MariaDB/server/commit/387b92df97)\
  2023-11-28 15:31:02 +0200
  * Remove deprication from mariadbd --debug
* [Revision #f436b4a523](https://github.com/MariaDB/server/commit/f436b4a523)\
  2023-11-27 09:56:21 +0400
  * [MDEV-32879](https://jira.mariadb.org/browse/MDEV-32879) Server crash in my\_decimal::operator= or unexpected ER\_DUP\_ENTRY upon comparison with INET6 and similar types
* [Revision #dd62a285b8](https://github.com/MariaDB/server/commit/dd62a285b8)\
  2023-11-20 16:22:07 +0100
  * [MDEV-31611](https://jira.mariadb.org/browse/MDEV-31611): mariadb-setpermission - Can't use string as an ARRAY ref while strict refs in use
* [Revision #78c9a12c8f](https://github.com/MariaDB/server/commit/78c9a12c8f)\
  2023-11-22 16:54:41 +0200
  * [MDEV-32861](https://jira.mariadb.org/browse/MDEV-32861) InnoDB hangs when running out of I/O slots
* [Revision #de31ca6a21](https://github.com/MariaDB/server/commit/de31ca6a21)\
  2023-11-21 08:53:02 +0200
  * [MDEV-32820](https://jira.mariadb.org/browse/MDEV-32820) Race condition between trx\_purge\_free\_segment() and trx\_undo\_create()
* [Revision #9b7a1c0e92](https://github.com/MariaDB/server/commit/9b7a1c0e92)\
  2023-11-13 23:38:47 +0100
  * [MDEV-22243](https://jira.mariadb.org/browse/MDEV-22243) type\_test.type\_test\_double fails with 'NUMERIC\_SCALE NULL'
* [Revision #8aa2076426](https://github.com/MariaDB/server/commit/8aa2076426)\
  2023-11-13 18:41:22 +0100
  * Revert "[MDEV-22243](https://jira.mariadb.org/browse/MDEV-22243) type\_test.type\_test\_double fails with 'NUMERIC\_SCALE NULL'"
* [Revision #8bbf6697cf](https://github.com/MariaDB/server/commit/8bbf6697cf)\
  2023-11-02 14:57:37 +0100
  * [MDEV-24784](https://jira.mariadb.org/browse/MDEV-24784) JSON\_ARRAYAGG charset issue
* [Revision #9a545eb67c](https://github.com/MariaDB/server/commit/9a545eb67c)\
  2023-11-16 17:45:37 +0200
  * [MDEV-26055](https://jira.mariadb.org/browse/MDEV-26055): Correct the formula for adaptive flushing
* [Revision #a3d0d5fc33](https://github.com/MariaDB/server/commit/a3d0d5fc33)\
  2023-11-16 17:45:18 +0200
  * [MDEV-26055](https://jira.mariadb.org/browse/MDEV-26055): Improve adaptive flushing
* [Revision #8b509a5d64](https://github.com/MariaDB/server/commit/8b509a5d64)\
  2023-09-25 12:56:30 +1100
  * Merge 10.4 into 10.5
* [Revision #a0f02f7438](https://github.com/MariaDB/server/commit/a0f02f7438)\
  2023-11-15 12:23:35 +0200
  * [MDEV-32757](https://jira.mariadb.org/browse/MDEV-32757) innodb\_undo\_log\_truncate=ON is not crash safe
* [Revision #15bb8acf8f](https://github.com/MariaDB/server/commit/15bb8acf8f)\
  2023-11-15 10:49:39 +0200
  * [MDEV-32689](https://jira.mariadb.org/browse/MDEV-32689): Remove Ubuntu Bionic from 10.5
* [Revision #c638051d80](https://github.com/MariaDB/server/commit/c638051d80)\
  2023-11-14 14:35:51 +0200
  * [MDEV-32798](https://jira.mariadb.org/browse/MDEV-32798) innodb\_fast\_shutdown=0 hang after incomplete startup
* Merge [Revision #9f83a8822f](https://github.com/MariaDB/server/commit/9f83a8822f) 2023-11-14 08:41:23 +0100 - Merge branch '10.5' into mariadb-10.5.23
* [Revision #8b84fb1383](https://github.com/MariaDB/server/commit/8b84fb1383)\
  2023-11-13 13:21:35 -0500
  * bump the VERSION
* [Revision #9da247b2e7](https://github.com/MariaDB/server/commit/9da247b2e7)\
  2023-11-11 15:37:29 +0100
  * galera: cleanup of the lists of disabled tests
* [Revision #c3fdfbdbd8](https://github.com/MariaDB/server/commit/c3fdfbdbd8)\
  2023-11-10 13:54:25 +0100
  * [MDEV-31413](https://jira.mariadb.org/browse/MDEV-31413): post-fix for 10.5+ (galera\_restart\_replica test failures)
* [Revision #e0c65784aa](https://github.com/MariaDB/server/commit/e0c65784aa)\
  2023-11-09 11:06:17 +0200
  * [MDEV-32737](https://jira.mariadb.org/browse/MDEV-32737) innodb.log\_file\_name fails on Assertion \`after\_apply || !(blocks).end in recv\_sys\_t::clear
* [Revision #c68620df48](https://github.com/MariaDB/server/commit/c68620df48)\
  2023-11-04 20:40:31 +0100
  * Fix random test failures in testcase perfschema.mdl\_func
* [Revision #3c1f324a55](https://github.com/MariaDB/server/commit/3c1f324a55)\
  2023-11-03 14:43:45 +0100
  * [MDEV-32672](https://jira.mariadb.org/browse/MDEV-32672): Don't hold LOCK\_thd\_data over commit\_ordered
* [Revision #b06ac9a8cd](https://github.com/MariaDB/server/commit/b06ac9a8cd)\
  2023-10-19 09:21:18 +0200
  * [MDEV-32462](https://jira.mariadb.org/browse/MDEV-32462): mysql\_upgrade -s still checks for non system tables
* [Revision #4eb8aeee8e](https://github.com/MariaDB/server/commit/4eb8aeee8e)\
  2023-10-17 15:41:52 +0200
  * [MDEV-32462](https://jira.mariadb.org/browse/MDEV-32462): mysql\_upgrade -s still checks for non system tables
* [Revision #ee77375377](https://github.com/MariaDB/server/commit/ee77375377)\
  2022-12-07 14:14:24 +0100
  * [MDEV-26875](https://jira.mariadb.org/browse/MDEV-26875): Wrong user in SET DEFAULT ROLE error
* [Revision #9d8f659f80](https://github.com/MariaDB/server/commit/9d8f659f80)\
  2023-11-10 12:40:21 +0100
  * galera: post-fix after migrating changes from 10.4

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
