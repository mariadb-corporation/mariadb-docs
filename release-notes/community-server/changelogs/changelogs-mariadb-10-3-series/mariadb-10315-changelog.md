# MariaDB 10.3.15 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/10.3/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/10.3/10.3.39.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.15/)[Release Notes](../../old-releases/10.3/10.3.15.md)[Changelog](mariadb-10315-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 14 May 2019

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.15.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.24](../changelogs-mariadb-102-series/mariadb-10224-changelog.md)
* [Revision #07aef9f7eb](https://github.com/MariaDB/server/commit/07aef9f7eb)\
  2019-05-13 20:53:34 +0300
  * Updated list of unstable tests for 10.3.15 release
* [Revision #5c93509aad](https://github.com/MariaDB/server/commit/5c93509aad)\
  2019-05-13 08:34:23 +0300
  * After-merge fix: Correct a copyright statement
* Merge [Revision #c51f85f882](https://github.com/MariaDB/server/commit/c51f85f882) 2019-05-12 17:20:23 +0200 - Merge branch '10.2' into 10.3
* [Revision #8ce702aa90](https://github.com/MariaDB/server/commit/8ce702aa90)\
  2019-05-10 10:49:09 +0300
  * [MDEV-17540](https://jira.mariadb.org/browse/MDEV-17540) Server crashes in row\_purge after TRUNCATE TABLE
* Merge [Revision #b2f3755c8e](https://github.com/MariaDB/server/commit/b2f3755c8e) 2019-05-10 08:02:21 +0300 - Merge 10.1 into 10.2
* [Revision #3e8cab51cb](https://github.com/MariaDB/server/commit/3e8cab51cb)\
  2019-05-07 12:53:50 +0530
  * [MDEV-13893](https://jira.mariadb.org/browse/MDEV-13893) encryption.innodb-redo-badkey failed in buildbot with page cannot be decrypted
* [Revision #542f32649b](https://github.com/MariaDB/server/commit/542f32649b)\
  2019-05-09 10:41:10 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): race condition in fts\_get\_table\_name()
* [Revision #f3718a112a](https://github.com/MariaDB/server/commit/f3718a112a)\
  2019-05-09 09:31:30 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): Backport some code from [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md)
* [Revision #f92749ed36](https://github.com/MariaDB/server/commit/f92749ed36)\
  2019-05-08 12:18:52 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): heap-use-after-free in fts\_get\_table\_name\_prefix()
* [Revision #5b3f7c0c33](https://github.com/MariaDB/server/commit/5b3f7c0c33)\
  2019-05-09 14:08:49 +0300
  * [MDEV-18220](https://jira.mariadb.org/browse/MDEV-18220): Remove some redundant data structures
* [Revision #06442e3e9f](https://github.com/MariaDB/server/commit/06442e3e9f)\
  2019-05-06 22:30:35 +0300
  * [MDEV-19399](https://jira.mariadb.org/browse/MDEV-19399) do not call slow my\_timer\_init() several times
* [Revision #d0ee3b5500](https://github.com/MariaDB/server/commit/d0ee3b5500)\
  2019-05-09 16:55:08 +0200
  * [MDEV-19427](https://jira.mariadb.org/browse/MDEV-19427) mysql\_upgrade\_service throws exception upgrading from 10.0 to 10.3
* [Revision #410585ca63](https://github.com/MariaDB/server/commit/410585ca63)\
  2019-05-01 15:22:22 +0400
  * Removed dead code
* [Revision #d0b73fb8d3](https://github.com/MariaDB/server/commit/d0b73fb8d3)\
  2019-03-29 19:08:22 +0400
  * [MDEV-16060](https://jira.mariadb.org/browse/MDEV-16060) - InnoDB: Failing assertion: ut\_strcmp(index->name, key->name)
* [Revision #136a27d9f1](https://github.com/MariaDB/server/commit/136a27d9f1)\
  2019-05-09 11:55:54 -0400
  * bump the VERSION
* [Revision #8f9c8579d0](https://github.com/MariaDB/server/commit/8f9c8579d0)\
  2019-01-09 15:00:56 +0200
  * Appveyor configuration and addition of badge
* Merge [Revision #9d3e2a7ca2](https://github.com/MariaDB/server/commit/9d3e2a7ca2) 2019-05-08 20:05:30 +0300 - Merge 10.1 into 10.2
* [Revision #3e5526b0df](https://github.com/MariaDB/server/commit/3e5526b0df)\
  2019-05-08 09:54:26 -0400
  * bump the VERSION
* Merge [Revision #4ad720282d](https://github.com/MariaDB/server/commit/4ad720282d) 2019-05-08 16:46:38 +0300 - Null merge mariadb-10.1.40 into 10.1
* [Revision #f92f313368](https://github.com/MariaDB/server/commit/f92f313368)\
  2019-05-07 16:41:07 -0400
  * bump the VERSION
* [Revision #101144f279](https://github.com/MariaDB/server/commit/101144f279)\
  2019-05-06 12:12:10 +0200
  * [MDEV-17640](https://jira.mariadb.org/browse/MDEV-17640) UMASK\_DIR configuration for mysql\_install\_db is not applied to mysql database
* [Revision #7b93d71a4b](https://github.com/MariaDB/server/commit/7b93d71a4b)\
  2019-05-07 15:21:41 +0530
  * [MDEV-19387](https://jira.mariadb.org/browse/MDEV-19387) innodb\_ft\_result\_cache\_limit\_32 fails on s390x
* [Revision #db9622f1f5](https://github.com/MariaDB/server/commit/db9622f1f5)\
  2019-05-07 12:51:59 +0300
  * [MDEV-19405](https://jira.mariadb.org/browse/MDEV-19405): Galera test failure on galera\_parallel\_autoinc\_largetrx
* [Revision #27232a9fa2](https://github.com/MariaDB/server/commit/27232a9fa2)\
  2018-05-31 17:42:54 -0700
  * edit MariaDB license info so that GitHub recognizes it
* [Revision #f2e27d53da](https://github.com/MariaDB/server/commit/f2e27d53da)\
  2019-04-24 12:47:40 +0300
  * [MDEV-19139](https://jira.mariadb.org/browse/MDEV-19139): pushdown condition with Item\_func\_set\_user\_var
* [Revision #a89f199c64](https://github.com/MariaDB/server/commit/a89f199c64)\
  2019-05-10 15:48:33 +0300
  * Fixed compiler warning in pcregrep.c
* [Revision #0c405b064d](https://github.com/MariaDB/server/commit/0c405b064d)\
  2019-05-09 12:31:59 +0300
  * [MDEV-18009](https://jira.mariadb.org/browse/MDEV-18009): Clean up the test case
* [Revision #646a3bd72d](https://github.com/MariaDB/server/commit/646a3bd72d)\
  2018-12-20 14:21:14 +0200
  * [MDEV-18009](https://jira.mariadb.org/browse/MDEV-18009) Missing redo log flush in innodb.instant\_alter\_crash
* [Revision #09aa5d3f69](https://github.com/MariaDB/server/commit/09aa5d3f69)\
  2019-05-08 00:08:09 -0700
  * [MDEV-17894](https://jira.mariadb.org/browse/MDEV-17894) Assertion \`(thd->lex)->current\_select' failed in MYSQLparse(), query with VALUES()
* [Revision #9d805004d8](https://github.com/MariaDB/server/commit/9d805004d8)\
  2019-05-08 15:00:16 +0400
  * Added missing reset\_changed()
* [Revision #88961a28e2](https://github.com/MariaDB/server/commit/88961a28e2)\
  2019-05-04 23:32:45 +0200
  * [MDEV-17710](https://jira.mariadb.org/browse/MDEV-17710) "unknown error" with FLUSH LOGS if log directory is not writeable
* [Revision #15c79c41e4](https://github.com/MariaDB/server/commit/15c79c41e4)\
  2019-05-04 13:11:25 +0200
  * [MDEV-17845](https://jira.mariadb.org/browse/MDEV-17845) Extreme high open file limit used
* [Revision #3d7e06d4ab](https://github.com/MariaDB/server/commit/3d7e06d4ab)\
  2019-05-02 14:31:36 +0200
  * cleanup: remove dead code
* [Revision #ffb83ba650](https://github.com/MariaDB/server/commit/ffb83ba650)\
  2019-05-02 13:09:27 +0200
  * cleanup: move checksum code to handler class
* [Revision #651a43e0a0](https://github.com/MariaDB/server/commit/651a43e0a0)\
  2019-05-07 16:13:53 +0400
  * [MDEV-18782](https://jira.mariadb.org/browse/MDEV-18782) mysqldump --all-databases causes segmentation fault.
* [Revision #26cb9f75ee](https://github.com/MariaDB/server/commit/26cb9f75ee)\
  2019-05-07 15:16:45 +0300
  * [MDEV-19404](https://jira.mariadb.org/browse/MDEV-19404): Assertion failure on !is\_thread\_specific || (mysqld\_server\_initialized && thd)
* [Revision #e8dd18a474](https://github.com/MariaDB/server/commit/e8dd18a474)\
  2019-05-04 12:43:29 +0400
  * Restore vars\_list destructor
* Merge [Revision #b6f4cccd19](https://github.com/MariaDB/server/commit/b6f4cccd19) 2019-05-03 20:14:09 +0300 - Merge 10.2 into 10.3
* [Revision #779fb636da](https://github.com/MariaDB/server/commit/779fb636da)\
  2019-03-20 18:35:20 +0400
  * Revert THD::THD(skip\_global\_sys\_var\_lock) argument
* [Revision #894df7edb6](https://github.com/MariaDB/server/commit/894df7edb6)\
  2019-03-21 00:42:48 +0400
  * Adieu find\_sys\_var\_ex()
* [Revision #53671a1fff](https://github.com/MariaDB/server/commit/53671a1fff)\
  2019-03-20 01:32:10 +0400
  * Make connect speed great again
* [Revision #1b5cf2f7e7](https://github.com/MariaDB/server/commit/1b5cf2f7e7)\
  2019-03-19 20:04:10 +0400
  * Safe session\_track\_system\_variables snapshot
* [Revision #554ac6f393](https://github.com/MariaDB/server/commit/554ac6f393)\
  2019-03-19 00:40:26 +0400
  * Allocate Session\_sysvars\_tracker statically
* [Revision #a7adc2ce16](https://github.com/MariaDB/server/commit/a7adc2ce16)\
  2019-03-18 19:18:54 +0400
  * Allocate Transaction\_state\_tracker statically
* [Revision #47bd06d55e](https://github.com/MariaDB/server/commit/47bd06d55e)\
  2019-03-18 17:13:00 +0400
  * Static current schema and state change trackers
* [Revision #01e8f3c52b](https://github.com/MariaDB/server/commit/01e8f3c52b)\
  2019-03-13 13:41:18 +0400
  * Allocate orig\_list statically
* [Revision #55bdd7f7b4](https://github.com/MariaDB/server/commit/55bdd7f7b4)\
  2019-03-13 12:20:11 +0400
  * Get rid of not implemented SESSION\_GTIDS\_TRACKER
* [Revision #2be28a91b1](https://github.com/MariaDB/server/commit/2be28a91b1)\
  2019-03-15 11:52:26 +0400
  * Cleanup session tracker API
* [Revision #19d5ddccfd](https://github.com/MariaDB/server/commit/19d5ddccfd)\
  2019-03-13 14:16:49 +0400
  * Cleanup session tracker redundancy
* [Revision #8f594b3384](https://github.com/MariaDB/server/commit/8f594b3384)\
  2019-03-18 14:43:14 +0400
  * Session\_sysvars\_tracker::vars\_list cleanups
* [Revision #0e91e0c377](https://github.com/MariaDB/server/commit/0e91e0c377)\
  2019-03-13 14:41:52 +0400
  * A proper State\_tracker::m\_changed enacpsulation
* [Revision #879878e43d](https://github.com/MariaDB/server/commit/879878e43d)\
  2019-05-02 14:38:43 +0530
  * [MDEV-18943](https://jira.mariadb.org/browse/MDEV-18943): Group Concat with limit not working with views
* Merge [Revision #5182348316](https://github.com/MariaDB/server/commit/5182348316) 2019-05-02 21:45:13 +0300 - Merge 10.2 into 10.3
* Merge [Revision #158247d3bd](https://github.com/MariaDB/server/commit/158247d3bd) 2019-05-02 21:43:24 +0300 - Merge 10.2 into 10.3
* [Revision #0d6fb43e6d](https://github.com/MariaDB/server/commit/0d6fb43e6d)\
  2019-05-02 16:49:47 +0300
  * Fixed some compilation warnings/errors
* [Revision #d46ffaf6af](https://github.com/MariaDB/server/commit/d46ffaf6af)\
  2018-12-19 16:48:07 +0300
  * [MDEV-17655](https://jira.mariadb.org/browse/MDEV-17655) Inconsistent grant-name usage between grant-statement and privilege tables
* [Revision #0fd5ecb03c](https://github.com/MariaDB/server/commit/0fd5ecb03c)\
  2019-05-02 10:12:35 +0530
  * Adjust the result for join\_cache.test
* [Revision #cb9fa1a08b](https://github.com/MariaDB/server/commit/cb9fa1a08b)\
  2019-04-30 21:05:50 +0530
  * [MDEV-9959](https://jira.mariadb.org/browse/MDEV-9959): A serious MariaDB server performance bug
* [Revision #8c8bee0a56](https://github.com/MariaDB/server/commit/8c8bee0a56)\
  2019-04-30 15:51:49 +0400
  * [MDEV-10307](https://jira.mariadb.org/browse/MDEV-10307) CAST(11068046444225730969 AS SIGNED) does not return a warning
* Merge [Revision #447b8ba164](https://github.com/MariaDB/server/commit/447b8ba164) 2019-04-29 17:54:10 +0300 - Merge 10.2 into 10.3
* Merge [Revision #4d59f45260](https://github.com/MariaDB/server/commit/4d59f45260) 2019-04-27 20:41:31 +0300 - Merge 10.2 into 10.3
* Merge [Revision #acf6f92aa9](https://github.com/MariaDB/server/commit/acf6f92aa9) 2019-04-25 09:05:52 +0300 - Merge 10.2 into 10.3
* [Revision #765ae6e821](https://github.com/MariaDB/server/commit/765ae6e821)\
  2019-04-21 12:07:30 +0400
  * [MDEV-19239](https://jira.mariadb.org/browse/MDEV-19239) ERROR 1300 (HY000): Invalid utf8 character string in 10.3.13-MariaDB
* [Revision #f4019f5b35](https://github.com/MariaDB/server/commit/f4019f5b35)\
  2019-04-20 00:11:50 +0400
  * Backporting from 10.4 to 10.3: [MDEV-17325](https://jira.mariadb.org/browse/MDEV-17325) NULL-ability problems with LEAST() in combination with NO\_ZERO\_DATE and NO\_ZERO\_IN\_DATE
* [Revision #42c58b87da](https://github.com/MariaDB/server/commit/42c58b87da)\
  2019-04-17 15:32:30 +0300
  * [MDEV-18096](https://jira.mariadb.org/browse/MDEV-18096) The server would crash when has configs rpl\_semi\_sync\_master\_enabled = OFF rpl\_semi\_sync\_master\_wait\_no\_slave = OFF
* [Revision #323e6cd74c](https://github.com/MariaDB/server/commit/323e6cd74c)\
  2019-04-18 08:34:08 +0400
  * [MDEV-18092](https://jira.mariadb.org/browse/MDEV-18092) Query with the table I\_S.PARAMETERS stop working after a package is created
* Merge [Revision #250799f961](https://github.com/MariaDB/server/commit/250799f961) 2019-04-17 15:26:17 +0300 - Merge 10.2 into 10.3
* [Revision #a2335b791a](https://github.com/MariaDB/server/commit/a2335b791a)\
  2019-04-14 22:24:26 +0800
  * Typo fix in sql\_sequence.cc
* [Revision #4dc10ec68d](https://github.com/MariaDB/server/commit/4dc10ec68d)\
  2019-04-11 11:49:26 +0300
  * [MDEV-19236](https://jira.mariadb.org/browse/MDEV-19236) Improve error message for ER\_ALTER\_OPERATION\_NOT\_SUPPORTED\_REASON\_COLUMN\_TYPE
* Merge [Revision #a05f423554](https://github.com/MariaDB/server/commit/a05f423554) 2019-04-12 10:56:36 +0300 - Merge remote-tracking branch 'origin/10.2' into 10.3
* [Revision #937ec3c48d](https://github.com/MariaDB/server/commit/937ec3c48d)\
  2019-04-08 21:53:30 +0300
  * [MDEV-19212](https://jira.mariadb.org/browse/MDEV-19212): After-merge fix for sizeof(ulong)!=sizeof(ulint)
* [Revision #ee7a4f4462](https://github.com/MariaDB/server/commit/ee7a4f4462)\
  2019-04-08 17:13:37 +0300
  * [MDEV-12266](https://jira.mariadb.org/browse/MDEV-12266): Pass fil\_space\_t\* to fseg\_free\_page()
* [Revision #05b84b2568](https://github.com/MariaDB/server/commit/05b84b2568)\
  2019-04-08 18:25:43 +0300
  * [MDEV-14192](https://jira.mariadb.org/browse/MDEV-14192): Add debug assertions
* Merge [Revision #9ba0865b87](https://github.com/MariaDB/server/commit/9ba0865b87) 2019-04-08 21:38:13 +0300 - Merge 10.2 into 10.3
* Merge [Revision #cc492bfd4f](https://github.com/MariaDB/server/commit/cc492bfd4f) 2019-04-07 11:49:50 +0300 - Merge 10.2 into 10.3
* Merge [Revision #d5a2bc6a0f](https://github.com/MariaDB/server/commit/d5a2bc6a0f) 2019-04-04 19:41:12 +0300 - Merge 10.2 into 10.3
* [Revision #532fffb4cc](https://github.com/MariaDB/server/commit/532fffb4cc)\
  2019-04-03 14:07:18 +0300
  * Fix the non-debug build
* Merge [Revision #c6b8b05be4](https://github.com/MariaDB/server/commit/c6b8b05be4) 2019-04-03 11:22:51 +0300 - Merge 10.2 into 10.3
* Merge [Revision #977d7a7572](https://github.com/MariaDB/server/commit/977d7a7572) 2019-04-03 08:21:43 +0300 - Merge 10.2 into 10.3
* Merge [Revision #849734376a](https://github.com/MariaDB/server/commit/849734376a) 2019-04-03 08:21:00 +0300 - Merge bb-10.3-release into 10.3
* [Revision #f5176c2dfa](https://github.com/MariaDB/server/commit/f5176c2dfa)\
  2019-04-02 11:31:53 -0400
  * bump the VERSION
* Merge [Revision #44e64fd7e0](https://github.com/MariaDB/server/commit/44e64fd7e0) 2019-04-02 13:48:42 +0300 - Merge 10.2 into 10.3
* Merge [Revision #7b42d892de](https://github.com/MariaDB/server/commit/7b42d892de) 2019-04-02 09:19:34 +0300 - Merge 10.2 into 10.3
* Merge [Revision #8f01a17292](https://github.com/MariaDB/server/commit/8f01a17292) 2019-04-01 14:25:41 +0300 - Merge 10.2 into 10.3
* Merge [Revision #0ffea01da5](https://github.com/MariaDB/server/commit/0ffea01da5) 2019-04-01 09:22:19 +0300 - Merge 10.2 into 10.3

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
