---
description: >-
  Read GridGain data region and data storage metrics programmatically, and
  calculate current node, cache, and cluster memory usage from the metric beans.
---

# Monitoring Memory

GridGain provides metrics for [data regions](../../gridgain8-usage/memory-configuration/data-regions.md) and persistence. This page shows how to read those metrics programmatically and how to use them to calculate memory usage. To enable or disable these metrics, see [Configuring Metrics](configuring-metrics.md); for the full list of available metrics, see the [Monitoring Reference](../../reference/monitoring/README.md).

## Data Region Metrics

GridGain's [memory-centric storage](../../gridgain8-usage/memory-configuration/README.md) can be monitored through the `DataRegionMetrics` interface and the related JMX bean. These metrics help you track overall memory utilization, measure performance, and plan optimizations. Because a node can have several data regions configured, metrics are collected for each region individually.

### Reading Data Region Metrics

Use `DataRegionMetricsMXBean` or the `Ignite.dataRegionMetrics()` method to get the latest metrics snapshot and iterate over it:

```java
// Get the metrics of all the data regions configured on a node.
Collection<DataRegionMetrics> regionsMetrics = ignite.dataRegionMetrics();

// Print out some of the metrics.
for (DataRegionMetrics metrics : regionsMetrics) {
    System.out.println(">>> Memory Region Name: " + metrics.getName());
    System.out.println(">>> Allocation Rate: " + metrics.getAllocationRate());
    System.out.println(">>> Fill Factor: " + metrics.getPagesFillFactor());
    System.out.println(">>> Allocated Size: " + metrics.getTotalAllocationSize());
    System.out.println(">>> Physical Memory Size: " + metrics.getPhysicalMemorySize());
}
```

All `DataRegionMetrics` of a local node are also available through the `DataRegionMetricsMXBean` JMX interface, which you can access from any JMX-compliant tool or API. The JMX beans expose the same metrics as `DataRegionMetrics` plus a few additional ones. For the full list of data region metrics, see [Generic Metrics](../../reference/monitoring/generic-metrics.md) and [JMX Metrics](../../reference/monitoring/jmx-metrics.md).

## Persistent Data Storage Metrics

When persistence is enabled for a data region, GridGain exposes additional metrics through the `DataStorageMetrics` interface and the `DataStorageMetricsMXBean` JMX bean, covering data volume, data storage, and page replacement.

{% hint style="warning" %}
**Cost of enabling data storage metrics**

Collecting data storage metrics is not a free operation and can affect application performance, so these metrics are disabled by default. See [Configuring Metrics](configuring-metrics.md) for how to enable or disable them.
{% endhint %}

### Reading Data Storage Metrics

Call `Ignite.dataStorageMetrics()` to get the latest persistence metrics snapshot:

```java
// Getting metrics.
DataStorageMetrics pm = ignite.dataStorageMetrics();

System.out.println("Fsync duration: " + pm.getLastCheckpointFsyncDuration());
System.out.println("Data pages: " + pm.getLastCheckpointDataPagesNumber());
System.out.println("Checkpoint duration:" + pm.getLastCheckpointDuration());
```

## Memory Usage Calculation

You can obtain metrics for the caches associated with a particular cache group through the `CacheGroupMetricsMXBean` JMX bean. Use the following metrics to calculate memory usage.

### Single-Node Memory Usage

- The current node size — the total size of data on a node — is `DataStorageMetricsMXBean.getTotalAllocatedSize`.
- The current size of a specific cache on a node is `CacheGroupMetricsMXBean.getTotalAllocatedSize`. There must be only one cache within the cache group (the default) for this metric to be meaningful.

### Cluster-Wide Memory Usage

- To calculate the total cluster size, sum `DataStorageMetricsMXBean.getTotalAllocatedSize` across all nodes.
- The current cache size is the sum of `CacheGroupMetricsMXBean.getTotalAllocatedSize` across all nodes. Again, there must be only one cache within the cache group for this metric to be meaningful.
