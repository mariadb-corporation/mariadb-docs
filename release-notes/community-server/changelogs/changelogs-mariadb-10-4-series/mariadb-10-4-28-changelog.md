# MariaDB 10.4.28 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.4/10.4.28.md)[Changelog](mariadb-10-4-28-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.4.28/)

**Release date:** 6 Feb 2023

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.28.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.38](../changelogs-mariadb-10-3-series/mariadb-10-3-38-changelog.md)
* [Revision #c8f2e9a5c0](https://github.com/MariaDB/server/commit/c8f2e9a5c0)\
  2023-01-30 11:49:42 +0100
  * Fix number of rows passing in case of EQ\_REF
* [Revision #9c6fcdb85e](https://github.com/MariaDB/server/commit/9c6fcdb85e)\
  2023-01-26 12:04:28 +0300
  * [MDEV-30218](https://jira.mariadb.org/browse/MDEV-30218): Incorrect optimization for rowid\_filtering, correction
* Merge [Revision #a977054ee0](https://github.com/MariaDB/server/commit/a977054ee0) 2023-01-28 18:22:55 +0100 - Merge branch '10.3' into 10.4
* [Revision #765291d63e](https://github.com/MariaDB/server/commit/765291d63e)\
  2023-01-25 16:44:23 +1100
  * CREDITS: re-instate Tencent Cloud
* [Revision #284810b3e8](https://github.com/MariaDB/server/commit/284810b3e8)\
  2023-01-19 18:28:14 +1100
  * [MDEV-30370](https://jira.mariadb.org/browse/MDEV-30370) Fixing spider hang when server aborts
* [Revision #801c0b4b47](https://github.com/MariaDB/server/commit/801c0b4b47)\
  2023-01-23 10:43:57 +0200
  * Update 10.4 HELP tables
* [Revision #734ad06880](https://github.com/MariaDB/server/commit/734ad06880)\
  2023-01-20 19:43:40 +0100
  * [MDEV-29461](https://jira.mariadb.org/browse/MDEV-29461) AddressSanitizer: stack-buffer-overflow in strxmov
* [Revision #0c27559994](https://github.com/MariaDB/server/commit/0c27559994)\
  2023-01-20 19:21:17 +0100
  * [MDEV-26817](https://jira.mariadb.org/browse/MDEV-26817) runtime error: index 24320 out of bounds for type 'json\_string\_char\_classes \[128] _and_ ASAN: global-buffer-overflow on address ... READ of size 4 on SELECT JSON\_VALID
* [Revision #fc292f42be](https://github.com/MariaDB/server/commit/fc292f42be)\
  2023-01-20 11:03:05 +0100
  * [MDEV-29199](https://jira.mariadb.org/browse/MDEV-29199) Unique hash key is ignored upon INSERT ... SELECT into non-empty MyISAM table
* [Revision #db50919f97](https://github.com/MariaDB/server/commit/db50919f97)\
  2023-01-19 21:53:16 +0100
  * [MDEV-27631](https://jira.mariadb.org/browse/MDEV-27631) Assertion \`global\_status\_var.global\_memory\_used == 0' failed in mysqld\_exit
* Merge [Revision #f3f09def23](https://github.com/MariaDB/server/commit/f3f09def23) 2023-01-20 11:46:18 +0200 - Merge branch 'codership-10.4-fix-sst\_received' into bb-10.4-[MDEV-30419](https://jira.mariadb.org/browse/MDEV-30419)
* [Revision #b2b9d91668](https://github.com/MariaDB/server/commit/b2b9d91668)\
  2023-01-12 13:18:33 +0700
  * [MDEV-29294](https://jira.mariadb.org/browse/MDEV-29294) Assertion \`functype() == ((Item\_cond \*) new\_item)->functype()' failed in Item\_cond::remove\_eq\_conds on SELECT
* [Revision #eea9f2a1e7](https://github.com/MariaDB/server/commit/eea9f2a1e7)\
  2023-01-20 09:52:00 +0400
  * [MDEV-27653](https://jira.mariadb.org/browse/MDEV-27653) long uniques don't work with unicode collations
* [Revision #ae96e21cf0](https://github.com/MariaDB/server/commit/ae96e21cf0)\
  2023-01-19 09:25:40 +0100
  * Correct assert\_grep.inc params in galera gcache tests
* [Revision #0253a2f48e](https://github.com/MariaDB/server/commit/0253a2f48e)\
  2023-01-12 13:41:49 +1100
  * [MDEV-26541](https://jira.mariadb.org/browse/MDEV-26541) Make UBSAN builds work with spider again.
* [Revision #a27b8b2683](https://github.com/MariaDB/server/commit/a27b8b2683)\
  2022-10-28 13:43:51 +0400
  * [MDEV-27653](https://jira.mariadb.org/browse/MDEV-27653) long uniques don't work with unicode collations
* [Revision #beb1e230dd](https://github.com/MariaDB/server/commit/beb1e230dd)\
  2023-01-16 17:45:06 +0200
  * [MDEV-30419](https://jira.mariadb.org/browse/MDEV-30419) Fix unhandled exception thrown from wsrep-lib
* [Revision #afb5deb9db](https://github.com/MariaDB/server/commit/afb5deb9db)\
  2023-01-12 13:18:33 +0700
  * [MDEV-29294](https://jira.mariadb.org/browse/MDEV-29294) Assertion \`functype() == ((Item\_cond \*) new\_item)->functype()' failed in Item\_cond::remove\_eq\_conds on SELECT
* [Revision #c256998b6e](https://github.com/MariaDB/server/commit/c256998b6e)\
  2023-01-20 09:52:00 +0400
  * [MDEV-27653](https://jira.mariadb.org/browse/MDEV-27653) long uniques don't work with unicode collations
* [Revision #c4f5128d46](https://github.com/MariaDB/server/commit/c4f5128d46)\
  2023-01-19 09:25:40 +0100
  * Correct assert\_grep.inc params in galera gcache tests
* [Revision #a68b9dd993](https://github.com/MariaDB/server/commit/a68b9dd993)\
  2023-01-12 13:41:49 +1100
  * [MDEV-26541](https://jira.mariadb.org/browse/MDEV-26541) Make UBSAN builds work with spider again.
* [Revision #284ac6f2b7](https://github.com/MariaDB/server/commit/284ac6f2b7)\
  2022-10-28 13:43:51 +0400
  * [MDEV-27653](https://jira.mariadb.org/browse/MDEV-27653) long uniques don't work with unicode collations
* [Revision #9924466b3b](https://github.com/MariaDB/server/commit/9924466b3b)\
  2023-01-16 23:06:38 +0100
  * v5.5.4-stable
* Merge [Revision #2b3423c462](https://github.com/MariaDB/server/commit/2b3423c462) 2023-01-17 18:03:58 +0200 - Merge 10.3 into 10.4
* [Revision #3e8b6a79b7](https://github.com/MariaDB/server/commit/3e8b6a79b7)\
  2023-01-16 10:23:22 +1100
  * Update sponsors
* [Revision #a44d896f98](https://github.com/MariaDB/server/commit/a44d896f98)\
  2022-10-12 14:13:49 +0300
  * 10.4-[MDEV-29684](https://jira.mariadb.org/browse/MDEV-29684) Fixes for cluster wide write conflict resolving
* [Revision #0ff7f33c7b](https://github.com/MariaDB/server/commit/0ff7f33c7b)\
  2022-10-12 15:07:20 +0300
  * 10.4-[MDEV-29684](https://jira.mariadb.org/browse/MDEV-29684) Fixes for cluster wide write conflict resolving
* [Revision #68cfcf9cb6](https://github.com/MariaDB/server/commit/68cfcf9cb6)\
  2022-11-08 16:36:34 +0200
  * [MDEV-29512](https://jira.mariadb.org/browse/MDEV-29512) deadlock between commit monitor and THD::LOCK\_thd\_data mutex
* [Revision #cd97523dcf](https://github.com/MariaDB/server/commit/cd97523dcf)\
  2022-12-29 12:59:34 +0200
  * [MDEV-30317](https://jira.mariadb.org/browse/MDEV-30317) Transaction savepoint may cause failure in galera replaying
* [Revision #66c05326d2](https://github.com/MariaDB/server/commit/66c05326d2)\
  2022-10-06 15:16:06 +0300
  * [MDEV-29684](https://jira.mariadb.org/browse/MDEV-29684) Fixes for cluster wide write conflict resolving
* Merge [Revision #71e8e4934d](https://github.com/MariaDB/server/commit/71e8e4934d) 2023-01-13 09:28:25 +0200 - Merge 10.3 into 10.4
* [Revision #12618cfb28](https://github.com/MariaDB/server/commit/12618cfb28)\
  2023-01-08 08:43:02 +0000
  * [MDEV-19160](https://jira.mariadb.org/browse/MDEV-19160) json\_pretty() alias for json\_detailed()
* [Revision #17920291a6](https://github.com/MariaDB/server/commit/17920291a6)\
  2023-01-12 20:11:19 +0530
  * fixup for [MDEV-19160](https://jira.mariadb.org/browse/MDEV-19160)
* [Revision #c08dba7b28](https://github.com/MariaDB/server/commit/c08dba7b28)\
  2023-01-12 02:48:33 +0200
  * Fixed failing test main.func\_json
* [Revision #f3d8a546e7](https://github.com/MariaDB/server/commit/f3d8a546e7)\
  2023-01-11 20:15:26 +0200
  * [MDEV-30345](https://jira.mariadb.org/browse/MDEV-30345) DML does not find rows it is supposed to
* Merge [Revision #fdcfc25127](https://github.com/MariaDB/server/commit/fdcfc25127) 2023-01-10 21:04:17 +0100 - Merge branch '10.3' into 10.4
* [Revision #6cb84346e1](https://github.com/MariaDB/server/commit/6cb84346e1)\
  2022-11-17 19:23:08 +0100
  * [MDEV-17869](https://jira.mariadb.org/browse/MDEV-17869) AddressSanitizer: use-after-poison in Item\_change\_list::rollback\_item\_tree\_changes
* [Revision #df82d68421](https://github.com/MariaDB/server/commit/df82d68421)\
  2022-11-17 20:03:33 +0100
  * cleanup
* [Revision #1e6ad0ce13](https://github.com/MariaDB/server/commit/1e6ad0ce13)\
  2023-01-09 12:49:37 +0100
  * don't set default value in temp table if NO\_DEFAULT\_VALUE\_FLAG
* [Revision #32f09df2b8](https://github.com/MariaDB/server/commit/32f09df2b8)\
  2022-11-17 17:33:34 +0100
  * [MDEV-29890](https://jira.mariadb.org/browse/MDEV-29890) Update with inner join false row count result
* [Revision #610cea3dda](https://github.com/MariaDB/server/commit/610cea3dda)\
  2022-11-17 17:30:59 +0100
  * cleanup
* [Revision #ad27e95d54](https://github.com/MariaDB/server/commit/ad27e95d54)\
  2022-12-24 13:45:06 +0100
  * disable hanging galera test
* [Revision #3d95737e55](https://github.com/MariaDB/server/commit/3d95737e55)\
  2022-12-23 23:58:56 +0100
  * galera.galera\_wsrep\_new\_cluster: fix bad merge
* [Revision #111a752b96](https://github.com/MariaDB/server/commit/111a752b96)\
  2023-01-04 18:44:03 +0000
  * [MDEV-19160](https://jira.mariadb.org/browse/MDEV-19160) JSON\_DETAILED output unnecessarily verbose
* Merge [Revision #fb0808c450](https://github.com/MariaDB/server/commit/fb0808c450) 2023-01-03 16:10:02 +0200 - Merge 10.3 into 10.4
* [Revision #fb41117c90](https://github.com/MariaDB/server/commit/fb41117c90)\
  2022-12-20 10:38:35 +1100
  * [MDEV-29653](https://jira.mariadb.org/browse/MDEV-29653) Make sure Item\_cache\_row has the correct type handler.
* [Revision #c21566a78a](https://github.com/MariaDB/server/commit/c21566a78a)\
  2022-12-19 16:54:15 -0600
  * header typos
* Merge [Revision #f97f6955bd](https://github.com/MariaDB/server/commit/f97f6955bd) 2022-12-14 06:20:04 +0200 - Merge 10.3 into 10.4
* [Revision #87eccd78a7](https://github.com/MariaDB/server/commit/87eccd78a7)\
  2022-12-13 12:40:53 +0200
  * [MDEV-30218](https://jira.mariadb.org/browse/MDEV-30218): Incorrect optimization for rowid\_filtering
* Merge [Revision #fdf43b5c78](https://github.com/MariaDB/server/commit/fdf43b5c78) 2022-12-13 11:37:33 +0200 - Merge 10.3 into 10.4
* [Revision #382e85fe70](https://github.com/MariaDB/server/commit/382e85fe70)\
  2022-11-22 13:47:14 +1100
  * [MDEV-30065](https://jira.mariadb.org/browse/MDEV-30065): mariadb-install-db allow for --enforce-storage-engine=InnoDB
* [Revision #c1cc6e8496](https://github.com/MariaDB/server/commit/c1cc6e8496)\
  2022-12-12 10:51:13 +1100
  * Correct DBUG\_ENTER for Pushdown\_derived::execute
* [Revision #a491400833](https://github.com/MariaDB/server/commit/a491400833)\
  2022-10-28 11:16:25 +0200
  * [MDEV-29814](https://jira.mariadb.org/browse/MDEV-29814): galera\_var\_notify\_ssl\_ipv6 causes testing system to hang
* [Revision #0174a9ff3d](https://github.com/MariaDB/server/commit/0174a9ff3d)\
  2022-10-26 08:08:06 +0300
  * [MDEV-30172](https://jira.mariadb.org/browse/MDEV-30172): Galera test case cleanup
* [Revision #07a06022c4](https://github.com/MariaDB/server/commit/07a06022c4)\
  2022-11-08 16:36:34 +0200
  * [MDEV-29512](https://jira.mariadb.org/browse/MDEV-29512) deadlock between commit monitor and THD::LOCK\_thd\_data mutex
* [Revision #283efe2680](https://github.com/MariaDB/server/commit/283efe2680)\
  2022-11-11 13:08:20 +0100
  * [MDEV-29878](https://jira.mariadb.org/browse/MDEV-29878) Galera test failure on [MDEV-26575](https://jira.mariadb.org/browse/MDEV-26575)
* [Revision #97d9bf98b2](https://github.com/MariaDB/server/commit/97d9bf98b2)\
  2022-11-17 16:02:04 +0100
  * Restore auto increment offset in test galera\_join\_with\_cc\_A
* [Revision #c2fc5266ad](https://github.com/MariaDB/server/commit/c2fc5266ad)\
  2022-11-14 11:31:14 +0100
  * [MDEV-29880](https://jira.mariadb.org/browse/MDEV-29880) Galera test failure on GCF-336
* [Revision #c77459f89c](https://github.com/MariaDB/server/commit/c77459f89c)\
  2022-11-29 06:49:17 +0200
  * Update wsrep-lib submodule
* [Revision #8535189f32](https://github.com/MariaDB/server/commit/8535189f32)\
  2022-11-25 19:50:40 +0000
  * reformat the test
* [Revision #0204cf182a](https://github.com/MariaDB/server/commit/0204cf182a)\
  2022-11-25 13:33:16 +0000
  * update anotation
* [Revision #8fc23c4a75](https://github.com/MariaDB/server/commit/8fc23c4a75)\
  2022-11-24 22:48:13 +0000
  * remove redundant test file
* [Revision #196a54052a](https://github.com/MariaDB/server/commit/196a54052a)\
  2022-11-23 09:36:28 +0000
  * increase max field name
* [Revision #640d299546](https://github.com/MariaDB/server/commit/640d299546)\
  2022-11-24 22:48:13 +0000
  * remove redundant test file
* [Revision #bbabdaef31](https://github.com/MariaDB/server/commit/bbabdaef31)\
  2022-11-23 09:36:28 +0000
  * increase max field name
* [Revision #da03d8d99f](https://github.com/MariaDB/server/commit/da03d8d99f)\
  2022-03-09 02:09:36 +0900
  * [MDEV-19190](https://jira.mariadb.org/browse/MDEV-19190) Assertion `...auto_inc_initialized` failed in get\_auto\_increment
* [Revision #1ebf0b7372](https://github.com/MariaDB/server/commit/1ebf0b7372)\
  2022-10-19 02:51:01 +0200
  * [MDEV-29817](https://jira.mariadb.org/browse/MDEV-29817): Issues with handling options for SSL CRLs (and some others)
* [Revision #931549ff66](https://github.com/MariaDB/server/commit/931549ff66)\
  2022-11-22 14:03:23 +0400
  * [MDEV-27670](https://jira.mariadb.org/browse/MDEV-27670) Assertion \`(cs->state & 0x20000) == 0' failed in my\_strnncollsp\_nchars\_generic\_8bit
* [Revision #3e0fd5e8a7](https://github.com/MariaDB/server/commit/3e0fd5e8a7)\
  2022-11-21 11:57:19 +0100
  * [MDEV-30055](https://jira.mariadb.org/browse/MDEV-30055) shutdown\_now\_windows.test fails with "Assertion \`unix\_sock.fd >= 0' failed."
* [Revision #0d586d62e5](https://github.com/MariaDB/server/commit/0d586d62e5)\
  2022-11-20 11:31:57 +0200
  * [MDEV-29613](https://jira.mariadb.org/browse/MDEV-29613) fixup: Fix Spider
* Merge [Revision #20969aa412](https://github.com/MariaDB/server/commit/20969aa412) 2022-11-09 09:28:39 +0200 - Merge 10.3 into 10.4
* [Revision #8fb176c3c1](https://github.com/MariaDB/server/commit/8fb176c3c1)\
  2022-11-08 16:59:36 +0200
  * [MDEV-27121](https://jira.mariadb.org/browse/MDEV-27121) fixup: mariadb-backup.[MDEV-14447](https://jira.mariadb.org/browse/MDEV-14447),full\_crc32
* [Revision #12f20c154d](https://github.com/MariaDB/server/commit/12f20c154d)\
  2022-11-08 16:04:16 +0200
  * Work around [MDEV-24813](https://jira.mariadb.org/browse/MDEV-24813) in main.rowid\_filter\_innodb\_debug
* Merge [Revision #93b4f84ab2](https://github.com/MariaDB/server/commit/93b4f84ab2) 2022-11-08 16:04:01 +0200 - Merge 10.3 into 10.4
* [Revision #1e8189fcee](https://github.com/MariaDB/server/commit/1e8189fcee)\
  2022-11-08 10:55:22 +0200
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) follow-up: Correct a bogus comment
* Merge [Revision #e9dc39572f](https://github.com/MariaDB/server/commit/e9dc39572f) 2022-11-07 15:49:14 +0100 - Merge branch '10.4' into bb-10.4-release
* [Revision #625fff0d8f](https://github.com/MariaDB/server/commit/625fff0d8f)\
  2022-11-07 08:35:15 -0500
  * bump the VERSION
* [Revision #10132ad261](https://github.com/MariaDB/server/commit/10132ad261)\
  2020-09-14 15:27:02 +0100
  * [MDEV-23264](https://jira.mariadb.org/browse/MDEV-23264) Unique blobs allow duplicate values upon UPDATE
* [Revision #0d927a57d2](https://github.com/MariaDB/server/commit/0d927a57d2)\
  2022-10-19 13:26:19 +0400
  * [MDEV-29624](https://jira.mariadb.org/browse/MDEV-29624) [MDEV-29655](https://jira.mariadb.org/browse/MDEV-29655) Fix ASAN errors on pushdown of derived table
* [Revision #ce443c8554](https://github.com/MariaDB/server/commit/ce443c8554)\
  2022-10-26 14:48:03 +0400
  * [MDEV-29495](https://jira.mariadb.org/browse/MDEV-29495) Generalize can\_convert\_xxx() hook engine API to cover any arbitrary data type

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
