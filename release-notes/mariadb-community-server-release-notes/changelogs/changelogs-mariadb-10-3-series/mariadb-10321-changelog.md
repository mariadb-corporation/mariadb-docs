# MariaDB 10.3.21 Changelog

The most recent release of [MariaDB 10.3](../../old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](../../old-releases/release-notes-mariadb-10-3-series/mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download](https://downloads.mariadb.org/mariadb/10.3.21/)[Release Notes](../../old-releases/release-notes-mariadb-10-3-series/mariadb-10321-release-notes.md)[Changelog](mariadb-10321-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

**Release date:** 11 Dec 2019

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-3-series/mariadb-10321-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.30](../changelogs-mariadb-102-series/mariadb-10230-changelog.md)
* [Revision #e5e5877740](https://github.com/MariaDB/server/commit/e5e5877740)\
  2019-12-06 00:18:10 +0200
  * List of unstable tests for 10.3.21 release
* [Revision #be92dce613](https://github.com/MariaDB/server/commit/be92dce613)\
  2019-12-05 23:45:57 +0300
  * [MDEV-21234](https://jira.mariadb.org/browse/MDEV-21234) Server crashes in setup\_on\_expr upon 3rd execution of SP
* [Revision #1fbd9bb2c5](https://github.com/MariaDB/server/commit/1fbd9bb2c5)\
  2019-12-05 18:26:52 +0200
  * Merge pull request #1261 from robertbindar/[MDEV-17978](https://jira.mariadb.org/browse/MDEV-17978)
* [Revision #d759f764f6](https://github.com/MariaDB/server/commit/d759f764f6)\
  2019-12-05 15:11:18 +0300
  * [MDEV-21233](https://jira.mariadb.org/browse/MDEV-21233) Assertion \`m\_extra\_cache' failed in ha\_partition::late\_extra\_cache
* [Revision #c4ed1bee5b](https://github.com/MariaDB/server/commit/c4ed1bee5b)\
  2019-12-04 18:10:31 +0200
  * [MDEV-21172](https://jira.mariadb.org/browse/MDEV-21172) Memory leak after failed ADD PRIMARY KEY
* Merge [Revision #008ee867a4](https://github.com/MariaDB/server/commit/008ee867a4) 2019-12-04 17:46:28 +0100 - Merge branch '10.2' into 10.3
* Merge [Revision #670c9a3a18](https://github.com/MariaDB/server/commit/670c9a3a18) 2019-12-04 15:57:09 +0100 - Merge remote-tracking branch 'origin/bb-10.3-release' into 10.3
* [Revision #f6d8640d67](https://github.com/MariaDB/server/commit/f6d8640d67)\
  2019-12-03 21:26:44 +0300
  * [MDEV-18929](https://jira.mariadb.org/browse/MDEV-18929) 2nd execution of SP does not detect ER\_VERS\_NOT\_VERSIONED
* [Revision #477629d2cd](https://github.com/MariaDB/server/commit/477629d2cd)\
  2019-12-03 15:46:49 +0300
  * [MDEV-21147](https://jira.mariadb.org/browse/MDEV-21147) Assertion \`marked\_for\_read()' upon UPDATE on versioned table via view
* Merge [Revision #81bf7d3317](https://github.com/MariaDB/server/commit/81bf7d3317) 2019-12-04 15:01:54 +0100 - Merge branch 'bb-10.3-release' into 10.3
* [Revision #bf2f391664](https://github.com/MariaDB/server/commit/bf2f391664)\
  2019-12-03 15:46:49 +0300
  * [MDEV-21147](https://jira.mariadb.org/browse/MDEV-21147) Assertion \`marked\_for\_read()' upon UPDATE on versioned table via view
* [Revision #cef2b34f25](https://github.com/MariaDB/server/commit/cef2b34f25)\
  2019-12-03 15:28:41 +0300
  * [MDEV-18929](https://jira.mariadb.org/browse/MDEV-18929) 2nd execution of SP does not detect ER\_VERS\_NOT\_VERSIONED
* [Revision #8a46b706aa](https://github.com/MariaDB/server/commit/8a46b706aa)\
  2019-12-03 14:47:55 +0200
  * Update innodb\_i\_s\_tables\_disabled.result post typo fix
* [Revision #4670a23957](https://github.com/MariaDB/server/commit/4670a23957)\
  2019-12-03 14:37:45 +0200
  * Re-record sql\_sequence.rebuild with sorted\_result
* [Revision #2daacddf6b](https://github.com/MariaDB/server/commit/2daacddf6b)\
  2019-12-03 14:34:12 +0200
  * Update versioning.alter after typo fix
* [Revision #abbff37eb4](https://github.com/MariaDB/server/commit/abbff37eb4)\
  2019-12-03 11:58:24 +0200
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) follow-up: Harden an assertion
* Merge [Revision #9d9a2253c6](https://github.com/MariaDB/server/commit/9d9a2253c6) 2019-12-02 14:35:10 +0200 - Merge remote-tracking branch 10.2 into 10.3
* [Revision #8d2a57b4b7](https://github.com/MariaDB/server/commit/8d2a57b4b7)\
  2019-04-16 17:52:31 +0300
  * [MDEV-15977](https://jira.mariadb.org/browse/MDEV-15977) Assertion !thd->in\_sub\_stmt failed in trans\_commit\_stmt
* [Revision #7e917bba5d](https://github.com/MariaDB/server/commit/7e917bba5d)\
  2019-11-29 15:51:20 +0100
  * Sourced script should be 644 not 755
* [Revision #2df2238cb8](https://github.com/MariaDB/server/commit/2df2238cb8)\
  2018-12-21 17:06:08 -0300
  * Lintian complains on spelling error
* [Revision #db32d9457e](https://github.com/MariaDB/server/commit/db32d9457e)\
  2019-12-02 11:48:37 +0300
  * [MDEV-18929](https://jira.mariadb.org/browse/MDEV-18929) 2nd execution of SP does not detect ER\_VERS\_NOT\_VERSIONED
* [Revision #a7cf0db3d8](https://github.com/MariaDB/server/commit/a7cf0db3d8)\
  2019-12-02 11:48:37 +0300
  * [MDEV-21011](https://jira.mariadb.org/browse/MDEV-21011) Table corruption reported for versioned partitioned table after DELETE: "Found a misplaced row"
* [Revision #6dd41e008e](https://github.com/MariaDB/server/commit/6dd41e008e)\
  2019-12-02 11:48:37 +0300
  * [MDEV-21155](https://jira.mariadb.org/browse/MDEV-21155) Assertion with versioned table upon DELETE from view of view after replacing first view
* [Revision #97aa07abf5](https://github.com/MariaDB/server/commit/97aa07abf5)\
  2019-12-02 11:48:37 +0300
  * [MDEV-21147](https://jira.mariadb.org/browse/MDEV-21147) Assertion \`marked\_for\_read()' upon UPDATE on versioned table via view
* [Revision #498a96a478](https://github.com/MariaDB/server/commit/498a96a478)\
  2019-12-02 11:48:37 +0300
  * [MDEV-20441](https://jira.mariadb.org/browse/MDEV-20441) ER\_CRASHED\_ON\_USAGE upon update on versioned Aria table
* [Revision #57cab7cd51](https://github.com/MariaDB/server/commit/57cab7cd51)\
  2019-11-27 14:36:21 +0100
  * fix ssl\_crl test failures on newer OpenSSL
* [Revision #95898ac9bd](https://github.com/MariaDB/server/commit/95898ac9bd)\
  2019-11-29 09:07:24 +0100
  * Revert "Fix upgrade errors on eoan"
* [Revision #0d345ec2e3](https://github.com/MariaDB/server/commit/0d345ec2e3)\
  2019-11-28 14:01:46 +0100
  * Fix upgrade errors on eoan
* [Revision #dc7d0b5030](https://github.com/MariaDB/server/commit/dc7d0b5030)\
  2019-11-27 18:55:14 +0100
  * RPM packaging fixes for FC31
* [Revision #ba95c303e3](https://github.com/MariaDB/server/commit/ba95c303e3)\
  2019-11-25 22:48:50 +0100
  * [MDEV-21167](https://jira.mariadb.org/browse/MDEV-21167) LF\_PINS::stack\_ends\_here inaccurate, leading to alloca() larger than stack
* [Revision #584ffa02f1](https://github.com/MariaDB/server/commit/584ffa02f1)\
  2019-11-27 20:44:14 +0100
  * [MDEV-19669](https://jira.mariadb.org/browse/MDEV-19669) - fix matching CIDR address for proxy protocol.
* [Revision #3fc1f6260f](https://github.com/MariaDB/server/commit/3fc1f6260f)\
  2019-11-27 14:00:01 +0200
  * [MDEV-21158](https://jira.mariadb.org/browse/MDEV-21158) trx\_undo\_seg\_free() is never redo-logged
* [Revision #bf58ec77a1](https://github.com/MariaDB/server/commit/bf58ec77a1)\
  2019-11-25 15:44:46 +0300
  * [MDEV-18727](https://jira.mariadb.org/browse/MDEV-18727) cleanup
* [Revision #1d5f6a0073](https://github.com/MariaDB/server/commit/1d5f6a0073)\
  2019-11-22 14:30:13 +0300
  * [MDEV-21049](https://jira.mariadb.org/browse/MDEV-21049) Segfault in create federatedx table with empty hostname
* [Revision #0076dce2c8](https://github.com/MariaDB/server/commit/0076dce2c8)\
  2019-11-22 14:29:03 +0300
  * [MDEV-18727](https://jira.mariadb.org/browse/MDEV-18727) improve DML operation of System Versioning [MDEV-18957](https://jira.mariadb.org/browse/MDEV-18957) UPDATE with LIMIT clause is wrong for versioned partitioned tables
* [Revision #a14544260c](https://github.com/MariaDB/server/commit/a14544260c)\
  2019-11-15 21:49:04 +0700
  * [MDEV-21045](https://jira.mariadb.org/browse/MDEV-21045) AddressSanitizer: use-after-poison in mem\_heap\_dup / row\_log\_table\_get\_pk\_col
* Merge [Revision #24a279bb27](https://github.com/MariaDB/server/commit/24a279bb27) 2019-11-20 09:53:05 +0300 - Merge branch '10.2' into 10.3
* [Revision #aa3d28ac34](https://github.com/MariaDB/server/commit/aa3d28ac34)\
  2019-11-20 14:02:30 +0800
  * [MDEV-21088](https://jira.mariadb.org/browse/MDEV-21088): Follow-up fix for ROW\_FORMAT=REDUNDANT
* [Revision #89f487f2e2](https://github.com/MariaDB/server/commit/89f487f2e2)\
  2019-11-20 13:03:34 +0800
  * [MDEV-21088](https://jira.mariadb.org/browse/MDEV-21088) Table cannot be loaded after instant ADD/DROP COLUMN
* [Revision #7b5654f3e9](https://github.com/MariaDB/server/commit/7b5654f3e9)\
  2019-11-20 00:33:32 +0400
  * [MDEV-14667](https://jira.mariadb.org/browse/MDEV-14667) Assertion \`used\_parts > 0' failed in ha\_partition::init\_record\_priority\_queue.
* [Revision #39d8652ca5](https://github.com/MariaDB/server/commit/39d8652ca5)\
  2019-11-19 00:42:10 +0200
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) follow-up: Remove unused code
* Merge [Revision #613e13072c](https://github.com/MariaDB/server/commit/613e13072c) 2019-11-19 00:37:01 +0200 - Merge 10.2 into 10.3
* [Revision #409ed60bb8](https://github.com/MariaDB/server/commit/409ed60bb8)\
  2019-11-16 13:18:24 +0300
  * Fix compile failure on Windows: use explicit type casts
* [Revision #86167e908f](https://github.com/MariaDB/server/commit/86167e908f)\
  2019-11-15 23:37:28 +0300
  * [MDEV-20611](https://jira.mariadb.org/browse/MDEV-20611): MRR scan over partitioned InnoDB table produces "Out of memory" error
* [Revision #3d4a801533](https://github.com/MariaDB/server/commit/3d4a801533)\
  2019-11-14 11:40:33 +0200
  * [MDEV-12353](https://jira.mariadb.org/browse/MDEV-12353) preparation: Replace mtr\_x\_lock() and friends
* Merge [Revision #4ded5fb9ac](https://github.com/MariaDB/server/commit/4ded5fb9ac) 2019-11-14 11:26:49 +0200 - [MDEV-20949](https://jira.mariadb.org/browse/MDEV-20949): Merge 10.2 into 10.3
* Merge [Revision #bc5cfe7769](https://github.com/MariaDB/server/commit/bc5cfe7769) 2019-11-14 10:51:06 +0200 - Merge 10.2 into 10.3
* [Revision #d4edb0510e](https://github.com/MariaDB/server/commit/d4edb0510e)\
  2019-11-13 18:53:59 +0300
  * [MDEV-20646](https://jira.mariadb.org/browse/MDEV-20646): 10.3.18 is slower than 10.3.17
* Merge [Revision #5098d708a0](https://github.com/MariaDB/server/commit/5098d708a0) 2019-11-12 16:30:57 +0200 - Merge 10.2 into 10.3
* Merge [Revision #d103c5a489](https://github.com/MariaDB/server/commit/d103c5a489) 2019-11-11 16:28:21 +0200 - merge 10.2->10.3 with conflict resolutions
* Merge [Revision #4fcfdb60e7](https://github.com/MariaDB/server/commit/4fcfdb60e7) 2019-11-11 14:56:51 +0200 - Merge 10.2 into 10.3
* [Revision #c4ee8a306b](https://github.com/MariaDB/server/commit/c4ee8a306b)\
  2019-11-08 09:52:10 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
