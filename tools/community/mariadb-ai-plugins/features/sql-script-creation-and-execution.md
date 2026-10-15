---
description: >-
  Have an AI coding agent write a MariaDB schema create script, run it on a
  sandbox instance or a configured server, and verify the result with the db
  and sandbox tools of the mariadb-shell MCP server.
---

# SQL Script Creation and Execution

With MariaDB AI Plugins, you can ask a coding agent to write a SQL script that creates a database schema, and then to run the script on a MariaDB server and check the result. The agent writes the script with the help of the SQL skills, and runs and verifies it with the `db.*` and `sandbox.*` tools of the MCP server.

This page describes the three steps of this workflow: creating the script, running it, and verifying the result.

## Requirements

* The `dev` or `sql` plugin. Both include the skills and the MCP server.
* A working folder on the [allowed-paths list](../configuring-the-mcp-server/README.md#allowed-paths) of the MCP server. The agent saves the script there, and the MCP server reads it from there.
* A MariaDB server to run the script on: either a [sandbox instance](sandbox-instances.md), which the agent can deploy itself, or a connection that you configured with `mcp setup`.

## Skills and Tools

| Skills | Tools |
| --- | --- |
| `mariadb-schema-create-script`, plus the SQL statement skills it refers to, such as `mariadb-create-database`, `mariadb-create-table`, `mariadb-create-index`, and `mariadb-create-view` | `sandbox.deploy`, `db.list_connections`, `db.connect`, `db.execute_sql_script`, `db.list_schemas`, `db.list_objects`, `db.get_object_details`, `db.execute_sql`, `db.close` |

## Create the Script

Start the agent in your working folder, and describe the schema and the name of the script file:

```text
Create a MariaDB database schema named notes_app for a note-taking app and
store it in a notes_app.sql file.
```

This step only creates a file; it doesn't need a database connection. Before it writes the script, the agent reads the `mariadb-schema-create-script` skill, which is maintained in the MariaDB AI Plugins repository. This skill defines the structure of the script and refers the agent to the SQL statement skills from the MariaDB documentation, such as `mariadb-create-database`, `mariadb-create-table`, `mariadb-create-index`, and `mariadb-create-view`. These skills describe the MariaDB-specific syntax of each statement.

A script that follows the skill has these characteristics:

* It starts with a block that saves the current session settings, disables unique and foreign key checks, sets the SQL mode, and switches to `utf8mb4`. It ends with a block that restores the saved settings.
* It creates the schema with `CREATE SCHEMA IF NOT EXISTS`, and the tables with `CREATE OR REPLACE TABLE`.
* Tables whose rows are exposed to client applications use the native `UUID` data type for their primary key, with `UUID_v7()` as the default value.
* Each schema object has a comment that describes its purpose.
* `INSERT` statements for sample or initial data come after the statements that create the schema objects.

You can refine the script in further requests, for example to add a full-text index or row history for a table. The agent reads the relevant skills again for each change.

{% hint style="info" %}
If you plan to run the script on a server where the schema has a different name, ask the agent to use fully qualified object names, such as `` `notes_app`.`note` ``, so that the script doesn't depend on the current schema of the session.
{% endhint %}

## Run the Script

To run the script, the agent needs a MariaDB server. For development and testing, a sandbox instance on your machine is a good choice:

```text
Spin up a MariaDB sandbox instance on port 3310, connect to it, and run
notes_app.sql against it.
```

The agent completes this request with the following tool calls:

1. `sandbox.deploy` deploys and starts a MariaDB Server instance on port 3310, and registers the connection `root@127.0.0.1:3310` with the MCP server.
2. `db.connect` opens this connection and returns a connection ID.
3. `db.execute_sql_script` reads `notes_app.sql` from the working folder and runs its statements in order on the connection.

`db.execute_sql_script` returns one result for each statement. A statement that fails doesn't raise an error; its result contains the error message, and by default the script stops at the first failed statement. A script isn't a transaction, so statements that ran before the failure keep their effect. The agent checks the results of all statements before it reports that the script ran successfully.

If the working folder isn't on the allowed-paths list, `db.execute_sql_script` can't read the file. In this case, the agent typically passes the content of the script directly with the `sql_script` argument instead.

## Verify the Result

Ask the agent to check the result on the server rather than to summarize what it ran:

```text
Read the result back from the server. Which schemas exist, which tables are
in notes_app, and what are the columns of the note table?
```

To answer, the agent queries the server with these tools:

* `db.list_schemas` lists the schemas, which should include `notes_app`.
* `db.list_objects` lists the tables and views in `notes_app`.
* `db.get_object_details` returns the columns, keys, indexes, and constraints of a table, for example the `UUID` primary key and the foreign keys of `note`.

To test the schema with data, ask the agent to insert sample rows and run a query, for example the number of notes per user. The agent runs these statements with `db.execute_sql`, which returns the result rows.

## Clean Up

When you no longer need the sandbox, ask the agent to remove it:

```text
Close the connection, then stop and delete the sandbox on port 3310.
```

The agent calls `db.close`, `sandbox.stop`, and `sandbox.delete`, in this order. A sandbox can't be deleted while it's running.

## The Complete Workflow in One Request

Once you're familiar with the steps, you can combine them in a single request:

```text
Work in the current folder and complete these steps in order:
1. Create a MariaDB database schema named notes_app for a note-taking app
   and store it in notes_app.sql.
2. Spin up a sandbox instance on port 3310, connect to it, and run
   notes_app.sql against it.
3. Read the result back from the server: list the tables you created and
   show the columns of the note table.
4. Stop and delete the sandbox, even if an earlier step failed.
```

## Run Scripts on Development and Production Servers

Besides sandbox instances, the agent can run queries and scripts on your existing development and production servers. To give the agent access to a server, add a connection for it, as described in [Configuring the MCP Server](../configuring-the-mcp-server/README.md):

```bash
mariadb-shell -- mcp setup
```

If a server is only reachable through an SSH host, configure the connection with a `mariadb+ssh://` URI, as described in [Tunnel Database Connections via SSH](../configuring-the-mcp-server/tunnel-database-connections-via-ssh.md). The agent finds the configured connections with `db.list_connections`, and you refer to a connection in your request, for example:

```text
Run notes_app.sql on the development server mcp@dev-db.example.com:3306.
```

{% hint style="danger" %}
Don't configure the connection with your personal MariaDB developer account, an administrator account, or `root`. The agent would have all privileges of that account, including access to production data. Create a dedicated MCP account with limited privileges instead, for example read-only access to production schemas and full access to a development schema. See [Database Accounts for the MCP Server](../configuring-the-mcp-server/database-accounts-for-the-mcp-server.md).
{% endhint %}

{% hint style="warning" %}
A script that follows the `mariadb-schema-create-script` skill creates tables with `CREATE OR REPLACE TABLE`. If a table already exists, this statement drops it, including its data, and creates it again. Run create scripts on new schemas, sandboxes, or development servers only. To change an existing schema, use versioned upgrade scripts as described in [Versioned Schemas with Schema Management](versioned-schemas-with-schema-management.md).
{% endhint %}
