---
description: >-
  Deploy, start, stop, and delete throwaway local MariaDB or MySQL server
  instances for development and testing with the sandbox global object.
icon: box-open
---

# Sandbox Instances

A sandbox is a complete, self-contained server instance on your own machine, created in a directory of its own and identified by its port. The `sandbox` global object deploys sandboxes and manages their life cycle, so you can get a disposable server for a test, a demo, or a dump-and-load trial in a few seconds and remove it without a trace afterward.

The `sandbox` object is a built-in plugin of MariaDB Shell. It works with MariaDB Server and with MySQL Server: it uses the server binary that it finds, detects the vendor, and initializes the instance the way that vendor requires.

{% hint style="warning" %}
Sandboxes are meant for local development and testing only. They use small memory and log sizes and self-signed certificates. Don't use them for production data.
{% endhint %}

## Requirements

* MariaDB Server or MySQL Server binaries on the same machine. An unpacked server package is enough: the server doesn't have to be installed. The plugin looks for `mariadbd`, then `mysqld`, on the `PATH`. Use the `mariadbdPath` option to point it at other binaries.
* For MariaDB Server, the data directory initialization tool `mariadb-install-db` (or `mysql_install_db`) from the same server package, found next to the server binary or on the `PATH`. MySQL Server 8.0 and later needs no separate tool.
* For TLS with MariaDB Server, an `openssl` command-line tool. The plugin looks next to the server binaries, then in the MariaDB Shell installation, which includes one, then on the `PATH`. MySQL Server generates its own certificates.

If you don't have server binaries, see [Sandbox Server Packages](#sandbox-server-packages).

## Quick Start

```text
MariaDB  Py > sandbox.deploy(3310, {"password": "sandbox-root-pw"})
Deploying new MariaDB sandbox instance on port 3310...
Preparing sandbox boilerplate for mariadb-12.3.2-MariaDB-log (one-time per version)...
Generating SSL certificates for the sandbox...
Starting MariaDB sandbox instance...

Instance localhost:3310 successfully deployed and started.
SSL is enabled; the CA certificate is at '/home/dev/.mariadb-shell/sandboxes/3310/ca-cert.pem'.
Use shell.connect('root@localhost:3310') to connect to it.
MariaDB  Py > shell.connect("root@localhost:3310")
...
MariaDB localhost:3310 ssl  Py > \sql SELECT VERSION();
```

When you are done:

```text
MariaDB localhost:3310 ssl  Py > sandbox.stop(3310)
Closing the active session to the sandbox being stopped.
Stopping MariaDB sandbox instance on port 3310...
Instance localhost:3310 successfully stopped.
MariaDB  Py > sandbox.delete(3310)
Deleting MariaDB sandbox instance on port 3310...
Instance localhost:3310 successfully deleted.
```

## Functions

| Function | Description |
| --- | --- |
| `sandbox.deploy(port[, options])` | Creates, initializes, and starts a new sandbox. |
| `sandbox.start(port[, options])` | Starts a stopped sandbox. |
| `sandbox.stop(port[, options])` | Shuts down a running sandbox cleanly. |
| `sandbox.kill(port[, options])` | Terminates the server process of a sandbox immediately, without a clean shutdown. |
| `sandbox.delete(port[, options])` | Removes a stopped sandbox and its directory. |
| `sandbox.get_path(port[, path_id][, options])` | Returns the sandbox directory, its option file, or its error log. |
| `sandbox.vendor([port][, options])` | Returns `"MariaDB"` or `"MySQL"`. |
| `sandbox.version([port][, options])` | Returns the server version as `major.minor.patch`. |

The `port` must be between 1024 and 65535. Every function except `deploy()` needs the same `sandboxDir` that the sandbox was deployed with, unless you use the default directory.

All functions reject unknown option names, so a misspelled option fails instead of being ignored.

### deploy()

