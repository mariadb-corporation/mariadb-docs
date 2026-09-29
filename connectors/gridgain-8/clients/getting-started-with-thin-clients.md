---
description: >-
  Overview of GridGain 8 thin clients: the features each client supports,
  connection failover, partition awareness, authentication, and how to configure
  the thin client connector on the cluster.
---

# Thin Clients Overview

## Overview

A thin client is a lightweight GridGain client that connects to the cluster via a standard socket connection. It does not become a part of the cluster topology, never holds any data, and is not used as a destination for compute calculations. What it does is simply establish a socket connection to a standard GridGain node​ and perform all operations through that node.

Thin clients are based on the [binary client protocol](https://apacheignite.readme.io/docs/binary-client-protocol), which makes it possible to support GridGain connectivity from any programming language.

GridGain provides the following thin clients:

- [Java Thin Client](java-thin-client.md)
- [.NET/C# Thin Client](dotnet-thin-client.md)
- [C++ Thin Client](cpp-thin-client.md)
- [Python Thin Client](python-thin-client.md)
- [Node.js Thin Client](nodejs-thin-client.md)
- [PHP Thin Client](php-thin-client.md)

## Thin Client Features

The following table outlines features supported by each client.

| Thin Client Feature | Java | .NET | C++ | Python | Node.js | PHP |
| --- | --- | --- | --- | --- | --- | --- |
| Scan Query | Yes | Yes | No | Yes | Yes | Yes |
| Scan Query with a filter | Yes | Yes | No | No | No | No |
| SqlQuery | Yes | Yes | No | Yes | Yes | Yes |
| SqlFieldsQuery | Yes | Yes | Yes | Yes | Yes | Yes |
| Binary Object API | Yes | Yes | No | No | Yes | Yes |
| Type name registration | Yes | Yes | No | No | No | No |
| Enum registration | Yes | No | No | No | No | No |
| Async Operations | Yes | Yes | No | Yes | Yes | Yes |
| SSL/TLS | Yes | Yes | Yes | Yes | Yes | Yes |
| Authentication | Yes | Yes | Yes | Yes | Yes | Yes |
| Partition Awareness | Yes | Yes | Yes | Yes | Yes | No |
| Failover | Yes | Yes | Yes | Yes | Yes | Yes |
| Transactions | Yes | Yes | Yes | Yes | No | No |
| Cluster API | Yes | Yes | Yes | No | No | No |
| Compute | Yes | Yes | Yes | No | No | No |
| Continuous Queries | Yes | Yes | Yes | No | No | No |
| Service Invocation | Yes | Yes | No | No | No | No |
| Server Discovery | Yes | Yes | No | No | No | No |
| Server Discovery in Kubernetes | Yes | No | No | No | No | No |
| Data Streaming | No | Yes | No | No | No | No |
| Retry Policy | Yes | Yes | No | No | No | No |
| Entry processor invocation | Yes | No | No | No | No | No |

### Client Connection Failover

All thin clients support a connection failover mechanism, whereby the client automatically switches to an available node in case of the current node or connection failure.
For this mechanism to work, you need to provide a list of node addresses you want to use for failover purposes in the client configuration.
Refer to the specific client documentation for more details.

### Partition Awareness

As explained in the [Data Partitioning](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/data-modeling/data-partitioning) section, data in the cluster is distributed between the nodes in a balanced manner for scalability and performance reasons.
Each cluster node maintains a subset of the data and the partition distribution map, which is used to determine the node that keeps the primary/backup copy of requested entries.

{% include "../.gitbook/includes/gg8-partition-awareness.md" %}

Partition Awareness is available for the Java, .NET, C++, Python, and Node.js thin clients.
Refer to the documentation of the specific client for more information.

### Authentication

All thin clients support authentication in the cluster side. Authentication is [configured in the cluster](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authentication) configuration, and the client simply provide user credentials.
Refer to the documentation of the specific client for more information.

## Cluster Configuration

Thin client connection parameters are controlled by the client connector configuration.
By default, GridGain accepts client connections on port 10800.
You can change the port, connection buffer size and timeout, enable SSL/TLS, etc.

### Configuring Thin Client Connector

The following example shows how to configure thin client connection parameters:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <property name="clientConnectorConfiguration">
        <bean class="org.apache.ignite.configuration.ClientConnectorConfiguration">
            <property name="port" value="10000"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
ClientConnectorConfiguration clientConnectorCfg = new ClientConnectorConfiguration();
// Set a port range from 10000 to 10005
clientConnectorCfg.setPort(10000);
clientConnectorCfg.setPortRange(5);

IgniteConfiguration cfg = new IgniteConfiguration().setClientConnectorConfiguration(clientConnectorCfg);

// Start a node
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    ClientConnectorConfiguration = new ClientConnectorConfiguration
    {
        // Set a port range from 10000 to 10005
        Port = 10000,
        PortRange = 5
    }
};

var ignite = Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

The following table describes some parameters that you may want to change.

| Parameter | Description | Default Value |
| --- | --- | --- |
| `thinClientEnabled` | Enables or disables thin client connectivity. | `true` |
| `port` | The port for thin client connections. | 10800 |
| `portRange` | This parameters sets a range of ports for thin client connections. For example, if `portRange` = 10, thin clients can connect to any port from range 10800–18010. The node tries to bind to each port from the range starting from the `port` until it finds an available one. If all ports are unavailable, the node won't start. | 100 |
| `sslEnabled` | Set this property to `true` to enable SSL for thin client connections. | `false` |
| `sessionOutboundMessageQueueLimit` | Limits the number of outbound messages the server queues for a single client connection while they wait to be sent. If the limit is exceeded, GridGain closes that client's connection, protecting the server from unbounded memory growth caused by a slow or unresponsive client. `0` means no limit is applied. | `0` |

See the complete list of parameters in the [ClientConnectorConfiguration](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/configuration/ClientConnectorConfiguration.html) javadoc.

{% hint style="info" %}
In addition to the node-level connector parameters above, you can cap the number of active thin client, ODBC, and thin JDBC connections per node cluster-wide using the [`thinClientProperty.maxConnectionsPerNode`](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/control-script#cluster-properties) cluster property. This limit is set at runtime through the control script and applies to every server in the cluster.
{% endhint %}

### Enabling SSL/TLS for Thin Clients

Refer to the [SSL for Thin Clients and JDBC/ODBC](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/ssl-tls#ssl-for-clients) section.

## Distributed Computing on Thin Clients

Distributed computing on thin clients has a number of limitations:

- The [ClientCompute API](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/client/ClientCompute.html) can only be used to execute existing tasks by class name;
- [Peer class loading](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/peer-class-loading) is not available.
