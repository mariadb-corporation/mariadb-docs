---
description: >-
  Configure the mariadb-shell MCP server with command-line options of mcp
  setup instead of the interactive walkthrough, with a reference of all
  options.
---

# Command Line Configuration

Everything you can configure in the walkthrough of `mcp setup` is also available as a command-line option. With options, you can configure the MCP server in a single command, for example in a setup script for new developer machines, and repeat the configuration exactly.

## How Options Work

Without options, `mcp setup` starts the interactive walkthrough. With at least one option, it carries out only what the options say and skips the walkthrough:

```bash
mariadb-shell -- mcp setup --addPaths=/home/dev/projects
```

The only question the setup still asks is the password of a connection that you add with `--addConnection`. To list all options with their descriptions, run:

```bash
mariadb-shell -- mcp setup --help
```

{% hint style="danger" %}
Always enter passwords at the prompt of the setup. The setup also has options that read a password from the command line, an environment variable, or standard input. This documentation doesn't cover them, because a password given that way can end up in the shell history, in the process list, or in the environment of other processes.
{% endhint %}

## Options

| Option | Description |
| --- | --- |
| `--addConnection=<uri>` | Verifies one connection and stores it. The setup asks for the password. To add several connections, run the setup once for each. Adding a connection that already exists updates its password. See [Adding Database Connections](adding-database-connections.md). |
| `--noVerify` | Stores the connection given with `--addConnection` without opening a session to check it first, for example for a server that isn't running yet. |
| `--deleteConnections=<list>` | Deletes the given connections. Any spelling of a URI that names a configured connection works. |
| `--addPaths=<list>` | Adds directories to the allowed-paths list. Each directory must already exist. |
| `--deletePaths=<list>` | Removes directories from the allowed-paths list. |
| `--installMigrator` | Downloads the MySQL-to-MariaDB migration tooling, builds its virtual environment, and installs its `mariadb-migrator` command. Linux and macOS only. |
| `--removeMigrator` | Removes all installed releases of the migration tooling and its `mariadb-migrator` command. |
| `--show` | Prints the current configuration and changes nothing. Can't be combined with options that change the configuration. |
| `--json` | Prints the output of `--show` as JSON. Only valid together with `--show`. |
| `--nonInteractive` | Never prompts. Together with `--addConnection`, the run fails, because the setup can't ask for the password. Use it for runs that only change paths or the migration tooling, or that show the configuration. |

### Lists

Options that take a list expect the values separated by commas, without spaces:

```bash
mariadb-shell -- mcp setup --addPaths=/home/dev/projects,/home/dev/scratch
```

Giving the same option more than once isn't supported. To add several directories, list them in one option.

### Options Without a Value

Options such as `--show`, `--installMigrator`, or `--noVerify` take no value. Giving the option switches the setting on.

### Quoting

Put connection URIs in single quotes. URIs can contain characters such as `?`, `&`, and `(`, which have a special meaning in the shell.

## Order of Operations

You can combine several options in one call. The setup then carries them out in a fixed order, regardless of the order on the command line:

1. Deletions of connections and paths.
2. Additions of connections and paths.
3. Installation or removal of the migration tooling.

If a step fails, the setup stops. The steps that already succeeded keep their effect, and the setup reports them, so you can see how far it got. Because deletions come first, deleting and adding the same connection in one call leaves the connection added.

## Examples

Add a connection. The setup asks for the password, verifies the connection, and stores it:

```bash
mariadb-shell -- mcp setup --addConnection='mariadb://mcp@db.example.com:3306'
```

Allow two directories and install the migration tooling in one call:

```bash
mariadb-shell -- mcp setup --addPaths=/home/dev/projects,/home/dev/scratch --installMigrator
```

Remove a connection and a directory:

```bash
mariadb-shell -- mcp setup \
  --deleteConnections='mariadb://mcp@old-db.example.com:3306' \
  --deletePaths=/home/dev/scratch
```

Reinstall the migration tooling. Removal runs before installation, so this combination installs a fresh copy:

```bash
mariadb-shell -- mcp setup --removeMigrator --installMigrator
```

Show the current configuration, as text or as JSON:

```bash
mariadb-shell -- mcp setup --show
mariadb-shell -- mcp setup --show --json
```

## Server Start Options

The options on this page configure what the MCP server may access. How the server itself is started, for example with which transport, is defined by the launcher script of each plugin and doesn't need to be configured. See [Architecture](../architecture.md).
