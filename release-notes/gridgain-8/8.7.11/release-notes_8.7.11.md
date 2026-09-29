---
description: >-
  GridGain 8.7.11 is a maintenance release with a number of critical bug fixes
  across atomic caches, SQL, storage, thin clients, and data replication.
hidden: true
---

# GridGain 8.7.11 Release Notes

## What's New in This Release

This release includes a number of critical bugfixes.

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Known Issues

- The ignite-ml module may not work correctly when used with Hadoop files models because of missing dependencies.
  If you experience issues, you can try adding the following libraries to the `$IGNITE_HOME/libs` directory:

  - jackson-jaxrs-1.8.3.jar
  - jackson-xc-1.8.3.jar
  - hadoop-auth-2.9.1.jar
- We don't recommend configuring caches with ATOMIC and TRANSACTIONAL atomicity modes within one cache group. Such configurations will be forbidden in future releases.
- This release does not include the following dependencies:

  - jaxb-api-2.3.0.jar
  - jaxb-impl-2.3.0.jar
  - jaxb-core-2.3.0.jar
  - javax.activation-1.2.0.jar

  This can affect the functionality of `CacheHibernateStore` when GridGain is launched on Java 9+.
  If you experience exceptions related to missing dependencies, try adding the above mentioned libraries to `$IGNITE_HOME/libs`.
- In this release, the failure handler will not print out the thread dump when an error is detected.
  In the previous versions, thread dumps were printed out by default.
  If you want to enable the old behavior, set the following system property:

  ```
  -DIGNITE_DUMP_THREADS_ON_FAILURE=true
  ```

  The old behavior is planned to be restored in the next version.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-27116 | Atomic Caches | Fixed atomic caches partitions desync caused by message reordering. |
| GG-26746 | Binary Objects | Fixed an issue where an enum field of a BinaryObject could not be deserialized. |
| GG-26733 | Diagnostics & Failure Handling | Added throttling for thread dump generation in the failure handler to prevent stop-the-world pauses. |
| GG-27037 | Platforms & Thin Clients | Improved serialization performance for DateTime and other ISerializable types. |
| GG-27197 | Security | Updated several dependencies to address the vulnerabilities reported by npm audit. |
| GG-27038 | Security | The "javax.net.ssl.keyStoreProvider" property is now used to specify the default SSL key store provider. |
| GG-27058 | SQL | Fixed an issue where the SQL MERGE INTO command fails when executed from a client node. |
| GG-24263 | SQL | Optimized the deletion procedure for large SQL indexes. Deletion of a large index blocked the checkpointing operations and caused other operations to wait until the deletion is completed. Now large index deletion does not delay checkpointing. |
| GG-22560 | SQL | Added support for SQL queries disk offloading. If a query consumes too much memory, it can be offloaded to disk in order to prevent out of memory error. |
| GG-26632 | SQL | JDBC thin driver: SSL cipher suites can now be configured via the 'sslCipherSuites' parameter. |
| GG-27193 | Storage Engine | Fixed an invalid assertion triggered by an intensive rebalancing leading to node crash. |
| GG-27150 | Storage Engine | Fixed a possible IgniteOutOfMemoryException when a large cache in a cache group is destroyed |
| GG-22162 | Storage Engine | GridGain will now print all partitions that will be evicted with the eviction reason to the log. |
| GG-27121 | Storage Engine | Fixed exception caused by incorrect WAL reservation leading to a historical rebalance failure. |
| GG-26754 | Thin Clients | Added an option to configure query timeout for thin clients. |
| GG-26922 | Transactions | Fixed an NPE on transaction start which could cause partition desynchronization for the partitions that were evicted and assigned to the same node again. |
| GG-26858 | Transactions | Performance improvement for transactional caches in PRIMARY_SYNC mode. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-26947 | Data Replication | Fixed an issue where a server node configured as a sender did not replicate some data due to errors. |
| GG-26494 | Data Replication | Fixed the compatibility issue introduced in version 8.7.8, where a custom implementation of `DrSenderStore` led to a compilation error. |
| GG-26487 | Data Replication | Fixed incorrect DrFsStore size calculation. |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
