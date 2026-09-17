---
description: >-
  Overview of MariaDB Connector/Python: a PEP-249-compliant DB API 2.0
  driver supporting sync and async operations, available as pure Python, a C
  extension, or pre-compiled binary wheels.
---

# About Connector/Python

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/9p9Gnd3FcRNTnYakGG0J/" %}

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249).

**Version 2.0** offers flexible distribution options:
- **Pure Python** - Works on all platforms, no compiler required
- **C extension** - Maximum performance (2-12× faster on data-heavy workloads)
- **Pre-compiled wheels** - No MariaDB Connector/C installation needed

All implementations support both synchronous and asynchronous operations.

{% hint style="info" %}
**Version 1.1 is the latest stable (GA) release; version 2.0 is currently a Release Candidate (RC).** Choose the version that fits your needs below. Do not use non-stable (non-GA) releases in production.
{% endhint %}

## Supported Versions

### Server Compatibility

MariaDB Connector/Python connects to MariaDB and MySQL database servers. Individual server-side features may require a minimum server version; those requirements are noted with the feature.

### Supported Release Series

The following MariaDB Connector/Python release series are currently supported:

| Release Series | Stable (GA) Date |
| -------------- | ---------------- |
| 1.1            | June 2022        |

For End of Standard Support and End of Life dates, see the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/).

Version 2.0 (currently 2.0.0rc2) is a Release Candidate and is not yet a supported release series.

### Requirements

| Requirement | 1.1 (GA) | 2.0 (RC) |
| ----------- | -------- | -------- |
| Python | CPython 3.9 through 3.14 | CPython 3.10 or later |
| MariaDB Connector/C | 3.3.1 or later, always required | 3.3.1 or later, and only for the `c` and `binary` extras — the pure Python build requires none |

### Checking Your Installed Version

Connector/Python reports both its own version and the version of the underlying MariaDB Connector/C:

```python
import mariadb

print(mariadb.__version__)          # connector version, e.g. '1.1.14'
print(mariadb.__version_info__)     # same, as a tuple: (1, 1, 14)
print(mariadb.client_version)       # MariaDB Connector/C version, numeric
print(mariadb.client_version_info)  # MariaDB Connector/C version, as a tuple
```

## Installation

**Installation — version 1.1 (stable / GA):**

A plain `pip3 install` installs the latest stable release (1.1). It always installs the C extension and requires MariaDB Connector/C to be pre-installed; connection pooling is included by default.

```bash
# Latest stable release (1.1)
$ pip3 install mariadb

# Pin to a specific 1.1 release
$ pip3 install mariadb==1.1.14
```

**Installation — version 2.0 (Release Candidate):**

Version 2.0 is a pre-release, so the `--pre` flag is required — without it, pip installs the latest GA release (1.1).

```bash
# Pure Python (default)
$ pip3 install --pre mariadb

# C extension for maximum performance
$ pip3 install --pre mariadb[c]

# Pre-compiled binary wheels
$ pip3 install --pre mariadb[binary]

# With connection pooling
$ pip3 install --pre mariadb[binary,pool]
```

## Links

* [Documentation](https://mariadb-corporation.github.io/mariadb-connector-python/index.html)
* [Bug tracker](https://jira.mariadb.org)
* Sources are hosted on [Github](https://github.com/mariadb-corporation/mariadb-connector-python)

<sub>_This page is_</sub> [<sub>_covered_</sub>](license.md) <sub>_by the_</sub> [<sub>_Creative Commons Attribution 3.0 license_</sub>](https://creativecommons.org/licenses/by/3.0/legalcode)<sub>_._</sub>

{% @marketo/form formId="4316" %}
