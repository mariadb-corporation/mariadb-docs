---
description: >-
  How to encrypt MaxScale connections to clients and servers with TLS/SSL,
  and every TLS/SSL setting for servers and listeners, in alphabetical order.
---

# MaxScale TLS/SSL Encryption

This page describes how to configure TLS/SSL for MaxScale servers and listeners.

This section describes TLS/SSL-related configuration parameters for both servers and listeners.

To enable TLS/SSL for a listener, set the `ssl` parameter to `allow` or
`require`. Listeners are SSL-enabled by default. If the clients expect a
specific certificate from MaxScale, set the `ssl_cert` and `ssl_key` parameters
for the listener. If a certificate is not defined, MaxScale will use an
auto-generated self-signed certificate. The generated certificate can pass
verification when used with a recent (11.4 or greater) client version.

To enable TLS/SSL-connections to a server, set its `ssl` parameter to `allow` or
`require`. If the backend database server has certificate verification enabled,
configure the `ssl_cert` and `ssl_key` parameters of the server. The database
server itself must also be configured to use TLS/SSL-connections if backend
connection encryption is enforced.

Custom CA certificates can be defined with the `ssl_ca` parameter. If `ssl_verify_peer_certificate` is enabled yet `ssl_ca` is not set, MaxScale will load CA certificates from the system default location.

If a listener is configured with `ssl=require`, the listener will reject any
unencrypted connections. To allow both encrypted and unencrypted connections to
the same listener, set `ssl` to `allow`. `allow` is the default mode.

Multiple listeners with different configurations can be created to enable
different encryption schemes.

If a server is configured with `ssl=require`, MaxScale enforces SSL usage for
all connections to the server. If an encrypted connection to the server cannot
be established, the connection fails.

Starting with MaxScale 2.5.20, if the TLS certificate given to MaxScale has the X509v3 extended key usage information, MaxScale will check it and refuse to use a certificate with the wrong usage. This means that a certificate with only clientAuth can only be used with servers and a certificate with only serverAuth can only be used with listeners. In order to use the same certificate for both listeners and servers, it must have both the clientAuth and serverAuth usages.

**From MaxScale 26.10,** listeners are SSL-enabled by default and can accept
both encrypted and unencrypted connections. In earlier versions they are not
SSL-enabled by default and cannot accept both.

## Settings for TLS/SSL Encryption

### `ssl`

