# MariaDB 10.5.22 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.5/10.5.22.md)[Changelog](mariadb-10-5-22-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.22/)

**Release date:** 14 Aug 2023

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.22.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.31](../changelogs-mariadb-10-4-series/mariadb-10-4-31-changelog.md)
* Merge [Revision #8852afe317](https://github.com/MariaDB/server/commit/8852afe317) 2023-08-08 11:24:42 +0200 - Merge branch '10.4' into 10.5
* [Revision #8adb6107ce](https://github.com/MariaDB/server/commit/8adb6107ce)\
  2023-08-05 21:37:55 +0200
  * [MDEV-31853](https://jira.mariadb.org/browse/MDEV-31853) Assertion failure in Column\_definition::check\_vcol\_for\_key upon adding FK
* [Revision #10eff9c809](https://github.com/MariaDB/server/commit/10eff9c809)\
  2023-08-04 18:38:51 +1000
  * [MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524) Post-merge fixup
* [Revision #8e8c020fb3](https://github.com/MariaDB/server/commit/8e8c020fb3)\
  2023-07-26 19:09:32 +0700
  * [MDEV-31743](https://jira.mariadb.org/browse/MDEV-31743) Server crash in store\_length, assertion failure in Type\_handler\_string\_result::sort\_length
* [Revision #61acb43689](https://github.com/MariaDB/server/commit/61acb43689)\
  2023-08-01 21:40:18 +0200
  * [MDEV-31822](https://jira.mariadb.org/browse/MDEV-31822) ALTER TABLE ENGINE=x started failing instead of producing warning on unsupported TRANSACTIONAL=1
* [Revision #da09ae05a9](https://github.com/MariaDB/server/commit/da09ae05a9)\
  2023-07-13 10:59:39 +0200
  * [MDEV-18114](https://jira.mariadb.org/browse/MDEV-18114) Foreign Key Constraint actions don't affect Virtual Column
* [Revision #ab1191c039](https://github.com/MariaDB/server/commit/ab1191c039)\
  2023-07-13 10:23:11 +0200
  * cleanup: key->key\_create\_info.check\_for\_duplicate\_indexes -> key->old
* [Revision #0c9794d022](https://github.com/MariaDB/server/commit/0c9794d022)\
  2023-06-29 18:03:54 +0200
  * cleanup: Item\_field::check\_vcol\_func\_processor()
* [Revision #b8233b38da](https://github.com/MariaDB/server/commit/b8233b38da)\
  2023-06-29 16:24:50 +0200
  * cleanup: put db/table\_name into Alter\_info
* [Revision #2f6d464fec](https://github.com/MariaDB/server/commit/2f6d464fec)\
  2023-07-11 14:25:12 +0200
  * cleanup: reorder enum\_fk\_option
* [Revision #f7a9f446d7](https://github.com/MariaDB/server/commit/f7a9f446d7)\
  2023-07-10 22:25:52 +0200
  * cleanup: remove unused keyinfo flag
* [Revision #383baa812e](https://github.com/MariaDB/server/commit/383baa812e)\
  2023-07-13 11:26:15 +0200
  * cleanup: invert return code
* [Revision #010f535b7f](https://github.com/MariaDB/server/commit/010f535b7f)\
  2023-07-13 11:24:52 +0200
  * cleanup: remove redundant arguments
* [Revision #bf5cc31d4c](https://github.com/MariaDB/server/commit/bf5cc31d4c)\
  2023-06-29 12:54:52 +0200
  * cleanup: cosmetic changes
* Merge [Revision #65405308a1](https://github.com/MariaDB/server/commit/65405308a1) 2023-08-01 08:15:42 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #4235c133ae](https://github.com/MariaDB/server/commit/4235c133ae) 2023-07-31 10:14:46 +0200 - Merge branch '10.4' into 10.5
* [Revision #055f2e308b](https://github.com/MariaDB/server/commit/055f2e308b)\
  2023-07-28 23:06:58 +0200
  * Fix of4cb0d43ac63761174a39cea892c176b9cfa6edfc after merge in 10.5
* [Revision #7f9468795d](https://github.com/MariaDB/server/commit/7f9468795d)\
  2023-07-28 15:35:06 +0200
  * galera: two tests are returned to the disabled list
* [Revision #f3bbf8666e](https://github.com/MariaDB/server/commit/f3bbf8666e)\
  2023-07-28 11:27:16 +0300
  * [MDEV-31790](https://jira.mariadb.org/browse/MDEV-31790) work-around: Add not\_msan.inc
* [Revision #35533dc0b3](https://github.com/MariaDB/server/commit/35533dc0b3)\
  2023-07-27 14:21:35 +0300
  * [MDEV-29727](https://jira.mariadb.org/browse/MDEV-29727) ALTER and CREATE with default partitioning differently react to SQL\_MODE => unusable SHOW CREATE
* Merge [Revision #f291c3df2c](https://github.com/MariaDB/server/commit/f291c3df2c) 2023-07-27 13:12:30 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #7564be1352](https://github.com/MariaDB/server/commit/7564be1352) 2023-07-26 13:54:59 +0200 - Merge branch '10.4' into 10.5
* [Revision #5da492c354](https://github.com/MariaDB/server/commit/5da492c354)\
  2023-07-21 12:09:15 +0200
  * switch off it for masan also
* Merge [Revision #f52954ef42](https://github.com/MariaDB/server/commit/f52954ef42) 2023-07-20 11:54:52 +0200 - Merge commit '10.4' into 10.5
* [Revision #f17a865c39](https://github.com/MariaDB/server/commit/f17a865c39)\
  2023-07-19 15:59:33 +1100
  * [MDEV-30710](https://jira.mariadb.org/browse/MDEV-30710) Incorrect operator when comparing large unsigned integers.
* [Revision #1a5c4c2d9b](https://github.com/MariaDB/server/commit/1a5c4c2d9b)\
  2023-07-18 11:02:18 +0400
  * [MDEV-26186](https://jira.mariadb.org/browse/MDEV-26186) 280 Bytes lost in mysys/array.c, mysys/hash.c, sql/sp.cc, sql/sp.cc, sql/item\_create.cc, sql/item\_create.cc, sql/sql\_yacc.yy:10748 when using oracle sql\_mode
* [Revision #68403eeda3](https://github.com/MariaDB/server/commit/68403eeda3)\
  2023-07-17 13:33:19 +0400
  * [MDEV-27207](https://jira.mariadb.org/browse/MDEV-27207) Assertion \`!m\_null\_value' failed in int FixedBinTypeBundle::cmp\_item\_fbt::compare or in cmp\_item\_inet6::compare
* [Revision #400c101332](https://github.com/MariaDB/server/commit/400c101332)\
  2023-07-14 12:14:56 +0400
  * [MDEV-30662](https://jira.mariadb.org/browse/MDEV-30662) SQL/PL package body does not appear in I\_S.ROUTINES.ROUTINE\_DEFINITION
* [Revision #9808ebe195](https://github.com/MariaDB/server/commit/9808ebe195)\
  2023-06-23 15:06:53 -0600
  * [MDEV-30978](https://jira.mariadb.org/browse/MDEV-30978): On slave XA COMMIT/XA ROLLBACK fail to return an error in read-only mode
* [Revision #29bc61912e](https://github.com/MariaDB/server/commit/29bc61912e)\
  2023-07-05 23:27:17 +0400
  * A cleanup for [MDEV-31578](https://jira.mariadb.org/browse/MDEV-31578) DECLARE CURSOR: "Memory not freed: 280 bytes lost" on syntax error
* [Revision #bd7908e6ac](https://github.com/MariaDB/server/commit/bd7908e6ac)\
  2023-07-05 15:15:04 +0300
  * [MDEV-31568](https://jira.mariadb.org/browse/MDEV-31568) InnoDB protection against dual processes accessing data insufficient
* [Revision #5f2a77cef1](https://github.com/MariaDB/server/commit/5f2a77cef1)\
  2023-06-10 08:35:58 +1000
  * [MDEV-31268](https://jira.mariadb.org/browse/MDEV-31268) Fedora MariaDB-shared replaces mariadb-connector-c
* [Revision #fdab2c4c64](https://github.com/MariaDB/server/commit/fdab2c4c64)\
  2023-06-29 17:30:02 +0400
  * [MDEV-31578](https://jira.mariadb.org/browse/MDEV-31578) DECLARE CURSOR: "Memory not freed: 280 bytes lost" on syntax error
* [Revision #0d3720c12a](https://github.com/MariaDB/server/commit/0d3720c12a)\
  2023-05-15 12:41:31 +0400
  * [MDEV-30680](https://jira.mariadb.org/browse/MDEV-30680) Warning: Memory not freed: 280 on mangled query, LeakSanitizer: detected memory leaks
* [Revision #33877cfeae](https://github.com/MariaDB/server/commit/33877cfeae)\
  2023-06-28 17:07:00 +0300
  * Fix WITH\_UBSAN GCC -Wconversion
* [Revision #24faa5de16](https://github.com/MariaDB/server/commit/24faa5de16)\
  2023-06-28 12:22:56 +1000
  * [MDEV-30542](https://jira.mariadb.org/browse/MDEV-30542) Fixing spider/bugfix.self\_reference\_multi
* [Revision #84dbd0253d](https://github.com/MariaDB/server/commit/84dbd0253d)\
  2023-06-27 09:12:38 +0300
  * [MDEV-31487](https://jira.mariadb.org/browse/MDEV-31487): Recovery or backup failure after innodb\_undo\_log\_truncate=ON
* [Revision #0b61f4e0e4](https://github.com/MariaDB/server/commit/0b61f4e0e4)\
  2023-06-19 21:42:16 +0300
  * Fix comment
* [Revision #bd076d4dff](https://github.com/MariaDB/server/commit/bd076d4dff)\
  2023-06-12 16:10:39 +0530
  * [MDEV-31442](https://jira.mariadb.org/browse/MDEV-31442) page\_cleaner thread aborts while releasing the tablespace
* [Revision #f7e9ac0d88](https://github.com/MariaDB/server/commit/f7e9ac0d88)\
  2023-06-12 15:58:55 +0300
  * [MDEV-31449](https://jira.mariadb.org/browse/MDEV-31449): Assertion s->table->opt\_range\_condition\_rows <= s->found\_records
* [Revision #0e2e70c4c1](https://github.com/MariaDB/server/commit/0e2e70c4c1)\
  2023-06-14 13:55:35 +0300
  * [MDEV-31479](https://jira.mariadb.org/browse/MDEV-31479): Inconsistency between MRR and SQL layer costs can cause poor query plan
* [Revision #841e905f20](https://github.com/MariaDB/server/commit/841e905f20)\
  2023-06-09 17:56:04 +0530
  * [MDEV-31442](https://jira.mariadb.org/browse/MDEV-31442) page\_cleaner thread aborts while releasing the tablespace
* [Revision #b3074128a6](https://github.com/MariaDB/server/commit/b3074128a6)\
  2023-06-08 11:13:10 +0300
  * [MDEV-31380](https://jira.mariadb.org/browse/MDEV-31380) post-fix: fix group\_min\_max.test with embedded and view-protocol
* [Revision #d3eefbaa55](https://github.com/MariaDB/server/commit/d3eefbaa55)\
  2023-06-08 10:40:48 +0300
  * [MDEV-31355](https://jira.mariadb.org/browse/MDEV-31355) fixup: Adjust one more test
* [Revision #21031b24fc](https://github.com/MariaDB/server/commit/21031b24fc)\
  2023-06-08 09:38:03 +0300
  * Suppress an occasional buffer pool warning
* [Revision #c25b496724](https://github.com/MariaDB/server/commit/c25b496724)\
  2023-06-08 09:18:21 +0300
  * [MDEV-31382](https://jira.mariadb.org/browse/MDEV-31382) SET GLOBAL innodb\_undo\_log\_truncate=ON has no effect on logically empty undo logs
* [Revision #3e40f9a7f3](https://github.com/MariaDB/server/commit/3e40f9a7f3)\
  2023-06-08 09:17:52 +0300
  * [MDEV-31355](https://jira.mariadb.org/browse/MDEV-31355) innodb\_undo\_log\_truncate=ON fails to wait for purge of enough transaction history
* Merge [Revision #609b4e997a](https://github.com/MariaDB/server/commit/609b4e997a) 2023-06-07 15:31:55 +0300 - Merge mariadb-10.5.21 into 10.5
* [Revision #91367e82f1](https://github.com/MariaDB/server/commit/91367e82f1)\
  2023-06-07 08:10:48 -0400
  * bump the VERSION
* [Revision #a0e7bd735b](https://github.com/MariaDB/server/commit/a0e7bd735b)\
  2023-06-01 14:06:06 +0300
  * [MDEV-31380](https://jira.mariadb.org/browse/MDEV-31380): Assertion \`s->table->opt\_range\_condition\_rows <= s->found\_records' failed
* [Revision #bb9da13baf](https://github.com/MariaDB/server/commit/bb9da13baf)\
  2023-06-01 12:11:18 +0300
  * [MDEV-31373](https://jira.mariadb.org/browse/MDEV-31373) innodb\_undo\_log\_truncate=ON recovery results in a corrupted undo log
* [Revision #3aea77edeb](https://github.com/MariaDB/server/commit/3aea77edeb)\
  2023-06-01 09:41:17 +0300
  * [MDEV-31347](https://jira.mariadb.org/browse/MDEV-31347) fil\_ibd\_create() may hijack the file handle of an old file
* Merge [Revision #383105dae1](https://github.com/MariaDB/server/commit/383105dae1) 2023-05-24 08:28:20 +0300 - Merge bb-10.5-release into 10.5
* [Revision #c5cf94b2dc](https://github.com/MariaDB/server/commit/c5cf94b2dc)\
  2023-05-24 08:25:26 +0300
  * [MDEV-31234](https://jira.mariadb.org/browse/MDEV-31234) fixup: Free some UNDO pages earlier
* [Revision #9c35f9c9c1](https://github.com/MariaDB/server/commit/9c35f9c9c1)\
  2023-05-23 12:20:27 +0300
  * [MDEV-31234](https://jira.mariadb.org/browse/MDEV-31234) fixup: Allow innodb\_undo\_log\_truncate=ON after upgrade
* [Revision #a7adfd4c52](https://github.com/MariaDB/server/commit/a7adfd4c52)\
  2023-05-23 10:02:33 +0300
  * Optimized version of safe\_strcpy()
* [Revision #92d2ceac73](https://github.com/MariaDB/server/commit/92d2ceac73)\
  2023-05-22 18:58:45 +0300
  * [MDEV-28285](https://jira.mariadb.org/browse/MDEV-28285) Unexpected result when combining DISTINCT, subselect and LIMIT
* [Revision #cd37e49422](https://github.com/MariaDB/server/commit/cd37e49422)\
  2023-04-20 14:12:48 +0300
  * [MDEV-31083](https://jira.mariadb.org/browse/MDEV-31083) ASAN use-after-poison in myrg\_attach\_children
* [Revision #c7e04af8bc](https://github.com/MariaDB/server/commit/c7e04af8bc)\
  2023-04-18 14:56:07 +0300
  * Update main.selectivity test and results
* [Revision #6a0314063d](https://github.com/MariaDB/server/commit/6a0314063d)\
  2023-04-18 11:21:06 +0300
  * Make install.db read only in mtr
* [Revision #16258677b3](https://github.com/MariaDB/server/commit/16258677b3)\
  2023-03-31 19:35:04 +0300
  * [MDEV-6768](https://jira.mariadb.org/browse/MDEV-6768) Wrong result with aggregate with join with no result set
* [Revision #c0adb05b30](https://github.com/MariaDB/server/commit/c0adb05b30)\
  2023-05-15 09:07:43 +1000
  * [MDEV-31268](https://jira.mariadb.org/browse/MDEV-31268): Fedora mariadb-connector-c-config conflicts with MariaDB's MariaDB-common
* [Revision #3f59bbeeae](https://github.com/MariaDB/server/commit/3f59bbeeae)\
  2023-04-17 16:04:01 +0300
  * [MDEV-29293](https://jira.mariadb.org/browse/MDEV-29293) MariaDB stuck on starting commit state
* [Revision #03d4fd3214](https://github.com/MariaDB/server/commit/03d4fd3214)\
  2023-01-27 23:10:47 +0000
  * Backport GitLab CI to 10.5
* [Revision #5422784792](https://github.com/MariaDB/server/commit/5422784792)\
  2023-05-12 17:20:03 +0300
  * [MDEV-31256](https://jira.mariadb.org/browse/MDEV-31256) fil\_node\_open\_file() releases fil\_system.mutex allowing other thread to open its file node
* Merge [Revision #06d555a41a](https://github.com/MariaDB/server/commit/06d555a41a) 2023-05-19 14:23:04 +0300 - Merge bb-10.5-release into 10.5
* [Revision #e0084b9d31](https://github.com/MariaDB/server/commit/e0084b9d31)\
  2023-05-19 12:19:26 +0300
  * [MDEV-31234](https://jira.mariadb.org/browse/MDEV-31234) InnoDB does not free UNDO after the fix of [MDEV-30671](https://jira.mariadb.org/browse/MDEV-30671)
* [Revision #caeff13579](https://github.com/MariaDB/server/commit/caeff13579)\
  2023-05-15 23:32:30 -0700
  * Remove CODEOWNERS as obsolete
* [Revision #c9eff1a144](https://github.com/MariaDB/server/commit/c9eff1a144)\
  2023-05-12 15:04:50 +0300
  * [MDEV-31254](https://jira.mariadb.org/browse/MDEV-31254) InnoDB: Trying to read doublewrite buffer page
* [Revision #477285c8ea](https://github.com/MariaDB/server/commit/477285c8ea)\
  2023-05-12 14:57:14 +0300
  * [MDEV-31253](https://jira.mariadb.org/browse/MDEV-31253) Freed data pages are not always being scrubbed
* [Revision #279d0120f5](https://github.com/MariaDB/server/commit/279d0120f5)\
  2023-05-11 13:21:57 +0300
  * [MDEV-29967](https://jira.mariadb.org/browse/MDEV-29967) innodb\_read\_ahead\_threshold (linear read-ahead) does not work
* Merge [Revision #d4dd634529](https://github.com/MariaDB/server/commit/d4dd634529) 2023-05-11 09:09:16 +0300 - Merge mariadb-10.5.20 into 10.5
* [Revision #0d8b0493ee](https://github.com/MariaDB/server/commit/0d8b0493ee)\
  2023-05-10 08:43:49 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
