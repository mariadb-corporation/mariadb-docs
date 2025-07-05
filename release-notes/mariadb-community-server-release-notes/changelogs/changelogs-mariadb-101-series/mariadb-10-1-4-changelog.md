# MariaDB 10.1.4 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.4)[Release Notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md)[Changelog](mariadb-10-1-4-changelog.md)[Overview of 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)

**Release date:** 13 Apr 2015

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-4-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #d8a4a83](https://github.com/MariaDB/server/commit/d8a4a83)\
  2015-04-12 10:48:20 +0200
  * Merge branch 'bb-10.1-explain-analyze' into 10.1
* [Revision #7ac2f1f](https://github.com/MariaDB/server/commit/7ac2f1f)\
  2015-04-12 10:30:10 +0200
  * Update test results after previous pushes
* [Revision #2bbf3b8](https://github.com/MariaDB/server/commit/2bbf3b8)\
  2015-04-12 06:07:58 +0200
  * [MDEV-7836](https://jira.mariadb.org/browse/MDEV-7836): ANALYZE FORMAT=JSON should provide info about GROUP/ORDER BY
* [Revision #cc8da9b](https://github.com/MariaDB/server/commit/cc8da9b)\
  2015-04-12 05:34:30 +0200
  * Merge ../10.1-explain-analyze into bb-10.1-explain-analyze
* [Revision #a445b83](https://github.com/MariaDB/server/commit/a445b83)\
  2015-04-12 05:16:48 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #771dec3](https://github.com/MariaDB/server/commit/771dec3)\
  2015-04-12 05:07:39 +0300
  * Merge branch '10.1' into bb-10.1-explain-analyze
* [Revision #0719df7](https://github.com/MariaDB/server/commit/0719df7)\
  2015-04-12 04:59:34 +0300
  * Merge
* [Revision #4938b82](https://github.com/MariaDB/server/commit/4938b82)\
  2015-04-12 04:48:42 +0300
  * [MDEV-7836](https://jira.mariadb.org/browse/MDEV-7836): ANALYZE FORMAT=JSON should provide info about GROUP/ORDER BY
* [Revision #d214c83](https://github.com/MariaDB/server/commit/d214c83)\
  2015-04-11 10:22:26 +0200
  * mtr: make search\_pattern\_in\_file.inc more verbose
* [Revision #4e15146](https://github.com/MariaDB/server/commit/4e15146)\
  2015-04-11 10:13:49 +0200
  * update tokudb test results after dd8f93195
* [Revision #4a7472b](https://github.com/MariaDB/server/commit/4a7472b)\
  2015-04-11 00:28:42 +0200
  * fix a crash in innodb.innodb-wl5522-zip,xtradb
* [Revision #a73676b](https://github.com/MariaDB/server/commit/a73676b)\
  2015-04-10 19:32:14 +0200
  * Merge branch '10.1' into bb-10.1-serg
* [Revision #24341cb](https://github.com/MariaDB/server/commit/24341cb)\
  2015-04-10 18:01:53 +0200
  * add encryption plugins to deb packages
* [Revision #135f203](https://github.com/MariaDB/server/commit/135f203)\
  2015-04-10 17:04:44 +0400
  * A cleanup for the contributed patch for [MDEV-7816](https://jira.mariadb.org/browse/MDEV-7816) ALTER with DROP INDEX and ADD INDEX .. COMMENT='comment2' ignores the new comment
* [Revision #d2ed256](https://github.com/MariaDB/server/commit/d2ed256)\
  2015-04-10 14:24:58 +0200
  * move debug\_ and example\_key\_management plugins to test component
* [Revision #899c5c3](https://github.com/MariaDB/server/commit/899c5c3)\
  2015-04-10 13:39:29 +0200
  * smarter MY\_CHECK\_AND\_SET\_COMPILER\_FLAG
* [Revision #87b46dc](https://github.com/MariaDB/server/commit/87b46dc)\
  2015-04-10 13:30:12 +0200
  * disable scrubbing tests on windows
* [Revision #23e90e9](https://github.com/MariaDB/server/commit/23e90e9)\
  2015-04-10 15:17:44 +0400
  * Merge branch '[MDEV-7816](https://jira.mariadb.org/browse/MDEV-7816)' of git:github.com/f4rnham/server into 10.1
* [Revision #7d49e69](https://github.com/MariaDB/server/commit/7d49e69)\
  2015-04-10 09:46:21 +0200
  * fix "use mutex before initialization" bug in example\_km plugin
* [Revision #966b236](https://github.com/MariaDB/server/commit/966b236)\
  2015-04-09 21:04:05 +0200
  * add support for --innodb-encrypt-tables=FORCE
* [Revision #da06baa](https://github.com/MariaDB/server/commit/da06baa)\
  2015-04-09 20:44:56 +0200
  * mtr: \*.opt files, always enable innodb-encrypt-log
* [Revision #dab6c83](https://github.com/MariaDB/server/commit/dab6c83)\
  2015-04-09 18:30:05 +0200
  * allow srv\_encrypt\_tables and ENCRYPTED=YES to be used together
* [Revision #bc9f118](https://github.com/MariaDB/server/commit/bc9f118)\
  2015-04-09 17:59:34 +0200
  * rename table attribute ENCRYPTION=ON/OFF to ENCRYPTED=YES/NO
* [Revision #ea764f5](https://github.com/MariaDB/server/commit/ea764f5)\
  2015-04-09 14:09:06 +0200
  * s/innodb\_default\_encryption\_key/innodb\_default\_encryption\_key\_id/
* [Revision #92ff523](https://github.com/MariaDB/server/commit/92ff523)\
  2015-04-10 02:39:36 +0200
  * change ENCRYPTION\_KEY\_ID to be HA\_TOPTION\_SYSVAR
* [Revision #dd8f931](https://github.com/MariaDB/server/commit/dd8f931)\
  2015-04-10 02:36:54 +0200
  * be less annoying about sysvar-based table attributes
* [Revision #eb29a63](https://github.com/MariaDB/server/commit/eb29a63)\
  2015-04-09 11:14:57 +0200
  * SET STATEMENT timestamp=xxx ....
* [Revision #0a9052f](https://github.com/MariaDB/server/commit/0a9052f)\
  2015-04-09 00:37:54 +0200
  * Store the key id in the tablespace and read it back
* [Revision #97d5de4](https://github.com/MariaDB/server/commit/97d5de4)\
  2015-04-09 00:37:47 +0200
  * Add encryption key id to the API as a distinct concept
* [Revision #5dffda3](https://github.com/MariaDB/server/commit/5dffda3)\
  2015-04-09 19:27:40 +0200
  * Merge branch 'bb-10.1-jan-encryption' into bb-10.1-serg
* [Revision #129e960](https://github.com/MariaDB/server/commit/129e960)\
  2015-04-09 19:06:11 +0200
  * fix log\_blocks\_crypt() to actually decrypt the encrypted log
* [Revision #d6b912c](https://github.com/MariaDB/server/commit/d6b912c)\
  2015-04-09 00:26:37 +0200
  * update XtraDB/InnoDB plugin maturity to match the server
* [Revision #3a2ec3f](https://github.com/MariaDB/server/commit/3a2ec3f)\
  2015-04-08 22:07:37 +0200
  * make innodb\_encryption\_debug test more robust
* [Revision #f130da7](https://github.com/MariaDB/server/commit/f130da7)\
  2015-04-05 17:37:06 +0200
  * clarify/simplify new innodb sysvars: help texts
* [Revision #87cf865](https://github.com/MariaDB/server/commit/87cf865)\
  2015-04-05 17:33:32 +0200
  * clarify/simplify new innodb sysvars: innodb-scrub-force-testing
* [Revision #19e7681](https://github.com/MariaDB/server/commit/19e7681)\
  2015-04-05 17:29:43 +0200
  * clarify/simplify new innodb sysvars: innodb-scrub-log-interval
* [Revision #72c8b3fcb](https://github.com/MariaDB/server/commit/72c8b3fcb)\
  2015-04-05 13:16:59 +0200
  * small cleanups as per review
* [Revision #4d40a7d](https://github.com/MariaDB/server/commit/4d40a7d)\
  2015-04-01 22:15:11 +0200
  * remove now-empty my\_aes.{h,cc}
* [Revision #65e7826](https://github.com/MariaDB/server/commit/65e7826)\
  2015-04-01 21:25:02 +0200
  * renames to follow single consistent naming style
* [Revision #c0878f6](https://github.com/MariaDB/server/commit/c0878f6)\
  2015-04-01 18:26:19 +0200
  * remove wrappers in encryption\_keys.cc
* [Revision #bb1b61b](https://github.com/MariaDB/server/commit/bb1b61b)\
  2015-03-31 19:32:35 +0200
  * encryption plugin controls the encryption
* [Revision #9ccafff](https://github.com/MariaDB/server/commit/9ccafff)\
  2015-03-27 09:45:22 +0100
  * rename "encryption key management plugin" to "encryption plugin"
* [Revision #6d3dace](https://github.com/MariaDB/server/commit/6d3dace)\
  2015-04-08 10:57:32 +0200
  * mtr: don't disable tests in suite.pm unnecessary
* [Revision #37e87b5](https://github.com/MariaDB/server/commit/37e87b5)\
  2015-04-09 16:47:04 +0300
  * [MDEV-6382](https://jira.mariadb.org/browse/MDEV-6382): ANALYZE $stmt and security
* [Revision #b05383c](https://github.com/MariaDB/server/commit/b05383c)\
  2015-04-08 20:14:48 +0200
  * [MDEV-7835](https://jira.mariadb.org/browse/MDEV-7835): ANALYZE FORMAT=JSON should show buffer sizes
* [Revision #6971944](https://github.com/MariaDB/server/commit/6971944)\
  2015-04-08 10:13:36 +0200
  * [MDEV-7856](https://jira.mariadb.org/browse/MDEV-7856): EXPLAIN FORMAT=JSON should show partitions
* [Revision #abba418](https://github.com/MariaDB/server/commit/abba418)\
  2015-04-09 10:05:27 +0200
  * Merge [MDEV-7940](https://jira.mariadb.org/browse/MDEV-7940) into 10.1
* [Revision #15a2b5a](https://github.com/MariaDB/server/commit/15a2b5a)\
  2015-04-09 10:02:16 +0200
  * [MDEV-7940](https://jira.mariadb.org/browse/MDEV-7940): Sporadic failure in rpl.rpl\_gtid\_until
* [Revision #66ff163](https://github.com/MariaDB/server/commit/66ff163)\
  2015-04-08 16:25:01 +0300
  * [MDEV-7860](https://jira.mariadb.org/browse/MDEV-7860): EXPLAIN FORMAT=JSON crashes for loose scan query
* [Revision #82b9eb5](https://github.com/MariaDB/server/commit/82b9eb5)\
  2015-04-08 15:11:44 +0200
  * Merge [MDEV-7910](https://jira.mariadb.org/browse/MDEV-7910) into 10.1
* [Revision #b3c7c8c](https://github.com/MariaDB/server/commit/b3c7c8c)\
  2015-04-08 15:07:23 +0200
  * [MDEV-7910](https://jira.mariadb.org/browse/MDEV-7910): innodb.binlog\_consistent fails sporadically in buildbot
* [Revision #7ee1a41](https://github.com/MariaDB/server/commit/7ee1a41)\
  2015-04-08 13:15:04 +0200
  * [MDEV-7888](https://jira.mariadb.org/browse/MDEV-7888), [MDEV-7929](https://jira.mariadb.org/browse/MDEV-7929): Parallel replication hangs sometimes on ANALYZE TABLE or DDL
* [Revision #48c10fb](https://github.com/MariaDB/server/commit/48c10fb)\
  2015-04-08 11:04:24 +0200
  * Merge [MDEV-7888](https://jira.mariadb.org/browse/MDEV-7888) and [MDEV-7929](https://jira.mariadb.org/browse/MDEV-7929) into 10.1.
* [Revision #3b96134](https://github.com/MariaDB/server/commit/3b96134)\
  2015-04-08 11:01:18 +0200
  * [MDEV-7888](https://jira.mariadb.org/browse/MDEV-7888), [MDEV-7929](https://jira.mariadb.org/browse/MDEV-7929): Parallel replication hangs sometimes on ANALYZE TABLE or DDL
* [Revision #6a3932f](https://github.com/MariaDB/server/commit/6a3932f)\
  2015-03-31 19:53:57 +0200
  * use key derivation procedure for all encryption algorithms
* [Revision #ef5b488](https://github.com/MariaDB/server/commit/ef5b488)\
  2015-03-31 19:00:51 +0200
  * optimize encryption api
* [Revision #c91e326](https://github.com/MariaDB/server/commit/c91e326)\
  2015-03-30 18:00:50 +0200
  * tests for file\_key\_management plugin key file parser
* [Revision #e02749a](https://github.com/MariaDB/server/commit/e02749a)\
  2015-03-28 13:25:25 +0100
  * completely rewrote file\_key\_management plugin
* [Revision #9bda4bc](https://github.com/MariaDB/server/commit/9bda4bc)\
  2015-03-30 14:16:34 +0200
  * report a plugin loading offset at dlopen time
* [Revision #beea778](https://github.com/MariaDB/server/commit/beea778)\
  2015-03-30 17:13:42 +0200
  * copy-paste bug in service\_sha1.h
* [Revision #32e5304](https://github.com/MariaDB/server/commit/32e5304)\
  2015-03-28 18:05:53 +0100
  * mtr: fix testname,combination syntax to work in many-combination case
* [Revision #5fcba6e](https://github.com/MariaDB/server/commit/5fcba6e)\
  2015-03-28 10:55:31 +0100
  * small cleanup
* [Revision #8863272](https://github.com/MariaDB/server/commit/8863272)\
  2015-03-27 15:58:02 +0100
  * rename plugins to remove "\_plugin" from the plugin name
* [Revision #817a63f](https://github.com/MariaDB/server/commit/817a63f)\
  2015-03-26 17:40:52 +0100
  * pass the correct key length to encryption routines
* [Revision #2643cc5](https://github.com/MariaDB/server/commit/2643cc5)\
  2015-03-26 17:20:23 +0100
  * Don't crash the server if en-/decryption fails in Aria
* [Revision #f379c9a](https://github.com/MariaDB/server/commit/f379c9a)\
  2015-03-26 17:00:49 +0100
  * remove Aria-only handler flag
* [Revision #3986532](https://github.com/MariaDB/server/commit/3986532)\
  2015-03-26 15:57:08 +0100
  * remove a google specific script
* [Revision #7a387c0](https://github.com/MariaDB/server/commit/7a387c0)\
  2015-03-26 15:37:40 +0100
  * table->keep\_row\_order no longer need to force DYNAMIC\_RECORD
* [Revision #5d8dbee](https://github.com/MariaDB/server/commit/5d8dbee)\
  2015-03-26 14:01:39 +0100
  * remove get\_iv() from the key management plugin API
* [Revision #c238e68](https://github.com/MariaDB/server/commit/c238e68)\
  2015-03-26 11:12:02 +0100
  * move debug\_use\_static\_encryption\_keys and debug\_encryption\_key\_version to a plugin
* [Revision #b937574](https://github.com/MariaDB/server/commit/b937574)\
  2015-03-25 19:36:10 +0100
  * remove old my\_aes\_encrypt/decrypt
* [Revision #91f7363](https://github.com/MariaDB/server/commit/91f7363)\
  2015-03-25 19:35:22 +0100
  * yassl padding
* [Revision #f444d13](https://github.com/MariaDB/server/commit/f444d13)\
  2015-03-25 16:11:16 +0100
  * my\_aes\* functions: support for different key lengths
* [Revision #2b475b5](https://github.com/MariaDB/server/commit/2b475b5)\
  2015-04-08 03:33:48 +0300
  * [MDEV-7927](https://jira.mariadb.org/browse/MDEV-7927): Server crashes in Time\_and\_counter\_tracker::incr\_loops
* [Revision #d2b8780](https://github.com/MariaDB/server/commit/d2b8780)\
  2015-04-02 16:52:30 +0300
  * Fix test failure on these scrub tests.
* [Revision #4865fd1](https://github.com/MariaDB/server/commit/4865fd1)\
  2015-04-02 13:49:50 +0300
  * InnoDB/XtraDB Encryption cleanup
* [Revision #af768c2](https://github.com/MariaDB/server/commit/af768c2)\
  2015-04-01 22:03:14 +0300
  * InnoDB/XtraDB Encryption code cleanup
* [Revision #71ec046](https://github.com/MariaDB/server/commit/71ec046)\
  2015-04-01 20:33:50 +0300
  * Encryption cleanup
* [Revision #0ba9fa3](https://github.com/MariaDB/server/commit/0ba9fa3)\
  2015-04-01 19:37:00 +0300
  * InnoDB/XtraDB Encryption cleanup
* [Revision #b4a4d82](https://github.com/MariaDB/server/commit/b4a4d82)\
  2015-04-01 11:50:21 +0300
  * InnoDB/XtraDB Encryption cleanup.
* [Revision #0df8c0a](https://github.com/MariaDB/server/commit/0df8c0a)\
  2015-04-07 12:02:58 +0300
  * Merge branch 'bb-10.1-explain-analyze' into 10.1
* [Revision #6be0f80](https://github.com/MariaDB/server/commit/6be0f80)\
  2015-04-07 12:01:43 +0300
  * Merge branch 'bb-10.1-explain-analyze' of github.com:MariaDB/server into bb-10.1-explain-analyze
* [Revision #129822a](https://github.com/MariaDB/server/commit/129822a)\
  2015-04-07 12:00:23 +0300
  * Merge branch 'bb-10.1-explain-analyze' into 10.1
* [Revision #2af935c](https://github.com/MariaDB/server/commit/2af935c)\
  2015-04-07 01:29:17 +0300
  * [MDEV-7899](https://jira.mariadb.org/browse/MDEV-7899): 10.1 is 3% slower than 10.0 in OLTP RO
* [Revision #7d9e94e](https://github.com/MariaDB/server/commit/7d9e94e)\
  2015-04-06 19:37:37 +0300
  * [MDEV-7916](https://jira.mariadb.org/browse/MDEV-7916): main.analyze\_format\_json fails in buildbot on labrador
* [Revision #eb83e94](https://github.com/MariaDB/server/commit/eb83e94)\
  2015-04-06 19:13:33 +0300
  * [MDEV-7917](https://jira.mariadb.org/browse/MDEV-7917) main.log\_tables fails sporadically in buildbot #2
* [Revision #2f6d63f](https://github.com/MariaDB/server/commit/2f6d63f)\
  2015-04-06 18:56:39 +0300
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #2936fb1](https://github.com/MariaDB/server/commit/2936fb1)\
  2015-04-06 18:54:08 +0300
  * [MDEV-7919](https://jira.mariadb.org/browse/MDEV-7919): main.explain\_json\* fail in buildbot with valgrind
* [Revision #3674c36](https://github.com/MariaDB/server/commit/3674c36)\
  2015-04-06 12:45:35 +0300
  * [MDEV-7918](https://jira.mariadb.org/browse/MDEV-7918): A number of tests fail in valgrind builder with "InnoDB: Error: Requested state 6 current state 4 old\_state 4"
* [Revision #3bbe205](https://github.com/MariaDB/server/commit/3bbe205)\
  2015-03-25 09:47:26 +0100
  * yassl support
* [Revision #2f8d101](https://github.com/MariaDB/server/commit/2f8d101)\
  2015-03-24 20:43:20 +0100
  * unify my\_{en|de}crypt\_{cbc|ecb|ctr}. no yassl support yet.
* [Revision #27cc252](https://github.com/MariaDB/server/commit/27cc252)\
  2015-03-24 13:52:43 +0100
  * simplify my\_crypt.cc, remove duplicate code
* [Revision #6a7ee5a](https://github.com/MariaDB/server/commit/6a7ee5a)\
  2015-03-26 17:16:37 +0100
  * encryption cleanup: small changes
* [Revision #87604c4](https://github.com/MariaDB/server/commit/87604c4)\
  2015-03-09 19:53:47 +0100
  * encryption cleanup: delete obsolete files
* [Revision #16a7738](https://github.com/MariaDB/server/commit/16a7738)\
  2015-03-13 18:52:10 +0100
  * [MDEV-6819](https://jira.mariadb.org/browse/MDEV-6819) st\_mysql\_show\_var::value should be void\* not char\*
* [Revision #0cbe0c9](https://github.com/MariaDB/server/commit/0cbe0c9)\
  2015-03-11 12:28:26 +0100
  * remove one cmake MESSAGE
* [Revision #47c344b](https://github.com/MariaDB/server/commit/47c344b)\
  2015-04-04 00:47:10 +0300
  * [MDEV-7904](https://jira.mariadb.org/browse/MDEV-7904): ANALYZE FORMAT=JSON doesn't print r\_rows for union output
* [Revision #a220905](https://github.com/MariaDB/server/commit/a220905)\
  2015-04-02 18:19:33 +0200
  * [MDEV-7833](https://jira.mariadb.org/browse/MDEV-7833):ANALYZE FORMAT=JSON and Range checked for each record
* [Revision #7f613eb](https://github.com/MariaDB/server/commit/7f613eb)\
  2015-04-03 15:43:55 +0400
  * [MDEV-7284](https://jira.mariadb.org/browse/MDEV-7284) INDEX: CREATE OR REPLACE
* [Revision #118fc5c](https://github.com/MariaDB/server/commit/118fc5c)\
  2015-04-03 08:50:59 +0300
  * Adjust test timeout to let long semaphore wait signaling to happen.
* [Revision #575dd77](https://github.com/MariaDB/server/commit/575dd77)\
  2015-04-01 18:25:40 -0400
  * [MDEV-7867](https://jira.mariadb.org/browse/MDEV-7867): Add binlog header to GRA\_.log file
* [Revision #ca2f2b7](https://github.com/MariaDB/server/commit/ca2f2b7)\
  2015-03-31 09:54:40 +0300
  * Adjust test wait timeout.
* [Revision #cbc5157](https://github.com/MariaDB/server/commit/cbc5157)\
  2015-03-31 09:00:01 +0300
  * [MDEV-7878](https://jira.mariadb.org/browse/MDEV-7878): innodb\_scrub\_background fails sporadically in buildbot (Failing assertion: offset > 0 && offset < UNIV\_PAGE\_SIZE)
* [Revision #f573b65](https://github.com/MariaDB/server/commit/f573b65)\
  2015-03-30 15:10:29 +0200
  * Merge [MDEV-7847](https://jira.mariadb.org/browse/MDEV-7847) and [MDEV-7882](https://jira.mariadb.org/browse/MDEV-7882) into 10.0.
* [Revision #880f227](https://github.com/MariaDB/server/commit/880f227)\
  2015-03-30 14:33:44 +0200
  * [MDEV-7847](https://jira.mariadb.org/browse/MDEV-7847): "Slave worker thread retried transaction 10 time(s) in vain, giving up", followed by replication hanging
* [Revision #a408291](https://github.com/MariaDB/server/commit/a408291)\
  2015-03-30 14:16:57 +0200
  * [MDEV-7882](https://jira.mariadb.org/browse/MDEV-7882): Excessive transaction retry in parallel replication
* [Revision #59df100](https://github.com/MariaDB/server/commit/59df100)\
  2015-03-30 10:57:44 +0400
  * Removing Item\_string::m\_cs\_specified and making Item\_string::is\_cs\_specified() virtual instead.
* [Revision #49220f7](https://github.com/MariaDB/server/commit/49220f7)\
  2015-03-30 01:11:14 +0300
  * Increased the version number
* [Revision #bf963d3](https://github.com/MariaDB/server/commit/bf963d3)\
  2015-03-30 01:09:59 +0300
  * [MDEV-7874](https://jira.mariadb.org/browse/MDEV-7874) deb package installation fails with "dpkg: dependency problems prevent configuration of mariadb-server"
* [Revision #b2a1187](https://github.com/MariaDB/server/commit/b2a1187)\
  2015-03-26 10:48:56 +0100
  * [MDEV-7812](https://jira.mariadb.org/browse/MDEV-7812): ANALYZE FORMAT=JSON UPDATE/DELETE doesnt print the r\_total\_time\_ms
* [Revision #9b8f86f](https://github.com/MariaDB/server/commit/9b8f86f)\
  2015-03-27 23:44:06 +0300
  * Better comments
* [Revision #47c26d5](https://github.com/MariaDB/server/commit/47c26d5)\
  2015-03-27 11:36:43 +0200
  * Skip necessary encryption tests if required plugin is not found.
* [Revision #50eee60](https://github.com/MariaDB/server/commit/50eee60)\
  2015-03-26 20:44:12 +0400
  * Preparatory refactoring for: [MDEV-6218](https://jira.mariadb.org/browse/MDEV-6218) Wrong result of CHAR\_LENGTH(non-BMP-character) with 3-byte utf8
    * Moving get\_text() as a method to Lex\_input\_stream.
    * Moving the unescaping part into a separate function, this piece of code will later go to /strings most likely.
    * Removing Lex\_input\_string::yytoklen, as it's not needed any more.
* [Revision #4feaa06](https://github.com/MariaDB/server/commit/4feaa06)\
  2015-03-26 00:00:12 +0100
  * [MDEV-7816](https://jira.mariadb.org/browse/MDEV-7816) ALTER with DROP INDEX and ADD INDEX .. COMMENT='comment2' ignores the new comment
* [Revision #01d7da6](https://github.com/MariaDB/server/commit/01d7da6)\
  2015-03-25 19:11:46 +0100
  * [MDEV-7834](https://jira.mariadb.org/browse/MDEV-7834): ANALYZE FORMAT=JSON output column should be named ANALYZE
* [Revision #e15d792](https://github.com/MariaDB/server/commit/e15d792)\
  2015-03-25 21:20:06 +0300
  * Trivial test results updates
* [Revision #3841e92](https://github.com/MariaDB/server/commit/3841e92)\
  2015-03-25 21:07:23 +0300
  * Merge branch 'bb-10.1-explain-analyze' into 10.1
* [Revision #34fcc28](https://github.com/MariaDB/server/commit/34fcc28)\
  2015-03-25 19:34:08 +0300
  * Merge pull request #33 from k0da/[MDEV-7839](https://jira.mariadb.org/browse/MDEV-7839)
* [Revision #71bbff8](https://github.com/MariaDB/server/commit/71bbff8)\
  2015-03-25 17:21:52 +0100
  * Fix BigEndian build
* [Revision #f42064a](https://github.com/MariaDB/server/commit/f42064a)\
  2015-03-25 12:20:16 +0300
  * Fix valgrind failure: correclty clean up handler::tracker
* [Revision #651a142a](https://github.com/MariaDB/server/commit/651a142a)\
  2015-03-25 13:06:04 +0400
  * [MDEV-7831](https://jira.mariadb.org/browse/MDEV-7831) Bad warning for DATE\_ADD(timestamp\_column, INTERVAL 10 SECOND)
* [Revision #bd2ae78](https://github.com/MariaDB/server/commit/bd2ae78)\
  2015-03-24 16:33:51 +0100
  * [MDEV-7825](https://jira.mariadb.org/browse/MDEV-7825): Parallel replication race condition on gco->flags, possibly resulting in slave hang
* [Revision #664ce4c](https://github.com/MariaDB/server/commit/664ce4c)\
  2015-03-24 17:35:29 +0300
  * Fix linking: move the inline functions
* [Revision #4106dfe](https://github.com/MariaDB/server/commit/4106dfe)\
  2015-03-24 16:26:42 +0300
  * Merge branch 'bb-10.1-explain-analyze' into 10.1
* [Revision #77e16ce](https://github.com/MariaDB/server/commit/77e16ce)\
  2015-03-24 16:17:41 +0300
  * [MDEV-7648](https://jira.mariadb.org/browse/MDEV-7648): Extra data in ANALYZE FORMAT=JSON $stmt
* [Revision #b273e4a](https://github.com/MariaDB/server/commit/b273e4a)\
  2015-03-24 13:22:03 +0300
  * Better comments
* [Revision #ec68494](https://github.com/MariaDB/server/commit/ec68494)\
  2015-03-23 17:38:55 +0400
  * [MDEV-7677](https://jira.mariadb.org/browse/MDEV-7677) my\_charset\_handler\_filename has a wrong "ismbchar" member
* [Revision #4fbba09](https://github.com/MariaDB/server/commit/4fbba09)\
  2015-03-21 19:54:06 +0200
  * [MDEV-7813](https://jira.mariadb.org/browse/MDEV-7813) analyze\_stmt fails with --embedded flag set
* [Revision #3578419](https://github.com/MariaDB/server/commit/3578419)\
  2015-03-20 12:38:53 +0200
  * [MDEV-7797](https://jira.mariadb.org/browse/MDEV-7797): file\_key\_management\_plugin uses static IV for a key
* [Revision #0c26c00](https://github.com/MariaDB/server/commit/0c26c00)\
  2015-03-20 13:51:41 +0400
  * A preparatory patch for [MDEV-7284](https://jira.mariadb.org/browse/MDEV-7284) INDEX: CREATE OR REPLACE. Removing "bool Key::create\_if\_not\_exists" and deriving Key from DDL\_options instead.
* [Revision #2a2cc16](https://github.com/MariaDB/server/commit/2a2cc16)\
  2015-03-20 11:46:44 +0400
  * Refactoring in sql\_yacc.yy. A pre-requirement patch for [MDEV-7801](https://jira.mariadb.org/browse/MDEV-7801) Unexpected syntax error in ALTER TABLE t1 ADD INDEX TYPE BTREE [MDEV-7284](https://jira.mariadb.org/browse/MDEV-7284) INDEX: CREATE OR REPLACE
* [Revision #e379531](https://github.com/MariaDB/server/commit/e379531)\
  2015-03-20 09:10:59 +0200
  * [MDEV-5214](https://jira.mariadb.org/browse/MDEV-5214) Status variables for number of global/db/table/column/role grants
* [Revision #ce0427a](https://github.com/MariaDB/server/commit/ce0427a)\
  2015-03-19 20:41:57 -0400
  * Update galera.global\_suppressions with galera warnings.
* [Revision #1a32993](https://github.com/MariaDB/server/commit/1a32993)\
  2015-03-18 20:36:58 +0200
  * [MDEV-5214](https://jira.mariadb.org/browse/MDEV-5214) Status variables for number of global/db/table/column/role grants
* [Revision #f8381d9](https://github.com/MariaDB/server/commit/f8381d9)\
  2015-03-19 09:47:20 -0400
  * [MDEV-6069](https://jira.mariadb.org/browse/MDEV-6069): Remove old logic for 3.23-to-higher upgrades from upgrade SQL scripts
* [Revision #b3438f2](https://github.com/MariaDB/server/commit/b3438f2)\
  2015-03-19 14:09:49 +0200
  * [MDEV-7803](https://jira.mariadb.org/browse/MDEV-7803): Encryption metadata (crypt\_data) is written to InnoDB file space page 0 even when encryption is not enabled
* [Revision #81113da](https://github.com/MariaDB/server/commit/81113da)\
  2015-03-19 10:22:27 +0200
  * Merge branch '10.1' into bb-10.1-jan
* [Revision #64a290d](https://github.com/MariaDB/server/commit/64a290d)\
  2015-03-19 10:18:40 +0200
  * [MDEV-7797](https://jira.mariadb.org/browse/MDEV-7797): file\_key\_management\_plugin uses static IV for a key
* [Revision #bab0bdb](https://github.com/MariaDB/server/commit/bab0bdb)\
  2015-03-19 07:07:56 +0200
  * Introduce two debug crash points while writing crypt data to test redo operations.
* [Revision #e28a241](https://github.com/MariaDB/server/commit/e28a241)\
  2015-03-18 17:10:48 +0400
  * [MDEV-7661](https://jira.mariadb.org/browse/MDEV-7661) Unexpected result for: CAST(0xHHHH AS CHAR CHARACTER SET xxx) for incorrect byte sequences
* [Revision #a471b70](https://github.com/MariaDB/server/commit/a471b70)\
  2015-03-18 15:25:34 +0400
  * Fixed innodb and innodb\_bug59641 failures on PPC64.
* [Revision #5e6905b](https://github.com/MariaDB/server/commit/5e6905b)\
  2015-03-17 10:59:25 +0200
  * Replace static usage of AES\_CTR with current encryption algorithm.
* [Revision #b0542b7](https://github.com/MariaDB/server/commit/b0542b7)\
  2015-03-17 14:56:14 +0400
  * Installation fix.
* [Revision #015994f](https://github.com/MariaDB/server/commit/015994f)\
  2015-03-17 14:44:59 +0400
  * [MDEV-7515](https://jira.mariadb.org/browse/MDEV-7515) GIS: No AddGeometryColumn or DropGeometryColumn in the tree.
* [Revision #69ae506](https://github.com/MariaDB/server/commit/69ae506)\
  2015-03-17 11:00:28 +0200
  * Merge branch '10.1' into bb-10.1-jan
* [Revision #97037da](https://github.com/MariaDB/server/commit/97037da)\
  2015-03-17 10:59:25 +0200
  * Replace static usage of AES\_CTR with current encryption algorithm.
* [Revision #ccc7297](https://github.com/MariaDB/server/commit/ccc7297)\
  2015-03-17 12:56:38 +0400
  * Test result fixed.
* [Revision #4ba16ea](https://github.com/MariaDB/server/commit/4ba16ea)\
  2015-03-17 09:24:22 +0100
  * Merge [MDEV-6981](https://jira.mariadb.org/browse/MDEV-6981) and [MDEV-6981](https://jira.mariadb.org/browse/MDEV-6981) (from danblack) into [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)
* [Revision #a3e68b4](https://github.com/MariaDB/server/commit/a3e68b4)\
  2015-03-13 14:18:07 +0200
  * [MDEV-7772](https://jira.mariadb.org/browse/MDEV-7772): SIGSEGV on my\_aes\_encrypt\_cbc when -DWITH\_SSL=bundled
* [Revision #5e6f123](https://github.com/MariaDB/server/commit/5e6f123)\
  2015-03-16 21:50:20 -0400
  * [MDEV-6069](https://jira.mariadb.org/browse/MDEV-6069): Remove old logic for 3.23-to-higher upgrades from upgrade SQL scripts
* [Revision #0d7bc1e](https://github.com/MariaDB/server/commit/0d7bc1e)\
  2015-03-16 21:01:58 +0100
  * 32 bit test fix
* [Revision #fec94a6](https://github.com/MariaDB/server/commit/fec94a6)\
  2015-03-16 22:54:43 +0400
  * [MDEV-7728](https://jira.mariadb.org/browse/MDEV-7728) - Improve xid cache scalability by using lock-free hash
* [Revision #e6f67c6](https://github.com/MariaDB/server/commit/e6f67c6)\
  2015-03-16 21:55:10 +0400
  * [MDEV-6572](https://jira.mariadb.org/browse/MDEV-6572) "USE dbname" with a bad sequence erroneously connects to a wrong database
* [Revision #4cb86b7](https://github.com/MariaDB/server/commit/4cb86b7)\
  2015-03-16 18:54:45 +0400
  * [MDEV-7728](https://jira.mariadb.org/browse/MDEV-7728) - Improve xid cache scalability by using lock-free hash
* [Revision #6bd24dea](https://github.com/MariaDB/server/commit/6bd24dea)\
  2015-03-16 18:44:06 +0400
  * [MDEV-7728](https://jira.mariadb.org/browse/MDEV-7728) - Improve xid cache scalability by using lock-free hash
* [Revision #be1c566](https://github.com/MariaDB/server/commit/be1c566)\
  2015-03-16 15:02:05 +0100
  * [MDEV-6981](https://jira.mariadb.org/browse/MDEV-6981): feature request MASTER\_GTID\_WAIT status variables
* [Revision #1f8efee](https://github.com/MariaDB/server/commit/1f8efee)\
  2015-03-16 14:54:16 +0100
  * Merge [MDEV-7198](https://jira.mariadb.org/browse/MDEV-7198): status variable for Slave\_skipped\_errors
* [Revision #ef4d8db](https://github.com/MariaDB/server/commit/ef4d8db)\
  2015-03-16 14:40:29 +0100
  * [MDEV-6981](https://jira.mariadb.org/browse/MDEV-6981): feature request MASTER\_GTID\_WAIT status variables
* [Revision #0e717c5](https://github.com/MariaDB/server/commit/0e717c5)\
  2015-03-16 13:41:11 +0100
  * Merge branch '[MDEV-6981](https://jira.mariadb.org/browse/MDEV-6981)-master\_gtid\_wait-status-variables' of [mariadb-server](https://github.com/openquery/mariadb-server) into danblack
* [Revision #9362dd4](https://github.com/MariaDB/server/commit/9362dd4)\
  2015-03-16 23:15:36 +1100
  * additional slave\_skip\_errors status
* [Revision #51ea393](https://github.com/MariaDB/server/commit/51ea393)\
  2015-03-16 23:06:30 +1100
  * Complete test for status slave\_skipped\_errors
* [Revision #18e9c31](https://github.com/MariaDB/server/commit/18e9c31)\
  2015-02-10 14:05:49 +0400
  * [MDEV-6650](https://jira.mariadb.org/browse/MDEV-6650) - LINT\_INIT emits code in non-debug builds
* [Revision #e7b1d73](https://github.com/MariaDB/server/commit/e7b1d73)\
  2015-03-16 12:47:32 +0200
  * Introduce only one combinations file and rule for aes\_ctr to suite.pm so that it is not used if not available.
* [Revision #10554ca](https://github.com/MariaDB/server/commit/10554ca)\
  2015-03-16 12:02:21 +0400
  * Test results fixed.
* [Revision #f48dc5c](https://github.com/MariaDB/server/commit/f48dc5c)\
  2015-03-16 12:14:31 +0400
  * Moving the conversion code from String::well\_formed\_copy() to my\_convert\_fix() - a new function in /strings.
* [Revision #c4b268a](https://github.com/MariaDB/server/commit/c4b268a)\
  2015-03-16 09:14:13 +0200
  * InnoDB cleanup. Remove empty statements i.e. extra ; characters.
* [Revision #da4b524](https://github.com/MariaDB/server/commit/da4b524)\
  2015-03-15 23:00:05 +0400
  * [MDEV-7512](https://jira.mariadb.org/browse/MDEV-7512) GIS: ST\_ synonyms for functions are not consistent. Checked for missing synonims, added those found.
* [Revision #874f0d7](https://github.com/MariaDB/server/commit/874f0d7)\
  2015-03-15 22:27:45 +0400
  * Test result fixed.
* [Revision #37345bd](https://github.com/MariaDB/server/commit/37345bd)\
  2015-03-15 22:20:38 +0400
  * [MDEV-7529](https://jira.mariadb.org/browse/MDEV-7529) GIS: ST\_Relate returns unexpected results for POINT relations. Problem was that we considered the point itself as the 'border' object. Instead of that the 'border' of a POINT is an empty set, and the point is the 'interior'. Another error fixed by the way - not all operations of the resulting function were properly allocated.
* [Revision #ca30418](https://github.com/MariaDB/server/commit/ca30418)\
  2015-03-15 11:17:50 +0400
  * [MDEV-7514](https://jira.mariadb.org/browse/MDEV-7514) GIS: PointOnSurface returns NULL instead of the point. Need to take into account cases of a polygon shaped as a very thin line.
* [Revision #a21ef88](https://github.com/MariaDB/server/commit/a21ef88)\
  2015-03-11 11:02:13 +0100
  * [MDEV-6954](https://jira.mariadb.org/browse/MDEV-6954): SET STATEMENT rand\_seedX = ...FOR ... makes the next rand() to return 0
* [Revision #41106b2](https://github.com/MariaDB/server/commit/41106b2)\
  2015-03-13 16:32:47 +0100
  * [MDEV-6997](https://jira.mariadb.org/browse/MDEV-6997): SET STATEMENT last\_insert\_id FOR ... does not affect the value written to the binlog
* [Revision #197afb4](https://github.com/MariaDB/server/commit/197afb4)\
  2015-03-13 16:51:36 +0400
  * [MDEV-6566](https://jira.mariadb.org/browse/MDEV-6566) Different INSERT behaviour on bad bytes with and without character set conversion
* [Revision #7c21ea9](https://github.com/MariaDB/server/commit/7c21ea9)\
  2015-03-13 14:18:07 +0200
  * [MDEV-7772](https://jira.mariadb.org/browse/MDEV-7772): SIGSEGV on my\_aes\_encrypt\_cbc when -DWITH\_SSL=bundled
* [Revision #702fba1](https://github.com/MariaDB/server/commit/702fba1)\
  2015-03-13 16:10:31 +0400
  * [MDEV-7510](https://jira.mariadb.org/browse/MDEV-7510) GIS: IsRing returns false for a primitive triangle.
* [Revision #75d65b5](https://github.com/MariaDB/server/commit/75d65b5)\
  2015-03-13 15:48:39 +0400
  * [MDEV-6989](https://jira.mariadb.org/browse/MDEV-6989) BINARY and COLLATE xxx\_bin comparisions are not used for optimization in some cases
* [Revision #bd21058](https://github.com/MariaDB/server/commit/bd21058)\
  2015-03-13 13:52:07 +0400
  * Adding "const" qualifier to Item::compare\_collation()
* [Revision #4d0e521](https://github.com/MariaDB/server/commit/4d0e521)\
  2015-03-13 09:38:08 +0200
  * [MDEV-7770](https://jira.mariadb.org/browse/MDEV-7770): Online DDL progress output contains incorrectly printed index names
* [Revision #bb3115b](https://github.com/MariaDB/server/commit/bb3115b)\
  2015-03-12 18:12:15 +0400
  * [MDEV-6990](https://jira.mariadb.org/browse/MDEV-6990) GROUP\_MIN\_MAX optimization is not applied in some cases when it could
* [Revision #129c82b](https://github.com/MariaDB/server/commit/129c82b)\
  2015-03-12 17:50:23 +0400
  * [MDEV-7334](https://jira.mariadb.org/browse/MDEV-7334) valgrind warning "unitialized bytes" in 10.1. The 'srid' field's copying was missing in the copying Create\_field::Create\_field() constructor.
* [Revision #8249dca](https://github.com/MariaDB/server/commit/8249dca)\
  2015-03-10 08:28:51 +0200
  * [MDEV-6858](https://jira.mariadb.org/browse/MDEV-6858): enforce\_storage\_engine option
* [Revision #ba3573c](https://github.com/MariaDB/server/commit/ba3573c)\
  2015-03-12 13:40:52 +0400
  * Clean-up:
    * Renaming Item::is\_bool\_func() to is\_bool\_type(), to avoid assumption that the item is an Item\_func derivant.
    * Deriving Item\_func\_spatial\_rel from Item\_bool\_func rather than Item\_int\_func
* [Revision #a71e2d2](https://github.com/MariaDB/server/commit/a71e2d2)\
  2015-02-17 12:54:51 +0100
  * [MDEV-7006](https://jira.mariadb.org/browse/MDEV-7006) [MDEV-7007](https://jira.mariadb.org/browse/MDEV-7007): SET STATEMENT and slow log fixed embedded server tests [MDEV-7009](https://jira.mariadb.org/browse/MDEV-7009): SET STATEMENT min\_examined\_row\_limit has no effect [MDEV-6948](https://jira.mariadb.org/browse/MDEV-6948):SET STATEMENT gtid\_domain\_id = ... FOR has no effect (same for gtid\_seq\_no and server\_id)
* [Revision #dab1236](https://github.com/MariaDB/server/commit/dab1236)\
  2015-02-25 21:29:13 +0100
  * [MDEV-6956](https://jira.mariadb.org/browse/MDEV-6956):SET STATEMENT default\_master\_connection = ... has no effect
* [Revision #e91bc2e](https://github.com/MariaDB/server/commit/e91bc2e)\
  2015-03-12 11:40:37 +0400
  * [MDEV-7759](https://jira.mariadb.org/browse/MDEV-7759) NULLIF(x,y) is not equal to CASE WHEN x=y THEN NULL ELSE x END
* [Revision #fa5809c](https://github.com/MariaDB/server/commit/fa5809c)\
  2015-03-12 06:43:38 +1100
  * Add Master\_gtid\_wait\_{count,time,timeouts} status
* [Revision #eac71ce](https://github.com/MariaDB/server/commit/eac71ce)\
  2015-03-12 05:23:05 +1100
  * Add Slave\_skipped\_errors to global status
* [Revision #80f03ab](https://github.com/MariaDB/server/commit/80f03ab)\
  2015-03-10 10:24:20 +0100
  * [MDEV-7671](https://jira.mariadb.org/browse/MDEV-7671): Cache VIEW definitions in the TDC
* [Revision #3aa1a60](https://github.com/MariaDB/server/commit/3aa1a60)\
  2015-03-11 15:15:43 +0100
  * Merge branch '10.1' of github.com:MariaDB/server into 10.1
* [Revision #be73c7e](https://github.com/MariaDB/server/commit/be73c7e)\
  2015-03-11 14:57:30 +0100
  * [MDEV-6951](https://jira.mariadb.org/browse/MDEV-6951): Erroneous SET STATEMENT produces two identical errors
* [Revision #52a1b5a](https://github.com/MariaDB/server/commit/52a1b5a)\
  2015-03-11 13:05:03 +0400
  * MY\_CHECK\_AND\_SET\_COMPILER\_FLAG changes
* [Revision #190858d](https://github.com/MariaDB/server/commit/190858d)\
  2015-03-11 12:40:35 +0400
  * Removing duplicate code: adding Item\_func\_bool\_predicate as a common parent class for Item\_func\_isnull and Item\_func\_isnotnull
* [Revision #9f4ee16](https://github.com/MariaDB/server/commit/9f4ee16)\
  2015-03-11 07:29:51 +0200
  * [MDEV-7619](https://jira.mariadb.org/browse/MDEV-7619): Improve long semaphore wait output
* [Revision #ba43735](https://github.com/MariaDB/server/commit/ba43735)\
  2015-03-10 22:34:57 +0400
  * Check for the openssl-dev so the build doesn't fail without it.
* [Revision #0ed57e3](https://github.com/MariaDB/server/commit/0ed57e3)\
  2015-03-04 12:20:10 +0200
  * [MDEV-7025](https://jira.mariadb.org/browse/MDEV-7025) ANALYZE SELECT/INSERT/UPDATE/DELETE from a view does not check access permissions on the view
* [Revision #c8035da](https://github.com/MariaDB/server/commit/c8035da)\
  2015-03-10 14:05:57 +0200
  * Add more information if page state is not correct.
* [Revision #f7d196b](https://github.com/MariaDB/server/commit/f7d196b)\
  2015-03-08 17:22:37 +0100
  * 32bit fix
* [Revision #e2de804](https://github.com/MariaDB/server/commit/e2de804)\
  2015-03-08 12:54:42 +0100
  * Merge branch '10.1' into bb-10.1-serg
* [Revision #1626e0d](https://github.com/MariaDB/server/commit/1626e0d)\
  2015-03-07 22:47:28 +0300
  * [MDEV-7648](https://jira.mariadb.org/browse/MDEV-7648): Extra data in ANALYZE FORMAT=JSON $stmt
* [Revision #2288b84](https://github.com/MariaDB/server/commit/2288b84)\
  2015-03-07 20:51:35 +0300
  * [MDEV-7679](https://jira.mariadb.org/browse/MDEV-7679): ANALYZE crashes when printing WHERE when no default db
* [Revision #66ad265](https://github.com/MariaDB/server/commit/66ad265)\
  2015-03-07 19:30:19 +0300
  * [MDEV-7674](https://jira.mariadb.org/browse/MDEV-7674): ANALYZE shows r\_rows=0
* [Revision #5bff6c5](https://github.com/MariaDB/server/commit/5bff6c5)\
  2015-03-07 15:32:52 +0100
  * bison warning: clash on default action: != \<object\_ddl\_options>
* [Revision #6d8b74d](https://github.com/MariaDB/server/commit/6d8b74d)\
  2015-03-05 17:11:23 +0100
  * add a test for drop trigger under --read-only
* [Revision #18feb62](https://github.com/MariaDB/server/commit/18feb62)\
  2015-03-04 10:13:06 +0100
  * [MDEV-6819](https://jira.mariadb.org/browse/MDEV-6819) st\_mysql\_show\_var::value should be void\* not char\*
* [Revision #20cacb0](https://github.com/MariaDB/server/commit/20cacb0)\
  2015-03-05 09:58:08 +0100
  * fix a crash of innodb.innodb\_mutexes,innodb\_plugin
* [Revision #2db62f6](https://github.com/MariaDB/server/commit/2db62f6)\
  2015-03-07 13:21:02 +0100
  * Merge branch '10.0' into 10.1
* [Revision #d61573d](https://github.com/MariaDB/server/commit/d61573d)\
  2015-03-06 20:49:48 +0100
  * fix connect.json\_udf test for static builds
* [Revision #c0af821](https://github.com/MariaDB/server/commit/c0af821)\
  2015-03-06 13:32:46 +0100
  * [MDEV-7669](https://jira.mariadb.org/browse/MDEV-7669) tmp\_table\_count-7586 fails in ps and embedded
* [Revision #5f510a9](https://github.com/MariaDB/server/commit/5f510a9)\
  2015-03-06 18:41:32 +0100
  * Merge branch '5.5' into 10.0
* [Revision #17a3779](https://github.com/MariaDB/server/commit/17a3779)\
  2015-03-06 18:13:06 +0100
  * after innodb/xtradb merge: use the correct visibility for internal functions
* [Revision #d7d1907](https://github.com/MariaDB/server/commit/d7d1907)\
  2015-03-06 17:03:46 +0100
  * [MDEV-6838](https://jira.mariadb.org/browse/MDEV-6838) Using too big key for internal temp tables
* [Revision #12d87c3](https://github.com/MariaDB/server/commit/12d87c3)\
  2015-03-06 11:15:55 +0100
  * [MDEV-7659](https://jira.mariadb.org/browse/MDEV-7659) buildbot may leave stale mysqld
* [Revision #206b111](https://github.com/MariaDB/server/commit/206b111)\
  2015-03-06 11:19:23 +0200
  * [MDEV-7672](https://jira.mariadb.org/browse/MDEV-7672): Crash creating an InnoDB table with foreign keys
* [Revision #e13459a](https://github.com/MariaDB/server/commit/e13459a)\
  2015-03-05 15:30:11 +0400
  * [MDEV-7148](https://jira.mariadb.org/browse/MDEV-7148) - Recurring: InnoDB: Failing assertion: !lock->recursive
* [Revision #f66fbe8](https://github.com/MariaDB/server/commit/f66fbe8)\
  2015-03-05 12:05:59 +0200
  * [MDEV-7578](https://jira.mariadb.org/browse/MDEV-7578) :Slave is 10x slower to execute set of statements compared to master when using RBR
* [Revision #7dee7a0](https://github.com/MariaDB/server/commit/7dee7a0)\
  2015-03-05 09:40:12 +0100
  * GTID: Add missing test of reconnecting into out-of-order binlog.
* [Revision #143f5d9](https://github.com/MariaDB/server/commit/143f5d9)\
  2015-03-03 17:38:02 +0200
  * [MDEV-7061](https://jira.mariadb.org/browse/MDEV-7061): Augment innochecksum to give insight of fragmentation
* [Revision #2e4dc5a](https://github.com/MariaDB/server/commit/2e4dc5a)\
  2015-03-04 14:06:44 +0100
  * after-merge fixes
* [Revision #95d7208](https://github.com/MariaDB/server/commit/95d7208)\
  2015-03-04 13:48:28 +0100
  * Merge [MDEV-6589](https://jira.mariadb.org/browse/MDEV-6589) and [MDEV-6403](https://jira.mariadb.org/browse/MDEV-6403) into 10.1.
* [Revision #3ef0b9b](https://github.com/MariaDB/server/commit/3ef0b9b)\
  2015-03-04 13:36:54 +0100
  * Merge [MDEV-6589](https://jira.mariadb.org/browse/MDEV-6589) and [MDEV-6403](https://jira.mariadb.org/browse/MDEV-6403) into 10.0.
* [Revision #78c74db](https://github.com/MariaDB/server/commit/78c74db)\
  2015-03-04 13:10:37 +0100
  * [MDEV-6403](https://jira.mariadb.org/browse/MDEV-6403): Temporary tables lost at STOP SLAVE in GTID mode if master has not rotated binlog since restart
* [Revision #ad0d203](https://github.com/MariaDB/server/commit/ad0d203)\
  2015-02-18 12:22:50 +0100
  * [MDEV-6589](https://jira.mariadb.org/browse/MDEV-6589): Incorrect relay log start position when restarting SQL thread after error in parallel replication
* [Revision #f4f37533](https://github.com/MariaDB/server/commit/f4f37533)\
  2015-03-04 11:01:32 +0400
  * Replaced lf-hash element\_size hack with initializer function.
* [Revision #5c6aa4d](https://github.com/MariaDB/server/commit/5c6aa4d)\
  2015-02-27 11:30:35 +0400
  * [MDEV-6089](https://jira.mariadb.org/browse/MDEV-6089) - [MySQL Worklog #7305](https://dev.mysql.com/worklog/task/?id=7305) "Improve MDL scalability by using lock-free hash"
* [Revision #d9e3a9f](https://github.com/MariaDB/server/commit/d9e3a9f)\
  2015-02-27 00:01:38 +0400
  * [MDEV-6089](https://jira.mariadb.org/browse/MDEV-6089) - [MySQL Worklog #7305](https://dev.mysql.com/worklog/task/?id=7305) "Improve MDL scalability by using lock-free hash"
* [Revision #9c8165f](https://github.com/MariaDB/server/commit/9c8165f)\
  2015-02-26 21:17:33 +0400
  * [MDEV-6089](https://jira.mariadb.org/browse/MDEV-6089) - [MySQL Worklog #7305](https://dev.mysql.com/worklog/task/?id=7305) "Improve MDL scalability by using lock-free hash"
* [Revision #f5bd1d0](https://github.com/MariaDB/server/commit/f5bd1d0)\
  2015-02-26 18:40:05 +0400
  * [MDEV-6089](https://jira.mariadb.org/browse/MDEV-6089) - [MySQL Worklog #7305](https://dev.mysql.com/worklog/task/?id=7305) "Improve MDL scalability by using lock-free hash"
* [Revision #f475a7f](https://github.com/MariaDB/server/commit/f475a7f)\
  2015-02-26 13:12:28 +0400
  * [MDEV-6089](https://jira.mariadb.org/browse/MDEV-6089) - [MySQL Worklog #7305](https://dev.mysql.com/worklog/task/?id=7305) "Improve MDL scalability by using lock-free hash"
* [Revision #ecd3ff9](https://github.com/MariaDB/server/commit/ecd3ff9)\
  2015-02-26 13:12:01 +0400
  * [MDEV-6089](https://jira.mariadb.org/browse/MDEV-6089) - [MySQL Worklog #7305](https://dev.mysql.com/worklog/task/?id=7305) "Improve MDL scalability by using lock-free hash"
* [Revision #903160e](https://github.com/MariaDB/server/commit/903160e)\
  2015-02-26 13:11:30 +0400
  * [MDEV-6089](https://jira.mariadb.org/browse/MDEV-6089) - [MySQL Worklog #7305](https://dev.mysql.com/worklog/task/?id=7305) "Improve MDL scalability by using lock-free hash"
* [Revision #87b0cc9](https://github.com/MariaDB/server/commit/87b0cc9)\
  2015-03-04 09:52:01 +0400
  * [MDEV-7286](https://jira.mariadb.org/browse/MDEV-7286) TRIGGER: CREATE OR REPLACE, CREATE IF NOT EXISTS Based on the patch by Sriram Patil, made under terms of GSoC 2014.
* [Revision #a7ed852](https://github.com/MariaDB/server/commit/a7ed852)\
  2015-03-04 09:16:43 +0400
  * Adding a shared include file ctype-mb.ic and removing a number of very similar copies of my\_well\_formed\_len\_xxx(), implemented for big5, cp932, euckr, eucjpms, gb2312m gbk, sjis, ujis.
* [Revision #d8c1165](https://github.com/MariaDB/server/commit/d8c1165)\
  2015-03-03 11:46:44 +0100
  * fix failing innodb.innodb-page\_encryption\_log\_encryption again
* [Revision #e33b48a](https://github.com/MariaDB/server/commit/e33b48a)\
  2015-03-02 16:47:43 +0100
  * Merge remote-tracking branch 'origin/10.0' into 10.0
* [Revision #c06c465](https://github.com/MariaDB/server/commit/c06c465)\
  2015-03-02 16:45:44 +0100
  * 10.0-connect merge
* [Revision #b1b6101](https://github.com/MariaDB/server/commit/b1b6101)\
  2015-03-02 18:24:22 +0400
  * A preparatory patch for [MDEV-6566](https://jira.mariadb.org/browse/MDEV-6566). Adding a new virtual function MY\_CHARSET\_HANDLER::copy\_abort(). Moving character set specific code into the correspoding implementations (for simple, multi-byte and mbmaxlen>1 character sets).
* [Revision #7047bef](https://github.com/MariaDB/server/commit/7047bef)\
  2015-03-02 10:55:48 +0200
  * Use standard InnoDB error mechanism on compression and encryption error messages.
* [Revision #b9a9b82](https://github.com/MariaDB/server/commit/b9a9b82)\
  2015-03-02 00:35:56 +0100
  * Make json\_udf test work on Windows
* [Revision #5f4909b](https://github.com/MariaDB/server/commit/5f4909b)\
  2015-03-01 23:55:09 +0100
  * Making json\_udf test working on linux
* [Revision #34c8959](https://github.com/MariaDB/server/commit/34c8959)\
  2015-03-01 19:29:56 +0100
  * Remove a signed/unsigned warning.
* [Revision #5c8862e](https://github.com/MariaDB/server/commit/5c8862e)\
  2015-03-01 19:20:40 +0100
  * Fix crash when Json\_Value was called without arguments.
  * Correct memory calculation in Serialize.
  * Correct some UDF's messages.
  * Add and modify the json tests
* [Revision #1f1f977](https://github.com/MariaDB/server/commit/1f1f977)\
  2015-03-01 16:51:34 +0100
  * Fix test failing when file\_key\_management\_plugin doesn't load
* [Revision #c3f80a2](https://github.com/MariaDB/server/commit/c3f80a2)\
  2015-03-01 16:53:16 +0100
  * fix new innodb warnings to use the standard innodb warning syntax
* [Revision #d862d7c](https://github.com/MariaDB/server/commit/d862d7c)\
  2015-02-28 23:01:55 +0100
  * Implement random access to ODBC tables
* [Revision #45b6edb](https://github.com/MariaDB/server/commit/45b6edb)\
  2015-02-28 23:44:55 +0200
  * [MDEV-6838](https://jira.mariadb.org/browse/MDEV-6838): Using too big key for internal temp tables
* [Revision #c78f594](https://github.com/MariaDB/server/commit/c78f594)\
  2015-02-28 13:51:22 +0100
  * [MDEV-6479](https://jira.mariadb.org/browse/MDEV-6479) stack traces in 10.1
* [Revision #7ba2916](https://github.com/MariaDB/server/commit/7ba2916)\
  2015-02-27 21:42:03 +0100
  * [MDEV-7000](https://jira.mariadb.org/browse/MDEV-7000) Assertion \`0' failed in Protocol::end\_statement() on executing DDL under innodb\_fake\_changes=1
* [Revision #ba80708](https://github.com/MariaDB/server/commit/ba80708)\
  2015-02-27 20:13:51 +0100
  * [MDEV-6960](https://jira.mariadb.org/browse/MDEV-6960) Server crashes in check\_alter\_user on setting a default role via PS
* [Revision #7951bb1](https://github.com/MariaDB/server/commit/7951bb1)\
  2015-02-25 17:34:31 +0100
  * cleanup: remove unused variables
* [Revision #75a27ee](https://github.com/MariaDB/server/commit/75a27ee)\
  2015-02-27 23:33:22 -0500
  * [MDEV-4987](https://jira.mariadb.org/browse/MDEV-4987): Sort by domain\_id when list of GTIDs are output
* [Revision #34d86ac](https://github.com/MariaDB/server/commit/34d86ac)\
  2015-02-27 22:33:41 -0500
  * [MDEV-6594](https://jira.mariadb.org/browse/MDEV-6594): Use separate domain\_id for Galera transactions
* [Revision #0f8cb3c](https://github.com/MariaDB/server/commit/0f8cb3c)\
  2015-02-27 22:30:38 -0500
  * [MDEV-7615](https://jira.mariadb.org/browse/MDEV-7615): Remove --galera-sst-mode option from mysqldump
* [Revision #4c191de](https://github.com/MariaDB/server/commit/4c191de)\
  2015-02-27 22:13:37 -0500
  * [MDEV-7560](https://jira.mariadb.org/browse/MDEV-7560): wsrep\* tests depend on the version of galera library
* [Revision #16c4462](https://github.com/MariaDB/server/commit/16c4462)\
  2015-02-24 21:55:22 -0500
  * Changes in wsrep\_guess\_ip()
* [Revision #fa87fc7](https://github.com/MariaDB/server/commit/fa87fc7)\
  2015-02-27 18:28:40 +0100
  * update tokudb version after merge
* [Revision #aa845d1](https://github.com/MariaDB/server/commit/aa845d1)\
  2015-02-27 14:32:33 +0100
  * [MDEV-6391](https://jira.mariadb.org/browse/MDEV-6391): GTID binlog state not recovered if mariadb-bin.state is removed
* [Revision #72d7b12](https://github.com/MariaDB/server/commit/72d7b12)\
  2015-02-27 16:26:12 +0400
  * Reducing duplicate code and simplifying well formed string copying by adding a new class String\_copier.
* [Revision #2d01907](https://github.com/MariaDB/server/commit/2d01907)\
  2015-02-27 13:34:18 +0400
  * [MDEV-7281](https://jira.mariadb.org/browse/MDEV-7281) EVENT: CREATE OR REPLACE
* [Revision #77806da](https://github.com/MariaDB/server/commit/77806da)\
  2015-02-26 23:31:35 +0200
  * Fix incorrect parameter passing to create\_tmp\_table in create\_result\_table
* [Revision #ec4ff9a](https://github.com/MariaDB/server/commit/ec4ff9a)\
  2015-02-26 23:06:18 +0200
  * [MDEV-7586](https://jira.mariadb.org/browse/MDEV-7586): Merged derived tables/VIEWs increment created\_tmp\_tables
* [Revision #d7c6f11](https://github.com/MariaDB/server/commit/d7c6f11)\
  2015-02-26 19:41:21 +0200
  * Try to fix test warning.
* [Revision #f37b857](https://github.com/MariaDB/server/commit/f37b857)\
  2015-02-26 17:19:51 +0200
  * Fix test case.
* [Revision #018f932](https://github.com/MariaDB/server/commit/018f932)\
  2015-02-26 12:09:35 +0200
  * test
* [Revision #2eae684](https://github.com/MariaDB/server/commit/2eae684)\
  2015-02-25 13:26:57 +0200
  * [MDEV-7572](https://jira.mariadb.org/browse/MDEV-7572): InnoDB: Assertion failure in log\_init\_crypt\_key if file\_key\_management\_plugin is used
* [Revision #5c66abf](https://github.com/MariaDB/server/commit/5c66abf)\
  2015-02-25 16:34:33 +0100
  * Merge remote-tracking branch 'origin/10.0' into 10.0
* [Revision #4a3e94e](https://github.com/MariaDB/server/commit/4a3e94e)\
  2015-02-25 16:58:36 +0300
  * [MDEV-7413](https://jira.mariadb.org/browse/MDEV-7413): optimizer\_use\_condition\_selectivity > 2 crashes 10.0.15+maria-1wheezy
* [Revision #2330107](https://github.com/MariaDB/server/commit/2330107)\
  2015-02-25 13:26:57 +0200
  * [MDEV-7572](https://jira.mariadb.org/browse/MDEV-7572): InnoDB: Assertion failure in log\_init\_crypt\_key if file\_key\_management\_plugin is used
* [Revision #aa107ef](https://github.com/MariaDB/server/commit/aa107ef)\
  2015-02-25 11:59:00 +0100
  * FIX assert failure when sorting JSON tables
* [Revision #f825b5a](https://github.com/MariaDB/server/commit/f825b5a)\
  2015-02-25 14:13:32 +0400
  * [MDEV-7629](https://jira.mariadb.org/browse/MDEV-7629) Regression: Bit and hex string literals changed column names in 10.0.14
* [Revision #cbf8cdc](https://github.com/MariaDB/server/commit/cbf8cdc)\
  2015-02-25 09:43:31 +0100
  * [MDEV-7530](https://jira.mariadb.org/browse/MDEV-7530) !includedir reads files in random order
* [Revision #e027f5e](https://github.com/MariaDB/server/commit/e027f5e)\
  2015-02-24 23:18:04 +0100
  * Fix [MDEV-7616](https://jira.mariadb.org/browse/MDEV-7616) by adding SQLCOM\_SET\_OPTION to the accepted command list.
* [Revision #6c09a72](https://github.com/MariaDB/server/commit/6c09a72)\
  2015-02-24 20:52:37 +0100
  * Merge remote-tracking branch 'origin/10.0' into 10.0
* [Revision #126523d](https://github.com/MariaDB/server/commit/126523d)\
  2015-02-23 20:53:41 +0100
  * [MDEV-6703](https://jira.mariadb.org/browse/MDEV-6703) Add "mysqlbinlog --binlog-row-event-max-size" support
* [Revision #73033e5](https://github.com/MariaDB/server/commit/73033e5)\
  2015-02-24 09:18:53 +0100
  * fix mroonga to compile w/o performance schema
* [Revision #a227cf8](https://github.com/MariaDB/server/commit/a227cf8)\
  2015-02-24 14:03:14 +0100
  * [MDEV-7335](https://jira.mariadb.org/browse/MDEV-7335): Potential parallel slave deadlock with specific binlog corruption
* [Revision #723be51](https://github.com/MariaDB/server/commit/723be51)\
  2015-02-24 14:17:00 +0100
  * Merge
* [Revision #8799f87](https://github.com/MariaDB/server/commit/8799f87)\
  2015-02-24 10:33:49 +0200
  * [MDEV-7623](https://jira.mariadb.org/browse/MDEV-7623): Add lock wait time and hold time to every record/table lock in InnoDB transaction lock printout.
* [Revision #79e9ff4](https://github.com/MariaDB/server/commit/79e9ff4)\
  2015-02-23 13:37:34 +0100
  * [MDEV-7458](https://jira.mariadb.org/browse/MDEV-7458): Deadlock in parallel replication can allow following transaction to start replicating too early
* [Revision #41cfdc8](https://github.com/MariaDB/server/commit/41cfdc8)\
  2015-02-23 13:36:52 +0100
  * Add error handling on realpath() call.
* [Revision #b5d6aa5](https://github.com/MariaDB/server/commit/b5d6aa5)\
  2015-02-23 13:27:51 +0100
  * [MDEV-7310](https://jira.mariadb.org/browse/MDEV-7310): last\_commit\_pos\_offset set to wrong value after binlog rotate in group commit
* [Revision #90635c6](https://github.com/MariaDB/server/commit/90635c6)\
  2015-02-23 11:24:19 +0200
  * [MDEV-7620](https://jira.mariadb.org/browse/MDEV-7620): Transaction lock wait is missing number of lock waits and total wait time.
* [Revision #f2cb45d](https://github.com/MariaDB/server/commit/f2cb45d)\
  2015-02-22 21:45:24 +0100
  * Merge remote-tracking branch 'origin/10.0' into 10.0
* [Revision #a736e63](https://github.com/MariaDB/server/commit/a736e63)\
  2015-02-22 17:53:02 +0100
  * Add new Json UDF's Json\_Array\_Add, Json\_Array\_Grp and Json\_Object\_Grp.
  * Handle longjmp's raised during json processing.
* [Revision #3653de8](https://github.com/MariaDB/server/commit/3653de8)\
  2015-02-21 19:49:57 +0100
  * test failure on labrador: account for a different errno on Mac OS X
* [Revision #dc94bd0](https://github.com/MariaDB/server/commit/dc94bd0)\
  2015-02-21 12:15:19 +0100
  * [MDEV-7520](https://jira.mariadb.org/browse/MDEV-7520) gtid replication broken during upgrade to debian 10.0.16
* [Revision #0ba1680](https://github.com/MariaDB/server/commit/0ba1680)\
  2015-02-21 10:43:27 +0100
  * [MDEV-6769](https://jira.mariadb.org/browse/MDEV-6769) DROP TRIGGER IF NOT EXIST binlogged on master but not on slave
* [Revision #b739103](https://github.com/MariaDB/server/commit/b739103)\
  2015-02-20 19:01:03 +0100
  * [MDEV-7591](https://jira.mariadb.org/browse/MDEV-7591) master crashed when slave specfied a future position with semi-repl plugin
* [Revision #22cf2f1](https://github.com/MariaDB/server/commit/22cf2f1)\
  2015-02-20 16:37:02 +0100
  * [MDEV-7482](https://jira.mariadb.org/browse/MDEV-7482) VIEW containing INTERVAL(...)
* [Revision #2a798ce](https://github.com/MariaDB/server/commit/2a798ce)\
  2015-02-20 17:45:18 -0500
  * [MDEV-7615](https://jira.mariadb.org/browse/MDEV-7615): Remove --galera-sst-mode option from mysqldump
* [Revision #8366ce4](https://github.com/MariaDB/server/commit/8366ce4)\
  2015-02-20 18:48:29 +0200
  * Fix test failure on labrador.
* [Revision #7b6beef](https://github.com/MariaDB/server/commit/7b6beef)\
  2015-02-20 14:21:27 +0100
  * disable -Werror in MYSQL\_MAINTAINER\_MODE=ON until all plugins are ready
* [Revision #6a1d443](https://github.com/MariaDB/server/commit/6a1d443)\
  2015-02-20 14:10:25 +0100
  * fix after 5.5 merge, debian packaging
* [Revision #775528a](https://github.com/MariaDB/server/commit/775528a)\
  2015-02-20 03:17:46 +0300
  * [MDEV-7220](https://jira.mariadb.org/browse/MDEV-7220): Materialization strategy is not used for REPLACE ... SELECT
* [Revision #77e6e74](https://github.com/MariaDB/server/commit/77e6e74)\
  2015-02-19 22:05:33 +0100
  * merge 10.0-spider
* [Revision #0f8b194](https://github.com/MariaDB/server/commit/0f8b194)\
  2015-02-19 20:54:20 +0300
  * [MDEV-6687](https://jira.mariadb.org/browse/MDEV-6687): Assertion \`0' failed in Protocol::end\_statement on query
* [Revision #cf3b51b](https://github.com/MariaDB/server/commit/cf3b51b)\
  2015-02-20 00:41:26 +0900
  * Merge Spider 3.2.18
* [Revision #004dd0a](https://github.com/MariaDB/server/commit/004dd0a)\
  2015-02-19 15:43:27 +0100
  * [MDEV-7568](https://jira.mariadb.org/browse/MDEV-7568): STOP SLAVE crashes the server
* [Revision #c1ebb4a](https://github.com/MariaDB/server/commit/c1ebb4a)\
  2015-02-19 11:28:03 +0100
  * compiler warnings in spider
* [Revision #16c01c7](https://github.com/MariaDB/server/commit/16c01c7)\
  2015-02-19 10:26:52 +0100
  * after merge: fix mroonga to compile and pass its tests
* [Revision #da63713](https://github.com/MariaDB/server/commit/da63713)\
  2015-02-19 09:57:34 +0100
  * merge 10.0-mroonga
* [Revision #56114a4](https://github.com/MariaDB/server/commit/56114a4)\
  2015-02-19 09:37:11 +0100
  * merge 10.0-connect
* [Revision #d9175f3](https://github.com/MariaDB/server/commit/d9175f3)\
  2015-02-19 01:25:31 +0100
  * Remove GCC warnings
* [Revision #564d41f](https://github.com/MariaDB/server/commit/564d41f)\
  2015-02-19 00:59:02 +0100
  * Work on JSON and JSON UDF's
* [Revision #174bccd](https://github.com/MariaDB/server/commit/174bccd)\
  2015-02-18 20:31:40 +0100
  * xtradb 5.6.22-72.0
* [Revision #6b05688](https://github.com/MariaDB/server/commit/6b05688)\
  2015-02-18 17:59:21 +0100
  * innodb 5.6.23
* [Revision #1645930](https://github.com/MariaDB/server/commit/1645930)\
  2015-02-18 16:20:46 +0100
  * 5.6.23
* [Revision #f37bdd9](https://github.com/MariaDB/server/commit/f37bdd9)\
  2015-02-18 15:18:35 +0100
  * Merge remote-tracking branch 'github/10.0' into 10.0
* [Revision #d7e7862](https://github.com/MariaDB/server/commit/d7e7862)\
  2015-02-18 15:16:27 +0100
  * Merge branch '5.5' into 10.0
* [Revision #dfb001e](https://github.com/MariaDB/server/commit/dfb001e)\
  2015-02-18 13:19:09 +0100
  * percona-server-5.6.22-72.0
* [Revision #865b83e](https://github.com/MariaDB/server/commit/865b83e)\
  2015-02-18 14:07:13 +0200
  * Fixed test failure seen on partition\_innodb\_plugin test case.
* [Revision #2fb81b9](https://github.com/MariaDB/server/commit/2fb81b9)\
  2015-02-18 11:25:59 +0200
  * [MDEV-7408](https://jira.mariadb.org/browse/MDEV-7408): Cannot use a table containing special chars for InnoDB stopwords
* [Revision #63905f1](https://github.com/MariaDB/server/commit/63905f1)\
  2015-02-18 07:28:44 +0200
  * Add forgotten test case change (add more).
* [Revision #a1a32f8](https://github.com/MariaDB/server/commit/a1a32f8)\
  2015-02-18 06:59:28 +0200
  * Revert file space allocation change on row0merge.cc.
* [Revision #44cf4d6](https://github.com/MariaDB/server/commit/44cf4d6)\
  2015-02-17 18:07:56 +0100
  * fix a case where automatic procedure grant was changing user's password
* [Revision #22dae70](https://github.com/MariaDB/server/commit/22dae70)\
  2015-02-17 20:07:12 +0300
  * Added testcase for [MDEV-7193](https://jira.mariadb.org/browse/MDEV-7193): Incorrect Query Result (MySQL Bug 68897) ...
* [Revision #f5dabd7](https://github.com/MariaDB/server/commit/f5dabd7)\
  2015-02-17 13:34:27 +0900
  * Update Mroonga to the latest version on 2015-02-17T13:34:27+0900
* [Revision #fdd6c11](https://github.com/MariaDB/server/commit/fdd6c11)\
  2015-02-13 12:57:11 +0100
  * [MDEV-7419](https://jira.mariadb.org/browse/MDEV-7419) Function cli\_safe\_read not exported
* [Revision #454beee](https://github.com/MariaDB/server/commit/454beee)\
  2015-02-13 11:49:31 +0200
  * [MDEV-6288](https://jira.mariadb.org/browse/MDEV-6288) :Innodb causes server crash after disk full, then can't ALTER TABLE any more
* [Revision #2201aa6](https://github.com/MariaDB/server/commit/2201aa6)\
  2015-02-12 17:23:28 +0100
  * Typo on the jsonudf.cpp name
* [Revision #356ae62](https://github.com/MariaDB/server/commit/356ae62)\
  2015-02-12 15:44:44 +0200
  * Crash during configure without development SSL libraries installed
* [Revision #5dce6aa](https://github.com/MariaDB/server/commit/5dce6aa)\
  2015-02-12 13:14:55 +0100
  * Merge remote-tracking branch 'bzr/5.5' into bb-5.5-merge
* [Revision #ed83905](https://github.com/MariaDB/server/commit/ed83905)\
  2015-02-12 00:23:21 +0100
  * Merge tag 'tokudb-7.5.5' into bb-5.5-merge
* [Revision #8e80f91](https://github.com/MariaDB/server/commit/8e80f91)\
  2015-02-11 23:50:40 +0100
  * Merge remote-tracking branch 'mysql/5.5' into bb-5.5-merge @ mysql-5.5.42
* [Revision #dcfe068](https://github.com/MariaDB/server/commit/dcfe068)\
  2015-02-11 21:39:41 +0100
  * Adding json udf's. Making the second version of json tables.
* [Revision #2a1be9c](https://github.com/MariaDB/server/commit/2a1be9c)\
  2015-02-11 20:40:56 +0100
  * XtraDB 5.5.41-37.0
* [Revision #13927f8](https://github.com/MariaDB/server/commit/13927f8)\
  2015-02-11 18:32:40 +0100
  * percona-server-5.5.41-37.0
* [Revision #d996dc2](https://github.com/MariaDB/server/commit/d996dc2)\
  2015-02-11 15:02:15 +0100
  * [MDEV-7290](https://jira.mariadb.org/browse/MDEV-7290) please update MSI installer to include HeidiSQL 9.1
* [Revision #56da625](https://github.com/MariaDB/server/commit/56da625)\
  2015-02-10 15:15:27 +0200
  * Improve InnoDB transaction lock output by providing number of table locks this transaction is currently holding and total number of table locks to the table where lock is held.
* [Revision #a257801](https://github.com/MariaDB/server/commit/a257801)\
  2015-02-10 16:01:03 +0400
  * Fixing compilation failure in storage/connect when -DMYSQL\_MAINTAINER\_MODE=ON: disabling some CXX errors in storage/connect/CMakeLists.txt.
* [Revision #63108dc](https://github.com/MariaDB/server/commit/63108dc)\
  2015-02-10 12:26:21 +0100
  * Fix the tree to work in git. Backport corresponing 10.1 changes.
* [Revision #7588424](https://github.com/MariaDB/server/commit/7588424)\
  2015-02-10 10:19:42 +0100
  * restore a cross-compiling bit that was lost in a merge
* [Revision #48e7c19](https://github.com/MariaDB/server/commit/48e7c19)\
  2015-02-10 09:41:54 +0200
  * Fix test failure innodb-mdev7046 on Windows. Test causes OS error printout from InnoDB.
* [Revision #a34fd50](https://github.com/MariaDB/server/commit/a34fd50)\
  2015-02-09 20:53:36 +0100
  * [MDEV-7478](https://jira.mariadb.org/browse/MDEV-7478) log-basename unpredictable behavior in standalone mode
* [Revision #f007f82](https://github.com/MariaDB/server/commit/f007f82)\
  2015-02-09 20:53:28 +0100
  * [MDEV-7351](https://jira.mariadb.org/browse/MDEV-7351) 5.5 build fails on Ubuntu Utopic in buildbot
* [Revision #c233d6e](https://github.com/MariaDB/server/commit/c233d6e)\
  2015-02-11 01:26:50 +0100
  * [MDEV-7260](https://jira.mariadb.org/browse/MDEV-7260): Crash in get\_best\_combination when executing multi-table UPDATE with nested views
* [Revision #cfb7d5d](https://github.com/MariaDB/server/commit/cfb7d5d)\
  2015-02-10 16:16:31 +0400
  * [MDEV-7516](https://jira.mariadb.org/browse/MDEV-7516) Assertion \`!cur\_p->event' failed in Gcalc\_scan\_iterator::arrange\_event(int, int). When the distance in ST\_BUFFER is too far negative the coordinates can run out of the operational area. We should just return an empty geometry in this case.
* [Revision #552f1b3](https://github.com/MariaDB/server/commit/552f1b3)\
  2015-02-10 14:17:23 +0200
  * Fix test failures on innodb-[MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055) and innodb-[MDEV-7513](https://jira.mariadb.org/browse/MDEV-7513).
* [Revision #ada0743](https://github.com/MariaDB/server/commit/ada0743)\
  2015-02-10 08:08:59 +0200
  * Fix test failure on innodb-[MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055).
* [Revision #44a9e3f](https://github.com/MariaDB/server/commit/44a9e3f)\
  2015-02-09 16:14:27 +0200
  * [MDEV-7139](https://jira.mariadb.org/browse/MDEV-7139): Sporadic failure in innodb.innodb\_corrupt\_bit on P8
* [Revision #3c097fd](https://github.com/MariaDB/server/commit/3c097fd)\
  2015-02-08 19:47:26 +0100
  * Remove some GCC warnings
* [Revision #919f40e](https://github.com/MariaDB/server/commit/919f40e)\
  2015-02-08 22:38:19 +0400
  * Audit plugin v1.2.0.
* [Revision #96ba1f1](https://github.com/MariaDB/server/commit/96ba1f1)\
  2015-02-08 18:17:29 +0100
  * Handle the use of date/time values when making queries for MYSQL or ODBC. Was raised by 7549.
* [Revision #0d73bc1](https://github.com/MariaDB/server/commit/0d73bc1)\
  2015-02-08 15:47:00 +0300
  * [MDEV-7519](https://jira.mariadb.org/browse/MDEV-7519) debian / ubuntu packaging creation of plugin table (if not exists)
* [Revision #35548d5](https://github.com/MariaDB/server/commit/35548d5)\
  2015-02-07 11:33:52 +0100
  * Modify the connect\_type\_conv and connect\_conv\_size variables. They were global (read-only) now they are session (not read-only)
* [Revision #b9d616c](https://github.com/MariaDB/server/commit/b9d616c)\
  2015-02-06 15:49:45 +0400
  * [MDEV-7435](https://jira.mariadb.org/browse/MDEV-7435) Windows debug: Run-Time Check Failure #3 The variable 'unused' is being used without being initialized. Fixed as it's done in 10.0.
* [Revision #ffd2996](https://github.com/MariaDB/server/commit/ffd2996)\
  2015-02-05 21:46:04 -0800
  * Merge
* [Revision #587c720](https://github.com/MariaDB/server/commit/587c720)\
  2015-02-05 20:09:08 -0800
  * Fixed bug [MDEV-7316](https://jira.mariadb.org/browse/MDEV-7316). The function table\_cond\_selectivity() should take into account that condition selectivity for some fields can be set to 0.
* [Revision #5c6eb52](https://github.com/MariaDB/server/commit/5c6eb52)\
  2015-02-04 16:50:29 +0200
  * Fix test failure.
* [Revision #8cc9751](https://github.com/MariaDB/server/commit/8cc9751)\
  2015-02-04 14:40:46 +0200
  * [MDEV-7538](https://jira.mariadb.org/browse/MDEV-7538): Wrong constraint (TINYINT or MEDIUMINT and INT) causes server crash
* [Revision #422ffe9](https://github.com/MariaDB/server/commit/422ffe9)\
  2015-02-04 11:12:46 +0200
  * InnoDB and XtraDB produce different output on [MDEV-7513](https://jira.mariadb.org/browse/MDEV-7513).
* [Revision #f320915](https://github.com/MariaDB/server/commit/f320915)\
  2015-02-04 10:50:16 +0200
  * [MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055): MySQL#74664 InnoDB: Failing assertion: len <= col->len || col->mtype == 5 || (col->len == 0 && col->mtype == 1) in file rem0rec.cc line 845
* [Revision #7afbf33](https://github.com/MariaDB/server/commit/7afbf33)\
  2015-02-04 09:29:54 +0200
  * [MDEV-7513](https://jira.mariadb.org/browse/MDEV-7513): ib\_warn\_row\_too\_big dereferences null thd
* [Revision #22367ba](https://github.com/MariaDB/server/commit/22367ba)\
  2015-02-02 19:34:35 +0100
  * Add or correct some tracing code
* [Revision #82f2be6](https://github.com/MariaDB/server/commit/82f2be6)\
  2015-02-02 15:35:58 +0100
  * Fix a bug causing Insert into ODBC to fail when the column name is UTF8 encoded.
* [Revision #6a78371](https://github.com/MariaDB/server/commit/6a78371)\
  2015-02-01 12:16:30 +0100
  * Fix a bug causing UseCnc not being initialized for ODBC catalog tables. This made errors by calling SQLConnect or SQLDriverConnect randomly with incorrect parameters.
* [Revision #180b2be](https://github.com/MariaDB/server/commit/180b2be)\
  2015-01-31 15:05:43 +0100
  * Add the possibility to establish an ODBC connection via SQLConnect (the default being still to use SQLDriverConnect)
* [Revision #fd1ca70](https://github.com/MariaDB/server/commit/fd1ca70)\
  2015-01-30 10:57:00 +0100
  * Enhance JSON tables handling.
* [Revision #9a2dc7d](https://github.com/MariaDB/server/commit/9a2dc7d)\
  2015-01-28 00:19:39 +0100
  * Repair the errors due to the PRXCOL Init function that must be called with 2 parameters. (previously the second one was optional)
* [Revision #ee5a4c8](https://github.com/MariaDB/server/commit/ee5a4c8)\
  2015-01-27 19:18:51 +0100
  * Begin eliminating on Linux OverloadedVirtual warnings. However some tests failed. Going to windows to try tracing them.
* [Revision #e7802bf](https://github.com/MariaDB/server/commit/e7802bf)\
  2015-01-27 12:50:50 +0100
  * Fix a bug causing the connection string of a partition table not being edited with the partition name when it was specified in the OPTION\_LIST.
* [Revision #162446a](https://github.com/MariaDB/server/commit/162446a)\
  2015-01-27 10:46:41 +0900
  * Merge from trunk
* [Revision #5b460c6](https://github.com/MariaDB/server/commit/5b460c6)\
  2015-01-24 12:17:03 +0100
  * Protect AllocateValue against a null sp.
* [Revision #7ebd3f6](https://github.com/MariaDB/server/commit/7ebd3f6)\
  2015-01-24 11:54:12 +0100
  * Commit merged files (just changing some ending CRLF to LF)
* [Revision #dbf690b](https://github.com/MariaDB/server/commit/dbf690b)\
  2015-01-24 11:46:18 +0100
  * Fix correctly [MDEV-7498](https://jira.mariadb.org/browse/MDEV-7498). The problem was not in AllocateValue but in the constructor of TYPVAL The new strg was widely uninitialised just by setting a terminated null char. Now the whole string is zero'ed. In Tabjson JSONCOL::ParseJpath, the original code was restored.
* [Revision #a87bb05](https://github.com/MariaDB/server/commit/a87bb05)\
  2015-01-23 23:14:34 +0100
  * Change some line endings from CRLF to LF
* [Revision #2cd36ad](https://github.com/MariaDB/server/commit/2cd36ad)\
  2015-01-23 21:54:29 +0100
  * This to fix [MDEV-7498](https://jira.mariadb.org/browse/MDEV-7498). All changes made to AllocateValue to be sure that the sp and p variable be initialised failed. Not understanding what causes this valgrind warning, I finally changed the way Mulval is allocated just to avoid it. This is a BAD solution as it does not really fix the problem but just hide it. This will have to be re-considered.
* [Revision #dc091a2](https://github.com/MariaDB/server/commit/dc091a2)\
  2015-01-23 17:54:53 +0100
  * Fix [MDEV-7489](https://jira.mariadb.org/browse/MDEV-7489) (in add\_field)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
