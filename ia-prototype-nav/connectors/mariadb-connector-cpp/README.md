---
description: >-
  The MariaDB Connector/C++ is used to connect applications developed in C++ to
  MariaDB and MySQL databases. MariaDB Connector/C++ is LGPLv2.1 licensed.
icon: link
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
  actions:
    visible: true
---

# Connector/C++

MariaDB Connector/C++ is the C++ client library for connecting C++ applications to MariaDB and MySQL databases. It is LGPLv2.1 licensed.

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/mariadb-connector-c++-guide" %}
[mariadb-connector-c++-guide.md]({connectors}/mariadb-connector-cpp/mariadb-connector-c++-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview and quickstart guide for MariaDB Connector/C++.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/application-development-with-mariadb-connector-cpp" %}
[application-development-with-mariadb-connector-cpp.md]({connectors}/mariadb-connector-cpp/application-development-with-mariadb-connector-cpp)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
C++ applications built with MariaDB Connector/C++ use the `sql` namespace classes for connections, prepared statements, and result sets to interact with MariaDB databases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/batch-operations-with-mariadb-connector-cpp" %}
[batch-operations-with-mariadb-connector-cpp.md]({connectors}/mariadb-connector-cpp/batch-operations-with-mariadb-connector-cpp)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports batch (bulk) operations by queuing commands on a `sql::Statement` or `sql::PreparedStatement` with `addBatch()` and sending them to the server in a single `executeBatch()` call.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/connect-with-mariadb-connectorcpp" %}
[connect-with-mariadb-connectorcpp.md]({connectors}/mariadb-connector-cpp/connect-with-mariadb-connectorcpp)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports JDBC and compatibility URL syntax, optional connection parameters, and two connection methods via `sql::Driver` and `sql::DriverManager` for C++ applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/ddl-with-mariadb-connector-cpp" %}
[ddl-with-mariadb-connector-cpp.md]({connectors}/mariadb-connector-cpp/ddl-with-mariadb-connector-cpp)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports DDL operations such as `ALTER TABLE` and `TRUNCATE TABLE`, letting C++ applications modify database schema using the `sql::Statement` class.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/dml-with-mariadb-connector-cpp" %}
[dml-with-mariadb-connector-cpp.md]({connectors}/mariadb-connector-cpp/dml-with-mariadb-connector-cpp)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports DML operations including `INSERT`, `UPDATE`, `DELETE`, and `SELECT`, using prepared statements and result sets to manipulate data in MariaDB databases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/install-mariadb-connector-cpp" %}
[install-mariadb-connector-cpp.md]({connectors}/mariadb-connector-cpp/install-mariadb-connector-cpp)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MariaDB Connector/C++ on Linux using RPM, DEB, or binary tarball packages, or on Windows using the MSI installer, with MariaDB Connector/C as a prerequisite.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/mariadb-connector-cpp-sample-application" %}
[mariadb-connector-cpp-sample-application.md]({connectors}/mariadb-connector-cpp/mariadb-connector-cpp-sample-application)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
`Tasks.cpp` is a complete MariaDB Connector/C++ sample demonstrating CRUD operations, with setup instructions, compilation steps, and command-line usage for a task management database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/setup-for-connector-cpp-examples" %}
[setup-for-connector-cpp-examples.md]({connectors}/mariadb-connector-cpp/setup-for-connector-cpp-examples)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create the schema and user account prerequisites for MariaDB Connector/C++ documentation examples, including the test database, contacts table, and appropriate `GRANT` statements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-cpp/transactions-with-mariadb-connector-cpp" %}
[transactions-with-mariadb-connector-cpp.md]({connectors}/mariadb-connector-cpp/transactions-with-mariadb-connector-cpp)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports multi-statement transactions with manual commit, rollback, and savepoints by disabling auto-commit on the `sql::Connection` object.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
