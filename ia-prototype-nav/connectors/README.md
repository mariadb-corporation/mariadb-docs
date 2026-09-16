---
title: Connectors
description: >-
  MariaDB Connectors are the client libraries that link your application to
  MariaDB Server, for Java, Python, Node.js, C, C++, .NET, ODBC, and R.
icon: plug
---

# Connectors

MariaDB Connectors are the client libraries that link your application to a MariaDB Server database. A connector implements the wire protocol, manages connections, and converts result rows into your language's own types, so your code writes statements and reads objects.

These are the connectors MariaDB maintains and tests directly, covering Java and the JVM, Python, Node.js, C, C++, .NET, ODBC, and R. Because MariaDB Server speaks the MySQL wire protocol, MySQL drivers also connect to it, and for existing applications that is often the reason a migration needs no code change. The MariaDB connectors are the ones that support MariaDB specific behavior and are tested against MariaDB Server releases.

Two capabilities matter more than the rest in production. Connection pooling reuses established connections instead of paying setup cost per query, which is usually the largest available performance win in application database code. Prepared statements separate a statement from its parameters, which removes a class of SQL injection and lets the server reuse a query plan.

**Install and connect.** Each connector has a quickstart that goes from an empty project to a live query. Install the library with your language's package manager, build a connection string from the host, port, user, password, and database, and run a statement.

**Configure them for production.** The guides cover pooling, timeouts, TLS, and the connection string options that determine how a client behaves when a server is slow or gone, which is what decides whether a failover looks like a pause or an error to your users.

**Look up the API.** The reference documents each connector's classes, methods, and options.

Pick the connector for your language, get one query returning rows, then configure pooling and TLS before you go to production.

{% content-ref url="{connectors}/connectors-quickstart-guides" %}
[Quickstart Guides]({connectors}/connectors-quickstart-guides)
{% endcontent-ref %}

{% content-ref url="{connectors}/mariadb-connector-c" %}
[Connector/C]({connectors}/mariadb-connector-c)
{% endcontent-ref %}

{% content-ref url="{connectors}/mariadb-connector-cpp" %}
[Connector/C++]({connectors}/mariadb-connector-cpp)
{% endcontent-ref %}

{% content-ref url="{connectors}/mariadb-connector-j" %}
[Connector/J]({connectors}/mariadb-connector-j)
{% endcontent-ref %}

{% content-ref url="{connectors}/mariadb-connector-r2dbc" %}
[Connector/R2DBC]({connectors}/mariadb-connector-r2dbc)
{% endcontent-ref %}

{% content-ref url="{connectors}/mariadb-connector-net" %}
[.NET Connector]({connectors}/mariadb-connector-net)
{% endcontent-ref %}

{% content-ref url="{connectors}/mariadb-connector-nodejs" %}
[Connector/Node.js]({connectors}/mariadb-connector-nodejs)
{% endcontent-ref %}

{% content-ref url="{connectors}/mariadb-connector-odbc" %}
[Connector/ODBC]({connectors}/mariadb-connector-odbc)
{% endcontent-ref %}

{% content-ref url="{connectors}/mariadb-connector-python" %}
[Connector/Python]({connectors}/mariadb-connector-python)
{% endcontent-ref %}

{% content-ref url="{connectors}/other" %}
[Other Connectors and Methods]({connectors}/other)
{% endcontent-ref %}
