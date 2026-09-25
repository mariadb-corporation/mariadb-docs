---
description: >-
  Controlling how GridGain distributes cache partitions across nodes using node
  filters, attribute-based filters, and backup filters.
---

# Managing Data Distribution

The partitions of each cache are distributed across all server nodes in accordance with the affinity function implementation.
You can prevent specific nodes from hosting the partitions of a given cache by defining a _node filter_ in the cache configuration.

In addition to node filters, you can control the way backup copies of the partitions are distributed.

## Node Filter

A node filter allows you to deploy a cache to a subset of server nodes instead of all server nodes (which is the default behavior).
It "filters out" the nodes that you don't want to use.
The node filter can be based on user attributes or node's consistent ID.
If the filter returns `true` for a given node, the cache is deployed on the node.
Otherwise, the node is excluded.

To create a node filter, implement `IgnitePredicate<ClusterNode>` and provide it in the cache configuration.
Here is an example of a node filter that filters out the nodes with specific consistent IDs.

{% tabs %}
{% tab title="Java" %}
```java
public class MyNodeFilter implements IgnitePredicate<ClusterNode> {

    // fill the collection with consistent IDs of the nodes you want to exclude
    private Collection<String> nodesToExclude;

    public MyNodeFilter(Collection<String> nodesToExclude) {
        this.nodesToExclude = nodesToExclude;
    }

    @Override
    public boolean apply(ClusterNode node) {
        return nodesToExclude == null || !nodesToExclude.contains(node.consistentId());
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

{% hint style="warning" %}
The class of the node filter must be present in the classpath of all nodes.
{% endhint %}

When you create a cache with the node filter defined above, the cache is deployed on the set of nodes that are _not_ provided in the node filter's constructor parameter.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="myCache"/>
            <property name="nodeFilter">
                <bean class="com.gridgain.snippets.MyNodeFilter">
                    <constructor-arg>
                        <set>
                           <value>consistentId1</value> 
                        </set>
                    </constructor-arg>
                </bean>
            </property>
        </bean>
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
Ignite ignite = Ignition.start();

CacheConfiguration<Integer, String> cacheCfg = new CacheConfiguration<>("myCache");
		
Collection<String> consistenIdSet = new HashSet<>();
consistenIdSet.add("consistentId1");

//the cache will not be hosted on the provided nodes
cacheCfg.setNodeFilter(new MyNodeFilter(consistenIdSet));

ignite.createCache(cacheCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Filtering Nodes by Attributes

`AttributeNodeFilter` is an implementation of `IgnitePredicate<ClusterNode>` that uses user attributes to filter nodes and can be used as a node filter.
The filter checks if a node contains the given attributes with the given values.

The following snippet is an example of using `AttributeNodeFilter` as a node filter for cache deployment. In the example, a cache named "myCache" is deployed on the nodes where the "host_myCache" attribute is set to `true`.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="userAttributes">
        <map>
            <entry key="host_myCache" value="true"/>
        </map>
    </property>
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="myCache"/>
            <property name="nodeFilter">
                <bean class="org.apache.ignite.util.AttributeNodeFilter">
                    <constructor-arg value="host_myCache"/>
                    <constructor-arg value="true"/>
                </bean>
            </property>
        </bean>
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
CacheConfiguration<Integer, String> cacheCfg = new CacheConfiguration<>("myCache");

cacheCfg.setNodeFilter(new AttributeNodeFilter("host_myCache", "true"));
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Add the attribute on the nodes where you want to deploy the cache.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="userAttributes">
        <map>
            <entry key="host_myCache" value="true"/>
        </map>
    </property>
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="myCache"/>
            <property name="nodeFilter">
                <bean class="org.apache.ignite.util.AttributeNodeFilter">
                    <constructor-arg value="host_myCache"/>
                    <constructor-arg value="true"/>
                </bean>
            </property>
        </bean>
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
Map<String, Object> attributes = new HashMap<String, Object>();
attributes.put("host_myCache", true);
cfg.setUserAttributes(attributes);

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

Note that attributes can also be set via environment variables.

## Backup Filter

A backup filter allows you to control how backup copies of the partitions are distributed between the nodes.
The backup filter is set via the [RendezvousAffinityFunction.setAffinityBackupFilter(IgniteBiPredicate<ClusterNode,List<ClusterNode>> affinityBackupFilter)](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/cache/affinity/rendezvous/RendezvousAffinityFunction.html#setAffinityBackupFilter-org.apache.ignite.lang.IgniteBiPredicate-) method.
A given partition is assigned to the first node that passes the filter.
The filter is invoked every time GridGain calculates partition distribution (which happens every time the cluster topology changes).

{% hint style="warning" %}
The backup filter is used when `RendezvousAffinityFunction.excludeNeighbors = false`.
{% endhint %}

As an example, let's consider an implementation of the backup filter that uses node attributes to decide to which node a backup copy should be assigned.
The `ClusterNodeAttributeAffinityBackupFilter` class provides such an implementation: the primary and backup partitions are assigned to the nodes with different values of a given attribute or environment variable.

The following code snippet defines a backup filter that is based on the values of the `AVAILABILITY_ZONE` attribute.
With this configuration, the primary and backup copies of each partition end up in different availability zones (provided the attribute is set correctly).

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="userAttributes">
        <map>
            <entry key="AVAILABILITY_ZONE" value="us-east-1a"/>
        </map>
    </property>
    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="myCache"/>
            <property name="backups" value="1"/>
            <property name="affinity">
                <bean class="org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction">
                    <property name="affinityBackupFilter">
                        <bean class="org.apache.ignite.cache.affinity.rendezvous.ClusterNodeAttributeAffinityBackupFilter">
                            <constructor-arg>
                                <array value-type="java.lang.String">
                                    <!-- Backups must go to different availability zones -->
                                    <value>AVAILABILITY_ZONE</value>
                                </array>
                            </constructor-arg>
                        </bean>
                    </property>
                </bean>
            </property>
        </bean>
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
CacheConfiguration<Integer, String> cacheCfg = new CacheConfiguration<Integer, String>("myCache");

cacheCfg.setBackups(1);
RendezvousAffinityFunction af = new RendezvousAffinityFunction();
af.setAffinityBackupFilter(new ClusterNodeAttributeAffinityBackupFilter("AVAILABILITY_ZONE"));

cacheCfg.setAffinity(af);
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
