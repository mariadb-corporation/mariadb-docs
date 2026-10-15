---
description: >-
  MariaDB Shell is an interactive SQL and Python client for MariaDB Server,
  derived from MySQL Shell and built on MariaDB Connector/C.
---

# About MariaDB Shell

MariaDB Shell is a command-line client and scripting environment for MariaDB Server. It combines an SQL console with a Python interpreter, and adds utilities for logical backups, data migration, local test servers, and diagnostics.

MariaDB Shell is derived from MySQL Shell. It keeps the shell's architecture and its scripting API, but it is built against MariaDB Server sources and links MariaDB Connector/C. All connections use the classic client/server protocol. Features of MySQL Shell that depend on MySQL-only server functionality are not included; see [Differences from MySQL Shell](getting-started/differences-from-mysql-shell.md).

The executable is `mariadb-shell`. Every installation also provides the short alias `msh`.

```sh
mariadb-shell app_user@db1.example.com:3306/shop
```

## Key Features

| Feature | Description |
| --- | --- |
| SQL and Python modes | Run SQL statements interactively, or switch to Python with `\py` to script the same connection. See [SQL and Python Modes](using-mariadb-shell/sql-and-python-modes.md). |
| Interactive editing | Multi-line input, persistent per-mode history, an external editor with `\edit`, and autocompletion of SQL keywords and schema object names. See [Editing and History](using-mariadb-shell/editing-and-history.md) and [Autocompletion](using-mariadb-shell/autocompletion.md). |
| Output formats | Table, vertical, tab-separated, JSON, and NDJSON output, with optional column type information and a pager. See [Output Formats](using-mariadb-shell/output-formats.md) and [Pager](using-mariadb-shell/pager.md). |
| Flexible connections | `mariadb://` URIs, TCP/IP, Unix sockets and Windows named pipes, TLS, compression, option files, and SSH tunnels with `mariadb+ssh://`. See [Connecting to a Server](connecting/). |
| Credential store | Save passwords in the macOS Keychain, the Windows Credential Manager, or a `~/.mylogin.cnf` login path on Linux. See [Credential Store](connecting/credential-store.md). |
| Dump, load, and copy | Parallel, chunked, compressed logical dumps of an instance, schemas, or tables, to local disk or object storage, and parallel loads that can resume. The copy utilities stream directly from one server to another. MariaDB objects such as sequences, packages, and system-versioned tables are supported. See [Dump and Load](utilities/dump-and-load/). |
| Table export and import | Export one table to a delimited file, or load delimited files into a table over parallel connections. See [Table Export and Import](utilities/table-export-and-import.md). |
| Sandbox instances | Deploy, start, stop, and delete throwaway local MariaDB or MySQL servers for testing with the `sandbox` global object. See [Sandbox Instances](sandbox-instances.md). |
| Command line integration | Call any utility from your operating system shell without entering the interactive shell, for example `mariadb-shell -- util dump-schemas shop --output-url=/backups/shop`. See [Command Line Integration](using-mariadb-shell/command-line-integration.md). |
| Diagnostics | Collect server and shell state into a single archive for troubleshooting. See [Diagnostics Utilities](utilities/diagnostics-utilities.md). |
| Extensibility | Reports, extension objects, plugins, and SQL handlers written in Python. See [Extending MariaDB Shell](extending-mariadb-shell/). |
| Customization | Startup scripts, persistent configuration options, and prompt themes, including themes for Nerd Fonts and a `%vendor%` variable that shows whether you are connected to MariaDB or MySQL. See [Customizing MariaDB Shell](customizing/). |

## Supported Platforms

Release packages are built for the following platforms:

| Operating system | Architectures | Minimum version |
| --- | --- | --- |
| Linux | x86-64, ARM64 | glibc 2.34 (for example, RHEL 9, Ubuntu 22.04, Debian 12, or later) |
| macOS | x86-64 | macOS 15 |
| macOS | ARM64 (Apple silicon) | macOS 26 |
| Windows | x86-64, ARM64 | Windows 10 version 1803 or later for the installation script |

Linux distributions that use musl libc, such as Alpine Linux, are not supported. 32-bit systems are not supported.

Each package bundles its own Python runtime, so you don't need to install Python separately. See [Installation](installation/).

## Server Compatibility

MariaDB Shell is designed for MariaDB Server, and its utilities support MariaDB-specific objects and behavior. Because it uses the classic protocol, it can also connect to MySQL servers. The connected server's vendor is available in a session as `session.server_vendor`, and some features, such as dump and load, apply vendor-specific rules. For example, a dump taken from a MariaDB server can only be loaded into a MariaDB server.

To see which MariaDB Server version a build was compiled against, run:

```sh
mariadb-shell --version
```

## Versioning

MariaDB Shell versions use the format `YY.M.patch`: the last two digits of the year, the month, and a patch number. For example, version 26.9.5 is the fifth patch release of the September 2026 line. Release tags add a `v` prefix, for example `v26.9.5`.
