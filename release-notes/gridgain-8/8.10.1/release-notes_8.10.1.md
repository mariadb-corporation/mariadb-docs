---
description: >-
  GridGain 8.10.1 fixes license checks that stopped nodes from starting with licenses issued before GridGain 8.10.
  Released on 2026-11-17.
---

# GridGain 8.10.1 Release Notes

**Release date:** 17 Nov 2026

## Overview

GridGain 8.10.1 is a maintenance release. It fixes the known issue in GridGain 8.10.0 that stopped nodes from starting when a license issued before GridGain 8.10 did not list a feature that the node used, such as cluster security. You no longer need to request a new license before you upgrade to GridGain 8.10.

For the full list of changes in GridGain 8.10, see the [GridGain 8.10.0 Release Notes](../8.10.0/release-notes_8.10.0.md).

## Licensing Changes

### Licenses Issued Before GridGain 8.10

GridGain 8.10.0 checked more features against the license than GridGain 8.9 did. With a license issued for GridGain 8.9, a 8.10 node that used one of those features could fail to start. In GridGain 8.10.1 these licenses are checked following the same rules as GridGain 8.9.

## Improvements and Fixed Issues

### Enterprise Edition Changes

| Issue ID | Category | Description                                                                                                                                                          |
|---|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GG-53662 | Licensing | Fixed an issue that prevented nodes from starting with licenses issued before GridGain 8.10 when cluster security or another Enterprise edition feature was enabled. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

If you upgrade from GridGain 8.9.x, read the [Breaking Changes](../8.10.0/release-notes_8.10.0.md#breaking-changes) and the [Installation and Upgrade Information](../8.10.0/release-notes_8.10.0.md#installation-and-upgrade-information) sections of the GridGain 8.10.0 release notes first.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`, `8.10.0`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older Thin Clients Compatibility

In most cases, older versions of thin clients should be compatible with newer versions of GridGain.
Below is the list of versions of thin clients that are tested for compatibility with the latest version.
The compatibility also means that you can safely update from any version on the list to any subsequent version.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`, `8.10.0`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`, `2.14.0`, `2.15.0`, `2.16.0`, `2.17.0`, `2.18.0`

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
