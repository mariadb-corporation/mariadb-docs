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

### Links:

* [Documentation](https://mariadb-corporation.github.io/mariadb-connector-python/index.html)
* [Bug tracker](https://jira.mariadb.org)
* Sources are hosted on [Github](https://github.com/mariadb-corporation/mariadb-connector-python)

<sub>_This page is_</sub> [<sub>_covered_</sub>](license.md) <sub>_by the_</sub> [<sub>_Creative Commons Attribution 3.0 license_</sub>](https://creativecommons.org/licenses/by/3.0/legalcode)<sub>_._</sub>

{% @marketo/form formId="4316" %}
