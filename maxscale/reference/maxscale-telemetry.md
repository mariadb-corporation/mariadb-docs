---
description: >-
  Reference list of the metrics MariaDB MaxScale exports over OpenTelemetry.
---

# MaxScale Telemetry

## Overview

MaxScale exports metrics and logs via OpenTelemetry. To enable it, add
`telemetry=true` under the `[maxscale]` section. To configure where metrics are
sent, use `telemetry_url`. For more information, refer to the
[telemetry settings](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry)
in the MaxScale configuration guide.

## Metrics

### Server Metrics

* `maxscale.server.operations`
  * Type: Gauge
  * Description: Number of active query operations
  * Added in: MaxScale 25.10

* `maxscale.server.connections`
  * Type: Gauge
  * Description: Number of open connections
  * Added in: MaxScale 25.10

* `maxscale.server.response_dur`
  * Type: Histogram
  * Description: Response duration in seconds
  * Added in: MaxScale 25.10

* `maxscale.server.read_packets`
  * Type: Gauge (running total)
  * Description: Number of routed reads
  * Added in: MaxScale 25.10

* `maxscale.server.write_packets`
  * Type: Gauge (running total)
  * Description: Number of routed writes
  * Added in: MaxScale 25.10

* `maxscale.server.status`
  * Type: Gauge
  * Description: Server status: `0` = Read, `1` = Write, `2` = Up, `3` = Down
  * Added in: MaxScale 25.10

* `maxscale.server.errors`
  * Type: Gauge (running total)
  * Description: Number of error responses
  * Added in: MaxScale 26.10

* `maxscale.server.transactions`
  * Type: Gauge (running total)
  * Description: Number of completed transactions
  * Added in: MaxScale 26.10

* `maxscale.server.pool_size`
  * Type: Gauge
  * Description: Connection pool size
  * Added in: MaxScale 26.10

* `maxscale.server.pool_found`
  * Type: Gauge (running total)
  * Description: Times connection was found in the pool
  * Added in: MaxScale 26.10

* `maxscale.server.pool_empty`
  * Type: Gauge (running total)
  * Description: Times connection pool was empty
  * Added in: MaxScale 26.10

* `maxscale.server.replication_lag`
  * Type: Gauge
  * Description: Replication lag in seconds
  * Added in: MaxScale 26.10

* `maxscale.server.transaction_lag`
  * Type: Gauge
  * Description: Number of transactions the server is behind
  * Added in: MaxScale 26.10

### Service Metrics

* `maxscale.service.operations`
  * Type: Gauge
  * Description: Number of active query operations
  * Added in: MaxScale 26.10

* `maxscale.service.connections`
  * Type: Gauge
  * Description: Number of open connections
  * Added in: MaxScale 26.10

* `maxscale.service.read_packets`
  * Type: Gauge (running total)
  * Description: Number of routed reads
  * Added in: MaxScale 26.10

* `maxscale.service.write_packets`
  * Type: Gauge (running total)
  * Description: Number of routed writes
  * Added in: MaxScale 26.10

* `maxscale.service.errors`
  * Type: Gauge (running total)
  * Description: Number of error responses
  * Added in: MaxScale 26.10

* `maxscale.service.transactions`
  * Type: Gauge (running total)
  * Description: Number of completed transactions
  * Added in: MaxScale 26.10

### Query Classifier Cache Metrics

* `maxscale.query_cache.size`
  * Type: Gauge
  * Description: Query cache size in bytes
  * Added in: MaxScale 25.10

* `maxscale.query_cache.hits`
  * Type: Gauge (running total)
  * Description: Query cache hits
  * Added in: MaxScale 25.10

* `maxscale.query_cache.misses`
  * Type: Gauge (running total)
  * Description: Query cache misses
  * Added in: MaxScale 25.10

### Query Metrics

* `maxscale.query.latency`
  * Type: Gauge
  * Description: Query latency per SQL statement, broken down by the 50th, 75th, 95th and 99th percentile.
    Each data point has a `percentile` attribute (`p50`, `p75`, `p95` or `p99`) and an `sql`
    attribute holding the canonical form of the statement. Only the most frequently executed
    statements are exported, up to
    [`telemetry_sql_count`](../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#telemetry_sql_count)
    (default 50); use `telemetry_sql_match` and `telemetry_sql_exclude` to filter them.
  * Added in: MaxScale 26.10

### General Metrics

* `maxscale.qps`
  * Type: Gauge
  * Description: Queries per second
  * Added in: MaxScale 25.10

* `maxscale.uptime`
  * Type: Gauge
  * Description: MaxScale uptime in seconds
  * Added in: MaxScale 25.10

* `maxscale.version`
  * Type: Gauge
  * Description: MaxScale version
  * Added in: MaxScale 25.10

* `maxscale.process.time`
  * Type: Gauge
  * Description: MaxScale CPU usage
  * Added in: MaxScale 25.10
