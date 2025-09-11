# Connector/C++ 1.1.6 Release Notes

[Download Now](https://mariadb.com/downloads/connectors/connectors-data-access/cpp-connector)

**Release date:** 14 Mar 2025

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of MariaDB Connector/C++.

**For a description of this library see the**[**MariaDB Connector/C++**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp) **page.**

[MariaDB Connector/C++](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/about-mariadb-connector-cpp/README.md) is the interface between C++ applications and MariaDB Server. MariaDB Connector/C++ enables development of C++ applications using a JDBC-based API, which is also used by MariaDB Connector/J.

MariaDB Connector/C++ implements the MySQL protocol using the MariaDB Connector/C API. This release depends on MariaDB Connector/C 3.3.14.

## Notable Changes

* [CONCPP-138](https://jira.mariadb.org/browse/CONCPP-138) - The Driver now always cache all binary results to avoid access violation error while using result-set created with server prepared statements after the connection object has been closed. In case result-set streaming is used results naturally are not cached, but operations on the result-set after statement/connection is closed will cause SQLException to be thrown that the result-set is closed because of that
* [CONCPP-140](https://jira.mariadb.org/browse/CONCPP-140) - reconnect and reset methods in the Connection interface are deprecated
* [CONCPP-141](https://jira.mariadb.org/browse/CONCPP-141) - if `trustServerCertificate` is `true`(this is default) the connector will explicitly disable certificate verification. This enables work of the connector with Connector/C v.3.4 for unencrypted connection on the platforms there Connector/C is linked dynamically. Setting the option to `false` enables certificate verification.
* Fixed possible crash in case of use of setBytes() method if passed sql::bytes object did not own the bytes array, but referenced C array

## Bugs Fixed

* [CONCPP-134](https://jira.mariadb.org/browse/CONCPP-134) - Removed volatile deprecation build warnings
* [CONCPP-136](https://jira.mariadb.org/browse/CONCPP-136) - With default settings the driver uses slowest possible batch executing method
* [CONCPP-137](https://jira.mariadb.org/browse/CONCPP-137) - Inconsistent types naming of the names returned by ResultSetMetaData::getColumnTypeName()

## Installation

[Install MariaDB Connector/C++](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp/install-mariadb-connector-cpp)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
