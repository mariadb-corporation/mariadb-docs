# MariaDB 10.2.22 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download](https://downloads.mariadb.org/mariadb/10.2.22/)[Release Notes](../../old-releases/10.2/10.2.22.md)[Changelog](mariadb-10222-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 11 Feb 2019

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.22.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #ca325a46d2](https://github.com/MariaDB/server/commit/ca325a46d2)\
  2019-02-10 00:21:43 +0100
  * CONNECT: update test results
* [Revision #894f44b60b](https://github.com/MariaDB/server/commit/894f44b60b)\
  2019-02-09 22:54:10 +0100
  * CONNECT: Windows paths
* [Revision #e5a5ae45d1](https://github.com/MariaDB/server/commit/e5a5ae45d1)\
  2019-02-08 14:10:44 +0100
  * revert the check changes made in 8f5ea83ff109827748d2f9f5025ed6c6bb91fd80
* [Revision #bc50d72604](https://github.com/MariaDB/server/commit/bc50d72604)\
  2019-02-08 16:38:39 +0100
  * C/C again
* [Revision #0216f87d38](https://github.com/MariaDB/server/commit/0216f87d38)\
  2019-02-08 01:07:19 +0200
  * Updated list of unstable tests for 10.2.22
* [Revision #65f22b8fd4](https://github.com/MariaDB/server/commit/65f22b8fd4)\
  2019-02-07 19:39:23 +0100
  * C/C again
* [Revision #fef9013d43](https://github.com/MariaDB/server/commit/fef9013d43)\
  2019-02-07 18:47:23 +0100
  * update test result
* [Revision #540a1dda7b](https://github.com/MariaDB/server/commit/540a1dda7b)\
  2019-02-07 12:14:49 +0100
  * update C/C to get latest PS fixes
* Merge [Revision #6f4bc21e4a](https://github.com/MariaDB/server/commit/6f4bc21e4a) 2019-02-07 11:18:13 +0200 - Merge pull request #1160 from tempesta-tech/sysprg/10.2-[MDEV-18426](https://jira.mariadb.org/browse/MDEV-18426)
* [Revision #8f5ea83ff1](https://github.com/MariaDB/server/commit/8f5ea83ff1)\
  2019-02-06 14:47:25 +0100
  * [MDEV-18426](https://jira.mariadb.org/browse/MDEV-18426): Most of the mtr tests in the galera\_3nodes suite fail
* [Revision #b3d571c398](https://github.com/MariaDB/server/commit/b3d571c398)\
  2019-02-06 12:27:56 +0100
  * C/C 3.0.9
* [Revision #a4c687c494](https://github.com/MariaDB/server/commit/a4c687c494)\
  2019-02-06 16:53:16 +0400
  * the opt\_constraint\_no\_id should not have the lex\_str type.
* Merge [Revision #e84dc567be](https://github.com/MariaDB/server/commit/e84dc567be) 2019-02-05 17:35:48 +0200 - Merge 10.1 into 10.2
* [Revision #5eb3e4d83c](https://github.com/MariaDB/server/commit/5eb3e4d83c)\
  2019-02-05 17:03:41 +0200
  * [MDEV-15798](https://jira.mariadb.org/browse/MDEV-15798) Mutex leak on accessing INFORMATION\_SCHEMA.INNODB\_MUTEXES
* [Revision #625994b7cc](https://github.com/MariaDB/server/commit/625994b7cc)\
  2019-02-05 11:16:43 +0200
  * [MDEV-16982](https://jira.mariadb.org/browse/MDEV-16982) Server crashes in mem\_heap\_dup upon DELETE from table with virtual columns
* [Revision #f53e795250](https://github.com/MariaDB/server/commit/f53e795250)\
  2019-02-05 11:24:19 +0400
  * [MDEV-17599](https://jira.mariadb.org/browse/MDEV-17599) ALTER TABLE DROP CONSTRAINT does not work for foreign keys.
* [Revision #227379988e](https://github.com/MariaDB/server/commit/227379988e)\
  2019-02-03 20:00:01 +0100
  * [MDEV-16905](https://jira.mariadb.org/browse/MDEV-16905) ASAN heap-use-after-free in `interceptor_strnlen / ... / TABLE::verify_constraints` upon INSERT into temporary table with CHECK constraint
* [Revision #b57ae8b58c](https://github.com/MariaDB/server/commit/b57ae8b58c)\
  2019-02-03 19:56:41 +0100
  * [MDEV-18239](https://jira.mariadb.org/browse/MDEV-18239) ASAN use-after-poison in process\_str\_arg / ... / mark\_unsupported\_func or unexpected ER\_BAD\_FIELD\_ERROR upon ALTER TABLE
* [Revision #db8f0daeb4](https://github.com/MariaDB/server/commit/db8f0daeb4)\
  2019-02-03 18:43:42 +0100
  * CONNECT: calculate table\_name from the path
* [Revision #676f43da3a](https://github.com/MariaDB/server/commit/676f43da3a)\
  2019-02-03 22:37:56 +0100
  * cleanup: don't ---replace\_regex /#sql-.\*/#sql-temporary/
* [Revision #ef4ccb6ce2](https://github.com/MariaDB/server/commit/ef4ccb6ce2)\
  2019-02-03 18:40:27 +0100
  * [MDEV-18083](https://jira.mariadb.org/browse/MDEV-18083) ASAN heap-use-after-free in Field::set\_warning\_truncated\_wrong\_value upon inserting into temporary table
* [Revision #3b7694b7f8](https://github.com/MariaDB/server/commit/3b7694b7f8)\
  2019-02-03 18:38:27 +0100
  * cleanup: don't search for a just-opened tmp table in ALTER
* [Revision #78d5a764b2](https://github.com/MariaDB/server/commit/78d5a764b2)\
  2019-02-03 17:10:31 +0100
  * compiler warnings
* Merge [Revision #1ed1b7794f](https://github.com/MariaDB/server/commit/1ed1b7794f) 2019-02-04 16:09:42 +0100 - Merge remote-tracking branch 'connect/11.2' into 10.2
* [Revision #a0e26599a3](https://github.com/MariaDB/server/commit/a0e26599a3)\
  2019-02-03 15:19:04 +0100
  * Fix [MDEV-13136](https://jira.mariadb.org/browse/MDEV-13136): enhance CREATE SERVER MyServerName FOREIGN DATA WRAPPER to work with CONNECT engine
* [Revision #bece44be4f](https://github.com/MariaDB/server/commit/bece44be4f)\
  2019-01-27 14:21:39 +0100
  * Enable CONNECT tables to have triggers Update version number
* [Revision #bcb8a52295](https://github.com/MariaDB/server/commit/bcb8a52295)\
  2019-01-25 13:02:40 +0100
  * Fix [MDEV-18192](https://jira.mariadb.org/browse/MDEV-18192): CONNECT Engine JDBC not able to issue simple UPDATE statement from trigger or stored procedure
* [Revision #720dedb333](https://github.com/MariaDB/server/commit/720dedb333)\
  2019-01-01 16:57:23 +0100
  * Modified because different result on Windows and Linux
* [Revision #4b3b3bfe56](https://github.com/MariaDB/server/commit/4b3b3bfe56)\
  2019-01-01 16:08:04 +0100
  * Modified because different result on Windows and Linux
* [Revision #4cdeee1e77](https://github.com/MariaDB/server/commit/4cdeee1e77)\
  2019-01-01 14:05:54 +0100
  * Fix a few bug mainly concerning discovery and call from OEM (and prepare new table types)
* [Revision #564f63ccf7](https://github.com/MariaDB/server/commit/564f63ccf7)\
  2019-02-04 16:28:27 +0300
  * [MDEV-18468](https://jira.mariadb.org/browse/MDEV-18468) merge instant\_varchar\_enlarge.test and alter\_varchar\_change.test
* Merge [Revision #a249e57b68](https://github.com/MariaDB/server/commit/a249e57b68) 2019-02-03 17:22:05 +0200 - Merge 10.1 into 10.2
* [Revision #261ce5286f](https://github.com/MariaDB/server/commit/261ce5286f)\
  2019-02-02 10:02:03 +0100
  * [MDEV-18281](https://jira.mariadb.org/browse/MDEV-18281) COM\_RESET\_CONNECTION changes the connection encoding
* [Revision #915ed7e614](https://github.com/MariaDB/server/commit/915ed7e614)\
  2019-02-01 19:19:33 +0200
  * Some more fixes for --suite=galera\_3nodes
* [Revision #dfc9bff5a9](https://github.com/MariaDB/server/commit/dfc9bff5a9)\
  2019-02-01 17:45:15 +0100
  * [MDEV-18379](https://jira.mariadb.org/browse/MDEV-18379): IPv6 compatibility changes/Unification of check for IPv6
* Merge [Revision #081fd8bfa2](https://github.com/MariaDB/server/commit/081fd8bfa2) 2019-02-02 11:40:02 +0200 - Merge 10.1 into 10.2
* [Revision #09cea8703f](https://github.com/MariaDB/server/commit/09cea8703f)\
  2019-02-01 17:10:27 +0400
  * [MDEV-17148](https://jira.mariadb.org/browse/MDEV-17148) DROP DATABASE throw "Directory not empty" after changed lower\_case\_table\_names.
* [Revision #7c7161a1bd](https://github.com/MariaDB/server/commit/7c7161a1bd)\
  2019-01-28 14:38:39 +0530
  * [MDEV-18194](https://jira.mariadb.org/browse/MDEV-18194) Incremental prepare tries to access page which is out of tablespace bounds
* [Revision #a2641b2611](https://github.com/MariaDB/server/commit/a2641b2611)\
  2019-01-29 13:15:59 +0100
  * [MDEV-18380](https://jira.mariadb.org/browse/MDEV-18380) : adjust max\_statement\_time in mariadb-backup
* [Revision #f669cecbe3](https://github.com/MariaDB/server/commit/f669cecbe3)\
  2019-01-31 02:20:51 +0530
  * [MDEV-18415](https://jira.mariadb.org/browse/MDEV-18415) mariadb-backup.[MDEV-14447](https://jira.mariadb.org/browse/MDEV-14447) test case fails with Table 'test.t' doesn't exist in engine
* [Revision #20e19f6975](https://github.com/MariaDB/server/commit/20e19f6975)\
  2019-01-31 22:08:45 +0100
  * [MDEV-17479](https://jira.mariadb.org/browse/MDEV-17479) Assertion \`mysql\_socket.fd != -1' failed in inline\_mysql\_socket\_send on server shutdown
* [Revision #b8aef87221](https://github.com/MariaDB/server/commit/b8aef87221)\
  2019-01-30 15:32:51 +0530
  * [MDEV-16849](https://jira.mariadb.org/browse/MDEV-16849) Extending indexed VARCHAR column should be instantaneous
* Merge [Revision #97930df13c](https://github.com/MariaDB/server/commit/97930df13c) 2019-01-28 12:01:35 +0200 - Merge pull request #1142 from codership/10.2-[MDEV-15740](https://jira.mariadb.org/browse/MDEV-15740)
* [Revision #4ef556955f](https://github.com/MariaDB/server/commit/4ef556955f)\
  2019-01-24 17:42:30 +0200
  * [MDEV-15740](https://jira.mariadb.org/browse/MDEV-15740) Enabled and recorded galera\_gcache\_recover\_manytrx
* [Revision #ddfc789098](https://github.com/MariaDB/server/commit/ddfc789098)\
  2019-01-27 15:44:35 +0200
  * [MDEV-15740](https://jira.mariadb.org/browse/MDEV-15740) Recorded wsrep-recover-v25
* [Revision #4ea128391b](https://github.com/MariaDB/server/commit/4ea128391b)\
  2019-01-24 17:37:45 +0200
  * [MDEV-15740](https://jira.mariadb.org/browse/MDEV-15740) Fix wsrep recovery with wsrep\_emulate\_bin\_log
* [Revision #040b840de7](https://github.com/MariaDB/server/commit/040b840de7)\
  2019-01-24 16:31:33 +0200
  * [MDEV-15740](https://jira.mariadb.org/browse/MDEV-15740) Backport wsrep recovery fixes from 10.4.
* [Revision #ce28fa5303](https://github.com/MariaDB/server/commit/ce28fa5303)\
  2019-01-24 16:01:28 +0200
  * Backported wsrep-recover test from 10.4.
* [Revision #3fb6d2587d](https://github.com/MariaDB/server/commit/3fb6d2587d)\
  2019-01-25 19:26:39 +0100
  * Don't run tests that check privileges in --embedded
* [Revision #d4515d1305](https://github.com/MariaDB/server/commit/d4515d1305)\
  2019-01-25 14:05:54 +0100
  * Deb: don't edit control file from inside rules file
* [Revision #74f184aff2](https://github.com/MariaDB/server/commit/74f184aff2)\
  2019-01-24 20:18:55 +0100
  * Fix tests not to fail with OpenSSL 1.1.1 with TLSv1.3
* [Revision #31d0727a10](https://github.com/MariaDB/server/commit/31d0727a10)\
  2019-01-25 15:23:57 +0200
  * [MDEV-18235](https://jira.mariadb.org/browse/MDEV-18235): Changes related to fsync()
* [Revision #d97db40a9f](https://github.com/MariaDB/server/commit/d97db40a9f)\
  2019-01-25 12:46:23 +0200
  * [MDEV-18352](https://jira.mariadb.org/browse/MDEV-18352) Add a regression test for VARCHAR enlarging
* [Revision #fab531a150](https://github.com/MariaDB/server/commit/fab531a150)\
  2019-01-24 15:57:26 +0200
  * Fix the build after [MDEV-17803](https://jira.mariadb.org/browse/MDEV-17803)
* Merge [Revision #25161e6219](https://github.com/MariaDB/server/commit/25161e6219) 2019-01-24 14:43:29 +0200 - Merge 10.1 into 10.2
* [Revision #7930ab7e33](https://github.com/MariaDB/server/commit/7930ab7e33)\
  2019-01-24 12:36:10 +0200
  * Comment out the statement that triggers [MDEV-18366](https://jira.mariadb.org/browse/MDEV-18366)
* [Revision #46f712c73c](https://github.com/MariaDB/server/commit/46f712c73c)\
  2019-01-24 12:31:54 +0200
  * [MDEV-15114](https://jira.mariadb.org/browse/MDEV-15114): Fix memory leaks
* [Revision #b572814baa](https://github.com/MariaDB/server/commit/b572814baa)\
  2019-01-23 20:56:52 +0200
  * After-merge fix of a result
* Merge [Revision #3dac4e9f0e](https://github.com/MariaDB/server/commit/3dac4e9f0e) 2019-01-23 19:48:19 +0200 - [MDEV-18338](https://jira.mariadb.org/browse/MDEV-18338) Merge new release of InnoDB 5.7.25 to 10.2
* [Revision #d283f80eae](https://github.com/MariaDB/server/commit/d283f80eae)\
  2019-01-22 16:43:59 +0200
  * Update the InnoDB version number
* [Revision #64678ca506](https://github.com/MariaDB/server/commit/64678ca506)\
  2019-01-23 18:09:32 +0200
  * Bug #22990029: Add a test case
* [Revision #aa8a31dadd](https://github.com/MariaDB/server/commit/aa8a31dadd)\
  2018-10-10 18:05:02 +0530
  * Bug #22990029 GCOLS: INCORRECT BEHAVIOR AFTER DATA INSERTED WITH IGNORE KEYWORD
* [Revision #e32305e505](https://github.com/MariaDB/server/commit/e32305e505)\
  2019-01-23 19:45:12 +0200
  * Add a test for Bug #28470805 DELETE CASCADE CRASHES ... ON RESTART
* Merge [Revision #9a7281a703](https://github.com/MariaDB/server/commit/9a7281a703) 2019-01-23 15:09:06 +0200 - Merge 10.1 into 10.2
* [Revision #d06ebd932d](https://github.com/MariaDB/server/commit/d06ebd932d)\
  2019-01-22 06:51:03 +0200
  * Remove references to removed dict\_sys->size
* [Revision #2565c02ca5](https://github.com/MariaDB/server/commit/2565c02ca5)\
  2019-01-22 06:19:21 +0200
  * Remove unnecessary type casts
* [Revision #5c159c9037](https://github.com/MariaDB/server/commit/5c159c9037)\
  2019-01-23 12:00:12 +0000
  * [MDEV-18356](https://jira.mariadb.org/browse/MDEV-18356)\
    Renamed backup-encrypted option introduced in 7158edcba3af3766e9329f9927ce4adfd2a40bf8
* [Revision #9f4d4f404f](https://github.com/MariaDB/server/commit/9f4d4f404f)\
  2019-01-22 18:23:47 +0400
  * [MDEV-12747](https://jira.mariadb.org/browse/MDEV-12747) - main.mysqld\_option\_err fails in buildbot with timeout
* Merge [Revision #37ffdb44ef](https://github.com/MariaDB/server/commit/37ffdb44ef) 2019-01-18 06:51:52 +0200 - Merge 10.1 into 10.2
* [Revision #69221746db](https://github.com/MariaDB/server/commit/69221746db)\
  2019-01-17 23:17:37 +0100
  * [MDEV-18289](https://jira.mariadb.org/browse/MDEV-18289) - Fix a race between thd\_destructor\_proxy() startup and server shutdown.
* Merge [Revision #8e80fd6bfd](https://github.com/MariaDB/server/commit/8e80fd6bfd) 2019-01-17 11:24:38 +0200 - Merge 10.1 into 10.2
* [Revision #f3e9d9a6e6](https://github.com/MariaDB/server/commit/f3e9d9a6e6)\
  2018-10-12 01:43:12 -0700
  * Change information\_schema-big to include innodb
* [Revision #802e8d6b89](https://github.com/MariaDB/server/commit/802e8d6b89)\
  2018-10-07 04:51:46 -0700
  * Backport INFORMATION\_SCHEMA.CHECK\_CONSTRAINTS
* [Revision #2153aaf66e](https://github.com/MariaDB/server/commit/2153aaf66e)\
  2019-01-15 22:47:54 +0100
  * mariadb-backup : use die() macro for fatal exit with error message.
* [Revision #a8a27e65a8](https://github.com/MariaDB/server/commit/a8a27e65a8)\
  2019-01-14 22:28:23 +0100
  * [MDEV-18212](https://jira.mariadb.org/browse/MDEV-18212) mariadb-backup: Make output format uniform whenever possible
* [Revision #61b600079b](https://github.com/MariaDB/server/commit/61b600079b)\
  2019-01-15 09:47:34 +0200
  * [MDEV-16690](https://jira.mariadb.org/browse/MDEV-16690) node hang due to conflicting inserts in FK child table
* [Revision #662217a592](https://github.com/MariaDB/server/commit/662217a592)\
  2019-01-09 16:36:41 +0300
  * [MDEV-18186](https://jira.mariadb.org/browse/MDEV-18186) assertion failure on missing InnoDB index
* [Revision #cbdc2d9489](https://github.com/MariaDB/server/commit/cbdc2d9489)\
  2018-12-27 21:14:07 +0300
  * Replace log\_group\_t::file\_header\_bufs with local array
* [Revision #46046f2e59](https://github.com/MariaDB/server/commit/46046f2e59)\
  2019-01-14 13:20:59 +0200
  * After-merge fix: Disable a failing test
* Merge [Revision #248dc12e60](https://github.com/MariaDB/server/commit/248dc12e60) 2019-01-14 11:37:51 +0200 - Merge 10.1 into 10.2
* [Revision #f5ee7fb31f](https://github.com/MariaDB/server/commit/f5ee7fb31f)\
  2018-11-29 13:38:16 +0100
  * Fix a memory leak in ALTER TABLE
* [Revision #79078167c3](https://github.com/MariaDB/server/commit/79078167c3)\
  2018-12-19 22:30:28 +0530
  * [MDEV-17753](https://jira.mariadb.org/browse/MDEV-17753) ALTER USER fail to replicate
* [Revision #7331c661db](https://github.com/MariaDB/server/commit/7331c661db)\
  2019-01-10 19:35:45 +0100
  * [MDEV-18201](https://jira.mariadb.org/browse/MDEV-18201) : mariadb-backup- fix processing of rename/create sequence in prepare
* [Revision #4a872ae1e7](https://github.com/MariaDB/server/commit/4a872ae1e7)\
  2019-01-09 22:28:31 +0100
  * [MDEV-18185](https://jira.mariadb.org/browse/MDEV-18185) - mariadb-backup - fix specific case of table rename handing in prepare.
* [Revision #9edadc29b1](https://github.com/MariaDB/server/commit/9edadc29b1)\
  2019-01-08 20:41:39 +0530
  * [MDEV-17748](https://jira.mariadb.org/browse/MDEV-17748) innodb.alter\_inplace\_perfschema fails in buildbot with wrong result
* [Revision #0c20b247de](https://github.com/MariaDB/server/commit/0c20b247de)\
  2019-01-04 21:22:41 +0200
  * Disable galera.query\_cache test.
* [Revision #b6b15de85d](https://github.com/MariaDB/server/commit/b6b15de85d)\
  2019-01-04 20:23:13 +0200
  * Disable failing Galera test galera\_query\_cache.
* Merge [Revision #3d8011b375](https://github.com/MariaDB/server/commit/3d8011b375) 2019-01-04 14:47:56 +0200 - Merge pull request #929 from angeloudy/fix-broken-thing
* [Revision #cb85803c45](https://github.com/MariaDB/server/commit/cb85803c45)\
  2019-01-02 15:40:55 +1100
  * Use absolute path for mariadb-backup binary
* [Revision #216d5f7899](https://github.com/MariaDB/server/commit/216d5f7899)\
  2018-11-29 12:36:57 +1100
  * use `ps -p` instead of `ps --pid`
* [Revision #0e794c6a69](https://github.com/MariaDB/server/commit/0e794c6a69)\
  2018-11-15 13:51:09 +1100
  * Make mariadb-backup.sh compatible on FreeBSD
* [Revision #23e4446adc](https://github.com/MariaDB/server/commit/23e4446adc)\
  2019-01-03 22:14:55 +0200
  * Fix a merge error in the parent commit
* Merge [Revision #b7392d142a](https://github.com/MariaDB/server/commit/b7392d142a) 2019-01-03 16:58:05 +0200 - Merge 10.1 into 10.2
* Merge [Revision #842402e4df](https://github.com/MariaDB/server/commit/842402e4df) 2019-01-03 09:57:02 +0100 - Merge branch '10.1' into 10.2
* [Revision #2f368bb967](https://github.com/MariaDB/server/commit/2f368bb967)\
  2019-01-02 19:33:52 +0100
  * fix RHEL8 "ambiguous python shebang" build failures
* [Revision #cf8a564686](https://github.com/MariaDB/server/commit/cf8a564686)\
  2019-01-02 19:29:58 +0100
  * compilation warning on windows
* [Revision #1f9f72b13e](https://github.com/MariaDB/server/commit/1f9f72b13e)\
  2019-01-02 16:34:15 +0100
  * fix debian builds for cosmic
* [Revision #099186d09e](https://github.com/MariaDB/server/commit/099186d09e)\
  2019-01-02 13:42:11 -0500
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
