# MariaDB 10.3.17 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.17/)[Release Notes](../../old-releases/10.3/10.3.17.md)[Changelog](mariadb-10317-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 31 Jul 2019

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.17.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.26](../changelogs-mariadb-102-series/mariadb-10226-changelog.md)
* [Revision #4b5a14d0fe](https://github.com/MariaDB/server/commit/4b5a14d0fe)\
  2019-07-28 03:14:33 +0300
  * List of unstable tests for 10.3.17 release (updated)
* [Revision #5e112a2620](https://github.com/MariaDB/server/commit/5e112a2620)\
  2019-07-27 07:50:12 +0200
  * Fix Windows packaging.
* [Revision #7a8747f757](https://github.com/MariaDB/server/commit/7a8747f757)\
  2019-07-27 10:01:12 +0200
  * Changes of merge moved to oracle mode parser.
* [Revision #8990e3e2b9](https://github.com/MariaDB/server/commit/8990e3e2b9)\
  2019-07-26 23:04:12 +0200
  * Fix initialiser.
* Merge [Revision #d97342b6f2](https://github.com/MariaDB/server/commit/d97342b6f2) 2019-07-26 22:42:35 +0200 - Merge branch '10.2' into 10.3
* [Revision #00a254cc06](https://github.com/MariaDB/server/commit/00a254cc06)\
  2019-07-26 17:29:52 +0300
  * [MDEV-20186](https://jira.mariadb.org/browse/MDEV-20186) Wrong result or Assertion on INSERT after DELETE HISTORY
* [Revision #29df1003d9](https://github.com/MariaDB/server/commit/29df1003d9)\
  2019-07-26 13:52:52 +0300
  * [MDEV-20184](https://jira.mariadb.org/browse/MDEV-20184) data race at global counter btr\_cur\_n\_non\_sea
* [Revision #7db999322c](https://github.com/MariaDB/server/commit/7db999322c)\
  2019-07-26 12:36:06 +0300
  * [MDEV-20183](https://jira.mariadb.org/browse/MDEV-20183) data race at safe\_mutex\_lock()
* [Revision #51d58f566a](https://github.com/MariaDB/server/commit/51d58f566a)\
  2019-07-26 08:44:43 +0400
  * [MDEV-18350](https://jira.mariadb.org/browse/MDEV-18350) Using audit plugin with MySQL, mysqld crashes when running COM\_INIT\_DB against invalid database.
* [Revision #f6d0d309fa](https://github.com/MariaDB/server/commit/f6d0d309fa)\
  2019-07-23 13:27:57 +0300
  * [MDEV-19814](https://jira.mariadb.org/browse/MDEV-19814) Assertion \`update->n\_fields < ulint(table->n\_cols + table->n\_v\_cols)' on DELETE HISTORY
* [Revision #1a73444d57](https://github.com/MariaDB/server/commit/1a73444d57)\
  2019-07-23 13:37:18 +0300
  * Cleanups: DELETE HISTORY \[[MDEV-19814](https://jira.mariadb.org/browse/MDEV-19814)]
* Merge [Revision #f3eb82f048](https://github.com/MariaDB/server/commit/f3eb82f048) 2019-07-25 18:09:34 +0300 - Merge 10.2 into 10.3
* Merge [Revision #75e1b1a088](https://github.com/MariaDB/server/commit/75e1b1a088) 2019-07-25 17:44:25 +0300 - Merge 10.2 into 10.3
* Merge [Revision #fdef9f9b89](https://github.com/MariaDB/server/commit/fdef9f9b89) 2019-07-25 15:31:11 +0300 - Merge 10.2 into 10.3
* [Revision #55d8ff0de8](https://github.com/MariaDB/server/commit/55d8ff0de8)\
  2019-07-04 22:38:47 -0700
  * [MDEV-19948](https://jira.mariadb.org/browse/MDEV-19948) `SHOW GRANTS FOR user` return privileges individually
* [Revision #0d99ccea1e](https://github.com/MariaDB/server/commit/0d99ccea1e)\
  2019-07-24 20:35:21 +0300
  * List of unstable tests for 10.3.17 release
* Merge [Revision #b951fc4e7f](https://github.com/MariaDB/server/commit/b951fc4e7f) 2019-07-24 15:34:24 +0300 - Merge 10.2 into 10.3
* [Revision #33215edcba](https://github.com/MariaDB/server/commit/33215edcba)\
  2019-07-24 15:30:27 +0300
  * Resolve conflicts in wsrep.variables
* Merge [Revision #70b226d966](https://github.com/MariaDB/server/commit/70b226d966) 2019-07-22 17:37:04 +0300 - Merge 10.2 into 10.3
* [Revision #abeacb9c82](https://github.com/MariaDB/server/commit/abeacb9c82)\
  2019-07-22 12:20:49 +0200
  * The test for the wsrep\_info plugin needs the same flexible wsrep version checking as the tests for Galera (continuation of [MDEV-18565](https://jira.mariadb.org/browse/MDEV-18565) task)
* [Revision #559584fd9a](https://github.com/MariaDB/server/commit/559584fd9a)\
  2019-07-22 02:12:46 -0700
  * Fix typo and example in comment/KB for `setval()`
* Merge [Revision #ef44ec4afa](https://github.com/MariaDB/server/commit/ef44ec4afa) 2019-07-19 12:31:56 +0300 - Merge 10.2 into 10.3
* [Revision #7e4ea4189a](https://github.com/MariaDB/server/commit/7e4ea4189a)\
  2019-07-19 11:48:36 +0300
  * Disable a test due to [MDEV-20101](https://jira.mariadb.org/browse/MDEV-20101)
* [Revision #8f35b32595](https://github.com/MariaDB/server/commit/8f35b32595)\
  2019-07-18 15:11:32 +0200
  * wsrep\_check\_version binary is added to .gitignore
* [Revision #0a6b21b673](https://github.com/MariaDB/server/commit/0a6b21b673)\
  2019-07-18 14:31:07 +0200
  * Fixed dependency checking in some Galera tests + remove duplicates
* [Revision #a842387fef](https://github.com/MariaDB/server/commit/a842387fef)\
  2019-07-18 11:39:05 +0200
  * Set the garbd\_exe variable to empty string to avoid warning about an uninitialized variable when wsrep\_provider is not initialized correctly, set to 'none' or when wsrep is switched off
* [Revision #4c7a92a565](https://github.com/MariaDB/server/commit/4c7a92a565)\
  2019-07-17 12:59:27 +0200
  * Added missing installation target (merge [MDEV-18565](https://jira.mariadb.org/browse/MDEV-18565) from 10.2 into 10.3)
* Merge [Revision #0f83c8878d](https://github.com/MariaDB/server/commit/0f83c8878d) 2019-07-16 15:42:36 +0300 - Merge 10.2 into 10.3
* [Revision #aa96e56c55](https://github.com/MariaDB/server/commit/aa96e56c55)\
  2019-07-09 16:54:08 +0200
  * Improved error messages and added another path to the version check utility
* [Revision #06ad00a478](https://github.com/MariaDB/server/commit/06ad00a478)\
  2019-07-12 19:31:57 +0200
  * compilation error with gcc 8.3.0
* [Revision #d78a14c599](https://github.com/MariaDB/server/commit/d78a14c599)\
  2019-07-12 19:16:19 +0200
  * cmake 3.14.3 warnings
* [Revision #ee8477f9dc](https://github.com/MariaDB/server/commit/ee8477f9dc)\
  2019-07-08 17:03:16 +0200
  * [MDEV-17627](https://jira.mariadb.org/browse/MDEV-17627) Assertion \`inited==RND' failed in handler::ha\_rnd\_end() upon actions on partitioned table with FTS
* [Revision #07b1a26c33](https://github.com/MariaDB/server/commit/07b1a26c33)\
  2019-07-10 13:24:10 +0530
  * [MDEV-19630](https://jira.mariadb.org/browse/MDEV-19630) ALTER TABLE ... ADD COLUMN damages foreign keys which are pointed to the table being altered Problem: ======== InnoDB failed to change the column name present in foreign key cache for instant add column. So it leads to column mismatch for the consecutive rename of column.
* [Revision #7df17ca8aa](https://github.com/MariaDB/server/commit/7df17ca8aa)\
  2019-07-10 13:21:40 +0530
  * [MDEV-19974](https://jira.mariadb.org/browse/MDEV-19974) InnoDB: Cannot load compressed BLOB
* [Revision #cf7a8b9eb2](https://github.com/MariaDB/server/commit/cf7a8b9eb2)\
  2019-06-25 10:53:33 +0300
  * [MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222) Assertion \`0' failed in row\_purge\_remove\_sec\_if\_poss\_leaf on table with virtual columns and indexes
* [Revision #b0dd048edd](https://github.com/MariaDB/server/commit/b0dd048edd)\
  2019-05-27 23:29:43 +0300
  * [MDEV-19175](https://jira.mariadb.org/browse/MDEV-19175) Server crashes in ha\_partition::vers\_can\_native upon INSERT DELAYED into versioned partitioned table
* [Revision #3ffa06bc20](https://github.com/MariaDB/server/commit/3ffa06bc20)\
  2019-06-25 18:26:09 +0300
  * Tests: versioning suite fix when no test\_versioning plugin
* [Revision #e91fb70f99](https://github.com/MariaDB/server/commit/e91fb70f99)\
  2019-06-17 11:44:53 +0300
  * [MDEV-19785](https://jira.mariadb.org/browse/MDEV-19785) Storage CONNECT compilation error: unknown type name 'UNZFAM'
* [Revision #41f4f6bea8](https://github.com/MariaDB/server/commit/41f4f6bea8)\
  2019-07-09 08:25:44 +0200
  * [MDEV-18565](https://jira.mariadb.org/browse/MDEV-18565): Galera mtr-suite fails if galera library is not installed (#1243)
* [Revision #099007c3c9](https://github.com/MariaDB/server/commit/099007c3c9)\
  2019-07-03 16:08:26 +0300
  * [MDEV-19936](https://jira.mariadb.org/browse/MDEV-19936): MyRocks: compile fails on Windows
* [Revision #7d580ad141](https://github.com/MariaDB/server/commit/7d580ad141)\
  2019-07-03 10:58:40 +0300
  * [MDEV-19936](https://jira.mariadb.org/browse/MDEV-19936): MyRocks: compile fails on Windows
* Merge [Revision #1d45b3b055](https://github.com/MariaDB/server/commit/1d45b3b055) 2019-07-02 21:41:40 +0300 - Merge 10.2 into 10.3
* Merge [Revision #e82fe21e3a](https://github.com/MariaDB/server/commit/e82fe21e3a) 2019-07-02 17:46:22 +0300 - Merge 10.2 into 10.3
* [Revision #709f0510e3](https://github.com/MariaDB/server/commit/709f0510e3)\
  2019-07-02 17:44:05 +0300
  * [MDEV-19845](https://jira.mariadb.org/browse/MDEV-19845): Adjust for Skylake based on benchmarks
* [Revision #0e1ba364a1](https://github.com/MariaDB/server/commit/0e1ba364a1)\
  2019-07-01 18:24:54 +0300
  * [MDEV-19916](https://jira.mariadb.org/browse/MDEV-19916) Corruption after instant ADD/DROP and shrinking the tree
* [Revision #92bbf4f53d](https://github.com/MariaDB/server/commit/92bbf4f53d)\
  2019-07-01 18:24:35 +0300
  * [MDEV-19916](https://jira.mariadb.org/browse/MDEV-19916): Improve page\_validate()
* [Revision #685b527f0c](https://github.com/MariaDB/server/commit/685b527f0c)\
  2019-07-01 16:56:16 +0300
  * [MDEV-16060](https://jira.mariadb.org/browse/MDEV-16060): Speed up the test by 1 second
* [Revision #9053047f3d](https://github.com/MariaDB/server/commit/9053047f3d)\
  2019-06-27 18:51:34 +0300
  * [MDEV-17551](https://jira.mariadb.org/browse/MDEV-17551) assert or crashed table when using blobs
* [Revision #f5c080c735](https://github.com/MariaDB/server/commit/f5c080c735)\
  2019-06-27 14:58:43 +0300
  * [MDEV-19845](https://jira.mariadb.org/browse/MDEV-19845): Fix the build on some platforms
* [Revision #0b7fa5a05d](https://github.com/MariaDB/server/commit/0b7fa5a05d)\
  2019-06-27 12:19:51 +0300
  * [MDEV-19845](https://jira.mariadb.org/browse/MDEV-19845): Fix the build on some x86 targets
* [Revision #042fc29597](https://github.com/MariaDB/server/commit/042fc29597)\
  2019-06-27 10:53:18 +0300
  * [MDEV-19845](https://jira.mariadb.org/browse/MDEV-19845): Adaptive spin loops
* [Revision #620f4f8af9](https://github.com/MariaDB/server/commit/620f4f8af9)\
  2019-06-20 01:15:40 -0700
  * [MDEV-17429](https://jira.mariadb.org/browse/MDEV-17429) mysqldump uses 10.3 options with pre-10.3 servers and breaks
* [Revision #68c15eee3f](https://github.com/MariaDB/server/commit/68c15eee3f)\
  2019-06-21 15:17:06 +0200
  * [MDEV-19643](https://jira.mariadb.org/browse/MDEV-19643) : Fix semisync on Windows
* Merge [Revision #192aa295b4](https://github.com/MariaDB/server/commit/192aa295b4) 2019-06-19 08:56:10 +0300 - Merge 10.2 into 10.3
* [Revision #03f3ba2dcb](https://github.com/MariaDB/server/commit/03f3ba2dcb)\
  2019-06-18 11:29:54 +0200
  * [MDEV-18940](https://jira.mariadb.org/browse/MDEV-18940) Galera: Rolling upgrade: all nodes except upgraded node5 failed with Assertion \`meta->gtid.seqno == wsrep\_thd\_trx\_seqno(thd)' with SEQUENCEs (#1342)
* [Revision #5352e9687a](https://github.com/MariaDB/server/commit/5352e9687a)\
  2019-06-18 04:58:15 +0400
  * [MDEV-17363](https://jira.mariadb.org/browse/MDEV-17363) - Compressed columns cannot be restored from dump
* [Revision #3784ed7a62](https://github.com/MariaDB/server/commit/3784ed7a62)\
  2019-06-17 10:51:41 -0400
  * bump the VERSION
* [Revision #a626abb669](https://github.com/MariaDB/server/commit/a626abb669)\
  2018-09-25 17:58:39 +1000
  * Fix LEX\_CSTRING passed as argument of printf-like functions
* [Revision #fb5ee3ff96](https://github.com/MariaDB/server/commit/fb5ee3ff96)\
  2019-06-14 10:07:23 +0300
  * Fixed that ma\_test\_all.sh works
* [Revision #86faa98bd7](https://github.com/MariaDB/server/commit/86faa98bd7)\
  2019-06-13 17:53:57 +0300
  * Removed -fno-rtti from BUILD scripts
* [Revision #95d783af62](https://github.com/MariaDB/server/commit/95d783af62)\
  2019-06-15 21:30:44 +0200
  * fix versioning.simple for embedded

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
