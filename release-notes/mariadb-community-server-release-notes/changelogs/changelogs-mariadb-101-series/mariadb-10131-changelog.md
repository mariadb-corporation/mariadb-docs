# MariaDB 10.1.31 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.31)[Release Notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes.md)[Changelog](mariadb-10131-changelog.md)[Overview of 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)

**Release date:** 6 Feb 2018

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10131-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Merge [Revision #3f42529a6f](https://github.com/MariaDB/server/commit/3f42529a6f) 2018-02-05 09:25:33 +0200 - Merge 10.0 into 10.1
* [Revision #cb5374801e](https://github.com/MariaDB/server/commit/cb5374801e)\
  2018-02-05 09:23:36 +0200
  * [MDEV-15202](https://jira.mariadb.org/browse/MDEV-15202) innodb.log\_file\_size failed in buildbot
* [Revision #aba15b864a](https://github.com/MariaDB/server/commit/aba15b864a)\
  2018-02-04 04:28:14 +0200
  * Updated list of unstable tests for 10.1.31 release
* Merge [Revision #8812a2f858](https://github.com/MariaDB/server/commit/8812a2f858) 2018-02-03 12:53:30 +0200 - Merge 10.0 into 10.1
* Merge [Revision #0765caa073](https://github.com/MariaDB/server/commit/0765caa073) 2018-02-02 18:14:35 +0100 - Merge remote-tracking branch 'origin/5.5' into 10.0
* [Revision #7a63ffab71](https://github.com/MariaDB/server/commit/7a63ffab71)\
  2018-01-29 18:56:08 +0200
  * Fix an out of scope bzero
* [Revision #5edd129fbf](https://github.com/MariaDB/server/commit/5edd129fbf)\
  2018-01-30 21:05:27 +0200
  * Fix ASAN failure in main.lock (and others)
* [Revision #ded07724ee](https://github.com/MariaDB/server/commit/ded07724ee)\
  2018-01-29 19:46:59 +0200
  * [MDEV-15014](https://jira.mariadb.org/browse/MDEV-15014) Assertion \`m\_cache\_lock\_status == LOCKED\_NO\_WAIT || m\_cache\_status == DISABLE\_REQUEST' failed in Query\_cache::free\_cache on startup
* [Revision #ec03390f9b](https://github.com/MariaDB/server/commit/ec03390f9b)\
  2018-02-03 12:52:25 +0200
  * fil\_write\_flushed\_lsn(): Ensure that the return value is initialized
* [Revision #d7d910d08b](https://github.com/MariaDB/server/commit/d7d910d08b)\
  2018-02-03 12:50:38 +0200
  * Fix a warning about possibly unused variable
* [Revision #a988c70922](https://github.com/MariaDB/server/commit/a988c70922)\
  2018-02-03 12:49:41 +0200
  * After-merge test result fix
* Merge [Revision #c383418cbf](https://github.com/MariaDB/server/commit/c383418cbf) 2018-02-03 08:09:06 +0100 - Merge branch 'github/10.0-galera' into 10.1
* Merge [Revision #c7e5feb259](https://github.com/MariaDB/server/commit/c7e5feb259) 2018-02-01 14:09:48 +0200 - Merge tag 'mariadb-10.0.34' into 10.0-galera
* Merge [Revision #08b2c516da](https://github.com/MariaDB/server/commit/08b2c516da) 2018-01-24 10:29:52 +0200 - Merge pull request #549 from grooverdan/10.0-galera-sst-default-options
* [Revision #c4b7074e72](https://github.com/MariaDB/server/commit/c4b7074e72)\
  2018-01-16 14:44:27 +1100
  * wsrep\_sst\_xtrabackup\*: use mysqld defaults arguments
* [Revision #3f27fa3797](https://github.com/MariaDB/server/commit/3f27fa3797)\
  2018-01-14 13:50:05 +1100
  * mtr: minor (and incomplete) fixes for suite galera\_3node
* [Revision #a2a038152e](https://github.com/MariaDB/server/commit/a2a038152e)\
  2018-01-14 12:46:03 +1100
  * wsrep\_sst\_xtrabackup\*: use wsrep\_sst\_common parsed vars
* [Revision #51ea696c8e](https://github.com/MariaDB/server/commit/51ea696c8e)\
  2018-01-14 12:34:11 +1100
  * wsrep\_sst\_common: keep WSREP\_SST\_OPT\_HOST\_UNESCAPED for IPv4
* [Revision #722df90534](https://github.com/MariaDB/server/commit/722df90534)\
  2018-01-14 12:18:26 +1100
  * wsrep\_sst\_xtrabackup\*: read all sections of config not nust mysqld
* [Revision #cc8abb21e3](https://github.com/MariaDB/server/commit/cc8abb21e3)\
  2018-01-14 11:38:12 +1100
  * wsrep\_sst\_xtrabackup\*: du -s removed lessens output
* [Revision #e78e308e81](https://github.com/MariaDB/server/commit/e78e308e81)\
  2018-01-14 11:28:43 +1100
  * wsrep\_sst\_common: parse --address and split WSREP\_SST\_OPT\_PATH
* [Revision #95e5fe6732](https://github.com/MariaDB/server/commit/95e5fe6732)\
  2018-01-13 23:05:21 +1100
  * wsrep\_sst\_common: parse\_cnf - use awk rather than grep/cut/tail excessiveness
* [Revision #943c62a5d4](https://github.com/MariaDB/server/commit/943c62a5d4)\
  2014-09-26 15:54:42 +0200
  * Backport 4bb49d84a9df, correct handling on defaults\[-extra]-file is SST scripts
* [Revision #f69a3b2e92](https://github.com/MariaDB/server/commit/f69a3b2e92)\
  2018-02-02 19:43:47 +0200
  * After-merge fix for commit d4df7bc9b1fbdfb5c98134091a9ff998af60954f
* [Revision #f694df6ac5](https://github.com/MariaDB/server/commit/f694df6ac5)\
  2018-02-02 17:21:27 +0100
  * Fix of NULLIF print statement.
* [Revision #29031fe391](https://github.com/MariaDB/server/commit/29031fe391)\
  2018-02-02 11:41:16 +0100
  * my\_addr\_resolve fixes
* [Revision #bd0eb2bdd7](https://github.com/MariaDB/server/commit/bd0eb2bdd7)\
  2018-02-02 11:38:39 +0100
  * less memory-leak-on-exit reports for clients
* [Revision #d94d937d1c](https://github.com/MariaDB/server/commit/d94d937d1c)\
  2018-02-02 11:35:13 +0100
  * compiler warning (signed/unsigned comparison)
* Merge [Revision #d4df7bc9b1](https://github.com/MariaDB/server/commit/d4df7bc9b1) 2018-02-01 21:55:30 +0100 - Merge branch 'github/10.0' into 10.1
* [Revision #96cb428b35](https://github.com/MariaDB/server/commit/96cb428b35)\
  2018-01-29 09:44:17 +0100
  * [MDEV-14862](https://jira.mariadb.org/browse/MDEV-14862): Server crashes in Bitmap<64u>::merge / add\_key\_field
* [Revision #d6638586c6](https://github.com/MariaDB/server/commit/d6638586c6)\
  2018-01-31 20:22:31 +0100
  * don't crash debug builds on "packets out of order"
* [Revision #f4414d4c4e](https://github.com/MariaDB/server/commit/f4414d4c4e)\
  2018-01-30 10:54:28 -0500
  * bump the VERSION
* [Revision #6b4a4a85a7](https://github.com/MariaDB/server/commit/6b4a4a85a7)\
  2018-01-30 11:28:21 +0400
  * [MDEV-14696](https://jira.mariadb.org/browse/MDEV-14696) Server crashes in prep\_alter\_part\_table on 2nd execution of PS.
* [Revision #c4a908cb56](https://github.com/MariaDB/server/commit/c4a908cb56)\
  2018-01-30 11:35:27 +0400
  * [MDEV-13790](https://jira.mariadb.org/browse/MDEV-13790) UNHEX() of a somewhat complicated CONCAT() returns NULL
* [Revision #dae4fb0acb](https://github.com/MariaDB/server/commit/dae4fb0acb)\
  2018-01-30 11:07:35 +0400
  * [MDEV-15118](https://jira.mariadb.org/browse/MDEV-15118) ExtractValue(xml,something\_complex) does not work
* [Revision #b76881a23c](https://github.com/MariaDB/server/commit/b76881a23c)\
  2018-01-29 16:39:54 +0200
  * Do not SET DEBUG\_DBUG=-d,... in tests
* Merge [Revision #a5fcced7d1](https://github.com/MariaDB/server/commit/a5fcced7d1) 2018-01-29 16:32:59 +0200 - Merge 5.5 into 10.0
* [Revision #547ec8ce27](https://github.com/MariaDB/server/commit/547ec8ce27)\
  2018-01-29 16:25:26 +0200
  * Do not SET DEBUG\_DBUG=-d,... in tests
* [Revision #ee8755e3c5](https://github.com/MariaDB/server/commit/ee8755e3c5)\
  2018-01-24 14:42:52 +0100
  * [MDEV-15012](https://jira.mariadb.org/browse/MDEV-15012): ASAN: numerous test failures in PS
* [Revision #706ed8552d](https://github.com/MariaDB/server/commit/706ed8552d)\
  2018-01-29 11:01:02 +0200
  * Revert "[MDEV-6928](https://jira.mariadb.org/browse/MDEV-6928): Add trx pointer to struct mtr\_t"
* [Revision #80d3eee072](https://github.com/MariaDB/server/commit/80d3eee072)\
  2018-01-26 16:59:53 +0100
  * [MDEV-14857](https://jira.mariadb.org/browse/MDEV-14857): problem with 10.2.11 server crashing when executing stored procedure
* [Revision #ad0013c8e2](https://github.com/MariaDB/server/commit/ad0013c8e2)\
  2018-01-29 15:10:31 +0100
  * [MDEV-14343](https://jira.mariadb.org/browse/MDEV-14343) Server crash on FIPS with openssl-1.0.2k
* [Revision #fb24eb87a8](https://github.com/MariaDB/server/commit/fb24eb87a8)\
  2018-01-19 20:55:34 +1100
  * [MDEV-12301](https://jira.mariadb.org/browse/MDEV-12301): galera\_recovery use @sbindir@ macro for mysqld
* [Revision #2749d25096](https://github.com/MariaDB/server/commit/2749d25096)\
  2018-01-29 14:21:08 +0200
  * [MDEV-13499](https://jira.mariadb.org/browse/MDEV-13499): Backing up table that "doesn't exist in engine" cause crash in mariadb-backup when using encryption
* [Revision #f9179b36d3](https://github.com/MariaDB/server/commit/f9179b36d3)\
  2018-01-23 14:11:53 +1100
  * systemd: revert to KillMode=control-group for galera
* [Revision #ac7610744a](https://github.com/MariaDB/server/commit/ac7610744a)\
  2018-01-28 02:09:35 +1100
  * mtr: set @skip\_auth\_anonymous=1 (#538)
* [Revision #524221e7a3](https://github.com/MariaDB/server/commit/524221e7a3)\
  2018-01-24 11:23:44 +0000
  * try to fix \[Warning] InnoDB: innodb\_open\_files=20 is exceeded (20) files stay open) on Appveyor
* Merge [Revision #72542ffd77](https://github.com/MariaDB/server/commit/72542ffd77) 2018-01-24 10:31:00 +0200 - Merge pull request #550 from grooverdan/10.1-wsrep\_sst\_mysqldump-no-max-version
* [Revision #c73b4b1698](https://github.com/MariaDB/server/commit/c73b4b1698)\
  2018-01-14 18:57:48 +1100
  * wsrep\_sst\_mysqldump: enforce a minimum version only
* Merge [Revision #f4d798635e](https://github.com/MariaDB/server/commit/f4d798635e) 2018-01-23 15:53:58 +0200 - Merge pull request #560 from grooverdan/10.1-[MDEV-13789](https://jira.mariadb.org/browse/MDEV-13789)-freebsd-wsrep-sst-xtrabackup
* [Revision #be83785d73](https://github.com/MariaDB/server/commit/be83785d73)\
  2018-01-18 22:04:12 +1100
  * [MDEV-13789](https://jira.mariadb.org/browse/MDEV-13789): FreeBSD wsrep\_sst\_xtrabackup-v2 - find compatibilty +lsof
* [Revision #30b1fbda28](https://github.com/MariaDB/server/commit/30b1fbda28)\
  2018-01-22 20:16:19 +0000
  * [MDEV-14746](https://jira.mariadb.org/browse/MDEV-14746) : read \[mariadb-backup] section from config file.
* [Revision #054051bb76](https://github.com/MariaDB/server/commit/054051bb76)\
  2018-01-22 20:01:03 +0000
  * [MDEV-14150](https://jira.mariadb.org/browse/MDEV-14150) - backup should fail early if rsync is missing
* [Revision #e30cdb68e5](https://github.com/MariaDB/server/commit/e30cdb68e5)\
  2018-01-22 15:10:52 +0000
  * mariadb-backup : improve help text
* [Revision #4794e5b091](https://github.com/MariaDB/server/commit/4794e5b091)\
  2018-01-15 16:19:46 +0200
  * Fix a test that always failed on --embedded
* [Revision #578ffcc5ef](https://github.com/MariaDB/server/commit/578ffcc5ef)\
  2018-01-11 10:56:13 +0200
  * Skip mariadb-backup.huge\_lsn if encryption is not available
* Merge [Revision #c15b3d2d41](https://github.com/MariaDB/server/commit/c15b3d2d41) 2018-01-11 10:44:05 +0200 - Merge 10.0 into 10.1
* [Revision #07aa985979](https://github.com/MariaDB/server/commit/07aa985979)\
  2018-01-09 12:37:58 +0200
  * [MDEV-14776](https://jira.mariadb.org/browse/MDEV-14776): InnoDB Monitor output generated by specific error is flooding error logs
* [Revision #18ccbf014a](https://github.com/MariaDB/server/commit/18ccbf014a)\
  2018-01-08 17:09:21 +0200
  * Make the [MDEV-14874](https://jira.mariadb.org/browse/MDEV-14874) test case more robust
* Merge [Revision #29b6e809a9](https://github.com/MariaDB/server/commit/29b6e809a9) 2018-01-08 14:51:20 +0200 - Merge 10.0 into 10.1
* [Revision #16d308e21d](https://github.com/MariaDB/server/commit/16d308e21d)\
  2018-01-08 09:24:13 +0200
  * [MDEV-14874](https://jira.mariadb.org/browse/MDEV-14874) innodb\_encrypt\_log corrupts the log when the LSN crosses 32-bit boundary
* [Revision #3a22d6c136](https://github.com/MariaDB/server/commit/3a22d6c136)\
  2018-01-05 18:22:57 +0000
  * Fix conf\_to\_src build.
* [Revision #d9e0c06b5d](https://github.com/MariaDB/server/commit/d9e0c06b5d)\
  2017-12-21 12:04:07 +0300
  * Tests: detect table count for some encryption tests
* Merge [Revision #21470de148](https://github.com/MariaDB/server/commit/21470de148) 2018-01-04 20:42:29 +0200 - Merge 10.0 into 10.1
* Merge [Revision #1e89c86dd7](https://github.com/MariaDB/server/commit/1e89c86dd7) 2018-01-03 20:41:34 +0200 - Merge 10.0 into 10.1
* Merge [Revision #016caa3d20](https://github.com/MariaDB/server/commit/016caa3d20) 2018-01-02 21:57:22 +0200 - Merge 10.0 into 10.1
* [Revision #7e4c185c77](https://github.com/MariaDB/server/commit/7e4c185c77)\
  2017-09-13 21:02:44 +0200
  * [MDEV-14272](https://jira.mariadb.org/browse/MDEV-14272) Mariadb crashes with signal 11 when using federatedx engine and galera
* Merge [Revision #d1c2cd30b7](https://github.com/MariaDB/server/commit/d1c2cd30b7) 2017-12-27 17:50:39 +0200 - Merge remote-tracking branch '10.0' into 10.1
* [Revision #5377242fff](https://github.com/MariaDB/server/commit/5377242fff)\
  2017-12-24 18:39:00 +0100
  * [MDEV-14026](https://jira.mariadb.org/browse/MDEV-14026) ALTER TABLE ... DELAY\_KEY\_WRITE=1 creates table copy for partitioned MyISAM table with DATA DIRECTORY/INDEX DIRECTORY options
* [Revision #6d8b1bd620](https://github.com/MariaDB/server/commit/6d8b1bd620)\
  2017-12-24 18:37:42 +0100
  * cleanup: ha\_partition::update\_create\_info
* [Revision #c881d82c93](https://github.com/MariaDB/server/commit/c881d82c93)\
  2017-12-24 17:21:50 +0100
  * cleanup: ha\_myisam::data\_file\_name and index\_file\_name
* [Revision #2fe6186124](https://github.com/MariaDB/server/commit/2fe6186124)\
  2017-12-25 05:09:49 +0530
  * [MDEV-10715](https://jira.mariadb.org/browse/MDEV-10715) Galera: Replicate MariaDB GTID to other nodes in the cluster
* [Revision #db3bdca7c2](https://github.com/MariaDB/server/commit/db3bdca7c2)\
  2017-12-22 16:45:20 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
