---
description: >-
  mariadb_get_infov retrieves generic or connection-specific information from a
  MariaDB Connector/C handle, accepting a value-type enum and a pointer to store
  the result.
---

# mariadb\_get\_infov

## Syntax

```c
my_bool mariadb_get_infov(MYSQL * mysql,
                      enum mariadb_value value,
                      void * arg,
                      ...);
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md). For general information which is not bound to connection this parameter might be null.
* `value` - the type of value you want to retrieve. See description below.
* `arg` - pointer to a variable for storing value of the specified option.
* `...` - variable argument list

## Description

Retrieves generic or connection specific information. Returns zero on success, non-zero if an error occurred (invalid option), This function was added in MariaDB Connector/C 3.0,

### Value types

#### Generic information

For these information types of parameters mysql needs to be set to NULL.

* `MARIADB_CHARSET_NAME`: Retrieves the charset information for a character set by its literal representation.Parameter type: `const MARIADB_CHARSET_INFO*`.
* `MARIADB_CLIENT_ERRORS`: Retrieve array of client errors. This can be used in plugins to set global error messages (which are not exported by MariaDB Connector/C).Parameter type: `const char **`.
* `MARIADB_CLIENT_VERSION`: The client version in literal representation.Parameter type: `const char *`.
* `MARIADB_CLIENT_VERSION_ID`: The client version in numeric format.Parameter type: `unsigned int`.
* `MARIADB_MAX_ALLOWED_PACKET`: Retrieves value of maximum allowed packet size.Parameter type: `size_t`
* `MARIADB_NET_BUFFER_LENGTH`: Retrieves the length of net buffer.Parameter type: `size_t`
* `MARIADB_TLS_LIBRARY`: The TLS library MariaDB Connector/C is compiled against.Parameter type: `const char *`.

#### Connection related information

* `MARIADB_CONNECTION_ASYNC_TIMEOUT`: Retrieves the timeout for non-blocking calls in seconds.Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_ASYNC_TIMEOUT_MS`: Retrieves the timeout for non-blocking calls in milliseconds.Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_MARIADB_CHARSET_INFO`: Retrieves character set information for given connection. Parameter type: `const MY_CHARSET_INFO *`.
* `MARIADB_CONNECTION_CLIENT_CAPABILITIES`: Returns the capability flags of the client.Parameter type: `unsigned long`.
* `MARIADB_CONNECTION_ERROR`: Retrieves error message for last used command. Parameter type: `const char *`.
* `MARIADB_CONNECTION_ERROR_ID`: Retrieves error number for last used command. Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_EXTENDED_SERVER_CAPABILITIES`: Returns the extended [capability flags](../../mariadb-connector-python/constants.md#capability) of the connected MariaDB server.Parameter type: `unsigned long`.
* `MARIADB_CONNECTION_HOST`: Retrieves connection's host name. Parameter type: `const char *`.
* `MARIADB_CONNECTION_INFO`: Retrieves generic info for last used command.Parameter type: `const char *`.
* `MARIADB_CONNECTION_PORT`: Retrieves the port number of server host.Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_PROTOCOL_VERSION_ID`: Retrieves the protocol version number.Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_PVIO_TYPE`: Retrieves the pvio plugin used for specified connection.Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_SCHEMA`: Retrieves the current schema.Parameter type: `const char*`.
* `MARIADB_CONNECTION_SERVER_CAPABILITIES`: Returns the [capability flags](../../mariadb-connector-python/constants.md#capability) of the connected server.Parameter type: `unsigned long`.
* `MARIADB_CONNECTION_SERVER_STATUS`: Returns server status after last operation. A list of possible flags can be found in the description OK packet.Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_SERVER_TYPE`: Retrieves the type of the server.Parameter type: `const char*`.
* `MARIADB_CONNECTION_SERVER_VERSION`: Retrieves the server version in literal format.Parameter type: `const char *`.
* `MARIADB_CONNECTION_SERVER_VERSION_ID`: Retrieves the server version in numeric format.Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_SOCKET`: Retrieves the handle (socket) for given connection.Parameter type: `my_socket`.
* `MARIADB_CONNECTION_SQLSTATE`: Retrieves current sqlstate information for last used command. Parameter type: `const char *`.
* `MARIADB_CONNECTION_SSL_CIPHER`: Retrieves the TLS cipher in use.Parameter type: `const char *`.
* `MARIADB_CONNECTION_TLS_VERSION`: Retrieves the TLS protocol version used in literal format.Parameter type: `char *`.
* `MARIADB_CONNECTION_TLS_VERSION_ID`: Retrieves the TLS protocol version used in numeric format.Parameter type: `unsigned int`.
* `MARIADB_CONNECTION_UNIX_SOCKET`: Retrieves the file name of the unix socketParameter type: `const char *`.
* `MARIADB_CONNECTION_USER`: Retrieves connection's user name.Parameter type: `const char *`.
* `MARIADB_TLS_PEER_CERT_INFO` Retrieves peer certificate information for TLS connections. The returned pointer to a MARIADB\_X509\_INFO structure becomes invalid after the connection has been closed. (Added in version 3.4.0)
* `MARIADB_TLS_VERIFY_STATUS` Retrieves the status of a previous peer certificate verification. The status is represented as a combination of [TLS verification flags](https://github.com/mariadb-corporation/mariadb-connector-c/wiki/types#tls-verification-flags). This option was added in version 3.4.1

## Return Value

Returns zero on success, non zero if an error occurred (e.g. if an invalid option was specified),

## History

This function was added in MariaDB Connector/C 3.0,

## Examples

```c
/* get server port for current connection */
unsigned int port;
mariadb_get_infov(mysql, MARIADB_CONNECTION_PORT, void *)&port);
```

```c
/* get user name for current connection */
const char *user;
mariadb_get_infov(mysql, MARIADB_CONNECTION_USER, (void *)&user);
```

## See Also

* [mysql\_get\_optionv()](mysql_get_optionv.md)

{% @marketo/form formId="4316" %}
