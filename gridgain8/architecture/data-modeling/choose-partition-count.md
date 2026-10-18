---
description: >-
  Pick a partition count for a partitioned cache on GridGain 8. Default is 1024.
---

# How to Choose a Partition Count for Your Workload

## Prerequisites

- **Familiarity with partitioned caches.** This guide assumes you know what a partition is and how keys hash to partitions. [Understand How Your Cache Is Distributed](../../gridgain8-tutorials/cache-centric-foundations/understand-cache-distribution.md) covers the mental model.
- **A cache configuration to edit,** or a new cache to create. The partition count is set on the `AffinityFunction` attached to a `CacheConfiguration` at cache-creation time.

## Overview

This guide covers the three inputs that determine a partition count on GridGain 8: the default (1024), the cache's expected row count, and the cluster's expected node count. By the end, you have a partition count for a new cache, a sizing check for an existing cache, and the formula that maps row count to a safe number.

The partition count is fixed once the cache holds data. Changing it later requires destroying and recreating the cache.

## The Short Answer

**Use 1024 unless you have a specific reason not to.** It is the documented default on GridGain 8. It is correct for caches under ~250 million keys running on clusters of 3 to 30 nodes.

```java
// The no-argument constructor already uses 1024. Pass it explicitly when
// the count is a conscious decision rather than a default.
CacheConfiguration<Integer, Customer> cfg =
    new CacheConfiguration<Integer, Customer>("customers")
        .setAffinity(new RendezvousAffinityFunction(false, 1024));
```

If your cache fits that profile, stop here. The rest of the guide covers the cases where 1024 is wrong.

## The Decision Framework

Three inputs drive the count: **how many keys the cache will hold at steady state**, **how many nodes the cluster runs on**, and **how aggressively you expect to scale**. Walk the three steps in order.

### Step 1: Size the Cache

The operating rule is one partition per 250,000 keys or fewer. This comes from the `RendezvousAffinityFunction` guidance: avoid partitions with more than a quarter million keys. Large partitions slow rebalance, slow scan queries, and concentrate memory pressure on whichever node owns them.

Compute a minimum:

```text
min_partitions = ceil(expected_keys / 250_000)
```

Round up to the next power of two so the affinity function takes the bitmask fast path.

### Step 2: Check Cluster Size

Partitions must be significantly larger than node count. The JavaDoc uses that phrase without pinning a ratio. In practice, aim for at least 30 to 50 partitions per node. That ratio keeps distribution even and limits the fraction of data that shifts when a single node leaves.

For 3 to 30 nodes, 1024 is comfortable. For 100 nodes, 1024 still works but leaves 10 partitions per node. That is tight for rebalance smoothness. At that scale, move to 2048 or 4096.

### Step 3: Plan for Growth

Partition count is fixed at cache creation. Changing it later requires creating a new cache, copying data, and destroying the old one. If you expect the cache to grow past its current sizing within the deployment's lifetime, pick for the target size, not today's size.

### Reference Table

| Expected row count | Recommended partition count | Reasoning |
|---|---|---|
| Under 1M | 256-1024 (default) | Plenty of headroom per partition; cluster size dominates |
| 1M to 10M | 1024 (default) | 10K keys per partition at the top end |
| 10M to 100M | 1024 (default) | 100K keys per partition at the top end, still inside the guidance |
| 100M to 250M | 1024 | 250K keys per partition at the top, the upper edge of safe |
| 250M to 1B | 1024-4096 | Formula: `ceil(keys / 250_000)` rounded to power of 2; the top of the band leaves headroom for growth |
| 1B to 10B | 4096-32768 | Formula applies; verify memory overhead at your node count and choose toward the top of the band for growth headroom |
| Over 10B | 32768-65000 | Approaching the configured maximum of 65,000 |

The formula (`keys / 250,000`) and the 65,000 cap come directly from the source. Cluster-size multipliers apply on top. If you run 100+ nodes, pick the higher end of the row-count band.

## When to Accept the Default

Most caches. Concretely:

- The cache will hold under 250 million keys at steady state.
- The cluster runs on 3 to 30 nodes.
- You have no specific requirement for finer rebalance granularity.

If all three hold, use 1024 and move on.

## When to Tune up

