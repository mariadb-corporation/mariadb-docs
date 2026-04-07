# Query Statistics for MariaDB Enterprise ColumnStore

### Description

In MariaDB Enterprise ColumnStore, Query statistics (query stats) offer comprehensive metrics about query execution. These statistics log execution metrics, including memory usage, I/O, cache activity, and processing mode. They can be used to optimize ColumnStore workloads, identify bottlenecks, and evaluate query performance.

> By default, query statistics are disabled. The setup and privileges described on this page are only required when this feature is explicitly enabled.

When query statistics are enabled:

* ColumnStore collects query execution metrics.
* The `infinidb_querystats.querystats` table contains statistics.
* Additional query execution information are available through:
  * `SHOW WARNINGS`&#x20;
  * `calGetStats()` function

> When query statistics are enabled, system performance can be affected. See [Performance Considerations](query-statistics-for-mariadb-enterprise-columnstore.md#performance-considerations).

### Prerequisites

Before enabling query statistics, ensure the following requirements are met:

* MariaDB Enterprise ColumnStore is installed and operational
* Cross-engine join support is configured. The utility user (cross-engine join user) must exist. For setup instructions, see [Configuring ColumnStore Cross-Engine Joins](../../management/managing-columnstore-database-environment/configuring-columnstore-cross-engine-joins.md).

#### Enable Query Statistics

QueryStats is disabled by default. Query statistics are managed by the `mcsSetConfig` utility. <br>

1. In order to enable query statistics, run the following command:

```sql
sudo mcsSetConfig QueryStats Enabled Y
```

2. After enabling, restart the cluster or ColumnStore services to apply the changes:

* Single-node setup: restart ColumnStore services
* For multiple nodes: restart the ColumnStore cluster

#### Grant Required Privileges

QueryStats writes data to a system table using the internal utility user. To enable this, you must grant the `INSERT` privilege to the utility user with the following command:

```sql
GRANT INSERT ON infinidb_querystats.querystats TO 'utility_user'@'localhost';
```

**Note**: Replace `utility_user'@'localhost` with the actual username and host configured for your cross-engine join utility user.

This follows the principle of least privilege by granting access only to the required table.

#### Query Statistics Table

Query statistics are stored in the `infinidb_querystats.querystats` table.

**Example**

```sql
DESCRIBE infinidb_querystats.querystats
```

This table includes past query execution metrics for every session.

#### Retrieve Historical Query Statistics

To view historical query statistics:

```sql
SELECT * FROM infinidb_querystats.querystats;
```

This provides statistics for previously executed queries across sessions.

#### Retrieve Session-Level Statistics

To get statistics for the current session's most recent ColumnStore query, use the following function:

```
SELECT calGetStats();
```

#### View Query Statistics Using SHOW WARNINGS

Each query generates a warning with execution metrics when query statistics are enabled.&#x20;

**Example**

```sql
SELECT COUNT(*) FROM lineitem;
```

**Output**

```
+----------+
| count(*) |
+----------+
|  6001215 |
+----------+
1 row in set, 1 warning (0.039 sec)
```

To view the statistics:

```
SHOW WARNINGS;
```

Example output:

```
Query Stats: MaxMemPct-0; NumTempFiles-0; TempFileSpace-0B; ApproxPhyI/O-0; CacheI/O-1468; BlocksTouched-1468; PartitionBlocksEliminated-0; MsgBytesIn-0B; MsgBytesOut-0B; Mode-Distributed 
```

### Performance Considerations

{% hint style="info" %}
Enabling query statistics logs metrics for every query executed through ColumnStore can degrade performance by 10% or more.
{% endhint %}

ColumnStore logs `calshowstats` metrics for each query it processes when it is enabled. This is intended for debugging sessions, performance analysis, and bulk query evaluation, not for continuous use in production setups.&#x20;

It is recommended to disable query statistics when active analysis is complete or only when needed.

### See Also

* [​ColumnStore Query Tuning](./)
* [​ColumnStore Configuration](../mariadb-columnstore-performance-related-configuration-settings.md)
* ​[Analyzing Queries](../analyzing-queries-in-columnstore.md)
* [Cross-Engine Joins in ColumnStore](../../management/managing-columnstore-database-environment/configuring-columnstore-cross-engine-joins.md)
