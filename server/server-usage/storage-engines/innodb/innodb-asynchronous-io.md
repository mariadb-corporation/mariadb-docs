---
description: >-
  Explore how InnoDB uses asynchronous I/O on various operating systems to
  handle multiple read and write requests concurrently without blocking.
---

# InnoDB Asynchronous I/O

From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), [InnoDB](./) uses asynchronous I/O to read from and write to disk asynchronously. This forms part of the InnoDB Background Thread Pool.

### Stages

Each asynchronous IO operation goes through multiple stages:

1. SUBMITTED – The IO operation is initiated.

* For asynchronous writes, this typically occurs in the buffer pool flushing code.
* For asynchronous reads, this may happen during buffer pool loading at startup or in prefetching logic.

1. COMPLETED\_IN\_OS – The operating system notifies InnoDB that the I/O operation is complete.

* If using libaio or io\_uring, a dedicated thread handles this notification.
* The completed IO operation is then submitted to InnoDB’s internal thread pool (tpool).

1. EXECUTING\_COMPLETION\_TASK – A tpool thread processes the completion task for the IO operation.
2. COMPLETED – The IO operation is fully handled.

### Resource Constraints and Queuing Mechanisms

#### Waiting for IO Slots

The total number of pending asynchronous IO operations is limited by:

```
total_count = number_of_IO_threads * 256
```

where number\_of\_IO\_threads refers to either [innodb\_io\_read\_threads](innodb-system-variables.md#innodb_read_io_threads) or [innodb\_io\_write\_threads](innodb-system-variables.md#innodb_write_io_threads).

Each IO operation is associated with an IO slot, which contains necessary metadata such as the file handle, operation type, offset, length, and any OS error codes. Initially, all total\_count slots are free, but as pending IO requests accumulate, slots get occupied. If all slots are in use, additional IO requests must wait for a free slot.

#### Queuing Mechanism

The number of completion tasks (EXECUTING\_COMPLETION\_TASK stage) that can run in parallel is also limited by [innodb\_io\_read\_threads](innodb-system-variables.md#innodb_read_io_threads) or [innodb\_io\_write\_threads](innodb-system-variables.md#innodb_write_io_threads). If too many IO operations complete simultaneously, they cannot all be processed in parallel and must be queued, respecting the thread limit.

### Variables

From [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115), a number of status variables were added to give insight into the above operations:

* [innodb\_async\_reads\_pending](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_pending) – Number of read IO operations currently in progress (from SUBMITTED to COMPLETED).
* [innodb\_async\_reads\_tasks\_running](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_tasks_running) – Number of read IO operations currently in the EXECUTING\_COMPLETION\_TASK state.
* [innodb\_async\_reads\_total\_count](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_total_count) – Total number of read completion tasks that have finished execution.
* [innodb\_async\_reads\_queue\_size](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_queue_size) – Current size of the queue (see [Queuing Mechanism](innodb-asynchronous-io.md#queuing-mechanism)).
* [innodb\_async\_reads\_wait\_slot\_sec](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_wait_slot_sec) – Total wait time for a free IO slot (see Waiting for IO Slots).
* [innodb\_async\_reads\_total\_enqueues](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_reads_total_enqueues) – Total number of read operations that were queued (see [Queuing Mechanism](innodb-asynchronous-io.md#queuing-mechanism)). Includes those still waiting and making up `innodb_async_reads_queue_size`.

Similar variables exist for write operations:

* [innodb\_async\_writes\_pending](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_pending)
* [innodb\_async\_writes\_tasks\_running](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_tasks_running)
* [innodb\_async\_reads\_total\_count](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_total_count)
* [innodb\_async\_writes\_queue\_size](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_queue_size)
* [innodb\_async\_writes\_wait\_slot\_sec](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_wait_slot_sec)
* [innodb\_async\_writes\_total\_enqueues](../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_async_writes_total_enqueues)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
