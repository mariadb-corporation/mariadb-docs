---
description: >-
  Manage a database schema as a versioned project with MariaDB Schema
  Management and the msm tools of the mariadb-shell MCP server.
---

# Versioned Schemas with Schema Management

MariaDB Schema Management (MSM) manages a database schema as a versioned project. A project contains a development script, a snapshot of each released version, an update script for each release, and generated deployment scripts. A deployment script creates the schema on a new server, or upgrades an existing schema to the version of the release.

## Requirements

* The `dev` plugin. The schema management skills aren't part of the `sql` plugin.
* The project directory on the [allowed-paths list](../configuring-the-mcp-server/README.md#allowed-paths).
* For deployment, a connection to the target server, or a [sandbox](sandbox-instances.md).

## Skills and Tools

| Skills | Tools |
| --- | --- |
| `mariadb-schema-management`, `mariadb-schema-management-create`, `mariadb-schema-management-develop`, `mariadb-schema-management-release`, `mariadb-schema-management-deploy` | [`msm.*`](../mcp-tool-reference/msm-tools.md), `db.connect` |

## Create a Project

Ask the agent to create a schema project. It calls `msm.create_project`, which creates a `<schema>.msm.project/` directory.

## Develop the Schema

The agent edits the development script one section at a time with `msm.get_sql_content_from_section` and `msm.set_section_sql_content`. See [Script Sections](../mcp-tool-reference/msm-tools.md#script-sections) for what belongs in each section.

## Release a Version

1. `msm.prepare_release` takes a snapshot of the development script and creates an empty update script.
2. The agent fills the update script with the table changes since the previous release, in section 240, and with revoked privileges, in section 270. New and changed views, routines, roles, and grants stay in the development script, because the deployment script runs them in full on every deployment.
3. `msm.generate_deployment_script` generates the deployment script.

{% hint style="danger" %}
Fill the update script before generating the deployment script. A script generated too early creates the schema correctly on an empty server but silently fails to upgrade an existing installation.
{% endhint %}

## Deploy a Version

`msm.deploy_schema` applies a version to a server through an open `db.connect` connection, optionally taking a backup first.
