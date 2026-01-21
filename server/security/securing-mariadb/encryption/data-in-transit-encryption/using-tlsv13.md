---
description: >-
  Information about TLSv1.3 support in MariaDB (available with OpenSSL 1.1.1+),
  noting that the ssl_cipher variable does not affect TLSv1.3 cipher suites.
---

# Using TLSv1.3

OpenSSL 1.1.1 introduced support for TLSv1.3. TLSv1.3 is a major rewrite of the TLS protocol. (Some even argued it should've been called TLSv2.0.) Among other things,

* it introduces a new set of cipher suites that only work with TLSv1.3,&#x20;
* and TLSv1.3 does not support cipher suites from previous TLS protocol versions.

This incompatible change had a non-obvious consequence. If you specified particular cipher suites to disable old and obsolete TLS protocol version, you might have inadvertently prevented TLSv1.3 from working, if the TLSv1.3 cipher suites were not added to their cipher list. After upgrading to OpenSSL 1.1.1, this might give the impression that you are using TLSv1.3, when their existing cipher suite configuration might prevent it.

To avoid this problem, OpenSSL developers decided that TLSv1.3 cipher suites should not be affected by the normal cipher-selecting API. This means that the [ssl\_cipher](ssltls-system-variables.md#ssl_cipher) system variable had no effect on the TLSv1.3 cipher suites. This has been fixed in MariaDB, though – you can use the `ssl_cipher` variable just like before that change.

{% hint style="warning" %}
You cannot specify both TLSv1.2 and TLSv1.3 at the same time when MariaDB is built against OpenSSL 1.1.1.
{% endhint %}

See this [OpenSSL blog post](https://www.openssl.org/blog/blog/2018/02/08/tlsv1.3/) and [GitHub issue](https://github.com/openssl/openssl/issues/5359) for more information.

### See Also

* [Secure Connections Overview](secure-connections-overview.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
