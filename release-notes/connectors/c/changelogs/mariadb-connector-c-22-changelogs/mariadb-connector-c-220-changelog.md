# Connector/C 2.2.0 Changelog

The most recent [_**Stable**_](../../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.2.0)[Release Notes](../../mariadb-connector-c-22-release-notes/mariadb-connector-c-220-release-notes.md)[Changelog](mariadb-connector-c-220-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-c/README.md)

**Release date:** 29 Sep 2015

For the highlights of this release, see the [release notes](../../mariadb-connector-c-22-release-notes/mariadb-connector-c-220-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On [GitHub](https://github.com/MariaDB/mariadb-connector-c/) you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #30ba4fe](https://github.com/mariadb-corporation/mariadb-connector-c/commit/30ba4fe)\
  2015-09-28 10:30:06 +0200
  * Fix for [CONC-143](https://jira.mariadb.org/browse/CONC-143): use #include "my\_stmt.h" instead of \<my\_stmt.h>
* [Revision #9d12de0](https://github.com/mariadb-corporation/mariadb-connector-c/commit/9d12de0)\
  2015-09-23 09:06:16 +0200
  * Ignore zip and gz files when building source packages
* [Revision #2acfd9c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/2acfd9c)\
  2015-09-23 07:53:08 +0200
  * Fixed source package build
* [Revision #604897e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/604897e)\
  2015-09-19 16:01:02 +0200
  * Fix for [CONC-133](https://jira.mariadb.org/browse/CONC-133). When CMAKE\_BUILD\_TYPE is Release some gcc versions fail to compile my\_context.c
* [Revision #0bc7dc5](https://github.com/mariadb-corporation/mariadb-connector-c/commit/0bc7dc5)\
  2015-09-19 13:02:30 +0200
  * Added build option WITH\_REMOTEIO (default=off)
* [Revision #5b33965](https://github.com/mariadb-corporation/mariadb-connector-c/commit/5b33965)\
  2015-09-19 11:27:26 +0200
  * Changed version number to 2.2.0
* [Revision #31c2a38](https://github.com/mariadb-corporation/mariadb-connector-c/commit/31c2a38)\
  2015-09-19 10:34:45 +0200
  * Fix windows build: predefined variable for VS is \_MSC\_VER
* [Revision #7b81b34](https://github.com/mariadb-corporation/mariadb-connector-c/commit/7b81b34)\
  2015-09-19 08:54:49 +0200
  * Fixed wrong socket\_blocking, introducd with fix for [CONC-130](https://jira.mariadb.org/browse/CONC-130)
* [Revision #f0e8953](https://github.com/mariadb-corporation/mariadb-connector-c/commit/f0e8953)\
  2015-09-18 15:27:47 +0200
  * Merge branch 'connector\_c\_2.2' of [mariadb-connector-c](https://github.com/MariaDB/mariadb-connector-c)
* [Revision #1f71590](https://github.com/mariadb-corporation/mariadb-connector-c/commit/1f71590)\
  2015-09-18 14:35:43 +0200
  * Fix for [CONC-139](https://jira.mariadb.org/browse/CONC-139): Build with XCode generator fails Both shared and static library are built from object library. XCode doesn't like targets which have only object files, so we just add an empty file.
* [Revision #07c0170](https://github.com/mariadb-corporation/mariadb-connector-c/commit/07c0170)\
  2015-09-17 19:17:53 +0200
  * Fixed build when using external iconv on MacOS
* [Revision #b0444f5](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b0444f5)\
  2015-09-17 14:15:38 +0200
  * Fix for [CONC-140](https://jira.mariadb.org/browse/CONC-140): MinGW error due to ssize\_t redefinition
* [Revision #8f64528](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8f64528)\
  2015-09-17 11:11:38 +0200
  * Fix for [CONC-140](https://jira.mariadb.org/browse/CONC-140): Prevent redefinition of ssize\_t for MinGW build
* [Revision #b950d2c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b950d2c)\
  2015-09-17 08:14:13 +0200
  * [CONC-141](https://jira.mariadb.org/browse/CONC-141): set stmt->state to MYSQL\_STMT\_FETCH\_DONE if no more resultsets are available
* [Revision #bc4a828](https://github.com/mariadb-corporation/mariadb-connector-c/commit/bc4a828)\
  2015-09-11 17:06:43 +0200
  * Fixed bug in OpenSSL: instead of ca and ca\_list we need to store crl and crl\_list for CRL\_CHECK
* [Revision #7b59e09](https://github.com/mariadb-corporation/mariadb-connector-c/commit/7b59e09)\
  2015-09-08 10:25:20 +0200
  * Fix for [CONC-130](https://jira.mariadb.org/browse/CONC-130): Initial wait on connect is wrong direction We need to wait for read instead of write if connect\_timeout was specified
* [Revision #abf0080](https://github.com/mariadb-corporation/mariadb-connector-c/commit/abf0080)\
  2015-09-08 07:33:30 +0200
  * Fix for [CONC-129](https://jira.mariadb.org/browse/CONC-129) (asynchronous api): Check if connection is still alive in mysql\_close\_start
* [Revision #7526361](https://github.com/mariadb-corporation/mariadb-connector-c/commit/7526361)\
  2015-09-05 17:17:14 +0200
  * Fix for [CONC-138](https://jira.mariadb.org/browse/CONC-138): When mysql\_ssl\_set will be called twice, memory from first call will not be freed. We call now mysql\_optionsv in mysql\_ssl\_set so values will be freed and new ones will be assigned. my\_strdup now checks flag MY\_ALLOW\_ZERO\_PTR
* [Revision #94a32d6](https://github.com/mariadb-corporation/mariadb-connector-c/commit/94a32d6)\
  2015-08-16 11:33:31 +0200
  * Fix for [CONC-137](https://jira.mariadb.org/browse/CONC-137): Error code not set in mysql\_stmt\_send\_long\_data
* [Revision #a6f40f2](https://github.com/mariadb-corporation/mariadb-connector-c/commit/a6f40f2)\
  2015-08-16 11:33:31 +0200
  * Fix for [CONC-137](https://jira.mariadb.org/browse/CONC-137): Error code not set in mysql\_stmt\_send\_long\_data
* [Revision #1466fec](https://github.com/mariadb-corporation/mariadb-connector-c/commit/1466fec)\
  2015-08-13 10:05:02 +0200
  * Fix memory overrun: When reallocating net->buffer we need to allocate extra space for header and compressed header
* [Revision #9e0f506](https://github.com/mariadb-corporation/mariadb-connector-c/commit/9e0f506)\
  2015-08-02 14:05:36 +0200
  * Fixed libs in mariadb\_config
* [Revision #8f5ec7d](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8f5ec7d)\
  2015-08-02 14:05:36 +0200
  * Fixed libs in mariadb\_config
* [Revision #330b7fb](https://github.com/mariadb-corporation/mariadb-connector-c/commit/330b7fb)\
  2015-07-16 08:06:03 +0200
  * Bumped version number to 3.0.0
* [Revision #3f1c7df](https://github.com/mariadb-corporation/mariadb-connector-c/commit/3f1c7df)\
  2015-07-14 13:57:23 +0200
  * Merge pull request #3 from grooverdan/speling-capability
* [Revision #bd6c340](https://github.com/mariadb-corporation/mariadb-connector-c/commit/bd6c340)\
  2015-07-14 18:17:19 +1000
  * more spelling/grammar errors
* [Revision #b42f702](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b42f702)\
  2015-07-14 18:07:27 +1000
  * spell capabilites -> capabilities
* [Revision #3c4bb27](https://github.com/mariadb-corporation/mariadb-connector-c/commit/3c4bb27)\
  2015-07-14 06:11:09 +0200
  * Merge remote-tracking branch 'origin/connector\_c\_2.2'
* [Revision #318257b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/318257b)\
  2015-07-14 06:07:36 +0200\
  \*
  * Fix for [CONC-136](https://jira.mariadb.org/browse/CONC-136): mysql\_select\_db\_start/cont aren't declared in mysql.h - ma\_dyncol.h no longer requires longlong declaration from my\_global.h
* [Revision #bdb3c65](https://github.com/mariadb-corporation/mariadb-connector-c/commit/bdb3c65)\
  2015-07-06 17:27:54 +0200
  * Bump minor version number
* [Revision #180a990](https://github.com/mariadb-corporation/mariadb-connector-c/commit/180a990)\
  2015-07-01 15:35:40 +0200
  * Merge remote-tracking branch 'origin/connector\_c\_2.2'
* [Revision #b1e0231](https://github.com/mariadb-corporation/mariadb-connector-c/commit/b1e0231)\
  2015-07-01 15:31:32 +0200
  * Fix for [CONC-135](https://jira.mariadb.org/browse/CONC-135): Return value of mysql\_get\_socket() indicating "no socket" not defined mysql\_get\_socket now returns in case of error: MARIADB\_INVALID\_SOCKET instead of INVALID\_SOCKET (which isn't defined on several OS). MARIADB\_INVALID\_SOCKET is defined as -1.
* [Revision #c615d61](https://github.com/mariadb-corporation/mariadb-connector-c/commit/c615d61)\
  2015-06-27 08:55:21 +0200
  * Merge remote-tracking branch 'origin/connector\_c\_2.2'
* [Revision #af04caf](https://github.com/mariadb-corporation/mariadb-connector-c/commit/af04caf)\
  2015-06-27 08:52:47 +0200
  * Fix for [CONC-132](https://jira.mariadb.org/browse/CONC-132): Set SUFFIX and PREFIX\_INSTALL\_DIR when specified
* [Revision #8f5e915](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8f5e915)\
  2015-06-26 11:01:10 +0200
  * Merge remote-tracking branch 'origin/connector\_c\_2.2'
* [Revision #33027b8](https://github.com/mariadb-corporation/mariadb-connector-c/commit/33027b8)\
  2015-06-26 11:00:01 +0200
  * Fix for bug [CONC-131](https://jira.mariadb.org/browse/CONC-131): Free async context when closing options (mysql\_options\_close)
* [Revision #64720ee](https://github.com/mariadb-corporation/mariadb-connector-c/commit/64720ee)\
  2015-06-26 09:52:11 +0200
  * Merge remote-tracking branch 'origin/connector\_c\_2.2'
* [Revision #ce013e7](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ce013e7)\
  2015-06-26 09:50:07 +0200
  * Moved certificate creation to CMakeLists.txt
* [Revision #8d7118f](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8d7118f)\
  2015-06-25 22:48:27 +0200
  * Small fix in STRING REPLACE command uses in unittest/libmariadb/CMakeLists.txt to let cmake swallow it
* [Revision #50e3a25](https://github.com/mariadb-corporation/mariadb-connector-c/commit/50e3a25)\
  2015-06-25 09:19:11 +0200
  * Merge remote-tracking branch 'origin/connector\_c\_2.2'
* [Revision #ae96108](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ae96108)\
  2015-06-17 09:54:31 +0200
  * added missing fingerprint white list
* [Revision #28dadb0](https://github.com/mariadb-corporation/mariadb-connector-c/commit/28dadb0)\
  2015-06-11 13:21:25 +0200\
  \*
  * OpenSSL security: report an error if client requires SSL but server doesn't support SSL (MTM attack) new options MARIADB\_OPT\_SSL\_FP for fingerprint of server certificate MARIADB\_OPT\_SSL\_FP\_LIST for white list of finger prints.
* [Revision #8680b57](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8680b57)\
  2015-04-07 17:06:35 +0200
  * Minor windows fixes
* [Revision #ec631f3](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ec631f3)\
  2015-03-19 20:42:16 +0100\
  \*
  * Don't include curl.h if LIBCURL is not installed - Export utf16le charset
* [Revision #bf33a4e](https://github.com/mariadb-corporation/mariadb-connector-c/commit/bf33a4e)\
  2015-03-18 20:03:02 +0100
  * Added missing file ma\_io.c:
* [Revision #95724c8](https://github.com/mariadb-corporation/mariadb-connector-c/commit/95724c8)\
  2015-03-18 19:52:51 +0100
  * Added support for remote files via plugin.
* [Revision #77251b0](https://github.com/mariadb-corporation/mariadb-connector-c/commit/77251b0)\
  2015-03-18 19:15:22 +0100
  * my\_free now expects only 1 paraemter: void \*ptr. This will allow us to share code between connector and server (e.g. dynamic columns)
* [Revision #11bcd44](https://github.com/mariadb-corporation/mariadb-connector-c/commit/11bcd44)\
  2015-03-18 18:21:47 +0100
  * Last commit (fix for [CONC-127](https://jira.mariadb.org/browse/CONC-127)) was incomplete for unknown reason
* [Revision #f8ebc60](https://github.com/mariadb-corporation/mariadb-connector-c/commit/f8ebc60)\
  2015-03-15 19:10:33 +0100
  * Fix for [CONC-127](https://jira.mariadb.org/browse/CONC-127): MariaDB Connector/C accepts dummy/self signed CA's
* [Revision #0612563](https://github.com/mariadb-corporation/mariadb-connector-c/commit/0612563)\
  2015-02-14 16:07:51 +0100
  * Add toolchain file for linux\_x86 cross compiling
* [Revision #ad50f9c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ad50f9c)\
  2015-02-08 21:25:06 +0100
  * Fix for [CONC-121](https://jira.mariadb.org/browse/CONC-121): Don't ship my\_config.h in source packages - it will be created during cmake
* [Revision #0b5a685](https://github.com/mariadb-corporation/mariadb-connector-c/commit/0b5a685)\
  2015-02-06 06:48:56 +0100
  * Fix for [CONC-120](https://jira.mariadb.org/browse/CONC-120): mariadb\_deinitialize\_ssl was declared as uint (which requires including my\_global.h) instead of unsigned int
* [Revision #7716833](https://github.com/mariadb-corporation/mariadb-connector-c/commit/7716833)\
  2015-02-04 10:35:27 +0100
  * removed sqlite plugin
* [Revision #fed2447](https://github.com/mariadb-corporation/mariadb-connector-c/commit/fed2447)\
  2015-02-03 21:35:53 +0100
  * removed SQLLite option

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
