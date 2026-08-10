---
name: mariadb-connector-c-install
description: "Installing and configuring MariaDB Connector/C, the C client library the other MariaDB connectors build on — the runtime and development package names per distribution (`libmariadb3`/`libmariadb-dev`, `MariaDB-shared`/`MariaDB-devel`), how to get compile and link flags from `mariadb_config` or pkg-config `libmariadb` rather than hardcoding them, the build-from-source prerequisites, and the configuration side: that the library reads option files only when the application asks for them via `MYSQL_READ_DEFAULT_FILE` or `MYSQL_READ_DEFAULT_GROUP`, which option groups it reads, how `!includedir` and unknown options differ from the server, and which TLS options depend on the library it was built against. Use when installing, building, packaging, or configuring Connector/C."
---

# MariaDB Connector/C: Installation and Configuration

*Last updated: 2026-08-10*

MariaDB Connector/C is the C client library for MariaDB, and the layer that MariaDB Connector/Python, Connector/C++, and Connector/ODBC are built on. This skill covers installing it, getting an application to compile and link against it, and configuring it through option files and connection options. For calling the API, see **`mariadb-connector-c-usage`**.

> **Default context:** Assume the **3.4** stable line unless the user states otherwise. Options introduced later than the 3.0 baseline carry the release that added them. Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Installs only the runtime package and then tries to compile | Compiling needs the **development** package as well: `libmariadb-dev` on Debian and Ubuntu, `MariaDB-devel` on RHEL, Rocky Linux, and SLES. The runtime alone (`libmariadb3` / `MariaDB-shared`) has no headers and no `mariadb_config` |
| Hardcodes `-I/usr/include/mysql -lmysqlclient` | Ask the installed connector instead: **`mariadb_config --cflags --libs`**, or `pkg-config --cflags --libs libmariadb`. The library is **`-lmariadb`**, and the include directory differs per distribution and per build |
| Expects the library to pick up `/etc/my.cnf` or `~/.my.cnf` automatically | It does **not**. `mysql_real_connect()` reads option files only if the application first called `mysql_optionsv()` with **`MYSQL_READ_DEFAULT_FILE`** or **`MYSQL_READ_DEFAULT_GROUP`**. This is the single most common configuration surprise — the command-line clients read option files because *they* opt in |
| Assumes only `[client]` is read | Connector/C reads **`[client]`, `[client-server]`, and `[client-mariadb]`**, and a fourth custom group if one is named via `MYSQL_READ_DEFAULT_GROUP`. Precedence follows the order the sections appear in the file, not the order of the group names |
| Calls `MYSQL_READ_DEFAULT_FILE` twice to read a custom file *and* the defaults | Both options are **exclusive** — a second call replaces the first. Pass the custom path in one call; reading the default files is governed separately by `MYSQL_READ_DEFAULT_GROUP` |
| Uses `!includedir /etc/my.cnf.d/` expecting every `.cnf` in the directory | Unlike the server, Connector/C reads only **`my.cnf`** (and `my.ini` on Windows) from the named directory. See CONC-396 |
| Writes `max-allowed-packet=1G` in an option file | Numeric suffixes are **not** parsed. The connector reads the leading digits and silently discards `K`, `M`, or `G` — write the plain byte count |
| Guards a risky option with the `loose` prefix | Option prefixes have no meaning here. Unknown options are **silently ignored** anyway, so `loose-` is unnecessary and misleading. See CONC-415 |
| Assumes every `ssl-*` option works everywhere | The available TLS options depend on which library the connector was **built against** — OpenSSL, GnuTLS, or Schannel. `ssl-capath` and `ssl-crlpath` need OpenSSL; `ssl-crl` needs OpenSSL or Schannel; `ssl-passphrase` needs OpenSSL or GnuTLS |
| Sets `ssl-ca` and considers the connection authenticated | Encryption and identity are separate. Add **`ssl-verify-server-cert`** (`MYSQL_OPT_SSL_VERIFY_SERVER_CERT`) to actually verify the server certificate |
| Uses a relative path for a certificate or key | The `ssl-ca`, `ssl-capath`, `ssl-cert`, `ssl-key`, `ssl-crl`, and `ssl-crlpath` options all require **absolute** paths |
| Expects a dropped connection to come back by itself | **`reconnect` defaults to `false`** (`MYSQL_OPT_RECONNECT`). Nothing reconnects unless the application asks |
| Ships client plugins and expects them to be found | The plugin directory is set with `MYSQL_PLUGIN_DIR`, the `plugin-dir` option, or the **`MARIADB_PLUGIN_DIR`** environment variable. Authentication plugins that are not on that path simply fail to load |
| Sets `$MYSQL_HOME` on a machine that also has `$MARIADB_HOME` | **`$MARIADB_HOME` wins outright** — when it is set, `$MYSQL_HOME` is ignored entirely rather than merged |

