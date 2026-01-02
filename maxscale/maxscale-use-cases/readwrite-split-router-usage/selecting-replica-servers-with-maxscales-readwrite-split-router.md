---
description: >-
  Customize load balancing algorithms. Explore options for the
  slave_selection_criteria parameter, including adaptive routing and
  least-global-connections strategies.
---

# Selecting Replica Servers with MaxScale's Read/Write Split Router

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) load balances read-only queries between one or more replica servers. It selects a replica server to execute a query using criteria configured by the `slave_selection_criteria` parameter.

| Criterion                  | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| ADAPTIVE\_ROUTING          | Selects using average response times                         |
| LEAST\_BEHIND\_MASTER      | Selects based on replication lag                             |
| LEAST\_CURRENT\_OPERATIONS | Selects based on number of active operations (the default)   |
| LEAST\_GLOBAL\_CONNECTIONS | Selects based on number of connections from MariaDB MaxScale |
| LEAST\_ROUTER\_CONNECTIONS | Selects based on number of connections from the service      |

## Using Adaptive Routing

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) uses adaptive routing when the `slave_selection_criteria` parameter is set to `ADAPTIVE_ROUTING`.

In this mode, the router measures average server response times. When the router routes queries, it compares the response times of the different replica servers. It favors the faster servers for most queries, while still guaranteeing some traffic on the slowest servers.

## Using Least Behind Primary

The [Read/Write Split Router (readwritesplit)](../../reference/maxscale-routers/maxscale-readwritesplit.md) uses the replica server that is least behind the primary server when the `slave_selection_criteria` parameter is set to `LEAST_BEHIND_MASTER`. This mode is only compatible with [MariaDB replication](../../../server/ha-and-performance/standard-replication/)

In this mode, the router measures replica lag using the `Seconds_Behind_Master` column from [SHOW REPLICA STATUS](../../../server/reference/sql-statements/administrative-sql-statements/show/show-replica-status.md) The replica server that has the lowest value is considered to be the least behind the primary server.

## Setting the Replica Selection Criteria

1. Set the replica selection criteria by configuring the `slave_selection_criteria` parameter for the Read/Write Split Router in `maxscale.cnf`:

```
[split-router]
type                     = service
router                   = readwritesplit
...
slave_selection_criteria = LEAST_GLOBAL_CONNECTIONS
```

2. Restart the MaxScale instance.

```
$ sudo systemctl restart maxscale
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
