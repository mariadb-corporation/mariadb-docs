---
description: >-
  Reference for MariaDB Connector/C types and definitions, including
  enumeration constants for field types, statement options, cursor types,
  indicator types, field flags, and server status.
---

# MariaDB Connector/C Types and Definitions

MariaDB Connector/C provides the following types and definitions.

### Enumeration Types

#### enum mysql\_option

`enum mysql_option` is used as a parameter in [mysql\_optionsv()](api-functions/mysql_optionsv.md) and [mysql\_get\_optionsv()](api-functions/mysql_get_optionv.md) API functions. For a list of integral constants and their meanings, please check the documentation of [mysql\_get\_optionsv()](api-functions/mysql_get_optionv.md).

#### enum enum\_mysql\_timestamp\_type

`enum enum_mysql_timestamp_type` is used in the `MYSQL_TIME` structure and indicates the type. It has the following constants:

* `MYSQL_TIMESTAMP_NONE`
* `MYSQL_TIMESTAMP_ERROR`
* `MYSQL_TIMESTAMP_DATE`
* `MYSQL_TIMESTAMP_DATETIME`
* `MYSQL_TIMESTAMP_TIME`

#### enum mysql\_set\_option

`enum mysql_set_option` is used as a parameter in [mysql\_set\_server\_option()](api-functions/mysql_set_server_option.md) and has the following constants:

* `MYSQL_OPTIONS_MULTI_STATEMENTS_ON`
* `MYSQL_OPTIONS_MULTI_STATEMENTS_OFF`

#### enum enum\_field\_types

`enum field_types` describes the different field types used by MariaDB and has the following constants:

* `MYSQL_TYPE_DECIMAL`
* `MYSQL_TYPE_TINY`
* `MYSQL_TYPE_SHORT`
* `MYSQL_TYPE_LONG`
* `MYSQL_TYPE_FLOAT`
* `MYSQL_TYPE_DOUBLE`
* `MYSQL_TYPE_NULL`
* `MYSQL_TYPE_TIMESTAMP`
* `MYSQL_TYPE_LONGLONG`
* `MYSQL_TYPE_INT24`
* `MYSQL_TYPE_DATE`
* `MYSQL_TYPE_TIME`
* `MYSQL_TYPE_DATETIME`
* `MYSQL_TYPE_YEAR`
* `MYSQL_TYPE_NEWDATE`
* `MYSQL_TYPE_VARCHAR`
* `MYSQL_TYPE_BIT`
* `MYSQL_TYPE_TIMESTAMP2`
* `MYSQL_TYPE_DATETIME2`
* `MYSQL_TYPE_TIME2`
* `MYSQL_TYPE_JSON`
* `MYSQL_TYPE_NEWDECIMAL`
* `MYSQL_TYPE_ENUM`
* `MYSQL_TYPE_SET`
* `MYSQL_TYPE_TINY_BLOB`
* `MYSQL_TYPE_MEDIUM_BLOB`
* `MYSQL_TYPE_LONG_BLOB`
* `MYSQL_TYPE_BLOB`
* `MYSQL_TYPE_VAR_STRING`
* `MYSQL_TYPE_STRING`
* `MYSQL_TYPE_GEOMETRY`

#### enum mysql\_enum\_shutdown\_level

`enum mysql_enum_shutdown_level` is used as a parameter in [mysql\_server\_shutdown()](api-functions/mysql_server_end.md) and has the following constants:

* `SHUTDOWN_DEFAULT`
* `KILL_QUERY`
* `KILL_CONNECTION`

#### enum enum\_stmt\_attr\_type

`enum_stmt_attr_type` is used to set different statement options. For a detailed description please check [mysql\_stmt\_attr\_set()](api-prepared-statement-functions/mysql_stmt_attr_set.md) function.

#### enum enum\_cursor\_type

`enum_cursor_type` specifies the cursor type and is used in [mysql\_stmt\_attr\_set()](api-prepared-statement-functions/mysql_stmt_attr_set.md) function. Currently the following constants are supported:

* `CURSOR_TYPE_READ_ONLY`
* `CURSOR_TYPE_NO_CURSOR`

#### enum enum\_indicator\_type

`enum_indicator_type` describes the type of indicator used for prepared statements bulk operations.

|                             |                            |
| --------------------------- | -------------------------- |
| `STMT_INDICATOR_NTS`        | String is zero terminated  |
| `STMT_INDICATOR_NONE`       | No indicator in use        |
| `STMT_INDICATOR_NULL`       | Value is NULL              |
| `STMT_INDICATOR_DEFAULT`    | Use default value          |
| `STMT_INDICATOR_IGNORE`     | Ignore the specified value |
| `STMT_INDICATOR_IGNORE_ROW` | Skip the current row       |

### Definitions

#### Field Flags

The following field flags are used in [MYSQL\_FIELD](mariadb-connectorc-data-structures.md) structure.

