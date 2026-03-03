---
description: >-
  MariaDB 11.4+ offers Zero-Configuration SSL, enabling automatic, MITM-secure
  encryption by default using passwords as a shared secret, eliminating the need
  for manual certificate management.
---

# Zero-Configuration SSL

{% hint style="info" %}
This feature is available from MariaDB 11.4.
{% endhint %}

## Zero-Configuration SSL (TLS)

Zero-Configuration SSL is a feature that makes encrypted connections the default standard without requiring manual certificate management. This allows for secure, MitM[^1]-resistant connections "out of the box", by automating server certificate generation and client-side verification.

## Overview

Traditionally, enabling SSL/TLS required manual steps: generating private keys, creating Certificate Signing Requests (CSRs), and managing a Certificate Authority (CA). Because of this complexity, many deployments remained unencrypted.

Zero-Configuration SSL eliminates these barriers:

1. Automatic Server Setup: The server automatically generates a self-signed certificate if no certificate is configured.
2. Zero-trust validation: Clients verify the server’s identity using the existing account password as a shared secret, rather than relying on a trusted CA.

## Requirements and Defaults

* MariaDB Version: Server and Client must be version 11.4 or higher.
* Default Behavior: SSL is enabled and verified by default. The client has `--ssl-verify-server-cert` enabled by default.
* Supported Authentication Plugins: This feature works with [mysql\_native\_password](../../../reference/plugins/authentication-plugins/authentication-plugin-mysql_native_password.md), [ed25519](../../../reference/plugins/authentication-plugins/authentication-plugin-ed25519.md), and [parsec](../../../reference/plugins/authentication-plugins/authentication-plugin-parsec.md) (that are MitM-proof even without SSL).

## Configuration Options

While designed to work automatically, the following options allow for manual control:

| Option                          | Description                                                                                                                                                                             |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `--disable-ssl`                 | Disables SSL entirely (not recommended).                                                                                                                                                |
| `--skip-ssl-verify-server-cert` | A verified certificate is not required, the client will accept unverified certificates or even a completely unencrypted connection. This is not MitM-safe, even if the server uses SSL. |

## Limitations

Authentication plugins such as PAM, GSSAPI, and `cached_sha2_plugin` are not MitM-proof without SSL, they require SSL to be secure and thus cannot be used to verify SSL itself. One should use traditional CA-based verification with these plugins.

## Verification

To verify that Zero-Configuration SSL is being used, connect via TCP/IP (not via UNIX socket, because in that case the certificate is automatically trusted), and look at the status output:

{% code overflow="wrap" %}
```bash
mariadb -h 127.0.0.1 -u <username> -p
...
MariaDB [(none)]> status
--------------
mariadb from 12.2.2-MariaDB, client 15.2 for osx10.20 (arm64) using  EditLine wrapper
...
Current user:		stefan@localhost
SSL:			Cipher in use is TLS_AES_256_GCM_SHA384, cert is OK
...
Connection:		127.0.0.1 via TCP/IP
...
TCP port:		3306
...
```
{% endcode %}

Check if the server has automatically generated its own certificates by querying the session variables:

{% code overflow="wrap" %}
```sql
MariaDB [(none)]> SHOW SESSION STATUS LIKE 'Ssl_cipher'; SHOW SESSION STATUS LIKE 'Ssl_version';
+---------------+------------------------+
| Variable_name | Value                  |
+---------------+------------------------+
| Ssl_cipher    | TLS_AES_256_GCM_SHA384 |
+---------------+------------------------+
...
+---------------+---------+
| Variable_name | Value   |
+---------------+---------+
| Ssl_version   | TLSv1.3 |
+---------------+---------+
```
{% endcode %}

Run the following to see the server's certificate details:

{% code overflow="wrap" %}
```bash
$ openssl s_client -starttls mysql 127.0.0.1:3306
Connecting to 127.0.0.1
CONNECTED(00000003)
Can't use SSL_get_servername
depth=0 CN=MariaDB Server
verify error:num=18:self-signed certificate
verify return:1
depth=0 CN=MariaDB Server
verify return:1
---
Certificate chain
 0 s:CN=MariaDB Server
   i:CN=MariaDB Server
   a:PKEY: RSA, 4096 (bit); sigalg: sha256WithRSAEncryption
   v:NotBefore: Mar  2 16:19:15 2026 GMT; NotAfter: Feb 28 16:19:15 2036 GMT
...
```
{% endcode %}

## How it Works

The core mechanism of Zero-Configuration SSL is the use of the user password as a shared secret to verify the server’s identity without a Certificate Authority (CA).

1. Connection Establishment: The client connects and establishes a TLS connection using the server's self-signed certificate.
2. Fingerprint Calculation: The client calculates the SHA256 fingerprint of the server’s certificate.
3. Signature Generation:
   * The client creates a signature based on the certificate fingerprint and the user’s password.
   * The server performs the same calculation.
4. Verification: By comparing these values, the client confirms it is communicating with the intended server. This prevents Man-in-the-Middle (MitM) attacks because an attacker would present a different certificate, resulting in a fingerprint mismatch that they cannot resolve without knowing the user's password.

[^1]: Man-in-the-Middle (MitM): A cyberattack where an unauthorized third party secretly intercepts, and potentially alters, the communication between two parties (such as a client and a server) who believe they are talking directly to each other.
