---
description: >-
  Encrypt data using AES. This function encrypts a string using the Advanced
  Encryption Standard (AES) algorithm and returns a binary string.
---

# AES\_ENCRYPT

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
AES_ENCRYPT(str, key, [, iv [, mode]])
```
{% endtab %}

{% tab title="< 11.2" %}
```sql
AES_ENCRYPT(str,key_str)
```
{% endtab %}
{% endtabs %}

## Description

`AES_ENCRYPT()` and [AES\_DECRYPT()](aes_decrypt.md) allow encryption and decryption of data using the official AES (Advanced Encryption Standard) algorithm, previously known as "Rijndael." Encoding with a 128-bit key length is used (from [MariaDB 11.2.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-0-release-notes), this is the default, and can be changed). 128 bits is much faster and is secure enough for most purposes.

`AES_ENCRYPT()` encrypts a string _`str`_ using the key _`key_str`_, and returns a binary string.

`AES_DECRYPT()` decrypts the encrypted string and returns the original string.

The input arguments may be any length. If either argument is `NULL`, the result of this function is also `NULL`.

Because AES is a block-level algorithm, padding is used to encode uneven length strings and so the result string length may be calculated using this formula:

```sql
16 x (trunc(string_length / 16) + 1)
```

If `AES_DECRYPT()` detects invalid data or incorrect padding, it returns `NULL`. However, it is possible for `AES_DECRYPT()` to return a non-`NULL` value (possibly garbage) if the input data or the key is invalid.

**MariaDB starting with** [**11.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-2-series/what-is-mariadb-112)

{% tabs %}
{% tab title="Current" %}
The function supports an initialization vector, and control of the block encryption mode. The default mode is specified by the [block\_encryption\_mode](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#block_encryption_mode) system variable, which can be changed when calling the function with a mode. _mode_ is aes-{128,192,256}-{ecb,cbc,ctr} for example: "AES-128-cbc".\
`AES_ENCRYPT(str, key)` can no longer be used in persistent virtual columns (and the like).
{% endtab %}

{% tab title="Tab 2" %}
The function does **not** support an initialization vector.
{% endtab %}
{% endtabs %}

## Examples

{% tabs %}
{% tab title="Current" %}
```sql
SELECT HEX(AES_ENCRYPT('foo', 'bar', '0123456789abcdef', 'aes-256-cbc')) AS x;
+----------------------------------+
| x                                |
+----------------------------------+
| 42A3EB91E6DFC40A900D278F99E0726E |
+----------------------------------+
```
{% endtab %}

{% tab title="< 11.2" %}
```sql
INSERT INTO t VALUES (AES_ENCRYPT('text',SHA2('password',512)));
```
{% endtab %}
{% endtabs %}

## See Also

* [RANDOM\_BYTES()](random_bytes.md) is a function for generating good encryption keys for `AES_ENCRYPT`.
* [KDF()](kdf.md) is a key derivation function which is useful if an authentication validation against the value is required without data being able to be decrypted.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
