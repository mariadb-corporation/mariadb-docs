# MaxScale Query Log All Filter

## Overview

The Query Log All (QLA) filter logs query content. Logs are written to a file in
CSV format, or to [Kafka](https://kafka.apache.org/). Log elements are
configurable and include the time submitted and the SQL statement text, among
others.

## Configuration

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

## Log Rotation

The `qlafilter` logs can be rotated by executing the `maxctrl rotate logs`
command. This will cause the log files to be reopened when the next message is
written to the file. This applies to both unified and session type logging.

## Settings

The QLA filter has one mandatory parameter, `filebase`, and a number of optional
parameters. These were introduced in the 1.0 release of MariaDB MaxScale.

### `filebase`

* Type: string
* Mandatory: Yes
* Dynamic: No

The basename of the output file created for each session. A session index is
added to the filename for each written session file. For unified log files,_.unified_ is appended.

```
filebase=/tmp/SqlQueryLog
```

### `match`

* Type: [regex](../../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

Include queries that match the regex.

### `exclude`

* Type: [regex](../../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes
* Default: None

Exclude queries that match the regex.

### `options`

* Type: [enum\_mask](../../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `case`, `ignorecase`, `extended`
* Default: `case`

The `extended` option enables PCRE2 extended regular expressions.

### `user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Limit logging to sessions with this user.

### `source`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Limit logging to sessions with this client source address.

### `user_match`

* Type: [regex](../../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

Only log queries from users that match this pattern. If the `user` parameter is
used, the value of `user_match` is ignored.

Here is an example pattern that matches the users `alice` and `bob`:

```
user_match=/(^alice$)|(^bob$)/
```

### `user_exclude`

* Type: [regex](../../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

Exclude all queries from users that match this pattern. If the `user` parameter
is used, the value of `user_exclude` is ignored.

Here is an example pattern that excludes the users `alice` and `bob`:

```
user_exclude=/(^alice$)|(^bob$)/
```

### `source_match`

* Type: [regex](../../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

Only log queries from hosts that match this pattern. If the `source` parameter
is used, the value of `source_match` is ignored.

Here is an example pattern that matches the loopback interface as well as the
address `192.168.0.109`:

```
source_match=/(^127[.]0[.]0[.]1)|(^192[.]168[.]0[.]109)/
```

### `source_exclude`

* Type: [regex](../../maxscale-management/deployment/maxscale-configuration-guide.md#regular-expressions)
* Mandatory: No
* Dynamic: Yes

Exclude all queries from hosts that match this pattern. If the `source`
parameter is used, the value of `source_exclude` is ignored.

Here is an example pattern that excludes the loopback interface as well as the
address `192.168.0.109`:

```
source_exclude=/(^127[.]0[.]0[.]1)|(^192[.]168[.]0[.]109)/
```

### `log_type`

* Type: [enum\_mask](../../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `session`, `unified`, `stdout`, `kafka`
* Default: `session`

The type of log file to use.

| Value   | Description                     |
| ------- | ------------------------------- |
| session | Write to session-specific files |
| unified | Use one file for all sessions   |
| stdout  | Same as unified, but to stdout  |
| kafka   | Send log events to Kafka        |

If you enable Kafka logging, you need to also configure
[Kafka bootstrap servers](#kafka_bootstrap_servers) and [topic](#kafka_topic).
Depending on the Kafka broker configuration, the various other [Kafka
settings](#kafka-settings) may also be required.

When Kafka logging is enabled, MaxScale attempts to send query events to the
Kafka broker. If the Kafka event production fails for any reason, MaxScale will
simply log the error to the MaxScale general log and continue.  The Kafka
messages MaxScale sends always contain the client session id as message key. If
`log_data` includes `session`, then the session is also included in the message
text. Kafka message timestamps match the time MaxScale receives the query from
the client.

### `log_data`

* Type: [enum\_mask](../../maxscale-management/deployment/maxscale-configuration-guide.md#enumerations)
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
| query              | The SQL of the query if it contains it                  |
| default\_db        | The default (current) database                          |
| num\_rows          | Number of rows in the result set (v6.2)                 |
| reply\_size        | Number of bytes received from the server (v6.2)         |
| transaction        | BEGIN, COMMIT and ROLLBACK (v6.2)                       |
| transaction\_time  | The duration of a transaction (v6.2)                    |
| num\_warnings      | Number of warnings in the server reply (v6.2)           |
| error\_msg         | Error message from the server (if any) (v6.2)           |
| server             | The server where the query was routed (if any) (v22.08) |
| command            | The protocol command that was executed (v24.02)         |

The durations _reply\_time_ and _total\_reply\_time_ are by default in milliseconds,
but can be specified to another unit using _duration\_unit_.

The log entry is written when the last reply from the server is received.
Prior to version 6.2 the entry was written when the query was received from
the client, or if _reply\_time_ was specified, on first reply from the server.

If you enable SQL query logging, the log entries contain the entire SQL
query. If the queries themselves are large (e.g. inserts with thousands of
elements), the log entries end up equally long. This can cause slowdown and high
disk space usage on the MaxScale host.

{% tabs %}
{% tab title="Current" %}
The filter limits the length of the logged query to 1024 characters by
default. Queries longer than the limit are only partially logged. See
[logged_query_max_length](#logged_query_max_length) for more information.
{% endtab %}

{% tab title="< 26.10" %}
The filter does not limit the length of the logged query.
{% endtab %}
{% endtabs %}

**NOTE** The _error\_msg_ is the raw message from the server. Even if _use\_canonical\_form_
is set the error message may contain user defined constants. For example:

```
MariaDB [test]> select secret from T where x password="clear text pwd";
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual
that corresponds to your MariaDB server version for the right syntax to
use near 'password="clear text pwd"' at line 1
```

Starting with MaxScale 24.02, the `query` parameter now correctly logs
the execution of binary protocol commands as SQL
([MXS-4959](https://jira.mariadb.org/browse/MXS-4959)). The execution of
batched statements (COM\_STMT\_BULK\_LOAD) used by some connectors is not
logged.

### `duration_unit`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `milliseconds`

The unit for logging a duration. The unit can be `milliseconds` or `microseconds`.
The abbreviations `ms` for milliseconds and `us` for microseconds are also valid.
This option is available as of MaxScale version 6.2.

### `use_canonical_form`

* Type: [bool](../../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

When this option is true the canonical form of the query is logged. In the
canonical form all user defined constants are replaced with question marks.
This option is available as of MaxScale version 6.2.

### `flush`

* Type: [bool](../../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

Flush log files after every write.

### `append`

* Type: [bool](../../maxscale-management/deployment/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `true`

### `separator`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `","`

Defines the separator string between elements of
log entries. The value should be enclosed in quotes.

### `newline_replacement`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `" "`

Default value is `" "` (one space). SQL-queries may include line breaks, which, if
printed directly to the log, may break automatic parsing. This parameter defines
what should be written in the place of a newline sequence (\r, \n or \r\n). If
this is set as the empty string, then newlines are not replaced and printed as
is to the output. The value should be enclosed in quotes.

```
newline_replacement=" NL "
```

### `logged_query_max_length`

* Type: count
* Mandatory: No
* Dynamic: Yes
* Default: `1024`

Limits the length of the logged SQL query when `log_data` includes `query`. If
`logged_query_max_length` is set to N, the filter only logs up to N characters
of any query. If `newline_replacement` is enabled, as it is by default, the
length limit takes effect before the filter replaces newlines. This means that
the final length of the logged query may be greater than N. This deviation
depends on the number of newlines in the query and the length of the value of
`newline_replacement`.

Use this setting to ensure that large queries do not cause the log file to
consume too much space. Setting `logged_query_max_length=0` removes the length
limit, causing the filter to always log the entire query.

{% tabs %}
{% tab title="< 26.10" %}
This feature is only available in MaxScale 26.10.0 and later.
{% endtab %}
{% endtabs %}

```
logged_query_max_length=100
```

### Kafka settings

These settings resemble the equivalent settings in the
[KafkaCDC Router](../maxscale-routers/maxscale-kafkacdc.md#settings). Although
these settings can be modified during runtime, this is typically ill-advised, as
any modifications only affect new client sessions. Define at least
`kafka_bootstrap_servers` and `kafka_topic` when logging events to Kafka. Kafka
logging only activates when the value of `log_type` includes `kafka`.

#### `kafka_bootstrap_servers`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

The list of Kafka brokers to use in `host:port` format. Multiple values can be
separated with commas.

```
kafka_bootstrap_servers=127.0.0.1:9092
```

#### `kafka_topic`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

The Kafka topic where the log events are published.

```
kafka_topic=maxscale_qlalogs
```

#### `kafka_enable_idempotence`

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

Enable idempotent producer mode. This feature requires Kafka version 0.11 or
newer to work. When enabled, the Kafka producer enters a strict mode which
avoids event duplication due to broker outages or other network errors.

#### `kafka_ssl`

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`

Enable SSL for Kafka connections.

#### `kafka_ssl_ca`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Path to the certificate authority file in PEM format. If this is not provided,
the default system certificates will be used.

#### `kafka_ssl_cert`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Path to the public certificate in PEM format. The client must provide a
certificate if the Kafka server performs authentication of the client
certificates. This feature is enabled by default in Kafka and is controlled by
[ssl.endpoint.identification.algorithm](https://kafka.apache.org/documentation/#brokerconfigs_ssl.endpoint.identification.algorithm).

If `kafka_ssl_cert` is provided, `kafka_ssl_key` must also be provided.

#### `kafka_ssl_key`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Path to the private key in PEM format. If `kafka_ssl_key` is provided,
`kafka_ssl_cert` must also be provided.

#### `kafka_sasl_user`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Username for SASL authentication. If `kafka_sasl_user` is provided,
`kafka_sasl_password` must also be provided.

#### `kafka_sasl_password`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`

Password for SASL authentication. If `kafka_sasl_password` is provided,
`kafka_sasl_user` must also be provided.

#### `kafka_sasl_mechanism`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `PLAIN`, `SCRAM-SHA-256`, `SCRAM-SHA-512`
* Default: `PLAIN`

The SASL mechanism used. The default value `PLAIN` uses plaintext
authentication. You should enable SSL whenever plaintext authentication is
used. The value that should be used depends on the SASL mechanism used by the
Kafka broker.

## Limitations

* Trailing parts of SQL queries that are larger than 16MiB are not
  logged. This means that the log output might contain truncated SQL.
* Batched execution using COM\_STMT\_BULK\_EXECUTE is not converted into
  their textual form. This is done due to the large volumes of data that
  are usually involved with batched execution.

## Examples

### Example 1 - Query without primary key

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
be a log file of all select queries querying PRODUCTS without using the
PRODUCT\_ID primary key in the predicates of the query. Executing `SELECT * FROM PRODUCTS` would log the following into `/var/logs/qla/SelectProducts`:

```
07:12:56.324 7/01/2016, SELECT * FROM PRODUCTS
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
