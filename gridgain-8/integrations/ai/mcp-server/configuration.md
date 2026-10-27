---
description: >-
  Settings of GridGain MCP Server: cluster connection, timeouts and retries, result limits, rate limit, audit log, and TLS, each as an environment variable and a flag.
---

# Configuring MCP Server

You configure GridGain MCP Server with environment variables or command-line flags.
Every setting has both forms. The following commands set the same cluster address:

```shell
GRIDGAIN_HOST=db.example.com java -jar gridgain-mcp-<version>.jar
java -jar gridgain-mcp-<version>.jar --host db.example.com
```

{% hint style="warning" %}
Pass the user name, the password, and the store passwords through environment variables.
Other users of the machine can see command-line arguments.
{% endhint %}

## How Settings are Applied

The server reads its settings when it starts. To apply a change, restart the server.

A flag overrides the environment variable, and the environment variable overrides the default.

You can write a flag in two ways, such as `--host db.example.com` or `--host=db.example.com`.
If a value starts with `--`, use the form with the equals sign.

Numbers are whole decimal numbers without spaces.
The values `true` and `false` are not case sensitive.

### Invalid Settings

The server does not start if the configuration has any of the following:

- A value that is not valid. The server does not replace it with the default.
- An unknown flag or an unexpected argument.
- A flag without a value.
- A flag that you set twice with different values.

The server then exits with code `2` and prints the error to standard error.
The message names the setting and the reason, but not the value.
For an unknown flag or an unexpected argument, the message is `arguments: unsupported argument` and does not name the flag.

## Cluster Connection

