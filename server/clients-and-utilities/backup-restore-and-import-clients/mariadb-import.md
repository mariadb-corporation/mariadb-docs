---
description: >-
  Complete mariadb-import reference: load tables from text files,
  --fields-terminated-by delimiter, --local file option, and --parallel/-j
  processing.
---

# mariadb-import

`mariadb-import` loads tables from text files in various formats.

{% hint style="info" %}
Previously, the client was called `mysqlimport`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

`mariadb-import` loads tables from text files in various formats. The base name of the text file must be the name of the table that should be used. If one uses sockets to connect to the MariaDB server, the server will open and read the text file directly. In other cases the client will open the text file. The SQL statement [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) is used to import the rows.

## Usage

The command to use `mariadb-import` and the general syntax is:

```bash
mariadb-import [OPTIONS] database textfile1 [textfile2 ...]
```

## Options

`mariadb-import` supports the following options:

#### `--character-sets-dir`=_directory_

_Directory_ for character set files.

#### `-c` _cols_, `--columns`=_cols_

Use only these columns to import the data to. Give the column names in a comma separated list. This is same as giving columns to [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md).

#### `-C`, `--compress`

Use compression in server/client protocol.

#### `--database`=_database_

Restore the specified database, ignoring others.To specify more than one database to include, use the directive multiple times, once for each database. Only takes effect when used together with the `--dir` option. This option is available from MariaDB 11.6.

#### `--debug`\[=options]

Output debug log. Often this is `d:t:o,filename`. The default is `d:t:o`.

#### `--debug-check`

Check memory and open file usage at exit.

#### `--debug-info`

Print some debug info at exit.

#### `--default-auth`=_plugin_

Default authentication client-side _plugin_ to use.

#### `--default-character-set`=_character-set_

Set the default [_character set_](../../reference/data-types/string-data-types/character-sets/).

#### `--defaults-extra-file`=_file_

Read this _file_ after the global files are read. Must be given as the first option.

#### `--defaults-file`=_file_

Only read default options from the given _file_ name Must be given as the first option.

#### `--defaults-group-suffix`=_group-suffix_

In addition to the given groups, also read groups with this _suffix_.

#### `-d`, `--delete`

First delete all rows from table.

#### `--dir`=_directory_

Restore all tables from backup directory created using [mariadb-dump --dir](mariadb-dump.md). This option is available from MariaDB 11.6.

#### `--fields-terminated-by`=_string_

Fields in the input file are terminated by the given _string_.

#### `--fields-enclosed-by`=_character_

Fields in the import file are enclosed by the given _character_.

#### `--fields-optionally-enclosed-by`=_character_

Fields in the input file are optionally enclosed by the given _character_.

#### `--fields-escaped-by`=_character_

Fields in the input file are escaped by the given _character_.

#### `-f`, `--force`

Continue even if we get an SQL error.

#### `-?`, `--help`

Display this help and exits.

#### `-h` _host_, `--host`=_host_

Connect to host.

#### `-i`, `--ignore`

If duplicate unique key was found, keep old row.

#### `-k`, `--ignore-foreign-keys`

Disable foreign key checks while importing the data.

#### `--ignore-database`=_database_

Do not restore the specified database. To specify more than one database to ignore, use the directive multiple times, once for each database. Only takes effect when used together with the `--dir` option. This option is available from MariaDB 11.6.

#### `--ignore-lines`=_n_

Ignore first n lines of data infile.

#### `--ignore-table`=_table_

Do not restore the specified table. To specify more than one table to ignore, use the directive multiple times, once for each table. Each table must be specified with both database and table names, for instance, `--ignore-table`=_database_._table_. Only takes effect when used together with the `--dir` option. This option is available from MariaDB 11.6.

#### `--innodb-optimize-keys`

Create secondary indexes after data load, which speeds up loading (InnoDB only). Defaults to on; use\
`--skip-innodb-optimize-keys` to disable. This option is available from MariaDB 11.8.

#### `--lines-terminated-by`=_string_

Lines in the input file are terminated by the given _string_.

#### `-L`, `--local`

Read all files through the client.

#### `-l`, `--lock-tables`

Lock all tables for write (this disables threads).

#### `--low-priority`

Use `LOW_PRIORITY` when updating the table.

#### `--no-defaults`

Don't read default options from any option file. Must be given as the first option.

#### `-j`, `--parallel`=_number_

Number of LOAD DATA jobs executed in parallel. This option is available from MariaDB 11.4.1. `--use-threads` is a synonym.

#### `-p`_password_, `--password`_password_

Password to use when connecting to server. If password is not given, it's asked from the terminal. Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line.

#### `--pipe`, `-W`

n Windows, connect to the server via a named pipe. This option applies only if the server supports named-pipe connections.

#### `--plugin-dir`

Directory for client-side plugins.

#### `-P` _port-number_, `--port`=_port-number_

_Port number_ to use for connection or `0` for default to, in order of preference, `my.cnf`, the `MYSQL_TCP_PORT` [environment variable](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-environment-variables.md), `/etc/services`. Default is `3306`.

#### `--print-defaults`

Print the program argument list and exit. Must be given as the first option.

#### `--protocol`=_protocol_

The _protocol_ to use for connection (`tcp`, `socket`, `pipe`, `memory`).

#### `-r`, `--replace`

If duplicate unique key was found, replace old row.

#### `--shared-memory-base-name`

Shared-memory name to use for Windows connections using shared memory to a local server (started with the `--shared-memory` option). Case sensitive.

