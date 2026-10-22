---
description: >-
  Diagnose and fix a hot partition on GridGain 8. Three-step procedure identifies the partition, its owner, and the skew pattern.
---

# How to Debug a Hot Partition

<!-- TODO (not tested): The sample numbers on this page was not run against GridGain 8.10. Run it on an 8.10 build, compare the output and samples with the page, fix differences, then delete this comment. -->

## Prerequisites

- **Familiarity with partitioned caches and affinity.** [Understand How Your Cache Is Distributed](../gridgain8-tutorials/cache-centric-foundations/understand-cache-distribution.md) covers partitions and owners. [Design Keys for Colocation](../gridgain8-tutorials/data-locality/design-keys-for-colocation.md) covers the three affinity mechanisms.
- **Thick-client access to the running cluster.** The diagnostic procedure broadcasts a callable to every server, which the thin client cannot do.
- **Monitoring that named the symptom.** CPU or heap pressure on one node while peers idle, or an alert from your observability stack.

## Overview

This guide walks through diagnosing a hot partition on GridGain 8, then applying the fix that matches the cause. By the end, you have the partition ID, the owning node, the skew pattern from a key sample, and a chosen fix from the six options below. The procedure uses thick-client APIs only: `SYS.PARTITION_STATES`, `IgniteCompute.broadcast`, `Affinity.primaryPartitions`, and a local `ScanQuery`.

## Symptoms: When to use This Guide

Use this guide when your monitoring shows:

- One node's CPU is pegged while peers sit idle, even though primary partitions are spread across all nodes.
- Latency spikes concentrate on specific keys or on reads against one cache.
- A rebalance after a scale-up event did not even out the load.
- A partitioned cache shows a memory footprint on one node that is many times the per-node average.

If the symptom is traffic concentrated on a **single key** (rather than a partition full of many keys), that is a hot-key problem, not a hot-partition problem. The fixes in this guide do not help. For a read-heavy hot key, a client-side near cache absorbs the repeated reads. Otherwise, application-level caching is usually the right answer.

## Diagnose the Hot Partition

Run the three steps in order. Each step has a stop condition. If a step's output does not match the description, do not continue to the next step.

### Step 1: Rule out Rebalance State

Query `SYS.PARTITION_STATES` grouped by node, filtered to primary partitions. Each node should own roughly the same count.

```java
// SYS.PARTITION_STATES is one row per partition per owner. Filtering to
// IS_PRIMARY = TRUE collapses to one row per partition (the primary).
// Grouping by NODE_ID gives the count of primary partitions each node
// is responsible for. A balanced cluster produces roughly equal counts.
// Uneven counts indicate an in-flight rebalance or a skewed node filter.
SqlFieldsQuery qry = new SqlFieldsQuery(
    "SELECT NODE_ID, COUNT(*) FROM SYS.PARTITION_STATES " +
    "WHERE CACHE_GROUP_ID = ? AND IS_PRIMARY = TRUE " +
    "GROUP BY NODE_ID ORDER BY NODE_ID"
).setArgs(cacheGroupId);

// SYS.* is schema-wide. The query can run from any SQL-enabled cache,
// not only the hot cache.
try (QueryCursor<List<?>> cur = ignite.cache(cacheName).query(qry)) {
    for (List<?> row : cur) {
        System.out.println(row.get(0) + " -> " + row.get(1) + " primary partitions");
    }
}
```

With 1024 partitions and 3 nodes, expect counts near 341, 341, 342. If the counts are uneven by more than a handful, the issue is rebalance state, a node filter on the affinity function, or an in-flight scale event. Stop. Let rebalance finish, or fix the topology, then re-check. Only continue to Step 2 when per-node primary counts are even.

### Step 2: Find the Hot Partition and Its Owner

Broadcast a callable to every server. On each server, read the primary partitions owned by that server, call `localSizeLong` on each, and return a list of `(partitionId, entryCount)` pairs. Aggregate on the client.

