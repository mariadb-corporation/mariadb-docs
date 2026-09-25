---
description: >-
  GridGain provides distributed blocking queue and set implementations that can be created in collocated or non-collocated mode.
---

# Queue and Set

## Overview

In addition to providing standard key-value map-like storage, GridGain also provides an implementation of a fast Distributed Blocking Queue and Distributed Set.

`IgniteQueue` and `IgniteSet`, an implementation of `java.util.concurrent.BlockingQueue` and `java.util.Set` interface respectively, also support all operations from the `java.util.Collection` interface.
Both types can be created in either collocated or non-collocated mode.

Below is an example of how to create a distributed queue and set.

{% tabs %}
{% tab title="Queue" %}
```java
Ignite ignite = Ignition.start();

IgniteQueue<String> queue = ignite.queue("queueName", // Queue name.
        0, // Queue capacity. 0 for an unbounded queue.
        new CollectionConfiguration() // Collection configuration.
);
```
{% endtab %}
{% tab title="Set" %}
```java
Ignite ignite = Ignition.start();

IgniteSet<String> set = ignite.set("setName", // Set name.
        new CollectionConfiguration() // Collection configuration.
);
```
{% endtab %}
{% endtabs %}

## Collocated vs. Non-Collocated Mode

If you plan to create just a few queues or sets containing lots of data, then you would create them in non-collocated mode. This will make sure that about equal portion of each queue or set will be stored on each cluster node. On the other hand, if you plan to have many queues or sets, relatively small in size (compared to the whole cache), then you would most likely create them in collocated mode. In this mode all queue or set elements will be stored on the same cluster node, but about equal amount of queues/sets will be assigned to every node.

Non-collocated mode only makes sense for and is only supported for `PARTITIONED` caches.

A collocated queue and set can be created by setting the `collocated` property of `CollectionConfiguration`, like so:

{% tabs %}
{% tab title="Queue" %}
```java
Ignite ignite = Ignition.start();

CollectionConfiguration colCfg = new CollectionConfiguration();

colCfg.setCollocated(true);

// Create a colocated queue.
IgniteQueue<String> queue = ignite.queue("queueName", 0, colCfg);
```
{% endtab %}
{% tab title="Set" %}
```java
Ignite ignite = Ignition.start();

CollectionConfiguration colCfg = new CollectionConfiguration();

colCfg.setCollocated(true);

// Create a colocated set.
IgniteSet<String> set = ignite.set("setName", colCfg);
```
{% endtab %}
{% endtabs %}

## Cache Queues and Load Balancing

Given that elements will remain in the queue until someone takes them, and that no two nodes should ever receive the same element from the queue, cache queues can be used as an alternate work distribution and load balancing approach within GridGain.

For example, you could simply add computations, such as instances of `IgniteRunnable` to a queue, and have threads on remote nodes call `IgniteQueue.take()`  method which will block if queue is empty. Once the `take()` method will return a job, a thread will process it and call `take()` again to get the next job. Given this approach, threads on remote nodes will only start working on the next job when they have completed the previous one, hence creating ideally balanced system where every node only takes the number of jobs it can process, and not more.

## Collection Configuration

GridGain collections can be in configured in API via `CollectionConfiguration` (see above examples). The following configuration parameters can be used:

| Setter | Description | Default |
|---|---|---|
| `setCollocated(boolean)` | Sets collocation mode. | `false` |
| `setCacheMode(CacheMode)` | Sets underlying cache mode (`PARTITIONED`, `REPLICATED` or `LOCAL`). | `PARTITIONED` |
| `setAtomicityMode(CacheAtomicityMode)` | Sets underlying cache atomicity mode (`ATOMIC` or `TRANSACTIONAL`). | `ATOMIC` |
| `setOffHeapMaxMemory(long)` | Sets offheap maximum memory size. | `0` (unlimited) |
| `setBackups(int)` | Sets number of backups. | `0` |
| `setNodeFilter(IgnitePredicate<ClusterNode>)` | Sets optional predicate specifying on which nodes entries should be stored. | |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