The connection settings tell the server which cluster to connect to and which account to use.
Use a dedicated read-only account, as described in [Preparing a Cluster Account](security.md#preparing-a-cluster-account).

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `GRIDGAIN_HOST` | `--host` | `localhost` | The cluster address. To give several addresses, separate them with commas. See [Address Format](#address-format). |
| `GRIDGAIN_PORT` | `--port` | `10800` | The port for the addresses that have no port of their own. Accepted values: `1` to `65535`. |
| `GRIDGAIN_USERNAME` | `--username` | None | The user name. It must not be blank. Set it together with the password. |
| `GRIDGAIN_PASSWORD` | `--password` | None | The password. It can be empty. Set it together with the user name. |

The server connects only to the addresses that you list. It does not look for other cluster nodes.

### Address Format

Each address in `GRIDGAIN_HOST` has one of the following forms:

| Form | Example |
| ---- | ------- |
| Host name or IP address | `db1.example.com` |
| Host and port | `db1.example.com:10800` |
| Host and port range | `db1.example.com:10800..10810` |
| IPv6 address, with or without a port | `[2001:db8::1]:10800` |

The following value lists two nodes:

```shell
GRIDGAIN_HOST=db1.example.com:10800,db2.example.com:10800
```

The server removes spaces around each address.
It ignores empty entries at the end of the list, such as in `db1,db2,,`.
The following are errors:

- An entry that contains only spaces, even at the end of the list.
- Any other empty entry.
- An empty host or port.
- A port outside the range `1` to `65535`.

The server does not check the host names until it connects.

## Timeouts and Retries

The server does not connect when it starts.
It connects when the assistant first uses a tool that needs the cluster.
It keeps the connection until the connection is lost or a request times out.
The timeout and retry settings control how long the server waits for the cluster at each step.

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `MCP_CONNECTION_TIMEOUT` | `--connection-timeout` | `20000` | The time in milliseconds to wait for a connection to a cluster node. Accepted values: `1` to `2147483647`. |
| `MCP_OPERATION_TIMEOUT` | `--operation-timeout` | `30000` | The time in milliseconds after which the cluster cancels a query. It is also the longest time that a call waits for a free worker. Accepted values: `1` to `2147483647`. |
| `MCP_HEARTBEAT_ENABLED` | `--heartbeat-enabled` | `true` | Whether the server sends heartbeat messages to keep an idle connection open. Accepted values: `true` or `false`. |
| `MCP_HEARTBEAT_INTERVAL` | `--heartbeat-interval` | `30000` | The time in milliseconds between heartbeat messages. Accepted values: `1` or more. |
| `MCP_RETRY_ATTEMPTS` | `--retry-attempts` | `6` | The number of times the server repeats a failed connection attempt. Use `0` to try only once. |
| `MCP_RETRY_DELAY` | `--retry-delay` | `500` | The upper limit in milliseconds for the pause before the first repeated attempt. |
| `MCP_RETRY_MAX_DELAY` | `--retry-max-delay` | `16000` | The largest value in milliseconds that the pause limit can grow to. It must not be less than `MCP_RETRY_DELAY`. |

The server waits for an answer to a request for `MCP_OPERATION_TIMEOUT` plus `MCP_CONNECTION_TIMEOUT`.

### Repeated Connection Attempts

The server repeats a connection attempt only when it cannot reach a node:

- The connection is refused.
- The host name cannot be resolved.
- The connection times out.
- A node accepts the connection, but the handshake times out.

Other failures, such as wrong credentials or a TLS error, end the attempt at once.

Before each repeated attempt, the server pauses for a random time.
The upper limit for the pause starts at `MCP_RETRY_DELAY` and doubles after every attempt, up to `MCP_RETRY_MAX_DELAY`.

{% hint style="warning" %}
With the default settings, a tool call can wait for minutes if the network drops packets to the cluster.
For one address, the call waits almost 3 minutes. Each additional address adds 20 seconds per attempt.
If the connection is refused or the host name cannot be resolved, the call fails within about 30 seconds.
To get an error sooner, lower `MCP_RETRY_ATTEMPTS`.
{% endhint %}

## Result Limits

The result limits restrict how much data a tool returns to the assistant.
They do not reduce the work that the cluster does for a query.

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `MCP_MAX_ROWS` | `--max-rows` | `1000` | The largest number of rows that a tool returns in one result. Accepted values: `1` to `100000`. |
| `MCP_MAX_RESPONSE_BYTES` | `--max-response-bytes` | `102400` | The largest size in bytes of one tool result. Accepted values: `1024` to `2147483647`. |

The server returns each result twice, as structured data and as text, and counts both toward `MCP_MAX_RESPONSE_BYTES`.
For details, see [Result Limits](tools-and-resources.md#result-limits).

## Concurrent Calls

The server runs a limited number of tool calls at the same time and queues the others.

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `MCP_MAX_CONCURRENT_QUERIES` | `--max-concurrent-queries` | `4` | The number of tool calls that run at the same time. Accepted values: `1` to `64`. |

When more calls arrive than `MCP_MAX_CONCURRENT_QUERIES` allows, up to 128 more calls wait in a queue.
A call fails if it waits longer than `MCP_OPERATION_TIMEOUT`, or at once if the queue is full.
The SQL tools and `check_database_connection` report these failures with the `TIMEOUT` and `BUSY` codes.
The tools that list objects return an error text without a code.

## Rate Limit

The rate limit protects the cluster from an assistant that calls a tool in a loop.

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `MCP_RATE_LIMIT_ENABLED` | `--rate-limit-enabled` | `true` | Whether the rate limit is on. Accepted values: `true` or `false`. |
| `MCP_RATE_LIMIT_DEFAULT_PER_MINUTE` | `--rate-limit-default-per-minute` | `100` | The number of calls per minute that each tool allows. Accepted values: `1` to `2147483647`. |

For details, see [Rate Limit](operations.md#rate-limit).

## Audit Log

The server records each tool call in an audit log file.
The log does not contain passwords or query results.

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `MCP_AUDIT_ENABLED` | `--audit-enabled` | `true` | Whether the server writes the audit log. Accepted values: `true` or `false`. |
| `MCP_AUDIT_LOG_PATH` | `--audit-log-path` | `~/.gridgain8/mcp/logs/audit.log` | The audit log file. A leading `~/` stands for the home folder of the user who runs the server. |
| `MCP_AUDIT_MAX_FILE_SIZE_MB` | `--audit-max-file-size-mb` | `100` | The file size in MiB at which the server starts a new log file. Accepted values: `1` to `2147483647`. |
| `MCP_AUDIT_RETENTION_DAYS` | `--audit-retention-days` | `90` | The number of days to keep old log files. Accepted values: `1` to `2147483647`. |

For details, see [Audit Log](operations.md#audit-log).

## TLS

The TLS settings encrypt the connection between the server and the cluster.
The cluster must accept TLS connections from thin clients. See [SSL/TLS](../../../security/ssl-tls.md).

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `GRIDGAIN_SSL_MODE` | `--ssl-mode` | `DISABLED` | Whether to encrypt the connection. Accepted values: `DISABLED` or `REQUIRED`. |
| `GRIDGAIN_SSL_PROTOCOL` | `--ssl-protocol` | `TLS` | The protocol. Accepted values: `TLS`, `TLSv1`, `TLSv1_1`, `TLSv1_2`, or `TLSv1_3`. |
| `GRIDGAIN_SSL_TRUSTSTORE_PATH` | `--ssl-truststore-path` | None | The trust store file. Set it together with the trust store password. |
| `GRIDGAIN_SSL_TRUSTSTORE_PASSWORD` | `--ssl-truststore-password` | None | The trust store password. It can be empty. |
| `GRIDGAIN_SSL_TRUSTSTORE_TYPE` | `--ssl-truststore-type` | `JKS` | The trust store format. Accepted values: `JKS` or `PKCS12`. |
| `GRIDGAIN_SSL_KEYSTORE_PATH` | `--ssl-keystore-path` | None | The key store file with the client certificate, for mutual TLS. Set it together with the key store password. |
| `GRIDGAIN_SSL_KEYSTORE_PASSWORD` | `--ssl-keystore-password` | None | The key store password. The server also uses it to open the private key. |
| `GRIDGAIN_SSL_KEYSTORE_TYPE` | `--ssl-keystore-type` | `JKS` | The key store format. Accepted values: `JKS` or `PKCS12`. |

The values of the mode, the protocol, and the store types are not case sensitive.

### Store Checks

The server checks the stores before it starts. It does not start in the following cases:

- `GRIDGAIN_SSL_MODE` is `REQUIRED`, and no trust store is set.
- A store is set, and `GRIDGAIN_SSL_MODE` is `DISABLED`.
- A store file cannot be read, is not of the declared type, or does not open with its password.
- The trust store has no certificates.
- The key store has no private key with a certificate, or a key in it does not open with the key store password.
- Your Java security settings disable the protocol. Java 17, for one, disables `TLSv1`.

The server ignores the `javax.net.ssl.*` Java system properties. Only the settings on this page define the stores.
