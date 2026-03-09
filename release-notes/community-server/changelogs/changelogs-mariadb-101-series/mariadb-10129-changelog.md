# MariaDB 10.1.29 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.29)[Release Notes](../../old-releases/10.1/10.1.29.md)[Changelog](mariadb-10129-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 14 Nov 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.29.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #05103c84ec](https://github.com/MariaDB/server/commit/05103c84ec)\
  2017-11-09 13:43:22 +0000
  * [MDEV-14205](https://jira.mariadb.org/browse/MDEV-14205) Windows : fix race condition writing into error log and setvbuf
* [Revision #8b18a44fa7](https://github.com/MariaDB/server/commit/8b18a44fa7)\
  2017-11-13 13:11:53 +0800
  * mroonga after-merge CMakeLists.txt fixes
* [Revision #1fdf11669c](https://github.com/MariaDB/server/commit/1fdf11669c)\
  2017-11-10 21:06:58 +0200
  * Updated list of unstable tests for 10.1.29 release
* Merge [Revision #2a4e4335c4](https://github.com/MariaDB/server/commit/2a4e4335c4) 2017-11-10 01:38:03 +0100 - Merge branch 'github/10.0-galera' into 10.1
* [Revision #9572bbdc37](https://github.com/MariaDB/server/commit/9572bbdc37)\
  2017-11-08 17:22:11 +0200
  * MW-388
* [Revision #ca42ee0ff3](https://github.com/MariaDB/server/commit/ca42ee0ff3)\
  2017-09-19 16:23:29 +0300
  * Fix galera.galera\_suspend\_slave on FreeBSD
* [Revision #0eaf24e842](https://github.com/MariaDB/server/commit/0eaf24e842)\
  2017-09-22 10:06:59 +0200
  * MW-410 Stability fix for test galera.galera\_ftwrl
* [Revision #736d75d455](https://github.com/MariaDB/server/commit/736d75d455)\
  2017-09-18 16:22:32 +0300
  * MW-406 Bumped up the wsrep patch version (5.6.37-25.21)
* [Revision #b5802888e3](https://github.com/MariaDB/server/commit/b5802888e3)\
  2017-09-07 16:45:21 +0300
  * MW-402 cascading FK issues, 5.6 version
* [Revision #c6251e36fc](https://github.com/MariaDB/server/commit/c6251e36fc)\
  2017-08-10 14:04:55 +0300
  * MW-399 Freeing wsrep\_status\_vars, before provider is released.
* [Revision #6d783b6a76](https://github.com/MariaDB/server/commit/6d783b6a76)\
  2017-11-08 14:15:54 +0200
  * MW-388
* [Revision #f4f2e8fa2a](https://github.com/MariaDB/server/commit/f4f2e8fa2a)\
  2017-08-24 10:34:21 +0300
  * MW-402 cascading FK issues
* [Revision #e5e33db5fb](https://github.com/MariaDB/server/commit/e5e33db5fb)\
  2017-11-08 13:55:09 +0200
  * MW-394
* [Revision #7cedebb99b](https://github.com/MariaDB/server/commit/7cedebb99b)\
  2017-07-27 11:39:31 +0300
  * MW-394
* [Revision #b79407c5e9](https://github.com/MariaDB/server/commit/b79407c5e9)\
  2017-07-21 10:56:25 +0200
  * MW-388 Remove unnecessary conditions
* [Revision #958ad5a880](https://github.com/MariaDB/server/commit/958ad5a880)\
  2017-11-08 12:25:46 +0200
  * MW-388 Fix conflict handling of SPs with DECLARE ... HANDLER
* [Revision #76f1195f5b](https://github.com/MariaDB/server/commit/76f1195f5b)\
  2017-07-11 12:55:03 +0200
  * MW-388 Fix conflict handling of SPs with DECLARE ... HANDLER
* Merge [Revision #3cecb1bab3](https://github.com/MariaDB/server/commit/3cecb1bab3) 2017-11-03 12:34:05 +0530 - Merge tag 'mariadb-10.0.33' into bb-10.0-galera
* [Revision #53b4185e58](https://github.com/MariaDB/server/commit/53b4185e58)\
  2017-10-25 11:45:30 -0400
  * bump the VERSION
* Merge [Revision #bb62a0ad99](https://github.com/MariaDB/server/commit/bb62a0ad99) 2017-10-04 07:59:25 +0300 - Merge pull request #458 from darkain/patch-1
* [Revision #98e09ee4b6](https://github.com/MariaDB/server/commit/98e09ee4b6)\
  2017-10-02 13:21:00 -0700
  * [MDEV-13909](https://jira.mariadb.org/browse/MDEV-13909) Fix wsrep\_sst\_rsync fails on debian
* Merge [Revision #7002291b8a](https://github.com/MariaDB/server/commit/7002291b8a) 2017-11-10 01:14:58 +0100 - Merge branch '10.0' into 10.1
* [Revision #56394a78e3](https://github.com/MariaDB/server/commit/56394a78e3)\
  2017-11-03 12:33:01 +0100
  * [MDEV-12372](https://jira.mariadb.org/browse/MDEV-12372) mysqlbinlog --version output is the same on 10.x as on 5.5.x, and contains not only version
* [Revision #c97a7cdbd0](https://github.com/MariaDB/server/commit/c97a7cdbd0)\
  2017-11-09 20:51:11 +0100
  * remove redundant tests from mysql-test/include/\*.inc files
* [Revision #7ec6c6fa62](https://github.com/MariaDB/server/commit/7ec6c6fa62)\
  2017-10-22 21:29:31 +0200
  * typo
* Merge [Revision #3028357aa5](https://github.com/MariaDB/server/commit/3028357aa5) 2017-11-09 20:33:23 +0100 - Merge branch '5.5' into 10.0
* [Revision #c64a697bba](https://github.com/MariaDB/server/commit/c64a697bba)\
  2017-11-03 22:36:58 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #2e964b233b](https://github.com/MariaDB/server/commit/2e964b233b)\
  2017-11-03 17:05:41 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* Merge [Revision #d79fd5ba7f](https://github.com/MariaDB/server/commit/d79fd5ba7f) 2017-11-10 01:14:55 +0100 - Merge branch 'ks-10.1-mroonga' into 10.1
* [Revision #ac12ab8f66](https://github.com/MariaDB/server/commit/ac12ab8f66)\
  2017-10-16 09:50:49 +0900
  * Update Mroonga to the latest version on 2017-10-16T09:50:49+0900
* [Revision #13167e6489](https://github.com/MariaDB/server/commit/13167e6489)\
  2017-10-10 23:15:25 +0900
  * Update Mroonga to the latest version on 2017-10-10T23:15:25+0900
* [Revision #53c7aaf332](https://github.com/MariaDB/server/commit/53c7aaf332)\
  2017-11-09 18:59:08 +0000
  * [MDEV-14077](https://jira.mariadb.org/browse/MDEV-14077) Incremental backup extremly slow
* [Revision #d2ffafe00f](https://github.com/MariaDB/server/commit/d2ffafe00f)\
  2017-11-09 14:37:03 +0200
  * [MDEV-14333](https://jira.mariadb.org/browse/MDEV-14333) mariadb-backup --apply-log-only crashes if incomplete transactions with update\_undo logs are present
* Merge [Revision #0fdb0bdf27](https://github.com/MariaDB/server/commit/0fdb0bdf27) 2017-11-09 14:05:53 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #c2c93fc6e4](https://github.com/MariaDB/server/commit/c2c93fc6e4)\
  2017-11-08 15:47:49 +0100
  * [MDEV-14164](https://jira.mariadb.org/browse/MDEV-14164): Unknown column error when adding aggregate to function in oracle style procedure FOR loop
* [Revision #ca695888e0](https://github.com/MariaDB/server/commit/ca695888e0)\
  2017-11-07 21:57:42 +0400
  * [MDEV-14116](https://jira.mariadb.org/browse/MDEV-14116) INET6\_NTOA output is set as null to varchar(39) variable
* [Revision #644ffdeb92](https://github.com/MariaDB/server/commit/644ffdeb92)\
  2017-11-08 09:26:27 +0200
  * Fix integer type mismatch in WSREP debug output
* [Revision #28c3459aa7](https://github.com/MariaDB/server/commit/28c3459aa7)\
  2017-11-07 13:31:55 +0000
  * [MDEV-10728](https://jira.mariadb.org/browse/MDEV-10728) test excluded from embedded tests
* [Revision #c09f22bab5](https://github.com/MariaDB/server/commit/c09f22bab5)\
  2017-11-07 12:57:11 +0400
  * [MDEV-8867](https://jira.mariadb.org/browse/MDEV-8867) Wrong field type or metadata for COALESCE(bit\_column, 1)
* [Revision #120f848f75](https://github.com/MariaDB/server/commit/120f848f75)\
  2017-11-06 21:00:06 +0000
  * Fix test case
* [Revision #f830314fd5](https://github.com/MariaDB/server/commit/f830314fd5)\
  2017-11-06 22:35:03 +0200
  * Remove dead code for non-debug builds
* [Revision #40bae98c3d](https://github.com/MariaDB/server/commit/40bae98c3d)\
  2017-11-06 18:58:04 +0000
  * [MDEV-12108](https://jira.mariadb.org/browse/MDEV-12108) Fix backup for Innodb tables with DATA DIRECTORY
* Merge [Revision #5691109689](https://github.com/MariaDB/server/commit/5691109689) 2017-11-06 18:10:23 +0200 - Merge 10.0 into 10.1
* [Revision #6a524fcfdd](https://github.com/MariaDB/server/commit/6a524fcfdd)\
  2017-11-06 14:55:34 +0200
  * [MDEV-14140](https://jira.mariadb.org/browse/MDEV-14140) IMPORT TABLESPACE must not go beyond FSP\_FREE\_LIMIT
* [Revision #bfde65c0ae](https://github.com/MariaDB/server/commit/bfde65c0ae)\
  2017-11-04 02:39:16 +0200
  * [MDEV-10651](https://jira.mariadb.org/browse/MDEV-10651), [MDEV-14196](https://jira.mariadb.org/browse/MDEV-14196) sys\_vars.innodb\_buffer\_pool\_\* tests fail
* [Revision #5e5adfa729](https://github.com/MariaDB/server/commit/5e5adfa729)\
  2017-11-01 18:40:09 +0200
  * [MDEV-14029](https://jira.mariadb.org/browse/MDEV-14029) Server does not remove #sql\*.frm files after crash during ALTER TABLE
* [Revision #0ed5c09b28](https://github.com/MariaDB/server/commit/0ed5c09b28)\
  2017-11-01 19:57:47 +0200
  * [MDEV-11864](https://jira.mariadb.org/browse/MDEV-11864) main.view test uses CHECK PARTITION but does not check for the partition plugin
* [Revision #1394ea6965](https://github.com/MariaDB/server/commit/1394ea6965)\
  2017-11-03 22:36:58 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #04daf30e9b](https://github.com/MariaDB/server/commit/04daf30e9b)\
  2017-11-03 17:05:41 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #c4c48e9740](https://github.com/MariaDB/server/commit/c4c48e9740)\
  2017-03-07 19:21:42 +0100
  * [MDEV-11965](https://jira.mariadb.org/browse/MDEV-11965) -Werror should not appear in released tarballs
* [Revision #51b4366bfb](https://github.com/MariaDB/server/commit/51b4366bfb)\
  2017-11-02 22:38:37 +0200
  * [MDEV-13328](https://jira.mariadb.org/browse/MDEV-13328) ALTER TABLE…DISCARD TABLESPACE takes a lot of time
* [Revision #57ba66b9ab](https://github.com/MariaDB/server/commit/57ba66b9ab)\
  2017-11-02 22:51:34 +0200
  * Remove redundant function parameters
* [Revision #9f3c014ca3](https://github.com/MariaDB/server/commit/9f3c014ca3)\
  2017-11-03 08:18:50 +0000
  * [MDEV-10728](https://jira.mariadb.org/browse/MDEV-10728) -- mysqlbinlog can't be input to mysql client
* [Revision #51679e5c38](https://github.com/MariaDB/server/commit/51679e5c38)\
  2017-11-03 16:09:43 +0200
  * [MDEV-14132](https://jira.mariadb.org/browse/MDEV-14132) InnoDB page corruption
* [Revision #30a8764b92](https://github.com/MariaDB/server/commit/30a8764b92)\
  2017-11-02 16:18:41 +0200
  * [MDEV-14244](https://jira.mariadb.org/browse/MDEV-14244) MariaDB fails to run with O\_DIRECT
* [Revision #6ceb49a941](https://github.com/MariaDB/server/commit/6ceb49a941)\
  2017-11-03 22:36:58 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #ffb1eebe05](https://github.com/MariaDB/server/commit/ffb1eebe05)\
  2017-11-03 16:02:19 +0000
  * [MDEV-13560](https://jira.mariadb.org/browse/MDEV-13560) Copy all innodb undo tablespaces from the backup directory to destination.
* [Revision #3a3f1328fe](https://github.com/MariaDB/server/commit/3a3f1328fe)\
  2017-11-03 17:05:41 +0400
  * [MDEV-13921](https://jira.mariadb.org/browse/MDEV-13921) Audit log writes invalid SQL if single-line comments are present.
* [Revision #5d0153c408](https://github.com/MariaDB/server/commit/5d0153c408)\
  2017-11-02 14:39:54 +0200
  * [MDEV-12633](https://jira.mariadb.org/browse/MDEV-12633) Error from valgrind related to dd\_frm\_type
* [Revision #d8a9b524f2](https://github.com/MariaDB/server/commit/d8a9b524f2)\
  2017-11-02 16:58:37 +0400
  * [MDEV-14221](https://jira.mariadb.org/browse/MDEV-14221) Assertion \`0' failed in Item::field\_type\_for\_temporal\_comparison
* Merge [Revision #892cf2de13](https://github.com/MariaDB/server/commit/892cf2de13) 2017-10-31 09:11:31 +0200 - Merge 10.0 into 10.1
* [Revision #d11001d11b](https://github.com/MariaDB/server/commit/d11001d11b)\
  2017-10-27 11:36:32 +0300
  * Backport [MDEV-13890](https://jira.mariadb.org/browse/MDEV-13890) from 10.2 (InnoDB/XtraDB shutdown failure)
* [Revision #2b332ab795](https://github.com/MariaDB/server/commit/2b332ab795)\
  2017-10-30 12:31:40 -0400
  * bump the VERSION
* [Revision #88edb1b3ed](https://github.com/MariaDB/server/commit/88edb1b3ed)\
  2017-10-30 18:47:43 +0200
  * [MDEV-14219](https://jira.mariadb.org/browse/MDEV-14219) Allow online table rebuild when encryption or compression parameters change
* Merge [Revision #38e12db478](https://github.com/MariaDB/server/commit/38e12db478) 2017-10-26 13:36:38 +0300 - Merge 10.0 into 10.1
* [Revision #909cdafd35](https://github.com/MariaDB/server/commit/909cdafd35)\
  2017-10-25 09:06:45 +0300
  * [MDEV-13496](https://jira.mariadb.org/browse/MDEV-13496) Use "mariadb-backup" rather than "xtrabackup" in console output
* Merge [Revision #db203d7471](https://github.com/MariaDB/server/commit/db203d7471) 2017-10-24 19:26:24 +0300 - Merge 10.0 into 10.1
* [Revision #4330505629](https://github.com/MariaDB/server/commit/4330505629)\
  2017-10-23 14:17:50 +0000
  * Do not use File::Which, it is not always available.
* [Revision #72407e544e](https://github.com/MariaDB/server/commit/72407e544e)\
  2017-10-23 10:37:28 +0000
  * [MDEV-13496](https://jira.mariadb.org/browse/MDEV-13496) Use "mariadb-backup" rather than "xtrabackup" in console output
* [Revision #125ce6f82f](https://github.com/MariaDB/server/commit/125ce6f82f)\
  2017-10-23 10:30:17 +0000
  * [MDEV-14102](https://jira.mariadb.org/browse/MDEV-14102) restore --remove-original options for mariadb-backup
* [Revision #2aa51f528f](https://github.com/MariaDB/server/commit/2aa51f528f)\
  2017-10-22 13:18:38 +0200
  * Various compier warnings
* Merge [Revision #9d2e2d7533](https://github.com/MariaDB/server/commit/9d2e2d7533) 2017-10-22 13:03:41 +0200 - Merge branch '10.0' into 10.1
* [Revision #d11af09865](https://github.com/MariaDB/server/commit/d11af09865)\
  2017-10-16 20:54:07 +0300
  * [MDEV-14076](https://jira.mariadb.org/browse/MDEV-14076) InnoDB: Failing assertion when accessing INFORMATION\_SCHEMA.INNODB\_SYS\_TABLESPACES upon upgrade from 10.1.0 to 10.1.20
* [Revision #98cd0ec536](https://github.com/MariaDB/server/commit/98cd0ec536)\
  2017-10-14 19:43:16 +0400
  * [MDEV-10802](https://jira.mariadb.org/browse/MDEV-10802) TIMESTAMP NOT NULL field with explicit\_defaults\_for\_timestamp and NO\_ZERO\_DATE shouldn't throw error
* [Revision #9534c04515](https://github.com/MariaDB/server/commit/9534c04515)\
  2017-10-11 01:08:14 +0530
  * Bug Fix
* [Revision #9749568deb](https://github.com/MariaDB/server/commit/9749568deb)\
  2017-10-09 18:22:24 +0200
  * [MDEV-13946](https://jira.mariadb.org/browse/MDEV-13946) Server RPMs have dependency on "which"
* [Revision #9b11956e86](https://github.com/MariaDB/server/commit/9b11956e86)\
  2017-10-06 18:16:46 +0200
  * [MDEV-13049](https://jira.mariadb.org/browse/MDEV-13049) Querying INFORMATION\_SCHEMA becomes slow in [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)
* [Revision #559dec33cc](https://github.com/MariaDB/server/commit/559dec33cc)\
  2017-10-06 19:38:56 +0200
  * cleanup: is\_show\_command(thd)
* [Revision #494d1bf885](https://github.com/MariaDB/server/commit/494d1bf885)\
  2017-10-09 10:22:47 +0200
  * [MDEV-14010](https://jira.mariadb.org/browse/MDEV-14010) merge issue in wsrep\_sst\_xtrabackup-v2
* [Revision #5eb666ad37](https://github.com/MariaDB/server/commit/5eb666ad37)\
  2017-10-07 14:17:45 +0400
  * [MDEV-12705](https://jira.mariadb.org/browse/MDEV-12705) 10.1.18-MariaDB-1jessie - mysqld got signal 11.
* Merge [Revision #01e656a685](https://github.com/MariaDB/server/commit/01e656a685) 2017-10-07 08:46:37 +0000 - Merge branch 'bb-10.1-wlad' into 10.1
* [Revision #bb3f4fbb59](https://github.com/MariaDB/server/commit/bb3f4fbb59)\
  2017-10-07 07:36:17 +0000
  * [MDEV-13310](https://jira.mariadb.org/browse/MDEV-13310) Preparing an incremental backup twice can corrupt data
* [Revision #8d1fb47e1d](https://github.com/MariaDB/server/commit/8d1fb47e1d)\
  2017-10-06 22:40:28 +0000
  * [MDEV-13798](https://jira.mariadb.org/browse/MDEV-13798) - fix incorrect alignment of the buffer in incremental backup
* [Revision #0f8295d7d5](https://github.com/MariaDB/server/commit/0f8295d7d5)\
  2017-10-06 22:34:51 +0000
  * [MDEV-13822](https://jira.mariadb.org/browse/MDEV-13822) mariadb-backup incremental prepare incorrectly sets file size.
* [Revision #420798a81a](https://github.com/MariaDB/server/commit/420798a81a)\
  2017-10-06 16:36:40 +0000
  * Refactor os\_file\_set\_size to extend already existing files.
* [Revision #0373e05a59](https://github.com/MariaDB/server/commit/0373e05a59)\
  2017-10-05 18:38:29 +0000
  * Refactor os\_file\_set\_size() so it can be used to extend existing file, not just for creating new files.
* [Revision #f9b50c0657](https://github.com/MariaDB/server/commit/f9b50c0657)\
  2017-10-06 17:51:29 +0300
  * [MDEV-13512](https://jira.mariadb.org/browse/MDEV-13512) buf\_flush\_update\_zip\_checksum() corrupts SPATIAL INDEX in ROW\_FORMAT=COMPRESSED tables
* [Revision #1cfaafafee](https://github.com/MariaDB/server/commit/1cfaafafee)\
  2017-10-05 13:41:16 +0400
  * [MDEV-13242](https://jira.mariadb.org/browse/MDEV-13242) Wrong results for queries with row constructors and information\_schema
* [Revision #bcda03b4fa](https://github.com/MariaDB/server/commit/bcda03b4fa)\
  2017-10-02 13:30:48 +0530
  * [MDEV-13950](https://jira.mariadb.org/browse/MDEV-13950) mysqld\_safe could not start Galera node after upgrade ...
* Merge [Revision #ac0b5a2e79](https://github.com/MariaDB/server/commit/ac0b5a2e79) 2017-10-02 10:45:55 +0300 - Merge 10.0 into 10.1
* [Revision #b8488e5cf5](https://github.com/MariaDB/server/commit/b8488e5cf5)\
  2017-09-29 14:12:38 +0300
  * [MDEV-13932](https://jira.mariadb.org/browse/MDEV-13932): fil0pagecompress.cc fails to compile with lzo 2.10
* [Revision #4d01dd79a1](https://github.com/MariaDB/server/commit/4d01dd79a1)\
  2017-09-28 12:38:51 +0300
  * [MDEV-12634](https://jira.mariadb.org/browse/MDEV-12634): Uninitialised ROW\_MERGE\_RESERVE\_SIZE bytes written to temporary file
* [Revision #4aeec7275f](https://github.com/MariaDB/server/commit/4aeec7275f)\
  2017-09-27 18:27:39 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
