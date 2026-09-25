---
description: >-
  Configuring TCP/IP-based node discovery in GridGain, including static,
  multicast, JDBC, shared file system, and ZooKeeper IP finders.
---

# TCP/IP Discovery

In a GridGain cluster, nodes can discover each other by using `DiscoverySpi`.
GridGain provides `TcpDiscoverySpi` as a default implementation of `DiscoverySpi` that uses TCP/IP for node discovery.
Discovery SPI can be configured for Multicast and Static IP based node discovery.

## Static IP Finder

Static IP Finder, implemented in `TcpDiscoveryVmIpFinder`, is the default finder option. It allows you
to specify a set of IP addresses and ports that will be checked for node
discovery.

You are only required to provide at least one IP address of a remote
node, but usually it is advisable to provide 2 or 3 addresses of
nodes that you plan to start in the future. Once a
connection to any of the provided IP addresses is established, GridGain
 automatically discovers all other  nodes.

{% hint style="info" %}
Instead of specifying addresses in the configuration, you can specify them in
the `IGNITE_TCP_DISCOVERY_ADDRESSES` environment variable or in the system property
with the same name. Addresses should be comma separated and may optionally contain
a port range.
{% endhint %}

{% hint style="info" %}
By default, the `TcpDiscoveryVmIpFinder` is used in the 'non-shared' mode.
If you plan to start a server node, then in this mode the list of IP addresses should contain the address of the local node as well. In this case, the node will not wait until other nodes join the cluster; instead, it will become the first cluster node and start to operate normally.
{% endhint %}

You can configure the static IP finder via XML configuration or programmatically:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <!--
                              Explicitly specifying address of a local node to let it start and
                              operate normally even if there is no more nodes in the cluster.
                              You can also optionally specify an individual port or port range.
                              -->
                            <value>1.2.3.4</value>
                            <!--
                              IP Address and optional port range of a remote node.
                              You can also optionally specify an individual port.
                              -->
                            <value>1.2.3.5:47500..47509</value>
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
TcpDiscoverySpi spi = new TcpDiscoverySpi();

TcpDiscoveryVmIpFinder ipFinder = new TcpDiscoveryVmIpFinder();

// Set initial IP addresses.
// Note that you can optionally specify a port or a port range.
ipFinder.setAddresses(Arrays.asList("1.2.3.4", "1.2.3.5:47500..47509"));

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start a node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    DiscoverySpi = new TcpDiscoverySpi
    {
        IpFinder = new TcpDiscoveryStaticIpFinder
        {
            Endpoints = new[] {"1.2.3.4", "1.2.3.5:47500..47509" }
        }
    }
};
```
{% endtab %}

{% tab title="Shell" %}
```shell
# The configuration should use TcpDiscoveryVmIpFinder without addresses specified:

