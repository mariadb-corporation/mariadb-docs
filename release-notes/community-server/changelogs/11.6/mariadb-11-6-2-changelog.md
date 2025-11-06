# MariaDB 11.6.2 Changelog

[Download](https://mariadb.com/downloads/)[Release Notes](../../old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md)[Changelog](mariadb-11-6-2-changelog.md)[Overview of 11.6](../../old-releases/release-notes-mariadb-11-6-rolling-releases/what-is-mariadb-116.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.6.2/)

**Release date:** 21 Nov 2024

For the highlights of this release, see the [release notes](../../old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/server/tree/11.1) you can view more\
details of the revision and view diffs of the code modified in that revision.

* Includes all fixes from [MariaDB 11.4.4](../11.4/11.4.4.md)
* Includes all fixes from [MariaDB 11.5.2](../11.5/mariadb-11-5-2-changelog.md)
* [Revision #d8dad8c3b5](https://github.com/MariaDB/server/commit/d8dad8c3b5)\
  2024-11-08 15:35:01 +0100
  * New CC 3.4
* [Revision #044d8c50c6](https://github.com/MariaDB/server/commit/044d8c50c6)\
  2024-10-28 22:41:41 +0100
  * ed25519: support empty password
* [Revision #583a5a79c9](https://github.com/MariaDB/server/commit/583a5a79c9)\
  2024-09-04 19:57:45 +0200
  * [MDEV-34854](https://jira.mariadb.org/browse/MDEV-34854) Parsec sends garbage when using an empty password
* Merge [Revision #9e1fb104a3](https://github.com/MariaDB/server/commit/9e1fb104a3) 2024-11-08 07:17:00 +0100 - Merge tag '11.4' into 11.6
* [Revision #4c7cfd2624](https://github.com/MariaDB/server/commit/4c7cfd2624)\
  2024-10-29 14:22:59 +0400
  * [MDEV-34817](https://jira.mariadb.org/browse/MDEV-34817) perfschema.lowercase\_fs\_off fails on buildbot
* [Revision #a88c71b294](https://github.com/MariaDB/server/commit/a88c71b294)\
  2024-10-22 11:10:58 +0400
  * [MDEV-35041](https://jira.mariadb.org/browse/MDEV-35041) Simple comparison causes "Illegal mix of collations" even with default server settings
* [Revision #4e1e9ea6f3](https://github.com/MariaDB/server/commit/4e1e9ea6f3)\
  2024-10-11 15:02:31 +0300
  * [MDEV-35124](https://jira.mariadb.org/browse/MDEV-35124) Set innodb\_snapshot\_isolation=ON by default
* [Revision #26dce1cec3](https://github.com/MariaDB/server/commit/26dce1cec3)\
  2024-10-08 14:05:12 +0200
  * [MDEV-34220](https://jira.mariadb.org/browse/MDEV-34220): Add --dir option to mariadb-dump man page
* [Revision #69686375a8](https://github.com/MariaDB/server/commit/69686375a8)\
  2024-10-09 17:22:48 +0300
  * [MDEV-34782](https://jira.mariadb.org/browse/MDEV-34782) SIGSEGV in handler::update\_global\_table\_stats in close\_thread\_table()
* [Revision #875d8c909f](https://github.com/MariaDB/server/commit/875d8c909f)\
  2024-10-09 17:10:30 +0300
  * Removed end '.' from variable comment
* Merge [Revision #43465352b9](https://github.com/MariaDB/server/commit/43465352b9) 2024-10-03 16:09:56 +0300 - Merge 11.4 into 11.6
* Merge [Revision #ba7088d462](https://github.com/MariaDB/server/commit/ba7088d462) 2024-10-03 15:59:20 +1000 - Merge '11.4' into 11.6
* [Revision #b7bca3ff71](https://github.com/MariaDB/server/commit/b7bca3ff71)\
  2024-07-03 16:52:08 +0800
  * [MDEV-34518](https://jira.mariadb.org/browse/MDEV-34518) Initialise THD::max\_tmp\_space\_used
* [Revision #45d99ea105](https://github.com/MariaDB/server/commit/45d99ea105)\
  2024-09-10 20:35:03 +0200
  * Workaround [MDEV-34890](https://jira.mariadb.org/browse/MDEV-34890)
* [Revision #7fd73f9ac9](https://github.com/MariaDB/server/commit/7fd73f9ac9)\
  2024-09-06 01:57:50 +0200
  * mariadb-import, multithreading - improve error handling
* [Revision #19cea73834](https://github.com/MariaDB/server/commit/19cea73834)\
  2024-09-05 13:24:22 +0200
  * Cleanup - make sure all members of table\_load\_params are initialized
* Merge [Revision #a5b80531fb](https://github.com/MariaDB/server/commit/a5b80531fb) 2024-09-04 10:38:25 +0300 - Merge 11.4 into 11.6
* [Revision #c67149b859](https://github.com/MariaDB/server/commit/c67149b859)\
  2024-08-28 14:41:21 +0400
  * [MDEV-34829](https://jira.mariadb.org/browse/MDEV-34829) LOCALTIME returns a wrong data type
* [Revision #9e845107f8](https://github.com/MariaDB/server/commit/9e845107f8)\
  2024-08-20 13:06:11 -0600
  * [MDEV-34765](https://jira.mariadb.org/browse/MDEV-34765): rpl.master\_last\_event\_time\_stmt fails with Result Length Mismatch
* Merge [Revision #492a7c2430](https://github.com/MariaDB/server/commit/492a7c2430) 2024-08-21 13:28:32 +0200 - Merge branch '11.5' into 11.6
* Merge [Revision #342fa29615](https://github.com/MariaDB/server/commit/342fa29615) 2024-08-21 11:52:54 +0200 - Merge branch '11.4' into 11.5
* [Revision #8b8c8fcb86](https://github.com/MariaDB/server/commit/8b8c8fcb86)\
  2024-08-12 10:33:12 +1000
  * [MDEV-33836](https://jira.mariadb.org/browse/MDEV-33836) Compute modulus correctly in sequence
* [Revision #2603453436](https://github.com/MariaDB/server/commit/2603453436)\
  2024-08-09 15:39:59 +1000
  * [MDEV-33836](https://jira.mariadb.org/browse/MDEV-33836) Fix version markers in tests relating to [MDEV-28152](https://jira.mariadb.org/browse/MDEV-28152)
* Merge [Revision #10b885907a](https://github.com/MariaDB/server/commit/10b885907a) 2024-08-15 08:13:32 +0300 - Merge 11.4 into 11.6
* [Revision #cf08f44d03](https://github.com/MariaDB/server/commit/cf08f44d03)\
  2024-08-14 16:00:21 -0400
  * bump the VERSION
* [Revision #72ab8bc990](https://github.com/MariaDB/server/commit/72ab8bc990)\
  2024-08-13 19:04:44 +0900
  * fix: fix typo at mysql-test README
* [Revision #ff865b088f](https://github.com/MariaDB/server/commit/ff865b088f)\
  2024-08-12 21:30:32 +0200
  * [MDEV-34741](https://jira.mariadb.org/browse/MDEV-34741) - remove LOCK TABLE from mariadb-import

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
