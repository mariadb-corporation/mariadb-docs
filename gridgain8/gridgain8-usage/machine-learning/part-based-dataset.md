---
description: >-
  How the partition-based dataset abstraction underpins GridGain Machine Learning algorithms with zero-ETL, fault-tolerant, MapReduce-style computation.
---

# Partition Based Dataset

## Overview

Partition-Based Dataset is an abstraction layer on top of the Apache Ignite storage and computational capabilities that allow us to build algorithms in accordance with [zero ETL](ml.md#zero-etl-and-massive-scalability) and [fault tolerance](ml.md#fault-tolerance-and-continuous-learning) principles.

A main idea behind the partition-based datasets is the classic [MapReduce](https://en.wikipedia.org/wiki/MapReduce) approach implemented using the Compute Grid in Ignite.

The most important advantage of MapReduce is the ability to perform computations on data distributed across the cluster without involving significant data transfers over the network. This idea is adopted in the partition-based datasets in the following way:

- Every dataset is spread across partitions;
- Partitions hold a persistent training context and recoverable training data stored locally on every node;
- Computations needed to be performed on a dataset splits on Map operations which executes on every partition and Reduce operations which reduces results of Map operations to one final result.

*Training Context (Partition Context)* is a persistent part of the partition which is kept in an Apache Ignite, so that all changes made in this part will be consistently maintained until a partition-based dataset is closed. Training context survives node failures but requires additional time to read and write, so it should be used only when it's not possible to use partition data.

*Training Data (Partition Data)* is a part of the partition that can be recovered from the upstream data and context at any time. Because of this, it is not necessary to maintain partition data in some persistent storage, so that partition data is kept on every node in local storage (On-Heap, Off-Heap, or even in GPU memory) and in case of node failure is recovered from upstream data and context on another node.

Why have partitions been selected as dataset and learning building blocks instead of cluster nodes?

One of the fundamental ideas of an Apache Ignite is that partitions are atomic, which means that they cannot be split between multiple nodes (see [Cache mode](../../architecture/data-modeling/data-partitioning.md#partitioned-replicated-mode) for more details). As a result in the case of rebalancing or node failure, a partition will be recovered on another node with the same data it contained on the previous node.

In case of a machine learning algorithm, it's vital​ because most of the ML algorithms are iterative and require some context maintained between iterations. This context cannot be split or merged and should be maintained in a consistent state during the whole learning process.

## Usage

To build a partition-based dataset you need to specify:

- Upstream Data Source which can be an Ignite Cache or just a Map with data;
- Partition Context Builder that defines how to build a partition context from upstream data rows corresponding to this partition;
- Partition Data Builder that defines how to build partition data from upstream data rows corresponding to this partition.

{% tabs %}
{% tab title="Cache Based Dataset" %}
```java
Dataset<MyPartitionContext, MyPartitionData> dataset =
    new CacheBasedDatasetBuilder<>(
        ignite,                            // Upstream Data Source
        upstreamCache
    ).build(
        new MyPartitionContextBuilder<>(), // Training Context Builder
        new MyPartitionDataBuilder<>()     // Training Data Builder
    );
```
{% endtab %}
{% tab title="Local Dataset" %}
```java
Dataset<MyPartitionContext, MyPartitionData> dataset =
    new LocalDatasetBuilder<>(
        upstreamMap,                       // Upstream Data Source
        10
    ).build(
        new MyPartitionContextBuilder<>(), // Partition Context Builder
        new MyPartitionDataBuilder<>()     // Partition Data Builder
    );
```
{% endtab %}
{% endtabs %}

After this you are able to perform different computations on this dataset in a MapReduce manner.

{% code title="Java" %}
```java
int numerOfRows = dataset.compute(
    (partitionData, partitionIdx) -> partitionData.getRows(),
    (a, b) -> a == null ? b : a + b
);
```
{% endcode %}

And, finally, when all computations are completed it's important to close the dataset and free resources.

{% code title="Java" %}
```java
dataset.close();
```
{% endcode %}

## Examples

To see how the Partition Based Dataset can be used in practice, try this [example](https://github.com/apache/ignite-extensions/tree/master/modules/ml-ext/examples/src/main/java/org/apache/ignite/examples/ml/dataset/AlgorithmSpecificDatasetExample.java), available on GitHub and delivered with every Apache Ignite distribution.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
