# MariaDB 10.1.26 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.26)[Release Notes](../../old-releases/10.1/10.1.26.md)[Changelog](mariadb-10126-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 10 Aug 2017

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.26.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #535910ae5f](https://github.com/MariaDB/server/commit/535910ae5f)\
  2017-08-09 16:15:30 +0300
  * Updated list of unstable tests for 10.1.26 release
* [Revision #fa1f214cf8](https://github.com/MariaDB/server/commit/fa1f214cf8)\
  2017-08-08 19:47:34 +0200
  * [MDEV-12725](https://jira.mariadb.org/browse/MDEV-12725) select on federated table crashes server
* [Revision #5099d6de61](https://github.com/MariaDB/server/commit/5099d6de61)\
  2017-08-08 14:52:08 +0200
  * [MDEV-12863](https://jira.mariadb.org/browse/MDEV-12863) No table can be created after second encryption plugin attempted to load
* Merge [Revision #8e8d42ddf0](https://github.com/MariaDB/server/commit/8e8d42ddf0) 2017-08-08 10:18:43 +0200 - Merge branch '10.0' into 10.1
* [Revision #2395adfbfd](https://github.com/MariaDB/server/commit/2395adfbfd)\
  2017-08-06 16:03:10 +0200
  * ssl tests: update ciphers as in 10.2
* [Revision #b7381526ab](https://github.com/MariaDB/server/commit/b7381526ab)\
  2017-07-13 21:56:03 +0200
  * Always require OpenSSL 1.0 on Debian
* [Revision #1093c0f2dd](https://github.com/MariaDB/server/commit/1093c0f2dd)\
  2017-07-14 16:14:22 +0200
  * disallow invalid values for WITH\_SYSTEMD cmake variable.
* [Revision #e95d65d7d0](https://github.com/MariaDB/server/commit/e95d65d7d0)\
  2017-08-05 19:46:40 +0200
  * fix sporadic failures of perfschema.privilege\_table\_io
* [Revision #2ef7a5a13a](https://github.com/MariaDB/server/commit/2ef7a5a13a)\
  2017-08-04 13:11:05 +0300
  * [MDEV-13443](https://jira.mariadb.org/browse/MDEV-13443): Port innochecksum tests from 10.2 innodb\_zip suite to 10.1
* [Revision #19f2b3d02f](https://github.com/MariaDB/server/commit/19f2b3d02f)\
  2017-08-05 19:26:31 +0300
  * Fixed compiler warnings
* [Revision #74543698a7](https://github.com/MariaDB/server/commit/74543698a7)\
  2017-08-05 19:26:10 +0300
  * [MDEV-13179](https://jira.mariadb.org/browse/MDEV-13179) main.errors fails with wrong errno
* [Revision #008786aedb](https://github.com/MariaDB/server/commit/008786aedb)\
  2017-08-05 20:41:55 +0300
  * [MDEV-13456](https://jira.mariadb.org/browse/MDEV-13456) main.create\_drop\_event fails sporadically in buildbot
* [Revision #8b019f87dd](https://github.com/MariaDB/server/commit/8b019f87dd)\
  2017-08-03 08:29:36 +0300
  * [MDEV-11939](https://jira.mariadb.org/browse/MDEV-11939): innochecksum mistakes a file for an encrypted one (page 0 invalid)
* [Revision #56959e7b2c](https://github.com/MariaDB/server/commit/56959e7b2c)\
  2017-08-01 09:46:27 +0400
  * [MDEV-11963](https://jira.mariadb.org/browse/MDEV-11963) RPM Lint: script-without-shebang /usr/bin/wsrep\_sst\_common.
* [Revision #d1b3e428d4](https://github.com/MariaDB/server/commit/d1b3e428d4)\
  2017-07-20 11:24:01 +0300
  * [MDEV-13227](https://jira.mariadb.org/browse/MDEV-13227): Assertion failure len < 16384 in file rem0rec.cc line 1285
* [Revision #f58142f644](https://github.com/MariaDB/server/commit/f58142f644)\
  2017-07-13 14:49:57 +0000
  * mariadb-backup : don't change argv\[0] to "innobackupex" in innobackupex mode.
* [Revision #9284e8b2c6](https://github.com/MariaDB/server/commit/9284e8b2c6)\
  2017-07-12 19:34:55 +0300
  * [MDEV-11828](https://jira.mariadb.org/browse/MDEV-11828): innodb\_page\_size=64k must reject ROW\_FORMAT=REDUNDANT records longer than 16383 bytes
* Merge [Revision #9e11e055ce](https://github.com/MariaDB/server/commit/9e11e055ce) 2017-07-07 11:30:03 +0200 - Merge branch '10.0' into 10.1
* [Revision #2b5c9bc2c8](https://github.com/MariaDB/server/commit/2b5c9bc2c8)\
  2017-07-06 14:18:53 +0300
  * [MDEV-13247](https://jira.mariadb.org/browse/MDEV-13247) innodb\_log\_compressed\_pages=OFF breaks crash recovery of ROW\_FORMAT=COMPRESSED tables
* [Revision #ec76945dac](https://github.com/MariaDB/server/commit/ec76945dac)\
  2017-07-06 00:45:43 +0300
  * [MDEV-13248](https://jira.mariadb.org/browse/MDEV-13248) binlog.binlog\_parallel\_replication\_marks\_row fails in buildbot
* [Revision #4693f01f57](https://github.com/MariaDB/server/commit/4693f01f57)\
  2017-07-05 18:27:03 +0300
  * Fix warning discovered by ASAN
* [Revision #e555540ab6](https://github.com/MariaDB/server/commit/e555540ab6)\
  2017-07-05 14:35:55 +0300
  * [MDEV-13105](https://jira.mariadb.org/browse/MDEV-13105) InnoDB fails to load a table with PAGE\_COMPRESSION\_LEVEL after upgrade from 10.1.20
* [Revision #8ae9c86f2a](https://github.com/MariaDB/server/commit/8ae9c86f2a)\
  2017-07-04 10:26:14 -0400
  * bump the VERSION
* [Revision #f8dadbdf24](https://github.com/MariaDB/server/commit/f8dadbdf24)\
  2017-06-04 11:47:30 +0300
  * Ensure that we have LOG\_log locked when relay\_log.close is called
* [Revision #228479a28c](https://github.com/MariaDB/server/commit/228479a28c)\
  2017-05-29 11:35:36 +0300
  * [MDEV-8075](https://jira.mariadb.org/browse/MDEV-8075): DROP TEMPORARY TABLE not marked as ddl, causing optimistic parallel replication to fail

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
