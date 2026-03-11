---
hidden: true
---

# Upgrading from MariaDB Enterprise Server 10.6 to 11.8

{% hint style="danger" %}
The content is subject to technical review by key stakeholders, MK and DK. While this draft is significantly improved from the initial versions, it should not be considered final.
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

    Bash

    ```bash
    sudo mariadb-upgrade
    ```
{% endstep %}
{% endstepper %}

## Incompatible and Deprecated Options

The following variables from version 10.6 have been removed, renamed, or deprecated in the 11.8 release series.

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

### 10.6 Compatibility and Rollback Support

To maintain 10.6 behavior or support reverse replication for rollback capabilities during the upgrade window, you can apply legacy defaults via a supplemental configuration file (e.g., `/etc/my.cnf.d/10.6_compat.cnf`).

```ini
[mariadb]
# --- Restore 10.6 Defaults ---
character_set_server           = latin1
collation_server               = latin1_swedish_ci
explicit_defaults_for_timestamp = OFF
innodb_snapshot_isolation      = OFF

# --- Reverse Replication / Rollback support ---
# Required to replicate 11.8 Primary to 10.6 Replica
character_set_collations       = ''
```

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
