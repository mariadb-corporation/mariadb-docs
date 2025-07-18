# Connector/C++ 1.1.3 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C++ is:[**MariaDB Connector/C++ 1.1.6**](mariadb-connector-cpp-1-1-6-release-notes.md)

[Download Now](https://mariadb.com/downloads/connectors/connectors-data-access/cpp-connector)

**Release date:** 2024-02-21

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of MariaDB Connector/C++.

**For a description of this library see the**[**MariaDB Connector/C++**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp) **page.**

[MariaDB Connector/C++](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-cpp/README.md) is the interface between C++ applications and MariaDB Server. MariaDB Connector/C++ enables development of C++ applications using a JDBC-based API, which is also used by MariaDB Connector/JDBC. This is the first GA release of the MariaDB Connector/C++ 1.1 series.

MariaDB Connector/C++ in its current implementation uses the MariaDB protocol via the MariaDB Connector/C API. Connector/C 3.3.3 is used in this release.

## Notable Changes

* Added new Prepared Statement Cache ([CONCPP-111](https://jira.mariadb.org/browse/CONCPP-111))
  * The cache can be enabled by the `cachePrepStmts = on` option when the `useServerPrepStmts = on` option is also used. The use of cache is controlled by following connection properties:
    * `cachePrepStmts` enables/disables use of cache, by default is false
    * `prepStmtCacheSize` sets the size of cache, by default 250
    * `prepStmtCacheSqlLimit` limits the maximum size of the query, that may be cached. Default is 2048. This value consists of length of query itself + length of schema name + 1
* Added Connector Level Logging Functionality to C/C++ ([CONCPP-123](https://jira.mariadb.org/browse/CONCPP-123))
  * Logging can be enabled for errors, warnings, debug information, and tracing. It is controlled by the following 2 connection properties:
    * `log` non-zero value turns on logging and determines logging level. 1 `= error`, 2 `= warning`, 3 `= info`, 4 `= debug`, and 5 `= trace`
    * `logname` The name of file to write the log in. If logname set, and log is not, log will be set to 1(error). Default name is `mariadbccpp.log`, and it's written to `%TEMP%` or `%USERPROFILE%` or current dir on Windows, and in `$HOME` or in `/tmp` on other systems. Logging is synchronized between threads, but not between processes.
* Packages for Red Hat (rpm) and Debian/Ubuntu (deb) added

## Issues Fixed

* Calling close() on the Connection object causes closing of all Statement objects created on this connection ([CONCPP-119](https://jira.mariadb.org/browse/CONCPP-119))
* If connection is obtained from the pool with wrong credentials, the exception is not thrown right away ([CONCPP-97](https://jira.mariadb.org/browse/CONCPP-97))
* Connection pool would leak some memory on idle item removal from the pool ([CONCPP-118](https://jira.mariadb.org/browse/CONCPP-118))
* If pool is used connectTimeout is not respected is some cases ([CONCPP-120](https://jira.mariadb.org/browse/CONCPP-120))
* Connection returned from the pool may be marked and behave as closed ([CONCPP-121](https://jira.mariadb.org/browse/CONCPP-121))
* Crashes in pool because of incorrect synchronization ([CONCPP-122](https://jira.mariadb.org/browse/CONCPP-122))

## Installation

* [Install MariaDB Connector/C++](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp/install-mariadb-connector-cpp)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
