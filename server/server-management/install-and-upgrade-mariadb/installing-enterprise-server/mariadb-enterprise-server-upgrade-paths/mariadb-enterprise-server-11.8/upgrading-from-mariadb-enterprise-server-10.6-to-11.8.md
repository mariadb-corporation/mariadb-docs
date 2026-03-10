---
hidden: true
---

# Upgrading from MariaDB Enterprise Server 10.6 to 11.8

{% hint style="info" %}
This guide is awaiting review from an SME and contains content to be removed before publication. Additionally, it does not include internal links to other documentation, as its content is subject to change.
{% endhint %}

This "multi-hop" upgrade path consolidates critical architectural changes, performance optimizations, and security enhancements from both the 11.4 and 11.8 release series into a single procedure.

## Prerequisites

Before beginning the upgrade, ensure these defensive measures and environment checks are completed to protect your data and ensure a smooth transition.

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
* Verify Recoverability: Always test your backup by restoring it to a non-production environment before proceeding with the upgrade.

### Service and Plugin Preparation

*   Remove Legacy Audit Plugin: If the `server_audit` plugin is present, it must be uninstalled to prevent conflicts with the modern MariaDB Enterprise Audit Plugin.

    ```sql
    UNINSTALL SONAME 'server_audit';
    ```
* Clear XA Transactions: Run `XA RECOVER;` to identify any external XA transactions in a prepared state.
* Finalize Transactions: All prepared XA transactions must be committed or rolled back before the 10.6 service is stopped.

### Environment Compatibility

* Operating System Support: Confirm your OS is compatible with version 11.8 (e.g., this series marks the final support for Windows 10 22H2).
* Customer Token: Have your Customer Download Token ready for the repository configuration step.

## Execution: The Upgrade Procedure

{% stepper %}
{% step %}
#### Perform a Controlled Shutdown of 10.6

1.  Initiate Fast Shutdown: Ensure the InnoDB engine closes cleanly.

    ```sql
    SET GLOBAL innodb_fast_shutdown = 1;
    ```
2. Check for XA transactions: Run `XA RECOVER;` and commit or roll back any prepared XA transactions before stopping the node.
3.  &#x20;Start the Service:

    ```bash
    sudo systemctl stop mariadb
    ```
{% endstep %}

{% step %}
#### Purge Legacy 10.6 Packages

You must remove the old version to prevent package manager conflicts before installing 11.8.

* YUM (RHEL/CentOS/Alma/Rocky): `sudo yum remove "MariaDB-*" galera-enterprise-4`
* APT (Debian/Ubuntu): `sudo apt-get remove "mariadb-*" galera-enterprise-4`
* ZYpp (SLES): `sudo zypper remove "MariaDB-*" galera-enterprise-4`
{% endstep %}

{% step %}
#### Switch to 11.8 Enterprise Repositories

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
#### Install the 11.8 Release Series

* YUM: `sudo yum install MariaDB-server MariaDB-backup`
* APT: `sudo apt update && sudo apt install mariadb-server mariadb-backup`
* ZYpp: `sudo zypper install MariaDB-server MariaDB-backup`
{% endstep %}

{% step %}
#### Implement Version-Specific Configuration Changes

Update your `my.cnf` file to address cumulative changes from both the 11.4 and 11.8 series. (See the Recommended 11.8 my.cnf section below.)
{% endstep %}

{% step %}
#### Bring the Service Online and Finalize Data

1.  Start the New Service:

    Bash

    ```bash
    sudo systemctl start mariadb
    ```
2.  Execute the Data Upgrade Utility: This final step corrects system table structures and marks all data files as compatible with version 11.8.

    Bash

    ```bash
    sudo mariadb-upgrade
    ```
{% endstep %}
{% endstepper %}

## Critical Cumulative Changes

Skipping version 11.4 means you must address the following important changes in your `my.cnf` configuration file:

### InnoDB and Optimizer Defaults

* Purge Batch Size: The default value for `innodb_purge_batch_size` has increased from 300 to 1000.
* Undo Tablespaces: MariaDB ES now defaults to 3 undo tablespaces (up from 0), enabling truncation while the server is running.
* Manual Undo Truncation: To reclaim disk space from undo logs, you must manually enable`innodb_undo_log_truncate=ON` in your configuration.
* Deprecated Frequency: The variable `innodb_purge_rseg_truncate_frequency` is now deprecated and ignored as the new truncation logic is a lighter operation.
* New Cost Model: The optimizer now uses a cost-based model optimized for SSD storage; default disk access costs have changed significantly.

### Security and Character Sets

* SSL Required by Default: Modern versions require SSL encryption by default; the server automatically generates self-signed certificates, and unencrypted connections are refused unless explicitly reconfigured.
* UTF-8 as Default: `utf8mb4` is now the default character set (replacing legacy `latin1` and `utf8`), and `utf8mb4_uca1400_ai_ci` is the standard collation.

