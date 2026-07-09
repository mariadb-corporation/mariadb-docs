---
description: >-
  Migrate a MySQL database to MariaDB with Serial Streaming Copy: preview with
  Assess & Plan, run the migration, and verify the result on the target.
---

# Migrate with Serial Streaming Copy

This guide walks through a complete MySQL to MariaDB migration in **Serial Streaming Copy** (`one_step`) mode. You preview the migration with Assess & Plan, run it, and verify the result on the target.

Serial Streaming Copy is the most direct mode: it pipes `mariadb-dump` from the source straight into the `mariadb` client on the target, one table at a time. It needs no extra data-transfer engine and no replication setup, which makes it the right choice for a first migration and for smaller databases that can move within a standard maintenance window.

{% hint style="info" %}
The migrator is in **beta**. Run this procedure against a non-production target first, and validate the result before you migrate a production database.
{% endhint %}

This guide uses the `sakila` sample database as the example. Substitute your own database name wherever `sakila` appears.

{% hint style="info" %}
**Following along with the sample?** `sakila` is MySQL's official sample database. To set it up on your source server, download the archive from the [MySQL example databases page](https://dev.mysql.com/doc/index-other.html), extract it, and load the two files:

```bash
mysql -u root -p < sakila-schema.sql   # tables, views, routines, triggers
mysql -u root -p < sakila-data.sql     # data
```

See the [Sakila documentation](https://dev.mysql.com/doc/sakila/en/) for the full schema. If you are migrating your own database instead, skip this step.
{% endhint %}

## Before You Begin

You need a source **MySQL 8.0 or 8.4** server with the database you want to migrate, and a target **MariaDB** server that is already installed and running. The migrator checks the target version but does not install MariaDB. The host running the migrator needs network connectivity to both servers.

You also need **admin credentials** on both servers that can connect from the migrator host, create and drop databases, and run dump and restore operations. Avoid `root`; the migrator blocks `root` by default.

Finally, the migrator host needs **Python 3.9 or later** and the **`mariadb` client**. The launcher bootstraps its own Python environment and offers to install the client if it is missing. On Debian or Ubuntu, install the venv module first with `sudo apt-get install -y python3-venv`. The optional `pv` tool improves progress visibility during the transfer but is not required.

## Step 1: Download and Start the Migrator

See [Installation and First Run](installation-and-first-run.md) for details on downloading and installing the MariaDB Migrator.

On the first run, the launcher creates a project-local Python environment (`.venv`), installs its dependencies into it, and checks for the `mariadb` client. Your system Python is never modified, and later runs reuse `.venv` and go straight to the menu.

```
---------------------------------------------------------------------
 Welcome to the MySQL to MariaDB Migration Tool
 Tool Version: 1.3.1-beta (Build 20260622)
 Supported Sources: MySQL 8.0, 8.4
---------------------------------------------------------------------
==> Validating execution environment...
==> No active virtualenv detected. Creating one at ./.venv ...
Installing missing dependencies: typer click rich PyYAML
Successfully installed PyYAML-6.0.2 click-8.1.7 rich-13.7.1 typer-0.12.3 ...
==> Environment ready.
==> Checking system dependencies...
==> Database client found: /usr/bin/mariadb
==> pv found (dump progress will be shown).
==> System dependencies ready.

What would you like to do?
  1) Assess & Plan    Inspect source and target, validate connectivity and
                      compatibility, and produce an assessment report and the
                      migration plan. No data is moved.
  2) Assess + Run     Assess the source, then proceed to the full migration
                      (plan + run, with confirm steps between phases).
  q) Quit
```

## Step 2: Preview with Assess & Plan

Choose **1) Assess & Plan** for the preview. This phase never writes to the target. The migrator prompts for the connection details it needs:

| Prompt                       | Example value                        |
| ---------------------------- | ------------------------------------ |
| Source host / port           | `mysql.example.com` / `3306`         |
| Source admin user / password | `migadmin` / (entered at the prompt) |
| Source database              | `sakila`                             |
| Target host / port           | `mariadb.example.com` / `3306`       |
| Target admin user / password | `migadmin` / (entered at the prompt) |

Then select mode **1) Serial Streaming Copy (mariadb-dump) \[OFFLINE]**. The assess phase checks connectivity and source-to-target compatibility, inventories the schema, and writes its reports under `artifacts/assess_<timestamp>/`.

```
== Precheck runner ==
Host: mysql.example.com  Port: 3306  User: migadmin
---- mysql_version ----
8.0.46
---- json_columns ----
(no rows)
---- engines_summary ----
InnoDB	59
Precheck complete.
==> Assess application users on source
Roles found on source                : 0
Users with portable native password  : 0
Users requiring default password     : 0
Users that would be SKIPPED          : 0
ASSESSMENT: PASS (see artifacts/report.json and run.log)
```

Review the reports before you run the migration. The **assessment report** confirms connectivity and compatibility. The **`user_assessment_report.txt`** predicts which application users would be migrated with their password preserved, which would be reset to a default password, and which would be skipped. In this example the `sakila` source has no application accounts of its own, so the user counts are zero; on a real database this report lists exactly which users fall into each category. For how the migrator classifies users, see [Application User Migration](application-user-migration.md).

