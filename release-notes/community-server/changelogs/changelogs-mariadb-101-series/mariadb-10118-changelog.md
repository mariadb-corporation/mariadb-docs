# MariaDB 10.1.18 Changelog

The most recent release of [MariaDB 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md) is:[**MariaDB 10.1.48**](../../old-releases/10.1/10.1.48.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.1.48/)

[Download](https://downloads.mariadb.org/mariadb/10.1.18)[Release Notes](../../old-releases/10.1/10.1.18.md)[Changelog](mariadb-10118-changelog.md)[Overview of 10.1](../../old-releases/10.1/changes-improvements-in-mariadb-10-1.md)

**Release date:** 30 Sep 2016

For the highlights of this release, see the [release notes](../../old-releases/10.1/10.1.18.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.1) you can view more details of the revision and view diffs of the code modified in that revision.

* [Revision #6925689](https://github.com/MariaDB/server/commit/6925689)\
  2016-09-29 14:58:32 -0400
  * [MDEV-9312](https://jira.mariadb.org/browse/MDEV-9312): storage engine not enforced during galera cluster replication
* [Revision #235876d](https://github.com/MariaDB/server/commit/235876d)\
  2016-09-29 14:21:14 +0200
  * update test results after merge
* [Revision #2ede40e](https://github.com/MariaDB/server/commit/2ede40e) 2016-09-29 12:59:51 +0200 - Merge branch '10.0' into 10.1
* [Revision #a3f11f7](https://github.com/MariaDB/server/commit/a3f11f7) 2016-09-29 12:31:46 +0200 - Merge branch '5.5' into 10.0
* [Revision #7497ebf](https://github.com/MariaDB/server/commit/7497ebf)\
  2016-09-29 10:16:24 +0200
  * mysqld\_safe: close stdout and stderr
* [Revision #0e76054](https://github.com/MariaDB/server/commit/0e76054)\
  2016-09-28 12:52:01 +0000
  * Feedback plugin : add support for Windows 10 / Server 2016.
* [Revision #b38d3c3](https://github.com/MariaDB/server/commit/b38d3c3)\
  2016-09-27 12:34:15 +0000
  * [MDEV-10907](https://jira.mariadb.org/browse/MDEV-10907) MTR and server writes can interleave in the error log
* [Revision #ad20769](https://github.com/MariaDB/server/commit/ad20769)\
  2016-09-29 11:50:13 +0200
  * init plugin psi keys before LOCK\_plugin
* [Revision #b34c813](https://github.com/MariaDB/server/commit/b34c813)\
  2016-09-28 22:12:03 +0200
  * [MDEV-10201](https://jira.mariadb.org/browse/MDEV-10201) SSL tests fail on fedora23
* [Revision #9ff9acb](https://github.com/MariaDB/server/commit/9ff9acb)\
  2016-09-22 17:52:05 +0200
  * [MDEV-10716](https://jira.mariadb.org/browse/MDEV-10716): Assertion \`\`real\_type() != FIELD\_ITEM'`failed in`Item\_ref::build\_equal\_items(THD\*, COND\_EQUAL\*, bool, COND\_EQUAL)\`
* [Revision #d5dfa0f](https://github.com/MariaDB/server/commit/d5dfa0f)\
  2016-09-28 13:27:34 -0400
  * [MDEV-9416](https://jira.mariadb.org/browse/MDEV-9416): MariaDB galera got signal 11 when altering table add unique index
* [Revision #7c525ce](https://github.com/MariaDB/server/commit/7c525ce)\
  2016-09-28 13:26:13 -0400
  * [MDEV-9312](https://jira.mariadb.org/browse/MDEV-9312): storage engine not enforced during galera cluster replication
* [Revision #88f2ec6](https://github.com/MariaDB/server/commit/88f2ec6)\
  2016-09-28 13:23:31 -0400
  * [MDEV-10041](https://jira.mariadb.org/browse/MDEV-10041): Server crashes sporadically during bootstrap while running wsrep tests
* [Revision #e1c6f28](https://github.com/MariaDB/server/commit/e1c6f28) 2016-09-28 13:20:02 -0400 - Merge branch '10.0-galera' into 10.1
* [Revision #c9ded85](https://github.com/MariaDB/server/commit/c9ded85)\
  2016-09-21 10:51:37 +0200
  * [MDEV-10853](https://jira.mariadb.org/browse/MDEV-10853) netcat help output in error log when running xtrabackup SST
* [Revision #3dd88fb](https://github.com/MariaDB/server/commit/3dd88fb)\
  2016-09-01 12:59:11 -0400
  * [MDEV-10714](https://jira.mariadb.org/browse/MDEV-10714): Could not execute Delete\_rows event on table; wsrep\_max\_ws\_rows exceeded. Error\_Code 1180
* [Revision #616271b](https://github.com/MariaDB/server/commit/616271b)\
  2016-09-01 12:53:44 -0400
  * Cleanup: MDL\_context::wsrep\_get\_thd() is no longer needed
* [Revision #16702ec](https://github.com/MariaDB/server/commit/16702ec)\
  2016-08-25 21:19:25 -0400
  * Record wsrep.variables test result (with non-debug galera library).
* [Revision #735a4a1](https://github.com/MariaDB/server/commit/735a4a1)\
  2016-09-28 17:59:11 +0200
  * [MDEV-10508](https://jira.mariadb.org/browse/MDEV-10508) Mariadb crash on out of disk space during dump import
* [Revision #794c826](https://github.com/MariaDB/server/commit/794c826)\
  2016-09-26 14:29:23 +0200
  * [MDEV-10890](https://jira.mariadb.org/browse/MDEV-10890) plugins.pam fails in buildbot with valgrind
* [Revision #66d9696](https://github.com/MariaDB/server/commit/66d9696) 2016-09-28 17:55:28 +0200 - Merge branch '10.0' into 10.1
* [Revision #23af6f5](https://github.com/MariaDB/server/commit/23af6f5) 2016-09-28 16:19:58 +0300 - Merge branch '10.0' of github.com:MariaDB/server into 10.0
* [Revision #078e510](https://github.com/MariaDB/server/commit/078e510) 2016-09-27 19:03:11 +0200 - Merge branch 'merge/merge-tokudb-5.6' into 10.0
* [Revision #e312e2e](https://github.com/MariaDB/server/commit/e312e2e)\
  2016-09-27 17:59:58 +0200
  * 5.6.32-78.1
* [Revision #2e914ac](https://github.com/MariaDB/server/commit/2e914ac) 2016-09-27 19:00:08 +0200 - Merge branch 'merge/merge-perfschema-5.6' into 10.0
* [Revision #e3124a8](https://github.com/MariaDB/server/commit/e3124a8)\
  2016-09-27 17:57:28 +0200
  * 5.6.33
* [Revision #bb8b658](https://github.com/MariaDB/server/commit/bb8b658) 2016-09-27 18:58:57 +0200 - Merge branch 'merge/merge-xtradb-5.6' into 10.0
* [Revision #93ab309](https://github.com/MariaDB/server/commit/93ab309)\
  2016-09-27 18:00:59 +0200
  * 5.6.32-78.1
* [Revision #3629f62](https://github.com/MariaDB/server/commit/3629f62) 2016-09-27 18:05:06 +0200 - Merge branch 'merge/merge-innodb-5.6' into 10.0
* [Revision #094f140](https://github.com/MariaDB/server/commit/094f140)\
  2016-09-27 17:56:00 +0200
  * 5.6.33
* [Revision #77ce4ea](https://github.com/MariaDB/server/commit/77ce4ea) 2016-09-27 09:21:19 +0200 - Merge branch '5.5' into 10.0
* [Revision #d61e526](https://github.com/MariaDB/server/commit/d61e526)\
  2016-09-26 17:48:08 +0200
  * [MDEV-10441](https://jira.mariadb.org/browse/MDEV-10441) Document the server\_audit\_loc\_info variable
* [Revision #c91fdb6](https://github.com/MariaDB/server/commit/c91fdb6)\
  2016-09-26 13:03:02 +0200
  * Windows , mtr : allow cdb to print core dumps also if --parallel > 1
* [Revision #8483659](https://github.com/MariaDB/server/commit/8483659)\
  2016-09-24 10:06:58 +0200
  * report correct write error on log writes
* [Revision #f620da1](https://github.com/MariaDB/server/commit/f620da1)\
  2016-09-24 01:17:35 +0200
  * [MDEV-10725](https://jira.mariadb.org/browse/MDEV-10725) Server 10.1.17 fails to build using clang with c++11
* [Revision #9434431](https://github.com/MariaDB/server/commit/9434431)\
  2016-09-24 13:50:42 +0200
  * Fix free() after my\_malloc() (should be my\_free()).
* [Revision #b3f7a80](https://github.com/MariaDB/server/commit/b3f7a80)\
  2016-09-13 11:12:54 -0400
  * bump the VERSION
* [Revision #0da39ca](https://github.com/MariaDB/server/commit/0da39ca)\
  2016-09-12 16:18:07 +0200
  * fix BIGINT+MEDIUMINT type aggregation
* [Revision #347eeef](https://github.com/MariaDB/server/commit/347eeef)\
  2016-09-11 20:55:11 +0200
  * don't use my\_copystat in the server
* [Revision #611dc0d](https://github.com/MariaDB/server/commit/611dc0d)\
  2016-09-11 20:53:16 +0200
  * missing element in prelocked\_mode\_name\[] array
* [Revision #a229091](https://github.com/MariaDB/server/commit/a229091)\
  2016-09-11 20:52:00 +0200
  * potential signedness issue
* [Revision #7ae555c](https://github.com/MariaDB/server/commit/7ae555c) 2016-09-11 20:51:09 +0200 - Merge branch 'mysql/5.5' into 5.5
* [Revision #b9631e3](https://github.com/MariaDB/server/commit/b9631e3)\
  2015-11-10 12:41:26 +0100
  * [MDEV-8833](https://jira.mariadb.org/browse/MDEV-8833) Crash of server on prepared statement with conversion to semi-join
* [Revision #ee97274](https://github.com/MariaDB/server/commit/ee97274)\
  2016-08-25 09:50:04 +0300
  * DEV-10595 MariaDB daemon leaks memory with specific query
* [Revision #a92a8cc](https://github.com/MariaDB/server/commit/a92a8cc)\
  2016-08-19 17:11:20 +0000
  * Windows packaging : use /d switch to sign MSI, to prevent installer showing randomly generated name in UAC prompt
* [Revision #723488b](https://github.com/MariaDB/server/commit/723488b)\
  2016-08-04 15:43:52 +0400
  * [MDEV-10424](https://jira.mariadb.org/browse/MDEV-10424) - Assertion \`\`ticket == null'\` failed in MDL\_request::set\_type
* [Revision #09cb646](https://github.com/MariaDB/server/commit/09cb646)\
  2016-08-11 19:35:53 +0000
  * Windows : fix search for WiX root directory when using 64bit cmake
* [Revision #737964d](https://github.com/MariaDB/server/commit/737964d)\
  2016-08-10 11:24:18 -0400
  * bump the VERSION
* [Revision #677c44f](https://github.com/MariaDB/server/commit/677c44f)\
  2016-09-23 20:27:58 +0200
  * [MDEV-10775](https://jira.mariadb.org/browse/MDEV-10775) System table in InnoDB format allowed in MariaDB could lead to crash
* [Revision #e56a539](https://github.com/MariaDB/server/commit/e56a539)\
  2016-07-01 13:57:18 +0400
  * [MDEV-10315](https://jira.mariadb.org/browse/MDEV-10315) - Online ALTER TABLE may get stuck in tdc\_remove\_table
* [Revision #83d5b96](https://github.com/MariaDB/server/commit/83d5b96)\
  2016-09-19 17:15:18 +0200
  * Fix tokudb jemalloc linking
* [Revision #fd0c114](https://github.com/MariaDB/server/commit/fd0c114)\
  2016-09-12 14:57:32 +0200
  * Update contributors
* [Revision #6e02d42](https://github.com/MariaDB/server/commit/6e02d42)\
  2016-09-13 13:16:11 +0200
  * Fix compilation failure of TokuDB on BSD-like systems
* [Revision #b34d7fb](https://github.com/MariaDB/server/commit/b34d7fb)\
  2016-09-11 11:18:27 +0200
  * Debian bug#837369 - test failures on hppa
* [Revision #af3dc48](https://github.com/MariaDB/server/commit/af3dc48)\
  2016-09-10 20:42:20 +0200
  * Attempt to fix strange rpm dependency issue following prior patch
* [Revision #577f3c1](https://github.com/MariaDB/server/commit/577f3c1)\
  2016-09-10 17:50:32 +0200
  * Fix use of `require` in mysql-test-run.
* [Revision #6c74ef8](https://github.com/MariaDB/server/commit/6c74ef8)\
  2016-09-07 09:30:02 +1000
  * [MDEV-10707](https://jira.mariadb.org/browse/MDEV-10707): Fix tokudb test rows-32m-rand-insert (#231)
* [Revision #a14f61e](https://github.com/MariaDB/server/commit/a14f61e)\
  2016-09-05 12:28:35 +0300
  * [MDEV-7142](https://jira.mariadb.org/browse/MDEV-7142): main.index\_merge\_innodb fails sporadically in buildbot
* [Revision #f81f985](https://github.com/MariaDB/server/commit/f81f985)\
  2016-08-29 11:53:33 +0200
  * fix conpilation on OpenBSD
* [Revision #39ec5ac](https://github.com/MariaDB/server/commit/39ec5ac)\
  2016-08-25 11:55:54 -0400
  * bump the VERSION
* [Revision #66a58f4](https://github.com/MariaDB/server/commit/66a58f4) 2016-09-28 16:19:05 +0300 - Merge fix for [MDEV-10649](https://jira.mariadb.org/browse/MDEV-10649) from 10.0 to 10.1
* [Revision #a53f3c6](https://github.com/MariaDB/server/commit/a53f3c6)\
  2016-09-28 16:12:58 +0300
  * [MDEV-10649](https://jira.mariadb.org/browse/MDEV-10649): Optimizer sometimes use "index" instead of "range" access for UPDATE
* [Revision #0e47223](https://github.com/MariaDB/server/commit/0e47223)\
  2016-09-27 17:38:47 +0200
  * Make sure to recompile the feedback plugin for EMBEDDED
* [Revision #e226276](https://github.com/MariaDB/server/commit/e226276)\
  2016-09-14 18:15:03 +0200
  * [MDEV-10777](https://jira.mariadb.org/browse/MDEV-10777): Server crashed due to query\_cache\_info plugin
* [Revision #3f5aedc](https://github.com/MariaDB/server/commit/3f5aedc)\
  2016-09-27 11:18:24 +0000
  * [MDEV-10847](https://jira.mariadb.org/browse/MDEV-10847) Bring AWS KMS encryption plugin up-to-date with released SDK
* [Revision #f1aefd9](https://github.com/MariaDB/server/commit/f1aefd9)\
  2016-09-23 18:55:44 +0200
  * [MDEV-10823](https://jira.mariadb.org/browse/MDEV-10823) Certain unicode characters in hostname prevent mysqld from starting
* [Revision #661d08c](https://github.com/MariaDB/server/commit/661d08c)\
  2016-09-26 15:16:00 +0300
  * [MDEV-10887](https://jira.mariadb.org/browse/MDEV-10887): innodb.innodb\_stats\_fetch\_nonexistent fails in buildbot on Windows
* [Revision #452e849](https://github.com/MariaDB/server/commit/452e849)\
  2016-09-26 12:29:31 +0300
  * [MDEV-10886](https://jira.mariadb.org/browse/MDEV-10886): encryption.innodb-bad-key-change fails (crashes) in buildbot
* [Revision #4e2a0c3](https://github.com/MariaDB/server/commit/4e2a0c3)\
  2016-09-26 09:58:50 +0300
  * [MDEV-10888](https://jira.mariadb.org/browse/MDEV-10888): encryption.filekeys\_emptyfile fails in buildbot with valgrind
* [Revision #d30809a](https://github.com/MariaDB/server/commit/d30809a)\
  2016-09-26 09:40:47 +0400
  * [MDEV-10832](https://jira.mariadb.org/browse/MDEV-10832) Out of tree build: mysql\_install\_db to see all .sql files.
* [Revision #7d7b92c](https://github.com/MariaDB/server/commit/7d7b92c)\
  2016-09-24 14:21:27 +0300
  * Disable encryption info and first page read info for every tablespace on product builds.
* [Revision #5d001d1](https://github.com/MariaDB/server/commit/5d001d1)\
  2016-09-23 17:28:38 +1000
  * [MDEV-10832](https://jira.mariadb.org/browse/MDEV-10832) - Out of tree build: mysql\_install\_db to see all .sql files (#237)
* [Revision #e136aa1](https://github.com/MariaDB/server/commit/e136aa1)\
  2016-09-23 09:11:11 +0300
  * Fix test failure. Need to mask more tablespace numbers as they are not consistent on parallel mtr runs.
* [Revision #1d55cfc](https://github.com/MariaDB/server/commit/1d55cfc)\
  2016-09-22 20:57:15 +0300
  * Do not use os\_file\_read() directly for reading first page of the tablespace. Instead use fil\_read() with syncronous setting. Fix test failures and mask tablespace number as it could change in concurrent mtr runs.
* [Revision #2bedc39](https://github.com/MariaDB/server/commit/2bedc39)\
  2016-09-22 16:32:26 +0300
  * [MDEV-9931](https://jira.mariadb.org/browse/MDEV-9931): InnoDB reads first page of every .ibd file at startup
* [Revision #e387bfa](https://github.com/MariaDB/server/commit/e387bfa)\
  2016-09-22 19:14:40 +1000
  * [MDEV-10830](https://jira.mariadb.org/browse/MDEV-10830) - Fix undefined database test error when running mysql\_install\_db (#234)
* [Revision #9f837c6](https://github.com/MariaDB/server/commit/9f837c6)\
  2016-09-22 10:03:12 +0400
  * [MDEV-10864](https://jira.mariadb.org/browse/MDEV-10864) Wrong result for WHERE .. (f2=COMPRESS('test') OR f2=COMPRESS('TEST'))
* [Revision #7e4eb99](https://github.com/MariaDB/server/commit/7e4eb99)\
  2016-09-22 07:00:10 +0400
  * [MDEV-10425](https://jira.mariadb.org/browse/MDEV-10425) Assertion \`\`collation.derivation == DERIVATION\_IMPLICIT'`failed in`Item\_func\_conv\_charset::fix\_length\_and\_dec()\`
  * [MDEV-10850](https://jira.mariadb.org/browse/MDEV-10850) Wrong result for `WHERE .. (f2=TO_BASE64('test') OR f2=TO_BASE64('TEST'))`
* [Revision #ec7e0b7](https://github.com/MariaDB/server/commit/ec7e0b7)\
  2016-09-21 09:13:33 +0400
  * [MDEV-10556](https://jira.mariadb.org/browse/MDEV-10556) Assertion \`\`0'`failed in virtual void`Item\_sum\_field::set\_result\_field(Field\*)\`
* [Revision #8b51bac](https://github.com/MariaDB/server/commit/8b51bac)\
  2016-09-20 21:32:53 -0400
  * [MDEV-10735](https://jira.mariadb.org/browse/MDEV-10735): Valgrind warnings around Galera SST
* [Revision #6eca463](https://github.com/MariaDB/server/commit/6eca463)\
  2016-09-20 15:17:57 -0400
  * Fix typo in valgrind.supp
* [Revision #bb2c1a5](https://github.com/MariaDB/server/commit/bb2c1a5) 2016-09-09 11:53:50 +0200 - Merge parallel replication async deadlock kill into 10.1
* [Revision #7e0c9de](https://github.com/MariaDB/server/commit/7e0c9de)\
  2016-09-08 15:25:40 +0200
  * Parallel replication async deadlock kill
* [Revision #de7f877](https://github.com/MariaDB/server/commit/de7f877)\
  2016-09-09 08:40:24 +0400
  * [MDEV-10702](https://jira.mariadb.org/browse/MDEV-10702) Crash in SET STATEMENT FOR EXECUTE
* [Revision #8494039](https://github.com/MariaDB/server/commit/8494039)\
  2016-09-06 16:34:25 +0200
  * fix the test to work
* [Revision #61fd38a](https://github.com/MariaDB/server/commit/61fd38a)\
  2016-09-05 17:11:14 +0200
  * update plugin maturities
* [Revision #362ad94](https://github.com/MariaDB/server/commit/362ad94)\
  2016-09-05 09:11:42 +0200
  * cleanup: don't copy-paste, don't current\_thd
* [Revision #747893a](https://github.com/MariaDB/server/commit/747893a)\
  2016-09-02 14:40:09 -0400
  * [MDEV-10545](https://jira.mariadb.org/browse/MDEV-10545): Update perfschema.nesting result
* [Revision #31697d0](https://github.com/MariaDB/server/commit/31697d0)\
  2016-09-02 12:21:40 -0400
  * [MDEV-10545](https://jira.mariadb.org/browse/MDEV-10545): Server crashed in my\_copy\_fix\_mb on querying I\_S and P\_S tables
* [Revision #a322651](https://github.com/MariaDB/server/commit/a322651)\
  2016-08-29 16:44:46 +0200
  * [MDEV-10017](https://jira.mariadb.org/browse/MDEV-10017): Get unexpected `Empty Set` for correlated subquery with aggregate functions
* [Revision #f6e47c0](https://github.com/MariaDB/server/commit/f6e47c0) 2016-08-31 11:51:12 +0400 - Merge pull request #224 from 0xAX/build-get-rid-from-die
* [Revision #080ac47](https://github.com/MariaDB/server/commit/080ac47)\
  2016-08-25 15:56:53 +0600
  * remove die() from BUILD/autorun.sh
* [Revision #64fe389](https://github.com/MariaDB/server/commit/64fe389)\
  2016-08-30 10:32:37 -0400
  * bump the VERSION

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
