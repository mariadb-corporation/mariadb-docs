---
description: >-
  mysql_ssl_set configures TLS parameters including key, certificate, CA, and
  cipher list for a MariaDB connection, and must be called before
  mysql_real_connect.
---

# mysql\_ssl\_set

## Syntax

```c
int mysql_ssl_set(MYSQL *mysql, const char *key, const char *cert,
  const char *ca, const char *capath, const char *cipher)
```

## Parameters

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `key` - path to the key file.
* `cert` - path to the certificate file.
* `ca` - path to the certificate authority file.
* `capath` - path to the directory containing the trusted TLS CA certificates in PEM format.
* `cipher` list of permitted ciphers to use for TLS encryption.

## Description

Used for establishing a [secure TLS connection](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-in-transit-encryption). It must be called before attempting to use [mysql\_real\_connect()](mysql_real_connect.md). TLS support must be enabled in the client library in order for the function to have any effect.

`NULL` can be used for an unused parameter. Always returns zero.

To enable TLS without specifying certificates, set all values to `NULL`:

```sql
mysql_ssl_set(mysql, NULL, NULL, NULL, NULL, NULL)
```

This is the same as [`mysql_optionsv(mysql, MYSQL_OPT_SSL_ENFORCE, &yes)`](mysql_optionsv.md).

{% hint style="info" %}
* [mysql\_real\_connect()](mysql_real_connect.md) will return an error if attempting to connect and TLS is incorrectly set up.
* Even if Connector/C supports TLSv1.3 protocol, it is not possible yet to specify TLSv1.3 cipher suites via `cipher` parameter.
{% endhint %}

## See Also

* [mysql\_get\_ssl\_cipher()](mysql_get_ssl_cipher.md)

{% @marketo/form formId="4316" %}
