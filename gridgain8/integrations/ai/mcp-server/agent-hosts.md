---
description: >-
  Connect Claude Code, Cursor, or Visual Studio Code to GridGain MCP Server, from the JAR file or the container image, without storing the password in a settings file.
---

# Connecting an MCP Host

An MCP host is the application that runs your AI assistant, such as Claude Code, Cursor, or Visual Studio Code.
The host starts GridGain MCP Server when it needs the server and talks to it through standard input and output.
You do not start the server yourself. To connect a host, you add an entry for the server to the host's settings.

Before you begin:

- Install the server. See [Installing MCP Server](installation.md).
- Create a read-only account on the cluster. See [Preparing a Cluster Account](security.md#preparing-a-cluster-account).

## Choosing the Start Command

The command depends on how you installed the server.

To run the JAR file:

```json
"command": "java",
"args": ["-jar", "/opt/gridgain-mcp/gridgain-mcp-<version>.jar"]
```

Use the full path to the JAR file, because the host can start the server from any folder.

To run the container image:

```json
"command": "docker",
"args": [
  "run", "-i", "--rm",
  "-e", "GRIDGAIN_HOST",
  "-e", "GRIDGAIN_USERNAME",
  "-e", "GRIDGAIN_PASSWORD",
  "gridgain/mcp:<version>"
]
```

A `-e` option without a value, such as `-e GRIDGAIN_PASSWORD`, passes that variable from the host into the container.
If you set more variables, add an `-e` option for each of them.
To keep the audit log, also mount a volume, as described in [Keeping the Audit Log](installation.md#keeping-the-audit-log).

## Setting the Connection Variables

The host passes the variables from the `env` block of the entry to the server.
At a minimum, set the following:

| Variable | Value |
| -------- | ----- |
| `GRIDGAIN_HOST` | The address of your cluster. |
| `GRIDGAIN_USERNAME` | The user name of the account for the server. |
| `GRIDGAIN_PASSWORD` | The password of the account. |

For all other settings, see [Configuring MCP Server](configuration.md).

{% hint style="info" %}
Do not write the password into the settings file, and do not pass it as a command-line argument.
Settings files are often shared, and arguments are visible in process lists.
{% endhint %}


## Adding the Server to the Host

The examples below run the JAR file.
To run the container image, replace `command` and `args` with the container form from [Choosing the Start Command](#choosing-the-start-command).
You can also open the container example under each host.
Replace `<version>` with the server version and `db.example.com` with the address of your cluster.

{% tabs %}
{% tab title="Claude Code" %}
Create a `.mcp.json` file in the root of your project:

```json
{
  "mcpServers": {
    "gridgain": {
      "type": "stdio",
      "command": "java",
      "args": ["-jar", "/opt/gridgain-mcp/gridgain-mcp-<version>.jar"],
      "env": {
        "GRIDGAIN_HOST": "db.example.com",
        "GRIDGAIN_USERNAME": "mcp_reader",
        "GRIDGAIN_PASSWORD": "${GRIDGAIN_PASSWORD}"
      }
    }
  }
}
```

<details>

<summary>Container image example</summary>

```json
{
  "mcpServers": {
    "gridgain": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "GRIDGAIN_HOST",
        "-e", "GRIDGAIN_USERNAME",
        "-e", "GRIDGAIN_PASSWORD",
        "gridgain/mcp:<version>"
      ],
      "env": {
        "GRIDGAIN_HOST": "db.example.com",
        "GRIDGAIN_USERNAME": "mcp_reader",
        "GRIDGAIN_PASSWORD": "${GRIDGAIN_PASSWORD}"
      }
    }
  }
}
```

</details>

Claude Code replaces `${GRIDGAIN_PASSWORD}` with the value of the environment variable, so set it in your shell before you start Claude Code:

```shell
export GRIDGAIN_PASSWORD='...'
claude
```

If the variable is not set, Claude Code shows a warning in `claude mcp list` and passes the text `${GRIDGAIN_PASSWORD}` to the server as the password.
You can also write `${NAME:-default}` to give a variable a default value.

The file contains no secrets, so you can commit it to share the server with your team.

To check the result, run `claude mcp list`, or type `/mcp` in a Claude Code session.
{% endtab %}

{% tab title="Cursor" %}
Add the server to the `.cursor/mcp.json` file in your project, or to `~/.cursor/mcp.json` to use it in all projects:

```json
{
  "mcpServers": {
    "gridgain": {
      "type": "stdio",
      "command": "java",
      "args": ["-jar", "/opt/gridgain-mcp/gridgain-mcp-<version>.jar"],
      "env": {
        "GRIDGAIN_HOST": "db.example.com",
        "GRIDGAIN_USERNAME": "mcp_reader",
        "GRIDGAIN_PASSWORD": "${env:GRIDGAIN_PASSWORD}"
      }
    }
  }
}
```

<details>

<summary>Container image example</summary>

```json
{
  "mcpServers": {
    "gridgain": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "GRIDGAIN_HOST",
        "-e", "GRIDGAIN_USERNAME",
        "-e", "GRIDGAIN_PASSWORD",
        "gridgain/mcp:<version>"
      ],
      "env": {
        "GRIDGAIN_HOST": "db.example.com",
        "GRIDGAIN_USERNAME": "mcp_reader",
        "GRIDGAIN_PASSWORD": "${env:GRIDGAIN_PASSWORD}"
      }
    }
  }
}
```

</details>

Cursor replaces `${env:GRIDGAIN_PASSWORD}` with the value of the environment variable.
Set the variable before you start Cursor.
{% endtab %}

{% tab title="Visual Studio Code" %}
Add the server to the `.vscode/mcp.json` file in your workspace.
To add it for all workspaces, run the `MCP: Open User Configuration` command and add it there.

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "gridgain-password",
      "description": "GridGain password for the MCP server",
      "password": true
    }
  ],
  "servers": {
    "gridgain": {
      "type": "stdio",
      "command": "java",
      "args": ["-jar", "/opt/gridgain-mcp/gridgain-mcp-<version>.jar"],
      "env": {
        "GRIDGAIN_HOST": "db.example.com",
        "GRIDGAIN_USERNAME": "mcp_reader",
        "GRIDGAIN_PASSWORD": "${input:gridgain-password}"
      }
    }
  }
}
```

<details>

<summary>Container image example</summary>

```json
{
  "inputs": [
    {
      "type": "promptString",
      "id": "gridgain-password",
      "description": "GridGain password for the MCP server",
      "password": true
    }
  ],
  "servers": {
    "gridgain": {
      "type": "stdio",
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "GRIDGAIN_HOST",
        "-e", "GRIDGAIN_USERNAME",
        "-e", "GRIDGAIN_PASSWORD",
        "gridgain/mcp:<version>"
      ],
      "env": {
        "GRIDGAIN_HOST": "db.example.com",
        "GRIDGAIN_USERNAME": "mcp_reader",
        "GRIDGAIN_PASSWORD": "${input:gridgain-password}"
      }
    }
  }
}
```

</details>

The `inputs` block makes Visual Studio Code ask for the password the first time it starts the server.
Visual Studio Code hides what you type and keeps the password in its secure storage, not in the file.
To enter a different password, run the `MCP: Reset Cached Inputs` command.
{% endtab %}
{% endtabs %}

## Verifying the Connection

After you add the server, the host lists the server's tools.
Ask the assistant to check the database connection.
The assistant calls the `check_database_connection` tool and reports whether the cluster answered.
If the call fails, see [Troubleshooting](operations.md#troubleshooting).

## Allowing the Tools

Hosts ask you for permission before the assistant uses a tool, unless you allow it in advance.
All GridGain MCP Server tools are marked as read-only, so a host may offer to run them without asking.
Before you allow this, read [Security](security.md), especially the part about user-defined functions.
