---
description: >-
  Install MariaDB AI Plugins in Claude Code, Codex, OpenCode, Pi, or Hermes Agent.
---

# Installation

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

If a harness has its own plugin system, you install MariaDB AI Plugins through it. The installation consists of two steps:

1. Install the plugin into your harness, using the page for your harness below.
2. Configure what the MCP server may access. This step is the same for every harness; see [Configuring the MCP Server](../configuring-the-mcp-server/README.md).

The skills are available after the first step. The MCP server rejects all requests until you complete the second step.

{% hint style="info" %}
When the plugin starts for the first time, it downloads and extracts MariaDB Shell, unless a suitable version is already installed. Depending on your network connection, this can take a minute. Later starts use the installed copy.
{% endhint %}

## Prerequisites

* A supported harness: Claude Code, Codex, OpenCode, Pi, or Hermes Agent.
* Linux, macOS, or Windows. The optional migration tooling is available on Linux and macOS only.
* Network access on first start, unless MariaDB Shell 26.10.3 or later is already installed.

You don't need a MariaDB Server installation. If you don't have a server, the MCP server can deploy a local [sandbox instance](../features/sandbox-instances.md).

## Choose Your Harness

{% content-ref url="claude-code.md" %}
[claude-code.md](claude-code.md)
{% endcontent-ref %}

{% content-ref url="codex.md" %}
[codex.md](codex.md)
{% endcontent-ref %}

{% content-ref url="opencode.md" %}
[opencode.md](opencode.md)
{% endcontent-ref %}

{% content-ref url="pi.md" %}
[pi.md](pi.md)
{% endcontent-ref %}

{% content-ref url="hermes.md" %}
[hermes.md](hermes.md)
{% endcontent-ref %}

## Verify the Skills Are Loaded

To check that the skills are loaded, ask the agent a question that requires MariaDB-specific knowledge, for example:

```text
Write a CREATE TABLE for a product catalog, MariaDB style.
```

If the answer uses the native `UUID` data type with `UUID_v7()` rather than `CHAR(36)`, the skills are loaded.

<sub>_This page is licensed: GPLv2_</sub>
