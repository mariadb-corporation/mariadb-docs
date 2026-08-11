---
name: mariadb-connector-odbc-install
description: "Installing and configuring MariaDB Connector/ODBC — that a driver manager (unixODBC on Linux, iODBC on macOS, the built-in manager on Windows) is a prerequisite and the driver has to be registered with it in `odbcinst.ini` before any DSN or `DRIVER=` connection string resolves; that the driver's own bitness must match the driver manager's; where `odbcinst`, `ODBCSYSINI`, `ODBCINI`, and `ODBCINSTINI` put the configuration; that the canonical DSN keywords are `UID` and `PWD` with `USER` and `PASSWORD` as synonyms; and the TLS keywords `SSLCA`, `SSLVERIFY`, `FORCETLS`, and `TLSVERSION`. Use when installing the driver, writing an `odbcinst.ini` or `odbc.ini` entry, building a connection string, or diagnosing a data source that will not connect."
---

# MariaDB Connector/ODBC: Installation and Configuration

*Last updated: 2026-08-10*

MariaDB Connector/ODBC is an ODBC 3.8-compliant driver built on MariaDB Connector/C. Almost everything that goes wrong with it goes wrong before the first query: the driver manager cannot find the driver, the bitness does not match, or the DSN is in a file nothing reads. This skill covers that layer. For the ODBC API itself, see **`mariadb-connector-odbc-usage`**.

> **Default context:** Assume the **3.2** stable line unless the user states otherwise. The 3.1 line is the previous series and is still supported. Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Installs the driver and connects straight away | ODBC always goes through a **driver manager**: unixODBC on Linux, iODBC on macOS, the built-in manager on Windows. The driver must be **registered** with it before either a DSN or a `DRIVER=` connection string can resolve |
| Installs MariaDB Connector/C first, as Connector/C++ requires | Not necessary here. The **binary packages carry Connector/C with them**. A source build can use the bundled `libmariadb` submodule or link the system one, but an installed driver package is self-contained |
| Edits `/etc/odbcinst.ini` by hand and hopes the path is right | Use **`odbcinst`**, which writes to whatever paths the local unixODBC was actually built with: `sudo odbcinst -i -d -f driver-template.ini` for the driver, `-i -s -l -f` for a system DSN, `-i -s -h -f` for a user DSN |
| Mixes a 64-bit driver with a 32-bit driver manager | Bitness must match end to end — driver, driver manager, and application. On Windows this means opening the **matching** version of the ODBC Data Source Administrator; the 64-bit and 32-bit tools show different lists |
| Adds a DSN through the unixODBC GUI | The driver **does not support the unixODBC GUI for adding DSNs**. Write the `.ini` entry or use `odbcinst` |
| Cannot find the configuration and assumes it is missing | Three environment variables move it: **`ODBCSYSINI`** (directory of the system files, default `/etc`), **`ODBCINSTINI`** (driver file name, relative to `ODBCSYSINI`, default `odbcinst.ini`), and **`ODBCINI`** (user DSN file, default `~/.odbc.ini`) |
| Writes `SERVER=…;USER=…;PASSWORD=…` and assumes those are the real keywords | They work — but as **synonyms**. The canonical ODBC keywords are **`UID`** and **`PWD`**, alongside `SERVER`, `PORT`, `DATABASE`, and `DRIVER` or `DSN` |
| Sets `SSLCA` and treats the connection as verified | Setting any of the `SSL*` keywords turns TLS on, but **`SSLVERIFY=1`** is what makes the server prove its identity against that CA. **`FORCETLS=1`** requires TLS without supplying certificate material at all |
| Assumes the driver reads `my.cnf` like the command-line clients | Only when asked: the **`USE_MYCNF`** option turns option-file reading on. Otherwise every setting comes from the DSN or the connection string |
| Expects `SQLExecDirect` to use server-side prepared statements | Only `SQLPrepare` uses the binary protocol by default. One-shot `SQLExecDirect` calls default to the client-side text protocol unless **`EDSERVER=1`** (or the `SQL_ATTR_EXECDIRECT_ON_SERVER` attribute) is set |
| Installs on macOS and dutifully registers the driver | The **PKG package registers itself** in `/Library/ODBC/odbcinst.ini`, so that step is usually already done |
| Declares the setup working without testing it | Test the DSN outside the application: **`isql <dsn>`** with unixODBC, **`iodbctest "DSN=<dsn>"`** with iODBC. That separates a driver-manager problem from an application problem |

## Installing

### Linux

Install unixODBC and its tools, then the driver package downloaded for the distribution:

```bash
sudo apt install unixodbc odbcinst          # Debian, Ubuntu
sudo yum install unixODBC                   # RHEL, Rocky Linux
```

### Registering the driver

