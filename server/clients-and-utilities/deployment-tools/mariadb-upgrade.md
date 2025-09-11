# mariadb-upgrade

`mariadb-upgrade` is a tool that checks and updates your tables to the latest version.

{% hint style="info" %}
Previously, the client was called `mysql_upgrade`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

## Overview

You should run `mariadb-upgrade` after upgrading from one major MySQL/MariaDB release to another, such as from MySQL 5.0 or MariaDB 10.4 to MariaDB 10.5. You also have to use `mariadb-upgrade` after a direct "horizontal" migration, for example from MySQL 5.5.40 to MariaDB 5.5.40. It's also safe to run `mariadb-upgrade` for minor upgrades, as, if there are no incompatibilities, nothing is changed.

{% tabs %}
{% tab title="Current" %}
`mariadb-upgrade` needs to be run as a user with write access to the data directory.

Starting from [mariadb-upgrade 2.0](mariadb-upgrade.md#mariadb-upgrade-2.0), the user running the upgrade tool must have write access to `datadir/mysql_upgrade_info`, so that the tool can write the current MariaDB version into the file.&#x20;
{% endtab %}

{% tab title="< 10.7.2 / 10.6.6 / 10.5.14" %}
`mariadb-upgrade` needs to be run as a user with write access to the data directory.
{% endtab %}
{% endtabs %}

`mariadb-upgrade` is run after starting the new MariaDB server. Running it before you shut down the old version will not hurt anything and will allow you to make sure it works and figure out authentication for it ahead of time.

{% hint style="success" %}
It is recommended to make a [backup](../../server-usage/backup-and-restore/) of all databases before running `mariadb-upgrade`.
{% endhint %}

In most cases, `mariadb-upgrade` should just take a few seconds. The main work of `mariadb-upgrade` is to:

* Update the system tables in the `mysql` database to the latest version (normally just add new fields to a few tables).
* Check that all tables are up to date (runs [CHECK TABLE table\_name FOR UPGRADE](../../reference/sql-statements/table-statements/check-table.md)). For tables that are not up to date, runs [ALTER TABLE table\_name FORCE](../../reference/sql-statements/data-definition/alter/alter-table/) on the table to update it. A table is not up to date in the following cases:
  * The table uses an index for which there has been a [collation](../../reference/data-types/string-data-types/character-sets/) change (rare).
  * A format change in the storage engine requires an update (very rare).

## Why run mariadb-upgrade?

If you skip running `mariadb-upgrade`, issues can arise, including these:

* Errors in the [error log](../../server-management/server-monitoring-logs/error-log.md) that some system tables don't have all needed columns.
* Updates or searches may not find the record they are attempting to update or search for.
* [CHECKSUM TABLE](../../reference/sql-statements/table-statements/checksum-table.md) may report the wrong checksum for [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/) or [Aria](../../server-usage/storage-engines/aria/) tables.
* The error message "Cannot load from mysql.proc. The table is probably corrupted."

To fix issues like this, run `mariadb-upgrade`, [mariadb-check](../table-tools/mariadb-check.md), [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md) and, if needed, [REPAIR TABLE](../../reference/sql-statements/table-statements/repair-table.md) on the faulty table.

## Upgrading to a Minor Version, or to Enterprise Server

Starting from [mariadb-upgrade 2.0](mariadb-upgrade.md#mariadb-upgrade-2.0), mysql-upgrade doesn't run when upgrading to a new minor version (for instance, from MariaDB 10.6.3 to 10.6.4).

{% hint style="warning" %}
This includes updating from Community Server to Enterprise Server.
{% endhint %}

In those cases, mariadb-upgrade terminates with a message like this:

```
This installation of MariaDB is already upgraded to 10.11.4-MariaDB.
There is no need to run mysql_upgrade again for 10.11.11-MariaDB.
You can use --force if you still want to run mysql_upgrade.
```

As the message indicates, use the [--force](mariadb-upgrade.md#f-force) option to override this behavior.

{% hint style="warning" %}
When upgrading from, say, Community Server 10.11.4 to Enterprise Server 10.11.11, mariadb-upgrade considers that a minor-version upgrade, so you must use the `--force` option to make it run.
{% endhint %}

## Usage

```bash
mariadb-upgrade [--force] [--user=# --password=# 
  --host=hostname --port=# --socket=#
  --protocol=tcp|socket|pipe|memory 
  --verbose] [OTHER_OPTIONS]
```

`mariadb-upgrade` is mainly a framework to call [mariadb-check](../table-tools/mariadb-check.md). `mariadb-upgrade` works by doing the following operations:

```bash
# Find out path to datadir
echo "show variables like 'datadir'" | mysql
mariadb-check --no-defaults --check-upgrade --auto-repair --databases mysql
mysql_fix_privilege_tables
mariadb-check --no-defaults --all-databases --fix-db-names --fix-table-names
mariadb-check --no-defaults --check-upgrade --all-databases --auto-repair
```

The connect options given to `mariadb-upgrade` are passed along to [mariadb-check](../table-tools/mariadb-check.md) and [mariadb command-line client](../mariadb-client/mariadb-command-line-client.md).

The `mysql_fix_privilege_tables` script is not called; it's included as part of `mariadb-upgrade` .

If you have a problem with `mariadb-upgrade`, try running it in very verbose mode:

```bash
mariadb-upgrade --verbose --verbose other-options
```

`mariadb-upgrade` also saves the MariaDB version number in a file named `mysql_upgrade_info` in the [data directory](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir). This is used to quickly check whether all tables have been checked for this release so that table-checking can be skipped. For this reason,`mariadb-upgrade` needs to be run as a user with write access to the data directory. To ignore this file and perform the check regardless, use the `--force` option.

## Options

`mariadb-upgrade` supports the following options:

#### -?, --help

Display this help message and exit.

#### --basedir=_path_

Old option accepted for backward compatibility but ignored.

#### --character-sets-dir=_path_

Old option accepted for backward compatibility but ignored.

#### --check-if-upgrade-is-needed

Do a quick check if upgrade is needed. Returns `0` if an upgrade is needed, `1` if not. Available from [mariadb-upgrade 2.0](mariadb-upgrade.md#mariadb-upgrade-2.0).

#### --compress=_name_

Old option accepted for backward compatibility but ignored.

#### --datadir=_name_

Old option accepted for backward compatibility but ignored.

#### --debug-check

Check memory and open file usage at exit.

#### -T, --debug-info

Print some debug info at exit.

#### --default-character-set=_name_

Old option accepted for backward compatibility but ignored.

#### -f, --force

Force execution of mariadb-check even if mariadb-upgrade has already been executed for the current version of MariaDB. Ignores `mysql_upgrade_info`.

#### -h, --host=_host_

Connect to MariaDB on the given _host_.

#### -p, --password=_password_

_Password_ to use when connecting to server. If password is not given, it's solicited on the command line (which should be considered insecure). You can use an option file to avoid giving the password on the command line.

#### -P, --port=_port-number_

_Port number_ to use for connection or 0 for default to, in order of preference, my.cnf, the `MYSQL_TCP_PORT` [environment variable](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-environment-variables.md), `/etc/services`, built-in default (`3306`).

#### --protocol=_protocol_

The _protocol_ to use for connection (`tcp`, `socket`, `pipe`, `memory`).

#### --silent

Print less information.

#### -S, --socket=_file_

For connections to localhost, the Unix socket _file_ to use, or, on Windows, the name of the _named pipe_ to use.

#### --ssl

Enables [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). TLS is also enabled even without setting this option when certain other TLS options are set. The `--ssl` option does not enable [verifying the server certificate](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, you must specify the `--ssl-verify-server-cert` option.

#### --ssl-ca=_path_

Defines a _path_ to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option implies the `--ssl` option.

#### --ssl-capath=_path_

Defines a _path_ to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option is only supported if the client was built with OpenSSL or yaSSL. If the client was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. This option implies the `--ssl` option.

#### --ssl-cert=_path_

Defines a _path_ to the X509 certificate file to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

#### --ssl-cipher=_ciphers_

_List of permitted ciphers_ or cipher suites to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option implies the `--ssl` option.

#### --ssl-crl=_path_

Defines a _path_ to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL or Schannel. If the client was built with yaSSL or GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

#### --ssl-crlpath=_path_

Defines a _path_ to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL. If the client was built with yaSSL, GnuTLS, or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

#### --ssl-key=_file_

Defines a path to a _private key file_ to use for [TLS](../../security/securing-mariadb/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

#### --ssl-verify-server-cert

Enables [server certificate verification](../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default.

#### -t, --tmpdir=_directory_

_Directory_ for temporary files.

#### -s, --upgrade-system-tables

Only upgrade the system tables in the mysql database. Tables in other databases are not checked or touched.

#### -u, --user=name

User for login if not current user.

#### -v, --verbose

Display more output about the process, using it twice will print connection arguments; using it 3 times will print out all [CHECK](../../reference/sql-statements/table-statements/check-table.md), [RENAME](../../reference/sql-statements/data-definition/rename-table.md) and [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) commands used during the check phase; using it 4 times will also write out all [mariadb-check](../table-tools/mariadb-check.md) commands used.

#### -V, --version

Output version information and exit.

#### -k, --version-check

Run this program only if its 'server version' matches the version of the server to which it's connecting check. Note: the 'server version' of the program is the version of the MariaDB server with which it was built/distributed. (Defaults to on; use `--skip-version-check` to disable.)

#### --write-binlog

{% tabs %}
{% tab title="Current" %}
All commands, including those run by [mariadb-check](../table-tools/mariadb-check.md), are written to the [binary log](../../server-management/server-monitoring-logs/binary-log/). Disabled by default.
{% endtab %}

{% tab title="< 10.0.6" %}
All commands, including those run by [mariadb-check](../table-tools/mariadb-check.md), are written to the [binary log](../../server-management/server-monitoring-logs/binary-log/). Enabled by default. The `--skip-write-binlog` option must be used when commands should not be sent to replication replicas.
{% endtab %}
{% endtabs %}

### Option Files

In addition to reading options from the command line, `mariadb-upgrade` can also read options from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-upgrade` in an option file, then it is ignored.

The following options relate to how MariaDB command line tools handles option files. They must be given as the first argument on the command line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

`mariadb-upgrade` is linked with [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/mariadb-connector-c-guide). However, MariaDB Connector/C does not handle the parsing of option files for `mariadb-upgrade`. That is still performed by the server option file parsing code. See [MDEV-19035](https://jira.mariadb.org/browse/MDEV-19035) for more information.

### Option Groups

`mariadb-upgrade` reads options from the following [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group              | Description                                                                                                                                                                                                           |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysql\_upgrade]  | Options read by mariadb-upgrade, which includes both MariaDB Server and MySQL Server.                                                                                                                                 |
| \[mariadb-upgrade] | Options read by mariadb-upgrade. Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes). |
| \[client]          | Options read by all MariaDB and MySQL client programs, which includes both MariaDB and MySQL clients. For example, mysqldump.                                                                                         |
| \[client-server]   | Options read by all MariaDB [client programs](../) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients.                                       |
| \[client-mariadb]  | Options read by all MariaDB client programs.                                                                                                                                                                          |

## Differences Between mysql\_upgrade in MariaDB and MySQL

* MariaDB converts long [table names](../../reference/sql-structure/sql-language-structure/identifier-names.md) properly.
* MariaDB converts [InnoDB](../../server-usage/storage-engines/innodb/) tables (no need to do a dump/restore or [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/)).
* MariaDB converts old archive tables to the new 5.1 format.
* `mysql_upgrade --verbose` runs `mariadb-check --verbose`, so that you get more information of what is happening. Running with 3 times --verbose prints out all `CHECK`, `RENAME` and `ALTER TABLE` statements executed.
* The [mysql.event table](../../reference/system-tables/the-mysql-database-tables/mysql-event-table.md) is upgraded live. There is no need to restart the server to use events if the event table has changed.
* More descriptive output.

## Speeding up mariadb-upgrade

* If you are sure that all your tables are up to date with the current version, then you can run `mariadb-upgrade ---upgrade-system-tables`, which will only fix your system tables in the mysql database to be compatible with the latest version.

The main reason to run `mariadb-upgrade` on all your tables is to allow it to check that:

* There has not been any change in table formats between versions.
* This has not happened since MariaDB 5.1.
* If some of the tables are using an index for which we have changed sort order.
* This has not happened since MariaDB 5.5.

{% hint style="warning" %}
If you are sure this applies to your situation, you can just run `mariadb-upgrade` with the `---upgrade-system-tables` option.
{% endhint %}

## Other Uses

* `mariadb-upgrade` recreates any missing tables in the [mysql database](../../reference/system-tables/the-mysql-database-tables/). It doesn't touch any data in existing tables.

## mariadb-upgrade 2.0

{% hint style="info" %}
`mariadb-upgrate/mysql_upgrade 2.0` was introduced in MariaDB 10.5.14 / 10.6.6 / 10.7.2.
{% endhint %}

Previously, the tool first ran the upgrade process and then created the `datadir/mysql_upgrade_info` file. If the file could not be created because of permissions (`mariadb-upgrade` did not have rights to create the file), `mariadb-upgrad` gave an error, but this was often ignored. One effect of not being able to create the `mysql_upgrade_info` file was that every new `mariadb-upgrade` run would have to do a full upgrade check, which can take a while if there are a lot of tables.

`mariadb-upgrade` 2.0 fixes the following issues:

* The `datadir/mysql_upgrade_info` is now created at the start of the upgrade process and locked. This ensures that two `mariadb-upgrade` processes cannot be run in parallel, which can cause deadlocks ([MDEV-27068](https://jira.mariadb.org/browse/MDEV-27068)). One side effect of this is that `mariadb-upgrade` has to have write access to `datadir`, which means it has to be run as the user that installed MariaDB, normally 'mysql' or 'root' .
* One can use `mariadb-upgrade --force --force` to force the upgrade to be run, even if there was no version change or if one doesn't have write access to `datadir`. Note that if this option is used, the next `mariadb-upgrade` run will assume that there is a major version change and the upgrade must be done (again).
* The upgrade is done only if there is a major server version change (for instance, from MariaDB 10.5 to 10.6). This avoids unnecessary upgrades.
* New option added: `--check-if-upgrade-is-needed`. If this is used, `mariadb-upgrade` will return `0` if there has been a major version change and you should run `mariadb-upgrade`. If not upgrade is needed, `1` is returned.
* `--verbose` writes more information, including from which version to which version the upgrade is done.
* Better messages when there is no need to run `mariadb-upgrade`.

## See Also

* [mariadb-check](../table-tools/mariadb-check.md)
* [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md)
* [REPAIR TABLE](../../reference/sql-statements/table-statements/repair-table.md)
* [Downgrading between Major Versions of MariaDB](../../server-management/install-and-upgrade-mariadb/downgrading-between-major-versions-of-mariadb.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
