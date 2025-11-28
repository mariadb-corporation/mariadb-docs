---
description: >-
  Decrypt data using DES. This function decrypts a string that was encrypted
  using the Data Encryption Standard (DES) algorithm.
---

# DES\_DECRYPT

{% hint style="warning" %}
`DES_DECRYPT` is deprecated and will be removed in a future release.
{% endhint %}

## Syntax

```sql
DES_DECRYPT(crypt_str[,key_str])
```

## Description

Decrypts a string encrypted with [DES\_ENCRYPT()](des_encrypt.md). If an error occurs, this function returns `NULL`.

This function works only if MariaDB has been configured with [TLS support](../../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md).

If no `key_str` argument is given, `DES_DECRYPT()` examines the first byte of the encrypted string to determine the DES key number that was used to encrypt the original string, and then reads the key from the DES key file to decrypt the message. For this to work, the user must have the SUPER privilege. The key file can be specified with the`--des-key-file` server option.

If you pass this function a <kbd>key\_str</kbd> argument, that string is used as the key for decrypting the message.

If the <kbd>crypt\_str</kbd> argument does not appear to be an encrypted string, MariaDB returns the given <kbd>crypt\_str</kbd>.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
