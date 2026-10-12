---
description: >-
  The MariaDB AI plugins add MariaDB skills, an MCP server, and the
  mariadb-shell client to coding agents such as Claude Code and Codex.
icon: puzzle-piece
---

# AI Plugins and Skills

{% hint style="info" %}
Placeholder page for the navigation prototype. This content does not exist in the documentation yet.
{% endhint %}

The MariaDB AI plugins give coding agents MariaDB support. A plugin installs three things:

* **Skills.** MariaDB reference material that the agent reads when a task needs it, such as how `ALTER TABLE` behaves in MariaDB or how vector indexes work. Skills need no database connection.
* **An MCP server.** A live connection to a MariaDB server, so that the agent can read the schema, run queries, and analyze a slow query with `EXPLAIN`.
* **`mariadb-shell`.** The MariaDB command-line shell, which runs the MCP server and stores database credentials.

The plugins work with Claude Code, Codex, OpenCode, and Pi. The source is in the [MariaDB/ai-plugins repository](https://github.com/MariaDB/ai-plugins), and the [MariaDB AI DevHub](https://mariadb.github.io/ai-plugins/) has installation steps and tutorials. The skills are also available separately from the [MariaDB/skills repository](https://github.com/mariadb/skills).
