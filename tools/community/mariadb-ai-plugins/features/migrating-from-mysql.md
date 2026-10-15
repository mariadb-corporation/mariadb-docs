---
description: >-
  Migrate an application and its database from MySQL to MariaDB with the
  skills and the optional migrator tools of MariaDB AI Plugins.
---

# Migrating from MySQL

MariaDB AI Plugins support a migration from MySQL to MariaDB in two ways. The skills describe the differences between MySQL and MariaDB that affect your SQL and application code, and the optional `migrator.*` tools migrate the database itself.

## Requirements

* For compatibility guidance, the `dev` or `sql` plugin. Both include the `mysql-to-mariadb` skill.
* For the database migration, the `dev` plugin and the migration tooling, which you install on Linux or macOS with this command:

  ```bash
  mariadb-shell -- mcp setup --installMigrator
  ```
* Connections to both the MySQL source and the MariaDB target, configured with `mcp setup`.

## Skills and Tools

| Skills | Tools |
| --- | --- |
| `mysql-to-mariadb`, `mariadb-migrator`, `mariadb-migrator-discovery`, `mariadb-migrator-configure`, `mariadb-migrator-modes`, `mariadb-migrator-run`, `mariadb-migrator-verify`, `mariadb-migrator-troubleshooting` | [`migrator.*`](../mcp-tool-reference/migrator-tools.md), `db.*`, `sandbox.*` |

## Assess Compatibility

Ask the agent what changes if you move the application from MySQL to MariaDB. It reads the `mysql-to-mariadb` skill and reviews your schema and queries for differences.

## Configure the Migration

The agent writes the migration configuration with `migrator.set_config`. The configuration can only refer to connections that you configured with `mcp setup`, and the tool rejects passwords.

## Plan and Run

1. `migrator.plan` resolves the steps and validates the configuration without changing anything.
2. `migrator.run` performs the migration.
3. If a run fails, `migrator.resume` continues it from where it stopped.

{% hint style="danger" %}
Omit `out` for every new run. A run pointed at the output directory of an earlier run reports every step as `SKIPPED`, exits with status 0, and migrates nothing. Check that every step reports `DONE`.
{% endhint %}

## Verify the Result

After the migration, the agent uses the `mariadb-migrator-verify` skill to check the result on the target server with the `db.*` tools. The checks include object counts by type, foreign keys, row counts, spot checks of values, and logins with each migrated account. To test the migration first, migrate into a [sandbox instance](sandbox-instances.md).
