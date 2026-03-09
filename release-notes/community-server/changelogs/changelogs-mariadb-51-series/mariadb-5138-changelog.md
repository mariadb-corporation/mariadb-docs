# MariaDB 5.1.38 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.38) | [Release Notes](../../old-releases/5.1/5.1.38.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 29 Oct 2009

MariaDB-5.1.38-beta is based on MySQL-5.1.38, but has these additional changes\
and bug fixes:

* mysql-test-run now has options `--stop-file` and `--stop-keep-alive` (also\
  accessible with environment variables MTR\_STOP\_FILE and MTR\_STOP\_KEEP\_ALIVE).\
  With these, it is possible to pause a running test temporarily and let it\
  continue later. See [mysql-test-run](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-test).
* Improvements to Gcov support in testing.
* New column [TIME\_MS in SHOW\
  FULL PROCESSLIST and INFORMATION\_SCHEMA.PROCESSLIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist), similar to the old\
  TIME column, but with microsecond resolution. Also fixes old TIME column to\
  not be influenced by @TIMESTAMP. Patch by Percona.
* Optimizer improvement: Table elimination ([MWL#17](https://askmonty.org/worklog/?tid=17)). See [Table Elimination](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/table-elimination).
* Enhancements to slow log. Includes details of execution plan and\
  microsecond-precision resolution. Based on microslow patch by Percona. See [Slow Query Log Extended Statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/slow-query-log-extended-statistics).
* PBXT storage engine. PBXT is developed by [PrimeBase Technologies](https://www.primebase.org).
* [XtraDB storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) version 6 as a replacement\
  for the MySQL built-in InnoDB. XtraDB is based on the Oracle/Innobase InnoDB\
  plugin version 1.0.3, with enhancements. XtraDB is developed by Percona.
* Performance improvements for common cases of character set conversion. See [Character Sets and Collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations) for a list of\
  the character sets and collations included with MariaDB.
* [Pool-of-threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb-51-53), allowing to map a high number of simultaneous connections\
  onto a lower number of operating system treads, to reduce overhead with using\
  large number of threads.
* New handler call prepare\_index\_scan() and other small improvements to the\
  internal storage engine handler API.
* ./configure now outputs a summary section at the end of the output. (By C.J.\
  Adams-Collier).
* NDB storage engine disabled in MariaDB builds. (NDB is not supported in\
  MariaDB).
* Added `--abort-source-on-error` to the [mysql\
  client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mysql-command-line-client).
* [Faster CHECKSUM TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/checksum-table).
* Debugging code to check for taking mutexes in the wrong order, which enables\
  to catch potential deadlocks in the server code.
* [Maria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) storage engine. The Maria storage engine is an enhanment over the\
  MyISAM storage engine which provides journaling and crash recovery.
* Added new startup option and test commands to [mysqltest](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-test).

## Bug Fixes

* mysqlslap: setting `--engine` does not get replicated ([MySQL Bug #46967](https://bugs.mysql.com/bug.php?id=46967)).
* mysqlslap: specifying `--engine` and `--create` does not work with`--engine=<storage_engine>:<option>`\
  ([Bug #429773](https://bugs.launchpad.net/bugs/429773)).
* rpl\_do\_grant fails on PB-2 with a failing connect\
  ([MySQL Bug #47016](https://bugs.mysql.com/bug.php?id=47016)).
* Windows: mysql-test-run `--log-error` fixed to not add `--console`. See [mysql-test-run](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-test).
* The myisam\_crash\_before\_flush\_keys test fails on Windows ([MySQL Bug #47455](https://bugs.mysql.com/bug.php?id=47455)).
* rpl.rpl\_get\_master\_version\_and\_clock fails on hpux11.31 ([MySQL Bug #46931](https://bugs.mysql.com/bug.php?id=46931))
* safe\_process: FATAL ERROR, Unknown option: `--nocore` ([MySQL Bug #46212](https://bugs.mysql.com/bug.php?id=46212)).
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb) crashes on startup on windows ([Bug #417751](https://bugs.launchpad.net/bugs/417751))
* Eliminate compiler warnings.
* Fix parsing of enum-valued options for plugins ([Bug #423035](https://bugs.launchpad.net/bugs/423035))
* Solaris build fixes.
* query\_cache\_debug.test fails ([MySQL Bug #45632](https://bugs.mysql.com/bug.php?id=45632)).
* enum-style command-line options are not honoured (maria.maria-recover fails)\
  ([MySQL Bug #41010](https://bugs.mysql.com/bug.php?id=41010))
* [mysql-test-run](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-test) sometimes terminated mysqld early, causing loss of memory leak\
  error reports from Valgrind and GCov test coverage output ([MySQL Bug #43418](https://bugs.mysql.com/bug.php?id=43418)).
* Several Valgrind reported bugs in the source code fixed.
* Save SAFE\_MUTEX configure #define in config.h, to facilitate correct build\
  options for plugins.
* test maria.maria fails if server built without '`--with-partition`'\
  ([Bug #330611](https://bugs.launchpad.net/bugs/330611)).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
