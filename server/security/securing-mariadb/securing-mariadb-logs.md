---
description: >-
  Learn how to harden MariaDB log files by implementing at-rest encryption, TLS
  for transit, strict OS permissions, and automated rotation to ensure data
  integrity and regulatory compliance.
---

# Securing MariaDB Logs

## Introduction

In any hardened database environment, logs are more than just a diagnostic tool; they are a critical trail of evidence and a blueprint of your data's movement. Ensuring the security of these logs is paramount for maintaining data integrity, achieving regulatory compliance (such as GDPR or HIPAA), and performing effective forensic analysis in the event of a breach.

Log security involves protecting data in two distinct states:

* Data-at-Rest: Preventing unauthorized users or malicious actors from reading or tampering with log files stored on the disk.
* Data-in-Transit: Ensuring that when logs are moved—specifically during replication—they cannot be intercepted or spoofed.

### Built-in Security Mechanisms

MariaDB provides several native features to help you secure this information:

* Access Control: Replication relies on a strictly defined username and password. Both the primary and the replica require specific privileges (`REPLICATION REPLICA`) to transfer, receive, and read log data.
* Native Encryption: You can protect the contents of your binary logs and relay logs at the storage level by enabling the `encrypt_binlog=ON` system variable.
* Database Table Security: While this guide focuses on file-based logging, MariaDB allows the General and Slow Query logs to be written to internal database tables. When logged to tables, these records inherit the same robust security, backup, and access control (via `GRANT` statements) as any other data in your database.
* On Linux, specifying `log_error` without a log file location is secure by default, because the systemd journal is used. See [this section](securing-mariadb-logs.md#changing-the-log-location) for context.

### Log File Locations

By default, MariaDB log files are located within the Data Directory ([`datadir`](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir); often `/var/lib/mysql/` on Linux systems). However, for both security and performance reasons, it is common practice to move these files to a dedicated, restricted volume.

This page focuses on the security of log _files_, providing best practices for file system permissions, encryption, and rotation strategies to ensure your "digital paper trail" remains uncompromised.

To control where logs are written, MariaDB uses the global system variable [`log_output`](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_output). The possible values are:

* `FILE`: (Default) Logs to a file.
* `TABLE`: Logs to the `mysql.general_log` and `mysql.slow_log` tables.
* `NONE`: Disables logging even if the logs are globally enabled.
* `FILE,TABLE`: Logs to both destinations simultaneously.

Table logging can be enabled for these log types:

1. [General Query Log](../../server-management/server-monitoring-logs/general-query-log.md): This logs all established client connections and all statements received from clients. Table logging uses the CSV storage engine by default. However, this can be changed; see [Writing Logs Into Tables](../../server-management/server-monitoring-logs/writing-logs-into-tables.md).
2. [Slow Query Log](../../server-management/server-monitoring-logs/slow-query-log/): This logs all SQL statements that took more than `long_query_time` seconds to execute and required at least `min_examined_row_limit` rows to be examined. Table logging uses the CSV storage engine by default. However, this can be changed; see [Writing Logs Into Tables](../../server-management/server-monitoring-logs/writing-logs-into-tables.md).
3. Binary Log (as of MariaDB 12.3): See [InnoDB-Based Binary Log](../../ha-and-performance/standard-replication/innodb-based-binary-log.md).

Since MariaDB is cross-platform, securing the physical log files requires a "defense-in-depth" approach tailored to each operating system's permission model. The goal is the same across all platforms: only the MariaDB service account should have read/write access, and only authorized administrators should have read access.

#### Implementation Pro-Tip: The Principle of Least Privilege

When setting up these logs, always remember that the MariaDB Service Account (for instance, `mysql` or `NT Service\MariaDB`) is the only entity that needs write access. Human administrators should only have read access, and only when necessary for troubleshooting.

## Summary of This Guide

By following this guide, you move from default, "open" logging to a hardened architecture:

* Logs are isolated on a dedicated partition.
* Access is restricted via OS-level permissions.
* Content is encrypted both on disk and over the wire.
* Retention is automated to prevent disk exhaustion.
* Activity is audited to detect tampering.

### Log Security Best Practices in a Nutshell

If you only have five minutes to harden your MariaDB logging environment, focus on these five pillars:

* Isolation: Move all log files (`log_error`, `general_log_file`, etc.) out of the default data directory and onto a dedicated, encrypted partition to prevent "Disk Full" stalls and unauthorized access.
* Encryption: Enable `encrypt_binlog = ON` to protect your data-at-rest and enforce `require_secure_transport = ON` to ensure log data-in-transit (replication) is wrapped in TLS/SSL.\
  **As of MariaDB 11.4**, TLS is enabled, even on a replication connection, by default (certificate-free TLS).
* Least Privilege: Restrict file-system permissions so that only the MariaDB service account can write to logs, and only high-level administrators can read them.
* Automated Rotation: Use `logrotate` (Linux) or scripts (Windows) for file-based logs, and `binlog_expire_logs_seconds` for binary logs to ensure you don't run out of storage.
* Integrity Monitoring: Use the MariaDB Audit Plugin to log any attempts to disable logging or modify security-sensitive system variables.

### Key Configuration Quick-Reference

| Feature             | Variable / Tool              | Recommended Setting             |
| ------------------- | ---------------------------- | ------------------------------- |
| At-Rest Encryption  | `encrypt_binlog`             | `ON`                            |
| In-Transit Security | `require_secure_transport`   | `ON`                            |
| Linux Permissions   | `chmod`                      | `660` for files; `750` for dirs |
| Log Retention       | `binlog_expire_logs_seconds` | `604800` (7 Days)               |
| Auditing            | `server_audit_events`        | `CONNECT, QUERY, TABLE`         |

## Securing Log Files at the OS Level

{% tabs %}
{% tab title="Linux" %}
On Linux, the MariaDB process usually runs under a dedicated `mysql` user and group.

* Ownership: Ensure the data directory and log files are owned by the `mysql` user.
  * `chown -R mysql:mysql /var/lib/mysql`
* Permissions: Use restrictive octal permissions. Log files should generally be `660` (read/write for user/group, nothing for others) and directories should be `750`.
  * `chmod 660 /var/lib/mysql/mariadb.log`
* AppArmor/SELinux: If your distribution uses these, ensure policies are defined so that even if the MariaDB process is compromised, it cannot write logs to unauthorized locations (like `/tmp`).
{% endtab %}

{% tab title="Windows" %}
Windows uses Access Control Lists (ACLs) which are more granular than Linux permissions.

* Service Account: MariaDB typically runs as `NetworkService` or a specific local user.
* Inheritance: Disable permission inheritance on the `data` folder to prevent "Authenticated Users" from browsing your logs.
*   Configuration: \
    1\. Right-click the log folder > Properties > Security > Advanced.

    2\. Remove _Everyone_ and _Users_.

    3\. Add the specific MariaDB service account with Full Control.

    4\. Add Administrators with Read/Execute.
{% endtab %}

{% tab title="macOS" %}
macOS follows a Unix-like permission structure similar to Linux, though the default user might be your local username if [installed via Homebrew](../../server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-on-macos-using-homebrew.md).

* Homebrew Path: Logs are often in `/opt/homebrew/var/mysql/`.
* Hardening: Use `chmod 700` on the log directory to ensure other local user accounts on the Mac cannot peek at your query history (which might contain sensitive data in plain text).
{% endtab %}
{% endtabs %}

## Sanitization of Backups

Logs are often backed up alongside data.

* Redaction: Be mindful that logs converted to `.sql` files for auditing (see [this example](securing-mariadb-logs.md#reading-log-files)) are now plain text and need to be deleted or encrypted immediately after use.
* Retention: Implement an automated purge policy ([`expire_logs_days`](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days)) to ensure sensitive data does not persist on disk longer than legally or operationally required.

## Changing the Log Location

As mentioned in the introduction, keeping logs on the same partition as your data is a security and availability risk (for instance, a "log bomb" filling up the disk and crashing the database).

To change the location, edit your `my.cnf` or `my.ini` file:

```ini
[mariadb]
# Example: Moving the Error Log
log_error = /var/log/mariadb/error.log

# Example: Moving the General Log
general_log_file = /var/log/mariadb/general.log
```

{% hint style="info" %}
When moving logs on Linux, you must manually create the new directory and set the ownership to `mysql` before restarting the service, or MariaDB will fail to start due to "Permission Denied."
{% endhint %}

{% hint style="info" %}
On **Linux**, adding `log_error` without specifying a location logs to the `systemd` journal. This is a viable alternative to the above, and even more secure than a log file on disk, since it cannot be changed by the MariaDB process.&#x20;
{% endhint %}

Because logs can grow indefinitely, an unmanaged log file is a security risk—not just for data exposure, but as a Denial of Service (DoS) vector. If a log file fills the storage partition, the MariaDB server will crash or hang.

## Log Rotation and Retention Strategies

Log rotation is the process of periodically archiving the current log file and starting a fresh one. This limits the size of individual files and allows for the automatic deletion of old data after a set period.

{% tabs %}
{% tab title="Linux" %}
### Linux: Using `logrotate`

On Linux, the standard way to handle this is the [`logrotate`](https://linux.die.net/man/8/logrotate) utility. It allows you to compress old logs (saving space) and set a retention policy (for instance, keep only the last 30 days).

A typical MariaDB `logrotate` configuration (usually found in `/etc/logrotate.d/mariadb`) looks like this:

{% code overflow="wrap" %}
```bash
/var/lib/mysql/*.log {
    daily
    rotate 30
    missingok
    compress
    sharedscripts
    postrotate
        # Tell MariaDB to close and reopen log files
        mariadb-admin --local flush-error-log  flush-engine-log flush-general-log flush-slow-log
    endscript
}
```
{% endcode %}

* `compress`: Encrypting logs is good, but compressing them is essential for storage.
* `postrotate`: This is critical. MariaDB holds a file handle on the log. If you move the file without telling MariaDB, it will keep writing to the old (now renamed) file. `flush-logs` forces it to start writing to the new filename.
{% endtab %}

{% tab title="Windows" %}
### Windows: Scripted Rotation

Windows does not have a native `logrotate` equivalent. Most administrators use a PowerShell script triggered by the Task Scheduler.

A basic security workflow for Windows logs:

1. Stop Logging: Briefly disable the log via SQL (`SET GLOBAL general_log = 'OFF';`).
2. Rename: Move `mariadb.log` to `mariadb_2026_02_25.log`.
3. Start Logging: Re-enable logging; MariaDB will automatically create a new, empty file.
4. Archive: Move the old file to a secure, long-term storage volume with restricted NTFS permissions.
{% endtab %}

{% tab title="Internal Rotation (Binary Logs)" %}
### MariaDB Internal Rotation (Binary Logs)

The Binary Log is unique because MariaDB manages its rotation internally. You should never use external tools like `logrotate` on binary logs, as it will break replication.

Instead, use these system variables in your configuration file:

* `max_binlog_size`: Defines the threshold at which a new file is created (default is 1GB).
* `binlog_expire_logs_seconds`: Defines how long (in seconds) MariaDB keeps binary logs before automatically deleting them.
{% endtab %}
{% endtabs %}

### Security Best Practices for Rotated Logs

* Off-site Logging: For high-security environments, don't just rotate logs locally. Use a logging agent (like [Fluentd](https://www.fluentd.org/) or [Logstash](https://www.elastic.co/logstash)) to stream logs to a centralized, hardened log server or a SIEM (Security Information and Event Management) system.\
  On Linux, an alternative is to log to systemd-journal-remote.
* Read-Only Archives: Once a log file is rotated/archived, change its permissions to Read-Only. There is no reason for the MariaDB process to have write access to a log from last month.
* Checksums: Periodically generate SHA-256 checksums of archived logs. This allows you to prove in an audit that the logs have not been tampered with since they were rotated.

## Securing Binary Log Files

Generally, the same security concepts and measures apply as for other log files. Here are some extra notes on binary log files and relay log files.

### Encryption at Rest

If your disk is compromised or a backup of the logs is stolen, raw binary logs are vulnerable.

* MariaDB Encryption: Enable the built-in MariaDB transparent encryption for binary logs. This ensures that even if someone copies a binary log file, they cannot decode it without the encryption keys.
* See detailed instructions for [encrypting binary logs](../encryption/data-at-rest-encryption/managing-binary-log-encryption.md).

### Securing Logs in Transit

When a replica connects to a primary server, it "pulls" binary log events. Without encryption, these events (which contain your raw SQL data) travel across the network in plain text.

Beyond the standard "use a strong password," there are three specific MariaDB security features you should definitely include to ensure log data isn't intercepted or faked during transmission.

{% hint style="info" %}
SSL/TLS: Always use encrypted connections for replication traffic to prevent "sniffing" of the log data as it moves across the network.
{% endhint %}

#### Mandatory TLS/SSL for Replication

The most critical step is ensuring the log data is wrapped in an encrypted tunnel. You can enforce this on the primary server so it rejects any replica trying to connect without a secure certificate.

*   Set `require_secure_transport = ON` globally, or specifically for the replication user:

    ```sql
    ALTER USER 'repl_user'@'%' REQUIRE SSL;
    ```
* This prevents "Man-in-the-Middle" (MITM) attacks where an attacker on the network could sniff the binary log stream to steal sensitive data.

#### Binary Log Checksums

While encryption protects against _reading_ the logs, checksums protect against _corruption_ or _tampering_ during the transfer.

* In your configuration file (`my.cnf` or `my.ini`), set the [`binlog_checksum`](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_checksum) variable: `binlog_checksum = CRC32`
* With that setting, the primary calculates a CRC32 hash for every event in the binary log. The replica verifies this hash before applying the event. If a packet is altered or corrupted during transit, the replica stops and reports an error rather than writing "junk" or malicious data to its database.

#### Master Key Rotation (for Encrypted Logs)

If you have enabled [`encrypt_binlog`](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#encrypt_binlog) `= ON`, you must consider how the encryption keys are handled during replication.

* Only the _file_ is encrypted on disk. When the log is read to be sent to a replica, it is decrypted by the primary and then re-encrypted by the network protocol (TLS).
* Security Tip: Ensure you are using a robust Key Management Service (KMS) plugin (like the AWS, [HashiCorp Vault](../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin.md), or [File Key Management](../encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin.md) plugins). Regularly rotating the Master Key ensures that, even if an old archived log file and an old key were somehow compromised, the current "live" logs remain secure.

#### Replica Side: Securing the Relay Log

Once the log data arrives at the replica, it is stored in Relay Logs before being executed.

* Security Risk: The replica's relay logs are just as sensitive as the primary's binary logs.
* Ensure `encrypt_binlog = ON` is also set on the replica. This ensures that the moment the log data hits the replica's disk, it is encrypted immediately.

To wrap up the technical documentation, we should address the "human element." Even with the best encryption and file permissions, simple configuration oversights can leave your logs vulnerable.

Here are the most common pitfalls to avoid when hardening MariaDB log security.

To finalize your security documentation, it is important to show users how to monitor the monitors. The MariaDB Audit Plugin is the gold standard for this, as it can track who accessed the server, what queries they ran, and—crucially—who attempted to change log settings.

## Audit Policy for Log Integrity

Unlike the General Log, the [Audit Plugin](../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-overview.md) allows for fine-grained filtering. This prevents your logs from becoming bloated while ensuring that any "meta-changes" to your security posture are recorded.

### **Enabling the Plugin**

First, the plugin must be installed and enabled. Add this to your configuration:

```ini
[mariadb]
plugin_load_add = server_audit
server_audit_logging = ON
server_audit_events = CONNECT,QUERY,TABLE
server_audit_file_path = /var/log/mariadb/audit.log
server_audit_file_rotate_size = 100M
server_audit_file_rotations = 5
```

### **Defining the Security Filter**

You don't want to log every `SELECT` statement, but you do want to log any attempt to disable logging or change security variables. You can filter for specific keywords.

* Filter for Sensitive Operations: You should monitor for any `SET GLOBAL` commands that affect security variables like `general_log`, `slow_query_log`, or `encrypt_binlog`.
* Filter for Privilege Changes: Use the `TABLE` event to track who is modifying the `mysql.user` or `mysql.general_log` tables.

### **Protecting the Audit Log Itself**

The `audit.log` is your "black box" recorder. It requires the highest level of protection:

* Immutable Bit (Linux): On high-security systems, you can use `chattr +a /var/log/mariadb/audit.log` to make the file append-only. Even the `mysql` user won't be able to delete or modify past entries, only add new ones.
*   Remote Syslog: Redirect the audit events to a remote, secure syslog server so that even if the local server is wiped, the audit trail persists.

    ```ini
    server_audit_output_type = SYSLOG
    server_audit_syslog_facility = LOG_LOCAL6
    server_audit_syslog_priority = LOG_INFO
    ```

### Summary Table: Who Watches the Watchmen?

| **Action**            | **Security Goal**                           | **Log Source**        |
| --------------------- | ------------------------------------------- | --------------------- |
| User Login/Logout     | Tracking access windows.                    | Audit Log (`CONNECT`) |
| Changing `log_output` | Detecting attempts to hide tracks.          | Audit Log (`QUERY`)   |
| Direct Table Edits    | Detecting tampering with `mysql.slow_log`.  | Audit Log (`TABLE`)   |
| System Errors         | Detecting "Log Bomb" or disk space attacks. | Error Log             |

## Verifying Your Security Setup

After restarting MariaDB with your new settings, run these queries to confirm the hardening is active.

### Confirm Data-at-Rest Encryption

To verify that your binary logs are actually being encrypted on the disk, check the global status of the encryption threads.

```sql
SHOW GLOBAL VARIABLES LIKE 'encrypt_binlog';
-- This should return 'ON'

SELECT * FROM INFORMATION_SCHEMA.INNODB_TABLESPACES_ENCRYPTION WHERE NAME='file_binlog';
-- This confirms the encryption plugin is actively managing the binlog files.
```

### Confirm Data-in-Transit Encryption (SSL/TLS)

If you are on a replica or a client machine, you can verify that your current connection is secure.

```sql
SHOW STATUS LIKE 'Ssl_cipher';
-- If this is empty, your connection is NOT encrypted. 
-- It should return a cipher suite like 'TLS_AES_256_GCM_SHA384'.

SHOW SESSION STATUS LIKE 'Ssl_version';
-- Ensures you are using a modern protocol (TLSv1.2 or TLSv1.3).
```

### Verify Log Destinations

Ensure the server is writing to the correct files (and not to tables, unless intended).

```sql
SHOW VARIABLES LIKE 'log_output';
-- Should return 'FILE'.

SHOW VARIABLES LIKE '%_log_file';
-- This lists the absolute paths for the Error, General, and Slow logs 
-- so you can verify they moved to your secure partition.
```

### Test the Audit Plugin

To ensure the "Black Box" is recording, perform a test action that should be caught by your filter (like changing a global variable), then check the log file.

```sql
-- Run a test change
SET GLOBAL slow_query_log = ON;

-- Then, from the OS terminal, check the audit log:
-- sudo tail /var/log/mariadb/audit.log
```

## Common Configuration Pitfalls

### Hardcoding Credentials in Configuration Files

When setting up replication or automated log rotation, it is tempting to put the username and password directly into the `[client]` or `[mariadb-dump]` sections of `my.cnf` or `my.ini`.

* This is risky since any user with read access to the config file (often world-readable by default in some environments) can steal the replication or administrative password.
* To close that loophole, use a [Secret Store](../../server-management/automated-mariadb-deployment-and-administration/a-comparison-between-automation-systems.md#storing-secrets) or restricted-access option files. If you must use a file, ensure its permissions are set to `400` or `600` and owned by the `mysql` user.

### Leaving the General Log Enabled in Production

The General Query Log records _every_ statement sent to the server.

* If an application sends sensitive data (like `INSERT INTO users (password) VALUES ('plain_text_pass')`), that password is now stored in plain text in your log file.
* Only enable the General Log during active debugging. For long-term auditing, use the MariaDB Audit Plugin, which allows you to filter exactly what is logged (for instance, only DDL changes) and mask sensitive information.

### Neglecting the Relay Log on Replicas

Don't just focus all security efforts on the primary server but leave the replicas wide open.

* The Relay Log on the replica contains a mirrored copy of the primary’s binary log. If an attacker gains access to the replica's file system, they have the same data access as if they had breached the primary.
* Always mirror your security settings (permissions, `encrypt_binlog`, and `log_error` locations) across the entire replication topology.

### Overlooking "Insecure Transport" Warnings

If you configure `REQUIRE SSL` for a user, but don't set [`require_secure_transport`](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#require_secure_transport) `= ON` globally, the server might still allow unencrypted connections from other users or administrative tools.

* This risks accidental "downgrade" attacks where a tool connects via a non-encrypted port, exposing log-related metadata.
* To close that loophole, explicitly disable non-TLS connections in the `[mariadb]` section of your configuration.

### Inadequate "Log Bomb" Protection

Failing to set a maximum size for your error logs or general logs.

* A flood of connection errors (perhaps from a brute-force attack) can cause the Error Log to balloon to hundreds of gigabytes, crashing the server by exhausting disk space.
* Always use `logrotate` (Linux) or a monitoring script (Windows) to alert you when log files exceed a specific percentage of disk capacity.

## Configuration Template

Here is a hardened `my.cnf` (Linux) or `my.ini` (Windows) template. This configuration applies the "Defense in Depth" principles, covering encryption, location, and transmission security. Adjust paths and filenames according to your environment.

```ini
# MariaDB Log Security Hardened Template
# Target: MariaDB 10.6+ 

[mariadb]
# --- 1. FILE LOCATIONS & AVAILABILITY ---
# Move logs to a dedicated, restricted directory
log_error           = /var/log/mariadb/error.log
general_log_file    = /var/log/mariadb/queries.log
slow_query_log_file = /var/log/mariadb/slow.log

# --- 2. DATA-AT-REST ENCRYPTION ---
# Requires a Key Management Plugin (e.g., file_key_management)
encrypt_binlog          = ON
encrypt_tmp_disk_tables = ON

# --- 3. DATA-IN-TRANSIT SECURITY ---
# Force all connections (including replication) to use TLS/SSL
require_secure_transport = ON
ssl_ca   = /etc/mysql/ssl/ca-cert.pem
ssl_cert = /etc/mysql/ssl/server-cert.pem
ssl_key  = /etc/mysql/ssl/server-key.pem

# --- 4. INTEGRITY & RETENTION ---
# Enable checksums to detect tampering or corruption during transit
binlog_checksum     = CRC32

# Set binary log expiration (e.g., 7 days in seconds)
# 7 days * 24h * 60m * 60s = 604800
binlog_expire_logs_seconds = 604800
max_binlog_size = 100M

# --- 5. OPERATIONAL HYGIENE ---
# Log warnings to the error log (useful for spotting failed login attempts)
log_warnings = 2

# Ensure the slow query log only captures what is necessary
long_query_time = 2.0
log_slow_admin_statements = ON
```

### Final Implementation Checklist for your Users

1. Directory Creation: Before restarting MariaDB with these settings, users must create the `/var/log/mariadb/` directory.
2. Permissions: Run `chown -R mysql:mysql /var/log/mariadb` and `chmod 750 /var/log/mariadb`.
3. Key Management: Remember that `encrypt_binlog = ON` requires an active encryption plugin; otherwise, the server will not start.

## Log File Security Checklist

| Security Category | Action Item                                           | Target Logs            | Platform      |
| ----------------- | ----------------------------------------------------- | ---------------------- | ------------- |
| Access Control    | Set permissions to `660` (Files) and `750` (Folders). | All Log Files          | Linux / macOS |
| Access Control    | Remove `Everyone` and `Users` groups from ACLs.       | All Log Files          | Windows       |
| Data Integrity    | Enable `encrypt_binlog = ON` in `my.cnf` or `my.ini`. | Binary / Relay Logs    | All           |
| Availability      | Move logs to a dedicated partition/volume.            | All Log Files          | All           |
| Availability      | Configure `logrotate` with `compress` enabled.        | Error / General / Slow | Linux         |
| Availability      | Set `binlog_expire_logs_seconds` for auto-purge.      | Binary Logs            | All           |
| Audit Trail       | Use `sha256sum` to baseline archived (rotated) logs.  | All Archives           | All           |
| Replication       | Require SSL/TLS for log transmission to replicas.     | Binary / Relay Logs    | All           |



