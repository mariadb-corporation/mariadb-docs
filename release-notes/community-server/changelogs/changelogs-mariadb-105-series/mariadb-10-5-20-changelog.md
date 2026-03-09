# MariaDB 10.5.20 Changelog

The most recent release of [MariaDB 10.5](../../old-releases/10.5/what-is-mariadb-105.md) is:[**MariaDB 10.5.28**](../../old-releases/10.5/10.5.28.md) Stable (GA) [Download Now](https://mariadb.com/downloads/)[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.28/)

[Download 10.5.20](https://downloads.mariadb.org/mariadb/10.5.20/)[Release Notes](../../old-releases/10.5/10.5.20.md)[Changelog](mariadb-10-5-20-changelog.md)[Overview of 10.5](../../old-releases/10.5/what-is-mariadb-105.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.5.20/)

**Release date:** 10 May 2023

For the highlights of this release, see the [release notes](../../old-releases/10.5/10.5.20.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.5) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.4.29](../changelogs-mariadb-10-4-series/mariadb-10-4-29-changelog.md)
* Merge [Revision #b735ca4773](https://github.com/MariaDB/server/commit/b735ca4773) 2023-05-05 10:50:02 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #ba0433dc1c](https://github.com/MariaDB/server/commit/ba0433dc1c) 2023-05-04 18:19:47 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #749c512911](https://github.com/MariaDB/server/commit/749c512911) 2023-05-04 11:23:37 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #e87440b79e](https://github.com/MariaDB/server/commit/e87440b79e) 2023-05-03 15:53:14 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #69932b6e68](https://github.com/MariaDB/server/commit/69932b6e68) 2023-05-03 09:46:49 +0200 - Merge branch '10.4' into 10.5
* [Revision #8c793eaaf4](https://github.com/MariaDB/server/commit/8c793eaaf4)\
  2023-05-03 07:30:12 +0200
  * Fix test after merge (by Thiru)
* Merge [Revision #46ebddba61](https://github.com/MariaDB/server/commit/46ebddba61) 2023-05-02 20:16:14 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #10e135b679](https://github.com/MariaDB/server/commit/10e135b679) 2023-05-02 15:47:10 +0200 - Merge branch 'bb-10.4-release' into bb-10.5-release
* [Revision #495f1ecac2](https://github.com/MariaDB/server/commit/495f1ecac2)\
  2023-05-02 15:52:36 +0300
  * [MDEV-29621](https://jira.mariadb.org/browse/MDEV-29621) manual merge from 10.4 -> 10.5
* Merge [Revision #edf8ce5b97](https://github.com/MariaDB/server/commit/edf8ce5b97) 2023-05-02 13:54:54 +0200 - Merge branch 'bb-10.4-release' into bb-10.5-release
* Merge [Revision #d821fd7fab](https://github.com/MariaDB/server/commit/d821fd7fab) 2023-04-28 08:22:17 +0200 - Merge branch 'merge-perfschema-5.7' into 10.5
* [Revision #512dbc4527](https://github.com/MariaDB/server/commit/512dbc4527)\
  2023-04-28 08:09:26 +0200
  * 5.7.42 (only copyright year in all files changed)
* Merge [Revision #902c622215](https://github.com/MariaDB/server/commit/902c622215) 2023-04-27 09:39:53 +0300 - Merge 10.4 into 10.5
* [Revision #6fccf8ba05](https://github.com/MariaDB/server/commit/6fccf8ba05)\
  2023-04-27 16:14:05 +1000
  * [MDEV-29644](https://jira.mariadb.org/browse/MDEV-29644) post-merge fixup
* [Revision #50f3b7d164](https://github.com/MariaDB/server/commit/50f3b7d164)\
  2023-04-25 12:17:06 +0300
  * [MDEV-31124](https://jira.mariadb.org/browse/MDEV-31124) Innodb\_data\_written miscounts doublewrites
* [Revision #31f09e36c1](https://github.com/MariaDB/server/commit/31f09e36c1)\
  2023-04-18 13:22:43 -0600
  * [MDEV-31038](https://jira.mariadb.org/browse/MDEV-31038): Parallel Replication Breaks if XA PREPARE Fails Updating Slave GTID State
* Merge [Revision #1d74927c58](https://github.com/MariaDB/server/commit/1d74927c58) 2023-04-24 12:43:47 +0200 - Merge branch '10.4' into 10.5
* [Revision #c6e58a8d17](https://github.com/MariaDB/server/commit/c6e58a8d17)\
  2023-04-21 11:05:44 +0300
  * [MDEV-30753](https://jira.mariadb.org/browse/MDEV-30753) fixup: Unsafe buffer page restoration
* [Revision #210db2935c](https://github.com/MariaDB/server/commit/210db2935c)\
  2023-03-14 14:08:12 +0300
  * [MDEV-30804](https://jira.mariadb.org/browse/MDEV-30804) Rollback multi-engine transaction requiring 2PC but committing in one phase
* [Revision #75063d1288](https://github.com/MariaDB/server/commit/75063d1288)\
  2023-04-04 15:54:26 +1000
  * [MDEV-30542](https://jira.mariadb.org/browse/MDEV-30542) Add multilength spider self-reference detection test
* [Revision #be7ef6566f](https://github.com/MariaDB/server/commit/be7ef6566f)\
  2023-03-28 10:25:59 +0300
  * [MDEV-30605](https://jira.mariadb.org/browse/MDEV-30605): Wrong result while using index for group-by
* [Revision #6c196090c8](https://github.com/MariaDB/server/commit/6c196090c8)\
  2023-04-13 20:13:13 +0300
  * Fix compilation on gcc 11.2.0
* [Revision #fb72dfbf7f](https://github.com/MariaDB/server/commit/fb72dfbf7f)\
  2023-04-06 09:45:05 +0400
  * [MDEV-30415](https://jira.mariadb.org/browse/MDEV-30415) [MDEV-30415](https://jira.mariadb.org/browse/MDEV-30415) PERIOD false positive overlap wtih utf8mb4\_unicode\_nopad\_ci
* Merge [Revision #62e137d4d7](https://github.com/MariaDB/server/commit/62e137d4d7) 2023-04-05 15:42:27 +0400 - Merge remote-tracking branch 'origin/10.4' into 10.5
* [Revision #afdf19cf33](https://github.com/MariaDB/server/commit/afdf19cf33)\
  2023-04-04 03:11:41 +0200
  * [MDEV-28641](https://jira.mariadb.org/browse/MDEV-28641) : Query cache entries not invalidated on slave of a Galera cluster
* Merge [Revision #3261a78ea1](https://github.com/MariaDB/server/commit/3261a78ea1) 2023-04-03 09:34:26 +0200 - Merge branch '10.4' into 10.5
* Merge [Revision #ac5a534a4c](https://github.com/MariaDB/server/commit/ac5a534a4c) 2023-03-31 21:32:41 +0200 - Merge remote-tracking branch '10.4' into 10.5
* [Revision #e093e5abbe](https://github.com/MariaDB/server/commit/e093e5abbe)\
  2022-12-15 12:38:27 +1100
  * [MDEV-30276](https://jira.mariadb.org/browse/MDEV-30276) - wsrep\_sst\_mariadb-backup to use mariadb-backup
* [Revision #402f36dd65](https://github.com/MariaDB/server/commit/402f36dd65)\
  2023-03-28 15:10:32 +0300
  * [MDEV-30936](https://jira.mariadb.org/browse/MDEV-30936) fixup
* [Revision #dfa90257f6](https://github.com/MariaDB/server/commit/dfa90257f6)\
  2023-03-28 11:44:24 +0300
  * [MDEV-30936](https://jira.mariadb.org/browse/MDEV-30936) clang 15.0.7 -fsanitize=memory fails massively
* [Revision #a8b616d1e9](https://github.com/MariaDB/server/commit/a8b616d1e9)\
  2023-03-23 22:31:55 +0300
  * [MDEV-30421](https://jira.mariadb.org/browse/MDEV-30421) rpl\_parallel\_\*.test cleanup
* [Revision #701399ad37](https://github.com/MariaDB/server/commit/701399ad37)\
  2023-03-22 15:19:52 +0200
  * [MDEV-30882](https://jira.mariadb.org/browse/MDEV-30882) Crash on ROLLBACK in a ROW\_FORMAT=COMPRESSED table
* [Revision #dccbb5a6db](https://github.com/MariaDB/server/commit/dccbb5a6db)\
  2023-03-15 19:14:01 +0000
  * \[[MDEV-30824](https://jira.mariadb.org/browse/MDEV-30824)] Fix binlog to use 'String' for setting 'character\_set\_client'
* [Revision #1495f057c8](https://github.com/MariaDB/server/commit/1495f057c8)\
  2023-03-16 13:39:23 +0200
  * [MDEV-30860](https://jira.mariadb.org/browse/MDEV-30860) Race condition between buffer pool flush and log file deletion in mariadb-backup --prepare
* [Revision #7d6b3d4008](https://github.com/MariaDB/server/commit/7d6b3d4008)\
  2023-03-06 19:09:13 +0300
  * [MDEV-30775](https://jira.mariadb.org/browse/MDEV-30775) Performance regression in fil\_space\_t::try\_to\_close() introduced in [MDEV-23855](https://jira.mariadb.org/browse/MDEV-23855)
* [Revision #08267ba0c8](https://github.com/MariaDB/server/commit/08267ba0c8)\
  2023-03-09 16:16:58 +0200
  * [MDEV-30819](https://jira.mariadb.org/browse/MDEV-30819) InnoDB fails to start up after downgrading from [MariaDB 11.0](../../old-releases/11.0/what-is-mariadb-110.md)
* [Revision #231c0eb7a6](https://github.com/MariaDB/server/commit/231c0eb7a6)\
  2023-03-02 21:21:46 +0100
  * [MDEV-23000](https://jira.mariadb.org/browse/MDEV-23000): Ensure we get a warning from THD::drop\_temporary\_table() in case of disk errors
* [Revision #1e58b8afc0](https://github.com/MariaDB/server/commit/1e58b8afc0)\
  2023-03-07 11:13:20 +0100
  * move alloca() definition from all \*.h files to one new header file
* [Revision #b1646d0433](https://github.com/MariaDB/server/commit/b1646d0433)\
  2023-03-06 17:17:32 +0200
  * [MDEV-30567](https://jira.mariadb.org/browse/MDEV-30567) rec\_get\_offsets() is not optimal
* [Revision #948fb3c27d](https://github.com/MariaDB/server/commit/948fb3c27d)\
  2023-03-06 12:01:15 +0200
  * Fix GCC 5.3.1 -Wsign-compare
* [Revision #6d923362bd](https://github.com/MariaDB/server/commit/6d923362bd)\
  2023-02-28 20:03:38 +0100
  * [CONC-637](https://jira.mariadb.org/browse/CONC-637) Build fails when specifying -DPLUGIN\_AUTH\_GSSAPI\_CLIENT=OFF
* [Revision #c14a39431b](https://github.com/MariaDB/server/commit/c14a39431b)\
  2023-02-28 15:39:23 +0200
  * [MDEV-30753](https://jira.mariadb.org/browse/MDEV-30753) Possible corruption due to trx\_purge\_free\_segment()
* [Revision #57c526ffb8](https://github.com/MariaDB/server/commit/57c526ffb8)\
  2023-02-26 18:33:10 +0200
  * Added detection of memory overwrite with multi\_malloc
* [Revision #0de3be8cfd](https://github.com/MariaDB/server/commit/0de3be8cfd)\
  2023-02-24 14:24:44 +0200
  * [MDEV-30671](https://jira.mariadb.org/browse/MDEV-30671) InnoDB undo log truncation fails to wait for purge of history
* [Revision #d3f35aa47b](https://github.com/MariaDB/server/commit/d3f35aa47b)\
  2023-02-16 10:16:38 +0200
  * [MDEV-30552](https://jira.mariadb.org/browse/MDEV-30552) fixup: Fix the test for non-debug
* [Revision #0c79ae9462](https://github.com/MariaDB/server/commit/0c79ae9462)\
  2023-02-16 10:09:19 +0200
  * Fix clang -Winconsistent-missing-override
* [Revision #5300c0fb76](https://github.com/MariaDB/server/commit/5300c0fb76)\
  2023-02-15 18:16:41 +0200
  * [MDEV-30657](https://jira.mariadb.org/browse/MDEV-30657) InnoDB: Not applying UNDO\_APPEND due to corruption
* [Revision #192427e37d](https://github.com/MariaDB/server/commit/192427e37d)\
  2023-02-15 13:56:33 +0200
  * [MDEV-30333](https://jira.mariadb.org/browse/MDEV-30333) Wrong result with not\_null\_range\_scan and LEFT JOIN with empty table
* [Revision #690fcfbd29](https://github.com/MariaDB/server/commit/690fcfbd29)\
  2023-01-18 16:16:34 +0000
  * Fix S3 engine Coverity hits
* [Revision #1a5c7552ea](https://github.com/MariaDB/server/commit/1a5c7552ea)\
  2023-02-14 14:36:17 +0530
  * [MDEV-30552](https://jira.mariadb.org/browse/MDEV-30552) InnoDB recovery crashes when error handling scenario
* [Revision #3eea2e8e10](https://github.com/MariaDB/server/commit/3eea2e8e10)\
  2023-02-14 14:35:35 +0530
  * [MDEV-30551](https://jira.mariadb.org/browse/MDEV-30551) InnoDB recovery hangs when buffer pool ran out of memory
* [Revision #badf6de171](https://github.com/MariaDB/server/commit/badf6de171)\
  2023-02-12 18:42:23 +0100
  * [MDEV-30412](https://jira.mariadb.org/browse/MDEV-30412): JSON\_OBJECTAGG doesn't escape double quote in key
* Merge [Revision #c41c79650a](https://github.com/MariaDB/server/commit/c41c79650a) 2023-02-10 12:02:11 +0200 - Merge 10.4 into 10.5
* [Revision #a9eb272f91](https://github.com/MariaDB/server/commit/a9eb272f91)\
  2023-02-01 09:49:58 +0200
  * [MDEV-30534](https://jira.mariadb.org/browse/MDEV-30534): Remove EOL Debian version 9 (stretch) from autobake-deb.sh
* [Revision #2b494ccc15](https://github.com/MariaDB/server/commit/2b494ccc15)\
  2023-02-06 18:00:15 +1100
  * [MDEV-30572](https://jira.mariadb.org/browse/MDEV-30572): my\_large\_malloc will only retry on ENOMEM
* [Revision #acd23da4c2](https://github.com/MariaDB/server/commit/acd23da4c2)\
  2023-02-06 20:29:42 +0200
  * [MDEV-30479](https://jira.mariadb.org/browse/MDEV-30479) optimization: Invoke recv\_sys\_t::trim() earlier
* [Revision #461402a564](https://github.com/MariaDB/server/commit/461402a564)\
  2023-02-06 20:29:29 +0200
  * [MDEV-30479](https://jira.mariadb.org/browse/MDEV-30479) OPT\_PAGE\_CHECKSUM mismatch after innodb\_undo\_log\_truncate=ON
* Merge [Revision #ff12a5b897](https://github.com/MariaDB/server/commit/ff12a5b897) 2023-02-06 17:55:01 +0200 - Merge mariadb-10.5.19 into 10.5
* [Revision #f6da6b249e](https://github.com/MariaDB/server/commit/f6da6b249e)\
  2023-02-06 09:59:18 -0500
  * bump the VERSION
* [Revision #4a04c18af9](https://github.com/MariaDB/server/commit/4a04c18af9)\
  2022-11-14 16:43:33 +0400
  * [MDEV-25765](https://jira.mariadb.org/browse/MDEV-25765) mariadb-backup reduced verbosity option for log output
* [Revision #50b69641ef](https://github.com/MariaDB/server/commit/50b69641ef)\
  2022-11-14 16:17:03 +0400
  * [MDEV-29244](https://jira.mariadb.org/browse/MDEV-29244) mariadb-backup --help output still referst to innobackupex
* [Revision #49ee18eb42](https://github.com/MariaDB/server/commit/49ee18eb42)\
  2023-01-27 10:40:07 +0200
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster
* [Revision #696562ce55](https://github.com/MariaDB/server/commit/696562ce55)\
  2023-01-26 14:34:12 +0200
  * [MDEV-30473](https://jira.mariadb.org/browse/MDEV-30473) : Do not allow GET\_LOCK() / RELEASE\_LOCK() in cluster
* [Revision #015fb54d45](https://github.com/MariaDB/server/commit/015fb54d45)\
  2023-01-26 10:27:31 +0200
  * [MDEV-25037](https://jira.mariadb.org/browse/MDEV-25037) : SIGSEGV in MDL\_lock::hog\_lock\_types\_bitmap
* [Revision #75bbf645a6](https://github.com/MariaDB/server/commit/75bbf645a6)\
  2023-01-24 21:40:43 -0800
  * Add missing include

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
