---
description: >-
  Example requests for AI coding agents with MariaDB AI Plugins, with and
  without a database connection.
---

# Basic Usage

You don't call skills or MCP tools yourself. Instead, you describe your task to the agent, and the agent decides which skills to read and which tools to use. The following examples show typical requests.

## With Skills Alone

The following requests don't require a database connection:

```text
Write a CREATE TABLE for a product catalog, MariaDB style.
```

```text
What changes if I move this application from MySQL to MariaDB?
```

```text
How do I do semantic search in MariaDB?
```

```text
Show me how to connect to MariaDB from Node.js.
```

## With the MCP Server Connected

The following requests work with a database that you configured with `mcp setup`:

```text
What does the schema of my orders table look like?
```

```text
Why is this query slow? Run EXPLAIN on it.
```

```text
Which of my tables have no primary key?
```

```text
Deploy a test instance and try this migration on it first.
```

## With a Sandbox Instance

If you don't have a database, the agent can deploy a local MariaDB Server instance for testing:

```text
Deploy a MariaDB sandbox on port 3310.
```

```text
Spin up a test instance, apply this schema to it, and show me the result.
```

```text
Try this migration on a sandbox before I run it for real.
```

```text
Stop and delete the sandbox, I'm done with it.
```

See [Sandbox Instances](features/sandbox-instances.md).

## A Complete Example

The following request uses both the skills and the MCP server. The agent designs the schema with the help of the skills, and uses the MCP tools to deploy a server and run the script:

```text
Create a MariaDB database schema for a note-taking app and store it in
notes_app.sql. Then spin up a sandbox instance on port 3310, connect to it,
and run the script. Finally, list the tables you created.
```

To complete the request, the agent calls `sandbox.deploy`, then `db.connect` with the connection that the sandbox registered, then `db.execute_sql_script` with the file, and finally `db.list_objects`. The directory that contains `notes_app.sql` must be on the [allowed-paths list](configuring-the-mcp-server/README.md#allowed-paths).

## Using MariaDB Shell Yourself

You can also use MariaDB Shell directly as a SQL client. Start it with:

```bash
mariadb-shell
```

For a list of commands, enter the following at the MariaDB Shell prompt:

```text
\help
```

MariaDB Shell can also access the sandbox instances that the agent creates.
