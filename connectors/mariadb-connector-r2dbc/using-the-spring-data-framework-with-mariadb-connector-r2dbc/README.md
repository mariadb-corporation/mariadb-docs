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

## Resources

{% @marketo/form formId="4316" %}
