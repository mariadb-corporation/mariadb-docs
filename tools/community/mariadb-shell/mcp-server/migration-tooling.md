---
description: >-
  Install and remove the MySQL to MariaDB migration tooling that the migrator
  tools of the MariaDB MCP server use.
---

# Migration Tooling

The `migrator` tools of the MCP server plan and run migrations from MySQL to MariaDB with the [MySQL to MariaDB migration tooling](https://github.com/mariadb-corporation/Mysql-to-MariaDB-Migration), which isn't part of MariaDB Shell. On Linux and macOS, `mcp setup` installs it for you. The tooling isn't available on Windows.

## Install the Tooling

The first run of [`mcp setup`](configuring-access.md) doesn't offer the tooling. Choose it from the menu of a [later run](configuring-access.md#later-runs), or run:

```bash
mariadb-shell -- mcp setup --installMigrator
```

The setup installs the release that the plugin is pinned to:

1. It downloads the release and extracts it to `~/.local/share/mariadb-migrator/<version>`, or to `$XDG_DATA_HOME/mariadb-migrator/<version>` when `XDG_DATA_HOME` is set.
2. It creates a Python virtual environment for the tooling, with the Python runtime included in MariaDB Shell, so no system Python is required.
3. It installs a `mariadb-migrator` command in `~/.local/bin`. If that directory isn't on your `PATH`, the setup prints the line to add.

Restart the MCP server after the installation. The server registers the `migrator` tools only if the tooling is installed when it starts; otherwise, it writes a message to standard error and serves the other groups.

## Remove the Tooling

To remove all installed releases and the `mariadb-migrator` command, choose the removal from the menu, or run:

```bash
mariadb-shell -- mcp setup --removeMigrator
```

## Check the Installation

`mcp setup --show` prints the configured release, the installed releases, and the paths, under `Migration tooling`. See [Show the Configuration](configuring-access.md#show-the-configuration).

| What | Location |
| --- | --- |
| Releases | `~/.local/share/mariadb-migrator/<version>/`, or `$XDG_DATA_HOME/mariadb-migrator/<version>/` when `XDG_DATA_HOME` is set. |
| Command | `mariadb-migrator` in `~/.local/bin/`. |
