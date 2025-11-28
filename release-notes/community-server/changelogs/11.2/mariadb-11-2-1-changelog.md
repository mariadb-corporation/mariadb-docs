# MariaDB 11.2.1 Changelog

The most recent release of [MariaDB 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md) is:[**MariaDB 11.2.6**](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.2.6/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.2.6/)

[Download 11.2.1](https://downloads.mariadb.org/mariadb/11.2.1/)[Release Notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-1-release-notes.md)[Changelog](mariadb-11-2-1-changelog.md)[Overview of 11.2](../../old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112.md)

**Release date:** 21 Aug 2023

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-1-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Changes from [11.2.0](../../old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes.md) are also included in this changelog
* Includes all fixes from [MariaDB 11.1.2](../11.1/mariadb-11-1-2-changelog.md)
* Merge [Revision #18ddde4826](https://github.com/MariaDB/server/commit/18ddde4826) 2023-08-17 17:27:05 +0200 - Merge branch '11.1' into 11.2
* [Revision #8aa1a9e6a7](https://github.com/MariaDB/server/commit/8aa1a9e6a7)\
  2023-08-08 18:07:56 +0400
  * [MDEV-31812](https://jira.mariadb.org/browse/MDEV-31812) Add switch to old\_mode to disable non-locking ALTER
* [Revision #a1af525588](https://github.com/MariaDB/server/commit/a1af525588)\
  2023-08-07 22:43:40 +0400
  * [MDEV-31804](https://jira.mariadb.org/browse/MDEV-31804) Assertion \`thd->m\_transaction\_psi == null' fails
* [Revision #c373e6c3d6](https://github.com/MariaDB/server/commit/c373e6c3d6)\
  2023-08-07 22:25:17 +0400
  * Cleanup: make slave\_exec\_mode of its enum type and pack Log\_event better
* [Revision #982b689566](https://github.com/MariaDB/server/commit/982b689566)\
  2023-08-04 00:20:03 +0400
  * [MDEV-31838](https://jira.mariadb.org/browse/MDEV-31838) Assertion fails upon replication online alter with MINIMAL row
* [Revision #c4adaed0d0](https://github.com/MariaDB/server/commit/c4adaed0d0)\
  2023-07-28 19:46:02 +0400
  * [MDEV-31781](https://jira.mariadb.org/browse/MDEV-31781) ALTER TABLE ENGINE=s3 fails
* [Revision #30c965f866](https://github.com/MariaDB/server/commit/30c965f866)\
  2023-07-28 17:13:55 +0400
  * [MDEV-31777](https://jira.mariadb.org/browse/MDEV-31777) ER\_GET\_ERRNO upon online alter on CONNECT table
* [Revision #44ca37ef17](https://github.com/MariaDB/server/commit/44ca37ef17)\
  2023-07-27 15:26:32 +0400
  * [MDEV-31631](https://jira.mariadb.org/browse/MDEV-31631) Adding auto-increment to table with history online misbehaves
* [Revision #e026a366bf](https://github.com/MariaDB/server/commit/e026a366bf)\
  2023-07-26 21:24:47 +0400
  * [MDEV-31776](https://jira.mariadb.org/browse/MDEV-31776) Online ALTER reports the number of affected rows incorrectly
* [Revision #9c8554259a](https://github.com/MariaDB/server/commit/9c8554259a)\
  2023-07-26 00:58:00 +0400
  * [MDEV-31775](https://jira.mariadb.org/browse/MDEV-31775) Server crash upon online alter on sequence
* [Revision #7d0d9eab03](https://github.com/MariaDB/server/commit/7d0d9eab03)\
  2023-07-25 17:32:24 +0400
  * add to binlog\_bytes\_written for an initial description event
* [Revision #2952274ac4](https://github.com/MariaDB/server/commit/2952274ac4)\
  2023-07-25 01:58:39 +0400
  * make a proper cleanup if online\_alter\_binlog is failed to create
* [Revision #bac8f189ed](https://github.com/MariaDB/server/commit/bac8f189ed)\
  2023-07-20 21:20:37 +0300
  * [MDEV-31755](https://jira.mariadb.org/browse/MDEV-31755) Replica's DML event deadlocks wit online alter table
* [Revision #e1b9ab1995](https://github.com/MariaDB/server/commit/e1b9ab1995)\
  2023-07-20 20:13:08 +0400
  * fix key detection on replica with extra columns
* [Revision #70491fb07b](https://github.com/MariaDB/server/commit/70491fb07b)\
  2023-07-19 18:28:17 +0400
  * [MDEV-31677](https://jira.mariadb.org/browse/MDEV-31677) Assertion failed upon online ALTER with binlog\_row\_image=NOBLOB
* [Revision #a539fac8bd](https://github.com/MariaDB/server/commit/a539fac8bd)\
  2023-07-19 13:26:37 +0400
  * [MDEV-31646](https://jira.mariadb.org/browse/MDEV-31646) untie from max\_allowed\_packet and opt\_binlog\_rows\_event\_max\_size
* [Revision #d5e59c983f](https://github.com/MariaDB/server/commit/d5e59c983f)\
  2023-07-13 18:15:28 +0400
  * [MDEV-31646](https://jira.mariadb.org/browse/MDEV-31646) Online alter applies binlog cache limit to cache writes
* [Revision #2cecb5a638](https://github.com/MariaDB/server/commit/2cecb5a638)\
  2023-07-04 22:14:27 +0400
  * [MDEV-31601](https://jira.mariadb.org/browse/MDEV-31601) Some ALTER TABLEs fail ... with a wrong error message
* [Revision #8a165d7c19](https://github.com/MariaDB/server/commit/8a165d7c19)\
  2023-06-28 23:11:45 +0300
  * follow-up [MDEV-30430](https://jira.mariadb.org/browse/MDEV-30430): fix versioning.rpl
* [Revision #43cb98b420](https://github.com/MariaDB/server/commit/43cb98b420)\
  2023-06-28 14:37:47 +0300
  * fix main.mysql57\_virtual, main.alter\_table, innodb.alter\_algorithm
* [Revision #c382de72ea](https://github.com/MariaDB/server/commit/c382de72ea)\
  2023-05-15 19:39:21 +0300
  * [MDEV-30984](https://jira.mariadb.org/browse/MDEV-30984) Online ALTER table is denied with non-informative error messages
* [Revision #b3f988d260](https://github.com/MariaDB/server/commit/b3f988d260)\
  2023-05-28 00:23:41 +0300
  * Add const to get\_foreign\_key\_list/get\_parent\_foreign\_key\_list
* [Revision #500787c72a](https://github.com/MariaDB/server/commit/500787c72a)\
  2023-05-27 22:54:13 +0300
  * Add const to alloc-related thd methods
* [Revision #d7b0c6d8a8](https://github.com/MariaDB/server/commit/d7b0c6d8a8)\
  2023-05-13 21:55:08 +0300
  * [MDEV-30987](https://jira.mariadb.org/browse/MDEV-30987) main.alter\_table\_online times out with view-protocol
* [Revision #55d1645d5b](https://github.com/MariaDB/server/commit/55d1645d5b)\
  2023-05-13 14:44:15 +0300
  * [MDEV-31059](https://jira.mariadb.org/browse/MDEV-31059) "Slave SQL" errors upon concurrent DML and erroneous ALTER
* [Revision #3a42f2869e](https://github.com/MariaDB/server/commit/3a42f2869e)\
  2023-05-04 16:55:42 +0300
  * refactor unpack\_row
* [Revision #500379cf49](https://github.com/MariaDB/server/commit/500379cf49)\
  2023-05-04 01:48:38 +0300
  * unpack\_row: unpack a correct number of fields
* [Revision #da277396bd](https://github.com/MariaDB/server/commit/da277396bd)\
  2023-07-04 22:16:31 +0400
  * [MDEV-31058](https://jira.mariadb.org/browse/MDEV-31058) ER\_KEY\_NOT\_FOUND upon concurrent CHANGE column autoinc and DML
* [Revision #af82d56a51](https://github.com/MariaDB/server/commit/af82d56a51)\
  2023-04-23 18:31:57 +0300
  * unpack\_row: set the correct fields in has\_value\_set for online alter
* [Revision #ecb9db4c3d](https://github.com/MariaDB/server/commit/ecb9db4c3d)\
  2023-04-18 00:52:46 +0300
  * [MDEV-30949](https://jira.mariadb.org/browse/MDEV-30949) Direct leak in binlog\_online\_alter\_end\_trans
* [Revision #0695f7dd7b](https://github.com/MariaDB/server/commit/0695f7dd7b)\
  2023-04-14 04:34:21 +0300
  * [MDEV-31043](https://jira.mariadb.org/browse/MDEV-31043) ER\_KEY\_NOT\_FOUND upon concurrent ALTER and transaction
* [Revision #c76072db93](https://github.com/MariaDB/server/commit/c76072db93)\
  2023-04-12 02:01:31 +0300
  * [MDEV-31033](https://jira.mariadb.org/browse/MDEV-31033) ER\_KEY\_NOT\_FOUND upon online COPY ALTER on a partitioned table
* [Revision #0775c7bdc3](https://github.com/MariaDB/server/commit/0775c7bdc3)\
  2023-04-11 00:11:21 +0300
  * [MDEV-30945](https://jira.mariadb.org/browse/MDEV-30945) RPL tests are failing with MSAN use-of-uninitialized-value
* [Revision #2ce2440538](https://github.com/MariaDB/server/commit/2ce2440538)\
  2023-04-10 23:58:42 +0300
  * clean up Rows\_log\_event virtual methods
* [Revision #e1f5c58ac7](https://github.com/MariaDB/server/commit/e1f5c58ac7)\
  2023-04-04 23:41:58 +0300
  * [MDEV-30891](https://jira.mariadb.org/browse/MDEV-30891) Assertion \`!table->versioned(VERS\_TRX\_ID)' failed
* [Revision #5361b87093](https://github.com/MariaDB/server/commit/5361b87093)\
  2023-04-04 12:46:02 +0300
  * add partition test
* [Revision #5f206259e5](https://github.com/MariaDB/server/commit/5f206259e5)\
  2023-04-04 04:19:35 +0300
  * [MDEV-30985](https://jira.mariadb.org/browse/MDEV-30985) Replica stops with error on ALTER ONLINE with Geometry Types
* [Revision #3ad0e7edd1](https://github.com/MariaDB/server/commit/3ad0e7edd1)\
  2023-03-26 17:50:37 +0300
  * [MDEV-30924](https://jira.mariadb.org/browse/MDEV-30924) Server crashes in MYSQL\_LOG::is\_open upon ALTER vs FUNCTION
* [Revision #6b35d6a909](https://github.com/MariaDB/server/commit/6b35d6a909)\
  2023-03-26 00:26:05 +0300
  * [MDEV-30925](https://jira.mariadb.org/browse/MDEV-30925) Assertion failed in translog\_write\_record in ONLINE ALTER + Aria
* [Revision #6f78efc01c](https://github.com/MariaDB/server/commit/6f78efc01c)\
  2023-03-22 23:31:15 +0300
  * [MDEV-30902](https://jira.mariadb.org/browse/MDEV-30902) Server crash in LEX::first\_lists\_tables\_same
* [Revision #b08b78c5b9](https://github.com/MariaDB/server/commit/b08b78c5b9)\
  2022-10-21 15:08:26 +0300
  * [MDEV-29068](https://jira.mariadb.org/browse/MDEV-29068) Cascade foreign key updates do not apply in online alter
* [Revision #84ed2e7ce6](https://github.com/MariaDB/server/commit/84ed2e7ce6)\
  2023-02-15 19:26:32 +0300
  * fix main.alter\_table\_{online,lock}
* [Revision #41697008fe](https://github.com/MariaDB/server/commit/41697008fe)\
  2022-11-29 20:40:07 +0100
  * [MDEV-29069](https://jira.mariadb.org/browse/MDEV-29069) follow-up: improve DEFAULT rules
* [Revision #30756775d5](https://github.com/MariaDB/server/commit/30756775d5)\
  2022-07-25 23:49:02 +0300
  * [MDEV-29069](https://jira.mariadb.org/browse/MDEV-29069) follow-up: support partially usable keys
* [Revision #bac728a263](https://github.com/MariaDB/server/commit/bac728a263)\
  2022-07-19 00:29:42 +0300
  * [MDEV-29069](https://jira.mariadb.org/browse/MDEV-29069) follow-up: allow deterministic DEFAULTs
* [Revision #2be4c836e5](https://github.com/MariaDB/server/commit/2be4c836e5)\
  2022-11-21 12:25:48 +0100
  * [MDEV-29069](https://jira.mariadb.org/browse/MDEV-29069) ER\_KEY\_NOT\_FOUND on online autoinc addition + concurrent DELETE
* [Revision #d1e09972f0](https://github.com/MariaDB/server/commit/d1e09972f0)\
  2022-11-07 16:52:56 +0100
  * cleanup: cache the result of Rows\_log\_event::find\_key()
* [Revision #6ecc90ae36](https://github.com/MariaDB/server/commit/6ecc90ae36)\
  2022-11-07 16:52:17 +0100
  * set table->pos\_in\_table\_list in online alter
* [Revision #e72ed758c7](https://github.com/MariaDB/server/commit/e72ed758c7)\
  2022-11-07 16:51:35 +0100
  * cleanup: remove rpl\_group\_info::get\_table\_data()
* [Revision #8a8f71b8b8](https://github.com/MariaDB/server/commit/8a8f71b8b8)\
  2022-11-07 16:10:10 +0100
  * cleanup: ifdefs
* [Revision #0311b11225](https://github.com/MariaDB/server/commit/0311b11225)\
  2022-10-13 18:08:48 +0300
  * few rgi assertions. this can proof that rgi is always present
* [Revision #daebec6093](https://github.com/MariaDB/server/commit/daebec6093)\
  2022-07-19 16:36:32 +0300
  * rename rpl/rpl\_alter\_instant -> rpl/rpl\_alter\_innodb
* [Revision #754c8dab52](https://github.com/MariaDB/server/commit/754c8dab52)\
  2022-07-19 01:19:11 +0300
  * [MDEV-29038](https://jira.mariadb.org/browse/MDEV-29038) XA assertions failing in binlog\_rollback and binlog\_commit
* [Revision #45bafdbe25](https://github.com/MariaDB/server/commit/45bafdbe25)\
  2022-07-25 23:52:49 +0300
  * log\_event.h: remove junk EOL spaces
* [Revision #6e0f456090](https://github.com/MariaDB/server/commit/6e0f456090)\
  2022-06-29 23:32:19 +0300
  * [MDEV-29013](https://jira.mariadb.org/browse/MDEV-29013) ER\_KEY\_NOT\_FOUND/lock timeout upon online alter with long unique
* [Revision #d6e0d29f84](https://github.com/MariaDB/server/commit/d6e0d29f84)\
  2022-11-24 17:45:30 +0100
  * Fix write\_set too
* [Revision #4a00bc87b5](https://github.com/MariaDB/server/commit/4a00bc87b5)\
  2022-07-24 13:34:39 +0200
  * [MDEV-28816](https://jira.mariadb.org/browse/MDEV-28816) Assertion \`wsrep\_thd\_is\_applying(thd)' failed in int wsrep\_ignored\_error\_code(Log\_event\*, int)
* [Revision #da5df33927](https://github.com/MariaDB/server/commit/da5df33927)\
  2022-09-28 10:01:07 +0300
  * rpl: check should go after defaults and vcols update
* [Revision #aa1a2507f5](https://github.com/MariaDB/server/commit/aa1a2507f5)\
  2022-07-15 09:08:52 +0200
  * [MDEV-29067](https://jira.mariadb.org/browse/MDEV-29067) Online alter ignores check constraint violation
* [Revision #472c3d082f](https://github.com/MariaDB/server/commit/472c3d082f)\
  2022-07-15 08:52:33 +0200
  * don't do ALTER IGNORE TABLE online
* [Revision #aa9e173e9e](https://github.com/MariaDB/server/commit/aa9e173e9e)\
  2022-07-04 20:29:36 +0300
  * [MDEV-29021](https://jira.mariadb.org/browse/MDEV-29021) add test case from [MDEV-29013](https://jira.mariadb.org/browse/MDEV-29013)
* [Revision #b0db7239b1](https://github.com/MariaDB/server/commit/b0db7239b1)\
  2022-07-04 19:34:32 +0300
  * Do not ignore sql\_mode when replicating
* [Revision #bdbd357362](https://github.com/MariaDB/server/commit/bdbd357362)\
  2022-07-04 18:27:33 +0300
  * Simplify rgi->get\_table\_data call
* [Revision #b8c5f94b91](https://github.com/MariaDB/server/commit/b8c5f94b91)\
  2022-07-04 17:47:50 +0300
  * reorder RPL\_TABLE\_LIST fields for better packing
* [Revision #a3d1d1485a](https://github.com/MariaDB/server/commit/a3d1d1485a)\
  2022-07-16 19:35:32 +0200
  * [MDEV-29021](https://jira.mariadb.org/browse/MDEV-29021) mark fields that have explicit values
* [Revision #93fb92d3f9](https://github.com/MariaDB/server/commit/93fb92d3f9)\
  2022-07-04 15:13:51 +0300
  * [MDEV-29021](https://jira.mariadb.org/browse/MDEV-29021) ALTER TABLE fails when a stored virtual column is dropped+added
* [Revision #ea46fdcea4](https://github.com/MariaDB/server/commit/ea46fdcea4)\
  2022-07-13 11:16:30 +0200
  * cleanup, remove dead code
* [Revision #845c939601](https://github.com/MariaDB/server/commit/845c939601)\
  2022-07-01 13:50:02 +0200
  * [MDEV-28943](https://jira.mariadb.org/browse/MDEV-28943) Online alter fails under LOCK TABLE with ER\_ALTER\_OPERATION\_NOT\_SUPPORTED\_REASON
* [Revision #2ed03a41e6](https://github.com/MariaDB/server/commit/2ed03a41e6)\
  2022-06-29 20:16:19 +0300
  * [MDEV-28930](https://jira.mariadb.org/browse/MDEV-28930) ALTER TABLE Deadlocks with parallel TL\_WRITE
* [Revision #8fbdc76038](https://github.com/MariaDB/server/commit/8fbdc76038)\
  2022-07-01 12:29:16 +0200
  * [MDEV-28967](https://jira.mariadb.org/browse/MDEV-28967) Assertion `marked_for_write_or_computed()' failed in Field_new_decimal::store_value / online_alter_read_from_binlog`
* [Revision #f562f773a3](https://github.com/MariaDB/server/commit/f562f773a3)\
  2022-06-30 18:26:54 +0200
  * remove redundant warnings in RBR and online alter
* [Revision #01b3cb2f46](https://github.com/MariaDB/server/commit/01b3cb2f46)\
  2022-06-30 17:07:56 +0200
  * cleanup: whitespace, etc
* [Revision #93049e3de6](https://github.com/MariaDB/server/commit/93049e3de6)\
  2022-06-30 12:12:00 +0200
  * [MDEV-28959](https://jira.mariadb.org/browse/MDEV-28959) Online alter ignores strict table mode
* [Revision #13f1e970a1](https://github.com/MariaDB/server/commit/13f1e970a1)\
  2022-06-29 16:58:33 +0200
  * [MDEV-28944](https://jira.mariadb.org/browse/MDEV-28944) XA assertions failing in binlog\_rollback and binlog\_commit
* [Revision #8f6f219a68](https://github.com/MariaDB/server/commit/8f6f219a68)\
  2023-08-11 02:13:45 +0400
  * control Cache\_flip\_event\_log lifetime with reference count
* [Revision #62a1e282d0](https://github.com/MariaDB/server/commit/62a1e282d0)\
  2022-06-29 16:57:22 +0200
  * [MDEV-28771](https://jira.mariadb.org/browse/MDEV-28771) Assertion \`table->in\_use&\&tdc->flushed' failed after ALTER
* [Revision #754333e6ad](https://github.com/MariaDB/server/commit/754333e6ad)\
  2022-06-29 18:08:50 +0200
  * test rename alter\_table\_online -> alter\_table\_online\_debug
* [Revision #64b55151f4](https://github.com/MariaDB/server/commit/64b55151f4)\
  2022-06-29 18:01:20 +0200
  * separate online\_alter\_cache\_data from binlog\_cache\_data
* [Revision #e358d5ee20](https://github.com/MariaDB/server/commit/e358d5ee20)\
  2022-06-29 16:55:44 +0200
  * put binlog\_cache\_data on a memroot
* [Revision #8cdd661341](https://github.com/MariaDB/server/commit/8cdd661341)\
  2022-06-05 14:39:30 +0200
  * Online alter: always commit for non-trans engines
* [Revision #5a867d847c](https://github.com/MariaDB/server/commit/5a867d847c)\
  2021-12-14 18:04:24 +0300
  * Online alter: savepoints
* [Revision #b2be2e39a6](https://github.com/MariaDB/server/commit/b2be2e39a6)\
  2022-06-01 21:52:27 +0200
  * don't crash if ALTER TABLE fails and a long transaction blocks MDL upgrade
* [Revision #332f41aae3](https://github.com/MariaDB/server/commit/332f41aae3)\
  2022-05-29 13:31:20 +0200
  * don't copy stmt IO\_CACHE to trx IO\_CACHE at the stmt end
* [Revision #3099a756ab](https://github.com/MariaDB/server/commit/3099a756ab)\
  2022-06-02 14:57:56 +0200
  * don't do DROP SYSTEM VERSIONING online
* [Revision #32c3d775e9](https://github.com/MariaDB/server/commit/32c3d775e9)\
  2022-05-31 22:06:27 +0200
  * Online alter: set read\_set early, before row reads
* [Revision #df0771c6a2](https://github.com/MariaDB/server/commit/df0771c6a2)\
  2022-05-31 11:17:17 +0200
  * no ALTER TABLE should return ER\_NO\_DEFAULT\_FOR\_FIELD
* [Revision #a5776aa341](https://github.com/MariaDB/server/commit/a5776aa341)\
  2022-05-25 22:08:40 +0200
  * online alter always uses ALGORITHM=COPY, LOCK=NONE
* [Revision #d767ed5c89](https://github.com/MariaDB/server/commit/d767ed5c89)\
  2022-05-25 19:20:30 +0200
  * remove handler::open\_read\_view()
* [Revision #0b67af5a81](https://github.com/MariaDB/server/commit/0b67af5a81)\
  2022-05-24 21:11:48 +0200
  * cleanup
* [Revision #a8a22b7af2](https://github.com/MariaDB/server/commit/a8a22b7af2)\
  2022-05-24 20:10:48 +0200
  * support 'alter online table t1 page\_checksum=0'
* [Revision #6c57e29b17](https://github.com/MariaDB/server/commit/6c57e29b17)\
  2022-05-25 22:22:03 +0200
  * tests: move around, add new
* [Revision #ab4bfad206](https://github.com/MariaDB/server/commit/ab4bfad206)\
  2020-11-26 21:08:58 +1000
  * [MDEV-16329](https://jira.mariadb.org/browse/MDEV-16329) \[5/5] ALTER ONLINE TABLE
* [Revision #d2d0995cf2](https://github.com/MariaDB/server/commit/d2d0995cf2)\
  2021-12-12 11:41:14 +0300
  * [MDEV-16329](https://jira.mariadb.org/browse/MDEV-16329) \[4/5] Refactor MYSQL\_BIN\_LOG: extract Event\_log ancestor
* [Revision #6427e343cf](https://github.com/MariaDB/server/commit/6427e343cf)\
  2020-11-25 00:03:53 +1000
  * [MDEV-16329](https://jira.mariadb.org/browse/MDEV-16329) \[3/5] use binlog\_cache\_data directly in most places
* [Revision #429f635f30](https://github.com/MariaDB/server/commit/429f635f30)\
  2020-10-06 19:56:03 +1000
  * [MDEV-16329](https://jira.mariadb.org/browse/MDEV-16329) \[2/5] refactor binlog and cache\_mngr
* [Revision #0dfbb05cd0](https://github.com/MariaDB/server/commit/0dfbb05cd0)\
  2020-03-04 17:27:38 +1000
  * [MDEV-16329](https://jira.mariadb.org/browse/MDEV-16329) \[1/5] add THD::binlog\_get\_cache\_mngr
* [Revision #f5e5013799](https://github.com/MariaDB/server/commit/f5e5013799)\
  2021-12-13 05:35:22 +0300
  * rpl: repack table\_def
* [Revision #af83d06d68](https://github.com/MariaDB/server/commit/af83d06d68)\
  2020-11-26 20:59:44 +1000
  * Copy\_field: add const to arguments
* [Revision #251102600a](https://github.com/MariaDB/server/commit/251102600a)\
  2022-05-25 22:36:25 +0200
  * rename tests
* [Revision #0b6066d021](https://github.com/MariaDB/server/commit/0b6066d021)\
  2022-05-24 14:32:51 +0200
  * binlog\_combinations.inc -> binlog\_format\_combinations.inc
* [Revision #275684d8fe](https://github.com/MariaDB/server/commit/275684d8fe)\
  2022-11-27 17:03:29 +0100
  * cleanup: remove vcol\_info->stored\_in\_db
* [Revision #9545eb969e](https://github.com/MariaDB/server/commit/9545eb969e)\
  2022-11-06 11:26:28 +0100
  * Fix recalculation of vcols in binlog\_row\_image=minimal
* [Revision #e499b25c65](https://github.com/MariaDB/server/commit/e499b25c65)\
  2022-11-06 15:33:46 +0100
  * cleanup: clarify ha\_innobase::column\_bitmaps\_signal()
* [Revision #eaa87eb89f](https://github.com/MariaDB/server/commit/eaa87eb89f)\
  2023-02-20 14:01:08 +0100
  * allow random\_bytes() in virtual columns
* [Revision #ffc0886341](https://github.com/MariaDB/server/commit/ffc0886341)\
  2023-08-11 17:04:12 +0200
  * update results for new UUID sorting
* [Revision #66f0f2f2d5](https://github.com/MariaDB/server/commit/66f0f2f2d5)\
  2023-08-11 16:48:54 +0200
  * bump the VERSION
* [Revision #4e87081b56](https://github.com/MariaDB/server/commit/4e87081b56)\
  2023-08-09 20:30:52 +0200
  * cleanup: remove useless check
* [Revision #80439e6918](https://github.com/MariaDB/server/commit/80439e6918)\
  2023-08-08 10:58:44 +0200
  * [MDEV-31618](https://jira.mariadb.org/browse/MDEV-31618): Server crashes in process\_i\_s\_table\_temporary\_tables/get\_all\_tables after alter in rename query
* [Revision #de57da733f](https://github.com/MariaDB/server/commit/de57da733f)\
  2023-08-02 17:46:33 +0200
  * [MDEV-28351](https://jira.mariadb.org/browse/MDEV-28351): Assertion \`this->file->children\_attached' failed in ha\_myisammrg::info
* [Revision #82d9d72fb1](https://github.com/MariaDB/server/commit/82d9d72fb1)\
  2023-07-19 13:48:53 +0200
  * [MDEV-31618](https://jira.mariadb.org/browse/MDEV-31618): Server crashes in process\_i\_s\_table\_temporary\_tables/get\_all\_tables
* [Revision #62decb5e8b](https://github.com/MariaDB/server/commit/62decb5e8b)\
  2023-06-17 13:17:18 +0200
  * [MDEV-12459](https://jira.mariadb.org/browse/MDEV-12459) post-review fixes
* [Revision #1fb4828b28](https://github.com/MariaDB/server/commit/1fb4828b28)\
  2022-07-16 13:33:15 +0200
  * [MDEV-28343](https://jira.mariadb.org/browse/MDEV-28343): sys.create\_synonym\_db fails with ER\_VIEW\_SELECT\_TMPTABLE when schema contains temporary tables
* [Revision #91bfc76fe1](https://github.com/MariaDB/server/commit/91bfc76fe1)\
  2023-06-08 13:21:09 +0200
  * [MDEV-28351](https://jira.mariadb.org/browse/MDEV-28351) Assertion \`this->file->children\_attached' failed in ha\_myisammrg::info
* [Revision #1923ff8e41](https://github.com/MariaDB/server/commit/1923ff8e41)\
  2023-06-07 13:23:25 +0200
  * [MDEV-12459](https://jira.mariadb.org/browse/MDEV-12459) Patch sysschema
* [Revision #0b7d1748ad](https://github.com/MariaDB/server/commit/0b7d1748ad)\
  2023-06-07 11:49:01 +0200
  * [MDEV-12459](https://jira.mariadb.org/browse/MDEV-12459) Get temporary tables visible to the IS.tables for current connection
* [Revision #1c052e9011](https://github.com/MariaDB/server/commit/1c052e9011)\
  2023-06-07 13:33:10 +0200
  * Cosmetic fixes
* [Revision #f329fe1c23](https://github.com/MariaDB/server/commit/f329fe1c23)\
  2023-08-10 17:23:11 +0700
  * [MDEV-31799](https://jira.mariadb.org/browse/MDEV-31799) Unexpected ER\_TRG\_NO\_SUCH\_ROW\_IN\_TRG and server crash after ALTER TABLE
* [Revision #00089ead50](https://github.com/MariaDB/server/commit/00089ead50)\
  2023-07-21 13:37:00 +0200
  * [MDEV-31633](https://jira.mariadb.org/browse/MDEV-31633) Assertion \`!item->null\_value' failed in Type\_handler::Item\_send\_str
* [Revision #5de39c5ae3](https://github.com/MariaDB/server/commit/5de39c5ae3)\
  2023-06-13 13:33:55 +0200
  * [MDEV-9069](https://jira.mariadb.org/browse/MDEV-9069) extend AES\_ENCRYPT() and AES\_DECRYPT() to support IV and the algorithm
* [Revision #f94d467d32](https://github.com/MariaDB/server/commit/f94d467d32)\
  2023-06-18 00:15:36 +0200
  * enable AES-CTR with wolfssl
* [Revision #75f5cc478f](https://github.com/MariaDB/server/commit/75f5cc478f)\
  2023-06-12 22:52:47 +0200
  * [MDEV-30905](https://jira.mariadb.org/browse/MDEV-30905) Remove old\_alter\_table variable
* [Revision #98de11723c](https://github.com/MariaDB/server/commit/98de11723c)\
  2023-06-17 18:37:22 +0200
  * cleanup: extern -> static
* [Revision #f9003c73a1](https://github.com/MariaDB/server/commit/f9003c73a1)\
  2023-08-01 15:44:14 +0530
  * [MDEV-14795](https://jira.mariadb.org/browse/MDEV-14795) InnoDB system tablespace cannot be shrunk
* Merge [Revision #e81fa34502](https://github.com/MariaDB/server/commit/e81fa34502) 2023-07-26 15:49:24 +0300 - Merge 11.1 into 11.2
* [Revision #742f960eeb](https://github.com/MariaDB/server/commit/742f960eeb)\
  2023-03-09 20:05:17 +0000
  * \[[MDEV-30178](https://jira.mariadb.org/browse/MDEV-30178)] Explicit errors on required secured transport
* [Revision #038d29258d](https://github.com/MariaDB/server/commit/038d29258d)\
  2023-07-25 11:44:16 +0200
  * Fix redundant call to update\_binlog\_end\_pos() (probably merge error).
* [Revision #f612e1c2bc](https://github.com/MariaDB/server/commit/f612e1c2bc)\
  2023-06-17 19:00:56 +0200
  * [MDEV-26182](https://jira.mariadb.org/browse/MDEV-26182) fixes for --ps
* [Revision #49088c914b](https://github.com/MariaDB/server/commit/49088c914b)\
  2022-06-16 15:05:35 +0800
  * [MDEV-26182](https://jira.mariadb.org/browse/MDEV-26182): Implement JSON\_INTERSECT()
* [Revision #15a7b6c0b7](https://github.com/MariaDB/server/commit/15a7b6c0b7)\
  2023-05-25 15:45:43 +0530
  * [MDEV-30145](https://jira.mariadb.org/browse/MDEV-30145): JSON\_TABLE: allow to retrieve the key when iterating on JSON objects
* [Revision #2e092583fe](https://github.com/MariaDB/server/commit/2e092583fe)\
  2023-07-18 08:06:52 +1000
  * [MDEV-31714](https://jira.mariadb.org/browse/MDEV-31714) Debian 50-mariadb\_safe.cnf has syslog enabled
* [Revision #2992d531b0](https://github.com/MariaDB/server/commit/2992d531b0)\
  2023-07-19 18:31:01 +0700
  * [MDEV-31661](https://jira.mariadb.org/browse/MDEV-31661): Assertion \`thd->lex == sp\_instr\_lex' failed in LEX\* sp\_lex\_instr::parse\_expr(THD\*, sp\_head\*, LEX\*)
* [Revision #856196ea59](https://github.com/MariaDB/server/commit/856196ea59)\
  2023-07-19 18:26:09 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): fixes for --view
* [Revision #3a8e769836](https://github.com/MariaDB/server/commit/3a8e769836)\
  2023-07-19 18:23:47 +0700
  * DEV-5816: Stored programs: validation of stored program statements
* [Revision #8a3c62c655](https://github.com/MariaDB/server/commit/8a3c62c655)\
  2023-07-19 18:22:31 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #ec04357bf9](https://github.com/MariaDB/server/commit/ec04357bf9)\
  2023-07-19 18:21:27 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #6abc16cbf7](https://github.com/MariaDB/server/commit/6abc16cbf7)\
  2023-07-19 18:19:17 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #1ee1979ed6](https://github.com/MariaDB/server/commit/1ee1979ed6)\
  2023-07-19 18:17:19 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #a0b4e0f816](https://github.com/MariaDB/server/commit/a0b4e0f816)\
  2023-07-19 18:14:00 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #9e599235a5](https://github.com/MariaDB/server/commit/9e599235a5)\
  2023-07-19 18:11:36 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #6ac1d882a1](https://github.com/MariaDB/server/commit/6ac1d882a1)\
  2023-07-19 18:06:59 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #2086f96c6b](https://github.com/MariaDB/server/commit/2086f96c6b)\
  2023-07-19 18:00:13 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #465c81b323](https://github.com/MariaDB/server/commit/465c81b323)\
  2023-07-19 17:57:13 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #5a8b9a16d1](https://github.com/MariaDB/server/commit/5a8b9a16d1)\
  2023-07-19 17:53:55 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #6840af6e01](https://github.com/MariaDB/server/commit/6840af6e01)\
  2023-07-19 17:50:47 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #40d730fba0](https://github.com/MariaDB/server/commit/40d730fba0)\
  2023-07-19 17:48:31 +0700
  * DEV-5816: Stored programs: validation of stored program statements
* [Revision #66d88176e9](https://github.com/MariaDB/server/commit/66d88176e9)\
  2023-07-19 17:47:08 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #9f34225ec4](https://github.com/MariaDB/server/commit/9f34225ec4)\
  2023-07-19 17:45:39 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #9e48460bdb](https://github.com/MariaDB/server/commit/9e48460bdb)\
  2023-07-19 17:43:31 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #053475fe4f](https://github.com/MariaDB/server/commit/053475fe4f)\
  2023-06-13 18:25:53 +0700
  * [MDEV-5816](https://jira.mariadb.org/browse/MDEV-5816): Stored programs: validation of stored program statements
* [Revision #c5405c075f](https://github.com/MariaDB/server/commit/c5405c075f)\
  2023-06-16 17:44:36 -0400
  * A procedure and script to speed up translation of MariaDB error messages to a new language
* [Revision #75f25e4ca7](https://github.com/MariaDB/server/commit/75f25e4ca7)\
  2022-12-14 18:46:27 +0400
  * [MDEV-30164](https://jira.mariadb.org/browse/MDEV-30164) System variable for default collations
* [Revision #584c2351de](https://github.com/MariaDB/server/commit/584c2351de)\
  2023-03-06 14:31:32 +0000
  * [MDEV-15736](https://jira.mariadb.org/browse/MDEV-15736) Remove mariadb-admin --vertical
* [Revision #b8c039fad1](https://github.com/MariaDB/server/commit/b8c039fad1)\
  2023-06-18 22:55:54 +0200
  * [MDEV-30188](https://jira.mariadb.org/browse/MDEV-30188): fixes for 32-bit
* [Revision #a63c558b20](https://github.com/MariaDB/server/commit/a63c558b20)\
  2023-04-04 00:21:28 +0000
  * Implement mysql\_upgrade upgrade testing in CI
* [Revision #9b431d714f](https://github.com/MariaDB/server/commit/9b431d714f)\
  2023-07-04 17:56:27 +1000
  * [MDEV-26137](https://jira.mariadb.org/browse/MDEV-26137) Improve import tablespace workflow.
* Merge [Revision #b7ee3c7b9c](https://github.com/MariaDB/server/commit/b7ee3c7b9c) 2023-07-04 08:22:18 +0300 - Merge 11.1 into 11.2
* Merge [Revision #2867894ac6](https://github.com/MariaDB/server/commit/2867894ac6) 2023-06-28 09:39:28 +0300 - Merge 11.1 into 11.2
* [Revision #dbc3429592](https://github.com/MariaDB/server/commit/dbc3429592)\
  2023-03-16 02:48:23 -0400
  * Fix encryption calls with overlapping buffers
* [Revision #b91d5bcedc](https://github.com/MariaDB/server/commit/b91d5bcedc)\
  2023-01-12 04:58:16 -0500
  * [MDEV-30389](https://jira.mariadb.org/browse/MDEV-30389) Ensure correct dlen during encryption
* [Revision #01e9e3955a](https://github.com/MariaDB/server/commit/01e9e3955a)\
  2023-05-23 09:03:53 +0300
  * [MDEV-31242](https://jira.mariadb.org/browse/MDEV-31242): Make sure every Debian post/pre script is using bash
* [Revision #34bbf37f4f](https://github.com/MariaDB/server/commit/34bbf37f4f)\
  2023-03-17 16:34:10 +0000
  * [MDEV-30188](https://jira.mariadb.org/browse/MDEV-30188): Ensure all binlog\* variables are visible as system variables Turn the remaining three `binlog*` options binlog\_do\_db, binlog\_ignore\_db, binlog\_rows\_event\_max\_size into global variables so that they can be visible from the SQL user level. This is for audit / secure configuration check purposes.
* Merge [Revision #907bc68d5f](https://github.com/MariaDB/server/commit/907bc68d5f) 2023-06-11 10:45:10 +0200 - Merge branch '11.1' into 11.2
* [Revision #5aebc0e195](https://github.com/MariaDB/server/commit/5aebc0e195)\
  2023-04-19 16:25:09 +0200
  * 11.2 branch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
