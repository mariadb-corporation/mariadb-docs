# MariaDB 5.5.68 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/5.5/5.5.68.md)[Changelog](mariadb-5568-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/5.5.68/)

**Release date:** 12 May 2020

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.68.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/5.5) you can view more details\
of the revision and view diffs of the code modified in that revision.

* [Revision #f20c63264a](https://github.com/MariaDB/server/commit/f20c63264a)\
  2020-05-06 13:47:55 +0300
  * [MDEV-21462](https://jira.mariadb.org/browse/MDEV-21462): Actually test for the original bug
* [Revision #459e8619f2](https://github.com/MariaDB/server/commit/459e8619f2)\
  2020-05-06 11:51:44 +0300
  * [MDEV-21462](https://jira.mariadb.org/browse/MDEV-21462) main.processlist\_notembedded fails to clean up
* [Revision #6a31aea5a1](https://github.com/MariaDB/server/commit/6a31aea5a1)\
  2020-04-28 11:20:52 +0200
  * BUG#30301356 - SOME EVENTS ARE DELAYED AFTER DROPPING EVENT
* [Revision #69bd73173d](https://github.com/MariaDB/server/commit/69bd73173d)\
  2020-04-28 21:41:49 +0200
  * correct off-by-one error in CONCAT
* [Revision #e8e67bd4a4](https://github.com/MariaDB/server/commit/e8e67bd4a4)\
  2019-12-26 16:29:04 +0530
  * Bug#30689251 - BACKPORT TO MYSQL-5.6, BUG#29597896 - NULL POINTER DEREFERENCE IN LIBMYSQL
* [Revision #39c60116e8](https://github.com/MariaDB/server/commit/39c60116e8)\
  2019-12-13 13:03:08 +0100
  * Bug#30628268: OUT OF MEMORY CRASH
* [Revision #6bb28e0bc5](https://github.com/MariaDB/server/commit/6bb28e0bc5)\
  2020-04-28 14:59:47 +0200
  * Bug#29915479 RUNNING COM\_REGISTER\_SLAVE WITHOUT COM\_BINLOG\_DUMP CAN RESULTS IN SERVER EXIT
* [Revision #8c534bdeb8](https://github.com/MariaDB/server/commit/8c534bdeb8)\
  2020-04-28 14:45:36 +0200
  * cleanup: remove dbug keywords that are never used
* [Revision #59880df8cd](https://github.com/MariaDB/server/commit/59880df8cd)\
  2020-04-27 15:49:27 +0200
  * Bug#28388217 - SERVER CAN FAIL WHILE REPLICATING CONDITIONAL COMMENTS
* [Revision #4d1de554bb](https://github.com/MariaDB/server/commit/4d1de554bb)\
  2019-11-26 09:39:35 +0530
  * Bug#28388217 - SERVER CAN FAIL WHILE REPLICATING CONDITIONAL COMMENTS
* [Revision #a13157a561](https://github.com/MariaDB/server/commit/a13157a561)\
  2020-04-27 15:50:51 +0200
  * don't enable -Werror in ft-index
* [Revision #ac2604f923](https://github.com/MariaDB/server/commit/ac2604f923)\
  2020-04-25 13:47:43 +0300
  * Correct the name of a contributor
* [Revision #bc1be39972](https://github.com/MariaDB/server/commit/bc1be39972)\
  2020-04-13 15:47:02 +0200
  * Fix failure for ipv6 not enabled
* [Revision #29cdd50822](https://github.com/MariaDB/server/commit/29cdd50822)\
  2020-04-17 20:58:55 -0700
  * [MDEV-21932](https://jira.mariadb.org/browse/MDEV-21932) Another attempt to fix the bug .
* [Revision #280b158501](https://github.com/MariaDB/server/commit/280b158501)\
  2020-04-13 16:12:18 +0200
  * Fix wrong argument size passed to --parent-pid strncmp check
* [Revision #b7cfd19759](https://github.com/MariaDB/server/commit/b7cfd19759)\
  2020-04-16 13:11:30 +0530
  * Minor fixup to [MDEV-22191](https://jira.mariadb.org/browse/MDEV-22191)
* [Revision #c1394ab6b5](https://github.com/MariaDB/server/commit/c1394ab6b5)\
  2020-04-08 17:39:27 +0530
  * [MDEV-22191](https://jira.mariadb.org/browse/MDEV-22191): Range access is not picked when index\_merge\_sort\_union is turned off
* [Revision #64b70b09e6](https://github.com/MariaDB/server/commit/64b70b09e6)\
  2020-03-30 16:36:48 +0300
  * my.cnf: mention that config files must be \*.cnf
* [Revision #24cb76b8dd](https://github.com/MariaDB/server/commit/24cb76b8dd)\
  2020-03-24 23:30:40 +0100
  * [MDEV-22032](https://jira.mariadb.org/browse/MDEV-22032) update HeidiSQL to version 11
* [Revision #407b0a6ae7](https://github.com/MariaDB/server/commit/407b0a6ae7)\
  2020-03-14 19:58:57 -0700
  * [MDEV-10466](https://jira.mariadb.org/browse/MDEV-10466) Server crashed in SEL\_ARG::store\_min() with extended\_keys=on
* [Revision #5af12e4635](https://github.com/MariaDB/server/commit/5af12e4635)\
  2020-03-12 23:50:20 -0700
  * [MDEV-21932](https://jira.mariadb.org/browse/MDEV-21932) A fast plan with ROR index-merge is ignored when 'index\_merge\_sort\_union=off'
* [Revision #3ab33c6c92](https://github.com/MariaDB/server/commit/3ab33c6c92)\
  2020-03-11 14:27:16 +0200
  * Cleanup: clang-10 -Wmisleading-indentation
* [Revision #be77fa914c](https://github.com/MariaDB/server/commit/be77fa914c)\
  2020-02-12 14:30:31 +0100
  * [MDEV-21646](https://jira.mariadb.org/browse/MDEV-21646): Failure to compile my\_addr\_resolve.c with binutils-2.34
* [Revision #4932ec871f](https://github.com/MariaDB/server/commit/4932ec871f)\
  2020-01-29 12:49:06 +0100
  * Clean the comment for `table_f_c unt` parameter
* [Revision #585e32cf3a](https://github.com/MariaDB/server/commit/585e32cf3a)\
  2020-01-27 15:01:14 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
