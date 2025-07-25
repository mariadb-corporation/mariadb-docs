# Connector/C++ 1.1.4 Release Notes

The most recent [_**Stable**_](../../../community-server/about/release-criteria.md) _**(GA)**_ release of MariaDB Connector/C++ is:[**MariaDB Connector/C++ 1.1.6**](mariadb-connector-cpp-1-1-6-release-notes.md)

[Download Now](https://mariadb.com/downloads/connectors/connectors-data-access/cpp-connector)

**Release date:** 2024-06-07

This is a [_**Stable (GA)**_](../../../community-server/about/release-criteria.md) release of MariaDB Connector/C++.

**For a description of this library see the**[**MariaDB Connector/C++**](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp) **page.**

This is a GA release of the [MariaDB Connector/C++ 1.1](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/about-mariadb-connector-cpp/README.md) series, the interface between C++ applications, and MariaDB Server. MariaDB Connector/C++ enables development of C++ applications using a JDBC-based API, which is also used by MariaDB Connector/JDBC.

MariaDB Connector/C++ in its current implementation uses the MariaDB protocol via the MariaDB Connector/C API. Connector/C 3.3.10 is used in this release.

## Notable Changes

* The false or nullptr value used for boolean connection property initialization is now treated as false. It used to end up as true because SQLString makes an empty string out of nullptr, which is rendered true for the connection property. This fix introduced a 3rd state for the SQLString, NULL, and makes such a string as a value option to be treated as false. However, the NULL string will still have an empty string value in different string operations. Setting or changing its value does not make the string NULL. This "Nulliness" is still intended mainly for the driver's internal use and is designed to not change anything for applications. Though when exposed to application comparison operators, such as == and !=, they will consider the NULL state of the SQLString object if compared with nullptr. ([CONCPP-130](https://jira.mariadb.org/browse/CONCPP-130))

## Bugs Fixed

* Newly introduced and referenced header files were missing in the MSI package ([CONCPP-129](https://jira.mariadb.org/browse/CONCPP-129))

## Installation

* [Install MariaDB Connector/C++](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-cpp/install-mariadb-connector-cpp)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
