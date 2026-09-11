---
description: >-
  What a committed write guarantees on a TideSQL table under each sync mode, and
  the single server setting that decides it.
---

# TideSQL Durability and Sync Modes

When a commit returns success on a TidesDB table, what has actually happened to those bytes is decided by one server setting, `tidesdb_memtable_sync_mode`. Every table shares the library's write-ahead log, so this is a single global choice rather than a per-table one, and it governs the durability of every commit.

## The Three Modes

| Mode | On return from commit, the write is | Survives a process crash | Survives a machine crash |
| --- | --- | --- | --- |
| `NONE` | In an in-process buffer, not yet handed to the operating system | No | No |
| `INTERVAL` | Handed to the operating system, and on the device within the interval | Yes | Within the interval |
| `FULL` *(default)* | On the device | Yes | Yes |

The mode that is easy to misread is `NONE`. Under `NONE` the library does nothing at commit time, so an acknowledged commit sits in an in-process buffer until a later batch writes it out. If the process stops before that happens, a kill, an abort, an OOM, the commit is gone, and a machine crash loses it too. `NONE` is the fastest mode and the least durable.

{% hint style="danger" %}
Reach for `NONE` only when the data can be rebuilt, never when an acknowledged commit has to stay acknowledged. A process crash discards commits that have already returned success.
{% endhint %}

`INTERVAL` and `FULL` both hand each commit to the operating system before returning, so neither loses an acknowledged commit to a process crash. They differ only in the machine-crash guarantee, covered below.

TideSQL defaults to `FULL`, so out of the box a committed write has reached the device and survives a power loss. This is the safe default for a database engine. `NONE` and `INTERVAL` trade some of that guarantee for throughput and are the right choice for data that is reconstructible, a cache, a derived index, or an analytics store, where losing the last moment of writes to a power cut costs a rebuild rather than correctness.

## What FULL Costs and How INTERVAL Sits Between

`FULL` costs commit throughput, because every commit waits for the device instead of returning once the bytes reach the operating system. How much depends entirely on the storage. Group commit softens the cost by letting concurrent commits that land in the same commit round share a single device sync, so the more concurrent the workload the better `FULL` amortizes.

`INTERVAL` forces the log on a timer, so the exposure to a machine crash is bounded by `tidesdb_memtable_sync_interval` microseconds rather than being unbounded, without paying a device barrier on every commit.

{% code title="my.cnf" %}
```ini
[mysqld]
tidesdb_memtable_sync_mode = INTERVAL
tidesdb_memtable_sync_interval = 500000   # 500 ms
```
{% endcode %}

`tidesdb_memtable_sync_mode` and `tidesdb_memtable_sync_interval` are read-only and set at server startup. For the underlying mechanics of the write-ahead log and recovery, see the TidesDB library manual.

<sub>_This page is licensed: GPLv2_</sub>
