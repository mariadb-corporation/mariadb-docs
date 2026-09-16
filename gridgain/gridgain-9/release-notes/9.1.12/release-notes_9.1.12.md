---
description: >-
  GridGain 9.1.12 focuses on stability and extended WebAssembly computing support.
---

# GridGain 9.1.12 Release Notes

## Overview

GridGain 9.1.12 is a private release that is focused on stability and extended support for WASM computing.

## New Features

### WASM Improvements

This release brings 2 major improvements to [WASM compute](../../developers-guide/compute/wasm.md) jobs.

- The new `compute.wasm.enableCompiler` configuration option can be used to control if your WebAssembly code is [compiled to JVM bytecode](https://chicory.dev/docs/usage/runtime-compiler) at runtime for faster execution.
- WebAssembly instances are now cached per deployment unit and file name, reducing repeated module loading and initialization. Cached instances are cleared on `undeploy`.  Synchronization is required since WASM is not thread-safe.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-29003 | General | Fixed an issue that caused cluster instability and exceptions when coordinator node restarts. |
| IGN-28758 | Cluster Storage Engine | A new IGN-NODECFG-5 error code was added for "Join Denied" exceptions. |
| IGN-26458 | General | Fixed the getAll operation for Read-Only transactions in distributed environments. |
| GG-45622 | Cluster SQL Engine | Fixed incorrect binary metadata propagation in DR connection, which could lead to a NPE. |
| GG-45410 | Cluster Storage Engine | Fixed a bug that was causing data loss in secondary storage when a node hosting partitions was restarted. |
| GG-45019 | Distributed Computing | Wasm Compute: added configurable module caching to reduce load and parse overhead for consequent calls. |
| GG-44942 | Distributed Computing | Wasm Compute: added WasmJobDescriptor to build Wasm function descriptors in a strongly-typed manner. |
| GG-44533 | Cluster Rolling Upgrade | Added a REST endpoint for tracking rolling upgrade status. |
| GG-43816 | Platforms & Clients | Added support for CQ ARCHIVED event to C++ client. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.9`, `9.1.10`, `9.1.11`

{% hint style="warning" %}
When performing a rolling upgrade from GridGain 9.1.8 or 9.1.9, it is required to update to 9.1.10 first.
{% endhint %}

When updating from older versions, we recommend updating to version `9.1.8` first, before performing an update to current version.

## Known Limitations

### Rolling Upgrade Over 9.1.10

When performing a rolling upgrade from GridGain 9.1.9 or earlier, it is necessary to first upgrade to 9.1.10 before upgrading to 9.1.11 or a later version. This is caused by improvements in rolling upgrade procedure that make skipping 9.1.10 with a rolling upgrade impossible.

The upgrade to 9.1.10 must be performed for the whole cluster and committed before the next upgrade can be started.

You do not need to perform this intermediary upgrade when upgrading with downtime, as it only affects the rolling upgrade procedure.

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
