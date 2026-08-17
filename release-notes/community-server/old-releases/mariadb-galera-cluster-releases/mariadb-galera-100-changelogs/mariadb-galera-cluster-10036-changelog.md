# MariaDB Galera Cluster 10.0.36 Changelog

The most recent [MariaDB Galera Cluster 10.0]({galera}) release is:[**MariaDB Galera Cluster 10.0.38**](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.36)[Release Notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10036-release-notes.md)[Changelog](mariadb-galera-cluster-10036-changelog.md)[Overview of MariaDB Galera Cluster]({galera}/readme/mariadb-galera-cluster-guide)

**Release date:** 7 Aug 2018

For the highlights of this release, see the [release notes](../mariadb-galera-100-release-notes/mariadb-galera-cluster-10036-release-notes.md).\
For changes made in MariaDB, see the [MariaDB 10.0.36 Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10036-changelog.md).

The revision number links will take you to the revision's page on Github. On\
Github you can view more details of the revision and view diffs of the code
modified in that revision.

* [Revision #5d90717cc9](https://github.com/MariaDB/server/commit/5d90717cc9)\
  2018-08-04 11:28:25 +0300
  * Add wsrep.cnf
* [Revision #ea0356e1ad](https://github.com/MariaDB/server/commit/ea0356e1ad)\
  2018-08-03 16:43:32 +0300
  * Add galera library dependency directly to test case.
* [Revision #9808e23a7a](https://github.com/MariaDB/server/commit/9808e23a7a)\
  2018-08-03 13:44:30 +0300
  * MariaDB adjustments.
* [Revision #3f0cd66a2b](https://github.com/MariaDB/server/commit/3f0cd66a2b)\
  2018-07-16 09:42:53 +0200
  * Also include InnoDB undo tablespaces in rsync sst
* [Revision #62e290923e](https://github.com/MariaDB/server/commit/62e290923e)\
  2018-07-16 09:41:37 +0200
  * Put one filter per line in wsrep\_sst\_rsync.sh
* [Revision #639bd1c71f](https://github.com/MariaDB/server/commit/639bd1c71f)\
  2018-07-06 11:53:43 +0200
  * galera#505 mtr test
* [Revision #1d414d9491](https://github.com/MariaDB/server/commit/1d414d9491)\
  2018-03-01 17:07:07 +0200
  * codership/galera#501 Check cluster weight in galera\_pc\_weight test
* [Revision #40f6bcb856](https://github.com/MariaDB/server/commit/40f6bcb856)\
  2018-08-02 20:35:44 +0300
  * Add missing WSREP(thd) condition and remove unnecessary DBUG\_RETURN.
* Merge [Revision #9b29bda0d6](https://github.com/MariaDB/server/commit/9b29bda0d6) 2018-08-02 13:13:21 +0300 - Merge remote-tracking branch 'origin/5.5-galera' into 10.0-galera
* [Revision #e88e26b424](https://github.com/MariaDB/server/commit/e88e26b424)\
  2018-05-23 14:13:11 +0200
  * Follow up to previous commit for codership/mysql-wsrep#332
* [Revision #4d2b552369](https://github.com/MariaDB/server/commit/4d2b552369)\
  2018-05-22 16:45:27 +0200
  * Fix FK constraint violation in applier, after ALTER TABLE ADD FK
* Merge [Revision #b286a9f823](https://github.com/MariaDB/server/commit/b286a9f823) 2018-08-01 10:58:38 +0300 - Merge tag 'mariadb-5.5.61' into 5.5-galera
* [Revision #33e39f0682](https://github.com/MariaDB/server/commit/33e39f0682)\
  2018-05-03 10:23:36 -0400
  * bump the VERSION
* Merge [Revision #c5a8583b31](https://github.com/MariaDB/server/commit/c5a8583b31) 2018-08-02 11:44:02 +0300 - Merge tag 'mariadb-10.0.36' into 10.0-galera
* [Revision #c863159c32](https://github.com/MariaDB/server/commit/c863159c32)\
  2018-07-24 14:54:50 +0300
  * [MDEV-16799](https://jira.mariadb.org/browse/MDEV-16799): Test wsrep.variables crash at sql\_class.cc:639 thd\_get\_ha\_data
* [Revision #f99fe68b4f](https://github.com/MariaDB/server/commit/f99fe68b4f)\
  2018-07-19 21:05:36 +0300
  * Fix compile error.
* [Revision #c09d54924a](https://github.com/MariaDB/server/commit/c09d54924a)\
  2018-07-19 15:13:31 +0300
  * [MDEV-10564](https://jira.mariadb.org/browse/MDEV-10564): Galera `wsrep_debug` patch logs MySQL user credentials
* Merge [Revision #71e0ba4ae6](https://github.com/MariaDB/server/commit/71e0ba4ae6) 2018-07-19 07:04:40 +0300 - Merge pull request #645 from grooverdan/10.0-wsrep\_sst\_common\_bashism
* [Revision #6aa22eaf62](https://github.com/MariaDB/server/commit/6aa22eaf62)\
  2018-03-07 14:36:40 +1100
  * wsrep\_sst\_common: fix per shellcheck
* [Revision #cf648afd5b](https://github.com/MariaDB/server/commit/cf648afd5b)\
  2018-06-14 15:12:13 +0200
  * fix galera sst tests
* [Revision #215d652c66](https://github.com/MariaDB/server/commit/215d652c66)\
  2018-05-09 09:16:20 +0300
  * [MDEV-15351](https://jira.mariadb.org/browse/MDEV-15351): wsrep\_sst\_xtrabackup is broken in 10.1.31
* [Revision #82f26dafcb](https://github.com/MariaDB/server/commit/82f26dafcb)\
  2018-03-12 15:23:58 +1100
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968): wsrep\_log\_error not defined until later in wsrep\_sst\_common
* [Revision #fe3c4a4182](https://github.com/MariaDB/server/commit/fe3c4a4182)\
  2017-10-24 20:59:54 +0200
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968) sst fails with "WSREP\_SST\_OPT\_PORT: readonly variable"
* [Revision #e6b31df6df](https://github.com/MariaDB/server/commit/e6b31df6df)\
  2017-10-16 17:49:52 +0200
  * [MDEV-13968](https://jira.mariadb.org/browse/MDEV-13968) sst fails with "WSREP\_SST\_OPT\_PORT: readonly variable"
* [Revision #24ab82e675](https://github.com/MariaDB/server/commit/24ab82e675)\
  2018-03-12 15:14:15 +1100
  * [MDEV-15541](https://jira.mariadb.org/browse/MDEV-15541): wsrep\_sst\_common - WSREP\_SST\_OPT\_PORT set twice (--address and --port)
* [Revision #2b35db5ac4](https://github.com/MariaDB/server/commit/2b35db5ac4)\
  2018-03-07 13:10:01 +1100
  * [MDEV-15496](https://jira.mariadb.org/browse/MDEV-15496): wsrep\_sst\_common - parse IPv6 correct
* [Revision #0f80c014c1](https://github.com/MariaDB/server/commit/0f80c014c1)\
  2018-05-09 11:22:26 -0400
  * bump the VERSION
* Merge [Revision #2bbc868c50](https://github.com/MariaDB/server/commit/2bbc868c50) 2018-05-09 10:05:14 +0300 - Merge pull request #710 from grooverdan/10.0-galera-[MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743)-mysqld-socket-o\_cloexec
* [Revision #ccd566af20](https://github.com/MariaDB/server/commit/ccd566af20)\
  2018-04-19 07:38:57 +1000
  * [MDEV-8743](https://jira.mariadb.org/browse/MDEV-8743): mysqld port/socket - FD\_CLOEXEC if no SOCK\_CLOEXEC

{% include "../../../../.gitbook/includes/announce.md" %}

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
