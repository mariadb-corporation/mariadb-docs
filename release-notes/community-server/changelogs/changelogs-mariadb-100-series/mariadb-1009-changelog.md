# MariaDB 10.0.9 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.9) |[Release Notes](../../old-releases/10.0/10.0.9.md) |**Changelog** |[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 10 Mar 2014

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.9.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4040](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4040)\
  Sat 2014-03-08 12:33:51 +0100
  * default xtradb - fixes for debian packaging
* [Revision #4039](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4039)\
  Fri 2014-03-07 21:05:28 +0100
  * @@old\_mode=zero\_date\_time\_cast
* [Revision #4038](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4038)\
  Fri 2014-03-07 17:47:47 +0100
  * workaround for xtradb on gcc 4.1.2 RHEL5/x86, gcc atomic ops only work under -march=i686
* [Revision #4037](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4037)\
  Fri 2014-03-07 15:21:07 +0100
  * XtraDB made the default
* [Revision #4036](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4036)\
  Fri 2014-03-07 12:08:38 +0100
  * [MDEV-5789](https://jira.mariadb.org/browse/MDEV-5789): race between rpl\_parallel\_change\_thread\_count and slave start upon server start without --skip-slave-start
* [Revision #4035](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4035)\
  Fri 2014-03-07 12:02:09 +0100
  * [MDEV-5788](https://jira.mariadb.org/browse/MDEV-5788): Incorrect free of rgi->deferred\_events in parallel replication
* [Revision #4034](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4034)\
  Fri 2014-03-07 10:34:07 +0400
  * Do not use SECONDS\_IN\_24H in nt\_servc.cc. This constant uses my\_time.h, which inclusion is not desirable in nt\_servc.cc
* [Revision #4033](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4033)\
  Fri 2014-03-07 00:21:25 +0400
  * [MDEV-5372](https://jira.mariadb.org/browse/MDEV-5372) Make "CAST(time\_expr AS DATETIME)" compatible with MySQL-5.6 (and the SQL Standard)
* [Revision #4032](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4032)\
  Thu 2014-03-06 16:19:12 +0400
  * [MDEV-5675](https://jira.mariadb.org/browse/MDEV-5675) - Performance: `my_hash_sort_bin` is called too often
* [Revision #4031](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4031)\
  Thu 2014-03-06 11:47:22 +0100
  * [MDEV-4603](https://jira.mariadb.org/browse/MDEV-4603) `mysql_stmt_reset` returns "commands out of sync" error
* [Revision #4030](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4030) \[merge]\
  Wed 2014-03-05 23:20:10 +0100
  * 10.0-base merge
  * [Revision #3427.43.13](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.13)\
    Wed 2014-03-05 02:10:06 +0400
    * [MDEV-5723](https://jira.mariadb.org/browse/MDEV-5723): `mysqldump -uroot` unusable for multi-database operations, checks all databases
    * MariaDB-5.5 part of the fix: since we can't easily fix query optimization for `I_S` tables, run the affected-tablespaces query with `semijoin=off`. It happens to have a good query plan with that setting. \[This is a forward-port to [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)]
  * [Revision #3427.43.12](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.12) \[merge]\
    Wed 2014-03-05 01:57:57 +0400
    * Merge
    * [Revision #3427.46.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.46.2)\
      Tue 2014-03-04 15:14:40 +0400
      * [MDEV-5723](https://jira.mariadb.org/browse/MDEV-5723): `mysqldump -uroot` unusable for multi-database operations, checks all databases
      * Make `do_fill_table()` use `join_tab->cache_select->cond` if it is present. When `join_tab->cache_select->cond` is present, `join_tab->select_cond` doesn't have any conditions that are usable for `I_S` optimizations.
    * [Revision #3427.46.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.46.1)\
      Tue 2014-03-04 00:41:50 +0400
      * [MDEV-5778](https://jira.mariadb.org/browse/MDEV-5778): Valgrind failure in `innodb_ext_keys.te`
      * Fix valgrind failure: make `test_if_order_by_key()` account for extended keys feature.
  * [Revision #3427.43.11](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.11)\
    Tue 2014-03-04 14:37:09 +0100
    * [MDEV-5703](https://jira.mariadb.org/browse/MDEV-5703): \[PATCH] Slave disconnects and fails to reconnect on Error\_code: 1159
  * [Revision #3427.43.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.10) \[merge]\
    Tue 2014-03-04 14:21:00 +0100
    * Merge [MDEV-5754](https://jira.mariadb.org/browse/MDEV-5754), [MDEV-5769](https://jira.mariadb.org/browse/MDEV-5769), and [MDEV-5764](https://jira.mariadb.org/browse/MDEV-5764) into 10.0-base
  * [Revision #3427.43.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.9)\
    Thu 2014-02-27 13:54:05 -0800
    * Fixed bug [MDEV-5635](https://jira.mariadb.org/browse/MDEV-5635). After constant row substitution some field items become constant items. The range analyzer should take into account this fact when looking for ranges.
  * [Revision #3427.43.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.8) \[merge]\
    Thu 2014-02-27 13:43:06 +0400
    * Merge
    * [Revision #3427.45.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.45.1)\
      Thu 2014-02-27 13:40:40 +0400
      * Update test results after fix for [MDEV-5732](https://jira.mariadb.org/browse/MDEV-5732)
  * [Revision #3427.43.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.7) \[merge]\
    Wed 2014-02-26 17:03:32 +0100
    * Merge [MDEV-5657](https://jira.mariadb.org/browse/MDEV-5657) (parallel replication) to 10.0-base
  * [Revision #3427.43.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.6) \[merge]\
    Tue 2014-02-25 19:35:00 +0400
    * Merge
    * [Revision #3427.44.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.44.1)\
      Tue 2014-02-25 19:25:49 +0400
      * [MDEV-5732](https://jira.mariadb.org/browse/MDEV-5732): Valgrind warning for `index_merge` and `extended_keys`
      * Make `is_key_scan_ror()` take into account the existence of extended keys.
* [Revision #4029](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4029)\
  Tue 2014-03-04 22:25:34 +0100
  * xtradb, windows, aio: fix the bad merge
* [Revision #4028](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4028)\
  Tue 2014-03-04 20:37:48 +0200
  * Fixed bug found by Pavel Ivanov in `Gtid_log_event`.
  * Removed double call to `trans_begin()` for GTID BEGIN event
  * Don't set `OPTION_BEGIN` before calling `trans_begin()` as this causes extra work in `trans_begin()`
* [Revision #4027](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4027)\
  Tue 2014-03-04 20:32:52 +0200
  * Fixed timing problem in `rpl_heartbeat_basic.test`
* [Revision #4026](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4026) \[merge]\
  Tue 2014-03-04 14:32:42 +0100
  * Merge [MDEV-5754](https://jira.mariadb.org/browse/MDEV-5754), [MDEV-5769](https://jira.mariadb.org/browse/MDEV-5769), and [MDEV-5764](https://jira.mariadb.org/browse/MDEV-5764) into 10.0
  * [Revision #3427.35.245](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.245)\
    Tue 2014-03-04 13:10:14 +0100
    * [MDEV-5754](https://jira.mariadb.org/browse/MDEV-5754): MySQL 5.5 slaves cannot replicate from [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)
  * [Revision #3427.35.244](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.244)\
    Tue 2014-03-04 08:48:32 +0100
    * [MDEV-5769](https://jira.mariadb.org/browse/MDEV-5769): Slave crashes on attempt to do parallel replication from an older master
  * [Revision #3427.35.243](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.243)\
    Mon 2014-03-03 12:13:55 +0100
    * [MDEV-5764](https://jira.mariadb.org/browse/MDEV-5764): START SLAVE UNTIL does not work with parallel replication
* [Revision #4025](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4025)\
  Tue 2014-03-04 01:22:53 +0100
  * [MDEV-5620](https://jira.mariadb.org/browse/MDEV-5620) CMake option to compile against an external PCRE library
* [Revision #4024](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4024)\
  Sun 2014-03-02 19:01:34 +0100
  * [MDEV-5748](https://jira.mariadb.org/browse/MDEV-5748) Assertion `status_var.memory_used == 0` fails on disconnect after opening an OQGRAPH table
* [Revision #4023](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4023)\
  Sun 2014-03-02 15:54:57 +0100
  * [MDEV-5674](https://jira.mariadb.org/browse/MDEV-5674) Valgrind warnings "Conditional jump or move depends on uninitialised value" in `create_sort_index` with small `sort_buffer_size`
* [Revision #4022](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4022)\
  Sun 2014-03-02 15:02:13 +0100
  * [MDEV-5667](https://jira.mariadb.org/browse/MDEV-5667) online alter and changed field/index options
* [Revision #4021](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4021)\
  Sat 2014-03-01 13:27:04 +0100
  * [MDEV-5735](https://jira.mariadb.org/browse/MDEV-5735) Selecting from SEQUENCE table with negative number hangs server
* [Revision #4020](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4020)\
  Sat 2014-03-01 11:55:31 +0100
  * [MDEV-5668](https://jira.mariadb.org/browse/MDEV-5668) Assertion `granted_role->is_role()` fails on granting role with empty name
* [Revision #4019](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4019)\
  Sat 2014-03-01 10:19:42 +0100
  * minor cleanup
* [Revision #4018](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4018)\
  Fri 2014-02-28 21:46:43 +0100
  * update InnoDB version
* [Revision #4017](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4017)\
  Fri 2014-02-28 21:04:58 +0100
  * XtraDB compilation failures on Windows (again)
* [Revision #4016](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4016)\
  Fri 2014-02-28 20:24:22 +0100
  * followup for [MDEV-4309](https://jira.mariadb.org/browse/MDEV-4309): DBT-3 Q1 benchmark: Benchmark + profile a patch don't forget to initialize `ORDER::fast_field_copier_setup`
* [Revision #4015](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4015) \[merge]\
  Fri 2014-02-28 10:00:31 +0100
  * merge
  * [Revision #4007.1.10](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.10)\
    Thu 2014-02-27 22:43:42 +0100
    * [MDEV-4955](https://jira.mariadb.org/browse/MDEV-4955) discover of table non-existance on CREATE
  * [Revision #4007.1.9](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.9)\
    Thu 2014-02-27 12:25:51 +0100
    * [MDEV-5672](https://jira.mariadb.org/browse/MDEV-5672) [MariaDB 10.0.8](../../old-releases/10.0/10.0.8.md) doesn't compile without perfschema
  * [Revision #4007.1.8](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.8)\
    Thu 2014-02-27 12:00:16 +0100
    * [MDEV-4447](https://jira.mariadb.org/browse/MDEV-4447) MariaDB sources should have unix-style line endings everywhere
  * [Revision #4007.1.7](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.7)\
    Thu 2014-02-27 08:43:54 +0100
    * compilation error in CONNECT with ODBC
  * [Revision #4007.1.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.6)\
    Wed 2014-02-26 20:11:00 +0100
    * OQGraph fails in `--embedded`
  * [Revision #4007.1.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.5) \[merge]\
    Wed 2014-02-26 19:36:33 +0100
    * InnoDB 5.6.15 merge. update test results
    * [Revision #0.49.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.49.2)\
      Wed 2014-02-26 19:23:04 +0100
      * 5.6.15
  * [Revision #4007.1.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.4) \[merge]\
    Wed 2014-02-26 19:22:48 +0100
    * null-merge from innodb-5.6 mergetree (as of 5.6.14)
    * [Revision #0.49.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.49.1)\
      Wed 2014-02-26 19:11:54 +0100
      * initial commit into innodb-5.6 mergetree
  * [Revision #4007.1.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.3) \[merge]\
    Wed 2014-02-26 19:21:23 +0100
    * Percona-Server-5.6.15-rel63.0.tar.gz merge
    * [Revision #0.12.68](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/0.12.68)\
      Wed 2014-02-26 16:25:11 +0100
      * Percona-Server-5.6.15-rel63.0.tar.gz
  * [Revision #4007.1.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.2)\
    Wed 2014-02-26 16:22:26 +0100
    * Fix code in `make_sortkey()` that only worked by chance (assert added by MySQL verified that strnxfrm can only _increase_ the string length if from == to, and the latter is a random decision made by individual items and `String::realloc`).
  * [Revision #4007.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007.1.1) \[merge]\
    Wed 2014-02-26 15:28:07 +0100
    * 10.0-base merge
    * [Revision #3427.43.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.5) \[merge]\
      Tue 2014-02-25 16:04:35 +0100
      * 5.5 merge
    * [Revision #3427.43.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.4)\
      Tue 2014-02-25 13:01:57 +0400
      * Update test results after the previous push
    * [Revision #3427.43.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.3)\
      Tue 2014-02-25 01:18:13 +0400
      * [MDEV-5244](https://jira.mariadb.org/browse/MDEV-5244): Make `extended_keys=ON` by default in 10.0
      * Change the default flag value to ON.
      * Update the testcases to be run `extended_keys=ON`:
        * trivial test result updates
        * If `extended_keys` setting makes a difference for a testcase, run the testcase with extended\_keys=off. There were only a few such cases
      * Update to `vcol_select_innodb` looks like a worse plan but it will be gone in 10.0.
    * [Revision #3427.43.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.2)\
      Wed 2014-02-12 21:37:58 +0400
      * Backport from 10.0 to 10.0-base the following:
        * revision-id: psergey@askmonty.org-20140204092710-2yt5ysa5ej3l2c03 [MDEV-5606](https://jira.mariadb.org/browse/MDEV-5606): range optimizer: "x < y" is sargable, while "y > x" is not Port to mariadb-1.0 the following fix from mysql-5.6:
        * Revision ID: jorgen.loland@oracle.com-20120314131055-ml54x9deueqfsff4 BUG#13701206: WHERE A>=B DOES NOT GIVE SAME EXECUTION PLAN AS WHERE B<=A (RANGE OPTIMIZER)
        * that fix didn't have a public testcase, so I created one.
    * [Revision #3427.43.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.43.1)\
      Tue 2014-02-11 19:22:17 -0800
      * Fixed bug [MDEV-5630](https://jira.mariadb.org/browse/MDEV-5630). The function `calculate_cond_selectivity_for_table()` must consider the case when the key range tree returned by the call of `get_mm_tree()` is of the type `SEL_TREE::ALWAYS`.
* [Revision #4014](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4014)\
  Thu 2014-02-27 19:44:00 +0400
  * Fixing AIX compilation failires
* [Revision #4013](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4013)\
  Thu 2014-02-27 16:41:49 +0200
  * Enable windows builds for XtraDB.
* [Revision #4012](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4012)\
  Thu 2014-02-27 14:31:39 +0400
  * [MDEV-5744](https://jira.mariadb.org/browse/MDEV-5744) OQGRAPH backing table changes not reflected in OQGRAPH table
* [Revision #4011](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4011)\
  Thu 2014-02-27 08:21:41 +0100
  * [MDEV-5728](https://jira.mariadb.org/browse/MDEV-5728): [BINLOG\_GTID\_POS(..)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/binlog_gtid_pos) does not return proper error unless `mysql_store_result` is called
* [Revision #4010](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4010) \[merge]\
  Wed 2014-02-26 16:54:08 +0100
  * Merge [MDEV-5657](https://jira.mariadb.org/browse/MDEV-5657) (parallel replication) to 10.0
  * [Revision #4008.1.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4008.1.1) \[merge]\
    Wed 2014-02-26 16:38:42 +0100
    * Merge [MDEV-5657](https://jira.mariadb.org/browse/MDEV-5657) (parallel replication) to 10.0
    * [Revision #3427.35.242](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.242)\
      Wed 2014-02-26 15:02:09 +0100
      * [MDEV-5657](https://jira.mariadb.org/browse/MDEV-5657): Parallel replication.
* [Revision #4009](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4009)\
  Wed 2014-02-26 15:46:13 +0200
  * [MDEV-4309](https://jira.mariadb.org/browse/MDEV-4309): DBT-3 Q1 benchmark: Benchmark + profile a patch
* [Revision #4008](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4008)\
  Wed 2014-02-26 12:55:28 +0400
  * [MDEV-5612](https://jira.mariadb.org/browse/MDEV-5612) - `my_rename()` deletes files when it shouldn't
* [Revision #4007](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4007)\
  Sat 2014-02-22 03:11:56 +0200
  * Fixed that `rpl_row_create_table` can be run with `--ps-protocol`
* [Revision #4006](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4006)\
  Wed 2014-02-19 14:05:15 +0400
  * [MDEV-5314](https://jira.mariadb.org/browse/MDEV-5314) - Compiling fails on OSX using clang
* [Revision #4005](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4005)\
  Thu 2014-02-13 11:13:55 +0400
  * [MDEV-5597](https://jira.mariadb.org/browse/MDEV-5597) - Reduce usage of `LOCK_open: LOCK_flush`
* [Revision #4004](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4004)\
  Thu 2014-02-13 10:44:10 +0400
  * [MDEV-5492](https://jira.mariadb.org/browse/MDEV-5492) - Reduce usage of `LOCK_open: TABLE::in_use`
* [Revision #4003](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4003)\
  Thu 2014-02-13 10:19:37 +0400
  * [MDEV-5403](https://jira.mariadb.org/browse/MDEV-5403) - Reduce usage of `LOCK_open: tc_count`
* [Revision #4002](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4002)\
  Wed 2014-02-12 00:06:44 +0200
  * Changed " to ' around connection name (safer)
* [Revision #4001](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4001)\
  Tue 2014-02-11 23:41:56 +0200
  * Fixed that `--apply-slave-statements` also uses multi-source
* [Revision #4000](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/4000) \[merge]\
  Tue 2014-02-11 19:45:38 +0200
  * Automatic merge
  * [Revision #3427.35.241](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.241)\
    Tue 2014-02-11 18:45:49 +0200
    * Fixed test case as gtid events are not counted anymore
  * [Revision #3427.35.240](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.240)\
    Tue 2014-02-11 18:08:02 +0200
    * Fixed wrong result file
* [Revision #3999](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3999)\
  Tue 2014-02-11 19:42:18 +0200
  * Fixed [MDEV-4551](https://jira.mariadb.org/browse/MDEV-4551): `mysqldump --dump-slave` fails with multi-source replication
* [Revision #3998](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3998)\
  Tue 2014-02-11 19:40:33 +0200
  * Fixed [MDEV-3815](https://jira.mariadb.org/browse/MDEV-3815): Aria engine return "The table is full" (ERROR 1114) inserting record, while MyISAM and InnoDB doesn't
* [Revision #3997](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3997) \[merge]\
  Tue 2014-02-11 14:21:48 +0100
  * Merge 10.0-base -> 10.0
  * [Revision #3427.35.239](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.239)\
    Tue 2014-02-11 14:06:03 +0100
    * [MDEV-4937](https://jira.mariadb.org/browse/MDEV-4937): `sql_slave_skip_counter` does not work with GTID
* [Revision #3996](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3996)\
  Tue 2014-02-11 01:51:48 +0400
  * Increase version number
* [Revision #3995](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3995) \[merge]\
  Mon 2014-02-10 15:12:17 +0100
  * Merge [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)-base to 10.0.
  * [Revision #3427.35.238](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.238)\
    Mon 2014-02-10 12:53:04 +0100
    * Fix `check_testcase` complaints due to missing `SET debug_sync=RESET` in a few tests.
  * [Revision #3427.35.237](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.237) \[merge]\
    Mon 2014-02-10 12:39:26 +0100
    * Merge of [MDEV-4984](https://jira.mariadb.org/browse/MDEV-4984), [MDEV-4726](https://jira.mariadb.org/browse/MDEV-4726), and [MDEV-5636](https://jira.mariadb.org/browse/MDEV-5636) into 10.0-base.
    * [Revision #3427.42.6](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.42.6)\
      Sun 2014-02-09 11:15:45 +0100
      * [MDEV-4726](https://jira.mariadb.org/browse/MDEV-4726): Race in `mysql-test/suite/rpl/t/rpl_gtid_stop_start.test`
    * [Revision #3427.42.5](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.42.5)\
      Sun 2014-02-09 00:56:18 +0100
      * [MDEV-5636](https://jira.mariadb.org/browse/MDEV-5636): Deadlock in RESET MASTER
    * [Revision #3427.42.4](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.42.4)\
      Sat 2014-02-08 22:28:41 +0100
      * [MDEV-4984](https://jira.mariadb.org/browse/MDEV-4984): Implement [MASTER\_GTID\_WAIT()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/master_gtid_wait) and [@@LAST\_GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid).
    * [Revision #3427.42.3](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.42.3)\
      Sat 2014-02-08 01:16:45 +0100
      * [MDEV-4984](https://jira.mariadb.org/browse/MDEV-4984): Implement `MASTER_GTID_WAIT()` and `@@LAST_GTID`.
    * [Revision #3427.42.2](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.42.2)\
      Fri 2014-02-07 20:24:39 +0100
      * [MDEV-4726](https://jira.mariadb.org/browse/MDEV-4726): Race in `mysql-test/suite/rpl/t/rpl_gtid_stop_start.test`
    * [Revision #3427.42.1](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.42.1)\
      Fri 2014-02-07 19:15:28 +0100
      * [MDEV-4984](https://jira.mariadb.org/browse/MDEV-4984): Implement `MASTER_GTID_WAIT()` and `@@LAST_GTID`.
  * [Revision #3427.35.236](https://bazaar.launchpad.net/~maria-captains/maria/10.0/revision/3427.35.236)\
    Wed 2014-01-08 11:00:44 +0100
    * [MDEV-5509](https://jira.mariadb.org/browse/MDEV-5509): `Seconds_behind_master` incorrect in parallel replication

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
