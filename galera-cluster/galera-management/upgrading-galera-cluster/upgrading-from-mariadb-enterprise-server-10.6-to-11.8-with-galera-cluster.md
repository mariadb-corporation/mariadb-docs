---
description: >-
  Upgrading a MariaDB Enterprise Server 10.6 Galera Cluster directly to 11.8 -
  the cluster-specific procedure (packages, bootstrap, state transfer) layered
  on top of the standalone 10.6-to-11.8 upgrade guide.
---

# Upgrading from MariaDB Enterprise Server 10.6 to 11.8 with Galera Cluster

[Galera Cluster](../../) ships with MariaDB Enterprise Server. Upgrading a Galera Cluster node is very similar to upgrading a standalone server directly from MariaDB Enterprise Server 10.6 to 11.8. For the full list of prerequisites, removed and renamed options, character-set and optimizer-cost-model changes, and the reverse-replication safety net, follow the standalone guide:

{% content-ref url="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrade-paths/mariadb-enterprise-server-11.8/upgrading-from-mariadb-enterprise-server-10.6-to-11.8" %}
[Upgrading from MariaDB Enterprise Server 10.6 to 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrade-paths/mariadb-enterprise-server-11.8/upgrading-from-mariadb-enterprise-server-10.6-to-11.8)
{% endcontent-ref %}

This page covers only what is **specific to a Galera Cluster deployment**: choosing an upgrade method, the Galera provider package, cluster shutdown order, and bootstrapping.

{% hint style="info" %}
The direct upgrade from 10.6 to 11.8, skipping 11.4, is a supported Enterprise Server upgrade path - see the standalone guide linked above. This page applies that same jump to a Galera Cluster.
{% endhint %}

## Choosing an Upgrade Method

There are two ways to move a Galera Cluster from 10.6 to 11.8. Which one you choose depends on whether you can tolerate a maintenance window.

* **Full cluster shutdown (recommended for the direct 10.6-to-11.8 jump).** Stop every node, upgrade all nodes to 11.8, then bootstrap the cluster again. Because no 10.6 and 11.8 nodes are ever running at the same time, there is no mixed-version window to reason about - each node performs exactly the standalone 10.6-to-11.8 upgrade. This method requires a maintenance window.
* **Rolling upgrade through intermediate versions (for zero downtime).** Galera guarantees mixed-version replication only between *adjacent* major releases, so a no-downtime rolling upgrade is performed one major version at a time: 10.6 → 10.11 → 11.4 → 11.8. Follow each hop in turn:
  * [Upgrading from MariaDB 10.6 to MariaDB 10.11 with Galera Cluster](upgrading-from-mariadb-10-6-to-mariadb-10-11-with-galeracluster.md)
  * [Upgrading from MariaDB 10.11 to MariaDB 11.4 with Galera Cluster](upgrading-from-mariadb-10.11-to-mariadb-11.4-with-galera-cluster.md)
  * [Upgrading from MariaDB 11.4 to MariaDB 11.8 with Galera Cluster](upgrading-from-mariadb-10.11-to-mariadb-11.4-with-galera-cluster-1.md)

{% hint style="warning" %}
Do not run a **rolling** upgrade that skips major versions (for example, keeping some nodes on 10.6 while others are already on 11.8). Galera negotiates the highest protocol version common to all cluster members, and mixed-version replication is only validated between adjacent major releases. To skip versions, use the full-cluster-shutdown method so that no two major versions are ever live at once.
{% endhint %}

The rest of this page describes the **full-cluster-shutdown** method.

## Before You Begin

