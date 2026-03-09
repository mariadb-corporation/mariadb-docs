# MariaDB 5.5.46 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.46)[Release Notes](../../old-releases/5.5/5.5.46.md)[Changelog](mariadb-5546-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 12 Oct 2015

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.46.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #16c4b3c](https://github.com/MariaDB/server/commit/16c4b3c)\
  2015-10-09 16:43:59 +0200
  * fixes for buildbot
* [Revision #f41a41f](https://github.com/MariaDB/server/commit/f41a41f)\
  2015-10-09 00:06:16 +0200
  * Merge branch 'merge-xtradb-5.5' into 5.5
* [Revision #db79f4c](https://github.com/MariaDB/server/commit/db79f4c)\
  2015-10-08 23:02:43 +0200
  * 5.5.45-37.4
* [Revision #82e9f6d](https://github.com/MariaDB/server/commit/82e9f6d)\
  2015-10-08 22:54:24 +0200
  * Merge remote-tracking branch 'mysql/5.5' into 5.5
* [Revision #c8d5112](https://github.com/MariaDB/server/commit/c8d5112)\
  2015-10-08 00:32:07 +0200
  * [MDEV-8796](https://jira.mariadb.org/browse/MDEV-8796) Delete with sub query with information\_schema.TABLES deletes too many rows
* [Revision #504802f](https://github.com/MariaDB/server/commit/504802f)\
  2015-08-05 11:57:35 +0200
  * [MDEV-7846](https://jira.mariadb.org/browse/MDEV-7846): postreview fix
* [Revision #54b9981](https://github.com/MariaDB/server/commit/54b9981)\
  2015-04-23 20:08:57 +0200
  * [MDEV-7846](https://jira.mariadb.org/browse/MDEV-7846): Server crashes in Item\_subselect::fix\_fields or fails with Thread stack overrun
* [Revision #0ab93fd](https://github.com/MariaDB/server/commit/0ab93fd)\
  2015-04-23 19:16:57 +0200
  * [MDEV-7445](https://jira.mariadb.org/browse/MDEV-7445):Server crash with Signal 6 [MDEV-7565](https://jira.mariadb.org/browse/MDEV-7565): Server crash with Signal 6 (part 2)
* [Revision #2e3e818](https://github.com/MariaDB/server/commit/2e3e818)\
  2015-04-23 19:11:06 +0200
  * [MDEV-7445](https://jira.mariadb.org/browse/MDEV-7445): Server crash with Signal 6
* [Revision #7ccde2c](https://github.com/MariaDB/server/commit/7ccde2c)\
  2015-04-23 19:04:11 +0200
  * [MDEV-7565](https://jira.mariadb.org/browse/MDEV-7565): Server crash with Signal 6 (part 2)
* [Revision #006acf7](https://github.com/MariaDB/server/commit/006acf7)\
  2015-09-30 10:49:45 +0300
  * Bug #68148: drop index on a foreign key column leads to missing table [MDEV-8845](https://jira.mariadb.org/browse/MDEV-8845): Table disappear after modifying FK
* [Revision #a95711e](https://github.com/MariaDB/server/commit/a95711e)\
  2015-09-29 08:39:54 +0300
  * [MDEV-8855](https://jira.mariadb.org/browse/MDEV-8855): innodb.innodb-fk-warnings fails on Windows
* [Revision #02a38fd](https://github.com/MariaDB/server/commit/02a38fd)\
  2015-09-24 17:25:52 +0200
  * [MDEV-8624](https://jira.mariadb.org/browse/MDEV-8624): MariaDB hangs on query with many logical condition
* [Revision #f804b74](https://github.com/MariaDB/server/commit/f804b74)\
  2015-09-28 03:40:29 +0300
  * [MDEV-8154](https://jira.mariadb.org/browse/MDEV-8154) rpl.show\_status\_stop\_slave\_race-7126 sporadically causes internal check failure
* [Revision #ce7d8c5](https://github.com/MariaDB/server/commit/ce7d8c5)\
  2015-09-27 18:01:47 +0300
  * [MDEV-7330](https://jira.mariadb.org/browse/MDEV-7330) plugins.feedback\_plugin\_send fails sporadically in buildbot
* [Revision #bdcf370](https://github.com/MariaDB/server/commit/bdcf370)\
  2015-09-27 16:00:48 +0300
  * [MDEV-7933](https://jira.mariadb.org/browse/MDEV-7933) plugins.feedback\_plugin\_send depends on being executed after plugins.feedback\_plugin\_load
* [Revision #2563609](https://github.com/MariaDB/server/commit/2563609)\
  2015-09-26 02:51:29 +0300
  * Increased the version number
* [Revision #86ed494](https://github.com/MariaDB/server/commit/86ed494)\
  2015-09-26 02:48:55 +0300
  * [MDEV-8849](https://jira.mariadb.org/browse/MDEV-8849) rpl.rpl\_innodb\_bug30888 sporadically fails in buildbot with testcase timeout
* [Revision #dca4ab9](https://github.com/MariaDB/server/commit/dca4ab9)\
  2015-09-24 21:24:28 +0300
  * [MDEV-8841](https://jira.mariadb.org/browse/MDEV-8841) innodb\_zip.innodb-create-options fails in buildbot
* [Revision #5cc149f](https://github.com/MariaDB/server/commit/5cc149f)\
  2015-09-24 10:28:47 +0200
  * The compiler warnings fixed.
* [Revision #29ac245](https://github.com/MariaDB/server/commit/29ac245)\
  2015-09-07 13:13:52 +0200
  * [MDEV-8473](https://jira.mariadb.org/browse/MDEV-8473): mysqlbinlog -v does not properly decode DECIMAL values in an RBR log
* [Revision #102a85f](https://github.com/MariaDB/server/commit/102a85f)\
  2015-09-03 18:00:43 +0200
  * [MDEV-8663](https://jira.mariadb.org/browse/MDEV-8663): IF Statement returns multiple values erroneously (or Assertion \`!null\_value' failed in Item::send(Protocol\*, String\*))

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
