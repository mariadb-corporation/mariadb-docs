---
description: >-
  Use GridGain's event-based auditing to track user actions and export event
  information to an external system.
---

# Auditing

Auditing capabilities of GridGain are based on the event functionality.
All user actions trigger specific events.
The events contain the information about the user and the data that was accessed or modified by the action.
You can track the events and export them into an external system.

You can use an [event listener](../gridgain8-usage/events/listening-to-events.md) to listen to events, or you can create a custom event storage.
On this page, we provide an example of an event storage that outputs information about events to `System.out`.

## Enabling Events

Decide which actions you want to track and [enable the corresponding event types](../gridgain8-usage/events/events.md).
We recommend enabling only the specific events you really need.
Too many events can have an impact on the performance of the cluster.
The events must be enabled on every server node.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="includeEventTypes">
        <list>
            <util:constant static-field="org.apache.ignite.events.EventType.EVT_CACHE_OBJECT_PUT"/>
            <util:constant static-field="org.apache.ignite.events.EventType.EVT_CACHE_OBJECT_REMOVED"/>
        </list>
    </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
cfg.setIncludeEventTypes(
    EventType.EVT_CACHE_OBJECT_PUT,
    EventType.EVT_CACHE_OBJECT_REMOVED);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    IncludedEventTypes = new[]
    {
        EventType.CacheObjectPut,
        EventType.CacheObjectRemoved
    }
};
```
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

## Custom Event Storage

Implement a custom [event storage](../gridgain8-usage/events/listening-to-events.md#storing-and-querying-events) and specify it in the node configuration.
The storage does not have to store events, it can simply output the information to the log or export into an external system.
The implementation will receive all events in the `record()` method.

The following example outputs the information about the event to console.

{% tabs %}
{% tab title="Java" %}
```java
package com.gridgain.snippets;

import java.util.Collection;

import org.apache.ignite.IgniteLogger;
import org.apache.ignite.events.CacheEvent;
import org.apache.ignite.events.Event;
import org.apache.ignite.lang.IgnitePredicate;
import org.apache.ignite.plugin.security.SecuritySubject;
import org.apache.ignite.resources.LoggerResource;
import org.apache.ignite.spi.IgniteSpiAdapter;
import org.apache.ignite.spi.IgniteSpiException;
import org.apache.ignite.spi.IgniteSpiMultipleInstancesSupport;
import org.apache.ignite.spi.eventstorage.EventStorageSpi;

@IgniteSpiMultipleInstancesSupport(true)
public class CustomEventStorage extends IgniteSpiAdapter implements EventStorageSpi {

    public CustomEventStorage() {
    }

    @LoggerResource
    private IgniteLogger log;

    @Override
    public <T extends Event> Collection<T> localEvents(IgnitePredicate<T> p) {
        return null;
    }

    @Override
    public void record(Event evt) throws IgniteSpiException {

        if (evt instanceof CacheEvent) {
            CacheEvent e = (CacheEvent) evt;
            SecuritySubject subj = e.subjectId() != null ? getSpiContext().authenticatedSubject(e.subjectId()) : null;
            System.out.format("user = %s;", subj.login());

        }
        System.out.println("  " + evt.name() + ";");
    }

    @Override
    public void spiStop() throws IgniteSpiException {

    }

    @Override
    public void spiStart(String igniteInstanceName) throws IgniteSpiException {
        
    }
}
```
{% endtab %}

{% tab title="C#/.NET" %}
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

Specify your event storage class in the node configuration.
The storage class must be available in the node's classpath.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="includeEventTypes">
        <list>
            <util:constant static-field="org.apache.ignite.events.EventType.EVT_CACHE_OBJECT_PUT"/>
            <util:constant static-field="org.apache.ignite.events.EventType.EVT_CACHE_OBJECT_REMOVED"/>
        </list>
    </property>

    <property name="eventStorageSpi">
        <!-- Insert the name of your implementation here. -->
        <bean class="com.gridgain.snippets.CustomEventStorage"/>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();
cfg.setEventStorageSpi(new CustomEventStorage());
```
{% endtab %}

{% tab title="C#/.NET" %}
Not supported.
{% endtab %}

{% tab title="C++" %}
Not supported.
{% endtab %}
{% endtabs %}

All nodes started with the above configuration will output the information about the “cache put” and “cache remove” events.

## Identifying the User

If your cluster is protected by [authentication](authentication.md), you can get the user name from the `subjectID` of an event.
Note that `subjectID` may be not available in some events.

The following piece of code illustrates how to obtain the user name:

```java
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

IgniteEvents events = ignite.events();

events.remoteListenAsync(new IgniteBiPredicate<UUID, CacheEvent>() {

    @Override
    public boolean apply(UUID uuid, CacheEvent e) {

        UUID subjectId = e.subjectId();

        if (subjectId != null) {
            // getting the user name
            SecuritySubject subj = gg.security().authenticatedSubject(subjectId);
            System.out.format("User '%s' executed operation %s on cache '%s'\n", subj.login(), e.name(),
                    e.cacheName());
        } else {
            System.out.println(e.toString());
        }
        return true;
    }

}, null, EventType.EVT_CACHE_OBJECT_PUT, EventType.EVT_CACHE_OBJECT_REMOVED);
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
