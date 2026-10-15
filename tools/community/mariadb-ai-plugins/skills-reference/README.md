---
description: >-
  Reference for all skills included in MariaDB AI Plugins, grouped by topic.
---

# Skills Reference

A skill is a Markdown document with MariaDB-specific information that the agent reads when it's relevant to a request. Skills don't require a database connection or any configuration.

## How the Agent Uses Skills

Each skill has a name and a short description. The harness provides the descriptions to the agent, and the agent reads the full skill when a request matches its description. For example, a request for a `CREATE TABLE` statement causes the agent to read `mariadb-create-table`, and a question about vector search causes it to read `mariadb-vector`. You don't need to select skills yourself.

## Skill Layers

| Layer | Skills | Plugins | Source |
| --- | --- | --- | --- |
| [SQL Statements](sql-statement-skills.md) | 31 | `dev`, `sql` | MariaDB documentation |
| [Built-in Functions](built-in-function-skills.md) | 10 | `dev`, `sql` | MariaDB documentation |
| [Command-Line Tools](command-line-tool-skills.md) | 4 | `dev` | MariaDB documentation |
| [Connectors](connector-skills.md) | 14 | `dev` | MariaDB documentation |
| [Topical](topical-skills.md) | 5 | `dev`, `sql` | MariaDB documentation |
| [Additional](additional-skills.md) | 21 | `dev`; one also in `sql` | MariaDB AI Plugins repository |
| [Contributor](contributor-skills.md) | 3 | `contributor` | MariaDB Shell repository |

The skills are verified against MariaDB 11.8 LTS.

## Skill Versions

The skills are copied into each plugin when a release is built, so their content doesn't change between releases. Each plugin records the source repository, commit, and synchronization date of its skills in `skills/skills-source.json`.
