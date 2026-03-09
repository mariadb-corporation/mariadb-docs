# SSL/TLS Status Variables

The status variables listed on this page relate to encrypting data during transfer with the Transport Layer Security (TLS) protocol. Often, the term Secure Socket Layer (SSL) is used interchangeably with TLS, although strictly speaking, the SSL protocol is a predecessor to TLS and is no longer considered secure.

For compatibility reasons, the TLS status variables in MariaDB still use the `Ssl_` prefix, but MariaDB only supports its more secure successors. For more information on SSL/TLS in MariaDB, see [Secure Connections Overview](../../../security/encryption/data-in-transit-encryption/secure-connections-overview.md).

Some of these status values are not under the control of the server, but are reporting back settings of the underlying SSL library used by the server.

## Variables

#### `Ssl_accept_renegotiates`

* Description: Number of negotiations needed to establish the TLS connection. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_accepts`

* Description: Number of accepted TLS handshakes. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_callback_cache_hits`

* Description: Number of sessions retrieved from the session cache. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_cipher`

* Description: The TLS cipher currently in use.
* Scope: Global, Session
* Data Type: `string`

#### `Ssl_cipher_list`

* Description: List of the available TLS ciphers.\
  This is not necessarily the list of ciphers the MariaDB server can actually accept, but rather the list of ciphers supported by the underlying SSL library in general. E.g. some of these may not be compatible with the servers SSL certificate and so can't be used to connect to that server.
* Scope: Global, Session
* Data Type: `string`

#### `Ssl_client_connects`

* Description: Number of TLS handshakes started in client mode. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_connect_renegotiates`

* Description: Number of negotiations needed to establish the connection to a TLS-enabled master. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_ctx_verify_depth`

* Description: Number of tested TLS certificates in the chain. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_ctx_verify_mode`

* Description: Mode used for TLS context verification.The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_default_timeout`

* Description: Default timeout for TLS, in seconds.
* Scope: Global, Session
* Data Type: `numeric`

#### `Ssl_finished_accepts`

* Description: Number of successful TLS sessions in server mode. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_finished_connects`

* Description: Number of successful TLS sessions in client mode. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_server_not_after`

* Description: Last valid date for the server TLS certificate.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Ssl_server_not_before`

* Description: First valid date for the server TLS certificate.
* Scope: Global, Session
* Data Type: `numeric`
* Introduced: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Ssl_session_cache_hits`

* Description: Number of TLS sessions found in the session cache. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_session_cache_misses`

* Description: Number of TLS sessions not found in the session cache. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_session_cache_mode`

* Description: Mode used for TLS caching by the server.
* Scope: Global
* Data Type: `string`

#### `Ssl_session_cache_overflows`

* Description: Number of sessions removed from the session cache because it was full. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_session_cache_size`

* Description: Size of the session cache. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_session_cache_timeouts`

* Description: Number of sessions which have timed out. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_sessions_reused`

* Description: Number of sessions reused. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global, Session
* Data Type: `numeric`

#### `Ssl_used_session_cache_entries`

* Description: Current number of sessions in the session cache. The global value can be flushed by [FLUSH STATUS](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).
* Scope: Global
* Data Type: `numeric`

#### `Ssl_verify_depth`

* Description: TLS verification depth.\
  How many levels within the certificate signing chain the verification should cover. This is not set by the server itself but by the OpenSSL configuration, and will typically show a very large number like 18446744073709551615, basically meaning "always verify the full signing chain up to the root CA"
* Scope: Global, Session
* Data Type: `numeric`

#### `Ssl_verify_mode`

* Description: TLS verification mode.

The OpenSSL verification mode flags in effect on the server side.

The value so far is always 5 when OpenSSL encryption is in effect, and 0 when not using encryption, or when the server is compiled against WolfSSL.

The value 5 is a combination of the `SSL_VERIFY_PEER` and `SSL_VERIFY_CLIENT_ONCE` flags, meaning that the client may send a certificate of its own connect, but will not be asked to send one again later for the duration of the encrypted connection.

The `SSL_VERIFY_FAIL_IF_NO_PEER_CERT` is not used at this point to enforce that the client sends a certificate if the database user was created with `REQUIRE X509`, `REQUIRE ISSUER` or `REQUIRE SUBJECT`, whether a client certificate was indeed sent, and whether it fits additional `REQUIRE` conditions, is checked by the server itself at a later state.

See also [#notes](https://docs.openssl.org/master/man3/SSL_CTX_set_verify/#notes) for a description of the OpenSSL verify mode flags.

* Scope: Global, Session
* Data Type: `numeric`

#### `Ssl_version`

* Description: TLS version in use by the current session, possible values are `TLSv1.0`, `TLSv1.1`, `TLSv1.2` and `TLSv1.3`
* Scope: Global, Session
* Data Type: `string`

## See Also

* [Server Status Variables](server-status-variables.md) - complete list of status variables.
* [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
