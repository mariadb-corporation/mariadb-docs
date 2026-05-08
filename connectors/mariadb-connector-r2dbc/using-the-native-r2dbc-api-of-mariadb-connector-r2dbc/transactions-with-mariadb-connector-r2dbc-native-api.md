---
description: >-
  The MariaDB Connector/R2DBC native API requires manual subscription for
  beginTransaction, commitTransaction, and rollbackTransaction; Spring Data
  R2DBC provides managed transactions.
---

# Transactions with MariaDB Connector/R2DBC (Native API)

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes R2DBC more scalable than Java's standard JDBC API.

## Transactions

By default, MariaDB Connector/R2DBC enables the auto-committing of transactions on all connections. When you issue a statement that modifies the table through the Connector, it automatically commits the transaction, making the change permanent on the database.

The native implementation of MariaDB Connector/R2DBC does not provide out-of-the-box support for reactive streams transactions unless user-managed transactions are subscribed to using Mono.from(Connection.beginTransaction()).block(), Mono.from(Connection.commitTransaction()).block(), and Mono.from(Connection.rollbackTransaction()).block() method calls.

To use Spring framework-managed reactive streams transactions from your Java code, use [MariaDB Connector/R2DBC with Spring Data R2DBC](../using-the-spring-data-framework-with-mariadb-connector-r2dbc/transactions-with-mariadb-connector-r2dbc-spring-data.md).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
