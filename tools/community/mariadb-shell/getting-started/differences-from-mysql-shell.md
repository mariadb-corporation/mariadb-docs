---
description: >-
  What MariaDB Shell leaves out of MySQL Shell, what it adds, and which names
  and paths changed.
---

# Differences from MySQL Shell

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

MariaDB Shell is derived from MySQL Shell. The interactive console, the SQL and Python modes, the `shell`, `mysql`, and `util` APIs, and most command-line options work the same way. This page lists every area where MariaDB Shell differs, so that you can adapt existing MySQL Shell scripts and habits.

{% hint style="info" %}
The rest of this documentation describes only what MariaDB Shell provides. This page is the only place that names MySQL Shell features that are not available.
{% endhint %}

## Features Not Available

The following MySQL Shell features depend on MySQL-only server functionality or client libraries. They are not compiled into MariaDB Shell: their global objects, functions, and command-line options don't exist, and the shell reports an unknown option or name if you use them.

| Feature | Reason |
| --- | --- |
| JavaScript mode (`--js`, `\js`) and the GraalVM runtime | The JavaScript engine is not shipped. Python is the only scripting language. |
| X Protocol and X DevAPI: `mysqlx://` URIs, the `mysqlx` module, X sessions, collections and the document store, port 33060, and the `--mx`, `--mysqlx`, and `--sqlx` options | MariaDB Server does not implement the X Protocol. All sessions use the classic protocol. |
| `util.importJson` | Relies on the X DevAPI document store. |
| AdminAPI: the `dba` global object, InnoDB Cluster, ClusterSet, ReplicaSet, read replicas, routing guidelines, MySQL Router integration, and AdminAPI sandbox functions such as `dba.deploySandboxInstance` | Built on MySQL Group Replication and the MySQL metadata schema. For local test servers, use the [`sandbox`](../sandbox-instances.md) global object instead. |
| Upgrade Checker (`util.checkForServerUpgrade`) | Encodes MySQL Server upgrade rules. |
| Binary log utilities (`util.dumpBinlogs`, `util.loadBinlogs`) | Built on the MySQL binary log client API and event library. |
| `util.upgradeAuthMethod` | Migrates accounts away from `mysql_native_password`, which remains the default and is not deprecated in MariaDB Server. |
| The `random`, `dual`, and `discardOld` options of `util.change_password` | Use MySQL 8.0 account statements that MariaDB Server does not have. See [Password Change Utility](../utilities/password-change-utility.md). |
| MySQL REST Service management | Specific to MySQL Router. |
| `--register-factor` and FIDO/WebAuthn authentication | Use a MySQL authentication plugin. |
| The client authentication plugins that MySQL Shell bundles: Kerberos (`authentication_kerberos_client`), LDAP SASL (`authentication_ldap_sasl_client`), OCI IAM (`authentication_oci_client`), and OpenID Connect (`authentication_openid_connect_client`), and the options that configure them | They implement MySQL Server authentication methods. MariaDB Shell authenticates through MariaDB Connector/C, and the only plugin file it ships in `lib/mariadb/plugins` is `caching_sha2_password`. |
| The `--where` option of the built-in `threads` report | Relies on the X DevAPI expression parser. The option is accepted but raises a "not supported in this build" error. |

### Dump and Load Options for MySQL HeatWave Service

The dump utilities refuse the `ocimds` and `compatibility` options when the source server is MariaDB, because they rewrite DDL and accounts for MySQL HeatWave Service. Features that only apply to MySQL sources, such as invisible primary key generation, JavaScript stored programs, data masking, `BULK LOAD`, histograms, and Lakehouse targets, are not applied to MariaDB dumps. See [Limitations](../utilities/dump-and-load/limitations.md).

### Connector Differences

MariaDB Connector/C replaces the MySQL client library, and some MySQL 8.0 client features have no equivalent:

* `--ssl-mode=REQUIRED` cannot be strictly enforced with every Connector/C version. When it cannot, the shell warns at connection time. See [Encrypted Connections](../connecting/encrypted-connections.md).
* Query attributes, second and third authentication factors, compression algorithm selection, TLS 1.3 cipher suite selection, and server public key retrieval are not supported. If you set them, the shell ignores them and prints a warning.

## New in MariaDB Shell

