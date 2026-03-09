# MariaDB 10.3.38 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/10.3/10.3.38.md)[Changelog](mariadb-10-3-38-changelog.md)[Overview of 10.3](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/10.3.38/)

**Release date:** 6 Feb 2023

For the highlights of this release, see the [release notes](../../old-releases/10.3/10.3.38.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/10.3) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 10.2.44](../changelogs-mariadb-102-series/mariadb-10244-changelog.md)
* [Revision #c73985f2ce](https://github.com/MariaDB/server/commit/c73985f2ce)\
  2023-01-28 14:30:46 +0200
  * [MDEV-30010](https://jira.mariadb.org/browse/MDEV-30010) post-push: fixing test results.
* [Revision #2279dddad6](https://github.com/MariaDB/server/commit/2279dddad6)\
  2023-01-24 19:41:29 +0100
  * [MDEV-30457](https://jira.mariadb.org/browse/MDEV-30457) Windows, signtool error "No file digest algorithm specified."
* [Revision #7fe932444d](https://github.com/MariaDB/server/commit/7fe932444d)\
  2023-01-05 20:08:01 +0200
  * [MDEV-30323](https://jira.mariadb.org/browse/MDEV-30323) Some DDLs like ANALYZE can complete on parallel slave out of order
* [Revision #3aa04c0deb](https://github.com/MariaDB/server/commit/3aa04c0deb)\
  2023-01-24 19:35:16 +0200
  * [MDEV-30010](https://jira.mariadb.org/browse/MDEV-30010) Slave (additional info): Commit failed due to failure of an earlier commit on which this one depends Error\_code: 1964
* [Revision #f513d71538](https://github.com/MariaDB/server/commit/f513d71538)\
  2023-01-23 15:54:49 -0800
  * [MDEV-30081](https://jira.mariadb.org/browse/MDEV-30081) Crash with splitting from constant mergeable derived table
* [Revision #d69e835787](https://github.com/MariaDB/server/commit/d69e835787)\
  2022-11-03 14:56:50 -0600
  * [MDEV-29639](https://jira.mariadb.org/browse/MDEV-29639): Seconds\_Behind\_Master is incorrect for Delayed, Parallel Replicas
* [Revision #2ed598eae8](https://github.com/MariaDB/server/commit/2ed598eae8)\
  2023-01-24 13:30:22 +0200
  * Added comments re JOIN::all\_fields, JOIN::fields\_list
* [Revision #c45630327c](https://github.com/MariaDB/server/commit/c45630327c)\
  2023-01-23 10:38:27 +0200
  * Update 10.3 HELP tables
* [Revision #074bef4dca](https://github.com/MariaDB/server/commit/074bef4dca)\
  2023-01-21 00:09:58 -0800
  * [MDEV-30248](https://jira.mariadb.org/browse/MDEV-30248) Infinite sequence of recursive calls when processing embedded CTE
* [Revision #f18c2b6c8a](https://github.com/MariaDB/server/commit/f18c2b6c8a)\
  2023-01-23 13:10:24 +0200
  * [MDEV-15178](https://jira.mariadb.org/browse/MDEV-15178): Filesort::make\_sortorder: Assertion \`pos->field != null |
* [Revision #00150ff8d4](https://github.com/MariaDB/server/commit/00150ff8d4)\
  2023-01-19 06:52:54 +0200
  * Fix connect bson.cpp warning
* [Revision #244bf37c73](https://github.com/MariaDB/server/commit/244bf37c73)\
  2023-01-19 06:49:47 +0200
  * Fix mroonga warning of use-after-free
* [Revision #567b681299](https://github.com/MariaDB/server/commit/567b681299)\
  2022-11-15 14:39:30 -0800
  * Minimize unsafe C functions usage - replace strcat() and strcpy() (and strncat() and strncpy()) with custom safe\_strcat() and safe\_strcpy() functions
* [Revision #ea270178b0](https://github.com/MariaDB/server/commit/ea270178b0)\
  2023-01-19 21:43:29 +0100
  * [MDEV-30052](https://jira.mariadb.org/browse/MDEV-30052) Crash with a query containing nested WINDOW clauses
* [Revision #6fe882cd85](https://github.com/MariaDB/server/commit/6fe882cd85)\
  2023-01-19 17:53:51 +0100
  * Add my\_afree after my\_alloca in early return case
* [Revision #0ddbec40fb](https://github.com/MariaDB/server/commit/0ddbec40fb)\
  2022-11-09 16:41:19 +0400
  * [MDEV-23335](https://jira.mariadb.org/browse/MDEV-23335) mariadb-backup Incremental Does Not Reflect Dropped/Created Databases
* [Revision #489b556947](https://github.com/MariaDB/server/commit/489b556947)\
  2023-01-17 17:52:16 +0200
  * [MDEV-30422](https://jira.mariadb.org/browse/MDEV-30422) Merge new release of InnoDB 5.7.41 to 10.3
* [Revision #834650c7cf](https://github.com/MariaDB/server/commit/834650c7cf)\
  2023-01-16 14:59:59 +0100
  * New CC 3.1
* [Revision #7a98d232e4](https://github.com/MariaDB/server/commit/7a98d232e4)\
  2023-01-11 18:57:44 +0300
  * [MDEV-30378](https://jira.mariadb.org/browse/MDEV-30378) Versioned REPLACE succeeds with ON DELETE RESTRICT constraint
* [Revision #eb145e5ad7](https://github.com/MariaDB/server/commit/eb145e5ad7)\
  2023-01-12 10:38:38 +0800
  * fix typos
* [Revision #b194c83b7b](https://github.com/MariaDB/server/commit/b194c83b7b)\
  2021-06-03 11:24:34 -0600
  * [MDEV-25277](https://jira.mariadb.org/browse/MDEV-25277): mysqlbinlog --verbose cannot read row events with compressed columns: Don't know how to handle column type: 140
* [Revision #53c4be7bc0](https://github.com/MariaDB/server/commit/53c4be7bc0)\
  2022-12-13 15:44:24 +0100
  * [MDEV-30220](https://jira.mariadb.org/browse/MDEV-30220): rsync SST completely ignores aria-log-dir-path
* [Revision #b84f3fa769](https://github.com/MariaDB/server/commit/b84f3fa769)\
  2022-12-13 14:59:24 +0100
  * [MDEV-30157](https://jira.mariadb.org/browse/MDEV-30157): Galera SST doesn't properly handle undo\* files from innodb
* [Revision #e4a4aad7cf](https://github.com/MariaDB/server/commit/e4a4aad7cf)\
  2022-12-13 10:32:21 +0100
  * pre-[MDEV-30157](https://jira.mariadb.org/browse/MDEV-30157) & pre-[MDEV-28669](https://jira.mariadb.org/browse/MDEV-28669): fixes before the main corrections
* [Revision #b928c849d2](https://github.com/MariaDB/server/commit/b928c849d2)\
  2023-01-04 13:01:47 +0300
  * [MDEV-28602](https://jira.mariadb.org/browse/MDEV-28602) Wrong result with outer join, merged derived table and view
* [Revision #b218dfead2](https://github.com/MariaDB/server/commit/b218dfead2)\
  2023-01-11 08:37:27 +0200
  * Remove an unused parameter
* [Revision #56948ee54c](https://github.com/MariaDB/server/commit/56948ee54c)\
  2023-01-10 10:45:03 +1100
  * clang15 warnings - unused vars and old prototypes
* [Revision #d7f447915c](https://github.com/MariaDB/server/commit/d7f447915c)\
  2023-01-08 09:53:09 +1100
  * [MDEV-30342](https://jira.mariadb.org/browse/MDEV-30342) Wrong "Truncated incorrect DECIMAL value" warning/error
* [Revision #e64e6768e0](https://github.com/MariaDB/server/commit/e64e6768e0)\
  2023-01-08 09:26:50 +1100
  * [MDEV-17093](https://jira.mariadb.org/browse/MDEV-17093): SOURCE\_REVISION in log (postfix - not in help)
* [Revision #b21832ef15](https://github.com/MariaDB/server/commit/b21832ef15)\
  2022-10-26 22:08:32 -0700
  * [MDEV-27624](https://jira.mariadb.org/browse/MDEV-27624) Wrong result for nested left join using not\_exists optimization
* [Revision #af0ff8b455](https://github.com/MariaDB/server/commit/af0ff8b455)\
  2022-12-08 19:34:00 +0000
  * [MDEV-17093](https://jira.mariadb.org/browse/MDEV-17093): SOURCE\_REVISION in log and handle\_fatal\_signal
* [Revision #758c24dae2](https://github.com/MariaDB/server/commit/758c24dae2)\
  2023-01-04 18:32:54 +0800
  * fix typos
* [Revision #e51a1d6fc0](https://github.com/MariaDB/server/commit/e51a1d6fc0)\
  2023-01-03 10:48:57 +1100
  * [MDEV-30329](https://jira.mariadb.org/browse/MDEV-30329): mariadb-service-convert resets systemd service to default User=root
* [Revision #21223c0461](https://github.com/MariaDB/server/commit/21223c0461)\
  2022-12-18 16:30:26 +0100
  * [MDEV-29988](https://jira.mariadb.org/browse/MDEV-29988) group by fix
* [Revision #908c48a34d](https://github.com/MariaDB/server/commit/908c48a34d)\
  2022-12-18 14:30:36 +0100
  * fixes for json.json\_table and main.func\_json in --ps
* [Revision #60f646e2f3](https://github.com/MariaDB/server/commit/60f646e2f3)\
  2022-12-14 14:36:27 +0100
  * [MDEV-29988](https://jira.mariadb.org/browse/MDEV-29988): (spider fix) Major performance regression with 10.6.11
* [Revision #37a316c01d](https://github.com/MariaDB/server/commit/37a316c01d)\
  2022-12-09 21:10:25 +0700
  * [MDEV-29988](https://jira.mariadb.org/browse/MDEV-29988): Major performance regression with 10.6.11
* [Revision #a9b31b0814](https://github.com/MariaDB/server/commit/a9b31b0814)\
  2022-12-09 11:50:05 +0700
  * [MDEV-29988](https://jira.mariadb.org/browse/MDEV-29988): (revert) Major performance regression with 10.6.11
* [Revision #8760f6907c](https://github.com/MariaDB/server/commit/8760f6907c)\
  2022-12-28 12:10:38 +0100
  * [MDEV-30102](https://jira.mariadb.org/browse/MDEV-30102) file missing in development libraries
* [Revision #ca23558a05](https://github.com/MariaDB/server/commit/ca23558a05)\
  2022-12-12 13:18:46 +0100
  * \--skip-name-resolve=0 didn't work
* [Revision #d78ac04ee6](https://github.com/MariaDB/server/commit/d78ac04ee6)\
  2022-12-09 14:32:58 +0100
  * ignore changes in submodules when committing everything
* [Revision #eba099184e](https://github.com/MariaDB/server/commit/eba099184e)\
  2022-12-05 00:21:28 +0100
  * [MDEV-30151](https://jira.mariadb.org/browse/MDEV-30151) parse error 1=2 not between/in
* [Revision #f8adc47b69](https://github.com/MariaDB/server/commit/f8adc47b69)\
  2022-12-06 15:48:13 +0100
  * [MDEV-19071](https://jira.mariadb.org/browse/MDEV-19071) Wrong results when using STDDEV\_SAMP() and view
* [Revision #6710fe4b42](https://github.com/MariaDB/server/commit/6710fe4b42)\
  2022-12-26 08:23:16 +0100
  * [MDEV-30293](https://jira.mariadb.org/browse/MDEV-30293): mariadb-backup fail with --galera-info option without Galera
* [Revision #72e2d1d220](https://github.com/MariaDB/server/commit/72e2d1d220)\
  2022-12-27 00:02:02 +0300
  * [MDEV-25004](https://jira.mariadb.org/browse/MDEV-25004) Refactorings
* [Revision #e056efdd6c](https://github.com/MariaDB/server/commit/e056efdd6c)\
  2022-12-27 00:02:02 +0300
  * [MDEV-25004](https://jira.mariadb.org/browse/MDEV-25004) Missing row in FTS\_DOC\_ID\_INDEX during DELETE HISTORY
* [Revision #68c437bad6](https://github.com/MariaDB/server/commit/68c437bad6)\
  2022-12-27 00:02:01 +0300
  * [MDEV-25004](https://jira.mariadb.org/browse/MDEV-25004) restart\_bindir option to restart server from different location
* [Revision #5d506ac201](https://github.com/MariaDB/server/commit/5d506ac201)\
  2022-12-27 00:02:01 +0300
  * [MDEV-25004](https://jira.mariadb.org/browse/MDEV-25004) vers\_force\_trx option to force transactional System Versioning
* [Revision #7c5609fb64](https://github.com/MariaDB/server/commit/7c5609fb64)\
  2022-12-20 17:41:24 -0600
  * typos
* [Revision #3ddc00dc3b](https://github.com/MariaDB/server/commit/3ddc00dc3b)\
  2022-12-13 16:06:13 +0300
  * [MDEV-30225](https://jira.mariadb.org/browse/MDEV-30225) RR isolation violation with locking unique search
* [Revision #3f63aa18a7](https://github.com/MariaDB/server/commit/3f63aa18a7)\
  2022-12-07 20:19:05 +1100
  * [MDEV-29562](https://jira.mariadb.org/browse/MDEV-29562) Spider table charset error should happen correctly.
* [Revision #e9e6c7a3c5](https://github.com/MariaDB/server/commit/e9e6c7a3c5)\
  2022-12-19 15:08:20 -0600
  * header typos
* [Revision #0ca3aaa75f](https://github.com/MariaDB/server/commit/0ca3aaa75f)\
  2022-12-15 16:12:49 +0000
  * [MDEV-27691](https://jira.mariadb.org/browse/MDEV-27691): make working view-protocol
* [Revision #9f8fc983d5](https://github.com/MariaDB/server/commit/9f8fc983d5)\
  2022-12-16 09:59:09 +0200
  * [MDEV-30242](https://jira.mariadb.org/browse/MDEV-30242) MTR fails to report stack traces of all threads by default
* [Revision #d0f6d46704](https://github.com/MariaDB/server/commit/d0f6d46704)\
  2022-11-25 17:32:16 -0600
  * debian typos
* [Revision #c562ccf796](https://github.com/MariaDB/server/commit/c562ccf796)\
  2022-12-15 11:14:23 +0200
  * [MDEV-30233](https://jira.mariadb.org/browse/MDEV-30233) DROP DATABASE test fails: Directory not empty
* [Revision #697dbd15e0](https://github.com/MariaDB/server/commit/697dbd15e0)\
  2022-12-04 10:47:31 +1100
  * [MDEV-21187](https://jira.mariadb.org/browse/MDEV-21187): log\_slow\_filter="" logs queries not using indexes
* [Revision #acfaa04587](https://github.com/MariaDB/server/commit/acfaa04587)\
  2022-12-14 01:17:44 +1100
  * [MDEV-18591](https://jira.mariadb.org/browse/MDEV-18591): mysql\_install\_db - pass --log-error to mysqld in install (#2363)
* [Revision #8f30973234](https://github.com/MariaDB/server/commit/8f30973234)\
  2022-10-28 11:16:25 +0200
  * [MDEV-29814](https://jira.mariadb.org/browse/MDEV-29814): galera\_var\_notify\_ssl\_ipv6 causes testing system to hang
* [Revision #782b2a7500](https://github.com/MariaDB/server/commit/782b2a7500)\
  2022-12-09 10:42:19 +0200
  * [MDEV-29144](https://jira.mariadb.org/browse/MDEV-29144) ER\_TABLE\_SCHEMA\_MISMATCH or crash on DISCARD/IMPORT
* [Revision #8f3631d009](https://github.com/MariaDB/server/commit/8f3631d009)\
  2022-12-03 15:09:48 +1100
  * [MDEV-30150](https://jira.mariadb.org/browse/MDEV-30150) ST\_GeomFromGeoJSON, 'geometry' before 'type: feature' error
* [Revision #d360fa6fa8](https://github.com/MariaDB/server/commit/d360fa6fa8)\
  2022-12-05 15:07:50 +0100
  * [MDEV-30162](https://jira.mariadb.org/browse/MDEV-30162) Fix occasional "Permission denied" on Windows caused by buggy 3rd party
* [Revision #2beede9ba4](https://github.com/MariaDB/server/commit/2beede9ba4)\
  2022-09-27 12:01:29 +0900
  * [MDEV-29636](https://jira.mariadb.org/browse/MDEV-29636) Assertion \`part\_share->auto\_inc\_initialized || !can\_use\_for\_auto\_inc\_init()' failed in ha\_partition::set\_auto\_increment\_if\_higher upon REPLACE with partition pruning
* [Revision #a59dffb0e9](https://github.com/MariaDB/server/commit/a59dffb0e9)\
  2022-12-05 11:13:21 +0100
  * dgcov: parsing without dot to get specific version
* [Revision #180b2bcd53](https://github.com/MariaDB/server/commit/180b2bcd53)\
  2022-12-04 00:31:29 +0100
  * dgcov: also remove rpm dependency on IO::Uncompress::Gunzip
* [Revision #7baf24a0f8](https://github.com/MariaDB/server/commit/7baf24a0f8)\
  2022-12-01 20:24:12 +0100
  * [MDEV-26102](https://jira.mariadb.org/browse/MDEV-26102) followup
* [Revision #43173ef261](https://github.com/MariaDB/server/commit/43173ef261)\
  2021-07-27 16:09:30 +0200
  * [MDEV-26102](https://jira.mariadb.org/browse/MDEV-26102) dgcov: add support for \*.gcda.gcov.json.gz files of gcov 9.1+
* [Revision #1547e55489](https://github.com/MariaDB/server/commit/1547e55489)\
  2022-11-30 22:49:44 +0100
  * fix more sporadic failures on main.kill
* [Revision #401ae95a60](https://github.com/MariaDB/server/commit/401ae95a60)\
  2022-11-27 19:50:02 +0100
  * [MDEV-30082](https://jira.mariadb.org/browse/MDEV-30082) View definition losing brackets changes semantics of the query and causes wrong result
* [Revision #37bfe32c6d](https://github.com/MariaDB/server/commit/37bfe32c6d)\
  2022-11-27 00:03:04 +0100
  * try harder to reject not strictly deterministic vcols in indexes/stored
* [Revision #ae53f684d3](https://github.com/MariaDB/server/commit/ae53f684d3)\
  2022-11-27 14:09:01 +0100
  * [MDEV-30016](https://jira.mariadb.org/browse/MDEV-30016) Virtual columns do not support autoincrement columns
* [Revision #a6b327e90a](https://github.com/MariaDB/server/commit/a6b327e90a)\
  2022-11-26 13:39:25 +0100
  * cleanup: VCOL\_NOT\_VIRTUAL->VCOL\_NEXTVAL
* [Revision #53e57a8681](https://github.com/MariaDB/server/commit/53e57a8681)\
  2022-11-25 19:04:31 +0100
  * [MDEV-30056](https://jira.mariadb.org/browse/MDEV-30056) Impossible to export column grants
* [Revision #f915681d2f](https://github.com/MariaDB/server/commit/f915681d2f)\
  2022-11-25 17:52:56 +0100
  * [MDEV-30036](https://jira.mariadb.org/browse/MDEV-30036) NULL pointer dereference in partition\_info::set\_partition\_bitmaps\_from\_table
* [Revision #c7c1461b94](https://github.com/MariaDB/server/commit/c7c1461b94)\
  2022-11-24 21:51:19 +0100
  * fix embedded startup with no command line arguments
* [Revision #cfb47ddde2](https://github.com/MariaDB/server/commit/cfb47ddde2)\
  2022-11-23 00:58:07 +0100
  * [MDEV-30066](https://jira.mariadb.org/browse/MDEV-30066) (limit + offset) union all (...) limit = incorrect result
* [Revision #da3fc33e88](https://github.com/MariaDB/server/commit/da3fc33e88)\
  2022-11-23 00:35:14 +0100
  * cleanup: union.test
* [Revision #d08f2ab6d6](https://github.com/MariaDB/server/commit/d08f2ab6d6)\
  2022-11-01 19:50:20 +0100
  * [MDEV-28855](https://jira.mariadb.org/browse/MDEV-28855) SEGV around dict\_free\_vc\_templ during DROP INDEX
* [Revision #4fb8f7d07a](https://github.com/MariaDB/server/commit/4fb8f7d07a)\
  2022-11-01 20:46:48 +0100
  * cleanup: clarify innobase\_init\_vc\_templ usage
* [Revision #126619047a](https://github.com/MariaDB/server/commit/126619047a)\
  2022-12-02 11:59:36 +0100
  * [MDEV-28643](https://jira.mariadb.org/browse/MDEV-28643): view protocol fails due to different column name
* [Revision #b91b4e0b97](https://github.com/MariaDB/server/commit/b91b4e0b97)\
  2022-12-01 15:04:59 +0400
  * [MDEV-28696](https://jira.mariadb.org/browse/MDEV-28696) View created as "select b''; " references invalid table(s) or column(s) or function(s) or definer/invoker of view lack rights to use them
* [Revision #cc86360f4a](https://github.com/MariaDB/server/commit/cc86360f4a)\
  2022-12-01 16:34:17 +0300
  * [MDEV-30112](https://jira.mariadb.org/browse/MDEV-30112) ASAN errors in Item\_ident::print / generate\_partition\_syntax
* [Revision #b527bfe823](https://github.com/MariaDB/server/commit/b527bfe823)\
  2022-11-24 19:50:14 +0200
  * [MDEV-30023](https://jira.mariadb.org/browse/MDEV-30023) Revoking Privilege on the Column Yields the Error
* [Revision #6c973be2e9](https://github.com/MariaDB/server/commit/6c973be2e9)\
  2022-11-28 16:29:20 +0100
  * [MDEV-28299](https://jira.mariadb.org/browse/MDEV-28299): Server crashes in XINDXS::Range/CntIndexRange (Connect engine)
* [Revision #9a95838a96](https://github.com/MariaDB/server/commit/9a95838a96)\
  2022-11-29 05:27:56 -0800
  * \[[MDEV-30002](https://jira.mariadb.org/browse/MDEV-30002)] Skip bad\_startup\_options test when running as root (#2344)
* [Revision #499ef7bf23](https://github.com/MariaDB/server/commit/499ef7bf23)\
  2022-11-29 11:06:29 +0200
  * Add a global suppression for O\_DIRECT failures
* [Revision #b8ad6fbd95](https://github.com/MariaDB/server/commit/b8ad6fbd95)\
  2022-11-28 18:37:55 +0200
  * Fixed warning from innodb.create\_isl\_with\_direct if have\_symlink is disabled
* [Revision #f208f6fb6f](https://github.com/MariaDB/server/commit/f208f6fb6f)\
  2022-11-28 18:07:43 +0200
  * Safety fix
* [Revision #f9c418c67d](https://github.com/MariaDB/server/commit/f9c418c67d)\
  2022-11-28 16:17:31 +0200
  * Fixed the BUILD scripts to work outside of a git repository
* [Revision #5b275b41aa](https://github.com/MariaDB/server/commit/5b275b41aa)\
  2022-10-18 13:02:32 +0300
  * Enable valgrind for replication test
* [Revision #112870d7b4](https://github.com/MariaDB/server/commit/112870d7b4)\
  2022-11-28 21:20:23 +0000
  * [MDEV-16735](https://jira.mariadb.org/browse/MDEV-16735) Ensure mysql\_upgrade works when changing alter\_algorithm
* [Revision #3d5ce0430b](https://github.com/MariaDB/server/commit/3d5ce0430b)\
  2022-08-28 14:46:14 +0200
  * [MDEV-29348](https://jira.mariadb.org/browse/MDEV-29348) rpl.rpl\_rewrt\_db test fails with \[gdb,manual-gdb] with wrong parsing
* [Revision #4e9206736c](https://github.com/MariaDB/server/commit/4e9206736c)\
  2022-07-01 21:41:45 +0900
  * [MDEV-28996](https://jira.mariadb.org/browse/MDEV-28996) ASAN errors in String::q\_append / spider\_string::q\_append / spider\_db\_mbase\_util::open\_item\_func
* [Revision #162c150505](https://github.com/MariaDB/server/commit/162c150505)\
  2022-10-23 19:59:34 +0900
  * [MDEV-29855](https://jira.mariadb.org/browse/MDEV-29855) Crash with SPIDER\_DIRECT\_SQL and spider\_udf\_ds\_use\_real\_table=1
* [Revision #d569e6dea4](https://github.com/MariaDB/server/commit/d569e6dea4)\
  2022-11-23 14:53:21 +0300
  * [MDEV-29169](https://jira.mariadb.org/browse/MDEV-29169) Using MATCH returns NULL for Virtual Column
* [Revision #f0820400ee](https://github.com/MariaDB/server/commit/f0820400ee)\
  2022-10-19 02:51:01 +0200
  * [MDEV-29817](https://jira.mariadb.org/browse/MDEV-29817): Issues with handling options for SSL CRLs (and some others)
* [Revision #71c93fb8fd](https://github.com/MariaDB/server/commit/71c93fb8fd)\
  2022-11-17 17:24:13 +0530
  * [MDEV-28462](https://jira.mariadb.org/browse/MDEV-28462) Race condition between instant alter and AHI access
* [Revision #f4a1298f24](https://github.com/MariaDB/server/commit/f4a1298f24)\
  2022-11-18 21:28:06 +1100
  * [MDEV-12274](https://jira.mariadb.org/browse/MDEV-12274): Too many connections warning in error log (#2213)
* [Revision #6216a2dfa2](https://github.com/MariaDB/server/commit/6216a2dfa2)\
  2022-11-17 17:51:01 +0400
  * [MDEV-29473](https://jira.mariadb.org/browse/MDEV-29473) UBSAN: Signed integer overflow: X \* Y cannot be represented in type 'int' in strings/dtoa.c
* [Revision #df4c3d96a4](https://github.com/MariaDB/server/commit/df4c3d96a4)\
  2022-11-10 12:09:16 +0530
  * [MDEV-29977](https://jira.mariadb.org/browse/MDEV-29977) Memory leak in row\_log\_table\_apply\_update
* [Revision #1895c769c2](https://github.com/MariaDB/server/commit/1895c769c2)\
  2022-11-14 16:22:11 +0200
  * Clean up file load.in in a test
* [Revision #043c1d1830](https://github.com/MariaDB/server/commit/043c1d1830)\
  2022-10-31 17:02:58 +0000
  * [MDEV-28489](https://jira.mariadb.org/browse/MDEV-28489) CONNECT used incorrect CHAR length
* [Revision #dc6a017111](https://github.com/MariaDB/server/commit/dc6a017111)\
  2022-11-07 15:58:40 +1100
  * [MDEV-27882](https://jira.mariadb.org/browse/MDEV-27882) Innodb - recognise MySQL-8.0 innodb flags and give a specific error message
* [Revision #0235a528e3](https://github.com/MariaDB/server/commit/0235a528e3)\
  2022-11-03 10:00:03 +0300
  * [MDEV-10087](https://jira.mariadb.org/browse/MDEV-10087) mysqld\_update()/mysql\_delete() continues execution even after subquery with JOIN gets error from storage engine
* [Revision #0ffdcf6784](https://github.com/MariaDB/server/commit/0ffdcf6784)\
  2022-11-07 14:56:09 +0000
  * MDEV 28970: Add RESET MASTER to clear possible remaining binlog from previous test
* [Revision #6b91792a08](https://github.com/MariaDB/server/commit/6b91792a08)\
  2022-11-09 09:23:18 +0200
  * [MDEV-29883](https://jira.mariadb.org/browse/MDEV-29883) Deadlock between InnoDB statistics update and BLOB insert
* [Revision #fda5846704](https://github.com/MariaDB/server/commit/fda5846704)\
  2022-11-08 15:49:52 +0000
  * [MDEV-29397](https://jira.mariadb.org/browse/MDEV-29397) CONNECT engine: Fix note turning into error (#2325)
* [Revision #2ef2e2322a](https://github.com/MariaDB/server/commit/2ef2e2322a)\
  2022-11-08 15:26:34 +0200
  * [MDEV-29856](https://jira.mariadb.org/browse/MDEV-29856) heap-use-after-poison in row\_merge\_spatial\_rows() w/ column prefix
* [Revision #b737d09dbc](https://github.com/MariaDB/server/commit/b737d09dbc)\
  2022-11-08 11:37:43 +0200
  * [MDEV-29905](https://jira.mariadb.org/browse/MDEV-29905) Change buffer operations fail to check for log file overflow
* [Revision #49a0ad695b](https://github.com/MariaDB/server/commit/49a0ad695b)\
  2022-11-08 11:24:49 +0200
  * [MDEV-23371](https://jira.mariadb.org/browse/MDEV-23371): Crash in _db\_doprnt_ via que\_thr\_step()
* [Revision #9ac8be4e29](https://github.com/MariaDB/server/commit/9ac8be4e29)\
  2022-11-08 10:39:29 +0200
  * Include some advice in the crash-upgrade message
* [Revision #95e2595d8d](https://github.com/MariaDB/server/commit/95e2595d8d)\
  2022-11-08 10:30:03 +0200
  * [MDEV-22512](https://jira.mariadb.org/browse/MDEV-22512): Disable frequently failing tests
* [Revision #314ed9f5ec](https://github.com/MariaDB/server/commit/314ed9f5ec)\
  2022-11-08 09:00:58 +0200
  * Work around [MDEV-24813](https://jira.mariadb.org/browse/MDEV-24813) in some tests
* [Revision #456d4a508c](https://github.com/MariaDB/server/commit/456d4a508c)\
  2022-11-08 08:54:07 +0200
  * Remove an unused file
* [Revision #eabb3b35d5](https://github.com/MariaDB/server/commit/eabb3b35d5)\
  2022-11-08 08:53:49 +0200
  * [MDEV-27121](https://jira.mariadb.org/browse/MDEV-27121) fixup: mariadb-backup.[MDEV-14447](https://jira.mariadb.org/browse/MDEV-14447) fault injection
* Merge [Revision #01ac7455e2](https://github.com/MariaDB/server/commit/01ac7455e2) 2022-11-07 15:32:35 +0100 - Merge branch '10.3' into bb-10.3-release
* [Revision #baa6b052a2](https://github.com/MariaDB/server/commit/baa6b052a2)\
  2022-11-07 08:08:55 -0500
  * bump the VERSION
* [Revision #f7e6198c02](https://github.com/MariaDB/server/commit/f7e6198c02)\
  2022-11-07 17:36:08 +0530
  * [MDEV-27121](https://jira.mariadb.org/browse/MDEV-27121) mariadb-backup incompatible with disabled dedicated undo log tablespaces
* [Revision #92be8d2048](https://github.com/MariaDB/server/commit/92be8d2048)\
  2022-11-05 18:36:43 +0100
  * [MDEV-29951](https://jira.mariadb.org/browse/MDEV-29951) server hang in crash handler
* [Revision #e7be2d3142](https://github.com/MariaDB/server/commit/e7be2d3142)\
  2022-11-02 16:24:36 +0200
  * Fix duplicate entry in mysqld\_safe man page
* [Revision #7d96cb4703](https://github.com/MariaDB/server/commit/7d96cb4703)\
  2022-10-30 17:25:32 -0400
  * Fix warning with signal typedef for \*BSD
* [Revision #4ebc8d8c27](https://github.com/MariaDB/server/commit/4ebc8d8c27)\
  2022-10-28 19:59:35 +1100
  * [MDEV-29847](https://jira.mariadb.org/browse/MDEV-29847): Wrong warning on rlimit capping of max\_open\_files (#2315)
* [Revision #899cedb33c](https://github.com/MariaDB/server/commit/899cedb33c)\
  2022-10-26 19:52:17 -0400
  * Fix building my\_gethwaddr() on OpenBSD

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
