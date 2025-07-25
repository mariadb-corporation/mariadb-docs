# Connector/C++ 1.1.0 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C++ is:[**MariaDB Connector/C++ 1.1.6**](mariadb-connector-cpp-1-1-6-release-notes.md)

[MariaDB Connector/C++](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-cpp/README.md) is the interface between C++ applications and MariaDB Server. MariaDB Connector/C++ enables development of C++ applications using a JDBC-based API, which is also used by MariaDB Connector/J.

MariaDB Connector/C++ 1.1.0 was released on 2021-08-06. This release is of Beta maturity, and should not be used with production workloads.

MariaDB Connector/C++ implements the MySQL protocol using the MariaDB Connector/C API. This release depends on Connector/C 3.2.3.

## Notable Changes

* The default connection character set is `utf8mb4`. ([CONCPP-91](https://jira.mariadb.org/browse/CONCPP-91))
* Re-execution or destruction on any type of statement object closes all of its result-sets. ([CONCPP-88](https://jira.mariadb.org/browse/CONCPP-88))
* `ResultSet` streaming is supported. The `defaultFetchSize` connection option sets the default number of rows in a result-sets retrieved at a time. The `setFetchSize` statement method sets number of rows for the statement. ([CONCPP-72](https://jira.mariadb.org/browse/CONCPP-72))

## Notable API Changes

* `ResultSet` get methods are `const` ([CONCPP-86](https://jira.mariadb.org/browse/CONCPP-86))
* `sql::Properties` class passed to connect methods is a class defined in the library. `DatabaseMetaData::getTables` accepts the `sql::List` class object. Methods still accept `std::map` and `std::list` objects. ([CONCPP-83](https://jira.mariadb.org/browse/CONCPP-83))
* `SQLString` class supports `find` methods. ([CONCPP-90](https://jira.mariadb.org/browse/CONCPP-90))
* `Properties` parameters to connect methods are `const` ([CONCPP-82](https://jira.mariadb.org/browse/CONCPP-82))
* `SQLString` constructor from `std::string` is not exported on Windows. ([CONCPP-85](https://jira.mariadb.org/browse/CONCPP-85))

## Installation

[Install MariaDB Connector/C++](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp/install-mariadb-connector-cpp)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
