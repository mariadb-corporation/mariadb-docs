---
description: >-
  This plugin implements the caching_sha2_password authentication method, using
  an in-memory cache for fast authentication or RSA encryption for full
  verification.
---

# Connecting via caching\_sha2\_password

## Overview

Caching `SHA256` first sends an `SHA256`-encrypted password. MySQL server has an in-memory cache of `SHA256` key for successful authentication. When a cache hit occurs, the connection is validated. Otherwise, authentication continues with additional steps similar to the [sha256\_password](sha256_password-plugin.md) process. The cache is MySQL server behavior. MariaDB Server does not cache and always requests full authentication.

Caching SHA256 authentication possible exchanges:

* Client sends an [SHA-2 encrypted password](caching_sha2_password-authentication-plugin.md#sha-2-encrypted-password).
* Server result is either [OK\_Packet](../4-server-response-packets/ok_packet.md), [ERR\_Packet](../4-server-response-packets/err_packet.md), or ["fast" authentication result](caching_sha2_password-authentication-plugin.md#fast-authentication-result).
* If the fast authentication result is `0x04` (full authentication required):
  * If the connection is secure (TLS is in use, or the transport is not TCP, such as a Unix socket):
    * Client sends a [clear password answer](caching_sha2_password-authentication-plugin.md#client-clear-password-answer).
  * Else:
    * If client doesn't know server RSA public key:
      * Client sends a [public key request](caching_sha2_password-authentication-plugin.md#public-key-request).
      * Server sends a [public key response](caching_sha2_password-authentication-plugin.md#public-key-response).
    * Client sends an [RSA encrypted password](caching_sha2_password-authentication-plugin.md#rsa-encrypted-password).
    * Ends with the server sending either an [OK\_Packet](../4-server-response-packets/ok_packet.md) or an [ERR\_Packet](../4-server-response-packets/err_packet.md).

## Authentication

### SHA-2 Encrypted Password

Encryption is `XOR`(`SHA256`(password), `SHA256`(`SHA256`(`SHA256`(password)), seed)).

* [byte<32>](../protocol-data-types.md#fixed-length-bytes) encrypted password.

### "Fast" Authentication Result

Result of fast authentication.

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed 0x01 value.
* [byte\<lenenc>](../protocol-data-types.md#length-encoded-bytes) authentication result.

`0x03` value means successful authentication.\
`0x04` value means continue.

### Client Clear Password Answer

* [string\<NUL>](../protocol-data-types.md#null-terminated-strings) password without encryption.

### Public Key Request

{% hint style="warning" %}
Value sent is not `0x01` like sha256\_password uses, but `0x02`.
{% endhint %}

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed 0x02 value.

### Public Key Response

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed 0x01 value.
* [byte\<EOF>](../protocol-data-types.md#end-of-file-length-bytes) public key data.

### RSA Encrypted Password

* [byte\<n>](../protocol-data-types.md#fixed-length-bytes) RSA encrypted password, where _n_ is the RSA key size in bytes (256 for a 2048-bit key).

RSA encrypted value of the password XORed with the seed, using the server public key (`RSA_PKCS1_OAEP_PADDING`). The password includes its terminating `NUL` byte. The seed is the raw 20-byte scramble sent by the server, repeated as needed: byte _i_ of the password is XORed with byte _i_ mod 20 of the seed. The seed is not hashed.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
