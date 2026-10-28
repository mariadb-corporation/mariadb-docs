---
description: >-
  Configure the database connections and local directories that the MariaDB
  MCP server may access with mcp setup.
---

# Configuring Access

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

A new MCP server has no access to any database or directory. You decide what it may use with `mcp setup`, which maintains two allow-lists:

* **Connections**: the MariaDB servers and accounts that the server may open sessions with. The password of each connection is stored in the MariaDB Shell [credential store](../connecting/credential-store.md).
* **Allowed paths**: the local directories that tools may read from and write to, for example for SQL script files, schema projects, and sandbox directories.

The configuration is per operating system user and applies to every MCP server that the user starts, regardless of the MCP client. You configure it once, and run the setup again only to change it. A running server reads the allow-lists each time it needs them, so changes take effect without a restart.

{% hint style="info" %}
This page describes the configuration of a single-user server. In [multi-tenant mode](multi-tenant-mode.md), each user of the server has their own connections and allowed directories, which you configure with the same options and `--user`.
{% endhint %}

## Run the Setup

Run the setup from a terminal:

```bash
mariadb-shell -- mcp setup
```

Alternatively, run it from an interactive MariaDB Shell session. MariaDB Shell starts in SQL mode, so switch to Python mode first:

```text
\py
```

Then call the setup function:

```python
mcp.setup()
```

The setup needs a terminal, because it prompts for input. For scripts and other runs without a terminal, pass command-line options instead, as described in [Automated Setup](automated-setup.md).

### First Run

When nothing is configured yet, the setup walks you through the configuration:

1. It asks `Add a connection?` and, for each connection you add, the connection URI and the password. Answer `No` when you have added all connections.
2. It asks `Add an allowed path?` and, for each path, the directory. It suggests the current directory as the default. Answer `No` when you have added all directories.

```text
=== MariaDB MCP Server setup ===
Configuration is stored in: /home/dev/.mariadb-shell/plugin_data/mcp_plugin
Let's configure the MariaDB connections the MCP server may use.
Add a connection? [Y/n]: y
Enter the MariaDB connection URI (e.g. mariadb://user@host:3306): mcp@db.example.com
The connection will be stored as 'mariadb://mcp@db.example.com:3306'.
Enter the password for 'mariadb://mcp@db.example.com:3306':
Connection 'mariadb://mcp@db.example.com:3306' verified and stored.
Add a connection? [Y/n]: n

Now choose the local directories the MCP server is allowed to access.
Add an allowed path? [Y/n]: y
Enter a directory the MCP server may access (default: /home/dev/projects/shop):
Allowed path '/home/dev/projects/shop' added.
Add an allowed path? [Y/n]: n

Setup complete.
```

### Later Runs

When a configuration exists, the setup shows the configured connections and paths and offers a menu. Enter the number of a choice, or press Enter to finish:

```text
Configured connections:
  1. mariadb://mcp@db.example.com:3306

Allowed paths:
  1. /home/dev/projects/shop

Migration tooling not downloaded yet (configured release: v1.5.0).
  1) Add a connection
  2) Delete a connection
  3) Add an allowed path
  4) Delete an allowed path
  5) Download the MySQL-to-MariaDB migration tooling (v1.5.0)
  6) Finish

What would you like to do? [6]:
```

Choice 5 installs the [migration tooling](migration-tooling.md), or removes it when it is installed. On Windows, the menu has no entry for the migration tooling, so `Finish` is choice 5.

## Connections

Each connection consists of a connection URI and a password. The URI uses the same format as everywhere else in MariaDB Shell; see [Connection URIs and Options](../connecting/connection-uris-and-options.md). For example:

```text
mariadb://mcp@db.example.com:3306
mariadb://mcp@db.example.com:3306?ssl-mode=VERIFY_IDENTITY&ssl-ca=/etc/ssl/certs/db-ca.pem
mariadb+ssh://mcp@db.internal:3306?ssh-host=bastion.example.com&ssh-user=tunnel
```

When you add a connection, the setup does the following:

