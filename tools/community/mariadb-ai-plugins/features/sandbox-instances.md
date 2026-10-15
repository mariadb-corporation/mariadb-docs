---
description: >-
  Deploy local MariaDB Server instances for development and testing with the
  mariadb-shell MCP server.
---

# Sandbox Instances

The MCP server can deploy MariaDB Server instances on your local machine for development and testing. These sandbox instances don't require Docker or another container runtime, and you don't need administrator rights to create them. A sandbox is useful when no database server is available, or when you want to test changes before you apply them to a production database.

## Deploy a Sandbox

To deploy a sandbox, ask the agent, for example:

```text
Deploy a MariaDB sandbox on port 3310.
```

The agent calls `sandbox.deploy`. The MCP server registers a connection to the new instance automatically, so you don't need to run `mcp setup` for it.

## Server Versions

You don't need to install MariaDB Server. To find a server binary, `sandbox.deploy` checks the following locations in order:

1. A `mariadbd` on the `PATH`.
2. A version the sandbox has already downloaded.
3. The published index of MariaDB Server releases, from which it downloads a package, verifies its SHA-256 checksum, and unpacks it.

You can request a specific version with a full or partial version number, such as `11.8.9`, `11.8`, or `11`. For a partial version number, the sandbox uses the latest matching release. To list the versions available for your platform, ask:

```text
Which MariaDB server versions can you deploy?
```

The agent calls `sandbox.list_available_versions`.

## Sandbox Lifecycle

| Action | Tool | Notes |
| --- | --- | --- |
| Deploy | `sandbox.deploy` | Creates and starts an instance, and registers its connection. |
| Stop | `sandbox.stop` | Graceful shutdown. |
| Start | `sandbox.start` | Restarts an existing instance with its data intact. |
| Stop forcefully | `sandbox.kill` | The fallback when `sandbox.stop` doesn't work. |
| Delete | `sandbox.delete` | Removes the instance. Refuses a running instance. |

{% hint style="warning" %}
If a sandbox uses a downloaded server, the server binary isn't on the `PATH`. In this case, `sandbox.start` needs the `mariadbd_path` that the deployment reported, and you must use `sandbox.kill` to shut the instance down, because `sandbox.stop` can't find the binary. The message returned by `sandbox.deploy` includes this information.
{% endhint %}

See [sandbox Tools](../mcp-tool-reference/sandbox-tools.md) for every argument.

## File Locations

| What | Linux and macOS | Windows |
| --- | --- | --- |
| Instances | `~/.mariadb-shell/sandboxes/<port>/` | `%USERPROFILE%\MariaDB\mariadb-shell\sandboxes\<port>\` |
| Downloaded servers | `~/.local/share/mariadb-sandbox-server/` | `%LOCALAPPDATA%\Programs\mariadb-sandbox-server\` |

## Security Considerations

{% hint style="danger" %}
A sandbox creates a `root@'%'` account and listens on all network interfaces. Use sandboxes for development only, and don't leave them running on an untrusted network.
{% endhint %}

* A sandbox is deployed without TLS, so command-line clients may need `--skip-ssl`.
* The connection that a sandbox registers is the only connection that the MCP server adds without your configuration. It points to the local sandbox instance only.
