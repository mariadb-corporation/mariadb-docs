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
| `online_alter` | Boolean or dictionary | The project's setting | This deployment's setting for online `ALTER TABLE`, over the project's `onlineAlter` setting. `false` runs every `ALTER TABLE` as written. See [Online ALTER TABLE](#online-alter-table). |
| `substitutions` | dictionary | The defaults of the project | The values of the substitutions that the project declares in its `substitutions` setting, for example `{"schema_prefix": "acme_"}`. Every `/*<msm:name>*/` in the scripts and in the schema name is replaced with its value before the scripts run. |
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

The deployment script then runs statement by statement on the session. While it runs, MSM holds a user lock for the schema on the server, `MSM_METADATA_LOCK_` followed by the MD5 hash of the schema name, so two deployments of the same schema can't overlap, while different schemas can be deployed at the same time. If the lock isn't free within one second, the deployment fails with *Failed to acquire MSM schema update lock*.

### When a Deployment Fails

DDL statements commit implicitly, so a deployment can't be rolled back as a whole. If a statement fails, the deployment stops, and what remains depends on the case:

* **A new schema** is dropped, so that the next attempt starts on an empty server.
* **An upgrade without a backup** leaves the schema as the failed statement left it. Its `msm_schema_version` view usually reports `0.0.0`, and every later deployment refuses the schema with *the version 0.0.0 cannot be updated* until you repair or restore it by hand.
* **An upgrade with a backup** drops the schema and loads the backup, so that the schema is back at its previous release.

The error message contains the statement that failed and the server's error.

## Online ALTER TABLE

When `msm.deploy_schema()` upgrades a schema, it runs the `ALTER TABLE` statements of the update scripts' section 240 the least disruptive way that the server accepts, so that the application can go on reading and writing the tables while they change. It tries each statement with the following clauses, in this order, and the first step that the server accepts applies the change:

| Step | The statement is sent with | While it runs |
| --- | --- | --- |
| `INSTANT` | `ALGORITHM=INSTANT` | Only the table's metadata changes. |
| `NOCOPY` | `ALGORITHM=NOCOPY, LOCK=NONE` | Reads and writes go on. |
| `INPLACE` | `ALGORITHM=INPLACE, LOCK=NONE` | InnoDB rebuilds the table in place; reads and writes go on. |
| `COPY` | `ALGORITHM=COPY, LOCK=NONE` | The table is copied; reads and writes go on. MariaDB versions before 11.2 refuse this step. |
| `NBO` | `LOCK=SHARED` or `LOCK=EXCLUSIVE`, as a non-blocking operation | Galera clusters only, and only when `nboLock` is set. Writes are blocked, with `EXCLUSIVE` reads too. |
| `SHARED_LOCK` | `LOCK=SHARED` | Writes are blocked. |
| `EXCLUSIVE_LOCK` | `LOCK=EXCLUSIVE` | Reads and writes are blocked. |

The server refuses a step that it can't run with these clauses at once, without changing anything, and MSM goes on with the next step. Size limits leave out steps for large tables; see [Online ALTER TABLE Settings](#online-alter-table-settings). A lock wait timeout is retried, waiting 2, 4, 8, and up to 30 seconds in between. Every other error stops the deployment, as described in [When a Deployment Fails](#when-a-deployment-fails).

The scripts themselves keep plain `ALTER TABLE` statements: a deployment script that you run without MSM, for example with the `mariadb` client, runs them as written. The creation of a new schema isn't affected, because it creates the tables with `CREATE TABLE`.

MSM runs these `ALTER TABLE` statements as written:

* a statement with its own `ALGORITHM` or `LOCK` clause, or with `ONLINE`, `IGNORE`, or `IF EXISTS`
* a statement that changes the partitioning of a table
* a statement inside a compound statement, such as `IF … END IF`
* every statement of an update step that declares a variable with `DECLARE`
* a statement on a table for which online `ALTER TABLE` is turned off

