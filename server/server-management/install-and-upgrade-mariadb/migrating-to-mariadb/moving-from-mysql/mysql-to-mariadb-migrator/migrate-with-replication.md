---
description: >-
  Migrate MySQL to MariaDB with minimal downtime using Replication: seed the
  target from a snapshot, replicate ongoing changes from the binlog, then cut over.
hidden: true
noIndex: true
noRobotsIndex: true
---

# Migrate a Database with Minimal Downtime Using Replication

This guide walks through a complete MySQL to MariaDB migration in **Replication** (`binlog`) mode. The migrator seeds the target from a consistent snapshot with embedded binlog coordinates, starts MariaDB replication from the MySQL binary log, and verifies it. The target then stays current with the source until you perform a short cutover.

This is the mode to use when downtime must be minimal. Unlike the offline modes, it does not finish in a single pass; it establishes ongoing replication that you cut over when you are ready.

{% hint style="info" %}
The migrator is in **beta**. Run this procedure against a non-production target first, and validate the result before you migrate a production database.
{% endhint %}

This guide uses the `sakila` sample database as the example. Substitute your own database name wherever `sakila` appears.

{% hint style="info" %}
**Following along with the sample?** `sakila` is MySQL's official sample database. Download it from the [MySQL example databases page](https://dev.mysql.com/doc/index-other.html), extract it, and load `sakila-schema.sql` then `sakila-data.sql` into your source server.
{% endhint %}

## Before You Begin

You need a source **MySQL 8.0 or 8.4** server and a target **MariaDB** server already installed and running. The host running the migrator needs network connectivity to both, and the target MariaDB must be able to reach the source MySQL directly, because the replica connects to the source to read its binary log.

You need **admin credentials** on both servers (not `root`, which is blocked by default), plus a **replication user** the migrator will use; you supply its name and password as `REPL_USER` and `REPL_PASS`, and the migrator creates it on the source if it does not exist. The migrator host needs **Python 3.9 or later** and the **`mariadb` client**.

### Source requirements

{% hint style="warning" %}
Replication requires `binlog_format=ROW` on the source and does not support schemas that contain JSON columns. Both conditions are enforced at the launcher, the assessment, and preflight, so a source with either is blocked upfront and routed to an offline mode. To use Replication, set `binlog_format = ROW` under `[mysqld]` in the source `my.cnf` and restart the source MySQL server.
{% endhint %}

A **MySQL 8.4** source additionally needs an upstream `mysqldump` 8.4 or later available, because 8.4 servers reject `SHOW MASTER STATUS`. An **8.0** source uses `mariadb-dump` directly and needs no extra client, which makes 8.0 the simpler source for this mode.

## Step 1: Download and Start the Migrator

Download the migrator release archive from the [MariaDB community downloads page](https://mariadb.com/downloads/community/) or the [GitHub releases page](https://github.com/mariadb-corporation/Mysql-to-MariaDB-Migration/releases), extract it, and run the launcher (example for `v1.3.1-beta`):

```bash
tar -xzf Mysql-to-MariaDB-Migration-1.3.1-beta.tar.gz
cd Mysql-to-MariaDB-Migration-1.3.1-beta
./mariadb-migrator
```

On the first run, the launcher creates a project-local Python environment (`.venv`) and checks for the `mariadb` client. Your system Python is never modified.

## Step 2: Preview with Assess & Plan

Choose **1) Assess & Plan**, supply the source and target connection details and the replication user when prompted, and select mode **4) Replication (binlog) [ONLINE]**. The assessment inventories the source and checks compatibility before anything is written. For Replication the decisive check is JSON columns: `sakila` has none, so the source clears the gate (the `binlog_format=ROW` requirement is confirmed when the migration runs).

```text
== Precheck runner ==
Host: mysql.example.com  Port: 3306  User: migadmin
---- mysql_version ----
8.0.46
---- json_columns ----
(no rows)
---- engines_summary ----
InnoDB	59
Precheck complete.
ASSESSMENT: PASS (see artifacts/report.json and run.log)
```

If the source has a JSON column, the assessment stops and lists the offending columns, then re-prompts for the database name(s) so you can drop or exclude the offending database and retry. If the JSON columns are ones you need to migrate, choose one of the offline modes instead.

