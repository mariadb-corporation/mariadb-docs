---
description: >-
  Upgrade directly from MariaDB Community Server 10.6 to MariaDB Enterprise
  Server 11.8 — combining a product switch (Community to Enterprise) and a
  major version jump (10.6 to 11.8) in a single upgrade window.
---

# Upgrade from MariaDB Community Server 10.6 to MariaDB Enterprise Server 11.8

This guide outlines a direct upgrade from **MariaDB Community Server 10.6** to **MariaDB Enterprise Server 11.8**. It combines two transitions in a single upgrade window: a product switch (Community to Enterprise) and a major version jump (10.6 to 11.8). With MariaDB Community Server 10.6 approaching end-of-life, this path lets you move to a maintained Enterprise release without an intermediate stop on ES 10.6.

{% hint style="info" %}
This guide assumes you are running on a variant of Linux that uses `systemd` to manage services (such as RHEL, CentOS, AlmaLinux, Rocky Linux, Debian, Ubuntu, or SLES).
{% endhint %}

{% hint style="warning" %}
This is a substantial change: a product switch and a major version jump performed back-to-back. Read this guide end-to-end before you start, and rehearse the procedure in a non-production environment first. Review the [MariaDB Engineering Policies](https://mariadb.com/engineering-policies/) to confirm your operating system is supported on the 11.8 release series.
{% endhint %}

## Prerequisites

Complete these checks and preparations before stopping your 10.6 service.

### Data Backup and Integrity

Occasionally, issues can be encountered during upgrades. These issues can even potentially corrupt the database's data files, preventing you from easily reverting to the old installation. It is generally best to perform a backup prior to upgrading. If an issue is encountered during the upgrade, you can use the backup to restore your MariaDB Server database to the old version. If the upgrade finishes without issue, then the backup can be deleted.

The instructions below show how to perform a backup using [MariaDB Backup](../../../../../server-usage/backup-and-restore/mariadb-backup/). For more information about backing up and restoring the database, please see the [Recovery Guide](../../../../../server-usage/backup-and-restore/).

1.  Take a full backup.

    ```bash
    sudo mariadb-backup --backup \
          --user=mariadb-backup_user \
          --password=mariadb-backup_passwd \
          --target-dir=/data/backup/preupgrade_cs10.6_to_es11.8
    ```

    Confirm successful completion of the backup operation.
2.  Prepare the backup so it is ready for immediate restoration if required.

    ```bash
    sudo mariadb-backup --prepare \
          --target-dir=/data/backup/preupgrade_cs10.6_to_es11.8
    ```

    Confirm successful completion of the prepare operation.
3. Verify recoverability: test your backup by restoring it to a non-production environment before proceeding.

### Convert InnoDB Row Format

MariaDB Enterprise Server 10.6 and later changed the `COMPRESSED` InnoDB row format to read-only. Before upgrading to MariaDB Enterprise Server 11.8, modify any compressed InnoDB tables on your 10.6 Community Server to use the `DYNAMIC` row format with `PAGE_COMPRESSED=1`.

1.  Identify any InnoDB tables that use the `COMPRESSED` row format:

    ```sql
    SELECT NAME, ROW_FORMAT
    FROM information_schema.INNODB_SYS_TABLES
    WHERE NAME NOT LIKE 'SYS_%'
       AND ROW_FORMAT = 'COMPRESSED';
    ```
2.  Convert each table to `DYNAMIC` row format with page compression:

    ```sql
    ALTER TABLE accounts.hq_sales
    ROW_FORMAT = DYNAMIC
    PAGE_COMPRESSED = 1;
    ```

### Audit Plugin Considerations

If you have the [MariaDB Audit Plugin](../../../../../reference/plugins/mariadb-audit-plugin/) (`server_audit.so`) installed on your Community Server, remove it before upgrading. Otherwise it will conflict with the [MariaDB Enterprise Audit Plugin](../../../../../reference/plugins/mariadb-enterprise-audit.md) that ships with MariaDB Enterprise Server 10.4 and later.

Remove the plugin by using the [UNINSTALL SONAME](../../../../../reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname.md) statement:

```sql
UNINSTALL SONAME 'server_audit';
```

If you load the plugin in a configuration file using the `plugin_load_add` option, remove that option as well. The MariaDB Enterprise Audit Plugin is automatically installed when you install MariaDB Enterprise Server.

### Compatibility and Legacy Support

These defaults ensure 11.8 keeps behaving like your 10.6 instance for applications that aren't yet ready for the new defaults.

* **Non-default character sets:** If your 10.6 instance uses `latin1` or `utf8mb3`, do not switch to `utf8mb4` immediately. Explicitly define your existing character set in the new `my.cnf` to override the 11.8 defaults.
* **`OLD_MODE` tip:** Set `old_mode = UTF8_IS_UTF8MB3` in your configuration so that `utf8` remains an alias for the legacy 3-byte character set instead of the new 4-byte standard.
* **SSL compatibility:** MariaDB 11.4 and later enable "Zero-configuration TLS" by default. If your application does not support SSL, set `require_secure_transport = OFF` in the `[mariadb]` section of `my.cnf` to prevent connection refusals.
* **XA transactions:** Run `XA RECOVER;` to identify any external XA transactions in a prepared state. These must be committed or rolled back before the service is stopped.

### Environment Compatibility

* **Engineering policy:** Verify your operating system version is supported for the 11.8 series in the [MariaDB Engineering Policies](https://mariadb.com/engineering-policies/).
* **Customer Download Token:** Retrieve your token from [https://customers.mariadb.com/downloads/token/](https://customers.mariadb.com/downloads/token/). You'll need it to configure the Enterprise repository in the steps below.

## The Upgrade Procedure

{% stepper %}
{% step %}
#### Perform a Controlled Shutdown of MariaDB Community Server 10.6

1.  Initiate a fast shutdown so the InnoDB engine closes cleanly:

    ```sql
    SET GLOBAL innodb_fast_shutdown = 1;
    ```
2.  Stop the service:

    ```bash
    sudo systemctl stop mariadb
    ```
{% endstep %}

{% step %}
#### Purge the MariaDB Community Server 10.6 Packages

When switching from MariaDB Community Server to MariaDB Enterprise Server, it is necessary to remove the existing Community Server installation before installing Enterprise Server. Otherwise, the package manager will refuse to install the Enterprise Server packages.

For Community Server 10.6, the Galera package is `galera-4` (named `galera-3` on APT for some legacy 10.3 installations, but 10.6 always uses `galera-4`).

{% tabs %}
{% tab title="Uninstall via YUM" %}
On RHEL, AlmaLinux, CentOS, and Rocky Linux:

```bash
sudo yum remove "MariaDB-*" galera-4
```

Verify that all MariaDB Community Server packages are uninstalled. The following command should return no results:

```bash
rpm --query --all | grep -i -E "mariadb|galera"
```
{% endtab %}

{% tab title="Uninstall via APT" %}
On Debian and Ubuntu:

```bash
sudo apt-get remove "mariadb-*" galera-4
```

Verify that all MariaDB Community Server packages are uninstalled. The following command should return no results:

```bash
apt list --installed | grep -i -E "mariadb|galera"
```
{% endtab %}

{% tab title="Uninstall via ZYpp" %}
On SLES:

```bash
sudo zypper remove "MariaDB-*" galera-4
```

Verify that all MariaDB Community Server packages are uninstalled. The following command should return no results:

```bash
rpm --query --all | grep -i -E "mariadb|galera"
```
{% endtab %}
{% endtabs %}

Be sure to check that the wildcard does not unintentionally refer to any of your custom applications.
{% endstep %}

{% step %}
#### Configure the MariaDB Enterprise Server 11.8 Repository

Download the repository setup script, verify it, and run it with your Customer Download Token to register the 11.8 Enterprise repository. Replace `CUSTOMER_DOWNLOAD_TOKEN` with the token retrieved during [Prerequisites](#environment-compatibility), and substitute `${checksum}` with the latest published checksum from the [Versions](../../../mariadb-package-repository-setup-and-usage.md#versions) section of the [MariaDB Package Repository Setup and Usage](../../../mariadb-package-repository-setup-and-usage.md) page.

{% code overflow="wrap" %}
```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
echo "${checksum}  mariadb_es_repo_setup" | sha256sum -c -
chmod +x mariadb_es_repo_setup
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply \
   --mariadb-server-version="11.8"
```
{% endcode %}

On APT systems, refresh the package index after running the setup script:

```bash
sudo apt update
```
{% endstep %}

{% step %}
#### Install MariaDB Enterprise Server 11.8

The repository setup only configures the source; install the new binaries explicitly.

{% tabs %}
{% tab title="Install via YUM" %}
```bash
sudo yum install MariaDB-server MariaDB-backup
```
{% endtab %}

{% tab title="Install via APT" %}
```bash
sudo apt install mariadb-server mariadb-backup
```
{% endtab %}

{% tab title="Install via ZYpp" %}
```bash
sudo zypper install MariaDB-server MariaDB-backup
```
{% endtab %}
{% endtabs %}

Installation of additional packages may be required for some plugins. Installation only loads MariaDB Enterprise Server onto the system — configuration is the next step.
{% endstep %}

{% step %}
#### Implement Version-Specific Configuration Changes

{% hint style="info" %}
Do not apply 11.8-specific variables while the 10.6 service is active. During the package swap, update `my.cnf` to adopt the 11.8 defaults for the [Optimizer Cost Model](#optimizer-cost-model-variables). These variables replace legacy hardcoded logic and are essential to the new engine's performance.
{% endhint %}

* **Scrub** legacy 10.6 variables (`old_alter_table`, etc.) — see [Removed, Superseded, or Renamed Options](#removed-superseded-or-renamed-options) below.
* **Adopt** the new [Optimizer Cost Model variables](#optimizer-cost-model-variables) using their 11.8 defaults.
* **Stabilize** with `NEW_MODE = OFF` to prevent unpredictable execution-plan changes on day one.

{% hint style="success" %}
**Recommended `my.cnf` for Version 11.8**

```ini
[mariadb]
# --- CHARACTER SETS & COLLATIONS ---
# utf8mb4 is the modern default; UCA 14.0.0 is ID #2304
character-set-server  = utf8mb4
collation-server      = utf8mb4_uca1400_ai_ci
# Use old_mode if your app requires 3-byte utf8 aliases
old_mode              = UTF8_IS_UTF8MB3

# --- OPTIMIZER COST MODEL (CRITICAL) ---
# Adopting 11.8 defaults replaces legacy hardcoded logic.
# Set NEW_MODE = OFF to stabilize query plans during initial cutover.
new_mode                        = OFF
optimizer_disk_read_cost        = 10.24
optimizer_disk_read_ratio       = 0.02
optimizer_extra_pruning_depth   = 8
optimizer_index_block_copy_cost = 0.0356
optimizer_key_compare_cost      = 0.011361
optimizer_key_copy_cost         = 0.015685
optimizer_key_lookup_cost       = 0.435777
optimizer_key_next_find_cost    = 0.082347
optimizer_rowid_compare_cost    = 0.002653
optimizer_rowid_copy_cost       = 0.002653
optimizer_row_copy_cost         = 0.060866
optimizer_row_lookup_cost       = 0.130839
optimizer_row_next_find_cost    = 0.045916
optimizer_scan_setup_cost       = 10
optimizer_where_cost            = 0.032

# --- INNODB STORAGE ENGINE ---
innodb_flush_method      = O_DIRECT
innodb_undo_log_truncate = ON
innodb_purge_batch_size  = 1000

# --- REPLICATION SAFETY NET ---
# REQUIRED if you intend to fail back to an existing 10.6 node.
# Fixes "Character set #2304" errors on legacy replicas.
character_set_collations = ''
binlog_alter_two_phase   = 1

# --- COMPLIANCE & CLEANUP ---
transaction_isolation    = REPEATABLE-READ
transaction_read_only    = OFF
```
{% endhint %}

If your platform uses YUM or ZYpp, note that MariaDB Enterprise Server's packages bundle the following configuration files: `/etc/my.cnf`, `/etc/my.cnf.d/client.cnf`, `/etc/my.cnf.d/mariadb-enterprise.cnf`, `/etc/my.cnf.d/mysql-clients.cnf`, and `/etc/my.cnf.d/server.cnf`. If your previous Community Server configuration files contained custom edits, the package manager may save your edited version with the `.rpmsave` extension during installation. Restore your edits before starting the new server.
{% endstep %}

{% step %}
#### Bring the Service Online and Run mariadb-upgrade

1.  Start the new service:

    ```bash
    sudo systemctl start mariadb
    ```
2.  Run the data-directory upgrade utility. It corrects system table structures and marks data files as compatible with version 11.8:

    ```bash
    sudo mariadb-upgrade
    ```
{% endstep %}
{% endstepper %}

## Incompatible and Significant Changes

The following variables from version 10.6 have been removed, renamed, or deprecated in the 11.8 release series.

### New Variables Added in 11.8

{% hint style="info" %}
Once the [11.8 binaries are installed](#install-mariadb-enterprise-server-11.8), update your [`my.cnf`](#implement-version-specific-configuration-changes) to define these new variables.
{% endhint %}

#### Optimizer Cost Model Variables

{% hint style="warning" %}
**Handle with care.** The 11.8 engine uses a new weighting system designed for modern storage (SSDs). Altering these variables without extensive benchmarks can lead to severe performance degradation or inefficient query execution plans. Keep these at their defaults upon upgrade unless you are performing expert-level performance tuning.
{% endhint %}

These variables define the weights of the new optimizer. If query execution plans change after the upgrade, these parameters are the primary audit points and represent [the optimizer cost model](../../../../../ha-and-performance/optimization-and-tuning/query-optimizer/the-optimizer-cost-model-from-mariadb-11-0.md).

<table><thead><tr><th width="423.5">Variable Name</th><th width="133.5">11.8 Default</th><th width="164.5">Note</th></tr></thead><tbody><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#new_mode"><code>NEW_MODE</code></a></td><td><code>OFF</code></td><td></td></tr><tr><td><code>OPTIMIZER_DISK_READ_COST</code></td><td><code>10.24</code></td><td><p><strong>Optimizer Plan Consistency:</strong></p><p>Row-based replication (RBR) remains unaffected by these changes. However, because the 11.8 Primary uses the new cost model while legacy 10.6 nodes use hardcoded logic, query execution plans may differ significantly between Master and Slave.</p></td></tr><tr><td><code>OPTIMIZER_DISK_READ_RATIO</code></td><td><code>0.02</code></td><td></td></tr><tr><td><code>OPTIMIZER_EXTRA_PRUNING_DEPTH</code></td><td><code>8</code></td><td></td></tr><tr><td><code>OPTIMIZER_INDEX_BLOCK_COPY_COST</code></td><td><code>0.0356</code></td><td></td></tr><tr><td><code>OPTIMIZER_KEY_COMPARE_COST</code></td><td><code>0.011361</code></td><td></td></tr><tr><td><code>OPTIMIZER_KEY_COPY_COST</code></td><td><code>0.015685</code></td><td></td></tr><tr><td><code>OPTIMIZER_KEY_LOOKUP_COST</code></td><td><code>0.435777</code></td><td></td></tr><tr><td><code>OPTIMIZER_KEY_NEXT_FIND_COST</code></td><td><code>0.082347</code></td><td></td></tr><tr><td><code>OPTIMIZER_ROWID_COMPARE_COST</code></td><td><code>0.002653</code></td><td></td></tr><tr><td><code>OPTIMIZER_ROWID_COPY_COST</code></td><td><code>0.002653</code></td><td></td></tr><tr><td><code>OPTIMIZER_ROW_COPY_COST</code></td><td><code>0.060866</code></td><td></td></tr><tr><td><code>OPTIMIZER_ROW_LOOKUP_COST</code></td><td><code>0.130839</code></td><td></td></tr><tr><td><code>OPTIMIZER_ROW_NEXT_FIND_COST</code></td><td><code>0.045916</code></td><td></td></tr><tr><td><code>OPTIMIZER_SCAN_SETUP_COST</code></td><td><code>10</code></td><td></td></tr><tr><td><code>OPTIMIZER_WHERE_COST</code></td><td><code>0.032</code></td><td></td></tr></tbody></table>

#### InnoDB Variables

InnoDB used complex buffering (such as the Change Buffer) to delay writes because hard drives were slow at random I/O. In version 11.8 these legacy layers are stripped back. The following [InnoDB system variables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) let MariaDB communicate more directly with modern SSD/NVMe storage, reducing the "middleman" overhead of the operating system's cache.

<table><thead><tr><th width="415.5">Variable Name</th><th>11.8 Default</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.4#innodb"><code>INNODB_ADAPTIVE_HASH_INDEX_CELLS</code></a><sup>^</sup></td><td><code>34679</code></td></tr><tr><td><a href="../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_alter_copy_bulk"><code>INNODB_ALTER_COPY_BULK</code></a><sup>#</sup></td><td><code>ON</code></td></tr><tr><td><code>INNODB_BUFFER_POOL_SIZE_AUTO_MIN</code></td><td><code>134217728</code></td></tr><tr><td><code>INNODB_BUFFER_POOL_SIZE_MAX</code></td><td><code>134217728</code></td></tr><tr><td><code>INNODB_DATA_FILE_BUFFERING</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_DATA_FILE_WRITE_THROUGH</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LINUX_AIO</code></td><td><code>auto</code></td></tr><tr><td><code>INNODB_LOG_CHECKPOINT_NOW</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LOG_FILE_BUFFERING</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LOG_FILE_MMAP</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LOG_FILE_WRITE_THROUGH</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LOG_SPIN_WAIT_DELAY</code></td><td><code>0</code></td></tr><tr><td><code>INNODB_TRUNCATE_TEMPORARY_TABLESPACE_NOW</code></td><td><code>OFF</code></td></tr></tbody></table>

#### Replication and Binlog Variables

As clusters grow, managing the Global Transaction ID (GTID) list becomes a performance bottleneck. 11.8 introduces "GTID Indexing," which treats the replication log more like a database table, allowing near-instant lookups when a replica reconnects. See [Replication and Binary Logging Variables](../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) for details.

<table><thead><tr><th width="455">Variable Name</th><th>11.8 Default</th><th>Note</th></tr></thead><tbody><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_alter_two_phase"><code>BINLOG_ALTER_TWO_PHASE</code></a><sup>#</sup></td><td><code>OFF</code></td><td></td></tr><tr><td><code>BINLOG_DO_DB</code></td><td><code>(None)</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_gtid_index"><code>BINLOG_GTID_INDEX</code></a><sup>#</sup></td><td><code>ON</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_gtid_index_page_size"><code>BINLOG_GTID_INDEX_PAGE_SIZE</code></a><sup>#</sup></td><td><code>4096</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_gtid_index_span_min"><code>BINLOG_GTID_INDEX_SPAN_MIN</code></a><sup>#</sup></td><td><code>65536</code></td><td></td></tr><tr><td><code>BINLOG_IGNORE_DB</code></td><td><code>(None)</code></td><td></td></tr><tr><td><code>BINLOG_LARGE_COMMIT_THRESHOLD</code></td><td><code>134217728</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_legacy_event_pos"><code>BINLOG_LEGACY_EVENT_POS</code></a><sup>#</sup></td><td><code>OFF</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_event_max_size"><code>BINLOG_ROW_EVENT_MAX_SIZE</code></a><sup>#</sup></td><td><code>8192</code></td><td>Packet safety: ensure this value on the 11.8 Primary is strictly lower than the <code>MAX_ALLOWED_PACKET</code> setting on your 10.6 Replicas. If an 11.8 row event exceeds the legacy replica's packet limit, replication will fail with a "Packet too large on slave" error.</td></tr><tr><td><code>BINLOG_SPACE_LIMIT</code></td><td><code>0</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_rewrite_db"><code>REPLICATE_REWRITE_DB</code></a><sup>#</sup></td><td><code>(None)</code></td><td></td></tr><tr><td><code>SLAVE_ABORT_BLOCKING_TIMEOUT</code></td><td><code>31536000</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_connections_needed_for_purge"><code>SLAVE_CONNECTIONS_NEEDED_FOR_PURGE</code></a><sup>#</sup></td><td><code>1</code></td><td><p><strong>Binary log purge safety:</strong></p><p>The default value is <code>1</code>. If your topology requires that binary logs be retained until acknowledged by multiple replicas, increase this value to prevent the primary from purging logs before all critical slaves have synchronized the data.</p></td></tr><tr><td><code>SLAVE_MAX_STATEMENT_TIME</code></td><td><code>0</code></td><td></td></tr></tbody></table>

#### Advanced Logging Variables

Slow logging was often a blunt instrument that could either miss critical spikes or flood the disk with useless data. Version 11.8 introduces granular filters: you can ignore queries that touch many rows but are still fast, or ensure that queries exceeding a specific "emergency" duration are always captured regardless of other filters. See [Server System Variables](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time) for details.

| Variable Name                     | 11.8 Default      |
| --------------------------------- | ----------------- |
| `LOG_SLOW_ALWAYS_QUERY_TIME`      | `31536000`        |
| `LOG_SLOW_MIN_EXAMINED_ROW_LIMIT` | `0`               |
| `LOG_SLOW_QUERY`                  | `OFF`             |
| `LOG_SLOW_QUERY_FILE`             | `(Host Specific)` |
| `LOG_SLOW_QUERY_TIME`             | `10`              |

#### Security and Authentication Variables

MariaDB 11.8 shifts toward modern cryptographic standards. This includes better handling of User-Defined Functions (UDFs) and a transition toward the [caching\_sha2\_password](../../../../../reference/plugins/authentication-plugins/authentication-plugin-caching_sha2_password.md) plugin, which provides significantly stronger protection against man-in-the-middle and brute-force attacks compared to legacy authentication.

<table><thead><tr><th width="506">Variable Name</th><th width="224.5">11.8 Default</th></tr></thead><tbody><tr><td><code>ALLOW_SUSPICIOUS_UDFS</code></td><td><code>OFF</code></td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_grant_tables"><code>SKIP_GRANT_TABLES</code></a><sup>#</sup></td><td><code>OFF</code></td></tr></tbody></table>

#### Resource Limits Variables

A single unoptimized query could theoretically consume all available disk space by creating a massive temporary table, crashing the operating system. Version 11.8 introduces safety valves that let administrators set hard limits on how much temporary space a single session or the entire server can use.

| Variable Name                 | 11.8 Default          |
| ----------------------------- | --------------------- |
| `MAX_BINLOG_TOTAL_SIZE`       | `0`                   |
| `MAX_TMP_SESSION_SPACE_USAGE` | `1099511627776` (1TB) |
| `MAX_TMP_TOTAL_SPACE_USAGE`   | `1099511627776` (1TB) |

#### Vector Search / MHNSW Variables

MariaDB 11.8 introduces a native Vector Search engine using the Metadata-HNSW (Hierarchical Navigable Small Worlds) algorithm. This allows the database to store and query embeddings (mathematical representations of text/images), enabling AI-powered semantic search directly within the SQL layer.

{% hint style="info" %}
Vector Search is entirely absent from MariaDB 10.6.

* Primary config: use `MHNSW_DEFAULT_DISTANCE` to define semantic search logic (default: `euclidean`).
* Compatibility warning: legacy 10.6 replicas cannot process vector data types or SQL functions; using them will break the replication link.
{% endhint %}

| Variable Name                                                                                                                            | 11.8 Default |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [`MHNSW_DEFAULT_DISTANCE`](../../../../../reference/sql-structure/vectors/vector-system-variables.md#mhnsw_default_distance)<sup>#</sup> | `euclidean`  |
| `MHNSW_DEFAULT_M`                                                                                                                        | `6`          |
| `MHNSW_EF_SEARCH`                                                                                                                        | `20`         |
| `MHNSW_MAX_CACHE_SIZE`                                                                                                                   | `16777216`   |

#### General Architecture Changes Variables

The final group of changes focuses on renaming legacy variables for industry compliance (SQL Standard) and adding features that improve how the database communicates with external tools such as proxies or system-versioning audit logs.

<table><thead><tr><th width="309.5">Variable Name</th><th width="161">11.8 Default</th><th>Note</th></tr></thead><tbody><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#redirect_url"><code>REDIRECT_URL</code></a><sup>#</sup></td><td><code>(None)</code></td><td><p><strong>Replication redirection safety:</strong></p><p><code>REDIRECT_URL</code> lets the server send redirection hints to proxies or clients.<br><strong>Crucial:</strong> configure this carefully on replicas to ensure internal slave-to-primary connections are not redirected, as accidental redirection of replication traffic will break the sync link.</p></td></tr><tr><td><a href="../../../../../reference/sql-structure/temporal-tables/system-versioned-tables.md#system_versioning_insert_history"><code>SYSTEM_VERSIONING_INSERT_HISTORY</code></a><sup>#</sup></td><td><code>OFF</code></td><td><p><strong>System versioning &#x26; binlog replay:</strong></p><p>The default is acceptable for standard operations. Because MariaDB 11.8's <code>mariadb-binlog</code> utility explicitly prints this value in its output, replaying binary logs with the 11.8 version of the tool is not recommended during the transition period.</p></td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#block_encryption_mode"><code>BLOCK_ENCRYPTION_MODE</code></a><sup>^</sup></td><td><code>aes-128-ecb</code></td><td>The 11.8 default is fine, but exercise care when calling <code>AES_ENCRYPT</code> and <code>AES_DECRYPT</code>; the syntax differs from 10.6.</td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_collations"><code>CHARACTER_SET_COLLATIONS</code></a><sup>#</sup></td><td><code>utf8mb4=...</code></td><td><code>character_set_collations</code> must be empty for reverse replication (11.8 → 10.6).</td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_isolation"><code>TRANSACTION_ISOLATION</code></a><sup>#</sup></td><td><code>REPEATABLE-READ</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_read_only"><code>TRANSACTION_READ_ONLY</code></a><sup>#</sup></td><td><code>OFF</code></td><td></td></tr><tr><td><code>WSREP_ALLOWLIST</code></td><td><code>(None)</code></td><td></td></tr><tr><td><code>WSREP_STATUS_FILE</code></td><td><code>(None)</code></td><td></td></tr></tbody></table>

{% hint style="danger" %}
<sup>#</sup>**Handle with extra care.** These variables have the highest impact on system stability and performance; please review during your configuration updates.
{% endhint %}

{% hint style="warning" %}
<sup>^</sup>**Caution.** These variables may impact system stability and performance; please review during your configuration updates.
{% endhint %}

### Options to Remove, Rename, or Update in 11.8

#### Removed, Superseded, or Renamed Options

During the maintenance window (after stopping 10.6 and before starting 11.8), you must scrub your `my.cnf` of all removed, superseded, and renamed options.

| Variable Name                                                                | 10.6 Default        | Technical Action / Replacement                               |
| ---------------------------------------------------------------------------- | ------------------- | ------------------------------------------------------------ |
| `DATETIME_FORMAT`<mark style="color:$warning;">²</mark>                      | `%Y-%m-%d %H:%i:%s` | Scrub. 11.8 enforces standard internal format strings.        |
| `DATE_FORMAT`<mark style="color:$warning;">²</mark>                          | `%Y-%m-%d`          | Scrub. Enforced standard format.                              |
| `DEBUG_NO_THREAD_ALARM`<mark style="color:$danger;">¹</mark>                 | `OFF`               | Remove. Retired legacy debug code.                            |
| `INNODB_CHANGE_BUFFERING`<mark style="color:$warning;">²</mark>              | `none`              | Scrub. Logic replaced by SSD-optimized write paths.           |
| `INNODB_CHANGE_BUFFER_MAX_SIZE`<mark style="color:$danger;">¹</mark>         | `25`                | Remove. Buffer size is now managed internally by the engine.  |
| `INNODB_DEFRAGMENT`<mark style="color:$warning;">²</mark>                    | `OFF`               | Scrub. Manual defragmentation is no longer supported.         |
| `INNODB_DEFRAGMENT_FILL_FACTOR`<mark style="color:$warning;">²</mark>        | `0.9`               | Scrub. Feature retired; logic is now internal.                |
| `INNODB_DEFRAGMENT_FILL_FACTOR_N_RECS`<mark style="color:$warning;">²</mark> | `20`                | Scrub. Feature retired; logic is now internal.                |
| `INNODB_DEFRAGMENT_FREQUENCY`<mark style="color:$warning;">²</mark>          | `40`                | Scrub. Feature retired; logic is now internal.                |
| `INNODB_DEFRAGMENT_N_PAGES`<mark style="color:$warning;">²</mark>            | `7`                 | Scrub. Feature retired; logic is now internal.                |
| `INNODB_DEFRAGMENT_STATS_ACCURACY`<mark style="color:$warning;">²</mark>     | `0`                 | Scrub. Feature retired; logic is now internal.                |
| `INNODB_VERSION`<mark style="color:$danger;">¹</mark>                        | `10.6.26`           | Remove. Versioning is consolidated in global server metadata. |
| `MAX_TMP_TABLES`<mark style="color:$danger;">¹</mark>                        | `32`                | Remove. Internal temp table management is now automated.      |
| `OLD_ALTER_TABLE`<mark style="color:$danger;">¹</mark>                       | `DEFAULT`           | Remove. Superseded by `ALTER_ALGORITHM`.                      |
| `TIME_FORMAT`<mark style="color:$warning;">²</mark>                          | `%H:%i:%s`          | Scrub. Enforced standard format.                              |
| `WSREP_CAUSAL_READS`<mark style="color:$warning;">²</mark>                   | `OFF`               | Scrub. Superseded by `wsrep_sync_wait`.                       |
| `WSREP_LOAD_DATA_SPLITTING`<mark style="color:$danger;">¹</mark>             | `OFF`               | Remove. Legacy Galera splitting logic retired.                |
| `WSREP_REPLICATE_MYISAM`<mark style="color:$danger;">¹</mark>                | `OFF`               | Remove. Galera no longer supports MyISAM replication.         |
| `WSREP_STRICT_DDL`<mark style="color:$danger;">¹</mark>                      | `OFF`               | Remove. Replaced by `wsrep_mode=STRICT_REPLICATION`.          |

{% hint style="danger" %}
<mark style="color:$danger;">¹</mark>**Fatal error.** MariaDB 11.8 will abort startup if these legacy parameters are detected in the configuration file. They MUST be removed before restart to prevent upgrade failure.

Example: `[ERROR] /usr/sbin/mariadbd: unknown variable 'MAX_TMP_TABLES=32'`
{% endhint %}

{% hint style="warning" %}
<mark style="color:$warning;">²</mark>**Warning.** MariaDB 11.8 will start but log a warning if these legacy parameters are detected in the configuration file. Scrub them during the upgrade to maintain configuration hygiene and ensure settings reflect active 11.8 features.

Warning example: `[Warning] 'innodb-change-buffering' was removed. It does nothing now and exists only for compatibility with old my.cnf files.`
{% endhint %}

#### Options That Have Changed Default Values

{% hint style="info" %}
For variables that exist in both versions but have different defaults (such as `innodb_purge_batch_size`), the 11.8 engine automatically applies the new value. If you require identical behavior to your 10.6 environment during the initial cutover, hardcode the 10.6 values into your new configuration file.
{% endhint %}

<table><thead><tr><th width="255.5">Option</th><th>10.6 Default</th><th>11.8 Default</th><th>Impact / Note</th></tr></thead><tbody><tr><td><code>character_set_server</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Global default encoding shift.</td></tr><tr><td><code>CHARACTER_SET_CLIENT</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Modern standard for client connections.</td></tr><tr><td><code>CHARACTER_SET_CONNECTION</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Modern standard for session connections.</td></tr><tr><td><code>CHARACTER_SET_DATABASE</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Modern standard for database storage.</td></tr><tr><td><code>CHARACTER_SET_RESULTS</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Modern standard for query results.</td></tr><tr><td><code>collation_server</code></td><td><code>latin1_swedish_ci</code></td><td><code>utf8mb4_uca1400_ai_ci</code></td><td>Transition to the modern Unicode collation standard.</td></tr><tr><td><code>COLLATION_CONNECTION</code></td><td><code>latin1_swedish_ci</code></td><td><code>utf8mb4_uca1400_ai_ci</code></td><td>Update to modern Unicode Collation Algorithm (UCA).</td></tr><tr><td><code>COLLATION_DATABASE</code></td><td><code>latin1_swedish_ci</code></td><td><code>utf8mb4_uca1400_ai_ci</code></td><td>Update to modern Unicode Collation Algorithm (UCA).</td></tr><tr><td><code>EXPLICIT_DEFAULTS_FOR_TIMESTAMP</code></td><td><code>OFF</code></td><td><code>ON</code></td><td>Impacts <code>NULL</code> handling in <code>TIMESTAMP</code> columns. Modify for reverse replication (11.8 → 10.6) to maintain the same behavior on master and slave.</td></tr><tr><td><code>HAVE_SSL</code></td><td><code>DISABLED</code></td><td><code>YES</code></td><td>SSL/TLS is now natively available and enabled by default.</td></tr><tr><td><code>HISTOGRAM_TYPE</code></td><td>(Empty)</td><td><code>JSON_HB</code></td><td>Optimizer now stores histogram stats in JSON format. Modify for reverse replication (11.8 → 10.6).</td></tr><tr><td><code>INNODB_BUFFER_POOL_CHUNK_SIZE</code></td><td><code>134217728</code></td><td><code>0</code></td><td>Set to <code>0</code> to enable automatic calculation.</td></tr><tr><td><code>INNODB_LOG_WRITE_AHEAD_SIZE</code></td><td><code>8192</code></td><td><code>4096</code></td><td>Optimized for modern storage block alignment.</td></tr><tr><td><code>innodb_snapshot_isolation</code></td><td><code>OFF</code></td><td><code>ON</code></td><td>Enabled by default for improved consistency.</td></tr><tr><td><code>innodb_undo_tablespaces</code></td><td><code>0</code></td><td><code>3</code></td><td>Enables online truncation of undo logs.</td></tr><tr><td><code>optimizer_prune_level</code></td><td><code>1</code></td><td><code>2</code></td><td>Primary audit point for plan changes.</td></tr><tr><td><code>VERSION</code></td><td><code>10.6.26-MariaDB-log</code></td><td><code>11.8.7-MariaDB-log</code></td><td>Metadata only.</td></tr></tbody></table>

#### Deprecated Options

| Option                                 | Reason / Recommendation                        |
| -------------------------------------- | ---------------------------------------------- |
| `tx_isolation`                         | Replaced by `transaction_isolation`.           |
| `tx_read_only`                         | Replaced by `transaction_read_only`.           |
| `innodb_purge_rseg_truncate_frequency` | Obsolete due to lighter truncation operations. |

## Reverse Replication (11.8 to 10.6)

If a critical regression is discovered, you can use an existing 10.6 machine in your setup as a failback safety net.

{% hint style="warning" %}
Replicating from a MariaDB 11.8 Primary to a MariaDB 10.6 Replica is NOT officially supported by MariaDB Engineering. This configuration should only be used as a temporary emergency safety net during the upgrade window.
{% endhint %}

### Required 11.8 Primary Configuration

To prevent the 10.6 replica from crashing due to modern metadata (such as the `#2304` character set ID), the 11.8 Primary must be configured to "downgrade" its binary log output using a compatibility file.

#### The `rollback_compat.cnf` Setup

Create a standalone configuration file to house these temporary reversion settings at `/etc/my.cnf.d/rollback_compat.cnf`:

```ini
[mariadb]
# --- Core 10.6 Behavioral Reversion ---
character_set_server            = latin1
collation_server                = latin1_swedish_ci
explicit_defaults_for_timestamp = OFF
innodb_snapshot_isolation       = OFF

# --- Mandatory Metadata Compatibility ---
# Prevents "Character set #2304" (utf8mb4_uca1400_ai_ci) errors on 10.6
character_set_collations        = ''

# Force session metadata to legacy-compatible versions
collation_connection            = utf8mb3_general_ci
collation_database              = latin1_swedish_ci

# Standardize log checksums for the 10.6 parser
binlog_checksum                 = CRC32
```

To activate these settings, append the following line to the end of the `[mariadb]` section in your primary `/etc/my.cnf` file: `!include /etc/my.cnf.d/rollback_compat.cnf`

{% hint style="danger" %}
**Critical Compatibility Step**

MariaDB 11.8 uses a new default collation ID (#2304) that version 10.6 does not recognize. To prevent the 10.6 replica from crashing, you must set `character_set_collations = ''` on the 11.8 Primary. This forces the Primary to use legacy IDs that the 10.6 machine can process.
{% endhint %}

### Known "Breaking" Factors

Certain 11.8 features will immediately break the 10.6 replication link if used:

* **Vector data types:** any `INSERT` or `UPDATE` involving a `VECTOR(N)` column.
* **New functions:** use of `VEC_Distance` or other 11.8-specific SQL functions.
* **Large row events:** if `binlog_row_event_max_size` is tuned significantly higher than 10.6 defaults.

{% hint style="info" %}
**Note on Existing Nodes**

You do not need a new machine for reverse replication. You can use an existing 10.6 node already in your setup — stop replication on that node before the upgrade and resume it once the 11.8 Primary is configured for compatibility.
{% endhint %}

### Operational Steps for the Safety Net

{% stepper %}
{% step %}
**Isolate a 10.6 Node**

Before upgrading your entire environment, identify one existing replica to remain on version 10.6. Stop replication on this node just before you upgrade the Primary to 11.8.
{% endstep %}

{% step %}
**Configure 11.8 for Compatibility**

Immediately after installing version 11.8 on your Primary, apply the `rollback_compat.cnf` settings (such as `character_set_collations = ''` and `binlog_checksum = CRC32`).
{% endstep %}

{% step %}
**Start 11.8 and Rotate Logs**

Start the 11.8 service and run `FLUSH LOGS;`. This ensures the Primary begins writing its binary logs in a format the 10.6 replica can understand.
{% endstep %}

{% step %}
**Connect the 10.6 Node**

Point your existing 10.6 machine to the new 11.8 Primary. Because the data on the 10.6 node is already consistent with the pre-upgrade state, it can simply pick up the new changes from the 11.8 Primary.
{% endstep %}
{% endstepper %}

## Post-Upgrade Verification

After the data upgrade is complete, verify the functionality of 11.8 features.

1.  Confirm the server version:

    ```sql
    SELECT VERSION();
    ```

    The result should reflect the 11.8 GA series.
2.  Confirm Vector Search by verifying the new `VECTOR(N)` data type and conversion functions:

    ```sql
    CREATE TABLE test_vector (v VECTOR(3));
    SELECT VEC_ToText(VEC_FromText('[1,2,3]'));
    ```
3.  Verify optimizer performance by prefixing any SQL query with `ANALYZE FORMAT=JSON` to audit the new SSD-aware cost model:

    ```sql
    ANALYZE FORMAT=JSON SELECT * FROM orders WHERE total > 1000 AND status = 'shipped';
    ```

    The output includes real-time execution metrics such as `engine_cost` (measured in milliseconds) and `pages_accessed`, verifying that the optimizer is correctly prioritizing high-speed storage over legacy 10.6 logic:

    ```json
    "table": {
      "table_name": "orders",
      "access_type": "index_scan",
      "engine_cost": 4.12,
      "r_engine_stats": {
        "pages_accessed": 142,
        "pages_read_time_ms": 1.05
      }
    }
    ```
4. On a replica server, run `SHOW REPLICA STATUS\G` and look for the new `Master_Slave_time_diff` field.

***

{% include "../../../../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
