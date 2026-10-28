---
description: >-
  How the mariadb-shell MCP server limits the databases and directories that
  an AI agent can access.
---

# Security Model

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

The MCP server only accesses databases and directories that you have explicitly allowed. You define both in two allow-lists with `mariadb-shell -- mcp setup`. Within a database, the privileges of the MariaDB account determine what the agent can do.

## Connections

The agent can only connect to the servers in the list of configured connections. `db.connect` checks each connection request against this list, and the agent calls `db.list_connections` to find out which connections exist.

When the MCP server compares a URI with the configured connections, it treats equivalent forms as equal, such as a `mariadb://` scheme, a different capitalization of the host name, an explicit default port, or a password in the URI. It does not accept a `mysql://` scheme, and it rejects a URI that requests more than the configured connection, for example a default schema or an additional option:

```text
root@127.0.0.1:3310/notes_app         → refused (a default schema)
root@127.0.0.1:3310?ssl-mode=REQUIRED → refused (an option)
```

The MCP server rejects these requests instead of ignoring the additional parts, because a connection without the requested schema or TLS setting could behave differently from what the agent expects.

{% hint style="warning" %}
The list of connections controls which servers the agent can access, and the privileges of the MariaDB account control what the agent can do on these servers. Create a dedicated account for each connection, with only the privileges the agent needs, for example read-only access to a single schema. Account privileges restrict the agent more reliably than instructions in a prompt. See [Database Accounts for the MCP Server](configuring-the-mcp-server/database-accounts-for-the-mcp-server.md).
{% endhint %}

## Paths

All tools that access files are restricted to the directories in the allowed-paths list. This includes `db.execute_sql_script` with a `file_path`, all `msm.*` tools, and `sandbox.deploy` with a `sandbox_dir`. For a path outside these directories, the MCP server asks for an interactive confirmation, which the agent can't give. As a result:

* The `msm.*` tools fail.
* `sandbox.deploy` stops responding.

In both cases, add the directory with `mcp setup`, for example:

```bash
mariadb-shell -- mcp setup --addPaths=/home/dev/projects
```

## Connections Created by Sandboxes

`sandbox.deploy` registers `root@127.0.0.1:<port>` with its password, so that the agent can connect to the new instance. This is the only case in which the MCP server adds a connection without your configuration, and the connection points to the local sandbox instance only.

## Credentials

Passwords are stored in the MariaDB Shell secret store, which uses the secret storage of the operating system. They are kept separately from your other MariaDB Shell connections and are never written to a file that the agent can read. The `migrator.set_config` tool refuses passwords for the same reason.

<sub>_This page is licensed: GPLv2_</sub>
