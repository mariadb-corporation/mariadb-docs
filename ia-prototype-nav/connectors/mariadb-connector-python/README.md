---
description: >-
  Complete Connector/Python guide: DB API 2.0 (PEP-249) implementation,
  MariaDB/MySQL connectivity, C+Python architecture, and Connector/C transport.
icon: link
---

# Connector/Python

## MariaDB Connector/Python

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 ([PEP-249](https://peps.python.org/pep-0249/)).

{% hint style="info" %}
**As of 2.0.0rc2, version 2.0 is a Release Candidate (RC); version 1.1 is the latest stable (GA) release.** Because 2.0 is not yet GA, install it with the `--pre` flag (for example `pip install --pre mariadb`); a plain `pip install mariadb` installs the latest stable release (1.1). See the [Installation]({connectors}/mariadb-connector-python/install) page for details. Do not use non-stable (non-GA) releases in production.
{% endhint %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/mariadb-connector-python-guide" %}
[mariadb-connector-python-guide.md]({connectors}/mariadb-connector-python/mariadb-connector-python-guide)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of MariaDB Connector/Python: a PEP-249-compliant DB API 2.0 driver supporting sync and async operations, available as pure Python, a C extension, or pre-compiled binary wheels.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/install" %}
[install.md]({connectors}/mariadb-connector-python/install)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install MariaDB Connector/Python via pip with pure Python, C extension, or binary wheel options; connection pooling requires the separate `mariadb[pool]` extra.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/usage" %}
[usage.md]({connectors}/mariadb-connector-python/usage)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Basic usage of MariaDB Connector/Python covers connecting, parameterized queries with `execute` and `executemany`, and NULL and default value handling with indicators.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/async-usage" %}
[async-usage.md]({connectors}/mariadb-connector-python/async-usage)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Async/await support in MariaDB Connector/Python 2.0 enables non-blocking database operations via `asyncConnect`, `AsyncCursor`, and `create_async_pool` for asyncio-based Python applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/pooling" %}
[pooling.md]({connectors}/mariadb-connector-python/pooling)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python 2.0 connection pooling supports sync and async pools via `create_pool` and `create_async_pool`, with configurable size, health checks, and context managers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/migration-from-1.1-to-2.0" %}
[migration-from-1.1-to-2.0.md]({connectors}/mariadb-connector-python/migration-from-1.1-to-2.0)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Migration from MariaDB Connector/Python 1.1 to 2.0 covers renamed parameters, removed auto-reconnect, updated pooling, URI connections, async/await support, and a migration checklist.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/application-development" %}
[application-development.md]({connectors}/mariadb-connector-python/application-development)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Application development with MariaDB Connector/Python.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/api" %}
[api.md]({connectors}/mariadb-connector-python/api)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python API reference covers the module, connection class, cursor class, async/await support, connection pooling, and constants used in Python database applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/license" %}
[license.md]({connectors}/mariadb-connector-python/license)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python is licensed under the GNU LGPL v2.1; the accompanying documentation is covered by the Creative Commons Attribution 3.0 license.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/bugs" %}
[bugs.md]({connectors}/mariadb-connector-python/bugs)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python bug reports are filed in the Jira CONPY project. Effective reports include version details, a short reproducing script, and table definitions where relevant.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/setup-for-examples" %}
[setup-for-examples.md]({connectors}/mariadb-connector-python/setup-for-examples)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set up the test database, contacts and accounts tables, and a user account required by the MariaDB Connector/Python code examples in this documentation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/transactions-with-mariadb-connector-python" %}
[transactions-with-mariadb-connector-python.md]({connectors}/mariadb-connector-python/transactions-with-mariadb-connector-python)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python transactions default to manual commit; the Connection class provides `commit` and `rollback`, with async transaction support via `asyncConnect` in version 2.0.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{connectors}/mariadb-connector-python/faq" %}
[faq.md]({connectors}/mariadb-connector-python/faq)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB Connector/Python FAQ addresses common installation issues, migration from 1.1 to 2.0, the binary vs text protocol distinction, async setup, and transaction commit requirements.
{% endcolumn %}
{% endcolumns %}

{% @marketo/form formId="4316" %}
