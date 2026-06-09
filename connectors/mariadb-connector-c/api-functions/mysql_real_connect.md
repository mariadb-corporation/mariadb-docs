---
description: >-
  mysql_real_connect opens a connection to a MariaDB server and returns a MYSQL
  handle on success, or NULL if the connection could not be established.
---

# mysql\_real\_connect

## Syntax

```c
MYSQL * mysql_real_connect(MYSQL * mysql,
                           const char * host,
                           const char * user,
                           const char * passwd,
                           const char * db,
                           unsigned int port,
                           const char * unix_socket,
                           unsigned long flags);
```

## Parameters

* `mysql` - a `mysql` handle, which was previously allocated by [mysql\_init()](mysql_init.md).
* `host` - can be either a host name or an IP address. Passing the NULL value or the string "localhost" to this parameter, the local host is assumed. When possible, pipes will be used instead of the TCP/IP protocol.
* `user` - the user name.
* `passwd` - If provided or NULL, the server will attempt to authenticate the user against those user records which have no password only. This allows one username to be used with different permissions (depending on if a password as provided or not).
* `db` - if provided will specify the default database to be used when performing queries.
* `port` - specifies the port number to attempt to connect to the server.
* `unix_socket` - specifies the socket or named pipe that should be used.
* `flags` - the flags allows various connection options to be set:
  * `CLIENT_FOUND_ROWS`: Return the number of matched rows instead of number of changed rows.
  * `CLIENT_NO_SCHEMA`: Forbids the use of database.tablename.column syntax and forces the SQL parser to generate an error.
  * `CLIENT_COMPRESS`: Use compression protocol
  * `CLIENT_IGNORE_SPACE`: Allows spaces after function names. All function names will become reserved words.
  * `CLIENT_LOCAL_FILES`: Allows LOAD DATA LOCAL statements
  * `CLIENT_MULTI_STATEMENTS`: Allows the client to send multiple statements in one command. Statements will be divided by a semicolon.
  * `CLIENT_MULTI_RESULTS`: Indicates that the client is able to handle multiple result sets from stored procedures or multi statements. This option will be automatically set if CLIENT\_MULTI\_STATEMENTS is set.
  * And others per [protocol capabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/clientserver-protocol/1-connecting/connection#capabilities).

## Description

Establishes a connection to a database server.&#x20;

## Return Value

Returns a connection handle (same as passed for 1st parameter) or `NULL` on error. On error, please check [mysql\_errno()](mysql_errno.md) and [mysql\_error()](mysql_error.md) functions for more information.

{% hint style="info" %}
* The password doesn't need to be encrypted before executing `mysql_real_connect()`. This will be handled in the client server protocol.
* The connection handle can't be reused for establishing a new connection. It must be closed and reinitialized before.
* `mysql_real_connect()` must complete successfully before you can execute any other API functions beside [mysql\_optionsv()](mysql_optionsv.md).
*   host parameter may contain multiple host/port combinations (supported since version 3.3.0). The following syntax is required:

    * hostname and port must be separated by a colon (:)
    * IPv6 addresses must be enclosed within square brackets
    * hostname:port pairs must be be separated by a comma (,)
    * if only one host:port was specified, the host string needs to end with a comma.
    * if no port was specified, the default port will be used.

    **Examples for failover host string:**

    `host=[::1]:3306,192.168.0.1:3306,test.example.com`

    `host=127.0.0.1:3306,`
{% endhint %}

## See Also

* [mariadb\_reconnect](mariadb_reconnect.md)
* [mysql\_close()](mysql_close.md)
* [mysql\_init()](mysql_init.md)
* [protocol capabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/clientserver-protocol/1-connecting/connection#capabilities)

{% @marketo/form formId="4316" %}
