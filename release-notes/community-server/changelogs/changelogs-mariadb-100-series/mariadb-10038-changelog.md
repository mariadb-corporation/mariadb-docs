# MariaDB 10.0.38 Changelog

[Download](https://mariadb.com/downloads/?showall=1\&tab=mariadbtx\&group=mariadb_server\&version=10.0.38)[Release Notes](../../old-releases/10.0/10.0.38.md)[Changelog](mariadb-10038-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 31 Jan 2019

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.38.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #368eda060f](https://github.com/MariaDB/server/commit/368eda060f)\
  2019-01-29 20:33:43 +0200
  * List of unstable tests for 10.0.38 release
* [Revision #1522ee2949](https://github.com/MariaDB/server/commit/1522ee2949)\
  2019-01-29 15:00:41 +0200
  * [MDEV-18016](https://jira.mariadb.org/browse/MDEV-18016): Assertion failure on ALTER TABLE after foreign\_key\_checks=0
* [Revision #6699cac0bf](https://github.com/MariaDB/server/commit/6699cac0bf)\
  2019-01-29 14:14:57 +0200
  * [MDEV-18256](https://jira.mariadb.org/browse/MDEV-18256) Duplicated call to dict\_foreign\_remove\_from\_cache()
* [Revision #5e06ee41a4](https://github.com/MariaDB/server/commit/5e06ee41a4)\
  2019-01-29 14:07:59 +0200
  * [MDEV-18222](https://jira.mariadb.org/browse/MDEV-18222): Duplicated call to dict\_foreign\_remove\_from\_cache()
* [Revision #f877f6b49d](https://github.com/MariaDB/server/commit/f877f6b49d)\
  2019-01-29 11:50:07 +0100
  * Fix xtradb version after merge
* [Revision #c991939bab](https://github.com/MariaDB/server/commit/c991939bab)\
  2019-01-29 09:34:08 +0100
  * MariaDB detect incorrect table name
* Merge [Revision #c4f97d3cfa](https://github.com/MariaDB/server/commit/c4f97d3cfa) 2019-01-28 20:52:47 +0100 - Merge branch '5.5' into 10.0
* [Revision #eff71f39dd](https://github.com/MariaDB/server/commit/eff71f39dd)\
  2019-01-28 11:51:12 +0100
  * disable an old test
* [Revision #8c2f3e0c16](https://github.com/MariaDB/server/commit/8c2f3e0c16)\
  2019-01-28 20:17:54 +0100
  * Fix detection of version in tokudb
* Merge [Revision #5cdb3fb25e](https://github.com/MariaDB/server/commit/5cdb3fb25e) 2019-01-28 20:15:57 +0100 - Merge branch 'merge-tokudb-5.6' into 10.0
* [Revision #13802fef83](https://github.com/MariaDB/server/commit/13802fef83)\
  2019-01-24 17:31:13 +0100
  * 5.6.42-84.2
* [Revision #724b09d5e7](https://github.com/MariaDB/server/commit/724b09d5e7)\
  2019-01-28 15:42:16 +0100
  * Version fix after merge
* [Revision #94b68b35f4](https://github.com/MariaDB/server/commit/94b68b35f4)\
  2019-01-28 15:39:27 +0100
  * Reverting part of da34c7de5dacac85c4dc1f714bcd7edf3b7fe5f9 that was already fixed by [MDEV-17531](https://jira.mariadb.org/browse/MDEV-17531) by Marko
* Merge [Revision #959f7415bd](https://github.com/MariaDB/server/commit/959f7415bd) 2019-01-28 15:37:01 +0100 - Merge branch 'merge-xtradb-5.6' into 10.0
* [Revision #3262afc6c5](https://github.com/MariaDB/server/commit/3262afc6c5)\
  2019-01-24 16:48:39 +0100
  * 5.6.42-84.2
* Merge [Revision #c2197e0cd2](https://github.com/MariaDB/server/commit/c2197e0cd2) 2019-01-28 13:16:27 +0100 - Merge branch 'merge-perfschema-5.6' into 10.0
* [Revision #1abdc0e435](https://github.com/MariaDB/server/commit/1abdc0e435)\
  2019-01-24 15:47:27 +0100
  * 5.6.43
* Merge [Revision #a3df9bcadc](https://github.com/MariaDB/server/commit/a3df9bcadc) 2019-01-28 10:36:12 +0100 - Merge branch '5.5' into 10.0
* [Revision #e6fcd72309](https://github.com/MariaDB/server/commit/e6fcd72309)\
  2018-12-02 00:25:05 +0100
  * Squashed commit of connect/10.0:
* [Revision #38ad46e005](https://github.com/MariaDB/server/commit/38ad46e005)\
  2019-01-24 13:31:05 +0100
  * cleanup: fill\_alter\_inplace\_info
* [Revision #013186eb96](https://github.com/MariaDB/server/commit/013186eb96)\
  2019-01-24 10:51:40 +0100
  * compiler warning
* [Revision #036ca990ab](https://github.com/MariaDB/server/commit/036ca990ab)\
  2019-01-24 20:47:46 +0530
  * [MDEV-18255](https://jira.mariadb.org/browse/MDEV-18255): Server crashes in Bitmap<64u>::intersect
* [Revision #edeba0c873](https://github.com/MariaDB/server/commit/edeba0c873)\
  2019-01-23 18:50:47 +0100
  * [MDEV-17868](https://jira.mariadb.org/browse/MDEV-17868) mysqltest fails to link with system PCRE libraries
* [Revision #a0f3b9f94f](https://github.com/MariaDB/server/commit/a0f3b9f94f)\
  2019-01-24 13:52:51 +0530
  * [MDEV-17376](https://jira.mariadb.org/browse/MDEV-17376) Server fails to set ADD\_PK\_INDEX, DROP\_PK\_INDEX if unique index nominated as PK
* [Revision #cce2b45c8f](https://github.com/MariaDB/server/commit/cce2b45c8f)\
  2019-01-10 16:32:56 +0200
  * [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803) Row-based event is not applied when table map id is greater 32 bit int
* [Revision #2a0f1d6132](https://github.com/MariaDB/server/commit/2a0f1d6132)\
  2019-01-22 11:06:15 +0100
  * Bug#28867993: POSSIBLE ISSUE WITH MYSQL SERVER RESTART
* [Revision #31d592ba7d](https://github.com/MariaDB/server/commit/31d592ba7d)\
  2019-01-23 12:05:24 +0200
  * [MDEV-18349](https://jira.mariadb.org/browse/MDEV-18349) InnoDB file size changes are not safe when file system crashes
* [Revision #6786fb004c](https://github.com/MariaDB/server/commit/6786fb004c)\
  2019-01-16 14:46:36 +0100
  * [MDEV-15925](https://jira.mariadb.org/browse/MDEV-15925) FRM\_MAX\_SIZE too low for some use cases
* [Revision #2061e00c20](https://github.com/MariaDB/server/commit/2061e00c20)\
  2019-01-17 22:56:12 +0200
  * [MDEV-14440](https://jira.mariadb.org/browse/MDEV-14440): Assertion \`inited==RND' failed in handler::ha\_rnd\_end
* [Revision #19a7656fb1](https://github.com/MariaDB/server/commit/19a7656fb1)\
  2018-05-21 10:42:44 +1000
  * safemalloc: warn, flush after fprintf
* [Revision #db469b6907](https://github.com/MariaDB/server/commit/db469b6907)\
  2019-01-11 11:55:07 +0100
  * [MDEV-17475](https://jira.mariadb.org/browse/MDEV-17475): Increase maximum possible value for table\_definition\_cache to match table\_open\_cache
* Merge [Revision #12f362c333](https://github.com/MariaDB/server/commit/12f362c333) 2019-01-15 14:53:27 +0200 - [MDEV-18233](https://jira.mariadb.org/browse/MDEV-18233) Moving the hash\_node\_t to improve locality of reference
* [Revision #a06a3e4670](https://github.com/MariaDB/server/commit/a06a3e4670)\
  2019-01-14 22:14:56 +0300
  * [MDEV-18233](https://jira.mariadb.org/browse/MDEV-18233) Moving the hash\_node\_t to improve locality of reference
* [Revision #e0633f25e8](https://github.com/MariaDB/server/commit/e0633f25e8)\
  2019-01-15 14:55:12 +0300
  * [MDEV-18243](https://jira.mariadb.org/browse/MDEV-18243) incorrect ASAN instrumentation
* [Revision #71e9f0d123](https://github.com/MariaDB/server/commit/71e9f0d123)\
  2019-01-15 11:50:15 +0200
  * [MDEV-17797](https://jira.mariadb.org/browse/MDEV-17797) Add ASAN poisoning for mem\_heap\_t
* Merge [Revision #b4c471099d](https://github.com/MariaDB/server/commit/b4c471099d) 2019-01-14 14:06:26 +0200 - Merge pull request #973 from tempesta-tech/tt-10.0-[MDEV-16499](https://jira.mariadb.org/browse/MDEV-16499)-virtual-innodb
* [Revision #e8bb94ccc8](https://github.com/MariaDB/server/commit/e8bb94ccc8)\
  2018-11-30 01:15:30 +0300
  * [MDEV-16499](https://jira.mariadb.org/browse/MDEV-16499) \[10.1] ER\_NO\_SUCH\_TABLE\_IN\_ENGINE followed by "Please drop the table and recreate" upon adding FULLTEXT key to table with virtual column
* [Revision #d0d0f88f2c](https://github.com/MariaDB/server/commit/d0d0f88f2c)\
  2019-01-06 23:15:25 +0530
  * [MDEV-13784](https://jira.mariadb.org/browse/MDEV-13784): query causes seg fault
* Merge [Revision #b87eb04f77](https://github.com/MariaDB/server/commit/b87eb04f77) 2019-01-03 00:20:53 +0100 - Merge branch '5.5' into 10.0
* [Revision #884caeafba](https://github.com/MariaDB/server/commit/884caeafba)\
  2019-01-02 19:32:05 +0100
  * fix RHEL8 "ambiguous python shebang" build failures
* [Revision #32150d2513](https://github.com/MariaDB/server/commit/32150d2513)\
  2019-01-02 19:28:48 +0100
  * compilation warning on Windows
* [Revision #802ce9672f](https://github.com/MariaDB/server/commit/802ce9672f)\
  2018-12-29 20:44:40 +0300
  * [MDEV-18041](https://jira.mariadb.org/browse/MDEV-18041) Database corruption after renaming a prefix-indexed column
* [Revision #b74eb5a5fe](https://github.com/MariaDB/server/commit/b74eb5a5fe)\
  2018-12-28 12:28:16 +0200
  * row\_drop\_table\_for\_mysql(): Correct a parameter to innobase\_format\_name()
* Merge [Revision #8634f7e528](https://github.com/MariaDB/server/commit/8634f7e528) 2018-12-20 09:15:01 +0100 - Merge branch '5.5' into 10.0
* [Revision #f16d4d4c6e](https://github.com/MariaDB/server/commit/f16d4d4c6e)\
  2018-12-19 16:33:00 +0530
  * [MDEV-17720](https://jira.mariadb.org/browse/MDEV-17720) slave\_ddl\_exec\_mode=IDEMPOTENT does not handle DROP DATABASE
* [Revision #7e606a2d5c](https://github.com/MariaDB/server/commit/7e606a2d5c)\
  2018-12-19 10:34:30 +0530
  * [MDEV-17589](https://jira.mariadb.org/browse/MDEV-17589): Stack-buffer-overflow with indexed varchar (utf8) field
* [Revision #da4efd56aa](https://github.com/MariaDB/server/commit/da4efd56aa)\
  2018-12-19 10:38:29 +0530
  * Backported [MDEV-11196](https://jira.mariadb.org/browse/MDEV-11196)(e4d10e09cf31) and [MDEV-10360](https://jira.mariadb.org/browse/MDEV-10360)(8a8ba1949bf4) to 10.0
* [Revision #d1f399408d](https://github.com/MariaDB/server/commit/d1f399408d)\
  2018-12-16 21:50:49 +0200
  * [MDEV-6453](https://jira.mariadb.org/browse/MDEV-6453): Assertion \`inited==NONE || (inited==RND && scan)' failed in handler::ha\_rnd\_init(bool) with InnoDB, joins, AND/OR conditions
* [Revision #1a7158b88a](https://github.com/MariaDB/server/commit/1a7158b88a)\
  2018-12-13 19:51:40 +0100
  * remove unsed variable
* [Revision #8e613458e1](https://github.com/MariaDB/server/commit/8e613458e1)\
  2018-12-13 12:36:57 +0200
  * Fix cmake -DWITH\_PARTITION\_STORAGE\_ENGINE:BOOL=OFF
* [Revision #5ab91f5914](https://github.com/MariaDB/server/commit/5ab91f5914)\
  2018-12-13 12:15:18 +0200
  * Remove space before #ifdef
* [Revision #5f5e73f1fe](https://github.com/MariaDB/server/commit/5f5e73f1fe)\
  2018-12-11 16:16:11 +0530
  * [MDEV-17957](https://jira.mariadb.org/browse/MDEV-17957) Make Innodb\_checksum\_algorithm stricter for strict\_\* values
* [Revision #ce1669af12](https://github.com/MariaDB/server/commit/ce1669af12)\
  2018-12-13 00:26:54 +0530
  * Fix compile error when building without the partition engine
* Merge [Revision #b58f28725b](https://github.com/MariaDB/server/commit/b58f28725b) 2018-12-12 20:19:06 +0100 - Merge branch '5.5' into 10.0
* [Revision #9eadef013e](https://github.com/MariaDB/server/commit/9eadef013e)\
  2018-12-12 15:05:14 +0800
  * Fix UNICODE issue of dlerror
* [Revision #d956709b4b](https://github.com/MariaDB/server/commit/d956709b4b)\
  2018-12-11 22:03:44 +0300
  * [MDEV-17833](https://jira.mariadb.org/browse/MDEV-17833) ALTER TABLE is not enforcing prefix index size limit
* [Revision #4886d14827](https://github.com/MariaDB/server/commit/4886d14827)\
  2018-12-07 02:12:22 +0530
  * [MDEV-17032](https://jira.mariadb.org/browse/MDEV-17032): Estimates are higher for partitions of a table with @@use\_stat\_tables= PREFERABLY
* [Revision #12b1ba195c](https://github.com/MariaDB/server/commit/12b1ba195c)\
  2018-12-07 12:54:02 +0200
  * [MDEV-17904](https://jira.mariadb.org/browse/MDEV-17904) Crash in fts\_is\_sync\_needed() after failed ALTER or CREATE TABLE
* [Revision #daca7e70d7](https://github.com/MariaDB/server/commit/daca7e70d7)\
  2018-12-06 01:17:44 +0100
  * [MDEV-17898](https://jira.mariadb.org/browse/MDEV-17898) FLUSH PRIVILEGES crashes server with segfault
* [Revision #eed0013bed](https://github.com/MariaDB/server/commit/eed0013bed)\
  2018-12-06 00:48:41 +0100
  * correct order of arguments for Dynamic\_array<>::CMP\_FUNC2
* [Revision #8a37ce0767](https://github.com/MariaDB/server/commit/8a37ce0767)\
  2018-12-06 00:48:00 +0100
  * cleanup: DYNAMIC\_ARRAY -> Dynamic\_array\<ACL\_DB> acl\_dbs
* [Revision #17e8570285](https://github.com/MariaDB/server/commit/17e8570285)\
  2018-12-05 19:27:34 +0530
  * Added a testcase for [MDEV-17734](https://jira.mariadb.org/browse/MDEV-17734)
* [Revision #14f6b0cdfd](https://github.com/MariaDB/server/commit/14f6b0cdfd)\
  2018-11-20 20:12:29 +0530
  * [MDEV-17734](https://jira.mariadb.org/browse/MDEV-17734): AddressSanitizer: use-after-poison in create\_key\_parts\_for\_pseudo\_indexes
* Merge [Revision #a84d87fde8](https://github.com/MariaDB/server/commit/a84d87fde8) 2018-11-15 13:57:35 +0100 - Merge branch '5.5' into 10.0
* [Revision #47274d902e](https://github.com/MariaDB/server/commit/47274d902e)\
  2018-11-14 15:46:53 +0100
  * fix of test suite
* [Revision #6cecb10a2f](https://github.com/MariaDB/server/commit/6cecb10a2f)\
  2018-11-07 09:25:12 +0100
  * [MDEV-11167](https://jira.mariadb.org/browse/MDEV-11167): InnoDB: Warning: using a partial-field key prefix in search, results in assertion failure or "Can't find record" error
* Merge [Revision #5f29fdecc0](https://github.com/MariaDB/server/commit/5f29fdecc0) 2018-11-07 08:02:18 +0200 - Merge 5.5 into 10.0
* [Revision #9c026273a9](https://github.com/MariaDB/server/commit/9c026273a9)\
  2018-11-06 10:58:02 +0000
  * Add implementation in .h and delete unneccessery printing
* [Revision #db55b39fb2](https://github.com/MariaDB/server/commit/db55b39fb2)\
  2018-11-05 16:47:14 +0200
  * Revert some InnoDB/XtraDB changes
* [Revision #03977e8273](https://github.com/MariaDB/server/commit/03977e8273)\
  2018-10-25 21:36:24 +0300
  * [MDEV-13671](https://jira.mariadb.org/browse/MDEV-13671) InnoDB should use case-insensitive column name comparisons like the rest of the server
* [Revision #f0cb21ea2e](https://github.com/MariaDB/server/commit/f0cb21ea2e)\
  2018-11-02 12:42:01 +0200
  * Remove dead code is\_thd\_killed()
* [Revision #9eb8a46790](https://github.com/MariaDB/server/commit/9eb8a46790)\
  2018-11-01 11:09:32 -0400
  * bump the VERSION
* [Revision #38b3e52c3c](https://github.com/MariaDB/server/commit/38b3e52c3c)\
  2018-10-31 23:30:34 +0530
  * [MDEV-16695](https://jira.mariadb.org/browse/MDEV-16695): Estimate for rows of derived tables is very high when we are using index\_merge union
* [Revision #c4c738e1ef](https://github.com/MariaDB/server/commit/c4c738e1ef)\
  2018-11-01 09:27:59 +0200
  * Revert commit b2f39a5f567d006000aad8b431267298cf81b569 wrong branch.
* [Revision #b2f39a5f56](https://github.com/MariaDB/server/commit/b2f39a5f56)\
  2018-11-01 09:15:41 +0200
  * Add missing wsrep.cnf.sh
* [Revision #75ceb6ff13](https://github.com/MariaDB/server/commit/75ceb6ff13)\
  2018-10-31 14:25:26 +0400
  * [MDEV-17298](https://jira.mariadb.org/browse/MDEV-17298) ASAN unknown-crash / READ of size 1 in my\_strntoul\_8bit upon INSERT .. SELECT
* Merge [Revision #09e97299ba](https://github.com/MariaDB/server/commit/09e97299ba) 2018-10-31 00:25:26 +0100 - Merge branch '5.5' into 10.0

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
