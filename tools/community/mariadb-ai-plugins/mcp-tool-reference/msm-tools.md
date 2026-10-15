---
description: >-
  Reference for the msm tools of the mariadb-shell MCP server, which manage versioned schema projects, releases, and deployments with MariaDB Schema Management.
---

# msm Tools

The `msm.*` tools manage database schemas with MariaDB Schema Management (MSM). With these tools, the agent creates and edits versioned schema projects, prepares releases, and generates and deploys the scripts that create or upgrade a schema. See [Versioned Schemas with Schema Management](../features/versioned-schemas-with-schema-management.md) for the workflow.

## Overview

| Tool | Description |
| --- | --- |
| `msm.create_project` | Creates a schema project directory, `<schema>.msm.project/`. |
| `msm.get_project_information` | Returns the project's metadata. |
| `msm.set_development_version` | Sets the version in section 910 of the development script. |
| `msm.get_released_versions` | Lists every released version. |
| `msm.get_last_released_version` | Returns the most recent release. |
| `msm.get_last_deployment_version` | Returns the version of the most recent generated deployment script. |
| `msm.get_deployment_script_versions` | Lists the versions of all generated deployment scripts. |
| `msm.get_sql_content_from_section` | Reads one section of a script. |
| `msm.set_section_sql_content` | Writes one section of a script. |
| `msm.prepare_release` | Takes a snapshot of the development script and creates an empty update script. |
| `msm.generate_deployment_script` | Creates the deployment script that creates or upgrades the schema. |
| `msm.deploy_schema` | Deploys a schema version to a server. |

## msm.create_project

Creates a schema project directory, `<schema>.msm.project/`.

| Argument | Description |
| --- | --- |
| `schema_name` | The schema's name. |
| `target_path` | Where to create the project. |
| `copyright_holder` | The copyright holder for the generated files. |
| `license` | A license name. An unrecognized name is rejected; omit it or pass your own text. |
| `overwrite_existing` | Whether to replace an existing project. |

## msm.get_project_information

Returns the project's metadata.

| Argument | Description |
| --- | --- |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |

## msm.set_development_version

Sets the version in section 910 of the development script.

| Argument | Description |
| --- | --- |
| `version` | The development version. |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |

## msm.get_released_versions

Lists every released version.

| Argument | Description |
| --- | --- |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |

## msm.get_last_released_version

Returns the most recent release.

| Argument | Description |
| --- | --- |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |

## msm.get_last_deployment_version

Returns the version of the most recent generated deployment script.

| Argument | Description |
| --- | --- |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |

## msm.get_deployment_script_versions

Lists the versions of all generated deployment scripts.

| Argument | Description |
| --- | --- |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |

## msm.get_sql_content_from_section

Reads one section of a script.

| Argument | Description |
| --- | --- |
| `file_path` | The script file. |
| `section_id` | The section number. |

## msm.set_section_sql_content

Writes one section of a script.

| Argument | Description |
| --- | --- |
| `file_path` | The script file. |
| `section_id` | The section number. |
| `sql_content` | The new section content. |

Always edit sections with `msm.get_sql_content_from_section` and `msm.set_section_sql_content`, so the section banners are never corrupted.

## msm.prepare_release

Takes a snapshot of the development script and creates an empty update script.

| Argument | Description |
| --- | --- |
| `version` | The version to release. |
| `next_version` | The next development version. |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |

## msm.generate_deployment_script

Creates the deployment script that creates or upgrades the schema.

| Argument | Description |
| --- | --- |
| `version` | The version to generate. |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |
| `overwrite_existing` | Whether to replace an existing script. |

{% hint style="danger" %}
Run `msm.prepare_release`, then fill the update script's section 240, and section 270 if privileges are revoked, and only then run `msm.generate_deployment_script`. A script generated before the update script is filled creates the schema correctly on an empty server but silently fails to upgrade an existing installation.
{% endhint %}

## msm.deploy_schema

Deploys a schema version to a server.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `version` | The version to deploy. |
| `schema_project_path` | The path of the schema project directory. Must be in an allowed path. |
| `backup` | Whether to back up the schema first. |
| `backup_directory` | Where to write the backup. |

Requires an open connection from `db.connect`.

## Script Sections

| Create script | Update script | Contents |
| --- | --- | --- |
| 130 | 230 | Helper routines, with names prefixed `msm_`. |
| 140 | 240 | Non-idempotent statements: tables and base data. In an update script, all `ALTER` statements, data backfills, and every `DROP` of an object that the new version no longer has. |
| 150 | 250 | Idempotent statements: views, procedures, functions, triggers, and events. Section 250 isn't deployed; leave it empty. |
| 170 | 270 | Authorization. Section 170: `CREATE ROLE IF NOT EXISTS` and `GRANT`. Section 270: only `REVOKE` and `DROP ROLE`. |
| 180 | — | Optional MariaDB REST Service endpoints, with `CREATE OR REPLACE REST` statements. |
| 190 | 290 | Removal of the `msm_` helpers. |

Sections 140, 240, 170, and 270 become the body of a stored procedure in the generated script. Write them as plain statements terminated by `;`, without `DELIMITER` or `USE`, and use dynamic SQL for conditional DDL. Sections 130, 150, 180, 230, 190, and 290 are emitted at the top level and use `DELIMITER %%`.

The deployment script runs the target version's sections 150, 170, and 180 in full on every deployment, after the table changes. New and changed views, routines, roles, grants, and REST endpoints therefore reach upgraded schemas without any statement in the update script. The update script only needs what these sections can't express: table changes, the `DROP` of removed objects in section 240, and `REVOKE` or `DROP ROLE` in section 270.

{% hint style="warning" %}
Don't grant privileges in section 270. On an upgrade, it runs before section 170, so a role that is new in the version doesn't exist yet, and the deployment fails with error 1133.
{% endhint %}
