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
{% content-ref url="mariadb-connector-node-js-guide.md" %}
[mariadb-connector-node-js-guide.md](mariadb-connector-node-js-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Node.js is a native JavaScript driver for connecting Node.js applications to MariaDB and MySQL databases, supporting both Promise and Callback APIs via npm.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connector-nodejs-batch-api.md" %}
[connector-nodejs-batch-api.md](connector-nodejs-batch-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The batch API in MariaDB Connector/Node.js sends multiple parameterized queries in one network trip, with server-version-aware optimizations and `max_allowed_packet` handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connector-nodejs-callback-api.md" %}
[connector-nodejs-callback-api.md](connector-nodejs-callback-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MariaDB Connector/Node.js Callback API provides MySQL- and mysql2-compatible callback-style access to MariaDB, with connection, query, batch, and pool methods using familiar patterns.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connector-nodejs-pipelining.md" %}
[connector-nodejs-pipelining.md](connector-nodejs-pipelining.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Node.js pipelining dispatches queries in FIFO order without blocking on each response, improving throughput for high-volume workloads over high-latency connections.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connector-nodejs-promise-api.md" %}
[connector-nodejs-promise-api.md](connector-nodejs-promise-api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Promise API is the default interface for MariaDB Connector/Node.js, enabling async/await patterns for connections, queries, batch operations, and transactions with MariaDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="getting-started-with-the-node-js-connector.md" %}
[getting-started-with-the-node-js-connector.md](getting-started-with-the-node-js-connector.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Getting started with MariaDB Connector/Node.js: installation, connection pooling, query execution, and error handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="node-js-connection-options.md" %}
[node-js-connection-options.md](node-js-connection-options.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Node.js connection options include essential, SSL, and advanced parameters for configuring host, authentication, compression, timeouts, and numeric type handling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="other-nodejs-connectors/README.md" %}
[other-nodejs-connectors](other-nodejs-connectors/README.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Node.js connectors beyond the official MariaDB Connector/Node.js: alternative drivers, ORMs, and other methods to connect Node.js applications to MariaDB.
{% endcolumn %}
{% endcolumns %}
