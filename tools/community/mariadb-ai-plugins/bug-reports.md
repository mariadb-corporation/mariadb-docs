---
description: >-
  Report MariaDB AI Plugins bugs and request features on GitHub, and report
  security vulnerabilities privately.
---

# Bug Reports

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

## Report a Bug

Report bugs and request features in the [MariaDB AI Plugins issue tracker on GitHub](https://github.com/mariadb/ai-plugins/issues). A good report includes:

* The harness and its version, for example Claude Code or Codex.
* The plugin variant and version.
* The MariaDB Shell version, which this command prints:

  ```bash
  mariadb-shell --version
  ```
* Your operating system.
* The request you gave the agent, and the tool call or error message that went wrong.

Report errors in skills that come from the MariaDB documentation in the [MariaDB documentation repository](https://github.com/mariadb-corporation/mariadb-docs).

## Report a Security Vulnerability

{% hint style="danger" %}
Don't report security vulnerabilities in public issues.
{% endhint %}

Follow the guidelines on the [Security Vulnerabilities (CVEs)](https://mariadb.com/docs/server/security/cve) page. You can report sensitive issues on [HackerOne](https://hackerone.com/mariadb), or send them to the MariaDB security team at `security [AT] mariadb (dot) org`.

<sub>_This page is licensed: GPLv2_</sub>
