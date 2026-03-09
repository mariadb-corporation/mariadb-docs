# mariadb-binlog Options

{% hint style="info" %}
Previously, the client was called `mysqlbinlog`. It can still be accessed under this name, via a symlink in Linux, or an alternate binary in Windows.
{% endhint %}

## Options

[mariadb-binlog](./) is a utility included with MariaDB for processing [binary log](../../../server-management/server-monitoring-logs/binary-log/) and [relay log](../../../server-management/server-monitoring-logs/binary-log/relay-log.md) files.

The following options are supported by [mariadb-binlog](./). They can be specified on the command line or in option files.

#### -?, --help

Display a help statement.

{% tabs %}
{% tab title="Current" %}
**--base64-output=**_**name**_

Determine when the output statements should be base64-encoded `BINLOG` statements. Options (case-insensitive) include `auto`, `unspec`, `never` ,and `decode-rows`. `never` neither prints base64 encodings nor verbose event data, and exits on error if a [row-based event](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) is found. This option is useful for binlogs that are entirely statement-based. `decode-rows` decodes row events into commented SQL statements if the `--verbose` option is also given. It can enhance the debugging experience with large binary log files, as the raw data is omitted. Unlike `never`, mariadb-binlog does not exit with an error if a row event is found. `auto` (synonymous with `unspec`) outputs base64 encoded entries for [row-based](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) and format description events; it should be used when `ROW`-format events are processed for re-executing on the MariaDB server. This behavior is presumed, such that `auto` is the default value when no option specification is provided. The other option values are intended only for debugging or testing purposes because they may produce output that does not include all events in executable form.
{% endtab %}

{% tab title="< 10.6 / 10.5.10" %}
**--base64-output\[=**_**name**_**]**

Determine when the output statements should be base64-encoded BINLOG statements. Options (case-insensitive) include `auto`, `unspec`, `always` (deprecated), `never` , and `decode-rows`. `never` disables it and works only for binlogs without [row-based events](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md); `decode-rows` decodes row events into commented SQL statements if the `--verbose` option is also given. Unlike `never`, `mariadb-binlog` does not exit with an error if a row event is found `auto` or `unspec`, the default, prints base64 only when necessary (for instance, for [row-based events](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) and format description events), and is the only safe behavior if you intend to use the output of `mariadb-binlog` to re-execute binary log file contents. The other option values are intended only for debugging or testing purposes, because they may produce output that does not include all events in executable form. `always` prints base64 whenever possible, and is for debugging only and should not be used in a production system. If this option is not given, the default is `auto`; if it is given with no argument, `always` is used.
{% endtab %}
{% endtabs %}

Default value: `auto`.

#### --binlog-row-event-max-size=_val_

The maximum size in bytes of a row-based [binary log](../../../server-management/server-monitoring-logs/binary-log/) event. Should be a multiple of 256. Minimum 256, maximum `18446744073709547520`. Default value: `4294967040` (4GB)

#### --character-sets-dir=_name_

Directory where the [character sets](../../../reference/data-types/string-data-types/character-sets/) are.

#### -d, --database=_name_

Output entries from the binary log (local log only) that occur while the name has been selected as the default database by [USE](../../../reference/sql-statements/administrative-sql-statements/use-database.md). Only one database can be specified. The effects depend on whether the [statement-based or row-based logging format](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md) is in use. For statement-based logging, the server only logs statements where the default database is _name_. The default database is set with the [USE](../../../reference/sql-statements/administrative-sql-statements/use-database.md) statement. For row-based logging, the server logs any updates to any tables in the named database, irrespective of the current database. Ignored in `--raw` mode.

#### ## \[options], --debug\[=options]

In a debug build, write a debugging log. A typical debug options string is `d:t:o,file\_name`. Default value: `d:t:o,/tmp/mariadb-binlog.trace`

#### --debug-check

Print some debug info at exit. Default value: `FALSE`

#### --debug-info

Print some debug info and memory and CPU info at exit. Default value: `FALSE`

#### --default-auth=_name_

Default authentication client-side plugin to use.

#### --defaults-extra-file=_name_

Read the file name, which can be the full path or the path relative to the current directory, after the global files are read.

#### --defaults-file=_name_

Only read default options from the given file name, which can be the full path or the path relative to the current directory.

#### --defaults-group-suffix=_str_

Also read groups with a suffix of _str_. For example, since `mariadb-binlog` normally reads the `[client]` and `[mysqlbinlog]` groups, `--defaults-group-suffix=`_`x`_ would cause it to also read the groups `\[mysqlbinlog\_x]` and `\[client\_x]`.

#### -D, --disable-log-bin

Disable binary log. This is useful if you enabled `--to-last-log` and are sending the output to the same MariaDB server. This way, you could avoid an endless loop. You would also like to use it when restoring after a crash to avoid duplication of the statements you already have. The `SUPER` privilege is needed to use this option. Default value: `FALSE`

