---
description: >-
  The MySQL to MariaDB Migrator automates end-to-end MySQL to MariaDB
  migrations — schema, data, users, and validation — in four selectable modes.
---

# MySQL to MariaDB Migrator

{% hint style="info" %}
**MariaDB tool.** The MySQL to MariaDB Migrator is proprietary MariaDB software, provided free to MariaDB customers and partners under approved usage terms. It is distributed from the [MariaDB community downloads page](https://mariadb.com/downloads/community/).
{% endhint %}

The **MySQL to MariaDB Migrator** is a MariaDB tool that automates end-to-end migrations from MySQL to MariaDB in a repeatable, auditable way. It orchestrates schema migration, data transfer, user and privilege migration, and post-migration validation, and it drives the standard MariaDB client tools (`mariadb-dump`, the `mariadb` client, and the `mariadb-mtk` data-transfer engine) under a single launcher.

{% hint style="info" %}
The migrator is currently in **beta**. All four migration modes have been exercised end-to-end against representative source and target pairs, including AWS RDS sources and MariaDB Cloud targets. Validate it in your own environment before a production migration.
{% endhint %}

The migrator complements the manual workflows in the [MySQL to MariaDB Migration: The Master Guide](../mysql-to-mariadb-migration-the-master-guide.md): the Master Guide explains the migration paths and the compatibility considerations, while the migrator automates the dump, load, user-migration, and validation steps for you.

## Supported Versions

* **Source:** MySQL 8.0 and 8.4 (some modes have version-specific requirements — see [Migration Modes](migration-modes.md)).
* **Target:** supported MariaDB Enterprise and Community editions.
* **MariaDB Cloud** is validated as a target for the Offline Copy (`staged`), Parallel Restartable Streaming Copy (`two_step`), and Serial Streaming Copy (`one_step`) modes.
* **Platforms:** the migrator is built and tested for Linux on x86-64 and ARM64.

## Migration Modes at a Glance

The launcher presents four migration modes as a numbered menu. The internal identifier in parentheses is the canonical form used in configuration files, environment variables (`MODE=...`), and the command line (`--mode <id>`).

| Mode | Internal ID | Type | Best For |
| --- | --- | --- | --- |
| Serial Streaming Copy | `one_step` | Offline | Smaller databases and standard maintenance windows |
| Parallel Restartable Streaming Copy | `two_step` | Offline | Larger datasets that need schema-then-parallel-data loading |
| Offline Copy | `staged` | Offline | Source and target not network-reachable, or a deferred / two-host load |
| Replication | `binlog` | Online | Low-downtime cutover with ongoing replication |

See [Migration Modes](migration-modes.md) for the detailed playbook for each.

## How the Tool Runs

When launched interactively, the migrator first offers two top-level choices:

* **Assess & Plan** — inspect the source and target, validate connectivity and compatibility, and produce an assessment report and a migration plan. No data is moved and nothing is written to the target.
* **Assess + Run** — assess the source, then proceed to the full migration, with confirmation steps between phases.

Preview a migration with **Assess & Plan** before committing to it; the assess and plan phases write their artifacts under `artifacts/` and leave the target untouched.

## In This Section

{% content-ref url="installation-and-first-run.md" %}
[installation-and-first-run.md](installation-and-first-run.md)
{% endcontent-ref %}

{% content-ref url="migration-modes.md" %}
[migration-modes.md](migration-modes.md)
{% endcontent-ref %}

{% content-ref url="application-user-migration.md" %}
[application-user-migration.md](application-user-migration.md)
{% endcontent-ref %}

{% content-ref url="environment-variables.md" %}
[environment-variables.md](environment-variables.md)
{% endcontent-ref %}

## Feedback

Join the [MariaDB Community on Slack](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/community/joining-the-community) to share your feedback.

## License

The [MariaDB Software License Terms](https://legal.mariadb.com/agreements/enterprise/MariaDB_Software_License_Terms_2026-05-15.pdf) apply to all MariaDB Software unless otherwise stated. They do not alter the license terms of any free and open-source software (FOSS) or software subject to the Business Source License (BSL); see Section 7 of the MariaDB Software License Terms.

For additional legal information, see the [MariaDB Terms](https://mariadb.com/terms/).
