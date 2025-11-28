# MariaDB 11.6.1 Changelog

The most recent release of [MariaDB 11.6](../../old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116.md) is:[**MariaDB 11.6.2**](../../old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb/11.6.2/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.6.2)

[Download 11.6.1](https://downloads.mariadb.org/mariadb/11.6.1/)[Release Notes](../../old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes.md)[Changelog](mariadb-11-6-1-changelog.md)[Overview of 11.6](../../old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.6.1/)

**Release date:** 14 Aug 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-1-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Changes from [11.6.0](../../old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-0-release-notes.md) are also included in this changelog
* Includes all fixes from [MariaDB 11.5.2](../11.5/mariadb-11-5-2-changelog.md)
* [Revision #05fe3f1c18](https://github.com/MariaDB/server/commit/05fe3f1c18)\
  2024-08-10 21:27:58 +0200
  * Two problems with auth\_parsec.so
* [Revision #72d54ff9d4](https://github.com/MariaDB/server/commit/72d54ff9d4)\
  2024-08-10 20:16:59 +0200
  * only enable client parsec plugin if HAVE\_THREADS\_H
* [Revision #18cf72df56](https://github.com/MariaDB/server/commit/18cf72df56)\
  2024-08-10 19:39:21 +0200
  * disable the test that doesn't work in MSAN
* [Revision #7e3dfe3e75](https://github.com/MariaDB/server/commit/7e3dfe3e75)\
  2024-08-09 15:57:32 +0200
  * fix version
* [Revision #43d478d41d](https://github.com/MariaDB/server/commit/43d478d41d)\
  2024-08-09 14:48:33 +0200
  * fix parameters values of the calls
* [Revision #e580cf7ae0](https://github.com/MariaDB/server/commit/e580cf7ae0)\
  2024-05-21 22:11:04 +0200
  * [MDEV-32618](https://jira.mariadb.org/browse/MDEV-32618) new auth plugin
* [Revision #68e369e3a9](https://github.com/MariaDB/server/commit/68e369e3a9)\
  2024-05-24 21:44:52 +0200
  * Sys\_var\_plugin: use const for default plugin name
* [Revision #4a819f52e3](https://github.com/MariaDB/server/commit/4a819f52e3)\
  2024-05-31 15:35:33 +0200
  * sql\_acl: send client plugin name in the server handshake packet
* [Revision #8386a529cc](https://github.com/MariaDB/server/commit/8386a529cc)\
  2024-04-29 22:41:07 +0200
  * [MDEV-19949](https://jira.mariadb.org/browse/MDEV-19949) mariadb-backup option of '--password' or '-p' without specifying password in commandline
* Merge [Revision #ba15ea117c](https://github.com/MariaDB/server/commit/ba15ea117c) 2024-08-09 11:34:31 +0200 - Merge branch '11.6' into 11.6
* Merge [Revision #523ef2a12c](https://github.com/MariaDB/server/commit/523ef2a12c) 2024-08-05 14:45:45 +0200 - Merge 11.5 into 11.6
* [Revision #c175f4988a](https://github.com/MariaDB/server/commit/c175f4988a)\
  2024-08-05 11:16:12 +0200
  * Disable innodb bulk load, because of [MDEV-34703](https://jira.mariadb.org/browse/MDEV-34703)
* [Revision #a4effbf90f](https://github.com/MariaDB/server/commit/a4effbf90f)\
  2024-08-08 13:11:25 +0200
  * Fix of [MDEV-33856](https://jira.mariadb.org/browse/MDEV-33856), becaouse we have more then 64 fields
* [Revision #337307a943](https://github.com/MariaDB/server/commit/337307a943)\
  2024-08-07 20:16:15 +1000
  * spider\_string: use c\_ptr\_safe() instead of ptr() in error messages
* [Revision #ba0d8aeffa](https://github.com/MariaDB/server/commit/ba0d8aeffa)\
  2024-08-07 11:26:15 +0300
  * Fix rocksdb.unique\_check: do not have two threads waiting on the same name
* Merge [Revision #d6444022ca](https://github.com/MariaDB/server/commit/d6444022ca) 2024-08-06 14:45:24 +0200 - Merge branch 'bb-11.5-release' into bb-11.6-release
* [Revision #9e1923ca23](https://github.com/MariaDB/server/commit/9e1923ca23)\
  2024-02-20 19:10:18 +0000
  * Extend Unix socket authentication to support authentication\_string
* [Revision #25b5c63905](https://github.com/MariaDB/server/commit/25b5c63905)\
  2024-05-14 23:47:59 +0300
  * [MDEV-33856](https://jira.mariadb.org/browse/MDEV-33856): Alternative Replication Lag Representation via Received/Executed Master Binlog Event Timestamps
* [Revision #4dde925f54](https://github.com/MariaDB/server/commit/4dde925f54)\
  2024-06-27 00:18:39 +0000
  * Cleanup Whitespace in unittest/ directory
* [Revision #d83742622d](https://github.com/MariaDB/server/commit/d83742622d)\
  2024-05-27 09:04:34 +0300
  * [MDEV-33750](https://jira.mariadb.org/browse/MDEV-33750): Rename mysql to mariadb in Debian directory
* [Revision #75d354a23a](https://github.com/MariaDB/server/commit/75d354a23a)\
  2024-05-01 12:51:53 +1000
  * [MDEV-33988](https://jira.mariadb.org/browse/MDEV-33988) DELETE single table to support table aliases
* [Revision #0cd20e3aaf](https://github.com/MariaDB/server/commit/0cd20e3aaf)\
  2024-07-16 06:41:35 -0600
  * [MDEV-34571](https://jira.mariadb.org/browse/MDEV-34571): Fix funcs\_1.is\_columns\_is\_embedded
* [Revision #9e25d6f0cc](https://github.com/MariaDB/server/commit/9e25d6f0cc)\
  2024-06-03 12:23:53 +0200
  * [MDEV-33627](https://jira.mariadb.org/browse/MDEV-33627) : Implement option --dir in mariadb-import
* [Revision #04988d87aa](https://github.com/MariaDB/server/commit/04988d87aa)\
  2024-07-16 15:14:28 +0200
  * [MDEV-33627](https://jira.mariadb.org/browse/MDEV-33627) refactor threading in mariadb-import
* [Revision #c483c5ca56](https://github.com/MariaDB/server/commit/c483c5ca56)\
  2024-07-16 14:59:55 +0200
  * [MDEV-33627](https://jira.mariadb.org/browse/MDEV-33627) preparation - tpool fix
* [Revision #59167c567b](https://github.com/MariaDB/server/commit/59167c567b)\
  2024-05-13 13:19:45 +0200
  * [MDEV-33627](https://jira.mariadb.org/browse/MDEV-33627) preparation - compile mysqlimport as C++
* [Revision #ecc7961140](https://github.com/MariaDB/server/commit/ecc7961140)\
  2024-07-11 14:52:23 +0300
  * [MDEV-34571](https://jira.mariadb.org/browse/MDEV-34571) Add page accessed and pages read from disk to table\_stats
* [Revision #d1af7fde55](https://github.com/MariaDB/server/commit/d1af7fde55)\
  2024-06-20 15:34:16 +1000
  * [MDEV-19123](https://jira.mariadb.org/browse/MDEV-19123) Debian configuration - no explicit configuration for ut8mb4
* [Revision #36eba98817](https://github.com/MariaDB/server/commit/36eba98817)\
  2024-05-28 09:08:51 +0400
  * [MDEV-19123](https://jira.mariadb.org/browse/MDEV-19123) Change default charset from latin1 to utf8mb4
* Merge [Revision #a2a5ba14a8](https://github.com/MariaDB/server/commit/a2a5ba14a8) 2024-07-10 13:30:01 +0400 - Merge remote-tracking branch 'origin/11.5' into 11.6
* [Revision #186a1afe63](https://github.com/MariaDB/server/commit/186a1afe63)\
  2024-06-09 14:09:33 +0200
  * [MDEV-32537](https://jira.mariadb.org/browse/MDEV-32537) due to Linux, restrict thread name to 15 characters, also in PS.
* [Revision #5bd0516488](https://github.com/MariaDB/server/commit/5bd0516488)\
  2024-06-09 14:01:24 +0200
  * [MDEV-32537](https://jira.mariadb.org/browse/MDEV-32537) Name threads to improve debugging experience and diagnostics.
* [Revision #584fc85e21](https://github.com/MariaDB/server/commit/584fc85e21)\
  2024-06-09 14:00:32 +0200
  * [MDEV-32537](https://jira.mariadb.org/browse/MDEV-32537) Name threads to improve debugging experience and diagnostics.
* Merge [Revision #027f137741](https://github.com/MariaDB/server/commit/027f137741) 2024-07-08 14:15:04 +0400 - Merge remote-tracking branch 'origin/11.5' into 11.6
* [Revision #becc8372c7](https://github.com/MariaDB/server/commit/becc8372c7)\
  2024-06-19 14:47:30 -0700
  * Delete unused global variables from mysqld.h
* [Revision #7c5fdc9b6a](https://github.com/MariaDB/server/commit/7c5fdc9b6a)\
  2024-06-07 16:20:10 +0200
  * [MDEV-33748](https://jira.mariadb.org/browse/MDEV-33748) get rid of pthread\_(get\_/set\_)specific, use thread\_local
* [Revision #68fed7e785](https://github.com/MariaDB/server/commit/68fed7e785)\
  2024-06-20 10:08:12 +0100
  * Update pull request template for refactoring
* [Revision #29e9ade269](https://github.com/MariaDB/server/commit/29e9ade269)\
  2024-05-17 23:42:16 +0300
  * fix the use of strchrnul() which may be not available on some systems
* [Revision #2ba1a8b878](https://github.com/MariaDB/server/commit/2ba1a8b878)\
  2024-06-11 02:11:02 +0200
  * [MDEV-31809](https://jira.mariadb.org/browse/MDEV-31809) addendum: corrections for SST scripts and for test failures
* [Revision #a1e5a284fc](https://github.com/MariaDB/server/commit/a1e5a284fc)\
  2023-07-26 22:34:56 +0300
  * [MDEV-31809](https://jira.mariadb.org/browse/MDEV-31809) Automatic SST user account management
* [Revision #1aa1a7cf64](https://github.com/MariaDB/server/commit/1aa1a7cf64)\
  2023-07-24 22:59:56 +0300
  * [MDEV-31809](https://jira.mariadb.org/browse/MDEV-31809) Use MariaDB allocator where possible in wsrep\_utils.cc
* [Revision #d9f910bfe9](https://github.com/MariaDB/server/commit/d9f910bfe9)\
  2023-07-24 22:15:01 +0300
  * [MDEV-31809](https://jira.mariadb.org/browse/MDEV-31809) Make SST script interface read-write
* [Revision #203d337a55](https://github.com/MariaDB/server/commit/203d337a55)\
  2023-07-29 14:27:48 +0300
  * [MDEV-25321](https://jira.mariadb.org/browse/MDEV-25321) mariadb-backup ignores MYSQL\_PWD variable
* Merge [Revision #3d4bdf76d3](https://github.com/MariaDB/server/commit/3d4bdf76d3) 2024-05-31 17:22:37 +0200 - Merge 11.5 into 11.6
* [Revision #aeffec60f6](https://github.com/MariaDB/server/commit/aeffec60f6)\
  2023-08-09 02:18:36 +0200
  * [MDEV-19210](https://jira.mariadb.org/browse/MDEV-19210): do not run pre and post scripts as root
* [Revision #4c56c66372](https://github.com/MariaDB/server/commit/4c56c66372)\
  2023-11-23 08:56:55 +0100
  * [MDEV-19210](https://jira.mariadb.org/browse/MDEV-19210): drop support for instantiated services from galera\_new\_cluster
* [Revision #621926e90a](https://github.com/MariaDB/server/commit/621926e90a)\
  2019-01-29 10:03:42 +0100
  * [MDEV-19210](https://jira.mariadb.org/browse/MDEV-19210): update galera\_new\_cluster to use environment file
* [Revision #7936254012](https://github.com/MariaDB/server/commit/7936254012)\
  2019-01-28 00:26:23 +0100
  * [MDEV-19210](https://jira.mariadb.org/browse/MDEV-19210): use environment file in systemd units for \_WSREP\_START\_POSITION
* [Revision #26f01f8be5](https://github.com/MariaDB/server/commit/26f01f8be5)\
  2024-05-16 12:12:03 +0200
  * 11.6 branch

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
