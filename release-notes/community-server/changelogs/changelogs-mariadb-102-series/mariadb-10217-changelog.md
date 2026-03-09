# MariaDB 10.2.17 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.17)[Release Notes](../../old-releases/10.2/10.2.17.md)[Changelog](mariadb-10217-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 14 Aug 2018

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.17.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #5553d3f1f6](https://github.com/MariaDB/server/commit/5553d3f1f6)\
  2018-08-12 14:25:53 +0300
  * Custom set of tests which can be run with 10.0 clients
* [Revision #4cbf77e16e](https://github.com/MariaDB/server/commit/4cbf77e16e)\
  2018-08-12 04:56:06 +0300
  * Updated list of unstable tests for 10.2.17
* [Revision #f30c5af42e](https://github.com/MariaDB/server/commit/f30c5af42e)\
  2018-08-09 17:38:40 +0300
  * InnoDB: Correct an error message
* [Revision #3f4274f8cd](https://github.com/MariaDB/server/commit/3f4274f8cd)\
  2018-08-08 17:39:45 +0200
  * SLES11 OpenSSL 0.9.8 support
* [Revision #ba1c05cc0d](https://github.com/MariaDB/server/commit/ba1c05cc0d)\
  2018-08-08 17:29:35 +0200
  * compiler warning
* [Revision #925b6ee048](https://github.com/MariaDB/server/commit/925b6ee048)\
  2018-08-08 11:19:01 +0200
  * update C/C up to v3.0.6 tag
* [Revision #eabf5230a2](https://github.com/MariaDB/server/commit/eabf5230a2)\
  2018-08-07 19:11:04 +0200
  * [MDEV-16906](https://jira.mariadb.org/browse/MDEV-16906) No groups to be reported (check your GNRs) - mysqld\_multi does not see instances
* Merge [Revision #26e2dd39c5](https://github.com/MariaDB/server/commit/26e2dd39c5) 2018-08-07 16:54:53 +0200 - Merge branch 'connect/10.2' into 10.2
* [Revision #9644415fa9](https://github.com/MariaDB/server/commit/9644415fa9)\
  2018-08-06 19:42:00 +0200
  * Fix [MDEV-16672](https://jira.mariadb.org/browse/MDEV-16672) Connect: Warnings with 10.0
* [Revision #4ddcb4eb46](https://github.com/MariaDB/server/commit/4ddcb4eb46)\
  2018-08-06 13:37:09 +0400
  * [MDEV-16750](https://jira.mariadb.org/browse/MDEV-16750) JSON\_SET mishandles unicode every second pair of arguments.
* [Revision #fc324a5f87](https://github.com/MariaDB/server/commit/fc324a5f87)\
  2018-08-05 18:33:17 +0400
  * [MDEV-16869](https://jira.mariadb.org/browse/MDEV-16869) String functions don't respect character set of JSON\_VALUE.
* Merge [Revision #affdd79c69](https://github.com/MariaDB/server/commit/affdd79c69) 2018-08-03 23:26:26 +0200 - Merge branch '10.1' into 10.2
* [Revision #e6a808bec7](https://github.com/MariaDB/server/commit/e6a808bec7)\
  2018-08-03 15:40:13 +0300
  * Fix heap-use-after-free in debug code
* [Revision #be370efac4](https://github.com/MariaDB/server/commit/be370efac4)\
  2018-08-03 14:36:38 +0300
  * Do not declare an unused variable
* [Revision #7b145fae13](https://github.com/MariaDB/server/commit/7b145fae13)\
  2018-08-03 11:24:05 +0300
  * mariadb-backup: Use snprintf() instead of sprintf()
* [Revision #391e60b2db](https://github.com/MariaDB/server/commit/391e60b2db)\
  2018-08-03 13:06:03 +0300
  * Fix -Wclass-memaccess warnings in InnoDB
* Merge [Revision #814ae57daf](https://github.com/MariaDB/server/commit/814ae57daf) 2018-08-03 13:02:56 +0300 - Merge 10.1 into 10.2
* Merge [Revision #976f920514](https://github.com/MariaDB/server/commit/976f920514) 2018-08-03 08:37:05 +0300 - [MDEV-16850](https://jira.mariadb.org/browse/MDEV-16850) Merge new release of InnoDB 5.7.23 to 10.2
* [Revision #62ee2cd461](https://github.com/MariaDB/server/commit/62ee2cd461)\
  2018-08-02 16:12:51 +0300
  * Fix a race between TRUNCATE and FOREIGN KEY check
* [Revision #de469a2f29](https://github.com/MariaDB/server/commit/de469a2f29)\
  2018-08-02 17:35:24 +0300
  * [MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637): Fix hang due to persistent statistics
* [Revision #2046089745](https://github.com/MariaDB/server/commit/2046089745)\
  2018-07-31 18:35:13 +0300
  * [MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637): Fix hang due to DDL with FOREIGN KEY
* [Revision #f70a318576](https://github.com/MariaDB/server/commit/f70a318576)\
  2018-04-08 09:16:56 +0800
  * Bug#27805553 HARD ERROR SHOULD BE REPORTED WHEN FSYNC() RETURN EIO.
* [Revision #a1b2336199](https://github.com/MariaDB/server/commit/a1b2336199)\
  2017-11-30 18:07:28 +0400
  * Optimized away excessive condition
* [Revision #f867a695f8](https://github.com/MariaDB/server/commit/f867a695f8)\
  2018-08-02 18:09:37 +0300
  * After-merge fix: Remove an unnecessary parameter
* Merge [Revision #5ce21bc67f](https://github.com/MariaDB/server/commit/5ce21bc67f) 2018-08-02 21:41:41 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #ef3070e997](https://github.com/MariaDB/server/commit/ef3070e997) 2018-08-02 08:19:57 +0300 - Merge 10.1 into 10.2
* [Revision #a90b3862d9](https://github.com/MariaDB/server/commit/a90b3862d9)\
  2018-08-01 12:41:50 +0100
  * [MDEV-16860](https://jira.mariadb.org/browse/MDEV-16860) MyRocks: support CRC32 instructions on Winx64
* [Revision #f4eac2deeb](https://github.com/MariaDB/server/commit/f4eac2deeb)\
  2018-07-31 16:33:05 +0400
  * [MDEV-16054](https://jira.mariadb.org/browse/MDEV-16054) simple json functions flatline cpu on garbage input.
* [Revision #fd378fc613](https://github.com/MariaDB/server/commit/fd378fc613)\
  2018-07-30 13:53:55 +0200
  * [MDEV-16809](https://jira.mariadb.org/browse/MDEV-16809) Allow full redo logging for ALTER TABLE Add the usual basic test for the variable innodb\_log\_optimize\_ddl.
* [Revision #5c5a116b47](https://github.com/MariaDB/server/commit/5c5a116b47)\
  2018-07-26 12:04:21 +0400
  * [MDEV-16614](https://jira.mariadb.org/browse/MDEV-16614) signal 7 after calling stored procedure, that uses regexp
* [Revision #3c141e319a](https://github.com/MariaDB/server/commit/3c141e319a)\
  2018-07-25 23:28:31 -0700
  * [MDEV-15087](https://jira.mariadb.org/browse/MDEV-15087) Item\_func::fix\_fields: Assertion \`used\_tables\_cache == 0' failed
* [Revision #0f90728bc0](https://github.com/MariaDB/server/commit/0f90728bc0)\
  2018-07-25 17:05:47 +0300
  * [MDEV-16809](https://jira.mariadb.org/browse/MDEV-16809) Allow full redo logging for ALTER TABLE
* [Revision #32eb5823e4](https://github.com/MariaDB/server/commit/32eb5823e4)\
  2018-07-24 10:54:15 +0300
  * Remove pointer indirection for BtrBulk::m\_page\_bulks
* [Revision #4a456eac2a](https://github.com/MariaDB/server/commit/4a456eac2a)\
  2018-07-24 10:48:31 +0300
  * Remove unused BtrBulk::m\_heap
* [Revision #a3b22147ca](https://github.com/MariaDB/server/commit/a3b22147ca)\
  2018-07-24 10:46:30 +0300
  * Remove pointer indirection for PageBulk::m\_mtr
* [Revision #172199b88c](https://github.com/MariaDB/server/commit/172199b88c)\
  2018-07-24 10:23:17 +0300
  * PageBulk: Remove dead code
* [Revision #7f54894329](https://github.com/MariaDB/server/commit/7f54894329)\
  2018-07-24 09:35:47 +0300
  * Remove mtr\_set\_flush\_observer()
* [Revision #aad70e9b4c](https://github.com/MariaDB/server/commit/aad70e9b4c)\
  2018-07-25 11:57:57 -0700
  * [MDEV-16820](https://jira.mariadb.org/browse/MDEV-16820) Lost 'Impossible where' from query with inexpensive subquery
* [Revision #de85355436](https://github.com/MariaDB/server/commit/de85355436)\
  2018-07-25 13:56:39 +0530
  * [MDEV-16713](https://jira.mariadb.org/browse/MDEV-16713) Hangs server with repeating log entry
* [Revision #969939e89c](https://github.com/MariaDB/server/commit/969939e89c)\
  2018-07-25 12:54:37 +0530
  * [MDEV-16821](https://jira.mariadb.org/browse/MDEV-16821) Set password for user makes rpl test to fail
* [Revision #a8227a1543](https://github.com/MariaDB/server/commit/a8227a1543)\
  2018-07-24 18:15:15 +0400
  * [MDEV-16814](https://jira.mariadb.org/browse/MDEV-16814) CREATE TABLE SELECT JSON\_QUOTE(multibyte\_charset\_expr) makes a field of a wrong length
* [Revision #45ab00f097](https://github.com/MariaDB/server/commit/45ab00f097)\
  2018-07-23 14:14:23 -0700
  * [MDEV-15786](https://jira.mariadb.org/browse/MDEV-15786): ERROR 1062 (23000) at line 365: Duplicate entry 'spider' for key 'PRIMARY'
* [Revision #9d1f3bf2e9](https://github.com/MariaDB/server/commit/9d1f3bf2e9)\
  2018-07-23 18:23:54 +0300
  * row\_purge\_poss\_sec(): Add debug instrumentation
* [Revision #c5ba13dda0](https://github.com/MariaDB/server/commit/c5ba13dda0)\
  2018-07-23 18:23:54 +0300
  * [MDEV-15855](https://jira.mariadb.org/browse/MDEV-15855) cleanup: Privatize purge\_vcol\_info\_t
* [Revision #a7a0c533c2](https://github.com/MariaDB/server/commit/a7a0c533c2)\
  2018-07-23 17:50:56 +0300
  * Follow-up to [MDEV-15855](https://jira.mariadb.org/browse/MDEV-15855): Remove bogus debug assertions
* [Revision #730f6c912c](https://github.com/MariaDB/server/commit/730f6c912c)\
  2018-07-23 13:42:19 +0300
  * [MDEV-16779](https://jira.mariadb.org/browse/MDEV-16779) Assertion !rw\_lock\_own failed upon purge
* [Revision #b660261be1](https://github.com/MariaDB/server/commit/b660261be1)\
  2018-07-23 15:58:31 +0300
  * ut\_print\_buf\_hex(): Correctly dump the hex
* [Revision #73af075366](https://github.com/MariaDB/server/commit/73af075366)\
  2018-07-23 13:31:10 +0300
  * Reduce the number of rw\_lock\_own() calls
* [Revision #d0d073b1aa](https://github.com/MariaDB/server/commit/d0d073b1aa)\
  2018-07-20 19:32:28 -0700
  * Corrected and added back the test case for [MDEV-15151](https://jira.mariadb.org/browse/MDEV-15151).
* [Revision #9827c5e103](https://github.com/MariaDB/server/commit/9827c5e103)\
  2018-06-26 11:33:58 +0530
  * [MDEV-16192](https://jira.mariadb.org/browse/MDEV-16192) Table 't' is specified twice, both as a target for 'CREATE' and... as a separate source for data
* [Revision #1cc1d0429d](https://github.com/MariaDB/server/commit/1cc1d0429d)\
  2018-07-07 11:34:26 +0300
  * [MDEV-16664](https://jira.mariadb.org/browse/MDEV-16664): Change the default to innodb\_lock\_schedule\_algorithm=fcfs
* [Revision #8b0d4cff07](https://github.com/MariaDB/server/commit/8b0d4cff07)\
  2018-07-06 17:13:53 +0300
  * [MDEV-15855](https://jira.mariadb.org/browse/MDEV-15855) Deadlock between purge thread and DDL statement
* [Revision #e3207b6c13](https://github.com/MariaDB/server/commit/e3207b6c13)\
  2018-07-06 09:01:24 +0300
  * [MDEV-14188](https://jira.mariadb.org/browse/MDEV-14188) mariadb-backup.incremental\_encrypted wrong result
* [Revision #e9b78a1055](https://github.com/MariaDB/server/commit/e9b78a1055)\
  2018-07-05 15:10:47 -0700
  * Removed the test case for [MDEV-15151](https://jira.mariadb.org/browse/MDEV-15151) for the following reasons:
* [Revision #1b335a74b4](https://github.com/MariaDB/server/commit/1b335a74b4)\
  2018-07-05 16:44:12 +0300
  * Clean up a test
* [Revision #d897b4dc25](https://github.com/MariaDB/server/commit/d897b4dc25)\
  2018-07-05 00:07:55 +0530
  * [MDEV-15855](https://jira.mariadb.org/browse/MDEV-15855): Use atomics for dict\_table\_t::n\_ref\_count
* [Revision #fdb9e66fee](https://github.com/MariaDB/server/commit/fdb9e66fee)\
  2018-07-05 13:15:35 +0300
  * Implement a parameter for wait\_all\_purged.inc
* [Revision #e9f1d8da57](https://github.com/MariaDB/server/commit/e9f1d8da57)\
  2018-07-05 11:41:55 +0300
  * Fix warnings about possibly uninitialized variables
* [Revision #058554027f](https://github.com/MariaDB/server/commit/058554027f)\
  2018-07-05 00:06:39 -0700
  * [MDEV-16629](https://jira.mariadb.org/browse/MDEV-16629) "Table Does Not Exist" Error from Recursive CTE Query Inside Function
* [Revision #400cf01715](https://github.com/MariaDB/server/commit/400cf01715)\
  2018-07-02 17:19:42 +0100
  * [MDEV-16571](https://jira.mariadb.org/browse/MDEV-16571) - some backup tests sometimes with missing data after restore.
* [Revision #8639e28808](https://github.com/MariaDB/server/commit/8639e28808)\
  2018-04-20 07:06:25 +0000
  * [MDEV-16630](https://jira.mariadb.org/browse/MDEV-16630): Ambiguous error message when check constraint matches table name
* [Revision #b71c9ae030](https://github.com/MariaDB/server/commit/b71c9ae030)\
  2018-07-01 13:55:38 +0100
  * amend fix for [MDEV-16596](https://jira.mariadb.org/browse/MDEV-16596) - do not use CREATE\_NEW flag when reopening redo log file.
* [Revision #c612a1e77c](https://github.com/MariaDB/server/commit/c612a1e77c)\
  2018-06-30 11:02:49 +0100
  * [MDEV-16596](https://jira.mariadb.org/browse/MDEV-16596) : Windows - redo log does not work on native 4K sector disks.
* Merge [Revision #1dd3c8f8ba](https://github.com/MariaDB/server/commit/1dd3c8f8ba) 2018-06-28 22:21:50 +0200 - Merge branch '10.1' into 10.2
* [Revision #04677f44c7](https://github.com/MariaDB/server/commit/04677f44c7)\
  2018-06-28 17:23:05 +0100
  * Innodb : do not use errno on Windows to print os\_file\_pwrite() error.
* [Revision #78a0646fe4](https://github.com/MariaDB/server/commit/78a0646fe4)\
  2018-06-28 09:05:01 +0200
  * make plugins.processlist more robust
* [Revision #00ccff48af](https://github.com/MariaDB/server/commit/00ccff48af)\
  2018-03-18 21:01:41 +0200
  * [MDEV-14014](https://jira.mariadb.org/browse/MDEV-14014) Multi-Slave Replication Fail: bogus data in log event
* [Revision #52a25d7b67](https://github.com/MariaDB/server/commit/52a25d7b67)\
  2018-06-28 12:36:32 +0200
  * [MDEV-16473](https://jira.mariadb.org/browse/MDEV-16473) WITH statement throws 'no database selected' error
* [Revision #090febbb2d](https://github.com/MariaDB/server/commit/090febbb2d)\
  2018-06-28 00:33:44 -0700
  * This is another attempt to fix [MDEV-16473](https://jira.mariadb.org/browse/MDEV-16473).
* [Revision #377cd52064](https://github.com/MariaDB/server/commit/377cd52064)\
  2018-06-27 11:38:09 +0300
  * Pretty-print table names in some error messages
* [Revision #6d377a523c](https://github.com/MariaDB/server/commit/6d377a523c)\
  2018-06-26 10:49:23 -0700
  * Correction for the patch to fix [MDEV-16473](https://jira.mariadb.org/browse/MDEV-16473).
* Merge [Revision #31c950cca8](https://github.com/MariaDB/server/commit/31c950cca8) 2018-06-26 18:16:49 +0300 - Merge 10.1 into 10.2
* [Revision #0e937f30f6](https://github.com/MariaDB/server/commit/0e937f30f6)\
  2018-06-26 11:04:57 -0400
  * bump the VERSION
* Merge [Revision #1b4ac075bf](https://github.com/MariaDB/server/commit/1b4ac075bf) 2018-06-26 15:12:58 +0300 - Merge 10.1 into 10.2
* [Revision #7d0d934ca6](https://github.com/MariaDB/server/commit/7d0d934ca6)\
  2018-06-25 19:19:10 -0700
  * [MDEV-16473](https://jira.mariadb.org/browse/MDEV-16473) WITH statement throws 'no database selected' error
* [Revision #31e52b1632](https://github.com/MariaDB/server/commit/31e52b1632)\
  2018-03-12 14:46:00 +0100
  * Optimize charset tracking a bit.
* [Revision #517d718201](https://github.com/MariaDB/server/commit/517d718201)\
  2018-03-09 14:39:40 +0100
  * [MDEV-15477](https://jira.mariadb.org/browse/MDEV-15477): SESSION\_SYSVARS\_TRACKER does not track last\_gtid
* [Revision #73de63e898](https://github.com/MariaDB/server/commit/73de63e898)\
  2018-03-09 14:27:13 +0100
  * Session tracking info support in mysqltest (port from mysql)
* [Revision #a8e1eef899](https://github.com/MariaDB/server/commit/a8e1eef899)\
  2018-03-09 14:26:10 +0100
  * Reset connection support in mysqltest (port from mysql)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
