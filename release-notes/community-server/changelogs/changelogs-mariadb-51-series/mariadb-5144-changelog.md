# MariaDB 5.1.44 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.44) | [Release Notes](../../old-releases/5.1/5.1.44.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 24 Mar 2010

See the [MariaDB 5.1.44 Release Notes](../../old-releases/5.1/5.1.44.md) for the\
highlights of this release.

[MariaDB 5.1.44](../../old-releases/5.1/5.1.44.md) is based on MySQL 5.1.44 and includes all changes made since\
MySQL 5.1.42, including MySQL 5.1.43. In addition to the changes listed in\
previous [changelogs](../../../connectors/odbc/changelogs/) it includes the following changes and bug fixes:

* fixed a reported performance problem with MariaDB internal temporary tables
* don't crash on failing to load a plugin with newer\
  MYSQL\_PLUGIN\_INTERFACE\_VERSION
* don't copy st\_mysql\_plugin structure unnecessary (sizeof hasn't changed)
* Fix myisam checksum patch to check for HA\_OPTION\_CHECKSUM after it was set,\
  not before
* Fix for [Bug #534626](https://bugs.launchpad.net/bugs/534626) MyISAM table created in MariaDB not readable by MySQL
* Fix for: [MySQL Bug #44987](https://bugs.mysql.com/bug.php?id=44987) DELETE IGNORE and FK constraint. Now DELETE IGNORE skips\
  over rows with a foreign key constraints (as it was supposed to do)
* Fix some compiler warnings seen in Buildbot. Add some extra error output and\
  code cleanup in an attempt to fix/debug a rare random testsuite problem in\
  check\_warnings, where the exit code from mysqltest is somehow corrupted\
  inside mysql-test-run.pl.
* Fixes for two test failures in Buildbot.
  1. Adjust timing in test case, to avoid test failures caused by high load on\
     machines and consequent race conditions in the test case.
  2. Add another variant of Valgrind suppressions for memory leak in system\
     libraries when unloading dynamic object files.
* Added count of my\_sync calls (to SHOW STATUS)
* tmp\_table\_size can now be set to 0 (to disable in memory internal temp\
  tables)
* Improved speed for internal Maria temp tables:
  * Don't use packed keys, except with long text fields.
  * Don't copy key all accessed pages during key search.
* Some new benchmark tests to sql-bench (for group by)
* do not take LOCK\_plugin for built-in plugins
* Fixed [Bug #524025](https://bugs.launchpad.net/bugs/524025): Running RQG outer\_join test leads to crash. Save\
  no-records constant tables in JOIN::const\_table\_map before we invoke\
  eliminate\_tables(). Failure to do so caused crash when the same table was\
  marked as constant two times
* fix for a possible DoS in the my\_net\_skip\_rest()
* Fixed [Bug #524679](https://bugs.launchpad.net/bugs/524679): make test ORDER BY date\_ord ASC. (Problem was missing\
  time\_zone setting)
* Fixed [Bug #523593](https://bugs.launchpad.net/bugs/523593): Running RQG optimizer\_no\_subquery crashes MariaDB.\
  When analying multiple equalities, take into account that they may not have a\
  single table field that belongs to one of the tables that we're trying to\
  eliminate (and they are not useful for table elimination in that case)
* Increased loop counts of sql-bench tests to get run times around 5 minutes on\
  current machines. Tested on a Xeon machine and a new dual core laptop.
* Fix for [Bug #516148](https://bugs.launchpad.net/bugs/516148): Test maria.maria3 fails when `--without-maria-tmp-tables`\
  is set
* Fix for [Bug #520243](https://bugs.launchpad.net/bugs/520243): useability bug of thread pool configuration. Now`mysqld --help --verbose` shows the value for thread-handling Fixed also that`mysqld --one-thread` works as expected.
* Added option `--temporary-tables` to test speed of temporary tables
* When one does a drop table, the indexes are not flushed to disk before drop\
  anymore (with MyISAM/Maria).
* myisam-recover options changed from OFF to 'DEFAULT' to get less chance of\
  data loss when using MyISAM. (The disadvantage is that changed MyISAM tables\
  will be checked at access time; Use `--myisam-recover=OFF` for old behavior)
* Don't call extra (HA\_EXTRA\_FORCE\_REOPEN) in ALTER TABLE if table is locked as\
  this will mark table as crashed!
* Added assert to detect if we accidentally would use MyISAM versioning in\
  MySQL
* Added `--connect-command="sql-string"` to sql-bench test suite. This allows one\
  to send an extra command to the mysql server to setup the environment before\
  starting tests.
* now we force at least libevent-1.4
* hide nm warnings in configure
* Support building with system libevent

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
