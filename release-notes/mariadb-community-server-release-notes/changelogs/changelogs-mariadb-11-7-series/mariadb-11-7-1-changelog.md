# MariaDB 11.7.1 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md)[Changelog](mariadb-11-7-1-changelog.md)[Overview of 11.7](../../old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.7.1/)

**Release date:** 21 Nov 2024

For the highlights of this release, see the[release notes](../../old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Changes from [11.7.0](../../old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-0-release-notes.md) are also included in this changelog
* Includes all fixes from [MariaDB 11.6.2](../changelogs-mariadb-11-6-series/mariadb-11-6-2-changelog.md)
* [Revision #74331a48dd](https://github.com/MariaDB/server/commit/74331a48dd)\
  2024-11-10 15:49:31 +0100
  * bump the VERSION
* [Revision #2ac98bcb3c](https://github.com/MariaDB/server/commit/2ac98bcb3c)\
  2024-11-10 15:45:16 +0100
  * [MDEV-35354](https://jira.mariadb.org/browse/MDEV-35354) fix the test for --embedded
* Merge [Revision #b12ff287ec](https://github.com/MariaDB/server/commit/b12ff287ec) 2024-11-09 19:01:12 +0100 - Merge branch '11.6' into 11.7
* [Revision #7aa28a2a54](https://github.com/MariaDB/server/commit/7aa28a2a54)\
  2024-11-07 06:15:18 -0800
  * [MDEV-35354](https://jira.mariadb.org/browse/MDEV-35354) InnoDB: Failing assertion: node->pcur->rel\_pos == BTR\_PCUR\_ON upon LOAD DATA REPLACE with unique blob
* [Revision #f24ebbaa5c](https://github.com/MariaDB/server/commit/f24ebbaa5c)\
  2024-11-07 06:07:54 -0800
  * cleanup: main.loaddata\_autocom\_innodb
* [Revision #ebbbe9d960](https://github.com/MariaDB/server/commit/ebbbe9d960)\
  2024-11-04 04:25:31 -0800
  * [MDEV-35319](https://jira.mariadb.org/browse/MDEV-35319) ER\_LOCK\_DEADLOCK not detected upon DML on table with vector key, server crashes
* [Revision #574e18f80d](https://github.com/MariaDB/server/commit/574e18f80d)\
  2024-11-01 13:31:48 +0100
  * [MDEV-35308](https://jira.mariadb.org/browse/MDEV-35308) NO\_KEY\_OPTIONS SQL mode has no effect on engine key options
* [Revision #e5a5d2b78d](https://github.com/MariaDB/server/commit/e5a5d2b78d)\
  2024-10-31 22:38:06 +0100
  * [MDEV-35214](https://jira.mariadb.org/browse/MDEV-35214) Server crashes in FVectorNode::gref\_len with insufficient mhnsw\_max\_cache\_size
* [Revision #cbc2812f80](https://github.com/MariaDB/server/commit/cbc2812f80)\
  2024-10-31 08:37:23 +0100
  * [MDEV-35287](https://jira.mariadb.org/browse/MDEV-35287) ER\_KEY\_NOT\_FOUND upon INSERT into InnoDB table with vector key under READ COMMITTED
* [Revision #ad33ffc0b5](https://github.com/MariaDB/server/commit/ad33ffc0b5)\
  2024-10-30 21:50:29 +0100
  * [MDEV-35296](https://jira.mariadb.org/browse/MDEV-35296) DESC does not work in ORDER BY with vector key
* [Revision #7feec30939](https://github.com/MariaDB/server/commit/7feec30939)\
  2024-10-30 10:03:18 +0100
  * relax the XA recovery error
* [Revision #b09c8b03d7](https://github.com/MariaDB/server/commit/b09c8b03d7)\
  2024-10-29 17:53:38 +0100
  * [MDEV-35244](https://jira.mariadb.org/browse/MDEV-35244) Vector-related system variables could use better names
* [Revision #784becf3e1](https://github.com/MariaDB/server/commit/784becf3e1)\
  2024-10-29 09:44:24 +0100
  * [MDEV-35267](https://jira.mariadb.org/browse/MDEV-35267) Server crashes in \_ma\_reset\_history upon altering on Aria table with vector key under lock
* [Revision #5d9ebef41e](https://github.com/MariaDB/server/commit/5d9ebef41e)\
  2024-10-26 13:38:45 +0200
  * [MDEV-35258](https://jira.mariadb.org/browse/MDEV-35258) mariadb-backup does not work with MyISAM tables with vector keys
* [Revision #0b9bc6c3cd](https://github.com/MariaDB/server/commit/0b9bc6c3cd)\
  2024-10-25 21:38:08 +0200
  * [MDEV-35246](https://jira.mariadb.org/browse/MDEV-35246) Vector search skips a row in the table
* [Revision #d50663198c](https://github.com/MariaDB/server/commit/d50663198c)\
  2024-09-10 16:55:02 +0400
  * DDL recovery for high-level indexes
* [Revision #883fb66cd4](https://github.com/MariaDB/server/commit/883fb66cd4)\
  2024-10-23 23:04:56 +0400
  * [MDEV-35130](https://jira.mariadb.org/browse/MDEV-35130) Assertion fails in trx\_t::check\_bulk\_buffer upon CREATE.. SELECT with vector key
* [Revision #f6de9a379a](https://github.com/MariaDB/server/commit/f6de9a379a)\
  2024-10-25 15:58:06 +0200
  * [MDEV-34919](https://jira.mariadb.org/browse/MDEV-34919) post-fix
* [Revision #1cc7ef52e3](https://github.com/MariaDB/server/commit/1cc7ef52e3)\
  2024-10-10 16:49:39 +0400
  * [MDEV-34919](https://jira.mariadb.org/browse/MDEV-34919) Aria crashes with high-level (vector) indexes
* [Revision #72839c1435](https://github.com/MariaDB/server/commit/72839c1435)\
  2024-10-24 14:32:35 +0200
  * [MDEV-35245](https://jira.mariadb.org/browse/MDEV-35245) SHOW CREATE TABLE produces unusable statement for vector fields with constant default value
* [Revision #053bd80d43](https://github.com/MariaDB/server/commit/053bd80d43)\
  2024-10-23 20:56:12 +0200
  * [MDEV-35230](https://jira.mariadb.org/browse/MDEV-35230) ASAN errors upon reading from joined temptable views with vector type
* [Revision #7d081c1b83](https://github.com/MariaDB/server/commit/7d081c1b83)\
  2024-10-23 20:08:57 +0200
  * [MDEV-35223](https://jira.mariadb.org/browse/MDEV-35223) REPAIR does not fix MyISAM table with vector key after crash recovery
* [Revision #e8cff8e829](https://github.com/MariaDB/server/commit/e8cff8e829)\
  2024-10-23 17:23:30 +0200
  * [MDEV-35219](https://jira.mariadb.org/browse/MDEV-35219) Unexpected ER\_DUP\_KEY after OPTIMIZE on MyISAM table with vector key
* [Revision #8988decbfe](https://github.com/MariaDB/server/commit/8988decbfe)\
  2024-10-23 17:07:17 +0200
  * [MDEV-35220](https://jira.mariadb.org/browse/MDEV-35220) Assertion \`!item->null\_value' failed upon VEC\_TOTEXT call
* [Revision #14364b09b9](https://github.com/MariaDB/server/commit/14364b09b9)\
  2024-10-23 14:25:11 +0200
  * [MDEV-35236](https://jira.mariadb.org/browse/MDEV-35236) Assertion \`(mem\_root->flags & 4) == 0' failed in safe\_lexcstrdup\_root
* [Revision #1a53048299](https://github.com/MariaDB/server/commit/1a53048299)\
  2024-10-20 16:47:20 +0200
  * [MDEV-35215](https://jira.mariadb.org/browse/MDEV-35215) ASAN errors in Item\_func\_vec\_fromtext::val\_str upon VEC\_FROMTEXT with an invalid argument
* [Revision #96eb66e5b3](https://github.com/MariaDB/server/commit/96eb66e5b3)\
  2024-10-20 12:38:09 +0200
  * [MDEV-35205](https://jira.mariadb.org/browse/MDEV-35205) Server crash in online alter upon concurrent ALTER and DML on table with vector field
* [Revision #e020a3a2ce](https://github.com/MariaDB/server/commit/e020a3a2ce)\
  2024-10-20 00:15:27 +0200
  * [MDEV-35210](https://jira.mariadb.org/browse/MDEV-35210) Vector type cannot store values which VEC\_FromText produces and VEC\_ToText accepts
* [Revision #f336b10bb1](https://github.com/MariaDB/server/commit/f336b10bb1)\
  2024-10-19 21:08:11 +0200
  * [MDEV-35212](https://jira.mariadb.org/browse/MDEV-35212) Server crashes in Item\_func\_vec\_fromtext::val\_str upon query from empty table
* [Revision #2bec721316](https://github.com/MariaDB/server/commit/2bec721316)\
  2024-10-19 20:08:28 +0200
  * [MDEV-35203](https://jira.mariadb.org/browse/MDEV-35203) ASAN errors or assertion failures in row\_sel\_convert\_mysql\_key\_to\_innobase upon query from table with usual key on vector field
* [Revision #2e74a00d9d](https://github.com/MariaDB/server/commit/2e74a00d9d)\
  2024-10-19 20:05:17 +0200
  * [MDEV-35195](https://jira.mariadb.org/browse/MDEV-35195) Assertion \`tab->join->order' fails upon vector search with DISTINCT #2
* [Revision #926b339b93](https://github.com/MariaDB/server/commit/926b339b93)\
  2024-10-19 20:33:57 +0200
  * [MDEV-35194](https://jira.mariadb.org/browse/MDEV-35194) non-BNL join fails on assertion
* [Revision #597e34d000](https://github.com/MariaDB/server/commit/597e34d000)\
  2024-10-20 12:53:27 +0200
  * [MDEV-35213](https://jira.mariadb.org/browse/MDEV-35213) Server crash or assertion failure upon query with high value of mhnsw\_min\_limit
* [Revision #dd9a5dd5b5](https://github.com/MariaDB/server/commit/dd9a5dd5b5)\
  2024-10-19 14:19:57 +0200
  * [MDEV-35204](https://jira.mariadb.org/browse/MDEV-35204) mysqlbinlog --verbose fails on row events with vector type
* [Revision #ed9fec0266](https://github.com/MariaDB/server/commit/ed9fec0266)\
  2024-10-17 18:39:21 +0200
  * [MDEV-35177](https://jira.mariadb.org/browse/MDEV-35177) Unexpected ER\_TRUNCATED\_WRONG\_VALUE\_FOR\_FIELD, diagnostics area assertion failures upon EITS collection with vector type
* [Revision #db10e5cf6c](https://github.com/MariaDB/server/commit/db10e5cf6c)\
  2024-10-16 17:41:56 +0200
  * [MDEV-35160](https://jira.mariadb.org/browse/MDEV-35160) RBR does not work with vector type, ER\_SLAVE\_CONVERSION\_FAILED
* [Revision #8f49fb8cc3](https://github.com/MariaDB/server/commit/8f49fb8cc3)\
  2024-10-18 17:31:28 +0200
  * [MDEV-35191](https://jira.mariadb.org/browse/MDEV-35191) Assertion failure in Create\_tmp\_table::finalize upon DISTINCT with vector type
* [Revision #cfbf065893](https://github.com/MariaDB/server/commit/cfbf065893)\
  2024-10-17 15:27:45 +0200
  * [MDEV-35176](https://jira.mariadb.org/browse/MDEV-35176) ASAN errors in Field\_vector::store with optimizer\_trace enabled
* [Revision #425aa95655](https://github.com/MariaDB/server/commit/425aa95655)\
  2024-10-17 09:37:11 +0200
  * [MDEV-35178](https://jira.mariadb.org/browse/MDEV-35178) Assertion failure in Field\_vector::store upon INSERT IGNORE with a wrong data
* [Revision #88adcbf35a](https://github.com/MariaDB/server/commit/88adcbf35a)\
  2024-10-29 12:11:41 +0100
  * [MDEV-35182](https://jira.mariadb.org/browse/MDEV-35182) crash in online\_alter\_end\_trans with XA over vector indexes
* [Revision #5bde23990b](https://github.com/MariaDB/server/commit/5bde23990b)\
  2024-10-16 13:10:28 +0200
  * [MDEV-35159](https://jira.mariadb.org/browse/MDEV-35159) Assertion \`tab->join->select\_limit < (\~ (ha\_rows) 0)' fails upon forcing vector key
* [Revision #a83afd8537](https://github.com/MariaDB/server/commit/a83afd8537)\
  2024-10-15 23:00:44 +0200
  * cleanup: remove String::append\_float
* [Revision #88119addff](https://github.com/MariaDB/server/commit/88119addff)\
  2024-10-15 19:05:18 +0200
  * Vec\_ToText was underestimating max\_length of the result
* [Revision #91720da9be](https://github.com/MariaDB/server/commit/91720da9be)\
  2024-10-15 18:58:50 +0200
  * [MDEV-35158](https://jira.mariadb.org/browse/MDEV-35158) Assertion \`res->length() > 0 && res->length() % 4 == 0' fails upon increasing length of vector column
* [Revision #6634c88480](https://github.com/MariaDB/server/commit/6634c88480)\
  2024-10-15 18:00:01 +0200
  * [MDEV-35150](https://jira.mariadb.org/browse/MDEV-35150) Column containing non-vector tables can be modified to VECTOR type without warnings
* [Revision #ca28761066](https://github.com/MariaDB/server/commit/ca28761066)\
  2024-10-15 17:36:08 +0200
  * [MDEV-35147](https://jira.mariadb.org/browse/MDEV-35147) Inconsistent NULL handling in vector type
* [Revision #f274cf1c25](https://github.com/MariaDB/server/commit/f274cf1c25)\
  2024-10-15 14:48:44 +0200
  * [MDEV-35141](https://jira.mariadb.org/browse/MDEV-35141) Server crashes in Field\_vector::report\_wrong\_value upon statistic collection
* [Revision #78119d1ae5](https://github.com/MariaDB/server/commit/78119d1ae5)\
  2024-10-13 14:15:25 +0200
  * [MDEV-33410](https://jira.mariadb.org/browse/MDEV-33410) VECTOR data type
* [Revision #b56ca29f89](https://github.com/MariaDB/server/commit/b56ca29f89)\
  2024-10-09 09:25:12 +0200
  * [MDEV-35105](https://jira.mariadb.org/browse/MDEV-35105) Assertion \`tab->join->order' fails upon vector search with DISTINCT
* [Revision #9ddb94f60e](https://github.com/MariaDB/server/commit/9ddb94f60e)\
  2024-10-08 22:57:10 +0200
  * [MDEV-35104](https://jira.mariadb.org/browse/MDEV-35104) Invalid (old?) table or database name upon DDL on table with vector key and unique key
* [Revision #7d9c0e4f62](https://github.com/MariaDB/server/commit/7d9c0e4f62)\
  2024-10-08 14:56:35 +0200
  * [MDEV-35092](https://jira.mariadb.org/browse/MDEV-35092) Server crash, hang or ASAN errors in mysql\_create\_frm\_image upon using non-default table options and system variables
* [Revision #cdc7253787](https://github.com/MariaDB/server/commit/cdc7253787)\
  2024-10-06 20:09:08 +0200
  * make MyISAM and Aria report correct reflength to the server
* [Revision #ea1e720391](https://github.com/MariaDB/server/commit/ea1e720391)\
  2024-10-06 11:55:54 +0200
  * [MDEV-35078](https://jira.mariadb.org/browse/MDEV-35078) Server crash or ASAN errors in mhnsw\_insert
* [Revision #855aefb7b5](https://github.com/MariaDB/server/commit/855aefb7b5)\
  2024-10-04 14:31:49 +0200
  * mysqldump and mariadb-backup tests of vector indexes
* [Revision #eb4ab2ce8f](https://github.com/MariaDB/server/commit/eb4ab2ce8f)\
  2024-10-02 20:33:42 +0200
  * [MDEV-35061](https://jira.mariadb.org/browse/MDEV-35061) XA PREPARE "not supported by the engine" from storage engine mhnsw, memory leak
* [Revision #09cd817f5d](https://github.com/MariaDB/server/commit/09cd817f5d)\
  2024-10-02 17:34:51 +0200
  * [MDEV-35060](https://jira.mariadb.org/browse/MDEV-35060) Assertion failure upon DML on table with vector under lock
* [Revision #09889d417b](https://github.com/MariaDB/server/commit/09889d417b)\
  2024-10-01 16:01:38 +0200
  * [MDEV-35055](https://jira.mariadb.org/browse/MDEV-35055) ASAN errors in TABLE\_SHARE::lock\_share upon committing transaction after FLUSH on table with vector key
* [Revision #d396fb9226](https://github.com/MariaDB/server/commit/d396fb9226)\
  2024-09-30 22:59:47 +0200
  * [MDEV-35021](https://jira.mariadb.org/browse/MDEV-35021) Behavior for RTREE indexes changed, assertion fails
* [Revision #b3afd9f640](https://github.com/MariaDB/server/commit/b3afd9f640)\
  2024-09-30 22:17:47 +0200
  * [MDEV-35042](https://jira.mariadb.org/browse/MDEV-35042) Vector indexes are allowed for MERGE tables, but do not
* [Revision #0932c3a27e](https://github.com/MariaDB/server/commit/0932c3a27e)\
  2024-09-30 19:22:30 +0200
  * [MDEV-35044](https://jira.mariadb.org/browse/MDEV-35044) ALTER on a table with vector index attempts to bypass unsupported locking limitation, server crashes in THD::free\_tmp\_table\_share
* [Revision #824a63852b](https://github.com/MariaDB/server/commit/824a63852b)\
  2024-09-30 19:12:31 +0200
  * [MDEV-35043](https://jira.mariadb.org/browse/MDEV-35043) Unsuitable error upon an attempt to create MEMORY table with vector key
* [Revision #9f80e3fbb7](https://github.com/MariaDB/server/commit/9f80e3fbb7)\
  2024-09-26 19:33:13 +0200
  * [MDEV-35032](https://jira.mariadb.org/browse/MDEV-35032) streaming mode for mhnsw search
* [Revision #b4811a9b63](https://github.com/MariaDB/server/commit/b4811a9b63)\
  2024-09-27 21:10:53 +0200
  * cleanup: simplify search\_layer() usage, remove std::swap()
* [Revision #7b00e2351b](https://github.com/MariaDB/server/commit/7b00e2351b)\
  2024-09-26 19:52:12 +0200
  * rename MHNSW\_Context->MHNSW\_Share
* [Revision #be69716287](https://github.com/MariaDB/server/commit/be69716287)\
  2024-09-29 15:46:28 +0200
  * [MDEV-35029](https://jira.mariadb.org/browse/MDEV-35029) ASAN errors in Lex\_ident\<Compare\_ident\_ci>::is\_valid\_ident upon DDL on table with vector index
* [Revision #a6499049af](https://github.com/MariaDB/server/commit/a6499049af)\
  2024-09-29 14:09:26 +0200
  * [MDEV-35033](https://jira.mariadb.org/browse/MDEV-35033) LeakSanitizer errors in my\_malloc / safe\_mutex\_lazy\_init\_deadlock\_detection / MHNSW\_Context::alloc\_node and alike
* [Revision #6837bb54f4](https://github.com/MariaDB/server/commit/6837bb54f4)\
  2024-09-29 12:36:00 +0200
  * [MDEV-35020](https://jira.mariadb.org/browse/MDEV-35020) After a failed attempt to create vector index temporary file remains and prevents further operation
* [Revision #ec2ff9f2a0](https://github.com/MariaDB/server/commit/ec2ff9f2a0)\
  2024-09-29 10:49:01 +0200
  * [MDEV-35035](https://jira.mariadb.org/browse/MDEV-35035) Assertion failure in ha\_blackhole::position upon INSERT into blackhole table with vector index
* [Revision #b44cde16cb](https://github.com/MariaDB/server/commit/b44cde16cb)\
  2024-09-29 10:33:06 +0200
  * [MDEV-35037](https://jira.mariadb.org/browse/MDEV-35037) Invalid (old?) table or database name 't#i#00' upon creating RocksDB table with vector index
* [Revision #8ac3f0b1d4](https://github.com/MariaDB/server/commit/8ac3f0b1d4)\
  2024-09-29 10:27:33 +0200
  * [MDEV-35038](https://jira.mariadb.org/browse/MDEV-35038) Server crash in Index\_statistics::get\_avg\_frequency upon EITS collection for vector index
* [Revision #0bd01f4a95](https://github.com/MariaDB/server/commit/0bd01f4a95)\
  2024-09-28 23:07:48 +0200
  * [MDEV-35039](https://jira.mariadb.org/browse/MDEV-35039) Number of indexes inside InnoDB differs from that defined in MariaDB after altering table with vector key
* [Revision #8253650aaa](https://github.com/MariaDB/server/commit/8253650aaa)\
  2024-09-25 20:22:17 +0200
  * [MDEV-35006](https://jira.mariadb.org/browse/MDEV-35006) Using varbinary as vector-storing column results in assertion failures
* [Revision #a471389d07](https://github.com/MariaDB/server/commit/a471389d07)\
  2024-09-21 11:57:19 +0200
  * [MDEV-34970](https://jira.mariadb.org/browse/MDEV-34970) Vector search fails to compile on s390x
* [Revision #3c6e836110](https://github.com/MariaDB/server/commit/3c6e836110)\
  2024-09-06 22:12:35 +0200
  * generous\_furthest optimization
* [Revision #fb04cad37e](https://github.com/MariaDB/server/commit/fb04cad37e)\
  2024-09-14 11:55:53 +0200
  * trying to stabilize floating-point tests
* [Revision #f867c2a21e](https://github.com/MariaDB/server/commit/f867c2a21e)\
  2024-09-13 11:44:35 +0400
  * Disabled high-level indexes with Aria
* [Revision #97b2392ede](https://github.com/MariaDB/server/commit/97b2392ede)\
  2024-09-10 14:31:26 +0200
  * cleanup: TABLE\_SHARE::lock\_share() helper
* [Revision #3283688797](https://github.com/MariaDB/server/commit/3283688797)\
  2024-09-01 17:43:46 +0400
  * Simplified quick\_rm\_table() and mysql\_rename\_table()
* [Revision #ca17b68bb6](https://github.com/MariaDB/server/commit/ca17b68bb6)\
  2024-08-27 22:25:34 +0400
  * ALTER TABLE fixes for high-level indexes (iii)
* [Revision #7aa6bb3aa3](https://github.com/MariaDB/server/commit/7aa6bb3aa3)\
  2024-08-26 12:56:43 +0400
  * ALTER TABLE fixes for high-level indexes (ii)
* [Revision #a90fa3f397](https://github.com/MariaDB/server/commit/a90fa3f397)\
  2024-08-12 13:27:48 +0400
  * ALTER TABLE fixes for high-level indexes (i)
* [Revision #e826875fe5](https://github.com/MariaDB/server/commit/e826875fe5)\
  2024-08-15 23:11:23 +0200
  * AVX-512 support
* [Revision #2ad9df8c9b](https://github.com/MariaDB/server/commit/2ad9df8c9b)\
  2024-08-29 20:49:54 +0200
  * VEC\_Distance\_Cosine()
* [Revision #2e1fcc6a80](https://github.com/MariaDB/server/commit/2e1fcc6a80)\
  2024-08-29 15:27:59 +0200
  * rename VEC\_Distance to VEC\_Distance\_Euclidean
* [Revision #0da820cb12](https://github.com/MariaDB/server/commit/0da820cb12)\
  2024-08-24 15:09:51 +0200
  * mhnsw: use plugin index options and transaction\_participant API
* [Revision #ea4562ef21](https://github.com/MariaDB/server/commit/ea4562ef21)\
  2024-08-27 15:10:06 +0200
  * cleanup: index options don't need hton anymore
* [Revision #aed5928207](https://github.com/MariaDB/server/commit/aed5928207)\
  2024-09-11 19:32:38 +0200
  * cleanup: extract transaction-related part of handlerton
* [Revision #126d6d787c](https://github.com/MariaDB/server/commit/126d6d787c)\
  2024-08-25 14:07:44 +0200
  * cleanup: handlerton
* [Revision #8087cefc07](https://github.com/MariaDB/server/commit/8087cefc07)\
  2024-07-25 22:28:30 +0200
  * make rename test to work with InnoDB too
* [Revision #445198c10e](https://github.com/MariaDB/server/commit/445198c10e)\
  2024-07-25 22:14:59 +0200
  * pos-fixes for rename
* [Revision #97e112fb82](https://github.com/MariaDB/server/commit/97e112fb82)\
  2024-07-15 21:47:19 +0400
  * VECTOR indexes support for RENAME TABLE
* [Revision #ebcbed6d74](https://github.com/MariaDB/server/commit/ebcbed6d74)\
  2024-07-25 20:27:50 +0200
  * post-fixes for TRUNCATE
* [Revision #70575defb7](https://github.com/MariaDB/server/commit/70575defb7)\
  2024-07-06 00:37:37 +0400
  * Fixed TRUNCATE TABLE against VECTOR indexes
* [Revision #91a24ddc5d](https://github.com/MariaDB/server/commit/91a24ddc5d)\
  2024-07-05 13:45:44 +0400
  * Test insert ... select with vector index
* [Revision #4aa1968b89](https://github.com/MariaDB/server/commit/4aa1968b89)\
  2024-07-03 19:52:53 +0400
  * Disable VECTOR indexes with partitioned tables
* [Revision #7c16bba71d](https://github.com/MariaDB/server/commit/7c16bba71d)\
  2024-07-05 14:55:45 +0400
  * CREATE TABLE ... LIKE loses VECTOR index
* [Revision #eec1339f5d](https://github.com/MariaDB/server/commit/eec1339f5d)\
  2024-07-24 22:01:53 +0300
  * [MDEV-32886](https://jira.mariadb.org/browse/MDEV-32886) Vec\_FromText and Vec\_ToText
* [Revision #f813ac2a51](https://github.com/MariaDB/server/commit/f813ac2a51)\
  2024-07-25 21:52:33 +0300
  * Introduce String::append\_float
* [Revision #26e599cd32](https://github.com/MariaDB/server/commit/26e599cd32)\
  2024-07-24 22:31:36 +0200
  * mhnsw: make the search less greedy
* [Revision #885eb19823](https://github.com/MariaDB/server/commit/885eb19823)\
  2024-07-22 21:24:11 +0200
  * cleanup search\_layer()
* [Revision #fa2078ddff](https://github.com/MariaDB/server/commit/fa2078ddff)\
  2024-07-19 12:25:25 +0200
  * mhnsw: store coordinates in 16 bits, not 32
* [Revision #f44989ff0f](https://github.com/MariaDB/server/commit/f44989ff0f)\
  2024-07-18 14:43:47 +0200
  * UPDATE/DELETE post-fixes
* [Revision #f2512c0fa8](https://github.com/MariaDB/server/commit/f2512c0fa8)\
  2024-07-18 14:40:15 +0200
  * cleanup: prepare\_for\_insert() -> prepare\_for\_modify()
* [Revision #0e2b9e7621](https://github.com/MariaDB/server/commit/0e2b9e7621)\
  2024-07-16 15:15:17 +0200
  * [MDEV-33408](https://jira.mariadb.org/browse/MDEV-33408) Initial support for vector DELETE and UPDATE
* [Revision #173b017c06](https://github.com/MariaDB/server/commit/173b017c06)\
  2024-07-14 16:02:09 +0200
  * non-SIMD fallback
* [Revision #049d839350](https://github.com/MariaDB/server/commit/049d839350)\
  2024-07-17 17:16:28 +0200
  * mhnsw: inter-statement shared cache
* [Revision #8eb39be512](https://github.com/MariaDB/server/commit/8eb39be512)\
  2024-06-13 23:24:51 +0200
  * mhnsw: change storage format
* [Revision #ca21d49042](https://github.com/MariaDB/server/commit/ca21d49042)\
  2024-06-12 17:12:20 +0200
  * mhnsw: return an error if lazy neighbor read failed
* [Revision #4657b63aa1](https://github.com/MariaDB/server/commit/4657b63aa1)\
  2024-06-06 16:39:45 +0200
  * mhnsw: SIMD for euclidean distance
* [Revision #5c2b7c6e7f](https://github.com/MariaDB/server/commit/5c2b7c6e7f)\
  2024-06-11 12:58:41 +0200
  * mhnsw: configurable parameters
* [Revision #25b4000290](https://github.com/MariaDB/server/commit/25b4000290)\
  2024-06-08 11:03:08 +0200
  * InnoDB support for hlindexes and mhnsw
* [Revision #2efd9b17ba](https://github.com/MariaDB/server/commit/2efd9b17ba)\
  2024-06-07 19:12:08 +0200
  * mhnsw: cache start node too, don't push too much in pg\_discard
* [Revision #687bfa7691](https://github.com/MariaDB/server/commit/687bfa7691)\
  2024-06-07 16:40:28 +0200
  * bugfix: properly reset db\_plugin when hlindex discovery fails
* [Revision #613542dceb](https://github.com/MariaDB/server/commit/613542dceb)\
  2024-06-07 13:50:13 +0200
  * mhnsw: build indexes with the columns of exactly right size
* [Revision #1029d2f245](https://github.com/MariaDB/server/commit/1029d2f245)\
  2024-06-07 00:31:49 +0200
  * cleanups
* [Revision #c42ec1932f](https://github.com/MariaDB/server/commit/c42ec1932f)\
  2024-06-06 15:08:02 +0200
  * mhnsw: remove EXTEND\_CANDIDATES and KEEP\_PRUNED\_CONNECTIONS
* [Revision #a8fd1199e2](https://github.com/MariaDB/server/commit/a8fd1199e2)\
  2024-06-06 14:50:17 +0200
  * mhnsw: search intermediate layers with ef=1
* [Revision #42804ad5a5](https://github.com/MariaDB/server/commit/42804ad5a5)\
  2024-06-05 17:55:24 +0200
  * mhnsw: fix the heuristic neighbor selection algorithm
* [Revision #ad94c8d714](https://github.com/MariaDB/server/commit/ad94c8d714)\
  2024-06-05 16:14:12 +0200
  * mhnsw: don't prefix blob ref array with its length
* [Revision #c91cab3b6f](https://github.com/MariaDB/server/commit/c91cab3b6f)\
  2024-06-05 14:59:25 +0200
  * mhnsw: don't create many empty layers
* [Revision #058976533f](https://github.com/MariaDB/server/commit/058976533f)\
  2024-06-05 13:31:58 +0200
  * mhnsw: remove a redundant loop and ha\_update\_row
* [Revision #e0bdddad74](https://github.com/MariaDB/server/commit/e0bdddad74)\
  2024-06-05 13:39:33 +0200
  * mhnsw: modify target's neighbors directly
* [Revision #27bfa21a58](https://github.com/MariaDB/server/commit/27bfa21a58)\
  2024-06-04 23:06:44 +0200
  * mhnsw: cache neighbors too
* [Revision #b492025c6c](https://github.com/MariaDB/server/commit/b492025c6c)\
  2024-06-05 12:12:28 +0200
  * mhnsw: don't guess whether it's insert or update
* [Revision #267092d4a1](https://github.com/MariaDB/server/commit/267092d4a1)\
  2024-06-04 14:47:52 +0200
  * mhnsw: refactor FVector\* classes
* [Revision #10de659020](https://github.com/MariaDB/server/commit/10de659020)\
  2024-06-03 15:21:57 +0200
  * mhnsw: fix memory management
* [Revision #51c8cdcbb2](https://github.com/MariaDB/server/commit/51c8cdcbb2)\
  2024-06-03 11:22:21 +0200
  * mhnsw: simplify memory management of returned results
* [Revision #3ff7f04fd4](https://github.com/MariaDB/server/commit/3ff7f04fd4)\
  2024-06-01 00:17:05 +0200
  * misc changes
* [Revision #88839e71a3](https://github.com/MariaDB/server/commit/88839e71a3)\
  2024-02-17 17:03:30 +0200
  * Initial HNSW implementation
* [Revision #26e5654301](https://github.com/MariaDB/server/commit/26e5654301)\
  2024-05-29 21:12:23 +0200
  * cleanup: simplify Queue<>, add const
* [Revision #553815ea24](https://github.com/MariaDB/server/commit/553815ea24)\
  2024-07-12 10:38:48 +0200
  * cleanup: C++11 range-based for loop for Hash\_set<>
* [Revision #d6add9a03d](https://github.com/MariaDB/server/commit/d6add9a03d)\
  2024-01-17 15:32:45 +0100
  * initial support for vector indexes
* [Revision #9ccf02a9a7](https://github.com/MariaDB/server/commit/9ccf02a9a7)\
  2023-11-25 14:58:06 +0100
  * [MDEV-32885](https://jira.mariadb.org/browse/MDEV-32885) VEC\_DISTANCE() function
* [Revision #08a7f18b19](https://github.com/MariaDB/server/commit/08a7f18b19)\
  2024-07-18 14:43:06 +0200
  * cleanup: init\_tmp\_table\_share(bool thread\_specific)
* [Revision #44c6328cbb](https://github.com/MariaDB/server/commit/44c6328cbb)\
  2024-06-01 16:15:53 +0200
  * cleanup: thd->alloc<>() and thd->calloc<>()
* [Revision #eff16d7593](https://github.com/MariaDB/server/commit/eff16d7593)\
  2024-02-09 23:50:26 +0100
  * Revert "[MDEV-15458](https://jira.mariadb.org/browse/MDEV-15458) Segfault in heap\_scan() upon UPDATE after ADD SYSTEM VERSIONING"
* [Revision #07ec1a9e37](https://github.com/MariaDB/server/commit/07ec1a9e37)\
  2024-01-26 12:19:47 +0100
  * cleanup: unused function argument
* [Revision #aa09cb3b11](https://github.com/MariaDB/server/commit/aa09cb3b11)\
  2024-01-27 00:15:40 +0100
  * open frm for DROP TABLE
* [Revision #c1b4f3a32c](https://github.com/MariaDB/server/commit/c1b4f3a32c)\
  2024-01-25 17:29:32 +0100
  * cleanup: extract ha\_create\_table\_from\_share()
* [Revision #1fe8a1bb76](https://github.com/MariaDB/server/commit/1fe8a1bb76)\
  2024-01-25 11:36:59 +0100
  * cleanup: generalize ER\_INNODB\_NO\_FT\_TEMP\_TABLE
* [Revision #fd69abe44f](https://github.com/MariaDB/server/commit/fd69abe44f)\
  2024-01-17 15:48:53 +0100
  * cleanup: generalize ER\_SPATIAL\_CANT\_HAVE\_NULL
* [Revision #356baeea4b](https://github.com/MariaDB/server/commit/356baeea4b)\
  2024-01-18 01:30:12 +0100
  * cleanup: make\_long\_hash\_field\_name() and add\_hash\_field()
* [Revision #062f8eb37d](https://github.com/MariaDB/server/commit/062f8eb37d)\
  2024-01-14 11:43:43 +0100
  * cleanup: key algorithm vs key flags
* [Revision #f5e9c4e9ef](https://github.com/MariaDB/server/commit/f5e9c4e9ef)\
  2024-02-07 00:15:45 +0100
  * cleanup: Queue and Bounded\_queue
* [Revision #ae59127158](https://github.com/MariaDB/server/commit/ae59127158)\
  2024-01-27 09:31:44 +0100
  * cleanup: lex\_string\_set3()
* [Revision #32e6f8ff2e](https://github.com/MariaDB/server/commit/32e6f8ff2e)\
  2024-01-10 20:31:43 +0100
  * cleanup: remove unconditional #ifdef's
* [Revision #570daecf49](https://github.com/MariaDB/server/commit/570daecf49)\
  2024-06-15 23:11:11 +0200
  * cleanup: const in List::push\_front()
* [Revision #44ff2f7831](https://github.com/MariaDB/server/commit/44ff2f7831)\
  2024-01-08 19:33:32 +0100
  * reject invalid spatial key declarations in the parser
* [Revision #0cc01bde45](https://github.com/MariaDB/server/commit/0cc01bde45)\
  2024-01-26 16:05:38 +0100
  * cleanup: pass TABLE\_SHARE to store\_key\_options()
* [Revision #949fed514a](https://github.com/MariaDB/server/commit/949fed514a)\
  2024-09-25 14:39:29 +0200
  * cleanup: get\_float convenience helper
* [Revision #115d3e050c](https://github.com/MariaDB/server/commit/115d3e050c)\
  2024-10-06 12:28:54 +0200
  * cleanup: engine\_option\_value::Value::find\_in\_list() helper
* [Revision #d046aca0c7](https://github.com/MariaDB/server/commit/d046aca0c7)\
  2024-08-30 11:04:14 +0200
  * cleanup: CREATE\_TYPELIB\_FOR() helper
* [Revision #9fa31c1bd9](https://github.com/MariaDB/server/commit/9fa31c1bd9)\
  2024-01-08 18:29:12 +0100
  * cleanup: spaces, casts, comments
* [Revision #9f2adffcca](https://github.com/MariaDB/server/commit/9f2adffcca)\
  2024-09-26 11:52:05 +0200
  * memroot improvement: fix savepoint support
* [Revision #4f4c5a2ba9](https://github.com/MariaDB/server/commit/4f4c5a2ba9)\
  2024-08-26 19:27:45 +0200
  * fix a typo and an old bug in prefschema.transaction test
* [Revision #70f000f1dc](https://github.com/MariaDB/server/commit/70f000f1dc)\
  2024-02-05 16:29:32 +0100
  * fix main.plugin\_vars test to cleanup after itself
* [Revision #9ddac64188](https://github.com/MariaDB/server/commit/9ddac64188)\
  2024-01-19 16:21:25 +0100
  * make INFORMATION\_SCHEMA.STATISTICS.COMMENT not nullable
* [Revision #680bdb76a6](https://github.com/MariaDB/server/commit/680bdb76a6)\
  2024-11-02 11:34:35 +0100
  * fix for 32bit
* [Revision #a914087fab](https://github.com/MariaDB/server/commit/a914087fab)\
  2024-11-02 18:25:10 +0700
  * [MDEV-35307](https://jira.mariadb.org/browse/MDEV-35307) Unexpected error WARN\_SORTING\_ON\_TRUNCATED\_LENGTH or assertion failure in diagnostics area #2
* [Revision #a4cb03ec56](https://github.com/MariaDB/server/commit/a4cb03ec56)\
  2024-11-05 09:14:06 +0400
  * Adding a comment near the keyword NOCOPY
* [Revision #5d4a4d2091](https://github.com/MariaDB/server/commit/5d4a4d2091)\
  2024-11-02 10:27:48 +0400
  * Fixing main.type\_timestamp failure with --view
* [Revision #ac7fe8b214](https://github.com/MariaDB/server/commit/ac7fe8b214)\
  2024-11-01 21:01:31 +0100
  * fix main.selectivity\_notembedded --view
* [Revision #0a3452cf83](https://github.com/MariaDB/server/commit/0a3452cf83)\
  2024-11-01 20:52:58 +0100
  * [MDEV-35229](https://jira.mariadb.org/browse/MDEV-35229) fix the test for --view
* [Revision #947de4b1db](https://github.com/MariaDB/server/commit/947de4b1db)\
  2024-09-11 22:55:14 +0200
  * print more digits for floating point options in mariadbd --help
* [Revision #40810baffe](https://github.com/MariaDB/server/commit/40810baffe)\
  2023-12-31 12:41:25 +0200
  * [MDEV-33144](https://jira.mariadb.org/browse/MDEV-33144) Implement the Percona variable slow\_query\_log\_always\_write\_time
* [Revision #bf9662f6fa](https://github.com/MariaDB/server/commit/bf9662f6fa)\
  2024-10-29 21:36:09 +0700
  * [MDEV-35275](https://jira.mariadb.org/browse/MDEV-35275) Unexpected WARN\_SORTING\_ON\_TRUNCATED\_LENGTH or assertion failure in diagnostics area
* [Revision #556a40dce0](https://github.com/MariaDB/server/commit/556a40dce0)\
  2024-10-29 09:52:42 +0400
  * [MDEV-35229](https://jira.mariadb.org/browse/MDEV-35229) NOCOPY has become reserved word bringing wide incompatibility
* [Revision #8c0a260a5b](https://github.com/MariaDB/server/commit/8c0a260a5b)\
  2024-10-27 14:07:59 +0400
  * [MDEV-35250](https://jira.mariadb.org/browse/MDEV-35250) Assertion \`dec <= 6' failed in my\_timestamp\_binary\_length
* [Revision #a79f314f1b](https://github.com/MariaDB/server/commit/a79f314f1b)\
  2024-10-29 14:22:59 +0400
  * [MDEV-34817](https://jira.mariadb.org/browse/MDEV-34817) perfschema.lowercase\_fs\_off fails on buildbot
* [Revision #cc183489da](https://github.com/MariaDB/server/commit/cc183489da)\
  2024-10-29 14:18:38 +0300
  * [MDEV-27293](https://jira.mariadb.org/browse/MDEV-27293) Allow converting a versioned table from implicit to explicit row\_start/row\_end columns
* [Revision #5e5c3c7cb6](https://github.com/MariaDB/server/commit/5e5c3c7cb6)\
  2024-09-12 11:54:24 +0200
  * post-merge changes
* [Revision #2fe269fdcb](https://github.com/MariaDB/server/commit/2fe269fdcb)\
  2024-02-28 19:09:58 +0100
  * [MDEV-32637](https://jira.mariadb.org/browse/MDEV-32637) Implement native UUID7 function
* [Revision #ae69ac204a](https://github.com/MariaDB/server/commit/ae69ac204a)\
  2024-06-25 17:17:13 +1000
  * [MDEV-32583](https://jira.mariadb.org/browse/MDEV-32583) UUID() should be treated as stochastic for the purposes of forcing query materialization
* [Revision #20611c8ae7](https://github.com/MariaDB/server/commit/20611c8ae7)\
  2024-04-04 06:22:06 +0400
  * cleanup: [MDEV-11339](https://jira.mariadb.org/browse/MDEV-11339) Implement native UUID4 function
* [Revision #ef585df440](https://github.com/MariaDB/server/commit/ef585df440)\
  2024-03-21 00:20:19 +0100
  * [MDEV-11339](https://jira.mariadb.org/browse/MDEV-11339) Implement native UUID4 function
* [Revision #47dd617c7f](https://github.com/MariaDB/server/commit/47dd617c7f)\
  2024-10-29 12:15:53 +0200
  * [MDEV-35265](https://jira.mariadb.org/browse/MDEV-35265) wsrep.wsrep-recover, wsrep.wsrep-recover-v25 fail on assertion
* [Revision #4b6922a315](https://github.com/MariaDB/server/commit/4b6922a315)\
  2024-08-29 11:10:59 +1000
  * [MDEV-25008](https://jira.mariadb.org/browse/MDEV-25008): UPDATE/DELETE: Cost-based choice IN->EXISTS vs Materialization
* [Revision #fd87e01f38](https://github.com/MariaDB/server/commit/fd87e01f38)\
  2023-09-04 13:15:06 +0700
  * [MDEV-27277](https://jira.mariadb.org/browse/MDEV-27277) Add a warning when max\_sort\_length is reached
* [Revision #0d17c540a5](https://github.com/MariaDB/server/commit/0d17c540a5)\
  2024-08-17 12:56:28 +0400
  * [MDEV-27277](https://jira.mariadb.org/browse/MDEV-27277) Add a warning when max\_sort\_length is reached
* [Revision #e1cd3c4033](https://github.com/MariaDB/server/commit/e1cd3c4033)\
  2023-09-25 21:48:01 +0400
  * [MDEV-12252](https://jira.mariadb.org/browse/MDEV-12252) ROW data type for stored function return values
* [Revision #dfaf7e2eb4](https://github.com/MariaDB/server/commit/dfaf7e2eb4)\
  2024-08-26 13:24:59 +0400
  * [MDEV-15751](https://jira.mariadb.org/browse/MDEV-15751) CURRENT\_TIMESTAMP should return a TIMESTAMP \[WITH TIME ZONE?]
* [Revision #128fc34990](https://github.com/MariaDB/server/commit/128fc34990)\
  2024-10-18 14:05:29 +0200
  * fix rdiff files in sys\_var suite
* [Revision #15a291e4e0](https://github.com/MariaDB/server/commit/15a291e4e0)\
  2024-10-18 13:58:37 +0200
  * [MDEV-14978](https://jira.mariadb.org/browse/MDEV-14978) fix client.client-env-variable test
* [Revision #a812dba6dc](https://github.com/MariaDB/server/commit/a812dba6dc)\
  2024-08-11 21:27:50 -0700
  * [MDEV-20153](https://jira.mariadb.org/browse/MDEV-20153): Slave error message incorrectly mentions server\_uuid
* [Revision #e213e916ad](https://github.com/MariaDB/server/commit/e213e916ad)\
  2024-10-17 15:52:41 -0600
  * [MDEV-32014](https://jira.mariadb.org/browse/MDEV-32014): Fix mysqld--help,win.rdiff
* [Revision #39cce39ae1](https://github.com/MariaDB/server/commit/39cce39ae1)\
  2024-10-13 14:24:05 -0600
  * [MDEV-32014](https://jira.mariadb.org/browse/MDEV-32014): typo fix in test
* [Revision #70aa713f58](https://github.com/MariaDB/server/commit/70aa713f58)\
  2024-09-14 21:26:55 +0200
  * [MDEV-32014](https://jira.mariadb.org/browse/MDEV-32014) test fix
* [Revision #7a7c338a0b](https://github.com/MariaDB/server/commit/7a7c338a0b)\
  2024-09-16 07:33:46 -0600
  * [MDEV-34930](https://jira.mariadb.org/browse/MDEV-34930): [MDEV-32014](https://jira.mariadb.org/browse/MDEV-32014) Galera and SST/no binlog fixes
* [Revision #3ebe317f9b](https://github.com/MariaDB/server/commit/3ebe317f9b)\
  2024-09-12 14:19:33 -0600
  * [MDEV-32014](https://jira.mariadb.org/browse/MDEV-32014): Reduce min val of large\_commit\_threshold for debug builds
* [Revision #72cc58bb71](https://github.com/MariaDB/server/commit/72cc58bb71)\
  2024-09-05 00:16:35 +0800
  * [MDEV-32014](https://jira.mariadb.org/browse/MDEV-32014) Rename binlog cache temporary file to binlog file for large transaction
* [Revision #35cebfdc51](https://github.com/MariaDB/server/commit/35cebfdc51)\
  2024-08-12 17:01:14 +1000
  * [MDEV-15696](https://jira.mariadb.org/browse/MDEV-15696) Implement SHOW CREATE SERVER
* [Revision #d2eba35653](https://github.com/MariaDB/server/commit/d2eba35653)\
  2024-09-05 16:12:35 +1000
  * [MDEV-34716](https://jira.mariadb.org/browse/MDEV-34716) Allow arbitrary options in CREATE SERVER
* [Revision #2345407b8c](https://github.com/MariaDB/server/commit/2345407b8c)\
  2024-08-07 17:27:15 +1000
  * [MDEV-34716](https://jira.mariadb.org/browse/MDEV-34716) Fix mysql.servers socket max length too short
* [Revision #84df8d7275](https://github.com/MariaDB/server/commit/84df8d7275)\
  2024-08-07 13:27:44 +1000
  * [MDEV-34716](https://jira.mariadb.org/browse/MDEV-34716) spider: some trivial cleanups and documentation
* [Revision #13cd8ad8db](https://github.com/MariaDB/server/commit/13cd8ad8db)\
  2019-06-27 02:16:33 +0400
  * json\_get\_object\_nkey() function implemented.
* [Revision #9315452ea0](https://github.com/MariaDB/server/commit/9315452ea0)\
  2024-09-17 15:42:55 +1100
  * [MDEV-34941](https://jira.mariadb.org/browse/MDEV-34941) [MDEV-31466](https://jira.mariadb.org/browse/MDEV-31466)-fix column count issue with union in derived table
* [Revision #e90aab7acc](https://github.com/MariaDB/server/commit/e90aab7acc)\
  2024-09-16 12:58:33 +1100
  * [MDEV-34931](https://jira.mariadb.org/browse/MDEV-34931) [MDEV-31466](https://jira.mariadb.org/browse/MDEV-31466) name resolution fails in --view
* [Revision #10008b3d3e](https://github.com/MariaDB/server/commit/10008b3d3e)\
  2024-08-23 14:55:46 +1100
  * [MDEV-31466](https://jira.mariadb.org/browse/MDEV-31466) Add optional correlation column list for derived tables
* [Revision #4016c905cb](https://github.com/MariaDB/server/commit/4016c905cb)\
  2024-07-22 20:27:51 +0000
  * Update mini-benchmark to use constant transactions
* [Revision #fd0cc2b1fd](https://github.com/MariaDB/server/commit/fd0cc2b1fd)\
  2023-12-13 23:30:18 +0000
  * Make SESSION\_USER() comparable with CURRENT\_USER()
* [Revision #eedbb901e5](https://github.com/MariaDB/server/commit/eedbb901e5)\
  2024-07-15 18:54:55 +0000
  * \[[MDEV-14978](https://jira.mariadb.org/browse/MDEV-14978)] Client programs to use $MARIADB\_HOST consistently
* [Revision #383d1f90dd](https://github.com/MariaDB/server/commit/383d1f90dd)\
  2024-09-30 11:27:45 +0800
  * The revision corresponds to the review comments. 1. Move the unit tests into the compat/oracle suite, sp-param.test file. 2. Remove the added unit test file and result file. 3. Add type, Alter\_info::enum\_alter\_table\_algorithm, into the union. 4. Remove the extra switch case
* [Revision #fa5eeb4931](https://github.com/MariaDB/server/commit/fa5eeb4931)\
  2024-09-13 19:10:56 +0800
  * Fixed ALTER TABLE NOCOPY keyword failure
* [Revision #43825af101](https://github.com/MariaDB/server/commit/43825af101)\
  2024-09-09 17:52:52 +0800
  * [MDEV-34316](https://jira.mariadb.org/browse/MDEV-34316) sql\_mode=ORACLE: Ignore the NOCOPY keyword in stored routine parameters
* Merge [Revision #f493e46494](https://github.com/MariaDB/server/commit/f493e46494) 2024-10-03 18:15:13 +0300 - Merge 11.6 into 11.7
* [Revision #8478a06cdb](https://github.com/MariaDB/server/commit/8478a06cdb)\
  2024-07-26 10:15:50 +0300
  * [MDEV-34380](https://jira.mariadb.org/browse/MDEV-34380): Set optimizer\_switch='cset\_narrowing=on' by default
* [Revision #fe3432b3bd](https://github.com/MariaDB/server/commit/fe3432b3bd)\
  2024-09-10 14:48:59 +1000
  * [MDEV-28009](https://jira.mariadb.org/browse/MDEV-28009) Deprecate spider\_table\_crd\_thread\_count and spider\_table\_sts\_thread\_count
* [Revision #5bbda97111](https://github.com/MariaDB/server/commit/5bbda97111)\
  2024-06-11 22:59:31 +0800
  * [MDEV-33853](https://jira.mariadb.org/browse/MDEV-33853) Async rollback prepared transactions during binlog crash recovery
* [Revision #db5d1cde45](https://github.com/MariaDB/server/commit/db5d1cde45)\
  2024-08-31 01:34:52 +0200
  * [MDEV-34857](https://jira.mariadb.org/browse/MDEV-34857): Implement --slave-abort-blocking-timeout
* Merge [Revision #669d8ffe2f](https://github.com/MariaDB/server/commit/669d8ffe2f) 2024-09-04 10:49:15 +0300 - Merge 11.6 into main
* [Revision #9811d23b6d](https://github.com/MariaDB/server/commit/9811d23b6d)\
  2024-07-11 11:53:03 -0600
  * [MDEV-33756](https://jira.mariadb.org/browse/MDEV-33756): Deprecate binlog\_optimize\_thread\_scheduling
* [Revision #e6df06d40d](https://github.com/MariaDB/server/commit/e6df06d40d)\
  2024-08-27 13:40:39 +0100
  * Update markdown files for `main` branch
* [Revision #7a65dcb59e](https://github.com/MariaDB/server/commit/7a65dcb59e)\
  2024-08-05 16:16:09 +0200
  * [MDEV-34704](https://jira.mariadb.org/browse/MDEV-34704) Quick mode produces the bug for mariadb client
* Merge [Revision #cb5bb4b319](https://github.com/MariaDB/server/commit/cb5bb4b319) 2024-08-21 15:26:07 +0200 - Merge branch '11.6' into 11.7
* [Revision #9adc81791e](https://github.com/MariaDB/server/commit/9adc81791e)\
  2024-08-20 08:41:24 +0200
  * 11.7 branch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
