---
description: >-
  The environment variables required to run each MySQL to MariaDB Migrator
  mode, plus the common source, target, and optional tuning variables.
---

# Environment Variables

{% hint style="info" %}
**Enterprise tooling.** The MySQL to MariaDB Migrator is proprietary MariaDB software, available to MariaDB customers and partners under approved usage terms. It is not open source and is not available for general public use.
{% endhint %}

The migrator reads its configuration from environment variables (or the configuration file it writes from your interactive answers). This page lists the variables **required** to run each mode. A complete reference of every variable, with defaults and descriptions, ships with the tool.

{% hint style="info" %}
The interactive launcher prompts for any required input that is not already set, so you do not have to export these variables by hand. Set them explicitly for scripted or unattended runs.
{% endhint %}

## Common Variables

Most modes share the same source and target connection variables:

| Variable | Purpose |
| --- | --- |
| `SRC_HOST`, `SRC_PORT` | Source MySQL host and port. |
| `SRC_ADMIN_USER`, `SRC_ADMIN_PASS` | Source admin credentials. |
| `SRC_DB` or `SRC_DBS` | A single source database, or a comma-separated list. |
| `TGT_HOST`, `TGT_PORT` | Target MariaDB host and port. |
| `TGT_ADMIN_USER`, `TGT_ADMIN_PASS` | Target admin credentials. |
| `SRC_SSL_MODE` | Optional source TLS mode (`DISABLED`, `PREFERRED`, `REQUIRED`, `VERIFY_CA`, or `VERIFY_IDENTITY`) for TLS-required sources. |

## Serial Streaming Copy (`one_step`)

Requires the common source and target variables above. Optional:

* `ANALYZE_TARGET` — `1` by default; runs [`ANALYZE TABLE`](../../../../../reference/sql-statements/table-statements/analyze-table.md) on the target after the load to refresh optimizer statistics. Set to `0` to skip. (Applies to `one_step`, `two_step`, and `staged`.)

## Parallel Restartable Streaming Copy (`two_step`)

Requires the common source and target variables. Optional:

* `SQLINESDATA_BIN` — full path to the `mariadb-mtk` binary; auto-detected from a `sqldata` or `sqlinesdata` binary on `PATH`.
* `MIGRATOR_SKIP_ROWCOUNT_VALIDATE` — set to `1` to skip the post-load row-count validation.

## Replication (`binlog`)

Requires the common source and target variables, plus:

* `REPL_USER`, `REPL_PASS` — replication credentials.

Optional:

* `SRC_BINLOG_FILE`, `SRC_BINLOG_POS` — binlog coordinates; auto-captured during the seed if not set.
* `BINLOG_COORD_FILE` — where captured coordinates are written (default: `artifacts/binlog_coords.env`).
* `BINLOG_MAX_LAG_SECS` — replication lag threshold in seconds (default: `30`).

## Offline Copy (`staged`)

The phase selector and connection requirements depend on the phase:

* `STAGED_PHASE` — `dump_and_load` (default), `dump_only`, or `load_only`.
* Source variables are required for `dump_and_load` and `dump_only`.
* Target variables are required for `dump_and_load` and `load_only`.

Dump and load tuning (all optional):

| Variable | Default | Purpose |
| --- | --- | --- |
| `STAGED_DUMP_DIR` | run directory | Dump location; required for `load_only` to point at the manifest directory. |
| `STAGED_COMPRESS` | `1` | Gzip-compress the dump. |
| `STAGED_PV` | `1` | Show a progress meter through `pv` or the fallback probe. |
| `STAGED_PARALLEL` | `4` | Concurrent per-database dumps. |
| `STAGED_LOAD_PARALLEL` | `1` | Concurrent per-database loads. |
| `STAGED_VERIFY_CHECKSUM` | `1` | Verify each dump file's integrity before load. |
| `STAGED_DISK_HEADROOM_FACTOR` | `2` | Multiplier on the source data size for the free-space check. |
| `STAGED_FINALIZE_VARIANCE_PCT` | `50` | Row-count variance threshold above which finalize warns. |
| `STAGED_CONFIRM_OFFLINE` | — | Set to bypass the interactive offline-acknowledgment prompt for non-interactive runs. |

## Run-Control Variables

These apply across modes:

| Variable | Purpose |
| --- | --- |
| `MODE` | Selects the mode (`one_step`, `two_step`, `staged`, or `binlog`) for non-interactive runs. |
| `ALLOW_TARGET_DB_OVERWRITE` | Set to `1` to allow migrating into an existing target database. |
| `ALLOW_ROOT_USERS` | Set to `1` to allow `root` as a source or target admin user. |
| `FORCE_NEW_RUN` | Set to `1` to force a fresh run instead of resuming a previous one. |
