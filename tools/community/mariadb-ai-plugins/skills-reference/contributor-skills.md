---
description: >-
  Reference for the skills in the MariaDB AI Plugins contributor plugin, for working on MariaDB tooling itself.
---

# Contributor Skills

These skills make up the `contributor` plugin and come from the MariaDB Shell repository. They support the development of MariaDB Shell and its plugins rather than work with MariaDB databases. The `contributor` plugin doesn't include the MCP server.

| Skill | What it covers |
| --- | --- |
| `create-shell-plugin` | Scaffold a MariaDB Shell plugin following project best practices. |
| `review-shell-change` | Review a diff, branch, or PR in the MariaDB Shell repository. Runs the standard code review, then applies this repo's policy — what the other CI jobs already cover (so the review stays silent about it), the C/C++ defect classes worth hunting here, and the MariaDB-port conventions needed to judge a guard, a vendor difference, or a gated test correctly. |
| `split-scripted-test` | Split a long scripted test (unittest/scripts/auto/*/scripts/*_norecord.py) into N parallel chunk groups for run_unit_tests.py, or rebalance the groups of a test that is already split, so every group takes about the same time. |
