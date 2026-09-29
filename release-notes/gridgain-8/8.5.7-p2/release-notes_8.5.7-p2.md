---
description: GridGain 8.5.7-p2 is a maintenance release with several bug fixes.
hidden: true
---

# GridGain 8.5.7-p2 Release Notes

## What's New in This Release

### Introduction

This maintenance release includes three bug fixes.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-21579 | Affinity and Baseline Topology | Fixed an exception related to the ability to pass offline nodes to a baseline topology. |
| GG-21575 | Data Structures | Fixed possible `java.lang.ClassNotFoundException` on data rebalance with enabled persistence after custom java class renaming. |
| IGNITE-11641 | Persistent Storage | Fixed possible excessive WAL segment copying after WAL archive cleanup. |
| IGNITE-9402 | WAL | Fixed incorrect processing of IO exception that can cause an issue with node recovery from WAL |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://docs.gridgain.com) for more information.
