# MariaDB 10.5.27 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.27](https://downloads.mariadb.org/mariadb/10.5.27/)[Release Notes](../../old-releases/10.5/10.5.27.md)[Changelog](mariadb-10-5-27-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 1 Nov 2024

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.27.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.34](../changelogs-mariadb-10-4-series/mariadb-10-4-34-changelog.md)
* [Revision #6aa47fae30](https://github.com/MariaDB/server/commit/6aa47fae30)\
  2024-10-29 11:39:17 +0100
  * [MDEV-35276](https://jira.mariadb.org/browse/MDEV-35276) Assertion failure in find\_producing\_item upon a query from a view
* [Revision #953f847aed](https://github.com/MariaDB/server/commit/953f847aed)\
  2024-10-28 10:29:27 +0100
  * Post-fix for [MDEV-35236](https://jira.mariadb.org/browse/MDEV-35236)
* [Revision #4b068b7fcb](https://github.com/MariaDB/server/commit/4b068b7fcb)\
  2024-10-28 10:45:50 +0100
  * [MDEV-32387](https://jira.mariadb.org/browse/MDEV-32387) - prevent output during temporary changes to STDOUT/STDERR
* [Revision #284593413f](https://github.com/MariaDB/server/commit/284593413f)\
  2024-10-25 15:33:57 +0300
  * [MDEV-35253](https://jira.mariadb.org/browse/MDEV-35253): xa\_prepare\_unlock\_unmodified fails: shift exponent 32 is too large
* [Revision #b8c2bd9f69](https://github.com/MariaDB/server/commit/b8c2bd9f69)\
  2024-10-25 18:03:40 +1100
  * [MDEV-35249](https://jira.mariadb.org/browse/MDEV-35249) Fix regression caused by [MDEV-34447](https://jira.mariadb.org/browse/MDEV-34447)
* [Revision #decdd4bf49](https://github.com/MariaDB/server/commit/decdd4bf49)\
  2024-10-24 16:08:56 +0300
  * [MDEV-29015](https://jira.mariadb.org/browse/MDEV-29015)/[MDEV-29260](https://jira.mariadb.org/browse/MDEV-29260)/[MDEV-34938](https://jira.mariadb.org/browse/MDEV-34938): os\_file\_get\_size() WSL work-around
* [Revision #3cd706b107](https://github.com/MariaDB/server/commit/3cd706b107)\
  2024-10-23 14:43:32 +0200
  * [MDEV-35236](https://jira.mariadb.org/browse/MDEV-35236) Assertion \`(mem\_root->flags & 4) == 0' failed in safe\_lexcstrdup\_root
* [Revision #eac33a23da](https://github.com/MariaDB/server/commit/eac33a23da)\
  2024-10-22 19:14:35 +0200
  * [MDEV-32022](https://jira.mariadb.org/browse/MDEV-32022) ERROR 1054 (42S22): Unknown column 'X' in 'NEW' in trigger
* [Revision #83db978271](https://github.com/MariaDB/server/commit/83db978271)\
  2024-10-22 15:18:35 +0200
  * new CC 3.1
* [Revision #2339f15a00](https://github.com/MariaDB/server/commit/2339f15a00)\
  2024-10-23 03:47:52 +0200
  * galera: wsrep-lib submodule update
* [Revision #7ffa7b6b01](https://github.com/MariaDB/server/commit/7ffa7b6b01)\
  2024-09-25 09:48:38 +0300
  * [MDEV-31888](https://jira.mariadb.org/browse/MDEV-31888) : galera.galera\_wan, galera.galera\_vote\_rejoin\_\* fail
* [Revision #9b3413c71f](https://github.com/MariaDB/server/commit/9b3413c71f)\
  2024-10-22 09:23:56 +0200
  * [MDEV-8578](https://jira.mariadb.org/browse/MDEV-8578): fix galera test
* [Revision #d29611afa1](https://github.com/MariaDB/server/commit/d29611afa1)\
  2024-10-22 09:12:23 +0200
  * [MDEV-15497](https://jira.mariadb.org/browse/MDEV-15497) fixed outdated syntax
* [Revision #855c21eb99](https://github.com/MariaDB/server/commit/855c21eb99)\
  2024-10-21 13:04:43 +0400
  * Recording ctype\_gbk\_export\_import.result according to [MDEV-34883](https://jira.mariadb.org/browse/MDEV-34883)
* [Revision #7f7d78bc18](https://github.com/MariaDB/server/commit/7f7d78bc18)\
  2024-10-21 10:31:24 +0530
  * [MDEV-35183](https://jira.mariadb.org/browse/MDEV-35183) ADD FULLTEXT INDEX unnecessarily DROPS FTS COMMON TABLES
* [Revision #e14d2b7974](https://github.com/MariaDB/server/commit/e14d2b7974)\
  2024-03-20 00:42:28 +0530
  * [MDEV-8578](https://jira.mariadb.org/browse/MDEV-8578): Wrong error code/message with enforce\_storage\_engine and NO\_ENGINE\_SUBSTITUTION
* [Revision #3da565c41d](https://github.com/MariaDB/server/commit/3da565c41d)\
  2024-10-17 15:57:03 +0200
  * [MDEV-35144](https://jira.mariadb.org/browse/MDEV-35144) CREATE TABLE ... LIKE uses current innodb\_compression\_default instead of the create value
* [Revision #600c42ea86](https://github.com/MariaDB/server/commit/600c42ea86)\
  2024-10-16 13:28:20 +0200
  * [MDEV-34883](https://jira.mariadb.org/browse/MDEV-34883) LOAD DATA INFILE with geometry data fails
* [Revision #c00145de58](https://github.com/MariaDB/server/commit/c00145de58)\
  2024-10-17 08:03:56 +0200
  * fix signed/unsigned and size\_t issue
* [Revision #6b436cba01](https://github.com/MariaDB/server/commit/6b436cba01)\
  2024-10-17 09:11:47 +0200
  * Revert "Fixes buildbot issue with plugin.fulltext\_plugin"
* [Revision #41b036bff0](https://github.com/MariaDB/server/commit/41b036bff0)\
  2024-10-17 03:21:51 +0200
  * This commit adds package dependencies for socat which is needed for testing galera.
* [Revision #4955f6018a](https://github.com/MariaDB/server/commit/4955f6018a)\
  2024-10-09 18:07:57 +0300
  * [MDEV-29351](https://jira.mariadb.org/browse/MDEV-29351) SIGSEGV when doing forward reference of item in select list
* [Revision #7e5ad5dd9e](https://github.com/MariaDB/server/commit/7e5ad5dd9e)\
  2024-10-08 21:48:30 +0300
  * Replace some usage of safe\_strcat() with strxnmov()
* [Revision #0403313bdb](https://github.com/MariaDB/server/commit/0403313bdb)\
  2024-10-16 16:59:41 +0300
  * Fixed connect to not call strlen() over and over again in a loop
* [Revision #864847d1cc](https://github.com/MariaDB/server/commit/864847d1cc)\
  2024-10-08 21:01:30 +0300
  * Fixed safe\_strcpy\_truncated() to get rid of compiler warnings.
* [Revision #8b057fee62](https://github.com/MariaDB/server/commit/8b057fee62)\
  2024-10-08 18:21:24 +0300
  * Fixed core dump in mysqltest in move-file when using wrong paths
* [Revision #0de2613e7a](https://github.com/MariaDB/server/commit/0de2613e7a)\
  2024-10-14 15:12:02 +0300
  * Fixed that SHOW CREATE TABLE for sequences shows used table options
* [Revision #2c52fdd28a](https://github.com/MariaDB/server/commit/2c52fdd28a)\
  2024-10-08 18:20:46 +0300
  * [MDEV-32350](https://jira.mariadb.org/browse/MDEV-32350) Can't selectively restore sequences using innodb tables from backup
* [Revision #ee908140ac](https://github.com/MariaDB/server/commit/ee908140ac)\
  2024-10-03 17:23:50 +0300
  * Fixed bug in main.connect test where Connection\_errors showed wrong value
* [Revision #a8010e7689](https://github.com/MariaDB/server/commit/a8010e7689)\
  2024-10-02 23:30:17 +0300
  * Fixes buildbot issue with plugin.fulltext\_plugin
* [Revision #bddbef3573](https://github.com/MariaDB/server/commit/bddbef3573)\
  2024-10-01 17:07:48 +0300
  * [MDEV-34533](https://jira.mariadb.org/browse/MDEV-34533) asan error about stack overflow when writing record in Aria
* [Revision #c1fc59277a](https://github.com/MariaDB/server/commit/c1fc59277a)\
  2024-10-15 18:54:53 +0200
  * [MDEV-34929](https://jira.mariadb.org/browse/MDEV-34929) page-compressed tables do not work on Windows
* [Revision #5ebda30ccc](https://github.com/MariaDB/server/commit/5ebda30ccc)\
  2024-10-16 13:23:47 +0200
  * Revert "[MDEV-35019](https://jira.mariadb.org/browse/MDEV-35019) Provide a way to enable "rollback XA on disconnect" behavior we had before 10.5.2"
* [Revision #8ae462a220](https://github.com/MariaDB/server/commit/8ae462a220)\
  2024-10-10 20:52:45 +0200
  * [MDEV-35019](https://jira.mariadb.org/browse/MDEV-35019) Provide a way to enable "rollback XA on disconnect" behavior we had before 10.5.2
* [Revision #e927e28ebe](https://github.com/MariaDB/server/commit/e927e28ebe)\
  2024-09-24 09:56:08 +1000
  * Remove HAVE\_BROKEN\_REALPATH
* [Revision #3a4bc9aa35](https://github.com/MariaDB/server/commit/3a4bc9aa35)\
  2024-09-24 09:35:08 +1000
  * [MDEV-34340](https://jira.mariadb.org/browse/MDEV-34340) mariadb-backup immediately dumps core on NetBSD
* [Revision #f9f1d26f2a](https://github.com/MariaDB/server/commit/f9f1d26f2a)\
  2024-09-24 10:12:02 +1000
  * [MDEV-34340](https://jira.mariadb.org/browse/MDEV-34340): MariaDB backup fail on NetBSD
* [Revision #171c4aa479](https://github.com/MariaDB/server/commit/171c4aa479)\
  2024-09-24 08:58:16 +1000
  * [MDEV-34340](https://jira.mariadb.org/browse/MDEV-34340) move get\_exepath to mysys as my\_get\_exepath
* [Revision #e9c71f3a25](https://github.com/MariaDB/server/commit/e9c71f3a25)\
  2024-10-09 17:48:22 -0400
  * [MDEV-34814](https://jira.mariadb.org/browse/MDEV-34814) mysqld hangs on startup when --init-file target does not exist
* [Revision #7038382e1b](https://github.com/MariaDB/server/commit/7038382e1b)\
  2024-10-15 12:42:45 +0200
  * Fix grant5.test with view protocol
* [Revision #44804c667e](https://github.com/MariaDB/server/commit/44804c667e)\
  2024-10-15 11:27:42 +0200
  * [MDEV-18151](https://jira.mariadb.org/browse/MDEV-18151) pam test result fix
* [Revision #d797c9879e](https://github.com/MariaDB/server/commit/d797c9879e)\
  2024-10-15 15:32:11 +1100
  * \[fixup] Restore the Chinese error translation of ER\_SET\_PASSWORD\_AUTH\_PLUGIN
* [Revision #6aaae4c03b](https://github.com/MariaDB/server/commit/6aaae4c03b)\
  2024-10-15 12:04:37 +0530
  * [MDEV-35122](https://jira.mariadb.org/browse/MDEV-35122) Incorrect NULL value handling for instantly dropped BLOB columns
* [Revision #77ed235d50](https://github.com/MariaDB/server/commit/77ed235d50)\
  2024-10-15 15:36:12 +1100
  * [MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345) Spider GBH should execute original queries on the data node
* [Revision #e6daff40e4](https://github.com/MariaDB/server/commit/e6daff40e4)\
  2024-10-10 16:03:14 +1100
  * [MDEV-32524](https://jira.mariadb.org/browse/MDEV-32524) \[fixup] Fixup of spider mem alloc enums missed in a previous merge
* [Revision #6080e3af19](https://github.com/MariaDB/server/commit/6080e3af19)\
  2022-02-10 15:36:44 +0900
  * [MDEV-26912](https://jira.mariadb.org/browse/MDEV-26912) Spider: Remove dead code related to Oracle OCI
* [Revision #03a5c683f9](https://github.com/MariaDB/server/commit/03a5c683f9)\
  2024-10-08 11:46:52 +1100
  * [MDEV-27650](https://jira.mariadb.org/browse/MDEV-27650) Spider: remove #ifdef SPIDER\_HAS\_GROUP\_BY\_HANDLER
* [Revision #0a59aafc5f](https://github.com/MariaDB/server/commit/0a59aafc5f)\
  2024-10-15 14:30:30 +1100
  * [MDEV-34659](https://jira.mariadb.org/browse/MDEV-34659) Bound check in spider cast function query construction
* [Revision #98a9c75ea3](https://github.com/MariaDB/server/commit/98a9c75ea3)\
  2024-07-29 17:03:11 +1000
  * [MDEV-34659](https://jira.mariadb.org/browse/MDEV-34659) Use evalp in CREATE SERVER's in init\_spider.inc
* [Revision #d3b84ff10d](https://github.com/MariaDB/server/commit/d3b84ff10d)\
  2024-10-14 17:19:22 +1100
  * [MDEV-30067](https://jira.mariadb.org/browse/MDEV-30067) Remove some overly enthusiastic asserts when deleting from a partitioned table
* [Revision #8a52639ede](https://github.com/MariaDB/server/commit/8a52639ede)\
  2024-08-07 13:27:44 +1000
  * [MDEV-34716](https://jira.mariadb.org/browse/MDEV-34716) spider: some trivial cleanups and documentation
* [Revision #d5f5062a48](https://github.com/MariaDB/server/commit/d5f5062a48)\
  2024-10-14 13:09:20 +0200
  * our release packages on rhel8 use bundled readline
* [Revision #5777d9f282](https://github.com/MariaDB/server/commit/5777d9f282)\
  2024-10-14 02:25:25 +0530
  * [MDEV-35116](https://jira.mariadb.org/browse/MDEV-35116) InnoDB fails to set error index for HA\_ERR\_NULL\_IN\_SPATIAL
* [Revision #b138f428ea](https://github.com/MariaDB/server/commit/b138f428ea)\
  2024-10-04 10:15:35 +0200
  * [MDEV-18151](https://jira.mariadb.org/browse/MDEV-18151) Skipped error returning for GRANT/SET PASSWORD
* [Revision #cc59fbfffa](https://github.com/MariaDB/server/commit/cc59fbfffa)\
  2024-10-04 09:28:46 +0200
  * [MDEV-18151](https://jira.mariadb.org/browse/MDEV-18151) Skipped error returning for GRANT/SET PASSWORD
* [Revision #9cd9c3cf16](https://github.com/MariaDB/server/commit/9cd9c3cf16)\
  2024-10-04 10:13:10 +0200
  * fix grant5 test to return to the original database.
* [Revision #8981ee238a](https://github.com/MariaDB/server/commit/8981ee238a)\
  2024-10-09 11:26:12 +0300
  * [MDEV-33106](https://jira.mariadb.org/browse/MDEV-33106) innodb.innodb-lock-inherit-read\_commited times out
* [Revision #23820f1d79](https://github.com/MariaDB/server/commit/23820f1d79)\
  2024-10-08 22:55:50 +0530
  * [MDEV-34392](https://jira.mariadb.org/browse/MDEV-34392) Inplace algorithm violates the foreign key constraint
* [Revision #4281e0068b](https://github.com/MariaDB/server/commit/4281e0068b)\
  2024-10-06 17:41:07 +0200
  * [MDEV-35082](https://jira.mariadb.org/browse/MDEV-35082) HANDLER with FULLTEXT keys is not always rejected
* [Revision #23d7dc1ea1](https://github.com/MariaDB/server/commit/23d7dc1ea1)\
  2024-10-06 17:06:07 +0200
  * [MDEV-35086](https://jira.mariadb.org/browse/MDEV-35086) Trying to lock mutex when the mutex was already locked (session\_tracker.cc), server hangs
* [Revision #3ea71a2c8e](https://github.com/MariaDB/server/commit/3ea71a2c8e)\
  2024-08-31 23:57:33 +0200
  * [MDEV-16699](https://jira.mariadb.org/browse/MDEV-16699) heap-use-after-free in group\_concat with compressed or GIS columns
* [Revision #65418ca9ad](https://github.com/MariaDB/server/commit/65418ca9ad)\
  2024-10-08 16:43:57 +0530
  * [MDEV-34392](https://jira.mariadb.org/browse/MDEV-34392) Inplace algorithm violates the foreign key constraint
* [Revision #706a8bcb5b](https://github.com/MariaDB/server/commit/706a8bcb5b)\
  2024-10-08 13:08:10 +0300
  * [MDEV-33470](https://jira.mariadb.org/browse/MDEV-33470) Unique hash index is broken on DML for system-versioned table
* [Revision #d37bb140b1](https://github.com/MariaDB/server/commit/d37bb140b1)\
  2024-10-08 13:08:10 +0300
  * [MDEV-31297](https://jira.mariadb.org/browse/MDEV-31297) Create table as select on system versioned tables do not work consistently on replication
* [Revision #4e4c7dd4f5](https://github.com/MariaDB/server/commit/4e4c7dd4f5)\
  2024-10-08 13:08:10 +0300
  * [MDEV-28288](https://jira.mariadb.org/browse/MDEV-28288) System versioning doesn't support correct work for engine=connect and doesn't always give any warnings/errors
* [Revision #5b940bdcfc](https://github.com/MariaDB/server/commit/5b940bdcfc)\
  2024-10-08 13:08:10 +0300
  * [MDEV-25060](https://jira.mariadb.org/browse/MDEV-25060) Freeing overrun buffer, various crashes, ASAN heap-buffer-overflow in \_mi\_put\_key\_in\_record
* [Revision #5673cbe094](https://github.com/MariaDB/server/commit/5673cbe094)\
  2024-10-04 12:49:37 +0300
  * [MDEV-35074](https://jira.mariadb.org/browse/MDEV-35074): selectivity\_notembedded fails with --view-protocol
* [Revision #e9c999caf4](https://github.com/MariaDB/server/commit/e9c999caf4)\
  2024-09-20 16:28:55 +1000
  * [MDEV-34915](https://jira.mariadb.org/browse/MDEV-34915) Sort output of session track system variable in mysqltest
* [Revision #ab15628bbc](https://github.com/MariaDB/server/commit/ab15628bbc)\
  2024-10-03 10:07:17 +0200
  * [MDEV-35050](https://jira.mariadb.org/browse/MDEV-35050) fix for embedded
* [Revision #6878c9d591](https://github.com/MariaDB/server/commit/6878c9d591)\
  2024-10-03 10:40:58 +0300
  * [MDEV-35050](https://jira.mariadb.org/browse/MDEV-35050) fixup: ./mtr --embedded
* [Revision #170e4555e2](https://github.com/MariaDB/server/commit/170e4555e2)\
  2024-10-03 08:15:48 +0300
  * [MDEV-35040](https://jira.mariadb.org/browse/MDEV-35040): Fix std::unique deleter for clang++-20 -stdlib=libc++
* [Revision #23debf214f](https://github.com/MariaDB/server/commit/23debf214f)\
  2024-10-03 08:15:17 +0300
  * [MDEV-28091](https://jira.mariadb.org/browse/MDEV-28091) fixup: Fix another pfs\_malloc() stub
* [Revision #1f7898f686](https://github.com/MariaDB/server/commit/1f7898f686)\
  2024-09-25 11:09:09 +1000
  * mroonga: remove -Wunused-but-set-variable warnings
* [Revision #3723fd1573](https://github.com/MariaDB/server/commit/3723fd1573)\
  2024-09-25 11:06:11 +1000
  * [MDEV-35007](https://jira.mariadb.org/browse/MDEV-35007) mroonga should modify source files during build
* [Revision #1cda4726ca](https://github.com/MariaDB/server/commit/1cda4726ca)\
  2024-09-24 10:23:34 +0300
  * [MDEV-34993](https://jira.mariadb.org/browse/MDEV-34993), part2: backport optimizer\_adjust\_secondary\_key\_costs
* [Revision #8166a5d33d](https://github.com/MariaDB/server/commit/8166a5d33d)\
  2024-09-24 09:44:39 +0300
  * [MDEV-34993](https://jira.mariadb.org/browse/MDEV-34993): Incorrect cardinality estimation causes poor query plan
* [Revision #9021f40b8e](https://github.com/MariaDB/server/commit/9021f40b8e)\
  2024-09-30 18:08:00 +0200
  * [MDEV-35050](https://jira.mariadb.org/browse/MDEV-35050) Found wrong usage of mutex upon setting plugin session variables
* [Revision #b1bbdbab9e](https://github.com/MariaDB/server/commit/b1bbdbab9e)\
  2024-09-27 12:58:15 +0200
  * cleanup: remove redundant if()
* [Revision #813e592763](https://github.com/MariaDB/server/commit/813e592763)\
  2024-09-27 13:10:17 +0200
  * compilation failure in CONNECT
* [Revision #5bf543fd43](https://github.com/MariaDB/server/commit/5bf543fd43)\
  2024-09-24 19:08:24 +0200
  * [MDEV-24193](https://jira.mariadb.org/browse/MDEV-24193) UBSAN: sql/sql\_acl.cc:9985:29: runtime error: member access within null pointer of type 'struct TABLE' , ASAN: use-after-poison in handle\_grant\_table
* [Revision #2cdcfb644c](https://github.com/MariaDB/server/commit/2cdcfb644c)\
  2024-09-24 14:40:04 +0200
  * [MDEV-26314](https://jira.mariadb.org/browse/MDEV-26314) ST\_EQUALS listed twice in information\_schema.SQL\_FUNCTIONS
* [Revision #464055fe65](https://github.com/MariaDB/server/commit/464055fe65)\
  2024-10-01 18:35:39 +0300
  * [MDEV-34078](https://jira.mariadb.org/browse/MDEV-34078) Memory leak in InnoDB purge with 32-column PRIMARY KEY
* [Revision #8d810e9426](https://github.com/MariaDB/server/commit/8d810e9426)\
  2024-09-20 14:58:23 +0200
  * [MDEV-29537](https://jira.mariadb.org/browse/MDEV-29537) Creation of view with UNION and SELECT ... FOR UPDATE in definition is failed with error
* [Revision #cc810e64d4](https://github.com/MariaDB/server/commit/cc810e64d4)\
  2024-09-30 13:37:26 +0530
  * [MDEV-34392](https://jira.mariadb.org/browse/MDEV-34392) Inplace algorithm violates the foreign key constraint
* [Revision #45298b730b](https://github.com/MariaDB/server/commit/45298b730b)\
  2024-09-20 08:48:52 +0200
  * sql/handler: referenced\_by\_foreign\_key() returns bool
* [Revision #b88f1267e4](https://github.com/MariaDB/server/commit/b88f1267e4)\
  2024-09-19 18:57:37 +0200
  * [MDEV-33373](https://jira.mariadb.org/browse/MDEV-33373) part 2: Unexpected ER\_FILE\_NOT\_FOUND upon reading from logging table after crash recovery
* [Revision #20f57a8529](https://github.com/MariaDB/server/commit/20f57a8529)\
  2024-09-19 16:51:05 +0200
  * [MDEV-33373](https://jira.mariadb.org/browse/MDEV-33373) part 1: Unexpected ER\_FILE\_NOT\_FOUND upon reading from logging table after crash recovery
* [Revision #282b92f0a2](https://github.com/MariaDB/server/commit/282b92f0a2)\
  2024-07-18 17:26:27 +0800
  * [MDEV-34589](https://jira.mariadb.org/browse/MDEV-34589) Do not execute before queries in spider\_db\_mbase::rollback()
* [Revision #42735c557e](https://github.com/MariaDB/server/commit/42735c557e)\
  2024-08-02 15:27:35 +1000
  * [MDEV-34636](https://jira.mariadb.org/browse/MDEV-34636) Spider: reset wide\_handler->trx in two occasions
* [Revision #f43ea935a1](https://github.com/MariaDB/server/commit/f43ea935a1)\
  2024-07-25 17:24:13 +0800
  * [MDEV-34636](https://jira.mariadb.org/browse/MDEV-34636) Remove implementation of ha-spider::extra() with MERGE flags
* [Revision #69874ee95c](https://github.com/MariaDB/server/commit/69874ee95c)\
  2024-09-30 15:12:00 +1000
  * [MDEV-34828](https://jira.mariadb.org/browse/MDEV-34828) Remove some obsolete cmake code related to the removed spider handlersocket support
* [Revision #95d285fb75](https://github.com/MariaDB/server/commit/95d285fb75)\
  2024-09-30 00:31:48 +0200
  * [MDEV-30307](https://jira.mariadb.org/browse/MDEV-30307) addendum: support for compilation in release mode
* [Revision #cf0c3ec274](https://github.com/MariaDB/server/commit/cf0c3ec274)\
  2022-12-28 19:44:41 +0200
  * [MDEV-30307](https://jira.mariadb.org/browse/MDEV-30307) KILL command inside a transaction causes problem for galera replication
* [Revision #78e640ea3e](https://github.com/MariaDB/server/commit/78e640ea3e)\
  2024-09-27 14:44:20 +0200
  * [MDEV-34808](https://jira.mariadb.org/browse/MDEV-34808) Update HeidiSQL to v12.8
* [Revision #2c0b7ff2b4](https://github.com/MariaDB/server/commit/2c0b7ff2b4)\
  2024-09-27 14:42:53 +0200
  * Windows : support Wix toolset 3.14
* [Revision #be164fc401](https://github.com/MariaDB/server/commit/be164fc401)\
  2024-09-04 00:58:59 +0000
  * ssl\_cipher parameter cannot configure TLSv1.3 and TLSv1.2 ciphers at the same time
* [Revision #9f61aa4f8a](https://github.com/MariaDB/server/commit/9f61aa4f8a)\
  2024-08-16 11:58:06 +0300
  * [MDEV-34822](https://jira.mariadb.org/browse/MDEV-34822) pre-fix: Make wsrep\_ready flag read lock-free
* [Revision #024e95128b](https://github.com/MariaDB/server/commit/024e95128b)\
  2024-09-03 12:11:05 +0300
  * [MDEV-32996](https://jira.mariadb.org/browse/MDEV-32996) : galera.galera\_var\_ignore\_apply\_errors -> \[ERROR] WSREP: Inconsistency detected
* [Revision #0ce5603b86](https://github.com/MariaDB/server/commit/0ce5603b86)\
  2024-09-03 09:07:19 +0300
  * [MDEV-33035](https://jira.mariadb.org/browse/MDEV-33035) : Galera test case [MDEV-16509](https://jira.mariadb.org/browse/MDEV-16509) unstable
* [Revision #b2429e2025](https://github.com/MariaDB/server/commit/b2429e2025)\
  2024-09-20 18:06:38 +0300
  * [MDEV-34976](https://jira.mariadb.org/browse/MDEV-34976) Server crash report broken if Galera is not loaded
* [Revision #f7c5182b7c](https://github.com/MariaDB/server/commit/f7c5182b7c)\
  2024-09-18 16:38:11 -0400
  * [MDEV-31636](https://jira.mariadb.org/browse/MDEV-31636) Memory leak in Sys\_var\_gtid\_binlog\_state::do\_check()
* [Revision #d67c88946f](https://github.com/MariaDB/server/commit/d67c88946f)\
  2024-09-22 21:35:19 +0300
  * Debugging: add dbug\_print\_join\_prefix() to use in best\_access\_path
* [Revision #42eb64e64d](https://github.com/MariaDB/server/commit/42eb64e64d)\
  2024-09-24 17:47:34 +1000
  * [MDEV-34996](https://jira.mariadb.org/browse/MDEV-34996) Buildbot MSAN options should be in server
* [Revision #ad5b9c207c](https://github.com/MariaDB/server/commit/ad5b9c207c)\
  2024-09-23 17:53:11 +0700
  * [MDEV-27944](https://jira.mariadb.org/browse/MDEV-27944): View-protocol fails if database was changed
* [Revision #53f5ee7929](https://github.com/MariaDB/server/commit/53f5ee7929)\
  2024-09-24 08:44:52 +0200
  * [MDEV-34994](https://jira.mariadb.org/browse/MDEV-34994): sql/mysqld: stop accept() loop after the first EAGAIN
* [Revision #8fd1b060f8](https://github.com/MariaDB/server/commit/8fd1b060f8)\
  2024-09-22 08:46:35 +0200
  * reformat galera sst error messages
* [Revision #dd1cad7e5f](https://github.com/MariaDB/server/commit/dd1cad7e5f)\
  2024-09-22 08:45:26 +0200
  * galera\_3nodes.[MDEV-29171](https://jira.mariadb.org/browse/MDEV-29171) fails
* [Revision #c9f54e20d4](https://github.com/MariaDB/server/commit/c9f54e20d4)\
  2024-09-19 10:55:25 +0200
  * [MDEV-33990](https://jira.mariadb.org/browse/MDEV-33990): SHOW STATUS counts ER\_CON\_COUNT\_ERROR as Connection\_errors\_internal
* [Revision #bbc62b1b9e](https://github.com/MariaDB/server/commit/bbc62b1b9e)\
  2024-09-06 19:09:02 +0200
  * clarify --thread-pool-mode usage
* [Revision #99837b6df6](https://github.com/MariaDB/server/commit/99837b6df6)\
  2024-09-18 20:54:38 +0200
  * restore --clent-rr after 7d86751de56
* [Revision #681609d8a0](https://github.com/MariaDB/server/commit/681609d8a0)\
  2024-09-20 15:07:39 +0400
  * [MDEV-32891](https://jira.mariadb.org/browse/MDEV-32891) Assertion \`value <= ((ulonglong) 0xFFFFFFFFL) \* 10000ULL' failed in str\_to\_DDhhmmssff\_internal
* [Revision #607fc15393](https://github.com/MariaDB/server/commit/607fc15393)\
  2024-09-20 14:10:27 +0400
  * [MDEV-31302](https://jira.mariadb.org/browse/MDEV-31302) Assertion \`mon > 0 && mon < 13' failed in my\_time\_t sec\_since\_epoch(int, int, int, int, int, int)
* [Revision #9ac8172ac3](https://github.com/MariaDB/server/commit/9ac8172ac3)\
  2024-09-20 11:47:56 +0400
  * [MDEV-31221](https://jira.mariadb.org/browse/MDEV-31221) UBSAN runtime error: negation of -9223372036854775808 cannot be represented in type 'long long int' in my\_strtoll10\_utf32
* [Revision #841dc07ee1](https://github.com/MariaDB/server/commit/841dc07ee1)\
  2024-09-20 09:23:33 +0400
  * [MDEV-28386](https://jira.mariadb.org/browse/MDEV-28386) UBSAN: runtime error: negation of -X cannot be represented in type 'long long int'; cast to an unsigned type to negate this value to itself in my\_strntoull\_8bit on SELECT ... OCT
* [Revision #0a5e4a0191](https://github.com/MariaDB/server/commit/0a5e4a0191)\
  2024-05-23 08:54:14 +0700
  * [MDEV-31005](https://jira.mariadb.org/browse/MDEV-31005): Make working cursor-protocol
* [Revision #ab569524dc](https://github.com/MariaDB/server/commit/ab569524dc)\
  2024-05-21 17:46:29 +0700
  * [MDEV-31005](https://jira.mariadb.org/browse/MDEV-31005): Make working cursor-protocol
* [Revision #450040e0da](https://github.com/MariaDB/server/commit/450040e0da)\
  2024-09-18 16:41:57 +1000
  * [MDEV-34952](https://jira.mariadb.org/browse/MDEV-34952) main.log\_slow test failure on opensuse builder
* [Revision #68938d2b42](https://github.com/MariaDB/server/commit/68938d2b42)\
  2024-09-09 08:50:02 -0600
  * [MDEV-33500](https://jira.mariadb.org/browse/MDEV-33500) (part 2): rpl.rpl\_parallel\_sbm can still fail
* [Revision #a1adabdd5c](https://github.com/MariaDB/server/commit/a1adabdd5c)\
  2024-09-17 08:44:20 +0400
  * [MDEV-25900](https://jira.mariadb.org/browse/MDEV-25900) Assertion `octets < 1024' failed in Binlog_type_info_fixed_string::Binlog_type_info_fixed_string OR Assertion` field\_length < 1024' failed in Field\_string::save\_field\_metadata
* [Revision #222744c54e](https://github.com/MariaDB/server/commit/222744c54e)\
  2024-09-16 04:57:56 +0200
  * galera SST scripts: fixing glitchy sockstat issues for FreeBSD
* [Revision #45be538cf4](https://github.com/MariaDB/server/commit/45be538cf4)\
  2024-09-15 06:46:53 +0200
  * galera SST scripts: added missing 'datadir' parameter for mysqldump method
* [Revision #64356509af](https://github.com/MariaDB/server/commit/64356509af)\
  2024-09-15 04:34:33 +0200
  * galera SST scripts: moving mysqldump-specific code out of the wsrep\_sst\_common
* [Revision #228cb073ad](https://github.com/MariaDB/server/commit/228cb073ad)\
  2024-09-15 04:27:23 +0200
  * galera SST scripts: comments update
* [Revision #46a5d2f1cf](https://github.com/MariaDB/server/commit/46a5d2f1cf)\
  2024-09-15 04:12:27 +0200
  * galera SST scripts: unification of the previous SST completion check
* [Revision #7742cc9ff9](https://github.com/MariaDB/server/commit/7742cc9ff9)\
  2024-09-13 16:46:12 +0200
  * galera SST scripts: more robust port checking
* [Revision #642195d255](https://github.com/MariaDB/server/commit/642195d255)\
  2024-09-12 19:00:26 +0200
  * [MDEV-34234](https://jira.mariadb.org/browse/MDEV-34234): SST hangs when running on unprivileged containers on RHEL9
* [Revision #202fd502cf](https://github.com/MariaDB/server/commit/202fd502cf)\
  2024-09-12 17:29:24 +0200
  * galera SST scripts: fixes for error logging in non-linux systems
* [Revision #606c867e7f](https://github.com/MariaDB/server/commit/606c867e7f)\
  2024-09-11 18:53:24 +0200
  * galera SST scripts: moving common code to wsrep\_sst\_common file
* [Revision #4cb73f49bc](https://github.com/MariaDB/server/commit/4cb73f49bc)\
  2024-09-10 22:57:51 +0200
  * galera SST scripts: unification of wsrep\_sst\_backup with the other scripts
* [Revision #fbd8829149](https://github.com/MariaDB/server/commit/fbd8829149)\
  2024-09-10 03:45:19 +0200
  * galera SST scripts: removing obsolete xtrabackup\_pid support
* [Revision #5cb436e07b](https://github.com/MariaDB/server/commit/5cb436e07b)\
  2024-09-10 02:44:46 +0200
  * [MDEV-30822](https://jira.mariadb.org/browse/MDEV-30822) preparation: refactoring galera sst scripts
* [Revision #7ee0e60bbb](https://github.com/MariaDB/server/commit/7ee0e60bbb)\
  2024-09-03 07:39:30 +0200
  * galera mtr tests: minor fixes to make tests more reliable
* [Revision #4010dff058](https://github.com/MariaDB/server/commit/4010dff058)\
  2024-09-14 11:05:44 +0300
  * mtr\_t::log\_file\_op(): Fix -Wnonnull
* [Revision #b331cde26b](https://github.com/MariaDB/server/commit/b331cde26b)\
  2024-09-13 14:34:08 +0300
  * [MDEV-34921](https://jira.mariadb.org/browse/MDEV-34921) MemorySanitizer reports errors for non-debug builds
* [Revision #95885261f0](https://github.com/MariaDB/server/commit/95885261f0)\
  2024-07-22 11:13:06 -0400
  * [MDEV-27037](https://jira.mariadb.org/browse/MDEV-27037) mysqlbinlog emits a warning when reaching EOF before stop-datetime
* [Revision #242b67f1de](https://github.com/MariaDB/server/commit/242b67f1de)\
  2024-07-12 09:15:19 -0400
  * [MDEV-27037](https://jira.mariadb.org/browse/MDEV-27037) mysqlbinlog emits a warning when reaching EOF before stop-condition
* [Revision #cc0faa1e3e](https://github.com/MariaDB/server/commit/cc0faa1e3e)\
  2024-06-19 12:05:09 +0800
  * [MDEV-31788](https://jira.mariadb.org/browse/MDEV-31788) Factor functions to reduce duplication around spider\_check\_and\_init\_casual\_read in ha\_spider.cc
* [Revision #0ba97e4dc6](https://github.com/MariaDB/server/commit/0ba97e4dc6)\
  2024-06-19 11:29:57 +0800
  * [MDEV-31788](https://jira.mariadb.org/browse/MDEV-31788) Factor out calls to spider\_ping\_table\_mon\_from\_table in ha\_spider.cc
* [Revision #9e1579788f](https://github.com/MariaDB/server/commit/9e1579788f)\
  2024-09-10 11:52:22 +1000
  * [MDEV-31788](https://jira.mariadb.org/browse/MDEV-31788) Factor spider locking and unlocking code around sending queries
* [Revision #84067291b4](https://github.com/MariaDB/server/commit/84067291b4)\
  2024-06-18 19:14:42 +0800
  * [MDEV-28360](https://jira.mariadb.org/browse/MDEV-28360) Spider: remove #ifdef SPIDER\_use\_LEX\_CSTRING\_for\_KEY\_Field\_name
* [Revision #f5b7c25e1e](https://github.com/MariaDB/server/commit/f5b7c25e1e)\
  2024-06-18 10:21:38 +0800
  * [MDEV-27643](https://jira.mariadb.org/browse/MDEV-27643) Spider: remove #ifdef HA\_CAN\_BULK\_ACCESS
* [Revision #e7570c7759](https://github.com/MariaDB/server/commit/e7570c7759)\
  2024-06-17 13:15:42 +0800
  * [MDEV-31788](https://jira.mariadb.org/browse/MDEV-31788) Remove spider\_file\_pos
* [Revision #a81f419b06](https://github.com/MariaDB/server/commit/a81f419b06)\
  2024-06-19 13:55:02 +0800
  * [MDEV-27648](https://jira.mariadb.org/browse/MDEV-27648) remove #define HASH\_UPDATE\_WITH\_HASH\_VALUE
* [Revision #5d54e86c22](https://github.com/MariaDB/server/commit/5d54e86c22)\
  2024-06-17 10:19:30 +0800
  * [MDEV-26178](https://jira.mariadb.org/browse/MDEV-26178) spider: delete spd\_environ.h
* [Revision #869c501ac3](https://github.com/MariaDB/server/commit/869c501ac3)\
  2024-06-19 13:52:29 +0800
  * [MDEV-27644](https://jira.mariadb.org/browse/MDEV-27644) Spider: remove HANDLER\_HAS\_DIRECT\_AGGREGATE
* [Revision #3a58291680](https://github.com/MariaDB/server/commit/3a58291680)\
  2024-06-19 13:52:07 +0800
  * [MDEV-27662](https://jira.mariadb.org/browse/MDEV-27662) remove SPIDER\_SUPPORT\_CREATE\_OR\_REPLACE\_TABLE
* [Revision #84977868b1](https://github.com/MariaDB/server/commit/84977868b1)\
  2024-06-19 13:50:20 +0800
  * [MDEV-27809](https://jira.mariadb.org/browse/MDEV-27809) remove SPIDER\_I\_S\_USE\_SHOW\_FOR\_COLUMN
* [Revision #6287fb6e17](https://github.com/MariaDB/server/commit/6287fb6e17)\
  2024-06-19 13:47:18 +0800
  * [MDEV-27652](https://jira.mariadb.org/browse/MDEV-27652) remove #ifdef HA\_HAS\_CHECKSUM\_EXTENDED
* [Revision #e8a5553cef](https://github.com/MariaDB/server/commit/e8a5553cef)\
  2024-06-19 13:47:07 +0800
  * [MDEV-27808](https://jira.mariadb.org/browse/MDEV-27808) remove SPIDER\_LIKE\_FUNC\_HAS\_GET\_NEGATED
* [Revision #ab49b46d01](https://github.com/MariaDB/server/commit/ab49b46d01)\
  2024-06-19 13:46:46 +0800
  * [MDEV-27664](https://jira.mariadb.org/browse/MDEV-27664) remove SPIDER\_SQL\_CACHE\_IS\_IN\_LEX
* [Revision #a1e5ee9111](https://github.com/MariaDB/server/commit/a1e5ee9111)\
  2024-06-19 13:43:28 +0800
  * [MDEV-27663](https://jira.mariadb.org/browse/MDEV-27663) remove SPIDER\_USE\_CONST\_ITEM\_FOR\_STRING\_INT\_REAL\_DECIMAL\_DATE\_ITEM
* [Revision #5e98471df1](https://github.com/MariaDB/server/commit/5e98471df1)\
  2024-06-19 13:43:05 +0800
  * [MDEV-27811](https://jira.mariadb.org/browse/MDEV-27811): remove SPIDER\_MDEV\_16246
* [Revision #8c8684b17f](https://github.com/MariaDB/server/commit/8c8684b17f)\
  2024-06-19 13:42:50 +0800
  * [MDEV-28226](https://jira.mariadb.org/browse/MDEV-28226) Remove HANDLER\_HAS\_NEED\_INFO\_FOR\_AUTO\_INC
* [Revision #affcb0713d](https://github.com/MariaDB/server/commit/affcb0713d)\
  2024-06-19 13:42:36 +0800
  * [MDEV-26178](https://jira.mariadb.org/browse/MDEV-26178) spider: remove PARTITION\_HAS\_GET\_PART\_SPEC
* [Revision #6d0d09ebc2](https://github.com/MariaDB/server/commit/6d0d09ebc2)\
  2024-06-19 13:42:25 +0800
  * [MDEV-26178](https://jira.mariadb.org/browse/MDEV-26178) Spider: remove HANDLER\_HAS\_TOP\_TABLE\_FIELDS
* [Revision #1cb75d9a33](https://github.com/MariaDB/server/commit/1cb75d9a33)\
  2024-06-19 13:42:10 +0800
  * [MDEV-27660](https://jira.mariadb.org/browse/MDEV-27660) Remove #ifdef SPIDER\_HANDLER\_START\_BULK\_INSERT\_HAS\_FLAGS
* [Revision #aaba68ac1e](https://github.com/MariaDB/server/commit/aaba68ac1e)\
  2024-06-19 13:41:53 +0800
  * [MDEV-28896](https://jira.mariadb.org/browse/MDEV-28896) Spider: remove #ifdef SPIDER\_UPDATE\_ROW\_HAS\_CONST\_NEW\_DATA
* [Revision #f16c037753](https://github.com/MariaDB/server/commit/f16c037753)\
  2024-06-19 13:37:51 +0800
  * [MDEV-28895](https://jira.mariadb.org/browse/MDEV-28895) Spider: remove #ifdef HANDLER\_HAS\_CAN\_USE\_FOR\_AUTO\_INC\_INIT
* [Revision #0650c87d9b](https://github.com/MariaDB/server/commit/0650c87d9b)\
  2024-06-19 13:36:48 +0800
  * [MDEV-27647](https://jira.mariadb.org/browse/MDEV-27647) Spider: remove HANDLER\_HAS\_DIRECT\_UPDATE\_ROWS
* [Revision #d5d65b948b](https://github.com/MariaDB/server/commit/d5d65b948b)\
  2024-06-19 13:36:03 +0800
  * [MDEV-26178](https://jira.mariadb.org/browse/MDEV-26178) Spider: remove HA\_EXTRA\_HAS\_HA\_EXTRA\_USE\_CMP\_REF
* [Revision #de3dd942c0](https://github.com/MariaDB/server/commit/de3dd942c0)\
  2024-06-19 13:35:05 +0800
  * [MDEV-28894](https://jira.mariadb.org/browse/MDEV-28894) Spider: remove #ifdef HA\_EXTRA\_HAS\_STARTING\_ORDERED\_INDEX\_SCAN
* [Revision #64581c83e8](https://github.com/MariaDB/server/commit/64581c83e8)\
  2024-06-19 13:34:30 +0800
  * [MDEV-28893](https://jira.mariadb.org/browse/MDEV-28893) Spider: remove #ifdef SPIDER\_NET\_HAS\_THD
* [Revision #ba9bebd719](https://github.com/MariaDB/server/commit/ba9bebd719)\
  2024-06-19 13:33:33 +0800
  * [MDEV-28892](https://jira.mariadb.org/browse/MDEV-28892) remove #ifdef SPIDER\_Item\_args\_arg\_count\_IS\_PROTECTED
* [Revision #05fafaf82d](https://github.com/MariaDB/server/commit/05fafaf82d)\
  2024-06-19 13:22:59 +0800
  * [MDEV-27646](https://jira.mariadb.org/browse/MDEV-27646) remove SPIDER\_HAS\_HASH\_VALUE\_TYPE
* [Revision #f06060f5ed](https://github.com/MariaDB/server/commit/f06060f5ed)\
  2024-09-06 14:31:55 +0300
  * Cleanup: Remove the function dict\_remove\_db\_name()
* [Revision #024a18dbcb](https://github.com/MariaDB/server/commit/024a18dbcb)\
  2024-09-06 14:29:09 +0300
  * [MDEV-34823](https://jira.mariadb.org/browse/MDEV-34823) Invalid arguments in ib\_push\_warning()
* [Revision #e886c2ba02](https://github.com/MariaDB/server/commit/e886c2ba02)\
  2024-08-21 15:47:37 +1000
  * [MDEV-34757](https://jira.mariadb.org/browse/MDEV-34757) Check leaf\_tables\_saved in partition pruning in UPDATE and DELETE
* [Revision #00cb344085](https://github.com/MariaDB/server/commit/00cb344085)\
  2024-08-16 17:04:23 +1000
  * [MDEV-33858](https://jira.mariadb.org/browse/MDEV-33858) Assertion \`(mem\_root->flags & 4) == 0' fails on 2nd execution of PS with -DWITH\_PROTECT\_STATEMENT\_MEMROOT=ON
* [Revision #2c3e07df47](https://github.com/MariaDB/server/commit/2c3e07df47)\
  2024-09-06 11:34:31 +1000
  * [MDEV-34447](https://jira.mariadb.org/browse/MDEV-34447): Memory leakage is detected on running the test main.ps against the server 11.1
* [Revision #8024b8e4c1](https://github.com/MariaDB/server/commit/8024b8e4c1)\
  2024-09-05 11:22:40 +1000
  * [MDEV-33091](https://jira.mariadb.org/browse/MDEV-33091) pcre2 headers - handle columnstore
* [Revision #dff354e7df](https://github.com/MariaDB/server/commit/dff354e7df)\
  2024-08-28 18:56:55 +1000
  * [MDEV-34825](https://jira.mariadb.org/browse/MDEV-34825): my\_cpu.h - non-glibc ism for POWER
* [Revision #e9b70e59a3](https://github.com/MariaDB/server/commit/e9b70e59a3)\
  2024-08-28 18:40:52 +1000
  * [MDEV-34825](https://jira.mariadb.org/browse/MDEV-34825) FreeBSD - upstream riscv64 compatibility patch
* [Revision #7b2b03c4f2](https://github.com/MariaDB/server/commit/7b2b03c4f2)\
  2024-08-28 18:37:49 +1000
  * [MDEV-34825](https://jira.mariadb.org/browse/MDEV-34825) FreeBSD fails to build under clang natively
* [Revision #566c22e814](https://github.com/MariaDB/server/commit/566c22e814)\
  2024-02-01 11:26:36 +0100
  * pcre.cmake: always check the library with check\_library\_exists()
* [Revision #b2ebe1cb7b](https://github.com/MariaDB/server/commit/b2ebe1cb7b)\
  2024-01-12 16:57:37 +0100
  * [MDEV-33091](https://jira.mariadb.org/browse/MDEV-33091) pcre2 headers aren't found on Solaris
* [Revision #2e23c7342f](https://github.com/MariaDB/server/commit/2e23c7342f)\
  2024-08-28 14:32:37 +1000
  * [MDEV-34567](https://jira.mariadb.org/browse/MDEV-34567) unit.my\_apc always failing on FreeBSD-14
* [Revision #c991efd9c3](https://github.com/MariaDB/server/commit/c991efd9c3)\
  2024-08-28 13:34:53 +1000
  * [MDEV-34825](https://jira.mariadb.org/browse/MDEV-34825) FreeBSD fails to build under clang natively
* [Revision #d1dc70675c](https://github.com/MariaDB/server/commit/d1dc70675c)\
  2024-09-04 10:10:04 +1000
  * [MDEV-34864](https://jira.mariadb.org/browse/MDEV-34864) SHOW INDEX FROM - SEQ\_IN\_INDEX to ULong
* [Revision #235f33e360](https://github.com/MariaDB/server/commit/235f33e360)\
  2024-01-17 17:32:29 +0300
  * [MDEV-33133](https://jira.mariadb.org/browse/MDEV-33133): MDL conflict handling code should skip BF-aborted trxs
* [Revision #7e748d075b](https://github.com/MariaDB/server/commit/7e748d075b)\
  2024-08-30 08:32:10 +0300
  * [MDEV-34841](https://jira.mariadb.org/browse/MDEV-34841) : Enable working Galera tests
* [Revision #dd64f29d6b](https://github.com/MariaDB/server/commit/dd64f29d6b)\
  2024-04-12 11:24:42 +0300
  * [MDEV-33897](https://jira.mariadb.org/browse/MDEV-33897) : Galera test failure on galera\_3nodes.galera\_gtid\_consistency
* [Revision #83196a7b23](https://github.com/MariaDB/server/commit/83196a7b23)\
  2024-05-19 22:09:18 +0300
  * Add a basic MTR test for DDL error voting to ensure that all DDLs generate consistent error messages,
* [Revision #731a5aba0b](https://github.com/MariaDB/server/commit/731a5aba0b)\
  2024-05-19 21:08:46 +0300
  * Use only MySQL code for TOI error vote
* [Revision #7119149f83](https://github.com/MariaDB/server/commit/7119149f83)\
  2024-05-19 21:26:46 +0300
  * If donor loop receives unknown signal from the SST script it is an error condition (SST failure), so it should set error code before exiting.
* [Revision #69c6cb5dc4](https://github.com/MariaDB/server/commit/69c6cb5dc4)\
  2024-05-19 00:23:00 +0300
  * Fix recovering state GTID in case log file contains non-text bytes - use grep with -a option.
* [Revision #54a10a4293](https://github.com/MariaDB/server/commit/54a10a4293)\
  2024-05-21 12:40:19 +0300
  * [MDEV-32363](https://jira.mariadb.org/browse/MDEV-32363) Shut down Galera networking and logging on fatal signal
* [Revision #b65bbb2fae](https://github.com/MariaDB/server/commit/b65bbb2fae)\
  2024-08-30 15:49:51 +0200
  * [MDEV-34647](https://jira.mariadb.org/browse/MDEV-34647): small refactoring after main fix
* [Revision #74d7168765](https://github.com/MariaDB/server/commit/74d7168765)\
  2024-08-30 10:28:28 -0700
  * [MDEV-25084](https://jira.mariadb.org/browse/MDEV-25084) Assertion failure when moving equality from having to where
* [Revision #9091afdc55](https://github.com/MariaDB/server/commit/9091afdc55)\
  2023-06-15 14:51:56 +0300
  * [MDEV-31173](https://jira.mariadb.org/browse/MDEV-31173) : Server crashes when setting wsrep\_cluster\_address after adding invalid value to wsrep\_allowlist table
* [Revision #b1d74b7e72](https://github.com/MariaDB/server/commit/b1d74b7e72)\
  2024-04-29 10:13:03 +0300
  * [MDEV-33997](https://jira.mariadb.org/browse/MDEV-33997) : Assertion \`((WSREP\_PROVIDER\_EXISTS\_ && this->variables.wsrep\_on) && wsrep\_emulate\_bin\_log) || mysql\_bin\_log.is\_open()' failed in int THD::binlog\_write\_row(TABLE\*, bool, const uchar\*)
* [Revision #5a61fd5819](https://github.com/MariaDB/server/commit/5a61fd5819)\
  2024-08-29 12:30:05 +0200
  * [MDEV-34831](https://jira.mariadb.org/browse/MDEV-34831): [MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704) introduces a typo, --qick
* [Revision #03a5455cb3](https://github.com/MariaDB/server/commit/03a5455cb3)\
  2024-08-29 09:32:29 +0200
  * [MDEV-34833](https://jira.mariadb.org/browse/MDEV-34833) Assertion failure in Item\_float::do\_build\_clone (Item\_static\_float\_func)
* [Revision #872dbec935](https://github.com/MariaDB/server/commit/872dbec935)\
  2024-08-05 16:16:09 +0200
  * [MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704) Quick mode produces the bug for mariadb client
* [Revision #1ff6b6f0b4](https://github.com/MariaDB/server/commit/1ff6b6f0b4)\
  2024-08-28 15:44:42 +0300
  * [MDEV-34802](https://jira.mariadb.org/browse/MDEV-34802) Recovery fails to note some log corruption
* [Revision #e7bb9b7c55](https://github.com/MariaDB/server/commit/e7bb9b7c55)\
  2024-08-27 18:06:24 +0300
  * [MDEV-24923](https://jira.mariadb.org/browse/MDEV-24923) fixup: Correct a function comment
* [Revision #58bc83e1a7](https://github.com/MariaDB/server/commit/58bc83e1a7)\
  2024-08-27 15:36:39 +1000
  * \[fixup] Spider: Restored lines accidentally deleted in [MDEV-32157](https://jira.mariadb.org/browse/MDEV-32157)
* [Revision #8642453ce6](https://github.com/MariaDB/server/commit/8642453ce6)\
  2024-08-19 22:27:44 +0200
  * Fix sporadic failure of test case rpl.rpl\_start\_stop\_slave
* [Revision #25e0224814](https://github.com/MariaDB/server/commit/25e0224814)\
  2024-08-19 20:58:09 +0200
  * Skip mariadb-backup.slave\_provision\_nolock in --valgrind, it uses a lot of CPU
* [Revision #214e6c5b3d](https://github.com/MariaDB/server/commit/214e6c5b3d)\
  2024-08-19 20:37:34 +0200
  * Fix sporadic failure of test case rpl.rpl\_old\_master
* [Revision #7dc4ea5649](https://github.com/MariaDB/server/commit/7dc4ea5649)\
  2024-08-16 21:58:49 +0200
  * Fix sporadic test failure in rpl.rpl\_create\_drop\_event
* [Revision #33854d7324](https://github.com/MariaDB/server/commit/33854d7324)\
  2024-08-03 12:16:32 +0200
  * Restore skiping rpl.rpl\_mdev6020 under Valgrind
* [Revision #b4c2e23954](https://github.com/MariaDB/server/commit/b4c2e23954)\
  2024-08-03 03:51:47 +0200
  * [MDEV-34696](https://jira.mariadb.org/browse/MDEV-34696): do\_gco\_wait() completes too early on InnoDB dict stats updates
* [Revision #1f040ae048](https://github.com/MariaDB/server/commit/1f040ae048)\
  2024-08-20 11:31:58 +0300
  * [MDEV-34043](https://jira.mariadb.org/browse/MDEV-34043) Drastically slower query performance between CentOS (2sec) and Rocky (48sec)
* [Revision #eadf0f63a2](https://github.com/MariaDB/server/commit/eadf0f63a2)\
  2024-08-21 15:32:14 +0200
  * fix [MDEV-34771](https://jira.mariadb.org/browse/MDEV-34771) & [MDEV-34776](https://jira.mariadb.org/browse/MDEV-34776)
* [Revision #0b7d19d500](https://github.com/MariaDB/server/commit/0b7d19d500)\
  2024-08-20 16:12:02 +0200
  * [MDEV-34785](https://jira.mariadb.org/browse/MDEV-34785): Assertion failure in Item\_func\_or\_sum::do\_build\_clone (Item\_func\_not\_all)
* [Revision #b68c100076](https://github.com/MariaDB/server/commit/b68c100076)\
  2024-08-20 18:00:23 +0300
  * [MDEV-34565](https://jira.mariadb.org/browse/MDEV-34565) MariaDB crashes with SIGILL because the OS does not support AVX512
* [Revision #ae02999cdb](https://github.com/MariaDB/server/commit/ae02999cdb)\
  2024-08-19 18:49:04 +0200
  * [MDEV-34776](https://jira.mariadb.org/browse/MDEV-34776) Assertion failure in Item\_string::do\_build\_clone
* [Revision #fccfdc28b8](https://github.com/MariaDB/server/commit/fccfdc28b8)\
  2024-08-19 17:15:46 +0200
  * [MDEV-34771](https://jira.mariadb.org/browse/MDEV-34771) Types mismatch when cloning items causes debug assertion
* [Revision #db8ab4aca2](https://github.com/MariaDB/server/commit/db8ab4aca2)\
  2024-08-19 11:14:11 +0300
  * Sort result from table\_statistics and index\_statistics
* [Revision #e51d55a63f](https://github.com/MariaDB/server/commit/e51d55a63f)\
  2024-08-19 10:59:57 +0300
  * Revert "mtr: remove not\_valgrind\_build"
* [Revision #ba5482ffc2](https://github.com/MariaDB/server/commit/ba5482ffc2)\
  2024-08-16 12:43:35 +0700
  * [MDEV-34718](https://jira.mariadb.org/browse/MDEV-34718): Trigger doesn't work correctly with bulk update
* [Revision #f41a120298](https://github.com/MariaDB/server/commit/f41a120298)\
  2024-08-13 18:28:23 +0200
  * Fix typo in xtrabackup --help output
* [Revision #e40dfcdd89](https://github.com/MariaDB/server/commit/e40dfcdd89)\
  2024-08-15 10:13:49 +0300
  * Fix clang++-19 -Wunused-but-set-variable
* [Revision #ecd910ae3a](https://github.com/MariaDB/server/commit/ecd910ae3a)\
  2024-08-14 08:43:08 +0300
  * [MDEV-34755](https://jira.mariadb.org/browse/MDEV-34755) g++- -Wstringop-truncation due to safe\_strcpy()
* [Revision #b304ec3030](https://github.com/MariaDB/server/commit/b304ec3030)\
  2024-08-13 15:22:09 +0530
  * [MDEV-14231](https://jira.mariadb.org/browse/MDEV-14231) MATCH() AGAINST( IN BOOLEAN MODE), results mismatch
* [Revision #2c5d8376cd](https://github.com/MariaDB/server/commit/2c5d8376cd)\
  2024-08-07 16:40:35 +0200
  * [MDEV-30686](https://jira.mariadb.org/browse/MDEV-30686): Endless loop when trying to establish connection
* [Revision #cd8b8bb964](https://github.com/MariaDB/server/commit/cd8b8bb964)\
  2024-07-18 10:10:26 +0300
  * [MDEV-34594](https://jira.mariadb.org/browse/MDEV-34594) : Assertion \`client\_state.transaction().active()' failed in int wsrep\_thd\_append\_key(THD\*, const wsrep\_key\*, int, Wsrep\_service\_key\_type)
* [Revision #0e27351028](https://github.com/MariaDB/server/commit/0e27351028)\
  2024-06-12 16:53:15 +0400
  * [MDEV-34376](https://jira.mariadb.org/browse/MDEV-34376) Wrong data types when mixing an utf8 \*TEXT column and a short binary
* [Revision #c83ba513da](https://github.com/MariaDB/server/commit/c83ba513da)\
  2024-08-06 20:34:33 +0200
  * Update sponsors
* Merge [Revision #662bb50784](https://github.com/MariaDB/server/commit/662bb50784) 2024-08-09 08:47:24 +0200 - Merge branch '10.5' into mariadb-10.5.26
* [Revision #e997bf58fb](https://github.com/MariaDB/server/commit/e997bf58fb)\
  2024-08-06 14:35:39 +0200
  * [MDEV-34714](https://jira.mariadb.org/browse/MDEV-34714) perror-win test failure on localized Windows
* [Revision #4a67bd5105](https://github.com/MariaDB/server/commit/4a67bd5105)\
  2024-08-08 11:13:41 +0200
  * Fix server on windows, so it does not write to error log byte-by-byte
* [Revision #62fd7b4cd2](https://github.com/MariaDB/server/commit/62fd7b4cd2)\
  2024-07-29 01:10:32 +0200
  * OpenSSL - set all heap functions in CRYPTO\_set\_mem\_functions.
* [Revision #b619be3569](https://github.com/MariaDB/server/commit/b619be3569)\
  2024-07-29 01:03:17 +0200
  * Support -DCONC\_WITH\_SSL parameter passed to CMake
* [Revision #d1713666b0](https://github.com/MariaDB/server/commit/d1713666b0)\
  2024-07-19 21:44:34 +0200
  * Fix incorrect setting of opt\_local\_file in mysqlimport, for named pipe
* [Revision #56fb04aa7c](https://github.com/MariaDB/server/commit/56fb04aa7c)\
  2024-08-08 17:56:56 -0400
  * bump the VERSION
* [Revision #25e2d0a6bb](https://github.com/MariaDB/server/commit/25e2d0a6bb)\
  2024-08-06 15:26:55 +0200
  * [MDEV-34632](https://jira.mariadb.org/browse/MDEV-34632) Assertion failed in handler::assert\_icp\_limitations
* [Revision #bce3f3f628](https://github.com/MariaDB/server/commit/bce3f3f628)\
  2024-08-02 10:29:08 +1000
  * [MDEV-34682](https://jira.mariadb.org/browse/MDEV-34682) Reset spider\_hton\_ptr in error mode of spider\_db\_init()
* [Revision #8b51d34462](https://github.com/MariaDB/server/commit/8b51d34462)\
  2024-07-23 11:57:01 +0300
  * [MDEV-34640](https://jira.mariadb.org/browse/MDEV-34640) : galera\_var\_ignore\_apply\_errors test freezes
* [Revision #71f289e5d1](https://github.com/MariaDB/server/commit/71f289e5d1)\
  2024-07-30 12:30:39 +0300
  * [MDEV-25614](https://jira.mariadb.org/browse/MDEV-25614) : Galera test failure on GCF-354
* [Revision #eb30a9d633](https://github.com/MariaDB/server/commit/eb30a9d633)\
  2024-07-26 09:04:30 +0300
  * [MDEV-34647](https://jira.mariadb.org/browse/MDEV-34647) : 'INSERT...SELECT' on MyISAM table suddenly replicated by Galera
* [Revision #cb80ef93a9](https://github.com/MariaDB/server/commit/cb80ef93a9)\
  2024-07-31 14:45:32 +0300
  * [MDEV-32778](https://jira.mariadb.org/browse/MDEV-32778) : galera\_ssl\_reload failed with warning message
* [Revision #0ba6068a82](https://github.com/MariaDB/server/commit/0ba6068a82)\
  2024-08-01 08:28:28 +0300
  * [MDEV-32782](https://jira.mariadb.org/browse/MDEV-32782) : galera\_sst\_mysqldump\_with\_key test failed
* [Revision #83040474dc](https://github.com/MariaDB/server/commit/83040474dc)\
  2024-05-24 22:51:01 +1000
  * [MDEV-34234](https://jira.mariadb.org/browse/MDEV-34234): make lsof optional on RPM
* [Revision #cf202decde](https://github.com/MariaDB/server/commit/cf202decde)\
  2024-08-02 18:48:29 +0700
  * [MDEV-34683](https://jira.mariadb.org/browse/MDEV-34683) Types mismatch when cloning items causes debug assertion
* [Revision #37119cd256](https://github.com/MariaDB/server/commit/37119cd256)\
  2024-08-01 17:44:54 +0530
  * [MDEV-29010](https://jira.mariadb.org/browse/MDEV-29010) Table cannot be loaded after instant ALTER
* [Revision #d072a29601](https://github.com/MariaDB/server/commit/d072a29601)\
  2024-07-24 13:55:55 +0200
  * [MDEV-23983](https://jira.mariadb.org/browse/MDEV-23983): Crash caused by query containing constant having clause

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
