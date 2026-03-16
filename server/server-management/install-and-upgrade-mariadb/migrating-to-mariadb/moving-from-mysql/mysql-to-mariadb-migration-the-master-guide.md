---
description: >-
  Mastering the MySQL to MariaDB transition? This guide covers migrations from
  MySQL 5.7, 8.0, and 8.4 LTS to MariaDB 11.4/12.3, featuring a full
  Compatibility Matrix and safe dump/restore workflows.
---

# MySQL to MariaDB Migration: The Master Guide

{% hint style="info" %}
#### Environment Scope

This guide focuses on **migrations within Linux-based environments** (RHEL/CentOS/Alma, Debian/Ubuntu, etc.), as these represent the vast majority of production MySQL and MariaDB deployments.
{% endhint %}

## **⚡ Pro Tip: Automated Migration**

If you prefer an automated approach, MariaDB provides an open-source migration script that handles data dumping, user porting, and configuration checks in a single workflow.

* Tool: [Mysql-to-MariaDB-Migration Script](https://github.com/mariadb-corporation/Mysql-to-MariaDB-Migration) (GitHub)
* How to use it: If this script successfully completes your migration, you can skip the manual steps outlined in the rest of this page.

**⚠️ Limitations & Considerations**

While the script simplifies the process, be aware of the following:

* Large Databases: For databases in the hundreds of gigabytes or terabytes, the script's "all-in-one" nature can make it difficult to resume if a network timeout occurs. In these cases, the manual workflow (logical migration – dump and restore) is often preferred for better granular control.
* Complex Permissions: If you have highly custom or non-standard `GRANT` structures, the script may require manual intervention. Always verify your user privileges after the script completes.
* Environment Support: Ensure your source and target servers have the necessary dependencies (like Python/Bash and network connectivity) as specified in the script's `README` file.

## Preparation

### **Pre-Migration Checklist**

Before touching the production server, verify these requirements:

* Operating System: Ensure your OS is not End-of-Life (EOL). If you are on an aging system (like RHEL 7), consider a "new server" migration rather than an "in-place" upgrade.
* Version Target: Identify your destination.
  * _Coming from MySQL 5.7?_ MariaDB 10.11 LTS or 11.4 LTS are safe harbors with the longest remaining support runways.
  * _Coming from MySQL 8.0/8.4?_ MariaDB 11.4 LTS or the new 12.3 LTS are recommended. These versions have the most modern feature parity (window functions, CTEs, etc.) required for 8.x-era applications.
* Compatibility Check: Review the [MySQL to MariaDB Compatibility Matrix](mysql-to-mariadb-compatibility-matrix.md) for potential high-impact differences in authentication and SQL syntax.

#### **Automated Configuration Migration**

If you are moving to MariaDB 11.4 LTS or later, you can automate the transition of your configuration files. The `mariadb-migrate-config-file` utility (technical preview at the time of writing this, March 2026) scans your existing MySQL `my.cnf` or `my.ini` and generates a MariaDB-compatible version, automatically handling renamed or deprecated variables.

### **Mandatory Backup**

Never start a migration without two types of backups:

1. Physical/Binary Backup: A copy of the `/var/lib/mysql` directory (while the server is stopped). This allows for the fastest "undo" if the binary swap fails.
2.  Logical Backup: A full dump of your data. (Use the MySQL `mysqldump` program, not MariaDB's `mariadb-dump`, because the latter hasn't been extensively tested against MySQL.)

    <pre class="language-bash" data-overflow="wrap"><code class="lang-bash"># The Universal Master Dump Command
    mysqldump --user=root --password --all-databases \
    --single-transaction --routines --events \
    --triggers --hex-blob > migration_dump.sql
    </code></pre>

### Porting Users and Privileges

Standard data dumps often fail to capture complex user permissions correctly when moving from MySQL 8.0+. Instead of migrating the entire `mysql` system database, use these scripts on your MySQL source server to generate the exact SQL commands needed to recreate your users and their permissions on MariaDB.

#### Generate User Creation Script

This script extracts all non-system users and automatically handles the conversion of the `caching_sha2_password` plugin to the MariaDB-compatible `mysql_native_password`.

{% code overflow="wrap" %}
```sql
SELECT CONCAT('CREATE USER IF NOT EXISTS ''', user, '''@''', host, ''' IDENTIFIED WITH ''', 
  IF(plugin='caching_sha2_password', 'mysql_native_password', plugin), ''' AS ''', authentication_string, ''';') 
AS _sql FROM mysql.user WHERE user NOT IN ('root', 'mysql.sys', 'mysql.session', 'mysql.infoschema');
```
{% endcode %}

#### Generate Privilege (GRANT) Script

Run this next to generate the necessary `GRANT` statements for all database, table, and procedure-level permissions.

```sql
SELECT CONCAT('SHOW GRANTS FOR ''', user, '''@''', host, ''';') AS _sql FROM mysql.user 
WHERE user NOT IN ('root', 'mysql.sys', 'mysql.session', 'mysql.infoschema');
```

> How to use: Copy the output (the generated SQL lines) from these queries and execute them on your new MariaDB instance after the data migration is complete.

{% hint style="info" %}
#### Notes on those steps (scripts generation)

* The `root` exclusion: Notice we exclude the `root` user. This is a safety feature so you don't accidentally overwrite your new MariaDB root account with old MySQL credentials and lock yourself out.
* Plugin Mapping: The `IF` statement is doing a "on-the-fly" translation of MySQL's new password format back to a format MariaDB can read.
{% endhint %}

### **Proactive SQL Validation**

If your application is mission-critical:

* Enable the General Query Log on your MySQL server for a period of time to capture real-world traffic.
* Replay those queries against a MariaDB test instance.
* Check the MariaDB error log for any "Syntax Error" or "Unknown Function" messages. This prevents surprises on migration night.

## Logical Migration (Dump and Restore)

The Logical Migration is the "Gold Standard" for safety. It is the best choice if you are moving to a new server, a different Linux distribution, or a cloud-managed environment.

By exporting the data into a SQL script, you effectively "filter" out any binary-level incompatibilities between MySQL and MariaDB.

A logical migration involves exporting your data into a text-based SQL file (a "dump") and importing it into a fresh MariaDB instance. This is the safest way to ensure data integrity, as it completely recreates your tables and indexes in the MariaDB format.

{% stepper %}
{% step %}
### Export Data from MySQL

On your existing MySQL server, create a complete dump of all databases, including stored procedures, triggers, and events. (Note this is the same dump command used in the Preparation step, so you can use that one instead of re-creating it.)

```bash
# The Universal Master Dump Command
mysqldump --user=root --password --all-databases \
--single-transaction --routines --events \
--triggers --hex-blob > migration_dump.sql
```

* `--single-transaction`: Ensures a consistent backup without locking your tables (for InnoDB).
* `--hex-blob`: Properly handles binary data like images or encrypted strings.
* `--routines` and `--events` ensures that the "logic" of the database moves, not just the "rows".

#### **Alternative: Direct Network Streaming (The Pipe Method)**

If you have limited disk space or a high-speed network connection between your servers, you can "stream" the data directly from the MySQL source to the MariaDB target. This avoids creating a large intermediate `.sql` file on your local disk.

{% code overflow="wrap" %}
```bash
mysqldump --user=root --password --all-databases --single-transaction --routines --events --triggers --hex-blob | mariadb --host=new_server_ip --user=root --password
```
{% endcode %}

> Pro Tip: To monitor the progress of your transfer in real-time, install the `pv` (Pipe Viewer) utility and insert it into the command: `mysqldump ... | pv | mariadb ...`
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
### **Character Set & Collation Validation**

MySQL 8.0 uses `utf8mb4_0900_ai_ci` as its default collation. This specific collation is not supported by MariaDB. During a logical migration, MariaDB will typically map this to `utf8mb4_unicode_ci` or `utf8mb4_general_ci`.

While the data will import correctly, this change can affect how your application performs joins or sorts data. If you notice unexpected behavior or performance drops in specific queries, verify your collations:

{% code overflow="wrap" %}
```sql
-- Check for collation issues in your migrated database
SHOW GLOBAL VARIABLES LIKE 'collation%';
SHOW  VARIABLES LIKE 'collation%';
SELECT table_schema, table_name, column_name, collation_name FROM information_schema.columns WHERE collation_name IS NOT NULL and table_schema not in('information_schema','performance_schema','mysql','sys') ORDER BY table_schema, table_name;
```
{% endcode %}

Check if you have queries that may lead to a mismatch error when joining 2 columns with different collations. Alter your table or database to use the same collation across all your databases. See [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) and [ALTER DATABASE](../../../../reference/sql-statements/data-definition/alter/alter-database.md) for details.

{% hint style="info" %}
#### Why this matters

If a user has one table set to the old MySQL default and another table set to a MariaDB default, a `JOIN` between them might suddenly stop using indexes because of the "collation mismatch." This snippet gives them the SQL command to find the problem immediately.
{% endhint %}
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

{% step %}
### Security Hardening: Transition to PARSEC

For migrations to MariaDB 11.4 LTS and later, consider transitioning your users to the PARSEC authentication plugin. While `mysql_native_password` is supported for compatibility, PARSEC is the modern successor designed for significantly stronger password hashing and better long-term security.

```sql
-- Example: Update a user to use PARSEC
ALTER USER 'app_user'@'localhost' IDENTIFIED VIA parsec USING PASSWORD('secure_password');
```
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

Q: Can I perform an in-place upgrade (binary swap)? A: No. MariaDB stores metadata (table structures etc.) in individual `.frm` files. In contrast, MySQL removed `.frm` files in MySQL 8.0, replacing it with a global data dictionary. If you stop a MySQL 8.0/8.4 server and point MariaDB binaries at that data directory, MariaDB will look for `.frm` files to understand what tables exist. Since those files no longer exist in MySQL 8.0+, MariaDB will see an "empty" data directory or throw critical errors. It has no way to read MySQL's new internal dictionary tables.

Q: Can I perform an in-place upgrade for MySQL versions prior to 5.7? After all, those versions still use .frm files instead of a global data dictionary. A: In theory, that's possible, but in practice, you shouldn't do that either. Those old MySQL versions are built for operating systems like RHEL 6 which are out of support. You'd end up on an unsupported version of the operating system, on which you shouldn't install supported versions of MariaDB.

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

