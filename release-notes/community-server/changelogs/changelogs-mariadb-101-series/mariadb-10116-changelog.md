# MariaDB 10.1.16 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.16)[Release Notes](../../old-releases/10.1/10.1.16.md)[Changelog](mariadb-10116-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 18 Jul 2016

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.16.md).

This changelog only details pushes made between 10.1.15 and 10.1.16. For changes made between 10.1.14 and 10.1.15, see the unreleased [MariaDB 10.1.15 Changelog](mariadb-10115-changelog.md)

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #1168c1a](https://github.com/MariaDB/server/commit/1168c1a)\
  2016-07-14 03:55:33 +0300
  * Fix embedded and 32-bit test results after [MDEV-8580](https://jira.mariadb.org/browse/MDEV-8580)
* [Revision #12ac3ee](https://github.com/MariaDB/server/commit/12ac3ee)\
  2016-07-13 14:47:58 +0300
  * Update test results: make innodb\_ext\_key test stable
* [Revision #bebabd6](https://github.com/MariaDB/server/commit/bebabd6) 2016-07-13 12:10:07 +0200 - Merge branch '10.0-galera' into 10.1
* [Revision #10880d6](https://github.com/MariaDB/server/commit/10880d6)\
  2016-06-30 10:24:54 -0400
  * Postfix: memory leak in XtraDB
* [Revision #326a8dc](https://github.com/MariaDB/server/commit/326a8dc) 2016-07-13 12:09:59 +0200 - Merge branch '10.0' into 10.1
* [Revision #c6fdb92](https://github.com/MariaDB/server/commit/c6fdb92) 2016-07-12 22:20:46 +0200 - Merge branch '5.5' into 10.0
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
* [Revision #f12ebed](https://github.com/MariaDB/server/commit/f12ebed)\
  2016-07-08 15:44:47 +0200
  * fixes for tokudb\_parts --big suite
* [Revision #865ae5d](https://github.com/MariaDB/server/commit/865ae5d)\
  2016-07-01 18:44:28 -0400
  * [MDEV-10261](https://jira.mariadb.org/browse/MDEV-10261) fix some tokudb partition test result files since the underlying tests have changed.
* [Revision #79fc519](https://github.com/MariaDB/server/commit/79fc519)\
  2016-07-12 22:20:20 +0200
  * json\_udf slowdown
* [Revision #ef125e2](https://github.com/MariaDB/server/commit/ef125e2)\
  2016-06-23 14:41:51 +0200
  * add a test case vcol.charsets
* [Revision #3e8ae6e](https://github.com/MariaDB/server/commit/3e8ae6e)\
  2016-07-12 12:36:11 +0200
  * [MDEV-10211](https://jira.mariadb.org/browse/MDEV-10211) postfix - in ssl.test, remove remaining SHOW STATUS LIKE 'Ssl\_cipher'
* [Revision #31e763d](https://github.com/MariaDB/server/commit/31e763d)\
  2016-07-11 21:29:18 +0200
  * [MDEV-10211](https://jira.mariadb.org/browse/MDEV-10211) : fix ssl test not to use specific value of ssl\_cipher, as it can change between different openssl/yassl version
* [Revision #7d4a7d8](https://github.com/MariaDB/server/commit/7d4a7d8)\
  2016-05-30 22:33:34 +0300
  * \[[MDEV-9127](https://jira.mariadb.org/browse/MDEV-9127)] Crash reporter often fails to show the query that crashed
* [Revision #406fe77](https://github.com/MariaDB/server/commit/406fe77)\
  2016-07-04 17:31:14 +0300
  * Add more diagnostic to find out the problem on innodb\_shutdown\_for\_mysql in ppc64el on test case innodb\_fts.innodb\_fts\_stopword\_charset.
* [Revision #6458362](https://github.com/MariaDB/server/commit/6458362)\
  2016-07-12 16:36:43 +0200
  * [MDEV-9588](https://jira.mariadb.org/browse/MDEV-9588) Mariadb client-only build creates a useless mysqld\_safe file
* [Revision #12dc083](https://github.com/MariaDB/server/commit/12dc083)\
  2016-07-12 13:41:29 +0200
  * [MDEV-8580](https://jira.mariadb.org/browse/MDEV-8580) For some BOOLEAN or ENUM sysvars list of valid values is not generated
* [Revision #0d5583b](https://github.com/MariaDB/server/commit/0d5583b)\
  2016-07-13 08:55:20 +0200
  * cleanup
* [Revision #c5d7318](https://github.com/MariaDB/server/commit/c5d7318)\
  2016-07-12 13:02:26 +0200
  * [MDEV-8227](https://jira.mariadb.org/browse/MDEV-8227) simple\_password\_check\_minimal\_length gets adjusted without a warning
* [Revision #4b88cf3](https://github.com/MariaDB/server/commit/4b88cf3)\
  2016-06-29 13:27:51 -0400
  * fix sql-bench test-table-elimination view leak. see [MDEV-10310](https://jira.mariadb.org/browse/MDEV-10310) for details
* [Revision #98b1bb0](https://github.com/MariaDB/server/commit/98b1bb0)\
  2016-06-25 16:44:48 -0400
  * fix [MDEV-7225](https://jira.mariadb.org/browse/MDEV-7225).
* [Revision #8a8ba19](https://github.com/MariaDB/server/commit/8a8ba19)\
  2016-07-11 22:22:32 +0300
  * [MDEV-10360](https://jira.mariadb.org/browse/MDEV-10360): Extended keys: index properties depend on index order
* [Revision #0bb5d95](https://github.com/MariaDB/server/commit/0bb5d95)\
  2016-07-11 22:01:24 +0300
  * [MDEV-10325](https://jira.mariadb.org/browse/MDEV-10325): Queries examines all rows of a tables when it should not
* [Revision #53e7fcc](https://github.com/MariaDB/server/commit/53e7fcc)\
  2016-06-28 11:23:12 -0400
  * [MDEV-10298](https://jira.mariadb.org/browse/MDEV-10298): Systemd hardening
* [Revision #f280a87](https://github.com/MariaDB/server/commit/f280a87)\
  2016-07-11 17:03:03 +0000
  * [MDEV-10318](https://jira.mariadb.org/browse/MDEV-10318) : Fix crash in embedded, in case prepared statement has parameter placeholders, but does not bind parameters
* [Revision #ae511cb](https://github.com/MariaDB/server/commit/ae511cb)\
  2016-06-28 14:53:17 +0400
  * [MDEV-9363](https://jira.mariadb.org/browse/MDEV-9363) - Mroonga tests with datetime field fail on Solaris in buildbot
* [Revision #ecb27d2](https://github.com/MariaDB/server/commit/ecb27d2)\
  2016-06-27 15:01:22 +0400
  * [MDEV-10010](https://jira.mariadb.org/browse/MDEV-10010) - Recursive call to mysql\_rwlock\_rdlock for LOCK\_system\_variables\_hash
* [Revision #95c286c](https://github.com/MariaDB/server/commit/95c286c)\
  2016-07-05 16:53:03 +0300
  * [MDEV-10324](https://jira.mariadb.org/browse/MDEV-10324): Server crash in get\_sel\_arg\_for\_keypart or Assertion
* [Revision #d1b2589](https://github.com/MariaDB/server/commit/d1b2589)\
  2016-07-05 15:23:22 +0400
  * Removing class Item\_func\_integer. It's not used since MySQL-5.0.
* [Revision #1ec9180](https://github.com/MariaDB/server/commit/1ec9180)\
  2016-07-03 13:52:06 +0400
  * [MDEV-10317](https://jira.mariadb.org/browse/MDEV-10317) EXCTACT(MINUTE\_MICROSECOND) truncates data
* [Revision #3ccf821](https://github.com/MariaDB/server/commit/3ccf821)\
  2016-07-03 11:20:46 +0400
  * Partial backporting of 7b50447aa6d051b8d14bb01ef14802cb8ffee223 ([MDEV-9407](https://jira.mariadb.org/browse/MDEV-9407), [MDEV-9408](https://jira.mariadb.org/browse/MDEV-9408)) from 10.1
* [Revision #f832b47](https://github.com/MariaDB/server/commit/f832b47)\
  2016-07-03 10:41:16 +0400
  * Removing the "thd" argument from Item::create\_field\_for\_create\_select().
* [Revision #ccdd633](https://github.com/MariaDB/server/commit/ccdd633)\
  2016-07-01 11:30:38 -0400
  * bump the VERSION
* [Revision #6a7c73e](https://github.com/MariaDB/server/commit/6a7c73e) 2016-07-01 10:24:25 +0300 - Merge pull request #198 from grooverdan/10.1-cross-compile
* [Revision #37b08ef](https://github.com/MariaDB/server/commit/37b08ef)\
  2016-07-01 17:10:46 +1000
  * Cross Compile HAVE\_FALLOC\_PUNCH\_HOLE\_AND\_KEEP\_SIZE change to compile check

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
