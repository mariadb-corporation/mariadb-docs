---
description: >-
  This plugin implements the caching_sha2_password authentication method, using
  an in-memory cache for fast authentication or RSA encryption for full
  verification.
---

# caching\_sha2\_password Authentication Plugin

## Overview

Caching `SHA256` first sends an `SHA256`-encrypted password.\
MySQL server has an in-memory cache of `SHA256` key for successful authentication. When a cache hit occurs, the connection is validated, if not, using some more steps to a process similar to [sha256\_password](sha256_password-plugin.md).

Caching SHA256 authentication possible exchanges:

* Client sends an [SHA-2 encrypted password](caching_sha2_password-authentication-plugin.md#sha-2-encrypted-password).
* Server result is either [OK\_Packet](../4-server-response-packets/ok_packet.md) , [ERR\_Packet](../4-server-response-packets/err_packet.md) or ["fast" authentication result](caching_sha2_password-authentication-plugin.md#fast-authentication-result).
* If fast authentication result:
  * If connection uses SSL ([SSLRequest](connection.md#sslrequest-packet) Packet sent):
    * Client sends a [clear password answer](caching_sha2_password-authentication-plugin.md#client-clear-password-answer).
  * Else:
    * If client doesn't know server RSA public key:
      * Client sends a [public key request](caching_sha2_password-authentication-plugin.md#public-key-request).
      * Server sends a [public key response](caching_sha2_password-authentication-plugin.md#public-key-response).
    * Client sends an [RSA encrypted password](caching_sha2_password-authentication-plugin.md#rsa-encrypted-password).
    * Ends with server sending either [OK\_Packet](../4-server-response-packets/ok_packet.md) , [ERR\_Packet](../4-server-response-packets/err_packet.md).

## Authentication

### SHA-2 encrypted password

Encryption is `XOR`(`SHA256`(password), `SHA256`(seed, `SHA256`(`SHA256`(password)))).

* [byte<32>](../protocol-data-types.md#fixed-length-bytes) encrypted password.

### "fast" authentication result

Result of fast authentication.

* [byte](../protocol-data-types.md#length-encoded-bytes) authentication result.

`0x03` value means success authentication.\
`0x04` value means continue.

### Client clear password answer

* [string](../protocol-data-types.md#null-terminated-strings) password without encryption.

### Public key request

{% hint style="warning" %}
Value send is not `0x01` like sha256\_password use, but `0x02`.
{% endhint %}

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed 0x02 value.

### Public key response

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed 0x01 value.
* [byte](../protocol-data-types.md#end-of-file-length-bytes) public key data.

### RSA encrypted password

* [byte<256>](../protocol-data-types.md#fixed-length-bytes) RSA encrypted password.

RSA encrypted value of `XOR`(password, seed) using server public key (`RSA_PKCS1_OAEP_PADDING`).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
