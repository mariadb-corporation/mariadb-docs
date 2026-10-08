---
description: >-
  Proxy protocol support, which lets proxy programs relay client IP addresses
  to MariaDB Server.
---

# Proxy Protocol Support

The proxy protocol allows proxy programs to relay the IP addresses of the clients to the server programs. It is important in the case of MariaDB, since IP information is actually a part of user identity.

## How Proxy Protocol Works

As per the [proxy protocol specification](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt), the connecting client can prefix its first packet with a proxy protocol header. The server will parse the header and assume the client's IP address is the one set in the proxy header.

For example, if a client sends the proxy header (V1, text) which is "PROXY TCP4 192.168.0.1 192.168.0.11 56324 443\r\n", the server, after parsing, assumes the client's IP is 192.168.0.1

MariaDB server understands both Version 1 (text) and Version 2 (binary) of the proxy header.

If the protocol specified by the version 1 header is "UNKNOWN", the MariaDB server will treat the connection as if the proxy protocol was disabled. This can be used when a valid proxy protocol header is needed, but there is no client to proxy, for example, when a proxy does a health check.

## Enabling Proxy Protocol in MariaDB Server

To enable use of the proxy protocol, it is necessary to specify subnetworks that are allowed to send proxy headers, using the [proxy-protocol-networks](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#proxy_protocol_networks) server variable.

[proxy-protocol-networks](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#proxy_protocol_networks) is either a comma-separated list of [(sub) networks](https://en.wikipedia.org/wiki/Subnetwork) or IP addresses. One can also use 'localhost' in this list, which means Unix domain socket/named pipe/shared memory connections are allowed as well. Or proxy-protocol-networks can be set to \*, meaning that proxy headers are allowed from any client.

{% hint style="warning" %}
Note that a client running on a host within an allowed proxy network or an IP address can itself pretend to be connected from any IP address whatsoever and thus can possibly impersonate other users. Generally, you should limit shell access to proxy hosts to a minimum. And remember, with `proxy-protocol-networks=*` every host is a proxy host.
{% endhint %}

Example in my.ini/my.cnf

```
proxy-protocol-networks=::1, 192.168.0.0/16, localhost
```

allows IPv6 connections from local machine ::1, from IP addresses starting with 192.168, and from connections made with Unix domain sockets or named pipes.

## Client-Side Support for Proxy Protocol

Since the functionality is suited only to very specific proxy-like programs, most client APIs do not provide support for sending proxy headers. One exception is [Connector/C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c) version 3 or later. One can now use [mysql\_optionsv()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_optionsv):

```
mysql_optionsv(mysql, MARIADB_OPT_PROXY_HEADER, header,  header_size)
```

prior to [mysql\_real\_connect()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-functions/mysql_real_connect) or mysql\_connect(), to send the header. In the call above, `_header_` is the proxy header with the type `void *`, and `_header_size_` is its size in bytes (type is `size_t`).

### Example

```
const char *hdr="PROXY TCP4 192.168.0.1 192.168.0.11 56324 443\r\n";
mysql_optionsv(mysql, MARIADB_OPT_PROXY_HEADER, hdr,  strlen(hdr));
```

## Using Proxy Protocol with MariaDB MaxScale

If you want to use proxy protocol with MaxScale:

* Add the IP address of the MaxScale server to [proxy-protocol-networks](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#proxy_protocol_networks)
* In `maxscale.cnf`, add the [proxy\_protocol](./) parameter for all configured servers

Once configured, MaxScale will proxy the credentials from the client to the server.

## See Also

* [Proxy Protocol](https://www.haproxy.org/download/1.8/doc/proxy-protocol.txt)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
