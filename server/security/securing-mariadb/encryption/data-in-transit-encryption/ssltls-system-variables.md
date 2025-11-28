# SSL/TLS System Variables

The system variables listed on this page relate to encrypting data during transfer between servers and clients using the Transport Layer Security (TLS) protocol. Often, the term Secure Sockets Layer (SSL) is used interchangeably with TLS, although strictly speaking the SSL protocol is the predecessor of TLS and is no longer considered secure.

For compatibility reasons, the TLS system variables in MariaDB still use the `ssl_` prefix, but MariaDB only supports its more secure successors. For more information on SSL/TLS in MariaDB, see [Secure Connections Overview](secure-connections-overview.md).

## Variables

#### `have_openssl`

* Description: This variable shows whether the server is linked with [OpenSSL](https://www.openssl.org/) rather than MariaDB's bundled TLS library, which might be [wolfSSL](https://www.wolfssl.com/products/wolfssl/) or [yaSSL](https://www.wolfssl.com/products/yassl/).
  * I this system variable shows `YES`, the server is linked with OpenSSL.
  * See [TLS and Cryptography Libraries Used by MariaDB](../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.
* Scope: Global
* Dynamic: No

#### `have_ssl`

* Description: This variable shows whether the server supports using [TLS](./) to secure connections.
  * If the value is `YES`, then the server supports TLS, and TLS is enabled.
  * If the value is `DISABLED`, then the server supports TLS, but TLS is not enabled.
  * If the value is `NO`, then the server was not compiled with TLS support, so TLS cannot be enabled.
  * When TLS is supported, check the [have\_openssl](ssltls-system-variables.md#have_openssl) system variable to determine whether the server is using OpenSSL or MariaDB's bundled TLS library. See [TLS and Cryptography Libraries Used by MariaDB](../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.
* Scope: Global
* Dynamic: No

#### `ssl_ca`

* Description: Defines a path to a PEM file that should contain one or more X509 certificates for trusted Certificate Authorities (CAs) to use for [TLS](./). This system variable requires that you use the absolute path, not a relative path. This system variable implies the [ssl](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option.
  * See [Secure Connections Overview: Certificate Authorities (CAs)](secure-connections-overview.md#certificate-authorities-cas) for more information.
* Command line: `--ssl-ca=file_name`
* Scope: Global
* Dynamic: No
* Data Type: `file name`

#### `ssl_capath`

* Description: Defines a path to a directory that contains one or more PEM files that should each contain one X509 certificate for a trusted Certificate Authority (CA) to use for [TLS](./). This system variable requires that you use the absolute path, not a relative path. The directory specified by this variable needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command. This system variable implies the [ssl](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option.
  * See [Secure Connections Overview: Certificate Authorities (CAs)](secure-connections-overview.md#certificate-authorities-cas) for more information.
* Command line: `--ssl-capath=directory_name`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`

#### `ssl_cert`

* Description: Defines a path to the X509 certificate file to use for [TLS](./). This system variable requires that you use the absolute path, not a relative path. This system variable implies the [ssl](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option.
* Command line: `--ssl-cert=name`
* Scope: Global
* Dynamic: No
* Data Type: `file name`
* Default Value: None

#### `ssl_cipher`

* Description: List of permitted ciphers or cipher suites to use for [TLS](./). Besides cipher names, if MariaDB was compiled with OpenSSL, this variable could be set to "SSLv3" or "TLSv1.2" to allow all SSLv3 or all TLSv1.2 ciphers. Note that the TLSv1.3 ciphers cannot be excluded when using OpenSSL, even by using this system variable. See [Using TLSv1.3](using-tlsv13.md) for details. This system variable implies the [ssl](../../../../server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/mariadbd-options.md) option.
* Command line: `--ssl-cipher=name`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: None

#### `ssl_crl`

* Description: Defines a path to a PEM file that should contain one or more revoked X509 certificates to use for [TLS](./). This system variable requires that you use the absolute path, not a relative path.
  * See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](secure-connections-overview.md#certificate-revocation-lists-crls) for more information.
  * This variable is only valid if the server was built with OpenSSL. If the server was built with [wolfSSL](https://www.wolfssl.com/products/wolfssl/) or [yaSSL](https://www.wolfssl.com/products/yassl/), then this variable is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.
* Command line: `--ssl-crl=name`
* Scope: Global
* Dynamic: No
* Data Type: `file name`
* Default Value: None

#### `ssl_crlpath`

* Description: Defines a path to a directory that contains one or more PEM files that should each contain one revoked X509 certificate to use for [TLS](./). This system variable requires that you use the absolute path, not a relative path. The directory specified by this variable needs to be run through the [openssl rehash](https://www.openssl.org/docs/man1.1.1/man1/rehash.html) command.
  * See [Secure Connections Overview: Certificate Revocation Lists (CRLs)](secure-connections-overview.md#certificate-revocation-lists-crls) for more information.
  * This variable is only supported if the server was built with OpenSSL. If the server was built with [wolfSSL](https://www.wolfssl.com/products/wolfssl/) or [yaSSL](https://www.wolfssl.com/products/yassl/), then this variable is not supported. See [TLS and Cryptography Libraries Used by MariaDB](../tls-and-cryptography-libraries-used-by-mariadb.md) for more information about which libraries are used on which platforms.
* Command line: `--ssl-crlpath=name`
* Scope: Global
* Dynamic: No
* Data Type: `directory name`
* Default Value: None

#### `ssl_key`

* Description: Defines a path to a private key file to use for [TLS](./). This system variable requires that you use the absolute path, not a relative path. This system variable implies the [ssl](../../../../server-management/starting-and-stopping-mariadb/mariadbd-options.md) option.
* Command line: `--ssl-key=name`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: None

#### `ssl_passphrase`

*   Description: SSL certificate key passphrase. Works similarly to the `--passout/--passin` openssl command-line parameters. The pass phrase value can be formatted as follows:

    * `pass:`_`password`_ — Provide the actual _password_.
    * `env:`_`var`_ — Obtain the password from the environment variable _var_.
    * `file:`_`filename`_ — Read the password from the specified file _filename_. Only the first line, up to the newline character, is read from the stream.

    If `ssl_passphrase` is set, [SHOW VARIABLE](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) shows one of `file:`, `env:`, or `pass:` , and doesn't reveal sensitive data.
* Command line: `--ssl-passphrase=val`
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: None
* Introduced: [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120)

#### `tls_version`

* Description: This system variable accepts a comma-separated list (with no whitespaces) of TLS protocol versions. A TLS protocol version will only be enabled if it is present in this list. All other TLS protocol versions will not be permitted.
  * See [Secure Connections Overview: TLS Protocol Versions](secure-connections-overview.md#tls-protocol-versions) for more information.
* Command line: `--tls-version=value`
* Scope: Global
* Dynamic: No
* Data Type: `enumerated`
* Default Value:
  * TLSv1.1,TLSv1.2,TLSv1.3 (<= [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-15-release-notes), [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-5-release-notes), [MariaDB 11.0.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes))
  * TLSv1.2,TLSv1.3 (>= [MariaDB 10.6.16](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-16-release-notes), [MariaDB 10.11.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-6-release-notes), [MariaDB 11.0.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-4-release-notes) and later versions)
* Valid Values: TLSv1.0,TLSv1.1,TLSv1.2,TLSv1.3
* Introduced: [MariaDB 10.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1046-release-notes)

#### `version_ssl_library`

* Description: The version of the [TLS](./) library that is being used. Note that the version returned by this system variable does not always necessarily correspond to the exact version of the OpenSSL package installed on the system. OpenSSL shared libraries tend to contain interfaces for multiple versions at once to allow for backward compatibility. Therefore, if the OpenSSL package installed on the system is newer than the OpenSSL version that the MariaDB server binary was built with, then the MariaDB server binary might use one of the interfaces for an older version.
  * See [TLS and Cryptography Libraries Used by MariaDB: Checking the Server's OpenSSL Version](../tls-and-cryptography-libraries-used-by-mariadb.md#checking-the-servers-openssl-version) for more information.
* Scope: Global
* Dynamic: No
* Data Type: `string`
* Default Value: None

## See Also

* [Secure Connections Overview](secure-connections-overview.md)
* [System Variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) for a complete list of system variables and instructions on setting them.
* [Full list of MariaDB options, system and status variables](../../../../reference/full-list-of-mariadb-options-system-and-status-variables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
