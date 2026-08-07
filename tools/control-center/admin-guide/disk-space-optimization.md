---
description: >-
  Optimizing GridGain Control Center disk space usage by limiting saved data,
  throttling collection, and cleaning up oversized tables.
---

# Disk Space Optimization

To prevent running out of disk space, you can optimize disk space utilization. I.e., you can accumulate less data, or keep the data for a shorter period, without missing what is important for your cluster operation. Data collection and accumulation parameters should be defined in the optimal way at the beginning - right after the [Control Center installation](../installation/README.md).

If you do run out of disk space in the course of Control Center operation, this might mean that your data collection and accumulation parameters need further optimization. Proceed as follows.

## Limit Saved Data

Combine the following approaches:

- [Reduce the data retention period](configuration.md#time-to-live-limits).

  {% hint style="info" %}
  When you reduce TTL, the new value applies only to the new data. The data that had been collected with the previous TTL setting will be retained for the period this previous value defined. Therefore, the disk size utilization will decrease gradually rather than immediately.
  {% endhint %}
- [Limit table size](configuration.md#table-size-limits).

## Throttle Down Data Collection

Throttle down data collection for:

- [Traces](../gg8/tracing/tracing.md#configuring-tracing)
- [Queries](../gg8/queries/querying.md#selecting-queries-to-track)
- [Metrics](configuration.md#common-properties) - see `control.metric-collector.pull-interval`

## Clean Up Space (Optional)

If you need to not only prevent disk clogging in the future but free up space that is already occupied, proceed as follows:

### Identify Oversized Tables

Identify the tables that occupy the most space on your disk:

{% hint style="info" %}
The number of records in a table does not precisely correlate to the volume that table occupies on your disk. This correlation depends on a cluster's specifics, such as the queries and tasks being executed.
{% endhint %}

1. Check the sizes of the relevant tables on the disk - QuerySession, Trace, Span, and TaskSession - in `work/db/ggcc_db`. Because of defragmentation, the table might appear significantly larger than in reality. For defragmented tables, check the actuator metrics for real sizes.
2. Get the number of records in the same tables by from [Spring actuator metrics](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.metrics.endpoint) at the following URLs:
   - `<control-center-url>/actuator/metrics/repository.table.Span.size`
   - `<control-center-url>/actuator/metrics/repository.table.Trace.size`
   - `<control-center-url>/actuator/metrics/repository.table.QuerySession.size`
   - `<control-center-url>/actuator/metrics/repository.table.TaskSession.size`

If the relevant tables in your environment are not yet of representative size, you can use our estimates for a 3-node cluster with an average load:

- [Query](../gg8/queries/querying.md#running-queries): 1 GB - approximately 200,000 records
- [Task](../gg8/compute/compute-grid.md): 1 GB - approximately 250,000 records
- [Trace](../gg8/tracing/tracing.md#configuring-tracing): 1 GB - approximately 800,000 records
- [Span](../gg8/tracing/tracing.md#viewing-spans): 1 GB - approximately 500,000 records

### Delete Oversized Tables

For optimization settings to take effect, you need to clean up the oversized tables. Because of defragmentation, each table occupies the maximum disk space it had achieved in its lifecycle. The occupied size will remain the same, even if the table becomes "empty," unless you physically delete the defragmented table from the disc.

To clean up the tables:

1. Stop Control Center.
2. Delete the oversized table (cache) folder. For example, delete `work/db/ggcc_db/cache-QuerySessionCache` to clean up the space occupied by the running query data.
3. Start Control Center.
