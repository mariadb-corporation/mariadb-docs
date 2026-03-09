# MariaDB 10.4.21 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download 10.4.21](https://downloads.mariadb.org/mariadb/10.4.21/)[Release Notes](../../old-releases/10.4/10.4.21.md)[Changelog](mariadb-10421-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.4.21/)

**Release date:** 6 Aug 2021

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.21.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.31](../changelogs-mariadb-10-3-series/mariadb-10331-changelog.md)
* Merge [Revision #4902b0fdc9](https://github.com/MariaDB/server/commit/4902b0fdc9) 2021-08-02 16:50:28 +0200 - Merge branch '10.3' into 10.4
* [Revision #89cc633853](https://github.com/MariaDB/server/commit/89cc633853)\
  2021-08-02 16:39:08 +0300
  * [MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564) fixup: Remove unused function fts\_check\_corrupt()
* Merge [Revision #7841a7eb09](https://github.com/MariaDB/server/commit/7841a7eb09) 2021-07-31 22:59:58 +0200 - Merge branch '10.3' into 10.4
* [Revision #77992bc710](https://github.com/MariaDB/server/commit/77992bc710)\
  2021-07-28 15:43:12 +0200
  * [MDEV-26092](https://jira.mariadb.org/browse/MDEV-26092) Remove things we do not use in wolfssl
* [Revision #093227c05e](https://github.com/MariaDB/server/commit/093227c05e)\
  2021-07-26 09:37:38 +0200
  * [MDEV-25410](https://jira.mariadb.org/browse/MDEV-25410) Assertion \`state\_ == s\_exec' failed - mysqld got signal 6
* [Revision #386ac12a48](https://github.com/MariaDB/server/commit/386ac12a48)\
  2021-07-26 09:14:37 +0200
  * [MDEV-25740](https://jira.mariadb.org/browse/MDEV-25740) Assertion \`!wsrep\_has\_changes(thd) || (thd->lex->sql\_command == SQLCOM\_CREATE\_TABLE && !thd->is\_current\_stmt\_binlog\_format\_row())' failed in void wsrep\_commit\_empty(THD\*, bool)
* [Revision #eb26e20df5](https://github.com/MariaDB/server/commit/eb26e20df5)\
  2021-07-26 08:46:36 +0200
  * [MDEV-22421](https://jira.mariadb.org/browse/MDEV-22421) Galera assertion !wsrep\_has\_changes(thd) || (thd->lex->sql\_command == SQLCOM\_CREATE\_TABLE && !thd->is\_current\_stmt\_binlog\_format\_row())
* [Revision #e7855119ba](https://github.com/MariaDB/server/commit/e7855119ba)\
  2021-07-24 00:16:31 +0300
  * [MDEV-26148](https://jira.mariadb.org/browse/MDEV-26148) SEGV or Assertion \`!page\_is\_comp(page) == !(index->table)->not\_redundant()'
* [Revision #2173f382ca](https://github.com/MariaDB/server/commit/2173f382ca)\
  2021-07-27 01:01:42 +0200
  * [MDEV-26236](https://jira.mariadb.org/browse/MDEV-26236) ssl\_8k\_key test fails on x86
* [Revision #217caf27e3](https://github.com/MariaDB/server/commit/217caf27e3)\
  2021-07-27 10:34:45 +0300
  * Update result files for Galera library 26.4.9
* [Revision #2b84e1c966](https://github.com/MariaDB/server/commit/2b84e1c966)\
  2021-07-20 12:45:00 -0300
  * [MDEV-23080](https://jira.mariadb.org/browse/MDEV-23080): desync and pause node on BACKUP STAGE BLOCK\_DDL
* [Revision #389f5cf76f](https://github.com/MariaDB/server/commit/389f5cf76f)\
  2021-06-29 20:12:00 +0200
  * disable spider/bugfix.wait\_timeout
* [Revision #8d3d802c54](https://github.com/MariaDB/server/commit/8d3d802c54)\
  2021-07-25 19:24:11 +0200
  * fix spider/bugfix.delete\_with\_float\_column\_mysql --ps
* [Revision #4533e6ef65](https://github.com/MariaDB/server/commit/4533e6ef65)\
  2021-07-14 18:03:53 +0200
  * [MDEV-18353](https://jira.mariadb.org/browse/MDEV-18353) Shutdown may miss to wait for connection thread
* [Revision #b34cafe9d9](https://github.com/MariaDB/server/commit/b34cafe9d9)\
  2021-07-20 13:00:31 +0200
  * cleanup: move thread\_count to THD\_count::value()
* [Revision #1fb71c7831](https://github.com/MariaDB/server/commit/1fb71c7831)\
  2021-07-23 16:33:14 +0300
  * [MDEV-19272](https://jira.mariadb.org/browse/MDEV-19272): Assertion unireg\_check..Field::NEXT\_NUMBER failed
* [Revision #0604592a85](https://github.com/MariaDB/server/commit/0604592a85)\
  2021-07-23 10:14:18 +0200
  * fix ssl\_cipher test
* [Revision #6cd3588f0e](https://github.com/MariaDB/server/commit/6cd3588f0e)\
  2021-07-22 12:40:15 +0100
  * Improve documentation of json parser functions
* [Revision #aafb888657](https://github.com/MariaDB/server/commit/aafb888657)\
  2021-07-13 07:53:19 +0000
  * [MDEV-26013](https://jira.mariadb.org/browse/MDEV-26013) distinct not work properly in some cases for spider tables
* [Revision #7ffa801cf2](https://github.com/MariaDB/server/commit/7ffa801cf2)\
  2021-07-21 21:26:25 +0200
  * [MDEV-22221](https://jira.mariadb.org/browse/MDEV-22221) Compile WolfSSL with TLSv1.3 support
* [Revision #6a3e0009a6](https://github.com/MariaDB/server/commit/6a3e0009a6)\
  2021-07-21 09:16:28 +0200
  * WolfSSL 4.8.0
* [Revision #3e5a11e488](https://github.com/MariaDB/server/commit/3e5a11e488)\
  2021-07-20 09:29:45 +0300
  * [MDEV-25236](https://jira.mariadb.org/browse/MDEV-25236) fixup: instant\_alter\_debug,dynamic result
* [Revision #7af5d96f00](https://github.com/MariaDB/server/commit/7af5d96f00)\
  2021-07-16 19:28:29 +0200
  * [MDEV-22221](https://jira.mariadb.org/browse/MDEV-22221): MariaDB with WolfSSL doesn't support AES-GCM cipher for SSL
* [Revision #bd3ac6758a](https://github.com/MariaDB/server/commit/bd3ac6758a)\
  2021-07-10 12:42:53 +0200
  * fix perfschema.sizing\_\* tests to run
* [Revision #e3814a74ee](https://github.com/MariaDB/server/commit/e3814a74ee)\
  2021-07-14 10:17:54 +0000
  * [MDEV-26139](https://jira.mariadb.org/browse/MDEV-26139) Spider crashes with segmentation fault (signal 11) on CREATE TABLE when COMMENT does not contain embedded double quotes
* [Revision #78735dcaf7](https://github.com/MariaDB/server/commit/78735dcaf7)\
  2021-07-08 17:47:17 -0700
  * [MDEV-26108](https://jira.mariadb.org/browse/MDEV-26108) Crash with query referencing twice CTE that uses embedded recursive CTE
* [Revision #e56fe39310](https://github.com/MariaDB/server/commit/e56fe39310)\
  2021-07-06 03:00:27 +0200
  * [MDEV-25978](https://jira.mariadb.org/browse/MDEV-25978): minor post-merge fix for .result file
* [Revision #a635588b56](https://github.com/MariaDB/server/commit/a635588b56)\
  2021-07-02 16:11:01 +0300
  * [MDEV-25236](https://jira.mariadb.org/browse/MDEV-25236) Online log apply fails for ROW\_FORMAT=REDUNDANT tables
* Merge [Revision #372ea88264](https://github.com/MariaDB/server/commit/372ea88264) 2021-07-02 14:55:52 +0300 - Merge 10.3 into 10.4
* Merge [Revision #c294443b41](https://github.com/MariaDB/server/commit/c294443b41) 2021-07-02 11:48:51 +0300 - Merge 10.3 into 10.4
* [Revision #fa8eb4de55](https://github.com/MariaDB/server/commit/fa8eb4de55)\
  2021-07-02 14:54:59 +1000
  * mtr: plugin.multiauth aix fix
* Merge [Revision #95e9f3c186](https://github.com/MariaDB/server/commit/95e9f3c186) 2021-07-02 17:17:33 +1000 - Merge branch 10.3 into 10.4
* [Revision #6a3a046013](https://github.com/MariaDB/server/commit/6a3a046013)\
  2021-07-02 13:00:34 +1000
  * mtr: aix - no pool of threads
* [Revision #2301093f8f](https://github.com/MariaDB/server/commit/2301093f8f)\
  2021-06-11 17:13:19 +1000
  * [MDEV-25894](https://jira.mariadb.org/browse/MDEV-25894): support AIX as a platform in mtr
* [Revision #c7443a0911](https://github.com/MariaDB/server/commit/c7443a0911)\
  2021-07-01 01:08:28 +0300
  * [MDEV-25969](https://jira.mariadb.org/browse/MDEV-25969): Condition pushdown into derived table doesn't work if select list uses SP
* Merge [Revision #eebe2090c8](https://github.com/MariaDB/server/commit/eebe2090c8) 2021-06-30 18:13:08 +0300 - Merge 10.3 -> 10.4
* [Revision #a1e2ca057d](https://github.com/MariaDB/server/commit/a1e2ca057d)\
  2021-06-30 10:38:44 +0300
  * [MDEV-26030](https://jira.mariadb.org/browse/MDEV-26030) : Warning: Memory not freed: 32 on setting wsrep\_sst\_auth
* [Revision #6431862022](https://github.com/MariaDB/server/commit/6431862022)\
  2021-06-29 12:44:42 +0200
  * [MDEV-25978](https://jira.mariadb.org/browse/MDEV-25978) post-merge: updated mtr result files
* [Revision #58700a426a](https://github.com/MariaDB/server/commit/58700a426a)\
  2021-06-29 12:42:14 +0200
  * [MDEV-26019](https://jira.mariadb.org/browse/MDEV-26019): Upgrading MariaDB breaks TLS mariadb-backup SST
* [Revision #1c03e7a667](https://github.com/MariaDB/server/commit/1c03e7a667)\
  2021-06-22 15:44:44 +0300
  * [MDEV-25978](https://jira.mariadb.org/browse/MDEV-25978) : rsync SST does not work with custom binlog name
* Merge [Revision #09b03ff31b](https://github.com/MariaDB/server/commit/09b03ff31b) 2021-06-23 08:05:27 +0300 - Merge 10.3 into 10.4
* [Revision #bf2680ea09](https://github.com/MariaDB/server/commit/bf2680ea09)\
  2021-06-22 22:42:42 -0400
  * bump the VERSION
* [Revision #7f24e37fbe](https://github.com/MariaDB/server/commit/7f24e37fbe)\
  2021-06-22 12:23:13 -0700
  * [MDEV-25679](https://jira.mariadb.org/browse/MDEV-25679) Wrong result selecting from simple view with LIMIT and ORDER BY
* Merge [Revision #ce868cd89e](https://github.com/MariaDB/server/commit/ce868cd89e) 2021-06-21 18:44:14 +0300 - Merge 10.3 into 10.4
* [Revision #baf0ef9a18](https://github.com/MariaDB/server/commit/baf0ef9a18)\
  2021-06-21 14:05:43 +0300
  * After-merge fix: Remove duplicated code
* Merge [Revision #d3e4fae797](https://github.com/MariaDB/server/commit/d3e4fae797) 2021-06-21 12:38:25 +0300 - Merge 10.3 into 10.4
* [Revision #690ae1de45](https://github.com/MariaDB/server/commit/690ae1de45)\
  2021-06-19 13:45:39 +0200
  * fix spider tests for --ps in 10.4
* [Revision #a4f485917e](https://github.com/MariaDB/server/commit/a4f485917e)\
  2021-06-19 13:45:14 +0200
  * spider tests aren't big in 10.4
* [Revision #8a2b4d531d](https://github.com/MariaDB/server/commit/8a2b4d531d)\
  2021-06-11 14:30:42 +1000
  * [MDEV-20162](https://jira.mariadb.org/browse/MDEV-20162): fix connect-abstract test case
* [Revision #e85df7feac](https://github.com/MariaDB/server/commit/e85df7feac)\
  2019-06-15 16:04:49 +0200
  * [MDEV-19702](https://jira.mariadb.org/browse/MDEV-19702) Refactor Bitmap to be based on ulonglong, not on uint32
* [Revision #0b9a59bbc4](https://github.com/MariaDB/server/commit/0b9a59bbc4)\
  2021-06-09 15:50:01 +0300
  * [MDEV-25884](https://jira.mariadb.org/browse/MDEV-25884) Tests use environment $USER variable without quotes
* [Revision #f13b80af39](https://github.com/MariaDB/server/commit/f13b80af39)\
  2021-06-09 13:17:58 +0200
  * [MDEV-23933](https://jira.mariadb.org/browse/MDEV-23933) main.failed\_auth\_unixsocket fails on arm
* [Revision #bafec28e43](https://github.com/MariaDB/server/commit/bafec28e43)\
  2021-05-06 19:47:11 +0200
  * rpm packaging: account for fedora > 31
* [Revision #7e9bc7bf4e](https://github.com/MariaDB/server/commit/7e9bc7bf4e)\
  2021-05-03 23:31:33 +0200
  * mdl\_dbug\_print\_locks(): make it useful in gdb too
* [Revision #b81803f065](https://github.com/MariaDB/server/commit/b81803f065)\
  2021-06-09 13:27:00 +0200
  * [MDEV-22221](https://jira.mariadb.org/browse/MDEV-22221): MariaDB with WolfSSL doesn't support AES-GCM cipher for SSL
* [Revision #dbe3161b6d](https://github.com/MariaDB/server/commit/dbe3161b6d)\
  2021-06-09 12:34:23 +0200
  * Remove WolfSSL workaround for old version. We're already on 4.4.6

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
