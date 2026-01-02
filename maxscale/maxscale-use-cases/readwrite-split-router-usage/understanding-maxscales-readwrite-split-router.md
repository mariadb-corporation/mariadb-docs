---
description: >-
  Get an overview of the readwritesplit router. Learn how it splits traffic for
  MariaDB replication and Galera clusters to enhance scalability and
  performance.
---

# Understanding MaxScale's Read/Write Split Router

MaxScale's [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) performs query-based load balancing. For each client connected to MaxScale, it opens up connections to multiple back-end database servers. When the client sends a write query to MaxScale, it routes the query to the connection opened with the primary server. When the client sends a read query to MaxScale, it routes the query to a connection opened with one of the replicas.

## What Does the Read/Write Split Router Support?

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) supports:

* [MariaDB replication](../../../server/architecture/topologies/primary-replica/) deployments.
* [Galera Cluster](../../../server/architecture/topologies/galera-cluster/) deployments.
* [Columnstore Object Storage](../../../server/architecture/topologies/columnstore-object-storage/) and [ColumnStore Shared Local Storage](../../../server/architecture/topologies/columnstore-shared-local-storage/) deployments.

## When to Use the Read/Write Split Router?

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) allows you to:

* Perform query-based load balancing.
* Route client connections to multiple servers simultaneously.
* Route write queries to primary and read queries to replicas.
* Automatically reconnect clients to the new primary after failover or switchover.
* Automatically replay transactions on the new primary after failover or switchover.
* Automatically retry failed queries.
* Enforce causal reads to avoid reading stale data caused by slave lag.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
