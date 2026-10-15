---
description: >-
  Register the MariaDB MCP server with Claude Code, Codex, Visual Studio Code,
  Claude Desktop, and other MCP clients, over stdio or streamable HTTP.
---

# Connecting MCP Clients

An MCP client uses the MariaDB MCP server in one of two ways:

* **It starts the server itself**, over the `stdio` transport. You register a command, and the client runs it whenever it needs the server. This is the usual setup on a developer machine.
* **It connects to a running server**, over the `streamable-http` transport. You start the server yourself, as described in [Starting the MCP Server](starting-the-mcp-server.md#streamable-http), and register its URL.

Configure the connections and directories the server may access before you use it with a client. See [Configuring Access](configuring-access.md).

{% hint style="info" %}
The [MariaDB AI Plugins](https://mariadb.com/docs/tools/community/mariadb-ai-plugins) register the MCP server with Claude Code, Codex, OpenCode, and Pi automatically, and install MariaDB Shell if needed. If you use one of these coding agents, install the plugin instead of registering the server by hand.
{% endhint %}

## The Server Command

Every client that starts the server over `stdio` needs the same command and arguments:

| Setting | Value |
| --- | --- |
| Command | `mariadb-shell`, or its absolute path |
| Arguments | `--`, `mcp`, `start-server`, `--transport=stdio` |

The `--` separates the options of MariaDB Shell from the [command line integration](../using-mariadb-shell/command-line-integration.md) call that follows. To provide only some tool groups, add an argument such as `--functionGroups=db,sandbox`.

Many clients, particularly desktop applications, don't start the command from a login shell and don't see the `PATH` of your terminal. If the client reports that it can't find `mariadb-shell`, use the absolute path. To find it, run:

{% tabs %}
{% tab title="Linux and macOS" %}
```bash
command -v mariadb-shell
```

The installation script links the command into `~/.local/bin` by default, for example `/home/dev/.local/bin/mariadb-shell`.
{% endtab %}

{% tab title="Windows" %}
```batch
where mariadb-shell
```

The installation script writes the command file to `%LOCALAPPDATA%\Programs\mariadb-shell\bin\mariadb-shell.cmd` by default. Clients start commands without a command interpreter, so they can't run a `.cmd` file directly. Register `cmd` as the command, and put `/c` and the path of `mariadb-shell.cmd` in front of the other arguments, as shown in the examples below.
{% endtab %}
{% endtabs %}

## Claude Code

Register the server with the `claude mcp add` command. Everything after the first `--` is the server command:

```bash
claude mcp add --scope user mariadb -- mariadb-shell -- mcp start-server --transport=stdio
```

`--scope user` makes the server available in all your projects. Use `--scope project` to write the registration to the `.mcp.json` file of the current project instead, which you can share with your team through version control:

{% code title=".mcp.json" %}
```json
{
  "mcpServers": {
    "mariadb": {
      "type": "stdio",
      "command": "mariadb-shell",
      "args": ["--", "mcp", "start-server", "--transport=stdio"],
      "env": {}
    }
  }
}
```
{% endcode %}

To connect to a running HTTP server instead:

```bash
claude mcp add --scope user --transport http mariadb http://127.0.0.1:8080/mcp
```

To check the connection, run `/mcp` in Claude Code.

## Codex

Register the server with the `codex mcp add` command:

```bash
codex mcp add mariadb -- mariadb-shell -- mcp start-server --transport=stdio
```

The command adds the server to `~/.codex/config.toml`:

{% code title="~/.codex/config.toml" %}
```toml
[mcp_servers.mariadb]
command = "mariadb-shell"
args = ["--", "mcp", "start-server", "--transport=stdio"]
```
{% endcode %}

To connect to a running HTTP server instead, pass its URL:

```bash
codex mcp add mariadb --url http://127.0.0.1:8080/mcp
```

## Visual Studio Code

In Visual Studio Code, MCP servers are available to the agent mode of GitHub Copilot. Add the server to the `.vscode/mcp.json` file of your workspace, or to your user configuration with the **MCP: Open User Configuration** command:

{% code title=".vscode/mcp.json" %}
```json
{
  "servers": {
    "mariadb": {
      "type": "stdio",
      "command": "mariadb-shell",
      "args": ["--", "mcp", "start-server", "--transport=stdio"]
    }
  }
}
```
{% endcode %}

To connect to a running HTTP server instead:

{% code title=".vscode/mcp.json" %}
```json
{
  "servers": {
    "mariadb": {
      "type": "http",
      "url": "http://127.0.0.1:8080/mcp"
    }
  }
}
```
{% endcode %}

## Claude Desktop

Claude Desktop reads its MCP servers from `claude_desktop_config.json`. To open the file, choose **Settings**, then **Developer**, then **Edit Config**. The file is in `~/Library/Application Support/Claude/` on macOS and in `%APPDATA%\Claude\` on Windows.

Claude Desktop doesn't see the `PATH` of your terminal, so use the absolute path of MariaDB Shell:

{% tabs %}
{% tab title="macOS" %}
{% code title="claude_desktop_config.json" %}
```json
{
  "mcpServers": {
    "mariadb": {
      "command": "/Users/dev/.local/bin/mariadb-shell",
      "args": ["--", "mcp", "start-server", "--transport=stdio"]
    }
  }
}
```
{% endcode %}
{% endtab %}

{% tab title="Windows" %}
{% code title="claude_desktop_config.json" %}
```json
{
  "mcpServers": {
    "mariadb": {
      "command": "cmd",
      "args": [
        "/c",
        "C:\\Users\\dev\\AppData\\Local\\Programs\\mariadb-shell\\bin\\mariadb-shell.cmd",
        "--", "mcp", "start-server", "--transport=stdio"
      ]
    }
  }
}
```
{% endcode %}
{% endtab %}
{% endtabs %}

Restart Claude Desktop after you change the file.

## Other Clients

Most other clients, such as Cursor and Windsurf, use the same `mcpServers` format as Claude Desktop, in a file of their own. Register the [server command](#the-server-command) under a name such as `mariadb`. For a client that supports only HTTP, start the server with `--transport=streamable-http` and register `http://127.0.0.1:8080/mcp`, with the port you chose.

## Multi-Tenant Servers

A [multi-tenant](multi-tenant-mode.md) server only serves over HTTP, and every request must carry the user's credentials:

* **With an API key**, register the URL with an `Authorization: Bearer <API key>` header. See [Connect a Client with an API Key](multi-tenant-mode.md#connect-a-client-with-an-api-key).
* **With OAuth2**, register only the URL. The client discovers the authorization server and runs the sign-in in your browser. In Claude Code, run `/mcp`, select the server, and choose **Authenticate**. See [OAuth Authentication](oauth-authentication.md#connecting-a-client-with-oauth2).

## Environment of the Server

A server that the client starts inherits the client's environment. This matters in the following cases:

* **SSH tunnels with the SSH agent.** For [connections through SSH tunnels](configuring-access.md#connections-through-ssh-tunnels) that use a key from the SSH agent, the client must pass on `SSH_AUTH_SOCK`. Start the client from a terminal in which the agent is available, or use a key file without a passphrase.
* **A different configuration directory.** If you set `MARIADB_SHELL_USER_CONFIG_HOME` when you ran `mcp setup`, set it for the server as well, for example in the `env` section of the client's configuration. Otherwise, the server doesn't find the allowed paths.
* **Sandbox servers.** The `sandbox` tools look for `mariadbd` on the `PATH` of the server, before they download a server package. To use a server installation that isn't on the client's `PATH`, add its `bin` directory to the `PATH` in the `env` section.

## Several Configurations

The allow-lists apply to every server the same user starts. To give different agents different tools, register the server several times under different names, each with its own `--functionGroups`:

```bash
claude mcp add --scope project mariadb-readonly -- mariadb-shell -- mcp start-server --transport=stdio --functionGroups=db
```

To restrict the databases themselves, use accounts with different privileges, as described in [Configuring Access](configuring-access.md#use-a-dedicated-account).

## Troubleshooting

| Symptom | Cause | Solution |
| --- | --- | --- |
| The client reports that the server failed to start, or that `mariadb-shell` wasn't found. | The client doesn't see the directory of `mariadb-shell` on its `PATH`. | Use the absolute path. On Windows, start `mariadb-shell.cmd` through `cmd /c`. |
| The client connects, but every `db.connect` call fails with *not a configured connection*. | No connection is configured, or the agent asked for a URI that differs from the configured one, for example with an added schema. | Configure the connection with `mcp setup`. The agent finds the configured URIs with `db.list_connections`. |
| `db.connect` fails with *This client uses MCP without sessions (protocol revision 2026-07-28)…* | The client uses the current MCP revision, which has no sessions, over HTTP with a server that doesn't authenticate. | Register the server over `stdio`, or use [multi-tenant mode](multi-tenant-mode.md). See [Clients Without MCP Sessions](security-and-session-handling.md#clients-without-mcp-sessions). |
| Tools that take a path fail with *Access to path '…' is not allowed*. | The directory isn't an allowed path, and the client doesn't support the confirmation question. | Add the directory with `mcp setup --addPaths`. |
| The `stdio` server stops immediately after it starts. | The client closed the server's standard input, or the command has wrong arguments. | Run the command in a terminal to see its error output, and check the client's MCP log. |
