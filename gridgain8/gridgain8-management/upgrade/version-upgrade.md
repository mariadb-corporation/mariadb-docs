---
description: >-
  The basic GridGain version upgrade process, including upgrading nodes safely
  without overwriting persistent data and checking version compatibility.
---

# Version Upgrade

Upgrade is an important part of the lifecycle of any software system. This page covers the basic upgrade process for GridGain.

{% hint style="info" %}
The version update process involves downtime. You can avoid downtime by using [rolling upgrades](rolling-upgrades.md).
{% endhint %}

## Upgrading Nodes

Updating node version is as simple as replacing the GridGain binaries with a new version. However, there are several things to keep in mind when performing the upgrade:

- GridGain cluster cannot have nodes that run on different GridGain versions. You need to stop the cluster and start it again on the new GridGain version.
- It is possible to accidentally overwrite your persistent storage or other important data during the upgrade. It is recommended to move this data outside of installation folder if you are planning upgrades:
* The work directory is used to store application data and all data required for the node to work. You can change its location as described in the [Configuring Work Directory](../../gridgain8-usage/setup.md#configuring-work-directory) section.
* The persistent storage holds all information stored on the node. You can change its location as described in the [Configuring Persistent Storage Directory](../../architecture/storage/native-persistence.md#configuring-persistent-storage-directory) section.
* WAL Archive os used to store WAL segments for recovery. You can change its location as described in [WAL Archive](../../architecture/storage/native-persistence.md#wal-archive) section.

## Version Compatibility

GridGain is tested for safe upgrade compatibility with recent versions. For the list of versions, check the [release notes]({release-notes}/8.10/release-notes_8.10) for the version you intend to update to.

If your planned update is not on the list, you may need to perform additional work to safely migrate to the new version.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
