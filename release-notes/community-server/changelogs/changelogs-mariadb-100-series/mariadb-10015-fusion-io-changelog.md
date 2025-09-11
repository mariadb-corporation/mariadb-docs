# MariaDB 10.0.15 Fusion-io Changelog

[Download](https://archive.mariadb.org/mariadb-10.0.15-FusionIO/) | [Release Notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10015-fusion-io-release-notes.md) | [Changelog](mariadb-10015-fusion-io-changelog.md) | [Fusion-io Introduction](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/fusion-io/fusion-io-introduction)

**Release date:** 12 Dec 2014

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10015-fusion-io-release-notes.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4009](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4009)\
  Thu 2014-12-04 13:19:51 +0200
  * [MDEV-7262](https://jira.mariadb.org/browse/MDEV-7262): innodb.innodb-mdev7046 and innodb-page\_compression\* fail on BuildBot
* [Revision #4008](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4008)\
  Wed 2014-12-03 13:23:42 +0200
  * Fix problem with trims.
* [Revision #4007](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4007)\
  Wed 2014-12-03 12:05:00 +0200
  * Fix compiler error on fallocate and flags used.
* [Revision #4006](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4006)\
  Tue 2014-12-02 20:26:21 +0200
  * Fix buildbot valgrind errors on test innodb.innodb-page\_compression\_tables
* [Revision #4005](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4005) \[merge]\
  Mon 2014-12-01 11:52:51 +0200
  * Merge [MariaDB 10.0.15](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10015-release-notes.md) from lp:maria/10.0 up to revision 4521
* [Revision #4004](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4004)\
  Mon 2014-11-24 12:08:45 +0200
  * [MDEV-7166](https://jira.mariadb.org/browse/MDEV-7166): innodb.innodb-page\_compression\_zip fails in buildbot
* [Revision #4003](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4003)\
  Wed 2014-11-19 20:20:31 +0200
  * [MDEV-7133](https://jira.mariadb.org/browse/MDEV-7133): InnoDB: Assertion failure in dict\_tf\_is\_valid
* [Revision #4002](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4002)\
  Wed 2014-11-12 10:06:39 +0200
  * [MDEV-7088](https://jira.mariadb.org/browse/MDEV-7088): Query stats for compression based on TRIM size
* [Revision #4001](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4001)\
  Fri 2014-11-07 12:06:53 +0200
  * Move debug output inside a UNIV\_DEBUG.
* [Revision #4000](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/4000)\
  Tue 2014-11-04 17:20:27 +0200
  * Fix posix\_fallocate error message and add temporal debug output to resolve the problems on trim.
* [Revision #3999](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3999)\
  Tue 2014-11-04 11:37:55 +0200
  * Fixed trim operation alligment problem.
* [Revision #3998](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3998)\
  Wed 2014-10-29 08:51:17 +0200
  * [MDEV-6648](https://jira.mariadb.org/browse/MDEV-6648): InnoDB: Add support for 4K sector size if supported
* [Revision #3997](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3997) \[merge]\
  Mon 2014-10-20 11:34:21 +0300
  * Merge [MariaDB 10.0.14](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10014-release-notes.md) from lp:maria/10.0 up to revision 4116.
* [Revision #3996](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3996) \[merge]\
  Tue 2014-09-23 12:46:21 +0300
  * Merge [MariaDB 10.0.13](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10013-release-notes.md) i.e. lp:maria/10.0 up to revision 4346.
* [Revision #3995](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3995)\
  Wed 2014-08-27 15:39:05 +0300
  * Fix small error on LZMA compression failure error message.
* [Revision #3994](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3994)\
  Thu 2014-08-07 13:40:00 +0300
  * [MDEV-6548](https://jira.mariadb.org/browse/MDEV-6548): Incorrect compression on LZMA.
* [Revision #3993](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3993)\
  Thu 2014-07-31 11:47:21 +0300
  * Merge [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) -> 10.0-FusionIO
* [Revision #3992](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3992)\
  Wed 2014-07-23 12:03:48 +0300
  * Fix default value for innodb-compression-algorithm to be 0 (uncompressed) to avoid test failures.
* [Revision #3991](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3991)\
  Mon 2014-07-21 21:17:58 +0300
  * [MDEV-6354](https://jira.mariadb.org/browse/MDEV-6354): mplement a way to read MySQL 5.7.4-labs-tplc page compression format (Fusion-IO).
* [Revision #3990](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3990) \[merge]\
  Sat 2014-06-28 13:10:57 +0300
  * Merge lp:maria/10.0 up to [MariaDB 10.0.12](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10012-release-notes.md) i.e. revision 4252.
* [Revision #3989](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3989)\
  Fri 2014-06-27 17:32:03 +0300
  * [MDEV-6392](https://jira.mariadb.org/browse/MDEV-6392): Change innodb\_have\_lzo and innodb\_have\_lz4 as a static variables and reduce the number of ifdef's
* [Revision #3988](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3988)\
  Thu 2014-06-26 07:50:48 +0300
  * [MDEV-6361](https://jira.mariadb.org/browse/MDEV-6361): innodb\_compression\_algorithm configuration variable can be set to unsupported value.
* [Revision #3987](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3987)\
  Mon 2014-05-26 20:42:06 +0200
  * compilation failure on Win64
* [Revision #3986](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3986)\
  Mon 2014-05-26 20:41:10 +0200
  * use ENUM not ULONG for innodb-compression-algorithm command-line option
* [Revision #3985](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3985)\
  Mon 2014-05-26 20:31:03 +0200
  * compilation failure on Windows
* [Revision #3984](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3984)\
  Mon 2014-05-26 20:27:14 +0200
  * don't include the file that 1) not present everywhere 2) not used anyway
* [Revision #3983](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3983)\
  Mon 2014-05-26 20:26:51 +0200
  * temporarily disable lzo compression
* [Revision #3982](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3982)\
  Mon 2014-05-26 20:26:04 +0200
  * lzo.cmake: don't use the same symbol for two different tests
* [Revision #3981](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3981)\
  Fri 2014-05-23 08:20:43 +0300
  * Fix compiler warnings.
* [Revision #3980](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3980)\
  Thu 2014-05-22 21:03:26 +0300
  * Fix compiler error if LZO is not installed.
* [Revision #3979](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3979)\
  Thu 2014-05-22 19:48:34 +0300
  * Fixed compiler errors caused by merge error.
* [Revision #3978](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3978)\
  Thu 2014-05-22 16:31:31 +0300
  * Fix some compiler warnings and small errors on code.
* [Revision #3977](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3977)\
  Fri 2014-05-16 15:30:13 +0300
  * Code cleanup after review.
* [Revision #3976](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3976)\
  Mon 2014-04-28 07:52:41 +0300
  * Fixed small error on compression failure error text.
* [Revision #3975](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3975)\
  Wed 2014-04-23 19:23:11 +0300
  * Fixed bug on free buffer space calculation when LZO is used. Fixed bug on function call when InnoDB plugin is used.
* [Revision #3974](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3974) \[merge]\
  Thu 2014-04-17 08:22:54 +0300
  * Merge lp:maria/10.0 up to [MariaDB 10.0.10](../../old-releases/release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md) revision 4140.
* [Revision #3973](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3973)\
  Wed 2014-04-16 16:55:36 +0300
  * [MDEV-6070](https://jira.mariadb.org/browse/MDEV-6070): FusionIO: Failure to create a table with ATOMIC\_WRITES option leaves the database in inconsistent state,
* [Revision #3972](https://bazaar.launchpad.net/~maria-captains/maria/10.0-FusionIO/revision/3972)\
  Tue 2014-04-15 14:28:25 +0300
  * Added support for LZO compression method.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formId="4316" %}
