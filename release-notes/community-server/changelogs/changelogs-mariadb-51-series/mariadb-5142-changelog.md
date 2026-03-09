# MariaDB 5.1.42 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.42) | [Release Notes](../../old-releases/5.1/5.1.42.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 01 Feb 2010

See the [MariaDB 5.1.42 Release Notes](../../old-releases/5.1/5.1.42.md) for the\
highlights of this release.

MariaDB-5.1.42 is based on MySQL-5.1.42, and in addition to the changes listed\
in previous [changelogs](../../../connectors/odbc/changelogs/) it includes the following changes and bug fixes:

* Includes MySQL 5.1.42
* Includes [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) 1.0.6-9
* Includes PBXT 1.0.09f RC3
* Includes [FederatedX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/federatedx-storage-engine)
* Added page fault counters for SHOW PROFILE on Windows.
* Fixed bug where one connection didn't see newly committed data from another\
  connection.
* Fix multiple test suite failures in Buildbot due to races in the test cases\
  or missing server features not properly checked.
* Make test case deterministic by replacing sleep with\
  include/wait\_condition.inc
* Move test from main.trigger to main.trigger\_notembedded, as it now depends on\
  INFORMATION\_SCHEMA.PROCESSLIST (rather than sleeps) to synchronise.
* Fixed bug where mysqlbinlog hold up multiple connections to MySQL when using\
  mysqlbinlog -R file1 file2 ...
* Merged patch from Percona to get proper fix for compilation issue of\
  srv0srv.c on Solaris
* Fixed compile errors on windows.
* Fixed that we use same flags when testing for assembler as by makefiles.
* Fixed bug in locking by triggers found by test case when compiling without\
  query cache.
* Fixed xtradb/handler/ha\_innodb.cc to call explain\_filename()
* Removed not needed test file (that caused embedded server to fail).
* Fix for XtraDB 9: missing DBUG\_RETURN.
* Fix crashes by taking kernel mutex when calling srv\_table\_reserve\_slot()\
  during thread startup.
* Apply to XtraDB MySQL/build-in innodb patches for [MySQL Bug #49032](https://bugs.mysql.com/bug.php?id=49032) and [MySQL Bug #47720](https://bugs.mysql.com/bug.php?id=47720).
* Fix freed-twice error in XtraDB (from InnoDB plugin 1.0.6).
* Fixed race condition when innobase\_shutdown\_for\_mysql() was called before\
  parser was initialized (as it's initialized on first usage).
* Fixes for some randomly occuring test failures in Buildbot.
* Fix for [Bug #509795](https://bugs.launchpad.net/bugs/509795): Result of reverse\_lookup("localhost") is system\
  dependent. Therefore we disable the result of it.
* \[SECURITY] yaSSL cert info buffer overflow fix. Fixes [CVE-2009-4484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-4484).
* Fix Windows test failures in binlog tests in certain time zones. Thanks to\
  Alex Budovski for helping with this.
* Fixed some compiler warnings and errors in test suite and compiler warnings\
  from OpenSolaris build.
* Add support in bintar build script for OpenSolaris.
* When compiling with debug, don't clear buffer in 'net\_clear()' - This allows\
  us to easier find bugs in the protocol and also get repeatable test failures\
  in test cases where someone forgot to do `--reap`
* Changed version number from RC to stable
* Fixed bug in Yassle to get correct error messages in case of errors
* Provide better error messages in case of SSL connect failure
* Updated out-of-date SSL certificates to fix failing mysql-test-system\
  (certificates now active for 10 years)
* Fixed bug in query\_cache that could cause asserts and hangs in DEBUG builds.
* Fixed bug where one connection did not see changes done by another\
  connection.
* Fix for [MySQL Bug #31173](https://bugs.mysql.com/bug.php?id=31173): mysqlslap.exe crashes if called without any parameters
* Fix Windows build of embedded server (forgotten dependency).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
