# About MariaDB Connector/R2DBC

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/97ObD80oLdZu6qT33Vhb/" %}

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/gvM6Yo355bp8HK2Rzyby/" %}

<p align="center"><a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/connectors/r2dbc/all-releases">See all MariaDB Connector/R2DBC releases</a></p>

## Overview

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes the R2DBC API more scalable than Java's standard JDBC API. MariaDB Connector/R2DBC has a native R2DBC implementation and the Spring Data R2DBC framework.

| Connector                    | MariaDB Connector/R2DBC                                                                                           |
| ---------------------------- |-------------------------------------------------------------------------------------------------------------------|
| Supported Versions           | 1.4                                                                                                               |
| Programming Language         | JAVA                                                                                                              |
| Programming Language Version | Java 8+                                                                                                           |
| API                          | [R2DBC 0.9.1](https://r2dbc.io/spec/0.9.1.RELEASE/api/) , [R2DBC 1.0.0](https://r2dbc.io/spec/1.0.0.RELEASE/api/) |
| Supports TLS                 | Yes                                                                                                               |
| Supports Connection Pools    | Yes                                                                                                               |
| License                      | Apache 2.0                                                                                                        |

## End-of-Life (EOL) Versions

The following versions of MariaDB Connector/R2DBC have reached the End of Life and are no longer supported:

* MariaDB Connector/R2DBC 1.0
* MariaDB Connector/R2DBC 1.1

Users are encouraged to upgrade to the next available supported version.

## Maven artifacts

Current connector supporting 1.0.0 R2DBC spec is:

```xml
<dependency>
    <groupId>org.mariadb</groupId>
    <artifactId>r2dbc-mariadb</artifactId>
    <version>1.4.0</version>
</dependency>
```

## Benefits of R2DBC

The R2DBC API relies on reactive data streams, which provide many benefits over standard JDBC:

* Reactive: R2DBC uses an event-driven, non-blocking, and functional programming model.
* Scalable: R2DBC is more scalable than standard JDBC because it allows the runtime to handle concurrency and scheduling.
* Fast: R2DBC streams results, which can improve performance.
* Efficient: R2DBC uses deferred execution and flow control to ensure its operations are performed efficiently.
* Simple: R2DBC is designed to make common usage patterns simple to implement for developers.

## Framework-Specific Documentation

For details on how to use MariaDB Connector/R2DBC, choose a supported framework:

| Parameter                                                                          | Description                                                                                                                |
| ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| [Native R2DBC](using-the-native-r2dbc-api-of-mariadb-connector-r2dbc/)             | The native implementation of R2DBC can be used to connect using MariaDB Connector/R2DBC from within your Java application. |
| [Spring Data R2DBC](using-the-spring-data-framework-with-mariadb-connector-r2dbc/) | Spring Data implementation of R2DBC allows you to connect using MariaDB Connector/R2DBC using the Spring Framework.        |

| Feature                             | [Native R2DBC](using-the-native-r2dbc-api-of-mariadb-connector-r2dbc/) | [Spring Data R2DBC](using-the-spring-data-framework-with-mariadb-connector-r2dbc/) |
| ----------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| Reactive                            | Yes                                                                    | Yes                                                                                |
| Scalable                            | Yes                                                                    | Yes                                                                                |
| Fast                                | Yes                                                                    | Yes                                                                                |
| Efficient                           | Yes                                                                    | Yes                                                                                |
| Executes SQL                        | Yes                                                                    | Yes                                                                                |
| Integrates with Spring Framework    | No                                                                     | Yes                                                                                |
| Spring Data: DatabaseClient         | No                                                                     | Yes                                                                                |
| Spring Data: Repositories           | No                                                                     | Yes                                                                                |
| Spring Data: Object Mapping         | No                                                                     | Yes                                                                                |
| Spring Data: Transaction Management | No                                                                     | Yes                                                                                |

## Resources

* [Release Notes](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/)
* [GitHub](https://github.com/mariadb-corporation/mariadb-connector-r2dbc/)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
