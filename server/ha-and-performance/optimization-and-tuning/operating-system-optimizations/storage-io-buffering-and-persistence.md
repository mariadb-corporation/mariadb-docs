---
description: >-
  Defines the OS-agnostic terms MariaDB documentation uses for disk I/O —
  unbuffered I/O, write-through, persist — and shows how each one maps to
  Linux and Windows mechanisms.
---

# Storage I/O: Buffering and Persistence

This page defines the I/O behavior terms that other MariaDB documentation pages use — *unbuffered I/O*, *write-through*, *persist to non-volatile storage* — and shows how each one maps to the underlying mechanism on Linux and Windows. Other pages refer here for the OS-level details rather than embedding Linux-specific flag names inline.

## Why This Matters

The MariaDB server, and especially the [InnoDB](../../../server-usage/storage-engines/innodb/) storage engine, needs precise control over when writes actually reach non-volatile storage. The operating system normally buffers writes in memory (the *page cache*) and flushes them to disk on its own schedule. That is fast, but unsafe for a transactional database: a power loss between the application write and the OS flush would lose committed data.

MariaDB therefore exposes configuration that lets administrators choose between OS-buffered performance and database-controlled durability. The configuration uses general I/O terms — buffering, write-through, persistence — that describe the behavior independent of the operating system. This page is the reference for what those terms mean and how each OS implements them.

## Unbuffered I/O

**Behavior**: Reads and writes bypass the operating system's page cache. Each read fetches directly from the storage device; each write is handed to the device without keeping a copy in OS memory.

**Trade-off**: Avoids "double buffering" — that is, caching the same data both in MariaDB's own buffer pool and in the OS page cache, which costs memory and CPU. The trade-off is the loss of the OS's read-ahead and write-coalescing optimizations. Unbuffered I/O is most appropriate when MariaDB itself manages most of the memory available for caching data (for example, when the InnoDB buffer pool is sized to most of system RAM).

| Operating system | Underlying mechanism |
|------------------|----------------------|
| Linux            | File opened with `O_DIRECT` |
| Windows          | File opened with `FILE_FLAG_NO_BUFFERING` |

## Write-Through

**Behavior**: Every individual write call returns only after the storage layer has accepted the data for non-volatile storage. Equivalent to issuing a write followed by an immediate persist, on every single write.

**Trade-off**: Maximum durability per write, at the cost of write latency. The application does not need to issue a separate persist call to know that data is safe.

| Operating system | Underlying mechanism |
|------------------|----------------------|
| Linux            | File opened with `O_DSYNC` |
| Windows          | File opened with `FILE_FLAG_WRITE_THROUGH` |

## Persist to Non-Volatile Storage

**Behavior**: After one or more buffered writes, force any data still in the OS page cache or the storage device's own write cache out to non-volatile media. The call returns only once the data is durable.

**Trade-off**: Lets the application batch many writes cheaply and persist them with a single explicit call, instead of paying the durability cost on every write (as write-through does). This is the foundation of MariaDB's group-commit and binary-log durability behavior.

| Operating system | Underlying mechanism |
|------------------|----------------------|
| Linux            | `fsync()` |
| Windows          | `FlushFileBuffers()` |

## Persist Data Without Metadata Sync

**Behavior**: Like *persist to non-volatile storage*, but skips synchronization of non-essential file metadata such as the last-modified timestamp. The file contents and any metadata required to read them back are durable; bookkeeping metadata may still be in cache.

**Trade-off**: Cheaper than a full persist on filesystems where metadata updates would otherwise trigger an additional disk write. Used in performance-critical paths where MariaDB does not care about timestamp durability.

| Operating system | Underlying mechanism |
|------------------|----------------------|
| Linux            | `fdatasync()` |
| Windows          | `NtFlushBuffersFileEx()` with the `FLUSH_FLAGS_FILE_DATA_SYNC_ONLY` flag, with `FlushFileBuffers()` as a fallback on older Windows versions or non-NTFS filesystems |

## See Also

* [`innodb_flush_method`](../../../server-usage/storage-engines/innodb/innodb-flush-method.md) — selects InnoDB's combination of buffering and persistence strategies.
* [`sync_binlog`](../../standard-replication/replication-and-binary-log-system-variables.md#sync_binlog) — controls how often the binary log is persisted.
* [`innodb_doublewrite`](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_doublewrite) — InnoDB's protection against torn writes.
* [Filesystem Optimizations](filesystem-optimizations.md) — choosing and tuning the filesystem MariaDB writes to.
