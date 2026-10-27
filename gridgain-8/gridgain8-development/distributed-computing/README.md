---
description: >-
  GridGain distributes computations across cluster nodes in a balanced and fault-tolerant manner, with support for the MapReduce pattern, cluster groups, load balancing, and job scheduling.
---

# Distributed Computing

GridGain provides an API for distributing computations across cluster nodes in a balanced and fault-tolerant manner. This section covers the distributed computing API, cluster groups, the executor service, fault tolerance, job scheduling, load balancing, and the MapReduce API.

{% columns %}
{% column %}
{% content-ref url="distributed-computing.md" %}
[Distributed Computing API](distributed-computing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain's distributed computing API distributes tasks across cluster nodes, with support for runnables, callables, closures, broadcasting, and asynchronous execution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cluster-groups.md" %}
[Cluster Groups](cluster-groups.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The ClusterGroup interface represents a logical group of nodes used to limit GridGain operations to a subset of the cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="executor-service.md" %}
[Executor Service](executor-service.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain provides a distributed ExecutorService implementation that submits load-balanced tasks to the cluster's server nodes for execution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="map-reduce.md" %}
[MapReduce API](map-reduce.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain's MapReduce API, provided by the ComputeTask interface, lets you split a task into jobs and aggregate their results.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="load-balancing.md" %}
[Load Balancing](load-balancing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain automatically load balances jobs across cluster nodes and supports round-robin, weighted random, and job-stealing load balancing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="fault-tolerance.md" %}
[Fault Tolerance](fault-tolerance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain supports automatic job failover, rerouting failed jobs to available nodes according to the configured failover SPI.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="job-scheduling.md" %}
[Job Scheduling](job-scheduling.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control how jobs are scheduled for processing on each node by configuring the CollisionSpi with FIFO or priority ordering.
{% endcolumn %}
{% endcolumns %}
