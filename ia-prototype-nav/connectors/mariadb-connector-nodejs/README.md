---
description: >-
  Explore MariaDB Connector/Node.js, the official client library for Node.js.
  Connect applications to MariaDB/MySQL databases, leverage Promise/Callback
  APIs for efficient data access.
icon: link
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

# Connector/Node.js

MariaDB Connector/Node.js is the official Node.js client library for connecting applications to MariaDB and MySQL databases, offering both Promise and Callback APIs. It is LGPL licensed.

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-nodejs/mariadb-connector-node-js-guide" %}
[mariadb-connector-node-js-guide.md]({connectors}/mariadb-connector-nodejs/mariadb-connector-node-js-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Node.js is a native JavaScript driver for connecting Node.js applications to MariaDB and MySQL databases, supporting both Promise and Callback APIs via npm.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-nodejs/connector-nodejs-batch-api" %}
[connector-nodejs-batch-api.md]({connectors}/mariadb-connector-nodejs/connector-nodejs-batch-api)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The batch API in MariaDB Connector/Node.js sends multiple parameterized queries in one network trip, with server-version-aware optimizations and `max_allowed_packet` handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-nodejs/connector-nodejs-callback-api" %}
[connector-nodejs-callback-api.md]({connectors}/mariadb-connector-nodejs/connector-nodejs-callback-api)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Connector/Node.js Callback API provides MySQL- and mysql2-compatible callback-style access to MariaDB, with connection, query, batch, and pool methods using familiar patterns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-nodejs/connector-nodejs-pipelining" %}
[connector-nodejs-pipelining.md]({connectors}/mariadb-connector-nodejs/connector-nodejs-pipelining)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Node.js pipelining dispatches queries in FIFO order without blocking on each response, improving throughput for high-volume workloads over high-latency connections.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-nodejs/connector-nodejs-promise-api" %}
[connector-nodejs-promise-api.md]({connectors}/mariadb-connector-nodejs/connector-nodejs-promise-api)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Promise API is the default interface for MariaDB Connector/Node.js, enabling async/await patterns for connections, queries, batch operations, and transactions with MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-nodejs/getting-started-with-the-node-js-connector" %}
[getting-started-with-the-node-js-connector.md]({connectors}/mariadb-connector-nodejs/getting-started-with-the-node-js-connector)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Getting started with MariaDB Connector/Node.js: installation, connection pooling, query execution, and error handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-nodejs/node-js-connection-options" %}
[node-js-connection-options.md]({connectors}/mariadb-connector-nodejs/node-js-connection-options)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Node.js connection options include essential, SSL, and advanced parameters for configuring host, authentication, compression, timeouts, and numeric type handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-nodejs/other-nodejs-connectors" %}
[other-nodejs-connectors]({connectors}/mariadb-connector-nodejs/other-nodejs-connectors)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Node.js connectors beyond the official MariaDB Connector/Node.js: alternative drivers, ORMs, and other methods to connect Node.js applications to MariaDB.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
