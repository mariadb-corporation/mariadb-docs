# MariaDB 10.2.42 Changelog

The most recent release of [MariaDB 10.2](../../old-releases/10.2/what-is-mariadb-102.md) is:[**MariaDB 10.2.44**](../../old-releases/10.2/10.2.44.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.2.44/)

[Download 10.2.42](https://mariadb.org/download/?tab=mariadb\&release=10.2.42\&product=mariadb)[Release Notes](../../old-releases/10.2/10.2.42.md)[Changelog](mariadb-10242-changelog.md)[Overview of 10.2](../../old-releases/10.2/what-is-mariadb-102.md)

**Release date:** 9 Feb 2022

For the highlights of this release, see the [release notes](../../old-releases/10.2/10.2.42.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.2)\
you can view more details of the revision and view diffs of the code modified\
in that revision.

* [Revision #e2b50213cf](https://github.com/MariaDB/server/commit/e2b50213cf)\
  2022-01-29 13:56:18 +0100
  * main.events\_embedded test failures in buildbot
* [Revision #8afcda9309](https://github.com/MariaDB/server/commit/8afcda9309)\
  2022-01-29 13:42:38 +0100
  * ASAN/valgrind errors in connect.misc test
* [Revision #5e5feb84b6](https://github.com/MariaDB/server/commit/5e5feb84b6)\
  2022-01-28 16:53:26 +0100
  * [MDEV-11241](https://jira.mariadb.org/browse/MDEV-11241) Certain combining marks cause MariaDB to crash when doing Full-Text searches
* [Revision #a1f630ccfe](https://github.com/MariaDB/server/commit/a1f630ccfe)\
  2022-01-27 21:48:02 +0200
  * Fixed result for embedded server
* [Revision #7045ec27a6](https://github.com/MariaDB/server/commit/7045ec27a6)\
  2022-01-28 13:53:39 +0200
  * Fixed wrong function call in embedded server
* [Revision #24c51be6fe](https://github.com/MariaDB/server/commit/24c51be6fe)\
  2022-01-27 21:44:45 +0200
  * Fixed compilation error if HAVE\_CRYPT is not defined
* [Revision #e99d3da638](https://github.com/MariaDB/server/commit/e99d3da638)\
  2022-01-27 16:04:58 +0200
  * Silence the file-key-management plugin during mysql\_install\_db
* [Revision #5acc79d030](https://github.com/MariaDB/server/commit/5acc79d030)\
  2022-01-27 14:51:16 +0200
  * Remove --upgrade-info option from mysql\_upgrade
* [Revision #93a5fb0025](https://github.com/MariaDB/server/commit/93a5fb0025)\
  2022-01-27 14:43:21 +0200
  * [MDEV-27477](https://jira.mariadb.org/browse/MDEV-27477) Remaining SUSE patches for 10.2+
* [Revision #8d9b1aa0d6](https://github.com/MariaDB/server/commit/8d9b1aa0d6)\
  2022-01-27 13:44:39 +0200
  * [MDEV-27536](https://jira.mariadb.org/browse/MDEV-27536) incremental commit to correct regression test.
* [Revision #2ef12cab42](https://github.com/MariaDB/server/commit/2ef12cab42)\
  2022-01-18 19:56:43 +0200
  * [MDEV-27536](https://jira.mariadb.org/browse/MDEV-27536) invalid BINLOG\_BASE64\_EVENT and assertion Diagnostics\_area:: !is\_set()
* [Revision #8b3b73808d](https://github.com/MariaDB/server/commit/8b3b73808d)\
  2020-05-21 16:19:49 +1000
  * [MDEV-27635](https://jira.mariadb.org/browse/MDEV-27635): selinux: allow read of /proc/sys/kernel/core\_pattern
* [Revision #68b3fa8865](https://github.com/MariaDB/server/commit/68b3fa8865)\
  2021-12-16 20:11:48 +1100
  * [MDEV-27289](https://jira.mariadb.org/browse/MDEV-27289): mtr test for WITH\_SERVER\_EMBEDDED=ON reenable
* [Revision #2e81eab29f](https://github.com/MariaDB/server/commit/2e81eab29f)\
  2022-01-25 13:59:41 +1100
  * [MDEV-27607](https://jira.mariadb.org/browse/MDEV-27607): mysql\_install\_db to install mysql\_upgrade\_info
* [Revision #2cbf92522b](https://github.com/MariaDB/server/commit/2cbf92522b)\
  2022-01-26 12:19:48 +0200
  * Cleanup: Remove an unused parameter of fts\_add\_doc\_by\_id()
* [Revision #7db489fc7d](https://github.com/MariaDB/server/commit/7db489fc7d)\
  2022-01-25 09:14:43 +0100
  * new CC
* [Revision #2925d0f2ee](https://github.com/MariaDB/server/commit/2925d0f2ee)\
  2022-01-25 10:34:13 +0100
  * [MDEV-27612](https://jira.mariadb.org/browse/MDEV-27612) Connect : check buffer sizes, fix string format errors
* [Revision #b9623383cc](https://github.com/MariaDB/server/commit/b9623383cc)\
  2022-01-25 17:31:59 +0700
  * [MDEV-8652](https://jira.mariadb.org/browse/MDEV-8652): Partitioned table creation problem when creating from procedure context twice in same session
* [Revision #8b15d0d4e0](https://github.com/MariaDB/server/commit/8b15d0d4e0)\
  2022-01-24 15:09:31 -0700
  * [MDEV-16091](https://jira.mariadb.org/browse/MDEV-16091): Seconds\_Behind\_Master spikes to millions of seconds
* [Revision #50e66db018](https://github.com/MariaDB/server/commit/50e66db018)\
  2022-01-22 06:59:40 +0400
  * [MDEV-25917](https://jira.mariadb.org/browse/MDEV-25917) create table like fails if source table is partitioned and engine is myisam or aria with data directory.
* Merge [Revision #ebc77c6d17](https://github.com/MariaDB/server/commit/ebc77c6d17) 2022-01-24 17:28:34 +0100 - Merge remote-tracking branch 'connect/10.2' into 10.2
* [Revision #e3b9efb330](https://github.com/MariaDB/server/commit/e3b9efb330)\
  2022-01-06 18:14:21 +0100
  * Fix incompatibility SRCDEF && MEMORY=2 for ODBC JDBC tables
* [Revision #c819a7a71e](https://github.com/MariaDB/server/commit/c819a7a71e)\
  2021-11-26 12:07:23 +0100
  * Fix [MDEV-27055](https://jira.mariadb.org/browse/MDEV-27055) (regression of [MDEV-24493](https://jira.mariadb.org/browse/MDEV-24493))
* [Revision #8acc7fb39c](https://github.com/MariaDB/server/commit/8acc7fb39c)\
  2022-01-09 19:35:43 +0100
  * [MDEV-24088](https://jira.mariadb.org/browse/MDEV-24088) Assertion in InnoDB's FTS code may be triggered by a repeated words fed to simple\_parser plugin
* [Revision #2c16fd9baf](https://github.com/MariaDB/server/commit/2c16fd9baf)\
  2022-01-22 10:17:05 +0200
  * [MDEV-24827](https://jira.mariadb.org/browse/MDEV-24827), [MDEV-20516](https://jira.mariadb.org/browse/MDEV-20516) fixup: Use C90, plug memory leaks
* [Revision #2b6f235ae0](https://github.com/MariaDB/server/commit/2b6f235ae0)\
  2022-01-21 13:02:08 +0200
  * [MDEV-21308](https://jira.mariadb.org/browse/MDEV-21308) : WSREP: binlog ... cache not empty warnings on server with WSREP disabled
* [Revision #f99d141cd2](https://github.com/MariaDB/server/commit/f99d141cd2)\
  2022-01-22 12:46:06 +0700
  * [MDEV-20516](https://jira.mariadb.org/browse/MDEV-20516): Assertion \`!lex->proc\_list.first && !lex->result && !lex->param\_list.elements' failed in mysql\_create\_view
* [Revision #faaecc8fcf](https://github.com/MariaDB/server/commit/faaecc8fcf)\
  2022-01-21 16:51:03 +0300
  * [MDEV-27273](https://jira.mariadb.org/browse/MDEV-27273) Confusing column count in IMPORT TABLESPACE error message
* [Revision #991d5dce32](https://github.com/MariaDB/server/commit/991d5dce32)\
  2021-11-13 16:12:05 +0530
  * Bug#31374305 - FORMAT() NOT DISPLAYING WHOLE NUMBER SIDE CORRECTLY FOR ES\_MX AND ES\_ES LOCALES
* [Revision #4504e6d14e](https://github.com/MariaDB/server/commit/4504e6d14e)\
  2022-01-21 12:40:20 +0100
  * test cases for MySQL bugs
* [Revision #c9beef4315](https://github.com/MariaDB/server/commit/c9beef4315)\
  2022-01-15 17:33:28 +0100
  * don't build with OpenSSL 3.0, it doesn't work before [MDEV-25785](https://jira.mariadb.org/browse/MDEV-25785)
* [Revision #c1d7b4575e](https://github.com/MariaDB/server/commit/c1d7b4575e)\
  2022-01-21 14:43:59 +0200
  * [MDEV-26870](https://jira.mariadb.org/browse/MDEV-26870) --skip-symbolic-links does not disallow .isl file creation
* [Revision #fa7a67ff49](https://github.com/MariaDB/server/commit/fa7a67ff49)\
  2022-01-20 22:52:41 +0300
  * [MDEV-27149](https://jira.mariadb.org/browse/MDEV-27149): Add rocksdb\_ignore\_datadic\_errors
* [Revision #ad88c428c5](https://github.com/MariaDB/server/commit/ad88c428c5)\
  2022-01-20 22:32:55 +0300
  * Avoid a crash on MyRocks data inconsistency.
* [Revision #d3143ef8a8](https://github.com/MariaDB/server/commit/d3143ef8a8)\
  2022-01-11 14:41:37 +0200
  * Improve --help and remove not-free warnings for mysql\_tzinfo\_to\_sql
* [Revision #9d4c0a6cab](https://github.com/MariaDB/server/commit/9d4c0a6cab)\
  2022-01-05 16:37:47 +0200
  * Fixed compiler error in auth\_pam plugin
* [Revision #0fd4d6d3bb](https://github.com/MariaDB/server/commit/0fd4d6d3bb)\
  2022-01-04 20:09:40 +0200
  * [MDEV-27068](https://jira.mariadb.org/browse/MDEV-27068) running mariadb-upgrade in parallel make it hangs forever
* [Revision #d28d3aee10](https://github.com/MariaDB/server/commit/d28d3aee10)\
  2022-01-20 18:39:36 +0700
  * [MDEV-24827](https://jira.mariadb.org/browse/MDEV-24827): Follow-up patch to fix the test main.mysql\_client\_test\_nonblock
* [Revision #474c6df804](https://github.com/MariaDB/server/commit/474c6df804)\
  2022-01-18 13:38:08 +0530
  * [MDEV-27417](https://jira.mariadb.org/browse/MDEV-27417) InnoDB spatial index updates change buffer bitmap page
* [Revision #7dcef65046](https://github.com/MariaDB/server/commit/7dcef65046)\
  2022-01-20 16:25:43 +0700
  * [MDEV-24827](https://jira.mariadb.org/browse/MDEV-24827): Follow-up patch to fix compilation warning
* [Revision #1d27b5789a](https://github.com/MariaDB/server/commit/1d27b5789a)\
  2022-01-20 09:10:44 +1100
  * [MDEV-27544](https://jira.mariadb.org/browse/MDEV-27544) database() function should return 64 characters
* [Revision #810ef9117a](https://github.com/MariaDB/server/commit/810ef9117a)\
  2022-01-19 11:15:22 +0700
  * [MDEV-24827](https://jira.mariadb.org/browse/MDEV-24827): [MariaDB 10.5.5](../../old-releases/10.5/10.5.5.md) crash (sig 11) during a SELECT
* [Revision #9cd6ecfe50](https://github.com/MariaDB/server/commit/9cd6ecfe50)\
  2022-01-17 16:26:47 +0100
  * [MDEV-18284](https://jira.mariadb.org/browse/MDEV-18284): JSON casting using JSON\_COMPACT doesn't always work with values from subqueries
* [Revision #410c4edef3](https://github.com/MariaDB/server/commit/410c4edef3)\
  2022-01-18 13:56:15 +1100
  * [MDEV-27467](https://jira.mariadb.org/browse/MDEV-27467): innodb to enforce the minimum innodb\_buffer\_pool\_size in SET GLOBAL
* [Revision #4db6e86ebe](https://github.com/MariaDB/server/commit/4db6e86ebe)\
  2022-01-18 18:16:10 +0200
  * [MDEV-27539](https://jira.mariadb.org/browse/MDEV-27539) Merge new release of InnoDB 5.7.37 to 10.2
* [Revision #bf9bc99106](https://github.com/MariaDB/server/commit/bf9bc99106)\
  2022-01-18 15:32:01 +0400
  * [MDEV-26129](https://jira.mariadb.org/browse/MDEV-26129) Bad results with join comparing case insensitive VARCHAR/ENUM/SET expression to a \_bin ENUM column
* [Revision #47e18af906](https://github.com/MariaDB/server/commit/47e18af906)\
  2022-01-13 17:27:28 +0100
  * [MDEV-27494](https://jira.mariadb.org/browse/MDEV-27494) Rename .ic files to .inl
* [Revision #746050d02d](https://github.com/MariaDB/server/commit/746050d02d)\
  2022-01-12 20:03:40 +0100
  * [MDEV-27109](https://jira.mariadb.org/browse/MDEV-27109) mysql\_config mariadb\_config lists non existant -lmariadb
* [Revision #b5a14f061b](https://github.com/MariaDB/server/commit/b5a14f061b)\
  2022-01-13 18:14:09 +0100
  * /usr/lib64/pkgconfig is not owned by MariaDB-devel
* [Revision #3548e80bc4](https://github.com/MariaDB/server/commit/3548e80bc4)\
  2022-01-11 00:35:47 +0100
  * [MDEV-4621](https://jira.mariadb.org/browse/MDEV-4621) select returns null for information\_schema.statistics.collation field
* [Revision #a88a4336fc](https://github.com/MariaDB/server/commit/a88a4336fc)\
  2022-01-01 17:19:21 +0100
  * mtr failed to detect when a combination is forced
* [Revision #d7f4fd30f2](https://github.com/MariaDB/server/commit/d7f4fd30f2)\
  2022-01-14 15:53:29 +0200
  * [MDEV-8851](https://jira.mariadb.org/browse/MDEV-8851) innodb.innodb\_information\_schema fails sporadically
* [Revision #a3267c11fa](https://github.com/MariaDB/server/commit/a3267c11fa)\
  2022-01-11 17:46:51 +0100
  * [MDEV-21252](https://jira.mariadb.org/browse/MDEV-21252) ER\_HOST\_IS\_BLOCKED returns packet sequence 1 instead of 0
* [Revision #a38b937bf1](https://github.com/MariaDB/server/commit/a38b937bf1)\
  2022-01-09 09:37:44 +0200
  * [MDEV-25201](https://jira.mariadb.org/browse/MDEV-25201) : Assertion \`thd->wsrep\_trx\_meta.gtid.seqno == (-1)' failed in int wsrep\_to\_isolation\_begin(THD\*, const char\*, const char\*, const TABLE\_LIST\*, Alter\_info\*)
* [Revision #e32c21cb93](https://github.com/MariaDB/server/commit/e32c21cb93)\
  2022-01-07 12:24:19 +0200
  * Changing wsrep\_slave\_threads parameter requires that cluster is connected so moved test here.
* [Revision #ce415be294](https://github.com/MariaDB/server/commit/ce415be294)\
  2022-01-04 12:01:31 +0200
  * [MDEV-25549](https://jira.mariadb.org/browse/MDEV-25549) : Assertion \`_new\_engine' failed in bool check\_engine(THD_, const char\*, const char\*, HA\_CREATE\_INFO\*)
* [Revision #c430f612eb](https://github.com/MariaDB/server/commit/c430f612eb)\
  2022-01-04 08:20:02 +0200
  * [MDEV-25856](https://jira.mariadb.org/browse/MDEV-25856) : SIGSEGV in ha\_myisammrg::append\_create\_info
* [Revision #d0ca241524](https://github.com/MariaDB/server/commit/d0ca241524)\
  2021-12-27 10:22:28 +0200
  * [MDEV-25472](https://jira.mariadb.org/browse/MDEV-25472) : Server crashes when wsrep\_cluster\_address set to unkown address and wsrep\_slave\_threads to 0
* [Revision #89c870b2b4](https://github.com/MariaDB/server/commit/89c870b2b4)\
  2022-01-11 11:50:29 +0700
  * [MDEV-20325](https://jira.mariadb.org/browse/MDEV-20325): Assertion \`\`outer\_context || !\*from\_field || \*from\_field == not\_found\_field' failed in Item\_field::fix\_outer\_field | `!derived->is_excluded()' failed in TABLE_LIST::set_check_materialized | SIGEGV in st_select_lex::mark_as_dependent (optimized builds)`
* [Revision #7692cec5b0](https://github.com/MariaDB/server/commit/7692cec5b0)\
  2022-01-06 00:31:42 -0800
  * [MDEV-25631](https://jira.mariadb.org/browse/MDEV-25631) Crash executing query with VIEW, aggregate and subquery
* [Revision #6dec0332fb](https://github.com/MariaDB/server/commit/6dec0332fb)\
  2022-01-05 22:36:20 -0800
  * [MDEV-25086](https://jira.mariadb.org/browse/MDEV-25086) Stored Procedure Crashes Server
* [Revision #d6ee351bbb](https://github.com/MariaDB/server/commit/d6ee351bbb)\
  2022-01-05 20:23:52 -0800
  * Revert "[MDEV-24454](https://jira.mariadb.org/browse/MDEV-24454) Crash at change\_item\_tree"
* [Revision #80d33261ea](https://github.com/MariaDB/server/commit/80d33261ea)\
  2022-01-09 12:39:15 +0100
  * Windows, appveyor - use VS2022
* [Revision #555a53f10d](https://github.com/MariaDB/server/commit/555a53f10d)\
  2018-09-08 16:18:42 +0100
  * Windows : fix broken build with OpenSSL
* [Revision #3fb3acf58e](https://github.com/MariaDB/server/commit/3fb3acf58e)\
  2022-01-08 23:16:19 +0100
  * Windows, appveyor - use Cygwin's bison again
* [Revision #8d8af31ab0](https://github.com/MariaDB/server/commit/8d8af31ab0)\
  2022-01-07 20:19:45 +0100
  * Windows, CI - workaround hardcoded limits for mtr --parallel=auto
* [Revision #d821feddac](https://github.com/MariaDB/server/commit/d821feddac)\
  2022-01-07 13:51:07 +0100
  * [MDEV-14938](https://jira.mariadb.org/browse/MDEV-14938) make buildbot to include galera into bintars
* [Revision #28a4836e2b](https://github.com/MariaDB/server/commit/28a4836e2b)\
  2022-01-07 11:13:34 +0100
  * Windows, CI : run mtr in buildbot\_suites.bat with --parallel=auto
* [Revision #96de6bfd5e](https://github.com/MariaDB/server/commit/96de6bfd5e)\
  2021-12-27 11:53:14 -0700
  * [MDEV-16091](https://jira.mariadb.org/browse/MDEV-16091): Seconds\_Behind\_Master spikes to millions of seconds
* [Revision #452c9a4d72](https://github.com/MariaDB/server/commit/452c9a4d72)\
  2021-12-24 14:00:47 +0530
  * [MDEV-26698](https://jira.mariadb.org/browse/MDEV-26698): Incorrect row number upon INSERT .. SELECT from the same table: rows are counted twice
* [Revision #5d57e04b27](https://github.com/MariaDB/server/commit/5d57e04b27)\
  2021-12-30 16:45:37 +1100
  * [MDEV-27386](https://jira.mariadb.org/browse/MDEV-27386): cpack rpm libsepol installed detects verison incorrectly
* [Revision #546520042f](https://github.com/MariaDB/server/commit/546520042f)\
  2021-12-29 23:04:13 +0400
  * [MDEV-22256](https://jira.mariadb.org/browse/MDEV-22256) Assertion \`length == pack\_length()' failed in Field\_timestamp\_with\_dec::sort\_string
* [Revision #189bf300ca](https://github.com/MariaDB/server/commit/189bf300ca)\
  2021-12-29 14:54:34 +0400
  * [MDEV-21639](https://jira.mariadb.org/browse/MDEV-21639) DEFAULT(col) evaluates to a bad value in WHERE clause
* [Revision #fad1d15326](https://github.com/MariaDB/server/commit/fad1d15326)\
  2021-12-15 13:59:38 +0530
  * [MDEV-25460](https://jira.mariadb.org/browse/MDEV-25460): Assertion \`\`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())' failed in Diagnostics\_area::set\_ok\_status in my\_ok from mysql\_sql\_stmt\_prepare\`
* [Revision #4daf9d7c3e](https://github.com/MariaDB/server/commit/4daf9d7c3e)\
  2021-12-27 14:47:47 +0100
  * [MDEV-27364](https://jira.mariadb.org/browse/MDEV-27364) Build from 10.2-10.4 srpm fails on RHEL8 family due to discrepancy in jemalloc requirements
* [Revision #42fea34d4a](https://github.com/MariaDB/server/commit/42fea34d4a)\
  2021-12-20 19:55:00 -0800
  * [MDEV-27262](https://jira.mariadb.org/browse/MDEV-27262) Unexpected index intersection with full index scan for an index
* [Revision #b5cbe50604](https://github.com/MariaDB/server/commit/b5cbe50604)\
  2021-12-23 14:19:45 +0100
  * [MDEV-24097](https://jira.mariadb.org/browse/MDEV-24097): galera\[\_3nodes] suite tests in MTR sporadically fails
* [Revision #12087d6757](https://github.com/MariaDB/server/commit/12087d6757)\
  2021-12-22 01:05:18 +0100
  * [MDEV-23175](https://jira.mariadb.org/browse/MDEV-23175): my\_timer\_milliseconds clock\_gettime for multiple platfomrs
* [Revision #85defc4764](https://github.com/MariaDB/server/commit/85defc4764)\
  2021-12-17 04:44:43 +0100
  * [MDEV-27181](https://jira.mariadb.org/browse/MDEV-27181) fixup: compatibility with Windows + small corrections
* [Revision #fff8ac2e96](https://github.com/MariaDB/server/commit/fff8ac2e96)\
  2021-11-08 15:22:06 +0700
  * [MDEV-21866](https://jira.mariadb.org/browse/MDEV-21866): Assertion \`!result' failed in convert\_const\_to\_int upon 2nd execution of PS
* [Revision #136bcfdf75](https://github.com/MariaDB/server/commit/136bcfdf75)\
  2021-12-15 15:12:06 +0300
  * [MDEV-27270](https://jira.mariadb.org/browse/MDEV-27270): Wrong query plan with Range Checked for Each Record and ORDER BY ... LIMIT
* [Revision #f1ca949f2b](https://github.com/MariaDB/server/commit/f1ca949f2b)\
  2021-12-15 13:16:29 +0200
  * Disable following tests from galera\_3nodes suite
* [Revision #ef9517eb81](https://github.com/MariaDB/server/commit/ef9517eb81)\
  2021-12-15 14:17:55 +0200
  * [MDEV-27268](https://jira.mariadb.org/browse/MDEV-27268) Failed InnoDB initialization leaves garbage files behind
* [Revision #8bb5563369](https://github.com/MariaDB/server/commit/8bb5563369)\
  2021-12-13 02:15:57 +0100
  * [MDEV-27181](https://jira.mariadb.org/browse/MDEV-27181): Galera SST scripts should use ssl\_capath for CA directory
* [Revision #6b066ec332](https://github.com/MariaDB/server/commit/6b066ec332)\
  2021-12-13 08:04:45 +0200
  * [MDEV-27235](https://jira.mariadb.org/browse/MDEV-27235): Crash on SET GLOBAL innodb\_encrypt\_tables
* [Revision #0745db7179](https://github.com/MariaDB/server/commit/0745db7179)\
  2021-12-09 19:14:17 +0100
  * don't use buffered\_option\_error\_reporter without perfschema
* [Revision #eafa2a1411](https://github.com/MariaDB/server/commit/eafa2a1411)\
  2021-12-09 16:29:22 +0100
  * enable partition\_open\_files\_limit test
* [Revision #f974062c51](https://github.com/MariaDB/server/commit/f974062c51)\
  2021-12-07 19:34:31 +0200
  * [MDEV-19129](https://jira.mariadb.org/browse/MDEV-19129): Fixed configure for Xcode, CMake generate
* [Revision #f13c2107b3](https://github.com/MariaDB/server/commit/f13c2107b3)\
  2021-12-07 17:46:29 +0100
  * Don't beep in mysql\_upgrade\_service.exe
* [Revision #8dd1f01d09](https://github.com/MariaDB/server/commit/8dd1f01d09)\
  2021-12-07 17:42:47 +0100
  * [MDEV-27191](https://jira.mariadb.org/browse/MDEV-27191) MariaDB client - "system" command does not work on Windows
* [Revision #d5ceddb391](https://github.com/MariaDB/server/commit/d5ceddb391)\
  2021-12-07 01:28:51 +0100
  * Appveyor - cache chocolatey packages
* [Revision #71027eceac](https://github.com/MariaDB/server/commit/71027eceac)\
  2021-11-29 17:02:31 +0100
  * fix srpm builds after fe065f8d90b0
* [Revision #214cad8c3b](https://github.com/MariaDB/server/commit/214cad8c3b)\
  2021-11-29 17:03:21 +0100
  * fix ./mtr --manual warning after f5441ef4dac9
* [Revision #17802165a6](https://github.com/MariaDB/server/commit/17802165a6)\
  2021-11-24 18:46:46 +1100
  * [MDEV-27088](https://jira.mariadb.org/browse/MDEV-27088): lf unit tests - cycles insufficient
* [Revision #4e0dcf1083](https://github.com/MariaDB/server/commit/4e0dcf1083)\
  2021-11-20 14:22:25 +1100
  * [MDEV-27088](https://jira.mariadb.org/browse/MDEV-27088): Server crash on ARM (WMM architecture) due to missing barriers in lf-hash
* [Revision #ac963142ee](https://github.com/MariaDB/server/commit/ac963142ee)\
  2021-11-24 23:19:22 -0800
  * [MDEV-26553](https://jira.mariadb.org/browse/MDEV-26553) NOT IN subquery construct crashing 10.1 and up
* [Revision #f5441ef4da](https://github.com/MariaDB/server/commit/f5441ef4da)\
  2021-11-26 17:15:41 +0100
  * [MDEV-26972](https://jira.mariadb.org/browse/MDEV-26972) MTR worker aborts after server restart failure
* [Revision #a96b428269](https://github.com/MariaDB/server/commit/a96b428269)\
  2021-11-03 15:34:28 +0100
  * [MDEV-26755](https://jira.mariadb.org/browse/MDEV-26755) innodb.undo\_truncate: ilink::assert\_linked(): Assertion \`prev != 0 && next != 0' failed
* [Revision #4ba7478553](https://github.com/MariaDB/server/commit/4ba7478553)\
  2019-08-12 19:29:06 +0200
  * add a test case
* [Revision #f809a4fbd0](https://github.com/MariaDB/server/commit/f809a4fbd0)\
  2021-11-10 18:35:17 +0800
  * [MDEV-26558](https://jira.mariadb.org/browse/MDEV-26558) Fix a deadlock due to cyclic dependence
* [Revision #ef179dadf4](https://github.com/MariaDB/server/commit/ef179dadf4)\
  2021-11-24 17:19:52 +1100
  * mysql\_install\_db: remove MySQL references
* [Revision #749d8dedc3](https://github.com/MariaDB/server/commit/749d8dedc3)\
  2021-11-17 17:14:27 +1100
  * [MDEV-27066](https://jira.mariadb.org/browse/MDEV-27066): Fixed scientific notation parsing bug
* [Revision #fe065f8d90](https://github.com/MariaDB/server/commit/fe065f8d90)\
  2021-11-22 19:34:47 +0700
  * [MDEV-22522](https://jira.mariadb.org/browse/MDEV-22522) RPM packages have meaningless summary/description
* [Revision #2f51511c08](https://github.com/MariaDB/server/commit/2f51511c08)\
  2021-11-16 07:32:14 +0100
  * [MDEV-26915](https://jira.mariadb.org/browse/MDEV-26915): SST scripts do not take log\_bin\_index setting into account
* [Revision #b952599786](https://github.com/MariaDB/server/commit/b952599786)\
  2021-11-16 05:21:18 +0100
  * [MDEV-26064](https://jira.mariadb.org/browse/MDEV-26064): mariadb-backup SST fails when starting with --innodb-force-recovery
* [Revision #114e18b8b6](https://github.com/MariaDB/server/commit/114e18b8b6)\
  2021-11-20 21:35:54 -0800
  * [MDEV-26470](https://jira.mariadb.org/browse/MDEV-26470) "No database" selected when using CTE in a subquery of DELETE statement
* [Revision #0dae41637a](https://github.com/MariaDB/server/commit/0dae41637a)\
  2021-11-19 14:51:12 -0800
  * [MDEV-27086](https://jira.mariadb.org/browse/MDEV-27086) "No database selected" when using UNION of CTEs to define table
* [Revision #e9f171b4fe](https://github.com/MariaDB/server/commit/e9f171b4fe)\
  2021-11-20 21:49:25 +0400
  * [MDEV-27098](https://jira.mariadb.org/browse/MDEV-27098) Subquery using the ALL keyword on TIME columns produces a wrong result
* [Revision #7efcc2794d](https://github.com/MariaDB/server/commit/7efcc2794d)\
  2021-11-20 16:11:08 +0400
  * [MDEV-27072](https://jira.mariadb.org/browse/MDEV-27072) Subquery using the ALL keyword on date columns produces a wrong result
* [Revision #81d7adb1e2](https://github.com/MariaDB/server/commit/81d7adb1e2)\
  2021-11-18 00:51:17 +0100
  * [MDEV-27075](https://jira.mariadb.org/browse/MDEV-27075) mysql\_upgrade\_service.exe - using uninitialized memory 'defaults\_file'
* [Revision #ed0a224b3d](https://github.com/MariaDB/server/commit/ed0a224b3d)\
  2021-11-01 23:51:58 +0600
  * [MDEV-26747](https://jira.mariadb.org/browse/MDEV-26747) improve corruption check for encrypted tables on ALTER IMPORT
* [Revision #8f24f5fee2](https://github.com/MariaDB/server/commit/8f24f5fee2)\
  2021-11-15 22:21:05 -0800
  * [MDEV-26825](https://jira.mariadb.org/browse/MDEV-26825) Bogus error for query with two usage of CTE referring another CTE
* [Revision #c5e09bf81a](https://github.com/MariaDB/server/commit/c5e09bf81a)\
  2021-11-16 00:18:12 +0100
  * [MDEV-27056](https://jira.mariadb.org/browse/MDEV-27056) Windows upgrade\_wizard - CloseHandle() on invalid (already closed) pipe handle
* [Revision #9e9e91b3c2](https://github.com/MariaDB/server/commit/9e9e91b3c2)\
  2021-11-16 00:08:48 +0100
  * Windows build - fix signtool search path to take modern SDKs into account
* [Revision #628c281db6](https://github.com/MariaDB/server/commit/628c281db6)\
  2021-11-11 22:12:12 +0100
  * [MDEV-27030](https://jira.mariadb.org/browse/MDEV-27030) vcol.vcol\_keys\_myisam fails on Windows x64, with Visual Studio 2022
* [Revision #3163d9e60c](https://github.com/MariaDB/server/commit/3163d9e60c)\
  2021-11-11 06:19:19 -0700
  * [MDEV-26991](https://jira.mariadb.org/browse/MDEV-26991): CURRENT\_TEST: main.mysql\_binary\_zero\_insert 'grep' is not recognized as an internal or external command, operable program or batch file.
* [Revision #d6d1a1fc21](https://github.com/MariaDB/server/commit/d6d1a1fc21)\
  2021-11-09 08:23:25 +0200
  * Remove a warning for clang 11 or earlier
* [Revision #8c7e551da1](https://github.com/MariaDB/server/commit/8c7e551da1)\
  2021-11-09 08:08:29 +0200
  * Remove restarts from encrypt\_and\_grep test
* Merge [Revision #75f0c595d9](https://github.com/MariaDB/server/commit/75f0c595d9) 2021-11-09 08:07:58 +0200 - Merge mariadb-10.2.41 into 10.2
* [Revision #7c30bc38a5](https://github.com/MariaDB/server/commit/7c30bc38a5)\
  2021-10-27 09:42:45 +1100
  * [MDEV-26561](https://jira.mariadb.org/browse/MDEV-26561) mariadb-backup release locks
* [Revision #e1eb39a446](https://github.com/MariaDB/server/commit/e1eb39a446)\
  2021-10-26 18:48:44 +0800
  * [MDEV-26561](https://jira.mariadb.org/browse/MDEV-26561) Fix a bug due to unreleased lock
* [Revision #8b6dfc3c02](https://github.com/MariaDB/server/commit/8b6dfc3c02)\
  2021-11-08 11:26:47 -0500
  * bump the VERSION
* [Revision #2a3dae115b](https://github.com/MariaDB/server/commit/2a3dae115b)\
  2021-10-23 22:38:13 +0700
  * [MDEV-22522](https://jira.mariadb.org/browse/MDEV-22522) RPM packages have meaningless summary/description
* [Revision #9dc05f1f11](https://github.com/MariaDB/server/commit/9dc05f1f11)\
  2021-11-05 16:27:08 +0400
  * [MDEV-25610](https://jira.mariadb.org/browse/MDEV-25610) Assertion \`escape != -1' failed in Item\_func\_like::val\_int
* [Revision #322fc4f4b3](https://github.com/MariaDB/server/commit/322fc4f4b3)\
  2021-11-03 18:23:16 +0100
  * appveyor - do not use buggy cygwin bison.
* [Revision #2df99f2193](https://github.com/MariaDB/server/commit/2df99f2193)\
  2021-11-03 18:14:02 +0200
  * Revert "[MDEV-19129](https://jira.mariadb.org/browse/MDEV-19129): Xcode compatibility update: deprecated vfork -> fork"
* [Revision #8ce5635a3e](https://github.com/MariaDB/server/commit/8ce5635a3e)\
  2021-11-02 11:26:35 +0300
  * [MDEV-22284](https://jira.mariadb.org/browse/MDEV-22284) Aria table key read crash because wrong index used
* [Revision #d0b611a76d](https://github.com/MariaDB/server/commit/d0b611a76d)\
  2021-11-02 09:00:49 +0400
  * [MDEV-24335](https://jira.mariadb.org/browse/MDEV-24335) Unexpected question mark in the end of a TINYTEXT column
* [Revision #026984c360](https://github.com/MariaDB/server/commit/026984c360)\
  2021-11-01 09:28:41 +0200
  * [MDEV-26949](https://jira.mariadb.org/browse/MDEV-26949) --debug-gdb installs redundant signal handlers
* [Revision #0c77c5f6e7](https://github.com/MariaDB/server/commit/0c77c5f6e7)\
  2021-10-29 13:32:32 +0300
  * [MDEV-19129](https://jira.mariadb.org/browse/MDEV-19129): Xcode compatibility update: #include \<editline/readline.h> path
* [Revision #5d6f3cebca](https://github.com/MariaDB/server/commit/5d6f3cebca)\
  2021-10-29 21:01:28 +0300
  * [MDEV-19129](https://jira.mariadb.org/browse/MDEV-19129): Xcode compatibility update: deprecated vfork -> fork
* [Revision #059797ed44](https://github.com/MariaDB/server/commit/059797ed44)\
  2021-10-29 12:24:47 +0400
  * [MDEV-24901](https://jira.mariadb.org/browse/MDEV-24901) SIGSEGV in fts\_get\_table\_name, SIGSEGV in ib\_vector\_size, SIGSEGV in row\_merge\_fts\_doc\_tokenize, stack smashing
* [Revision #4e5cf34819](https://github.com/MariaDB/server/commit/4e5cf34819)\
  2021-10-27 17:50:12 +0200
  * rpl\_get\_master\_version\_and\_clock and rpl\_row\_big\_table\_id tests are slow, so let's not run them under valgrind

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
