---
description: >-
  An overview of monitoring and metrics in GridGain: the available approaches,
  what to monitor at each layer, and the scope of global vs. node-specific metrics.
---

# Introduction: Monitoring and Metrics

This chapter covers monitoring and metrics in GridGain, starting with an overview of the methods available for monitoring and then delving into the GridGain specifics, including a list of JMX metrics and MBeans.

## Overview

The basic monitoring task in GridGain involves metrics. There are several approaches to accessing metrics:

- via [Control Center]({tools}/control-center)
- via [JMX](../../reference/monitoring/jmx-metrics.md)
- Programmatically
- [System views](../../reference/monitoring/system-views.md)

{% hint style="info" %}
**Monitoring vs Auditing**

While getting Auditing/Event information is not covered in this chapter, it is often used in conjunction with metrics and monitoring. For more information on Auditing, see [Security and Auditing](../../security/auditing-events.md).
{% endhint %}

## What to Monitor

You can start by monitoring:

- Each node in isolation
- The Connection between nodes
- The system as a whole

Note that a node consists of several layers: hardware, the operating system, the Virtual Machine (JVM, etc.), and the application. You need to check all of these levels, and the network surrounding it.

- Hardware (Hypervisor): CPU/Memory/Disk => System Logs/Cloud Provider's Logs
- Operating System
- JVM: GC Logs, JMX, Java Flight Recorder, Thread Dumps, Heap dumps, etc.
- Application: Logs, JMX, Throughput/Latency, Test queries
  * For log based monitoring, the key is that you can act proactively, watch the logs for trends/etc., don't just wait to check the logs until something breaks.
- Network: ping monitoring, network hardware monitoring, TCP dumps

This should give you a good place to start for setting up monitoring of your hardware, operating system, and network. To monitor the application layer (the nodes that make up your in-memory computing solution), you'll need to perform GridGain-specific monitoring via metrics you access with JMX/Beans or Control Center, or programmatically.

## Global vs. Node-specific Metrics

The information exposed through different metrics has different scope (applicability), and may be different depending on the node where you get the metrics.
The following list explains different metric scopes.

**Global metrics**: Provide information about the cluster in general, for example: the number nodes, state of the cluster. This information is available on any node of the cluster.

**Node-specific metrics**: Provide information specific to the node on which you obtain the metrics, for example: memory consumption, data region metrics, WAL size, queue size, etc.

Cache-related metrics can be global as well as node-specific.
For example, the total number of entries in a cache is a global metric, and you can obtain it on any node.
You can also get the number of entries of the cache that are stored on a specific node, in which case it will be a node-specific metric.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