Deploys a plain, standalone instance: no replication or GTID settings are configured. The server is started, the root password is set, and the instance is left running.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `password` | string | Required | Password for the `root` accounts of the new instance. |
| `sandboxDir` | string | See [Sandbox Directory](#sandbox-directory) | Directory under which the sandbox directory, named after the port, is created. |
| `allowRootFrom` | string | `%` | Host pattern for an additional `root` account with all privileges, for connections from other hosts. An empty string creates no such account. |
| `serverId` | integer | Not set | Value for `server_id`. A standalone instance doesn't need one. |
| `ssl` | Boolean | `true`; `false` for MariaDB Server on Windows | Generate certificates and enable TLS. See [TLS](#tls). |
| `opensslPath` | string | Searched | Path to the `openssl` executable, or to a directory that contains it. Ignored for MySQL Server. |
| `mariadbdPath` | string | Searched on the `PATH` | Path to the `mariadbd` or `mysqld` binary, or to the top directory of the server binaries, such as an unpacked server package. |
| `mariadbdOptions` | list of strings | `[]` | Additional server options for the `[mysqld]` group of the option file, as `"name=value"` or `"name"`. They are applied after the TLS and network settings, so they can override them, `bind_address` included. An option replaces the default of the same name whatever its spelling, so `bind-address` or `loose_bind_address` also replaces `bind_address`. You can't override `port`. |
| `timeout` | integer | `60` | Seconds to wait for the instance to accept connections. |

The deployment fails if the sandbox directory already exists and isn't empty, or if another process already listens on the port.

```python
sandbox.deploy(3311, {
    "password": "sandbox-root-pw",
    "sandboxDir": "~/sandboxes",
    "allowRootFrom": "",
    "mariadbdOptions": ["character_set_server=utf8mb4", "max_connections=50"],
})
```

### start(), stop(), and kill()

| Function | Options |
| --- | --- |
| `start()` | `sandboxDir`; `timeout` (default `60`); `mariadbdPath`, to start the sandbox with a different server binary than the one it was deployed with. Giving it also rewrites the start and stop scripts and the recorded vendor and version. |
| `stop()` | `sandboxDir`; `timeout` (default `60`); `password`, the root password, which is needed only on Windows. |
| `kill()` | `sandboxDir`. |

On Linux and macOS, `stop()` sends the server process a `SIGTERM` signal, which triggers a clean shutdown, so no password is needed. On Windows, it connects as `root` and runs `SHUTDOWN`. If the global session is connected to the sandbox, `stop()` closes it first. Stopping a sandbox that isn't running only prints a message.

`kill()` ends the server process at once. Use it only when `stop()` doesn't work, because InnoDB has to run crash recovery at the next start.

### delete()

Takes the `sandboxDir` option. The sandbox must be stopped first; otherwise `delete()` fails with `The MariaDB sandbox on port 3310 is running. Stop it before deleting it.` Deleting removes the sandbox directory with its data, certificates, and logs.

### get\_path()

Returns a path that belongs to an existing sandbox. `path_id` selects which one:

| `path_id` | Returns |
| --- | --- |
| `""` or omitted | The sandbox directory. |
| `"config"` | The option file of the instance, `my.cnf`. |
| `"error"` | The server error log. |

To give `options` without a `path_id`, pass `None` or an empty string as the `path_id`:

```python
print(sandbox.get_path(3311, None, {"sandboxDir": "~/sandboxes"}))
```

### vendor() and version()

Without a port, both functions report on the server binary that a new deployment would use: the one on the `PATH`, or the one at `mariadbdPath`. They return `None` if no server binary can be found. With a port, they report what was recorded for that sandbox when it was deployed or last started with `mariadbdPath`. If nothing was recorded, as for a sandbox from an older release, they fall back to the server binary a new deployment would use.

```text
MariaDB  Py > sandbox.vendor(), sandbox.version()
('MariaDB', '12.3.2')
```

## Sandbox Directory

Each sandbox lives in `<sandboxDir>/<port>`. The default `sandboxDir` is the value of the `sandboxDir` [shell option](customizing/configuration-options.md):

| Platform | Default |
| --- | --- |
| Linux and macOS | `~/.mariadb-shell/sandboxes` |
| Windows | `%USERPROFILE%\MariaDB\mariadb-shell\sandboxes` |
| `MARIADB_SHELL_USER_CONFIG_HOME` set | `$MARIADB_SHELL_USER_CONFIG_HOME/sandboxes` |

To keep your sandboxes elsewhere without passing `sandboxDir` every time, persist the option:

```python
shell.options.set_persist("sandboxDir", "/data/sandboxes")
```

A sandbox directory contains:

| Entry | Content |
| --- | --- |
| `my.cnf` | The option file, with a `[mysqld]` group for the server and a `[client]` group for clients. |
| `sandboxdata/` | The data directory. The error log is `sandboxdata/error.log`. |
| `start.sh`, `stop.sh` (`start.bat`, `stop.bat` on Windows) | Scripts that start and stop the instance from a terminal, without MariaDB Shell. They contain the absolute path of the server binary, so they work even if the binary is not on the `PATH`. |
| `<port>.pid` | The process ID of the running server. |
| `ca-cert.pem`, `server-*.pem`, `client-*.pem` | The certificates and keys, for a MariaDB sandbox with TLS. |
| `tmp/` | A private temporary directory for the server. |
| `vendor`, `version` | The recorded server vendor and version. |

The files contain absolute paths, so moving a sandbox directory breaks it. Deploy a new sandbox instead.

### Boilerplates

Initializing a data directory takes a while. The first deployment for a server version therefore creates a boilerplate, an initialized data directory named `myboilerplate-<vendor>-<version>`, in the sandbox directory. Later deployments of the same version copy it, which takes about a second. To share boilerplates between several sandbox directories, set the `MARIADB_SANDBOX_BOILERPLATE_DIR` environment variable to a directory of your choice. Delete a boilerplate directory to force a fresh initialization.

## How an Instance Is Configured

* **Initialization.** MariaDB data directories are initialized with `mariadb-install-db`, with password authentication for `root`. MySQL data directories are initialized with `mysqld --initialize-insecure`.
* **Accounts.** The plugin sets the password of every `root` account the data directory has: `root@localhost`, `root@127.0.0.1`, and `root@::1`, and on MariaDB Server also the `root` account that `mariadb-install-db` creates for the host name of the machine. By default it also creates `root@'%'` with the same password. All of them have every privilege. On MariaDB Server, the root accounts use the server default, `mysql_native_password`.
* **Connections.** The instance listens on `127.0.0.1` only, so other hosts can't reach it; a MySQL sandbox's X Protocol port too. To accept connections from other hosts, add `"bind_address=*"` (or one address) to `mariadbdOptions`, and `"mysqlx_bind_address=*"` for X Protocol on MySQL Server. On Linux and macOS, the instance also listens on a Unix socket. The socket path is `<sandbox directory>/mysqld.sock`, or a short path in the temporary directory when the full path would be too long for a socket. On Windows, the instance listens on TCP only.
* **Resources.** The option file keeps InnoDB small: a 16 MB buffer pool, a 10 MB initial system tablespace, and a small redo log. The Performance Schema is enabled. To give a sandbox more memory, pass a larger `innodb_buffer_pool_size` in `mariadbdOptions`. Don't change `innodb_data_file_path`: it must match the boilerplate that the data directory was copied from.
* **Faster DDL for tests.** If the `MARIADB_SANDBOX_NO_SYNC` environment variable is set to a non-empty value when you deploy, MariaDB sandboxes run with `debug-no-sync`. DDL statements become much faster, especially on macOS, but everything except InnoDB data is no longer safe from an operating system crash. MySQL sandboxes ignore the variable.

## TLS

By default, a sandbox serves TLS connections with certificates that are generated for it:

* **MariaDB Server.** The plugin creates a private certificate authority, a server certificate, and a client certificate in the sandbox directory, valid for 10 years. The `[mysqld]` group points the server at the CA and server certificate, and the `[client]` group points clients at the CA and client certificate.
* **MySQL Server.** The server generates its own certificates in the data directory while it is initialized, and the plugin uses those.

To deploy without TLS, set `ssl` to `false`. For MariaDB Server, the option file then contains `skip_ssl`, because recent MariaDB Server versions enable TLS on their own and refuse to start when they can't load a key.

{% hint style="info" %}
**Windows:** For MariaDB Server on Windows, `ssl` defaults to `false`, and `deploy()` prints a note. The MariaDB Server builds for Windows use the bundled wolfSSL library, whose server side doesn't complete TLS handshakes with MariaDB Shell or with other clients. Set `ssl` to `true` only for a MariaDB Server build that uses OpenSSL. MySQL Server on Windows, and all servers on Linux and macOS, use TLS by default.
{% endhint %}

On Windows, `mariadb-install-db.exe` doesn't accept an option file, so the boilerplate is created with the default InnoDB file sizes. The sandbox's own option file still applies the small sizes, and the redo log shrinks when the sandbox first starts.

## MariaDB and MySQL Sandboxes

The plugin reads the vendor from the `--version` output of the server binary and records it in the sandbox directory. Messages name the vendor, as in `Deploying new MySQL sandbox instance on port 3320...`. The differences:

| | MariaDB Server | MySQL Server |
| --- | --- | --- |
| Initialization | `mariadb-install-db` | `mysqld --initialize-insecure` |
| Certificates | Generated with `openssl` | Generated by the server |
| Redo log sizing | `innodb_log_file_size` | `innodb_redo_log_capacity` on versions that have it |
| `debug-no-sync` with `MARIADB_SANDBOX_NO_SYNC` | Yes | No |
| Root authentication | `mysql_native_password` | `caching_sha2_password` |

To deploy a MySQL sandbox while MariaDB Server is on the `PATH`, point `mariadbdPath` at the MySQL binaries:

```python
sandbox.deploy(3320, {"password": "sandbox-root-pw", "mariadbdPath": "/opt/mysql-9.4"})
```

## Sandbox Server Packages

Each MariaDB Shell release on [GitHub](https://github.com/mariadb-corporation/mariadb-shell/releases) also carries minimal MariaDB Server packages for sandboxes, with the checksums in `SERVER_SHA256SUMS`. The 26.9.5 release includes MariaDB Server 11.8.9, 12.3.3, and 13.1.1 for each supported platform, named like the shell packages with a `-sandbox` suffix:

```text
mariadb-13.1.1-linux-glibc2.34-x86-64bit-sandbox.tar.gz
mariadb-13.1.1-linux-glibc2.34-arm-64bit-sandbox.tar.gz
mariadb-13.1.1-macos15-x86-64bit-sandbox.tar.gz
mariadb-13.1.1-macos26-arm-64bit-sandbox.tar.gz
mariadb-13.1.1-windows-x86-64bit-sandbox.tar.gz
mariadb-13.1.1-windows-arm-64bit-sandbox.tar.gz
```

The packages contain only what a sandbox needs, such as the server, `mariadb-install-db`, and `mariadb-admin`. The Linux packages run on distributions with glibc 2.34 or later, such as RHEL 9, Ubuntu 22.04, and Debian 12.

Neither the `sandbox` plugin nor the installation scripts download these packages. Download one, verify it, unpack it, and point `mariadbdPath` at it, or put its `bin` directory on the `PATH`:

```sh
curl -fLO https://github.com/mariadb-corporation/mariadb-shell/releases/download/v26.9.5/mariadb-12.3.3-linux-glibc2.34-x86-64bit-sandbox.tar.gz
curl -fLO https://github.com/mariadb-corporation/mariadb-shell/releases/download/v26.9.5/SERVER_SHA256SUMS
sha256sum -c SERVER_SHA256SUMS --ignore-missing
mkdir -p ~/servers && tar -xzf mariadb-12.3.3-linux-glibc2.34-x86-64bit-sandbox.tar.gz -C ~/servers
mariadb-shell -- sandbox deploy 3312 --password=sandbox-root-pw --mariadbd-path=~/servers/mariadb-12.3.3-linux-glibc2.34-x86-64bit-sandbox
```

On macOS, use `shasum -a 256 -c` instead of `sha256sum -c`.

## Using Sandboxes from the Command Line

Every `sandbox` function supports [command line integration](using-mariadb-shell/command-line-integration.md), so you can manage sandboxes from scripts and CI jobs. Options become `--name=value` arguments in camelCase or kebab-case:

```sh
mariadb-shell -- sandbox deploy 3313 --password=sandbox-root-pw --sandbox-dir=/tmp/ci-sandboxes --ssl=false
mariadb-shell root:sandbox-root-pw@localhost:3313 --sql -e "CREATE DATABASE shop"
mariadb-shell -- sandbox get-path 3313 error --sandbox-dir=/tmp/ci-sandboxes
mariadb-shell -- sandbox stop 3313 --sandbox-dir=/tmp/ci-sandboxes
mariadb-shell -- sandbox delete 3313 --sandbox-dir=/tmp/ci-sandboxes
```

A failed operation prints the reason and returns a non-zero exit code:

```text
$ mariadb-shell -- sandbox deploy 80 --password=x
ERROR: Error: Shell Error: Invalid 'port' value 80: it must be >= 1024 and <= 65535.
```
