# mariadb Command-Line Client

**mariadb** is a simple SQL shell (with GNU readline capabilities).

Prior to [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105), the client used to be called `mysql`, and can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.

### About the mariadb Command-Line Client

**mariadb** supports interactive and non-interactive use. When used\
interactively, query results are presented in an ASCII-table format. When used\
non-interactively (for example, as a filter), the result is presented in\
tab-separated format. The output format can be changed using command options.

If you have problems due to insufficient memory for large result sets, use the`--quick` option. This forces mariadb to retrieve results from\
the server a row at a time rather than retrieving the entire result set and\
buffering it in memory before displaying it. This is done by returning the\
result set using the `mysql_use_result()` C API function in the\
client/server library rather than `mysql_store_result()`.

Using mariadb is very easy. Invoke it from the prompt of your command interpreter\
as follows:

```
mariadb db_name
```

Or:

```
mariadb --user=user_name --password=your_password db_name
```

Then type an SQL statement, end it with “;”, \g, or \G and press Enter.

Typing Control-C causes mariadb to attempt to kill the\
current statement. If this cannot be done, or Control-C is typed again before\
the statement is killed, mariadb exits.

You can execute SQL statements in a script file (batch file) like this:

```
mariadb db_name < script.sql > output.tab
```

### Using mariadb

The command to use `mariadb` and the general syntax is:

```
mariadb <options>
```

#### Options

`mariadb` supports the following options:

**`-?, --help`**

Display help and exit.

**`-I, --help`**

Synonym for `-?`

**`--abort-source-on-error`**

Abort 'source filename' operations in case of errors.

**`--auto-rehash`**

Enable automatic rehashing. This option is on by default, which enables database, table, and column name completion. Use `--disable-auto-rehash`, `--no-auto-rehash` or `skip-auto-rehash` to disable rehashing. That causes mariadb to start faster, but you must issue the rehash command if you want to use name completion. To complete a name, enter the first part and press Tab. If the name is unambiguous, mariadb completes it. Otherwise, you can press Tab again to see the possible names that begin with what you have typed so far. Completion does not occur if there is no default database.

**`-A, --no-auto-rehash`**

No automatic rehashing. One has to use 'rehash' to get table and field completion. This gives a quicker start of mariadb and disables rehashing on reconnect.

**`--auto-vertical-output`**

Automatically switch to vertical output mode if the result is wider than the terminal width.

**`-B, --batch`**

Print results using tab as the column separator, with each row on a new line. With this option, mariadb does not use the history file. Batch mode results in nontabular output format and escaping of special characters. Escaping may be disabled by using raw mode; see the description for the `--raw` option. (Enables `--silent`.)

**`--binary-mode`**

By default, ASCII '\0' is disallowed and '\r\n' is translated to '\n'. This switch turns off both features, and also turns off parsing of all client commands except \C and DELIMITER, in non-interactive mode (for input piped to mariadb or loaded using the 'source' command). This is necessary when processing output from [mariadb-binlog](../logging-tools/mariadb-binlog/) that may contain blobs.

**`--character-sets-dir=name`**

Directory for [character set](../../reference/data-types/string-data-types/character-sets/) files.

**`--column-names`**

Write column names in results. (Defaults to on; use `--skip-column-names` to disable.)

**`--column-type-info`**

Display column type information.

**`-c, --comments`**

Preserve comments. Send comments to the server. The default is `--skip-comments` (discard comments), enable with `--comments`.

**`-C, --compress`**

Compress all information sent between the client and the server if both support compression.

**`--connect-expired-password`**

Notify the server that this client is prepared to handle [expired password sandbox mode](../../security/user-account-management/user-password-expiry.md) even if `--batch` was specified. From [MariaDB 10.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1043-release-notes).

**`--connect-timeout=num`**

Number of seconds before connection timeout. Defaults to zero.

**`-D, --database=name`**

Database to use.

