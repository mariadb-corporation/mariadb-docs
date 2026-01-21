# Upgrading MariaDB Enterprise ColumnStore (Alpha)

{% hint style="info" %}
This page documents an Alpha version of the upgrade procedure using the `mcs install_es` command. Behavior may change. Validate in a non‑production environment first.
{% endhint %}

This guide explains how to upgrade MariaDB Enterprise Server (ES) and MariaDB Enterprise ColumnStore _across all nodes_ in a cluster using the unified `mcs` command-line tool that you have to run only once.

{% hint style="info" %}
The `mcs` command must be run as `root`. Either become `root`, or prefix the `mcs` commands on this page with `sudo`.
{% endhint %}

The `mcs install_es` command:

* Validates your MariaDB Enterprise Repository access using an ES API token.
* Stops ColumnStore and MariaDB services in a controlled sequence.
* Installs/configures the ES repository for the target version.
* Creates a pre‑upgrade backup of ColumnStore DBRM and config files on each node.
* Upgrades MariaDB Enterprise Server, ColumnStore, and CMAPI.
* Waits for CMAPI to come back online on each node and, for upgrades, automatically restarts services.

## Prerequisites

* Administrative privileges on all cluster nodes (package installation and service management required).
* A valid ES API token with access to the MariaDB Enterprise Repository.
* Network access from the nodes to the MariaDB Enterprise Repository endpoints.
* A maintenance window: the upgrade will stop ColumnStore and MariaDB services.
* Recent backups:
  * At a minimum, ensure Extent Map and configuration backups exist.
  * Recommended: take a full backup with the `mcs backup` command.

Related docs:

* [Extent Map backup and recovery](extent-map-backup-recovery.md)
* General backup and restore guidance: [ColumnStore Backup and Restore](column-store-backup-and-restore/)

{% hint style="danger" %}
Always back up your data before upgrading. While the tool performs a pre‑upgrade backup of DBRM and configs, it is not a substitute for a full database backup.
{% endhint %}

## Command Overview

The command can target a specific ES version, or use the latest tested version (currently latest 10.6 version).

* Install latest tested version (if you omit the `--version` option, `mcs` uses the latest version):

```console
mcs install_es --token <ES_API_TOKEN> --version latest
```

* Install a specific version:

```console
mcs install_es --token <ES_API_TOKEN> --version <ES_VERSION>
```

* Proceed even if nodes report different installed package versions (use the majority version as baseline):

```console
mcs install_es --token <ES_API_TOKEN> --version <ES_VERSION> --ignore-mismatch
```

Options summary:

* `--token TEXT`: ES API Token to use for the upgrade (required) — get it [from here](https://customers.mariadb.com/downloads/token/).
* `-v, --version TEXT`: ES version to install; if omitted or set to `latest`, upgrades to the latest tested version.
  * For a different version, specify something like `--version 10.6.23-19` or `--version 11.4.8-5` .
* `--ignore-mismatch`: Continue even if cluster nodes report different package versions; uses majority versions as the baseline.

## Before you Begin

* Stop or pause write workloads and heavy ingestion (e.g., `cpimport`, large `INSERT`/`LOAD DATA` jobs).
* Drain or put traffic managers/proxies (for example, MaxScale) into maintenance/drain mode.
* Ensure you have administrative/SSH and package manager access on all nodes.
* Verify time synchronization across all nodes (NTP/Chrony) to avoid coordination issues.
* Confirm recent backups are complete and restorable.

## What mcs install\_es Does

{% stepper %}
{% step %}
Validate token and target version.

* If `--version=latest`, the tool resolves the latest tested ES version.
* If a specific version is requested, it is validated against the repository. Some versions could exists only for specific operating systems.
{% endstep %}

{% step %}
Stop services.

* Gracefully stops the ColumnStore cluster.
* Stops the MariaDB server.
{% endstep %}

{% step %}
Configure repository.

* Installs/configures the MariaDB Enterprise Server repository for the chosen version on each node automatically.
* Validate installed repo on each node separately
{% endstep %}

{% step %}
Pre‑upgrade backups (per node).

Creates a backup of DBRM and key configuration files with name `preupgrade_dbrm_backup` in default backup directory.
{% endstep %}

{% step %}
Upgrade packages (per node).

* Upgrades MariaDB Enterprise Server and ColumnStore packages.
* Upgrades CMAPI and waits for it to become ready again on each node (up to 5 minutes).
{% endstep %}

{% step %}
Service handling after upgrade.

* On upgrades: automatically restarts MariaDB and the ColumnStore cluster.
* On downgrades: automatic restarts are intentionally skipped; manual steps are required.
{% endstep %}
{% endstepper %}

## Post-Upgrade Checks

* Run `mcs cluster status` to verify all services are up and the cluster is healthy. In case of a failure:
  * Verify CMAPI readiness on all nodes (for example, via `mcs` or an external monitoring tool).
* Run a quick smoke test:
  * Create a small ColumnStore table, insert a few rows, and run a `SELECT` query.
  * Check for errors in server/ColumnStore logs.
* Review `/var/tmp/mcs_cli_install_es.log` for the full sequence, and ensure no errors were reported.

## Downgrades

* Downgrades are supported up to MariaDB 10.6.9-5 and ColumnStore 22.08.4.
* When downgrading, the tool doesn't automatically restart services. Complete these steps manually:
  1. Start MariaDB on each node (for example, via your service manager).
  2. Start the ColumnStore cluster (for example, using the `mcs cluster start` command).
  3. Verify cluster health before resuming traffic.

{% hint style="danger" %}
Downgrades can cause data loss or cluster inconsistency if not planned and validated. Always test and ensure backups are restorable.
{% endhint %}

## Verification and Logs

After a successful upgrade, or after downgrading and a manual restart:

* Validate that CMAPI is ready on all nodes:\
   `mcs cmapi is-ready`
* Check ColumnStore and MariaDB services are running and the cluster is healthy:\
  `mcs cluster status`

The `mcs install_es` command writes a detailed run log to:

* `/var/tmp/mcs_cli_install_es.log`

If CMAPI readiness times out or services do not start cleanly, review:

* CMAPI logs: `/var/log/mariadb/columnstore/cmapi_server.log`
* Service logs on each node: `/var/log/mariadb/columnstore/`
* The `install_es` log file (`/var/tmp/mcs_cli_install_es.log`) for the full sequence and any errors

## Known Issues and Limitations (Alpha/Beta)

* Mixed package versions across nodes.
  * If nodes report different installed versions of Server/ColumnStore/CMAPI, the command fails with a mismatch message.
  * You can force continuation with `--ignore-mismatch`; the tool uses the majority version per package as the baseline, but this carries risk—align versions whenever possible.
* CMAPI readiness timeout
  * After upgrading CMAPI, the command waits up to 300 seconds per node for readiness.
  * On slow nodes or constrained environments, this timeout may be insufficient, and the command  exits with a failure; verify services manually and adjust operational expectations.
* Downgrade restarts are skipped by design.
  * After a downgrade, automatic restarts are not performed; you must start MariaDB and the ColumnStore cluster manually and validate health.
  * ColumnStore skips automatic restarts, because it cannot guarantee that all the expected APIs endpoints exist or are backward-compatible.
* MaxScale maintenance handling not automated.
  * Transitioning MaxScale to maintenance/normal mode during upgrades is not automated at this time; manage traffic routing and maintenance state manually if applicable.
* Repository access and version validation.
  * Invalid tokens, network restrictions, or unsupported version strings can result in validation errors (for example, HTTP 422). Ensure the token has the correct entitlements and the requested version exists for your platform.
* Single‑node detection.
  * If no active nodes are detected, the tool falls back to localhost only; ensure this matches your topology.
* Downgrading to 22.08.4 (10.6.9-5) technically working but finished with known issues:
  * Got ERROR on waiting CMAPI ready. But in fact CMAPI starts and is working fine (check `mcs status` and `systemctl status mariadb-columnstore-cmapi` on each node).
  * If you try to run a `mariadb` command, you got an error due to unknown configuration flag. Tool forcing to save current config files while installing packages, and an older MariaDB version doesn't support never flag obviously. To fix it, remove this flag from the configuration file, or restore the configuration from last installed package.
* Tool currently supported limited packages.
  * Only `MariaDB-server` (and dependencies), `MariaDB-columnstore-engine` (MariaDB-plugin-columnstore) and `MariaDB-columnstore-cmapi` packages remove and install supported. So packages like MariaDB-backup currently not supported and should be upgraded/downgraded manually.

## Troubleshooting

* Re‑run with `-v/--verbose` to enable console debug logging.
* Inspect `/var/tmp/mcs_cli_install_es.log` for the complete sequence and API responses.
* If package repository installation fails, verify token validity and outbound access from all nodes.
* If CMAPI does not become ready, check service logs on each node.
* For mismatched node versions, align package versions before re‑running, or proceed with `--ignore-mismatch` , but only after assessing the risk.

## Environment and Network Requirements

* Cluster state: ColumnStore cluster should be healthy before starting.
* Node access: All nodes must be reachable (SSH/admin access) and responsive.
* Disk space: Ensure sufficient free space for package downloads and pre-upgrade backups.
* Internet access: Nodes must reach MariaDB Enterprise repositories (per your operating system).
* CMAPI communication: Port 8640 (default) must be reachable between nodes.
* Time sync: Keep NTP/Chrony synchronized across nodes.

### Additional Usage Example (Downgrade)

```console
mcs install_es --token <ES_API_TOKEN> --version 10.6.15-10
```

{% hint style="danger" %}
Downgrades can be destructive.
{% endhint %}

This prompts for confirmation. After downgrade, services are not restarted automatically; start MariaDB and the ColumnStore cluster manually and verify health.

## Recovery Procedures

If the upgrade fails or CMAPI does not become ready on all nodes:

1. Review the detailed log at `/var/tmp/mcs_cli_install_es.log` for errors.
2. Check service status on each node:
   * `systemctl status mariadb`
   * `systemctl status mariadb-columnstore-cmapi`
3. Verify network/ports (CMAPI 8640) and repository reachability.
4. Manually start services if safe to do so:
   * `systemctl start mariadb`
   * `mcs start` (or `mcs cluster start`)
5. If corruption is suspected, follow your backup recovery plan (for example, restore from a recent backup and/or extent map backup).

## Best Practices

* Prior to upgrading:
  * Create a full backup and verify restore procedures.
  * Test the process in staging with similar topology/data.
  * Document current package versions and configs.
  * Schedule a maintenance window and inform stakeholders.
* During upgrading:
  * Monitor the console output and `/var/tmp/mcs_cli_install_es.log` .
  * Avoid interrupting the process; ensure network stability.
* After upgrading:
  * Validate services and cluster health (`mcs cluster status`).
  * Run basic data integrity and application smoke tests.
  * Monitor performance and logs for regressions.

## Support and Reporting Issues

Contact MariaDB Support if you encounter unexpected failures, data issues, or performance regressions. Provide:

* The complete log file: `/var/tmp/mcs_cli_install_es.log` .
* The `mcs` review logs: `mcs review --logs` .
* The exact command used (with parameters, masking sensitive values).
* Cluster topology (nodes, versions, operating system, network).
* Source and target versions (Server, ColumnStore, CMAPI).
* Exact error messages and timestamps.

## See Also

* Command reference: `mcs install_es` in the command-line tool help and tool README.
* Backups: `mcs backup` and Extent Map backup guidance.
* Cluster management: `mcs cluster start|stop|status` .

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
