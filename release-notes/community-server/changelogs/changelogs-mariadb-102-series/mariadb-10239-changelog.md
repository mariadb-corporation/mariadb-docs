# MariaDB 10.2.39 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download 10.2.39](https://downloads.mariadb.org/mariadb/10.2.39/)[Release Notes](../../old-releases/10.2/10.2.39.md)[Changelog](mariadb-10239-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 23 Jun 2021

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.39.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #dfa2d0bc13](https://github.com/MariaDB/server/commit/dfa2d0bc13)\
  2021-06-07 17:46:59 +0300
  * [MDEV-25869](https://jira.mariadb.org/browse/MDEV-25869) Change buffer entries are lost on InnoDB restart
* [Revision #3c922d6def](https://github.com/MariaDB/server/commit/3c922d6def)\
  2021-05-28 22:04:17 -0700
  * Revert "CONNECT: move jar files to /usr/share and include them in DEBs"
* [Revision #9f9a925c39](https://github.com/MariaDB/server/commit/9f9a925c39)\
  2021-06-06 08:46:59 +0200
  * [MDEV-23815](https://jira.mariadb.org/browse/MDEV-23815) Windows : mysql\_upgrade\_wizard fails, if service name has spaces
* [Revision #cebc435592](https://github.com/MariaDB/server/commit/cebc435592)\
  2021-06-05 16:57:10 +0200
  * [MDEV-25859](https://jira.mariadb.org/browse/MDEV-25859) - HeidiSQL 11.3
* [Revision #7eed97ed9f](https://github.com/MariaDB/server/commit/7eed97ed9f)\
  2021-05-26 14:15:26 +0200
  * [MDEV-25777](https://jira.mariadb.org/browse/MDEV-25777): JAVA\_INCLUDE\_PATH and JAVA\_INCLUDE\_PATH2 not found with out of source configuration and Ninja generator
* [Revision #5c896472b6](https://github.com/MariaDB/server/commit/5c896472b6)\
  2021-06-02 23:10:21 +0200
  * [MDEV-25672](https://jira.mariadb.org/browse/MDEV-25672) table alias from previous statement interferes later commands
* [Revision #2e78910806](https://github.com/MariaDB/server/commit/2e78910806)\
  2021-06-02 08:40:30 -0700
  * [MDEV-25635](https://jira.mariadb.org/browse/MDEV-25635) Assertion failure when pushing from HAVING into WHERE of view
* [Revision #a8434c6c59](https://github.com/MariaDB/server/commit/a8434c6c59)\
  2021-06-02 08:25:12 +0300
  * [MDEV-25730](https://jira.mariadb.org/browse/MDEV-25730) fixup: GCC -Og -Wmaybe-uninitialized
* [Revision #2fb4407827](https://github.com/MariaDB/server/commit/2fb4407827)\
  2021-05-29 19:54:25 +0200
  * [MDEV-25818](https://jira.mariadb.org/browse/MDEV-25818): RSYNC SST failed due to busy port
* [Revision #d3c77e08ae](https://github.com/MariaDB/server/commit/d3c77e08ae)\
  2021-05-31 12:27:47 +0200
  * [MDEV-20556](https://jira.mariadb.org/browse/MDEV-20556) Remove references to "xtrabackup" and "innobackupex" in mariadb-backup --help
* [Revision #91bde0fb67](https://github.com/MariaDB/server/commit/91bde0fb67)\
  2021-05-30 17:31:55 +0700
  * [MDEV-25576](https://jira.mariadb.org/browse/MDEV-25576): The statement EXPLAIN running as regular statement and as prepared statement produces different results for UPDATE with subquery
* [Revision #d06205ba37](https://github.com/MariaDB/server/commit/d06205ba37)\
  2021-05-27 14:00:58 +0200
  * CONNECT: use my\_snprintf
* [Revision #1638241e31](https://github.com/MariaDB/server/commit/1638241e31)\
  2021-05-27 12:06:21 +0200
  * mtr: fix the debug printout
* [Revision #ef0d883903](https://github.com/MariaDB/server/commit/ef0d883903)\
  2021-05-26 15:27:07 +0300
  * Revert "Add Pull Request template file to the MariaDB/server repository"
* [Revision #c11c5f36d8](https://github.com/MariaDB/server/commit/c11c5f36d8)\
  2021-05-24 19:40:47 +0530
  * [MDEV-25758](https://jira.mariadb.org/browse/MDEV-25758) InnoDB spatial indexes miss large geometry fields after [MDEV-25459](https://jira.mariadb.org/browse/MDEV-25459)
* [Revision #ab87fc6c7a](https://github.com/MariaDB/server/commit/ab87fc6c7a)\
  2021-05-27 09:31:19 +0300
  * Cleanup: Remove handler::update\_table\_comment()
* [Revision #17106c984b](https://github.com/MariaDB/server/commit/17106c984b)\
  2021-03-11 18:17:06 +0200
  * Add Pull Request template file to the MariaDB/server repository
* [Revision #d8fa71a089](https://github.com/MariaDB/server/commit/d8fa71a089)\
  2021-05-19 22:26:02 +0200
  * [MDEV-25730](https://jira.mariadb.org/browse/MDEV-25730): maria.repair test fails with valgrind
* [Revision #fe7e44d8ad](https://github.com/MariaDB/server/commit/fe7e44d8ad)\
  2021-05-25 05:08:25 +0200
  * [MDEV-21192](https://jira.mariadb.org/browse/MDEV-21192): SST failing when enabling IPV6
* [Revision #81f94c26a4](https://github.com/MariaDB/server/commit/81f94c26a4)\
  2021-05-24 16:48:27 +0200
  * [MDEV-15730](https://jira.mariadb.org/browse/MDEV-15730): rename --stream=xbstream to --stream=mbstream
* [Revision #5c75ba9cad](https://github.com/MariaDB/server/commit/5c75ba9cad)\
  2021-05-24 11:33:01 +0530
  * [MDEV-25663](https://jira.mariadb.org/browse/MDEV-25663) Double free of transaction during truncate operation
* [Revision #349d77ecdd](https://github.com/MariaDB/server/commit/349d77ecdd)\
  2021-05-20 15:47:21 +0530
  * [MDEV-25721](https://jira.mariadb.org/browse/MDEV-25721) Double free of table when inplace alter FTS add index fails
* [Revision #98f7b2cb09](https://github.com/MariaDB/server/commit/98f7b2cb09)\
  2021-05-14 14:13:59 +0530
  * [MDEV-25663](https://jira.mariadb.org/browse/MDEV-25663) Double free of transaction during truncate operation
* [Revision #c88e9342f3](https://github.com/MariaDB/server/commit/c88e9342f3)\
  2021-05-23 01:11:19 +0200
  * [MDEV-25759](https://jira.mariadb.org/browse/MDEV-25759): is\_local\_ip function can come to incorrect conclusion
* [Revision #f70b11c8c9](https://github.com/MariaDB/server/commit/f70b11c8c9)\
  2021-05-21 10:52:12 +0200
  * cmake: fewer Build-Depends in SRPM
* [Revision #d7321893d8](https://github.com/MariaDB/server/commit/d7321893d8)\
  2021-05-14 21:25:46 +0200
  * CONNECT: move jar files to /usr/share and include them in DEBs
* [Revision #9d0fde3ba1](https://github.com/MariaDB/server/commit/9d0fde3ba1)\
  2021-05-22 12:21:05 +0200
  * cmake: silence repeated git searches too
* [Revision #f9f8cae9fe](https://github.com/MariaDB/server/commit/f9f8cae9fe)\
  2021-05-14 19:55:53 +0200
  * cmake: fix FindJava/FindJNI wrappers for cmake re-runs
* [Revision #6bf866cc79](https://github.com/MariaDB/server/commit/6bf866cc79)\
  2021-05-14 14:45:53 +0200
  * [MDEV-25641](https://jira.mariadb.org/browse/MDEV-25641) max\_password\_errors not working with ed25519 auth plugin
* [Revision #681918a849](https://github.com/MariaDB/server/commit/681918a849)\
  2021-05-13 18:35:02 +0200
  * [MDEV-24996](https://jira.mariadb.org/browse/MDEV-24996) file conflict in rpm packages
* [Revision #43c9fcefc0](https://github.com/MariaDB/server/commit/43c9fcefc0)\
  2021-05-12 19:32:29 -0700
  * [MDEV-23886](https://jira.mariadb.org/browse/MDEV-23886) Reusing CTE inside a function fails with table doesn't exist
* [Revision #9739cf1859](https://github.com/MariaDB/server/commit/9739cf1859)\
  2021-05-21 18:50:30 +0300
  * [MDEV-25664](https://jira.mariadb.org/browse/MDEV-25664) Potential hang in purge for virtual columns
* [Revision #2087d47aae](https://github.com/MariaDB/server/commit/2087d47aae)\
  2021-05-21 17:46:48 +0300
  * [MDEV-22462](https://jira.mariadb.org/browse/MDEV-22462): Item\_in\_subselect::create\_single\_in\_to\_exists\_cond(JOIN \*, Item , Item ): Assertion \`false' failed.
* [Revision #8c8a6ed3b8](https://github.com/MariaDB/server/commit/8c8a6ed3b8)\
  2021-05-21 03:11:48 +0200
  * [MDEV-25719](https://jira.mariadb.org/browse/MDEV-25719): stunnel uses "verifyChain" without subject checks
* [Revision #629449172a](https://github.com/MariaDB/server/commit/629449172a)\
  2021-04-30 23:14:57 +0530
  * [MDEV-25462](https://jira.mariadb.org/browse/MDEV-25462): Assertion \`m\_status == DA\_ERROR || m\_status == DA\_OK || m\_status == DA\_OK\_BULK' failed in Diagnostics\_area::message from get\_schema\_tables\_record
* [Revision #406ce57232](https://github.com/MariaDB/server/commit/406ce57232)\
  2021-05-19 18:09:49 +1000
  * [MDEV-25728](https://jira.mariadb.org/browse/MDEV-25728): mysqld --help --verbose creates a log-bin-index file
* [Revision #e570f740cd](https://github.com/MariaDB/server/commit/e570f740cd)\
  2021-05-14 20:43:21 +0300
  * [MDEV-25629](https://jira.mariadb.org/browse/MDEV-25629): Crash in get\_sort\_by\_table() in subquery with order by having outer ref
* [Revision #af8d4a97e2](https://github.com/MariaDB/server/commit/af8d4a97e2)\
  2021-05-18 15:45:43 +0530
  * [MDEV-22530](https://jira.mariadb.org/browse/MDEV-22530): Aborting OPTIMIZE TABLE still logs in binary log and replicates to the Slave server.
* [Revision #acede480c5](https://github.com/MariaDB/server/commit/acede480c5)\
  2021-05-13 15:31:58 +0300
  * Updated galera\_3nodes disabled.def file
* [Revision #b9a2e4609f](https://github.com/MariaDB/server/commit/b9a2e4609f)\
  2021-05-18 08:37:24 +0300
  * [MDEV-25594](https://jira.mariadb.org/browse/MDEV-25594): Assertion failure in DeadlockChecker::check\_and\_resolve()
* [Revision #23cad4d8c5](https://github.com/MariaDB/server/commit/23cad4d8c5)\
  2021-05-17 18:59:26 +0200
  * wsrep\_sst\_common.sh: file mode changed back to 664
* [Revision #88c7a58ecf](https://github.com/MariaDB/server/commit/88c7a58ecf)\
  2021-05-12 18:03:45 +0530
  * [MDEV-22530](https://jira.mariadb.org/browse/MDEV-22530): Aborting OPTIMIZE TABLE still logs in binary log and replicates to the Slave server.
* [Revision #410e3c1a9a](https://github.com/MariaDB/server/commit/410e3c1a9a)\
  2021-05-12 18:00:06 +0530
  * [MDEV-17515](https://jira.mariadb.org/browse/MDEV-17515): GTID Replication in optimistic mode deadlock
* [Revision #80ae3677e1](https://github.com/MariaDB/server/commit/80ae3677e1)\
  2021-05-17 09:39:19 +1000
  * [MDEV-25681](https://jira.mariadb.org/browse/MDEV-25681): --relay-log{,-index} missing warning
* [Revision #6811ed3e10](https://github.com/MariaDB/server/commit/6811ed3e10)\
  2021-05-14 12:51:36 +0200
  * [MDEV-25669](https://jira.mariadb.org/browse/MDEV-25669): SST scripts should check all server groups in config files
* [Revision #4675febb7a](https://github.com/MariaDB/server/commit/4675febb7a)\
  2021-05-13 12:23:11 +0200
  * Added missing connection lines to some tests
* [Revision #677f1ef6f0](https://github.com/MariaDB/server/commit/677f1ef6f0)\
  2021-05-14 16:43:36 -0700
  * [MDEV-25682](https://jira.mariadb.org/browse/MDEV-25682) Explain shows an execution plan different from actually executed
* [Revision #e607f3398c](https://github.com/MariaDB/server/commit/e607f3398c)\
  2021-04-14 10:56:12 +0100
  * [MDEV-25336](https://jira.mariadb.org/browse/MDEV-25336) Parallel replication causes failed assert while restarting
* [Revision #355dc74b76](https://github.com/MariaDB/server/commit/355dc74b76)\
  2021-04-14 11:23:38 +0100
  * [MDEV-22370](https://jira.mariadb.org/browse/MDEV-22370) safe\_mutex: Trying to lock uninitialized mutex at /data/src/10.4-bug/sql/rpl\_parallel.cc, line 470 upon shutdown during FTWRL
* [Revision #3616640a31](https://github.com/MariaDB/server/commit/3616640a31)\
  2020-01-17 20:26:14 +0200
  * [MDEV-20821](https://jira.mariadb.org/browse/MDEV-20821) parallel slave server shutdown hang
* [Revision #ec348f555b](https://github.com/MariaDB/server/commit/ec348f555b)\
  2021-05-11 20:08:40 +0200
  * mtr: --gdb mode, also quote ";", not only " "
* [Revision #3cf57aae9f](https://github.com/MariaDB/server/commit/3cf57aae9f)\
  2021-05-11 10:04:52 +0200
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580) addendum: normal operation in configurations where stunnel is not available
* [Revision #089d82a74b](https://github.com/MariaDB/server/commit/089d82a74b)\
  2021-05-10 09:50:56 -0400
  * bump the VERSION
* [Revision #8fef2b8667](https://github.com/MariaDB/server/commit/8fef2b8667)\
  2021-05-10 04:27:16 +0200
  * [MDEV-23580](https://jira.mariadb.org/browse/MDEV-23580): WSREP\_SST: \[ERROR] rsync daemon port has been taken
* [Revision #d0785f7731](https://github.com/MariaDB/server/commit/d0785f7731)\
  2021-05-09 10:32:49 +0200
  * [MDEV-25232](https://jira.mariadb.org/browse/MDEV-25232) Ninja MSVC build sets default CMAKE\_BUILD\_TYPE to Debug
* [Revision #e1bf1aea5c](https://github.com/MariaDB/server/commit/e1bf1aea5c)\
  2021-05-06 22:58:28 +0200
  * force jemalloc to be used in release rpm/deb builds
* [Revision #66acec99d5](https://github.com/MariaDB/server/commit/66acec99d5)\
  2021-05-03 18:10:13 +0200
  * XA PREPARE and SHOW STATUS
* [Revision #18fbe566bd](https://github.com/MariaDB/server/commit/18fbe566bd)\
  2021-05-03 18:01:30 +0200
  * mtr --gdb='commands' and restarts
* [Revision #af781f1ac4](https://github.com/MariaDB/server/commit/af781f1ac4)\
  2021-05-03 18:00:09 +0200
  * fix mtr --client-gdb to work
* [Revision #ad4b51948f](https://github.com/MariaDB/server/commit/ad4b51948f)\
  2021-05-03 17:53:17 +0200
  * Revert "Connect: remove Mongo dependencies"
* [Revision #afb8e87391](https://github.com/MariaDB/server/commit/afb8e87391)\
  2021-05-07 21:42:42 +0200
  * Skip auth\_named\_pipe test, if plugin was not built
* [Revision #76c2b5106e](https://github.com/MariaDB/server/commit/76c2b5106e)\
  2021-05-07 14:52:46 +0300
  * Fix clang++-11 -Wsometimes-uninitialized
* Merge [Revision #c225eee219](https://github.com/MariaDB/server/commit/c225eee219) 2021-05-07 11:18:55 +0200 - Merge branch 'bb-10.2-release' into 10.2
* [Revision #54d7ba9609](https://github.com/MariaDB/server/commit/54d7ba9609)\
  2021-05-06 04:03:07 +0200
  * [MDEV-25418](https://jira.mariadb.org/browse/MDEV-25418): Improve mariadb-backup SST script compliance with native MariaDB SSL practices and configuration.
* [Revision #cf67ca48d6](https://github.com/MariaDB/server/commit/cf67ca48d6)\
  2021-04-25 18:06:53 +0300
  * [MDEV-25418](https://jira.mariadb.org/browse/MDEV-25418) rsync SST does not work with stunnel encryption
* [Revision #ee1e877470](https://github.com/MariaDB/server/commit/ee1e877470)\
  2021-05-06 01:16:52 +0200
  * [MDEV-24962](https://jira.mariadb.org/browse/MDEV-24962) addendum: improved handling of paths with spaces
* [Revision #6895c9eaa0](https://github.com/MariaDB/server/commit/6895c9eaa0)\
  2021-05-05 03:17:51 +0200
  * [MDEV-24962](https://jira.mariadb.org/browse/MDEV-24962) addendum: mariadb-backup does not understand --log-bin-index and --log-basename options
* [Revision #5ad7f52558](https://github.com/MariaDB/server/commit/5ad7f52558)\
  2021-05-03 23:26:30 +0200
  * [MDEV-21603](https://jira.mariadb.org/browse/MDEV-21603) Crashing SHOW TABLES with derived table in WHERE condition
* [Revision #1ae7673aae](https://github.com/MariaDB/server/commit/1ae7673aae)\
  2021-04-28 01:39:31 +0200
  * [MDEV-24962](https://jira.mariadb.org/browse/MDEV-24962): Galera SST innobackupex-move ignores Environment settings
* [Revision #e0324bf300](https://github.com/MariaDB/server/commit/e0324bf300)\
  2021-04-15 13:53:28 +0200
  * wsrep sst scripts: removing extra blank lines and spaces

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