1. It normalizes the URI and shows the form it stores, if that differs from what you entered. A missing scheme becomes `mariadb://`, and a missing port becomes `3306`.
2. It prompts for the password of the account.
3. It verifies the connection by opening a session and closing it again. If this fails, it reports the error and doesn't store the connection.
4. It stores the password in the credential store, under a key that starts with `MCP:CONN:` followed by the normalized URI.

Adding a connection that is already configured updates its password.

{% hint style="danger" %}
Enter the password at the prompt. Don't write it into the URI: the setup removes a password from a URI that you enter in the walkthrough, and refuses a URI with a password on the command line.
{% endhint %}

### Use a Dedicated Account

The connection list controls which servers the agent can reach. What the agent can do on a server depends only on the privileges of the account. Don't configure the MCP server with an administrator account, `root`, or your personal account. Create a dedicated account with only the privileges the agent needs, for example read-only access to production schemas and full access to a development schema:

{% code title="create-mcp-account.sql" %}
```sql
CREATE USER 'mcp'@'10.0.0.%'
  IDENTIFIED BY 'replace-with-a-generated-password'
  WITH MAX_USER_CONNECTIONS 10
       MAX_STATEMENT_TIME 60;

GRANT SELECT, SHOW VIEW ON `shop`.* TO 'mcp'@'10.0.0.%';
GRANT ALL PRIVILEGES ON `shop_dev`.* TO 'mcp'@'10.0.0.%';
```
{% endcode %}

`ALL PRIVILEGES` at the schema level doesn't include `GRANT OPTION`, so the account can't pass its privileges on. The resource limits keep a runaway query or a loop of connections from affecting other users of the server.

### Schemas and Options Are Part of the Connection

The server compares the URI that the agent asks for with the configured connections. Spellings that mean the same connection match: a missing scheme, `mysql://` instead of `mariadb://`, a missing default port, or a different capitalization of the host name.

A default schema, connection options, and the scheme are part of the connection. If you configure `mariadb://mcp@db.example.com:3306?ssl-mode=VERIFY_IDENTITY`, the server refuses to open the same server without `ssl-mode`, and if you configure a `mariadb+ssh://` URI, the server refuses a `mariadb://` URI for the same host. This way, the options you configure always apply, and the agent can't bypass a tunnel or TLS by accident.

In most cases, leave the default schema out of the URI. The agent then works with every schema the account has privileges on. The agent finds the configured URIs with the `db.list_connections` tool.

### Connections Through SSH Tunnels

For a server that is only reachable through an SSH host, add a `mariadb+ssh://` URI, as described in [SSH Tunnels](../connecting/ssh-tunnels.md). The MCP server runs without a terminal and can't prompt for an SSH password, a key passphrase, or the confirmation of a host key, so prepare the tunnel accordingly:

* Use a key without a passphrase that is only used for the tunnel, referenced with `ssh-identity-file`, or load the key into the SSH agent before you start the MCP client. The MCP client must pass `SSH_AUTH_SOCK` on to the server.
* Add the host key of the SSH host to `~/.ssh/known_hosts` before the agent uses the connection. When you add a `mariadb+ssh://` connection, the setup verifies it through the tunnel and asks you to confirm an unknown host key, then stores it. Alternatively, connect once with `ssh` and accept the key there.

The password that the setup asks for is the password of the database account, not an SSH password.

### Stored Separately from Other Connections

The MCP connections are stored apart from the passwords that MariaDB Shell saves for your own connections. The agent can only open the connections you configure for the MCP server, never the other servers you work with in MariaDB Shell.

