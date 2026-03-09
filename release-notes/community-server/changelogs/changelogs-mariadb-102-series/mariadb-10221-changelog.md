# MariaDB 10.2.21 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.21/)[Release Notes](../../old-releases/10.2/10.2.21.md)[Changelog](mariadb-10221-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 2 Jan 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.21.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* Merge [Revision #67240858b2](https://github.com/MariaDB/server/commit/67240858b2) 2018-12-30 15:50:20 +0100 - Merge branch '10.1' into 10.2
* Merge [Revision #aeefd26ecb](https://github.com/MariaDB/server/commit/aeefd26ecb) 2018-12-29 23:44:45 +0100 - Merge branch '10.0' into 10.1
* [Revision #802ce9672f](https://github.com/MariaDB/server/commit/802ce9672f)\
  2018-12-29 20:44:40 +0300
  * [MDEV-18041](https://jira.mariadb.org/browse/MDEV-18041) Database corruption after renaming a prefix-indexed column
* [Revision #b74eb5a5fe](https://github.com/MariaDB/server/commit/b74eb5a5fe)\
  2018-12-28 12:28:16 +0200
  * row\_drop\_table\_for\_mysql(): Correct a parameter to innobase\_format\_name()
* Merge [Revision #8634f7e528](https://github.com/MariaDB/server/commit/8634f7e528) 2018-12-20 09:15:01 +0100 - Merge branch '5.5' into 10.0
* [Revision #b0fd06a6f2](https://github.com/MariaDB/server/commit/b0fd06a6f2)\
  2018-12-18 17:07:29 +0400
  * [MDEV-15670](https://jira.mariadb.org/browse/MDEV-15670) - unit.my\_atomic failed in buildbot with Signal 11 thrown
* [Revision #65525550ab](https://github.com/MariaDB/server/commit/65525550ab)\
  2018-12-17 16:09:28 +0100
  * Don't default to bundled zlib
* [Revision #15eaeace39](https://github.com/MariaDB/server/commit/15eaeace39)\
  2018-12-12 19:58:20 +0400
  * [MDEV-16987](https://jira.mariadb.org/browse/MDEV-16987) - ALTER DATABASE possible in read-only mode
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
* Merge [Revision #cf9070a8f7](https://github.com/MariaDB/server/commit/cf9070a8f7) 2018-12-29 23:12:25 +0200 - Merge 10.1 into 10.2
* [Revision #50c9469be8](https://github.com/MariaDB/server/commit/50c9469be8)\
  2018-12-29 22:59:20 +0200
  * [MDEV-18105](https://jira.mariadb.org/browse/MDEV-18105) mariadb-backup fails to copy encrypted InnoDB system tablespace if LSN>4G
* Merge [Revision #0b73b96f9d](https://github.com/MariaDB/server/commit/0b73b96f9d) 2018-12-29 11:05:26 +0200 - Merge 10.1 into 10.2
* [Revision #68143c8905](https://github.com/MariaDB/server/commit/68143c8905)\
  2018-12-29 10:57:26 +0200
  * [MDEV-17470](https://jira.mariadb.org/browse/MDEV-17470): Fix the test for --embedded
* [Revision #ed66acb291](https://github.com/MariaDB/server/commit/ed66acb291)\
  2018-12-29 02:06:19 +0100
  * Silence LeakSanitizer by default in mariadb-backup, so that phanthom "leaks" would not hide more interesting information, like invalid memory accesses.
* Merge [Revision #33caaba5c8](https://github.com/MariaDB/server/commit/33caaba5c8) 2018-12-28 17:40:38 +0200 - Merge 10.1 into 10.2
* [Revision #c5a5eaa9a9](https://github.com/MariaDB/server/commit/c5a5eaa9a9)\
  2018-12-14 01:28:55 +0300
  * [MDEV-17470](https://jira.mariadb.org/browse/MDEV-17470) Orphan temporary files after interrupted ALTER cause InnoDB: Operating system error number 17 and eventual fatal error 71
* [Revision #9ad1663f78](https://github.com/MariaDB/server/commit/9ad1663f78)\
  2018-12-22 15:04:50 +0530
  * Grammatical errors of README-wsrep fixed. (#915)
* [Revision #734029fa79](https://github.com/MariaDB/server/commit/734029fa79)\
  2018-12-26 00:00:49 +0300
  * Fix a trivial (and harmless) merge error
* [Revision #835f49d9ce](https://github.com/MariaDB/server/commit/835f49d9ce)\
  2018-12-24 09:22:55 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
