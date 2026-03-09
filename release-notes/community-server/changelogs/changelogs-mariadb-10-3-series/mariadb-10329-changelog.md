# MariaDB 10.3.29 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.29](https://downloads.mariadb.org/mariadb/10.3.29/)[Release Notes](../../old-releases/10.3/10.3.29.md)[Changelog](mariadb-10329-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 7 May 2021

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.29.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.38](../changelogs-mariadb-102-series/mariadb-10238-changelog.md)
* [Revision #4f143a88bc](https://github.com/MariaDB/server/commit/4f143a88bc)\
  2021-05-05 15:56:23 +0200
  * Fix of ppc64 by Wlad
* Merge [Revision #e7701f8db2](https://github.com/MariaDB/server/commit/e7701f8db2) 2021-05-04 17:32:29 +0200 - Merge branch '10.2' into 10.3
* Merge [Revision #a8a925dd22](https://github.com/MariaDB/server/commit/a8a925dd22) 2021-05-04 14:49:31 +0300 - Merge branch bb-10.2-release into bb-10.3-release
* [Revision #2820f30dde](https://github.com/MariaDB/server/commit/2820f30dde)\
  2021-04-29 19:30:07 +0300
  * [MDEV-23723](https://jira.mariadb.org/browse/MDEV-23723): Crash when test\_if\_skip\_sort\_order() is checked for derived ...
* [Revision #8f9a72a150](https://github.com/MariaDB/server/commit/8f9a72a150)\
  2021-04-28 21:27:04 +0200
  * [MDEV-25501](https://jira.mariadb.org/browse/MDEV-25501) routine\_definition in information\_schema.routines loses tablename if it starts with an \_ and is not backticked
* [Revision #64b7433709](https://github.com/MariaDB/server/commit/64b7433709)\
  2021-04-27 13:05:13 +0200
  * [MDEV-25109](https://jira.mariadb.org/browse/MDEV-25109) Server crashes in sp\_name::sp\_name upon invalid data in mysql.proc
* [Revision #2e279962e9](https://github.com/MariaDB/server/commit/2e279962e9)\
  2021-04-27 13:00:04 +0200
  * cleanup: lowercase\_table.test
* [Revision #1ca56de8a6](https://github.com/MariaDB/server/commit/1ca56de8a6)\
  2021-04-27 21:30:15 +0300
  * [MDEV-20842](https://jira.mariadb.org/browse/MDEV-20842) fix windows result failure
* [Revision #a312cb28bd](https://github.com/MariaDB/server/commit/a312cb28bd)\
  2021-04-27 12:57:17 +0300
  * [MDEV-20842](https://jira.mariadb.org/browse/MDEV-20842) fix test internal check failure
* [Revision #23e090626a](https://github.com/MariaDB/server/commit/23e090626a)\
  2021-04-24 09:06:16 +0300
  * [MDEV-20842](https://jira.mariadb.org/browse/MDEV-20842) Crash using versioning plugin functions after plugin was removed from server
* [Revision #6d73282b13](https://github.com/MariaDB/server/commit/6d73282b13)\
  2021-04-21 22:14:08 +0300
  * [MDEV-25468](https://jira.mariadb.org/browse/MDEV-25468) DELETE HISTORY may delete current data on system-versioned table
* [Revision #29b2f3dbb5](https://github.com/MariaDB/server/commit/29b2f3dbb5)\
  2021-04-27 08:44:28 +0300
  * [MDEV-24545](https://jira.mariadb.org/browse/MDEV-24545) Sequence created by one connection remains invisible to another
* Merge [Revision #0785771e57](https://github.com/MariaDB/server/commit/0785771e57) 2021-04-27 08:42:51 +0300 - Merge 10.2 into 10.3
* [Revision #4d412e9854](https://github.com/MariaDB/server/commit/4d412e9854)\
  2021-04-26 18:17:18 +0300
  * [MDEV-24758](https://jira.mariadb.org/browse/MDEV-24758) heap-use-after-poison in innobase\_add\_instant\_try/rec\_copy
* [Revision #391f1aa6ee](https://github.com/MariaDB/server/commit/391f1aa6ee)\
  2021-02-05 16:45:35 +0530
  * [MDEV-24773](https://jira.mariadb.org/browse/MDEV-24773): slave\_compressed\_protocol doesn't work properly with semi-sync replication
* [Revision #42aad65b89](https://github.com/MariaDB/server/commit/42aad65b89)\
  2021-04-23 19:45:09 +0300
  * [MDEV-24898](https://jira.mariadb.org/browse/MDEV-24898): Server crashes in st\_select\_lex::next\_select
* [Revision #393cf51c04](https://github.com/MariaDB/server/commit/393cf51c04)\
  2021-04-23 19:28:48 +0300
  * [MDEV-24925](https://jira.mariadb.org/browse/MDEV-24925): Server crashes in Item\_subselect::init\_expr\_cache\_tracker
* [Revision #2c9bf0ae87](https://github.com/MariaDB/server/commit/2c9bf0ae87)\
  2021-04-24 15:50:25 -0700
  * This commit adds the same call of st\_select\_lex::set\_unique\_exclude() that complemented the fix for [MDEV-24823](https://jira.mariadb.org/browse/MDEV-24823) in 10.2. As it is the only call of this function in 10.3 the commit also has added the code of the function.
* Merge [Revision #c425d93b92](https://github.com/MariaDB/server/commit/c425d93b92) 2021-04-24 10:37:21 +0300 - Merge 10.2 into 10.3
* [Revision #e3a25793be](https://github.com/MariaDB/server/commit/e3a25793be)\
  2021-04-22 20:02:08 -0700
  * [MDEV-24823](https://jira.mariadb.org/browse/MDEV-24823) Crash with invalid multi-table update of view in 2nd execution of SP
* Merge [Revision #6f271302b6](https://github.com/MariaDB/server/commit/6f271302b6) 2021-04-22 07:32:51 +0300 - Merge 10.2 into 10.3
* Merge [Revision #75c01f39b1](https://github.com/MariaDB/server/commit/75c01f39b1) 2021-04-21 07:25:48 +0300 - Merge 10.2 into 10.3
* [Revision #562bbf5212](https://github.com/MariaDB/server/commit/562bbf5212)\
  2021-04-13 23:56:49 +0300
  * [MDEV-25327](https://jira.mariadb.org/browse/MDEV-25327) Unexpected ER\_DUP\_ENTRY upon dropping PK column from system-versioned table
* [Revision #cc3105e100](https://github.com/MariaDB/server/commit/cc3105e100)\
  2020-12-20 20:52:51 +0200
  * Fix riscv64 build failure by linking correctly with pthread
* [Revision #13d0641710](https://github.com/MariaDB/server/commit/13d0641710)\
  2021-04-14 10:09:04 +0300
  * Fixup merge 6e6318b29b446f76f01f2ef65d1460870b607d2a
* Merge [Revision #ef26a30486](https://github.com/MariaDB/server/commit/ef26a30486) 2021-04-14 07:54:43 +0300 - Merge 10.2 into 10.3
* [Revision #b8c8692fd9](https://github.com/MariaDB/server/commit/b8c8692fd9)\
  2021-04-13 10:28:13 +0300
  * [MDEV-24620](https://jira.mariadb.org/browse/MDEV-24620) ASAN heap-buffer-overflow in btr\_pcur\_restore\_position()
* Merge [Revision #6e6318b29b](https://github.com/MariaDB/server/commit/6e6318b29b) 2021-04-13 10:26:01 +0300 - Merge 10.2 into 10.3
* Merge [Revision #450c017c2d](https://github.com/MariaDB/server/commit/450c017c2d) 2021-04-09 14:32:06 +0300 - Merge 10.2 into 10.3
* [Revision #4c80dcda46](https://github.com/MariaDB/server/commit/4c80dcda46)\
  2021-04-01 16:49:07 +0300
  * fix gcc optimized build
* [Revision #77ffbbca49](https://github.com/MariaDB/server/commit/77ffbbca49)\
  2021-03-24 20:34:16 +0300
  * [MDEV-25172](https://jira.mariadb.org/browse/MDEV-25172) Wrong error message for ADD COLUMN .. AS ROW START
* [Revision #0c99e6e9a6](https://github.com/MariaDB/server/commit/0c99e6e9a6)\
  2021-02-14 23:26:12 +0300
  * [MDEV-22562](https://jira.mariadb.org/browse/MDEV-22562) Assertion \`next\_insert\_id == 0' upon UPDATE on system-versioned table
* [Revision #af52a0e516](https://github.com/MariaDB/server/commit/af52a0e516)\
  2021-02-05 01:52:21 +0300
  * [MDEV-24690](https://jira.mariadb.org/browse/MDEV-24690) Dropping primary key column from versioned table always fails with 1072
* [Revision #b9d1c6574b](https://github.com/MariaDB/server/commit/b9d1c6574b)\
  2021-01-25 13:02:28 +0300
  * [MDEV-23446](https://jira.mariadb.org/browse/MDEV-23446) goto error cleanup
* Merge [Revision #d6d3d9ae2f](https://github.com/MariaDB/server/commit/d6d3d9ae2f) 2021-03-31 08:01:03 +0300 - Merge 10.2 into 10.3
* [Revision #96475b78c5](https://github.com/MariaDB/server/commit/96475b78c5)\
  2021-03-27 23:07:31 +0400
  * [MDEV-25457](https://jira.mariadb.org/browse/MDEV-25457) CREATE / DROP PROCEDURE not logged with audit plugin.
* Merge [Revision #3157fa182a](https://github.com/MariaDB/server/commit/3157fa182a) 2021-03-27 16:11:26 +0200 - Merge 10.2 into 10.3
* [Revision #480a06718d](https://github.com/MariaDB/server/commit/480a06718d)\
  2021-03-23 20:54:54 -0700
  * [MDEV-25128](https://jira.mariadb.org/browse/MDEV-25128) Wrong result from join with materialized semi-join and splittable derived
* [Revision #7d5ec9f1ae](https://github.com/MariaDB/server/commit/7d5ec9f1ae)\
  2021-03-23 12:37:55 +0700
  * fixed typo in postinst script
* [Revision #61e00db6ad](https://github.com/MariaDB/server/commit/61e00db6ad)\
  2021-03-22 15:22:59 +0200
  * [MDEV-24796](https://jira.mariadb.org/browse/MDEV-24796) Assertion \`page\_has\_next... failed in btr\_pcur\_store\_position()
* [Revision #0f3045e432](https://github.com/MariaDB/server/commit/0f3045e432)\
  2021-03-19 17:29:18 +0100
  * fix for engines/funcs/rpl\_sp.test
* Merge [Revision #93d8f887a0](https://github.com/MariaDB/server/commit/93d8f887a0) 2021-03-19 13:33:46 +0200 - Merge 10.2 into 10.3
* [Revision #2944d7e692](https://github.com/MariaDB/server/commit/2944d7e692)\
  2021-03-19 12:20:50 +0100
  * fix for tests from engines/funcs
* [Revision #867724fd30](https://github.com/MariaDB/server/commit/867724fd30)\
  2021-03-18 13:36:02 +0200
  * [MDEV-25125](https://jira.mariadb.org/browse/MDEV-25125) Assertion failure in fetch\_data\_into\_cache\_low()
* Merge [Revision #19052b6deb](https://github.com/MariaDB/server/commit/19052b6deb) 2021-03-18 12:34:48 +0200 - Merge 10.2 into 10.3
* [Revision #eb7c5530ec](https://github.com/MariaDB/server/commit/eb7c5530ec)\
  2021-03-06 05:55:14 +0530
  * [MDEV-24730](https://jira.mariadb.org/browse/MDEV-24730) Insert log operation fails after purge resets n\_core\_fields
* [Revision #08e8ad7c71](https://github.com/MariaDB/server/commit/08e8ad7c71)\
  2021-03-11 12:50:04 +0200
  * [MDEV-25106](https://jira.mariadb.org/browse/MDEV-25106) Deprecation warning for innodb\_checksum\_algorithm=none,innodb,...
* [Revision #6e7ac4060d](https://github.com/MariaDB/server/commit/6e7ac4060d)\
  2021-03-11 12:34:56 +0200
  * [MDEV-25070](https://jira.mariadb.org/browse/MDEV-25070) fixup: Correct the result
* [Revision #cc9c303a45](https://github.com/MariaDB/server/commit/cc9c303a45)\
  2021-03-10 16:46:42 +0530
  * [MDEV-25070](https://jira.mariadb.org/browse/MDEV-25070) SIGSEGV in fts\_create\_in\_mem\_aux\_table
* [Revision #75f781f0d2](https://github.com/MariaDB/server/commit/75f781f0d2)\
  2021-03-05 17:51:17 +0000
  * [MDEV-24868](https://jira.mariadb.org/browse/MDEV-24868) Server crashes in optimize\_schema\_tables\_memory\_usage after select from information\_schema.innodb\_sys\_columns
* [Revision #ecc1cd219d](https://github.com/MariaDB/server/commit/ecc1cd219d)\
  2021-03-05 14:12:35 +0200
  * Fixed that unit.pcre\_test works again.
* Merge [Revision #bcd160753c](https://github.com/MariaDB/server/commit/bcd160753c) 2021-03-05 10:06:42 +0200 - Merge 10.2 into 10.3
* Merge [Revision #e9b8b76f47](https://github.com/MariaDB/server/commit/e9b8b76f47) 2021-03-04 16:04:30 +0200 - Merge branch '10.2' into 10.3
* [Revision #08d8bce583](https://github.com/MariaDB/server/commit/08d8bce583)\
  2021-03-03 22:48:39 -0800
  * [MDEV-22786](https://jira.mariadb.org/browse/MDEV-22786) Crashes with nested table value constructors
* [Revision #5bd994b0d5](https://github.com/MariaDB/server/commit/5bd994b0d5)\
  2021-03-03 10:13:56 +0200
  * [MDEV-24811](https://jira.mariadb.org/browse/MDEV-24811) Assertion find(table) failed with innodb\_evict\_tables\_on\_commit\_debug
* Merge [Revision #ddbc612692](https://github.com/MariaDB/server/commit/ddbc612692) 2021-03-03 09:41:50 +0200 - Merge 10.2 into 10.3
* [Revision #0f81ca6a0b](https://github.com/MariaDB/server/commit/0f81ca6a0b)\
  2021-03-01 09:40:33 -0800
  * [MDEV-24919](https://jira.mariadb.org/browse/MDEV-24919) Crash with subselect formed by table value constructor and used in set function
* [Revision #c25e6f91da](https://github.com/MariaDB/server/commit/c25e6f91da)\
  2021-03-01 22:08:47 +0200
  * Fixed typo in comment
* [Revision #3f15d3bad9](https://github.com/MariaDB/server/commit/3f15d3bad9)\
  2021-03-01 17:51:44 +0200
  * Fixed unit test to not 'bail out' if some tests are not compiled.
* [Revision #415409579a](https://github.com/MariaDB/server/commit/415409579a)\
  2021-03-01 14:44:18 +0200
  * [MDEV-24958](https://jira.mariadb.org/browse/MDEV-24958) Server crashes in my\_strtod ... with DEFAULT(blob)
* [Revision #6983ce704b](https://github.com/MariaDB/server/commit/6983ce704b)\
  2021-02-27 19:56:46 +0200
  * [MDEV-24710](https://jira.mariadb.org/browse/MDEV-24710) Uninitialized value upon CREATE .. SELECT ... VALUE...
* [Revision #43a0a81397](https://github.com/MariaDB/server/commit/43a0a81397)\
  2021-02-27 19:42:43 +0200
  * Fixed printing of wring filname "maria\_open" in maria.maria-recovery2.test
* [Revision #a18b39e3f4](https://github.com/MariaDB/server/commit/a18b39e3f4)\
  2021-03-01 20:08:14 +0400
  * [MDEV-24965](https://jira.mariadb.org/browse/MDEV-24965) With ALTER USER ...IDENTIFIED BY command, password doesn't replaced by asterisks in audit log.
* [Revision #25ecf8ed4b](https://github.com/MariaDB/server/commit/25ecf8ed4b)\
  2021-02-26 13:26:00 +0400
  * [MDEV-24965](https://jira.mariadb.org/browse/MDEV-24965) With ALTER USER ...IDENTIFIED BY command, password doesn't replaced by asterisks in audit log.
* [Revision #1d80e8e4f3](https://github.com/MariaDB/server/commit/1d80e8e4f3)\
  2021-02-25 11:55:08 +0200
  * MENT-1098 Crash during update on 10.4.17 after upgrade from 10.4.10
* Merge [Revision #4473d17430](https://github.com/MariaDB/server/commit/4473d17430) 2021-02-25 12:19:11 +0200 - Merge 10.2 into 10.3
* [Revision #48b5f8a544](https://github.com/MariaDB/server/commit/48b5f8a544)\
  2021-02-25 15:44:45 +1100
  * mysys: lf\_hash - fix l\_search size\_t keylen
* Merge [Revision #3e2afcb3f4](https://github.com/MariaDB/server/commit/3e2afcb3f4) 2021-02-25 12:16:13 +1100 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #bf6484e7bb](https://github.com/MariaDB/server/commit/bf6484e7bb)\
  2021-02-24 13:51:47 -0800
  * [MDEV-24910](https://jira.mariadb.org/browse/MDEV-24910) Crash with SELECT that uses table value constructor as a subselect
* Merge [Revision #13f0e1e139](https://github.com/MariaDB/server/commit/13f0e1e139) 2021-02-23 21:43:05 +0200 - Merge branch '10.2' into 10.3
* Merge [Revision #69bf55ffb6](https://github.com/MariaDB/server/commit/69bf55ffb6) 2021-02-23 10:56:00 +0200 - Merge 10.2 into 10.3
* [Revision #640f42311a](https://github.com/MariaDB/server/commit/640f42311a)\
  2021-02-20 14:46:19 +0200
  * [MDEV-24929](https://jira.mariadb.org/browse/MDEV-24929) Server crash in thr\_multi\_unlock or in get\_schema\_tables\_result
* Merge [Revision #0ab1e3914c](https://github.com/MariaDB/server/commit/0ab1e3914c) 2021-02-22 21:25:16 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #ca126d96f5](https://github.com/MariaDB/server/commit/ca126d96f5) 2021-02-22 19:46:21 +0100 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #a5b18613ec](https://github.com/MariaDB/server/commit/a5b18613ec)\
  2021-02-21 22:01:24 -0800
  * [MDEV-24936](https://jira.mariadb.org/browse/MDEV-24936) EXPLAIN for query based on table value constructor lacks info on used subqueries
* [Revision #a49ce0bf93](https://github.com/MariaDB/server/commit/a49ce0bf93)\
  2021-02-22 09:44:23 -0500
  * bump the VERSION
* [Revision #8db5274dce](https://github.com/MariaDB/server/commit/8db5274dce)\
  2021-02-21 20:38:32 +0200
  * [MDEV-22703](https://jira.mariadb.org/browse/MDEV-22703) DEFAULT() on a BLOB column can overwrite the default record
* [Revision #da88e1ec12](https://github.com/MariaDB/server/commit/da88e1ec12)\
  2021-02-10 23:38:52 -0800
  * [MDEV-24840](https://jira.mariadb.org/browse/MDEV-24840) Crash caused by query with IN subquery containing union of two table value costructors

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
