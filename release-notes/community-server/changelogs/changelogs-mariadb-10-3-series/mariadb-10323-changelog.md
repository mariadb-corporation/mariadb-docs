# MariaDB 10.3.23 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.23/)[Release Notes](../../old-releases/10.3/10.3.23.md)[Changelog](mariadb-10323-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 12 May 2020

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.23.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.32](../changelogs-mariadb-102-series/mariadb-10232-changelog.md)
* Merge [Revision #607467bd63](https://github.com/MariaDB/server/commit/607467bd63) 2020-05-09 20:20:02 +0200 - Merge branch '10.2' into 10.3
* [Revision #1a9c593db8](https://github.com/MariaDB/server/commit/1a9c593db8)\
  2020-05-09 20:53:39 +0300
  * List of unstable tests for 10.3.23 release (updated)
* [Revision #54ba541b64](https://github.com/MariaDB/server/commit/54ba541b64)\
  2020-05-05 21:15:37 +0300
  * List of unstable tests for 10.3.23 release
* [Revision #7337abd2f7](https://github.com/MariaDB/server/commit/7337abd2f7)\
  2020-05-04 23:25:20 +0200
  * [MDEV-22123](https://jira.mariadb.org/browse/MDEV-22123) On RHEL8 mariadb-server is not provided
* [Revision #b22a4bf626](https://github.com/MariaDB/server/commit/b22a4bf626)\
  2020-05-04 22:58:14 +0200
  * [MDEV-21886](https://jira.mariadb.org/browse/MDEV-21886) MariaDB RPM upgrade overwrites PAM user map
* Merge [Revision #8648b9bed8](https://github.com/MariaDB/server/commit/8648b9bed8) 2020-05-04 22:06:00 +0300 - Merge 10.2 into 10.3
* Merge [Revision #7fb73ed143](https://github.com/MariaDB/server/commit/7fb73ed143) 2020-05-04 16:47:11 +0200 - Merge branch '10.2' into 10.3
* [Revision #42bba9782b](https://github.com/MariaDB/server/commit/42bba9782b)\
  2020-05-04 15:27:24 +0530
  * [MDEV-22446](https://jira.mariadb.org/browse/MDEV-22446) InnoDB aborts while adding instant column for discarded tablespace
* [Revision #ec9908b257](https://github.com/MariaDB/server/commit/ec9908b257)\
  2020-04-25 14:27:00 +0530
  * [MDEV-16288](https://jira.mariadb.org/browse/MDEV-16288) ALTER TABLE…ALGORITHM=DEFAULT does not override alter\_algorithm
* [Revision #f98017bb6d](https://github.com/MariaDB/server/commit/f98017bb6d)\
  2020-04-30 19:52:49 +0530
  * [MDEV-16288](https://jira.mariadb.org/browse/MDEV-16288) ALTER TABLE…ALGORITHM=DEFAULT does not override alter\_algorithm
* [Revision #644d9f38b9](https://github.com/MariaDB/server/commit/644d9f38b9)\
  2020-04-21 12:16:10 +0530
  * [MDEV-21480](https://jira.mariadb.org/browse/MDEV-21480): Unique key using ref access though eq\_ref access can be used
* [Revision #7f9dc0d84a](https://github.com/MariaDB/server/commit/7f9dc0d84a)\
  2020-04-28 00:40:13 +0300
  * split log\_t::buf into two buffers
* Merge [Revision #1fbdcada73](https://github.com/MariaDB/server/commit/1fbdcada73) 2020-04-28 22:29:13 +0300 - Merge 10.2 into 10.3
* [Revision #c755974775](https://github.com/MariaDB/server/commit/c755974775)\
  2020-04-25 13:49:40 +0530
  * [MDEV-19611](https://jira.mariadb.org/browse/MDEV-19611) INPLACE ALTER does not fail on bad implicit default value
* Merge [Revision #3568fad5c9](https://github.com/MariaDB/server/commit/3568fad5c9) 2020-04-27 15:40:39 +0300 - Merge 10.2 into 10.3
* [Revision #f7437d8a3c](https://github.com/MariaDB/server/commit/f7437d8a3c)\
  2020-04-27 14:29:23 +0300
  * Flag a result dependency on PLUGIN\_PERFSCHEMA
* Merge [Revision #2e12d471ea](https://github.com/MariaDB/server/commit/2e12d471ea) 2020-04-27 14:24:41 +0300 - Merge 10.2 into 10.3
* [Revision #61c0df9465](https://github.com/MariaDB/server/commit/61c0df9465)\
  2020-04-23 10:30:58 +0300
  * After-merge fix
* Merge [Revision #455cf6196c](https://github.com/MariaDB/server/commit/455cf6196c) 2020-04-22 14:45:55 +0300 - Merge 10.2 into 10.3
* [Revision #42af2b1d8b](https://github.com/MariaDB/server/commit/42af2b1d8b)\
  2020-04-16 22:56:51 +0200
  * [MDEV-22263](https://jira.mariadb.org/browse/MDEV-22263): main.func\_debug fails on a valgrind build with wrong result
* Merge [Revision #0155d64448](https://github.com/MariaDB/server/commit/0155d64448) 2020-04-17 10:28:57 +0900 - Merge commit '619a2ccd67813b98a92983fca70a93a8d32b9abe' into 10.3
* [Revision #619a2ccd67](https://github.com/MariaDB/server/commit/619a2ccd67)\
  2020-04-17 01:49:46 +0900
  * [MDEV-21884](https://jira.mariadb.org/browse/MDEV-21884) MariaDB with Spider crashes on a query
* [Revision #6577a7a8f2](https://github.com/MariaDB/server/commit/6577a7a8f2)\
  2020-04-15 13:10:51 +0300
  * fix tests related to SQL comment length
* Merge [Revision #84db10f27b](https://github.com/MariaDB/server/commit/84db10f27b) 2020-04-15 09:56:03 +0300 - Merge 10.2 into 10.3
* [Revision #9aacda409d](https://github.com/MariaDB/server/commit/9aacda409d)\
  2020-03-26 13:13:31 +1100
  * [MDEV-21984](https://jira.mariadb.org/browse/MDEV-21984): POWER crc32 acceleration - fix clang's behavior on versions >= 7
* [Revision #811e4409ce](https://github.com/MariaDB/server/commit/811e4409ce)\
  2020-03-16 13:07:52 +0200
  * Travis-CI: Shorten deb build log to keep it under 4 MB
* [Revision #396e83d777](https://github.com/MariaDB/server/commit/396e83d777)\
  2020-04-05 18:55:15 +0300
  * Travis-CI: Add missing build dependency dh-exec
* [Revision #21b8743734](https://github.com/MariaDB/server/commit/21b8743734)\
  2020-04-04 09:24:22 -0700
  * [MDEV-21673](https://jira.mariadb.org/browse/MDEV-21673) Calling stored procedure twice in the same session causes MariaDB to crash
* [Revision #fbef428645](https://github.com/MariaDB/server/commit/fbef428645)\
  2020-04-03 12:33:31 +0200
  * [MDEV-22137](https://jira.mariadb.org/browse/MDEV-22137) correct documentation of tcp\_keepalive\_time system variable
* [Revision #0932c5804d](https://github.com/MariaDB/server/commit/0932c5804d)\
  2020-04-02 20:48:38 +0300
  * [MDEV-20515](https://jira.mariadb.org/browse/MDEV-20515) multi-update tries to position updated table by null reference
* [Revision #ba34f409ad](https://github.com/MariaDB/server/commit/ba34f409ad)\
  2020-04-02 20:48:38 +0300
  * [MDEV-21688](https://jira.mariadb.org/browse/MDEV-21688) Assertion or ER\_WARN\_DATA\_OUT\_OF\_RANGE upon ALTER on previously versioned table
* [Revision #44c6c7a923](https://github.com/MariaDB/server/commit/44c6c7a923)\
  2020-04-02 20:48:38 +0300
  * [MDEV-21342](https://jira.mariadb.org/browse/MDEV-21342) Assertion in set\_ok\_status() upon spatial field error on system-versioned table
* [Revision #9149017bb8](https://github.com/MariaDB/server/commit/9149017bb8)\
  2020-04-02 22:37:36 +1000
  * [MDEV-17091](https://jira.mariadb.org/browse/MDEV-17091) - Assertion failed after dropping versioning
* [Revision #b40b3720cb](https://github.com/MariaDB/server/commit/b40b3720cb)\
  2020-04-02 00:39:54 +0400
  * [MDEV-21348](https://jira.mariadb.org/browse/MDEV-21348) - column compression memory leak
* [Revision #b092d35f13](https://github.com/MariaDB/server/commit/b092d35f13)\
  2020-03-30 12:31:54 +0300
  * [MDEV-20590](https://jira.mariadb.org/browse/MDEV-20590) Introduce a file format constraint to ALTER TABLE
* [Revision #f8ec3ba01b](https://github.com/MariaDB/server/commit/f8ec3ba01b)\
  2020-03-27 16:32:34 +0530
  * [MDEV-21832](https://jira.mariadb.org/browse/MDEV-21832) FORCE all partition to rebuild if any one of the partition does rebuild
* [Revision #67f2782413](https://github.com/MariaDB/server/commit/67f2782413)\
  2020-03-30 12:16:07 +0300
  * Fix GCC -Wstringop-truncation
* Merge [Revision #1a9b6c4c7f](https://github.com/MariaDB/server/commit/1a9b6c4c7f) 2020-03-30 11:12:56 +0300 - Merge 10.2 into 10.3
* [Revision #0fb84216a3](https://github.com/MariaDB/server/commit/0fb84216a3)\
  2020-03-26 19:39:51 +0200
  * Make mysql.innodb\_mysql\_lock deterministic
* [Revision #caf110fa52](https://github.com/MariaDB/server/commit/caf110fa52)\
  2020-03-23 19:20:48 -0700
  * [MDEV-21883](https://jira.mariadb.org/browse/MDEV-21883) Server crashes when joining a subselect with 32 tables and GROUP BY
* [Revision #fd5c36bed5](https://github.com/MariaDB/server/commit/fd5c36bed5)\
  2020-03-20 21:41:39 +0200
  * [MDEV-21959](https://jira.mariadb.org/browse/MDEV-21959): Fix a type mismatch on 64-bit systems
* Merge [Revision #44298e4dea](https://github.com/MariaDB/server/commit/44298e4dea) 2020-03-20 18:08:16 +0200 - Merge 10.2 into 10.3
* [Revision #dd68db0c17](https://github.com/MariaDB/server/commit/dd68db0c17)\
  2020-03-18 22:14:38 +0200
  * Change exec bit to allow dh-exec to work
* [Revision #2e0277373d](https://github.com/MariaDB/server/commit/2e0277373d)\
  2020-03-16 17:49:44 +0200
  * Fixed multi\_update\_debug.test
* [Revision #c7daabdb05](https://github.com/MariaDB/server/commit/c7daabdb05)\
  2020-03-16 10:10:11 +0200
  * [MDEV-13134](https://jira.mariadb.org/browse/MDEV-13134)/[MDEV-21855](https://jira.mariadb.org/browse/MDEV-21855): Add a test case
* Merge [Revision #5fe87ac413](https://github.com/MariaDB/server/commit/5fe87ac413) 2020-03-13 12:30:29 +0200 - Merge 10.2 into 10.3
* [Revision #51e9381dcc](https://github.com/MariaDB/server/commit/51e9381dcc)\
  2020-03-11 12:10:49 +0200
  * Add galera debug sync to galera\_slave\_replay test.
* [Revision #cebf43e166](https://github.com/MariaDB/server/commit/cebf43e166)\
  2020-03-11 22:04:06 +0200
  * Fixed wrong assert (found by clang)
* Merge [Revision #3c9bc0ce19](https://github.com/MariaDB/server/commit/3c9bc0ce19) 2020-03-11 14:05:41 +0100 - Merge branch '10.2' into 10.3
* [Revision #8fa1b6bb88](https://github.com/MariaDB/server/commit/8fa1b6bb88)\
  2018-02-20 15:35:09 +0300
  * [MDEV-15724](https://jira.mariadb.org/browse/MDEV-15724) - Possible crash in parser
* [Revision #fd2dc9c3fd](https://github.com/MariaDB/server/commit/fd2dc9c3fd)\
  2020-03-08 16:19:43 +0200
  * Correctly link mysqlclient.pc to mariadb.pc under multi-arch support
* Merge [Revision #1d99e4d674](https://github.com/MariaDB/server/commit/1d99e4d674) 2020-03-08 11:02:55 +0200 - Merge branch '10.2' into 10.3
* Merge [Revision #440452628d](https://github.com/MariaDB/server/commit/440452628d) 2020-03-06 23:28:26 +0100 - Merge branch '10.2' into 10.3
* [Revision #f8ab5ca374](https://github.com/MariaDB/server/commit/f8ab5ca374)\
  2020-02-28 14:40:00 +0100
  * [MDEV-20382](https://jira.mariadb.org/browse/MDEV-20382): SHOW PRIVILEGES displays "Delete versioning rows" rather than "Delete History"
* [Revision #a662cb9b43](https://github.com/MariaDB/server/commit/a662cb9b43)\
  2020-02-25 14:55:15 +0300
  * Better comments
* [Revision #cfa0506f8a](https://github.com/MariaDB/server/commit/cfa0506f8a)\
  2020-02-25 00:47:03 -0800
  * [MDEV-21554](https://jira.mariadb.org/browse/MDEV-21554) Crash in JOIN\_CACHE\_BKAH::skip\_index\_tuple when mrr=on and join\_cache\_level=6+
* [Revision #f6b9a29820](https://github.com/MariaDB/server/commit/f6b9a29820)\
  2019-10-15 15:03:53 +1100
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662): cmake remove empty INSTALL\_DEBUG\_TARGET
* [Revision #c749eb2b41](https://github.com/MariaDB/server/commit/c749eb2b41)\
  2019-10-15 14:35:46 +1100
  * [MDEV-16662](https://jira.mariadb.org/browse/MDEV-16662): cmake: CMP0026 compatible for dtrace
* [Revision #affe7fabc7](https://github.com/MariaDB/server/commit/affe7fabc7)\
  2020-02-19 21:27:38 +0300
  * [MDEV-21628](https://jira.mariadb.org/browse/MDEV-21628): Index condition pushdown condition ... not used with BKA
* [Revision #85d4a45d15](https://github.com/MariaDB/server/commit/85d4a45d15)\
  2020-02-09 22:27:51 +0200
  * Deb: Run 'wrap-and-sort -a' so comparison across releases is easier
* [Revision #1f0e72f874](https://github.com/MariaDB/server/commit/1f0e72f874)\
  2020-02-12 10:44:46 +0200
  * Deb: Remove unnecessary manual libzstd1 dependency from RocksDB plugin
* Merge [Revision #58b70dc136](https://github.com/MariaDB/server/commit/58b70dc136) 2020-02-10 20:34:16 +0100 - Merge branch '10.2' into 10.3
* [Revision #d72038a738](https://github.com/MariaDB/server/commit/d72038a738)\
  2020-02-07 14:18:17 +0200
  * [MDEV-21667](https://jira.mariadb.org/browse/MDEV-21667) : Galera test failure on MW-336
* [Revision #a30ab52635](https://github.com/MariaDB/server/commit/a30ab52635)\
  2020-01-31 08:05:41 +0200
  * [MDEV-21601](https://jira.mariadb.org/browse/MDEV-21601) : Cleanup Galera disabled tests
* [Revision #8d7462ec49](https://github.com/MariaDB/server/commit/8d7462ec49)\
  2020-02-07 19:42:11 -0800
  * [MDEV-21614](https://jira.mariadb.org/browse/MDEV-21614) Wrong query results with optimizer\_switch="split\_materialized=on"
* [Revision #fafb35ee51](https://github.com/MariaDB/server/commit/fafb35ee51)\
  2019-11-06 12:35:19 +0100
  * [MDEV-20076](https://jira.mariadb.org/browse/MDEV-20076): SHOW GRANTS does not quote role names properly
* [Revision #b3ded21922](https://github.com/MariaDB/server/commit/b3ded21922)\
  2020-02-05 00:54:16 +0300
  * ha\_partition: add comments, comment out unused member variables
* [Revision #b0fa308086](https://github.com/MariaDB/server/commit/b0fa308086)\
  2020-02-02 15:13:29 +0300
  * [MDEV-21195](https://jira.mariadb.org/browse/MDEV-21195) INSERT chooses wrong partition for RANGE partitioning by DECIMAL column
* [Revision #74deeaee34](https://github.com/MariaDB/server/commit/74deeaee34)\
  2020-02-02 15:13:29 +0300
  * [MDEV-21317](https://jira.mariadb.org/browse/MDEV-21317) mysqlhotcopy and transaction\_registry table
* [Revision #e13e49e5ab](https://github.com/MariaDB/server/commit/e13e49e5ab)\
  2020-02-02 15:13:29 +0300
  * [MDEV-20528](https://jira.mariadb.org/browse/MDEV-20528) innodb.purge\_secondary\_[MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222) failed in buildbot, debug sync point wait timed out
* [Revision #006f6f97b1](https://github.com/MariaDB/server/commit/006f6f97b1)\
  2020-02-02 15:13:29 +0300
  * [MDEV-17798](https://jira.mariadb.org/browse/MDEV-17798) System variable system\_versioning\_asof accepts wrong values
* [Revision #14e6f0251c](https://github.com/MariaDB/server/commit/14e6f0251c)\
  2020-02-02 15:13:29 +0300
  * [MDEV-20955](https://jira.mariadb.org/browse/MDEV-20955) versioning.update failed in buildbot with wrong result code
* [Revision #c8bd8d5c64](https://github.com/MariaDB/server/commit/c8bd8d5c64)\
  2020-01-31 13:16:11 +0200
  * [MDEV-14330](https://jira.mariadb.org/browse/MDEV-14330): After-merge fix
* Merge [Revision #5ff66fb0b9](https://github.com/MariaDB/server/commit/5ff66fb0b9) 2020-01-31 11:37:12 +0200 - Merge 10.2 into 10.3
* Merge [Revision #dbbe9961a5](https://github.com/MariaDB/server/commit/dbbe9961a5) 2020-01-28 09:28:18 +0100 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #8b8d333d7f](https://github.com/MariaDB/server/commit/8b8d333d7f)\
  2020-01-27 15:10:11 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
