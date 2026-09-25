---
description: >-
  How to enable, listen to, and query local and remote events in GridGain,
  including batching and event storage configuration.
---

# Working with Events

## Overview

GridGain can generate events for a variety of operations happening in the cluster and notify your application about those operations. There are many types of events, including cache events, node discovery events, distributed task execution events, and many more.

The list of events is available in the [Events](events.md) section.

## Enabling Events

By default, events are disabled, and you have to enable each event type explicitly if you want to use it in your application.
To enable specific event types, list them in the `includeEventTypes` property of `IgniteConfiguration` as shown below:

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
                <util:constant static-field="org.apache.ignite.events.EventType.EVT_CACHE_OBJECT_PUT"/>
                <util:constant static-field="org.apache.ignite.events.EventType.EVT_CACHE_OBJECT_READ"/>
                <util:constant static-field="org.apache.ignite.events.EventType.EVT_CACHE_OBJECT_REMOVED"/>
                <util:constant static-field="org.apache.ignite.events.EventType.EVT_NODE_LEFT"/>
                <util:constant static-field="org.apache.ignite.events.EventType.EVT_NODE_JOINED"/>
            </list>
        </property>
    </bean>

</beans>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

// Enable cache events.
cfg.setIncludeEventTypes(EventType.EVT_CACHE_OBJECT_PUT, EventType.EVT_CACHE_OBJECT_READ,
        EventType.EVT_CACHE_OBJECT_REMOVED, EventType.EVT_NODE_JOINED, EventType.EVT_NODE_LEFT);

// Start a node.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    IncludedEventTypes = new[]
    {
        EventType.CacheObjectPut,
        EventType.CacheObjectRead,
        EventType.CacheObjectRemoved,
        EventType.NodeJoined,
        EventType.NodeLeft
    }
};
var ignite = Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Getting the Events Interface

The events functionality is available through the events interface, which provides methods for listening to cluster events. The events interface can be obtained from an instance of `Ignite` as follows:

{% tabs %}
{% tab title="Java" %}
```java
IgniteEvents events = ignite.events();
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.GetIgnite();
var events = ignite.GetEvents();
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The events interface can be associated with a [set of nodes](../distributed-computing/cluster-groups.md). This means that you can access events that happen on a given set of nodes. In the following example, the events interface is obtained for the set of nodes that host the data for the Person cache.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();

IgniteEvents events = ignite.events(ignite.cluster().forCacheNodes("person"));
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.GetIgnite();
var events = ignite.GetCluster().ForCacheNodes("person").GetEvents();
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Listening to Events

You can listen to either local or remote events. Local events are events that are generated on the node where the listener is registered. Remote events are events that happen on other nodes.

Note that some events may be fired on multiple nodes even if the corresponding real-world event happens only once. For example, when a node leaves the cluster, the `EVT_NODE_LEFT` event is generated on every remaining node.

Another example is when you put an object into a cache. In this case, the `EVT_CACHE_OBJECT_PUT` event occurs on the node that hosts the [primary partition](../../architecture/data-modeling/data-partitioning.md#backup-partitions) into which the object is actually written, which may be different from the node where the `put(...)` method is called. In addition, the event is fired on all nodes that hold the [backup partitions](../../architecture/data-modeling/data-partitioning.md#backup-partitions) for the cache if they are configured.

The events interface provides methods for listening to local events only, and for listening to both local and remote events.

### Listening to Local Events

To listen to local events, use the  `localListen(listener, eventTypes...)` method, as shown below. The method accepts an event listener that is called every time an event of the given type occurs on the local node.

To unregister the local listener, return `false` in its functional method.

{% tabs %}
{% tab title="Java" %}
```java
IgniteEvents events = ignite.events();

// Local listener that listens to local events.
IgnitePredicate<CacheEvent> localListener = evt -> {
    System.out.println("Received event [evt=" + evt.name() + ", key=" + evt.key() + ", oldVal=" + evt.oldValue()
            + ", newVal=" + evt.newValue());

    return true; // Continue listening.
};

// Subscribe to specified cache events occurring on the local node.
events.localListen(localListener, EventType.EVT_CACHE_OBJECT_PUT, EventType.EVT_CACHE_OBJECT_READ,
        EventType.EVT_CACHE_OBJECT_REMOVED);
```

The event listener is an object of the `IgnitePredicate<T>` class with a type argument that matches the type of events the listener is going to process.
For example, cache events (`EVT_CACHE_OBJECT_PUT`, `EVT_CACHE_OBJECT_READ`, etc.) correspond to the `CacheEvent` class, discovery events (`EVT_NODE_LEFT`, `EVT_NODE_JOINED`, etc.) correspond to
the `DiscoveryEvent` class, and so on.
If you want to listen to events of different types, you can use the generic `Event` interface:

```java
IgnitePredicate<Event> localListener = evt -> {
    // process the event
    return true;
};
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
class LocalListener : IEventListener<CacheEvent>
{
    public bool Invoke(CacheEvent evt)
    {
        Console.WriteLine("Received event [evt=" + evt.Name + ", key=" + evt.Key + ", oldVal=" + evt.OldValue
                          + ", newVal=" + evt.NewValue);
        return true;
    }
}

