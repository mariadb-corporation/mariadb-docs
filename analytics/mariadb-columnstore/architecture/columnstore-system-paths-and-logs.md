---
description: >-
  MariaDB ColumnStore file system paths: where binaries, data files,
  configuration files, and logs are located, which paths can be configured
  with mcsSetConfig, and how to gather logs for support tickets.
---

# ColumnStore System Paths and Logs

## Overview

MariaDB ColumnStore installs its binaries, data files, configuration files, and logs into a fixed set of directories. This page describes where each type of file is located, which paths can be reconfigured (and how), and how to collect logs when working with MariaDB Support.

## Default File System Paths

| Type                | Default Path                              | Configurable                                          |
| ------------------- | ----------------------------------------- | ----------------------------------------------------- |
| Binaries            | `/usr/bin` (e.g., `mcsSetConfig`, `cpimport`, `PrimProc`) | No, set at build time                  |
| Storage engine plugin (`ha_columnstore.so`) | MariaDB plugin directory: `/usr/lib/mysql/plugin` (DEB) or `/usr/lib64/mysql/plugin` (RPM); shown by `SELECT @@plugin_dir` | No, set at build time |
| Configuration files | `/etc/columnstore`                        | No, set at build time                                  |
| Data files          | `/var/lib/columnstore`                    | Yes, in `Columnstore.xml` and `storagemanager.cnf`     |
| Logs                | `/var/log/mariadb/columnstore`            | Partially, see [Log Files](#log-files)                 |
| Temporary files     | `/tmp/columnstore_tmp_files`              | Yes, `SystemTempFileDir` in `Columnstore.xml`          |

The locations of the binaries, the plugin, the configuration directory, and the main log directory are compiled into ColumnStore at build time and cannot be changed on an installed system. The data, temporary, and bulk-load paths are runtime-configurable, as described below.

## Configuration Files

ColumnStore reads its configuration from `/etc/columnstore`:

| File                                  | Purpose                                                                                                 |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `/etc/columnstore/Columnstore.xml`    | Main configuration file for all ColumnStore components. Modify it with `mcsSetConfig`, not by hand.     |
| `/etc/columnstore/storagemanager.cnf` | Storage Manager configuration: chooses between local and S3-compatible object storage and sets the related cache, metadata, and journal paths. |
| `/etc/columnstore/cmapi_server.conf`  | Cluster Management API (CMAPI) configuration, including the API key and cluster node list. Present only when the CMAPI package (`mariadb-columnstore-cmapi`) is installed; CMAPI also provides the `mcs` command. |

MariaDB Server itself is configured separately, through `my.cnf` and the `*.cnf` files in the include directories it references. The exact locations depend on how the server was installed: RPM-based builds typically use `/etc/my.cnf` plus `/etc/my.cnf.d/`, while Debian-based builds typically use `/etc/mysql/` plus `/etc/mysql/mariadb.conf.d/`. Some installations have files in more than one of these directories; the authoritative way to see which files are actually read, and in what order, is:

```bash
mariadbd --help --verbose | grep -A1 'Default options'
```

ColumnStore installs its own server-side settings as a `columnstore.cnf` file in the relevant directory. This file holds the `plugin-load-add=ha_columnstore.so` line and the ColumnStore-related system variables (`columnstore_*`), alongside general server settings such as `log_error`. To confirm the effective server settings regardless of which files they came from, run:

```bash
my_print_defaults mysqld
```

{% hint style="info" %}
A timestamped snapshot of `Columnstore.xml` (for example, `Columnstore.xml-20260612`) is taken daily by `logrotate` and provides a history of recent configuration changes. Snapshots are written to the log archive directory, `/var/log/mariadb/columnstore/archive`; the retention is defined in `/etc/logrotate.d/columnstore`. In older ColumnStore versions, the snapshots were written to `/etc/columnstore` itself.
{% endhint %}

## Configurable Data Paths

### Columnstore.xml

The following path-related parameters in `Columnstore.xml` can be changed with [`mcsSetConfig`](#viewing-and-changing-configuration-with-mcsgetconfig-and-mcssetconfig):

| Section        | Parameter           | Default                                                | Description                                               |
| -------------- | ------------------- | ------------------------------------------------------ | --------------------------------------------------------- |
| `SystemConfig` | `DBRoot1` ... `DBRootN` | `/var/lib/columnstore/data1`                       | Location of a DBRoot. A DBRoot is a top-level storage location for ColumnStore data: a directory tree containing the segment files that hold [extents](columnstore-storage-architecture.md). A deployment can have multiple DBRoots (`DBRootCount` in total, one `DBRootN` parameter each), for example, on separate volumes; in a multi-node cluster, each DBRoot is owned by exactly one node at a time. |
| `SystemConfig` | `DBRMRoot`          | `/var/lib/columnstore/data1/systemFiles/dbrm/BRM_saves` | Prefix path for the Block Resolution Manager (BRM) files, including the extent map. |
| `SystemConfig` | `TableLockSaveFile` | `/var/lib/columnstore/data1/systemFiles/dbrm/tablelocks` | File in which active table locks are persisted.           |
| `SystemConfig` | `SystemTempFileDir` | `/tmp/columnstore_tmp_files`                            | Base directory for temporary files used by disk-based joins and aggregations. |
| `WriteEngine`  | `BulkRoot`          | `/var/log/mariadb/columnstore/data/bulk`                | Working directory for `cpimport` bulk loads: job descriptions, bulk-load logs, and rollback metadata. |

Two locations under the data directory are worth knowing when diagnosing problems:

* `/var/lib/columnstore/data1/systemFiles/dbrm/` holds the Block Resolution Manager files, including the extent map. Multiple save copies are kept (`BRM_savesA_*`, `BRM_savesB_*`), and `BRM_saves_current` records which copy is active.
* `/var/lib/columnstore/local/module` identifies the node within a cluster (for example, `pm1`). It is written by CMAPI when the node is configured; if the file is absent, the node is treated as `pm1`.

{% hint style="warning" %}
Do not change `DBRoot*`, `DBRMRoot`, or `DBRootCount` on a system that already contains data. These values define where ColumnStore finds its extents and extent map; changing them without physically relocating the data renders the system unusable. If you need to move data to another volume, stop ColumnStore, move the directories, update the parameters, and start ColumnStore again — or deploy with the desired paths from the start.
{% endhint %}

{% hint style="warning" %}
Be careful when changing `SystemTempFileDir`: on startup, ColumnStore deletes and recreates the subdirectories it uses below this path. Always point it at a dedicated directory, never at a shared location such as `/tmp` itself or a data directory.
{% endhint %}

### storagemanager.cnf

When ColumnStore uses S3-compatible object storage, the Storage Manager keeps its local working set under `/var/lib/columnstore/storagemanager`. The paths are set in `/etc/columnstore/storagemanager.cnf`:

| Section          | Parameter       | Default                                       | Description                                          |
| ---------------- | --------------- | --------------------------------------------- | ---------------------------------------------------- |
| `[ObjectStorage]` | `metadata_path` | `/var/lib/columnstore/storagemanager/metadata` | Object metadata describing which objects make up each file. |
| `[ObjectStorage]` | `journal_path`  | `/var/lib/columnstore/storagemanager/journal`  | Journal of pending writes not yet flushed to object storage. |
| `[Cache]`        | `path`          | `/var/lib/columnstore/storagemanager/cache`    | Local disk cache of downloaded objects.              |
| `[Cache]`        | `cache_size`    | `2g`                                          | Maximum size of the local disk cache.                |
| `[LocalStorage]` | `path`          | `/var/lib/columnstore/storagemanager/fake-cloud` | Directory used to emulate object storage in `LocalStorage` mode (testing only). |

Changes to `storagemanager.cnf` are made by editing the file directly and take effect after restarting ColumnStore.

## Viewing and Changing Configuration with mcsGetConfig and mcsSetConfig

Use the `mcsGetConfig` and `mcsSetConfig` utilities to read and modify `Columnstore.xml`. Both identify a setting by its section name and parameter name; `mcsSetConfig` additionally takes a value. By default they operate on `/etc/columnstore/Columnstore.xml`.

### mcsGetConfig

Displays the value of a configuration parameter:

```bash
mcsGetConfig [-vh] [-c config_file] section parameter
```

| Option | Description                                                                         |
| ------ | ----------------------------------------------------------------------------------- |
| `-c`   | Use an alternative configuration file instead of `/etc/columnstore/Columnstore.xml`. |
| `-a`   | Display all configuration values (the section and parameter arguments are not required). |
| `-i`   | Display all configuration values in `.ini`-file format (implies `-a`).               |
| `-v`   | Display verbose information.                                                         |
| `-h`   | Display help text.                                                                  |

### mcsSetConfig

Updates the value of a configuration parameter:

```bash
mcsSetConfig [-vdhx] [-c config_file] section parameter value
```

| Option | Description                                                                           |
| ------ | ------------------------------------------------------------------------------------- |
| `-c`   | Use an alternative configuration file instead of `/etc/columnstore/Columnstore.xml`.   |
| `-d`   | Skip checks and do not distribute the configuration file to other nodes after changes. |
| `-x`   | Delete the parameter from the section (a value is still required but ignored).         |
| `-v`   | Display verbose information.                                                            |
| `-h`   | Display help text.                                                                      |

Examples:

```bash
# Show the location of the first DBRoot
mcsGetConfig SystemConfig DBRoot1

# Show all current settings
mcsGetConfig -a

# Move the temporary file directory to a dedicated volume
mcsSetConfig SystemConfig SystemTempFileDir /data/columnstore_tmp_files

# Move the cpimport bulk-load working directory
mcsSetConfig WriteEngine BulkRoot /data/columnstore/bulk

# Allow disk-based joins (uses SystemTempFileDir for spill files)
mcsSetConfig HashJoin AllowDiskBasedJoin Y
```

Configuration changes take effect after ColumnStore is restarted:

```bash
mcs cluster restart
```

On a multi-node cluster, run `mcsSetConfig` on the primary node. The change is distributed to the other nodes unless `-d` is specified.

## Log Files

### ColumnStore Engine Logs

The ColumnStore processes (PrimProc, WriteEngineServer, DMLProc, DDLProc, controllernode, workernode) log through the system logger (`rsyslog` or `syslog-ng`) using the `local1` facility. The package installs a syslog rule set that splits messages by severity into files under `/var/log/mariadb/columnstore`:

| File                                          | Contents                              |
| --------------------------------------------- | ------------------------------------- |
| `/var/log/mariadb/columnstore/crit.log`       | Critical messages                     |
| `/var/log/mariadb/columnstore/err.log`        | Error messages                        |
| `/var/log/mariadb/columnstore/warning.log`    | Warning messages                      |
| `/var/log/mariadb/columnstore/info.log`       | Informational messages                |
| `/var/log/mariadb/columnstore/debug.log`      | Debug messages, including queries executed against ColumnStore |

These files are rotated daily by `logrotate` into `/var/log/mariadb/columnstore/archive`; the rotation schedule and retention are defined in `/etc/logrotate.d/columnstore`.

Because the log directory location is compiled in, relocating ColumnStore logs is done at the operating system level: adjust the installed syslog rules (for example, `/etc/rsyslog.d/49-columnstore.conf`) and the `logrotate` configuration, or mount the desired volume at `/var/log/mariadb/columnstore`.

### Bulk Load (cpimport) Logs

A `cpimport` run produces two kinds of output, in two different places.

**Per-job logs** are written to `/var/log/mariadb/columnstore/cpimport/`, one pair of files per job:

| File                                                  | Contents                                |
| ----------------------------------------------------- | --------------------------------------- |
| `/var/log/mariadb/columnstore/cpimport/Job_<id>.log`  | Progress and informational messages.    |
| `/var/log/mariadb/columnstore/cpimport/Job_<id>.err`  | Errors and warnings for the job.        |

**Working files** are kept under `BulkRoot` (by default `/var/log/mariadb/columnstore/data/bulk`). The directory contains these subdirectories, relative to `BulkRoot`:

| Subdirectory   | Contents                                                                       |
| -------------- | ------------------------------------------------------------------------------ |
| `job/`         | Generated job description files (`Job_<id>.xml`).                              |
| `tmpjob/`      | Temporary job files created while a job is being prepared.                      |
| `data/import/` | Default location searched for input data files when none is given by path.      |
| `rollback/`    | Rollback metadata used to undo a failed import.                                 |

When a load rejects rows, `cpimport` also writes two reject files per input file: a `.bad` file (the rejected rows) and a `.err` file (the reason each row was rejected). By default these go to `/var/log/mariadb/columnstore/cpimport/`; the location can be changed with the `cpimport -L` (`--errors-dir`) option.

### CMAPI and mcs Logs

When the CMAPI package is installed, the Cluster Management API and the `mcs` command-line tool write their own logs:

| File                                                    | Contents                                  |
| ------------------------------------------------------- | ----------------------------------------- |
| `/var/log/mariadb/columnstore/cmapi_server.log`         | CMAPI server log                          |
| `/var/log/mariadb/columnstore/mcs_cli.log`              | Log of `mcs` command-line tool activity   |
| `/var/log/mariadb/columnstore/shared_storage_monitor.log` | Shared storage monitor log              |

### System Log

Output from ColumnStore child processes that does not reach the files above is written to the general system log — `/var/log/messages` on RHEL-based systems or `/var/log/syslog` on Debian-based systems. Check it when a ColumnStore process fails to start or dies unexpectedly.

### Systemd Journal

Each ColumnStore process runs as a systemd service, so startup and shutdown messages are also available from the journal:

```bash
journalctl -u mcs-primproc
journalctl -u mcs-writeengineserver
journalctl -u mcs-controllernode
journalctl -u mcs-workernode@1
journalctl -u mcs-dmlproc
journalctl -u mcs-ddlproc
journalctl -u mcs-loadbrm
journalctl -u mcs-storagemanager        # only runs with S3/object storage
journalctl -u mariadb-columnstore-cmapi # only with the CMAPI package installed
```

`mcs-storagemanager` only starts when ColumnStore is configured for S3/object storage; on local-storage deployments the service stays inactive and has no journal output. Likewise, `mariadb-columnstore-cmapi` exists only when the CMAPI package is installed.

### MariaDB Server Error Log

Errors raised at the SQL layer (including ColumnStore plugin messages) go to the regular MariaDB Server [error log](https://mariadb.com/docs/server/server-management/server-monitoring-logs/error-log), configured with the [`log_error`](https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables#log_error) system variable.

## Gathering Logs for Support Tickets

When opening a support ticket, use `mcs review --logs` to collect all relevant logs and diagnostic information in one archive:

```bash
mcs review --logs
```

The `mcs` command is provided by the Cluster Management API (CMAPI) package, `mariadb-columnstore-cmapi`, and `mcs review` is available in ColumnStore 23.10.6 and later.

{% hint style="info" %}
If `mcs` is not present — because CMAPI is not installed, or on older versions — download and run the standalone [columnstore\_review.sh](https://github.com/mariadb-edwardstoever/columnstore_review) script that `mcs review` is based on. It provides the same `--logs` and `--path` options:

```bash
wget https://raw.githubusercontent.com/mariadb-edwardstoever/columnstore_review/main/columnstore_review.sh
bash columnstore_review.sh --logs
```
{% endhint %}

This creates a compressed archive named `<hostname>_<YYYY-MM-DD-HH-MM-SS>_logs.tar.gz` in `/tmp` containing:

* ColumnStore logs from `/var/log/mariadb/columnstore`, including archived and trace logs
* The journal output of every ColumnStore service
* The contents of `/etc/columnstore` (`Columnstore.xml`, `storagemanager.cnf`, `cmapi_server.conf`)
* The tail of the MariaDB Server error log, global variables, and global status
* System information: kernel limits, system logs, port status, and the installed service unit files

To write the archive to a different location, use `--path`:

```bash
mcs review --logs --path /mnt/diagnostics
```

Attach the resulting `.tar.gz` file to your support ticket. On a multi-node cluster, run the command on every node and attach all archives. If an archive is larger than 50 MB, upload it via the [MariaDB large file upload](https://mariadb.com/upload/) and mention the upload in the ticket.

`mcs review` without options runs a read-only health check (version, topology, storage, extent map, locks, open ports, and more) and writes its report to `/tmp/columnstore_review/<hostname>_cs_review.txt`; see `mcs review --help` for the full list of diagnostic options.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
