---
description: >-
  MariaDB Cloud backup support reference: which backup types (full,
  incremental, dump, snapshot, PITR) are supported by each MariaDB Server
  version and deployment topology.
---

# Supported Backup Types

## **MariaDB Server Versions and Backup Support**

| Server Version             | Full Backup | Incremental Backup | Dump(mariadb-dump) Backup | Snapshot Backup |
| -------------------------- | ----------- | ------------------ | ------------------------- | --------------- |
| 11.4.x                     | ✓           | ✓                  | ✓                         | ✓               |
| 10.11.x                    | ✓           | ✓                  | ✓                         | ✓               |
| 10.6.x                     | ✓           | ✓                  | ✓                         | ✓               |
| 10.5.x                     | ✓           | ✓                  | ✓                         | ✓               |
| 11.6.2 (Vector Preview)    | ✗           | ✗                  | ✗                         | ✓               |
| 11.7.1 (Release Candidate) | ✗           | ✗                  | ✗                         | ✓               |

### Notes:

* Versions 11.6.2 and 11.7.1 support only snapshot backups
* All other versions support all backup types: Full, Incremental, Dump, and Snapshot

### **Backup Support by Topology**

| Topology                       | Full Backup | Incremental Backup | Dump(mariadb-dump) Backup | Snapshot Backup | Point-in-Time Recovery (PITR) |
| ------------------------------ | ----------- | ------------------ | ------------------------- | --------------- | ----------------------------- |
| Single Node                    | ✓           | ✓                  | ✓                         | ✓               | ✓                             |
| Replicated                     | ✓           | ✓                  | ✓                         | ✓               | ✓                             |
| MariaDB Enterprise Cluster     | ✗           | ✗                  | ✗                         | ✓               | ✓                             |

{% hint style="info" %}
**Snapshots Only**&#x20;

MariaDB Enterprise Cluster supports **only** cloud-native snapshot backups. Full (physical) backups and logical backups are not available for this topology. Point-in-Time Recovery is supported from snapshot backups.
{% endhint %}

Please contact us if you have any questions about backup support for specific MariaDB versions.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
