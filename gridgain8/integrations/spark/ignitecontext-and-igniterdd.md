---
description: >-
  Use IgniteContext and IgniteRDD to read, save, and query GridGain cache data
  from Spark applications.
---

# IgniteContext and IgniteRDD

## IgniteContext

IgniteContext is the main entry point to Spark-GridGain integration. To create an instance of IgniteContext, user must provide an instance of SparkContext and a closure creating `IgniteConfiguration` (configuration factory). Ignite context will make sure that server or client Ignite nodes exist in all involved job instances. Alternatively, a path to an XML configuration file can be passed to `IgniteContext` constructor which will be used to configure nodes being started.

When creating an `IgniteContext` instance, an optional boolean `client` argument (defaulting to `true`) can be passed to context constructor. This is typically used in a Shared Deployment installation. When `client` is set to `false`, context will operate in embedded mode and will start server nodes on all workers during the context construction. This is required in an Embedded Deployment installation. See [Installation](installation.md) for information on deployment configurations.

{% hint style="warning" %}
**Embedded Mode Deprecation**

Embedded mode implies starting Ignite server nodes within Spark executors which can cause unexpected rebalancing or even data loss. Therefore this mode is currently deprecated and will be eventually discontinued. Consider starting a separate Ignite cluster and using standalone mode to avoid data consistency and performance issues.
{% endhint %}

Once `IgniteContext` is created, instances of `IgniteRDD` may be obtained using `fromCache` methods. It is not required that requested cache exist in Ignite cluster when RDD is created. If the cache with the given name does not exist, it will be created using provided configuration or template configuration.

For example, the following code will create an Ignite context with default Ignite configuration

```scala
val igniteContext = new IgniteContext(sparkContext,
    () => new IgniteConfiguration())
```

The following code will create an Ignite context configured from a file `example-shared-rdd.xml`:

```scala
val igniteContext = new IgniteContext(sparkContext,
    "examples/config/spark/example-shared-rdd.xml")
```

## IgniteRDD

`IgniteRDD` is an implementation of Spark RDD abstraction representing a live view of GridGain cache. `IgniteRDD` is not immutable, all changes in Ignite cache (regardless whether they were caused by another RDD or external changes in cache) will be visible to RDD users immediately.

`IgniteRDD` utilizes partitioned nature of Ignite caches and provides partitioning information to Spark executor. Number of partitions in `IgniteRDD` equals to the number of partitions in underlying Ignite cache. `IgniteRDD` also provides affinity information to Spark via `getPrefferredLocations` method so that RDD computations use data locality.

## Reading values from GridGain

Since `IgniteRDD` is a live view of Ignite cache, there is no need to explicitly load data to Spark application from Ignite. All RDD methods are available to use right away after an instance of `IgniteRDD` is created.

For example, assuming a GridGain cache with name "partitioned" contains string values, the following code will find all values that contain the word "GridGain":

```scala
val cache = igniteContext.fromCache("partitioned")
val result = cache.filter(_._2.contains("GridGain")).collect()
```

## Saving values to GridGain

Since GridGain caches operate on key-value pairs, the most straightforward way to save values to Ignite cache is to use a Spark tuple RDD and `savePairs` method. This method will take advantage of the RDD partitioning and store value to cache in a parallel manner, if possible.

It is also possible to save value-only RDD into GridGain cache using `saveValues` method. In this case `IgniteRDD` will generate a unique affinity-local key for each value being stored into the cache.

For example, the following code will store pairs of integers from 1 to 10000 into cache named "partitioned" using 10 parallel store operations:

```scala
val cacheRdd = igniteContext.fromCache("partitioned")

cacheRdd.savePairs(sparkContext.parallelize(1 to 10000, 10).map(i => (i, i)))
```

## Running SQL queries against a GridGain cache

When a GridGain cache is configured with the indexing subsystem enabled, it is possible to run SQL queries against the cache using `objectSql` and `sql` methods. See [Working with SQL](../../gridgain8-usage/sql/sql-introduction.md) for more information about Ignite SQL queries.

For example, assuming the "partitioned" cache is configured to index pairs of integers, the following code will get all integers in the range (10, 100):

```scala
val cacheRdd = igniteContext.fromCache("partitioned")

val result = cacheRdd.sql("select _val from Integer where val > ? and val < ?", 10, 100)
```

## Example

There are a couple of examples available on GitHub that demonstrate the usage of `IgniteRDD`:

- [Java Example](https://github.com/apache/ignite-extensions/tree/master/modules/spark-ext/examples/src/main/java/org/apache/ignite/examples/spark/SharedRDDExample.java)
