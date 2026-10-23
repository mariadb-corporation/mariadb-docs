---
description: >-
  GridGain 8.7.2-p9 is a maintenance release with a number of bug fixes,
  including affinity, baseline topology, and data center replication.
hidden: true
---

# GridGain 8.7.2-p9 Release Notes

## What's New in This Release

### Introduction

This maintenance release includes a number of bug fixes.

### Changes in Behavior

## Installation and Upgrade Information

See the [Rolling Upgrades](https://docs.gridgain.com/docs/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Known Issue

| Issue ID | Category | Description |
|---|---|---|
| GG-24210 | Discovery | OOM on clients during RU |

## Fixed Issues

### GridGain Professional Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-24088 | Affinity & BLT | Fixed bug with affinity history overflow when too many clients leave or join the cluster |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-24197 | DR | Fixed unexpected DR stop when client with default configuration connects to "drUseCacheNames=true" cluster |
| GG-24022 | DR | Fixed bug with ignoring cache level expiry policy during full state transfer |
| GG-23919 | DR | Fixed TTL not being transferred via DR |

### GridGain Ultimate Edition Changes

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://docs.gridgain.com) for more information.
