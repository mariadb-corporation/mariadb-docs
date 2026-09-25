---
description: >-
  Overview of the internal thread pools GridGain maintains, how to size them, and
  how to create a custom thread pool for compute tasks.
---

# Thread Pools Tuning

GridGain creates and maintains a variety of thread pools that are used for different purposes. In this section, we list some of the more common internal pools and show how you can create a custom one.

{% hint style="info" %}
Starting in 8.9.38, each pool listed below also has a matching system property (for example, `IGNITE_PUBLIC_THREAD_POOL_SIZE`) that overrides the size configured through `IgniteConfiguration`.
GridGain reads these properties only when the node starts, so changes take effect after a restart, not while the node is running.
{% endhint %}

## System Pool

The system pool handles all the cache related operations except for SQL and some other types of queries that go to the queries pool.
Also, this pool is responsible for processing compute tasks' cancellation operations.

The default pool size is `max(8, total number of cores)`.
Use `IgniteConfiguration.setSystemThreadPoolSize(...)` or a similar API from your programming language to change the pool size.
You can also set the `IGNITE_SYSTEM_THREAD_POOL_SIZE` system property.

## Queries Pool

The queries pool takes care of all SQL, Scan, and SPI queries being sent and executed across the cluster.

The default pool size is `max(8, total number of cores)`.
Use `IgniteConfiguration.setQueryThreadPoolSize(...)` or a similar API from your programming language to change the pool size.
You can also set the `IGNITE_QUERY_THREAD_POOL_SIZE` system property.

## Public Pool

Public pool is the work-horse of the Compute Grid. All computations are received and processed by this pool.

The default pool size is `max(8, total number of cores)`. Use `IgniteConfiguration.setPublicThreadPoolSize(...)` or a similar API from your programming language to change the pool size.
You can also set the `IGNITE_PUBLIC_THREAD_POOL_SIZE` system property.

## Service Pool

Service Grid calls go to the services' thread pool.
Having dedicated pools for the Service and Compute components allows us to avoid threads starvation and deadlocks when a service implementation wants to call a computation or vice versa.

The default pool size is `max(8, total number of cores)`. Use `IgniteConfiguration.setServiceThreadPoolSize(...)` or a similar API from your programming language to change the pool size.
You can also set the `IGNITE_SERVICE_THREAD_POOL_SIZE` system property.

If you don't set a service pool size explicitly, it defaults to the size of the public pool.
Setting `IGNITE_PUBLIC_THREAD_POOL_SIZE` does not change the service pool size — set `IGNITE_SERVICE_THREAD_POOL_SIZE` explicitly if you need a different value.

## Striped Pool

The striped pool helps accelerate basic cache operations and transactions by spreading operations execution across multiple stripes that don't contend with each other for resources.

The default pool size is `max(8, total number of cores)`. Use `IgniteConfiguration.setStripedPoolSize(...)` or a similar API from your programming language to change the pool size.
You can also set the `IGNITE_STRIPED_THREAD_POOL_SIZE` system property.

## Data Streamer Pool

The data streamer pool processes all messages and requests coming from `IgniteDataStreamer` and a variety of streaming adapters that use `IgniteDataStreamer` internally.

The default pool size is `max(8, total number of cores)`. Use `IgniteConfiguration.setDataStreamerThreadPoolSize(...)` or a similar API from your programming language to change the pool size.
You can also set the `IGNITE_DATA_STREAMER_THREAD_POOL_SIZE` system property.

## Creating Custom Thread Pool

It is possible to configure a custom thread pool for compute tasks.
This is useful if you want to execute one compute task from another synchronously avoiding deadlocks.
To guarantee this, you need to make sure that a nested task is executed in a thread pool separate from the parent's tasks thread pool.

A custom pool is defined in `IgniteConfiguration` and must have a unique name:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="executorConfiguration">
        <list>
            <bean class="org.apache.ignite.configuration.ExecutorConfiguration">
                <property name="name" value="myPool"/>
                <property name="size" value="16"/>
            </bean>
        </list>
    </property>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setExecutorConfiguration(new ExecutorConfiguration("myPool").setSize(16));
```
{% endtab %}
{% endtabs %}

Now, let's assume that you want to execute the following compute task in a thread from the `myPool` defined above:

```java
public class InnerRunnable implements IgniteRunnable {
    @Override
    public void run() {
        System.out.println("Hello from inner runnable!");
    }
}
```

To do that, use `IgniteCompute.withExecutor()`, which will execute the task immediately from the parent task, as shown below:

```java
public class OuterRunnable implements IgniteRunnable {
    @IgniteInstanceResource
    private Ignite ignite;

    @Override
    public void run() {
        // Synchronously execute InnerRunnable in a custom executor.
        ignite.compute().withExecutor("myPool").run(new InnerRunnable());
        System.out.println("outer runnable is executed");
    }
}
```

The parent task's execution might be triggered the following way and, in this scenario, it will be executed by the public pool:

```java
ignite.compute().run(new OuterRunnable());
```

{% hint style="warning" %}
**Undefined Thread Pool**

If an application attempts to execute a compute task in a custom pool which is not defined in the configuration of the node, then a special warning message will be printed to the logs, and the task will be picked up by the public pool for execution.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
