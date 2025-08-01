# Connector/C 3.0.3 Changelog

The most recent [_**Stable**_](../../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/3.0.3)[Release Notes](../../mariadb-connector-c-30-release-notes/mariadb-connector-c-303-release-notes.md)[Changelog](mariadb-connector-c-303-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 18 Jan 2018

For the highlights of this release, see the [release notes](../../mariadb-connector-c-30-release-notes/mariadb-connector-c-303-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-c/) you can view more\
details of the revision and view diffs of the code modified in that revision.

* [Revision #c1a5ed4](https://github.com/mariadb-corporation/mariadb-connector-c/commit/c1a5ed4)\
  2018-01-17 12:43:58 +0100
  * Added installation layout for Debian (-DINSTALL\_LAYOUT=DEB)
* [Revision #d3a6061](https://github.com/mariadb-corporation/mariadb-connector-c/commit/d3a6061)\
  2018-01-17 08:01:21 +0100
  * Changed/fixed Wix installer images
* [Revision #5c16523](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5c16523)\
  2018-01-16 15:24:54 +0100
  * Fix for [MDEV-10361](https://jira.mariadb.org/browse/MDEV-10361): Don't try to reconnect twice: if mysql->options.reconnect is set, ma\_simple\_command already tries to reconnect, so there is no need to reconnect in mysql\_ping again
* [Revision #0335873](https://github.com/mariadb-corporation/mariadb-connector-c/commit/0335873)\
  2017-12-25 16:10:20 +0100
  * [CONC-299](https://jira.mariadb.org/browse/CONC-299): Add support for missing collation and character sets
* [Revision #edeffbf](https://github.com/mariadb-corporation/mariadb-connector-c/commit/edeffbf)\
  2018-01-16 11:45:49 +0100
  * If gnutls pkg-config file is missing, Cmake's module FindGNUTLS.cmake will not determine and check the version number. If GNUTLS\_VERSION\_STRING could not be determined, we try to get the version string by running gnutls\_check\_version (try\_run)
* [Revision #7fab2ec](https://github.com/mariadb-corporation/mariadb-connector-c/commit/7fab2ec)\
  2018-01-15 18:56:14 +0100
  * Merge branch 'master' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #1ea0354](https://github.com/mariadb-corporation/mariadb-connector-c/commit/1ea0354)\
  2018-01-15 18:18:42 +0100
  * Merge pull request #31 from kevgs/clang\_tsan
* [Revision #7f9629a](https://github.com/mariadb-corporation/mariadb-connector-c/commit/7f9629a)\
  2017-10-06 00:38:00 +0300
  * fix TSAN build with Clang
* [Revision #c066666](https://github.com/mariadb-corporation/mariadb-connector-c/commit/c066666)\
  2018-01-15 18:55:55 +0100
  * updated README
* [Revision #ddcb21c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ddcb21c)\
  2018-01-15 17:57:29 +0100
  * Skip test for SESSION\_TRACK\_STATE\_CHANGE if the test server is a MySQL server, since MySQL 5.7 (and above) doesn't send this flag after set session session\_track\_state\_change=1
* [Revision #1af934e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/1af934e)\
  2018-01-15 17:42:37 +0100
  * Merge branch 'master' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #9f9a1c5](https://github.com/mariadb-corporation/mariadb-connector-c/commit/9f9a1c5)\
  2018-01-15 17:41:19 +0100
  * Merge pull request #39 from InuSasha/patch-1
* [Revision #642320e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/642320e)\
  2018-01-04 22:00:40 +0100
  * fix typo in plugins.cmake
* [Revision #86dacf3](https://github.com/mariadb-corporation/mariadb-connector-c/commit/86dacf3)\
  2018-01-15 12:25:52 +0100
  * Removed determination of programname and reading configuration options from section \[programname] when parameter NULL was passed to mysql\_options(, MYSQL\_READ\_DEFAULT\_GROUP)
* [Revision #b15a7aa](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b15a7aa)\
  2018-01-11 12:10:05 +0200
  * Remove unused definitions
* [Revision #794689b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/794689b)\
  2018-01-10 16:37:15 +0000
  * Fix warnings about RETSIGTYPE/RETQSORTTYPE redefinition when using libmariadb headers together with server's
* [Revision #2e42f7a](https://github.com/mariadb-corporation/mariadb-connector-c/commit/2e42f7a)\
  2018-01-14 07:34:01 +0100
  * Test cleanup: - removed unused test for old sqlite3 module - to avoid warnings and make code more readable mysql\_stmt\_prepare and mysql\_real\_query now use the SL (string and length) macro.
* [Revision #64cf572](https://github.com/mariadb-corporation/mariadb-connector-c/commit/64cf572)\
  2018-01-04 15:43:44 +0000
  * support build with static openssl on Windows
* [Revision #75ca3c1](https://github.com/mariadb-corporation/mariadb-connector-c/commit/75ca3c1)\
  2018-01-09 18:13:54 +0100
  * TLS/SSL fixes: - don't run fingerprint and passphrase protected tests if the corresponding files (sha1 and encrypted client key) are not found in CERT\_PATH - don't overwrite SSL errors if handshake failed - Use gnutls read/write instead of pvio
* [Revision #5abcb1b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5abcb1b)\
  2018-01-08 13:57:53 +0100
  * [CONC-302](https://jira.mariadb.org/browse/CONC-302):
* [Revision #9345d74](https://github.com/mariadb-corporation/mariadb-connector-c/commit/9345d74)\
  2018-01-08 12:39:48 +0100
  * Merge branch 'master' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #74b1ba2](https://github.com/mariadb-corporation/mariadb-connector-c/commit/74b1ba2)\
  2018-01-08 12:31:33 +0100
  * removed unused function char\_val from ma\_password.c
* [Revision #72b38f5](https://github.com/mariadb-corporation/mariadb-connector-c/commit/72b38f5)\
  2018-01-08 12:31:33 +0100
  * removed unused function char\_val from ma\_password.c
* [Revision #b00cdcd](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b00cdcd)\
  2017-12-22 09:00:13 +0100
  * Merge branch 'master' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #3e164b5](https://github.com/mariadb-corporation/mariadb-connector-c/commit/3e164b5)\
  2017-12-20 10:01:32 +0100
  * Fix test failues if testing against server < 10.2
* [Revision #2314598](https://github.com/mariadb-corporation/mariadb-connector-c/commit/2314598)\
  2017-12-22 08:59:32 +0100
  * Fix for [CONC-301](https://jira.mariadb.org/browse/CONC-301) (manually merged from 2.3.5)
* [Revision #6d2fb01](https://github.com/mariadb-corporation/mariadb-connector-c/commit/6d2fb01)\
  2017-12-15 10:48:42 +0100
  * [MDEV-14647](https://jira.mariadb.org/browse/MDEV-14647): Fixed crash when client receives extended ok packet with SESSION\_TRACK\_STATE\_CHANGE information flag.
* [Revision #434b67e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/434b67e)\
  2017-12-04 19:45:07 +0100
  * Fix for [CONC-297](https://jira.mariadb.org/browse/CONC-297): MariaDB Connector/C was not compatible to libmysql when passing value for MYSQL\_OPT\_LOCAL\_INFILE. According to the documentatin local infile will be enabled if a NULL pointer was passed or a pointer to an unsigned integer which value is > 0. Connector/C expected a bool pointer, which ends up in wrong results on big endian systems.
* [Revision #87b863e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/87b863e)\
  2017-11-27 19:02:37 +0100
  * Windows build fix: init\_once assignment needs to be casted (C99).
* [Revision #14fe661](https://github.com/mariadb-corporation/mariadb-connector-c/commit/14fe661)\
  2017-11-27 18:22:05 +0100
  * Fix for [MDEV-14514](https://jira.mariadb.org/browse/MDEV-14514): Wrong exit code when an invalid option was passed to mariadb\_config.
* [Revision #c849a21](https://github.com/mariadb-corporation/mariadb-connector-c/commit/c849a21)\
  2017-11-27 17:31:16 +0100
  * Fix for FreeBSD build: PTHREAD\_ONCE\_INIT is defined as a struct, so we need to cast it.
* [Revision #a81a799](https://github.com/mariadb-corporation/mariadb-connector-c/commit/a81a799)\
  2017-11-12 21:29:10 +0000
  * [MDEV-11546](https://jira.mariadb.org/browse/MDEV-11546) main.ssl\_7937 failed with timeout in buildbot on Windows
* [Revision #15e9ee4](https://github.com/mariadb-corporation/mariadb-connector-c/commit/15e9ee4)\
  2017-11-22 09:50:12 +0100
  * Fix for [CONC-277](https://jira.mariadb.org/browse/CONC-277): For backwards compatibiliry we now allow reinitialization of client library by setting init\_once to zero in mysql\_server\_end() function.
* [Revision #683e2f3](https://github.com/mariadb-corporation/mariadb-connector-c/commit/683e2f3)\
  2017-11-18 16:20:33 +0100
  * Fix for Solaris build ([MDEV-11603](https://jira.mariadb.org/browse/MDEV-11603))
* [Revision #77490eb](https://github.com/mariadb-corporation/mariadb-connector-c/commit/77490eb)\
  2017-11-08 09:12:42 +0100
  * Fix windows build: For using \_malloca (instead of deprecated alloca) we need to include malloc.h
* [Revision #b825f34](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b825f34)\
  2017-11-08 09:09:52 +0100
  * Revert "Fix windows build: Use \_malloca instead of alloca"
* [Revision #b21e60a](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b21e60a)\
  2017-11-08 08:51:36 +0100
  * Fix windows build: Use \_malloca instead of alloca
* [Revision #1e6cdb8](https://github.com/mariadb-corporation/mariadb-connector-c/commit/1e6cdb8)\
  2017-11-08 04:56:04 +0100
  * [CONC-292](https://jira.mariadb.org/browse/CONC-292): Fxed malloc result check in dynamic columns
* [Revision #c979378](https://github.com/mariadb-corporation/mariadb-connector-c/commit/c979378)\
  2017-11-07 18:45:08 +0100
  * Added additional test (invalid user)
* [Revision #771a409](https://github.com/mariadb-corporation/mariadb-connector-c/commit/771a409)\
  2017-11-07 18:36:14 +0100
  * Implementation for [MDEV-9059](https://jira.mariadb.org/browse/MDEV-9059):
* [Revision #b40058f](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b40058f)\
  2017-10-28 16:46:49 +0200
  * Fix for [MDEV-14165](https://jira.mariadb.org/browse/MDEV-14165):
* [Revision #5d920a9](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5d920a9)\
  2017-10-26 18:34:05 +0200
  * [CONC-290](https://jira.mariadb.org/browse/CONC-290): Return error (=1) instead of exiting.
* [Revision #12a6865](https://github.com/mariadb-corporation/mariadb-connector-c/commit/12a6865)\
  2017-10-25 19:07:17 +0200
  * Fix compiler warning
* [Revision #8ea4d2f](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8ea4d2f)\
  2017-10-23 11:04:14 +0200
  * [MDEV-14101](https://jira.mariadb.org/browse/MDEV-14101): tls-version
* [Revision #9272a18](https://github.com/mariadb-corporation/mariadb-connector-c/commit/9272a18)\
  2017-10-17 15:53:45 +0200
  * Provide details about TLS/SSL library in use
* [Revision #d67ee8b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/d67ee8b)\
  2017-10-15 09:41:12 +0200
  * Revert "[MDEV-14027](https://jira.mariadb.org/browse/MDEV-14027): Determine TLS/SSL library version"
* [Revision #113418c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/113418c)\
  2017-10-15 06:01:59 +0200
  * [MDEV-14027](https://jira.mariadb.org/browse/MDEV-14027): Determine TLS/SSL library version
* [Revision #5e32110](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5e32110)\
  2017-10-12 12:15:39 +0200\
  \*
  * Build fix: When building as subproject inside server tree, ZLIB\_FOUND was already set by parent, so we need additionally check if WITH\_EXTERNAL\_ZLIB was specified. - New server status flags Added SERVER\_STATUS\_ANSI\_QUOTES and SERVER\_STATUS\_IN\_TRANS\_READONLY
* [Revision #6d24e0b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/6d24e0b)\
  2017-10-12 09:56:50 +0200
  * Added missing dependency for zlib (WITH\_EXTERNAL\_ZLIB=ON) Added CC\_SOURCE\_REVISION definition (mariadb\_version.h)
* [Revision #cd46b30](https://github.com/mariadb-corporation/mariadb-connector-c/commit/cd46b30)\
  2017-10-10 12:20:37 +0200
  * Merge branch 'master' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #0334aa4](https://github.com/mariadb-corporation/mariadb-connector-c/commit/0334aa4)\
  2017-08-14 17:23:42 +0200
  * Implementation and testcase for [CONC-275](https://jira.mariadb.org/browse/CONC-275) - skipping particular paramset in bulk operation - with help of special indicator value STMT\_INDICATOR\_IGNORE\_ROW set in any column of the row. The revision also adds some (mainly VS specific) file/dirs definitions to .gitignore to make 'gid status' usable on Windows, and the typo in bulk1 testsuite
* [Revision #6329049](https://github.com/mariadb-corporation/mariadb-connector-c/commit/6329049)\
  2017-10-10 12:19:01 +0200
  * [CONC-286](https://jira.mariadb.org/browse/CONC-286): - Force TLS/SSL connection if finger print options were specified - Allow hex finger prints with colon separated 2 digit numbers
* [Revision #2546445](https://github.com/mariadb-corporation/mariadb-connector-c/commit/2546445)\
  2017-10-02 09:08:03 +0200
  * [CONC-282](https://jira.mariadb.org/browse/CONC-282): Connector/C now provides additional information for package version mariadb\_config --cc\_version lists the package version Beside MARIADB\_PACKAGE\_VERSION numeric representation MARIADB\_PACKAGE\_VERSION\_ID can be used now within preprocessor directives
* [Revision #2e39bb7](https://github.com/mariadb-corporation/mariadb-connector-c/commit/2e39bb7)\
  2017-10-01 05:57:58 +0200
  * Fixed test case name for [CONC-281](https://jira.mariadb.org/browse/CONC-281)
* [Revision #2083aa9](https://github.com/mariadb-corporation/mariadb-connector-c/commit/2083aa9)\
  2017-09-30 14:10:01 +0200
  * Fix for [MDEV-13959](https://jira.mariadb.org/browse/MDEV-13959): duplicated if condition in mariadb\_dyncol.c
* [Revision #5bf7813](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5bf7813)\
  2017-09-29 11:12:36 +0200
  * Fix parentheses ([MDEV-13956](https://jira.mariadb.org/browse/MDEV-13956))
* [Revision #cb02751](https://github.com/mariadb-corporation/mariadb-connector-c/commit/cb02751)\
  2017-09-25 19:16:55 +0200
  * Update year in mariadb\_config output
* [Revision #7d6101d](https://github.com/mariadb-corporation/mariadb-connector-c/commit/7d6101d)\
  2017-09-15 01:06:05 +0200
  * define MARIADB\_BASE\_VERSION in mariadb\_version.h
* [Revision #3d11d0f](https://github.com/mariadb-corporation/mariadb-connector-c/commit/3d11d0f)\
  2017-09-09 16:03:08 +0200
  * [MDEV-13588](https://jira.mariadb.org/browse/MDEV-13588) /usr/lib/x86\_64-linux-gnu/libmariadbclient.so.18: version \`libmariadbclient\_18' not found
* [Revision #17110fb](https://github.com/mariadb-corporation/mariadb-connector-c/commit/17110fb)\
  2017-09-25 13:51:01 +0200
  * Fix for [CONC-282](https://jira.mariadb.org/browse/CONC-282): mysql\_stmt\_fetch\_column doesn't work with prior call to mysql\_stmt\_store\_result - If no bind variables were bound or the function mysql\_stmt\_store\_result was not called before, the internal bind variables (stmt->bind) was not filled (lengths and null values)
* [Revision #f9a6b8e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/f9a6b8e)\
  2017-09-08 12:19:32 +0200
  * Merge branch 'master' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #85d150e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/85d150e)\
  2017-09-07 17:35:35 +0200
  * Export _mysql\_client\_plugin\_declaration_ from auth\_gssapi\_client.so
* [Revision #d76663a](https://github.com/mariadb-corporation/mariadb-connector-c/commit/d76663a)\
  2017-09-08 12:18:37 +0200
  * Added missing break in mysql\_get\_infov
* [Revision #cd50748](https://github.com/mariadb-corporation/mariadb-connector-c/commit/cd50748)\
  2017-08-31 07:54:21 +0200
  * Fixed memory leak and added missing break in dynamic column conversion function
* [Revision #a2b0bcd](https://github.com/mariadb-corporation/mariadb-connector-c/commit/a2b0bcd)\
  2017-08-24 18:05:58 +0200
  * Fix for [CONC-276](https://jira.mariadb.org/browse/CONC-276): client library crashes on Windows after TLS reconnect: The connection pointer mysql is now no longer part (and doesn't need to be updated) of schannel security context, since it can be obtained directly from tls container.
* [Revision #482a0b6](https://github.com/mariadb-corporation/mariadb-connector-c/commit/482a0b6)\
  2017-07-25 09:45:16 +0200
  * Merge branch 'master' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #ce01b63](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ce01b63)\
  2017-07-21 08:06:53 +0000
  * Merge branch 'master' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #b481265](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b481265)\
  2017-07-19 13:50:40 +0200
  * Bumped version number to 3.0.3
* [Revision #bc2d6df](https://github.com/mariadb-corporation/mariadb-connector-c/commit/bc2d6df)\
  2017-07-21 07:53:03 +0000
  * Warning fixes for Win64 build
* [Revision #843c492](https://github.com/mariadb-corporation/mariadb-connector-c/commit/843c492)\
  2017-07-25 09:43:55 +0200
  * Fix for [CONC-271](https://jira.mariadb.org/browse/CONC-271): RPM layout now works for other 64-bit architectures than x86\_64. Thx to Michal Schorn for contributing this patch.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
