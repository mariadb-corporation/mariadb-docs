---
description: >-
  Download, prerequisites, and first run for the MySQL to MariaDB Migrator,
  including the self-bootstrapping Python environment and the interactive menu.
---

# Installation and First Run

{% hint style="info" %}
**MariaDB tool.** The MySQL to MariaDB Migrator is proprietary MariaDB software, provided free to MariaDB customers and partners under approved usage terms.
{% endhint %}

The MySQL to MariaDB Migrator is distributed as a release archive (`.tar.gz` or `.zip`) from the [MariaDB community downloads page](https://mariadb.com/downloads/community/). Download the latest version (for example, `v1.3.1-beta`), extract it, and run the launcher — it bootstraps its own Python environment, so there is no manual setup beyond the prerequisites below.

```bash
tar -xzf mariadb-migrator-<version>.tar.gz
cd Mysql-to-MariaDB-Migration-<version>
./mariadb-migrator
```

The `.zip` archive is equivalent: `unzip` it, then change into the extracted directory and run `./mariadb-migrator`. The version embedded in the archive and directory names matches the release you download.

The data-transfer engine `mariadb-mtk` used by [Parallel Restartable Streaming Copy](migrate-with-parallel-restartable-streaming-copy.md) is available from the same [MariaDB community downloads page](https://mariadb.com/downloads/community/). See [Prerequisites](#prerequisites) below.

## Prerequisites

### Required

* **MariaDB must be installed and running on the target host before you run the tool.** The migrator verifies the target version during preflight, but it does not install MariaDB.
* **Python 3.9 or later** on the host that runs the migrator. On the first run, the launcher creates a project-local virtual environment (`.venv`) and installs its Python dependencies into it automatically — no manual `pip install` is needed. On Debian and Ubuntu, install the venv module first: `sudo apt-get install -y python3-venv`.
* **The `mariadb` client** on the host that runs the migrator, used for connectivity, version, and database checks. If it is missing, the launcher detects your platform and offers to install it on the first run. You can also install it manually, for example with `dnf install mariadb`, `apt-get install mariadb-client`, `zypper install mariadb-client`, or `brew install mariadb`.
* **Network connectivity** from the host that runs the migrator to both the source MySQL server and the target MariaDB server. The exception is Offline Copy (`staged`) in its `dump_only` or `load_only` phase, which only needs connectivity to one side.
* For **[Parallel Restartable Streaming Copy](migrate-with-parallel-restartable-streaming-copy.md)** (`two_step`), the `mariadb-mtk` engine must be installed by extracting its release archive:

  ```bash
  tar -xzf mariadb-mtk-<version>_<x86_64/arm_64>_linux.tar.gz
  ```

  It is available from the [MariaDB community downloads page](https://mariadb.com/downloads/community/). Set the `SQLINESDATA_BIN` environment variable to the full path of the `mariadb-mtk` binary.

{% hint style="info" %}
`pv` is recommended for live progress visibility but is optional. When it is missing, [Offline Copy](migrate-with-offline-copy.md) (`staged`) falls back to a 60-second file-size probe and [Serial Streaming Copy](migrate-with-serial-streaming-copy.md) (`one_step`) falls back to a 60-second heartbeat.
{% endhint %}

### User Privileges

The tool expects valid privileges to already exist for the source and target admin users you provide (`SRC_ADMIN_USER` and `TGT_ADMIN_USER`). Each must be able to:

* Connect from the host that runs the migrator.
* Check, create, and drop target database objects as required by the workflow.
* Run dump and restore operations, and configure replication where applicable.

In practice this means admin-level privileges, including the ability to grant.

## First Run

On the first run, the launcher:

1. Creates a project-local virtual environment at `./.venv` (unless one is already active) and installs the Python dependencies into it. Your system Python is never modified.
2. Detects the `mariadb` client and, if it is missing, shows the correct install command for your platform and offers to run it. The optional `pv` tool is offered the same way, without blocking the run.
3. Presents the interactive menu.

Later runs reuse `./.venv` and go straight to the menu.

### Unattended and CI Hosts

The first-run prompts can be controlled with environment variables for unattended or CI hosts:

| Variable | Effect |
| --- | --- |
| `MIGRATOR_ASSUME_YES=1` | Accept install prompts automatically. |
| `MIGRATOR_NO_SYSTEM_INSTALL=1` | Never run system installs; print the commands only. |
| `MIGRATOR_NO_AUTO_VENV=1` | Do not auto-create `.venv`; print the manual venv steps and exit. |

## Next Steps

* [Migration Modes](migration-modes.md) — choose and run a migration mode.
* [Environment Variables](environment-variables.md) — the variables required to run each mode.
