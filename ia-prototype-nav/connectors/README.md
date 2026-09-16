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

## Get Started

{% content-ref url="get-started/install-connectors.md" %}
[install-connectors.md](get-started/install-connectors.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-connectors.md" %}
[connect-to-connectors.md](get-started/connect-to-connectors.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/connectors-tutorial.md" %}
[connectors-tutorial.md](tutorials/connectors-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-connectors.md" %}
[configure-connectors.md](how-to-guides/configure-connectors.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-connectors.md" %}
[secure-connectors.md](how-to-guides/secure-connectors.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-connectors.md" %}
[what-is-connectors.md](overview/what-is-connectors.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-connectors-works.md" %}
[how-connectors-works.md](concepts/how-connectors-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/connectors-reference.md" %}
[connectors-reference.md](reference/connectors-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/connectors-releases.md" %}
[connectors-releases.md](release-notes/connectors-releases.md)
{% endcontent-ref %}
