---
description: >-
  How client nodes connect and reconnect to a GridGain cluster, handle
  disconnect/reconnect events, and how to manage slow client nodes.
---

# Connecting Client Nodes

## Reconnecting a Client Node

A client node can get disconnected from the cluster in several cases:

* The client node cannot re-establish the connection with the server node due to network issues.
* Connection with the server node was broken for some time; the client node is able to re-establish the connection with the cluster, but the server already dropped the client node since the server did not receive client heartbeats.
* Slow clients can be kicked out by the cluster.

When a client determines that it is disconnected from the cluster, it assigns a new node ID to itself and tries to reconnect to the cluster.
Note that this has a side effect: the ID property of the local `ClusterNode` changes in the case of a client reconnection.
This means that any application logic that relied on the ID may be affected.

You can disable client reconnection in the node configuration:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="clientMode" value="true"/>
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <!-- prevent this client from reconnecting on connection loss -->
            <property name="clientReconnectDisabled" value="true"/>
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

    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="slowClientQueueLimit" value="1000"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

TcpDiscoverySpi discoverySpi = new TcpDiscoverySpi();
discoverySpi.setClientReconnectDisabled(true);

cfg.setDiscoverySpi(discoverySpi);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

While a client is in a disconnected state and an attempt to reconnect is in progress, the Ignite API throws a `IgniteClientDisconnectedException`.
The exception contains a `future` that represents a re-connection operation.
You can use the `future` to wait until the operation is complete.

{% tabs %}
{% tab title="Java" %}
```java
IgniteCache cache = ignite.getOrCreateCache(new CacheConfiguration<>("myCache"));

try {
    cache.put(1, "value");
} catch (Exception e) {
    if (e.getCause() instanceof IgniteClientDisconnectedException) {
        IgniteClientDisconnectedException cause = (IgniteClientDisconnectedException) e.getCause();

        cause.reconnectFuture().get(); // Wait until the client is reconnected.
        // proceed
    }
}
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Client Disconnected/Reconnected Events

There are two discovery events that are triggered on the client node when it is disconnected from or reconnected to the cluster:

* `EVT_CLIENT_NODE_DISCONNECTED`
* `EVT_CLIENT_NODE_RECONNECTED`

You can listen to these events and execute custom actions in response.
Refer to the [Listening to events](../events/listening-to-events.md) section for a code example.

## Managing Slow Client Nodes

In many deployments, client nodes are launched on slower machines with lower network throughput.
In these scenarios, it is possible that the servers will generate the load (such as continuous queries notification, for example) that the clients cannot handle.
This can result in a growing queue of outbound messages on the servers, which may eventually cause either an out-of-memory situation on the server or block the whole cluster.

To handle these situations, you can configure the maximum number of outgoing messages for client nodes.
If the size of the outbound queue exceeds this value, the client node is disconnected from the cluster.

The examples below show how to configure a slow client queue limit.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="clientMode" value="true"/>

    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="slowClientQueueLimit" value="1000"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
cfg.setClientMode(true);

TcpCommunicationSpi commSpi = new TcpCommunicationSpi();
commSpi.setSlowClientQueueLimit(1000);

cfg.setCommunicationSpi(commSpi);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
