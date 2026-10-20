---
description: >-
  Connect Claude Code, Cursor, or Visual Studio Code to GridGain MCP Server, from the JAR file or the container image, without putting the password in a settings file.
---

# Connecting an Assistant

An assistant, such as Claude Code, Cursor, or Visual Studio Code, is called an MCP host.
To connect it to GridGain MCP Server, you give the host the command that starts the server.
The host runs the command when it needs the server and talks to it through standard input and output.

You can start the server in two ways:

- From the JAR file of the download package. The command is `java -jar <path to the JAR file>`.
- From the container image. The command is `docker run -i --rm gridgain/mcp:<version>`.

Both ways are described in [Installing MCP Server](installation.md).
The examples below show both ways for each host.
Replace `<version>` with the version of the server and `db.example.com` with the address of your cluster.

## Keeping the Password Safe

Pass the cluster user name and password to the server through its environment, and not as command-line arguments.
Arguments are visible in process lists and in the settings files of the host.

The examples below follow this rule:

- The host reads the password from your environment or asks you for it. It does not save the password in the settings file.
- With the JAR file, the host gives the variables from its `env` block to the server directly.
- With the container image, the `docker run` arguments name the variables, such as `-e GRIDGAIN_PASSWORD`, but do not contain the values. The host gives the values to `docker`, and Docker passes them into the container.

Create the account for the server as described in [Security](security.md#preparing-a-cluster-account).

{% tabs %}
{% tab title="Claude Code" %}
Add the server with the `claude mcp add` command.
Set the password in your shell first. The single quotes keep the shell from replacing the reference, so Claude Code reads the password from your environment each time it starts the server.

To use the JAR file:

```shell
export GRIDGAIN_PASSWORD='...'

claude mcp add --transport stdio \
  --env GRIDGAIN_HOST=db.example.com \
  --env GRIDGAIN_USERNAME=mcp_reader \
  --env 'GRIDGAIN_PASSWORD=${GRIDGAIN_PASSWORD}' \
  gridgain \
  -- java -jar /opt/gridgain-mcp/gridgain-mcp-<version>.jar
```

To use the container image:

```shell
export GRIDGAIN_PASSWORD='...'

claude mcp add --transport stdio \
  --env GRIDGAIN_HOST=db.example.com \
  --env GRIDGAIN_USERNAME=mcp_reader \
  --env 'GRIDGAIN_PASSWORD=${GRIDGAIN_PASSWORD}' \
  gridgain \
  -- docker run -i --rm \
     -e GRIDGAIN_HOST -e GRIDGAIN_USERNAME -e GRIDGAIN_PASSWORD \
     gridgain/mcp:<version>
```

By default, Claude Code stores the server for the current project only, on your machine.
Add `--scope project` to share it with the team through the `.mcp.json` file, or `--scope user` to use it in all projects.

Instead of the command, you can create a `.mcp.json` file in the project root.
Claude Code reads the `${...}` references from the environment of the user who starts it.

To use the JAR file:

```json
{
  "mcpServers": {
    "gridgain": {
      "type": "stdio",
      "command": "java",
      "args": ["-jar", "/opt/gridgain-mcp/gridgain-mcp-<version>.jar"],
      "env": {
        "GRIDGAIN_HOST": "${GRIDGAIN_HOST:-localhost}",
        "GRIDGAIN_USERNAME": "${GRIDGAIN_USERNAME}",
        "GRIDGAIN_PASSWORD": "${GRIDGAIN_PASSWORD}"
      }
    }
  }
}
```

To use the container image:

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
        "GRIDGAIN_HOST": "${GRIDGAIN_HOST:-localhost}",
        "GRIDGAIN_USERNAME": "${GRIDGAIN_USERNAME}",
        "GRIDGAIN_PASSWORD": "${GRIDGAIN_PASSWORD}"
      }
    }
  }
}
```

If a variable is not set and has no default, Claude Code shows a warning in `claude mcp list`.
It then passes the text `${GRIDGAIN_PASSWORD}` to the server as the value.

To check the result, run `claude mcp list`, or type `/mcp` in a Claude Code session.
{% endtab %}

{% tab title="Cursor" %}
Add the server to the `.cursor/mcp.json` file in your project, or to `~/.cursor/mcp.json` to use it in all projects.
Cursor reads the `${env:...}` references from the environment in which Cursor starts.

To use the JAR file:

```json
{
  "mcpServers": {
    "gridgain": {
      "type": "stdio",
      "command": "java",
      "args": ["-jar", "/opt/gridgain-mcp/gridgain-mcp-<version>.jar"],
      "env": {
        "GRIDGAIN_HOST": "${env:GRIDGAIN_HOST}",
        "GRIDGAIN_USERNAME": "${env:GRIDGAIN_USERNAME}",
        "GRIDGAIN_PASSWORD": "${env:GRIDGAIN_PASSWORD}"
      }
    }
  }
}
```

To use the container image:

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
        "GRIDGAIN_HOST": "${env:GRIDGAIN_HOST}",
        "GRIDGAIN_USERNAME": "${env:GRIDGAIN_USERNAME}",
        "GRIDGAIN_PASSWORD": "${env:GRIDGAIN_PASSWORD}"
      }
    }
  }
}
```

Make sure the variables are set before you start Cursor.
{% endtab %}

{% tab title="Visual Studio Code" %}
Add the server to the `.vscode/mcp.json` file in your workspace.
To edit the settings for all workspaces, run the `MCP: Open User Configuration` command.

Visual Studio Code asks for the password the first time it starts the server and hides what you type.
The password is not saved in the file.

To use the JAR file:

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

To use the container image:

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
{% endtab %}
{% endtabs %}

## Notes on the JAR File

- The server requires Java 17 or later. To check the version, run `java -version`. The host runs the `java` command from its own environment, which can differ from the one in your terminal.
- Use the full path to the JAR file, because the host may start the server from a different folder.
- Keep the `libs` folder next to the JAR file, or use the single JAR from the `standalone` folder.

## Verifying the Connection

After you add the server, the host lists the tools of the server.
Ask the assistant to check the database connection.
The assistant calls the `check_database_connection` tool and reports whether the cluster answered.
If the call fails, see [Troubleshooting](operations.md#troubleshooting).

## Allowing the Tools

Hosts ask you for permission before the assistant uses a tool, unless you allow it in advance.
All tools of GridGain MCP Server are marked as read-only, so a host may offer to run them without asking.
Before you allow this, read [Security](security.md), especially the part about user-defined functions.