#### --do-domain-ids=_name_

A list of positive integers, separated by commas, that form a whitelist of domain ids. Any log event with a [GTID](../../../ha-and-performance/standard-replication/gtid.md) that originates from a domain id specified in this list is displayed. Cannot be used with `--ignore-domain-ids`. When used with `--ignore-server-ids` or `--do-server-ids`, the result is the intersection between the two datasets. Available from MariaDB 10.9.

#### --do-server-ids=_name_

A list of positive integers, separated by commas, that form a whitelist of server ids. Any log event originating from a server id specified in this list is displayed. Cannot be used with `--ignore-server-ids`. When used with `--ignore-domain-ids` or `do-domain-ids`, the result is the intersection between the two datasets. Alias for `--server-id`. Available from MariaDB 10.9.

#### -B, --flashback

Support [flashback](../../../server-management/server-monitoring-logs/binary-log/flashback.md) mode. Default value: `FALSE`

#### -F, --force-if-open

Force if binlog was not closed properly. Defaults to `ON`; use `--skip-force-if-open` to disable. Default value: `TRUE`

#### -f, --force-read

If `mariadb-binlog` reads a binary log event that it does not recognize, it prints a warning, ignores the event, and continues. Without this option, `mariadb-binlog` stops if it reads such an event. Default value: `FALSE`

#### --gtid-strict-mode

Process binlog according to `gtid-strict-mode` specification. The start, stop positions are verified to satisfy the start < stop comparison condition. Sequence numbers of any [GTID](../../../ha-and-performance/standard-replication/gtid.md) domain must comprise a monotonically growing sequence. Defaults to `ON`; use `--skip-gtid-strict-mode` to disable. Available from MariaDB 10.8. Default value: `TRUE`

#### -H, --hexdump

Augment output with hexadecimal and ASCII event dump. Default value: `FALSE`

#### -h, --host=_name_

Get the binlog from the MariaDB server on the given host.

#### --ignore-domain-ids=_name_

A list of positive integers, separated by commas, that form a blacklist of domain ids. Any log event with a [GTID](../../../ha-and-performance/standard-replication/gtid.md) that originates from a domain id specified in this list is hidden. Cannot be used with `--do-domain-ids`. When used with `--ignore-server-ids` or `--do-server-ids`, the result is the intersection between the two datasets. Available from MariaDB 10.9.

#### --ignore-server-ids=_name_

A list of positive integers, separated by commas, that form a blacklist of server ids. Any log event originating from a server id specified in this list is hidden. Cannot be used with `--do-server-ids`. When used with `--ignore-domain-ids` or `--do-domain-ids`, the result is the intersection between the two datasets. Available from MariaDB 10.9.

#### -l path, --local-load=_path_

Prepare local temporary files for [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) in the specified directory. The temporary files are not automatically removed.

#### --no-defaults

Don't read default options from any option file.

#### -o value, --offset=_value_

Skip the first value entries in the log. Default value: `0`

#### --open\_files\_limit=_#_

Reserve file descriptors for usage by mariadb-binlog. Default value: `64`

#### -p\[_passwd_], --password\[=_passwd_]

Password to connect to the remote server. The password can be omitted, allow it to be entered from the prompt, or an option file can be used to avoid the security risk of passing a password on the command line.

#### --plugin-dir=_dir\_name_

Directory for client-side plugins.

#### -P _num_, --port=_num_

Port number to use for connection or `0` for default to, in order of preference, `my.cnf`, `$MYSQL_TCP_PORT`, `/etc/services`, built-in default (`3306`). Default value: `0`

#### --position=_#_

Removed. Use `--start-position` instead.

#### --print-defaults

Print the program argument list from all option files and exit.

#### --print-row-count

Print row counts for each row of events. (Defaults to `ON`; use `--skip-print-row-count` to disable.) Default value: `TRUE`

#### --print-row-event-positions

Print row event positions. Defaults to on; use `--skip-print-row-event-positions` to disable.) Default value: `TRUE`

#### print-table-metadata

Print metadata stored in `Table_map_log_event`.

#### --protocol=_name_

The protocol of the connection (`tcp`, `socket`, `pipe`, `memory`).

#### --raw

Requires `-R`. Output raw binlog data instead of SQL statements. Output files are named after server logs.

#### -R, --read-from-remote-server

Read binary logs from a remote MariaDB server rather than reading a local log file. Any connection parameter options are ignored unless this option is given as well. These options are `--host`, `--password`, `--port`, `--protocol`, `--socket`, and `--user`. This option requires that the remote server be running. It works only for binary log files on the remote server, not relay log files. Default value: `FALSE`

#### -r name, --result-file=_name_

