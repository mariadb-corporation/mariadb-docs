# MariaDB 10.4.7 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.7/)[Release Notes](../../old-releases/10.4/10.4.7.md)[Changelog](mariadb-1047-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 31 Jul 2019

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.7.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.3.17](../changelogs-mariadb-10-3-series/mariadb-10317-changelog.md)
* [Revision #9a78a283f4](https://github.com/MariaDB/server/commit/9a78a283f4)\
  2019-07-30 14:28:46 +0300
  * List of unstable tests for 10.4.7 release (updated)
* [Revision #6dfa085fd5](https://github.com/MariaDB/server/commit/6dfa085fd5)\
  2019-07-30 06:16:48 +0900
  * [MDEV-20179](https://jira.mariadb.org/browse/MDEV-20179) Server hangs on shutdown during installation of Spider (#1368)
* [Revision #7221b9ef52](https://github.com/MariaDB/server/commit/7221b9ef52)\
  2019-07-30 01:30:14 +0900
  * [MDEV-20179](https://jira.mariadb.org/browse/MDEV-20179) Server hangs on shutdown during installation of Spider (#1367)
* [Revision #ccaaa3d200](https://github.com/MariaDB/server/commit/ccaaa3d200)\
  2019-07-29 16:44:39 +0200
  * [MDEV-20200](https://jira.mariadb.org/browse/MDEV-20200): AddressSanitizer: use-after-poison in Item\_direct\_view\_ref::get\_null\_ref\_table
* [Revision #83d368a062](https://github.com/MariaDB/server/commit/83d368a062)\
  2019-07-29 21:18:51 +0900
  * [MDEV-20179](https://jira.mariadb.org/browse/MDEV-20179) Server hangs on shutdown during installation of Spider (#1366)
* [Revision #67177cd2c8](https://github.com/MariaDB/server/commit/67177cd2c8)\
  2019-07-26 02:55:28 +0200
  * Fix for MW-336 test
* [Revision #1c27eb7ebd](https://github.com/MariaDB/server/commit/1c27eb7ebd)\
  2019-07-01 00:43:26 +0200
  * Do not compile socket IO code in WolfSSL
* [Revision #f61a980686](https://github.com/MariaDB/server/commit/f61a980686)\
  2019-07-26 17:01:36 +0200
  * Update WolfSSL, remove older workarounds.
* Merge [Revision #2792c6e7b0](https://github.com/MariaDB/server/commit/2792c6e7b0) 2019-07-28 13:43:26 +0200 - Merge branch '10.3' into 10.4
* Merge [Revision #c0743e4b00](https://github.com/MariaDB/server/commit/c0743e4b00) 2019-07-26 18:31:48 +0300 - Merge 10.3 into 10.4
* Merge [Revision #4c7a743964](https://github.com/MariaDB/server/commit/4c7a743964) 2019-07-26 15:22:31 +0300 - Merge 10.3 into 10.4
* [Revision #de9e393094](https://github.com/MariaDB/server/commit/de9e393094)\
  2019-07-26 12:03:23 +0200
  * [MDEV-20108](https://jira.mariadb.org/browse/MDEV-20108): \[ERROR] mysqld got signal 11 in st\_select\_lex::add\_table\_to\_list
* Merge [Revision #e9c1701e11](https://github.com/MariaDB/server/commit/e9c1701e11) 2019-07-25 18:42:06 +0300 - Merge 10.3 into 10.4
* [Revision #17794fb9aa](https://github.com/MariaDB/server/commit/17794fb9aa)\
  2019-07-25 03:10:18 +0300
  * List of unstable tests for 10.4.7 release
* [Revision #11f3e23662](https://github.com/MariaDB/server/commit/11f3e23662)\
  2019-07-10 10:48:26 +0200
  * [MDEV-19876](https://jira.mariadb.org/browse/MDEV-19876) pam v2: auth\_pam\_tool\_dir and auth\_pam\_tool permissions are wrong in RPMs
* [Revision #c9f0f88838](https://github.com/MariaDB/server/commit/c9f0f88838)\
  2019-07-08 12:32:17 +0200
  * [MDEV-19822](https://jira.mariadb.org/browse/MDEV-19822) [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) install fails on Ubuntu 18.04 if Prometheus mysqld\_exporter is running
* [Revision #bccd9d0e3a](https://github.com/MariaDB/server/commit/bccd9d0e3a)\
  2019-07-24 13:20:36 +0200
  * [MDEV-20108](https://jira.mariadb.org/browse/MDEV-20108): \[ERROR] mysqld got signal 11 in st\_select\_lex::add\_table\_to\_list
* [Revision #819c40d694](https://github.com/MariaDB/server/commit/819c40d694)\
  2019-07-22 14:34:12 +0100\
  \*
  * wsrep-lib update (SR cleanups and voting support) (#1359)
* [Revision #1f54b662ae](https://github.com/MariaDB/server/commit/1f54b662ae)\
  2019-07-22 12:24:01 +0200
  * The test for the wsrep\_info plugin needs the same flexible wsrep version checking as the tests for Galera (continuation of [MDEV-18565](https://jira.mariadb.org/browse/MDEV-18565) task)
* [Revision #09e9f884f1](https://github.com/MariaDB/server/commit/09e9f884f1)\
  2019-07-19 18:13:36 +0300
  * [MDEV-20048](https://jira.mariadb.org/browse/MDEV-20048) Assertion 'n < tuple->n\_fields on ROLLBACK after DROP COLUMN
* [Revision #90600e8fc5](https://github.com/MariaDB/server/commit/90600e8fc5)\
  2019-07-18 14:42:21 +0200
  * Fixed dependency checking in some Galera tests + remove duplicates
* [Revision #4733464975](https://github.com/MariaDB/server/commit/4733464975)\
  2019-07-18 15:32:22 +0300
  * Fixed that mariadb-

## binaries reads their corresponding entry from my.cnf

* [Revision #5a95a33e30](https://github.com/MariaDB/server/commit/5a95a33e30)\
  2019-07-18 11:39:57 +0200
  * Set the garbd\_exe variable to empty string to avoid warning about an uninitialized variable when wsrep\_provider is not initialized correctly, set to 'none' or when wsrep is switched off
* [Revision #f5390eea9a](https://github.com/MariaDB/server/commit/f5390eea9a)\
  2019-07-16 12:48:04 +0200
  * [MDEV-18565](https://jira.mariadb.org/browse/MDEV-18565): Galera mtr-suite fails if galera library is not installed
* [Revision #ee3ef790ca](https://github.com/MariaDB/server/commit/ee3ef790ca)\
  2019-07-16 09:21:26 +0300
  * [MDEV-19970](https://jira.mariadb.org/browse/MDEV-19970) Galera test failure on galera\_sr.galera-features#56
* [Revision #5244813114](https://github.com/MariaDB/server/commit/5244813114)\
  2019-07-16 07:54:57 +0300
  * [MDEV-19968](https://jira.mariadb.org/browse/MDEV-19968): Galera test failure on galera\_load\_data
* [Revision #61cc932781](https://github.com/MariaDB/server/commit/61cc932781)\
  2019-07-15 12:06:24 +0300
  * Wsrep crash caused by COM\_CHANGE\_USER, COM\_RESET\_CONNECTION (#1358)
* [Revision #a0230bc76d](https://github.com/MariaDB/server/commit/a0230bc76d)\
  2019-07-10 21:15:12 +0300
  * [MDEV-18266](https://jira.mariadb.org/browse/MDEV-18266) Changing an index comment unnecessarily rebuilds index
* [Revision #70c2bde931](https://github.com/MariaDB/server/commit/70c2bde931)\
  2019-07-09 15:10:45 +0400
  * [MDEV-19996](https://jira.mariadb.org/browse/MDEV-19996) Bison grammar: turn singe-character operators into
* [Revision #6974962945](https://github.com/MariaDB/server/commit/6974962945)\
  2019-06-25 10:53:33 +0300
  * [MDEV-16222](https://jira.mariadb.org/browse/MDEV-16222) Assertion \`0' failed in row\_purge\_remove\_sec\_if\_poss\_leaf on table with virtual columns and indexes
* [Revision #af5b0dbab6](https://github.com/MariaDB/server/commit/af5b0dbab6)\
  2019-05-27 23:29:43 +0300
  * [MDEV-19175](https://jira.mariadb.org/browse/MDEV-19175) Server crashes in ha\_partition::vers\_can\_native upon INSERT DELAYED into versioned partitioned table
* [Revision #c7f818928d](https://github.com/MariaDB/server/commit/c7f818928d)\
  2019-06-25 18:26:09 +0300
  * Tests: versioning suite fix when no test\_versioning plugin
* [Revision #1bb57e59a1](https://github.com/MariaDB/server/commit/1bb57e59a1)\
  2019-06-17 11:44:53 +0300
  * [MDEV-19785](https://jira.mariadb.org/browse/MDEV-19785) Storage CONNECT compilation error: unknown type name 'UNZFAM'
* [Revision #9d6b601e79](https://github.com/MariaDB/server/commit/9d6b601e79)\
  2019-07-06 23:54:53 +0900
  * [MDEV-19866](https://jira.mariadb.org/browse/MDEV-19866) With a Spider table, a SELECT with WHERE involving primary key breaks following SELECTs (#1356)
* [Revision #fa7051c419](https://github.com/MariaDB/server/commit/fa7051c419)\
  2019-07-06 23:52:53 +0900
  * [MDEV-19842](https://jira.mariadb.org/browse/MDEV-19842) Crash while creating statistics for Spider table (#1355)
* [Revision #4a739d7650](https://github.com/MariaDB/server/commit/4a739d7650)\
  2019-07-06 22:38:43 +0900
  * [MDEV-16248](https://jira.mariadb.org/browse/MDEV-16248) Row based replication to spider with float column fails on delete/update (#1354)
* [Revision #fb3998c351](https://github.com/MariaDB/server/commit/fb3998c351)\
  2019-07-05 18:27:44 +0300
  * fix build
* [Revision #c6dff51276](https://github.com/MariaDB/server/commit/c6dff51276)\
  2019-07-05 17:11:54 +0200
  * Workaround for [1221](https://github.com/systemd/systemd/issues/1221)
* [Revision #c9aa495fb6](https://github.com/MariaDB/server/commit/c9aa495fb6)\
  2019-07-04 21:31:35 +0300
  * [MDEV-19955](https://jira.mariadb.org/browse/MDEV-19955) make argument of handler::ha\_write\_row() const
* [Revision #23c12ed5cb](https://github.com/MariaDB/server/commit/23c12ed5cb)\
  2019-07-04 12:06:48 +0300
  * [MDEV-19951](https://jira.mariadb.org/browse/MDEV-19951) use override keyword across the InnoDB
* [Revision #e8392e58b2](https://github.com/MariaDB/server/commit/e8392e58b2)\
  2019-07-01 13:21:07 +0300
  * [MDEV-19696](https://jira.mariadb.org/browse/MDEV-19696) - Cleanup gcc sync builtins
* [Revision #3acf741051](https://github.com/MariaDB/server/commit/3acf741051)\
  2019-07-02 21:23:47 +0200
  * fix suite.pm to not garble $\_
* Merge [Revision #7a3d34d645](https://github.com/MariaDB/server/commit/7a3d34d645) 2019-07-02 21:44:58 +0300 - Merge 10.3 into 10.4
* [Revision #faeaf978b8](https://github.com/MariaDB/server/commit/faeaf978b8)\
  2019-07-02 20:16:35 +0200
  * fix suite.pm for windows
* [Revision #6842a1538a](https://github.com/MariaDB/server/commit/6842a1538a)\
  2019-07-01 22:07:32 +0800
  * Fix github urls of submodules
* [Revision #4fef644303](https://github.com/MariaDB/server/commit/4fef644303)\
  2019-07-01 23:45:01 +0200
  * cleanup: mtr and plugins
* [Revision #d84792b689](https://github.com/MariaDB/server/commit/d84792b689)\
  2019-07-01 23:03:16 +0200
  * Skip pam tests unless $USER owns auth\_pam\_tool\_dir
* [Revision #4f87ad1975](https://github.com/MariaDB/server/commit/4f87ad1975)\
  2019-06-30 21:29:38 +0200
  * [MDEV-19879](https://jira.mariadb.org/browse/MDEV-19879) server can send empty error message to client with pam\_use\_cleartext\_plugin
* [Revision #3914a792d8](https://github.com/MariaDB/server/commit/3914a792d8)\
  2019-06-30 17:18:26 +0200
  * [MDEV-19880](https://jira.mariadb.org/browse/MDEV-19880) pam v1: pam password authentication doesn't work at all in [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/)
* [Revision #dd93028dae](https://github.com/MariaDB/server/commit/dd93028dae)\
  2019-06-30 20:41:26 +0200
  * [MDEV-19878](https://jira.mariadb.org/browse/MDEV-19878) pam v2: pam password authentication doesn't work at all
* [Revision #ec494cb1fa](https://github.com/MariaDB/server/commit/ec494cb1fa)\
  2019-06-30 11:14:58 +0200
  * [MDEV-19876](https://jira.mariadb.org/browse/MDEV-19876) pam v2: auth\_pam\_tool\_dir and auth\_pam\_tool permissions are wrong in RPMs
* [Revision #a07c10f53f](https://github.com/MariaDB/server/commit/a07c10f53f)\
  2019-06-30 18:06:49 +0200
  * build pam test module as a part of the build
* [Revision #9c74cc4df7](https://github.com/MariaDB/server/commit/9c74cc4df7)\
  2019-06-30 15:15:46 +0200
  * Alter pam test to ask for a password first
* [Revision #e46b87aaed](https://github.com/MariaDB/server/commit/e46b87aaed)\
  2019-06-17 23:12:42 +0200
  * enable TLSv1.0 in WolfSSL
* [Revision #e79b9005f1](https://github.com/MariaDB/server/commit/e79b9005f1)\
  2019-06-17 13:35:16 +0200
  * don't run tls\_version test if TLSv1.1 is disabled
* [Revision #4bfb19d407](https://github.com/MariaDB/server/commit/4bfb19d407)\
  2019-06-17 13:31:11 +0200
  * cleanup: mtr suite.pm ssl checks
* [Revision #4bad6aa9ae](https://github.com/MariaDB/server/commit/4bad6aa9ae)\
  2019-07-02 12:25:08 +0530
  * [MDEV-19716](https://jira.mariadb.org/browse/MDEV-19716): ASAN use-after-poison in Query\_log\_event::Query\_log\_event / THD::log\_events\_and\_free\_tmp\_shares
* Merge [Revision #9c16460e63](https://github.com/MariaDB/server/commit/9c16460e63) 2019-07-01 18:37:15 +0300 - Merge 10.3 into 10.4
* [Revision #747dccfe23](https://github.com/MariaDB/server/commit/747dccfe23)\
  2019-06-18 12:17:46 +1000
  * systemd multiinstance - doc fix - version number
* [Revision #c5c515130c](https://github.com/MariaDB/server/commit/c5c515130c)\
  2019-06-27 14:35:34 +0200
  * [MDEV-19847](https://jira.mariadb.org/browse/MDEV-19847): Update mysqladmin man page
* [Revision #223c550d92](https://github.com/MariaDB/server/commit/223c550d92)\
  2019-06-30 18:52:45 +0900
  * [MDEV-17402](https://jira.mariadb.org/browse/MDEV-17402) slave\_transaction\_retry\_errors="12701" won't be enabled (#1349)
* [Revision #76200870ea](https://github.com/MariaDB/server/commit/76200870ea)\
  2019-06-29 03:42:35 +0900
  * [MDEV-17204](https://jira.mariadb.org/browse/MDEV-17204) [Mariadb 10.3.9](../../old-releases/10.3/10.3.9.md) Spider DB SQL Alias no execute (#1348)
* [Revision #d4bdf1c0b6](https://github.com/MariaDB/server/commit/d4bdf1c0b6)\
  2019-06-29 03:35:48 +0900
  * [MDEV-16508](https://jira.mariadb.org/browse/MDEV-16508) spider: sql\_mode not maintained between spider node and data nodes (#1347)
* [Revision #5e929ee8a0](https://github.com/MariaDB/server/commit/5e929ee8a0)\
  2019-06-28 12:52:13 +0300
  * [MDEV-19845](https://jira.mariadb.org/browse/MDEV-19845): Define my\_timer\_cycles() inline
* [Revision #1635ea9474](https://github.com/MariaDB/server/commit/1635ea9474)\
  2019-06-29 00:05:34 +0900
  * [MDEV-17402](https://jira.mariadb.org/browse/MDEV-17402) slave\_transaction\_retry\_errors="12701" won't be enabled (#1346)
* Merge [Revision #b7b0bc8f11](https://github.com/MariaDB/server/commit/b7b0bc8f11) 2019-06-27 17:54:47 +0300 - Merge 10.3 into 10.4
* [Revision #bb702c2e4c](https://github.com/MariaDB/server/commit/bb702c2e4c)\
  2019-06-26 19:47:56 +0300
  * Limit minium aria\_block\_size to 4096
* [Revision #4dbe6776fb](https://github.com/MariaDB/server/commit/4dbe6776fb)\
  2019-06-26 19:45:00 +0300
  * [MDEV-19585](https://jira.mariadb.org/browse/MDEV-19585) Assertion with S3 table and flush\_tables
* [Revision #12ce066edf](https://github.com/MariaDB/server/commit/12ce066edf)\
  2019-06-22 13:50:39 +0300
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) InnoDB transition to C++11 atomics
* [Revision #adb640e25a](https://github.com/MariaDB/server/commit/adb640e25a)\
  2019-06-22 13:46:46 +0300
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) InnoDB transition to C++11 atomics
* [Revision #52a5097764](https://github.com/MariaDB/server/commit/52a5097764)\
  2019-06-22 12:48:50 +0300
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) InnoDB transition to C++11 atomics
* [Revision #e9a5f288f2](https://github.com/MariaDB/server/commit/e9a5f288f2)\
  2019-01-09 01:44:29 +0400
  * [MDEV-17441](https://jira.mariadb.org/browse/MDEV-17441) - InnoDB transition to C++11 atomics
* [Revision #04ee96199e](https://github.com/MariaDB/server/commit/04ee96199e)\
  2019-06-19 10:35:39 +0530
  * [MDEV-19049](https://jira.mariadb.org/browse/MDEV-19049) Server crashes in check\_duplicate\_long\_entry\_key, ASAN stack-buffer-overflow in Field\_blob::get\_key\_image
* [Revision #9e0ed0fabd](https://github.com/MariaDB/server/commit/9e0ed0fabd)\
  2019-06-25 23:53:09 +0200
  * [MDEV-19860](https://jira.mariadb.org/browse/MDEV-19860) - do not produce huge strings wtih comp\_sql anymore.
* [Revision #1a518aa1d2](https://github.com/MariaDB/server/commit/1a518aa1d2)\
  2019-06-25 08:06:27 -0700
  * [MDEV-19820](https://jira.mariadb.org/browse/MDEV-19820) Wrong result with multiple single column index request
* [Revision #65368255ff](https://github.com/MariaDB/server/commit/65368255ff)\
  2019-06-05 18:24:49 +0200
  * [MDEV-6521](https://jira.mariadb.org/browse/MDEV-6521): Update server HELP contents
* [Revision #a82e42fd13](https://github.com/MariaDB/server/commit/a82e42fd13)\
  2019-06-17 16:54:47 +0300
  * NFC: refactor Field::is\_equal() and related stuff
* [Revision #854c219a7f](https://github.com/MariaDB/server/commit/854c219a7f)\
  2019-06-14 12:18:49 +0300
  * [MDEV-17301](https://jira.mariadb.org/browse/MDEV-17301) Change of COLLATE unnecessarily requires ALGORITHM=COPY
* [Revision #72d3676fe5](https://github.com/MariaDB/server/commit/72d3676fe5)\
  2019-06-21 18:51:36 +0200
  * remove workaround from [MDEV-9409](https://jira.mariadb.org/browse/MDEV-9409)
* [Revision #e9a692fe1e](https://github.com/MariaDB/server/commit/e9a692fe1e)\
  2019-06-21 15:23:58 +0400
  * [MDEV-19819](https://jira.mariadb.org/browse/MDEV-19819) ALTER from POINT to LINESTRING erroneously preserves POINT values
* [Revision #8b576616b4](https://github.com/MariaDB/server/commit/8b576616b4)\
  2019-06-20 12:03:32 +0530
  * [MDEV-19776](https://jira.mariadb.org/browse/MDEV-19776): Assertion \`to\_len >= 8' failed in convert\_to\_printable with optimizer trace enabled
* [Revision #cfbd714868](https://github.com/MariaDB/server/commit/cfbd714868)\
  2019-06-20 09:48:34 +0400
  * [MDEV-19774](https://jira.mariadb.org/browse/MDEV-19774) Assertion \`sec.se c() <= 0x7FFFFFFFL' failed in Item\_func\_from\_unixtime::get\_date
* Merge [Revision #02979daab4](https://github.com/MariaDB/server/commit/02979daab4) 2019-06-19 10:49:00 +0300 - Merge 10.3 into 10.4
* [Revision #efbfcc8b73](https://github.com/MariaDB/server/commit/efbfcc8b73)\
  2019-06-18 17:44:05 -0400
  * bump the VERSION
* Merge [Revision #3db4d018b8](https://github.com/MariaDB/server/commit/3db4d018b8) 2019-06-18 15:26:16 +0200 - Merge branch 'bb-10.4-release' into 10.4
* [Revision #48570eb65c](https://github.com/MariaDB/server/commit/48570eb65c)\
  2019-06-18 11:36:29 +0200
  * [MDEV-18832](https://jira.mariadb.org/browse/MDEV-18832) Galera: 10.4 node crashed with Assertion \`state() == s\_committing' if you create SEQUENCE, use it, then drop and recreate and use again (#1339)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
