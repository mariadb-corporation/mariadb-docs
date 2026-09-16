---
title: Development
description: >-
  Build applications on MariaDB Server. Connect from Java, Python, Node.js, and more
  with a MariaDB connector, then write the SQL your queries and schema depend
  on.
icon: code
---

# Development

Building an application on MariaDB Server comes down to two things: a connector that links your code to the database, and the SQL that shapes your data. Get the connector working first, then spend your time on the queries.

Because MariaDB Server speaks the MySQL wire protocol, the drivers, ORMs, and query builders you already use work against it without changes. The connectors below are the ones MariaDB maintains and tests directly, and they support the features production applications depend on, including connection pooling, prepared statements, and failover aware connection strings.

**Connect from your language.** Each MariaDB connector has a quickstart that goes from an empty project to a live query. The connector handles the wire protocol, the pooling, and the conversion of result rows into your language's own types, so your code writes statements and reads objects. Java and other JVM languages use Connector/J. Python uses the standard DB-API interface. JavaScript uses the async Node.js driver. Other languages, including C, C++, .NET, ODBC, and R, have their own quickstarts in the connector documentation.

Before wiring up a driver, confirm the database is reachable from the command line. A short `mariadb` client session proves your host, port, user, and password are correct, and rules out a class of problems that otherwise present as driver faults.

**Write the SQL.** With a connection open, the rest is SQL. The basics guide covers creating databases and tables and running your first statements. The advanced SQL guide moves into joins, subqueries, and the query patterns applications rely on as a schema grows. The string functions reference covers the text handling most schemas need.

Pick the connector for your language, get one query returning rows, then build the schema out from there.

## Connect From Your Language

{% content-ref url="explore-by-task/%7Bconnectors%7D/connectors-quickstart-guides/mariadb-connector-j-guide/" %}
[mariadb-connector-j-guide](explore-by-task/%7Bconnectors%7D/connectors-quickstart-guides/mariadb-connector-j-guide/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bconnectors%7D/connectors-quickstart-guides/connector-python-guide/" %}
[connector-python-guide](explore-by-task/%7Bconnectors%7D/connectors-quickstart-guides/connector-python-guide/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bconnectors%7D/connectors-quickstart-guides/connector-node.js-guide" %}
[connector-node.js-guide](explore-by-task/%7Bconnectors%7D/connectors-quickstart-guides/connector-node.js-guide)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/mariadb-connecting-guide/" %}
[mariadb-connecting-guide](explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/mariadb-connecting-guide/)
{% endcontent-ref %}

## Write the SQL

{% content-ref url="explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/basics-guide/" %}
[basics-guide](explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/basics-guide/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/mariadb-advanced-sql-guide/" %}
[mariadb-advanced-sql-guide](explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/mariadb-advanced-sql-guide/)
{% endcontent-ref %}

{% content-ref url="explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/mariadb-string-functions-guide/" %}
[mariadb-string-functions-guide](explore-by-task/%7Bserver%7D/mariadb-quickstart-guides/mariadb-string-functions-guide/)
{% endcontent-ref %}
