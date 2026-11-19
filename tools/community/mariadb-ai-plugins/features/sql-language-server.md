---
description: >-
  Check SQL files against the MariaDB parser while the agent edits them, with
  the MariaDB SQL language server that ships with MariaDB Shell.
---

# SQL Language Server

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

The MariaDB SQL language server, `mariadb-lsp`, reads `.sql` files with the parser of the MariaDB server. When the coding agent writes or edits a SQL file, the language server reports syntax errors back to the agent, so the agent can fix them before it runs the script. In harnesses that let the agent query a language server, the agent can also list the objects a script defines and look up where a table or column is created.

## Requirements

* MariaDB Shell 26.10.3 or later, installed from its release packages. The `mariadb-lsp` binary is installed next to `mariadb-shell`. The native `.deb` and `.rpm` packages of MariaDB Shell don't include it yet.
* The `dev` or `sql` plugin, in a harness that supports language servers.

## Harness Support

| Harness | Registration | What the agent gets |
| --- | --- | --- |
| Claude Code | Automatic, from the plugin's `.lsp.json`. | Diagnostics after each edit of a `.sql` file. With `ENABLE_LSP_TOOL=1` in the environment, also the `LSP` tool: document symbols, hover, definitions, and references. |
| OpenCode | The `lsp` block of the plugin's `opencode.json`, which you merge into your configuration. See [OpenCode](../installation/opencode.md#register-the-language-server). | Diagnostics after each edit of a `.sql` file. |
| Hermes Agent | An entry under `lsp.servers` that you add to `config.yaml`. See [Hermes Agent](../installation/hermes.md#register-the-language-server). | Diagnostics in the result of each `write_file` or `patch` of a `.sql` file, in git repositories that Hermes trusts. |
| Codex, Pi | Not supported. Neither harness runs language servers. | The same checks through the `sql.*` tools of the MCP server. See [Without a Language Server](#without-a-language-server). |

## What the Language Server Checks

The diagnostics come from the same grammar as the MariaDB server, so they cover MariaDB-specific syntax that a generic SQL checker rejects or misses. The language server follows `SET sql_mode` and `DELIMITER` statements through the file, and expands the `SOURCE` directives of MariaDB Schema Management scripts. A syntax error is reported with the tokens the parser expected at that position.

## Without a Language Server

The MCP server offers the core functions of the language server as tools, so an agent can use them in every harness, including Codex and Pi. [`sql.check`](../mcp-tool-reference/sql-tools.md#sql.check) reports syntax errors, [`sql.outline`](../mcp-tool-reference/sql-tools.md#sql.outline) lists the schema objects that a script defines, and [`sql.format`](../mcp-tool-reference/sql-tools.md#sql.format) lays SQL out. They run the same `mariadb-lsp` binary on SQL that the agent passes inline or names by file, and need no database connection. In a harness with language server support, the agent gets diagnostics automatically and can still call the tools, for example to check a script before it runs it with `db.execute_sql_script`.

## How the Language Server Starts

The plugin starts the language server with a launcher script, `mariadb-lsp-launcher.sh`, or `mariadb-lsp-launcher.cmd` on Windows. The launcher never installs anything. It finds the MariaDB Shell that the MCP server's launcher uses and starts the `mariadb-lsp` installed with it.

On the first start, when MariaDB Shell isn't installed yet, the MCP server's launcher downloads it. The language server's launcher waits for that installation, for up to 180 seconds by default, so the package is downloaded only once. The variables that control the launcher are listed in the [Configuration Reference](../configuration-reference.md#lsp-launcher-environment-variables).

<sub>_This page is licensed: GPLv2_</sub>
