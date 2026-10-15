---
description: >-
  Configure the connections and directories that the mariadb-shell MCP server
  may access, and optionally install the migration tooling.
---

# Configuring the MCP Server

After installation, the MCP server has no access to any database or directory. You define the connections and directories it may use with MariaDB Shell. The configuration applies to all harnesses on the machine, so you only need to do it once:

```bash
mariadb-shell -- mcp setup
```

From an interactive MariaDB Shell session, you can run the setup function instead. MariaDB Shell starts in SQL mode, so switch to Python mode first:

```text
\py
```

Then run the setup function:

```python
mcp.setup()
```

{% hint style="info" %}
The MCP server is implemented as a MariaDB Shell plugin. This way, it can use the database connections, credential management, sandbox handling, and schema management of MariaDB Shell.
{% endhint %}

## Locate MariaDB Shell

If `mariadb-shell` isn't on your `PATH`, use the copy the plugin's launcher installed:

{% tabs %}
{% tab title="Linux and macOS" %}
```bash
~/.local/bin/mariadb-shell -- mcp setup
```
{% endtab %}

{% tab title="Windows" %}
```batch
%LOCALAPPDATA%\Programs\mariadb-shell\bin\mariadb-shell.cmd -- mcp setup
```
{% endtab %}
{% endtabs %}

The installer doesn't add this directory to your `PATH`; it only prints a hint. Because the launcher installs MariaDB Shell when the MCP server starts for the first time, either start the agent once before you run the setup, or install MariaDB Shell yourself.

## What the Setup Configures

### Connections

The setup asks for the connection URIs of the databases the agent may connect to. For the format of the URI and its options, see [Adding Database Connections](adding-database-connections.md). To reach a server through an SSH host, use a `mariadb+ssh://` URI, as described in [Tunnel Database Connections via SSH](tunnel-database-connections-via-ssh.md). For each connection, it prompts for the password, verifies it, and stores it in the MariaDB Shell secret store, separately from your other MariaDB Shell connections. The agent has no access to the passwords.

{% hint style="warning" %}
Use a dedicated MariaDB account for each connection, and grant it only the privileges the agent needs, for example read-only access to specific schemas. The MCP server controls which servers the agent can connect to, but the account privileges determine what the agent can do on them. See [Database Accounts for the MCP Server](database-accounts-for-the-mcp-server.md).
{% endhint %}

### Allowed Paths

The setup also asks for the local directories the MCP server may read from and write to, and suggests the current directory as the default. All tools that access files are restricted to these directories.

### Migration Tooling

On Linux and macOS, you can optionally install the [MySQL-to-MariaDB migration tooling](https://github.com/mariadb-corporation/Mysql-to-MariaDB-Migration). The setup downloads it and extracts it to `~/.local/share/mariadb-migrator/<version>`. The initial setup doesn't offer this option. To install the tooling, run the setup again and select it from the menu, or run:

```bash
mariadb-shell -- mcp setup --installMigrator
```

Then restart the MCP server. The `migrator.*` tools are available after the restart. See [migrator Tools](../mcp-tool-reference/migrator-tools.md).

## Configure from the Command Line

Instead of the walkthrough, you can configure the MCP server with command-line options of `mcp setup`, for example in a setup script for new developer machines. Every setting of the walkthrough has an option, and you can combine several options in one call:

```bash
mariadb-shell -- mcp setup --addPaths=/home/dev/projects --installMigrator
```

For all options and their rules, see [Command Line Configuration](command-line-configuration.md).

## Change the Configuration

Run `mariadb-shell -- mcp setup` again at any time to add or remove connections and paths. To see the current configuration, run:

```bash
mariadb-shell -- mcp setup --show
```

For the complete option reference, see the [MCP server documentation](https://github.com/mariadb-corporation/mariadb-shell-plugins/blob/main/mcp_plugin/README.md#configuration-mcpsetup).

## Related Topics

{% content-ref url="database-accounts-for-the-mcp-server.md" %}
[database-accounts-for-the-mcp-server.md](database-accounts-for-the-mcp-server.md)
{% endcontent-ref %}

{% content-ref url="adding-database-connections.md" %}
[adding-database-connections.md](adding-database-connections.md)
{% endcontent-ref %}

{% content-ref url="tunnel-database-connections-via-ssh.md" %}
[tunnel-database-connections-via-ssh.md](tunnel-database-connections-via-ssh.md)
{% endcontent-ref %}

{% content-ref url="command-line-configuration.md" %}
[command-line-configuration.md](command-line-configuration.md)
{% endcontent-ref %}
