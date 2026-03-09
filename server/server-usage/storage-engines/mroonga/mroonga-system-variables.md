# Mroonga System Variables

This page documents system variables related to the [Mroonga storage engine](./). See [Server System Variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for instructions on setting them.

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `mroonga_action_on_fulltext_query_error`

* Description: Action to take when encountering a Mroonga fulltext error.
  * `ERROR`: Report an error without logging.
  * `ERROR_AND_LOG`: Report an error with logging (the default)
  * `IGNORE`: No logging or reporting - the error is ignored.
  * `IGNORE_AND_LOG`: Log the error without reporting it.
* Command line: `--mroonga-action-on-fulltext-query-error=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `ERROR_AND_LOG`

#### `mroonga_boolean_mode_syntax_flags`

* Description: Flags to customize syntax in BOOLEAN MODE searches. Available flags:
  * `DEFAULT`: (=SYNTAX\_QUERY,ALLOW\_LEADING\_NOT)
  * `ALLOW_COLUMN`: Allows `COLUMN:...` syntax in query syntax, an incompatible change to the regular BOOLEAN MODE syntax. Permits multiple indexes in one `MATCH () AGAINST ()`. Can be used in other operations besides full-text search, such as equal, and prefix search. See [Groonga query syntax](https://groonga.org/docs/reference/grn_expr/query_syntax.html) for more details.
  * `ALLOW_LEADING_NOT` Permits using the `NOT_INCLUDED_KEYWORD` syntax in the query syntax.
  * `ALLOW_UPDATE`: Permits updating values with the `COLUMN:=NEW_VALUE` syntax in the query syntax.
  * `SYNTAX_QUERY`: Mroonga will use Groonga's query syntax, compatible with MariaDB's BOOLEAN MODE syntax. Unless `SYNTAX_SCRIPT` is specified, this mode is always in use.
  * `SYNTAX_SCRIPT`: Mroonga will use Groonga's script syntax, a JavaScript-like syntax. If both `SYNTAX_QUERY` and `SYNTAX_SCRIPT` are specified, `SYNTAX_SCRIPT` will take precedence..
* Command line: `--mroonga-boolean-mode-syntax-flags=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `DEFAULT`

#### `mroonga_database_path_prefix`

* Description: The database path prefix.
* Command line: `--mroonga-database-path-prefix=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: (Empty)

#### `mroonga_default_parser`

* Description: The fulltext default parser, for example `TokenBigramSplitSymbolAlphaDigit` or `TokenBigram` (the default). See the list of options at [Mroonga Overview:Parser](mroonga-overview.md#parser). Deprecated since Mroonga 5.04, use [mroonga\_default\_tokenizer](mroonga-system-variables.md#mroonga_default_tokenizer) instead.
* Command line: `--mroonga-default-parser=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `TokenBigram`
* Deprecated: [MariaDB 10.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.6), Mroonga 5.0.4

#### `mroonga_default_tokenizer`

* Description: The fulltext default parser, for example `TokenBigramSplitSymbolAlphaDigit` or `TokenBigram` (the default). See the list of options at [Mroonga Overview:Parser](mroonga-overview.md#parser).
* Command line: `--mroonga-default-tokenizer=value`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `string`
* Default Value: `TokenBigram`
* Introduced: [MariaDB 10.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.6), Mroonga 5.0.4

#### `mroonga_default_wrapper_engine`

* Description: The default engine for wrapper mode.
* Command line: `--mroonga-default-wrapper-engine=value`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: (Empty)

#### `mroonga_dry_write`

* Description: If set to `on`, (`off` is default), data is not actually written to the Groonga database. Only really useful to change for benchmarking.
* Command line: `--mroonga-dry-write[={0|1}]`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `off`

#### `mroonga_enable_operations_recording`

* Description: Whether recording operations for recovery to the Groonga database is enabled (default) or not. Requires reopening the database with [FLUSH TABLES](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) after changing the variable.
* Command line: `--mroonga-enable-operations-recording={0|1}`
* Scope: Global
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.2.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.11), [MariaDB 10.1.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.29)

#### `mroonga_enable_optimization`

* Description: If set to `on` (the default), optimization is enabled. Only really useful to change for benchmarking.
* Command line: `--mroonga-enable-optimization={0|1}`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `boolean`
* Default Value: `on`

#### `mroonga_libgroonga_embedded`

* Description: Whether libgroonga is embedded or not.
* Command line: None
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`
* Introduced: [MariaDB 10.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.6)

#### `mroonga_libgroonga_support_lz4`

* Description: Whether libgroonga supports lz4 or not.
* Command line: None
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`

#### `mroonga_libgroonga_support_zlib`

* Description: Whether libgroonga supports zlib or not.
* Command line: None
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `ON`

#### `mroonga_libgroonga_support_zstd`

* Description: Whether libgroonga supports Zstandard or not.
* Command line: None
* Scope: Global
* Dynamic: No
* Data Type: `boolean`
* Default Value: `OFF`
* Introduced: [MariaDB 10.2.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.11), [MariaDB 10.1.29](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.29)

#### `mroonga_libgroonga_version`

* Description: Groonga library version.
* Command line: None
* Scope: Global
* Dynamic: No
* Data Type: `string`

#### `mroonga_lock_timeout`

* Description: Lock timeout used in Groonga.
* Command line: `--mroonga-lock-timeout=#`
* Scope: Global
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `900000`
* Range: `-1` to `2147483647`

#### `mroonga_log_file`

* Description: Name and path of the Mroonga log file.
* Command line: `--mroonga-log-file=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: `groonga.log`

#### `mroonga_log_level`

* Description: Mroonga log file output level, which determines what is logged. Valid levels include:
  * `NONE` No output.
  * `EMERG`: Only emergency error messages, such as database corruption.
  * `ALERT`: Alert messages, such as internal errors.
  * `CRIT`: Critical error messages, such as deadlocks.
  * `ERROR`: Errors, such as API errors.
  * `WARNING`: Warnings, such as invalid arguments.
  * `NOTICE`: Notices, such as a change in configuration or a status change.
  * `INFO`: Information messages, such as file system operations.
  * `DEBUG`: Debug messages, suggested for developers or testers.
  * `DUMP`: Dump messages.
* Command line: `--mroonga-log-level=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `enum`
* Default Value: `NOTICE`

#### `mroonga_match_escalation_threshold`

* Description: The threshold to determine whether the match method is escalated. `-1` means never escalate.
* Command line: `--mroonga-match-escalation-threshold=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `0`
* Range: `-1` to `9223372036854775807`

#### `mroonga_max_n_records_for_estimate`

* Description: The max number of records to estimate the number of matched records
* Command line: `--mroonga-max-n-records-for-estimate=#`
* Scope: Global, Session
* Dynamic: Yes
* Data Type: `numeric`
* Default Value: `1000`
* Range: `-1` to `2147483647`

#### `mroonga_query_log_file`

* Description: Query log file for Mroonga.
* Command line: `--mroonga-query-log-file=filename`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: (Empty string)
* Introduced: [MariaDB 10.2.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.11)

#### `mroonga_vector_column_delimiter`

* Description: Delimiter to use when outputting a vector column. The default is a white space.
* Command line: `--mroonga-vector-column-delimiter=value`
* Scope: Global
* Dynamic: Yes
* Data Type: `string`
* Default Value: \`\` (white space)

#### `mroonga_version`

* Description: Mroonga version
* Command line: None
* Scope: Global
* Dynamic: No
* Data Type: `string`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
