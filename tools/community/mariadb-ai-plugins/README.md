---
description: >-
  MariaDB AI Plugins add MariaDB skills and the mariadb-shell MCP server to the
  Claude Code, Codex, OpenCode, Pi, Hermes Agent, and Cursor coding agents.
icon: robot
---

# MariaDB AI Plugins

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

## MariaDB AI Plugins

MariaDB AI Plugins are plugins for AI coding agents that help the agent work with MariaDB. They include skills, which are reference documents on MariaDB SQL, tools, and connectors, and the `mariadb-shell` MCP server, which connects the agent to your MariaDB servers.

{% hint style="info" %}
The skills are available as soon as the plugin is installed and don't require a database. Before the agent can use the MCP server, you must configure it as described in [Configuring the MCP Server](configuring-the-mcp-server/README.md).
{% endhint %}

{% columns %}
{% column %}
{% content-ref url="about-mariadb-ai-plugins.md" %}
[about-mariadb-ai-plugins.md](about-mariadb-ai-plugins.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of the plugins, the coding agents they support, and the MariaDB and MariaDB Shell versions they work with.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="installation/" %}
[installation](installation/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to install a plugin in Claude Code, Codex, OpenCode, Pi, Hermes Agent, or Cursor.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-the-mcp-server/" %}
[configuring-the-mcp-server](configuring-the-mcp-server/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to set up the database connections and directories that the MCP server is allowed to use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="basic-usage.md" %}
[basic-usage.md](basic-usage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Example requests that use the skills, a configured database, or a sandbox instance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="plugin-variants.md" %}
[plugin-variants.md](plugin-variants.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The differences between the `dev`, `sql`, and `contributor` plugins.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="features/" %}
[features](features/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Detailed descriptions of SQL scripts, sandbox instances, schema management, REST endpoints, and the migration from MySQL.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="architecture.md" %}
[architecture.md](architecture.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the skills, the MCP server, and MariaDB Shell work together, and how the launcher installs MariaDB Shell.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="security-model.md" %}
[security-model.md](security-model.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How the MCP server limits the databases and directories that the agent can access.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="skills-reference/" %}
[skills-reference](skills-reference/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A list of all skills included in the plugins, grouped by topic.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mcp-tool-reference/" %}
[mcp-tool-reference](mcp-tool-reference/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Descriptions and arguments of all tools that the MCP server provides.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration-reference.md" %}
[configuration-reference.md](configuration-reference.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Environment variables, file locations, and configuration files.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="troubleshooting.md" %}
[troubleshooting.md](troubleshooting.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Solutions for common error messages and problems.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="release-notes.md" %}
[release-notes.md](release-notes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How releases are numbered, and the changes in the latest release.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="license.md" %}
[license.md](license.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
License terms for the plugin code and the bundled skills.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bug-reports.md" %}
[bug-reports.md](bug-reports.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to report bugs and security vulnerabilities.
{% endcolumn %}
{% endcolumns %}

<sub>_This page is licensed: GPLv2_</sub>
