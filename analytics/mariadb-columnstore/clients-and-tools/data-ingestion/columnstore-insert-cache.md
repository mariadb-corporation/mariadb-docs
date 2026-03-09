# ColumnStore Insert Cache

## Description

The ColumnStore Insert Cache is a performance optimization feature that improves `INSERT` operations in MariaDB ColumnStore, especially for write-heavy workloads. It uses a hidden Aria table that serves as a fast front‑end buffer before data is flushed to ColumnStore's columnar storage.

When this feature is enabled, inserts are first written to a lightweight internal Aria table (the cache table), and later flushed in batches to the [ColumnStore storage engine](../../architecture/columnstore-storage-engine-overview.md). Because Aria is a built-in, memory‑optimized storage engine, inserts into its cache table are considerably faster than inserting directly into ColumnStore. This significantly improves insert performance by reducing the overhead of writing directly to ColumnStore for each row.

A write-heavy workload consists of:

* High volumes of `INSERT` statements
* Occasional `DELETE`, `UPDATE`, or `SELECT` statements

This feature was originally developed for [Hybrid Transactional/Analytical Processing (HTAP)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap) deployments, in which an InnoDB primary replicates to a ColumnStore replica (including single- and multi-node deployments), allowing the ColumnStore replica to maintain with the InnoDB primary's high insert rates.

This insert cache feature is not limited to HTAP environments; it can also be enabled in standalone ColumnStore deployments.&#x20;

By default, the insert cache is disabled. When enabled, the insert cache significantly improves insert throughput.&#x20;

## Purpose

[ColumnStore](../../) is designed for analytical queries and large-scale batch workloads. However, workloads that rely on frequent small inserts may see lower throughput when writing directly to ColumnStore.

The insert cache feature addresses this by:

* Buffering inserts in a lightweight storage engine (Aria)
* Flushing cached data in larger batches
* Reducing write amplification and SQL layer overhead

This makes ColumnStore particularly well-suited for write-heavy workloads, HTAP deployments, replication scenarios where data is moved from InnoDB to ColumnStore, and environments that involve frequent `INSERT` statements or `LOAD DATA INFILE` operations.

## Supported Insert Operations

When this feature is enabled, the performance of the following types of inserts is improved:

*   Single-row INSERT statements<br>

    ```
    INSERT INTO t1 VALUES ();
    ```
*   Multi-row INSERT statements<br>

    ```
    INSERT INTO t1 VALUES (), ();
    ```
* `LOAD DATA INFILE` statements

Other DML operations such as `UPDATE`, `DELETE`, and `INSERT ... SELECT` do not benefit from the insert cache.

## How the Insert Cache Works

When `columnstore_cache_inserts=ON`:

1. A hidden Aria table (cache table) is automatically created internally when a new ColumnStore table is created.
2. This Aria table acts as a front-end for incoming inserts, writing operations rapidly to the cache table using MariaDB’s lightweight storage engine.
3. Cached rows are flushed into the actual ColumnStore table when one of the following event occurs:
   * A non-insert statement is executed (`SELECT`, `UPDATE`, `DELETE`, `INSERT ... SELECT`)
   * The number of cached rows exceeds `columnstore_cache_flush_threshold`
   * A server restart occurs
4. Once flushed, the data becomes visible to all queries.

The flush operation writes accumulated rows to ColumnStore in bulk.

## When to Use the Insert Cache

Ideal use cases for ColumnStore include:

* Write-heavy workloads
* Environments with high-frequency insert operations
* Replication from InnoDB to ColumnStore
* HTAP deployments

## When to Avoid the Insert Cache

Avoid enabling when:

* Strict transactional behavior with rollback support are required
* Workloads are update-heavy rather than insert-heavy
* Flush fragmentation caused by `cpimport` is undesirable
* Insert rates are low and performance gain is negligible

## Configuration

### Enabling the Insert Cache

The insert cache is disabled by default. The following system variable manages the insert cache:

```
columnstore_cache_inserts
```

1. To enable the insert cache, add the following to your MariaDB configuration file:

```
[mariadb]
columnstore_cache_inserts=ON
```

2. After modifying the setting, restart the MariaDB server.
3. Once the server is restarted, verify the setting with:

```
SHOW VARIABLES LIKE 'columnstore_cache_inserts';
```

This setting applies globally to all ColumnStore tables created while it is enabled.

### Flush Threshold

```
columnstore_cache_flush_threshold
```

Defines the number of cached rows that trigger an automatic flush to ColumnStore.

When set to lower values:

* More frequent flushes
* Potentially reduced performance

When set to higher values:

* Fewer flushes
* Larger batch writes

The optimal value depends on workload characteristics.

### Import-Based Flush Mode

```
columnstore_cache_use_import
```

When enabled, cache flushes use `cpimport` instead of the internal batch SQL processing mode.

**Default Behavior (OFF)**

* Flush uses ColumnStore's internal batch processing mode
* Writes go through the SQL layer

**When Enabled (ON)**

* Flush uses `cpimport`
* Bypasses the ColumnStore SQL layer
* Significantly improves flush performance for large batches

**Important Consideration**

When `columnstore_cache_use_import=ON` is enabled, frequent flushes can cause disk fragmentation in database files. This occurs because each `cpimport` operation begins inserting data at a new block boundary, creating fragmentation (“holes”) with every flush.

DBAs should evaluate workload characteristics before enabling this option.

### Configuration Variables

#### `columnstore_cache_inserts`

**Scope:** Global\
**Dynamic:** No (requires restart)\
**Default:** OFF\
**Description**: Enables or disables the insert cache feature globally

#### `columnstore_cache_flush_threshold`

**Scope:** Global / Session\
**Default:** 500000\
**Description**: Maximum number of rows to cache before automatic flush

#### `columnstore_cache_use_import`&#x20;

**Scope:** Global\
**Default:** OFF\
**Description**: Use `cpimport` for cache flush instead of batch processing mode

For comprehensive details on system configuration variables, refer to [ColumnStore System Variables](../../management/columnstore-system-variables.md).

## Performance Characteristics

Internal benchmarking showed significant improvements in insert throughput:

* \~4642x improvement for 50,000 single-row inserts
* \~4763x improvement for 100,000 single-row inserts

These benchmarks were performed before the introduction of `columnstore_cache_use_import`. Enabling import-based flush mode may provide additional improvements depending on workload.

Actual performance gains depend on:

* Insert batch size
* Flush threshold configuration
* Use of replication
* Storage configuration

## Replication and HTAP Use Cases

The insert cache was originally designed for HTAP deployments where:

* An InnoDB master manages transactional workloads
* A ColumnStore replica handles analytical queries
* High insert rates must be maintained on the replica

With this configuration, the insert cache enables the ColumnStore replica to handle replication traffic more efficiently.

The feature is supported for:

* Single-node ColumnStore deployments
* Multi-node ColumnStore clusters

It is not limited to replication scenarios and can be used in standalone ColumnStore environments.

## Operational Considerations

#### Global Scope

The insert cache is a global setting. It is not configurable per table. All ColumnStore tables created while the cache is enabled will use the insert cache.

#### Orphaned Tables

ColumnStore tables created with the insert cache enabled create corresponding hidden Aria cache tables. These tables must be dropped while the insert cache remains enabled. Dropping such tables with `columnstore_cache_inserts=OFF` may leave orphaned hidden Aria tables.

#### Unflushed Records Visibility

Rows that remain unflushed in the insert cache are not visible to queries executed after the cache is disabled; they only become accessible once the cache is re‑enabled and flushed.

#### Transactional Behavior

Because the cache uses Aria at the front-end, which is a non-transactional storage engine:

* `ROLLBACK` is not supported for cached inserts
* The insert cache is not suitable for transactional workloads that require rollback support

## Limitations

The insert cache feature has certain limitations, including:

* No rollback support for cached inserts
* Global-only configuration (not per-table)
* Potential file fragmentation when using import mode
* Non-insert DML operations such as `INSERT..SELECT`, `DELETE`, and `UPDATE` are not accelerated by the cache and will trigger and immediate flush any pending data.

## See Also

* [LOAD DATA INFILE in ColumnStore](../data-import/mariadb-enterprise-columnstore-data-loading-with-load-data-infile.md)
* [System Variables Reference](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables)
* [Aria Storage Engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-storage-engine)
* [ColumnStore System Variables](../../management/columnstore-system-variables.md)