IGNITE_TCP_DISCOVERY_ADDRESSES=1.2.3.4,1.2.3.5:47500..47509 bin/ignite.sh -v config/default-config.xml
```
{% endtab %}
{% endtabs %}

## Multicast IP Finder

`TcpDiscoveryMulticastIpFinder` uses Multicast to discover other nodes. Here is an example of how to configure
this finder via a Spring XML file or programmatically:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder">
                    <property name="multicastGroup" value="228.10.10.157"/>
                </bean>
            </property>
        </bean>
    </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
TcpDiscoverySpi spi = new TcpDiscoverySpi();

TcpDiscoveryMulticastIpFinder ipFinder = new TcpDiscoveryMulticastIpFinder();

ipFinder.setMulticastGroup("228.10.10.157");

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start the node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    DiscoverySpi = new TcpDiscoverySpi
    {
        IpFinder = new TcpDiscoveryMulticastIpFinder
        {
            MulticastGroup = "228.10.10.157"
        }
    }
};
Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Multicast and Static IP Finder

You can use both Multicast and Static IP based discovery together. In
this case, in addition to any addresses received via multicast,
`TcpDiscoveryMulticastIpFinder` can also work with a pre-configured list
of static IP addresses, just like Static IP-Based Discovery described
above. Here is an example of how to configure Multicast IP finder with
static IP addresses:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.multicast.TcpDiscoveryMulticastIpFinder">
                    <property name="multicastGroup" value="228.10.10.157"/>
                    <!-- list of static IP addresses-->
                    <property name="addresses">
                        <list>
                            <value>1.2.3.4</value>
                            <!--
                              IP Address and optional port range.
                              You can also optionally specify an individual port.
                             -->
                            <value>1.2.3.5:47500..47509</value>
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
TcpDiscoverySpi spi = new TcpDiscoverySpi();

TcpDiscoveryMulticastIpFinder ipFinder = new TcpDiscoveryMulticastIpFinder();

// Set Multicast group.
ipFinder.setMulticastGroup("228.10.10.157");

// Set initial IP addresses.
// Note that you can optionally specify a port or a port range.
ipFinder.setAddresses(Arrays.asList("1.2.3.4", "1.2.3.5:47500..47509"));

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start a node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    DiscoverySpi = new TcpDiscoverySpi
    {
        IpFinder = new TcpDiscoveryMulticastIpFinder
        {
            MulticastGroup = "228.10.10.157",
            Endpoints = new[] {"1.2.3.4", "1.2.3.5:47500..47509" }
        }
    }
};
Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Isolated GridGain Clusters on Same Set of Machines

GridGain allows you to start two isolated clusters on the same set of
machines. This can be done if nodes from different clusters use non-intersecting local port ranges for `TcpDiscoverySpi` and `TcpCommunicationSpi`.

Let’s say you need to start two isolated clusters on a single machine
for testing purposes. For the nodes from the first cluster, you
should use the following `TcpDiscoverySpi` and `TcpCommunicationSpi`
configurations:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <!--
    Explicitly configure TCP discovery SPI to provide list of
    initial nodes from the first cluster.
    -->
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <!-- Initial local port to listen to. -->
            <property name="localPort" value="48500"/>

            <!-- Changing local port range. This is an optional action. -->
            <property name="localPortRange" value="20"/>

            <!-- Setting up IP finder for this cluster -->
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <!--
                            Addresses and port range of nodes from
                            the first cluster.
                            127.0.0.1 can be replaced with actual IP addresses
                            or host names. Port range is optional.
                            -->
                            <value>127.0.0.1:48500..48520</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>

    <!--
    Explicitly configure TCP communication SPI changing local
    port number for the nodes from the first cluster.
    -->
    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="48100"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration firstCfg = new IgniteConfiguration();

firstCfg.setIgniteInstanceName("first");

// Explicitly configure TCP discovery SPI to provide list of initial nodes
// from the first cluster.
TcpDiscoverySpi firstDiscoverySpi = new TcpDiscoverySpi();

// Initial local port to listen to.
firstDiscoverySpi.setLocalPort(48500);

// Changing local port range. This is an optional action.
firstDiscoverySpi.setLocalPortRange(20);

TcpDiscoveryVmIpFinder firstIpFinder = new TcpDiscoveryVmIpFinder();

// Addresses and port range of the nodes from the first cluster.
// 127.0.0.1 can be replaced with actual IP addresses or host names.
// The port range is optional.
firstIpFinder.setAddresses(Collections.singletonList("127.0.0.1:48500..48520"));

// Overriding IP finder.
firstDiscoverySpi.setIpFinder(firstIpFinder);

// Explicitly configure TCP communication SPI by changing local port number for
// the nodes from the first cluster.
TcpCommunicationSpi firstCommSpi = new TcpCommunicationSpi();

firstCommSpi.setLocalPort(48100);

// Overriding discovery SPI.
firstCfg.setDiscoverySpi(firstDiscoverySpi);

// Overriding communication SPI.
firstCfg.setCommunicationSpi(firstCommSpi);

// Starting a node.
Ignition.start(firstCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var firstCfg = new IgniteConfiguration
{
    IgniteInstanceName = "first",
    DiscoverySpi = new TcpDiscoverySpi
    {
        LocalPort = 48500,
        LocalPortRange = 20,
        IpFinder = new TcpDiscoveryStaticIpFinder
        {
            Endpoints = new[]
            {
                "127.0.0.1:48500..48520"
            }
        }
    },
    CommunicationSpi = new TcpCommunicationSpi
    {
        LocalPort = 48100
    }
};
Ignition.Start(firstCfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

For the nodes from the second cluster, the configuration might look like
this:

{% tabs %}
{% tab title="XML" %}
```xml
<bean id="ignite.cfg" class="org.apache.ignite.configuration.IgniteConfiguration">
    <!--
    Explicitly configure TCP discovery SPI to provide list of initial
    nodes from the second cluster.
    -->
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <!-- Initial local port to listen to. -->
            <property name="localPort" value="49500"/>

            <!-- Changing local port range. This is an optional action. -->
            <property name="localPortRange" value="20"/>

            <!-- Setting up IP finder for this cluster -->
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <!--
                            Addresses and port range of the nodes from the second cluster.
                            127.0.0.1 can be replaced with actual IP addresses or host names. Port range is optional.
                            -->
                            <value>127.0.0.1:49500..49520</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>

    <!--
    Explicitly configure TCP communication SPI changing local port number
    for the nodes from the second cluster.
    -->
    <property name="communicationSpi">
        <bean class="org.apache.ignite.spi.communication.tcp.TcpCommunicationSpi">
            <property name="localPort" value="49100"/>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration secondCfg = new IgniteConfiguration();

secondCfg.setIgniteInstanceName("second");

// Explicitly configure TCP discovery SPI to provide list of initial nodes
// from the second cluster.
TcpDiscoverySpi secondDiscoverySpi = new TcpDiscoverySpi();

