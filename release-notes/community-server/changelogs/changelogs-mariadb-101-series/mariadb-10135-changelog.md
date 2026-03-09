# MariaDB 10.1.35 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.35)[Release Notes](../../old-releases/10.1/10.1.35.md)[Changelog](mariadb-10135-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 7 Aug 2018

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.35.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #50c4262002](https://github.com/MariaDB/server/commit/50c4262002)\
  2018-08-04 22:53:16 +0100
  * [MDEV-16544](https://jira.mariadb.org/browse/MDEV-16544) - crash in ha\_sphinx::create()
* [Revision #1e37fa70bd](https://github.com/MariaDB/server/commit/1e37fa70bd)\
  2018-08-04 03:06:27 +0300
  * Updated list of unstable tests for 10.1.35 release
* [Revision #701f0b8e36](https://github.com/MariaDB/server/commit/701f0b8e36)\
  2018-08-03 14:37:55 +0200
  * Fix gcc 7.3 compiler warnings.
* [Revision #9d42eb5e28](https://github.com/MariaDB/server/commit/9d42eb5e28)\
  2018-08-03 12:30:50 +0300
  * Disable an unstable test
* [Revision #769f6d2db7](https://github.com/MariaDB/server/commit/769f6d2db7)\
  2018-08-03 12:21:13 +0300
  * Fix -Wclass-memaccess in WSREP,InnoDB,XtraDB
* Merge [Revision #0d3972c6be](https://github.com/MariaDB/server/commit/0d3972c6be) 2018-08-03 12:03:10 +0300 - Merge 10.0 into 10.1
* [Revision #9dfef6e29b](https://github.com/MariaDB/server/commit/9dfef6e29b)\
  2018-08-03 11:22:20 +0300
  * Fix -Wclass-memaccess warnings in InnoDB,XtraDB
* [Revision #b963cbaf4b](https://github.com/MariaDB/server/commit/b963cbaf4b)\
  2018-08-03 11:49:49 +0300
  * Follow-up fix to [MDEV-16865](https://jira.mariadb.org/browse/MDEV-16865): InnoDB fts\_query() ignores KILL
* [Revision #90b66c1699](https://github.com/MariaDB/server/commit/90b66c1699)\
  2018-08-01 12:09:33 -0400
  * bump the VERSION
* [Revision #b4f7f12e2b](https://github.com/MariaDB/server/commit/b4f7f12e2b)\
  2018-08-02 20:27:10 +0200
  * fix galera test.
* Merge [Revision #2fb68244b4](https://github.com/MariaDB/server/commit/2fb68244b4) 2018-08-01 08:45:59 +0300 - Merge 10.0 into 10.1
* [Revision #a7f84f09bf](https://github.com/MariaDB/server/commit/a7f84f09bf)\
  2018-07-31 16:12:38 +0300
  * [MDEV-16865](https://jira.mariadb.org/browse/MDEV-16865) InnoDB fts\_query() ignores KILL
* [Revision #b3e95086e1](https://github.com/MariaDB/server/commit/b3e95086e1)\
  2018-07-31 14:29:05 +0300
  * Fix function pointer type mismatch
* Merge [Revision #87ec6a0448](https://github.com/MariaDB/server/commit/87ec6a0448) 2018-07-31 15:19:56 +0300 - Merge 10.0 into 10.1
* Merge [Revision #865e807125](https://github.com/MariaDB/server/commit/865e807125) 2018-07-31 11:58:29 +0200 - Merge branch '10.0' into 10.1
* [Revision #14306bcbec](https://github.com/MariaDB/server/commit/14306bcbec)\
  2018-07-27 10:05:26 +0300
  * [MDEV-16831](https://jira.mariadb.org/browse/MDEV-16831): Galera test failure on galera\_sst\_mysqldump\_with\_key
* Merge [Revision #189157d052](https://github.com/MariaDB/server/commit/189157d052) 2018-07-26 06:34:33 +0200 - Merge branch '10.1' into bb-10.1-merge-sanja
* [Revision #1fde449f1d](https://github.com/MariaDB/server/commit/1fde449f1d)\
  2018-07-24 23:45:55 -0700
  * [MDEV-16820](https://jira.mariadb.org/browse/MDEV-16820) Lost 'Impossible where' from query with inexpensive subquery
* Merge [Revision #cb5952b506](https://github.com/MariaDB/server/commit/cb5952b506) 2018-07-25 22:24:40 +0200 - Merge branch '10.0' into bb-10.1-merge-sanja
* [Revision #57cde8ccd1](https://github.com/MariaDB/server/commit/57cde8ccd1)\
  2018-07-25 08:21:25 +0300
  * [MDEV-15822](https://jira.mariadb.org/browse/MDEV-15822): WSREP: BF lock wait long for trx
* [Revision #a0d33dc6ef](https://github.com/MariaDB/server/commit/a0d33dc6ef)\
  2018-07-20 13:35:58 +0200
  * [MDEV-16689](https://jira.mariadb.org/browse/MDEV-16689): core-file should become a real server variable
* [Revision #323f269d40](https://github.com/MariaDB/server/commit/323f269d40)\
  2018-07-19 15:13:31 +0300
  * [MDEV-10564](https://jira.mariadb.org/browse/MDEV-10564): Galera `wsrep_debug` patch logs MySQL user credentials
* Merge [Revision #fb4b3472d2](https://github.com/MariaDB/server/commit/fb4b3472d2) 2018-07-19 19:13:44 +0200 - Merge branch '10.1' into bb-10.1-merge-sanja
* [Revision #09f147659f](https://github.com/MariaDB/server/commit/09f147659f)\
  2018-07-19 12:07:07 +0300
  * [MDEV-16777](https://jira.mariadb.org/browse/MDEV-16777): galera.galera\_gra\_log fails with File ...GRA\_\*.log not found error
* [Revision #4d06b7e1bd](https://github.com/MariaDB/server/commit/4d06b7e1bd)\
  2018-07-18 11:22:17 +0300
  * [MDEV-16769](https://jira.mariadb.org/browse/MDEV-16769): Notes "WSREP: Waiting for SST to complete" flood the error log
* Merge [Revision #0896d7ebc3](https://github.com/MariaDB/server/commit/0896d7ebc3) 2018-07-19 12:55:54 +0200 - Merge branch '10.0' into bb-10.1-merge
* Merge [Revision #312de43f40](https://github.com/MariaDB/server/commit/312de43f40) 2018-07-18 10:25:35 +0300 - Merge pull request #786 from codership/10.1-[MDEV-14612](https://jira.mariadb.org/browse/MDEV-14612)
* [Revision #15c6d6a94a](https://github.com/MariaDB/server/commit/15c6d6a94a)\
  2018-06-07 17:12:38 +0300
  * [MDEV-14612](https://jira.mariadb.org/browse/MDEV-14612) wsrep\_sst\_mariadb-backup unnecessarily converts address to host name
* Merge [Revision #e08ddccc35](https://github.com/MariaDB/server/commit/e08ddccc35) 2018-07-16 12:22:36 +0300 - Merge pull request #793 from codership/10.1-[MDEV-15442](https://jira.mariadb.org/browse/MDEV-15442)
* [Revision #7a7a61998c](https://github.com/MariaDB/server/commit/7a7a61998c)\
  2018-06-20 13:16:34 +0200
  * [MDEV-15442](https://jira.mariadb.org/browse/MDEV-15442) xtrabackup-v2 SST donor stuck in DONOR/DESYNCED state when joiner is killed
* [Revision #e5c6580178](https://github.com/MariaDB/server/commit/e5c6580178)\
  2018-06-19 16:09:31 +0200
  * [MDEV-15442](https://jira.mariadb.org/browse/MDEV-15442) xtrabackup-v2 SST donor stuck in DONOR/DESYNCED state when joiner is killed
* [Revision #fe9f2f4bb6](https://github.com/MariaDB/server/commit/fe9f2f4bb6)\
  2018-06-06 14:19:14 +0300
  * [MDEV-16401](https://jira.mariadb.org/browse/MDEV-16401): Apply review comments to [MDEV-16005](https://jira.mariadb.org/browse/MDEV-16005)
* [Revision #b75d819604](https://github.com/MariaDB/server/commit/b75d819604)\
  2018-07-15 18:40:25 -0700
  * [MDEV-16711](https://jira.mariadb.org/browse/MDEV-16711) Crash in Field\_blob::store() while reading statistics for the small InnoDB table
* [Revision #ae0eb507bd](https://github.com/MariaDB/server/commit/ae0eb507bd)\
  2018-07-13 23:03:57 -0700
  * [MDEV-16760](https://jira.mariadb.org/browse/MDEV-16760) CREATE OR REPLACE TABLE never updates statistical tables
* [Revision #095dc81158](https://github.com/MariaDB/server/commit/095dc81158)\
  2018-07-15 16:24:24 -0700
  * [MDEV-16757](https://jira.mariadb.org/browse/MDEV-16757) Memory leak after adding manually min/max statistical data for blob column
* [Revision #1d10c9afe0](https://github.com/MariaDB/server/commit/1d10c9afe0)\
  2018-07-02 15:29:22 +0300
  * Post-fix to "Adopt Debian's fix-FTBFS-on-GNU-Hurd.patch", part #2.
* [Revision #36ea82617c](https://github.com/MariaDB/server/commit/36ea82617c)\
  2018-06-29 18:16:56 +0300
  * Fix a typo a in the commit before the last one
* [Revision #83bf267e0d](https://github.com/MariaDB/server/commit/83bf267e0d)\
  2018-06-29 12:09:38 +0300
  * Fix Internal Compiler Error GCC-6.3.0
* [Revision #f46acd4a3a](https://github.com/MariaDB/server/commit/f46acd4a3a)\
  2018-06-29 14:00:00 +0300
  * Adopt Debian's fix-FTBFS-on-GNU-Hurd.patch.
* [Revision #45cabf1017](https://github.com/MariaDB/server/commit/45cabf1017)\
  2018-06-28 16:17:21 +0200
  * [MDEV-16615](https://jira.mariadb.org/browse/MDEV-16615) ASAN SEGV in handler::print\_error or server crash after error upon CREATE TABLE
* [Revision #8ca18294d5](https://github.com/MariaDB/server/commit/8ca18294d5)\
  2018-03-18 21:01:41 +0200
  * [MDEV-14014](https://jira.mariadb.org/browse/MDEV-14014) Multi-Slave Replication Fail: bogus data in log event
* [Revision #16c14d7ba0](https://github.com/MariaDB/server/commit/16c14d7ba0)\
  2018-06-21 09:43:05 +0200
  * mark ed25519 stable
* Merge [Revision #44d1cada12](https://github.com/MariaDB/server/commit/44d1cada12) 2018-06-28 14:07:51 +0200 - Merge branch '10.0' into 10.1
* [Revision #be5698265a](https://github.com/MariaDB/server/commit/be5698265a)\
  2018-06-27 12:37:21 +0300
  * [MDEV-15607](https://jira.mariadb.org/browse/MDEV-15607): mysqld crashed few after node is being joined with sst
* Merge [Revision #c6392d52ee](https://github.com/MariaDB/server/commit/c6392d52ee) 2018-06-26 17:34:44 +0300 - Merge 10.0 into 10.1
* [Revision #c4eb4bcef6](https://github.com/MariaDB/server/commit/c4eb4bcef6)\
  2018-06-26 11:34:51 +0300
  * [MDEV-16515](https://jira.mariadb.org/browse/MDEV-16515) InnoDB: Failing assertion: ++retries < 10000 in file dict0dict.cc
* Merge [Revision #c09a8b5b36](https://github.com/MariaDB/server/commit/c09a8b5b36) 2018-06-21 08:34:35 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #4b821e02f6](https://github.com/MariaDB/server/commit/4b821e02f6) 2018-06-20 16:57:21 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #bb24663f5a](https://github.com/MariaDB/server/commit/bb24663f5a)\
  2018-06-20 10:45:57 +0200
  * [MDEV-13577](https://jira.mariadb.org/browse/MDEV-13577) slave\_parallel\_mode=optimistic should not report the mode's specific temporary errors
* [Revision #44682962e3](https://github.com/MariaDB/server/commit/44682962e3)\
  2018-06-20 11:10:15 +0200
  * Fix another double WSREP\_ISOLATION\_BEGIN merge error
* [Revision #04c4745478](https://github.com/MariaDB/server/commit/04c4745478)\
  2018-06-20 01:28:59 +0300
  * Fix double WSREP\_ISOLATION\_BEGIN merge error
* Merge [Revision #f5b128dfad](https://github.com/MariaDB/server/commit/f5b128dfad) 2018-06-19 14:04:53 +0400 - Merge remote-tracking branch 'origin/10.0' into 10.1
* [Revision #f7b1b2bc5d](https://github.com/MariaDB/server/commit/f7b1b2bc5d)\
  2018-06-18 07:40:58 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
