---
description: >-
  Encrypt connections with TLS, verify the server certificate, and present a
  client certificate. Includes how each ssl-mode value behaves with MariaDB
  Connector/C.
---

# Encrypted Connections

<!--
  SYNCED: this page is maintained in mariadb-corporation/mariadb-shell, under docs-ref/content/,
  and copied one way into mariadb-docs (tools/community/mariadb-shell/).
  Make every change in mariadb-corporation/mariadb-shell. A change made in mariadb-docs or in the
  GitBook editor is overwritten by the next sync.
-->

MariaDB Shell encrypts connections with TLS through MariaDB Connector/C. By default, it uses TLS whenever the server supports it. To protect against a server impersonator, you also need to verify the server certificate with `ssl-mode=VERIFY_CA` or `VERIFY_IDENTITY`.

You set the TLS options in a URI, in a connection dictionary, on the command line, or in an option file. In a URI, encode file paths or enclose them in parentheses.

{% tabs %}
{% tab title="URI" %}
```text
mariadb://dba@db1.example.com/shop?ssl-mode=VERIFY_IDENTITY&ssl-ca=(/etc/mysql/certs/ca.pem)
```
{% endtab %}

{% tab title="Command line" %}
```sh
mariadb-shell dba@db1.example.com/shop --ssl-mode=VERIFY_IDENTITY --ssl-ca=/etc/mysql/certs/ca.pem
```
{% endtab %}

{% tab title="Python" %}
```python
shell.connect({
    "uri": "dba@db1.example.com/shop",
    "ssl-mode": "VERIFY_IDENTITY",
    "ssl-ca": "/etc/mysql/certs/ca.pem",
})
```
{% endtab %}

{% tab title="Option file" %}
```ini
[mariadb-shell]
ssl-mode = VERIFY_IDENTITY
ssl-ca = /etc/mysql/certs/ca.pem
```
{% endtab %}
{% endtabs %}

To check whether a session is encrypted, run `\status`. The `SSL` line shows the cipher and the TLS version, or `Not in use.` The prompt also shows `ssl` for an encrypted session.

## SSL Modes

The `ssl-mode` option (`--ssl-mode`) accepts five values. Connector/C has no direct equivalent of this option, so MariaDB Shell maps each value onto the connector's own settings. The resulting behavior differs from MySQL Shell for `PREFERRED` and `REQUIRED`:

| Value | Encryption | Server certificate | Server without TLS |
| --- | --- | --- | --- |
| `DISABLED` | Off | Not checked | Connects without TLS. |
| `PREFERRED` | On if the server supports it | Not checked | Connects without TLS. |
| `REQUIRED` | On if the server supports it | Not checked | Connects without TLS. |
| `VERIFY_CA` | Required | Verified | Fails with error 2026. |
| `VERIFY_IDENTITY` | Required | Verified | Fails with error 2026. |

If you don't set `ssl-mode`, MariaDB Shell uses `PREFERRED`. If you set `ssl-ca` or `ssl-capath` without `ssl-mode`, it uses `VERIFY_CA`.

{% hint style="danger" %}
`ssl-mode=REQUIRED` doesn't guarantee an encrypted connection. If the server has TLS turned off, MariaDB Shell connects in plain text, without an error or a warning. To make sure that a connection is encrypted, use `VERIFY_CA` or `VERIFY_IDENTITY`, which refuse a server without TLS.
{% endhint %}

### Certificate Verification

With `VERIFY_CA` and `VERIFY_IDENTITY`, Connector/C checks the server certificate against your certificate authority (CA), and also checks that the host name or IP address you connect to matches the certificate. In this build, the two values therefore behave the same: both include the host name check. Connect with a name that appears in the server certificate's subject alternative names or common name, such as `db1.example.com`, not with an alias or an address that the certificate doesn't list.

You normally give the CA with `ssl-ca`. If you leave it out, Connector/C can still verify the self-signed certificate that MariaDB Server 11.4 and later generates automatically, provided that you log in with a password: the client then checks the certificate's fingerprint against a value derived from the password. If verification isn't possible, the connection fails, for example:

```text
MySQL Error 2026 (HY000): TLS/SSL error: self-signed certificate in certificate chain
```

### Rules for Combining Options

The certificate authority and revocation options only make sense when the server certificate is verified. If you combine `ssl-ca`, `ssl-capath`, `ssl-crl`, or `ssl-crlpath` with `ssl-mode` set to `DISABLED`, `PREFERRED`, or `REQUIRED`, MariaDB Shell refuses the connection:

```text
Invalid ssl-mode, value should be either 'verify_ca' or 'verify_identity' when any of 'ssl-ca', 'ssl-capath', 'ssl-crl' or 'ssl-crlpath' are provided.
```

## Certificate and Key Options

| Option | Description |
| --- | --- |
| `ssl-ca` | The file that contains the trusted CA certificates, in PEM format. |
| `ssl-capath` | A directory of trusted CA certificate files, in PEM format. |
| `ssl-cert` | The client certificate, in PEM format, for accounts that require one (`REQUIRE X509`, `REQUIRE SUBJECT`, or `REQUIRE ISSUER`). |
| `ssl-key` | The private key of the client certificate, in PEM format. |
| `ssl-crl` | A file of certificate revocation lists, in PEM format. |
| `ssl-crlpath` | A directory of certificate revocation list files. |

Each option exists with the same name on the command line, with two leading dashes, and in option files. In option files, you can also write the names with underscores, such as `ssl_ca`.

A connection with a client certificate:

```sh
mariadb-shell 'mariadb://app@db1.example.com/shop?ssl-mode=VERIFY_IDENTITY' \
  --ssl-ca=/etc/mysql/certs/ca.pem \
  --ssl-cert=/home/app/.certs/app-cert.pem \
  --ssl-key=/home/app/.certs/app-key.pem
```

## Protocol Versions and Ciphers

| Option | Description |
| --- | --- |
| `tls-version` | A comma-separated list of the TLS versions to allow. The valid versions are `TLSv1.2` and `TLSv1.3`. |
| `ssl-cipher` | A colon-separated list of the ciphers to allow, in OpenSSL syntax. With OpenSSL, the list also selects the TLS 1.3 cipher suites. |
| `tls-ciphersuites` | Accepted for compatibility, but has no effect: Connector/C has no setting for TLS 1.3 cipher suites. |

For example, to restrict a connection to TLS 1.2 with one cipher:

```sh
mariadb-shell dba@db1.example.com --tls-version=TLSv1.2 --ssl-cipher=ECDHE-RSA-AES128-GCM-SHA256
```

If client and server have no protocol version or cipher in common, the connection fails with error 2026.

## Related Topics

* A sandbox instance has TLS turned on and comes with its own CA, server, and client certificates. See [Sandbox Instances](../sandbox-instances.md).

<sub>_This page is licensed: GPLv2_</sub>
