---
description: >-
  GridGain automatically load balances jobs across cluster nodes and supports round-robin, weighted random, and job-stealing load balancing.
---

# Load Balancing

GridGain automatically load balances jobs produced by a [compute task](map-reduce.md) as well as individual tasks submitted via the distributed computing API. Individual tasks submitted via `IgniteCompute.run(...)` and other compute methods are treated as tasks producing a single job.

By default, GridGain uses a round-robin algorithm (`RoundRobinLoadBalancingSpi`), which distributes jobs in sequential order across the nodes specified for the compute task.

{% hint style="info" %}
Load balancing does not apply to [colocated computations](../colocating-computations.md).
{% endhint %}

The load balancing algorithm is controlled by the `IgniteConfiguration.loadBalancingSpi` property.

## Round-Robin Load Balancing

`RoundRobinLoadBalancingSpi` iterates through the available nodes in a round-robin fashion and picks the next sequential node. The available nodes are defined when you [get the compute instance](distributed-computing.md#getting-the-compute-interface) through which you execute your tasks.

Round-Robin load balancing supports two modes of operation: per-task and global.

When configured in per-task mode, the implementation picks a random node at the beginning of every task execution and then sequentially iterates through all the nodes in the topology starting from that node. For cases when the split size of a task is equal to the number of nodes, this mode guarantees that all nodes will participate in job execution.

{% hint style="warning" %}
The per-task mode requires that the following event types be enabled: `EVT_TASK_FAILED`, `EVT_TASK_FINISHED`, `EVT_JOB_MAPPED`.
{% endhint %}

When configured in global mode, a single sequential queue of nodes is maintained for all tasks and the next node in the queue is picked every time. In this mode (unlike in per-task mode), it is possible that even if the split size of a task is equal to the number of nodes, some jobs within the same task will be assigned to the same node whenever multiple tasks are executing concurrently.

The global mode is used by default.

{% tabs %}
{% tab title="XML" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans" 
    xmlns:util="http://www.springframework.org/schema/util" 
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" 
    xsi:schemaLocation="         http://www.springframework.org/schema/beans
         http://www.springframework.org/schema/beans/spring-beans.xsd
         http://www.springframework.org/schema/util
         http://www.springframework.org/schema/util/spring-util.xsd">
    <bean class="org.apache.ignite.configuration.IgniteConfiguration">
        <property name="includeEventTypes">
            <list>
                <!--these events are required for the per-task mode-->
                <util:constant static-field="org.apache.ignite.events.EventType.EVT_TASK_FINISHED"/>
                <util:constant static-field="org.apache.ignite.events.EventType.EVT_TASK_FAILED"/>
                <util:constant static-field="org.apache.ignite.events.EventType.EVT_JOB_MAPPED"/>
            </list>
        </property>

        <property name="loadBalancingSpi">
            <bean class="org.apache.ignite.spi.loadbalancing.roundrobin.RoundRobinLoadBalancingSpi">
                <!-- Activate the per-task round-robin mode. -->
                <property name="perTask" value="true"/>
            </bean>
        </property>

    </bean>
</beans>
```
{% endtab %}
{% tab title="Java" %}
```java
RoundRobinLoadBalancingSpi spi = new RoundRobinLoadBalancingSpi();
spi.setPerTask(true);

IgniteConfiguration cfg = new IgniteConfiguration();
// these events are required for the per-task mode
cfg.setIncludeEventTypes(EventType.EVT_TASK_FINISHED, EventType.EVT_TASK_FAILED, EventType.EVT_JOB_MAPPED);

// Override default load balancing SPI.
cfg.setLoadBalancingSpi(spi);

// Start a node.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Random and Weighted Load Balancing

`WeightedRandomLoadBalancingSpi` picks a random node from the list of available nodes. You can also optionally assign weights to nodes, so that nodes with larger weights will end up getting proportionally more jobs routed to them. By default all nodes get a weight of 10.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="loadBalancingSpi">
        <bean class="org.apache.ignite.spi.loadbalancing.weightedrandom.WeightedRandomLoadBalancingSpi">
            <property name="useWeights" value="true"/>
            <property name="nodeWeight" value="10"/>
        </bean>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
WeightedRandomLoadBalancingSpi spi = new WeightedRandomLoadBalancingSpi();

// Configure SPI to use the weighted random load balancing algorithm.
spi.setUseWeights(true);

// Set weight for the local node.
spi.setNodeWeight(10);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default load balancing SPI.
cfg.setLoadBalancingSpi(spi);

// Start a node.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Job Stealing

Quite often grids are deployed across many computers some of which may be more powerful or under-utilized than others. Enabling `JobStealingCollisionSpi` helps avoid jobs being stuck at an over-utilized node, as they will be stolen by an under-utilized node.

`JobStealingCollisionSpi` supports job stealing from over-utilized nodes to under-utilized nodes. This SPI is especially useful if you have some jobs that complete quickly, while others are sitting in the waiting queue on over-utilized nodes. In such a case, the waiting jobs will be stolen from the slower node and moved to the fast/under-utilized node.

`JobStealingCollisionSpi` adopts a "late" load balancing technique, which allows reassigning a job from node A to node B after the job has been scheduled for execution on node A​.

Here is an example of how to configure `JobStealingCollisionSpi`:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <!-- Enabling the required Failover SPI. -->
    <property name="failoverSpi">
        <bean class="org.apache.ignite.spi.failover.jobstealing.JobStealingFailoverSpi"/>
    </property>
    <!-- Enabling the JobStealingCollisionSpi for late load balancing. -->
    <property name="collisionSpi">
        <bean class="org.apache.ignite.spi.collision.jobstealing.JobStealingCollisionSpi">
            <property name="activeJobsThreshold" value="50"/>
            <property name="waitJobsThreshold" value="0"/>
            <property name="messageExpireTime" value="1000"/>
            <property name="maximumStealingAttempts" value="10"/>
            <property name="stealingEnabled" value="true"/>
            <property name="stealingAttributes">
                <map>
                    <entry key="node.segment" value="foobar"/>
                </map>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
JobStealingCollisionSpi spi = new JobStealingCollisionSpi();

// Configure number of waiting jobs
// in the queue for job stealing.
spi.setWaitJobsThreshold(10);

// Configure message expire time (in milliseconds).
spi.setMessageExpireTime(1000);

// Configure stealing attempts number.
spi.setMaximumStealingAttempts(10);

// Configure number of active jobs that are allowed to execute
// in parallel. This number should usually be equal to the number
// of threads in the pool (default is 100).
spi.setActiveJobsThreshold(50);

// Enable stealing.
spi.setStealingEnabled(true);

// Set stealing attribute to steal from/to nodes that have it.
spi.setStealingAttributes(Collections.singletonMap("node.segment", "foobar"));

// Enable `JobStealingFailoverSpi`
JobStealingFailoverSpi failoverSpi = new JobStealingFailoverSpi();

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default Collision SPI.
cfg.setCollisionSpi(spi);

cfg.setFailoverSpi(failoverSpi);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
If you want to enable job stealing, you have to configure `org.apache.ignite.spi.failover.jobstealing.JobStealingFailoverSpi`.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
