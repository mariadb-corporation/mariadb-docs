---
hidden: true
---

# Upgrading from MariaDB Enterprise Server 10.6 to 11.8

{% hint style="danger" %}
The content is subject to technical review by key stakeholders DK and should not be considered final.
{% endhint %}

This guide outlines the process for performing a major version upgrade from MariaDB Enterprise Server (ES) 10.6 directly to MariaDB Enterprise Server 11.8.

{% hint style="info" %}
This guide assumes you are running on a variant of Linux that uses `systemd` to manage services (such as RHEL, CentOS, AlmaLinux, Rocky Linux, Debian, Ubuntu, or SLES).
{% endhint %}

## Prerequisites

Before beginning the upgrade, ensure these precautionary measures and environment checks are completed to protect your data.

### Data Backup and Integrity

*   Perform a Full Backup: Use `mariadb-backup` to create a complete copy of your current data.

    ```bash
    sudo mariadb-backup --backup \
          --user=mariadb-backup_user \
          --password=mariadb-backup_passwd \
          --target-dir=/data/backup/preupgrade_10.6_to_11.8
    ```
*   Prepare the Backup: Consolidate the backup files so they are ready for immediate restoration if required.

    ```bash
    sudo mariadb-backup --prepare --target-dir=/data/backup/preupgrade_10.6_to_11.8
    ```
* Verify Recoverability: Test your backup by restoring it to a non-production environment before proceeding.

### Service and Plugin Preparation

* Audit Plugin Transition: If you currently use the MariaDB 10.6 Audit Plugin (`server_audit.so`), it is recommended to transition to the MariaDB Enterprise Audit Plugin during this upgrade. If you maintain the Community version, ensure your configuration explicitly loads it to avoid conflicts.
* Commit or Roll Back XA Transactions: Run XA RECOVER; to identify any external XA transactions in a prepared state; these must be finalized before the service is stopped.

### Compatibility & Legacy Support

This ensures the team can maintain 10.6 behavior for applications that aren't ready for the new defaults.

* Handling Non-Default Character Sets: If your 10.6 instance uses `latin1` or `utf8mb3`, do not switch to `utf8mb4` immediately. You must explicitly define your existing character set in the new `my.cnf` to override the 11.8 defaults.
* The `OLD_MODE` Tip: Set `old_mode = UTF8_IS_UTF8MB3` in your configuration; this ensures that `utf8` remains an alias for the legacy 3-byte character set instead of the new 4-byte standard.
* Maintaining SSL Compatibility: Version 11.4+ enables "Zero-configuration TLS" by default. If your application does not support SSL, set `require_secure_transport = OFF` in the `[mariadb]` section of your `my.cnf` to prevent connection refusals.

### Environment Compatibility

