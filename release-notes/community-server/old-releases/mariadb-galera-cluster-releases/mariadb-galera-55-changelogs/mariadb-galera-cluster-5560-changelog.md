# MariaDB Galera Cluster 5.5.60 Changelog

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.60)[Release Notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5560-release-notes.md)[Changelog](mariadb-galera-cluster-5560-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 3 May 2018

For the highlights of this release, see the [release notes](../mariadb-galera-55-release-notes/mariadb-galera-cluster-5560-release-notes.md). For changes in\
MariaDB, see the [MariaDB 5.5.60 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5560-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #1ecd68d867](https://github.com/MariaDB/server/commit/1ecd68d867)\
  2018-04-30 23:06:09 +0200
  * Use after free in authentication
* [Revision #ccad629d7e](https://github.com/MariaDB/server/commit/ccad629d7e)\
  2018-04-30 13:50:59 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* [Revision #75dec85c2e](https://github.com/MariaDB/server/commit/75dec85c2e)\
  2018-04-27 11:21:55 +0200
  * Bug#25471090: MYSQL USE AFTER FREE
* [Revision #231c02f7b9](https://github.com/MariaDB/server/commit/231c02f7b9)\
  2018-04-24 13:58:42 +0300
  * MariaDB adjustments.
* [Revision #c2c61bbcce](https://github.com/MariaDB/server/commit/c2c61bbcce)\
  2017-12-17 14:41:55 +0200
  * Provider rollback for ineffective trx
* Merge [Revision #a5001a2ad7](https://github.com/MariaDB/server/commit/a5001a2ad7) 2018-04-24 13:34:57 +0300 - Merge tag 'mariadb-5.5.60' into 5.5-galera
* Merge [Revision #804a7e60d7](https://github.com/MariaDB/server/commit/804a7e60d7) 2018-03-14 10:29:47 +0200 - Merge pull request #637 from grooverdan/5.5-galera
* [Revision #d3c0e34bdc](https://github.com/MariaDB/server/commit/d3c0e34bdc)\
  2018-03-02 16:19:14 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): protect myisam/aria MYI with O\_CLOEXEC
* [Revision #bbee025370](https://github.com/MariaDB/server/commit/bbee025370)\
  2018-03-02 12:45:36 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): O\_CLOEXEC on innodb/xtradb temp files
* [Revision #88fb8b2e36](https://github.com/MariaDB/server/commit/88fb8b2e36)\
  2018-03-02 11:52:20 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): protect myisam/aria MYD files and aria log files
* [Revision #c54c490c59](https://github.com/MariaDB/server/commit/c54c490c59)\
  2018-03-02 11:17:35 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): O\_CLOEXEC/SOCK\_CLOEXEC defines for non-unix compatibility
* [Revision #4ec7b84077](https://github.com/MariaDB/server/commit/4ec7b84077)\
  2018-03-02 10:54:34 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): use O\_CLOEXEC MYSQL\_LOG::open / TC\_LOG\_MMAP::open
* [Revision #9629bca1f0](https://github.com/MariaDB/server/commit/9629bca1f0)\
  2018-03-02 10:54:00 +1100
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): use O\_CLOEXEC (innodb/xtradb)
* [Revision #09b25f8596](https://github.com/MariaDB/server/commit/09b25f8596)\
  2018-03-01 16:35:46 +0100
  * only allow SUPER user to modify wsrep\_on
* [Revision #7cec685758](https://github.com/MariaDB/server/commit/7cec685758)\
  2018-01-30 05:37:22 -0800
  * Bump wsrep patch version to 25.23
* Merge [Revision #a8d64fbe16](https://github.com/MariaDB/server/commit/a8d64fbe16) 2018-01-24 10:34:25 +0200 - Merge pull request #570 from grooverdan/5.5-[MDEV-1044](https://jira.mariadb.org/browse/MDEV-1044)-backport-wsrep-no-new-processgroup
* [Revision #2400b769c6](https://github.com/MariaDB/server/commit/2400b769c6)\
  2016-11-21 16:20:10 -0500
  * [MDEV-10442](https://jira.mariadb.org/browse/MDEV-10442): "Address already in use" on restart
* [Revision #4132b1785a](https://github.com/MariaDB/server/commit/4132b1785a)\
  2018-01-23 12:05:10 -0500
  * bump the VERSION

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
