---
description: >-
  Learn to integrate MariaDB Connector/R2DBC with Spring Data Framework. This
  guide covers reactive, non-blocking data access using Spring Data R2DBC for
  efficient and modern Java applications.
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

# Using the Spring Data Framework with MariaDB Connector/R2DBC

## Overview

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes it more scalable than Java's standard JDBC API. MariaDB Connector/R2DBC can be used with the very popular Spring Data framework, which can provide support for repositories, object mapping, and transaction management.

This page discusses how to use MariaDB Connector/R2DBC with the Spring Data framework.

For information on how to use MariaDB Connector/R2DBC with the native R2DBC API, refer to, [Using the native API of MariaDB Connector/R2DBC](../using-the-native-r2dbc-api-of-mariadb-connector-r2dbc/).

## Spring Data R2DBC

[Spring Data R2DBC](https://spring.io/projects/spring-data-r2dbc/) allows MariaDB Connector/R2DBC to be used with the popular [Spring Data](https://spring.io/projects/spring-data/) framework, which is part of the larger [Spring Framework](https://spring.io/projects/spring-framework/).

Spring Data R2DBC is currently in incubation, so it is not yet included with the main Spring Data modules.

Spring Data R2DBC supports many features from the Spring Data framework:

| Spring Data Feature    | Supported |
| ---------------------- | --------- |
| DatabaseClient         | Yes       |
| Repositories           | Yes       |
| Object Mapping         | Yes       |
| Transaction Management | Yes       |

## In This Section

{% columns %}
{% column %}
{% content-ref url="application-development-with-mariadb-connector-r2dbc-spring-data.md" %}
[application-development-with-mariadb-connector-r2dbc-spring-data.md](application-development-with-mariadb-connector-r2dbc-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Spring Data R2DBC applications with MariaDB Connector/R2DBC require Maven, Entity classes for object mapping, and the `spring-boot-starter-data-r2dbc` dependency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="batch-operations-with-mariadb-connector-r2dbc-spring-data.md" %}
[batch-operations-with-mariadb-connector-r2dbc-spring-data.md](batch-operations-with-mariadb-connector-r2dbc-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Spring Data R2DBC batch with MariaDB Connector/R2DBC loops over statements via `DatabaseClient.execute`, replacing the native `io.r2dbc.spi.Batch` class unavailable in this framework.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect-with-mariadb-connector-r2dbc-spring-data.md" %}
[connect-with-mariadb-connector-r2dbc-spring-data.md](connect-with-mariadb-connector-r2dbc-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/R2DBC Spring Data wraps `MariadbConnectionFactory` in `DatabaseClient`, providing a higher-level reactive interface for executing queries against MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ddl-with-mariadb-connector-r2dbc-spring-data.md" %}
[ddl-with-mariadb-connector-r2dbc-spring-data.md](ddl-with-mariadb-connector-r2dbc-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Spring Data R2DBC DDL with MariaDB Connector/R2DBC uses `DatabaseClient.execute` to run schema statements including `CREATE TABLE` and `ALTER TABLE` within the Spring reactive framework.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dml-with-mariadb-connector-r2dbc-spring-data.md" %}
[dml-with-mariadb-connector-r2dbc-spring-data.md](dml-with-mariadb-connector-r2dbc-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Spring Data R2DBC DML with MariaDB Connector/R2DBC uses `DatabaseClient` methods execute, select, insert, update, and delete for reactive `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="install-mariadb-connector-r2dbc-spring-data.md" %}
[install-mariadb-connector-r2dbc-spring-data.md](install-mariadb-connector-r2dbc-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MariaDB Connector/R2DBC with Spring Data via Maven using `spring-boot-starter-data-r2dbc`; Spring Boot 3.0 and later manage the `r2dbc-mariadb` connector version automatically.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="r2dbc-code-example-spring-data.md" %}
[r2dbc-code-example-spring-data.md](r2dbc-code-example-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete Java code example using MariaDB Connector/R2DBC with Spring Data R2DBC to query a MariaDB table via `DatabaseClient` and reactive `StepVerifier` result assertions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="repositories-with-mariadb-connector-r2dbc-spring-data.md" %}
[repositories-with-mariadb-connector-r2dbc-spring-data.md](repositories-with-mariadb-connector-r2dbc-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Spring Data repositories with MariaDB Connector/R2DBC use `R2dbcRepository` and JavaConfig to implement reactive CRUD, with ApplicationConfig, Entity, Repository, and Service classes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setup-for-connector-r2dbc-examples-spring-data.md" %}
[setup-for-connector-r2dbc-examples-spring-data.md](setup-for-connector-r2dbc-examples-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up the test database, contact table, and user account required by the MariaDB Connector/R2DBC Spring Data code examples in this documentation section.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-with-mariadb-connector-r2dbc-spring-data.md" %}
[transactions-with-mariadb-connector-r2dbc-spring-data.md](transactions-with-mariadb-connector-r2dbc-spring-data.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Spring Data R2DBC transactions with MariaDB Connector/R2DBC use `R2dbcTransactionManager` and `TransactionalOperator` for framework-managed reactive commit and rollback.
{% endcolumn %}
{% endcolumns %}

## Resources

{% @marketo/form formId="4316" %}
