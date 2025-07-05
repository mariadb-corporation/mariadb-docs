# Configuring MariaDB Connector/C with Option Files

Just like MariaDB Server and libmysqlclient, MariaDB Connector/C can also read configuration options from client [option groups](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in [option files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files).

### Default Option File Locations

MariaDB Connector/C reads option files from many different directories by default. See the sections below to find out which directories are checked for which system.

MariaDB Connector/C allows application developers to read options from the default option files by calling the [mysql_optionsv](mariadb-connectorc-api-functions/mysql_optionsv.md) function and providing the [MYSQL_READ_DEFAULT_FILE](mariadb-connectorc-api-functions/mysql_optionsv.md#options) option name and a `NULL` pointer as arguments. For example:

```c
mysql_optionsv(mysql, MYSQL_READ_DEFAULT_FILE, NULL);
```

#### Default Option File Locations on Linux, Unix, Mac

On Linux, Unix, or Mac OS X, the default option file is called `my.cnf`. MariaDB Connector/C looks for the MariaDB option file in the locations and orders listed below.

The locations are dependent on whether the `DEFAULT_SYSCONFDIR` [cmake](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/compiling-mariadb-from-source/generic-build-instructions#using-cmake) option was defined when MariaDB Connector/C was built. This option is usually defined as `/etc` when building [RPM packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/rpm), but it is usually not defined when building [DEB packages](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-deb-files) or [binary tarballs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/installing-mariadb-binary-tarballs).

* When the `DEFAULT_SYSCONFDIR` [cmake](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/compiling-mariadb-from-source/generic-build-instructions#using-cmake) option was not defined, MariaDB Connector/C looks for the MariaDB option file in the following locations in the following order:

| Location            |
| ------------------- |
| Location            |
| /etc/my.cnf         |
| /etc/mysql/my.cnf   |
| $MYSQL\_HOME/my.cnf |
| \~/.my.cnf          |

* When the `DEFAULT_SYSCONFDIR` [cmake](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/compiling-mariadb-from-source/generic-build-instructions#using-cmake) option was defined, MariaDB Connector/C looks for the MariaDB option file in the following locations in the following order:

| Location                   |
| -------------------------- |
| Location                   |
| DEFAULT\_SYSCONFDIR/my.cnf |
| $MYSQL\_HOME/my.cnf        |
| \~/.my.cnf                 |

#### Default Option File Locations on Windows

On Windows, the default option file can be called either `my.ini` or `my.cnf`. MariaDB Connector/C looks for the MariaDB option file in the following locations in the following order:

| Location                        |
| ------------------------------- |
| Location                        |
| System Windows Directory\my.ini |
| System Windows Directory\my.cnf |
| Windows Directory\my.ini        |
| Windows Directory\my.cnf        |
| C:\my.ini                       |
| C:\my.cnf                       |
| EXEDIR\my.ini                   |
| EXEDIR\my.cnf                   |
| %MYSQL\_HOME%\my.ini            |
| %MYSQL\_HOME%\my.cnf            |

* The `System Windows Directory` is the directory returned by the [GetSystemWindowsDirectory](https://docs.microsoft.com/en-us/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemwindowsdirectorya) function. The value is usually `C:\Windows`. To find its specific value on your system, open [cmd.exe](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/cmd) and execute:

```bash
echo %WINDIR%
```

* The `Windows Directory` is the directory returned by the [GetWindowsDirectory](https://docs.microsoft.com/en-us/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) function. The value may be a private `Windows Directory` for the application, or it may be the same as the `System Windows Directory` returned by the [GetSystemWindowsDirectory](https://docs.microsoft.com/en-us/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemwindowsdirectorya) function.
* `EXEDIR` is the parent directory of the executable program that MariaDB Connector/C is linked with.
* `MYSQL_HOME` is the [environment variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-environment-variables) containing the path to the directory holding the server-specific `my.cnf` file.

#### Default Option File Hierarchy

MariaDB Connector/C will look in all of the above locations, in order, even if has already found an option file, and it's possible for more than one option file to exist. For example, you could have an option file in `/etc/my.cnf` with global settings for all servers, and then you could another option file in `~/.my.cnf` (i.e.your user account's home directory) which will specify additional settings (or override previously specified setting) that are specific only to that user.

### Custom Option File Locations

MariaDB Connector/C allows application developers to read option files from a custom option file by calling the [mysql_optionsv](mariadb-connectorc-api-functions/mysql_optionsv.md) function and providing the [MYSQL_READ_DEFAULT_FILE](mariadb-connectorc-api-functions/mysql_optionsv.md#options) option name and an option file path as arguments. For example:

```c
mysql_optionsv(mysql, MYSQL_READ_DEFAULT_FILE, (void *)"./my_conf.cnf");
```

Many MariaDB clients can be configured to read options from custom options files with the following command-line arguments. They must be given as the first argument on the command-line. Application developers who use MariaDB Connector/C in their application and rely on option files may also want to consider implementing these command-line arguments:

| Option                                                                                                                                         | Description                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| Option                                                                                                                                         | Description                                                        |
| [--defaults-file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options) =path       | Only read options from the given option file.                      |
| [--defaults-extra-file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options) =path | Read this extra option file after all other option files are read. |

The [--defaults-file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options) command-line option is roughly equivalent to setting the [MYSQL_READ_DEFAULT_FILE](mariadb-connectorc-api-functions/mysql_optionsv.md#options) option with a non-NULL argument.

The [--defaults-extra-file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options) command-line option does not yet have an equivalent option in MariaDB Connector/C. See [CONC-399](https://jira.mariadb.org/browse/CONC-399) for more information.

### Option File Syntax

The syntax of the MariaDB option files are:

* Lines starting with

## are comments.

* Empty lines are ignored.
* Option groups use the syntax `[group-name]`. See the [Option Groups](configuring-mariadb-connectorc-with-option-files.md#option-groups) section below for more information on available option groups.
* The same option group can appear multiple times.
* The `!include` directive can be used to include other option files. See the [Including Option Files](configuring-mariadb-connectorc-with-option-files.md#including-option-files) section below for more information on this syntax.
* Unlike with the server, the `!includedir` directive does not include all `.cnf` files (and potentially `.ini` files) in a given directory. Instead, it reads the `my.cnf` and (potentially the `my.ini`) in the given directory. See [CONC-396](https://jira.mariadb.org/browse/CONC-396) for more information. See the [Including Option File Directories](configuring-mariadb-connectorc-with-option-files.md#including-option-file-directories) section below for more information on this syntax.
* Dashes (`-`) and underscores (`_`) in options are interchangeable in MariaDB Connector C 3.1.1 and later. In versions before that, options must be specified exactly as they are defined. See [CONC-395](https://jira.mariadb.org/browse/CONC-395) for more information.
* MariaDB Connector/C does not support the [option prefixes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-prefixes) that are supported by MariaDB Server. See [CONC-415](https://jira.mariadb.org/browse/CONC-415) for more information.
* See the [Options](configuring-mariadb-connectorc-with-option-files.md#options) section below for information about available options.

### Option Groups

MariaDB Connector/C reads client options from the following [option groups](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in [option files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files):

| Group             | Description                                                                                                                                                                                                                                                                    |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Group             | Description                                                                                                                                                                                                                                                                    |
| \[client]         | Options read by all MariaDB and MySQL [client programs](https://github.com/mariadb-corporation/docs-connectors/blob/test/kb/en/clients-utilities/README.md), which includes both MariaDB and MySQL clients. For example, mysqldump.                                            |
| \[client-server]  | Options read by all MariaDB [client programs](https://github.com/mariadb-corporation/docs-connectors/blob/test/kb/en/clients-utilities/README.md) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[client-mariadb] | Options read by all MariaDB [client programs](https://github.com/mariadb-corporation/docs-connectors/blob/test/kb/en/clients-utilities/README.md).                                                                                                                             |

MariaDB Connector/C allows application developers to read options from these option groups by calling the [mysql_optionsv](mariadb-connectorc-api-functions/mysql_optionsv.md) function and providing the [MYSQL_READ_DEFAULT_GROUP](mariadb-connectorc-api-functions/mysql_optionsv.md#options) option name and a `NULL` pointer as arguments. For example:

```c
mysql_optionsv(mysql, MYSQL_READ_DEFAULT_GROUP, NULL);
```

#### Custom Option Groups

MariaDB Connector/C allows application developers to read options from a custom option group by calling the [mysql_optionsv](mariadb-connectorc-api-functions/mysql_optionsv.md) function and providing the [MYSQL_READ_DEFAULT_GROUP](mariadb-connectorc-api-functions/mysql_optionsv.md#options) option name and the name of the custom option group as arguments. For example:

```c
mysql_optionsv(mysql, MYSQL_READ_DEFAULT_GROUP, (void *)"my_section");
```

The custom option group will be read in addition to the default option groups listed above.

Many MariaDB clients can be configured to read options from option groups with a custom suffix by providing the following command-line argument. It must be given as the first argument on the command-line. Application developers who use MariaDB Connector/C in their application and rely on option files may also want to consider implementing this command-line argument:

| Option                                                                                                                                             | Description                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Option                                                                                                                                             | Description                                                                              |
| [--defaults-group-suffix](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options) =suffix | In addition to the default option groups, also read option groups with the given suffix. |

The [--defaults-group-suffix](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options) command-line option does not yet have an equivalent option in MariaDB Connector/C. See [CONC-404](https://jira.mariadb.org/browse/CONC-404) for more information.

### Including Option Files

It is possible to include additional option files from another option file. For example, to include `/etc/mysql/dbserver1.cnf`, an option file could contain:

```
[client-mariadb]
...
!include /etc/mysql/dbserver1.cnf
```

### Including Option File Directories

It is also possible to include the default option files in a directory from another option file. For example, to include the default option files in `/etc/my.cnf.d/`, an option file could contain:

```
[client-mariadb]
...
!includedir /etc/my.cnf.d/
```

Unlike with MariaDB server, this directive does not configure MariaDB Connector/C to include all option files ending in `.cnf` on Unix-like operating systems or all option files ending in `.cnf` and `.ini` files on Windows. Instead, it just configures MariaDB Connector/C to include the `my.cnf` in the given directory, and also the `my.ini` in the given directory if it's Windows. See [CONC-396](https://jira.mariadb.org/browse/CONC-396) for more information.

### Checking Program Options

For many MariaDB clients, you can check which options a given program is going to use by using the [--print-defaults](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options) command-line argument:

| Option                                                                                                                              | Description                                                                         |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| Option                                                                                                                              | Description                                                                         |
| [--print-defaults](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options) | Read options from option files, print all option values, and then exit the program. |

It must be given as the first argument on the command-line. Application developers who use MariaDB Connector/C in their application and rely on option files may also want to consider implementing this command-line argument. For example:

```bash
mysqldump --print-defaults
mysqldump would have been started with the following arguments:
--ssl_cert=/etc/my.cnf.d/certificates/client-cert.pem --ssl_key=/etc/my.cnf.d/certificates/client-key.pem --ssl_ca=/etc/my.cnf.d/certificates/ca.pem --ssl-verify-server-cert --max_allowed_packet=1GB
```

If it is installed on your system, then you can also check which options a given program is going to use by using the [my_print_defaults](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/my_print_defaults) utility and providing the names of the option groups that the program reads. For example:

```bash
my_print_defaults my_section client client-server client-mariadb
--ssl_cert=/etc/my.cnf.d/certificates/client-cert.pem
--ssl_key=/etc/my.cnf.d/certificates/client-key.pem
--ssl_ca=/etc/my.cnf.d/certificates/ca.pem
--ssl-verify-server-cert
--max_allowed_packet=1GB
```

See [Configuring MariaDB with Option Files: Checking Program Options](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#checking-program-options) for more information.

### MySQL 5.6 Obfuscated Authentication Credential Option File

MySQL 5.6 and above support an obfuscated authentication credential option file called `.mylogin.cnf` that is created with [mysql_config_editor](https://dev.mysql.com/doc/refman/5.6/en/mysql-config-editor.html).

MariaDB Connector/C does not support this. The passwords in MySQL's `.mylogin.cnf` are only obfuscated, rather than encrypted, so the feature does not really add much from a security perspective. It is more likely to give users a false sense of security, rather than to seriously protect them.

### Options

MariaDB Connector/C options can be set in client [option groups](configuring-mariadb-connectorc-with-option-files.md#option-groups).

Unlike with the server, dashes (`-`) and underscores (`_`) in options are **not** interchangeable for MariaDB Connector/C. Options must be specified exactly as they are defined. See [CONC-395](https://jira.mariadb.org/browse/CONC-395) for more information.

Unlike with the server, the `loose` prefix has **no** meaning for MariaDB Connector/C. Unknown options will simply be ignored.

#### Custom Options

MariaDB Connector/C allows application developers to implement custom options in option files by defining a function that matches this signature:

```c
my_bool (*set_option)(MYSQL *mysql, const char *config_option, const char *config_value);
```

And then assigning the function pointer to `mysql->options.extension->set_option`.

#### Default Options

These are the options supported in option files by MariaDB Connector/C by default.

These options can also be set inside your application with the [mysql_optionsv](mariadb-connectorc-api-functions/mysql_optionsv.md) function.

**`bind-address`**

* Description: Specify the network interface from which to connect to MariaDB Server.
* mysql\_optionsv: `MYSQL_OPT_BIND`
* Data Type: `string`
* Default Value:
* Introduced: MariaDB Connector/C 3.0.0

**`character-sets-dir`**

* Description: Directory for [character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) files.
* mysql\_optionsv: `MYSQL_SET_CHARSET_DIR`
* Data Type: `string`
* Default Value:

**`compress`**

* Description: Compress all information sent between the client and the server if both support compression.
* mysql\_optionsv: `MYSQL_OPT_COMPRESS`
* Data Type: `boolean`
* Default Value: `false`

**`connect-timeout`, `timeout`**

* Description: Connect timeout in seconds. This value will be passed as an unsigned int parameter.
* mysql\_optionsv: `MYSQL_OPT_CONNECT_TIMEOUT`
* Data Type: `int`
* Default Value:

**`database`**

* Description: Database to use.
* mysql\_optionsv: `MARIADB_OPT_SCHEMA`
* Data Type: `string`
* Default Value:

**`debug`**

* Description:
* mysql\_optionsv: `MARIADB_OPT_DEBUG`
* Data Type: `string`
* Default Value:

**`default-auth`**

* Description: Default authentication client-side plugin to use.
* mysql\_optionsv: `MYSQL_DEFAULT_AUTH`
* Data Type: `string`
* Default Value:

**`default-character-set`**

* Description: Specify the default [character set](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) for the connection.
* mysql\_optionsv: `MYSQL_SET_CHARSET_NAME`
* Data Type: `string`
* Default Value:

**`disable-local-infile`**

* Description: Disable the use of [LOAD DATA LOCAL INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile).
* mysql\_optionsv: N/A
* Data Type: `string`
* Default Value:

**`host`**

* Description: Hostname or IP address of the server to connect to.
* mysql\_optionsv: `MARIADB_OPT_HOST`
* Data Type: `string`
* Default Value:

**`interactive-timeout`**

* Description:
* mysql\_optionsv: `MARIADB_OPT_INTERACTIVE`
* Data Type: `none`
* Default Value:

**`init-command`**

* Description: Command(s) which will be executed when connecting and reconnecting to the server.
* mysql\_optionsv: `MYSQL_INIT_COMMAND`
* Data Type: `string`
* Default Value:

**`local-infile`**

* Description: Enable or disable the use of [LOAD DATA LOCAL INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements-and-structure/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile).
* mysql\_optionsv: `MYSQL_OPT_LOCAL_INFILE`
* Data Type: `boolean`
* Default Value: `false`

**`max-allowed-packet`**

* Description: The maximum packet length to send to or receive from server. The default is 16MB, the maximum 1GB.
* mysql\_optionsv: `MYSQL_OPT_MAX_ALLOWED_PACKET`
* Data Type: `size_t`
* Default Value:

**`multi-results`**

* Description: Indicates that the client is able to handle multiple result sets from stored procedures or multi statements. This option will be automatically set if `multi-statements` is set.
* mysql\_optionsv: `MARIADB_OPT_MULTI_RESULTS`
* Data Type: `none`
* Default Value:

**`multi-statements`, `multi-queries`**

* Description: Allows the client to send multiple statements in one command. Statements will be divided by a semicolon.
* mysql\_optionsv: `MARIADB_OPT_MULTI_STATEMENTS`
* Data Type: `string`
* Default Value:

**`net-buffer-length`**

* Description: The buffer size for TCP/IP and socket communication. Default is 16KB.
* mysql\_optionsv: `MYSQL_OPT_NET_BUFFER_LENGTH`
* Data Type: `size_t`
* Default Value:
* Introduced: MariaDB Connector/C 3.0.0

**`password`**

* Description: Password of the user to login to the server.
* mysql\_optionsv: `MARIADB_OPT_PASSWORD`
* Data Type: `string`
* Default Value:

**`pipe`**

* Description: For Windows operating systems only: Use named pipes for client/server communication.
* mysql\_optionsv: `MYSQL_OPT_NAMED_PIPE`
* Data Type: `boolean`
* Default Value: `false`

**`plugin-dir`**

* Description: Specify the location of client plugins.
  * The plugin directory can also be specified with the `MARIADB_PLUGIN_DIR` environment variable.
* mysql\_optionsv: `MYSQL_PLUGIN_DIR`
* Data Type: `string`
* Default Value:

**`port`**

* Description: Port number to use for connection.
* mysql\_optionsv: `MARIADB_OPT_PORT`
* Data Type: `int`
* Default Value: 3306

**`protocol`**

* Description: Specify the type of client/server protocol. Possible values are:
  * `0` - Refers to `MYSQL_PROTOCOL_DEFAULT`
  * `1` - Refers to `MYSQL_PROTOCOL_TCP`
  * `2` - Refers to `MYSQL_PROTOCOL_SOCKET`
  * `3` - Refers to `MYSQL_PROTOCOL_PIPE`
  * `4` - Refers to `MYSQL_PROTOCOL_MEMORY`
* mysql\_optionsv: `MYSQL_OPT_PROTOCOL`
* Data Type: `int`
* Default Value:

**`reconnect`**

* Description: Enable or disable automatic reconnect.
* mysql\_optionsv: `MYSQL_OPT_RECONNECT`
* Data Type: `boolean`
* Default Value: `false`
* Introduced: MariaDB Connector/C 3.0.0

**`report-data-truncation`**

* Description: Enable or disable reporting data truncation errors for prepared statements.
* mysql\_optionsv: `MYSQL_REPORT_DATA_TRUNCATION`
* Data Type: `boolean`
* Default Value:

**`return-found-rows`**

* Description: Return the number of matched rows instead of number of changed rows.
* mysql\_optionsv: `MARIADB_OPT_FOUND_ROWS`
* Data Type: `none`
* Default Value:

**`secure-auth`**

* Description: Refuse client connecting to server if it uses old (pre-MySQL4.1.1) protocol. Defaults to false (unlike MySQL since 5,6, which defaults to true).
* mysql\_optionsv: `MYSQL_SECURE_AUTH`
* Data Type: `boolean`
* Default Value: `false`

**`server_public_key`**

* Description: Specifies the name of the file which contains the RSA public key of the database server. The format of this file must be in PEM format. This option is used by the [caching_sha2_password](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-sha-256) client authentication plugin.
* mysql\_optionsv: `MYSQL_SERVER_PUBLIC_KEY`
* Data Type: `string`
* Default Value:
* Introduced: MariaDB Connector/C 3.1.0

**`shared-memory-base-name`**

* Description: Shared-memory name to use for Windows connections using shared memory to a local server (started with the --shared-memory option). Case-sensitive.
* mysql\_optionsv: `MYSQL_SHARED_MEMORY_BASE_NAME`
* Data Type: `string`
* Default Value:

**`socket`**

* Description: For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use.
* mysql\_optionsv: `MARIADB_OPT_UNIXSOCKET`
* Data Type: `string`
* Default Value:

**`ssl-ca`**

* Description: Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path.
  * See [Secure Connections Overview: Certificate Authorities (CAs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-authorities-cas) for more information.
* mysql\_optionsv: `MYSQL_OPT_SSL_CA`
* Data Type: `string`
* Default Value:

**`ssl-capath`**

* Description: Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.
  * See [Secure Connections Overview: Certificate Authorities (CAs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-authorities-cas) for more information.
  * This option is only supported if the connector was built with OpenSSL. If the connector was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.
* mysql\_optionsv: `MYSQL_OPT_SSL_CAPATH`
* Data Type: `string`
* Default Value:

**`ssl-cert`**

* Description: Defines a path to the X509 certificate file to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path.
* mysql\_optionsv: `MYSQL_OPT_SSL_CERT`
* Data Type: `string`
* Default Value:

**`ssl-cipher`**

* Description: List of permitted ciphers or cipher suites to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption).
* mysql\_optionsv: `MYSQL_OPT_SSL_CIPHER`
* Data Type: `string`
* Default Value:

**`ssl-crl`**

* Description: Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path.
  * See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-revocation-lists-crls) for more information.
  * This option is only supported if the connector was built with OpenSSL or Schannel. If the connector was built with GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.
* mysql\_optionsv: `MYSQL_OPT_SSL_CRL`
* Data Type: `string`
* Default Value:
* Introduced: MariaDB Connector/C 3.1.1

**`ssl-crlpath`**

* Description: Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.
  * See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#certificate-revocation-lists-crls) for more information.
  * This option is only supported if the connector was built with OpenSSL. If the connector was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.
* mysql\_optionsv: `MYSQL_OPT_SSL_CRLPATH`
* Data Type: `string`
* Default Value:
* Introduced: MariaDB Connector/C 3.1.1

**`ssl-enforce`**

* Description: Whether to force [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption).
* mysql\_optionsv: `MYSQL_OPT_SSL_ENFORCE`
* Data Type: `boolean`
* Default Value:
* Introduced: MariaDB Connector/C 3.1.1

**`ssl-fp`**

* Description: Specify the SHA1 fingerprint of a server certificate for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) handshake.
* mysql\_optionsv: `MARIADB_OPT_SSL_FP`
* Data Type: `string`
* Default Value:
* Introduced: MariaDB Connector/C 3.0.0

**`ssl-fp-list`, `ssl-fplist`**

* Description: Specify a file which contains one or more SHA1 fingerprints of server certificates for validation during the [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) handshake.
* mysql\_optionsv: `MARIADB_OPT_SSL_FP_LIST`
* Data Type: `string`
* Default Value:
* Introduced: MariaDB Connector/C 3.0.0

**`ssl-key`**

* Description: Defines a path to a private key file to use for [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption). This option requires that you use the absolute path, not a relative path. If the key is protected with a passphrase, the passphrase needs to be specified with `ssl-passphrase` option.
* mysql\_optionsv: `MYSQL_OPT_SSL_KEY`
* Data Type: `string`
* Default Value:

**`ssl-passphrase`**

* Description: Specify a passphrase for a passphrase-protected private key, as configured by the [ssl-key](#ssl-key) option.
  * This option is only supported if the connector was built with OpenSSL or GnuTLS. If the connector was built with Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which libraries are used on which platforms.
* mysql\_optionsv: `MARIADB_OPT_TLS_PASSPHRASE`
* Data Type: `string`
* Default Value:
* Introduced: MariaDB Connector/C 3.0.0

**`ssl-verify-server-cert`**

* Description: Enables (or disables) [server certificate verification](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#server-certificate-verification).
* mysql\_optionsv: `MYSQL_OPT_SSL_VERIFY_SERVER_CERT`
* Data Type: `boolean`
* Default Value:
* Introduced: MariaDB Connector/C 3.0.0

**`tls_version`**

* Description: Defines which [TLS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption) protocol versions are allowed. This should be a comma-separated list of TLS protocol versions to allow. Valid TLS protocol versions are `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`. Both the client and server should support the allowed TLS protocol versions. See [Secure Connections Overview: TLS Protocol Version Support](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview#tls-protocol-version-support) for information on which TLS libraries support which TLS protocol versions. See [TLS and Cryptography Libraries Used by MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb) for more information about which TLS libraries are used on which platforms.
* mysql\_optionsv: `MARIADB_OPT_TLS_VERSION`
* Data Type: `string`
* Default Value:
* Introduced: MariaDB Connector/C 3.0.4

**`user`**

* Description: User to login to the server.
* mysql\_optionsv: `MARIADB_OPT_USER`
* Data Type: `string`
* Default Value:

### See Also

* [Configuring MariaDB with Option Files](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files)


{% @marketo/form formId="4316" %}
