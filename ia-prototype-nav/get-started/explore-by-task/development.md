---
title: Development
description: >-
  Build applications on MariaDB. Connect from your language with a MariaDB
  connector, then learn the SQL that your queries and schema depend on.
icon: code
---

# Development

Developing against MariaDB has two halves. One is the connection: getting your application language to open a session, run statements, and read results through a MariaDB connector. The other is the SQL: the statements, joins, and functions your queries and schema are built from. This page brings both together, because a working application needs the driver and the language of the database, and the two live in different parts of the documentation.

MariaDB maintains connectors for the common application languages, and each one has a quickstart that takes you from an empty project to a query against the database. The connector handles the wire protocol, connection pooling, and the mapping between result rows and your language's data types, so your code works in terms of statements and rows rather than bytes on a socket. Pick the guide for your stack. The Connector/J guide covers Java and the JVM languages, the Python guide covers the standard database interface for Python, and the Node.js guide covers the asynchronous driver most JavaScript applications use. If your language is not among these three, the connector documentation has a quickstart for each of the others as well.

Before you wire up a driver, it is often worth connecting from the command line to confirm the database is reachable and your credentials work. The Server connection guide covers the `mariadb` client and the connection parameters, the host, the port, the user, and the database, that your driver will need in its configuration. Getting a successful command line session first rules out a whole class of problems that otherwise look like driver bugs.

With a connection open, most development is SQL. The basics guide covers creating tables and running single statements, which is enough to back a first feature. The advanced SQL guide moves into joins, subqueries, and the query patterns that real applications rely on, and it is the guide you return to as your schema grows past a few tables. The string functions guide is a worked reference for the text handling that most schemas need, from formatting output to searching within columns. Together these three cover the SQL that an application developer writes day to day, and they link on into the full reference when you need a specific statement.

## Connect from your language

{% content-ref url="{connectors}/connectors-quickstart-guides/mariadb-connector-j-guide" %}
[Connector/J for Java]({connectors}/connectors-quickstart-guides/mariadb-connector-j-guide)
{% endcontent-ref %}

{% content-ref url="{connectors}/connectors-quickstart-guides/connector-python-guide" %}
[Connector/Python]({connectors}/connectors-quickstart-guides/connector-python-guide)
{% endcontent-ref %}

{% content-ref url="{connectors}/connectors-quickstart-guides/connector-node.js-guide" %}
[Connector/Node.js]({connectors}/connectors-quickstart-guides/connector-node.js-guide)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-connecting-guide" %}
[Connect to MariaDB Server]({server}/mariadb-quickstart-guides/mariadb-connecting-guide)
{% endcontent-ref %}

## Write the SQL

{% content-ref url="{server}/mariadb-quickstart-guides/basics-guide" %}
[MariaDB Basics]({server}/mariadb-quickstart-guides/basics-guide)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide" %}
[Advanced SQL]({server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide)
{% endcontent-ref %}

{% content-ref url="{server}/mariadb-quickstart-guides/mariadb-string-functions-guide" %}
[String Functions]({server}/mariadb-quickstart-guides/mariadb-string-functions-guide)
{% endcontent-ref %}
