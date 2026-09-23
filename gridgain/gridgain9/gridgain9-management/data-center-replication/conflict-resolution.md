---
description: >-
  How GridGain 9 data center replication resolves conflicting writes —
  last-write-wins by source timestamp, and how topologies converge.
---

# Conflict Resolution

{% hint style="info" %}
This feature is only available as a part of GridGain 9 Enterprise and Ultimate editions.
{% endhint %}

In single-source layouts such as active-passive or hub-and-spoke, there are no replication conflicts: only one cluster writes to a given row, and the other clusters receive that write as a replicated update. In multi-source layouts such as active-active or ring, the same row can be written on more than one cluster before replication has propagated the change, and GridGain has to decide which write wins. This page describes how that decision is made.

## Last-Write-Wins by Source Timestamp

Every change committed on a source cluster is timestamped with the source cluster's hybrid logical clock at commit time. DCR carries this timestamp along with the change all the way to the replica, where it is compared against the timestamp of the row currently stored on the replica.

The rule is:

- If the *incoming change has a later timestamp* than the row stored on the replica, the incoming change is applied. The replica's row is overwritten and stored with the source's timestamp.
- If the *incoming change has an earlier timestamp*, the incoming change is rejected. The replica's row is left as it was.
- If the *two timestamps are equal*, the incoming change is treated as a duplicate of a write that has already been seen on the replica, and is not applied again.

This rule applies symmetrically: cluster A applies it to changes received from B, and cluster B applies it to changes received from A. Both clusters end up holding the value with the latest source-side timestamp.

## How Active-Active and Ring Topologies Converge

The same timestamp comparison that resolves a single write makes complex multi-cluster topologies converge to a consistent state, without any topology-aware logic in DCR.

In an *active-active* setup with two clusters, both clusters apply the comparison symmetrically. A write replicated from A to B is compared on B against B's stored row, and the later value wins. A write replicated from B to A is compared on A against A's stored row, and again the later value wins. The end state on both clusters is the value with the latest source-side timestamp, regardless of which cluster wrote first or which replication delivers its copy first.

In a *ring* topology, the same rule prevents a change from looping. A change committed on cluster A travels A → B → C → … → A carrying A's original timestamp the whole way. When the change arrives back at A, the locally stored row already has that exact timestamp – A wrote it. The equal-timestamp branch of the comparison treats the incoming change as a duplicate, and the loop terminates at the first hop back to its origin.

The same mechanism applies to any topology built from one-way replications. Every cluster applies the same comparison on every replicated write, and the cluster that wrote with the latest source-side timestamp wins everywhere.

## Idempotency and Re-Applies

The same comparison rule also makes routine restarts and recoveries safe. When a replication is restarted (`dcr stop` followed by `dcr start`), or when a worker node fails and another takes over, GridGain repeats the full state transfer for each replicated table. Any row that the replica already has is re-shipped with its original timestamp, the equal-timestamp branch of the rule treats it as a duplicate, and no data is corrupted.

## Clock Synchronization

Conflict resolution uses *hybrid logical clock* (HLC) timestamps. HLC absorbs modest clock drift between clusters: even if the two clusters' clocks differ by a few hundred milliseconds, HLC produces a consistent total order of writes across them.

In practice:

- *Synchronize cluster clocks.* Use NTP, PTP, or another time-sync service on every node in every cluster that participates in replication. Tight clock synchronization makes the timestamps that decide conflicts agree with operators' intuitions about which write was "first".
- *Conflict resolution is correct even if clocks are imperfectly synchronized.* What clock drift affects is which write *feels* newer to a human looking at wall-clock timestamps in the application, not whether the two clusters converge to the same value.
- *Replication-lag metrics depend on local time.* Lag is computed as the difference between the replica node's current clock and the slowest partition's watermark. If the replica's clock is ahead of the source's, the metric reads higher than the actual delay; if it is behind, the metric reads lower (and may even read negative). Use the metric as a relative trend rather than an absolute number.
- *`flushPoint` is interpreted in source-cluster time.* When you call `dcr flush --flush-point <time>`, the supplied instant is compared against the timestamps on incoming changes from the source. If the source's clock is behind the replica's, a flush point set to "now" on the replica may take longer to reach than expected.
