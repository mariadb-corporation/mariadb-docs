# MySQL to MariaDB Migration: The Master Guide

{% hint style="info" %}
#### Environment Scope

This guide focuses on **migrations within Linux-based environments** (RHEL/CentOS/Alma, Debian/Ubuntu, etc.), as these represent the vast majority of production MySQL and MariaDB deployments.
{% endhint %}

## Preparation

### **Pre-Migration Checklist**

Before touching the production server, verify these requirements:

* Operating System: Ensure your OS is not End-of-Life (EOL). If you are on an aging system (like RHEL 7), consider a "New Server" migration rather than an "In-Place" upgrade.
* Version Target: Identify your destination.
  * _Coming from MySQL 5.7?_ MariaDB 10.6 or 10.11 are the most stable "long-term" jumps.
  * _Coming from MySQL 8.0/8.4?_ MariaDB 10.11 or 11.4 are recommended for modern feature parity.
* Compatibility Check: Review the \[MySQL to MariaDB Compatibility Matrix] for potential high-impact differences in authentication and SQL syntax.

### **Mandatory Backup**

Never start a migration without two types of backups:

1. Physical/Binary Backup: A copy of the `/var/lib/mysql` directory (while the server is stopped). This allows for the fastest "undo" if the binary swap fails.
2.  Logical Backup: A full dump of your data.

    <pre class="language-bash" data-overflow="wrap"><code class="lang-bash">mariadb-dump --all-databases --user=root --password --single-transaction --routines --events > full_backup.sql
    </code></pre>

### **Proactive SQL Validation**

If your application is mission-critical:

* Enable the General Query Log on your MySQL server for a period of time to capture real-world traffic.
* Replay those queries against a MariaDB test instance.
* Check the MariaDB error log for any "Syntax Error" or "Unknown Function" messages. This prevents surprises on migration night.

## In-Place Upgrade (Binary Swap)

An in-place upgrade involves replacing the MySQL software with MariaDB while keeping your existing data directory (`/var/lib/mysql`) intact. This is the fastest method but carries the highest risk if a backup isn't prepared.

{% stepper %}
{% step %}
### Perform a Clean Shutdown

Before switching binaries, you must ensure that MySQL has flushed all pending changes from memory to the disk. A _fast_ shutdown can leave the data files in an inconsistent state that MariaDB might struggle to recover.

Log into your MySQL instance and run:

```sql
-- Ensure all InnoDB redo logs are flushed to disk
SET GLOBAL innodb_fast_shutdown = 0;
```

Then, stop the service:

```bash
sudo systemctl stop mysql
```
{% endstep %}

{% step %}
### Uninstall MySQL

Once the service is stopped, remove the MySQL packages. This process varies by your Linux distribution's package manager.

{% tabs %}
{% tab title="RHEL / Alma / Fedora" %}
{% code overflow="wrap" %}
```bash
sudo dnf remove mysql-server
```
{% endcode %}
{% endtab %}

{% tab title="Debian / Ubuntu" %}
{% code overflow="wrap" %}
```bash
sudo apt-get remove mysql-server
```
{% endcode %}
{% endtab %}
{% endtabs %}
{% endstep %}

{% step %}
### Install MariaDB

