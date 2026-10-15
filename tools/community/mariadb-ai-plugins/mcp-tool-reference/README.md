---
description: >-
  Reference for the db, msm, sandbox, migrator, and rest tools of the
  mariadb-shell MCP server.
---

# MCP Tool Reference

The `mariadb-shell` MCP server provides 28 tools in three groups. A fourth, optional group is available when the migration tooling is installed, and a fifth group, for the MariaDB REST Daemon, in MariaDB Shell releases later than 26.10.1.

| Group | Tools | What they do |
| --- | --- | --- |
| [`db.*`](db-tools.md) | 8 | List connections and schemas, describe objects, and run SQL. |
| [`msm.*`](msm-tools.md) | 12 | Versioned schema projects, releases, and deployments with MariaDB Schema Management. |
| [`sandbox.*`](sandbox-tools.md) | 8 | List deployable server versions; deploy, start, stop, and delete local instances. |
| [`migrator.*`](migrator-tools.md) | 4 | MySQL-to-MariaDB migration. Optional, and not counted in the 28. |
| [`rest.*`](rest-tools.md) | 5 | Set up, start, stop, and delete MariaDB REST Daemons. Requires a MariaDB Shell release later than 26.10.1, and not counted in the 28. |

A server in multi-tenant mode (the `--multiTenant` option of `mcp setup`, available in MariaDB Shell 26.10.0 and later) serves only the `db.*` and `msm.*` groups. The `sandbox.*`, `migrator.*`, and `rest.*` tools run local server instances, daemons, and long-running jobs on the machine that hosts the MCP server, and aren't offered to tenants. The server that the plugins' launcher scripts start is single-tenant and serves every group.

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

{% content-ref url="migrator-tools.md" %}
[migrator-tools.md](migrator-tools.md)
{% endcontent-ref %}

{% content-ref url="rest-tools.md" %}
[rest-tools.md](rest-tools.md)
{% endcontent-ref %}