* Type: [enumeration](README.md#enumerations)
* Mandatory: No
* Dynamic: Yes
* Values: `disable`, `allow`, `require`
* Default: `allow`
* Description: Configures the SSL encryption for connections.

Enables SSL connections when set to `allow` or `require`. The old boolean values
can still be used and map to `require` (true) and `disable` (false).

In listener configuration, `allow` means that the listener accepts both
encrypted and unencrypted connections. `disable` only accepts unencrypted
connections and `require` only accepts encrypted connections.

In server configuration, `disable` only uses unencrypted connections to the
server. `require` only uses encrypted connections. `allow`-mode is flexible, and
means that MaxScale generally prefers to use encrypted connections but falls
back to unencrypted connections if the server does not support encryption. In
some cases (e.g. the
[Binlogrouter](../../../../reference/maxscale-routers/maxscale-binlogrouter.md))
`allow` may default to unencrypted connections. Use `allow` when encryption is
not essential, or when MariaDB Server SSL support may change while MaxScale is
running.

Starting with MaxScale 21.06.18, 22.08.15, 23.02.12, 23.08.8, 24.02.4 and
24.08.1, if SSL is disabled for a listener, MariaDB user accounts that require
SSL cannot log in through that listener. Any user account with a non-empty
_ssl\_type_-field in _mysql.user_-table is blocked. This includes users created
with `REQUIRE SSL` or `REQUIRE X509`.

**From MaxScale 26.10,** the value `allow` is available and is the default.
In earlier versions the setting is a boolean and the default is `false`.

### `ssl_ca`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the CA certificate used to validate the peer’s certificate.

A string giving a file path that identifies an existing readable file. The file must be a Certificate Authority (CA) certificate. It will be used to verify that the peer certificate (sent by either client or a MariaDB Server) is valid. The CA certificate can consist of a certificate chain.

**NOTE** Up until MariaDB MaxScale 6, the parameter was called `ssl_ca_cert`, which is still accepted as an alias for `ssl_ca`.

### `ssl_ca_cert`

Deprecated since MariaDB MaxScale 22.08. See `ssl_ca`.

### `ssl_cert`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Deprecated - use [ssl\_ca](#ssl_ca) instead.

A string giving a file path that identifies an existing readable file. The file must be the SSL certificate MaxScale should use. The certificate must match the key defined in `ssl_key`. This is an optional parameter for listeners and servers.

### `ssl_cert_verify_depth`

* Type: number
* Mandatory: No
* Dynamic: Yes
* Default: `9`
* Description: Specifies the maximum depth of the CA chain during verification.

The maximum length of the certificate authority chain that will be accepted. The default value is 9, same as the OpenSSL default. The configured value must be larger than 0.

### `ssl_cipher`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Provides the list of TLS ciphers to use for SSL connections.

Set the list of TLS ciphers. By default, no explicit ciphers are defined and the system defaults are used. Note that this parameter does not modify TLSv1.3 ciphers.

### `ssl_crl`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the CRL file used to validate revoked SSL certificates.

A string giving a file path that identifies an existing readable file. The file must be a Certificate Revocation List in the PEM format that defines the revoked certificates. This parameter is only accepted by listeners.

**Example SSL enabled server configuration**

```
[server1]
type=server
address=10.131.24.62
port=3306
ssl=true
ssl_cert=/usr/local/mariadb/maxscale/ssl/crt.max-client.pem
ssl_key=/usr/local/mariadb/maxscale/ssl/key.max-client.pem
ssl_ca_cert=/usr/local/mariadb/maxscale/ssl/crt.ca.maxscale.pem
```

This example configuration requires all connections to this server to be encrypted with SSL. The paths to the certificate files and the Certificate Authority file are also provided.

**Example SSL enabled listener configuration**

```
[RW-Split-Listener]
type=listener
service=RW-Split-Router
port=3306
ssl=true
ssl_cert=/usr/local/mariadb/maxscale/ssl/crt.maxscale.pem
ssl_key=/usr/local/mariadb/maxscale/ssl/key.csr.maxscale.pem
ssl_ca_cert=/usr/local/mariadb/maxscale/ssl/crt.ca.maxscale.pem
```

This example configuration requires all connections to be encrypted with SSL. The paths to the certificate files and the Certificate Authority file are also provided.

### `ssl_key`

* Type: path
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Specifies the path to the SSL/TLS private key that is used for secure connections.

A string giving a file path that identifies an existing readable file. The file must be the SSL certificate private key MaxScale should use. This is an optional parameter for listeners but an optional parameter for servers.

### `ssl_passphrase`

* Type: string
* Mandatory: No
* Dynamic: Yes
* Default: `""`
* Description: Defines the passphrase used to decrypt the SSL/TLS private key.

If the private key specified using [ssl\_key](#ssl_key) requires a password, it should be provided with `ssl_passphrase`. The setting supports 3 different ways for providing the passphrase, indicated by the used prefix:

* `env:string`: The string is the name of an environment variable specifying the password.
* `file:string`: The string is the path of a file containing the password.
* `pass:string`: The string is the password.

In the case of `file`, the password is assumed to be the first read line, excluding a trailing line-feed. Any additional data is ignored. A failure to read the line will cause errors to be logged, but will not cause MaxScale to terminate.

It is an error, not to provide a prefix.

Examples:

```
ssl_passphrase=env:MY_SECRET_PASSWORD
ssl_passphrase=file:/path/to/pass.txt
ssl_passphrase=pass:MySecretPassword
```

### `ssl_verify_peer_certificate`

* Type: [boolean](README.md#booleans)
* Mandatory: No
* Dynamic: Yes
* Default: `false`
* Description: Verifies the peer's SSL/TLS certificate against a trusted CA.

Peer certificate verification. This functionality is disabled by default. In versions prior to 2.3.17 the feature was enabled by default.

When this feature is enabled, the peer (client or MariaDB Server) must send a certificate. The certificate sent by the peer is verified against the configured Certificate Authority to ensure the peer is who they claim to be. For listeners, this behaves as if `REQUIRE X509` was defined for all users.

If this feature is enabled for a server yet `ssl_ca` is not set, MaxScale will attempt to verify the backend server certificate after authentication as explained [here](https://mariadb.org/mission-impossible-zero-configuration-ssl/). This verification method is only supported with MariaDBAuth and Ed25519Auth and requires MariaDB Server version 11.4 or later.

### `ssl_verify_peer_host`

* Type: [boolean](README.md#booleans)
* Mandatory No
* Dynamic: Yes
* Default: `false`
* Description: Verifies the peer's hostname or IP address using its SSL/TLS certificate.

Peer host verification.

When this feature is enabled, the peer (client or MariaDB Server) hostname or IP is verified against the certificate sent by the peer. If the IP address or the hostname does not match the one in the certificate, the connection is closed.

If the peer does not provide a certificate, host verification is skipped. To require peer certificates, also enable `ssl_verify_peer_certificate`. For servers, the combination of

```
ssl_verify_peer_certificate=true
ssl_verify_peer_host=true
```

behaves like the `--ssl-verify-server-cert` command line option for the `mysql` client.

### `ssl_version`

* Type: [enum\_mask](README.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `MAX`, `TLSv1.0`, `TLSv1.1`, `TLSv1.2`, `TLSv1.3`, `TLSv10`, `TLSv11`, `TLSv12`, `TLSv13`
* Default: `MAX`
* Description: Lists the TLS protocol versions that are allowed for SSL/TLS connections.

This parameter controls the allowed TLS version. Accepted values are:

* `TLSv10`
* `TLSv11`
* `TLSv12`
* `TLSv13` (not supported on OpenSSL 1.0)
* `MAX`

MaxScale versions 6.4.16, 22.08.13, 23.02.10, 23.08.6, 24.02.2 and all newer releases accept also the following alias values:

* `TLSv1.0`
* `TLSv1.1`
* `TLSv1.2`
* `TLSv1.3` (not supported on OpenSSL 1.0)

The default setting (MAX) allows all supported versions. MaxScale supports TLSv1.0, TLSv1.1, TLSv1.2 and TLSv1.3 depending on the OpenSSL library version. TLSv1.0 and TLSv1.1 are considered deprecated and should not be used, so setting `ssl_version=TLSv1.2,TLSv1.3` or `ssl_version=TLSv1.3` is recommended.

In MaxScale versions 6.4.13, 22.08.11, 23.02.7, 23.08.3 and earlier, this setting defined the _only_ allowed TLS version, e.g. `ssl_version=TLSv12` would only enable TLSv12. The interpretation changed in MaxScale versions 6.4.14, 22.08.12, 23.02.8, 23.08.4 to enable the user to disable old versions while allowing multiple recent TLS versions. In these versions, `ssl_version=TLSv1.2` enabled both TLSv1.2 and TLSv1.3.

The interpretation changed again in MaxScale versions 6.4.16, 22.08.13, 23.02.10, 23.08.6, 24.02.2. In these versions the value of `ssl_version` is an enumeration of accepted TLS protocol versions. This means that `admin_ssl_version=TLSv1.2` again only allows TLSv1.2. To retain the behavior from the previous releases where the newer versions were automatically enabled, the protocol versions must be explicitly listed, for example `admin_ssl_version=TLSv1.2,TLSv1.3`. The change was done to make the `ssl_version` behave identically to how the MariaDB [tls\_version](../../../../../server/security/encryption/data-in-transit-encryption/ssltls-system-variables.md#tls_version) parameter works.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