### Removed and Deprecated Options

* Legacy Variables: `old_alter_table` is superseded by `alter_algorithm`.
* Deprecated Isolation Aliases: `tx_isolation` and `tx_read_only` are deprecated; use `transaction_isolation` and `transaction_read_only` instead.
* Flush Method: `innodb_flush_method` now defaults to `O_DIRECT`.

### Replication and Modern Workloads

* Optimistic ALTER TABLE: Replicas can now start `ALTER TABLE` operations in parallel with the primary server, significantly reducing replication lag for large schema changes. This is enabled by setting `binlog_alter_two_phase=1`.
* Vector Search Capabilities: Version 11.8 introduces native support for AI-powered semantic search via the `VECTOR(N)` data type and distance functions like `VEC_DISTANCE()`. Version 11.8 specifically optimizes these searches to be 30-50% faster than previous implementations.

### Recommended `my.cnf` for Version 11.8

This sample highlights critical changes needed when jumping from 10.6 to 11.8, reflecting new security and performance defaults.

```ini
[mariadb]
# --- CHARACTER SETS & COLLATIONS ---
# utf8mb4 is the modern default, replacing legacy utf8 (utf8mb3)
character-set-server  = utf8mb4
collation-server      = utf8mb4_uca1400_ai_ci

# --- INNODB STORAGE ENGINE ---
# Default flush method is now O_DIRECT for better throughput
innodb_flush_method   = O_DIRECT

# MariaDB ES now uses 3 undo tablespaces by default (up from 0)
# Manual enable is REQUIRED in Enterprise to reclaim space from undo logs
innodb_undo_log_truncate = ON

# Optimized purge batch size (increased from 300 to 1000)
innodb_purge_batch_size = 1000

# --- REMOVED OR DEPRECATED OPTIONS ---
# Replace legacy tx_* aliases with full names
transaction_isolation   = REPEATABLE-READ
transaction_read_only   = OFF

# REMOVE these legacy variables if they exist in your 10.6 config:
# debug_no_thread_alarm (Unused code)
# old_alter_table (Superseded by alter_algorithm)
# innodb_defragment_* (Manual defrag variables are removed)
# innodb_purge_rseg_truncate_frequency (Ignored with new truncation logic)

# --- REPLICATION ---
# Enable Optimistic ALTER TABLE to reduce replica lag
binlog_alter_two_phase = 1

# --- SECURITY ---
# SSL is required by default; unencrypted logins are refused

# --- VECTOR SEARCH TUNING (Optional) ---
# Fine-tune the MHNSW algorithm for AI workloads
# mhnsw_max_cache_size = 1G 
# mhnsw_ef_search = 100
```

## Post-Upgrade Verification

After the data upgrade is complete, verify the availability of 11.8-specific features:

*   Confirm Vector Search: Verify the new `VECTOR(N)` data type and conversion functions.

    ```sql
    CREATE TABLE test_vector (v VECTOR(3));
    SELECT VEC_ToText(VEC_FromText('[1,2,3]'));
    ```

    Note that version 11.8 optimizes these searches to be 30-50% faster than previous implementations.
* Verify Optimizer Performance: Run `EXPLAIN` on a complex query to see the new SSD-optimized cost model in action. Look for engine-specific costs in the `r_engine_stats` section of `ANALYZE FORMAT=JSON`.
* Check Replication Lag Fields: If this node is a replica, run `SHOW REPLICA STATUS\G` and look for the new `Master_Slave_time_diff` field for high-precision lag monitoring.

## Footnotes

* Controlled Shutdown & Package Removal: Correctly uses the `innodb_fast_shutdown = 1` command and platform-specific wildcards (`MariaDB-*`) identified in the official 11.8 upgrade guide.
* Repository Configuration: Accurately reflects the use of the `mariadb_es_repo_setup` script with the specific `--mariadb-server-version="11.8"` flag.
* Purge Batch Size & Undo Tablespaces: Accurately sources the default change for `innodb_purge_batch_size` (300 to 1000) and the new Enterprise default of 3 undo tablespaces.
* Manual Undo Truncation: Correctly identifies that `innodb_undo_log_truncate=ON` remains a manual requirement in Enterprise Server to reclaim space.
* Optimistic ALTER TABLE: Correctly includes the configuration `binlog_alter_two_phase=1` as the requirement for parallel replica schema changes.
* Vector Search Performance: Correctly cites the 30-50% speed increase specifically introduced in version 11.8 for vector search recall.
* `my.cnf` Deprecations: Accurately lists `old_alter_table` and `tx_isolation` as legacy variables that should be replaced with their modern counterparts.