* Engineering Policy: Verify your operating system version is still supported for the 11.8 series by checking the [MariaDB Engineering Policies](https://mariadb.com/engineering-policies).
* Customer Token: Have your Customer Download Token ready for the repository configuration step.

## The Upgrade Procedure

{% stepper %}
{% step %}
### Perform a Controlled Shutdown of 10.6

1.  Initiate Fast Shutdown to ensure the InnoDB engine closes cleanly.

    ```sql
    SET GLOBAL innodb_fast_shutdown = 1;
    ```
2.  Stop the Service `mariadb`.

    ```bash
    sudo systemctl stop mariadb
    ```
{% endstep %}

{% step %}
### Purge Legacy 10.6 Packages

Remove the old version to prevent package manager conflicts before installing 11.8.

* YUM (RHEL/CentOS/Alma/Rocky): `sudo yum remove "MariaDB-*" galera-enterprise-4`
* APT (Debian/Ubuntu): `sudo apt-get remove "mariadb-*" galera-enterprise-4`
* ZYpp (SLES): `sudo zypper remove "MariaDB-*" galera-enterprise-4`
{% endstep %}

{% step %}
### Switch to 11.8 Enterprise Repositories

Download and run the setup script, specifying version `11.8`.

{% code overflow="wrap" %}
```bash
curl -LsSO https://dlm.mariadb.com/enterprise-release-helpers/mariadb_es_repo_setup
chmod +x mariadb_es_repo_setup
sudo ./mariadb_es_repo_setup --token="CUSTOMER_DOWNLOAD_TOKEN" --apply --mariadb-server-version="11.8"
```
{% endcode %}
{% endstep %}

{% step %}
### Install the 11.8 Release Series

The repository setup only configures the source; you must explicitly install the new binaries.

* YUM: `sudo yum install MariaDB-server MariaDB-backup`
* APT: `sudo apt update && sudo apt install mariadb-server mariadb-backup`
*   ZYpp: `sudo zypper install MariaDB-server MariaDB-backup`

    \{% endstep %\}
{% endstep %}

{% step %}
### Implement Version-Specific Configuration Changes

{% hint style="info" %}
Do not apply 11.8-specific variables while the 10.6 service is active. During the package swap, update `my.cnf` to adopt the 11.8 defaults for the [Optimizer Cost Model](upgrading-from-mariadb-enterprise-server-10.6-to-11.8.md#optimizer-cost-model-variables). These variables replace legacy hardcoded logic and are essential for the new engine's performance.
{% endhint %}

* Scrub: Remove legacy 10.6 variables (`old_alter_table`, etc.).
* Adopt: Add the new [Optimizer Cost Model variables](upgrading-from-mariadb-enterprise-server-10.6-to-11.8.md#optimizer-cost-model-variables) using their 11.8 defaults.
* Stabilize: Set `NEW_MODE = OFF` to prevent unpredictable execution plan changes on Day 1.

{% hint style="success" %}
**Recommended `my.cnf` for Version 11.8 section**

```ini
[mariadb]
# --- CHARACTER SETS & COLLATIONS ---
# utf8mb4 is the modern default; UCA 14.0.0 is ID #2304
character-set-server  = utf8mb4
collation-server      = utf8mb4_uca1400_ai_ci
# Use old_mode if your app requires 3-byte utf8 aliases
old_mode              = UTF8_IS_UTF8MB3

# --- OPTIMIZER COST MODEL (CRITICAL #) ---
# Adopting 11.8 defaults replaces legacy hardcoded logic.
# Set NEW_MODE = OFF to stabilize query plans during initial cutover.
new_mode                      = OFF
optimizer_disk_read_cost      = 10.24
optimizer_disk_read_ratio     = 0.02
optimizer_extra_pruning_depth = 8
optimizer_index_block_copy_cost = 0.0356
optimizer_key_compare_cost    = 0.011361
optimizer_key_copy_cost       = 0.015685
optimizer_key_lookup_cost     = 0.435777
optimizer_key_next_find_cost  = 0.082347
optimizer_rowid_compare_cost  = 0.002653
optimizer_rowid_copy_cost     = 0.002653
optimizer_row_copy_cost       = 0.060866
optimizer_row_lookup_cost     = 0.130839
optimizer_row_next_find_cost  = 0.045916
optimizer_scan_setup_cost     = 10
optimizer_where_cost          = 0.032

# --- INNODB STORAGE ENGINE ---
innodb_flush_method      = O_DIRECT
innodb_undo_log_truncate = ON
innodb_purge_batch_size  = 1000

# --- REPLICATION SAFETY NET ---
# REQUIRED for failing back to an existing 10.6 node.
# Fixes "Character set #2304" errors on legacy replicas.
character_set_collations = ''
binlog_alter_two_phase   = 1

# --- COMPLIANCE & CLEANUP ---
transaction_isolation    = REPEATABLE-READ
transaction_read_only    = OFF
```
{% endhint %}
{% endstep %}

{% step %}
### Bring the Service Online and Finalize Data

1. Start the New Service: `sudo systemctl start mariadb`.
2.  Execute the Data Upgrade Utility: This corrects system table structures and marks data files as compatible with version 11.8.

    ```bash
    sudo mariadb-upgrade
    ```
{% endstep %}
{% endstepper %}

## Incompatible and Significant Changes

{% hint style="info" %}
In the following tables, **New Architecture** indicates that the variable controls a subsystem that was previously hardcoded or non-existent in 10.6.
{% endhint %}

The following variables from version 10.6 have been removed, renamed, or deprecated in the 11.8 release series.

### New Variables Added in 11.8

{% hint style="warning" %}
Once the 11.8 binaries are installed, update your `my.cnf` to explicitly define these new variables to their 11.8 default values. Optimizer variables represent a _New Architecture_ designed for SSDs; using the 11.8 defaults is the safest strategy moving forward.
{% endhint %}

#### Optimizer Cost Model Variables

{% hint style="warning" %}
**Handle with care**

Because the 11.8 engine uses a completely new "weighting" system designed for modern storage (SSDs), altering these variables without extensive benchmarks can lead to severe performance degradation or inefficient query execution plans. It is strongly recommended to keep these at their defaults upon upgradation unless you are performing expert-level performance tuning.
{% endhint %}

These variables define the weights of the new optimizer. If query execution plans change after the upgrade, these parameters are the primary audit points and represent [the optimizer cost model](../../../../../ha-and-performance/optimization-and-tuning/query-optimizer/the-optimizer-cost-model-from-mariadb-11-0.md).

<table><thead><tr><th width="430">Variable Name</th><th width="321.5">11.8 Default</th></tr></thead><tbody><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#new_mode"><code>NEW_MODE</code></a></td><td><code>OFF</code></td></tr><tr><td><code>OPTIMIZER_DISK_READ_COST</code></td><td><code>10.24</code></td></tr><tr><td><code>OPTIMIZER_DISK_READ_RATIO</code></td><td><code>0.02</code></td></tr><tr><td><code>OPTIMIZER_EXTRA_PRUNING_DEPTH</code></td><td><code>8</code></td></tr><tr><td><code>OPTIMIZER_INDEX_BLOCK_COPY_COST</code></td><td><code>0.0356</code></td></tr><tr><td><code>OPTIMIZER_KEY_COMPARE_COST</code></td><td><code>0.011361</code></td></tr><tr><td><code>OPTIMIZER_KEY_COPY_COST</code></td><td><code>0.015685</code></td></tr><tr><td><code>OPTIMIZER_KEY_LOOKUP_COST</code></td><td><code>0.435777</code></td></tr><tr><td><code>OPTIMIZER_KEY_NEXT_FIND_COST</code></td><td><code>0.082347</code></td></tr><tr><td><code>OPTIMIZER_ROWID_COMPARE_COST</code></td><td><code>0.002653</code></td></tr><tr><td><code>OPTIMIZER_ROWID_COPY_COST</code></td><td><code>0.002653</code></td></tr><tr><td><code>OPTIMIZER_ROW_COPY_COST</code></td><td><code>0.060866</code></td></tr><tr><td><code>OPTIMIZER_ROW_LOOKUP_COST</code></td><td><code>0.130839</code></td></tr><tr><td><code>OPTIMIZER_ROW_NEXT_FIND_COST</code></td><td><code>0.045916</code></td></tr><tr><td><code>OPTIMIZER_SCAN_SETUP_COST</code></td><td><code>10</code></td></tr><tr><td><code>OPTIMIZER_WHERE_COST</code></td><td><code>0.032</code></td></tr></tbody></table>

#### **InnoDB Variables**

InnoDB used complex buffering (like the "Change Buffer") to delay writes because hard drives were slow at random I/O. In version 11.8, these legacy layers are being stripped back. The following [InnoDB System Variables](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md) allow MariaDB to communicate more directly with modern SSD/NVMe storage, reducing the "middleman" overhead of the Operating System's cache.

<table><thead><tr><th width="415.5">Variable Name</th><th>11.8 Default</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/11.8.4#innodb"><code>INNODB_ADAPTIVE_HASH_INDEX_CELLS</code></a><sup>^</sup></td><td><code>34679</code></td></tr><tr><td><a href="../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_alter_copy_bulk"><code>INNODB_ALTER_COPY_BULK</code></a><sup>#</sup></td><td><code>ON</code></td></tr><tr><td><code>INNODB_BUFFER_POOL_SIZE_AUTO_MIN</code></td><td><code>134217728</code></td></tr><tr><td><code>INNODB_BUFFER_POOL_SIZE_MAX</code></td><td><code>134217728</code></td></tr><tr><td><code>INNODB_DATA_FILE_BUFFERING</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_DATA_FILE_WRITE_THROUGH</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LINUX_AIO</code></td><td><code>auto</code></td></tr><tr><td><code>INNODB_LOG_CHECKPOINT_NOW</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LOG_FILE_BUFFERING</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LOG_FILE_MMAP</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LOG_FILE_WRITE_THROUGH</code></td><td><code>OFF</code></td></tr><tr><td><code>INNODB_LOG_SPIN_WAIT_DELAY</code></td><td><code>0</code></td></tr><tr><td><code>INNODB_TRUNCATE_TEMPORARY_TABLESPACE_NOW</code></td><td><code>OFF</code></td></tr></tbody></table>

#### **Replication & Binlog Variables**

As clusters grow, managing the Global Transaction ID (GTID) list becomes a performance bottleneck. 11.8 introduces "GTID Indexing," which treats the replication and log more like a database table, allowing for near-instant lookups when a replica reconnects. See [Replication and Binary Logging Variables](../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) to learn more about the variables.

<table data-header-hidden><thead><tr><th width="455">Variable Name</th><th>11.8 Default</th></tr></thead><tbody><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_alter_two_phase"><code>BINLOG_ALTER_TWO_PHASE</code></a><sup>#</sup></td><td><code>OFF</code></td></tr><tr><td><code>BINLOG_DO_DB</code></td><td><code>(None)</code></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_gtid_index"><code>BINLOG_GTID_INDEX</code></a><sup>#</sup></td><td><code>ON</code></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_gtid_index_page_size"><code>BINLOG_GTID_INDEX_PAGE_SIZE</code></a><sup>#</sup></td><td><code>4096</code></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_gtid_index_span_min"><code>BINLOG_GTID_INDEX_SPAN_MIN</code></a><sup>#</sup></td><td><code>65536</code></td></tr><tr><td><code>BINLOG_IGNORE_DB</code></td><td><code>(None)</code></td></tr><tr><td><code>BINLOG_LARGE_COMMIT_THRESHOLD</code></td><td><code>134217728</code></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_legacy_event_pos"><code>BINLOG_LEGACY_EVENT_POS</code></a><sup>#</sup></td><td><code>OFF</code></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_row_event_max_size"><code>BINLOG_ROW_EVENT_MAX_SIZE</code></a><sup>#</sup></td><td><code>8192</code></td></tr><tr><td><code>BINLOG_SPACE_LIMIT</code></td><td><code>0</code></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#replicate_rewrite_db"><code>REPLICATE_REWRITE_DB</code></a><sup>#</sup></td><td><code>(None)</code></td></tr><tr><td><code>SLAVE_ABORT_BLOCKING_TIMEOUT</code></td><td><code>31536000</code></td></tr><tr><td><a href="../../../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#slave_connections_needed_for_purge"><code>SLAVE_CONNECTIONS_NEEDED_FOR_PURGE</code></a><sup>#</sup></td><td><code>1</code></td></tr><tr><td><code>SLAVE_MAX_STATEMENT_TIME</code></td><td><code>0</code></td></tr></tbody></table>

#### **Advanced Logging Variables**

Slow logging was often a "blunt instrument" that could either miss critical spikes or flood the disk with useless data. Version 11.8 introduces granular filters. You can now tell the engine to ignore queries that touch many rows but are still fast, or to ensure that queries exceeding a specific "emergency" duration are always captured, regardless of other filters. See [Server System Variables](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_query_time) to learn more about the following variables

| Variable Name                     | 11.8 Default      |
| --------------------------------- | ----------------- |
| `LOG_SLOW_ALWAYS_QUERY_TIME`      | `31536000`        |
| `LOG_SLOW_MIN_EXAMINED_ROW_LIMIT` | `0`               |
| `LOG_SLOW_QUERY`                  | `OFF`             |
| `LOG_SLOW_QUERY_FILE`             | `(Host Specific)` |
| `LOG_SLOW_QUERY_TIME`             | `10`              |

#### **Security & Authentication Variables**

MariaDB 11.8 shifts toward modern cryptographic standards. This includes better handling of User Defined Functions (UDFs) and a transition toward the [caching\_sha2\_password](../../../../../reference/plugins/authentication-plugins/authentication-plugin-caching_sha2_password.md) plugin, which provides significantly stronger protection against "man-in-the-middle" and brute-force attacks compared to legacy authentication.

<table><thead><tr><th width="406">Variable Name</th><th width="128.5">11.8 Default</th><th>Note</th></tr></thead><tbody><tr><td><code>ALLOW_SUSPICIOUS_UDFS</code></td><td><code>OFF</code></td><td></td></tr><tr><td><code>CACHING_SHA2_PASSWORD_AUTO_GENERATE_RSA_KEYS</code></td><td><code>ON</code></td><td>Caching_sha2 authentication plugin information should be configured when updating to 11.8</td></tr><tr><td><code>CACHING_SHA2_PASSWORD_DIGEST_ROUNDS</code></td><td><code>5000</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_grant_tables"><code>SKIP_GRANT_TABLES</code></a><sup>#</sup></td><td><code>OFF</code></td><td>Added in 10.10, check about event scheduler</td></tr></tbody></table>

#### **Resource Limits Variables**

A single unoptimized query could theoretically consume all available disk space by creating a massive temporary table, crashing the entire operating system. Version 11.8 introduces "Safety Valves" that allow administrators to set hard limits on how much temporary space a single session or the entire server can use.

| Variable Name                 | 11.8 Default          |
| ----------------------------- | --------------------- |
| `MAX_BINLOG_TOTAL_SIZE`       | `0`                   |
| `MAX_TMP_SESSION_SPACE_USAGE` | `1099511627776` (1TB) |
| `MAX_TMP_TOTAL_SPACE_USAGE`   | `1099511627776` (1TB) |

#### **Vector Search / MHNSW Variables**

MariaDB 11.8 introduces a native Vector Search engine using the Metadata-HNSW (Hierarchical Navigable Small Worlds) algorithm. This allows the database to store and query "embeddings" (mathematical representations of text/images), enabling AI-powered semantic search directly within the SQL layer.

| Variable Name                                                                                                                            | 11.8 Default |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| [`MHNSW_DEFAULT_DISTANCE`](../../../../../reference/sql-structure/vectors/vector-system-variables.md#mhnsw_default_distance)<sup>#</sup> | `euclidean`  |
| `MHNSW_DEFAULT_M`                                                                                                                        | `6`          |
| `MHNSW_EF_SEARCH`                                                                                                                        | `20`         |
| `MHNSW_MAX_CACHE_SIZE`                                                                                                                   | `16777216`   |

\*

#### **General Architecture Changes Variables**

The final group of changes focuses on renaming legacy variables for industry compliance (SQL Standard) and adding features that improve how the database communicates with external tools, such as proxies or system-versioning audit logs.

<table><thead><tr><th width="309.5">Variable Name</th><th width="161">11.8 Default</th><th>Note</th></tr></thead><tbody><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#redirect_url"><code>REDIRECT_URL</code></a><sup>#</sup></td><td><code>(None)</code></td><td></td></tr><tr><td><a href="../../../../../reference/sql-structure/temporal-tables/system-versioned-tables.md#system_versioning_insert_history"><code>SYSTEM_VERSIONING_INSERT_HISTORY</code></a><sup>#</sup></td><td><code>OFF</code></td><td>Default of this variable is fine, but mariadb-binlog prints this value and replay of binary logs using 11.8 mariadb-binlog is not recommended.</td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#block_encryption_mode"><code>BLOCK_ENCRYPTION_MODE</code></a><sup>^</sup></td><td><code>aes-128-ecb</code></td><td>High; Block_encryption_mode default on 11.8 is fine, but we should be careful when calling AES_ENCRYPT and AES DECRYPT_FUNCTION as syntax is different in 10.6</td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_collations"><code>CHARACTER_SET_COLLATIONS</code></a><sup>#</sup></td><td><code>utf8mb4=...</code></td><td>Character_set_collations should be empty for 11.8 -> 10.6</td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_isolation"><code>TRANSACTION_ISOLATION</code></a><sup>#</sup></td><td><code>REPEATABLE-READ</code></td><td></td></tr><tr><td><a href="../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#transaction_read_only"><code>TRANSACTION_READ_ONLY</code></a><sup>#</sup></td><td><code>OFF</code></td><td></td></tr><tr><td><code>WSREP_ALLOWLIST</code></td><td><code>(None)</code></td><td></td></tr><tr><td><code>WSREP_STATUS_FILE</code></td><td><code>(None)</code></td><td></td></tr></tbody></table>

{% hint style="danger" %}
<sup>#</sup>**Handle them with extra care**

These variables have the highest impact on system stability and performance; please review during your configuration updates.
{% endhint %}

{% hint style="warning" %}
<sup>^</sup>**Caution**

These variables may impact system stability and performance; please review during your configuration updates.
{% endhint %}

### Options to Remove, Rename, or Update in 11.8

#### Removed, Superseded or Renamed Options

During the maintenance window (after stopping 10.6 and before starting 11.8), you must scrub your `my.cnf` of all removed, superseded and renamed options.

| Options                                                                                                                                                | 10.6 Status / Default | Action / Recommendation                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------- | ---------------------------------------------------------------- |
| `old_alter_table`                                                                                                                                      | `OFF`                 | Remove. Superseded by `alter_algorithm`.                         |
| `innodb_defragment_*`                                                                                                                                  | N/A                   | Remove. Manual InnoDB defragmentation is no longer supported.    |
| `debug_no_thread_alarm`                                                                                                                                | N/A                   | Remove. Unused code.                                             |
| [`DATETIME_FORMAT`](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datetime_format)<sup>#</sup> | N/A                   | <p><br>Remove. Use standard format strings. Expected ERROR</p>   |
| [`DATE_FORMAT`](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#date_format)<sup>#</sup>         | `%Y-%m-%d`            | Remove. Standard format strings are now enforced. Expected ERROR |
| `TIME_FORMAT`                                                                                                                                          | `%H:%i:%s`            | Remove. Standard format strings are now enforced                 |
| `WSREP_STRICT_DDL`                                                                                                                                     | N/A                   | Remove. Replaced by `wsrep_mode=STRICT_REPLICATION`.             |
| `WSREP_CAUSAL_READS`                                                                                                                                   | `OFF`                 | Remove. Superseded by `wsrep_sync_wait`                          |
| `WSREP_LOAD_DATA_SPLITTING`                                                                                                                            | `OFF`                 | Legacy Galera splitting logic removed                            |
| `WSREP_REPLICATE_MYISAMOFF`                                                                                                                            | `OFF`                 | Remove. MyISAM replication support in Galera removed.            |
| `innodb_checksum_algorithm`                                                                                                                            | `crc32`               | Remove. Now hardcoded to `crc32` for performance.                |
| `innodb_log_files_in_group`                                                                                                                            | `2`                   | Remove. MariaDB 11.x uses a single dynamic log structure.        |
| `innodb_log_file_size`                                                                                                                                 | `96M`                 | Remove. Replaced by `innodb_redo_log_capacity`.                  |
| `query_cache_size`                                                                                                                                     | `1M`                  | Remove. The Query Cache feature has been removed.                |
| `query_cache_type`                                                                                                                                     | `OFF`                 | Remove. Associated with the removed Query Cache.                 |
| `slave_parallel_threads`                                                                                                                               | `0`                   | Remove. Replaced by `slave_parallel_workers`.                    |
| `innodb_change_buffering`                                                                                                                              | `all`                 | Remove. Engine now handles this via SSD-optimized logic.         |

#### Options That Have Changed Default Values

{% hint style="info" %}
For variables that have existed in both versions but have different defaults (e.g., `innodb_purge_batch_size`), the 11.8 engine will automatically apply the new value. If you require identical behavior to your 10.6 environment during the initial cutover, you must explicitly hardcode the 10.6 values into your new configuration file.
{% endhint %}

<table><thead><tr><th width="255.5">Options</th><th>10.6 Default</th><th>11.8 Default</th><th>Impact / Note</th></tr></thead><tbody><tr><td><code>binlog_row_image</code></td><td><code>FULL</code></td><td><code>MINIMAL</code></td><td>Minimal logging can break certain ETL or Audit tools.</td></tr><tr><td><code>character_set_server</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Certified Change:Global default encoding shift.</td></tr><tr><td><code>CHARACTER_SET_CLIENT</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Modern standard for client connections.</td></tr><tr><td><code>CHARACTER_SET_CONNECTION</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Modern standard for session connections.</td></tr><tr><td><code>CHARACTER_SET_DATABASE</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Modern standard for database storage.</td></tr><tr><td><code>CHARACTER_SET_RESULTS</code></td><td><code>latin1</code></td><td><code>utf8mb4</code></td><td>Modern standard for query results.</td></tr><tr><td><code>collation_server</code></td><td><code>latin1_swedish_ci</code></td><td><code>utf8mb4_uca1400_ai_ci</code></td><td>Transition to the modern Unicode collation standard.</td></tr><tr><td><code>COLLATION_CONNECTION</code></td><td><code>latin1_swedish_ci</code></td><td><code>utf8mb4_uca1400_ai_ci</code></td><td>Update to modern Unicode Collation Algorithm (UCA).</td></tr><tr><td><code>COLLATION_DATABASE</code></td><td><code>latin1_swedish_ci</code></td><td><code>utf8mb4_uca1400_ai_ci</code></td><td>Update to modern Unicode Collation Algorithm (UCA).</td></tr><tr><td><code>explicit_defaults_for_timestamp</code></td><td><code>OFF</code></td><td><code>ON</code></td><td>Impacts <code>NULL</code> handling in <code>TIMESTAMP</code>columns.</td></tr><tr><td><code>HAVE_SSL</code></td><td><code>DISABLED</code></td><td><code>YES</code></td><td>SSL/TLS is now natively available and enabled by default.</td></tr><tr><td><code>HISTOGRAM_TYPE</code></td><td>(Empty)</td><td><code>JSON_HB</code></td><td>Optimizer now stores histogram stats in JSON format.</td></tr><tr><td><code>innodb_adaptive_hash_index</code></td><td><code>ON</code></td><td><code>OFF</code></td><td>May reduce CPU contention but slow point-lookups.</td></tr><tr><td><code>innodb_buffer_pool_dump_at_shutdown</code></td><td><code>OFF</code></td><td><code>ON</code></td><td>Server now automatically saves buffer pool state.</td></tr><tr><td><code>INNODB_BUFFER_POOL_CHUNK_SIZE</code></td><td><code>134217728</code></td><td><code>0</code></td><td>Set to <code>0</code> to enable automatic calculation.</td></tr><tr><td><code>INNODB_LOG_WRITE_AHEAD_SIZE</code></td><td><code>8192</code></td><td><code>4096</code></td><td>Optimized for modern storage block alignment.</td></tr><tr><td><code>innodb_purge_batch_size</code></td><td><code>300</code></td><td><code>1000</code></td><td>Faster cleanup; may impact long-running reads.</td></tr><tr><td><code>innodb_snapshot_isolation</code></td><td><code>OFF</code></td><td><code>ON</code></td><td>Enabled by default for improved consistency.</td></tr><tr><td><code>innodb_undo_tablespaces</code></td><td><code>0</code></td><td><code>3</code></td><td>Enables online truncation of undo logs.</td></tr><tr><td><code>log_slow_admin_statements</code></td><td><code>OFF</code></td><td><code>ON</code></td><td><code>ALTER</code>/<code>OPTIMIZE</code> will now appear in slow logs.</td></tr><tr><td><code>optimizer_prune_level</code></td><td><code>1</code></td><td><code>2</code></td><td>Red Flag: Primary audit point for plan changes.</td></tr><tr><td><code>OPTIMIZER_SWITCH</code></td><td>(10.6 string)</td><td>(11.8 string)</td><td>Added <code>hash_join_cardinality=on</code>, <code>sargable_casefold=on</code>.</td></tr><tr><td><code>OPTIMIZER_ADJUST_SECONDARY_KEY_COSTS</code></td><td><code>fix_reuse_...</code></td><td><code>0</code></td><td>Weights for secondary key lookups simplified.</td></tr><tr><td><code>SESSION_TRACK_SYSTEM_VARIABLES</code></td><td>(10.6 list)</td><td>(11.8 list)</td><td>Added <code>redirect_url</code> to the tracking list.</td></tr><tr><td><code>PERFORMANCE_SCHEMA_MAX_STATEMENT_CLASSES</code></td><td><code>222</code></td><td><code>223</code></td><td>Expanded monitoring for new statement types.</td></tr></tbody></table>

#### Deprecated Options

| Option                                 | Reason / Recommendation                        |
| -------------------------------------- | ---------------------------------------------- |
| `tx_isolation`                         | Replaced by `transaction_isolation`.           |
| `tx_read_only`                         | Replaced by `transaction_read_only`.           |
| `innodb_purge_rseg_truncate_frequency` | Obsolete due to lighter truncation operations. |

## Reverse Replication (11.8 to 10.6)

If a critical regression is discovered, you can use an existing 10.6 machine in your setup as a failback safety net.

{% hint style="danger" %}
Replicating from a MariaDB 11.8 Primary to a MariaDB 10.6 Replica is NOT officially supported by MariaDB Engineering. This configuration should only be used as a temporary emergency safety net during the upgrade window.
{% endhint %}

### Required 11.8 Primary Configuration

To prevent the 10.6 replica from crashing due to modern metadata (such as the `#2304` character set ID), the 11.8 Primary must be configured to "downgrade" its binary log output.

Apply these settings to the 11.8 Primary `/etc/my.cnf.d/rollback_compat.cnf`:

```ini
[mariadb]
# --- Core 10.6 Behavioral Reversion ---
character_set_server            = latin1
collation_server                = latin1_swedish_ci
explicit_defaults_for_timestamp = OFF
innodb_snapshot_isolation       = OFF

# --- Mandatory Metadata Compatibility (SME "Red" List) ---
# Prevents "Character set #2304" (utf8mb4_uca1400_ai_ci) errors on 10.6
character_set_collations        = ''

# Forces session metadata to legacy-compatible versions
collation_connection            = utf8mb3_general_ci
collation_database              = latin1_swedish_ci

# Standardizes log checksums for the 10.6 parser
binlog_checksum                 = CRC32
```

{% hint style="danger" %}
**Critical Compatibility Step**

MariaDB 11.8 uses a new default collation ID (#2304) that version 10.6 does not recognize. To prevent the 10.6 replica from crashing, you must set `character_set_collations = ''` on the 11.8 Primary. This forces the Primary to use legacy IDs that the 10.6 machine can process
{% endhint %}

### Known "Breaking" Factors

Certain 11.8 features will immediately break the 10.6 replication link if used:

* Vector Data Types: Any `INSERT` or `UPDATE` involving a `VECTOR(N)` column.
* New Functions: Use of `VEC_Distance` or other 11.8-specific SQL functions.
* Large Row Events: If `binlog_row_event_max_size` is tuned significantly higher than 10.6 defaults.

{% hint style="info" %}
**Note on Existing Nodes**

You do not need a new machine for reverse replication. You can use an existing 10.6 node already in your setup. Simply stop replication on that node before the upgrade, and resume it once the 11.8 Primary is configured for compatibility.
{% endhint %}

### Operational Steps for the Safety Net

{% stepper %}
{% step %}
#### Isolate a 10.6 Node

Before upgrading your entire environment, identify one existing replica to remain on version 10.6. Stop the replication on this node just before you upgrade the Primary to 11.8.
{% endstep %}

{% step %}
#### Configure 11.8 for Compatibility

Immediately after installing version 11.8 on your Primary, apply the `rollback_compat.cnf` settings (such as `character_set_collations = ''` and `binlog_checksum = CRC32`).
{% endstep %}

{% step %}
#### Start 11.8 and Rotate Logs

Start the 11.8 service and run `FLUSH LOGS;`. This ensures the Primary begins writing its binary logs in a format the 10.6 replica can understand.
{% endstep %}

{% step %}
#### Connect the 10.6 Node

Point your existing 10.6 machine to the new 11.8 Primary. Because the data on the 10.6 node is already consistent with the pre-upgrade state, it can simply "pick up" the new changes from the 11.8 Primary.
{% endstep %}
{% endstepper %}

## Post-Upgrade Verification

After the data upgrade is complete, verify the functionality of 11.8 features:

* Confirm Version: `SELECT VERSION();` should reflect the 11.8 GA series.
*   Confirm Vector Search: Verify the new `VECTOR(N)` data type and conversion functions.

    ```sql
    CREATE TABLE test_vector (v VECTOR(3));
    SELECT VEC_ToText(VEC_FromText('[1,2,3]'));
    ```
* Verify Optimizer Performance: Run `ANALYZE FORMAT=JSON` on a complex query to see the new SSD-optimized cost model and engine-specific metrics (e.g., `pages_accessed`) in action.
* Check Replication Lag Fields: On a replica server, run `SHOW REPLICA STATUS\G` and look for the new `Master_Slave_time_diff` field.

## Footnotes (Not for publication)

* Controlled Shutdown & Package Removal: Uses the `innodb_fast_shutdown = 1` command and platform-specific wildcards (`MariaDB-*`) identified in the official 11.8 upgrade guide.
* Repository Configuration: Reflects the use of the `mariadb_es_repo_setup` script with the specific `--mariadb-server-version="11.8"` flag.
* Purge Batch Size & Undo Tablespaces: Sources the default change for `innodb_purge_batch_size` (300 to 1000) and the new Enterprise default of 3 undo tablespaces.
* Manual Undo Truncation: Identifies that `innodb_undo_log_truncate=ON` remains a manual requirement in Enterprise Server to reclaim space.
* Optimistic ALTER TABLE: Includes the configuration `binlog_alter_two_phase=1` as the requirement for parallel replica schema changes.
* `my.cnf` Deprecations: Lists `old_alter_table` and `tx_isolation` as legacy variables that should be replaced with their modern counterparts.
