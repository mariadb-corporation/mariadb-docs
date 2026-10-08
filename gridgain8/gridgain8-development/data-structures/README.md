---
description: >-
  GridGain provides distributed implementations of common data structures, including atomic types, sequences, latches, locks, semaphores, queues, and sets.
---

# Data Structures

GridGain provides distributed implementations of common data structures that work across all cluster nodes, including atomic types, a distributed ID generator, count-down latches, locks, semaphores, queues, and sets.

{% columns %}
{% column %}
{% content-ref url="queue-and-set.md" %}
[Queue and Set](queue-and-set.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain provides distributed blocking queue and set implementations that can be created in collocated or non-collocated mode.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="atomic-types.md" %}
[Atomic Types](atomic-types.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain distributed atomic long and atomic reference to perform cluster-wide atomic operations on a globally visible value.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="countdownlatch.md" %}
[CountDownLatch](countdownlatch.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
IgniteCountDownLatch provides a distributed count-down latch that synchronizes operations across cluster nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="locks.md" %}
[Locks](locks.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain distributed reentrant locks to lock threads across the cluster, with optional failover safety and fair or non-fair ordering.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="semaphore.md" %}
[Semaphore](semaphore.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain's counting distributed semaphore restricts access to a resource or synchronizes execution flow cluster-wide.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="id-generator.md" %}
[ID Generator](id-generator.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The distributed atomic sequence provided by IgniteCacheAtomicSequence is an efficient data structure for implementing a cluster-wide ID generator.
{% endcolumn %}
{% endcolumns %}
