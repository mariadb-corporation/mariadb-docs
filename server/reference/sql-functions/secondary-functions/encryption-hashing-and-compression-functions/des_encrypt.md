---
description: >-
  Encrypt data using DES. This function encrypts a string using the Data
  Encryption Standard (DES) algorithm.
---

# DES\_ENCRYPT

{% hint style="warning" %}
`DES_ENCRYPT` is deprecated and will be removed in a future release.
{% endhint %}

## Syntax

```sql
DES_ENCRYPT(str[,{key_num|key_str}])
```

## Description

Encrypts the string with the given key using the Triple-DES algorithm.

This function works only if MariaDB has been configured with [TLS support](../../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md).

The encryption key to use is chosen based on the second argument to`DES_ENCRYPT()`, if one was given. With no argument, the first key from the DES key file is used. With a _`key_num`_ argument, the given key\
number (0-9) from the DES key file is used. With a _`key_str`_ argument, the given key string is used to encrypt _`str`_.

The key file can be specified with the `--des-key-file` server option.

The return string is a binary string where the first character is`CHAR(128 | key_num)`. If an error occurs, `DES_ENCRYPT()` returns `NULL`.

The 128 is added to make it easier to recognize an encrypted key. If you use a string key, _`key_num`_ is 127.

The string length for the result is given by this formula:

```sql
new_len = orig_len + (8 - (orig_len % 8)) + 1
```

Each line in the DES key file has the following format:

```sql
key_num des_key_str
```

Each _`key_num`_ value must be a number in the range from 0 to 9. Lines in the file may be in any order. _`des_key_str`_ is the string that is used to encrypt the message. There should be at least one space between the number and the key. The first key is the default key that is used if you do not specify any key argument to `DES_ENCRYPT()`.

You can tell MariaDB to read new key values from the key file with the `FLUSH DES_KEY_FILE` statement. This requires the RELOAD privilege.

One benefit of having a set of default keys is that it gives applications a way to check for the existence of encrypted column values, without giving the end user the right to decrypt those values.

## Examples

```sql
SELECT customer_address FROM customer_table 
   WHERE crypted_credit_card = DES_ENCRYPT('credit_card_number');
```

## See Also

* [DES\_DECRYPT()](des_decrypt.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
