---
description: >-
  Detailed description of the innodb_flush_method variable, its various
  settings, and effects.
---

# InnoDB Flush Method

{% hint style="info" %}
The `innodb_flush_method` variable has been deprecated from MariaDB 11.0.
{% endhint %}

## Overview

[innodb\_flush\_method](innodb-system-variables.md#innodb_flush_method) is a variable that has been available in MariaDB (and MySQL) for a long time. It defines the method used to flush data to InnoDB data files and log files, which can affect I/O throughput quite a bit.&#x20;

The default setting for this variable initially was `fsync`, but was [changed to `O_DIRECT` in MariaDB 10.6](innodb-flush-method.md#behavior-change-in-mariadb-10.6). The variable has been [deprecated in MariaDB 11.0 and replaced by other settings](innodb-flush-method.md#behavior-change-in-mariadb-11.0).

This page describes the main settings and examines when it makes sense or not to change the default values.

## Options and Startup Parameters

First of all, let’s look at what the different options for `innodb_flush_method` mean, and how they map to the new Boolean options that can be changed while the server is running. There are 2 sets of Boolean options, controlling how the InnoDB write-ahead log `ib_logfile0` as well as the persistent data files are written:

1. `innodb_data_file_write_through`, `innodb_log_file_write_through`: Controls if each write is made durable without an additional system call, such as `fdatasync()` or `fsync()`. This can be useful if there is a battery-backed cache, or if the storage stack can make efficient use of FUA[^1].
2. `innodb_data_file_buffering`, `innodb_log_file_buffering`: Controls if the operating system’s file system cache is used. Those options are disabled by default, to allow efficient writes by DMA[^2] from an aligned memory buffer. Starting with MariaDB Server 10.8, the log block size adapts to the underlying physical block size (typically 512 or 4096 bytes), to avoid an inefficient read-before-write anomaly.

The non-default setting `innodb_flush_method=O_DSYNC` disables buffering and enables write-through on all persistent InnoDB files. On suitable hardware, this can provide the best write performance.

The old default setting `innodb_flush_method=fsync` disables write-through and enables `innodb_data_file_buffering=ON`. The setting of `innodb_log_file_buffering` is not affected. The settings `littlesync` and `nosync`, as well as the Microsoft Windows setting `normal` are treated in the same way.

The MariaDB Server 10.6 default setting `innodb_flush_method=O_DIRECT`  leaves the new Boolean options at their default values. On Microsoft Windows, this option is also known as `unbuffered` and `async_unbuffered`.

The unsafe setting `innodb_flush_method=O_DIRECT_NO_FSYNC` is treated like `O_DIRECT`. You can disable any use of `fdatasync()` or `fsync()` system calls, but that means you lose all crash-safety guarantees. To do that, set `debug_no_sync=ON`. Starting with MariaDB Server 11.0, this unsafe parameter  affects InnoDB as well.

## Behavior Change in MariaDB 10.6

Let’s now look at why the default behavior was changed in 10.6. Looking at how most modern file systems handle writes, it seems clear that the penalty of writing twice (to the file system cache and then to the disk) is not needed, and  typically slows down the system. With `O_DIRECT`, there is no such double writing, as everything goes straight to disk.

However, there are still cases where reads are affected negatively by using `O_DIRECT`. Note that this only affects I/O-bound workloads. Ideally, a requested data page is cached in an internal MariaDB buffer (in this case the, [InnoDB buffer pool](innodb-buffer-pool.md)), and the data can be accessed without involving the operating system, no matter how the data is written to disk.

There is a possibility that a data page is written from the buffer pool to the file system, evicted from the buffer pool, and again read from the file system. In this kind of scenario, the operating system could provide an additional layer of cache between the buffer pool and the storage, allowing the “read” to be a simple matter of copying the data from the kernel buffer to the buffer pool. The worst-case scenario is that the page needs to be read from actual storage, which can be orders of magnitude slower than copying from the file system cache.

If `innodb_buffer_pool_size` is very small compared to the available memory, the file system cache may effectively become the main cache. This can be useful when a MariaDB Server instance is small, or used sporadically on a system that runs many other services. In such an environment, it can make sense to use `innodb_flush_method=fsync`, and to let the operating system tune the use of buffers according to the variable workload. From its early days decades ago, the Linux kernel tries to use all “free” memory for the file system cache.

Another thing to consider is read-ahead, or loading data into a cache in the anticipation of it being needed soon. While read-ahead mechanisms into the InnoDB buffer pool exist, the read-ahead into the Linux file system cache may perform much better. Part of the problem can be that MariaDB always reads InnoDB pages one at a time, giving an advantage to the operating system’s file system cache.

To summarize: Changing the default of `innodb_flush_method` to `O_DIRECT` in MariaDB 10.6 was the right choice — however, there are cases illustrated above where you might want to change this behavior back to the original one.&#x20;

## Behavior Change in MariaDB 11.0

From MariaDB 11.0, the flushing behavior of InnoDB is no longer controlled by `innodb_flush_method`, but rather by the  following parameters, which can be modified with a `SET GLOBAL` statement while the server is running:

1. `innodb_log_file_buffering`: This is best left to its default value (`OFF`), except when backing up a write-heavy server.
2. `innodb_data_file_buffering`: The default is `OFF`; set it to `ON` if you encounter read performance problems.
3. `innodb_log_file_write_through`, `innodb_data_file_write_through`: The default is `OFF` for both parameters; setting them to `ON` can improve or degrade write performance, depending on the hardware used.<br>

[^1]: Force Unit Access (FUA) is a feature in storage systems that ensures data is written directly to stable, non-volatile storage before a write command is acknowledged as complete.\
    It is implemented as a flag in I/O commands, such as SCSI and SATA commands, and is used to bypass the device's write cache, guaranteeing that data is physically written to the storage medium.\
    When the FUA bit is set to 1, the storage device must complete the write operation to the physical media before returning a "good" status, ensuring data durability even in the event of a power failure.

[^2]: Direct Memory Access; see [https://en.wikipedia.org/wiki/Direct\_memory\_access](https://en.wikipedia.org/wiki/Direct_memory_access) for details.