Three situations justify deviating upward from 1024.

**Large caches.** When the expected row count exceeds 250 million, partitions grow past the quarter-million-keys guidance. Use the formula in Step 1 and round up.

**Large clusters.** When the cluster runs on more than 100 nodes, 1024 partitions produce fewer than 10 partitions per node. Rebalance moves full-node-sized chunks of data at a time. Bump to 2048 or 4096 so each node holds 20-40 partitions.

**Write-heavy caches with rebalance sensitivity.** If node additions or losses cause noticeable latency spikes during rebalance, smaller partitions move less data per operation and smooth the curve. This is a second-order optimization; confirm with measurement before committing.

## When to Tune Down

Rarely. The two narrow cases:

**Small caches on small clusters.** A cache of a few thousand rows on a 3-node cluster runs fine with 1024 partitions, but 256 reduces the per-partition bookkeeping on each node. The difference is small. Leave it alone unless memory accounting shows the overhead matters.

**Teaching clusters.** [Understand How Your Cache Is Distributed](../../gridgain8-tutorials/cache-centric-foundations/understand-cache-distribution.md) uses 32 partitions so the per-node counts fit in a printed table. That is a teaching number, not a production one.

## Tradeoffs

**More partitions** means finer rebalance granularity. When a node joins or leaves, the cluster moves one partition's worth of data per transfer instead of a larger chunk.

More partitions also raises the per-partition bookkeeping on each node. Every partition carries a partition state, update counter, and index segment whether it holds one key or a million. At 1024 partitions and 10 nodes, the bookkeeping overhead is negligible. At 65,000 partitions and 100 nodes, it dominates.

**Fewer partitions** means coarser rebalance and a higher risk of hot partitions. With 32 partitions on 3 nodes, a skewed key distribution concentrates traffic on one node. With 1024 partitions, the same skew spreads across many partitions before any single one heats up. How to Debug a Hot Partition (coming soon) handles the diagnostic when skew is the cause.

## Set it in Code

Set the partition count on the affinity function, then attach the function to the cache configuration.

```java
import org.apache.ignite.configuration.CacheConfiguration;
import org.apache.ignite.cache.affinity.rendezvous.RendezvousAffinityFunction;

CacheConfiguration<Integer, Customer> cfg =
    new CacheConfiguration<Integer, Customer>("customers")
        .setAffinity(new RendezvousAffinityFunction(false, 1024));
```

The first argument, `false`, is `excludeNeighbors`. The default of `false` lets backups land on any node. Set it to `true` to make the affinity function itself enforce primary/backup separation across physical hosts. Most deployments leave it `false` and enforce rack or host separation through `setBackupFilter` or the cluster's topology.

The partition count is fixed once the cache holds data. Changing it requires destroying the cache and recreating it. Caches that share a cache group must share the same affinity function, so the partition count applies to every cache in the group.

Valid values run from 1 to 65,000 (`CacheConfiguration.MAX_PARTITIONS_COUNT`). Powers of two enable a bitmask fast path in the hash calculation, so prefer 256, 512, 1024, 2048, 4096, 8192, 16384, 32768 over arbitrary integers.

## Verify

After creating the cache, confirm the partition count is what you set and that data spreads evenly across nodes. The `Affinity` runtime API reports the count directly:

```java
int count = ignite.affinity("customers").partitions();
```

[Verify Colocation Is Working](../../gridgain8-tutorials/data-locality/verify-colocation.md) teaches the full verification pattern, including per-partition row counts and the `SYS.CACHE_GROUPS` system view. The same techniques confirm a partition-count decision holds at runtime. The partition count reported by the cluster should equal the value you passed. The per-partition row counts should cluster around the expected mean, with no individual partition carrying a disproportionate share.

## Related

- [Understand How Your Cache Is Distributed](../../gridgain8-tutorials/cache-centric-foundations/understand-cache-distribution.md) introduces partitions, the `Affinity` API, and the relationship between partition count and node count.
- [Verify Colocation Is Working](../../gridgain8-tutorials/data-locality/verify-colocation.md) teaches the per-partition verification techniques that confirm a partition-count choice produces an even distribution.
- How to Debug a Hot Partition (coming soon) handles the case where the count is correct but a single partition takes disproportionate traffic because of key skew.
