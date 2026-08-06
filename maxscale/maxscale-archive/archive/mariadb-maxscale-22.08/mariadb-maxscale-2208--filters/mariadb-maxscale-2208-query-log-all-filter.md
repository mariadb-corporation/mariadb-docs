# MaxScale 22.08 Query Log All Filter

## Query Log All Filter

## Query Log All Filter

### Overview

The Query Log All (QLA) filter logs query content. Logs are written to a file in\
CSV format. Log elements are configurable and include the time submitted and the\
SQL statement text, among others.

### Configuration

A minimal configuration is below.

```
[MyLogFilter]
type=filter
module=qlafilter
filebase=/tmp/SqlQueryLog

[MyService]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=MyLogFilter
```

### Log Rotation

The `qlafilter` logs can be rotated by executing the `maxctrl rotate logs`
command. This will cause the log files to be reopened when the next message is
written to the file. This applies to both unified and session type logging.

### Filter Parameters

The QLA filter has one mandatory parameter, `filebase`, and a number of optional
parameters. These were introduced in the 1.0 release of MariaDB MaxScale.

#### `filebase`

* Type: string
* Mandatory: Yes
* Dynamic: No

The basename of the output file created for each session. A session index is
added to the filename for each written session file. For unified log files,_.unified_ is appended.

```
filebase=/tmp/SqlQueryLog
```

#### `match`

* Type: [regex](../mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

Include queries that match the regex.

#### `exclude`

* Type: [regex](../mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

Exclude queries that match the regex.

#### `options`

* Type: [enum\_mask](../mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`

The `extended` option enables PCRE2 extended regular expressions.

#### `user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Limit logging to sessions with this user.

#### `source`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Limit logging to sessions with this client source address.

#### `log_type`

* Type: [enum\_mask](../mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`
* Default: `session`

The type of log file to use.

| Value   | Description                     |
| ------- | ------------------------------- |
| session | Write to session-specific files |
| unified | Use one file for all sessions   |
| stdout  | Same as unified, but to stdout  |

#### `log_data`

* Type: [enum\_mask](../mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `service`, `session`, `date`, `user`, `reply_time`, `total_reply_time`, `query`, `default_db`, `num_rows`, `reply_size`, `transaction`, `transaction_time`, `num_warnings`, `error_msg`
* Default: `date, user, query`

Type of data to log in the log files.

| Value              | Description                                             |
| ------------------ | ------------------------------------------------------- |
| service            | Service name                                            |
| session            | Unique session id (ignored for session files)           |
| date               | Timestamp                                               |
| user               | User and hostname of client                             |
| reply\_time        | Duration from client query to first server reply        |
| total\_reply\_time | Duration from client query to last server reply (v6.2)  |
| query              | Query                                                   |
| default\_db        | The default (current) database                          |
| num\_rows          | Number of rows in the result set (v6.2)                 |
| reply\_size        | Number of bytes received from the server (v6.2)         |
| transaction        | BEGIN, COMMIT and ROLLBACK (v6.2)                       |
| transaction\_time  | The duration of a transaction (v6.2)                    |
| num\_warnings      | Number of warnings in the server reply (v6.2)           |
| error\_msg         | Error message from the server (if any) (v6.2)           |
| server             | The server where the query was routed (if any) (v22.08) |

The durations _reply\_time_ and _total\_reply\_time_ are by default in milliseconds,
but can be specified to another unit using _duration\_unit_.

The log entry is written when the last reply from the server is received.\
Prior to version 6.2 the entry was written when the query was received from
the client, or if _reply\_time_ was specified, on first reply from the server.

**NOTE** The _error\_msg_ is the raw message from the server. Even if _use\_canonical\_form_
is set the error message may contain user defined constants. For example:

```
MariaDB [test]> select secret from T where x password="clear text pwd";
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual
that corresponds to your MariaDB server version for the right syntax to
use near 'password="clear text pwd"' at line 1
```

#### `duration_unit`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`

The unit for logging a duration. The unit can be `milliseconds` or `microseconds`.\
The abbreviations `ms` for milliseconds and `us` for microseconds are also valid.\
This option is available as of MaxScale version 6.2.

#### `use_canonical_form`

* Type: [bool](../mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

When this option is true the canonical form of the query is logged. In the
canonical form all user defined constants are replaced with question marks.\
This option is available as of MaxScale version 6.2.

#### `flush`

* Type: [bool](../mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

Flush log files after every write.

#### `append`

* Type: [bool](../mariadb-maxscale-2208-getting-started/mariadb-maxscale-2208-mariadb-maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

#### `separator`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`

Defines the separator string between elements of
log entries. The value should be enclosed in quotes.

#### `newline_replacement`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`

Default value is `" "` (one space). SQL-queries may include line breaks, which, if
printed directly to the log, may break automatic parsing. This parameter defines
what should be written in the place of a newline sequence (\r, \n or \r\n). If
this is set as the empty string, then newlines are not replaced and printed as
is to the output. The value should be enclosed in quotes.

### Examples

#### Example 1 - Query without primary key

Imagine you have observed an issue with a particular table and you want to
determine if there are queries that are accessing that table but not using the
primary key of the table. Let's assume the table name is PRODUCTS and the
primary key is called PRODUCT\_ID. Add a filter with the following definition:

```
[ProductsSelectLogger]
type=filter
module=qlafilter
match=SELECT.*from.*PRODUCTS .*
exclude=WHERE.*PRODUCT_ID.*
filebase=/var/logs/qla/SelectProducts

[Product-Service]
type=service
router=readconnroute
servers=server1
user=myuser
password=mypasswd
filters=ProductsSelectLogger
```

The result of using this filter with the service used by the application would
be a log file of all select queries querying PRODUCTS without using the\
PRODUCT\_ID primary key in the predicates of the query. Executing `SELECT * FROM PRODUCTS` would log the following into `/var/logs/qla/SelectProducts`:

```
07:12:56.324 7/01/2016, SELECT * FROM PRODUCTS
```

CC BY-SA / Gnu FDL
