---
description: >-
  Migrate a large MySQL database to MariaDB with Parallel Restartable Streaming
  Copy, using the mariadb-mtk engine to load data through concurrent sessions.
hidden: true
noIndex: true
noRobotsIndex: true
---

# Migrate a Large Database with Parallel Restartable Streaming Copy

This guide walks through a complete MySQL to MariaDB migration in **Parallel Restartable Streaming Copy** (`two_step`) mode. The migrator dumps the schema first, loads the data in parallel through the `mariadb-mtk` engine, validates row counts, and finalizes the remaining objects.

This mode is for larger databases where a single serial transfer is too slow. It dumps the schema, then loads table data through multiple concurrent worker sessions, then applies triggers, routines, and events at the end.

{% hint style="info" %}
The migrator is in **beta**. Run this procedure against a non-production target first, and validate the result before you migrate a production database.
{% endhint %}

This guide uses the `employees` sample database, which is large enough (about 3.9 million rows across six tables) to show the parallel load and the row-count validation doing real work. Substitute your own database name wherever `employees` appears.

{% hint style="info" %}
**Following along with the sample?** `employees` is MySQL's sample database for larger datasets, from the [datacharmer/test_db](https://github.com/datacharmer/test_db) project. Clone it and load it into your source with `mysql -u root -p < employees.sql` from inside the repository directory.
{% endhint %}

## Before You Begin

You need a source **MySQL 8.0 or 8.4** server with the database you want to migrate, and a target **MariaDB** server already installed and running. The host running the migrator needs network connectivity to both servers.

You need **admin credentials** on both servers that can connect from the migrator host and create, drop, dump, and restore databases. Avoid `root`; the migrator blocks it by default. The migrator host needs **Python 3.9 or later** and the **`mariadb` client**.

The target must be **clean** for this mode: Parallel Restartable Streaming Copy does not resume across separate invocations, so if a target database already exists from a previous attempt, drop it before you start.

### The mariadb-mtk engine

This mode requires the `mariadb-mtk` data-transfer engine (the SQLines Data engine, invoked as `sqldata`). The other three modes do not use it. Download it from the [MariaDB community downloads page](https://mariadb.com/downloads/community/). The launcher auto-detects a `sqldata` or `sqlinesdata` binary on `PATH`; if it is installed elsewhere, set `SQLINESDATA_BIN` to its full path. The engine may ship a temporary evaluation license; use a production license before production runs.

## Step 1: Download and Start the Migrator

Download the migrator release archive from the [MariaDB community downloads page](https://mariadb.com/downloads/community/) or the [GitHub releases page](https://github.com/mariadb-corporation/Mysql-to-MariaDB-Migration/releases), extract it, and run the launcher (example for `v1.3.1-beta`):

```bash
tar -xzf Mysql-to-MariaDB-Migration-1.3.1-beta.tar.gz
cd Mysql-to-MariaDB-Migration-1.3.1-beta
./mariadb-migrator
```

On the first run, the launcher creates a project-local Python environment (`.venv`) and checks for the `mariadb` client. Your system Python is never modified.

## Step 2: Preview with Assess & Plan

Choose **1) Assess & Plan**, supply the source and target connection details when prompted, and select mode **2) Parallel Restartable Streaming Copy (sqldata) [OFFLINE]**. This phase checks connectivity and compatibility and writes its reports under `artifacts/assess_<timestamp>/` without touching the target. Review the assessment before running.

## Step 3: Run the Migration

Start the launcher again, choose **2) Assess + Run**, and select Parallel Restartable Streaming Copy. The run executes four steps in order: a schema-only dump, the parallel data load, row-count validation, and object finalization.

The schema is dumped in two parts. The pre-data DDL (tables, indexes, foreign keys) is loaded first, with triggers, routines, and events held back. Those post-data objects are applied during finalization rather than before the load, so a trigger cannot fire and re-insert rows while data is still streaming in.

Watch live progress with `tail -f artifacts/run_two_step_<timestamp>/run.log` from a second shell.

### How the parallel load behaves

The engine transfers the database with several concurrent sessions (the `-ss` value, default 4), working on different tables at once. In this run of `employees`, four sessions moved all six tables and 3.9 million rows transferred in about three seconds:

```text
Transferring database (4 concurrent sessions):
employees.departments  - Started (1 of 6, 1 chunk, session 1)
employees.dept_emp     - Started (2 of 6, 1 chunk, session 2)
employees.employees    - Started (4 of 6, 1 chunk, session 3)
employees.salaries     - Started (5 of 6, 1 chunk, session 4)
employees.titles       - Started (6 of 6, 1 chunk, session 1)
  Rows written:  3919015 (3.9M rows)
  Transfer time: 3.4 sec (1144238 rows/s, 134.9 MB, 39.4 MB/s)
```

That parallelism is across tables. The engine can also split a single large table into parallel chunks, but that is a separate, opt-in behavior: it is gated by `large_tables_parallel` (off in the shipped `sqldata.cfg`) and additionally requires the table to have an `AUTO_INCREMENT` column. The `employees` tables use composite primary keys with no `AUTO_INCREMENT`, so each table, `salaries` included, transfers as a single stream within its session, which is what the `1 chunk` markers show. To split one very large table across sessions, set `large_tables_parallel=yes` and ensure the table has an `AUTO_INCREMENT` column.

### Row-count validation

After the load, the tool validates source and target row counts per database using the engine's own validate command. This is a report, not a gate: the data transfer is the gate, so reaching validation means every database loaded successfully. A mismatch is recorded and surfaced but does not fail the migration.

```text
===== row-count validation: employees =====
  Total number of tables:         6
    With the different row count: 0
  Total number of rows:           3919015 in source, 3919015 in target
[employees] row counts OK (all tables equal)
==> Row-count validation: all selected database(s) match
```

Set `MIGRATOR_SKIP_ROWCOUNT_VALIDATE=1` to skip this step.

## Step 4: Verify the Result

When the run finishes, confirm the migration on the target. In this run the target `employees` matched the source exactly: 6 base tables and 2 views, with 300024 rows in `employees` and 2844047 in `salaries`. The views are part of the schema dump and are created before the data load; only triggers, routines, and events are applied during finalize.

```bash
mariadb -h mariadb.example.com -u migadmin -p -t -e "
  SELECT table_type, COUNT(*) FROM information_schema.tables
   WHERE table_schema='employees' GROUP BY table_type;
  SELECT COUNT(*) AS salaries FROM employees.salaries;"
```

## Restart Behavior

{% hint style="warning" %}
`mariadb-mtk` does not resume a load across separate invocations. An interrupted or failed run is restarted by dropping the target database, then re-running from a clean target. The launcher always starts a fresh run for this mode and reports a leftover target database as a conflict to drop.
{% endhint %}

Chunked loading is still restartable within a run: transient errors are retried automatically (`restart_attempts`, default 10). The no-resume limitation applies only across separate invocations.

## Constraint Checks During Load

By default the tool disables foreign-key checks on the target during the parallel load (`TWO_STEP_KEEP_FK_CHECKS=0`) so cross-table load order does not cause failures. If you keep them on and hit foreign-key or unique-constraint ordering errors, disable the checks on the target before the load and re-enable them after finalize. The tool does not toggle these for you in that case.

```sql
-- Before the load:
SET GLOBAL FOREIGN_KEY_CHECKS=0;
SET GLOBAL UNIQUE_CHECKS=0;
-- After finalize:
SET GLOBAL FOREIGN_KEY_CHECKS=1;
SET GLOBAL UNIQUE_CHECKS=1;
```

## After the Migration

Review the run reports under `artifacts/run_two_step_<timestamp>/`, rotate any default passwords from the user migration report, and remove infrastructure accounts that do not belong on the target. Repoint your application at the target MariaDB server once you have verified the data and credentials.

## Other Modes

If Parallel Restartable Streaming Copy does not fit your situation, see the [migrator overview](README.md) to choose another mode: [Serial Streaming Copy](migrate-with-serial-streaming-copy.md) for a smaller database, [Offline Copy](migrate-with-offline-copy.md) for hosts that cannot reach each other, or [Replication](migrate-with-replication.md) for a low-downtime cutover.
