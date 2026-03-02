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

| Topology                   | Full Backup | Incremental Backup | Dump(mariadb-dump) Backup | Snapshot Backup | Point-in-Time Recovery (PITR) |
| -------------------------- | ----------- | ------------------ | ------------------------- | --------------- | ----------------------------- |
| Single Node                | ✓           | ✓                  | ✓                         | ✓               | ✓                             |
| Replicated                 | ✓           | ✓                  | ✓                         | ✓               | ✓                             |
| MariaDB Galera Cluste**r** | ✗           | ✗                  | ✗                         | ✓               | ✗                             |

{% hint style="danger" %}
**Tech Preview Limitation: Snapshots Only**&#x20;

During the Tech Preview phase, MariaDB Galera Clusters support **only** cloud-native snapshot backups. Full (physical) backups, logical backups, and Point-in-Time Recovery (PITR) are not currently supported.
{% endhint %}

Please contact us if you have any questions about backup support for specific MariaDB versions.