// Initial local port to listen to.
secondDiscoverySpi.setLocalPort(49500);

// Changing local port range. This is an optional action.
secondDiscoverySpi.setLocalPortRange(20);

TcpDiscoveryVmIpFinder secondIpFinder = new TcpDiscoveryVmIpFinder();

// Addresses and port range of the nodes from the second cluster.
// 127.0.0.1 can be replaced with actual IP addresses or host names.
// The port range is optional.
secondIpFinder.setAddresses(Collections.singletonList("127.0.0.1:49500..49520"));

// Overriding IP finder.
secondDiscoverySpi.setIpFinder(secondIpFinder);

// Explicitly configure TCP communication SPI by changing local port number for
// the nodes from the second cluster.
TcpCommunicationSpi secondCommSpi = new TcpCommunicationSpi();

secondCommSpi.setLocalPort(49100);

// Overriding discovery SPI.
secondCfg.setDiscoverySpi(secondDiscoverySpi);

// Overriding communication SPI.
secondCfg.setCommunicationSpi(secondCommSpi);

// Starting a node.
Ignition.start(secondCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var secondCfg = new IgniteConfiguration
{
    IgniteInstanceName = "second",
    DiscoverySpi = new TcpDiscoverySpi
    {
        LocalPort = 49500,
        LocalPortRange = 20,
        IpFinder = new TcpDiscoveryStaticIpFinder
        {
            Endpoints = new[]
            {
                "127.0.0.1:49500..49520"
            }
        }
    },
    CommunicationSpi = new TcpCommunicationSpi
    {
        LocalPort = 49100
    }
};
Ignition.Start(secondCfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

As you can see from the configurations, the difference between them is minor — only port numbers for SPIs and IP finder vary.

{% hint style="info" %}
If you want the nodes from different clusters to be able to look for
each other using the multicast protocol, replace
`TcpDiscoveryVmIpFinder` with `TcpDiscoveryMulticastIpFinder` and set
unique `TcpDiscoveryMulticastIpFinder.multicastGroups` in each
configuration above.
{% endhint %}

{% hint style="warning" %}
**Persistence Files Location**

If the isolated clusters use Native Persistence, then every
cluster has to store its persistence files under different paths in the
file system. Refer to the [Native Persistence documentation](../../architecture/storage/native-persistence.md) to learn how you can change persistence related directories.
{% endhint %}

## JDBC-Based IP Finder

{% hint style="info" %}
Not supported in .NET/C#/C++.
{% endhint %}

You can have your database be a common shared storage of initial IP addresses. With this IP finder, nodes will write their IP addresses to a database on startup. This is done via `TcpDiscoveryJdbcIpFinder`.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.jdbc.TcpDiscoveryJdbcIpFinder">
                    <property name="dataSource" ref="ds"/>
                </bean>
            </property>
        </bean>
    </property>

</bean>

<!-- Configured data source instance. -->
<bean id="ds" class="some.Datasource">

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
TcpDiscoverySpi spi = new TcpDiscoverySpi();

// Configure your DataSource.
DataSource someDs = new MySampleDataSource();

TcpDiscoveryJdbcIpFinder ipFinder = new TcpDiscoveryJdbcIpFinder();

ipFinder.setDataSource(someDs);

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start the node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Shared File System IP Finder

{% hint style="info" %}
Not supported in .NET/C#/C++.
{% endhint %}

A shared file system can be used as a storage for nodes' IP addresses. The nodes will write their IP addresses to the file system on startup. This behavior is supported by `TcpDiscoverySharedFsIpFinder`.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.sharedfs.TcpDiscoverySharedFsIpFinder">
                  <property name="path" value="/var/ignite/addresses"/>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
// Configuring discovery SPI.
TcpDiscoverySpi spi = new TcpDiscoverySpi();

// Configuring IP finder.
TcpDiscoverySharedFsIpFinder ipFinder = new TcpDiscoverySharedFsIpFinder();

ipFinder.setPath("/var/ignite/addresses");

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start the node.
Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## ZooKeeper IP Finder

{% hint style="info" %}
Not supported in .NET/C#.
{% endhint %}

To set up ZooKeeper IP finder use `TcpDiscoveryZookeeperIpFinder` (note that `ignite-zookeeper` module has to be enabled).

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.zk.TcpDiscoveryZookeeperIpFinder">
                    <property name="zkConnectionString" value="127.0.0.1:2181"/>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
TcpDiscoverySpi spi = new TcpDiscoverySpi();

TcpDiscoveryZookeeperIpFinder ipFinder = new TcpDiscoveryZookeeperIpFinder();

// Specify ZooKeeper connection string.
ipFinder.setZkConnectionString("127.0.0.1:2181");

spi.setIpFinder(ipFinder);

IgniteConfiguration cfg = new IgniteConfiguration();

// Override default discovery SPI.
cfg.setDiscoverySpi(spi);

// Start the node.
Ignition.start(cfg);
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
