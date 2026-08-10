---
name: mariadb-connector-python-install
description: "Installing and configuring MariaDB Connector/Python (the `mariadb` PyPI module) — that a plain `pip install mariadb` gets the 1.1 GA line, which always builds the C extension and so needs MariaDB Connector/C 3.3.1 or later with `mariadb_config` on the `PATH`; that the pure-Python, binary-wheel and pooling variants exist only on the 2.0 line and need `pip install --pre mariadb[...]`; that pooling is built in on 1.1 but a separate `[pool]` extra on 2.0; the Python floor (3.8 on 1.1, 3.10 on 2.0); that option files are read only when `default_file` or `default_group` is passed; and that `ssl_verify_cert` defaults to off on 1.1. Use when installing, packaging, containerizing, or configuring the `mariadb` module, or when diagnosing a failed build or connection setup."
---

# MariaDB Connector/Python: Installation and Configuration

*Last updated: 2026-08-10*

MariaDB Connector/Python is published on PyPI as **`mariadb`**. This skill covers getting it installed and configured — the install variants, their prerequisites, the build failures that follow from picking the wrong one, and the connection settings that belong in configuration rather than in code. For writing queries against an established connection, see **`mariadb-connector-python-usage`**.

> **Default context:** Assume the **1.1** stable (GA) line unless the user states otherwise. Behavior that applies only to the newer **2.0** line — which is still a release candidate — is marked *since 2.0*. Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `pip install mariadb` yields a pure-Python package with no system dependencies | On the current GA line (**1.1**) it does not. 1.1 **always** builds the C extension, so the machine needs **MariaDB Connector/C 3.3.1 or later** and a C compiler. A pure-Python install exists only *since 2.0* |
| Reaches for `pip install --pre` only when told to | The reverse: plain `pip install mariadb` deliberately resolves to **1.1**, because 2.0 is still a release candidate and pip skips pre-releases. `--pre` is **required** to get 2.0: `pip install --pre mariadb` |
| Writes `mariadb[binary]`, `mariadb[c]`, or `mariadb[pool]` against 1.1 | Those extras are **2.0-only**. On 1.1 there is one install and it includes pooling. Combine them *since 2.0*: `pip install --pre mariadb[binary,pool]` |
| Assumes connection pooling always ships in the box | True on 1.1. *Since 2.0* pooling is a separate optional package — without the **`[pool]`** extra, `ConnectionPool` is unavailable |
| Build fails with `mariadb_config not found` and the agent installs a compiler | The compiler is not the missing piece. **`mariadb_config` ships with the Connector/C development package** and must be on the `PATH`: `libmariadb-dev` (Debian, Ubuntu) or `MariaDB-devel` (RHEL, Rocky, SLES). Alternatively, point at it explicitly in `site.cfg` |
| Targets any Python 3 | The floor differs by line: **1.1 requires Python 3.8+**, **2.0 requires Python 3.10+** |
| Installs `mysql-connector-python`, `mysqlclient`, or `PyMySQL` and imports `mariadb` | The distribution and the module are both **`mariadb`** — `pip install mariadb`, then `import mariadb`. No other PyPI package provides this API |
| Builds a slim container image, then wonders why `import mariadb` fails at runtime | A source install needs the Connector/C **development** files at build time and the **runtime** library afterwards. In a multi-stage image, install `libmariadb3` (or `MariaDB-shared`) in the final stage, or *since 2.0* use `mariadb[binary]`, whose wheels bundle Connector/C |
| Puts host, user, and password in code and expects `~/.my.cnf` to be picked up anyway | Option files are **not** read by default. Pass **`default_file`** (a path, or `""` for the standard locations) or **`default_group`**; explicit `connect()` arguments still win over option-file values |
| Assumes TLS verifies the server certificate as soon as `ssl_ca` is set | On **1.1**, **`ssl_verify_cert` defaults to `False`** — the connection is encrypted but the server is unauthenticated until you pass `ssl_verify_cert=True`. *Since 2.0* the default flips to `True` |
| Pins nothing, or pins the connector to the server version | Pin the connector line explicitly (`mariadb==1.1.14`). Connector releases are **independent of the server release**; there is no matching 11.8 or 12.x connector |

