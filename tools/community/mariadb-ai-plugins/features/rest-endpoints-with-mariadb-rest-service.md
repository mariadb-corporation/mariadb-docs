---
description: >-
  Create REST endpoints for a MariaDB schema with the MariaDB REST Service and
  the mariadb-shell MCP server.
---

# REST Endpoints with MariaDB REST Service

The MariaDB REST Service provides REST endpoints for schema objects, which return and accept JSON. You configure the REST Service with SQL statements that extend the SQL grammar with `REST` keywords. MariaDB Shell supports these statements, so the agent can create REST services and endpoints with the same MCP tools it uses to run other SQL statements.

{% hint style="warning" %}
As of MariaDB AI Plugins 26.9.5, you can define REST services and endpoints with MariaDB Shell, but the MariaDB REST Daemon that serves them isn't available.
{% endhint %}

## Requirements

* The `dev` plugin. The REST Service skills aren't part of the `sql` plugin.
* A connection to a server where the account may create schemas, because `CONFIGURE REST METADATA` creates one.

## Skills and Tools

| Skills | Tools |
| --- | --- |
| `mariadb-rest-service-create`, `mariadb-rest-service-update-endpoints`, `mariadb-rest-service-authorization`, `mariadb-rest-service-show`, `mariadb-rest-service-drop` | `db.connect`, `db.execute_sql` |

## Configure the Metadata

The agent runs `CONFIGURE REST METADATA` once per server to create the REST Service metadata schema.

## Create a Service and Endpoints

The agent creates a REST service, adds a REST schema to it, and exposes tables and views as REST data mapping views, and stored procedures and functions as REST procedures and functions.

Statements such as `USE REST SERVICE` and `USE REST SCHEMA` set the current REST service and REST schema for the following statements on the same connection. The agent can run the statements as a script with `db.execute_sql_script`, or one at a time with `db.execute_sql`; in both cases, they run on the session of the connection.

## Control Access

To require authentication for endpoints, the agent uses the `mariadb-rest-service-authorization` skill. It covers REST authentication apps, REST users and roles, and the `GRANT` and `REVOKE` statements for REST privileges on services, schemas, and objects.