Direct output to a given file. With `--raw`, this is a prefix for the file names.

#### --rewrite-db=_name_

Updates to a database with a different name than the original. Example: `rewrite-db='from->to'`. For events that are logged as statements, rewriting the database constitutes changing a statement's default database from `db1` to `db2`. There is no statement analysis or rewrite of any kind; that is, if you specify `db1.tbl` in the statement explicitly, that occurrence won't be changed to `db2.tbl`. Row-based events are rewritten correctly to use the new database name. Filtering (for instance, with `--database=name`) happens before the database rewrites have been performed. If you use this option on the command line and `>` has a special meaning to your command interpreter, quote the value (for instance, `--rewrite-db="oldname->newname"`).

#### --server-id=_idnum_

Extract only binlog entries created by the server having the given id. From MariaDB 10.9, an alias for `--do-server-ids`. Default value: `0`

#### --set-charset=_character\_set_

Add `SET NAMES character_set` to the output to specify the [character set](../../../reference/data-types/string-data-types/character-sets/) to be used for processing log files.

#### --shared-memory-base-name=_name_

Shared-memory _name_ to use for Windows connections using shared memory to a local server (started with the `--shared-memory` option). Case-sensitive. Default value: `MYSQL`

#### -s, --short-form

Just show regular queries: no extra info and no row-based events. This is for testing only, and should not be used in production systems. If you want to suppress base64-output, consider using `--base64-output=never` instead. Default value: `FALSE`

#### --skip-annotate-row-events

Skip all [Annotate\_rows](annotate_rows_log_event.md) events in the mariadb-binlog output (by default, `mariadb-binlog` prints `Annotate_rows` events if the binary log contains them).

#### -S, --socket=_name_

For connections to localhost, the Unix socket file to use, or, on Windows, the name of the named pipe to use.

#### --ssl

Enables [TLS](../../../security/encryption/data-in-transit-encryption/). TLS is also enabled even without setting this option when certain other TLS options are set. The `--ssl` option does not enable [verifying the server certificate](../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification) by default. In order to verify the server certificate, you must specify the `--ssl-verify-server-cert` option. Default value: `FALSE`

#### --ssl-ca=_name_

Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](../../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Authorities (CAs)](../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option implies the `--ssl` option.

#### --ssl-capath=_name_

Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](../../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Authorities (CAs)](../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-authorities-cas) for more information. This option is only supported if the client was built with OpenSSL or yaSSL. If the client was built with GnuTLS or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../security/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms. This option implies the `--ssl` option.

#### --ssl-cert=_name_

