---
description: >-
  Run the MariaDB MCP server that is included with MariaDB Shell, so that AI
  agents and other MCP clients can work with your MariaDB servers, schema
  projects, and local sandboxes.
icon: robot
---

# MCP Server

MariaDB Shell includes a [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) server. MCP is an open protocol that lets AI agents, such as coding assistants, call tools that an external server provides. The MariaDB MCP server provides tools to connect to MariaDB servers, inspect schemas, run SQL, manage versioned schema projects, and deploy local sandbox instances.

The MCP server runs inside MariaDB Shell, as the built-in `mcp` plugin. It uses the shell's own connection handling, [credential store](../connecting/credential-store.md), [sandbox](../sandbox-instances.md) functions, and SSH tunnels, and it brings its own Python runtime and libraries with the shell, so it needs no separate installation.

{% hint style="info" %}
The pages in this section describe how to set up, start, and secure the MCP server. For the tools themselves and for example requests, see the [MariaDB AI Plugins](https://mariadb.com/docs/tools/community/mariadb-ai-plugins) documentation. The AI Plugins also start the MCP server for you in Claude Code, Codex, OpenCode, and Pi; in these coding agents, you only need to [configure its access](configuring-access.md).
{% endhint %}

{% hint style="warning" %}
The MCP server is a preview feature. `mcp.info()` reports it as `PREVIEW` and for testing purposes only.
{% endhint %}

## Requirements

* A MariaDB Shell release package, installed as described in [Installation](../installation/README.md). The release packages include the `mcp` plugin; a MariaDB Shell built from source doesn't.
* An MCP client, for example a coding agent or a desktop AI application.
* For the `db` tools, a MariaDB server and an account on it. Without a server, the `sandbox` tools can deploy a local instance.

To check that the plugin is available, print its version:

```bash
mariadb-shell -- mcp version
```

## How It Works

You set up the MCP server in two steps, and then let the MCP client start it:

1. **Configure what the server may access.** `mcp setup` stores the database connections the server may open, with their passwords in the credential store, and the local directories it may read and write. Until you do this, the server refuses every connection and every path. See [Configuring Access](configuring-access.md).
2. **Register the server with your MCP client.** The client starts `mariadb-shell -- mcp start-server` as a child process and talks to it over standard input and output, or it connects to a server that you started yourself over HTTP. See [Connecting MCP Clients](connecting-mcp-clients.md).

The agent never sees the passwords. It lists the configured connections, asks the server to open one, and receives a connection ID that it uses for further calls.

This setup serves one person. To share one server among several users, each authenticated and each with their own connections, use [multi-tenant mode](multi-tenant-mode.md). Its users authenticate with an API key or with [OAuth2](oauth-authentication.md), through Keycloak or by signing in with their MariaDB account.

## Tool Groups

The server's tools are organized in function groups. By default, the server provides all of them. To provide only some, use the `--functionGroups` option of `mcp start-server`, as described in [Starting the MCP Server](starting-the-mcp-server.md#function-groups).

| Group | What its tools do |
| --- | --- |
| `db` | List the configured connections, open and close sessions, list schemas and objects, describe objects, and run SQL statements and scripts. |
| `msm` | Create and work with versioned schema projects of [MariaDB Schema Management](../schema-management/README.md), prepare releases, and deploy schemas. |
| `mrs` | Work with the files of the MariaDB REST Service: generate client SDKs, dump and load REST services and service projects, and load static content. The REST services themselves are managed with REST SQL, which the `db` tools run. |
| `sandbox` | List the server versions that can be deployed, and deploy, start, stop, and delete local sandbox instances. A sandbox's MariaDB REST Daemon starts and stops with it. |
| `migrator` | Plan and run a migration from MySQL to MariaDB. Only available on Linux and macOS, after you install the [migration tooling](migration-tooling.md) with `mcp setup`. |
| `util` | Dump, load, copy, export, and import data as [background tasks](dump-and-load-tools.md) that a client follows and can cancel. |
| `rest` | Set up, start, stop, and delete MariaDB REST Daemons for sandbox instances and other servers. |

A [multi-tenant](multi-tenant-mode.md) server provides only the `db` group. The `msm` and `mrs` tools work on files on the developer's own machine, and the `util` and `rest` tools run long jobs and local processes on the server's machine, so they are not available on a server that several users reach remotely.

## The mcp Global Object

The plugin adds the `mcp` global object to Python mode, and the `mcp` object to [command line integration](../using-mariadb-shell/command-line-integration.md):

| Python | Command line | Description |
| --- | --- | --- |
| `mcp.setup()` | `mcp setup` | Configures the connections and directories the server may access, and installs or removes the migration tooling. In multi-tenant mode, also manages the users. |
| `mcp.setup_oauth()` | `mcp setup-oauth` | Configures how a [multi-tenant](multi-tenant-mode.md) server accepts OAuth2 tokens. See [OAuth Authentication](oauth-authentication.md). |
| `mcp.setup_keycloak_realm()` | `mcp setup-keycloak-realm` | Prepares a Keycloak realm to issue tokens for the server. See [OAuth Authentication](oauth-authentication.md#using-keycloak). |
| `mcp.start_server()` | `mcp start-server` | Starts the MCP server. It runs in the foreground until it is stopped. |
| `mcp.info()` | `mcp info` | Returns a short description of the plugin. |
| `mcp.version()` | `mcp version` | Returns the version of the plugin. |

To show the built-in help, run `\? mcp` in Python mode, or `mariadb-shell -- mcp --help` on the command line.

## In This Section

{% content-ref url="configuring-access.md" %}
[configuring-access.md](configuring-access.md)
{% endcontent-ref %}

{% content-ref url="migration-tooling.md" %}
[migration-tooling.md](migration-tooling.md)
{% endcontent-ref %}

{% content-ref url="automated-setup.md" %}
[automated-setup.md](automated-setup.md)
{% endcontent-ref %}

{% content-ref url="starting-the-mcp-server.md" %}
[starting-the-mcp-server.md](starting-the-mcp-server.md)
{% endcontent-ref %}

{% content-ref url="dump-and-load-tools.md" %}
[dump-and-load-tools.md](dump-and-load-tools.md)
{% endcontent-ref %}

{% content-ref url="connecting-mcp-clients.md" %}
[connecting-mcp-clients.md](connecting-mcp-clients.md)
{% endcontent-ref %}

{% content-ref url="multi-tenant-mode.md" %}
[multi-tenant-mode.md](multi-tenant-mode.md)
{% endcontent-ref %}

{% content-ref url="oauth-authentication.md" %}
[oauth-authentication.md](oauth-authentication.md)
{% endcontent-ref %}

{% content-ref url="security-and-session-handling.md" %}
[security-and-session-handling.md](security-and-session-handling.md)
{% endcontent-ref %}