public static void LocalListenDemo()
{
    var cfg = new IgniteConfiguration
    {
        IncludedEventTypes = new[]
        {
            EventType.CacheObjectPut,
            EventType.CacheObjectRead,
            EventType.CacheObjectRemoved,
        }
    };
    var ignite = Ignition.Start(cfg);
    var events = ignite.GetEvents();
    events.LocalListen(new LocalListener(), EventType.CacheObjectPut, EventType.CacheObjectRead,
        EventType.CacheObjectRemoved);

    var cache = ignite.GetOrCreateCache<int, int>("myCache");
    cache.Put(1, 1);
    cache.Put(2, 2);
}
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Listening to Remote Events

The `IgniteEvents.remoteListen(localListener, filter, types)` method can be used to register a listener that listens for both remote and local events.
It accepts a local listener, a filter, and a list of event types you want to listen to.

The filter is deployed to all the nodes associated with the events interface, including the local node. The events that pass the filter are sent to the local listener.

The method returns a unique identifier that can be used to unregister the listener and filters. To do this, call `IgniteEvents.stopRemoteListen(uuid)`. Another way to unregister the listener is to return `false` in the `apply()` method.

{% tabs %}
{% tab title="Java" %}
```java
IgniteEvents events = ignite.events();

IgnitePredicate<CacheEvent> filter = evt -> {
    System.out.println("remote event: " + evt.name());
    return true;
};

// Subscribe to specified cache events on all nodes that have cache running.
UUID uuid = events.remoteListen(new IgniteBiPredicate<UUID, CacheEvent>() {

    @Override
    public boolean apply(UUID uuid, CacheEvent e) {

        // process the event

        return true; //continue listening
    }
}, filter, EventType.EVT_CACHE_OBJECT_PUT);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Batching Events

Each activity in a cache can result in an event notification being generated and sent. For systems with high cache activity, getting notified for every event could be network intensive, possibly leading to a decreased performance of cache operations.

Event notifications can be grouped together and sent in batches or timely intervals to mitigate the impact on performance. Here is an example of how this can be done:

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.ignite();

// Get an instance of named cache.
final IgniteCache<Integer, String> cache = ignite.cache("cacheName");

// Sample remote filter which only accepts events for keys
// that are greater than or equal to 10.
IgnitePredicate<CacheEvent> rmtLsnr = new IgnitePredicate<CacheEvent>() {
    @Override
    public boolean apply(CacheEvent evt) {
        System.out.println("Cache event: " + evt);

        int key = evt.key();

        return key >= 10;
    }
};

// Subscribe to cache events occurring on all nodes
// that have the specified cache running.
// Send notifications in batches of 10.
ignite.events(ignite.cluster().forCacheNodes("cacheName")).remoteListen(10 /* batch size */,
        0 /* time intervals */, false, null, rmtLsnr, EventType.EVTS_CACHE);

// Generate cache events.
for (int i = 0; i < 20; i++)
    cache.put(i, Integer.toString(i));

```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Storing and Querying Events

You can configure an event storage that will keep events on the nodes where they occur. You can then query events in your application.

The event storage can be configured to keep events for a specific period, keep only the most recent events, or keep the events that satisfy a specific filter. See the `MemoryEventStorageSpi` javadoc for details.

Below is an example of event storage configuration:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="eventStorageSpi" >
        <bean class="org.apache.ignite.spi.eventstorage.memory.MemoryEventStorageSpi">
            <property name="expireAgeMs" value="600000"/>
        </bean>
    </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
MemoryEventStorageSpi eventStorageSpi = new MemoryEventStorageSpi();
eventStorageSpi.setExpireAgeMs(600000);

IgniteConfiguration igniteCfg = new IgniteConfiguration();
igniteCfg.setEventStorageSpi(eventStorageSpi);

Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    EventStorageSpi = new MemoryEventStorageSpi()
    {
        ExpirationTimeout = TimeSpan.FromMilliseconds(600000)
    },
    IncludedEventTypes = new[]
    {
        EventType.CacheObjectPut,
        EventType.CacheObjectRead,
        EventType.CacheObjectRemoved,
    }
};
var ignite = Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Querying Local Events

The following example shows how you can query local `EVT_CACHE_OBJECT_PUT` events stored in the event storage.

{% tabs %}
{% tab title="Java" %}
```java
Collection<CacheEvent> cacheEvents = events.localQuery(e -> {
    // process the event
    return true;
}, EventType.EVT_CACHE_OBJECT_PUT);

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var events = ignite.GetEvents();
var cacheEvents = events.LocalQuery(EventType.CacheObjectPut);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Querying Remote Events

Here is an example of querying remote events:

{% tabs %}
{% tab title="Java" %}
```java
Collection<CacheEvent> storedEvents = events.remoteQuery(e -> {
    // process the event
    return true;
}, 0, EventType.EVT_CACHE_OBJECT_PUT);

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
class EventFilter : IEventFilter<CacheEvent>
{
    public bool Invoke(CacheEvent evt)
    {
        return true;
    }
}
// ....

    var events = ignite.GetEvents();
    var storedEvents = events.RemoteQuery(new EventFilter(), null, EventType.CacheObjectPut);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