| Feature | Description |
| --- | --- |
| `mariadb://` URI scheme | The default scheme for connection URIs. `mysql://` is accepted as a synonym. See [Connection URIs and Options](../connecting/connection-uris-and-options.md). |
| `mariadb+ssh://` URIs | Describe an SSH tunnel and the database connection in a single URI. See [SSH Tunnels](../connecting/ssh-tunnels.md). |
| `sandbox` global object | Deploys and manages local MariaDB and MySQL test servers, detecting the vendor from the server binary. See [Sandbox Instances](../sandbox-instances.md). |
| `server_vendor` session property | `session.server_vendor` returns `MariaDB` or `MySQL`. See [Sessions](sessions.md). |
| `%vendor%` prompt variable and Nerd Fonts themes | Prompts show the vendor of the connected server. Two additional sample themes use Nerd Fonts symbols. See [Prompt](../customizing/prompt.md). |
| `login-path` credential helper | The default credential store helper on Linux. It stores passwords in the obfuscated `~/.mylogin.cnf` login file and is also available on macOS. See [Credential Store](../connecting/credential-store.md). |
| MariaDB objects in dump and load | Sequences, Oracle-mode packages, system-versioned tables, `UUID`, `INET4`, and `INET6` columns, MariaDB roles, a consistent snapshot taken with `BACKUP STAGE`, and the MariaDB GTID position. See [MariaDB-Specific Features](../utilities/dump-and-load/mariadb-specific-features.md). |
| Vendor rules for dump and load | A dump records the vendor of its source. Loading a dump into a server of another vendor is refused before any DDL runs, and the copy utilities refuse to copy between vendors. |
| Script-based installation | `install.sh` and `install.ps1` install the right package for your platform from a GitHub release. See [Installation](../installation/). |
| Default mode | Without `--py` or a `defaultMode` setting, the shell starts in SQL mode. |
| Slash prefix for shell commands | Shell commands also run with a `/` in place of the `\`, such as `/quit` or `/status`. The `slashCommands` option turns it off. See [Shell Commands](../using-mariadb-shell/shell-commands.md#the-slash-prefix). |

## Renamed Items

| MySQL Shell | MariaDB Shell | Notes |
| --- | --- | --- |
| `mysqlsh` executable | `mariadb-shell`, with the alias `msh` | No `mysqlsh` alias is installed, so update scripts that call the old name. |
| `MYSQLSH_*` environment variables | `MARIADB_SHELL_*` | The `MYSQLSH_` name is still read when the `MARIADB_SHELL_` name is not set. See [Files and Environment Variables](../files-and-environment-variables.md). |
| `~/.mysqlsh` | `~/.mariadb-shell` | On Windows, `%AppData%\MariaDB\mariadb-shell`. Settings are not migrated from a MySQL Shell configuration directory. |
| `mysqlsh.log` | `mariadb-shell.log` | |
| `mysqlshrc.py` | `mariadb-shellrc.py` | See [Startup Scripts](../customizing/startup-scripts.md). |
| `[mysqlsh]` option group | `[mariadb-shell]` | The shell reads `[mariadb-shell]`, `[mysqlsh]`, and `[client]`. See [Option Files and Login Paths](../connecting/option-files-and-login-paths.md). |
| `~/mysql-sandboxes` | `~/.mariadb-shell/sandboxes` | On Windows, `%USERPROFILE%\MariaDB\mariadb-shell\sandboxes`. |
| `mysql-secret-store-*` helper executables | `mariadb-secret-store-*` | The `credentialStore.helper` values (`login-path`, `keychain`, `windows-credential`, `secret-service`) are unchanged. |
| `lib/mysql/plugins` (client authentication plugins) | `lib/mariadb/plugins` | The `mysqlPluginDir` option and `--mysql-plugin-dir` keep their names. |
| `mysql-shell-plugins-manifest.json` (plugin repository manifest) | `mariadb-shell-plugins-manifest.json` | `plugins.repositories.add()` looks only for the new name, and a `github/<user>` repository defaults to `mariadb-shell-plugins`, so MySQL Shell plugin repositories are not found. See [Plugins](../extending-mariadb-shell/plugins.md). |

The Python module that plugins and scripts import from is still named `mysqlsh` (for example, `from mysqlsh import globals`), so existing Python plugins keep working.

## Coexistence with MySQL Shell

Every file that MariaDB Shell installs uses a MariaDB-specific name or path, and its configuration lives in its own directory. You can install MariaDB Shell and MySQL Shell on the same system and use them side by side.

<sub>_This page is licensed: GPLv2_</sub>
