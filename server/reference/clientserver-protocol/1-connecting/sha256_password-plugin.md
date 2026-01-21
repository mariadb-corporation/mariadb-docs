---
description: >-
  The sha256_password plugin manages authentication using SHA-256 encryption,
  supporting both clear text passwords over SSL and RSA encrypted password
  exchange.
---

# sha256\_password Plugin

## Overview

`SHA256` authentication possible exchanges:

* if connection use SSL (SSLRequest Packet sent):
  * Client sends a [clear password answer](sha256_password-plugin.md#client-clear-password-answer).
* Else:
  * If client doesn't know server RSA public key:
    * Client sends a [public key request](sha256_password-plugin.md#public-key-request).
    * Server sends a [public key response](sha256_password-plugin.md#public-key-response).
  * Client sends an [RSA encrypted password](sha256_password-plugin.md#rsa-encrypted-password).
  * Ends with server sending either [OK\_Packet](../4-server-response-packets/ok_packet.md) , [ERR\_Packet](../4-server-response-packets/err_packet.md).

## Authentication

### Client Clear Password Answer

* [string](../protocol-data-types.md#null-terminated-strings) password without encryption.

### Public key request

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed `0x01` value.

### Public key response

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) fixed `0x01` value.
* [byte](../protocol-data-types.md#end-of-file-length-bytes) public key data.

### RSA encrypted password

* [byte<256>](../protocol-data-types.md#fixed-length-bytes) RSA encrypted password.

RSA encrypted value of `XOR`(password, seed) using server public key (`RSA_PKCS1_OAEP_PADDING`).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
