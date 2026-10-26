---
description: >-
  How to estimate the disk space a GridGain 9 cluster needs for table data,
  secondary indexes, system data, and the RAFT log, with a worked example.
---

# Capacity Planning

Use this guide to estimate how much disk space your GridGain 9 cluster will need before you deploy it. Estimates in the guide are provided for the entire cluster. To get the size of an individual node, divide the cluster total across your nodes according to how partitions are distributed. Adding nodes spreads the same data over more machines rather than changing the total.

## How GridGain Stores Data on Disk

GridGain stores a variety of information on disk. For this guide, the following will be important:

- **Table data** is stored in partition files. The persistent engine keeps each partition in its own file and reuses free space within pages, so the on-disk size of a row is larger than the raw value it holds.
- **Secondary indexes** are stored inside the same partition file as the table data. There is no separate index file, and each index adds a per-row cost that depends on the indexed column type.
- **RAFT log** is a separate write-ahead log that replicates changes across replicas. It grows with your write rate and is reclaimed over time.
- **System data** covers small internal stores, for example those required for the Cluster Management Group and Metastorage. These are small compared to table data.

For more information about the persistent engine, see [Native Persistent Storage](engines/native-persistent-storage.md).

## Estimating Row Size

### Serialized Row Size

GridGain serializes each row as a binary tuple. You can approximate the serialized size the following way:

```
tuple size ≈ W * N + R + 5
```

Where:

- `N` is the number of columns in the row.
- `R` is the total size, in bytes, of the raw column values.
- `W` is the width of each column offset entry. Size depends on `R`: `1` byte if `R` is less than 256 bytes, `2` bytes if `R` is less than 65,536 bytes, and `4` bytes otherwise.
- `5` is the fixed per-tuple overhead (tuple header and framing).

The result of this calculation is approximate. The real size can be slightly larger because of type-specific framing, or slightly smaller because some values are compressed. Make sure you can account for possible difference.

### On-Disk Row Overhead

Storing a row costs more than its serialized size. Each row adds about 200 bytes of overhead in the partition file. The exact number varies depending on your configuration.

```
stored row ≈ tuple size + 200 bytes
```

## Accounting for Indexes

Each secondary index adds a per-row cost on top of the stored row. The cost depends heavily on the indexed column type and value size, so an exact formula is impractical. Use the following measured reference values as a starting point:

| Index type | Indexed column | Overhead per row |
| --- | --- | --- |
| Hash | `BIGINT` | \~55 bytes |
| Sorted | `BIGINT` | \~45 bytes |
| Sorted | `VARCHAR(32)`, inlined | \~85 bytes |
| Hash | `VARCHAR(32)`, inlined | \~85–90 bytes |
| Sorted | `VARCHAR(128)`, not inlined | \~275 bytes |

Keep the following rules of thumb in mind:

- **Fixed-length columns** add roughly 40–50 bytes on top of the column payload itself.
- **Variable-length columns** that fit inline add roughly 50 bytes on top of the payload. Inside an index, the payload of a `VARCHAR` or `VARBINARY` column is capped at 64 bytes of pre-allocated space, and a `DECIMAL` value is stored in 6 bytes.
- **Variable-length columns** that do not fit inline cost significantly more, because the full value is stored in addition to the pre-allocated inline space.

If you would rather not estimate each index separately, apply a simple heuristic: take your table-data estimate and add 30–50 percent to cover indexes.

## Reserving Space for System Data

Internal system stores are small. Cluster Management Group and Metastorage together use about 10 MB, and transaction state storage requires roughly the same amount. The Metastorage is expected to grow with the number of distribution zones, but remains modest.

Reserve about **5 GB** for system data. This will cover the majority of deployments.

## Sizing the RAFT Log

The RAFT log is hard to estimate precisely because its storage compresses log entries. As an upper bound, the log size is limited in the following way:

```
raft log size ≈ number of rows * (tuple size + 50 bytes)
```

In practice the log typically is smaller for larger data amounts. Rather than sizing the log to your total data, size it to absorb your write load: provision enough space for the RAFT log to hold at least two hours of writes at your expected rate.

You can limit RAFT log disk usage with the node configuration properties described under the disk usage limits section of [Node Configuration Parameters](../../reference/configuration/node-configuration-parameters.md#hard-disk-usage-limits).

## Example Estimate

Consider a table with the following schema:

- `id BIGINT` (primary key)
- `i0` to `i7`: eight `BIGINT` columns
- `s0` to `s3`: four `VARCHAR(32)` columns
- `shortkey VARCHAR(32)`
- `longkey VARCHAR(128)`

In this example, we assume that the string columns are filled to their full length, and a hash index exists on the `id` column.

Estimate the stored row size step by step:

1. **Raw value size (`R`).** Sum the column sizes: `8 + (8 * 8) + (4 * 32) + 32 + 128 = 360` bytes.
2. **Serialized tuple size.** There are 15 columns (`N = 15`). `R` is 360 bytes, so the offset width is `W = 2`. The tuple size is `(2 * 15) + 360 + 5 = 395` bytes.
3. **On-disk row.** Add the 200-byte row overhead: `395 + 200 = 595` bytes.
4. **Index.** The hash index on the `BIGINT` primary key adds about 55 bytes: `595 + 55 = 650` bytes per row.

As a result, you can make estimates for your requirements, depending on the number of rows. For example, storing 10 million rows would require roughly 10.17 GB.

{% hint style="info" %}
Always add at least 10 percent on top of your estimate as a safety margin.
{% endhint %}
