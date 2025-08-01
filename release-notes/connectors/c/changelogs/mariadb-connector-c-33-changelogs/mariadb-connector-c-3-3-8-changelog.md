# Connector/C 3.3.8 Changelog

The most recent [_**Stable**_](../../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://mariadb.com/downloads/connectors)[Release Notes](../../mariadb-connector-c-33-release-notes/mariadb-connector-c-3-3-8-release-notes.md)[Changelog](mariadb-connector-c-3-3-8-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 29 Nov 2023

For the highlights of this release, see the [release notes](../../mariadb-connector-c-33-release-notes/mariadb-connector-c-3-3-8-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-c/) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #458a439](https://github.com/mariadb-corporation/mariadb-connector-c/commit/458a439)\
  2023-11-01 11:26:56 +0100
  * don't force -Werror if a subproject
* [Revision #eb6cad1](https://github.com/mariadb-corporation/mariadb-connector-c/commit/eb6cad1)\
  2023-10-24 10:07:01 +0200
  * \[misc] correcting CI testing label with ps-protocol
* [Revision #7293150](https://github.com/mariadb-corporation/mariadb-connector-c/commit/7293150)\
  2023-10-23 17:59:33 +0200
  * \[misc] CI testing changes
* [Revision #64f9d88](https://github.com/mariadb-corporation/mariadb-connector-c/commit/64f9d88)\
  2023-10-23 13:36:05 +0200
  * Merge branch '3.1' into 3.3
* [Revision #ae565ee](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ae565ee)\
  2023-10-23 13:32:45 +0200
  * Use safer snprintf call.
* [Revision #4f5950b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/4f5950b)\
  2023-10-21 19:46:00 +0200
  * Merge branch '3.1' into 3.3
* [Revision #8320f0d](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8320f0d)\
  2023-10-21 19:43:42 +0200
  * Fix error on 32-bit systems
* [Revision #642bc31](https://github.com/mariadb-corporation/mariadb-connector-c/commit/642bc31)\
  2023-10-21 08:09:40 +0200
  * Follow up of PR-236 (update ma\_context):
* [Revision #26b2edd](https://github.com/mariadb-corporation/mariadb-connector-c/commit/26b2edd)\
  2023-10-20 06:53:07 +0200
  * Merge branch '3.1' into 3.3
* [Revision #808312f](https://github.com/mariadb-corporation/mariadb-connector-c/commit/808312f)\
  2023-09-23 02:33:37 +0200
  * Update ma\_context.c
* [Revision #35cd69b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/35cd69b)\
  2023-10-20 06:44:38 +0200
  * Fix for [CONC-672](https://jira.mariadb.org/browse/CONC-672)
* [Revision #ab38a07](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ab38a07)\
  2023-10-11 10:43:25 +0200
  * Fix for [CONC-670](https://jira.mariadb.org/browse/CONC-670)
* [Revision #acc0b05](https://github.com/mariadb-corporation/mariadb-connector-c/commit/acc0b05)\
  2023-10-20 06:50:43 +0200
  * Merge pull request #236 from tildeslash/patch-1
* [Revision #249d838](https://github.com/mariadb-corporation/mariadb-connector-c/commit/249d838)\
  2023-09-23 02:33:37 +0200
  * Update ma\_context.c
* [Revision #b323b54](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b323b54)\
  2023-09-27 10:19:23 +0200
  * Windows installation fix
* [Revision #5d51d16](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5d51d16)\
  2023-09-27 09:58:22 +0200
  * Merge branch '3.3' of [mariadb-connector-c](https://github.com/mariadb-corporation/mariadb-connector-c) into 3.3
* [Revision #4692e9c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/4692e9c)\
  2023-09-22 00:52:00 +0200
  * [CONC-645](https://jira.mariadb.org/browse/CONC-645) : fix build with clang (v16), clang-cl(v16), and mingw-gcc(v12).
* [Revision #463a50e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/463a50e)\
  2023-09-21 23:45:35 +0200
  * Merge remote-tracking branch 'origin/3.1' into 3.3
* [Revision #1b3cf6b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/1b3cf6b)\
  2023-09-21 13:36:23 +0200
  * [CONC-669](https://jira.mariadb.org/browse/CONC-669) Cache bcrypt algorithm providers in win\_crypt.c
* [Revision #a6d8ef5](https://github.com/mariadb-corporation/mariadb-connector-c/commit/a6d8ef5)\
  2023-09-21 07:08:37 +0200
  * Merge pull request #235 from grooverdan/3.1-remove-words\_big\_endian
* [Revision #07ae949](https://github.com/mariadb-corporation/mariadb-connector-c/commit/07ae949)\
  2023-09-09 08:20:45 +1000
  * [MDEV-19511](https://jira.mariadb.org/browse/MDEV-19511) Remove WORDS\_BIGENDIAN - HAVE\_BIGENDIAN replaced it
* [Revision #d9626e3](https://github.com/mariadb-corporation/mariadb-connector-c/commit/d9626e3)\
  2023-09-13 10:36:15 +0200
  * [CONC-666](https://jira.mariadb.org/browse/CONC-666): Fix memory allocation issue with prepared statement reexecution.
* [Revision #04b3d83](https://github.com/mariadb-corporation/mariadb-connector-c/commit/04b3d83)\
  2023-09-20 14:13:19 +0200
  * Added -Wno-stringop-truncation to the default gcc options
* [Revision #9f37c27](https://github.com/mariadb-corporation/mariadb-connector-c/commit/9f37c27)\
  2023-09-18 16:05:00 +0200
  * Fix for [CONC-668](https://jira.mariadb.org/browse/CONC-668):
* [Revision #4e3905c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/4e3905c)\
  2023-08-23 16:18:50 +0200
  * Fix for bcrypt hash functions:
* [Revision #0e7082f](https://github.com/mariadb-corporation/mariadb-connector-c/commit/0e7082f)\
  2023-09-27 09:57:55 +0200
  * Fix include file path for ma\_io.h
* [Revision #9a0ddd8](https://github.com/mariadb-corporation/mariadb-connector-c/commit/9a0ddd8)\
  2023-09-14 12:36:59 -0400
  * bump the VERSION

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
