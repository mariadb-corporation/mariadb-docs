# Connector/C++ 1.0.4 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C++ is:[**MariaDB Connector/C++ 1.1.6**](../mariadb-connector-cpp-1-1-release-notes/mariadb-connector-cpp-1-1-6-release-notes.md)

[Download Now](https://mariadb.com/downloads/connectors/connectors-data-access/cpp-connector)

**Release date:** 2024-10-21

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of MariaDB Connector/C++.

**For a description of this library see the** [**MariaDB Connector/C++**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp) **page.**

[MariaDB Connector/C++](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp) is the interface between C++ applications and MariaDB Server. MariaDB Connector/C++ enables development of C++ applications using a JDBC-based API, which is also used by MariaDB Connector/J.

MariaDB Connector/C++ implements the MySQL protocol using the MariaDB Connector/C API. This release depends on MariaDB Connector/C 3.3.11.

## Bugs Fixed

`getMoreResults()` may pick other statement result if the first statement used text protocol ([CONCPP-132](https://jira.mariadb.org/browse/CONCPP-132))

Driver fails to cache multiple results in case other query requires the connection and that will cause "commands out of sync" errors ([CONCPP-133](https://jira.mariadb.org/browse/CONCPP-133))

## Installation

[Install MariaDB Connector/C++](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp/install-mariadb-connector-cpp)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
