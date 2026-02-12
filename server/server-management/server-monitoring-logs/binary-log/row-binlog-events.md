---
hidden: true
---

# Row Binlog Events

A `Row_log_event` is a fundamental structure used in [Row-Based Replication (RBR)](binary-log-formats.md#row-based-logging).

When your database is configured to use row-based logging (`binlog_format=ROW`), the binary log doesn't store the actual SQL statements (like `UPDATE users SET status='active'`). Instead, it stores the specific changes made to individual rows. The `Row_log_event` is the container for that data.

## Row\_log\_event

### How it Works

When a transaction occurs, MariaDB records the state of the row before and/or after the change. This ensures that the replica database stays perfectly in sync with the primary, regardless of non-deterministic functions (like `NOW()` or `UUID()`) that might cause issues in statement-based replication.

### The Three Main Subtypes

While _Row\_log\_event_ is the general category, you usually see it manifested as one of these three specific events in binary logs:

1. `Write_rows` event: Triggered by an `INSERT`. It contains the data for the new rows.
2. `Update_rows` event: Triggered by an `UPDATE`. It contains both the "before" image (to find the row on the replica) and the "after" image (the new data).
3. `Delete_rows` event: Triggered by a `DELETE`. It contains the data of the deleted rows so the replica can identify exactly which ones to remove.

### Anatomy of a Row\_log\_event

Each event contains specific metadata to ensure the data lands in the right place:

* **Table ID:** A numeric identifier mapping the event to a specific table.
* **Columns Present Bitmap:** A sequence of bits identifying which columns are actually included in the event (useful for saving space if only one column in a wide table changed).
* **Row Data:** The actual payload, encoded in a binary format.

### Why Does it Matter?

* Consistency: Row-based logging is much more "expensive" in terms of log size than statement-based logging, but it is significantly more reliable for data integrity.
* Point-in-Time Recovery: Tools like `mysqlbinlog` read these events to reconstruct data if a crash occurs.
* Performance: On the primary, it saves the overhead of complex query parsing for the logs, but it can create very large log files if you perform bulk updates (for instance, updating 1 million rows  creates 1 million row events).

### How to View Them

Log events can be seen by inspecting binary log files with `mariadb-binlog -v` (`-v` stands for verbose). Consider having issued these statements:

```sql
MariaDB [test]> INSERT INTO mynation VALUES (1001, 'Wonderland', 3, '2026-12-02', 'AL', 'ALC', 5);
Query OK, 1 row affected (0.004 sec)

MariaDB [test]> UPDATE mynation SET name = 'Aliceland' WHERE name = 'Wonderland';
Query OK, 1 row affected (0.006 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [test]> DELETE FROM mynation WHERE name = 'Aliceland';
Query OK, 1 row affected (0.006 sec)
```

The binary log now contains a `Write_rows`, an `Update_rows`, and a `Delete_rows` entry:

<pre class="language-bash" data-expandable="true"><code class="lang-bash">mariadb-binlog -v 6f6d5cb3-8a83-4f4d-a61a-6f3816cfbf93-bin.000002
…
# at 489
# at 593
#260212 21:36:26 server id 1  end_log_pos 0 CRC32 0xea542edb 	Annotate_rows:
#Q> INSERT INTO mynation VALUES (1001, 'Wonderland', 3, '2026-12-02', 'AL', 'ALC', 5)
#260212 21:36:26 server id 1  end_log_pos 0 CRC32 0x984e0b89 	Table_map: `test`.`mynation` mapped to number 34
# at 658
#260212 21:36:26 server id 1  end_log_pos 0 CRC32 0x9963032c 	<a data-footnote-ref href="#user-content-fn-1">Write_rows</a>: table id 34 flags: STMT_END_F
…
# at 799
# at 886
#260212 21:37:00 server id 1  end_log_pos 0 CRC32 0xee76b32e 	Annotate_rows:
#Q> UPDATE mynation SET name = 'Aliceland' WHERE name = 'Wonderland'
#260212 21:37:00 server id 1  end_log_pos 0 CRC32 0xf6c030e3 	Table_map: `test`.`mynation` mapped to number 34
# at 951
#260212 21:37:00 server id 1  end_log_pos 0 CRC32 0x5a8bc928 	<a data-footnote-ref href="#user-content-fn-2">Update_rows</a>: table id 34 flags: STMT_END_F
…
# at 1127
# at 1195
#260212 21:38:19 server id 1  end_log_pos 0 CRC32 0x5321ba3a 	Annotate_rows:
#Q> DELETE FROM mynation WHERE name = 'Aliceland'
#260212 21:38:19 server id 1  end_log_pos 0 CRC32 0x48c7ef4f 	Table_map: `test`.`mynation` mapped to number 34
# at 1260
#260212 21:38:19 server id 1  end_log_pos 0 CRC32 0xd4ba019d 	<a data-footnote-ref href="#user-content-fn-3">Delete_rows</a>: table id 34 flags: STMT_END_F

</code></pre>

## Partial\_rows\_log\_event

{% hint style="info" %}
This log event is available from MariaDB 12.3.
{% endhint %}

### Overview

The `Partial_rows_log_event` was introduced to solve the issue of oversized binary log events. Previously, a single `Rows_log_event` containing a large number of row changes (or very large `BLOB` data) had to be written and transmitted as a single, contiguous block.

A `Partial_rows_log_event` represents a fragment of a larger logical row change. When a standard `Rows_log_event` exceeds the system-defined threshold, MariaDB splits the payload into a sequence of partial events.

{% hint style="info" %}
The configuration of splitting log events is described [here](binary-log-formats.md#splitting-large-row-format-replication-events).
{% endhint %}

### How Fragmentation Works

Instead of one massive event, the binary log contains a sequence of events structured like this:

1. `Table_map_event`: Identifies the table being modified.
2. `Partial_rows_log_event` (`N` times): Each event is exactly the size of the configured maximum threshold.
3. `Rows_log_event`: The concluding fragment which contains the remaining data and signals the end of the logical group.

### Key Characteristics

* Atomic Reassembly: Replicas and log parsers (like `mariadb-binlog`) must buffer all related `Partial_rows_log_event` entries until the final event in the group is received before the rows can be applied.
* Size Determinism: All partial events in a sequence (except the last one) are of a uniform size, defined by the system variable `binlog_row_event_max_size` (or the equivalent threshold setting).
* Order Preservation: Because the binary log is a sequential stream, these fragments always appear contiguously for a single statement within a transaction.

### Configuration

Splitting log events is enabled by setting the `binlog_row_event_max_size` variable. See [this section](binary-log-formats.md#splitting-large-row-format-replication-events) for details.

### Use Case: Large BLOBs and Bulk Inserts

This feature is particularly beneficial for environments with:

* Limited network buffers: Prevents "packet too large" errors during replication.
* High memory concurrency: Allows the master to stream log data to disk in chunks rather than allocating one massive buffer for a multi-megabyte row change.

### Best Practices & Troubleshooting: `Partial_rows_log_event`

#### Best Practices

* **Align with network MTU:** If you are experiencing "Packet too large" errors or network instability in your replication stream, set [`binlog_row_event_max_size`](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_event_max_size) to a value slightly lower than your network's maximum transmission unit (MTU) or the [`max_allowed_packet`](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) setting.
* **Monitor disk I/O:** While fragmentation prevents massive memory allocations, writing many small `Partial_rows_log_event` entries can increase the number of small I/O operations. If you see an I/O bottleneck on the binary log disk, consider increasing the fragment size slightly.
* **Buffer memory on replicas:** Ensure your replicas have sufficient memory. Because the replica must buffer all `Partial_rows_log_event` fragments before applying the final `Rows_log_event`, very large row changes will still consume memory on the "subscriber" side during the reassembly phase.

#### Troubleshooting & Common Issues

**1. Increased Replication Lag**

If you notice an increase in replication lag after upgrading to MariaDB 12.3, check the frequency of partial events.

* Cause: The replica is spending more time "assembling" the fragments in memory before the SQL thread can execute them.
* Solution: Increase the threshold size to reduce the number of fragments per row change.

**2. `mariadb-binlog` Compatibility**

Older versions of `mariadb-binlog` (pre-12.3) will likely fail to parse these events or skip them entirely because they do not recognize the `Partial_rows_log_event` type code.

* Symptom: "Unknown event type" errors or truncated output when reading logs.
* Solution: Always use the `mariadb-binlog` binary that matches or exceeds the version of the MariaDB server generating the logs.

**3. Monitoring Fragmentation Frequency**

You can monitor how often fragmentation is occurring by checking the binary log headers. If almost every `Rows_log_event` is preceded by a `Partial_rows_log_event`, your threshold is likely set too low for your typical row size (for instance, you have many wide tables or `JSON`/`BLOB` columns).

| **Observation**           | **Likely Cause**    | **Recommended Action**                           |
| ------------------------- | ------------------- | ------------------------------------------------ |
| Frequent small fragments  | Threshold too low   | Increase `binlog_row_event_max_size`             |
| "Packet too large" errors | Threshold too high  | Decrease `binlog_row_event_max_size`             |
| High replica memory usage | Massive row updates | Break up large transactions into smaller batches |

#### Implementation Summary

{% hint style="warning" %}
The introduction of `Partial_rows_log_event` does _not_ change the transactional nature of MariaDB. The fragments are part of a single unit of work; if the connection is lost mid-fragment, the replica discards the partial buffer and waits for a re-transmission or restart of that event group.
{% endhint %}



<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

[^1]: This Row\_log\_event stems from the INSERT statement.

[^2]: This Row\_log\_event stems from the UPDATE statement.

[^3]: This Row\_log\_event stems from the DELETE statement.
