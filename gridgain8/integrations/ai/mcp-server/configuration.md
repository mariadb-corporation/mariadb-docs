---
description: >-
  Settings of GridGain MCP Server: cluster connection, timeouts and retries, result limits, rate limit, audit log, and TLS, each as an environment variable and a flag.
---

# Configuring MCP Server

You configure the server with environment variables or command-line flags.
Every setting has both forms. The `GRIDGAIN_HOST` variable and the `--host` flag, for instance, set the same value.

## How Settings Are Applied

- A flag overrides the environment variable. The environment variable overrides the default.
- You can write a flag as `--name value` or `--name=value`. If a value starts with `--`, use the form with the equals sign.
- An invalid value stops the server. The server never replaces it with a default.
- An unknown flag, an unexpected argument, or a flag without a value also stops the server.
- When the configuration is invalid, the server exits with code 2 and prints the error to standard error. The message names the setting and the reason, but never the value you passed.

{% hint style="warning" %}
Pass the user name, password, and store passwords through environment variables.
Command-line arguments are visible to other users of the machine.
{% endhint %}

All numbers are whole decimal numbers without spaces.

## Cluster Connection

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `GRIDGAIN_HOST` | `--host` | `localhost` | The cluster address. You can give several addresses, separated by commas. Each address can have its own port. See [Address Format](#address-format). |
| `GRIDGAIN_PORT` | `--port` | `10800` | The port used for the addresses that have no port of their own. Accepted values: 1 to 65535. |
| `GRIDGAIN_USERNAME` | `--username` | None | The user name. It must not be blank. Set it together with the password. |
| `GRIDGAIN_PASSWORD` | `--password` | None | The password. Set it together with the user name. An empty password is allowed. |

The server uses only the addresses that you list. It does not look for other nodes of the cluster.

### Address Format

Each address in `GRIDGAIN_HOST` has one of the following forms:

- `host`
- `host:port`
- `host:from..to`, a range of ports, such as `db1:10800..10810`
- `[ipv6]:port`, or an IPv6 address without a port

The server removes spaces around an address and ignores empty entries at the end of the list.
Any other empty entry, an empty host or port, and a port outside the range 1 to 65535 are errors.
The server does not check the host names until it connects.

## Timeouts and Retries

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `MCP_CONNECTION_TIMEOUT` | `--connection-timeout` | `20000` | The time in milliseconds to wait for a connection to a cluster node. Accepted values: 1 to 2147483647. |
| `MCP_OPERATION_TIMEOUT` | `--operation-timeout` | `30000` | The time in milliseconds after which the cluster cancels a query. Accepted values: 1 to 2147483647. |
| `MCP_HEARTBEAT_ENABLED` | `--heartbeat-enabled` | `true` | Whether the server sends heartbeat messages to keep an idle connection open. Accepted values: `true` or `false`. |
| `MCP_HEARTBEAT_INTERVAL` | `--heartbeat-interval` | `30000` | The time in milliseconds between heartbeat messages. Must be at least 1. |
| `MCP_RETRY_ATTEMPTS` | `--retry-attempts` | `6` | The number of repeated attempts to connect after the first one fails. Use `0` to try only once. |
| `MCP_RETRY_DELAY` | `--retry-delay` | `500` | The upper limit in milliseconds of the first pause before a repeated attempt. |
| `MCP_RETRY_MAX_DELAY` | `--retry-max-delay` | `16000` | The largest value in milliseconds to which the pause limit grows. Must not be less than `MCP_RETRY_DELAY`. |

The server does not connect when it starts.
It connects when the assistant first uses a tool that needs the cluster.
It keeps the connection until the connection is lost or a request times out.

The server repeats the connection attempt only when it cannot reach a node.
This happens when the connection is refused, the host name cannot be resolved, or the connection times out.
Before each repeated attempt, it waits for a random time.
The upper limit for this time starts at `MCP_RETRY_DELAY` and doubles after every attempt, up to `MCP_RETRY_MAX_DELAY`.
Other failures, such as wrong credentials or a TLS error, end the attempt at once.

{% hint style="warning" %}
With the default settings, an unreachable cluster can keep a tool call waiting for minutes.
Lower `MCP_RETRY_ATTEMPTS` if you want the assistant to get an error sooner.
{% endhint %}

## Result Limits

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `MCP_MAX_ROWS` | `--max-rows` | `1000` | The largest number of rows that a tool returns in one result. Accepted values: 1 to 100000. |
| `MCP_MAX_RESPONSE_BYTES` | `--max-response-bytes` | `102400` | The largest size in bytes of one tool result. Accepted values: 1024 to 2147483647. |
| `MCP_MAX_CONCURRENT_QUERIES` | `--max-concurrent-queries` | `4` | The number of tool calls that run at the same time. Accepted values: 1 to 64. |

The server counts the result size twice, because it returns each result in two forms: as structured data and as text.
For details, see [Result Limits](tools-and-resources.md#result-limits).

If more calls arrive than `MCP_MAX_CONCURRENT_QUERIES` allows, up to 128 more calls wait.
A call that waits longer than the operation timeout fails with the `TIMEOUT` code.
A call that finds the waiting line full fails at once with the `BUSY` code.

## Rate Limit and Audit Log

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `MCP_RATE_LIMIT_ENABLED` | `--rate-limit-enabled` | `true` | Whether the rate limit is on. Accepted values: `true` or `false`. |
| `MCP_RATE_LIMIT_DEFAULT_PER_MINUTE` | `--rate-limit-default-per-minute` | `100` | The number of calls per minute that each tool allows. Accepted values: 1 to 2147483647. |
| `MCP_AUDIT_ENABLED` | `--audit-enabled` | `true` | Whether the server writes the audit log. Accepted values: `true` or `false`. |
| `MCP_AUDIT_LOG_PATH` | `--audit-log-path` | `~/.gridgain8/mcp/logs/audit.log` | The audit log file. A leading `~/` stands for the home folder of the user who runs the server. |
| `MCP_AUDIT_MAX_FILE_SIZE_MB` | `--audit-max-file-size-mb` | `100` | The size in MiB at which the server starts a new log file. Accepted values: 1 to 2147483647. |
| `MCP_AUDIT_RETENTION_DAYS` | `--audit-retention-days` | `90` | The number of days to keep old log files. Accepted values: 1 to 2147483647. |

For details, see [Rate Limit](operations.md#rate-limit) and [Audit Log](operations.md#audit-log).

## TLS

| Environment variable | Flag | Default | Description |
| -------------------- | ---- | ------- | ----------- |
| `GRIDGAIN_SSL_MODE` | `--ssl-mode` | `DISABLED` | Whether to encrypt the connection. Accepted values: `DISABLED` or `REQUIRED`. |
| `GRIDGAIN_SSL_PROTOCOL` | `--ssl-protocol` | `TLS` | The protocol. Accepted values: `TLS`, `TLSv1`, `TLSv1_1`, `TLSv1_2`, or `TLSv1_3`. |
| `GRIDGAIN_SSL_TRUSTSTORE_PATH` | `--ssl-truststore-path` | None | The trust store file. Set it together with the trust store password. |
| `GRIDGAIN_SSL_TRUSTSTORE_PASSWORD` | `--ssl-truststore-password` | None | The trust store password. It can be empty. |
| `GRIDGAIN_SSL_TRUSTSTORE_TYPE` | `--ssl-truststore-type` | `JKS` | The trust store format. Accepted values: `JKS` or `PKCS12`. |
| `GRIDGAIN_SSL_KEYSTORE_PATH` | `--ssl-keystore-path` | None | The key store file with the client certificate, for mutual TLS. Set it together with the key store password. |
| `GRIDGAIN_SSL_KEYSTORE_PASSWORD` | `--ssl-keystore-password` | None | The key store password. It is also used to open the private key. |
| `GRIDGAIN_SSL_KEYSTORE_TYPE` | `--ssl-keystore-type` | `JKS` | The key store format. Accepted values: `JKS` or `PKCS12`. |

The values of the mode, the protocol, and the store types are not case-sensitive.

The server checks the stores before it starts, and refuses to start in these cases:

- `GRIDGAIN_SSL_MODE` is `REQUIRED` and no trust store is set.
- A store is set while `GRIDGAIN_SSL_MODE` is `DISABLED`.
- A store file cannot be read, is not of the declared type, or does not open with its password.
- The trust store has no certificates.
- The key store has no private key with a certificate, or a key in it does not open with the key store password.
- The protocol is disabled in your Java security settings. `TLSv1` is disabled in Java 17, for instance.

The server ignores the Java system properties `javax.net.ssl.*`. Only the settings on this page define the stores.

For more about enabling TLS on the cluster, see [SSL/TLS](../../../security/ssl-tls.md).
