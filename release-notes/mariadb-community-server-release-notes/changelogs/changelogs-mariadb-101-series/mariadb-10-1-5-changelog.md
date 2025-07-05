# MariaDB 10.1.5 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10148-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.5)[Release Notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes.md)[Changelog](mariadb-10-1-5-changelog.md)[Overview of 10.1](../../old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1.md)

**Release date:** 4 Jun 2015

For the highlights of this release, see the[release notes](../../old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-5-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #cd70bed](https://github.com/MariaDB/server/commit/cd70bed)\
  2015-06-03 11:12:50 +0200
  * fix for 32-bit tests
* [Revision #51d6763](https://github.com/MariaDB/server/commit/51d6763)\
  2015-05-27 20:53:41 +0200
  * AES-GCM support in file\_key\_management plugin
* [Revision #0f00927](https://github.com/MariaDB/server/commit/0f00927)\
  2015-05-27 20:53:16 +0200
  * my\_aes\_encrypt\_gcm() and my\_aes\_decrypt\_gcm()
* [Revision #ebc5e00](https://github.com/MariaDB/server/commit/ebc5e00)\
  2015-05-27 19:41:29 +0200
  * my\_aes\_get\_size()
* [Revision #487e5f4](https://github.com/MariaDB/server/commit/487e5f4)\
  2015-05-27 12:18:29 +0200
  * file\_key\_management plugin: complain if key id 1 is not found
* [Revision #432b78c](https://github.com/MariaDB/server/commit/432b78c)\
  2015-05-27 12:08:13 +0200
  * just like tempfiles: use key id 2 for temp Aria tables
* [Revision #d9340d6](https://github.com/MariaDB/server/commit/d9340d6)\
  2015-05-27 00:18:20 +0200
  * [MDEV-8126](https://jira.mariadb.org/browse/MDEV-8126) encryption for temp files
* [Revision #318c826](https://github.com/MariaDB/server/commit/318c826)\
  2015-05-26 22:09:40 +0200
  * always use my\_b\_pread() instead of mysql\_file\_pread()
* [Revision #6309a30](https://github.com/MariaDB/server/commit/6309a30)\
  2015-05-22 14:07:35 +0200
  * my\_b\_fill, inline my\_b\_\* functions instead of hairy macros
* [Revision #196e852](https://github.com/MariaDB/server/commit/196e852)\
  2015-05-18 11:54:55 +0200
  * misc IO\_CACHE cleanups
* [Revision #1841557](https://github.com/MariaDB/server/commit/1841557)\
  2015-05-27 21:43:25 +0200
  * myisam/aria: don't mess with IO\_CACHE::file
* [Revision #80e61ae](https://github.com/MariaDB/server/commit/80e61ae)\
  2015-05-16 08:48:52 +0200
  * cleanup: LOAD DATA replication support in IO\_CACHE
* [Revision #91dab5d](https://github.com/MariaDB/server/commit/91dab5d)\
  2015-06-02 18:09:53 +0200
  * fix cmake dependencies
* [Revision #72d01f2](https://github.com/MariaDB/server/commit/72d01f2)\
  2015-06-02 12:55:00 +0200
  * remove few #ifdefs in innodb/xtradb
* [Revision #5fc53b7](https://github.com/MariaDB/server/commit/5fc53b7)\
  2015-06-02 15:39:14 +0400
  * [MDEV-8202](https://jira.mariadb.org/browse/MDEV-8202) - st\_select\_lex::master\_unit() takes 0.17% in OLTP RO
* [Revision #adb952f](https://github.com/MariaDB/server/commit/adb952f)\
  2015-06-02 15:37:04 +0400
  * [MDEV-8192](https://jira.mariadb.org/browse/MDEV-8192) - THD::set\_command() takes 0.05% in OLTP RO
* [Revision #d298b02](https://github.com/MariaDB/server/commit/d298b02)\
  2015-06-02 15:35:02 +0400
  * [MDEV-8191](https://jira.mariadb.org/browse/MDEV-8191) - THD::set\_query() takes 0.07% in OLTP RO
* [Revision #3709c7f](https://github.com/MariaDB/server/commit/3709c7f)\
  2015-06-02 15:42:01 +0400
  * [MDEV-8222](https://jira.mariadb.org/browse/MDEV-8222) "string\_field LIKE int\_const" returns a wrong result in case of UCS2 [MDEV-8257](https://jira.mariadb.org/browse/MDEV-8257) Erroneous "Impossible where" when mixing decimal comparison and LIKE
* [Revision #8f92a70](https://github.com/MariaDB/server/commit/8f92a70)\
  2015-06-02 09:26:16 +0200
  * update for 32-bit, again
* [Revision #0d54cb1](https://github.com/MariaDB/server/commit/0d54cb1)\
  2015-06-01 21:35:02 +0200
  * compilation failure on windows
* [Revision #2133230](https://github.com/MariaDB/server/commit/2133230)\
  2015-06-01 21:31:31 +0200
  * avoid ulong sysvars, prefer uint or ulonglong
* [Revision #78c10cc](https://github.com/MariaDB/server/commit/78c10cc)\
  2015-06-01 17:31:39 +0200
  * [MDEV-7913](https://jira.mariadb.org/browse/MDEV-7913) main.openssl\_6975 'tlsv10' fails in buildbot on Wheezy and Precise
* [Revision #9c41b35](https://github.com/MariaDB/server/commit/9c41b35)\
  2015-06-01 16:33:41 +0200
  * [MDEV-8220](https://jira.mariadb.org/browse/MDEV-8220) Server crashes if started with --enforce-storage-engine option
* [Revision #fce4ab0](https://github.com/MariaDB/server/commit/fce4ab0)\
  2015-06-01 16:01:23 +0200
  * generalize ER\_TABLE\_NEEDS\_UPGRADE to work for views too
* [Revision #5283789](https://github.com/MariaDB/server/commit/5283789)\
  2015-05-31 08:10:07 +0300
  * Fix test warnings by adding global supression to InnoDB warnings.
* [Revision #13235a5](https://github.com/MariaDB/server/commit/13235a5)\
  2015-05-31 07:53:20 +0300
  * Fix compiler warning.
* [Revision #59815a2](https://github.com/MariaDB/server/commit/59815a2)\
  2015-05-22 08:24:59 +0300
  * [MDEV-7484](https://jira.mariadb.org/browse/MDEV-7484): Log Time not consistent with InnoDB errors nor with MySQL error log time format
* [Revision #84eaf09](https://github.com/MariaDB/server/commit/84eaf09)\
  2015-05-30 14:06:17 +0200
  * [MDEV-7913](https://jira.mariadb.org/browse/MDEV-7913) main.openssl\_6975 'tlsv10' fails in buildbot on Wheezy and Precise
* [Revision #3839e91](https://github.com/MariaDB/server/commit/3839e91)\
  2015-05-30 12:13:45 +0300
  * [MDEV-8248](https://jira.mariadb.org/browse/MDEV-8248): mysqldump incorrect identifier quoting during equality comparison
* [Revision #ae4b243](https://github.com/MariaDB/server/commit/ae4b243)\
  2015-03-19 15:16:22 +0200
  * [MDEV-6714](https://jira.mariadb.org/browse/MDEV-6714) mysqldump slow with tables in big databases
* [Revision #c6b4212](https://github.com/MariaDB/server/commit/c6b4212)\
  2015-05-30 09:13:49 +0200
  * temporarily disable failing test
* [Revision #0f01bf2](https://github.com/MariaDB/server/commit/0f01bf2)\
  2015-05-28 07:59:57 +0200
  * [MDEV-8241](https://jira.mariadb.org/browse/MDEV-8241): Debug build on Windows is broken: error LNK2019: unresolved external symbol pthread\_detach referenced in function ma\_checkpoint\_init
* [Revision #c1c22c0](https://github.com/MariaDB/server/commit/c1c22c0)\
  2015-05-29 21:23:52 +0200
  * update test results
* [Revision #903cfde](https://github.com/MariaDB/server/commit/903cfde)\
  2015-05-29 11:26:46 -0400
  * [MDEV-7067](https://jira.mariadb.org/browse/MDEV-7067): Server outputs Galera (WSREP) information, even if Galera is disabled
* [Revision #1b00edc](https://github.com/MariaDB/server/commit/1b00edc)\
  2015-05-21 16:31:24 +0200
  * [MDEV-7011](https://jira.mariadb.org/browse/MDEV-7011): MAX\_STATEMENT\_TIME has no effect in a procedure after a previous successful statement
* [Revision #34e01f8](https://github.com/MariaDB/server/commit/34e01f8)\
  2015-05-28 10:03:12 +0200
  * restore innodb\_encrypt\_tables validation function
* [Revision #5443b9d](https://github.com/MariaDB/server/commit/5443b9d)\
  2015-05-28 16:00:05 +0400
  * Moving "bool abort\_on\_null" from Item\_bool\_func2 to Item\_func\_eq, as it's not used by the other Item\_bool\_func2 descendands.
* [Revision #979c504](https://github.com/MariaDB/server/commit/979c504)\
  2015-05-28 07:52:27 +0300
  * [MDEV-8242](https://jira.mariadb.org/browse/MDEV-8242): encryption.innodb\_page\_encryption\_key\_change fails in buildbot
* [Revision #ab5094b](https://github.com/MariaDB/server/commit/ab5094b)\
  2015-05-27 21:41:02 +0400
  * Fixing typos in DBUG\_ENTER() comments.
* [Revision #5991efc](https://github.com/MariaDB/server/commit/5991efc)\
  2015-05-27 21:32:35 +0400
  * [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO Step #8: Adding get\_mm\_tree() in Item\_func, Item\_func\_between, Item\_func\_in, Item\_equal. This removes one virtual call item->type() in queries like: SELECT \* FROM t1 WHERE c BETWEEN const1 AND const2; SELECT \* FROM t1 WHERE c>const; SELECT \* FROM t1 WHERE c IN (const\_list);
* [Revision #a25ccd4](https://github.com/MariaDB/server/commit/a25ccd4)\
  2015-05-27 15:37:13 +0300
  * [MDEV-8238](https://jira.mariadb.org/browse/MDEV-8238): Tables with encryption=yes using file\_key\_management plugin are not encrypted
* [Revision #2bea4bd](https://github.com/MariaDB/server/commit/2bea4bd)\
  2015-05-26 14:59:39 +0300
  * [MDEV-8233](https://jira.mariadb.org/browse/MDEV-8233): InnoDB: Assertion failure in fil\_page\_decompress with encrypted tables
* [Revision #0dc1425](https://github.com/MariaDB/server/commit/0dc1425)\
  2015-05-27 12:03:20 +0400
  * [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO Step #7 (mostly preparatory for the next step #8): Splitting the function get\_mm\_parts() into a virtual method in Item. This changes a virtual call for item->type() into a virtual call for item->get\_mm\_tree(), but also _removes_ one virtual call Item\_cond::functype(), which used to distinguish between COND\_AND\_FUNC vs COND\_OR\_FUNC.
* [Revision #58d7e35](https://github.com/MariaDB/server/commit/58d7e35)\
  2015-05-27 11:00:46 +0300
  * Fixed innodb\_scrub\_background test.
* [Revision #8c0ea28](https://github.com/MariaDB/server/commit/8c0ea28)\
  2015-05-26 16:09:36 +0300
  * [MDEV-8213](https://jira.mariadb.org/browse/MDEV-8213): encryption.encryption\_force, encryption.encrypt\_and\_grep fail with valgrind warnings (Invalid read)
* [Revision #e5f1e84](https://github.com/MariaDB/server/commit/e5f1e84)\
  2015-05-26 12:47:35 +0200
  * [MDEV-8147](https://jira.mariadb.org/browse/MDEV-8147): Assertion \`m\_lock\_type == 2' failed in handler::ha\_close() during parallel replication
* [Revision #5bd25a9](https://github.com/MariaDB/server/commit/5bd25a9)\
  2015-05-26 11:59:17 +0400
  * A helper patch for "[MDEV-8228](https://jira.mariadb.org/browse/MDEV-8228) Move Item\_func\_like out of Item\_bool\_func2"
* [Revision #b3aece9](https://github.com/MariaDB/server/commit/b3aece9)\
  2015-05-25 09:38:47 +0300
  * [MDEV-8209](https://jira.mariadb.org/browse/MDEV-8209): encryption.encrypt\_and\_grep fails in buildbot and outside
* [Revision #536112d](https://github.com/MariaDB/server/commit/536112d)\
  2015-05-21 15:07:19 +0300
  * [MDEV-8195](https://jira.mariadb.org/browse/MDEV-8195): InnoDB: Error: trying to access tablespace 11262 page no. 7, InnoDB: but the tablespace does not exist or is just being dropped.
* [Revision #8635c4b](https://github.com/MariaDB/server/commit/8635c4b)\
  2015-05-21 11:02:03 +0300
  * Fix test failure.
* [Revision #137ba7d](https://github.com/MariaDB/server/commit/137ba7d)\
  2015-05-21 08:14:35 +0300
  * Fix compiler error.
* [Revision #925b641](https://github.com/MariaDB/server/commit/925b641)\
  2015-05-20 20:32:10 +0300
  * [MDEV-8182](https://jira.mariadb.org/browse/MDEV-8182): Failing assertion: 1 == UT\_LIST\_GET\_LEN(space->chain)
* [Revision #3e55ef2](https://github.com/MariaDB/server/commit/3e55ef2)\
  2015-05-20 13:35:51 +0300
  * [MDEV-8173](https://jira.mariadb.org/browse/MDEV-8173): InnoDB; Failing assertion: crypt\_data->type == 1
* [Revision #44cd6f2](https://github.com/MariaDB/server/commit/44cd6f2)\
  2015-05-20 11:36:26 +0200
  * [MDEV-7921](https://jira.mariadb.org/browse/MDEV-7921): main.sp\_sync fails in buildbot with valgrind
* [Revision #c1fb91e](https://github.com/MariaDB/server/commit/c1fb91e)\
  2015-05-18 17:34:50 +0200
  * [MDEV-7921](https://jira.mariadb.org/browse/MDEV-7921): main.sp\_sync fails in buildbot with valgrind
* [Revision #80333ad](https://github.com/MariaDB/server/commit/80333ad)\
  2015-05-20 07:57:55 +0300
  * Add missing requirement to test case and remove unnecessary output.
* [Revision #bb15b9e](https://github.com/MariaDB/server/commit/bb15b9e)\
  2015-05-19 17:03:18 +0400
  * [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO
* [Revision #bac6bba](https://github.com/MariaDB/server/commit/bac6bba)\
  2015-05-19 12:04:09 +0000
  * \[[MDEV-8063](https://jira.mariadb.org/browse/MDEV-8063)]: Fix incorrect commit.
* [Revision #29c7aff](https://github.com/MariaDB/server/commit/29c7aff)\
  2015-05-18 01:35:47 +0000
  * [MDEV-8063](https://jira.mariadb.org/browse/MDEV-8063): Unconditional ANALYZE DELETE does not delete rows
* [Revision #20c2304](https://github.com/MariaDB/server/commit/20c2304)\
  2015-05-17 14:14:16 +0300
  * [MDEV-8164](https://jira.mariadb.org/browse/MDEV-8164): Server crashes in pfs\_mutex\_enter\_func after fil\_crypt\_is\_closing or alike
* [Revision #476dfb1](https://github.com/MariaDB/server/commit/476dfb1)\
  2015-05-16 08:55:21 +0200
  * update big tokudb test results after dd8f93195
* [Revision #9cc7eb3](https://github.com/MariaDB/server/commit/9cc7eb3)\
  2015-05-16 16:27:36 +0200
  * upate test results after 2300fe2e
* [Revision #54672a4](https://github.com/MariaDB/server/commit/54672a4)\
  2015-05-15 09:54:41 +0200
  * [MDEV-8043](https://jira.mariadb.org/browse/MDEV-8043) innodb tablespace encryption
* [Revision #e5989d5](https://github.com/MariaDB/server/commit/e5989d5)\
  2015-05-14 12:27:49 +0200
  * InnoDB: simplify innobase\_compression\_algorithm\_validate()
* [Revision #8815fb3](https://github.com/MariaDB/server/commit/8815fb3)\
  2015-05-14 12:25:47 +0200
  * [MDEV-8158](https://jira.mariadb.org/browse/MDEV-8158) InnoDB: Failing assertion: new\_state->key\_version != ENCRYPTION\_KEY\_VERSION\_INVALID on dynamic change of encryption variables
* [Revision #8827eb8](https://github.com/MariaDB/server/commit/8827eb8)\
  2015-05-14 10:35:30 +0200
  * [MDEV-8162](https://jira.mariadb.org/browse/MDEV-8162) func\_str crashes on SELECT AES\_DECRYPT(AES\_ENCRYPT(...)) on line 107
* [Revision #8258a34](https://github.com/MariaDB/server/commit/8258a34)\
  2015-05-14 10:13:03 +0200
  * InnoDB: check if scrubbing is enabled before scanning the tablespace
* [Revision #a94cabd](https://github.com/MariaDB/server/commit/a94cabd)\
  2015-05-14 08:37:34 +0200
  * [MDEV-8159](https://jira.mariadb.org/browse/MDEV-8159) InnoDB: Failing assertion: key\_state->key\_id
* [Revision #2300fe2](https://github.com/MariaDB/server/commit/2300fe2)\
  2015-05-13 21:57:24 +0200
  * Identical key derivation code in XtraDB/InnoDB/Aria
* [Revision #632f230](https://github.com/MariaDB/server/commit/632f230)\
  2015-05-14 17:42:40 +0400
  * [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO Step#5: changing the function remove\_eq\_conds() into a virtual method in Item. It removes 6 virtual calls for Item\_func::type(), and adds only 2 virtual calls for Item\*::remove\_eq\_conds().
* [Revision #fb3e935](https://github.com/MariaDB/server/commit/fb3e935)\
  2015-05-14 12:44:07 +0400
  * [MDEV-7999](https://jira.mariadb.org/browse/MDEV-7999) - PROFILING routines take 0.2% when profiling disabled
* [Revision #18f88d6](https://github.com/MariaDB/server/commit/18f88d6)\
  2015-04-22 14:18:51 +0400
  * [MDEV-7943](https://jira.mariadb.org/browse/MDEV-7943) - pthread\_getspecific() takes 0.76% in OLTP RO
* [Revision #f8cacd0](https://github.com/MariaDB/server/commit/f8cacd0)\
  2015-05-13 11:41:22 +0300
  * [MDEV-8143](https://jira.mariadb.org/browse/MDEV-8143): InnoDB: Database page corruption on disk or a failed file read
* [Revision #be2038e](https://github.com/MariaDB/server/commit/be2038e)\
  2015-05-13 17:08:24 +0400
  * [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO Step 4 (there will be more)
* [Revision #16b6ec2](https://github.com/MariaDB/server/commit/16b6ec2)\
  2015-05-12 09:43:26 +0200
  * [MDEV-8130](https://jira.mariadb.org/browse/MDEV-8130) Wrong error code/message while encrypting a partitioned InnoDB table
* [Revision #def48e6](https://github.com/MariaDB/server/commit/def48e6)\
  2015-05-11 21:05:02 +0200
  * [MDEV-8141](https://jira.mariadb.org/browse/MDEV-8141) InnoDB: background encryption thread uses FIL\_DEFAULT\_ENCRYPTION\_KEY
* [Revision #6e4c22a](https://github.com/MariaDB/server/commit/6e4c22a)\
  2015-05-11 14:21:44 +0200
  * example encryption plugin supports key ids
* [Revision #acd992d](https://github.com/MariaDB/server/commit/acd992d)\
  2015-05-10 20:57:16 +0200
  * [MDEV-8022](https://jira.mariadb.org/browse/MDEV-8022) Assertion \`rc == 0' failed in ma\_encrypt on dropping an encrypted Aria table
* [Revision #bea3f30](https://github.com/MariaDB/server/commit/bea3f30)\
  2015-05-10 19:57:43 +0200
  * move AES\_CTR to its own greatly simplified function
* [Revision #a583976](https://github.com/MariaDB/server/commit/a583976)\
  2015-05-10 11:44:08 +0200
  * [MDEV-8015](https://jira.mariadb.org/browse/MDEV-8015) InnoDB: Failing assertion: new\_state->key\_version != ENCRYPTION\_KEY\_VERSION\_INVALID
* [Revision #b4777bf](https://github.com/MariaDB/server/commit/b4777bf)\
  2015-05-11 19:03:19 +0200
  * cleanup, use encryption\_key\_id\_exists() where appropriate
* [Revision #6638091](https://github.com/MariaDB/server/commit/6638091)\
  2015-05-10 11:03:33 +0200
  * [MDEV-7993](https://jira.mariadb.org/browse/MDEV-7993) file\_key\_management\_filekey doesn't work as expected with FILE:
* [Revision #a35b538](https://github.com/MariaDB/server/commit/a35b538)\
  2015-05-09 19:13:18 +0200
  * [MDEV-8040](https://jira.mariadb.org/browse/MDEV-8040) make aria encryption use real keys
* [Revision #ab8415d](https://github.com/MariaDB/server/commit/ab8415d)\
  2015-05-09 12:31:53 +0200
  * move encryption tests to a dedicate suite
* [Revision #b229599](https://github.com/MariaDB/server/commit/b229599)\
  2015-04-22 13:29:56 +0400
  * [MDEV-7943](https://jira.mariadb.org/browse/MDEV-7943) - pthread\_getspecific() takes 0.76% in OLTP RO
* [Revision #8345bc6](https://github.com/MariaDB/server/commit/8345bc6)\
  2015-05-13 15:34:20 +0400
  * [MDEV-8152](https://jira.mariadb.org/browse/MDEV-8152) is\_columns\_is\_embedded test fails Recording --ps and --embedded tests (a postfix for [MDEV-7807](https://jira.mariadb.org/browse/MDEV-7807))
* [Revision #9851a81](https://github.com/MariaDB/server/commit/9851a81)\
  2015-05-13 15:28:34 +0400
  * [MDEV-8001](https://jira.mariadb.org/browse/MDEV-8001) - mysql\_reset\_thd\_for\_next\_command() takes 0.04% in OLTP RO
* [Revision #4d1ccc4](https://github.com/MariaDB/server/commit/4d1ccc4)\
  2015-04-17 14:30:15 +0400
  * [MDEV-7951](https://jira.mariadb.org/browse/MDEV-7951) - sql\_alloc() takes 0.25% in OLTP RO
* [Revision #c4d2c4e](https://github.com/MariaDB/server/commit/c4d2c4e)\
  2015-04-16 18:38:26 +0400
  * [MDEV-7964](https://jira.mariadb.org/browse/MDEV-7964) - delete\_dynamic() takes 0.12% in OLTP RO
* [Revision #7cfa803](https://github.com/MariaDB/server/commit/7cfa803)\
  2015-04-15 18:32:34 +0400
  * [MDEV-8001](https://jira.mariadb.org/browse/MDEV-8001) - mysql\_reset\_thd\_for\_next\_command() takes 0.04% in OLTP RO
* [Revision #5cfb6b4](https://github.com/MariaDB/server/commit/5cfb6b4)\
  2015-04-15 18:12:23 +0400
  * [MDEV-7999](https://jira.mariadb.org/browse/MDEV-7999) - PROFILING routines take 0.2% when profiling disabled
* [Revision #55d5af7](https://github.com/MariaDB/server/commit/55d5af7)\
  2015-04-15 11:29:01 +0400
  * [MDEV-7945](https://jira.mariadb.org/browse/MDEV-7945) - THD::enter\_stage() takes 0.48% in OLTP RO
* [Revision #c8ad5b2](https://github.com/MariaDB/server/commit/c8ad5b2)\
  2015-05-12 17:15:16 -0400
  * [MDEV-8151](https://jira.mariadb.org/browse/MDEV-8151) : wsrep.foreign\_key, wsrep.pool\_of\_threads,
* [Revision #8c54182](https://github.com/MariaDB/server/commit/8c54182)\
  2015-05-12 15:09:28 +0500
  * [MDEV-7926](https://jira.mariadb.org/browse/MDEV-7926) Server crashes in get\_geometry\_column\_record on concurrent SELECT FROM I\_S.GEOMETRY\_COLUMNS with join and DDL. The bug was that open\_tables() returned error in case of thd->killed() without properly calling thd->send\_kill\_message() to set the correct error. This was fixed already in get\_schema\_column\_record, so the code was just copied to get\_geometry\_column\_record.
* [Revision #58e8db2](https://github.com/MariaDB/server/commit/58e8db2)\
  2015-05-11 14:29:14 +0300
  * [MDEV-7942](https://jira.mariadb.org/browse/MDEV-7942): InnoDB: abuse of UNIV\_LIKELY()/UNIV\_UNLIKELY()
* [Revision #6e49201](https://github.com/MariaDB/server/commit/6e49201)\
  2015-05-11 12:47:43 +0200
  * Fix compilation warnings in -DWITH\_WSREP=OFF build.
* [Revision #8bedb63](https://github.com/MariaDB/server/commit/8bedb63)\
  2015-05-11 11:55:58 +0200
  * [MDEV-8113](https://jira.mariadb.org/browse/MDEV-8113): Parallel slave: slave hangs on ALTER TABLE (or other DDL) as the first event after slave start
* [Revision #ecfc3de](https://github.com/MariaDB/server/commit/ecfc3de)\
  2015-05-11 09:21:04 +0300
  * [MDEV-8129](https://jira.mariadb.org/browse/MDEV-8129): Compilation warnings in log0crypt.cc
* [Revision #5fdb145](https://github.com/MariaDB/server/commit/5fdb145)\
  2015-05-09 11:19:36 +0200
  * [MDEV-8021](https://jira.mariadb.org/browse/MDEV-8021) "InnoDB: Tablespace id 4 encrypted but encryption service not available. Can't continue opening tablespace" on server restart when there are encrypted tables
* [Revision #d259376](https://github.com/MariaDB/server/commit/d259376)\
  2015-05-07 19:13:22 +0300
  * [MDEV-8041](https://jira.mariadb.org/browse/MDEV-8041): InnoDB redo log encryption
* [Revision #ab54f5a](https://github.com/MariaDB/server/commit/ab54f5a)\
  2015-05-08 17:31:54 +0300
  * Fix win/ files to be stored with LF in repository
* [Revision #5ae8d06](https://github.com/MariaDB/server/commit/5ae8d06)\
  2015-05-08 17:27:41 +0300
  * Update .gitattributes
* [Revision #0880284](https://github.com/MariaDB/server/commit/0880284)\
  2015-05-08 17:06:35 +0300
  * Fix win/ files to be stored with LF in repository
* [Revision #c1b07ff](https://github.com/MariaDB/server/commit/c1b07ff)\
  2015-05-08 11:56:48 +0200
  * update .gitattributes
* [Revision #b5c5f31](https://github.com/MariaDB/server/commit/b5c5f31)\
  2015-05-08 11:48:16 +0200
  * convert files from CRLF to LF line endings
* [Revision #e774008](https://github.com/MariaDB/server/commit/e774008)\
  2015-05-08 11:48:02 +0200
  * bump the VERSION
* [Revision #91ee98a](https://github.com/MariaDB/server/commit/91ee98a)\
  2015-05-08 00:34:06 +0400
  * [MDEV-7807](https://jira.mariadb.org/browse/MDEV-7807) information\_schema.processlist truncates queries with binary strings
* [Revision #0014bdc](https://github.com/MariaDB/server/commit/0014bdc)\
  2015-05-07 22:18:34 +0200
  * [MDEV-8115](https://jira.mariadb.org/browse/MDEV-8115) mysql\_upgrade crashes the server with REPAIR VIEW
* [Revision #0fcc350](https://github.com/MariaDB/server/commit/0fcc350)\
  2015-04-08 10:55:51 +0400
  * [MDEV-7922](https://jira.mariadb.org/browse/MDEV-7922) - ERROR 1939 (HY000): Engine PERFORMANCE\_SCHEMA failed to discover table
* [Revision #3832bda](https://github.com/MariaDB/server/commit/3832bda)\
  2015-05-07 14:00:14 +0300
  * Fix compiler error if compiler does not support c99 style initializers.
* [Revision #7ed673f](https://github.com/MariaDB/server/commit/7ed673f)\
  2015-03-17 19:49:04 +0400
  * [MDEV-7793](https://jira.mariadb.org/browse/MDEV-7793) - Race condition between XA COMMIT/ROLLBACK and disconnect
* [Revision #8350ea0](https://github.com/MariaDB/server/commit/8350ea0)\
  2015-05-07 13:04:03 +0300
  * Fix compiler error if compiler does not support c99 style initializers.
* [Revision #a1ad712](https://github.com/MariaDB/server/commit/a1ad712)\
  2015-05-07 07:39:45 +0400
  * Fixing connect.dbf test failures on big endian machines.
* [Revision #bad81f2](https://github.com/MariaDB/server/commit/bad81f2)\
  2015-05-06 15:16:28 +0300
  * [MDEV-8046](https://jira.mariadb.org/browse/MDEV-8046): Server crashes in pfs\_mutex\_enter\_func on select from I\_S.INNODB\_TABLESPACES\_ENCRYPTION if InnoDB is disabled
* [Revision #2f25c65](https://github.com/MariaDB/server/commit/2f25c65)\
  2015-05-06 14:09:10 +0300
  * [MDEV-8074](https://jira.mariadb.org/browse/MDEV-8074): Failing assertion: mutex->magic\_n == MUTEX\_MAGIC\_N in file sync0sync.cc line 508
* [Revision #ef99edf](https://github.com/MariaDB/server/commit/ef99edf)\
  2015-05-06 12:24:15 +0200
  * [MDEV-8103](https://jira.mariadb.org/browse/MDEV-8103): Missing DBUG\_RETURN in open\_table\_uncached()
* [Revision #a82f475](https://github.com/MariaDB/server/commit/a82f475)\
  2015-05-05 11:37:21 +0200\
  \*
  * Fix a regression bug on (XML) HTML tables. modified: tabxml.cpp added: xml\_html.test xml\_html.result beers.xml coffee.htm
* [Revision #c09c265](https://github.com/MariaDB/server/commit/c09c265)\
  2015-05-05 22:05:05 +0200
  * Fix [MDEV-8090](https://jira.mariadb.org/browse/MDEV-8090) in tabmysql.cpp
* [Revision #95797b9](https://github.com/MariaDB/server/commit/95797b9)\
  2015-05-05 20:23:22 +0200
  * [MDEV-8096](https://jira.mariadb.org/browse/MDEV-8096) vio timeouts are multiplied by 1000 for ssl
* [Revision #d3a3adb](https://github.com/MariaDB/server/commit/d3a3adb)\
  2015-05-05 21:19:53 +0300
  * [MDEV-7985](https://jira.mariadb.org/browse/MDEV-7985): MySQL Users Break when Migrating to MariaDB, part 2
* [Revision #9304737](https://github.com/MariaDB/server/commit/9304737)\
  2015-05-05 16:28:23 +0200
  * mroonga doesn't work in embedded anymore
* [Revision #e4fde09](https://github.com/MariaDB/server/commit/e4fde09)\
  2015-05-05 15:39:32 +0400
  * Temporarily disabling Mroonga on Solaris (See [MDEV-7440](https://jira.mariadb.org/browse/MDEV-7440) Build fails in libgroonga on Solaris)
* [Revision #73c2356](https://github.com/MariaDB/server/commit/73c2356)\
  2015-05-05 13:22:09 +0400
  * [MDEV-7778](https://jira.mariadb.org/browse/MDEV-7778) impossible create copy of table, if table contain default value for timestamp field [MDEV-8082](https://jira.mariadb.org/browse/MDEV-8082) ON UPDATE is not preserved by CREATE TABLE .. SELECT
* [Revision #dd0207b](https://github.com/MariaDB/server/commit/dd0207b)\
  2015-05-05 08:53:52 +0200
  * .gitignore: add generated mroonga \*.result files
* [Revision #539b3ca](https://github.com/MariaDB/server/commit/539b3ca)\
  2015-05-05 09:30:17 +0400\
  \*
  * Moving Item\_func\_spatial\_mbr\_rel from Item\_bool\_func2 to Item\_bool\_func, as Item\_func\_spatial\_mbr\_rel needs nothing from Item\_bool\_func2. - Renaming Item\_func\_spacial\_rel (the class that implements precise spacial relations) to Item\_func\_spatial\_precise\_rel - Adding a new abstract class Item\_func\_spatial\_rel as a common parent for Item\_func\_spatial\_precise\_rel and Item\_func\_spatial\_mbr\_rel.
* [Revision #872cbb8](https://github.com/MariaDB/server/commit/872cbb8)\
  2015-05-05 13:48:54 +0900
  * revert CMakeList.txt at groonga-normalizer-mysql/normalizers
* [Revision #2fe4d0e](https://github.com/MariaDB/server/commit/2fe4d0e)\
  2015-05-05 01:09:47 +0400
  * [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO Step #3: Splitting the function check\_equality() into a method in Item. Implementing Item::check\_equality() and Item\_func\_eq::check\_equality(). Implement Item\_func\_eq::build\_equal\_items() in addition to Item\_func::build\_equal\_items() and moving the call for check\_equality() from Item\_func::build\_equal\_items() to Item\_func\_eq::build\_equal\_items().
* [Revision #d33cef1](https://github.com/MariaDB/server/commit/d33cef1)\
  2015-05-05 05:26:06 +0900
  * add -fPIC for groonga-normalizer-mysql
* [Revision #c4cc91c](https://github.com/MariaDB/server/commit/c4cc91c)\
  2015-05-04 22:19:22 +0200
  * 8.37
* [Revision #a4416ab](https://github.com/MariaDB/server/commit/a4416ab)\
  2015-05-04 22:17:04 +0200
  * 5.6.23-72.1
* [Revision #d71d411](https://github.com/MariaDB/server/commit/d71d411)\
  2015-05-04 22:16:00 +0200
  * 5.6.24
* [Revision #085297a](https://github.com/MariaDB/server/commit/085297a)\
  2015-05-04 22:13:46 +0200
  * 5.6.24
* [Revision #9130cc7](https://github.com/MariaDB/server/commit/9130cc7)\
  2015-05-05 03:09:34 +0900
  * update Spider to 3.2.21
* [Revision #d18becc](https://github.com/MariaDB/server/commit/d18becc)\
  2015-05-05 02:43:19 +0900
  * add -fPIC for groonga-normalizer-mysql
* [Revision #e2a87bd](https://github.com/MariaDB/server/commit/e2a87bd)\
  2015-05-04 19:20:59 +0200
  * move to storage/sphinx
* [Revision #6d06fbb](https://github.com/MariaDB/server/commit/6d06fbb)\
  2015-05-04 19:17:21 +0200
  * move to storage/innobase
* [Revision #14a142f](https://github.com/MariaDB/server/commit/14a142f)\
  2015-05-04 19:15:28 +0200
  * move to storage/xtradb
* [Revision #9090c3e](https://github.com/MariaDB/server/commit/9090c3e)\
  2015-05-04 18:31:24 +0400
  * Adding a test for Item\_default\_value in WHERE condition: WHERE DEFAULT(col) It seems this was not covered yet.
* [Revision #462bca3](https://github.com/MariaDB/server/commit/462bca3)\
  2015-05-04 18:12:31 +0400
  * [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO Step 2c:
* [Revision #ae18a28](https://github.com/MariaDB/server/commit/ae18a28)\
  2015-05-04 08:32:05 +0200
  * [MDEV-7973](https://jira.mariadb.org/browse/MDEV-7973) bigint fail with gcc 5.0
* [Revision #2983686](https://github.com/MariaDB/server/commit/2983686)\
  2015-05-03 18:26:02 +0200
  * [MDEV-8045](https://jira.mariadb.org/browse/MDEV-8045) Assertion \`0' fails in Protocol::end\_statement on CREATE VIEW after another connection aborted
* [Revision #8e797ae](https://github.com/MariaDB/server/commit/8e797ae)\
  2015-05-03 14:43:34 +0200
  * [MDEV-8014](https://jira.mariadb.org/browse/MDEV-8014) MariaDB client can hang in an infinite loop
* [Revision #dbe97bc](https://github.com/MariaDB/server/commit/dbe97bc)\
  2015-05-03 11:51:22 +0200
  * clarify the test case
* [Revision #532de70](https://github.com/MariaDB/server/commit/532de70)\
  2015-05-03 11:31:04 +0200
  * more tests, moving code around
* [Revision #ef1eb9c](https://github.com/MariaDB/server/commit/ef1eb9c)\
  2015-05-02 12:32:10 +0200
  * SSL: Verbosely report SSL initialization errors
* [Revision #601dcd4](https://github.com/MariaDB/server/commit/601dcd4)\
  2015-05-02 08:46:04 +0200
  * [MDEV-7794](https://jira.mariadb.org/browse/MDEV-7794) MariaDB - mysql-test - fips: some ssl tests with cipher are failing
* [Revision #7e7dd8e](https://github.com/MariaDB/server/commit/7e7dd8e)\
  2015-05-02 08:45:10 +0200
  * [MDEV-7695](https://jira.mariadb.org/browse/MDEV-7695) MariaDB - ssl - fips: can not connect with --ssl-cipher=DHE-RSA-AES256-SHA - handshake failure
* [Revision #e1e1f94](https://github.com/MariaDB/server/commit/e1e1f94)\
  2015-05-01 18:53:18 +0200
  * remove unused file and unnecessary #include
* [Revision #93c563d](https://github.com/MariaDB/server/commit/93c563d)\
  2015-05-01 18:52:29 +0200
  * [MDEV-7788](https://jira.mariadb.org/browse/MDEV-7788) my\_md5 crashes with openssl in fips mode
* [Revision #cc12a35](https://github.com/MariaDB/server/commit/cc12a35)\
  2015-05-01 17:56:47 +0200
  * [MDEV-7697](https://jira.mariadb.org/browse/MDEV-7697) Client reports ERROR 2006 (MySQL server has gone away) or ERROR 2013 (Lost connection to MySQL server during query) while executing AES\* functions under SSL
* [Revision #f875c9f](https://github.com/MariaDB/server/commit/f875c9f)\
  2015-04-30 19:48:11 +0200
  * [MDEV-5114](https://jira.mariadb.org/browse/MDEV-5114) seconds\_behind\_master flips to 0 & spikes back, when running show slaves status
* [Revision #e6d918c](https://github.com/MariaDB/server/commit/e6d918c)\
  2015-05-03 06:44:08 +0200
  * init\_status\_vars() was not invoked for embedded
* [Revision #91f8931](https://github.com/MariaDB/server/commit/91f8931)\
  2015-05-03 06:51:33 +0200
  * reformat long strings
* [Revision #6c55e52](https://github.com/MariaDB/server/commit/6c55e52)\
  2015-03-13 20:12:22 +0200
  * [MDEV-7774](https://jira.mariadb.org/browse/MDEV-7774): Crash when dropping user within rebuild\_role\_grants
* [Revision #acab0fa](https://github.com/MariaDB/server/commit/acab0fa)\
  2015-05-02 21:46:32 +0300
  * [MDEV-7038](https://jira.mariadb.org/browse/MDEV-7038) Assertion \`status\_var.memory\_used == 0' failed in THD::THD() on disconnect after executing EXPLAIN for multi-table UPDATE
* [Revision #f5b05a1](https://github.com/MariaDB/server/commit/f5b05a1)\
  2015-05-01 15:59:12 +0200\
  \*
  * Fix bug on updating JSON expanded values modified: json.result tabjson.cpp tabjson.h
* [Revision #37093eb](https://github.com/MariaDB/server/commit/37093eb)\
  2015-05-01 14:51:50 +0300
  * [MDEV-8079](https://jira.mariadb.org/browse/MDEV-8079): Crash when running MariaDB Debug with InnoDB on Windows
* [Revision #53382ac](https://github.com/MariaDB/server/commit/53382ac)\
  2015-05-01 14:23:08 +0300
  * [MDEV-8079](https://jira.mariadb.org/browse/MDEV-8079): Crash when running MariaDB Debug with InnoDB on Windows
* [Revision #2bb0e71](https://github.com/MariaDB/server/commit/2bb0e71)\
  2015-03-12 07:08:31 +1100
  * Alter online table x (no options) possible
* [Revision #320240b](https://github.com/MariaDB/server/commit/320240b)\
  2015-04-30 10:23:36 -0400
  * Merge test for bug#72594 from upstream
* [Revision #ff1e082](https://github.com/MariaDB/server/commit/ff1e082)\
  2015-04-30 12:36:39 +0400
  * [MDEV-8073](https://jira.mariadb.org/browse/MDEV-8073) - Build error in sql/mdl.cc on OS X 10.10
* [Revision #a0fdb25](https://github.com/MariaDB/server/commit/a0fdb25)\
  2015-04-30 04:44:30 +0900
  * Update Mroonga to the latest version on 2015-04-30T04:44:30+0900
* [Revision #499deca](https://github.com/MariaDB/server/commit/499deca)\
  2015-04-29 17:53:27 +0400
  * A clean-up for c8141f53140054282306d17459310fbca94cbf0e [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO (Step#2)
* [Revision #a4477d2](https://github.com/MariaDB/server/commit/a4477d2)\
  2015-04-29 14:14:45 +0300
  * Fix failing test cases for [MDEV-7912](https://jira.mariadb.org/browse/MDEV-7912) patch
* [Revision #f632b51](https://github.com/MariaDB/server/commit/f632b51)\
  2015-04-28 21:27:43 +0200
  * [MDEV-7987](https://jira.mariadb.org/browse/MDEV-7987) Fatal error: Please read "Security" section of the manual to find out how to run mysqld as root!
* [Revision #6f17e23](https://github.com/MariaDB/server/commit/6f17e23)\
  2015-04-28 21:24:32 +0200
  * post-merge fixes
* [Revision #9088f26](https://github.com/MariaDB/server/commit/9088f26)\
  2015-04-29 11:29:25 +0200
  * [MDEV-7802](https://jira.mariadb.org/browse/MDEV-7802): group commit status variable addition
* [Revision #fbab068](https://github.com/MariaDB/server/commit/fbab068)\
  2015-04-28 13:57:21 +0200
  * post-merge changes, fixes, and tests
* [Revision #40e9560](https://github.com/MariaDB/server/commit/40e9560)\
  2015-04-28 13:42:58 +0200
  * percona-server-5.5.42-37.1.tar.gz
* [Revision #a5fa434](https://github.com/MariaDB/server/commit/a5fa434)\
  2015-04-28 15:31:49 +0500
  * [MDEV-7779](https://jira.mariadb.org/browse/MDEV-7779) View definition changes upon creation. Fixed by using POINT instead of ST\_POINT in the item. Later need to fix that with proper ST\_POINT implementation
* [Revision #4c174fc](https://github.com/MariaDB/server/commit/4c174fc)\
  2015-04-28 15:28:29 +0300
  * [MDEV-8020](https://jira.mariadb.org/browse/MDEV-8020): innodb.innodb-[MDEV-7055](https://jira.mariadb.org/browse/MDEV-7055) produces valgrind warnings in buildbot
* [Revision #ac2b92c](https://github.com/MariaDB/server/commit/ac2b92c)\
  2015-04-28 15:09:04 +0300
  * [MDEV-7912](https://jira.mariadb.org/browse/MDEV-7912) multitable delete with wrongly set sort\_buffer\_size crashes in merge\_buffers
* [Revision #c8141f5](https://github.com/MariaDB/server/commit/c8141f5)\
  2015-04-28 14:06:07 +0400
  * [MDEV-7950](https://jira.mariadb.org/browse/MDEV-7950) Item\_func::type() takes 0.26% in OLTP RO
* [Revision #ed701c6](https://github.com/MariaDB/server/commit/ed701c6)\
  2015-04-28 11:56:54 +0200
  * [MDEV-7864](https://jira.mariadb.org/browse/MDEV-7864): Slave SQL: stopping on non-last RBR event with annotations results in SEGV (signal 11)
* [Revision #fd39c56](https://github.com/MariaDB/server/commit/fd39c56)\
  2015-04-27 23:37:51 +0200
  * move to storage/xtradb/
* [Revision #245cc73](https://github.com/MariaDB/server/commit/245cc73)\
  2015-04-27 12:47:39 +0200
  * [MDEV-7434](https://jira.mariadb.org/browse/MDEV-7434) XtraDB does not build on Solaris
* [Revision #e26b207](https://github.com/MariaDB/server/commit/e26b207)\
  2015-04-26 16:27:41 +0200
  * [MDEV-7938](https://jira.mariadb.org/browse/MDEV-7938) MariaDB Crashes Suddenly while writing binlogs
* [Revision #053143e](https://github.com/MariaDB/server/commit/053143e)\
  2015-04-25 21:56:46 +0200
  * [MDEV-7883](https://jira.mariadb.org/browse/MDEV-7883) Segmentation failure when running mysqladmin -u root -p
* [Revision #18215dd](https://github.com/MariaDB/server/commit/18215dd)\
  2015-04-25 17:22:46 +0200
  * [MDEV-7859](https://jira.mariadb.org/browse/MDEV-7859) SSL hostname verification fails for long subject names
* [Revision #9fd65db](https://github.com/MariaDB/server/commit/9fd65db)\
  2015-04-25 00:19:20 +0200
  * [MDEV-7585](https://jira.mariadb.org/browse/MDEV-7585) Assertion \`thd->is\_error() || kill\_errno || thd->killed == ABORT\_QUERY' failed in ha\_rows filesort
* [Revision #8e78160](https://github.com/MariaDB/server/commit/8e78160)\
  2015-04-24 21:41:00 +0200
  * [MDEV-6870](https://jira.mariadb.org/browse/MDEV-6870) Not possible to use FIFO file as a general\_log file
* [Revision #c05d431](https://github.com/MariaDB/server/commit/c05d431)\
  2015-04-24 21:03:43 +0200
  * bug: crash when sync() or close() of a log file fails on shutdown
* [Revision #8f499c3](https://github.com/MariaDB/server/commit/8f499c3)\
  2015-04-24 21:02:37 +0200
  * bug: debug assert crash when seek on log file fails
* [Revision #5fd0088](https://github.com/MariaDB/server/commit/5fd0088)\
  2015-04-27 15:31:12 +0200
  * [MDEV-8058](https://jira.mariadb.org/browse/MDEV-8058): funcs\_1.innodb\_views and funcs\_1.memory\_views fail
* [Revision #574227c](https://github.com/MariaDB/server/commit/574227c)\
  2015-04-27 21:15:23 +1000
  * /run/shm is the general replacement for /dev/shm in newer distros
* [Revision #3d801e6](https://github.com/MariaDB/server/commit/3d801e6)\
  2015-04-27 21:08:52 +1000
  * c99 style for assigning structure members
* [Revision #f832021](https://github.com/MariaDB/server/commit/f832021)\
  2015-04-23 08:26:57 +0200
  * [MDEV-7126](https://jira.mariadb.org/browse/MDEV-7126) replication slave - deadlock in terminate\_slave\_thread with stop slave and show variables of replication filters and show global status
* [Revision #4681699](https://github.com/MariaDB/server/commit/4681699)\
  2015-04-26 01:46:55 +0400
  * Moving members' initialization from LEX::init\_last\_field to constructor Create\_field::Create\_field().
* [Revision #4d606cb](https://github.com/MariaDB/server/commit/4d606cb)\
  2015-04-24 23:17:16 +1000
  * c99 style for assigning structure members
* [Revision #ecb009b](https://github.com/MariaDB/server/commit/ecb009b)\
  2015-04-25 00:54:00 +0400
  * Adding Type\_std\_attributes to reduce some duplicate code. TODO: move some methods from Item to Type\_std\_attributes.
* [Revision #060ec5b](https://github.com/MariaDB/server/commit/060ec5b)\
  2015-04-24 12:38:59 +0200
  * [MDEV-7130](https://jira.mariadb.org/browse/MDEV-7130): MASTER\_POS\_WAIT(log\_name,log\_pos,timeout,"connection\_name") hangs, does not respect the timeout
* [Revision #04fb09d](https://github.com/MariaDB/server/commit/04fb09d)\
  2015-04-24 12:59:21 +0400
  * Deriving Item\_row from Item\_args and sharing more code between Item\_func, Item\_sum, Item\_row.
* [Revision #44d1e85](https://github.com/MariaDB/server/commit/44d1e85)\
  2015-04-24 11:00:34 +0400
  * [MDEV-7649](https://jira.mariadb.org/browse/MDEV-7649) wrong result when comparing utf8 column with an invalid literal
* [Revision #f9b2704](https://github.com/MariaDB/server/commit/f9b2704)\
  2015-04-23 23:06:14 +0300
  * Testcase for: [MDEV-7893](https://jira.mariadb.org/browse/MDEV-7893) table\_elimination works wrong ...
* [Revision #2010971](https://github.com/MariaDB/server/commit/2010971)\
  2015-04-14 23:18:54 +0200
  * [MDEV-6892](https://jira.mariadb.org/browse/MDEV-6892): WHERE does not apply
* [Revision #b616991](https://github.com/MariaDB/server/commit/b616991)\
  2015-04-23 14:09:15 +0200
  * [MDEV-8031](https://jira.mariadb.org/browse/MDEV-8031): Parallel replication stops on "connection killed" error (probably incorrectly handled deadlock kill)
* [Revision #8cbaafd](https://github.com/MariaDB/server/commit/8cbaafd)\
  2015-04-22 10:14:11 +0200
  * [MDEV-8018](https://jira.mariadb.org/browse/MDEV-8018): main.multi\_update fails with --ps-protocol
* [Revision #fc1f301](https://github.com/MariaDB/server/commit/fc1f301)\
  2015-04-22 12:40:23 +0400
  * [MDEV-8024](https://jira.mariadb.org/browse/MDEV-8024) Remove excessive update\_used\_tables() calls
* [Revision #e428c80](https://github.com/MariaDB/server/commit/e428c80)\
  2015-04-21 15:41:01 +0300
  * [MDEV-7911](https://jira.mariadb.org/browse/MDEV-7911): crash in Item\_cond::eval\_not\_null\_tables
* [Revision #4760528](https://github.com/MariaDB/server/commit/4760528)\
  2015-04-21 10:16:14 +0200
  * [MDEV-8029](https://jira.mariadb.org/browse/MDEV-8029): test failure in rpl.rpl\_parallel\_temptable
* [Revision #6876a7d](https://github.com/MariaDB/server/commit/6876a7d)\
  2015-04-20 15:37:45 +0200
  * Bump VERSION following 10.1.4 release
* [Revision #d4e3aa4](https://github.com/MariaDB/server/commit/d4e3aa4)\
  2015-04-20 14:23:55 +0200
  * After-merge fixes: .result file update
* [Revision #519ad0f](https://github.com/MariaDB/server/commit/519ad0f)\
  2015-04-20 12:59:46 +0200
  * [MDEV-8016](https://jira.mariadb.org/browse/MDEV-8016): Replication aborts on DROP /\*!40005 TEMPORARY \*/ TABLE IF EXISTS
* [Revision #0759568](https://github.com/MariaDB/server/commit/0759568)\
  2015-04-20 18:36:19 +1000
  * test case for install plugin on boostrap
* [Revision #f1f8adf](https://github.com/MariaDB/server/commit/f1f8adf)\
  2015-04-20 05:02:10 +0200
  * tokuftdump: Install to ${INSTALL\_BINDIR} instead of bin
* [Revision #87d5438](https://github.com/MariaDB/server/commit/87d5438)\
  2015-04-20 02:43:26 +0300
  * Increase the version number
* [Revision #4cfb7f9](https://github.com/MariaDB/server/commit/4cfb7f9)\
  2015-04-19 15:49:35 +0300
  * Increase the version number
* [Revision #eae8318](https://github.com/MariaDB/server/commit/eae8318)\
  2015-04-17 20:05:41 +0200\
  \*
  * Fix Catalog JSON table crash when no Jpath - Added JSON OBJECT specification for pretty != 2. - Fix NULL values not recognized for nullable JSON columns - Issue an error message when a JSON table is created without specifying LRECL if PRETTY != 2. - Make JSONColumns use a TDBJSON class. - Make JSON table using MAPFAM modified: filamap.h filamtxt.h ha\_connect.cc json.result tabjson.cpp tabjson.h table.cpp
* [Revision #18715be](https://github.com/MariaDB/server/commit/18715be)\
  2015-04-17 19:48:55 +0200
  * Post-merge fix: build error in innodb-enabled build.
* [Revision #22a7b4d](https://github.com/MariaDB/server/commit/22a7b4d)\
  2015-04-17 16:26:08 +0400
  * Removing duplicate code/declarations:
* [Revision #14d1578](https://github.com/MariaDB/server/commit/14d1578)\
  2015-04-17 12:45:55 +0200
  * [MDEV-7802](https://jira.mariadb.org/browse/MDEV-7802): Omit one test which could fail on very loaded host.
* [Revision #8125db1](https://github.com/MariaDB/server/commit/8125db1)\
  2015-04-17 12:36:31 +0400
  * Moving fix\_length\_and\_dec() from Item\_result\_field to Item\_func\_or\_sum, as the other decendants of Item\_result\_field (Item\_avg\_field, Item\_variance\_field, Item\_cache\_wrapper) don't need fix\_length\_and\_dec().
* [Revision #99898c6](https://github.com/MariaDB/server/commit/99898c6)\
  2015-04-17 09:52:44 +0400
  * Minor reorganization in Item hierarchy, to remove duplicate code.
* [Revision #3c4668c](https://github.com/MariaDB/server/commit/3c4668c)\
  2015-04-15 23:06:03 -0400
  * wsrep\_sst\_mysqldump : Fix server version and a syntax error
* [Revision #d051f6c](https://github.com/MariaDB/server/commit/d051f6c)\
  2015-04-15 11:12:12 -0400
  * [MDEV-6594](https://jira.mariadb.org/browse/MDEV-6594): Use separate domain\_id for Galera transactions
* [Revision #a1f3356](https://github.com/MariaDB/server/commit/a1f3356)\
  2015-04-15 10:21:46 -0400
  * Update galera package name/version for debian
* [Revision #eb47b22](https://github.com/MariaDB/server/commit/eb47b22)\
  2015-04-15 16:23:43 +0300
  * [MDEV-7820](https://jira.mariadb.org/browse/MDEV-7820) Server crashes in my\_strcasecmp\_utf8 on subquery in ORDER BY clause of GROUP\_CONCAT
* [Revision #59d847b](https://github.com/MariaDB/server/commit/59d847b)\
  2015-04-15 12:08:37 +0400
  * [MDEV-7814](https://jira.mariadb.org/browse/MDEV-7814) Assertion \`args\[0]->fixed' fails in Item\_func\_conv\_charset::Item\_func\_conv\_charset Removing a wrong assertion.
* [Revision #b9a7586](https://github.com/MariaDB/server/commit/b9a7586)\
  2015-03-05 16:34:13 +0100
  * [MDEV-7613](https://jira.mariadb.org/browse/MDEV-7613): [MariaDB 5.5.40](../../old-releases/release-notes-mariadb-5-5-series/mariadb-5540-release-notes.md) server crash on update table left join with a view
* [Revision #5d2b85a](https://github.com/MariaDB/server/commit/5d2b85a)\
  2015-04-14 13:03:11 +0200
  * [MDEV-7975](https://jira.mariadb.org/browse/MDEV-7975): sporadic failure in test case rpl.rpl\_gtid\_startpos
* [Revision #f6f253b](https://github.com/MariaDB/server/commit/f6f253b)\
  2015-04-14 04:02:45 -0700
  * Fix a typo, s/false/NULL/.
* [Revision #83ce352](https://github.com/MariaDB/server/commit/83ce352)\
  2015-04-14 13:26:55 +1000
  * quote table name in mysql\_check:is\_view. increment version too
* [Revision #4987080](https://github.com/MariaDB/server/commit/4987080)\
  2015-04-14 13:26:22 +1000
  * Don't run upgrade-views if not mysql or --upgrade-system-tables
* [Revision #97e0aea](https://github.com/MariaDB/server/commit/97e0aea)\
  2015-04-14 12:43:50 +1000
  * mysqlcheck fix-view-algorithm -> upgrade-views
* [Revision #808608c](https://github.com/MariaDB/server/commit/808608c)\
  2015-04-14 11:26:13 +1000
  * corrected mysql\_upgrade to always list output for every phase
* [Revision #c584058](https://github.com/MariaDB/server/commit/c584058)\
  2015-04-14 11:01:31 +1000
  * Update tests for mysql\_upgrade\_view
* [Revision #201c985](https://github.com/MariaDB/server/commit/201c985)\
  2015-04-13 22:36:49 +0400
  * [MDEV-7886](https://jira.mariadb.org/browse/MDEV-7886) CREATE VIEW IF NOT EXISTS produces a wrong warning
* [Revision #76c18f7](https://github.com/MariaDB/server/commit/76c18f7)\
  2015-04-13 23:25:23 +1000
  * sql\_print\_information corrected
* [Revision #622891c](https://github.com/MariaDB/server/commit/622891c)\
  2015-04-13 22:58:45 +1000
  * mariadb\_fix\_view to allow fixing of view->mariadb\_version
* [Revision #8a827d5](https://github.com/MariaDB/server/commit/8a827d5)\
  2015-04-13 22:39:37 +1000
  * avoid calling runctiosn in DBUG\_RETURN
* [Revision #ed34927](https://github.com/MariaDB/server/commit/ed34927)\
  2015-04-13 14:38:25 +0200
  * [MDEV-7936](https://jira.mariadb.org/browse/MDEV-7936): Assertion \`!table || table->in\_use == \_current\_thd()' failed on parallel replication in optimistic mode
* [Revision #29721d7](https://github.com/MariaDB/server/commit/29721d7)\
  2015-04-13 22:31:44 +1000
  * mariadb\_fix\_view need only check view->mariadb\_version
* [Revision #7229b19](https://github.com/MariaDB/server/commit/7229b19)\
  2015-04-13 22:28:12 +1000
  * remove include sql\_view.h from sql\_table.cc - unneeded
* [Revision #60d094a](https://github.com/MariaDB/server/commit/60d094a)\
  2015-04-13 09:52:56 +0200
  * [MDEV-7936](https://jira.mariadb.org/browse/MDEV-7936): Assertion \`!table || table->in\_use == \_current\_thd()' failed on parallel replication in optimistic mode
* [Revision #fc277cd](https://github.com/MariaDB/server/commit/fc277cd)\
  2015-04-13 22:17:57 +1000
  * Add --fix-tables option to mysql-check
* [Revision #c47fe0e](https://github.com/MariaDB/server/commit/c47fe0e)\
  2015-03-09 13:06:32 +0100
  * [MDEV-7668](https://jira.mariadb.org/browse/MDEV-7668): Intermediate master groups CREATE TEMPORARY with INSERT, causing parallel replication failure
* [Revision #28b1731](https://github.com/MariaDB/server/commit/28b1731)\
  2015-04-13 21:12:23 +1000
  * Allow REPAIR NO\_WRITE\_TO\_BINLOG as per serg's review
* [Revision #f91dafc](https://github.com/MariaDB/server/commit/f91dafc)\
  2015-04-13 20:52:19 +1000
  * correct phase numbering in test results
* [Revision #eaa3da8](https://github.com/MariaDB/server/commit/eaa3da8)\
  2015-04-13 20:41:49 +1000
  * Add mysql-test/std\_data/mysql\_upgrade/\* for [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916)
* [Revision #8a01a0a](https://github.com/MariaDB/server/commit/8a01a0a)\
  2015-04-13 11:26:49 +0400
  * [MDEV-7920](https://jira.mariadb.org/browse/MDEV-7920) main.group\_min\_max fails in buildbot with valgrind
* [Revision #4409e04](https://github.com/MariaDB/server/commit/4409e04)\
  2015-04-12 21:40:07 +1000
  * correct server side error messages
* [Revision #9b067a3](https://github.com/MariaDB/server/commit/9b067a3)\
  2015-04-12 21:05:01 +1000
  * Corrections to mysqlcheck
* [Revision #96e277a](https://github.com/MariaDB/server/commit/96e277a)\
  2015-04-12 20:42:13 +1000
  * mysql\_upgrade to pass binlog option to mysqlcheck
* [Revision #c8dbef2](https://github.com/MariaDB/server/commit/c8dbef2)\
  2015-04-12 20:41:28 +1000
  * [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916) REPAIR VIEW / mysql migration
* [Revision #e5191dd](https://github.com/MariaDB/server/commit/e5191dd)\
  2015-04-12 17:26:50 +1000
  * mysql-upgrade -> fix-view-algorithm as mysqlcheck option
* [Revision #25872e2](https://github.com/MariaDB/server/commit/25872e2)\
  2015-04-12 17:21:02 +1000
  * Correct phase count on mysql\_upgrade
* [Revision #ebd3c6c](https://github.com/MariaDB/server/commit/ebd3c6c)\
  2015-04-12 17:05:02 +1000
  * Remove mysql-upgrade / skip-mysql-upgrade options from mysql-upgrade.c
* [Revision #87f5bae](https://github.com/MariaDB/server/commit/87f5bae)\
  2015-04-12 16:50:16 +1000
  * Get my\_getop to parse opt\_mysql\_upgrade in mysqlcheck
* [Revision #70960e7](https://github.com/MariaDB/server/commit/70960e7)\
  2015-04-12 15:56:21 +1000
  * [MDEV-6916](https://jira.mariadb.org/browse/MDEV-6916): Upgrade from MySQL to MariaDB breaks already created views
* [Revision #85660d7](https://github.com/MariaDB/server/commit/85660d7)\
  2015-04-11 18:13:08 +1000
  * [MDEV-7977](https://jira.mariadb.org/browse/MDEV-7977) MYSQL\_BIN\_LOG::write\_incident failing to release LOCK\_log
* [Revision #e9c10f9](https://github.com/MariaDB/server/commit/e9c10f9)\
  2015-04-06 17:38:51 +0300
  * [MDEV-7908](https://jira.mariadb.org/browse/MDEV-7908): assertion in innobase\_release\_savepoint
* [Revision #05b30fb](https://github.com/MariaDB/server/commit/05b30fb)\
  2015-04-04 19:29:34 +0200
  * Fix [MDEV-7890](https://jira.mariadb.org/browse/MDEV-7890)
* [Revision #0695fdd](https://github.com/MariaDB/server/commit/0695fdd)\
  2015-04-03 01:34:30 +1100
  * [MDEV-7802](https://jira.mariadb.org/browse/MDEV-7802)-binlog\_groupcommit\_stats
* [Revision #836740c](https://github.com/MariaDB/server/commit/836740c)\
  2015-04-02 11:36:53 +0200
  * Correct a typo that made multiple 1 tables to return 0 lines on Linux
* [Revision #1d5220d](https://github.com/MariaDB/server/commit/1d5220d)\
  2015-04-01 22:47:36 +1100
  * binlog\_group\_commit\_\* status variables update
* [Revision #dd7026a](https://github.com/MariaDB/server/commit/dd7026a)\
  2015-04-01 21:51:55 +1100
  * All updates to binlog\_status\_group\_commit\_reason\* are under LOCK\_prepare\_ordered
* [Revision #cc84ac3](https://github.com/MariaDB/server/commit/cc84ac3)\
  2015-03-31 13:10:43 +0500
  * [MDEV-7596](https://jira.mariadb.org/browse/MDEV-7596) audit plugin - record full query / document line length / make buffer configurable. The serve\_audit\_query\_log\_limit variable implemented. Also QUERY\_DCL filter added.
* [Revision #b53bcd4](https://github.com/MariaDB/server/commit/b53bcd4)\
  2015-03-30 18:53:10 +0300
  * [MDEV-7367](https://jira.mariadb.org/browse/MDEV-7367): Updating a virtual column corrupts table which crashes server
* [Revision #0563f49](https://github.com/MariaDB/server/commit/0563f49)\
  2015-03-17 16:03:05 +0200
  * [MDEV-7754](https://jira.mariadb.org/browse/MDEV-7754): innodb assert "array->n\_elems < array->max\_elems" on a huge blob update
* [Revision #8721d20](https://github.com/MariaDB/server/commit/8721d20)\
  2015-03-30 19:03:57 +0200\
  \*
  * Fix [MDEV-7879](https://jira.mariadb.org/browse/MDEV-7879) by adding a test in all SetValue\_pval function to return when valp == this.
* [Revision #995f622](https://github.com/MariaDB/server/commit/995f622)\
  2015-03-30 00:49:16 +0300
  * [MDEV-7858](https://jira.mariadb.org/browse/MDEV-7858): main.subselect\_sj2\_jcl6 fails in buildbot
* [Revision #daa8b6b](https://github.com/MariaDB/server/commit/daa8b6b)\
  2015-03-28 20:18:46 +0100
  * D:\Ber\Develop\git3.msg
* [Revision #323a7e9](https://github.com/MariaDB/server/commit/323a7e9)\
  2015-03-25 19:44:31 +0300
  * Backport from 10.1 to 10.0: Merge pull request #33 from k0da/[MDEV-7839](https://jira.mariadb.org/browse/MDEV-7839)
* [Revision #86f46a3d](https://github.com/MariaDB/server/commit/86f46a3d)\
  2015-03-23 09:49:32 +0200
  * [MDEV-7301](https://jira.mariadb.org/browse/MDEV-7301): Unknown column quoted with backticks in HAVING clause when using function.
* [Revision #9cace99](https://github.com/MariaDB/server/commit/9cace99)\
  2015-03-22 11:34:29 +0100\
  \*
  * Fix a bug that caused a crash when doing delete on a json table with wrong syntax file
* [Revision #9253064](https://github.com/MariaDB/server/commit/9253064)\
  2015-03-10 12:34:17 +0200
  * [MDEV-7682](https://jira.mariadb.org/browse/MDEV-7682) Incorrect use of SPATIAL KEY for query plan
* [Revision #5e20df2](https://github.com/MariaDB/server/commit/5e20df2)\
  2015-03-19 19:46:08 +0400
  * [MDEV-7641](https://jira.mariadb.org/browse/MDEV-7641) Server crash on set global server\_audit\_incl\_users=null.
* [Revision #41c337a](https://github.com/MariaDB/server/commit/41c337a)\
  2015-03-19 21:47:51 +1100
  * add group\_commit\_reason\_immediate to binlog\_commit\_wait test
* [Revision #f3eb1d0](https://github.com/MariaDB/server/commit/f3eb1d0)\
  2015-03-19 19:21:22 +1100
  * rpl\_parallel\_multilevel2 can be 1 or 3 binlog groups
* [Revision #54287ad](https://github.com/MariaDB/server/commit/54287ad)\
  2015-03-19 15:26:58 +1100
  * [MDEV-7802](https://jira.mariadb.org/browse/MDEV-7802) Add status binlog\_group\_commit\_reason\_\*
* [Revision #1020d56](https://github.com/MariaDB/server/commit/1020d56)\
  2015-03-18 15:17:17 +0200
  * Better and more correct comment.
* [Revision #2bb4280](https://github.com/MariaDB/server/commit/2bb4280)\
  2015-03-18 13:30:14 +0100
  * This commit includes changes done in a previous (deleted) branch plus new ones.
* [Revision #2bdbfd3](https://github.com/MariaDB/server/commit/2bdbfd3)\
  2015-03-18 12:18:39 +0200
  * Fix assertion failure seen on Buildbot win32-debug
* [Revision #c14d9c2](https://github.com/MariaDB/server/commit/c14d9c2)\
  2015-03-18 06:25:10 +0200
  * Make sure that sync level vector is emptied.
* [Revision #99a2c06](https://github.com/MariaDB/server/commit/99a2c06)\
  2015-03-17 20:35:05 +0200
  * [MDEV-7754](https://jira.mariadb.org/browse/MDEV-7754): innodb assert "array->n\_elems < array->max\_elems" on a huge blob update
* [Revision #c020d36](https://github.com/MariaDB/server/commit/c020d36)\
  2015-03-17 13:26:33 +0300
  * [MDEV-7474](https://jira.mariadb.org/browse/MDEV-7474): Semi-Join's DuplicateWeedout strategy skipped ...
* [Revision #3d48501](https://github.com/MariaDB/server/commit/3d48501)\
  2015-03-17 10:36:38 +0100
  * Fix embarrassing bug in test case that caused sporadic test failures.
* [Revision #57aacce](https://github.com/MariaDB/server/commit/57aacce)\
  2015-03-16 17:37:00 +0100\
  \*
  * Adding files to ignore from C C++ and Visual Studio - Making result files to be ended by LF to avoid test failures
* [Revision #2e82a82](https://github.com/MariaDB/server/commit/2e82a82)\
  2015-03-16 10:54:47 +0100
  * [MDEV-7785](https://jira.mariadb.org/browse/MDEV-7785): errorneous -> erroneous spelling mistake
* [Revision #fd97739](https://github.com/MariaDB/server/commit/fd97739)\
  2015-03-15 14:50:22 +1100
  * Allow {un,}install plugins during bootstrap/skip-grant-tables
* [Revision #184f718](https://github.com/MariaDB/server/commit/184f718)\
  2015-03-13 10:46:00 +0100
  * [MDEV-7249](https://jira.mariadb.org/browse/MDEV-7249): Performance problem in parallel replication with multi-level slaves
* [Revision #bc902a2](https://github.com/MariaDB/server/commit/bc902a2)\
  2015-03-13 16:12:54 +0400
  * [MDEV-7387](https://jira.mariadb.org/browse/MDEV-7387) \[PATCH] Alter table xxx CHARACTER SET utf8, CONVERT TO CHARACTER SET latin1 should fail A contribution from Daniel Black, with minor additional enhancements.
* [Revision #5a3bf84](https://github.com/MariaDB/server/commit/5a3bf84)\
  2015-03-12 18:53:31 +0200
  * [MDEV-7692](https://jira.mariadb.org/browse/MDEV-7692) MariaDB - mysql-test - SUITE:percona - percona.innodb\_sys\_index 'xtradb' fails - @@version\_comment
* [Revision #702fdc5](https://github.com/MariaDB/server/commit/702fdc5)\
  2015-03-12 18:37:32 +0200
  * [MDEV-7714](https://jira.mariadb.org/browse/MDEV-7714): Make possible to get innodb internal primary key for wrapper type storage engine.
* [Revision #ed04c40](https://github.com/MariaDB/server/commit/ed04c40)\
  2015-03-11 09:18:16 +0100
  * [MDEV-5289](https://jira.mariadb.org/browse/MDEV-5289): master server starts slave parallel threads
* [Revision #a7fd11b](https://github.com/MariaDB/server/commit/a7fd11b)\
  2015-03-09 18:21:48 +0200
  * [MDEV-7685](https://jira.mariadb.org/browse/MDEV-7685): MariaDB - server crashes when inserting more rows than available space on disk
* [Revision #ec16d1b](https://github.com/MariaDB/server/commit/ec16d1b)\
  2015-03-09 02:07:47 +0200
  * [MDEV-7107](https://jira.mariadb.org/browse/MDEV-7107) Sporadic test failure in multi\_source.multisource
* [Revision #34f37aa](https://github.com/MariaDB/server/commit/34f37aa)\
  2015-03-02 19:18:10 +0200
  * [MDEV-7643](https://jira.mariadb.org/browse/MDEV-7643) MTR creates nested links when tests are run with --mem
* [Revision #96784eb](https://github.com/MariaDB/server/commit/96784eb)\
  2015-03-09 13:06:32 +0100
  * [MDEV-7668](https://jira.mariadb.org/browse/MDEV-7668): Intermediate master groups CREATE TEMPORARY with INSERT, causing parallel replication failure
* [Revision #040027c](https://github.com/MariaDB/server/commit/040027c)\
  2015-03-09 09:47:25 +0200
  * [MDEV-7627](https://jira.mariadb.org/browse/MDEV-7627) :Some symbols in table name can cause to Error Code: 1050 when created FK
* [Revision #6fc0a8a](https://github.com/MariaDB/server/commit/6fc0a8a)\
  2015-03-08 23:12:19 +0200
  * [MDEV-7187](https://jira.mariadb.org/browse/MDEV-7187) perfschema.aggregate fails sporadically in buildbot
* [Revision #eb2f763](https://github.com/MariaDB/server/commit/eb2f763)\
  2015-03-03 12:39:42 +0100
  * Add #include in dict0mem.h and change iterator to const\_iterator in dic0mem.cc
* [Revision #a235504](https://github.com/MariaDB/server/commit/a235504)\
  2015-02-28 22:43:18 +1030
  * Ensure VERBOSE\_DEBUG is off by default
* [Revision #2b9aba3](https://github.com/MariaDB/server/commit/2b9aba3)\
  2015-02-28 22:43:04 +1030
  * Updated © message to 2015, and changelog
* [Revision #c65f323](https://github.com/MariaDB/server/commit/c65f323)\
  2014-11-05 20:11:32 +1030
  * Fixed more cases for [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282)
* [Revision #e32dafe](https://github.com/MariaDB/server/commit/e32dafe)\
  2014-10-30 22:47:48 +1030
  * Hopefully finally fixes [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282), [MDEV-5748](https://jira.mariadb.org/browse/MDEV-5748) and [MDEV-6345](https://jira.mariadb.org/browse/MDEV-6345)
* [Revision #f8e0f1a](https://github.com/MariaDB/server/commit/f8e0f1a)\
  2014-10-28 21:50:34 +1030
  * Minor code cleanup: validation of options to member function.
* [Revision #fbcabb2](https://github.com/MariaDB/server/commit/fbcabb2)\
  2014-10-28 21:45:47 +1030
  * Fixed minor spelling mistake.
* [Revision #6ff6bf8](https://github.com/MariaDB/server/commit/6ff6bf8)\
  2014-10-25 21:36:55 +1030
  * Added regression test for [MDEV-6345](https://jira.mariadb.org/browse/MDEV-6345)
* [Revision #a657abd](https://github.com/MariaDB/server/commit/a657abd)\
  2014-10-25 21:36:29 +1030
  * Added extra debug to support [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282)
* [Revision #e72abc5](https://github.com/MariaDB/server/commit/e72abc5)\
  2014-10-25 21:23:34 +1030
  * Minor fix: make sure alter table wont try to change our storage engine to something else.
* [Revision #79246eb](https://github.com/MariaDB/server/commit/79246eb)\
  2014-10-30 23:00:07 +1030
  * Partial code tidy: move plugin description to end with other items, and added status variable for debug.
* [Revision #13e30c0](https://github.com/MariaDB/server/commit/13e30c0)\
  2014-10-25 21:17:13 +1030
  * Removed dead code and support for dead (<10.0.5) versions of mariadb
* [Revision #abf1e25](https://github.com/MariaDB/server/commit/abf1e25)\
  2014-10-25 20:00:41 +1030
  * Partial whitespace cleanup.
* [Revision #8261413](https://github.com/MariaDB/server/commit/8261413)\
  2014-06-15 21:39:23 +0930
  * Added regression test for [MDEV-6282](https://jira.mariadb.org/browse/MDEV-6282)
* [Revision #1973c00](https://github.com/MariaDB/server/commit/1973c00)\
  2014-06-22 19:59:42 +0930
  * Update 2014 © message

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
