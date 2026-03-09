# MariaDB 5.1.41 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.41) | [Release Notes](../../old-releases/5.1/5.1.41.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 13 Jan 2010

See the [MariaDB 5.1.41 Release Notes](../../old-releases/5.1/5.1.41.md) for the\
highlights of this release.

MariaDB-5.1.41 RC is based on MySQL-5.1.41, and in addition to the changes\
listed in the [5.1.39](mariadb-5139-changelog.md) and [5.1.38](mariadb-5138-changelog.md) changelogs it includes these additional\
changes and bug fixes:

* Includes MySQL 5.1.41
* Includes [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) 1.0.4-8
* Includes [PBXT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/obsolete-replication-information/mariadb-52-replication-feature-preview#pbxt-consistent-commit-ordering) 1.0.09f RC3
* Includes [FederatedX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/federatedx-storage-engine)
* Fixed typos of `--engine` help text.
* Added page fault counters for SHOW PROFILE on Windows.
* Fixed bug where one connection didn't see newly committed data from another\
  connection.
* Safety change to ensure read/black trees (used with heap tables) works on 64\
  bit setups where `ulong <> size_t`
* Don't retry test cases by default
* Fixed bug where we could (under unlikely error conditions) access not\
  initialized variable
* Added error handling for my\_seek() & my\_tell() failures
* Fixed [Bug #485443](https://bugs.launchpad.net/bugs/485443) `--with-fast-mutexes` and without safe mutexes (debug\
  build) maria do not builds
* Added 'mariadb\_SERVER' as extra config group for MariaDB embedded server
* Apply the strict aliasing patch from [89843](https://lists.mysql.com/commits/89843)
* Remove compiler warnings (Including some warnings from -Wstrict-aliasing)
* Don't use static link by default (in compile-pentium) as some new systems\
  don't have all static libraries available
* Change type for functions in plugin.h:str\_mysql\_ftparser\_param() to const\
  unsigned char and string lengths to size\_t.
  * One effect of the above change is that one needs to include mysql\_global.h\
    or define size\_t before including plugin.h
  * This fixes a case where mysql\_client\_test failed with newer gcc that enables\
    strict-aliasing by default
* Added protection around usage of thd->mysys\_var (May be changed to 0 by\
  scheduler)
* Fix for [MySQL Bug #48357](https://bugs.mysql.com/bug.php?id=48357) SHOW BINLOG EVENTS: Wrong offset or I/O error
* Removed some not needed casts
* Change plugin.h to be 'binary compatible' with old versions
* Added mysql\_ft\_size\_t typedef to plugin.h to make it trivial to change string\
  lengths to size\_t on next ABI change
* Protect stack->keywords with THR\_LOCK\_dbug
  * This solves a core dump in MariaDB when one sets the GLOBAL.DEBUG variable\
    in mysql-test-run when other threads are checking the keyword list
* Fixed [MySQL Bug #49474](https://bugs.mysql.com/bug.php?id=49474) Replication from 4.0 to 5.1 broken
* Changed -1 row number in some warnings to 0 (-1 doesn't make sense as a row\
  number and when doing insert / load data, first row is 1, so 0 is free to\
  use)
* Fixed [MySQL Bug #47017](https://bugs.mysql.com/bug.php?id=47017) rpl\_timezone fails on PB-2 with mismatch error
* Fixed coredump in sql\_plugin.cc:intern\_plugin\_lock() on mysqld start with\
  PBXT
* Ensure that mysql\_get\_server\_version() also works if there is a non numerical\
  prefix before the version number
* Applied patch from Alexander Barkov to fix some problems with Croatian\
  character set and LIKE queries
* Fix for PBXT running inside embedded server ([Bug #439889](https://bugs.launchpad.net/bugs/439889)). Also some\
  small fixes to make the PBXT testsuite work in `--embedded`.
* Add DB\_TYPE\_AUTOASSIGN as a better name for DB\_TYPE\_UNKNOWN, which is what\
  plugins should generally use.
* Fixed bug in my\_uuid() that caused failures on hpux and ia64
* Fixed bug in tc.log recovery code that caused crash\_commit\_before to\
  sometimes crash.
* OpenSolaris 5.11-x86 now compiles (tested with 32 bit)
* Add BUILD/compile-bintar, which builds MariaDB with correct options for a\
  binary tarball release.
* Various test suite fixes and improvements.

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