Install the MariaDB version you selected in Phase 1. Refer to the [Installation Guide](https://www.google.com/search?q=link-to-install-page\&authuser=1) for specific repository setup and package names.
{% endstep %}

{% step %}
### Upgrade the Configuration

MySQL 8.0 and 8.4 have removed many variables that MariaDB still uses, or renamed them. To prevent the MariaDB service from failing on its first start, use the Configuration Upgrade Helper (available in MariaDB 11.4+).

```bash
mariadb-cfg-upgrade-helper --config-file=/etc/my.cnf
```

This tool scans your configuration and provides a report on which variables need to be adjusted or renamed for compatibility.
{% endstep %}

{% step %}
### Start MariaDB and Initialize the Upgrade

Once your configuration is clean, start the MariaDB service. The server will start, but the internal system tables (the `mysql` database) will still be in the MySQL format.

```bash
sudo systemctl start mariadb
```

Immediately run the upgrade utility to convert the system tables and check all existing databases for compatibility:

```bash
sudo mariadb-upgrade -u root -p
```
{% endstep %}
{% endstepper %}

{% hint style="info" %}
#### Why these steps matter

* `innodb_fast_shutdown = 0`: This is your insurance policy. It guarantees the data files are "quiesced" (resting) and ready for a new engine.
* `mariadb-upgrade`: This is the most critical step. Without it, you might be able to read your user data, but your permissions, stored procedures, and views might behave erratically because the underlying system metadata hasn't been updated.
{% endhint %}

While the "In-Place" method is fast, the Logical Migration is the "Gold Standard" for safety. It is the best choice if you are moving to a new server, a different Linux distribution, or a cloud-managed environment.

By exporting the data into a SQL script, you effectively "filter" out any binary-level incompatibilities between MySQL and MariaDB.

## Logical Migration (Dump and Restore)

A logical migration involves exporting your data into a text-based SQL file (a "dump") and importing it into a fresh MariaDB instance. This is the safest way to ensure data integrity, as it completely recreates your tables and indexes in the MariaDB format.

{% stepper %}
{% step %}
### Export Data from MySQL

On your existing MySQL server, create a complete dump of all databases, including stored procedures, triggers, and events.

```bash
# Export everything to a single file
mysqldump --user=root --password --all-databases \
--single-transaction --routines --events \
--triggers --hex-blob > mysql_full_dump.sql
```

* `--single-transaction`: Ensures a consistent backup without locking your tables (for InnoDB).
* `--hex-blob`: Properly handles binary data like images or encrypted strings.
* `--routines` and `--events` ensures that the "logic" of the database moves, not just the "rows".
{% endstep %}

{% step %}
### Prepare the MariaDB Environment

On your new server, install MariaDB using the [Installation Guide for MariaDB Enterprise Server](../../installing-enterprise-server/) or the [Installation Guide for MariaDB Community Server](../../installing-mariadb/).

Before importing, ensure your MariaDB configuration (`my.cnf`) has enough resources to handle a large import.

* `max_allowed_packet`: Set this to at least `64M` or higher if you have large `BLOB` columns.
* `innodb_buffer_pool_size`: Temporarily increase this to 70-80% of available RAM to speed up index creation.
{% endstep %}

{% step %}
### Import Data into MariaDB

Transfer your `mysql_full_dump.sql` file to the new server and run the import:

```bash
# Import the data
mariadb -u root -p < mysql_full_dump.sql
```
{% endstep %}

{% step %}
### Finalize with `mariadb-upgrade`

Even with a logical dump, some system-level permissions or views might need a quick internal "refresh" to match the MariaDB structure.

```bash
sudo mariadb-upgrade -u root -p
```
{% endstep %}
{% endstepper %}

## Verification and Optimization

Once your data is moved (via either method), complete these three steps to ensure your new server is running at peak performance.

{% stepper %}
{% step %}
### Rebuild Optimizer Statistics

MariaDB uses a sophisticated cost-based optimizer that may differ from MySQL’s. To ensure your queries use the most efficient execution plans, force a fresh analysis of all tables:

```bash
# Run on all tables to refresh statistics
mariadb-admin -u root -p analyze
```

This makes the difference between a migration that "works" and a migration that "works fast".
{% endstep %}

{% step %}
### Check the Error Log

Check for any "Deprecated Variable" or "Ignored Option" warnings that might have appeared during startup.

```bash
sudo tail -f /var/log/mysql/error.log
```
{% endstep %}

{% step %}
### Application Smoke Test

Verify that your application can connect. Pay special attention to:

* Character Sets: Ensure your app and the server agree on `utf8mb4`.
* Temporary Tables: If your app uses heavy temporary table logic, verify performance.
{% endstep %}
{% endstepper %}

## Troubleshooting & FAQ

Even with careful preparation, migrations can encounter specific hurdles. Here are the most common issues and how to resolve them.

### Common Troubleshooting Scenarios

| Issue                                       | Likely Cause                      | Resolution                                                                                                                                                                      |
| ------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Access denied" for `root` after migration. | Authentication plugin mismatch.   | MySQL 8.0 `root` users often use `caching_sha2_password`. In MariaDB, use `ALTER USER 'root'@'localhost' IDENTIFIED VIA mysql_native_password USING PASSWORD('your_password');` |
| "Unknown system variable" on startup.       | MySQL-only variables in `my.cnf`. | Run `mariadb-cfg-upgrade-helper` to identify legacy variables. Common culprits: `innodb_log_file_size` (now dynamic) or removed SSL variables.                                  |
| "Table 'mysql.user' doesn't exist"          | Missing `mariadb-upgrade` step.   | The system tables must be converted. Run `sudo mariadb-upgrade -u root -p` immediately after starting the service.                                                              |
| Replication fails with "relay log" errors.  | GTID Incompatibility.             | MariaDB cannot use MySQL GTIDs. You must switch to position-based replication (File and Position) to link the two systems.                                                      |
| Slow queries after migration.               | Outdated optimizer statistics.    | MariaDB's optimizer needs fresh data. Run `ANALYZE TABLE` on all large tables or use `mariadb-admin analyze`.                                                                   |

## Frequently Asked Questions

Q: Can I go back to MySQL if the MariaDB migration fails? A: Yes, provided you took a physical backup (the `/var/lib/mysql` folder) before running `mariadb-upgrade`. Once `mariadb-upgrade` has modified the system tables, you cannot simply point MySQL binaries back at that data directory.

Q: Do I need to change my application's client libraries? A: Usually, no. MariaDB is protocol-compatible with MySQL. Your existing MySQL connectors (JDBC, PHP PDO, Python mysqlclient) will continue to work. However, for the best performance and features (like IAM authentication), switching to the [official MariaDB Connectors](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L/) is recommended.

Q: What about the JSON data type? A: Your `JSON` columns will be treated as `LONGTEXT` with a `CHECK` constraint. Your queries using `JSON_EXTRACT()` or the `->` operator will continue to work exactly as they did in MySQL.

Q: Is MariaDB 11.4 compatible with MySQL 8.4? A: Yes, for standard SQL and data. However, MySQL 8.4 removed many "legacy" behaviors that MariaDB still supports. If your app relies on those removed features, MariaDB is actually a _more_ compatible home for your code than MySQL 8.4.

## Further Reading

{% columns %}
{% column %}
{% content-ref url="mysql-to-mariadb-compatibility-matrix.md" %}
[mysql-to-mariadb-compatibility-matrix.md](mysql-to-mariadb-compatibility-matrix.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The reference guide companion page to the Migration Master Guide.
{% endcolumn %}
{% endcolumns %}

***

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-features" %}
[MariaDB versus MySQL - Features](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-features)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compare MariaDB vs. MySQL features. Learn about exclusive storage engines, speed enhancements and binary compatibility.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-compatibility" %}
[MariaDB versus MySQL - Compatibility](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-compatibility)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB Community Server release notes. Complete version history with features, bug fixes, and upgrade compatibility details for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/function-differences-between-mariadb-and-mysql" %}
[Function Differences Between MariaDB and MySQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/function-differences-between-mariadb-and-mysql)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Functions in MariaDB that are not present in MySQL, or vice versa.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/system-variable-differences-between-mariadb-and-mysql" %}
[System Variable Differences between MariaDB and MySQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/system-variable-differences-between-mariadb-and-mysql)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore system variable differences between MariaDB Rolling Release and MySQL 8.0. This section details how configuration options vary, aiding in compatibility and migration planning.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/replication-compatibility-between-mariadb-and-mysql" %}
[Replication Compatibility Between MariaDB and MySQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/replication-compatibility-between-mariadb-and-mysql)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes replication compatibility between MariaDB and MySQL.
{% endcolumn %}
{% endcolumns %}