* **Read the standalone upgrade guide.** All of the 10.6-to-11.8 configuration work - removed options that abort startup (`wsrep_strict_ddl`, `wsrep_load_data_splitting`, `wsrep_replicate_myisam`, and others), the character-set and optimizer-cost-model changes, and `old_mode`/`character_set_collations` compatibility - applies to every node. See [Upgrading from MariaDB Enterprise Server 10.6 to 11.8](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrade-paths/mariadb-enterprise-server-11.8/upgrading-from-mariadb-enterprise-server-10.6-to-11.8).
* **Take a backup.** Back up your data with [mariadb-backup](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview) before proceeding.
* **Identify the most advanced node.** Note which node has the highest `wsrep_last_committed` value at shutdown; you will bootstrap the new cluster from that node so it becomes the reference copy for state transfers.
* **Size gcache appropriately.** A large enough [`gcache.size`](../../reference/wsrep-variable-details/wsrep_provider_options.md#gcachesize) lets rejoining nodes catch up with an Incremental State Transfer (IST) instead of a full [State Snapshot Transfer (SST)](../../high-availability/state-snapshot-transfers-ssts-in-galera-cluster/introduction-to-state-snapshot-transfers-ssts.md). With a full shutdown, expect at least the first joining nodes to require an SST.
* **Finalize XA transactions.** Run `XA RECOVER` and commit or roll back any prepared external XA transactions before stopping the service.

## Performing a Full Cluster Shutdown Upgrade

{% stepper %}
{% step %}
**Take a final backup and stop the whole cluster**

Stop the application traffic (or drain the cluster from your load balancer or MaxScale), then perform a controlled shutdown on **every** node:

```sql
SET GLOBAL innodb_fast_shutdown = 1;
```

```bash
sudo systemctl stop mariadb
```

Stop the node holding the most up-to-date data **last** so it is the final writer, and record it - you will bootstrap from it in step 6.
{% endstep %}

{% step %}
**Remove the 10.6 Enterprise packages on each node**

Remove the old server together with the `galera-enterprise-4` wsrep provider to avoid package-manager conflicts.

{% tabs %}
{% tab title="RHEL, CentOS, Alma, Rocky" %}
```bash
sudo yum remove "MariaDB-*" galera-enterprise-4
```
{% endtab %}

{% tab title="Debian, Ubuntu" %}
```bash
sudo apt-get remove "mariadb-*" galera-enterprise-4
```
{% endtab %}

{% tab title="SLES" %}
```bash
sudo zypper remove "MariaDB-*" galera-enterprise-4
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
**Switch each node to the 11.8 Enterprise repositories**

{% code overflow="wrap" %}
```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
chmod +x mariadb_es_repo_setup
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply --mariadb-server-version="11.8"
```
{% endcode %}
{% endstep %}

{% step %}
**Install the 11.8 release series on each node**

Installing `MariaDB-server` pulls in the matching `galera-enterprise-4` wsrep provider automatically - in the 11.8 series Galera is still a dependency of the server package. (This changes in MariaDB 12.3, where Galera moves to a separate `mariadb-server-galera` package.)

{% tabs %}
{% tab title="RHEL, CentOS, Alma, Rocky" %}
```bash
sudo yum install MariaDB-server MariaDB-backup
```
{% endtab %}

{% tab title="Debian, Ubuntu" %}
```bash
sudo apt update && sudo apt install mariadb-server mariadb-backup
```
{% endtab %}

{% tab title="SLES" %}
```bash
sudo zypper install MariaDB-server MariaDB-backup
```
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
**Apply the 11.8 configuration changes on each node**

Before starting the service, update `my.cnf` on every node: scrub the removed 10.6 options and adopt the 11.8 defaults exactly as described in the standalone guide's [Implement Version-Specific Configuration Changes](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrade-paths/mariadb-enterprise-server-11.8/upgrading-from-mariadb-enterprise-server-10.6-to-11.8) and [Incompatible and Significant Changes](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrade-paths/mariadb-enterprise-server-11.8/upgrading-from-mariadb-enterprise-server-10.6-to-11.8) sections. Leave the Galera settings in your `wsrep.cnf` (such as `wsrep_cluster_address` and `wsrep_provider_options`) unchanged unless a value is explicitly removed in 11.8.

{% hint style="warning" %}
On Galera nodes, do **not** set `new_mode = OFF`. `new_mode` is a `SET` variable and rejects a literal `OFF`; the invalid value aborts startup during wsrep recovery:

```
[ERROR] mariadbd: Error while setting value 'OFF' to 'new_mode'
```

To clear `new_mode` - for example, to keep query planning closer to 10.6 - use an empty value instead: `new_mode = ""`.
{% endhint %}
{% endstep %}

{% step %}
**Bootstrap the first node**

Start the most up-to-date node (identified in step 1) as the first member of the new cluster, using [`--wsrep-new-cluster`](../installation-and-deployment/getting-started-with-mariadb-galera-cluster.md#bootstrapping-a-new-cluster) (for example, `galera_new_cluster`). This node becomes the reference copy the other nodes synchronize from.
{% endstep %}

{% step %}
**Start the remaining nodes**

Start MariaDB normally on the other nodes, one at a time:

```bash
sudo systemctl start mariadb
```

Each node rejoins the cluster and synchronizes via IST or SST. Wait for a node to reach `Synced` before starting the next one.
{% endstep %}

{% step %}
**Run the data upgrade on each node**

On every node, run [mariadb-upgrade](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade) with `--skip-write-binlog` so the schema-fix statements are not replicated across the cluster:

```bash
sudo mariadb-upgrade --skip-write-binlog
```

This upgrades the system tables and marks all tables as compatible with 11.8.
{% endstep %}
{% endstepper %}

## Post-Upgrade Verification

After all nodes are upgraded, confirm the cluster is healthy and running 11.8:

```sql
SELECT VERSION();
SHOW GLOBAL STATUS WHERE Variable_name IN
  ('wsrep_cluster_size', 'wsrep_cluster_status', 'wsrep_local_state_comment', 'wsrep_provider_version');
```

* `VERSION()` reflects the 11.8 series on every node.
* `wsrep_cluster_size` equals the number of nodes in the cluster.
* `wsrep_cluster_status` is `Primary` and `wsrep_local_state_comment` is `Synced`.
* [`wsrep_provider_version`](../../reference/galera-cluster-status-variables.md#wsrep_provider_version) is consistent across all nodes.

For general cluster health and quorum checks, see [What is MariaDB Galera Cluster](../../readme/mariadb-galera-cluster-guide.md).

{% @marketo/form formId="4316" %}
