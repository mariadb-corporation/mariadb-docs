---
description: >-
  MariaDB AI Plugins are licensed under the GNU General Public License, version
  2; the bundled skills keep the licenses of their source repositories.
---

# License

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

## Plugin Code

The plugin code is licensed under the GNU General Public License, version 2 (GPL-2.0), because it depends on the MariaDB Shell MCP plugin. Each plugin ships an identical copy of the license.

## Skills

The bundled skills are vendored from several repositories and keep their original licenses:

| Source | Skills | License |
| --- | --- | --- |
| [MariaDB documentation](https://github.com/mariadb-corporation/mariadb-docs/tree/main/agent-skills) | SQL statement, built-in function, command-line tool, connector, and topical skills | As indicated in the source repository. The topical layer is licensed under the MIT license. |
| [MariaDB Shell](https://github.com/mariadb-corporation/mariadb-shell) | Contributor skills | As indicated in the source repository. |
| MariaDB AI Plugins, `additional-skills/` | Additional skills | GPL-2.0 |

<sub>_This page is licensed: GPLv2_</sub>
