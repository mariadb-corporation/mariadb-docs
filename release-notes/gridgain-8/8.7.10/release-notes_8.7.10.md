---
description: >-
  GridGain 8.7.10 introduces the @DurableStore annotation for durable sender
  storage in data center replication, together with a number of bug fixes and
  enhancements.
hidden: true
---

# GridGain 8.7.10 Release Notes

## What's New in This Release

This release includes a new feature and a number of bug fixes/enhancements.

### New Feature: @DurableStore annotation

Custom implementations of the sender node storage can now be annotated with the `@DurableStore` annotation to tell GridGain that the storage persists data and can survive restarts.
When a sender node with a durable storage goes down, the replication process will not be stopped.
The process will wait for the storage to be available again.
Refer to the [Sender storage](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/configuring-replication#sender-storage) documentation for details.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Known Issues

The public interface of `DrSenderStore` has been changed compared to version 8.7.8. If you use a custom implementation of this interface, do not upgrade to this version of the product. The old interface will be restored in a future release.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-26232 | Communication | The communication logic has been updated. Now there will be no attempts to establish connections to IPv6 addresses if IPv6 support is disabled. |
| GG-26663 | Security | Update external dependencies to resolve vulnerabilities reported by npm audit. |
| GG-26812 | Security | External dependencies that are used for Docker image were updated in order to resolve vulnerabilities found by nmp audit. |
| GG-26628 | SQL | SQL execution is now under threads starvation monitoring subsystem control. User will get a report in case threads are blocked for a long time. |
| GG-26534 | SQL | Fixed an issue that caused a SQL query to return incorrect results when executed against a REPLICATED cache on a data node that was being rebalanced. |
| GG-25940 | SQL | Users could get ArrayIndexOutOfBoundsException on SQL queries after non indexed fields have been dropped. This issue was fixed. |
| GG-26170 | SQL | Fix a client node failure caused by server nodes leaving the cluster during a SQL query execution. |
| GG-21371 | SQL | Fixed an issue that could cause a deadlock when a lazy query and DDL operations are executed simultaneously. |
| GG-26474 | Storage Changes | Checkpoint throttling logic has been improved. In case of simultaneous rebalance and checkpoint processes, checkpoint IO operations are given higher priority to decrease performance pressure from background tasks. |
| GG-26246 | Transactions | Fixed transaction recovery protocol to prevent a race causing partition desynchronization in case the originator node fails while a transaction is being rolled back. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-26492 | DR | Sender store annotation @DurableStore has been added. DR sender stop with durable store will not terminate datacenter replication process. |
| GG-24266 | DR | Data replication metrics for sender and receiver nodes are now supported via JMX. |
| GG-25788 | DR | Simultaneous execution of synchronous and non-synchronous Full State Transfer procedures is now prohibited. |
| GG-25693 | Security | Fixed an issue that required TASK_EXECUTE permissions to be configured to execute control.sh commands even when ADMIN_OPS is already granted. |
| GG-26352 | Snapshots & PITR | Fixed several issues that caused snapshot operations to terminate during a concurrent cache destroy. A cache snapshot will be cancelled if the cache is being destroyed. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
