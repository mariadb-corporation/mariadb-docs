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

### Environment Compatibility

* Engineering Policy: Verify your operating system version is still supported for the 11.8 series by checking the [MariaDB Engineering Policies](https://mariadb.com/engineering-policies).
* Customer Token: Have your Customer Download Token ready for the repository configuration step.

## The Upgrade Procedure

{% stepper %}
{% step %}
### **Perform a Controlled Shutdown of 10.6**

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
### **Purge Legacy 10.6 Packages**

Remove the old version to prevent package manager conflicts before installing 11.8.

* YUM (RHEL/CentOS/Alma/Rocky): `sudo yum remove "MariaDB-*" galera-enterprise-4`
* APT (Debian/Ubuntu): `sudo apt-get remove "mariadb-*" galera-enterprise-4`
* ZYpp (SLES): `sudo zypper remove "MariaDB-*" galera-enterprise-4`
{% endstep %}

{% step %}
### **Switch to 11.8 Enterprise Repositories**

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
### **Install the 11.8 Release Series**

The repository setup only configures the source; you must explicitly install the new binaries.

* YUM: `sudo yum install MariaDB-server MariaDB-backup`
* APT: `sudo apt update && sudo apt install mariadb-server mariadb-backup`
*   ZYpp: `sudo zypper install MariaDB-server MariaDB-backup`

    \{% endstep %\}
{% endstep %}

{% step %}
### **Implement Version-Specific Configuration Changes**

Update your `my.cnf` file to address cumulative changes from both the 11.4 and 11.8 series.

{% hint style="success" %}
**Recommended `my.cnf` for Version 11.8 section**

```ini
[mariadb]
# --- CHARACTER SETS & COLLATIONS ---
# utf8mb4 is now the modern default
character-set-server  = utf8mb4
collation-server      = utf8mb4_uca1400_ai_ci

# --- INNODB STORAGE ENGINE ---
# O_DIRECT is the modern default for better throughput
innodb_flush_method   = O_DIRECT

# MariaDB ES now uses 3 undo tablespaces by default (up from 0)
# Manual enable is REQUIRED to reclaim space from undo logs
innodb_undo_log_truncate = ON

# Purge batch size default increased (300 -> 1000)
innodb_purge_batch_size = 1000

# --- REMOVED OR DEPRECATED OPTIONS ---
# Use full names instead of legacy aliases
transaction_isolation   = REPEATABLE-READ
transaction_read_only   = OFF

# REMOVE these if present in your 10.6 config:
# debug_no_thread_alarm, old_alter_table, innodb_defragment_*

# --- REPLICATION ---
# Enable to reduce lag by starting ALTERS on replicas immediately
binlog_alter_two_phase = 1

# --- SECURITY ---
# SSL is required by default; unencrypted logins are refused
```
{% endhint %}
{% endstep %}

{% step %}
### **Bring the Service Online and Finalize Data**

1. Start the New Service: `sudo systemctl start mariadb`.
2.  Execute the Data Upgrade Utility: This corrects system table structures and marks data files as compatible with version 11.8.

    ```bash
    sudo mariadb-upgrade
    ```
{% endstep %}
{% endstepper %}

## Incompatible and Significant Changes

The following variables from version 10.6 have been removed, renamed, or deprecated in the 11.8 release series.

### Performance and Optimizer Risk

These variables represent the most significant behavioral shifts between 10.6 and 11.8. Variables marked as New Architecture or New Feature indicate logic that was either hardcoded or non-existent in the 10.6 series.

<table><thead><tr><th width="264.5">Variable Name</th><th>10.6 Status/Default</th><th>11.8 Default</th><th>Impact / Note</th></tr></thead><tbody><tr><td><code>OPTIMIZER_DISK_READ_COST</code></td><td>New Architecture</td><td><code>10.24</code></td><td>New SSD-optimized cost model weight.</td></tr><tr><td><code>OPTIMIZER_ROW_LOOKUP_COST</code></td><td>New Architecture</td><td><code>0.130839</code></td><td>Impacts row fetch weight in join plans.</td></tr><tr><td><code>OPTIMIZER_DISK_READ_RATIO</code></td><td>New Architecture</td><td><code>0.02</code></td><td>Ratio for disk vs. memory reads.</td></tr><tr><td><code>OPTIMIZER_SCAN_SETUP_COST</code></td><td>New Architecture</td><td><code>10</code></td><td>Initial cost to initiate a table scan.</td></tr><tr><td><code>OPTIMIZER_WHERE_COST</code></td><td>New Architecture</td><td><code>0.032</code></td><td>Cost of evaluating row-level filters.</td></tr><tr><td><code>OPTIMIZER_KEY_LOOKUP_COST</code></td><td>New Architecture</td><td><code>0.435777</code></td><td>Index lookup weight in the cost model.</td></tr><tr><td><code>OPTIMIZER_KEY_COMPARE_COST</code></td><td>New Architecture</td><td><code>0.011361</code></td><td>Index comparison weight.</td></tr><tr><td><code>OPTIMIZER_ROW_COPY_COST</code></td><td>New Architecture</td><td><code>0.060866</code></td><td>Cost of copying rows to temporary tables.</td></tr><tr><td><code>OPTIMIZER_PRUNE_LEVEL</code></td><td><code>1</code></td><td><code>2</code></td><td>Changes join search depth and pruning strategy.</td></tr><tr><td><code>INNODB_PURGE_BATCH_SIZE</code></td><td><code>300</code></td><td><code>1000</code></td><td>Increased history cleanup; impacts long reads.</td></tr><tr><td><code>INNODB_LOG_FILE_BUFFERING</code></td><td><code>ON</code> (via 10.6)</td><td><code>OFF</code></td><td>Part of the new granular flush logic.</td></tr><tr><td><code>INNODB_DATA_FILE_BUFFERING</code></td><td><code>ON</code> (via 10.6)</td><td><code>OFF</code></td><td>Replaces legacy <code>O_DIRECT</code> behavior.</td></tr><tr><td><code>INNODB_LOG_FILE_WRITE_THRU</code></td><td><code>ON</code> (via 10.6)</td><td><code>OFF</code></td><td>Granular control over log file flushing.</td></tr><tr><td><code>INNODB_DATA_FILE_WRITE_THRU</code></td><td><code>ON</code> (via 10.6)</td><td><code>OFF</code></td><td>Granular control over data file flushing.</td></tr><tr><td><code>SKIP_GRANT_TABLES</code></td><td><code>OFF</code></td><td><code>OFF</code></td><td>The flag now automatically disables the Event Scheduler.</td></tr><tr><td><code>CHARACTER_SET_COLLATIONS</code></td><td>New Architecture</td><td><code>utf8mb4=...</code></td><td>Critical: Must be <code>''</code> for 10.6 reverse replication.</td></tr><tr><td><code>EXPLICIT_DEFAULTS_TIMESTAMP</code></td><td><code>OFF</code></td><td><code>ON</code></td><td>Changes how <code>NULL</code> is handled in <code>TIMESTAMP</code> fields.</td></tr><tr><td><code>INNODB_UNDO_TABLESPACES</code></td><td><code>0</code></td><td><code>3</code></td><td>Enables online truncation of undo logs.</td></tr><tr><td><code>INNODB_SNAPSHOT_ISOLATION</code></td><td><code>OFF</code></td><td><code>ON</code></td><td>Default for improved multi-statement consistency.</td></tr><tr><td><code>BINLOG_ALTER_TWO_PHASE</code></td><td>New Feature</td><td><code>OFF</code></td><td>Manual Enable: Reduces replica lag for DDL.</td></tr><tr><td><code>MHNSW_MAX_CACHE_SIZE</code></td><td>New Feature</td><td><code>16777216</code></td><td>Memory cache for Vector Search operations.</td></tr><tr><td><code>MHNSW_EF_SEARCH</code></td><td>New Feature</td><td><code>20</code></td><td>Candidate limit for HNSW Vector searches.</td></tr><tr><td><code>INNODB_LINUX_AIO</code></td><td><code>ON</code></td><td><code>auto</code></td><td>Modernized OS-level Async I/O handling.</td></tr><tr><td><code>MAX_TMP_SESSION_SPACE</code></td><td>New Architecture</td><td><code>1TB</code></td><td>Hard limit on session-level temporary disk usage.</td></tr><tr><td><code>BINLOG_ROW_EVENT_MAX_SIZE</code></td><td>New Architecture</td><td><code>8192</code></td><td>Controls splitting of large binlog row events.</td></tr></tbody></table>

### Options That Have Been Removed or Renamed

| Option                  | Reason / Recommendation                               |
| ----------------------- | ----------------------------------------------------- |
| `old_alter_table`       | Superseded by `alter_algorithm`.                      |
| `innodb_defragment_*`   | Manual InnoDB defragmentation is no longer supported. |
| `debug_no_thread_alarm` | Unused code.                                          |
| `DATETIME_FORMAT`       | Removed; use standard format strings.                 |
| `WSREP_STRICT_DDL`      | Replaced by `wsrep_mode=STRICT_REPLICATION`.          |

### Options That Have Changed Default Values

| Option                            | 10.6 Default        | 11.8 Default            |
| --------------------------------- | ------------------- | ----------------------- |
| `character_set_server`            | `latin1`            | `utf8mb4`               |
| `collation_server`                | `latin1_swedish_ci` | `utf8mb4_uca1400_ai_ci` |
| `explicit_defaults_for_timestamp` | `OFF`               | `ON`                    |
| `innodb_purge_batch_size`         | `300`               | `1000`                  |
| `innodb_undo_tablespaces`         | `0`                 | `3`                     |
| `innodb_snapshot_isolation`       | `OFF`               | `ON`                    |
| `optimizer_prune_level`           | `1`                 | `2`                     |

### Deprecated Options

| Option                                 | Reason / Recommendation                        |
| -------------------------------------- | ---------------------------------------------- |
| `tx_isolation`                         | Replaced by `transaction_isolation`.           |
| `tx_read_only`                         | Replaced by `transaction_read_only`.           |
| `innodb_purge_rseg_truncate_frequency` | Obsolete due to lighter truncation operations. |

## Critical Cumulative Changes

The upgrade from 10.6 to 11.4 is generally a smooth transition; however, jumping to 11.8 means addressing the following important default changes.

### InnoDB and Optimizer Defaults

* Purge Batch Size: The default value for `innodb_purge_batch_size` has increased from 300 to 1000.
* Undo Tablespaces: MariaDB ES now defaults to 3 undo tablespaces (up from 0), enabling truncation while the server is running.
* Manual Undo Truncation: To reclaim disk space from undo logs, you must manually enable `innodb_undo_log_truncate=ON` in your configuration.
* Deprecated Frequency: The variable `innodb_purge_rseg_truncate_frequency` is now deprecated and ignored as the new truncation logic is a lighter operation.
* New Cost Model: The optimizer now uses a cost-based model optimized for SSD storage; default disk access costs have changed significantly. See [Optimizer Cost Variables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/mariadb-internals-documentation-query-optimizer/the-optimizer-cost-model-from-mariadb-11-0#description-of-the-different-cost-variables) for manual tuning.

### Security and Character Sets

* SSL Required by Default: Modern versions require SSL encryption by default; unencrypted connections are refused unless reconfigured.
* UTF-8 as Default: `utf8mb4` is now the default character set (replacing legacy `latin1` and `utf8`), and `utf8mb4_uca1400_ai_ci` is the standard collation.

### Removed and Deprecated Options

* Legacy Variables: `old_alter_table` is superseded by `alter_algorithm`.
* Deprecated Isolation Aliases: `tx_isolation` and `tx_read_only` are deprecated; use `transaction_isolation` and `transaction_read_only` instead.
* Flush Method: `innodb_flush_method` now defaults to `O_DIRECT`.

### Replication and Modern Workloads

* Optimistic ALTER TABLE: Replicas can now start `ALTER TABLE` operations in parallel with the primary server to reduce lag, enabled by setting `binlog_alter_two_phase=1`.
* Vector Search Capabilities: Version 11.8 introduces native support for AI workloads via the `VECTOR(N)` data type and distance functions like `VEC_DISTANCE()`.

## Reverse Replication (11.8 to 10.6)

If the 11.8 upgrade is completed but a critical regression is discovered in production, a "Point-in-Time" rollback is required. Since the 11.8 data files are physically incompatible with 10.6, the only viable path without significant data loss is Reverse Replication.

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

### Known "Breaking" Factors

Certain 11.8 features will immediately break the 10.6 replication link if used:

* Vector Data Types: Any `INSERT` or `UPDATE` involving a `VECTOR(N)` column.
* New Functions: Use of `VEC_Distance` or other 11.8-specific SQL functions.
* Large Row Events: If `binlog_row_event_max_size` is tuned significantly higher than 10.6 defaults.

### Operational Steps for the Safety Net

1. Post-Upgrade Sync: Immediately after `mariadb-upgrade` finishes on the 11.8 server, take a fresh backup.
2. Provision 10.6: Restore that backup to a separate 10.6 instance (using `--skip-system-tables` if necessary, as system tables are now 11.8 format).
3. Rotate Logs: Run `FLUSH LOGS;` on the 11.8 Primary to ensure a clean start with the compatibility settings active.
4. Change Master: Point the 10.6 replica to the 11.8 Primary.

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
