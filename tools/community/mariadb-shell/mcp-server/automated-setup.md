---
description: >-
  Configure the MariaDB MCP server without prompts, with the command-line
  options of mcp setup, for provisioning scripts, new developer machines, and
  CI jobs.
---

# Automated Setup

Every step of the interactive setup is also available as a command-line option of `mcp setup`. With options, you can configure the MCP server in one command, repeat the configuration exactly on other machines, and run it where no terminal is available, for example in a provisioning script or a CI job.

## How Options Work

Without options, `mcp setup` starts the interactive walkthrough described in [Configuring Access](configuring-access.md). With at least one option, it carries out only what the options say and skips the walkthrough:

```bash
mariadb-shell -- mcp setup --addPaths=/home/dev/projects
```

The only question it can still ask is the password of a connection that you add with `--addConnection`, unless you provide the password with one of the password options or forbid prompts with `--nonInteractive`.

To list all options with their descriptions, run:

```bash
mariadb-shell -- mcp setup --help
```

The options follow the rules of [command line integration](../using-mariadb-shell/command-line-integration.md). The help lists them in camelCase, and kebab-case such as `--add-paths` works as well.

## Options

| Option | Description |
| --- | --- |
| `--addConnection=<uri>` | Verifies one connection and stores it. Takes one URI, because each connection needs its own password; to add several connections, run the setup once for each. Adding a connection that already exists updates its password. A URI that contains a password is refused. |
| `--passwordStdin` | Reads the password for `--addConnection` from the first line of standard input. Refused when standard input is a terminal. |
| `--passwordEnv=<name>` | Reads the password for `--addConnection` from the environment variable with this name. Pass the name of the variable, not the password. The variable must be set; an empty value is an empty password. |
| `--password=<password>` | The password for `--addConnection`. Not recommended; see [Passwords](#passwords). |
| `--noVerify` | Stores the connection without opening a session to check it first, for example for a server that isn't running yet. |
| `--deleteConnections=<list>` | Deletes connections. Any spelling of a URI that names a configured connection works. |
| `--addPaths=<list>` | Adds directories to the allowed paths. Each directory must exist. |
| `--deletePaths=<list>` | Removes directories from the allowed paths. |
| `--installMigrator` | Downloads the migration tooling, creates its virtual environment, and installs the `mariadb-migrator` command. Linux and macOS only. |
| `--removeMigrator` | Removes all installed releases of the migration tooling and the `mariadb-migrator` command. |
| `--toolNameSeparator=<separator>` | The character between a tool's group and its name in the tool names that the server provides: `.` (the default), `_`, or `-`. Use `_` for gateways that refuse dots, such as Arcade. See [Tool Names](starting-the-mcp-server.md#tool-names). |
| `--nonInteractive` | Never prompts. A password that isn't provided with a password option is an error, so an automated run fails instead of waiting for input. |
| `--show` | Prints the current configuration and changes nothing. Can't be combined with options that change the configuration. |
| `--json` | Prints the output of `--show` as JSON. Only valid together with `--show`. |

The options for [multi-tenant mode](multi-tenant-mode.md), which manage users, API keys, and each user's connections and directories, are described in [Options of mcp setup for Multi-Tenant Mode](multi-tenant-mode.md#options-of-mcp-setup-for-multi-tenant-mode). OAuth2 has its own command, `mcp setup-oauth`, described in [OAuth Authentication](oauth-authentication.md#options-of-mcp-setup-oauth).

Options that take a list expect the values separated by commas, without spaces. Giving the same option more than once isn't supported; put all values into one option:

```bash
mariadb-shell -- mcp setup --addPaths=/home/dev/projects,/home/dev/scratch
```

Options without a value, such as `--show` or `--noVerify`, switch the setting on.

Put connection URIs in single quotes, because characters such as `?`, `&`, and `(` have a special meaning in the shell.

## Passwords

At most one password option is allowed per call. If you give none, the setup prompts for the password, as long as a terminal is available.

* **At a terminal**, let the setup prompt for the password. Nothing ends up in the shell history or the process list.
* **In a CI job**, use `--passwordEnv` with a variable that the CI system fills from its secret storage.
* **From a secret manager**, pipe the password into `--passwordStdin`.

{% hint style="danger" %}
Avoid `--password`. A password on the command line is visible to other users in the process list, and it is saved in the shell history.
{% endhint %}

Add `--nonInteractive` to every unattended run, so that a missing password stops the run with an error instead of waiting for input.

## Order of Operations

You can combine several options in one call. The setup carries them out in a fixed order, regardless of their order on the command line:

1. Deletions of connections and paths.
2. Additions of connections and paths.
3. Removal, then installation of the migration tooling.

If a step fails, the setup stops. The steps that already succeeded keep their effect, and the setup reports them, so you can see how far it got. Because deletions come first, deleting and adding the same connection in one call leaves the connection added, and `--removeMigrator --installMigrator` reinstalls the migration tooling.

A setup script can run repeatedly: adding a path that is already allowed changes nothing, and adding a connection that already exists only updates its password.

## Examples

Add a connection at a terminal. The setup prompts for the password, verifies the connection, and stores it:

```bash
mariadb-shell -- mcp setup --addConnection='mariadb://mcp@db.example.com:3306'
```

Add a connection in a CI job, from a variable that the CI system provides:

```bash
mariadb-shell -- mcp setup --addConnection='mariadb://mcp@db.example.com:3306' \
  --passwordEnv=MCP_DB_PASSWORD --nonInteractive
```

Add a connection with a password from a secret manager, here HashiCorp Vault:

```bash
vault kv get -field=password secret/mcp-db \
  | mariadb-shell -- mcp setup --addConnection='mariadb://mcp@db.example.com:3306' --passwordStdin
```

Register a connection to a sandbox that a later step deploys, without verifying it now:

```bash
mariadb-shell -- mcp setup --addConnection='mariadb://root@127.0.0.1:3310' \
  --passwordEnv=SANDBOX_ROOT_PASSWORD --noVerify --nonInteractive
```

Allow two directories and install the migration tooling:

```bash
mariadb-shell -- mcp setup --addPaths=/home/dev/projects,/home/dev/scratch --installMigrator
```

Remove a connection and a directory:

```bash
mariadb-shell -- mcp setup \
  --deleteConnections='mariadb://mcp@old-db.example.com:3306' \
  --deletePaths=/home/dev/scratch
```

Print the configuration as JSON, for example to check it in a script:

```bash
mariadb-shell -- mcp setup --show --json
```

```json
{
  "config_path": "/home/dev/.mariadb-shell/plugin_data/mcp_plugin",
  "connections": [
    "mariadb://mcp@db.example.com:3306"
  ],
  "allowed_paths": [
    "/home/dev/projects",
    "/home/dev/scratch"
  ],
  "migrator": {
    "supported": true,
    "configured_release": "v1.5.0",
    "installed_releases": [
      "v1.5.0"
    ],
    "install_path": "/home/dev/.local/share/mariadb-migrator/v1.5.0",
    "wrapper_path": "/home/dev/.local/bin/mariadb-migrator"
  }
}
```

## Exit Codes and Errors

The setup returns `0` on success and `1` on failure, and prints the reason to standard error:

| Message | Cause |
| --- | --- |
| *The connection URI carries a password.* | The URI given to `--addConnection` contains a password, for example `mcp:secret@db.example.com`. Remove it and use a password option or the prompt. |
| *No password given and --nonInteractive forbids asking for one.* | `--addConnection` was used with `--nonInteractive` but without a password option. |
| *--passwordEnv names '…', which is not set in the environment.* | The environment variable doesn't exist. |
| *Give exactly one of --password, --passwordEnv …* | More than one password option was given. |
| *--show only reports the configuration, so it cannot be combined with …* | `--show` was combined with an option that changes the configuration. |
| *--json only applies to --show.* | `--json` was used without `--show`. |
| *'…' is not an existing directory.* | A directory given to `--addPaths` doesn't exist. |
| *Could not connect to '…': …* | The verification of a connection failed. The message contains the error of the server or client. |