```ini
# MariaDB_odbc_driver_template.ini
[MariaDB ODBC 3.2 Driver]
Description = MariaDB Connector/ODBC v.3.2
Driver = /usr/lib64/libmaodbc.so
```

```bash
sudo odbcinst -i -d -f MariaDB_odbc_driver_template.ini
```

At this point `SQLDriverConnect` works with `Driver={MariaDB ODBC 3.2 Driver};…`, with no DSN involved.

### Defining a DSN

```ini
# MariaDB_odbc_data_source_template.ini
[MariaDB-server]
Description = MariaDB server
Driver      = MariaDB ODBC 3.2 Driver
SERVER      = db.example.com
PORT        = 3306
UID         = app
PWD         = secret
DATABASE    = appdb
```

```bash
sudo odbcinst -i -s -l -f MariaDB_odbc_data_source_template.ini   # system-wide, /etc/odbc.ini
odbcinst -i -s -h -f MariaDB_odbc_data_source_template.ini        # this user, ~/.odbc.ini
```

### macOS

macOS uses iODBC. The PKG package registers the driver in `/Library/ODBC/odbcinst.ini` automatically; the driver library lives at `/Library/MariaDB/MariaDB-Connector-ODBC/libmaodbc.dylib`. DSNs go in `~/Library/ODBC/odbc.ini` or `/Library/ODBC/odbc.ini`.

### Windows

Install the MSI, then define the DSN in the ODBC Data Source Administrator — taking care to open the version matching the driver's bitness.

### Building from source

```bash
sudo apt install git cmake make gcc libssl-dev unixodbc odbcinst unixodbc-dev
# or: sudo yum install git cmake make gcc openssl openssl-devel unixODBC unixODBC-devel

git clone https://github.com/MariaDB/mariadb-connector-odbc.git
cd mariadb-connector-odbc
git submodule update --init --recursive      # brings in the bundled libmariadb
cmake -B build -DCMAKE_BUILD_TYPE=RelWithDebInfo .
cmake --build build
sudo cmake --install build
```

OpenSSL development headers are what make the resulting driver TLS-capable on Unix-like platforms; on Windows there are no dependencies beyond CMake, git, and Visual Studio.

## Configuration

### Connection-string keywords

The same keywords work in a DSN file and in a `SQLDriverConnect` string:

| Keyword | Purpose |
|---|---|
| `DRIVER`, `DSN` | Which driver, or which predefined data source |
| `SERVER`, `PORT`, `SOCKET`, `NamedPipe` | Where the server is |
| `UID`, `PWD` | Credentials (`USER`, `PASSWORD` are synonyms) |
| `DATABASE` | Default schema |
| `CHARSET` | Connection character set |
| `INITSTMT` | Statement executed on connect |
| `CONN_TIMEOUT` | Connect timeout, in seconds |
| `AUTO_RECONNECT` | Reconnect after a dropped connection |
| `USE_MYCNF` | Read settings from MariaDB option files as well |
| `EDSERVER` | Send `SQLExecDirect` statements as server-side prepared statements |
| `FORWARDONLY` | Force forward-only cursors |
| `PLUGIN_DIR` | Where the Connector/C authentication plugins live |
| `OPTION` | Legacy numeric flag word; prefer the named options above |

### TLS keywords

| Keyword | Purpose |
|---|---|
| `SSLCA`, `SSLCAPATH` | Trusted CA certificate, or a directory of them |
| `SSLCERT`, `SSLKEY`, `TLSKEYPWD` | Client certificate for mutual TLS, and the key passphrase |
| `SSLVERIFY` | Verify the server certificate — off unless set |
| `FORCETLS` | Refuse to connect unencrypted |
| `SSLCIPHER`, `TLSVERSION` | Restrict cipher suites and protocol versions |
| `SSLCRL`, `SSLCRLPATH` | Certificate revocation list |
| `TLSPEERFP`, `TLSPEERFPLIST` | Pin the server certificate by fingerprint |

```
Driver={MariaDB ODBC 3.2 Driver};SERVER=db.example.com;PORT=3306;
UID=app;PWD=secret;DATABASE=appdb;
SSLCA=/etc/ssl/certs/ca.pem;SSLVERIFY=1;FORCETLS=1
```

Which of the certificate options are honored depends on the TLS library the bundled Connector/C was built against — see **`mariadb-connector-c-install`**.

## Verifying the install

```bash
isql MariaDB-server                     # unixODBC
iodbctest "DSN=MariaDB-server"          # iODBC
```

A "data source name not found" error is a driver-manager registration problem; an authentication or TLS error means the registration worked and the problem has moved to the connection settings.

## See Also

- **`mariadb-connector-odbc-usage`** — using the driver once it is registered: handles, binding, prepared statements, cursors, diagnostics
- **`mariadb-connector-c-install`** — the underlying client library, and the TLS behavior it determines
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-odbc>

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
