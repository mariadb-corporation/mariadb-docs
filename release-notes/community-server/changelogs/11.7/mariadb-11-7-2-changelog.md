# MariaDB 11.7.2 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-2-release-notes.md)[Changelog](mariadb-11-7-2-changelog.md)[Overview of 11.7](../../old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.7.2/)

**Release date:** 13 Feb 2025

For the highlights of this release, see the [release notes](../../old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-2-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.7) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 11.6.2](../11.6/mariadb-11-6-2-changelog.md)
* Includes all fixes from [MariaDB 11.4.5](../11.4/11.4.5.md)
* [Revision #80067a69fe](https://github.com/MariaDB/server/commit/80067a69fe)\
  2025-02-10 22:22:39 +0200
  * [MDEV-36057](https://jira.mariadb.org/browse/MDEV-36057): Assertion failure on 2nd execution of parameterized PS
* [Revision #2d971709a8](https://github.com/MariaDB/server/commit/2d971709a8)\
  2025-02-10 15:25:09 +0100
  * [MDEV-36026](https://jira.mariadb.org/browse/MDEV-36026) Problem with INSERT SELECT on NOT NULL columns while having BEFORE UPDATE trigger
* [Revision #2b17265ae2](https://github.com/MariaDB/server/commit/2b17265ae2)\
  2025-02-09 17:10:05 +0100
  * [MDEV-35186](https://jira.mariadb.org/browse/MDEV-35186) IGNORED attribute has no effect on vector keys
* [Revision #55d1f6c229](https://github.com/MariaDB/server/commit/55d1f6c229)\
  2024-11-13 16:46:29 +0400
  * [MDEV-35069](https://jira.mariadb.org/browse/MDEV-35069) IMPORT TABLESPACE does not work for tables with vector, although allowed
* [Revision #e240da3b19](https://github.com/MariaDB/server/commit/e240da3b19)\
  2025-02-06 21:46:53 +0100
  * [MDEV-35146](https://jira.mariadb.org/browse/MDEV-35146) Vector-related error messages worth improving when possible
* [Revision #a37eb6d013](https://github.com/MariaDB/server/commit/a37eb6d013)\
  2025-02-03 19:33:59 +0100
  * [MDEV-35792](https://jira.mariadb.org/browse/MDEV-35792) Adding a regular index on a vector column leads to invalid table structure
* [Revision #1ea79d1774](https://github.com/MariaDB/server/commit/1ea79d1774)\
  2025-02-03 18:27:13 +0100
  * [MDEV-35317](https://jira.mariadb.org/browse/MDEV-35317) Server crashes in mhnsw\_insert upon using vector key on a Spider table
* [Revision #40d39b1176](https://github.com/MariaDB/server/commit/40d39b1176)\
  2025-02-03 15:19:30 +0100
  * [MDEV-35221](https://jira.mariadb.org/browse/MDEV-35221) Vector values do not survive mariadb-dump / restore
* [Revision #a2f0234c82](https://github.com/MariaDB/server/commit/a2f0234c82)\
  2025-02-03 12:27:03 +0100
  * [MDEV-36011](https://jira.mariadb.org/browse/MDEV-36011) Server crashes in Charset::mbminlen / Item\_func\_vec\_fromtext::val\_str upon mixing vector type with string
* [Revision #6fc75e0868](https://github.com/MariaDB/server/commit/6fc75e0868)\
  2025-02-03 12:08:10 +0100
  * [MDEV-35922](https://jira.mariadb.org/browse/MDEV-35922) Server crashes in mhnsw\_read\_first upon using vector key with views
* [Revision #69041af67d](https://github.com/MariaDB/server/commit/69041af67d)\
  2025-02-02 22:51:12 +0100
  * only enforce innodb\_force\_primary\_key when a table is created
* [Revision #5b8c087e84](https://github.com/MariaDB/server/commit/5b8c087e84)\
  2025-02-02 20:13:57 +0100
  * [MDEV-36005](https://jira.mariadb.org/browse/MDEV-36005) Server crashes when checking/updating a table having vector key after enabling innodb\_force\_primary\_key
* [Revision #e928bf1c0e](https://github.com/MariaDB/server/commit/e928bf1c0e)\
  2024-11-01 12:04:49 +0400
  * [MDEV-35292](https://jira.mariadb.org/browse/MDEV-35292) - ALTER TABLE re-creating vector key is no-op with non-copying alter algorithms (default)
* [Revision #c453391187](https://github.com/MariaDB/server/commit/c453391187)\
  2025-01-15 09:57:49 +0100
  * [MDEV-35834](https://jira.mariadb.org/browse/MDEV-35834) Server crash in FVector::distance\_to upon concurrent SELECT
* [Revision #44d0f5864e](https://github.com/MariaDB/server/commit/44d0f5864e)\
  2025-02-05 22:21:37 +0100
  * fix the test case
* [Revision #adc1beb868](https://github.com/MariaDB/server/commit/adc1beb868)\
  2025-02-05 22:19:42 +0100
  * relax the assert
* [Revision #fe31424e00](https://github.com/MariaDB/server/commit/fe31424e00)\
  2025-02-06 16:47:52 +0100
  * fix sporadic test failures caused by InnoDB #record estimation
* Merge [Revision #ba01c2aaf0](https://github.com/MariaDB/server/commit/ba01c2aaf0) 2025-02-06 16:46:02 +0100 - Merge branch '11.4' into 11.7
* [Revision #14a80f0929](https://github.com/MariaDB/server/commit/14a80f0929)\
  2025-02-03 14:58:58 +0200
  * [MDEV-35318](https://jira.mariadb.org/browse/MDEV-35318) Assertion \`tl->jtbm\_subselect' failed... - PART 2
* [Revision #0e21ff8ca4](https://github.com/MariaDB/server/commit/0e21ff8ca4)\
  2025-01-20 17:44:51 +0200
  * [MDEV-35318](https://jira.mariadb.org/browse/MDEV-35318) Assertion \`tl->jtbm\_subselect' failed in JOIN::calc\_allowed\_top\_level\_tables
* [Revision #491e2b17a9](https://github.com/MariaDB/server/commit/491e2b17a9)\
  2025-01-29 00:25:12 +0400
  * [MDEV-35081](https://jira.mariadb.org/browse/MDEV-35081) - Assertion \`!n\_mysql\_tables\_in\_use' failed after error upon binary logging of DML involving vector table
* [Revision #697b88bf75](https://github.com/MariaDB/server/commit/697b88bf75)\
  2025-01-22 17:31:30 -0700
  * SHOW REPLICA STATUS: mark columns as unsigned
* [Revision #aaa02f6aa3](https://github.com/MariaDB/server/commit/aaa02f6aa3)\
  2025-01-31 14:02:44 -0700
  * [MDEV-35693](https://jira.mariadb.org/browse/MDEV-35693): Improve SHOW REPLICA STATUS column sizes
* [Revision #01fafd45eb](https://github.com/MariaDB/server/commit/01fafd45eb)\
  2025-01-26 09:17:20 -0700
  * [MDEV-35939](https://jira.mariadb.org/browse/MDEV-35939): rpl.rpl\_parallel\_sbm: "Slave\_last\_event\_time is not equal to Master\_last\_event\_time"
* [Revision #195dcfec6f](https://github.com/MariaDB/server/commit/195dcfec6f)\
  2025-01-17 08:42:17 +0100
  * [MDEV-35793](https://jira.mariadb.org/browse/MDEV-35793): Server crashes in Item\_func\_vec\_distance\_common::get\_const\_arg
* [Revision #9171ef3faf](https://github.com/MariaDB/server/commit/9171ef3faf)\
  2024-12-11 18:59:39 +1100
  * [MDEV-35557](https://jira.mariadb.org/browse/MDEV-35557) Fix SEGV when reading from ALTERed mysql.servers table
* [Revision #e02e24dff2](https://github.com/MariaDB/server/commit/e02e24dff2)\
  2024-12-15 23:53:00 +0400
  * [MDEV-35338](https://jira.mariadb.org/browse/MDEV-35338) - Non-copying ALTER does not pad VECTOR column, vector search further does not work
* [Revision #8ef37ade17](https://github.com/MariaDB/server/commit/8ef37ade17)\
  2025-01-06 20:26:06 +0100
  * [MDEV-35745](https://jira.mariadb.org/browse/MDEV-35745) Assertion failure, ASAN errors, crash in mhnsw\_read\_first/mhnsw\_read\_next
* [Revision #0eaefafbaf](https://github.com/MariaDB/server/commit/0eaefafbaf)\
  2025-01-04 17:27:55 +0100
  * [MDEV-35769](https://jira.mariadb.org/browse/MDEV-35769) ER\_SQL\_DISCOVER\_ERROR upon updating vector key column using incorrect value
* [Revision #cca243bf02](https://github.com/MariaDB/server/commit/cca243bf02)\
  2025-01-04 14:42:01 +0100
  * [MDEV-35768](https://jira.mariadb.org/browse/MDEV-35768) Vector key is not used upon selecting from views / subqueries
* [Revision #61806af658](https://github.com/MariaDB/server/commit/61806af658)\
  2024-12-29 17:54:52 +0100
  * [MDEV-35417](https://jira.mariadb.org/browse/MDEV-35417) InnoDB crashes under ... AND DISABLE CHECKPOINT
* [Revision #8de5b58627](https://github.com/MariaDB/server/commit/8de5b58627)\
  2025-01-05 13:14:58 +0100
  * Bump the VERSION
* [Revision #c618c6612f](https://github.com/MariaDB/server/commit/c618c6612f)\
  2025-01-09 08:27:57 -0500
  * [MDEV-35805](https://jira.mariadb.org/browse/MDEV-35805) Update main.lowercase\_table4 for new default collation
* [Revision #8b9c8631a4](https://github.com/MariaDB/server/commit/8b9c8631a4)\
  2025-01-11 12:04:35 -0700
  * [MDEV-35818](https://jira.mariadb.org/browse/MDEV-35818): Fix `replace_binlog_file` info message
* [Revision #3e9da8c923](https://github.com/MariaDB/server/commit/3e9da8c923)\
  2025-01-09 12:31:17 +0200
  * Disable atomic.alter\_table on MSAN because of slowness
* Merge [Revision #15700f54c2](https://github.com/MariaDB/server/commit/15700f54c2) 2025-01-09 09:41:38 +0200 - Merge 11.4 into 11.7
* [Revision #bc32705f46](https://github.com/MariaDB/server/commit/bc32705f46)\
  2024-12-10 13:21:23 +0700
  * [MDEV-31005](https://jira.mariadb.org/browse/MDEV-31005): Make working cursor-protocol
* [Revision #a090a3c571](https://github.com/MariaDB/server/commit/a090a3c571)\
  2024-11-30 21:27:29 +0100
  * [MDEV-33239](https://jira.mariadb.org/browse/MDEV-33239): mysqlbinlog always stops at timestamp 0xffffffff
* [Revision #d60efa269e](https://github.com/MariaDB/server/commit/d60efa269e)\
  2024-11-22 09:54:52 +0100
  * [MDEV-35482](https://jira.mariadb.org/browse/MDEV-35482) Raise the plugin PARSEC maturity
* [Revision #56e4b01b7b](https://github.com/MariaDB/server/commit/56e4b01b7b)\
  2024-11-15 20:20:53 +0100
  * [MDEV-35419](https://jira.mariadb.org/browse/MDEV-35419) Server crashes when a adding column to the table which has a primary key using hash
* [Revision #a826e6db0e](https://github.com/MariaDB/server/commit/a826e6db0e)\
  2024-08-05 01:38:08 +0200
  * binlog\_cache\_data: use the correct cache size in reset()
* Merge [Revision #0796bb8216](https://github.com/MariaDB/server/commit/0796bb8216) 2024-12-04 09:42:46 +0200 - Merge 11.4 into 11.7
* Merge [Revision #33907f9ec6](https://github.com/MariaDB/server/commit/33907f9ec6) 2024-12-02 17:51:17 +0200 - Merge 11.4 into 11.7
* [Revision #4d9548876e](https://github.com/MariaDB/server/commit/4d9548876e)\
  2024-12-02 10:44:06 +0200
  * [MDEV-31340](https://jira.mariadb.org/browse/MDEV-31340) fixup: clang++-20 -Wdeprecated-literal-operator
* [Revision #d4d5bce2da](https://github.com/MariaDB/server/commit/d4d5bce2da)\
  2024-11-25 13:37:56 +0200
  * Fix typo in description of s3\_ssl\_no\_verify
* [Revision #87da4f8938](https://github.com/MariaDB/server/commit/87da4f8938)\
  2024-11-21 17:59:38 +1100
  * main.type\_timestamp fix for cursor protocol
* [Revision #b2d8c632a2](https://github.com/MariaDB/server/commit/b2d8c632a2)\
  2024-09-20 18:29:29 -0600
  * Add missing `LEX_STRING::str`s for `my_snprintf`
* [Revision #74743b0d88](https://github.com/MariaDB/server/commit/74743b0d88)\
  2024-11-11 19:53:41 +0100
  * fix test failures on x86, gcc -O1
* [Revision #38ffaeadab](https://github.com/MariaDB/server/commit/38ffaeadab)\
  2024-10-28 10:29:27 +0100
  * Fix a bad merge
* [Revision #54ab281de8](https://github.com/MariaDB/server/commit/54ab281de8)\
  2024-11-12 14:10:58 +1100
  * [MDEV-34915](https://jira.mariadb.org/browse/MDEV-34915) track session variables - test adjust

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