## Step 3: Run the Migration

Start the launcher again and choose **2) Assess + Run**, then select **1) Serial Streaming Copy** again. The migrator re-runs the assessment, then prompts for a few decisions before it moves any data.

The **`Migrate application users? (y/n)`** prompt controls whether application users and roles are migrated along with the data. If you answer `y`, the migrator also asks for a **`Default password for app users:`** used for any user whose original password cannot be carried over. The **`Run ANALYZE TABLE on target after load? (y/n)`** prompt defaults to `y`; it refreshes the target's optimizer statistics after the load so queries get good plans immediately.

The migrator then streams the data. Because Serial Streaming Copy is a logical dump and restore, it carries the full schema across: tables, views, stored procedures, functions, triggers, and events. It strips `DEFINER` clauses by default so those objects restore without permission errors on the target.

Output is captured to a run log rather than streamed to your terminal, and each phase prints a `tail -f` hint. To watch live progress, open a second shell and run `tail -f artifacts/run_one_step_<timestamp>/run.log`.

```
==> One-step migration (mariadb-dump | mariadb)
Source MySQL: 8.0.46  Dump tool: mariadb-dump
Source: mysql.example.com:3306  DB: sakila
Target: mariadb.example.com:3306
0:00:00 [ <=>                                                                  ]
One-step migration completed.
==> Post-load ANALYZE TABLE on target (refresh optimizer statistics)
    [done] sakila: 16 table(s) in 0s
RUN: PASS
```

The `pv` line is the live transfer heartbeat. For `sakila` the transfer finishes in under a second, so you see a single heartbeat; on a larger database `pv` prints a progress line every 10 seconds, and a 60-second heartbeat is used only when `pv` is not installed.

{% hint style="info" %}
By default the migration stops if the target database already exists, so an accidental overwrite cannot happen. To migrate into an existing database, set `ALLOW_TARGET_DB_OVERWRITE=1` before the run.
{% endhint %}

## Step 4: Verify the Result

When the run finishes, confirm the migration on the target. The run artifacts under `artifacts/run_one_step_<timestamp>/` include **`user_migration_report.txt`** (what happened to each user) and **`analyze_target_report.txt`** (the tables analyzed and any per-table errors).

```
# user_migration_report.txt
Roles created on target              : 0
Users migrated with original password: 0
Users migrated with default password : 0  <- PASSWORD EXPIRE set
Grants dropped (incompatible)        : 0

# analyze_target_report.txt
Databases analyzed   : 1  (sakila)
Tables analyzed      : 16
  status OK          : 16
Overall              : PASS
```

Then spot-check the data on the target and compare against the source:

```bash
mariadb -h mariadb.example.com -u migadmin -p \
  -e "SELECT COUNT(*) FROM sakila.film; SHOW TABLES FROM sakila;"
```

```
+----------+
| COUNT(*) |
+----------+
|     1000 |
+----------+
actor
address
category
... (16 base tables and 7 views)
```

Object fidelity is the important check for Serial Streaming Copy. On the migrated target, `sakila` has **16 base tables, 7 views, 6 stored routines, and 6 triggers**, matching the source, and the stored functions and procedures execute and return the same results as the source. Confirm the stored objects with:

```bash
mariadb -h mariadb.example.com -u migadmin -p -N -e "
  SELECT COUNT(*) FROM information_schema.routines WHERE routine_schema='sakila';
  SELECT COUNT(*) FROM information_schema.triggers WHERE trigger_schema='sakila';"
```

## After the Migration

Rotate any default passwords. A user that could not keep its original password was created with the default password you supplied and marked `PASSWORD EXPIRE`. That default is recorded in plain text in `user_migration_report.txt`, so treat the file as sensitive and rotate the password before re-enabling application traffic. This is common when migrating from MySQL 8.4, which defaults to `caching_sha2_password`.

Clean up infrastructure accounts. Replication, monitoring, and backup accounts are migrated as application users in this release; remove any that do not belong on the target. Once you have verified the data and credentials, repoint your application at the target MariaDB server.

## Run Without Prompts

For a scripted, non-interactive run, set the connection details as environment variables and the launcher skips the prompts:

```bash
MODE=one_step \
SRC_HOST=mysql.example.com SRC_PORT=3306 SRC_ADMIN_USER=migadmin SRC_ADMIN_PASS=... SRC_DB=sakila \
TGT_HOST=mariadb.example.com TGT_PORT=3306 TGT_ADMIN_USER=migadmin TGT_ADMIN_PASS=... \
./mariadb-migrator --run
```

See [Environment Variables](environment-variables.md) for the full list.

## Other Modes

If Serial Streaming Copy does not fit your situation, see the [migrator overview](./) to choose another mode: [Offline Copy](migrate-with-offline-copy.md) for hosts that cannot reach each other, [Parallel Restartable Streaming Copy](migrate-with-parallel-restartable-streaming-copy.md) for large databases, or [Replication](migrate-with-replication.md) for a low-downtime cutover.
