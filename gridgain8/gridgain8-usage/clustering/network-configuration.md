---
description: >-
  Configuring the GridGain discovery and communication SPIs, including IPv4/IPv6,
  port settings, connection timeouts, and internal address resolution.
---

# Network Configuration

## IPv4 vs IPv6

GridGain tries to support IPv4 and IPv6 but this can sometimes lead to issues where the cluster becomes detached. A possible solution — unless you require IPv6 — is to restrict GridGain to IPv4 by setting the `-Djava.net.preferIPv4Stack=true` JVM parameter.

## Discovery

This section describes the network parameters of the default discovery mechanism, which uses the TCP/IP protocol to exchange discovery messages and is implemented in the `TcpDiscoverySpi` class.

You can change the properties of the discovery mechanism as follows:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="failureDetectionTimeout" value="5000"/>

    <property name="clientFailureDetectionTimeout" value="10000"/>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="localPort" value="8300"/>  
        </bean>
    </property>

    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="4321"/> 
        </bean>
    </property>

</bean>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="localPort" value="8300"/>  
        </bean>
    </property>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

TcpDiscoverySpi discoverySpi = new TcpDiscoverySpi().setLocalPort(8300);

cfg.setDiscoverySpi(discoverySpi);
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The following table describes some most important properties of `TcpDiscoverySpi`.
You can find the complete list of properties in the `TcpDiscoverySpi` javadoc.

| Property | Description | Default Value |
|---|---|---|
| `localAddress` | Local host IP address used for discovery. | By default, the node uses the first non-loopback address it finds. If there is no non-loopback address available, then `java.net.InetAddress.getLocalHost()` is used. |
| `networkInterfacesBlacklist` | **EXPERIMENTAL** The list of network interfaces that should not be used as a connection target by other nodes when a local address represents a wildcard. Wildcard symbol `*` represents a range of values between `0` and `255`. For example, `12.12.12.*` refers to addresses from `12.12.12.0` to `12.12.12.255`. The range symbol `-` represents a range of values. For example, `12.12.12.12-24` refers to addresses from `12.12.12.12` to `12.12.12.24`. Only active if the `localAddress` property is not set or is `0.0.0.0`. | Empty by default. |
| `localPort` | The port that the node binds to. If set to a non-default value, other cluster nodes must know this port to be able to discover the node. | `47500` |
| `localPortRange` | If the `localPort` is busy, the node attempts to bind to the next port (incremented by 1) and continues this process until it finds a free port. The `localPortRange` property defines the number of ports the node will try (starting from `localPort`). | `100` |
| `reconnectCount` | The number of times the node tries to (re)establish connection to another node. | `10` |
| `networkTimeout` | The maximum network timeout in milliseconds for network operations. | `5000` |
| `socketTimeout` | The socket operations timeout. This timeout is used to limit connection time and write-to-socket time. | `5000` |
| `ackTimeout` | The acknowledgement timeout for discovery messages. If an acknowledgement is not received within this timeout, the discovery SPI tries to resend the message. | `5000` |
| `joinTimeout` | The join timeout defines how much time the node waits to join a cluster. If a non-shared IP finder is used and the node fails to connect to any address from the IP finder, the node keeps trying to join within this timeout. If all addresses are unresponsive, an exception is thrown and the node terminates. `0` means waiting indefinitely. | `0` |
| `statisticsPrintFrequency` | Defines how often the node prints discovery statistics to the log. `0` indicates no printing. If the value is greater than 0, and quiet mode is disabled, then statistics is printed out at INFO level once every period. | `0` |

## Communication

After the nodes discover each other and the cluster is formed, the nodes exchange messages via the communication SPI.
The messages represent distributed cluster operations, such as task execution, data modification operations, queries, etc.
The default implementation of the communication SPI uses the TCP/IP protocol to exchange messages (`TcpCommunicationSpi`).
This section describes the properties of `TcpCommunicationSpi`.

Each node opens a local communication port and address to which other nodes connect and send messages.
At startup, the node tries to bind to the specified communication port (default is 47100).
If the port is already used, the node increments the port number until it finds a free port.
The number of attempts is defined by the `localPortRange` property (defaults to 100).

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="failureDetectionTimeout" value="5000"/>

    <property name="clientFailureDetectionTimeout" value="10000"/>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="localPort" value="8300"/>  
        </bean>
    </property>

    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="4321"/> 
        </bean>
    </property>

</bean>

    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="4321"/> 
        </bean>
    </property>
