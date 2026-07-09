---
description: >-
  Migrate MySQL to MariaDB with Offline Copy when the source and target are not
  network-reachable: dump to files on one host, transfer them, and load on
  another.
---

# Migrate with Offline Copy

This guide walks through a complete MySQL to MariaDB migration in **Offline Copy** (`staged`) mode. You dump the source database to compressed files with a manifest, move that directory to where the target lives, and load it there.

Offline Copy is the right mode when the source and target cannot reach each other directly, for example across an air gap or between separate networks, or when you simply want a verifiable checkpoint between the dump and the load. It uses the same `mariadb-dump` and `mariadb` tooling as Serial Streaming Copy, but writes to disk in between instead of streaming through a single pipe.

{% hint style="info" %}
The migrator is in **beta**. Run this procedure against a non-production target first, and validate the result before you migrate a production database.
{% endhint %}

This guide uses the `sakila` sample database as the example. Substitute your own database name wherever `sakila` appears.

{% hint style="info" %}
**Following along with the sample?** `sakila` is MySQL's official sample database. Download it from the [MySQL example databases page](https://dev.mysql.com/doc/index-other.html), extract it, and load `sakila-schema.sql` then `sakila-data.sql` into your source server.
{% endhint %}

## Before You Begin

You need a source **MySQL 8.0 or 8.4** server and a target **MariaDB** server already installed and running. Unlike the online modes, Offline Copy does not need a single host that can reach both: the dump phase needs only the source, and the load phase needs only the target. You do need a directory you can move between the two sides, with free space for the compressed dump.

You also need **admin credentials** on each server that can connect from the host running that phase and can dump or restore databases. Avoid `root`; the migrator blocks it by default.

The host that runs each phase needs **Python 3.9 or later** and the **`mariadb` client**. The launcher bootstraps its own Python environment and offers to install the client if it is missing. The optional `pv` tool improves progress visibility.

## Step 1: Download and Start the Migrator

See [Installation and First Run](installation-and-first-run.md) for details on downloading and installing the MariaDB Migrator.

## Step 2: Understand the Phases

Offline Copy is driven by the `STAGED_PHASE` setting, which selects which part of the migration runs:

* `dump_and_load` (default) runs the whole migration on a single host that can reach both the source and the target.
* `dump_only` dumps from the source to a directory of files and then exits. The target is untouched, and only source connectivity is needed.
* `load_only` loads existing dump files into the target. Only target connectivity is needed, and the database list comes from the manifest in the dump directory.

The two-host workflow below uses `dump_only` and `load_only`. If one host can reach both servers, you can run `dump_and_load` instead and skip the transfer step.

## Step 3: Dump on the Source

On the host that can reach the source, run the dump phase, pointing `STAGED_DUMP_DIR` at a directory you can move. `STAGED_CONFIRM_OFFLINE=1` acknowledges without an interactive prompt that writes to the source during the dump are not captured.

```bash
STAGED_PHASE=dump_only STAGED_DUMP_DIR=/mnt/transfer/dumps \
  STAGED_CONFIRM_OFFLINE=1 ./mariadb-migrator
```

The dump phase reports each database as it finishes and prints a summary:

```
==> Staged dump (mariadb-dump | pv | gzip > file, per database)
Source MySQL : 8.0.46
Dump tool    : mariadb-dump
Compress     : gzip
Databases    : sakila

==> Dumping: sakila
   sakila: 0:00:00 [================>          ]  51%
    [done] sakila: 702KB, 47685 approx rows, 0s

==> Staged dump complete.
    Databases : 1
    Total size: 702KB
    Manifest  : /mnt/transfer/dumps/manifest.txt
```

The directory now holds one compressed file per database (`sakila.sql.gz`) and a `manifest.txt` that records each database's SHA-256, byte size, and approximate row count:

```
# staged-migration-manifest v1
# source_host: mysql.example.com
# source_version: 8.0.46
# dump_tool: mariadb-dump
# database	filename	sha256	size_bytes	approx_rows
sakila	sakila.sql.gz	c1040adb994b9a6c85a1c777b2abba7ea19d5dd9f86cc53e5f3b09b971fc8720	718005	47685
```

## Step 4: Transfer the Dump

Move the dump directory to the target side by whatever transport your environment allows: `scp`, a shared volume, removable media, or an object-store bucket. The manifest travels with the dump files and is used to verify them at load time.

```bash
scp -r /mnt/transfer/dumps target-host:/mnt/load/
```

## Step 5: Load on the Target

On the host that can reach the target, run the load phase against the transferred directory:

```bash
STAGED_PHASE=load_only STAGED_DUMP_DIR=/mnt/load/dumps \
  STAGED_CONFIRM_OFFLINE=1 ./mariadb-migrator
```

The load phase reads the manifest, verifies each file's SHA-256 before loading it, loads each database, refreshes optimizer statistics with `ANALYZE TABLE`, and finalizes:

```
==> Preflight checks (staged)
Phase: load_only
Manifest: 1 database(s) — sakila

==> Loading: sakila (file: sakila.sql.gz)
    checksum: OK
    [done] sakila: loaded 702KB in 2s

==> Staged load complete.
```

## Step 6: Verify the Result

After the load, a finalize step compares the manifest against the target's `information_schema.tables`. It hard-fails on a missing or empty database and warns on row-count variance above the threshold:

```
==> Staged finalize (post-load sanity counts and manifest verification)
Per-DB verification:
  Database                 Exists    Tables  Source rows     Target rows     Variance
  ------------------------ --------- ------- --------------- --------------- --------
  sakila                   OK        16      ~47685          ~47375          -0.7%

==> Staged finalize complete.
    Databases verified: 1
```

The -0.7% variance is expected. Both row counts are InnoDB sampled estimates from `information_schema`, not exact `COUNT(*)` results, so small differences are normal and do not indicate data loss. The checksum verified during load is the authoritative file-integrity check. For an exact check, run `SELECT COUNT(*)` on a few tables on both servers.

## After the Migration

Review the run reports under `artifacts/run_staged_<timestamp>/`, rotate any default passwords recorded in the user migration report, and remove replication, monitoring, or backup accounts that do not belong on the target. Repoint your application at the target MariaDB server once you have verified the data and credentials.

## Known Limitations

{% hint style="warning" %}
Offline Copy does not capture writes made to the source during the dump. For a consistent cutover, stop application traffic to the source before the dump and resume it on the target only after the load completes. If downtime is unacceptable, use [Replication](migrate-with-replication.md) instead.
{% endhint %}

{% hint style="warning" %}
Target-side TLS certificate verification is not yet configurable. Connections to TLS-required targets, such as MariaDB Cloud, are encrypted but not verified against a trusted CA. Source-side TLS works as expected through `SRC_SSL_MODE`.
{% endhint %}

Per-database load resume is not supported. If a multi-database load fails partway, drop the partially loaded databases on the target and re-run with `STAGED_PHASE=load_only`.

## Reference

The dump phase accepts tuning variables including `STAGED_PARALLEL` (concurrent per-database dumps, default 4), `STAGED_COMPRESS` (gzip on by default), and `STAGED_FINALIZE_VARIANCE_PCT` (the warning threshold, default 50). See [Environment Variables](environment-variables.md) for the full list.

## Other Modes

If Offline Copy does not fit your situation, see the [migrator overview](./) to choose another mode: [Serial Streaming Copy](migrate-with-serial-streaming-copy.md) for a single-pipe transfer when both servers are reachable, [Parallel Restartable Streaming Copy](migrate-with-parallel-restartable-streaming-copy.md) for large databases, or [Replication](migrate-with-replication.md) for a low-downtime cutover.