## Installing

### Version 1.1 (stable, GA)

Install the Connector/C development files first, then the module:

```bash
# Debian, Ubuntu
sudo apt install libmariadb3 libmariadb-dev

# RHEL, Rocky Linux, SLES
sudo dnf install MariaDB-shared MariaDB-devel

pip install mariadb            # latest 1.1
pip install mariadb==1.1.14    # pinned
```

Connector/C itself comes from the MariaDB package repository; configure it with `mariadb_repo_setup` (Community Server) or `mariadb_es_repo_setup` (Enterprise Server) if the distribution's own packages are too old. On POSIX systems the build reads `mariadb_config` from the `PATH`; if it lives somewhere unusual, set the path in `site.cfg`:

```ini
[cc_options]
mariadb_config=/usr/local/bin/mariadb_config
```

### Version 2.0 (release candidate)

Three variants, all requiring `--pre`:

```bash
pip install --pre mariadb                # pure Python — no compiler, no Connector/C
pip install --pre mariadb[c]             # C extension — needs Connector/C 3.3.1+
pip install --pre mariadb[binary]        # prebuilt wheel — Connector/C bundled
pip install --pre mariadb[binary,pool]   # …and connection pooling
```

The pure-Python implementation runs on any interpreter and needs no system libraries; the C extension is the faster option on data-heavy workloads. The API is the same either way, so the choice is a deployment decision, not a code one.

### Microsoft Windows

Binary wheels are the path of least resistance, because they carry Connector/C with them:

```bash
pip install --pre mariadb[binary,pool]
```

To build the C extension instead, install MariaDB Connector/C from its MSI package first, then `pip install --pre mariadb[c,pool]`.

## Configuration

### Where connection settings can live

`connect()` keyword arguments are the primary mechanism, but host, port, user, socket, and the TLS settings can equally come from a MariaDB option file — useful for keeping credentials out of source:

```python
import mariadb

# Read ~/.my.cnf and the other standard locations, plus a custom group
conn = mariadb.connect(
    default_file="",             # "" = standard locations; or an explicit path
    default_group="myapp",       # read in addition to [client], [client-server], [client-mariadb]
    database="appdb",
)
```

Setting either `default_file` or `default_group` is what switches option-file reading on. On Windows the file must be an `.ini` file. Explicit keyword arguments override anything the option file supplies.

### TLS

```python
conn = mariadb.connect(
    host="db.example.com", user="app", password="secret", database="appdb",
    ssl_ca="/etc/ssl/certs/ca.pem",
    ssl_cert="/etc/ssl/certs/client-cert.pem",
    ssl_key="/etc/ssl/private/client-key.pem",
    ssl_verify_cert=True,        # on 1.1 this is NOT the default — set it explicitly
)
```

`ssl_capath`, `ssl_cipher`, `ssl_crl`, and `ssl_crlpath` are also accepted; which of them the underlying Connector/C honors depends on the TLS library it was built against.

### Pooling configuration

On 1.1, `ConnectionPool` is available immediately; *since 2.0* it requires the `[pool]` extra. Pool sizing belongs with the rest of the deployment configuration:

```python
pool = mariadb.ConnectionPool(
    pool_name="app", pool_size=8,   # maximum 64
    pool_reset_connection=True,     # the default
    host="localhost", user="app", password="secret", database="appdb",
)
```

## Verifying the install

```python
import mariadb
print(mariadb.__version__)                 # module version
conn = mariadb.connect(host="localhost", user="app", password="secret")
print(conn.get_server_version())           # proves the round trip works
```

A failure at `import mariadb` points at the runtime library or the wheel; a failure at `connect()` points at credentials, networking, or TLS.

## See Also

- **`mariadb-connector-python-usage`** — using the module once it is installed: parameters, transactions, cursors, pooling, error handling
- **`mariadb-connector-c-install`** — installing and configuring the underlying C client library this module builds against
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-python>
