---
description: >-
  Use GridGain conflict resolution with GoldenGate updates: keep the old value, accept the new one, or merge them. Includes cache and data streamer examples.
---

# GoldenGate Conflicts Resolution

When the cache is updated via the GoldenGate and GridGain cache API, you can choose to proceed with the update, retain the old value, or generate some other value by merging old and new values. To achieve this, GridGain offers [Conflicts Resolution](../../gridgain8-management/conflict-resolution.md).

For using conflicts resolution for cache operations and `Data Streamer`, you need to use the `GridGain.cache(String cacheName, byte dataCenterId)` and `GridGain.dataStreamer(String cacheName, byte dataCenterId)` methods. It is expected that the data center ID will be unique for all topologies participating in data center replication, and same for all nodes that belong to the given topology.

{% tabs %}
{% tab title="Cache" %}
```java
// Get GridGain plugin.
GridGain gridGain = ignite.plugin(GridGain.PLUGIN_NAME);

// Get "Person" cache with given data center id.
IgniteCache cache = gridGain.cache("Person", 31);

...

/**
 * Conflict resolver for Person entity. In conflicts always used an entry
 * with data center id equals 31.
 */
public class PersonConflictResolver implements CacheConflictResolver<Integer, Person> {
    /** {@inheritDoc} */
    @Override public void resolve(CacheConflictContext<Integer, Person> ctx) {
        // If we
        if (oldEntry.dataCenterId() == 31)
            ctx.useOld();
        else if (newEntry.dataCenterId() == 31)
            ctx.useNew();
    }
}
```
{% endtab %}

{% tab title="Data Streamer" %}
```java
// Get GridGain plugin.
GridGain gridGain = ignite.plugin(GridGain.PLUGIN_NAME);

// Get Data Streamer for cache with given data center id.
IgniteDataStreamer cache = gridGain.dataStreamer("Person", 31);

...

/**
 * Conflict resolver for Person entity. In conflicts always used an entry
 * with data center id equals 31.
 */
public class PersonConflictResolver implements CacheConflictResolver<Integer, Person> {
    /** {@inheritDoc} */
    @Override public void resolve(CacheConflictContext<Integer, Person> ctx) {
        // If we
        if (oldEntry.dataCenterId() == 31)
            ctx.useOld();
        else if (newEntry.dataCenterId() == 31)
            ctx.useNew();
    }
}
```
{% endtab %}
{% endtabs %}
