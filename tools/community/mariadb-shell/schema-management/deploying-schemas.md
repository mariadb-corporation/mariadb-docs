---
description: >-
  Deploy an MSM schema release to a MariaDB server with msm.deploy_schema,
  creating or upgrading the schema, with optional backups, the deployment log,
  and the errors a deployment can report.
---

# Deploying Schemas

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

`msm.deploy_schema()` runs the deployment script of a release on a server. The same call creates the schema on a server that doesn't have it, and upgrades the schema on a server that has an earlier release.

## Deploy a Release

Connect to the server, then deploy:

```python
shell.connect("mariadb://admin@db.example.com:3306")
msm.deploy_schema(schema_project_path="~/projects/shop.msm.project")
```

```text
Completed the update of `shop` version 1.0.0 to 1.1.0 successfully.
```

From the command line, pass the connection URI before the `--`:

```bash
mariadb-shell mariadb://admin@db.example.com:3306 -- msm deploy-schema --schema-project-path=/home/dev/projects/shop.msm.project
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `schema_project_path` | string | The [MSM working directory](schema-projects.md#the-msm-working-directory) | The project folder. |
| `version` | string | The latest release | The release to deploy. A deployment script for it must exist. |
| `backup` | Boolean | `false` | Take a backup of an existing schema before it is upgraded, and restore it if the upgrade fails. See [Backups](#backups). |
| `backup_directory` | string | `plugin_data/msm_plugin/backups/<schema>_backup_<version>` | Where to write the backup. |
| `session` | Session | The global session | The session to deploy with. |

The function returns a message that describes what it did. It requires a deployment script for every released version, so generate them first, as described in [Preparing Releases](preparing-releases.md#generate-the-deployment-script).

## What a Deployment Does

Before it runs the deployment script, the function compares the schema on the server with the project:

| Schema on the server | Result |
| --- | --- |
| Doesn't exist | The schema is created at the requested release. |
| Managed by MSM, at an earlier release | The schema is upgraded, one release after the other, up to the requested release. |
| Managed by MSM, at the requested release | Nothing changes. The message says so. |
| Managed by MSM, at a later release than the project has | Nothing changes. The message says so. |
| Managed by MSM, at a version that isn't a release of the project | Refused. |
| Exists, but isn't managed by MSM | Refused. |

A schema is managed by MSM when it contains the view `msm_schema_version`. See [The Schema Version](msm-sections.md#the-schema-version).

The deployment script then runs statement by statement on the session. While it runs, MSM holds the user lock `MSM_METADATA_LOCK` on the server, so two deployments on the same server can't overlap. If the lock isn't free within one second, the deployment fails with *Failed to acquire MSM schema update lock*.

### When a Deployment Fails

DDL statements commit implicitly, so a deployment can't be rolled back as a whole. If a statement fails, the deployment stops, and what remains depends on the case:

* **A new schema** is dropped, so that the next attempt starts on an empty server.
* **An upgrade without a backup** leaves the schema as the failed statement left it. Its `msm_schema_version` view usually reports `0.0.0`, and every later deployment refuses the schema with *the version 0.0.0 cannot be updated* until you repair or restore it by hand.
* **An upgrade with a backup** drops the schema and loads the backup, so that the schema is back at its previous release.

The error message contains the statement that failed and the server's error.

## Backups

With `backup` set to `true`, an upgrade of an existing schema starts with a dump of that schema, made with [`util.dump_schemas()`](../utilities/dump-and-load/dump-utilities.md):

```python
msm.deploy_schema(schema_project_path=project, backup=True)
```

* If the upgrade fails, MSM drops the schema and loads the dump with [`util.load_dump()`](../utilities/dump-and-load/load-dump-utility.md). The error message then says that the schema has been restored to its previous version.
* If the upgrade succeeds, or the restore succeeds, MSM deletes the dump. A backup is a safety net for the deployment, not an archive; take your own dump if you want to keep one.
* If the restore fails, the error message says that the schema couldn't be restored, and the dump stays in the backup directory, so that you can load it yourself.
* Loading a dump requires the server variable `local_infile`. If it is off, MSM turns it on with `SET GLOBAL local_infile=1` before the dump, and off again afterwards. This requires a privilege to set global variables. If MSM can't set it, the deployment fails before anything is changed.
* The dump progress is printed while the backup is taken.

No backup is taken when the schema doesn't exist yet, because a failed creation drops the new schema anyway.

{% hint style="info" %}
If MSM can't turn on `local_infile`, its error message suggests `SET PERSIST GLOBAL local_infile=1`. MariaDB has no `SET PERSIST`. Run `SET GLOBAL local_infile=1` as an administrator, or set `local_infile=1` in the server's option file.
{% endhint %}

## Required Privileges

The deployment runs with the privileges of the session's account. Use an account that can do everything the scripts contain:

* create the schema, and create, alter, and drop tables, views, stored routines, triggers, and events in it
* run the stored procedures that the deployment script creates
* create roles and grant privileges, if section 170 or 270 has statements, which also requires the privileges that are granted
* change REST endpoints, if section 180 has statements
* for backups, the privileges of the dump and load utilities, and the privilege to set `local_infile`

## REST Endpoints

Statements in section 180 define MariaDB REST Service endpoints. They aren't SQL that the server understands: MariaDB Shell processes them through the [SQL handler](../extending-mariadb-shell/sql-handlers.md) of its REST Service plugin, which stores the definitions in the REST metadata schema on the server. Therefore:

* The server needs the REST metadata schema before the first deployment with REST endpoints.
* Deploy with `msm.deploy_schema()` or with MariaDB Shell. A deployment script that contains REST statements fails in other clients, such as `mariadb`.

## Collation of the Schema

{% hint style="warning" %}
The scripts create the schema with `DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci`. Recent MariaDB versions accept this MySQL collation name; older ones, such as MariaDB 10.11, refuse it, and the deployment fails. Changing section 110 of the development script only affects the first release of a project, because the deployment scripts of later releases always use this collation.
{% endhint %}

## The Deployment Log

MSM writes every step of a deployment to `msm_schema_update_log.txt` in its plugin data directory, `plugin_data/msm_plugin/` in the [user configuration directory](../files-and-environment-variables.md#user-configuration-directory). Successful and failed deployments are both logged, with the error messages:

```text
2026-10-05 20:51:34.833212 - INFO - Starting deployment of database schema `shop` using version 1.1.0 ...
2026-10-05 20:51:34.833454 - INFO - Running SQL script `/home/dev/projects/shop.msm.project/releases/deployment/shop_deployment_1.1.0.sql` ...
2026-10-05 20:51:35.091501 - INFO - SQL script /home/dev/projects/shop.msm.project/releases/deployment/shop_deployment_1.1.0.sql executed successfully.
2026-10-05 20:51:35.092061 - INFO - Deployment of `shop` version 1.1.0 completed successfully.
```

The log grows with every deployment; MSM never truncates it.

## Check a Server

These functions read the state of the schema on the server of the global session, or of the session passed with the `session` option:

| Function | Returns |
| --- | --- |
| `msm.get.schema_exists()` | Whether the schema of the project exists. |
| `msm.get.schema_is_managed()` | Whether the schema has the `msm_schema_version` view. |
| `msm.get.schema_version()` | The deployed version, for example `"1.1.0"`, or `None` if the schema doesn't exist. |

```bash
mariadb-shell mariadb://admin@db.example.com:3306 -- msm get schema-version --schema-project-path=/home/dev/projects/shop.msm.project
```

```text
1.1.0
```

To list what the project can deploy, use `msm.get.deployment_script_versions()` and `msm.get.last_deployment_version()`. They read the project folder, not the server.

## Error Messages

| Message | Cause |
| --- | --- |
| *There are no versions of the schema `…` that have been released yet.* | The project has no release. |
| *Deployment script(s) missing. Please generate deployment scripts for all released versions first.* | A released version has no deployment script. |
| *… there is no deployment script available for this version.* | The requested version isn't a release of the project. |
| *… requested but the schema is not managed by MSM.* | A schema of the same name exists without an `msm_schema_version` view. |
| *… the version … cannot be updated.* | The deployed version isn't a release of the project, so no upgrade path leads from it. The version `0.0.0` means that an earlier upgrade failed and left the schema behind; repair or restore it. |
| *Failed to acquire MSM schema update lock.* | Another deployment runs on the same server. |
| *MariaDB session not specified.* | No global session is open and no `session` was passed. |
| *Failed to run the SQL script.* followed by a statement and an error | A statement of the deployment script failed on the server. |

When you run a deployment script without MSM, for example with `mariadb-shell -f`, the script checks the schema itself and stops with one of these errors:

| Error | Cause |
| --- | --- |
| 32100 | The schema exists and has tables, but no `msm_schema_version` view. |
| 32101 | The schema reports version `0.0.0`, so an earlier deployment failed or is still running. |
| 32102 | The deployed version can't be upgraded by this script. |

<sub>_This page is licensed: GPLv2_</sub>