#### `-s`, `--silent`

Silent mode. Produce output only when errors occur.

#### `-S`, `--socket`={_socket|named-pipe}_

For connections to localhost, the Unix _socket_ file to use, or, on Windows, the name of the _named pipe_ to use.

#### `--ssl`

Enables [TLS](../../security/encryption/data-in-transit-encryption/). TLS is also enabled even without setting this option when certain other TLS options are set. The `--ssl` option does not enable [verifying the server certificate](../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the `--ssl-verify-server-cert` option.

#### `--ssl-ca`=_pem-file_

Define a path to a _PEM file_ that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option implies the `--ssl` option.

#### `--ssl-capath`=_pem-directory_

Define a _path to a directory that contains one or more PEM files_ that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option is only supported if the client was built with OpenSSL or yaSSL. If the client was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. This option implies the `--ssl` option. |

#### `--ssl-cert`=_file_

Define a path to the X509 _certificate file_ to use for [TLS](../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

#### `--ssl-cipher`=_cipher-list_

_List of permitted ciphers_ or cipher suites to use for [TLS](../../security/encryption/data-in-transit-encryption/). This option implies the `--ssl` option.

#### `--ssl-crl`=_pem-file_

Defines a path to a _PEM file_ that should contain one or more revoked X509 certificates to use for [TLS](../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL or Schannel. If the client was built with yaSSL or GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

#### `--ssl-crlpath`=_pem-directory_

Define a _path to a directory that contains one or more PEM files_ that should each contain one revoked X509 certificate to use for [TLS](../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL. If the client was built with yaSSL, GnuTLS, or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

#### `--ssl-key`=_key-file_

Define a path to a private _key file_ to use for [TLS](../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

#### `--ssl-verify-server-cert`

Enable [server certificate verification](../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default.

#### `--table`=_table_

Restore the specified _table_ ignoring others. Use `--table`=dbname.tablename with this option. To specify more than one table to include, use the directive multiple times, once for each table. Only takes effect when used together with the `--dir` option. This option is available from MariaDB 11.6.

#### `--tls-version`=_tls-list_

This option accepts a _comma-separated list of TLS protocol versions_. A TLS protocol version will only be enabled if it is present in this list. All other TLS protocol versions will not be permitted. See [Secure Connections Overview: TLS Protocol Versions](../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#tls-protocol-versions) for more information.

#### `--use-threads`=_number_

Load files in parallel. The argument is the _number of threads_ to use for loading data. From [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes), a synonym for -j, `--parallel`=num.

#### `-u` _username_, `--user`=_username_

_User_ for login if not current user.

#### `-v`, `--verbose`

Print info about the various stages.

#### `-V`, `--version`

Output version information and exit.

### Option Files

In addition to reading options from the command line, `mariadb-import` can also read options from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-import` in an option file, then it is ignored.

The following options relate to how MariaDB command line tools handles option files. They must be given as the first argument on the command line:

| Option                    | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `--print-defaults`        | Print the program argument list and exit.        |
| `--no-defaults`           | Don't read default options from any option file. |
| `--defaults-file`=#       | Only read default options from the given file #. |
| `--defaults-extra-file`=# | Read this file after the global files are read.  |

`mariadb-import` is linked with MariaDB Connector/C. Therefore, it may be helpful to see [Configuring MariaDB Connector/C with Option Files](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/configuring-mariadb-connectorc-with-option-files) for more information on how MariaDB Connector/C handles option files.

### Option Groups

`mariadb-import` reads options from the following [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group             | Description                                                                                                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysqlimport]    | Options read by mysqlimport, which includes both MariaDB Server and MySQL Server.                                                                                               |
| \[mariadb-import] | Options read by mysqlimport.                                                                                                                                                    |
| \[client]         | Options read by all MariaDB and MySQL client programs, which includes both MariaDB and MySQL clients. For example, mysqldump.                                                   |
| \[client-server]  | Options read by all MariaDB [client programs](../) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[client-mariadb] | Options read by all MariaDB client programs.                                                                                                                                    |

## Default Values

| Variables                     | Value (after reading options) |
| ----------------------------- | ----------------------------- |
| character-sets-dir            | (No default value)            |
| default-character-set         | latin1                        |
| columns                       | (No default value)            |
| compress                      | FALSE                         |
| debug-check                   | FALSE                         |
| debug-info                    | FALSE                         |
| delete                        | FALSE                         |
| fields-terminated-by          | (No default value)            |
| fields-enclosed-by            | (No default value)            |
| fields-optionally-enclosed-by | (No default value)            |
| fields-escaped-by             | (No default value)            |
| force                         | FALSE                         |
| host                          | (No default value)            |
| ignore                        | FALSE                         |
| ignore-lines                  | 0                             |
| lines-terminated-by           | (No default value)            |
| local                         | FALSE                         |
| lock-tables                   | FALSE                         |
| low-priority                  | FALSE                         |
| port                          | 3306                          |
| replace                       | FALSE                         |
| silent                        | FALSE                         |
| socket                        | /var/run/mysqld/mysqld.sock   |
| ssl                           | FALSE                         |
| ssl-ca                        | (No default value)            |
| ssl-capath                    | (No default value)            |
| ssl-cert                      | (No default value)            |
| ssl-cipher                    | (No default value)            |
| ssl-key                       | (No default value)            |
| ssl-verify-server-cert        | FALSE                         |
| use-threads                   | 0                             |
| user                          | (No default value)            |
| verbose                       | FALSE                         |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
