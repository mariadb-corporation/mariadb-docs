---
description: >-
  The four MySQL to MariaDB Migrator modes — Serial Streaming Copy, Parallel
  Restartable Streaming Copy, Offline Copy, and Replication — and how to run them.
---

# Migration Modes

{% hint style="info" %}
**Enterprise tooling.** The MySQL to MariaDB Migrator is proprietary MariaDB software, available to MariaDB customers and partners under approved usage terms. It is not open source and is not available for general public use.
{% endhint %}

The MySQL to MariaDB Migrator offers four migration modes. This page describes how to select a mode and the playbook for each one. For the variables each mode requires, see [Environment Variables](environment-variables.md).

## Selecting a Mode

Run the launcher interactively:

```bash
./mariadb-migrator
```

It first offers two top-level choices:

* **Assess & Plan** — inspect the source and target, validate connectivity and compatibility, and produce an assessment report and a migration plan. No data is moved.
* **Assess + Run** — assess the source, then proceed to the full migration (plan and run), with confirmation steps between phases.

It then presents the four modes as a numbered menu:

```
Select a migration mode:

  1) Serial Streaming Copy (mariadb-dump)            [OFFLINE]
  2) Parallel Restartable Streaming Copy (sqldata)   [OFFLINE]
  3) Offline Copy (mariadb-dump)                     [OFFLINE]
  4) Replication (binlog)                            [ONLINE]
```

The assess, plan, and run phases are also reachable non-interactively with the `--assess`, `--plan`, and `--run` flags; run `./mariadb-migrator --help` for the full list. Command-line flags bypass the menu.

{% hint style="info" %}
The internal mode identifiers — `one_step`, `two_step`, `staged`, and `binlog` — are the canonical form used in the configuration file, the `MODE` environment variable, and the `--mode <id>` command-line option.
{% endhint %}

## Serial Streaming Copy (`one_step`)

Best for smaller databases and standard maintenance windows.

* Uses `mariadb-dump` on the source and streams directly to the target `mariadb` client.
* A single pipe transfers tables sequentially, giving a predictable memory and network profile with no concurrency tuning.
* Supports a single database (`SRC_DB`) or multiple databases (`SRC_DBS="db1,db2"`).
* Strips `DEFINER` clauses by default to avoid permission errors on the target.
* Shows live progress through `pv` when available, and falls back to a 60-second heartbeat otherwise.

## Parallel Restartable Streaming Copy (`two_step`)

Best for larger datasets or tighter migration windows. This mode requires the `mariadb-mtk` engine (see [Installation and First Run](installation-and-first-run.md)).

The mode runs in stages: a schema-only dump first, then a parallel data load through `mariadb-mtk`, a post-load row-count validation, and finally an object-finalization step for triggers, routines, and events. `mariadb-mtk` uses multiple concurrent worker sessions per database for the data phase.

### Restart Behavior

Restartable, chunked loading is native to `mariadb-mtk` and on by default. Large tables (by default those with 1,000,000 or more rows) are loaded as parallel chunks, and transient errors are retried automatically within a run. Chunking requires an `AUTO_INCREMENT` column; tables without one transfer as a single stream.

`mariadb-mtk` does not resume a load across separate invocations. An interrupted or failed `two_step` run is restarted by dropping the target database or databases and re-running from a clean target. The launcher always starts a fresh run for this mode and reports a leftover target database as a conflict to drop.

### Disabling Constraint Checks During the Data Load

If you hit foreign key or unique-constraint ordering errors during the parallel data load, run the following on the **target** MariaDB before starting the load:

```sql
SET GLOBAL FOREIGN_KEY_CHECKS=0;
SET GLOBAL UNIQUE_CHECKS=0;
```

After the object-finalization step completes, re-enable both:

```sql
SET GLOBAL FOREIGN_KEY_CHECKS=1;
SET GLOBAL UNIQUE_CHECKS=1;
```

This is a manual DBA step performed with an account that can set global variables — the migrator does not toggle these globals automatically.

### Row-Count Validation

After the parallel data load completes successfully, the migrator validates row counts between the source and the target for each migrated database, using `mariadb-mtk`'s own validation command.

This is a post-load **report, not a gate**. The data transfer itself is the gate: a failed load stops the run before validation is reached, so reaching validation means every database transferred successfully. A row-count mismatch is recorded and surfaced, but does not fail the migration. Each database's per-table comparison and summary are written to both the per-database load log and the run log, and a concise verdict per database is echoed to the console. Set `MIGRATOR_SKIP_ROWCOUNT_VALIDATE=1` to skip the validation entirely.

## Offline Copy (`staged`)

Best when the source and target are not directly network-reachable, or when you want a checkpoint between the dump and the load.