## Step 3: Run the Migration

Start the launcher again, choose **2) Assess + Run**, and select Replication. The migrator first re-checks source compatibility with a Replication-specific preflight, then runs three steps: seed, start replication, and verify. Watch progress with `tail -f artifacts/run_binlog_<timestamp>/run.log`.

```text
==> Preflight checks (binlog)
Source MySQL: 8.0.46 (using: SHOW MASTER STATUS;)
Checking source schemas for JSON columns...
Checking source binary logging...
Checking source binlog format...
Checking source master/binary-log status visibility...
Preflight complete.
```

### Seed the target

A consistent snapshot is taken with `mariadb-dump --single-transaction --master-data=2`, which embeds the binlog coordinates, and is restored to the target. The coordinates are saved for the next step.

```text
==> Binlog migration: seed target from source snapshot
Source MySQL: 8.0.46  Dump tool: mariadb-dump
Creating source snapshot with binlog coordinates (--master-data=2)...
Restoring snapshot to target...
Seed completed.
```

```text
# binlog_coords.env
SRC_BINLOG_FILE=mysql-bin.000004
SRC_BINLOG_POS=66378596
```

### Start replication

The migrator ensures the replication user exists on the source (created `WITH mysql_native_password`, which cross-vendor replication requires), assigns the target a distinct `server_id` if it collides with the source, and points MariaDB at the captured coordinates.

```text
==> Binlog migration: configure and start replication
Ensuring replication user exists on source...
Applying replication coordinates: mysql-bin.000004:66378596
Replication started.
```

### Verify

The tool polls replication status until both threads are running and lag is within `BINLOG_MAX_LAG_SECS` (default 30).

```text
==> Binlog migration: verify replication
IO running: Yes
SQL running: Yes
Seconds behind master/source: 0
Replication verify passed.
```

There is no `ANALYZE TABLE` step in this mode, because replication keeps changing the tables after the seed.

## Step 4: Confirm Changes Are Flowing

The target is now live-following the source, so a write on the source appears on the target within seconds. Inserting one row on the source and reading it back on the target confirms the pipeline end to end:

```text
# on the source:
INSERT INTO sakila.film (title, language_id) VALUES ('LIVE REPLICATION TEST', 1);

# on the target, moments later:
+---------+-----------------------+
| film_id | title                 |
+---------+-----------------------+
|    1001 | LIVE REPLICATION TEST |
+---------+-----------------------+

# SHOW REPLICA STATUS on the target:
Master_Host: mysql.example.com
Seconds_Behind_Master: 0
```

## Step 5: Cut Over

The tool stops after verification with replication running; the cutover is yours to perform when you are ready. The migrator does not stop replication or repoint your application for you. A safe cutover:

1. Stop application writes to the source. Put the application in maintenance mode or revoke write access so no new transactions are generated.
2. Wait for zero lag. Confirm `Seconds_Behind_Master: 0` on the target with `SHOW REPLICA STATUS\G`, so every committed source change has been applied.
3. Stop replication on the target with `STOP REPLICA;`, then `RESET REPLICA ALL;` once you are committed, to clear the replication configuration.
4. Repoint the application at the target MariaDB server and resume traffic.
5. Clean up the replication user on the source and any infrastructure accounts that were migrated.

Downtime is only the window between stopping writes on the source and resuming them on the target, which is short because the target is already caught up before you begin.

## Reference

Beyond the common source and target variables, Replication requires `REPL_USER` and `REPL_PASS`. Optional variables include `SRC_BINLOG_FILE` and `SRC_BINLOG_POS` (auto-captured during the seed if unset), `BINLOG_MAX_LAG_SECS` (default 30), and `BINLOG_CREATE_REPL_USER` (default 1; set to 0 if the replication user already exists). See [Environment Variables](environment-variables.md) for the full list.

## Other Modes

If Replication does not fit your situation, see the [migrator overview](README.md) to choose another mode: [Serial Streaming Copy](migrate-with-serial-streaming-copy.md) or [Parallel Restartable Streaming Copy](migrate-with-parallel-restartable-streaming-copy.md) for an offline transfer when both servers are reachable, or [Offline Copy](migrate-with-offline-copy.md) when they are not.
