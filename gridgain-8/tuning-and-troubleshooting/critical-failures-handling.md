---
description: >-
  How GridGain detects critical failures, configures the failure handler, and runs health checks on critical system workers.
---

# Critical Failures Handling

GridGain is a robust and fault tolerant system. But in the real world, some unpredictable issues and problems arise that can affect the state of both an individual node as well as the whole cluster. Such issues can be detected at runtime and handled accordingly using a preconfigured critical failure handler.

## Critical Failures

The following failures are treated as critical:

- System critical errors (e.g. `OutOfMemoryError`).
- Unintentional system worker termination (e.g. due to an unhandled exception).
- System workers hanging.
- Cluster nodes segmentation.

A system critical error is an error which leads to the system's inoperability. For example:

- File I/O errors - usually `IOException` is thrown by file read/write operations. It's possible when Ignite native persistence is enabled (e.g., in cases when no space is left or on a device error), and also for in-memory mode because GridGain uses disk storage for keeping some metadata (e.g., in cases when the file descriptors limit is exceeded or file access is prohibited).
- Out of memory error - when GridGain memory management system fails to allocate more space (`IgniteOutOfMemoryException`).
- Out of memory error - when a cluster node runs out of Java heap (`OutOfMemoryError`).

## Failures Handling

When GridGain detects a critical failure, it handles the failure according to a preconfigured failure handler. The failure handler can be configured as follows:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="failureHandler">
        <bean class="org.apache.ignite.failure.StopNodeFailureHandler"/>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
cfg.setFailureHandler(new StopNodeFailureHandler());
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% endtabs %}

GridGain support following failure handlers:

| Class | Description |
| --- | --- |
| `NoOpFailureHandler` | Ignores any failures. Useful for testing and debugging. |
| `RestartProcessFailureHandler` | A specific implementation that can be used only with `ignite.sh\|bat`. The process must be terminated by using the `Ignition.restart(true)` method. |
| `StopNodeFailureHandler` | Stops the node in case of critical errors by calling the `Ignition.stop(true)` or `Ignition.stop(nodeName, true)` methods. |
| `StopNodeOrHaltFailureHandler` | This is the default handler, which tries to stop a node. If the node can't be stopped, then the handler terminates the JVM process. |

## Critical Workers Health Check

GridGain has a number of internal workers that are essential for the cluster to function correctly. If one of them is terminated, the node can become inoperative.

The following system workers are considered mission critical:

- Discovery worker - discovery events handling.
- TCP communication worker - peer-to-peer communication between nodes.
- Exchange worker - partition map exchange.
- Workers of the system's striped pool.
- Data Streamer striped pool workers.
- Timeout worker - timeouts handling.
- Checkpoint thread - check-pointing in Ignite persistence.
- WAL workers - write-ahead logging, segments archiving, and compression.
- Expiration worker - TTL based expiration.
- NIO workers - base networking.

GridGain has an internal mechanism for verifying that critical workers are operational. Each worker is regularly checked to confirm that it is alive and updating its heartbeat timestamp. If a worker is not alive and updating, the worker is regarded as blocked and GridGain will print a message to the log file. You can set the period of inactivity via the `IgniteConfiguration.systemWorkerBlockedTimeout` property.

Even though GridGain considers an unresponsive system worker to be a critical error, it doesn't handle this situation automatically, other than printing out a message to the log file. If you want to enable a particular failure handler for unresponsive system workers of all the types, clear the `ignoredFailureTypes` property of the handler as shown below:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="systemWorkerBlockedTimeout" value="#{60 * 60 * 1000}"/>

    <property name="failureHandler">
        <bean class="org.apache.ignite.failure.StopNodeFailureHandler">

          <!-- Enable this handler to react to unresponsive critical workers occasions. -->
          <property name="ignoredFailureTypes">
            <list>
            </list>
          </property>

      </bean>

    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
StopNodeFailureHandler failureHandler = new StopNodeFailureHandler();
failureHandler.setIgnoredFailureTypes(Collections.EMPTY_SET);

IgniteConfiguration cfg = new IgniteConfiguration().setFailureHandler(failureHandler);

Ignite ignite = Ignition.start(cfg);
```
{% endtab %}
{% endtabs %}
