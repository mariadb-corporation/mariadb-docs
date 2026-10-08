---
description: >-
  Run your own code across a GridGain 9 cluster as distributed, balanced, and
  fault-tolerant compute jobs, including colocated execution, MapReduce tasks,
  and WebAssembly jobs.
---

# Distributed Computing

GridGain 9 lets you run your own code on the cluster in a distributed, balanced, and fault-tolerant way. This section explains how to configure and execute compute jobs, serialize the objects they exchange, and run WebAssembly compute jobs.

- [About Distributed Computing](about-distributed-computing.md) — configure and execute compute jobs, including colocated execution, MapReduce tasks, and .NET jobs.
- [Object Serialization](object-serialization.md) — control how job arguments and results are marshalled between servers and clients.
- [WebAssembly Compute Jobs](webassembly-compute-jobs.md) — run code compiled to WebAssembly on cluster nodes.

{% columns %}
{% column %}
{% content-ref url="about-distributed-computing.md" %}
[About Distributed Computing](about-distributed-computing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure and execute GridGain 9 compute jobs on one node, multiple nodes, or colocated with data, including .NET jobs, job states, failover, and MapReduce tasks.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="object-serialization.md" %}
[Object Serialization](object-serialization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control how GridGain 9 serializes compute job arguments and results, from automatic handling of native types and tuples to custom marshallers for user objects.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="webassembly-compute-jobs.md" %}
[WebAssembly Compute Jobs](webassembly-compute-jobs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run code compiled to WebAssembly on GridGain 9 cluster nodes, including runtime configuration, instance caching, and building modules in Rust, Go, WebAssembly text format, and Python.
{% endcolumn %}
{% endcolumns %}
