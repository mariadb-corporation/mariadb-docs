---
description: >-
  Reference for the skills maintained in the MariaDB AI Plugins repository, including skills for the MariaDB REST Service, schema management, and the migration from MySQL.
---

# Additional Skills

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

These skills are maintained in the `additional-skills/` directory of the MariaDB AI Plugins repository rather than in the MariaDB documentation. Most of them describe workflows that use the tools of the MCP server.

## SQL Scripts

Skills for writing SQL scripts that create a schema.

| Skill | Plugins | What it covers |
| --- | --- | --- |
| `mariadb-schema-create-script` | `dev`, `sql` | Best practices when writing a MariaDB-specific database script. |

## MariaDB REST Service

Skills for creating and managing REST endpoints with the MariaDB REST Service.

| Skill | Plugins | What it covers |
| --- | --- | --- |
| `mariadb-rest-service-authorization` | `dev` | Set up authentication and authorization for a MariaDB REST Service — create a REST AUTH APP (MRS, MARIADB or OAuth2 vendor), link it to a service, add REST users, and control access with REST roles and GRANT/REVOKE REST CREATE/READ/UPDATE/DELETE privileges at service/schema/object level. |
| `mariadb-rest-service-create` | `dev` | Create a MariaDB REST Service for a database schema — configure the REST metadata schema, create the REST service, add a REST schema, and expose tables/views as REST data mapping views and stored procedures/functions as REST procedures/functions. |
| `mariadb-rest-service-drop` | `dev` | Remove MariaDB REST Service objects with DROP REST statements — drop a REST service, schema, data mapping view, procedure, function, content set/file, auth app, user, role or stale REST Daemon registration, using IF EXISTS to avoid errors. |
| `mariadb-rest-service-show` | `dev` | Browse and inspect existing MariaDB REST Service objects with SHOW REST commands — list services, schemas, data mapping views, procedures, functions, scripts, content sets/files, auth apps and vendors, users, roles, grants, REST Daemons and metadata schemas; check service status; list the columns a table can expose; dump the DDL (or JSON) of any object with SHOW CREATE REST. |
| `mariadb-rest-service-update-endpoints` | `dev` | Update MariaDB REST Service endpoints — alter a REST service, schema, data mapping view, procedure or function; rename request paths; enable/disable; publish/unpublish a service; add/remove auth apps; merge JSON options; and drop endpoints. |

## Schema Management

Skills for the project lifecycle of MariaDB Schema Management (MSM), which use the `msm.*` tools.

| Skill | Plugins | What it covers |
| --- | --- | --- |
| `mariadb-schema-management-create` | `dev` | Scaffold a MariaDB Schema Management (MSM) project and author the initial schema in the development folder — create the project with msm.create_project and write the first version's tables, objects and grants into the MSM sections of `<schema>_next.sql`. |
| `mariadb-schema-management-deploy` | `dev` | Deploy a MariaDB Schema Management (MSM) schema version onto a live server with msm.deploy_schema — running the generated deployment script over an open db.connect connection to create the schema fresh or upgrade any prior released version to the target, optionally taking a backup first. |
| `mariadb-schema-management-develop` | `dev` | Develop the next version of a MariaDB Schema Management (MSM) schema in `development/<schema>_next.sql`, and keep large scripts maintainable by breaking section bodies out into development/sections/ files linked with the SOURCE `'<path>'[start:end];` statement. |
| `mariadb-schema-management-release` | `dev` | Prepare a MariaDB Schema Management (MSM) version release — snapshot the development script with msm.prepare_release, FILL the generated previous→new update script (table changes and drops in section 240, revoked privileges in 270) with the actual migration, and only then generate the deployment script with msm.generate_deployment_script. |
| `mariadb-schema-management` | `dev` | Overview of managing a MariaDB database schema across its whole lifecycle with the MariaDB Schema Management (MSM) plugin via the mariadb-shell MCP server — the versioned schema project, the MSM section model, and the create → develop → release → deploy workflow. |