## Installing

### Linux, from the MariaDB package repository

Configure the repository first — `mariadb_repo_setup` for Community Server, `mariadb_es_repo_setup` (with a customer download token) for Enterprise Server. All major releases of a given server line ship the same Connector/C version.

```bash
# Debian, Ubuntu
sudo apt install libmariadb3 libmariadb-dev

# CentOS, RHEL, Rocky Linux
sudo yum install MariaDB-shared MariaDB-devel

# SLES
sudo zypper install MariaDB-shared MariaDB-devel
```

Binary tarballs for Linux and an MSI installer for Windows are available from the MariaDB Connector/C download page when the distribution's packages are unsuitable.

### Building from source

```bash
cmake -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo .
cmake --build build
sudo cmake --install build
```

Prerequisites:

- **Linux and macOS** — gcc 3.4.6 or newer, CMake 3.12.0 or newer, and TLS libraries: OpenSSL 1.0.1+ or GnuTLS 3.4.2+. The remote-io plugin additionally needs Curl; the GSSAPI plugin needs Kerberos V5.
- **Windows** — Visual Studio 2013 or newer and CMake 3.12.0 or newer.

## Compiling an application against it

```bash
gcc app.c $(mariadb_config --cflags --libs) -o app
```

`mariadb_config` also reports `--version`, `--cc_version`, `--socket`, `--port`, and `--plugindir`, which is the reliable way to discover how a given installation was configured. Under pkg-config the module is `libmariadb`. In code, the public header is `mysql.h` and the API is `mysql_`-prefixed — that naming is historical and is what the library actually exports.

## Configuration

### Turning on option files

```c
MYSQL *mysql = mysql_init(NULL);

/* Read the default option files: /etc/my.cnf, /etc/mysql/my.cnf,
   $MARIADB_HOME (or $MYSQL_HOME)/my.cnf, ~/.my.cnf */
mysql_optionsv(mysql, MYSQL_READ_DEFAULT_FILE, NULL);

/* …or one specific file */
mysql_optionsv(mysql, MYSQL_READ_DEFAULT_FILE, (void *)"/etc/myapp/db.cnf");

/* Read an application-specific group in addition to the standard ones */
mysql_optionsv(mysql, MYSQL_READ_DEFAULT_GROUP, (void *)"myapp");

mysql_real_connect(mysql, host, user, passwd, db, 0, NULL, 0);
```

Without at least one of those two calls, every setting must be passed programmatically.

An option file for the above might read:

```ini
[client]
port=3306
socket=/var/run/mysqld/mysqld.sock

[client-mariadb]
ssl-ca=/etc/ssl/certs/ca.pem
ssl-verify-server-cert

[myapp]
default-character-set=utf8mb4
connect-timeout=10
```

Dashes and underscores in option names are interchangeable in Connector/C 3.1.1 and later.

### Options worth setting deliberately

| Option | `mysql_optionsv` name | Note |
|---|---|---|
| `connect-timeout` | `MYSQL_OPT_CONNECT_TIMEOUT` | Seconds; no default, so a dead host blocks until the OS gives up |
| `default-character-set` | `MYSQL_SET_CHARSET_NAME` | Set it explicitly rather than inheriting the build default |
| `local-infile` | `MYSQL_OPT_LOCAL_INFILE` | Defaults to `false`; `LOAD DATA LOCAL INFILE` fails until enabled on both ends |
| `max-allowed-packet` | `MYSQL_OPT_MAX_ALLOWED_PACKET` | 16 MB default, 1 GB ceiling, plain integers only |
| `multi-statements` | `MARIADB_OPT_MULTI_STATEMENTS` | Off by default; also implies multi-results |
| `init-command` | `MYSQL_INIT_COMMAND` | **Multi-element** — each occurrence across option files appends rather than replaces, and all of them run on every connect and reconnect |
| `tls_version` | `MARIADB_OPT_TLS_VERSION` | Comma-separated allow-list, `TLSv1.0` through `TLSv1.3` (3.0.4+) |
| `ssl-fp`, `ssl-fp-list` | `MARIADB_OPT_SSL_FP` | Certificate fingerprint pinning; SHA1 only before 3.4.0, SHA256/384/512 from 3.4.0 |

MySQL's obfuscated `.mylogin.cnf` credential file is not supported.

### Checking what a configuration resolves to

`my_print_defaults` reads the same files and groups and prints the result, which settles most "why is it still connecting to the wrong socket" questions:

```bash
my_print_defaults myapp client client-server client-mariadb
```

## See Also

- **`mariadb-connector-c-usage`** — using the API once it is installed: connecting, prepared statements, transactions, result handling
- **`mariadb-connector-python-install`**, **`mariadb-connector-cpp-install`**, **`mariadb-connector-odbc-install`** — connectors that depend on this library
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-c>
