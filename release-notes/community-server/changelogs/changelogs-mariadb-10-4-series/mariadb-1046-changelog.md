# MariaDB 10.4.6 Changelog

The most recent release of [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) is:[**MariaDB 10.4.34**](../../old-releases/10.4/10.4.34.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.6/)[Release Notes](../../old-releases/10.4/10.4.6.md)[Changelog](mariadb-1046-changelog.md)[Overview of 10.4](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)

**Release date:** 18 Jun 2019

For the highlights of this release, see the [release notes](../../old-releases/10.4/10.4.6.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.4) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #b8e655ce02](https://github.com/MariaDB/server/commit/b8e655ce02)\
  2019-06-17 23:33:04 +0200
  * bugfix: crash on the empty db name
* [Revision #e85e4814ee](https://github.com/MariaDB/server/commit/e85e4814ee)\
  2019-06-17 17:26:42 +0200
  * 10.4.6 is stable, not gamma
* [Revision #306e439c6d](https://github.com/MariaDB/server/commit/306e439c6d)\
  2019-06-15 18:27:30 +0200
  * [MDEV-17592](https://jira.mariadb.org/browse/MDEV-17592) Create MariaDB named commands/symlinks
* [Revision #24503d5711](https://github.com/MariaDB/server/commit/24503d5711)\
  2019-05-18 06:11:01 +0000
  * [MDEV-17592](https://jira.mariadb.org/browse/MDEV-17592) Create MariaDB named commands/symlinks
* [Revision #f02bc3cf0f](https://github.com/MariaDB/server/commit/f02bc3cf0f)\
  2019-06-16 22:38:02 +0200
  * change pam and disks plugin maturity beta->gamma
* [Revision #da619f010f](https://github.com/MariaDB/server/commit/da619f010f)\
  2019-06-16 19:42:59 +0200
  * compilation fix for fulltest-big
* [Revision #20bb4ed15e](https://github.com/MariaDB/server/commit/20bb4ed15e)\
  2019-06-16 14:53:17 +0200
  * make the heap.heap test portable
* [Revision #13e8f728ec](https://github.com/MariaDB/server/commit/13e8f728ec)\
  2019-06-16 01:25:03 +0200
  * compilation failure on ppc with -DCMAKE\_BUILD\_TYPE=Debug
* [Revision #0933212036](https://github.com/MariaDB/server/commit/0933212036)\
  2019-06-16 00:41:54 +0200
  * C/C
* [Revision #a4cc6fb91f](https://github.com/MariaDB/server/commit/a4cc6fb91f)\
  2019-06-14 16:10:45 +0200
  * [MDEV-15526](https://jira.mariadb.org/browse/MDEV-15526) SysV init service deployed file '/etc/init.d/mysql' prevents systemctl disable command to work correctly (mariadb|mysql naming support) (debian/ubuntu)
* [Revision #0a43df4fbc](https://github.com/MariaDB/server/commit/0a43df4fbc)\
  2019-06-10 12:13:39 +0200
  * [MDEV-14735](https://jira.mariadb.org/browse/MDEV-14735) better matching order for grants
* [Revision #fd00c449e3](https://github.com/MariaDB/server/commit/fd00c449e3)\
  2019-06-10 09:24:43 +0200
  * bugfix: PROXY privilege matched usernames incorrectly
* [Revision #d13080133f](https://github.com/MariaDB/server/commit/d13080133f)\
  2019-06-11 12:44:16 +0200
  * [MDEV-14101](https://jira.mariadb.org/browse/MDEV-14101) Provide an option to select TLS protocol version
* [Revision #379ffc6eaa](https://github.com/MariaDB/server/commit/379ffc6eaa)\
  2019-06-14 19:52:00 +0200
  * [MDEV-19765](https://jira.mariadb.org/browse/MDEV-19765) Bug in CMakeLists.txt introduced by [MDEV-11670](https://jira.mariadb.org/browse/MDEV-11670)
* [Revision #b3f3b3eaca](https://github.com/MariaDB/server/commit/b3f3b3eaca)\
  2019-06-15 21:30:44 +0200
  * fix versioning.simple for embedded
* [Revision #7ad1e4a546](https://github.com/MariaDB/server/commit/7ad1e4a546)\
  2019-06-17 12:26:15 +0200
  * fix tests, failing after daf333abcfc
* [Revision #daf333abcf](https://github.com/MariaDB/server/commit/daf333abcf)\
  2019-06-17 11:20:31 +0300
  * Rename of stat table tried to rename open table.
* [Revision #bff7cf9df8](https://github.com/MariaDB/server/commit/bff7cf9df8)\
  2019-06-15 18:57:07 +0200
  * Fix of fail of period.updtae with ps protocol.
* [Revision #bf90a486c3](https://github.com/MariaDB/server/commit/bf90a486c3)\
  2019-06-14 23:52:13 +0200
  * Do not use LEX\_CSTRING in printf-like function
* Merge [Revision #f66d1850ac](https://github.com/MariaDB/server/commit/f66d1850ac) 2019-06-14 22:10:50 +0200 - Merge branch '10.3' into 10.4
* [Revision #772c5f3c78](https://github.com/MariaDB/server/commit/772c5f3c78)\
  2019-06-14 12:16:17 +0530
  * [MDEV-19634](https://jira.mariadb.org/browse/MDEV-19634): Assertion \`0' failed in row\_sel\_convert\_mysql\_key\_to\_innobase, \[Warning] InnoDB: Using a partial-field key prefix in search
* [Revision #1e3dc15d62](https://github.com/MariaDB/server/commit/1e3dc15d62)\
  2019-06-04 17:11:42 +0200
  * Use generated user\_settings.h for WolfSSL, as recommended by WolfSSL documentation
* [Revision #4ec302ebf8](https://github.com/MariaDB/server/commit/4ec302ebf8)\
  2019-06-14 15:49:38 +0200
  * WolfSSL : Fix crosscompiling i386 on x86\_64, on Linux
* [Revision #e22d2cfe58](https://github.com/MariaDB/server/commit/e22d2cfe58)\
  2019-02-13 07:31:48 +1100
  * fix typo support-files/mariadb@.service.in
* [Revision #764a10a926](https://github.com/MariaDB/server/commit/764a10a926)\
  2019-02-12 12:14:01 +1100
  * [MDEV-11670](https://jira.mariadb.org/browse/MDEV-11670): mariadb@.service remove alias, clean up documentation/order
* [Revision #6e5c246639](https://github.com/MariaDB/server/commit/6e5c246639)\
  2019-02-12 12:13:14 +1100
  * [MDEV-11670](https://jira.mariadb.org/browse/MDEV-11670): ensure sysconfdir/sysconf2dir are not blank for mariadb@.service
* [Revision #91f1694836](https://github.com/MariaDB/server/commit/91f1694836)\
  2019-01-18 14:52:25 +1100
  * systemd: multi-instance not for Galera, User/Group flexible
* [Revision #3a0a570e0b](https://github.com/MariaDB/server/commit/3a0a570e0b)\
  2017-12-12 11:26:09 +1100
  * systemd: multi-instance changes to -defaults-group-suffix=.%I
* [Revision #e5fab61a73](https://github.com/MariaDB/server/commit/e5fab61a73)\
  2019-06-14 07:53:42 +0300
  * [MDEV-6275](https://jira.mariadb.org/browse/MDEV-6275): Use a non-narrowing conversion
* [Revision #2cd45add27](https://github.com/MariaDB/server/commit/2cd45add27)\
  2019-06-14 07:34:25 +0300
  * [MDEV-6275](https://jira.mariadb.org/browse/MDEV-6275): Fix signed/unsigned comparison
* Merge [Revision #991d5140c3](https://github.com/MariaDB/server/commit/991d5140c3) 2019-06-14 07:29:20 +0300 - Merge 10.3 into 10.4
* [Revision #8e3a4be45c](https://github.com/MariaDB/server/commit/8e3a4be45c)\
  2019-06-12 19:30:50 +0900
  * [MDEV-6275](https://jira.mariadb.org/browse/MDEV-6275) spider\_same\_server\_link not enforced (#1330)
* Merge [Revision #2fd82471ab](https://github.com/MariaDB/server/commit/2fd82471ab) 2019-06-12 08:37:27 +0300 - Merge 10.3 into 10.4
* [Revision #1f6b02e9f0](https://github.com/MariaDB/server/commit/1f6b02e9f0)\
  2019-06-12 01:08:09 +0200
  * [MDEV-19709](https://jira.mariadb.org/browse/MDEV-19709) Workaround "internal compiler bug" on GCC v 4.9
* [Revision #0af1840892](https://github.com/MariaDB/server/commit/0af1840892)\
  2019-06-07 20:04:09 +0200
  * [MDEV-19706](https://jira.mariadb.org/browse/MDEV-19706) RPM no longer installs init script on systemd systems, but preun script still tries to erase it
* [Revision #27fcdb161c](https://github.com/MariaDB/server/commit/27fcdb161c)\
  2019-06-11 17:51:09 +0200
  * [MDEV-16249](https://jira.mariadb.org/browse/MDEV-16249) CHECKSUM TABLE for a spider table is not parallel and saves all data in memory in the spider head by default (#1328)
* [Revision #bb70d41932](https://github.com/MariaDB/server/commit/bb70d41932)\
  2019-06-11 13:52:20 +0300
  * [MDEV-19709](https://jira.mariadb.org/browse/MDEV-19709): Unbreak the build for clang
* [Revision #1b86ef9f54](https://github.com/MariaDB/server/commit/1b86ef9f54)\
  2019-06-11 12:39:46 +0530
  * enabled test archive\_gis
* [Revision #a0cb7551a4](https://github.com/MariaDB/server/commit/a0cb7551a4)\
  2019-06-10 15:56:36 +0530
  * [MDEV-18880](https://jira.mariadb.org/browse/MDEV-18880): Optimizer trace prints date in hexadecimal
* [Revision #40ff8019d2](https://github.com/MariaDB/server/commit/40ff8019d2)\
  2019-06-07 11:41:18 +0200
  * [MDEV-19709](https://jira.mariadb.org/browse/MDEV-19709) Bitmap<128>::merge etc may crash on older GCC versions
* [Revision #be5c432a42](https://github.com/MariaDB/server/commit/be5c432a42)\
  2019-06-11 00:25:08 +0900
  * [MDEV-16249](https://jira.mariadb.org/browse/MDEV-16249) CHECKSUM TABLE for a spider table is not parallel and saves all data in memory in the spider head by default (#1328)
* [Revision #5e9090ef16](https://github.com/MariaDB/server/commit/5e9090ef16)\
  2019-06-01 23:56:55 +0300
  * Deb: Purge unused debconf translations
* [Revision #973b281e59](https://github.com/MariaDB/server/commit/973b281e59)\
  2019-06-06 17:10:57 +0200
  * [MDEV-18788](https://jira.mariadb.org/browse/MDEV-18788) Live upgrade from MySQL 5.6/5.7 to [MariaDB 10.4](../../../mariadb-community-server-release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/) fails with "Event Scheduler: An error occurred when initializing system tables"
* [Revision #06291c3f36](https://github.com/MariaDB/server/commit/06291c3f36)\
  2019-06-06 17:06:41 +0200
  * small cleanup
* [Revision #4e0c6139b2](https://github.com/MariaDB/server/commit/4e0c6139b2)\
  2019-06-07 12:54:16 +0200
  * Minor Galera MTR test fixes (#1326)
* [Revision #6999da9b19](https://github.com/MariaDB/server/commit/6999da9b19)\
  2019-06-06 14:41:45 +0400
  * Record BACKUP and SCHEMA namespaces order
* [Revision #965db355e6](https://github.com/MariaDB/server/commit/965db355e6)\
  2019-06-05 13:06:27 +0200
  * update C/C
* [Revision #c5beac6847](https://github.com/MariaDB/server/commit/c5beac6847)\
  2019-06-04 10:07:39 +0200
  * [MDEV-19684](https://jira.mariadb.org/browse/MDEV-19684) enable intel assembly (AESNI etc) and fastmath when compiling WolfSSL
* [Revision #92df31dfbf](https://github.com/MariaDB/server/commit/92df31dfbf)\
  2019-06-02 13:12:39 +0200
  * Added new file client-certkey.pem for testing [CONC-386](https://jira.mariadb.org/browse/CONC-386):
* [Revision #cd1d161c26](https://github.com/MariaDB/server/commit/cd1d161c26)\
  2019-05-30 17:03:26 +0400
  * [MDEV-19637](https://jira.mariadb.org/browse/MDEV-19637) Crash on an SP variable assignment to a wrong subselect
* Merge [Revision #f98bb23168](https://github.com/MariaDB/server/commit/f98bb23168) 2019-05-29 22:17:00 +0300 - Merge 10.3 into 10.4
* [Revision #e35676f555](https://github.com/MariaDB/server/commit/e35676f555)\
  2019-05-29 06:06:36 +0200
  * Fix compilation on Linux
* [Revision #1df42a2ca0](https://github.com/MariaDB/server/commit/1df42a2ca0)\
  2019-05-28 20:03:44 +0200
  * [MDEV-19617](https://jira.mariadb.org/browse/MDEV-19617) Assertion \`src' failed in MyCTX::update
* [Revision #5e36f5dd00](https://github.com/MariaDB/server/commit/5e36f5dd00)\
  2019-05-28 15:43:12 +0530
  * [MDEV-18741](https://jira.mariadb.org/browse/MDEV-18741): Optimizer trace: multi-part key ranges are printed incorrectly
* [Revision #24773bf380](https://github.com/MariaDB/server/commit/24773bf380)\
  2019-05-27 20:14:49 +0300
  * [MDEV-19606](https://jira.mariadb.org/browse/MDEV-19606): dict\_v\_col\_t: Encapsulate v\_indexes
* [Revision #0274ab1de3](https://github.com/MariaDB/server/commit/0274ab1de3)\
  2019-05-27 19:45:44 +0300
  * [MDEV-19606](https://jira.mariadb.org/browse/MDEV-19606): Replace most std::list with std::forward\_list
* [Revision #50e79f604e](https://github.com/MariaDB/server/commit/50e79f604e)\
  2019-05-27 13:52:49 +0300
  * [MDEV-19606](https://jira.mariadb.org/browse/MDEV-19606): Make recv\_dblwr\_t::list a forward\_list
* [Revision #7d3a759d42](https://github.com/MariaDB/server/commit/7d3a759d42)\
  2019-05-27 17:41:55 +0200
  * [MDEV-19604](https://jira.mariadb.org/browse/MDEV-19604) WolfSSL breaks binlog\_encryption.binlog\_incident
* [Revision #d80065c2e4](https://github.com/MariaDB/server/commit/d80065c2e4)\
  2019-05-27 14:18:05 +0300
  * [MDEV-18425](https://jira.mariadb.org/browse/MDEV-18425): wsrep.mdev\_10186: Test failure: "Result length mismatch" (@@GLOBAL.wsrep\_provider)
* [Revision #e32212c63c](https://github.com/MariaDB/server/commit/e32212c63c)\
  2019-05-27 10:16:23 +0300
  * [MDEV-19582](https://jira.mariadb.org/browse/MDEV-19582) Out-of-bounds memory accesses by WolfSSL
* [Revision #f465ec8c45](https://github.com/MariaDB/server/commit/f465ec8c45)\
  2019-05-25 23:03:02 +0200
  * Lets pretend that WolfSSL does not support AES-CTR
* [Revision #88b7926ff8](https://github.com/MariaDB/server/commit/88b7926ff8)\
  2019-05-25 22:59:33 +0200
  * [MDEV-19582](https://jira.mariadb.org/browse/MDEV-19582) WolfSSL decyption function can read memory out-of-bounds. [MDEV-19581](https://jira.mariadb.org/browse/MDEV-19581) Valgrind error with WolfSSL and encrypted binlog
* [Revision #5d2619b693](https://github.com/MariaDB/server/commit/5d2619b693)\
  2019-05-24 16:19:38 +0300
  * [MDEV-19584](https://jira.mariadb.org/browse/MDEV-19584) Allocate recv\_sys statically
* [Revision #592fe954ef](https://github.com/MariaDB/server/commit/592fe954ef)\
  2019-02-13 10:57:54 +0100
  * [MDEV-18531](https://jira.mariadb.org/browse/MDEV-18531) : remove yassl
* [Revision #5e4b657dd4](https://github.com/MariaDB/server/commit/5e4b657dd4)\
  2019-02-13 09:08:06 +0100
  * [MDEV-18531](https://jira.mariadb.org/browse/MDEV-18531) : Use WolfSSL instead of YaSSL as "bundled" SSL/encryption library
* [Revision #31fe70290c](https://github.com/MariaDB/server/commit/31fe70290c)\
  2019-05-22 10:30:20 +0300
  * Fixed sometimes wrong result in main.subselect\_sj2\_mat
* [Revision #b40c99a82c](https://github.com/MariaDB/server/commit/b40c99a82c)\
  2019-05-21 16:33:37 +0300
  * [MDEV-17458](https://jira.mariadb.org/browse/MDEV-17458): Clear more of the TRX\_SYS page
* Merge [Revision #cf77951fb6](https://github.com/MariaDB/server/commit/cf77951fb6) 2019-05-22 08:42:31 +0300 - Merge 10.3 into 10.4
* [Revision #1921df6697](https://github.com/MariaDB/server/commit/1921df6697)\
  2019-05-21 15:33:35 +0200
  * [MDEV-19540](https://jira.mariadb.org/browse/MDEV-19540): 10.4 allow lock options with SELECT in brackets which previous version do not
* [Revision #fceffcdf0b](https://github.com/MariaDB/server/commit/fceffcdf0b)\
  2018-11-06 23:49:27 +0100
  * Add GNU/Hurd cmake configuration
* [Revision #89d7185760](https://github.com/MariaDB/server/commit/89d7185760)\
  2019-05-21 08:40:47 -0400
  * bump the VERSION
* [Revision #8164bd24a6](https://github.com/MariaDB/server/commit/8164bd24a6)\
  2019-05-21 14:22:49 +0400
  * [MDEV-19535](https://jira.mariadb.org/browse/MDEV-19535) sql\_mode=ORACLE: 'SELECT INTO @var FOR UPDATE' does not lock the table
* [Revision #ed39181a27](https://github.com/MariaDB/server/commit/ed39181a27)\
  2019-05-21 12:30:21 +0400
  * [MDEV-19533](https://jira.mariadb.org/browse/MDEV-19533) Add methods make() and append\_uniq() to Row\_definition\_list
* [Revision #fae1319450](https://github.com/MariaDB/server/commit/fae1319450)\
  2019-05-20 18:50:12 +0300
  * [MDEV-19524](https://jira.mariadb.org/browse/MDEV-19524) Server crashes in Bitmap<64u>::is\_clear\_all / Field\_longstr::csinfo\_change\_allows\_instant\_alter

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