## MySQL to MariaDB Migration

Skills for migrating a MySQL database to MariaDB, which use the optional `migrator.*` tools.

| Skill | Plugins | What it covers |
| --- | --- | --- |
| `mariadb-migrator-configure` | `dev` | Write the MySQL-to-MariaDB migrator's config/migration.yaml with migrator.set_config — the rules that get a configuration refused (every named account must be a configured MCP connection, SRC_PORT/TGT_PORT always explicit, no password key ever, string values only), the keys each mode requires, the useful optional keys, and what MIGRATE_APP_USERS does to accounts and grants. |
| `mariadb-migrator-discovery` | `dev` | Turn a bare MySQL-to-MariaDB migration request into something runnable — call db.list_connections, probe and present source and target in one table, list the migratable schemas, and know when a fully-specified request may go straight to run and when a name that matches no configured connection is a hard stop. |
| `mariadb-migrator-modes` | `dev` | The MySQL-to-MariaDB migration modes and the gate each one brings — one_step (serial streaming), two_step (parallel, needs mariadb-mtk and only retries within a run), staged (dump to disk with a SHA-256 manifest, STAGED_PHASE dump_only/load_only across sessions, needs bash 4), binlog (replication, MySQL 8.0+ and no JSON columns), and why inplace/replace_slave are never picked. |
| `mariadb-migrator-run` | `dev` | Execute a MySQL-to-MariaDB migration with migrator.plan, migrator.run and migrator.resume — always plan first, omit `out` on a new run so a stale state.json cannot report every step SKIPPED at exit 0, check a finished run three ways (succeeded, every step DONE, the data actually on the target), read report.json/run.log in the artifacts directory, and hold the source baseline instead of publishing an interim report. |
| `mariadb-migrator-troubleshooting` | `dev` | The MySQL-to-MariaDB migrator's known defects and failure playbook — the bash 3.2 traps (unbound SRC_SSL_ARGS, exit 143 without pv, declare -A in staged mode), the SHOW PACKAGE STATUS 1064 that is a mariadb-dump age problem and not a MySQL 8.4 one, the root-user and existing-target-DB refusals, option-file contamination, and what every refusal message from set_config/plan/run/resume means and what to set. |
| `mariadb-migrator-verify` | `dev` | Verify a finished MySQL-to-MariaDB migration on the target with the db.\* tools and report it — object counts per type, foreign keys, row counts and value spot-checks (never a checksum unless asked), authenticating as each migrated account, the four things that vanish silently through MySQL's /\*!80016\*/ version gates (CHECK NOT ENFORCED, SRID, DEFAULT ENCRYPTION, utf8mb4_0900 collations), and the fixed markdown comparison table — one per database, real pipes, nothing added when every check comes back clean. |
| `mariadb-migrator` | `dev` | Overview and entry point for migrating a MySQL database to MariaDB with the migrator.\* tools of the mariadb-shell MCP server — what the tooling is, the two things you may never choose (unconfigured connections, passwords), the resume-safe trap that reports success while migrating nothing, the four tools, and the discover → mode → configure → run → verify workflow. |

## Laravel

Skills for using MariaDB in Laravel applications. These skills are included in the `dev` plugin only.

| Skill | Plugins | What it covers |
| --- | --- | --- |
| `mariadb-laravel-ai-sdk` | `dev` | Use MariaDB Vector as the store behind Laravel's AI SDK (laravel/ai): generating embeddings, persisting them in a MariaDB vector column, semantic search and giving an agent a similarity-search tool. |
| `mariadb-laravel-connector` | `dev` | Connect a Laravel (PHP) application to MariaDB: PDO requirements, the dedicated mariadb driver, version support and Docker/Sail setup. |
| `mariadb-laravel-vector` | `dev` | MariaDB Vector in a Laravel (PHP) application: vector columns, VECTOR INDEX, the AsVector Eloquent cast and similarity search with the query builder. |

<sub>_This page is licensed: GPLv2_</sub>
