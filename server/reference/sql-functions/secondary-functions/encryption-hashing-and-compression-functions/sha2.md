---
description: >-
  Calculate SHA-2 checksum. This function computes the SHA-2 family of hash
  functions (SHA-224, SHA-256, SHA-384, and SHA-512).
---

# SHA2

## Syntax

```sql
SHA2(str,hash_len)
```

## Description

Given a string _`str`_, calculates an SHA-2 checksum, which is considered more cryptographically secure than its [SHA-1](sha1.md) equivalent. The SHA-2 family includes SHA-224, SHA-256, SHA-384, and SHA-512, and the _`hash_len`_ must correspond to one of these, i.e. 224, 256, 384 or 512. 0 is equivalent to 256.

The return value is a nonbinary string in the connection [character set and collation](../../../data-types/string-data-types/character-sets/), determined by the values of the [character\_set\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#character_set_connection) and [collation\_connection](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variables.

`NULL` is returned if the hash length is not valid, or the string `str` is `NULL`.

{% hint style="warning" %}
`SHA2` only works if MariaDB is configured with [TLS support](../../../../security/securing-mariadb/encryption/data-in-transit-encryption/secure-connections-overview.md).
{% endhint %}

## Examples

```sql
SELECT SHA2('Maria',224);
+----------------------------------------------------------+
| SHA2('Maria',224)                                        |
+----------------------------------------------------------+
| 6cc67add32286412efcab9d0e1675a43a5c2ef3cec8879f81516ff83 |
+----------------------------------------------------------+

SELECT SHA2('Maria',256);
+------------------------------------------------------------------+
| SHA2('Maria',256)                                                |
+------------------------------------------------------------------+
| 9ff18ebe7449349f358e3af0b57cf7a032c1c6b2272cb2656ff85eb112232f16 |
+------------------------------------------------------------------+

SELECT SHA2('Maria',0);
+------------------------------------------------------------------+
| SHA2('Maria',0)                                                  |
+------------------------------------------------------------------+
| 9ff18ebe7449349f358e3af0b57cf7a032c1c6b2272cb2656ff85eb112232f16 |
+------------------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
