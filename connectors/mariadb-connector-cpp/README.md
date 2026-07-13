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
{% content-ref url="mariadb-connector-c++-guide.md" %}
[mariadb-connector-c++-guide.md](mariadb-connector-c++-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview and quickstart guide for MariaDB Connector/C++.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="application-development-with-mariadb-connector-cpp.md" %}
[application-development-with-mariadb-connector-cpp.md](application-development-with-mariadb-connector-cpp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
C++ applications built with MariaDB Connector/C++ use the `sql` namespace classes for connections, prepared statements, and result sets to interact with MariaDB databases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-with-mariadb-connectorcpp.md" %}
[connect-with-mariadb-connectorcpp.md](connect-with-mariadb-connectorcpp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports JDBC and compatibility URL syntax, optional connection parameters, and two connection methods via `sql::Driver` and `sql::DriverManager` for C++ applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ddl-with-mariadb-connector-cpp.md" %}
[ddl-with-mariadb-connector-cpp.md](ddl-with-mariadb-connector-cpp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports DDL operations such as `ALTER TABLE` and `TRUNCATE TABLE`, letting C++ applications modify database schema using the `sql::Statement` class.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dml-with-mariadb-connector-cpp.md" %}
[dml-with-mariadb-connector-cpp.md](dml-with-mariadb-connector-cpp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports DML operations including `INSERT`, `UPDATE`, `DELETE`, and `SELECT`, using prepared statements and result sets to manipulate data in MariaDB databases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="install-mariadb-connector-cpp.md" %}
[install-mariadb-connector-cpp.md](install-mariadb-connector-cpp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MariaDB Connector/C++ on Linux using RPM, DEB, or binary tarball packages, or on Windows using the MSI installer, with MariaDB Connector/C as a prerequisite.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-connector-cpp-sample-application.md" %}
[mariadb-connector-cpp-sample-application.md](mariadb-connector-cpp-sample-application.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
`Tasks.cpp` is a complete MariaDB Connector/C++ sample demonstrating CRUD operations, with setup instructions, compilation steps, and command-line usage for a task management database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setup-for-connector-cpp-examples.md" %}
[setup-for-connector-cpp-examples.md](setup-for-connector-cpp-examples.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create the schema and user account prerequisites for MariaDB Connector/C++ documentation examples, including the test database, contacts table, and appropriate `GRANT` statements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-with-mariadb-connector-cpp.md" %}
[transactions-with-mariadb-connector-cpp.md](transactions-with-mariadb-connector-cpp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/C++ supports multi-statement transactions with manual commit, rollback, and savepoints by disabling auto-commit on the `sql::Connection` object.
{% endcolumn %}
{% endcolumns %}