**\`-**

## \[options], --debug\[=options]\`

On debugging builds, write a debugging log. A typical debug\_options string is `d:t:o,file_name`. The default is `d:t:o,/tmp/mysql.trace`.

**`--debug-check`**

Check memory and open file usage at exit.

**`-T, --debug-info`**

Print some debug info at exit.

**`--default-auth=plugin`**

Default authentication client-side plugin to use.

**`--default-character-set=name`**

Set the default [character set](../../reference/data-types/string-data-types/character-sets/). A common issue that can occur when the operating system uses utf8 or another multibyte character set is that output from the mariadb client is formatted incorrectly, due to the fact that the MariaDB client uses the latin1 character set by default. You can usually fix such issues by using this option to force the client to use the system character set instead. If set to `auto` the character set is taken from the client environment (`LC_CTYPE` on Unix).

**`--defaults-extra-file=file`**

Read this file after the global files are read. Must be given as the first option.

**`--defaults-file=file`**

Only read default options from the given _file_. Must be given as the first option.

**`--defaults-group-suffix=suffix`**

In addition to the given groups, also read groups with this suffix.

**`--delimiter=name`**

Delimiter to be used. The default is the semicolon character (“;”).

**`--enable-cleartext-plugin`**

Obsolete option. Exists only for MySQL compatibility.

**`-e, --execute=name`**

Execute statement and quit. Disables `--force` and history file. The default output format is like that produced with `--batch`.

**`-f, --force`**

Continue even if we get an SQL error. Sets `--abort-source-on-error` to 0.

**`-h, --host=name`**

Connect to host.

**`-H, --html`**

Produce HTML output.

**`-U, --i-am-a-dummy`**

Synonym for option `--safe-updates`, `-U`.

**`-i, --ignore-spaces`**

Ignore space after function names. Allows one to have spaces (including tab characters and new line characters) between function name and '('. The drawback is that this causes built in functions to become reserved words.

**`--init-command=str`**

SQL Command to execute when connecting to the MariaDB server. Will automatically be re-executed when reconnecting.

**`--line-numbers`**

Write line numbers for errors. (Defaults to on; use `--skip-line-numbers` to disable.)

**`--local-infile`**

Enable or disable LOCAL capability for [LOAD DATA INFILE](../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md). With no value, the option enables LOCAL. The option may be given as`--local-infile=0` or `--local-infile=1` to explicitly disable or enable LOCAL. Enabling LOCAL has no effect if the server does not also support it.

**`--max-allowed-packet=num`**

The maximum packet length to send to or receive from server. The default is 16MB, the maximum 1GB.

**`--max-join-size=num`**

Automatic limit for rows in a join when using `--safe-updates`. Default is 1000000.

**`-G, --named-commands`**

Enable named commands. Named commands mean mariadb's internal commands (see below) . When enabled, the named commands can be used from any line of the query, otherwise only from the first line, before an enter. Long-format commands are allowed, not just short-format commands. For example, `quit` and `\q` are both recognized. Disable with `--disable-named-commands`. This option is disabled by default.

**`--net-buffer-length=num`**

The buffer size for TCP/IP and socket communication. Default is 16KB.

**`-b, --no-beep`**

Turn off beep on error.

**`--no-defaults`**

Don't read default options from any option file. Must be given as the first option.

**`-o, --one-database`**

Ignore statements except those that occur while the default database is the one named on the command line. This filtering is limited, and based only on [USE](../../reference/sql-statements/administrative-sql-statements/use-database.md) statements. This is useful for skipping updates to other databases in the binary log.

**`--pager[=name]`**

Pager to use to display results (Unix only). If you don't supply an option, the default pager is taken from your ENV variable PAGER. Valid pagers are _less_, _more_, _cat \[> filename]_, etc. See interactive help (\h) also. This option does not work in batch mode. Disable with `--disable-pager`. This option is disabled by default.

**`-p, --password[=name]`**

Password to use when connecting to server. If you use the short option form (-p), you cannot have a space between the option and the password. If you omit the password value following the `--password` or `-p` option on the command line, mariadb prompts for one. Specifying a password on the command line should be considered insecure. You can use an option file to avoid giving the password on the command line.

**`--plugin-dir=name`**

Directory for client-side plugins.

**`-P, --port=num`**

Port number to use for connection or 0 for default to, in order of preference, my.cnf, $MYSQL\_TCP\_PORT, /etc/services, built-in default (3306).

**`--print-defaults`**

Print the program argument list and exit. Must be given as the first option.

**`--progress-reports`**

Get [progress reports](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for long running commands (such as [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table.md)). (Defaults to on; use `--skip-progress-reports` to disable.)

**`--prompt=name`**

Set the mariadb prompt to this value. See [prompt command](mariadb-command-line-client.md#prompt-command) for options.

**`--protocol=name`**

The protocol to use for connection (tcp, socket, pipe, memory).

**`-q, --quick`**

Don't cache result, print it row by row. This may slow down the server if the output is suspended. Doesn't use history file.

**`--quick-max-column-width=N`**

Maximal field length limit in case of --quick (since [MariaDB 10.5.27](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10-5-27-release-notes), [MariaDB 10.6.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-20-release-notes), [MariaDB 10.11.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-10-release-notes), [MariaDB 11.4.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-4-release-notes), [MariaDB 11.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-6-rolling-releases/mariadb-11-6-2-release-notes) and [MariaDB 11.7.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/mariadb-11-7-rolling-releases/mariadb-11-7-1-release-notes))

**`-r, --raw`**

For tabular output, the “boxing” around columns enables one column value to be distinguished from another. For nontabular output (such as is produced in batch mode or when the `--batch` or `--silent` option is given), special characters are escaped in the output so they can be identified easily. Newline, tab, NUL, and backslash are written as , , `\0`, and \`\`. The `--raw` option disables this character escaping.

**`--reconnect`**

Reconnect if the connection is lost. This option is enabled by default. Disable with `--disable-reconnect` or `skip-reconnect`.

**`-U, --safe-updates`**

Allow only those [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statements that specify which rows to modify by using key values. If you have set this option in an option file, you can override it by using `--safe-updates` on the command line. See [using the --safe-updates option](mariadb-command-line-client.md#using-the-safe-updates-option) for more.

**`--sandbox`**

Disallow commands that access the file system (except `\P` without an argument and `\e`). Disabled commands include system (`\!`), tee (), pager with an argument(`\P foo`), source (`\.`). Using a disabled command is an error, which can be ignored with [--force](mariadb-command-line-client.md#-f-force). A sandbox command (`\-`) enables the sandbox mode until EOF (current file or the session, if interactive). From [MariaDB 10.5.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10-5-25-release-notes), [MariaDB 10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-18-release-notes), [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes), [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes), [MariaDB 11.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-2-release-notes).

**`--script-dir`**

Sets an alternative directory path for searching scripts invoked via the source command. From [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).

**`--secure-auth`**

Refuse client connecting to server if it uses old (pre-MySQL4.1.1) protocol. Defaults to false.

**`--select-limit=num`**

Automatic limit for SELECT when using --safe-updates. Default 1000.

**`--server-arg=name`**

Send embedded server this as a parameter.

**`--shared-memory-base-name=name`**

Shared-memory name to use for Windows connections using shared memory to a local server (started with the --shared-memory option). Case-sensitive.

**`--show-warnings`**

Show warnings after every statement. Applies to interactive and batch mode.

**`--sigint-ignore`**

Ignore SIGINT signals (usually CTRL-C).

**`-s, --silent`**

Be more silent. This option can be given multiple times to produce less and less output. This option results in nontabular output format and escaping of special characters. Escaping may be disabled by using raw mode; see the description for the `--raw` option.

**`--skip-auto-rehash`**

Disable automatic rehashing. See `--auto-rehash`.

**`-N, --skip-column-names`**

Don't write column names in results. See `--column-names`.

**`--skip-comments`**

Discard comments. Set by default, see `--comments` to enable.

**`-L`, `--skip-line-numbers`**

Don't write line number for errors. See `--line-numbers`.

**`--skip-progress-reports`**

Disables getting [progress reports](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for long running commands. See `--progress-reports`.

**`--skip-reconnect`**

Don't reconnect if the connection is lost. See `--reconnect`.

**`-S, --socket=name`**

For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use. The socket file can exist in different locations depending on setup. Common locations include:

* Debian-based, Ubuntu: /var/run/mysqld/mysqld.sock
* SUSE: /var/run/mysql/mysql.sock
* Red Hat: /var/lib/mysql/mysql.sock
* Other: /tmp/mysql.sock

**`--ssl`**

Enables [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). TLS is also enabled even without setting this option when certain other TLS options are set. The `--ssl` option does not enable [verifying the server certificate](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, the user must specify the `--ssl-verify-server-cert` option. Set by default from [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010).

**`--ssl-ca=name`**

Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option implies the `--ssl` option.

**`--ssl-capath=name`**

Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option is only supported if the client was built with OpenSSL or yaSSL. If the client was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. This option implies the `--ssl` option.

**`--ssl-cert=name`**

Defines a path to the X509 certificate file to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

**`--ssl-cipher=name`**

List of permitted ciphers or cipher suites to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option implies the `--ssl` option.

**`--ssl-crl=name`**

Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL or Schannel. If the client was built with yaSSL or GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

**`--ssl-crlpath=name`**

Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL. If the client was built with yaSSL, GnuTLS, or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../security/securing-mariadb/securing-mariadb-encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

**`--ssl-key=name`**

Defines a path to a private key file to use for [TLS](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

**`--ssl-verify-server-cert`**

Enables [server certificate verification](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). Prior to [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/what-is-mariadb-114), this option is disabled by default, otherwise enabled. Use `--disable-ssl` or `--disable-ssl-verify-server-cert` to revert to the pre-11.4 behavior.

**`-t, --table`**

Display output in table format. This is the default for interactive use, but can be used to produce table output in batch mode.

**`--tee=name`**

Append everything into outfile. See interactive help (\h) also. Does not work in batch mode. Disable with `--disable-tee`. This option is disabled by default.

**`--tls-version=name`**

This option accepts a comma-separated list of TLS protocol versions. A TLS protocol version will only be enabled if it is present in this list. All other TLS protocol versions will not be permitted. See [Secure Connections Overview: TLS Protocol Versions](../../security/securing-mariadb/securing-mariadb-encryption/data-in-transit-encryption/secure-connections-overview.md#tls-protocol-versions) for more information. This option was added in [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes).

**`--ssl-fp=name`**

Server certificate fingerprint (implies --ssl). Added in [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes).

**`--ssl-fplist=name`**

File with accepted server certificate fingerprints, one per line (implies --ssl). Added in [MariaDB 11.3.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-3-rolling-releases/mariadb-11-3-0-release-notes).

**`-n, --unbuffered`**

Flush buffer after each query.

**`-u`, `--user=name`**

User for login if not current user.

**`-v, --verbose`**

Write more. (-v -v -v gives the table output format).

**`-V, --version`**

Output version information and exit.

**`-E, --vertical`**

Print the output of a query (rows) vertically. Use the `\G` delimiter to apply to a particular statement if this option is not enabled.

**`-w, --wait`**

If the connection cannot be established, wait and retry instead of aborting.

**`-X`, `--xml`**

Produce XML output. See the [mariadb-dump --xml option](../backup-restore-and-import-clients/mariadb-dump.md#null-null-and-empty-values-in-xml) for more.

#### Option Files

In addition to reading options from the command-line, `mariadb` can also read options from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb` in an option file, then it is ignored.