```java
public class HotPartitionCallable implements IgniteCallable<List<long[]>> {

    // @IgniteInstanceResource injects the running server's local GridGain
    // instance into this field, so the callable reaches the local
    // affinity and cache APIs without constructing a new client.
    // The field is transient so closure serialization skips it.
    @IgniteInstanceResource
    private transient Ignite ignite;

    private final String cacheName;

    public HotPartitionCallable(String cacheName) {
        this.cacheName = cacheName;
    }

    @Override
    public List<long[]> call() {
        // broadcast() sends one copy of the callable to every server.
        // localNode() on each server returns that server, so every copy
        // reports partitions for a different node.
        ClusterNode local = ignite.cluster().localNode();

        // primaryPartitions(local) returns the int[] of partition IDs
        // this node owns as primary. The Affinity API reads the
        // client-side topology cache, so no network round-trip.
        Affinity<?> aff = ignite.affinity(cacheName);
        IgniteCache<?, ?> cache = ignite.cache(cacheName);

        List<long[]> rows = new ArrayList<>();
        for (int p : aff.primaryPartitions(local)) {
            // CachePeekMode.PRIMARY counts only primary-owned entries.
            // Without it, a backup copy on the same node doubles the count.
            long size = cache.localSizeLong(p, CachePeekMode.PRIMARY);
            rows.add(new long[] { p, size });
        }
        return rows;
    }
}
```

Call it and print the distribution:

```java
// broadcast() returns one List<long[]> per server. The outer collection
// preserves which server produced which list, so the owner of any
// partition can be recovered from the same result.
Collection<List<long[]>> perNode = ignite.compute().broadcast(new HotPartitionCallable(cacheName));

// A healthy distribution produces max / mean near 1.0. A hot partition
// shows max / mean in the tens or hundreds.
long total = 0;
int partitionCount = 0;
long max = 0;
int hotPartition = -1;
for (List<long[]> node : perNode) {
    for (long[] row : node) {
        total += row[1];
        partitionCount++;
        // Track the single hottest partition. Ties resolve to whichever
        // partition iterated first. The fix is the same either way.
        if (row[1] > max) {
            max = row[1];
            hotPartition = (int) row[0];
        }
    }
}

// partitionCount equals the total number of primary partitions in
// the cache (sum of per-node primary counts). With 1024 partitions
// and even balance, that is 1024 regardless of node count.
double mean = (double) total / partitionCount;
System.out.printf("mean=%.0f max=%d hottest=partition %d (%.1fx mean)%n",
    mean, max, hotPartition, max / mean);
```

A healthy cache shows `max` within a small multiple of the mean. A hot partition stands out by one or two orders of magnitude. Record the partition ID (`hotPartition`) and, from the broadcast result, the node whose callable produced that row. That node is the primary owner.

### Step 3: Sample Keys From the hot Partition

Before sampling, identify which field drives placement. Read the cache's key configuration, or check the key class for `@AffinityKeyMapped`.

```java
CacheConfiguration<?, ?> cfg = cache.getConfiguration(CacheConfiguration.class);

// Each CacheKeyConfiguration entry names a key type and the field
// within that type that drives partition placement. An empty array
// means no cache-level affinity override is in effect.
for (CacheKeyConfiguration k : cfg.getKeyConfiguration()) {
    // Example output: com.example.InvoiceKey.customerId
    System.out.println(k.getTypeName() + "." + k.getAffinityKeyFieldName());
}
```

If `getKeyConfiguration()` is empty, the affinity field is either `@AffinityKeyMapped` on the key class, an `AffinityKey<K>` wrapper applied at the call site, or the key itself (no composite).

Scan the hot partition from a callable pinned to the owning node and print a handful of entries:

```java
// Run this callable only on the partition's primary owner. Target the
// owner with compute().affinityCall(...) or with ClusterGroup.forNodeId(...).
// The setLocal(true) + setPartition(p) combination requires the partition
// to be primary-owned by the executing node.
public class SampleCallable implements IgniteCallable<List<String>> {

    @IgniteInstanceResource
    private transient Ignite ignite;

    private final String cacheName;
    private final int partition;

    public SampleCallable(String cacheName, int partition) {
        this.cacheName = cacheName;
        this.partition = partition;
    }

    @Override
    public List<String> call() {
        // setLocal(true) restricts the scan to entries owned by the
        // running node. Thin clients reject this flag. setPartition(p)
        // narrows the scan to one partition on the executing primary owner.
        ScanQuery<Object, Object> q = new ScanQuery<>();
        q.setLocal(true);
        q.setPartition(partition);

        List<String> sample = new ArrayList<>();
        try (QueryCursor<Cache.Entry<Object, Object>> cur = ignite.<Object, Object>cache(cacheName).query(q)) {
            int n = 0;
            for (Cache.Entry<Object, Object> e : cur) {
                sample.add(e.getKey().toString());
                if (++n >= 10) break;
            }
        }
        return sample;
    }
}
```

Call it with a cluster group that targets the owning node, and read the output. The pattern in the affinity-key values points at the cause:

- **Identical values** indicate a low-cardinality field (country code, status enum, tenant ID with few tenants).
- **Small sequential integers** indicate an autoincrement key in a short-lived cache.
- **Timestamps clustered in one range** indicate a time-range access pattern.

You now know the partition number, the node that owns it, the entry count relative to the mean, and the key pattern. Move to the cause.

## Identify the Cause

The key sample from Step 3 already pointed at one of the causes below. Confirm the match by answering the relevant question from your own code.

**Low-cardinality affinity field.** Is the affinity key a field with few distinct values, such as a country code, a status enum, or a tenant ID on a deployment with a handful of tenants? Every entry with the same affinity-key value lands on the same partition. Five distinct values put every record on five partitions. *Applies fix 1, 2, or 3.*

**Autoincrement keys in short-lived caches.** Does the cache get wiped and refilled frequently, and do keys start near zero? Early IDs hash to a subset of partitions. A short-lived cache keeps that subset hot for the lifetime of the data. *Applies fix 1 or 4.*

**Time-range access pattern on timestamp keys.** Are keys timestamps, and do your hot queries cover a narrow time range? `RendezvousAffinityFunction` implements the Highest Random Weight algorithm, which distributes adjacent timestamps across partitions rather than clustering them. The hot read pattern, not the key distribution, concentrates traffic. *Applies fix 5 (if the cache is small and read-mostly); otherwise the fix is application-side caching or a read-pattern change outside this guide.*

**Custom mapper bug.** Is there a `setAffinityMapper(...)` call in cache config, or a `CacheKeyConfiguration` pointing at a field the code no longer populates? The mapping is stale. *Applies fix 3 (correct the cache-side config) or fix 4 (redesign).*

## Apply the fix

Each fix is small. Pick by cause.

### Fix 1: Salt the key

Append a modulo suffix to a low-cardinality affinity-key value.

```java
// Append a deterministic shard suffix (derived from a high-cardinality
// companion field) to a low-cardinality value. The salted result hashes
// across `shards` partitions instead of one. The separator must not
// appear in either input.
public static String saltedAffinityKey(String lowCardValue, int id, int shards) {
    // For negative IDs, switch to Math.floorMod(id, shards) to avoid
    // negative suffixes.
    return lowCardValue + "#" + (id % shards);
}
```

At put time, use the salted value as the affinity-key field. Reads must reconstruct the same salt or fan out across all `shards` variants. A shard count around 16 or 32 spreads load without making reads expensive.

**Tradeoff:** reads must know the salt. A point read becomes a fan-out read when the caller does not hold the original ID.

### Fix 2: Change the Affinity Field

Pick a higher-cardinality field for `@AffinityKeyMapped`, or switch to a composite key where the high-cardinality field drives placement. [Design Keys for Colocation](../gridgain8-tutorials/data-locality/design-keys-for-colocation.md) covers the three mechanisms: `@AffinityKeyMapped` on the key class, the `AffinityKey<K>` wrapper at the call site, and `CacheKeyConfiguration` on the cache.

**Tradeoff:** schema change. Every caller that constructs the old key must update.

### Fix 3: Override Affinity at the Cache Level

