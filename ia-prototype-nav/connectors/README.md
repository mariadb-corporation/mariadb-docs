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

{% content-ref url="connectors-quickstart-guides/README.md" %}
[Quickstart Guides](connectors-quickstart-guides/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-connector-c/README.md" %}
[Connector/C](mariadb-connector-c/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-connector-cpp/README.md" %}
[Connector/C++](mariadb-connector-cpp/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-connector-j/README.md" %}
[Connector/J](mariadb-connector-j/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-connector-r2dbc/README.md" %}
[Connector/R2DBC](mariadb-connector-r2dbc/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-connector-net/README.md" %}
[.NET Connector](mariadb-connector-net/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-connector-nodejs/README.md" %}
[Connector/Node.js](mariadb-connector-nodejs/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-connector-odbc/README.md" %}
[Connector/ODBC](mariadb-connector-odbc/README.md)
{% endcontent-ref %}

{% content-ref url="mariadb-connector-python/README.md" %}
[Connector/Python](mariadb-connector-python/README.md)
{% endcontent-ref %}

{% content-ref url="other/README.md" %}
[Other Connectors and Methods](other/README.md)
{% endcontent-ref %}
