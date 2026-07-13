---
description: >-
  Complete Connector/Python guide: DB API 2.0 (PEP-249) implementation,
  MariaDB/MySQL connectivity, C+Python architecture, and Connector/C transport.
icon: link
---

# Connector/Python

## MariaDB Connector/Python

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 ([PEP-249](https://peps.python.org/pep-249)).

{% hint style="info" %}
**Version 2.0 is currently a Release Candidate (RC); version 1.1 is the latest stable (GA) release.** Because 2.0 is not yet GA, install it with the `--pre` flag (for example `pip install --pre mariadb`); a plain `pip install mariadb` installs the latest stable release (1.1). See the [Installation](install.md) page for details. Do not use non-stable (non-GA) releases in production.
{% endhint %}

{% columns %}
{% column %}
{% content-ref url="mariadb-connector-python-guide.md" %}
[mariadb-connector-python-guide.md](mariadb-connector-python-guide.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of MariaDB Connector/Python: a PEP-249-compliant DB API 2.0 driver supporting sync and async operations, available as pure Python, a C extension, or pre-compiled binary wheels.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="install.md" %}
[install.md](install.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MariaDB Connector/Python via pip with pure Python, C extension, or binary wheel options; connection pooling requires the separate `mariadb[pool]` extra.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="usage.md" %}
[usage.md](usage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Basic usage of MariaDB Connector/Python covers connecting, parameterized queries with `execute` and `executemany`, and NULL and default value handling with indicators.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="async-usage.md" %}
[async-usage.md](async-usage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Async/await support in MariaDB Connector/Python 2.0 enables non-blocking database operations via `asyncConnect`, `AsyncCursor`, and `create_async_pool` for asyncio-based Python applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pooling.md" %}
[pooling.md](pooling.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python 2.0 connection pooling supports sync and async pools via `create_pool` and `create_async_pool`, with configurable size, health checks, and context managers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="migration-from-1.1-to-2.0.md" %}
[migration-from-1.1-to-2.0.md](migration-from-1.1-to-2.0.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Migration from MariaDB Connector/Python 1.1 to 2.0 covers renamed parameters, removed auto-reconnect, updated pooling, URI connections, async/await support, and a migration checklist.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="application-development.md" %}
[application-development.md](application-development.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Application development with MariaDB Connector/Python.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="api.md" %}
[api.md](api.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python API reference covers the module, connection class, cursor class, async/await support, connection pooling, and constants used in Python database applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="license.md" %}
[license.md](license.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python is licensed under the GNU LGPL v2.1; the accompanying documentation is covered by the Creative Commons Attribution 3.0 license.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bugs.md" %}
[bugs.md](bugs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python bug reports are filed in the Jira CONPY project. Effective reports include version details, a short reproducing script, and table definitions where relevant.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setup-for-examples.md" %}
[setup-for-examples.md](setup-for-examples.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up the test database, contacts and accounts tables, and a user account required by the MariaDB Connector/Python code examples in this documentation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-with-mariadb-connector-python.md" %}
[transactions-with-mariadb-connector-python.md](transactions-with-mariadb-connector-python.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python transactions default to manual commit; the Connection class provides `commit` and `rollback`, with async transaction support via `asyncConnect` in version 2.0.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="faq.md" %}
[faq.md](faq.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python FAQ addresses common installation issues, migration from 1.1 to 2.0, the binary vs text protocol distinction, async setup, and transaction commit requirements.
{% endcolumn %}
{% endcolumns %}

{% @marketo/form formId="4316" %}
