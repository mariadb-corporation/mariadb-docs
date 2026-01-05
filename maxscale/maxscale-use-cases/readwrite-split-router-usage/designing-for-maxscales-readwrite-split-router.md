---
description: >-
  Optimize applications for read-write splitting. This guide outlines best
  practices for transaction management and connection handling to ensure
  compatibility with MaxScale.
---

# Designing for MaxScale's Read/Write Split Router

[MaxScale's Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) performs query-based load balancing. For each client connected to MaxScale, it opens up connections to multiple back-end database servers. When the client sends a write query to MaxScale, it routes the query to the connection opened with the primary server. When the client sends a read query to MaxScale, it routes the query to a connection opened with one of the replicas.

This page contains topics that need to be considered when designing applications that use the Read/Write Split Router.

* How does the [Read/Write Split Router route queries?](routing-statements-with-maxscales-readwrite-split-router.md)
* How does the [Read/Write Split Router select replica servers to load balance queries?](selecting-replica-servers-with-maxscales-readwrite-split-router.md)
* How does the [Write Split Router reconnect client connections to the new primary server after automatic failover?](reconnecting-to-the-primary-server-with-maxscales-readwrite-split-router.md)
* How does the [Read/Write Split Router retry failed reads?](retrying-failed-reads-with-maxscales-readwrite-split-router.md)
* How does the [Read/Write Split Router retry failed queries during automatic failover?](delayed-retrying-of-failed-queries-with-maxscales-readwrite-split-router.md)

Additional information is available [here](../../reference/maxscale-routers/maxscale-readwritesplit.md)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
