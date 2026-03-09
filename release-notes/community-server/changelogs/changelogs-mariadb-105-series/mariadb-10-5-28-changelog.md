# MariaDB 10.5.28 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.5/10.5.28.md)[Changelog](mariadb-10-5-28-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

**Release date:** 4 Feb 2025

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.28.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.34](../changelogs-mariadb-10-4-series/mariadb-10-4-34-changelog.md)
* [Revision #7eded23be6](https://github.com/MariaDB/server/commit/7eded23be6)\
  2025-01-23 13:22:12 +0100
  * ColumnStore 5.6.9-1
* [Revision #1fec4fc4f8](https://github.com/MariaDB/server/commit/1fec4fc4f8)\
  2022-11-14 20:46:42 +0100
  * more C API methods in the service\_sql
* [Revision #ffff702623](https://github.com/MariaDB/server/commit/ffff702623)\
  2025-01-23 12:14:31 +0100
  * C/C 3.1.27
* [Revision #fafa10dbc4](https://github.com/MariaDB/server/commit/fafa10dbc4)\
  2025-01-23 12:21:32 +0100
  * update HeidiSQL to 12.10
* [Revision #66cf3c6974](https://github.com/MariaDB/server/commit/66cf3c6974)\
  2025-01-25 14:57:16 +0100
  * [MDEV-35612](https://jira.mariadb.org/browse/MDEV-35612) fix for system-versioning
* [Revision #c1933b46e4](https://github.com/MariaDB/server/commit/c1933b46e4)\
  2025-01-25 09:51:20 +0100
  * [MDEV-33285](https://jira.mariadb.org/browse/MDEV-33285) make the test deterministic
* [Revision #caec03cb79](https://github.com/MariaDB/server/commit/caec03cb79)\
  2025-01-23 23:32:02 +0100
  * [MDEV-35907](https://jira.mariadb.org/browse/MDEV-35907) debian-start script fails when using non-standard socket path
* [Revision #9a0ac0cdf7](https://github.com/MariaDB/server/commit/9a0ac0cdf7)\
  2025-01-24 13:48:12 +0100
  * [MDEV-35911](https://jira.mariadb.org/browse/MDEV-35911) Assertion \`marked\_for\_write\_or\_computed()' failed in bool Field\_new\_decimal::store\_value(const my\_decimal\*, int\*)
* [Revision #b8b77177c2](https://github.com/MariaDB/server/commit/b8b77177c2)\
  2025-01-24 08:21:48 -0500
  * [MDEV-35964](https://jira.mariadb.org/browse/MDEV-35964) fix cast warnings on mac in mysql\_file.h
* [Revision #bcb87f5ccb](https://github.com/MariaDB/server/commit/bcb87f5ccb)\
  2025-01-27 23:07:23 +0100
  * fix for galera\_query\_cache\_invalidate test results
* [Revision #0018df2b55](https://github.com/MariaDB/server/commit/0018df2b55)\
  2023-12-05 01:40:57 +0100
  * galera fix: Assertion `WSREP(thd)` failed in wsrep\_restore\_kill\_after\_commit()
* [Revision #50d49493db](https://github.com/MariaDB/server/commit/50d49493db)\
  2024-03-06 03:40:37 +0100
  * galera: fixes for mtr test for performance schema
* [Revision #c43db43a7c](https://github.com/MariaDB/server/commit/c43db43a7c)\
  2024-02-22 09:17:29 +0100
  * MENT-2038 Assert WSREP(thd) fails in wsrep\_restore\_kill\_after\_commit
* [Revision #479a5832f0](https://github.com/MariaDB/server/commit/479a5832f0)\
  2024-08-28 04:12:10 +0200
  * galera fix: MSAN reports use-of-uninitialized-value on binlog\_encryption
* [Revision #862d1be2e6](https://github.com/MariaDB/server/commit/862d1be2e6)\
  2025-01-26 05:26:26 +0100
  * [MDEV-25718](https://jira.mariadb.org/browse/MDEV-25718) addendum: stabilization of test success (especially for 11.4+)
* [Revision #779ae4c511](https://github.com/MariaDB/server/commit/779ae4c511)\
  2025-01-25 21:01:58 +0100
  * wsrep mtr tests: fix for [MDEV-23081](https://jira.mariadb.org/browse/MDEV-23081) failure
* [Revision #331975c5c5](https://github.com/MariaDB/server/commit/331975c5c5)\
  2025-01-25 19:38:41 +0100
  * galera: disable problematic test (galera\_nbo\_master\_non\_prim\_failure)
* [Revision #5af1f69a84](https://github.com/MariaDB/server/commit/5af1f69a84)\
  2025-01-25 16:53:47 +0100
  * [MDEV-26266](https://jira.mariadb.org/browse/MDEV-26266) addendum: more stable test
* [Revision #0a5d6cf478](https://github.com/MariaDB/server/commit/0a5d6cf478)\
  2025-01-25 12:43:12 +0100
  * galera: disable problematic test (galera\_sequences)
* [Revision #acf7b000ff](https://github.com/MariaDB/server/commit/acf7b000ff)\
  2025-01-24 19:31:00 +0100
  * fixes for galera\_as\_slave replication tests
* [Revision #e53ffdee96](https://github.com/MariaDB/server/commit/e53ffdee96)\
  2024-12-19 15:03:10 +0200
  * [MDEV-35804](https://jira.mariadb.org/browse/MDEV-35804) : galera\_ddl\_fk\_conflict test failed due to timeout
* [Revision #2cfad396ee](https://github.com/MariaDB/server/commit/2cfad396ee)\
  2025-01-24 02:22:01 +0100
  * galera tests: more informative messages about the number of variables
* [Revision #0ddaefcc76](https://github.com/MariaDB/server/commit/0ddaefcc76)\
  2024-11-20 16:17:50 +0200
  * galera fix : MW-402 galera test fails sporadically
* [Revision #6e3274e814](https://github.com/MariaDB/server/commit/6e3274e814)\
  2024-11-19 14:16:48 +0200
  * MENT-31857 post-fix: fix for timeouts in the galera\_as\_slave\_ctas test
* [Revision #c0b11e75ff](https://github.com/MariaDB/server/commit/c0b11e75ff)\
  2025-01-08 13:22:46 +0530
  * [MDEV-34218](https://jira.mariadb.org/browse/MDEV-34218): Mariadb Galera cluster fails when replicating from Mysql 5.7 on use of DDL
* [Revision #746471b8d8](https://github.com/MariaDB/server/commit/746471b8d8)\
  2025-01-27 12:11:47 +0200
  * [MDEV-33978](https://jira.mariadb.org/browse/MDEV-33978) P\_S.THREADS is not showing all server threads
* [Revision #dffe3d1fb2](https://github.com/MariaDB/server/commit/dffe3d1fb2)\
  2025-01-26 20:39:38 -0800
  * [MDEV-35910](https://jira.mariadb.org/browse/MDEV-35910) Conditions with SP local variables are not pushed into derived table
* [Revision #765458c93c](https://github.com/MariaDB/server/commit/765458c93c)\
  2020-11-17 04:59:41 +0100
  * fix my\_error usage
* [Revision #e7cc1a3047](https://github.com/MariaDB/server/commit/e7cc1a3047)\
  2024-10-13 19:28:51 +0200
  * [MDEV-33658](https://jira.mariadb.org/browse/MDEV-33658) 2/2 Cannot add a foreign key on a table with a matching long UNIQUE
* [Revision #ecaedbe299](https://github.com/MariaDB/server/commit/ecaedbe299)\
  2024-10-12 21:32:18 +0200
  * [MDEV-33658](https://jira.mariadb.org/browse/MDEV-33658) 1/2 Refactoring: extract Key length initialization
* [Revision #e33064e0fc](https://github.com/MariaDB/server/commit/e33064e0fc)\
  2025-01-16 01:44:06 +0100
  * [MDEV-27769](https://jira.mariadb.org/browse/MDEV-27769) Assertion failed in Field::ptr\_in\_record upon UPDATE in ORACLE mode
* [Revision #cb5dd76959](https://github.com/MariaDB/server/commit/cb5dd76959)\
  2025-01-25 09:58:56 -0700
  * [MDEV-35938](https://jira.mariadb.org/browse/MDEV-35938): rpl.rpl\_parallel\_gco\_wait\_kill fails - "Can't initialize replace ..."
* [Revision #47f87c5f88](https://github.com/MariaDB/server/commit/47f87c5f88)\
  2025-01-24 17:08:04 +0100
  * [MDEV-20281](https://jira.mariadb.org/browse/MDEV-20281) "\[ERROR] Failed to write to mysql.slow\_log:" without error reason
* [Revision #d598ee3cf9](https://github.com/MariaDB/server/commit/d598ee3cf9)\
  2024-09-26 08:43:45 +0300
  * [MDEV-32780](https://jira.mariadb.org/browse/MDEV-32780) : galera\_as\_slave\_replay: assertion in the wsrep::transaction::before\_rollback()
* [Revision #552cba92de](https://github.com/MariaDB/server/commit/552cba92de)\
  2024-12-31 08:04:15 +0200
  * [MDEV-35710](https://jira.mariadb.org/browse/MDEV-35710) support for threadpool
* [Revision #50cf189717](https://github.com/MariaDB/server/commit/50cf189717)\
  2025-01-24 16:59:46 +0100
  * [MDEV-35018](https://jira.mariadb.org/browse/MDEV-35018) addendum: improved warnings handling
* [Revision #841a7d391b](https://github.com/MariaDB/server/commit/841a7d391b)\
  2024-09-26 16:07:13 +0200
  * [MDEV-35018](https://jira.mariadb.org/browse/MDEV-35018) MDL BF-BF conflict on DROP TABLE
* [Revision #40a23e08e6](https://github.com/MariaDB/server/commit/40a23e08e6)\
  2025-01-24 12:07:42 +0100
  * WolfSSL - make it compilable also with older versions of Windows SDK.
* [Revision #73f415c955](https://github.com/MariaDB/server/commit/73f415c955)\
  2025-01-21 12:26:51 +0700
  * [MDEV-24935](https://jira.mariadb.org/browse/MDEV-24935): Server crashes in Field\_iterator\_natural\_join::next or Field\_iterator\_table\_ref::set\_field\_iterator upon 2nd execution of SP
* [Revision #d261fa5c70](https://github.com/MariaDB/server/commit/d261fa5c70)\
  2024-11-08 13:51:34 +0400
  * [MDEV-30111](https://jira.mariadb.org/browse/MDEV-30111) InnoDB: Failing assertion: update->n\_fields == 0 in row\_ins\_sec\_index\_entry\_by\_modify
* [Revision #77ea99a4b5](https://github.com/MariaDB/server/commit/77ea99a4b5)\
  2025-01-23 13:48:00 -0800
  * [MDEV-35869](https://jira.mariadb.org/browse/MDEV-35869) Wrong result using degenerated subquery with window function
* [Revision #136e866119](https://github.com/MariaDB/server/commit/136e866119)\
  2025-01-23 00:03:04 +0100
  * Update WolfSSL to the latest release 5.7.6
* [Revision #b214ca7219](https://github.com/MariaDB/server/commit/b214ca7219)\
  2025-01-23 11:29:52 +0100
  * [MDEV-35090](https://jira.mariadb.org/browse/MDEV-35090) (Item\_func\_current\_user) Assertion \`typeid(\*copy) == typeid(\*this)' failed in Item\_func\_or\_sum::do\_build\_clone
* [Revision #82310f926b](https://github.com/MariaDB/server/commit/82310f926b)\
  2025-01-22 17:22:07 +0200
  * [MDEV-29182](https://jira.mariadb.org/browse/MDEV-29182) Assertion fld->field\_no < table->n\_v\_def failed on cascade
* [Revision #b730abda09](https://github.com/MariaDB/server/commit/b730abda09)\
  2024-11-08 18:41:05 +0400
  * [MDEV-33285](https://jira.mariadb.org/browse/MDEV-33285) - Assertion \`m\_table' failed in ha\_perfschema::rnd\_end on CHECKSUM TABLE
* [Revision #aef6f35989](https://github.com/MariaDB/server/commit/aef6f35989)\
  2025-01-22 10:53:44 +0400
  * [MDEV-35549](https://jira.mariadb.org/browse/MDEV-35549) UBSAN: runtime error: applying zero offset to null pointer on XA RECOVER
* [Revision #1f306d395d](https://github.com/MariaDB/server/commit/1f306d395d)\
  2025-01-20 17:50:29 +1100
  * [MDEV-34849](https://jira.mariadb.org/browse/MDEV-34849) Spider: update conn->queue\_connect\_share when needed
* [Revision #e3c768dc8a](https://github.com/MariaDB/server/commit/e3c768dc8a)\
  2025-01-21 10:41:20 +1100
  * [MDEV-34849](https://jira.mariadb.org/browse/MDEV-34849) Clean up spider\_check\_trx\_and\_get\_conn()
* [Revision #402b1374a7](https://github.com/MariaDB/server/commit/402b1374a7)\
  2025-01-20 13:41:53 +1100
  * [MDEV-34849](https://jira.mariadb.org/browse/MDEV-34849) Spider: do not change the first byte of a connection key
* [Revision #7358cbe627](https://github.com/MariaDB/server/commit/7358cbe627)\
  2025-01-17 18:15:04 +1100
  * [MDEV-28526](https://jira.mariadb.org/browse/MDEV-28526) Spider: remove conn\_kind member variables
* [Revision #068d061454](https://github.com/MariaDB/server/commit/068d061454)\
  2025-01-03 17:40:05 +1100
  * [MDEV-34813](https://jira.mariadb.org/browse/MDEV-34813) A simple implementation of ha\_partition::compare\_key\_parts
* [Revision #0301ef38b4](https://github.com/MariaDB/server/commit/0301ef38b4)\
  2025-01-21 18:52:33 +0530
  * [MDEV-35445](https://jira.mariadb.org/browse/MDEV-35445) Disable foreign key column nullability check for strict sql mode
* [Revision #b056ed6d98](https://github.com/MariaDB/server/commit/b056ed6d98)\
  2025-01-20 14:07:23 +0100
  * [MDEV-35891](https://jira.mariadb.org/browse/MDEV-35891) mtr, Windows - fix multi-process append for stdout and stderr
* [Revision #d32ec7d48e](https://github.com/MariaDB/server/commit/d32ec7d48e)\
  2025-01-20 12:14:46 +0100
  * [MDEV-35852](https://jira.mariadb.org/browse/MDEV-35852) : ASAN heap-use-after-free in WSREP\_DEBUG after INSERT DELAYED
* [Revision #43c36b3c88](https://github.com/MariaDB/server/commit/43c36b3c88)\
  2025-01-15 09:44:30 +0200
  * [MDEV-35852](https://jira.mariadb.org/browse/MDEV-35852) : ASAN heap-use-after-free in WSREP\_DEBUG after INSERT DELAYED
* [Revision #cbb24d9aa5](https://github.com/MariaDB/server/commit/cbb24d9aa5)\
  2025-01-16 20:57:01 -0700
  * [MDEV-35646](https://jira.mariadb.org/browse/MDEV-35646): Limit `pseudo_thread_id` to `UINT32_MAX`
* [Revision #782c4b94f0](https://github.com/MariaDB/server/commit/782c4b94f0)\
  2025-01-18 15:11:12 +0100
  * [MDEV-25654](https://jira.mariadb.org/browse/MDEV-25654) only force HA\_KEY\_ALG\_HASH for fast alter partition
* [Revision #b1f57a98a8](https://github.com/MariaDB/server/commit/b1f57a98a8)\
  2025-01-18 15:07:53 +0100
  * cleanup: Alter\_table\_ctx::Alter\_table\_ctx()
* [Revision #b87c1b06dc](https://github.com/MariaDB/server/commit/b87c1b06dc)\
  2025-01-18 08:10:49 +0100
  * [MDEV-29968](https://jira.mariadb.org/browse/MDEV-29968) update test results
* [Revision #a69da0c31e](https://github.com/MariaDB/server/commit/a69da0c31e)\
  2024-12-23 21:27:00 +0100
  * [MDEV-19761](https://jira.mariadb.org/browse/MDEV-19761) Before Trigger not processed for Not Null Columns if no explicit value and no DEFAULT
* [Revision #350cc77fee](https://github.com/MariaDB/server/commit/350cc77fee)\
  2024-11-26 13:34:28 +0400
  * [MDEV-29968](https://jira.mariadb.org/browse/MDEV-29968) Functions in default values in tables with some character sets break SHOW CREATE (and mysqldump)
* [Revision #f521b8ac21](https://github.com/MariaDB/server/commit/f521b8ac21)\
  2025-01-17 12:34:03 +0200
  * [MDEV-35723](https://jira.mariadb.org/browse/MDEV-35723): applying non-zero offset to null pointer in INSERT
* [Revision #df602ff7fa](https://github.com/MariaDB/server/commit/df602ff7fa)\
  2025-01-16 23:04:59 +0100
  * Fix main.stack on Windows
* [Revision #86b257f870](https://github.com/MariaDB/server/commit/86b257f870)\
  2025-01-16 10:35:44 -0500
  * [MDEV-35632](https://jira.mariadb.org/browse/MDEV-35632) HandlerSocket uses deprecated C++98 auto\_ptr
* [Revision #78157c4765](https://github.com/MariaDB/server/commit/78157c4765)\
  2025-01-14 17:47:08 +1100
  * [MDEV-35840](https://jira.mariadb.org/browse/MDEV-35840) Eliminate -warray-bounds triggered by TABLE\_SHARE::db\_type()
* [Revision #a5174aaffb](https://github.com/MariaDB/server/commit/a5174aaffb)\
  2025-01-14 22:42:18 +0200
  * [MDEV-35828](https://jira.mariadb.org/browse/MDEV-35828): Assertion fails in alloc\_root() when memory causes it to call itself
* [Revision #0fa1a7cc6a](https://github.com/MariaDB/server/commit/0fa1a7cc6a)\
  2025-01-13 15:40:59 +0300
  * [MDEV-28130](https://jira.mariadb.org/browse/MDEV-28130) MariaDB SEGV issue at tree\_search\_next
* [Revision #ab90eaad79](https://github.com/MariaDB/server/commit/ab90eaad79)\
  2025-01-13 15:40:59 +0300
  * [MDEV-22695](https://jira.mariadb.org/browse/MDEV-22695) Server crashes in heap\_rnext upon DELETE from a HEAP table
* [Revision #4a58d1085d](https://github.com/MariaDB/server/commit/4a58d1085d)\
  2025-01-13 15:40:59 +0300
  * [MDEV-35612](https://jira.mariadb.org/browse/MDEV-35612) EXCHANGE PARTITION does not work for tables with unique blobs
* [Revision #78c192644c](https://github.com/MariaDB/server/commit/78c192644c)\
  2025-01-13 15:40:59 +0300
  * [MDEV-35343](https://jira.mariadb.org/browse/MDEV-35343) unexpected replace behaviour when long unique index on system versioned table
* [Revision #e1e1e50bba](https://github.com/MariaDB/server/commit/e1e1e50bba)\
  2025-01-13 15:40:59 +0300
  * [MDEV-35343](https://jira.mariadb.org/browse/MDEV-35343) DML debug logging
* [Revision #e760a6dc1c](https://github.com/MariaDB/server/commit/e760a6dc1c)\
  2025-01-13 15:40:59 +0300
  * [MDEV-35343](https://jira.mariadb.org/browse/MDEV-35343) ha\_heap: recover the cursor after failed ha\_update\_row
* [Revision #0dcd30197a](https://github.com/MariaDB/server/commit/0dcd30197a)\
  2025-01-13 15:40:58 +0300
  * [MDEV-25654](https://jira.mariadb.org/browse/MDEV-25654) Unexpected ER\_CRASHED\_ON\_USAGE and Assertion \`limit >= trx\_id' failed in purge\_node\_t::skip
* [Revision #0cf2176b79](https://github.com/MariaDB/server/commit/0cf2176b79)\
  2025-01-13 15:40:58 +0300
  * [MDEV-34033](https://jira.mariadb.org/browse/MDEV-34033) Exchange partition with virtual columns fails
* [Revision #92383f8db1](https://github.com/MariaDB/server/commit/92383f8db1)\
  2025-01-13 15:40:58 +0300
  * [MDEV-26891](https://jira.mariadb.org/browse/MDEV-26891) Segfault in Field::register\_field\_in\_read\_map upon INSERT DELAYED with virtual columns
* [Revision #d8adc52863](https://github.com/MariaDB/server/commit/d8adc52863)\
  2025-01-13 15:40:58 +0300
  * [MDEV-22441](https://jira.mariadb.org/browse/MDEV-22441) SCOPE\_VALUE macro for temporary values
* [Revision #52dd489515](https://github.com/MariaDB/server/commit/52dd489515)\
  2025-01-13 15:40:58 +0300
  * [MDEV-22441](https://jira.mariadb.org/browse/MDEV-22441) implement a generic way to change a value of a variable in a scope
* [Revision #b337e14440](https://github.com/MariaDB/server/commit/b337e14440)\
  2025-01-13 15:40:58 +0300
  * WITHOUT\_ABI\_CHECK
* [Revision #200c235244](https://github.com/MariaDB/server/commit/200c235244)\
  2025-01-09 17:54:57 -0700
  * [MDEV-35429](https://jira.mariadb.org/browse/MDEV-35429) my\_snprintf fixes for 10.5+
* [Revision #6868d965db](https://github.com/MariaDB/server/commit/6868d965db)\
  2025-01-14 08:54:14 +1100
  * [MDEV-34825](https://jira.mariadb.org/browse/MDEV-34825) FreeBSD fails to build under clang natively (postfix)
* [Revision #d1f2ceee1b](https://github.com/MariaDB/server/commit/d1f2ceee1b)\
  2024-06-20 12:34:55 +0300
  * [MDEV-33064](https://jira.mariadb.org/browse/MDEV-33064): Sync trx->wsrep state from THD on trx start
* [Revision #901c6c7ab6](https://github.com/MariaDB/server/commit/901c6c7ab6)\
  2023-12-25 13:59:07 +0300
  * [MDEV-33064](https://jira.mariadb.org/browse/MDEV-33064): Sync trx->wsrep state from THD on trx start
* [Revision #4b0ac5a12b](https://github.com/MariaDB/server/commit/4b0ac5a12b)\
  2025-01-14 10:48:59 +1100
  * [MDEV-35838](https://jira.mariadb.org/browse/MDEV-35838) libressl support differences in CRYPTO\_set\_mem\_functions
* [Revision #d8c841d0d4](https://github.com/MariaDB/server/commit/d8c841d0d4)\
  2025-01-13 07:04:53 -0700
  * [MDEV-35096](https://jira.mariadb.org/browse/MDEV-35096): History is stored in different partitions on different nodes when using SYSTEM VERSION
* [Revision #133e26fd7d](https://github.com/MariaDB/server/commit/133e26fd7d)\
  2024-12-11 09:34:18 +0200
  * [MDEV-34924](https://jira.mariadb.org/browse/MDEV-34924) : gtid\_slave\_pos table neven been deleted on non replica nodes (wsrep\_gtid\_mode = 1)
* [Revision #fe2f237768](https://github.com/MariaDB/server/commit/fe2f237768)\
  2025-01-13 17:43:58 +0200
  * [MDEV-35808](https://jira.mariadb.org/browse/MDEV-35808) Test case to handle undo tablespace truncation in mariadb-backup
* [Revision #1327f40f96](https://github.com/MariaDB/server/commit/1327f40f96)\
  2025-01-13 17:51:51 +0400
  * [MDEV-35596](https://jira.mariadb.org/browse/MDEV-35596) Assertion \`type\_handler()->result\_type() == value.type\_handler()->result\_type()' failed in virtual bool Item\_param::get\_date(THD\*, MYSQL\_TIME\*, date\_mode\_t)
* [Revision #14f42e12a4](https://github.com/MariaDB/server/commit/14f42e12a4)\
  2025-01-13 16:29:11 +0400
  * [MDEV-35596](https://jira.mariadb.org/browse/MDEV-35596) Assertion \`type\_handler()->result\_type() == value.type\_handler()->result\_type()' failed in virtual bool Item\_param::get\_date(THD\*, MYSQL\_TIME\*, date\_mode\_t)
* [Revision #0d35fe6e57](https://github.com/MariaDB/server/commit/0d35fe6e57)\
  2024-12-23 22:36:01 +0100
  * [MDEV-35326](https://jira.mariadb.org/browse/MDEV-35326): Memory Leak in init\_io\_cache\_ext upon SHUTDOWN
* [Revision #f862fe8b2b](https://github.com/MariaDB/server/commit/f862fe8b2b)\
  2024-12-16 10:26:21 +1100
  * [MDEV-35641](https://jira.mariadb.org/browse/MDEV-35641) bring call to use\_all\_columns() forward when reading from mysql.servers
* [Revision #04408fff40](https://github.com/MariaDB/server/commit/04408fff40)\
  2025-01-12 13:20:56 +1100
  * [MDEV-35687](https://jira.mariadb.org/browse/MDEV-35687) Various UBSAN function-type-mismatch debug\_sync and myisam
* [Revision #6e86fe0063](https://github.com/MariaDB/server/commit/6e86fe0063)\
  2024-11-29 13:52:19 -0800
  * [MDEV-35528](https://jira.mariadb.org/browse/MDEV-35528): mariadb-binlog cannot process more than 1 logfiles when --stop-datetime is specified
* [Revision #cb26d41d81](https://github.com/MariaDB/server/commit/cb26d41d81)\
  2025-01-10 12:59:01 +1100
  * [MDEV-35735](https://jira.mariadb.org/browse/MDEV-35735): UBSAN: spider udf functions mismatch with UDF defination
* [Revision #c3fd0f189a](https://github.com/MariaDB/server/commit/c3fd0f189a)\
  2025-01-12 12:33:34 +1100
  * [MDEV-33158](https://jira.mariadb.org/browse/MDEV-33158): UBSAN - plugin.cc partial move to C++ casts
* [Revision #d7f27d7172](https://github.com/MariaDB/server/commit/d7f27d7172)\
  2025-01-09 18:15:41 +1100
  * [MDEV-33158](https://jira.mariadb.org/browse/MDEV-33158): UBSAN via MYSQL\_THDVAR\_U{INT,LONG{,LONG\}}
* [Revision #f60a8a680e](https://github.com/MariaDB/server/commit/f60a8a680e)\
  2025-01-09 17:27:29 +1100
  * [MDEV-35554](https://jira.mariadb.org/browse/MDEV-35554) runtime error: call to function show\_cached\_thread\_count()
* [Revision #82fd202fa4](https://github.com/MariaDB/server/commit/82fd202fa4)\
  2025-01-08 18:42:37 +0100
  * fix "enforce no trailing \n in Diagnostic\_area messages"
* [Revision #505b7127c9](https://github.com/MariaDB/server/commit/505b7127c9)\
  2024-12-26 17:30:11 +0700
  * [MDEV-32411](https://jira.mariadb.org/browse/MDEV-32411) Item\_sum arguments incorrectly reset to temp table fields which causes crash
* [Revision #3bbbeae792](https://github.com/MariaDB/server/commit/3bbbeae792)\
  2025-01-07 16:46:32 +0100
  * fix a memory leak
* [Revision #1d6f857534](https://github.com/MariaDB/server/commit/1d6f857534)\
  2024-12-29 16:20:19 +0100
  * [MDEV-35607](https://jira.mariadb.org/browse/MDEV-35607) Compile error with gcc-15 (signal returns)
* [Revision #3bf8b60caf](https://github.com/MariaDB/server/commit/3bf8b60caf)\
  2024-12-28 20:16:22 +0100
  * clarify the message when filesort is aborted by LIMIT ROWS EXAMINED
* [Revision #9508a44c37](https://github.com/MariaDB/server/commit/9508a44c37)\
  2024-12-28 20:15:43 +0100
  * enforce no trailing \n in Diagnostic\_area messages
* [Revision #0031f4a74f](https://github.com/MariaDB/server/commit/0031f4a74f)\
  2024-12-24 17:53:03 +0100
  * [MDEV-35663](https://jira.mariadb.org/browse/MDEV-35663) Sporadic connection failures during FLUSH PRIVILEGES
* [Revision #9f9072c344](https://github.com/MariaDB/server/commit/9f9072c344)\
  2024-12-23 21:55:02 +0100
  * [MDEV-34733](https://jira.mariadb.org/browse/MDEV-34733) main.mysqld--help-aria test failure: feedback plugin: failed to retrieve the MAC address
* [Revision #b059f60510](https://github.com/MariaDB/server/commit/b059f60510)\
  2024-12-23 17:44:24 +0100
  * [MDEV-35704](https://jira.mariadb.org/browse/MDEV-35704) Error message mispelled when altering table engine to MEMORY
* [Revision #828b928fce](https://github.com/MariaDB/server/commit/828b928fce)\
  2024-12-15 20:14:16 +0100
  * [MDEV-35651](https://jira.mariadb.org/browse/MDEV-35651) NO\_UNSIGNED\_SUBTRACTION does not work for multiple unsigned integers
* [Revision #680d461b5d](https://github.com/MariaDB/server/commit/680d461b5d)\
  2024-10-25 13:41:28 +0200
  * [MDEV-35239](https://jira.mariadb.org/browse/MDEV-35239) mariadb-backup incorrectly thinks we are on a multithreaded slave if slave\_parallel\_workers > 0
* [Revision #4e9c7031a5](https://github.com/MariaDB/server/commit/4e9c7031a5)\
  2024-12-27 13:07:04 +0100
  * [MDEV-35575](https://jira.mariadb.org/browse/MDEV-35575) Fix memory leak, when installing auth\_gssapi plugin fails.
* [Revision #a2f510fccf](https://github.com/MariaDB/server/commit/a2f510fccf)\
  2024-12-23 15:58:55 +0100
  * [MDEV-33978](https://jira.mariadb.org/browse/MDEV-33978) P\_S.THREADS is not showing all server threads
* [Revision #cc5d738999](https://github.com/MariaDB/server/commit/cc5d738999)\
  2025-01-07 12:12:24 +0200
  * Disable mmap usage in Aria and MyISAM when compiling with valgrind
* [Revision #fd9a11d8a5](https://github.com/MariaDB/server/commit/fd9a11d8a5)\
  2025-01-06 01:43:42 +0100
  * [MDEV-35749](https://jira.mariadb.org/browse/MDEV-35749): Add support for --use-memory option for SST with mariadb-backup
* [Revision #24e5d56400](https://github.com/MariaDB/server/commit/24e5d56400)\
  2024-12-20 14:58:33 +0700
  * [MDEV-35680](https://jira.mariadb.org/browse/MDEV-35680) Table number > MAX\_TABLES causes overflow of table\_map at main.join test
* [Revision #d878d80bc4](https://github.com/MariaDB/server/commit/d878d80bc4)\
  2024-12-19 16:40:18 +0100
  * [MDEV-35695](https://jira.mariadb.org/browse/MDEV-35695): mtr failure suggests wrong url
* [Revision #f2ffcd949b](https://github.com/MariaDB/server/commit/f2ffcd949b)\
  2024-12-19 14:18:55 +0200
  * [MDEV-35657](https://jira.mariadb.org/browse/MDEV-35657): Add work-arounds for clang 11
* [Revision #e5c4c0842d](https://github.com/MariaDB/server/commit/e5c4c0842d)\
  2024-12-19 14:05:16 +0200
  * [MDEV-35443](https://jira.mariadb.org/browse/MDEV-35443): opt\_search\_plan\_for\_table() may degrade to full table scan
* [Revision #a226f12675](https://github.com/MariaDB/server/commit/a226f12675)\
  2024-12-05 09:36:52 -0500
  * [MDEV-35578](https://jira.mariadb.org/browse/MDEV-35578) innodb\_gis.rtree\_debug fails on mac
* [Revision #7b0f59da43](https://github.com/MariaDB/server/commit/7b0f59da43)\
  2024-12-17 09:56:54 +0100
  * wsrep mtr suite: update for galera library 26.4.21
* [Revision #c93ffd5e58](https://github.com/MariaDB/server/commit/c93ffd5e58)\
  2024-12-17 09:53:19 +0100
  * galera: wsrep-lib submodule update
* [Revision #eadf96cea4](https://github.com/MariaDB/server/commit/eadf96cea4)\
  2024-10-10 14:28:49 +0200
  * [MDEV-26266](https://jira.mariadb.org/browse/MDEV-26266) Update wsrep-lib
* [Revision #75dd0246f8](https://github.com/MariaDB/server/commit/75dd0246f8)\
  2024-12-11 17:35:53 +0100
  * Remove error handling from wsrep\_sync\_wait()
* [Revision #d72c5d1ace](https://github.com/MariaDB/server/commit/d72c5d1ace)\
  2024-12-10 15:08:38 +0100
  * Fixup for [MDEV-35446](https://jira.mariadb.org/browse/MDEV-35446)
* [Revision #ee2dc336d7](https://github.com/MariaDB/server/commit/ee2dc336d7)\
  2024-12-12 12:22:53 +0200
  * TODO-5067 addendum : Add test case for Galera library protocol versions
* [Revision #28463b2824](https://github.com/MariaDB/server/commit/28463b2824)\
  2024-12-12 09:28:49 +0200
  * TODO-5067 : Add test case for Galera library protocol versions
* [Revision #7c9cbe684b](https://github.com/MariaDB/server/commit/7c9cbe684b)\
  2024-12-13 14:42:40 -0500
  * [MDEV-35648](https://jira.mariadb.org/browse/MDEV-35648) Update partition lc2 tests for mac
* [Revision #77c9917663](https://github.com/MariaDB/server/commit/77c9917663)\
  2024-12-17 10:40:57 +1100
  * [MDEV-34716](https://jira.mariadb.org/browse/MDEV-34716) Fix mysql.servers socket max length too short
* [Revision #bc6121819c](https://github.com/MariaDB/server/commit/bc6121819c)\
  2024-12-16 19:34:09 +0200
  * [MDEV-35098](https://jira.mariadb.org/browse/MDEV-35098) rpl.rpl\_mysqldump\_gtid\_slave\_pos fails in buildbot
* [Revision #aa49770d79](https://github.com/MariaDB/server/commit/aa49770d79)\
  2024-10-21 12:21:51 +0700
  * [MDEV-31005](https://jira.mariadb.org/browse/MDEV-31005): Make working cursor-protocol
* [Revision #17cb65593a](https://github.com/MariaDB/server/commit/17cb65593a)\
  2024-04-20 00:17:30 +0200
  * [MDEV-22964](https://jira.mariadb.org/browse/MDEV-22964): archive.archive and main.mysqlbinlog\_{row,stmt}\_compressed)
* [Revision #d98ac8511e](https://github.com/MariaDB/server/commit/d98ac8511e)\
  2024-10-26 20:29:56 +0700
  * [MDEV-26247](https://jira.mariadb.org/browse/MDEV-26247) MariaDB Server SEGV on INSERT .. SELECT
* [Revision #e640373389](https://github.com/MariaDB/server/commit/e640373389)\
  2024-10-25 14:35:22 +0700
  * Revert "[MDEV-26427](https://jira.mariadb.org/browse/MDEV-26427) MariaDB Server SEGV on INSERT .. SELECT"
* [Revision #271b73770c](https://github.com/MariaDB/server/commit/271b73770c)\
  2024-12-13 16:27:14 +0100
  * [MDEV-30263](https://jira.mariadb.org/browse/MDEV-30263) Assertion failure in Protocol::end\_statement upon HANDLER READ with invalid timestamp
* [Revision #d1f42fc80f](https://github.com/MariaDB/server/commit/d1f42fc80f)\
  2024-12-03 14:03:17 +0400
  * [MDEV-21589](https://jira.mariadb.org/browse/MDEV-21589) AddressSanitizer: memcpy-param-overlap in Static\_binary\_string::q\_append or String::append
* [Revision #54c1031b74](https://github.com/MariaDB/server/commit/54c1031b74)\
  2024-12-13 09:29:23 +0700
  * [MDEV-34958](https://jira.mariadb.org/browse/MDEV-34958): after Trigger doesn't work correctly with bulk insert
* [Revision #0b7fa4c267](https://github.com/MariaDB/server/commit/0b7fa4c267)\
  2024-11-29 21:03:16 +0400
  * [MDEV-31219](https://jira.mariadb.org/browse/MDEV-31219) Assertion \`fixed' failed in Item\_func\_hybrid\_field\_type / Frame\_positional\_cursor
* [Revision #432856c473](https://github.com/MariaDB/server/commit/432856c473)\
  2024-12-09 19:27:53 +1100
  * [MDEV-35571](https://jira.mariadb.org/browse/MDEV-35571) Check for LIMIT ROWS EXAMINED exceeded in UNION ALL
* [Revision #3e34e4c161](https://github.com/MariaDB/server/commit/3e34e4c161)\
  2024-12-12 10:56:36 +0100
  * [MDEV-34820](https://jira.mariadb.org/browse/MDEV-34820): wsrep\_sst\_mariadb-backup get\_footprint() portability and accuracy fix
* [Revision #b52f88edf8](https://github.com/MariaDB/server/commit/b52f88edf8)\
  2024-12-12 10:15:26 +0100
  * [MDEV-35387](https://jira.mariadb.org/browse/MDEV-35387): wsrep\_sst\_rsync crash if aria\_log\_dir\_path is defined
* [Revision #71a9b3bf16](https://github.com/MariaDB/server/commit/71a9b3bf16)\
  2024-12-10 17:16:53 +0100
  * galera sst scripts: fix for error hangling code
* [Revision #6dcd9de2a9](https://github.com/MariaDB/server/commit/6dcd9de2a9)\
  2024-07-30 13:20:39 +1000
  * [MDEV-34669](https://jira.mariadb.org/browse/MDEV-34669): ER\_NEED\_REPREPARE on SELECT DEFAULT(name) FROM table1\_containing\_sequence
* [Revision #ab9182470d](https://github.com/MariaDB/server/commit/ab9182470d)\
  2024-11-20 13:46:43 +0400
  * [MDEV-31366](https://jira.mariadb.org/browse/MDEV-31366) Assertion \`thd->start\_time' failed in bool LOGGER::slow\_log\_print(THD\*, const char\*, size\_t, ulonglong)
* [Revision #95fdfb733d](https://github.com/MariaDB/server/commit/95fdfb733d)\
  2024-12-12 12:36:42 +0100
  * In allocate\_dynamic() fixed return value on error.
* [Revision #9a25f2a5bb](https://github.com/MariaDB/server/commit/9a25f2a5bb)\
  2024-12-12 11:58:11 +0200
  * [MDEV-35632](https://jira.mariadb.org/browse/MDEV-35632): HandlerSocket uses deprecated auto\_ptr
* [Revision #965e65d6bb](https://github.com/MariaDB/server/commit/965e65d6bb)\
  2023-11-10 11:59:06 +1100
  * [MDEV-32686](https://jira.mariadb.org/browse/MDEV-32686): Signal hander- minimise resource limit output.
* [Revision #801587c821](https://github.com/MariaDB/server/commit/801587c821)\
  2023-11-10 11:22:46 +1100
  * [MDEV-32686](https://jira.mariadb.org/browse/MDEV-32686): minimise crash information
* [Revision #7181ea5663](https://github.com/MariaDB/server/commit/7181ea5663)\
  2024-12-06 11:35:58 +1100
  * [MDEV-33245](https://jira.mariadb.org/browse/MDEV-33245) SIGSEGV in wsrep\_check\_sequence
* [Revision #ee287821e3](https://github.com/MariaDB/server/commit/ee287821e3)\
  2024-12-06 11:34:58 +1100
  * [MDEV-32561](https://jira.mariadb.org/browse/MDEV-32561): WSREP FSM failure: (postfix) - enable galera.galera\_sequences
* [Revision #807e4f320f](https://github.com/MariaDB/server/commit/807e4f320f)\
  2024-12-10 18:00:37 +1100
  * Change my\_umask{,\_dir} to mode\_t and remove os\_innodb\_umask
* [Revision #bf7cfa2535](https://github.com/MariaDB/server/commit/bf7cfa2535)\
  2024-12-05 15:31:40 +1100
  * [MDEV-35574](https://jira.mariadb.org/browse/MDEV-35574) remove obsolete pthread\_exit calls
* [Revision #d92d271648](https://github.com/MariaDB/server/commit/d92d271648)\
  2024-04-15 15:17:30 -0400
  * [MDEV-35583](https://jira.mariadb.org/browse/MDEV-35583) Tests failing on macOS
* [Revision #694d91da89](https://github.com/MariaDB/server/commit/694d91da89)\
  2024-12-09 08:54:17 +0100
  * [MDEV-35604](https://jira.mariadb.org/browse/MDEV-35604): SIGSEGV in filter\_query\_type | log\_statement\_ex / auditing
* [Revision #2ab10fbec2](https://github.com/MariaDB/server/commit/2ab10fbec2)\
  2024-12-03 15:02:06 +0100
  * [MDEV-24959](https://jira.mariadb.org/browse/MDEV-24959): ER\_BINLOG\_ROW\_LOGGING\_FAILED (1534: Writing one row to the row-based binary log failed)
* [Revision #b4fde50b1f](https://github.com/MariaDB/server/commit/b4fde50b1f)\
  2024-11-29 13:05:41 +0100
  * [MDEV-5798](https://jira.mariadb.org/browse/MDEV-5798): Wrong errorcode for missing partition after TRUNCATE PARTITION
* [Revision #5a3a16154f](https://github.com/MariaDB/server/commit/5a3a16154f)\
  2024-11-28 11:54:26 +0100
  * [MDEV-35514](https://jira.mariadb.org/browse/MDEV-35514): Too much mtr output from analyze: sync\_with\_master
* [Revision #daea59a81d](https://github.com/MariaDB/server/commit/daea59a81d)\
  2024-11-28 11:11:03 +0100
  * [MDEV-31761](https://jira.mariadb.org/browse/MDEV-31761): mariadb-binlog prints fractional timestamp part incorrectly
* [Revision #673936173f](https://github.com/MariaDB/server/commit/673936173f)\
  2024-12-04 13:08:28 +0100
  * Make sql\_acl\_getsort.ic named in line with other files i.e. sql\_acl\_getsort.inl
* [Revision #aa9d5aea48](https://github.com/MariaDB/server/commit/aa9d5aea48)\
  2024-12-04 15:39:10 +0300
  * [MDEV-34770](https://jira.mariadb.org/browse/MDEV-34770) GCC warning fix
* [Revision #2bf9f0d422](https://github.com/MariaDB/server/commit/2bf9f0d422)\
  2023-11-16 15:34:53 -0800
  * [MDEV-32395](https://jira.mariadb.org/browse/MDEV-32395): update\_depend\_map\_for\_order: SEGV at /mariadb-11.3.0/sql/sql\_select.cc:16583
* [Revision #8e9aa9c6b0](https://github.com/MariaDB/server/commit/8e9aa9c6b0)\
  2024-12-04 12:58:00 +0200
  * Fix MariadDB to compile with gcc 7.5.0
* [Revision #818c84ad45](https://github.com/MariaDB/server/commit/818c84ad45)\
  2024-12-03 15:08:25 +0100
  * galera mtr tests: post-fix changes to test suite
* [Revision #a2575a0703](https://github.com/MariaDB/server/commit/a2575a0703)\
  2024-11-21 16:54:51 +0200
  * [MDEV-35465](https://jira.mariadb.org/browse/MDEV-35465) Async replication stops working on Galera async replica node when parallel replication is enabled
* [Revision #c772344510](https://github.com/MariaDB/server/commit/c772344510)\
  2024-11-29 14:50:14 +0100
  * Allow mysqltest to run COMMIT statement under --ps-protocol
* [Revision #85bcc7d263](https://github.com/MariaDB/server/commit/85bcc7d263)\
  2024-11-19 16:56:21 +0100
  * [MDEV-35446](https://jira.mariadb.org/browse/MDEV-35446) Sporadic failure of galera.galera\_insert\_multi
* [Revision #b8ad202da1](https://github.com/MariaDB/server/commit/b8ad202da1)\
  2024-12-03 13:49:43 +0300
  * [MDEV-34770](https://jira.mariadb.org/browse/MDEV-34770) UBSAN: runtime error: load of address 0x... with insufficient space for an object of type 'uchar' in sys\_vars.inl
* [Revision #13f93da1f6](https://github.com/MariaDB/server/commit/13f93da1f6)\
  2024-12-03 13:49:43 +0300
  * [MDEV-33783](https://jira.mariadb.org/browse/MDEV-33783) CREATE SERVER segfaults on wrong mysql.servers
* [Revision #27c25ceedb](https://github.com/MariaDB/server/commit/27c25ceedb)\
  2024-12-03 13:49:42 +0300
  * [MDEV-31030](https://jira.mariadb.org/browse/MDEV-31030) Assertion \`!error' failed in ha\_partition::update\_row on UPDATE
* [Revision #55b5993205](https://github.com/MariaDB/server/commit/55b5993205)\
  2024-12-03 13:49:42 +0300
  * Cleanup: make\_keypart\_map inline
* [Revision #3835437eb8](https://github.com/MariaDB/server/commit/3835437eb8)\
  2024-12-03 13:49:42 +0300
  * [MDEV-15330](https://jira.mariadb.org/browse/MDEV-15330) Cleanup: load\_data.test removed
* [Revision #c20f09ddcf](https://github.com/MariaDB/server/commit/c20f09ddcf)\
  2024-12-03 13:49:42 +0300
  * Dtrace cmake fix for clang
* [Revision #8a32ae5d6d](https://github.com/MariaDB/server/commit/8a32ae5d6d)\
  2024-11-05 09:24:09 +0200
  * [MDEV-32779](https://jira.mariadb.org/browse/MDEV-32779) : galera\_concurrent\_ctas: assertion in the galera::ReplicatorSMM::finish\_cert()
* [Revision #f219fb8489](https://github.com/MariaDB/server/commit/f219fb8489)\
  2024-11-07 09:04:16 +0200
  * [MDEV-35355](https://jira.mariadb.org/browse/MDEV-35355) : Galera test failure on galera\_sr.mysql-wsrep-features#165
* [Revision #af50783fcd](https://github.com/MariaDB/server/commit/af50783fcd)\
  2024-11-21 13:22:49 +0200
  * [MDEV-35471](https://jira.mariadb.org/browse/MDEV-35471) : Sporadic failures in the galera\_pc\_recovery mtr test
* [Revision #bf3e16eb81](https://github.com/MariaDB/server/commit/bf3e16eb81)\
  2024-11-21 12:23:31 +0200
  * [MDEV-35467](https://jira.mariadb.org/browse/MDEV-35467) : WSREP: read\_completion\_condition(): shutdown while in init ()
* [Revision #d0fcac4450](https://github.com/MariaDB/server/commit/d0fcac4450)\
  2024-11-29 11:12:10 +1100
  * [MDEV-35422](https://jira.mariadb.org/browse/MDEV-35422) Fix spider group by handler trying to use fake group by fields
* [Revision #5c86f3df33](https://github.com/MariaDB/server/commit/5c86f3df33)\
  2024-11-29 11:45:01 +0100
  * [MDEV-35522](https://jira.mariadb.org/browse/MDEV-35522): MariaDB Audit does not detect all DCLs forms when masking password
* [Revision #3de412fbe8](https://github.com/MariaDB/server/commit/3de412fbe8)\
  2024-11-19 12:44:42 +0400
  * [MDEV-25593](https://jira.mariadb.org/browse/MDEV-25593) Assertion \`0' failed in Type\_handler\_temporal\_result::Item\_get\_date on double EXECUTE
* [Revision #ecf2e131bd](https://github.com/MariaDB/server/commit/ecf2e131bd)\
  2024-12-02 11:04:38 +0200
  * [MDEV-31174](https://jira.mariadb.org/browse/MDEV-31174) fixup: clang++-20 -Wnontrivial-memcall
* [Revision #01cc92e098](https://github.com/MariaDB/server/commit/01cc92e098)\
  2024-12-01 13:52:41 +0400
  * [MDEV-34700](https://jira.mariadb.org/browse/MDEV-34700) Connect SQLite3 MTR test fails due to various charset/collation related output changes
* [Revision #fdb6db6b47](https://github.com/MariaDB/server/commit/fdb6db6b47)\
  2024-11-06 10:21:08 +0400
  * [MDEV-29462](https://jira.mariadb.org/browse/MDEV-29462) ASAN: heap-use-after-free in Binary\_string::copy on DO CONVERT
* [Revision #f39217da0c](https://github.com/MariaDB/server/commit/f39217da0c)\
  2024-11-22 08:10:58 +0200
  * [MDEV-35473](https://jira.mariadb.org/browse/MDEV-35473) : Sporadic failures in the galera\_3nodes.galera\_evs\_suspect\_timeout mtr test
* [Revision #e7e06b3cb7](https://github.com/MariaDB/server/commit/e7e06b3cb7)\
  2024-11-22 11:58:06 +0200
  * [MDEV-35481](https://jira.mariadb.org/browse/MDEV-35481) : ER\_LOCK\_DEADLOCK instead of ER\_NO\_SUCH\_TABLE in galera\_var\_ignore\_apply\_errors
* [Revision #ff45fdac29](https://github.com/MariaDB/server/commit/ff45fdac29)\
  2024-11-22 15:31:48 +0200
  * [MDEV-35440](https://jira.mariadb.org/browse/MDEV-35440) : Protocol error warning in the galera\_wsrep\_schema\_detached test
* [Revision #8bc254dd62](https://github.com/MariaDB/server/commit/8bc254dd62)\
  2024-11-20 17:47:24 +0100
  * [MDEV-26516](https://jira.mariadb.org/browse/MDEV-26516): WSREP: Record locking is disabled in this thread, but the table being modified
* [Revision #0ea19c12fd](https://github.com/MariaDB/server/commit/0ea19c12fd)\
  2024-11-27 14:40:02 +0100
  * [MDEV-35507](https://jira.mariadb.org/browse/MDEV-35507) ed25519 authentication plugin create user statement trigger plain text password in audit log
* [Revision #f39a61505f](https://github.com/MariaDB/server/commit/f39a61505f)\
  2024-08-13 15:56:03 +0200
  * [MDEV-33075](https://jira.mariadb.org/browse/MDEV-33075) \[backport/2f5174e556] use more robust self-pipe to wake up poll() in break\_connect\_loop()
* [Revision #c4cadb768f](https://github.com/MariaDB/server/commit/c4cadb768f)\
  2024-08-13 15:53:42 +0200
  * [MDEV-33075](https://jira.mariadb.org/browse/MDEV-33075) \[backport/2f5174e556] fix rnd crash on macOS from pthread\_kill(signal\_handler)
* [Revision #8214707699](https://github.com/MariaDB/server/commit/8214707699)\
  2024-08-13 15:43:33 +0200
  * [MDEV-33075](https://jira.mariadb.org/browse/MDEV-33075) \[backport/2f5174e556] fix signal handler thread exit on abort
* [Revision #490274e850](https://github.com/MariaDB/server/commit/490274e850)\
  2024-08-18 21:40:34 +0200
  * [MDEV-33075](https://jira.mariadb.org/browse/MDEV-33075) \[backport/2f5174e556] eliminated support for `#ifndef HAVE_POLL`
* [Revision #5be859d52c](https://github.com/MariaDB/server/commit/5be859d52c)\
  2024-11-27 10:25:09 +1100
  * [MDEV-30649](https://jira.mariadb.org/browse/MDEV-30649) Adding a spider testcase showing copying from a remote to a local table
* [Revision #a8cc40d9a4](https://github.com/MariaDB/server/commit/a8cc40d9a4)\
  2024-10-04 16:49:53 +1000
  * [MDEV-35064](https://jira.mariadb.org/browse/MDEV-35064) Reduce the default spider connect retry counts to 2
* [Revision #142851f120](https://github.com/MariaDB/server/commit/142851f120)\
  2024-11-25 10:31:37 +0200
  * Update my\_print\_defaults to accept --mariadbd as an option
* [Revision #f09020b3bb](https://github.com/MariaDB/server/commit/f09020b3bb)\
  2024-11-25 10:28:44 +0200
  * Fixed bug in subselect3.inc (not notable)
* [Revision #225c17d35c](https://github.com/MariaDB/server/commit/225c17d35c)\
  2024-11-07 12:16:33 +0400
  * [MDEV-34090](https://jira.mariadb.org/browse/MDEV-34090) Client allows to set character set to utf32 and crashes on the next command
* [Revision #425d2521ec](https://github.com/MariaDB/server/commit/425d2521ec)\
  2024-11-12 08:58:48 +0400
  * [MDEV-33472](https://jira.mariadb.org/browse/MDEV-33472) Assertion \`0' failed in Item\_row::illegal\_method\_call on CREATE EVENT
* [Revision #20eba06d9b](https://github.com/MariaDB/server/commit/20eba06d9b)\
  2024-11-25 16:13:16 +0400
  * [MDEV-35489](https://jira.mariadb.org/browse/MDEV-35489) Assertion \`!ldate->neg' or unexpected result upon extracting unit from invalid value
* [Revision #2e404c9850](https://github.com/MariaDB/server/commit/2e404c9850)\
  2024-11-12 11:06:32 +0400
  * [MDEV-21029](https://jira.mariadb.org/browse/MDEV-21029) Incorrect result for expression with the <=> operator and IS NULL
* [Revision #773cb726a8](https://github.com/MariaDB/server/commit/773cb726a8)\
  2024-07-15 07:54:38 -0600
  * [MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348): MariaDB is violating clang-16 -Wcast-function-type-strict
* [Revision #6456e437f2](https://github.com/MariaDB/server/commit/6456e437f2)\
  2024-07-09 18:29:11 +1000
  * [MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348): Add cast-function-type-strict to warnings
* [Revision #971a0ba23c](https://github.com/MariaDB/server/commit/971a0ba23c)\
  2024-06-14 13:13:40 +1000
  * [MDEV-34408](https://jira.mariadb.org/browse/MDEV-34408): Facilitate the addition of warnings into the build system
* [Revision #78d7bb1d27](https://github.com/MariaDB/server/commit/78d7bb1d27)\
  2024-10-26 14:19:57 -0600
  * [MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348): Miscellaneous fixes
* [Revision #3c785499da](https://github.com/MariaDB/server/commit/3c785499da)\
  2024-10-26 14:13:32 -0600
  * [MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348): Fix casts relating to tree\_walk\_action
* [Revision #5432fa802b](https://github.com/MariaDB/server/commit/5432fa802b)\
  2024-10-26 14:00:11 -0600
  * [MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348): Fix casts in sql\_acl
* [Revision #7a8eb26bda](https://github.com/MariaDB/server/commit/7a8eb26bda)\
  2024-10-26 13:53:51 -0600
  * [MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348): Fix casting related to plugins
* [Revision #840fe316d4](https://github.com/MariaDB/server/commit/840fe316d4)\
  2024-10-26 11:34:26 -0600
  * [MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348): my\_hash\_get\_key fixes
* [Revision #dbfee9fc2b](https://github.com/MariaDB/server/commit/dbfee9fc2b)\
  2024-10-26 08:17:03 -0600
  * [MDEV-34348](https://jira.mariadb.org/browse/MDEV-34348): Consolidate cmp function declarations
* [Revision #3997d28f48](https://github.com/MariaDB/server/commit/3997d28f48)\
  2024-11-21 10:47:56 +0400
  * [MDEV-16698](https://jira.mariadb.org/browse/MDEV-16698) ASAN: heap-use-after-free in field\_longstr::uncompress
* [Revision #95df7ea33a](https://github.com/MariaDB/server/commit/95df7ea33a)\
  2024-11-21 10:01:48 +0400
  * [MDEV-31881](https://jira.mariadb.org/browse/MDEV-31881) ASAN: unknown-crash in check\_ulonglong (sql/sql\_analyse.cc) on SELECT ... FROM ... PROCEDURE ANALYSE()
* [Revision #39f1f30f68](https://github.com/MariaDB/server/commit/39f1f30f68)\
  2024-11-22 12:11:32 +0400
  * [MDEV-23687](https://jira.mariadb.org/browse/MDEV-23687) Assertion \`is\_valid\_value\_slow()' failed in Datetime::Datetime upon EXTRACT under mode ZERO\_DATE\_TIME\_CAST
* [Revision #cf2d49ddcf](https://github.com/MariaDB/server/commit/cf2d49ddcf)\
  2024-11-14 17:42:43 -0700
  * Extract some of #3360 fixes to 10.5.x
* [Revision #b414eca98d](https://github.com/MariaDB/server/commit/b414eca98d)\
  2024-11-21 16:51:41 +1100
  * Correct cursor protocol tests main.{loaddata,grant\_plugin} & innodb\_fts.fulltext
* [Revision #2c89fe7ea6](https://github.com/MariaDB/server/commit/2c89fe7ea6)\
  2024-11-21 17:30:13 +1100
  * main.stack view protocol - correct test result
* [Revision #32962ea253](https://github.com/MariaDB/server/commit/32962ea253)\
  2024-11-19 21:41:06 +0200
  * Do not read aria bitmap page for internal temporary tables
* [Revision #93fb364cd9](https://github.com/MariaDB/server/commit/93fb364cd9)\
  2024-11-19 20:15:45 +0200
  * Removed not used ha\_drop\_table()
* [Revision #69be363daa](https://github.com/MariaDB/server/commit/69be363daa)\
  2024-11-19 19:05:52 +0200
  * Fixed that internal temporary Aria tables are not flushed to disk
* [Revision #0de9e40f4b](https://github.com/MariaDB/server/commit/0de9e40f4b)\
  2024-10-21 15:05:14 +0300
  * Added status variable "stack\_usable" to be able to check stack usage
* [Revision #ae0cbfe934](https://github.com/MariaDB/server/commit/ae0cbfe934)\
  2024-11-11 12:50:56 +0400
  * [MDEV-28001](https://jira.mariadb.org/browse/MDEV-28001) greatest/least with bigint unsigned maxium has unexpected results compared to 0
* [Revision #74184074a0](https://github.com/MariaDB/server/commit/74184074a0)\
  2024-11-11 10:00:26 +0400
  * [MDEV-28652](https://jira.mariadb.org/browse/MDEV-28652) SUBSTRING(str,pos,len) returns incorrect result in view (returns an empty string)
* [Revision #09fe74c7fd](https://github.com/MariaDB/server/commit/09fe74c7fd)\
  2024-11-13 09:40:18 +0400
  * [MDEV-25174](https://jira.mariadb.org/browse/MDEV-25174) DOUBLE columns do not accept large hex hybrids
* [Revision #70dbd63e02](https://github.com/MariaDB/server/commit/70dbd63e02)\
  2024-11-18 12:38:43 +0400
  * [MDEV-24337](https://jira.mariadb.org/browse/MDEV-24337) Server crash in DTCollation::set\_repertoire\_from\_charset
* [Revision #76fc26d632](https://github.com/MariaDB/server/commit/76fc26d632)\
  2024-11-19 03:08:20 +0100
  * galera SST scripts: correction of the grep pattern
* [Revision #540288ac7c](https://github.com/MariaDB/server/commit/540288ac7c)\
  2024-11-15 11:58:04 +1100
  * Fix URL in mariadb-install (no longer on launchpad)
* [Revision #1d6502b4f4](https://github.com/MariaDB/server/commit/1d6502b4f4)\
  2024-11-18 21:02:19 +1100
  * [MDEV-34534](https://jira.mariadb.org/browse/MDEV-34534) main.plugin\_load(daemon\_example) - AddressSanitizer: Joining already joined thread, aborting
* [Revision #b65504b8db](https://github.com/MariaDB/server/commit/b65504b8db)\
  2024-11-18 11:34:13 +0400
  * [MDEV-23138](https://jira.mariadb.org/browse/MDEV-23138) Odd behavior of character\_set variables set to utf16 (when allowed)
* [Revision #ed72eadfb8](https://github.com/MariaDB/server/commit/ed72eadfb8)\
  2024-11-15 17:35:57 +0400
  * [MDEV-35421](https://jira.mariadb.org/browse/MDEV-35421) - main.mysql\_upgrade fails without unix\_socket plugin
* [Revision #7f55c61060](https://github.com/MariaDB/server/commit/7f55c61060)\
  2024-11-10 12:34:02 +1100
  * Update Windows TZ data from unicode source (2024b)
* [Revision #13a14c0d78](https://github.com/MariaDB/server/commit/13a14c0d78)\
  2024-11-14 11:35:36 +0400
  * [MDEV-33987](https://jira.mariadb.org/browse/MDEV-33987) Server crashes at Item\_func\_as\_wkt::val\_str\_ascii
* [Revision #8a3c53f32b](https://github.com/MariaDB/server/commit/8a3c53f32b)\
  2024-11-13 23:07:02 +0100
  * Connect engine - fix compiler error with MSVC 17.12
* [Revision #cad881ab10](https://github.com/MariaDB/server/commit/cad881ab10)\
  2024-11-08 17:11:41 +1100
  * [MDEV-35088](https://jira.mariadb.org/browse/MDEV-35088) main.timezone failing - MEST vs CET time zone difference
* [Revision #ce3d0cd5b4](https://github.com/MariaDB/server/commit/ce3d0cd5b4)\
  2024-08-16 12:16:11 +0300
  * [MDEV-35407](https://jira.mariadb.org/browse/MDEV-35407) Suppress STDERR while determining rpm package vendor
* [Revision #155a82e0b1](https://github.com/MariaDB/server/commit/155a82e0b1)\
  2024-11-08 06:39:55 -0700
  * [MDEV-35350](https://jira.mariadb.org/browse/MDEV-35350): Backport search\_pattern\_in\_file.inc SEARCH\_WAIT to 10.5
* [Revision #a927e59e63](https://github.com/MariaDB/server/commit/a927e59e63)\
  2024-08-30 22:13:38 +0200
  * [MDEV-34847](https://jira.mariadb.org/browse/MDEV-34847) : Unquoted argument in `{{logger}}` call leads to invalid argument warnings
* [Revision #1802785cc2](https://github.com/MariaDB/server/commit/1802785cc2)\
  2024-08-30 21:47:51 +0200
  * [MDEV-34847](https://jira.mariadb.org/browse/MDEV-34847) : Unquoted argument in `{{logger}}` call leads to invalid argument warnings
* [Revision #df4b1349d9](https://github.com/MariaDB/server/commit/df4b1349d9)\
  2024-11-06 14:43:18 +1100
  * fixup of [MDEV-26345](https://jira.mariadb.org/browse/MDEV-26345): make initialisation of a local bitmap earlier
* [Revision #7afee25b08](https://github.com/MariaDB/server/commit/7afee25b08)\
  2024-11-08 12:15:55 +0530
  * [MDEV-35115](https://jira.mariadb.org/browse/MDEV-35115) Inconsistent Replace behaviour when multiple unique index exist
* [Revision #98d57719e2](https://github.com/MariaDB/server/commit/98d57719e2)\
  2024-11-08 11:35:19 +0530
  * [MDEV-32667](https://jira.mariadb.org/browse/MDEV-32667) dict\_stats\_save\_index\_stat() reads uninitialized index->stats\_error\_printed
* [Revision #4b38af06a4](https://github.com/MariaDB/server/commit/4b38af06a4)\
  2024-10-30 09:37:10 +0200
  * [MDEV-35157](https://jira.mariadb.org/browse/MDEV-35157) : wrong binlog timestamps on secondary nodes of a galera cluster
* [Revision #db68eb69f9](https://github.com/MariaDB/server/commit/db68eb69f9)\
  2024-11-06 01:39:31 +0100
  * [MDEV-35344](https://jira.mariadb.org/browse/MDEV-35344): post-fix correction for other galera tests
* [Revision #e4a3a11dcc](https://github.com/MariaDB/server/commit/e4a3a11dcc)\
  2024-11-05 12:09:30 +0200
  * [MDEV-35344](https://jira.mariadb.org/browse/MDEV-35344) : Galera test failure on galera\_sync\_wait\_upto
* [Revision #eb891b6a95](https://github.com/MariaDB/server/commit/eb891b6a95)\
  2024-11-05 12:42:50 +0200
  * [MDEV-35345](https://jira.mariadb.org/browse/MDEV-35345) : Galera test failure on MW-402
* [Revision #6d5fe9ed0d](https://github.com/MariaDB/server/commit/6d5fe9ed0d)\
  2024-03-20 14:12:22 +0300
  * [MDEV-28378](https://jira.mariadb.org/browse/MDEV-28378): Don't hang trying to peek log event past the end of log
* Merge [Revision #ecdccddaae](https://github.com/MariaDB/server/commit/ecdccddaae) 2024-11-04 07:35:28 +0100 - Merge branch '10.5' into mariadb-10.5.27
* [Revision #2c42b24534](https://github.com/MariaDB/server/commit/2c42b24534)\
  2024-11-01 11:13:09 -0400
  * bump the VERSION
* [Revision #e147f8a5ed](https://github.com/MariaDB/server/commit/e147f8a5ed)\
  2024-10-30 21:29:21 +0100
  * Fixup bddbef357334
* [Revision #c3a7a3c7a2](https://github.com/MariaDB/server/commit/c3a7a3c7a2)\
  2024-08-01 21:22:55 +0700
  * [MDEV-34665](https://jira.mariadb.org/browse/MDEV-34665) Simplify IN predicate processing for NULL-aware materialization involving only one column
* [Revision #9bb95de186](https://github.com/MariaDB/server/commit/9bb95de186)\
  2024-10-29 12:09:13 +0200
  * [MDEV-35253](https://jira.mariadb.org/browse/MDEV-35253): xa\_prepare\_unlock\_unmodified fails ... : part 2
* [Revision #d64034770e](https://github.com/MariaDB/server/commit/d64034770e)\
  2024-10-28 14:48:28 +0100
  * [MDEV-35273](https://jira.mariadb.org/browse/MDEV-35273) tpool::worker\_data - replace MY\_ALIGNED with pad member

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
