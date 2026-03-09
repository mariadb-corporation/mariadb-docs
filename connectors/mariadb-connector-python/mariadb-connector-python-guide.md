# About Connector/Python

{% include "https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/~/reusable/9p9Gnd3FcRNTnYakGG0J/" %}

MariaDB Connector/Python enables python programs to access MariaDB and MySQL databases, using an API which is compliant with the Python DB API 2.0 (PEP-249).

**Version 2.0** offers flexible distribution options:
- **Pure Python** - Works on all platforms, no compiler required
- **C extension** - Maximum performance (2-12× faster on data-heavy workloads)
- **Pre-compiled wheels** - No MariaDB Connector/C installation needed

All implementations support both synchronous and asynchronous operations.

**Installation:**

```bash
# Pure Python (default)
$ pip3 install mariadb

# C extension for maximum performance
$ pip3 install mariadb[c]

# Pre-compiled binary wheels
$ pip3 install mariadb[binary]

# With connection pooling
$ pip3 install mariadb[binary,pool]
```

### Links:

* [Documentation](https://mariadb-corporation.github.io/mariadb-connector-python/index.html)
* [Bug tracker](https://jira.mariadb.org)
* Sources are hosted on [Github](https://github.com/mariadb-corporation/mariadb-connector-python)

<sub>_This page is_</sub> [<sub>_covered_</sub>](license.md) <sub>_by the_</sub> [<sub>_Creative Commons Attribution 3.0 license_</sub>](https://creativecommons.org/licenses/by/3.0/legalcode)<sub>_._</sub>

{% @marketo/form formId="4316" %}
