# MariaDB 5.5.51 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.51)[Release Notes](../../old-releases/5.5/5.5.51.md)[Changelog](mariadb-5551-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 10 Aug 2016

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.51.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #5ad0206](https://github.com/MariaDB/server/commit/5ad0206)\
  2016-08-09 16:15:10 +0300
  * [MDEV-10341](https://jira.mariadb.org/browse/MDEV-10341): InnoDB: Failing assertion: mutex\_own(mutex) - mutex\_exit\_func
* [Revision #0098d78](https://github.com/MariaDB/server/commit/0098d78)\
  2016-08-09 13:25:40 +0200
  * [MDEV-10465](https://jira.mariadb.org/browse/MDEV-10465) general\_log\_file can be abused
* [Revision #a3f6424](https://github.com/MariaDB/server/commit/a3f6424)\
  2016-08-08 12:58:27 +0200
  * [MDEV-6128](https://jira.mariadb.org/browse/MDEV-6128):\[PATCH] mysqlcheck wrongly escapes '.' in table names
* [Revision #2a54a53](https://github.com/MariaDB/server/commit/2a54a53)\
  2016-08-08 10:27:22 +0200
  * [MDEV-10465](https://jira.mariadb.org/browse/MDEV-10465) general\_log\_file can be abused
* [Revision #a7c43a6](https://github.com/MariaDB/server/commit/a7c43a6)\
  2016-01-26 14:49:25 +0200
  * [MDEV-9304](https://jira.mariadb.org/browse/MDEV-9304): MariaDB crash with specific query
* [Revision #5269d37](https://github.com/MariaDB/server/commit/5269d37)\
  2016-08-08 18:37:02 +0400
  * [MDEV-10468](https://jira.mariadb.org/browse/MDEV-10468) Assertion \`nr >= 0.0' failed in Item\_sum\_std::val\_real()
* [Revision #1b3430a](https://github.com/MariaDB/server/commit/1b3430a)\
  2016-08-08 16:04:40 +0400
  * [MDEV-10500](https://jira.mariadb.org/browse/MDEV-10500) CASE/IF Statement returns multiple values and shifts further result values to the next column
* [Revision #5e23b63](https://github.com/MariaDB/server/commit/5e23b63)\
  2016-08-07 11:02:42 +0200
  * [MDEV-10506](https://jira.mariadb.org/browse/MDEV-10506) Protocol::end\_statement(): Assertion \`0' failed upon ALTER TABLE
* [Revision #93d5cdf](https://github.com/MariaDB/server/commit/93d5cdf)\
  2016-08-04 13:14:45 +0300
  * [MDEV-9946](https://jira.mariadb.org/browse/MDEV-9946): main.xtradb\_mrr fails sporadically
* [Revision #c0cb84b](https://github.com/MariaDB/server/commit/c0cb84b) 2016-08-04 10:57:55 +0200 - Merge branch 'bb-5.5-serg' into 5.5
* [Revision #470f259](https://github.com/MariaDB/server/commit/470f259)\
  2016-08-03 20:56:24 +0200
  * [MDEV-10465](https://jira.mariadb.org/browse/MDEV-10465) general\_log\_file can be abused
* [Revision #0214115](https://github.com/MariaDB/server/commit/0214115)\
  2016-08-01 16:53:57 +0200
  * trivial cleanup
* [Revision #03dec1a](https://github.com/MariaDB/server/commit/03dec1a)\
  2016-08-03 18:05:29 +0200
  * [MDEV-10350](https://jira.mariadb.org/browse/MDEV-10350) "./mtr --report-features" doesn't work
* [Revision #9d2f892](https://github.com/MariaDB/server/commit/9d2f892)\
  2016-08-03 17:58:56 +0200
  * [MDEV-7329](https://jira.mariadb.org/browse/MDEV-7329) plugins.pam\_cleartext fails sporadically in buildbot
* [Revision #75891ed](https://github.com/MariaDB/server/commit/75891ed)\
  2016-08-03 17:50:45 +0200
  * improve pam\_cleartext.test a bit
* [Revision #5265243](https://github.com/MariaDB/server/commit/5265243) 2016-08-03 20:44:08 +0200 - Merge branch 'merge/merge-xtradb-5.5' into 5.5
* [Revision #e316c46](https://github.com/MariaDB/server/commit/e316c46)\
  2016-08-03 20:43:29 +0200
  * 5.5.50-38.0
* [Revision #19fe10c](https://github.com/MariaDB/server/commit/19fe10c)\
  2016-08-03 20:39:47 +0200
  * [MDEV-6581](https://jira.mariadb.org/browse/MDEV-6581) Writing to TEMPORARY TABLE not possible in read-only
* [Revision #a350e53](https://github.com/MariaDB/server/commit/a350e53) 2016-08-03 20:38:25 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #eb32dfd](https://github.com/MariaDB/server/commit/eb32dfd)\
  2016-08-03 11:49:35 +0400
  * [MDEV-10365](https://jira.mariadb.org/browse/MDEV-10365) - Race condition in error handling of INSERT DELAYED
* [Revision #511313b](https://github.com/MariaDB/server/commit/511313b)\
  2016-08-03 13:42:46 +0000
  * [MDEV-10010](https://jira.mariadb.org/browse/MDEV-10010) - potential deadlock on windows due to recursive SRWLock acquisition
* [Revision #141f88d](https://github.com/MariaDB/server/commit/141f88d)\
  2016-08-03 12:41:38 +0000
  * [MDEV-10357](https://jira.mariadb.org/browse/MDEV-10357) my\_context\_continue() does not store current fiber on Windows
* [Revision #ecb7ce7](https://github.com/MariaDB/server/commit/ecb7ce7)\
  2016-08-03 15:55:48 +0400
  * [MDEV-10467](https://jira.mariadb.org/browse/MDEV-10467) Assertion \`nr >= 0.0' failed in Item\_sum\_std::val\_real() Backporting [MDEV-5781](https://jira.mariadb.org/browse/MDEV-5781) from 10.0.
* [Revision #35c9c85](https://github.com/MariaDB/server/commit/35c9c85)\
  2016-08-03 13:40:53 +0300
  * [MDEV-10217](https://jira.mariadb.org/browse/MDEV-10217): innodb.innodb\_bug59641 fails sporadically in buildbot: InnoDB: Failing assertion: current\_rec != insert\_rec in file page0cur.c line 1052
* [Revision #6b71a6d](https://github.com/MariaDB/server/commit/6b71a6d)\
  2016-08-02 18:52:51 +0200
  * [MDEV-10383](https://jira.mariadb.org/browse/MDEV-10383) Named pipes : multiple servers can listen on the same pipename
* [Revision #5fdb3cf](https://github.com/MariaDB/server/commit/5fdb3cf)\
  2016-07-29 18:21:08 +0200
  * [MDEV-10419](https://jira.mariadb.org/browse/MDEV-10419): crash in [mariadb 10.1.16](../../old-releases/10.1/10.1.16.md)-MariaDB-1trusty
* [Revision #c6aaa2a](https://github.com/MariaDB/server/commit/c6aaa2a)\
  2016-07-30 10:53:01 +0300
  * [MDEV-10228](https://jira.mariadb.org/browse/MDEV-10228): update test results
* [Revision #15ef38d](https://github.com/MariaDB/server/commit/15ef38d)\
  2016-07-27 00:38:51 +0300
  * [MDEV-10228](https://jira.mariadb.org/browse/MDEV-10228): Delete missing rows with OR conditions
* [Revision #1b5da2c](https://github.com/MariaDB/server/commit/1b5da2c)\
  2016-07-21 15:32:28 +0400
  * [MDEV-10316](https://jira.mariadb.org/browse/MDEV-10316) - main.type\_date fails around midnight sporadically
* [Revision #5cf49cd](https://github.com/MariaDB/server/commit/5cf49cd)\
  2016-07-15 23:51:30 +0300
  * [MDEV-10248](https://jira.mariadb.org/browse/MDEV-10248) Cannot Remove Test Tables
* [Revision #4e19aa3](https://github.com/MariaDB/server/commit/4e19aa3)\
  2016-07-12 12:13:31 +0200
  * [MDEV-10318](https://jira.mariadb.org/browse/MDEV-10318) unset params in --ps --embedded
* [Revision #97ded96](https://github.com/MariaDB/server/commit/97ded96)\
  2016-07-11 17:03:03 +0000
  * [MDEV-10318](https://jira.mariadb.org/browse/MDEV-10318) : Fix crash in embedded, in case prepared statement has parameter placeholders, but does not bind parameters
* [Revision #e81455bb](https://github.com/MariaDB/server/commit/e81455bb)\
  2015-05-04 08:32:05 +0200
  * [MDEV-7973](https://jira.mariadb.org/browse/MDEV-7973) bigint fail with gcc 5.0
* [Revision #a7814d4](https://github.com/MariaDB/server/commit/a7814d4)\
  2016-06-30 12:59:52 +0400
  * [MDEV-10311](https://jira.mariadb.org/browse/MDEV-10311) - funcs\_1.processlist\_priv\_no\_prot fails sporadically
* [Revision #79f852a](https://github.com/MariaDB/server/commit/79f852a)\
  2016-06-22 14:17:06 +0200
  * [MDEV-10050](https://jira.mariadb.org/browse/MDEV-10050): Crash in subselect
* [Revision #ef92aaf](https://github.com/MariaDB/server/commit/ef92aaf)\
  2016-06-22 22:37:28 +0300
  * [MDEV-10083](https://jira.mariadb.org/browse/MDEV-10083): Orphan ibd file when playing with foreign keys
* [Revision #a482e76](https://github.com/MariaDB/server/commit/a482e76)\
  2016-06-20 16:12:54 +0200
  * fix a mysql-5.5.50 merge: mysqlcheck
* [Revision #95bf696](https://github.com/MariaDB/server/commit/95bf696)\
  2016-06-19 14:51:03 +0200
  * [MDEV-9749](https://jira.mariadb.org/browse/MDEV-9749) InnoDB receives 'Bad file descriptor' error, possibly related to feedback plugin
* [Revision #7f38a07](https://github.com/MariaDB/server/commit/7f38a07)\
  2016-06-17 18:54:11 +0400
  * [MDEV-10043](https://jira.mariadb.org/browse/MDEV-10043) - main.events\_restart fails sporadically in buildbot (crashes upon shutdown)
* [Revision #128930c](https://github.com/MariaDB/server/commit/128930c)\
  2016-06-17 12:39:20 -0400
  * bump the VERSION
* [Revision #7ff86b4](https://github.com/MariaDB/server/commit/7ff86b4)\
  2016-06-17 14:59:17 +0300
  * [MDEV-10247](https://jira.mariadb.org/browse/MDEV-10247) TokuDB assertion error when building with DEBUG

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
