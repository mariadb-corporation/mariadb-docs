---
description: >-
  Recommended JVM options for GridGain 9, including heap sizing guidance,
  garbage collector tuning, thread pools, and NUMA-aware memory allocation.
---

# JVM Tuning

## Recommended JVM Options

Below is the list of recommended JVM options for high performance GridGain installations in embedded mode:

```
-server
-XX:+AlwaysPreTouch
-XX:+HeapDumpOnOutOfMemoryError \
-XX:+ExitOnOutOfMemoryError"
-XX:HeapDumpPath=/path/to/dump \
-Xlog:gc=info:file=/path/to/gc-%t.log::filecount=10,filesize=100m" \
-Xms16g \
-Xmx16g \
-XX:+UseG1GC \
-XX:G1HeapRegionSize=32m \
-XX:+PerfDisableSharedMem
```

## Heap Sizes Between 32 GB and 47 GB

Do not set the maximum heap size (`-Xmx`) to a value between 32 GB and roughly 47 GB.
A heap in that range holds less data than a 31 GB heap does.

Below 32 GB, the JVM stores object references as 32-bit values, a technique called compressed ordinary object pointers, or compressed oops.
At 32 GB the JVM turns compressed oops off, every reference grows from 4 to 8 bytes, and every object that holds references grows with them, so fewer objects fit.
The heap has to reach roughly 47 GB before the added capacity makes up for the larger references.
The exact crossover depends on how many references your data holds.

Set `-Xmx` to 31 GB or less, or to well above 47 GB.
Raising a 31 GB heap to 40 GB can cause the very `OutOfMemoryError` it was meant to prevent.

{% hint style="info" %}
The 32 GB threshold assumes the default object alignment of 8 bytes. Raising `-XX:ObjectAlignmentInBytes` moves the threshold higher, at the cost of more padding per object.
{% endhint %}

## Garbage collector tuning

G1 is a recommended collector for GridGain.

Normally G1 collector doesn't require any special tuning due to its adaptive behavior and works fine out of the box.

However, you can try other collectors, like [ZGC](https://docs.oracle.com/en/java/javase/21/gctuning/z-garbage-collector.html) and see if they work better for you workload.
Collectors availability depends on JVM vendor.

```
-XX:+UseG1GC \
-XX:G1HeapRegionSize=32m \
```

## Thread Pools Tuning

All worker pools are sized automatically and don't require special tuning.

## NUMA-Aware Memory Allocation

G1 garbage collector is NUMA-aware since release 14. It can be enabled with:

```
-XX:+UseNUMA
```
