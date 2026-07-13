---
description: >-
  Learn to use MariaDB Connector/R2DBC's native API. This guide details direct
  interaction for reactive, non-blocking database operations, offering
  fine-grained control over data access in Java applications.
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

# Using the Native R2DBC API of MariaDB Connector/R2DBC

Use MariaDB Connector/R2DBC directly through the native R2DBC API for reactive, non-blocking database access with fine-grained control.

{% columns %}
{% column %}
{% content-ref url="application-development-with-mariadb-connector-r2dbc-native-api.md" %}
[application-development-with-mariadb-connector-r2dbc-native-api.md](application-development-with-mariadb-connector-r2dbc-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Application development with the MariaDB Connector/R2DBC native API covers building Java projects with Maven or JAR, adding the connector to the classpath, and running compiled applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="batch-operations-with-mariadb-connector-r2dbc-native-api.md" %}
[batch-operations-with-mariadb-connector-r2dbc-native-api.md](batch-operations-with-mariadb-connector-r2dbc-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Batch operations with the MariaDB Connector/R2DBC native API group multiple DML statements into a single `io.r2dbc.spi.Batch` to reduce per-statement network overhead.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-with-mariadb-connector-r2dbc-native-api.md" %}
[connect-with-mariadb-connector-r2dbc-native-api.md](connect-with-mariadb-connector-r2dbc-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Connecting to MariaDB with the native R2DBC API uses `MariadbConnectionConfiguration` and `MariadbConnectionFactory` to create and manage reactive client connections via `io.r2dbc.spi.Connection`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connection-pools-with-mariadb-connector-r2dbc-native-api.md" %}
[connection-pools-with-mariadb-connector-r2dbc-native-api.md](connection-pools-with-mariadb-connector-r2dbc-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Connector/R2DBC native API supports connection pooling via `r2dbc-pool`, holding reactive connections open for reuse and configuring them with `ConnectionPoolConfiguration`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ddl-with-mariadb-connector-r2dbc-native-api.md" %}
[ddl-with-mariadb-connector-r2dbc-native-api.md](ddl-with-mariadb-connector-r2dbc-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
DDL operations with the MariaDB Connector/R2DBC native API execute schema statements such as `CREATE TABLE` and `ALTER TABLE` reactively using `io.r2dbc.spi.Statement` and `io.r2dbc.spi.Result`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dml-with-mariadb-connector-r2dbc-native-api.md" %}
[dml-with-mariadb-connector-r2dbc-native-api.md](dml-with-mariadb-connector-r2dbc-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
DML with the MariaDB Connector/R2DBC native API executes `INSERT`, `UPDATE`, `DELETE`, and `SELECT` reactively using `io.r2dbc.spi.Statement`, `Result`, `Row`, and `RowMetadata` classes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="install-mariadb-connector-r2dbc.md" %}
[install-mariadb-connector-r2dbc.md](install-mariadb-connector-r2dbc.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MariaDB Connector/R2DBC via Maven by adding the `r2dbc-mariadb` dependency to `pom.xml`, or manually by downloading the JAR and adding it to the Java CLASSPATH alongside `r2dbc-pool`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="r2dbc-code-example-native-api.md" %}
[r2dbc-code-example-native-api.md](r2dbc-code-example-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete Java code example using the MariaDB Connector/R2DBC native API to query a MariaDB table with `MariadbConnectionFactory` and reactive `Flux` result handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setup-for-connector-r2dbc-examples-native-api.md" %}
[setup-for-connector-r2dbc-examples-native-api.md](setup-for-connector-r2dbc-examples-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up the test database, contact table, and user account required by the MariaDB Connector/R2DBC native API code examples in this documentation section.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-with-mariadb-connector-r2dbc-native-api.md" %}
[transactions-with-mariadb-connector-r2dbc-native-api.md](transactions-with-mariadb-connector-r2dbc-native-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Connector/R2DBC native API requires manual subscription for `beginTransaction`, `commitTransaction`, and `rollbackTransaction`; Spring Data R2DBC provides managed transactions.
{% endcolumn %}
{% endcolumns %}
