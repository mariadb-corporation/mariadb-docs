---
description: >-
  The MySQL to MariaDB Migrator automates end-to-end MySQL to MariaDB migrations
  — schema, data, users, and validation — in four selectable modes.
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

| Mode                                                                                       | Internal ID | Type    | Best For                                                               |
| ------------------------------------------------------------------------------------------ | ----------- | ------- | ---------------------------------------------------------------------- |
| [Serial Streaming Copy](migrate-with-serial-streaming-copy.md)                             | `one_step`  | Offline | Smaller databases and standard maintenance windows                     |
| [Parallel Restartable Streaming Copy](migrate-with-parallel-restartable-streaming-copy.md) | `two_step`  | Offline | Larger datasets that need schema-then-parallel-data loading            |
| [Offline Copy](migrate-with-offline-copy.md)                                               | `staged`    | Offline | Source and target not network-reachable, or a deferred / two-host load |
| [Replication](migrate-with-replication.md)                                                 | `binlog`    | Online  | Low-downtime cutover with ongoing replication                          |

Each mode links to its step-by-step guide above. For the variable-level detail on all four modes in one place, see [Migration Modes](migration-modes.md).

## Choose a Guide

If you are not sure which mode fits, match your situation to a guide:

| Your situation                                                                                                                               | Guide                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| A small or medium database, a standard maintenance window is acceptable, and one host can reach both the source and the target               | [Serial Streaming Copy](migrate-with-serial-streaming-copy.md)                             |
| The source and target cannot reach each other (air-gapped or separate networks), or you want a checkpoint between the dump and the load      | [Offline Copy](migrate-with-offline-copy.md)                                               |
| A large database where a single serial transfer is too slow, you can install the `mariadb-mtk` engine, and you can start from a clean target | [Parallel Restartable Streaming Copy](migrate-with-parallel-restartable-streaming-copy.md) |
| Downtime must be minimal, the source uses `binlog_format=ROW` with no JSON columns, and you can perform a cutover                            | [Replication](migrate-with-replication.md)                                                 |

If more than one row fits, use this order: minimal downtime points to Replication (when the source qualifies); otherwise, if one host cannot reach both sides, use Offline Copy; otherwise choose Serial Streaming Copy for a small or medium database and Parallel Restartable Streaming Copy for a large one.

## How the Tool Runs

When launched interactively, the migrator first offers two top-level choices:

* **Assess & Plan** — inspect the source and target, validate connectivity and compatibility, and produce an assessment report and a migration plan. No data is moved and nothing is written to the target.
* **Assess + Run** — assess the source, then proceed to the full migration, with confirmation steps between phases.

Preview a migration with **Assess & Plan** before committing to it; the assess and plan phases write their artifacts under `artifacts/` and leave the target untouched.

## In This Section

Start with the reference pages to understand how the tool installs, runs, and handles users:

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

Then follow the step-by-step guide for your mode:

{% content-ref url="migrate-with-serial-streaming-copy.md" %}
[migrate-with-serial-streaming-copy.md](migrate-with-serial-streaming-copy.md)
{% endcontent-ref %}

{% content-ref url="migrate-with-offline-copy.md" %}
[migrate-with-offline-copy.md](migrate-with-offline-copy.md)
{% endcontent-ref %}

{% content-ref url="migrate-with-parallel-restartable-streaming-copy.md" %}
[migrate-with-parallel-restartable-streaming-copy.md](migrate-with-parallel-restartable-streaming-copy.md)
{% endcontent-ref %}

{% content-ref url="migrate-with-replication.md" %}
[migrate-with-replication.md](migrate-with-replication.md)
{% endcontent-ref %}

## Feedback

Join the [MariaDB Community on Slack](https://r.mariadb.com/join-community-slack) to share your feedback.

## License

The [MariaDB Software License Terms](https://legal.mariadb.com/agreements/enterprise/MariaDB_Software_License_Terms_2026-05-15.pdf) apply to all MariaDB Software unless otherwise stated. They do not alter the license terms of any free and open-source software (FOSS) or software subject to the Business Source License (BSL); see Section 7 of the MariaDB Software License Terms.

For additional legal information, see the [MariaDB Terms](https://mariadb.com/terms/).

## See Also

[An Easy Path from MySQL to MariaDB](https://mariadb.com/resources/blog/an-easy-path-from-mysql-to-mariadb-introducing-mariadb-migrator/) • blog post • 2026 • 4 minutes
