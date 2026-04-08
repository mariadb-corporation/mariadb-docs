---
description: >-
  Learn to maintain MariaDB partitions using ALTER TABLE. Includes syntax for
  optimizing and repairing partitions, plus best practices for managing
  time-series data and performance.
---

# Partition Maintenance

## Maintenance Instructions

You can perform several maintenance tasks on partitioned tables using standard SQL statements or specific `ALTER TABLE` extensions.

### Table-Level Maintenance

For general maintenance, MariaDB supports the following statements on partitioned tables just as it does for non-partitioned tables:

* `CHECK TABLE`
* `OPTIMIZE TABLE`
* `ANALYZE TABLE`
* `REPAIR TABLE`

### Partition-Specific Operations

To target one or more specific partitions rather than the entire table, use the `ALTER TABLE` extensions listed below. In the SQL syntaxes below, _`partition_names`_ is a comma-separated list of partitions, like `p0, p1, p2`.

{% hint style="info" %}
For an operation to be performed on all partitions, you can use the `ALL` keyword instead of specifying all the partitions in a comma-separated list. Example:

{% code overflow="wrap" %}
```sql
ALTER TABLE table_name REBUILD PARTITION ALL
```
{% endcode %}
{% endhint %}

#### Rebuilding Partitions

Use this to defragment a partition. This operation drops all records in the partition and re-inserts them:

{% code expandable="true" %}
```sql
ALTER TABLE table_name REBUILD PARTITION partition_names
```
{% endcode %}

#### Optimizing Partitions

If you have deleted many rows or modified variable-length columns (such as `VARCHAR`, `BLOB`, or `TEXT`), use this statement to reclaim unused space and defragment the data file:

{% code expandable="true" %}
```sql
ALTER TABLE table_name OPTIMIZE PARTITION partition_names
```
{% endcode %}

{% hint style="info" %}
Some storage engines, including `InnoDB`, do not support per-partition optimization. When you run `OPTIMIZE PARTITION` on an `InnoDB` table, MariaDB rebuilds and analyzes the entire table instead.
{% endhint %}

#### Analyzing Partitions

Use this to read and store the key distributions for specific partitions:

{% code expandable="true" %}
```sql
ALTER TABLE table_name ANALYZE PARTITION partition_names
```
{% endcode %}

#### Repairing Partitions

Use this to fix corrupted partitions:

{% code expandable="true" %}
```sql
ALTER TABLE table_name REPAIR PARTITION partition_names
```
{% endcode %}

#### Checking Partitions

You can verify the integrity of data and indexes within a partition:

{% code expandable="true" %}
```sql
ALTER TABLE table_name CHECK PARTITION partition_names
```
{% endcode %}

#### Truncating Partitions

To remove all rows from specific partitions while keeping the table structure, use the `TRUNCATE PARTITION` clause:

{% code expandable="true" %}
```sql
ALTER TABLE table_name TRUNCATE PARTITION partition_names
```
{% endcode %}

#### Reorganizing Partitions

Reorganizing partitions isn't just maintenance, but it can help with making future maintenance easier. Use the following statement to change the structure of existing partitions without losing data. This is particularly useful for splitting a partition that contains a `MAXVALUE` range into a new specific range and a new `MAXVALUE` partition. Use the following syntax:

{% code overflow="wrap" %}
```sql
ALTER TABLE table_name REORGANIZE PARTITION partition_names INTO (PARTITION partition_definition, ...)
```
{% endcode %}

Example: If you have a partition `p_future` defined as `VALUES LESS THAN MAXVALUE`, you can split it to add a specific range for the year 2026:

{% code overflow="wrap" %}
```sql
ALTER TABLE tbl REORGANIZE PARTITION p_future INTO (PARTITION p_2026 VALUES LESS THAN (2027), PARTITION p_future VALUES LESS THAN MAXVALUE)
```
{% endcode %}

## Best Practices and Considerations

When managing partitioned tables, follow these guidelines to ensure optimal performance and maintainability.

### Managing Time-Series Data

Partitioning is most effective for tables containing time-series data where you periodically remove old records.

* Efficient Deletion: Use `DROP PARTITION` instead of `DELETE` to remove expired data. This is a metadata operation and is significantly faster than row-by-row deletion.
* The Future Partition: When using `RANGE` partitioning, define a "future" partition using `VALUES LESS THAN MAXVALUE`. To add a new specific range, use `REORGANIZE PARTITION` to split the "future" partition into a new range and a new `MAXVALUE` partition. See [this section](partition-maintenance.md#reorganizing-partitions) for the syntax.
* The Start Partition: Consider creating a small, empty "start" partition (for example, `VALUES LESS THAN (0)`) to catch `NULL` values or invalid data. Because the partition pruner often scans the first partition by default, keeping it empty improves query efficiency.

### Performance and Scale

* Table Size: Partitioning generally provides noticeable benefits only for tables with more than one million rows.
* Partition Limits: Aim to keep the number of partitions below 50. While MariaDB supports up to 8192 partitions, high partition counts can increase the time required for the server to open the table or perform status checks.
* Index Efficiency: Partitioning is not a substitute for proper indexing. Point queries (finding a single row) are often just as fast with a proper index on a non-partitioned table.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
