---
description: >-
  Create a dedicated MariaDB account with limited privileges for the
  mariadb-shell MCP server, with read-only access to production schemas and
  full access to a development schema.
---

# Database Accounts for the MCP Server

The MCP server connects to MariaDB with the account of each connection that you configure with `mcp setup`. Everything the agent does on a server, it does with the privileges of this account. This page explains why the MCP server needs its own account, and shows how to create one with limited privileges.

## Why the MCP Server Needs Its Own Account

The MCP server restricts which servers the agent can connect to, but it doesn't restrict the SQL statements the agent runs on them. An agent can misread a request, run a statement on the wrong connection, or rerun a script that replaces existing tables. The privileges of the account are what limit the effect of such mistakes.

{% hint style="danger" %}
Don't configure the MCP server with your personal developer account, an administrator account, or `root`. These accounts typically have privileges on every schema, including production data, and the agent would have the same privileges.
{% endhint %}

Use a dedicated account for the MCP server instead, and follow these rules:

* Grant only the privileges the agent needs for its tasks.
* Grant read-only access to production schemas.
* Grant write access only to development or test schemas.
* Don't grant global privileges, such as privileges `ON *.*`, or `GRANT OPTION`.
* Use a separate password that you don't use for other accounts.

## Create the Account

The following example creates an account named `mcp` for a server with two production schemas, `shop` and `crm`, and a development schema, `shop_dev`. The account can read the production schemas and has full access to the development schema.

{% code title="create-mcp-account.sql" %}
```sql
-- A dedicated account for the MCP server. Replace the password with a
-- generated one. The resource limits keep a runaway query from the agent
-- from affecting other users of the server.
CREATE USER 'mcp'@'%'
  IDENTIFIED BY 'replace-with-a-generated-password'
  WITH MAX_USER_CONNECTIONS 10
       MAX_STATEMENT_TIME 60;

-- Read-only access to the production schemas.
GRANT SELECT ON `shop`.* TO 'mcp'@'%';
GRANT SELECT ON `crm`.* TO 'mcp'@'%';

-- Full access to the development schema. ALL PRIVILEGES at the schema level
-- doesn't include GRANT OPTION, so the account can't pass privileges on.
GRANT ALL PRIVILEGES ON `shop_dev`.* TO 'mcp'@'%';
```
{% endcode %}

Run these statements with an administrator account. The grants are made at the schema level, so they also apply to tables and views that are created in these schemas later.

The account can't access any other schema, can't create schemas other than `shop_dev`, and can't manage users or change the server configuration.

### Resource Limits

`MAX_USER_CONNECTIONS` limits the number of simultaneous connections of the account. `MAX_STATEMENT_TIME` cancels statements that run longer than the given number of seconds; this doesn't apply to statements within stored procedures. If the agent runs long `ALTER TABLE` statements on large tables in the development schema, increase the limit or set it to `0` to remove it.

### Reading View Definitions

With `SELECT` alone, the account can query views but can't read their definitions. If the agent should be able to explain views in a production schema, also grant `SHOW VIEW`:

```sql
GRANT SELECT, SHOW VIEW ON `shop`.* TO 'mcp'@'%';
```

## Check the Privileges

To check the privileges of the account, run:

```sql
SHOW GRANTS FOR 'mcp'@'%';
```

The output lists the `USAGE` grant that holds the resource limits, the `SELECT` grants on `shop` and `crm`, and the `ALL PRIVILEGES` grant on `shop_dev`.

## Separate Development and Production Servers

If your development and production schemas are on different servers, create the account on each server with only the grants that apply there:

* On the production server, grant `SELECT` on the production schemas only.
* On the development server, grant `ALL PRIVILEGES` on the development schemas.

Then configure a connection to each server with `mcp setup`. The agent sees both connections in `db.list_connections`, and the privileges of each account determine what it can do on that server.

## Restrict the Host

The account in the example can connect from any host (`'%'`). If the MCP server always runs on the same machine or in the same network, restrict the account to that host or network, for example `'mcp'@'10.0.0.%'`. Use the same host part in all `CREATE USER` and `GRANT` statements.

## Configure the Connection

Add the account as a connection with `mcp setup`, for example:

```bash
mariadb-shell -- mcp setup --addConnection='mariadb://mcp@db.example.com:3306'
```

The setup prompts for the password, verifies it, and stores it in the MariaDB Shell secret store. See [Configuring the MCP Server](README.md).
