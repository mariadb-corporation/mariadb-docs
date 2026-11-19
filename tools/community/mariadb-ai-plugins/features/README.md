---
description: >-
  Detailed descriptions of the main features of MariaDB AI Plugins, such as
  SQL scripts, sandbox instances, schema management, REST endpoints, and the
  migration from MySQL.
---

# Features

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

This section describes the main features of MariaDB AI Plugins in detail. For each feature, you'll find its requirements, the skills and MCP tools the agent uses, and a description of how the feature works and where its limits are.

For a quick overview of what you can ask an agent, see [Basic Usage](../basic-usage.md). For the arguments of each tool, see the [MCP Tool Reference](../mcp-tool-reference/).

## Feature Overview

| Feature | What it does | Plugins | Requires |
| --- | --- | --- | --- |
| [SQL Script Creation and Execution](sql-script-creation-and-execution.md) | Writes schema create scripts, runs them on a server, and verifies the result. | `dev`, `sql` | The MCP server, to run scripts |
| [Sandbox Instances](sandbox-instances.md) | Deploys local MariaDB Server instances for development and testing. | `dev`, `sql` | The MCP server |
| [Versioned Schemas with Schema Management](versioned-schemas-with-schema-management.md) | Keeps a schema in a versioned project, and creates or upgrades it on any server. | `dev` | The MCP server |
| REST Endpoints with MariaDB REST Service | Defines REST endpoints for schema objects with SQL statements. | `dev` | The MCP server and a server connection |
| [Migrating from MySQL](migrating-from-mysql.md) | Assesses MySQL compatibility and migrates a MySQL database to MariaDB. | `dev`; compatibility guidance also in `sql` | The migration tooling, on Linux and macOS |
| [SQL Language Server](sql-language-server.md) | Checks SQL files against the MariaDB parser while the agent edits them. | `dev`, `sql` | MariaDB Shell 26.10.3 or later, and Claude Code, OpenCode, or Hermes Agent |

{% content-ref url="sql-script-creation-and-execution.md" %}
[sql-script-creation-and-execution.md](sql-script-creation-and-execution.md)
{% endcontent-ref %}

{% content-ref url="sandbox-instances.md" %}
[sandbox-instances.md](sandbox-instances.md)
{% endcontent-ref %}

{% content-ref url="versioned-schemas-with-schema-management.md" %}
[versioned-schemas-with-schema-management.md](versioned-schemas-with-schema-management.md)
{% endcontent-ref %}

{% content-ref url="migrating-from-mysql.md" %}
[migrating-from-mysql.md](migrating-from-mysql.md)
{% endcontent-ref %}

{% content-ref url="sql-language-server.md" %}
[sql-language-server.md](sql-language-server.md)
{% endcontent-ref %}

{% hint style="info" %}
For step-by-step tutorials with example prompts, see the [MariaDB AI Plugins DevHub](https://ai-plugins.mariadb.org/tutorials/).
{% endhint %}

<sub>_This page is licensed: GPLv2_</sub>
