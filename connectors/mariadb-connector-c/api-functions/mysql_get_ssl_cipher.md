---
description: >-
  mysql_get_ssl_cipher returns the name of the TLS cipher in use for a MariaDB
  Connector/C connection, or NULL for non-TLS connections.
---

# mysql\_get\_ssl\_cipher

## Syntax

```c
const char *mysql_get_ssl_cipher(MYSQL *mysql)
```

## Parameter

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).

## Description

Returns the name of the currently used cipher of the [TLS connection](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption/secure-connections-overview), or NULL for non TLS connections.

## Return Value

Returns a zero terminated string containing the cipher suite used for a secure connection, or `NULL` if connection doesn't use TLS/SSL.

## Notes

* For using `mysql_get_ssl_cipher()` MariaDB Connector/C must be built with TLS/SSL support, otherwise the function will return NULL.
* \`mysql\_get\_ssl\_cipher()' can be used to determine if the client server connection is secure.
* Depending on the TLS library in use (OpenSSL, GnuTLS or Windows Schannel) the name of the cipher suites may differ. For example the cipher suite 0x002F (`TLS_RSA_WITH_AES_128_CBC_SHA`) has different names: `AES128-SHA` for OpenSSL and Schannel and `TLS_RSA_AES_128_CBC_SHA1` for GnuTLS.

## See Also

* [mysql\_ssl\_set()](mysql_ssl_set.md)

{% @marketo/form formId="4316" %}