Use `CacheKeyConfiguration` when the key class cannot change (generated code, third-party library, shared domain type). The cache points at the field by name.

```java
// CacheKeyConfiguration(typeName, affKeyFieldName) names the key class
// by fully-qualified name and the field that drives placement. The key
// class stays a plain POJO. The cache extracts the named field via
// reflection at put time.
//
// setKeyConfiguration takes a varargs CacheKeyConfiguration[]. One cache
// can declare overrides for multiple key types when it holds more than one.
CacheConfiguration<?, ?> cfg = new CacheConfiguration<>("invoices")
    .setKeyConfiguration(new CacheKeyConfiguration("com.example.InvoiceKey", "customerId"));
```

**Tradeoff:** the colocation contract is hidden from the domain code. The next developer finds it only by reading the cache configuration. Document it.

{% hint style="info" %}

`AffinityKeyMapper` was the older route for cache-side affinity overrides. It is deprecated. The JavaDoc recommends `@AffinityKeyMapped` or `CacheKeyConfiguration.setAffinityKeyFieldName(String)` in its place. New code should use `CacheKeyConfiguration`, and an existing mapper should migrate to it.

{% endhint %}

### Fix 4: Redesign the Schema

When the key distribution itself is wrong, no runtime fix survives. Pick new keys. [When to Break Colocation](../gridgain8-tutorials/data-locality/when-to-break-colocation.md) covers the schema-level decision.

**Tradeoff:** disruptive. Requires migration.

### Fix 5: Replicate the Cache

For a small reference table that reads heavily, switch the cache to `CacheMode.REPLICATED`. Every node keeps a full copy; no hot partition because no partitioning.

```java
// CacheMode.REPLICATED copies every entry to every server. Every node
// answers reads from local storage, so no partition can concentrate
// traffic. Backups are implicit. setBackups(...) has no effect on a
// REPLICATED cache.
//
// Write cost scales with cluster size. A put fans out to every node.
// Use this mode only for small, read-dominated tables.
CacheConfiguration<?, ?> cfg = new CacheConfiguration<>("genres")
    .setCacheMode(CacheMode.REPLICATED);
```

**Tradeoff:** every write hits every node. Works for small, read-mostly tables (country, genre, media type). Does not work for anything that grows with the business.

### Fix 6: Near Cache

For a read-heavy hot key, a client-side near cache absorbs the repeated reads. See [Near Caches](../gridgain8-development/near-caches.md) for configuration.

## Cause-to-fix Mapping

| Cause | Primary fix | Alternatives |
|---|---|---|
| Low-cardinality affinity field | 2 (change the field) | 1 (salt), 3 (cache-level override) |
| Autoincrement keys, short-lived cache | 1 (salt) | 4 (redesign) |
| Time-range pattern on timestamps | 5 (replicate if small) | Read-pattern change |
| Custom mapper bug | 3 (correct the override) | 4 (redesign) |

## Verify the fix

Re-run Step 2 of the diagnosis procedure. The `max / mean` ratio should drop to a small multiple (roughly 1.5 or less on a uniform distribution). If the ratio stays high, either the fix was applied to the wrong cause or the data has not fully redistributed yet. [Verify Colocation Is Working](../gridgain8-tutorials/data-locality/verify-colocation.md) covers the full verification toolkit, including the per-node primary count check that complements `localSizeLong`.

## Related

- [How to Choose a Partition Count for Your Workload](../architecture/data-modeling/choose-partition-count.md) handles the case where the count itself is wrong, rather than the key distribution.
- [Verify Colocation Is Working](../gridgain8-tutorials/data-locality/verify-colocation.md) teaches `SYS.CACHE_GROUPS`, `SYS.PARTITION_STATES`, and the local-scan broadcast pattern used in Step 2.
- [Design Keys for Colocation](../gridgain8-tutorials/data-locality/design-keys-for-colocation.md) covers the three mechanisms that Fix 2 and Fix 3 draw from.
- [When to Break Colocation](../gridgain8-tutorials/data-locality/when-to-break-colocation.md) covers the `PARTITIONED` vs `REPLICATED` decision that Fix 5 depends on.
