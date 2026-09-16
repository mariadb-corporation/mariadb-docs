---
description: >-
  Persistence tuning for GridGain 9, covering log and data separation,
  checkpointing and write throttling, SSD selection and over-provisioning, and
  MVCC considerations.
---

# Persistence Tuning

## Keep Replication Logs Separately From Data

Consider using separate drives for data files and replications logs. GridGain actively writes to both the data and log files.

## Checkpoints and Write Throttling

GridGain periodically starts the [checkpointing process](../administrators-guide/storage/engines/aipersist.md#checkpointing) that syncs dirty pages from memory to disk.

If dirty pages are allocated faster than they are written to disk, write throttling may occur. If you see a saw-like picture in write load and messages like
"Throttling is applied to page modifications", consider:

- using better hardware
- reduce cluster load
- add more data nodes to the cluster

## Purchase Production-Level SSDs

Note that the performance of Ignite Native Persistence may drop after several hours of intensive write load due to
the nature of how
[SSDs are designed and operate](http://codecapsule.com/2014/02/12/coding-for-ssds-part-2-architecture-of-an-ssd-and-benchmarking).
Consider buying fast production-level SSDs to keep the performance high or switch to non-volatile memory devices.

## SSD Over-provisioning

Performance of random writes on a 50% filled disk is much better than on a 90% filled disk because of the SSDs over-provisioning.

Consider buying SSDs with higher over-provisioning rates and make sure the manufacturer provides the tools to adjust it.

## HDD Usage Considerations

GridGain was designed to work on non-rotating devices. It's not recommended to deploy GridGain on HDD due to possible performance issues.

## MVCC

GridGain utilizes multi version data model, which means multiple copies of the same row exist in the storage. This can quickly exhaust the storage capacity under specific scenarios. Make sure you adjust GC watermark to avoid uncontrollable history growth.