```
{% endtab %}

{% tab title="Java" %}
```java
TcpCommunicationSpi commSpi = new TcpCommunicationSpi();

// Override local port.
commSpi.setLocalPort(4321);

IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setCommunicationSpi(commSpi);

// Start the node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
 var cfg = new IgniteConfiguration
 {
     CommunicationSpi = new TcpCommunicationSpi
     {
         LocalPort = 1234
     }
 };
Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Below is a list of some important properties of `TcpCommunicationSpi`.
You can find the list of all properties in the `TcpCommunicationSpi` javadoc.

| Property | Description | Default Value |
|---|---|---|
| `localAddress` | The local address for the communication SPI to bind to. |  |
| `localPort` | The local port that the node uses for communication. | `47100` |
| `localPortRange` | The range of ports the nodes tries to bind to sequentially until it finds a free one. | `100` |
| `tcpNoDelay` | Sets the value for the `TCP_NODELAY` socket option. Each socket accepted or created will use the provided value.<br><br>The option should be set to `true` (default) to reduce request/response time during communication over TCP. In most cases we do not recommend changing this option. | `true` |
| `idleConnectionTimeout` | The maximum idle connection timeout (in milliseconds) after which the connection is closed. | `600000` |
| `usePairedConnections` | Whether dual socket connection between the nodes should be enforced. If set to `true`, two separate connections will be established between the communicating nodes: one for outgoing messages, and one for incoming messages. When set to `false`, a single TCP connection will be used for both directions. This flag is useful on some operating systems when messages take too long to be delivered. | `false` |
| `directBuffer` | A boolean flag that indicates whether to allocate NIO direct buffer instead of NIO heap allocation buffer. Although direct buffers perform better, in some cases (especially on Windows) they may cause JVM crashes. If that happens in your environment, set this property to `false`. | `true` |
| `directSendBuffer` | Whether to use NIO direct buffer instead of NIO heap allocation buffer when sending messages. | `false` |
| `socketReceiveBuffer` | Receive buffer size for sockets created or accepted by the communication SPI. If set to `0`, the operating system's default value is used. | `0` |
| `socketSendBuffer` | Send buffer size for sockets created or accepted by the communication SPI. If set to `0` the operating system's default value is used. | `0` |

## Connection Timeouts

There are several properties that define connection timeouts:

| Property | Description | Default Value |
|---|---|---|
| `IgniteConfiguration.failureDetectionTimeout` | A timeout for basic network operations for server nodes. | `10000` |
| `IgniteConfiguration.clientFailureDetectionTimeout` | A timeout for basic network operations for client nodes. | `30000` |

You can set the failure detection timeout in the node configuration as shown in the example below.
The default values allow the discovery SPI to work reliably on most on-premise and containerized deployments.
However, in stable low-latency networks, you can set the parameter to ~200 milliseconds in order to detect and react to failures more quickly.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="failureDetectionTimeout" value="5000"/>

    <property name="clientFailureDetectionTimeout" value="10000"/>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="localPort" value="8300"/>  
        </bean>
    </property>

    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="4321"/> 
        </bean>
    </property>

</bean>

    <property name="failureDetectionTimeout" value="5000"/>

    <property name="clientFailureDetectionTimeout" value="10000"/>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setFailureDetectionTimeout(5_000);

cfg.setClientFailureDetectionTimeout(10_000);
```
{% endtab %}

{% tab title="C#/.NET" %}
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Internal Address Resolution

When running in an internal network, you need to map internal addresses to external ones. You can do this by using an `addressResolver` and providing mapping of internal IP addresses to external ones. Internal addresses are used for communication among the cluster nodes, while the clients in the external network use the external ones to connect to server nodes.

The example below shows how you can create a configuration with mapping:

{% tabs %}
{% tab title="XML" %}
```xml
<property name="addressResolver">
  <bean class="org.apache.ignite.configuration.BasicAddressResolver">
    <constructor-arg>
      <map>
        <entry key="10.0.0.1" value="192.0.2.0"/>
        <entry key="10.0.0.2" value="192.0.2.1"/>
      </map>
    </constructor-arg>
  </bean>
</property>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

Map<String, String> addressMap = new HashMap<>();
addressMap.put("10.0.0.1", "192.0.2.0");
addressMap.put("10.0.0.2", "192.0.2.1");

BasicAddressResolver addressResolver = new BasicAddressResolver(addressMap);

cfg.setAddressResolver(addressResolver);
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