This mode is phase-driven through the `STAGED_PHASE` variable:

* `dump_and_load` (default) — full end-to-end migration from source to target.
* `dump_only` — dump from the source to a directory of files, then exit; the target is untouched.
* `load_only` — load existing dumps into the target; no source connection is needed, and the database list comes from the dump manifest.

Other characteristics:

* Per-database compressed dumps (`<db>.sql.gz`) are written under the run directory by default, or to a custom location set with `STAGED_DUMP_DIR`.
* A manifest tracks each database's SHA-256 hash, byte size, and approximate row count. By default each dump file's integrity is verified against this hash before it is loaded.
* Per-database dump parallelism is configurable (`STAGED_PARALLEL`, default `4`); loads run sequentially by default.
* A post-load finalize step compares the manifest against the target's `information_schema.tables`. It hard-fails on missing or empty databases and warns on row-count variance above a configurable threshold (`STAGED_FINALIZE_VARIANCE_PCT`, default 50%). Both source and target counts are InnoDB sampled estimates, so small variance is expected and does not indicate data loss.

### Dump Now, Load Later on Another Host

```bash
# On the source host:
STAGED_PHASE=dump_only STAGED_DUMP_DIR=/mnt/transfer/dumps ./mariadb-migrator

# Transfer the directory:
scp -r /mnt/transfer/dumps target-host:/mnt/load/

# On the target host:
STAGED_PHASE=load_only STAGED_DUMP_DIR=/mnt/load/dumps ./mariadb-migrator
```

{% hint style="warning" %}
Offline Copy does not capture writes made to the source during the dump. If downtime is unacceptable, use Replication (`binlog`) instead.
{% endhint %}

{% hint style="warning" %}
Target connections negotiate TLS where the server requires it (for example, MariaDB Cloud), but server-certificate verification on the target side is not yet configurable: connections are encrypted in transit but not authenticated against a trusted CA. Source-side TLS verification works as expected through `SRC_SSL_MODE`.
{% endhint %}

## Replication (`binlog`)

Best for low-downtime cutover.

* Seeds the target from a consistent dump snapshot with embedded binlog coordinates, then starts MariaDB replication from the MySQL binary log using the `REPL_USER` and `REPL_PASS` credentials.
* Verifies replication thread health and lag after replication starts.
* For MySQL 8.4 sources, an upstream `mysqldump` 8.4 or later must be available, because 8.4 servers reject `SHOW MASTER STATUS`. The migrator detects this and fails fast at preflight.

{% hint style="warning" %}
**Replication requires `binlog_format=ROW` on the source and does not support schemas that contain JSON columns.** Both conditions are checked upfront — at the launcher, the assessment, and preflight — and an operator with either configuration is blocked and routed to one of the offline modes, which are unaffected by these limitations. To use Replication, set `binlog_format = ROW` under `[mysqld]` in the source `my.cnf` and restart the source MySQL server.
{% endhint %}

## Post-Load Optimizer Statistics

After a dump-and-restore, the target's optimizer statistics are empty or stale, which can lead to poor query plans until they are refreshed. The migrator can run [`ANALYZE TABLE`](../../../../../reference/sql-statements/table-statements/analyze-table.md) across the migrated databases on the target as a final step, so the optimizer has accurate statistics immediately.

A prompt — `Run ANALYZE TABLE on target after load? (y/n)` — appears during setup, just after the application-user prompt. It defaults to `y` and is shown only for the modes where a fresh load occurs: Serial Streaming Copy (`one_step`), Parallel Restartable Streaming Copy (`two_step`), and Offline Copy (`staged`). It is not part of Replication (`binlog`), where replication keeps changing the tables after the seed.

* Set `ANALYZE_TARGET=0` (or answer `n`) to skip it.
* The step is skipped automatically when Offline Copy runs as `dump_only`, because no load happens on that host.
* A connection failure to the target stops the run; an `ANALYZE TABLE` error on an individual table is reported but does not fail the migration.
* A report listing the tables analyzed, status counts, and any per-table errors is written to the run's artifacts directory.

## Notes and Limitations

* The migration fails by default if the target database already exists. Set `ALLOW_TARGET_DB_OVERWRITE=1` only when an overwrite is intentional. (For `staged` `load_only`, the database list comes from the manifest, and the same overwrite check applies before the load begins.)
* `root` source and target users are blocked by default; set `ALLOW_ROOT_USERS=1` to allow them.
* Offline Copy per-database load resume is not supported. If a multi-database load fails partway through, drop the partially loaded databases on the target and re-run with `STAGED_PHASE=load_only`.
* The migrator is built and tested for Linux on x86-64 and ARM64. Validate it in your target environment before production use.
