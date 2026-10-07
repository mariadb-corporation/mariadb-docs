---
description: GridGain 8.7.6-p1 is a maintenance release that includes a number of bug fixes.
hidden: true
---

# GridGain 8.7.6-p1 Release Notes

## What's New in This Release

### Introduction

This maintenance release includes a number of bug fixes.

### Changes in Behavior

## Installation and Upgrade Information

See the [Rolling Upgrades](https://docs.gridgain.com/docs/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-17371 | C++ | C++: Added support for enum. |
| IGN-12426 | JDBC | Fixed an issue that caused the JDBC thin driver to return incorrect metadata for DECIMAL and DATE types. |
| GG-19543 | Discovery | Decreased the client node reconnection time in large topologies. |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-21616 | Security | JaasAuthenticator will now merge permissions from multiple JAAS principals if a user belongs to multiple groups. |

### GridGain Ultimate Edition Changes

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://docs.gridgain.com) for more information.
