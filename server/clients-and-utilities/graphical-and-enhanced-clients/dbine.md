---
description: >-
  DBine is a free, open-source desktop database manager for MariaDB with a SQL
  editor, schema and data compare, ER diagrams, query plans, and a profiler.
---

# DBine

{% hint style="info" %}
DBine is third-party software, not developed or maintained by MariaDB and not included with MariaDB Server. MariaDB doesn't test, validate, or support it. Refer to its own documentation and license terms.
{% endhint %}

[DBine](https://dbine.com) is a free, open-source (MIT) desktop database manager by AddLayer, available for Windows, macOS, and Linux. It connects to local, self-hosted, and managed MariaDB servers, directly or through an SSH tunnel, and works with 130+ databases and cloud services in the same window.

DBine provides the following for MariaDB:

* A SQL editor with autocomplete, script execution, and query cancellation.
* Table data editing, where each change is generated as SQL that you review before running it.
* A table designer, ER diagrams, and object scripts.
* Schema compare and data compare between databases.
* Query plans from `EXPLAIN FORMAT=JSON` and `ANALYZE FORMAT=JSON`.
* A process list and a profiler that samples `information_schema.PROCESSLIST`.
* Notebooks that query several databases and join the results with DuckDB.
* An AI assistant that proposes queries and runs nothing until you approve it, with support for local models.

Passwords can come from a secret manager, and connections can be marked read-only.

* [DBine on GitHub](https://github.com/addlayer-io/dbine)
* [Download DBine](https://github.com/addlayer-io/dbine/releases)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
