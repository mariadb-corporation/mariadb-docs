---
description: >-
  Use GridGain distributed atomic long and atomic reference to perform cluster-wide atomic operations on a globally visible value.
---

# Atomic Types

GridGain supports distributed atomic long and atomic reference, similar to `java.util.concurrent.atomic.AtomicLong` and `java.util.concurrent.atomic.AtomicReference` respectively.

Atomics in GridGain are distributed across the cluster, essentially enabling performing atomic operations (such as increment-and-get or compare-and-set) with the same globally-visible value. For example, you could update the value of an atomic long on one node and read it from another node.

Features:

- Retrieve current value.
- Atomically modify current value.
- Atomically increment or decrement current value.
- Atomically compare-and-set the current value to new value.

Distributed atomic long and atomic reference can be obtained via `IgniteAtomicLong` and `IgniteAtomicReference` interfaces respectively, as shown below:

{% tabs %}
{% tab title="AtomicLong" %}
```java
Ignite ignite = Ignition.start();

IgniteAtomicLong atomicLong = ignite.atomicLong("atomicName", // Atomic long name.
        0, // Initial value.
        true // Create if it does not exist.
);

// Increment atomic long on local node
System.out.println("Incremented value: " + atomicLong.incrementAndGet());
```
{% endtab %}
{% tab title="AtomicReference" %}
```java
Ignite ignite = Ignition.start();

// Create an AtomicReference
IgniteAtomicReference<String> ref = ignite.atomicReference("refName", // Reference name.
        "someVal", // Initial value for atomic reference.
        true // Create if it does not exist.
);

// Compare and update the value
ref.compareAndSet("WRONG EXPECTED VALUE", "someNewVal"); // Won't change.
```
{% endtab %}
{% endtabs %}

All atomic operations provided by `IgniteAtomicLong` and `IgniteAtomicReference` are synchronous. The time an atomic operation will take depends on the number of nodes performing concurrent operations with the same instance of atomic long, the intensity of these operations, and network latency.

## Atomic Configuration

Atomics in GridGain can be configured via the `atomicConfiguration` property of `IgniteConfiguration`.

The following table lists available configuration parameters:

| Setter | Description | Default |
|---|---|---|
| `setBackups(int)` | The number of backups. | 1 |
| `setCacheMode(CacheMode)` | Cache mode for all atomic types. | `PARTITIONED` |
| `setAtomicSequenceReserveSize(int)` | Sets the number of sequence values reserved for `IgniteAtomicSequence` instances. | 1000 |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
