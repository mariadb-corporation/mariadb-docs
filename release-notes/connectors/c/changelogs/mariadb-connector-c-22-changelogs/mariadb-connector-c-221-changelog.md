# MariaDB Connector/C 2.2.1 Changelog

The most recent [_**Stable**_](../../../../mariadb-release-criteria.md) _**(GA)**_ release of MariaDB Connector/C is:[**MariaDB Connector/C 3.4.5**](../../mariadb-connector-c-3-4-release-notes/mariadb-connector-c-3-4-5-release-notes.md)

[Download](https://downloads.mariadb.org/connector-c/2.2.1)[Release Notes](../../mariadb-connector-c-22-release-notes/mariadb-connector-c-221-release-notes.md)[Changelog](mariadb-connector-c-221-changelog.md)[About MariaDB Connector/C](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-c/README.md)

**Release date:** 18 Nov 2015

For the highlights of this release, see the[release notes](../../mariadb-connector-c-22-release-notes/mariadb-connector-c-221-release-notes.md).

The revision number links will take you to the revision's page on GitHub. On[GitHub](https://github.com/MariaDB/mariadb-connector-c/) you can view more details of the revision and view diffs of the code\
modified in that revision.

* [Revision #11b367c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/11b367c)\
  2015-11-17 10:03:56 +0100
  * [CONC-147](https://jira.mariadb.org/browse/CONC-147): TCP address binding for mysql client library On clients with multiple possible TCP routes to a server it's now possible to specify an IP address to connect to the server. The IP address can be set either via mysql\_options and MYSQL\_OPT\_BIND or by "bind-address=value" in configuration file.
* [Revision #9769a43](https://github.com/mariadb-corporation/mariadb-connector-c/commit/9769a43)\
  2015-11-16 13:39:14 +0100
  * Include sign/target\_info macros
* [Revision #d5944d4](https://github.com/mariadb-corporation/mariadb-connector-c/commit/d5944d4)\
  2015-11-16 13:13:37 +0100
  * Windows build fixes: Support external sign command (if verisign is too slow or not responding) Added version\_info for static and dynamic libraries
* [Revision #73a8261](https://github.com/mariadb-corporation/mariadb-connector-c/commit/73a8261)\
  2015-11-14 11:19:30 +0100
  * Fixes for Windows Visual Studio 2015 build
* [Revision #cfdeb95](https://github.com/mariadb-corporation/mariadb-connector-c/commit/cfdeb95)\
  2015-11-12 14:19:19 +0100
  * Fixed bug in mysql\_ssl\_set (intoduced by merge from 3.0 development tree) Fixed ssl test
* [Revision #604346c](https://github.com/mariadb-corporation/mariadb-connector-c/commit/604346c)\
  2015-11-12 05:20:07 +0100
  * mysql\_asnc fixes: - check if ucontext.h is available - set error if stacksize allocation fails
* [Revision #ec26c03](https://github.com/mariadb-corporation/mariadb-connector-c/commit/ec26c03)\
  2015-11-09 11:54:10 +0100
  * Fixed compiler warning
* [Revision #74f8adf](https://github.com/mariadb-corporation/mariadb-connector-c/commit/74f8adf)\
  2015-11-09 11:36:31 +0100
  * Since CPack doesn't deliver expected results on windows, we now build source packages directly from git (git archive). To activate this option, define GIT\_BUILD\_SRCPKG: cmake . -DGIT\_BUILD\_SRCPKG=1
* [Revision #4bef072](https://github.com/mariadb-corporation/mariadb-connector-c/commit/4bef072)\
  2015-11-09 09:11:05 +0100
  * exclude unittests from archives
* [Revision #29aa0c9](https://github.com/mariadb-corporation/mariadb-connector-c/commit/29aa0c9)\
  2015-11-08 16:28:37 +0100
  * Fixed warnings Disabled ps query cache
* [Revision #a7ce3ad](https://github.com/mariadb-corporation/mariadb-connector-c/commit/a7ce3ad)\
  2015-11-04 07:06:39 +0100
  * Windows build fixes
* [Revision #052e5db](https://github.com/mariadb-corporation/mariadb-connector-c/commit/052e5db)\
  2015-11-03 14:25:18 +0100
  * Set socket to blocking after connect
* [Revision #4c794e5](https://github.com/mariadb-corporation/mariadb-connector-c/commit/4c794e5)\
  2015-10-28 22:02:02 +0100
  * Fixed compiler warnings in ps\_bugs.c and client\_plugin.c
* [Revision #8bf167b](https://github.com/mariadb-corporation/mariadb-connector-c/commit/8bf167b)\
  2015-10-28 15:53:39 +0200
  * Fix for mariadb\_convert\_string - charset names for utf16 and utf32 are changed so iconv understands it. Also if endianness is not specified, BE charsets used by default, to avoid BOMs Names mapped for both source and destination charsets. Also the regression test for this change is added to charset.c
* [Revision #3431674](https://github.com/mariadb-corporation/mariadb-connector-c/commit/3431674)\
  2015-10-28 13:32:49 +0100
  * Bumped patch number
* [Revision #a272706](https://github.com/mariadb-corporation/mariadb-connector-c/commit/a272706)\
  2015-10-08 13:36:22 +0300
  * Fix for mariadb\_convert\_string function. Fix of the charset name in case of Utf16 - iconv digests UTF-16, and not UTF16, as destination charset. Also we always use either BE or LE for utf16, to avoid BOM in the result string.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
