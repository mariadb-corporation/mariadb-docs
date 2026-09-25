---
description: >-
  How GridGain helps you detect and mitigate network segmentation (the
  split-brain problem) using the Topology Validator and SegmentationResolver APIs.
---

# Split-Brain Protection

When it comes to maintaining a consistent database state, distributed environments face a variety of challenges. Network segmentation, also known as a "split-brain" problem, is one of these challenges. Due to temporary network problems, your Apache Ignite or GridGain cluster may become segmented with some nodes (or groups of nodes) isolated from the rest of the topology.

By default, each isolated group acts as if it were the only group and is unaware of other groups. Network segmentation, if not addressed, can quickly cause inconsistent clusters and inconsistent data.

GridGain provides the special Topology Validator API to reduce the possible  damage.

The topology validator checks that cluster topology is valid for cache operations. It is invoked each time a node joins or leaves the cluster.

You can use the `validate(Collection <ClusterNode>)` method to check for any combination of node parameters in your cluster. For example, you can check if your cluster has a specific number of nodes and stop all transactions if some nodes stop. This way, you can prevent having independent groups doing updates on their own.

## Split-Brain Prevention

### Data Validation

You can implement the `validate(Collection <ClusterNode>)` method to check the status of cluster topology and restrict potentially dangerous operations to prevent cluster from entering split brain.

- If the method returns `true`, the topology is considered valid, and operations are allowed to proceed.

- If the method returns `false`, update operations are restricted, and the following exceptions occur:

  * `CacheException` for all update operations (put, remove, and so on) that were attempted

  * `IgniteException` for all transaction commit attempts

If the topology validator is not configured, any cluster topology is considered valid. If an invalid topology becomes valid (for example, if a node rejoins the cluster, or cluster metrics normalize), operations are allowed to proceed.

#### Configuration Example

The following example shows how you can use the topology validator to allow cache updates to a group where only a majority of baseline nodes are alive:

```java
/** */
    private static class MajorityTopologyValidator implements TopologyValidator {
        /** */
        @CacheNameResource
        private transient String cacheName;
        /** */
        @IgniteInstanceResource
        private transient Ignite ignite;
        /** */
        @LoggerResource
        private transient IgniteLogger log;
        /** {@inheritDoc} */
        @Override public boolean validate(Collection<ClusterNode> nodes) {
            boolean valid = nodes.stream().filter(n -> !n.isClient()).count() >= ignite.cluster().currentBaselineTopology().size() / 2 + 1;
            if (!valid)
                log.warning("Possible split-brain for the cache " + cacheName + " has been detected, moving the cache to invalid state");
            return valid;
        }
    }
```

You can also set up TopologyValidator to use an external service like [Zookeeper](../gridgain8-usage/clustering/zookeeper-discovery.md) to make a topology check and decide if the current node group is segmented and should be deactivated.

After you resolve the split-brain situation, it is necessary to restart inactive groups to restore valid topology.

### Segment Analysis

GridGain provides a `SegmentationResolver` interface for active segment validation and split brain prevention.

The `isValidSegment` method checks a segment for validity. It is recommended to run the resolver in parallel with the topology validator to perform light-weight single checks (for example, accessibility of one IP address or one shared folder). Compound segment checks should be performed by using several resolver instances.

## Recovering from Split-Brain

While using topology validator helps you identify split brain issues and act on them quickly, it does not provide 100% guarantee that they will not happen.  If your topology does encounter split-brain issues, you may need to recover some data manually.

For example, let's assume the topology validator has selected a single active group of nodes and moved all other segmented groups to inactive.

If no data loss has happened (which means at least one valid data copy is present in active group), the recovery is as simple as cleaning persistent storages on segmented nodes and restarting them after resolving the split-brain issue, and then waiting for [data rebalancing](rebalancing/data-rebalancing.md) to complete.

You can check for data loss by calling the `IgniteCache.lostPartitions` method and testing for emptiness in return data:

```java
IgniteCache<Integer, String> cache = ignite.cache("myCache");

if (cache.lostPartitions().isEmpty){
    // Proceed normally
} else {
    // Handle lost partitions
}
```

If some partitions are lost, two outcomes are possible:

1. If persistence is enabled, you may get inconsistent data for both tx and atomic caches due to broken communications between nodes. You can resolve the issue by using a pre-made database snapshot to restore your data to consistent state. For example, you can set GridGain to continuously store data to enable [Point in Time Recovery](../gridgain8-management/snapshots/point-in-time-recovery.md).
Manual intervention may be necessary to restore lost updates.

2. If persistence is disabled, some data is lost forever and business invariants can be broken.
We recommend that you reload cache data.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