<table><thead><tr><th></th><th width="89"></th><th></th></tr></thead><tbody><tr><td>Flag</td><td>Value</td><td>Description</td></tr><tr><td><code>NOT_NULL_FLAG</code></td><td>1</td><td>Field can't be NULL</td></tr><tr><td><code>PRI_KEY_FLAG</code></td><td>2</td><td>Field is part of primary key</td></tr><tr><td><code>UNIQUE_KEY_FLAG</code></td><td>4</td><td>Field is part of unique key</td></tr><tr><td><code>MULTIPLE_KEY_FLAG</code></td><td>8</td><td>Field is part of a key</td></tr><tr><td><code>BLOB_FLAG</code></td><td>16</td><td>Field is a blob</td></tr><tr><td><code>UNSIGNED_FLAG</code></td><td>32</td><td>Field is unsigned integer</td></tr><tr><td><code>ZEROFILL_FLAG</code></td><td>64</td><td>Field is zero filled</td></tr><tr><td><code>BINARY_FLAG</code></td><td>128</td><td>Field is binary</td></tr><tr><td><code>ENUM_FLAG</code></td><td>256</td><td>Field is enum</td></tr><tr><td><code>AUTO_INCREMENT_FLAG</code></td><td>512</td><td>Field is an autoincrement field</td></tr><tr><td><code>TIMESTAMP_FLAG</code></td><td>1024</td><td>Field is a timestamp</td></tr><tr><td><code>SET_FLAG</code></td><td>2048</td><td>Field is a set</td></tr><tr><td><code>NO_DEFAULT_VALUE_FLAG</code></td><td>4096</td><td>Field has no default value</td></tr><tr><td><code>ON_UPDATE_NOW_FLAG</code></td><td>8192</td><td>If a field is updated it will get the current time value (NOW())</td></tr><tr><td><code>NUM_FLAG</code></td><td>32768</td><td>Field is numeric</td></tr></tbody></table>

#### Server Status

The server\_status can be obtained by the [mariadb\_get\_infov()](api-functions/mariadb_get_infov.md) function using the `MARIADB_CONNECTION_SERVER_STATUS` option.

<table><thead><tr><th></th><th width="91"></th><th></th></tr></thead><tbody><tr><td><code>SERVER_STATUS_IN_TRANS</code></td><td>1</td><td>A transaction is currently active</td></tr><tr><td><code>SERVER_STATUS_AUTOCOMMIT</code></td><td>2</td><td>Autocommit mode is set</td></tr><tr><td><code>SERVER_MORE_RESULTS_EXISTS</code></td><td>8</td><td>more results exists (more packet follow)</td></tr><tr><td><code>SERVER_QUERY_NO_GOOD_INDEX_USED</code></td><td>16</td><td></td></tr><tr><td><code>SERVER_QUERY_NO_INDEX_USED</code></td><td>32</td><td></td></tr><tr><td><code>SERVER_STATUS_CURSOR_EXISTS</code></td><td>64</td><td>when using <code>COM_STMT_FETCH</code>, indicate that current cursor still has result</td></tr><tr><td><code>SERVER_STATUS_LAST_ROW_SENT</code></td><td>128</td><td>when using <code>COM_STMT_FETCH</code>, indicate that current cursor has finished to send results</td></tr><tr><td><code>SERVER_STATUS_DB_DROPPED</code></td><td>1&#x3C;&#x3C;8</td><td>database has been dropped</td></tr><tr><td><code>SERVER_STATUS_NO_BACKSLASH_ESCAPES</code></td><td>1&#x3C;&#x3C;9</td><td>current escape mode is "no backslash escape"</td></tr><tr><td><code>SERVER_STATUS_METADATA_CHANGED</code></td><td>1&#x3C;&#x3C;10</td><td>A DDL change did have an impact on an existing PREPARE (an automatic reprepare has been executed)</td></tr><tr><td><code>SERVER_QUERY_WAS_SLOW</code></td><td>1&#x3C;&#x3C;11</td><td>Last statement took more than the time value specified in server variable <code>long_query_time</code>.</td></tr><tr><td><code>SERVER_PS_OUT_PARAMS</code></td><td>1&#x3C;&#x3C;12</td><td>this <code>resultset</code> contain stored procedure output parameter</td></tr><tr><td><code>SERVER_STATUS_IN_TRANS_READONLY</code></td><td>1&#x3C;&#x3C;13</td><td>current transaction is a read-only transaction</td></tr><tr><td><code>SERVER_SESSION_STATE_CHANGED</code></td><td>1&#x3C;&#x3C;14</td><td>session state change. see Session change type for more information</td></tr></tbody></table>

#### Macros

|                            |                                            |
| -------------------------- | ------------------------------------------ |
| `IS_PRI_KEY(flag)`         | True if the field is part of a primary key |
| `IS_NOT_NULL(flags)`       | True if the field is defined as not NULL   |
| `IS_BLOB(flags)`           | True if the field is a text or blob field  |
| `IS_NUM(column_type)`      | True if the column type is numeric         |
| `IS_LONGDATA(column_type)` | True if the column is a blob or text field |

{% @marketo/form formId="4316" %}
