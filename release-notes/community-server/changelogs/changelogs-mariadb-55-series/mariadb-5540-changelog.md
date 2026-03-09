# MariaDB 5.5.40 Changelog

The most recent release in the [MariaDB 5.5](../../old-releases/5.5/changes-improvements-in-mariadb-5-5.md) series is:[**MariaDB 5.5.68**](../../old-releases/5.5/5.5.68.md) [Download Now](https://downloads.mariadb.org/mariadb/5.5.68/)

[Download](https://downloads.mariadb.org/mariadb/5.5.40)[Release Notes](../../old-releases/5.5/5.5.40.md)[Changelog](mariadb-5540-changelog.md)\[[Overview of 5.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)

**Release date:** 9 Oct 2014

For the highlights of this release, see the [release notes](../../old-releases/5.5/5.5.40.md).

The revision number links will take you to the revision's page on Launchpad. On\
Launchpad you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #4321](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4321)\
  Wed 2014-10-08 09:35:00 +0200
  * remove mariadb.pc file again, it cannot be added in a GA version
* [Revision #4320](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4320)\
  Wed 2014-10-08 09:24:41 +0200
  * don't run privilege checking tests in embedded
* [Revision #4319](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4319)\
  Wed 2014-10-08 00:46:10 +0200
  * decimal: _correct_ implementation of ROUND\_UP at last
* [Revision #4318](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4318)\
  Wed 2014-10-08 00:45:56 +0200
  * include mariadb.pc in debian builds
* [Revision #4317](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4317)\
  Wed 2014-10-08 00:45:41 +0200
  * jemalloc compatibility
* [Revision #4316](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4316) \[merge]\
  Wed 2014-10-08 00:44:37 +0200
  * XtraDB 5.5.40-36.1
  * [Revision #0.12.71](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.71)\
    Tue 2014-10-07 21:41:48 +0200
    * percona-server-5.5.40-36.1
* [Revision #4315](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4315)\
  Tue 2014-10-07 19:38:45 +0200
  * [MDEV-6781](https://jira.mariadb.org/browse/MDEV-6781): bug with query cache when using views
* [Revision #4314](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4314)\
  Tue 2014-10-07 16:21:53 +0200
  * packaging issues:
    * skip debian `44_scripts_mysql_config_libs.dpatch` it does not apply anymore (and anyway it would not work for a static library)
    * fix the path for install(mariadb.pc)
* [Revision #4313](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4313)\
  Tue 2014-10-07 11:55:39 +0200
  * [MDEV-5553](https://jira.mariadb.org/browse/MDEV-5553) A view or procedure with a non existing definer can block "SHOW TABLE STATUS" with an unclear error message
* [Revision #4312](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4312)\
  Tue 2014-10-07 10:54:14 +0200
  * [MDEV-4813](https://jira.mariadb.org/browse/MDEV-4813) Replication fails on updating a MEMORY table with an index using btree
* [Revision #4311](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4311)\
  Tue 2014-10-07 10:53:43 +0200
  * fixes for decimal type
* [Revision #4310](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4310)\
  Tue 2014-10-07 10:53:06 +0200
  * post-merge fixes
* [Revision #4309](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4309) \[merge]\
  Mon 2014-10-06 20:06:39 +0200
  * XtraDB 5.5.39-36.0
  * [Revision #0.12.70](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/0.12.70)\
    Mon 2014-10-06 19:56:00 +0200
    * percona-server-5.5.39-36.0
* [Revision #4308](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4308) \[merge]\
  Mon 2014-10-06 19:53:55 +0200
  * mysql-5.5.40
* [Revision #4307](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4307)\
  Fri 2014-10-03 23:04:25 +0200
  * [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) crash in GROUP\_CONCAT(IF () ORDER BY 1)
* [Revision #4306](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4306)\
  Thu 2014-10-02 16:58:26 +0200
  * [MDEV-5749](https://jira.mariadb.org/browse/MDEV-5749) Please add a .pc file to MariaDB for easy use via pkg-config
* [Revision #4305](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4305)\
  Thu 2014-10-02 13:52:51 +0200
  * [MDEV-6461](https://jira.mariadb.org/browse/MDEV-6461) mysqld should not trap SIGTSTP if running with --gdb/--debug-gdb
* [Revision #4304](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4304)\
  Thu 2014-10-02 13:47:52 +0200
  * [MDEV-6550](https://jira.mariadb.org/browse/MDEV-6550) Missing dependency on Debian 7 (Wheezy) installation package
* [Revision #4303](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4303)\
  Thu 2014-10-02 12:57:20 +0200
  * [MDEV-5707](https://jira.mariadb.org/browse/MDEV-5707) MTR fails on kfreebsd
* [Revision #4302](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4302)\
  Thu 2014-10-02 11:58:24 +0200
  * [MDEV-6528](https://jira.mariadb.org/browse/MDEV-6528) review debian patches for mysql
* [Revision #4301](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4301)\
  Thu 2014-10-02 11:58:13 +0200
  * [MDEV-6800](https://jira.mariadb.org/browse/MDEV-6800) auth\_socket plugin fails to build on OpenBSD with [MariaDB 10.0.14](../../old-releases/10.0/10.0.14.md)
* [Revision #4300](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4300)\
  Thu 2014-10-02 11:57:40 +0200
  * [MDEV-5120](https://jira.mariadb.org/browse/MDEV-5120) Test suite test maria-no-logging fails
* [Revision #4299](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4299)\
  Thu 2014-09-25 19:00:41 +0200
  * update tokudb version in CMakeLists.txt, disable unstable tokudb tests
* [Revision #4298](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4298)\
  Fri 2014-10-03 15:07:53 +0400
  * [MDEV-6592](https://jira.mariadb.org/browse/MDEV-6592) Assertion \`ltime->day == 0' failed with TIMESTAMP, MAKETIME
* [Revision #4297](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4297)\
  Thu 2014-09-25 10:43:11 +0400
  * [MDEV-6774](https://jira.mariadb.org/browse/MDEV-6774) - Deadlock between SELECT, DROP TABLE, SHOW STATUS and SET @@global.log\_output
* [Revision #4296](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4296)\
  Thu 2014-09-18 19:45:06 +0400
  * [MDEV-6749](https://jira.mariadb.org/browse/MDEV-6749) - Deadlock between GRANT/REVOKE, SELECT FROM I\_S.COLUMNS, SET slow\_query\_log and failed connection attempt
* [Revision #4295](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4295) \[merge]\
  Tue 2014-09-23 23:37:35 +0200
  * merge
  * [Revision #4292.1.2](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4292.1.2) \[merge]\
    Tue 2014-09-23 22:03:35 +0200
    * tokudb 7.5.0
  * [Revision #4292.1.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4292.1.1)\
    Fri 2014-09-19 09:21:51 +0200
    * remove unused (obsolete) declarations from slave.h
* [Revision #4294](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4294)\
  Tue 2014-09-23 13:57:55 +0300
  * Allow tokudb test to pass even if jemalloc is not available.
* [Revision #4293](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4293)\
  Tue 2014-09-23 13:57:29 +0300
  * [MDEV-6743](https://jira.mariadb.org/browse/MDEV-6743) crash in GROUP\_CONCAT(IF () ORDER BY 1)
* [Revision #4292](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4292)\
  Thu 2014-09-18 17:00:44 +0200
  * support statically linked jemalloc. use that for release builds
* [Revision #4291](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4291)\
  Tue 2014-09-16 13:35:28 +0200
  * for mysql-test: fix mysqlhotcopy script to return a predictable exit code
* [Revision #4290](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4290)\
  Mon 2014-09-15 18:55:17 +0200
  * debian: require jemalloc >= 3.0.0, because 2.2.5 (on precise) crashes
* [Revision #4289](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4289)\
  Sat 2014-09-13 21:32:49 +0200
  * ft-index: restore a chunk that was lost in the merge and other fixes for gcc-4.9.1 on sid
* [Revision #4288](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4288)\
  Sat 2014-09-13 08:32:53 +0200
  * tokudb: use thd\_killed() api function, not thd->killed directly
* [Revision #4287](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4287)\
  Sat 2014-09-13 08:16:00 +0200
  * tokudb tests: master-slave.inc should be included _last_
* [Revision #4286](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4286) \[merge]\
  Sat 2014-09-13 00:28:15 +0200
  * tokudb 7.1.8
* [Revision #4285](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4285) \[merge]\
  Fri 2014-09-12 16:51:41 +0200
  * 5.3 merge
  * [Revision #2502.567.238](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.238)\
    Tue 2014-09-09 16:44:54 -0700
    * Fixed bug [MDEV-6292](https://jira.mariadb.org/browse/MDEV-6292). Avoided exponential recursive calls of JOIN\_CACHE::join\_records() in the case of non-nested outer joins. A different solution is required to resolve this performance problem for nested outer joins.
  * [Revision #2502.567.237](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.567.237) \[merge]\
    Mon 2014-08-04 10:05:51 -0700
    * Merge.
    * [Revision #2502.587.1](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/2502.587.1)\
      Thu 2014-07-31 22:17:43 -0700
      * Fixed bug [MDEV-5721](https://jira.mariadb.org/browse/MDEV-5721). Do not define a look-up key for a temporary table if its length exceeds the maximum length of such keys.
* [Revision #4284](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4284)\
  Fri 2014-09-12 08:41:44 +0200
  * [MDEV-6526](https://jira.mariadb.org/browse/MDEV-6526) INFO\_SRC and INFO\_BIN installed wrong
* [Revision #4283](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4283)\
  Fri 2014-09-12 08:41:35 +0200
  * [MDEV-6619](https://jira.mariadb.org/browse/MDEV-6619) SHOW PROCESSLIST returns empty result set after KILL QUERY
* [Revision #4282](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4282)\
  Fri 2014-09-12 08:41:16 +0200
  * [MDEV-6613](https://jira.mariadb.org/browse/MDEV-6613) build system endianness test fails for ppc64le (i.e. Ubuntu)
* [Revision #4281](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4281)\
  Tue 2014-09-09 19:03:05 +0200
  * [MDEV-6561](https://jira.mariadb.org/browse/MDEV-6561) libedit detection is broken
* [Revision #4280](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4280)\
  Mon 2014-09-08 18:38:13 +0200
  * [MDEV-6605](https://jira.mariadb.org/browse/MDEV-6605) Multiple Clients Inserting Causing Error: Failed to read auto-increment value from storage engine
* [Revision #4279](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4279)\
  Mon 2014-09-08 17:10:48 +0200
  * fix compilation on windows - wrong include file
* [Revision #4278](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4278)\
  Sat 2014-09-06 09:59:01 +0200
  * [MDEV-6577](https://jira.mariadb.org/browse/MDEV-6577) auth\_socket.so does not build in kFreeBSD
* [Revision #4277](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4277)\
  Sat 2014-09-06 09:51:34 +0200
  * [MDEV-6595](https://jira.mariadb.org/browse/MDEV-6595) \[PATCH] HPPA: storage/xtradb/os/os0stacktrace.c:88:54: error: invalid operands to binary & (have 'void \*' and 'long unsigned int')
* [Revision #4276](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4276)\
  Wed 2014-09-03 07:37:13 +0300
  * [MDEV-6682](https://jira.mariadb.org/browse/MDEV-6682) innodb.innodb\_simulate\_comp\_failures\_small is too slow if it's run on a real disk
* [Revision #4275](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4275)\
  Sun 2014-08-31 19:55:11 +0200
  * [MDEV-6673](https://jira.mariadb.org/browse/MDEV-6673) I\_S.SESSION\_VARIABLES shows global values
* [Revision #4274](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4274)\
  Fri 2014-08-29 16:14:11 +0400
  * Backport from 10.0:
* [Revision #4273](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4273)\
  Fri 2014-08-29 16:02:46 +0400
  * Backport from 10.0:
* [Revision #4272](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4272)\
  Mon 2014-08-25 16:58:19 +0200
  * [MDEV-6601](https://jira.mariadb.org/browse/MDEV-6601) Assertion \`!thd->in\_active\_multi\_stmt\_transa ction() || thd->in\_multi\_stmt\_transaction\_mode()' failed on executing a stored procedure with commit
* [Revision #4271](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4271)\
  Tue 2014-08-19 19:28:35 +0300
  * [MDEV-6450](https://jira.mariadb.org/browse/MDEV-6450) - MariaDB crash on Power8 when built with advance tool chain
* [Revision #4270](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4270)\
  Wed 2014-08-13 15:46:39 +0200
  * Change a couple of permissions that cause lintian warnings in .deb packaging and don't really hurt to fix.
* [Revision #4269](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4269)\
  Wed 2014-08-13 09:37:12 +0300
  * [MDEV-6546](https://jira.mariadb.org/browse/MDEV-6546): innodb.innodb\_simulate\_comp\_failures\_small fails sporadically
* [Revision #4268](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4268)\
  Tue 2014-08-12 17:12:08 +0200
  * disable still racy tokudb tests
* [Revision #4267](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4267)\
  Tue 2014-08-12 16:39:12 +0200
  * [MDEV-5706](https://jira.mariadb.org/browse/MDEV-5706) MariaDB does not build on hurd-i386
* [Revision #4266](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4266)\
  Tue 2014-08-05 20:22:57 +0200
  * fix tokudb version
* [Revision #4265](https://bazaar.launchpad.net/~maria-captains/maria/5.5/revision/4265)\
  Tue 2014-08-12 19:14:52 +0400
  * Increased the version number

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
