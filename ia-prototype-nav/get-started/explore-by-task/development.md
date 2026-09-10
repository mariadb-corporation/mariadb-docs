---
title: Development
description: >-
  Build applications on MariaDB. Connect from Java, Python, Node.js, and more
  with a MariaDB connector, then write the SQL your queries and schema depend
  on.
icon: code
---

# Development

Build your application on MariaDB and you get a fast, standard SQL database that your language already knows how to talk to. Two things get you productive: a connector that links your code to the database, and the SQL that shapes your data. Start with the driver, then spend your time on the queries.

Because MariaDB is compatible with MySQL, the drivers, ORMs, and query builders you already use work against it without changes, so you rarely start from scratch. The connectors below are the ones MariaDB maintains and tests directly, and they support the features, like connection pooling and prepared statements, that production applications lean on.

**Connect from your language.** MariaDB ships connectors for the languages you build in, and each has a quickstart that goes from an empty project to a live query. The connector does the heavy lifting: the wire protocol, connection pooling, and turning result rows into your language's own types, so you write statements and read objects. Grab the guide for your stack. Java and the JVM use Connector/J, Python uses the standard database interface, and JavaScript uses the async Node.js driver. Building in something else? The connector documentation has a quickstart for that too.

Before you wire up a driver, it is worth proving the database is reachable from the command line. A quick `mariadb` session confirms your host, port, user, and password work, and rules out a whole class of problems that otherwise look like driver bugs.

**Write the SQL.** With a connection open, the rest is SQL, and this is where your application takes shape. The basics guide gets you creating tables and running statements. The advanced SQL guide moves into joins, subqueries, and the query patterns real applications rely on, and it is the one you come back to as your schema grows. The string functions guide is a handy reference for the text handling nearly every schema needs.

Pick your connector, get a query running, then build out your schema from there.

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
