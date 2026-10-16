---
title: Development
description: >-
  Build applications on MariaDB Server: connect from your language, write the SQL, and use the features MariaDB adds on top of standard SQL.
icon: code
---

# Development

Most of building on MariaDB is a connector and some SQL. MariaDB Server speaks the MySQL wire protocol, so the drivers, ORMs, and query builders you already know work against it. The MariaDB connectors are the ones we maintain and test ourselves, and each one has a quickstart that gets you from an empty project to a query that returns rows.

If a driver won't connect, try the `mariadb` command-line client with the same host, port, user, and password first. When that works, you know the problem is in the application, not the server.

## Connect From Your Language

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Python</strong></td><td>MariaDB Connector/Python, a DB-API driver with connection pooling.</td><td><a href="{connectors}/connectors-quickstart-guides/connector-python-guide">connector-python-guide</a></td></tr><tr><td><strong>Node.js</strong></td><td>MariaDB Connector/Node.js, with Promise and callback APIs.</td><td><a href="{connectors}/connectors-quickstart-guides/connector-node.js-guide">connector-node.js-guide</a></td></tr><tr><td><strong>Java</strong></td><td>MariaDB Connector/J for JDBC, plus R2DBC for reactive code.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-j-guide">mariadb-connector-j-guide</a></td></tr><tr><td><strong>PHP</strong></td><td>PDO and mysqli, the drivers PHP already ships with.</td><td><a href="{connectors}/other/mariadb-php-connectors-guide">mariadb-php-connectors-guide</a></td></tr><tr><td><strong>C# and .NET</strong></td><td>MariaDB Connector/NET for ADO.NET applications.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-net-guide">mariadb-connector-net-guide</a></td></tr><tr><td><strong>C++</strong></td><td>MariaDB Connector/C++ for native applications.</td><td><a href="{connectors}/connectors-quickstart-guides/mariadb-connector-c++-guide">mariadb-connector-c++-guide</a></td></tr></tbody></table>

## Write the SQL

Start with the basics, then pick up the query patterns that matter once real data shows up.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>SQL Basics</strong></td><td>Create databases and tables, insert rows, and run your first queries.</td><td><a href="{server}/mariadb-quickstart-guides/basics-guide">basics-guide</a></td></tr><tr><td><strong>Essential Queries</strong></td><td>Joins, grouping, ordering, and the everyday patterns applications lean on.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-advanced-sql-guide">mariadb-advanced-sql-guide</a></td></tr><tr><td><strong>Connect From the Command Line</strong></td><td>Use the <code>mariadb</code> client to check a connection and explore a schema.</td><td><a href="{server}/mariadb-quickstart-guides/mariadb-connecting-guide">mariadb-connecting-guide</a></td></tr></tbody></table>

## Use What MariaDB Adds

These features save you from building the same thing in application code.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>JSON</strong></td><td>Keep flexible documents next to relational columns and query both in one statement.</td><td><a href="{server}/reference/sql-functions/special-functions/json-functions">json-functions</a></td></tr><tr><td><strong>Temporal Tables</strong></td><td>Let the server keep every version of a row, then query the table as it was at any point in time.</td><td><a href="{server}/reference/sql-structure/temporal-tables/system-versioned-tables">system-versioned-tables</a></td></tr><tr><td><strong>Common Table Expressions</strong></td><td>Break a hard query into named steps, including recursive queries over trees and graphs.</td><td><a href="{server}/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions">common-table-expressions</a></td></tr></tbody></table>

## Learn From Working Code

Clone one of these and you have a running app to take apart.

<table data-view="cards"><thead><tr><th></th><th></th><th data-hidden data-card-target data-type="content-ref"></th></tr></thead><tbody><tr><td><strong>Sample Apps</strong></td><td>The MariaDB Developers organization on GitHub, with apps in Python, Node.js, Java, .NET, and C++.</td><td><a href="https://github.com/mariadb-developers">mariadb-developers</a></td></tr><tr><td><strong>Modern SQL Samples</strong></td><td>Runnable examples of JSON, temporal tables, and other MariaDB SQL features.</td><td><a href="https://github.com/mariadb-developers/mariadb-modern-sql-samples">mariadb-modern-sql-samples</a></td></tr><tr><td><strong>ORM Samples</strong></td><td>The same app built with the common ORMs, so you can see how each one maps to MariaDB.</td><td><a href="https://github.com/mariadb-developers/mariadb-orm-samples">mariadb-orm-samples</a></td></tr></tbody></table>
