---
description: >-
  Reference for the sql tools of the mariadb-shell MCP server, which check, outline, and format SQL text with the MariaDB grammar, without a database.
---

# sql Tools

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

The `sql.*` tools check, outline, and format SQL text with the grammar of the MariaDB server. They run `mariadb-lsp`, the program of the [SQL language server](../features/sql-language-server.md), on SQL that the agent passes inline or names by file. Nothing is executed, and no connection is needed.

The tools give an agent the core checks of the language server even in a harness that doesn't run language servers, such as Codex and Pi. In a harness that does, the agent can use both.

{% hint style="info" %}
The `sql.*` tools are available in MariaDB Shell 26.10.3 and later.
{% endhint %}

## Overview

| Tool | Description |
| --- | --- |
| `sql.check` | Checks the syntax of SQL and reports each error with its position and the tokens the grammar expected. |
| `sql.outline` | Lists the schema objects that SQL defines. |
| `sql.format` | Lays SQL out in a readable form. |

The MCP server offers the `sql.*` tools only when it finds a `mariadb-lsp` binary, in the following order:

1. The binary, or the folder that contains it, that you set with `mariadb-shell -- mcp setup --lspPath=PATH`. To clear the setting, run `mcp setup --lspPath=""`.
2. The `mariadb-lsp` next to the running `mariadb-shell`, which the MariaDB Shell release packages install.
3. The first `mariadb-lsp` on the `PATH`.
4. `~/.local/bin/mariadb-lsp`.

The binary must answer `--version` with `mariadb-lsp <version>`. A binary that you install takes effect the next time the MCP server starts. A server in multi-tenant mode never offers the `sql.*` tools.

## Input

Each tool takes the SQL in one of two arguments:

| Argument | Description |
| --- | --- |
| `sql` | The SQL, inline: one or more statements. |
| `file_path` | A `.sql` file to read instead. It must be in an allowed path. See [Security Model](../security-model.md#paths). `sql.format` doesn't change the file; it returns the formatted text. |

Pass exactly one of them. The SQL can be at most 10 MB, and a call that takes longer than 60 seconds fails.

`sql.check` and `sql.outline` follow the `SOURCE '<path>'[<start>:<end>];` directives of MariaDB Schema Management scripts. A relative path is taken from the folder of `file_path`, or, for inline SQL, from the `source_dir` argument. Every included file must be in an allowed path. The MCP server expands the directives with the same code and checks as `db.execute_sql_script`, so `mariadb-lsp` reads no file itself. A position in an included part names that file, with the line and column in it.

The following arguments set the state at the start of the SQL. A `SET sql_mode` or `DELIMITER` statement in the SQL is followed from there.

| Argument | Description |
| --- | --- |
| `sql_mode` | Optional. The `sql_mode` at the start, comma-separated. The default is the server's default `sql_mode`. |
| `delimiter` | Optional. The statement delimiter at the start. The default is `;`. |
| `version_id` | Optional. The server release that versioned comments (`/*!100500 ... */`) are judged against, as major × 10000 + minor × 100 + patch. For example, `130100` is 13.1.0. |

Lines and columns in the results are counted from 1, in characters, as an editor shows them.

## sql.check

Checks the syntax of SQL with the MariaDB grammar. The agent uses it on SQL before it runs or saves it.

| Argument | Description |
| --- | --- |
| `sql`, `file_path` | The SQL to check. See [Input](#input). |
| `source_dir` | Optional. For inline SQL, the folder that relative `SOURCE` paths are taken from. It must be in an allowed path. |
| `sql_mode`, `delimiter`, `version_id` | Optional. See [Input](#input). |
| `max_errors` | Optional. The maximum number of errors to list. The default is 100. |

Returns the following fields:

| Field | Description |
| --- | --- |
| `valid` | `true` when the SQL has no errors. |
| `statements` | The number of statements checked, including those of `SOURCE` includes. |
| `errors` | One entry per error, with `start` (its `line` and `column`, and `file` for an error in an included file), `message`, `token` (where the parser failed), and `expected` (the tokens the grammar would have accepted there). |
| `notes` | Remarks that aren't errors, such as statements that couldn't be checked. |

An include that can't be read, or that isn't in an allowed path, fails the call and names the line of its directive.

## sql.outline

Lists the schema objects that SQL defines, without running it. The tool applies the `CREATE`, `ALTER`, `DROP`, `RENAME`, and `USE` statements in order, as a server would, and reports the result: schemas with their tables (columns, indexes, foreign keys, and checks), views, routines, triggers, events, sequences, and MariaDB REST Service objects. The agent uses it to understand a schema script, such as the development script of a Schema Management project.

| Argument | Description |
| --- | --- |
| `sql`, `file_path` | The SQL to outline. See [Input](#input). |
| `source_dir` | Optional. For inline SQL, the folder that relative `SOURCE` paths are taken from. It must be in an allowed path. |
| `sql_mode`, `delimiter`, `version_id` | Optional. See [Input](#input). |

Returns the outline in format 1 of `mariadb-lsp`, with the following fields:

| Field | Description |
| --- | --- |
| `schemas` | The schemas and the objects in them. Each object has a `range` and a `selection_range` (the range of its name), each a `start` and an `end` with a `line` and a `column`. Names are as written, without quotes. |
| `rest` | The MariaDB REST Service objects. |
| `statements` | The number of DDL statements, and how many of them were applied. |
| `notes` | The statements that weren't read, and why. |
| `includes` | For a script with `SOURCE` directives, the file that each directive included and the line of the directive. |

## sql.format

Lays SQL out in a readable form: clauses on lines of their own, keywords in one case, and lines kept within a width. The tool formats `SELECT`, `WITH`, `INSERT ... SELECT`, `UPDATE`, `DELETE`, `CREATE VIEW`, `CREATE TABLE`, and `ALTER TABLE` statements that parse. It leaves any other statement, and any statement that doesn't parse, as it is, and keeps comments. It doesn't follow `SOURCE` directives.

| Argument | Description |
| --- | --- |
| `sql`, `file_path` | The SQL to format. See [Input](#input). |
| `line_width` | Optional. The width that lines are kept within. The default is 80, and 0 means no limit. |
| `keyword_case` | Optional. `upper`, the default, or `lower`. |
| `indent` | Optional. One level of indentation: `tab`, `2`, the default, or `4` spaces. |
| `sql_mode`, `delimiter`, `version_id` | Optional. See [Input](#input). |

Returns `sql`, the formatted SQL.

## Common Failures

| Symptom | Cause |
| --- | --- |
| The MCP server offers no `sql.*` tools. | The server found no `mariadb-lsp`, runs in multi-tenant mode, or is from a MariaDB Shell release earlier than 26.10.3. MariaDB Shell installed from the native `.deb` or `.rpm` packages doesn't include `mariadb-lsp`; set its path with `mcp setup --lspPath`. |
| A tool reports that the SQL is larger than 10 MB. | Split the script, or check its parts separately. |
| A tool refuses `file_path` or a `SOURCE` include. | The file isn't in an allowed path. See [Security Model](../security-model.md#paths). |
| A tool reports that `mariadb-lsp` took longer than 60 seconds. | The SQL is very large. Check smaller parts. |

<sub>_This page is licensed: GPLv2_</sub>
