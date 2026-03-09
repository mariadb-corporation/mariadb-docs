# MariaDB 10.1.15 Changelog

**MariaDB-10.1.15 was never released,** [**MariaDB 10.1.16**](../../old-releases/10.1/10.1.16.md) **is the release that followed** [**MariaDB 10.1.14**](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-15-release-notes)**.**

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.15)[Release Notes](../../old-releases/10.1/10.1.15.md)[Changelog](mariadb-10115-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** _unreleased_

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.15.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #3fd214c](https://github.com/MariaDB/server/commit/3fd214c)\
  2016-06-29 16:50:53 -0400
  * [MDEV-9423](https://jira.mariadb.org/browse/MDEV-9423): cannot add new node to the cluser: Binlog..
* [Revision #33492ec](https://github.com/MariaDB/server/commit/33492ec)\
  2016-06-29 21:51:15 +0200
  * update tests for 32bit
* [Revision #f10b7db](https://github.com/MariaDB/server/commit/f10b7db)\
  2016-06-29 11:16:26 +0200
  * valgrind.supp: fix a typo
* [Revision #341e5f4](https://github.com/MariaDB/server/commit/341e5f4)\
  2016-06-28 15:38:41 +0200
  * [MDEV-10054](https://jira.mariadb.org/browse/MDEV-10054) Secure login fails when CIPHER is required
* [Revision #8354c0c](https://github.com/MariaDB/server/commit/8354c0c) 2016-06-28 22:13:59 +0200 - Merge remote-tracking branch 'refs/remotes/github/10.1' into 10.1
* [Revision #e786a57](https://github.com/MariaDB/server/commit/e786a57)\
  2016-06-28 17:20:19 +0300
  * Output more information when assertion `ut_a(state == BUF_BLOCK_NOT_USED || state == BUF_BLOCK_REMOVE_HASH);` is hit.
* [Revision #736f821](https://github.com/MariaDB/server/commit/736f821) 2016-06-28 22:12:50 +0200 - Merge branch 'connect/10.1' into 10.1
* [Revision #7e64b07](https://github.com/MariaDB/server/commit/7e64b07)\
  2016-06-20 16:37:57 +0200
  * Add column pattern and table type argument to catalog tables
* [Revision #7992dae](https://github.com/MariaDB/server/commit/7992dae) 2016-06-20 16:12:19 +0200 - Merge branch '10.1' of [server](https://github.com/MariaDB/server) into ob-10.1
* [Revision #7400953](https://github.com/MariaDB/server/commit/7400953)\
  2016-06-13 12:58:24 +0200
  * Possibly fix [MDEV-10179](https://jira.mariadb.org/browse/MDEV-10179) Reset remote tables when re-opening
* [Revision #613680a](https://github.com/MariaDB/server/commit/613680a)\
  2016-06-02 22:11:08 +0200
  * Fix [MDEV-10111](https://jira.mariadb.org/browse/MDEV-10111) Reconize unsigned integers when creating tables via srcdef
* [Revision #ead4147](https://github.com/MariaDB/server/commit/ead4147)\
  2016-05-26 18:48:47 +0200
  * Reconize the JDBC type -7 (BIT)
* [Revision #afa4657](https://github.com/MariaDB/server/commit/afa4657)\
  2016-05-24 23:57:06 +0200
  * Fix failing json\_udf\_bin test when --ps
* [Revision #8094228](https://github.com/MariaDB/server/commit/8094228)\
  2016-05-24 11:29:12 +0200
  * Alternative versions of the java JdbcInterface Some of them (ap/ds) enable connection to a DataSource
* [Revision #0dae293](https://github.com/MariaDB/server/commit/0dae293)\
  2016-05-23 15:08:51 +0200
  * New version of the java JdbcInterface
* [Revision #f8bc587](https://github.com/MariaDB/server/commit/f8bc587) 2016-05-22 14:49:14 +0200 - Merge branch '10.1' of [server](https://github.com/MariaDB/server) into ob-10.1
* [Revision #77dd5ec](https://github.com/MariaDB/server/commit/77dd5ec)\
  2016-05-21 14:28:21 +0200
  * Fix wrong return from ExecuteQuery
* [Revision #a982f59](https://github.com/MariaDB/server/commit/a982f59)\
  2016-05-21 11:56:59 +0200
  * JDBC using separate jmethodID for data types Some DEBUG tests
* [Revision #2f2797e](https://github.com/MariaDB/server/commit/2f2797e)\
  2016-05-20 00:18:29 +0200
  * JDBC tables can be connected via foreign server wrapper Redesign the handling of errors and exceptions
* [Revision #7972a45](https://github.com/MariaDB/server/commit/7972a45)\
  2016-05-12 17:22:45 +0200
  * Remove REQUIRED option that caused compilation to fail Remove JVM\_LIBRARY (is now dynamically loaded at run time)
* [Revision #0f5ced1](https://github.com/MariaDB/server/commit/0f5ced1)\
  2016-05-12 15:41:21 +0200
  * Fix some typo ... causing crash!
* [Revision #6aa163b](https://github.com/MariaDB/server/commit/6aa163b)\
  2016-05-12 12:20:52 +0200
  * Continue working on the JDBC table type Suppress the jpath option add the connect\_jvm\_path and connect\_class\_path global variables
* [Revision #2323cf0](https://github.com/MariaDB/server/commit/2323cf0)\
  2016-05-09 17:26:50 +0200
  * Make the JVM lib dynamically loaded This makes the CONNECT storage engine usable when Java JDK is not installed.
* [Revision #025decf](https://github.com/MariaDB/server/commit/025decf)\
  2016-05-06 01:07:14 +0200
  * Remove gcc compiling errors and warnings
* [Revision #80a204f](https://github.com/MariaDB/server/commit/80a204f)\
  2016-05-05 01:03:26 +0200
  * Try to fix [MDEV-9950](https://jira.mariadb.org/browse/MDEV-9950) (not tested yet)
* [Revision #bbdeb91](https://github.com/MariaDB/server/commit/bbdeb91)\
  2016-04-27 12:57:27 +0200
  * Add the JdbcInterface.java to the project
* [Revision #7b7414c](https://github.com/MariaDB/server/commit/7b7414c)\
  2016-04-27 12:36:55 +0200
  * Add the JDBC table type compilation for CMAKE.
* [Revision #62e0a45](https://github.com/MariaDB/server/commit/62e0a45) 2016-06-28 22:06:22 +0200 - Merge branch '10.0-galera' into 10.1
* [Revision #f629f53](https://github.com/MariaDB/server/commit/f629f53)\
  2016-06-27 14:44:07 -0400
  * Fix memory leak in XtraDB.
* [Revision #94a6183](https://github.com/MariaDB/server/commit/94a6183)\
  2016-06-26 21:15:36 -0400
  * Fix galera,wsrep tests.
* [Revision #fc799e3](https://github.com/MariaDB/server/commit/fc799e3)\
  2016-06-24 13:54:04 -0400
  * Fix build failure.
* [Revision #74dd07e](https://github.com/MariaDB/server/commit/74dd07e) 2016-06-24 12:02:41 -0400 - Merge branch '5.5-galera' into 10.0-galera
* [Revision #ecdb2b6](https://github.com/MariaDB/server/commit/ecdb2b6) 2016-06-23 12:54:38 -0400 - Merge tag 'mariadb-5.5.50' into 5.5-galera
* [Revision #14d6250](https://github.com/MariaDB/server/commit/14d6250) 2016-06-24 12:01:22 -0400 - Merge tag 'mariadb-10.0.26' into 10.0-galera
* [Revision #868c2ce](https://github.com/MariaDB/server/commit/868c2ce)\
  2016-06-12 19:28:56 -0400
  * [MDEV-9083](https://jira.mariadb.org/browse/MDEV-9083): Slave IO thread does not handle autoreconnect to restarting Galera Cluster node
* [Revision #3361aee](https://github.com/MariaDB/server/commit/3361aee) 2016-06-28 22:01:55 +0200 - Merge branch '10.0' into 10.1
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
* [Revision #6ce20fb](https://github.com/MariaDB/server/commit/6ce20fb)\
  2016-06-28 10:10:49 +0200
  * [MDEV-9428](https://jira.mariadb.org/browse/MDEV-9428) NO\_AUTO\_VALUE\_ON\_ZERO is ignored when a trigger before insert is defined
* [Revision #9c38308](https://github.com/MariaDB/server/commit/9c38308)\
  2016-06-28 10:04:34 +0200
  * [MDEV-10086](https://jira.mariadb.org/browse/MDEV-10086) no gssapi-server RPM package anymore in 10.1
* [Revision #414a417](https://github.com/MariaDB/server/commit/414a417)\
  2016-06-28 09:29:23 +0200
  * [MDEV-10032](https://jira.mariadb.org/browse/MDEV-10032) Connect engine not installable on Xenial
* [Revision #56a3496](https://github.com/MariaDB/server/commit/56a3496)\
  2016-06-28 13:11:04 +0400
  * [MDEV-10236](https://jira.mariadb.org/browse/MDEV-10236) Where expression with NOT function gives incorrect result
* [Revision #64c115b](https://github.com/MariaDB/server/commit/64c115b)\
  2016-06-14 21:50:46 +0200
  * Use hostname instead of IP in donor's socat
* [Revision #7ff44b1](https://github.com/MariaDB/server/commit/7ff44b1)\
  2016-06-27 18:30:07 -0400
  * [MDEV-10161](https://jira.mariadb.org/browse/MDEV-10161): wsrep\_sync\_wait not enabled when set to 1 in config file
* [Revision #aa9c8f2](https://github.com/MariaDB/server/commit/aa9c8f2)\
  2016-06-27 18:24:07 -0400
  * [MDEV-10233](https://jira.mariadb.org/browse/MDEV-10233): Support bootstraping a Galera cluster with mysqld\_multi
* [Revision #7ef5257](https://github.com/MariaDB/server/commit/7ef5257)\
  2016-06-27 18:22:35 -0400
  * [MDEV-10230](https://jira.mariadb.org/browse/MDEV-10230): --wsrep\_on option no longer passed through by mysqld\_safe
* [Revision #90f222e](https://github.com/MariaDB/server/commit/90f222e)\
  2016-06-27 18:21:00 -0400
  * [MDEV-10235](https://jira.mariadb.org/browse/MDEV-10235): Deadlock in CREATE TABLE .. AS SELECT .. if result set is empty in Galera
* [Revision #ad3584b](https://github.com/MariaDB/server/commit/ad3584b)\
  2016-06-27 18:17:03 -0400
  * Test cleanup: Remove unnecessary global suppressions
* [Revision #48a0a66](https://github.com/MariaDB/server/commit/48a0a66)\
  2016-06-27 18:15:47 -0400
  * [MDEV-10186](https://jira.mariadb.org/browse/MDEV-10186): mysqld crash when runtime setting wsrep\_cluster\_address without wsrep\_on=ON
* [Revision #7f9fcfe](https://github.com/MariaDB/server/commit/7f9fcfe)\
  2016-06-27 18:07:43 -0400
  * Code cleanup (wsrep patch).
* [Revision #47e4e5d](https://github.com/MariaDB/server/commit/47e4e5d)\
  2016-06-27 18:06:18 -0400
  * [MDEV-6699](https://jira.mariadb.org/browse/MDEV-6699): wsrep\_node\_name not automatically set to hostname
* [Revision #a681699](https://github.com/MariaDB/server/commit/a681699)\
  2016-06-27 18:03:24 -0400
  * [MDEV-10004](https://jira.mariadb.org/browse/MDEV-10004): Galera's pc.recovery process fails in 10.1 with systemd
* [Revision #0645699](https://github.com/MariaDB/server/commit/0645699)\
  2016-06-27 18:01:21 -0400
  * [MDEV-10145](https://jira.mariadb.org/browse/MDEV-10145): Systemd fails to start mysqld in multi-instance mode
* [Revision #2768829](https://github.com/MariaDB/server/commit/2768829)\
  2016-06-27 17:59:12 -0400
  * [MDEV-10056](https://jira.mariadb.org/browse/MDEV-10056): SST method mysqldump is broken
* [Revision #b57232d](https://github.com/MariaDB/server/commit/b57232d)\
  2016-06-27 17:56:59 -0400
  * [MDEV-6699](https://jira.mariadb.org/browse/MDEV-6699) : wsrep\_node\_name not automatically set to hostname
* [Revision #e337fd1](https://github.com/MariaDB/server/commit/e337fd1)\
  2016-06-27 22:12:21 +0400
  * [MDEV-10119](https://jira.mariadb.org/browse/MDEV-10119) mysql\_install\_db creates GIS procedures with invalid definer.
* [Revision #09d902d](https://github.com/MariaDB/server/commit/09d902d)\
  2016-06-27 18:02:28 +0400
  * [MDEV-9618](https://jira.mariadb.org/browse/MDEV-9618) solaris sparc build fails on 10.1.
* [Revision #652e799](https://github.com/MariaDB/server/commit/652e799)\
  2016-06-27 15:14:07 +0400
  * [MDEV-8502](https://jira.mariadb.org/browse/MDEV-8502) DECIMAL accepts out of range DEFAULT values [MDEV-10277](https://jira.mariadb.org/browse/MDEV-10277) Redundant NOTE when inserting '0.00001 ' into a DECIMAL(2,1) column
* [Revision #305bbbc](https://github.com/MariaDB/server/commit/305bbbc) 2016-06-24 18:08:13 +0400 - Merge pull request #183 from mweigel/10.1-[MDEV-10214](https://jira.mariadb.org/browse/MDEV-10214)
* [Revision #626a62e](https://github.com/MariaDB/server/commit/626a62e)\
  2016-06-12 23:13:26 +1200
  * [MDEV-10214](https://jira.mariadb.org/browse/MDEV-10214): Fix segfault when using groups in PAM user mapping plugin
* [Revision #6f66920](https://github.com/MariaDB/server/commit/6f66920)\
  2016-06-23 21:57:15 +0400
  * Recording innodb\_ctype\_ldml.result forgotten in the patch for: [MDEV-8686](https://jira.mariadb.org/browse/MDEV-8686) A user defined collation utf8\_confusables doesn't work 25e68c5e46ced7e626853cdf5491c2b5430fd51b
* [Revision #25e68c5](https://github.com/MariaDB/server/commit/25e68c5)\
  2016-06-23 14:25:48 +0400
  * [MDEV-8686](https://jira.mariadb.org/browse/MDEV-8686) A user defined collation utf8\_confusables doesn't work The collation customization code for the UCA (Unicode Collation Alrorithm) based collations now allows to reset to and shift of characters with implicit weights. Previously reset/shift worked only for the characters with explicit DUCET weights. An attempt to use reset/shift with character with implicit weights made the server crash.
* [Revision #3e03b89](https://github.com/MariaDB/server/commit/3e03b89)\
  2016-06-22 23:20:41 +0300
  * [MDEV-10185](https://jira.mariadb.org/browse/MDEV-10185): Assertion \`\`tree1->keys\[key\_no] && tree2->keys\[key\_no]'\` failed in
* [Revision #6312009](https://github.com/MariaDB/server/commit/6312009)\
  2016-06-21 21:36:23 +0400
  * [MDEV-10262](https://jira.mariadb.org/browse/MDEV-10262) ucs2\_thai\_520\_w2: wrong implicit weights on the secondary level
* [Revision #61492ea](https://github.com/MariaDB/server/commit/61492ea)\
  2016-06-19 15:03:13 +0300
  * Reset user status after unix\_socket.test Fixed mysql-test-run failures for roles.acl\_statistics
* [Revision #94b47bc](https://github.com/MariaDB/server/commit/94b47bc) 2016-06-08 15:16:39 +0200 - Merge branch 'mdev9991' into mdev9991-10.1
* [Revision #9ff9365](https://github.com/MariaDB/server/commit/9ff9365)\
  2016-06-03 19:22:47 +0000
  * Fix sporadic failure of set\_statement mtr test.
* [Revision #1859caf](https://github.com/MariaDB/server/commit/1859caf)\
  2016-06-03 14:43:08 +0300
  * [MDEV-10175](https://jira.mariadb.org/browse/MDEV-10175): range optimizer calls records\_in\_range() for full extended keys
* [Revision #825427f](https://github.com/MariaDB/server/commit/825427f)\
  2016-06-03 10:58:32 +0300
  * Update test results
* [Revision #904027c](https://github.com/MariaDB/server/commit/904027c) 2016-06-02 19:27:22 +0300 - Merge branch 'bb-10.1-mdev8989' into 10.1
* [Revision #b3fc7c7](https://github.com/MariaDB/server/commit/b3fc7c7)\
  2016-06-02 17:31:56 +0300
  * Update test results part #3.
* [Revision #685c63b](https://github.com/MariaDB/server/commit/685c63b)\
  2016-06-02 15:19:52 +0300
  * Update test results part#2.
* [Revision #3fd2521](https://github.com/MariaDB/server/commit/3fd2521)\
  2016-06-02 13:35:21 +0300
  * Update test results
* [Revision #5a5a54f](https://github.com/MariaDB/server/commit/5a5a54f)\
  2016-06-01 23:43:11 +0300
  * [MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989): ORDER BY optimizer ignores equality propagation
* [Revision #a85f653](https://github.com/MariaDB/server/commit/a85f653)\
  2016-05-27 15:16:08 +0300
  * [MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989): ORDER BY optimizer ignores equality propagation
* [Revision #99cd5a9](https://github.com/MariaDB/server/commit/99cd5a9)\
  2016-05-23 21:15:01 +0300
  * [MDEV-8989](https://jira.mariadb.org/browse/MDEV-8989): ORDER BY optimizer ignores equality propagation
* [Revision #7d3d758](https://github.com/MariaDB/server/commit/7d3d758)\
  2016-06-02 19:00:26 +0300
  * [MDEV-9764](https://jira.mariadb.org/browse/MDEV-9764): MariaDB does not limit memory used for range optimization
* [Revision #66dd9fa](https://github.com/MariaDB/server/commit/66dd9fa) 2016-06-02 11:46:35 +0300 - Merge pull request #174 from Cona19/10.1
* [Revision #389c51f](https://github.com/MariaDB/server/commit/389c51f)\
  2016-05-26 10:33:17 +0000
  * Remove some unnecessary parentheses
* [Revision #e0e3747](https://github.com/MariaDB/server/commit/e0e3747)\
  2016-06-01 13:06:14 +0300
  * [MDEV-9865](https://jira.mariadb.org/browse/MDEV-9865): Test encryption.innodb-log-encrypt-crash takes too long on debug build
* [Revision #743814f](https://github.com/MariaDB/server/commit/743814f) 2016-06-01 09:23:29 +0300 - Merge pull request #177 from Cona19/10.1-spelling-check
* [Revision #500b03fe](https://github.com/MariaDB/server/commit/500b03fe)\
  2016-06-01 06:09:13 +0000
  * Fix spelling: shhould -> should
* [Revision #0167904](https://github.com/MariaDB/server/commit/0167904)\
  2016-05-31 17:59:04 +0300
  * [MDEV-9764](https://jira.mariadb.org/browse/MDEV-9764): MariaDB does not limit memory used for range optimization
* [Revision #bc54622](https://github.com/MariaDB/server/commit/bc54622)\
  2016-05-30 16:56:29 +0400
  * Adding collations utf8mb4\_thai\_520\_w2, ucs2\_thai\_520\_w2, utf16\_thai\_520\_w2, utf32\_thai\_520\_w2
* [Revision #c5733e5](https://github.com/MariaDB/server/commit/c5733e5)\
  2016-05-30 14:27:24 +0400
  * Moving ctype\_utf8\_th.test to ctype\_thai.inc and including it from ctype\_uca.test. This is to reuse ctype\_thai.inc for other Unicode character sets later - Removing separate ctype\_uca.result
* [Revision #dd7f307](https://github.com/MariaDB/server/commit/dd7f307)\
  2016-05-30 13:47:57 +0400
  * Moving tests from t/ctype\_uca\_th.test to include/ctype\_uca\_w2.inc and including it from t/ctype\_uca.test - Deleting r/ctype\_uca\_th.result
* [Revision #a8cd030](https://github.com/MariaDB/server/commit/a8cd030)\
  2016-05-30 13:07:43 +0400
  * Adding LIKE range tests for tricky characters U+0425, U+045F, U+2525, U+5F5F. They have bytes 0x25 and 0x5F. Testing that these bytes are treated as parts of multi-byte characters rather than underscore and percent sign.
* [Revision #683b88e](https://github.com/MariaDB/server/commit/683b88e)\
  2016-05-28 11:46:46 +0200
  * Mark gssapi plugin as stable. No open bug reports, and no further work planned, thus stable is accurate
* [Revision #29db3b5](https://github.com/MariaDB/server/commit/29db3b5)\
  2016-05-26 22:56:28 +0400
  * Clean-ups for [MDEV-10132](https://jira.mariadb.org/browse/MDEV-10132) utf8\_thai\_520\_w2 collation: - Changing strnxfrm\_multiply from 8 to 4, as agreed with Pruet Boonma - Adjusting tests
* [Revision #d930d07](https://github.com/MariaDB/server/commit/d930d07) 2016-05-26 21:09:55 +0400 - Merge branch 'pruet-utf8thai-10.1' into 10.1
* [Revision #fb35b9a](https://github.com/MariaDB/server/commit/fb35b9a)\
  2016-05-26 16:45:50 +0700
  * Multi-level collation in UCA, Thai sorting with contraction for UTF8.
* [Revision #9c9747f](https://github.com/MariaDB/server/commit/9c9747f)\
  2016-05-18 12:35:38 +0400
  * Updating uca-dump.c to be able to dump weights outside of BMP.
* [Revision #9eaf934](https://github.com/MariaDB/server/commit/9eaf934)\
  2016-05-17 14:01:16 +0300
  * Update test result after the last commit
* [Revision #5c68bc2](https://github.com/MariaDB/server/commit/5c68bc2)\
  2016-05-06 12:30:01 +0300
  * [MDEV-10006](https://jira.mariadb.org/browse/MDEV-10006): optimizer doesn't convert outer join to inner on views with WHERE clause
* [Revision #4388cb4](https://github.com/MariaDB/server/commit/4388cb4)\
  2016-05-10 09:28:00 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
