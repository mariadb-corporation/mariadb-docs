---
description: >-
  Where to find the changes in each MariaDB AI Plugins release, and how plugin
  versions relate to MariaDB Shell versions.
---

# Release Notes

<!--
  SYNCED: this page is maintained in mariadb-corporation/ai-plugins, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-ai-plugins/).
  Make every change in mariadb-corporation/ai-plugins. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

## Versioning

MariaDB AI Plugins releases are numbered after the MariaDB Shell release they require: plugin version 26.9.5 requires MariaDB Shell 26.9.5 or later. All plugins and harnesses share one version number.

## Changelogs

Each plugin keeps a changelog in its directory, for example `claude/dev-plugin/CHANGELOG.md`. Releases are published on the [GitHub releases page](https://github.com/mariadb/ai-plugins/releases).

## Latest Release

### 26.9.5

* Adds three Laravel skills to the `dev` plugin: `mariadb-laravel-connector`, `mariadb-laravel-vector`, and `mariadb-laravel-ai-sdk`, for 85 skills in total.
* Raises the minimum MariaDB Shell version, `MARIADB_SHELL_VERSION`, to 26.9.5. An installed MariaDB Shell at or above that version is used as it is.
* Updates the vendored skills from the MariaDB documentation, correcting the sample output in `mariadb-explain`.

<sub>_This page is licensed: GPLv2_</sub>
