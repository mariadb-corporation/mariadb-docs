# Connecting

## Overview

Connection is done by many exchanges:

* (Create socket)
* If first byte from server is `0xFF`:
  * Packet is an [ERR\_Packet](../4-server-response-packets/err_packet.md), socket has to be closed.
* Else:
  * Packet is an [Initial handshake packet](connection.md#initial-handshake-packet).
  * If SSL/TLS connection:
    * Client sends [SSLRequest packet](connection.md#sslrequest-packet) and switches to SSL mode for sending and receiving the following messages:
  * Client sends [Handshake response packet](connection.md#handshake-response-packet).
  * Server sends either:
    * An `OK` packet in case of success [OK\_Packet](../4-server-response-packets/ok_packet.md).
    * An error packet in case of error [ERR\_Packet](../4-server-response-packets/err_packet.md).
    * Further authentication data, if requested by the authentication plugin.
      * The content of this authentication data is defined by the authentication plugin.
      * The server _may_ send `0x01` byte first to escape the authentication data, particularly if the data starts with the `0x00` or `0xFF` or `0XFF` byte.
      * This optional first `0x01` byte must always be skipped by the client.
    * Authentication switch:
      * If the client or server doesn't have `PLUGIN_AUTH` capability:
        * Server sends `0xFE` byte.
        * Client sends `old_password`.
      * Else:
        * Server sends [Authentication switch request](connection.md#authentication-switch-request).
        * Client may have many exchange with the server according to the [Plugin](connection.md#plugin-list).
      * Authentication switch ends with server sending either [OK\_Packet](../4-server-response-packets/ok_packet.md) or [ERR\_Packet](../4-server-response-packets/err_packet.md).

## Initial Handshake Packet

* [int<1>](../protocol-data-types.md#fixed-length-integers) protocol version.
* [string](../protocol-data-types.md#null-terminated-strings) server version
  * MariaDB Server 10.X versions are by default prefixed "5.5.5-".
  * [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110) and later versions do not have a "5.5.5-" default prefix.
* [int<4>](../protocol-data-types.md#fixed-length-integers) connection id.
* [string<8>](../protocol-data-types.md#fixed-length-strings) authentication plugin data (1st part).
* [string<1>](../protocol-data-types.md#fixed-length-strings) reserved byte.
* [int<2>](../protocol-data-types.md#fixed-length-integers) server capabilities (1st part).
* [int<1>](../protocol-data-types.md#fixed-length-integers) server default collation.
* [int<2>](../protocol-data-types.md#fixed-length-integers) status flags.
* [int<2>](../protocol-data-types.md#fixed-length-integers) server capabilities (2nd part).
* If (`server_capabilities` & `PLUGIN_AUTH`):
  * [int<1>](../protocol-data-types.md#fixed-length-integers) plugin data length.
* Else:
  * [int<1>](../protocol-data-types.md#fixed-length-integers) 0x00.
* [string<6>](../protocol-data-types.md#fixed-length-strings) filler.
* If (`server_capabilities` & `CLIENT_MYSQL`):
  * [string<4>](../protocol-data-types.md#fixed-length-strings) filler.
* Else:
  * [int<4>](../protocol-data-types.md#fixed-length-integers) server capabilities 3rd part . MariaDB specific flags `/* MariaDB 10.2 or later */`.
* If (`server_capabilities` & `CLIENT_SECURE_CONNECTION`):
  * [string](../protocol-data-types.md#fixed-length-strings) authentication plugin data 2nd part . Length = max(12, plugin data length - 9).
  * [string<1>](../protocol-data-types.md#fixed-length-strings) reserved byte.
* If (server\_capabilities & PLUGIN\_AUTH):
  * [string](../protocol-data-types.md#null-terminated-strings) authentication plugin name.

## Client Handshake Response

If the client requests a TLS/SSL connection, the first response is an SSL connection request packet, followed by a handshake response packet. If no TLS is required, client directly sends a handshake response packet.

### SSLRequest Packet

* [int<4>](../protocol-data-types.md#fixed-length-integers) client capabilities.
* [int<4>](../protocol-data-types.md#fixed-length-integers) max packet size.
* [int<1>](../protocol-data-types.md#fixed-length-integers) client's default character set and collation.
* [string<19>](../protocol-data-types.md#fixed-length-strings) reserved.
* If not (`server_capabilities` & `CLIENT_MYSQL`):
  * [int<4>](../protocol-data-types.md#fixed-length-integers) extended client capabilities
* Else:
  * [string<4>](../protocol-data-types.md#fixed-length-strings) reserved.

### Zero-Configuration SSL Encryption

Automatic Encrypted Connections ([MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114)+):

Previously, failed SSL connections due to self-signed certificates prevented communication. [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114)+ introduces a secondary validation method that works for all servers.

#### **What Happens When SSL Validation Fails?**

Even without a valid SSL certificate, the connector can still authenticate by remembering the server's fingerprint (unique identifier). However, it needs to confirm the connection is secure.

#### **Verifying a Secure Connection:**

The confirmation method depends on the connection type. When using secure MitM-proof methods, like Unix sockets, connector can automatically validate the connection. Otherwise, a shared secret is used.

#### **Shared Secret for Secure Connection:**

The shared secret is only used if the authentication plugin password is hashable (for instance, `mysql_native_password` , `client_ed25519`, or `parsec`) and not empty.

It's calculated by hashing the user's hash password with the authentication seed and the server fingerprint.

Password hash is generated depending on authentication plugin:

* `ed25519` : identical to password encryption.
* `mysql_native_password` : identical to password encryption.
* `parsec`: ext-salt + raw ed25519 public key.

#### **Server 11.4+ Confirmation Details:**

For servers running [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/what-is-mariadb-114) or later, the final confirmation packet contains:

* [int<1>](../protocol-data-types.md#fixed-length-integers) encryption (actually only 0x01 = SHA256 encryption)
* [byte](../protocol-data-types.md#end-of-file-length-bytes) shared secret.

#### **Matching the Shared Secret**

If the calculated shared secret matches the received one, the SSL connection is considered valid (host validation is not needed). Otherwise, the connection must be closed for security reasons.

#### Handshake Response Packet

* [int<4>](../protocol-data-types.md#fixed-length-integers) client capabilities.
* [int<4>](../protocol-data-types.md#fixed-length-integers) max packet size.
* [int<1>](../protocol-data-types.md#fixed-length-integers) client's default character set and collation.
* [string<19>](../protocol-data-types.md#fixed-length-strings) reserved.
* If not (`server_capabilities` & `CLIENT_MYSQL`):
  * [int<4>](../protocol-data-types.md#fixed-length-integers) extended client capabilities.
* Else:
  * [string<4>](../protocol-data-types.md#fixed-length-strings) reserved.
* [string](../protocol-data-types.md#null-terminated-strings) username.
* If (password):
  * If (`server_capabilities` & `PLUGIN_AUTH_LENENC_CLIENT_DATA`):
    * [string](../protocol-data-types.md#length-encoded-strings) authentication data.
  * Else if (`server_capabilities` & `CLIENT_SECURE_CONNECTION`):
    * [int<1>](../protocol-data-types.md#fixed-length-integers) length of authentication response.
    * [string](../protocol-data-types.md#fixed-length-strings) authentication response (length is indicated by previous field).
  * Else:
    * [string](../protocol-data-types.md#null-terminated-strings) authentication response null ended.
* Else:
  * string<1>\0 (empty password).
* If (`server_capabilities` & `CLIENT_CONNECT_WITH_DB`):
  * [string](../protocol-data-types.md#null-terminated-strings) default database name.
* If (`server_capabilities` & `CLIENT_PLUGIN_AUTH`):
  * [string](../protocol-data-types.md#null-terminated-strings) authentication plugin name.
* If (`server_capabilities` & `CLIENT_CONNECT_ATTRS`):
  * [int](../protocol-data-types.md#length-encoded-integers) size of connection attributes.
  * While packet has remaining data:
    * [string](../protocol-data-types.md#length-encoded-strings) key.
    * [string](../protocol-data-types.md#length-encoded-strings) value.

## Server Response to Handshake Response Packet

If the authentication plugin needs further rounds of data exchange (like `parsec`), the server sends additional plugin authentication data (optionally prefixed with `0x01`) to which the client sends an additional response. This can be repeated in multiple rounds. It ends with one of the following:

The server responds with an [OK\_packet](../4-server-response-packets/ok_packet.md), an [ERR\_packet](../4-server-response-packets/err_packet.md), or an Authentication Switch Request packet.

### Authentication Switch Request

(If client and server support `CLIENT_AUTH` capability):

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0xFE : Authentication switch request header.
* [string](../protocol-data-types.md#null-terminated-strings) authentication plugin name.
* [byte](../protocol-data-types.md#end-of-file-length-bytes) authentication plugin data.

## Plugin List

#### mysql\_old\_password Plugin

_deprecated —_ send a 8 byte encrypted password.

Authentication plugin data format :

* [byte<8>](../protocol-data-types.md#fixed-length-bytes) 8-byte seed.

Client response:

* [string](../protocol-data-types.md#null-terminated-strings) old format encrypted password.

#### mysql\_clear\_password Plugin

{% hint style="danger" %}
Since password is transmitted in clear, this has be used only when using SSL connection
{% endhint %}

Send clear password to server.

Client response:

* [string](../protocol-data-types.md#null-terminated-strings) password without encryption.

#### mysql\_native\_password Plugin

SHA-1 encrypted password with server seed.

Authentication plugin data format:

* [string](../protocol-data-types.md#null-terminated-strings) seed.

Client response:

* [byte](../protocol-data-types.md#end-of-file-length-bytes) `SHA1`-encrypted password.

The password is encrypted with: `SHA1( password ) ^ SHA1( seed + SHA1( SHA1( password ) ) )` .

### dialog Plugin (PAM)

Interactive exchanges to permit fill passwords — for example for 2-step authentication.

Authentication plugin data format:

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) password type.
* [string](../protocol-data-types.md#end-of-file-length-strings) prompt message.

The server can send one or many requests. For each of them, the client must display this prompt message to the user, to permit the user to type requested information, then send it to the server in [string](../protocol-data-types.md#null-terminated-strings) format. Password type indicates the answer format (`2` means "read the input with the echo enabled", `4` means "password-like input, echo disabled")

First authentication format (from authentication switch packet) can be empty.

This end when the server sends an [EOF\_Packet](../4-server-response-packets/eof_packet.md), [OK\_Packet](../4-server-response-packets/ok_packet.md) or [ERROR\_packet](../4-server-response-packets/err_packet.md).

### auth\_gssapi\_client Plugin

GSSAPI implementation.

Authentication plugin data format :

* [string](../protocol-data-types.md#null-terminated-strings) serverPrincipalName (UTF-8 format).
* [string](../protocol-data-types.md#null-terminated-strings) mechanisms (UTF-8 format).

Client must exchange packet with server until having a mutual [GSSAPI](https://en.wikipedia.org/wiki/Generic_Security_Services_Application_Program_Interface) authentication.\
The only difference compared to standard client-server GSSAPI authentication is that exchanges contain standard protocol with packet headers.

### client\_ed25519 Plugin

The `ed25519` plugin uses the Elliptic Curve Digital Signature Algorithm to securely store users' passwords and to authenticate users.

See [plugin description](../../plugins/authentication-plugins/authentication-plugin-ed25519.md).

The server sends a random nonce that the client signs.

authentication plugin data format :

* [byte](../protocol-data-types.md#end-of-file-length-bytes) seed.

Client response :

* [byte](../protocol-data-types.md#end-of-file-length-bytes) `ed25519` encrypted password.

### parsec Plugin

Authentication plugin data format:

* [string<32>](../protocol-data-types.md#null-terminated-strings) server nonce.

Client has to send an empty packet to request "ext-salt".


Format of ext-salt is:

* [string<1>](../protocol-data-types.md#fixed-length-strings) 'P' (denotes KDF algorithm = PBKDF2).
* [byte<1>](../protocol-data-types.md#fixed-length-bytes) iteration factor. number of iterations correspond to 1024 << iteration factor (0x0 means 1024, 0x1 means 2048, etc.).
* [byte](../protocol-data-types.md#end-of-file-length-bytes) salt.

The client must then:

* Generate derived key = hash password with PBKDF2 ( sha512 digest) with iteration number and salt from ext-salt.
* Generate a client 32 bytes nonce.
* Generate the signature with `ed25519` of an array concatenation of server nonce + client nonce with the generated derived key as private key.

Client response:

* [byte<32>](../protocol-data-types.md#fixed-length-bytes) client nonce.
* [byte<64>](../protocol-data-types.md#fixed-length-bytes) signature.

## Capabilities

Server and Client have different capabilities, here is the possibles values.\
client with capabilities CLIENT\_MYSQL + CONNECT\_WITH\_DB will have a value of 9 (1 + 8).

| Capability                              | Value   | Details                                                                                                                                                                              |
| --------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CLIENT\_MYSQL                           | 1       | Set by older MariaDB versions. MySQL named this `CLIENT_LONG_PASSWORD`.                                                                                                              |
| FOUND\_ROWS                             | 2       |                                                                                                                                                                                      |
| CONNECT\_WITH\_DB                       | 8       | You can specify database on connect.                                                                                                                                                 |
| COMPRESS                                | 32      | Can use compression protocol                                                                                                                                                         |
| LOCAL\_FILES                            | 128     | Can use [LOAD DATA LOCAL](../../sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md#load-data-local-infile).                  |
| IGNORE\_SPACE                           | 256     | Ignore spaces before `(`.                                                                                                                                                            |
| CLIENT\_PROTOCOL\_41                    | 1 << 9  | 4.1 protocol.                                                                                                                                                                        |
| CLIENT\_INTERACTIVE                     | 1 << 10 |                                                                                                                                                                                      |
| SSL                                     | 1 << 11 | Can use SSL.                                                                                                                                                                         |
| TRANSACTIONS                            | 1 << 13 |                                                                                                                                                                                      |
| SECURE\_CONNECTION                      | 1 << 15 | 4.1 authentication.                                                                                                                                                                  |
| MULTI\_STATEMENTS                       | 1 << 16 | Enable/disable multi-statement support.                                                                                                                                              |
| MULTI\_RESULTS                          | 1 << 17 | Enable/disable multi-results.                                                                                                                                                        |
| PS\_MULTI\_RESULTS                      | 1 << 18 | Enable/disable multi-results for PrepareStatement.                                                                                                                                   |
| PLUGIN\_AUTH                            | 1 << 19 | Client supports plugin authentication.                                                                                                                                               |
| CONNECT\_ATTRS                          | 1 << 20 | Client send connection attributes.                                                                                                                                                   |
| PLUGIN\_AUTH\_LENENC\_CLIENT\_DATA      | 1 << 21 | Enable authentication response packet to be larger than 255 bytes.                                                                                                                   |
| CLIENT\_CAN\_HANDLE\_EXPIRED\_PASSWORDS | 1 << 22 | Client can handle expired passwords.                                                                                                                                                 |
| CLIENT\_SESSION\_TRACK                  | 1 << 23 | Enable/disable session tracking in `OK_Packet`.                                                                                                                                      |
| CLIENT\_DEPRECATE\_EOF                  | 1 << 24 | `EOF_Packet` deprecation: `OK_Packet` replace `EOF_Packet` at the end of the result set when in text format. `EOF_Packet` between columns definition and `resultsetRows` is deleted. |
| CLIENT\_OPTIONAL\_RESULTSET\_METADATA   | 1 << 25 | Not in use for MariaDB.                                                                                                                                                              |
| CLIENT\_ZSTD\_COMPRESSION\_ALGORITHM    | 1 << 26 | Support `zstd` protocol compression.                                                                                                                                                 |
| CLIENT\_CAPABILITY\_EXTENSION           | 1 << 29 | Reserved for future use.                                                                                                                                                             |
| CLIENT\_SSL\_VERIFY\_SERVER\_CERT       | 1 << 30 | Client verify server certificate. Deprecated, client has options to indicate if server certificate must be verified.                                                                  |
| CLIENT\_REMEMBER\_OPTIONS               | 1 << 31 |                                                                                                                                                                                      |
| MARIADB\_CLIENT\_PROGRESS               | 1 << 32 | Client support progress indicator.                                                                                                                                                   |
| MARIADB\_CLIENT\_COM\_MULTI             | 1 << 33 | Permit `COM_MULTI` protocol.                                                                                                                                                         |
| MARIADB\_CLIENT\_STMT\_BULK\_OPERATIONS | 1 << 34 | Permit bulk insert.                                                                                                                                                                  |
| MARIADB\_CLIENT\_EXTENDED\_METADATA     | 1 << 35 | Add extended metadata information.                                                                                                                                                   |
| MARIADB\_CLIENT\_CACHE\_METADATA        | 1 << 36 | Permit skipping metadata.                                                                                                                                                            |
| MARIADB\_CLIENT\_BULK\_UNIT\_RESULTS    | 1 << 37 | When enabled, indicate that bulk command can use `STMT_BULK_FLAG_SEND_UNIT_RESULTS` flag that permits to return a result set of all affected rows and auto-increment values.         |

## Native Password Authentication

The 20 byte string 'seed' is calculated by concatenating scramble first part (8 bytes) and scramble second part from [Initial handshake packet](connection.md#initial-handshake-packet). After that, the client calculates a password hash using the password and seed by using ^ (bitwise xor), + (string concatenation) and SHA1 as follows:

```
SHA1( passwd) ^ SHA1( seed + SHA1( SHA1( passwd ) ) )
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
