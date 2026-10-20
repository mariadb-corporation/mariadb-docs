---
description: >-
  Start the MariaDB MCP server with mcp start-server, choose between the stdio
  and streamable HTTP transports, select the tool groups it provides, and read
  its log output.
---

# Starting the MCP Server

`mcp start-server` starts the MCP server. It runs in the foreground until it is stopped, and serves the tools to one MCP client over standard input and output, or to any number of clients over HTTP:

```bash
mariadb-shell -- mcp start-server --transport=stdio
```

In most setups, you don't run this command yourself. You register it with your MCP client, which starts the server when it needs it and stops it when it exits. See [Connecting MCP Clients](connecting-mcp-clients.md). Run the command yourself to serve over HTTP, or to test the server.

Configure the connections and directories the server may access before you start it, as described in [Configuring Access](configuring-access.md). A server without a configuration starts, but refuses every connection and every path.

## Options

| Option | Default | Description |
| --- | --- | --- |
| `--transport=<name>` | `streamable-http` | The MCP transport: `stdio` or `streamable-http`. See [Transports](#transports). |
| `--host=<address>` | `127.0.0.1` | The address that the HTTP server binds to. Only used by `streamable-http`. See [Security and Session Handling](security-and-session-handling.md#network-exposure) before you change it. |
| `--port=<number>` | `8080` | The TCP port of the HTTP server. Only used by `streamable-http`. |
| `--functionGroups=<list>` | All groups | The tool groups to provide, as a comma-separated list of `db`, `msm`, `rest`, `sandbox`, `migrator`, `util`, and `restd`. See [Function Groups](#function-groups). |
| `--allowedHosts=<list>` | None | Additional values of the HTTP `Host` header to accept, for a server that clients reach under another name, for example through a reverse proxy. Only used by `streamable-http`. See [Host and Origin Validation](security-and-session-handling.md#host-and-origin-validation). |
| `--sslCertfile=<file>` | None | A certificate, or certificate chain, in PEM format to serve HTTPS with. Requires `--sslKeyfile`. Only used by `streamable-http`. |
| `--sslKeyfile=<file>` | None | The private key of `--sslCertfile`, in PEM format. |
| `--trustedProxies=<list>` | None | The reverse proxies in front of the server, as a comma-separated list of IP addresses and networks. On requests from them, the server takes the client's address from the `X-Forwarded-For` header. Only used by `streamable-http`. See [Client Addresses Behind a Reverse Proxy](security-and-session-handling.md#client-addresses-behind-a-reverse-proxy). |
| `--maxConnections=<number>` | `64` | The maximum number of database connections the server holds open for all clients together. See [Connection Limits](security-and-session-handling.md#connection-limits). |
| `--publicUrl=<url>` | The configured URL | The URL clients reach the MCP endpoint at, which OAuth2 tokens are issued for. Overrides the URL set with `mcp setup-oauth --publicUrl` for this run. See [OAuth Authentication](oauth-authentication.md#the-public-url). |
| `--gui` | Off | Reserved for the MariaDB extension for Visual Studio Code, which starts the server with it. Don't use it for other clients: in this mode, the server allows access to every local path. Not available in multi-tenant mode. |

To show the built-in help for the options, run:

```bash
mariadb-shell -- mcp start-server --help
```

While the server runs, it disables the interactive wizards of MariaDB Shell, so that no tool waits for input that nobody can give.

## Transports

### stdio

With `--transport=stdio`, the server exchanges MCP messages over its standard input and output. The MCP client starts the server as a child process, and the server serves only that client. It exits when the client closes its standard input.

```bash
mariadb-shell -- mcp start-server --transport=stdio
```

Use `stdio` whenever the MCP client runs on the same machine and can start a command, which applies to most coding agents and desktop applications. It needs no network port, and no other process can talk to the server.

Standard output carries only MCP messages. The server redirects all other output, including messages of MariaDB Shell and of the tools, to standard error, which MCP clients typically write to their MCP log.

### Streamable HTTP

With `--transport=streamable-http`, which is the default, the server listens on an HTTP port and serves every client that connects to it. The MCP endpoint is `/mcp`:

```bash
mariadb-shell -- mcp start-server --port=8080
```

```text
INFO:     Started server process [84513]
INFO:     Waiting for application startup.
StreamableHTTP session manager started
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8080 (Press CTRL+C to quit)
```

Clients connect to `http://127.0.0.1:8080/mcp`. Press Ctrl+C to stop the server.

Use HTTP when the client can't start a command, when several clients share one server, or when you want to watch the server's output while you work. The HTTP server writes its startup messages to standard error and one access log line for each request to standard output.

{% hint style="danger" %}
Unless it runs in [multi-tenant mode](multi-tenant-mode.md), the MCP server has no authentication. Every client that can reach the HTTP port can open the configured connections with the stored passwords. Keep the default `--host=127.0.0.1`, which accepts connections from the local machine only. See [Security and Session Handling](security-and-session-handling.md#network-exposure).
{% endhint %}

### Serve HTTPS

To serve HTTPS instead of HTTP, pass a certificate and its private key in PEM format:

```bash
mariadb-shell -- mcp start-server --port=8443 \
  --sslCertfile=/etc/mariadb-mcp/server.pem --sslKeyfile=/etc/mariadb-mcp/server-key.pem
```

Clients then connect to `https://<host>:8443/mcp`. A [multi-tenant](multi-tenant-mode.md) server, whose requests carry the users' credentials, warns when it listens on a non-loopback address without HTTPS.

### Which Transport to Use

| | stdio | Streamable HTTP |
| --- | --- | --- |
| Started by | The MCP client | You |
| Clients | One, the process that started it | Any number |
| Network port | None | `--port`, on `127.0.0.1` by default |
| Ends | When the client exits | When you stop it |
| Idle sessions closed after 30 minutes | No | Yes |
| Multi-tenant mode | Not available | Available |

## Function Groups

By default, the server provides all tool groups. To restrict what an agent can do, provide only the groups it needs:

```bash
mariadb-shell -- mcp start-server --transport=stdio --functionGroups=db
```

| Group | Provides |
| --- | --- |
| `db` | Tools for the configured database connections. |
| `msm` | Tools for MariaDB Schema Management projects. The `msm.deploy_schema` tool deploys onto a connection opened with the `db` tools, so the server provides it only when `db` is enabled as well. |
| `rest` | Tools for the files of the MariaDB REST Service: client SDKs, dumps of REST services and service projects, and static content. The tools that work on a REST service through a connection opened with the `db` tools are provided only when `db` is enabled as well. |
| `sandbox` | Tools for local sandbox instances. |
| `migrator` | Tools for the migration from MySQL to MariaDB. The server registers them only if the migration tooling is installed; see [Migration Tooling](migration-tooling.md). |
| `util` | Tools that dump, load, copy, export, and import data as background tasks; see [Dump and Load Tools](dump-and-load-tools.md). They work on connections opened with the `db` tools, so the server provides them only when `db` is enabled as well. |
| `restd` | Tools that set up, start, stop, and delete MariaDB REST Daemons; see REST Daemon Tools. The `restd.configure_restd` tool sets a daemon up for a connection opened with the `db` tools, so the server provides it only when `db` is enabled as well. |

For example, a server for an agent that should only read schemas and run queries on configured servers provides `db`. A server for schema development on local sandboxes provides `db,msm,sandbox`.

When the migration tooling isn't installed, the server writes this message to standard error at startup and serves the other groups:

```text
2026-10-05T20:25:50+0200 [mcp] migration tools not registered: the MySQL-to-MariaDB migration tooling (v1.5.0) is not installed in '/home/dev/.local/share/mariadb-migrator'
```

### Tool Names

Each tool is named after its group and its function, separated by a dot, for example `db.list_connections`. The MCP specification allows dots in tool names, but some gateways and model APIs accept only letters, digits, hyphens, and underscores. Arcade is one of them. For these, publish the tool names with another separator:

```bash
mariadb-shell -- mcp setup --toolNameSeparator=_
```

The server then provides `db_list_connections`, `msm_create_project`, and so on. The tools' descriptions and error messages refer to the other tools by the same names, so an agent is never told to call a tool that doesn't exist. The setting takes effect when the server starts. To return to dots, run `mcp setup --toolNameSeparator=.`.

## Multi-Tenant Servers

When [multi-tenant mode](multi-tenant-mode.md) is on, `mcp start-server` serves authenticated users: it refuses `--transport=stdio` and `--gui`, provides only the `db` group, and refuses to start if `--functionGroups` names another group, or if there is no enabled user and no OAuth2 mode that creates users at sign-in. In an [OAuth2](oauth-authentication.md) mode, it also needs a public URL, from `mcp setup-oauth --publicUrl` or from its own `--publicUrl`. Everything else on this page applies unchanged.

## Log Output

The server writes one line to standard error for each event that concerns a database connection, with either transport:

* a connection opened, with the configured URI and the client it is bound to
* a use of a connection refused, because the request came from another client
* a connection refused, because the client couldn't be identified
* an idle session closed, or a session that failed to close

A multi-tenant server adds the user to each line, by the name given with `mcp setup --name`, and also logs refused API keys and tokens, sign-ins to the [built-in authorization server](oauth-authentication.md#using-the-built-in-authorization-server), and the end of each sign-in. A user without a name is left out of the line:

```text
2026-10-06T16:34:24+0200 [mcp] db.connect: opened a connection on 'mariadb://ada@db.example.com:3306' (mcp) for address=203.0.113.24 user='Ada Lovelace'
2026-10-06T17:13:44+0200 [mcp] auth: REFUSED a bearer token from address=203.0.113.24
```

```text
2026-08-07T14:03:11+0200 [mcp] db.connect: opened a connection on 'mariadb://mcp@db.example.com:3306' (mcp) for address=127.0.0.1
2026-08-07T14:37:44+0200 [mcp] db: closed the idle session of a connection on 'mariadb://mcp@db.example.com:3306' (mcp) for address=127.0.0.1 after 1800s unused; the connection stays valid and opens a new session when it is used again
```

The log doesn't contain the SQL statements that clients run, and no part of any ID: connections are named by their URI, and users by their name. Connection IDs, MCP session IDs, user IDs, API keys, tokens, and OAuth client IDs are never logged, not even in part, because a client that knows them could use them. For the meaning of the client binding, see [Security and Session Handling](security-and-session-handling.md#connections-belong-to-the-client-that-opened-them).

To keep the log of an HTTP server, redirect standard error to a file:

```bash
mariadb-shell -- mcp start-server --port=8080 2>> ~/mcp-server.log
```

For a `stdio` server, the MCP client captures standard error. Check the MCP log of the client.

## Troubleshooting

| Message or symptom | Cause | Solution |
| --- | --- | --- |
| *Unsupported transport '…'. Supported transports are: streamable-http, stdio.* | The value of `--transport` is misspelled, or names a transport that the server doesn't support, such as `sse`. | Use `stdio` or `streamable-http`. |
| *Unknown function group(s): …* | `--functionGroups` names a group that doesn't exist. | Use `db`, `msm`, `rest`, `sandbox`, `migrator`, `util`, or `restd`. |
| *There is no object registered under name 'mcp'* | The `mcp` plugin isn't installed, for example in a MariaDB Shell built from source, or plugins are disabled with `--disable-builtin-plugins`. | Install a MariaDB Shell release package. |
| *error while attempting to bind on address ('127.0.0.1', 8080): … address already in use* | Another process uses the port. | Choose another port with `--port`. |
| A client receives HTTP status `421 Misdirected Request`. | The client uses a host name that the server doesn't accept. | Add the name with `--allowedHosts`. See [Host and Origin Validation](security-and-session-handling.md#host-and-origin-validation). |
| No `migrator` tools | The migration tooling isn't installed, or the server was started before it was installed. | Install it with `mcp setup --installMigrator`, then restart the server. |
| *This server is configured for multi-tenant mode, which serves authenticated users over HTTP only* | Multi-tenant mode is on, and the server was started with `--transport=stdio`. | Use `--transport=streamable-http`, or turn multi-tenant mode off. See [Multi-Tenant Mode](multi-tenant-mode.md). |
| A gateway refuses the server's tools with *tool name must only contain ASCII letters, numbers, and the dash and underscore characters*. | The gateway doesn't accept dots in tool names. | Run `mcp setup --toolNameSeparator=_` and restart the server. See [Tool Names](#tool-names). |
| *--trustedProxies takes IP addresses and networks (such as 192.0.2.3 or 192.0.2.0/24); not: …* | An entry of `--trustedProxies` is a host name or misspelled. | Give the proxies' IP addresses or networks. |
| *--trustedProxies cannot trust every address (…)* | `--trustedProxies` contains `0.0.0.0/0` or `::/0`. | Name the proxies themselves. |
| *Give both --sslCertfile and --sslKeyfile to serve HTTPS, or neither.* | Only one of `--sslCertfile` and `--sslKeyfile` was given. | Pass both. |