All other statements of an update step run in their order, as they would in the stored procedure. Each `ALTER TABLE` and the step that applied it are written to the [deployment log](#the-deployment-log), for example ``ALTER TABLE `product`: INSTANT (0.01 s).``

{% hint style="info" %}
The binary log records each `ALTER TABLE` with the clauses of the step that applied it. Replicas must therefore run the same MariaDB version as the primary.
{% endhint %}

### Online ALTER TABLE Settings

The setting `onlineAlter` in `msm.project.json` controls online `ALTER TABLE` for a project. It is on by default, and a new project has it written as `{"enabled": true}`. The value `true` or `false` stands for `{"enabled": true}` or `{"enabled": false}`, and a project without the setting has it on, with the defaults. Values for one table go into `tables`, under the name of the table:

{% code title="msm.project.json" %}
```json
{
    ...
    "onlineAlter": {
        "enabled": true,
        "maxRebuildBytes": 1073741824,
        "tables": {
            "order_item": {"maxLockedBytes": 0}
        }
    },
    ...
}
```
{% endcode %}

| Key | Default | Description |
| --- | --- | --- |
| `enabled` | `true` | Whether to run the `ALTER TABLE` statements online. |
| `maxRebuildBytes` | 10 GiB | The largest table on which the `INPLACE` and `COPY` steps may run, in bytes. `null` sets no limit, `0` leaves the steps out. |
| `maxLockedBytes` | No limit | The largest table on which the `SHARED_LOCK` and `EXCLUSIVE_LOCK` steps, which block writes, may run, in bytes. `0` leaves the steps out. |
| `galeraMaxBytes` | 256 MiB | On a Galera cluster, the largest table on which a step other than `INSTANT` and `NBO` may run, in bytes. These steps run under Total Order Isolation, which pauses the cluster. `null` or `0` allows only `INSTANT` and `NBO`. |
| `nboLock` | `null` | On a Galera cluster, `SHARED` or `EXCLUSIVE` allows the `NBO` step with this lock. MariaDB Community Server refuses non-blocking operations. |
| `lockWait` | 5 | The seconds to wait for the table's metadata lock in each attempt, at least 1. |
| `maxRetries` | 10 | The attempts after a lock wait timeout, in each step. |

The size of a table is the sum of `DATA_LENGTH` and `INDEX_LENGTH` in `information_schema.TABLES`, which is an estimate for InnoDB tables.

The `online_alter` option of `msm.deploy_schema()` takes the same format, for the values that depend on the server you deploy to:

```python
msm.deploy_schema(schema_project_path=project, online_alter={"maxRebuildBytes": 0})
```

For each table, the most specific value wins, in this order, from the least to the most specific: the project's general values, the deployment's general values, the project's values for the table, and the deployment's values for the table. The names in `tables` are the names of the project's tables, matched exactly; an `ALTER TABLE` of a table in another schema gets the general values. MSM checks both settings before the deployment starts, and refuses a setting with an unknown key or a value out of range.

To read the setting, use `msm.get_online_alter_settings()`, which also returns the defaults and, with the `table` option, the values that a table gets. To change it, pass the whole setting to `msm.set.project_settings()`, as described in [Change Project Settings](schema-projects.md#change-project-settings).

### When No Step Applies

If none of the steps applies a change, the deployment stops. Its error message names the update step, the table, and the reason, for example for the table `order_item` of the settings above, when it is larger than `maxRebuildBytes`:

```text
… The update from 1.0.0 to 1.1.0 needs an external tool for an ALTER TABLE of `order_item`: online rebuilds (INPLACE, COPY) skipped: table size 2147483648 > max_rebuild_bytes 1073741824; blocking writes skipped: table size 2147483648 > max_locked_bytes 0; the server refused INSTANT, NOCOPY (last: …). Nothing of that statement was changed; the statements before it ran. Statement: ALTER TABLE `shop`.`order_item` …
```

The reason lists each limit that left a step out, and then the steps that the server refused, so that you can see which limit would allow more. The statements of the update before this `ALTER TABLE` have run, and the schema is left as after any failed upgrade, as described in [When a Deployment Fails](#when-a-deployment-fails). Raise the limit, run the change in a maintenance window with online `ALTER TABLE` turned off for the table or the deployment, or make it with a tool of your own.

{% hint style="warning" %}
On a Galera cluster, an `ALTER TABLE` of a table larger than `galeraMaxBytes` that can't run with `ALGORITHM=INSTANT` stops the deployment, unless `nboLock` is set. Without online `ALTER TABLE`, it would run under Total Order Isolation and pause the cluster for the whole change. To allow that, raise `galeraMaxBytes`, or turn online `ALTER TABLE` off for the table or the deployment. MSM refuses a session whose `wsrep_OSU_method` is `RSU`, which would change the table on one node only.
{% endhint %}

### Run One ALTER TABLE Online

`msm.online_alter_table()` runs a single `ALTER TABLE` on a table of a server through the same steps, outside of a deployment, on the global session or the one passed with the `session` option:

```python
msm.online_alter_table("shop", "product", "ADD COLUMN `sku` VARCHAR(20)")
```

```text
{
    "method": "INSTANT",
    "applied": true,
    ...
}
```

| Parameter or option | Description |
| --- | --- |
| `schema` | The schema of the table. |
| `table` | The table. |
| `spec` | Everything after `ALTER TABLE <table>`. It must not contain an `ALGORITHM` or `LOCK` clause, which the steps set, or a change of the partitioning. |
| `options` | The limits, with the keys of `onlineAlter` other than `enabled` and `tables`. The defaults apply to those you leave out. |
| `session` | The session to use. The default is the global session. |

The function returns `method`, the step that applied the change, or `NEEDS_EXTERNAL` when none did and nothing changed; `applied`; `reason`; `table_size`; `galera`; and `steps`, the outcome of each step that was tried or left out. `msm.get_online_alter_defaults()` returns the default limits.

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
| *Failed to acquire MSM schema update lock.* | Another deployment of the same schema runs on the server. |
| *… needs an external tool for an ALTER TABLE of …* | No step of online `ALTER TABLE` could apply a statement of the update. See [When No Step Applies](#when-no-step-applies). |
| *Unknown key … onlineAlter …* or *… must be …* | The `onlineAlter` setting of the project or the `online_alter` option has a key or value that MSM doesn't accept. Nothing has run. |
| *MariaDB session not specified.* | No global session is open and no `session` was passed. |
| *Failed to run the SQL script.* followed by a statement and an error | A statement of the deployment script failed on the server. |

When you run a deployment script without MSM, for example with `mariadb-shell -f`, the script checks the schema itself and stops with one of these errors:

| Error | Cause |
| --- | --- |
| 32100 | The schema exists and has tables, but no `msm_schema_version` view. |
| 32101 | The schema reports version `0.0.0`, so an earlier deployment failed or is still running. |
| 32102 | The deployed version can't be upgraded by this script. |

<sub>_This page is licensed: GPLv2_</sub>
