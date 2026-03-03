---
description: >-
  Complete Connector/Python guide: DB API 2.0 (PEP-249) implementation,
  MariaDB/MySQL connectivity, C+Python architecture, and Connector/C transport.
icon: link
---

# Connector/Python

## MariaDB Connector/Python

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 ([PEP-249](https://peps.python.org/pep-249)).

#### Contents

## Contents:

* [Installation](install.md)
  * [Prerequisites](install.md#prerequisites)
  * [Installation Options](install.md#installation-options)
  * [Installation from Source](install.md#installation-from-source)
  * [Test suite](install.md#test-suite)
* [Basic usage](usage.md)
  * [Connecting](usage.md#connecting)
  * [Passing parameters to SQL statements](usage.md#passing-parameters-to-sql-statements)
* [Async/Await Support](async-usage.md) *(New in 2.0)*
  * [Basic Async Connection](async-usage.md#basic-async-connection)
  * [Async Connection Pools](async-usage.md#async-connection-pools)
  * [FastAPI Integration](async-usage.md#fastapi-integration-example)
* [Connection pooling](pooling.md)
  * [Synchronous Connection Pool](pooling.md#synchronous-connection-pool)
  * [Asynchronous Connection Pool](pooling.md#asynchronous-connection-pool)
* [Migration Guide](migration-from-1.1-to-2.0.md) *(1.1 to 2.0)*
  * [Breaking Changes](migration-from-1.1-to-2.0.md#breaking-changes)
  * [New Features](migration-from-1.1-to-2.0.md#new-features)
  * [Migration Checklist](migration-from-1.1-to-2.0.md#migration-checklist)
* [API Reference](api.md)
  * [The MariaDB Connector/Python module](module.md)
  * [The connection class](connection.md)
  * [The cursor class](cursor.md)
  * [The ConnectionPool class](pool.md)
  * [Constants](constants.md)
* [License](license.md)
  * [MariaDB Connector/Python](license.md#mariadb-connector-python)
  * [MariaDB Connector/Python documentation](license.md#mariadb-connector-python-documentation)
* [Bug reports](bugs.md)
  * [How to report a bug?](bugs.md#how-to-report-a-bug)
* [MariaDB Connector/Python FAQ](faq.md)
  * [Installation](faq.md#installation)
  * [Connecting](faq.md#connecting)
  * [General](faq.md#general)
  * [Transactions](faq.md#transactions)

{% @marketo/form formId="4316" %}
