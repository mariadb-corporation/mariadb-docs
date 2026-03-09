# MariaDB 10.2.6 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.6)[Release Notes](../../old-releases/10.2/10.2.6.md)[Changelog](mariadb-1026-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 23 May 2017

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.6.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #ca7cf69cb1](https://github.com/MariaDB/server/commit/ca7cf69cb1)\
  2017-05-15 02:09:28 +0300
  * Additions to 10.2.6 unstable-tests list
* [Revision #f9069a3dc0](https://github.com/MariaDB/server/commit/f9069a3dc0)\
  2017-05-12 15:44:17 +0300
  * [MDEV-12674](https://jira.mariadb.org/browse/MDEV-12674) Post-merge fix: Include accidentally omitted changes
* Merge [Revision #b9474b5d51](https://github.com/MariaDB/server/commit/b9474b5d51) 2017-05-12 13:29:24 +0300 - Merge 10.1 into 10.2
* Merge [Revision #03dca7a333](https://github.com/MariaDB/server/commit/03dca7a333) 2017-05-12 13:12:45 +0300 - Merge 10.0 into 10.1
* [Revision #ff16609374](https://github.com/MariaDB/server/commit/ff16609374)\
  2017-05-11 21:12:37 +0300
  * [MDEV-12674](https://jira.mariadb.org/browse/MDEV-12674) Innodb\_row\_lock\_current\_waits has overflow
* [Revision #d7cfe2c4f3](https://github.com/MariaDB/server/commit/d7cfe2c4f3)\
  2017-05-09 13:40:42 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253) post-fix: Do not leak memory in crash recovery
* [Revision #9d2c1d09aa](https://github.com/MariaDB/server/commit/9d2c1d09aa)\
  2017-05-06 23:10:52 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253) post-push fix: buf\_read\_page\_low() can return DB\_ERROR
* [Revision #9933239956](https://github.com/MariaDB/server/commit/9933239956)\
  2017-05-11 17:28:47 +0300
  * [MDEV-10804](https://jira.mariadb.org/browse/MDEV-10804) main.stat\_tables\_par fails sporadically in buildbot
* [Revision #1fbf1c6d7c](https://github.com/MariaDB/server/commit/1fbf1c6d7c)\
  2017-05-11 17:08:40 +0300
  * Build MyRocks as a plugin (as static compilation doesn't work)
* [Revision #f4df8c00c9](https://github.com/MariaDB/server/commit/f4df8c00c9)\
  2017-05-10 23:13:06 +0300
  * [MDEV-11197](https://jira.mariadb.org/browse/MDEV-11197): TrxInInnoDB::is\_aborted(const trx\_t\*): Assertion \`srv\_read\_only\_mode || trx->in\_depth > 0' failed
* [Revision #00821c3825](https://github.com/MariaDB/server/commit/00821c3825)\
  2017-05-10 15:13:11 +0300
  * [MDEV-12776](https://jira.mariadb.org/browse/MDEV-12776) Do not create the InnoDB temporary tablespace in innodb\_read\_only mode
* [Revision #fee8d39ecb](https://github.com/MariaDB/server/commit/fee8d39ecb)\
  2017-05-10 17:10:28 +0200
  * [MDEV-12754](https://jira.mariadb.org/browse/MDEV-12754) innodb.truncate\_debug fails in buildbot with embedded due to semaphore wait
* [Revision #2819133711](https://github.com/MariaDB/server/commit/2819133711)\
  2017-05-10 17:57:40 +0200
  * fix 32 bit platform test
* [Revision #535f489210](https://github.com/MariaDB/server/commit/535f489210)\
  2017-05-10 14:03:59 +0200
  * update to the latest C/C to fix failures on Windows
* [Revision #8cec525644](https://github.com/MariaDB/server/commit/8cec525644)\
  2017-05-10 13:40:41 +0200
  * skip innodb.innodb\_xtradb\_compat on Windows
* [Revision #3a906ca982](https://github.com/MariaDB/server/commit/3a906ca982)\
  2017-05-10 14:31:57 +0300
  * [MDEV-12708](https://jira.mariadb.org/browse/MDEV-12708) innodb.truncate\_purge\_debug fails sporadically in buildbot
* [Revision #e3a7f75aef](https://github.com/MariaDB/server/commit/e3a7f75aef)\
  2017-05-10 14:14:50 +0300
  * [MDEV-12679](https://jira.mariadb.org/browse/MDEV-12679) purge\_sys\_t::purge\_sys\_t(): Assertion \`latch.magic\_n == 0' failed on --bootstrap (CMAKE\_BUILD\_TYPE=Debug)
* [Revision #021d636551](https://github.com/MariaDB/server/commit/021d636551)\
  2017-05-10 09:07:50 +0300
  * Fix some integer type mismatch.
* [Revision #2e41259bfc](https://github.com/MariaDB/server/commit/2e41259bfc)\
  2017-05-10 09:06:03 +0200
  * Fix of emulated variables comments to reflect reality.
* [Revision #069d0472b3](https://github.com/MariaDB/server/commit/069d0472b3)\
  2017-05-10 00:11:52 +0300
  * [MDEV-12762](https://jira.mariadb.org/browse/MDEV-12762) Some files in current 10.2 tree seem to be reverted to an old state
* [Revision #2980b0c348](https://github.com/MariaDB/server/commit/2980b0c348)\
  2017-05-10 01:28:01 +0200
  * fix crashes with openssl fips builds
* [Revision #bde397b3eb](https://github.com/MariaDB/server/commit/bde397b3eb)\
  2017-05-10 01:57:54 +0300
  * List of unstable tests for 10.2.6 (initial 10.2 version for GA)
* [Revision #001e54af70](https://github.com/MariaDB/server/commit/001e54af70)\
  2017-05-10 01:56:23 +0300
  * Disable RocksDB tests that fail regularly on buildbot ([MDEV-12474](https://jira.mariadb.org/browse/MDEV-12474))
* [Revision #b5b7874186](https://github.com/MariaDB/server/commit/b5b7874186)\
  2017-05-10 00:46:09 +0200
  * Update C/C (fix build on Windows)
* [Revision #588a6a186a](https://github.com/MariaDB/server/commit/588a6a186a)\
  2017-05-09 17:23:08 +0300
  * [MDEV-12750](https://jira.mariadb.org/browse/MDEV-12750) Fix crash recovery of key rotation
* [Revision #6322913339](https://github.com/MariaDB/server/commit/6322913339)\
  2017-05-04 09:12:00 +0300
  * [MDEV-12472](https://jira.mariadb.org/browse/MDEV-12472): InnoDB should accept XtraDB parameters, warning that they are ignored
* [Revision #96987cb4e9](https://github.com/MariaDB/server/commit/96987cb4e9)\
  2017-05-02 13:00:15 +0300
  * Added tests for [MDEV-11724](https://jira.mariadb.org/browse/MDEV-11724), [MDEV-11725](https://jira.mariadb.org/browse/MDEV-11725), [MDEV-11726](https://jira.mariadb.org/browse/MDEV-11726).
* [Revision #ccca4f43c9](https://github.com/MariaDB/server/commit/ccca4f43c9)\
  2017-05-03 21:22:59 +0200
  * [MDEV-10332](https://jira.mariadb.org/browse/MDEV-10332) support for OpenSSL 1.1 and LibreSSL
* [Revision #f8866f8f66](https://github.com/MariaDB/server/commit/f8866f8f66)\
  2017-03-08 17:39:47 +0100
  * [MDEV-10332](https://jira.mariadb.org/browse/MDEV-10332) support for OpenSSL 1.1 and LibreSSL
* [Revision #eb2b7ff623](https://github.com/MariaDB/server/commit/eb2b7ff623)\
  2017-05-09 18:32:36 +0200
  * update C/C
* [Revision #0ca2be92e6](https://github.com/MariaDB/server/commit/0ca2be92e6)\
  2017-05-09 17:32:52 +0300
  * Fix test failure on Windows.
* [Revision #2e2e0d9105](https://github.com/MariaDB/server/commit/2e2e0d9105)\
  2017-04-03 11:55:51 +0530
  * [MDEV-12019](https://jira.mariadb.org/browse/MDEV-12019) FLASHBACK: Server crashes in bitmap\_bits\_set / pack\_row / ...
* Merge [Revision #c91ecf9e9b](https://github.com/MariaDB/server/commit/c91ecf9e9b) 2017-05-09 13:24:52 +0200 - Merge branch '10.1' into 10.2
* Merge [Revision #c92168fcd2](https://github.com/MariaDB/server/commit/c92168fcd2) 2017-05-09 12:40:48 +0300 - Merge pull request #389 from iangilfillan/10.1
* [Revision #44eca0f512](https://github.com/MariaDB/server/commit/44eca0f512)\
  2017-05-09 11:24:22 +0200
  * galera\_new\_cluster man page and sh typo
* [Revision #fbdf18f86e](https://github.com/MariaDB/server/commit/fbdf18f86e)\
  2017-05-08 19:23:39 +0200
  * [MDEV-12696](https://jira.mariadb.org/browse/MDEV-12696) Crash with LOAD XML and non-updatable VIEW column
* Merge [Revision #d738722eee](https://github.com/MariaDB/server/commit/d738722eee) 2017-05-08 14:58:49 +0200 - Merge branch '10.0' into 10.1
* Merge [Revision #1c418df722](https://github.com/MariaDB/server/commit/1c418df722) 2017-05-08 12:12:48 +0200 - Merge branch '5.5' into 10.0
* [Revision #15f9931f6d](https://github.com/MariaDB/server/commit/15f9931f6d)\
  2017-05-04 22:45:32 -0700
  * Fixed the bug [MDEV-12673](https://jira.mariadb.org/browse/MDEV-12673).
* [Revision #14fca28ea4](https://github.com/MariaDB/server/commit/14fca28ea4)\
  2017-05-02 19:11:21 -0400
  * bump the VERSION
* [Revision #dbe2c3c5f2](https://github.com/MariaDB/server/commit/dbe2c3c5f2)\
  2017-04-30 13:29:56 +1000
  * mysqld\_safe\_help - remove warning
* [Revision #fc25437aff](https://github.com/MariaDB/server/commit/fc25437aff)\
  2017-05-05 13:08:23 +0300
  * [MDEV-10104](https://jira.mariadb.org/browse/MDEV-10104) Table lock race condition with replication
* [Revision #e3521ab904](https://github.com/MariaDB/server/commit/e3521ab904)\
  2017-05-05 13:03:41 +0300
  * Fixed some bugs in fork\_big.pl which caused some tests to die early
* [Revision #bc5c1d9970](https://github.com/MariaDB/server/commit/bc5c1d9970)\
  2017-05-05 14:04:18 +0300
  * [MDEV-12635](https://jira.mariadb.org/browse/MDEV-12635) innodb.log\_file\_size fails when run with Valgrind
* [Revision #a7c5fd6b4e](https://github.com/MariaDB/server/commit/a7c5fd6b4e)\
  2017-05-03 15:49:19 +0200
  * restore dependencies, removed in f2dc04abea
* [Revision #e1efeaa550](https://github.com/MariaDB/server/commit/e1efeaa550)\
  2017-05-08 12:04:08 +0300
  * [MDEV-12628](https://jira.mariadb.org/browse/MDEV-12628): innodb.innodb\_bug14147491 sporadically fails in buildbot due to wrong error number
* [Revision #57e667357a](https://github.com/MariaDB/server/commit/57e667357a)\
  2017-05-08 11:23:02 +0300
  * [MDEV-12627](https://jira.mariadb.org/browse/MDEV-12627): innodb.innodb\_bug14147491 does not do proper cleanup
* [Revision #c7d85db1c4](https://github.com/MariaDB/server/commit/c7d85db1c4)\
  2017-05-06 01:55:45 +0200
  * Fix AWS key managemennt compile error on Linux
* [Revision #13752faa4d](https://github.com/MariaDB/server/commit/13752faa4d)\
  2017-05-05 16:37:00 +0000
  * Fix compilation of aws\_key\_management plugin
* [Revision #bc6426e44d](https://github.com/MariaDB/server/commit/bc6426e44d)\
  2017-05-02 19:10:01 -0400
  * bump the VERSION
* Merge [Revision #63e4be267b](https://github.com/MariaDB/server/commit/63e4be267b) 2017-05-02 16:31:24 +0300 - Merge pull request #362 from grooverdan/10.1-MDEV-XXXX-mysqltest-replace-regex-vars
* [Revision #bbef745574](https://github.com/MariaDB/server/commit/bbef745574)\
  2017-04-13 00:19:08 +1000
  * tests: sys\_vars.sysvars\_wsrep
* [Revision #d59b94e7fd](https://github.com/MariaDB/server/commit/d59b94e7fd)\
  2017-04-13 16:14:21 +1000
  * Add replace\_regex to not ignore the regex in "$var /regex/val/"
* Merge [Revision #2d457843d6](https://github.com/MariaDB/server/commit/2d457843d6) 2017-05-02 16:29:40 +0300 - Merge pull request #375 from grooverdan/10.1-galera\_new\_cluster--help
* [Revision #a9a38fcd7a](https://github.com/MariaDB/server/commit/a9a38fcd7a)\
  2017-04-30 14:47:34 +1000
  * wsrep\_new\_cluster: Add -h and --help options
* Merge [Revision #6b8225ffe6](https://github.com/MariaDB/server/commit/6b8225ffe6) 2017-05-02 16:28:25 +0300 - Merge pull request #371 from grooverdan/10.1-wsrep-this\_not\_null
* [Revision #3d4882feb2](https://github.com/MariaDB/server/commit/3d4882feb2)\
  2017-04-30 13:58:18 +1000
  * Remove compile warning - "this" canot be null
* [Revision #acce1f37c2](https://github.com/MariaDB/server/commit/acce1f37c2)\
  2017-05-02 08:09:16 +0300
  * [MDEV-12624](https://jira.mariadb.org/browse/MDEV-12624): encryption.innodb\_encryption\_tables fails in buildbot with timeout
* [Revision #935a1c676e](https://github.com/MariaDB/server/commit/935a1c676e)\
  2017-04-29 10:05:39 +0300
  * [MDEV-12623](https://jira.mariadb.org/browse/MDEV-12623): InnoDB: Failing assertion: kv == 0
* [Revision #57795bb436](https://github.com/MariaDB/server/commit/57795bb436)\
  2017-04-29 07:18:25 +0300
  * Updated list of unstable tests for 10.1.23
* Merge [Revision #e74f2e2b86](https://github.com/MariaDB/server/commit/e74f2e2b86) 2017-04-28 20:19:32 +0200 - Merge branch '10.0' 10.1
* Merge [Revision #49552cf1f7](https://github.com/MariaDB/server/commit/49552cf1f7) 2017-04-25 16:30:39 +0200 - Merge branch '5.5' into bb-10.0-merge-5.5
* [Revision #2e7ba70a94](https://github.com/MariaDB/server/commit/2e7ba70a94)\
  2017-04-22 10:30:55 -0700
  * Fixed the bug [MDEV-10693](https://jira.mariadb.org/browse/MDEV-10693).
* [Revision #57fea99eeb](https://github.com/MariaDB/server/commit/57fea99eeb)\
  2017-04-24 16:42:35 +0300
  * Add and adjust a test from MySQL:
* [Revision #864548c4ec](https://github.com/MariaDB/server/commit/864548c4ec)\
  2017-04-24 13:40:36 +0300
  * Add and adjust a test from MySQL:
* [Revision #fac2a7a85d](https://github.com/MariaDB/server/commit/fac2a7a85d)\
  2017-04-22 22:51:43 +0400
  * [MDEV-12495](https://jira.mariadb.org/browse/MDEV-12495) Conditional jump depends on uninitialised value for: SELECT NULL UNION geom\_expression
* [Revision #97fb1f2679](https://github.com/MariaDB/server/commit/97fb1f2679)\
  2017-04-21 14:34:24 -0700
  * Fixed bug [MDEV-10053](https://jira.mariadb.org/browse/MDEV-10053).
* [Revision #26ed68dcae](https://github.com/MariaDB/server/commit/26ed68dcae)\
  2017-04-18 16:28:14 +0200
  * fix "cmake -DWITH\_PCRE=bundled"
* Merge [Revision #8d75a7533e](https://github.com/MariaDB/server/commit/8d75a7533e) 2017-04-21 18:34:06 +0200 - Merge branch '5.5' into 10.0
* [Revision #c6ee3fe9d4](https://github.com/MariaDB/server/commit/c6ee3fe9d4)\
  2017-04-19 20:31:05 +0200
  * respect client's desire to force ssl even when WITH\_SSL=NO
* [Revision #4fe65ca33a](https://github.com/MariaDB/server/commit/4fe65ca33a)\
  2017-04-18 12:35:05 +0200
  * [MDEV-12230](https://jira.mariadb.org/browse/MDEV-12230) include/my\_sys.h:600:43: error: unknown type name ‘PSI\_file\_key’" when -DWITHOUT\_SERVER=1
* [Revision #0001049be0](https://github.com/MariaDB/server/commit/0001049be0)\
  2017-04-18 11:36:11 +0200
  * [MDEV-12276](https://jira.mariadb.org/browse/MDEV-12276) Missing DBUG\_RETURN or DBUG\_VOID\_RETURN macro in function "do\_exec"
* [Revision #036b689f18](https://github.com/MariaDB/server/commit/036b689f18)\
  2017-04-18 11:29:02 +0200
  * [MDEV-12310](https://jira.mariadb.org/browse/MDEV-12310) openat(, ...O\_EXEC) fails on Illumos / Solaris
* [Revision #786363e89b](https://github.com/MariaDB/server/commit/786363e89b)\
  2017-04-18 10:29:59 +0200
  * compiler warning
* [Revision #39f1917f46](https://github.com/MariaDB/server/commit/39f1917f46)\
  2016-09-10 20:42:20 +0200
  * Attempt to fix strange rpm dependency issue following prior patch
* [Revision #d185f1d68b](https://github.com/MariaDB/server/commit/d185f1d68b)\
  2017-04-19 14:30:52 +0200
  * Fix use of `require` in mysql-test-run.
* [Revision #d53b541389](https://github.com/MariaDB/server/commit/d53b541389)\
  2017-04-13 09:35:57 -0400
  * bump the VERSION
* Merge [Revision #663068c6ee](https://github.com/MariaDB/server/commit/663068c6ee) 2017-04-11 10:18:04 -0400 - Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #5c579482eb](https://github.com/MariaDB/server/commit/5c579482eb)\
  2017-04-07 16:25:02 -0700
  * Adjusted test results after the fix for [MDEV-12429](https://jira.mariadb.org/browse/MDEV-12429).
* [Revision #b0395d8701](https://github.com/MariaDB/server/commit/b0395d8701)\
  2017-04-04 10:04:52 -0700
  * Fixed the bug [MDEV-12429](https://jira.mariadb.org/browse/MDEV-12429) and its duplicates [MDEV-12145](https://jira.mariadb.org/browse/MDEV-12145) and [MDEV-9886](https://jira.mariadb.org/browse/MDEV-9886).
* [Revision #2645bda5f2](https://github.com/MariaDB/server/commit/2645bda5f2)\
  2017-05-09 13:40:42 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253) post-fix: Do not leak memory in crash recovery
* [Revision #56b3bcc812](https://github.com/MariaDB/server/commit/56b3bcc812)\
  2017-05-08 18:02:46 +0530
  * [MDEV-12290](https://jira.mariadb.org/browse/MDEV-12290) Wrong timestamps in binary log causes replication issues
* [Revision #b3939a35aa](https://github.com/MariaDB/server/commit/b3939a35aa)\
  2017-05-09 11:41:35 +0300
  * [MDEV-12720](https://jira.mariadb.org/browse/MDEV-12720) recovery fails with "Generic error" for ROW\_FORMAT=compressed
* [Revision #d0ce870466](https://github.com/MariaDB/server/commit/d0ce870466)\
  2017-05-09 10:55:17 +0300
  * [MDEV-12735](https://jira.mariadb.org/browse/MDEV-12735): Accidental revert of [MDEV-6933](https://jira.mariadb.org/browse/MDEV-6933)
* [Revision #e8889c8002](https://github.com/MariaDB/server/commit/e8889c8002)\
  2017-05-09 10:00:49 +0300
  * [MDEV-12745](https://jira.mariadb.org/browse/MDEV-12745) InnoDB Assertion \`0' failed at row0umod.cc:1181
* Merge [Revision #9a73af0152](https://github.com/MariaDB/server/commit/9a73af0152) 2017-05-09 09:35:11 +0300 - Merge pull request #388 from grooverdan/10.2-[MDEV-8684](https://jira.mariadb.org/browse/MDEV-8684)-innobase-remove-maths
* [Revision #015966d2ce](https://github.com/MariaDB/server/commit/015966d2ce)\
  2017-05-09 12:06:24 +1000
  * [MDEV-8684](https://jira.mariadb.org/browse/MDEV-8684): innodb ut\_delay - no maths
* [Revision #b246993cfc](https://github.com/MariaDB/server/commit/b246993cfc)\
  2017-05-09 08:23:24 +0300
  * [MDEV-12706](https://jira.mariadb.org/browse/MDEV-12706): !trx->declared\_to\_be\_inside\_innodb with innodb\_thread\_concurrency during CREATE .. SELECT
* [Revision #0627a0f399](https://github.com/MariaDB/server/commit/0627a0f399)\
  2017-05-08 17:01:38 +0300
  * [MDEV-12586](https://jira.mariadb.org/browse/MDEV-12586) ALTER TABLE…ALGORITHM=INPLACE fails with non-constant DEFAULT values
* [Revision #85ea327727](https://github.com/MariaDB/server/commit/85ea327727)\
  2017-05-08 22:06:32 +0300
  * Disable the innodb\_defragment tests until [MDEV-11336](https://jira.mariadb.org/browse/MDEV-11336) is done
* [Revision #844a575946](https://github.com/MariaDB/server/commit/844a575946)\
  2017-05-08 12:26:23 +0300
  * [MDEV-12449](https://jira.mariadb.org/browse/MDEV-12449): Debian Packaging AWS key management plugin
* [Revision #d049a560bc](https://github.com/MariaDB/server/commit/d049a560bc)\
  2017-05-08 21:19:26 +0530
  * [MDEV-12319](https://jira.mariadb.org/browse/MDEV-12319) Fix galera test failures
* [Revision #8773f14677](https://github.com/MariaDB/server/commit/8773f14677)\
  2017-05-08 16:14:04 +0300
  * Disable defragmentation support for now.
* [Revision #f0eb8f153d](https://github.com/MariaDB/server/commit/f0eb8f153d)\
  2017-05-08 12:04:08 +0300
  * [MDEV-12628](https://jira.mariadb.org/browse/MDEV-12628): innodb.innodb\_bug14147491 sporadically fails in buildbot due to wrong error number
* [Revision #1e227d8880](https://github.com/MariaDB/server/commit/1e227d8880)\
  2017-05-08 11:23:02 +0300
  * [MDEV-12627](https://jira.mariadb.org/browse/MDEV-12627): innodb.innodb\_bug14147491 does not do proper cleanup
* [Revision #d53eb85997](https://github.com/MariaDB/server/commit/d53eb85997)\
  2017-05-06 14:00:19 +0200
  * [MDEV-12580](https://jira.mariadb.org/browse/MDEV-12580) Wrong query result in join when using an index (Version > "10.2.3")
* [Revision #d6d7e169fb](https://github.com/MariaDB/server/commit/d6d7e169fb)\
  2017-05-03 15:42:35 +0200
  * [MDEV-12669](https://jira.mariadb.org/browse/MDEV-12669) Circular foreign keys cause a loop and OOM upon LOCK TABLE
* Merge [Revision #2b29c52ea8](https://github.com/MariaDB/server/commit/2b29c52ea8) 2017-05-07 23:42:59 +0000 - Merge branch '10.2' of github.com:MariaDB/server into bb-10.2-mariarocks
* [Revision #3f5a8cbe12](https://github.com/MariaDB/server/commit/3f5a8cbe12)\
  2017-05-06 23:10:52 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253) post-push fix: buf\_read\_page\_low() can return DB\_ERROR
* [Revision #8f05c848c5](https://github.com/MariaDB/server/commit/8f05c848c5)\
  2017-05-05 13:32:01 +0300
  * [MDEV-10541](https://jira.mariadb.org/browse/MDEV-10541): Faking the version string only works with MariaDB-Clients
* [Revision #c22ef4df26](https://github.com/MariaDB/server/commit/c22ef4df26)\
  2017-05-06 15:54:31 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253) post-merge fix: Use accessors for dict\_table\_t::file\_unreadable
* [Revision #6c91be54b1](https://github.com/MariaDB/server/commit/6c91be54b1)\
  2017-05-06 15:50:09 +0300
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) Properly retry posix\_fallocate() on EINTR
* Merge [Revision #14c6f00a9f](https://github.com/MariaDB/server/commit/14c6f00a9f) 2017-05-06 14:36:46 +0300 - Merge 10.1 into 10.2
* [Revision #b82c602db5](https://github.com/MariaDB/server/commit/b82c602db5)\
  2017-04-28 03:20:49 +0300
  * [MDEV-12602](https://jira.mariadb.org/browse/MDEV-12602) InnoDB: Failing assertion: space->n\_pending\_ops == 0
* [Revision #6935d66053](https://github.com/MariaDB/server/commit/6935d66053)\
  2017-04-26 21:58:21 +0200
  * [MDEV-12591](https://jira.mariadb.org/browse/MDEV-12591) MariaDB embedded server refuses start with innodb\_plugin
* [Revision #1b27c25473](https://github.com/MariaDB/server/commit/1b27c25473)\
  2017-04-25 23:00:58 +0200
  * [MDEV-10594](https://jira.mariadb.org/browse/MDEV-10594) SSL hostname verification fails for SubjectAltNames
* [Revision #b8c8405008](https://github.com/MariaDB/server/commit/b8c8405008)\
  2017-04-26 17:55:27 +0200
  * cleanup: simplify setting of ssl\* options in my.cnf templates
* [Revision #0636637e37](https://github.com/MariaDB/server/commit/0636637e37)\
  2017-04-25 22:55:27 +0200
  * regenerate SSL certificates again
* [Revision #c0e24cd0e8](https://github.com/MariaDB/server/commit/c0e24cd0e8)\
  2017-04-20 22:43:58 +0200
  * compiler warnings
* [Revision #f21dcd9933](https://github.com/MariaDB/server/commit/f21dcd9933)\
  2017-04-20 20:12:16 +0200
  * .gitignore mariadb-backup
* [Revision #4e07fc0ab5](https://github.com/MariaDB/server/commit/4e07fc0ab5)\
  2017-04-21 00:50:53 +0200
  * test failure
* [Revision #e8bc838eb9](https://github.com/MariaDB/server/commit/e8bc838eb9)\
  2017-04-20 19:23:07 +0000
  * mariadb-backup - do not extend innodb tablespaces in prepare, unless incremental prepare is running.
* [Revision #ecb25df21b](https://github.com/MariaDB/server/commit/ecb25df21b)\
  2017-04-19 13:09:03 +0000
  * Xtrabackup 2.3.8
* [Revision #c8ac0244a8](https://github.com/MariaDB/server/commit/c8ac0244a8)\
  2017-04-19 07:45:24 +0000
  * add mariadb-backup to default suites
* [Revision #f344d7ec61](https://github.com/MariaDB/server/commit/f344d7ec61)\
  2017-04-18 20:59:33 +0000
  * Make Ninja generator happy with BUILD\_BYPRODUCTS.
* [Revision #7228b9985f](https://github.com/MariaDB/server/commit/7228b9985f)\
  2017-04-18 20:18:16 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) build mariadb-backup with libarchive for release
* [Revision #d894f7ceed](https://github.com/MariaDB/server/commit/d894f7ceed)\
  2017-04-18 20:01:30 +0000
  * update gitignore with commonly used (by me) out-of-source builddir names
* [Revision #64b3427b89](https://github.com/MariaDB/server/commit/64b3427b89)\
  2017-04-18 19:58:06 +0000
  * Run mariadb-backup test on Windows on buildbot
* [Revision #3d8aacba86](https://github.com/MariaDB/server/commit/3d8aacba86)\
  2017-02-22 15:58:45 -0500
  * SST script for mariadb-backup.
* [Revision #ca24f35b67](https://github.com/MariaDB/server/commit/ca24f35b67)\
  2017-04-18 19:52:03 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) mariadb-backup test suite
* [Revision #1991411f16](https://github.com/MariaDB/server/commit/1991411f16)\
  2017-04-18 19:35:48 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) mariadb-backup packaging
* [Revision #ce4c56db0c](https://github.com/MariaDB/server/commit/ce4c56db0c)\
  2017-04-18 19:05:57 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) Port Percona Xtrabackup to MariaDB as mariadb-backup
* [Revision #d7714308e0](https://github.com/MariaDB/server/commit/d7714308e0)\
  2017-04-18 18:43:20 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) Add Percona Xtrabackup 2.3.7
* [Revision #9c4b7cad27](https://github.com/MariaDB/server/commit/9c4b7cad27)\
  2017-04-18 17:57:07 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) Prepare xtradb for xtrabackup
* [Revision #f06ab0fc99](https://github.com/MariaDB/server/commit/f06ab0fc99)\
  2017-04-18 17:20:55 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) Server code changes in preparation for mariadb-backup
* [Revision #ec68f764f6](https://github.com/MariaDB/server/commit/ec68f764f6)\
  2017-04-18 17:09:28 +0000
  * [MDEV-9566](https://jira.mariadb.org/browse/MDEV-9566) prepare mysqltest for mariadb-backup
* [Revision #7bf409593e](https://github.com/MariaDB/server/commit/7bf409593e)\
  2017-04-25 15:44:18 +0200
  * [MDEV-11660](https://jira.mariadb.org/browse/MDEV-11660) Make encryption plugins "pure"
* [Revision #db39107413](https://github.com/MariaDB/server/commit/db39107413)\
  2017-04-18 16:37:57 +0000
  * [MDEV-11663](https://jira.mariadb.org/browse/MDEV-11663) Create services for functionality used by plugins
* [Revision #175dd3ad59](https://github.com/MariaDB/server/commit/175dd3ad59)\
  2017-04-23 20:05:55 +0200
  * cleanup: don't include \*.h files into SQL\_SOURCES
* [Revision #99e1294c1e](https://github.com/MariaDB/server/commit/99e1294c1e)\
  2017-04-24 15:39:47 +0200
  * bugfix: federated/replication did not increment bytes\_received status variable
* [Revision #2c3f578789](https://github.com/MariaDB/server/commit/2c3f578789)\
  2017-04-27 17:40:44 +0200
  * don't generate wsrep\_sst\_common in-place
* [Revision #baad0f3484](https://github.com/MariaDB/server/commit/baad0f3484)\
  2017-05-06 14:33:07 +0300
  * [MDEV-11520](https://jira.mariadb.org/browse/MDEV-11520) post-fix: Retry posix\_fallocate() on EINTR in fil\_ibd\_create()
* [Revision #07cb4646c6](https://github.com/MariaDB/server/commit/07cb4646c6)\
  2017-05-05 13:32:42 +0200
  * [MDEV-12704](https://jira.mariadb.org/browse/MDEV-12704): Document --add-drop-trigger option in mysqldump man page
* [Revision #cf31db184e](https://github.com/MariaDB/server/commit/cf31db184e)\
  2017-05-05 16:43:25 +0200
  * Fix test to be windows file system tollerant.
* [Revision #a3e0a952f7](https://github.com/MariaDB/server/commit/a3e0a952f7)\
  2017-05-05 12:09:07 +0200
  * [MDEV-12485](https://jira.mariadb.org/browse/MDEV-12485): fixed test
* [Revision #82811f7966](https://github.com/MariaDB/server/commit/82811f7966)\
  2017-04-28 19:42:32 +0200
  * [MDEV-12485](https://jira.mariadb.org/browse/MDEV-12485) foreign key on delete cascade stale entries with query cache enabled
* [Revision #e946297d8f](https://github.com/MariaDB/server/commit/e946297d8f)\
  2017-05-05 11:06:46 +0300
  * Remove an unused variable.
* Merge [Revision #f9cc391863](https://github.com/MariaDB/server/commit/f9cc391863) 2017-05-05 10:25:29 +0300 - Merge 10.1 into 10.2
* [Revision #765a43605a](https://github.com/MariaDB/server/commit/765a43605a)\
  2017-04-26 15:19:16 +0300
  * [MDEV-12253](https://jira.mariadb.org/browse/MDEV-12253): Buffer pool blocks are accessed after they have been freed
* [Revision #db0917f68f](https://github.com/MariaDB/server/commit/db0917f68f)\
  2017-05-05 11:05:55 +0400
  * [MDEV-12696](https://jira.mariadb.org/browse/MDEV-12696) Crash with LOAD XML and non-updatable VIEW column
* [Revision #96247be1a0](https://github.com/MariaDB/server/commit/96247be1a0)\
  2017-05-03 12:26:57 +0200
  * [MDEV-10431](https://jira.mariadb.org/browse/MDEV-10431): Please implement mysqldump --add-drop-trigger from MySQL 5.6
* [Revision #ba824b66c1](https://github.com/MariaDB/server/commit/ba824b66c1)\
  2017-05-03 18:15:54 +0000
  * [MDEV-12597](https://jira.mariadb.org/browse/MDEV-12597) Do not print warning about inconsistent slow-log variables
* [Revision #ce8ee7d90b](https://github.com/MariaDB/server/commit/ce8ee7d90b)\
  2017-05-03 13:49:43 -0700
  * Fixed the bug [MDEV-11990](https://jira.mariadb.org/browse/MDEV-11990).
* [Revision #52463ccff7](https://github.com/MariaDB/server/commit/52463ccff7)\
  2017-04-28 12:25:52 +1000
  * [MDEV-12469](https://jira.mariadb.org/browse/MDEV-12469): rocksdb having large numberic storage errors on ppc64 (BE)
* [Revision #a60bdcba64](https://github.com/MariaDB/server/commit/a60bdcba64)\
  2017-05-02 16:24:42 +0400
  * [MDEV-12462](https://jira.mariadb.org/browse/MDEV-12462) SPATIAL index fails to work with CONTAINS.
* [Revision #3ea9d3e59e](https://github.com/MariaDB/server/commit/3ea9d3e59e)\
  2017-05-02 15:47:43 +0400
  * [MDEV-12363](https://jira.mariadb.org/browse/MDEV-12363) Assertion \`0' failed in Type\_handler\_string\_result::make\_sort\_key(uchar\*, Item\*, const SORT\_FIELD\_ATTR\*, Sort\_param\*).
* [Revision #4a484e7a20](https://github.com/MariaDB/server/commit/4a484e7a20)\
  2017-05-02 15:16:01 +0400
  * [MDEV-12351](https://jira.mariadb.org/browse/MDEV-12351) Assertion \`cur\_step->type & JSON\_PATH\_KEY' failed in json\_find\_path.
* [Revision #42ad4f2821](https://github.com/MariaDB/server/commit/42ad4f2821)\
  2017-05-02 14:28:57 +0400
  * [MDEV-12364](https://jira.mariadb.org/browse/MDEV-12364) Server crashes in memcpy\_sse2\_unaligned / String::copy on JSON\_SEARCH with variables.
* [Revision #7afcee4cf6](https://github.com/MariaDB/server/commit/7afcee4cf6)\
  2017-05-01 16:04:47 -0700
  * [MDEV-8954](https://jira.mariadb.org/browse/MDEV-8954) unnecessary fetch of entire table
* [Revision #a0aacb3443](https://github.com/MariaDB/server/commit/a0aacb3443)\
  2017-05-07 23:40:51 +0000
  * Continuation of e13e1eea9672fa6e0cff24d86cb86cb5495178e1
* [Revision #b48f2a097d](https://github.com/MariaDB/server/commit/b48f2a097d)\
  2017-05-02 13:55:08 +0000
  * [MDEV-12663](https://jira.mariadb.org/browse/MDEV-12663) : rocksdb.compact\_deletes times out and causes other tests to fail
* [Revision #07d329a758](https://github.com/MariaDB/server/commit/07d329a758)\
  2017-05-02 09:36:16 -0400
  * Continuation of the previous cset: rename sysvar's test, too.
* [Revision #e13e1eea96](https://github.com/MariaDB/server/commit/e13e1eea96)\
  2017-05-01 17:50:18 +0300
  * MyRocks: update to latest rocksdb
* [Revision #5ccaabe962](https://github.com/MariaDB/server/commit/5ccaabe962)\
  2017-04-19 15:58:15 +0200
  * [MDEV-10355](https://jira.mariadb.org/browse/MDEV-10355) Weird error message upon CREATE TABLE with DEFAULT
* [Revision #d17093b2ed](https://github.com/MariaDB/server/commit/d17093b2ed)\
  2017-04-18 17:44:30 +0200
  * [MDEV-12293](https://jira.mariadb.org/browse/MDEV-12293) Assertion \`table->no\_keyread || !table->covering\_keys.is\_set(tab->index) || table->file->keyread == tab->index' failed
* [Revision #54e24fcbd5](https://github.com/MariaDB/server/commit/54e24fcbd5)\
  2017-04-16 07:05:19 -0400
  * Compile user\_variables plugin statically
* [Revision #0072d2e9a1](https://github.com/MariaDB/server/commit/0072d2e9a1)\
  2017-04-07 15:01:27 +0200
  * InnoDB cleanup: remove a bunch of #ifdef UNIV\_INNOCHECKSUM
* [Revision #7a29ca2776](https://github.com/MariaDB/server/commit/7a29ca2776)\
  2017-04-28 21:58:04 -0700
  * Fixed the bug [MDEV-12563](https://jira.mariadb.org/browse/MDEV-12563).
* [Revision #4b24467ff3](https://github.com/MariaDB/server/commit/4b24467ff3)\
  2017-04-28 12:23:35 +0300
  * [MDEV-12602](https://jira.mariadb.org/browse/MDEV-12602) InnoDB: Failing assertion: space->n\_pending\_ops == 0
* Merge [Revision #f740d23ce6](https://github.com/MariaDB/server/commit/f740d23ce6) 2017-04-28 12:22:32 +0300 - Merge 10.1 into 10.2
* [Revision #97e0c260dc](https://github.com/MariaDB/server/commit/97e0c260dc)\
  2017-04-25 15:25:10 +0530
  * Fix Galera tests failures on 10.1 and 10.2
* Merge [Revision #340af4ebc3](https://github.com/MariaDB/server/commit/340af4ebc3) 2017-04-24 08:31:59 +0300 - Merge pull request #363 from grooverdan/10.1-[MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488)-xtradb-os\_thread\_pf
* [Revision #7d0ac3ade7](https://github.com/MariaDB/server/commit/7d0ac3ade7)\
  2017-04-24 13:02:08 +1000
  * [MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488): Remove type mismatch in InnoDB printf-like calls
* [Revision #200ef51344](https://github.com/MariaDB/server/commit/200ef51344)\
  2017-04-21 18:29:50 +0300
  * Fix a compilation error
* [Revision #996c7d5cb5](https://github.com/MariaDB/server/commit/996c7d5cb5)\
  2017-04-21 17:32:02 +0300
  * [MDEV-12545](https://jira.mariadb.org/browse/MDEV-12545) Reduce the amount of fil\_space\_t lookups
* [Revision #555e52f3bc](https://github.com/MariaDB/server/commit/555e52f3bc)\
  2017-04-21 11:52:25 +0300
  * [MDEV-12467](https://jira.mariadb.org/browse/MDEV-12467) encryption.create\_or\_replace hangs during DROP TABLE
* [Revision #d23eb8e6d2](https://github.com/MariaDB/server/commit/d23eb8e6d2)\
  2017-04-21 16:06:05 +0300
  * Follow-up to [MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488): Fix some type mismatch in header files
* [Revision #aafaf05a47](https://github.com/MariaDB/server/commit/aafaf05a47)\
  2017-04-21 08:45:48 +0300
  * Fix some InnoDB type mismatch introduced in 10.1
* Merge [Revision #7445ff84f4](https://github.com/MariaDB/server/commit/7445ff84f4) 2017-04-21 17:41:40 +0300 - Merge 10.0 into 10.1
* [Revision #e056d1f1ca](https://github.com/MariaDB/server/commit/e056d1f1ca)\
  2017-04-21 17:39:12 +0300
  * Fix some InnoDB type mismatch
* [Revision #e48ae21b0e](https://github.com/MariaDB/server/commit/e48ae21b0e)\
  2017-04-21 16:22:46 +0300
  * Follow-up to [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534): Fix warnings on 32-bit systems
* [Revision #3a6af51a8a](https://github.com/MariaDB/server/commit/3a6af51a8a)\
  2017-04-21 05:05:51 +0300
  * Do not crash XtraDB when fil\_space\_acquire() fails
* Merge [Revision #8c38147cdd](https://github.com/MariaDB/server/commit/8c38147cdd) 2017-04-21 12:24:17 +0300 - Merge 10.0 into 10.1
* [Revision #87b6df31c4](https://github.com/MariaDB/server/commit/87b6df31c4)\
  2017-04-21 04:36:50 +0300
  * [MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488) Remove type mismatch in InnoDB printf-like calls
* [Revision #d34a67b067](https://github.com/MariaDB/server/commit/d34a67b067)\
  2017-04-19 22:30:18 +0300
  * [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534) Use atomic operations whenever available
* [Revision #88613e1df6](https://github.com/MariaDB/server/commit/88613e1df6)\
  2016-12-01 09:59:58 +0100
  * [MDEV-11201](https://jira.mariadb.org/browse/MDEV-11201): gtid\_ignore\_duplicates incorrectly ignores statements when GTID replication is not enabled
* [Revision #7dd6efeaab](https://github.com/MariaDB/server/commit/7dd6efeaab)\
  2017-04-02 16:43:43 +1000
  * Don't use full path of libtool
* [Revision #5136295b21](https://github.com/MariaDB/server/commit/5136295b21)\
  2017-04-02 20:11:12 +1000
  * OSX: get cache line size
* [Revision #107de652b6](https://github.com/MariaDB/server/commit/107de652b6)\
  2017-03-29 14:53:55 +0200
  * [MDEV-11964](https://jira.mariadb.org/browse/MDEV-11964) my\_safe\_process, tokuft\_logdump stub man pages
* [Revision #3bb32e8682](https://github.com/MariaDB/server/commit/3bb32e8682)\
  2017-04-15 03:36:23 +0300
  * [MDEV-10509](https://jira.mariadb.org/browse/MDEV-10509): Remove excessive server error logging on InnoDB ALTER TABLE
* [Revision #16b2b1eae5](https://github.com/MariaDB/server/commit/16b2b1eae5)\
  2017-04-08 16:46:26 +0300
  * Use page\_is\_leaf() where applicable
* [Revision #ea4146229c](https://github.com/MariaDB/server/commit/ea4146229c)\
  2017-04-06 12:41:55 +0530
  * Fix test failure , and add galera\_restart\_on\_unknown\_option to disabled.
* [Revision #2e889de34a](https://github.com/MariaDB/server/commit/2e889de34a)\
  2017-04-05 16:24:39 +0530
  * Fix test cases in galera suite
* [Revision #969fc61120](https://github.com/MariaDB/server/commit/969fc61120)\
  2017-03-28 13:09:28 +0530
  * Fix build on windows
* [Revision #d036cc9b2f](https://github.com/MariaDB/server/commit/d036cc9b2f)\
  2017-03-24 16:20:59 +0530
  * Fix WSREP\_PATCH\_VERSION
* [Revision #1ba2242ef3](https://github.com/MariaDB/server/commit/1ba2242ef3)\
  2017-03-22 09:40:57 +0530
  * [MDEV-12319](https://jira.mariadb.org/browse/MDEV-12319) Test added to disabled.def
* [Revision #34d11b344b](https://github.com/MariaDB/server/commit/34d11b344b)\
  2017-03-21 14:23:45 +0530
  * Fix galera\_admin test
* [Revision #2af4659b05](https://github.com/MariaDB/server/commit/2af4659b05)\
  2017-03-21 10:00:02 +0200
  * Fix failure on galera\_toi\_drop\_database test.
* [Revision #5866c4d084](https://github.com/MariaDB/server/commit/5866c4d084)\
  2017-03-23 17:11:31 +0530
  * Fix test cases
* [Revision #bd2064e820](https://github.com/MariaDB/server/commit/bd2064e820)\
  2017-04-05 16:30:03 +0530
  * MW-313 Enforce wsrep\_max\_ws\_rows also when binlog is enabled
* [Revision #633959525c](https://github.com/MariaDB/server/commit/633959525c)\
  2017-03-14 18:41:38 +0530
  * Fix Some failing tests
* [Revision #adc151fdaf](https://github.com/MariaDB/server/commit/adc151fdaf)\
  2017-01-25 09:58:07 +0200
  * Bump WSREP\_PATCH\_VERSION to 19
* [Revision #66916bba2a](https://github.com/MariaDB/server/commit/66916bba2a)\
  2016-12-16 02:30:09 -0800
  * Galera MTR Tests: Tests for MW-328 Fix unnecessary/silent BF aborts
* [Revision #97a3a07c35](https://github.com/MariaDB/server/commit/97a3a07c35)\
  2016-12-08 05:15:31 -0800
  * Galera MTR Tests: Stability fix for MW-329
* [Revision #59f3285f35](https://github.com/MariaDB/server/commit/59f3285f35)\
  2016-12-08 00:17:28 -0800
  * Galera MTR Tests: Test for MW-329 Fix incorrect affected rows count after replay
* [Revision #ff7426290c](https://github.com/MariaDB/server/commit/ff7426290c)\
  2017-03-23 16:52:55 +0530
  * MW-329 Fix incorrect affected rows count after replay
* [Revision #770553e185](https://github.com/MariaDB/server/commit/770553e185)\
  2016-11-25 16:56:57 -0200
  * [GAL-480](https://github.com/codership/galera/issues/480) MTR test
* [Revision #298daccb10](https://github.com/MariaDB/server/commit/298daccb10)\
  2016-11-23 02:55:36 -0800
  * Galera MTR Test: Test for MW-28 : Assertion with --wsrep-log-conflicts
* [Revision #cdd1dc829b](https://github.com/MariaDB/server/commit/cdd1dc829b)\
  2017-03-23 15:46:11 +0530
  * MW-28, codership/mysql-wsrep#28 Fix sync\_thread\_levels debug assert
* [Revision #836727c971](https://github.com/MariaDB/server/commit/836727c971)\
  2016-11-21 10:38:20 +0200
  * refs: MW-319 \* silenced the WSREP\_ERROR, this fires for all replication filtered DDL, and is false positive
* [Revision #70ae1dbac0](https://github.com/MariaDB/server/commit/70ae1dbac0)\
  2017-03-23 15:01:57 +0530
  * Galera MTR tests: Make the mysqlhotcopy tests pass on Ubuntu 16.04
* [Revision #8aa5356d86](https://github.com/MariaDB/server/commit/8aa5356d86)\
  2016-11-08 15:19:37 +0200
  * Bump WSREP\_PATCH\_VERSION to 18
* [Revision #59dcf2a5d5](https://github.com/MariaDB/server/commit/59dcf2a5d5)\
  2016-11-05 09:15:14 -0700
  * Galera MTR Tests: stability fix for galera#414.test
* [Revision #f369942d90](https://github.com/MariaDB/server/commit/f369942d90)\
  2017-03-23 15:00:14 +0530
  * Galera MTR Tests: stability fixes
* [Revision #c72e1ea940](https://github.com/MariaDB/server/commit/c72e1ea940)\
  2016-11-04 01:33:54 -0700
  * Galera MTR Tests: Test for MW-313 Enforce wsrep\_max\_ws\_rows also when binlog is enabled
* [Revision #f94c9b02cf](https://github.com/MariaDB/server/commit/f94c9b02cf)\
  2016-11-03 04:05:05 -0700
  * Galera MTR Tests: MW-305 , re-enable the test for ALTER USER
* [Revision #0f6aa6ba66](https://github.com/MariaDB/server/commit/0f6aa6ba66)\
  2016-11-02 07:04:34 -0700
  * Galera MTR tests: Update galera\_defaults.result for [GAL-360](https://github.com/codership/galera/issues/360)
* [Revision #c3e9110033](https://github.com/MariaDB/server/commit/c3e9110033)\
  2017-03-23 13:43:12 +0530
  * Galera MTR Tests: Tests for [GAL-419](https://github.com/codership/galera/issues/419) Respect safe\_to\_bootstrap flag also with gcomm:
* [Revision #07fe265a47](https://github.com/MariaDB/server/commit/07fe265a47)\
  2016-11-02 02:01:10 -0700
  * Galera MTR Tests: [GAL-405](https://github.com/codership/galera/issues/405) Initial implementation of GCache recovery on startup.
* [Revision #9b13147d72](https://github.com/MariaDB/server/commit/9b13147d72)\
  2017-03-22 11:41:47 +0530
  * Galera MTR Tests: MW-308 , MW-307, GCF-992
* [Revision #09d8fbc0cf](https://github.com/MariaDB/server/commit/09d8fbc0cf)\
  2016-10-11 03:37:42 -0700
  * Galera MTR Tests: GCF-981 - galera\_bf\_abort is non deterministic
* [Revision #e043029aaa](https://github.com/MariaDB/server/commit/e043029aaa)\
  2016-10-03 03:09:49 -0700
  * Galera MTR Tests: Test for GCF-942 - safe\_to\_bootstrap flag in grastate.dat
* [Revision #3de28b42b4](https://github.com/MariaDB/server/commit/3de28b42b4)\
  2016-09-14 14:33:59 +0300
  * Bump WSREP\_PATCH\_VERSION to 17
* [Revision #e757e02417](https://github.com/MariaDB/server/commit/e757e02417)\
  2017-03-22 10:04:57 +0530
  * Galera MTR Tests: Copy over some MTR tests from PXC
* [Revision #912ca4c153](https://github.com/MariaDB/server/commit/912ca4c153)\
  2016-08-20 13:42:11 +0200
  * [GAL-401](https://github.com/codership/galera/issues/401): MTR test for the fix.
* [Revision #e21c15a7e6](https://github.com/MariaDB/server/commit/e21c15a7e6)\
  2017-04-28 12:28:16 +0530
  * Fix binlog.flashback test.
* [Revision #eb55a9df52](https://github.com/MariaDB/server/commit/eb55a9df52)\
  2017-04-27 21:20:02 +0530
  * [MDEV-12017](https://jira.mariadb.org/browse/MDEV-12017) Post Fix
* [Revision #3167c91244](https://github.com/MariaDB/server/commit/3167c91244)\
  2017-04-27 07:50:56 +0300
  * Temporarily disable a failing test
* [Revision #7fc93fd60a](https://github.com/MariaDB/server/commit/7fc93fd60a)\
  2017-04-26 15:31:16 +0300
  * Adapt a test from MySQL
* [Revision #14fe6dd239](https://github.com/MariaDB/server/commit/14fe6dd239)\
  2017-02-15 12:00:07 +0530
  * Bug #23046302 COUNT(\*) MUCH SLOWER ON 5.7 THAN 5.6
* [Revision #07f331151c](https://github.com/MariaDB/server/commit/07f331151c)\
  2017-04-26 14:16:53 +0300
  * Adapt the second test case for Oracle Bug#25385590
* [Revision #fca0698fd8](https://github.com/MariaDB/server/commit/fca0698fd8)\
  2017-02-14 14:34:44 +0530
  * Bug #25385590 DROP TABLE CRASHES IF INNODB\_FORCE\_RECOVERY > 4
* [Revision #67e9c4cf6c](https://github.com/MariaDB/server/commit/67e9c4cf6c)\
  2017-04-26 13:53:13 +0300
  * Adapt the test case for Oracle Bug#25385590
* [Revision #7223ec4ca7](https://github.com/MariaDB/server/commit/7223ec4ca7)\
  2017-02-01 16:03:57 +0530
  * Bug #25385590 DROP TABLE CRASHES IF INNODB\_FORCE\_RECOVERY > 4
* [Revision #da0b2f0972](https://github.com/MariaDB/server/commit/da0b2f0972)\
  2017-04-26 13:02:03 +0300
  * Adapt the test case for Oracle Bug#24793413
* [Revision #2ef1baa75f](https://github.com/MariaDB/server/commit/2ef1baa75f)\
  2017-01-10 10:48:56 +0530
  * Bug #24793413 LOG PARSING BUFFER OVERFLOW
* [Revision #88a84f49b3](https://github.com/MariaDB/server/commit/88a84f49b3)\
  2017-01-06 19:48:54 +0530
  * Bug #25167032 CRASH WHEN ASSIGNING MY\_ERRNO - MISSING MY\_THREAD\_INIT IN BACKGROUND THREAD
* [Revision #e180f3c5cf](https://github.com/MariaDB/server/commit/e180f3c5cf)\
  2017-04-26 12:02:13 +0300
  * Adapt the test case for Oracle Bug#25330449
* [Revision #dbe4c4e354](https://github.com/MariaDB/server/commit/dbe4c4e354)\
  2017-01-06 10:37:07 +0100
  * BUG#25330449 ASSERT SIZE==SPACE->SIZE DURING BUF\_READ\_AHEAD\_RANDOM
* [Revision #849af74a48](https://github.com/MariaDB/server/commit/849af74a48)\
  2017-04-25 18:25:57 +0300
  * MariaDB adjustments for Oracle Bug#23070734 fix
* [Revision #62dca454e7](https://github.com/MariaDB/server/commit/62dca454e7)\
  2017-01-04 14:34:38 +0530
  * Bug #23070734 CONCURRENT TRUNCATE TABLES CAUSE STALLS
* [Revision #13dcdb0903](https://github.com/MariaDB/server/commit/13dcdb0903)\
  2017-04-26 10:30:13 +0300
  * [MDEV-11802](https://jira.mariadb.org/browse/MDEV-11802) InnoDB purge does not always run when there is work to do
* [Revision #731435af9a](https://github.com/MariaDB/server/commit/731435af9a)\
  2017-04-26 10:13:22 +0300
  * srv\_purge\_coordinator\_thread(): Remove redundant variables
* [Revision #6264e892cf](https://github.com/MariaDB/server/commit/6264e892cf)\
  2017-04-26 10:11:46 +0300
  * Remove redundant initialization of global InnoDB variables
* [Revision #797db28d53](https://github.com/MariaDB/server/commit/797db28d53)\
  2017-04-26 07:31:54 +0300
  * Remove the unused declaration fsp\_is\_temporary()
* [Revision #6b63e4ad4a](https://github.com/MariaDB/server/commit/6b63e4ad4a)\
  2016-12-28 17:44:16 +0530
  * Bug #23219499 CONCURRENT UPDATE DOESN'T APPLY IN VIRTUAL INDEX DURING TABLE REBUILD
* [Revision #698e37d60c](https://github.com/MariaDB/server/commit/698e37d60c)\
  2016-12-16 12:14:38 +0530
  * BUG#25251082 DISABLING CERTAIN MACROS IN INNODB RESULTS IN COMPILATION ERRORS
* [Revision #16ed1f9c31](https://github.com/MariaDB/server/commit/16ed1f9c31)\
  2016-12-15 16:50:44 +0530
  * BUG#25053705 INVALID I/O ON TABLE AFTER TRUNCATE
* [Revision #c2d9c0ce85](https://github.com/MariaDB/server/commit/c2d9c0ce85)\
  2016-12-15 15:38:06 +0530
  * Bug #24585978 INNODB: ASSERTION TOTAL\_RECS > 0 FAILURE IN FILE DICT0STATS.CC
* [Revision #35652ed631](https://github.com/MariaDB/server/commit/35652ed631)\
  2016-12-14 18:42:46 +0530
  * Bug#25222337 FIELD NAME IS NULL IN NEWLY ADDED VIRTUAL INDEX FOR NEWLY ADDED VIRTUAL COLUMN
* [Revision #49edf2d476](https://github.com/MariaDB/server/commit/49edf2d476)\
  2016-11-25 11:04:23 +0530
  * BUG#25126722 FOREIGN KEY CONSTRAINT NAME IS NULL IN INFORMATION\_SCHEMA AFTER RESTART
* [Revision #07e88be5b7](https://github.com/MariaDB/server/commit/07e88be5b7)\
  2016-11-22 14:35:16 +0800
  * Bug#23044098 INSERT OF GIS DATA INTO RTREE HITS ASSERT IN RTR\_CUR\_RESTORE\_POSITION\_FUNC()
* [Revision #4e41ac26f5](https://github.com/MariaDB/server/commit/4e41ac26f5)\
  2016-11-13 10:31:35 +0530
  * BUG#25082593 FOREIGN KEY VALIDATION DOESN'T NEED TO ACQUIRE GAP LOCK IN READ COMMITTED
* [Revision #bf5be32376](https://github.com/MariaDB/server/commit/bf5be32376)\
  2016-11-12 20:53:15 +0530
  * BUG#25032066 PREPARED TRANSACTION SHOULD NOT BE ROLLED BACK BY HIGH PRIORITY TRANSACTION
* [Revision #9df0426103](https://github.com/MariaDB/server/commit/9df0426103)\
  2016-11-04 13:44:36 +0100
  * Bug#25048573: STD::MAP INSTANTIATIONS CAUSE STATIC ASSERT FAILURES ON FREEBSD 11
* [Revision #8923f6b741](https://github.com/MariaDB/server/commit/8923f6b741)\
  2016-09-27 14:09:54 +0300
  * Fix Bug#24707869 GCC 5 AND 6 MISCOMPILE MACH\_PARSE\_COMPRESSED
* [Revision #32f99b288b](https://github.com/MariaDB/server/commit/32f99b288b)\
  2016-09-23 11:20:34 +0100
  * Bug #24711351 64 BIT WINDOWS MYSQLD BUILD REPORTS INNODB: OPERATING SYSTEM ERROR NUMBER 995
* [Revision #6c76e5a00b](https://github.com/MariaDB/server/commit/6c76e5a00b)\
  2016-09-12 10:54:45 +0300
  * Fix Bug#24605956 SERVER MAY CRASH DUE TO A GLIBC BUG IN HANDLING SHORT-LIVED DETACHED THREADS
* [Revision #da76c1bd3e](https://github.com/MariaDB/server/commit/da76c1bd3e)\
  2017-04-25 15:39:06 +0300
  * Minor cleanup
* [Revision #ce3ffefc45](https://github.com/MariaDB/server/commit/ce3ffefc45)\
  2017-04-25 09:26:01 +0300
  * Adapt the innodb\_undo tests from MySQL 5.7
* [Revision #d1bcc1f49f](https://github.com/MariaDB/server/commit/d1bcc1f49f)\
  2016-09-07 12:40:10 +0530
  * Bug #24488141 ACTIVE UNDO TABLESPACE NOT UPDATED WHEN INNODB\_UNDO\_LOGS IS INCREASED
* [Revision #bdfa49f6e2](https://github.com/MariaDB/server/commit/bdfa49f6e2)\
  2017-04-25 10:11:40 +0300
  * Remove redundant initialization of some InnoDB startup parameters
* [Revision #206ecb79a5](https://github.com/MariaDB/server/commit/206ecb79a5)\
  2017-04-25 09:26:01 +0300
  * Follow-up to [MDEV-12289](https://jira.mariadb.org/browse/MDEV-12289): Support innodb\_undo\_tablespaces=127
* [Revision #23ea4360fd](https://github.com/MariaDB/server/commit/23ea4360fd)\
  2017-04-25 09:37:27 +0300
  * Remove TRX\_SYS\_OLD\_N\_RSEGS
* [Revision #472b5f0d1f](https://github.com/MariaDB/server/commit/472b5f0d1f)\
  2016-09-06 14:57:16 +0300
  * Follow-up to Bug#24346574 PAGE CLEANER THREAD, ASSERT BLOCK->N\_POINTERS == 0
* [Revision #e63ead68bf](https://github.com/MariaDB/server/commit/e63ead68bf)\
  2016-09-02 17:28:54 +0300
  * Bug#24346574 PAGE CLEANER THREAD, ASSERT BLOCK->N\_POINTERS == 0
* [Revision #a6adf567fd](https://github.com/MariaDB/server/commit/a6adf567fd)\
  2016-09-01 19:53:04 +0530
  * Bug #23533396 ASSERTION !M\_PREBUILT->TRX->CHECK\_FOREIGNS
* [Revision #93078c9cb1](https://github.com/MariaDB/server/commit/93078c9cb1)\
  2016-08-31 09:21:13 +0300
  * Bug#24444831 MY\_ERROR(ER\_INNODB\_ONLINE\_LOG\_TOO\_BIG) CALLED WITH INVALID INDEX NAME
* [Revision #9a848ee182](https://github.com/MariaDB/server/commit/9a848ee182)\
  2017-04-25 07:15:23 +0300
  * Fix the -DWITH\_INNODB\_AHI=OFF build
* [Revision #8080d79f7e](https://github.com/MariaDB/server/commit/8080d79f7e)\
  2017-04-26 23:00:57 +0300
  * Adjust a test for WL9513 Bug#23333990
* [Revision #c7a153453e](https://github.com/MariaDB/server/commit/c7a153453e)\
  2017-04-26 10:10:36 -0700
  * Fixed the bug [MDEV-12556](https://jira.mariadb.org/browse/MDEV-12556).
* [Revision #e180c35619](https://github.com/MariaDB/server/commit/e180c35619)\
  2017-04-26 11:01:51 +0530
  * [MDEV-12017](https://jira.mariadb.org/browse/MDEV-12017) Unclear error with flashback: Variable 'binlog\_format' can't ...
* [Revision #a287bfa09a](https://github.com/MariaDB/server/commit/a287bfa09a)\
  2017-04-25 19:34:39 -0700
  * Fixed the bug [MDEV-12558](https://jira.mariadb.org/browse/MDEV-12558).
* [Revision #d7d8c23654](https://github.com/MariaDB/server/commit/d7d8c23654)\
  2017-04-10 11:05:50 +1000
  * [MDEV-12469](https://jira.mariadb.org/browse/MDEV-12469): static\_assert cannot be determined on bigendian
* [Revision #a9ad84e4d4](https://github.com/MariaDB/server/commit/a9ad84e4d4)\
  2017-04-25 15:25:10 +0530
  * Fix Galera tests failures on 10.1 and 10.2
* [Revision #4beb7e5355](https://github.com/MariaDB/server/commit/4beb7e5355)\
  2017-04-24 23:58:23 -0700
  * Fixed the bug [MDEV-12373](https://jira.mariadb.org/browse/MDEV-12373).
* [Revision #0906dc49e8](https://github.com/MariaDB/server/commit/0906dc49e8)\
  2017-04-24 14:56:53 -0700
  * Fixed the bug [MDEV-12564](https://jira.mariadb.org/browse/MDEV-12564).
* [Revision #44b1fb3614](https://github.com/MariaDB/server/commit/44b1fb3614)\
  2016-08-31 20:16:48 +0530
  * WL9513 Bug#23333990 PERSISTENT INDEX STATISTICS UPDATE BEFORE TRANSACTION IS COMMITTED
* [Revision #6f5f720848](https://github.com/MariaDB/server/commit/6f5f720848)\
  2016-08-30 08:34:49 +0300
  * Bug#22018745 CORRUPTION IN ONLINE TABLE REBUILD (ROW\_FORMAT=REDUNDANT, INDEXED VIRTUAL COLUMN)
* [Revision #223eb5fb9a](https://github.com/MariaDB/server/commit/223eb5fb9a)\
  2016-08-26 11:00:44 +0530
  * Bug #20989615 INNODB AUTO\_INCREMENT PRODUCES SAME VALUE TWICE
* [Revision #01389ee8ac](https://github.com/MariaDB/server/commit/01389ee8ac)\
  2016-08-08 14:19:32 +0300
  * Bug#24397406 INNODB: ALGORITHM=INPLACE FAILS TO PROMOTE UNIQUE KEY TO CLUSTERED INDEX
* [Revision #92f7f81b6b](https://github.com/MariaDB/server/commit/92f7f81b6b)\
  2016-08-16 03:33:21 +0200
  * BUG#24331265 MEMORY LEAK IN SOME INNODB FTS TESTS
* [Revision #f5759bd8d8](https://github.com/MariaDB/server/commit/f5759bd8d8)\
  2016-08-10 14:47:36 +0530
  * Bug #24347476 HIGH PRIORITY TRX FAILED TO KILL LOW PRIORITY TRX WHEN FOREIGN KEYS ARE INVOLVED
* [Revision #a930c0aa86](https://github.com/MariaDB/server/commit/a930c0aa86)\
  2016-08-05 09:05:18 +0200
  * BUG#23760086 INNODB: ASSERTION FAILURE: MACH0DATA.IC:56:(N | 0XFFFFUL) <= 0XFFFFUL
* [Revision #d3a2f60e1a](https://github.com/MariaDB/server/commit/d3a2f60e1a)\
  2016-07-28 13:08:52 +0800
  * BUG#23477773 OPTION TO TURN OFF/ON DEADLOCK CHECKER
* [Revision #1a5ca702b1](https://github.com/MariaDB/server/commit/1a5ca702b1)\
  2016-07-27 10:39:19 +0200
  * Followup: BUG#23479595 SEGMENTATION FAULT WHEN SELECT FTS INDEX TABLES IN INFORMATION SCHEMA
* [Revision #b862c7972b](https://github.com/MariaDB/server/commit/b862c7972b)\
  2016-07-27 09:37:20 +0200
  * BUG#24315031 FAILING ASSERTION: !TABLE->CAN\_BE\_EVICTED
* [Revision #9ce1ea6f51](https://github.com/MariaDB/server/commit/9ce1ea6f51)\
  2016-07-27 03:43:52 +0200
  * BUG#24009272 SEGFAULT WITH CREATE+SELECT FROM IS+DROP FTS TABLE CONCURRENTLY
* [Revision #4b5a9d8e0f](https://github.com/MariaDB/server/commit/4b5a9d8e0f)\
  2016-07-15 14:39:37 +0530
  * Bug #23475211 COMBINING ALTER OPERATIONS TRIGGERS TABLE REBUILD
* [Revision #d66c171e0f](https://github.com/MariaDB/server/commit/d66c171e0f)\
  2017-04-22 23:45:38 -0700
  * Fixed the bug [MDEV-12554](https://jira.mariadb.org/browse/MDEV-12554).
* [Revision #54a995cd22](https://github.com/MariaDB/server/commit/54a995cd22)\
  2017-04-20 13:09:31 -0700
  * Fixed the bug [MDEV-12519](https://jira.mariadb.org/browse/MDEV-12519).
* [Revision #14d124880f](https://github.com/MariaDB/server/commit/14d124880f)\
  2017-04-21 18:29:50 +0300
  * Fix a crash when page\_compression fails during IMPORT TABLESPACE
* [Revision #11f772fad6](https://github.com/MariaDB/server/commit/11f772fad6)\
  2017-04-21 05:53:15 +0300
  * Remove an orphan declaration of os\_get\_os\_version()
* [Revision #0871a00a62](https://github.com/MariaDB/server/commit/0871a00a62)\
  2017-04-21 11:28:18 +0300
  * [MDEV-12545](https://jira.mariadb.org/browse/MDEV-12545) Reduce the amount of fil\_space\_t lookups
* [Revision #b66e15ecbc](https://github.com/MariaDB/server/commit/b66e15ecbc)\
  2017-04-21 11:52:25 +0300
  * [MDEV-12467](https://jira.mariadb.org/browse/MDEV-12467) encryption.create\_or\_replace hangs during DROP TABLE
* [Revision #47141c9d9b](https://github.com/MariaDB/server/commit/47141c9d9b)\
  2017-04-21 08:45:48 +0300
  * Fix some InnoDB type mismatch
* [Revision #5684aa220c](https://github.com/MariaDB/server/commit/5684aa220c)\
  2017-04-21 05:51:27 +0300
  * [MDEV-12488](https://jira.mariadb.org/browse/MDEV-12488) Remove type mismatch in InnoDB printf-like calls
* [Revision #039a299b92](https://github.com/MariaDB/server/commit/039a299b92)\
  2017-04-19 22:30:18 +0300
  * [MDEV-12534](https://jira.mariadb.org/browse/MDEV-12534) Use atomic operations whenever available
* [Revision #8bbeac0171](https://github.com/MariaDB/server/commit/8bbeac0171)\
  2017-04-20 13:39:02 +0000
  * Fix AWS SDK build error on some buildbot builders.
* [Revision #9a91d743bb](https://github.com/MariaDB/server/commit/9a91d743bb)\
  2017-04-09 18:08:24 +1000
  * [MDEV-12453](https://jira.mariadb.org/browse/MDEV-12453): AWS SDK version failed to build on OSX
* [Revision #571d4137bf](https://github.com/MariaDB/server/commit/571d4137bf)\
  2017-04-19 08:17:41 +0300
  * Add IMPORT test for [MDEV-12123](https://jira.mariadb.org/browse/MDEV-12123) Page contains nonzero PAGE\_MAX\_TRX\_ID
* [Revision #d0ef1aaf61](https://github.com/MariaDB/server/commit/d0ef1aaf61)\
  2017-04-08 19:28:19 +0300
  * [MDEV-12123](https://jira.mariadb.org/browse/MDEV-12123) Page contains nonzero PAGE\_MAX\_TRX\_ID
* [Revision #0b52b28b91](https://github.com/MariaDB/server/commit/0b52b28b91)\
  2017-04-18 17:36:05 -0700
  * [MDEV-10355](https://jira.mariadb.org/browse/MDEV-10355) Weird error message upon CREATE TABLE with DEFAULT
* [Revision #38af34bb21](https://github.com/MariaDB/server/commit/38af34bb21)\
  2017-04-17 15:32:44 -0700
  * [MDEV-11117](https://jira.mariadb.org/browse/MDEV-11117) CHECK constraint fails on intermediate step of ALTER
* [Revision #3a50fd9d2f](https://github.com/MariaDB/server/commit/3a50fd9d2f)\
  2017-04-10 12:42:38 +0300
  * Simplify page\_is\_comp().
* [Revision #a039d6c3e6](https://github.com/MariaDB/server/commit/a039d6c3e6)\
  2017-04-10 01:36:33 +0300
  * Remove unused tokens from the InnoDB SQL parser.
* [Revision #e5eef05140](https://github.com/MariaDB/server/commit/e5eef05140)\
  2017-04-08 19:13:32 +0300
  * Minor code cleanup.
* [Revision #bb81828938](https://github.com/MariaDB/server/commit/bb81828938)\
  2017-04-08 16:47:41 +0300
  * Use page\_is\_leaf() where applicable.
* [Revision #3849f8b2bb](https://github.com/MariaDB/server/commit/3849f8b2bb)\
  2017-04-17 03:18:21 +0300
  * Fixup for [MDEV-11995](https://jira.mariadb.org/browse/MDEV-11995).
* [Revision #eecce3d7c8](https://github.com/MariaDB/server/commit/eecce3d7c8)\
  2017-04-10 19:11:01 +1000
  * Travis: Test more suites, latest OSX
* [Revision #c7319cf3d5](https://github.com/MariaDB/server/commit/c7319cf3d5)\
  2017-04-03 14:11:27 +0200
  * 10.2 man pages
* [Revision #8c9cd26c06](https://github.com/MariaDB/server/commit/8c9cd26c06)\
  2017-04-07 17:00:35 +0000
  * Rocksdb - disable tests that fail regularly on buildbot ([MDEV-12474](https://jira.mariadb.org/browse/MDEV-12474))
* [Revision #d9484a2f60](https://github.com/MariaDB/server/commit/d9484a2f60)\
  2017-04-04 14:47:58 +0200
  * [MDEV-12395](https://jira.mariadb.org/browse/MDEV-12395): DROP PARTITION does not work as expected when table has DEFAULT LIST partition
* [Revision #27f6b11a97](https://github.com/MariaDB/server/commit/27f6b11a97)\
  2017-04-04 11:00:25 +0200
  * [MDEV-12379](https://jira.mariadb.org/browse/MDEV-12379): Server crashes in TABLE\_LIST::is\_with\_table on SHOW CREATE VIEW
* [Revision #a33653eedb](https://github.com/MariaDB/server/commit/a33653eedb)\
  2017-04-07 15:09:28 +0000
  * [MDEV-12473](https://jira.mariadb.org/browse/MDEV-12473) - fix rocksdb linking error
* [Revision #85da56bf2d](https://github.com/MariaDB/server/commit/85da56bf2d)\
  2017-04-07 13:33:59 +0300
  * Remove the unused variable trx\_t::support\_xa.
* [Revision #84d9d286cf](https://github.com/MariaDB/server/commit/84d9d286cf)\
  2017-04-05 13:17:43 +0200
  * use log-error in mtr, don't let mysqld to write to stderr
* [Revision #cd79be82d1](https://github.com/MariaDB/server/commit/cd79be82d1)\
  2017-04-06 14:47:55 +0200
  * cleanup: unused method LOGGER::flush\_logs
* [Revision #06ee58a7dd](https://github.com/MariaDB/server/commit/06ee58a7dd)\
  2017-04-03 23:58:36 +0200
  * ASAN error in rpl.mysql-wsrep#110-2
* [Revision #30ed99cb82](https://github.com/MariaDB/server/commit/30ed99cb82)\
  2017-04-03 21:08:23 +0200
  * ASAN errors in many rpl tests
* [Revision #82196f0131](https://github.com/MariaDB/server/commit/82196f0131)\
  2017-04-03 17:18:37 +0200
  * [MDEV-11995](https://jira.mariadb.org/browse/MDEV-11995) ALTER TABLE proceeds despite reporting ER\_TOO\_LONG\_KEY error
* [Revision #30cbbfbf77](https://github.com/MariaDB/server/commit/30cbbfbf77)\
  2017-04-07 06:09:25 +0000
  * [MDEV-12452](https://jira.mariadb.org/browse/MDEV-12452) postfix - use C style cast, not reinterpret\_cast
* [Revision #73c57e2be7](https://github.com/MariaDB/server/commit/73c57e2be7)\
  2017-04-06 23:11:57 +0000
  * Fix building aws\_key\_management on Linux
* [Revision #b64910ce27](https://github.com/MariaDB/server/commit/b64910ce27)\
  2017-04-06 18:29:33 -0400
  * [MDEV-12452](https://jira.mariadb.org/browse/MDEV-12452) [MDEV-12453](https://jira.mariadb.org/browse/MDEV-12453) : Fix building rocksdb and aws\_key\_management on macOS
* [Revision #428a922cd0](https://github.com/MariaDB/server/commit/428a922cd0)\
  2017-04-06 12:08:14 -0700
  * Fixed the bug [MDEV-12440](https://jira.mariadb.org/browse/MDEV-12440).
* [Revision #1759e91986](https://github.com/MariaDB/server/commit/1759e91986)\
  2017-04-02 21:46:10 +1000
  * travis: osx - specify allowed\_failures accurately
* [Revision #08359bc570](https://github.com/MariaDB/server/commit/08359bc570)\
  2017-04-02 20:39:01 +1000
  * travis: OSX - 2 minute test case timeout
* [Revision #3bfb0b3bbd](https://github.com/MariaDB/server/commit/3bfb0b3bbd)\
  2017-04-02 20:20:32 +1000
  * Travis: Add OSX to tests (but allow failure)
* [Revision #46e2442f6f](https://github.com/MariaDB/server/commit/46e2442f6f)\
  2017-03-17 16:37:53 +1100
  * [MDEV-6262](https://jira.mariadb.org/browse/MDEV-6262): travis coverity support
* [Revision #fce645745b](https://github.com/MariaDB/server/commit/fce645745b)\
  2017-03-17 14:41:53 +1100
  * Travis: remove tokudb when building with clang
* [Revision #e130ee552a](https://github.com/MariaDB/server/commit/e130ee552a)\
  2017-03-17 13:33:21 +1100
  * Travis: remove Mroonga for clang
* [Revision #837fa86cf0](https://github.com/MariaDB/server/commit/837fa86cf0)\
  2017-03-17 13:09:00 +1100
  * Travis: add ccache for clang
* [Revision #cfd9a75c23](https://github.com/MariaDB/server/commit/cfd9a75c23)\
  2017-04-02 12:30:13 +1000
  * travis: disable main.mysqlhotcopy\_myisam in container builds
* [Revision #eb04ee5c9d](https://github.com/MariaDB/server/commit/eb04ee5c9d)\
  2017-03-17 12:50:21 +1100
  * Travis: llvm, additional packages and container
* Merge [Revision #d235782fca](https://github.com/MariaDB/server/commit/d235782fca) 2017-04-06 09:51:35 +0000 - Merge branch '10.1' into 10.2
* [Revision #b666732182](https://github.com/MariaDB/server/commit/b666732182)\
  2017-04-06 09:50:27 +0000
  * Do not link client plugins to mysqld
* Merge [Revision #1494147cf6](https://github.com/MariaDB/server/commit/1494147cf6) 2017-04-06 09:52:25 +0300 - Merge 10.1 into 10.2
* [Revision #25d69ea012](https://github.com/MariaDB/server/commit/25d69ea012)\
  2017-04-04 10:13:53 +0300
  * [MDEV-12198](https://jira.mariadb.org/browse/MDEV-12198) innodb\_defragment=1 crashes server on OPTIMIZE TABLE when FULLTEXT index exists
* Merge [Revision #8d4871a953](https://github.com/MariaDB/server/commit/8d4871a953) 2017-04-06 08:53:59 +0300 - Merge 10.0 into 10.1
* [Revision #57a699b0a0](https://github.com/MariaDB/server/commit/57a699b0a0)\
  2016-06-17 16:51:11 +0200
  * [MDEV-8642](https://jira.mariadb.org/browse/MDEV-8642): WHERE Clause not applied on View - Empty result set returned
* [Revision #8e36216a06](https://github.com/MariaDB/server/commit/8e36216a06)\
  2017-04-05 14:46:35 +0300
  * Import two ALTER TABLE…ALGORITHM=INPLACE tests from MySQL 5.6.
* [Revision #f2dc04abea](https://github.com/MariaDB/server/commit/f2dc04abea)\
  2017-04-03 18:48:48 +0000
  * Compiling, Windows . Avoid unnecessary rebuilds with MSVC.
* [Revision #ff6f4d7db1](https://github.com/MariaDB/server/commit/ff6f4d7db1)\
  2017-04-03 15:18:46 +0000
  * Windows : Fix compiling with VS2013
* [Revision #cd494f4cef](https://github.com/MariaDB/server/commit/cd494f4cef)\
  2017-04-05 08:54:20 +0300
  * fix warning "ignoring return value" of fwrite.
* Merge [Revision #64a37f6cab](https://github.com/MariaDB/server/commit/64a37f6cab) 2017-04-05 09:43:36 +0300 - Merge pull request #352 from grooverdan/10.1-xtradb-fil\_crypt\_rotate\_page
* [Revision #a7bb9e8fdb](https://github.com/MariaDB/server/commit/a7bb9e8fdb)\
  2017-04-05 16:29:08 +1000
  * xtradb: fil\_crypt\_rotate\_page, space\_id should be compared to TRX\_SYS\_SPACE not space
* Merge [Revision #85239bdfeb](https://github.com/MariaDB/server/commit/85239bdfeb) 2017-04-05 08:40:47 +0300 - Merge pull request #350 from grooverdan/10.1-TRX\_SYS\_PAGE\_NO
* [Revision #9a218f4fb8](https://github.com/MariaDB/server/commit/9a218f4fb8)\
  2017-04-04 15:47:21 +1000
  * fil\_crypt\_rotate\_page - space\_id should be compared to TRX\_SYS\_SPACE not space
* [Revision #d528fd72f2](https://github.com/MariaDB/server/commit/d528fd72f2)\
  2017-04-05 14:43:24 -0400
  * bump the VERSION
* [Revision #8423294acf](https://github.com/MariaDB/server/commit/8423294acf)\
  2017-04-05 16:24:44 +0300
  * Make InnoDB doublewrite buffer creation more robust.
* [Revision #35e582c917](https://github.com/MariaDB/server/commit/35e582c917)\
  2017-04-05 16:00:35 +0300
  * Adjust tests for the removal of kill\_and\_restart\_mysqld.inc.
* [Revision #0d34dd7cfb](https://github.com/MariaDB/server/commit/0d34dd7cfb)\
  2017-04-04 12:19:42 +0300
  * [MDEV-11840](https://jira.mariadb.org/browse/MDEV-11840) InnoDB: "Cannot open \<ib\_buffer\_pool file>" should not be an error

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