Defines a path to the X509 certificate file to use for [TLS](../../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

#### --ssl-cipher=_name_

List of permitted ciphers or cipher suites to use for [TLS](../../../security/encryption/data-in-transit-encryption/). This option implies the `--ssl` option.

#### --ssl-crl=_name_

Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](../../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL or Schannel. If the client was built with yaSSL or GnuTLS, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../security/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

#### --ssl-crlpath=_name_

Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](../../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. The directory specified by this option needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#certificate-revocation-lists-crls) for more information. This option is only supported if the client was built with OpenSSL. If the client was built with yaSSL, GnuTLS, or Schannel, then this option is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../../../security/encryption/tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.

#### --ssl-key=_name_

Defines a path to a private key file to use for [TLS](../../../security/encryption/data-in-transit-encryption/). This option requires that you use the absolute path, not a relative path. This option implies the `--ssl` option.

#### --ssl-verify-server-cert

Enables [server certificate verification](../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#server-certificate-verification). This option is disabled by default. Default value: `FALSE`

#### --start-datetime=_datetime_

If specified, start reading the binlog at the first event having a datetime equal to or later than the argument; the argument must be a date and time in the local time zone, in any format accepted by the MariaDB server for [DATETIME](../../../reference/data-types/date-and-time-data-types/datetime.md) and [TIMESTAMP](../../../reference/data-types/date-and-time-data-types/timestamp.md) types, for example: `2014-12-25 11:25:56` (you should probably use quotes for your shell to set it properly). This option is useful for point-in-time recovery.

#### -j pos, --start-position=_pos_

Start reading the binlog at this position. Type can either be a positive integer or, from MariaDB 10.8, a [GTID](../../../ha-and-performance/standard-replication/gtid.md) list. When using a positive integer, the value only applies to the first binlog passed on the command line. In GTID mode, multiple GTIDs can be passed as a comma-separated list, where each must have a unique domain id. The list represents the GTID binlog state that the client (another "replica" server) is aware of. Therefore, each GTID is exclusive; only events after a given sequence number are printed to allow users to receive events after their current state. Default value: `4`

{% hint style="warning" %}
Options `--start-position` and `--stop-position` currently compare Sequence Numbers only per Domain ID and ignore Server IDs. This is incorrect, as it is different from the Replication design for GTIDs, which compares per Domain–Server ID pair. MDEV-37231 tracks this bug.
{% endhint %}

#### --stop-datetime=_name_

If specified, stop reading the binlog at the first event having a datetime equal to or posterior to the argument; the argument must be a date and time in the local time zone, in any format accepted by the MariaDB server for `DATETIME` and `TIMESTAMP` types, for example: `2014-12-25 11:25:56` (you should probably use quotes for your shell to set it properly). Ignored in `--raw` mode.

{% tabs %}
{% tab title="≥ 10.11.14" %}
Emit a warning if the specified time is not found within the specified binlogs.
{% endtab %}
{% endtabs %}

#### --stop-never

Wait for more data from the server (and thus requires `-R` or `--read-from-remote-server`) instead of stopping at the end of the last log. Implies `--to-last-log`.

#### --stop-never-slave-server-id

The replica [server\_id](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#server_id) used for `--read-from-remote-server` `--stop-never`.

#### --stop-position=_position_

If specified, stop reading the binlog at this _position_. Type can either be a positive integer or, from MariaDB 10.8, a [GTID](../../../ha-and-performance/standard-replication/gtid.md) list. When using a positive integer, the value only applies to the last binlog passed on the command line. In GTID mode, multiple GTIDs can be passed as a comma-separated list, where each must have a unique domain id. Each GTID is inclusive; only events up to the given sequence numbers are printed. Ignored in `--raw` mode.

{% tabs %}
{% tab title="≥ 10.11.14" %}
Emit a warning if the specified position or GTID is not within the specified binlogs.
{% endtab %}

{% tab title="≥ 10.5.27" %}
Emit a warning if the specified position is beyond the end of the last binlog.
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Options `--start-position` and `--stop-position` currently compare Sequence Numbers only per Domain ID and ignore Server IDs. This is incorrect, as it is different from the Replication design for GTIDs, which compares per Domain–Server ID pair. MDEV-37231 tracks this bug.
{% endhint %}

#### -T, --table

List entries for just this table (affects only row events).

#### --tls-version=_name_

This option accepts a comma-separated list of TLS protocol versions. A TLS protocol version will only be enabled if it is present in this list. All other TLS protocol versions will not be permitted. See [Secure Connections Overview: TLS Protocol Versions](../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md#tls-protocol-versions) for more information. Default value: `TLSv1.1,TLSv1.2,TLSv1.3`

#### -t, --to-last-log

Requires `-R` or `--read-from-remote-server`. Does not stop at the end of the requested binlog but rather continues printing until the end of the last binlog of the MariaDB server. If you send the output to the same MariaDB server, that may lead to an endless loop. Default value: `FALSE`

#### -u, --user=_username_

Connect to the remote server as _username_.

#### -v, --verbose

Reconstruct SQL statements out of row events. `-v -v` adds comments on column data types.

#### -V, --version

Print version and exit.

#### --verify-binlog-checksum

Verify [binlog event checksums](../../../ha-and-performance/standard-replication/binlog-event-checksums.md) when reading a binlog file.

## Option Files

In addition to reading options from the command line, `mariadb-binlog` can also read options from [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md). If an unknown option is provided to `mariadb-binlog` in an option file, it is ignored.

The following options relate to how MariaDB command line tools handle option files. They must be given as the first argument on the command line:

| Option                    | Description                                                                         |
| ------------------------- | ----------------------------------------------------------------------------------- |
| --print-defaults          | Print the program argument list and exit.                                           |
| --no-defaults             | Don't read default options from any option file.                                    |
| --defaults-file=#         | Only read default options from the given file #.                                    |
| --defaults-extra-file=#   | Read this file after the global files are read.                                     |
| --defaults-group-suffix=# | In addition to the default option groups, also read option groups with this suffix. |

`mariadb-binlog` is linked with [MariaDB Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c). However, MariaDB Connector/C does not handle the parsing of option files for this client. That is performed by the server's option file parsing code. See [MDEV-19035](https://jira.mariadb.org/browse/MDEV-19035) for more information.

## Option Groups

`mariadb-binlog` reads options from the following [option groups](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) from the [option files](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md):

| Group             | Description                                                                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[mysqlbinlog]    | Options read by mariadb-binlog, which includes both MariaDB Server and MySQL Server.                                                                                                |
| \[mariadb-binlog] | Options read by mariadb-binlog.                                                                                                                                                     |
| \[client]         | Options read by all MariaDB and MySQL client programs, which include both MariaDB and MySQL clients. For example, mysqldump.                                                        |
| \[client-server]  | Options read by all MariaDB [client programs](../../) and the MariaDB Server. This is useful for options like socket and port, which are common between the server and the clients. |
| \[client-mariadb] | Options read by all MariaDB client programs.                                                                                                                                        |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
