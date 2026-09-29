---
description: >-
  GridGain 8.7.3 introduces Java 11 support, announces the deprecation of the VisorGUI monitoring tool, and includes several bug fixes.
hidden: true
---

# GridGain 8.7.3 Release Notes


## What's New in This Release

### Introduction
This release introduces support for Java 11 and a number of bug fixes.

### Visor GUI deprecation

GridGain is announcing the deprecation of the VisorGUI monitoring tool for GridGain. GridGain currently offers two tools that provide monitoring and metrics for GridGain and Apache Ignite clusters; VisorGUI and GridGain Web Console. VisorGUI was the initial monitoring tool for monitoring of local GridGain/Ignite clusters.

Since its introduction, GridGain Web Console has steadily added features to support management of GridGain and Apache Ignite applications from metrics analysis and querying to rolling upgrades and snapshotting. Web Console has reached a point in its maturity where it is at feature parity with and exceeds the capabilities of VisorGUI in many respects.

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-14823 | Common | Java 11 support |

### GridGain Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| IGN-13356 | SQL | Create table with template doesn’t work properly with data inserted from key-value API |
| IGN-11847 | Cache | Fixed possible failure during async partition cleanup |

## Related Information

[Customer Support](https://gridgain.freshdesk.com/support/login)

### We Value Your Feedback
The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://docs.gridgain.com) for more information.
