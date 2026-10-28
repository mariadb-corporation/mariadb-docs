---
description: >-
  Reference for the db, msm, sandbox, util, and migrator tools of the
  mariadb-shell MCP server.
---

# MCP Tool Reference

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

The `mariadb-shell` MCP server provides 43 tools in five groups. A sixth, optional group is available when the migration tooling is installed.

| Group | Tools | What they do |
| --- | --- | --- |
| [`db.*`](db-tools.md) | 8 | List connections and schemas, describe objects, and run SQL. |
| [`msm.*`](msm-tools.md) | 12 | Versioned schema projects, releases, and deployments with MariaDB Schema Management. |
| [`sandbox.*`](sandbox-tools.md) | 8 | List deployable server versions; deploy, start, stop, and delete local instances. |
| [`util.*`](util-tools.md) | 12 | Dump, load, export, import, and copy data between servers, as background tasks. Requires MariaDB Shell 26.10.2 or later. |
| [`sql.*`](sql-tools.md) | 3 | Check, outline, and format SQL text with the MariaDB grammar, without a database. Requires MariaDB Shell 26.10.3 or later and `mariadb-lsp`. |
| [`migrator.*`](migrator-tools.md) | 4 | MySQL-to-MariaDB migration. Optional, and not counted in the 43. |

A server in multi-tenant mode (the `--multiTenant` option of `mcp setup`, available in MariaDB Shell 26.10.0 and later) serves only the `db.*` group. In MariaDB Shell 26.10.0 and 26.10.1, it also serves the `msm.*` group. The other groups run local server instances and long-running jobs, or read and write files, on the machine that hosts the MCP server, and aren't offered to tenants. The server that the plugins' launcher scripts start is single-tenant and serves every group.

## Conventions

* Arguments are named as the tools take them.
* `connection_id` always comes from a prior `db.connect` call.
* Any argument that takes a file path is limited to the allowed-paths list. See [Security Model](../security-model.md#paths).

{% content-ref url="db-tools.md" %}
[db-tools.md](db-tools.md)
{% endcontent-ref %}

{% content-ref url="msm-tools.md" %}
[msm-tools.md](msm-tools.md)
{% endcontent-ref %}

{% content-ref url="sandbox-tools.md" %}
[sandbox-tools.md](sandbox-tools.md)
{% endcontent-ref %}

{% content-ref url="util-tools.md" %}
[util-tools.md](util-tools.md)
{% endcontent-ref %}

{% content-ref url="sql-tools.md" %}
[sql-tools.md](sql-tools.md)
{% endcontent-ref %}

{% content-ref url="migrator-tools.md" %}
[migrator-tools.md](migrator-tools.md)
{% endcontent-ref %}

<sub>_This page is licensed: GPLv2_</sub>
