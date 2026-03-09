# MariaDB 10.0.27 Changelog

The most recent release in the [MariaDB 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md) series is:[**MariaDB 10.0.38**](../../old-releases/10.0/10.0.38.md) [Download Now](https://downloads.mariadb.org/mariadb/10.0.38)

[Download](https://downloads.mariadb.org/mariadb/10.0.27)[Release Notes](../../old-releases/10.0/10.0.27.md)[Changelog](mariadb-10027-changelog.md)[Overview of 10.0](../../old-releases/10.0/changes-improvements-in-mariadb-10-0.md)

**Release date:** 25 Aug 2016

For the highlights of this release, see the [release notes](../../old-releases/10.0/10.0.27.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.0) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #5bbe929](https://github.com/MariaDB/server/commit/5bbe929)\
  2016-08-24 17:39:57 +0300
  * [MDEV-10604](https://jira.mariadb.org/browse/MDEV-10604) Create a list of unstable MTR tests to be disabled in distribution builds
* [Revision #ed99e2c](https://github.com/MariaDB/server/commit/ed99e2c)\
  2016-08-18 14:00:40 +0300
  * [MDEV-10341](https://jira.mariadb.org/browse/MDEV-10341): InnoDB: Failing assertion: mutex\_own(mutex) - mutex\_exit\_func
* [Revision #4eb898b](https://github.com/MariaDB/server/commit/4eb898b)\
  2016-08-16 11:25:11 +0300
  * [MDEV-10563](https://jira.mariadb.org/browse/MDEV-10563) Crash during shutdown in Master\_info\_index::any\_slave\_sql\_running
* [Revision #4da2b83](https://github.com/MariaDB/server/commit/4da2b83)\
  2016-08-23 15:03:31 +0300
  * Fixed compiler error and some warnings on windows
* [Revision #a5051cd](https://github.com/MariaDB/server/commit/a5051cd)\
  2016-08-22 10:19:07 +0300
  * Minor cleanups - Remove impossible test in test\_quick\_select - Ensure that is\_fatal\_error is set if we run out of stack space
* [Revision #b511096](https://github.com/MariaDB/server/commit/b511096)\
  2016-08-22 10:16:00 +0300
  * [MDEV-10630](https://jira.mariadb.org/browse/MDEV-10630) rpl.rpl\_mdev6020 fails in buildbot with timeout
* [Revision #5932fa7](https://github.com/MariaDB/server/commit/5932fa7)\
  2016-08-21 20:38:47 +0300
  * Fixed "Packets out of order" warning message on stdout in clients, compiled for debugging, when the server goes down
* [Revision #6f31dd0](https://github.com/MariaDB/server/commit/6f31dd0)\
  2016-08-21 20:18:39 +0300
  * Added new status variables to make it easier to debug certain problems: - Handler\_read\_retry - Update\_scan - Delete\_scan
* [Revision #8d5a0d6](https://github.com/MariaDB/server/commit/8d5a0d6)\
  2016-08-21 20:14:13 +0300
  * Cleanups and minor fixes
    * Fixed typos
    * Added --core-on-failure to mysql-test-run
    * More DBUG\_PRINT in viosocket.c
    * Don't forget CLIENT\_REMEMBER\_OPTIONS for compressed slave protocol
    * Removed not used stage variables
* [Revision #05f61ba](https://github.com/MariaDB/server/commit/05f61ba)\
  2016-08-16 21:23:57 +0200
  * [MDEV-10559](https://jira.mariadb.org/browse/MDEV-10559): main.mysql\_client\_test\_nonblock crashes in buildbot on 10.0
* [Revision #df09d5e](https://github.com/MariaDB/server/commit/df09d5e)\
  2016-08-15 16:28:19 +0200
  * [MDEV-10559](https://jira.mariadb.org/browse/MDEV-10559): main.mysql\_client\_test\_nonblock crashes in buildbot on 10.0
* [Revision #47a1087](https://github.com/MariaDB/server/commit/47a1087) 2016-08-14 09:16:07 +0200 - Merge branch 'bb-10.0-serg' into 10.0
* [Revision #191f7b0](https://github.com/MariaDB/server/commit/191f7b0)\
  2016-08-10 21:15:51 +0200
  * after merge fixes
* [Revision #2bd9495](https://github.com/MariaDB/server/commit/2bd9495) 2016-08-10 19:58:42 +0200 - Merge branch 'connect/10.0' into 10.0
* [Revision #a2934d2](https://github.com/MariaDB/server/commit/a2934d2)\
  2016-08-10 18:27:31 +0200\
  \*
  * JdbcInterface: change return type of ...Field function modified: storage/connect/JdbcInterface.java
* [Revision #ec72508](https://github.com/MariaDB/server/commit/ec72508)\
  2016-07-15 00:50:18 +0200
  * Change jdbc test to reflect girls.txt LF ending
* [Revision #44012db](https://github.com/MariaDB/server/commit/44012db)\
  2016-07-14 20:12:22 +0200
  * All changes made on 10.1 for last 11 commits
* [Revision #077f29a](https://github.com/MariaDB/server/commit/077f29a) 2016-08-10 19:57:13 +0200 - Merge branch 'merge/merge-tokudb-5.6' into 10.0
* [Revision #4f2d214](https://github.com/MariaDB/server/commit/4f2d214)\
  2016-08-10 19:30:20 +0200
  * 5.6.31-77.0
* [Revision #3863e72](https://github.com/MariaDB/server/commit/3863e72) 2016-08-10 19:55:45 +0200 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #64752ac](https://github.com/MariaDB/server/commit/64752ac)\
  2016-08-10 19:24:58 +0200
  * 5.6.31-77.0
* [Revision #e672d3f](https://github.com/MariaDB/server/commit/e672d3f) 2016-08-10 19:44:28 +0200 - Merge branch 'merge/merge-perfschema-5.6' into 10.0
* [Revision #0d8bb01](https://github.com/MariaDB/server/commit/0d8bb01)\
  2016-08-10 19:26:54 +0200
  * 5.6.32
* [Revision #57fbc60](https://github.com/MariaDB/server/commit/57fbc60) 2016-08-10 19:43:37 +0200 - Merge branch 'merge/merge-innodb-5.6' into 10.0
* [Revision #b4f97a1](https://github.com/MariaDB/server/commit/b4f97a1)\
  2016-08-10 19:23:00 +0200
  * 5.6.32
* [Revision #309c08c](https://github.com/MariaDB/server/commit/309c08c) 2016-08-10 19:19:05 +0200 - Merge branch '5.5' into 10.0
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
* [Revision #72290cd](https://github.com/MariaDB/server/commit/72290cd) 2016-08-13 09:27:57 +0300 - Merge branch '10.0' of github.com:MariaDB/server into 10.0
* [Revision #98e36b2](https://github.com/MariaDB/server/commit/98e36b2)\
  2016-08-12 20:02:23 +0300
  * With parallel replication we have had a couple of bugs where DDL's (like DROP TABLE) has been scheduled before conflicting DDL's (like INSERT) are commited.
* [Revision #66ac894](https://github.com/MariaDB/server/commit/66ac894)\
  2016-08-11 17:50:21 +0200
  * [MDEV-10455](https://jira.mariadb.org/browse/MDEV-10455): libmariadbclient18 + MySQL-python leaks memory on failed connections
* [Revision #9b23f80](https://github.com/MariaDB/server/commit/9b23f80)\
  2016-08-11 14:39:47 +0300
  * [MDEV-10535](https://jira.mariadb.org/browse/MDEV-10535): ALTER TABLE causes standalone/wsrep cluster crash
* [Revision #b3df257](https://github.com/MariaDB/server/commit/b3df257)\
  2016-08-09 16:51:35 +0300
  * [MDEV-10469](https://jira.mariadb.org/browse/MDEV-10469): innodb.innodb-alter-tempfile fails in buildbot: InnoDB: Warning: database page corruption or a failed
* [Revision #b5fb2a6](https://github.com/MariaDB/server/commit/b5fb2a6)\
  2016-08-02 14:29:55 +0400
  * Fixed main.contributors failure
* [Revision #246866d](https://github.com/MariaDB/server/commit/246866d) 2016-08-02 10:32:48 +0400 - Merge pull request #207 from iangilfillan/10.0
* [Revision #5d0dfcb](https://github.com/MariaDB/server/commit/5d0dfcb)\
  2016-07-27 15:29:32 +0200
  * Update contributors
* [Revision #df4fddb](https://github.com/MariaDB/server/commit/df4fddb)\
  2016-07-25 01:57:00 +0300
  * [MDEV-10428](https://jira.mariadb.org/browse/MDEV-10428) main.information\_schema\_stats fails sporadically in buildbot
* [Revision #bf2e315](https://github.com/MariaDB/server/commit/bf2e315)\
  2016-07-18 11:50:08 +0400
  * [MDEV-8569](https://jira.mariadb.org/browse/MDEV-8569) build\_table\_filename() doesn't support temporary tables.
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
* [Revision #0fdb17e](https://github.com/MariaDB/server/commit/0fdb17e) 2016-06-28 11:25:59 +0200 - Merge branch '5.5' into 10.0
* [Revision #79f852a](https://github.com/MariaDB/server/commit/79f852a)\
  2016-06-22 14:17:06 +0200
  * [MDEV-10050](https://jira.mariadb.org/browse/MDEV-10050): Crash in subselect
* [Revision #ef92aaf](https://github.com/MariaDB/server/commit/ef92aaf)\
  2016-06-22 22:37:28 +0300
  * [MDEV-10083](https://jira.mariadb.org/browse/MDEV-10083): Orphan ibd file when playing with foreign keys
* [Revision #6dfe3fb](https://github.com/MariaDB/server/commit/6dfe3fb)\
  2016-06-28 10:23:24 +0200
  * remove incorrect .gitattributes
* [Revision #214f507](https://github.com/MariaDB/server/commit/214f507)\
  2016-06-24 11:08:09 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