To read the password of an MCP connection yourself, list the secrets with `shell.list_secrets()`, find the entry that starts with `MCP:CONN:`, and pass it to `shell.read_secret()`. See [Credential Store](../connecting/credential-store.md#storing-secrets).

### Remove a Connection

Removing a connection revokes the agent's access to it. The server checks the configured connections each time it opens a session, so it refuses the next session for a removed connection. A session that is in continuous use can stay open until it reaches its maximum lifetime of 12 hours. If a removal must take effect immediately, restart the MCP server. See [Security and Session Handling](security-and-session-handling.md#session-lifetime).

## Allowed Paths

Tools that take a file or directory path accept only paths within the allowed directories or their subdirectories. This applies to SQL script files of `db.execute_sql_script`, to the schema projects of the `msm` tools, to the files and folders of the `rest` tools, to the sandbox directories of the `sandbox` tools, to the files and folders that the `util` tools write or read, and to the `mariadb-restd` executable and the deployment folders of the `restd` tools that the server did not create itself. Each directory must exist when you add it. An empty list allows no path at all.

When a tool receives a path outside the allowed directories, the server asks the MCP client to confirm it, using the MCP elicitation feature:

```text
The path '/home/dev/scratch' is not in the MCP server's list of allowed paths. Trust it as an allowed path?
```

If you confirm, the server adds the directory to the allowed paths permanently and continues. If you decline, or if the client doesn't support elicitation, the tool fails:

```text
Access to path '/home/dev/scratch' is not allowed. Add it (or a parent directory) to the allowed paths with mcp.setup.
```

To avoid the question, add the directories you work in beforehand. Allow project directories, not your home directory or the root directory, because the agent can read and write every file within an allowed directory.

## Show the Configuration

To print the current configuration without changing anything, run:

```bash
mariadb-shell -- mcp setup --show
```

```text
=== MariaDB MCP Server configuration ===
Configuration is stored in: /home/dev/.mariadb-shell/plugin_data/mcp_plugin

Configured connections:
  1. mariadb://mcp@db.example.com:3306

Allowed paths:
  1. /home/dev/projects/shop

Migration tooling:
  Configured release: v1.5.0
  Installed releases: (none)
  Install path:       /home/dev/.local/share/mariadb-migrator/v1.5.0
  Wrapper:            /home/dev/.local/bin/mariadb-migrator
```

Add `--json` for machine-readable output.

## Where the Configuration Is Stored

| What | Location |
| --- | --- |
| Allowed paths | `settings.json` in the plugin data directory: `~/.mariadb-shell/plugin_data/mcp_plugin/` on Linux and macOS, `%AppData%\MariaDB\mariadb-shell\plugin_data\mcp_plugin\` on Windows. The directory follows `MARIADB_SHELL_USER_CONFIG_HOME`. |
| Connections and passwords | The MariaDB Shell credential store, which uses the secret storage of the operating system by default. The entries start with `MCP:CONN:`. |

{% hint style="info" %}
`MARIADB_SHELL_USER_CONFIG_HOME` moves the allowed paths. When the credential store uses the secret storage of the operating system, which is the default on macOS and Windows, it doesn't move the connections, because that storage is shared by all configuration directories of the same user.
{% endhint %}

## Troubleshooting

| Message | Cause | Solution |
| --- | --- | --- |
| *Could not connect to '…': …* followed by *The connection was not stored.* | The setup couldn't open a session with the URI and password. The message contains the error of the server or client, for example *Access denied* (error 1045) or *Can't connect to server* (error 2002). | Correct the URI, the password, or the account, and add the connection again. To store a connection to a server that isn't running yet, use `--noVerify`, as described in [Automated Setup](automated-setup.md). |
| *'…' is not a valid connection URI.* | MariaDB Shell can't parse the URI, for example because of an unknown option or a character that must be percent-encoded. | Check the URI against [Connection URIs and Options](../connecting/connection-uris-and-options.md). |
| *'…' is not an existing directory. It was not added.* | The directory doesn't exist. | Create the directory first. |
| *mcp.setup must be run from an interactive shell session, or with options* | The setup was started without options and without a terminal. | Run it in a terminal, or pass options as described in [Automated Setup](automated-setup.md). |
| *The authenticity of host '…' can't be established.* | The host key of an SSH host isn't in the known-hosts file. | Confirm the key when the setup asks, or connect once with `ssh`. |

<sub>_This page is licensed: GPLv2_</sub>