The following options relate to how MariaDB command-line tools handles option files. They must be given as the first argument on the command-line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

`mariadb` is linked with [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c). However, MariaDB Connector/C does not yet handle the parsing of option files for this client. That is still performed by the server option file parsing code. See [MDEV-19035](https://jira.mariadb.org/browse/MDEV-19035) for more information.

**Option Groups**

`mariadb` reads options from the following [option groups](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from [option files](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group             | Description                                                                                                                                                                                                                                                                |
| ----------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysql]          | Options read by mysql, which includes both MariaDB Server and MySQL Server.                                                                                                                                                                                                |
| \[mariadb-client] | Options read by mariadb. Available starting with [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes).                                        |
| \[client]         | Options read by all MariaDB and MySQL [client programs](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md), which includes both MariaDB and MySQL clients. For example, mysqldump.                                            |
| \[client-server]  | Options read by all MariaDB [client programs](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md) and the MariaDB Server. This is useful for options like socket and port, which is common between the server and the clients. |
| \[client-mariadb] | Options read by all MariaDB [client programs](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/clients-utilities/README.md).                                                                                                                             |

### How to Specify Which Protocol to Use When Connecting to the Server

You can force which protocol to be used to connect to the `mariadbd` server by giving the `protocol` option one of the following values: `tcp`, `socket`, `pipe` or `memory`.

If `protocol` is not specified, before [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes), command line connection properties that do not force protocol are ignored.

From [MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-1061-release-notes), a connection property specified via the command line (e.g. `--port=3306`) will force its type. The protocol that matches the respective connection property is used, e.g. a TCP/IP connection is created when `--port` is specified.

If multiple or no connection properties are specified via the command-line, then the following happens:

#### Linux/Unix

* If `hostname` is not specified or `hostname` is `localhost`, then Unix sockets are used.
* In other cases (`hostname` is given and it's not `localhost`) then a TCP/IP connection through the `port` option is used.

Note that `localhost` is a special value. Using 127.0.0.1 is not the same thing. The latter will connect to the mariadbd server through TCP/IP.

#### Windows

* If `shared-memory-base-name` is specified and `hostname` is not specified or `hostname` is `localhost`, then the connection will happen through shared memory.
* If `shared-memory-base-name` is not specified and `hostname` is not specified or `hostname` is `localhost`, then the connection will happen through windows named pipes.
* Named pipes will also be used if the `libmysql` / `libmariadb` client library detects that the client doesn't support TCP/IP.
* In other cases then a TCP/IP connection through the `port` option is used.

### How to Test Which Protocol is Used

The `status` command shows you information about which protocol is used:

```
shell> mariadb test

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 3
Server version: 11.4.1-MariaDB MariaDB Server

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [test]> status;
--------------
mysql  Ver 15.1 Distrib 10.0.25-MariaDB, for Linux (x86_64) using readline 5.2

Connection id:          10
Current database:       test
Current user:           monty@localhost
...
Connection:             Localhost via UNIX socket
...
UNIX socket:            /tmp/mysql-dbug.sock
```

### mariadb Commands

There are also a number of commands that can be run inside the client. Note that all text commands must be first on line and end with ';'

| Command       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| -             | Enables [sandbox](mariadb-command-line-client.md#-sandbox) mode until EOF (current file or the session, if interactive). From [MariaDB 10.5.25](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-10-5-25-release-notes), [MariaDB 10.6.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-18-release-notes), [MariaDB 10.11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-8-release-notes), [MariaDB 11.0.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-6-release-notes), [MariaDB 11.1.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-5-release-notes), [MariaDB 11.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-4-release-notes), [MariaDB 11.4.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-4-series/mariadb-11-4-2-release-notes). |
| ?, ?          | Synonym for \`help'.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| clear, \c     | Clear the current input statement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| connect,      | Reconnect to the server. Optional arguments are db and host.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| delimiter, \d | Set statement delimiter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| edit, \e      | Edit command with $EDITOR.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ego, \G       | Send command to mariadb server, display result vertically.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| exit, \q      | Exit mariadb. Same as quit.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| go, \g        | Send command to mariadb server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| help, \h      | Display this help.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| nopager,      | Disable pager, print to stdout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| notee,        | Don't write into outfile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| pager, \P     | Set PAGER \[to\_pager]. Print the query results via PAGER.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| print, \p     | Print current command.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| prompt,       | Change your mariadb prompt. See [prompt command](mariadb-command-line-client.md#prompt-command) for options.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| quit, \q      | Quit mariadb.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| rehash, #     | Rebuild completion hash.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| source, .     | Execute an SQL script file. Takes a file name as an argument. Usually looks in the working directory, unless, from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120), a path is given with [--script-dir](mariadb-command-line-client.md#-script-dir).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| status, \s    | Get status information from the server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| system, !     | Execute a system shell command. Only works in Unix-like systems.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| tee,          | Set outfile \[to\_outfile]. Append everything into given outfile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| use, \u       | Use another database. Takes database name as argument.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| charset, \C   | Switch to another charset. Might be needed for processing binlog with multi-byte charsets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| warnings, \W  | Show warnings after every statement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| nowarning, \w | Don't show warnings after every statement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

### The mysql\_history File

On Unix, the mariadb client writes a record of executed statements to a history\
file. By default, this file is named `.mysql_history` and is created in your home\
directory. To specify a different file, set the value of the MYSQL\_HISTFILE\
environment variable.

The .mysql\_history file should be protected with a restrictive access mode because\
sensitive information might be written to it, such as the text of SQL\
statements that contain passwords.

If you do not want to maintain a history file, first remove .mysql\_history if\
it exists, and then use either of the following techniques:

* Set the MYSQL\_HISTFILE variable to /dev/null. To cause this setting to take\
  effect each time you log in, put the setting in one of your shell's startup\
  files.
* Create .mysql\_history as a symbolic link to /dev/null:

```
shell> ln -s /dev/null $HOME/.mysql_history
```

You need do this only once.

### prompt Command

The prompt command reconfigures the default prompt `\N [\d]>`. The string for defining the prompt can contain the following special sequences.

| Option | Description                                                         |
| ------ | ------------------------------------------------------------------- |
| \c     | A counter that increments for each statement you issue.             |
| \D     | The full current date.                                              |
| \d     | The default database.                                               |
| \h     | The server host.                                                    |
| \l     | The current delimiter.                                              |
| \m     | Minutes of the current time.                                        |
|        | A newline character.                                                |
| \O     | The current month in three-letter format (Jan, Feb, ...).           |
| \o     | The current month in numeric format.                                |
| \P     | am/pm.                                                              |
| \p     | The current TCP/IP port or socket file.                             |
|        | The current time, in 24-hour military time (0–23).                  |
|        | The current time, standard 12-hour time (1–12).                     |
| \S     | Semicolon.                                                          |
| \s     | Seconds of the current time.                                        |
|        | A tab character.                                                    |
| \U     | Your full user\_name@host\_name account name.                       |
| \u     | Your user name.                                                     |
| \v     | The server version.                                                 |
| \w     | The current day of the week in three-letter format (Mon, Tue, ...). |
| \Y     | The current year, four digits.                                      |
| \y     | The current year, two digits.                                       |
| \_     | A space.                                                            |
| \\     | A space (a space follows the backslash).                            |
| '      | Single quote.                                                       |
| "      | Double quote.                                                       |
| \ \\   | A literal “\” backslash character.                                  |
| \x     | x, for any “x” not listed above.                                    |

### mariadb Tips

This section describes some techniques that can help you use`mariadb` more effectively.

#### Displaying Query Results Vertically

Some query results are much more readable when displayed vertically, instead of\
in the usual horizontal table format. Queries can be displayed vertically by\
terminating the query with \G instead of a semicolon. For example, longer text\
values that include newlines often are much easier to read with vertical\
output:

```
mariadb> SELECT * FROM mails WHERE LENGTH(txt) < 300 LIMIT 300,1\G
*************************** 1. row ***************************
  msg_nro: 3068
    date: 2000-03-01 23:29:50
time_zone: +0200
mail_from: Monty
    reply: monty@no.spam.com
  mail_to: "Thimble Smith" <tim@no.spam.com>
      sbj: UTF-8
      txt: >>>>> "Thimble" == Thimble Smith writes:
Thimble> Hi.  I think this is a good idea.  Is anyone familiar
Thimble> with UTF-8 or Unicode? Otherwise, I´ll put this on my
Thimble> TODO list and see what happens.
Yes, please do that.
Regards,
Monty
    file: inbox-jani-1
    hash: 190402944
1 row in set (0.09 sec)
```

#### Using the --safe-updates Option

For beginners, a useful startup option is `--safe-updates` (or`--i-am-a-dummy`, which has the same effect). It is helpful\
for cases when you might have issued a`DELETE FROM tbl_name` statement but forgotten the`WHERE` clause. Normally, such a statement deletes all rows\
from the table. With `--safe-updates`, you can delete rows\
only by specifying the key values that identify them. This helps prevent\
accidents.

When you use the `--safe-updates` option, mariadb issues the\
following statement when it connects to the MariaDB server:

```
SET sql_safe_updates=1, sql_select_limit=1000, sql_max_join_size=1000000;
```

The [SET](../../reference/sql-statements/administrative-sql-statements/set-commands/set.md) statement has the following effects:

* You are not allowed to execute an [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) or [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statement unless you\
  specify a key constraint in the WHERE clause or provide a LIMIT clause (or\
  both). For example:

```
UPDATE tbl_name SET not_key_column=val WHERE key_column=val;
UPDATE tbl_name SET not_key_column=val LIMIT 1;
```

* The server limits all large`SELECT` results to 1,000 rows\
  unless the statement includes a `LIMIT` clause.
* The server aborts multiple-table `SELECT` statements that\
  probably need to examine more than 1,000,000 row combinations.

To specify limits different from 1,000 and 1,000,000, you can override the\
defaults by using the `--select_limit` and `--max_join_size` options:

```
mariadb --safe-updates --select_limit=500 --max_join_size=10000
```

#### Disabling mariadb Auto-Reconnect

If the mariadb client loses its connection to the server while sending a\
statement, it immediately and automatically tries to reconnect once to the\
server and send the statement again. However, even if mariadb succeeds in\
reconnecting, your first connection has ended and all your previous session\
objects and settings are lost: temporary tables, the autocommit mode, and\
user-defined and session variables. Also, any current transaction rolls back.\
This behavior may be dangerous for you, as in the following example where the\
server was shut down and restarted between the first and second statements\
without you knowing it:

```
mariadb> SET @a=1;
Query OK, 0 rows affected (0.05 sec)
mariadb> INSERT INTO t VALUES(@a);
ERROR 2006: MySQL server has gone away
No connection. Trying to reconnect...
Connection id:    1
Current database: test
Query OK, 1 row affected (1.30 sec)
mariadb> SELECT * FROM t;
+------+
| a    |
+------+
| NULL |
+------+
```

The @a user variable has been lost with the connection, and after the\
reconnection it is undefined. If it is important to have mariadb terminate with\
an error if the connection has been lost, you can start the mariadb client with\
the `--skip-reconnect` option.

### See Also

* [Troubleshooting Connection Issues](../../mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide.md)
* [Readline commands and configuration](https://docs.freebsd.org/info/readline/readline.pdf)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
