# MariaDB 10.5.14 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.14](https://mariadb.org/download/?tab=mariadb\&release=10.5.14\&product=mariadb)[Release Notes](../../old-releases/10.5/10.5.14.md)[Changelog](mariadb-10514-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

**Release date:** 9 Feb 2022

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.14.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.23](../changelogs-mariadb-10-4-series/mariadb-10423-changelog.md)
* [Revision #ad3ac55641](https://github.com/MariaDB/server/commit/ad3ac55641)\
  2022-02-04 09:55:04 +0100
  * fix 32bit embedded result file.
* [Revision #2cf52736de](https://github.com/MariaDB/server/commit/2cf52736de)\
  2022-02-04 09:54:45 +0100
  * Fix for clang compilation
* Merge [Revision #cf63eecef4](https://github.com/MariaDB/server/commit/cf63eecef4) 2022-02-01 20:33:04 +0100 - Merge branch '10.4' into 10.5
* [Revision #fb40a2fabf](https://github.com/MariaDB/server/commit/fb40a2fabf)\
  2022-01-30 22:52:59 +0100
  * pass MYSQL\_MAINTAINER\_MODE down to srpm builds
* [Revision #0943386fb3](https://github.com/MariaDB/server/commit/0943386fb3)\
  2022-01-31 11:41:12 +0100
  * fix main.mysqld--help-aria failures
* [Revision #66bc8bf09e](https://github.com/MariaDB/server/commit/66bc8bf09e)\
  2022-01-30 18:09:55 +0100
  * fix query cache in embedded, enable MARIADB\_CLIENT\_EXTENDED\_METADATA
* [Revision #9667ec1f53](https://github.com/MariaDB/server/commit/9667ec1f53)\
  2022-01-30 13:56:22 +0100
  * fix query cache in embedded
* [Revision #646e2f423b](https://github.com/MariaDB/server/commit/646e2f423b)\
  2022-01-29 14:11:31 +0100
  * update columnstore to 5.6.4-1
* [Revision #059a8fd87e](https://github.com/MariaDB/server/commit/059a8fd87e)\
  2022-01-28 22:32:56 +0400
  * [MDEV-27668](https://jira.mariadb.org/browse/MDEV-27668) Assertion \`item->type\_handler()->is\_traditional\_scalar\_type() || item->type\_handler() == type\_handler()' failed in Field\_inet6::can\_optimize\_keypart\_ref
* [Revision #fb8fea3490](https://github.com/MariaDB/server/commit/fb8fea3490)\
  2022-01-28 15:55:39 +0200
  * [MDEV-27667](https://jira.mariadb.org/browse/MDEV-27667) Fix [MDEV-26720](https://jira.mariadb.org/browse/MDEV-26720) on 64-bit Microsoft Windows
* Merge [Revision #880d543554](https://github.com/MariaDB/server/commit/880d543554) 2022-01-28 11:57:52 +0100 - Merge branch 'merge-perfschema-5.7' into 10.5
* [Revision #157e66273b](https://github.com/MariaDB/server/commit/157e66273b)\
  2022-01-25 11:13:39 +0100
  * 5.7.37
* [Revision #0b116d160a](https://github.com/MariaDB/server/commit/0b116d160a)\
  2021-05-03 11:21:56 +0200
  * 5.7.34
* [Revision #430d60d1fc](https://github.com/MariaDB/server/commit/430d60d1fc)\
  2022-01-27 15:54:20 +0400
  * [MDEV-24487](https://jira.mariadb.org/browse/MDEV-24487) Error after update to 10.5.8 on CentOS-8: DBD::mysql::st execute failed: Unknown MySQL error
* [Revision #4d74bac8bc](https://github.com/MariaDB/server/commit/4d74bac8bc)\
  2022-01-26 11:23:20 +0100
  * new pcre fixup - they renamed static libraries, again.
* [Revision #a73acf6c06](https://github.com/MariaDB/server/commit/a73acf6c06)\
  2022-01-25 10:33:52 +0100
  * new pcre 10.39
* [Revision #53173709b3](https://github.com/MariaDB/server/commit/53173709b3)\
  2022-01-25 14:19:52 +0100
  * [MDEV-26223](https://jira.mariadb.org/browse/MDEV-26223) Galera cluster node consider old server\_id value even after modification of server\_id \[wsrep\_gtid\_mode=ON]
* [Revision #56f5599f09](https://github.com/MariaDB/server/commit/56f5599f09)\
  2022-01-26 13:29:34 +0200
  * [MDEV-27610](https://jira.mariadb.org/browse/MDEV-27610) Unnecessary wait in InnoDB crash recovery
* [Revision #216834b068](https://github.com/MariaDB/server/commit/216834b068)\
  2022-01-25 17:48:44 +0400
  * A cleanup for [MDEV-18918](https://jira.mariadb.org/browse/MDEV-18918)/[MDEV-20254](https://jira.mariadb.org/browse/MDEV-20254)
* [Revision #0f7fececbf](https://github.com/MariaDB/server/commit/0f7fececbf)\
  2022-01-25 11:05:41 +0200
  * Revert "[MDEV-26223](https://jira.mariadb.org/browse/MDEV-26223) Galera cluster node consider old server\_id value even after modification of server\_id \[wsrep\_gtid\_mode=ON]"
* [Revision #62e320c86d](https://github.com/MariaDB/server/commit/62e320c86d)\
  2021-12-28 17:43:40 +0400
  * [MDEV-18918](https://jira.mariadb.org/browse/MDEV-18918) SQL mode EMPTY\_STRING\_IS\_NULL breaks RBR upon CREATE TABLE .. SELECT
* [Revision #e4b302e436](https://github.com/MariaDB/server/commit/e4b302e436)\
  2022-01-10 18:05:55 +0400
  * [MDEV-27018](https://jira.mariadb.org/browse/MDEV-27018) IF and COALESCE lose "json" property
* [Revision #28e166d643](https://github.com/MariaDB/server/commit/28e166d643)\
  2022-01-20 16:30:18 +0530
  * [MDEV-26784](https://jira.mariadb.org/browse/MDEV-26784) \[Warning] InnoDB: Difficult to find free blocks in the buffer pool
* [Revision #a0f711e928](https://github.com/MariaDB/server/commit/a0f711e928)\
  2022-01-20 11:30:49 +0200
  * [MDEV-26223](https://jira.mariadb.org/browse/MDEV-26223) Galera cluster node consider old server\_id value even after modification of server\_id \[wsrep\_gtid\_mode=ON]
* [Revision #66465914c1](https://github.com/MariaDB/server/commit/66465914c1)\
  2022-01-20 07:37:43 +0200
  * [MDEV-27550](https://jira.mariadb.org/browse/MDEV-27550): Disable galera.MW-328D
* [Revision #7259b299a5](https://github.com/MariaDB/server/commit/7259b299a5)\
  2022-01-13 15:53:44 +0300
  * [MDEV-27382](https://jira.mariadb.org/browse/MDEV-27382): OFFSET is ignored when combined with DISTINCT
* [Revision #be8113861c](https://github.com/MariaDB/server/commit/be8113861c)\
  2022-01-11 18:19:39 +0300
  * [MDEV-27025](https://jira.mariadb.org/browse/MDEV-27025) insert-intention lock conflicts with waiting ORDINARY lock
* [Revision #e44439ab73](https://github.com/MariaDB/server/commit/e44439ab73)\
  2022-01-17 16:56:07 +0200
  * [MDEV-27499](https://jira.mariadb.org/browse/MDEV-27499) Performance regression in log\_checkpoint\_margin()
* [Revision #745aa8bee7](https://github.com/MariaDB/server/commit/745aa8bee7)\
  2021-12-29 14:37:03 +0100
  * [MDEV-26230](https://jira.mariadb.org/browse/MDEV-26230) mysql\_upgrade fails to load type\_mysql\_json due to insufficient maturity level
* [Revision #5af6a13771](https://github.com/MariaDB/server/commit/5af6a13771)\
  2021-12-29 13:53:19 +0100
  * [MDEV-25373](https://jira.mariadb.org/browse/MDEV-25373) DROP TABLE doesn't raise error while dropping non-existing table in [MariaDB 10.5.9](../../old-releases/10.5/10.5.9.md) when OQGraph SE is loaded to the server
* [Revision #f18e25649d](https://github.com/MariaDB/server/commit/f18e25649d)\
  2022-01-17 16:09:09 +0200
  * [MDEV-27461](https://jira.mariadb.org/browse/MDEV-27461): Buffer pool resize fails to wake up the page cleaner
* [Revision #b7e4dc121a](https://github.com/MariaDB/server/commit/b7e4dc121a)\
  2022-01-15 21:24:25 +0900
  * [MDEV-27240](https://jira.mariadb.org/browse/MDEV-27240) fixup: remove dead code
* [Revision #64f844b611](https://github.com/MariaDB/server/commit/64f844b611)\
  2022-01-15 17:28:06 +0900
  * [MDEV-27240](https://jira.mariadb.org/browse/MDEV-27240) fixup: remove #ifdef in macro call
* [Revision #2ecd39c983](https://github.com/MariaDB/server/commit/2ecd39c983)\
  2022-01-11 21:57:11 +0900
  * [MDEV-27240](https://jira.mariadb.org/browse/MDEV-27240) SIGSEGV in ha\_spider::store\_lock on LOCK TABLE
* [Revision #8535c260dd](https://github.com/MariaDB/server/commit/8535c260dd)\
  2022-01-14 20:27:51 +0200
  * Remove FIXME comments that refer to an early [MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425) plan
* [Revision #c104a01b50](https://github.com/MariaDB/server/commit/c104a01b50)\
  2022-01-14 17:42:19 +0200
  * [MDEV-27500](https://jira.mariadb.org/browse/MDEV-27500) buf\_page\_free() fails to drop the adaptive hash index
* [Revision #6831b3f2a0](https://github.com/MariaDB/server/commit/6831b3f2a0)\
  2022-01-12 17:18:38 +0300
  * [MDEV-26824](https://jira.mariadb.org/browse/MDEV-26824) Can't add foreign key with empty referenced columns list
* [Revision #017d1b867b](https://github.com/MariaDB/server/commit/017d1b867b)\
  2022-01-12 12:29:16 +0200
  * [MDEV-27476](https://jira.mariadb.org/browse/MDEV-27476) heap-use-after-free in buf\_pool\_t::is\_block\_field()
* [Revision #f443cd1100](https://github.com/MariaDB/server/commit/f443cd1100)\
  2021-11-11 15:22:20 +0600
  * [MDEV-27022](https://jira.mariadb.org/browse/MDEV-27022) Buffer pool is being flushed during recovery
* [Revision #81e00485c3](https://github.com/MariaDB/server/commit/81e00485c3)\
  2020-10-16 20:19:09 +0530
  * [MDEV-23836](https://jira.mariadb.org/browse/MDEV-23836): Assertion \`! is\_set() || m\_can\_overwrite\_status' in Diagnostics\_area::set\_error\_status (interrupted ALTER TABLE under LOCK)
* [Revision #c62bb9c3b4](https://github.com/MariaDB/server/commit/c62bb9c3b4)\
  2022-01-09 23:52:24 +0100
  * Silence CMake warning from exteral cmake project (pcre2)
* [Revision #4c3ad24413](https://github.com/MariaDB/server/commit/4c3ad24413)\
  2022-01-04 07:40:31 +0200
  * [MDEV-27416](https://jira.mariadb.org/browse/MDEV-27416) InnoDB hang in buf\_flush\_wait\_flushed(), on log checkpoint
* [Revision #eab89f14ab](https://github.com/MariaDB/server/commit/eab89f14ab)\
  2021-12-31 23:12:54 +0200
  * Deb: Adapt custom build steps to be compatible with latest Salsa-CI
* Merge [Revision #c9db50b585](https://github.com/MariaDB/server/commit/c9db50b585) 2022-01-03 07:23:49 +0200 - Merge 10.4 into 10.5
* [Revision #1df05a0854](https://github.com/MariaDB/server/commit/1df05a0854)\
  2022-01-03 07:23:39 +0200
  * Correct some copyright messages
* [Revision #c14dd0d19d](https://github.com/MariaDB/server/commit/c14dd0d19d)\
  2022-01-03 07:23:18 +0200
  * Cleanup: Remove RECV\_READ\_AHEAD\_AREA
* [Revision #89a0364fc8](https://github.com/MariaDB/server/commit/89a0364fc8)\
  2021-12-24 22:16:10 +0100
  * [MDEV-27304](https://jira.mariadb.org/browse/MDEV-27304) SHOW ... result columns are right-aligned
* Merge [Revision #55bb933a88](https://github.com/MariaDB/server/commit/55bb933a88) 2021-12-26 12:51:04 +0100 - Merge branch 10.4 into 10.5
* [Revision #be20b3b03f](https://github.com/MariaDB/server/commit/be20b3b03f)\
  2021-12-21 16:22:33 -0700
  * [MDEV-26919](https://jira.mariadb.org/browse/MDEV-26919): binlog.binlog\_truncate\_active\_log fails in bb with valgrind, Conditional jump or move depends on uninitialised value
* [Revision #6487b8e330](https://github.com/MariaDB/server/commit/6487b8e330)\
  2021-12-21 11:59:08 +0400
  * [MDEV-27307](https://jira.mariadb.org/browse/MDEV-27307) main.ctype\_utf8mb4\_uca\_allkeys tests fail with Valgrind/MSAN
* [Revision #2776635cb9](https://github.com/MariaDB/server/commit/2776635cb9)\
  2021-05-19 14:56:09 +1000
  * [MDEV-24788](https://jira.mariadb.org/browse/MDEV-24788): mariadbd --help Can't lock aria control file
* [Revision #03678bcf55](https://github.com/MariaDB/server/commit/03678bcf55)\
  2021-12-14 03:47:59 +0100
  * [MDEV-27181](https://jira.mariadb.org/browse/MDEV-27181): Galera SST scripts should use ssl\_capath for CA directory
* [Revision #88b339805d](https://github.com/MariaDB/server/commit/88b339805d)\
  2021-12-11 15:27:14 +0200
  * Fix a test for cmake -DPLUGIN\_PERFSCHEMA=NO
* [Revision #a9b5f59989](https://github.com/MariaDB/server/commit/a9b5f59989)\
  2021-12-08 14:06:33 +0100
  * enable rpl\_parallel2 test, as [MDEV-23089](https://jira.mariadb.org/browse/MDEV-23089) is fixed
* [Revision #62ea1b4407](https://github.com/MariaDB/server/commit/62ea1b4407)\
  2021-10-28 09:43:49 +0200
  * BUG#31761802 STATISTICS ANY QUERIES USING VIEWS ARE SUMMARIZED TOGETHER WITH THE VIEW DEFINITION SELECT
* [Revision #e27b1c3137](https://github.com/MariaDB/server/commit/e27b1c3137)\
  2021-11-05 15:12:14 +0100
  * require system pcre2 in rpms
* [Revision #88ac91c7cc](https://github.com/MariaDB/server/commit/88ac91c7cc)\
  2021-12-07 17:29:05 +0100
  * ColumnStore and S3 SUMMARY/DESCRIPTION for RPM
* Merge [Revision #de70f921ce](https://github.com/MariaDB/server/commit/de70f921ce) 2021-12-07 21:30:27 +0100 - Merge branch '10.4' into 10.5
* [Revision #cfcfdc65df](https://github.com/MariaDB/server/commit/cfcfdc65df)\
  2021-12-07 17:00:46 +0200
  * [MDEV-27190](https://jira.mariadb.org/browse/MDEV-27190) InnoDB upgrade from 10.2, 10.3, 10.4 is not crash-safe
* [Revision #890c55177d](https://github.com/MariaDB/server/commit/890c55177d)\
  2021-12-07 15:22:06 +0600
  * [MDEV-27183](https://jira.mariadb.org/browse/MDEV-27183) optimize std::map lookup in during crash recovery
* [Revision #0064316f19](https://github.com/MariaDB/server/commit/0064316f19)\
  2021-12-03 17:21:59 +0600
  * cleanup: reduce code bloat
* [Revision #fa1325512b](https://github.com/MariaDB/server/commit/fa1325512b)\
  2021-12-03 17:01:48 +0200
  * Correct some comments
* [Revision #5d7da02793](https://github.com/MariaDB/server/commit/5d7da02793)\
  2021-11-29 18:55:16 +0600
  * [MDEV-27139](https://jira.mariadb.org/browse/MDEV-27139) 32-bit systems fail to use big innodb-log-file-size
* Merge [Revision #d2a7710635](https://github.com/MariaDB/server/commit/d2a7710635) 2021-12-03 10:27:35 +0200 - Merge 10.4 into 10.5
* [Revision #f9726ced25](https://github.com/MariaDB/server/commit/f9726ced25)\
  2021-12-01 13:43:43 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) fixup: Correct a comment
* [Revision #4ebac0fc86](https://github.com/MariaDB/server/commit/4ebac0fc86)\
  2021-11-20 14:22:25 +1100
  * [MDEV-27088](https://jira.mariadb.org/browse/MDEV-27088): Server crash on ARM (WMM architecture) due to missing barriers in lf-hash (10.5)
* Merge [Revision #d4cb177603](https://github.com/MariaDB/server/commit/d4cb177603) 2021-11-29 11:16:20 +0200 - Merge 10.4 into 10.5
* Merge [Revision #ca26953924](https://github.com/MariaDB/server/commit/ca26953924) 2021-11-25 07:49:58 +0200 - Merge 10.4 into 10.5
* [Revision #cba065f4fe](https://github.com/MariaDB/server/commit/cba065f4fe)\
  2021-11-15 00:42:26 +0200
  * Json\_writer\_object add integers
* [Revision #691f7e165a](https://github.com/MariaDB/server/commit/691f7e165a)\
  2021-11-14 06:11:12 +0200
  * [MDEV-27036](https://jira.mariadb.org/browse/MDEV-27036): allow Json\_writer\_\[array|object] from Json\_writer
* [Revision #917b421012](https://github.com/MariaDB/server/commit/917b421012)\
  2021-11-24 12:05:44 +0200
  * [MDEV-26682](https://jira.mariadb.org/browse/MDEV-26682) fixup: GCC -Wunused-variable
* [Revision #6b2b510839](https://github.com/MariaDB/server/commit/6b2b510839)\
  2021-11-24 12:04:51 +0200
  * PFS\_events\_statements cleanup: Use offsetof
* [Revision #8d398710b3](https://github.com/MariaDB/server/commit/8d398710b3)\
  2021-11-08 14:45:17 +1100
  * Debian: comment default config
* Merge [Revision #5489ce0ae1](https://github.com/MariaDB/server/commit/5489ce0ae1) 2021-11-17 14:49:12 +0200 - Merge 10.4 into 10.5
* [Revision #ebb15f986f](https://github.com/MariaDB/server/commit/ebb15f986f)\
  2021-11-16 17:13:15 +0200
  * [MDEV-27059](https://jira.mariadb.org/browse/MDEV-27059) page\_zip\_dir\_insert() may corrupt ROW\_FORMAT=COMPRESSED tables
* Merge [Revision #09205a1c9a](https://github.com/MariaDB/server/commit/09205a1c9a) 2021-11-16 14:26:13 +0200 - Merge 10.4 into 10.5
* [Revision #0269d491ea](https://github.com/MariaDB/server/commit/0269d491ea)\
  2021-11-16 13:58:22 +0200
  * [MDEV-27047](https://jira.mariadb.org/browse/MDEV-27047): Replication fails to remove affected queries from query cache
* [Revision #079516f00e](https://github.com/MariaDB/server/commit/079516f00e)\
  2021-11-16 12:49:51 +0200
  * [MDEV-27016](https://jira.mariadb.org/browse/MDEV-27016): Assertion 'id.page\_no() < space.size' failed
* [Revision #72afeaf8a5](https://github.com/MariaDB/server/commit/72afeaf8a5)\
  2021-11-13 10:29:26 +0100
  * [MDEV-18439](https://jira.mariadb.org/browse/MDEV-18439) Windows builds should have core\_file=1 by default
* [Revision #5b21a8fafc](https://github.com/MariaDB/server/commit/5b21a8fafc)\
  2021-11-11 22:12:12 +0100
  * [MDEV-27030](https://jira.mariadb.org/browse/MDEV-27030) vcol.vcol\_keys\_myisam fails on Windows x64, with Visual Studio 2022
* Merge [Revision #9c18b96603](https://github.com/MariaDB/server/commit/9c18b96603) 2021-11-09 08:50:33 +0200 - Merge 10.4 into 10.5
* Merge [Revision #d8d6e99528](https://github.com/MariaDB/server/commit/d8d6e99528) 2021-11-08 19:40:39 +0100 - Merge branch '10.5' into bb-10.5-release
* [Revision #cf06eaf1af](https://github.com/MariaDB/server/commit/cf06eaf1af)\
  2021-11-08 12:21:07 -0500
  * bump the VERSION
* [Revision #bb200599ff](https://github.com/MariaDB/server/commit/bb200599ff)\
  2021-11-03 15:29:35 +0400
  * [MDEV-24584](https://jira.mariadb.org/browse/MDEV-24584) Selecting INT column with COLLATE utf8mb4\_general\_ci throws an error
* [Revision #5cae401b00](https://github.com/MariaDB/server/commit/5cae401b00)\
  2021-11-03 12:31:47 +0300
  * [MDEV-25555](https://jira.mariadb.org/browse/MDEV-25555) Server crashes in tree\_record\_pos after INPLACE-recreating index on HEAP table
* [Revision #b3bdc1c142](https://github.com/MariaDB/server/commit/b3bdc1c142)\
  2021-11-03 12:31:47 +0300
  * [MDEV-25803](https://jira.mariadb.org/browse/MDEV-25803) Inplace ALTER breaks MyISAM/Aria table when order of keys is changed

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
